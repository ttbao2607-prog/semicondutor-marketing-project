# Wave 0 intake — 20 destination readers (2026-10-08)

Status: WAVE0_INTAKE_COMPLETE / read-only research. No reader built, no ImageGen/codex call, no commit, no push. Owner: root. Slice `slice/linkedin-fdi-destination-html`, base main `0ee82f56`.

PO scope (Bảo, 2026-10-08): this worktree targets case readers only. Assets are not modified. Photo fallback: if no suitable authentic photo, call codex CLI image generation (labelled illustration; see Fallback). **B10–B12 (O4-Q) deferred** — case information not available.

Pins and sizes: [Wave0-intake.json](Wave0-intake.json) (SHA256 of current `case-reader.html`, `index.html`, `selected-copy.json` for each target; all 20 have 10–11 PNG assets; every entry href is `case-reader.html` with no `?lang=`).

## Targets and waves

| Wave | Batches | Treatment / case | Photo |
|---|---|---|---|
| 1 | B8 zh-Hans, B9 zh-Hant | O4-O, 江苏中科智芯集成科技有限公司 (same case as approved B7) | Reuse the B1/B7 2020 Sohu visit photo (byline 鼎捷智造___new), same provenance and scope caveats |
| 2 | B13–B21 | F1/F2/F3 × en/zh-Hans/zh-Hant, 上海晶丰明源半导体股份有限公司 (Bright Power, China chip design) | None found → fallback |
| 3 | B22–B30 | P1/P2/P3 × en/zh-Hans/zh-Hant, Wafer Works / 合晶科技 (Taiwan–Shanghai silicon wafer) | None found → fallback |

Per-treatment questions (from stub readers) differ and need their own copy: F1 outsourced-production lot/stage, F2 demand-change/planning, F3 handoff/identifier mismatch; P1 lot records → operating decision, P2 record ownership before system handoff, P3 scope customer question before collecting records.

## Findings

1. **Bright Power photo: not found.** Digiwin Vietnam case collection (case 04) has no image in the panel. Digiwin CN semiconductor page lists the name as text only, no logo/photo/case link. Digiwin TW semiconductor page does not mention it. Searches (CN keywords: 签约/启动会/上线) found no event or site photo. Only a CSDN repost of the 2023 case collection mentions it (fetch returned HTTP 521; not usable). Official PDF `digiwin.com/digiwin2023/img/top4_19.pdf` p16 is a graphic casebook, already used as claim source in the proof ledger (PR03).
2. **Wafer Works photo: not found.** Digiwin Vietnam supplier LDP (`solutions.digiwin.com.vn/supplierecosystem`) Wafer Works section uses a labelled simulated diagram only; other images on the LDP are generic stock-like visuals with no credit. Digiwin TW semiconductor page has the 合晶科技 logo and a text line only (no photo). Searches found no deployment case, visit or event photo. Proof ledger PR07 already says "do not recycle local simulation image as facility evidence".
3. **Source-scope caveats to carry into copy:** Bright Power numeric outcome diverges between sources (2 days vs 1 day → 2 hours), so use the qualitative case only. Wafer Works proof is silicon wafer (crystal → wafer → epitaxy), not PCB; Digiwin VN claims for it are self-reported on the Vietnam LDP. P1–P3 readers must not present it as PCB or ERP/MES connector proof.
4. **Route anomaly:** B22 reader lives at `B22-en-p1-v1/supplier-v7/`, unlike all others. Decide in Wave 3 whether to keep the nested route or normalise (affects the journey `index.html` entry link and the inventory row).
5. **Language/entry:** none of the 20 stubs has a locale toggle; entry hrefs need `?lang=<journey locale>` and each page's configured fallback per anchor.
6. Search tools used are web search plus page fetch; Sohu-style pages needing a real browser were not re-checked for these two customers. "Not found" means not found with these tools, not proven absent.

## Fallback image path (Waves 2–3, not run)

Use `codex` CLI (`codex-cli 0.160.1` installed) to generate a clearly labelled illustration, per PO direction. Anchor rule 5 still applies: PREGEN guard and semantic message/script review for the exact revision must be satisfied first; adapter is DEVELOPING/NOT_FROZEN. The illustration must be labelled as an illustration in all four languages, must not imitate customer facility, people or software, and must not be treated as proof.

## Decisions pending from Bảo

- Confirm generating one illustration per case (Bright Power, Wafer Works) rather than per reader, and whether the PREGEN guard requirement is satisfied by the existing process or needs a separate release.
- Approve Wave 1 (B8/B9, reuse photo) as the next step.

Docs impact reviewed: working intake files only; no canonical marketing doc updated, asset bytes untouched.
