"""Adapt approved B1 O1 reader to each existing Chinese journey route."""
import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
BASE = ROOT / 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html'
TARGETS = [
    ('B2', 'zh-Hans', 'deliverables/linkedin-safe-batches/2026-10-06/B2-zh-Hans-o1-v1'),
    ('B3', 'zh-Hant', 'deliverables/linkedin-safe-batches/2026-10-07/B3-zh-Hant-o1-v1'),
]
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
base = BASE.read_text(encoding='utf-8')
packs = json.loads(re.search(r'<script type="application/json" id="reader-copy">(.*?)</script>', base, re.S).group(1))
intake = {'base_checkpoint': 'ac7df75', 'base_reader_sha256': digest(BASE), 'targets': []}
for batch, locale, relative in TARGETS:
    directory = ROOT / relative
    selected = json.loads((directory / 'selected-copy.json').read_text(encoding='utf-8-sig'))
    assert '江苏中科智芯集成科技有限公司' in json.dumps(selected, ensure_ascii=False)
    assert 'ERP + iMES' in json.dumps(selected, ensure_ascii=False)
    entry = directory / 'index.html'
    copy = packs[locale]
    output = base.replace('<html lang="en">', f'<html lang="{locale}">', 1)
    output = re.sub(r'<title>.*?</title>', '<title>' + html.escape(copy['title']) + ' | Digiwin</title>', output, count=1)

    # Initial static text/attributes are localized too; no browser-language/storage override.
    def localize_text(match):
        return match[1] + html.escape(copy[match[2]]) + match[3]
    output = re.sub(r'(<[a-z][^>]*\bdata-i18n="([^"]+)"[^>]*>)[^<]*(</[a-z]+>)', localize_text, output)
    def localize_attr(match):
        tag = match[0]
        attr, key = match[1].split(':')
        tag, count = re.subn(r'\b' + re.escape(attr) + r'="[^"]*"', attr + '="' + html.escape(copy[key], quote=True) + '"', tag, count=1)
        if count == 0:
            tag = tag[:-1] + ' ' + attr + '="' + html.escape(copy[key], quote=True) + '">'
        return tag
    output = re.sub(r'<[a-z][^>]*\bdata-i18n-attr="([^"]+)"[^>]*>', localize_attr, output)
    output = re.sub(r'(<button[^>]*data-locale="([^"]+)"[^>]*aria-pressed=")[^"]+("[^>]*>)', lambda m: m[1] + str(m[2] == locale).lower() + m[3], output)
    output = output.replace("if (!allowed.includes(locale)) locale = 'en';", f"if (!allowed.includes(locale)) locale = '{locale}';")
    assert output != base and 'href="index.html"' in output
    entry_before = entry.read_text(encoding='utf-8-sig')
    entry_after, count = re.subn(r'href="case-reader\.html(?:\?lang=[^"]+)?"', f'href="case-reader.html?lang={locale}"', entry_before)
    assert count == 1
    record = {'batch': batch, 'locale': locale, 'directory': relative,
              'selected_copy_sha256': digest(directory / 'selected-copy.json'),
              'manifest_sha256': digest(directory / 'manifest.json'),
              'closing_card': selected['cards'][-1], 'reader_before_sha256': digest(directory / 'case-reader.html'),
              'entry_before_sha256': digest(entry), 'photo_provenance': 'B1-photo-research/provenance.json'}
    (directory / 'case-reader.html').write_text(output, encoding='utf-8', newline='\n')
    entry.write_text(entry_after, encoding='utf-8', newline='\n')
    record.update(reader_after_sha256=digest(directory / 'case-reader.html'), entry_after_sha256=digest(entry))
    intake['targets'].append(record)
(PACKET / 'B2-B3-intake.json').write_text(json.dumps(intake, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
print('B2/B3 built; initial locales zh-Hans/zh-Hant; all4 toggles; local journey returns.')
