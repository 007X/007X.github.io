# Search Term -> Recommendation Pipeline

## Objective
Turn Search Term Report rows into traceable keyword-growth and spend-control recommendations while protecting discovery capacity.

## Stage A: Candidate preparation

For each search term, preserve:
- date range
- profile
- campaign and ad group
- search term
- source match type / targeting context
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
- attribution window

Join against current keyword/target coverage before proposing a new target.

## Stage B: Classification

Classify every meaningful candidate into exactly one primary state:

### HARVEST
Use when conversion evidence is repeatable or commercial intent is strong and the term is not already intentionally captured.

Typical recommendation:
- add controlled exact/phrase coverage
- preserve source discovery traffic
- avoid unnecessary duplication across campaigns

### TEST
Use when the signal is promising but evidence is insufficient for full harvesting.

Typical recommendation:
- add a controlled test
- conservative initial bid
- explicit review window

### OBSERVE
Use when the signal is interesting but incomplete.

Typical recommendation:
- no backend change
- keep discovery path active
- revisit after additional evidence

### SUPPRESS
Use only for clearly irrelevant or repeatedly destructive terms with sufficient evidence.

Typical recommendation:
- negative or pause candidate
- include stronger evidence requirement than bid reduction
- state discovery impact

## Stage C: Bid interaction

A search term recommendation must consider the current source bid/target context.

Prefer:
1. lower source bid when spend is inefficient but relevance remains;
2. test a dedicated keyword when the query demonstrates demand;
3. scale a proven term only when delivery/capacity is the limiting factor;
4. suppress only when evidence supports removing traffic.

## Stage D: Opportunity object

Each candidate becomes an Opportunity object with:
- `opportunity_id`
- `classification`
- `search_term`
- `source_campaign_id`
- `source_ad_group_id`
- `coverage_status`
- `current_state`
- `proposed_state`
- `proposed_match_type`
- `current_bid`
- `proposed_bid`
- `evidence_window`
- `metrics`
- `confidence`
- `rationale`
- `expected_effect`
- `risk`
- `reversibility`
- `discovery_impact`
- `approval_required=true`

## Stage E: De-duplication

Before a new keyword recommendation is produced:
1. inspect existing exact/phrase/broad coverage;
2. detect duplicate target structures;
3. prefer attaching the recommendation to the most appropriate existing structure when possible;
4. record the conflict rather than silently creating another target.

## Stage F: Ranking

Sort recommendations by evidence strength and expected business impact, not by ACOS alone.

Suggested order:
1. high-confidence productive harvests
2. high-confidence efficiency repairs
3. promising controlled tests
4. monitoring opportunities
5. suppression candidates requiring explicit review

Never use a ranking as a substitute for the Execution Gate.

## Stage G: Output

Return four blocks:

### Harvest queue
New proven-demand candidates.

### Test queue
Promising but still experimental candidates.

### Control queue
Bid/budget efficiency actions.

### Review queue
Negative/pause candidates and ambiguous cases.

All backend changes remain recommendation-only until explicit approval.
