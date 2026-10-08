# Package v2 — Phase 1

Trạng thái: **PHASE1_PREPARED / BAO_DATA_LOCK_PENDING**. Đã chuẩn hóa nguồn và dựng skeleton nội bộ theo mandate Bảo ngày 07/10. Plan checkpoint local `7796bc6`; các output Phase 1 là working files local, chưa commit mới, chưa vào main/GitHub. Phase 2–3 chưa bắt đầu.

Mở [Skeleton Phase 1](Package_V2_Skeleton_Phase1.md) để review phương án. Đối chiếu [Data register](Data_Register.md), [Claim register](Claim_Register.md), [34 disposition](Inventory_Disposition.md) và [Reconciliation Notes](Reconciliation_Notes.md) khi cần xem căn cứ/điểm chưa chốt. OPEN-01 thuế đã đóng, OPEN-02 cadence/quyền tuần2 đã chốt theo [quyết định Bảo](PO_Dashboard_Weekly_Decision_2026-10-07.md). [Data matrix tuần2](Week1_Review_Week2_Data_Matrix.md) giữ action logic nội bộ; reader/metric/readback cụ thể là execution inputs, không loạt câu hỏi gửi sếp.

Evidence: [source pins](source-register.json), [selected assets](asset-register.json), [reader revisions](reader-register.json), [workbook v1 inspection](legacy-workbook-inspection.json), [message anchor review 1.2](Message_Anchor_Review_1.2.md), [bounded audit](verification.json). Source/file pins tại capture ghi trong audit cuối; 25 selection groups/253 PNG placements và 10 redesigned reader revisions được kiểm file/hash. Reuse làm một ảnh có thể xuất hiện nhiều lần; con số 253 không là số ảnh độc nhất, số accepted assets hoặc số calls. Audit cuối ghi số pins thực tế. [Receipt và data revision 1.0](history/phase1-1.0/Message_Anchor_Review.md) giữ riêng để đối soát lịch sử.

Không copy ảnh/HTML/XLSX v1 vào namespace v2 hoặc tạo ZIP. Skeleton là Markdown nội bộ, không có UI/artwork mới nên không cần browser/render. Selected image hash checks không phải fresh visual review hoặc quyền paid. Root tự đối chiếu; không independent/PO acceptance.

Capture/verify scripts chỉ phục vụ bước này, không scheduler/framework. `.gitattributes` giữ byte LF cho hồ sơ pin/receipt trong phase1; hash nguồn ở checkout có CRLF và hash Git blob được ghi riêng. Khi source hoặc skeleton thay revision, capture/review lại affected inputs thay vì mang PASS cũ.

Bảo chốt data/skeleton hoặc thay assumption trước Phase 2. Lượt này đã hoàn thành phần chuẩn bị và hậu kiểm bounded; chưa tự ghi data lock hoặc final package acceptance.
