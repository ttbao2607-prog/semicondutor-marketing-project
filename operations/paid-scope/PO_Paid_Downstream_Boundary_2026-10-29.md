# Bảo — ranh giới paid ads và downstream,29Oct2026

Source: Bảo trực tiếp chỉ đạo trong phiên: “Phần Bảo và agent lo paid ad là được, sẽ chỉ scope vòng quanh như plan (ad metric), downstream sẽ có đội khác lo (như rep tn, có ng liên hệ sẽ có đội nhận thông tin, Bảo sẽ nhận feedback sau đó).” Đây là scope clarification hiện hành, không là chọn journey mới, launch/spend hoặc đổi budget mandate.

Contract: cập nhật current readiness theo đúng ownership; giữ actual message/eligibility/creative/metric gates, bỏ blanket commercial-qualification/CRM/downstream blockers đã suy quá rộng. Evidence: approved delivery plan và current user instruction. Root SELF_REVIEW, no independent audit; no runtime/account/creative change. Completion bằng source-linked scope table và canonical synchronization, không dùng việc sửa docs để cấp launch PASS. Local checkpoint theo yêu cầu commit trước; không push/merge.

## Trong scope Bảo + repo/agent

| Việc | Mức evidence cần cho paid |
|---|---|
| Audience ↔ persona/pain/journey relevance | Có hypothesis có căn cứ về ngành/hoạt động/chức năng người đọc; đối chiếu copy/proof/reader không gọi sai nhóm. Không đòi chứng minh mọi recipient có quyền mua ERP hoặc chắc chắn thành khách trước awareness |
| Native eligibility/configuration | Exact targeting được UI hỗ trợ và đủ điều kiện, không dùng470+ toànR5 để chứng minh subgroup. Nhóm5 too-small là actual paid issue vẫn giữ, không bị scope clarification xóa |
| Creative/copy/proof/rights | Đúng literal copy, hình/render/định dạng/headline/CTA/nguồn/phạm vi quyền dùng. Giữ approval case/translation/publication đã có; chỉ nêu permission thật sự chưa có cho exact paid set. Không tự đặt thêm một reviewer bản ngữ/đội commercial như mandatory approval chain khi không có chỉ đạo yêu cầu |
| Entry/reader/CTA handoff | Đúng URL/locale/journey, nội dung tiếp nối hợp lý và đến đích nhận thông tin đã duyệt. Kiểm lỗi link/technical handoff là paid QA; không phải vận hành inbox, tư vấn, sửa quy trình nhận lead hoặc triển khai CRM |
| Budget/schedule/placement/bidding | Theo approved cap11.7m/first5.6m/reserve6.1m và weekly review; exact saved execution fields và release của Bảo vẫn cần theo scope hiện hành. Không hỏi lại cap/cadence, không tự launch |
| Metric / review / điều chỉnh | Company/function/seniority delivery khi report có, reach/impressions/frequency/CTR/engagement, spend/CPM/CPC. Plan cũng có reader engaged sessions/đi tiếp theo nguồn đo hiện có; giữ phần này, không tự bỏ vì gọi chung “ad metric”. Ghi unavailable/data-sparse đúng trạng thái, không số0 giả hoặc ROI giả |

## Ngoài delivery scope repo, không chặn chạy awareness vì chưa hoàn tất

- Rep tin nhắn, tiếp nhận thông tin, phân công/tư vấn, follow-up/sales, qualification và closing: đội downstream phụ trách.
- Xác minh nhu cầu mua, ngân sách mua hệ thống, local procurement authority và quyết định ERP cụ thể của từng account/visitor: không phải điều kiện đủ bắt buộc trước awareness. Những dữ liệu chưa biết vẫn ghi hypothesis/risk, không claim qualified buyer.
- CRM integration, form-success/receiver reconciliation end-to-end, conversion API, toàn bộ full-funnel attribution, tỷ lệ lead hợp lệ hoặc doanh thu: không tự thêm vào critical path paid trong nhiệm vụ hiện tại. Không triển khai/sửa downstream system.
- Bảo nhận feedback sau từ đội tiếp nhận; dùng feedback/verified lead làm tín hiệu thương mại bổ sung theo plan khi có, không bắt phải có lead/feedback để kết thúc technical paid readiness.

## Reconciliation với anchor và prior findings

VY-CONTENT-ANCHOR v1.0 A1/A2 vẫn áp dụng: rà relevance/decision context bằng evidence có, không mặc định group global=local buyer; thiếu commercial qualification không tự thành MESSAGE_ANCHOR_FAIL hoặc blanket launch blocker. A2 là yêu cầu kiểm fit và phân biệt unknown, không quy định phải verified purchasing authority52/52 trước awareness. Nội dung phải giữ usefulness và đúng persona/role; scope này không làm một Fabless journey tự phù hợp toàn52R5.

Prior group5 native warning giữ **INSUFFICIENT_REACH**. F1/F2/F3 comparison giữ conditional relevance; các phrase “phải xác minh local ERP buying authority” như điều kiện bắt buộc cần đọc theo scope addendum này. Chưa có số subgroup mới hoặc selected-set change. Native/render QA cho exact selected creative vẫn có ích/cần theo gate; “human/domain acceptance” không là một external reviewer blocker mới do agent tự thêm. Root review được khai đúng independence, không giả independent/native-market PASS.

Reader transport đã verified scoped; processed GA4 reporting còn chưa verified. Chỉ những nguồn đo cần để báo metric đã cam kết mới cần kiểm thích hợp; không đòi chứng nhận full attribution/CRM trước launch. Không report contact click thành verified lead, không suy measurable success từHTTP204. Tracking/privacy regression thật ở paid entry vẫn là vấn đề phải xử lý.

Docs impact reviewed: CURRENT_STATE/README, readiness index, Pre_Ad_Readiness_Plan, LinkedIn build entrypoints và S04 có current-scope notice. Historical source/receipts/hash-bound packs không rewrite. Execution SUCCESS khi các pointers/row dispositions nhất quán; full paid-ready chưa được cấp vì không có saved final build/release trong lượt này.
