#!/usr/bin/env python3
"""NikBench — scorecard aggregator (v2.0).

Turns judge scorecards (JSON) into a ranked leaderboard (markdown), optionally
merging the peer-review round (`peer/*.md`, schema nikbench.peer.v1) and each
model's self-rating into a Final score.

Usage:
    python scripts/aggregate.py [scorecards_dir] [--out FILE] [--peer-dir DIR]
    python scripts/aggregate.py --selftest [scorecards_dir]

Scoring:
    Pillar = 0–100 per pillar per judge (weighted criteria; `rat` adds 60 exact-answer pts)
    NBS    = weighted mean over the six pillars of (median across judges of pillar score)
    Peer   = mean of other models' Overall ratings for this candidate (×10)   0–100
    Self   = the candidate's own Overall rating of itself                (×10) 0–100
    Final  = 0.6·NBS + 0.2·Peer + 0.2·Self (missing parts redistribute evenly)

Pillars (v2.0): rat (ratiocination), tho (thought), vis (visual craft),
alg (algorithm design), fe (frontend), be (backend).

Pure standard library; no dependencies.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "nikbench.scorecard.v1"
PEER_SCHEMA = "nikbench.peer.v1"

# criterion -> weight (points awarded = clamp(score, 0, 10) * weight)
WEIGHTS: dict[str, dict[str, float]] = {
    "rat": {  # ratiocination: exact answers (60 pts, correct_count x 6) + weighted criteria (40 pts)
        "rigor": 2.0,
        "clarity": 2.0,
    },
    "tho": {  # thought — open problems; graded on the quality & honesty of thinking
        "comprehension": 2.0,
        "synthesis": 2.0,
        "originality": 2.0,
        "argument_rigor": 2.5,
        "intellectual_candor": 1.5,
    },
    "vis": {  # visual craft: v1 art + v2 infographic + v3 motion + v4 data-viz
        "art_fidelity": 1.0,
        "art_craft": 1.0,
        "infographic_facts": 1.5,
        "infographic_design": 1.5,
        "motion_design": 1.5,
        "motion_timing": 1.0,
        "dataviz_choice": 1.0,
        "dataviz_honesty": 1.5,
    },
    "alg": {  # algorithm design
        "correctness": 3.0,
        "complexity_analysis": 2.5,
        "edge_cases": 1.5,
        "communication": 1.5,
        "innovation": 1.5,
    },
    "fe": {  # frontend
        "functionality": 3.0,
        "visual_design": 2.5,
        "code_quality": 2.0,
        "accessibility": 1.5,
        "responsive": 1.0,
    },
    "be": {  # backend
        "spec_correctness": 3.5,
        "security": 2.0,
        "validation_errors": 1.5,
        "data_modeling": 1.0,
        "design_answers": 1.5,
        "code_quality": 0.5,
    },
}

# sanity: each pillar's weighted criteria must top out at its max of 100
# (rat: 60 from exact_answers + 40 from weighted criteria; the rest: 100 only from weighted)
EXACT_POINTS_PER_PROBLEM = 6.0  # 10 problems * 6 = 60, plus rigor(20)+clarity(20) = 100
EXACT_PILLAR = "rat"
PILLAR_MAX = 100.0

# how much each pillar counts toward a candidate's overall NBS
PILLAR_WEIGHTS: dict[str, float] = {
    "rat": 0.20,
    "tho": 0.20,
    "vis": 0.15,
    "alg": 0.15,
    "fe": 0.15,
    "be": 0.15,
}

for pillar, crits in WEIGHTS.items():
    max_points = sum(crits.values()) * 10.0
    expected = 40.0 if pillar == EXACT_PILLAR else 100.0
    if abs(max_points - expected) > 1e-9:
        raise SystemExit(f"internal error: {pillar} weighted max is {max_points}, expected {expected}")
if abs(sum(PILLAR_WEIGHTS.values()) - 1.0) > 1e-9:
    raise SystemExit("internal error: pillar weights must sum to 1.0")

GRADES = ((90.0, "S"), (80.0, "A"), (70.0, "B"), (60.0, "C"), (45.0, "D"))

PILLARS = ("rat", "tho", "vis", "alg", "fe", "be")


def grade(score: float) -> str:
    for floor, letter in GRADES:
        if score >= floor:
            return letter
    return "F"


# ---------------------------------------------------------------- scorecards


def _extract_json(text: str) -> dict | None:
    """Parse a scorecard that may be wrapped in prose or a ```json fence."""
    text = text.strip()
    try:
        obj = json.loads(text)
        return obj if isinstance(obj, dict) else None
    except (json.JSONDecodeError, ValueError):
        pass
    # find first balanced {...} block, ignoring braces inside strings
    depths = 0
    start = -1
    in_str = False
    esc = False
    for i, ch in enumerate(text):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            if depths == 0:
                start = i
            depths += 1
        elif ch == "}":
            if depths == 0:
                continue
            depths -= 1
            if depths == 0 and start >= 0:
                try:
                    obj = json.loads(text[start : i + 1])
                    if isinstance(obj, dict):
                        return obj
                except (json.JSONDecodeError, ValueError):
                    start = -1
    return None


def _extract_last_json(text: str, require_schema: str | None = None) -> dict | None:
    """Parse the last schema-valid JSON object in a mixed markdown+json file.

    Scans candidate starts ('{' chars) from last to first; for each start, walks
    candidate ends ('}' chars) from last to first until a loadable, schema-valid
    object is found. This survives fence tails, leaked scaffolding, or prose
    after the block (any junk containing stray braces).
    """
    starts = [i for i, ch in enumerate(text) if ch == "{"]
    ends = [i for i, ch in enumerate(text) if ch == "}"]
    for start in reversed(starts):
        pos_ends = [e for e in reversed(ends) if e > start]
        for cap, end in enumerate(pos_ends[:200]):
            try:
                obj = json.loads(text[start : end + 1])
            except (json.JSONDecodeError, ValueError):
                continue
            if isinstance(obj, dict):
                if require_schema is None or obj.get("schema") == require_schema:
                    return obj
                break  # a smaller-but-valid dict can still envelope our target
    return None


def _as_score(value) -> float:
    if isinstance(value, dict):
        value = value.get("score", 0)
    try:
        return max(0.0, min(10.0, float(value)))
    except (TypeError, ValueError):
        return 0.0


def _as_correct_count(entry) -> float:
    raw = entry.get("correct_count", 0) if isinstance(entry, dict) else entry
    try:
        return max(0.0, min(10.0, float(raw)))
    except (TypeError, ValueError):
        return 0.0


def pillar_score(pillar: str, crits: dict) -> tuple[float, list[str]]:
    """Return (points out of 100, warnings)."""
    warnings: list[str] = []
    if not isinstance(crits, dict):
        return 0.0, [f"{pillar}: missing/invalid"]

    points = 0.0
    if pillar == EXACT_PILLAR:
        points += _as_correct_count(crits.get("exact_answers", 0)) * EXACT_POINTS_PER_PROBLEM
    for name, weight in WEIGHTS[pillar].items():
        if name not in crits:
            warnings.append(f"{pillar}.{name}: missing -> 0")
            continue
        points += weight * _as_score(crits[name])
    if points > PILLAR_MAX + 1e-6:
        warnings.append(f"{pillar}: {points:.1f} above max, clamped")
        points = PILLAR_MAX
    return points, warnings


def _salvage_scorecard(text: str) -> dict | None:
    """Rebuild a scorecard from a broken (e.g. unescaped inner quotes) JSON dump.

    Extracts judge_id/candidate_id and every verbatim score value per the rigid
    v1 schema shape; prose details are not recoverable reliably and get a
    salvage note instead. Never invents a score: criteria missing from the raw
    text are recorded as 0 with a salvage note.
    """
    import re
    idx = []
    for p in PILLARS:
        found = re.search(rf'"{p}"\s*:\s*\{{', text)
        idx.append((found.start() if found else -1, p))
    located = [(i, p) for i, p in idx if i >= 0]
    if not located:
        return None
    located.sort()
    scores: dict[str, dict] = {}
    for k, (i, pillar) in enumerate(located):
        end = located[k + 1][0] if k + 1 < len(located) else len(text)
        seg = text[i:end]
        pillar_scores: dict = {}
        if pillar == EXACT_PILLAR:
            m = re.search(r'"correct_count"\s*:\s*([0-9.]*)', seg)
            pillar_scores["exact_answers"] = {
                "correct_count": float(m.group(1)) if m and m.group(1) else 0.0,
                "detail": "salvaged: detail text unrecoverable, value verbatim",
            }
        for crit in WEIGHTS[pillar]:
            m = re.search(rf'"{re.escape(crit)}"\s*:\s*\{{[^{{}}]*?"score"\s*:\s*([0-9.]+)', seg)
            pillar_scores[crit] = {
                "score": float(m.group(1)) if m else 0.0,
                "detail": "salvaged: detail text unrecoverable" if m else "salvage: criterion not found in raw card (0)",
            }
        scores[pillar] = pillar_scores
    mjudge = re.search(r'"judge_id"\s*:\s*"([^"]*)"', text)
    mcand = re.search(r'"candidate_id"\s*:\s*"([^"]*)"', text)
    flags: list[str] = ["parser-salvaged: original card had invalid JSON (likely unescaped quotes); every score value below extracted verbatim from the raw judge output"]
    mflags = re.search(r'"flags"\s*:\s*\[(.*?)\]', text, re.S)
    if mflags:
        for f in re.findall(r'"([^"]+)"', mflags.group(1)):
            flags.append(f"judge said: {f}")
    return {"schema": SCHEMA, "judge_id": mjudge.group(1) if mjudge else "unknown",
            "candidate_id": mcand.group(1) if mcand else "unknown",
            "scores": scores, "flags": flags}


def parse_scorecard(path: Path) -> dict | None:
    obj = _extract_json(path.read_text(encoding="utf-8", errors="replace"))
    if not obj or not isinstance(obj.get("scores"), dict):
        obj = _salvage_scorecard(path.read_text(encoding="utf-8", errors="replace"))
    if not obj or not isinstance(obj.get("scores"), dict):
        return None
    return obj


def aggregate(cards: list[dict]) -> dict:
    """cards: validated scorecard dicts for ONE candidate -> NBS + judge details."""
    per_judge = []
    all_flags: set[str] = set()
    for card in cards:
        scores = card.get("scores", {})
        pillars, flags = {}, []
        for pillar in PILLARS:
            value, warns = pillar_score(pillar, scores.get(pillar, {}))
            pillars[pillar] = round(value, 2)
            flags.extend(warns)
        pillars["overall"] = round(sum(PILLAR_WEIGHTS[p] * pillars[p] for p in PILLARS), 2)
        for flag in card.get("flags", []):
            flags.append(f"judge:{card.get('judge_id', '?')}: {flag}")
        all_flags.update(flags)
        per_judge.append({"judge_id": card.get("judge_id", "unknown"), "pillars": pillars})

    medians = {
        p: round(statistics.median(j["pillars"][p] for j in per_judge), 2)
        for p in PILLARS
    }
    overall = round(sum(PILLAR_WEIGHTS[p] * medians[p] for p in PILLARS), 2)
    overalls = [j["pillars"]["overall"] for j in per_judge]
    spread = round(max(overalls) - min(overalls), 2) if overalls else 0.0
    outlier_judges = [
        j["judge_id"] for j in per_judge
        if abs(j["pillars"]["overall"] - statistics.median(overalls)) > 15.0
    ]
    if outlier_judges:
        all_flags.add("judge outlier >15 from median overall: " + ", ".join(outlier_judges))
    return {"judges": per_judge, "medians": medians, "overall": overall,
            "spread": spread, "flags": sorted(all_flags)}


# ---------------------------------------------------------------- peer round


def parse_peer_file(path: Path) -> tuple[str, dict[str, dict]] | None:
    """Return (reviewer_id, {model: rating}) or None."""
    text = path.read_text(encoding="utf-8", errors="replace")
    obj = _extract_last_json(text, PEER_SCHEMA)
    if not obj or obj.get("schema") != PEER_SCHEMA:
        return None
    reviewer = str(obj.get("reviewer") or path.stem)
    raw = obj.get("ratings")
    if isinstance(raw, dict):
        items = list(raw.items())
    elif isinstance(raw, list):
        items = []
        for entry in raw:
            if isinstance(entry, dict):
                name = str(entry.get("model") or entry.get("name") or "unknown")
                items.append((name, entry))
    else:
        items = []
    ratings: dict[str, dict] = {}
    for model, rating in items:
        if not isinstance(rating, dict):
            continue
        values = {}
        for key in ("rat", "tho", "vis", "alg", "fe", "be", "overall"):
            try:
                values[key] = max(0.0, min(10.0, float(rating.get(key, 0))))
            except (TypeError, ValueError):
                values[key] = 0.0
        values["self"] = bool(rating.get("self", model == reviewer))
        ratings[str(model)] = values
    if not ratings:
        return None
    return reviewer, ratings


def collect_peer(peer_dir: Path) -> tuple[dict[str, dict], list[str]]:
    """Return (stats per candidate, problems). stats: peer100/self100/votes/self_votes."""
    stats: dict[str, dict] = {}
    problems: list[str] = []
    files = sorted(p for p in peer_dir.glob("*.md") if p.name != "README.md")
    for path in files:
        parsed = None
        try:
            parsed = parse_peer_file(path)
        except Exception as exc:  # noqa: BLE001 — a bad peer file must never crash the board
            problems.append(f"{path.name}: unreadable/unparseable ({type(exc).__name__})")
        if parsed is None:
            problems.append(f"{path.name}: no valid {PEER_SCHEMA} json block found")
            continue
        reviewer, ratings = parsed
        for model, rating in ratings.items():
            entry = stats.setdefault(model, {"peer_votes": [], "self_vote": None})
            if bool(rating["self"]) or reviewer == model:
                if entry["self_vote"] is None or reviewer == model:
                    entry["self_vote"] = rating["overall"] * 10.0
            else:
                entry["peer_votes"].append(rating["overall"] * 10.0)
    out: dict[str, dict] = {}
    for model, entry in stats.items():
        peer100 = round(statistics.mean(entry["peer_votes"]), 2) if entry["peer_votes"] else None
        self100 = round(entry["self_vote"], 2) if entry["self_vote"] is not None else None
        out[model] = {"peer100": peer100, "self100": self100,
                      "n_peer_votes": len(entry["peer_votes"]), "has_self": entry["self_vote"] is not None}
    return out, problems


def final_score(nbs: float | None, peer100: float | None, self100: float | None) -> float | None:
    """0.6/0.2/0.2 blend; missing components redistribute weight evenly."""
    parts = []
    if nbs is not None:
        parts.append((0.6, nbs))
    if peer100 is not None:
        parts.append((0.2, peer100))
    if self100 is not None:
        parts.append((0.2, self100))
    if not parts:
        return None
    weight_sum = sum(w for w, _ in parts)
    return round(sum(w * v for w, v in parts) / weight_sum, 2)


# ---------------------------------------------------------------- rendering


def render_leaderboard(results, updated: str, peer: dict[str, dict] | None = None) -> str:
    merged = []
    for name, res in results:
        peer100 = self100 = None
        if peer and name in peer:
            peer100 = peer[name].get("peer100")
            self100 = peer[name].get("self100")
        final = final_score(res["overall"], peer100, self100)
        merged.append((name, res, peer100, self100, final))

    scoring_key = "final" if peer is not None else "overall"
    ranked = sorted(
        merged,
        key=lambda t: (-(t[4] if t[4] is not None else (t[1]["overall"] if t[1]["overall"] is not None else 0.0)),
                       t[1]["spread"], t[0].lower()),
    )

    if peer is not None:
        lines = [
            "# NikBench — Official Leaderboard",
            "",
            f"_Last updated: {updated} · scorer: `scripts/aggregate.py` · protocol: `docs/methodology.md`_",
            "",
            "| Rank | Model | Final | Grade | NBS | Peer | Self | RAT | THO | VIS | ALG | FE | BE | Judges | Spread |",
            "|---:|---|---:|:--:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:--:|---:|",
        ]
        for i, (name, res, peer100, self100, final) in enumerate(ranked, 1):
            m = res["medians"]
            peer_cell = f"{peer100:.1f}" if peer100 is not None else "—"
            self_cell = f"{self100:.1f}" if self100 is not None else "—"
            nbs_cell = f"{res['overall']:.1f}" if res["overall"] is not None else "—"
            pillar_cells = " | ".join(
                f"{m[p]:.0f}" if res["judges"] else "—" for p in PILLARS
            )
            key_score = final if final is not None else res["overall"]
            key_cell = f"{key_score:.2f}" if key_score is not None else "—"
            key_grade = grade(key_score) if key_score is not None else "—"
            lines.append(
                f"| {i} | **{name}** | {key_cell} | {key_grade} "
                f"| {nbs_cell} | {peer_cell} | {self_cell} "
                f"| {pillar_cells} "
                f"| {len(res['judges'])} | ±{res['spread']:.1f} |"
            )
        legend = (
            "**NBS** = rubric-judge score (weighted across the 6 pillar medians) · **Peer** = mean of the other models' ratings · "
            "**Self** = the model's own rating of itself (last, by design) · **Final** = `0.6·NBS + 0.2·Peer + 0.2·Self`. "
            "Pillars: **RAT** ratiocination · **THO** thought · **VIS** visual · **ALG** algorithms · **FE** frontend · **BE** backend. "
            "Grades follow **Final** when peer data exists."
        )
    else:
        lines = [
            "# NikBench — Official Leaderboard",
            "",
            f"_Last updated: {updated} · scoring: `scripts/aggregate.py` · protocol: `docs/methodology.md`_",
            "",
            "| Rank | Model | NBS | Grade | RAT | THO | VIS | ALG | FE | BE | Judges | Spread |",
            "|---:|---|---:|:--:|---:|---:|---:|---:|---:|---:|:--:|---:|",
        ]
        for i, (name, res, _p, _s, _f) in enumerate(ranked, 1):
            m = res["medians"]
            pillar_cells = " | ".join(f"{m[p]:.1f}" for p in PILLARS)
            lines.append(
                f"| {i} | **{name}** | {res['overall']:.2f} | {grade(res['overall'])} "
                f"| {pillar_cells} "
                f"| {len(res['judges'])} | ±{res['spread']:.1f} |"
            )
        legend = (
            "**NBS** = NikBench Score, 0–100, the pillar-weighted mean of the six pillar medians. "
            "`Spread` = range of per-judge overall scores; below 10.0 is healthy agreement, "
            "above 15.0 gets flagged for review."
        )

    lines += [
        "",
        "## Grade scale",
        "",
        "| Grade | Score | Meaning |",
        "|:--:|---:|---|",
        "| S | ≥ 90 | frontier: production-grade on all six pillars |",
        "| A | ≥ 80 | excellent, minor gaps |",
        "| B | ≥ 70 | solid generalist |",
        "| C | ≥ 60 | functional, notable gaps |",
        "| D | ≥ 45 | incomplete work on at least one pillar |",
        "| F | < 45 | failed to produce usable submissions |",
        "",
        legend,
    ]
    return "\n".join(lines) + "\n"


def render_details(results) -> str:
    out = []
    for name, res in results:
        if not res["judges"]:
            continue
        out.append(f"### {name} — NBS {res['overall']:.2f} ({grade(res['overall'])})")
        out.append("")
        out.append("| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |")
        out.append("|---|---:|---:|---:|---:|---:|---:|---:|")
        for j in res["judges"]:
            p = j["pillars"]
            cells = " | ".join(f"{p[p_key]:.1f}" for p_key in PILLARS)
            out.append(
                f"| {j['judge_id']} | {cells} | {p['overall']:.1f} |"
            )
        if res["flags"]:
            out.append("")
            out.append("Flags:")
            for flag in res["flags"]:
                out.append(f"- {flag}")
        out.append("")
    return "\n".join(out)


def render_peer_notes(peer: dict[str, dict]) -> str:
    lines = ["### Peer-round notes", ""]
    for name, entry in sorted(peer.items()):
        bits = []
        if entry["peer100"] is not None:
            bits.append(f"peer {entry['peer100']:.1f}/100 from {entry['n_peer_votes']} reviewer(s)")
        if entry["has_self"]:
            bits.append(f"self {entry['self100']:.1f}/100")
        lines.append(f"- **{name}**: " + ", ".join(bits) if bits else f"- **{name}**: no ratings")
    return "\n".join(lines) + "\n"


def collect(scores_dir: Path) -> tuple[list[tuple[str, dict]], list[str]]:
    by_candidate: dict[str, list[dict]] = {}
    problems: list[str] = []
    files = sorted(scores_dir.rglob("*.json"))
    if not files:
        return [], [f"no scorecard JSON files under {scores_dir}"]
    for path in files:
        card = parse_scorecard(path)
        if card is None:
            problems.append(f"{path.name}: not a valid {SCHEMA} object — skipped")
            continue
        cand = str(card.get("candidate_id") or "unknown")
        by_candidate.setdefault(cand, []).append(card)
    results = [(cand, aggregate(cards)) for cand, cards in by_candidate.items()]
    return results, problems


def selftest(scores_dir: Path, peer_dir: Path | None = None) -> int:
    results, problems = collect(scores_dir)
    assert results, "selftest: no candidates parsed"
    for name, res in results:
        for pillar, value in res["medians"].items():
            assert 0.0 <= value <= 100.0, f"{name}: {pillar} out of range: {value}"
        assert 0.0 <= res["overall"] <= 100.0
        assert res["judges"], f"{name}: no judges"
    ok = render_leaderboard(results, "selftest")
    assert "| Rank | Model |" in ok and grade(95) == "S" and grade(10) == "F"
    broken = _extract_json("```json\n{\"a\": 1\n```\n")
    assert broken is None
    fenced = _extract_json("junk```json\n" + json.dumps({"b": {"c": '"x{"'}}) + "\n```")
    assert fenced == {"b": {"c": '"x{"'}}

    # peer parsing + final-score blend
    assert final_score(70, None, None) == 70
    assert final_score(70, 80, None) == 72.5
    assert final_score(70, 80, 70) == 72.0
    sample = (
        "# Peer review by rev-x\n\n| Model | RAT | THO | VIS | ALG | FE | BE | O | why |\n|---|---:|---:|---:|---:|---:|---:|---:|---|\n"
        "| good | 8 | 8 | 8 | 8 | 8 | 8 | 8 | ok |\n\n```json\n" + json.dumps({
            "schema": PEER_SCHEMA,
            "reviewer": "rev-x",
            "ratings": {"good": {"rat": 8, "tho": 8, "vis": 8, "alg": 8, "fe": 8, "be": 8, "overall": 8, "self": False},
                        "rev-x": {"rat": 9, "tho": 9, "vis": 9, "alg": 9, "fe": 9, "be": 9, "overall": 9, "self": True}},
        }) + "\n```"
    )
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp) / "rev-x.md"
        tmp_path.write_text(sample, encoding="utf-8")
        peer, _problems = collect_peer(tmp_path.parent)
    assert peer["good"]["peer100"] == 80.0 and peer["good"]["has_self"] is False
    assert peer["rev-x"]["self100"] == 90.0
    board2 = render_leaderboard(results, "selftest", peer)
    assert "| Final |" in board2 and "| Peer |" in board2

    n_judges = sum(len(r["judges"]) for _n, r in results)
    print(f"SELFTEST OK — {len(results)} candidate(s), {n_judges} judge cards parsed, peer blending verified")
    print(render_details(results))
    return 0


def main(argv: list[str] | None = None) -> int:
    # Windows consoles default to legacy codepages; make stdout tolerant of ≥/·/± in the board
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

    parser = argparse.ArgumentParser(description="NikBench scorecard aggregator")
    parser.add_argument("scores_dir", nargs="?", default="scorecards", type=Path)
    parser.add_argument("--out", "-o", type=Path, default=None)
    parser.add_argument("--peer-dir", "-p", type=Path, default="peer", help="directory of peer-review files; pass 'none' to skip")
    parser.add_argument("--selftest", action="store_true", help="validate examples and peer blending, then exit")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest(args.scores_dir, args.peer_dir)

    results, problems = collect(args.scores_dir)
    for problem in problems:
        print(f"WARNING: {problem}", file=sys.stderr)

    peer = None
    peer_problems: list[str] = []
    if args.peer_dir and args.peer_dir.is_dir():
        peer, peer_problems = collect_peer(args.peer_dir)
        for problem in peer_problems:
            print(f"WARNINGpeer: {problem}", file=sys.stderr)
        if peer:
            results.sort(key=lambda t: t[0].lower())
        else:
            peer = None

    if not results and not peer:
        raise SystemExit(
            "Nothing to aggregate: no scorecard JSONs found and no peer-review files."
        )

    # peer-only candidates (a run where no rubric judge got to grade someone)
    if peer:
        scored_names = {name for name, _ in results}
        for cand in sorted(set(peer) - scored_names):
            results.append((cand, {
                "judges": [], "medians": {}, "overall": None,
                "spread": 0.0, "flags": ["no rubric judge covered this candidate"],
            }))
        results.sort(key=lambda t: t[0].lower())

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    board = render_leaderboard(results, updated, peer)
    if peer:
        board += "\n<details>\n<summary><b>Peer-round notes</b></summary>\n\n" + render_peer_notes(peer) + "\n</details>\n\n"
    board += "\n<details>\n<summary><b>Per-judge details</b> (click to expand)</summary>\n\n" + render_details(results) + "\n</details>\n"

    if args.out:
        args.out.write_text(board, encoding="utf-8")
        print(f"wrote {args.out}")
    print(board)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
