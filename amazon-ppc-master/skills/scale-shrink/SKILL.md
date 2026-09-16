# Scale / Shrink Planner Skill

## Purpose
Scale productive demand gradually while reducing inefficient traffic without collapsing the account's keyword discovery surface.

## Inputs
- Campaign, ad group, target/keyword and search term performance
- 3d / 7d / 14d / 30d trend
- Spend, orders, sales, ACOS, ROAS, CVR, CPC
- Budget utilization and placement performance
- Discovery vs harvesting role
- Historical changes and recent bid/budget actions

## Scale Rules
1. Scale only when productive performance is supported by enough recent evidence.
2. Prefer incremental bid or budget changes over abrupt jumps.
3. Protect proven converting terms from unnecessary suppression.
4. Separate scaling of proven demand from expansion into unproven demand.
5. When scaling, check whether additional spend is available without starving exploration campaigns.

## Shrink Rules
1. Shrink inefficient traffic primarily through bid or budget controls first.
2. Do not shrink the keyword pool merely because a target has temporarily high ACOS.
3. Stronger suppression requires stronger evidence: persistent waste, clear irrelevance, or deliberate strategic exclusion.
4. Compare recent and longer windows before shrinking an established target.
5. Never optimize all campaigns toward the same short-term ACOS objective if doing so removes discovery capacity.

## Output
Return action candidates grouped as:
- SCALE
- HOLD
- CONTROL
- SUPPRESS

Each recommendation includes target, current value, proposed value, evidence windows, rationale, expected effect, risk, confidence, and `approval_required=true`.

## Safety
This Skill does not execute backend mutations. It prepares bounded actions for the Execution Gate.