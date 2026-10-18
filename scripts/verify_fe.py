"""Static spec checklist for every model's F1 Mission Control.

No browser required: extracts each ```html block and checks the 10 spec items
by concrete, regex-level evidence. Reports a per-model pass count so the FE
pillar is at least partially objective.
"""
import argparse
import json as _json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(".")
MODELS = sorted(p.stem for p in (ROOT / "submissions").glob("*.md")
                if p.name != "README.md")

CLOCK_RE = re.compile(r"HH:MM:SS|HH:mm:ss|getUTCHours|toISOString\(\)\.slice\(11|toISOString\(\)\.substring\(11")

CHECKS = [
    ("live UTC clock HH:MM:SS", lambda h: bool(CLOCK_RE.search(h))),
    ("mulberry32 / seed 42", lambda h: ("mulberry32" in h.lower()) and ("42" in h)),
    ("countdown target 2026-12-01T09:00:00Z", lambda h: "2026-12-01T09:00:00Z" in h),
    ("LANDED status", lambda h: "LANDED" in h),
    ("sortable table headers", lambda h: bool(re.search(r"th.*onclick|addEventListener.*click.*sort|sortColumn", h, re.I | re.S))),
    ("canvas chart", lambda h: "<canvas" in h.lower()),
    ("anomaly feed (RUN DIAGNOSTIC / dismiss)", lambda h: ("RUN DIAGNOSTIC" in h) and bool(re.search(r"✕|&times;|remove\(\)|splice", h))),
    ("localStorage nikbench.f1.", lambda h: "nikbench.f1." in h),
    ("theme toggle + shortcut d", lambda h: bool(re.search(r"keydown.*['\"]d['\"]|toggle.*theme|theme.*toggle", h, re.I | re.S))),
    ("responsive 4/2/1 cols", lambda h: bool(re.search(r"grid-template-columns|@media", h, re.I))),
    ("aria-label", lambda h: "aria-label" in h.lower()),
    ("prefers-reduced-motion", lambda h: "prefers-reduced-motion" in h),
    ("semantic landmarks", lambda h: all(t in h.lower() for t in ("<header", "<main", "<section")) or all(t in h.lower() for t in ("<header", "<main", "<aside"))),
]


def extract_html(model: str) -> str | None:
    text = (ROOT / "submissions" / f"{model}.md").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^## F1\b.*?(?=\n## |\Z)", text, re.S | re.M)
    if not m:
        return None
    block = re.search(r"```html\s*\n(.*?)```", m.group(0), re.S)
    return block.group(1) if block else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="print {model: live_FE_score_0_100} JSON and exit")
    args = ap.parse_args()
    out = {}
    if args.json:
        for model in MODELS:
            html = extract_html(model)
            if not html:
                out[model] = 0
                continue
            n = sum(1 for _, fn in CHECKS if fn(html))
            out[model] = round(n / len(CHECKS) * 100)
        print(_json.dumps(out))
        return
    print("FE static spec checklist (13 items, F1 Mission Control):")
    print(f"{'model':<32} {'pass':>5}  {'/13'}")
    print("-" * 70)
    for model in MODELS:
        html = extract_html(model)
        if not html:
            print(f"{model:<32}   --  (no F1 section)")
            continue
        passed = [name for name, fn in CHECKS if fn(html)]
        failed = [name for name, fn in CHECKS if not fn(html)]
        n = len(passed)
        print(f"{model:<32} {n:>3}/13  {', '.join(failed) if failed else 'all pass'}")


if __name__ == "__main__":
    main()
