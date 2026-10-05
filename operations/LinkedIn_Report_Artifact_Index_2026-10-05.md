# LinkedIn — danh mục artifact cho report · 2026-10-05

## Current PO direction

Phase 1 gần như cold traffic: **Brand awareness + Carousel image**. Sau đó RMK theo exact new-ad/campaign source, interaction lookback được chọn và objective Engagement hoặc click LDP. Đây là concept đã được Bảo ghi nhận; native Carousel engagement-source eligibility và exact window/objective vẫn cần verify khi chuẩn bị Phase 2. Không lấy existing Digiwin Page audience. Không cần warm pool có sẵn trước cold launch. Document cold alternative không được chọn.

## Sources có thể trích xuất

| Phần report | Artifact canonical | Scope / limitation |
|---|---|---|
| Tiến độ tổng | [CURRENT_STATE](../CURRENT_STATE.md) | Dated latest notes supersede historical snapshots only in stated scope |
| Cold creative | [Corrective rollout result](LinkedIn_Corrective_Scenarios_Rollout_Result_2026-10-04.md) + [root final audit](linkedin-imagegen-dogfood/corrective-rollout-2026-10-04/operator/final-audit.json) | 11 treatments / 55 selected cards; offline creative acceptance. Lấy selected sets/export manifest, tránh historical FAIL/reserve |
| Cold selected queue | [Queue ledger](linkedin-imagegen-dogfood/corrective-rollout-2026-10-04/operator/queue-ledger.json) | Chỉ dùng current selection; delivery/buyer acceptance không được suy từ creative audit |
| RMK Quality/case06 R4 | [R4 overview/export location](linkedin-rmk-proof/quality-pilot-harness-r4/README.md) + [PO freeze](linkedin-rmk-proof/quality-pilot-harness-r4/operator/bao-freeze-receipt.json) | 4-card accepted/frozen candidate; dùng export pinned theo manifest, không R2/R3 failed history |
| RMK Bright/Pressway/Phẩm Thuyên + HTML | [Final evaluation](linkedin-rmk-production-coordination/carousel-html-final-evaluation.md) + [postcommit receipt](linkedin-rmk-production-coordination/carousel-html-postcommit-receipt.json) | Three offline four-card sets; HTML case06/Pressway v2 freeze scoped. Bright/Phẩm Thuyên expanded HTML chưa có; host/pair/tracking/live còn pending |
| Company List Ready | [Ready update/task register](LinkedIn_Company_List_Ready_Update_2026-10-05.md) + [live research receipt](LinkedIn_Audience_Ready_Research_2026-10-05.md) | Ready/80%/753,731 displayed members; role filters 4,800+ → leadership 780; identity/ICP chưa accepted |
| Mapping findings | [Decision evidence](LinkedIn_Audience_Decision_Evidence_2026-10-05.md) | 117-row name triage 34/8/75, không phải verified false-match ratio. Page inventory chỉ historical research phụ, không planned RMK source |
| Carousel objectives / campaign sequence | [Cold→RMK evidence/data plan](LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md) | Awareness và Engagement có Carousel; thêm 3 objectives theo official guidance. Native engagement source là capability khác |
| Source/rule/data/budget | [S03](../drafts/S03_LinkedIn_Audience_Research.md), [S04](../drafts/S04_Measurement_and_Budget.md), [Build pack](../ads/linkedin/LinkedIn_Build_Pack.md) | Templates chưa có real-delivery data; chưa đổi allocation/budget/enable/spend |

## Private local evidence cho Bảo

Private root: `D:/LinkedIn_Audience_Research_Evidence_2026-10-05` — không nằm trong public Git repo.

- Round1: 14 JPEG, `REPORT.md`, `manifest.json`; Ready/details, reach/language/source menu, saved audience và mapping examples.
- `round2`: 10 JPEG, 117-row mapping JSON/CSV, Page/Website editor snapshots và hash manifest.
- `round3`: 10 agent JPEG + 1 PO PNG, Carousel Engagement selected proof **34**, PO Awareness screenshot **35**, full-source review worksheet **424 rows**, source-quality summary, source registry/daily measurement/RMK gate CSV templates và hash manifest.

Tổng **35 screenshot files**; không đếm cùng ảnh PO gốc clipboard lần nữa. Source worksheet chưa upload-ready; collection templates header-only, không có invented delivery rows. Raw account/company names/private URLs có trong private evidence: Bảo chọn ảnh/columns phù hợp khi trích xuất report. Không đưa toàn bộ private folder vào public repo.

## Integration / audit scope

User-authorized local checkpoint và merge vào local main của worktree hiện tại, gồm prior consolidated Cold/RMK history + audience research. Research đã nằm trên branch/worktree, không cần một merge nội bộ bổ sung. Main target là `D:/Digiwin_Semiconducter_Workspace`; merge disposition/actual SHA được verify sau operation và ghi trong private closeout. Không push GitHub hoặc live ad action.

Main có Fabless changes chưa commit từ phiên khác, gồm shared status docs. Full original files/hash snapshot + named Git stash giữ khả năng recovery; sau merge chỉ reapply Fabless delta, không overwrite newer LinkedIn docs bằng old Ready snapshot. Các file Fabless đó vẫn uncommitted, không bị ghi nhận như new LinkedIn work.

Docs impact reviewed: CURRENT_STATE, README, Build Pack, Pre_Ad_Readiness, S03/S04 và Cold→RMK data plan được đồng bộ. Creative/HTML/tracking/proof artifacts không sửa. Report-index links và evidence counts được check; merge acceptance là branch commit reachable from main, tracked research/artifact files present, Fabless-only delta preserved và no remote push. Không dùng Git integration để grant campaign PASS.
