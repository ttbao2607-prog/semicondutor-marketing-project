# B10–B12 O4-Q reader review (Wave 4) — 2026-10-08

Status: IMPLEMENTED / destination-only SELF_REVIEW / PO_PENDING. Not committed. No push, no live.

Correction: B10–B12 were first recorded as deferred because "the case information is missing". Repo check shows they use the same case as B7–B9 (江苏中科智芯集成科技有限公司, Digiwin Vietnam case 06; journey proof cards RMK-R4-1..4), so no new case research or image was needed.

What changed: B10 (en), B11 (zh-Hans), B12 (zh-Hant) stub readers rebuilt from the approved B7 reader (VN Soft Structuralism + Editorial Split, 4 languages in one HTML, defaults en/zh-Hans/zh-Hant, journey entry hrefs carry `?lang=`). Case context, the SPC/ECN/linked-records/exception mechanism section and the authentic September 2020 visit photo with its Sohu source line are inherited from B7. Only the Quality-persona copy changes (`OQ-copy/o4q.json`, 4 languages), following the O4-Q journey cards B1–B5: which lot is under review, what surrounding context (people/machines/materials/methods/environment) needs checking, who checks what is missing. It states the information-management view complements the technical evaluation and does not assume a cause. Assets, selected-copy, prompts and manifests untouched (pins in `../B10-B12-intake.json`). The Vietnamese pack is newly authored by root; zh/en follow the journey card wording.

Runtime checks (headless Chrome): 3 readers × 1280/390/320 × entry (explicit `?lang`, absent, invalid `fr`) → journey locale; 4 toggles per reader/width = 36 states: lang, aria-pressed, `?lang=` URL, 3 sections with labels, 3 value items, 4 mechanism items, no empty/placeholder text, return links `index.html`, no overflow, photo loaded; 0 failures. B12 desktop zh-Hant screenshot inspected.

Limits: one screenshot inspected; others DOM-checked. New Vietnamese copy not reviewed by a native reader. Photo rights (Sohu byline account) unverified; ROI/ outcome numbers not used. Historical technical status of the B10–B12 journeys (browser not observed for B10/B11; mobile/desktop640 incomplete for B12) is unchanged. Message-anchor review is root self-review against the journey cards and case source; no independent review.
