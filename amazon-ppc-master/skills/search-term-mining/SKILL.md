# Search Term Mining Skill

## Purpose
Continuously expand useful keyword coverage from Amazon Ads search-term data while controlling inefficient spend without causing unnecessary keyword-pool shrinkage.

## Inputs
Use the normalized data contract from `integrations/amazon-ads-mcp/data-contract.md`.

Required when available:
- Search Term Report
- Campaign / ad group context
- Existing keyword / target inventory
- Match type
- Recent and longer-term performance

Preferred windows:
- discovery signal: 7 days
- operating validation: 14 days
- context: 30 days

## Candidate Classes
Classify every meaningful search term into one of four states:

### Harvest
The query has credible conversion evidence and is sufficiently relevant to become a structured keyword/target candidate in an appropriate harvesting campaign.

### Test
The query is relevant and promising but has limited evidence. Preserve it as an exploration candidate; do not treat limited data as a failure.

### Observe
The query has mixed, weak, or immature evidence. Continue gathering data unless spend is clearly destructive or relevance is poor.

### Suppress
Use only when the query is clearly irrelevant, structurally harmful, or has accumulated strong negative evidence. High ACOS alone is insufficient.

## Mining Logic
1. Normalize search terms and preserve exact source evidence.
2. Check whether the term is already represented in exact/phrase/broad or another target form.
3. Detect converting terms that are not adequately represented in the keyword structure.
4. Detect high-intent query patterns that deserve testing even before conversion proof is complete.
5. Estimate incremental opportunity without assuming every successful query should be isolated immediately.
6. Protect Auto/Broad/Phrase discovery paths from premature suppression.
7. Deduplicate recommendations across campaigns and match types.
8. Prefer controlled testing over removal when evidence is incomplete.

## Spend Protection
For non-converting terms, compare spend against configurable thresholds and conversion history. A term that is still exploratory should normally receive a bid/budget control recommendation before a negative recommendation.

Do not create negatives solely because:
- ACOS is temporarily high
- one day is weak
- click count is low
- the term has not yet accumulated sufficient evidence

## Keyword-Pool Preservation
Track:
- new search terms discovered
- new keyword candidates
- existing discovery coverage
- negatives added
- targets paused

A mining cycle should report the net change in discovery capacity. If suppression materially outpaces useful expansion, flag the cycle for review rather than silently proceeding.

## Output
Return a ranked opportunity table and an approval queue.

Each opportunity should contain:
- search_term
- campaign_id
- ad_group_id
- source_match_type
- existing_target_status
- classification: harvest | test | observe | suppress
- spend
- clicks
- orders
- sales
- CTR
- CPC
- CVR
- ACOS
- evidence_window
- recommendation
- proposed_match_type
- proposed_bid_if_applicable
- rationale
- confidence
- approval_required=true

For suppress recommendations, include the exact negative target form and stronger evidence than for bid reductions.

## Safety
This skill only recommends additions, bid changes, negatives, pauses, or campaign moves. It must not mutate Amazon Ads backend state. All changes pass through the Execution Gate.