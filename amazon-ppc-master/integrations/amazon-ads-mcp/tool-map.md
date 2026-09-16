# Amazon Ads MCP Tool Map

This document maps the PPC runtime stages to the Amazon Ads MCP capabilities required by V1.

## Boundary

The MCP server is the transport/API tool layer. Skill files decide what the data means and what should be recommended. The Execution Gate decides whether an approved write may be sent back to Amazon Ads.

## V1 read path

| Runtime stage | MCP capability | Required output | Write? |
|---|---|---|---|
| Select region | `set_active_region` | `na` | No |
| Discover advertiser context | profiles / identity tools | profile id, currency, timezone | No |
| Select profile | `set_active_profile` | active profile | No |
| Campaign inventory | Sponsored Products campaign-management read operations | campaign ids, status, budget, targeting structure | No |
| Performance | `reporting-version-3` | report id/status | No |
| Search-term mining | Sponsored Products search-term report | search term metrics + source campaign/ad group | No |
| Keyword/target diagnosis | keyword/target reporting | target metrics | No |
| Placement diagnosis | placement reporting | placement metrics | No |
| Normalize | internal data contract | stable analysis schema | No |
| Analyze | PPC Skills | findings + recommendations | No |

## Report state machine

```text
REQUEST
  -> CREATED
  -> IN_PROGRESS
  -> SUCCESS
       -> DOWNLOAD
       -> VALIDATE
       -> NORMALIZE
       -> ANALYZE

Any stage
  -> TRANSIENT_ERROR
       -> retry with bounded backoff

Terminal failure
  -> FAILED
       -> mark data unavailable
       -> do not manufacture metrics
```

The runtime must preserve `report_id`, `profile_id`, `report_type`, requested date range, timezone, currency, and retrieval timestamps.

## Search Term Report priority

For the first daily loop, request Sponsored Products search-term data first because it drives both waste diagnosis and keyword expansion. Keep source campaign/ad group identifiers attached to every normalized row so recommendations remain traceable.

## Read-before-write

No write-capable tool should be invoked merely because a recommendation was generated. The runtime must first emit an Execution Gate record containing:

- `action_type`
- `target_id`
- `current_value`
- `proposed_value`
- evidence window
- supporting metrics
- rationale
- expected effect
- risk
- `approval_required=true`

Only an explicit approval event can move a recommendation into the execution queue.

## Tool naming note

Exact exposed tool names can vary with the selected Amazon Ads MCP package set and upstream version. Prefer capability-based resolution through the MCP server's schema/tool discovery rather than hard-coding undocumented method names.

The current reference deployment is `KuudoAI/amazon_ads_mcp`; check its current package/schema before connecting a production runtime.
