# NikBench v1.0 — Candidate Packet

> **How you got this:** a human pasted this file into a fresh chat with you. Nothing else accompanies it.
> Your full reply will be saved as a peer submission and given to **three or more independent judge models**. The judges do **not** receive any answer key — they will independently solve every task and rate your output. Unsupported correct answers lose points; wrong answers with sound, honest reasoning are scored more fairly than lucky guesses.

You are evaluated on three pillars: **Reasoning**, **Frontend engineering**, and **Backend engineering**. Do all three.

---

## Rules (strict)

1. **One single response.** Everything you produce must be in this reply. Do not ask questions back; if a spec is ambiguous, pick the most reasonable interpretation and note it in that task's notes.
2. **No tools.** No internet, no code execution, no file system, no analysis mode. Pure generation.
3. **No placeholders.** `TODO`, `...`, "left as an exercise", mock stubs where real code is asked for, or truncated code are heavily penalized. Every code block must be complete and runnable as-is.
4. **Show derivations.** For reasoning tasks, give a concise derivation (not an essay), then a line reading exactly `Final Answer: <value>`. For multiple-choice tasks, the value is the option letter, e.g. `Final Answer: (B)`.
5. **Assume UTC everywhere.** State any constant seeds you use inside the code.
6. **Do not restate the tasks.** Solve them. No meta commentary about being an AI, no flattery, no closing speech.

---

## Section A — Reasoning (R1–R10)

Answer each numbered problem. The problems are taken verbatim from public benchmark datasets (GSM8K, AQuA-RAT, BIG-Bench Hard); solve them fresh — do not recite memorized answers without a derivation, because judges verify your reasoning line by line. End each with `Final Answer: <value>`.

### R1
The Adams family is busy making cookies. So far, they've made 7995 cookies. They have 2595 rainbow cookies, 3075 oatmeal cookies, and some chocolate chip cookies. How many chocolate chip cookies have they made?

### R2
Nate's dog can dig six holes a day. He digs for 14 days while Nate is on vacation. When Nate gets home, he starts filling in 9 holes a day, but the dog keeps digging 6 new holes every night. How many weeks does it take him to fill in all the holes?

### R3
If the probability that Stock A will increase in value during the next month is 0.56, and the probability that Stock B will increase in value during the next month is 0.74. What is the greatest value for the probability that neither of these two events will occur?

### R4
At a certain factory, 10 percent of the staplers produced on Monday were defective and 2 percent of the non-defective staplers were rejected by mistake. If 72 of the non-defective staplers were rejected, what was the number of staplers produced that day?

### R5
Evaluate the arithmetic expression:

```
((-1 + 2 + 9 * 5) - (-2 + -4 + -4 * -7)) =
```

### R6
Evaluate the arithmetic expression:

```
((-9 * -5 - 6 + -2) - (-8 - -6 * -3 * 1)) =
```

### R7
The following paragraph describes a set of five objects arranged in a fixed order. The statements are logically consistent. On a branch, there are five birds: a quail, an owl, a raven, a falcon, and a robin. The owl is the leftmost. The robin is to the left of the raven. The quail is the rightmost. The raven is the third from the left.

Options:
(A) The quail is the rightmost
(B) The owl is the rightmost
(C) The raven is the rightmost
(D) The falcon is the rightmost
(E) The robin is the rightmost

### R8
Today is Christmas Eve of 1937. What is the date tomorrow in MM/DD/YYYY?

Options:
(A) 12/11/1937
(B) 12/25/1937
(C) 01/04/1938
(D) 12/04/1937
(E) 12/25/2006
(F) 07/25/1937

### R9
Alice, Bob, Claire, Dave, and Eve are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Patrick, Bob is dancing with Sam, Claire is dancing with Jamie, Dave is dancing with Lola, and Eve is dancing with Melissa.

Throughout the song, the dancers often trade partners. First, Dave and Eve switch partners. Then, Dave and Alice switch partners. Then, Eve and Alice switch partners. Then, Claire and Bob switch partners. Finally, Dave and Alice switch partners. At the end of the dance, Alice is dancing with

Options:
(A) Patrick
(B) Sam
(C) Jamie
(D) Lola
(E) Melissa

### R10
Question: Sherrie tells the truth. Vernell says Sherrie tells the truth. Alexis says Vernell lies. Michaela says Alexis tells the truth. Elanor says Michaela tells the truth. Does Elanor tell the truth?

---

## Section B — Frontend (F1)

Build **one complete, single-file web app**. Deliverable: a single fenced code block containing a full `index.html` (HTML + CSS + JS, all inline). It must open directly via `file://` in Chrome or Edge with **zero network access and zero external dependencies** (no CDN, no imports, no fonts fetched).

### Spec — "Mission Control"

1. **Header**: mission name ("NIKBENCH-1"), and a live UTC clock (`HH:MM:SS`) updated every second.
2. **Metrics strip**: four stat cards — Fuel %, Battery %, Signal dB, Crew count — each initialized from a deterministic PRNG you implement inline (seed 42; e.g. mulberry32) and updated every 5 seconds with a small bounded random walk (no negative values, capped at maxima: fuel 100, battery 100, signal 0–99, crew 6, 2 decimals for fuel/battery).
3. **Countdown**: a live countdown to `2026-12-01T09:00:00Z`, displayed as `DD:HH:MM:SS`, correct even if the target date already passed (then display `T-00:00:00:00` with status `LANDED`).
4. **Satellite table**: 8 fixed rows (invent the IDs/names); columns: ID, Name, Orbit type (LEO/MEO/GEO), Status (ACTIVE, DEGRADED, OFFLINE), Last contact (relative, e.g. "4m ago", counting up live). Clicking a column header sorts by that column (asc ⇄ desc, visible arrow indicator ▲/▼).
5. **Telemetry chart**: a `<canvas>` line chart of the Signal metric over the last 60 samples (one per second), redrawn every second, with y-axis min/max labels and a visible baseline axis. Colors read from CSS variables, not hardcoded script values.
6. **Anomaly feed**: a list. A button "RUN DIAGNOSTIC" appends a simulated event (timestamp + severity + message) chosen from a pool of ≥ 6 messages; each list item has an "✕" dismiss button that removes it.
7. **Persistence** under localStorage keys prefixed `nikbench.f1.`: survive reload — table sort column+direction, theme, dismissed anomalies, and the current metric values (rehydrate roughly where they left off).
8. **Theme toggle**: dark is default; keyboard shortcut `d` toggles light/dark; also a clickable toggle button. Both themes must have proper contrast.
9. **Responsive**: metrics strip is 4 columns on wide, 2 on tablet, 1 on ≤ 480px, no horizontal scroll at 375px width.
10. **Accessibility**: semantic landmarks (`header`, `main`, `aside`/`section`), `aria-label`s on all icon-only/interactive controls, visible focus styles, and `prefers-reduced-motion` respected (no sweeping animations when set).

After the code block you will write `## F1-NOTES` (≤ 150 words): assumptions made and anything you knowingly skipped.

---

## Section C — Backend (B1)

Build a **single-file, dependency-free Node.js (≥ 18) HTTP server** — deliverable: one fenced code block containing a complete `api.js` runnable as `node api.js` (port: `process.env.PORT || 3000`), no npm install, no frameworks, only Node built-ins, ES2022 or CommonJS (your choice, but consistent).

### Spec — "Clinic Appointment API"

In-memory data. All timestamps are UTC ISO-8601. Every non-2xx response uses the envelope:

```json
{ "error": { "code": "<MACHINE_CODE>", "message": "<human readable>" } }
```

**Resources & endpoints**

| # | Endpoint | Behavior |
|---|----------|----------|
| 1 | `GET /health` | `200 { "status": "ok", "uptime_s": <int> }` |
| 2 | `POST /doctors` | body `{ "name": str(2..80), "specialty": str(2..40) }` → `201` doctor `{ "id", "name", "specialty", "created_at" }` |
| 3 | `GET /doctors` | `200` array of doctors |
| 4 | `POST /appointments` | body `{ "doctor_id", "patient_name" (2..100), "start" (ISO), "duration_min" ∈ {15,30,...,120} }` → `201` appointment `{ "id", "doctor_id", "patient_name", "start", "end", "duration_min", "status": "scheduled", "created_at" }` |
| 5 | `GET /appointments` | optional query `doctor_id`, `date=YYYY-MM-DD` (UTC day); unknown `doctor_id` → 404 `DOCTOR_NOT_FOUND` |
| 6 | `GET /appointments/:id` | `200` or `404 APPOINTMENT_NOT_FOUND` |
| 7 | `PATCH /appointments/:id` | body `{ "status": "confirmed" \| "cancelled" }` — only from `scheduled`; modifying a cancelled appointment → `409 APPOINTMENT_CANCELLED` |
| 8 | `DELETE /appointments/:id` | only when `scheduled` → `204`; otherwise `409` |

**Invariants for `POST /appointments`** (any violated rule → exactly one error, priority order):

- a. `doctor_id` of an existing doctor, else `404 DOCTOR_NOT_FOUND`.
- b. malformed/missing JSON body → `400 INVALID_JSON`.
- c. wrong types / out-of-range fields → `422 VALIDATION_ERROR` (list ALL offending fields in the message).
- d. `start` must be valid ISO-8601 UTC and not before server start time → `422 VALIDATION_ERROR`.
- e. overlap: the new `[start,end)` must not overlap any non-cancelled appointment of the same doctor → `409 SLOT_TAKEN`. Touching is allowed (`end == next start` is legal).
- f. IDs are immutable strings you generate (`dr_…`, `appt_…`) and unique.

**Prose answers (each ≤ 120 words, sections `## B1-D1` … `## B1-D5`)**

- **D1 — Concurrency:** how would you make the "no overlap" invariant safe with two simultaneous booking requests on a real multi-node deployment with PostgreSQL? Name concrete primitives (transactions, isolation level, locks/unique constraints) and say why simple application-side checks fail.
- **D2 — Auth:** design authentication and authorization for this API (roles: `receptionist`, `doctor`, `admin`). Token format, lifetimes, and how each endpoint would gate roles. Sketch, do not implement.
- **D3 — Rate limiting:** strategy, algorithm choice (justify token bucket vs fixed window), scope (per API key? per IP?), and what headers the responses expose.
- **D4 — Persistence:** give a PostgreSQL schema sketch (tables, FKs, indexes) that supports this API and prevents double-booking at the DB level.
- **D5 — Failure mode:** describe one realistic silent-failure mode of *your own implementation above* (not the schema), and its mitigation.

---

## Output contract (do not deviate)

Respond with **exactly** these sections, in this order, using `##` headers, and nothing outside them:

```
## R1        … derivation …   Final Answer: <value>
… (R2–R10 in order)
## F1        one fenced ```html block with the complete index.html
## F1-NOTES  ≤ 150 words
## B1        one fenced ```javascript block with the complete api.js
## B1-D1 … ## B1-D5   (each ≤ 120 words)
```

Do not wrap sections in extra containers, do not merge sections, do not add a preamble.
