# Amazon Ads MCP Bring-Up Checklist

## 0. Run the MCP Server

Use the upstream repository as the runtime source:

```bash
git clone https://github.com/KuudoAI/amazon_ads_mcp.git
cd amazon_ads_mcp
cp .env.example .env
```

Configure the `.env` locally or through your secret manager. Never commit the real `.env`.

Start:

```bash
docker compose up -d
```

Verify:

```bash
docker compose ps
docker compose logs --tail=200
```

V1 endpoint:

```text
http://localhost:9080/mcp/
```

## 1. Authentication

For BYOA:

```env
AUTH_METHOD=direct
AMAZON_AD_API_CLIENT_ID=<runtime-secret>
AMAZON_AD_API_CLIENT_SECRET=<runtime-secret>
REGION=na
```

The Login with Amazon callback must match the MCP server listener. For local development this is typically:

```text
http://localhost:9080/auth/callback
```

Complete OAuth as the Amazon Ads account owner/operator, then retain credentials only on the MCP host.

## 2. Profile Smoke Test

Run the MCP client and confirm:

1. Set active region to `na`.
2. Start OAuth flow if authorization is not already present.
3. List advertiser profiles.
4. Select the intended US profile.
5. Record the profile context in the PPC runtime, not in Git.

Expected result:

```text
region = na
marketplace = US
currency = USD
profile_id = <runtime value>
```

## 3. Read-Only Campaign Test

Before any write operation, retrieve:

- enabled and paused campaigns
- campaign IDs and names
- budgets
- targeting type / campaign type when available

No mutation is part of this test.

## 4. Reporting Test

Create one Sponsored Products report for a bounded date window. Follow the asynchronous lifecycle:

```text
create -> poll -> download -> parse -> validate
```

Validate the normalized fields against `data-contract.md`.

## 5. PPC Skill Smoke Test

Feed the normalized report bundle into:

```text
Daily Audit
    -> Search Term Mining
    -> Bid Optimizer (recommendation only)
```

The output must contain evidence and confidence, not just a list of changes.

## 6. Execution Gate Test

Intentionally generate a sample bid-change recommendation. Confirm it contains:

```yaml
approval_required: true
action_type: bid_change
target_identifier: <id>
current_value: <value>
proposed_value: <value>
evidence: <metrics>
rationale: <reason>
risk: <description>
```

Do not execute the mutation during bring-up.

## 7. Failure Handling

Stop the test if any of the following occurs:

- OAuth succeeds but profile list is empty
- profile region is not `na`
- report remains incomplete
- report schema does not match the data contract
- monetary fields use an unexpected currency
- a tool attempts a backend mutation before approval

Capture the server error and relevant operation name. Do not retry blindly.
