# Amazon PPC Master

Amazon PPC AI Skill Stack for the US marketplace.

## Objective

Use Amazon Ads data to continuously discover useful search demand, improve spend efficiency, and scale proven demand while avoiding aggressive keyword-pool shrinkage.

## Architecture

**Amazon Ads API/MCP = data + execution layer**  
**PPC Skills = analysis + decision layer**  
**Execution Gate = human approval layer**

## V1 Modules

- Daily Audit
- Search Term Mining
- Bid Optimizer
- Budget Optimizer
- Negative Keyword
- Scale / Shrink Planner
- Profit / TACOS Planner

## Safety

V1 is recommendation-first. No bid, budget, negative, pause, or campaign-creation mutation should run without explicit approval.

## Design Principle

Reduce inefficient spend without destroying exploration. Bid and budget controls generally come before deletion when evidence is incomplete.
