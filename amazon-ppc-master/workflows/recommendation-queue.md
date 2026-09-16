# Unified Recommendation Queue

## Purpose
Merge outputs from Daily Audit, Search Term Mining, Bid Optimizer, Budget Optimizer, Negative Keyword, Scale/Shrink, and Profit/TACOS into one approval surface.

## Required fields

Every row must contain:

| Field | Meaning |
|---|---|
| `recommendation_id` | Stable ID for this recommendation |
| `skill` | Producing Skill |
| `action_type` | observe / bid / budget / keyword / negative / pause / scale |
| `target_type` | campaign / ad_group / keyword / target / search_term / placement |
| `target_id` | Amazon object identifier when available |
| `current_state` | Current backend state |
| `proposed_state` | Exact proposed change |
| `evidence_window` | Data window supporting the recommendation |
| `metrics` | Relevant measured values |
| `confidence` | Evidence strength, not outcome certainty |
| `rationale` | Why this action is proposed |
| `expected_effect` | Expected directional impact |
| `risk` | Main downside |
| `reversibility` | easy / moderate / difficult |
| `discovery_impact` | effect on exploration capacity |
| `approval_required` | Always `true` for backend changes |

## Conflict resolution

When two Skills propose changes to the same object:

1. merge evidence;
2. preserve both rationales;
3. detect incompatible proposed states;
4. prefer the less destructive reversible action when evidence is incomplete;
5. route the conflict to human review rather than auto-resolving by guesswork.

## Action precedence

Default precedence for spend-control decisions:

`observe -> bid control -> budget control -> structural test -> negative/pause`

For proven productive demand:

`observe -> controlled scale -> budget support -> bid/placement expansion`

This is a workflow ordering, not a performance ranking.

## Discovery guardrail

Before publishing the queue, calculate:
- number of discovery campaigns affected
- number of Auto/Broad/Phrase paths affected
- new search-term candidates
- new test candidates
- negative candidates
- paused targets
- expected change in discovery spend

If proposed suppressions materially reduce discovery capacity, mark the queue for review even when individual suppressions have reasonable local metrics.

## Output views

The runtime should support four views:

### Executive view
Top business issues, opportunities, and risks.

### Operator view
Exact object IDs, current values, proposed values, evidence, and rationale.

### Discovery view
New terms, tests, source campaigns, and coverage gaps.

### Approval view
Only backend-changing actions, grouped by campaign and ordered by reversibility and evidence strength.

## No-write guarantee

This queue is a decision artifact. Creating it never mutates Amazon Ads.
