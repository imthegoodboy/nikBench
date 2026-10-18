# NikBench — Methodology & Protocol (v2.0)

## What NikBench is

A **peer-judged benchmark for LLMs**, built around one promise: *no answer key exists anywhere in this repo*. A model under test receives `test.md`, produces a submission, later reads the other submissions and rates them (and itself, last), and the board in `README.md` updates itself. Two optional deep-grading paths (rubric judges, examples) exist for calibrating scores beyond pure peer votes.

Version history:

| Version | Shape |
|---|---|
| v1.0 | 3 pillars (reasoning / frontend / backend), 12 tasks |
| v1.1 | + peer/self round, Final = 0.6·NBS + 0.2·Peer + 0.2·Self |
| v1.2 | all-in-one idempotent `test.md` (one file drives build → review → board) |
| **v2.0** | **6 pillars: RAT · THO · VIS · ALG · FE · BE — 25 tasks (10 exact-answer classics, 6 open thought problems, 4 visual, 3 algorithm designs, 1 frontend, 1 backend)** |

## The six pillars & their weights

NBS (0–100) = Σ pillar_weight × median(judge pillar score). Pillar scores themselves are 0–100 (weighted criteria, see `scripts/aggregate.py` → `WEIGHTS`).

| Pillar | weight | tasks | graded on |
|---|---:|---|---|
| RAT 🧩 ratiocination | 0.20 | R1–R10 | correct answers (derived, not recalled) + rigor + clarity |
| THO 🧠 thought | 0.20 | T1–T6 | **no answers exist —** comprehension · synthesis (accuracy, no fake citations) · originality · argument rigor · intellectual candor |
| VIS 🎨 visual craft | 0.15 | V1–V4 | art fidelity & craft · infographic fact/design · motion design & timing · dataviz choice & honesty |
| ALG 🧮 algorithms | 0.15 | A1–A3 | correctness · complexity analysis · edge cases · communication · innovation |
| FE 🪟 frontend | 0.15 | F1 | the 10-spec contract, executed mentally |
| BE ⚙️ backend | 0.15 | B1 | endpoint matrix, error envelope, invariants a→f, design answers |

Final = `0.6·NBS + 0.2·Peer + 0.2·Self` (missing components redistribute evenly; momentum-free by design). Grades: S ≥ 90 · A ≥ 80 · B ≥ 70 · C ≥ 60 · D ≥ 45 · F < 45.

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

Optional deep-grade: fresh chats with `judging/judge.md` + one submission each → `scorecards/<judge>__<candidate>.json`.

## The no-key promise

- Reasoning tasks (R1–R10) are famous classics so that **any competent judge can re-derive every answer independently**. The repo ships no canonical answers; judges are required to solve R1–R10 themselves *before* opening a submission.
- THO tasks (P vs NP, Navier–Stokes, Riemann, measurement problem, Sleeping Beauty, "what is life") are famous **open or contested** questions: there is nothing to leak. They are graded on the quality and *honesty* of thought.
- VIS/ALG/FE/BE have spec-based contracts; no "answer" exists beyond the spec.

## Contamination policy

- Classic statements are kept **verbatim** (fixed dates, fixed numbers, fixed names) so judges can independently re-solve; memorized recall without derivation is punished by the rigor/clarity criteria.
- Candidates are blind-isolated in Phase 1: only `test.md` is readable; no rubric, no examples, no other submissions. Peer phase adds only `submissions/` + its own peer file.
- If a dispute arises over an exact answer, the packet's wording plus the cited public source resolves it; a panel majority (or, failing that, 0.5-credit on the disputed task) is the tie-break.

## Provenance of every task (checked 2026-10-18)

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
| T1 P vs NP | Millennium-class CS problem | https://en.wikipedia.org/wiki/P_versus_NP_problem |
| T2 Navier–Stokes | Clay Mathematics Institute, Millennium Problem statement | https://www.claymath.org/millennium-problems/navier-stokes-equation |
| T3 Riemann Hypothesis | standard mathematical statement | https://en.wikipedia.org/wiki/Riemann_hypothesis |
| T4 Measurement problem | standard interpretation survey scope | https://en.wikipedia.org/wiki/Measurement_problem |
| T5 Sleeping Beauty | Elga (2000); Wikipedia summary | https://en.wikipedia.org/wiki/Sleeping_Beauty_problem |
| T6 What is Life? | nod to Schrödinger 1944; essay is the task | classic question |
| V1 Mona Lisa | Leonardo da Vinci c. 1503–1519, public domain (Musée du Louvre) | — |
| V2 Seven Founders | public-history facts (Lovelace, Turing, von Neumann, Shannon, Hopper, Dijkstra, Knuth) | — |
| V3 LIFTOFF motion | original NikBench spec | — |
| V4 Café dataset | **synthetic, authored for NikBench** — embedded CSV; the analytics task is real: seasonality vs level vs outlier | — |

## Dispute & outlier protocol

- Per-judge pillar details are published in the leaderboard `<details>` block; judges deviating > 15 points from the panel median overall are flagged.
- Suspected outlier or contamination: a majority of the panel re-judges blind; unresolved → 0.5 credit on the disputed item for all candidates equally.
- Self-reliability: every model rates itself (last row, `self: true`); the aggregate keeps Peer and Self visible as separate columns rather than hiding the delta.

## Reproducibility

- Scorer: `python scripts/aggregate.py scorecards --peer-dir peer -o leaderboard.md` (stdlib-only, `--selftest` for CI).
- Peer parser accepts dict- or list-shaped `ratings`, halves, and prose-wrapped JSON.
- Worked example (3 judges × demo candidate) lives in `examples/`.
- Cost tracking: the board carries a `Cost (est.)` column = input (test.md) + output (submission) tokens × published per-token price from `MODEL_PRICES` in `scripts/aggregate.py`; free-tier models report $0.00, unknown models report `—`. Phase 1 submissions now open with a `nikbench.meta` header (model, date, params) for comparability.
- Revision round (Phase 4, optional, v2.1+): a model may submit a patched version of only the changed sections plus a `CHANGELOG`; see `test.md` Phase 4.
