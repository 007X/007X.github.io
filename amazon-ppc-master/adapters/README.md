# Amazon Ads Report Adapter Layer

## Purpose

Convert raw Amazon Ads report payloads/files into the canonical PPC data contract without assuming that every upstream report schema remains identical.

## Pipeline

```text
raw Amazon report
  -> source detection
  -> field mapping
  -> numeric/date normalization
  -> derived metrics
  -> attribution-window preservation
  -> data-quality flags
  -> canonical records
```

## Rules

- Keep the raw source field names available for traceability.
- Never silently rename an attribution window such as `14d` into an unspecified orders/sales field.
- Missing values remain explicit; do not convert missing numeric data into zero unless the source semantics prove zero.
- Preserve profile, campaign, ad group, target/keyword, search term, placement, date, currency, timezone, and report metadata.
- Derived metrics are calculated only when their denominators are valid.
- Every recommendation downstream should be able to reference the source report, reporting window, and freshness timestamp.

## Canonical metric formulas

- CTR = clicks / impressions
- CPC = spend / clicks
- CVR = orders / clicks
- ACOS = spend / sales
- ROAS = sales / spend
- spend_per_order = spend / orders

## Data-quality states

Use one or more flags:

- `ok`
- `missing_required_field`
- `partial_report`
- `attribution_window_present`
- `stale_report`
- `duplicate_record`
- `invalid_numeric`
- `invalid_date`
- `currency_mismatch`
- `timezone_mismatch`

A record with material quality issues must not be escalated directly to a destructive action recommendation.
