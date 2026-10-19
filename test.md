# NikBench v3.0 — Hard Mode (build → review → update the board)

> **How you got this:** a human pasted this file into a chat with you. This packet is **idempotent** — run it once now and, later, run it again (fresh chat) once other models finish: it will route you into the correct phase automatically.
>
> Your job today may be **Phase 1 only**, or Phases 2–3 — determined by ONE check in the Phase Router below.

You are participating in **NikBench v3.0 — Hard Mode**, a peer-judged benchmark with six pillars: **Ratiocination 🧩**, **Thought 🧠**, **Visual craft 🎨**, **Algorithm design 🧮**, **Frontend 🪟**, **Backend ⚙️**.

**v3.0 is deliberately harder than v2.0.** It adds three hard reasoning classics (R11–R13), a current open problem in theoretical physics (T7), three demanding new visual builds (V5 Eiffel Tower, V6 Taj Mahal, V7 Earth colour system), a sequence-CRDT design (A4), and materially harder frontend/backend contracts (virtualised 10k-row UI, command palette, undo/redo; idempotency keys, ETags, pagination, audit log). The output is large on purpose: finishing a complete, correct build is part of what is being measured.

---

## Your identity & file name

- Your **file name** is your model name, normalized: lowercase, hyphens, version kept (e.g. `gpt-5.2.md`, `claude-opus-5.5.md`, `glm-5.3-flash-free.md`).
- If it is genuinely ambiguous what exact file name the human expects, you may ask **exactly one** clarifying question about the name — then never ask again; everything else must be solved without questions.

---

## ⛰️ Phase Router (run this FIRST, before anything else)

Check whether **`submissions/<your-name>.md` already exists** (one directory listing is allowed for this).

- **Does not exist** → start at **PHASE 1** (blind build). Do it completely, then STOP exactly as instructed there.
- **Exists** → you already built in an earlier chat. Do **not** re-do Phase 1, do **not** read your own old submission. Go straight to the **PHASE GATE**.

---

# PHASE 1 — BLIND BUILD

Your full reply will later be reviewed by the other candidate models. Judges do **not** receive any answer key — they solve every task themselves. Unsupported correct answers lose points; wrong answers with honest reasoning score better than lucky guesses. Tasks marked **THO** and parts of **VIS/ALG** have **no correct answer at all** — they are graded on the *quality and honesty of your thinking*.

## Rules (strict)

1. **One single generation.** Everything below must be produced in this reply without external help. Do not ask further questions; if a spec is ambiguous, pick the most reasonable interpretation and note it in that task's notes.
2. **No tools, no internet, no code execution while solving.** Pure generation. (The single exception: the harness-allowed `write` at the very end.)
3. **No placeholders.** `TODO`, `...`, "omitted", truncated code: heavily penalized. Every code block must be complete and runnable as-is.
4. **Show derivations** for reasoning tasks, then a line reading exactly `Final Answer: <value>`. Multiple-choice tasks: the letter, e.g. `Final Answer: (B)`.
5. **Assume UTC everywhere.** State any constant seeds inline.
6. **Do not restate the tasks.** Solve them. No meta commentary, no flattery, no closing speech.
7. **Blind-phase isolation:** read no files other than this packet; never look into `submissions/`, `peer/`, `scorecards/`, `docs/`, or `judging/`.
8. **Anti-vibes protocol (all THO tasks):** do not invent citations, theorem names, people, or results. Claiming to *solve* an open problem is a candor failure. "Here is what is actually known, here is where I stop, and here is my reasoned position" scores **better** than confident mush.
9. **Completion contract:** a complete build is part of the capability being measured. If you genuinely run out of budget, stop cleanly and write `<!-- incomplete: <sections> -->` at the point where you stopped — never emit `TODO`/`...` placeholders or fake content. Omitted sections score 0; an honest partial build is graded as-is.

## Section R — Ratiocination (R1–R13)

Each problem below is quoted from (or anchored to) its classic public source; provenance is listed in `docs/methodology.md`. All have exact answers, but **no answer key exists in this repo** — judges solve them independently. Show real derivations; verify your own work before writing it. R11–R13 are the v3.0 hard tier: they are longer, and a memorised answer without a derivation earns little.

### R1 — The Hardest Logic Puzzle Ever (Boolos, 1996)

Three gods A, B, and C are called, in some order, True, False, and Random. True always speaks truly, False always speaks falsely, but whether Random speaks truly or falsely is a completely random matter. Your task is to determine the identities of A, B, and C by asking three yes-no questions; each question must be put to exactly one god. The gods understand English, but will answer all questions in their own language, in which the words for yes and no are da and ja, in some order. You do not know which word means which.

- It could be that some god gets asked more than one question (and hence that some god is not asked any question at all).
- What the second question is, and to which god it is put, may depend on the answer to the first question. (And of course similarly for the third question.)
- Whether Random speaks truly or not should be thought of as depending on the flip of a coin hidden in his brain: if the coin comes down heads, he speaks truly; if tails, falsely.
- Random will answer da or ja when asked any yes-no question.

**Deliverable:** your complete three-question strategy (questions may be adaptive and self-referential, e.g. of the form "Does *da* mean yes iff *X*?"), and a case analysis proving it can never fail.

### R2 — Blue Eyes (xkcd's classic statement)

A group of people with assorted eye colors live on an island. They are all perfect logicians — if a conclusion can be logically deduced, they will do it instantly. No one knows the color of their eyes. Every night at midnight, a ferry stops at the island. Any islanders who have figured out the color of their own eyes then leave the island, and the rest stay. Everyone can see everyone else at all times and keeps a count of the number of people they see with each eye color (excluding themselves), but they cannot otherwise communicate. Everyone on the island knows all the rules in this paragraph. On this island there are 100 blue-eyed people, 100 brown-eyed people, and the Guru (she happens to have green eyes). So any given blue-eyed person can see 100 people with brown eyes and 99 people with blue eyes (and one with green), but that does not tell him his own eye color; as far as he knows the totals could be 101 brown and 99 blue. Or 100 brown, 99 blue, and he could have red eyes. The Guru is allowed to speak once (let's say at noon), on one day in all their endless years on the island. Standing before the islanders, she says the following: **"I can see someone who has blue eyes."** Who leaves the island, and on what night? There are no mirrors or reflecting surfaces, nothing dumb. It is not a trick question, and the answer is logical. It doesn't depend on tricky wording or anyone lying or guessing, and it doesn't involve people doing something silly like creating a sign language or doing genetics. The Guru is not making eye contact with anyone in particular; she's simply saying "I count at least one blue-eyed person on this island who isn't me." And lastly, the answer is not "no one leaves."

### R3 — Cheryl's Birthday (SASMO 2015, verbatim)

Albert and Bernard just became friends with Cheryl, and they want to know when her birthday is. Cheryl gives them a list of 10 possible dates:

```
May 15, May 16, May 19
June 17, June 18
July 14, July 16
August 14, August 15, August 17
```

Cheryl then tells Albert and Bernard separately the month and the day of her birthday respectively.

- Albert: I don't know when Cheryl's birthday is, but I know that Bernard doesn't know too.
- Bernard: At first I don't know when Cheryl's birthday is, but I know now.
- Albert: Then I also know when Cheryl's birthday is.

So when is Cheryl's birthday?

### R4 — Cheryl's Age (the 2015 sequel, verbatim)

Albert and Bernard now want to know how old Cheryl is.

- Cheryl: I have two younger brothers. The product of all our ages (i.e. my age and the ages of my two brothers) is 144, assuming that we use whole numbers for our ages.
- Albert: We still don't know your age. What other hints can you give us?
- Cheryl: The sum of all our ages is the bus number of this bus that we are on.
- Bernard: Of course we know the bus number, but we still don't know your age.
- Cheryl: Oh, I forgot to tell you that my brothers have the same age.
- Albert and Bernard: Oh, now we know your age.

So what is Cheryl's age?

### R5 — The Zebra Puzzle (*Life International*, December 17, 1962, verbatim)

1. There are five houses.
2. The Englishman lives in the red house.
3. The Spaniard owns the dog.
4. Coffee is drunk in the green house.
5. The Ukrainian drinks tea.
6. The green house is immediately to the right of the ivory house.
7. The Old Gold smoker owns snails.
8. Kools are smoked in the yellow house.
9. Milk is drunk in the middle house.
10. The Norwegian lives in the first house.
11. The man who smokes Chesterfields lives in the house next to the man with the fox.
12. Kools are smoked in the house next to the house where the horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments.
15. The Norwegian lives next to the blue house.

Now, who drinks water? Who owns the zebra?

In the interest of clarity, it must be added that each of the five houses is painted a different color, and their inhabitants are of different national extractions, own different pets, drink different beverages and smoke different brands of American cigarets. One other thing: in statement 6, *right* means *your* right.

**Deliverable:** the full table (house 1–5 × color/nationality/drink/smoke/pet), not just the two answers.

### R6 — The Ant on the Rubber Band

An ant starts to crawl along a taut rubber rope 1 km long at a speed of 1 cm per second (relative to the rubber it is crawling on). At the same time, the rope starts to stretch uniformly at a constant rate of 1 km per second, so that after 1 second it is 2 km long, after 2 seconds it is 3 km long, etc. Will the ant ever reach the far end of the rope? If so, when, and how do you prove it? Your answer must address the *fraction of the rope* per unit time and the divergence that decides the outcome.

### R7 — 100 Prisoners & the Light Bulb

A prison holds 100 prisoners and has a special room containing nothing but a light bulb (initially, reliably OFF) and its switch. The warden will bring prisoners into that room one at a time, indefinitely, in an order each prisoner cannot predict (a prisoner may be brought back many times; every prisoner is eventually guaranteed to be brought in). Each prisoner, while in the room, may toggle the switch or leave it as is. There is no other channel of communication. The prisoners may agree on a strategy beforehand; once imprisonment begins they cannot talk. Each prisoner can observe the bulb's state and count his own visits (but only if he visits; a strategy may not rely on visits each prisoner cannot count... choose your counting carefully).

Devise a strategy under which some prisoner can at some moment declare **with certainty** that all 100 prisoners have visited the room at least once, and that declaration is never false. How many room-visits elapse until the declaration (best case / worst case / expected)? Justify all three.

### R8 — Two Eggs, 100 Floors

You have a 100-floor building and two identical eggs. There is an unknown threshold floor T (1 ≤ T ≤ 100): an egg dropped from floor ≥ T breaks; an egg dropped from floor < T survives intact and is reusable. (Dropping from exactly floor 100 with T = 100 breaks; define T = the lowest floor from which an egg breaks; assume such a T always exists.) A broken egg is gone for good. Design a drop strategy that minimizes the worst-case number of drops needed to determine T exactly, prove your worst-case bound, and prove no strategy can guarantee fewer.

### R9 — The Fly and the Two Trains

Two trains are 100 km apart on the same straight track, moving toward each other, each at 50 km/h. At the instant they start, a fly sitting on the nose of the first train flies toward the second train at 75 km/h; the instant it arrives at the second train's nose it reverses direction without losing speed, flies back to the first train, reverses again, and so on — until the trains collide. What total distance has the fly traveled?

### R10 — Twelve Coins, Three Weighings

You have 12 visually identical coins; exactly one is counterfeit and differs in weight from the other eleven — it may be **heavier or lighter, you don't know which**. You have a two-pan balance (no reference weights). In at most **three** weighings, identify the counterfeit coin **and** determine whether it is heavier or lighter. Present your strategy as a complete decision tree: every possible outcome branch of all three weighings leads to a definitive (coin, heavier/lighter) answer, with no branch left unassigned.

### R11 — The 100 Prisoners and 100 Boxes (hard tier)

The 100 prisoners are numbered 1 to 100. A room contains a cupboard with 100 boxes; the warden has placed one prisoner's number, chosen uniformly at random, inside each box — a uniformly random permutation of 1…100. One at a time, each prisoner enters the room and may open **at most 50** boxes, looking for their own number. A prisoner may not mark, move, or reorder boxes; after each prisoner leaves, every box is closed again exactly as found. If **every** prisoner finds their own number, all 100 are freed; if even one fails, all are executed. Before the game begins, the prisoners may agree on a strategy, but they cannot communicate once it starts.

**Deliverable:** the strategy that maximises the probability that all 100 survive, a proof that it does so, and the exact survival probability as a closed-form expression plus a decimal to four places. State explicitly what the warden's permutation being uniformly random buys you, and why the naive independent-search strategy is far worse.

### R12 — The Sum and Product Puzzle (Freudenthal, 1969) (hard tier)

Two integers `x` and `y` are chosen with `1 < x < y` and `x + y ≤ 100`. Perfect logician **S** is told only their sum `x + y`; perfect logician **P** is told only their product `xy`. Both know all the rules above. The following conversation occurs, in order:

- **P:** I don't know the two numbers.
- **S:** I knew you didn't know.
- **P:** Now I know.
- **S:** Now I also know.

**Deliverable:** determine `x` and `y`, and prove the answer is unique under this dialogue. Show the successive sets of possible pairs after each statement (or a table that makes the eliminations auditable) — a bare memorised pair scores near zero.

### R13 — The Five Pirates (hard tier)

Five perfectly logical pirates, A (oldest), B, C, D, E (youngest), have found 100 gold coins. They must divide the coins using this rule: the oldest surviving pirate proposes an allocation of all 100 coins (integer coins); every surviving pirate, **including the proposer**, votes. If **at least half** of the surviving pirates vote yes, the proposal passes and the game ends. Otherwise the proposer is thrown overboard, and the next-oldest surviving pirate proposes under the same rule. Every pirate's preferences are, in strict order: (1) survive; (2) maximise their own gold; (3) if survival and gold are equal either way, vote **no** so that the proposer is thrown overboard. All of this is common knowledge.

**Deliverable:** the allocation proposed by A under subgame-perfect equilibrium, the votes, and the full backward-induction table for 1, 2, 3, 4, and 5 pirates. State why the "at least half" threshold and the bloodthirsty tie-break both matter; changing either changes the answer.

## Section T — Thought (T1–T7) — *no answers exist*

These are famous open or contested questions. Nobody — neither judge nor peer nor model — knows "the answer", because **there is none**. You are graded on: comprehension of what is actually being asked; accurate survey of the state of the art (no invented citations); originality within honesty; rigor of your argument; and intellectual candor (saying clearly what you don't know). Always answer **in your own reasoning, not by reciting a memorized survey**: judges check whether grasp is real.

### T1 — P vs NP

Write a dossier on the single most famous open question in computer science. Required parts (≤ 600 words total):

1. A precise statement of what P = NP? is asking — define P, NP, NP-completeness, and the role of polynomial-time reductions (choose Cook–Levin or Karp framing; say which and why).
2. The three known *proof barriers* — relativization, natural proofs, algebrization — described accurately enough that your description shows you know what each actually constrains.
3. A survey of at least three concrete research directions (circuits, algebraic, descriptive complexity, machine-learning angle, etc.) how each actually went.
4. Your own position: which side you'd bet on, your probability, and your two strongest arguments — plus the strongest argument against yourself.

### T2 — Navier–Stokes Existence & Smoothness (Clay Millennium Problem)

One of six Clay Millennium problems carries a $1M bounty for mathematically settling whether smooth initial data for the incompressible 3D Navier–Stokes equations can develop singularities. Required (≤ 600 words): state precisely what "existence and smoothness" asks; why solutions *could* blow up (what the energy estimates do and don't buy); what partial results actually exist (weak solutions à la Leray; known smoothness classes; any conditional or partial regularity results — name at least one, correctly); then propose the research program *you* would bet on (energy methods, critical function spaces, harmonic analysis, numerics understanding of blow-up scenarios), and name honestly the obstacle standing in its way.

### T3 — The Riemann Hypothesis

Required (≤ 600 words): state exactly what RH claims about the non-trivial zeros of ζ(s); explain in one tight paragraph what it has to do with how well the primes can be predicted (error term in the Prime Number Theorem / explicit formula — keep it honest about what is equivalent and what is merely suggestive); present at least two distinct approaches or reformulations (function-field analogy & Weil proves, Hilbert–Pólya, random-matrix statistics of zeros, Lindelöf-on-steroids conjectures — pick real ones and describe them faithfully); then argue which line you find most promising and what a full proof would immediately unlock.

### T4 — The Quantum Measurement Problem

State the problem precisely: two valid-looking evolution rules (Schödinger unitary dynamics vs the collapse postulate) disagree about what happens when a quantum system interacts with a measuring device. Survey at least four interpretations (Copenhagen, Everett/Many-Worlds, de Broglie–Bohm, objective collapse (GRW/CSL), QBism or relational — pick real ones), in 2–4 sentences each, saying clearly what each counts as "measurement" and what it pays as a price (e.g. hidden variables, preferred basis, probability ontology). Then the thought part: propose **one** experimentally implementable discriminator (or argue carefully for why the space is fiendishly hard to test — with named constraints, e.g. Leggett-type inequalities, macroscopic superposition limits). Defend your pick. ≤ 600 words.

### T5 — Sleeping Beauty

Sleeping Beauty agrees to the experiment: on Sunday she is told the rules; a fair coin will be flipped. On Monday she wakes and is told today is Monday (heads or tails run). If the coin came up heads the experiment ends; if tails she is put to sleep again with amnesia of Monday and wakes Tuesday, told nothing about the day. **Question: when she wakes and formulates her credence that the coin landed heads, what should P(heads) be?** Halfers say 1/2, thirders say 1/3. Take a side and give the strongest argument for it; then steelman the opposing side as strongly as its best advocates actually give it; if you instead regard the question as ill-posed, say precisely in what sense (credence? betting? decision theory?) and what machinery would need to be added to make it well-posed. ≤ 400 words.

### T6 — What is Life?

Give an operational definition of "life" — criteria with cut-offs you actually commit to. Then stress-test it honestly against: viruses; prions; a growing crystal; a glider in Conway's Game of Life; a hypothetical von Neumann universal constructor; fire; a beehive (colony-level vs individual). Where your definition draws boundaries that *feel* wrong, diagnose whether the fault is the definition or our intuitions, and say which criterion you would bend first. One nod to Schrödinger's *What Is Life?* (1944) and what he got right is welcome; beyond that, the reasoning must be your own. ≤ 400 words.

### T7 — The Black Hole Information Paradox (hard tier)

Hawking's 1974 semiclassical calculation says a black hole radiates a thermal spectrum and evaporates. If the radiation is exactly thermal, the information about what formed the hole appears to be destroyed — but ordinary quantum mechanics is unitary, and a pure state must evolve to a pure state. That is the paradox. Required (≤ 500 words total):

1. **State it precisely.** Define unitarity, the Bekenstein–Hawking entropy `S = A/(4G)` (in appropriate units), the Page curve, and what "information recovery" would actually mean operationally. Say clearly which assumptions are semiclassical and which are quantum-gravitational.
2. **Survey the live positions**, 2–3 sentences each: black-hole complementarity (Susskind), the firewall argument (AMPS 2012), ER=EPR, and the island formula / replica-wormhole derivations of the Page curve (2019–20). State at least one concrete result or equation correctly; do not invent citations.
3. **Take a position.** Which line do you find most promising, what would count as a resolution, and what is the strongest objection to your view? Be explicit about what remains unknown — this problem is not experimentally settled.

## Section V — Visual Craft (V1–V7)

Read as an art director would: composition, palette discipline, typography, motion timing, and — where facts are on the canvas — **factual accuracy**. Deliverables are static code, renderable by judges with a browser. V5–V7 are the v3.0 hard tier: architecture, symmetry, and a real colour system (with WCAG math), not just decoration.

### V1 — Mona Lisa, in pure SVG

Recreate Leonardo da Vinci's *Mona Lisa* (c. 1503–1519, public domain) as hand-authored vector art. Constraints:

- One `\`\`\`svg` fenced block; root `<svg viewBox="0 0 400 600">`.
- No `<image>`, no external references, no CSS from outside the file; inline `<defs>` allowed.
- You may use `<linearGradient>`/`<radialGradient>` (use them for the *sfumato* mood) and at most one `<filter>` (a gaussian blur).
- Max **300** shape elements; keep a comment noting your palette choices.
- The silhouette (pose, hands, hair, veil, background) must read unmistakably as *her* — aim for "recognized at thumbnail size".

### V2 — Seven Founders of Computing, infographic

A hand-authored SVG infographic, `<svg viewBox="0 0 1200 700">`, single `\`\`\`svg` block, zero libraries. Content is fixed — all seven, pinned on a **to-scale timeline 1800–2000** (map birth years onto the x-axis truthfully):

- **Ada Lovelace** 1815–1852 — first published algorithm (Note G, Analytical Engine)
- **Alan Turing** 1912–1954 — universal machine (1936)
- **John von Neumann** 1903–1957 — stored-program architecture (EDVAC report, 1945)
- **Claude Shannon** 1916–2001 — information theory (1948)
- **Grace Hopper** 1906–1992 — compilers & COBOL
- **Edsger Dijkstra** 1930–2002 — shortest path; structured programming
- **Donald Knuth** 1938– — *The Art of Computer Programming*; analysis of algorithms

Each card: name, years, one-line fact as listed. Add **at least two** influence arrows between people you can justify (e.g. Turing → von Neumann's stored-program machine). Design goal: hierarchy, spacing rhythm, one palette, clean typography — the facts must be **accurate**; peers will fact-check.

### V3 — LIFTOFF: a 60-second motion graphic

Build a single-file HTML (`\`\`\`html` block, complete and opening via `file://`) that plays a **total-exactly-60-second looping** motion piece describing a rocket launch. You choose the tech (CSS keyframes, SVG SMIL, JS rAF — or a mix) but it must be genuinely timeline-driven.

Source comments must mark the beats at real timestamps, minimum:

- `0–8s` TITLE — "NKB-1 // T-MINUS" title card with subtle build-up
- `8–25s` COUNTDOWN — a compressed countdown readout (e.g. 10 → 0 numbers with animated telemetry bars)
- `25–40s` IGNITION & ASCENT — flame particles, camera shake, receding ground
- `40–60s` ORBIT & CREDITS — earth curvature drifts past, a satellite, credits fade that **dissolves seamlessly back to t=0**

Requirements: loop duration exactly 60.000s and seamless at the seam; `prefers-reduced-motion` → render a static "poster" keyframe instead; **zero external assets or libraries** (all inline); readable at 720p. Follow with `## V3-NOTES` (≤ 100 words): what you'd change with another day.

### V4 — The Café Rebuild Chart (data honesty test)

Below is 24 months of a café's revenue in EUR; it contains three stories braided together: **seasonality, a level change (renovation at month 13), and a one-off outlier (festival, month 19)**. Produce **one** static SVG chart (`<svg viewBox="0 0 900 500">`, single `\`\`\`svg` block, hand-computed coordinates or inline inline `<style>`+`<script>` allowed but no libraries) that tells the *honest* story:

- labeled axes with units; a chart type you can justify;
- the renovation month marked; the outlier visibly annotated as one-off;
- a headline reading that decomposes seasonal vs level vs outlier — the honest headline here is close to "the renovation's effect is ambiguous/modest, not '+X% growth'";

followed by `## V4-NOTES` (≤ 80 words) with your chart-type justification.

```
month,revenue_eur,note
1,38800,
2,37950,
3,41100,
4,40200,
5,42750,
6,43300,
7,45190,
8,44800,
9,41900,
10,40600,
11,38300,
12,39150,
13,41000,renovation begins (closed 10 days)
14,41500,
15,41900,
16,41100,
17,40800,
18,42100,
19,63500,festival weekend (one-off, city festival)
20,42700,
21,42300,
22,40900,
23,39800,
24,40100,
```

### V5 — The Eiffel Tower, architectural elevation (hard tier)

Recreate the Eiffel Tower (1889, Gustave Eiffel's company) as a **hand-authored architectural elevation** in pure SVG. No reference image is provided; work from the specification below.

- One `\`\`\`svg` fenced block; root `<svg viewBox="0 0 600 900">`.
- No `<image>`, no external references, no external CSS; inline `<defs>` allowed (max 2 gradients, max 1 filter).
- **Geometry is checkable.** Map height linearly onto the canvas: ground line `y = 850`, overall height 330 m at `y = 50` (so 1 m ≈ 2.424 px vertically). Draw the three platforms at the correct scaled heights: **57 m** (first), **115 m** (second), **276 m** (top). Platform deck lines must be within ±10 px of `y = 712`, `y = 571`, and `y = 181` respectively. Base width is **125 m** — make the outer legs span a plausible scaled base (roughly 300 px), and taper monotonically to the top.
- Must read as the Eiffel Tower: four splayed legs, the two large decorative arches between the legs, three platforms, lattice/cross-bracing on the lower and middle sections, a tapering upper shaft, and an antenna. No solid silhouette-only cheat: at least 40 distinct lattice/brace elements must be visible.
- Include a small scale/annotation block inside the SVG: `1889 · 330 m overall · 125 m base · platforms 57 / 115 / 276 m`, plus a 0–100 m scale bar. Palette ≤ 6 colours; include a `<!-- palette: ... -->` comment.
- Max **220** shape elements. At 120 px wide it must still be recognisable as the Eiffel Tower.

### V6 — The Taj Mahal, bilateral symmetry (hard tier)

Recreate the Taj Mahal's garden façade as a **single hand-authored SVG** with true bilateral symmetry.

- One `\`\`\`svg` fenced block; root `<svg viewBox="0 0 900 600">`.
- **Symmetry contract:** the composition must be mirror-symmetric about `x = 450` to within 1 px (use one mirrored `<g transform="translate(900,0) scale(-1,1)">` for the repeated half; the central dome and finial may be drawn once on the axis). No asymmetric decorative elements.
- Required silhouette: raised plinth, central onion dome with finial, four minarets (two visible in front, two behind — all four must be drawn), the large central iwan/arch, side arches, reflecting pool with a symmetric reflection, and cypress trees.
- **Factual/proportional anchors:** annotate `1632–1653 · dome ≈ 73 m · minarets ≈ 40 m`. Make the dome clearly taller than the minarets; the minarets must read as four separate towers, not columns attached to the façade.
- Palette ≤ 8 colours (marble/ivory, sandstone, sky, water, green, shadow); include a `<!-- palette: ... -->` comment.
- Max **260** shape elements. Sunrise/sunset mood allowed but keep the marble legible; no `<image>` or external assets.

### V7 — Earth: a colour system, not a poster (hard tier)

Build a single SVG **design-system board** for a fictional Earth-observation brand. It must prove the palette works, not just display it.

- One `\`\`\`svg` fenced block; root `<svg viewBox="0 0 1200 800">`; no `<image>`, external fonts, or external CSS.
- **Fixed core palette (use these exact values):**

  | Token | Hex | Meaning |
  |---|---|---|
  | `void` | `#05070D` | space / background |
  | `ocean` | `#0B3D91` | deep water |
  | `atmosphere` | `#7FD4FF` | scattered light |
  | `forest` | `#1F6F43` | biosphere |
  | `sand` | `#D9B26A` | desert / lithosphere |
  | `ice` | `#F2F7FA` | cryosphere / text |
  | `magma` | `#C1440E` | heat / alert |
  | `city` | `#FFC857` | human light |

  You may add at most **2** neutral tints (e.g. a shadow and a grid line); no other hues.
- **Board contents (all required):**
  1. A stylised Earth disc at least 360 px across, rendered **only** from the core palette: at least three recognisable land masses, cloud swirls, an atmosphere rim, and a day/night terminator. It must look like Earth, not a generic marble.
  2. Eight swatch cards: token name, hex, and a one-line usage rule (where the colour is allowed / forbidden).
  3. **WCAG 2.1 contrast block:** at least three text/background pairs from the palette, each with the computed contrast ratio to **two decimal places**. Include at least one pair ≥ 7:1 (AAA) and one pair in 4.5–7:1 (AA). Show the formula or the relative-luminance values you used. Judges will recompute these — invented ratios score 0.
  4. A 60-30-10 usage bar with percentages that sum to 100, using the palette.
  5. A short typographic hierarchy (display / body / caption) in system fonts only.
- Max **200** shape elements. Include a `<!-- palette: ... -->` comment. The board must remain readable at 50% zoom.

## Section A — Algorithm Design (A1–A4)

No execution — design, invariants, and honest complexity claims. Pseudo-code ≤ 60 lines per task, inside the prose. Points live in: correctness of the mechanics, real amortized analysis (not hand-waving), edge-case awareness.

### A1 — The O(k) Prefix-Scan KV Store

Design an in-memory key–value store with exactly these operations and budget: `GET` O(1); `SET` O(1) amortized; `DELETE` O(1); `SCAN(prefix)` O(k) where k = number of matches (explicitly **not** O(total keys)); plus "survives 10M keys in one heap without GC death" — say what your per-key overhead is and why. Deliverable: chosen data structure(s) with diagram-in-words, invariants maintained by each op, the amortized argument for SET, correctness of the scan, and honest failure modes (e.g. delete-then-scan, iterating a mutating snapshot).

### A2 — Counting the Unidentifiable (streaming distinct count)

Design **two** algorithms for the number of *distinct* elements in a potentially endless data stream, with bounded memory: (1) an **exact** one for the regime where n is small enough to fit; (2) a **probabilistic** one for ≫10⁶ distinct (describe a real sketch — K-Minimum-Values/MinHash-flavored or HyperLogLog-style — with its estimator and a genuine (not vibes!) mathematical statement of its standard error); give the **merge rule** for combining distributed sketches and say what failure modes bias the count. ≤ 550 words + pseudo-code.

### A3 — The Melting Hashtag (sharding under hot keys)

A counter service: cluster of cache nodes, load-balanced by consistent hashing with virtual nodes; `INCR(hashtag)` is the whole API. A concert tweet creates a celebrity hashtag that receives ~50k INCR/s — consistent hashing maps it to exactly one node, which melts. Deliverables: (i) the consistent-hashing design with vnodes and what actually moves when a node dies; (ii) a **two-layer** mitigation that resolves the hot-key melt (local aggregation buffers, key-splitting, or both — justify your choice with the staleness/accuracy trade-off); (iii) invariants + failure behavior (net split, node death mid-buffer-flush); (iv) pseudo-code of the hot path. Bounded: ≤ 550 words.

### A4 — The Convergent Text (sequence CRDT, hard tier)

Design a **multi-writer collaborative plain-text** document that converges without a central server. Any replica may edit offline; replicas exchange operations in arbitrary order and at arbitrary times; every replica must eventually show the same text. This is the problem solved by RGA/LSEQ/Yjs-style sequence CRDTs — you must design the mechanism, not name-drop it.

**Deliverables (≤ 650 words + pseudo-code ≤ 50 lines):**

1. **Replica state and identifiers.** How is a character identified uniquely across replicas? What metadata travels with each insert/delete?
2. **Total order.** Give the exact deterministic tie-break that orders concurrent insertions at the same position. Prove that all replicas compute the same order for any two concurrent characters (commutativity + confluence), including the delete/insert interleavings.
3. **The interleaving anomaly.** Show a concrete timeline where two users concurrently type "HELLO" and "WORLD" at the same position and a naive tie-break produces `HWEOLRLLOD`; state whether your design prevents it, and if it accepts it, why that is acceptable.
4. **Tombstones and garbage collection.** Why deletions must leave a trace; give a **safe** reclamation rule (what must be true about causal stability/frontier before a tombstone can be dropped) and show a counterexample if the rule is violated.
5. **Cost.** Per-character metadata overhead; memory for a 1M-character document with 20% deletions; merge cost for an operation log from 30 offline days; one bounded-buffer strategy.
6. **One adversarial failure mode** (buggy or Byzantine replica) and the mitigation.

## Section F — Frontend (F1)

Build **one complete, single-file web app**. Deliverable: a single fenced code block containing a full `index.html` (HTML + CSS + JS, all inline). It must open directly via `file://` in Chrome or Edge with **zero network access and zero external dependencies** (no CDN, no imports, no fonts fetched). This is the v3.0 hard build: a 10,000-row virtualised data grid, a command palette, and undo/redo — not just a dashboard.

### Spec — "Mission Control" (v3.0)

1. **Header**: mission name ("NIKBENCH-1"), a live UTC clock (`HH:MM:SS`) updated every second, and a **mission-time selector** (UTC offset −12…+14, persisted) that shows the current time in the selected zone next to UTC.
2. **Metrics strip**: four stat cards — Fuel %, Battery %, Signal dB, Crew count — each initialized from a deterministic PRNG you implement inline (seed 42; e.g. mulberry32) and updated every 5 seconds with a small bounded random walk (no negative values, capped at maxima: fuel 100, battery 100, signal 0–99, crew 6, 2 decimals for fuel/battery).
3. **Countdown**: a live countdown to `2026-12-01T09:00:00Z`, displayed as `DD:HH:MM:SS`. If the target already passed, display status `LANDED` and an elapsed `T+DD:HH:MM:SS` instead.
4. **Satellite grid**: **10,000 deterministic rows** generated by the seeded PRNG (invent the schema; every field plausible). Columns: ID, Name, Orbit type (LEO/MEO/GEO), Status (ACTIVE, DEGRADED, OFFLINE), Last contact (relative, e.g. "4m ago", counting up live). The grid must be **virtualised** — only rows near the viewport exist in the DOM at any time — and must survive scroll, sort, and filter without freezing. Clicking a column header sorts by that column (asc ⇄ desc, visible ▲/▼ indicator); a search box filters by ID/name live; a visible row count reflects the filter.
5. **Telemetry chart**: a `<canvas>` line chart of **two series** (Signal and Fuel) over the last 60 samples (one per second), redrawn every second, with y-axis min/max labels, a visible baseline axis, and a legend. A pointer crosshair shows the nearest sample's values in a tooltip. Colours read from CSS variables, not hardcoded script values; the canvas must handle high-DPI displays.
6. **Command palette**: `Ctrl`/`Cmd`+`K` opens a palette with fuzzy search over satellites **and** actions (toggle theme, run diagnostic, sort by a column, clear anomalies, jump to grid). `↑`/`↓` move, `Enter` runs, `Esc` closes; focus is trapped while open; it is fully keyboard operable and announced (`role="dialog"`/combobox semantics).
7. **Anomaly feed**: RUN DIAGNOSTIC appends a simulated event (timestamp + severity + message) chosen from a pool of ≥ 8 messages; each item has an "✕" dismiss button. **Undo/redo** (`Ctrl+Z` / `Ctrl+Shift+Z` or `Ctrl+Y`) restores/redoes the last ≥ 20 dismissal/diagnostic actions, with a visible history indicator.
8. **Persistence** under localStorage keys prefixed `nikbench.f1.`: survive reload — table sort column+direction, theme, dismissed anomalies, metric values, filter query, selected timezone, and chart series visibility.
9. **Theme toggle**: dark is default; keyboard shortcut `d` toggles light/dark; also a clickable toggle button. Both themes must have proper contrast.
10. **Responsive**: metrics strip is 4 columns on wide, 2 on tablet, 1 on ≤ 480px; the grid collapses to one card per row below 640px; the command palette is full-screen on mobile; no horizontal scroll at 375px width.
11. **Accessibility**: semantic landmarks (`header`, `main`, `aside`/`section`), `aria-label`s on all icon-only/interactive controls, visible focus styles, `aria-live` for feed changes, full keyboard operation of grid and palette, and `prefers-reduced-motion` respected (no sweeping animations when set — render a static state instead).

The build must be deterministic: identical seed → identical rows and metrics. Document your virtualisation and PRNG choices briefly in the notes.

After the code block write `## F1-NOTES` (≤ 150 words): assumptions and anything knowingly skipped.

## Section B — Backend (B1)

Build a **single-file, dependency-free Node.js (≥ 18) HTTP server**. Deliverable: one fenced code block with a complete `api.js`, runnable as `node api.js` (port `process.env.PORT || 3000`), only Node built-ins, consistent module style. This is the v3.0 hard build: idempotency, optimistic concurrency, pagination, request IDs, and an audit log — on top of the booking contract.

### Spec — "Clinic Appointment API" (v3.0)

In-memory data. All timestamps UTC ISO-8601. Every non-2xx response carries the envelope:

```json
{ "error": { "code": "<MACHINE_CODE>", "message": "<human readable>", "request_id": "<uuid>" } }
```

Every response (2xx and non-2xx) carries an `X-Request-Id` header: echo a client-supplied `X-Request-Id` if it is a valid UUID, otherwise generate a UUIDv4. The same value must appear in error envelopes.

**Idempotency (global rule for unsafe methods).** `POST /doctors` and `POST /appointments` accept an `Idempotency-Key` header (8–128 chars):

- first time a key is seen for a method+path: process normally and store `(key, sha256(body), status, response_body)`;
- same key **and** identical body hash: replay the stored status and body exactly, with no side effects;
- same key **different** body: `409 IDEMPOTENCY_CONFLICT`.

**Endpoints**

| # | Endpoint | Behavior |
|---|----------|----------|
| 1 | `GET /health` | `200 { "status": "ok", "uptime_s": <int>, "version": "1.0" }` |
| 2 | `POST /doctors` | body `{ "name": str(2..80), "specialty": str(2..40) }` → `201` doctor `{ "id", "name", "specialty", "created_at" }` |
| 3 | `GET /doctors` | `200` array of doctors |
| 4 | `POST /appointments` | body `{ "doctor_id", "patient_name" (2..100), "start" (ISO), "duration_min" ∈ {15,30,…,120} }` → `201` appointment `{ "id", "doctor_id", "patient_name", "start", "end", "duration_min", "status": "scheduled", "version": 1, "created_at" }` |
| 5 | `GET /appointments` | query `doctor_id`, `date=YYYY-MM-DD` (UTC day), `limit` (1..100, default 20), `cursor` → `200 { "data": [...], "next_cursor": <string\|null> }`. Sorted by `(created_at, id)`. Invalid `limit`/`cursor` → `422 VALIDATION_ERROR`; unknown `doctor_id` → `404 DOCTOR_NOT_FOUND` |
| 6 | `GET /appointments/:id` | `200` with an `ETag` header (`"v<version>"`); missing → `404 APPOINTMENT_NOT_FOUND` |
| 7 | `PATCH /appointments/:id` | requires `If-Match: "v<version>"`; missing header → `428 PRECONDITION_REQUIRED`; stale/mismatched version → `412 PRECONDITION_FAILED`; body `{ "status": "confirmed" \| "cancelled" }`; only from `scheduled`; modifying a cancelled appointment → `409 APPOINTMENT_CANCELLED`. On success: increment `version`, return the new `ETag` |
| 8 | `DELETE /appointments/:id` | only when `scheduled` → `204`; otherwise `409 APPOINTMENT_NOT_SCHEDULED` |
| 9 | `GET /audit` | `200 { "data": [...], "next_cursor": <string\|null> }`; query `limit` (1..200, default 50), `entity_id`, `cursor`. Append-only events `{ "id", "ts", "action", "entity", "entity_id", "actor" }` where `actor` comes from the optional `X-Actor` header (default `"anonymous"`). Every mutation (doctor/appointment create, confirm, cancel, delete) appends exactly one event |

**Invariants for `POST /appointments`** (first violated rule wins, in this exact priority order):

1. malformed/missing JSON body → `400 INVALID_JSON`;
2. idempotency replay/conflict (see above);
3. `doctor_id` of an existing doctor, else `404 DOCTOR_NOT_FOUND`;
4. wrong types / out-of-range fields → `422 VALIDATION_ERROR` (list ALL offending fields);
5. `start` must be valid ISO-8601 UTC and not before server start time → `422 VALIDATION_ERROR`;
6. overlap: the new `[start,end)` must not overlap any non-cancelled appointment of the same doctor → `409 SLOT_TAKEN`. Touching is allowed (`end == next start` is legal);
7. IDs are immutable unique strings you generate (`dr_…`, `appt_…`).

**Cursor semantics.** `next_cursor` is opaque; it must let a client page forward across inserts without duplicating or skipping rows that were present at the first request. Pass `null` when the page is the last.

**Graceful shutdown.** On `SIGINT`/`SIGTERM`: stop accepting new connections, let in-flight requests finish, exit within 2 seconds.

**Prose answers (`## B1-D1` … `## B1-D6`, each ≤ 120 words)**

- **D1 — Concurrency:** make the no-overlap invariant safe under two simultaneous bookings on real PostgreSQL: transactions, isolation, locks/unique constraints; why app-side checks fail.
- **D2 — Auth:** token scheme + roles (`receptionist`, `doctor`, `admin`), lifetimes, endpoint gating. Sketch.
- **D3 — Rate limiting:** algorithm choice (justify token bucket vs fixed window), scope, response headers.
- **D4 — Persistence:** PostgreSQL DDL sketch (tables, FKs, indexes) that prevents double-booking at DB level, including the `version` column for optimistic concurrency.
- **D5 — Failure mode:** one realistic silent-failure mode of your own implementation above + mitigation.
- **D6 — Exactly-once webhooks:** the clinic must notify an external calendar service when an appointment is confirmed. Design the outbound delivery (retries, exponential backoff, signatures, dead-letter). Explain why end-to-end exactly-once is impossible and what you do instead; state the receiver-side rule that makes duplicates harmless.

## Output contract for Phase 1 (exact)
Respond in this section order, `##` headers, nothing outside them. Begin the file with a single metadata line so runs stay comparable:

```
<!-- nikbench.meta: bench=v3.0 model=<your-name> date=<YYYY-MM-DD UTC> params=<temperature/top_p or "default"> -->
```

```
## R1 … ## R13      derivation then  Final Answer: <value>
## T1 … ## T7       dossiers (respect each task's word cap)
## V1               one ```svg block
## V2               one ```svg block
## V3               one ```html block
## V3-NOTES         ≤ 100 words
## V4               one ```svg block
## V4-NOTES         ≤ 80 words
## V5               one ```svg block
## V6               one ```svg block
## V7               one ```svg block
## A1 … ## A4       design prose (+ optional pseudo-code)
## F1               one ```html block, complete index.html
## F1-NOTES         ≤ 150 words
## B1               one ```javascript block, complete api.js
## B1-D1 … ## B1-D6 each ≤ 120 words
```

**Then (harness exception only):** write the ENTIRE content above to `submissions/<your-name>.md` using the `write` tool — one file, everything.

**Then STOP.** Final chat response exactly:

```
PHASE 1 COMPLETE — waiting for peers
```

(Phase 2 unlocks in a later chat when the roster is complete. Do not attempt it now.)

---

# PHASE GATE (runs whenever your submission already exists)

You may now list/read the `submissions/` directory.

- Peer round requires **your submission + at least 2 other models' submissions**.
- If fewer: reply exactly `PHASE 2 LOCKED — waiting for peers` and stop.
- If enough: proceed to **PHASE 2**.

Permitted reads from here on: everything in `submissions/`, your own `peer/` state refresh, `scripts/`, `leaderboard.md`, and `README.md`. Still **forbidden**: anyone else's `peer/` files (if present), `scorecards/`, `docs/`, `judging/` — rate on your own eyes.

---

# PHASE 2 — PEER REVIEW (rate the others, then yourself — in that order)

1. **Read every submission file** in `submissions/` (all candidate .md files; skip `README.md`).
2. For each, grade **six pillars (0–10 each)** and an **Overall**:
   - **RAT 🧩:** re-solve what you can — R1–R13, including the hard tier (100 prisoners & boxes, Freudenthal's sum-and-product, the five pirates). Verify derivations line by line. Sound working + correct answers = high; lucky guesses or confidently wrong derivations = low.
   - **THO 🧠:** no answers exist — grade comprehension, accuracy of the survey (punish invented names/claims), originality of the attack, argument quality, candor about unknowns. T7 (black-hole information) is graded the same way.
   - **VIS 🎨:** read SVG/HTML/CSS as an interpreter; does the art actually draw the thing (Mona Lisa, founders, Eiffel geometry, Taj symmetry, Earth palette)? do the facts hold? is the motion timeline coherent & 60 s? is the chart honest about the outlier trap? For V7, recompute the WCAG ratios yourself — invented ratios are a fail.
   - **ALG 🧮:** are the complexity claims actually proven? edge cases handled? did they invent or cargo-cult? A4 (sequence CRDT) must survive the interleaving anomaly and prove convergence, not name-drop CRDTs.
   - **Frontend (FE) 🪟:** check the spec requirements (clock + timezone, seeded cards, countdown + LANDED, virtualised 10k-row grid, dual-series canvas chart, command palette, undo/redo, anomaly feed, localStorage, theme, responsive, a11y).
   - **Backend (BE) ⚙️:** trace endpoints against the spec (status codes, error envelope + `request_id`, idempotency replay/conflict, ETag/If-Match 412/428, pagination shape, audit events, overlap rules, validation priority). Mentally execute before believing.
3. Calibrate: **5 = solid pass**, **8–9 = excellent**, **10 = would ship today**, **0–2 = broken/empty**. Length ≠ quality; placeholders are near-fatal.
4. No copying others' opinions; grade what's on the page. Score the work, not the name — if you recognize a model, set that aside and let the derivation carry the score.

### Output — one file: `peer/<your-name>.md` (via the `write` tool)

```markdown
# Peer review by <your-name>

| Model | RAT | THO | VIS | ALG | FE | BE | Overall | One-line justification |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| <every other model, highest Overall first> | … | … | … | … | … | … | … | … |
| _<your-name> (self)_ | … | … | … | … | … | … | … | … |
```

…then this machine-read block (the script parses **this**; the table is for humans — your own entry is **last** with `"self": true`):

```json
{
  "schema": "nikbench.peer.v1",
  "reviewer": "<your-name>",
  "ratings": {
    "<model-name>": { "rat": 0, "tho": 0, "vis": 0, "alg": 0, "fe": 0, "be": 0, "overall": 0, "self": false },
    "<your-name>":   { "rat": 0, "tho": 0, "vis": 0, "alg": 0, "fe": 0, "be": 0, "overall": 0, "self": true }
  }
}
```

Values: integers or halves 0–10. Include **every** submission. Phase 3 = rating yourself — it happens **now, as the last row**: inflating yourself is obvious next to peer votes.

**Then STOP.** Final chat response exactly: `PEER REVIEW WRITTEN — <N> rated`.

---

# PHASE 3 — BOARD REFRESH (only when your peer file already exists)

If `peer/<your-name>.md` already exists, you are re-entering after the peer round.

1. Run: `python scripts/aggregate.py scorecards --peer-dir peer -o leaderboard.md`
   - If the script is missing or fails: leave the board untouched and report the error in your final message instead.
2. Update **README.md** inside the markers `<!-- NIKBENCH:LEADERBOARD:START -->` and `<!-- NIKBENCH:LEADERBOARD:END -->` with the fresh contents of `leaderboard.md` (keep the legend/notes inside the markers). Do not touch anything else in README.
3. Best-effort git: `git add -A` → commit message `NikBench run: <your-name>` → `git push`.
   - If push fails: `git pull --rebase` once and retry; still failing → leave the local commit and say so.
4. Final chat response exactly: `PHASE 3 COMPLETE — board updated` (or a precise failure note).

---

# PHASE 4 — REVISION ROUND (optional, v3.0+)

If `peer/<your-name>.md` already exists **and** the human opts into a revision round:

1. Read your own Phase-1 submission and the **peer notes addressed to you** (the one-line justifications and your self-vs-peer gap).
2. Produce a **patched** submission at `submissions/<your-name>.md` containing **only the sections you changed**, each prefixed with `## <section> (rev 2)`, plus a `## CHANGELOG` (≤ 150 words) stating what you fixed and why. Do not rewrite unchanged sections.
3. Run the Phase Router again in a fresh chat; the board refresh (Phase 3) re-grades the delta and reports both scores.

Purpose: tests responsiveness to critique, diff discipline, and honesty ("did you actually fix the flagged bug?").

---

*Protocol design: `docs/methodology.md`. Rubric judges (optional deep-grading): `judging/judge.md`. Current board: the marked block inside `README.md`.*
