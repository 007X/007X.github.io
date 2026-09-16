# Expected Synthetic Dry Run

Using `fixtures/search-term-synthetic.json`, the runtime should demonstrate:

| Search term | Expected class | Rationale |
| --- | --- | --- |
| insulated lunch bag large | harvest/test | Converts with meaningful evidence; check existing coverage before proposing creation. |
| lunch bag for work | test | Relevant and converting, but evidence is lighter than the strongest candidate. |
| free lunch bag | suppress review | Low commercial relevance plus spend without sales; still requires the configured evidence gate. |
| lunch bag | harvest/observe | Converting and relevant; protect existing discovery coverage and avoid blind duplication. |

No fixture should produce an automatic backend mutation. All actions remain recommendation-only with `approval_required=true`.
