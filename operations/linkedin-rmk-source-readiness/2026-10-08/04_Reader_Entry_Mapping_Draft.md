# 04 · Reader entry mapping — draft

Status: DRAFT_PROPOSAL. Full table: [04_Reader_Entry_Mapping_Draft.csv](04_Reader_Entry_Mapping_Draft.csv), 33 rows generated from `operations/fdi-destination-html/2026-10-07/inventory.csv` (11 treatments × 3 locales). No URL is hosted, no tag or tracking is changed, nothing is published.

## What the table gives
Per reader: treatment and persona, locale, journey batch, viewer path, reader path in the repository, language entry (`?lang=<locale>`), the case entity, and a **proposed** UTM set. Every reader opens in the language of its journey and has a four-language toggle; the entry query is already set in each journey viewer.

## Proposed UTM pattern (to be inventoried before use)
`utm_source=linkedin`, `utm_medium=paid_social`, `utm_campaign=fdi_<treatment>_<locale>_awareness_w1`, `utm_content=<batch>_closing_reader`. The existing tracking documents define a UTM scheme only for Google Search (`utm_source=google`, `utm_medium=cpc`, …); **no LinkedIn naming exists in the repository**, so this pattern is a proposal. Per project rules: check existing events/tags first and avoid duplicates, verify UTM across the whole route, never put PII in a URL or analytics parameter, and use clearly marked fake data for tests.

## Open questions (decisions for Bảo, none can be closed offline)
1. **Hosting route is UNKNOWN.** The readers are local single-file HTML. The project rules say not to assume LadiPage accepts arbitrary HTML; the real route must be proven first (see the LadiPage runbook). Publishing is outside Phase A without a mandate.
2. **The return link has no production meaning.** Every reader links back to `index.html`, which is the offline review viewer, not something a LinkedIn visitor has. A production version needs a decided target (for example none, the Digiwin site, or the contact page) before hosting. This is a design decision, not a bug fix I should make alone.
3. **Analytics ownership.** The HTML must not carry analytics dispatch or a form; page views come from the existing global tag on the hosting route, which must be inventoried. The readers' CTA currently points to Digiwin Vietnam's contact page (Fabless, O-series); Partner readers have no CTA button or contact link (checked: no `cta` class, no form or submit button, no contact-vn link in the nine P readers). Whether Partner should get one is open.
4. **Shared reader across ads.** One reader per route, with language by query. Whether different ads of one treatment share one hosted URL (and differ only by UTM content) is a choice for Bảo.
5. **Rights.** The September 2020 photo (Sohu byline account) and the two generated illustrations have no verified public/paid usage rights.

Related: [operational mandate checklist](06_Operational_Mandate_Checklist.md) · [week 1 readback template](05_Week1_Readback_Template.md) · [tracking contract](../../../tracking/Semiconductor_Tracking_Contract.md).
