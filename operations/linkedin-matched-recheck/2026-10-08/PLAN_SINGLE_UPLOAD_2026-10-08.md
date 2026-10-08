# Week1 company list — sửa tổng thể, chốt một file, upload một lần

Owner quyết định: Bảo. Owner chuẩn bị: Codex/root trong worktree `D:/LinkedIn_Matched_Recheck_2026-10-08`, nhánh `slice/linkedin-matched-recheck-2026-10-08`. Không delegate. Trạng thái: **PLAN_PROPOSED**, chưa chạy vòng nghiên cứu tổng thể hoặc upload theo plan này. Checkpoint trước `c5c38c93` đã commit local; hồ sơ recovery và plan hiện là file local chưa commit, chưa merge/push.

Mục tiêu: hoàn tất một lượt rà và sửa tổng thể tệp công ty week1; giao một gói quyết định đầy đủ, khóa một CSV, rồi cập nhật Discovery hiện có đúng một lần khi Bảo duyệt gói final. Dừng các lượt upload thử theo từng công ty. Bản nháp sửa hai công ty trước đó chỉ là đầu vào, không phải file final để upload.

## 1. 93 unmatched sẽ xử lý thế nào?

93 là số mục trong bảng LinkedIn đã chụp, không mặc định là93 công ty nguồn khác nhau hoặc93 công ty không có Page.

| Nhóm hiện có | Số mục | Việc phải làm trong lượt tổng thể |
|---|---:|---|
| Khớp duy nhất toàn bộ thông tin đầu vào của bản nguồn hiện tại |64| Xác minh pháp nhân Việt Nam, website và Page; ghi định danh có bằng chứng hoặc lý do chưa tìm được. Không mặc định thiếu Page là nguyên nhân duy nhất. |
| Tên có trong nguồn nhưng các trường đầu vào khác phiên bản hiện tại |28| Đối chiếu domain/Page/city/date-added và lịch sử nguồn trước. Chốt mục này đại diện bản nào, có còn là lỗi hiện hành không; không sửa lại một định danh đã đúng chỉ vì mục cũ còn xuất hiện. |
| Khớp nhiều dòng nguồn trùng |1| Giữ các dòng nguồn; đối chiếu địa điểm/định danh và ghi quan hệ nhiều dòng–một công ty. Không chọn đại hoặc tự xóa dòng trùng. |

Mỗi mục phải có kết luận và liên kết tới source row. Những mục có cùng pháp nhân dùng chung một hồ sơ nghiên cứu; vẫn giữ mọi source row và provenance. Số64/28/1 là kết quả đối chiếu hiện có, chưa là chẩn đoán nguyên nhân backend.

Phạm vi không chỉ93 unmatched: rà luôn **3 mapping sai đã xác minh,141 matched chưa đủ bằng chứng**, cùng phần coverage của toàn424 dòng. Sáu mapping đã có bằng chứng giữ lại nếu định danh/revision không đổi. Nhóm210 dòng chưa thấy trong capture cần giải thích coverage, không gọi là unmatched hoặc tự loại bỏ. Các nhóm giao nhau nên không cộng số lượng thành backlog công ty mới.

## 2. Trình tự chạy một lượt tổng thể

### Bước A — khóa nguồn và giải thích khác phiên bản

1. Pin nguồn424 dòng/hash và bản immutable; ghi rõ CSV nào đã nạp, audience Discovery nào là mục tiêu, saved filename và checkpoint live. Đọc evidence cũ trước; chỉ bổ sung capture read-only khi còn thiếu thông tin cần cho đối chiếu. Không upload để thử xem nguồn nào đúng.
2. Đưa93 mục và150 matched vào cùng ledger424 dòng bằng tên + domain + Page + city/country; giữ quan hệ nhiều–nhiều và khác phiên bản. Không dùng tên gần giống để kết luận đúng công ty.
3. Chốt disposition cho28 mục khác phiên bản,1 mục vướng trùng,11 source rows xuất hiện cả matched/unmatched và210 dòng chưa quan sát. Nếu platform không cho chứng minh coverage, ghi rõ `SOURCE_VERSION_OR_COVERAGE_UNRESOLVED`; không bịa phần thiếu hoặc tính tỷ lệ match bằng150/(150+93).

Đầu ra A: một danh sách nghiên cứu không trùng pháp nhân, nhưng truy ngược được mọi mục/source row; không còn lỗi bị đếm lặp giữa nhóm unmatched và matched.

### Bước B — nghiên cứu định danh theo cả danh sách

Ưu tiên:3 mapping sai →93 mục unmatched hiện hành sau đối chiếu →141 matched còn thiếu bằng chứng → các dòng còn thiếu định danh/coverage. Reuse101 hồ sơ enrichment có nguồn; kiểm revision và entity scope trước khi nhận lại kết luận. Website từng được xác minh không tự chứng minh output LinkedIn đúng.

Mỗi pháp nhân có tối đa hai pass nghiên cứu trước khi đưa vào bảng ngoại lệ chung:

- **Pass1:** website chính thức/trang pháp nhân, hồ sơ công ty từ nguồn chính thức và Page công ty LinkedIn. Tìm exact entity/domain/local address; không thu thập hồ sơ cá nhân làm bằng chứng chính.
- **Pass2:** đối chiếu các dấu hiệu còn mâu thuẫn, alias Page numeric↔named, chi nhánh/công ty mẹ/JV, địa điểm và tên cũ. Chỉ mở rộng vào câu hỏi cụ thể chưa giải quyết; không tìm vô hạn hoặc upload thử.

Ưu tiên Page chính xác của pháp nhân trong nguồn, bổ sung website chính thức có căn cứ. Không gán Page công ty mẹ/tập đoàn cho nhà máy Việt Nam chỉ vì cùng thương hiệu; không đoán email domain, đổi thành tên công ty khác hoặc tạo Page mới. Nếu hai pass chưa đủ bằng chứng, kết thúc nghiên cứu dòng đó với lý do cụ thể và trường còn thiếu, gom vào một bảng cuối. Có bằng chứng mới từ Bảo thì xử lý toàn bộ bảng bổ sung trước khi khóa file.

LinkedIn hướng dẫn Page URL hoặc company website có thể giúp cải thiện matching; đây không phải cam kết match hoặc đúng scope pháp nhân. Nguồn: [Company list targeting](https://www.linkedin.com/help/lms/answer/a423102), [Troubleshoot Matched Audiences](https://www.linkedin.com/help/lms/answer/a420864).

Đầu ra B: **424/424 dòng có disposition cuối của lượt nghiên cứu**, kể cả chưa giải quyết; mọi sửa đổi có nguồn cụ thể. Không đổi nhãn “chưa đủ bằng chứng” thành “đã xử lý đúng” chỉ để chốt lượt.

### Bước C — sửa và kiểm toàn bộ ở local

Tích hợp tất cả sửa đổi đã xác minh vào một candidate duy nhất. Chỉ sửa `companywebsite` và `linkedincompanypageurl` trong phạm vi hiện có. Giữ424 dòng, thứ tự, dòng trùng và tám cột bảo vệ: companyname/companyemaildomain/stocksymbol/industry/city/state/companycountry/zipcode. Nếu cần sửa tên pháp nhân/địa điểm hoặc thu hẹp tập upload, liệt kê một lần trong gói ngoại lệ; chưa tự áp dụng.

Kiểm bằng cách đọc lại CSV đã lưu, so với nguồn hiện tại và immutable:

- Đúng template10 cột, đủ424 dòng và nguyên các trường bảo vệ; không thêm dòng/company ngoài nguồn.
- Mọi cell diff có source row, before/after, nguồn chính thức, lý do và reviewer thật.
- URL truy cập/alias và exact entity đúng; phân biệt endpoint bị rate-limit với Page sai hoặc không tồn tại.
- Rà toàn bộ định danh thay đổi và toàn bộ finding sai cũ; sáu mapping đúng không bị regression.
- Tách rõ identity, mapping correctness, ICP và quyền quyết định ERP; không suy FDI/locale hoặc loại công ty theo tên/tập đoàn.
- Chốt mọi known-wrong vẫn còn trong file và mọi trường hợp không đủ bằng chứng. Không đánh đồng kiểm cấu trúc PASS với audience quality PASS.

Đầu ra C: một candidate đã kiểm, change log đầy đủ và một bảng ngoại lệ tổng hợp. Root self-review ghi đúng self-review; independent audit không tự nhận PASS khi chưa có reviewer độc lập. Không tự spawn reviewer.

### Bước D — Bảo chốt một gói quyết định, rồi khóa final

Giao chung: **(1) master424 đã sửa, (2) ledger424, (3) change log, (4) bảng ngoại lệ cần Bảo quyết định, (5) báo cáo kiểm và file hash**. Dữ liệu công ty/account giữ private; Git chỉ nhận hồ sơ sanitize.

Đề xuất mặc định: giữ đầy đủ424 dòng như mandate hiện tại. Các công ty chưa tìm được Page nhưng có website chính thức vẫn được giữ với định danh có bằng chứng, nêu giới hạn matching. Không bảo đảm93/93 sẽ match.

**Known-wrong chưa có replacement là điểm phải chốt chung:** nếu còn công ty đang bị ghép sai mà không tìm được exact local Page, không gọi master424 là sẵn sàng sạch lỗi. Codex giao một bảng duy nhất gồm công ty, vấn đề, định danh còn thiếu và phương án. Bảo có thể yêu cầu giữ chờ bổ sung hoặc duyệt một tập upload thu hẹp có liệt kê các dòng tạm giữ ngoài upload. Tập thu hẹp chỉ là phương án đề xuất, không tự làm thay mandate424; master424 luôn được bảo toàn. Không tự bỏ công ty để tăng tỷ lệ match, và không hỏi duyệt lẻ từng dòng.

Sau khi quyết định gói được phản ánh vào file, tạo **một CSV FINAL**, đặt revision/hash/row count và xác nhận chính file đó. Nếu quyết định làm đổi phạm vi file, Bảo xem kết quả cụ thể đã sửa trước upload. Không upload draft hai công ty hoặc file còn đang nghiên cứu.

### Bước E — một lần cập nhật, một vòng hậu kiểm đầy đủ

Chỉ sau khi có duyệt cụ thể cho final file và Discovery hiện có: xác minh target identity, saved filename/current state và các phụ thuộc sử dụng audience; cập nhật **đúng một lần** bằng CSV đã khóa. Nếu UI hiện chấp thuận Ads Agreement, cần xác nhận tại bước đó theo browser policy; không suy từ lần chấp thuận R5 sang Discovery. Không tạo audience thử/duplicate, xóa audience hoặc thay campaign.

Lưu receipt gồm file hash/count, thời điểm submit, success/readback và filename sau reload. Nếu thao tác lỗi hoặc kết quả mơ hồ, đọc lại trạng thái trước; không bấm submit lần hai để thử. Một lần upload là một lần submit thành công, không đồng nghĩa hoàn tất matching.

Theo [LinkedIn Help](https://www.linkedin.com/help/lms/answer/a423102), audience có thể cần tới48 giờ, hiếm khi lâu hơn. Sau submit:

- T+0: ghi nhận thành công/lưu file; chưa kết luận chất lượng từ số tức thì.
- Chốt một lượt hậu kiểm toàn bộ sau khi xử lý hoàn tất; mốc dự kiến T+48h. Nếu vẫn Building, T+72h chỉ đọc lại và ghi chậm xử lý, không upload lại. Đây là cadence đề xuất, chưa tạo lịch tự động.
- Capture đầy đủ matched/unmatched; đối chiếu với FINAL và ledger source. Rà mọi mapping thay đổi, mọi wrong finding cũ và các output mới chưa từng được xác minh; không chỉ nhìn badge Ready hoặc phần trăm match.
- Kết thúc bằng một báo cáo: đúng/sai/chưa đủ bằng chứng, residual unmatched, coverage và next disposition. Nếu vẫn lỗi, gom một diagnostic pack; không bắt đầu vòng sửa/upload lẻ mới. Support cho Discovery cần mandate riêng; không gửi tự động từ quyền Support có điều kiện của R5.

## 3. Điều kiện hoàn tất và quyền đang có

Plan hoàn tất khi các bước, đầu ra, giới hạn và điểm quyết định nói trên được ghi rõ và Bảo có thể duyệt phạm vi. **Lượt này chỉ lập plan, không bắt đầu nghiên cứu tổng thể hoặc upload.**

Lượt chuẩn bị tổng thể hoàn tất khi ledger424 đủ disposition, toàn93 mục được đối chiếu, mọi thay đổi có bằng chứng và gói ngoại lệ được giao chung. Unresolved có lý do được tính là kết thúc pass nghiên cứu, không tính là mapping đã sửa thành công.

Upload acceptance: file final cụ thể được duyệt, mọi ngoại lệ material có quyết định, cấu trúc/định danh qua kiểm và đúng target. Hậu kiểm acceptance: không còn known-wrong trong phạm vi được chấp nhận, output chưa xác minh giữ INSUFFICIENT_EVIDENCE; Ready không đủ để release. Chưa có mandate spend/enable/campaign attach hoặc quyết định budget.

Giữ công việc ở worktree riêng. Không commit/merge/push thêm trong lượt lập plan này. Checkpoint R5 và Master203 giữ nguyên, không trộn vào lần upload Discovery.

## 4. Anchor và docs impact

Đã đọc VY-CONTENT-ANCHOR1.0 và email VY-MAIL-USER-20261006. Plan chỉ xử lý identity/mapping; danh sách công ty đúng Page chưa chứng minh fit chuỗi cung ứng, quyền mua ERP hoặc segment/locale. Không tự loại tập đoàn lớn theo nhận định trong mail. Không tạo creative, ROI claim, case, CTA hoặc journey; các bề mặt này N/A trong plan. Fresh hash binding/review của plan ghi ở `single-upload-plan-review.json`; audience readiness vẫn CHANGES_REQUIRED/INSUFFICIENT_EVIDENCE.

DOCS_IMPACT_MAP reviewed: current status/build/readiness/S03 và owned progress được bổ sung notice liên kết plan này, ghi rõ PROPOSED/no new live action. Không sửa receipt/checkpoint lịch sử, budget, frozen core hoặc locale-adapter DEVELOPING/NOT_FROZEN.
