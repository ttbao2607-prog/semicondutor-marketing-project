# P4 — Phương án thay cold F1/F2

Revision 1 · 29/10/2026 · INTERNAL_PREPARATION_COMPLETE / BRIEF_ONLY. Authority: Bảo giao P4–P7 (chat 29/10/2026). Chỉ chuẩn bị nội bộ: không generate, adapt, upload asset hay tạo ad; chưa chọn winner, chưa có metric. Root tự review; independent audit NOT_RUN. Anchor: VY-CONTENT-ANCHOR r1.0 (SHA256 trong [REVIEW.json](REVIEW.json)); nhánh FDI · English · Fabless Operations (F1) và Planning (F2).

## Kết luận inventory

**Không có biến thể cold cùng persona/locale/tình huống nào đã tồn tại và qua review để dùng như swap-ready.** Cả hai phương án thay ưu tiên là **BRIEF_ONLY**; không giả có PNG sẵn sàng.

| Phạm vi | Ứng viên đã rà | Disposition | Lý do |
|---|---|---|---|
| F1 cold hiện hành | B13 v5, card `COLD-FABLESS-B13` (sha256 `b89e0ec2…`, 1254×1254, reused byte-identical từ v4) | ĐANG CHẠY | không có phiên bản cold khác cùng hook trong `deliverables/`; thư mục B13 chỉ có v5 |
| F2 cold hiện hành | B16 v2, card `COLD-FABLESS-B16` (sha256 `829bdd6e…`) | ĐANG CHẠY | như trên; `operations/` có B16 v1 nhưng không phải alternate đã chọn |
| F3 / B19 EN “A lot changes partners. What goes with it?” | [B19](../../../../deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B19-en-f3-v1/README.md) | KHÔNG PHẢI hook/visual swap | đổi tình huống (partner-to-partner handoff); review hiện là INSUFFICIENT_EVIDENCE/PARTIAL, mobile chưa đủ; cần scope review riêng ([ASSET_OPTIONS](../ASSET_OPTIONS.md)) |
| B14/B15/B17/B18 (zh-Hans/zh-Hant) | cùng thư mục batch | NGOÀI SCOPE | đổi locale/segment (A3); không phải thử hook |
| OSAT O1–O4, Supplier P1–P3 | [SCREENING](../../../pre-ad-readiness/2026-10-29/library-reselection/SCREENING.csv) | KHÔNG DÙNG | `NOT_A_WHOLE_R5_REPLACEMENT`; P-group fail native eligibility |

## Brief F1 — giữ Operations/partner reports

- **Giữ:** audience/objective/bid/budget/locale (R5 EN, Reach, USD10 shared), persona (chip-design Operations dùng outsourced production), pain (partner report không cùng lot/stage/time/owner), business value (cơ sở chung cho quyết định kế tiếp), caption gốc (145 ký tự), destination `t=F1&lang=en`, giữ Digiwin/manufacturing ERP, không ROI/outcome.
- **Đổi một phần, chọn một trong hai:**
  - **Hook-only:** giữ visual B13; đổi dòng hook từ “Outsourced production. Your next decision.” sang hướng nêu mâu thuẫn báo cáo, ví dụ ý “Same lot. Which partner report is current?”. Câu chữ này là *ý tưởng chưa duyệt*: cần MSG-ANCHOR pre-gen, kiểm giới hạn ký tự native và alt mới.
  - **Visual-only:** giữ nguyên hook/caption; đổi cảnh (hiện: bàn giấy, wafer, thẻ kho) sang cảnh dòng thời gian/mốc báo cáo theo lot. Không thêm KPI hay logo mới.
- **Không đổi:** nếu đổi cả hook và visual cùng lúc thì không đọc được nguyên nhân; chỉ một.
- **Rollback:** card gốc B13 v5 (hash ở trên), ad gốc `LI-wave01-F1-en-COLD-v1` giữ nguyên Off thay vì xóa.

## Brief F2 — giữ Planning/affected lots

- **Giữ:** như F1; persona Planning/Operations; pain “demand đổi → lot/báo cáo partner nào cần xem trước khi replan”; destination `t=F2&lang=en`; caption gốc (206 ký tự).
- **Đổi một phần:**
  - **Hook-only:** từ “Demand changed. Which lots need a review?” sang hướng nhắc tới kế hoạch trước, ví dụ ý “The plan changed. Which partner reports still apply?”. Chưa duyệt; cần gate.
  - **Visual-only:** giữ hook; đổi cảnh sang kỳ kế hoạch/lịch kèm lot.
- **Rollback:** B16 v2 card gốc và ad `LI-wave01-F2-en-COLD-v1`.

## Điểm cần QA trước khi dùng bất kỳ phương án nào

1. MSG-ANCHOR-01: PREGEN_SCRIPT rồi hậu kiểm artifact thật; khi chưa có anchor PASS thì chưa được SCRIPT_REVIEW_PASS hay generation.
2. Giới hạn ký tự native headline/intro, alt “Illustration: …”, ảnh vuông 1254 PNG, không crop/edit; hash mới ghi vào receipt.
3. `utm_content` mới (ví dụ `f1_cold_v2`/`f2_cold_v2`) để tách đọc số; không đổi `utm_campaign` giữa kỳ nếu muốn so equal windows.
4. Phân biệt rõ: hook/visual swap cùng persona (C4) ≠ F3 đổi tình huống.
5. Generation/adaptation/upload là việc riêng sau quyết định của Bảo; không có mandate trong lượt này.

## Gate quyết định (từ SCENARIOS C4)

Chỉ cân nhắc thay khi C1–C3 đủ cơ sở (đúng link/audience/delivery) và có raw clicks/impressions với định nghĩa click đã khóa; criteria UNSET ([CRITERIA_DECISIONS](CRITERIA_DECISIONS.md)). Hai ad dùng chung ngân sách/thuật toán nên không declare loser khi một ad ít phân phối.

Docs impact reviewed: no canonical update required.
