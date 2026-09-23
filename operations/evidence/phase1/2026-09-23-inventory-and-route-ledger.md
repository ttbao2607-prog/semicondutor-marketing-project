# Phase 1 inventory and route ledger

**Observed:** 2026-09-23 (read-only, existing authenticated browser sessions). **Branch:** `slice/awareness-tracking-plan`, baseline `9b0743740c8118227a4ae088b5a39146bf28daa7`. **Scope:** Phase 1 / §4.1, slices A–B. No live changes were made.

## Sanitized live inventory

| Surface | Status | Observation |
|---|---|---|
| LadiPage route / popup / receiver ownership | UNKNOWN | The accessible editor was an unrelated staging page; it does not establish ownership or target identity for OSAT/Fabless/Supplier. No target or receiver was opened or changed. |
| GTM workspace, live version, tags, triggers, variables, listeners | UNKNOWN / BLOCKED | Container workspace remained on a loading screen. No live configuration evidence was readable. |
| GA4 | OBSERVED LIVE | Correct paid-LadiPage property label: `Digiwin - Ladipage - Bao`. One web stream, `ladipage ERP`, domain `solutions.digiwin.com.vn`; UI reported traffic in the previous 48 hours. No account/property numeric identifiers or raw URLs are retained. |
| GA4 Enhanced Measurement / redaction | OBSERVED LIVE | Enhanced Measurement enabled: page views, scrolls, outbound clicks, site search, video engagement and form interactions. Email redaction active; URL query-parameter redaction inactive. Stream details displayed zero connected site tags. |
| GA4 events / key events | OBSERVED LIVE | Recent catalogue showed 42 events and 27 configured key events. Existing relevant names included `page_view`, `section_view`, `section_engagement_time`, `click`, `contact_info_copy`, `form_start`, `generate lead`, `LeadConversionSuccess`, `diagram_v3_cta_click`, and `industry_cta_click`. The catalogue does not identify producer/owner; no submit-success event was verified. `accepted_form` was not observed. |
| GA4 custom definitions | OBSERVED LIVE | 25 event-scoped custom dimensions displayed, including `cta_location`, `cta_type`, `section_name`, `trigger_section`, `page_location`, and `profile_key`. This confirms definitions exist, not their GTM population or ownership. |
| GA4 consent signals | OBSERVED LIVE | The settings page selected `ladipage ERP`. Summary said “Tốt / Bạn đã thiết lập đúng”; each displayed individual status said no signal for `analytics_storage`, `ad_storage`, `ad_user_data`, and `ad_personalization`. Implementation behavior and cause are unverified. |
| Google Ads goals | UNKNOWN / BLOCKED | Conversion-goals view failed to load after one in-app reload attempt. No goals, account identifiers, or configuration were recorded. |
| LinkedIn reporting | UNKNOWN / BLOCKED | Existing session showed no permission to access the ad account. No reporting data were read. |

A separate GA4 website-property inspection was excluded after a Coordinator L1 surface correction. It is WRONG-SURFACE and contributes no facts to this inventory or collision graph.

## Collision graph

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
| OSAT | Route owner; visual candidate recorded on local `main` at `bb892e2` | `P1_BLOCKED_OSAT` | Candidate uses Shadow DOM, which the bridge rejects. Flattening with visual/semantic equivalence is not proven; supporting proof/claim rights also need review. No frozen manifest or bridge preflight generated. |
| Fabless | Route owner; candidate lineage on `slice/fabless-ldp-canonical` at `37ea3e9` | `P1_BLOCKED_FABLESS` | Flat candidate has legacy lead-popup adapter/residue and existing provider-trigger markers; it is not a provider-free canonical source. Proof/claim selector scope is not cleared. Cleanup and visual-equivalence review required before freeze. No bridge preflight generated. |
| Supplier | Route owner; current partner candidate is not a final Supplier route | `P1_BLOCKED_SUPPLIER_NOT_APPROVED` | Final visual/content approval is absent. No source freeze or bridge preflight. |

No eligible route reached bridge preflight. The installed canonical bridge runtime is available and its skill validation/CLI smoke gates passed; route-specific prepare/validate was intentionally not attempted because each route fails the documented source eligibility gate. No Phase-2 tracking change, form operation, publish, audience action, spend or push occurred.
