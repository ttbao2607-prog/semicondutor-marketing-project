# LinkedIn Build Pack

**Status:** offline creative revision and Bảo-approved proof-carousel v1 complete; authorized external read-only validation was completed on 2026-09-14. The public record retains only sanitized findings. No audience upload, creative attachment, campaign delivery or spend occurred.

## Format and delivery specifications

- Static concepts: square 1200x1200; JPG/PNG/GIF <=5MB; official sources are recorded in `operations/Public_Source_Register.md`.
- Document ad: 6-page PDF; <=100MB and far below 300 pages.
- Objective: **Brand Awareness**.
- No LinkedIn Lead Gen Form.
- Destination: native/in-platform; official LinkedIn Company Page only if a destination is required.
- Measurement: native delivery and engagement metrics are reported in Campaign Manager; these in-platform metrics do not require a Digiwin website Insight Tag. Phase 5 Preview observed an existing LinkedIn InsightTag firing on OSAT as website behavior; its purpose and consent behavior were not revalidated or changed, and this does not make it a native-delivery prerequisite. Website conversion tracking or visitor retargeting would be a separate, explicitly approved scope.
- Audience Expansion: **OFF** baseline.
- LinkedIn Audience Network: **OFF** baseline.

## Prospecting hypotheses

| Sanitized ad set | Include hypotheses | Exclude hypotheses | Status |
|---|---|---|---|
| LI-P1-OSAT-OPS | Vietnam; OSAT/factory; operations, manufacturing, quality, process engineering, supply chain, IT/MES; manager/head/director/VP where available | Students, recruitment, unrelated consumer electronics, broad policy-only roles | Sanitized external validation completed; no delivery evidence. Production mapping and eligibility remain gated. |
| LI-P1-FABLESS-WIP | Vietnam; fabless/commercialization; operations, planning, supply chain, R&D/program, finance; manager/director/VP | Pure academic/recruitment, unrelated chip hobby/consumer roles | Sanitized external validation completed; no delivery evidence. Production mapping and eligibility remain gated. |
| LI-P1-PARTNER-INTEGRATION | Vietnam; supplier/SI/automation/materials-equipment; ERP/MES/OT, solution engineering, partner/channel, quality; manager/director | End-user-only exclusions where partner objective is selected; unrelated sales roles | Sanitized external validation completed; no delivery evidence. Production mapping and eligibility remain gated. |

No company/contact upload is allowed. Account-list targeting must remain separate from role-delivery evidence. No PII, personal names, emails or raw lists are included.

## Retargeting definition

`LI-AUD-P1-ENGAGED-30D`: single-image/document engagement, status **Building**, launchable only when reachable audience is `>=300` and UI evidence confirms eligibility. No audience is created in this milestone.

## Creative pack

### Vy four-locale offline source-copy coverage (2026-09-29)

`assets/linkedin/source/vy-four-locale-copy-register.md` is the S5 copy and QA register. It proposes **three languages/four locale variants**: Vietnamese `vi`, English `en`, Simplified Chinese `zh-Hans` for China FDI and Traditional Chinese `zh-Hant` for Taiwan FDI. Bảo decided the scripts/markets and confirmed on 2026-09-29 that case/claim content already present in Vietnamese source has management approval for use and full translation. Localized terminology, exact claim scope, layout and platform readiness still require QA; new or broader claims require their own evidence. S1's FDI/domestic account framework is a research hypothesis, not an audience list or proof of platform delivery.

| Asset family | Coverage in source-copy register | Existing canonical asset | Remaining production gate |
|---|---|---|---|
| OSAT, Fabless and Supplier/Partner static concepts | 3 × 4 complete editable-SVG node copy; EN/Hans/Hant square SVG/PNG and VI/Hans/Hant b2b-v2 candidates rendered | Three original source SVGs; six original square/b2b-v2 PNG derivatives | Stage A square renders inspected at 1200²; Stage B b2b-v2 raster edits inspected at 1254². Native wording, placement crop/mobile preview, alt text and platform format review remain open. |
| OSAT six-page document | Six-page × four-variant source-line ledger; EN/Hans/Hant PDF rendered | Vietnamese six-page copy MD and original PDF | Stage A 3×6 A4 pages rendered and text/visual checked; native wording and active-account format review open. |
| CAR-01 Taiwan, CAR-02 China, CAR-03 abstract, CAR-04 Vietnam | Four × four metric-free message candidates; 12 EN/Hans/Hant candidate PNGs rendered | Four approved English offline-v1 PNGs | VI metric-free cards remain copy-only. Native terminology, placement/crop and platform review remain open. CAR-03 stays abstract; English-only 200+/700+ metrics were removed from localized candidates and their translation remains a separate claim decision. |

Bảo also chose the paid-entry design: preserve each existing route URL (`/semiconductor-osat`, `/fabless`, `/supplierecosystem`) and use a non-PII `lang` query parameter (`vi`, `en`, `zh-Hans`, `zh-Hant`) to select the initial locale; the top language switch remains user-controlled. Route behavior still needs per-route runtime and ad-entry QA before use. An ad-to-landing matrix must check the exact route plus parameter, existing UTM and `gclid`, initial locale, switch override, fallback and persistence. Do not launch an EN/Chinese ad to a Vietnamese-only runtime. Stage A produced localized offline square PNGs and OSAT PDFs; Stage B produced b2b-v2 and metric-free carousel raster candidates. No account object or campaign was created.

**2026-09-29 Stage A render checkpoint:** added `assets/linkedin/source/{osat,fabless,partner}-square-{en,zh-Hans,zh-Hant}.svg`, corresponding `assets/linkedin/final/*.png` at 1200×1200, and `output/pdf/digiwin-osat-document-ad-6p-{en,zh-Hans,zh-Hant}.pdf` (six A4 pages each). All 39 SVG `<title>/<desc>/<text>` nodes per locale family map to the copy register; rendered images were inspected for glyphs, logo, line wrap and clipping. All 18 PDF pages were rendered to temporary QA images and visually scanned. Extracted text matched each displayed localized source-line row, including unchanged page-six contact values; page-5 `Table headers` is a ledger-only structure absent from the source card design. Font/HTML-print PDF passes that failed glyph or artwork QA were rejected. Final PDFs retain the original vector art through text-only replacement, with light-background contrast corrected on pages 2 and 5. Original assets below retain their historical evidence and hashes.

**2026-09-29 Stage B raster candidate checkpoint:** Imagegen edits of the flattened source PNGs produced the following local-only matrix. The original PNGs remain untouched. Every candidate was opened and visually checked at 1254×1254 for text, accents/glyphs, logo/art, connectors, margin and claim scope. The first OSAT VI pass was rejected because its rail/nodes retained descriptive English; its saved candidate was replaced with a fully Vietnamese inspected pass. Imagegen outputs remain raster candidates without editable text layers or deterministic typography. Native terminology review, alt text, placement crop/mobile preview, platform export specifications and account rights remain open.

| Raster family | VI | EN | zh-Hans | zh-Hant |
|---|---|---|---|---|
| OSAT b2b-v2 | `osat-linkedin-b2b-v2-vi-candidate.png` | original `osat-linkedin-b2b-v2.png` | `osat-linkedin-b2b-v2-zh-Hans-candidate.png` | `osat-linkedin-b2b-v2-zh-Hant-candidate.png` |
| Fabless b2b-v2 | `fabless-linkedin-b2b-v2-vi-candidate.png` | original `fabless-linkedin-b2b-v2.png` | `fabless-linkedin-b2b-v2-zh-Hans-candidate.png` | `fabless-linkedin-b2b-v2-zh-Hant-candidate.png` |
| Supplier/Partner b2b-v2 | `partner-linkedin-b2b-v2-vi-candidate.png` | original `partner-linkedin-b2b-v2.png` | `partner-linkedin-b2b-v2-zh-Hans-candidate.png` | `partner-linkedin-b2b-v2-zh-Hant-prototype.png` |
| CAR-01 Taiwan, CAR-02 China, CAR-03 abstract, CAR-04 Vietnam | VI source copy only; image not rendered | four `carousel-car-0*-en-candidate.png` | four `carousel-car-0*-zh-Hans-candidate.png` | CAR-01/02/04 `-zh-Hant-candidate.png`; CAR-03 `-zh-Hant-prototype.png` |

CAR-01/02 candidates remove the original English-only `200+`/`700+` metric panels while preserving Taiwan/China scope. CAR-03 has no customer name, mark, metric or result; CAR-04 retains the Bac Ninh and Ho Chi Minh City map pins. No image is cleared for live LinkedIn use by this offline render gate.


Three static concepts are provided under `assets/linkedin/source/` and rendered under `assets/linkedin/final/`, one per segment. The six-page OSAT document follows: cover; operating questions; mechanism map; traceability lens; operating review; contact-copy CTA. The static concepts use customer-facing route copy and contain no customer name, number, case, outcome or unverified claim. Offline creative revision and PNG visual QA are recorded below; account/Page/placement/audience UI and live-object readiness remain pending.

### Offline proof-carousel v1

Bảo approved the four-card awareness carousel for offline use on 2026-09-18. The canonical files are:

- `assets/linkedin/final/carousel-car-01-taiwan-v1.png`
- `assets/linkedin/final/carousel-car-02-china-v1.png`
- `assets/linkedin/final/carousel-car-03-proof-abstract-v1.png`
- `assets/linkedin/final/carousel-car-04-vietnam-v1.png`

The generated working size is `1254×1254` for each card; final export dimensions remain subject to the active LinkedIn account specification. CAR-03 intentionally uses abstract proof-safe copy with no customer name or logo. This is an offline creative artifact only; no carousel upload, object creation, launch or spend is authorized by this section. See `operations/LinkedIn_Carousel_Governance_Record.md` for the approval and source/rights boundary.

### Offline static-creative revision

- Replaced internal production notes in all three footers with the approved customer-facing copy and updated each SVG description for accessibility.
- Rendered the three source SVGs to 1200x1200 PNGs using local headless Chrome; inspected each full-resolution image against its SVG text for legibility, clipping, overlap and logo/aspect integrity. The OSAT caption was moved below its diagram connector for clear separation.

| Creative | PNG dimensions | Bytes | SHA-256 |
|---|---:|---:|---|
| OSAT | 1200x1200 | 83760 | `5a3a3d7cc49396bab74ec72b94817cd4def74967170195127cb43665408c82c9` |
| Fabless | 1200x1200 | 89954 | `f3597683064bd343e63137ad95f8a4e4836b4681bb3ef14f881b635d41bac05a` |
| Partner | 1200x1200 | 85464 | `f15ceaa34bcdf8ab936dcf2dc21e6ba3309d29d74c22fc8913db323dddfc3680` |

- This verifies offline creative assets only. It does not verify LinkedIn account/Page permissions, placements, audience availability, or any remote ad object; those remain pending the explicitly authorized UI review.

### Offline OSAT document-ad revision

- Rebuilt the six-page A4 OSAT document with customer-facing copy and the verified public Digiwin contact block. The page-by-page copy source is `assets/linkedin/source/osat-document-ad-6p-copy.md`.
- QA: six A4 portrait pages; all six pages rendered with bundled Poppler at 120 dpi and visually reviewed for legibility, margins, tables, diagram, page sequence, clipping and overlap. Extracted page text was checked against the copy source, and the extracted copy contains none of the prohibited internal/governance terms.
- PDF: `output/pdf/digiwin-osat-document-ad-6p.pdf` | 6 pages | A4 portrait | 98,953 bytes | SHA-256 `64defd157bbded2cdc245df22346f5b96c0d8702f53b470ec530c84d7c5881fa`.
- This is an offline creative artifact only. LinkedIn account/Page permissions, placements, audience availability and live-ad-object readiness remain pending; no account or campaign action was taken.

## Production gate and validation plan

External validation was completed as non-delivering draft/off work on 2026-09-14. Raw account, audience, list and screenshot evidence is not committed to this public repository. The validation did not create or upload an audience, attach creative, publish an ad, generate delivery or incur spend.

Before any future draft/paused object creation: obtain human sign-off for unresolved entity mappings; reconfirm the current business/account, placement, objective, audience eligibility and settings in the authorized UI; retain Expansion/LAN OFF; and keep all objects non-delivering. Treat any historical estimate or configuration observation as a bounded input, never as delivery, awareness or commercial performance evidence.
