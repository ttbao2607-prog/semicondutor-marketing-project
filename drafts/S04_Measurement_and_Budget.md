# S04 — Measurement & budget draft

**Status:** draft only; no tracking/account mutation and no live budget  
**Owner:** Executor in this batch  
**Objective:** define evidence layers, candidate measurement semantics, reconciliation rules and budget/pacing options without inventing a budget amount or requiring new events before inventory.

## Source boundary

- Local: kickoff §§6–9 and source brief “Digital Ads — Bảo”.
- Public official context: Google Analytics engagement-rate definition, https://support.google.com/analytics/answer/12195621 (accessed 2026-09-11); Google Ads primary/secondary conversion guidance, https://support.google.com/google-ads/answer/11461796 (accessed 2026-09-11); LinkedIn audience documentation listed in S03.
- Google Campaigns, Ad groups, Settings and Keyword Planner were observed accessible/functional in sanitized read-only evidence. Keyword Planner returned six supplied English OSAT seed rows without displayed metrics: `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`; no demand is validated. No GA4, LinkedIn, GTM, form receiver, CRM or Ladipage UI evidence was added here.

## Fact / proposal / unknown

**Facts:** kickoff requires separate reach, attention, progression, cost and optional commercial signals. The earlier working-rate and channel-split proposal was `1,000,000 VND/eligible paid day`, with LinkedIn `600,000 VND/day`, Google `250,000 VND/day`, and reserve/retargeting `150,000 VND/day`; this split remains unapproved. Bảo's dated 35m Scale-1 ceiling over 56 calendar days, with at most 35 eligible paid days at that historical rate, is reconciled below. This is not spend authorization. Paid-day dates and tax/fee basis remain pending. Existing tags/events must be inventoried before reuse or change.

**Proposal:** use a layered scorecard and one reconciliation table, with targets provisional until account, traffic, audience and budget baselines exist.

**Known deployment boundary (2026-09-26):** the three approved landing routes are published and their PopupX modal-opening checks pass. Phase 4 Preview verified section dispatch and the exact-route copy-listener exclusion on all three routes. Phase 5 Chrome-controlled tests now cover real focus/visibility transitions, section re-entry, attention timing and real pagehide on all three routes at desktop and 390×844; bounded GA4 requests contained the existing section events. These visits are test traffic, not delivery data. The authenticated GTM workspace opened Tag Assistant Preview without another login; its OSAT summary showed an existing LinkedIn InsightTag firing. That is observed website behavior, not a dependency for native Campaign Manager delivery, and its website purpose/consent behavior were not revalidated or changed. GTM Version 51 remains `Live, Latest`; the three Semiconductor micro-events are not GA4 key events or Google Ads conversion actions. Bảo confirmed there is no cookie-accept mechanism in the current paid-ad landing flow and excluded consent-behavior verification from Phase 5; no allowed/denied behavior is claimed. **Unknown / not ready to claim:** any later LinkedIn delivery (native delivery metrics will be read in Campaign Manager after delivery; no Insight Tag is needed for those in-platform metrics), GA4 campaign attribution, account timezone, delivery dates, tax/fee basis and final management approval of the planning envelope. Website conversions or website-audience retargeting via LinkedIn would require separate scope approval and Insight Tag assessment. Phase 5 is `PASS WITH SCOPE EXCLUSION` for the three routes; this draft does not authorize account changes or spend.

Production handoff: `../tracking/Semiconductor_Tracking_Contract.md` and `../operations/Pre_Ad_Readiness_Plan.md`.

As of 2026-09-24, Phase 2 local source instrumentation is implemented on OSAT, Fabless and Supplier/Partner. Each emits only section-view and bounded section-engagement events; Supplier has one inert header CTA by Product Owner exception, and no route emits CTA or content-click events. Source tests and offline bridge compatibility pass. This does not prove live browser dispatch, consent behavior, accepted forms, brand recall, or campaign performance. The Phase 1 live GTM/GA4 inventory still requires refresh before any account change.

## KPI register

| Layer | Metric | Source | Scope / denominator | Baseline | Target status | Action / review | Limitation |
|---|---|---|---|---|---|---|---|
| Audience | Target-account exposure / coverage observed | LinkedIn UI/export if available | Exposed target companies / fixed target universe; only where identities connect | Unknown | Provisional after S03 | Review after 5–7 delivery days | Hidden/incomplete company data; not unique people |
| Delivery | Reach and frequency | Native platform | Platform and same period separately | Unknown | Provisional | Check weekly | Do not sum unique reach across platforms |
| Search relevance | Relevant-query clicks / observed-query clicks | Google search-terms export | Explicit query sample and rubric | Unknown | Provisional | Review after sufficient query sample | Visible query set is not all demand |
| Attention | Paid landing sessions, engaged sessions, engagement rate | Existing analytics if verified | Same source/route/filter; engagement rate = engaged sessions / sessions per tool definition | Unknown | Provisional | Check tracking first, then 5–7 days | Behavioral proxy, not awareness lift or qualified audience |
| Expertise interest | Proof interaction rate | Analytics/asset telemetry if existing and verified | Defined proof interaction sessions / paid landing sessions | Unknown | Provisional | Review by route/pain | Must define interaction; cannot imply comprehension |
| Progression | CTA intent, successful form submission (event name pending), booking confirmed | Analytics + receiver/native system | Each step separately | Unknown | Provisional | Verify live owner/name; any receiver test requires authorization | CTA intent is not form success; form success is not booking |
| Cost | Spend, CPM, CPC, cost per engaged session | Native platform + reconciled spend | Same platform/tactic/period; cost per engaged session uses matching source and denominator | Unknown | No numeric target yet | Pacing weekly | Attribution and consent limitations |
| Commercial optional | End-user/partner lead and follow-up status | Lead receiver/owner | Only accepted records and stated qualification fields | Unknown | Not mandatory | Review if implemented | Do not infer role or quality from reading behavior |

## Candidate tracking semantic contract

### Proposed decision KPI dictionary (2026-09-29)

The first seven *eligible delivery* days are a technical and destination check, not a statistical claim about demand or audience fit. Record calendar dates and actual eligible days separately. All baselines below are `unknown` until real, same-scope campaign delivery exists. Floors and decision thresholds in S04A are proposals pending Bảo's approval; missing or hidden data means `insufficient evidence`.

| KPI | Numerator / denominator and scope | Source; baseline | Proposed sufficiency and cadence | Limitation / decision use |
|---|---|---|---|---|
| Technical integrity | Count of unresolved critical route, claim, duplicate, privacy, URL or receiver defects; no rate | Route QA, GTM/GA4 and receiver evidence as authorized; current campaign baseline unknown | Check before delivery and during first 7 eligible days; proposed zero-open-critical gate | Synthetic route tests establish technical behavior only, not paid performance. |
| LinkedIn target distribution | Delivered impressions in reported target company/function/seniority cells / all impressions with the same available breakdown; report unclassified share | Campaign Manager; unknown | Compare weekly on unchanged audience configuration; proposal requires two comparable weekly snapshots | Reported cells may be hidden; no claim of person-level identity or total account coverage. |
| LinkedIn reach/frequency | Native unique reach; impressions / native reach, same campaign and period | Campaign Manager; unknown | Weekly after actual delivery | Do not add unique reach across platforms or equate impressions with people. |
| Search observed-query relevance | Clicks on visible search terms classified relevant by a prewritten rubric / clicks on all visible classified terms; also report visible-term clicks / total Search clicks when available | Google Ads search-terms and campaign click reports; unknown | Inspect during first 7 eligible days; **proposed** 20 observed classified clicks before using relevance rate for allocation, with sample and coverage disclosed | Hidden terms prevent an all-query claim; 7 relevant of 10 clicks is descriptive only, not a sufficient decision sample. |
| Core Search impression share | Eligible impressions received / estimated eligible impressions for the explicitly scoped core term set | Google Ads Search impression-share report, if exposed; unknown | Weekly once core terms and eligibility are stable | Missing estimate is unknown, not zero demand; compare like settings only. |
| Paid landing engagement | Engaged paid sessions / paid landing sessions, same source, route, language/variant, timezone and period | Verified GA4 paid-session report; unknown | Proposed 100 sessions per route/variant for first comparison; weekly | Behavioral attention proxy, not audience qualification or awareness lift; zero sessions makes rate undefined. |
| Cost per engaged session | Reconciled media spend attributable to the same paid slice / engaged paid sessions for that slice | Platform spend plus verified GA4 attribution; unknown | Weekly only when matching attribution and nonzero denominator are available | Platform and GA4 windows can disagree; disclose unmatched spend/sessions. |
| Proof interaction | Paid sessions with one defined proof/content action / paid landing sessions in the same slice | Verified existing event or asset telemetry; unknown | Define action first; proposed 100 sessions per compared slice; weekly | Interaction does not prove comprehension or permission to use the claim. |
| CTA / accepted lead / booking | Three separate counts or rates: CTA intents / paid sessions; receiver-accepted records / attributable paid sessions; confirmed bookings / accepted records | Governed route event (OSAT only where verified), provider/receiver, booking source; all baselines unknown | Weekly only for individually verified sources; no minimum decision floor yet | CTA intent is not PopupX opening, form acceptance or booked meeting. No synthetic/test record enters campaign result. |
| Pacing and reserve | Actual media spend / approved period ceiling; remaining ceiling = approved ceiling − actual media spend | Reconciled native platform bills; no approved baseline/envelope yet | Weekly and before any proposed allocation change | Draft ceiling is not authority; tax/fee inclusion and eligible days must be fixed first. |

Source, numerator, denominator, route/segment/language, date window, currency, timezone, attribution window, reporting latency and missing/hidden share travel with each reported KPI. A zero denominator yields `not calculable`. No provisional threshold is a live bidding goal or approval to create an event.

| Semantic | Candidate condition | Required validation |
|---|---|---|
| `landing_view/session` | Correct paid destination loads; page view not duplicated | Route, tags, consent, duplicate check |
| `content/proof_interaction` | Defined opening/view/interaction on a proof asset | DOM/asset behavior and scope |
| `cta_click` | Click on typed CTA with action label | Correct destination and UTM persistence |
| Successful form submission (event name pending; semantic KPI only) | Receiver accepts and stores a marked test record, only after authorization and live event-owner/name verification | Confirm actual LadiPage/editor + GTM/GA4 source/name, receiver acceptance/storage, and success/error/refresh behavior; do not assume or synthesize `accepted_form` |
| `booking_confirmed` | External/native confirmation exists | Source of truth and attribution join |

These are candidate semantics, not an instruction to create events. Reuse existing names after inventory; do not create a new taxonomy solely for naming convenience.

The reviewed local technical-document inventory does not substantiate an `accepted_form` event. The successful-submit KPI has no assigned event name here. Do not test receiver acceptance/storage until specifically authorized and the live LadiPage/editor and GTM/GA4 event owner/name have been verified.

## UTM, source and reconciliation policy

- Keep campaign, route, segment, pain and creative identifiers distinguishable without PII.
- Decide whether stored source means last submit or first touch; do not mix silently.
- Keep click IDs/UTMs through redirect and form handoff where the existing route supports it.
- Reconcile platform spend and receiver records separately from analytics attribution; report timezone, currency, window, latency and missing/hidden data.
- GA4 engagement rate, Google bidding goals and LinkedIn objective are separate configurations. A candidate micro-event is not automatically a bidding goal.

## Budget and pacing options

### Calendar and ceiling reconciliation (options, no selected envelope)

| Source shape | Eligible days and arithmetic at the stated daily reference | Interpretation |
|---|---|---|
| Earlier main S04A/S04B phase proposal | 7 + 14 + one Scale-1 cycle of 7 = 28 eligible days at up to 1,000,000 VNĐ/day = **28,000,000 VNĐ**; separate first 7 Scale-2 days at up to 1,250,000 VNĐ/day = **8,750,000 VNĐ** after new approval | **36,750,000 VNĐ** combined former proposal; the one-cycle scope is superseded for the current ceiling decision, not historical evidence of spend. |
| Older local-only workbook `ff493a7` under `docs/plans/` | `01_Thiet_lap` D13=7, D14=14, D15=7, D16=2; `02_Lo_trinh` G1+G2+G3.1+G3.2 = `7+14+7+7=35` eligible days × 1m = **35,000,000 VNĐ**. G4 separately `7×1.25m=8,750,000 VNĐ`. | Workbook is the verified source of the **35,000,000 + 8,750,000 = 43,750,000 VNĐ** reference also repeated in Vy's email; it is local-only and never itself spend authority. |
| Bảo's 2026-09-29 ceiling decision | **35,000,000 VNĐ through Scale 1 across eight calendar weeks (56 calendar days)**; at 1m/day, full use permits at most 35 eligible paid days. First Scale-2 7 days/8.75m stays a separate approval. | Exact eligible-day dates and phase placement remain to design/approve. Eight calendar weeks are not 56 paid days. Reserve inside the daily ceiling is capacity, not required spend. |

The earlier 28m proposal and workbook 35m model had different Scale-1 cycle counts; Bảo has now selected the 35m **planning ceiling** over eight calendar weeks. The 56-day email schedule is interpreted as calendar duration under that decision, not 56 eligible delivery days or a 56m budget. Bảo still must approve the phase/day schedule, reserve treatment, tax/fee basis and any operational spend mandate; Scale 2 remains separately gated. Proposed Search underspend rule: if relevant query volume cannot absorb its bucket, keep unspent funds unspent and record the variance; transfer to LinkedIn only with an evidence-backed allocation decision within an approved envelope. Do not widen keywords merely to spend.

Earlier daily working-rate proposal: `1,000,000 VND/eligible paid day`, split LinkedIn `600,000 VND/day`, Google Search `250,000 VND/day`, and reserve/retargeting `150,000 VND/day` (**channel allocation unapproved**). The current decision is the dated 35m Scale-1 planning ceiling across 56 calendar days with at most 35 eligible paid days, as reconciled above; exact paid-day dates and tax/fee basis remain pending. Neither the ceiling nor the proposed split is approval to spend or change any live budget.

| Option | Planning shape | Use when | Risk / decision needed |
|---|---|---|---|
| A — current planning split | LinkedIn 600k/day; Google Search 250k/day; reserve/retargeting 150k/day | Planning only; dates and tax/fee basis remain pending | Draft; management approval pending; not spend authorization |
| B — demand-constrained | Hold some or all of the 150k/day flexible reserve until Search query evidence or retargeting eligibility exists | Search volume/fit or retargeting audience is uncertain | Any reallocation requires approval; slower learning |
| C — single-route learning | Propose concentrating a limited tranche on one OSAT route, then review | Budget is small or proof/route is narrow | Requires a separately approved allocation and route/measurement readiness |

Pacing controls to be filled after discovery: delivery dates, spend curve, review cadence, pacing-ratio threshold, max change per review, pause authority and budget-remaining formula. Do not divide the envelope mechanically across channel × segment × pain × format.

## Acceptance, dependencies and L2

**Acceptance:** KPI register has source, scope/denominator, baseline-or-unknown, target/provisional status, action/review rule and limitation; candidate semantics, reconciliation rules and the pending-approval planning split are explicit.

**Dependencies:** S00 inventory; S01 message/route; S02 query evidence; S03 audience evidence; management approval of the envelope, dates/tax basis and a separate operational mandate before implementation.

**L2 decision pack:** confirm the planning envelope, delivery dates, tax/fee basis, route, form/receiver scope, objective/bidding posture, pacing limits and permissions for any publish/enable/pause action.

**Stop:** no tag/event/container setup, no form submit, no account edit, no budget change and no live KPI claim.
