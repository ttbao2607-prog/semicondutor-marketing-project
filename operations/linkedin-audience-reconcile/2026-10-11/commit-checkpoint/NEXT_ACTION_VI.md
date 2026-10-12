# Bảo nên xử lý tệp LinkedIn thế nào?

**Khuyến nghị: chốt hồ sơ audit, giữ Discovery ở CHANGES_REQUIRED, sửa tệp rồi mới upload lại một lần.** Chưa chấp nhận tệp hiện tại để dùng chạy ads. Chưa có bản CSV sửa mới được chứng nhận; upload lại nguyên 409 không sửa được 36 cặp sai đã có bằng chứng.

Đã quan sát/nghiên cứu đủ 199 cặp: **30 đúng, 36 sai, 133 đã làm nhưng thiếu bằng chứng**. Kết luận áp dụng ma trận 10/10 và Page quan sát 11/10; lần đọc exact roster cuối bị timeout, nên chưa chứng minh roster hiện hành giống bản pin. Audit 199 matched không bao phủ toàn bộ 409 dòng đầu vào hay 93 unmatched.

## Một vòng sửa có kiểm soát

1. **Đọc lại roster hiện hành:** so sánh từng công ty đầu vào và Page với ma trận đã pin. Giữ evidence cũ cho cặp không đổi; kiểm thêm các cặp thay đổi.
2. **Sửa 36 cặp sai:** join về đúng source row, kiểm domain/pháp nhân/địa chỉ và Page đúng đơn vị tại Việt Nam. Dùng canonical Company Page URL đã chứng minh alias/redirect thuộc đúng numeric Page; numeric ID là khóa audit, không tự chọn làm định dạng upload tối ưu. Nếu không có Page đúng, ghi ngoại lệ và đề xuất Bảo quyết định giữ/cách ly. Không tự trừ 36 khỏi 409: matched pairs không phải partition của source rows.
3. **Đóng các gap theo nhóm:** ưu tiên 15 khoảng trống tập đoàn/nhà máy và 6 Page corroboration nếu có nguồn để đóng nhanh; 112 trường hợp còn lại cần tên pháp nhân, domain, địa chỉ hoặc nguồn công ty/cơ quan. Thiếu bằng chứng vẫn là unresolved, không tự ghi sai hay đúng. Chốt decision unit và hoạt động phù hợp chuỗi cung ứng bán dẫn/điện tử; identity đúng không chứng minh customer fit hoặc quyền mua ERP.
4. **Lập một candidate hợp nhất:** bảng thay đổi theo source row, exact replacement/exception, coverage đối với toàn bộ source được chọn, số dòng và hash CSV, kiểm bảo toàn 11 dòng/12 cell identifier đã cải thiện. Phạm vi chưa được kiểm trong 409/unmatched phải ghi rõ trước quyết định giữ hoặc loại; không gọi 30 cặp đúng là một audience sẵn sàng chạy.
5. **Sau khi Bảo chốt scope/file và cấp upload mandate:** cập nhật existing Discovery một lần, đọc lại filename/status thực, đợi xử lý và hậu kiểm roster mới. Quan sát trạng thái platform trả về; không đặt “phải Building” làm tiêu chí thành công. Tiêu chí là source đúng, các cặp sai đã sửa/ngoại lệ được xử lý rõ và output mới được đối chiếu. Readiness về persona/locale/reach/creative/journey là gate riêng.

## Week2 / R5 giữ riêng

Snapshot trước trong ngày cho R5 là 52 matched/0 unmatched; vòng Discovery không phải full identity audit của R5. Forecast cấu hình English + Vietnam + functions + seniorities khoảng 460, cấu hình Vietnamese dưới 300; đây không là buyer-fit/FDI/locale hay quyền chạy campaign. R5 có thể là phương án dự phòng để Bảo cân nhắc sau các gate riêng, chưa tự chuyển campaign sang R5 hoặc upload lại R5.

## Căn cứ platform được kiểm 11/10

[LinkedIn company-list guidance](https://www.linkedin.com/help/linkedin/answer/a9419037) khuyên thêm website/Company Page URL; ưu tiên URL có company name thay numeric ID để cải thiện matching. Identifier tốt hỗ trợ matching, không bảo đảm mọi output sẽ đúng.

[LinkedIn troubleshooting](https://www.linkedin.com/help/linkedin/answer/a420864/troubleshooting-tips-for-linkedin-matched-audiences?lang=en) giải thích Building là đang xử lý matching, thường tới 48 giờ và đôi khi lâu hơn; hướng dẫn retry sau hơn 72 giờ thuộc trường hợp bị kẹt Building. Snapshot Discovery đã Ready có lỗi identity là bài toán khác: phải sửa dữ liệu và hậu kiểm, không dùng retry nguyên tệp như bằng chứng chất lượng.

**Discrepancy cần giữ:** help page hiện ghi company-list upload tối thiểu 300 rows, trong khi account evidence cũ cho thấy tệp R5-52 được nhận và có output. Chưa giải thích được khác biệt; không phủ nhận observed R5 và không cam kết tệp 30/52 dòng mới sẽ upload được. Kiểm template/current-account route thực trước candidate upload. Quy tắc 300 member accounts sau targeting là khái niệm riêng với số company rows.

## Mốc lưu hồ sơ

Bảo đã cấp quyền commit. **Containing commit** lưu audit và khuyến nghị trên `slice/linkedin-audience-reconcile-2026-10-11`, chỉ local, chưa push/merge main. Các dòng “uncommitted/no Git mutation” trong receipt audit trước là trạng thái lúc thu bằng chứng, được giữ nguyên. Việc commit hồ sơ không nâng Discovery lên PASS và không đổi source CSV/live audience. [Audit gốc](../full-identity-audit/README.md) giữ 30/36/133 và các gap; [contract](PLAN.md) quy định bằng chứng chốt Git.

Docs impact reviewed: cập nhật scoped commit/next-action notice ở 7 entrypoints; body và receipts lịch sử giữ nguyên. Anchor/internal-document review riêng, không là generation, full-journey hay live acceptance.
