# Amazon Ads MCP Integration

This directory defines the deployment boundary between Amazon PPC Master and the Amazon Ads MCP tool layer.

## Architecture

```text
ChatGPT
  |
  | Remote MCP
  v
Amazon Ads MCP (KuudoAI/amazon_ads_mcp)
  |
  | Amazon Ads API
  v
Amazon Ads / US advertiser profile
  |
  v
Amazon PPC Master Skills
```

The MCP server is the API/tool layer. The PPC Skill Stack remains the decision layer.

## Selected MCP

V1 uses `KuudoAI/amazon_ads_mcp` as the reference implementation. The current upstream provides Docker Compose deployment, HTTP MCP at the configured port (the example uses `9080`), configurable tool packages, Code Mode, asynchronous report workflows, and multi-region routing. Ads API v1 packages are currently marked beta upstream, so V1 keeps the mature reporting surface as the primary source of truth and adds v1 packages deliberately. citeturn112052view0

Upstream: https://github.com/KuudoAI/amazon_ads_mcp

## V1 Packages

Default read/reporting package set for PPC Master:

```text
profiles
accounts-ads-accounts
reporting-version-3
sponsored-products
sp-suggested-keywords
```

For later campaign-management work, add only the package required by the Skill. The upstream also supports `ads-api-v1-all` and product-specific Ads API v1 packages; these are currently beta and should not replace the stable reporting contract without validation. citeturn112052view0

## Code Mode

Use Code Mode by default for the broader catalog. Upstream documents that Code Mode exposes lightweight discovery/execute tools while keeping the larger catalog available on demand, reducing context pressure. citeturn112052view0

## Authentication

Do not commit Amazon credentials, refresh tokens, client secrets, access tokens, profile IDs, or OAuth state to this repository.

For BYOA, configure these at runtime:

- `AMAZON_AD_API_CLIENT_ID`
- `AMAZON_AD_API_CLIENT_SECRET`
- `AUTH_METHOD=direct`
- `REGION=na`

The upstream BYOA flow requires a Login with Amazon application and an allowed callback URL matching the MCP HTTP listener. For local port `9080`, the documented callback pattern is `http://localhost:9080/auth/callback`. citeturn112052view0

## Reports

The PPC system treats Amazon Ads reporting data as the source of truth for spend, clicks, orders, sales, and placement performance. V3 reports are asynchronous:

```text
create report
  -> poll status
  -> download completed report
  -> parse
  -> validate
  -> normalize
```

The normalized schema is defined in `data-contract.md`. Upstream documents server-side report/download workflows and the need for HTTP transport for report downloads. citeturn112052view0

## Client

For an HTTP MCP server, see `client-config.example.json`. The example intentionally uses `localhost` and contains no credentials. For remote/public deployment, use TLS and an inbound authorization mechanism rather than exposing an unauthenticated MCP endpoint. The upstream documents `MCP_INBOUND_TOKEN` or trusted-proxy authorization for public HTTP deployments. citeturn855643search0

## Bring-Up

Follow `bring-up.md` in order. V1 stops at read-only verification before any write operation.

## Safety Boundary

The MCP layer may technically expose write operations, but Amazon PPC Master must keep them behind the execution gate:

`Analyze -> Recommendation -> Explicit approval -> Execute -> Verify`

No credential or write endpoint belongs in the Skill repository itself.
