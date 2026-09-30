# Vy LinkedIn four-locale source-copy register — offline candidates

**Date/revision:** 2026-09-29, base `a71acbc`. **Owner:** S5 creative copy. **Status:** four-locale copy candidates; Stage A localized square SVG/PNG and OSAT PDFs rendered offline, with layout/source checks below. Native semiconductor/market review and platform export QA remain open. Bảo selected three languages/four variants: `vi`, `en`, `zh-Hans` for China FDI, `zh-Hant` for Taiwan FDI. S1's FDI/domestic account criteria remain provisional. Bảo selected a non-PII `lang` query parameter on each existing route URL for paid-entry initial locale; the top switch remains the visitor control. Destination runtime behavior is not QA'd here. Bảo confirmed on 2026-09-29 that case/claim already present in the Vietnamese source has management approval for use and full translation; native wording and exact source scope remain review requirements, but this existing-source claim approval is not an outstanding rights gate. No new or broader claim is authorized by this statement.

## Coverage and asset mapping

| Source family | Canonical offline inputs | Four-variant output here | Render/export gap |
|---|---|---|---|
| OSAT static | `osat-square.svg`; `final/osat-square.png`; `final/osat-linkedin-b2b-v2.png` | OSAT copy candidate × `vi/en/zh-Hans/zh-Hant` | EN/Hans/Hant square SVG + 1200² PNG and VI/Hans/Hant 1254² b2b-v2 raster candidates rendered and inspected. Original EN b2b-v2 remains. Native/platform/alt/mobile QA remains. |
| Fabless static | `fabless-square.svg`; `final/fabless-square.png`; `final/fabless-linkedin-b2b-v2.png` | Fabless copy candidate × four | EN/Hans/Hant square SVG + PNG and VI/Hans/Hant b2b-v2 raster candidates rendered and inspected; native/platform/alt/mobile QA remains. |
| Supplier/Partner static | `partner-square.svg`; `final/partner-square.png`; `final/partner-linkedin-b2b-v2.png` | Partner copy candidate × four | EN/Hans/Hant square SVG + PNG and VI/Hans/Hant b2b-v2 raster candidates rendered and inspected; native/platform/alt/mobile QA remains. |
| OSAT document | `osat-document-ad-6p-copy.md`; `output/pdf/digiwin-osat-document-ad-6p.pdf` | Page-by-page source-line candidate × four | Three EN/Hans/Hant A4 six-page PDFs rendered and visually/text checked; native review and account-format acceptance remain. |
| Proof carousel | `carousel-proof-pre-generation-brief.md`; four `final/carousel-car-0{1..4}-*.png` | Four card messages × four | Twelve EN/Hans/Hant metric-free raster candidates rendered at 1254×1254; VI remains copy-only. Original English v1 metric files stay untouched. Active-account export specification, native wording and mobile crop QA pending. |

This is **3 static concepts × 4 variants**, **6 document pages × 4 variants**, and **4 cards × 4 variants** at copy level. Stage A added EN/Hans/Hant rendered square and document outputs; Stage B added VI/Hans/Hant b2b-v2 raster candidates and EN/Hans/Hant metric-free carousel candidates. Original source files remain untouched. VI carousel cards remain copy-only. Every delivered creative record later needs image text, platform headline/body/CTA (if supported), alt text/metadata, source ID, target market, destination variant signal and approval state. No account object or placement capability is assumed.

**B2B-v2 Vietnamese text audit:** the raster candidates translate descriptive English retained as technical shorthand in the square-SVG ledger. OSAT uses `theo lô`, `4M1E · dữ liệu kiểm thử · chất lượng · WIP · kết sổ chi phí`, nodes `LÔ / KIỂM THỬ / CHẤT LƯỢNG / CHI PHÍ` and footer `Từ lô đến kết sổ chi phí, theo một mạch đối chiếu`. Fabless uses `WIP gia công ngoài`, `dự báo · mã ngày · BIN · lô · chi phí` and nodes `DỰ BÁO / WIP GIA CÔNG NGOÀI / CHI PHÍ`. Supplier uses `giao nhận dữ liệu · trách nhiệm · chất lượng · truy vết` and nodes `ERP / NGUỒN`, `MES / GIAO NHẬN`, `OT / HÀNH ĐỘNG`. These are scope-preserving Vietnamese render choices; brand, product/technical acronyms remain. Native terminology review still applies.

| Creative family | Existing destination path | Approved initial-locale parameter values for future QA |
|---|---|---|
| OSAT static/document | `/semiconductor-osat` | `?lang=vi`, `?lang=en`, `?lang=zh-Hans`, `?lang=zh-Hant` |
| Fabless static | `/fabless` | same four values |
| Supplier/Partner static | `/supplierecosystem` | same four values |
| Proof carousel | Destination route must be chosen from the card's actual ad promise and approved audience | same four values on the selected existing route; do not assume one carousel-wide route |

These are relative URL design examples, not tested destinations. Append the `lang` parameter alongside existing non-PII UTMs and `gclid` using correct query joining/encoding; do not overwrite them. Do not assign a China/Taiwan target company from script alone.

## Static route concepts — copy candidates

These describe an operating question or mechanism, not a verified outcome. Keep in-image acronym labels (`OSAT`, `ERP`, `MES`, `OT`, `WIP`, `BIN`, `4M1E`) consistent with the route glossary after review. The current SVG line breaks are Vietnamese-specific and cannot be reused mechanically.

| Route / variant | Main image headline | Support line | Suggested ad body / consultation intent |
|---|---|---|---|
| OSAT · vi | OSAT: Nối dữ liệu theo lô | Lot · test · chất lượng · WIP · chốt chi phí | Cùng xem một câu hỏi truy vết cụ thể: dữ liệu nào cần nối và ai cần đối chiếu? Trao đổi bài toán OSAT. |
| OSAT · en | OSAT: Connect data by lot | Lot · test · quality · WIP · cost close | Explore one traceability question: which records need to connect, and who reviews them? Discuss an OSAT operating question. |
| OSAT · zh-Hans | OSAT：按批次梳理数据 | 批次 · 测试 · 质量 · 在制品 · 成本结算 | 从一个具体追溯问题出发，梳理需要关联的数据与审核责任。交流 OSAT 运营问题。 |
| OSAT · zh-Hant | OSAT：依批次梳理資料 | 批次 · 測試 · 品質 · 在製品 · 成本結算 | 從一個具體追溯問題出發，梳理需要關聯的資料與檢視責任。討論 OSAT 營運問題。 |
| Fabless · vi | Làm rõ WIP gia công ngoài | Dự báo · lô/datecode/BIN · trạng thái · chi phí | Xem cách đối chiếu tiến độ đối tác với dữ liệu sản phẩm và kế hoạch. Trao đổi bài toán Fabless. |
| Fabless · en | Clarify outsourced WIP | Forecast · lot/datecode/BIN · status · cost | Explore how partner progress can be reviewed alongside product and planning data. Discuss a Fabless operating question. |
| Fabless · zh-Hans | 梳理委外在制品状态 | 预测 · 批次/日期码/BIN · 进度 · 成本 | 探讨如何将合作方进度与产品及计划数据放在同一视角核对。交流 Fabless 运营问题。 |
| Fabless · zh-Hant | 梳理委外在製品狀態 | 預測 · 批次/日期碼/BIN · 進度 · 成本 | 探討如何將合作夥伴進度與產品及規劃資料放在同一視角檢視。討論 Fabless 營運問題。 |
| Partner · vi | Làm rõ điểm nối ERP–MES–OT | Nguồn dữ liệu · bàn giao · trách nhiệm | Khảo sát ranh giới dữ liệu và trách nhiệm trong một bài toán tích hợp cụ thể. Tư vấn. |
| Partner · en | Clarify ERP–MES–OT handoffs | Data source · handoff · ownership | Explore data and ownership boundaries in one integration question. Discuss an integration need. |
| Partner · zh-Hans | 梳理 ERP–MES–OT 数据交接 | 数据来源 · 交接 · 责任边界 | 从一个具体集成问题出发，厘清数据与责任边界。交流集成需求。 |
| Partner · zh-Hant | 梳理 ERP–MES–OT 資料交接 | 資料來源 · 交接 · 責任邊界 | 從一個具體整合問題出發，釐清資料與責任邊界。討論整合需求。 |

**Static layout text inventory:** the tables below provide copy for each SVG `<title>`, `<desc>` and `<text>` node in source order. Review the b2b-v2 PNGs separately because no editable source for those derivatives is inventoried. A generic platform CTA is a candidate only; exact LinkedIn CTA menu/character constraints need active-account evidence. Supplier's landing has one consultation CTA only, `partner-cta-header`; ad wording must not imply extra landing CTAs.

### Complete square-SVG node copy

Each row maps one source node; repeated tokens such as `LOT`, `TEST`, `ERP` and `COST` remain technical labels. Layout line breaks must be re-set per script, not copied from the Vietnamese SVG. The source SVG and its current PNG remain unchanged.

| OSAT source node | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| `<title>` | Cơ chế truy vết OSAT | OSAT traceability mechanism | OSAT 追溯机制 | OSAT 追溯機制 |
| `<desc>` | Minh họa luồng đối chiếu dữ liệu lot, test, quality, WIP và cost close. | Diagram of the data review flow across lot, test, quality, WIP and cost close. | 批次、测试、质量、在制品与成本结算数据核对流程示意。 | 批次、測試、品質、在製品與成本結算資料檢視流程示意。 |
| Eyebrow | VẬN HÀNH BÁN DẪN | SEMICONDUCTOR OPERATIONS | 半导体运营 | 半導體營運 |
| Heading line 1 | OSAT: Nối dữ liệu | OSAT: Connect data | OSAT：关联数据 | OSAT：串聯資料 |
| Heading line 2 | theo lot | by lot | 按批次 | 依批次 |
| Detail rail | 4M1E · test data · quality · WIP · cost close | 4M1E · test data · quality · WIP · cost close | 4M1E · 测试数据 · 质量 · 在制品 · 成本结算 | 4M1E · 測試資料 · 品質 · 在製品 · 成本結算 |
| Diagram 1 | LOT | LOT | 批次 | 批次 |
| Diagram 2 | TEST | TEST | 测试 | 測試 |
| Diagram 3 | QUALITY | QUALITY | 质量 | 品質 |
| Diagram 4 | COST | COST | 成本 | 成本 |
| Body | Một khung cơ chế để đối chiếu traceability và câu hỏi vận hành. | A framework to review traceability and an operating question. | 用于核对追溯链与运营问题的机制框架。 | 用於檢視追溯鏈與營運問題的機制框架。 |
| Prompt | Đối chiếu một pain point OSAT cụ thể | Review one specific OSAT operating issue | 核对一个具体的 OSAT 运营问题 | 檢視一個具體的 OSAT 營運問題 |
| Footer | Từ lot đến cost close, theo một mạch đối chiếu | From lot to cost close in one review thread | 从批次到成本结算，沿同一条核对链 | 從批次到成本結算，沿同一條檢視脈絡 |

| Fabless source node | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| `<title>` | Cơ chế quản trị WIP gia công ngoài Fabless | Fabless outsourced WIP mechanism | Fabless 委外在制品机制 | Fabless 委外在製品機制 |
| `<desc>` | Minh họa luồng đối chiếu forecast, outsourced WIP và cost cho Fabless. | Diagram of the Fabless review flow across forecast, outsourced WIP and cost. | Fabless 预测、委外在制品与成本核对流程示意。 | Fabless 預測、委外在製品與成本檢視流程示意。 |
| Eyebrow | THƯƠNG MẠI HÓA FABLESS | FABLESS COMMERCIALIZATION | FABLESS 商业化 | FABLESS 商業化 |
| Heading line 1 | Quản trị | Manage | 管理 | 管理 |
| Heading line 2 | outsourced WIP | outsourced WIP | 委外在制品 | 委外在製品 |
| Detail rail | forecast · Datecode · BIN · lot · cost | forecast · datecode · BIN · lot · cost | 预测 · 日期码 · BIN · 批次 · 成本 | 預測 · 日期碼 · BIN · 批次 · 成本 |
| Diagram 1 | FORECAST | FORECAST | 预测 | 預測 |
| Diagram 2 | OUTSOURCE WIP | OUTSOURCE WIP | 委外在制品 | 委外在製品 |
| Diagram 3 | COST | COST | 成本 | 成本 |
| Body | Nối trạng thái gia công ngoài với dữ liệu kế hoạch và sản phẩm. | Connect outsourced production status with planning and product data. | 将委外生产状态与计划及产品数据关联。 | 將委外生產狀態與規劃及產品資料串聯。 |
| Prompt | Đối chiếu bài toán Fabless | Review a Fabless operating question | 核对 Fabless 运营问题 | 檢視 Fabless 營運問題 |
| Footer | Làm rõ trạng thái, điểm giao nhận và dữ liệu đối chiếu | Clarify status, handoffs and review data | 明确状态、交接点与核对数据 | 釐清狀態、交接點與檢視資料 |

| Supplier/Partner source node | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| `<title>` | Cơ chế tích hợp ERP MES OT | ERP MES OT integration mechanism | ERP MES OT 集成机制 | ERP MES OT 整合機制 |
| `<desc>` | Minh họa điểm giao nhận dữ liệu giữa ERP, MES và OT. | Diagram of data handoffs among ERP, MES and OT. | ERP、MES 与 OT 之间的数据交接示意。 | ERP、MES 與 OT 之間的資料交接示意。 |
| Eyebrow | NHÀ CUNG CẤP · SI · TỰ ĐỘNG HÓA | SUPPLIER · SI · AUTOMATION | 供应商 · SI · 自动化 | 供應商 · SI · 自動化 |
| Heading line 1 | Nối ERP, MES | Connect ERP, MES | 连接 ERP、MES | 串接 ERP、MES |
| Heading line 2 | và OT | and OT | 与 OT | 與 OT |
| Detail rail | data handoff · ownership · quality · traceability | data handoff · ownership · quality · traceability | 数据交接 · 责任归属 · 质量 · 追溯 | 資料交接 · 責任歸屬 · 品質 · 追溯 |
| Diagram 1 | ERP | ERP | ERP | ERP |
| Diagram 2 | SOURCE | SOURCE | 来源 | 來源 |
| Diagram 3 | MES | MES | MES | MES |
| Diagram 4 | HANDOFF | HANDOFF | 交接 | 交接 |
| Diagram 5 | OT | OT | OT | OT |
| Diagram 6 | ACTION | ACTION | 动作 | 動作 |
| Prompt | Làm rõ một điểm nối đang vướng | Clarify one blocked integration handoff | 厘清一个受阻的集成交接点 | 釐清一個受阻的整合交接點 |
| Footer | Làm rõ nguồn dữ liệu, điểm giao nhận và trách nhiệm | Clarify data source, handoff and ownership | 厘清数据来源、交接点与责任 | 釐清資料來源、交接點與責任 |

## OSAT document — six-page copy register

The Vietnamese source document remains canonical for its existing PDF. The message map is followed by a source-line translation ledger covering its headings, text, tables, prompts, footer and contact panel. These are copy candidates used in the offline localized PDFs below. Preserve the verified company contact values exactly; do not place them in analytics or tracking parameters. Native wording, metadata and platform acceptance still need review.

| Page | vi headline / key line | en candidate | zh-Hans candidate | zh-Hant candidate |
|---|---|---|---|---|
| 1 cover | Nối dữ liệu theo lô để nhìn rõ câu hỏi vận hành; lot–test–quality–WIP–cost close | Connect lot-level data to frame an operating question; lot–test–quality–WIP–cost close | 关联批次层级数据，厘清运营问题；批次–测试–质量–在制品–成本结算 | 串聯批次層級資料，釐清營運問題；批次–測試–品質–在製品–成本結算 |
| 2 questions | Bắt đầu từ câu hỏi cần truy vết; xác định dữ liệu và người cần đối chiếu | Start with a traceability question; identify the records and reviewer | 从追溯问题出发；明确所需数据与审核人员 | 從追溯問題出發；明確所需資料與檢視人員 |
| 3 mechanism | Một mạch dữ liệu có thể kiểm tra; input → context → review | A reviewable data thread; input → context → review | 可供核对的数据脉络；输入 → 情境 → 复核 | 可供檢視的資料脈絡；輸入 → 脈絡 → 檢視 |
| 4 data lens | Từ lô tới bằng chứng vận hành; nguồn, người phụ trách, điều kiện xác nhận | From lot to operating evidence; source, owner, confirmation condition | 从批次到运营依据；来源、责任人、确认条件 | 從批次到營運依據；來源、負責人、確認條件 |
| 5 review cadence | Một nhịp review có thể bắt đầu nhỏ; chọn câu hỏi, dữ liệu, bước tiếp | Start a focused review: choose the question, records and next step | 从一个聚焦问题开始复核：确定问题、数据与下一步 | 從一個聚焦問題開始檢視：確認問題、資料與下一步 |
| 6 contact | Trao đổi một bài toán OSAT; không gửi dữ liệu sản xuất/khách hàng nhạy cảm | Discuss an OSAT operating question; do not send sensitive production or customer information | 交流一个 OSAT 运营问题；请勿发送敏感生产或客户资料 | 討論一個 OSAT 營運問題；請勿傳送敏感生產或客戶資料 |

The contact details in page 6 are source-verified display content, not a lead form or tracked conversion. The three localized PDFs below retain the exact source contact values and pass source-line extraction/layout checks; native terminology and platform-format review remain open.

### Document source-line translation ledger

Repeated strings use the same row on every page: `DIGIWIN · SEMICONDUCTOR OPERATIONS` → VI `DIGIWIN · VẬN HÀNH BÁN DẪN`; EN source unchanged; zh-Hans `DIGIWIN · 半导体运营`; zh-Hant `DIGIWIN · 半導體營運`. `PAGE n / 6` → VI `TRANG n / 6`; EN source unchanged; zh-Hans `第 n / 6 页`; zh-Hant `第 n / 6 頁` for n=1…6. Technical keys `LOT`, `TEST`, `QUALITY`, `COST`, `WIP`, `4M1E`, `ERP` may be retained as labels where the translated context is explicit. The original contact email, phone, street address and source URL are exact shared values in all four variants.

| Page 1 source component | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| OSAT OPERATIONS | VẬN HÀNH OSAT | OSAT OPERATIONS | OSAT 运营 | OSAT 營運 |
| Nối dữ liệu theo lot để nhìn rõ câu hỏi vận hành | Nối dữ liệu theo lot để nhìn rõ câu hỏi vận hành | Connect data by lot to clarify the operating question | 按批次关联数据，厘清运营问题 | 依批次串聯資料，釐清營運問題 |
| Một khung cơ chế cho lot, test data, 4M1E, quality, WIP và cost close. | Một khung cơ chế cho lot, test data, 4M1E, quality, WIP và cost close. | A framework for lot, test data, 4M1E, quality, WIP and cost close. | 覆盖批次、测试数据、4M1E、质量、在制品与成本结算的机制框架。 | 涵蓋批次、測試資料、4M1E、品質、在製品與成本結算的機制框架。 |
| Four table headers: LOT / TEST / QUALITY / COST | LOT / TEST / QUALITY / COST | LOT / TEST / QUALITY / COST | 批次 / 测试 / 质量 / 成本 | 批次 / 測試 / 品質 / 成本 |
| Lot · test · quality · WIP · cost close | Lot · test · quality · WIP · cost close | Lot · test · quality · WIP · cost close | 批次 · 测试 · 质量 · 在制品 · 成本结算 | 批次 · 測試 · 品質 · 在製品 · 成本結算 |

| Page 2 source component | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| 01 · CÂU HỎI VẬN HÀNH | 01 · CÂU HỎI VẬN HÀNH | 01 · OPERATING QUESTION | 01 · 运营问题 | 01 · 營運問題 |
| Bắt đầu từ câu hỏi cần truy vết | Bắt đầu từ câu hỏi cần truy vết | Start with the question that needs tracing | 从需要追溯的问题开始 | 從需要追溯的問題開始 |
| Một cuộc trao đổi hiệu quả bắt đầu từ dữ liệu nào đang rời nhau và ai cần nhìn thấy điều gì. | Một cuộc trao đổi hiệu quả bắt đầu từ dữ liệu nào đang rời nhau và ai cần nhìn thấy điều gì. | A useful discussion starts by identifying which records are disconnected and who needs to see what. | 有效讨论先明确哪些数据尚未关联，以及谁需要看到哪些信息。 | 有效討論先釐清哪些資料尚未串聯，以及誰需要看到哪些資訊。 |
| LOT GENEALOGY — Theo dõi luồng lot, các lần tách/gộp và từng điểm chuyển tiếp. | PHẢ HỆ LOT — Theo dõi luồng lot, các lần tách/gộp và từng điểm chuyển tiếp. | LOT GENEALOGY — Track lot flow, splits/merges and each handoff. | 批次谱系 — 跟踪批次流向、拆分/合并与每个交接点。 | 批次譜系 — 追蹤批次流向、拆分/合併與每個交接點。 |
| TEST DATA — Đặt kết quả test cạnh lot và quality để xem xét trong đúng ngữ cảnh. | DỮ LIỆU TEST — Đặt kết quả test cạnh lot và quality để xem xét trong đúng ngữ cảnh. | TEST DATA — Review test results alongside lot and quality in context. | 测试数据 — 将测试结果与批次和质量信息放在同一情境检视。 | 測試資料 — 將測試結果與批次和品質資訊放在同一脈絡檢視。 |
| 4M1E CONTEXT — Xem xét người, máy, vật tư và phương pháp quanh câu hỏi cần truy vết. | NGỮ CẢNH 4M1E — Xem xét người, máy, vật tư và phương pháp quanh câu hỏi cần truy vết. | 4M1E CONTEXT — Review people, machines, materials and methods around the tracing question. | 4M1E 情境 — 围绕追溯问题查看人员、设备、物料与方法。 | 4M1E 脈絡 — 圍繞追溯問題查看人員、設備、物料與方法。 |
| COST CLOSE — Đưa dữ liệu shopfloor và finance vào cùng một cuộc trao đổi về cost close. | CHỐT CHI PHÍ — Đưa dữ liệu shopfloor và finance vào cùng một cuộc trao đổi về cost close. | COST CLOSE — Bring shopfloor and finance data into the same cost-close discussion. | 成本结算 — 将车间与财务数据纳入同一成本结算讨论。 | 成本結算 — 將現場與財務資料納入同一成本結算討論。 |
| Nguồn dữ liệu nào? Ngữ cảnh nào đang thiếu? Ai chịu trách nhiệm? Bước review nào cần làm rõ? | Nguồn dữ liệu nào? Ngữ cảnh nào đang thiếu? Ai chịu trách nhiệm? Bước review nào cần làm rõ? | Which data source? What context is missing? Who is responsible? Which review step needs clarification? | 数据来自哪里？缺少什么情境？由谁负责？哪个核对步骤需要厘清？ | 資料來自哪裡？缺少什麼脈絡？由誰負責？哪個檢視步驟需要釐清？ |

| Page 3 source component | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| 02 · CƠ CHẾ ĐỐI CHIẾU | 02 · CƠ CHẾ ĐỐI CHIẾU | 02 · REVIEW MECHANISM | 02 · 核对机制 | 02 · 檢視機制 |
| Một mạch dữ liệu có thể kiểm tra | Một mạch dữ liệu có thể kiểm tra | A reviewable data thread | 可供核对的数据脉络 | 可供檢視的資料脈絡 |
| Nối các điểm dữ liệu theo câu hỏi vận hành, từ đầu vào đến ngữ cảnh và bước review. | Nối các điểm dữ liệu theo câu hỏi vận hành, từ đầu vào đến ngữ cảnh và bước review. | Connect data points around the operating question, from input through context to review. | 围绕运营问题关联数据点，从输入、情境到核对。 | 圍繞營運問題串聯資料點，從輸入、脈絡到檢視。 |
| 01 · INPUT: Lot / Test | 01 · ĐẦU VÀO: Lot / Test | 01 · INPUT: Lot / Test | 01 · 输入：批次 / 测试 | 01 · 輸入：批次 / 測試 |
| 02 · CONTEXT: 4M1E / Quality | 02 · NGỮ CẢNH: 4M1E / Quality | 02 · CONTEXT: 4M1E / Quality | 02 · 情境：4M1E / 质量 | 02 · 脈絡：4M1E / 品質 |
| 03 · REVIEW: WIP / Cost close | 03 · ĐỐI CHIẾU: WIP / Cost close | 03 · REVIEW: WIP / Cost close | 03 · 核对：在制品 / 成本结算 | 03 · 檢視：在製品 / 成本結算 |
| Đối chiếu lot, test, quality, WIP và cost close trong cùng một nhịp review. | Đối chiếu lot, test, quality, WIP và cost close trong cùng một nhịp review. | Review lot, test, quality, WIP and cost close in one cadence. | 在同一核对节奏中查看批次、测试、质量、在制品与成本结算。 | 在同一檢視節奏中查看批次、測試、品質、在製品與成本結算。 |

| Page 4 source component | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| 03 · LỚP DỮ LIỆU | 03 · LỚP DỮ LIỆU | 03 · DATA LAYERS | 03 · 数据层 | 03 · 資料層 |
| Từ lot tới bằng chứng vận hành | Từ lot tới bằng chứng vận hành | From lot to operating evidence | 从批次到运营依据 | 從批次到營運依據 |
| Mỗi lớp dữ liệu trả lời một phần câu hỏi, từ vị trí lot đến test, WIP và cost close. | Mỗi lớp dữ liệu trả lời một phần câu hỏi, từ vị trí lot đến test, WIP và cost close. | Each data layer answers part of the question, from lot position through test and WIP to cost close. | 每个数据层回答问题的一部分，从批次位置、测试、在制品到成本结算。 | 每個資料層回答問題的一部分，從批次位置、測試、在製品到成本結算。 |
| Table headers: Lớp / Câu hỏi / Điểm review | Lớp / Câu hỏi / Điểm review | Layer / Question / Review point | 层级 / 问题 / 核对点 | 層級 / 問題 / 檢視點 |
| Lot: Lot đang ở đâu và đã đi qua điểm nào? Genealogy / split-merge | Lot: Lot đang ở đâu và đã đi qua điểm nào? Genealogy / split-merge | Lot: Where is the lot and which points has it passed? Genealogy / split-merge | 批次：目前在哪里，经过哪些节点？谱系 / 拆分与合并 | 批次：目前在哪裡，經過哪些節點？譜系 / 拆分與合併 |
| Test: Kết quả test gắn với lot và quality thế nào? Context / bất thường | Test: Kết quả test gắn với lot và quality thế nào? Context / bất thường | Test: How do results relate to lot and quality? Context / anomalies | 测试：结果如何关联批次与质量？情境 / 异常 | 測試：結果如何關聯批次與品質？脈絡 / 異常 |
| WIP: Trạng thái đang chờ ở đâu và ai cần biết? Handoff / trách nhiệm | WIP: Trạng thái đang chờ ở đâu và ai cần biết? Handoff / trách nhiệm | WIP: Where is work waiting, and who needs to know? Handoff / ownership | 在制品：哪里处于等待状态，谁需要知晓？交接 / 责任 | 在製品：哪裡處於等待狀態，誰需要知悉？交接 / 責任 |
| Cost: Dữ liệu nào cần cho cost close? Shopfloor / finance review | Cost: Dữ liệu nào cần cho cost close? Shopfloor / finance review | Cost: Which data are needed for cost close? Shopfloor / finance review | 成本：结算需要哪些数据？车间 / 财务核对 | 成本：結算需要哪些資料？現場 / 財務檢視 |
| ĐIỂM GIAO NHẬN — Làm rõ nguồn dữ liệu, người chịu trách nhiệm và điều kiện xác nhận tại mỗi bước review. | ĐIỂM GIAO NHẬN — Làm rõ nguồn dữ liệu, người chịu trách nhiệm và điều kiện xác nhận tại mỗi bước review. | HANDOFF — Clarify the data source, owner and confirmation condition at each review step. | 交接点 — 明确每个核对步骤的数据来源、责任人与确认条件。 | 交接點 — 釐清每個檢視步驟的資料來源、負責人與確認條件。 |

| Page 5 source component | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| 04 · NHỊP REVIEW | 04 · NHỊP REVIEW | 04 · REVIEW CADENCE | 04 · 核对节奏 | 04 · 檢視節奏 |
| Một nhịp review có thể bắt đầu nhỏ | Một nhịp review có thể bắt đầu nhỏ | A review cadence can start small | 核对可以从小范围开始 | 檢視可以從小範圍開始 |
| Chọn một pain point, xác định dữ liệu cần nối, rồi thống nhất bước tiếp theo phù hợp với hiện trạng. | Chọn một pain point, xác định dữ liệu cần nối, rồi thống nhất bước tiếp theo phù hợp với hiện trạng. | Choose one operating issue, identify records to connect, then agree on a next step that fits current conditions. | 选定一个运营问题，明确需关联的数据，再商定适合现状的下一步。 | 選定一個營運問題，釐清需串聯的資料，再商定符合現況的下一步。 |
| Table headers: Bước / Hành động / Nội dung | Bước / Hành động / Nội dung | Step / Action / Detail | 步骤 / 行动 / 内容 | 步驟 / 行動 / 內容 |
| 01 Chọn câu hỏi — Ví dụ: cần truy vết lot, đối chiếu test data hay làm rõ cost close? | 01 Chọn câu hỏi — Ví dụ: cần truy vết lot, đối chiếu test data hay làm rõ cost close? | 01 Choose a question — For example, trace a lot, review test data or clarify cost close? | 01 选择问题 — 例如追溯批次、核对测试数据，或厘清成本结算？ | 01 選擇問題 — 例如追溯批次、檢視測試資料，或釐清成本結算？ |
| 02 Xác định dữ liệu — Ghi nguồn dữ liệu, ngữ cảnh, người phụ trách và điểm đang thiếu. | 02 Xác định dữ liệu — Ghi nguồn dữ liệu, ngữ cảnh, người phụ trách và điểm đang thiếu. | 02 Identify records — Note the source, context, owner and missing points. | 02 明确数据 — 记录来源、情境、负责人和缺口。 | 02 釐清資料 — 記錄來源、脈絡、負責人和缺口。 |
| 03 Chốt bước tiếp theo — Thống nhất hành động, người chịu trách nhiệm và điều kiện xác nhận. | 03 Chốt bước tiếp theo — Thống nhất hành động, người chịu trách nhiệm và điều kiện xác nhận. | 03 Agree next step — Confirm the action, owner and acceptance condition. | 03 商定下一步 — 明确行动、责任人与确认条件。 | 03 商定下一步 — 確認行動、負責人與確認條件。 |
| Review prompts | Gợi ý đối chiếu | Review prompts | 核对提示 | 檢視提示 |
| Nguồn dữ liệu nào cần được nhìn thấy? | Nguồn dữ liệu nào cần được nhìn thấy? | Which data sources need visibility? | 需要看到哪些数据来源？ | 需要看到哪些資料來源？ |
| Ai nhận cảnh báo hoặc hành động? | Ai nhận cảnh báo hoặc hành động? | Who receives an alert or takes action? | 谁接收提醒或采取行动？ | 誰接收提醒或採取行動？ |
| Điều kiện nào xác nhận bước tiếp theo? | Điều kiện nào xác nhận bước tiếp theo? | What condition confirms the next step? | 什么条件确认下一步？ | 什麼條件確認下一步？ |
| Phần nào vẫn cần xác nhận? | Phần nào vẫn cần xác nhận? | What still needs confirmation? | 哪些部分仍待确认？ | 哪些部分仍待確認？ |

| Page 6 source component | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| 05 · TRAO ĐỔI | 05 · TRAO ĐỔI | 05 · DISCUSSION | 05 · 交流 | 05 · 交流 |
| Trao đổi một bài toán OSAT | Trao đổi một bài toán OSAT | Discuss an OSAT operating question | 交流一个 OSAT 运营问题 | 討論一個 OSAT 營運問題 |
| Bắt đầu từ một pain point cụ thể. Không gửi dữ liệu sản xuất, hồ sơ khách hàng hoặc thông tin nhạy cảm qua trang. | Bắt đầu từ một pain point cụ thể. Không gửi dữ liệu sản xuất, hồ sơ khách hàng hoặc thông tin nhạy cảm qua trang. | Start with a specific operating issue. Do not send production data, customer records or sensitive information through the page. | 从具体运营问题开始。请勿通过页面发送生产数据、客户档案或敏感信息。 | 從具體營運問題開始。請勿透過頁面傳送生產資料、客戶檔案或敏感資訊。 |
| EMAIL / HOTLINE / ĐỊA CHỈ | EMAIL / HOTLINE / ĐỊA CHỈ | EMAIL / HOTLINE / ADDRESS | 电子邮件 / 热线 / 地址 | 電子郵件 / 專線 / 地址 |
| `info_vn@digiwin.com` | `info_vn@digiwin.com` | `info_vn@digiwin.com` | `info_vn@digiwin.com` | `info_vn@digiwin.com` |
| `+84 28 7307 0788` | `+84 28 7307 0788` | `+84 28 7307 0788` | `+84 28 7307 0788` | `+84 28 7307 0788` |
| Tầng 12A, Tòa nhà GOLDEN KING, 15 Nguyễn Lương Bằng, Phường Tân Mỹ, TP.HCM. | Tầng 12A, Tòa nhà GOLDEN KING, 15 Nguyễn Lương Bằng, Phường Tân Mỹ, TP.HCM. | Tầng 12A, Tòa nhà GOLDEN KING, 15 Nguyễn Lương Bằng, Phường Tân Mỹ, TP.HCM. | Tầng 12A, Tòa nhà GOLDEN KING, 15 Nguyễn Lương Bằng, Phường Tân Mỹ, TP.HCM. | Tầng 12A, Tòa nhà GOLDEN KING, 15 Nguyễn Lương Bằng, Phường Tân Mỹ, TP.HCM. |
| Digiwin Vietnam contact: `https://www.digiwin.com.vn/contact-vn/` | Digiwin Vietnam contact: `https://www.digiwin.com.vn/contact-vn/` | Digiwin Vietnam contact: `https://www.digiwin.com.vn/contact-vn/` | Digiwin Vietnam 联系方式：`https://www.digiwin.com.vn/contact-vn/` | Digiwin Vietnam 聯絡方式：`https://www.digiwin.com.vn/contact-vn/` |

## Four proof-carousel cards — metric-free copy candidates

Existing English v1 CAR-01 (`200+`) and CAR-02 (`700+`) metrics were approved for **exact offline v1 copy** only. This register deliberately proposes metric-free variants; those English-only carousel metrics are outside Bảo's approval of claims already present in Vietnamese source. Adding a translated metric requires the source excerpt, count definition, territory/date and a separate decision. CAR-03 remains abstract with no name, logo, result or endorsement. These cards have no CTA or form.

| Card / scope | vi | en | zh-Hans China | zh-Hant Taiwan |
|---|---|---|---|---|
| CAR-01 Taiwan experience, never a Vietnam result | Kinh nghiệm vận hành bán dẫn tại Đài Loan. Từ vật liệu wafer đến đóng gói và kiểm thử. | Semiconductor operating experience in Taiwan. From wafer materials to packaging and test. | 源于台湾的半导体运营经验，涵盖晶圆材料至封装测试。 | 源自台灣的半導體營運經驗，涵蓋晶圓材料至封裝測試。 |
| CAR-02 China solution scope, not local delivery claim | Một mạch vận hành tại thị trường Trung Quốc: từ IC design, wafer đến đóng gói và kiểm thử. | One operating thread in the China market: from IC design and wafer to packaging and test. | 中国市场的运营脉络：从 IC 设计、晶圆到封装测试。 | 中國市場的營運脈絡：從 IC 設計、晶圓到封裝測試。 |
| CAR-03 abstract proof posture | Bằng chứng cần đúng phạm vi. Xem nguồn và mối liên hệ trước khi kết luận. | Proof needs clear scope. Review the source and relationship before drawing conclusions. | 证据需要明确边界。先核对来源与关系，再作判断。 | 證據需要明確範圍。先核對來源與關係，再作判斷。 |
| CAR-04 Vietnam office presence | Digiwin có văn phòng tại Việt Nam: TP.HCM và Bắc Ninh. | Digiwin has offices in Vietnam: Ho Chi Minh City and Bac Ninh. | Digiwin 在越南胡志明市与北宁设有办公室。 | Digiwin 在越南胡志明市與北寧設有辦公室。 |

No team size, Vietnam semiconductor-project outcome, customer visit or regional transfer of capability is asserted. CAR-01/02 territory labels must remain visible in every export. The four-variant candidate copy needs native terminology and scope QA before rendering; management's existing-Vietnamese-claim approval is recorded above and should not be treated as an unresolved rights gate.

### Carousel card-by-card image and support copy

These rows cover every text line in the metric-free English source brief, including the CAR-03 abstract third line and CAR-04 support line. EN/Hans/Hant candidate PNGs have now been rendered from these rows; VI card PNGs remain unrendered. The original English v1 metric artwork remains a separate historical artifact, not the source for a new localized metric claim.

| Card/text role | vi | en | zh-Hans | zh-Hant |
|---|---|---|---|---|
| CAR-01 eyebrow | NĂNG LỰC VẬN HÀNH BÁN DẪN | SEMICONDUCTOR OPERATIONS EXPERTISE | 半导体运营经验 | 半導體營運經驗 |
| CAR-01 body | Kinh nghiệm từ Đài Loan trải từ vật liệu wafer, chế tạo chip đến đóng gói và kiểm thử. | Built in Taiwan across wafer materials, fabrication, packaging and test. | 源自台湾的经验，涵盖晶圆材料、芯片制造、封装与测试。 | 源自台灣的經驗，涵蓋晶圓材料、晶片製造、封裝與測試。 |
| CAR-02 eyebrow | MỘT MẠCH VẬN HÀNH | ONE OPERATING THREAD | 一条运营脉络 | 一條營運脈絡 |
| CAR-02 body | Từ IC design, chế tạo wafer đến đóng gói và kiểm thử tại thị trường Trung Quốc. | In the China market, from IC design to wafer fabrication, packaging and test. | 在中国市场，从 IC 设计、晶圆制造到封装测试。 | 在中國市場，從 IC 設計、晶圓製造到封裝測試。 |
| CAR-03 eyebrow | BẰNG CHỨNG KHÁCH HÀNG BÁN DẪN | SEMICONDUCTOR CUSTOMER PROOF | 半导体客户证据 | 半導體客戶證據 |
| CAR-03 headline | NIỀM TIN DỰA TRÊN PHẠM VI RÕ RÀNG. | TRUST IS BUILT ON CLEAR SCOPE. | 信任建立在清晰的证据边界上。 | 信任建立在清楚的證據範圍上。 |
| CAR-03 support | Mối liên hệ dựa trên bằng chứng, không dựa trên suy đoán. | Evidence-led relationships, not assumptions. | 依据证据确认关系，而非凭推断。 | 依據證據確認關係，而非憑推測。 |
| CAR-04 eyebrow | NĂNG LỰC QUỐC TẾ. HIỆN DIỆN TẠI VIỆT NAM. | GLOBAL CAPABILITY. LOCAL VIETNAM PRESENCE. | 国际能力，越南本地布局。 | 國際能力，越南在地布局。 |
| CAR-04 body | Digiwin có văn phòng tại TP.HCM và Bắc Ninh. | Digiwin offices in Ho Chi Minh City and Bac Ninh. | Digiwin 在胡志明市与北宁设有办公室。 | Digiwin 在胡志明市與北寧設有辦公室。 |
| CAR-04 support | Trao đổi bài toán vận hành sản xuất với Digiwin Vietnam. | Talk through manufacturing operating questions with Digiwin Vietnam. | 与 Digiwin Vietnam 探讨制造运营问题。 | 與 Digiwin Vietnam 討論製造營運問題。 |

## QA and release ledger

| Gate | Evidence required | Current state |
|---|---|---|
| Copy | Each concept/page/card × four variants has text, segment, source/proof ID, reviewer and rights decision; terminology reviewed separately for both Chinese markets | Complete source-node/line copy candidates for three editable SVGs, six document pages and four carousel cards recorded above; native market review and typesetting remain open. B2B derivative PNG text still lacks an editable source. |
| Proof | Existing Vietnamese case/claim approval from Bảo; CAR-01 Taiwan, CAR-02 China, CAR-03 abstract, CAR-04 office scope; no customer mark or new metric | Existing-VI claim use/translation approved by Bảo on 2026-09-29. Scope-preserving translation QA remains; new/broader claims and English-only 200+/700+ metric translation are separate decisions. |
| Visual | Render square/b2b derivatives, six PDF pages and four cards per variant; inspect script glyphs, clipping, hierarchy, contrast, safe margins, alt text and mobile view | Stage A square SVG/PNG and six-page PDFs rendered and locally inspected. Stage B VI/Hans/Hant b2b-v2 and EN/Hans/Hant carousel raster candidates rendered and visually inspected at 1254². VI carousel images, native/mobile/account placement review remain open. |
| Platform | Confirm active placement, character/format/size, Page/object rights and preview | Unknown; no account action in this slice. |
| Landing | Ad variant uses the same OSAT/Fabless/Supplier URL with non-PII `lang=vi|en|zh-Hans|zh-Hant` as appropriate; existing UTM/gclid survive; top switch overrides initial locale | Bảo approved the parameter design, but route runtime, URL encoding, fallback, user-choice persistence and end-to-end behavior still require implementation and QA. |

**Stop:** do not upload, attach, publish or spend; do not promote provisional S1 segments into verified target accounts. A missing source for a new claim, market review, unrendered derivative, platform specification or destination mapping leaves the affected asset unready. **Terminal:** four-variant source copy ledger is drafted for three editable static concepts, six document pages and four abstract carousel cards. Stage A square SVG/PNG and six-page PDFs and Stage B b2b-v2/carousel raster candidates are offline renders; VI carousel cards remain copy-only. No localized creative is production-ready. Bảo's approval of existing Vietnamese case/claim translation is recorded and is not counted as a pending claim-rights blocker.

## Stage A render and QA record — 2026-09-29

| Family | New local-only files per locale `en`, `zh-Hans`, `zh-Hant` | Bounded inspection |
|---|---|---|
| OSAT square | `source/osat-square-{locale}.svg`, `final/osat-square-{locale}.png` | 13 title/desc/text nodes mapped to register; 1200×1200 PNG; English, simplified and traditional glyphs, Digiwin logo, diagram, line wrap and safe margins inspected. |
| Fabless square | `source/fabless-square-{locale}.svg`, `final/fabless-square-{locale}.png` | 12 nodes mapped; 1200×1200; all three inspected for heading, three-box diagram, logo and clipping. |
| Supplier/Partner square | `source/partner-square-{locale}.svg`, `final/partner-square-{locale}.png` | 14 nodes mapped; 1200×1200; all three inspected for ERP–MES–OT diagram, heading, logo and clipping. |
| OSAT document | `output/pdf/digiwin-osat-document-ad-6p-{locale}.pdf` | Each opens as six A4 pages. All 18 pages rendered to temporary QA PNGs and visually scanned. Every display-copy ledger row was found in extracted text; page-5 `Table headers` is a structural ledger label, absent from the original card layout and intentionally not displayed. Page 6 email, phone, Vietnamese street address and contact URL match the source exactly. Light-background pages 2 and 5 were corrected for readable contrast. |

The first PDF font pass was rejected during visual QA because its CJK font spaced Latin characters and lost Vietnamese address accents. A subsequent HTML-print pass was rejected because it degraded the source artwork. The delivered PDFs use text-only replacement over the original vector PDF, preserving the logo, diagrams, card geometry and decorative art; Unicode shaping preserves the exact address. Original VI SVG/PNG/PDF and existing English offline-v1 carousel PNGs were not overwritten. These checks establish local render/source coverage, not native translation approval, LinkedIn placement acceptance, audience readiness or live destination behavior.
