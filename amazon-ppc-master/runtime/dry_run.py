#!/usr/bin/env python3
"""Deterministic, read-only Dry Run for Amazon PPC Master.

Consumes canonical records and emits a recommendation queue. This file never
calls Amazon Ads APIs and never performs backend mutations.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def ratio(num: float, den: float) -> float | None:
    return None if den == 0 else num / den


def classify(row: dict[str, Any], target_acos: float | None) -> str:
    orders = float(row.get("orders", 0) or 0)
    clicks = float(row.get("clicks", 0) or 0)
    spend = float(row.get("spend", 0) or 0)
    sales = float(row.get("sales", 0) or 0)
    relevant = bool(row.get("relevant", True))
    historical_orders = float(row.get("orders_30d", orders) or 0)

    if not relevant and clicks >= 8 and spend > 0:
        return "SUPPRESS_REVIEW"
    if orders >= 2 and (target_acos is None or ratio(spend, sales) is not None and ratio(spend, sales) <= target_acos):
        return "HARVEST"
    if orders >= 1 or (clicks >= 8 and relevant):
        return "TEST"
    if historical_orders > 0 or relevant:
        return "OBSERVE"
    return "OBSERVE"


def recommend(row: dict[str, Any], target_acos: float | None) -> dict[str, Any]:
    spend = float(row.get("spend", 0) or 0)
    clicks = float(row.get("clicks", 0) or 0)
    sales = float(row.get("sales", 0) or 0)
    orders = float(row.get("orders", 0) or 0)
    current_bid = row.get("current_bid")
    acos = ratio(spend, sales)
    classification = classify(row, target_acos)

    action = "HOLD"
    proposed_bid = current_bid
    rationale = "Evidence is insufficient for a backend-changing recommendation."

    if classification == "HARVEST" and current_bid is not None:
        action = "HARVEST_REVIEW"
        rationale = "Repeatable productive demand; review intentional keyword capture without suppressing the discovery source."
    elif classification == "TEST" and current_bid is not None:
        action = "TEST_REVIEW"
        rationale = "Promising/relevant traffic has evidence, but not enough to treat it as fully harvested demand."
    elif classification == "SUPPRESS_REVIEW":
        action = "SUPPRESS_REVIEW"
        rationale = "Relevance concern plus sufficient traffic warrants manual review; do not auto-negative."
    elif current_bid is not None and target_acos is not None and acos is not None and acos > target_acos * 1.35 and clicks >= 8:
        proposed_bid = round(float(current_bid) * 0.8, 2)
        action = "REDUCE_BID_REVIEW"
        rationale = "Recent spend efficiency is materially weaker than target; use a controlled bid reduction before suppression."

    return {
        "search_term": row.get("search_term"),
        "source_campaign": row.get("campaign_id"),
        "source_ad_group": row.get("ad_group_id"),
        "classification": classification,
        "action_type": action,
        "current_bid": current_bid,
        "proposed_bid": proposed_bid,
        "evidence_window": row.get("evidence_window", "7d"),
        "supporting_metrics": {
            "spend": spend,
            "clicks": clicks,
            "orders": orders,
            "sales": sales,
            "acos": acos,
            "cvr": ratio(orders, clicks),
        },
        "rationale": rationale,
        "expected_effect": "Control waste while preserving useful discovery capacity.",
        "risk": "Low-to-moderate; suppression actions remain approval-gated.",
        "reversibility": "high" if action in {"HOLD", "REDUCE_BID_REVIEW"} else "medium",
        "approval_required": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--target-acos", type=float, default=None)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    rows = payload.get("records", payload if isinstance(payload, list) else [])
    queue = [recommend(row, args.target_acos) for row in rows]
    result = {
        "mode": "DRY_RUN",
        "backend_mutation": False,
        "records_in": len(rows),
        "recommendations": queue,
    }
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
