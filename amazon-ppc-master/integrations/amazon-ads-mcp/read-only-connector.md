# Amazon Ads Read-only Connector Contract

## Purpose
Define the V1 connector boundary between the Amazon Ads MCP server and Amazon PPC Master without permitting backend mutations.

## Required capabilities
1. Resolve the active Amazon Ads region.
2. Resolve the active advertiser profile.
3. Read campaign inventory.
4. Read keyword/target inventory when available.
5. Create/poll/download Sponsored Products reporting jobs.
6. Pass report metadata and raw records to the Adapter layer.

## Explicitly prohibited in V1
- Bid updates
- Budget updates
- Keyword creation
- Negative keyword creation
- Target pause/archive
- Campaign creation/editing
- Any other write/mutation operation

## Request envelope
```json
{
  "mode": "READ_ONLY",
  "marketplace": "US",
  "region": "na",
  "profile_id": "<runtime-resolved>",
  "reporting_window": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "sources": ["campaign", "target", "search_term", "placement"]
}
```

## Response envelope
Every connector response must carry:
- `mode=READ_ONLY`
- source capability used
- profile identifier (runtime only; do not persist secrets)
- request timestamp
- source report identifier when applicable
- report status
- raw payload reference or records
- `data_quality` flags
- adapter version

## Report state machine
```text
REQUESTED
  ↓
CREATED
  ↓
PROCESSING
  ├── RETRYABLE_ERROR → POLL_AGAIN
  ├── FAILED → STOP + DIAGNOSTIC
  └── SUCCESS
        ↓
      DOWNLOAD
        ↓
      VALIDATE
        ↓
      NORMALIZE
```

## Read-only smoke test
Run in this order:
1. Resolve `region=na`.
2. Resolve active US advertiser profile.
3. Read campaign list.
4. Read targets/keywords if available.
5. Create a small Sponsored Products Search Term Report window.
6. Poll until terminal status.
7. Download and validate the report.
8. Normalize into the canonical record contract.
9. Run `runtime/dry_run.py`.
10. Confirm zero backend mutations.

## Failure handling
- Authentication failure: stop; do not retry writes or alter configuration automatically.
- Rate limit / temporary service failure: bounded retry with backoff.
- Report failure: preserve diagnostic metadata and stop the downstream analysis for that source.
- Missing required columns: mark `schema_mismatch` and do not fabricate fields.
- Stale report: mark `stale` and lower recommendation confidence.
- Partial data: continue only with explicit `partial_data=true` and confidence reduction.

## Audit requirements
Log connector operation, timestamp, source capability, request scope, result status, retry count, and adapter version. Do not log client secrets, access tokens, refresh tokens, or other credentials.

## Security boundary
Credentials live only on the MCP host / secret manager. The Skill repository contains schemas, rules, fixtures, and connector contracts—not live credentials.