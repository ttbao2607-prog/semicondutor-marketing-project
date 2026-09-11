# S04 — Measurement & budget draft

**Status:** draft only; no tracking/account mutation and no live budget  
**Owner:** Executor in this batch  
**Objective:** define evidence layers, candidate measurement semantics, reconciliation rules and budget/pacing options without inventing a budget amount or requiring new events before inventory.

## Source boundary

- Local: kickoff §§6–9 and source brief “Digital Ads — Bảo”.
- Public official context: Google Analytics engagement-rate definition, https://support.google.com/analytics/answer/12195621 (accessed 2026-09-11); Google Ads primary/secondary conversion guidance, https://support.google.com/google-ads/answer/11461796 (accessed 2026-09-11); LinkedIn audience documentation listed in S03.
- No GA4, Google Ads, LinkedIn, GTM, form receiver, CRM or Ladipage UI evidence was observed.

## Fact / proposal / unknown

**Facts:** kickoff requires separate reach, attention, progression, cost and optional commercial signals; `B_media` has no amount; existing tags/events must be inventoried before reuse or change.

**Proposal:** use a layered scorecard and one reconciliation table, with targets provisional until account, traffic, audience and budget baselines exist.

**Unknown:** domain/landing route, current tags, event names, duplicate firing, consent behavior, attribution windows, form receiver, timezone/currency, account goals and actual budget.

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
| `cta_click` | Click on typed CTA with action label | Correct destination and UTM persistence |
| `accepted_form` | Receiver accepts and stores a marked test record | Success/error/refresh behavior and owner |
| `booking_confirmed` | External/native confirmation exists | Source of truth and attribution join |

These are candidate semantics, not an instruction to create events. Reuse existing names after inventory; do not create a new taxonomy solely for naming convenience.

## UTM, source and reconciliation policy

- Keep campaign, route, segment, pain and creative identifiers distinguishable without PII.
- Decide whether stored source means last submit or first touch; do not mix silently.
- Keep click IDs/UTMs through redirect and form handoff where the existing route supports it.
- Reconcile platform spend and receiver records separately from analytics attribution; report timezone, currency, window, latency and missing/hidden data.
- GA4 engagement rate, Google bidding goals and LinkedIn objective are separate configurations. A candidate micro-event is not automatically a bidding goal.

## Budget and pacing options

Let `B_media` be Bảo’s confirmed media envelope. No currency or absolute amount is available.

| Option | Planning shape | Use when | Risk / decision needed |
|---|---|---|---|
| A — awareness-first | LinkedIn 0.60 × `B_media`; Google Search 0.25 × `B_media`; flexible 0.15 × `B_media` | Audience and format are usable; Search has enough relevant demand | Must not be treated as approved allocation |
| B — demand-constrained | Hold more of the flexible amount until Search query evidence or retargeting eligibility exists | Search volume/fit or retargeting audience is uncertain | Slower learning; Bảo chooses release rule |
| C — single-route learning | Concentrate a limited first tranche on one OSAT route, then review | Budget is small or proof/route is narrow | Requires route and measurement readiness |

Pacing controls to be filled after discovery: delivery dates, spend curve, review cadence, pacing-ratio threshold, max change per review, pause authority and budget-remaining formula. Do not divide the envelope mechanically across channel × segment × pain × format.

## Acceptance, dependencies and L2

**Acceptance:** KPI register has source, scope/denominator, baseline-or-unknown, target/provisional status, action/review rule and limitation; candidate semantics and reconciliation rules are explicit; options use `B_media` only.  
**Dependencies:** S00 inventory; S01 message/route; S02 query evidence; S03 audience evidence; Bảo’s budget envelope and operational mandate before implementation.  
**L2 decision pack:** confirm `B_media`, currency/tax basis, route, form/receiver scope, objective/bidding posture, pacing limits and permissions for any publish/enable/pause action.  
**Stop:** no tag/event/container setup, no form submit, no account edit, no budget change and no live KPI claim.
