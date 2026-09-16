# Bid Optimizer Skill

## Purpose
Recommend conservative Amazon PPC bid changes that reduce inefficient spend while preserving useful exploration and proven demand.

## Inputs
Required when available:
- keyword/target report
- search term report
- placement report
- campaign budget/delivery context

Use recent 3-day performance, compare to 14-day baseline, and use 30-day context for stability. Do not overreact to one-day anomalies.

## Core Principle
Change bids before deleting traffic when the traffic may still have discovery, historical, or strategic value.

## Decision Factors
Evaluate:
- ACOS and ROAS
- orders and sales
- spend and spend velocity
- clicks and CPC
- CVR
- CTR
- trend vs 14-day baseline
- target/match type
- placement
- campaign role: discovery vs harvesting
- budget constraint
- relevance and strategic importance

## Bid Actions
### Reduce bid
Use when spend is inefficient but the target still has relevant traffic, historical value, or insufficient evidence for suppression.

Default v1 change: make a small controlled reduction rather than a large step. Use the current bid as the anchor and state the exact proposed value.

### Hold
Use when evidence is insufficient, performance is stable, or the target is important to discovery.

### Increase bid
Use when a target has repeatable productive outcomes, adequate conversion evidence, and is limited by rank/delivery rather than by budget inefficiency.

### Placement adjustment
Recommend only when placement-level evidence shows a distinct and repeatable opportunity and the campaign structure supports it.

## High-ACOS Protection
Never reduce a bid solely because ACOS is above target. Before recommending suppression, evaluate spend, clicks, orders, sales, conversion trend, match type, campaign role, and historical performance.

A high-ACOS exploratory target may receive a bid reduction and continued observation rather than removal.

## Exploration Preservation
Maintain meaningful spend for Auto/Broad/Phrase discovery. Avoid bid changes that would effectively shut down the discovery layer across the account.

The default account-level allocation reference is:
- 40% exploration
- 30% new keyword testing
- 30% profitable harvesting

Treat these as starting guidelines, not fixed quotas.

## Proposed Bid Method
When data is sufficient, estimate an efficiency-guided bid using observed conversion and target efficiency, then constrain the result by a conservative change limit. The recommendation must show:
- current bid
- reference efficiency
- target efficiency if supplied
- suggested bid
- change percentage
- evidence window

Do not invent a target ACOS when none is provided. Prefer user/account targets from configuration or supplied business economics.

## Output
Return:
1. Reduce-bid candidates
2. Hold candidates
3. Increase-bid candidates
4. Placement candidates
5. Discovery-protection notes
6. Execution queue

Every action must contain:
- action_type
- target identifier
- current bid
- proposed bid
- evidence window
- supporting metrics
- rationale
- expected effect
- risk
- approval_required=true

## Safety
This skill is recommendation-only. No bid, budget, negative, pause, or campaign mutation is executed without explicit approval through the Execution Gate.