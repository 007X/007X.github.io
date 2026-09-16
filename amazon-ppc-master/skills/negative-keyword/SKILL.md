# Negative Keyword Skill

## Purpose
Suppress clearly irrelevant or persistently destructive search demand while minimizing false negatives and protecting exploration.

## Inputs
- Search Term Report
- Search term, targeting keyword, match type
- Impressions, clicks, spend, orders, sales
- CTR, CPC, CVR, ACOS/ROAS
- 7d / 14d / 30d trend
- Product/catalog relevance when available
- Campaign role and discovery value

## Decision Rules
1. Negative exact/phrase actions require stronger evidence than bid reduction.
2. Clearly irrelevant queries may be suppressed even with limited performance history when semantic irrelevance is strong.
3. High ACOS alone is not sufficient for a negative decision.
4. A query with spend but no orders must be evaluated against click volume, CPC, relevance, historical performance, and attribution lag.
5. Converting search terms should normally be candidates for harvesting rather than negatives.
6. Protect Auto/Broad/Phrase discovery when the observed query is relevant and evidence of waste is incomplete.
7. When evidence is insufficient, prefer lower bid / controlled test / observation.
8. Avoid duplicative negatives that block useful future discovery unless the blocking intent is explicit.

## Output
For each candidate:
- search_term
- source campaign/ad group
- current targeting context
- proposed negative type: none / negative exact / negative phrase
- supporting metrics and windows
- relevance assessment
- reason
- risk of blocking useful demand
- confidence
- `approval_required=true`

## Safety
No negative keyword, ad-group, campaign pause, or targeting deletion is executed automatically. All suppression recommendations pass through the Execution Gate.