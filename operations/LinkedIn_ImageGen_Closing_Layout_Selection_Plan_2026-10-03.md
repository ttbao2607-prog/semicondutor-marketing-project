# Chọn bố cục card cuối trước khi sửa harness — 03-10-2026

DRAFT_PLAN_READY / NO_CANDIDATE_YET / NO_HARNESS_UPDATE. Checkpoint đã lưu tại `f3c7e17c50163672659ab75bd9ee5300384b1694`; parent xác minh151run-file bytes,164files trong checkpoint và indexempty. Kế hoạch mới là local UNCOMMITTED/UNSTAGED sau checkpoint; chưa yêu cầu commit thứ hai, push/merge/live.

## Thứ tự bắt buộc

1. Checkpoint findings/drafts đã hoàn tất. P3 Wave0 vẫn FAIL,1base+1correction đã tiêu thụ; không thêm permission từ reserve cũ.
2. Sau khi Bảo cho thực hiện kế hoạch preview: tạo đúng hai prototype P3-A5 A/B, cùng exact copy, rồi xem actual native và actual reader desktop/mobile. Không đánh giá layout bằng prompt/spec.
3. Bảo chọn A hoặc B sau khi xem actual renders và nhận xét chất lượng hình/độ dễ đọc. Không đưa thông số font/JSON/runtime thành câu hỏi cho Bảo.
4. Nếu cần, refine đúng phương án được chọn, tối đa một lượt theo fresh internal release trong budget đã duyệt; audit lại. Nếu không đạt thì stop CHANGES_REQUIRED, không retry liên tục.
5. Freeze exact accepted layout+wording+assets chỉ sau auditclear và Bảo chấp thuận đúng render. Sau khi Bảo chốt đúng bố cục, cập nhật harness trong sequence đã được user phê duyệt, với fresh internal bindings và relevant checks.
6. SAU freeze layout: đề xuất propagation harness, stress-test body/source dài hơn trên Fabless+OSAT theo phạm vi stress-test được giới hạn riêng. Implement harness sau khi Bảo chốt đúng bố cục, trong sequence đã duyệt; không xin thêm generic permission trừ khi có material scope mới. Không tạo toàn bộ rollout ngay.

## Hai hướng để preview sau này

**A — khuyến nghị:** headline/body và source paragraph full-width nằm trên vùng ảnh/grounded diagram thấp hơn, giảm diện tích ảnh để dành khoảng chữ. Source là đoạn chính ngang cỡ body, không footer.

**B:** vùng ảnh/diagram chuyển tiếp nhỏ ở giữa; source panel full-width nằm dưới với hierarchy như đoạn chính, CTA ở hàng riêng. Giảm ảnh trước khi giảm chữ.

Cả hai giữ white/blue daylight office/material/semiconductor grammar, official header/category/5/5/logo. Không iconcolumn/Taipei skyline chiếm sourcewidth, không tinyfooter, không mandatory propcount/percentages. Blank records/no microglyphs/chart/extra labels/ticks/seals. Source comfort bằng body, ample wrap/spacing, không co font để nhét copy.

## Copy và ranh giới immutable

Cùng exact reviewed Wave0 copy SHA256 `b5225251b5abe014caa2d9fcd2e38ebc3f70b19188ac28ac052f08d4ff41ca19`, path `operations/linkedin-imagegen-dogfood/all-scenarios-2026-10-03/wave0/common/p3-copy.json`. Không đổi wording để fit hoặc chấp nhận dấu câu ảnh khác nguồn:

- headline: Từ yêu cầu đến dữ liệu có người giữ
- body: Bộ hồ sơ cần được đối chiếu với yêu cầu cụ thể của khách hàng.
- source_text: Tài liệu giải pháp bán dẫn Digiwin Đài Loan: ERP và MES trong bối cảnh quản trị và sản xuất.
- cta: Đọc thêm về dữ liệu audit
- native_headline: Digiwin: góc nhìn quản trị hồ sơ
- Artwork labels: ERP · QUẢN TRỊ BÁN DẪN, 5/5, Góc nhìn ngành tại Đài Loan

Headline không finalperiod. Regional label/logo/category/5/5/CTA giữ exact. Source/context xuất hiện đúng một lần. Caption/nativeheadline/alt ngoài raster; reconcile alt với actualimage dưới fresh review.

Future proposed budget:2base P3closing layouts +max1refine chosen, DRAFT_NOT_RELEASED. Built-in native ImageGen, square minimum1080, preserve original bytes/noresize/composite. Parent owns source/copy/review/release/spec/preflight/dispatch/audit; leaf draft/viewer bounded newnamespace only. Gate/tests/reference/source/priornative/audits unchanged trong phase này.

## Kiểm tra và quyết định

Exactwording/punctuation/logo/source trước; ordinary mobile actual317–333px imagewidth/nozoom và fullcard desktop phải dễ đọc. Không chỉ native zoom. Chosenclosing cần xem trong full5 P3 cùng unchangedA1–A4, fourtransitions, CTA/reader behavior, public-only bundle và frozenF3 familycomparison. Sourceparagraph không được icon/decoration làm hẹp. Mechanical tests không chứng nhận creative/readability.

PO chỉ cần chọn A/B sau actualrenders và chấp thuận chosenquality hoặc nêu điểm chưa vừa ý. Tệp pins/font targets/implementation do operator chịu trách nhiệm. Sau chọn/freeze mới đề xuất stress-test longerbody/source Fabless+OSAT và propagation trong sequence sau khi Bảo chốt đúng bố cục; không đổi frozen mechanism trước bước đó hoặc mở9future scenarios.

Existing frozen_harness scope mechanism+exactF3 giữ nguyên; P3 closingFAIL/currentrun/counts không đổi, không newPOacceptance/buyer/live inference. Docsimpactreviewed: current workflowstage/currententry/status/runbook/execution/readiness/build/remainingplan synchronized; strategy/proofrights/landing/budget/tracking unaffected.
