# S04 — Measurement & budget draft

**Status:** draft only; no tracking/account mutation and no live budget  
**Owner:** Executor in this batch  
**Objective:** define evidence layers, candidate measurement semantics, reconciliation rules and budget/pacing options without inventing a budget amount or requiring new events before inventory.

## Source boundary

- Local: kickoff §§6–9 and source brief “Digital Ads — Bảo”.
- Public official context: Google Analytics engagement-rate definition, https://support.google.com/analytics/answer/12195621 (accessed 2026-09-11); Google Ads primary/secondary conversion guidance, https://support.google.com/google-ads/answer/11461796 (accessed 2026-09-11); LinkedIn audience documentation listed in S03.
- Google Campaigns, Ad groups, Settings and Keyword Planner were observed accessible/functional in sanitized read-only evidence. Keyword Planner returned six supplied English OSAT seed rows without displayed metrics: `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`; no demand is validated. No GA4, LinkedIn, GTM, form receiver, CRM or Ladipage UI evidence was added here.

## Fact / proposal / unknown

**Facts:** kickoff requires separate reach, attention, progression, cost and optional commercial signals. The current planning envelope is `1,000,000 VND/day`, marked **DRAFT / MANAGEMENT APPROVAL PENDING**, with LinkedIn `600,000 VND/day`, Google `250,000 VND/day`, and reserve/retargeting `150,000 VND/day`. This is not spend authorization. Dates and tax/fee basis remain pending. Existing tags/events must be inventoried before reuse or change.

**Proposal:** use a layered scorecard and one reconciliation table, with targets provisional until account, traffic, audience and budget baselines exist.

**Unknown:** domain/landing route, current tags, event names, duplicate firing, consent behavior, attribution windows, form receiver, account timezone/goals, delivery dates, tax/fee basis and final management approval of the planning envelope.

Production handoff: `../tracking/Semiconductor_Tracking_Contract.md` and `../operations/Pre_Ad_Readiness_Plan.md`.

## KPI register

| Layer | Metric | Source | Scope / denominator | Baseline | Target status | Action / review | Limitation |
|---|---|---|---|---|---|---|---|
| Audience | Target-account exposure / coverage observed | LinkedIn UI/export if available | Exposed target companies / fixed target universe; only where identities connect | Unknown | Provisional after S03 | Review after 5–7 delivery days | Hidden/incomplete company data; not unique people |
| Delivery | Reach and frequency | Native platform | Platform and same period separately | Unknown | Provisional | Check weekly | Do not sum unique reach across platforms |
| Search relevance | Relevant-query clicks / observed-query clicks | Google search-terms export | Explicit query sample and rubric | Unknown | Provisional | Review after sufficient query sample | Visible query set is not all demand |
| Attention | Paid landing sessions, engaged sessions, engagement rate | Existing analytics if verified | Same source/route/filter; engagement rate = engaged sessions / sessions per tool definition | Unknown | Provisional | Check tracking first, then 5–7 days | Behavioral proxy, not awareness lift or qualified audience |
| Expertise interest | Proof interaction rate | Analytics/asset telemetry if existing and verified | Defined proof interaction sessions / paid landing sessions | Unknown | Provisional | Review by route/pain | Must define interaction; cannot imply comprehension |
| Progression | CTA click, accepted form, booking confirmed | Analytics + receiver/native system | Each step separately | Unknown | Provisional | Reconcile weekly | Click is not accepted form; form is not booking |
| Cost | Spend, CPM, CPC, cost per engaged session | Native platform + reconciled spend | Same platform/tactic/period; cost per engaged session uses matching source and denominator | Unknown | No numeric target yet | Pacing weekly | Attribution and consent limitations |
| Commercial optional | End-user/partner lead and follow-up status | Lead receiver/owner | Only accepted records and stated qualification fields | Unknown | Not mandatory | Review if implemented | Do not infer role or quality from reading behavior |

## Candidate tracking semantic contract

| Semantic | Candidate condition | Required validation |
|---|---|---|
| `landing_view/session` | Correct paid destination loads; page view not duplicated | Route, tags, consent, duplicate check |
| `content/proof_interaction` | Defined opening/view/interaction on a proof asset | DOM/asset behavior and scope |
| `consultation_cta_click` | User activates the landing CTA; route handler invokes the LadiPage-owned `OpenformWF2` trigger if present | One trigger click; intent only; no form/lead inference |
| `accepted_form` | LadiPage-owned popup/receiver accepts and stores a submission under its existing acceptance condition | Existing success/error/refresh behavior and owner; do not alter semantics from the CTA handler |
| `booking_confirmed` | External/native confirmation exists | Source of truth and attribution join |

These are candidate semantics, not an instruction to create events. Reuse existing names after inventory; do not create a new taxonomy solely for naming convenience.

## UTM, source and reconciliation policy

- Keep campaign, route, segment, pain and creative identifiers distinguishable without PII.
- Decide whether stored source means last submit or first touch; do not mix silently.
- Keep click IDs/UTMs through redirect and form handoff where the existing route supports it.
- Reconcile platform spend and receiver records separately from analytics attribution; report timezone, currency, window, latency and missing/hidden data.
- GA4 engagement rate, Google bidding goals and LinkedIn objective are separate configurations. A candidate micro-event is not automatically a bidding goal.

## Budget and pacing options

Planning envelope: `1,000,000 VND/day` (**DRAFT / MANAGEMENT APPROVAL PENDING**), split LinkedIn `600,000 VND/day`, Google Search `250,000 VND/day`, and reserve/retargeting `150,000 VND/day`. Dates and tax/fee basis are pending. This planning envelope is not approval to spend or change any live budget.

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
