# Amazon PPC Master

Amazon PPC AI Skill Stack for the US marketplace.

## Objective

Use Amazon Ads data to continuously discover useful search demand, improve spend efficiency, and scale proven demand while avoiding aggressive keyword-pool shrinkage.

## Architecture

**Amazon Ads API/MCP = data + execution layer**  
**PPC Skills = analysis + decision layer**  
**Execution Gate = human approval layer**

## V1 Pipeline

```text
Amazon Ads MCP
  -> Data Contract
  -> Daily Audit
  -> Search Term Mining
  -> Bid Optimizer
  -> Budget / Negative / Scale-Shrink / Profit modules
  -> Execution Gate
  -> Explicit Approval
  -> Amazon Ads write action
  -> Verification
```

## V1 Modules

- Daily Audit
- Search Term Mining
- Bid Optimizer
- Budget Optimizer
- Negative Keyword
- Scale / Shrink Planner
- Profit / TACOS Planner

The first three modules are the initial decision chain because they establish account health, continuous keyword discovery, and conservative bid control.

## Data Flow

Primary inputs are Campaign, Keyword/Target, Search Term, and Placement data from Amazon Ads reporting. The normalized schema is defined in `integrations/amazon-ads-mcp/data-contract.md`.

Use recent and baseline windows together rather than optimizing from a single anomalous day. Preserve Amazon attribution-window semantics in raw data.

## Safety

V1 is recommendation-first. No bid, budget, negative, pause, or campaign-creation mutation should run without explicit approval.

Every write candidate must include evidence, current value, proposed value, rationale, expected effect, risk, and `approval_required=true`.

## Design Principle

Reduce inefficient spend without destroying exploration. Bid and budget controls generally come before deletion when evidence is incomplete.

Protect meaningful Auto/Broad/Phrase discovery paths unless there is clear evidence of structural waste or a deliberate decision to reduce exploration.