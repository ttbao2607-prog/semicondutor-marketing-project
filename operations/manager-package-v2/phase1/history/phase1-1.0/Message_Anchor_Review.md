# MSG-ANCHOR-01 — Package v2 Phase 1

Stage: **INTERNAL_CONTENT_REVIEW**. Artifact revision: **package-v2-phase1-1.0**, 07/10/2026. Writer/reviewer: current `/root`, **SELF_REVIEW**, không độc lập, không PO acceptance. Các exact hashes đã đọc của anchor/email/skeleton và message-bearing registers/notices nằm trong [message-bindings.json](message-bindings.json), không dùng hash receipt tự trỏ chính nó.

Anchor: `operations/Vy_Email_Content_Anchor.md`, **VY-CONTENT-ANCHOR / 1.0**, source pin SRC-ANCHOR. Email: `operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md`, **VY-MAIL-USER-20261006**, SRC-MAIL. Workflow: PACKAGE-V2-WORKFLOW /1.0, SRC-WORKFLOW. Đã đọc source và phân loại content anchors với operational/historical proposals trước dựng skeleton.

Scope: Markdown skeleton S1–S10, Data/Claim/Inventory/Reconciliation registers và bounded current-state/progress notices. Language: tiếng Việt cho Bảo review nội bộ; mô tả riêng VN_DOMESTIC vi-VN và FDI en/zh-Hans/zh-Hant. Audience trong skeleton là content scenario/decision unit, không observed buyer qualification. File/hash checks của 233 selected PNG và 10 reader revisions chỉ phục vụ input inventory; không fresh native/postgen certification của chúng. Không có ảnh, HTML UI hoặc generation mới nên native/desktop/mobile render cho artifact Phase1 là **N/A — internal Markdown**. Chưa đóng actual final portable journey hoặc customer-facing copy v2.

## Rule review trên nội dung thực

| Rule | Exact passage / vị trí đọc | Match / scope | Action |
|---|---|---|---|
| A1 | S2: “Ưu tiên hoạt động PCB, substrate, linh kiện, vật liệu đóng gói, gia công chính xác cho thiết bị.”; D03 và C07 | MATCH: hoạt động trong chuỗi; không mở thành mọi manufacturer hoặc mặc định route name là ICP. | Giữ entity/fit pending ở S3/S7. |
| A2 | S2: “từng công ty vẫn cần xác định đúng hoạt động và đơn vị có ảnh hưởng/quyền quyết định hệ thống”; D39 | MATCH: tách decision unit/customer fit với tên doanh nghiệp hoặc Page match. ERP chung của tập đoàn là yếu tố xem xét, không blacklist/fact từng account. | Bảo xử lý account qualification ở vận hành. |
| A3 | S2 có 4 hàng riêng VN, OSAT, Fabless, Supplier; S3: “Bốn bản creative không tạo ra bốn audience độc lập.” | MATCH: segment/persona/locale độc lập; không quốc tịch hoặc ngôn ngữ = FDI/buyer authority. | Không chuyển targeted-locales thành 4 campaign pools. |
| A4 | S2: “ROI ở đây có thể là nuance về thời gian, chi phí đối soát, hiệu quả hoặc rủi ro”; FDI S4 giữ mechanism/value; C02 outcome15→5 ngày có attribution | MATCH cho FDI descriptions; không yêu cầu chữ ROI mỗi card, không ROI%/payback/guaranteed savings. A4 N/A đối với riêng thông điệp VN readiness vì A5 chi phối. | Numeric ROI không được thêm ở polish. |
| A5 | S2 VN: “ERP hỗ trợ năng lực quản trị; thông điệp tránh hứa đạt chuẩn hoặc có đơn hàng nhờ mua ERP”; S4/C03 giữ case minh họa | MATCH cho VN; FDI rows dùng operating trigger, A5 N/A cho các FDI descriptions vì branch không mặc định gia nhập chuỗi. | Giữ readiness nuance khi chọn VN demo. |
| A6 | S2/S4: hồ sơ/trách nhiệm/lot/change/hand-off; C01 phân lớp ERP+iMES/SPC/ECN; C04 integrated scope; S4 “Không gộp mọi capability ERP, MES và equipment integration thành ERP-only.” | MATCH: menu chiều sâu hợp persona, không buộc yield/recipe/audit vào mọi nội dung, không claim ERP thay MES/test equipment. | Các new capability statements cần nguồn tương ứng. |
| A7 | S4: cold→cohort→explanation/case/reader và “Người dùng thực tế có thể gặp nội dung theo thứ tự khác”; Claim Register binding từng nhóm | MATCH cho internal journey specification. Không gọi là toàn rendered campaign PASS. O3 bridge Operations→Finance và Partner supplier→WaferWorks context được nói rõ. | Final chosen journey revision phải recheck entry/locale/return thực ở bước bàn giao. |

## Quan sát từng unit/surface và transition

| Unit | Nội dung đã đọc / evidence thực | Disposition |
|---|---|---|
| S1 proposal/investment | “doanh nghiệp phù hợp trong chuỗi cung ứng bán dẫn và điện tử”; target/attention/progression, lead verified bổ sung;5,6/6,1 trong11,7m | A1/A4/A5 phù hợp brief; budget là current PO/source, không email schedule. |
| S2 VN row | Trigger “Yêu cầu hồ sơ, quy trình, dữ liệu và trách nhiệm khi chuẩn bị tham gia chuỗi” | A3/A5 MATCH; không factory-already-in-sector hook dịch sang VN. |
| S2 OSAT row | Plant Operations/Quality, O3 bridge records→Finance; time/reconciliation/risk | A1/A3/A4 MATCH; Finance không thay Operations entry persona. |
| S2 Fabless row | Hoạt động sản phẩm/đối tác sản xuất, lot/forecast/partner handoff | A1/A3/A4 MATCH; integrated proof giữ entity thiết kế chip. |
| S2 Supplier row | “nhà cung ứng công nghiệp như gia công linh kiện chính xác cho thiết bị bán dẫn” | A1/A3/A4 MATCH; không SI/channel-partner persona historical. |
| S2 customer-fit paragraph | Group ERP được xem xét, không bắt buộc loại từng công ty; role/entity còn cần evidence | A2 MATCH; scenario không là observed buyer fact. |
| S3 original424 row | Research101/323, submitonce, Updating06/10, mapping/reachpending | A2/A3 scope preserved; không clean-all/reachforecast/customer-fit claim. |
| S3 backup52 row | Ready/>90%/444274 vsDetails0;460/<300unsaved, separatefrom424 | A2/A3 preserved; summarypool khôngqualifiedbuyers/4localepools. |
| S4 cold→RMK description | Cohort từchínhadsSingleimagemới, từngsurfacecócontext; khôngguaranteedsequence | A7 MATCH ởspecification, actualplatformdelivery chưaobserved. |
| S4 VN selection | Mainweek1/week2;AplusChinaiMES+TOPGP minh họamechanism,khôngVNvàochuỗi | A3/A5/A6/A7 MATCH;15→5daysFDI khônggánVN. |
| S4 OSAT selections/O3 | B1–B12/batchsubset vs3pilotsriêng;Ops/Quality/Operations→Finance phânbiệt | A3/A4/A7 MATCH;C01/C02phạmvi giữ. |
| S4 Fabless candidates | Each11sourcePNG, renderpending, qualitativeBrightPower;source-only status | A1/A3/A4/A7 MATCH; khôngadoptfailedhistory hoặcmetricbaselineHOLD. |
| S4 Partner candidates |30selected/sourcecheckpoint;WaferWorksTaiwan/Shanghai;VNteamseparate | A1/A3/A4/A6/A7 MATCH;scenarioprecisioncomponentskhônggọiWaferWorks làcùngfactory. |
| S4 FDI redesign readers |10sourcefour-toggle;mainrevisionseparate,chooseversion | A3/A7 MATCH;languagefeaturekhôngtrởthànhlocalemarketacceptance. |
| S4 numeric-proof paragraph | “3 tháng … go-live toàn dự án tích hợp”;15→5ngàyreportedcase;BrightPowerbaselinesmâu thuẫnheld | A4/A5/A6 MATCH;attribution vàlimitations ởC02–C04. |
| S5 budget surface |11,7media;5,6+5,6+0,5;6,1insidecap;all-inpending | Emailbudget/timetable làhistorical,separatecontentanchor;khônglấy35m/43,75m/daily600k250kactive. |
| S6 target/delivery metric rows |Đúngtarget/role,uniquereach/frequency,campaignscope,coverage | A2/A3 scopeprotected;engagementkhôngcomprehension/brandlift/buyerproof. |
| S6 progression/cost rows |Paidengagedsessions/sectiondefinition,mediaremain;actualsample/eligibility | A4/A7 preserved; khôngCTA=lead hoặcgiải ngân mặcđịnh. |
| S6 Search/commercial rows |Searchtermscoverage,notdemandzero;verifiedlead/bookingcountsseparate | Principles mail cònphùhợp;oldthresholds khôngautoapproval. |
| S7 audience/cohort execution |Readback,sourceIDs/rule/Ready/filter trướcRMKrelease;nooldPagepool | A2/A3/A7 consistent;actualRMKwholejourney notcertified. |
| S7 creative/destination/proof |Selectedrevisions,source/main distinction,rights vàclaimedlayerroles | A6/A7 consistent;offline/technical/PO/live scopesđúngnguồn. |
| S7 production metadata |Frozenharness/anchor vsadapterdeveloping,hash/self-review khôngxinbossduyệt | WorkflowMATCH;chỉinternalstatus. |
| S8 planned investment topics |3–4nội dung đầu tư ởPhase2;khônglọcfinalquestionsởPhase1 | WorkflowMATCH; khôngcarry22questions/answers. |
| S9 topology/folder |Report/demo/library/workbookrelationships,formatslater,folderregular | N/A detailedA1–A6 vìtopology;A7spec giữdependency/return;khôngnewpublishedartifact. |
| S10 data lock |OPEN-01–04internal,BảosteersbeforePhase2 | WorkflowMATCH;pending khôngpoapprovalclaim. |
| Data register40rows |Sameunits/dates/decisionvassumption/fact/pending;oldmetricsnotcurrent;existingproofscope | Phânloạingồn/anchorMATCH;pendingaccountdatakhôngviếtthànhmarketingfact. |
| Claim registerC01–C08/bindingtable |Entity/geography/solution/metric/unit/approval/rights;OpsFinance/localoverseasbridge | A1–A7 reviewed theo từngcase;khôngbroadernewclaim/markrightinfer. |
| Inventory34rows |Covered/hold/reference/dropdefaultgắnsource/section,không34bossquestions | Internaldisposition khônglaunch/acceptance hoặcrolechange. |
| Reconciliation notes/currentnotices |Ownerrecords stale vsactualGit;sourceadvancements chưa-main/POaccepted | N/A newcustomermessage;A2/A3/A7 scopebounded,nohindsightPASS. |

Transition review: VN readiness→data/process→Aplus→read-case giữ cùng branch và role; OSAT Operations/Quality→lot/change→integratedChina proof giữ case scope; O3 records→Finance handoff→month-close case có bridge; Fabless partner updates→qualitativeBrightPower context→reader giữ chip-design; Supplier responsibility→operating records→WaferWorks context→factory discussion giữ industrial buyer và tách Digiwin Vietnam capability. Đây là nội dung/spec đã đọc, không fresh review của ảnh/reader cũ hoặc final exports.

MSG-ANCHOR-01 verdict: **MESSAGE_ANCHOR_PASS** cho internal Markdown audience/message/classification nói trên. Content record: **INTERNAL_DRAFT_REVIEWED / BAO_DATA_LOCK_PENDING**. Không có content-anchor mismatch được xác nhận trong skeleton. Open inputs/revision choice/rights và full rendered/live gates vẫn đúng trạng thái ở registers; PASS này không tự cấp generation, artifact acceptance, native-market/independent certification hoặc Phase2 activation. Lượt này không có POSTGEN_ARTWORK hoặc SCRIPT_REVIEW_PASS để mang sang batch.

Nếu anchor, source, persona, proof, locale hoặc skeleton thay revision, tạo fresh binding/review affected scope. Historical receipts không bị sửa. Read source→dựng skeleton→đọc actual Markdown→ghi receipt; không nhận acceptance hồi tố cho artifacts khác.
