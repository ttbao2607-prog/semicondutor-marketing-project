# Bảo — quyết định cuối W1 cho F1/F2

Trạng thái: INTERNAL_PREPARATION_COMPLETE / W2_NOT_AUTHORIZED. Gói này cụ thể hóa plan đã duyệt, không đổi tiêu chí kinh doanh hoặc kết luận hiệu quả trước khi có dữ liệu. [Contract](CONTRACT.md) · [7 kịch bản](SCENARIOS.csv) · [Cách đọc số](METRICS.md) · [Asset dự phòng](ASSET_OPTIONS.md) · [Decision log](DECISION_LOG.csv).

## Phạm vi đang chạy và thời điểm review

Theo [activation receipt](../../pre-ad-readiness/2026-10-29/f1-f2-cycle/SCHEDULE_ACTIVATED.md), last observed29Oct: parent Active, ad set On/Scheduled; F1/F2 On/Active. Chỉ một cold ad set R5/English ở Việt Nam, USD10/ngày chung; Reach/Maximum delivery, Feed only, Expansion/LAN/RightRail off. Tên còn DRAFT_REVIEW không còn nghĩa là đang draft. Không làm live readback mới trong lượt chuẩn bị này.

W1 đã schedule từ **01/11/2026 07:00 → 08/11/2026 06:45 giờ Việt Nam**; saved platform dates01–07Nov. Đây là cửa sổ lịch, không chứng minh đủ7ngày delivery. Ghi actual first delivery và các khoảng pause/reject; eligible-delivery-day3/day7 phụ thuộc lúc thực sự phân phối. Không tự kéo dài lịch nếu xét duyệt chậm.

- Trước/đầu chạy: đọc xét duyệt, delivery, targeting, link và pacing khi Bảo giao readback.
- Trong kỳ: note integrity/pacing hằng ngày và kiểm ở ngày delivery3/7 là cadence đề xuất theo data plan; chưa tạo tác vụ tự chạy.
- Cuối kỳ: snapshot từ08/11 sau06:45 VN; ghi timezone báo cáo và đúng timestamp/cửa sổ nền tảng. Kết quả ban đầu có thể provisional vì report/GA4 chậm; recheck khi nguồn đã xử lý, ghi thời điểm thực tế. Mốc09/11 trong operating proposal cũ không còn là ngày kết thúc lịch này.
- Lịch W1 tự kết thúc; W2 không tự nối tiếp. Không phê duyệt kịp thì giữ hết lịch, không mặc định gia hạn.

## Thứ tự ra quyết định

Đọc C1 integrity trước → C2 audience và C3 delivery → C4 cold/C5 đọc tiếp → C6 RMK. C7 dữ liệu mỏng có thể áp dụng ở mọi khâu. Một kỳ có thể gặp nhiều nhánh; ghi nhánh chính và nhánh phụ, không cộng chúng thành các nhóm campaign mới. Lỗi link/locale/claim/targeting/measurement thật hoặc budget breach phải được báo ngay, không đợi hết W1.

Điền [READBACK.csv](READBACK.csv) theo [METRICS](METRICS.md), đối chiếu source trong [SOURCE_REGISTRY.csv](SOURCE_REGISTRY.csv), rồi ghi decision log. Các dòng hiện là PLANNED_NOT_OBSERVED, không phải số liệu đã lấy. Không đưa raw account/member/lead data vào public repo; account/ad numeric IDs và raw exports giữ private, đối chiếu với tên + identity trong saved receipt, ghi tham chiếu evidence đã sanitize.

## Bảo chốt gì ở cuối W1?

Chọn action cụ thể: giữ hết lịch/giữ ngân sách; tiếp tục cold với ngày và ngân sách mới; sửa đúng một đoạn; hoặc dựng RMK sau gate. Mỗi quyết định ghi kỳ đo/raw counts/độ tin cậy, phần giữ/phần đổi, owner, ngân sách/ngày bắt đầu-kết thúc, recheck và rollback. Không cần xin duyệt lại tổng plan11,7triệu/đợt đầu5,6triệu/giữ lại6,1triệu; chỉ ghi việc dùng phần còn lại cho hành động cụ thể, không mặc định giải ngân reserve hoặc Search. USD10 là daily pacing shared, nominal W1USD70, không lifetime hard cap; không tự dùng tỷ giá để suy spend VND.

CTR cao không tự chứng minh đúng khách hoặc liên tưởng thương hiệu; thiếu lead không tự là W1 fail. Phản hồi downstream là bổ sung khi Bảo nhận, không chặn paid review. Không phát sinh rep tin nhắn/CRM/form-success workflow trong gói này.

## Khoảng trống còn phụ thuộc dữ liệu

Không có performance baseline, sample minimum hay ngưỡng CTR/frequency/CPM win-loss đã được duyệt cho F1/F2. Metric definitions và quyết định gates đã có; numeric criteria vẫn UNSET, cần Bảo chọn trước phép thử tiếp theo theo lượng dữ liệu/ngân sách thực, không chọn ngưỡng sau khi thấy số để hợp thức hóa winner. Khi chưa đủ cơ sở ghi INCONCLUSIVE và C7. Hai ads dùng chung thuật toán/budget, không bảo đảm equal rotation hay A/B test.

RMK source rule/lookback/objective chưa chọn, audience chưa được xác minh tạo/Ready trong gói này. CSV registry là mapping dự kiến của hai ads đã lưu, không phải audience đã tạo. Native delivery mapping RMK chưa có; không bật chỉ vì đã hết tuần hoặc library có ảnh.
