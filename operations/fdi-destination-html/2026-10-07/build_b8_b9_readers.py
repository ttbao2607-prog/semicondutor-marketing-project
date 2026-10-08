"""Wave 1: B8/B9 O4-O readers = approved B7 reader with route default locale changed.

B8/B9 selected-copy cards are exact zh-Hans/zh-Hant localisations of B7 (same card ids/stages),
so the approved B7 four-language pack is reused. Only html lang, title, active toggle, fallback
locale and the journey entry ?lang= change. Assets/copy/prompts/manifests are untouched.
"""
import hashlib, html, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
OSAT = ROOT / 'deliverables/linkedin-safe-batches/parallel-osat-2026-10-07'
BASE = OSAT / 'B7-en-o4-o-v1/case-reader.html'
TARGETS = [('B8', 'zh-Hans', 'B8-zh-Hans-o4-o-v1'), ('B9', 'zh-Hant', 'B9-zh-Hant-o4-o-v1')]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
if (PACKET / 'B8-B9-intake.json').exists():
    raise SystemExit('Intake exists; preserve original pins.')
base = BASE.read_text(encoding='utf-8')
packs = json.loads(re.search(r'<script type="application/json" id="reader-copy">(.*?)</script>', base, re.S)[1])
intake = {'base_checkpoint': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD']).decode().strip(),
          'base_reader': 'B7-en-o4-o-v1/case-reader.html', 'base_reader_sha256': sha(BASE), 'targets': []}
for batch, locale, folder in TARGETS:
    target = OSAT / folder
    rec = {'batch': batch, 'locale': locale, 'directory': target.relative_to(ROOT).as_posix(),
           'reader_before_sha256': sha(target / 'case-reader.html'), 'index_before_sha256': sha(target / 'index.html'),
           'selected_copy_sha256': sha(target / 'selected-copy.json')}
    pack = packs[locale]
    out = base.replace('<html lang="en">', f'<html lang="{locale}">', 1)
    out = re.sub(r'<title>.*?</title>', '<title>' + html.escape(pack['title']) + ' | Digiwin</title>', out, count=1)
    out = re.sub(r'(<[a-z][^>]*\bdata-i18n="([^"]+)"[^>]*>)[^<]*(</[a-z]+>)', lambda m: m[1] + html.escape(pack[m[2]]) + m[3], out)
    def attr(m):
        tag = m[0]; name, key = m[1].split(':')
        value = name + '="' + html.escape(pack[key], quote=True) + '"'
        tag, c = re.subn(r'\b' + re.escape(name) + r'="[^"]*"', value, tag, count=1)
        return tag if c else tag[:-1] + ' ' + value + '>'
    out = re.sub(r'<[a-z][^>]*\bdata-i18n-attr="([^"]+)"[^>]*>', attr, out)
    out = re.sub(r'(<button[^>]*data-locale="([^"]+)"[^>]*aria-pressed=")[^"]+("[^>]*>)', lambda m: m[1] + str(m[2] == locale).lower() + m[3], out)
    assert "if (!allowed.includes(locale)) locale = 'en';" in out
    out = out.replace("if (!allowed.includes(locale)) locale = 'en';", f"if (!allowed.includes(locale)) locale = '{locale}';")
    (target / 'case-reader.html').write_text(out, encoding='utf-8')
    idx = target / 'index.html'
    new, c = re.subn(r'href="case-reader\.html(?:\?lang=[^"]+)?"', f'href="case-reader.html?lang={locale}"', idx.read_text(encoding='utf-8-sig'))
    assert c == 1
    idx.write_text(new, encoding='utf-8')
    rec.update(reader_after_sha256=sha(target / 'case-reader.html'), index_after_sha256=sha(idx))
    intake['targets'].append(rec)
(PACKET / 'B8-B9-intake.json').write_text(json.dumps(intake, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('B8/B9 built')
