# Unified Case Reader — ứng viên offline

Một HTML chứa 11 treatment × 4 locale = 44 tổ hợp hiển thị, phục vụ 33 entry journey FDI trong inventory (11 × 3 locale đầu vào). Hiển thị tiếng Việt vẫn là nội dung FDI, không phải journey VN nội địa.

**Trạng thái:** bản sửa local sau audit 28/10/2026; Bảo yêu cầu commit checkpoint trong phiên này. Commit chứa bản ghi này lưu gói sửa trên nhánh hiện tại; chưa merge/push, chưa upload hay publish. Đóng gói không đóng blocker hosting, quyền proof, tracking, native review hoặc campaign readiness. [Kế hoạch và evidence](../../operations/unified-case-reader/2026-10-28/PLAN.md).

## File và dependency

- [unified-case-reader.html](unified-case-reader.html): CSS/JS, logo và ảnh đều nhúng; không tải font/CSS/script/ảnh ngoài khi mở trang. Font dùng fallback hệ thống; hình dạng chữ có thể khác giữa các máy.
- Dung lượng hiện tại: 905146 bytes (883.9 KiB). Các liên kết nguồn/contact là external navigation chỉ khi khách bấm, không phải tài nguyên cần tải để đọc bài.
- Bỏ 11 link quay lại `index.html` của viewer offline. Chưa có đích quay lại production được chốt; không thay bằng URL tùy ý. CTA/contact/source còn giữ đúng bản nguồn, Partner không được tự thêm nút tư vấn.

## Router và tham số

| Tham số | Giá trị và thứ tự xử lý |
|---|---|
| `t` (alias `treatment`) | O1, O2, O3, O4-O, O4-Q, F1–F3, P1–P3; mã không phân biệt hoa thường; chấp nhận o4o/o4q |
| `lang` (alias `locale`) | `vi`, `en`, `zh-Hans`, `zh-Hant`; giá trị hợp lệ ưu tiên hơn UTM |
| `utm_campaign`, `utm_content` | Nếu thiếu/sai mã trực tiếp, suy treatment và locale từ chuỗi UTM; mẫu có hỗ trợ: `fdi_o4-q_zh-hans_cold_test`, `fdi_f1_en_rmk_test`. Đây không phải quyết định naming campaign mới. |
| `entry` | Chỉ O2: allowlist `B4`, `B5`, `B6` để giữ bản nguồn của journey khi chuyển ngữ/reload. Không nhận URL hoặc HTML. |

Ví dụ: `?t=F2&lang=zh-Hans`, `?t=O4-Q&lang=en`, `?t=O2&lang=en&entry=B6`.

Không suy được treatment → O1; không suy được locale → **en** theo contract shared reader. Không có tham số → O1/en. Fallback này chỉ chọn nội dung trong file; không bảo đảm host/path luôn trả HTTP 200. Mọi entry ad cần `t` và `lang` rõ ràng, được kiểm xuyên route trước sử dụng.

Chuyển ngữ cập nhật tiêu đề, nội dung, alt/aria, html lang, trạng thái nút và URL bằng `history.replaceState`; giữ treatment, UTM, vị trí cuộn và focus. Với O2, nếu không có `entry` hợp lệ, en/vi chọn B4, zh-Hans chọn B5, zh-Hant chọn B6. Sau toggle, `entry` được ghi vào URL để giữ nguyên nguồn khi reload; đổi ngôn ngữ không đổi câu hỏi của source journey.

## Nội dung và ảnh

| Treatment | Tiêu đề tiếng Việt thực tế | Nguồn case / ảnh |
|---|---|---|
| O1 | Cùng dữ liệu gốc để rà soát chất lượng | Case 06, China / ảnh tham quan 2020 (Sohu) |
| O2 | Cùng thông tin làm căn cứ bàn giao lô | Case 06, China / ảnh tham quan 2020 (Sohu) |
| O3 | Cùng hồ sơ sản xuất cho trao đổi cuối tháng | Case 06, China / ảnh tham quan 2020 (Sohu) |
| O4-O | Ba câu hỏi trước lần bàn giao lô tiếp theo | Case 06, China / ảnh tham quan 2020 (Sohu) |
| O4-Q | Ba câu hỏi trước khi rà soát kết quả kiểm thử bất thường | Case 06, China / ảnh tham quan 2020 (Sohu) |
| F1 | Ba câu hỏi trước lần cập nhật sản xuất tiếp theo từ đối tác | Bright Power, China / ảnh minh họa có nhãn |
| F2 | Ba câu hỏi trước kế hoạch gia công ngoài tiếp theo | Bright Power, China / ảnh minh họa có nhãn |
| F3 | Ba câu hỏi trước lần bàn giao tiếp theo với đối tác | Bright Power, China / ảnh minh họa có nhãn |
| P1 | Từ hồ sơ lô đến quyết định vận hành tiếp theo | Wafer Works, Taiwan–Shanghai / ảnh minh họa có nhãn |
| P2 | Xác định người sở hữu hồ sơ trước khi bàn giao hệ thống | Wafer Works, Taiwan–Shanghai / ảnh minh họa có nhãn |
| P3 | Xác định phạm vi câu hỏi của khách hàng trước khi thu thập hồ sơ | Wafer Works, Taiwan–Shanghai / ảnh minh họa có nhãn |

O2 không phải ba bản nguồn đồng nhất: B4/B5 giữ câu hỏi về phiên bản tham số/ngoại lệ; B6 giữ câu hỏi thông tin bàn giao và bước tiếp theo. Cả hai bản được bảo toàn, không tự chấp nhận bản này thay bản kia. Các nguồn reader gốc không thay đổi.

## Hosting và tracking: còn phải chứng minh

[Runbook LadiPage](../../operations/LadiPage_Draft_Runbook.md) ghi route Basic đã dùng cho ba trang khác; chưa chứng minh import/router của file này hoặc chốt host/URL của nó. Không có hướng dẫn publish một bước hay khẳng định tự kế thừa GTM. Evidence cũ ghi loader GTM được thêm trong page settings trên từng route đã duyệt; không chứng minh trang mới có container, đúng version hoặc event.

Trước thao tác ngoài máy: có mandate đúng target/route; chứng minh import và JS/URL trên preview; inventory tag/event/consent/privacy theo đúng URL; kiểm desktop/mobile, UTM, nguồn copy, CTA và locale; publish chỉ khi được cấp quyền. Nếu sửa một trong ba trang đang tồn tại, dùng `$ladipage-operator` với `revise_existing_page` và receipt/preflight tương ứng; không tự tạo trang thay thế.

[Entry mapping canonical](../../operations/linkedin-rmk-source-readiness/2026-10-08/04_Reader_Entry_Mapping_Draft.md) và [hồ sơ sửa](../../operations/unified-case-reader/2026-10-28/REVIEW.md) ghi scope, hash, checks và các gate còn mở. Bản nguồn chưa được chứng nhận public/paid rights, native-market hay toàn journey; không suy readiness từ kiểm tra router.
