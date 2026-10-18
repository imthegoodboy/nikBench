# NikBench — Official Leaderboard

_Last updated: 2026-10-18 09:45 UTC · scorer: `scripts/aggregate.py` · protocol: `docs/methodology.md`_

| Rank | Model | Final | Grade | NBS | Peer | Self | RAT | THO | VIS | ALG | FE | BE | Judges | Spread | Live (BE/FE) | Cost (est.) |
|---:|---|---:|:--:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:--:|---:|---:|---:|
| 1 | **big-pickle** | 90.30 | S | 93.2 | 86.9 | 85.0 | 98 | 97 | 88 | 85 | 95 | 95 | 1 | ±0.0 | 100/100 | $0.0000 |
| 2 | **glm-5.3-flash-free** | 88.09 | A | 92.0 | 81.4 | 83.0 | 100 | 90 | 92 | 80 | 95 | 94 | 1 | ±0.0 | 100/100 | $0.0000 |
| 3 | **nemotron-3.5-super-vl-free** | 87.38 | A | 90.8 | 79.4 | 85.0 | 86 | 86 | 94 | 90 | 94 | 98 | 2 | ±2.0 | 100/92 | $0.0000 |
| 4 | **beam-free** | 85.43 | A | 90.3 | 71.3 | 85.0 | 96 | 88 | 91 | 82 | 93 | 91 | 3 | ±30.1 | 100/100 | $0.0000 |
| 5 | **deepseek-v4.1-flash-free** | 81.07 | A | 78.7 | 84.1 | 85.0 | 66 | 70 | 82 | 77 | 93 | 93 | 2 | ±28.0 | 100/100 | $0.0000 |
| 6 | **space-bunny-free** | 80.47 | A | 85.4 | 76.1 | 70.0 | 88 | 86 | 71 | 83 | 95 | 89 | 1 | ±0.0 | 100/100 | $0.0000 |
| 7 | **longcat-2.5-preview-free** | 73.61 | B | 78.1 | 68.7 | 65.0 | 95 | 67 | 73 | 73 | 91 | 68 | 2 | ±11.3 | 50/100 | $0.0000 |
| 8 | **mimo-v2.6-flash-free** | 38.24 | F | 37.5 | 33.6 | 45.0 | 98 | 90 | 0 | 0 | 0 | 0 | 3 | ±2.7 | 0/0 | $0.0000 |

## Grade scale

| Grade | Score | Meaning |
|:--:|---:|---|
| S | ≥ 90 | frontier: production-grade on all six pillars |
| A | ≥ 80 | excellent, minor gaps |
| B | ≥ 70 | solid generalist |
| C | ≥ 60 | functional, notable gaps |
| D | ≥ 45 | incomplete work on at least one pillar |
| F | < 45 | failed to produce usable submissions |

**NBS** = rubric-judge score (weighted across the 6 pillar medians) · **Peer** = mean of the other models' ratings · **Self** = the model's own rating of itself (last, by design) · **Final** = `0.6·NBS + 0.2·Peer + 0.2·Self`. Pillars: **RAT** ratiocination · **THO** thought · **VIS** visual · **ALG** algorithms · **FE** frontend · **BE** backend. Grades follow **Final** when peer data exists. **Cost (est.)** = input (test.md) + output (submission) tokens × published per-token price; free-tier models report $0.00, unknown models report `—`. **Live (BE/FE)** = pass rate of `scripts/verify_be.py` / `scripts/verify_fe.py` (50/50 blended into BE/FE medians when both judge and live data exist).

<details>
<summary><b>Peer-round notes</b></summary>

### Peer-round notes

- **beam-free**: peer 71.3/100 from 7 reviewer(s), self 85.0/100
- **big-pickle**: peer 86.9/100 from 7 reviewer(s), self 85.0/100
- **deepseek-v4.1-flash-free**: peer 84.1/100 from 7 reviewer(s), self 85.0/100
- **glm-5.3-flash-free**: peer 81.4/100 from 7 reviewer(s), self 83.0/100
- **longcat-2.5-preview-free**: peer 68.7/100 from 7 reviewer(s), self 65.0/100
- **mimo-v2.6-flash-free**: peer 33.6/100 from 7 reviewer(s), self 45.0/100
- **nemotron-3.5-super-vl-free**: peer 79.4/100 from 7 reviewer(s), self 85.0/100
- **space-bunny-free**: peer 76.1/100 from 7 reviewer(s), self 70.0/100

</details>


<details>
<summary><b>Per-judge details</b> (click to expand)</summary>

### beam-free — NBS 90.28 (S)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| cohere-north-mini | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| nemotron-3-ultra-free | 96.0 | 88.0 | 91.0 | 81.5 | 86.0 | 82.0 | 87.9 |
| nemotron-3.5-lightning-free | 92.0 | 65.0 | 62.5 | 58.5 | 70.5 | 65.5 | 70.0 |

Flags:
- judge outlier >15 from median overall: nemotron-3.5-lightning-free
- judge:cohere-north-mini: parser-salvaged: original card had invalid JSON (likely unescaped quotes); every score value below extracted verbatim from the raw judge output
- judge:nemotron-3.5-lightning-free: R1 3-god strategy verification not exhaustively traced branch-by-branch; THO pillars rely on LLM-generated content quality assessment; VIS art_fidelity score low due to highly stylized Mona Lisa representation

### big-pickle — NBS 93.21 (S)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| nemotron-3-ultra-free | 98.0 | 96.8 | 87.5 | 85.0 | 89.2 | 89.2 | 91.6 |

Flags:
- judge:nemotron-3-ultra-free: BE D4 exclusion constraint is the correct production solution for invariant (e); D5 correctly identifies silent cluster failure.
- judge:nemotron-3-ultra-free: No suspicious omissions or placeholder content found in any pillar.
- judge:nemotron-3-ultra-free: R1-R10 all match canonical solutions with full derivations — no contamination detected (derivations shown, not just answers).
- judge:nemotron-3-ultra-free: V1 Mona Lisa SVG is hand-authored (not traced) with single blur filter — respects element economy.
- judge:nemotron-3-ultra-free: V4 dataviz_honesty explicitly decomposes season/level/outlier — avoids the festival-spike trap.

### deepseek-v4.1-flash-free — NBS 78.73 (B)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| cohere-north-mini | 36.0 | 49.5 | 76.0 | 68.0 | 82.0 | 77.0 | 62.5 |
| nemotron-3-ultra-free | 96.0 | 90.0 | 87.0 | 85.8 | 88.5 | 94.5 | 90.6 |

Flags:
- judge:cohere-north-mini: parser-salvaged: original card had invalid JSON (likely unescaped quotes); every score value below extracted verbatim from the raw judge output

### glm-5.3-flash-free — NBS 92.01 (S)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| nemotron-3-ultra-free | 100.0 | 89.5 | 92.0 | 80.0 | 89.5 | 88.0 | 90.3 |

### longcat-2.5-preview-free — NBS 78.12 (B)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| nemotron-3-ultra-free | 96.0 | 86.8 | 73.0 | 80.5 | 81.0 | 88.8 | 85.0 |
| nemotron-3.5-lightning-free | 94.0 | 48.0 | 73.0 | 65.5 | 81.5 | 82.0 | 73.7 |

### mimo-v2.6-flash-free — NBS 37.55 (F)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| cohere-north-mini | 97.0 | 83.0 | 0.0 | 0.0 | 0.0 | 0.0 | 36.0 |
| nemotron-3-ultra-free | 98.0 | 89.8 | 0.0 | 0.0 | 0.0 | 0.0 | 37.5 |
| nemotron-3.5-lightning-free | 100.0 | 93.5 | 0.0 | 0.0 | 0.0 | 0.0 | 38.7 |

Flags:
- alg.communication: missing -> 0
- alg.complexity_analysis: missing -> 0
- alg.correctness: missing -> 0
- alg.edge_cases: missing -> 0
- alg.innovation: missing -> 0
- be.code_quality: missing -> 0
- be.data_modeling: missing -> 0
- be.design_answers: missing -> 0
- be.security: missing -> 0
- be.spec_correctness: missing -> 0
- be.validation_errors: missing -> 0
- fe.accessibility: missing -> 0
- fe.code_quality: missing -> 0
- fe.functionality: missing -> 0
- fe.responsive: missing -> 0
- fe.visual_design: missing -> 0
- judge:cohere-north-mini: judge said: all VIS/ALG/FE/BE pillars absent - only RAT and THO content present
- judge:cohere-north-mini: judge said: candidate submission incomplete: V/A/F/B sections missing due to repeated session failures
- judge:cohere-north-mini: parser-salvaged: original card had invalid JSON (likely unescaped quotes); every score value below extracted verbatim from the raw judge output
- judge:nemotron-3-ultra-free: Submission incomplete: ends at T6 with comment 'CONTINUE FROM: ## V1 (Mona Lisa SVG) — then V2, V3+V3-NOTES, V4+V4-NOTES, A1–A3, F1+F1-NOTES, B1+B1-D1..D5; then write full file and reply "PHASE 1 COMPLETE — waiting for peers"' indicating the candidate intended to produce VIS/ALG/FE/BE content but did not. All four pillars entirely absent.
- judge:nemotron-3.5-lightning-free: VIS/ALG/FE/BE pillars set to 0 because candidate submission has no content in these sections (marked 'section absent - candidate produced no such submission content')
- vis.art_craft: missing -> 0
- vis.art_fidelity: missing -> 0
- vis.dataviz_choice: missing -> 0
- vis.dataviz_honesty: missing -> 0
- vis.infographic_design: missing -> 0
- vis.infographic_facts: missing -> 0
- vis.motion_design: missing -> 0
- vis.motion_timing: missing -> 0

### nemotron-3.5-super-vl-free — NBS 90.83 (S)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| cohere-north-mini | 72.0 | 89.0 | 100.0 | 97.5 | 100.0 | 100.0 | 91.8 |
| nemotron-3-ultra-free | 100.0 | 83.5 | 88.0 | 82.2 | 93.0 | 91.0 | 89.8 |

Flags:
- judge:cohere-north-mini: parser-salvaged: original card had invalid JSON (likely unescaped quotes); every score value below extracted verbatim from the raw judge output

### space-bunny-free — NBS 85.40 (A)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| nemotron-3-ultra-free | 88.0 | 85.5 | 71.0 | 83.0 | 90.5 | 77.5 | 83.0 |

Flags:
- judge:nemotron-3-ultra-free: BE implementation lacks authentication and rate limiting (described only in design answers D2/D3).
- judge:nemotron-3-ultra-free: R3 answer incorrect (June 17 vs correct July 16) — derivation eliminates only unique days, not months containing them.
- judge:nemotron-3-ultra-free: V1 Mona Lisa table in R5 has fox/cat swap (house 1 cats vs fox in text, house 4 fox vs dog in text) though Final Answer correct.
- judge:nemotron-3-ultra-free: V2 infographic_facts: milestone x-positions wrong for Turing, Hopper, Shannon, Dijkstra (4 of 7). Timeline not truthful to scale.
- judge:nemotron-3-ultra-free: V3 CSS animations for visual elements (rocket, earth) not perfectly aligned with declared beat boundaries, but JS driver enforces correct timing for interactive elements.

</details>
