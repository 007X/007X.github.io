# PPC Dry-Run Runtime

This runtime is the deterministic bridge between canonical Amazon Ads records and the approval queue.

## Run

```bash
python3 amazon-ppc-master/runtime/dry_run.py \
  amazon-ppc-master/fixtures/search-term-synthetic.json \
  --target-acos 0.30 \
  --output /tmp/ppc-dry-run.json
```

## Guarantees

- `mode=DRY_RUN`
- `backend_mutation=false`
- every recommendation contains `approval_required=true`
- no Amazon credential is accepted by this script
- no network call is made by this script

## Production boundary

The runtime consumes canonicalized records only. A future live executor must sit behind the existing Execution Gate and require explicit approval before invoking any write-capable Amazon Ads MCP operation.
