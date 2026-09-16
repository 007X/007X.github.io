# Search Term Mining Skill

## Purpose
Continuously expand the keyword pool from Amazon Ads search-term performance without turning exploration into an uncontrolled source of waste.

## Inputs
Primary source:
- Sponsored Products Search Term Report

Supporting sources when available:
- keyword/target report
- campaign report
- product conversion data
- profit or margin data

Use 7-day and 14-day windows, with 30-day context. Preserve attribution-window semantics.

## Classification
Classify search terms into:

### Harvest
Evidence of repeatable conversion or strong commercial intent. Recommend moving proven demand into an intentional keyword/target structure when it is not already captured.

### Test
Promising term with insufficient evidence for full harvesting. Recommend controlled testing using an appropriate match type and conservative starting bid.

### Observe
Interesting term with weak or incomplete evidence. Keep discovery active and avoid premature suppression.

### Suppress
Only when the term is clearly irrelevant, structurally destructive, or supported by strong repeated evidence of waste. A high ACOS number alone is insufficient.

## Candidate Signals
Consider:
- orders
- sales
- spend
- clicks
- CPC
- CVR
- ACOS
- ROAS
- CTR
- recurrence across multiple days
- recurrence across campaigns/ad groups
- commercial relevance
- query-to-product relevance
- match-type source
- recent vs baseline performance

A term can qualify for testing before it qualifies for harvesting.

## Expansion Rules
1. Preserve Auto/Broad/Phrase discovery paths.
2. Prefer exact or phrase harvesting for proven demand when strategically appropriate.
3. Do not duplicate a term blindly across overlapping campaigns; inspect existing coverage first.
4. When a term is promising but unproven, use a lower-risk test rather than a full-scale launch.
5. When mining from broad/auto traffic, keep the source campaign/ad group in the recommendation for traceability.
6. Track rejected candidates so the same search term is not repeatedly proposed without new evidence.

## Anti-Shrink Rule
Search-term mining must never reduce the overall discovery pool merely to improve a short-term ACOS snapshot. Any negative or pause recommendation needs stronger evidence than a normal bid recommendation.

## Output
Return:
1. New harvest candidates
2. New test candidates
3. Observe candidates
4. Suppression candidates, with evidence threshold explicitly stated
5. Existing coverage conflicts or duplicates
6. Estimated opportunity and risk
7. Execution queue

Each candidate recommendation should include:
- search_term
- source campaign/ad group
- current targeting status
- proposed match type
- proposed initial bid or action
- evidence window
- spend/click/order/sales metrics
- rationale
- expected effect
- risk
- approval_required=true

## Safety
No keyword creation, negative targeting, bid change, pause, or campaign mutation is executed by this skill. It only returns structured recommendations for the Execution Gate.