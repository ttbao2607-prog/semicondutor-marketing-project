# Google Search Build Sheet

**Future ad-copy first mention (Bảo, 2026-10-02):** In each independently encountered Search ad, explain the first customer-visible abbreviation/acronym and OSAT/Fabless with a brief, locale-matched, source-checked parenthetical phrase. Reword RSA headlines/descriptions to respect their actual character limits and avoid unexplained acronym chains; do not infer product capability from definitions. Rule source: `../../operations/linkedin-awareness-execution/first-touch-anchor.md`. Existing keywords/candidates and campaign status are unchanged; this is no build/live release.

**Status:** offline production draft; no remote campaign creation, enablement or spend. Campaign target state remains paused. Vietnamese-first OSAT, Fabless and ERP–MES–OT/partner seed research was completed in Keyword Planner on 2026-09-14 under the recorded configuration. OSAT and Fabless showed no displayed metrics; Partner had one row with limited displayed historical estimates and seven rows with dashes. These observations do not establish demand, campaign eligibility or performance. Each query automatically created a draft plan entry; no explicit save was clicked. These are Planner drafts, not campaigns.

## Campaign structure

- One campaign; status **paused**.
- Ad groups: `OSAT_LOT_TEST`, `FABLESS_OUTSOURCE_WIP`, `ERP_MES_OT_PARTNER`.
- Exact and phrase only; Vietnam presence-only; Vietnamese and English; Search Network only.
- Display **OFF**; Search Partners **OFF**.
- Draft bidding: Maximize Clicks; provisional max CPC `25,000 VND`; no conversion-based bidding.
- Micro conversions are reporting-only, never primary Google Ads conversions.
- UTM: `utm_source=google`, `utm_medium=cpc`, `utm_campaign=vn_semiconductor_search_p1`, `utm_content=<segment>_rsa_<variant>`, `utm_term={keyword}`; preserve auto-tagging/gclid.

## Keyword hypotheses

Every set remains an **unvalidated build hypothesis**; the Planner observations below do not retain or approve terms for a campaign. Account-grounded sanitized observation: authenticated account context showed ERP/MES/manufacturing adjacency but no observed direct OSAT terms. No private metrics or campaign names are recorded.

| Ad group | Candidate exact/phrase themes (8–15 target after Keyword Planner) |
|---|---|
| OSAT_LOT_TEST | `OSAT lot tracking`; `semiconductor lot tracking`; `wafer lot traceability`; `IC lot genealogy`; `semiconductor production traceability`; `outsourced assembly test tracking`; `OSAT traceability software`; `semiconductor test data management` |
| FABLESS_OUTSOURCE_WIP | `fabless WIP tracking`; `semiconductor outsourced WIP`; `foundry WIP management`; `chip manufacturing WIP`; `subcontract manufacturing tracking`; `fabless production planning`; `outsourced semiconductor production`; `Datecode BIN lot management` |
| ERP_MES_OT_PARTNER | `semiconductor ERP MES integration`; `MES implementation partner semiconductor`; `electronics manufacturing ERP`; `MES integration partner Vietnam`; `ERP MES OT integration`; `factory data integration partner`; `semiconductor quality traceability`; `industrial automation MES partner` |

Validate language, geography, match type, search volume, competition, CPC, search terms and overlap in Keyword Planner/account UI. **Historical UI evidence (2026-09-11):** Campaigns, Ad groups, Settings and Keyword Planner were observed functional; the orange `GOOGLE_ADS_GOAL_UPDATE_BANNER / INFORMATIONAL / NON_BLOCKING` was informational; the six supplied English OSAT seeds returned no displayed metrics (`OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`). These are historical observations, not current validation or demand evidence.

### Offline S3 candidate mapping (not build-ready)

The per-term VI/EN/zh-Hans/zh-Hant wording, intent, route, exact/phrase hypothesis and `unknown` volume status are in `../../drafts/S02_Google_Search_Research.md` § S3 candidate keyword register. It supplements the historical English theme list above; neither list is an approved import. The earlier Planner dashes and the single `electronics manufacturing ERP` historical estimate cannot be assigned to any new candidate. D1 ICP and FDI/domestic classification remain provisional and do not create separate campaigns or targeting facts.

| Candidate group | VI core IDs | EN test IDs | zh-Hans China test IDs | zh-Hant Taiwan test IDs | Landing and build gate |
|---|---|---|---|---|---|
| `OSAT_LOT_TEST` | O-V1, O-V2 | O-E1, O-E2 | O-Z1, O-Z2 | O-T1, O-T2 | Existing OSAT route; verify selected locale on arrival, relevant copy and term/negative overlap. |
| `FABLESS_OUTSOURCE_WIP` | F-V1, F-V2 | F-E1, F-E2 | F-Z1, F-Z2 | F-T1, F-T2 | Existing Fabless route; verify outsourced-WIP promise and selected locale on arrival. |
| `ERP_MES_OT_PARTNER` | P-V1, P-V2 | P-E1, P-E2 | P-Z1, P-Z2 | P-T1, P-T2 | Existing Supplier/Partner route; distinguish partner intent from generic electronics ERP. |
| Brand group **candidate only** | B-V1 | B-E1 | B-Z1 | B-T1 | Route unresolved; confirm objective, baseline, existing brand overlap and locale destination before group design. |

Bảo selected one HTML with a top language switch at each existing URL (D3). How an ad opens the intended VI/EN/zh-Hans/zh-Hant view, preserves UTM and `gclid`, and avoids redirect/source loss still needs design and QA; a switch existing in HTML does not prove the entry behavior. D2 selects Simplified Chinese for China FDI and Traditional Chinese separately for Taiwan FDI; the 21 EN/zh-Hans/zh-Hant candidate seed terms in the 2026-09-30 Planner receipt were queried; all showed no displayed metrics. Their Chinese wording remains unreviewed for buyer terminology, and the seven VI candidates in the S3 register remain unqueried. Do not create EN/Chinese RSAs, upload terms or mark a group ready until the matching landing copy, locale-specific translation review and account observations exist. Vietnamese-first remains the current offline structure, not a demand conclusion. Brand terms must be reported separately from non-brand semiconductor intent.

**Current Planner evidence (2026-09-14, Asia/Ho_Chi_Minh):** screenshots showed no ad-blocker dialog. The string remained in the accessibility/DOM tree as a false signal; direct navigation and the Keyword Planner query form worked. Classify `OBSERVED_DOM_FALSE_SIGNAL_NON_BLOCKING`, not a visible modal or blocker. The orange Vietnamese goal/budget mechanism-update banner was visible and informational. Shared query configuration for all three seed clusters: Vietnam, Vietnamese, Google, Sep 2025–Aug 2026, adult ideas excluded. OSAT: all displayed metric fields were dashes and the chart/related-idea panel showed no data; classify `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`, not zero demand. Fabless: all eight seed rows showed dashes in every displayed metric field; classify `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`, not zero demand. Partner: eight seed rows; only `electronics manufacturing ERP` displayed average monthly searches 10, three-month change 0%, and year-over-year change -100%; its other displayed metrics were dashes. Each of the other seven rows showed dashes in all displayed metric fields. This is limited historical UI evidence, not a demand, bid, competition, eligibility or performance conclusion. “Get results” automatically created a draft plan entry after each of the three queries, without an explicit save click; these are not campaigns. This query work was authorized with acceptance of that side effect. No campaign was created or modified, no settings changed, and no enablement, spend, export or upload occurred. This is not a validated account-wide failure. Campaign geography, language, network and auto-tagging remain unverified.

**Multilingual Planner evidence (2026-09-30, Asia/Ho_Chi_Minh):** 7 EN, 7 zh-Hans and 7 zh-Hant candidate seeds were queried separately for Vietnam with the Google network, Sep 2025–Aug 2026, and adult ideas excluded. Each batch returned 7 seed rows and all displayed metric fields were dashes; related-idea panels showed no results. Statuses in the receipt: EN and zh-Hans PLANNER_NO_DISPLAYED_DATA_DASHES; zh-Hant PLANNER_DOM_FALSE_SIGNAL_NON_BLOCKING because the DOM contained “Turn off ad blockers” but the heading was invisible and results returned normally. Do not infer demand=0. No campaign or settings changes, keyword import, enablement, spend, export or upload occurred. After returning home, only two existing Jul 20 drafts were visible; no new list row was observed. See operations/CODEX_GOOGLE_PLANNER_DISCOVERY_RECEIPT.md and outputs/evidence/.

## Negative taxonomy and overlap

- Education/non-commercial: `course`, `khóa học`, `tutorial`, `pdf`, `definition`, `là gì`, `wiki`.
- Employment: `job`, `career`, `tuyển dụng`, `salary`, `internship`.
- Consumer/unrelated: `phone`, `gpu`, `arduino`, `repair`, unrelated chip design tools.
- Free/download/crack: `free`, `open source`, `download`, `crack`, `license key`.
- News/policy/investment: `news`, `stock`, `investment`, unless a later route explicitly supports it.
- Stock/investment Vietnamese review set: `cổ phiếu`, `đầu tư`; assess factory-investment context before any negative is applied.
- Employment/education Vietnamese review set: `việc làm`, `khóa học`, `là gì`; assess query context before applying.
- Competitor terms: excluded by default pending Bảo decision; do not bid on competitor names.

Do not blanket-negative `MES`, `ERP`, `traceability`, `quality`, `WIP` or ambiguous technical terms before observing intent. Deduplicate cross-group overlap and map each retained term to one segment/route.

## RSA copy

Each group maintains responsive search ad (RSA) copy frameworks across 4 locales: Vietnamese (VN-first canonical baseline), English (EN test framework), Simplified Chinese (zh-Hans China FDI framework), and Traditional Chinese (zh-Hant Taiwan FDI framework).
All character counts strictly follow Google Ads length rules:
- English/Latin: Headlines <= 30 characters; Descriptions <= 90 characters.
- Chinese (CJK full-width): Each CJK ideograph counts as 2 characters against Google Ads limits; Headlines <= 30 character-units (max 15 CJK); Descriptions <= 90 character-units (max 45 CJK).

### 1. Vietnamese (VN-First Canonical Baseline)

#### OSAT_LOT_TEST
Headlines (12): `OSAT: Nối dữ liệu theo lot` (26); `Traceability cho OSAT` (21); `Quản trị WIP theo lot` (21); `Kết nối test data & quality` (27); `4M1E trong một luồng dữ liệu` (28); `Đối soát cost close` (19); `MES cho vận hành OSAT` (21); `Dữ liệu test có ngữ cảnh` (24); `Theo dấu lot đến cost` (21); `Khung cơ chế OSAT` (17); `Nối quality với shopfloor` (25); `Đối chiếu pain point OSAT` (25).

Descriptions (4): `Khung cơ chế nối lot, 4M1E, test data, quality, WIP và cost close.` (66); `Đối chiếu traceability và dữ liệu vận hành trước khi chọn bước tiếp theo.` (73); `Trao đổi cách nối dữ liệu lot, chất lượng và WIP trong vận hành OSAT.` (69); `Trao đổi một pain point OSAT cụ thể, không gửi dữ liệu sản xuất qua trang.` (74).

#### FABLESS_OUTSOURCE_WIP
Headlines (12): `Quản trị outsourced WIP` (23); `Nối forecast với outsource` (26); `Datecode BIN lot rõ hơn` (23); `Theo dõi WIP gia công ngoài` (27); `Cost visibility cho Fabless` (27); `Kết nối forecast & WIP` (22); `Outsource WIP có ngữ cảnh` (25); `Quản trị lot cho Fabless` (24); `Đối chiếu dữ liệu gia công` (26); `Khung cơ chế Fabless` (20); `Nối kế hoạch với cost` (21); `Trao đổi bài toán Fabless` (25).

Descriptions (4): `Khung cơ chế nối forecast, outsourced WIP, Datecode/BIN/lot và cost.` (68); `Đối chiếu trạng thái gia công ngoài với dữ liệu kế hoạch và sản phẩm.` (69); `Trao đổi cách đối soát forecast, WIP và chi phí gia công ngoài.` (63); `Trao đổi bài toán outsource WIP, không yêu cầu gửi dữ liệu nhạy cảm.` (68).

#### ERP_MES_OT_PARTNER
Headlines (12): `Nối ERP MES và OT` (17); `Traceability xuyên hệ thống` (27); `Làm rõ data handoff` (19); `Quality data có ownership` (25); `Tích hợp ERP MES OT` (19); `Kiến trúc dữ liệu nhà máy` (25); `Đối chiếu điểm tích hợp` (23); `Kết nối IT và OT` (16); `Quản trị dữ liệu thiết bị` (25); `Khung cơ chế tích hợp` (21); `Supplier SI: Nối dữ liệu` (24); `Trao đổi bài toán tích hợp` (26).

Descriptions (4): `Xác định nguồn dữ liệu, ownership và handoff giữa ERP, MES và OT.` (65); `Đặt quality và traceability vào đúng điểm giao nhận dữ liệu.` (60); `Trao đổi phạm vi tích hợp và điểm giao nhận dữ liệu ERP, MES, OT.` (65); `Bắt đầu từ một điểm nối đang vướng trong vận hành nhà máy.` (58).

### 2. English (EN Test Framework)

#### OSAT_LOT_TEST
Headlines (12): `OSAT Lot Traceability` (21); `Semiconductor Lot Tracking` (26); `Wafer Lot Genealogy` (19); `Test Data & Quality Flow` (24); `4M1E Shopfloor Context` (22); `Real-Time Lot Traceability` (26); `MES for OSAT Operations` (23); `Contextual Test Data` (20); `Lot-Level Cost Accounting` (25); `OSAT Architecture Framework` (27); `Bridge Quality & Shopfloor` (26); `Resolve OSAT Bottlenecks` (24).

Descriptions (4): `Connect lot genealogy, 4M1E, test data, WIP and cost closing in one unified model.` (82); `Map operational traceability and test yield data before selecting execution steps.` (82); `Explore verified enterprise semiconductor architecture for OSAT manufacturing plants.` (85); `Discuss specific OSAT operational challenges without sending sensitive production data.` (87).

#### FABLESS_OUTSOURCE_WIP
Headlines (12): `Fabless Outsourced WIP` (22); `Semiconductor Outsource WIP` (27); `Wafer Foundry WIP Visibility` (28); `Connect Forecast & WIP Flow` (27); `Datecode & BIN Lot Tracking` (27); `Fabless Production Planning` (27); `Chip Subcontract Tracking` (25); `Outsource Lot Management` (24); `Yield Visibility for Fabless` (28); `Fabless Multi-Tier BOM` (22); `End-to-End Wafer Trace` (22); `Control Chip Outsource Cost` (27).

Descriptions (4): `Bridge design forecast, outsourced foundry WIP, packaging test and final inventory.` (83); `Gain multi-tier visibility across external OSAT and foundry production stages.` (78); `Track Datecode, BIN split and lot genealogy without manual spreadsheet overhead.` (80); `Discuss fabless WIP tracking architecture without exposing proprietary design files.` (84).

#### ERP_MES_OT_PARTNER
Headlines (12): `Semiconductor ERP MES OT` (24); `Factory IT & OT Integration` (27); `Electronics MES Partner` (23); `Shopfloor Data Architecture` (27); `Define IT-OT Data Ownership` (27); `Equipment OT Integration` (24); `End-to-End Traceability SI` (26); `Industrial Automation Partner` (29); `Vietnam Factory ERP MES` (23); `Automated Equipment Context` (27); `Quality Data Handoff Flow` (25); `Semiconductor SI Partner` (24).

Descriptions (4): `Define clear data ownership and interface boundaries across ERP, MES and shopfloor OT.` (86); `Embed quality control and lot traceability at critical equipment data handoff points.` (85); `Bridge industrial automation with business operations for high-tech Vietnam plants.` (83); `Explore technical integration architecture based on verified engineering mechanisms.` (84).

### 3. Simplified Chinese (zh-Hans China FDI Framework)

#### OSAT_LOT_TEST
Headlines (12): `半导体封测批次追溯` (18); `OSAT 批次与品质追踪` (19); `晶圆级 4M1E 追溯体系` (20); `打线接合与测试数据串联` (22); `封测厂 MES 制造系统` (19); `建立芯片批次谱系` (16); `实时监测良率与SPC` (17); `封测精细化成本核算` (18); `封测制造数据底座` (16); `机台配方参数闭环管理` (20); `快速响应客户批次审核` (20); `对接车规级追溯标准` (18).

Descriptions (4): `贯通芯片批次谱系、4M1E设备参数、测试数据与在制品成本，实现车规级透明追溯。` (74); `在决定下一步前，梳理封测车间工序流转与实时良率异常，优化交付周期。` (66); `立足鼎捷40年制造底蕴，为越南中资与外资半导体工厂构筑合规数字化基石。` (68); `深入探讨具体封测运营难点，无需在网页上传敏感生产数据，保障核心资产。` (68).

#### FABLESS_OUTSOURCE_WIP
Headlines (12): `无晶圆厂外包在制品` (18); `委外晶圆与封测进度追踪` (22); `贯通预测与外包生产排程` (22); `Datecode与BIN分料管理` (21); `芯片代工生产协同平台` (20); `跨委外厂在制品库存可视` (22); `Fabless 晶圆批次追溯` (20); `外包良率与损耗实时监控` (22); `多阶半导体 BOM 架构` (19); `委外成本精细分摊核算` (20); `缩短芯片客户交付周期` (20); `Fabless 数字化运营架构` (22).

Descriptions (4): `连接销售预测、代工厂晶圆流转、外包封测进度与在制品成本，消除外包黑盒。` (70); `跨越外部晶圆厂与封测厂数据壁垒，掌握实时 Datecode 与 BIN 级批次流向。` (69); `摆脱繁琐手工 Excel 汇总，构建无晶圆芯片设计企业高韧性供应链协同底座。` (69); `交流芯片委外加工管理方案，无需在网页提供敏感电路设计或客户私密信息。` (68).

#### ERP_MES_OT_PARTNER
Headlines (12): `半导体 ERP MES OT 集成` (22); `工厂 IT 与 OT 深度互联` (22); `打通设备机台与企业系统` (22); `电子制造 MES 实施伙伴` (21); `厘清跨系统数据交接职责` (22); `自动化车间数据集成底座` (22); `越南工厂数字化整合专家` (22); `构筑车规级质量追溯链` (20); `设备互联与生产调度闭环` (22); `减少跨系统数据孤岛断层` (22); `半导体生态 SI 合作方案` (22); `制造业数字化落地咨询` (20).

Descriptions (4): `明确 ERP、MES 与车间底层 OT 之间的数据归属权与握手协议，杜绝信息孤岛。` (70); `将品质追溯与批次防错嵌入关键工序交接点，确保工业生产数据真实可信。` (66); `凭借在越深厚落地经验，助力电子与半导体制造企业构建稳固高效的集成底座。` (70); `从现有车间痛点切入探讨集成蓝图，纯技术架构推演，无需提供商业机密。` (66).

### 4. Traditional Chinese (zh-Hant Taiwan FDI Framework)

#### OSAT_LOT_TEST
Headlines (12): `半導體封測批次追溯` (18); `OSAT 批號與品質追蹤` (19); `晶圓級 4M1E 追溯體系` (20); `打線接合與測試數據串聯` (22); `封測廠 MES 製造系統` (19); `建立晶片批次譜系` (16); `即時監測良率與SPC` (17); `封測精細化成本結算` (18); `封測製造數據底座` (16); `機台配方參數閉環管理` (20); `快速響應客戶稽核審查` (20); `對接車規級追溯標準` (18).

Descriptions (4): `貫通晶片批號譜系、4M1E機台參數、測試數據與在製品成本，落實車規級透明追溯。` (74); `在評估下一步前，釐清封測現場工序流轉與即時良率異常，優化訂單交期。` (66); `立足鼎捷40年製造積累，為越南台資半導體封測廠打造高彈性數位化運營基石。` (70); `深入交流封測運營痛點，無需在網頁上傳機密生產數據，守護企業核心資產。` (68).

#### FABLESS_OUTSOURCE_WIP
Headlines (12): `無晶圓廠委外在製品` (18); `委外晶圓與封測進度追蹤` (22); `貫通預測與委外生產排程` (22); `Datecode與BIN分料管理` (21); `晶片代工生產協同平台` (20); `跨委外廠在製品庫存可視` (22); `Fabless 晶圓批次追溯` (20); `委外良率與損耗即時監控` (22); `多階半導體 BOM 架構` (19); `委外成本精細分攤結算` (20); `縮短晶片客戶交貨週期` (20); `Fabless 數位化運營架構` (22).

Descriptions (4): `串聯銷售預測、晶圓代工進度、外包封測在製品與結算成本，打破外包黑盒子。` (70); `跨越外部晶圓代工廠與封測廠數據孤島，掌握精確 Datecode 與 BIN 級批號。` (69); `揮別繁雜手工 Excel 對帳，構建 IC 設計公司高彈性供應鏈運營協同平台。` (67); `共同探討晶片委外管理架構，無需在網頁提交敏感電路圖紙或商業核心機密。` (68).

#### ERP_MES_OT_PARTNER
Headlines (12): `半導體 ERP MES OT 整合` (22); `工廠 IT 與 OT 深度互聯` (22); `打通設備機台與企業系統` (22); `電子製造 MES 導入夥伴` (21); `釐清跨系統數據交接職責` (22); `自動化車間數據整合底座` (22); `越南工廠數位化整合專家` (22); `構築車規級品質追溯鏈` (20); `設備聯網與生產排程閉環` (22); `消除跨系統資訊孤島斷層` (22); `半導體生態 SI 合作方案` (22); `製造業數位化落地諮詢` (20).

Descriptions (4): `明確 ERP、MES 與現場底層 OT 之間的數據權責與介面協定，杜絕資訊斷層。` (68); `將品質追溯與批號防錯機制嵌入關鍵製程交接點，確保現場運營數據真實可信。` (70); `憑藉鼎捷40年製造底蘊，協助電子與半導體供應鏈夥伴構建穩固高效的整合體系。` (72); `從現有車間瓶頸切入探討架構藍圖，純技術機制推演，無需提供商業機密。` (66).

## Extensions and sitelinks across 4 locales

### Callouts (4 per locale)
- **VI:** `Truy xuất theo lot`; `Đối soát WIP`; `Kết nối ERP MES OT`; `Trao đổi vận hành`.
- **EN:** `Lot Traceability`; `WIP Visibility`; `ERP MES OT Integration`; `Shopfloor Focus`.
- **zh-Hans:** `批次追溯`; `40年制造底蕴`; `在制品可视`; `聚焦车间痛点`.
- **zh-Hant:** `批號追溯`; `40年製造底蘊`; `在製品可視`; `聚焦現場痛點`.

### Sitelinks (3 per locale with language parameter)
- **VI:** `Khung OSAT` -> `/osat-lot-test-traceability?lang=vi`; `Outsource WIP` -> `/fabless-outsourced-wip?lang=vi`; `Data handoff ERP-MES` -> `/semiconductor-erp-mes-ot?lang=vi`.
- **EN:** `OSAT Lot Traceability` -> `/osat-lot-test-traceability?lang=en`; `Fabless Outsource WIP` -> `/fabless-outsourced-wip?lang=en`; `ERP MES OT Integration` -> `/semiconductor-erp-mes-ot?lang=en`.
- **zh-Hans:** `封测批次追溯` -> `/osat-lot-test-traceability?lang=zh-Hans`; `委外在制品管理` -> `/fabless-outsourced-wip?lang=zh-Hans`; `ERP MES OT 集成` -> `/semiconductor-erp-mes-ot?lang=zh-Hans`.
- **zh-Hant:** `封測批號追溯` -> `/osat-lot-test-traceability?lang=zh-Hant`; `委外在製品管理` -> `/fabless-outsourced-wip?lang=zh-Hant`; `ERP MES OT 整合` -> `/semiconductor-erp-mes-ot?lang=zh-Hant`.

## Multilingual readiness status

Offline character validation covers RSA text lengths only; native terminology, exact claim scope and platform readiness remain pending. Keyword Planner verification for the 21 listed EN/ZH seed candidates was completed on 2026-09-30; no displayed metrics were returned. Live campaign deployment remains blocked pending PO enablement, account permission and the remaining terminology, landing, overlap and launch gates.


## Offline reconciliation notes (2026-09-30)
Governance: do not publish unverified cases, outcomes or expanded claims. These instructions are metadata, never RSA descriptions or callout text.
The 40-year heritage claim is not a 40-year Vietnam deployment claim. Native review and proof scope remain launch gates.
Search sitelink paths above are historical draft destinations and **NOT BUILD-READY**. No evidence establishes that those paths are valid public aliases. Resolve them against the published route ledger (`/semiconductor-osat`, `/fabless`, `/supplierecosystem`) and verify locale, UTM and gclid before import; this slice makes no live URL claim.
Provisional max CPC 25,000 VND is a draft bid setting. Adapter monitoring proposals (35,000 VND CPC / 3.5% CTR and 45,000 VND escalation) are distinct, unapproved thresholds, not automatic pause rules. The Search 250k/day bucket and LI 600k / reserve 150k split remain proposals.
