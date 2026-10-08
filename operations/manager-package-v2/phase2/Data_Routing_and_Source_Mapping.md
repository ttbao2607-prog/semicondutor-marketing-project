# Phase 2 — data routing và nguồn bản executive

Baseline chỉ đọc: Phase 1 revision 1.2 tại `4030d40d727668918bf079fd730d2071268a9004`. Bản executive là đề xuất, không actual spend/performance hoặc approval mới. Khung 5,6 + tối đa 5,6 + tối đa 0,5 được đưa thành phương án Bảo đề xuất để duyệt, không đổi `ASSUMPTION` của source thành fact đã chọn/đã chi.

## Executive blocks

| ID | Surface trong executive | Data / claim dùng | Transform giữ đúng scope |
|---|---|---|---|
| E01 | Opening/mục tiêu | D01, D03, D08, D34 | Đề xuất tiếp cận/quan tâm/đi tiếp, không hứa leads/ROI |
| E02 | Hướng tiếp cận | D03–D06; C07 | VN chuẩn bị năng lực; FDI operating value; không blanket customer fit |
| E03 | LinkedIn journey | D02, D05, D06; C07 | Single image → chính ads mới → carousel khi eligible → case; không guaranteed order |
| E04 | Budget table và tax | D08–D12, D15 | Cap11,7 chưa thuế, held6,1 nằm trong tổng; toàn bộ là proposal/current cap |
| E05 | Vận hành/review | D25, D26, D34, D36; C07 | Week1/review/week2; đúng đoạn, giữ persona/message, không claim toàn bộ source-ready |
| E06 | Quy mô/tín hiệu | D16, D20, D23, D35, D36 | Material uncertainty thành hệ quả/cách xử lý; không đưa unsaved metrics thành forecast |
| E07 | Measurement | D31, D33–D36 | Source tương ứng, cùng kỳ; đề xuất layered measurement, verified leads bổ sung |
| E08 | Câu 1 | D08, D15 | Mức chi/tax basis, proposal/unanswered |
| E09 | Câu 2 | D09–D12, D36 | Cơ cấu chi/held, không thêm ngân sách tuần2 hoặc permission từng swap |
| E10 | Câu 3 | D34–D36 | Business evaluation; numeric thresholds/technical setup thuộc Bảo |

## Routing đủ 40 data rows

| Data ID | Disposition | Nơi dùng / giữ |
|---|---|---|
| D01 | EXECUTIVE_BRIEF | E01; BA-16; không hỏi quyền Bảo |
| D02 | EXECUTIVE | E03; BA-08 |
| D03 | EXECUTIVE | E01/E02; BA-01 |
| D04 | EXECUTIVE_BRIEF | E02; detailed locales/pools ở BA-01 |
| D05 | EXECUTIVE | E02/E03; C07 |
| D06 | EXECUTIVE | E02/E03; C07 |
| D07 | INTERNAL | BA-10; Claim register |
| D08 | EXECUTIVE | E01/E04/E08; BA-04 |
| D09 | EXECUTIVE_PROPOSAL | E04/E09; giữ assumption nguồn |
| D10 | EXECUTIVE_PROPOSAL | E04/E09; giữ assumption nguồn |
| D11 | EXECUTIVE_PROPOSAL | E04/E09; BA-12 |
| D12 | EXECUTIVE | E04/E09; held trong cap |
| D13 | INTERNAL | BA-04; reference daily |
| D14 | INTERNAL | BA-04; reference 14 ngày |
| D15 | EXECUTIVE | E04/E08; BA-05 |
| D16 | MATERIAL_BRIEF | E06; actuals/baselines ở BA-11 |
| D17 | INTERNAL | BA-02; nghiên cứu424 |
| D18 | INTERNAL | BA-02; integrity rows/fields |
| D19 | INTERNAL | BA-02; dated processing observation |
| D20 | MATERIAL_BRIEF | E06; exact mapping/readback ở BA-02 |
| D21 | INTERNAL | BA-03; backup203/52 |
| D22 | INTERNAL | BA-03; Ready/Details contradiction |
| D23 | MATERIAL_BRIEF | E06; exact unsaved estimates ở BA-03 |
| D24 | INTERNAL | BA-02/BA-03; proposed readback |
| D25 | EXECUTIVE_BRIEF | E05; revisions/readers ở BA-07/BA-09 |
| D26 | EXECUTIVE_BRIEF | E05; OSAT counts/limits ở BA-15 |
| D27 | INTERNAL | BA-15; Fabless source/review |
| D28 | INTERNAL | BA-15; Partner source/review |
| D29 | INTERNAL | BA-15; lane queues/intake |
| D30 | INTERNAL | BA-09; reader source/main |
| D31 | EXECUTIVE_BRIEF | E07; tracking/source scope ở BA-09/BA-11 |
| D32 | INTERNAL | BA-15; frozen vs developing |
| D33 | EXECUTIVE_BRIEF | E07; Search optional/relevance, Planner ở BA-12 |
| D34 | EXECUTIVE_PROPOSAL | E01/E05/E07/E10; BA-11 |
| D35 | MATERIAL_BRIEF | E06/E07/E10; exact settings/targets ở BA-08/BA-11 |
| D36 | EXECUTIVE | E05/E06/E09/E10; BA-06/BA-07/BA-13 |
| D37 | INTERNAL | BA-14; workbook/source calculations |
| D38 | INTERNAL | BA-16; formats/history/old engine |
| D39 | INTERNAL | BA-01/BA-02/BA-03; execution configuration |
| D40 | INTERNAL | Authority/phase status; BA-16 |

Data source IDs/SHA256 và loại fact/decision/assumption/pending giữ nguyên [Phase 1 data](../phase1/Data_Register.md), [source pins](../phase1/source-register.json) và [claims](../phase1/Claim_Register.md). Dữ kiện của source worktrees là snapshot tại capture, không readback mới. Asset/reader intake final sẽ recheck revision ở Phase 3; lượt này không copy ảnh/HTML/workbook vào deliverable.
