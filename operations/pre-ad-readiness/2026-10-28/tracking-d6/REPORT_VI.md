# Theo plan đã duyệt — tracking inventory và bước tiếp

## Trả lời Bảo: plan có gì?

**Có ngân sách và cadence review; không phải yêu cầu duyệt lại từ đầu.** Dùng đúng Package v2 đã gửi, nguồn Git c91633dd; proposal blob SHA256 3eea25db215e66cd7e12800c4951443cdebce559f2db8595953394ae7ad95de6 khớp delivery manifest. [Bản đọc của đúng proposal đã giao](APPROVED_DELIVERY_PROPOSAL.md), chỉ chuẩn hóa xuống dòng; [binding](SOURCE_BINDING.json). Current checkout proposal MD/HTML khác bytes manifest, nên không suy nó là exact ZIP; dùng delivery Git object đối chiếu. Không thay package đã gửi.

| Đã ghi trong plan / PO record | Áp dụng |
|---|---|
| Trần 11,7 triệu media chưa thuế | Đã duyệt theo Bảo; không hỏi duyệt lại |
| Đợt LinkedIn đầu 5,6 triệu | Bắt đầu một nhóm phù hợp, vài mẫu đại diện; R5 English/P1/P2 là selected set hiện hành |
| Giữ lại 6,1 triệu trong cùng tổng | Gồm tối đa5,6 triệu LinkedIn tiếp theo + tối đa0,5 triệu Search; không tự dùng hết hoặc cộng ngoài tổng |
| Tuần1 theo plan, review cuối tuần; tuần2 theo data matrix | Đã có cadence, không xin lại |
| Chi dashboard; kế toán xử lý thuế/thanh toán | Giữ đơn vị tài khoản, không tự tạo FX |
| 400.000đ/ngày ×14 ngày | Có trong nền Phase1 dưới nhãn tham chiếu; PO weekly record nói rõ không là lịch live/final USD đã chọn |
| Bắt đầu từ tháng11 | Có chỉ đạo hiện hành; chưa riêng ngày01/11. Proposal giao không có calendar start/end hoặc daily USD |

Workbook giao `Theo_doi_paid_ads.xlsx` khớp manifest SHA256 eb8de3fff09f8acf6e5b2ef22dc94a42f2cde2c669854e6c6deba9fd4e319aa7. Hai sheet Review tuan/Nhat ky: Review tuan!B6=11700000, B7=5600000; D9 ghi review cuối tuần. Nhat ky!A7:B7 là header Từ ngày/Đến ngày, không là lịch đã nhập. [Đọc workbook](APPROVED_WORKBOOK_READ.json); không sửa/recalculate workbook.

**Điều chỉnh cách hỏi:** câu hỏi daily USD/calendar trước khi rà exact package là quá sớm. Bảo đã chỉ đạo theo plan; ngân sách/cadence trên là authority hiện hành. Chỉ khi dựng lịch thực cần đề xuất thông số dashboard phù hợp envelope, currency/minimum và actual forecast, rồi trình các trường cụ thể chưa có; không mở lại duyệt tổng ngân sách, cơ cấu hoặc hỏi một D6 chung chung. Không coi sự im lặng hay budget probe10USD/ngày là production approval.

## Tracking — evidence mới

| Surface | Observed | Implication / giới hạn |
|---|---|---|
| Reader P1 QA reload với t/lang+UTM | DOM chỉ external LadiPage SDK; 0 form. Network có a.ladipage.com/event, không thấy GTM/GA4/LinkedIn requests trong bounded window; reader buffer không truncated | Native LadiPage telemetry có hoạt động; không nói toàn trang không đo gì. Chưa có proof GA4 reader sessions/engagement hoặc website audience. Negative chỉ áp window đã kiểm |
| CTA reader→contact-vn | Actual destination không query; referrer chỉ origin solutions.digiwin.com.vn | Current URL handoff bỏ UTM, không giữ treatment/creative metadata qua URL. Chưa kiểm cookies/linker/CRM attribution, không khẳng định mất mọi attribution của mọi session |
| contact-vn | GTM-PC6FVTMZ + G-MV5QWN0XVM, observed GA4 page_view và response204; LinkedIn Insight scripts/requests, Meta/Zalo scripts cũng có | Đích contact là hệ tracking main website khác paid-LadiPage; không gộp hai property. Không submit form, không kiểm form-success/CRM. Contact event buffer truncated: không có completeness/dedup claim |
| Paid VN GTM | GTM-NGT54TM9, Version51 Live/Latest;71tags/63triggers/37variables; workspace0changes | Khớp snapshot three-route trước. Chưa đọc lại nội dung từng tag/trigger; container hiện có không chứng minh new reader đã cài nó |
| GTM tab có sẵn | Đang ở container Thailand NLBMPVS2/workspace khác | Loại khỏi evidence VN; không sửa tab/workspace đó |

[BROWSER_INVENTORY.json](BROWSER_INVENTORY.json) chỉ lưu hosts/paths, event names, public measurement IDs và query-key names; không cookies, headers, device/user identifiers hoặc raw request body. Không thay tag/container/settings/consent/form/ad. Browser CDP Network.disable bị runtime từ chối khi xử lý paused document response; đã đóng owned observed tab để detach instrumentation, đóng owned GTM tab; tab người dùng giữ nguyên. Không dùng Preview/Submit/lead test.

## Next action cụ thể

**Ưu tiên chuẩn bị bản sửa đo lường reader trong hạ tầng hiện có, để Bảo review đúng diff trước khi publish.** Chưa có mutation authority cho tracking trong lượt inventory này.

1. Giữ UTM nguồn từ ad khi qua contact: allowlist utm_source/medium/campaign/content/term, không tự đổi thành campaign nội bộ, không thêm PII/company/cohort. Target origin/path contact-vn giữ đã duyệt. Đây là proposed bounded link patch, chưa áp.
2. Chọn measurement owner cho reader trong hệ hiện có: paid VN GTM-NGT54TM9/GA4 G-20TL63SYLQ là reuse candidate theo historical route contract; contact hiện dùng GTM-PC6FVTMZ/G-MV5QWN0XVM. Kiểm config/consent/collision cụ thể trước đề xuất loader, không cài cả hai container. Giữ page_view do global tag sở hữu; không phát inline page_view hoặc bịa lead success.
3. Trước bật GTM paid trên route mới, recheck text-copy All Pages listener và exact-route exclusion. Version51 chỉ chứng minh published state; old three-route exclusion không tự bao reader mới. Chuẩn bị diff route-scoped để tránh đưa copied text vào analytics, không copy nguyên config cho toàn site.
4. Nếu cần section reading metrics cho chỉ số plan, dùng lại section_view/section_engagement_time theo contract khi owner được inventory; bind treatment/locale/readiness mapping đã verify. Không suy old three-page initializer áp lên reader hoặc tạo event taxonomy/CTA conversion mới. Website tracking phục vụ reader progression; không cần ép website audience cho native ad-engagement RMK hiện hành.
5. Sau bản sửa được duyệt: verify real network payload minimal, một page_view owner, preserved UTM trên contact, correct properties, no duplicate/copy-content dispatch; consent scope được ghi đúng. Form/lead submission chỉ khi có scope riêng.

D6 triển khai theo plan: cold Brand awareness/Single image, R5 VN English, P1/P2 selected source; cadence weekly như đã duyệt. Mức daily/currency và ngày bắt đầu cần đề xuất cụ thể khi chuẩn bị saved paused build, không phải xin lại toàn plan. Expansion/LAN off là observed scoped R5 config; production placement (Feed/Right Rail) và bidding phải đọc lại exact build, không kế thừa probe mặc định. RMK chỉ từ chính ads mới khi pool đủ điều kiện; Search là tùy chọn trong cap, không chặn cold.

## URL draft để review, chưa áp vào ad

- P1 cold: https://solutions.digiwin.com.vn/semiconductor-case-reader?t=P1&lang=en&utm_source=linkedin&utm_medium=paid_social&utm_campaign=fdi_p1_en_cold_wave01&utm_content=b22_cold_v1
- P2 cold: https://solutions.digiwin.com.vn/semiconductor-case-reader?t=P2&lang=en&utm_source=linkedin&utm_medium=paid_social&utm_campaign=fdi_p2_en_cold_wave01&utm_content=b25_cold_v1

Wave01/creative v1 là nhãn proposed cho build, không actual ad ID; source artwork revision vẫn pinned theo PO_CHOICE. RMK dùng stage rmk và role explain/proof tương ứng khi set được chọn, không dùng cold cho mọi click.

Execution SUCCESS cho bounded inventory/source reconciliation; measurement readiness PARTIAL/CHANGES_REQUIRED, D6 plan authority recorded/execution fields open; independent audit NOT_RUN. Docs impact reviewed: readiness C09/C10 và D6/current entrypoints cập nhật evidence này. Chưa commit/push; không sửa creative/runtime hay tạo ad/launch trong lượt này. CTA changes trước vẫn working after ea3d612d, không bị rollback.
