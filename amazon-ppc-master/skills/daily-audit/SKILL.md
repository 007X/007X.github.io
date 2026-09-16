# Daily Audit Skill

## Purpose
Run a conservative daily Amazon PPC health check for the US marketplace. Detect spend leakage, stalled delivery, budget constraints, and meaningful performance shifts while preserving keyword discovery.

## Inputs
Use the normalized data contract from `integrations/amazon-ads-mcp/data-contract.md`.

Required sources when available:
- Campaign report
- Keyword/target report
- Search term report
- Placement report

Preferred comparison windows:
- recent: 3 days
- operating baseline: 14 days
- context: 30 days

Do not make a suppression decision from a single anomalous day.

## Metrics
Calculate or validate:
- spend
- sales
- orders
- clicks
- impressions
- CTR = clicks / impressions
- CPC = spend / clicks
- CVR = orders / clicks
- ACOS = spend / sales
- ROAS = sales / spend
- spend per order = spend / orders

Preserve Amazon attribution-window semantics in raw fields. Do not silently reinterpret attribution windows.

## Audit Sequence
1. Verify profile, currency, timezone, and report freshness.
2. Check campaign delivery and obvious data-quality issues.
3. Identify budget-constrained campaigns.
4. Identify spend-heavy campaigns/targets with weak recent productivity.
5. Identify profitable or strategically important demand that may be underfunded.
6. Check discovery paths: Auto, Broad, and Phrase should remain represented unless there is documented structural waste.
7. Compare recent results with the 14-day baseline before recommending structural changes.
8. Route each finding to: observe, bid change, budget change, negative, pause, or scale.

## Decision Logic
### Spend leakage
Flag for investigation when spend is materially increasing without corresponding orders/sales improvement. Prefer a controlled bid reduction before keyword removal when the target still has exploration or historical value.

### Budget constraint
Flag when a campaign repeatedly hits its budget and has productive recent demand. Recommend budget expansion only when the evidence shows the campaign is constrained rather than simply consuming budget inefficiently.

### Underfunded productive demand
Flag stable converting demand with adequate efficiency that is repeatedly limited by budget or too-low bids. Recommend gradual scale, not abrupt expansion.

### Discovery health
Report whether the account still has active discovery traffic. Do not optimize all campaigns toward immediate ACOS if doing so would materially reduce search-term discovery.

## Output
Return:
1. Account summary
2. Top positive changes
3. Top risk findings
4. Discovery-health status
5. Recommended actions sorted by expected impact and evidence strength
6. Items requiring monitoring only
7. Execution queue

Every action must contain:
- action_type
- target identifier
- current value
- proposed value
- evidence window
- supporting metrics
- rationale
- expected effect
- risk
- approval_required=true

## Safety
This skill is recommendation-first. It must not mutate Amazon Ads backend state. Bid, budget, negative, pause, campaign creation, or other writes are emitted only as approval-gated recommendations.