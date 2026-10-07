# Package v2 · worktree riêng

Mandate Bảo: “Tách 1 worktree, rà các đầu việc cần làm cho package ver2, chưa lên plan vì Bảo sẽ thay đổi khá nhiều so với package ver1, chỉ list, lập danh sách các việc sẽ ghi vào package, commit đầu cho worktree đó.”

- Worktree: `D:/LinkedIn_Package_V2_2026-10-07`.
- Branch: `slice/linkedin-package-v2-inventory`.
- Main baseline: `196f26b9f3064fca8fe6b3b50b5707c2b54b65af`.
- Đầu ra hiện tại: [Danh sách nội dung/đầu việc](Package_V2_Content_Inventory_2026-10-07.md) và [nguồn đã rà](source-inventory.json).
- Trạng thái: **INVENTORY_ONLY / AWAITING_PO_REDESIGN_INPUT**. Commit đầu chỉ checkpoint danh sách; không phải package v2 đã dựng hoặc plan đã duyệt.

Danh sách dùng để Bảo giữ/bỏ/đổi/bổ sung nội dung. ID phục vụ tham chiếu, không thể hiện thứ tự, ưu tiên, phase, dependency hay phân công. Chưa xác định sitemap, số report/câu hỏi, mô hình ra quyết định, công thức, timeline, campaign allocation hoặc tiêu chí số mới. Không sao chép package/ZIP/artifact cũ sang namespace v2.

“Package v1” là tên phiên bản Bảo dùng trong mandate. Source lịch sử có nhãn internal candidate v6 ở `deliverables/manager-package/2026-10-05`; đó là các revision của package cũ, không gọi nhầm thành package v2 mới.

Phạm vi writer hiện tại chỉ `operations/manager-package-v2/`. Main và source worktrees khác chỉ đọc; không merge vào main/push/live trong mandate này. Frozen harness/anchor/process, adapter DEVELOPING/NOT_FROZEN và artifact receipts giữ nguyên.

Docs impact reviewed: CURRENT_STATE.md, DOCS_IMPACT_MAP.md, canonical current-progress/kickoff/build/readiness và source package đã rà. Danh sách chưa thay đổi business decision hoặc trạng thái implementation nào; **Docs impact reviewed: no canonical update required.** Trạng thái worktree nằm ở README này; khi Bảo đổi scope/decision sẽ review lại các canonical liên quan.
