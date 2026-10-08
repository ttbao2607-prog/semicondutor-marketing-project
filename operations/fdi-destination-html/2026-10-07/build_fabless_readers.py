"""Wave 2: build Fabless F1-F3 destination readers (B13-B21) from the approved B7 reader template.

Template: B7 reader (VN Soft Structuralism + Editorial Split, 4-language toggle). The Bright Power case
has no authentic photo, so the hero uses the labelled illustration; the mechanism section lists the
three published challenges only (no invented mechanism, no numbers). Copy: F-copy/common.json
(case-level, 4 locales) + F-copy/treatments.json (F1/F2/F3 persona questions, 4 locales).
"""
import base64, hashlib, html, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
FAB = ROOT / 'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
BASE = ROOT / 'deliverables/linkedin-safe-batches/parallel-osat-2026-10-07/B7-en-o4-o-v1/case-reader.html'
ILLU = PACKET / 'F-illustration/bright-power-illustration-v1.jpg'
TARGETS = [('B13', 'F1', 'en', 'B13-en-f1-v5'), ('B14', 'F1', 'zh-Hans', 'B14-zh-Hans-f1-v1'), ('B15', 'F1', 'zh-Hant', 'B15-zh-Hant-f1-v3'),
           ('B16', 'F2', 'en', 'B16-en-f2-v2'), ('B17', 'F2', 'zh-Hans', 'B17-zh-Hans-f2-v2'), ('B18', 'F2', 'zh-Hant', 'B18-zh-Hant-f2-v4'),
           ('B19', 'F3', 'en', 'B19-en-f3-v1'), ('B20', 'F3', 'zh-Hans', 'B20-zh-Hans-f3-v3'), ('B21', 'F3', 'zh-Hant', 'B21-zh-Hant-f3-v1')]
LANGS = ['vi', 'en', 'zh-Hans', 'zh-Hant']
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
if (PACKET / 'B13-B21-intake.json').exists():
    raise SystemExit('Intake exists; preserve original pins.')
COPY_RE = re.compile(r'(<script type="application/json" id="reader-copy">)(.*?)(</script>)', re.S)
base = BASE.read_text(encoding='utf-8')
b7 = json.loads(COPY_RE.search(base)[2])
common = json.loads((PACKET / 'F-copy/common.json').read_text(encoding='utf-8'))
treat = json.loads((PACKET / 'F-copy/treatments.json').read_text(encoding='utf-8'))
uri = 'data:image/jpeg;base64,' + base64.b64encode(ILLU.read_bytes()).decode()


def packs_for(t):
    out = {}
    for lang in LANGS:
        p = dict(b7[lang])
        p.update(common[lang])
        p.update(treat[t][lang])
        p.pop('m3Title', None)
        p.pop('m3Body', None)
        out[lang] = p
    return out


# structural edits shared by all nine readers
tpl = base
tpl, n = re.subn(r'<li><h3 data-i18n="m3Title"[^>]*>.*?</li>', '', tpl, count=1, flags=re.S)
assert n == 1
tpl, n = re.subn(r'<div class="systems">.*?</div>', '<div class="systems"><span>上海晶丰明源半导体股份有限公司</span></div>', tpl, count=1, flags=re.S)
assert n == 1
tpl, n = re.subn(r'(<img class="case-photo" src=")[^"]+(" width=")1080(" height=")656(")',
                 lambda m: m[1] + uri + m[2] + '1536' + m[3] + '1024' + m[4], tpl, count=1)
assert n == 1
tpl, n = re.subn(r'<a data-i18n="figureSource"[^>]*>(.*?)</a>', r'<span data-i18n="figureSource">\1</span>', tpl, count=1, flags=re.S)
assert n == 1
assert 'data-i18n="m3Title"' not in tpl

intake = {'base_checkpoint': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD']).decode().strip(),
          'template': 'B7-en-o4-o-v1/case-reader.html', 'template_sha256': sha(BASE),
          'illustration_jpg_sha256': sha(ILLU), 'common_sha256': sha(PACKET / 'F-copy/common.json'),
          'treatments_sha256': sha(PACKET / 'F-copy/treatments.json'), 'targets': []}
I18N = re.compile(r'(<[a-z][^>]*\bdata-i18n="([^"]+)"[^>]*>)[^<]*(</[a-z]+>)')
ATTR = re.compile(r'<[a-z][^>]*\bdata-i18n-attr="([^"]+)"[^>]*>')
BTN = re.compile(r'(<button[^>]*data-locale="([^"]+)"[^>]*aria-pressed=")[^"]+(")')
FALLBACK = "if (!allowed.includes(locale)) locale = 'en';"
for batch, t, locale, folder in TARGETS:
    target = FAB / folder
    rec = {'batch': batch, 'treatment': t, 'locale': locale, 'directory': target.relative_to(ROOT).as_posix(),
           'reader_before_sha256': sha(target / 'case-reader.html'), 'index_before_sha256': sha(target / 'index.html'),
           'selected_copy_sha256': sha(target / 'selected-copy.json')}
    packs = packs_for(t)
    pack = packs[locale]
    out = COPY_RE.sub(lambda m: m[1] + json.dumps(packs, ensure_ascii=False) + m[3], tpl)
    out = out.replace('<html lang="en">', '<html lang="' + locale + '">', 1)
    out = re.sub(r'<title>.*?</title>', lambda m: '<title>' + html.escape(pack['title']) + ' | Digiwin</title>', out, count=1)
    out = I18N.sub(lambda m: m[1] + html.escape(pack[m[2]]) + m[3], out)

    def attr(m, pack=pack):
        tag = m[0]
        name, key = m[1].split(':')
        value = name + '="' + html.escape(pack[key], quote=True) + '"'
        tag, c = re.subn(r'\b' + re.escape(name) + r'="[^"]*"', lambda _: value, tag, count=1)
        return tag if c else tag[:-1] + ' ' + value + '>'
    out = ATTR.sub(attr, out)
    out = BTN.sub(lambda m: m[1] + str(m[2] == locale).lower() + m[3], out)
    assert FALLBACK in out
    out = out.replace(FALLBACK, "if (!allowed.includes(locale)) locale = '" + locale + "';")
    assert 'sohu' not in out.lower() and 'm3Title' not in out
    (target / 'case-reader.html').write_text(out, encoding='utf-8')
    idx = target / 'index.html'
    new, c = re.subn(r'href="case-reader\.html(?:\?lang=[^"]+)?"', 'href="case-reader.html?lang=' + locale + '"', idx.read_text(encoding='utf-8-sig'))
    assert c == 1
    idx.write_text(new, encoding='utf-8')
    rec.update(reader_after_sha256=sha(target / 'case-reader.html'), index_after_sha256=sha(idx))
    intake['targets'].append(rec)
(PACKET / 'B13-B21-intake.json').write_text(json.dumps(intake, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('B13-B21 readers built')
