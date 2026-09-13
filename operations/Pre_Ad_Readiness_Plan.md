# Pre-Ad Readiness Execution Plan

**Status:** PLAN APPROVED / EXECUTION ACTIVE / LAUNCH NOT AUTHORIZED
**Revision:** 2026-09-13 · Asia/Ho_Chi_Minh
**Revision note:** Recorded fresh Coordinator-reported Google Ads Overview modal evidence and corrected branch provenance; no operational approval gates or budget changed.
**Owner:** Executor leaf, reporting to Coordinator/Auditor
**Canonical branch:** `main` at baseline `393caa365b5a183c72c90e3e2a571e18ca3ebdb2`. **Evidence review slice:** `slice/google-ads-blocker-evidence`, branched from that exact baseline; this branch is not canonical and is not merged.

## 1. Scope and phase end state

This plan covers three segments: OSAT/factories, Fabless commercialization, and semiconductor supplier/partner/SI/automation/materials-equipment.

The phase end state is:

- three reviewed static concepts, one per segment;
- one OSAT document ad with six pages;
- three prospecting LinkedIn audience/ad sets;
- one paused Google Search campaign with three ad groups, retained keywords, negatives and RSA drafts;
- three final LadiPage routes for Google-only traffic;
- tracking contract and QA evidence ready;
- safe remote draft/paused/building object preparation after readiness and applicable UI confirmation.

This plan authorizes preparation of the approved assets/routes and progression to the publication action-time gate. Publication requires the separate action-time confirmation required by Computer Use policy. Campaign enable, launch, spend, lead submission, audience upload and live optimization remain **NOT AUTHORIZED**.

## 2. Decision register

### Approved decisions

- Use Vietnamese-first messaging while retaining necessary English technical terms.
- Use official/company-controlled Digiwin brand assets only.
- LinkedIn is native/in-platform. Do not use LadiPage as LinkedIn’s primary destination; use the official LinkedIn Company Page only if a destination is required.
- Google Search may use the three specified LadiPage routes, subject to final route and publication QA.
- Keep proof mechanism-only unless claims, named cases, numbers, scope and usage rights are independently verified.
- Use shared GTM/GA4 if it exists; do not create a new container or property.

### Assumptions to validate

- The current OSAT HTML draft is a reusable design/content starting point, not a final published route.
- The existing LadiPage Basic import/preview evidence is sufficient to continue draft preparation, but does not prove publication compatibility.
- Existing GA4/GTM event names may be reusable; actual inventory, duplication and ownership remain to be checked.
- The contact-copy CTA can use verified company-controlled contact information without sending the copied value to analytics.

### Deferred mandatory manager decisions (L2 before launch)

- Approved actual budget envelope, including tax/fee basis.
- Campaign date window and timezone/currency confirmation for live delivery.

Publication is an approved scope item that remains gated by action-time confirmation. Other evidence/platform blockers, proof-use issues and material business-scope changes remain stop conditions.

The working `1,000,000 VND/day` figure below is labeled **DRAFT / MANAGEMENT APPROVAL PENDING** and is not an approved budget.

## 3. Workstreams and acceptance

### A — Lock canonical contracts

Lock this plan, brand source, verified contact block, tracking IDs/names after inventory, route names, budget note and revision identifiers.

**Acceptance:** one owner per shared file; no conflicting route/message/tracking definitions; no private account IDs, private URLs, credentials, PII or raw audience exports.

**Stop:** unresolved budget, platform change, proof-rights issue or destination ownership goes to the L2 decision pack.

### B — Prepare assets, audiences, keywords and routes

Prepare the three static concepts, OSAT document ad, LinkedIn audience hypotheses, Google keyword/RSA drafts and three LadiPage final-route candidates. After readiness and applicable UI confirmation, safe remote objects may be created only in draft/paused/building states.

**Acceptance:** every asset maps to one segment, pain, mechanism, CTA and route; claims are verified or explicitly omitted; final copy contains no “draft/internal” language and no live placeholder.

**Stop:** do not enable, launch, spend, submit a form or transmit audience/contact data; publication remains behind its separate action-time confirmation gate.

### C — Freeze DOM and run tracking QA

Freeze page structure and candidate event semantics before QA. Validate event meaning, duplicate prevention, UTM handling, consent behavior and non-PII payloads using marked test data only.

**Acceptance:** route-specific QA record; no CTA duplicate; no copied contact value in telemetry; micro-events remain reporting-only.

**Stop:** unknown container ownership, route mismatch, duplicate event, PII exposure or failed source reconciliation blocks downstream creation.

### D — Publish final routes

After final route QA, publication of the three Google-only routes requires a separate action-time confirmation and explicit publication authority. Publication does not authorize campaign enable or spend.

**Acceptance:** each route is visibly published at the approved destination, responsive, noindex/follow as specified, and passes route/CTA/metadata checks.

**Stop:** no domain, form, tag/container or lead-routing change without explicit mandate.

### E — Create paused Google and LinkedIn objects

After route/asset readiness and any required action-time confirmation, create only the approved paused/draft objects. If platform minimums make the LinkedIn split exceed the envelope, create only the fitting portion and keep the rest import-ready; never increase total draft budget.

**Acceptance:** object structure, targeting, creative, URL, tracking labels and budget note match this plan; no object is enabled or delivering.

### F — Define LinkedIn engagement retargeting

Create the definition for `LI-AUD-P1-ENGAGED-30D` in Building only when the audience source and eligibility are evidenced. Source is single-image/document engagement. This audience is launchable only at `>=300` reachable members, subject to platform/UI evidence.

**Acceptance:** definition and threshold are recorded; no upload or activation occurs in this plan.

### G — Independent S09 QA

Use a reviewer independent from the writer where available. Review business/message/proof, audience/query, route, tracking, budget, status and operational readiness by revision.

**Acceptance:** blockers are separated from notes; page published, campaign active, campaign delivering and data verified are reported as distinct states.

## 4. LinkedIn native/in-platform design

### Segments and creative

Prepare exactly three initial static concepts:

1. **OSAT:** lot genealogy, 4M1E, test data, traceability, WIP and cost-close mechanism.
2. **Fabless:** outsourced WIP, Datecode/BIN/lot, forecast and cost visibility mechanism.
3. **Supplier/partner:** ERP–MES–OT, quality, traceability and integration ownership mechanism.

Prepare one **OSAT document ad with six pages**: pain, operating consequence, data mechanism, traceability flow, cost/quality decision point, and non-form discussion CTA. Use only official/company-controlled Digiwin assets and safe mechanism wording.

### Delivery design

- Objective: **Brand Awareness**.
- No LinkedIn Lead Gen Form.
- Destination: native/in-platform; if a destination is mandatory, official LinkedIn Company Page only.
- Prospecting: three audience/ad sets, one per segment, subject to identity/role availability.
- Audience Expansion: **OFF** baseline.
- LinkedIn Audience Network: **OFF** baseline.
- Retargeting: `LI-AUD-P1-ENGAGED-30D`, single-image/document engagement, Building until evidence shows `>=300`; not launchable before that threshold.

**Dependency:** S01 message/proof map and S03 UI validation of business/account identity, roles, sizes, placements and permissions. No audience upload, message, invitation or enable action is authorized.

## 5. Google Search design

### Campaign and ad groups

- One campaign, status **paused**.
- Ad groups: `OSAT_LOT_TEST`, `FABLESS_OUTSOURCE_WIP`, `ERP_MES_OT_PARTNER`.
- Match types: exact and phrase only.
- Geography: Vietnam presence-only.
- Languages: Vietnamese and English; Vietnamese-first.
- Network: Search Network only.
- Display: **OFF**.
- Search Partners: **OFF**.
- Draft bidding: Maximize Clicks with provisional max CPC `25,000 VND`.
- No conversion-based bidding. Micro conversions are reporting-only and never primary Google Ads conversions.

### Research and creative requirements

Use Keyword Planner and account search-term/overlap evidence when authorized. Retain 8–15 validated keywords per ad group and maintain the negative taxonomy from S02. No volume, CPC, competition, overlap or result claim is valid without observed evidence.

**Current readiness evidence (2026-09-13, Coordinator-reported):** the authenticated Google Ads Overview displayed a “Turn off ad blockers” modal. The Coordinator stopped without dismissing or interacting with it; no Keyword Planner query was made. This is distinct from the orange Vietnamese mechanism-update banner, which remains informational/non-blocking. Fresh Vietnam OSAT, Fabless and ERP–MES–OT/partner research remains pending; the modal's downstream effect is unknown. The six-English-seed no-metrics result remains historical only. No campaign, save, enable or spend action occurred.

Each ad group gets one VN-first RSA with 10–12 headlines and 4 descriptions. Add an English RSA only when English demand evidence exists. Prepare 4 callouts and 3 sitelinks. Final copy must map to the correct segment/pain/route and omit unverified proof.

**Dependency:** S01 message map, S02 validation, S04 measurement contract and final route URLs. No campaign enable, launch, spend or delivery is authorized; safe paused/draft object preparation may proceed after readiness and applicable UI confirmation.

## 6. Google-only LadiPage routes

Final route candidates:

- https://solutions.digiwin.com.vn/osat-lot-test-traceability
- https://solutions.digiwin.com.vn/fabless-outsourced-wip
- https://solutions.digiwin.com.vn/semiconductor-erp-mes-ot

Apply the existing OSAT design direction consistently. Each page must have final Vietnamese-first copy, necessary English technical terms, official Digiwin branding, a contact-copy block, no form, no unverified claims, no draft/internal label, and no live placeholder.

The current offline redesign follows `design-system/MASTER.md` and each route override. Each route has its own static explanatory diagram (OSAT lot trace rail; Fabless outsourced-WIP handoff with ownership to confirm; Partner ERP–MES–OT layer map marked architecture hypothesis) and exactly two primary consultation buttons, in the hero and terminal contact band. OSAT retains only its existing `osat_cta_click` intent candidate with `cta_location=hero|terminal`; Fabless and Partner have no CTA event pending inventory. This is a local design candidate, not import, publication or tracking authorization.

Required metadata and QA: meta title/description, OG metadata, favicon, responsive desktop/mobile behavior, noindex/follow, route integrity and Lighthouse readiness. Publication route and custom HTML compatibility remain subject to direct UI evidence; the existing draft import/preview is not publication proof.

## 7. Contact CTA and tracking contract

Use contact information verified from a company-controlled Digiwin source. Event `copied_contact` may fire only after a successful copy operation. Allowed parameters are exactly `contact_type`, `placement` and `segment`. Never send the copied phone/email/address value to analytics, URLs, ads platforms or evidence.

Tracking rules:

- Reuse shared GTM/GA4; do not create a container/property.
- Keep global `page_view`.
- Reuse `section_view` and `section_engagement_time` after inventory.
- Each of the two consultation buttons invokes `OpenformWF2` no more than once per click. OSAT records its existing hero/terminal intent location; Fabless and Partner emit no CTA event pending inventory.
- Treat micro-events as reporting-only, never primary Google Ads conversions.
- Google UTM: `utm_source=google`, `utm_medium=cpc`, `utm_campaign=vn_semiconductor_search_p1`, `utm_content=<segment>_rsa_<variant>`, `utm_term={keyword}`.
- Preserve auto-tagging and `gclid`.
- Validate consent, redirect, attribution choice, timezone/currency, missing data and receiver reconciliation before implementation.

## 8. Budget and schedule gate

**DRAFT / MANAGEMENT APPROVAL PENDING**

- Working envelope: `1,000,000 VND/day`.
- LinkedIn: `600,000 VND/day`.
- Google: `250,000 VND/day`.
- Reserve/retargeting: `150,000 VND/day`.
- Dates: `SCHEDULE_PENDING`.
- Auto-start/spend: **OFF**.

This is a management planning note, not an approved spend authorization. No actual budget may be inferred until Bảo confirms the envelope, dates and tax/fee basis.

## 9. Dependencies and stop conditions

Critical path: lock message/proof/brand/contact/tracking contracts → finalize three routes and assets → freeze DOM → tracking QA → independent S09 QA → separately authorized publication/object creation. Research and draft preparation may proceed in parallel.

Stop and send an L2 decision pack for: budget envelope or pacing change, platform/destination change, proof/usage-right conflict, account identity/permission uncertainty, PII risk, route mismatch, or any external business trade-off. Publication itself remains an action-time confirmation gate, not a deferred scope decision. Do not add superior approval as a default layer.

Public-repository boundary: no account IDs, private URLs, credentials, cookies, PII, raw audience/lead exports or unverified proof presented as fact.

Responsible roles: Bảo — Product Owner; Coordinator/Auditor — coordination and independent audit; Executor — leaf implementation within mandate, no delegation.
