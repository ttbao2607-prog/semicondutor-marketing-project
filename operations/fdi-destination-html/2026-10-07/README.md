> **PO checkpoint approval · 2026-10-07:** Bảo: “Okie đẹp r, commit checkpoint”. Current B1 four-language/photo reader approved for offline checkpoint on the dedicated slice. Main integration, GitHub push, live publish and public/paid image rights are separate. Current scoped backlog:8 mapped destination routes (B1–B5 +3 O3 pilot routes),1 done/approved and7 still require the new design. Broader pipeline:11 treatments /33 incoming-locale coverage rows; final shared-file count is not fixed until persona/return mapping is reviewed. B4/B5 now both have draft HTML on local main b2694b4; earlier script-only/uncommitted-source states are preparation history.

> **PO imagery rule07/10:** Every destination follows [Destination_HTML_Anchor.md](Destination_HTML_Anchor.md): find authentic exact-case Digiwin photography before implementation; generate an explicitly labelled illustration only if no suitable real photo is available and current generation gates pass. B1 now uses the2020 visit photo with translated source/date/alt; [new review](B1-photo-review/README.md) supersedes SVG rendering for current bytes.

# FDI destination HTML preparation · 2026-10-07

Status: B1_TRIAL_IMPLEMENTED / SCOPED_SELF_REVIEW_COMPLETE; other destinations NOT_IMPLEMENTED. See [B1 trial receipt](B1-review/README.md). Owner: root SELF_REVIEW; no delegation.

## Contract and baseline

User mandate: take the accepted VN design/layout, list every FDI destination that needs work (draft = not done), and prepare a separate worktree. Worktree: D:/LinkedIn_FDI_Destination_HTML_2026-10-07; branch slice/linkedin-fdi-destination-html; base local main 8895a3ebce7ab3b815be4e005be03f571fd96d92. Opened research checkout ff0cb4d has concurrent unstaged/untracked B4/B5 work; it is an input source, not canonical main. Existing research files are untouched. New preparation files are unstaged/uncommitted; no push or live action.

Selected library: Leonxinx — High-End Visual Design, docs/taste_leonxinx.md, V3 Soft Structuralism + L3 Editorial Split. Library preference to vary layouts is overridden by Bảo's explicit request to use the same VN layout throughout this pipeline. Apply the guidance; do not install a project skill.

## Design implementation reference

- deliverables/linkedin-vn-journey/2026-10-06-v3/case-aplus.html (path from repository root; accepted Week1)
- deliverables/linkedin-vn-journey/2026-10-06-week2-time-v2/case-aplus.html (accepted Week2)
- operations/linkedin-vn-journey-rebuild/2026-10-06/ldp-value-main-integration/README.md

Both VN references are already available unchanged in this worktree. Use their CSS/layout as implementation authority: #f6f6f8 canvas, white paper, bold sans, blue hierarchy/orange CTA, diffused shadows; 1180px shell; editorial 1fr / 1px / 1fr split; sticky left section labels; double bezel illustration and consultation cards; source attribution and return link; pill CTA with circular trailing icon; <=600px single column. Follow actual accepted VN spacing/breakpoints rather than enlarging every section to library defaults. Preserve focus, skip link, 44px controls, reduced-motion handling and readable source text. Chinese requires an actual glyph/fallback-font and line-break review; do not assume Plus Jakarta covers Chinese.

Content topology: hero/context and named case -> published mechanism -> persona-relevant business value and questions to review current operations -> appropriate next step -> attributed primary source -> return to exact journey. Reuse the VN visual system, not VN readiness/audit messaging or Aplus claims for a different case. No invented ROI, savings, payback or guarantee; ERP+iMES must remain an integrated mechanism. Do not use a large invented KPI simply to fill the VN metric slot. Keep technical IDs and internal release status out of customer content.

Packaging (PO revision 2026-10-07): every confirmed destination is one self-contained HTML with all four language toggles: vi / en / zh-Hans / zh-Hant. Inline CSS/JS and embedded approved imagery/logo follow VN single-HTML delivery. Preserve existing case-reader.html routes where they are already linked. All four versions translate the same FDI persona, case, solution scope and business-value message; Vietnamese display does not turn this into the domestic VN journey. Locale coverage rows describe incoming journeys, not separate monolingual deliverables. Sharing an HTML between different journeys still requires equivalent persona/content and verified return mapping; language alone does not justify merging O1/O2/O3. Real-photo selection follows the linked HTML anchor; no ImageGen required for B1 because a suitable authentic photo was found.

### Four-language entry and toggle contract

- Every journey link supplies an explicit non-PII `lang` query: English -> `case-reader.html?lang=en`, China -> `?lang=zh-Hans`, Taiwan -> `?lang=zh-Hant`, Vietnamese -> `?lang=vi`. Confirm actual route before applying links.
- A valid URL `lang` is authoritative at opening. If absent or invalid, use that destination's configured source-journey locale (B1/B4/candidate1 = en, B2/B5/candidate2 = zh-Hans, B3/candidate3 = zh-Hant). For a future shared destination with no single source locale, configure en as the direct-open fallback and require explicit lang on every journey entry.
- Do not let browser language, a prior localStorage/cookie choice or a different journey override the incoming locale. Apply the initial locale before revealing customer content to avoid a flash of the wrong language.
- Toggle labels are Tiếng Việt / English / 简体中文 / 繁體中文. A click updates all visible text, document title, html lang, alt/aria labels and active aria-pressed state. Preserve section position and keyboard focus; use allowlisted locale values only.
- Update `lang` via history.replaceState on the same pathname so refresh/copy keeps the selected language without adding a back-history entry for each toggle. Preserve other allowed journey context. Keep the original journey return target and its original locale even after the reader language changes; never accept arbitrary return URLs.
- Both Chinese profiles require separate terminology/glyph review. All four versions retain entity names, numbers, geography, source language disclosure and CTA scope. External source/contact pages keep their actual language disclosure; toggle does not imply those pages are translated.

## Actionable existing destinations — B1 trial implemented; others NOT DONE

| Journey | Locale | Current input | Work |
|---|---|---|---|
| O1 Quality + Operations B1 | en | deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html | Rebuild VN design + FDI value/persona review |
| O1 B2 | zh-Hans | deliverables/linkedin-safe-batches/2026-10-06/B2-zh-Hans-o1-v1/case-reader.html | Same design, separate locale review |
| O1 B3 | zh-Hant | deliverables/linkedin-safe-batches/2026-10-07/B3-zh-Hant-o1-v1/case-reader.html | Same design, separate Taiwan terminology review |
| O2 Operations + Quality B4 | en | research worktree deliverables/linkedin-safe-batches/2026-10-07/B4-en-o2-v1/case-reader.html | Rebuild; uncommitted source snapshot needed |
| O2 B5 | zh-Hans | local main deliverables/linkedin-safe-batches/2026-10-07/B5-zh-Hans-o2-v1/case-reader.html | Rebuild draft; current main source must be pinned before work |
| O3 pilot candidate1-v4 | en | deliverables/linkedin-locale-dogfood/2026-10-06/en-osat-candidate1-v4/case-reader.html | Rebuild after Finance/Operations bridge review |
| O3 pilot candidate2-v2 | zh-Hans | deliverables/linkedin-locale-dogfood/2026-10-06/zh-Hans-osat-candidate2-v2/case-reader.html | Rebuild after same context review |
| O3 pilot candidate3-v1 | zh-Hant | deliverables/linkedin-locale-dogfood/2026-10-06/zh-Hant-osat-candidate3-v1/case-reader.html | Rebuild after same context review |

B1/B2/B3 offline adoption and historical technical verdicts are preserved; neither certifies this new design. Earlier dogfood versions are history, not extra production destinations. O1 and O2 can reference the same China case but must keep separate persona/value/return mapping until a shared destination is reviewed.

## Conditional pipeline backlog

Inventory.csv lists 11 treatments x three FDI incoming journey locales = 33 coverage rows for planning, not a production quota. Each eventual destination requires all four toggle languages, including vi; the Locale column remains the incoming journey/default locale. Eight have current HTML/script inputs above; 25 are conditional future slots. O2 zh-Hant, O4-O and O4-Q, F1/F2/F3, P1/P2/P3 need current intake and proof/persona mapping before HTML production. F1/Bright and P2/Pressway are historical proposals, not automatic acceptance. Partner SI and industrial supplier must be distinguished. No invented batch numbers or future route is declared canonical.

## Execution order and acceptance

1. Start with O1 EN, using existing reader/script and accepted VN layout; inspect adjacent caption/closing/CTA and primary source snapshot.
2. Review destination message against VY-CONTENT-ANCHOR revision1.0 (hash in source-pins.json) and original supplied email; bind fresh MSG-ANCHOR-01 receipt. Existing PASS does not transfer to a new HTML revision.
3. Build and review all four language versions in each O1 destination, starting with its source journey locale; then O2 and O3 after persona/proof review. Other treatments wait for their intake. No destination is completed with fewer than four toggle languages.
4. Verify native text and actual desktop/mobile render (1280 and 390, plus 320 overflow smoke), loaded images, every section, source legibility, language/title/alt/aria parity, keyboard focus and exact journey return. Per HTML inspect all four languages on desktop/mobile (8 rendered states minimum), all four explicit lang entry URLs, absent/invalid-lang fallback, toggle -> refresh persistence and return after switching languages. In multi-journey HTML verify every incoming journey locale and its return target. Use local-web-preview for browser QA. Hash/DOM checks alone cannot certify layout.
5. Review CURRENT_STATE, DOCS_IMPACT_MAP, build/readiness and message/locale docs before handoff; synchronize only actual changed canonical truth. No canonical state change from this preparation alone.

Preparation SUCCESS requires separate worktree at correct main base, actual VN references present, selected library fully read, inventory with source states and pinned inputs. HTML completion requires actual rendered and semantic evidence per destination; default remains NOT_IMPLEMENTED. Audit target: inventory.csv, source-pins.json and the final revised HTML/render receipts. No independent-agent audit claimed. Future LadiPage import/runtime, tracking/forms, deployment, commit/merge/push and campaign/spend require their own authorized scope.

Docs impact reviewed: no canonical update required. This is an owned preparation packet; existing artifact/status receipts remain unchanged.

