# Proposed execution fields — not applied

This proposal fills missing dashboard inputs. Approved authority remains 11.7m VND media before tax, 5.6m first LinkedIn envelope, 6.1m held inside the total, and weekly review. No FX rate is asserted. USD was observed in the prior probe; actual account currency/timezone/minimums must be read back before a saved production build. USD10 here is a proposed conservative average, not adoption of the probe's old dates/budget or a delivery forecast.

| Field | Concrete proposed value | Verification / boundary |
|---|---|---|
| Local wave label | wave01 | Concrete naming proposal; no actual campaign/ad IDs |
| Structure | One cold Brand awareness / Single image ad set with two ads: P1 COLD and P2 COLD | One shared audience/budget; no split into two USD10/day ad sets, no claim of equal rotation or statistical A/B test |
| Audience | R5, Vietnam recent/permanent, English; Engineering OR IT OR Operations OR Quality Assurance AND Manager OR Director OR VP OR CXO | Existing scoped configuration only; fit route in GAP_DECISIONS must be resolved. No narrower subcohort invented in saved targeting |
| Expansion / LAN | OFF / OFF | Recheck saved state; preserve cohort intent |
| Placement | Feed only; no Right Rail if exposed as an independent option | Proposal, not copied from validation defaults. Verify actual format-supported UI; stop on incompatible controls |
| Optimization / bid | Impressions / Maximum delivery, standard pacing | Proposal for awareness, no manual CPM guess or accelerated delivery; current availability must be read back |
| Average daily budget | USD10 for the shared cold ad set | Nominal week total USD70; daily actual spend can vary. This is not a strict per-day charge ceiling |
| Calendar | Start 02/11/2026 00:00 UTC; end 08/11/2026 23:59 UTC | In Vietnam: 02/11 07:00 through 09/11 06:59. Fixed seven platform days; not 01/11 auto-start. If approval/fit/build misses the slot, revise dates before save; never backdate |
| Budget mode | Daily budget with fixed start/end, subject to actual UI validation | Nominal scheduled total 7×USD10=USD70. Do not enter a USD70 lifetime budget assuming it passes platform minimums; do not combine daily+lifetime with fixed dates if UI only permits continuous schedule |
| VND control | Proposed first-week working ceiling 2.8m VND within the approved 5.6m | 2.8m is proposed pacing, not a new approved allocation. USD70 fits only when documented dashboard-to-VND media basis ≤40,000 VND/USD. This is an algebraic ceiling, not an FX quote. Obtain actual company/account basis; if unknown, keep off. No automatic FX conversion or all-in-tax hold |
| Reserve / week2 | Remaining first-envelope budget stays uncommitted; 6.1m reserve untouched | Week1 ending does not authorize week2. Weekly data matrix determines continuation; no automatic RMK/Search allocation |
| Platform CTA / URLs | Learn more; selected BUILD_ADS/BUILD_CARDS destinations | Verify actual button availability. Artwork CTA remains artwork text; do not replace native headline with artwork hook |
| Save state | Draft/Off or paused, campaign non-delivering | Production build would require a specific mandate after fit/asset decisions; do not edit VALIDATION_ONLY probe into production |

## Measurement and stop proposal

Operator/decision owner proposed: **Bảo**. Codex can prepare a dated readback on instruction; no scheduler or recurring account control is created. Log to existing Week1_Readback_Template with date range, account currency/timezone, actual spend, exact source ad IDs, reach/impressions, frequency if available, clicks/CTR/CPM and company/function/seniority breakdown where available. Do not identify buyers from aggregate delivery or impute missing metrics as zero.

- Before enable: saved native field/asset/order/URL/CTA readback, exact recipient scope, actual budget/date/currency, page permissions, fit/rights dispositions and processed GA4 reader-cohort reporting method. Native original/render QA is not native feed preview.
- First delivery day: Bảo checks unexpected activation/spend, cohort drift, source URL and reader arrival. No lead submission needed. Log immediate technical issues without waiting for weekly performance review.
- At week close **09/11/2026 Vietnam**, after the proposed UTC window ends: review full week and evidence sufficiency; do not declare win/loss from tiny samples. If data remains sparse, record INSUFFICIENT_DATA rather than invent a CTR/lead threshold or broaden solely to spend.
- Stop/pause proposal for Bảo: wrong destination/locale/claim, unauthorized asset, targeting or Expansion/LAN drift, missing/wrong-stream reader measurement, unexplained bridge/session mismatch, or projected/actual VND envelope breach. Preserve sanitized evidence and investigate before resuming. These rules do not delegate autonomous pause authority to Codex.
- Reader reporting: source cohort from reader entrance UTM + treatment, ordered same-session contact path; native engagement is reading evidence only. Contact bridge metadata is in page_location, not proven contact ep.bridge_* dimensions. Platform clicks and GA4 sessions need not match one-to-one. Form-success, CRM/valid leads and optional section metrics remain unverified; never count CTA clicks as leads.
- RMK: four prepared carousels stay deferred until exact cold ad-source registry/rule/window/objective and native eligibility/reachable gate are met. Do not replace source with existing Page/website audiences. Search remains optional and separate.

Official guidance checked 29/10/2026: [budget types and variable daily pacing](https://www.linkedin.com/help/lms/answer/a422101), [schedule, UTC boundaries and budget-mode restrictions](https://www.linkedin.com/help/lms/answer/a427572). Those rules support the proposed mode; they do not prove saved UI availability or delivery at this audience size.
