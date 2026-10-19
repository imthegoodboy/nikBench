"""NikBench round QA — one command runs every verifier.

Structure (verify_phase1) + FE static checks (verify_fe) + BE live contract
(verify_be), merged into one per-model report. Use this before a board refresh:

    python scripts/verify_all.py            # human table
    python scripts/verify_all.py --json     # machine JSON

Scores are 0–100 per column; `structure` = fraction of expected v3.0 sections
present (R1–R13 · T1–T7 · V1–V7 · A1–A4 · F1 · B1 + notes/design answers).
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(".")
EXPECTED = (
    [f"## R{i}" for i in range(1, 14)]
    + [f"## T{i}" for i in range(1, 8)]
    + ["## V1", "## V2", "## V3", "## V3-NOTES", "## V4", "## V4-NOTES",
       "## V5", "## V6", "## V7"]
    + [f"## A{i}" for i in range(1, 5)]
    + ["## F1", "## F1-NOTES", "## B1"]
    + [f"## B1-D{i}" for i in range(1, 7)]
)


def structure_score(model: str) -> int:
    path = ROOT / "submissions" / f"{model}.md"
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    found = sum(1 for s in EXPECTED if re.search(rf"^{re.escape(s)}\b", text, re.M))
    return round(found / len(EXPECTED) * 100)


def run_json(script: str) -> dict:
    try:
        r = subprocess.run([sys.executable, f"scripts/{script}", "--json"],
                           capture_output=True, text=True, timeout=420,
                           encoding="utf-8", errors="replace")
        if r.returncode != 0 or not r.stdout.strip():
            return {}
        return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception as exc:  # noqa: BLE001
        print(f"WARNING: {script} failed: {exc}", file=sys.stderr)
        return {}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="emit {model: {structure, fe, be}} JSON")
    args = ap.parse_args()

    models = sorted(p.stem for p in (ROOT / "submissions").glob("*.md")
                    if p.name != "README.md")
    if not models:
        print("no submissions found under submissions/")
        return

    fe = run_json("verify_fe.py")
    be = run_json("verify_be.py")

    report = {}
    for m in models:
        report[m] = {"structure": structure_score(m),
                     "fe": int(fe.get(m, 0)),
                     "be": int(be.get(m, 0))}
    if args.json:
        print(json.dumps(report))
        return

    print("NikBench round QA — structure · FE static · BE live (0–100)")
    print(f"{'model':<32} {'struct':>7} {'FE':>4} {'BE':>4}   note")
    print("-" * 84)
    for m in models:
        r = report[m]
        note = "complete build" if min(r.values()) >= 90 else (
            "partial build" if r["structure"] < 90 else "spec gaps")
        print(f"{m:<32} {r['structure']:>6}% {r['fe']:>4} {r['be']:>4}   {note}")
    print()
    print("structure counts the v3.0 sections R1–R13/T1–T7/V1–V7/A1–A4/F1/B1 (+notes & D1–D6).")


if __name__ == "__main__":
    main()
