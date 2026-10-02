"""Embed untouched ImageGen raster bytes into versioned carousel demo."""
from pathlib import Path
import json,base64,hashlib,csv,re
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
OLD=OUT.parent/'quality-pilot-r1'
copy=json.loads((OLD/'copy-vi.json').read_text(encoding='utf-8'))
copy.update(revision='quality-rmk-imagegen-r2',format='carousel-images/5-native-ImageGen-PNG',status='OFFLINE_DRAFT_HUMAN_PENDING')
records=[]
for rec in copy['records']:
 p=OUT/(rec['id']+'-native.png');b=p.read_bytes();rec.update(revision=copy['revision']);records.append({**rec,'image':'data:image/png;base64,'+base64.b64encode(b).decode()})
(OUT/'copy-vi.json').write_text(json.dumps(copy,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'copy-vi.md').write_bytes((OLD/'copy-vi.md').read_bytes())
template=(OLD/'index.html').read_text(encoding='utf-8')
template=re.sub(r'(<script id="copy-source" type="application/json">).*?(</script>)',lambda m:m[1]+json.dumps({'records':records},ensure_ascii=False).replace('</','<\\/')+m[2],template,flags=re.S)
template=template.replace('Quality RMK R1','Quality RMK ImageGen R2').replace('SVG vector gốc','Ảnh raster ImageGen').replace('Pilot vector gốc; PNG export 1080 vuông. Chưa native account QA.','5 ảnh raster ImageGen nguyên bản, không SVG. Chưa native account QA.')
template=template.replace('Nối cold O1/O4-Q tới tài liệu ngành Digiwin tại Đài Loan.','Nối cold O1/O4-Q tới tài liệu ngành Digiwin tại Đài Loan. Bản ảnh mới thay candidate vector R1.').replace('SVG vector gốc','Ảnh ImageGen nguyên bản')
(OUT/'index.html').write_text(template,encoding='utf-8')
paths=['operations/linkedin-rmk-proof/quality-pilot-r1/copy-vi.json','operations/linkedin-rmk-proof/quality-pilot-r1/continuity-and-contract.md','operations/linkedin-rmk-proof/proof-ledger.md','operations/linkedin-rmk-proof/implementation-manifest.json']
pins=[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),'revision':'3c5fa3a'} for p in paths]
(OUT/'source-map.json').write_text(json.dumps({'revision':copy['revision'],'inputs':pins,'proof':'PR01 metric-free Taiwan industry context, existing scope; no outcome/customer marks','public_source':'https://www.digiwin.com.tw/dsc/solution/semiconductor/index','artwork':'AI-generated editorial semiconductor imagery; not actual customer/site/product proof','transforms':'none; original PNG bytes embedded'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (OUT/'manifest.csv').open('w',encoding='utf-8',newline='') as out:
 w=csv.writer(out);w.writerow(['path','sha256','bytes'])
 for p in sorted(OUT.iterdir()):
  if p.is_file() and p.name not in ['manifest.csv','human-review-receipt.md']:w.writerow([p.name,hashlib.sha256(p.read_bytes()).hexdigest(),p.stat().st_size])
print('Embedded five original raster images; R1 protected.')
