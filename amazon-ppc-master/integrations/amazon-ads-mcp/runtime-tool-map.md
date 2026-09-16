# Amazon Ads MCP Runtime Tool Map

This document maps the PPC runtime to the current capabilities exposed by the reference Amazon Ads MCP. Keep operation semantics stable while allowing exact tool names to vary by enabled package/server version.

## Runtime stages

### 1. Context and identity

Required capabilities:
- set/select active region (`na` for US)
- discover/list advertiser profiles
- set/select active profile
- confirm profile currency and timezone

Expected output:
- `region`
- `profile_id`
- `currency`
- `timezone`

### 2. Campaign inventory

Required capability:
- list/query campaigns for the active profile

Expected output:
- campaign id/name
- state/status
- daily budget
- campaign type
- serving status when available

Do not mutate campaign state during inventory collection.

### 3. Reporting

Primary capability:
- Sponsored Products / campaign / keyword-target / placement / search-term reporting through V3 reporting tools

Execution pattern:
1. create asynchronous report
2. capture report/job identifier
3. poll status
4. stop on success/failure/timeout
5. download completed report
6. preserve raw artifact
7. normalize into the PPC data contract

The MCP currently documents this asynchronous pattern for V3 reports and stores downloaded files server-side under profile-scoped storage. The exact schema/tool names should be discovered from the deployed server version rather than hard-coded in Skills.

### 4. Targeting and keyword operations

Required read capabilities:
- list/query keywords or targets
- inspect match type and current bid
- inspect negative keywords where available

Write capabilities are not called by Skills directly. They are exposed to the Execution Gate only after explicit approval.

### 5. Recommendation/experiment support

Optional capabilities:
- suggested keywords
- recommendations/insights
- change history
- placement detail

These can enrich evidence but cannot override the core performance data contract.

## Code Mode behavior

The reference MCP currently defaults to `CODE_MODE=true`. In Code Mode, the client sees four lightweight discovery/execute meta-tools and discovers specific tools on demand. This is preferred for a broad package catalog because it reduces context consumption.

## Package baseline for V1

Start with the smallest package set needed for PPC:

- `profiles`
- `accounts-ads-accounts`
- `reporting-version-3`
- `campaign-manage`
- `sponsored-products`
- `sp-suggested-keywords`

Add other packages only when a Skill has a documented dependency.

## Failure handling

Classify failures as:
- authentication
- profile/region
- throttling/rate-limit
- report validation
- report processing
- download/storage
- schema mismatch
- transient network/server
- unknown

For transient failures, retry conservatively with bounded attempts. For schema mismatch or unknown errors, stop the pipeline and surface the raw error context instead of guessing.

## Safety boundary

Read/reporting operations may run automatically. Any operation that changes bids, budgets, keywords, targets, negatives, campaign state, or creates/deletes objects must be routed through:

`Recommendation -> Explicit approval -> Execute -> Verify`

Never place real credentials or refresh/access tokens in this repository.
