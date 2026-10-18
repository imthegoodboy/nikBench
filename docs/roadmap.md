# NikBench improvement roadmap (v2.1 → v3.0)

> Companion to `docs/methodology.md`. This file is the **living backlog** of what we learned from
> running v2.0 round 1 and what we want to fix next. Items are prioritized; status tags:
> `[done]` shipped, `[next]` queued for the next round, `[idea]` needs design.

## 0. What round 1 actually taught us (data, not vibes)

| Signal | Evidence | Implication |
|---|---|---|
| Judge ≠ peers disagree sharply | beam: judge 100 vs peer 71.3; deepseek: judge RAT 36 vs peer ~84 | Single-judge NBS is fragile; we need ≥3 judges + median + spread |
| Self-inflation is real but bounded | beam self 85 vs peer 71.3 (+13.7); mimo self 45 vs peer 33.6 (+11.4) | Keep self-row-last; track self-vs-peer gap as a calibration metric |
| Honest self-docking is possible | space-bunny docked its own RAT to 5 after re-deriving the Boolos `da`/`ja` lemma mid-review | Candor can be measured, not just asserted — keep the anti-vibes protocol |
| Partial builds are a real outcome | mimo died in 6 sessions; produced R+T only; NBS 36, grade F | Session stability is part of "capability" in a one-shot protocol; disclose, don't hide |
| Static review misses real bugs | longcat's B1 has no DELETE handler (caught only by `verify_be.py`); nemotron's FE has no `<main>` landmark | "Mentally execute" is insufficient — execution verification must be in the pipeline |
| Peers catch what judges miss | space-bunny caught glm's fabricated "Rabern–Rabern"/"Sapienti"; nemotron's V3 crashes at t=25s | Peer round is not redundant with judges — keep both |
| Classic puzzles are memorizable | R10 12-coins is a known classic; models may recite, not derive | Contamination resistance needs fresh variants |
| Visual quality is measurable | top-3 peer VIS: space-bunny 81.4, big-pickle 80.7, glm 78.6 | Gallery curation works; add per-task peer VIS spread |

## 1. Trust & genuineness (highest leverage)

- **[next] Multi-judge median.** `aggregate.py` already supports N judges (per-judge medians, spread, outlier flagging >15). Round 1 ran only cohere. Run ≥3 judges from *different* families (cohere + a paid strong model if budget allows + one opencode free model that is NOT a candidate). Report `Judges: N` and spread. Single judge = single point of failure.
- **[next] Judge self-consistency.** Run each judge twice on the same submission at temperature 0; if R-solutions differ, distrust that card (flag + drop from median). Guards against a judge that "solves" by pattern-matching rather than reasoning.
- **[next] Ground-truth RAT consensus.** Aggregate judges' independent R-solutions; where they disagree, surface it (don't silently pick). A disagreement on R1 (Boolos) is a *finding*, not a bug — publish it.
- **[next] Execution verification in Phase 3.** `scripts/verify_be.py` and `scripts/verify_fe.py` already exist and ran green on 6/7 models. Make them mandatory Phase-3 steps that feed the BE/FE NBS (e.g., BE = 0.5·spec-trace + 0.5·live-contract). A server that doesn't boot cannot score 80 on BE.
- **[idea] Reproducibility metadata.** Each submission should open with a small header: model version, sampling params (temperature/top_p if known), date, harness. Currently absent. Without it, "same model, different day" results are incomparable.
- **[idea] Statistical power.** n=1 per task. Run each task 3× at fixed temperature and report mean±std for at least RAT and ALG. Triples judge cost — gate behind a `--repeats N` flag.
- **[idea] Contamination-resistant variants.** Keep canonical classics for comparability, add a "v2.1 variants" track: Cheryl with a different candidate-date table, Boolos with 4 gods, 13 coins/3 weighings with two counterfeits. Memorization dies; reasoning survives. Generate variants deterministically from a seed so rounds stay reproducible.
- **[idea] Blind peer review.** Shuffle model names to pseudonyms (A..H) during Phase 2 and de-anonymize after. Prevents "model X is usually good" bias. Costs ~10 lines in the Phase 2 instructions.

## 2. Capability coverage (what's missing)

- **[next] Tool-use / agentic pillar (new pillar "AGY").** NikBench currently tests single-shot generation only, but the product is an *agent*. Add tasks: "here is a repo with one failing test; find the bug, fix it, run the tests, report the diff." Requires tool access — only models with tools participate; others skip with disclosure. This is the single biggest coverage gap.
- **[idea] Vision input.** A task where the model receives a small base64 PNG (a chart, a UI screenshot, a diagram) and must reproduce or critique it. Tests multimodal capability; V1 Mona Lisa is description-only today.
- **[idea] Long-context retrieval.** A 30k-token document with a single needle question buried in it. Tests retrieval, not generation.
- **[idea] Design critique (not just generation).** Give a deliberately broken UI; ask for 5 specific issues with fixes and severity. Tests taste and diagnosis, which generation tasks don't.
- **[idea] Safety/adversarial.** Embed a jailbreak-shaped instruction inside an otherwise legitimate spec; grade whether the model refuses the injection while still solving the legitimate part. Report refusal rate separately (not mixed into capability score).
- **[idea] Multi-file / repo tasks.** "Add feature X to this codebase; here are the tests." Tests integration, not isolated snippets.

## 3. Difficulty & multi-work

- **[next] Phase 4 — revision round.** After Phase 2, each model receives its own peer notes and must produce a *patched* submission (changed sections only, with a changelog). Re-grade the delta. Tests responsiveness to critique, diff discipline, and honesty ("did they actually fix the flagged bug?"). space-bunny explicitly said it would fix R3/R4 — let's measure it.
- **[next] Hard-mode tier.** Add R11–R15 (novel variants), A4 (a genuinely novel data-structure problem with no textbook answer), T7 (a recent, obscure open conjecture). Keep classics for comparability; hard tier is opt-in and reported separately.
- **[idea] Hidden edge cases in F1/B1.** The spec states the contract; add *unstated* boundary tests (B1: `start` exactly equal to server start time; a request with `duration_min` not in the allowed set; PATCH on a cancelled appointment). The smoke harness already found longcat's missing DELETE — extend it to cover every edge in the spec's priority order (a→f).
- **[idea] Iterative tool-use tasks.** "Fix this until the tests pass" with up to 5 turns. Measures debugging, not just first-shot generation.
- **[idea] Multi-agent coordination.** One model designs, another implements, a third reviews. Too complex for v2.x — park for v3.0.

## 4. Visual tasks (user-asked expansion)

Round 1 has 4 visual tasks (V1 Mona Lisa, V2 founders, V3 60s loop, V4 honest chart). Proposals:

- **[next] V5 — reproduce from a reference.** Provide a small base64 PNG (a UI card, a chart, an icon). Model must reproduce it in SVG/HTML. Tests vision + code. (Requires vision-capable models; others skip.)
- **[next] V6 — micro-interaction.** A button hover/press state + a loading spinner, both in one file, with reduced-motion fallback. Tests animation craft at small scale (V3 is large-scale only).
- **[idea] V7 — icon set.** 6 icons in one consistent style (stroke weight, grid, corner radius). Tests design-system discipline.
- **[idea] V8 — data-viz choice.** Give the same dataset three ways (table, bar, line) and ask which + why. Tests judgment, not just execution.
- **[next] Animated verification.** Actually run V3 in a headless browser and assert: total loop 60.000s ±100ms, seam continuous (first frame == last frame), reduced-motion renders a static poster. `scripts/verify_v3.py` via Playwright. Today V3 is only mentally checked.
- **[next] Visual diff in the gallery.** Overlay the V1 renders at 50% opacity to show divergence; add a per-task peer-VIS spread column (max−min across reviewers).

## 5. Governance & measurement hygiene

- **[next] Calibration audit.** Track self-vs-peer gap per model across rounds; flag systematic inflation (beam +13.7 this round). Publish a "calibration" column on the board.
- **[next] Version pinning.** Record model version/hash + sampling params in each submission header (see §1). Without this, "beam-free improved from 91 to 95" is meaningless.
- **[next] Judge diversity.** Use ≥3 judges from different families; report spread. Already supported by `aggregate.py`; just needs orchestration.
- **[idea] Open the judge prompts to review.** `judging/judge.md` is in the repo; publish the exact judge model + version + temperature used per round. Reproducibility.
- **[idea] Dispute process.** A model that disagrees with its score can file a dispute (a markdown file in `disputes/`) citing specific evidence; a human or a different judge re-runs. Currently scores are final.

## 6. What we will NOT fix (and why)

- **Honor-system isolation.** We cannot prevent a model from using tools/internet during Phase 1. We state the rule and trust. Any "enforcement" would require a sandboxed harness, which changes the benchmark's "paste into any chat" portability. Accept and disclose.
- **n=1 variance.** Single runs are noisy. Mitigation: repeats (§1) and multiple judges, not claiming precision we don't have. Grades are bands, not points.
- **Memorization of classics.** Mitigation: variants (§1), not banning classics (they're the comparability anchor).
- **Provider/session failures (mimo).** These are *real* reliability data — a model that can't finish a 40k-token generation in one session loses. Disclose attempts; don't retry until it passes (that would hide the failure).

## 7. Proposed milestones

- **v2.1 (next round, ~1 week):** multi-judge (≥3), execution verification mandatory (BE/FE), Phase 4 revision round, V5 reproduce-from-reference, judge self-consistency check, reproducibility header.
- **v2.2:** contamination-resistant variants, blind peer review (pseudonyms), calibration audit column, V6 micro-interaction, animated V3 verification.
- **v3.0:** tool-use/agentic pillar, vision input, long-context retrieval, multi-file tasks, multi-agent coordination, dispute process.

## 8. Open questions for the user

1. Budget for paid judges? ($10 OpenRouter credits unlocks 1000 free-model requests/day and removes the cap that blocked 4 cards this round.)
2. Should partial builds (mimo) be graded on what exists, or marked "incomplete" with no Final? Current: graded on what exists (F, honest).
3. Is session-stability (mimo's 6 failed attempts) a capability we want to measure, or should we allow retries with a penalty? Current: no retries, disclosed.
4. Priority order among §2/§3/§4 additions — which pillar do you want expanded first?
