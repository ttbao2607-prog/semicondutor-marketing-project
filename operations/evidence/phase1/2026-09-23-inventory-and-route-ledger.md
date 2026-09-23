# Phase 1 inventory and route ledger

**Observed:** 2026-09-23 (read-only, existing authenticated browser sessions). **Branch:** `slice/awareness-tracking-plan`, baseline `9b0743740c8118227a4ae088b5a39146bf28daa7`. **Scope:** Phase 1 / §4.1, slices A–B. No live changes were made.

## Sanitized live inventory

| Surface | Status | Observation |
|---|---|---|
| LadiPage route / popup / receiver ownership | UNKNOWN | The accessible editor was an unrelated staging page; it does not establish ownership or target identity for OSAT/Fabless/Supplier. No target or receiver was opened or changed. |
| GTM account/container identity | OBSERVED LIVE | Existing authenticated GTM UI showed account label `DigiwinVietnam`, container label `www.digiwin.com.vn`, public container ID `GTM-NGT54TM9`. These approved routing identifiers identify the intended container only. |
| GTM versions/workspace | OBSERVED LIVE UI / UNKNOWN live configuration | Correct container workspace opened read-only; workspace showed 69 tags, 60 triggers, and `Workspace Changes: 0`. Versions view stated there are no versions. Therefore these displayed definitions are workspace-only and no published/live firing version or its ownership is established. |
| GA4 | OBSERVED LIVE | Correct paid-LadiPage property label: `Digiwin - Ladipage - Bao`. One web stream, `ladipage ERP`, domain `solutions.digiwin.com.vn`; UI reported traffic in the previous 48 hours. No account/property numeric identifiers or raw URLs are retained. |
| GA4 Enhanced Measurement / redaction | OBSERVED LIVE | Enhanced Measurement enabled: page views, scrolls, outbound clicks, site search, video engagement and form interactions. Email redaction active; URL query-parameter redaction inactive. Stream details displayed zero connected site tags. |
| GA4 events / key events | OBSERVED LIVE | Recent catalogue showed 42 events and 27 configured key events. Existing relevant names included `page_view`, `section_view`, `section_engagement_time`, `click`, `contact_info_copy`, `form_start`, `generate lead`, `LeadConversionSuccess`, `diagram_v3_cta_click`, and `industry_cta_click`. The catalogue does not identify producer/owner; no submit-success event was verified. `accepted_form` was not observed. |
| GA4 custom definitions | OBSERVED LIVE | 25 event-scoped custom dimensions displayed, including `cta_location`, `cta_type`, `section_name`, `trigger_section`, `page_location`, and `profile_key`. This confirms definitions exist, not their GTM population or ownership. |
| GA4 consent signals | OBSERVED LIVE | The settings page selected `ladipage ERP`. Summary said “Tốt / Bạn đã thiết lập đúng”; each displayed individual status said no signal for `analytics_storage`, `ad_storage`, `ad_user_data`, and `ad_personalization`. Implementation behavior and cause are unverified. |
| Google Ads goals | UNKNOWN / BLOCKED | Conversion-goals view failed to load after one in-app reload attempt. No goals, account identifiers, or configuration were recorded. |
| LinkedIn reporting | UNKNOWN / BLOCKED | Existing session showed no permission to access the ad account. No reporting data were read. |

A separate GA4 website-property inspection was excluded after a Coordinator L1 surface correction. It is WRONG-SURFACE and contributes no facts to this inventory or collision graph.

## GTM workspace-only inventory and collision graph (read-only, 2026-09-23)

Container routing identity is the approved label/ID above. The account/container UI is directly observed. No published versions exist in the Versions view; all tag, trigger, variable, and listener records below are **OBSERVED WORKSPACE ONLY**, while active/live execution is **UNKNOWN**. Workspace changes displayed 0. Consent fields for individual tags were not exposed in this read-only detail view; tag-level consent requirements are UNKNOWN. No Preview or Submit action was used.

| Path | Workspace evidence | Status and collision/ownership result |
|---|---|---|
| `page_view` / base tags | `GA4 - Config - All pages` (Google Tag) fires on `All Pages`; configuration UI references Google tag `ladipage ERP`. GA4 stream details separately showed zero connected site tags. | Workspace setup observed; active global page-view producer and auto page-view behavior UNKNOWN. Do not add route sender. |
| `section_view` | `Custom HTML - Section View & Engagement Tracker` fires on `All Pages`; watches exactly `digiwinerp`, `digiwindonghanh`, `t100erp`, `badges`, `workflowerp`, `diagram-product`, `luachon-nganh-erp`, `downloadcasestudy`, `review-leadership`, and `contactus`. `TR - Section View` listens for exact custom event and feeds `Section VIew` GA4 tag with `section_name`, `industry`; DLVs shown in workspace. | Workspace producer/consumer wiring observed; live ownership UNKNOWN. Frozen OSAT/Fabless anchors are not in the listener's fixed ID list; shared event duplication/compatibility still requires active-version evidence. |
| `section_engagement_time` | Same listener uses 20-second key-section threshold, 3600-second cap, visibility/focus pausing and `IntersectionObserver`; pushes `section_name` and `engagement_seconds`. `TR - Section Engagement Time` feeds `Section Time On Screen` GA4 tag; DLVs shown. | Workspace wiring observed; live ownership UNKNOWN. |
| `potential_viewer` | Same listener also pushes this event for selected legacy sections and invokes Meta custom event when `fbq` exists; custom-event trigger and GA4 tag are present. | Workspace wiring observed; not route-approved and live state UNKNOWN. |
| CTA/click | `GA4 - Industry CTA Click` and diagram CTA/V3 tags exist in separate folders with their own custom-event triggers and DLVs. No OSAT CTA event tag/trigger or Fabless route CTA tag was found in the inspected workspace list. | Existing events are not shown equivalent to OSAT/Fabless semantics; active ownership and reuse UNKNOWN. Do not infer reuse. |
| Copy | `cHTML - Listener - Text Copy.` fires All Pages and pushes `text_copy` plus selected text when selection length is at least 9. `CE - Text Copy Detected` fans out to GA4 `Copied Event` (`contact_info_copy`, `content` from copied-text DLV) and Meta `Facebook - Microconversion - Copied content`. | Workspace behavior is observed and presents a copied-content privacy/collision risk; active firing UNKNOWN. No copied values were inspected or retained. Do not reuse/transmit copied content. |
| Form/success | `Success - Leadform` listens to `Ladi_form_success` and references only paused `ZZ_DEPRECATED - Facebook - Event - Lead - 2026-07-10`. Several active-looking workspace lead tags are tied to old ERP thank-you URL triggers. | Workspace config observed; no verified success producer for OSAT/Fabless and no active-version status. GA4 `generate lead` / `LeadConversionSuccess` remain semantically unverified. |
| Variables | Built-ins include click text/ID/URL, page path/URL and referrer. Relevant workspace DLVs include `section_name`, `engagement_seconds`, `industry`, `cta_location`, `cta_type`, `copied_text`, and diagram fields. | Variable names/config presence are workspace-only; route producer paths and live usage UNKNOWN. |
| Consent | GA4 property UI reported no individual consent signals despite a positive summary. GTM per-tag consent requirements were not surfaced without entering edit mode. | Consent implementation and active tag behavior UNKNOWN. |

### Collision graph

| Measurement path | Evidence/status | Consequence |
|---|---|---|
| Global `page_view` | GA4 event observed; GTM/tag owner UNKNOWN | Do not add a route page-view sender. |
| `section_view` / `section_engagement_time` | GA4 events observed; GTM listeners/tag ownership UNKNOWN | Reuse/duplicate decision blocked. |
| CTA names (`osat_cta_click`, `diagram_v3_cta_click`, `industry_cta_click`) | OSAT name is historical/local candidate; latter two observed in GA4 catalogue; owner and semantic equivalence UNKNOWN | No CTA event mutation in Phase 1. |
| Automatic outbound click | Enhanced Measurement enabled; emitted payload/conditions UNKNOWN | Route link and automatic-click collision review blocked. |
| Copy path (`text_copy` / `contact_info_copy`) | `contact_info_copy` observed as key event; `text_copy` is HISTORICAL from July docs; live listener/tag UNKNOWN | Privacy/collision review blocked; never send copied content. |
| Form path (`form_start`, `form_submit`) | `form_start` observed; `form_submit` producer/status UNKNOWN | Interaction is not receiver acceptance. |
| Form success (`generate lead`, `LeadConversionSuccess`, `accepted_form`) | First two names observed in GA4 catalogue; ownership/success semantics UNKNOWN. `accepted_form` not observed; historical proposal only. | No event may be treated as verified accepted lead; route HTML must emit none. |
| Consent and Ads conversion use | GA4 consent panel observation above; Google Ads goals UNKNOWN | Cannot conclude consent behavior or bidding-goal status. |

Historical facts above are limited to the reviewed July 2026 technical documents and are not current live ownership evidence.

## Route ledger

| Route | Owner / source revision | Phase-1 result | Exact blocker / boundary |
|---|---|---|---|
| OSAT | Approved visual source lineage `landing/osat-route/osat-lot-test-traceability.html` at `bb892e2`; frozen flat source at `3189b5aff672804b45ca9ae61e08716c849d6cbd` | `P1_BLOCKED_OSAT_EVENT_OWNERSHIP_UNKNOWN` | Sub-gate `ROUTE_FREEZE_PREFLIGHT_PASS`: flat/provider-free freeze and visual parity verified. CTA IDs `osat-cta-header`, `osat-cta-terminal`; anchors `top`, `main-content`, `osat-footer`; render model `flat_document`; tracking content allowlist `NOT APPLICABLE` (no cleared markers). Bridge prepare/validate PASS. Overall Phase 1 gate fails because live GTM/tag ownership is UNKNOWN, so event ownership/reuse cannot be selected. |
| Fabless | Approved flat lineage `landing/fabless-route/fabless-outsourced-popupx-basic-flat.html` from `37ea3e92c8bf52761814c7d939fde1f085e72eb9`; normalized frozen source at `3189b5aff672804b45ca9ae61e08716c849d6cbd` | `P1_BLOCKED_FABLESS_EVENT_OWNERSHIP_UNKNOWN` | Sub-gate `ROUTE_FREEZE_PREFLIGHT_PASS`: legacy adapter/provider trigger residue removed with visible DOM/content preserved. CTA IDs `fabless-cta-header`, `fabless-cta-terminal`; anchors `hero`, `main`, `footer`; render model `flat_document`; tracking content allowlist `NOT APPLICABLE` (no cleared markers). Bridge prepare/validate PASS. Overall Phase 1 gate fails because live GTM/tag ownership is UNKNOWN, so event ownership/reuse cannot be selected. |
| Supplier | Route owner; current partner candidate is not a final Supplier route | `DEFERRED_BY_PRODUCT_OWNER` | Bảo deferred Supplier; exclude it from Phases 2–5 until its approved source returns through Phase 1. No source freeze or bridge preflight. |

The Phase 1 route-freeze/preflight sub-gate passed for OSAT and Fabless, but neither satisfies the overall §4.1 Phase 1 gate: live inventory did not establish event ownership. Their terminal states are `P1_BLOCKED_OSAT_EVENT_OWNERSHIP_UNKNOWN` and `P1_BLOCKED_FABLESS_EVENT_OWNERSHIP_UNKNOWN`. Supplier is `DEFERRED_BY_PRODUCT_OWNER` and excluded from Phases 2–5 until an approved source returns through Phase 1.

Both canonical sources are pinned to commit `3189b5aff672804b45ca9ae61e08716c849d6cbd`, tree `d0437164ec84c2c81b0ad9d145e2894772c1ace3`. OSAT source SHA-256: `bfff2e75f24e20ded64e84dc0e230ad90e47af84a904fe2fd699343d3fd21523`; Fabless source SHA-256: `746d79adda6b80db7a6fe76ec58faa8d5d5857ccc15de4daaa56d305c5d98625`. Original proof/source text remains visually unchanged; no proof-rights conclusion was made. Since no content markers were cleared for tracking, route content tracking allowlists are N/A. Desktop/mobile comparison was performed against the approved lineage; both routes retained layout/text/CTA parity with no horizontal document overflow. Visual review used requested 1440×1000 and 390×844 viewports (browser CSS viewport measured 1600×1000 desktop and 434×844 mobile due device scale); no screenshots or account identifiers are retained.

Bridge compatibility preflights (not final tracking packages): OSAT intent `phase1-osat-modal-intent.json`, prepared artifact `operations/evidence/phase1/bridge/osat/osat-prepared.html`, receipt `operations/evidence/phase1/bridge/osat/osat-handoff-receipt.json`; Fabless intent `phase1-fabless-modal-intent.json`, artifact `operations/evidence/phase1/bridge/fabless/fabless-prepared.html`, receipt `operations/evidence/phase1/bridge/fabless/fabless-handoff-receipt.json`. Both prepare and validate returned `MODAL_OPENFORM_HANDOFF_READY`, `valid: true`, with no errors. Receipts confirm two CTA selectors, anchor coverage, `flat_document`, and false for HTML form, inline provider bundle, physical reference and Shadow DOM.

The installed canonical bridge runtime is available and skill validation/CLI smoke gates passed. No Phase-2 tracking change, form operation, publish, audience action, spend or push occurred. Live LadiPage route/receiver, active GTM version/ownership, and Ads/LinkedIn access limitations above remain unresolved.
