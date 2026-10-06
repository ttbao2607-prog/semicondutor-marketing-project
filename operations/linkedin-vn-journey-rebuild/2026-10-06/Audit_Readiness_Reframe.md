# VN RMK / evidence — thay case và làm rõ kinh nghiệm ngành

2026-10-06 · Owner /root · DRAFT / CHANGES_REQUIRED · chưa SCRIPT_REVIEW_PASS, chưa gent.

Mandate mới của Bảo: bỏ case hiện tại vì không đủ liên quan bán dẫn; ưu tiên Trung Quốc/Đài Loan; RMK phải chứng minh kinh nghiệm chuẩn hóa quy trình để chuẩn bị audit. Mandate này thay hướng Pressway của bộ mới, không thay Cold v4 đã freeze. Không chỉ sửa ba ảnh xưng hô rồi chạy lại bộ cũ.

Contract: nghiên cứu nguồn công khai, chọn case phù hợp, lưu storyboard mới và giới hạn claim. Đạt khi case có ngành/địa lý/product rõ, mỗi ý có nguồn và count không bị đổi thành số khách hàng vượt audit. Audit target: đối chiếu bảng nguồn, storyboard và current status. Root self-review, không independent-agent audit. Không ImageGen/live/Git mutation.

## Nguồn và quyết định nội dung

| Nguồn | Điều có evidence | Giới hạn |
|---|---|---|
| [Digiwin CN — bán dẫn](https://www.digiwin.com/solution/Semiconductor/index) | Publisher nêu kinh nghiệm tư vấn hơn 700 khách hàng IC; có phần hỗ trợ kiểm tra nhà máy. | Không phải 700 khách hàng vượt audit; không riêng ERP, VN hoặc số dự án chuẩn hóa. Ngày/count definition chưa rõ. Web open lỗi, nhưng public HTTP GET ngày06/10 trả200 và xác nhận exact claim; bounded observation tại IC700_Claim_Scope.json. Full script review vẫn pending. |
| [Aplus / 常州欣盛 — DigiHua](https://www.digihua.com/常州欣盛半导体技术股份有限公司/) | Case Trung Quốc, COF; audit khách hàng là động lực triển khai iMES + TOP GP. Có truy xuất lịch sử từng sản phẩm, SPC, quản lý tham số và theo dõi bất thường. | Không có kết luận đã vượt audit hoặc điểm audit. Không quy mọi cơ chế cho ERP. Không lấy thời gian triển khai làm cam kết cho VN. |
| [WONIK Taiwan Quartz](https://www.digiwin.com.tw/case/1563.html) | Nhà cung ứng sản phẩm thạch anh cho bán dẫn tại Đài Loan; EasyFlow.NET quản lý phiên bản/tài liệu quy trình, EIS có báo cáo quản trị và kiểm tra. | Case công bố 2018; không chứng minh vượt audit khách hàng, không phải outcome ERP đơn lẻ. |
| [DigiHua — lịch sử](https://digihua.com.tw/en/about-digihua/) | Công bố các mốc Digiwin đầu tư DigiChain/iMES và hình thành DigiHua. | Ghi rõ nguồn và đơn vị thực hiện; không suy đội VN thực hiện case hay cam kết năng lực triển khai tại VN. |

**Chọn Aplus làm case chính cho storyboard mới** vì có trigger audit trực tiếp và thuộc bán dẫn. WONIK là lựa chọn thay thế nếu muốn câu chuyện nhà cung ứng vật liệu + quản lý tài liệu sát vai trò VN hơn, hoặc muốn tránh case thiên MES. Cả hai tốt hơn Pressway cho scope mới; Pressway giữ historical asset, không tiếp tục làm evidence trong journey này.

Điểm phân biệt cần kể: kinh nghiệm tình huống bán dẫn được cụ thể hóa bằng quy tắc và hồ sơ có thể kiểm tra, qua case ngành thật. Không claim độc quyền hoặc chứng minh Digiwin hơn mọi đối thủ. ERP, MES, SPC và quản lý tài liệu phải tách đúng sản phẩm.

Hook số đề xuất: **“Kinh nghiệm tư vấn hơn 700 khách hàng IC”** — attributed publisher claim, PENDING release. Không viết “đã chuẩn hóa cho 700 doanh nghiệp vượt audit”. Không cộng/gộp với 200+ Cold; hai nguồn có scope khác nhau, không chứng minh cùng mẫu/period.

## Storyboard RMK — hướng mới, chưa phải exact copy release

| Card | Thông điệp / câu dự kiến | Vai trò |
|---|---|---|
| R1 | “Khách hàng yêu cầu audit. Quý Doanh Nghiệp đã chuẩn bị hồ sơ đến đâu?” | Trigger người đọc và bước chuẩn bị; không hứa đạt chuẩn. |
| R2 | “Kinh nghiệm tư vấn hơn 700 khách hàng IC” | Đặt kinh nghiệm ngành của chúng tôi có attribution, count chưa release. Nếu pin không đủ, bỏ số và dùng kinh nghiệm từ case cụ thể. |
| R3 | “Từ hồ sơ rời rạc đến lịch sử có thể truy xuất” | Dẫn cơ chế truy xuất trong case, ghi rõ iMES; minh họa dữ liệu liên kết, không ảnh thực nhà máy. |
| R4 | “Chuẩn hóa kiểm soát chất lượng và thay đổi tham số” | SPC / ECN trong case; không gọi là tính năng ERP chung hay cam kết vượt audit. |
| R5 | “Xem Aplus chuẩn bị hệ thống trước audit khách hàng” | Nối sang case cùng vấn đề. Caption xác lập chủ thể chúng tôi, nguồn DigiHua và giá trị chuẩn bị cho VN. |

## Storyboard evidence — Aplus, Trung Quốc

| Card | Nội dung cần chứng minh | Bridge |
|---|---|---|
| E1 | Danh tính, ngành, địa lý; audit là động lực triển khai iMES + TOP GP. | Đúng case / product scope. |
| E2 | Lịch sử từng sản phẩm theo serial, dữ liệu kiểm tra. | Hồ sơ có thể tra lại. |
| E3 | Tham số thay đổi và luồng theo dõi bất thường. | Cơ chế kiểm soát, không tự suy chứng nhận. |
| E4 | “Cùng chúng tôi rà soát nhu cầu chuẩn bị của Quý Doanh Nghiệp.” | Trao đổi hiện trạng; không invent gói audit consulting/free assessment đã được phép cung cấp. |

Không có card “đã vượt audit” vì nguồn không xác nhận outcome đó. Scene dùng minh họa quá trình/hồ sơ bán dẫn, không logo khách hàng, nhà máy thật, chứng chỉ hoặc số liệu tự sinh. Các field caption/native headline/alt/CTA/labels và destination phải viết lại theo revision này; chưa mang PASS từ bộ Pressway.

## Binding / gate / next action

- Anchor VY-CONTENT-ANCHOR revision1.0: `operations/Vy_Email_Content_Anchor.md`; SHA256 `96197cd1999e250af64ab0a3a54e24cf3c2429b8366be53e2cc680a634667337`.
- Email VY-MAIL-USER-20261006: `operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md`; SHA256 `87475d082cb66cc1dc11285a6a2d7982d77d80ca9cd2c14522bab2d212ebb5b3`.
- Branch slice/linkedin-vn-journey-rebuild; VN_DOMESTIC / vi-VN; owner/operations director của nhà cung ứng nội địa đang chuẩn bị cho chuỗi bán dẫn. A1/A3/A5/A6/A7 relevance có hướng phù hợp; A4 giá trị là hồ sơ/kiểm soát có thể kiểm tra, chưa outcome audit. Review theo từng field/transition còn pending: **MSG-ANCHOR-01 INSUFFICIENT_EVIDENCE**, không SCRIPT_REVIEW_PASS.
- VN-VOICE-01 revision1.1: mọi direct-reader address phải đúng “Quý Doanh Nghiệp”; pregen scan + semantic review và postgen chữ thực/native/desktop/mobile bắt buộc.
- Next: pin nguồn/count; hoàn thiện exact copy và scene toàn bộ 5+4, destination VN bridge; fresh source/rights/product/anchor/editorial/V5 receipts + dispatch bindings; sau đó mới gent/rebuild demo và hậu kiểm. Các claim quyền dùng/customer marks, VN delivery scope và count-audit outcome chưa được xác minh.
- Current demo cũ là historical preview, CHANGES_REQUIRED cả message/case lẫn xưng hô. Reader-address candidate trước đây chỉ sửa cách gọi, không còn là ứng viên đủ để chạy lại.

Execution research/draft: SUCCESS. Creative release: CHANGES_REQUIRED / REVIEW_PENDING. Claim “bao nhiêu khách hàng vượt audit”: INSUFFICIENT_EVIDENCE. Chưa ảnh mới/commit/push/main/live. Cold, frozen core, EN/Chinese và budget 11,7 triệu giữ nguyên.


## PO nuance update — kinh nghiệm tư vấn700

Bảo chọn nuance kinh nghiệm tư vấn, thay số khách hàng vượt audit. Nguồn đã kiểm lại qua public HTTP200: “超过700家IC客户辅导经验”. Exact count sentence không ghi phạm vi Đài Loan/Trung Quốc, nên không gắn địa lý đó vào700 khi chưa có evidence. [Claim scope](IC700_Claim_Scope.json).

Copy candidate: **Với kinh nghiệm tư vấn hơn 700 khách hàng IC trong ngành bán dẫn, chúng tôi đồng hành cùng Quý Doanh Nghiệp chuẩn bị năng lực quản trị để đáp ứng yêu cầu đánh giá của khách hàng.** Đây là câu caption/bridge dài; headline và scene cần chia lại để đọc mobile. Case ghi địa lý riêng đúng nguồn. Count không biến thành audit outcome; policy1.1 vẫn bắt buộc. Chưa full script release hoặc generation.
