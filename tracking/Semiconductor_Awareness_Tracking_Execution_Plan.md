# Semiconductor paid — awareness measurement build and audit plan

**Status:** execution design, revised 2026-09-23. Bảo has selected PopupX `modal_openform` for all three Semiconductor routes. No live GTM, GA4, LadiPage, LinkedIn or Google Ads change is authorized by this document. **Owner:** Bảo (Product Owner). **Execution:** one assigned tracking executor per shared surface; independent auditor checks the evidence and reports PASS/BLOCKED. Do not publish tags, pages or campaigns, submit a form, spend, or upload audiences under this planning mandate.

## 1. Decision and source boundary

This is the implementation specification for **awareness first**: exposure in each ad platform, paid visits to the Google landing routes, useful attention to route content, and optional proof interest. Consultation intent and accepted leads are separate progression measures. A click or time on page does not demonstrate brand recall, understanding, qualified demand or form acceptance.

Source precedence for this project: Bảo's current instruction; `Semiconductor_Work_Kickoff.md` v2.0; `Semiconductor - Website & Ads.md`; project `AGENTS.md`, `CURRENT_STATE.md`, `tracking/Semiconductor_Tracking_Contract.md`, `drafts/S04_Measurement_and_Budget.md`, and `operations/Pre_Ad_Readiness_Plan.md`. Technical reference: `G:\Other computers\My Laptop\Documents\GTM-GA4-Technical-Documents\` (`CLAUDE.md`, `digiwin_master_tracking_system.md` §§4, 6, 9, `digiwin_industry_landing_tracking.md` §§0–1, `digiwin_gtm_governance_standard.md` §§1–4, 6, `digiwin_legacy_ldp_funnel_tracking.md`, `debug_log.md`). These files describe July 2026 setup and debugging, **not verified September live state**.

The July docs identify a shared section event catalog and GTM tag, a sitewide page tag, and legacy LadiPage funnel events. The debug log reports GTM Section Tracker version 49 published on 2026-07-23 with blur/focus handling; it also reports unresolved/locally patched Bento and Industry embeds. Those historical statuses cannot be used as proof that the current semiconductor routes receive the same code. The master doc's earlier section sample handles `visibilitychange` but omits `blur`/`focus`; **do not copy that sample verbatim**. Its `potential_viewer` 20-second rule belongs to different sections and is excluded from this build.

**Local audit on 2026-09-23:** `node --test tests/landing-tracking.test.cjs` returned 8 pass / 16 fail. The OSAT/Fabless harness expects the older tracking implementation and canonical link structure, while their current visual sources contain no `dataLayer` dispatch. The passing Partner cases apply only to its current candidate, not a Supplier-ready final route. Do not report source tracking QA as passed for the two ready visuals. Slice C must replace or adapt this harness to the final flat PopupX artifacts and rerun it before account preview.

The master doc describes `generate lead` (space) as a historical GA4 event, but its producer was inferred, not verified. It also describes `form_start` from Enhanced Measurement and a sitewide `text_copy` → `contact_info_copy` listener that can send copied text. None establishes a semiconductor form-success source. The older guidance to mark high-intent events as conversions does not override this project's rule: awareness micro-events remain reporting only and never primary Google Ads conversions.

## 2. Route and channel boundary

| Surface | Source revision to lock | Measurement owner | Current evidence / build decision |
|---|---|---|---|
| LinkedIn Brand Awareness | `ads/linkedin/LinkedIn_Build_Pack.md` | Campaign Manager native reporting | In-platform static/document/carousel activity; no LDP as primary destination. Read reach, frequency, impressions, spend and format engagement from LinkedIn only. No GTM/GA4 event or Insight Tag build for this v1. |
| Google Search → OSAT | Approved visual lineage on local `main` at `bb892e2`; frozen normalized source at `3189b5aff672804b45ca9ae61e08716c849d6cbd` | Google Ads delivery + existing site GA4/GTM + route HTML | The approved Shadow DOM source was flattened with visual/semantic parity; provider-free `flat_document` source has two stable CTA IDs and render anchors. Phase 1 bridge compatibility preflight passed; see route ledger. |
| Google Search → Fabless | Reviewed flat artifact lineage on `slice/fabless-ldp-canonical` at `37ea3e92c8bf52761814c7d939fde1f085e72eb9`; frozen normalized source at `3189b5aff672804b45ca9ae61e08716c849d6cbd` | Same | Legacy adapter/provider trigger residue was removed without changing visible content. Provider-free `flat_document` source has two stable CTA IDs and render anchors; Phase 1 bridge compatibility preflight passed. Earlier `OpenformWF2`, prepared and dogfood receipts remain historical lineage. |
| Google Search → Supplier/Partner | Freeze only after Bảo approves the final LDP revision, then produce/qualify a flat source | Same | Current candidate is not Supplier-ready evidence. Apply the same PopupX modal and tracking contract only after its DOM, two CTA IDs, anchors and content are final. |

There are **two primary consultation buttons per OSAT and Fabless source**, despite `data-consultation-cta` appearing a third time in each file's JavaScript selector. Check actual DOM elements, not raw string counts. Give the two declared PopupX buttons stable, unique IDs in the final flat source and pin those selectors in the bridge manifest. The primary buttons may be in the header/terminal positions; `hero` is the existing OSAT analytics location label, not proof of a physical hero-section position. Do not invent a third CTA. OSAT's supporting demo control is not a declared PopupX primary CTA unless Bảo later changes the route contract.

At the read-only recovery checkpoint before this plan was written, local `main` was clean at `bb892e2`, two commits ahead of its fetched remote-tracking `origin/main`; the Fabless branch contained later local-only commits. This plan and the synchronized canonical-doc edits are now **unstaged working-tree files on this computer only**. A remote-tracking reference is a fetched local snapshot, not proof of a live GitHub page. Future route implementation must use an authorized owned branch/worktree before commit or integration; no Git history change is part of this plan.

## 3. Measurement specification to build

| Layer / KPI | Owner and definition | Build decision | Interpretation |
|---|---|---|---|
| Exposure | LinkedIn: reach, average frequency, impressions, spend by campaign/ad/format and period; Google: impressions, clicks, CTR, spend, search terms where available | Use native platform columns with confirmed timezone/currency. Record the account/object/filter definition. | Exposure/delivery proxies; do not add unique reach across platforms. |
| Audience fit / observed coverage | LinkedIn aggregate company, role/function/seniority delivery when available; observed target companies / fixed, sourced target-company universe only where identities can actually be matched | Record the target-universe revision and visible/missing share; keep account-match eligibility separate from delivery. | Marginal company and role reports do not prove their intersection for a person; hidden companies are unknown, not unexposed. |
| Search relevance | Relevant-query clicks / clicks in the observed search-term set, plus observed-query clicks / all Google Search clicks | Freeze a rubric against OSAT/Fabless/Partner pain and exclude irrelevant/recruitment/student intent; classify each visible term, then count clicks within the visible sample. | Hidden search terms are not zero demand or automatically relevant. |
| Paid landing arrival | Existing global `page_view`, GA4 session/source/medium/campaign and the approved route path; Google Ads landing URL with documented UTM and auto-tagging | Verify one page-view owner and UTM/gclid preservation. **No inline page_view, duplicate Google tag, custom landing_view or URL rewriting.** | Sessions and engaged sessions are site behavior, not awareness lift or ad reach. |
| Section exposure | `section_view` with `section_name` only, once per viewed section per page instance | Reuse existing event name/DLV/GA4 tag after live inventory. Instrument the final **flat document** using frozen section IDs/markers and `rootMargin: '-45% 0px -45% 0px'`. | Count exposed sections; not unique readers or comprehension. |
| Section attention | `section_engagement_time` with `section_name`, integer `engagement_seconds` in 1…3600 | Reuse existing DLV/GA4 tag after inventory. Accumulate only intersection time while document visible and window focused; pause on `visibilitychange`/`blur`, resume on `focus` only when visible, flush once per viewed section on `pagehide`; idempotent initialization. | Report sum of seconds with event count and session denominator; cap/outliers monitored. Do not call seconds a brand-lift measure. |
| Proof/resource interest | **Proposed new** `semiconductor_content_click` with fixed `semi_route` (`osat|fabless|partner`) and `content_id` from a reviewed allowlist | Build **one shared event mapping**, only if inventory finds no existing equivalent with safe semantics. Instrument deliberate proof/resource opens, not every decorative/scroll/navigation click. Do not send link URL, link text, source document title, copied value or dynamic user input. Details below. | An interest signal; never a lead, key event or bidding goal. |
| Consultation progression | OSAT candidate `osat_cta_click` + `cta_location=hero|terminal`; Fabless/Supplier no CTA analytics event in v1 | Enable OSAT candidate only after inventory verifies event/tag ownership and Bảo accepts the exact candidate. Do not derive popup-open or successful-submit from either route's trigger request. | Secondary diagnostic only. |
| Accepted form / booking | Actual LadiPage/receiver and verified live GA4 event owner/name; booking from its own source | Inventory and separately authorized marked test are required. Do not emit `accepted_form`, `Ladi_form_success`, `generate lead`, `generate_lead` or `form_submit` from route HTML. | A native `form_submit` may describe interaction; it is not proof that the receiver accepted a record. |

**Content allowlist rule.** For OSAT v1, eligible existing markers are `hero_proof_casic`, `hero_proof_kyec`, `hero_proof_local`, `resource_S09`, `resource_S13`, `resource_S08`, `resource_S14`. For Fabless v1, eligible existing markers are `relationship_open`, `case_brightpower_open`, `hero_proof_velocity`, `hero_proof_local`, `resource_S02`, `resource_S10`, `resource_S13`, `resource_S15`. These are **selector candidates**, not proof-use approval. During the frozen DOM/proof audit, remove any item whose public claim, link destination, or rights are not cleared; attach one `content_id` value exactly equal to the surviving static marker. Count one actual user activation (mouse, touch or keyboard) per action, not the subsequent anchor scroll, resource load or LadiPage popup. Never send the URL itself. Supplier's list is created from its final approved content; no placeholder event fires before then. If no marker clears, omit this event for that route and record `NOT APPLICABLE — no cleared content`.

**Frozen section IDs to check, not to rename:** OSAT `top`, `operations-questions`, `lot-map`, `management-layers`, `cas-ic-case`, `industry-delivery`, `resources`; Fabless `top`, `operations-questions`, `fabless-map`, `relationship-proof`, `bright-power-case`, `resources`. A differing reviewed artifact requires a revised route manifest before instrumentation. The business label “Supplier” maps to the current Partner route/ad-group terminology and the fixed `semi_route=partner`; do not create both `supplier` and `partner` values for one route.

**No `industry` parameter or `industry_*` event.** That taxonomy is for eight other full-page routes. No new `potential_viewer` or remarketing threshold in v1. Route breakdown for existing section events uses the verified GA4 page path/landing page dimensions; the proposed content event uses `semi_route`. Check whether `semi_route` and `content_id` custom dimensions already exist before creating one event-scoped definition for each. Do not create a custom dimension for `engagement_seconds` if the existing metric works. If a quota/collision prevents the two new dimensions, block the content event report; do not silently replace them or create route-specific GA4 tags.

**Implementation placement.** The final provider-free flat source owns one idempotent observer/click initializer. Keep `window.dataLayer = window.dataLayer || []` local to that initializer and push only the exact event/fields above. Do not embed the PopupX SDK, popup URL, provider ID, physical form reference or form configuration in market HTML; the live operator owns the official SDK and narrow adapter. The shared GTM container receives route pushes through one set of DLVs/triggers/tags. Check the live all-pages Section Tracker's selector/URL scope: if it already reaches the new flat sections, choose exactly one observer owner and prove no duplicate. Do not add one GTM observer/tag per LDP or rewrite a global tracker blindly.

**Bridge receipt integrity.** `canonical-form-bridge` never configures the live form; it prepares and validates the offline `modal_openform` handoff. Its receipt pins the source and prepared artifact hashes. Agents may run an initial bridge compatibility preflight on the flat visual baseline, but any later tracking mutation invalidates that package. After tracking code and tests pass, run `prepare_modal_openform.py` and `validate_modal_openform.py` again from the tracked canonical source. Only this final passed manifest + receipt + exact non-overwriting prepared HTML may be handed to `ladipage-operator`. Never edit the prepared artifact after final validation.

**Skill-runtime preflight — resolved 2026-09-23.** The installed `SKILL.md` hashes match their canonical sources in `C:\home\asus\ladipage-agentic-operator` at clean `main`/`origin/main` commit `c700435accf2ea75dfc990ec97fe76712f66dd6d`. Each installed skill now resolves `contracts`, `scripts` and `ladipage_operator` through local directory junctions to that canonical repo. Both installed skills pass `quick_validate`; the installed `prepare_modal_openform.py` and `validate_modal_openform.py` CLIs load successfully; focused modal freeze/handoff regression is 14/14 passed; full harness regression is 338 passed with 271 subtests passed. Before Slice B, verify those junction targets still resolve to the named repo, the repo is clean at the expected canonical commit, both contracts are readable, and the CLI smoke gates pass. If any check drifts, stop as `FORM_BRIDGE_RUNTIME_UNAVAILABLE`. Do not recreate a contract/validator from memory or use historical Fabless intent as a substitute.

**Legacy and automatic collection collision rule.** In GTM preview, inspect whether the all-pages copy listener fires on semiconductor routes. If it would send selected contact text or another user-selected value, add route-scoped exclusion to that legacy listener/tag in the owned GTM workspace, then verify the old pages still behave as intended; if exclusion cannot be proven without broader regression, block release. Inspect every automatic outbound-click payload and final link destination. Remove or replace an uncleared/private link in the owned route before QA; do not solve it by sending the link URL in a new event. Inspect shared section GA4 tags for a mapped `industry` DLV or stale page state; no semiconductor hit may carry an eight-industry value. Any shared-tag change requires a before/after preview on one existing non-semiconductor route.

**Google URL labeling to verify against the paused build sheet:** `utm_source=google`, `utm_medium=cpc`, `utm_campaign=vn_semiconductor_search_p1`, `utm_content=<segment>_rsa_<variant>`, `utm_term={keyword}`, with auto-tagging/gclid preserved. Use the existing segment/ad identifiers in the approved build sheet; do not insert PII. This is a verification contract, not permission to create or change an ad object. Native LinkedIn delivery uses its own campaign/ad identifiers; no invented LDP UTM is needed for the in-platform format.

## 4. Five-phase deterministic execution plan

Execute the phases in order. The A–H slice codes remain the traceability IDs used in receipts. A route may advance independently, but a later phase never repairs or waives a failed earlier gate. All slices have one writer for their surface; the same authenticated browser session has one controller at a time. Save sanitized evidence only: no account identifiers, private URL, session state, credentials, raw lead data, contact values or screenshots exposing them.

| Phase | Included slices | Primary owner | Required terminal gate |
|---|---|---|---|
| 1. Discovery and route freeze | A–B | Tracking executor for inventory; route owner for local artifact | `P1_PASS_<ROUTE>` or a named blocker |
| 2. Local tracking build and final handoff | C–D | Route tracking owner; `$canonical-form-bridge` owner | `P2_PASS_<ROUTE>` with immutable final receipt |
| 3. LadiPage deploy and PopupX bind | E | Authorized `$ladipage-operator` controller | `P3_PASS_<ROUTE>` or `P3_PREVIEW_ONLY_<ROUTE>` |
| 4. Tracking and lead validation | F–G | Tracking executor; operator for the single form action | `P4_PASS_<ROUTE>` or an explicit form-test exclusion |
| 5. Independent audit and handoff | H | Auditor who did not write the audited surface | `PASS`, `PASS WITH ROUTE EXCLUSION`, or `BLOCKED` |

### 4.1 Phase 1 — Discovery and route freeze (Slices A–B)

**Goal:** replace historical assumptions with a live read-only inventory and identify one exact flat, provider-free source per route before any tracking mutation.

**Entry inputs:** current canonical docs; named visual candidate; read-only access to relevant LadiPage/GTM/GA4/Ads surfaces; canonical skill runtime at `C:\home\asus\ladipage-agentic-operator` commit `c700435accf2ea75dfc990ec97fe76712f66dd6d`.

**Ordered procedure:**

1. Read `CURRENT_STATE.md`, `DOCS_IMPACT_MAP.md`, this plan and the route override. Open a route ledger with owner, source revision, timestamp, read/write boundary and current phase.
2. Verify the installed skill junction targets, clean canonical harness revision, readable `modal_openform` contracts, both CLI smoke gates and `quick_validate`. A mismatch ends the phase as `FORM_BRIDGE_RUNTIME_UNAVAILABLE`.
3. In read-only mode, inventory current LadiPage page/popup/receiver ownership; GTM container, live version and workspace; GA4 stream, events and custom definitions; consent behavior; Enhanced Measurement; Google Ads standard/custom goals; LinkedIn reporting; and all existing page, section, copy, click and form listeners.
4. Build a collision graph for `page_view`, `section_view`, `section_engagement_time`, any `osat_cta_click`, content-click equivalents, automatic outbound click, `text_copy`/`contact_info_copy`, `form_start`, `form_submit` and every observed success event. Label every record `OBSERVED LIVE`, `HISTORICAL` or `UNKNOWN`.
5. Select the visually approved route source. Flatten Shadow DOM where required while preserving the approved visual and semantic structure. Remove every form, provider SDK/reference/configuration and hidden provider artifact.
6. Freeze exactly two primary CTA element IDs, required render anchors, section IDs, surviving cleared content markers, route name and `semi_route`. Supplier stops until Bảo has approved its final visual/content revision.
7. Commit the frozen local source on the executor's authorized owned branch if a valid commit/tree pin is required by the bridge contract. Record commit, tree and SHA-256; this commit is local unless a separate push is authorized.
8. Run `$canonical-form-bridge` prepare and validate as a compatibility preflight. Preserve the preflight manifest/receipt as evidence only; Phase 2 tracking changes will invalidate its artifact.

**Required outputs:** sanitized live inventory receipt; collision graph; frozen-route manifest; source commit/tree/hash; CTA/anchor/section/content allowlists; passed bridge preflight or exact validation failure; route ledger update.

**Gate:** record `ROUTE_FREEZE_PREFLIGHT_PASS` only when the route identity and flat provider-free source pass bridge compatibility preflight. Issue overall `P1_PASS_<ROUTE>` only when the sanitized live inventory is also sufficient to choose event ownership, as required by §4.1. If account access leaves event ownership/reuse UNKNOWN, preserve the route-freeze sub-result but issue a named overall blocker such as `P1_BLOCKED_<ROUTE>_EVENT_OWNERSHIP_UNKNOWN`. Preserve visible proof/content when needed for visual parity, but set the tracking content allowlist to N/A unless the marker is explicitly cleared. Shadow DOM, ambiguous CTA selectors, provider residue, or unknown route identity blocks source freeze; Supplier also requires final approval. No live mutation is allowed in Phase 1.

### Phase 1 execution record (2026-09-23)

The sanitized live inventory, collision graph and route ledger are in `operations/evidence/phase1/2026-09-23-inventory-and-route-ledger.md`. The correct paid-LadiPage GA4 property was inspected read-only; a separate website-property inspection was excluded after Coordinator surface correction and is not evidence. Runtime junction/contracts/CLI smoke and `quick_validate` passed. The existing authenticated GTM UI identified account `DigiwinVietnam` (Account ID `6331240604`), container `www.digiwin.com.vn` (public ID `GTM-NGT54TM9`). Version 49 was explicitly confirmed `Live, Latest`, published 2026-07-23; the prior no-versions conclusion was premature and is withdrawn. Its section tracker and downstream section GA4 tags/triggers are recorded as live; current workspace shows the same tag list/source, with a conflicting overview pending-change count noted in the ledger. LadiPage route/receiver identity was not established; Ads goals failed to load; LinkedIn reporting was permission-blocked. GA4 exposed existing relevant events and custom dimensions; their owners remain unknown, and its consent view showed no individual consent signals alongside a positive summary status. OSAT was flattened from the approved visual lineage and Fabless legacy/provider residue was removed while preserving visible content. Both normalized sources have exactly two stable CTA IDs, render anchors, provider-free flat identity, and desktop/mobile visual parity; their content tracking allowlists are N/A because no markers were cleared. Both bridge compatibility prepare/validate runs passed; receipts and the source pin are in the Phase 1 ledger. OSAT and Fabless have `ROUTE_FREEZE_PREFLIGHT_PASS` and now satisfy the §4.1 event-owner selection gate through the live Version 49 section-event dispatcher: terminals are `P1_PASS_OSAT` and `P1_PASS_FABLESS`. The route initializer is the sole section producer because its frozen IDs are disjoint from Version 49’s fixed legacy observer list. No OSAT CTA event is enabled; there is no compatible published tag, and Fabless retains no CTA analytics. The live all-pages copied-text path is a known privacy collision that requires route exclusion/governance before publication; per-tag consent, GA4 connected-tag indicator, capability-section DOM ID, route/receiver identity, and success-event semantics remain unknown. Supplier is `DEFERRED_BY_PRODUCT_OWNER` and excluded from Phases 2–5 until its approved source returns through Phase 1. This gate update authorizes Phase 2 local work only; no Phase 2 mutation was made in this inventory correction.

### 4.2 Phase 2 — Local tracking build and final PopupX handoff (Slices C–D)

**Goal:** add the exact awareness instrumentation to the canonical flat source and produce the immutable package consumed by LadiPage.

**Entry gate:** `P1_PASS_<ROUTE>` plus the Phase 1 inventory, collision graph and frozen-route manifest. The writer may change only the owned canonical route source and its tests.

**Ordered procedure:**

1. Decide the single owner of section observation from the inventory. Reuse the existing compatible owner or add the route initializer; never allow both to observe the same sections.
2. Add one idempotent flat-DOM initializer for `section_view` and `section_engagement_time` with the exact fields, viewport rule, visibility/focus handling, pagehide flush and 3600-second cap in §3.
3. Add `semiconductor_content_click` only for the surviving static allowlist and only when the inventory found no safe semantic equivalent. Add the OSAT CTA candidate only when its explicit inventory/owner gate passed. Add no CTA event to Fabless or Supplier.
4. Confirm the source contains no inline `page_view`, form-success event, PopupX SDK/provider ID/config, URL/text/copied value payload, PII field, network collector or duplicate initialization path.
5. Replace or adapt `tests/landing-tracking.test.cjs` to the final flat artifacts. Run source tests plus browser checks using marked fake data: repeat intersection, blur/focus, hide/show, pagehide, keyboard content activation, non-allowlisted controls and missing provider.
6. Render desktop and mobile and compare the approved visual, CTA count, anchor navigation and route semantics. Fix in the canonical source and rerun the full Phase 2 checks after each change.
7. Commit the final tracked canonical source and tests on the owned branch. Record commit/tree/SHA-256 and the exact passing commands/results.
8. Create a new final `modal_openform` manifest pinned to that tracked commit/tree/hash. Run `$canonical-form-bridge` prepare then validate to a non-overwriting output path.
9. Make the final prepared HTML read-only by process: calculate its hash, record it in the handoff, and do not edit or reformat it afterward.

**Required outputs:** tracked canonical source; passing test log; desktop/mobile render evidence; final source commit/tree/hash; final manifest; passed bridge receipt; exact prepared artifact/hash; operator handoff record.

**Gate:** issue `P2_PASS_<ROUTE>` only when all local tests pass and receipt/artifact hashes agree. Any source or prepared-artifact byte change, CTA/anchor/content change, visual regression, provider residue, duplicate event or stale test invalidates Phase 2 and requires steps 5–9 again.

### 4.3 Phase 3 — LadiPage deployment and PopupX binding (Slice E)

**Goal:** import the exact validated artifact, bind the existing PopupX form through the supported runtime, and prove the saved page without submitting a lead.

**Entry gate:** `P2_PASS_<ROUTE>`; exact named LadiPage target and lifecycle; explicit Product Owner authority for that target; one browser controller; final manifest/receipt/artifact available unchanged.

**Ordered procedure:**

1. Invoke `$ladipage-operator` for `modal_openform`. Revalidate route, commit/tree, source hash, artifact hash, CTA selectors, anchors, target identity and authorized lifecycle before opening the editor.
2. Bảo performs the visible Basic file-selection/create action required by the operator contract. The operator records the resulting page identity and compares it with the authorized target.
3. Capture a fresh PopupX profile witness showing exactly `name`, `email`, `phone`, `industry`, Data Leads enabled and the exact visible Industry labels. Stop if the profile, provider or receiver is ambiguous.
4. Verify the imported baseline and visual fidelity before mutation. Add only the official PopupX SDK and the narrow runtime modal adapter; retain no second form, provider-specific physical reference or route-owned success event.
5. Save, reopen and re-identify the same page. On desktop and mobile, prove each of the two declared CTA IDs requests and opens the existing modal exactly once; a missing provider must fail safely.
6. Check anchors, responsive layout and console/runtime errors. Correct only within the authorized operator surface. A material HTML/content change returns the route to Phase 2.
7. Publish only when the exact lifecycle includes publication. Otherwise stop after saved preview and label the result `P3_PREVIEW_ONLY_<ROUTE>`; preview is not public deployment.

**Required outputs:** operator route receipt; target/page identity; fresh redacted profile witness; before/after mutation record; save/reopen evidence; desktop/mobile popup and visual checks; public URL/version only if authorized; rollback reference.

**Gate:** issue `P3_PASS_<ROUTE>` only for an authorized deployed route with exact identity and two working CTAs. Wrong target, tampered receipt, Shadow DOM rejection, missing field/industry label, receiver ambiguity, duplicate form, visual regression or save/reopen mismatch is `BLOCKED`; do not improvise another provider or form.

### 4.4 Phase 4 — Tracking and lead validation (Slices F–G)

**Goal:** prove the deployed route's event path, consent and attribution, then verify the real receiver once if separately authorized.

**Entry gate:** Phase 3 passed for the intended lifecycle; Phase 1 inventory still matches the live GTM/GA4 versions. If either version changed, refresh the inventory/collision graph before proceeding.

**Ordered procedure:**

1. Open one controlled Tag Assistant/GTM Preview session and GA4 DebugView. Record container/workspace/live version and route URL in sanitized form.
2. Verify consent allowed/denied behavior, exactly one legitimate page owner, UTM values and gclid preservation, route/session attribution and absence of an eight-industry stale parameter.
3. Execute the QA matrix in §5 for section entry/re-entry, hidden tab, blur/focus, pagehide, content actions, non-allowlisted actions, CTA boundaries and missing-provider behavior. Confirm one intended GA4 send per event.
4. Inspect legacy copy, automatic outbound click, Enhanced Measurement and form listeners. If needed, add only the shared `Semiconductor Paid` DLV/trigger/tag definitions or a route-scoped legacy exclusion in the owned workspace, then regression-check one existing non-semiconductor route.
5. Record the GTM workspace diff and GA4 custom-definition result. GTM Submit/Publish requires exact separate authority; without it, retain preview evidence and report `READY FOR GTM PUBLISH`, never `DEPLOYED`.
6. Confirm no awareness micro-event is a GA4 key event, Google Ads primary action or campaign custom-goal member. Record LinkedIn as native delivery measurement only.
7. Treat the form test as a separate sub-gate. Immediately before the action, obtain Bảo's action-time confirmation for one fresh marked submission to the named route/receiver.
8. Select one exact visible Industry label, submit once, and stop. Record sanitized thank-you evidence, PopupX/Data Leads acceptance and Bảo's matching Lark pool screenshot. Do not retry when the outcome is uncertain and do not synthesize a success event in HTML.

**Required outputs:** Tag Assistant/DebugView test matrix; consent/attribution/duplicate evidence; GTM workspace diff and version state; GA4 custom-definition record; regression evidence; form-test receipt if authorized; route ledger update.

**Gate:** issue `P4_PASS_<ROUTE>` when event/debug checks pass and any authorized publish is proven. If the form test is not authorized, record `FORM TEST EXCLUDED — awaiting action-time confirmation`; this may support a later `PASS WITH ROUTE EXCLUSION`, but never proves receiver acceptance. PII/private URL egress, duplicates, lost attribution, micro-event conversion use, uncertain receiver or unrelated-site regression is `BLOCKED`.

### 4.5 Phase 5 — Independent audit and operational handoff (Slice H)

**Goal:** independently reproduce the critical evidence, reconcile documentation and leave one unambiguous operational state for each route.

**Entry inputs:** all Phase 1–4 receipts; canonical sources and commits; final bridge packages; operator receipts; GTM/GA4 debug evidence; current canonical docs. The auditor must not be the writer/controller for the audited surface.

**Ordered procedure:**

1. Reconstruct Git state with `$git-state-recovery`; distinguish working files, local commits, remote-tracking references and actual pushed state. Verify every recorded commit/tree/hash and identify local-only artifacts.
2. Re-run bridge receipt/artifact validation and local tracking tests from the pinned revision. Compare the deployed identity to the final handoff; inspect two CTA selectors, anchors and provider-free source constraints.
3. Reperform a sampled desktop/mobile render, PopupX open, consent, section, attention, content-click, duplicate and conversion-goal check. Review form evidence without exposing raw lead data.
4. Confirm rollback references, one-writer ownership and every authority boundary. Verify LinkedIn, Google Ads and GA4 scopes remain separate and reporting language does not claim brand lift or cross-platform unique reach.
5. Read `DOCS_IMPACT_MAP.md`; update affected canonical state/contract/runbook statements to the observed implementation. Do not rewrite history logs to mimic current truth. If nothing changes, record **Docs impact reviewed: no canonical update required.**
6. Produce a route-by-route audit table containing phase terminals, evidence references, exclusions, residual unknowns, next authorized owner/action and release/reporting eligibility.

**Required output and terminal:**

- `PASS`: all required phases and docs agree, including receiver evidence where production lead acceptance is claimed.
- `PASS WITH ROUTE EXCLUSION`: named route or optional form-test scope is excluded, with no claim for that scope; the other routes have complete evidence.
- `BLOCKED`: any receipt is stale, live/source identity differs, required tracking/runtime evidence is absent, canonical docs materially disagree, or a stop condition remains unresolved.

No terminal may be upgraded from a verbal statement. The auditor signs the final ledger with timestamp and evidence paths; Bảo retains the separate decisions to publish remaining versions, enable campaigns and spend.

### 4.6 Handoff receipt and invalidation rules

Every handoff uses a named revision and timestamp. Required fields: phase/slice; route; owner; input SHA/file hash and GTM version; sanitized platform surface; read/write permission; exact changes; evidence summary; test matrix and commands; failures/exclusions; rollback reference; terminal; next owner/action; stop condition. A dependent phase cannot start from an undocumented verbal state.

| Change discovered after a gate | Required restart |
|---|---|
| Visual/content DOM, CTA ID/count, anchor, section or content allowlist changes | Restart Phase 1 route freeze, then rerun Phases 2 onward |
| Tracking code or test changes with frozen DOM intact | Restart Phase 2 step 5 and regenerate the final bridge package |
| Any byte changes in final prepared artifact | Invalidate `P2_PASS`; regenerate manifest, receipt and artifact |
| PopupX profile, Industry labels, receiver or target page changes | Restart Phase 3 profile/identity gate; repeat Phase 4 form scope if affected |
| GTM live version, GA4 stream/custom definition, consent or goal configuration changes | Refresh Phase 1 account inventory and rerun Phase 4 |
| Deployment fix changes imported HTML/content | Return to Phase 2; a builder-side patch cannot become the new canonical source silently |
| Canonical doc disagrees with observed state | Phase 5 remains `BLOCKED` until reconciled or explicitly documented as unknown |

**Agent start instruction:** execute only the assigned phase and route. Read the prior phase receipt before action; verify its terminal and hashes; keep one writer/controller; stop on the listed condition; write the required receipt; do not begin the next phase or infer its authorization.

## 5. QA and audit matrix

Run the matrix per route on desktop and mobile where applicable. Use only dummy traffic labels with no PII; mark preview traffic distinctly in the private test receipt. Consent-denied behavior must follow the verified site's consent configuration; DebugView absence under denied consent is not by itself a tracking defect.

| Check | Expected evidence / PASS criterion | Blocker if failed |
|---|---|---|
| Identity and owner | Frozen artifact matches inspected route; Tag Assistant shows exact current container/tag owner; page and GA4 stream are correct | Wrong artifact, unexpected property/container, duplicate global tags |
| Landing attribution | Approved route loads with Google UTM values and gclid preserved; GA4 paid session/source data attributable after processing; exactly one legitimate `page_view` path | Lost UTM/gclid, PII in URL, duplicate page owner |
| Section view | Each allowlisted section emits `section_view` once on effective viewport entry and none from hidden/blurred state; actual ID becomes `section_name` | Extra/missing event, wrong section or duplicate path |
| Time | Repeat enter/exit, hide/show, alt-tab blur/focus and pagehide; accumulated active time is plausible, positive and ≤3600 per section, one final event per viewed section | Hidden time counted, outlier, double flush/listener |
| Content click | One cleared allowlisted action → one `semiconductor_content_click` with exact `semi_route`/`content_id`; non-allowlisted control → none; URL/text/value absent | Duplicate, unapproved proof, dynamic or sensitive payload |
| CTA/popup | Two primary buttons request the frozen external provider once; missing provider stays safe. OSAT intent only if enabled from A; Fabless/Supplier have no CTA analytics event | Click misreported as popup/lead, wrong provider, extra CTA event |
| Legacy collision and form | Existing all-pages `text_copy`/`contact_info_copy` cannot leak copied contact on these routes; inspect automatic outbound-click/link URL payloads, `form_start`/`form_submit` and real successful-submit owner without assuming equivalence; no route HTML success event | PII or private URL egress, fabricated lead, duplicate success source, unknown receiver before production |
| Consent and Ads goals | Test allowed/denied states; no awareness event marked GA4 key event or Google Ads primary; inspect Google campaign standard/custom goals and LinkedIn native source | Unapproved collection, micro-event used for bidding, mismatched consent |
| Reporting | LinkedIn native delivery separated from Google Ads delivery and GA4 behavior; route/device/source filters, timezone/currency/date and denominator recorded; no cross-platform unique-reach sum | Misattribution, mixed scopes, unqualified awareness-lift claim |
| Regression and rollback | Existing site events unchanged in preview; compare GTM workspace diff and version; post-release smoke test only after authority, with prior version ready | Unrelated site tag changed, no rollback evidence |

Audit the first reporting window only after platform data has had time to populate; record observed latency and missingness, and reconcile Google Ads clicks with GA4 sessions directionally rather than forcing equality. Inspect engagement-time distribution and any value above 3600 or repeated near-cap totals against the July debug pattern. If an outlier appears, suspend the attention KPI, locate the live source/revision, and do not relabel the anomalous seconds as high interest. Supplier is `NOT READY` until its own route manifest and QA pass.

**Reporting output after verification:** one weekly scorecard by platform, route and period with audience fit/observed coverage where available, search-query relevance/visible share, spend, impressions, platform reach/frequency, clicks, paid landing sessions, engaged sessions, section-view sessions and cleared-content-click sessions. Show each numerator and denominator: engagement rate = engaged sessions / paid landing sessions; section progression = sessions with a given section view / paid landing sessions on that route; content interest rate = sessions with a cleared content click / paid landing sessions on that route; cost per engaged session = matched platform spend / attributed engaged sessions. Use session counts, not raw event counts, for rates; a zero/unknown denominator yields `not calculable`, not zero cost. Each KPI row records source, filter/scope, baseline or unknown, provisional target/range, reason, action threshold, review date and confidence/limitation. Keep CTA requests, verified accepted forms and bookings in a separate progression table; show `unknown` rather than zero where wiring is unverified. Targets remain provisional until a valid baseline and Bảo's budget/delivery decision exist. Review after 5–7 delivery days only if a campaign has actually delivered. A later recall/message-association study requires its own sample, cost and comparison design; no click/engagement metric is labeled brand lift.

## 6. Decision pack and terminal states

Only these choices remain for Bảo after agents have produced concrete receipts: (1) approve the frozen route identities, exact LadiPage targets and final Supplier route; (2) authorize each live lifecycle/publish action for those exact targets; (3) give action-time confirmation for the single synthetic form test and decide production success-event attribution after evidence; (4) decide eventual campaign enable/spend and budget separately. Missing live evidence is **not** filled with a guessed event name, threshold, tag or platform capability.

`PLAN READY` means this design is audited, with no implementation claim. `READY FOR DECISION` means A–E have passed but release authority is pending. `BLOCKED` means a listed stop condition failed. `DEPLOYED` requires an authorized GTM/page version and post-release smoke evidence. `MEASUREMENT VERIFIED` requires the final independent audit plus a real reporting window; it is distinct from campaign active/delivering. The working budget remains a draft, and this plan does not authorize spend.

## 7. External product references checked 2026-09-23

- [Google Tag Manager Preview](https://support.google.com/tagmanager/answer/6107056) and [publishing/versions](https://support.google.com/tagmanager/answer/6107163): preview is separate from live publication; keep a version and diff.
- [GA4 DebugView](https://support.google.com/analytics/answer/7201382) and [custom definitions](https://support.google.com/analytics/answer/14240153): test event payloads; create reportable definitions for new custom parameters as needed.
- [GA4 Enhanced Measurement](https://support.google.com/analytics/answer/9216061) and [PII guidance](https://support.google.com/analytics/answer/6366371): automatic page/form events require live verification; URLs and event params must remain free of personal data.
- [Google Ads primary/secondary actions](https://support.google.com/google-ads/answer/11461796): secondary is observational, with a custom-goal exception; audit campaign goal selection.
- [LinkedIn delivery metrics](https://www.linkedin.com/help/lms/answer/a426154) and [document ads](https://www.linkedin.com/help/lms/answer/a737898/linkedin-document-ads?lang=en): use native awareness delivery/format reporting; document interactions stay on LinkedIn.
