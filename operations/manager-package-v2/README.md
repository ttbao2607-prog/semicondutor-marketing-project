> **PO steering applied — Phase1 revision1.1:** Đã chốt ngân sách chưa thuế/dashboard owner và tuần1→review→tuần2 data matrix. Thuế không còn input phải chờ trong package; asset/audience swaps thuộc Bảo. [Decision](phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md), [matrix nội bộ](phase1/Week1_Review_Week2_Data_Matrix.md). Các output mới vẫn working files local; Phase2/3 chưa bắt đầu.

# Package v2 · worktree riêng

Mandate Bảo: “Tách 1 worktree, rà các đầu việc cần làm cho package ver2, chưa lên plan vì Bảo sẽ thay đổi khá nhiều so với package ver1, chỉ list, lập danh sách các việc sẽ ghi vào package, commit đầu cho worktree đó.”

- Worktree: `D:/LinkedIn_Package_V2_2026-10-07`.
- Branch: `slice/linkedin-package-v2-inventory`.
- Main baseline: `196f26b9f3064fca8fe6b3b50b5707c2b54b65af`.
- Đầu ra hiện tại: [Danh sách nội dung/đầu việc](Package_V2_Content_Inventory_2026-10-07.md) và [nguồn đã rà](source-inventory.json).
- Trạng thái: **PHASE1_PREPARED / BAO_DATA_LOCK_PENDING**. Inventory checkpoint `5738a1c`; [workflow anchor](Package_V2_Workflow_Anchor_2026-10-07.md) checkpoint `823cc8b`; [plan 3 phase](Package_V2_Three_Phase_Plan_2026-10-07.md) checkpoint `7796bc6`. Theo mandate mới, [Phase 1](phase1/README.md) đã có source/data/asset/claim/reader registers, disposition 34 mục và skeleton để Bảo chốt. Phase 2–3 chưa bắt đầu. Files Phase 1 và cập nhật docs là working files local, chưa checkpoint mới/main merge/push.

Danh sách dùng để Bảo giữ/bỏ/đổi/bổ sung nội dung. ID inventory phục vụ tham chiếu; Phase 1 đã gán disposition nhưng chưa thực hiện content split Phase 2. Mục tiêu khoảng 3–4 câu duyệt đã chốt ở anchor; câu hỏi cụ thể, sitemap, format, timeline, campaign allocation hoặc ngưỡng KPI mới chưa được chọn. Công thức budget và metric từ nguồn đã đối chiếu nội bộ; chưa dựng workbook v2. Không sao chép package/ZIP/artifact cũ sang namespace v2.

“Package v1” là tên phiên bản Bảo dùng trong mandate. Source lịch sử có nhãn internal candidate v6 ở `deliverables/manager-package/2026-10-05`; đó là các revision của package cũ, không gọi nhầm thành package v2 mới.

Phạm vi writer Phase 1: `operations/manager-package-v2/` và bounded current-state/progress notices trong checkout riêng để đáp ứng documentation gate. Output trình sếp sau này dự kiến `deliverables/manager-package-v2/`; Phase 1 là Markdown/registers nội bộ. Main và source worktrees khác chỉ đọc; không merge main/push/live trong mandate này. Frozen harness/anchor/process, adapter DEVELOPING/NOT_FROZEN và artifact receipts giữ nguyên.

Docs impact reviewed: CURRENT_STATE.md, DOCS_IMPACT_MAP.md, current progress/kickoff/budget/S01/S04/build/readiness/tracking và nguồn package. Phase 1 bổ sung current-state/progress notices trong worktree này về package và source advancements; không đổi quyết định business, main adoption hoặc runtime. Xem [reconciliation notes](phase1/Reconciliation_Notes.md). Historical inventory/source-inventory.json giữ snapshot ban đầu; source-register Phase 1 là input hiện tại.
