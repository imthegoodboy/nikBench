# scorecards/ — judge JSON outputs

One JSON per (judge × candidate) pair. Recommended naming:

```text
scorecards/judge-id__model-name.json
scorecards/gemini-3-pro__gpt-5.2.json
```

- Produced by pasting [`judging/judge.md`](../judging/judge.md) + the candidate's submission file into the judge model.
- Shape: [`templates/scorecard.json`](../templates/scorecard.json) — schema `nikbench.scorecard.v1`.
- The aggregator parses these, not the raw judge chat: `python scripts/aggregate.py scorecards -o leaderboard.md`
