"""Build only the requested B14/B15 offline folder; copy raw PNGs unchanged."""
import hashlib
import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LANE = Path(__file__).resolve().parent.relative_to(ROOT).as_posix()
batch = sys.argv[1]
assert batch in ['B20', 'B21']
locale = 'zh-Hans' if batch == 'B20' else 'zh-Hant'
treatment='f3'
BASE = LANE + '/' + batch + '-' + locale + '-'+treatment+'-v1'
version = sys.argv[2] if len(sys.argv) > 2 else 'v1'
assert version in ['v1', 'v2', 'v3', 'v4']
OUT = ROOT / 'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07' / (batch + '-' + locale + '-'+treatment+'-' + version)
OUT.mkdir(parents=True, exist_ok=True)


def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8-sig'))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def put(p, v):
    p.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


ui = load(BASE + '/ui.json')
attempts = load(BASE + '/attempt-ledger.json')['attempts'] if (ROOT / BASE / 'attempt-ledger.json').exists() else []
reuse = load(BASE + '/reuse-ledger.json')['artwork']
selected = {x['card_id']: x for x in reuse + attempts}
plan = load(BASE + '/dispatch-plan.json')
cards, pins, prompts = [], [], []
for stage in ['cold', 'explanation', 'proof']:
    cp = load(BASE + '/' + stage + '/public-copy.json')
    for c in cp['ads'][0]['cards']:
        row = dict(c, stage=stage, caption=cp['ads'][0]['caption'], image=None)
        if c['card_id'] in selected:
            a = selected[c['card_id']]
            filename = str(len(cards) + 1).zfill(2) + '-' + c['card_id'].lower() + '.png'
            dest = OUT / 'assets' / filename
            dest.parent.mkdir(parents=True, exist_ok=True)
            assert not dest.exists() or sha(dest) == a['sha256'], 'Do not overwrite a different reviewed PNG'
            if not dest.exists():
                shutil.copyfile(ROOT / a['path'], dest)
            assert sha(dest) == a['sha256']
            row['image'] = 'assets/' + filename
            pins.append(dict(card_id=c['card_id'], path=dest.relative_to(ROOT).as_posix(), sha256=sha(dest), source=a['path'], transformation=False))
        cards.append(row)
        if c['card_id'] in selected and selected[c['card_id']]['kind'] == 'reuse':
            oldprompt=selected[c['card_id']]['source_prompt']; prompts.append(dict(oldprompt, card_id=c['card_id'], provenance_original_card_id=oldprompt['card_id'], exact_byte_reuse=True))
        else:
            selected_plan = load(BASE + '/corrective-dispatch-plan.json') if c['card_id'] in selected and selected[c['card_id']]['kind'] == 'corrective' else plan
            jobs = [x for x in selected_plan['calls'] if x['card_id'] == c['card_id']]
            job = jobs[-1]
            spec = load(job['folder'] + '/spec.json')
            prompts.append(dict(card_id=c['card_id'], call_id=job['call_id'], prompt=spec['calls'][0]['prompt'], prompt_sha256=spec['calls'][0]['prompt_sha256'], source_spec=job['folder']+'/spec.json'))
put(OUT / 'selected-copy.json', dict(revision=batch.lower() + '-review-copy-' + locale + '-' + version, cards=cards))
put(OUT / 'selected-prompts.json', dict(revision=batch.lower() + '-review-prompts-' + version, tool='built-in image_gen', calls=prompts))
e = html.escape
style = '''<style>*{box-sizing:border-box}body{margin:0;font-family:Arial,"Microsoft JhengHei","Microsoft YaHei",sans-serif;color:#0b132b;background:#f3f7fc}main{max-width:960px;margin:auto;padding:12px}h1{font-size:25px;line-height:1.4;margin:8px 0}h2{font-size:17px;margin:10px 0}nav{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin:10px 0}button,a{font:inherit}button{padding:7px 11px;min-height:36px;border:1px solid #93abc9;border-radius:6px;background:white;color:#0b132b;cursor:pointer}button[aria-pressed=true]{background:#0052ff;color:white}button:disabled{opacity:.45}a{color:#004adb}article{background:white;border:1px solid #d1deef;border-radius:10px;padding:16px;max-width:674px}#caption,#native{font-size:15px;line-height:1.65;margin:0 0 12px;overflow-wrap:anywhere}#native{font-weight:600;margin:12px 0 0}#art{display:block;width:640px;max-width:100%;height:auto}.feed #art{width:333px}#missing{padding:24px;background:#eef4fc}details{margin:12px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}.reader{max-width:820px;font-size:18px;line-height:1.9}.reader article{max-width:none}.reader h1{font-size:29px}.reader h2{font-size:23px}.entity{font-weight:700;overflow-wrap:anywhere}.source{border-top:1px solid #b4c8e5;margin-top:20px;padding-top:10px}@media(max-width:450px){h1{font-size:22px}article{padding:16px}nav{gap:5px}button{padding:6px 9px}.reader{font-size:16px}.reader h1{font-size:25px}}</style>'''
head = '<!doctype html><html lang="' + locale + '"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
data = json.dumps(cards, ensure_ascii=False).replace('</', '<\\/')
labels = json.dumps(ui, ensure_ascii=False).replace('</', '<\\/')
viewer = (head + '<title>' + e(ui['title']) + '</title>' + style + '<main><h1>' + e(ui['title']) + '</h1>'
          + '<nav aria-label="' + e(ui['select']) + '"><button id="desktop" aria-pressed="true">' + e(ui['desktop']) + '</button><button id="feed" aria-pressed="false">' + e(ui['feed']) + '</button></nav><nav id="cards" aria-label="' + e(ui['select']) + '"></nav><h2 id="stage"></h2><article id="ad"><p id="caption"></p><img id="art" alt=""><div id="missing" hidden></div><p id="native"></p></article><nav><button id="prev">' + e(ui['previous']) + '</button><span id="counter"></span><button id="next">' + e(ui['next']) + '</button><a id="reader" href="case-reader.html">' + e(ui['reader']) + '</a></nav><details><summary>' + e(ui['inspect']) + '</summary><pre id="script"></pre></details></main><script>const data=' + data + ';const labels=' + labels + ';'
          + '''let pos=0;const q=id=>document.getElementById(id);data.forEach((x,i)=>{const b=document.createElement('button');b.id='card-'+(i+1);b.textContent=i+1;b.onclick=()=>show(i);q('cards').append(b)});function show(i){pos=i;const x=data[i];q('stage').textContent=labels[x.stage];q('caption').textContent=x.caption;q('art').hidden=!x.image;q('art').style.display=x.image?'block':'none';if(x.image){q('art').src=x.image;q('art').alt=x.alt}else{q('art').removeAttribute('src');q('art').alt=''}q('missing').hidden=!!x.image;q('missing').textContent=x.headline+' '+x.body;q('native').textContent=x.native_headline;q('counter').textContent=(i+1)+' / '+data.length;q('prev').disabled=i===0;q('next').disabled=i===data.length-1;q('script').textContent=JSON.stringify(x,null,2);Array.from(q('cards').children).forEach((b,k)=>b.setAttribute('aria-pressed',String(k===i)))}q('prev').onclick=()=>show(pos-1);q('next').onclick=()=>show(pos+1);function mode(feed){document.body.classList.toggle('feed',feed);q('feed').setAttribute('aria-pressed',String(feed));q('desktop').setAttribute('aria-pressed',String(!feed))}q('feed').onclick=()=>mode(true);q('desktop').onclick=()=>mode(false);const params=new URLSearchParams(location.search);show(Math.max(0,Math.min(data.length-1,Number(params.get('card')||1)-1)));mode(params.get('mode')==='feed');</script></html>''')
(OUT / 'index.html').write_text(viewer, encoding='utf-8')
r = load(BASE + '/reader-script.json')
reader = (head + '<title>' + e(r['title']) + '</title>' + style + '<main class="reader"><a id="return" href="index.html">' + e(r['return_label']) + '</a><article><p>' + e(ui['case_label']) + '</p><h1>' + e(r['title']) + '</h1><p class="entity">' + e(r['entity']) + '</p><p>' + e(r['intro']) + '</p>'
          + ''.join('<h2>' + e(s['title']) + '</h2><p>' + e(s['text']) + '</p>' for s in r['sections'])
          + '<div class="source"><p>' + e(r['source_language']) + '</p><a href="' + e(r['source_url']) + '">' + e(r['source_cta']) + '</a></div></article><a href="index.html">' + e(r['return_label']) + '</a></main></html>')
(OUT / 'case-reader.html').write_text(reader, encoding='utf-8')
put(OUT / 'manifest.json', dict(revision=batch.lower() + '-review-manifest-' + version, locale=locale,
                               status='GENERATION_IN_PROGRESS' if len(pins) < 11 else 'REVIEW_DRAFT_RENDER_GATE_PENDING',
                               planned_units=11, generated_selected=len(pins), imagegen_original=len([a for a in attempts if a['kind']=='original']),
                               imagegen_corrective=len([a for a in attempts if a['kind']=='corrective']), reused_pngs=len(reuse), tool='built-in image_gen',
                               artwork=pins, viewer_sha256=sha(OUT/'index.html'), reader_sha256=sha(OUT/'case-reader.html'), raster_transformation=False, zip=False))
(OUT / 'README.md').write_text('# ' + batch + ' '+treatment.upper()+' ' + locale + ' offline review\n\n' + str(len(pins)) + '/11 selected native PNGs, copied byte-identically. Open index.html for the localized journey and case-reader.html for the same-language China case summary. Technical status remains review pending; actual postgen receipt lives in the owned operations batch. No independent/native-market/PO/live certification, commit/main/push or later batch. Prompt set: selected-prompts.json.\n', encoding='utf-8')
print(batch + ': built ' + str(len(pins)) + '/11 PNG review positions and localized reader; original native bytes retained.')
