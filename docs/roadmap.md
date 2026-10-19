# NikBench improvement roadmap (v3.0 shipped → v3.1+)

> Companion to `docs/methodology.md`. This file is the **living backlog**. Status tags:
> `[done]` shipped, `[next]` queued, `[idea]` needs design.
>
> **v3.0 "Hard Mode" shipped 2026-10-19**: 33 tasks, new difficulty tier, harder F1/B1
> contracts, dual-rubric scorer, relaxed verification tooling. Items below are re-baselined
> against it.

## 0. What the v2.0 round taught us (historical data, not vibes)

| Signal | Evidence | Implication | Status in v3.0 |
|---|---|---|---|
| Judge ≠ peers disagree sharply | beam: judge 100 vs peer 71.3; deepseek: judge spread 28 | Single-judge NBS is fragile | `[done]` multi-judge median + spread + outlier flags |
| Self-inflation is real but bounded | beam self 85 vs peer 71.3 (+13.7) | Keep self-row-last; track the gap | `[done]` Peer/Self columns |
| Static review misses real bugs | longcat had no DELETE handler; nemotron missing `<main>` | Execution verification must be in the pipeline | `[done]` `verify_be.py` now drives 30+ live contract checks; `verify_fe.py` 24 static checks |
| Peers catch what judges miss | space-bunny caught fabricated citations | Keep both rounds | `[planned]` keep peer round in v3.1 |
| Classic puzzles are memorizable | R10 12-coins is a known classic | Contamination resistance needs harder/fresher variants | `[done]` hard tier R11–R13 + derivation-over-answer rubric; `[next]` seeded variants |
| Visual quality is measurable | top-3 peer VIS: space-bunny 81.4 etc. | Gallery curation works | `[done]` gallery; `[next]` V5–V7 renders |

## 1. Shipped in v3.0 (this release)

- `[done]` **Hard tier R11–R13**: 100 prisoners & 100 boxes (cycle strategy + exact probability), Freudenthal sum-and-product (elimination table), five pirates (backward induction + tie-break sensitivity).
- `[done]` **T7 black-hole information paradox**: complementarity, firewalls, ER=EPR, island formula; candor-graded.
- `[done]` **V5 Eiffel Tower**: checkable platform geometry (±10 px at 57/115/276 m), lattice count, palette cap.
- `[done]` **V6 Taj Mahal**: 1 px bilateral symmetry contract, four minarets, proportional anchors.
- `[done]` **V7 Earth colour system**: fixed 8-token palette, stylized Earth, recomputed WCAG ratios, 60-30-10 bar.
- `[done]` **A4 sequence CRDT**: convergence proof, interleaving anomaly, safe tombstone GC, adversarial replica.
- `[done]` **F1 hard rebuild**: 10,000-row virtualised grid, Ctrl/Cmd+K command palette, undo/redo ≥ 20, dual-series canvas chart with crosshair, timezone selector, high-DPI, no-network.
- `[done]` **B1 hard rebuild**: idempotency replay/conflict, ETag + `If-Match` (428/412), cursor pagination, audit log, `X-Request-Id` everywhere, graceful shutdown, D6 exactly-once webhooks.
- `[done]` **Scorer v2 schema**: `nikbench.scorecard.v2`, RAT 0–13, new VIS/FE/BE criteria; v1 cards still scored under v2.0 weights (no silent re-weighting).
- `[done]` **Verifiers upgraded**: `verify_be.py` returns 0–100 with ~30 contract checks; `verify_fe.py` returns 0–100 with 24 checks; `verify_phase1.py` knows the 33-section contract.
- `[done]` **Judge packet v3.0**: hard-tier solving instructions, geometry/colour checklists, protocol-hardening BE rubric.

## 2. Next (v3.1 candidate queue)

- `[next]` **Seeded variants track.** Generate deterministic contamination-resistant variants (new Cheryl date table, 4-god Boolos, 13 coins + known genuine coin, parameterised pirate counts) from a published seed; keep classics as the comparability anchor. The generator lives in `scripts/`, variants quoted verbatim in `test.md`.
- `[next]` **Judge self-consistency.** Re-run each judge twice at temperature 0 on the same submission; drop cards whose R-solutions disagree.
- `[next]` **Ground-truth RAT consensus publishing.** Aggregate judges' independent R11–R13 solves; disagreements are findings — publish them in the board details.
- `[next]` **V3 animated verification.** `scripts/verify_v3.py` (Playwright): loop = 60.000 s ± 100 ms, seam continuity, reduced-motion poster.
- `[next]` **V5–V7 gallery + geometry check.** Extract new SVGs to `gallery/`, add `scripts/verify_vis.py` that parses platform y-coordinates, symmetry pairs, and recomputes WCAG ratios for V7.
- `[next]` **F1 live check.** Headless smoke for the grid: 10k rows present in the data model but not the DOM; palette opens on Ctrl+K; undo restores a dismissal.
- `[next]` **Blind peer review (pseudonyms).** Shuffle names A..H in Phase 2; de-anonymise after the round.
- `[next]` **Calibration audit column.** Track self-vs-peer gap per model across rounds; flag systematic inflation.
- `[next]` **Version pinning.** Record model version/hash + sampling params in the `nikbench.meta` header (already has `bench=v3.0`).

## 3. Ideas not yet scheduled

- `[idea]` **Tool-use / agentic pillar (AGY).** "Here is a repo with one failing test; find the bug, fix it, run the tests, report the diff." Requires tools; others skip with disclosure. The single biggest capability gap.
- `[idea]` **Vision input.** V8: reproduce a small base64 reference image; only multimodal models participate.
- `[idea]` **Long-context retrieval.** 30k-token document with one needle question.
- `[idea]` **Design critique.** Deliberately broken UI → 5 specific issues with severity.
- `[idea]` **Safety/adversarial injection.** Jailbreak-shaped instruction inside a legitimate spec; report refusal rate separately.
- `[idea]` **Multi-file / repo tasks.** "Add feature X; here are the tests."
- `[idea]` **Statistical power.** `--repeats N` for RAT/ALG; mean ± std.
- `[idea]` **Dispute process.** `disputes/` markdown with evidence; re-run by a different judge.
- `[idea]` **Multi-agent coordination.** Designer/implementer/reviewer split — park for v4.

## 4. What we will NOT fix (and why)

- **Honor-system isolation.** We cannot prevent a model from using tools/internet during Phase 1. Any enforcement would require a sandboxed harness and break the "paste into any chat" portability. Accept and disclose.
- **n=1 variance.** Single runs are noisy. Mitigation: repeats (not scheduled) and multiple judges; grades are bands, not points.
- **Memorization of classics.** Mitigation: hard tier + variants, not banning classics.
- **Provider/session failures.** Real reliability data — a model that cannot finish a large generation loses, and v3.0 is large on purpose. Disclose attempts; do not retry until it passes.

## 5. Milestones

- **v3.0 (shipped):** hard mode — 33 tasks, V5–V7, A4, F1/B1 hardening, dual-rubric scorer, upgraded verifiers.
- **v3.1 (next round):** seeded variants, judge self-consistency, V3/V5–V7 verification, F1 live check, blind peer pseudonyms, calibration column.
- **v4.0 (later):** agentic pillar, vision input, long-context retrieval, multi-file tasks, dispute process, multi-agent coordination.

## 6. Open questions for the user

1. Budget for paid judges? (Paid models unlock stronger rubric panels and dispute re-runs.)
2. Rerun v3.0 on the current 8-model roster, or add the two new opencode models (`nemotron-3.5-lightning-free`, `nemotron-3-ultra-free`) as candidates?
3. Should the hard tier be mandatory (current: yes, all 33 tasks) or scored as a separate "Hard" column alongside core?
4. Priority among §3 ideas — which pillar do you want expanded first?
