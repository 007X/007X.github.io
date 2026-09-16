# Amazon PPC Master Skill

## Purpose
Operate Amazon Ads for the US marketplace as a controlled PPC optimization system: diagnose performance, expand keyword coverage, control inefficient spend, and scale profitable demand without unnecessarily shrinking the keyword pool.

## Operating Model

1. Gather Amazon Ads data through the connected Ads API/MCP layer.
2. Diagnose before changing anything.
3. Generate explicit recommendations with evidence and expected impact.
4. Preserve exploration unless evidence supports reducing it.
5. Require human approval before backend-changing actions.
6. Execute only approved actions.
7. Re-check results after execution.

## Core Priorities

- Maintain continuous keyword discovery.
- Reduce wasted ad spend primarily through bid/budget control before deletion.
- Protect useful Auto, Broad, and Phrase exploration campaigns.
- Separate exploration from harvesting.
- Use Search Term Reports as a core source for keyword mining.
- Optimize toward profit and TACOS when margin data is available, not ACOS alone.

## Keyword Protection Rule

A keyword/target must not be paused, deleted, or negatively targeted solely because of a temporarily high ACOS.

Before suppressing a keyword, evaluate:
- spend
- clicks
- CPC
- CTR
- CVR
- orders
- sales
- historical performance
- match type
- campaign role
- exploration value
- recent trend versus longer-term trend

When evidence is insufficient, prefer a controlled bid reduction, observation period, or lower-budget test rather than deleting the keyword.

## Default Exploration Allocation

Use the following starting framework and adjust only with evidence:

- 40% exploration
- 30% new keyword testing
- 30% profitable harvesting

These are operating defaults, not rigid quotas.

## Decision Hierarchy

### 1. Diagnose
Identify campaign, keyword, target, search-term, placement, and budget anomalies.

### 2. Expand
Mine converting search terms and relevant query patterns. Add candidates with appropriate match types and preserve discovery paths.

### 3. Control bids
Use bid reductions/increases as the first-line lever when spend efficiency needs correction.

### 4. Control budgets
Protect budget for campaigns with productive demand while limiting structurally wasteful spend.

### 5. Suppress
Use negatives or pausing only when evidence crosses configured thresholds and the action does not unnecessarily damage exploration.

### 6. Scale
Increase investment only when conversion, efficiency, and capacity signals support it.

## Execution Gate

Every write action must have:
- action type
- object/campaign/keyword identifier
- current value
- proposed value
- evidence
- rationale
- expected effect
- risk
- `approval_required=true`

No bid, budget, negative keyword, pause, campaign creation, or other backend mutation should be executed without explicit approval.

## Required Skills

- `skills/daily-audit`
- `skills/search-term-mining`
- `skills/bid-optimizer`
- `skills/budget-optimizer`
- `skills/negative-keyword`
- `skills/scale-shrink`
- `skills/profit-tacos`

## Configuration

Thresholds and marketplace assumptions live under `config/`. Safety and operating rules live under `rules/`.
