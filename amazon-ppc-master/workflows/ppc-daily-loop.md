# PPC Daily Loop

This workflow defines the default daily runtime for Amazon PPC Master.

## 1. Ingest

Pull fresh US advertiser-profile data through Amazon Ads MCP.

Minimum inputs:
- Campaign report
- Keyword/target report
- Sponsored Products search-term report
- Placement report when available
- Existing keyword/target inventory
- Budget and delivery state
- Profit/margin inputs when available

Validate profile, currency, timezone, report freshness, and attribution-window semantics before analysis.

## 2. Audit

Run `skills/daily-audit` using 3d recent, 14d baseline, and 30d context.

Produce:
- account summary
- positive changes
- risk findings
- discovery-health status
- monitoring items
- recommendation queue

## 3. Mine

Run `skills/search-term-mining`.

For each meaningful search term:
1. Check relevance.
2. Check existing keyword/target coverage.
3. Classify as harvest, test, observe, or suppress.
4. Preserve source campaign/ad group for traceability.
5. Estimate whether the recommendation expands, preserves, or reduces discovery capacity.

A mining cycle must not silently produce a net contraction of discovery traffic. Any large suppression wave is surfaced for review.

## 4. Optimize Bids

Run `skills/bid-optimizer`.

Prefer:
- small bid changes
- evidence across multiple windows
- stronger action only when evidence is stronger
- bid control before deletion when exploration value exists

## 5. Optimize Budgets

Run `skills/budget-optimizer`.

Protect budget for productive constrained campaigns while avoiding increases that simply fund inefficient traffic.

## 6. Profit Check

Run `skills/profit-tacos` when margin, COGS, fees, or TACOS inputs are available.

When those economics are unavailable, label recommendations as advertising-efficiency based rather than profit-validated.

## 7. Execution Gate

Combine recommendations into one queue using `config/recommendation-schema.md`.

For each write action require:
- exact target
- current value
- proposed value
- evidence window
- metrics
- rationale
- expected effect
- risk
- confidence
- `approval_required=true`

No backend mutation is permitted before explicit user approval.

## 8. Execute

After approval, execute only the approved actions. Do not expand scope during execution.

## 9. Verify

Re-read the affected entities and confirm the new state. Record:
- action status
- resulting value
- timestamp
- any API error
- whether the change matched the approved action

## 10. Learn

Compare the next reporting window against the pre-change baseline. Use observed impact to tune thresholds rather than making aggressive changes from isolated outcomes.
