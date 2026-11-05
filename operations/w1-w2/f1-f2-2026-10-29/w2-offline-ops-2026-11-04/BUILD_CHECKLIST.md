# W2 F2 build checklist — expected values only

04/11/2026 · OFFLINE_ONLY / NOT_CREATED. Owner: Codex prepares; Bảo decides release; live operator PENDING. All saved-state observations below are **NOT_READ** in this task. Check boxes are uncompleted actions for a later authorized operator.

## Exact creative and destination

| Field | Expected candidate value | Later saved-state evidence |
|---|---|---|
| Ad key | `LI-wave02-F2-en-COLD-v2` | NOT_READ |
| Artwork | [f2-cold-hook-v2-candidate.png](../../../../deliverables/linkedin-w2-hook/2026-11-04-f2-v2/assets/f2-cold-hook-v2-candidate.png), 1254×1254 PNG | NOT_READ |
| Artwork SHA256 | `41fd350c889bc2d253155d364d98e70079403b460df0b52ce143b9686cc3ca3b` | NOT_READ |
| Copy | [candidate-copy.json](../../../../deliverables/linkedin-w2-hook/2026-11-04-f2-v2/candidate-copy.json), card `COLD-FABLESS-B16` | NOT_READ |
| Copy SHA256 | `9d30c232acc4606c3e168e3639321ba41108460eb98705837d17fa449045213a` | NOT_READ |
| Caption | We provide manufacturing ERP (enterprise resource planning). Fabless (chip design without owning a fabrication plant) planning teams: demand changed. Which partner lot reports need review before replanning? | NOT_READ; 206 characters expected |
| Artwork/native headline | Demand changed. Are your lot reports current? | NOT_READ; 45 characters expected |
| Alt | Illustration: Demand changed. Are your lot reports current? | NOT_READ |
| Artwork body | Before replanning, check the product, planning period and partner lot reports. | NOT_READ |
| Artwork labels | Fabless planning; Manufacturing ERP; one existing Digiwin logo | NOT_READ |
| Platform CTA | Learn more; verify actual availability and preview | NOT_READ |
| Reader query | `t=F2&lang=en` | NOT_READ |
| UTM source / medium | `linkedin` / `paid_social` | NOT_READ; saved parameter precedence/duplicates unresolved |
| UTM campaign / content | `fdi_f2_en_cold_wave01` / `f2_cold_v2` | NOT_READ |

Exact proposed URL (not tested online in this task):

```text
https://solutions.digiwin.com.vn/semiconductor-case-reader?t=F2&lang=en&utm_source=linkedin&utm_medium=paid_social&utm_campaign=fdi_f2_en_cold_wave01&utm_content=f2_cold_v2
```

Use the matching row in [BUILD_PROPOSAL.csv](../w2-hook-candidate-2026-11-04/BUILD_PROPOSAL.csv). URL campaign remains the existing journey grouping; native wave02 naming does not rename it. Inventory URL parameters at every exposed saved hierarchy level before save. Report the known `linkedin`/`LinkedIn` conflict to Bảo for disposition; this document fixes only local proposal metadata. Do not silently change live attribution settings.

## Account / hierarchy / targeting expected from the existing proposal

| Field | Expected / proposed | Observed saved value |
|---|---|---|
| Business Manager / account | DigiwinSoft ASEAN BM / DigiwinSoft_SEA_Performance_Bao | NOT_READ; verify identity first |
| Parent | Existing suitable parent; exact object and budget hierarchy PENDING readback | NOT_READ |
| W2 ad set | Proposed `REVIEW_R5_EN_F2_HOOK_WAVE02_RELEASE_PENDING`; exact final name/state PENDING | NOT_READ |
| Objective / bidding | Brand awareness / Reach / Maximum delivery as existing proposal; verify native labels | NOT_READ |
| Company list | TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52 | NOT_READ |
| Location / language | Vietnam recent/permanent / English | NOT_READ |
| Functions | Engineering OR IT OR Operations OR QA | NOT_READ |
| Seniority | Manager OR Director OR VP OR CXO | NOT_READ |
| Boolean relationship | R5 AND location/language AND function group AND seniority group; no Industry addition | NOT_READ |
| Expansion / placements | Expansion off; Feed only; LAN off; Right Rail off | NOT_READ |
| Advertiser identity | Existing authorized Digiwin Page; resolve exact saved Page privately | NOT_READ |
| Budget / dates / timezone | PENDING Bảo decision and saved-control verification | NOT_READ |

If native hierarchy cannot isolate the proposed spend, record the actual constraint and return to Bảo. Do not create an alternative campaign or widen the audience from this checklist. Old eligibility/mapping observations do not prove current delivery or buyer fit.

## Proposed object lifecycle — no action authorized here

| Object | Current evidence | Intended later state, only after exact mandate |
|---|---|---|
| Existing W1 F1 and F2 / shared ad set | On/Active in 04/11 historical readback; current state NOT_READ | Preserve W1 schedule/history; verify actual end and spend; no rewrite, extension or automatic re-enable |
| New W2 ad set / F2-v2 | NOT_CREATED | One candidate only, separately identifiable after W1; any draft/Off build, save, upload, enable and funded start require explicit scope |
| Other funded objects | NOT_READ; account-wide inventory not performed | No unapproved overlapping W1/W2 funding; report other spend without modifying unrelated objects |
| RMK | HOLD | No attachment/edit/new pool; new W2 source coverage is not assumed from W1 |

- [ ] Close P1 and final W1 gaps; record lag and saved schedule/budget hierarchy.
- [ ] Obtain exact candidate acceptance, including semantic visual preservation rather than pixel identity, and complete [release decision](RELEASE_DECISION.md).
- [ ] Under a future build mandate, inspect native headline/alt/artwork/CTA/link preview at desktop/mobile; record rejection/eligibility limits.
- [ ] Save/reopen only within that mandate; compare every expected field with actual persisted state and final URL parameters.
- [ ] Under a future release mandate, verify actual start/stop and first delivery; use [readback template](READBACK_TEMPLATE.md). Budget or integrity drift is escalated using [incident cards](../pre-readback/INCIDENT_CARDS.md).

Rollback proposal: Bảo-authorized pause of the affected W2 scope, preserving W1 sources/history. Returning to old F2 requires a new bounded mandate and budget; no automatic restart. Audit evidence in Git must use stable keys and sanitized facts, without raw IDs, account URLs, member/lead data or credentials.
