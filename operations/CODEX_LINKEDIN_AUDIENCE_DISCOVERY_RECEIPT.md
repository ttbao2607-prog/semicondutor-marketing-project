> **Research live UI · 2026-10-05:** Exact Company List Ready/80%; Details và refreshed list có **753,731 members**, 117 Companies, tab Unmatched 86. VN + English profile + Engineering/Operations/IT/QA = **4,800+**; thêm Manager/Director/VP/CXO = **780** ở saved definition `RSCH-CL-VN-LEAD-20261005` (persistence verified). Cùng filters + Vietnamese profile báo too small. Size gate discovery đã xác minh; mapping quality/denominator và production decisions vẫn OPEN. Retargeting menu không có Carousel riêng; warm RMK chưa đủ evidence. Chỉ lưu Saved Audience; Exit without saving ad set, không publish/enable/spend. [Receipt](LinkedIn_Audience_Ready_Research_2026-10-05.md). Snapshot cropped-size phía dưới là lịch sử trước research.

> **Company List Ready · 2026-10-05:** Bảo xác nhận đúng `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`; ảnh cung cấp hiển thị **Ready / match rate 80% / Company List / Owned**, Active ad sets `-`. Exact audience count bị cắt nên chưa xác minh reachable size hoặc gán `AUD_STATUS_READY_VIABLE`. Điều kiện chờ Building của đúng tệp này đã gỡ; engagement RMK `LI-AUD-P1-ENGAGED-30D`, targeting/filtered reach, attachment, budget và live vẫn có gate riêng. Các snapshot Building ngày 2026-09-30 bên dưới là lịch sử, được thay thế cho current Company List status bởi [evidence và bảng task](LinkedIn_Company_List_Ready_Update_2026-10-05.md).

# BIÊN BẢN NGHIỆM THU KHÁM PHÁ LINKEDIN MATCHED AUDIENCE

## Snapshot lịch sử — 2026-09-30 (không phải current status)

- **Thời điểm kiểm tra (Timestamp):** 2026-09-30 14:16 UTC+7
- **Tài khoản Campaign Manager:** Tài khoản Digiwin đã được xác nhận trên UI (tên và ID được lược khỏi receipt đã sanitize)
- **Tên tệp đối tượng kiểm chứng:** `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`
- **Mã Trạng Thái Kết Luận (Deterministic Status):** `AUD_STATUS_PROCESSING_LATENCY`

### Số Liệu Đo Lường Thực Tế

- Tổng số công ty tải lên: 424
- Số công ty khớp thành công (Matched Companies): N/A; không hiển thị trên bảng Audiences
- Tỷ lệ khớp hiển thị (Match Rate): `-`
- Quy mô thành viên khả dụng (Target Audience Size): `-`
- Trạng thái hiển thị (Displayed Status): `Building`
- Nguồn: `Company List`; Active ad sets: `-`; Ownership: `Owned`

### Bằng Chứng Đo Lường

- Campaign Manager hiển thị toast `Your audience has been successfully created.` và đúng dòng audience test với trạng thái `Building`.
- Screenshot crop chỉ chứa dòng audience đã được quan sát trong phiên này, nhưng chưa được ghi thành file local. Vì vậy chưa có đường dẫn ảnh để đính kèm receipt; cần lưu ảnh vào `outputs/evidence/` để hoàn tất yêu cầu lưu bằng chứng của plan.
- Màn hình không cho biết ai bấm xác nhận. Việc Bảo đã xác nhận action-time được ghi nhận theo thông tin người dùng báo; trạng thái tạo thành công được xác nhận độc lập trên Campaign Manager.
- Không tạo/sửa campaign hoặc ad set; audience không được gắn vào ad set; không enable budget hoặc spend.

### Hành Động Tiếp Theo

- Chờ xử lý và kiểm tra lại sau 24 giờ; không suy luận match rate, quy mô, reach hay khả năng phân phối khi status còn `Building`.
- Không có lịch nhắc tự động nào được tạo.
