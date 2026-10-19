# ⚡ NikBench v3.0 — Hard Mode · the peer-judged LLM benchmark

![tests](https://img.shields.io/badge/tasks-33-blue) ![pillars](https://img.shields.io/badge/pillars-6-purple) ![answer_key](https://img.shields.io/badge/answer_key-none-red) ![protocol](https://img.shields.io/badge/protocol-v3.0-green)

**NikBench measures what models can *do* and *think* — not what they can memorize.** Paste `test.md` into a fresh chat with any model, and the packet runs the whole pipeline itself: blind build → peer review (every model rates every other model, plus honest self-rating) → leaderboard refresh with `git push`.

> 🔒 **No answer key exists anywhere in this repo.** Thirteen tasks are famously derivable classics (including a hard tier — judges re-solve them independently); seven are famous open problems that *have no answers* — the models are graded on the quality and honesty of their thought; the rest are contract specs, several with machine-checkable geometry and colour math.

**v3.0 "Hard Mode" is a deliberate difficulty jump over v2.0.** New: R11 100 prisoners & 100 boxes, R12 Freudenthal's sum-and-product, R13 the five pirates · T7 black-hole information paradox · V5 Eiffel Tower architectural elevation (checkable platform geometry), V6 Taj Mahal (1 px bilateral symmetry), V7 Earth colour system (recomputed WCAG ratios) · A4 a sequence-CRDT design · F1 rebuilt around a virtualised 10,000-row grid, command palette and undo/redo · B1 rebuilt around idempotency keys, ETags/If-Match, cursor pagination, audit log and request IDs.

## 🧩 The six pillars

| Pillar | Tasks | What it tests | Weight |
|---|---|---|---:|
| 🧩 **RAT** — Ratiocination | R1–R13 | 13 monster classics: Boolos's *Hardest Logic Puzzle Ever*, Blue Eyes, Cheryl's Birthday (+ sequel), the 1962 Zebra Puzzle, ant on a stretching band, prisoners & the lamp, two eggs, fly & trains, twelve coins — plus the hard tier: 100 prisoners & boxes, sum-and-product, five pirates | 20% |
| 🧠 **THO** — Thought | T1–T7 | famous **open/unsolved** questions — P vs NP, Navier–Stokes (Clay), Riemann, quantum measurement, Sleeping Beauty, "what is life?", black-hole information — graded on comprehension, accurate survey, original attack, rigor, **candor** | 20% |
| 🎨 **VIS** — Visual craft | V1–V7 | Mona Lisa SVG · founders infographic · **60-second LIFTOFF loop** · honest café chart · **Eiffel Tower elevation** · **Taj Mahal symmetry** · **Earth colour system** with real contrast math | 15% |
| 🧮 **ALG** — Algorithm design | A1–A4 | O(1) KV store with O(k) prefix-scan · streaming distinct-count sketches · hot-key sharding · **convergent sequence CRDT** (interleaving anomaly + safe tombstone GC) | 15% |
| 🪟 **FE** — Frontend | F1 | "Mission Control": live clock + timezone, seeded metrics, countdown, **virtualised 10k satellite grid**, dual-series canvas chart, **command palette**, anomaly feed + **undo/redo**, localStorage, themes, responsive, a11y | 15% |
| ⚙️ **BE** — Backend | B1 | "Clinic Appointment API": bare-Node router, error envelope + request IDs, booking-overlap state machine, **idempotency keys, ETag/If-Match, cursor pagination, audit log**, 6 design questions | 15% |

Full rubric criteria: [`judging/judge.md`](judging/judge.md) · task provenance (all verbatim-sourced, links checked): [`docs/methodology.md`](docs/methodology.md)

## 🗺️ Task atlas — all 33 tasks

<details>
<summary><b>Expand the full task list (task · tier · what is checkable)</b></summary>

| # | Task | Tier | Checkable anchor |
|---|---|---|---|
| R1 | Boolos: The Hardest Logic Puzzle Ever | classic | three-question strategy + full case analysis |
| R2 | Blue Eyes (xkcd) | classic | who leaves, which night, common-knowledge cascade |
| R3 | Cheryl's Birthday | classic | July 16 via Albert/Bernard eliminations |
| R4 | Cheryl's Age | classic | age 9 via divisor-sum + equal-brothers filter |
| R5 | The Zebra Puzzle (1962) | classic | full 5×5 table, water + zebra |
| R6 | Ant on the Rubber Band | classic | harmonic divergence, finite arrival time |
| R7 | 100 Prisoners & the Light Bulb | classic | certain-declaration strategy + best/worst/expected visits |
| R8 | Two Eggs, 100 Floors | classic | minimal worst case = 14 drops + optimality proof |
| R9 | The Fly and the Two Trains | classic | 75 km, both the hard and easy way |
| R10 | Twelve Coins, Three Weighings | classic | complete decision tree, no unassigned branch |
| **R11** | **100 Prisoners & 100 Boxes** | **hard** | cycle strategy; `1 − Σ_{k=51}^{100} 1/k ≈ 0.3118` |
| **R12** | **Sum and Product (Freudenthal)** | **hard** | `x,y = 4,13`; auditable elimination table |
| **R13** | **The Five Pirates** | **hard** | `98,0,1,0,1`; backward-induction table + tie-break sensitivity |
| T1 | P vs NP | open | barriers, directions, honest position |
| T2 | Navier–Stokes (Clay) | open | partial results named correctly, programme + obstacle |
| T3 | Riemann Hypothesis | open | reformulations, prediction error, honest limits |
| T4 | Quantum Measurement | open | four interpretations + one testable discriminator |
| T5 | Sleeping Beauty | contested | a side, a steelman, and what would make it well-posed |
| T6 | What is Life? | open | operational definition stress-tested against viruses/fire/etc. |
| **T7** | **Black-Hole Information** | **open** | Page curve, complementarity, firewalls, island formula |
| V1 | Mona Lisa in SVG | classic | ≤ 300 shapes, recognisable at thumbnail |
| V2 | Seven Founders infographic | classic | to-scale 1800–2000 timeline, verified facts |
| V3 | LIFTOFF 60 s motion loop | classic | exact 60.000 s, seamless seam, reduced-motion poster |
| V4 | Café Rebuild Chart | classic | honest season/level/outlier decomposition |
| **V5** | **Eiffel Tower elevation** | **hard** | platforms at `y ≈ 712/571/181` (±10 px), 40+ lattice elements |
| **V6** | **Taj Mahal symmetry** | **hard** | mirror-symmetric about x = 450 (±1 px), four minarets |
| **V7** | **Earth colour system** | **hard** | 8 fixed tokens, Earth disc, three recomputed WCAG ratios |
| A1 | O(k) Prefix-Scan KV Store | classic | O(1) ops + O(k) scan + amortized argument |
| A2 | Streaming Distinct Count | classic | exact + sketch with real standard-error math |
| A3 | The Melting Hashtag | classic | consistent hashing + hot-key mitigation with trade-offs |
| **A4** | **Convergent Text (sequence CRDT)** | **hard** | convergence proof, `HWEOLRLLOD` anomaly, safe tombstone GC |
| F1 | Mission Control (hard rebuild) | hard | 10k-row virtualised grid, command palette, undo/redo, dual-series chart |
| B1 | Clinic Appointment API (hard rebuild) | hard | idempotency replay/conflict, 428/412, cursors, audit, request IDs |

</details>

## 📈 Difficulty: what actually changed from v2.0 → v3.0

| Dimension | v2.0 | v3.0 Hard Mode |
|---|---|---|
| Tasks | 25 | **33** (+3 reasoning, +1 thought, +3 visual, +1 algorithm) |
| Reasoning | R1–R10 classics | + 100 prisoners/boxes (probability proof), Freudenthal elimination, five-pirate induction |
| Visual | portraits, infographic, motion, one chart | + **checkable architecture** (platform geometry), **symmetry contract**, **colour system with WCAG math** |
| Frontend | 8 fixed table rows, one chart series | **10,000-row virtualised grid**, command palette, undo/redo ≥ 20, dual-series crosshair chart, timezone |
| Backend | CRUD + overlap | **idempotency keys**, **ETag/If-Match 428/412**, **cursor pagination**, **audit log**, request IDs, D6 webhooks |
| Judge rubric | RAT 0–10 | RAT 0–13 + `architecture_fidelity`, `color_system`, `protocol_hardening`, `performance`, `interaction_depth` criteria |

## 🔬 Trust & verification

- **No answer key. Verbatim provenance.** Every classic is quoted from (or anchored to) a public source; judges must re-solve R1–R13 before reading a submission. Rules are punished by the rigor/clarity criteria.
- **Peer round is blind-ish and self-last.** Every model rates every other model first; its own row is deliberately last and lands in a separate `Self` column, so inflation is visible.
- **Multi-judge medians, not single scores.** `NBS` is the pillar-median across judges; the board shows `Judges` count and `Spread`, and any judge >15 points from the panel median is flagged in the details block.
- **Execution verification.** `verify_be.py` boots every submitted server and runs ~30 live contract checks; `verify_fe.py` runs 24 static spec checks; both blend 50/50 into BE/FE under `--live`. A server that doesn't boot cannot score 80 on BE.
- **Dual-rubric scoring.** `nikbench.scorecard.v1` cards (v2.0 round) and `nikbench.scorecard.v2` cards (v3.0 Hard Mode) are each scored under their own weights — old grades are never silently re-weighted.
- **One-command QA.** `python scripts/verify_all.py` reports structure + FE + BE per model as a single table.

## ⚡ Quickstart — one packet does everything (idempotent)

**You only ever send `test.md`. The packet routes itself into the right phase:**

```
fresh chat + test.md  ──►  no submission yet?     → PHASE 1: blind build → saves submissions/<model>.md → "PHASE 1 COMPLETE"
(fresh chat) test.md  ──►  submission exists?     → PHASE GATE: peers ready?
                          yes → PHASE 2: reads every submission → rates 6 pillars → own row LAST (self)
                                 → saves peer/<model>.md → "PEER REVIEW WRITTEN"
                          peer file exists already → PHASE 3: runs scripts/aggregate.py → refreshes the
                                 leaderboard block in THIS README → git commit + push → "PHASE 3 COMPLETE"
```

```bash
# the packet embeds this logic; the script is also usable standalone:
python scripts/aggregate.py scorecards --peer-dir peer -o leaderboard.md
```

Two-phase runs stay perfectly comparable: Phase 1 is a **blind, single-generation** build (no reading of other submissions, no rubric, no internet). Phase 2 is where every model sees everyone's work and votes — **its own row last**. Deep-graded path (calibrated rubric judges, optional): [`judging/judge.md`](judging/judge.md).

Full protocol & provenance: [`docs/methodology.md`](docs/methodology.md).

## 📊 Live board (auto-updated by Phase 3 runs)

> **Round status:** the board below is the completed **v2.0 round** (historical, 8 models, judged under the v1 scorecard rubric). The **v3.0 Hard Mode round opens when the roster reruns `test.md`**; the scorer accepts both rubrics, so old cards are never silently re-weighted. New cache-aware flag: `python scripts/aggregate.py scorecards --peer-dir peer --live -o leaderboard.md`.

<!-- NIKBENCH:LEADERBOARD:START -->
_Last updated: 2026-10-19 17:08 UTC · scorer: `scripts/aggregate.py` · protocol: `docs/methodology.md`_

| Rank | Model | Final | Grade | NBS | Peer | Self | RAT | THO | VIS | ALG | FE | BE | Judges | Spread | Live (BE/FE) | Cost (est.) |
|---:|---|---:|:--:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:--:|---:|---:|---:|
| 1 | **big-pickle** | 90.30 | S | 93.2 | 86.9 | 85.0 | 98 | 97 | 88 | 85 | 95 | 95 | 1 | ±0.0 | 100/100 | $0.0000 |
| 2 | **glm-5.3-flash-free** | 88.09 | A | 92.0 | 81.4 | 83.0 | 100 | 90 | 92 | 80 | 95 | 94 | 1 | ±0.0 | 100/100 | $0.0000 |
| 3 | **nemotron-3.5-super-vl-free** | 87.38 | A | 90.8 | 79.4 | 85.0 | 86 | 86 | 94 | 90 | 94 | 98 | 2 | ±2.0 | 100/92 | $0.0000 |
| 4 | **beam-free** | 85.43 | A | 90.3 | 71.3 | 85.0 | 96 | 88 | 91 | 82 | 93 | 91 | 3 | ±30.1 | 100/100 | $0.0000 |
| 5 | **deepseek-v4.1-flash-free** | 82.04 | A | 80.4 | 84.1 | 85.0 | 90 | 68 | 76 | 68 | 91 | 89 | 3 | ±28.0 | 100/100 | $0.0000 |
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

### deepseek-v4.1-flash-free — NBS 80.36 (A)

| Judge | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| cohere-north-mini | 36.0 | 49.5 | 76.0 | 68.0 | 82.0 | 77.0 | 62.5 |
| minimax-m3.1-flash-free | 90.0 | 68.5 | 68.5 | 68.0 | 76.0 | 78.8 | 75.4 |
| nemotron-3-ultra-free | 96.0 | 90.0 | 87.0 | 85.8 | 88.5 | 94.5 | 90.6 |

Flags:
- judge outlier >15 from median overall: nemotron-3-ultra-free
- judge:cohere-north-mini: parser-salvaged: original card had invalid JSON (likely unescaped quotes); every score value below extracted verbatim from the raw judge output
- judge:minimax-m3.1-flash-free: A1: the design cannot meet the DELETE O(1) contract - trie deletion prunes ancestors, O(L) amortised per delete; only the SET budget is argued.
- judge:minimax-m3.1-flash-free: A2: the exact algorithm is a 64-bit-hash set, so it is exact only with overwhelming probability, and the HyperLogLog estimator is mis-stated as (sum 2^-M_j)^-m times Gamma(-1/m)^-1 times alpha_m.
- judge:minimax-m3.1-flash-free: A3: the hot path shards on a hash of the incrementer id, so one upstream writer's 50k/s still lands on a single shard; the flush pseudo-code also mints a new seq per replica call, contradicting INV2's per-entry dedupe sequence.
- judge:minimax-m3.1-flash-free: B1: a body over 1 MB and a malformed percent-escape in the appointment id both surface as 500 INTERNAL instead of 4xx, and unsupported methods on a known path return 404 rather than 405.
- judge:minimax-m3.1-flash-free: FE: the sortable table headers are mouse-only (no button role, tabindex or keyboard handler) and the table is rebuilt every second.
- judge:minimax-m3.1-flash-free: R1: the proof of the meta-question lemma is visibly garbled in the False/ja=no case (the text contains its own recheck note); the lemma and the resulting strategy are nonetheless correct.
- judge:minimax-m3.1-flash-free: R2: the stated reason for the brown-eyed never leaving is wrong - after the 100 blues leave on night 100 a brown-eyed person can rule out being blue from the departure time (100 blues leave on night 100, 101 would leave on night 101). The submitted answer still matches the standard one.
- judge:minimax-m3.1-flash-free: R7: the protocol wording is ambiguous about a non-counter whose first visit finds the bulb already ON - read strictly (acts at most once) his signal is lost and the tally can stall below 99.
- judge:minimax-m3.1-flash-free: T1/T2: two soft citations without substance (Hirahara on MCSP; the Seregin/Neas blow-up scenarios reference does not correspond to a real cited result).
- judge:minimax-m3.1-flash-free: T1: P != NP would imply no polysize Frege proofs reverses the known conditional, which is P = NP implies Frege has polynomially bounded proofs.
- judge:minimax-m3.1-flash-free: V1 uses two filter elements (soft stdDeviation 3.4 and soft2 stdDeviation 6); the brief allows at most one gaussian blur filter.
- judge:minimax-m3.1-flash-free: V2: four of the seven cards overlap (Hopper/Shannon, Shannon/Knuth, von Neumann/Turing), so the John von Neumann card and part of the Hopper text are covered, and the Ada-to-Turing arrow terminates on the Hopper card.
- judge:minimax-m3.1-flash-free: V3: the loop is exactly 60 s but not seamless - the earth (opacity 0.9) and the satellite (opacity 0.95, left 90 percent) snap to zero at t=0, contradicting the notes claim of a seamless dissolve.
- judge:minimax-m3.1-flash-free: V4: the y-axis tick labels contradict the plotted geometry - 55k is printed on the 50k gridline (y=229) and 65k on the 60k gridline (y=115); the 24 data points themselves are all computed correctly.

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

<!-- NIKBENCH:LEADERBOARD:END -->

## 🖼️ Visual showcase — what the models actually made

The VIS pillar is scored on what a model *draws, animates, and charts* — not what it describes. GitHub renders SVG in color; the round-1 curation below is the three strongest v2.0 VIS builds by peer vote (space-bunny-free **81.4**, big-pickle **80.7**, glm **78.6** /100 from the 7 non-self reviewers). v3.0 adds V5 Eiffel, V6 Taj Mahal and V7 Earth colour system to this showcase automatically after the next round: `python scripts/build_gallery.py`.

### V1 — Mona Lisa in ≤300 SVG shapes

Blind art fidelity: painters pose, folded hands, sfumato smile, from a text spec with no reference image. Peer-judged for recognizability and craft.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **space-bunny** | <img src="gallery/space-bunny-free_mona-lisa.svg" alt="space-bunny-free V1" width="210"> | 81.4 |
| **big-pickle** | <img src="gallery/big-pickle_mona-lisa.svg" alt="big-pickle V1" width="210"> | 80.7 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_mona-lisa.svg" alt="glm-5.3-flash-free V1" width="210"> | 78.6 |

### V2 — Seven Founders infographic (1200×700)

Fixed roster — Lovelace · Turing · von Neumann · Shannon · Hopper · Dijkstra · Knuth — on a *to-scale* 1800–2000 timeline. Wrong facts or wrong spacing = lost points.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **space-bunny** | <img src="gallery/space-bunny-free_seven-founders.svg" alt="space-bunny-free V2" width="330"> | 81.4 |
| **big-pickle** | <img src="gallery/big-pickle_seven-founders.svg" alt="big-pickle V2" width="330"> | 80.7 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_seven-founders.svg" alt="glm-5.3-flash-free V2" width="330"> | 78.6 |

### V3 — LIFTOFF: 60-second motion loop (HTML/CSS)

A 60-second animated web “video” with 4 timed beats. GitHub sandboxes scripts, so open these files in a browser to watch them loop — they are the real deliverables.

| Model | Open in browser (GitHub won't run it) | Peer VIS /100 |
|---|---|---:|
| **space-bunny** | [`gallery/space-bunny-free_liftoff.html`](gallery/space-bunny-free_liftoff.html) | 81.4 |
| **big-pickle** | [`gallery/big-pickle_liftoff.html`](gallery/big-pickle_liftoff.html) | 80.7 |
| **glm-5.3-flash** | [`gallery/glm-5-3-flash-free_liftoff.html`](gallery/glm-5-3-flash-free_liftoff.html) | 78.6 |

### V4 — Café revenue chart with an honesty trap (900×500)

Same CSV for every model. The trap: noise invites a big “trend”, the truth is a renovation effect ≈ nil and a single festival outlier at month 19. Reward goes to models that decompose instead of dramatize.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **space-bunny** | <img src="gallery/space-bunny-free_cafe-chart.svg" alt="space-bunny-free V4" width="330"> | 81.4 |
| **big-pickle** | <img src="gallery/big-pickle_cafe-chart.svg" alt="big-pickle V4" width="330"> | 80.7 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_cafe-chart.svg" alt="glm-5.3-flash-free V4" width="330"> | 78.6 |

### Bonus — F1 Mission Control (single-file dashboard)

The frontend task is visual too: a 10-requirement dashboard app. Open the real files.

| Model | Open in browser (GitHub won't run it) | Peer VIS /100 |
|---|---|---:|
| **space-bunny** | [`gallery/space-bunny-free_mission-control.html`](gallery/space-bunny-free_mission-control.html) | 81.4 |
| **big-pickle** | [`gallery/big-pickle_mission-control.html`](gallery/big-pickle_mission-control.html) | 80.7 |
| **glm-5.3-flash** | [`gallery/glm-5-3-flash-free_mission-control.html`](gallery/glm-5-3-flash-free_mission-control.html) | 78.6 |

_Full raw builds (all 8 models, all 4 visual tasks plus F1) live in `submissions/`
between rounds; the renders above are extracted verbatim by
`scripts/build_gallery.py` — no retouching. **Round-1 extras:** the three
featured B1 Clinic-API servers additionally pass a live contract smoke test
(`python scripts/smoke_b1.py`, Node run): create doctor → book **201** →
double-book **409 SLOT_TAKEN** → delete **204** → gone **404**, with clean
validation errors on malformed input. **Across the whole round** (full run:
`python scripts/verify_be.py` + `python scripts/verify_fe.py`): BE **6 PASS / 1
PARTIAL (longcat has no DELETE handler) / 1 NO-B1 (mimo, partial build)**; FE
**6 of 7 full-pass at 13/13, nemotron missing the `<main>` landmark (12/13)**._

## 🗂️ Repository map

```
nikBench/
├── test.md                     ← 🔫 THE one packet: routing → blind build (33 tasks) → peer+self → board refresh
├── judging/
│   ├── judge.md                ← 🧑‍⚖️ optional calibrated rubric judges (paste + submission → JSON scorecard v2)
│   └── peer-review.md          ← reference copy of the peer round (test.md embeds it)
├── docs/
│   ├── methodology.md          ← full protocol, verbatim task provenance (v3.0 checked 2026-10-19), dispute rules
│   └── roadmap.md              ← living backlog: what shipped in v3.0, what's queued for v3.1+
├── submissions/                ← candidate raw replies, one <model-name>.md each
├── peer/                       ← peer-round rating tables + self rows (one <model-name>.md each)
├── scorecards/                 ← optional rubric judge JSON outputs (v1 and v2 rubrics both accepted)
├── templates/scorecard.json    ← blank v3.0 scorecard shape (6 pillars, RAT 0–13)
├── examples/                   ← worked examples: v2.0 and v3.0 cards → example board
├── gallery/                    ← committed color renders from the latest round (README shows the VIS showcase)
├── scripts/
│   ├── aggregate.py            ← stdlib-only scorer → leaderboard.md (dual rubric, --selftest, --live)
│   ├── verify_be.py            ← boots every B1 server; ~30 live contract checks → 0–100
│   ├── verify_fe.py            ← F1 static spec checks (24 items) → 0–100
│   ├── verify_all.py           ← one-command round QA: structure + FE + BE per model
│   ├── verify_phase1.py        ← submission structure check (33 sections, 13 Final Answers)
│   ├── build_gallery.py        ← extracts V1–V7/ F1 renders into gallery/
│   └── _splice_board.py        ← refreshes the README board block from leaderboard.md
├── leaderboard.md              ← canonical generated board
└── .github/workflows/ci.yml    ← validates both rubrics on every push
```

## 🧠 Why "no answer key"?

Because the interesting part isn't whether a model *knows* that Boolos's gods can be disambiguated — it's whether it can:

- derive the full case tree instead of reciting it,
- argue the 100-prisoners cycle probability and the pirate backward induction instead of pattern-matching remembered answers,
- write a dossier on P vs NP (or black-hole information) that names the *actual* results without inventing citations — and without claiming to solve it,
- draw an Eiffel Tower whose platforms land where 57/115/276 m put them, a Taj Mahal symmetric to the pixel, and an Earth colour system whose WCAG ratios survive independent recomputation,
- keep a 60-second motion loop seamless,
- render a 10,000-row grid without melting the DOM, and
- refuse to sell a "+25% growth" story when month 19 is a festival outlier and the renovation did nothing.

Peer votes make this robust: every model rates every other **before** rating itself (self-inflation lands in its own labeled column). The rubric-judge path exists for when you want panel medians with outlier flags (Δ > 15 triggers disputes; disputed items are re-solved blind by panel majority), and execution verification keeps "it looks right" from beating "it runs right".

## 🏅 Grading scale

| Grade | Score | Meaning |
|:--:|---:|---|
| S | ≥ 90 | frontier: production-grade on all six pillars |
| A | ≥ 80 | excellent, minor gaps |
| B | ≥ 70 | solid generalist |
| C | ≥ 60 | functional, notable gaps |
| D | ≥ 45 | incomplete work on at least one pillar |
| F | < 45 | failed to produce usable submissions |
