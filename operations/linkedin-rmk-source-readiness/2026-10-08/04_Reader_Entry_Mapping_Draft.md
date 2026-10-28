> **Unified reader đã public · 28/10/2026:** [LadiPage Basic deploy và 32 state checks](../../pre-ad-readiness/2026-10-28/ladipage-deploy/DEPLOYED_VI.md) hoàn tất theo Bảo; agent tự upload/tạo theo override hiện hành. Endpoint https://solutions.digiwin.com.vn/semiconductor-case-reader chọn P1/P2 bằng t/lang; 11 route English, P1/P2 bốn locale và desktop/mobile đúng; save/reopen/copy/router retained. Không còn chờ PO import hoặc UNKNOWN host cho gói này. P1/P2 contact CTA, fit/rights/native/tracking và ads release giữ gate riêng; không launch ads. Các notice pending/offline bên dưới là capture-time history. Docs/evidence chỉ local corrected chưa commit/push; source/main không đổi.

# 04 · Reader entry mapping — draft

Status: DRAFT_PROPOSAL. Full table: [04_Reader_Entry_Mapping_Draft.csv](04_Reader_Entry_Mapping_Draft.csv), 33 rows generated from `operations/fdi-destination-html/2026-10-07/inventory.csv` (11 treatments × 3 locales). The CSV remains a source/proposed-UTM mapping. The unified reader is now hosted at the endpoint in the current notice; no tracking installation is claimed.

## What the table gives
Per reader: treatment and persona, locale, journey batch, viewer path, reader path in the repository, language entry (`?lang=<locale>`), the case entity, and a **proposed**, stage-aware UTM pattern (cold and RMK campaign patterns, creative-level content pattern). Every reader opens in the language of its journey and has a four-language toggle; the entry query is already set in each journey viewer.

## Proposed UTM pattern (to be inventoried before use)
`utm_source=linkedin`, `utm_medium=paid_social`. The stage and the creative must be readable from the URL, because the same reader can receive visits from a cold ad and from a Carousel RMK ad, and one batch holds several ads:
- `utm_campaign` carries the **stage of the ad that sent the click**: `fdi_<treatment>_<locale>_cold_<wave>` for cold ads, `fdi_<treatment>_<locale>_rmk_<wave>` for RMK ads. The reader is never labelled as awareness by default.
- `utm_content=<batch>_<creative_id>`: identifies the creative that produced the visit, with the real creative ID filled in when ads exist (placeholder until then).
- The **original cold cohort** of an RMK visit is kept in the source registry and in the readback sheet (`source_cohort_id`), not in the URL; keep it out of URLs so no cohort or company detail leaks into analytics parameters. The existing tracking documents define a UTM scheme only for Google Search (`utm_source=google`, `utm_medium=cpc`, …); **no LinkedIn naming exists in the repository**, so this pattern is a proposal. Per project rules: check existing events/tags first and avoid duplicates, verify UTM across the whole route, never put PII in a URL or analytics parameter, and use clearly marked fake data for tests.

## Open questions (decisions for Bảo, none can be closed offline)
1. **Unified hosting VERIFIED_SCOPED 28/10.** Bảo authorized Basic import/deploy; public endpoint serves treatments/locales through `?t=<treatment>&lang=<locale>`. O2 can add `entry=B4/B5/B6`. See current deployment report; source paths in CSV remain provenance, not public URLs.
2. **Return differs by artifact.** Original offline readers retain `index.html`; deployed unified package removes these returns. Do not apply offline reset findings to public unified. Partner contact next-step remains open.
3. **Analytics ownership.** The HTML must not carry analytics dispatch or a form; page views come from the existing global tag on the hosting route, which must be inventoried. The readers' CTA currently points to Digiwin Vietnam's contact page (Fabless, O-series); Partner readers have no CTA button or contact link (checked: no `cta` class, no form or submit button, no contact-vn link in the nine P readers). Whether Partner should get one is open.
4. **Shared endpoint deployed.** The existing full unified package is hosted per Bảo. Treatment and locale must be explicit for final ad destinations; UTM/creative naming remains proposed until measurement/ad mapping is closed. Bare/invalid query defaults O1/en.
5. **Rights.** The September 2020 photo (Sohu byline account) and the two generated illustrations have no verified public/paid usage rights.

Related: [operational mandate checklist](06_Operational_Mandate_Checklist.md) · [week 1 readback template](05_Week1_Readback_Template.md) · [tracking contract](../../../tracking/Semiconductor_Tracking_Contract.md).
