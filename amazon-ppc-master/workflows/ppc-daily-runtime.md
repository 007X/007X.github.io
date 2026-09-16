# PPC Daily Runtime

## Goal
Run one controlled daily pass over a US Amazon Ads profile.

## Phase A — Context

1. Resolve the active `na` region.
2. Resolve the advertiser profile.
3. Capture profile currency and timezone.
4. Record the run timestamp and requested lookback windows.

## Phase B — Read

Collect, when available:

- campaign delivery and budgets
- Sponsored Products search-term report
- keyword/target performance
- placement performance

Preferred windows:

- 3d for recency
- 7d for search-term mining
- 14d for operating baseline
- 30d for context

## Phase C — Normalize

Convert raw report rows into the internal data contract. Preserve:

- profile_id
- report_id
- report_type
- date/window
- timezone
- currency
- campaign/ad group/entity identifiers
- attribution-window semantics
- data-quality flags

Stop analysis for a dataset if required fields are missing or report state is not terminal-success.

## Phase D — Analyze

Run in this sequence:

1. Daily Audit
2. Search Term Mining
3. Bid Optimizer
4. Budget Optimizer
5. Negative Keyword review
6. Scale / Shrink review
7. Profit / TACOS review when business-economics inputs exist

## Phase E — Merge

Normalize each recommendation into `config/opportunity-schema.md`.

De-duplicate by entity and action family. Do not silently merge conflicting recommendations; surface the conflict and preserve the evidence windows.

## Phase F — Protect exploration

Before finalizing actions, calculate the proposed discovery impact:

- discovery campaigns affected
- new search terms found
- new keyword/test candidates
- negative candidates
- paused targets
- estimated discovery traffic reduction

A proposed action that materially reduces discovery must be explicitly flagged for review.

## Phase G — Execution Gate

No backend write occurs in the analysis phase.

Every write candidate must include:

- action_type
- exact target id
- current value
- proposed value
- evidence window
- supporting metrics
- rationale
- expected effect
- risk
- reversibility
- `approval_required=true`

The queue is split into:

```text
APPROVAL REQUIRED
MONITOR ONLY
BLOCKED BY DATA QUALITY
```

## Phase H — Execute

Only explicitly approved actions may be sent to the write-capable MCP tools.

Execute small batches. Record the exact before/after state for each action.

## Phase I — Verify

After execution:

1. Re-read changed entities.
2. Confirm current state equals the approved proposed state.
3. Record failures individually.
4. Never mark an action successful because the request was merely submitted.

## Phase J — Learn

Persist the recommendation, approval, execution, and verification outcome so future audits can compare:

- predicted effect
- realized effect
- reversals
- false positives
- discovery impact

The system should become more conservative or more confident based on observed evidence, not on arbitrary fixed rules.
