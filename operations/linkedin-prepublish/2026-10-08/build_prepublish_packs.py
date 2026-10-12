"""Build the offline pre-publish drafts from current main artifacts (read-only inputs).

Generated (overwritten on every run) in this folder:
  03_LinkedIn_Ad_Build_Sheet.csv      one row per ad (3 ads per journey: cold, explanation, proof)
  03_LinkedIn_Ad_Cards.csv            one row per card: artwork headline, native headline, body, CTA, alt text, image path
  04_Review_Items.csv                 unique customer-visible strings with STABLE review IDs (hash of locale + text)
  04_Review_Occurrences.csv           every place a string appears: treatment / batch / surface / key / source
  04_Review_Status.csv                UNREVIEWED / REVIEWED per item, joined from the responses file
  04_Review_Orphans.csv               responses whose text no longer exists in the sources (needs re-review)
  04_Native_Review_Packet_<locale>.md readable packets per locale and treatment
  _stats.json
Reviewer-owned (created only if missing, NEVER overwritten):
  04_Review_Responses.csv             reviewer verdicts keyed by review_id

Inputs: operations/fdi-destination-html/2026-10-07/inventory.csv, each journey index.html and case-reader.html.
Nothing here is published or sent. No ID, URL or metric is invented.
"""
import csv, hashlib, json, re, statistics
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent
INV = ROOT / 'operations/fdi-destination-html/2026-10-07/inventory.csv'
rows = list(csv.DictReader(INV.open(encoding='utf-8-sig')))

PERSONA = {'O1': 'OSAT Quality + Operations', 'O2': 'OSAT Operations + Quality (lot handoff)', 'O3': 'OSAT Operations + Finance (month-end)',
           'O4-O': 'OSAT Operations (three handoff questions)', 'O4-Q': 'OSAT Quality (unusual test results)',
           'F1': 'Fabless partner production update', 'F2': 'Fabless demand change / planning', 'F3': 'Fabless partner handoff',
           'P1': 'Supplier operations', 'P2': 'Supplier systems / factory IT', 'P3': 'Supplier quality (PCB)'}
SOURCE_REF = {
    'O': 'Case 06 江苏中科智芯集成科技有限公司 (Digiwin Vietnam case collection, ERP + iMES); O3 adds the attributed month-close case; anchor operations/Vy_Email_Content_Anchor.md',
    'F': 'Case 04 上海晶丰明源半导体股份有限公司 (Digiwin Vietnam case collection; source-stated challenges only, no outcome figures); anchor operations/Vy_Email_Content_Anchor.md',
    'P': 'Wafer Works / 合晶科技 (Digiwin Vietnam supplier LDP and Digiwin Taiwan semiconductor page; claims as stated, not PCB proof); anchor operations/linkedin-safe-batches/parallel-partner-2026-10-07/partner-ldp-content-anchor-v1.md'}
ROLE = {'cold': ('COLD_SINGLE_IMAGE', 'Single image', 'cold'), 'explanation': ('EXPLAIN_CAROUSEL', 'Carousel', 'rmk'), 'proof': ('PROOF_CAROUSEL', 'Carousel', 'rmk')}
SURFACES = ['journey caption', 'card headline (artwork)', 'card native headline', 'card body', 'card source line', 'card CTA', 'artwork label', 'card alt text', 'reader']


def load_journey(path):
    t = (ROOT / path).read_text(encoding='utf-8')
    m = re.search(r'const\s+(?:DATA|data|rows)\s*=\s*', t)
    data, _ = json.JSONDecoder().raw_decode(t[m.end():])
    cards = []
    if isinstance(data, dict) and 'rows' in data:
        for r in data['rows']:
            c = dict(r['copy']); c['stage'] = r['stage']; c['caption'] = r.get('caption', ''); c['image'] = r.get('image', c.get('image', '')); cards.append(c)
    elif isinstance(data, dict) and 'stages' in data:
        for s in data['stages']:
            for c in s['cards']:
                c = dict(c); c.setdefault('caption', s.get('caption', '')); c['stage'] = c.get('stage', s['id']); cards.append(c)
    elif isinstance(data, list) and data and 'copy' in data[0]:
        for r in data:
            c = dict(r['copy']); c['stage'] = r['stage']; c['caption'] = r.get('caption', ''); c['image'] = r.get('image', ''); cards.append(c)
    else:
        cards = [dict(c) for c in data]
    return cards


def load_reader_packs(path):
    """Return (packs, used_keys): only strings the page actually renders are reviewed."""
    t = (ROOT / path).read_text(encoding='utf-8')
    packs = json.loads(re.search(r'id="reader-copy">(.*?)</script>', t, re.S)[1])
    body = re.sub(r'<script type="application/json" id="reader-copy">.*?</script>', '', t, flags=re.S)
    used = set(re.findall(r'data-i18n="([^"]+)"', body))
    for m in re.findall(r'data-i18n-attr="([^"]+)"', body):
        used.add(m.split(':', 1)[1])
    return packs, used


def labels(c):
    v = c.get('artwork_labels') or []
    if isinstance(v, str):
        try:
            v = json.loads(v.replace("'", '"'))
        except Exception:
            v = [v]
    return v


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').replace('\n', ' ')).strip()


def full_sha(locale, text):
    return hashlib.sha1((locale + '|' + text).encode('utf-8')).hexdigest()


def rid(locale, text):
    return 'RV-' + full_sha(locale, text)[:8]


items = OrderedDict()   # (locale, text) -> item
occ = []                # every occurrence


def add_review(locale, surface, treatment, batch, key, text, source):
    text = (text or '').strip()
    if not text:
        return
    k = (locale, text)
    if k not in items:
        items[k] = {'id': rid(locale, text), 'sha1': full_sha(locale, text), 'locale': locale, 'text': text, 'surfaces': [], 'treatments': [], 'batches': [], 'n': 0}
    e = items[k]
    for lst, v in ((e['surfaces'], surface), (e['treatments'], treatment), (e['batches'], batch)):
        if v not in lst:
            lst.append(v)
    e['n'] += 1
    occ.append({'review_id': e['id'], 'locale': locale, 'surface': surface, 'treatment': treatment, 'batch': batch, 'key': key, 'source_ref': source})


ads, ad_cards = [], []
for r in rows:
    t, loc = r['Treatment'], r['Locale']
    route = r['OutputRoute'].split('?')[0]
    d = route.rsplit('/', 1)[0]
    batch = d.rsplit('/', 1)[-1] if not d.endswith('supplier-v7') else d.rsplit('/', 2)[-2]
    bnum = re.match(r'(B\d+)', batch)
    jid = bnum.group(1) if bnum else batch
    cards = load_journey(d + '/index.html')
    src = SOURCE_REF[t[0]]
    by_stage = OrderedDict()
    for c in cards:
        by_stage.setdefault(c['stage'], []).append(c)
        cid = c.get('card_id', '')
        add_review(loc, 'journey caption', t, jid, cid, c.get('caption', ''), src)
        add_review(loc, 'card headline (artwork)', t, jid, cid, c.get('headline', ''), src)
        add_review(loc, 'card native headline', t, jid, cid, c.get('native_headline', ''), src)
        add_review(loc, 'card body', t, jid, cid, c.get('body', ''), src)
        add_review(loc, 'card source line', t, jid, cid, c.get('source_text', ''), src)
        add_review(loc, 'card CTA', t, jid, cid, c.get('cta', ''), src)
        add_review(loc, 'card alt text', t, jid, cid, c.get('alt', ''), src)
        for lab in labels(c):
            add_review(loc, 'artwork label', t, jid, cid, lab, src)
    for stage, cs in by_stage.items():
        role, fmt, cohort = ROLE[stage]
        suffix = {'cold': 'COLD', 'explanation': 'EXPL', 'proof': 'PROOF'}[stage]
        ad_key = 'LI-<wave>-%s-%s-%s-v1' % (t.replace('-', ''), loc.replace('-', ''), suffix)
        caps = list(OrderedDict.fromkeys(c['caption'] for c in cs))
        intro = caps[0]
        last = cs[-1]
        for i, c in enumerate(cs, 1):
            ad_cards.append({'ad_key': ad_key, 'journey_batch': jid, 'locale': loc, 'position': i, 'card_id': c.get('card_id', ''),
                             'artwork_headline': norm(c.get('headline', '')), 'native_headline': norm(c.get('native_headline', '')),
                             'headline_differs': 'yes' if norm(c.get('headline', '')) != norm(c.get('native_headline', '')) else 'no',
                             'body': norm(c.get('body', '')), 'source_line': norm(c.get('source_text', '')), 'cta_label': norm(c.get('cta', '')),
                             'alt_text': norm(c.get('alt', '')), 'artwork_labels': ' / '.join(labels(c)), 'image_path': d + '/' + c.get('image', '')})
        ads.append({
            'ad_key': ad_key, 'treatment': t, 'persona': PERSONA[t], 'locale': loc, 'journey_batch': jid, 'role': role, 'format': fmt,
            'objective_proposal': 'Brand awareness (route decision)' if stage == 'cold' else 'RMK objective: Engagement or click to the reader (decision R4)',
            'audience_proposal': 'Company-list audience (state after 10/10 readback), Vietnam, functions and seniority per route' if stage == 'cold' else 'RMK audience from the exact cold source (decisions R1-R3; registry source_id)',
            'card_count': len(cs), 'card_ids': ' | '.join(c.get('card_id', '') for c in cs),
            'intro_text': intro, 'intro_chars': len(intro), 'intro_variants_in_stage': len(caps),
            'card_native_headlines': ' | '.join(norm(c.get('native_headline', '')) for c in cs),
            'card_artwork_headlines': ' | '.join(norm(c.get('headline', '')) for c in cs),
            'card_alt_texts': ' | '.join(norm(c.get('alt', '')) for c in cs),
            'closing_card_cta_label': last.get('cta', ''),
            'destination_proposal': 'READER ' + route + ' (?lang=' + loc + ') on hosted URL: UNKNOWN' + ('' if stage == 'proof' else ' [D1=A, PROVISIONAL until manager approval]'),
            'destination_note': 'Journey ends at the reader after the proof carousel (inventory + journey viewer).' if stage == 'proof' else 'PO decision D1=A (12/10/2026): sends to the same reader as the proof ad of this journey. PROVISIONAL: final only after the manager approves the package. Hosting route and return link are still open.',
            'platform_cta_button': 'Learn more (PO decision D2, 12/10/2026; availability for this objective/format not verified in the platform UI)',
            'utm_campaign_pattern': 'fdi_%s_%s_%s_<wave>' % (t.lower().replace('-', ''), loc.lower().replace('-', ''), cohort),
            'utm_content_pattern': '%s_<creative_id>' % jid.lower(),
            'status': 'DRAFT_PROPOSAL', 'source_ref': src})
    rp, used = load_reader_packs(route)
    for lang, pack in rp.items():
        for k, v in pack.items():
            if isinstance(v, str) and k in used:
                add_review(lang, 'reader', t, jid, k, v, src)


def write_csv(name, header, rows_):
    with (OUT / name).open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n'); w.writerow(header); w.writerows(rows_)


# ---------------- ad sheet + cards
cols = list(ads[0].keys())
write_csv('03_LinkedIn_Ad_Build_Sheet.csv', cols, [[a[c] for c in cols] for a in ads])
ccols = list(ad_cards[0].keys())
write_csv('03_LinkedIn_Ad_Cards.csv', ccols, [[c[k] for k in ccols] for c in ad_cards])

# ---------------- review items / occurrences (generated)
its = list(items.values())
write_csv('04_Review_Items.csv', ['review_id', 'locale', 'surfaces', 'treatments', 'batches', 'occurrence_count', 'chars', 'text', 'text_sha1'],
          [[e['id'], e['locale'], ' ; '.join(e['surfaces']), ' '.join(e['treatments']), ' '.join(e['batches']), e['n'], len(e['text']), e['text'], e['sha1']] for e in its])
write_csv('04_Review_Occurrences.csv', ['review_id', 'locale', 'surface', 'treatment', 'batch', 'key', 'source_ref'],
          [[o['review_id'], o['locale'], o['surface'], o['treatment'], o['batch'], o['key'], o['source_ref']] for o in occ])

# ---------------- reviewer-owned responses: create only if missing; join for status / orphans
RESP = OUT / '04_Review_Responses.csv'
RHEAD = ['review_id', 'locale', 'text_sha1_at_review', 'reviewer', 'reviewed_on', 'verdict', 'suggested_change', 'reviewer_note']
if not RESP.exists():
    with RESP.open('w', encoding='utf-8', newline='') as f:
        csv.writer(f, lineterminator='\r\n').writerow(RHEAD)
resp = {}
for r in csv.DictReader(RESP.open(encoding='utf-8', newline='')):
    if r.get('review_id'):
        resp[r['review_id']] = r
by_id = {e['id']: e for e in its}
status_rows, orphan_rows = [], []
for e in its:
    r = resp.get(e['id'])
    if not r:
        st = 'UNREVIEWED'
    elif r.get('text_sha1_at_review') and r['text_sha1_at_review'] != e['sha1']:
        st = 'NEEDS_RECHECK'
    else:
        st = 'REVIEWED'
    status_rows.append([e['id'], e['locale'], ' '.join(e['treatments']), st, resp.get(e['id'], {}).get('verdict', '')])
for k, r in resp.items():
    if k not in by_id:
        orphan_rows.append([k, r.get('locale', ''), r.get('verdict', ''), r.get('suggested_change', ''), r.get('reviewer_note', ''), 'Text no longer present in the sources (changed or removed): re-review the replacement item'])
write_csv('04_Review_Status.csv', ['review_id', 'locale', 'treatments', 'status', 'verdict'], status_rows)
write_csv('04_Review_Orphans.csv', ['review_id', 'locale', 'verdict', 'suggested_change', 'reviewer_note', 'reason'], orphan_rows)

# ---------------- packets per locale, grouped by treatment from OCCURRENCES (not first-seen)
LOCALE_NAME = {'en': 'English', 'zh-Hans': '简体中文 (mainland)', 'zh-Hant': '繁體中文 (Taiwan)', 'vi': 'Tiếng Việt'}
CHECK = {
    'en': ['Plain international English; no idiom or inflated benefit.', 'Terminology: lot, process stage, recording time, handoff, record owner.', 'Claims stay inside the cited source; no outcome, ROI or guarantee.'],
    'zh-Hans': ['简体字、中文标点与行内换行；ERP、iMES、SPC、ECN 等英文缩写前后空格。', '术语是否符合大陆半导体/制造业用法（批次、工序、在制品、核对、委外）。', '公司法定名称保留来源原文；不出现来源以外的结果或承诺。'],
    'zh-Hant': ['繁體字與台灣標點；不是簡轉繁（例如 紀錄/批次/製程/委外/整合式）。', '術語是否符合台灣半導體用法（製程、品質、紀錄、權責）。', '公司法定名稱保留來源原文（可能含簡體字）；不出現來源以外的結果或承諾。'],
    'vi': ['Văn phong tự nhiên cho người đọc doanh nghiệp (Quý Doanh Nghiệp), không dịch máy.', 'Thuật ngữ: lô, công đoạn, thời điểm ghi nhận, bàn giao, hồ sơ nguồn, gia công ngoài.', 'Không hứa kết quả, đạt chuẩn, vượt audit hay có đơn hàng; giữ đúng phạm vi nguồn.']}
for loc in ['en', 'zh-Hans', 'zh-Hant', 'vi']:
    loc_items = [e for e in its if e['locale'] == loc]
    grid = defaultdict(lambda: defaultdict(OrderedDict))   # treatment -> surface -> review_id -> [batches]
    for o in occ:
        if o['locale'] == loc:
            b = grid[o['treatment']][o['surface']].setdefault(o['review_id'], [])
            if o['batch'] not in b:
                b.append(o['batch'])
    lines = ['# Native / domain review packet · %s' % LOCALE_NAME[loc], '',
             'Status: DRAFT for reviewer use, generated from current main artifacts. Nothing here is published or sent. IDs (`RV-xxxxxxxx`) are stable: they come from the locale and the exact text, so they do not change when the generator is rerun; a changed text gets a new ID. The same ID can appear under several treatments and surfaces; `04_Review_Occurrences.csv` lists every occurrence with its batch and source.', '',
             '**How to review:** read each text as a customer in this market would and record OK / CHANGE / QUESTION in `04_Review_Responses.csv` (never overwritten by the generator). Scope: journey captions, artwork headlines, platform native headlines, card text, image labels, source lines, CTAs and alt text (en, zh-Hans, zh-Hant journeys) and reader pages (all four languages).', '',
             '**What to check**', ''] + ['- ' + c for c in CHECK[loc]] + ['',
             '**Out of scope here:** product claims about the case itself beyond the cited source; image art direction; VN domestic journeys; legal clearance of photos.', '', '%d unique strings.' % len(loc_items), '']
    for tr in sorted(grid, key=lambda x: (x[0], x)):
        lines += ['## %s · %s' % (tr, PERSONA[tr]), '', 'Source reference: ' + SOURCE_REF[tr[0]], '']
        for surf in SURFACES:
            ids_ = grid[tr].get(surf)
            if not ids_:
                continue
            lines += ['### ' + surf, '']
            for i, b in ids_.items():
                lines.append('- `%s` [%s] %s' % (i, ' '.join(b), by_id[i]['text'].replace('\n', ' / ')))
            lines.append('')
    (OUT / ('04_Native_Review_Packet_%s.md' % loc)).write_text('\n'.join(lines) + '\n', encoding='utf-8')

# ---------------- stats
roles = Counter(a['role'] for a in ads)
chars = [a['intro_chars'] for a in ads]
stats = {'ads': len(ads), 'ad_cards': len(ad_cards), 'roles': dict(roles), 'cards_where_native_headline_differs_from_artwork_headline': sum(1 for c in ad_cards if c['headline_differs'] == 'yes'),
         'intro_chars_min': min(chars), 'intro_chars_median': int(statistics.median(chars)), 'intro_chars_max': max(chars),
         'stages_with_more_than_one_caption': sum(1 for a in ads if a['intro_variants_in_stage'] > 1),
         'review_items': len(its), 'review_occurrences': len(occ), 'review_items_by_locale': dict(Counter(e['locale'] for e in its)),
         'occurrences_by_surface': dict(Counter(o['surface'] for o in occ)), 'items_in_more_than_one_treatment': sum(1 for e in its if len(e['treatments']) > 1),
         'responses': len(resp), 'orphan_responses': len(orphan_rows)}
(OUT / '_stats.json').write_text(json.dumps(stats, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps(stats, ensure_ascii=False))
