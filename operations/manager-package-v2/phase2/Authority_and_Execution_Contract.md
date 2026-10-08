# Phase 2 — mandate và execution contract

Ngày 07/10/2026. Nguồn mới nhất của Bảo: **“commit checkpoint, làm phase 2 codex.”**

Phase 1 đã checkpoint trên nhánh `slice/linkedin-package-v2-inventory` tại **4030d40d727668918bf079fd730d2071268a9004**. Commit này tồn tại local, chưa vào main/GitHub. Bảo cho phép dùng baseline này để làm Phase 2 sau khi đã steering ngân sách/dashboard và review tuần; record này không nhận PO acceptance mới cho từng asset, live readiness hoặc thay scope receipt Phase 1.

## Kết quả và phạm vi

Tạo một bản executive có **3 câu hỏi đầu tư** từ baseline Phase 1: tổng ngân sách, cơ cấu chi/phần giữ lại, cách đánh giá đầu tư. Tách lựa chọn vận hành của Bảo và metadata agent/operator ra hồ sơ riêng; business rationale cần thiết vẫn đủ để sếp quyết định. Bản executive độc lập, không chứa internal notes trong file đi kèm, hidden data, metadata, DOM hay export.

Writer/reviewer: `/root`, thực hiện bounded draft/documentation theo mandate trực tiếp. Không spawn. Phase 3 polish, HTML/workbook/demo/export final chưa được kích hoạt. Main/source worktrees khác chỉ đọc. Các file Phase 1 tại checkpoint được giữ nguyên; budget, account, assets, harness/anchor/process và adapter không có mutation mới.

## Thực hiện và kiểm kết quả

1. Lưu checkpoint Phase 1 đã qua 82 bounded checks; đối chiếu staged message hashes trước commit.
2. Rà S1–S10, 40 data rows và 34 inventory items; phân loại executive, business rationale hoặc internal-only/drop-default.
3. Dựng bản executive Markdown trong namespace riêng; giữ 3 câu, đề xuất/căn cứ/phản hồi rõ; không kế thừa câu trả lời/engine v1.
4. Đọc actual content để review semantic/message anchor; kiểm số liệu, phân quyền, content split, namespace và hash/source mapping.
5. Sync current-state/progress và owned plan/README; handoff Bảo chốt split trước Phase 3.

Critical criteria: 40/40 data và 34/34 inventory được routing; đủ budget + logic + measurement; cap 11,7 triệu chưa thuế và held 6,1 nằm trong tổng; cadence/swap là quyền Bảo; exactly 3 investment questions với proposal và response choices; không technical approval, local/integrity claims hoặc old answers trong deliverable/payload; fresh MSG-ANCHOR-01 và canonical state đúng phạm vi.

Audit target: actual executive file, content/data split, source mapping về commit Phase 1, decision/action register của Bảo và bindings/verification. Structural/hash checks chỉ xác minh topology/provenance; semantic review đọc nội dung thực. Reviewer hiện tại là **SELF_REVIEW**, không độc lập; không tự ghi AUDIT_PASS độc lập. Evidence/render: Markdown nội bộ, N/A artwork/UI.

Terminal execution status ghi trong [review](Review_Receipt.md); user review state là **PHASE2_PREPARED / BAO_SPLIT_REVIEW_PENDING** khi các criteria đạt. Không tự chốt Phase 3 hoặc budget acceptance của sếp.
