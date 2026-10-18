"""Insert the VIS showcase section into README.md from gallery/_book.json."""
import ast
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

book = ast.literal_eval((Path("gallery/_book.json")).read_text(encoding="utf-8"))
readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")

WIDTHS = {"V1": 210, "V2": 330, "V3": 330, "V4": 330}
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
    "F1": ("Bonus — F1 Mission Control (single-file dashboard)",
           "The frontend task is visual too: a 10-requirement dashboard app. Open the real files."),
}


def build_section() -> str:
    lines = [
        "## 🖼️ Visual showcase — what the models actually made",
        "",
        "The VIS pillar is scored on what a model *draws, animates, and charts* — not what it "
        "describes. GitHub renders SVG in color; round-1 curation is the three strongest VIS "
        "builds by peer vote (space-bunny-free **81.4**, big-pickle **80.7**, glm "
        "**78.6** /100 from the 7 non-self reviewers). Regenerate after any round: "
        "`python scripts/build_gallery.py`.",
        "",
    ]
    for task in ("V1", "V2", "V3", "V4", "F1"):
        title, blurb = TASK_BLURB[task]
        lines += [f"### {title}", "", blurb, ""]
        rows = book.get(task, [])
        if not rows:
            lines += ["_(no render — missing section in every submission)_", ""]
            continue
        if task in ("V1", "V2", "V4"):
            lines += ["| Model | Render (in color, straight from the submission) | Peer VIS /100 |",
                      "|---|---|---:|"]
            w = WIDTHS[task]
            for model, path, score in rows:
                alt = f"{model} {task}"
                lines.append(f"| **{model.replace('-free', '')}** "
                             f"| <img src=\"{path}\" alt=\"{alt}\" width=\"{w}\"> | {score} |")
            lines.append("")
        else:
            lines += ["| Model | Open in browser (GitHub won't run it) | Peer VIS /100 |",
                      "|---|---|---:|"]
            for model, path, score in rows:
                lines.append(f"| **{model.replace('-free', '')}** "
                             f"| [`{path}`]({path}) | {score} |")
            lines.append("")
    lines += [
        "_Full raw builds (all 8 models, all 4 visual tasks plus F1) live in `submissions/` "
        "between rounds; the renders above are extracted verbatim by "
        "`scripts/build_gallery.py` — no retouching._",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


section = build_section()
anchor = "## 🗂️ Repository map"
idx = readme.index(anchor)
readme = readme[:idx] + section + "\n" + readme[idx:]

# add gallery bullet to the repo map
readme = readme.replace(
    "- [`leaderboard.md`](leaderboard.md)",
    "- [`gallery/`](gallery)\n- [`leaderboard.md`](leaderboard.md)",
    1,
)

readme_path.write_text(readme, encoding="utf-8")
print("showcase inserted before the repository map; gallery bullet added")
