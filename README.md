# ⚡ NikBench v2.0 — the peer-judged LLM benchmark

![tests](https://img.shields.io/badge/tests-25-blue) ![pillars](https://img.shields.io/badge/pillars-6-purple) ![answer_key](https://img.shields.io/badge/answer_key-none-red) ![protocol](https://img.shields.io/badge/protocol-v2.0-green)

**NikBench measures what models can *do* and *think* — not what they can memorize.** Paste `test.md` into a fresh chat with any model, and the packet runs the whole pipeline itself: blind build → peer review (every model rates every other model, plus honest self-rating) → leaderboard refresh with `git push`.

> 🔒 **No answer key exists anywhere in this repo.** Ten tasks are famously derivable classics (judges re-solve them independently); six are famous open problems that *have no answers* — the models are graded on the quality and honesty of their thought; the rest are contract specs.

## 🧩 The six pillars

| Pillar | Tasks | What it tests | Weight |
|---|---|---|---:|
| 🧩 **RAT** — Ratiocination | R1–R10 | 10 monster classics: Boolos's *Hardest Logic Puzzle Ever*, Blue Eyes, Cheryl's Birthday (+ its sequel!), the 1962 Zebra Puzzle, the ant on the stretching band, the prisoners & the lamp, two eggs, the fly & the trains, twelve coins | 20% |
| 🧠 **THO** — Thought | T1–T6 | famous **open/unsolved** questions — P vs NP, Navier–Stokes (Clay), Riemann, the quantum measurement problem, Sleeping Beauty, "what is life?" — graded on comprehension, accurate survey, original attack, rigor, **candor** | 20% |
| 🎨 **VIS** — Visual craft | V1–V4 | SVG recreation of the Mona Lisa · "Seven Founders of Computing" infographic (fact-checked) · a **60-second looping LIFTOFF motion graphic** in one HTML file · a data-visualization with a built-in **outlier honesty trap** | 15% |
| 🧮 **ALG** — Algorithm design | A1–A3 | O(1) KV store with O(k) prefix-scan · streaming distinct-count sketches · sharding a melting hot-key hashtag counter | 15% |
| 🪟 **FE** — Frontend | F1 | "Mission Control": live clock, seeded metrics, countdown, sortable satellite table, canvas telemetry, localStorage, themes, responsive, a11y | 15% |
| ⚙️ **BE** — Backend | B1 | "Clinic Appointment API": bare-Node router, error envelope, booking-overlap state machine, 5 design questions | 15% |

Full rubric criteria: [`judging/judge.md`](judging/judge.md) · task provenance (all verbatim-sourced, links checked): [`docs/methodology.md`](docs/methodology.md)

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

<!-- NIKBENCH:LEADERBOARD:START -->
_NikBench v2.0 board reset — no live run recorded yet. Send `test.md` to the candidates to start one._

Scoring when a run arrives: **Final** = `0.6·NBS + 0.2·Peer + 0.2·Self` (NBS = rubric-judge score if judges ran, else peer/self-only with disclosure). Grades: S ≥ 90 · A ≥ 80 · B ≥ 70 · C ≥ 60 · D ≥ 45 · F < 45.
<!-- NIKBENCH:LEADERBOARD:END -->

## 🗂️ Repository map

```
nikBench/
├── test.md                     ← 🔫 THE one packet: routing → blind build (25 tasks) → peer+self → board refresh
├── judging/
│   ├── judge.md                ← 🧑‍⚖️ optional calibrated rubric judges (paste + submission → JSON scorecard)
│   └── peer-review.md          ← reference copy of the peer round (test.md embeds it)
├── docs/
│   └── methodology.md          ← full protocol, verbatim task provenance (checked 2026-10-18), dispute rules
├── submissions/                ← candidate raw replies, one <model-name>.md each
├── peer/                       ← peer-round rating tables + self rows (one <model-name>.md each)
├── scorecards/                 ← optional rubric judge JSON outputs
├── templates/scorecard.json    ← blank scorecard shape (6 pillars)
├── examples/                   ← worked example: 3 judges scoring a demo candidate → example board
├── scripts/aggregate.py        ← stdlib-only scorer → leaderboard.md (supports --selftest, peer-only boards)
├── leaderboard.md              ← canonical generated board
└── .github/workflows/ci.yml    ← validates the scorer on every push
```

## 🧠 Why "no answer key"?

Because the interesting part isn't whether a model *knows* that Boolos's gods can be disambiguated — it's whether it can:

- derive the full case tree instead of reciting it,
- write a dossier on P vs NP that names the *actual* barrier results without inventing citations (and without claiming to solve it!),
- draw a Mona Lisa that reads at thumbnail size in ≤300 SVG elements,
- keep a 60-second motion loop seamless,
- refuse to sell a "+25% growth" story when month 19 is a festival outlier and the renovation did nothing.

Peer votes make this robust: every model rates every other **before** rating itself (self-inflation lands in its own labeled column). The rubric-judge path exists for when you want panel medians with outlier flags (σ > 15 triggers disputes; disputed items are re-solved blind by panel majority).

## 🏅 Grading scale

| Grade | Score | Meaning |
|:--:|---:|---|
| S | ≥ 90 | frontier: production-grade on all six pillars |
| A | ≥ 80 | excellent, minor gaps |
| B | ≥ 70 | solid generalist |
| C | ≥ 60 | functional, notable gaps |
| D | ≥ 45 | incomplete work on at least one pillar |
| F | < 45 | failed to produce usable submissions |
