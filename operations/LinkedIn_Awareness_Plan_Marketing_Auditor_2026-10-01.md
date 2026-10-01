# Marketing plan audit — LinkedIn awareness POV plan

Ngày: 2026-10-01. Auditor lens: `$marketing-plan-auditor`. Báo cáo cho plan writer, theo yêu cầu ghi file của Bảo; không sửa plan hoặc commit.

## Kết luận và phạm vi

**Plan dùng được để Bảo review và chọn shortlist, với một finding material cần đóng trước sản xuất cặp test.** Không thấy critical finding trong phạm vi plan offline. Đây là audit plan, không phải audit complete copy, live test hoặc activation readiness. Báo cáo không cấp operational authorization.

Artifact: `operations/LinkedIn_Awareness_Adcopy_Optimization_Plan.md`, file mới chưa track, toàn bộ file là delta tại thời điểm audit. Worktree `D:/optimize-awareness-LinkedIn-adcopy`, branch `slice/optimize-awareness-linkedin-adcopy`, HEAD `f49ce83aab18779228fbe5f696d0bafab5cb770e`, cùng HEAD local main. SHA-256 file: `f0bda2b83a16b2220cbcbb82e25e740a7c61cbb7ba7aeb0d8418c133ded02add`. Remote không được fetch lại trong lượt audit; không kết luận trạng thái remote hiện tại.

Stage: internal plan để chọn role/POV và phạm vi production; không yêu cầu evidence activation ở giai đoạn này. Buyer hypothesis: các role OSAT, Fabless, Supplier/SI và domestic end-user. Objective: liên tưởng Digiwin với chuyên môn vận hành bán dẫn và độ phủ đúng tệp; wave đầu đề xuất OSAT. Thời gian test cụ thể còn mở; planning ceiling và chương trình tám tuần giữ theo canonical, không phải quyền spend.

## Findings

| ID / severity | Evidence/location | Finding và ảnh hưởng | Đề xuất / điều kiện đóng |
|---|---|---|---|
| MPA-01 / Material | Plan dòng 50: O4 dành cho Plant leadership, bao gồm lot/test/WIP. Dòng 63–65, 115: dùng O4 làm comparator cho cả Quality và Operations. Dòng 79: một ad một pain chính. | Brief O4 chưa nhất quán với role cohort và độ rộng pain của O1/O2. Nếu writer giữ nguyên, phép thử có thể phản ánh độ phù hợp role hoặc độ rộng nội dung, làm yếu cách diễn giải khác biệt POV. Đây là rủi ro thiết kế suy ra từ brief, chưa phải kết quả delivery. | Brief O4 cho chính cohort đã chọn, giữ cùng operating question, pain và desired association với bản đối chiếu, khác cách kể; hoặc ghi rõ test gói thông điệp có nhiều khác biệt. Đóng khi hai brief thể hiện cùng role, pain, association, mức proof và format, hoặc experiment card giới hạn rõ kết luận về gói. |
| MPA-02 / Minor | Plan dòng 63 và 81: baseline copy hiện có làm C nếu được chọn; chưa pin source/revision. Creative register có static, B2B-v2 và nhiều locale. | Writer có thể chọn baseline khác phương án Bảo hình dung, khiến comparison không tái dựng được. Chưa chặn PO review vì baseline C là tùy chọn. | Nếu chọn C, pin source path/revision hoặc hash, locale và phần giữ nguyên. Nếu bỏ C, ghi production package có hai complete records. Đóng khi quyết định và artifact tương ứng được xác định trước sản xuất/test. |

Owner/deadline chưa được nguồn xác lập; auditor không tự gán. Các đề xuất không phải mandate sửa hoặc launch.

## Strengths và giới hạn

- Plan phân biệt fact/proposal/unknown; chẩn đoán copy ở dòng 23 là nhận định biên tập, không giả làm evidence delivery.
- Dòng 65–73 tách POV, hook, format và locale; không hứa equal delivery hoặc significance.
- Dòng 87–97 phân biệt coverage, interaction, comprehension và brand lift; không dùng click như bằng chứng nhận thức hoặc quan hệ nhân quả.
- Allocation, sample, account-specific test design và live authority được defer đúng stage. Thiếu chúng không phải critical finding cho việc chọn shortlist hiện tại.
- Quyền dùng VI claims đã được Bảo phê duyệt được giữ trong scope; không tự tái mở approval hoặc suy thành quyền live.
- Không có live/account validation; chưa có complete ad records để kiểm chứng artifact-level role fit, attribution hoặc format equivalence.

## Nguồn đã đối chiếu

AGENTS.md/session guidance; CURRENT_STATE.md; DOCS_IMPACT_MAP.md; Semiconductor_Work_Kickoff.md v2.0; Semiconductor - Website & Ads.md; drafts/S01_Proof_and_Message.md; drafts/S03_LinkedIn_Audience_Research.md; drafts/S04_Measurement_and_Budget.md; ads/linkedin/LinkedIn_Build_Pack.md; operations/Pre_Ad_Readiness_Plan.md; assets/linkedin/source/vy-four-locale-copy-register.md; operations/LinkedIn_Carousel_Governance_Record.md; plan và focused rubric của marketing-plan-auditor. Kết luận dùng scope và quyết định mới, không coi statement lịch sử bị supersede là current truth.

## Handoff

Bảo có thể chọn cohort, association, POV và baseline option. Plan writer nên đóng MPA-01 trong brief sau shortlist; pin MPA-02 nếu dùng C. Re-audit các thay đổi và dependencies liên quan; không mặc định chạy lại toàn bộ audit hoặc mở live gate.

Dogfood observation: skill giúp review theo stage và giữ quyền quyết định của Bảo. Một lượt không chứng minh reliability trên mọi plan; chưa có behavioral benchmark độc lập.

**Docs impact reviewed: no canonical update required.** Chỉ thêm báo cáo tư vấn; chưa thay đổi canonical strategy, allocation, assets hoặc account state. Không sửa plan, không commit/merge/push.
