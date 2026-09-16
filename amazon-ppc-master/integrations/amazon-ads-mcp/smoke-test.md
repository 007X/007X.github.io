# Amazon Ads MCP Smoke Test

## Goal
Prove that the US advertiser profile can be read and that a Sponsored Products Search Term Report can flow into the PPC Master Dry Run without any backend mutation.

## Preconditions
- MCP server is reachable from the intended client.
- Amazon Ads OAuth is configured on the MCP host.
- Region is `na` for US.
- Active profile is selected at runtime.
- V1 remains in read-only mode.

## Test sequence
### 1. Identity
- Resolve active region.
- Resolve advertiser profiles.
- Select the intended US profile.
- Record profile timezone and currency.

Pass criteria: profile resolves; no write operation is attempted.

### 2. Campaign inventory
- List campaigns for the active profile.
- Check that campaign IDs and states are readable.
- Record the number of enabled/paused campaigns.

Pass criteria: inventory is non-empty or an explicit empty-account result is returned.

### 3. Search term report
- Request a small recent reporting window.
- Capture report ID/job ID and request parameters.
- Poll with bounded retries.
- Download only after terminal success.

Pass criteria: report reaches success and downloads without schema errors.

### 4. Adapter validation
Check required canonical fields where available:
- date
- profile_id
- campaign_id
- ad_group_id
- search_term
- match_type
- impressions
- clicks
- spend
- orders
- sales

Derived metrics must use safe divide-by-zero handling.

Pass criteria: every row is either canonicalized or carries an explicit data-quality flag; no value is silently invented.

### 5. Dry Run
Feed canonical records to `runtime/dry_run.py`.

Expected envelope:
```json
{
  "mode": "DRY_RUN",
  "backend_mutation": false,
  "recommendations": []
}
```

Pass criteria: `backend_mutation=false` and every actionable recommendation has `approval_required=true`.

### 6. Safety audit
Confirm logs contain no client secret, access token, refresh token, or credential material.

Confirm that no bid, budget, negative, pause, creation, or other backend write call was made.

## Exit conditions
- All pass criteria satisfied: proceed to calibration with real report data.
- Schema mismatch: stop and update the Adapter mapping.
- Stale/partial report: preserve the diagnostic and lower confidence.
- Any mutation observed during smoke test: stop the rollout and investigate the execution boundary.

## Evidence to retain
Persist only non-secret run metadata:
- test timestamp
- adapter/runtime version
- source report type
- report window
- row count
- data-quality summary
- recommendation counts by classification
- backend_mutation flag
