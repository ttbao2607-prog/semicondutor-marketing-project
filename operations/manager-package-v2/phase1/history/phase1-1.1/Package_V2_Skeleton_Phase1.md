# Phương án LinkedIn và Search bán dẫn — skeleton Phase 1

Ngày 07/10/2026. Bản làm việc để Bảo chốt dữ liệu và cấu trúc nội dung. Trần media hiện hành: **11,7 triệu đồng, chưa thuế**. Revision Phase 1: **1.1**, cập nhật theo chỉ đạo Bảo về ngân sách dashboard và review tuần. Bảo phụ trách paid ads và quyết định toàn pipeline. Hồ sơ nguồn và trạng thái chi tiết nằm trong [Data register](Data_Register.md), [Claim register](Claim_Register.md) và [đối soát](Reconciliation_Notes.md).

## S1. Mục đích của khoản đầu tư

Đề xuất dùng paid ads để tiếp cận doanh nghiệp phù hợp trong chuỗi cung ứng bán dẫn và điện tử, giúp người phụ trách vận hành nhận ra bài toán quản trị liên quan và tìm hiểu cách Digiwin giải quyết. Kết quả cần đọc theo mức tiếp cận đúng tệp, sự quan tâm đến nội dung và khả năng đi tiếp đến phần giải thích/case. Lead đã xác minh là tín hiệu bổ sung khi có dữ liệu.

Khung hiện hành là 11,7 triệu đồng media, chưa thuế. Cấu trúc tham chiếu dành 5,6 triệu cho đợt đầu; giữ 6,1 triệu để quyết định đợt tiếp theo và thử Search khi có căn cứ. Bảo theo dõi số tiền ads trên dashboard, kế toán xử lý thuế và thanh toán theo pipeline của công ty. Tuần đầu chạy đúng plan; cuối tuần review dữ liệu để Bảo chọn hướng tuần 2. Package v2 sẽ trình khoản đầu tư, lý do dùng tiền và cách đánh giá để sếp đồng ý, từ chối hoặc góp ý. Phase 1 giữ các đầu vào vận hành cho Bảo chốt; Phase 2 lọc còn khoảng 3–4 nội dung hỏi sếp.

Data: D01, D02, D08–D16, D34, D40.

## S2. Người đọc và thông điệp

| Segment | Persona cần mô tả trong nội dung | Trigger và giá trị | Ngôn ngữ |
|---|---|---|---|
| VN nội địa | Người phụ trách quản trị/vận hành của doanh nghiệp phù hợp chuỗi đang chuẩn bị nâng năng lực đáp ứng khách hàng | Yêu cầu hồ sơ, quy trình, dữ liệu và trách nhiệm khi chuẩn bị tham gia chuỗi. ERP hỗ trợ năng lực quản trị; thông điệp tránh hứa đạt chuẩn hoặc có đơn hàng nhờ mua ERP. | Tiếng Việt, xưng hô và nuance theo bản VN đã duyệt |
| FDI OSAT | Plant Operations/Quality; O3 có cầu nối hồ sơ vận hành sang Finance | Truy xuất lô, phối hợp bàn giao, dữ liệu chất lượng và độ tin cậy của quyết định. Giá trị ở thời gian, giảm đối soát, trách nhiệm và kiểm soát rủi ro theo đúng nguồn. | English quốc tế, giản thể, phồn thể; từng persona/locale review riêng |
| FDI Fabless | Người quản lý hoạt động sản phẩm/đối tác sản xuất của doanh nghiệp thiết kế chip phù hợp | Tiến độ sản phẩm, lô, forecast và bàn giao đối tác; ERP nối dữ liệu phục vụ kế hoạch và quyết định. Case thiết kế chip được giữ đúng phạm vi. | English, giản thể, phồn thể |
| FDI Supplier/Partner | Operations Manager của nhà cung ứng công nghiệp như gia công linh kiện chính xác cho thiết bị bán dẫn | Trách nhiệm cập nhật, hồ sơ nguồn, vật tư và tiến độ thực thi phục vụ quyết định nhà máy. Partner ở đây là nhà cung ứng công nghiệp. | English, giản thể, phồn thể |

Ưu tiên hoạt động PCB, substrate, linh kiện, vật liệu đóng gói, gia công chính xác cho thiết bị. Tên route OSAT/Fabless/Supplier phục vụ tổ chức nội dung; từng công ty vẫn cần xác định đúng hoạt động và đơn vị có ảnh hưởng/quyền quyết định hệ thống. Nhận định về ERP chung của tập đoàn là yếu tố xem xét customer fit, không phải kết luận hoặc blacklist cho từng công ty.

Nội dung FDI có thể mở bằng một tình huống vận hành cụ thể và làm rõ giá trị kinh doanh ở phần giải thích/case. ROI ở đây có thể là nuance về thời gian, chi phí đối soát, hiệu quả hoặc rủi ro; dữ liệu hiện có chưa hỗ trợ ROI tài chính hoặc lời hứa tiết kiệm chung.

Data: D03–D07, D39. Claim: C01–C07.

## S3. Tệp tiếp cận và công việc còn lại

| Luồng | Đã làm | Evidence cuối | Bước vận hành tiếp theo của Bảo |
|---|---|---|---|
| Danh sách công ty cung cấp ban đầu | Nghiên cứu đủ 424 dòng; 101 dòng có định danh hỗ trợ, 323 đã điều tra nhưng còn blocked. Giữ nguyên danh sách và submit sửa existing Discovery một lần. | Updating ngày 06/10; chưa có mapping/reach sau xử lý. | Đọc lại existing Discovery, kiểm mapping rồi đo filtered reach; ưu tiên hai mapping sai đã quan sát trước update. |
| Contingency backup riêng | Rà 203 dòng, R5 giữ 52 Pages có căn cứ và upload một lần. | 07/10: Ready/>90%/444.274 members; Details hiển thị 0 dòng. Estimate unsaved sau địa lý/functions/seniority là 460 với English, Vietnamese <300. | Recheck Details theo handoff; khi có đủ mapping, Bảo quyết định backup có phù hợp cho lượt chạy không. |

Hai luồng được theo dõi riêng. Công việc làm sạch đã kết thúc trong phạm vi nghiên cứu; bước còn lại là kiểm kết quả xử lý của nền tảng. Các estimate 460/<300 phục vụ nhận diện quy mô cấu hình tại thời điểm quan sát, không dùng làm số người sẽ được tiếp cận hoặc qualified buyers. Bốn bản creative không tạo ra bốn audience độc lập.

Bảo chọn nhóm chạy đầu và cấu hình theo kết quả mapping/reach, persona và khả năng dùng nội dung phù hợp. Đây là quyết định execution trong quyền Bảo; bảng này giữ đầy đủ đầu vào cho bước chốt data.

Data: D17–D24, D39.

## S4. Nội dung và hành trình đã có

Luồng đã chọn: **Single image cold → cohort từ chính ads mới → Carousel RMK**. Cold nêu trigger; lớp giải thích nói rõ dữ liệu/cơ chế và giá trị; case cung cấp căn cứ có attribution; reader giúp người quan tâm hiểu bài toán và bước tiếp theo. Người dùng thực tế có thể gặp nội dung theo thứ tự khác, nên từng surface cần đủ context.

| Nhóm | Bộ chọn hiện tại | Phạm vi dùng cho package |
|---|---|---|
| VN nội địa | Week1v3 và week2-time-v2, mỗi journey 10 ảnh; hai reader Aplus có vi/en/zh-Hans. | Đã duyệt offline và có trên main. Aplus Trung Quốc/iMES + TOP GP minh họa cơ chế quản trị; không chứng minh doanh nghiệp VN đã vào chuỗi. |
| OSAT FDI | B1–B12: 120 ảnh chọn theo journey; B6–B12 riêng 70 ảnh. Ba O3 pilot/candidates có 30 ảnh chọn riêng. | Đã duyệt offline và có trên main. Giữ Operations/Quality hoặc cầu nối Operations→Finance theo từng treatment. Hạn chế technical/render của receipt giữ phạm vi riêng. |
| Fabless FDI | B13 EN v5, B14 giản thể v1, B15 phồn thể v2: mỗi bộ 11 ảnh chọn. | B13 checkpoint local; B14/B15 checkpoint local461a752, còn riêng với main. Corrective native và hậu kiểm feed/main/desktop reader đã ghi nhận; full mobile và whole-journey acceptance còn pending. Dùng làm inventory, chưa chọn vào final library. |
| Supplier/Partner FDI | B22–B24: 30 ảnh chọn, root review trong phạm vi đã ghi; checkpoint local 4a17968. | Source-only, chờ PO asset acceptance/main adoption. Proof Wafer Works giữ Taiwan/Shanghai và solution scope; năng lực đội Việt Nam là phần riêng. |
| FDI reader redesign | 10 HTML cụ thể, mỗi file 4 toggle vi/en/zh-Hans/zh-Hant; mapping B1–B7 và 3O3. | PO offline checkpoint tại source, chưa main. Package phải chọn revision reader trước khi đóng gói; source redesigned reader không được gọi là current main. |

Fabless B16–B21, Partner B25–B30 và các reader conditional là phần sản xuất/intake còn lại theo scope lane. Số lượng ảnh trên đây là số bản chọn theo bộ; ảnh reuse không làm tăng số ảnh độc nhất. Các original/fail/corrective attempts chỉ lưu ở hồ sơ sản xuất. VN week 1/week 2 và thư viện FDI là nguồn thay/ghép linh hoạt sau review: đoạn nào yếu thì chọn asset phù hợp thay đoạn đó, giữ phần đang hiệu quả. Mỗi tổ hợp giữ cùng persona, locale và thông điệp; kiểm lại đoạn chuyển tiếp bị ảnh hưởng.

Demo/library v2 sẽ gắn đúng cold, explanation, proof và reader của từng persona/locale; giữ đường quay lại đúng journey. Template hoặc ảnh đẹp không thay sự phù hợp của proof. Số 3 tháng của Aplus là go-live toàn dự án tích hợp; 15→5 ngày của case OSAT là kết sổ của case tích hợp ERP+iMES. Cả hai không là SLA hoặc ROI tài chính của proposal mới. Bright Power dùng qualitative scope; các baseline order-response mâu thuẫn chưa dùng. Không gộp mọi capability ERP, MES và equipment integration thành ERP-only.

Data: D05–D07, D25–D30, D32. Claim: C01–C07.

## S5. Khung ngân sách và logic sử dụng

| Khoản | Tham chiếu media | Logic |
|---|---:|---|
| Đợt LinkedIn đầu | 5.600.000 đồng | Tiếp cận một nhóm phù hợp với ít mẫu đại diện để quan sát phân phối, relevance và mức quan tâm. 400.000/ngày × 14 ngày là tham chiếu lập kế hoạch. |
| Một đợt tiếp theo | Tối đa 5.600.000 đồng | Bảo điều chỉnh theo evidence đợt đầu; có thể dùng awareness/RMK khi cohort đủ điều kiện. |
| Search tùy chọn | Tối đa 500.000 đồng | Thử demand/query relevance trong phạm vi nhỏ. Volume không hấp thụ được thì giữ phần dư, không mở rộng keyword chỉ để tiêu tiền. |
| Tổng trần media, chưa thuế | **11.700.000 đồng** | 5,6 + 5,6 + 0,5 triệu. |
| Phần giữ lại trong tổng | **6.100.000 đồng** | Đợt tiếp và Search; không cộng thêm vào tổng hoặc coi đã giải ngân. |

Bảo chọn daily, lịch và pacing trong trần hiện hành theo mapping và dữ liệu của cấu hình chạy. Package ghi ngân sách **chưa thuế**; Bảo quản lý và phối hợp xử lý số tiền trên dashboard, kế toán tính thuế và thanh toán qua pipeline riêng của công ty. Tuần 1 chạy theo plan, review cuối tuần; tuần 2 điều chỉnh theo data matrix trong tổng ngân sách 11,7 triệu. Các mốc 35 triệu, 43,75 triệu hoặc daily 600k/250k trong mail/lịch sử đã được thay thế.

Data: D08–D16, D33, D36. Calc: CALC-01–CALC-04.

## S6. Measurement và cách đánh giá khoản đầu tư

| Câu cần trả lời bằng dữ liệu | Chỉ số / nguồn | Cách dùng |
|---|---|---|
| Quảng cáo đến đúng doanh nghiệp/người phụ trách không? | Native company/function/seniority breakdown và fixed target universe khi nền tảng cho xem; source/rule/filter rõ ràng. | Kiểm relevance trước khi đọc engagement như tín hiệu thị trường. Dữ liệu bị ẩn hoặc thiếu mapping được ghi coverage. |
| Nhóm mục tiêu có cơ hội thấy và chú ý đến nội dung không? | Native reach, impressions, frequency, loại engagement/clicks, CTR; cùng campaign/segment/locale/kỳ. | Đọc cùng phân phối và mức lặp; unique reach theo kỳ, không cộng ngày/kênh. Không gọi engagement là hiểu thông điệp hoặc brand lift. |
| Người quan tâm có đi tiếp vào phần giải thích/case không? | Paid/engaged sessions, section view/engagement đã có scope; proof interaction chỉ dùng khi có nguồn/event định nghĩa rõ. | Đối soát route/UTM/locale và loại test traffic. Reader mới cần mapping measurement tương ứng. |
| Tiền dùng thế nào, có nên dùng tiếp phần giữ lại không? | Actual media, remaining cap, CPM/CPC đúng denominator; relevance, attention và cohort eligibility cùng kỳ. | Bảo đưa recommendation theo dữ liệu, giữ phần dư khi bằng chứng chưa đủ hoặc reach/frequency mất hiệu quả. |
| Search có nhu cầu thương mại phù hợp không? | Search terms đúng chủ đề, số clicks đã phân loại/coverage, impression share lõi nếu có, engaged LDP sessions. | Không suy metrics Planner trống là demand bằng 0; không dùng 7/10 clicks hay 70% như ngưỡng đạt đã chốt. |
| Có tín hiệu thương mại nào được xác minh? | Lead thô, receiver-accepted/verified leads, booking ghi riêng; baseline brand search/direct traffic/follower đúng target nếu có nguồn. | Tín hiệu bổ sung, không lấy số form thô làm kết quả chính hoặc gọi CTA click là lead. |

Existing landing/tracking đã có kiểm tra production trong scope ghi nhận. Campaign delivery, attribution và reader mới được kiểm trong scope triển khai kế tiếp. Bảo xác định baseline, metric và điều kiện điều chỉnh trên dữ liệu phù hợp. Cadence đã chốt: **tuần 1 chạy đúng plan → review cuối tuần → tuần 2 Bảo quyết định theo data matrix**. Matrix đọc độ tin cậy đo, đúng tệp, delivery/attention, đoạn explanation/proof/reader và số tiền dashboard. Nếu phát hiện vấn đề, sửa/swap đúng đoạn; audience có tệp chính và backup với evidence riêng. Mẫu mỏng được ghi rõ trước kết luận. [Matrix nội bộ](Week1_Review_Week2_Data_Matrix.md) cụ thể hóa cách đọc dữ liệu và chọn hành động.

Workbook v2 dự kiến lưu plan/actual/remaining, kết quả theo kênh, danh sách keyword/negative, target account/audience và định nghĩa KPI. Dữ liệu gốc được giữ riêng với kết quả phân tích. Công thức chi phí/tỷ lệ có đơn vị và cùng kỳ; input thiếu giữ thiếu thay vì hiện 0. V1 workbook là một nguồn học về cách nối budget và actuals, không là template bắt buộc giữ 6 sheet/29 formulas.

Data: D16, D20, D23, D31, D33–D37.

## S7. Hồ sơ vận hành để Bảo triển khai

| Việc | Trạng thái và dependency | Người quyết định/thực hiện |
|---|---|---|
| Audience | Research đã xong; mapping/readback gốc và backup còn phạm vi riêng. | Bảo/operator theo account evidence |
| Nhóm chạy, locale, targeting, lịch/pacing | Bảo chọn trong cap sau khi có mapping/reach và content fit. | Bảo |
| Cohort RMK | Pin source IDs từ chính ads Single image mới; rule/lookback/Ready/filtered eligibility trước release. Cold có thể bắt đầu khi đủ cold readiness, không cần warm pool cũ. | Bảo/operator |
| Creative/library | Dùng selected revision đã duyệt; Fabless/Partner giữ review/acceptance riêng. | Bảo + lane owner |
| Destination | Chọn main reader hoặc source redesign đã duyệt offline; adoption, entry/locale/return, tracking/handoff phải cùng revision. | Bảo + destination owner |
| Capability/proof/quyền ảnh | Giữ exact existing approval; đối chiếu claim mới và quyền ảnh riêng, không mở rộng attribution. | Bảo/source owner |
| KPI/actuals | Chốt definition, baseline, nguồn và review/stop conditions trước chạy; đọc actuals đúng kỳ. | Bảo |

Harness/anchor tiền–hậu kiểm và process giữ freeze; adapter locale đang developing. Đây là metadata sản xuất phục vụ hồ sơ nội bộ. Không đưa runtime, hash, self-review hoặc quyền thao tác agent thành lời xin sếp duyệt.

Data: D02, D07, D19, D24, D27–D32, D35, D36, D39.

## S8. Chủ đề sẽ rút thành phần hỏi sếp ở Phase 2

Giữ toàn bộ dữ liệu gốc ở Phase 1. Phase 2 sẽ dùng bản Bảo chốt để soạn khoảng 3–4 nội dung về khoản đầu tư: mức media chưa thuế; logic chi theo đợt/phần giữ lại và review tuần 1→tuần 2; cách đánh giá trước khi dùng tiếp tiền; góp ý về mức đầu tư hoặc hướng thử nghiệm. Mỗi nội dung có phương án Bảo đề xuất và căn cứ ngắn.

Các lựa chọn audience/locale/creative/targeting/rule/tag/technical và công việc agent thuộc hồ sơ Bảo. Bộ 22 câu và câu trả lời v1 chưa được tái sử dụng. Lượt này chưa thực hiện content split hoặc dựng bộ câu hỏi cuối.

Data: D01, D08–D16, D36, D38, D40.

## S9. Những nội dung package sẽ chứa

Package cần có phần phương án và ngân sách; phần measurement/cách review; demo/thư viện chọn theo segment/persona/locale và reader; workbook theo dõi khi format được chốt. Căn cứ/evidence vận hành nằm ở hồ sơ nội bộ và chỉ đưa business rationale cần thiết vào phần trình sếp sau Phase 2.

V1 có 3 report, demo/library và workbook nối nhau; v2 học mối liên hệ này để người xem hiểu tiền phục vụ luồng nào và đánh giá bằng gì. Sitemap, số report/tab, engine câu hỏi, bản export hoặc layout final vẫn để quyết định khi nội dung đã chốt. Delivery bằng thư mục thường.

Data: D37, D38, D40. Inventory: V2-27–V2-34.

## S10. Điểm chốt nội bộ trước Phase 2

Phase 1 đã dựng data register và skeleton theo nguồn hiện hành. Bảo đã chốt [budget/dashboard và nhịp review](PO_Dashboard_Weekly_Decision_2026-10-07.md): ngân sách chưa thuế, kế toán xử lý thuế, tuần 1 chạy đúng plan, review cuối tuần và tuần 2 theo data matrix. Phần ghép/swap VN/FDI và audience chính/backup nằm trong quyền Bảo. [Reconciliation Notes](Reconciliation_Notes.md) giữ reader revision, metric/ngưỡng và account readback như đầu vào execution nội bộ. Những thay đổi định hướng tiếp theo sẽ được cập nhật vào data trước khi tách phần hỏi sếp.

Trạng thái: **PHASE1_PREPARED / BAO_DATA_LOCK_PENDING**. Đây là skeleton nội bộ; Phase 2–3 chưa bắt đầu.

Data: D01, D15, D16, D30, D35, D39, D40.
