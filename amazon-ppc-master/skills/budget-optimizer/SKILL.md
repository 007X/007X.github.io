# Budget Optimizer Skill

## Purpose
Optimize campaign budgets without starving keyword discovery or allowing repeated unproductive spend to consume the account budget.

## Inputs
- Campaign-level spend, sales, orders, ACOS/ROAS
- Daily budget and budget utilization
- Budget-constrained status when available
- 7d / 14d / 30d performance
- Exploration vs harvesting campaign role
- Placement and targeting mix when available

## Decision Rules
1. Budget changes require repeated evidence, not a single high-spend day.
2. A campaign that is repeatedly budget constrained and productive may justify a budget increase.
3. A campaign that repeatedly consumes budget with weak outcomes may justify a budget decrease, but first inspect bids and targeting mix.
4. Protect discovery campaigns from being starved solely because their short-term ACOS is higher than harvesting campaigns.
5. Do not transfer budget merely to improve blended ACOS if doing so materially reduces exploration capacity.
6. Prefer bid controls for target-level inefficiency; use budget controls for campaign-level allocation problems.
7. When evidence is mixed, recommend observation or a bounded budget test instead of a large change.

## Output
For every recommendation return:
- campaign_id / campaign name
- current budget
- proposed budget
- 7d / 14d / 30d evidence
- budget utilization evidence
- campaign role
- rationale
- expected effect
- risk to exploration
- confidence
- `approval_required=true`

## Safety
No budget mutation is executed by this Skill. It produces an approval-ready recommendation for the Execution Gate.