# NikBench Methodology (v1.0)

NikBench is a **peer-judged benchmark**: one candidate model performs a fixed task packet, the raw reply is stored as a submission file, and ≥ 3 *independent judge models* — from different model families, in fresh chats — score it against a fixed rubric. A small script aggregates the judges' scorecards into one 0–100 **NikBench Score (NBS)**.

---

## 1. Run procedure (end to end)

### Step 1 — Candidate run
1. Open a **fresh chat** with the candidate model, default settings (no system-prompt tuning, no tools enabled, temperature provider-default).
2. Paste the complete contents of [`test.md`](../test.md).
3. Save the model's **entire, unedited reply** to `submissions/<model-name>.md`.
   > e.g. `submissions/gpt-5.2.md`, `submissions/claude-opus-4-6.md`, `submissions/gemini-3-pro.md`
   > Keep the file name = the model name you will publish on the leaderboard.

### Step 2 — Judging (per judge model)
For each judge (pick ≥ 3 judges; different families than the candidate; ideally ≥ 2 of 3 at frontier quality):
1. Open a **fresh chat**.
2. Paste the complete contents of [`judging/judge.md`](../judging/judge.md).
3. Paste the full contents of `submissions/<model-name>.md`.
4. The judge replies with a single JSON scorecard. Save it to `scorecards/<judge-id>__<model-name>.json`.

### Step 3 — Aggregation
```bash
python scripts/aggregate.py scorecards -o leaderboard.md
```
The script computes pillar scores, medians across judges, the overall NBS, grades, agreement spread, and flags. Committing updated scorecards + `leaderboard.md` via pull request completes a run.

### Judge independence rules
- Judges must **not** be the candidate model and must not share the candidate's own family in the same run if avoidable.
- Judges must judge without communication; each runs in a fresh chat.
- Judges solve the reasoning tasks themselves *before* reading the candidate's answers (there is no answer key in this repo by design).

---

## 2. Scoring model

Every criterion is 0–10; weights convert criteria to 0–100 pillar scores (weights live in `scripts/aggregate.py` and mirror `judging/judge.md`):

| Pillar | Criteria (×weight) | Max |
|---|---|---:|
| Reasoning (REA) | exact_answers (6/task) + rigor ×2 + clarity ×2 | 100 |
| Frontend (FE) | functionality ×3, visual ×2.5, code ×2, a11y ×1.5, responsive ×1 | 100 |
| Backend (BE) | spec ×3.5, security ×2, errors ×1.5, modeling ×1, design Q&A ×1.5, code ×0.5 | 100 |

- **Per-judge overall** = mean of that judge's three pillar scores.
- **Pillar score (official)** = *median* across judges.
- **NBS** = mean of the three pillar medians, 0–100.
- **Grades:** `S ≥ 90 · A ≥ 80 · B ≥ 70 · C ≥ 60 · D ≥ 45 · F < 45`.
- **Agreement:** spread = max − min of per-judge overalls. Spread ≤ 10 is healthy; > 15 adds a review flag.
- **Outliers:** a judge deviating > 15 NBS points from the median is flagged (kept, not discarded — transparency over silent filtering).

### Dispute protocol (reasoning answers)
There is **no answer key**; each judge solves R1–R10 independently. If judges disagree on a task: **majority wins**; if there is no majority (all three differ), the task counts **0.5** toward `correct_count`. This is executed when entering `correct_count` — the script accepts halves for exactly this case.

---

## 3. Task provenance & attribution

All Section A reasoning tasks are taken **verbatim from public benchmark datasets** (so the benchmark is a test against the internet's real eval distribution, not invented puzzles):

| Tasks | Dataset | Source | License |
|---|---|---|---|
| R1, R2 | **GSM8K** (test split) | [openai/grade-school-math](https://github.com/openai/grade-school-math) | MIT |
| R3, R4 | **AQuA-RAT** (test split) | [google-deepmind/AQuA](https://github.com/google-deepmind/AQuA) | Apache-2.0 |
| R5, R6 | **BBH — multistep_arithmetic_two** | [suzgunmirac/BIG-Bench-Hard](https://github.com/suzgunmirac/BIG-Bench-Hard) | MIT |
| R7 | **BBH — logical_deduction_five_objects** | same | MIT |
| R8 | **BBH — date_understanding** | same | MIT |
| R9 | **BBH — tracking_shuffled_objects_five_objects** | same | MIT |
| R10 | **BBH — web_of_lies** | same | MIT |
| F1 | original spec (authored for NikBench) | — | — |
| B1 | original spec (authored for NikBench) | — | — |

**No ground-truth answers are published in this repository.** Judges derive them independently and cross-check each other (§2 dispute protocol).

---

## 4. Contamination policy

Public tasks mean public contamination risk: a frontier model may have seen GSM8K/BBH items during training. We accept this trade-off (it is the same exposure every public benchmark has), with these mitigations:

1. **Rigor is judged, not just the letter.** Memorized answers without derivations score low on `rigor`/`clarity`.
2. **Judging is relative & peer-based** — all models face the same items, so contamination registers as uniform inflation rather than model-differential advantage.
3. **v1.1 will ship a rotated variant**: same spec structure, items parameterized/seeded at run time (F1/B1 constants get a per-run seed; reasoning items get regenerated from held-out splits).
4. Report the exact run date in your submission folder so scores can be contextualized.

---

## 5. What is *not* measured (v1.0 scope)

- Multimodal/image generation, agentic browsing, tool-loop tasks — planned for v1.2/v1.3 packs.
- Latency, cost-per-token, safety/red-team robustness — track these separately; NikBench scores *capability of a single generation*.
- Human visual review of F1 is optional (judges read code); a human may append a visual commentary to the submission folder but cannot override the JSON protocol.

## 6. Versioning

- `v1.0` (current): 10 sourced reasoning tasks + F1 frontend flagship + B1 backend flagship. Fixed packet; scorecards use schema `nikbench.scorecard.v1`.
- `v1.1` (planned): seeded rotation + held-out task pool.
- Score compatibility: scorecards from different minor versions are **not** mixed on one leaderboard.
