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
- **Multi-judge medians, not single scores.** `NBS` is the pillar-median across judges; the board shows `Judges` count and `Spread`, and any judge >15 points from the panel median is flagged in the details block. When the candidate roster itself removes the independent judges (v3.0), the round runs with a single free judge and discloses `Judges = 1` rather than borrowing a candidate.
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

> **Round status:** the board below is the completed **v3.0 Hard Mode round** — 7 scored models, one independent free rubric judge (`minimax-m3.1-flash-free`), and a seven-model peer round. `space-bunny-free` was removed by the provider; the two Nemotron challengers were attempted but excluded as partial builds (full disclosure: [`docs/round-v3.0.md`](docs/round-v3.0.md)). The scorer still accepts v2.0 cards (`nikbench.scorecard.v1`), so historical grades are never silently re-weighted. Regenerate with `python scripts/aggregate.py scorecards --peer-dir peer --live -o leaderboard.md`.

<!-- NIKBENCH:LEADERBOARD:START -->
_Last updated: 2026-10-19 06:32 UTC · scorer: `scripts/aggregate.py` · protocol: `docs/methodology.md`_

| Rank | Model | Final | Grade | NBS | Peer | Self | RAT | THO | VIS | ALG | FE | BE | Judges | Spread | Live (BE/FE) | Cost (est.) |
|---:|---|---:|:--:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:--:|---:|---:|---:|
| 1 | **big-pickle** | 88.90 | A | 88.6 | 88.8 | 90.0 | 96 | 89 | 82 | 82 | 87 | 92 | 1 | ±0.0 | 100/96 | $0.0000 |
| 2 | **deepseek-v4.1-flash-free** | 87.57 | A | 89.1 | 85.5 | 85.0 | 97 | 89 | 76 | 88 | 91 | 91 | 1 | ±0.0 | 97/96 | $0.0000 |
| 3 | **mimo-v2.6-flash-free** | 86.46 | A | 87.9 | 83.7 | 85.0 | 94 | 86 | 82 | 84 | 87 | 92 | 1 | ±0.0 | 100/88 | $0.0000 |
| 4 | **glm-5.3-flash-free** | 80.72 | A | 85.4 | 82.5 | 65.0 | 93 | 85 | 79 | 76 | 87 | 90 | 1 | ±0.0 | 97/100 | $0.0000 |
| 5 | **nemotron-3.5-super-vl-free** | 77.94 | B | 75.6 | 73.0 | 90.0 | 83 | 80 | 61 | 72 | 69 | 84 | 1 | ±0.0 | 94/92 | $0.0000 |
| 6 | **beam-free** | 72.85 | B | 74.3 | 68.3 | 73.0 | 86 | 76 | 52 | 59 | 81 | 88 | 1 | ±0.0 | 97/96 | $0.0000 |
| 7 | **longcat-2.5-preview-free** | 72.19 | B | 76.7 | 80.8 | 50.0 | 85 | 83 | 72 | 69 | 77 | 69 | 1 | ±0.0 | 74/100 | $0.0000 |

## Grade scale

| Grade | Score | Meaning |
|:--:|---:|---|
| S | ≥ 90 | frontier: production-grade on all six pillars |
| A | ≥ 80 | excellent, minor gaps |
| B | ≥ 70 | solid generalist |
| C | ≥ 60 | functional, notable gaps |
| D | ≥ 45 | incomplete work on at least one pillar |
| F | < 45 | failed to produce usable submissions |

**NBS** = rubric-judge score (weighted across the 6 pillar medians) · **Peer** = mean of the other models' ratings · **Self** = the model's own rating of itself (last, by design) · **Final** = `0.6·NBS + 0.2·Peer + 0.2·Self`. Pillars: **RAT** ratiocination (R1–R13 in v3.0) · **THO** thought (T1–T7) · **VIS** visual (V1–V7) · **ALG** algorithms (A1–A4) · **FE** frontend · **BE** backend. Grades follow **Final** when peer data exists. **Cost (est.)** = input (test.md) + output (submission) tokens × published per-token price; free-tier models report $0.00, unknown models report `—`. **Live (BE/FE)** = pass rate of `scripts/verify_be.py` / `scripts/verify_fe.py` (50/50 blended into BE/FE medians when both judge and live data exist).

<details>
<summary><b>Peer-round notes</b></summary>

### Peer-round notes

- **beam-free**: peer 68.3/100 from 6 reviewer(s), self 73.0/100
- **big-pickle**: peer 88.8/100 from 6 reviewer(s), self 90.0/100
- **deepseek-v4.1-flash-free**: peer 85.5/100 from 6 reviewer(s), self 85.0/100
- **glm-5.3-flash-free**: peer 82.5/100 from 6 reviewer(s), self 65.0/100
- **longcat-2.5-preview-free**: peer 80.8/100 from 6 reviewer(s), self 50.0/100
- **mimo-v2.6-flash-free**: peer 83.7/100 from 6 reviewer(s), self 85.0/100
- **nemotron-3.5-super-vl-free**: peer 73.0/100 from 6 reviewer(s), self 90.0/100

</details>


<details>
<summary><b>Per-judge details</b> (click to expand)</summary>

### beam-free — NBS 74.30 (B)

| Judge | Rubric | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| minimax-m3.1-flash-free | v3.0 | 86.0 | 76.2 | 51.9 | 58.8 | 65.2 | 78.5 | 70.6 |

Flags:
- judge:minimax-m3.1-flash-free: BE is contract-correct (30/31 on the repo's live suite, the only miss being an ETag on POST that the spec does not require), but a body over 1 MB returns 400 INVALID_JSON instead of 413, unsupported methods return 404 instead of 405, and the 500 envelope echoes raw exception messages.
- judge:minimax-m3.1-flash-free: FE functional bugs: the global keydown handler toggles the theme when 'd' is typed into the search field or palette input; below 640px the card mode renders only 5 rows because the hidden .grid-wrap reports clientHeight 0, with no way to scroll further; the palette has no focus trap and the sortable headers are not keyboard-reachable; light-theme muted text is about 2.7:1.
- judge:minimax-m3.1-flash-free: No contamination flag on RAT: R1-R13 all match my independent solutions and carry visible derivations (R1 case analysis, R2 induction, R6 harmonic integral, R11 cycle probability, R13 backward-induction table), with R12 the only hard-tier derivation thin enough to be worth a dispute.
- judge:minimax-m3.1-flash-free: R10's decision tree delegates the entire 'W1 right-heavy' branch to 'symmetric: swap the two sides of the left-heavy branch' and leaves the impossible 'W3: 3 vs 9 right-heavy' leaf unassigned, against the brief's 'no branch left unassigned'.
- judge:minimax-m3.1-flash-free: R12 does not deliver the required successive-elimination table (the brief says a bare memorised pair scores near zero). The answer (4,13) is correct and the filter rules are named, but only P=52 is worked through and 'only 52 survives' is asserted, not shown.
- judge:minimax-m3.1-flash-free: R8 contains visibly unedited scratch-work ('increments 14,13,...,4? actually ...') and two conflicting floor lists; the lower bound is stated as the d(d+1)/2 formula rather than proved.
- judge:minimax-m3.1-flash-free: V4's plotted geometry is wrong against the CSV: all twelve post-renovation points are ~10 px (about 1.7k EUR) too low, and the festival point is drawn at about 54.8k instead of 63.5k, so the drawn chart undercuts its own '+60%' headline; x-tick labels 12 and 18 are misplaced.
- judge:minimax-m3.1-flash-free: V6's bilateral-symmetry contract is broken: the mirrored <g transform='translate(900,0) scale(-1,1)'> and the second direct group both render on the left half, so all four minarets and all four cypress trees appear on one side and the right half has none. V6 also omits the required <!-- palette: ... --> comment.
- judge:minimax-m3.1-flash-free: V7's WCAG block fails recomputation on 4 of 5 pairs: atmosphere/ocean claimed 8.86 AAA vs true 6.11 (AA); ocean/ice claimed 4.56 AA vs true 9.31 (AAA) and inconsistent with the submission's own stated L_ocean=0.023; city/void 10.88 vs 13.09; sand/void 7.58 vs 10.10. V7 also uses three extra neutral tints (#111, #333, #889) beyond the allowed two.

### big-pickle — NBS 88.56 (A)

| Judge | Rubric | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| minimax-m3.1-flash-free | v3.0 | 96.0 | 89.0 | 81.9 | 82.5 | 78.0 | 84.8 | 86.1 |

Flags:
- judge:minimax-m3.1-flash-free: A1 complexity: the potential-function argument for amortised O(1) SET is self-contradictory as written ('Phi = 3n - cap/2 ... which is >= 0 exactly while n <= cap/6'). The conclusion (standard resize amortisation) is right; the proof as printed is not.
- judge:minimax-m3.1-flash-free: B1 security: the audit 'actor' is a client-supplied X-Actor header, so the audit trail is spoofable, and authentication/authorisation is only designed in D2 rather than implemented in the server.
- judge:minimax-m3.1-flash-free: F1 load-time defect (verified by rendering): '#palette' carries the hidden attribute but '.overlay{display:flex}' in the author stylesheet overrides the UA '[hidden]{display:none}' rule, so the command palette is open on first paint, with a full-page scrim. At <=640px it is a full-viewport sheet that hides the entire app at 375px. The Ctrl+K toggle also tests pal.hidden (which stays true), so the palette cannot be closed by the shortcut.
- judge:minimax-m3.1-flash-free: No contamination flag: every R answer, including the hard tier R11/R12/R13, carries its derivation - the cycle-structure probability argument, the successive elimination sets with a per-sum table, and the backward induction with the base cases, the >=half threshold and the bloodthirsty tie-break spelled out. Nothing looks recalled from a key.
- judge:minimax-m3.1-flash-free: R3: the candidate's 'Final Answer: July 16' is Albert's date. If the task key expects Cheryl's own birthday (May 15), the answer is stated incompletely - the derivation does exclude May and June, so May 15 follows, but it is never said. Scored as a match on the resolution of the dialogue; a stricter key would mark it partial.
- judge:minimax-m3.1-flash-free: R5 rigor: the branch that eliminates (ivory, green) = (3, 4) is narrated in a confused way - the text has house 4 drinking both coffee and OJ before reaching the contradiction. The final table is correct and I verified all 15 clues against it.
- judge:minimax-m3.1-flash-free: R7: the final answer is a triple (198 best case / unbounded worst case / ~10,418 expected). If the task wanted a single number, ~10,418 (100*H99 + 9900) is the likely key; the other two quantities are defensible readings of the same question.
- judge:minimax-m3.1-flash-free: V6 geometry bug (verified by rendering the submitted SVG): the left half is authored at x=110..450 and drawn only through <g transform='translate(900,0) scale(-1,1)>, so every replicated element lands right of the axis and the left half of the facade is empty. The board is visibly one-sided, only 2 of the 4 claimed minarets exist, and the annotation 'four minarets: 2 near (x 246 / 654), 2 far (x 292 / 608)' is false. The claimed '0 px symmetry error' does not hold for the rendered composition.
- judge:minimax-m3.1-flash-free: V7 layout nit: the last contrast row 'ice on sand (documented failure)' collides with its '1.85:1 FAIL' value at the panel edge, and the Earth disc's landmasses are schematic blobs rather than continents. The colour/contrast mathematics itself is exact.
- judge:minimax-m3.1-flash-free: Verification method note: I re-derived R1-R13 independently before reading the candidate, and additionally executed the submitted F1 page (headless render at 1280px and at a true 375px viewport via an iframe) and the submitted B1 server (node, full endpoint-matrix probe), plus recomputed all WCAG 2.1 luminances/ratios and the V5 deck-line pixel positions myself.

### deepseek-v4.1-flash-free — NBS 89.11 (A)

| Judge | Rubric | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| minimax-m3.1-flash-free | v3.0 | 97.0 | 88.8 | 76.2 | 88.5 | 86.0 | 84.2 | 87.4 |

Flags:
- judge:minimax-m3.1-flash-free: B1: POST /appointments omits an ETag header (the repo's live contract flags this as its only failure, 30/31); the idempotency check is evaluated before the malformed-JSON check, inverting the spec's stated priority 1 -> 2; and the shipped server has no authentication or rate limiting (designed only in D2/D3) while returning Access-Control-Allow-Origin: * on every response.
- judge:minimax-m3.1-flash-free: No contamination signal: every R1-R13 answer carries its own derivation, the hard-tier numbers match my independent computation exactly (0.3118; admissible sums {11,17,23,27,29,35,37,41,47,53}; 98/0/1/0/1), and the tone is worked-through rather than recalled.
- judge:minimax-m3.1-flash-free: R5 orientation is dispute-worthy: with the packet's 15 clues and clue 6 read literally ('the green house is immediately to the right of the ivory house', 'right means your right'), the unique solution is the candidate's table (Nor/Yel/Wat/Koo/Fox, Ukr/Blu/Tea/Che/Hor, Eng/Red/Mil/OG/Sni, Spa/Ivo/Ora/Luc/Dog, Jap/Grn/Cof/Par/Zeb), which is the mirror of the canonical Wikipedia 16-clue table (green 4 / ivory 5). I brute-forced both orientations: each has exactly one solution. The two answers the task asks for (Norwegian drinks water, Japanese owns the zebra) are identical under both readings, so the candidate's Final Answer is right either way; only the full table differs from the commonly circulated one.
- judge:minimax-m3.1-flash-free: V1 Mona Lisa fidelity is weak: frontal and symmetric rather than three-quarter, no sfumato smile, and the folded hands render as an unreadable blob.
- judge:minimax-m3.1-flash-free: V3 seam is not exactly seamless: the starfield twinkle phase is not 60-periodic, so t=60 and t=0 are not identical frames, and the V3-NOTES claim that both seam frames are black is inaccurate (stars are drawn at alpha 0.85 throughout). The flame also uses performance.now() rather than t, contradicting the note's 'all motion is analytic in t'.
- judge:minimax-m3.1-flash-free: V5 declares a 6-colour palette but renders 10 distinct hex values; V6 declares 8 but renders 14 - in both cases the extras are gradient stops/shades of the declared colours, so this reads as palette drift rather than a new palette.
- judge:minimax-m3.1-flash-free: V7's Earth disc does not clearly read as Earth - the land masses are amorphous green/tan blobs and the terminator is barely legible - although every checkable system requirement (exact hexes, WCAG maths, 60-30-10, palette-only rendering) is met.
- judge:minimax-m3.1-flash-free: Word-cap overruns (spec compliance, not placeholders): T1 ~660 words (cap 600), T6 ~429 (400), T7 ~549 (500), A4 ~924 (650); B1-D1 ~135, D5 ~130, D6 ~155 words (cap 120 each).

### glm-5.3-flash-free — NBS 85.37 (A)

| Judge | Rubric | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| minimax-m3.1-flash-free | v3.0 | 93.0 | 84.8 | 78.8 | 76.5 | 74.2 | 82.5 | 82.3 |

Flags:
- judge:minimax-m3.1-flash-free: A1: the DELETE operation is O(|k|) (leaf unlink + pruning to the next branch), not the O(1) the brief requires; this is disclosed honestly but the contract is not met.
- judge:minimax-m3.1-flash-free: BE: X-Actor is not propagated on the create paths - doctor_created and appointment_created always record actor 'anonymous' even when the client sends X-Actor (PATCH/DELETE do honour it).
- judge:minimax-m3.1-flash-free: BE: on an idempotent replay of a stored error body the envelope keeps the original request_id, so on a replay it differs from the X-Request-Id header of the replaying request (the spec asks for both 'replay exactly' and 'same value in the envelope').
- judge:minimax-m3.1-flash-free: FE (determinism): the chart bootstrap block (seed 1337) overwrites metrics.signal/metrics.fuel after the seed-42 initialisation and after localStorage restore, so 'identical seed -> identical metrics' and the persisted-metric continuity are both broken.
- judge:minimax-m3.1-flash-free: FE (functional defect): rebuild() calls 'VP.scrollTop=0' but VP is never declared and the script block is strict mode, so rebuild() throws a ReferenceError before updateSortIndicators()/scheduleRender(). The 10k grid therefore paints no rows on load (rows appear only after the user scrolls) and sorting, filtering and the required asc/desc indicator never work. The virtualisation itself is correct and real.
- judge:minimax-m3.1-flash-free: Independently verified positives: V7's six WCAG ratios recompute exactly (18.66, 10.10, 6.11, 13.09, 3.93, 3.27); V5's platform decks land at y = 711.8 / 571.2 / 180.9 against the required 712/571/181; V6 is exactly mirror-symmetric about x = 450; V2's seven birth-year positions are truthful on a 5.4 px/year axis; V3 loops at exactly 60.000 s with a true black-to-black seam and a proper reduced-motion poster; the B1 server boots and passes the endpoint matrix, idempotency replay/conflict, 428/412, cursor pagination without duplicates across inserts, legal touching slots and exactly one audit event per mutation.
- judge:minimax-m3.1-flash-free: No contamination flags: I re-solved R1-R13 before reading the submission; all thirteen Final Answers match my independent results and every one except R12 comes with a genuine derivation (R12 is the only case where part of the elimination is asserted rather than shown).
- judge:minimax-m3.1-flash-free: R12: the Layer-2 surviving-sum set is wrong (it adds 59,65,67,71,77,79,83,87,89,95,97; e.g. sum 59 dies because (6,53) -> product 318 has only one valid factorization under x+y<=100), and the Layer-4 elimination of the other sums is asserted by appeal to Freudenthal rather than shown. The pivotal s=17 product/sum cross-check is correct and auditable, and the answer 4/13 is right.
- judge:minimax-m3.1-flash-free: R1: the counterfactual lemma's four-case derivation contains a visible mid-derivation self-correction ('no - wait: ...'); the lemma itself (ja iff X is true for any non-Random god) and the resulting strategy are correct. Q3 is phrased once as 'Is A Random?' and then adapted per branch in the case analysis - a wording inconsistency, not a logic error.
- judge:minimax-m3.1-flash-free: R5: the full 5x5 table is the mirror image of the canonical solution - 'right' was read as the viewer's right, so green=5/ivory=4, Japanese=5, Spanish=4, whereas the canonical published solution (and the puzzle's clarifier 'right means YOUR right', with the Norwegian's house at the left) gives green=4/ivory=5, Japanese=4 owning the zebra, Spanish=4 owning the dog. The two contracted answers (Norwegian drinks water, Japanese owns the zebra) are correct; houses 1-3 are correct.
- judge:minimax-m3.1-flash-free: R8: the lower-bound recurrence is misstated - M(w)=M(w-1)+w+1 with M(0)=1 gives M(w)=(w+1)(w+2)/2, which would make 13 drops sufficient. The correct argument (M(w)=M(w-1)+w; 13*14/2=91 < 100 <= 14*15/2=105) appears in the next sentence and the answer 14 is right.
- judge:minimax-m3.1-flash-free: V2: Hopper's life bar is 382.8 px = 70.9 years, ending ~1977 although the label says 1992 (should be 464.4 px), and three of four milestone dots are at the wrong years (Turing 1918 instead of 1936, von Neumann 1939.4 instead of 1945, Shannon 1944.7 instead of 1948) although the caption advertises to-scale milestone placement. All seven birth-year positions are correct and every founder fact is accurate.
- judge:minimax-m3.1-flash-free: V4: the gridlines and y-axis tick labels are on a ~0.010753 px/EUR scale while the plotted series uses 0.0134483 px/EUR, so the axis misstates every value (the EUR 63.5k festival point is drawn where the axis reads ~EUR 70k) and contradicts the chart's own annotation. The 24 data points and the pre/post means (41,170 / 41,291 / +0.3% / +EUR 22.0k) are exact, and the honesty decomposition is correctly executed.

### longcat-2.5-preview-free — NBS 76.71 (B)

| Judge | Rubric | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| minimax-m3.1-flash-free | v3.0 | 85.4 | 82.8 | 71.8 | 69.2 | 54.5 | 64.0 | 72.5 |

Flags:
- judge:minimax-m3.1-flash-free: A3 CONSISTENCY: the prose says INCR is routed by hash(client)/round-robin for key splitting, but the hot-path pseudo-code uses hash(key) % N, which routes every client to the same shard - the key-splitting layer is not actually implemented on the hot path.
- judge:minimax-m3.1-flash-free: A4 CORRECTNESS: the claim that the (lamport, siteID) tie-break keeps each user's block contiguous is inconsistent with a per-character tie-break, which produces exactly the HWEOLRLLOD interleaving the task asks about; 'reject deletes of unknown ids' also conflicts with out-of-order delivery in a CRDT.
- judge:minimax-m3.1-flash-free: A4 MISSING DELIVERABLE: the required HWEOLRLLOD timeline is asserted in one sentence rather than shown as a concrete interleaving timeline; the safe-GC counterexample is present and good.
- judge:minimax-m3.1-flash-free: B1 FATAL RUNTIME BUG (verified by booting the server): POST /doctors and POST /appointments without an Idempotency-Key never return a response - handleIdempotency returns proceed()'s value without sending it - while the resource is still created server-side (visible as an orphaned audit event). The key is optional per the spec.
- judge:minimax-m3.1-flash-free: B1 SPEC VIOLATION (verified by booting the server): the no-overlap invariant never fires - overlaps() compares numeric epoch values with stored ISO strings - so 409 SLOT_TAKEN is unreachable and double bookings are accepted (a 10:15-10:45 booking over an existing 10:00-10:30 slot returned 201).
- judge:minimax-m3.1-flash-free: F1 FATAL RUNTIME BUG (verified by reading the extracted code): line 1604 uses an undefined identifier OVERCAN while the constant is OVERSCAN, so renderGrid() throws a ReferenceError on every call; the 10 000-row virtualised grid renders zero rows and the boot-time throw aborts the remaining boot statements.
- judge:minimax-m3.1-flash-free: F1 SECOND FATAL BUG: there is no 'scroll' listener on the viewport, so even with the typo fixed the virtualised window would never be recomputed while scrolling.
- judge:minimax-m3.1-flash-free: MINOR: R4's triple enumeration omits (16,1,9) (harmless); R10 misprints two leaf outcomes ('balance: 5L' should be 5H; 'right heavy: 2L' should be 'right light') though the twelve-coin tree is otherwise complete and correct; R11's parenthetical conflates two different classical cycle facts; R13 contains a visible mid-derivation self-correction ('wait, recheck:'); R1 repeats a heading and its Final Answer defers to the tables.
- judge:minimax-m3.1-flash-free: R1 DISPUTE: the double-embedding lemma is false. With R = 'da means yes iff Q' and D = 'If I asked you R, would you say da?', a True or False god answers 'da' iff ('da means yes' <-> Q) = (Q <-> sigma), so the decoding 'da <=> Q' only holds in the worlds where 'da' means 'yes'. The published embedded-question lemma (Roberts 2001; Rabern & Rabern 2008) requires the inner question to be Q itself. The strategy therefore fails (and misroutes Q2/Q3 to the Random god) whenever 'da' means 'no' - roughly half of all worlds. Scored 0 for R1; a panel re-check of the sigma-dependence is warranted.
- judge:minimax-m3.1-flash-free: STRENGTHS CONFIRMED: THO dossiers are accurate with no invented citations (T7's island/QES expression and WCAG math in V7 both check out exactly); V4's data honesty is correct and its pre/post means (41 170 vs 41 290.9 excluding the festival month, +0.29 %) reproduce exactly; V5's platform geometry lands inside +/-10 px of 712/571/181; BE's idempotency replay/conflict, ETag/If-Match 428/412, insert-safe keyset cursor, audit-with-actor and D1-D6 prose answers are all solid.
- judge:minimax-m3.1-flash-free: V2 LAYOUT: the Grace Hopper card (x 583-723) and the Claude Shannon card (x 637-777) overlap by 86 px and Shannon's later-drawn panel paints over Hopper's initials, name and years; the Knuth card also overlaps Shannon by 20 px.
- judge:minimax-m3.1-flash-free: V3 TIMING: the title layer's opacity curve keeps the 'NKB-1 // T-MINUS' card visible from 3.5 s to 56.5 s rather than the declared 0-8 s beat, so the beats do not read as separate scenes; and at the seam every layer is at opacity 0, so t=60 is not congruent to t=0 (black frame).
- judge:minimax-m3.1-flash-free: V4 GEOMETRY: the y-axis gridlines/labels are on a different scale from the plotted data (labels 42k-62k at y=352/310/267/224/182 vs the data scale's 369/309/248/187/126; up to ~56 px / 1.4 k EUR error), so values cannot be read off the chart. The 24 data points themselves are exactly right.

### mimo-v2.6-flash-free — NBS 87.87 (A)

| Judge | Rubric | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| minimax-m3.1-flash-free | v3.0 | 94.0 | 86.5 | 82.1 | 83.5 | 86.5 | 84.5 | 86.6 |

Flags:
- judge:minimax-m3.1-flash-free: BE security is the weakest pillar area: no authn/authz and no rate limiting are implemented (only sketched in D2/D3), the X-Actor header is client-spoofable, and the 500 handler echoes the raw exception message.
- judge:minimax-m3.1-flash-free: Independently re-derived and CONFIRMED CORRECT by this judge: V7's WCAG luminances and all six printed ratios (18.66, 12.24, 9.31, 6.53, 5.70, 4.32) plus cross-checks (2.01, 1.85); V4's pre mean 41,170 and post ex-festival mean 41,291 (+0.3%) and the 85.7 EUR/px geometry; V2's birth-year x-positions on the 5.2 px/year axis; R6's arrival time e^100000 - 1 s; R11's 1 - (H100 - H50) = 0.3118; R12's S=17 elimination table; R13's five-row backward induction.
- judge:minimax-m3.1-flash-free: No contamination indicators found: R1-R13 all carry derivations rather than recalled prose, including the hard tier (R11 cycle-structure argument, R12 elimination table, R13 base-case induction). No TODO/placeholder content; no external network assets in the SVG/HTML/JS.
- judge:minimax-m3.1-flash-free: R11 contains a false sub-statement ('the chance the cycle through i has length <= 50 is sum_{k=1}^{50} 1/k / ... = 1/2'); the correct per-prisoner figure is ~0.312, and the strategy's optimality is asserted rather than proved.
- judge:minimax-m3.1-flash-free: R12 stage-2 survivor list wrongly includes sum 51 (it is eliminated there by the split (17,34), product 578, whose only factorisation with sum <= 100 is (17,34)); the stage-4 elimination list is incomplete ('37: 160', '47: 196 and ...'). The final answer (4,13) and the S=17 table are correct.
- judge:minimax-m3.1-flash-free: R13's 'strict majority' sensitivity chain misstates the 2-pirate stage (D cannot buy E for 1 coin since E would get 100 alone); the headline allocation (98,0,1,0,1) is correct.
- judge:minimax-m3.1-flash-free: R2's parenthetical about the brown-eyed islanders ('would leave on night 101 only if...') is muddled, though the stated conclusion - they never leave - is correct.
- judge:minimax-m3.1-flash-free: R5's rejection of the (ivory,green)=(3,4) case is written nonsensically (asserts the dog lands in house 1); the final table satisfies all 15 clues under the candidate's mirror convention for clue 6, and the two headline answers (Norwegian/water, Japanese/zebra) are canonical.
- judge:minimax-m3.1-flash-free: Spec-contract deviation: the file omits the required '<!-- nikbench.meta: bench=v3.0 model=... -->' first line.
- judge:minimax-m3.1-flash-free: V3 seam defect: the starfield rotation advances 0.12 turns per 60 s loop, so t=60 is not identical to t=0 (43-degree pop), contradicting the code comment's claim of seam continuity.
- judge:minimax-m3.1-flash-free: V6 omits the required cypress trees and the reflecting pool carries no reflection of the building.
- judge:minimax-m3.1-flash-free: VIS spec deviations: V5 root viewBox is 0 0 900 900 (spec: 600x900) and V6 root viewBox is 0 0 900 900 (spec: 900x600). The checkable V5 platform anchors still land exactly on y=712/570.5/180.5.
- judge:minimax-m3.1-flash-free: Word-cap overruns across THO: T5 ~582 words (cap 400), T6 ~650 (cap 400), T7 ~821 (cap 500), T1 658 / T2 646 / T3 725 / T4 681 (cap 600 each); A2 595 (cap 550), A4 746 (cap 650), B1-D6 137 (cap 120). Measured mechanically.

### nemotron-3.5-super-vl-free — NBS 75.56 (B)

| Judge | Rubric | RAT | THO | VIS | ALG | FE | BE | Judge overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| minimax-m3.1-flash-free | v3.0 | 83.4 | 79.8 | 61.4 | 71.5 | 45.8 | 75.0 | 70.7 |

Flags:
- judge:minimax-m3.1-flash-free: BE live-test deviations (server booted and exercised): PATCH is allowed from 'confirmed' although the spec says only from 'scheduled'; DELETE leaves the row queryable as 200 because it is modelled as status='cancelled'; limit=1.5 is accepted; the date filter only matches Z-suffixed starts; the X-Request-Id echo accepts UUIDv4 only.
- judge:minimax-m3.1-flash-free: F1 dead code: allAnomalies() returns [] with an explicit '// placeholder' comment, so the X dismiss handler always early-returns - dismissal and undo-of-dismiss never work. This is a placeholder in a feature the spec requires.
- judge:minimax-m3.1-flash-free: F1 layout: <body class="theme dark"> inherits the .theme rule (display:flex; align-items:center), so the body becomes a row flex container - the header renders mid-viewport and the countdown sits beside it (headless renders at 1280px and 375px both show this).
- judge:minimax-m3.1-flash-free: F1 other breaks: the light theme never applies (variables only overridden under prefers-color-scheme), #cards is never populated so the <640px card mode is empty, metric values are saved but never restored, metrics tick every 1s instead of 5s, the crosshair tooltip is positioned against the page rather than the chart, and there is no 2-column tablet breakpoint.
- judge:minimax-m3.1-flash-free: F1 virtualisation bug: the 400,000px spacer div is in flow before the table, pushing the table below the fold - the grid renders blank at load and the scroll window index is off by the full list height. The DOM-level virtualisation itself (only ~26 rows) is correct.
- judge:minimax-m3.1-flash-free: No contamination flag: R10-R13 are derived rather than recalled (I re-derived the 12-coin tree, the 1/L cycle law, the Freudenthal eliminations and the pirate table independently and they agree), and the THO section contains no invented citations or claim to have solved an open problem - T7's attributions and the island formula are faithful and it explicitly states the problem is not experimentally settled.
- judge:minimax-m3.1-flash-free: R1 rigor gap: the inference 'da => A is Random' is invalid when the respondent B is itself Random; the chosen non-Random god G happens to be correct in every branch (I simulated all 6 worlds), but the promised 8-branch case analysis is asserted rather than shown - a panel judge could read this as a broken strategy.
- judge:minimax-m3.1-flash-free: R11 and R12 assert the two conclusions the rubric explicitly demands as derivations: R11's optimality ('this is the known optimal strategy') and R12's uniqueness ('no other (x,y) satisfies the full dialogue (verified by the elimination sets)'). The probability work in R11 is rigorous; the elimination table in R12 is only partially exposed.
- judge:minimax-m3.1-flash-free: R7 compound answer is materially wrong: best case is >=198 visits (99 signaller visits + 99 counter consumptions), not the stated '~100' (their own justification contradicts the headline number), and 'expected ~10^4 (order n^2 log n)' is unsupported; liveness also needs repeated visits, which the prompt guarantees only once each. This is the one R-task I did not credit.
- judge:minimax-m3.1-flash-free: V2 render: three of seven founder cards overlap and one (Turing) is ~100% hidden behind Shannon's; every one-line fact overflows its 120px card because SVG <text> does not wrap; both influence arrows are hidden behind cards. The underlying content (facts + truthful to-scale x mapping) is correct.
- judge:minimax-m3.1-flash-free: V3 timing: animation-delay is additive with keyframe percentages, so the countdown digits actually fire 18.0-33.0s (only '10'..'6' land in the wrapper's 9-25s window; '0' never appears) and the claimed 8-25s beat is wrong; the satellite/earth pop at the t=60 seam rather than dissolving; reduced-motion leaves .num/.star/.cloud animating.
- judge:minimax-m3.1-flash-free: V4 render: the polyline y-values are not a function of the CSV (m3=41100 -> y235.3 but m16=41100 -> y248.3; m1=38800 plotted at 246.7 vs the 356.9 implied by the declared scale), the y-axis labels are on a broken scale (35000/40000/45000 then 65000 in one equal step), and the x tick labels (1,6,12,18,24) sit at x=70/200/330/460/590 instead of 70/239.6/443/646.5/850. The honesty of the story is intact; the geometry is not.
- judge:minimax-m3.1-flash-free: V7 render: the WCAG block is translated to y=720 (cards spanning 728-1006) and the typography block to y=785, so three of four contrast cards and the whole type hierarchy are clipped outside the 1200x800 viewBox, and the 60-30-10 bar collides with the contrast block. The contrast math itself is correct (I recomputed 18.66 / 12.25 / 5.70 / 4.75 from the hexes).
- judge:minimax-m3.1-flash-free: VIS XML-portability: the fenced SVGs are authored for HTML embedding, not standalone XML. V1 contains a double hyphen inside a comment ('earth tones -- skin') -> XML parse error, the file renders NOTHING; V2 uses &rarr;/&ndash;, V5/V6/V7 use &middot;/&mdash;/&ndash;/&asymp;/&ccedil; -> standalone rendering aborts at the first entity (V5 loses its required annotation block and scale bar, V7 loses its footer). After substituting the entities, all six render. Judges will score this differently depending on whether they inline the SVG into HTML or open the .svg file - I flagged it rather than treating it as fatal.

</details>

<!-- NIKBENCH:LEADERBOARD:END -->

## 🖼️ Visual showcase — what the models actually made

The VIS pillar is scored on what a model *draws, animates, and charts* — not what it describes. GitHub renders SVG in color; the curation below is the three strongest VIS builds of the round by peer vote (big-pickle **90.0**, glm-5.3-flash **86.0**, deepseek-v4.1-flash **86.0** /100 from the non-self reviewers). Regenerate with `python scripts/build_gallery.py` then `python scripts/insert_showcase.py`.

### V1 — Mona Lisa in ≤300 SVG shapes

Blind art fidelity: painters pose, folded hands, sfumato smile, from a text spec with no reference image. Peer-judged for recognizability and craft.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | <img src="gallery/big-pickle_mona-lisa.svg" alt="big-pickle V1" width="210"> | 90.0 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_mona-lisa.svg" alt="glm-5.3-flash-free V1" width="210"> | 86.0 |
| **deepseek-v4.1-flash** | <img src="gallery/deepseek-v4-1-flash-free_mona-lisa.svg" alt="deepseek-v4.1-flash-free V1" width="210"> | 86.0 |

### V2 — Seven Founders infographic (1200×700)

Fixed roster — Lovelace · Turing · von Neumann · Shannon · Hopper · Dijkstra · Knuth — on a *to-scale* 1800–2000 timeline. Wrong facts or wrong spacing = lost points.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | <img src="gallery/big-pickle_seven-founders.svg" alt="big-pickle V2" width="330"> | 90.0 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_seven-founders.svg" alt="glm-5.3-flash-free V2" width="330"> | 86.0 |
| **deepseek-v4.1-flash** | <img src="gallery/deepseek-v4-1-flash-free_seven-founders.svg" alt="deepseek-v4.1-flash-free V2" width="330"> | 86.0 |

### V3 — LIFTOFF: 60-second motion loop (HTML/CSS)

A 60-second animated web “video” with 4 timed beats. GitHub sandboxes scripts, so open these files in a browser to watch them loop — they are the real deliverables.

| Model | Open in browser (GitHub won't run it) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | [`gallery/big-pickle_liftoff.html`](gallery/big-pickle_liftoff.html) | 90.0 |
| **glm-5.3-flash** | [`gallery/glm-5-3-flash-free_liftoff.html`](gallery/glm-5-3-flash-free_liftoff.html) | 86.0 |
| **deepseek-v4.1-flash** | [`gallery/deepseek-v4-1-flash-free_liftoff.html`](gallery/deepseek-v4-1-flash-free_liftoff.html) | 86.0 |

### V4 — Café revenue chart with an honesty trap (900×500)

Same CSV for every model. The trap: noise invites a big “trend”, the truth is a renovation effect ≈ nil and a single festival outlier at month 19. Reward goes to models that decompose instead of dramatize.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | <img src="gallery/big-pickle_cafe-chart.svg" alt="big-pickle V4" width="330"> | 90.0 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_cafe-chart.svg" alt="glm-5.3-flash-free V4" width="330"> | 86.0 |
| **deepseek-v4.1-flash** | <img src="gallery/deepseek-v4-1-flash-free_cafe-chart.svg" alt="deepseek-v4.1-flash-free V4" width="330"> | 86.0 |

### V5 — Eiffel Tower architectural elevation (hard tier, 600×900)

To-scale engineering: platforms pinned at 57 / 115 / 276 m on a linear height map, ≥40 visible lattice elements, and an in-SVG annotation block. Judges measure the y-coordinates — a pretty silhouette with wrong decks loses.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | <img src="gallery/big-pickle_eiffel-tower.svg" alt="big-pickle V5" width="210"> | 90.0 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_eiffel-tower.svg" alt="glm-5.3-flash-free V5" width="210"> | 86.0 |
| **deepseek-v4.1-flash** | <img src="gallery/deepseek-v4-1-flash-free_eiffel-tower.svg" alt="deepseek-v4.1-flash-free V5" width="210"> | 86.0 |

### V6 — Taj Mahal bilateral symmetry (hard tier, 900×600)

One mirrored `<g>` half, true about x = 450 within 1 px, four separate minarets, dome taller than the towers, pool reflection. The round's sharpest failure mode: mirrored groups that land on the same side and leave the façade one-sided.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | <img src="gallery/big-pickle_taj-mahal.svg" alt="big-pickle V6" width="330"> | 90.0 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_taj-mahal.svg" alt="glm-5.3-flash-free V6" width="330"> | 86.0 |
| **deepseek-v4.1-flash** | <img src="gallery/deepseek-v4-1-flash-free_taj-mahal.svg" alt="deepseek-v4.1-flash-free V6" width="330"> | 86.0 |

### V7 — Earth colour system (hard tier, 1200×800)

A design-system board, not a poster: an Earth disc built only from eight fixed tokens, eight swatch cards, a WCAG 2.1 contrast block with ratios to two decimals, a 60-30-10 bar, and a type hierarchy. Judges recompute every contrast ratio.

| Model | Render (in color, straight from the submission) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | <img src="gallery/big-pickle_earth-color-system.svg" alt="big-pickle V7" width="420"> | 90.0 |
| **glm-5.3-flash** | <img src="gallery/glm-5-3-flash-free_earth-color-system.svg" alt="glm-5.3-flash-free V7" width="420"> | 86.0 |
| **deepseek-v4.1-flash** | <img src="gallery/deepseek-v4-1-flash-free_earth-color-system.svg" alt="deepseek-v4.1-flash-free V7" width="420"> | 86.0 |

### Bonus — F1 Mission Control (single-file dashboard)

The frontend task is visual too: a 10-requirement dashboard app. Open the real files.

| Model | Open in browser (GitHub won't run it) | Peer VIS /100 |
|---|---|---:|
| **big-pickle** | [`gallery/big-pickle_mission-control.html`](gallery/big-pickle_mission-control.html) | 90.0 |
| **glm-5.3-flash** | [`gallery/glm-5-3-flash-free_mission-control.html`](gallery/glm-5-3-flash-free_mission-control.html) | 86.0 |
| **deepseek-v4.1-flash** | [`gallery/deepseek-v4-1-flash-free_mission-control.html`](gallery/deepseek-v4-1-flash-free_mission-control.html) | 86.0 |

_Full raw builds live in `submissions/` between rounds; the renders above are extracted verbatim by `scripts/build_gallery.py` — no retouching. Per-model live BE/FE numbers are in the live column of the board above._

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
