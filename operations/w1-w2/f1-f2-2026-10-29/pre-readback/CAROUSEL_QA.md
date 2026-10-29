# P5 — QA bốn carousel dự phòng (F1/F2 explanation 6 + proof 4)

Revision 1 · 29/10/2026 · INTERNAL_REVIEW_COMPLETE_WITH_FINDINGS. Authority: Bảo giao P4–P7. Review nội bộ, **không là native-ready/live-ready**; không tạo ad, không generate hay sửa ảnh, không publish. Root tự review; independent audit NOT_RUN. Anchor VY-CONTENT-ANCHOR r1.0, nhánh FDI · English · Fabless (F1 Operations, F2 Planning). Quyền dùng exact set đã được Bảo chấp nhận ([PO acceptance](../../../pre-ad-readiness/2026-10-29/f1-f2-cycle/PO_PAID_ASSET_ACCEPTANCE.md)); không hỏi lại, và không hồi tố visual/native PASS.

## Phương pháp và giới hạn

- **Nguồn pin:** `B13-en-f1-v5` (`b13-review-copy-v5-six-explanation`) và `B16-en-f2-v2` (`b16-review-copy-en-v2`) trong `deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/`; copy/headline/alt từ `selected-copy.json`.
- **Đã làm:** đo độ phân giải và hash từng PNG; xem từng ảnh duy nhất ở kích thước phiên bản điện thoại (hạ xuống 420 px, mô phỏng đọc trên phone, không phải native preview); đối chiếu headline/alt/thứ tự/giới hạn.
- **Chưa làm / không chứng minh được:** native platform preview (chưa có draft carousel); reader trực tiếp: trang reader render bằng JS nên truy cập tĩnh chỉ ra phần đầu trang, còn mở bằng trình duyệt sẽ sinh traffic GA4 giả → **không quan sát lại reader trực tiếp lượt này**. Transition từ reader dùng evidence 29/10 (`f1-f2-cycle/evidence`, `OBSERVATIONS.json`), gắn nhãn FROM_EXISTING_EVIDENCE.
- Trạng thái nguồn: README B13 ghi `REVIEW_DRAFT_RENDER_GATE_PENDING` và mobile đầy đủ chưa đủ ở lần review trước; B16 ghi `PASS_SELF_REVIEW` nhưng chưa native-market/independent. Ghi lại, không nâng.

## Ảnh duy nhất: 16 chứ không phải 20

Tất cả PNG là 1254×1254, 1,65–1,89 MB. Bốn bộ có 20 vị trí nhưng ảnh dùng chung: explanation card 6 giống hệt nhau giữa F1 và F2 (sha `8D2D935B…`); proof card 1, 3, 4 giống hệt nhau (sha `07D462C4…`, `76CC1590…`, `0D045BD1…`); chỉ proof card 2 khác nhau (cùng copy, layout khác: `34D81860…` ở F1, `A8F0A88C…` ở F2). Vậy: explanation 11 duy nhất + proof 5 duy nhất = **16**.

## Checklist từng card (đọc ở cỡ phone; ✓ = đọc rõ, không cắt chữ)

### F1 explanation (6) — thứ tự 1→6

| Slot | Card | Native headline (ký tự) | Đọc / bố cục | Ghi chú |
|---|---|---|---|---|
| 1 | F1-A1 | Partner reports. A clear view of each lot? (42) | ✓ | nối thẳng từ cold F1 |
| 2 | F1-A2 | Start with the product and lot. (31) | ✓ | |
| 3 | F1-A3 | Which stage does this report describe? (38) | ✓ | |
| 4 | F1-A4 | Who keeps the shared view current? (34) | ✓ | |
| 5 | F1-A5 | Give the next decision a shared basis. (38) | ✓ | pill “Explore outsourced-production questions” trong ảnh; dòng nguồn nêu “Digiwin Taiwan semiconductor solution material: ERP and MES” — quy cho tài liệu Taiwan, không ngụ ý MES ở Việt Nam |
| 6 | F1-A6 | Consulting and implementation in Vietnam (40) | ✓ | dùng chung với F2-A6; chỉ nói đội ERP consulting/implementation ở Việt Nam, không có deployment/kết quả Fabless Việt Nam |

### F2 explanation (6)

| Slot | Card | Native headline (ký tự) | Đọc / bố cục | Ghi chú |
|---|---|---|---|---|
| 1 | F2-A1 | Demand changed. Which lots matter? (34) | ✓ | |
| 2 | F2-A2 | Start with product and planning period. (39) | ✓ | |
| 3 | F2-A3 | When was this lot status recorded? (34) | ✓ | |
| 4 | F2-A4 | What needs confirmation from the partner? (41) | ✓ | |
| 5 | F2-A5 | Give replanning a shared basis. (31) | ✓ có lưu ý | khối chữ nguồn/footer dày, xuống 4–5 dòng, dòng cách sát; vẫn đọc được ở cỡ phone nhưng là chỗ chữ nhỏ nhất và câu “ERP business management and MES … production context” hơi nặng |
| 6 | F2-A6 | Consulting and implementation in Vietnam (40) | ✓ | ảnh trùng F1-A6 |

### Proof (4) — Bright Power China, dùng chung F1/F2 ngoại trừ card 2

| Slot | Card | Native headline (ký tự) | Đọc | Ghi chú |
|---|---|---|---|---|
| 1 | RMK-BRIGHT-1 | Digital solutions for manufacturing (35) | ✓ | giống nhau F1/F2; “Company introduction”, “from ERP to smart manufacturing” |
| 2 | RMK-BRIGHT-2 | A chip-design case from China (29) | ✓ | hai layout khác nhau (F1 vs F2), cùng copy; tên pháp nhân tiếng Trung hiển thị trong carousel EN là entity gốc của case, giữ |
| 3 | RMK-BRIGHT-3 | Outsourcing management in focus (31) | ✓ | chỉ nêu challenge “inefficient outsourcing management” và “integrated digital solution”, không KPI/module |
| 4 | RMK-BRIGHT-4 | Read the chip-design case (25) | ✓ | pill “Read the China case” trong ảnh |

Tất cả headline ≤ 45 ký tự; alt đều dạng “Illustration: <headline>”. Intro text hiện: F1 explanation 181, F2 explanation 219, F1 proof 129, F2 proof 171 ký tự ([BUILD_CANDIDATES](../../../pre-ad-readiness/2026-10-29/f1-f2-cycle/BUILD_CANDIDATES.csv)); giới hạn native thực tế chưa kiểm trong UI.

## Transition và toàn journey

| Bước | Disposition | Căn cứ |
|---|---|---|
| Cold (đang chạy, single image) → reader trực tiếp | FROM_EXISTING_EVIDENCE | đường click W1 thật: cold → reader `t=F1/F2&lang=en`; explanation/proof chỉ dùng cho RMK sau gate |
| Cold → explanation (F1: Ops outsourced production → partner reports; F2: demand change → lots cần xem) | OK (review nội dung) | cùng persona và pain, hook cold nối thẳng với card 1 |
| Explanation → proof Bright | OK có lưu ý | cầu nối là card 6 (đội tại Việt Nam) rồi “Company introduction” → case China; nhãn “from China” rõ nên không ngụ ý case chứng minh nhà máy Việt Nam (A6/A7); proof giống nhau giữa F1/F2 nên không phân biệt theo treatment |
| Proof → reader đúng treatment | FROM_EXISTING_EVIDENCE | reader F1/F2 mở “Reference case · China”, “Three questions …” (F2 đọc được); proof không phát outcome mới |
| Reader → contact-vn notice / quay lại | FROM_EXISTING_EVIDENCE | 29/10 CTA tới `www.digiwin.com.vn/contact-vn/` và return về đúng reader theo treatment; một lần capture F1 390px có cờ `hasWarning:true` chưa rõ nghĩa (lần chụp thứ hai không có) — cần mở lại khi dựng native |

## Defect / finding list

| ID | Mức | Finding | Đề xuất bounded (không tự sửa) |
|---|---|---|---|
| CQ-1 | thấp | F2-A5 footer dày, dòng sát | Chấp nhận như hiện tại, hoặc nếu muốn sửa cần regen riêng một card với mandate; không sửa lúc này |
| CQ-2 | thông tin | “pill” CTA trong ảnh (F1-A5, F2-A5, proof 4) trông như nút nhưng không bấm được; nút native là “Learn more” | Ghi chú khi dựng native để Bảo biết; không đổi |
| CQ-3 | thông tin | 16 ảnh duy nhất; proof gần như dùng chung F1/F2 | Không báo là 20 ảnh khác nhau; RMK proof không phân biệt F1/F2 |
| CQ-4 | thông tin | Reader chưa quan sát lại; mobile B13 trước đây chưa đủ | Làm native preview và reader mobile khi có mandate dựng draft; tạm nhận evidence 29/10 |
| CQ-5 | thông tin | Chữ nguồn Taiwan trong F1-A5/F2-A5 | Giữ; không mở rộng thành năng lực MES ở Việt Nam |

Bright Power China/challenges giữ đúng scope; không KPI hay outcome module mới. Không phát hiện lỗi chặn trong phạm vi đọc được; dispositions ở trên chỉ chứng minh review nội bộ.

Docs impact reviewed: no canonical update required.
