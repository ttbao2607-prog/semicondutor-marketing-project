# Status checkpoint — four-locale production deployment

**Result:** `COMPLETED / PUBLICLY VERIFIED`. This checkpoint records the completed LadiPage deployment; this Git commit does not perform or authorize a new publication.

## Git provenance

- Source and approved candidate commit: `9d1adc6875faf340d615421884a471a1ca9f028f` on `slice/audit-automation-artifacts`; the handoff manifest records it as local-only, with no remote branch containing it.
- Branch at handoff completion: `slice/audit-automation-artifacts`, HEAD `0dcbb939224e495111cead99f1c8ed38c6e0c9ed`. This is the working branch for this checkpoint.
- The earlier packaged snapshot recorded `slice/executive-reporting-pack` at `de9570e3550b582f4f8636a12d4b2d79269f200d`; the manifest preserves both snapshots because the checkout changed during handoff preparation.
- The current branch has no upstream. The recovery audit also found a newer local-only `main` in another worktree; this checkpoint does not switch branches, merge, or push.

## Published pages

Each existing page now serves the four locale variants `vi`, `en`, `zh-Hans`, and `zh-Hant` at its unchanged production URL. Builder source was saved, reopened and read back at the SHA-256 shown below; the same revision was published and publicly verified.

| Route | Production URL | Candidate SHA-256 | Published Builder readback SHA-256 |
|---|---|---|---|
| OSAT | https://solutions.digiwin.com.vn/semiconductor-osat | `df8c4119afb8cacdded9b37031c5d0c81ead3c66cc372d8360a0f2119951f1ed` | `b8b3c241849cfcdcb07a98e11013795080d3ec6449024ad9b7d25c4244c1dd11` |
| Fabless | https://solutions.digiwin.com.vn/fabless | `4a48d52c7a5a862f4740f34f7878ba1979191fde6a65f932c7a2ca9abef26e11` | `a888b89a48e081fb99b1b20170108675c3edbe2066bd1ec7f05119a471512a68` |
| Partner | https://solutions.digiwin.com.vn/supplierecosystem | `fab771125c062c726136172fcf7538ef0cab46583c98952673af21059898b6d7` | `98b31eea72a473217ebfea2a606b5787b043a60aeadabcc69ed3d2644465807f` |

All three per-route receipts report `COMPLETED`; preflight returned `EXISTING_PAGE_REVISION_PREFLIGHT_READY` and closeout returned `EXISTING_PAGE_REVISION_RECONCILED`, with no validator errors. Locale selection and translated hero content were checked publicly. Fabless retained English after reload. The PopupX modal opened and closed without submitting the form or creating a lead. Protected witnesses were checked before and after revision.

Responsive evidence covers desktop, 390 px and 320 px. At 320 px the page root matches the viewport and `scrollX=0`, while the existing 320 px minimum width and 305 px client width leave a 15 px horizontal scrollbar; this known limitation was retained.

## Scope and evidence

The separate PageSpeed result remains `P4_P5_CLOSED_PARTIAL_ACCEPTANCE_FROZEN`; production Mobile scores remain below the original 80-point target. The locale deployment does not change that performance decision, authorize further page edits, or authorize campaign enablement or spend.

Full sanitized receipts, screenshots, public observations and protected witnesses are in `C:\Users\ASUS\AppData\Local\Temp\semiconductor-locale-9d1adc6-handoff\HANDOFF.md`. The 53-file SHA-256 ledger was rechecked before this commit with zero missing files or mismatches.

**Docs impact reviewed:** `CURRENT_STATE.md`, `README.md`, `operations/Pre_Ad_Readiness_Plan.md` and the OSAT route truth now point to this completed deployment. The tracking contract was reviewed; no update was required because CTA, form, provider and event behavior did not change.
