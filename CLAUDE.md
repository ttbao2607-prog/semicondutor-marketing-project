# CLAUDE.md

@AGENTS.md

`AGENTS.md` là nguồn chỉ dẫn vận hành chính của workspace này (vai trò, Phase A/trust boundary, quy tắc public Git, documentation sync gate). Đọc và tuân thủ nó trước mọi việc; file này chỉ là điểm vào cho Claude Code và không thay thế hoặc override AGENTS.md.

## Bản chất workspace

Workspace marketing paid (LinkedIn + Google Search) cho Digiwin Vietnam trong ngành bán dẫn, không phải code project. Product Owner là Bảo. Phần lớn nội dung là tài liệu Markdown/HTML và ảnh PNG; `scripts/` và `tests/` chỉ có vài kiểm tra nhỏ (tracking, RSA, ImageGen preflight, locale adapter).

## Đọc gì trước khi làm việc

1. `CURRENT_STATE.md` (rất dài, banner mới nhất ở đầu file; các banner bên dưới là snapshot lịch sử theo ngày) và `DOCS_IMPACT_MAP.md`.
2. Thứ tự nguồn theo AGENTS.md: chỉ đạo mới của Bảo > `Semiconductor_Work_Kickoff.md` > `Semiconductor - Website & Ads.md` > AGENTS.md.
3. Với artifact VN/FDI: `operations/Vy_Email_Content_Anchor.md` (gate MSG-ANCHOR-01).

## Bản đồ thư mục

- `deliverables/manager-package-v2/2026-10-07/` — gói giao Vy (mở `BAT_DAU.html`; mail ở `01_De_xuat/Mail_gui_Vy.md`; theo dõi ở `04_Theo_doi/*.xlsx`; Google Search ở `06_Google/`). Giữ nguyên cấu trúc thư mục vì đường dẫn tương đối.
- `deliverables/linkedin-*` — thư viện creative (batch PNG, viewer/reader) đã chọn vào main.
- `operations/` — plan, receipt, evidence, runbook; thư mục lớn nhất (hàng nghìn file), phần lớn là lịch sử. Không rewrite lịch sử để khớp trạng thái hiện tại.
- `landing/`, `ads/`, `tracking/`, `design-system/` — HTML landing, nội dung ads, tracking contract, design system canonical.

## Lưu ý khi làm việc

- Repository nặng (`.git` ≈ 1,7 GB, ~4.900 file tracked): dùng Grep/Glob có phạm vi, tránh quét toàn repo và tránh đọc cả `CURRENT_STATE.md`/`README.md` (>80 KB mỗi file) khi chỉ cần banner đầu.
- Mọi trạng thái "local / chưa push / NOT_RUN" ở banner cũ là snapshot theo ngày, không phải trạng thái hiện hành.
- Không live action, publish, spend, login hay thu thập PII khi chưa có operational mandate cụ thể (AGENTS.md, Phase A).
- Không tự spawn child agent; worker mặc định theo AGENTS.md chỉ áp dụng khi có mandate spawn.
- Khi PASS/handoff, chạy documentation sync gate: đọc `DOCS_IMPACT_MAP.md`, hoặc ghi rõ **Docs impact reviewed: no canonical update required.**
