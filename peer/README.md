# peer/ — peer-review & self-assessment outputs (v1.1 round)

One file per candidate-turned-reviewer, written **after** all blind-phase submissions exist:

```text
peer/nemotron-3.5-super-vl-free.md   ← a rating TABLE of every submission + its own row LAST (self)
peer/beam-free.md
...
```

- Produced by giving the model [`judging/peer-review.md`](../judging/peer-review.md) in a fresh chat; from that moment it may read everything in [`submissions/`](../submissions/).
- Each file ends with a machine-read `nikbench.peer.v1` JSON block — the aggregation script parses that block:
  `python scripts/aggregate.py scorecards --peer-dir peer -o leaderboard.md`

## Final-score blend

| Signal | Source | Weight |
|---|---|---:|
| **NBS** | calibrated rubric judges (median) | 0.6 |
| **Peer** | other models' ratings of this candidate | 0.2 |
| **Self** | the candidate's own last-row rating | 0.2 |

Self-inflated ratings are easy to detect (they sit next to peer votes in the same table) — honesty is part of what's being graded in ~10 of the board.
