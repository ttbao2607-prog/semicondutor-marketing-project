# B8/B9 O4-O reader review (Wave 1) — 2026-10-08

Status: IMPLEMENTED / destination-only SELF_REVIEW / PO_PENDING. Not committed. No ImageGen, no push, no live.

Method: B8 (zh-Hans) and B9 (zh-Hant) selected-copy cards are exact localisations of approved B7 (same 10 card ids/stages, same three questions, same ERP+iMES case 江苏中科智芯集成科技有限公司). Their readers are built from the approved B7 four-language reader (`build_b8_b9_readers.py`): only `<html lang>`, title, active toggle, fallback locale and the journey entry `?lang=` change. 2020 Sohu visit photo, translated source/date/alt and rights caveats are inherited from B1/B7 (rights for public/paid use remain unverified). Pins: `../B8-B9-intake.json`.

Runtime checks (headless Chrome 127.0.0.1 server, same-origin iframes; widths 1280/390/320):
- Explicit `?lang=<journey locale>`, absent lang and invalid lang (`fr`) all open in the journey locale (B8 zh-Hans, B9 zh-Hant) at all 3 widths.
- All four toggles on each route at all 3 widths: html lang, title, aria-pressed and `?lang=` URL update; no horizontal overflow; photo and logo load.
- 390px checked with real mobile emulation (viewport 390 CSS px) for B9 toggles; 320px smoke in iframes.
- Return links `index.html` unchanged; journey entry hrefs now `case-reader.html?lang=zh-Hans` / `?lang=zh-Hant`.
- Screenshots inspected: B8 desktop full page (zh-Hans), B9 mobile top (zh-Hant).

Not done / limits: not every locale×viewport full-page screenshot was captured (only the two above were visually inspected; others verified by DOM checks). Chinese glyph/wrapping and terminology were not reviewed by a native reader. Message-anchor binding relies on the B7 review plus identical card structure; no new independent review. Historical whole-journey findings, photo rights and PO acceptance are unchanged.
