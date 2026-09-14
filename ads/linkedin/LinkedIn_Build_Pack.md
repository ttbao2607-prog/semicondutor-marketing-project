# LinkedIn Build Pack

**Status:** offline creative revision complete; latest direct route redirected to Campaign Manager sign-in. No credentials were entered; account/Page, placement, audience, permissions and live-object verification remain pending.

## Format and delivery specifications

- Static concepts: square 1200x1200; JPG/PNG/GIF <=5MB; official sources are recorded in `operations/Public_Source_Register.md`.
- Document ad: 6-page PDF; <=100MB and far below 300 pages.
- Objective: **Brand Awareness**.
- No LinkedIn Lead Gen Form.
- Destination: native/in-platform; official LinkedIn Company Page only if a destination is required.
- Audience Expansion: **OFF** baseline.
- LinkedIn Audience Network: **OFF** baseline.

## Prospecting hypotheses

| Sanitized ad set | Include hypotheses | Exclude hypotheses | Status |
|---|---|---|---|
| LI-P1-OSAT-OPS | Vietnam; OSAT/factory; operations, manufacturing, quality, process engineering, supply chain, IT/MES; manager/head/director/VP where available | Students, recruitment, unrelated consumer electronics, broad policy-only roles | UI size/availability/login verification pending |
| LI-P1-FABLESS-WIP | Vietnam; fabless/commercialization; operations, planning, supply chain, R&D/program, finance; manager/director/VP | Pure academic/recruitment, unrelated chip hobby/consumer roles | UI size/availability/login verification pending |
| LI-P1-PARTNER-INTEGRATION | Vietnam; supplier/SI/automation/materials-equipment; ERP/MES/OT, solution engineering, partner/channel, quality; manager/director | End-user-only exclusions where partner objective is selected; unrelated sales roles | UI size/availability/login verification pending |

No company/contact upload is allowed. Account-list targeting must remain separate from role-delivery evidence. No PII, personal names, emails or raw lists are included.

## Retargeting definition

`LI-AUD-P1-ENGAGED-30D`: single-image/document engagement, status **Building**, launchable only when reachable audience is `>=300` and UI evidence confirms eligibility. No audience is created in this milestone.

## Creative pack

Three static concepts are provided under `assets/linkedin/source/` and rendered under `assets/linkedin/final/`, one per segment. The six-page OSAT document follows: cover; operating questions; mechanism map; traceability lens; operating review; contact-copy CTA. The static concepts use customer-facing route copy and contain no customer name, number, case, outcome or unverified claim. Offline creative revision and PNG visual QA are recorded below; account/Page/placement/audience UI and live-object readiness remain pending.

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

## Current blocker and validation plan

The authenticated LinkedIn route redirected to sign-in in the discovery attempt; current account, Page, permissions, audience size, objective availability and delivery are therefore unverified. Before any future draft/paused object creation: confirm business/account identity, validate role facets and sizes, confirm Company Page destination if needed, retain Expansion/LAN OFF, and keep all objects non-delivering.
