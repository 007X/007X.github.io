# Recommendation Schema

All PPC Skills should emit recommendations using the same logical structure so the Execution Gate can review them consistently.

## Required Fields

```yaml
recommendation_id: stable-unique-id
action_type: keyword_add | bid_change | budget_change | negative_keyword | pause | scale | observe
scope:
  profile_id: string
  campaign_id: string|null
  ad_group_id: string|null
  target_id: string|null
  keyword_id: string|null
  search_term: string|null
current_value: number|string|null
proposed_value: number|string|null
evidence_window: 7d | 14d | 30d | multi-window
metrics:
  impressions: number|null
  clicks: number|null
  spend: number|null
  orders: number|null
  sales: number|null
  ctr: number|null
  cpc: number|null
  cvr: number|null
  acos: number|null
  roas: number|null
classification: harvest | test | observe | suppress | scale | protect
rationale: string
expected_effect: string
risk: low | medium | high
confidence: low | medium | high
approval_required: true
```

## Evidence Rules

- Always state the evidence window.
- Prefer multi-window evidence for suppression, pause, or structural changes.
- Do not treat missing values as zero.
- Preserve Amazon attribution-window semantics from raw reports.
- When profit/margin data is unavailable, explicitly say that the recommendation is revenue/advertising-efficiency based rather than profit-validated.

## Priority

Recommendations should be ordered by:

1. material risk or spend leakage
2. high-confidence profitable expansion
3. budget-constrained productive demand
4. controlled tests and exploration opportunities
5. monitoring-only items

Priority is an execution-review order, not a quality ranking of campaigns or keywords.

## Execution Boundary

The schema is advisory. A recommendation cannot be executed unless the user explicitly approves the proposed backend action. Approval must apply to the exact target and proposed value at review time; stale recommendations must be revalidated before execution.
