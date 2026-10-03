> **PO freeze 03-10-2026:** Bảo chốt hybrid harness và chọn Sol visual family làm chuẩn project; native leaf mặc định `gpt-6.1-sol/low`, runtime/admission/acceptance phải xác minh, không silent Luna fallback. Lifecycle giữ `testing_dogfood`. Quyết định này supersede ghi chú chưa PO duyệt hướng visual hoặc pending/uncommitted bên dưới cho current freeze này; historical operator FAIL/CHANGES_REQUIRED và findings không đổi, không blanket buyer/live/external release hoặc thêm image calls. Quyết định được ghi bởi containing local freeze checkpoint, prior baseline `7e95a44`; không push/merge. [Freeze record](LinkedIn_ImageGen_Harness_Freeze_2026-10-03.md).

> **Hiện hành 03-10-2026 — hybrid full carousel.** Đã tạo 20 base/0 correction, F2-A/P2-A đủ năm thẻ mỗi carousel cho Sol/low và Luna/max. Cả hai CHANGES_REQUIRED; execution PARTIAL, measurement COMPLETE, creative audit FAIL, lifecycle testing_dogfood. 49 tests và parent 19 negative + 3 positive/model đạt. 20 native 1254 × 1254 giữ nguyên byte đạt policy mới minimum 1080; chưa creative/PO/buyer/live acceptance. Bảy lỗi chữ chắc chắn, Sol F2-A3 microglyph cách ly riêng; tick/bridge và cả bốn closing Taiwan source khó đọc mobile 390px cần sửa. R2 office/daylight/material phần lớn trở lại; Luna P2-A1 teal là operator outlier. Active bốn R2 + logo (năm refs), sau một lần bảy refs bị từ chối trước inference tạo zero ảnh. Không quyền gọi tiếp. Proposal bảy thẻ và chưa-alignment bên dưới là lịch sử được full-carousel mandate thay thế; forward alignment đã triển khai. Trial cũ exact 1024 / actual 1254 vẫn FAIL; checkpoint implementation/preparation lịch sử giữ nguyên. [Báo cáo nội bộ](LinkedIn_ImageGen_Hybrid_Full_Dogfood_Benchmark_2026-10-03.md) và status JSON giữ rõ phạm vi. Local uncommitted, chưa stage/commit/push, remote thực chưa kiểm tra.

# Tiêu chí duyệt creative chiến dịch R2

Ngày 03-10-2026. Dùng để xem các phiên bản sẽ được chuẩn bị tiếp theo, không đánh giá lại ảnh hoặc hợp đồng lịch sử. Bảo đã chấp nhận màu, nội dung và logo của ảnh thử; hình ảnh và chấp nhận toàn quảng cáo vẫn chờ xem.

## Quy tắc quyết định

- **Dừng:** nội dung sai hoặc chưa được duyệt, hoặc nguồn bắt buộc không đọc được. Không mở rộng sản xuất trước khi giải quyết.
- **Chỉnh:** nội dung đúng, nhưng đã chỉ ra khoảng thiếu về hình ảnh hoặc mạch kể. Nêu card, vị trí và việc cần sửa; xem lại các phần phụ thuộc.
- **Đạt:** tất cả tiêu chí được giao đã được quan sát và thỏa mãn trên phiên bản đang xem. Không tự cấp Đạt khi chưa có bằng chứng quan sát.

| Mức xem | Điều cần thấy để Đạt | Ví dụ cần Chỉnh | Ví dụ cần Dừng |
|---|---|---|---|
| Từng card | Câu hỏi hoặc hành động rõ; hình giải thích đúng quan hệ; cùng chất liệu, ánh sáng và phân cấp R2; chữ, logo và nguồn dễ đọc ở khung đọc bình thường trên máy tính và điện thoại | Khoảng trống, chất liệu, phân cấp chữ hoặc sơ đồ chưa hòa vào cảnh; nội dung vẫn đúng | Sai quan hệ, chữ chưa duyệt, giá trị hồ sơ giả, ghi chú nội bộ hoặc nguồn cần thiết không đọc được |
| Toàn bộ năm card | Mở đầu đủ ai nói, người đọc, tình huống và lý do đọc tiếp; chuyển ý thêm nghĩa; kết nối được với câu chuyện; nhận diện ổn định, mỗi hình làm việc riêng | Chuyển ý lặp hoặc yếu, nhận diện lệch, hai hình cùng nghĩa không có lý do | Thiếu card hoặc nguồn bắt buộc; đổi đối tượng hay phạm vi không có căn cứ; hình khiến nội dung thành ý sai |
| Giữa các tình huống | Nhận ra cùng chiến dịch qua ánh sáng, chất liệu, nhận diện và chữ; vật thể, quan hệ phù hợp từng nhóm; hai card đối chiếu có vai trò khác nhau | Một tình huống quá chung chung hoặc mang đạo cụ OSAT không phù hợp; nội dung vẫn đúng | Thêm năng lực hoặc case chưa được duyệt; hình mang ý nghĩa sai hoặc nguồn không đọc được |

Lệch phong cách hoặc mạch kể khi nội dung vẫn đúng cần Chỉnh; nếu hình làm nội dung thành sai hoặc chưa được duyệt thì Dừng. Không dùng điểm trung bình, số đạo cụ, từ khóa hoặc sự khác nhau của mã ảnh để chứng minh chất lượng. Một sơ đồ đúng nguồn vẫn dùng được nếu hòa vào ngôn ngữ chiến dịch. Lặp cách nhận diện có chủ ý được giữ; lặp ý nghĩa hình cần lý do trong câu chuyện. Đạt ở một mức không tự cấp Đạt ở mức khác.

## Cách xem và biểu mẫu nội bộ

Xem ảnh thực tế cạnh sáu mẫu R2, rồi xem cả bộ cạnh nhau. Đọc đủ chuỗi năm card và phần giới thiệu từ góc nhìn người mới gặp quảng cáo. Kiểm tra trên máy tính, điện thoại ở kích thước đọc bình thường không phóng to, và thêm ảnh gốc khi cần.

Người xem: [tên] · ngày: [ngày] · phiên bản nội dung/ảnh/bản xem: [mã hoặc liên kết nội bộ] · bề mặt xem và chiều rộng: [thực tế quan sát]. Không điền sẵn quyết định của Bảo.

| Mã card | Ảnh mẫu R2 gần nhất | Người đọc cần hiểu gì | Quan sát thực tế | Đạt / Chỉnh / Dừng | Sửa gì, ai phụ trách, xem lại gì |
|---|---|---|---|---|---|
| [card] | [mẫu] | [ý nghĩa] | [bằng chứng trên ảnh và bề mặt đã xem] | [chờ xem] | [việc cụ thể / tên / phần phụ thuộc] |

| Chuyển ý trong carousel | Ý nghĩa cần phát triển | Quan sát thực tế | Quyết định | Sửa và xem lại |
|---|---|---|---|---|
| [1→2, 2→3, 3→4, 4→5 hoặc phần kết] | [ý nghĩa] | [bằng chứng] | [chờ xem] | [việc / người / chuỗi liên quan] |

| Hai tình huống đối chiếu | Dấu hiệu cùng chiến dịch | Khác biệt cần thiết về vai trò/vật thể | Quan sát và khoảng thiếu | Quyết định, sửa và xem lại |
|---|---|---|---|---|
| [tình huống 1 / tình huống 2] | [ánh sáng / chất liệu / nhận diện / chữ] | [phù hợp từng câu chuyện] | [bằng chứng] | [chờ xem / việc / người] |

Kết luận của người xem: [chờ xem] · các phần chưa quan sát: [ghi rõ] · quyết định của Bảo: [chưa ghi nhận]. Thay phiên bản phải xem lại quyết định phụ thuộc. Hiểu đúng của người mua khi chưa thử thật vẫn là điều chưa biết; quy trình không tự bảo đảm chất lượng hình ảnh. Hồ sơ vận hành ở nội bộ; thông tin nguồn đúng và cần thiết vẫn hiện trong nội dung được duyệt.

## Bước thử tiếp theo được đề xuất

Chuẩn bị một quảng cáo đủ năm card và hai card làm hai việc khác nhau của một tình huống đối chiếu. Đây không phải yêu cầu sản xuất tự động hai nhánh A/B với mười bản ghi. Đề xuất tối đa bảy lượt tạo ảnh gốc, không có lượt sửa ảnh. Chưa được phép gọi công cụ tạo ảnh.

Trước khi chạy, phải xác định và duyệt đúng tình huống, quảng cáo, mã card, nhóm dùng chung, đường dẫn đầu ra, phiên bản nội dung và nguồn; đồng thời ghi nhận quyết định cấp phép riêng. Hai card của tình huống thứ hai phải có vai trò khác nhau, chẳng hạn mở đầu và giải thích quan hệ hoặc bước tiếp. Xem cả chuỗi năm card và cả bảy ảnh để đánh giá mạch kể và tính nhất quán giữa tình huống. Kết quả nhỏ này không tự cấp phép toàn chiến dịch, không chứng minh người mua hiểu đúng và không cấp quyền hoạt động trên tài khoản thật.

Đối với lượt tạo ảnh trong tương lai, ảnh gốc phải vuông, mỗi cạnh ít nhất 1080 pixel; không thay đổi kích thước hoặc ghép ảnh để đạt điều kiện. Kiểm tra kích thước ảnh thực tế sau mỗi lượt. Quy tắc này chỉ áp dụng về sau: hai thử nghiệm cũ yêu cầu 1024 nhưng nhận 1254 vẫn không đạt hợp đồng cũ; giữ nguyên hợp đồng, ảnh và báo cáo đã ghi.

Cần một điều chỉnh nhỏ được duyệt riêng trước khi gọi công cụ để đưa đầy đủ định hướng chiến dịch vào cách chuẩn bị ảnh. Điều chỉnh đó chưa được làm trong bước chuẩn bị này.

## Phụ lục nội bộ

Chuẩn bị `READY_FOR_PO_REVIEW`; chưa sản xuất. Kết quả hợp đồng thử cũ vẫn `FAIL`. Phải có đúng card, nội dung, nguồn và quyết định cấp phép trước lượt tương lai; điều chỉnh nhỏ của cách thực thi chưa làm. Kiểm tra tính toàn vẹn và quyết định chất lượng của con người là hai lớp riêng.

Bước chuẩn bị đã qua audit, sẵn sàng cho Bảo xem; chưa sản xuất. Parent đã xem bản hướng dẫn trên máy tính 1280×900 và điện thoại 390×844, kiểm tra sáu ảnh và tính toàn vẹn của 528 tệp được bảo vệ. Kết luận chỉ áp dụng bước chuẩn bị, không chấp nhận creative mới hoặc cấp phép sản xuất. Hồ sơ audit nội bộ: `operations/linkedin-awareness-execution/campaign-r2-preparation-2026-10-03/operator-audit.json`.
