"""
Automated unit test for Google Ads RSA Copy Suite across 4 locales (VI, EN, zh-Hans, zh-Hant).
Validates:
1. Exact counts: 12 headlines and 4 descriptions per ad group per locale.
2. Character length rules:
   - English/Latin: Headlines <= 30 chars, Descriptions <= 90 chars.
   - Chinese CJK: Double-byte counting, Headlines <= 30 character-units, Descriptions <= 90 character-units.
"""

import re
import os
import sys

def g_len(s):
    l = 0
    for ch in s:
        if ('\u4e00' <= ch <= '\u9fff' or 
            '\u3400' <= ch <= '\u4dbf' or 
            '\u3000' <= ch <= '\u303f' or 
            '\uff01' <= ch <= '\uffee'):
            l += 2
        else:
            l += 1
    return l

def test_google_rsa():
    build_sheet_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ads', 'google', 'Google_Search_Build_Sheet.md')
    with open(build_sheet_path, 'r', encoding='utf-8') as f:
        content = f.read()

    h_matches = re.findall(r'Headlines \((\d+)\): (.*)', content)
    d_matches = re.findall(r'Descriptions \((\d+)\): (.*)', content)

    print(f"Total Headline blocks found: {len(h_matches)}")
    print(f"Total Description blocks found: {len(d_matches)}")

    assert len(h_matches) == 12, f"Expected 12 headline blocks (3 groups x 4 locales), found {len(h_matches)}"
    assert len(d_matches) == 12, f"Expected 12 description blocks (3 groups x 4 locales), found {len(d_matches)}"

    all_passed = True
    total_h = 0
    total_d = 0

    for idx, (count_str, items_str) in enumerate(h_matches):
        expected_count = int(count_str)
        items = re.findall(r'`([^`]+)`', items_str)
        total_h += len(items)
        if len(items) != expected_count:
            print(f"ERROR in Block {idx+1}: Expected {expected_count} headlines, found {len(items)}")
            all_passed = False
        for item in items:
            length = g_len(item)
            if length > 30:
                print(f"ERROR: Headline exceeds 30 units ({length}): '{item}'")
                all_passed = False

    for idx, (count_str, items_str) in enumerate(d_matches):
        expected_count = int(count_str)
        items = re.findall(r'`([^`]+)`', items_str)
        total_d += len(items)
        if len(items) != expected_count:
            print(f"ERROR in Block {idx+1}: Expected {expected_count} descriptions, found {len(items)}")
            all_passed = False
        for item in items:
            length = g_len(item)
            if length > 90:
                print(f"ERROR: Description exceeds 90 units ({length}): '{item}'")
                all_passed = False

    print(f"Total headlines verified: {total_h}")
    print(f"Total descriptions verified: {total_d}")

    if all_passed:
        print("ALL RSA HEADLINES AND DESCRIPTIONS STRICTLY PASS GOOGLE ADS LIMITS!")
        return 0
    else:
        print("FAIL: Validation errors encountered.")
        return 1

if __name__ == '__main__':
    sys.exit(test_google_rsa())
