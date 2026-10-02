"""Embed original raster bytes into case-led four-card review fixture."""
from pathlib import Path
import json,base64,re,hashlib,csv
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
copy=json.loads((OUT/'copy-vi.json').read_text(encoding='utf-8'))
records=[{**r,'image':'data:image/png;base64,'+base64.b64encode((OUT/(r['id']+'-native.png')).read_bytes()).decode()} for r in copy['records']]
template=(OUT.parent/'quality-pilot-imagegen-r2/index.html').read_text(encoding='utf-8')
template=re.sub(r'(<script id="copy-source" type="application/json">).*?(</script>)',lambda m:m[1]+json.dumps({'records':records},ensure_ascii=False).replace('</','<\\/')+m[2],template,flags=re.S)
start=template.index('<header class="review">');end=template.index('<main class="workspace"')
template=template[:start]+'''<header class="review"><h1>RMK case R3 · Carousel images 4 card</h1><p class="intro">Pilot theo anchor mới: Digiwin là ai → case nào và vai trò gì → kết quả được công bố → cách tự tra cứu. Case06 tại Trung Quốc, proof vận hành liền kề cold Quality, không phải kết quả xử lý kiểm thử bất thường.</p><div class="tools"><button data-mode="desktop" aria-pressed="true">Desktop 640</button><button data-mode="mobile" aria-pressed="false">Mobile 390</button><button id="reset">Về card đầu</button></div></header><details class="limits"><summary>Phạm vi review và nguồn</summary>PR05 và PR10. Nguồn company-controlled, kết quả publisher-reported, period/method/sample chưa disclosed. Không customer logo hoặc ảnh nhà máy thật. Warm traffic là hypothesis đã được Bảo chấp nhận. Không account/audience/live proof. R2 ad-copy failed giữ nguyên lịch sử; bản này chưa được human accepted. Destination case là metadata, click trong demo bất hoạt.</details>'''+template[end:]
template=template.replace("'RMK · Quality · Nguồn ngành Đài Loan'","'RMK · Digiwin · Case đóng gói và kiểm thử'").replace('n<5','n<4')
(OUT/'index.html').write_text(template,encoding='utf-8')
(OUT/'copy-vi.md').write_text('# R3 exact case-led copy\n\nCaption: '+copy['records'][0]['caption']+'\n\n'+'\n\n'.join(f"## {r['id']}\n\nHeadline: {r['image_headline']}\n\nBody: {r['image_body']}\n\nCue: {r['cue']}\n\nSource/scope: {r['source']}\n\nNative headline: {r['native_headline']}\n\nDestination: {r['destination']}" for r in copy['records']),encoding='utf-8')
assert len(copy['records'])==4 and len(copy['records'][0]['caption'])<=150
assert all(len(r['native_headline'])<=45 for r in copy['records'])
with (OUT/'manifest.csv').open('w',encoding='utf-8',newline='') as out:
 w=csv.writer(out);w.writerow(['path','sha256','bytes'])
 for p in sorted(OUT.iterdir()):
  if p.is_file() and p.name not in ['manifest.csv','human-review-receipt.md']:w.writerow([p.name,hashlib.sha256(p.read_bytes()).hexdigest(),p.stat().st_size])
print('Current demo: four original PNG embedded without transformations.')
