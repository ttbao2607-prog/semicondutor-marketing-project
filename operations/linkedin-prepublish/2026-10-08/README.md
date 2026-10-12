# Pre-publish offline drafts · 08/10/2026

**Status: DRAFT / offline.** Branch `slice/linkedin-prepublish-adsheet-review` from main `f266e11d`. Nothing is created, uploaded, published or sent; no ad ID, URL, rights confirmation or review result is invented. Group 2, items 3 and 4 of the pre-publish review.

| # | File | Purpose |
|---|---|---|
| 3 | [03_LinkedIn_Ad_Build_Sheet.md](03_LinkedIn_Ad_Build_Sheet.md) + [csv](03_LinkedIn_Ad_Build_Sheet.csv) | 99 ad rows (33 journeys × cold / explanation / proof), native headline and artwork headline kept apart, open decisions D1–D6 |
| 3 | [03_LinkedIn_Ad_Cards.csv](03_LinkedIn_Ad_Cards.csv) | 339 card rows: artwork headline, native headline, body, source line, CTA label, alt text, image path |
| 4 | [04_Native_Review_Packet_en.md](04_Native_Review_Packet_en.md), [zh-Hans](04_Native_Review_Packet_zh-Hans.md), [zh-Hant](04_Native_Review_Packet_zh-Hant.md), [vi](04_Native_Review_Packet_vi.md) | Readable packets for native/domain reviewers, grouped by treatment (each treatment shows every string that occurs in it) |
| 4 | [04_Review_Items.csv](04_Review_Items.csv) + [04_Review_Occurrences.csv](04_Review_Occurrences.csv) | Unique strings with stable IDs, and every occurrence (treatment, batch, surface, key, source) |
| 4 | [04_Review_Responses.csv](04_Review_Responses.csv) | **Reviewer-owned**, never overwritten by the generator |
| 4 | [04_Review_Status.csv](04_Review_Status.csv), [04_Review_Orphans.csv](04_Review_Orphans.csv) | Generated: UNREVIEWED / REVIEWED / NEEDS_RECHECK per item; responses whose text no longer exists |
| – | [build_prepublish_packs.py](build_prepublish_packs.py), `_stats.json` | Reproducible generator (read-only on journeys/readers) and its counts |

## Review packet content
2,000 unique strings (en 582, zh-Hans 590, zh-Hant 587, vi 241) with 8,493 occurrences. Surfaces: journey captions, artwork headlines, platform native headlines, card bodies, card source lines, card CTAs, image labels, card alt text (339 each for caption, headline, native headline, body and alt) and reader pages. Journey texts exist only in the journey's own locale (en, zh-Hans, zh-Hant); reader pages exist in all four languages, so Vietnamese has reader text only. 577 strings occur in more than one treatment (for example "ERP for manufacturing"); the items file lists all treatments and batches and the occurrences file lists each place, so no treatment or source context is lost.

**IDs are stable.** A review ID is `RV-` plus a hash of the locale and the exact text, so rerunning the generator never renumbers; a changed text gets a new ID.

How to use: a reviewer reads the packet for their market and records OK / CHANGE / QUESTION in `04_Review_Responses.csv` (columns: review ID, locale, `text_sha1_at_review` copied from the items file, reviewer, date, verdict, suggested change, note). **Rerunning the generator never touches that file.** After a rerun, `04_Review_Status.csv` shows which items are still UNREVIEWED or NEEDS_RECHECK, and `04_Review_Orphans.csv` lists responses whose text changed or disappeared so the replacement is reviewed again. Changes are applied to readers/journeys only after Bảo accepts them; image text changes need artwork work, not a text edit.

Out of scope: VN domestic journeys, image art direction, legal clearance of photos and illustrations, and the facts of the case beyond the cited sources.

## Boundaries and limits
- Everything here describes the current main artifacts; if they change, rerun the script (`python -I build_prepublish_packs.py` from this folder). It overwrites only the generated files; reviewer responses are kept.
- Platform field limits, button lists and carousel limits were not verified (no source in the repository).
- No native review has happened yet; the packets are the means to start one.

Docs impact reviewed: no canonical update required (draft preparation files; no status, budget, asset or decision changed). Decisions D1–D6 must be written into the build pack and CURRENT_STATE when Bảo makes them.

## Main integration note · 12/10/2026

Nhánh `slice/linkedin-prepublish-adsheet-review` được merge vào main local (chưa push). Trước khi merge, generator được chạy lại trên main: thống kê trùng `_stats.json` (99 ad, 339 card, 2.000 chuỗi, 8.493 lần xuất hiện) và nội dung file sinh ra không đổi; chỉ khác ký tự xuống dòng, đã hoàn lại bản commit.

Phạm vi MSG-ANCHOR-01: các gói này **tập hợp chuỗi có sẵn** từ journey/reader đã có trên main, không viết hay chỉnh copy mới. Gói không tự mang verdict `MESSAGE_ANCHOR_PASS`, `SCRIPT_REVIEW_PASS` hay native-market review; chưa có phản hồi reviewer nào (`04_Review_Responses.csv` rỗng). `objective_proposal` và `audience_proposal` trong bảng build là đề xuất, không phải quyết định. D1–D6 vẫn chờ Bảo; trạng thái audience hiện hành ở [CURRENT_STATE](../../../CURRENT_STATE.md), không lấy từ bảng này.

Docs impact reviewed: CURRENT_STATE có notice tham chiếu gói này; không đổi ngân sách, asset, verdict hay quyết định.
