"""Check retained copy against all inventory sources; never change the package."""
import csv
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HTML = ROOT / 'deliverables/unified-case-reader/unified-case-reader.html'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def data_script(text, script_id):
    match = re.search(r'<script[^>]*id="' + re.escape(script_id) + r'"[^>]*>(.*?)</script>', text, re.S)
    assert match, script_id
    return json.loads(match[1])


class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.external = []
        self.forms = []
        self.offline_links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('img', 'script', 'iframe', 'link', 'source', 'video', 'audio'):
            for key in ('src', 'href', 'srcset'):
                value = attrs.get(key)
                if value and not value.startswith(('data:', '#')):
                    self.external.append((tag, key, value))
        if tag in ('form', 'input', 'textarea', 'select', 'iframe'):
            self.forms.append(tag)
        if tag == 'a' and attrs.get('href') == 'index.html':
            self.offline_links.append(attrs['href'])


def inspect():
    text = HTML.read_text(encoding='utf-8')
    copies = data_script(text, 'all-copies')
    entries = data_script(text, 'o2-entry-copies')
    parser = Resources()
    parser.feed(text)
    assert len(copies) == 11
    assert not parser.external, parser.external
    assert not parser.forms, parser.forms
    assert not parser.offline_links
    assert '<main id="main" class="shell">' in text
    assert not re.search(r'@import|url\(\s*[\'"]?https?://', text)
    assert not re.search(r'\b(?:fetch|sendBeacon|XMLHttpRequest|dataLayer|gtag)\b', text)
    inventory = ROOT / 'operations/fdi-destination-html/2026-10-07/inventory.csv'
    rows = list(csv.DictReader(inventory.open(encoding='utf-8-sig')))
    assert len(rows) == 33
    comparisons = []
    for row in rows:
        path = ROOT / row['OutputRoute'].split('?')[0]
        source = data_script(path.read_text(encoding='utf-8'), 'reader-copy')
        treatment, entry_locale = row['Treatment'], row['Locale']
        entry = {'en': 'B4', 'zh-Hans': 'B5', 'zh-Hant': 'B6'}[entry_locale] if treatment == 'O2' else None
        target = entries[entry] if entry else copies[treatment]
        assert set(source) == set(target) == {'vi', 'en', 'zh-Hans', 'zh-Hant'}
        assert source == target, (treatment, entry_locale, path)
        comparisons.append({'treatment': treatment, 'entry_locale': entry_locale,
                            'entry': entry, 'source': path.relative_to(ROOT).as_posix(),
                            'source_sha256': digest(path), 'all_four_locale_packs_equal': True,
                            'titles': {loc: pack['title'] for loc, pack in target.items()}})
    return {'artifact': HTML.relative_to(ROOT).as_posix(), 'sha256': digest(HTML),
            'bytes': HTML.stat().st_size,
            'anchor_sha256': digest(ROOT / 'operations/Vy_Email_Content_Anchor.md'),
            'email_sha256': digest(ROOT / 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),
            'source_routes': comparisons, 'source_locale_comparisons': len(rows) * 4,
            'external_automatic_resources': parser.external, 'forms': parser.forms,
            'offline_return_links': parser.offline_links,
            'scope': 'Copy retention and structural checks; not semantic/native/live acceptance.'}


if __name__ == '__main__':
    print(json.dumps(inspect(), ensure_ascii=True, indent=2))
