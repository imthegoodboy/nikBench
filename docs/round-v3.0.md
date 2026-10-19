# Round notes — v3.0 "Hard Mode"

**Packet:** [`test.md`](../test.md) · 33 tasks · R1–R13, T1–T7, V1–V7, A1–A4, F1, B1 (D1–D6)
**Opened:** 2026-10-19 · **Status:** complete — the board is live in the README

This page records the exact roster, exclusions, and method for the v3.0 round so the
resulting board is reproducible and the historical v2.0 board is not silently rewritten.

## Result

| Rank | Model | Final | Grade | NBS | Peer | Self |
|:--:|---|---:|:--:|---:|---:|---:|
| 1 | `big-pickle` | **88.90** | A | 88.6 | 88.8 | 90.0 |
| 2 | `deepseek-v4.1-flash-free` | 87.57 | A | 89.1 | 85.5 | 85.0 |
| 3 | `mimo-v2.6-flash-free` | 86.46 | A | 87.9 | 83.7 | 85.0 |
| 4 | `glm-5.3-flash-free` | 80.72 | A | 85.4 | 82.5 | 65.0 |
| 5 | `nemotron-3.5-super-vl-free` | 77.94 | B | 75.6 | 73.0 | 90.0 |
| 6 | `beam-free` | 72.85 | B | 74.3 | 68.3 | 73.0 |
| 7 | `longcat-2.5-preview-free` | 72.19 | B | 76.7 | 80.8 | 50.0 |

Per-judge flags and dispute notes are in the README board's details block.

### What the judge actually caught

Every card was backed by re-solving R1–R13 and by executing the artifacts (headless
SVG/HTML renders at desktop and 375 px, live B1 endpoint probes, recomputed WCAG
luminance). Representative failures that moved scores:

- **V6 unilateral mirror (big-pickle, beam):** the mirrored and direct groups both land
  on the left half, so the Taj façade is one-sided — only 2 of the advertised 4 minarets
  render.
- **F1 palette visible on first paint (big-pickle):** `.overlay{display:flex}` overrides
  the UA `[hidden]{display:none}` rule; the palette also cannot be closed with Ctrl+K.
- **F1 placeholder (nemotron-super):** `allAnomalies()` returns `[]` with a literal
  `// placeholder`, so dismiss/undo never work; `<body class="theme dark">` also inherits
  the flex layout and breaks the page.
- **B1 hang without an Idempotency-Key (longcat):** POST creates the row but never sends
  a response; the overlap invariant is unreachable, so double-booking returns 201.
- **F1 rebuild ReferenceError (glm):** `VP` is undeclared in strict mode, so the 10k grid
  paints no rows on load and sorting/filtering/indicators never run.
- **V7 WCAG math (beam):** 4 of 5 claimed ratios are wrong; the contrast block is the
  checkable part of the task and was recomputed from the hexes.

## Roster

### Scored (7 complete builds)

| Candidate | Submission | Structure |
|---|---|---:|
| `big-pickle` | 267 KB | complete (13/13 finals) |
| `glm-5.3-flash-free` | 205 KB | complete (20 final-answer lines) |
| `deepseek-v4.1-flash-free` | 205 KB | complete (14 final-answer lines) |
| `mimo-v2.6-flash-free` | 239 KB | complete (20 final-answer lines) |
| `nemotron-3.5-super-vl-free` | 175 KB | complete (17 final-answer lines) |
| `longcat-2.5-preview-free` | 157 KB | complete (13/13 finals) |
| `beam-free` | 88 KB | complete (12/13 finals) |

Final-answer counts above 13 come from extra per-task "Final Answer" lines; the
structure verifier only requires the 13 contracted answers.

### Not scored in this round

| Candidate | Why |
|---|---|
| `nemotron-3-ultra-free` | Partial build — all R/T/V/A sections landed, but the F1 app and B1 API were repeatedly cut off by upstream `504` timeouts. Excluded rather than scored as a capability failure caused by provider instability. |
| `nemotron-3.5-lightning-free` | Partial build — the harness truncated its submission during the run (`write` instead of `edit`); R1–R13 were rebuilt, but T/V/A/F/B were not completed before the round was frozen. |
| `space-bunny-free` | Removed from the OpenCode model list before the round; it could not defend its v2.0 rank. The v2.0 board remains historical. |

## Judging

- **Rubric judge:** `minimax-m3.1-flash-free`, one independent judge per scored candidate,
  writing `nikbench.scorecard.v2` cards.
- **Why one judge:** the two previously independent free judges
  (`nemotron-3-ultra-free`, `nemotron-3.5-lightning-free`) were added as challengers in
  v3.0, leaving `minimax-m3.1-flash-free` as the only non-candidate free OpenCode model.
  OpenRouter judges are excluded by the benchmark's protocol, so this round trades panel
  width for independence. The board discloses `Judges = 1`; peer medians remain the
  multi-rater check on the same submissions.
- **Peer round:** the seven scored candidates rate each other (self row last, separate
  column). Peer and self each carry 20% of `Final` when present; missing peer data is
  redistributed rather than zeroed.

## Verification

- Structure: `python scripts/verify_phase1.py` (33 sections, 13 contracted finals,
  SVG/HTML/JS presence).
- Live: `python scripts/verify_be.py` boots every B1 server and runs the contract suite;
  `python scripts/verify_fe.py` runs the static F1 checks. Both are blended 50/50 into
  the BE/FE medians under `aggregate.py --live`.

| Candidate | BE (live contract) | FE (static, 24 checks) |
|---|---:|---:|
| `big-pickle` | 100 | 96 |
| `mimo-v2.6-flash-free` | 100 | 88 |
| `glm-5.3-flash-free` | 97 | 100 |
| `deepseek-v4.1-flash-free` | 97 | 96 |
| `beam-free` | 97 | 96 |
| `nemotron-3.5-super-vl-free` | 94 | 92 |
| `longcat-2.5-preview-free` | 74 | 100 |

Two verifier fixes were required to measure these honestly: `verify_fe.py` and
`verify_be.py` now accept the descriptive `## Section F — Frontend (F1)` /
`## Section B — Backend (B1)` headings as well as the contracted `## F1` / `## B1`
form. Without that, nemotron-super's present app and API were scored 0.

- Raw submissions, peer files, and scorecards stay untracked (`submissions/`, `peer/`,
  `scorecards/`); the v2.0 artifacts are preserved locally under `archive/v2.0/`.

## Honest limitations

- One rubric judge means no judge-spread diagnostics for this round; peer disagreement is
  still visible in the `Peer` vs `Self` columns.
- Two Nemotron builds were lost to provider/harness failures, not to the tasks
  themselves. Their absence is recorded here rather than hidden.
- The `space-bunny-free` removal makes the v3.0 roster a seven-model comparison, not a
  one-for-one rerun of v2.0.
