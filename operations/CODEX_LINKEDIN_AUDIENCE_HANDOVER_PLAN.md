> **Research live UI · 2026-10-05:** Exact Company List Ready/80%; Details và refreshed list có **753,731 members**, 117 Companies, tab Unmatched 86. VN + English profile + Engineering/Operations/IT/QA = **4,800+**; thêm Manager/Director/VP/CXO = **780** ở saved definition `RSCH-CL-VN-LEAD-20261005` (persistence verified). Cùng filters + Vietnamese profile báo too small. Size gate discovery đã xác minh; mapping quality/denominator và production decisions vẫn OPEN. Retargeting menu không có Carousel riêng; warm RMK chưa đủ evidence. Chỉ lưu Saved Audience; Exit without saving ad set, không publish/enable/spend. [Receipt](LinkedIn_Audience_Ready_Research_2026-10-05.md). Snapshot cropped-size phía dưới là lịch sử trước research.

> **Company List Ready · 2026-10-05:** Bảo xác nhận đúng `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`; ảnh cung cấp hiển thị **Ready / match rate 80% / Company List / Owned**, Active ad sets `-`. Exact audience count bị cắt nên chưa xác minh reachable size hoặc gán `AUD_STATUS_READY_VIABLE`. Điều kiện chờ Building của đúng tệp này đã gỡ; engagement RMK `LI-AUD-P1-ENGAGED-30D`, targeting/filtered reach, attachment, budget và live vẫn có gate riêng. Các snapshot Building ngày 2026-09-30 bên dưới là lịch sử, được thay thế cho current Company List status bởi [evidence và bảng task](LinkedIn_Company_List_Ready_Update_2026-10-05.md).

# KẾ HOẠCH BÀN GIAO THỰC THI KHÁM PHÁ MATCHED AUDIENCE TRÊN LINKEDIN
# (CODEX HANDOFF SPECIFICATION: LINKEDIN COMPANY LIST MATCH DISCOVERY)

**Người đệ trình:** Bảo (Product Owner / Paid Project Lead)  
**Đơn vị thực thi:** Codex Automation Agent (Browser/Account Execution)  
**Nhánh Git làm việc:** `slice/crm-audience-discovery`  
**Ngày ban hành:** 2026-09-30  
**Ranh giới vận hành (Trust Boundary):** **CHẾ ĐỘ THỬ NGHIỆM VÀ ĐỌC DỮ LIỆU ĐO LƯỜNG (DRAFT & READ-ONLY METRICS). TUYỆT ĐỐI KHÔNG TẠO CHIẾN DỊCH LIVE, KHÔNG PUBLISH QUẢNG CÁO, KHÔNG KÍCH HOẠT NGÂN SÁCH (ZERO SPEND).**

---

## 1. Mục Đích & Nguyên Tắc Cách Ly Dữ Liệu (Data Isolation Protocol)

### 1.1. Mục Đích
Kiểm chứng thực nghiệm trên LinkedIn Campaign Manager xem danh sách **424 doanh nghiệp pháp nhân đã làm sạch** (thuộc ngành linh kiện điện tử, quang điện và phụ trợ bán dẫn tại Việt Nam) có đạt tỷ lệ khớp (Match Rate) và quy mô thành viên khả dụng (Audience Size) đáp ứng ngưỡng sàn tối thiểu (>= 300 members) để phân phối quảng cáo B2B hay không.

### 1.2. Nguyên Tắc Bảo Vệ Dữ Liệu & Loại Bỏ Tính Chất CRM (Zero CRM Leakage)
1. **Cách ly 100% hai tệp CRM gốc:** Hai tệp CRM nội bộ (`VN_Contact_Linh kiện điện tử.csv` và `CN-Contact-Điện tử Bán dẫn.csv`) nằm hoàn toàn ngoài repository dự án. Tuyệt đối không copy, commit hay dẫn link trực tiếp vào git.
2. **Triệt tiêu hoàn toàn thuộc tính bán hàng & PII:**
   - Đã loại bỏ 100% các trường CRM nội bộ: *săn đón, SDR/MDR, Opps Stage, nhật ký ngày, xếp hạng khách hàng, nguồn mua*.
   - Đã loại bỏ 100% dữ liệu định danh cá nhân (PII): *họ tên người liên hệ, số điện thoại cá nhân, địa chỉ email cá nhân*.
   - Đã loại trừ 4 đại tập đoàn theo đúng giả thuyết vận hành D1: `Intel Corporation`, `Samsung Electronics`, `Amkor Technology`, `Hana Micron`.
3. **Tài nguyên đầu vào duy nhất cho Codex:**
   - File CSV trung tính cấp pháp nhân được sinh ra bởi script [`scripts/sanitize_linkedin_company_list.py`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/scripts/sanitize_linkedin_company_list.py):
     `D:\Digiwin_Semiconductor_Audit_Worktree\private\linkedin_company_list_sanitized.csv`
   - Đây là schema nguồn đã sanitize gồm 3 cột; không đồng nhất schema này với template CSV upload hiện hành của LinkedIn:
     * `companyname`: Tên đăng ký kinh doanh chính thức của doanh nghiệp tại Việt Nam.
     * `country`: `Vietnam`
     * `city`: Tỉnh / Thành phố đặt nhà máy hoặc văn phòng (TP.HCM, Hà Nội, Bắc Ninh, Đồng Nai, Hải Phòng...).
   - Template Company List hiện hành có 10 header theo đúng thứ tự: `companyname,companywebsite,companyemaildomain,linkedincompanypageurl,stocksymbol,industry,city,state,companycountry,zipcode`. Giữ file nguồn nguyên trạng; chỉ tạo bản upload tương thích khi Campaign Manager yêu cầu header template chính xác.

---

## 2. Quy Trình Thao Tác Chi Tiết Cho Codex Agent (Execution Steps)

Codex agent thực hiện tuần tự theo 6 bước có kiểm soát sau trên LinkedIn Campaign Manager:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│              QUY TRÌNH THỰC THI KIỂM CHỨNG TỆP ĐỐI TƯỢNG (DISCOVERY WORKFLOW)           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Bước 1: Đăng nhập LinkedIn Campaign Manager (Tài khoản Digiwin được cấp quyền)         │
│ Bước 2: Điều hướng vào Plan (Kế hoạch) ──> Audiences (Đối tượng)                       │
│ Bước 3: Click 'Create audience' ──> Chọn 'Company / Account' ──> 'Upload a list'       │
│ Bước 4: Đặt tên tệp: TEST-AUD-COMPANY-LIST-DISCOVERY-202610                            │
│ Bước 5: Upload bản template-compatible, giữ nguyên 424 dòng từ file nguồn              │
│ Bước 6: Quan sát trạng thái xử lý và ghi nhận bằng chứng đo lường                      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Hướng dẫn chi tiết từng bước:
* **Bước 1 — Xác thực tài khoản:** Đăng nhập vào LinkedIn Campaign Manager bằng tài khoản được ủy quyền. Kiểm tra quyền truy cập vào đúng Ad Account của Digiwin.
* **Bước 2 — Điều hướng đến Trình quản lý Đối tượng:** 
  - Tại thanh menu bên trái, nhấp vào **Plan** (hoặc **Analyze**) -> chọn **Audiences**.
* **Bước 3 — Khởi tạo tệp Company List:**
  - Nhấp vào nút **Create audience** (Tạo đối tượng) ở góc trên bên phải.
  - Chọn danh mục: **Company / Account** (Công ty / Tài khoản doanh nghiệp) -> chọn phương thức **Upload a list** (Tải lên danh sách).
* **Bước 4 — Thiết lập định danh:**
  - Audience Name (Tên đối tượng): Nhập chính xác chuỗi:
    `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`
* **Bước 5 — Tải lên danh sách:**
  - File nguồn: `D:\Digiwin_Semiconductor_Audit_Worktree\private\linkedin_company_list_sanitized.csv`. Nếu UI từ chối header, dùng bản dẫn xuất riêng tư `D:\Digiwin_Semiconductor_Audit_Worktree\private\linkedin_company_list_sanitized_linkedin_template.csv`; bản này giữ nguyên 424 dòng và các giá trị tên/thành phố, ánh xạ `country=Vietnam` sang `companycountry=VN`, để trống các trường không có trong nguồn. Không bổ sung website/domain hoặc company rows.
  - Preflight trực tiếp ngày 2026-09-30 xác nhận file nguồn 3 cột bị UI từ chối vì header không trùng template; bản 10 cột nêu trên được UI chấp nhận ở trạng thái `Processing complete. Company list ready for upload.` Không suy ra audience đã được tạo từ trạng thái tiền upload này.
  - UI hiện hiển thị hướng dẫn `Upload between 10,000 - 300,000 companies`; [LinkedIn Help](https://www.linkedin.com/help/lms/answer/a423102) nêu tối thiểu 300 dòng và khuyến nghị 1.000+ công ty. Với 424 dòng, ngưỡng tối thiểu trong Help được đáp ứng nhưng còn khác biệt với dòng hướng dẫn trên UI; ghi nhận đúng nếu server từ chối.
  - Nhấp **Agree & Upload** (Đồng ý & Tải lên).
  - Campaign Manager ghi rõ thao tác này đồng ý với **Ads Agreement**. Chỉ thực hiện sau xác nhận action-time riêng của Bảo.
* **Bước 6 — Đọc dữ liệu và lưu bằng chứng:**
  - Sau khi upload, tệp sẽ xuất hiện trong danh sách Audiences với trạng thái ban đầu là `Building` hoặc `Ready`.
  - Đọc và trích xuất các chỉ số hiển thị trên giao diện:
    1. Trạng thái tệp (Status)
    2. Số lượng công ty khớp được (Matched Companies / Total Uploaded)
    3. Tỷ lệ khớp ước tính (Match Rate %)
    4. Quy mô thành viên hoạt động (Target Audience Size / Active Members)
  - Chụp ảnh màn hình làm bằng chứng (Mask/che mờ tên tài khoản cá nhân hoặc thẻ tín dụng nếu xuất hiện).
  - **Kết quả kiểm tra sau upload (2026-09-30 14:16 UTC+7):** Campaign Manager hiển thị toast `Your audience has been successfully created.` và dòng `TEST-AUD-COMPANY-LIST-DISCOVERY-202610` với `Status=Building`, `Source=Company List`, `Match rate=-`, `Active ad sets=-`, `Ownership=Owned`, `Last audience count=-`. Gán `AUD_STATUS_PROCESSING_LATENCY`; chưa có số liệu match/size để kết luận. Dòng này không được chọn và nút `Add to ad set` đang disabled. Không có campaign/ad set nào được tạo hoặc sửa, không có spend. Xem receipt tại `operations/CODEX_LINKEDIN_AUDIENCE_DISCOVERY_RECEIPT.md`.

---

## 3. Tiêu Chí Phân Loại Trạng Thái Định Danh (Deterministic Status Criteria)

Sau khi hoàn tất quy trình khám phá, Codex **bắt buộc phải trả về chính xác 1 trong 5 mã trạng thái định danh dưới đây**, kèm bằng chứng cụ thể. Tuyệt đối không đưa ra các nhận xét định tính mơ hồ ("tệp khá tốt", "có vẻ khớp", "chưa rõ ràng"):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG MÃ TRẠNG THÁI NGHIỆM THU ĐỊNH DANH (STATUS ENUM)             │
├───────────────────────────────────┬──────────────────────┬─────────────────────────────┤
│ Mã Trạng Thái (Deterministic Code)│ Điều Kiện Kỹ Thuật   │ Ý Nghĩa Vận Hành Cho PO     │
├───────────────────────────────────┼──────────────────────┼─────────────────────────────┤
│ 1. AUD_STATUS_READY_VIABLE        │ Status = Ready;      │ ĐỦ ĐIỀU KIỆN SÀN: Có thể    │
│                                   │ Size >= 300 members  │ phân phối quảng cáo độc lập.│
├───────────────────────────────────┼──────────────────────┼─────────────────────────────┤
│ 2. AUD_STATUS_READY_SUB_THRESHOLD │ Status = Ready;      │ DƯỚI NGƯỠNG SÀN: Không chạy │
│                                   │ Size < 300 members   │ riêng lẻ, phải ghép Job.    │
├───────────────────────────────────┼──────────────────────┼─────────────────────────────┤
│ 3. AUD_STATUS_PROCESSING_LATENCY  │ Upload OK;           │ ĐANG XỬ LÝ (24–48H):        │
│                                   │ Status = Building    │ Đặt lịch kiểm tra lại sau.  │
├───────────────────────────────────┼──────────────────────┼─────────────────────────────┤
│ 4. AUD_STATUS_UPLOAD_REJECTED     │ File bị từ chối;     │ LỖI ĐỊNH DẠNG: Cần chuẩn    │
│                                   │ Báo lỗi cấu trúc     │ hóa lại schema/bổ sung web. │
├───────────────────────────────────┼──────────────────────┼─────────────────────────────┤
│ 5. AUD_STATUS_ACCESS_BLOCKED      │ Thiếu quyền / 2FA;   │ CHẶN TRUY CẬP: Trả ticket   │
│                                   │ Giao diện bị khóa    │ để Bảo cấp quyền tài khoản. │
└───────────────────────────────────┴──────────────────────┴─────────────────────────────┘
```

### Quy chuẩn chi tiết từng mã:

#### 1. `AUD_STATUS_READY_VIABLE`
* **Điều kiện kích hoạt:** 
  - Trạng thái tệp trên LinkedIn Campaign Manager chuyển sang **`Ready`**.
  - Quy mô đối tượng khả dụng (**Target Audience Size**) hiển thị số liệu cụ thể và đạt **>= 300 active members** (ngưỡng tối thiểu của LinkedIn để bắt đầu phân phối quảng cáo).
* **Bằng chứng bắt buộc:** Ảnh chụp màn hình dòng đối tượng hiển thị rõ: Tên tệp `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`, Status `Ready`, và cột `Audience size`.
* **Hành động tiếp theo của PO:** Tệp đạt chuẩn khả thi cao; Bảo sẽ quyết định tích hợp tệp này vào Campaign `LI-CMP-FDI-SEGMENT` hoặc `LI-CMP-DOMESTIC-SEGMENT`.

#### 2. `AUD_STATUS_READY_SUB_THRESHOLD`
* **Điều kiện kích hoạt:**
  - Trạng thái tệp chuyển sang **`Ready`**.
  - Quy mô đối tượng hiển thị cảnh báo **`< 300`** hoặc *"Audience too small to target alone"* (do số lượng nhân sự đăng ký trên LinkedIn của các nhà máy này chưa đủ ngưỡng kích hoạt phân phối độc lập).
* **Bằng chứng bắt buộc:** Ảnh chụp màn hình dòng đối tượng với nhãn cảnh báo `< 300`.
* **Hành động tiếp theo của PO:** Bảo lưu danh sách này làm lớp phủ ưu tiên (Exclusion hoặc Retargeting); chiến dịch chính sẽ tiếp tục nhắm mục tiêu theo *Ngành (Industry: Electronic Manufacturing) + Chức danh (Job Function: Operations / Engineering / IT)* để đảm bảo độ phủ.

#### 3. `AUD_STATUS_PROCESSING_LATENCY`
* **Điều kiện kích hoạt:**
  - File tải lên thành công, không phát sinh lỗi validation của LinkedIn.
  - Cột trạng thái hiển thị **`Building`** hoặc **`Updating`** kèm thông báo LinkedIn cần thời gian đối chiếu (thường từ 24 đến 48 giờ đối với Company List).
* **Bằng chứng bắt buộc:** Ảnh chụp màn hình thông báo tải lên thành công và timestamp ghi nhận trạng thái `Building`.
* **Hành động tiếp theo của PO:** Không đưa ra kết luận vội vã; thiết lập lịch kiểm tra lại (Checkback reminder) sau 24 giờ để cập nhật số liệu chính thức.

#### 4. `AUD_STATUS_UPLOAD_REJECTED`
* **Điều kiện kích hoạt:**
  - LinkedIn từ chối file ngay tại bước upload (ví dụ: thiếu số lượng dòng tối thiểu, sai định dạng header, hoặc lỗi ký tự UTF-8).
* **Bằng chứng bắt buộc:** Ảnh chụp màn hình thông báo lỗi chi tiết (Error dialog / text).
* **Hành động tiếp theo của PO:** Bổ sung thêm trường `companydomain` (website công ty) cho top 100 doanh nghiệp lớn để tăng khả năng nhận diện của thuật toán LinkedIn.

#### 5. `AUD_STATUS_ACCESS_BLOCKED`
* **Điều kiện kích hoạt:**
  - Agent không thể mở trang Audiences do tài khoản thiếu vai trò *Campaign Manager* / *Account Admin*, hoặc gặp rào cản xác thực 2 lớp (2FA) / Captcha.
* **Bằng chứng bắt buộc:** Ảnh chụp màn hình thông báo từ chối truy cập hoặc màn hình yêu cầu xác thực.
* **Hành động tiếp theo của PO:** Bảo làm việc với Quản trị viên cấp cao để cấp quyền hoặc thực hiện phê duyệt phiên đăng nhập.

---

## 4. Biên Bản Bàn Giao & Mẫu Báo Cáo Nghiệm Thu (Evidence Receipt Template)

Sau khi Codex thực thi xong, Codex phải tạo file báo cáo nghiệm thu tại đường dẫn:  
`operations/CODEX_LINKEDIN_AUDIENCE_DISCOVERY_RECEIPT.md` theo đúng cấu trúc sau:

```markdown
# BIÊN BẢN NGHIỆM THU KHÁM PHÁ LINKEDIN MATCHED AUDIENCE

- **Thời điểm kiểm tra (Timestamp):** [YYYY-MM-DD HH:MM UTC+7]
- **Tài khoản Campaign Manager:** [Tên account hoặc `không ghi nhận`; không ghi ID]
- **Tên tệp đối tượng kiểm chứng:** `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`
- **Mã Trạng Thái Kết Luận (Deterministic Status):** `[CHỌN 1 TRONG 5 MÃ Ở MỤC 3]`

### Số Liệu Đo Lường Thực Tế:
- Tổng số công ty tải lên: 424
- Số công ty khớp thành công (Matched Companies): [Số lượng hoặc N/A]
- Tỷ lệ khớp hiển thị (Match Rate): [Tỷ lệ % hoặc N/A]
- Quy mô thành viên khả dụng (Target Audience Size): [Số lượng cụ thể hoặc < 300]
- Trạng thái hiển thị (Displayed Status): [Ready / Building / Error]

### Bằng Chứng Đo Lường (Evidence):
- File ảnh chụp màn hình lưu tại: `outputs/evidence/linkedin_audience_discovery_[timestamp].jpg` (nếu được lưu; nếu không, nêu rõ bằng chứng quan sát và hạn chế)
- Ghi chú kỹ thuật: [Mô tả trung thực những gì quan sát thấy trên màn hình]
```

---

## 5. Ranh Giới Nghiêm Ngặt Dành Cho Codex (Strict Prohibitions)
1. **CẤM** bấm nút "Create campaign" hoặc gắn tệp này vào bất kỳ chiến dịch nào đang chạy.
2. **CẤM** nhập thông tin thanh toán, thẻ tín dụng, hoặc kích hoạt ngân sách.
3. **CẤM** xuất hoặc commit file chứa thông tin chi tiết các công ty trở lại vào Git public repository.
4. **CẤM** tự ý suy diễn hoặc kết luận quy mô thị trường khi tệp còn ở trạng thái `Building`.
