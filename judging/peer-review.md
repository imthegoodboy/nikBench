# NikBench v2.0 — Peer & Self Review Packet

> **Runtime note (v1.2+):** this round is embedded in `test.md` (Phase 2) — the normal flow no longer reads this file; `test.md` is the single packet you paste. This file remains as the standalone reference for the peer/self round.

You are one of the candidate models after your blind build. Now you read every submission and rate them — then rate yourself, as the deliberate last row.

## What to do

1. Read every file in `submissions/` (skip `README.md`).
2. Grade each on **six pillars, 0–10**, plus an Overall:
   - **RAT 🧩** (R1–R10): re-solve what you can; derivations line by line. Wrong-but-shown beats lucky answers.
   - **THO 🧠** (T1–T6): no answers exist — comprehension, accuracy (punish invented citations), originality of the attack, argument quality, candor about limits.
   - **VIS 🎨** (V1–V4): does the SVG actually draw the thing? founders' facts right? 60-s loop coherent? chart honest about the month-19 outlier trap?
   - **ALG 🧮** (A1–A3): complexity claims provable? edge cases? innovation without cargo-culting?
   - **FE 🪟** (F1): the 10 spec requirements, one by one.
   - **BE ⚙️** (B1): endpoint matrix, error envelope, invariant priority a→f, state machine. Mentally execute first.
3. Calibrate: **5 = solid pass · 8–9 = excellent · 10 = ship-today · 0–2 = broken/empty**. Length ≠ quality; placeholders → near-fatal.
4. Then the self row — rating your own submission honestly. **Self-inflation is visible** in the aggregated `Self` column; an honest 6 next to peers' 4 reads better than a fake 9.

## Output — `peer/<your-name>.md`

A human-readable table **(others first, your own row last)**:

```markdown
| Model | RAT | THO | VIS | ALG | FE | BE | Overall | One-line justification |
|---|---:|---:|---:|---:|---:|---:|---:|---|
```

…followed by the machine block (this is what `scripts/aggregate.py` parses):

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

Ratings = integers or halves, 0–10. Include **every** submission in `ratings`. Final board formula (v1.1+): `Final = 0.6·NBS + 0.2·Peer + 0.2·Self` — your peer votes carry real weight, and the board is permanent.
