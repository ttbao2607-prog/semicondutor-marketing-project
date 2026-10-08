"""Build the offline pre-publish drafts from current main artifacts (read-only inputs).

Outputs (same folder):
  03_LinkedIn_Ad_Build_Sheet.csv / .md   one row per ad (3 ads per journey: cold, explanation, proof)
  04_Review_Items.csv                    de-duplicated customer-visible strings for native/domain review
  04_Native_Review_Packet_<locale>.md    readable packets per locale (en, zh-Hans, zh-Hant, vi)
Inputs: operations/fdi-destination-html/2026-10-07/inventory.csv, each journey index.html, each case-reader.html.
Nothing here is published, uploaded or sent. No metric or ID is invented: URL/IDs stay placeholders.
"""
import csv, json, re, statistics
from collections import OrderedDict, defaultdict
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


def load_journey(path):
    t = (ROOT / path).read_text(encoding='utf-8')
    m = re.search(r'const\s+(?:DATA|data|rows)\s*=\s*', t)
    data, _ = json.JSONDecoder().raw_decode(t[m.end():])
    cards = []
    if isinstance(data, dict) and 'rows' in data:
        for r in data['rows']:
            c = dict(r['copy']); c['stage'] = r['stage']; c['caption'] = r.get('caption', ''); cards.append(c)
    elif isinstance(data, dict) and 'stages' in data:
        for s in data['stages']:
            for c in s['cards']:
                c = dict(c); c.setdefault('caption', s.get('caption', '')); c['stage'] = c.get('stage', s['id']); cards.append(c)
    elif isinstance(data, list) and data and 'copy' in data[0]:
        for r in data:
            c = dict(r['copy']); c['stage'] = r['stage']; c['caption'] = r.get('caption', ''); cards.append(c)
    else:
        cards = [dict(c) for c in data]
    return cards


def load_reader_packs(path):
    t = (ROOT / path).read_text(encoding='utf-8')
    return json.loads(re.search(r'id="reader-copy">(.*?)</script>', t, re.S)[1])


def labels(c):
    v = c.get('artwork_labels') or []
    if isinstance(v, str):
        try:
            v = json.loads(v.replace("'", '"'))
        except Exception:
            v = [v]
    return v


ads = []
review = OrderedDict()   # (locale, text) -> info


def add_review(locale, surface, treatment, batch, key, text, source):
    text = (text or '').strip()
    if not text:
        return
    k = (locale, text)
    if k not in review:
        review[k] = {'locale': locale, 'surface': surface, 'treatment': treatment, 'batches': [], 'keys': [], 'text': text, 'source_ref': source}
    e = review[k]
    if batch not in e['batches']:
        e['batches'].append(batch)
    kk = surface + ':' + key
    if kk not in e['keys']:
        e['keys'].append(kk)


reader_done = set()
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
        for f, surf in (('caption', 'journey caption'), ('headline', 'card headline'), ('body', 'card body'), ('source_text', 'card source line'), ('cta', 'card CTA')):
            add_review(loc, surf, t, jid, c.get('card_id', ''), c.get(f, ''), src)
        for lab in labels(c):
            add_review(loc, 'artwork label', t, jid, c.get('card_id', ''), lab, src)
    for stage, cs in by_stage.items():
        role, fmt, cohort = ROLE[stage]
        caps = list(OrderedDict.fromkeys(c['caption'] for c in cs))
        intro = caps[0]
        last = cs[-1]
        ads.append({
            'ad_key': 'LI-<wave>-%s-%s-%s-v1' % (t.replace('-', ''), loc.replace('-', ''), {'cold': 'COLD', 'explanation': 'EXPL', 'proof': 'PROOF'}[stage]),
            'treatment': t, 'persona': PERSONA[t], 'locale': loc, 'journey_batch': jid, 'role': role, 'format': fmt,
            'objective_proposal': 'Brand awareness (route decision)' if stage == 'cold' else 'RMK objective: Engagement or click to the reader (decision R4)',
            'audience_proposal': 'Company-list audience (state after 10/10 readback), Vietnam, functions and seniority per route' if stage == 'cold' else 'RMK audience from the exact cold source (decisions R1-R3; registry source_id)',
            'card_count': len(cs), 'card_ids': ' | '.join(c.get('card_id', '') for c in cs),
            'intro_text': intro, 'intro_chars': len(intro), 'intro_variants_in_stage': len(caps),
            'card_headlines': ' | '.join(c.get('headline', '').replace('\n', ' ') for c in cs),
            'closing_card_cta_label': last.get('cta', ''),
            'destination_proposal': 'READER ' + route + ' (?lang=' + loc + ') on hosted URL: UNKNOWN' if stage == 'proof' else 'DECISION_NEEDED',
            'destination_note': 'Journey ends at the reader after the proof carousel (inventory + journey viewer).' if stage == 'proof' else 'The journey viewer shows no link at this step; options: reader, Digiwin Vietnam contact page, or the proof carousel. Not decided in the repository.',
            'utm_campaign_pattern': 'fdi_%s_%s_%s_<wave>' % (t.lower().replace('-', ''), loc.lower().replace('-', ''), cohort),
            'utm_content_pattern': '%s_<creative_id>' % jid.lower(),
            'status': 'DRAFT_PROPOSAL', 'source_ref': src})
    # reader strings once per (treatment) set of batches
    rp = load_reader_packs(route)
    for lang, pack in rp.items():
        for k, v in pack.items():
            if isinstance(v, str):
                add_review(lang, 'reader', t, jid, k, v, src)

# ---------------- ad sheet csv
cols = list(ads[0].keys())
with (OUT / '03_LinkedIn_Ad_Build_Sheet.csv').open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator='\r\n'); w.writeheader(); w.writerows(ads)

# ---------------- review items csv
items = list(review.values())
rcols = ['review_id', 'locale', 'surface', 'treatments', 'batches', 'keys', 'chars', 'text', 'source_ref', 'reviewer_verdict', 'suggested_change', 'reviewer_note']
with (OUT / '04_Review_Items.csv').open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, lineterminator='\r\n'); w.writerow(rcols)
    for i, e in enumerate(items, 1):
        w.writerow(['RV%04d' % i, e['locale'], e['surface'], e['treatment'], ' '.join(e['batches']), ' ; '.join(e['keys'][:6]), len(e['text']), e['text'], e['source_ref'], '', '', ''])

# ---------------- review packets per locale
LOCALE_NAME = {'en': 'English', 'zh-Hans': '简体中文 (mainland)', 'zh-Hant': '繁體中文 (Taiwan)', 'vi': 'Tiếng Việt'}
CHECK = {
    'en': ['Plain international English; no idiom or inflated benefit.', 'Terminology: lot, process stage, recording time, handoff, record owner.', 'Claims stay inside the cited source; no outcome, ROI or guarantee.'],
    'zh-Hans': ['简体字、中文标点与行内换行；ERP、iMES、SPC、ECN 等英文缩写前后空格。', '术语是否符合大陆半导体/制造业用法（批次、工序、在制品、核对、委外）。', '公司法定名称保留来源原文；不出现来源以外的结果或承诺。'],
    'zh-Hant': ['繁體字與台灣標點；不是簡轉繁（例如 紀錄/批次/製程/委外/整合式）。', '術語是否符合台灣半導體用法（製程、品質、紀錄、權責）。', '公司法定名稱保留來源原文（可能含簡體字）；不出現來源以外的結果或承諾。'],
    'vi': ['Văn phong tự nhiên cho người đọc doanh nghiệp (Quý Doanh Nghiệp), không dịch máy.', 'Thuật ngữ: lô, công đoạn, thời điểm ghi nhận, bàn giao, hồ sơ nguồn, gia công ngoài.', 'Không hứa kết quả, đạt chuẩn, vượt audit hay có đơn hàng; giữ đúng phạm vi nguồn.']}
for loc in ['en', 'zh-Hans', 'zh-Hant', 'vi']:
    its = [e for e in items if e['locale'] == loc]
    by_t = defaultdict(list)
    for e in its:
        by_t[e['treatment']].append(e)
    lines = ['# Native / domain review packet · %s' % LOCALE_NAME[loc], '',
             'Status: DRAFT for reviewer use, generated %s from current main artifacts. Nothing here is published or sent. Rows with the same text are shown once and list every batch they appear in.' % '2026-10-08', '',
             '**How to review:** read each text as a customer in this market would; mark OK / CHANGE / QUESTION in `04_Review_Items.csv` (columns `reviewer_verdict`, `suggested_change`, `reviewer_note`) using the review ID. Scope covers journey captions, card text and image labels (en, zh-Hans, zh-Hant journeys) and reader pages (all four languages).', '',
             '**What to check**', ''] + ['- ' + c for c in CHECK[loc]] + ['', '**Out of scope here:** product claims about the case itself beyond the cited source; image art direction; VN domestic journeys; legal clearance of photos.', '', '%d unique strings.' % len(its), '']
    ids = {id(e): i for i, e in enumerate(items, 1)}
    for tr in sorted(by_t, key=lambda x: (x[0], x)):
        lines += ['## %s · %s' % (tr, PERSONA[tr]), '', 'Source reference: ' + SOURCE_REF[tr[0]], '']
        for surf in ['journey caption', 'card headline', 'card body', 'card source line', 'card CTA', 'artwork label', 'reader']:
            ss = [e for e in by_t[tr] if e['surface'] == surf]
            if not ss:
                continue
            lines += ['### ' + surf, '']
            for e in ss:
                txt = e['text'].replace('\n', ' / ')
                lines.append('- `RV%04d` [%s] %s' % (ids[id(e)], ' '.join(e['batches']), txt))
            lines.append('')
    (OUT / ('04_Native_Review_Packet_%s.md' % loc)).write_text('\n'.join(lines) + '\n', encoding='utf-8')

# ---------------- summary stats for the md
from collections import Counter
roles = Counter(a['role'] for a in ads)
chars = [a['intro_chars'] for a in ads]
multi = [a for a in ads if a['intro_variants_in_stage'] > 1]
stats = {'ads': len(ads), 'roles': dict(roles), 'intro_chars_min': min(chars), 'intro_chars_median': int(statistics.median(chars)), 'intro_chars_max': max(chars),
         'stages_with_more_than_one_caption': len(multi), 'review_items': len(items), 'review_items_by_locale': dict(Counter(e['locale'] for e in items)),
         'review_items_by_surface': dict(Counter(e['surface'] for e in items))}
(OUT / '_stats.json').write_text(json.dumps(stats, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps(stats, ensure_ascii=False))
