import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EXPECTED_SECTIONS = (
    [f"## R{i}" for i in range(1, 11)]
    + [f"## T{i}" for i in range(1, 7)]
    + ["## V1", "## V2", "## V3", "## V3-NOTES", "## V4", "## V4-NOTES"]
    + [f"## A{i}" for i in range(1, 4)]
    + ["## F1", "## F1-NOTES", "## B1"]
    + [f"## B1-D{i}" for i in range(1, 6)]
)

def check(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    missing = [s for s in EXPECTED_SECTIONS if not re.search(rf"^{re.escape(s)}\b", text, re.M)]
    finals = len(re.findall(r"^Final Answer:", text, re.M))
    fences = text.count("```")
    svg_blocks = len(re.findall(r"```svg", text))
    html_blocks = len(re.findall(r"```html", text))
    js_blocks = len(re.findall(r"```javascript", text))
    todo = len(re.findall(r"\b(TODO|not implemented|omitted for brevity)\b", text, re.I))
    issues = []
    if missing:
        issues.append(f"missing sections: {', '.join(s[3:] for s in missing)}")
    if finals != 10:
        issues.append(f"Final Answer lines = {finals}/10")
    if svg_blocks < 3:
        issues.append(f"svg blocks = {svg_blocks}/3 (V1,V2,V4)")
    if html_blocks < 2:
        issues.append(f"html blocks = {html_blocks}/2 (V3,F1)")
    if js_blocks < 1:
        issues.append("javascript block missing (B1)")
    if todo:
        issues.append(f"placeholder-ish words: {todo}")
    size = len(text.encode('utf-8'))
    status = "OK " if not issues else "WARN"
    return f"{status} {path.name:<32} {size//1024:>4} KB | finals={finals} fences={fences} | " + ("; ".join(issues) or "structure complete")

if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "submissions")
    for f in sorted(root.glob("*.md")):
        if f.name != "README.md":
            print(check(f))
