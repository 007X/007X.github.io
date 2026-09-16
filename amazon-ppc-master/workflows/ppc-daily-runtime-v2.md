# PPC Daily Runtime v2

## Goal
Run a repeatable daily read -> analyze -> recommend workflow against a US Amazon Ads profile without changing backend state until the user explicitly approves actions.

## 0. Preconditions

- MCP server reachable over HTTP.
- US region selected (`na`).
- Active advertiser profile selected.
- Profile currency and timezone confirmed.
- Required report packages enabled.
- No real credentials stored in the Skill repository.

## 1. Identity check

Collect profile, region, currency, and timezone.

Stop on authentication or profile errors.

## 2. Inventory check

Read campaign inventory and delivery/budget state.

Do not mutate.

## 3. Reporting

Generate or retrieve:
- Sponsored Products search term report
- campaign report
- keyword/target report
- placement report

Prefer a common evidence window of 14 days plus 3-day recent context and 30-day stability context.

For asynchronous reports:

```text
CREATE -> POLL -> COMPLETE -> DOWNLOAD -> VALIDATE -> NORMALIZE
```

Retry only transient failures with bounded attempts. Do not retry invalid request/schema failures blindly.

## 4. Normalize

Convert source records to the internal Data Contract. Preserve raw attribution-window fields, source report name, reporting window, generated timestamp, timezone, and currency.

Flag:
- partial data
- stale data
- missing metrics
- duplicated rows
- attribution ambiguity
- schema mismatch

## 5. Analyze

Run in this order:

```text
Daily Audit
  -> Search Term Mining
  -> Bid Optimizer
  -> Budget Optimizer
  -> Negative Keyword
  -> Scale/Shrink
  -> Profit/TACOS
```

Each Skill returns recommendations, not writes.

## 6. Merge

Merge into the Unified Recommendation Queue. Resolve conflicts by combining evidence and routing incompatible actions to review.

## 7. Discovery protection

Before any suppression action is surfaced for approval, calculate discovery impact:
- affected Auto/Broad/Phrase paths
- discovery spend affected
- new candidates generated
- new tests proposed
- negatives proposed
- targets proposed for pause

Do not let local efficiency actions silently eliminate the account's discovery layer.

## 8. Approval gate

Only backend-changing recommendations enter the approval surface.

Required fields:
- recommendation_id
- action_type
- target_type
- target_id
- current_state
- proposed_state
- evidence_window
- metrics
- rationale
- expected_effect
- risk
- reversibility
- discovery_impact
- approval_required=true

## 9. Execute approved actions

Execute only the exact actions explicitly approved by the user.

Never infer approval from context, previous approval of a different target, or a general statement such as "optimize the account".

## 10. Verify

After execution:
- re-read affected objects
- verify the proposed state matches backend state
- record execution timestamp
- record result or error
- retain old/new values

## 11. Learn

Write a compact decision log containing:
- what changed
- why it changed
- evidence window
- expected effect
- observed verification result
- follow-up review date/window

The log is for future analysis and must not contain secrets.

## Failure states

### AUTH_ERROR
Stop. Ask for credential/authorization repair.

### PROFILE_ERROR
Stop until a valid active profile is selected.

### REPORT_ERROR
Retry only when transient; otherwise surface the exact validation failure.

### DATA_ERROR
Stop downstream decisions that depend on the affected dataset.

### SCHEMA_ERROR
Stop and update the adapter/data contract rather than guessing field semantics.

### EXECUTION_ERROR
Do not partially repeat the queue automatically. Verify actual backend state first, then reconcile.

## Operating mode

V2 remains dry-run/recommendation-first by default. Automatic writes are not enabled by this runtime document.
