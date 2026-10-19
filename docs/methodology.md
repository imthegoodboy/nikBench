# NikBench — Methodology & Protocol (v3.0)

## What NikBench is

A **peer-judged benchmark for LLMs**, built around one promise: *no answer key exists anywhere in this repo*. A model under test receives `test.md`, produces a submission, later reads the other submissions and rates them (and itself, last), and the board in `README.md` updates itself. Two optional deep-grading paths (rubric judges, examples) exist for calibrating scores beyond pure peer votes.

Version history:

| Version | Shape |
|---|---|
| v1.0 | 3 pillars (reasoning / frontend / backend), 12 tasks |
| v1.1 | + peer/self round, Final = 0.6·NBS + 0.2·Peer + 0.2·Self |
| v1.2 | all-in-one idempotent `test.md` (one file drives build → review → board) |
| v2.0 | 6 pillars: RAT · THO · VIS · ALG · FE · BE — 25 tasks; execution verification blended into BE/FE; multi-judge medians |
| **v3.0** | **Hard Mode — 33 tasks: R1–R13 (hard tier: 100 prisoners/boxes, sum-and-product, five pirates) · T1–T7 (black-hole information) · V1–V7 (Eiffel, Taj Mahal, Earth colour system) · A1–A4 (sequence CRDT) · F1 (virtualised 10k-row app, command palette, undo/redo) · B1 (idempotency, ETags, cursor pagination, audit log)** |

## The six pillars & their weights

NBS (0–100) = Σ pillar_weight × median(judge pillar score). Pillar scores themselves are 0–100 (weighted criteria, see `scripts/aggregate.py` → `WEIGHTS_V1` for the v2.0 rubric and `WEIGHTS_V2` for v3.0).

| Pillar | weight | tasks (v3.0) | graded on |
|---|---:|---|---|
| RAT 🧩 ratiocination | 0.20 | R1–R13 | correct answers (derived, not recalled) + rigor + clarity; exact answers = 60 pts, 60/13 per task |
| THO 🧠 thought | 0.20 | T1–T7 | **no answers exist —** comprehension · synthesis (accuracy, no fake citations) · originality · argument rigor · intellectual candor |
| VIS 🎨 visual craft | 0.15 | V1–V7 | art fidelity & craft · architecture geometry/symmetry · colour system + recomputed WCAG ratios · infographic facts/design · motion design/timing · dataviz choice/honesty |
| ALG 🧮 algorithms | 0.15 | A1–A4 | correctness · complexity analysis · edge cases · communication · innovation (A4: CRDT convergence + interleaving + GC) |
| FE 🪟 frontend | 0.15 | F1 | functionality · performance (virtualisation) · interaction depth (palette, undo/redo) · visual design · code quality · accessibility · responsive |
| BE ⚙️ backend | 0.15 | B1 + D1–D6 | endpoint matrix, error envelope + request IDs · **protocol hardening** (idempotency, ETag/If-Match, cursors, audit) · security · validation · data modeling · design answers |

Final = `0.6·NBS + 0.2·Peer + 0.2·Self` (missing components redistribute evenly; momentum-free by design). Grades: S ≥ 90 · A ≥ 80 · B ≥ 70 · C ≥ 60 · D ≥ 45 · F < 45.

**Scorecard schemas.** Judges write `nikbench.scorecard.v2` (v3.0 rubric, RAT 0–13). The aggregator still accepts `nikbench.scorecard.v1` (v2.0 rubric, RAT 0–10) and scores each card under its own weights, so historical boards can be re-rendered without silently changing old grades.

## The flow (Phase Router; idempotent)

```
send test.md to a fresh chat with any model…
├─ no submissions/<you>.md?      → PHASE 1 blind build → write submission → "PHASE 1 COMPLETE — waiting for peers"
├─ your file exists, <3 others   → "PHASE 2 LOCKED — waiting for peers"
├─ ≥2 others → PHASE 2 peer round: read every submission, rate 6 pillars + overall (others first),
│                own row LAST (self) → peer/<you>.md → "PEER REVIEW WRITTEN"
└─ peer file exists → PHASE 3: python scripts/aggregate.py scorecards --peer-dir peer -o leaderboard.md
                     → paste between the NIKBENCH:LEADERBOARD markers in README.md → git push → "PHASE 3 COMPLETE"
```

Optional deep-grade: fresh chats with `judging/judge.md` + one submission each → `scorecards/<judge>__<candidate>.json` (schema v2).

Execution verification (Phase 3, recommended):
`python scripts/verify_be.py` boots every B1 server and drives the v3.0 contract over HTTP (health/request IDs, idempotency replay + conflict, overlap/priority, validation, pagination cursors, ETag/If-Match 428/412, cancel/delete state machine, audit log), returning a 0–100 score; `python scripts/verify_fe.py` checks the F1 static spec (now including virtualisation evidence, command palette, undo/redo, dual-series chart, high-DPI, no-network). Both scores blend 50/50 into the BE/FE medians under `--live`.

## The no-key promise

- Reasoning tasks (R1–R13) are famous classics or classic extensions so that **any competent judge can re-derive every answer independently**. The repo ships no canonical answers; judges are required to solve R1–R13 themselves *before* opening a submission.
- THO tasks (P vs NP, Navier–Stokes, Riemann, measurement problem, Sleeping Beauty, "what is life", black-hole information) are famous **open or contested** questions: there is nothing to leak. They are graded on the quality and *honesty* of thought.
- VIS/ALG/FE/BE have spec-based contracts; some anchors are checkable (Eiffel platform heights, Taj symmetry, WCAG ratios, cursor semantics) but the answer key is the spec, not hidden solutions.

## Contamination policy

- Classic statements are kept **verbatim** (fixed dates, fixed numbers, fixed names) so judges can independently re-solve; memorized recall without derivation is punished by the rigor/clarity criteria. R11–R13 are known problems too — their value is the derivation (cycle-structure argument, elimination table, backward induction).
- Candidates are blind-isolated in Phase 1: only `test.md` is readable; no rubric, no examples, no other submissions. Peer phase adds only `submissions/` + its own peer file.
- If a dispute arises over an exact answer, the packet's wording plus the cited public source resolves it; a panel majority (or, failing that, 0.5-credit on the disputed task) is the tie-break.

## Provenance of every task (v3.0 additions checked 2026-10-19)

| Task | Source (verbatim basis) | Link |
|---|---|---|
| R1 Boolos "Hardest Logic Puzzle Ever" | G. Boolos, *Harvard Review of Philosophy* 6 (1996) 62–65; clarifications per the standard reprint | https://en.wikipedia.org/wiki/The_Hardest_Logic_Puzzle_Ever |
| R2 Blue Eyes | Randall Munroe's definitive statement | https://xkcd.com/blue_eyes.html |
| R3 Cheryl's Birthday | SASMO 2015 (Dr Joseph Yeo Boon Wooi); Q24, verbatim | https://en.wikipedia.org/wiki/Cheryl's_Birthday |
| R4 Cheryl's Age | the 2015 sequel (NTU/SASMO), verbatim | https://en.wikipedia.org/wiki/Cheryl's_Birthday |
| R5 Zebra Puzzle | *Life International*, 17 Dec 1962, verbatim 15 clues | https://en.wikipedia.org/wiki/Zebra_puzzle |
| R6 Ant on a rubber band | Gardner 1982 *aha! Gotcha*; Wikipedia statement | https://en.wikipedia.org/wiki/Ant_on_a_rubber_rope |
| R7 100 prisoners & the light bulb | circulating classic (no single author); phrasing by NikBench | classic puzzle |
| R8 Two eggs, 100 floors | egg-dropping classic (DP folklore); phrasing by NikBench | classic puzzle |
| R9 Fly & the two trains | classic lore, associated with the von Neumann anecdote | classic puzzle |
| R10 Twelve coins | balance-puzzle classic (counterfeit, unknown sign) | https://en.wikipedia.org/wiki/Balance_puzzle |
| **R11 100 prisoners & 100 boxes** | classic introduced by Peter Bro Miltersen (variant of Gál–Miltersen); standard statement | https://en.wikipedia.org/wiki/100_prisoners_problem |
| **R12 Sum and Product** | Hans Freudenthal, *Nieuw Archief voor Wiskunde* (1969); the "impossible puzzle" | https://en.wikipedia.org/wiki/Sum_and_Product_Puzzle |
| **R13 Five pirates** | classic game-theory puzzle (backward induction); standard statement | https://en.wikipedia.org/wiki/Pirate_game |
| T1 P vs NP | Millennium-class CS problem | https://en.wikipedia.org/wiki/P_versus_NP_problem |
| T2 Navier–Stokes | Clay Mathematics Institute, Millennium Problem statement | https://www.claymath.org/millennium-problems/navier-stokes-equation |
| T3 Riemann Hypothesis | standard mathematical statement | https://en.wikipedia.org/wiki/Riemann_hypothesis |
| T4 Measurement problem | standard interpretation survey scope | https://en.wikipedia.org/wiki/Measurement_problem |
| T5 Sleeping Beauty | Elga (2000); Wikipedia summary | https://en.wikipedia.org/wiki/Sleeping_Beauty_problem |
| T6 What is Life? | nod to Schrödinger 1944; essay is the task | classic question |
| **T7 Black-hole information** | Hawking (1974/1976); Page (1993); AMPS (2012); Penington / Almheiri–Engelhardt–Marolf–Maxfield (2019); standard survey scope | https://en.wikipedia.org/wiki/Black_hole_information_paradox |
| V1 Mona Lisa | Leonardo da Vinci c. 1503–1519, public domain (Musée du Louvre) | — |
| V2 Seven Founders | public-history facts (Lovelace, Turing, von Neumann, Shannon, Hopper, Dijkstra, Knuth) | — |
| V3 LIFTOFF motion | original NikBench spec | — |
| V4 Café dataset | **synthetic, authored for NikBench** — embedded CSV; the analytics task is real: seasonality vs level vs outlier | — |
| **V5 Eiffel Tower** | Eiffel Tower (1889) public facts: 330 m overall, 125 m base, platforms at 57/115/276 m | https://en.wikipedia.org/wiki/Eiffel_Tower |
| **V6 Taj Mahal** | Taj Mahal (1632–1653) public facts: dome ≈ 73 m, minarets ≈ 40 m | https://en.wikipedia.org/wiki/Taj_Mahal |
| **V7 Earth colour system** | original NikBench spec; WCAG 2.1 contrast formula is the checkable anchor | https://www.w3.org/TR/WCAG21/#dfn-contrast-ratio |
| **A4 Sequence CRDT** | the RGA/LSEQ/Yjs problem class; original NikBench spec | https://crdt.tech/background |

## Dispute & outlier protocol

- Per-judge pillar details are published in the leaderboard `<details>` block; judges deviating > 15 points from the panel median overall are flagged.
- Suspected outlier or contamination: a majority of the panel re-judges blind; unresolved → 0.5 credit on the disputed item for all candidates equally.
- Self-reliability: every model rates itself (last row, `self: true`); the aggregate keeps Peer and Self visible as separate columns rather than hiding the delta.
- Mixed-rubric cards: if one candidate has both v1 and v2 scorecards, each card is scored under its own rubric and the flag surfaces the mix; medians are reported with that disclosure.

## Reproducibility

- Scorer: `python scripts/aggregate.py scorecards --peer-dir peer -o leaderboard.md` (stdlib-only, `--selftest` for CI; both rubrics exercised by `examples/scorecards`).
- Peer parser accepts dict- or list-shaped `ratings`, halves, and prose-wrapped JSON.
- Worked examples live in `examples/` (v2.0 card + v3.0 card).
- Cost tracking: the board carries a `Cost (est.)` column = input (test.md) + output (submission) tokens × published per-token price from `MODEL_PRICES` in `scripts/aggregate.py`; free-tier models report $0.00, unknown models report `—`. Phase 1 submissions open with a `nikbench.meta` header (`bench=v3.0 model=… date=… params=…`).
- Revision round (Phase 4, optional): a model may submit a patched version of only the changed sections plus a `CHANGELOG`; see `test.md` Phase 4.
- Difficulty is a first-class variable: v3.0 adds the hard tier, and the packet states the completion contract (stop cleanly + `<!-- incomplete: … -->` rather than placeholders).
