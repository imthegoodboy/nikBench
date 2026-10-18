import importlib.util
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
spec = importlib.util.spec_from_file_location("agg", "scripts/aggregate.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

REQUIRED = {"rat", "tho", "vis", "alg", "fe", "be", "overall"}

for f in sorted(Path("peer").glob("*.md")):
    if f.name == "README.md":
        continue
    p = m.parse_peer_file(f)
    if p:
        rev, ratings = p
        selfs = [k for k, v in ratings.items() if v.get("self")]
        keys_ok = all(REQUIRED.issubset(v) for v in ratings.values())
        print(
            f"{f.name:<32} VALID | reviewer={rev} | n={len(ratings)}"
            f" | self={selfs} | keys_ok={keys_ok}"
        )
    else:
        print(f"{f.name:<32} INVALID")
