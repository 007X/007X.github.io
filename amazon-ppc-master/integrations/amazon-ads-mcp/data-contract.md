# Amazon Ads Data Contract (V1)

This contract is the normalization boundary between Amazon Ads MCP responses and PPC Skills.

## Required Account Context

- `region`: `na` for the US marketplace in V1
- `profile_id`
- `currency`: expected `USD` for US profiles
- `report_start_date`
- `report_end_date`
- `retrieved_at`

## Core Entities

### Campaign

Minimum normalized fields:

- `campaign_id`
- `campaign_name`
- `state`
- `budget`
- `budget_type`
- `targeting_type` when available
- `portfolio_id` when available

### Target / Keyword

Minimum normalized fields:

- `target_id` or `keyword_id`
- `campaign_id`
- `ad_group_id`
- `keyword_text` / target expression
- `match_type` when applicable
- `state`
- `bid`

### Search Term

Minimum normalized fields:

- `search_term`
- `campaign_id`
- `ad_group_id`
- `target_id` when available
- `match_type` when available
- `impressions`
- `clicks`
- `spend`
- `orders`
- `sales`

### Placement

Minimum normalized fields:

- `campaign_id`
- `placement`
- `impressions`
- `clicks`
- `spend`
- `orders`
- `sales`

## Derived Metrics

Use decimal-safe arithmetic and return `null` when the denominator is zero.

- `ctr = clicks / impressions`
- `cpc = spend / clicks`
- `cvr = orders / clicks`
- `acos = spend / sales`
- `roas = sales / spend`
- `sales_per_click = sales / clicks`

Where order/sales attribution is unavailable or delayed, explicitly mark the metric as unavailable rather than treating it as zero.

## Lookback Windows

The default diagnostic bundle should compare:

- 1 day: anomaly detection only
- 3 days: short-term movement
- 7 days: primary operating view
- 14 days: stability check
- 30 days: historical context

A single anomalous day must not be sufficient for a negative, pause, deletion, or structural change.

## Report Acquisition

V3 async reports follow:

`create report -> poll status -> download completed file -> parse -> normalize -> validate`

Do not send partially downloaded, malformed, or schema-mismatched rows into optimization Skills.

## Validation Rules

Reject or quarantine a dataset when:

- profile/region context is missing
- currency context is unknown for monetary comparisons
- date range is missing
- required primary keys are absent
- numeric fields contain invalid values
- a report is incomplete or still processing

## Provenance

Every normalized dataset should retain:

- source operation/tool name
- source report type
- profile ID
- date window
- retrieval timestamp
- original row count
- normalized row count
- validation status

## Optimization Boundary

Skills may calculate and recommend actions from this contract. Backend mutations remain blocked until the Execution Gate receives explicit human approval.
