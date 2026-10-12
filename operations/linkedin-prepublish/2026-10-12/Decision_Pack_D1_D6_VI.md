# Decision pack D1–D6 — bảng build 99 ad (gửi Bảo)

12/10/2026 · Trạng thái **DRAFT_FOR_PO_DECISION**, chuẩn bị offline (Phase A). Không tạo ad, không đăng, không thao tác tài khoản. Nguồn: [bảng build](../2026-10-08/03_LinkedIn_Ad_Build_Sheet.md), [gói RMK](../../linkedin-rmk-source-readiness/2026-10-08/README.md), [map reader → URL](../../linkedin-rmk-source-readiness/2026-10-08/04_Reader_Entry_Mapping_Draft.md), [quyết định tuần/ngân sách của Bảo 07/10](../../manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md).

Phân loại dưới đây tách **Đã biết** (có nguồn trong repo), **Chưa biết** (chưa kiểm) và **Đề xuất** (ý kiến của tôi, không phải sự thật). Đề xuất chỉ là điểm xuất phát để Bảo chọn Approve / Change / Hold.

## Tóm tắt

| # | Quyết định | Đề xuất ngắn | Phụ thuộc |
|---|---|---|---|
| D1 | Đích đến của ad cold (Single image) và ad giải thích | Cả hai trỏ tới reader, giống ad proof | Route host reader đang **UNKNOWN** |
| D2 | Loại nút CTA của LinkedIn | Chọn trong giao diện khi tạo ad; mặc định đề xuất "Learn more" | Danh sách nút chưa kiểm |
| D3 | Journey chạy tuần 1 | Chọn 1 nhóm + vài journey đại diện, không chạy 33 | Quyết định của Bảo |
| D4 | Giải thích và proof: 2 carousel hay 1 | Giữ 2 carousel | Ảnh hưởng số card, intro |
| D5 | Quy ước đặt tên ad | Dùng `LI-<wave>-<treatment>-<locale>-<role>-v1` | Khớp UTM và sheet readback |
| D6 | Targeting và delivery control | Không kế thừa bản cũ, đọc lại từng mục trong giao diện | Cần mandate tạo campaign |

## D1 — Đích đến của ad cold và ad giải thích

- **Đã biết:** Chỉ ad proof có đích đến đã ghi (reader). Viewer journey không ghi đích cho ad cold và ad giải thích. Mỗi treatment/locale có một reader, vào bằng `?lang=<locale>`, và có công tắc 4 ngôn ngữ. Reader nhóm Fabless và O-series có nút CTA trỏ tới trang liên hệ của Digiwin Việt Nam; 9 reader Partner không có nút CTA hay link liên hệ.
- **Chưa biết:** Route đưa reader lên mạng (HTML cục bộ, chưa chứng minh LadiPage nhận HTML tùy ý). Link "quay lại" trong reader đang trỏ tới `index.html` của viewer nội bộ, nên chưa có nghĩa trên môi trường thật. Quyền dùng ảnh công khai/trả phí chưa xác minh.
- **Lựa chọn:** (A) cả ba ad trỏ tới reader của journey đó; (B) cold và giải thích trỏ tới trang liên hệ Digiwin Việt Nam, proof trỏ tới reader; (C) mỗi ad một đích khác nhau.
- **Đề xuất: A.** Reader được thiết kế như trang đích; trỏ ad cold thẳng tới trang liên hệ bỏ qua bước giải thích. UTM đã có thiết kế theo từng ad (`utm_content=<batch>_<creative_id>`) nên chia sẻ một URL reader vẫn đọc tách được từng ad. Đây là ý kiến, chưa có số liệu.
- **Mở khóa:** điền cột đích đến ở bảng build, gốc cho mapping UTM. Chưa mở khóa được việc đưa lên mạng nếu route host chưa chứng minh (cần mandate riêng).

## D2 — Loại nút CTA

- **Đã biết:** Artwork đã có cụm CTA riêng; build pack cũ dùng "Learn More". 75 lần xuất hiện CTA trên card (mục 04 gói review).
- **Chưa biết:** Danh sách nút khả dụng của LinkedIn theo objective/định dạng không có nguồn trong repo.
- **Lựa chọn:** (A) "Learn more" cho cả ba vai trò; (B) khác nhau theo vai trò (ví dụ cold không nút, proof "Learn more"); (C) quyết khi thấy danh sách nút trong giao diện.
- **Đề xuất: C, mặc định A.** Nút nền tảng không nên mâu thuẫn với cụm CTA trên artwork. Cần xem danh sách thật khi tạo ad nên không chốt trước được.
- **Mở khóa:** cột CTA ở bảng build.

## D3 — Journey chạy tuần 1

- **Đã biết:** Package nêu "một nhóm phù hợp và ít mẫu đại diện" cho đợt đầu 5,6 triệu. Bảo đã quyết tuần 1 chạy đúng plan, review cuối tuần rồi chọn hướng tuần 2. Bảng build chứa cả 33 journey (11 treatment × 3 locale), mỗi journey 3 ad = 99 ad.
- **Chưa biết:** Nhóm/locale nào là "phù hợp" chưa được ghi thành quyết định. Chưa có dữ liệu phân phối.
- **Đề xuất:** cắt bảng 99 ad xuống còn vài journey đại diện của một nhóm. Việc chọn nhóm và locale là quyết định của Bảo; repo không có căn cứ để tôi chọn thay. Tôi chỉ cắt bảng sau khi Bảo nêu nhóm.
- **Lưu ý:** audience Discovery đang CHANGES_REQUIRED và chưa đọc lại sau upload v3; lựa chọn nhóm nên tính đến việc không suy từ identity công ty sang ICP hay quyền mua ERP.
- **Mở khóa:** số ad cần dựng, số reader cần host, đúng một đợt review native cho các chuỗi thực sự dùng.

## D4 — Giải thích và proof: 2 carousel hay 1

- **Đã biết:** Viewer hiện có hai giai đoạn riêng. Gộp sẽ đổi số card và intro text (intro 38–230 ký tự, trung vị 61). Hướng đã chốt: cold Single image → audience từ chính ad mới → Carousel RMK.
- **Chưa biết:** Giới hạn số card carousel của LinkedIn không có trong repo.
- **Đề xuất:** giữ 2 carousel như viewer đã review. Gộp là thay đổi nội dung, sẽ phải qua tiền/hậu kiểm lại.
- **Mở khóa:** số ad cuối cùng (99 hay ít hơn) và nội dung gói review.

## D5 — Quy ước đặt tên ad

- **Đã biết:** Đề xuất trong bảng build là `LI-<wave>-<treatment>-<locale>-<role>-v1`. UTM cũng đề xuất: `utm_source=linkedin`, `utm_medium=paid_social`; repo **chưa có quy ước UTM LinkedIn**, chỉ có của Google Search.
- **Đề xuất:** chấp nhận tên trên, và kiểm kê tag/event có sẵn trước khi chốt nhãn UTM, tránh trùng lặp và không đưa thông tin cohort hay công ty vào URL.
- **Mở khóa:** sheet readback tuần 1 dùng cùng ID.

## D6 — Targeting và delivery control

- **Đã biết:** Bản đề xuất cũ để Audience Expansion và LinkedIn Audience Network ở trạng thái tắt; mục đó đã bị ghi *superseded*. Checklist ghi targeting (Việt Nam, chức năng, cấp bậc) và lịch chưa được mandate. Quan sát 11/10 trên audience backup: tiếng Anh + Việt Nam ≈ 8.200 → chức năng ≈ 5.000 → cấp bậc ≈ 460; lọc đầy đủ theo tiếng Việt < 300. Đó là ước tính trong giao diện cho một audience cụ thể, không phải dự báo của chiến dịch.
- **Chưa biết:** Cấu hình hiện tại trong tài khoản cho từng setting.
- **Đề xuất:** không kế thừa bản cũ; đọc từng setting trong giao diện khi có mandate tạo campaign rồi ghi vào build pack. Tôi chưa có căn cứ để đề xuất bật/tắt từng mục.
- **Mở khóa:** cần mandate tạo campaign (checklist hàng 4); không thực hiện được trong Phase A.

## Các quyết định liên đới đã chuẩn bị ở gói RMK (không lặp lại ở đây)

- R1–R5 (quy tắc tương tác, lookback, cấu trúc pool, objective RMK, chủ sở hữu source): [01](../../linkedin-rmk-source-readiness/2026-10-08/01_RMK_Source_Rule_Decision_Pack.md). Đề xuất của gói đó: tương tác bất kỳ, 30 ngày, một pool cho mỗi cohort tương thích, ngưỡng 300 thành viên theo giao diện.
- Câu hỏi mở về reader (host, link quay lại, CTA Partner, reader dùng chung, quyền ảnh): [04](../../linkedin-rmk-source-readiness/2026-10-08/04_Reader_Entry_Mapping_Draft.md).
- 13 hạng mục chờ mandate vận hành: [06](../../linkedin-rmk-source-readiness/2026-10-08/06_Operational_Mandate_Checklist.md).

## Giới hạn

Pack này không xác minh gì trên nền tảng. Các nhận định về giao diện LinkedIn (danh sách nút, giới hạn card) là **chưa kiểm**. Không có verdict MSG-ANCHOR hay native review. Trạng thái audience hiện hành xem [CURRENT_STATE](../../../CURRENT_STATE.md).

Docs impact reviewed: không đổi ngân sách, asset, verdict hay quyết định; chỉ thêm tài liệu chuẩn bị quyết định.
