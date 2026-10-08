# B22–B30 Partner (P1–P3) reader review (Wave 3) — 2026-10-08

Status: IMPLEMENTED / destination-only SELF_REVIEW / PO_PENDING. Not committed. No push, no live.

What changed: the nine Partner stub readers now use the approved B7 reader design with all four languages (vi/en/zh-Hans/zh-Hant) in one HTML. Defaults follow the journey locale (B22/B25/B28 en, B23/B26/B29 zh-Hans, B24/B27/B30 zh-Hant); journey entry hrefs carry `?lang=`. Assets, selected-copy, prompts, manifests and each batch's existing `reader-copy.json` untouched (hashes in `../B22-B30-intake.json`).

Content: the en / zh-Hans / zh-Hant text of each treatment is taken verbatim from the batches' own reviewed `reader-copy.json` (P1 operations B22–B24, P2 systems B25–B27, P3 PCB-supplier quality B28–B30); only the Vietnamese pack (`P-copy/vi.json`) is newly authored by root from the English text. Wafer Works claims stay as the stub states them (silicon wafer materials; crystal growth, wafer processing, epitaxy; production genealogy, progress/equipment visibility, epitaxy history with parameter limits); no top-10 / 24-year / 600+ statistics, no ROI, and it is not presented as PCB or connector proof. No CTA button was added (stubs had none): the Digiwin Vietnam text block and the two source links remain. B22 stays at its nested route `B22-en-p1-v1/supplier-v7/`.

Image: no authentic photo found (Wave 0), so the hero is a labelled AI illustration generated with codex CLI (one call): `../F-illustration/wafer-works-provenance.json`. Captions/alt in all locales state it is an illustration, not a photo of Wafer Works or its equipment. The frozen PREGEN guard was not run (see provenance).

Runtime checks (headless Chrome, same-origin iframes): 9 readers × 1280/390/320 × entry (explicit `?lang`, absent, invalid `fr`) → all open in the journey locale; 4 toggles per reader/width → lang, aria-pressed, `?lang=` URL, 3 sections, 7 paragraphs, 2 source links, return links `index.html`, no empty or placeholder text, no horizontal overflow, image loaded. 108 toggle states, 0 failures. One full-page screenshot inspected (B22 desktop en): `B22-desktop-en-full.png`.

Limits: only one screenshot reviewed visually; others DOM-checked. No native-reader review of the new Vietnamese pack or of the Chinese copy (the Chinese is pre-existing). Historical findings (P-journey 390px unverified, B24 v1 exclusion) are unchanged. Message-anchor review is root self-review of the destination against the stub copy and case source; no independent review. Illustration/public-paid rights unverified.

## Revision after PO review (2026-10-08)
Bảo noticed sections 01–03 had no left-column title (the B7 design highlights it). Added a short section label per section in all four languages (`s1Index`–`s3Index` in `P-copy/common.json`: where to start / roles and responsibilities / industry context). Rebuilt with `build_partner_readers.py` (original before-pins in `B22-B30-intake.json` preserved). Re-checked 9 readers × 1280/390/320 × 4 toggles = 108 states: 3 non-empty labels each, no overflow; B30 zh-Hant desktop screenshot inspected. Fabless (B13–B21) and B8/B9 already had these labels.
