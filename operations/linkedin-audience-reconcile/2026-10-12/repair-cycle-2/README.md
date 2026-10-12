# Repair cycle 2 — P1–P6 Discovery (Week1) — 12/10/2026

Executor/Auditor: Claude solo, **AUDIT_MODE=SELF** (không phải independent-agent review). Mandate của Bảo trong chat: dùng Chrome đã đăng nhập (đọc), xác minh phía input, chọn v3 310 dòng rồi upload. Scope là **Week1/Discovery**; Week2/R5 không đụng tới.

**Execution PARTIAL · upload thực hiện, P7 chưa làm · Audit INSUFFICIENT_EVIDENCE · Discovery vẫn CHANGES_REQUIRED · PO đã chọn scope v3.**

| Stage | Kết quả |
|---|---|
| P1 — Roster hiện hành | Đọc đủ 199 matched (Discovery, 12/10). 196/199 cặp (input, Page numeric) giống pin 10/10; 3 cặp đổi nhãn input nhưng giữ Page. Tab Unmatched 93 và 66 cặp đã chứng minh chưa đọc lại. |
| P2 — 36 cặp sai | Tìm bằng LinkedIn đã đăng nhập: 4 có Page thay thế ứng viên, 3 chỉ có Page công ty mẹ/global, 29 không có Page đúng đơn vị. |
| P3 — 133 gap | Đọc About của 133 Page, so với input (tên, domain, thành phố): 6 domain bridge khớp, 17 hợp lý chưa chứng minh, 4 đơn vị VN liên quan, 22 Page tập đoàn/HQ ngoài VN, 69 tên khác hẳn, 15 mismatch mạnh. |
| Xác minh phía input | 84 dòng mismatch tra theo tên pháp nhân trong bản sao công khai dữ liệu đăng ký thuế (masothue.com): 62 có pháp nhân độc lập khác công ty của Page, 22 chưa khớp chính xác. Tìm thêm 2 Page đúng (Canon VN, Wintek VN). |
| Candidate | v3 = 310 dòng: 289 giữ byte-identical, 15 giữ mismatch tên chưa xác minh, 6 sửa `linkedincompanypageurl`; loại 32 sai đã chứng minh + 14 mismatch mạnh + 53 pháp nhân khác hẳn. v2a (362) và v2b (293) giữ làm phương án so sánh. |
| P6 — Upload | Một lần, Edit audience hiện có `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`. Preflight "Processing complete"; toast "Your audience has been successfully updated"; sau reload **Updating**, Last modified 12/10/2026, count vẫn hiện số cũ. Saved filename chưa đọc lại (menu khóa khi Updating). |
| P7 — Output audit | **NOT_STARTED.** Cần đọc lại sau khi Ready (≥48h, từ khoảng 14/10 sau giờ upload sáng 12/10). |

Giới hạn: nhãn P3 là self-audit từ so sánh tên/domain/địa điểm. 69 dòng mismatch tên chỉ được loại khi pháp nhân input tồn tại độc lập (bằng chứng gián tiếp, input không có mã số thuế gốc); 15 dòng chưa xác minh được vẫn được giữ. 2 trong 6 Page sửa là Page LinkedIn tự sinh (không do doanh nghiệp quản lý). LinkedIn có khớp đúng Page sau upload hay không chỉ biết sau readback P7. Dialog upload ghi "10,000 - 300,000 companies" nhưng file 310 dòng được nhận, chưa giải thích được. Số member 794.946 hiển thị trước upload không phản ánh chất lượng audience và sẽ đổi sau xử lý.

Hash file private: [SUMMARY.json](SUMMARY.json). Tên công ty, mã số thuế, Page URL và CSV ở kho private, không vào Git. approved409 nguồn không đổi (sha `ca12a1c8…`). R5-52, MASTER-203 và VN_ERP_Partners_List_01 không bị sửa. Không push, không đổi ngân sách/campaign/creative/tracking.

Docs impact reviewed: cập nhật notice audience hiện hành ở 7 entrypoint; thân tài liệu và receipt lịch sử giữ nguyên.
