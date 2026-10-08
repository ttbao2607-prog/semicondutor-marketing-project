# B13–B21 Fabless (F1–F3) reader review (Wave 2) — 2026-10-08

Status: IMPLEMENTED / destination-only SELF_REVIEW / PO_PENDING. Not committed. No push, no live.

What changed: the nine stub readers now use the approved B7 reader design (VN Soft Structuralism + Editorial Split) with all four languages (vi/en/zh-Hans/zh-Hant) in one HTML. Route defaults follow the journey locale (B13/B16/B19 en, B14/B17/B20 zh-Hans, B15/B18/B21 zh-Hant); journey entry hrefs carry `?lang=`. Assets, selected-copy, prompts and manifests untouched (hashes in `../B13-B21-intake.json`).

Case content (Bright Power, 上海晶丰明源半导体股份有限公司, case 04 of the Digiwin Vietnam collection): only what the source states — long engineering response, slow order response, low outsourcing-management efficiency, "integrated digital solution", plus its note that order handling and outsourcing coordination can be a fabless bottleneck. No mechanism, module, number, ROI or causal claim; published outcome figures are deliberately omitted (sources diverge, see Wave0-README). Per-treatment persona questions: F1 partner production update, F2 demand change/planning, F3 handoff.

Image: no authentic photo found (Wave 0), so the hero is a labelled AI illustration generated with codex CLI, one call: `../F-illustration/provenance.json` (SHA256, prompt summary, content review, guard status). Captions/alt in all locales say it is an illustration, not a customer photo. The frozen PREGEN guard was not run (see provenance); no ad-card generation authority is implied.

Runtime checks (headless Chrome, same-origin iframes): 9 readers × widths 1280/390/320 × entry (explicit `?lang`, absent, invalid `fr`) → all open in the journey locale; 4 toggles per reader/width → html lang, title, aria-pressed, `?lang=` URL, 3 mechanism items, alt and caption present, no placeholder text, no horizontal overflow, image loaded. 108 toggle states, 0 failures. One full-page screenshot inspected (B13 desktop en): `B13-desktop-en-full.png`.

Limits: only one full-page screenshot reviewed visually; other states DOM-checked only. No native-reader review of Chinese/Vietnamese wording (new copy authored by root from the case source and the existing stub terminology). The journey card wording/artwork and historical findings (B15 proof2 CHANGES_REQUIRED; B18–B21 INSUFFICIENT_EVIDENCE) are unchanged and not addressed here. Message-anchor review is a fresh root self-review of the destination copy against the case source; no independent review. Photo/illustration public-paid rights unverified.
