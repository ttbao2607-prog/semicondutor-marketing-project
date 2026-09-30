# Vy landing localization contract — offline draft

**Date:** 2026-09-29. **Owner:** S4 landing localization. **Source revision:** local `a71acbccfcdd2ce809a2b69f6948da85cbcf98e1`. **Status:** specification only; no localized HTML, translated asset, public route, or account change exists from this slice. The three current public routes remain Vietnamese. Bảo approved three languages in four locale variants: VI, EN, Simplified Chinese (`zh-Hans`) for China FDI and Traditional Chinese (`zh-Hant`) for Taiwan FDI. Bảo approved D3: one HTML per existing route URL, a top language switch, and a non-PII `lang` query parameter for paid-entry initial locale selection.

## Decisions and boundaries

| Gate | Decision required from Bảo | Dependent work held |
|---|---|---|
| D2 | **Decided:** Simplified Chinese (`zh-Hans`) for China FDI and Traditional Chinese (`zh-Hant`) separately for Taiwan FDI. Select qualified market/domain reviewers and preferred terminology for each. | Final copy, font/render QA and exports for both Chinese variants still need review; script decision alone approves no finished translation. |
| D3 | **Decided:** one HTML per existing route URL, top language switch and non-PII `lang=vi|en|zh-Hans|zh-Hant` query value to select the initial locale from ads. Resolve persistence precedence, fallback, URL encoding, canonical metadata, query-string preservation and PopupX handoff in implementation design. No duplicate language URLs. | HTML implementation, runtime and ad-destination QA, live revision and publication |
| Proof | Bảo confirmed on 2026-09-29 that case/claim content already present in the Vietnamese page has management approval for use and full translation. Preserve its exact numbers, entity, geography, date, relationship, source links and scope; review translated terminology and layout per locale. New or broader claims still need separate evidence/rights review. | Any translated claim or proof panel with that claim |

Use `VI`, `EN`, `zh-Hans` (China FDI) and `zh-Hant` (Taiwan FDI) as four explicit variant keys across three languages. Do not collapse the two Chinese versions into one `ZH` copy cell or assume a script conversion alone is market localization. Keep proper names, identifiers, product names and measured values exact unless the source owner approves a localized form. Translation may narrow a claim but must never widen geography, product capability, customer relationship or measured outcome.

## Source-to-language inventory

The implementation inventory must include every customer-visible string in the frozen flat canonical source, including text introduced by interaction scripts. Use stable source IDs/DOM anchors in the copy register and record `source text`, `VI`, `EN`, `zh-Hans`, `zh-Hant`, `source/proof ID`, variant-specific `reviewer`, `state`, and `QA result`. Blank cells mean missing, not approved fallback. HTML `lang`, page title, description, social metadata when present, navigation, headings, body, diagram labels, cards, tables, source-link labels, footer, CTA, alt text, `aria-label`, `title`, keyboard instructions, detail toggles, tabs, options, dialog messages and any runtime text all count. Preserve functional identifiers and event names verbatim.

| Route and source file | Route story and specific inventory | Consultation CTA invariant |
|---|---|---|
| OSAT — `landing/osat-route/osat-lot-test-traceability.html` | Lot → test → quality/4M1E → WIP → cost-review rail; simulation/inspector, mobile detail reveal, proof/source links, page metadata and all accessible/interactive labels in each of four variants. | Exactly two consultation controls, header and terminal, with existing IDs and intent semantics; VI/EN/zh-Hans/zh-Hant labels require copy review. |
| Fabless — `landing/fabless-route/fabless-outsourced-popupx-basic-flat.html` | Forecast → outsource → lot/datecode/BIN → cost-review flow; mobile map, map tabs, stage/trace/cost controls, three decision dialogs, glossary, case/proof cards, source links, metadata and accessible labels. The source contains a 48h-to-02h case claim and customer/logo panels; existing VI case/claim may be translated under Bảo's 2026-09-29 approval, with exact scope and source preserved. | Exactly `fabless-cta-header` and `fabless-cta-terminal`; source VI text is `Đăng ký tư vấn`. |
| Supplier/Partner — `landing/partner-route/supplier-ecosystem-flat.html` | ERP → MES → OT/SECS-GEM architecture hypothesis; three audience cards, mobile architecture reveal, product/source panels, metadata and accessible/interactive labels. Distinguish proposed integration mechanism from verified installed capability. | Exactly one consultation control: header ID `partner-cta-header`, VI label `Tư Vấn`; no hero/terminal replacement. |

Existing public identities are `/semiconductor-osat`, `/fabless`, `/supplierecosystem`; the business route value for Supplier is `partner`. Each route retains its current path and one HTML document, with a top language switch. The approved entry design appends `lang=vi`, `lang=en`, `lang=zh-Hans` or `lang=zh-Hant` to that same URL to choose the initial variant. These are design values, not tested public behavior. A switch must update all customer-visible and accessible text coherently, including `html lang`, title and description, without resetting the route's interaction state unexpectedly. Source files are provider-free HTML; current live pages have an external PopupX bridge. Do not insert form fields, SDK, popup callback, new analytics dispatch or provider IDs into localized canonical HTML.

## Terminology proposals for reviewer

These are semantic prompts, not approved translations. The China FDI column must use Simplified Chinese and the Taiwan FDI column Traditional Chinese; each requires its own native domain review. Shared terminology is allowed only after both reviewers confirm the same sense and claim scope.

| Source concept | VI working sense | EN working sense | zh-Hans China / zh-Hant Taiwan reviewer task |
|---|---|---|---|
| lot | lô sản xuất / lô wafer according to context | lot / wafer lot | Choose context-specific term; preserve lot identifier. |
| yield | tỷ lệ đạt; specify stage and denominator | yield; specify stage and denominator | Avoid implied improvement or benchmark. |
| recipe | công thức/thông số quy trình | process recipe | Distinguish process settings from material formula. |
| traceability | truy xuất nguồn gốc / truy vết lô | traceability / lot trace | Preserve forward/backward scope actually shown. |
| audit | đối chiếu/kiểm tra theo ngữ cảnh | audit / review | Do not imply certification. |
| WIP | bán thành phẩm đang xử lý / tiến độ WIP | work in progress (WIP) | Keep acronym on first use with reviewed explanation. |
| substrate | đế/giá mang theo công đoạn | substrate | Distinguish package substrate from wafer. |
| PCB | bảng mạch in | printed circuit board (PCB) | Keep distinct from substrate. |
| OSAT, Fabless, MES, ERP, OT, SECS/GEM, BIN, datecode, 4M1E | retain acronym with contextual explanation | retain acronym with contextual explanation | Approve first-use expansion, casing and line-break rules. |

The glossary must record a final preferred term, disallowed near synonyms, first-use expansion and proof context per language. A technical and market-language reviewer signs off before a language is marked ready.

## Ad-to-landing and measurement handoff

For each future ad creative, record `channel/object`, `audience (FDI or domestic)`, `locale variant (VI/EN/zh-Hans/zh-Hant)`, `message/proof ID`, `route`, `exact destination URL with lang`, `CTA text`, `UTM source/medium/campaign/content/term as applicable`, and `QA status`. Match ad language, Chinese script/market and claim scope to the landing variant. All three destinations retain their current route paths; append the approved non-PII `lang` value for the initial variant. An EN, zh-Hans or zh-Hant ad cannot silently resolve to VI or the wrong Chinese script. Define whether language persistence lasts for a page, browser session or later visits, how user choice overrides `lang` on subsequent navigation, and the fallback for missing/invalid values; no persistence technology is approved yet. Verify URL encoding and joining with existing query parameters. Preserve inbound UTM and `gclid` through language selection, navigation and PopupX handoff without placing personal data in URLs or analytics payloads. Keep canonical metadata aligned with the single-URL architecture; review search indexing and language-discovery behavior without inventing duplicate URLs or hreflang alternates. Never infer ad-platform readiness from an offline link.

Keep existing `section_view(section_name)` and `section_engagement_time(section_name, engagement_seconds)` semantics, observer boundaries, focus/visibility timing, pagehide flush, idempotency and cap. Section IDs and names must remain stable unless tracking governance approves a mapping. OSAT's `osat_cta_click` with `cta_location=hero|terminal` remains only its governed candidate; Fabless and Partner gain no CTA event. The global tag owns `page_view`; no route emits a form-success event. PopupX/form, customer fields and lead receiver remain outside canonical HTML and require their own operator validation.

## Acceptance matrix for a future implementation

| Case | OSAT VI/EN/zh-Hans/zh-Hant | Fabless VI/EN/zh-Hans/zh-Hant | Partner VI/EN/zh-Hans/zh-Hant | Evidence / stop rule |
|---|---|---|---|---|
| Copy coverage | All visible, metadata, diagram, accessible and runtime strings in four variants | Same, including tabs, dialogs and glossary | Same, including audience/architecture views | Route × four-variant copy register complete; missing or unreviewed EN, zh-Hans or zh-Hant blocks release. |
| Proof and CTA | Two IDs, case scope and source links preserved | Two IDs, 48h/02h claim and logos reviewed | One `partner-cta-header`, VI `Tư Vấn` | Claim register and reviewer approval; no widened claim or new CTA. |
| Layout and controls | 375/390, 768, 1024, 1440px; compact rail and simulation reveal | Same; map, tabs, dialogs and glossary | Same; audience cards and architecture reveal | Each route × four variants: screenshots and keyboard run; no clipped glyph, overflow or broken focus/reading order, including Traditional glyph rendering. |
| Routes and links | Same route path; top switch, `lang` initial variant, persistence, source links, UTM/gclid | Same | Same | D3 entry design recorded; implementation and destination matrix checked later, including valid/invalid `lang`, precedence, encoding and PopupX/UTM handoff; no duplicate path or lost query parameter. |
| Provider/tracking | Source stays inert/provider-free; section and OSAT intent semantics preserved | Source inert; section semantics preserved | Source inert; section semantics preserved | Local regression plus authorized live checks of PopupX, GTM and section/pagehide only at the applicable later gate. |

Before any synchronization to an existing LadiPage page, the operator must read `$ladipage-operator` and `revise_existing_page`, match a `PENDING` receipt to that exact page identity/URL and run preflight. If it applies, use bounded semantic patch, save/reopen, same-URL publish, public/protected-invariant check and receipt closeout under a publication mandate. This specification authorizes none of those actions.

## Documentation impact and status

`DOCS_IMPACT_MAP.md` categories are strategy/market/language, landing/CTA, ads/creative and tracking. At this offline specification stage, current implementation and canonical truth have not changed: **Docs impact reviewed: no canonical update required.** On implementation, coordinator must review `CURRENT_STATE.md`, `README.md`, kickoff/source brief, `operations/Pre_Ad_Readiness_Plan.md`, relevant S01–S03/build packs, route design overrides and `tracking/Semiconductor_Tracking_Contract.md`; update only statements made stale by actual accepted changes. Preserve history/log meaning.

**Terminal for this artifact:** offline draft complete; Bảo decided both Chinese scripts/markets and the same-path, top-switch, non-PII `lang` initial-selection design. Bảo also approved full translation/use of case/claim already in Vietnamese source on 2026-09-29; native terminology, scope-preservation and visual QA remain open, while new/broader proof still needs evidence and rights review. Runtime implementation, persistence precedence, fallback, query encoding and UTM/gclid/PopupX QA remain open. This spec itself changes no live page, ad or lead result.
