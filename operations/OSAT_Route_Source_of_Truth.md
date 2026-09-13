# OSAT route — canonical-source candidate

**Status:** draft candidate for review; no live-account or publication authority.
**Owner:** paid executor, reporting to the coordinator. **Revision date:** 2026-09-13 (Asia/Ho_Chi_Minh).

## Evidence classes

1. **User direction / current mandate:** build one OSAT/factory route around 4M1E, lot, test data, traceability, audit, WIP and cost-close mechanisms. The route is mechanism-only until proof, permissions and account inventory are verified.
2. **Local strategy sources:** `Semiconductor_Work_Kickoff.md` v2.0 and `Semiconductor - Website & Ads.md`, plus drafts `S01`–`S04`. These provide message hypotheses and pain vocabulary; named cases, counts and performance claims remain leads pending verification.
3. **Technical evidence (read-only):** the supplied GTM/GA4 notes describe existing event naming and section-tracking patterns. They do not authorize changes to tags, containers, destinations or accounts.
4. **Observed authenticated UI evidence:** the LadiPage HTML-to-LadiPage GUI accepted `osat-route-draft.html` in **Basic** mode, created the clearly named draft, and opened the editor preview. The platform rejected the filename `index.html`, so the byte-identical source was renamed. This evidence covers draft creation/preview only, not publication.

## Sanitized account/UI observations (not public-source evidence)

- Google Ads Campaigns, Ad groups, Settings and Keyword Planner were accessible and functional in sanitized read-only evidence. Existing Search activity has ERP/MES/manufacturing adjacency; no direct OSAT campaign or direct OSAT demand evidence was observed.
- Active Search inventory and search-term availability were observed.
- Google Campaigns, Ad groups, Settings and Keyword Planner were accessible and functional in sanitized read-only evidence. The orange “Xem xét mục tiêu của chiến dịch...” banner is informational and non-blocking. Keyword Planner returned the six supplied English OSAT seed rows under Vietnam/Vietnamese/Google/last 12 months but displayed no search/competition/bid metrics: `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`; this is not a blocker or validated demand. Accessibility/DOM text alone is insufficient for blocker status; future claims require a visibly rendered dialog confirmed by `isVisible()`, reviewed screenshot and actual interaction test.
- No account IDs, private URLs, credentials, cookies, lead records or audience data are recorded in this source.

## Unverified items

- LadiPage publication compatibility, upload size/encoding limits beyond this successful import, and cloud draft identity.
- Account permissions, publication route, domain/URL, form/CRM handoff, consent, tag/container inventory and any proof-use rights.
- All customer names, case outcomes, percentages, savings, delivery/yield figures and capability counts.

## Route artifacts (distinct revisions)

- **Previously imported LadiPage draft:** `osat-route-draft.html` was imported in Basic mode and previewed. This older draft has no contact-copy UI; the observation proves draft/preview only, not publication.
- **Current final offline candidate:** `landing/osat-route/osat-lot-test-traceability.html` is the newer mechanism-only candidate. It contains a contact-copy UI and a candidate `copied_contact` event emitted only after copy success with the approved non-PII parameters. This local candidate has not been imported or published.
- **Form integration ownership:** the locked HTML owns visual layout and the primary consultation CTA only. That CTA invokes `document.getElementById('OpenformWF2').click()` when LadiPage has supplied the external trigger. LadiPage owns popup/form setup, form fields and data storage, and successful-submit behavior/tracking. The imported HTML must never include a visible or hidden form; CTA intent does not mean `accepted_form`. See the runbook for the binding and regression checklist.
- **2026-09-13 import attempt:** Basic mode was selected, but the browser upload bridge rejected the verified worktree path before file transfer because it is outside configured upload roots. No new LadiPage draft was created. This does not change the older draft evidence above. See `LadiPage_Draft_Runbook.md` for scope and stop condition.
- The final candidate connects lot genealogy, 4M1E context, test data, traceability, WIP visibility and cost-close review. It uses no named customer, case, number, percentage, outcome or unverified capability claim, and has no visible or hidden embedded form. Its primary CTA requests a consultation by clicking the separately configured LadiPage popup trigger `OpenformWF2`; a click is intent only, not a lead-success, booking, or accepted-form claim. See the tracking contract and LadiPage runbook for binding requirements.

## Tracking boundary

- The older imported draft and current offline candidate have no hard-coded GTM, GA4, pixel, Ads or other tag ID, make no analytics network request, set no cookie, collect no query parameter and have no form field.
- The current offline candidates contain dataLayer-only candidate events: `section_view`, `section_engagement_time`, `consultation_cta_click` (CTA intent only), and `copied_contact` after successful contact copy. They require actual container inventory and QA before any downstream tag is considered.
- The copied contact value is never part of the event payload. The older imported draft has no contact-copy UI; do not use that older-draft observation to describe the newer offline candidate.
- Do not add tags, containers, IDs or URL parameters as part of this draft or import workflow.

## Sanitized import evidence (2026-09-11)

- Source accepted after platform filename constraint: `osat-route-draft.html`; `index.html` was rejected.
- Mode: **Basic**. Draft title: **DRAFT — OSAT vận hành — mechanism review**.
- Draft creation and editor preview succeeded; the draft remained unpublished.
- Desktop and mobile editor views visibly contained the hero, mechanism cards, operating-view steps, and non-form CTA anchors (`#mechanism`).
- Candidate tracking remains unverified/deployed nowhere: only the source HTML dataLayer helper was inspected; no GTM/GA4/tag/container change was made.
