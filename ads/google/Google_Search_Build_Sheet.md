# Google Search Build Sheet

**Status:** offline production draft; no remote campaign creation, enablement or spend. Campaign target state remains paused. One fresh Vietnamese-first OSAT Keyword Planner query returned no displayed metrics (`OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`). Fabless and ERP–MES–OT/partner queries remain pending. A “Get results” query automatically created one draft plan entry; no explicit save was clicked, and no further query was run.

## Campaign structure

- One campaign; status **paused**.
- Ad groups: `OSAT_LOT_TEST`, `FABLESS_OUTSOURCE_WIP`, `ERP_MES_OT_PARTNER`.
- Exact and phrase only; Vietnam presence-only; Vietnamese and English; Search Network only.
- Display **OFF**; Search Partners **OFF**.
- Draft bidding: Maximize Clicks; provisional max CPC `25,000 VND`; no conversion-based bidding.
- Micro conversions are reporting-only, never primary Google Ads conversions.
- UTM: `utm_source=google`, `utm_medium=cpc`, `utm_campaign=vn_semiconductor_search_p1`, `utm_content=<segment>_rsa_<variant>`, `utm_term={keyword}`; preserve auto-tagging/gclid.

## Keyword hypotheses

Every set is **HYPOTHESIS_PENDING_KEYWORD_PLANNER**; none is retained or validated. Account-grounded sanitized observation: authenticated account context showed ERP/MES/manufacturing adjacency but no observed direct OSAT terms. No private metrics or campaign names are recorded.

| Ad group | Candidate exact/phrase themes (8–15 target after Keyword Planner) |
|---|---|
| OSAT_LOT_TEST | `OSAT lot tracking`; `semiconductor lot tracking`; `wafer lot traceability`; `IC lot genealogy`; `semiconductor production traceability`; `outsourced assembly test tracking`; `OSAT traceability software`; `semiconductor test data management` |
| FABLESS_OUTSOURCE_WIP | `fabless WIP tracking`; `semiconductor outsourced WIP`; `foundry WIP management`; `chip manufacturing WIP`; `subcontract manufacturing tracking`; `fabless production planning`; `outsourced semiconductor production`; `Datecode BIN lot management` |
| ERP_MES_OT_PARTNER | `semiconductor ERP MES integration`; `MES implementation partner semiconductor`; `electronics manufacturing ERP`; `MES integration partner Vietnam`; `ERP MES OT integration`; `factory data integration partner`; `semiconductor quality traceability`; `industrial automation MES partner` |

Validate language, geography, match type, search volume, competition, CPC, search terms and overlap in Keyword Planner/account UI. **Historical UI evidence (2026-09-11):** Campaigns, Ad groups, Settings and Keyword Planner were observed functional; the orange `GOOGLE_ADS_GOAL_UPDATE_BANNER / INFORMATIONAL / NON_BLOCKING` was informational; the six supplied English OSAT seeds returned no displayed metrics (`OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`). These are historical observations, not current validation or demand evidence.

**Current Planner evidence (2026-09-14, Asia/Ho_Chi_Minh):** screenshots showed no ad-blocker dialog. The string remained in the accessibility/DOM tree as a false signal; direct navigation and the Keyword Planner query form worked. Classify `OBSERVED_DOM_FALSE_SIGNAL_NON_BLOCKING`, not a visible modal or blocker. The orange Vietnamese goal/budget mechanism-update banner was visible and informational. Query configuration was Vietnam, Vietnamese, Google, Sep 2025–Aug 2026, with adult ideas excluded. For the OSAT lot/test/traceability seed cluster, all displayed metric fields were dashes and the chart/related-idea panel showed no data. Record `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`; do not infer zero demand. The query generated one draft plan entry automatically despite no explicit save click. Further queries await an explicit decision/mandate on accepting additional automatically created Planner draft entries; this is a scope/side-effect gate, not an ad-blocker or platform failure. No campaign was created or modified, no settings changed, and no enablement or spend occurred. This is not a validated account-wide failure. Geography, language, network and auto-tagging for any campaign remain unverified.

## Negative taxonomy and overlap

- Education/non-commercial: `course`, `khóa học`, `tutorial`, `pdf`, `definition`, `là gì`, `wiki`.
- Employment: `job`, `career`, `tuyển dụng`, `salary`, `internship`.
- Consumer/unrelated: `phone`, `gpu`, `arduino`, `repair`, unrelated chip design tools.
- Free/download/crack: `free`, `open source`, `download`, `crack`, `license key`.
- News/policy/investment: `news`, `stock`, `investment`, unless a later route explicitly supports it.
- Competitor terms: excluded by default pending Bảo decision; do not bid on competitor names.

Do not blanket-negative `MES`, `ERP`, `traceability`, `quality`, `WIP` or ambiguous technical terms before observing intent. Deduplicate cross-group overlap and map each retained term to one segment/route.

## RSA copy

Each group has one VN-first RSA with exactly 12 headlines and 4 descriptions. Character counts below are Unicode code points; all are within the Google limits of <=30 headline characters and <=90 description characters.

### OSAT_LOT_TEST

Headlines (12): `OSAT: Nối dữ liệu theo lot` (26); `Traceability cho OSAT` (21); `Quản trị WIP theo lot` (21); `Kết nối test data & quality` (27); `4M1E trong một luồng dữ liệu` (28); `Đối soát cost close` (19); `MES cho vận hành OSAT` (21); `Dữ liệu test có ngữ cảnh` (24); `Theo dấu lot đến cost` (21); `Khung cơ chế OSAT` (17); `Nối quality với shopfloor` (25); `Đối chiếu pain point OSAT` (25).

Descriptions (4): `Khung cơ chế nối lot, 4M1E, test data, quality, WIP và cost close.` (66); `Đối chiếu traceability và dữ liệu vận hành trước khi chọn bước tiếp theo.` (73); `Không dùng case, số liệu hay kết quả chưa được xác minh trong bản này.` (70); `Trao đổi một pain point OSAT cụ thể, không gửi dữ liệu sản xuất qua trang.` (74).

### FABLESS_OUTSOURCE_WIP

Headlines (12): `Quản trị outsourced WIP` (23); `Nối forecast với outsource` (26); `Datecode BIN lot rõ hơn` (23); `Theo dõi WIP gia công ngoài` (27); `Cost visibility cho Fabless` (27); `Kết nối forecast & WIP` (22); `Outsource WIP có ngữ cảnh` (25); `Quản trị lot cho Fabless` (24); `Đối chiếu dữ liệu gia công` (26); `Khung cơ chế Fabless` (20); `Nối kế hoạch với cost` (21); `Trao đổi bài toán Fabless` (25).

Descriptions (4): `Khung cơ chế nối forecast, outsourced WIP, Datecode/BIN/lot và cost.` (68); `Đối chiếu trạng thái gia công ngoài với dữ liệu kế hoạch và sản phẩm.` (69); `Mechanism-only: chưa dùng tên khách hàng, case hoặc kết quả chưa xác minh.` (74); `Trao đổi bài toán outsource WIP, không yêu cầu gửi dữ liệu nhạy cảm.` (68).

### ERP_MES_OT_PARTNER

Headlines (12): `Nối ERP MES và OT` (17); `Traceability xuyên hệ thống` (27); `Làm rõ data handoff` (19); `Quality data có ownership` (25); `Tích hợp ERP MES OT` (19); `Kiến trúc dữ liệu nhà máy` (25); `Đối chiếu điểm tích hợp` (23); `Kết nối IT và OT` (16); `Quản trị dữ liệu thiết bị` (25); `Khung cơ chế tích hợp` (21); `Supplier SI: Nối dữ liệu` (24); `Trao đổi bài toán tích hợp` (26).

Descriptions (4): `Xác định nguồn dữ liệu, ownership và handoff giữa ERP, MES và OT.` (65); `Đặt quality và traceability vào đúng điểm giao nhận dữ liệu.` (60); `Architecture hypothesis only; phạm vi tích hợp cần discovery thực tế.` (69); `Bắt đầu từ một điểm nối đang vướng trong vận hành nhà máy.` (58).

## Extensions and blockers

Callouts (4): `Mechanism-first`; `Vietnamese-first`; `Không claim chưa duyệt`; `Đối chiếu pain point`.

Sitelinks (3): `Khung OSAT` -> `/osat-lot-test-traceability`; `Outsource WIP` -> `/fabless-outsourced-wip`; `Data handoff ERP-MES` -> `/semiconductor-erp-mes-ot`. Descriptions map to the corresponding route and segment.

No English RSA is prepared unless later evidence shows English demand. No campaign is created because English demand metrics, overlap and live auto-tagging remain unverified; the current no-metrics Keyword Planner result is not a blocker.
