# Google Search — plan bàn giao sau hậu kiểm Codex

Ngày: 02/11/2026. Owner quyết định: Bảo. Planner/auditor của execution Claude: Codex/root; không spawn reviewer. Base main `5f1ffa150e6f93a17d19a783c113d79c0e646929`; execution `d1e5193c`; integration `26b7584a`.

**HANDOFF_ONLY / REMEDIATION_NOT_STARTED.** Bảo yêu cầu commit plan để agent sau làm. Quyền hiện tại: ghi plan và commit local trên nhánh riêng. Không cấp quyền sửa Google Ads, pause/enable, đổi budget/bidding, tạo campaign, publish landing, submit lead, merge hoặc push. Findings là claims cần xác minh lại; không là mutation instructions. Agent sau điều tra chỉ đọc và lấy mandate cho thay đổi live cụ thể nếu chưa được giao.

## Outcome và phạm vi

Campaign `SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261102]_50.000d-ngay_10d_end20261111` trong DIGIWIN SOFTWARE VIETNAM có cơ chế kiểm soát tổng ngân sách được chứng minh so với trần PO ₫500.000, CPC limit khớp quyết định được duyệt và docs mô tả đúng saved live. Không đo thành công bằng upload/Save hoặc docs giống nhau.

Giữ 16 ad group/16 RSA/28 keyword/24 negative/96 sitelink associations, geo/locale/network, end date, tracking/landing và các campaign khác, trừ mandate thay đổi cụ thể của Bảo. Không tự broaden keyword vì low volume, chuyển tiền, đổi goal/conversion, sửa brand route/copy, tạo scheduler/automation hoặc campaign thay thế. Một browser controller; một writer cho bộ docs. Không tự delegate.

## Baseline read-only và hạn chế evidence

Google Ads qua Chrome profile ASEAN ngày 02/11, kết thúc khoảng 14:28 +07; đối chiếu receipt/upload files/canonical docs tại base trên. Đây là ghi nhận phiên audit, không có raw screenshot archive: Chrome capture timeout hai lần, chưa visual certification. Không lưu account ID/private URL/PII. Editor chỉ mở đọc rồi Cancel; không save account; tab audit mới đã đóng.

| Finding | Quan sát / discrepancy | Disposition |
|---|---|---|
| F1 HIGH — cap | Daily budget ₫50.000. Tooltip ghi November không bị tính quá ₫1.450.000. Budget report: monthly spending limit ₫1,45M; forecast ₫0; cost to date ₫0. Dates 02–11/11 lưu đúng. Receipt/S04 nói dates enforce cap ₫500.000. | Chưa chứng minh hard cap ₫500.000. Phân biệt monthly limit, campaign total budget và end date; không kết luận đã chi vượt hoặc chắc chắn sẽ tiêu ₫1,45M. |
| F2 HIGH — CPC | Maximize clicks; checkbox “Set a maximum cost per click bid limit” = 0. CSV đặt25000; build-sheet banner khẳng định ₫25.000. Receipt trung thực hơn: set trong file, chưa re-read. | Saved setting lệch file/docs; đọc lại trước đề xuất áp dụng limit. |
| F3 MEDIUM — eligibility | 28 keyword Enabled; 24 Not eligible / Low search volume, gồm toàn bộ vi và brand. 4 Eligible: phrase `半导体封装测试 MES`, exact `semiconductor test data management`, phrase `PCB manufacturing ERP`, phrase `PCB制造ERP`. | Hạn chế phân phối, không demand=0; inventory/match type khớp execution đã đọc. Không tự broaden. |
| F4 MEDIUM — guidance | Receipt nói “Google Search has no total-spend cap”. Official Google docs hiện có campaign total budget cho Search, new campaign only, không đổi trực tiếp budget type existing campaign. | Sửa guidance lỗi thời sau xác minh current source/account availability; không tự tạo replacement. |
| F5 LOW — nhãn lịch | Receipt ghi05/11 day3,09/11 day7. Nếu02/11=day1 thì day3=04/11,day7=08/11,last=11/11. | Làm rõ inclusive day N hay elapsed N days; không tự thay lịch PO hoặc tạo lịch chạy. |

Các phần khớp: campaign Enabled/Eligible (Learning);16 ad group/16 RSA; Vietnam Presence; đủ vi/en/Chinese simplified/traditional; Search Partners/Display off; AI Max/final URL expansion off; Account-default: No goals added; dates02–11/11. Có24 campaign-level phrase negatives. UI có96 sitelink associations; các mẫu đọc Pending/Under review, không suy cả96 đã approved/serving. Today02/11:0 impressions/0 clicks/₫0; reporting có độ trễ, không đánh giá hiệu quả.

URL sample: brand English editor lưu OSAT `?lang=en`; suffix `utm_source=google&utm_medium=cpc&utm_campaign=vn_semiconductor_search_p1&utm_content=brand_en_rsa_v1&utm_term={keyword}`; tracking template trống/mobile override off. Public OSAT vi/en, Fabless zh-Hans `#bright-power-case`, Supplier zh-Hant `#supply-chain` đúng locale; case anchors tồn tại;7 OSAT vi target IDs tồn tại. Chưa chứng minh toàn16 ad/96 sitelink URL/suffix, gclid hoặc processed attribution.

## Plan agent sau

1. **Resume chỉ đọc:** chạy git-state-recovery; đọc applicable AGENTS, CURRENT_STATE, DOCS_IMPACT_MAP, plan này và receipt gốc; xác định worktree/revision và current mandate. Không lấy worktree khác làm canonical mặc định. Chrome: đọc `C:/Users/ASUS/.codex/tmp/chrome-control-recovery-20261102.md`, bootstrap runtime hiện hành, chọn ASEAN bằng live inventory. Không login/config repair khi không cần.
2. **Readback exact target:** timestamp/timezone, status, cost từ start đến hiện tại, actual budget type/limit/report, daily budget, end date, CPC checkbox/value. So F1/F2; nếu khác baseline ghi discrepancy trước mutation. Không pause/enable để thử.
3. **Budget decision pack:** kiểm official guidance và actual account controls. Trình lựa chọn cụ thể giữ tổng cap₫500.000, tính cả cost đã có/phần còn lại; nêu latency/limitations của guard. Không gọi manual monitoring/dates là guaranteed hard cap. New campaign là material scope cần Bảo quyết định; không tạo replacement để thử. Không auto giảm budget/pause hoặc reset/cộng thêm cap khi restart.
4. **CPC có điều kiện:** nếu Bảo giao áp dụng₫25.000, capture before, sửa đúng bidding field, Save, đóng/mở lại xác nhận checked/value25000. Giữ Maximize clicks/protected settings. Nếu Bảo chọn không limit, docs ghi đúng quyết định mới; không khai đã sửa khi chưa thực hiện.
5. **Inventory còn thiếu:** đối chiếu28 keyword/24 negative/16 ads/96 associations, approval vs enabled vs delivery; saved URL/locale/suffix theo từng group/asset nếu cần kết luận toàn bộ. Brand overlap là investigation chỉ đọc; không sửa campaign khác. Tách sample và full coverage.
6. **Docs sync:** cập nhật canonical current truth theo bảng dưới từ fresh evidence; thêm dated follow-up vào receipt gốc, giữ capture-time history. Mốc day N ghi rõ inclusive hay elapsed, không thay lịch PO chỉ vì đổi nhãn. Giữ content gates đúng trạng thái.
7. **Audit/closeout:** compare saved live với mandate và acceptance; reviewer inspect actual state/evidence, không chỉ executor summary. Không bắt buộc spawn; delegation cần mandate. Quyền commit plan không tự thành quyền commit/merge/push remediation.

## Docs impact và message boundary

Đã review DOCS_IMPACT_MAP và canonical entrypoints trong phiên audit. Commit này thêm plan và CURRENT_STATE notice; **chưa hoàn tất remediation/docs-sync PASS**. Notice mới supersede riêng các khẳng định cap/CPC chưa được chứng minh; không rewrite lịch sử. Agent sau reconcile:

| File | Current truth cần sync |
|---|---|
| CURRENT_STATE.md; README.md | Actual controls, latest readback, remaining gaps, local commit vs remote |
| ads/google/Google_Search_Build_Sheet.md | Saved CPC thay file-only claim; budget type/limit; keyword eligibility/asset review |
| drafts/S04_Measurement_and_Budget.md | PO cap vs platform controls; cost/remaining; bỏ guidance lỗi thời và restart không được cấp quyền |
| operations/Pre_Ad_Readiness_Plan.md; operations/Pre_Ad_Readiness_Index_2026-10-28.md S01 | Findings/decisions/gates; PO live authority không readiness PASS |
| operations/google-search-draft/2026-11-02/RECEIPT.md | Dated follow-up/evidence; uploaded khác saved; preserve original record |
| operations/Public_Source_Register.md | Giữ scope PO proof-use; chỉ đổi nếu có evidence/quyết định mới |
| operations/OSAT_Route_Source_of_Truth.md; tracking/Semiconductor_Tracking_Contract.md | Review nếu route/tracking truth bị ảnh hưởng; URL tồn tại không chứng minh attribution |

MSG/native review chưa hoàn tất. Anchor đã đọc: VY-CONTENT-ANCHOR revision1.0, SHA256 `6621d53c845939730ebcb1f59bbf85fb8a0d9acb156e5236e7387c0e69867ac5`; email VY-MAIL-USER-20261006 SHA256 `c5a6f35533e7a8b3b439ec4d9a260611fcdd2f67ddb0f046a3e33d28c6316d2b`. Binding này không là message-review PASS. VN domestic và FDI en/zh-Hans/zh-Hant cần riêng persona/decision unit/business value hoặc readiness. Live OSAT có `车规级/車規級`; receipt đã flag claim. Không biến flag thành unsupported-fact verdict khi chưa kiểm nguồn. Không tự reword vì execution mandate copy verbatim. Copy revision mới cần reread anchor/email, AD-ED-01, first-touch-anchor (ERP/MES exception hiện hành) và receipt template từng surface/journey. Không freeze/adopt locale adapter hay thay frozen core.

## Acceptance và rollback

- **A1:** Saved control + actual report/official rule chứng minh cap PO, tính cả cost đã phát sinh. Nếu chỉ có daily budget/dates/manual checks, ghi limitation và không PASS hard-cap criterion.
- **A2:** Saved/reopened CPC đúng quyết định Bảo; protected settings/inventory không đổi ngoài mandate. CSV không thay readback.
- **A3:** Canonical current notices thống nhất live/evidence/timestamp/unknown; không còn khẳng định cap/CPC chưa chứng minh dưới nhãn current. Old history giữ đúng scope/date. Local commit khác remote push.
- **A4:** Low volume không demand zero; under review không approved; URL sample không all-URL PASS; MSG/native/brand/proof/attribution gaps giữ nhãn đến khi thực sự đóng.
- **A5:** Không extra campaign, enablement, tag/form/landing change, lead submission, scheduler hoặc mutation campaign khác. Vượt scope cần exact mandate.

Trước authorized mutation ghi prior saved values và recovery route. Rollback chỉ hoàn nguyên setting đã đổi trong authority rồi verify; không refund được spend, không reset cost/history, không tự xóa campaign. Docs recovery dùng bounded follow-up theo mandate, không reset/rewrite Git.

Execution chọn SUCCESS/PARTIAL/FAILURE/BLOCKED theo evidence; audit chọn AUDIT_PASS/AUDIT_FAIL/INSUFFICIENT_EVIDENCE riêng. Chỉ PASS khi critical criteria của scope được giao có evidence. Hiện tại: **plan recorded; remediation NOT_STARTED; prior execution CHANGES_REQUIRED; full content/URL/attribution certification INSUFFICIENT_EVIDENCE**.

## Official sources checked02/11

- [Budgets overview](https://support.google.com/google-ads/answer/10486536?hl=en): average daily vs campaign total budgets; daily/monthly limits.
- [Campaign total budgets](https://support.google.com/google-ads/answer/10486938): Search supported, new campaign only, không đổi budget type existing campaign.
- [Budget changes](https://support.google.com/google-ads/answer/10487143?hl=en): budget/end-date changes ảnh hưởng limit; recheck actual report.

Reverify current guidance khi execute ở ngày/revision khác; platform documentation không chứng minh account đã lưu control.
