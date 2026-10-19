"""Extract the visual-task blocks from a round's submissions into gallery/ files.

Curation: the three highest peer-VIS-rated models of the round feed each
visual task. SVG tasks (V1/V2/V4/V5/V6/V7) become <img>-able .svg files; V3
(the 60-second CSS motion loop) and F1 (Mission Control) become .html files
the visitor opens in a browser (GitHub sandboxes HTML on purpose).
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(".")
TASKS = {
    "V1": ("svg", "mona-lisa"),
    "V2": ("svg", "seven-founders"),
    "V3": ("html", "liftoff"),
    "V4": ("svg", "cafe-chart"),
    "V5": ("svg", "eiffel-tower"),
    "V6": ("svg", "taj-mahal"),
    "V7": ("svg", "earth-color-system"),
    "F1": ("html", "mission-control"),
}


def slug(name: str) -> str:
    return name.replace(".", "-")


def peer_vis_means() -> dict[str, float]:
    """Mean vis rating across the 7 non-self reviewers per candidate."""
    totals: dict[str, list[float]] = {}
    for path in sorted(ROOT.glob("peer/*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        import importlib.util
        spec = importlib.util.spec_from_file_location("agg", "scripts/aggregate.py")
        agg = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(agg)
        parsed = agg.parse_peer_file(path)
        if not parsed:
            continue
        _reviewer, ratings = parsed
        for model, r in ratings.items():
            if not r.get("self") and r.get("vis") is not None:
                totals.setdefault(model, []).append(float(r["vis"]))
    return {m: round(sum(v) / len(v) * 10, 1) for m, v in totals.items()}


def extract_block(sub_text: str, section: str, lang: str) -> str | None:
    """First fenced ``lang`` block inside the ``## <section>`` section."""
    m = re.search(rf"^## {section}\b.*?(?=\n## |\Z)", sub_text, re.S | re.M)
    if not m:
        return None
    block = re.search(rf"```{lang}\s*\n(.*?)```", m.group(0), re.S)
    return block.group(1).rstrip() + "\n" if block else None


def main() -> None:
    gallery = ROOT / "gallery"
    gallery.mkdir(exist_ok=True)
    means = peer_vis_means()
    print("peer VIS means (0-10, peers only):")
    for m, v in sorted(means.items(), key=lambda kv: -kv[1]):
        print(f"  {m:<32} {v}")
    ranked = [m for m, _ in sorted(means.items(), key=lambda kv: -kv[1])]

    picks: dict[str, list[tuple[str, str, float]]] = {}
    for task, (lang, slugname) in TASKS.items():
        rows = []
        for model in ranked:
            sub = ROOT / "submissions" / f"{model}.md"
            if not sub.exists():
                continue
            block = extract_block(sub.read_text(encoding="utf-8", errors="replace"),
                                  task, lang)
            if not block or len(block) < 200:
                continue
            out = gallery / f"{slug(model)}_{slugname}.{lang}"
            out.write_text(block, encoding="utf-8")
            rows.append((model, out.as_posix(), means[model]))
            if len(rows) == 3:
                break
        picks[task] = rows
        print(f"{task}: {len(rows)} extracted -> {[(r[0], r[1]) for r in rows]}")

    gb = ROOT / "gallery" / "_book.json"
    gb.write_text(repr(picks), encoding="utf-8")
    print("book written")


if __name__ == "__main__":
    main()
