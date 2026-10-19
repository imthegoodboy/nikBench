"""Static spec checklist for every model's F1 Mission Control (v3.0 hard build).

No browser required: extracts each ```html block and checks the v3.0 spec items
by concrete, regex-level evidence. Reports a per-model pass count so the FE
pillar is at least partially objective. v3.0 adds: 10k-row virtualisation,
command palette, undo/redo, dual-series chart with crosshair, timezone selector,
high-DPI handling, high-DPI + no-network checks.
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
    ("LANDED + T+ elapsed state", lambda h: ("LANDED" in h) and bool(re.search(r"T\+|elapsed", h))),
    ("mission timezone selector (offsets)", lambda h: bool(re.search(r"offset|timezone|utc[+-]|gmt", h, re.I)) and ("select" in h.lower() or "-12" in h)),
    ("10k-row data model", lambda h: bool(re.search(r"10[_,]?000|1e4", h))),
    ("virtualised grid (windowed DOM)", lambda h: bool(re.search(r"slice\(|requestAnimationFrame|scrollTop|virtual", h, re.I)) and bool(re.search(r"scroll", h, re.I))),
    ("sortable table headers", lambda h: bool(re.search(r"sortColumn|sortBy|sort\(|addEventListener.*click.*sort", h, re.I | re.S))),
    ("live search/filter", lambda h: bool(re.search(r"filter\(|search(input)?\b|query", h, re.I))),
    ("canvas chart", lambda h: "<canvas" in h.lower()),
    ("dual series (signal + fuel)", lambda h: ("signal" in h.lower()) and ("fuel" in h.lower()) and ("<canvas" in h.lower())),
    ("chart tooltip / crosshair", lambda h: bool(re.search(r"mousemove|pointermove", h, re.I)) and bool(re.search(r"tooltip|crosshair|nearest", h, re.I))),
    ("anomaly feed (RUN DIAGNOSTIC / dismiss)", lambda h: ("RUN DIAGNOSTIC" in h) and bool(re.search(r"✕|&times;|remove\(\)|splice|dismiss", h, re.I))),
    ("undo/redo history", lambda h: bool(re.search(r"undo", h, re.I)) and bool(re.search(r"redo", h, re.I)) and bool(re.search(r"ctrlKey|metaKey", h))),
    ("command palette (Ctrl/Cmd+K)", lambda h: bool(re.search(r"metaKey|ctrlKey|Ctrl", h)) and bool(re.search(r"['\"]k['\"]", h)) and bool(re.search(r"palette|combobox|role=[\"']dialog", h, re.I)) and bool(re.search(r"escape", h, re.I))),
    ("localStorage nikbench.f1.", lambda h: "nikbench.f1." in h),
    ("theme toggle + shortcut d", lambda h: bool(re.search(r"keydown.*['\"]d['\"]|toggle.*theme|theme.*toggle", h, re.I | re.S))),
    ("responsive breakpoints", lambda h: bool(re.search(r"grid-template-columns|@media", h, re.I)) and bool(re.search(r"375|480|640", h))),
    ("aria-label", lambda h: "aria-label" in h.lower()),
    ("aria-live for feed", lambda h: "aria-live" in h.lower()),
    ("prefers-reduced-motion", lambda h: "prefers-reduced-motion" in h),
    ("semantic landmarks", lambda h: all(t in h.lower() for t in ("<header", "<main", "<section")) or all(t in h.lower() for t in ("<header", "<main", "<aside"))),
    ("high-DPI canvas (devicePixelRatio)", lambda h: "devicePixelRatio" in h),
    ("self-contained (no network assets)", lambda h: not re.search(r"<script[^>]+src=|<link[^>]+href=[\"']https?://|<img[^>]+src=[\"']https?://|@import", h, re.I)),
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
    print(f"FE static spec checklist ({len(CHECKS)} items, v3.0 hard F1):")
    print(f"{'model':<32} {'pass':>5}  {'/' + str(len(CHECKS))}")
    print("-" * 70)
    for model in MODELS:
        html = extract_html(model)
        if not html:
            print(f"{model:<32}   --  (no F1 section)")
            continue
        passed = [name for name, fn in CHECKS if fn(html)]
        failed = [name for name, fn in CHECKS if not fn(html)]
        n = len(passed)
        print(f"{model:<32} {n:>3}/{len(CHECKS)}  {', '.join(failed) if failed else 'all pass'}")


if __name__ == "__main__":
    main()
