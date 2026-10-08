> **Current — PO approved 08/10/2026:** Bảo duyệt package hiện tại, yêu cầu checkpoint local và kho evidence riêng. [Approval/checkpoint scope](ad-logic-2026-10-08/PO_Approval_2026-10-08.md). **PO_APPROVED_OFFLINE**; package không đổi thêm, không gắn link evidence. Chưa merge main hoặc push. Những notices pending và working-files bên dưới giữ trạng thái trước approval.

> **Current extension — 08/10/2026:** Bảo đã duyệt hướng bổ sung logic quảng cáo; [package hiện tại](../../deliverables/manager-package-v2/2026-10-07/BAT_DAU.html) có [trang logic minh họa](../../deliverables/manager-package-v2/2026-10-07/01_De_xuat/logic_quang_cao.html). **AD_LOGIC_PREPARED / BAO_REVIEW_PENDING**. [Hồ sơ hậu kiểm hiện hành](ad-logic-2026-10-08/README.md) ghi source, PREGEN và actual post-assembly review. Giữ ba câu hỏi, ngân sách và 205 file bảo vệ. Baseline ecf87ad là commit local; bổ sung này là working files local, chưa commit/main/GitHub. Phase 1–3 và main baseline 196f26b bên dưới là lịch sử của lần dựng trước; không phải trạng thái current source. Main đã đối chiếu read-only tại 581f79b, không nhập thêm asset vào gói này.

> **Current — Phase3 prepared, 07/10:** Theo mandate mới của Bảo, [package gửi Vy](../../deliverables/manager-package-v2/2026-10-07/BAT_DAU.html) đã dựng trong thư mục thường, dùng xưng tên Bảo–Vy. **PHASE3_PREPARED / BAO_FINAL_REVIEW_PENDING**; xem [hồ sơ Phase3](phase3/README.md). Phase1 checkpoint4030d40; Phase2/3 được checkpoint local theo mandate “commit local codex”; chưa đưa vào main/GitHub. [Phạm vi checkpoint](Checkpoint_Phase2_Phase3_2026-10-07.md). Phase1/2 records là historical baseline; không suy Vy đã phản hồi hoặc PO final acceptance.

# Package v2 · worktree riêng

Mandate Bảo: “Tách 1 worktree, rà các đầu việc cần làm cho package ver2, chưa lên plan vì Bảo sẽ thay đổi khá nhiều so với package ver1, chỉ list, lập danh sách các việc sẽ ghi vào package, commit đầu cho worktree đó.”

- Worktree: `D:/LinkedIn_Package_V2_2026-10-07`.
- Branch: `slice/linkedin-package-v2-inventory`.
- Main baseline: `196f26b9f3064fca8fe6b3b50b5707c2b54b65af`.
- Đầu ra hiện tại: [Danh sách nội dung/đầu việc](Package_V2_Content_Inventory_2026-10-07.md) và [nguồn đã rà](source-inventory.json).
- Trạng thái: **PHASE3_PREPARED / BAO_FINAL_REVIEW_PENDING**. Inventory5738a1c, workflow823cc8b, plan7796bc6 và Phase1 revision1.2 checkpoint4030d40 là local history. [Phase2](phase2/README.md) giữ split40data/34items/S1–S10 và3câu ở snapshot trước. [Phase3](phase3/README.md) là current delivery/review record; recipient Vy, names in email. Checkpoint local Phase2–3 theo mandate Bảo; chưa main/push/live và không suy phản hồi từ Vy.

Phase 2 đã routing đủ 34 inventory items, S1–S10 và 40 data rows. Bản executive có 3 câu về cap, cơ cấu chi/phần giữ lại và cách đánh giá; phần execution của Bảo, source/QA/local/integrity và old answers nằm ngoài deliverable. Phase3 đã dựng sitemap/demo/library/readers/workbook và polished mail/proposal; records Phase2 giữ nguyên như baseline lịch sử. Ngân sách/dashboard/cadence theo [quyết định Bảo](phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md); asset/audience swaps nằm trong quyền Bảo.

“Package v1” là tên phiên bản Bảo dùng trong mandate. Source lịch sử có nhãn internal candidate v6 ở `deliverables/manager-package/2026-10-05`; đó là các revision của package cũ, không gọi nhầm thành package v2 mới.

Historical writer scope Phase2: `operations/manager-package-v2/phase2/`, executive Markdown riêng tại `deliverables/manager-package-v2/phase2/`, owned plan/README và current-state/progress notices trong checkout package. Phase 1 files/receipts giữ exact checkpoint; main và source worktrees khác chỉ đọc. Frozen harness/anchor/process và adapter DEVELOPING/NOT_FROZEN giữ nguyên.

Docs impact reviewed: CURRENT_STATE.md, DOCS_IMPACT_MAP.md, current progress, budget/S04/build/readiness và nguồn package đã đối chiếu. Cập nhật trạng thái/content split trong checkout riêng, không đổi cap/cadence/message/runtime. [Phase 1 reconciliation](phase1/Reconciliation_Notes.md) và historical inventory/source pins giữ snapshot; [Phase 2 review](phase2/Review_Receipt.md) binding vào commit `4030d40`.
