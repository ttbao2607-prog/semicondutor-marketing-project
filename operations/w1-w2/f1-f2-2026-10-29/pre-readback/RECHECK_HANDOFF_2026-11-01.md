# Handoff — recheck F1/F2 ngày 01/11/2026

29/10/2026 · revision 1 · **HANDOFF_ONLY / NOT_STARTED**. Authority: Bảo (chat 29/10/2026): cần recheck, sẽ làm vào 01/11, nên chỉ để lại handoff. Tài liệu này không phải mandate live; người/agent thực hiện cần mandate đọc của Bảo cho ngày đó. Không đặt lịch tự động.

## Mục tiêu

Đóng các trường [Q1](FOLLOWUP_Q1_READBACK.md) còn UNVERIFIED, trước/ngay sau 01/11 07:00 VN. Không sửa ad/lịch để đạt kết quả; không Save/Launch/pause/enable.

## Cần đọc lại (ưu tiên)

| # | Trường | Vì sao còn mở | Cách đọc |
|---|---|---|---|
| 1 | Nhãn review/hold/rejection từng ad `LI-wave01-F1/F2-en-COLD-v1` | danh sách chỉ hiện "Active"; Active ≠ đã duyệt | phiên **chụp được ảnh**; tìm nhãn trên hàng ad hoặc trang xem ad; nếu không có, ghi UNVERIFIED |
| 2 | Giờ bắt đầu/kết thúc thực tế (07:00 → 06:45 VN) và timezone tài khoản | editor chỉ hiện ngày | đọc nơi nào UI hiển thị giờ; ghi timezone nguồn LinkedIn; lịch dự kiến tách khỏi actual first delivery |
| 3 | Destination URL / UTM live của hai ad | công cụ đọc bị chặn giá trị chứa query string | phiên đọc được giá trị hoặc ảnh; đối chiếu [SOURCE_REGISTRY](../SOURCE_REGISTRY.csv) (`t=F1/F2`, `lang=en`, `fdi_f1/f2_en_cold_wave01`, `f1/f2_cold_v1`) |
| 4 | Tín hiệu "Validation error icon" trong trình sửa ad set | cây truy cập liệt kê icon ở cả 7 mục lúc còn "Loading/Saving"; chưa giải thích | nhìn trực tiếp; nếu có lỗi thật, báo Bảo ngay kèm đề xuất bounded, không tự sửa |
| 5 | Trạng thái ad/ad set/parent, hai probe, budget USD10, placement, Expansion, list R5-52, English | giữ invariant | so với [Q1](FOLLOWUP_Q1_READBACK.md) |

Sau 01/11 07:00: ghi **actual first delivery**, khoảng reject/pause riêng, impressions/spend thực; không suy từ lịch. Báo cáo theo [Q2](FOLLOWUP_Q2_REPORT_MAP.md) (cột LinkedIn "Clicks to landing page" làm click vào reader; GA4 Traffic acquisition, Session campaign, tìm `fdi_`; không đòi LinkedIn clicks = GA4 sessions).

## Điều kiện dừng và báo ngay

Reject, target drift, link lỗi, budget risk, hoặc side effect ngoài ý muốn: dừng bước đó, báo Bảo kèm evidence; không tự pause/enable/extend. Mỗi lần rời editor dùng nút thoát của app (Cancel / Back to account), không bấm Save. Nên đọc từ danh sách trước; chỉ vào editor khi cần.

## Quy tắc giữ nguyên

Một browser controller; không spawn; đánh dấu rõ observed_at (giờ + timezone); numeric ID và ảnh/DOM thô giữ private ngoài repo, public chỉ có observation sanitize kèm SHA256/ref; không PII; không mở rộng sang campaign Test/RSCH. Nếu có trường vẫn không đọc được, ghi exact UNVERIFIED với blocker.

## Việc khác đang chờ Bảo

Source audience RMK **đã tạo** (xem [receipt](RMK_SOURCE_AUDIENCE_CREATED.md)): `RMK-SRC-F1F2-R5-EN-WAVE01-ANY-30D`, status Building lúc 13:42 29/10. Khi recheck, thêm mục 6: đọc lại Status (Building/Processing/Ready), kích thước/reachable thực (nếu UI hiển thị), ghi observed_at; không suy từ 470+. Chỉ gán Ready/S2 sau readback thực; không tạo ad RMK hay gắn targeting nếu chưa có mandate. R1–R3, R6 đã quyết theo mặc định; R4 (objective) và nguồn tiền W2 vẫn để sau.

Docs impact reviewed: chỉ thêm handoff; không đổi scope, lịch, budget, creative, tracking hay anchor; canonical pointer cập nhật ở `CURRENT_STATE.md`.
