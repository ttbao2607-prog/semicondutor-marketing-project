"""Wave 3: build Partner P1-P3 destination readers (B22-B30) from the approved B7 reader template.

Content: existing reviewed reader-copy.json of each treatment in en / zh-Hans / zh-Hant (from B22-B30 themselves)
plus the authored Vietnamese pack P-copy/vi.json. Hero: labelled Wafer Works illustration (no authentic photo found).
No CTA button is added (the stub readers had none); sources keep their two links.
"""
import base64, hashlib, html, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
PAR = ROOT / 'deliverables/linkedin-safe-batches/parallel-partner-2026-10-07'
BASE = ROOT / 'deliverables/linkedin-safe-batches/parallel-osat-2026-10-07/B7-en-o4-o-v1/case-reader.html'
ILLU = PACKET / 'F-illustration/wafer-works-illustration-v1.jpg'
# batch, treatment, default locale, reader directory (B22 reader lives in supplier-v7)
TARGETS = [('B22', 'P1', 'en', 'B22-en-p1-v1/supplier-v7'), ('B23', 'P1', 'zh-Hans', 'B23-zh-Hans-p1-v1'), ('B24', 'P1', 'zh-Hant', 'B24-zh-Hant-p1-v2'),
           ('B25', 'P2', 'en', 'B25-en-p2-v1'), ('B26', 'P2', 'zh-Hans', 'B26-zh-Hans-p2-v1'), ('B27', 'P2', 'zh-Hant', 'B27-zh-Hant-p2-v1'),
           ('B28', 'P3', 'en', 'B28-en-p3-v1'), ('B29', 'P3', 'zh-Hans', 'B29-zh-Hans-p3-v1'), ('B30', 'P3', 'zh-Hant', 'B30-zh-Hant-p3-v1')]
LANGS = ['vi', 'en', 'zh-Hans', 'zh-Hant']
SOURCE_BATCH = {'P1': {'en': 'B22', 'zh-Hans': 'B23', 'zh-Hant': 'B24'}, 'P2': {'en': 'B25', 'zh-Hans': 'B26', 'zh-Hant': 'B27'}, 'P3': {'en': 'B28', 'zh-Hans': 'B29', 'zh-Hant': 'B30'}}
DIRS = {b: d for b, _, _, d in TARGETS}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
PREV = json.loads((PACKET / 'B22-B30-intake.json').read_text(encoding='utf-8')) if (PACKET / 'B22-B30-intake.json').exists() else None  # rerun keeps original before-pins
COPY_RE = re.compile(r'(<script type="application/json" id="reader-copy">)(.*?)(</script>)', re.S)
base = BASE.read_text(encoding='utf-8')
b7 = json.loads(COPY_RE.search(base)[2])
vi = json.loads((PACKET / 'P-copy/vi.json').read_text(encoding='utf-8'))
common = json.loads((PACKET / 'P-copy/common.json').read_text(encoding='utf-8'))
uri = 'data:image/jpeg;base64,' + base64.b64encode(ILLU.read_bytes()).decode()
reader_copy = {}
for t, per in SOURCE_BATCH.items():
    reader_copy[t] = {'vi': vi[t]}
    for lang, b in per.items():
        reader_copy[t][lang] = json.loads((PAR / DIRS[b] / 'reader-copy.json').read_text(encoding='utf-8-sig'))
        assert reader_copy[t][lang]['locale'] == lang


def pack(t, lang):
    c = reader_copy[t][lang]
    p = dict(b7[lang])
    for k in ('title', 'lead', 'caseLabel', 'figure', 'figureSource', 'figureAlt', 'market'):
        p.pop(k, None)
    for k in ('m0Title', 'm0Body', 'm1Title', 'm1Body', 'm2Title', 'm2Body', 'm3Title', 'm3Body'):
        p.pop(k, None)
    p.update(common[lang])
    p.update({'title': c['title'], 'lead': c['intro'], 'caseLabel': c['eyebrow'].title() if lang in ('en', 'vi') else c['eyebrow'],
              'back': c['return_label'], 'articleLabel': c['title']})
    assert len(c['sections']) == 4 and [len(s['paragraphs']) for s in c['sections']] == [2, 2, 3, 2]
    for i, s in enumerate(c['sections'], 1):
        p['s%dh' % i] = s['heading']
        for j, para in enumerate(s['paragraphs'], 1):
            p['s%dp%d' % (i, j)] = para
    srcs = c['sources']
    p['src1'] = srcs[0]['label'] if isinstance(srcs[0], dict) else srcs[0]
    p['src2'] = srcs[1]['label'] if isinstance(srcs[1], dict) else srcs[1]
    return p


def sections_html():
    out = []
    for i in (1, 2, 3):
        paras = ''.join('<p data-i18n="s%dp%d" class="body-copy" ></p>' % (i, j) for j in range(1, 3 if i < 3 else 4))
        chip = '<div class="systems"><span>Wafer Works / 合晶科技</span></div>' if i == 3 else ''
        out.append('<section class="section"><p class="section-index"><span>0%d</span><span data-i18n="s%dIndex" ></span></p><div><h2 data-i18n="s%dh" ></h2>%s%s</div></section>' % (i, i, i, paras, chip))
    return ''.join(out)


def urls(t):
    s = reader_copy[t]['en']['sources']
    return s[0]['url'], s[1]['url']


tpl = base
tpl, n = re.subn(r'<article .*?</article>', lambda m: '<article data-i18n-attr="aria-label:articleLabel" aria-label="">' + sections_html() + '</article>', tpl, count=1, flags=re.S)
assert n == 1
tpl, n = re.subn(r'<section class="consult">.*?</section>', '<section class="consult"><div class="consult-inner"><p data-i18n="consultLabel" class="section-label" ></p><h2 data-i18n="s4h" ></h2><p data-i18n="s4p1" ></p><p data-i18n="s4p2" ></p></div></section>', tpl, count=1, flags=re.S)
assert n == 1
tpl, n = re.subn(r'(<img class="case-photo" src=")[^"]+(" width=")1080(" height=")656(")', lambda m: m[1] + uri + m[2] + '1536' + m[3] + '1024' + m[4], tpl, count=1)
assert n == 1
tpl, n = re.subn(r'<a data-i18n="figureSource"[^>]*>(.*?)</a>', r'<span data-i18n="figureSource">\1</span>', tpl, count=1, flags=re.S)
assert n == 1
assert not re.search(r'data-i18n="m[0-9]', tpl)

intake = {'base_checkpoint': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD']).decode().strip(),
          'template': 'B7-en-o4-o-v1/case-reader.html', 'template_sha256': sha(BASE),
          'illustration_jpg_sha256': sha(ILLU), 'illustration_png_sha256': sha(PACKET / 'F-illustration/wafer-works-illustration-v1.png'),
          'vi_copy_sha256': sha(PACKET / 'P-copy/vi.json'), 'common_sha256': sha(PACKET / 'P-copy/common.json'), 'targets': []}
I18N = re.compile(r'(<[a-z][^>]*\bdata-i18n="([^"]+)"[^>]*>)[^<]*(</[a-z]+>)')
ATTR = re.compile(r'<[a-z][^>]*\bdata-i18n-attr="([^"]+)"[^>]*>')
BTN = re.compile(r'(<button[^>]*data-locale="([^"]+)"[^>]*aria-pressed=")[^"]+(")')
FALLBACK = "if (!allowed.includes(locale)) locale = 'en';"
SRC_ANCHOR = '<section class="source"><strong data-i18n="sourceLabel" ></strong><div><p><a data-i18n="src1" href="%s" target="_blank" rel="noopener noreferrer"></a></p><p><a data-i18n="src2" href="%s" target="_blank" rel="noopener noreferrer"></a></p></div></section>'
for batch, t, locale, folder in TARGETS:
    target = PAR / folder
    rec = {'batch': batch, 'treatment': t, 'locale': locale, 'reader_dir': target.relative_to(ROOT).as_posix(),
           'reader_before_sha256': sha(target / 'case-reader.html'), 'index_before_sha256': sha(target / 'index.html'),
           'reader_copy_sha256': sha(target / 'reader-copy.json')}
    if PREV:
        old = next(x for x in PREV['targets'] if x['batch'] == batch)
        rec['reader_before_sha256'], rec['index_before_sha256'] = old['reader_before_sha256'], old['index_before_sha256']
        rec['rebuilt_after_label_fix'] = True
    packs = {lang: pack(t, lang) for lang in LANGS}
    u1, u2 = urls(t)
    cur = re.sub(r'<section class="source">.*?</section>', lambda m: SRC_ANCHOR % (u1, u2), tpl, count=1, flags=re.S)
    assert SRC_ANCHOR % (u1, u2) in cur
    p = packs[locale]
    out = COPY_RE.sub(lambda m: m[1] + json.dumps(packs, ensure_ascii=False) + m[3], cur)
    out = out.replace('<html lang="en">', '<html lang="' + locale + '">', 1)
    out = re.sub(r'<title>.*?</title>', lambda m: '<title>' + html.escape(p['title']) + ' | Digiwin</title>', out, count=1)
    out = I18N.sub(lambda m: m[1] + html.escape(p[m[2]]) + m[3], out)

    def attr(m, p=p):
        tag = m[0]
        name, key = m[1].split(':')
        value = name + '="' + html.escape(p[key], quote=True) + '"'
        tag, c = re.subn(r'\b' + re.escape(name) + r'="[^"]*"', lambda _: value, tag, count=1)
        return tag if c else tag[:-1] + ' ' + value + '>'
    out = ATTR.sub(attr, out)
    out = BTN.sub(lambda m: m[1] + str(m[2] == locale).lower() + m[3], out)
    assert FALLBACK in out
    out = out.replace(FALLBACK, "if (!allowed.includes(locale)) locale = '" + locale + "';")
    plain = re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', out).lower()
    for w in ('sohu', 'undefined'):
        assert w not in plain, (batch, w)
    (target / 'case-reader.html').write_text(out, encoding='utf-8')
    idx = target / 'index.html'
    new, c = re.subn(r'href="case-reader\.html(?:\?lang=[^"]+)?"', 'href="case-reader.html?lang=' + locale + '"', idx.read_text(encoding='utf-8-sig'))
    assert c == 1
    idx.write_text(new, encoding='utf-8')
    rec.update(reader_after_sha256=sha(target / 'case-reader.html'), index_after_sha256=sha(idx))
    intake['targets'].append(rec)
(PACKET / 'B22-B30-intake.json').write_text(json.dumps(intake, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('B22-B30 readers built')
