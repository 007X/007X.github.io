# Dry Run Regression

## Purpose
Validate that the PPC runtime produces useful recommendations while avoiding destructive over-optimization.

## Required checks

### 1. Harvest detection
A converting search term with meaningful evidence should be classified as `harvest` or `test`, depending on evidence volume and existing coverage.

### 2. Test preservation
A relevant term with limited clicks/orders should not be classified as `suppress` solely because it has no orders yet.

### 3. High-ACOS protection
A term with high ACOS but historical or exploratory value must not be auto-paused or negatively targeted solely on ACOS.

### 4. Irrelevance suppression
A clearly irrelevant query can enter `suppress` review when evidence is strong enough and relevance is low.

### 5. Bid conservatism
Bid changes must be bounded and must include current bid, proposed bid, evidence window, rationale, risk, and `approval_required=true`.

### 6. Discovery capacity
The dry run must report discovery exposure before and after proposed actions. The system should flag any action set that materially shrinks Auto/Broad/Phrase discovery without explicit intent.

### 7. Duplicate protection
A candidate already captured by an equivalent keyword/target should not be blindly proposed again.

## Regression output

For each fixture run, record:

- harvest_count
- test_count
- observe_count
- suppress_review_count
- bid_reduce_count
- bid_hold_count
- bid_increase_count
- discovery_campaigns_preserved
- duplicate_candidates_blocked
- destructive_actions_blocked
- approval_queue_count

A regression run passes only when all safety checks are satisfied and no backend mutation occurs during Dry Run.