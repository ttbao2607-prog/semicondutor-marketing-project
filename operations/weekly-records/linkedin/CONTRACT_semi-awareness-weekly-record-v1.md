# Semiconductor — record tuần LinkedIn cho báo cáo stakeholder (contract v1)

Soạn 03/11/2026 theo chỉ đạo của Bảo (PO), bởi agent Claude ở repo Report
(`Review_Ga4_GooglAd_Weekly`). Người nhận: agent Claude theo dõi LinkedIn trong repo
`D:\Digiwin_Semiconducter_Workspace`. Tài liệu tự đủ ngữ cảnh: không cần đọc thêm repo Report.
Đây là yêu cầu định dạng, **không phải mandate live**: agent bên Semi chỉ đọc (read-only) tài
khoản LinkedIn theo mandate đọc hiện hành của Bảo; không Save/Launch/pause/enable, không đổi
budget, lịch, targeting, creative.

## 1. Vì sao cần record này

Bảo vận hành Paid Ads của Digiwin Vietnam (B2B ERP/MES/AIoT cho SME sản xuất) và mỗi thứ Tư
đồng bộ một "snapshot tuần" lên hai nơi cho stakeholder (quản lý Đài Loan và các bên liên quan):
một dashboard và một Google Sheet. Từ 03/11/2026 Bảo chỉ đạo đưa Semiconductor (Google Search +
LinkedIn) vào snapshot đó, kể cả số liệu trên dashboard. Repo Report chưa có đường thu LinkedIn
(không API, không collector). Bảo quyết: **agent bên Semi theo dõi LinkedIn và ghi record vào repo
Semi; agent bên Report lấy record đó làm nguồn báo cáo.** Hai agent không gọi nhau; cầu nối duy nhất
là file record + commit SHA mà Bảo chuyển.

## 2. Bên Report sẽ làm gì với record (để bạn hiểu mức chính xác cần)

- Ghim đúng file bằng đường dẫn + SHA-256 + git blob của commit bạn báo; đọc lại repo mỗi batch.
- Chép các con số sang một khối "Semiconductor awareness" riêng trên dashboard: theo tuần, theo
  treatment F1/F2 và tổng: impressions, clicks, CTR, reach/frequency (nếu có), kèm số ngày có
  delivery. Khối này **không cộng** vào số VN/TL, không vào lịch sử/Monthly/WoW.
- Đưa ra stakeholder **không có**: tiền (spend, budget, CPC/CPM kiểu tiền), danh sách audience,
  creative, ID tài khoản/campaign, URL tài khoản, PII, ảnh/DOM thô. Vì vậy **file record không được
  chứa các thứ này** (xem §6) — spend vẫn ghi trong tài liệu nội bộ của Semi như hiện nay, chỉ
  không ghi vào file record.
- Không được viết "winner/loser", "hiệu quả", "lead", "qualified" — record chỉ cung cấp số quan sát.

## 3. Kỳ và thời điểm

- Kỳ = tuần **Thứ Hai–Chủ Nhật**, múi giờ **Asia/Ho_Chi_Minh**, đã đóng ≥48 giờ. Lịch review là
  thứ Tư; kỳ gần nhất đủ điều kiện là tuần kết thúc Chủ Nhật trước đó.
- Dữ liệu phải **đọc với đúng khoảng ngày của kỳ** (date range của LinkedIn đặt đúng Mon–Sun).
  Không dùng số cộng dồn của cả chiến dịch hay cửa sổ khác kỳ (ví dụ cửa sổ 04/10–02/11 trong
  `STATUS_2026-11-02.md` KHÔNG dùng được làm số tuần). Nếu UI không cho đặt đúng khoảng ngày →
  ghi `unavailable`, đừng suy ra.
- `observed_at` không quá **24 giờ** trước khi bên Report nhận bàn giao đầu tiên.
- Lịch cụ thể:

| Batch (thứ Tư) | Kỳ record | Ghi chú |
|---|---|---|
| **04/11/2026** | 26/10–01/11 | Chỉ có **một ngày delivery (01/11, bắt đầu 07:00)**. Cần đọc đúng 01/11. Cho phép record gần như rỗng nhưng trung thực. Không kịp thì bên Report đăng trạng thái, số ghi "chưa có". |
| 11/11/2026 | 02/11–08/11 | Tuần vòng 1 kết thúc (lịch tới 06:45 08/11 giờ VN). Là tuần số đầu tiên đầy đủ. |
| 18/11/2026 | 09/11–15/11 | Còn lại nếu LinkedIn tiếp tục chạy. |

## 4. Vị trí, tên file, commit

- Đặt tại `operations/weekly-records/linkedin/` trong repo Semi (tạo thư mục nếu chưa có), tên
  `linkedin_<start>_<end>.json`, ví dụ `linkedin_2026-10-26_2026-11-01.json`.
- Một file mỗi kỳ. Sửa số đã commit = file mới có `supersedes` trỏ file/commit cũ, không ghi đè
  im lặng.
- Commit local trên nhánh Bảo chỉ định (không push GitHub khi chưa có lệnh). Báo lại cho Bảo:
  **đường dẫn + commit SHA đầy đủ 40 ký tự + SHA-256 của file**. Chạy documentation sync gate của
  repo Semi (đọc `DOCS_IMPACT_MAP.md` hoặc ghi "Docs impact reviewed: no canonical update required.").

## 5. Cấu trúc record (JSON, UTF-8)

```json
{
  "schema": "semi-awareness-weekly-record-v1",
  "channel": "linkedin",
  "period": {"start": "2026-10-26", "end": "2026-11-01", "timezone": "Asia/Ho_Chi_Minh"},
  "observed_at": "2026-11-04T08:30:00+07:00",
  "observer": "claude (repo Semi)",
  "collection": {
    "method": "linkedin_campaign_manager_ui_read",
    "date_range_applied": "2026-11-01..2026-11-01",
    "range_matches_period": false,
    "clicks_definition": "Clicks (tất cả lượt bấm, cột hiển thị mặc định; Bảo chọn 02/11 — không đổi sang landing-page clicks)",
    "ctr_definition": "total clicks / total impressions, tính lại, không lấy trung bình CTR dòng"
  },
  "delivery": {
    "state": "active",
    "first_delivery_at": "2026-11-01T07:00:00+07:00",
    "days_with_delivery_in_period": ["2026-11-01"],
    "days_eligible_in_period": ["2026-11-01"]
  },
  "units": [
    {
      "key": "f1",
      "label": "F1 (treatment cold EN, wave 1)",
      "impressions": null, "clicks": null, "ctr": null,
      "reach": null, "frequency": null,
      "read_status": "read | partial | unavailable",
      "unavailable": {"reach": "UI hiển thị '-' dù có impressions"}
    },
    {"key": "f2", "label": "F2 (treatment cold EN, wave 1)", "impressions": null, "clicks": null, "ctr": null, "reach": null, "frequency": null, "read_status": "unavailable", "unavailable": {}}
  ],
  "totals": {
    "impressions": null, "clicks": null, "ctr": null,
    "reach": null, "frequency": null,
    "reach_note": "chỉ điền nếu platform trả reach ở đúng cấp (ad set); không cộng reach của F1+F2"
  },
  "internal_flags": {
    "impression_ratio_over_3_to_1": null,
    "delivery_below_expected": null,
    "frequency_ge_2_with_reach": null
  },
  "limits": [
    "Ads 'Active' không phải đã duyệt.",
    "Khác biệt utm_source linkedin vs LinkedIn chưa xác minh (C1).",
    "Không phải lead, không phải so sánh hiệu quả."
  ],
  "evidence": {
    "internal_receipt": "operations/w1-w2/f1-f2-2026-10-29/pre-readback/<tên receipt nội bộ>.md",
    "note": "receipt có thể chứa chi tiết nhạy cảm — bên Report CHỈ ghim file record này, không chép receipt"
  },
  "supersedes": null
}
```

Quy ước giá trị:
- Số nguyên/số thực không dấu phân cách. `ctr` là tỷ lệ 0–1 (hoặc null). `frequency` null nếu `reach` null/0.
- **`null` = không đọc được hoặc chưa đọc; `0` chỉ khi đọc thành công và UI thực sự hiện 0.**
  Mỗi `null` phải có lý do trong `unavailable` hoặc `limits`. Không bao giờ đổi null thành 0.
- Nếu `range_matches_period` = `false` thì mọi số ở `units`/`totals` phải là `null` (hoặc ghi rõ
  khoảng ngày thực tế đã áp ở `date_range_applied` và bên Report sẽ quyết có dùng được không).
  Tuần 26/10–01/11 hợp lệ nếu bạn đặt range 01/11–01/11 vì trước 01/11 không có delivery;
  khi đó `range_matches_period` = `true` được phép nếu bạn ghi rõ ngày bắt đầu delivery và xác
  nhận các ngày 26–31/10 không có delivery (lịch chưa bắt đầu).
- `internal_flags` chỉ là cờ nội bộ cho Bảo (theo K4/K7/K8 trong `CRITERIA_DECISIONS.md`), **không
  công bố**; ghi `null` nếu không đủ dữ liệu để đánh giá. Không ghi số tiền để giải thích cờ.
- Tùy chọn: `ga4_sessions` trong từng unit `{ "value": int|null, "definition": "Session campaign =
  fdi_f1_en_cold_wave01, stream website, processed, đúng kỳ" }` nếu bạn đọc được GA4; để vắng nếu
  không. Không suy sessions từ clicks.

## 6. Cấm trong file record

Tiền (spend, budget, CPC/CPM/CPL), danh sách công ty/audience (kể cả tên R5-52, tên audience, số
thành viên audience), nội dung/ảnh creative, ID tài khoản/campaign/ad, URL Campaign Manager,
đường dẫn máy ngoài `operations/...` tương đối, PII, secret, ảnh/DOM thô. Nếu cần nhắc, dùng nhãn
trung tính (F1, F2). Tên treatment F1/F2 là nhãn nghiệp vụ, được phép.

## 7. Việc bạn KHÔNG làm

- Không sửa tài khoản LinkedIn, không bật RMK, không quyết W2 hay đổi `utm_source`.
- Không tạo lịch tự động; Bảo mở/ủy quyền việc đọc như hiện nay.
- Không đưa kết luận hiệu quả; không so F1/F2 nếu impressions lệch >3:1 (K4).
- Không viết vào repo Report. Bên Report chỉ nhận qua commit SHA Bảo chuyển.

## 8. Việc bên Report làm sau khi nhận SHA

Đọc file bằng `git show <sha>:<path>`, kiểm hash, kiểm kỳ/độ mới/quy tắc null, đưa vào khối
Semiconductor trên dashboard + hai hàng trạng thái ở Sheet (không thêm tab), tạo hai bản xem
trước và chỉ publish sau consent của Bảo. Record thiếu/cũ/không hợp lệ → số hiển thị là "chưa có
trong kỳ này" (không phải 0), phần trạng thái vẫn đăng.
