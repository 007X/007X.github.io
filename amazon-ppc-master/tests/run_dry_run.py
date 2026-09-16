import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "search-term-synthetic.json"


def metrics(row):
    clicks = row.get("clicks", 0) or 0
    spend = row.get("spend", 0) or 0
    orders = row.get("orders", 0) or 0
    sales = row.get("sales", 0) or 0
    return {
        "cpc": spend / clicks if clicks else 0.0,
        "cvr": orders / clicks if clicks else 0.0,
        "acos": spend / sales if sales else None,
        "roas": sales / spend if spend else None,
    }


def classify(row):
    m = metrics(row)
    term = row["search_term"].lower()
    clicks = row.get("clicks", 0) or 0
    orders = row.get("orders", 0) or 0

    if term.startswith("free ") and clicks >= 10 and orders == 0:
        return "suppress_review"
    if orders >= 3:
        return "harvest"
    if orders >= 1:
        return "test"
    if clicks < 25:
        return "observe"
    return "suppress_review"


def main():
    rows = json.loads(FIXTURE.read_text(encoding="utf-8"))
    counts = {}
    for row in rows:
        label = classify(row)
        counts[label] = counts.get(label, 0) + 1
        m = metrics(row)
        print(row["search_term"], label, m)

    assert counts.get("harvest", 0) >= 1, "Expected at least one harvest candidate"
    assert counts.get("test", 0) >= 1, "Expected at least one test candidate"
    assert counts.get("suppress_review", 0) >= 1, "Expected at least one suppression-review candidate"

    # Safety invariants for the synthetic dry run.
    assert all(row.get("campaign_id") for row in rows), "Every row needs traceable campaign context"
    print("Dry-run regression passed")


if __name__ == "__main__":
    main()
