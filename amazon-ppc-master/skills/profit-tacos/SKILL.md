# Profit / TACOS Planner Skill

## Purpose
Evaluate PPC decisions against business economics instead of optimizing ACOS in isolation.

## Inputs
- Ad spend, attributed sales, orders
- Organic / total sales when available
- Gross margin or contribution margin assumptions when provided
- Fees, COGS, fulfillment and other cost inputs when available
- 7d / 14d / 30d trend
- Campaign / target role
- Exploration vs harvesting allocation

## Metrics
Prefer, when the required inputs exist:
- ACOS = ad spend / attributed ad sales
- ROAS = attributed ad sales / ad spend
- TACOS = ad spend / total sales
- Ad spend as % of contribution margin
- Break-even ACOS derived from the user's economics

Do not invent margin assumptions. If profit inputs are missing, state that profit conclusions are limited and keep the analysis at spend/sales efficiency level.

## Decision Rules
1. Do not treat lower ACOS as universally better when growth or discovery objectives matter.
2. Protect campaigns that generate strategically valuable demand even if short-term ACOS is above a target, provided economics and role justify continued testing.
3. Flag cases where ad sales rise but total-sales economics do not improve.
4. Distinguish harvesting efficiency from exploration investment.
5. Recommend bounded bid/budget changes before structural suppression when evidence is incomplete.

## Output
Return:
- current efficiency metrics
- profit/economic assumptions used
- target / campaign / portfolio issue
- recommended action
- expected economic effect
- uncertainty / missing data
- confidence
- `approval_required=true`

## Safety
This Skill only produces analysis and recommendations. It does not modify campaigns or keywords directly.