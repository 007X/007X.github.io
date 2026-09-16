# Execution Gate

The PPC system has two phases.

## Phase 1 — Analyze

Return findings, evidence, recommended actions, and expected impact.

## Phase 2 — Execute

Only execute backend-changing actions after explicit human approval.

Every proposed mutation must include:

- `approval_required=true`
- action type
- target identifier
- current value
- proposed value
- evidence
- rationale
- risk

For v1, the default operating mode is Dry Run / recommendation mode.
