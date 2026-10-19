"""Insert or refresh the VIS showcase in README.md from gallery/_book.json.

Run after `python scripts/build_gallery.py`.
"""
import ast
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

book = ast.literal_eval(Path("gallery/_book.json").read_text(encoding="utf-8"))
readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")

WIDTHS = {"V1": 210, "V2": 330, "V3": 330, "V4": 330, "V5": 210, "V6": 330, "V7": 420}
TASK_BLURB = {
    "V1": ("V1 — Mona Lisa in ≤300 SVG shapes",
           "Blind art fidelity: painters pose, folded hands, sfumato smile, from a text "
           "spec with no reference image. Peer-judged for recognizability and craft."),
    "V2": ("V2 — Seven Founders infographic (1200×700)",
           "Fixed roster — Lovelace · Turing · von Neumann · Shannon · Hopper · Dijkstra · "
           "Knuth — on a *to-scale* 1800–2000 timeline. Wrong facts or wrong spacing = lost points."),
    "V3": ("V3 — LIFTOFF: 60-second motion loop (HTML/CSS)",
           "A 60-second animated web “video” with 4 timed beats. GitHub sandboxes scripts, "
           "so open these files in a browser to watch them loop — they are the real deliverables."),
    "V4": ("V4 — Café revenue chart with an honesty trap (900×500)",
           "Same CSV for every model. The trap: noise invites a big “trend”, the truth is a "
           "renovation effect ≈ nil and a single festival outlier at month 19. Reward goes to "
           "models that decompose instead of dramatize."),
    "V5": ("V5 — Eiffel Tower architectural elevation (hard tier, 600×900)",
           "To-scale engineering: platforms pinned at 57 / 115 / 276 m on a linear height map, "
           "≥40 visible lattice elements, and an in-SVG annotation block. Judges measure the "
           "y-coordinates — a pretty silhouette with wrong decks loses."),
    "V6": ("V6 — Taj Mahal bilateral symmetry (hard tier, 900×600)",
           "One mirrored `<g>` half, true about x = 450 within 1 px, four separate minarets, "
           "dome taller than the towers, pool reflection. The round's sharpest failure mode: "
           "mirrored groups that land on the same side and leave the façade one-sided."),
    "V7": ("V7 — Earth colour system (hard tier, 1200×800)",
           "A design-system board, not a poster: an Earth disc built only from eight fixed "
           "tokens, eight swatch cards, a WCAG 2.1 contrast block with ratios to two decimals, "
           "a 60-30-10 bar, and a type hierarchy. Judges recompute every contrast ratio."),
    "F1": ("Bonus — F1 Mission Control (single-file dashboard)",
           "The frontend task is visual too: a 10-requirement dashboard app. Open the real files."),
}


def top_three() -> str:
    rows = book.get("V1") or []
    return ", ".join(f"{model.replace('-free', '')} **{score:.1f}**" for model, _path, score in rows[:3])


def build_section() -> str:
    lines = [
        "## 🖼️ Visual showcase — what the models actually made",
        "",
        "The VIS pillar is scored on what a model *draws, animates, and charts* — not what it "
        f"describes. GitHub renders SVG in color; the curation below is the three strongest VIS "
        f"builds of the round by peer vote ({top_three()} /100 from the non-self reviewers). "
        "Regenerate with `python scripts/build_gallery.py` then `python scripts/insert_showcase.py`.",
        "",
    ]
    for task in ("V1", "V2", "V3", "V4", "V5", "V6", "V7", "F1"):
        title, blurb = TASK_BLURB[task]
        lines += [f"### {title}", "", blurb, ""]
        rows = book.get(task, [])
        if not rows:
            lines += ["_(no render — missing section in every submission)_", ""]
            continue
        if task in ("V3", "F1"):
            lines += ["| Model | Open in browser (GitHub won't run it) | Peer VIS /100 |",
                      "|---|---|---:|"]
            for model, path, score in rows:
                lines.append(f"| **{model.replace('-free', '')}** | [`{path}`]({path}) | {score} |")
        else:
            lines += ["| Model | Render (in color, straight from the submission) | Peer VIS /100 |",
                      "|---|---|---:|"]
            width = WIDTHS[task]
            for model, path, score in rows:
                alt = f"{model} {task}"
                lines.append(f"| **{model.replace('-free', '')}** "
                             f"| <img src=\"{path}\" alt=\"{alt}\" width=\"{width}\"> | {score} |")
        lines.append("")
    lines += [
        "_Full raw builds live in `submissions/` between rounds; the renders above are extracted "
        "verbatim by `scripts/build_gallery.py` — no retouching. Per-model live BE/FE numbers are "
        "in the live column of the board above._",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


section = build_section()
anchor = "## 🗂️ Repository map"
header = "## 🖼️ Visual showcase"
if header in readme:
    start = readme.index(header)
    end = readme.index(anchor, start)
    readme = readme[:start] + section + "\n" + readme[end:]
else:
    idx = readme.index(anchor)
    readme = readme[:idx] + section + "\n" + readme[idx:]

# add the gallery bullet to the repo map when it is missing
if "[`gallery/`](gallery)" not in readme:
    readme = readme.replace(
        "- [`leaderboard.md`](leaderboard.md)",
        "- [`gallery/`](gallery)\n- [`leaderboard.md`](leaderboard.md)",
        1,
    )

readme_path.write_text(readme, encoding="utf-8")
print("showcase refreshed — README now matches gallery/_book.json")
