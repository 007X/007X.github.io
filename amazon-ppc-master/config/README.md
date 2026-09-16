# Configuration

Configuration is split into two layers:

- `account-profile.example.yaml`: account/business inputs that vary by Amazon Ads advertiser profile.
- `runtime-policy.yaml`: stable safety and optimization policy used by the Skills and Dry Run runtime.

## Account profile

Populate the account profile only in a private runtime location. Do not commit real profile IDs, credentials, OAuth tokens, client secrets, or other sensitive account identifiers.

Business economics may include target ACOS/ROAS/TACOS, contribution margin, and minimum profit per order. Leave them null when they are not known; Skills must not invent targets.

## Runtime policy

The default policy is conservative and recommendation-only:

- recent 3-day window vs 14-day operating baseline, with 30-day context;
- preserve Auto/Broad/Phrase discovery;
- reduce bids before deleting traffic when evidence is incomplete;
- require stronger evidence for negative/pause actions;
- budget increases require repeated productive constraint;
- backend mutation is disabled by default;
- approval is required for every write recommendation.

Treat the example values as starting policy, not account-specific truth. Tune them after observing the real account baseline.
