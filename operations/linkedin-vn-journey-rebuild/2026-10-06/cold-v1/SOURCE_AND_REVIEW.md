# Cold VN v1 — source và PREGEN content review

Date: 2026-10-06. Writer/reviewer: /root, **SELF_REVIEW**, không independent hoặc PO acceptance. Scope: một Cold Single image, tất cả copy fields và storyboard trong [public-copy.json](public-copy.json). Base f52f391, branch slice/linkedin-vn-journey-rebuild. Persona và segment đã ghi trong JSON là giả thuyết nội dung, chưa phải live targeting verified.

## Binding

- Stage: PREGEN_SCRIPT / content-only review. Revision VN-COLD-READINESS-v1.
- Copy SHA256: `71e18428f86c112ea7b2ebd61e768ac8bc3c3c478d601bf73d3f1188d1398bf7`.
- Anchor VY-CONTENT-ANCHOR v1.0: `96197cd1999e250af64ab0a3a54e24cf3c2429b8366be53e2cc680a634667337`.
- Email VY-MAIL-USER-20261006: `87475d082cb66cc1dc11285a6a2d7982d77d80ca9cd2c14522bab2d212ebb5b3`.
- Native/demo: **POSTGEN_NOT_RUN**. Contract/spec/release chưa tạo; đây chưa phải dispatch receipt. Destination và các stage RMK/evidence chưa hoàn tất.

## Nguồn official đã mở lại

[Pressway Precision — Digiwin Vietnam](https://www.digiwin.com.vn/casestudies/erp-pressway-precision-case-study-vn/), observed 2026-10-06. Locator: đoạn thảo luận quy trình/Workflow ERP (web lines127–134); phần quản lý tiến độ/số lô và minh bạch dữ liệu (lines147–156). Trang xác nhận nhà máy linh kiện nhựa điện tử tại VN và dự án Workflow ERP; không xác nhận doanh nghiệp thuộc sở hữu nội địa hoặc admission vào chuỗi bán dẫn. Dùng làm căn cứ cho phạm vi tư vấn quy trình và quản lý thông tin của nhà cung cấp; không sử dụng ảnh/tên/result của khách hàng trên Cold. Quyền tái sử dụng case/customer asset trong paid vẫn chưa được cấp bởi việc đọc trang.

Claim ledger: “Chúng tôi cùng doanh nghiệp rà soát quy trình, nhu cầu thông tin và cách quản lý dữ liệu với ERP cho sản xuất” là diễn giải vai trò tư vấn theo cơ chế có nguồn. “Chuẩn hóa quy trình và dữ liệu với ERP cho sản xuất” là hướng giải pháp cần trao đổi theo hiện trạng, không claim kết quả cho mọi nhà máy. Không dùng số liệu, thời gian triển khai, audit certification, traceability depth hoặc hệ thống MES như năng lực ERP mặc định. Email/anchor là nguồn của trigger VN chuẩn bị vào chuỗi, không phải proof admission.

## MSG-ANCHOR-01 — exact field observations

| Rule | Observed field / string / scene | Disposition |
|---|---|---|
| A1 | category “NHÀ CUNG ỨNG VIỆT NAM”; caption “chuỗi cung ứng bán dẫn”; scene component workshop | MATCH trong hypothesis nhà cung ứng phù hợp hoạt động chuỗi, không nhắm mọi doanh nghiệp Việt Nam. Company/industry live fit vẫn pending. |
| A2 | persona chủ doanh nghiệp/giám đốc vận hành; không tên tập đoàn hay blanket exclusion | MATCH: nhắm người quyết định chuẩn bị quản trị; không suy hệ thống ERP tập đoàn hoặc account fit. |
| A3 | vi-VN; category, headline và caption cùng persona nội địa; câu hỏi quản trị | MATCH: không dịch hook OSAT/Finance, không dùng ROI FDI làm primary trigger. |
| A4 | Không claim ROI tài chính/FDI | N/A: VN_DOMESTIC Cold này. |
| A5 | headline “Muốn vào chuỗi bán dẫn. Năng lực quản trị đã sẵn sàng?” → body “Chuẩn hóa quy trình và dữ liệu với ERP cho sản xuất.” | MATCH: nhu cầu chuẩn bị → ERP bridge. Không hứa đã đủ chuẩn/vượt audit/có đơn hàng. |
| A6 | caption “rà soát quy trình, nhu cầu thông tin và cách quản lý dữ liệu”; role_line ERP; blank physical folders | MATCH có nguồn tư vấn/ERP. Cold đặt vấn đề, chưa giải thích kỹ thuật; lot/yield/recipe N/A cho unit này, không né yêu cầu depth ở RMK. Không fake UI/records. |
| A7 | native_headline “Chuẩn bị năng lực quản trị để tham gia chuỗi bán dẫn”; alt mô tả chuẩn bị quản trị; next_question về quy trình/dữ liệu và ERP | MATCH trong Cold. Category → hook → body → caption/native/alt/storyboard thống nhất. Không có CTA giả. Full journey/destination chưa review, không được nhận PASS từ receipt này. |

MSG-ANCHOR-01: **MESSAGE_ANCHOR_PASS — Cold source-copy/storyboard scope only, SELF_REVIEW**. Full journey + finished artwork: **INSUFFICIENT_EVIDENCE / NOT_RUN**. Nếu persona/copy/scene/anchor hoặc destination thay đổi, tạo review mới.

## AD-ED-01 / BRAND-ROLE / ADVERTISER-VOICE

- Logo: dự kiến một official mark, không thêm chữ Digiwin cạnh logo. Role_line xác định loại giải pháp; category xác định người đọc, không nhắc thương hiệu. Caption dùng “Chúng tôi” làm speaker, không kể Digiwin như reviewer thứ ba. Native headline/alt không nhắc thương hiệu thừa. Brand-role và advertiser-voice: **PASS cho script scope**, chưa artwork PASS.
- Headline/body: nhu cầu và cơ chế ngắn; không nội bộ “pending/verified/không chứng minh” trên ảnh. Category/role_line phải đủ lớn, không tự sinh label/footnote. source_footer/cta trống có chủ đích cho Cold nội bộ chưa bind destination.
- Caption/native headline/alt: cùng câu chuyện chuẩn bị; alt mô tả scene và thông điệp thay vì thêm capability/result. Storyboard: không cleanroom/customer site, badge certification, UI hoặc tuyến tự động đã hoạt động.
- Editorial script content: **PASS / SELF_REVIEW**. Artwork editorial/native/mobile: POSTGEN_NOT_RUN.

## Release blocker và next action

**Không ghi SCRIPT_REVIEW_PASS cho dispatch hoặc gọi ImageGen ở revision này.** PREGEN guard chỉ tồn tại dưới dạng WIP chưa commit tại worktree gốc khi kiểm tra 06/10. [Guard procedure](../../../../../optimize-awareness-LinkedIn-adcopy/operations/message-anchor/Pregen_Script_Guard.md) yêu cầu chạy wrapper ngay trước mọi image call với trusted pins và frozen fresh validation. Link này là local cross-worktree dependency, không portable public reference.

Sau handoff: nhận committed guard/version từ owner; kiểm đúng Single-image adapter route; tạo contract/review/release/spec mới bound copy, context, source và scope Cold; chạy fresh guard rồi mới generation theo mandate “làm lại Cold” của Bảo. Không copy WIP rồi tự tuyên bố release. Sau ảnh: inspect native + desktop/mobile và ghi POSTGEN receipts, mới handoff human review.

Status: **COLD_COPY_READY_FOR_REVIEW / IMAGE_GENERATION_BLOCKED**. Execution PARTIAL: Cold copy + source + semantic self-review hoàn tất; chưa ảnh. Không commit/push/live/account change. Frozen core/old artwork untouched.
