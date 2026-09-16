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

V1 uses `KuudoAI/amazon_ads_mcp` as the reference implementation. It supports Amazon Ads API operations, reporting, Sponsored Products, profiles, and other advertising surfaces. The repository recommends Docker and exposes an HTTP MCP endpoint; its default example port is 9080. See the upstream project before deployment because its API surface and package names can change.

Upstream: https://github.com/KuudoAI/amazon_ads_mcp

## V1 Packages

Keep the initial tool surface intentionally small:

- `profiles`
- `accounts-ads-accounts`
- `reporting-version-3`
- `campaign-manage`
- `sponsored-products`
- `sp-suggested-keywords`

Add other packages only when a PPC Skill needs them.

## Authentication

Do not commit Amazon credentials, refresh tokens, client secrets, access tokens, or profile identifiers to this repository.

Use environment variables / a secret manager on the MCP host. For BYOA, the upstream server documents:

- `AMAZON_AD_API_CLIENT_ID`
- `AMAZON_AD_API_CLIENT_SECRET`
- `AUTH_METHOD=direct`

Authorization is completed through the MCP server's OAuth flow. The US marketplace uses the `na` region.

## Reports

The PPC system should treat Amazon Ads reporting data as the source of truth for spend, clicks, orders, sales, and placement performance. Reports are asynchronous: create report -> poll -> download/process.

The first implementation should expose read/reporting operations before enabling mutation operations.

## Safety Boundary

The MCP layer may technically expose write operations, but Amazon PPC Master must keep them behind the execution gate:

`Analyze -> Recommendation -> Explicit approval -> Execute -> Verify`

No credential or write endpoint belongs in the Skill repository itself.
