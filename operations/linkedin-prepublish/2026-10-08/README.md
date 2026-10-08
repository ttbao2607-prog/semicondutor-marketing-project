# Pre-publish offline drafts · 08/10/2026

**Status: DRAFT / offline.** Branch `slice/linkedin-prepublish-adsheet-review` from main `f266e11d`. Nothing is created, uploaded, published or sent; no ad ID, URL, rights confirmation or review result is invented. Group 2, items 3 and 4 of the pre-publish review.

| # | File | Purpose |
|---|---|---|
| 3 | [03_LinkedIn_Ad_Build_Sheet.md](03_LinkedIn_Ad_Build_Sheet.md) + [csv](03_LinkedIn_Ad_Build_Sheet.csv) | 99 ad rows (33 journeys × cold / explanation / proof), fields from the journeys, open decisions D1–D6 |
| 4 | [04_Native_Review_Packet_en.md](04_Native_Review_Packet_en.md), [zh-Hans](04_Native_Review_Packet_zh-Hans.md), [zh-Hant](04_Native_Review_Packet_zh-Hant.md), [vi](04_Native_Review_Packet_vi.md) | Readable packets for native/domain reviewers, grouped by treatment |
| 4 | [04_Review_Items.csv](04_Review_Items.csv) | The same strings as one sheet with review IDs and empty reviewer columns |
| – | [build_prepublish_packs.py](build_prepublish_packs.py), `_stats.json` | Reproducible generator (read-only on journeys/readers) and its counts |

## Review packet content
1,699 unique strings: en 482, zh-Hans 489, zh-Hant 487, vi 241. Surfaces: journey captions (78), card headlines (230), card bodies (236), image labels (92), card source lines (56), card CTAs (45), reader pages (962). Journey texts exist only in the journey's own locale (en, zh-Hans, zh-Hant); reader pages exist in all four languages, so Vietnamese has reader text only. Identical strings are shown once and list every batch they appear in. Each treatment section carries its source reference (case, anchor).

How to use: a reviewer reads the packet for their market and fills `reviewer_verdict` (OK / CHANGE / QUESTION), `suggested_change` and `reviewer_note` in the CSV by review ID. Changes are applied to the readers/journeys only after Bảo accepts them; image text changes would need artwork work, not a text edit.

Out of scope: VN domestic journeys, image art direction, legal clearance of photos and illustrations, and the facts of the case beyond the cited sources.

## Boundaries and limits
- Everything here describes the current main artifacts; if they change, rerun the script (`python -I build_prepublish_packs.py` from this folder).
- Platform field limits, button lists and carousel limits were not verified (no source in the repository).
- No native review has happened yet; the packets are the means to start one.

Docs impact reviewed: no canonical update required (draft preparation files; no status, budget, asset or decision changed). Decisions D1–D6 must be written into the build pack and CURRENT_STATE when Bảo makes them.
