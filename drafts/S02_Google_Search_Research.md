# S02 — Google Search research

**Status:** draft only; no Google Ads account access and no campaign created  
**Owner:** Executor in this batch  
**Objective:** define VN/EN query clusters, intent hypotheses, negatives and validation steps without claiming volume, CPC, competition, overlap or campaign results.

## Source boundary

- Local: kickoff §§4, 7, 8; source brief “SEO cluster ưu tiên” and “Digital Ads — Bảo”.
- Public official: Google Ads Keyword Planner guidance, https://support.google.com/google-ads/answer/7337243 (accessed 2026-09-11); Google forecast guidance, https://support.google.com/google-ads/answer/3022575 (accessed 2026-09-11).
- Public official guidance establishes that Keyword Planner can provide ideas, historical search estimates and forecasts, but values depend on location, match type, bid, budget, seasonality and account setup. No such values were observed for this project.

## Fact / proposal / unknown

**Facts:** local brief names high-intent topics such as semiconductor MES, ERP, wafer/WIP management, OSAT MES and lot/wafer traceability; Google Search is a planned function.

**Proposal:** begin with tightly themed exact/phrase hypotheses and a mechanism-led landing mapping; validate Vietnamese and English separately.

**Unknown:** account/campaign overlap, location/language settings, actual search volume/CPC/competition, query terms, existing negatives, conversion goals and final landing URL.

## Query clusters

| Cluster | VN hypotheses | EN hypotheses | Intent | Message / landing hypothesis |
|---|---|---|---|---|
| OSAT/MES | `MES đóng gói kiểm thử`, `phần mềm MES bán dẫn`, `truy xuất lot kiểm thử` | `semiconductor OSAT MES`, `packaging testing traceability software` | Solution/problem | OSAT mechanism route: lot–test–quality–cost |
| Traceability / lot | `truy xuất nguồn gốc lot wafer`, `traceability lot bán dẫn` | `semiconductor lot traceability`, `wafer traceability system` | Problem/solution | Traceability proof or mechanism-only route |
| WIP / outsource | `quản lý WIP bán dẫn`, `quản lý gia công ngoài IC` | `semiconductor outsourced WIP management`, `fabless WIP visibility` | Problem/education | Fabless mechanism route |
| ERP / semiconductor operations | `ERP ngành bán dẫn`, `ERP sản xuất bán dẫn` | `semiconductor ERP`, `electronics manufacturing ERP semiconductor` | Solution | ERP–MES–quality–cost explanation |
| SPC / test data | `SPC bán dẫn`, `quản lý test data bán dẫn` | `semiconductor SPC software`, `semiconductor test data management` | Problem/solution | Test-data and quality mechanism |
| Capacity / planning | `lập kế hoạch sản xuất bán dẫn`, `capacity planning OSAT` | `OSAT capacity planning`, `semiconductor production planning` | Problem/solution | Only if landing can support planning claim |

These are hypotheses, not observed query volume or buyer language.

## Negative keyword taxonomy

Validate against search terms before activation; do not apply remotely in this batch.

- Education/non-commercial: `course`, `khóa học`, `tutorial`, `pdf`, `definition`, `là gì`, `wiki`.
- Employment: `job`, `career`, `tuyển dụng`, `salary`, `internship`.
- Consumer/electronics unrelated: `chip design tool`, `phone`, `gpu`, `arduino`, `repair`.
- Free/open-source/software download: `free`, `open source`, `download`, `crack`, `license key`.
- Policy/news/general research: `news`, `stock`, `investment`, `government job`, unless the selected route explicitly supports it.

Do not blanket-negative ambiguous terms such as `MES`, `ERP`, `traceability`, `quality` or `WIP` before observing intent; they may contain relevant demand.

## Validation plan

1. In an authorized Google Ads account, confirm business/account identity, timezone, currency, location, language, existing campaigns and search-term overlap before any build.
2. Use Keyword Planner for Vietnam and selected language separately; record date, location, network, match type, historical window, average monthly searches, competition and bid ranges only if visible/exported.
3. Label every value as observed, forecast, estimate or unknown; do not treat forecast as delivery.
4. Classify query intent and map only validated clusters to the S01 message and an actually compatible landing route.
5. Produce a paused/draft-only campaign design only after mandate and URL/measurement contracts exist; no enable/spend.

## Acceptance, dependencies and stop

**Acceptance:** each cluster has VN/EN hypotheses, intent, message/landing hypothesis, negative taxonomy and validation method; no fabricated metrics.  
**Dependencies:** S01 message map; S00 account/UI and route evidence; S04 measurement semantics before conversion-goal decisions.  
**Stop:** no account access, no reliable source, unclear overlap, or missing route means “pending validation”; do not infer volume/CPC/competition or create a campaign.
