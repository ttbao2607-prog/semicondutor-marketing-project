> **Research live UI · 2026-10-05:** Exact Company List Ready/80%; Details và refreshed list có **753,731 members**, 117 Companies, tab Unmatched 86. VN + English profile + Engineering/Operations/IT/QA = **4,800+**; thêm Manager/Director/VP/CXO = **780** ở saved definition `RSCH-CL-VN-LEAD-20261005` (persistence verified). Cùng filters + Vietnamese profile báo too small. Size gate discovery đã xác minh; mapping quality/denominator và production decisions vẫn OPEN. Retargeting menu không có Carousel riêng; warm RMK chưa đủ evidence. Chỉ lưu Saved Audience; Exit without saving ad set, không publish/enable/spend. [Receipt](LinkedIn_Audience_Ready_Research_2026-10-05.md). Snapshot cropped-size phía dưới là lịch sử trước research.

# LinkedIn Company List — Ready và task phụ thuộc · 2026-10-05

## Evidence và quyết định PO

Bảo cung cấp Image #1 trong phiên ngày 2026-10-05 và xác nhận “tệp Matched Audience của Linkedin duyệt rồi”. Ghi nhận PO xác nhận trạng thái Ready của đúng tệp; không suy rộng thành quyết định campaign, budget, production attachment hoặc launch.

- Audience: `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`.
- Status: **Ready**; Match rate: **80%**; Source: **Company List**; Ownership: **Owned**.
- Active ad sets hiển thị `-`; không có bằng chứng gắn vào ad set trong ảnh.
- Cột số lượng bên phải bị cắt, chỉ thấy một phần giá trị và header; **exact audience count / reachable members chưa xác minh**.
- 424 dòng upload là dữ liệu lịch sử ngày 2026-09-30, không phải số công ty khớp hay số thành viên. Không tính matched companies từ tỷ lệ hiển thị đã làm tròn.
- Nguồn: ảnh do PO cung cấp; không mở browser/account hoặc refresh trong lần cập nhật này. Ngày nhận evidence là 2026-10-05; thời điểm chụp ảnh không hiển thị.
- SHA-256 ảnh: `53552bc7f68c4becb6e5647458845d4bb3e2fabbe8662f0767a7aae1575f45ed`. Raw screenshot giữ ngoài public repository; chỉ lưu ghi nhận đã sanitize.

## Khoanh vùng task trước đây chờ Ready

| Task / tài liệu nguồn | Kết quả sau evidence Ready | Điều kiện còn lại |
|---|---|---|
| Discovery bước 6: chờ Building xử lý, kiểm tra lại sau 24 giờ — CODEX_LINKEDIN_AUDIENCE_HANDOVER_PLAN / DISCOVERY_RECEIPT | **DONE cho status + match rate**; không còn chờ xử lý cho đúng tệp này | Đọc đầy đủ audience count / reachable members; chưa kết luận toàn bộ discovery viable |
| Phân loại AUD_STATUS_READY_VIABLE hoặc READY_SUB_THRESHOLD — handover mục 3 | **Chờ bằng chứng size**, không còn PROCESSING_LATENCY hiện tại | Enum có 5 mã nhưng không bao phủ Ready + cropped size; không gán bừa viable hay sub-threshold, không sửa các tiêu chí |
| S03 Phase 2 / Build Pack § Company List: đánh giá company-list targeting | **Gỡ dependency Building**; có thể tiếp tục chuẩn bị đánh giá offline với Ready/80% | Exact size sau geography + role filters, entity mapping và production targeting decision vẫn pending |
| Pre_Ad_Readiness B/D: chuẩn bị audience và account draft | **Gỡ dependency chờ Ready của discovery list**, chưa closeout toàn task | Account/permission, final targeting, draft-build mandate và launch gates vẫn riêng; không tự attach/create/enable |
| Đề xuất LI-CMP-FDI-SEGMENT / LI-CMP-DOMESTIC-SEGMENT — executive reporting / partial closeout | **Bổ sung evidence Company List Ready**, không còn dùng Building của tệp này làm lý do chờ | Chưa chứng minh split FDI/domestic, filtered reach, budget/allocation hoặc kiến trúc đã duyệt |
| RMK LI-AUD-P1-ENGAGED-30D và carousel→RMK source | **Không được gỡ bằng evidence này** | Company List khác engagement audience; source eligibility, reachable >=300 và actual account witness vẫn pending |
| RMK HTML expand / proof / ad→adapter / host / tracking | **Không phụ thuộc việc Company List còn Building** | Giữ nguyên queue, proof holds, O3 binding, HTML Bright/Phẩm Thuyên, route/pair/tracking/live gates |

## Canonical synchronization và phạm vi lưu

Cập nhật theo mandate trực tiếp của Bảo tại worktree RMK và working-tree files của local main; không chép đè toàn bộ tài liệu giữa hai nhánh vì main chưa chứa toàn bộ Cold/RMK mới. Các thay đổi main có sẵn được giữ nguyên. Không commit, merge, push hoặc account action trong lần cập nhật này. Nội dung mới tồn tại trong working tree; chưa tới GitHub.

Docs impact reviewed: CURRENT_STATE, README, Build Pack, Pre_Ad_Readiness, S03, discovery plan/receipt được cập nhật. S02, S04, proof/governance, creative runbook và tracking không cần đổi: không có keyword, budget, creative/proof, workflow hay tracking decision mới.
