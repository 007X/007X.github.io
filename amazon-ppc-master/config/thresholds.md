# PPC Thresholds

Thresholds are intentionally conservative in v1. Tune them after observing the account's baseline.

## Evidence Minimums

- Do not make suppression decisions from a single anomalous day.
- Require enough clicks/spend/orders for the action type before treating a signal as stable.
- Compare recent performance with a longer lookback when available.

## Bid Control

Prioritize bid adjustment over keyword deletion when spend is inefficient but the keyword still has exploration or historical value.

## Budget Control

Consider budget changes when a campaign is repeatedly budget-constrained or repeatedly consuming budget without productive outcomes. Avoid reallocating based only on short-term volatility.

## Negative / Pause

Use stronger evidence for negatives and pauses than for bid reductions. Preserve discovery paths unless the query/target is clearly irrelevant or persistently destructive to efficiency.
