#!/usr/bin/env python3
"""NikBench v1.0 — scorecard aggregator.

Turns judge scorecards (JSON) into a ranked leaderboard (markdown).

Usage:
    python scripts/aggregate.py <scorecards_dir> [--out FILE]
    python scripts/aggregate.py --selftest [<scorecards_dir>]

Scorecard schema: "nikbench.scorecard.v1" (see templates/scorecard.json and
judging/judge.md). Pure standard library; no dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "nikbench.scorecard.v1"

# criterion -> weight (points awarded = clamp(score, 0, 10) * weight)
WEIGHTS: dict[str, dict[str, float]] = {
    "reasoning": {
        "rigor": 2.0,
        "clarity": 2.0,
    },
    "frontend": {
        "functionality": 3.0,
        "visual_design": 2.5,
        "code_quality": 2.0,
        "accessibility": 1.5,
        "responsive": 1.0,
    },
    "backend": {
        "spec_correctness": 3.5,
        "security": 2.0,
        "validation_errors": 1.5,
        "data_modeling": 1.0,
        "design_answers": 1.5,
        "code_quality": 0.5,
    },
}

# sanity: each pillar's weighted criteria must top out at its max of 100
# (reasoning: 60 from exact_answers + 40 from weighted criteria; others: 100 only from weighted)
EXACT_POINTS_PER_PROBLEM = 6.0  # 10 problems * 6 = 60, plus rigor(20)+clarity(20) = 100
PILLAR_MAX = 100.0

for pillar, crits in WEIGHTS.items():
    max_points = sum(crits.values()) * 10.0
    expected = 40.0 if pillar == "reasoning" else 100.0
    if abs(max_points - expected) > 1e-9:
        raise SystemExit(f"internal error: {pillar} weighted max is {max_points}, expected {expected}")

GRADES = ((90.0, "S"), (80.0, "A"), (70.0, "B"), (60.0, "C"), (45.0, "D"))


def grade(overall: float) -> str:
    for floor, letter in GRADES:
        if overall >= floor:
            return letter
    return "F"


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


def _as_score(value) -> tuple[float, str]:
    """Return (score0to10, detail)."""
    if isinstance(value, dict):
        raw = value.get("score", 0)
        detail = str(value.get("detail", ""))[:200]
    else:
        raw, detail = value, ""
    try:
        score = float(raw)
    except (TypeError, ValueError):
        score = 0.0
    return max(0.0, min(10.0, score)), detail


def _as_correct_count(entry) -> float:
    if isinstance(entry, dict):
        raw = entry.get("correct_count", 0)
    else:
        raw = entry
    try:
        value = float(raw)
    except (TypeError, ValueError):
        value = 0.0
    return max(0.0, min(10.0, value))


def pillar_score(pillar: str, crits: dict) -> tuple[float, list[str]]:
    """Return (points out of 100, warnings)."""
    warnings: list[str] = []
    if not isinstance(crits, dict):
        return 0.0, [f"{pillar}: missing/invalid"]

    points = 0.0
    if pillar == "reasoning":
        points += _as_correct_count(crits.get("exact_answers", 0)) * EXACT_POINTS_PER_PROBLEM
    for name, weight in WEIGHTS[pillar].items():
        if name not in crits:
            warnings.append(f"{pillar}.{name}: missing -> 0")
            continue
        score, _ = _as_score(crits[name])
        points += weight * score
    if points > PILLAR_MAX + 1e-6:
        warnings.append(f"{pillar}: {points:.1f} above max, clamped")
        points = PILLAR_MAX
    return points, warnings


def parse_scorecard(path: Path) -> dict | None:
    obj = _extract_json(path.read_text(encoding="utf-8", errors="replace"))
    if not obj or not isinstance(obj.get("scores"), dict):
        return None
    return obj


def aggregate(cards: list[dict]) -> dict:
    """cards: validated scorecard dicts for ONE candidate."""
    per_judge = []
    all_flags: set[str] = set()
    for card in cards:
        scores = card.get("scores", {})
        pillars, flags = {}, []
        for pillar in ("reasoning", "frontend", "backend"):
            value, warns = pillar_score(pillar, scores.get(pillar, {}))
            pillars[pillar] = round(value, 2)
            flags.extend(warns)
        pillars["overall"] = round(sum(pillars[p] for p in ("reasoning", "frontend", "backend")) / 3.0, 2)
        for flag in card.get("flags", []):
            flags.append(f"judge:{card.get('judge_id', '?')}: {flag}")
        all_flags.update(flags)
        per_judge.append({"judge_id": card.get("judge_id", "unknown"), "pillars": pillars})

    medians = {
        p: round(statistics.median(j["pillars"][p] for j in per_judge), 2)
        for p in ("reasoning", "frontend", "backend")
    }
    overall = round(sum(medians.values()) / 3.0, 2)
    overalls = [j["pillars"]["overall"] for j in per_judge]
    spread = round(max(overalls) - min(overalls), 2) if overalls else 0.0
    outlier_judges = [j["judge_id"] for j in per_judge if abs(j["pillars"]["overall"] - statistics.median(overalls)) > 15.0]
    if outlier_judges:
        all_flags.add("judge outlier >15 from median overall: " + ", ".join(outlier_judges))
    return {"judges": per_judge, "medians": medians, "overall": overall, "spread": spread, "flags": sorted(all_flags)}


def render_leaderboard(results: list[tuple[str, dict]], updated) -> str:
    lines = [
        "# NikBench — Official Leaderboard",
        "",
        f"_Last updated: {updated} · scoring: `scripts/aggregate.py` · protocol: `docs/methodology.md`_",
        "",
        "| Rank | Model | NBS | Grade | Reasoning | Frontend | Backend | Judges | Spread |",
        "|---:|---|---:|:--:|---:|---:|---:|:--:|---:|",
    ]
    ranked = sorted(results, key=lambda kv: (-kv[1]["overall"], kv[1]["spread"], kv[0].lower()))
    for i, (name, res) in enumerate(ranked, 1):
        m = res["medians"]
        spread = res["spread"]
        lines.append(
            f"| {i} | **{name}** | {res['overall']:.2f} | {grade(res['overall'])} "
            f"| {m['reasoning']:.1f} | {m['frontend']:.1f} | {m['backend']:.1f} "
            f"| {len(res['judges'])} | ±{spread:.1f} |"
        )
    lines += [
        "",
        "## Grade scale",
        "",
        "| Grade | NBS | Meaning |",
        "|:--:|---:|---|",
        "| S | ≥ 90 | frontier: production-grade on all three pillars |",
        "| A | ≥ 80 | excellent, minor gaps |",
        "| B | ≥ 70 | solid generalist |",
        "| C | ≥ 60 | functional, notable gaps |",
        "| D | ≥ 45 | incomplete work on at least one pillar |",
        "| F | < 45 | failed to produce usable submissions |",
        "",
        "**NBS** = NikBench Score, 0–100, mean of the three pillar medians. `Spread` = range of per-judge overall scores; below 10.0 is healthy agreement, above 15.0 gets flagged for review.",
    ]
    return "\n".join(lines) + "\n"


def render_details(results: list[tuple[str, dict]]) -> str:
    out = []
    for name, res in results:
        out.append(f"### {name} — overall {res['overall']:.2f} ({grade(res['overall'])})")
        out.append("")
        out.append("| Judge | Reasoning | Frontend | Backend | Judge overall |")
        out.append("|---|---:|---:|---:|---:|")
        for j in res["judges"]:
            p = j["pillars"]
            out.append(
                f"| {j['judge_id']} | {p['reasoning']:.1f} | {p['frontend']:.1f} | {p['backend']:.1f} | {p['overall']:.1f} |"
            )
        if res["flags"]:
            out.append("")
            out.append("Flags:")
            for flag in res["flags"]:
                out.append(f"- {flag}")
        out.append("")
    return "\n".join(out)


def collect(scores_dir: Path) -> tuple[list[tuple[str, dict]], list[str]]:
    by_candidate: dict[str, list[dict]] = {}
    problems: list[str] = []
    files = sorted(scores_dir.rglob("*.json")) if scores_dir.is_dir() else []
    if not files:
        raise SystemExit(f"No scorecard JSON files found under {scores_dir}")
    for path in files:
        card = parse_scorecard(path)
        if card is None:
            problems.append(f"{path.name}: not a valid nikbench.scorecard.v1 object — skipped")
            continue
        cand = str(card.get("candidate_id") or "unknown")
        by_candidate.setdefault(cand, []).append(card)
    results = [(cand, aggregate(cards)) for cand, cards in by_candidate.items()]
    return results, problems


def selftest(scores_dir: Path) -> int:
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
    fixture = "junk```json\n" + json.dumps({"b": {"c": '"x{"'}}) + "\n```"
    fenced = _extract_json(fixture)
    assert fenced == {"b": {"c": '"x{"'}}
    print(f"SELFTEST OK — {len(results)} candidate(s), {sum(1 for _, r in results for _j in r['judges'])} judge cards parsed")
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
    parser.add_argument("--selftest", action="store_true", help="validate examples and exit")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest(args.scores_dir)

    results, problems = collect(args.scores_dir if args.scores_dir.is_dir() else Path("examples/scorecards") if (Path("examples/scorecards")).is_dir() else args.scores_dir)
    for problem in problems:
        print(f"WARNING: {problem}", file=sys.stderr)

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    board = render_leaderboard(results, updated)
    board += "\n\n<details>\n<summary><b>Per-judge details</b> (click to expand)</summary>\n\n" + render_details(results) + "\n</details>\n" if results else ""

    if args.out:
        args.out.write_text(board, encoding="utf-8")
        print(f"wrote {args.out}")
    print(board)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
