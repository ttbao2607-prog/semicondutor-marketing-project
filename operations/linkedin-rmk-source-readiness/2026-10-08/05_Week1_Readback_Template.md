# 05 · Week 1 readback template

Status: TEMPLATE / NOT FILLED. [05_Week1_Readback_Template.csv](05_Week1_Readback_Template.csv) is header only. Baseline for the new cold campaign is **UNKNOWN / NOT CREATED**: do not copy numbers from historical test rows, and do not write 0 where nothing was observed (write UNKNOWN).

Purpose: one consistent record at each check so the end-of-week-1 review in the sent package (week 1 → review → week 2, measured by right audience, interest, onward behaviour and cost) can be answered from evidence. Cadence from the data plan: daily integrity/pacing note once delivery is authorized, checks at eligible delivery day 3 and 7, then weekly. It is a sampling proposal, not a scheduler.

## What to record per check
| Group | Fields | Why |
|---|---|---|
| Identity | date, account timezone, eligible delivery day, source cohort ID, content and targeting revision | Keep slices with different scope apart |
| Right audience | distribution by company, function and seniority as the platform reports it | Did the ads reach the intended group (matched mapping quality is separate and may be CHANGES_REQUIRED) |
| Opportunity | reach, impressions, frequency | Exposure |
| Interest | CTR, engagement counts (by the platform's own metric definition) | Interest in the opening ad |
| Onward behaviour | reader sessions with interaction, by source/medium/campaign, after processing | Did interested people go on to the reader |
| Cost | spend (currency, before tax), CPM, CPC, budget remaining | Is the use of money reasonable |
| RMK pool | source rule, lookback, audience status, displayed members, filtered reachable, eligible | Feeds [03 decision tree](03_RMK_Fallback_Decision_Tree.md) |
| Integrity | tracking present, UTM preserved, any delivery change or pause, notes | Separate measurement problems from content problems |

## Interpretation rules
- Reach and frequency show chance of exposure; CTR, engagement and onward behaviour show interest; awareness (association with Digiwin) is a separate goal that needs its own signal.
- Verified leads are a supplementary commercial signal.
- Thin data or limited coverage: record inconclusive, narrow the test, observe longer or hold budget.
- Each change records the signal, the part replaced and the result at the next review; when changing a hook keep the audience and the rest constant so the effect can be read.
- Synthetic or test visits never enter paid results.

Money is read from the dashboard that Bảo manages; tax and payment are handled by accounting under company process.
