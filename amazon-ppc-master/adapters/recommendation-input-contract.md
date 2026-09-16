# Recommendation Input Contract

This contract defines the minimum evidence that must reach PPC decision skills before an action can be recommended.

## Required context

- US advertiser profile
- marketplace currency and timezone
- source report name
- reporting window
- report generation/freshness timestamp
- campaign / ad group / target identity where applicable
- campaign role: `exploration`, `testing`, or `harvesting` when known

## Required performance fields

At minimum, preserve available values for:

- impressions
- clicks
- spend
- orders
- sales
- CTR
- CPC
- CVR
- ACOS
- ROAS

## Comparative evidence

The preferred evidence package contains:

- recent 3-day window
- operating 14-day baseline
- 30-day context
- previous recommendation/action when available

## Recommendation confidence

Use:

- `low`: incomplete, sparse, or conflicting evidence
- `medium`: sufficient evidence for reversible optimization
- `high`: repeated evidence across the requested windows with clean data

`high` confidence is required before proposing destructive changes such as persistent negative targeting or pause, unless the term is clearly irrelevant.

## Exploration protection

Every recommendation must report:

- affected discovery path
- estimated discovery impact
- whether Auto/Broad/Phrase coverage changes
- whether the overall keyword pool shrinks

If a recommendation materially shrinks discovery capacity, require explicit rationale even when the efficiency metrics look favorable.
