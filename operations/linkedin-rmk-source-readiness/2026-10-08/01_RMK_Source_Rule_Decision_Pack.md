# 01 · RMK source rule — decision pack for Bảo

Status: DRAFT_FOR_PO_DECISION. No live action. Source of the facts below: [data plan](../../LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md) (source registry, pool check, release gate), [Build Pack](../../../ads/linkedin/LinkedIn_Build_Pack.md) and [remarketing proof plan](../../LinkedIn_Remarketing_Proof_Plan.md).

## What is already decided
- Source = members who interacted with the exact **new cold release** (campaign, ad set and creative IDs). Not the Digiwin Page pool, not organic, not website visits or Insight Tag, not unrelated campaigns, and no silent union of pools.
- Cold needs no pre-existing warm pool. RMK is released only when the exact source is Ready and eligible.
- Native RMK needs at least **300 reachable members after filters, as shown in the UI** (figure from the project documents; the actual platform minimum was not re-verified here).
- Pool size cannot be forecast from CTR × reach, and engagements are not unique people.

## Decisions needed (5)

| # | Decision | Options | Proposed |
|---|---|---|---|
| R1 | Interaction rule | **A** Any interactions (proposed default in the data plan) · **B** Chargeable clicks only · **C** Document view/download (only if Document is chosen; Bảo did not choose Document, so not applicable) | **A** for week 1 |
| R2 | Lookback window | **30 days** (data plan default) · longer window | **30 days**; longer windows only after checking which options the UI offers (not verified) |
| R3 | Pool structure | One pool per compatible source cohort · one pool per creative or scenario | **One pool per compatible cohort**; keep per-creative metrics for reading, do not split into 11 tiny pools at the start |
| R4 | RMK objective | Engagement · click to the reader | Decide at release; both recorded as reasonable, neither verified as releasable |
| R5 | Source owner | Bảo or a named delegate | Bảo (owns paid ads and measurement) |

## Trade-offs (qualitative; no numbers are known)
- **A (any interactions, 30d):** widest definition, so most likely to reach the 300 gate on a small budget; mixes strong and weak signals, so RMK relevance is less certain. Definition of "any interaction" must be read from the UI when the audience is created.
- **B (chargeable clicks):** stricter intent and cleaner signal; much smaller pool, so it may never pass 300 with the first-wave budget. Treat as a separate pool if volume allows, never as a replacement silently.
- **Longer lookback:** raises pool size but reaches older, colder interactions; it also weakens the link to the current week's message.

## Recommendation
Choose **A with exact new cold source IDs, 30 days**, one pool per compatible cohort. Check at eligible delivery day 3 and 7, then weekly (cadence from the data plan, not a scheduler). If the pool is below the gate, follow [03_RMK_Fallback_Decision_Tree.md](03_RMK_Fallback_Decision_Tree.md) instead of widening the source on your own.

## What this decision unblocks
Filling [02_RMK_Source_Registry_Template.md](02_RMK_Source_Registry_Template.md) the moment real cold IDs exist; nothing else in the RMK route can be fixed before the cold campaign is created.

## Unknowns that remain
- Cold campaign, ad set and creative IDs: NOT CREATED. Spend, impressions, engagements and RMK member counts: UNKNOWN.
- Lookback options, exact "any interaction" definition and the 300 minimum in the live UI: not re-verified.
- Whether the first-wave budget produces enough interactions: UNKNOWN until delivery.

Stop condition: if Bảo prefers not to decide before the cold results exist, keep option A as the documented default and revisit at the day 3 check.
