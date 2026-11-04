# Manual readback and W1→W2 measurement template

04/11/2026 · TEMPLATE / NOT_RUN. Fill a dated copy when Bảo authorizes the actual read; keep this blank template and historical observations intact. First delivery, day3/day7 are proposed checkpoints relative to actual W2 start, with calendar dates/owner PENDING approval. No automation/reminder exists.

## Before reading

Record authorization scope, observer, read timestamp/timezone, correct BM/account, stable ad-set/ad keys, report filters, currency and full report window. Use [BUILD_CHECKLIST](BUILD_CHECKLIST.md) expected settings; resolve actual object identity privately. Sanitize evidence before Git. Do not mix data across accounts/ad sets or confuse ad/set/campaign totals.

| Receipt field | Fill from actual observation |
|---|---|
| Checkpoint / authority / observer / timestamp | UNKNOWN |
| BM / account identity checked / exact scope | UNKNOWN |
| Account timezone / report start-end / daily or cumulative | UNKNOWN |
| Extraction time / incomplete day / processing status | UNKNOWN |
| Saved budget/hierarchy/schedule/targeting and current ad states | UNKNOWN |
| Actual start/end / eligible delivery days / interruptions | UNKNOWN |
| Click definition / native metric labels | UNKNOWN; expected K3 all-Clicks |
| Native or derived frequency / Reach freshness / 7-day window | UNKNOWN |
| Demographics counts / denominator / suppressed and unknown portions | UNKNOWN |
| Processed GA4 source/campaign/content/window/timezone / QA exclusion | UNKNOWN |
| Integrity gaps / limitations / sanitized evidence refs | UNKNOWN |
| Bảo decision required / next manual check / action actually authorized | UNKNOWN |

## Checkpoint-specific evidence

| Check | What to capture | Interpretation / next step |
|---|---|---|
| P1 05/11 W1, when assigned | Cumulative + completed-day same-window set/F1/F2 spend, impressions, all-Clicks, Reach/native frequency; daily spend; saved budget/schedule/hierarchy/targeting; demographics if exposed | Compare saved settings, separate lag from confirmed error; present unresolved C1–C3 to Bảo. No widening. |
| Final W1 review 08/11 06:45 VN and later lag reconciliation | Final actual window/end, actual spent and unpaid/committed basis if available; set/F1/F2 observations; eligibility duration; updated Reach/reporting freshness | Review time is not proof reporting is final. Fill W1_FINAL rows only with observed data and explicit status; freeze a revision for comparison after reconciliation. |
| W2 first delivery, after future release | Save/reopen expected vs actual settings, exact asset/copy/URL/parameters, actual start/state/eligibility; first spend/impressions and period | This is runtime verification, not completed by the offline pack. If no delivery, record native reason rather than inventing zero/diagnosis. |
| W2 day3 / day7 | Cumulative and completed-day views; same-window impressions/all-Clicks/spend/Reach/frequency; daily pacing and eligibility; processed reports when available | Label elapsed vs inclusive calendar days from actual start; no automatic renewal or budget changes. Day7 also verifies actual stop and later lag. |
| First displayed Clicks >0, at any checkpoint | K3 all-Clicks plus separately available landing-page clicks; persisted final URL parameters; processed GA4 source/campaign/content/sessions/engaged sessions in correct property/window; processing/consent/QA contamination | All-clicks can occur without landing visits. Missing sessions alone is not confirmed tracking failure. Follow I4 investigation; HTTP204 is transport evidence only. |

## MEASUREMENT.csv usage and definitions

[MEASUREMENT.csv](MEASUREMENT.csv) contains W1_PROVISIONAL_CONTEXT rows copied from the 04/11 source, plus NOT_OBSERVED templates for W1 final and W2. Future numeric fields are UNKNOWN, not 0. Template rows are not evidence that an ad exists, is eligible or has run. Put later observations in a new dated copy, retaining provisional rows as history.

Each row binds scope, period, report timezone, extraction status, creative revision and metric origin. The 04/11 extraction is labelled completed-by13:56 VN, not an exact per-cell timestamp. Its CPM/CTR are displayed native values. `frequency_derived` is a separate calculation; use only positive Reach and record freshness. For a new observation, fill the actual native values; do not overwrite them with calculations from rounded spend.
UTM columns on provisional W1 rows are expected identifiers from the existing contract, not fresh saved-URL observations from 04/11. Future W2 currency/UTM entries are proposal metadata; actual saved controls and parameters still need readback. A CSV row never closes those checks by itself.

| Metric/rule | Method and limits |
|---|---|
| K2/K3 | Report raw all-Clicks + impressions per ad; keep K3 definition across periods. Landing clicks, sessions and leads are distinct. No sample minimum adopted. |
| CTR / CPM / CPC | Native values retain label/origin. If derived: CTR=100×Clicks/impressions, CPM=1000×spend/impressions, CPC=spend/Clicks; denominator must be positive. Undefined CPC at 0 clicks is N/A, not 0. No CTR target or CPM ceiling adopted. |
| Reach / frequency | Do not sum ad Reach or average frequencies/CTR to get set totals. Native frequency preferred; derived=impressions/Reach when Reach>0. Keep suppression/freshness explicit. |
| K4 | Within W1 same-window F1/F2 comparison, >3:1 impressions forbids comparing CTR. One-ad W2 has no simultaneous F1/F2 pair. If either denominator is zero, report insufficient exposure rather than divide by zero. |
| K7 | Warning-only: cumulative spend <50%×USD10×actual eligible delivery days under the reference plan, at ad-set scope, not low F1 allocation. Eligible days/settings must be evidenced. Changed W2 budget/window requires a recorded applicability decision; do not silently change the rule or hardcode expected spend. |
| K8 | Warning-only frequency≥2 in the same 7-day window with native Reach>0. Label DERIVED if calculated. Uncertain Reach freshness keeps actual-frequency confidence unresolved; do not label confirmed fatigue from this alone. Shorter-period frequency does not establish a 7-day result. |
| GA4 | G-MV5QWN0XVM is the documented stream; privately verify correct property/stream/timezone. Read processed sessions/engaged sessions filtered by source/campaign/content, with processing/consent and synthetic-QA caveats. Do not assume `t` is a registered dimension or HTTP204 proves reports. |
| Accounting | Spend stays in native currency. VND balance/FX uses actual dated accounting evidence; UNKNOWN until reconciled. No reserve or Search transfer implied. |

Compare **W1 F2 final vs W2 F2-v2**, with set totals as separate budget context and F1 as W1 context only. Record window length, clock bounds/timezones, eligible duration, targeting/revision/object differences and lag. Prefer comparable-length windows; if unlike, label them and do not compare totals as equal exposure. This sequential pilot does not establish causal lift; shared W1 budget versus single W2 ad changes allocation opportunity.

## Interpretation and escalation

Report facts → derived values → limitations → proposal → actual Bảo decision. No clicks remains INCONCLUSIVE; a positive count triggers investigation, not winner status. Confirmed URL/claim/targeting/budget drift is reported immediately using [incident cards](../pre-readback/INCIDENT_CARDS.md). For W2, use the v2 URL in this pack as expected; incident cards' v1 URL is the historical W1 baseline. Agent pause/enable/fix still requires an exact mandate. K7/K8 warning alone does not authorize it.

Closeout fields to fill: observed boundary preservation `UNKNOWN`; useful content/reader retention `UNKNOWN`; execution outcome `UNKNOWN`; decision `PENDING`; independently reviewed `NOT_RUN` unless actually performed. New W2 source inclusion in RMK is not checked by this template and remains HOLD.
