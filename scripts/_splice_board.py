"""Splice the generated leaderboard.md into README.md between the live markers."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

board = Path("leaderboard.md").read_text(encoding="utf-8")
readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")

# Drop the generated H1 (README supplies its own section header).
lines = board.split("\n")
if lines and lines[0].startswith("# NikBench"):
    lines = lines[1:]
# Trim leading blanks from the H1 removal.
while lines and not lines[0].strip():
    lines = lines
    break
content = "\n".join(lines).strip()

START = "<!-- NIKBENCH:LEADERBOARD:START -->"
END = "<!-- NIKBENCH:LEADERBOARD:END -->"
i0 = readme.index(START) + len(START)
i1 = readme.index(END)
new_readme = readme[:i0] + "\n" + content + "\n\n" + readme[i1:]
readme_path.write_text(new_readme, encoding="utf-8")

print("spliced OK — README markers now contain the live board")
