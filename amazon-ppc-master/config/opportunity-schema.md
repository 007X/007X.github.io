# PPC Opportunity Schema

All analysis modules should describe opportunities with the same logical fields.

## Required fields

```yaml
opportunity_id: stable id
source: daily_audit | search_term_mining | bid_optimizer | budget_optimizer | negative_keyword | scale_shrink | profit_tacos
profile_id: Amazon Ads profile identifier
entity_type: campaign | ad_group | keyword | target | search_term | placement
entity_id: source entity identifier
classification: harvest | test | observe | suppress | reduce_bid | hold | increase_bid | budget_change | scale | shrink
confidence: low | medium | high
evidence_window: 3d | 7d | 14d | 30d | custom
metrics: {}
current_state: {}
proposed_state: {}
rationale: explanation
expected_effect: explanation
risk: low | medium | high
reversibility: easy | moderate | hard
approval_required: true
```

## Required metric discipline

Never fabricate missing metrics. Preserve raw Amazon attribution-window fields exactly enough to identify the source window. Derived metrics must identify their denominator and source window.

Recommended derived fields:

- ctr = clicks / impressions
- cpc = spend / clicks
- cvr = orders / clicks
- acos = spend / sales
- roas = sales / spend
- spend_per_order = spend / orders
- budget_utilization = spend / budget when comparable

Return null when the denominator is zero or unavailable.

## Action ordering

When several opportunities affect the same entity, resolve them in this order:

1. data-quality block
2. safety/compliance block
3. suppression only when strong evidence exists
4. bid control
5. budget control
6. expansion/test
7. scale

This ordering is a decision aid, not a permission to mutate the account. Every write remains approval-gated.

## Conflict resolution

Prefer the recommendation with stronger evidence and lower irreversible risk. When recommendations disagree across windows, surface the conflict rather than averaging it away.

Example:

- 3d suggests reduce bid
- 30d shows strong profitable history

The combined output should normally be an evidence-qualified controlled bid test, not an automatic pause.
