# P7 — Output readback, Matched Audiences — 20/10/2026

Executor/Auditor: Claude solo, **AUDIT_MODE=SELF**. Mandate của Bảo trong chat: dùng Chrome đã mở sẵn, đọc Matched Audiences và ghi nhận. Read-only: không Edit, không upload, không tạo/xóa audience, không gắn ad set. Account Campaign Manager của Digiwin (Active). Tab Chrome đã đóng.

**Execution PASS (đọc xong 3 audience) · Discovery vẫn CHANGES_REQUIRED · R5 mapping được khôi phục · Audit INSUFFICIENT_EVIDENCE (self-review).**

| Audience | Status | Members (list) | Matched | Unmatched | Last modified |
|---|---|---|---|---|---|
| TEST-AUD-COMPANY-LIST-DISCOVERY-202610 | Ready | 789,768 | 135 | 93 | 12/10/2026 |
| TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52 | Ready | 445,884 | 52 | 0 | 8/10/2026 |
| TEST-AUD-CONTINGENCY-MASTER-203-20261006 | Ready | 1,354,750 | 178 | 13 | 6/10/2026 |
| VN_ERP_Partners_List_01 | Ready | 1,017,596 | không đọc Details | — | 24/2/2026 |

## Observed

- **R5:** trước đây (8/10) Details là 0/0/0; nay 52 matched, 0 unmatched. Khớp 52 dòng nguồn. Mapping recovery có bằng chứng, không cần LinkedIn Support cho R5.
- **Discovery:** Ready (hết Updating). Sau upload v3 (310 dòng, 12/10), Matched 135 + Unmatched 93 = 228, không bằng 310 (chưa giải thích; có thể LinkedIn gộp/loại dòng trùng hoặc dòng không đọc được). Trước upload đọc 199 matched, nay 135.
- **Chất lượng khớp Discovery (trang 1 của 3, 50 dòng đầu):** nhiều dòng tên input khác hẳn công ty LinkedIn được khớp (ví dụ input là công ty điện tử/pháp nhân khác nhưng Page khớp là tập đoàn thực phẩm, xây dựng, bán lẻ, kế toán). Đây là quan sát trực tiếp từ cột input vs matched; chưa đếm đủ 135 dòng nên không có tỷ lệ chính thức.
- Tên công ty và danh sách dòng không đưa vào Git; evidence chi tiết ở kho private nếu cần.

## Kết luận goal

Goal "matched audience dùng được" **chưa đạt cho Discovery**: số khớp thấp hơn nguồn và còn nhiều cặp sai rõ ràng. R5 đạt mức mapping. MASTER-203 có 13 unmatched, chưa đánh giá chất lượng.

## Addendum — đọc đủ Discovery (3 trang Matched + 2 trang Unmatched)

**Matched 135 (tất cả Date added 12/10):** so tên input với Page được khớp, tôi phân loại thủ công theo tên (self-audit, sai số vài dòng):

| Trang | Dòng | Khớp sai rõ ràng |
|---|---|---|
| 1 | 50 | 12 (+1 chưa xác minh được) |
| 2 | 50 | 25 |
| 3 | 35 | 10 |
| **Cộng** | **135** | **≈47 (~35%)** |

"Sai rõ ràng" = tên pháp nhân input và công ty của Page là hai đơn vị khác nhau (không phải bản dịch/tên VN của cùng công ty). Chưa tính các dòng input VN khớp vào Page tập đoàn/global (coi là parent match). Con số 47 lớn hơn "15 mismatch tên chưa xác minh" mà receipt 12/10 ghi cho v3; chưa đối chiếu được với CSV private nên chưa giải thích.

**Unmatched 93 theo Date added:** 9/30 = 78, 10/6 = 6, 10/8 = 2, 10/12 = 7. Tức **chỉ 7 dòng unmatched thuộc lần upload 12/10**; 85 dòng còn lại là tồn dư từ các lần upload trước (9/30, 10/6, 10/8) mà LinkedIn không xóa khi Edit audience. Ví dụ cùng một tên input nằm ở Unmatched (9/30) và Matched (12/10) với Page khác.

**Hệ quả:** 135 + 7 = 142 dòng có dấu 12/10 so với 310 dòng v3; 168 dòng chưa giải thích được (LinkedIn có thể gộp trùng hoặc bỏ dòng không đọc được; chưa có bằng chứng). Unmatched 93 không phải số đo của file v3.

## Kết luận goal (cập nhật)

Discovery **CHANGES_REQUIRED** (xác nhận): ≈35% dòng matched là Page sai đơn vị; nếu chạy ads với audience này sẽ nhắm sai công ty. R5 đạt mapping. MASTER-203 chưa đánh giá chất lượng.

## Repair cycle 3 — v4 upload (20/10/2026)

Mandate của Bảo trong chat: chọn hướng v4 và "Tạo audience mới"; Agree and upload bấm đúng một lần.

- **v4 = 263 dòng** = v3 (310) trừ 47 dòng input có Page khớp sai (danh sách từ readback 20/10, cả 47 tên đều tìm thấy trong v3). Cùng 10 cột, sha256 `5c0c5d9ce9580d0c60c0787403395f544a73087cf3e6bfb6a0ccee31cf65cccc`, 17.859 byte. CSV và changelog ở kho private, không vào Git.
- **Upload:** tạo audience mới **TEST-AUD-COMPANY-LIST-DISCOVERY-202610-V4** (Company list). Preflight "Processing complete"; toast "Your audience has been successfully created."; danh sách hiện Ready, 782,059 members, 10/20/2026. Audience Discovery cũ, R5, MASTER-203, VN_ERP không bị sửa.
- **Readback ngay sau upload:** Details = Matched 0 / Unmatched 0 ("No records to show"). Giống R5 sau upload 8/10; chưa phải kết quả mapping. Dialog vẫn ghi "10,000–300,000 companies" nhưng nhận file 263 dòng.
- **Status: Execution PARTIAL (upload xong), P7 cho v4 NOT_DONE, Audit INSUFFICIENT_EVIDENCE.** Việc cần làm: đọc lại Details sau khi LinkedIn xử lý (checkpoint đề xuất ≥ 21/10 sau giờ upload; có thể tới 48h) rồi so matched/unmatched với 263 dòng và rà khớp sai. Không upload lặp.
- Giới hạn: danh sách 47 dòng là phân loại thủ công theo tên; dòng có tên "gần giống" vẫn có thể khớp sai. Chưa kiểm tra audience v4 có kế thừa tồn dư nào hay không (audience mới nên không dự kiến).

## Unknown / chưa làm

Tỷ lệ chính xác (cần đối chiếu CSV private); lý do 310 → 142; chi tiết MASTER-203 và VN_ERP; tab Saved; so với roster 199 cặp P1.

Docs impact reviewed: chưa cập nhật notice audience hiện hành ở entrypoint (CURRENT_STATE/README); cần bước sync riêng nếu Bảo duyệt. Receipt này chưa commit/merge/push.
