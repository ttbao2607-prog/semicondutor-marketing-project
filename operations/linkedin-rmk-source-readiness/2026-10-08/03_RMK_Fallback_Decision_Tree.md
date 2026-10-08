# 03 · RMK fallback decision tree

Status: DRAFT_FOR_PO_DECISION. Every action below needs Bảo's decision or an operational mandate; nothing here is automatic and no scheduler is created. Budget numbers come only from the approved envelope: **11.7 million VND before tax**, of which 5.6 million is the first wave and 6.1 million is held inside the same total (up to 5.6 million for the next LinkedIn wave and up to 0.5 million for optional Search). The package budget table has no separate RMK line (remarketing sits inside "LinkedIn tiếp theo", `De_xuat_paid_ads.md` line 39) and says thin data may lead to holding budget (line 51).

Release gate from the [data plan](../../LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md): exact new-cold source cohort + rule/window chosen by Bảo + actual Ready/eligible + **at least 300 reachable members after UI filters** + proof, destination/HTML, tracking, pacing and budget gates. No calendar-based release, no Page users substituted.

| State | What is observed | Options for Bảo | Do not |
|---|---|---|---|
| **S0** | Cold campaign not delivering yet | Wait; keep decisions in [01](01_RMK_Source_Rule_Decision_Pack.md) and [06](06_Operational_Mandate_Checklist.md) | Create an RMK audience from historical or Page data |
| **S1** | Source audience created but processing / not Ready | Re-read at the next planned check; keep cold running within the approved envelope | Enable RMK or judge size before Ready |
| **S2** | Ready but below 300 reachable after filters | (a) Keep cold running and re-check at the next point; (b) decide to widen the rule or lookback within what the UI offers (a decision, with the trade-offs in 01); (c) skip RMK for week 2 and put the effort into replacing the weak cold part; (d) use the held Search part for demand capture instead | Pool other campaigns, Page or organic users; split into smaller pools; promise a date for RMK |
| **S3** | Ready, 300 or more reachable, other gates not met (destination, tracking, pacing, budget) | Fix the missing gate first; hold RMK until all gates pass | Release RMK because the pool is large enough |
| **S4** | All gates pass | Bảo selects objective (Engagement or click to the reader) and releases within the 5.6 million next-wave cap | Exceed the envelope; change several variables at once |

Reading rules at every check: use the same cohort and revision; read reach and frequency as exposure, CTR/engagement/onward behaviour as interest; a thin dataset is recorded as inconclusive, not as a winner or a failure; per the package, weak parts are replaced one at a time and the working part is kept.

Check points (from the data plan, proposed sampling only): eligible delivery day 3 and 7, then weekly on a stable setup. Native audience processing has latency, so read fresh status when judging.

Escalate to Bảo (L2) when: the pool stays below the gate after the second check; a change of platform, budget structure or business scope is considered; or any step would need a live action not yet authorized.
