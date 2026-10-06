# Fabless interaction repair — production deployment

**Observed:** 2026-09-30, Asia/Ho_Chi_Minh
**Route:** existing production page, `https://solutions.digiwin.com.vn/fabless`
**Disposition:** interaction repair published and publicly verified; no GitHub push.

## Pinned source and Builder lifecycle

- The repair is commit `2e52bf1346d1214a2823b69f10aed7c735f3daef`, included in local `main`. At closeout, `main` was `f49ce83aab18779228fbe5f696d0bafab5cb770e`; its Fabless HTML blob is `f6aac838dcd0b9ab76d493c0aedf9091a6abb8f9`, the same blob as the repair commit.
- Canonical candidate SHA-256: `5db304b5fad545ed81847453d1d3eb4db06b81b943e75f848d118d0fcb0f15b1`. Baseline SHA-256: `4a48d52c7a5a862f4740f34f7878ba1979191fde6a65f932c7a2ca9abef26e11`.
- The four declared Builder steps were applied from their one-shot, hash-pinned payloads. Each full-source result matched the planned bounded transformation. Save/reopen retained Builder source SHA-256 `657435f77de9f9ccde3c6bec0099d5ad18e7848de10a541fbf77d9ed759faad7` (301,075 characters). The pre-edit Builder source fingerprint was `a888b89a48e081fb99b1b20170108675c3edbe2066bd1ec7f05119a471512a68`.
- Publisher showed success for the same `/fabless` URL. The same-page identity and production authorization are retained in the operation-owned receipt outside Git, not in this public-safe note.
- The declared semantic-delta SHA-256 is `0bc01b821901824afc22b0f0ae411ec65d2d6edf618e7c8c628de7727008b711`. Applying the delta reproduces the candidate; reversing it reproduces the baseline byte-for-byte.

## Public verification

- At desktop `1536×735`, the production page loaded at the exact route, had no horizontal overflow, and selected Cost showed `diagram-cost` with inspector `Hạch toán giá vốn & lợi nhuận`. Selecting Cost from its pain card scrolled the map into place (`mapTop` settled at about 94px). A browser screenshot of this public state was captured during review.
- At mobile `390×844`, selecting Cost showed the same diagram and inspector; the map detail expanded and the page had no horizontal overflow. The mobile map state DOM witness SHA-256 is `1de98489ef352e2f05fa827c81fc31ea884fa958205e4fb5ace2d31ac43e2941`.
- At `320×800` in the desktop-browser viewport override, Cost selection and the inspector worked, but a horizontal scrollbar was visible: `scrollWidth=320`, `clientWidth=305`. This is recorded as an observed responsive limitation, not as a no-overflow pass. The approved semantic delta adds interaction/localization JavaScript; it does not change CSS or visible HTML elements. No separate responsive redesign was authorized or applied.
- Direct Progress, Lot and Cost tab selection updated the corresponding diagrams and inspector. WIP, Lot and Cost pain cards selected their corresponding views and smoothly scrolled to the map. Keyboard `ArrowLeft`, `Home`, and `End` navigation worked; `Enter` on Lot and `Space` on Cost pain cards activated the matching view. The RMA and MCU cost controls updated their displayed states.
- Vietnamese, English, Simplified Chinese and Traditional Chinese all updated the document language and map/inspector copy. Source inspection confirms the locale selector updates only the `lang` query key via `URLSearchParams`; no synthetic UTM or click-ID query was sent to production.
- Exactly two Fabless CTA IDs remained. The existing consultation CTA opened its external LadiPage PopupX iframe; it was closed without entering data or submitting the form. The canonical HTML contains no form tags or PopupX provider script, and the revision did not rebind the form.
- The public document DOM fingerprint at the exact route was `37650c411836dfc144f845fe7d2c8a18c38fed587eec40d68b7e8869eeea5d12`. The desktop map witness SHA-256 was `92e6bda9f7e68a2085002a3b39c3f325cc67dbfc11534184af15a54b16f82099`.
- Browser console error review returned none. After scrolling through the page, 29 of 30 images had loaded, none were broken, and one lazy image remained pending.

## Protected state and scope

The bounded source change preserved the tracking/event markers, both CTA IDs, approved static Vietnamese content, page identity/URL, styles, image/preload markup, mobile map toggle and locale selector. The approved PageSpeed decision remains frozen; no new PageSpeed measurement was taken. Existing GTM/bridge and PopupX behavior remain owned by their prior live configuration. No form configuration, campaign, audience, lead, spend or analytics setting was changed.

The local review screenshot is visible in the deployment review session; no screenshot or raw Builder source was added to Git.
