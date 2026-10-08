"""Wave 4: build O4-Q readers B10/B11/B12 from the approved B7 reader template.

Same case as B7-B9 (江苏中科智芯集成科技有限公司, Digiwin Vietnam case 06): case context, mechanism section and the
authentic 2020 visit photo with its source line are inherited. Only the Quality-persona questions and
bridge/consult copy change (OQ-copy/o4q.json), following the O4-Q journey cards B1-B5.
"""
import hashlib, html, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
OSAT = ROOT / 'deliverables/linkedin-safe-batches/parallel-osat-2026-10-07'
BASE = OSAT / 'B7-en-o4-o-v1/case-reader.html'
TARGETS = [('B10', 'en', 'B10-en-o4-q-v1'), ('B11', 'zh-Hans', 'B11-zh-Hans-o4-q-v1'), ('B12', 'zh-Hant', 'B12-zh-Hant-o4-q-v1')]
LANGS = ['vi', 'en', 'zh-Hans', 'zh-Hant']
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
if (PACKET / 'B10-B12-intake.json').exists():
    raise SystemExit('Intake exists; preserve original pins.')
COPY_RE = re.compile(r'(<script type="application/json" id="reader-copy">)(.*?)(</script>)', re.S)
base = BASE.read_text(encoding='utf-8')
b7 = json.loads(COPY_RE.search(base)[2])
over = json.loads((PACKET / 'OQ-copy/o4q.json').read_text(encoding='utf-8'))
packs = {}
for lang in LANGS:
    p = dict(b7[lang])
    assert all(k in p for k in over[lang]), lang
    p.update(over[lang])
    packs[lang] = p
out0 = COPY_RE.sub(lambda m: m[1] + json.dumps(packs, ensure_ascii=False) + m[3], base)
I18N = re.compile(r'(<[a-z][^>]*\bdata-i18n="([^"]+)"[^>]*>)[^<]*(</[a-z]+>)')
ATTR = re.compile(r'<[a-z][^>]*\bdata-i18n-attr="([^"]+)"[^>]*>')
BTN = re.compile(r'(<button[^>]*data-locale="([^"]+)"[^>]*aria-pressed=")[^"]+(")')
FALLBACK = "if (!allowed.includes(locale)) locale = 'en';"
intake = {'base_checkpoint': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD']).decode().strip(),
          'template': 'B7-en-o4-o-v1/case-reader.html', 'template_sha256': sha(BASE), 'o4q_copy_sha256': sha(PACKET / 'OQ-copy/o4q.json'), 'targets': []}
for batch, locale, folder in TARGETS:
    target = OSAT / folder
    rec = {'batch': batch, 'locale': locale, 'directory': target.relative_to(ROOT).as_posix(),
           'reader_before_sha256': sha(target / 'case-reader.html'), 'index_before_sha256': sha(target / 'index.html'),
           'selected_copy_sha256': sha(target / 'selected-copy.json')}
    p = packs[locale]
    out = out0.replace('<html lang="en">', '<html lang="' + locale + '">', 1)
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
    (target / 'case-reader.html').write_text(out, encoding='utf-8')
    idx = target / 'index.html'
    new, c = re.subn(r'href="case-reader\.html(?:\?lang=[^"]+)?"', 'href="case-reader.html?lang=' + locale + '"', idx.read_text(encoding='utf-8-sig'))
    assert c == 1
    idx.write_text(new, encoding='utf-8')
    rec.update(reader_after_sha256=sha(target / 'case-reader.html'), index_after_sha256=sha(idx))
    intake['targets'].append(rec)
(PACKET / 'B10-B12-intake.json').write_text(json.dumps(intake, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('B10-B12 readers built')
