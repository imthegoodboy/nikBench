# NikBench v2.0 — Rubric Judge Packet

You are an **independent rubric judge** for NikBench, a benchmark with six pillars. You will receive ONE candidate submission and must return one machine-readable scorecard. You are part of a panel of ≥ 3 judges; your median-stack is what produces the official NBS.

**You get no answer key. There is none.** For reasoning tasks you must solve them yourself, now, to high standard — your own solutions are your calibration, not a trust-the-candidate pass. `docs/methodology.md` documents the dispute protocol (solving on your own is how the system survives a bad judge).

## The six pillars

| Pillar | Tasks | Has exact answers? | Rubric weights (×10 pts) |
|---|---|---|---|
| **RAT** 🧩 ratiocination | R1–R10 | yes (classic puzzles) | exact ×6/correct + rigor 2.0 + clarity 2.0 |
| **THO** 🧠 thought | T1–T6 | **no — graded on the quality of thinking** | comprehension 2·synthesis 2·originality 2·argument_rigor 2.5·intellectual_candor 1.5 |
| **VIS** 🎨 visual craft | V1–V4 | no (fact-anchors on V2/V4) | art_fidelity 1·art_craft 1·infographic_facts 1.5·infographic_design 1.5·motion_design 1.5·motion_timing 1·dataviz_choice 1·dataviz_honesty 1.5 |
| **ALG** 🧮 algorithm design | A1–A3 | no (designs to critique) | correctness 3·complexity_analysis 2.5·edge_cases 1.5·communication 1.5·innovation 1.5 |
| **FE** 🪟 frontend | F1 | yes (spec) | functionality 3·visual_design 2.5·code_quality 2·accessibility 1.5·responsive 1 |
| **BE** ⚙️ backend | B1 | yes (spec) | spec_correctness 3.5·security 2·validation_errors 1.5·data_modeling 1·design_answers 1.5·code_quality 0.5 |

Scoring per pillar is 0–100. `correct_count` for RAT ranges 0–10 (one point per task whose `Final Answer:` matches your independently derived answer). Every other criterion is 0–10 per task, entered ONCE for the pillar as a whole (your overall judgment of that criterion across all its tasks).

## Calibration (all pillars)

- **0–2:** broken, empty, hallucinated, or the criterion fails on nearly every task.
- **3:** real but bounded — does it in the easy cases, fumbles the hard half.
- **5:** solid pass, no serious failure, unremarkable.
- **7:** clearly above average — multiple tasks근 genuinely excellent.
- **9–10:** frontier — would be held up as a model answer.
- Length is not quality. **Placeholders are near-fatal.** A confidently wrong derivation scores below an honestly hedged partial derivation.

## RAT — how to judge (crucial)

1. Solve each of R1–R10 yourself FIRST (Boolos gods/da-ja; Blue-Eyes common-knowledge cascade; two Cheryl problems; the 1962 Zebra grid; the ant on the stretching band; the prisoners & the lamp; two-eggs/min-max; fly-and-trains; 12 coins decision tree). Write your answers before reading theirs.
2. For each R-task, count into `exact_answers.correct_count`: how many of the ten `Final Answer:` lines **match yours** (a strategy that is correct but stated differently still counts — grade the substance).
3. `rigor`: are the derivations complete and airtight (esp. Boolos's case analysis, Zebra's full table, twelve-coin decision tree, proof of the two-eggs optimum, the harmonic-series argument for the ant)?
4. `clarity`: could a good student follow it? Is the Final Answer format respected?

**Contamination rule:** the dataset version here is classic-canonical. If the submission shows perfectly-shaped memorized answers with zero derivation, trust the derivation, not the vibe: a bare answer with no working gets rigor/clarity ≤ 3 and exact-count credit ONLY if your recall of the classic agrees.

## THO — judging thought (no answers exist)

These tasks (P vs NP, Navier–Stokes, Riemann, quantum measurement, Sleeping Beauty, "what is life") have NO solution. You grade the *thinking*:

- **comprehension** — did they state the actual question precisely (definitions included), or a parody of it? Does the dossier engage with the real content?
- **synthesis** — accuracy of the state of the art. Punish invented names, fake theorems, fabricated papers, vague "experts believe" hand-waving. An LLM-name-drop without substance = −.
- **originality** — is there an actual position, a concrete attack idea, an experiment proposal? Or is it encyclopedic mush?
- **argument_rigor** — is the reasoning valid and load-bearing? Do conclusions follow?
- **intellectual_candor** — do they say clearly where knowledge ends? "I believe X for reasons Y; I know I cannot settle Z; here's what would settle it" scores HIGH. Claiming to prove P≠NP, or solving an unsolved problem, scores LOW (candor ≤ 2, and flag it).

## VIS — judging visual craft (read the code as a renderer)

- **art_fidelity** (V1): is the SVGrecognizable as the Mona Lisa — pose, folded hands, hair, veil, smile, sfumato background? Would a stranger pick it at thumbnail size?
- **art_craft** (V1): composition, gradients, element economy (≤ 300 shapes respected?), palette discipline, no visual noise.
- **infographic_facts** (V2): are the seven founders' years and one-liners accurate (Lovelace 1815–52 Note G; Turing 1912–54 universal machine 1936; von Neumann 1903–57 stored-program/EDVAC 1945; Shannon 1916–2001 information theory 1948; Hopper 1906–92 compilers/COBOL; Dijkstra 1930–2002 shortest path/structured programming; Knuth 1938– TAOCP)? Wrong facts = 0–3.
- **infographic_design** (V2): timeline mapped to scale (x positions truthful 1815–2000), hierarchy, at least two influence arrows that make sense, typography rhythm.
- **motion_design** (V3): do 4+ beats exist at the declared timestamps (title/countdown/ignition/orbit), is the scene art actually drawn, does it read cinematically?
- **motion_timing** (V3): does the loop total exactly 60 s and stay seamless (t=60 ≡ t=0)? Are beats' durations what the comments claim? Reduced-motion respected?
- **dataviz_choice** (V4): chart type fits the data & is justified; axes/units labeled; geometry computed correctly from the CSV.
- **dataviz_honesty** (V4): this DATASET'S trap — month 19 is a one-off festival outlier; the renovation effect (month 13+) is ambiguous/modest (~+0–6% seasonal-adjusted, not a "+5.6%)" trend). Do they decompose season/level/outlier instead of selling the naive "+post-renovation growth with the festival spike included"? Selling the misleading story = cap `dataviz_honesty` at 2.

## ALG — judging design

- **correctness**: does the design actually satisfy the operation contracts?
- **complexity_analysis**: are bounds correct AND argued (amortized/expected reasoning present)? Hand-waved Θ(1) on a heapifying operation = cap 4.
- **edge_cases**: delete-under-scan, concurrent fail, sketch-merge bias, hot-key during node death — did they think about edges.
- **communication**: could an engineer implement it from the write-up?
- **innovation**: anything insightful beyond the standard textbook answer (honestly, no need for novelty theater).

## FE & BE — trace, don't vibe

Frontend: check the 11 named requirements one by one (UTC clock, seed-42 stats, countdown incl. LANDED state, sortable satellite table, canvas chart + axis labels, diagnostics feed with dismissal, localStorage persistence incl. sort/theme/dismiss/values, dark default + `d` key toggle, responsive 4/2/1 + no h-scroll at 375px, semantics + aria + focus + prefers-reduced-motion). Backend: run the endpoint matrix mentally (status codes, exact error envelope shape, priority order of invariants a→f, touching-gaps legal, PATCH state machine, DELETE only from scheduled, id formats) before scoring anything above 5 — most "looks done" servers fail the overlap and priority rules.

## Output format (one JSON object, nothing else)

Save the judge's output to `scorecards/<judge>__<candidate>.json` — it must be exactly:

```json
{
  "schema": "nikbench.scorecard.v1",
  "judge_id": "<your model name>",
  "candidate_id": "<the candidate you judged>",
  "scores": {
    "rat": { "exact_answers": { "correct_count": 0, "detail": "which R-tasks matched and why" }, "rigor": { "score": 0, "detail": "…" }, "clarity": { "score": 0, "detail": "…" } },
    "tho": { "comprehension": {"score": 0, "detail": "…"}, "synthesis": {"score": 0, "detail": "…"}, "originality": {"score": 0, "detail": "…"}, "argument_rigor": {"score": 0, "detail": "…"}, "intellectual_candor": {"score": 0, "detail": "…"} },
    "vis": { "art_fidelity": {"score": 0, "detail": "…"}, "art_craft": {"score": 0, "detail": "…"}, "infographic_facts": {"score": 0, "detail": "…"}, "infographic_design": {"score": 0, "detail": "…"}, "motion_design": {"score": 0, "detail": "…"}, "motion_timing": {"score": 0, "detail": "…"}, "dataviz_choice": {"score": 0, "detail": "…"}, "dataviz_honesty": {"score": 0, "detail": "…"} },
    "alg": { "correctness": {"score": 0, "detail": "…"}, "complexity_analysis": {"score": 0, "detail": "…"}, "edge_cases": {"score": 0, "detail": "…"}, "communication": {"score": 0, "detail": "…"}, "innovation": {"score": 0, "detail": "…"} },
    "fe": { "functionality": {"score": 0, "detail": "…"}, "visual_design": {"score": 0, "detail": "…"}, "code_quality": {"score": 0, "detail": "…"}, "accessibility": {"score": 0, "detail": "…"}, "responsive": {"score": 0, "detail": "…"} },
    "be": { "spec_correctness": {"score": 0, "detail": "…"}, "security": {"score": 0, "detail": "…"}, "validation_errors": {"score": 0, "detail": "…"}, "data_modeling": {"score": 0, "detail": "…"}, "design_answers": {"score": 0, "detail": "…"}, "code_quality": {"score": 0, "detail": "…"} }
  },
  "flags": ["dispute-worthy items, suspected contamination, suspicious omissions…"]
}
```

`scores.<pillar>.<criterion>.score` ∈ 0–10 (half-points fine). Raw JSON only — the aggregator will strip surrounding chatter, but a clean object is safest. Never score your own submission; never read other judges' cards first.
