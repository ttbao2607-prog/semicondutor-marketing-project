# LinkedIn carousel — constraints và awareness anchor

Ngày/revision: 2026-10-01 / v1.0. Owner: Bảo. Trạng thái: FORMAT AND POSITIONING SELECTED; production/live chưa bắt đầu. Đây là anchor để writer và auditor đối chiếu, không phải approval account/spend.

## 1. Quyết định Bảo

Chuỗi awareness dùng **carousel images + introductory ad copy**, kể chuyện qua từng card, để định vị **“Hình ảnh ERP chuyên gia / nhiều kinh nghiệm trong ngành semiconductor”** cho Digiwin. Đây là anchor chính của awareness; các role/POV là cách diễn đạt cụ thể anchor, không thay nó bằng nội dung giáo dục chung hoặc lời mời tư vấn đơn thuần.

Category hypothesis: giải pháp ERP và quản trị vận hành liên quan ngành bán dẫn. Desired association: khi cân nhắc giải pháp quản trị cho bài toán vận hành semiconductor, nhớ Digiwin là ERP có chuyên môn ngành và kinh nghiệm phù hợp. Đây là mục tiêu định vị, chưa phải kết quả brand-memory đã đo hoặc factual claim về mọi capability/deployment tại Việt Nam.

Ad phải thể hiện chuyên môn bằng tình huống, lập luận, cơ chế và proof đúng scope. Claim “nhiều kinh nghiệm”, số năm/số khách hàng, regional deployments và case cụ thể phải có source/entity/territory/date/rights; không suy kinh nghiệm MES thành capability ERP, hoặc kinh nghiệm Đài Loan/Trung Quốc thành triển khai Việt Nam. Approval existing VI claims vẫn giữ trong scope đã được Bảo quyết định; claim mới/rộng hơn cần proof riêng. Không cần viết nguyên câu “chúng tôi là chuyên gia” trên mọi card.

## 2. Platform constraints — verified official docs 2026-10-01

| Hạng mục | Constraint / nguồn |
|---|---|
| Introductory text | Tối đa 255 ký tự; Help khuyên ≤150 để tránh truncation trên một số thiết bị [S2]. Caption mở tình huống, không chứa toàn bộ câu chuyện |
| Card headline | 45 ký tự; tối đa 2 dòng trước truncation [S2]. Đây là field headline, khác chữ thiết kế trong ảnh |
| Cards | 2–10 card mỗi carousel [S1/S2] |
| Images | Production lựa chọn PNG; JPG cũng được S1 hỗ trợ. Tỷ lệ 1:1, khuyến nghị ít nhất 1080×1080 [S1]; Help nêu max dimension 4320×4320, max file size 10 MB từng card [S2] |
| Feed rendering | Help mô tả ảnh scale xuống 312×312 px [S2]. Dùng làm điểm kiểm readability, không hứa mọi device/viewport đều đúng kích thước này; account desktop/mobile preview vẫn cần |
| In-image text | Hai spec đọc được không nêu quota ký tự riêng; vẫn chịu readability/layout và ad policies. Không suy là chữ vô hạn hoặc chắc chắn không bị moderation |
| Destination | Landing URL là required theo S1; prefix http/https, tối đa 2000 ký tự. “Không click-driven” là mục tiêu/narrative, không có nghĩa card bị vô hiệu hóa link |
| Media/edit lifecycle | Không hỗ trợ video trong image carousel [S1]. Help nói không sửa carousel cards sau save [S2]; revision content cần kiểm tra lifecycle trong account trước thao tác, không overwrite như chắc chắn editable |

[S1: LinkedIn Carousel Ads Specifications](https://business.linkedin.com/advertise/ads/sponsored-content/carousel-ads/specs).
[S2: LinkedIn Help — Carousel Ads advertising specifications](https://www.linkedin.com/help/linkedin/answer/a427022).

Specs là observed public documentation, chưa xác nhận current account rights/objective/placement/CTA/metrics. Recheck trước export/upload. Help còn hỗ trợ non-animated GIF, nhưng output scope chọn PNG để thống nhất.

## 3. Editorial constraints — quyết định thiết kế nội bộ

- Câu chuyện hoàn chỉnh ngay trên LinkedIn. Người không mở LDP vẫn hiểu tình huống, cách nhìn và vì sao Digiwin liên quan.
- Một carousel một role/POV và một pain chính. Caption là hook; card text là nội dung chính; headline dưới card hỗ trợ từng beat.
- Planning default 4–5 card/ad, có thể điều chỉnh trong range platform theo story; test cách kể giữ cùng số card, brand treatment, độ sâu/proof và destination. 20–35 từ/card là starting guideline để thử layout, không platform limit hoặc acceptance quota cứng.
- Card đầu đặt tình huống; các card giữa giải thích; card cuối gắn chuyên môn/kinh nghiệm Digiwin với scope có proof. Mỗi card có ngữ cảnh, không giả định mọi người swipe hết. Không nhồi chữ hoặc thu nhỏ font để “kể nhiều”.
- Brand/name/logo và category ERP hiện diện rõ; mechanism/proof phải liên quan positioning. Không chỉ đổi logo lên một infographic ngành chung.
- Một route phù hợp cho mỗi carousel: OSAT `/semiconductor-osat`, Fabless `/fabless`, Supplier `/supplierecosystem`, trên `https://solutions.digiwin.com.vn`. Không nhét cả ba URL vào caption. Pin destination/locale/UTM khi test được giao; landing dùng để đọc thêm, click/lead là tín hiệu phụ. Đây là quyết định route khác baseline cũ Company-Page-only, không thay objective native awareness.

## 4. Artifact contract chọn cho production

| Artifact | Format / acceptance |
|---|---|
| Decision/evidence/brief/ad records/experiment/QA | Markdown `.md`; ad record có caption và character count, card order, text trong ảnh, headline từng card và count, alt text, source IDs, destination/locale/revision |
| Storyboard | `.md` theo từng card: beat, visual, copy, desired association, proof và expected role relevance |
| Editable card sources | `.svg` từng card với text chỉnh sửa được; `.md` copy là authoritative wording. Raster artwork riêng `.png` khi cần, không khóa chữ chính vào raster-only source |
| Upload exports | `.png`, square 1080×1080 target, mỗi card ≤10 MB; spec/account gate trước release |
| Review preview | Local self-contained `.html` mô phỏng caption + card sequence + headlines; `.png` contact sheet và desktop/mobile QA screenshots. Đây là simulated preview, không bằng chứng UI LinkedIn/account |
| Manifest | `.csv`: ad ID, POV/cohort/locale/revision, order, source/export path, hash, dimensions, bytes, destination, source/proof IDs, QA state |

Hai carousel A/B; C tùy chọn. Mọi ad được chọn đều preview/QA. Nếu C là static cũ, comparison phải ghi mixed-format package; nếu adapt C thành carousel, ghi adapted baseline với delta và source pin, không gọi unchanged control.

## 5. Audit anchors / release limits

Auditor kiểm tra platform counts/spec provenance, readability tại rendered size, story/role fit, ERP–semiconductor brand association, proof scope, advertiser attribution và destination consistency. Caption/card engagement không chứng minh đọc hết, hiểu hoặc memory lift. Self-review khác buyer evidence. SUCCESS của artifact scope không tự là AUDIT_PASS, LIVE READY hoặc brand outcome SUCCESS.

Format/positioning đã chốt; cohort/pair/test type/locale/C, budget, live mandate và buyer/product/native validation vẫn theo execution gates. Chưa tạo content/asset trong lượt ghi anchor. Anchor và docs sync hiện local working-tree, chưa commit/merge/push.
