# NikBench — Official Leaderboard

_Last updated: 2026-10-17 22:17 UTC · scoring: `scripts/aggregate.py` · protocol: `docs/methodology.md`_

| Rank | Model | NBS | Grade | RAT | THO | VIS | ALG | FE | BE | Judges | Spread |
|---:|---|---:|:--:|---:|---:|---:|---:|---:|---:|:--:|---:|
| 1 | **example-candidate** | 67.90 | C | 64.0 | 67.0 | 70.5 | 65.5 | 73.5 | 68.5 | 3 | ±8.8 |

## Grade scale

| Grade | Score | Meaning |
|:--:|---:|---|
| S | ≥ 90 | frontier: production-grade on all six pillars |
| A | ≥ 80 | excellent, minor gaps |
| B | ≥ 70 | solid generalist |
| C | ≥ 60 | functional, notable gaps |
| D | ≥ 45 | incomplete work on at least one pillar |
| F | < 45 | failed to produce usable submissions |

**NBS** = NikBench Score, 0–100, the PILLAR_WEIGHTS-weighted mean of the six pillar medians. `Spread` = range of per-judge overall scores; below 10.0 is healthy agreement, above 15.0 gets flagged for review.

<details>
<summary><b>Per-judge details</b> (click to expand)</summary>

### example-candidate — NBS 67.90 (C)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| judge-alpha | 72.0 | 73.0 | 70.5 | 65.5 | 73.5 | 68.5 | 70.7 |
| judge-beta | 64.0 | 63.0 | 63.0 | 55.5 | 63.5 | 61.5 | 61.9 |
| judge-gamma | 62.0 | 67.0 | 74.5 | 65.5 | 73.5 | 69.5 | 68.2 |

Flags:
- judge:judge-beta: spread between my pillar scores and judge-alpha's on alg/fe — see dispute protocol

</details>
