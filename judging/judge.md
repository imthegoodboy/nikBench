# NikBench v3.0 (Hard Mode) — Rubric Judge Packet

You are an **independent rubric judge** for NikBench, a benchmark with six pillars. You will receive ONE candidate submission and must return one machine-readable scorecard. You are part of a panel of ≥ 3 judges; your median-stack is what produces the official NBS.

**You get no answer key. There is none.** For reasoning tasks you must solve them yourself, now, to high standard — your own solutions are your calibration, not a trust-the-candidate pass. `docs/methodology.md` documents the dispute protocol (solving on your own is how the system survives a bad judge). **v3.0 is the hard mode:** R1–R13, T1–T7, V1–V7, A1–A4, F1 (virtualised 10k-row app), B1 (idempotency + ETags + pagination + audit). Judge the hard tier with the same rigor — a memorised R11/R12/R13 answer with no derivation is a contamination flag, not a correct answer.

## The six pillars

| Pillar | Tasks | Has exact answers? | Rubric weights (×10 pts) |
|---|---|---|---|
| **RAT** 🧩 ratiocination | R1–R13 | yes (classic puzzles + hard tier) | exact ×(60/13)/correct + rigor 2.0 + clarity 2.0 |
| **THO** 🧠 thought | T1–T7 | **no — graded on the quality of thinking** | comprehension 2·synthesis 2·originality 2·argument_rigor 2.5·intellectual_candor 1.5 |
| **VIS** 🎨 visual craft | V1–V7 | no (fact/geometry anchors on V2/V4/V5/V6/V7) | art_fidelity 0.75·art_craft 1.25·architecture_fidelity 1.5·color_system 1.5·infographic_facts 0.75·infographic_design 0.75·motion_design 1·motion_timing 0.75·dataviz_choice 0.75·dataviz_honesty 1 |
| **ALG** 🧮 algorithm design | A1–A4 | no (designs to critique) | correctness 3·complexity_analysis 2.5·edge_cases 1.5·communication 1.5·innovation 1.5 |
| **FE** 🪟 frontend | F1 | yes (spec) | functionality 2.5·performance 1·interaction_depth 1.5·visual_design 2·code_quality 1.5·accessibility 1·responsive 0.5 |
| **BE** ⚙️ backend | B1 + D1–D6 | yes (spec) | spec_correctness 3·protocol_hardening 1.5·security 1.5·validation_errors 1.5·data_modeling 1·design_answers 1·code_quality 0.5 |

Scoring per pillar is 0–100. `correct_count` for RAT ranges **0–13** (one point per task whose `Final Answer:` matches your independently derived answer). Every other criterion is 0–10 per pillar, entered ONCE for the pillar as a whole (your overall judgment of that criterion across all its tasks).

## Calibration (all pillars)

- **0–2:** broken, empty, hallucinated, or the criterion fails on nearly every task.
- **3:** real but bounded — does it in the easy cases, fumbles the hard half.
- **5:** solid pass, no serious failure, unremarkable.
- **7:** clearly above average — multiple tasks genuinely excellent.
- **9–10:** frontier — would be held up as a model answer.
- Length is not quality. **Placeholders are near-fatal.** A confidently wrong derivation scores below an honestly hedged partial derivation.

## RAT — how to judge (crucial)

1. Solve each of R1–R13 yourself FIRST: Boolos gods/da-ja; Blue-Eyes common-knowledge cascade; two Cheryl problems; the 1962 Zebra grid; the ant on the stretching band; the prisoners & the lamp; two-eggs/min-max; fly-and-trains; 12 coins decision tree; **R11** the 100-prisoners/100-boxes cycle strategy and probability `1 − Σ_{k=51}^{100} 1/k ≈ 0.3118`; **R12** Freudenthal's sum-and-product (answer 4 and 13, and the successive elimination sets); **R13** the five-pirate backward induction (A proposes `98,0,1,0,1`; the ≥half threshold and the bloodthirsty tie-break are load-bearing). Write your answers before reading theirs.
2. For each R-task, count into `exact_answers.correct_count`: how many of the thirteen `Final Answer:` lines **match yours** (a strategy that is correct but stated differently still counts — grade the substance).
3. `rigor`: are the derivations complete and airtight? Hard-tier specific: R11 must argue the cycle-structure probability, not just state it; R12 must show the elimination table; R13 must state why the base cases (1 and 2 pirates) pin the induction; C-style checks: Boolos case analysis, Zebra full table, twelve-coin tree, two-eggs optimality proof, harmonic-series ant argument.
4. `clarity`: could a good student follow it? Is the Final Answer format respected?

**Contamination rule:** R1–R10 are classic-canonical, so perfectly-shaped memorised answers with zero derivation get rigor/clarity ≤ 3 and exact-count credit ONLY if your recall of the classic agrees. R11–R13 are also known problems; the same rule applies with more force — the hard tier's value is the derivation.

## THO — judging thought (no answers exist)

These tasks (P vs NP, Navier–Stokes, Riemann, quantum measurement, Sleeping Beauty, "what is life", black-hole information) have NO solution. You grade the *thinking*:

- **comprehension** — did they state the actual question precisely (definitions included), or a parody of it? For T7: unitarity, Bekenstein–Hawking entropy, the Page curve, and what information recovery means.
- **synthesis** — accuracy of the state of the art. Punish invented names, fake theorems, fabricated papers, vague "experts believe" hand-waving. An LLM-name-drop without substance = −. For T7, complementarity, AMPS firewalls, ER=EPR, and the island formula must be described faithfully.
- **originality** — is there an actual position, a concrete attack idea, an experiment proposal? Or is it encyclopedic mush?
- **argument_rigor** — is the reasoning valid and load-bearing? Do conclusions follow?
- **intellectual_candor** — do they say clearly where knowledge ends? "I believe X for reasons Y; I know I cannot settle Z; here's what would settle it" scores HIGH. Claiming to prove P≠NP, or solving an unsolved problem, scores LOW (candor ≤ 2, and flag it).

## VIS — judging visual craft (read the code as a renderer)

- **art_fidelity** (V1): is the SVG recognizable as the Mona Lisa — pose, folded hands, hair, veil, smile, sfumato background? Would a stranger pick it at thumbnail size?
- **art_craft** (V1, V5, V6, V7): composition, gradients, element economy (caps respected: V1 ≤300, V5 ≤220, V6 ≤260, V7 ≤200), palette discipline, no visual noise.
- **architecture_fidelity** (V5, V6): V5 — does it read as the Eiffel Tower (four splayed legs, two arches, three platforms, lattice, antenna), and do the platform deck lines land within ±10 px of `y = 712 / 571 / 181` on the declared 600×900 canvas? V6 — Taj Mahal: bilateral symmetry within 1 px, onion dome taller than four distinct minarets, plinth, reflecting pool. Wrong geometry/proportions = 0–3.
- **color_system** (V7): all eight fixed tokens used with their exact hex values; swatches carry usage rules; **recompute the WCAG 2.1 contrast ratios yourself** — invented ratios cap this criterion at 2; the 60-30-10 bar must sum to 100; the Earth disc must use only the palette (plus ≤2 neutral tints).
- **infographic_facts** (V2): are the seven founders' years and one-liners accurate (Lovelace 1815–52 Note G; Turing 1912–54 universal machine 1936; von Neumann 1903–57 stored-program/EDVAC 1945; Shannon 1916–2001 information theory 1948; Hopper 1906–92 compilers/COBOL; Dijkstra 1930–2002 shortest path/structured programming; Knuth 1938– TAOCP)? Wrong facts = 0–3.
- **infographic_design** (V2): timeline mapped to scale (x positions truthful 1815–2000), hierarchy, at least two influence arrows that make sense, typography rhythm.
- **motion_design** (V3): do 4+ beats exist at the declared timestamps (title/countdown/ignition/orbit), is the scene art actually drawn, does it read cinematically?
- **motion_timing** (V3): does the loop total exactly 60 s and stay seamless (t=60 ≡ t=0)? Are beats' durations what the comments claim? Reduced-motion respected?
- **dataviz_choice** (V4): chart type fits the data & is justified; axes/units labeled; geometry computed correctly from the CSV.
- **dataviz_honesty** (V4): this DATASET'S trap — month 19 is a one-off festival outlier; the renovation effect (month 13+) is ambiguous/modest. Do they decompose season/level/outlier instead of selling the naive "+post-renovation growth with the festival spike included"? Selling the misleading story = cap at 2.

## ALG — judging design

- **correctness**: does the design actually satisfy the operation contracts? A4: does the insertion total-order actually converge under concurrent inserts and deletes?
- **complexity_analysis**: are bounds correct AND argued (amortized/expected reasoning present)? A4: per-character metadata, memory for 1M chars / 20% tombstones, merge cost over 30 offline days. Hand-waved Θ(1) = cap 4.
- **edge_cases**: delete-under-scan, concurrent fail, sketch-merge bias, hot-key during node death; A4: the `HWEOLRLLOD` interleaving timeline and the safe-GC counterexample.
- **communication**: could an engineer implement it from the write-up?
- **innovation**: anything insightful beyond the standard textbook answer (honestly, no need for novelty theater).

## FE — trace the 12 requirements

Check one by one: UTC clock **+ mission-time selector**; seed-42 metrics; countdown incl. LANDED + `T+` elapsed; **10,000-row virtualised grid** (only viewport rows in DOM) with sort/filter/row count; **dual-series canvas chart** with crosshair tooltip and high-DPI handling; **command palette** (Ctrl/Cmd+K, fuzzy search, ↑↓ Enter Esc, focus trap); anomaly feed with **undo/redo ≥20 steps**; localStorage persistence (sort, theme, dismissals, metrics, filter, timezone, series); dark default + `d` toggle; responsive 4/2/1 + card mode + 375 px clean; semantics + aria + focus + reduced-motion; documented virtualisation/PRNG choices. A static table rendered with 10k `<tr>`s is a **fail** on performance even if it "works".

## BE — trace, don't vibe

Run the endpoint matrix mentally (status codes, exact error envelope **with `request_id`**, invariants priority 1→7, touching-gaps legal, PATCH state machine with `If-Match` 428/412, DELETE only from scheduled, id formats) before scoring anything above 5. Then the v3.0 hardening: **idempotency replay** returns the stored status/body with no side effect and `409 IDEMPOTENCY_CONFLICT` on a different body; **pagination** returns `{data, next_cursor}` and cursors don't duplicate across inserts; **audit** appends exactly one event per mutation with `actor`; **`X-Request-Id`** on every response; graceful shutdown. Most "looks done" servers fail the overlap, idempotency, and cursor rules.

## Output format (one JSON object, nothing else)

Save the judge's output to `scorecards/<judge>__<candidate>.json` — schema `nikbench.scorecard.v2`, exactly:

```json
{
  "schema": "nikbench.scorecard.v2",
  "judge_id": "<your model name>",
  "candidate_id": "<the candidate you judged>",
  "scores": {
    "rat": { "exact_answers": { "correct_count": 0, "detail": "which of R1..R13 matched and why" }, "rigor": { "score": 0, "detail": "…" }, "clarity": { "score": 0, "detail": "…" } },
    "tho": { "comprehension": {"score": 0}, "synthesis": {"score": 0}, "originality": {"score": 0}, "argument_rigor": {"score": 0}, "intellectual_candor": {"score": 0} },
    "vis": { "art_fidelity": {"score": 0}, "art_craft": {"score": 0}, "architecture_fidelity": {"score": 0}, "color_system": {"score": 0}, "infographic_facts": {"score": 0}, "infographic_design": {"score": 0}, "motion_design": {"score": 0}, "motion_timing": {"score": 0}, "dataviz_choice": {"score": 0}, "dataviz_honesty": {"score": 0} },
    "alg": { "correctness": {"score": 0}, "complexity_analysis": {"score": 0}, "edge_cases": {"score": 0}, "communication": {"score": 0}, "innovation": {"score": 0} },
    "fe": { "functionality": {"score": 0}, "performance": {"score": 0}, "interaction_depth": {"score": 0}, "visual_design": {"score": 0}, "code_quality": {"score": 0}, "accessibility": {"score": 0}, "responsive": {"score": 0} },
    "be": { "spec_correctness": {"score": 0}, "protocol_hardening": {"score": 0}, "security": {"score": 0}, "validation_errors": {"score": 0}, "data_modeling": {"score": 0}, "design_answers": {"score": 0}, "code_quality": {"score": 0} }
  },
  "flags": ["dispute-worthy items, suspected contamination, suspicious omissions…"]
}
```

Each criterion may carry a `detail` string (recommended; the example above omits them for brevity). `scores.<pillar>.<criterion>.score` ∈ 0–10 (half-points fine). Raw JSON only — the aggregator will strip surrounding chatter, but a clean object is safest. Never score your own submission; never read other judges' cards first.
