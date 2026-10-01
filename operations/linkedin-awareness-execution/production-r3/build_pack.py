"""Deterministic artifact authoring/render script, not a test suite."""
from pathlib import Path
import re, json, base64, html, hashlib, csv, subprocess, time
from PIL import Image, ImageFont, ImageDraw

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'ad-records-vi.md'
STORY=ROOT.parent/'storyboards-vi.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=SOURCE.read_text(encoding='utf-8')
expected='8f51b8d3144670206a2517f1be0b9bc2b4b7f7bcadaa671f0bd666b88a19e052'
if sha(SOURCE)!=expected: raise RuntimeError('Protected input changed')
for sub in ['svg','png','qa']:(ROOT/sub).mkdir(exist_ok=True)
ads=[]
for letter,section in zip(['A','B'],re.split(r'## [AB] — ',source)[1:]):
    section=section.split('## Source mapping')[0]
    caption=re.search(r'caption \((\d+) characters\):\*\*\s*\n([^\n]+)',section)
    ad={'ad_id':'Q-'+letter+'-VI-R3','pov':'O1' if letter=='A' else 'O4-Q','locale':'vi','revision':'R3','status':'TESTING_OFFLINE_DRAFT','caption':caption[2],'caption_count':int(caption[1]),'destination':'https://solutions.digiwin.com.vn/semiconductor-osat?lang=vi','cards':[]}
    for order,chunk in enumerate(re.split(r'### [AB]\d — ',section)[1:],1):
        fields={m[1]:m[2] for m in re.finditer(r'^(Native headline \(\d+\)|Image headline|Image body|Image invitation|Image regional context label|Image regional context|Alt text): `([^`]+)`',chunk,re.M)}
        hkey=next(x for x in fields if x.startswith('Native'))
        card={'order':order,'card_id':letter+str(order),'native_headline':fields[hkey],'headline_count':int(re.search(r'\d+',hkey)[0]),'image_headline':fields['Image headline'],'image_body':fields['Image body'],'alt_text':fields['Alt text'],'brand':'DIGIWIN','category':'ERP · VẬN HÀNH BÁN DẪN','sequence':str(order)+'/5','illustration_label':'Tình huống minh họa' if order<5 else ''}
        for key,label in [('image_invitation','Image invitation'),('regional_label','Image regional context label'),('regional_context','Image regional context')]:
            if label in fields:card[key]=fields[label]
        card['source_ids']='L1;L2;A03;P1' if order<5 else 'L1;L2;A03;P1;P2'
        ad['cards'].append(card)
    ads.append(ad)
if [len(a['cards']) for a in ads]!=[5,5]:raise RuntimeError('Input parse incomplete')
data={'status':'TESTING_OFFLINE_DRAFT','logic_status':'TESTING_NON_CANONICAL','baseline':'71226fec12053857b8e6f8f2579e7c3d791b5ba0','input_copy_sha256':sha(SOURCE),'input_storyboard_sha256':sha(STORY),'ads':ads}
(ROOT/'adcopy.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'adcopy.md').write_text('# Exact R3 copy — TESTING_OFFLINE_DRAFT\n\nInput SHA-256: '+sha(SOURCE)+'\n\n'+source,encoding='utf-8')

fontcss=''
for name,weight in [('Outfit',600),('Outfit',700),('WorkSans',400),('WorkSans',500),('WorkSans',600)]:
    b64=base64.b64encode((ROOT/'dependencies'/f'{name}-{weight}.ttf').read_bytes()).decode()
    fam='Work Sans' if name=='WorkSans' else name
    fontcss+=f"@font-face{{font-family:'{fam}';font-weight:{weight};src:url(data:font/ttf;base64,{b64}) format('truetype');}}"
logo='data:image/webp;base64,'+base64.b64encode((ROOT/'dependencies/digiwin-logo.webp').read_bytes()).decode()
def rect(x,y,w,h,fill='#E9EFF8',stroke='none',rx=20):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
def wrap(text,size,width,family='Work Sans',weight=400):
    name='WorkSans' if family=='Work Sans' else family
    font=ImageFont.truetype(str(ROOT/'dependencies'/f'{name}-{weight}.ttf'),size)
    lines=[];line=''
    for word in text.split():
        new=(line+' '+word).strip()
        if font.getlength(new)>width and line:lines.append(line);line=word
        else:line=new
    if line:lines.append(line)
    return lines
def text(value,x,y,size=46,width=920,family='Work Sans',weight=400,color='#1E293B',lineheight=None):
    lines=wrap(value,size,width,family,weight);lh=lineheight or size*1.25
    return ''.join(f'<text x="{x}" y="{y+i*lh}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}">{html.escape(line)}</text>' for i,line in enumerate(lines)), y+len(lines)*lh
def tile(label,x,y,w=280,h=95):
    t,_=text(label,x+22,y+57,34,w-40,weight=500)
    return rect(x,y,w,h)+t
def diagram(card,letter):
    n=card['order'];s=''
    if n==1:
        labels=['KẾT QUẢ','HỒ SƠ RÀ SOÁT'] if letter=='A' else ['LÔ','NGỮ CẢNH','PHỤ TRÁCH']
    elif n==2:labels=['MÃ LÔ','CÔNG ĐOẠN','THỜI ĐIỂM']
    elif n==3:labels=['NGƯỜI','MÁY','VẬT TƯ','PHƯƠNG PHÁP','MÔI TRƯỜNG']
    else:labels=['NGUỒN HỒ SƠ','NGƯỜI ĐỐI CHIẾU','PHẦN CÒN THIẾU']
    if n==3:
        s+=rect(300,710,480,78,'#FFFFFF','#2563EB')
        t,_=text('KẾT QUẢ KIỂM THỬ',322,761,34,440,weight=600,color='#2563EB');s+=t
        s+='<path d="M540 788V801M224 801H840M224 801V810M532 801V810M840 801V810" stroke="#2563EB" stroke-width="3" fill="none"/>'
        for i,label in enumerate(labels):
            x=80+(i%3)*308;y=810+(i//3)*95;s+=tile(label,x,y,292,76)
    else:
        for i,label in enumerate(labels):
            w=435 if len(labels)==2 else 292;x=80+i*(w+16);s+=tile(label,x,766,w,125)
        if letter=='A':s+='<path d="M100 930H960" stroke="#2563EB" stroke-width="4"/><path d="M940 914L960 930L940 946" fill="none" stroke="#2563EB" stroke-width="4"/>'
        if n==2:
            s+='<path d="M175 905H215M215 905L265 885M215 905L265 925M265 885H300M265 925H300" stroke="#2563EB" stroke-width="4" fill="none"/>'
    return s
layout=[]
for ad in ads:
 for card in ad['cards']:
    letter=card['card_id'][0];n=card['order']
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1080 1080" role="img">',f'<title>{html.escape(card["native_headline"])}</title><desc>{html.escape(card["alt_text"])}</desc>',f'<style>{fontcss}</style>',rect(0,0,1080,1080,'#F8FAFC',rx=0),'<rect x="0" y="0" width="12" height="1080" fill="#2563EB"/>',f'<image href="{logo}" x="80" y="55" width="220" height="62"/>']
    category,_=text(card['category'],80,152,30,920,weight=600,color='#2563EB');parts.append(category)
    heading,end=text(card['image_headline'],80,250,64,920,'Outfit',700);parts.append(heading)
    if n<5:
        body,bend=text(card['image_body'],80,405,46,920);parts.extend([body,diagram(card,letter)])
        label,_=text(card['illustration_label'],80,1010,28,700,color='#475569');parts.append(label)
    else:
        body,bend=text(card['image_body'],80,414,46,920);parts.append(body)
        label,_=text(card['regional_label'],80,575,34,920,weight=600,color='#2563EB');parts.append(label)
        regional,rend=text(card['regional_context'],80,635,42,920);parts.append(regional)
        for i,label in enumerate(['HỒ SƠ','NGỮ CẢNH','PHỤ TRÁCH']):parts.append(tile(label,80+i*308,855,292,82))
        invite,_=text(card['image_invitation'],80,1007,34,820,weight=500,color='#2563EB');parts.append(invite)
    seq,_=text(card['sequence'],935,1010,30,70,weight=500,color='#475569');parts.append(seq);parts.append('</svg>')
    svg=''.join(parts)
    (ROOT/'svg'/f'{card["card_id"]}.svg').write_text(svg,encoding='utf-8')
    layout.append({'card':card['card_id'],'headline_lines':len(wrap(card['image_headline'],64,920,'Outfit',700)),'body_lines':len(wrap(card['image_body'],46,920)),'regional_lines':len(wrap(card.get('regional_context',''),42,920)) if n==5 else 0})
    wrapper=f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;width:1080px;height:1080px;overflow:hidden}}</style>{svg}'
    renderfile=ROOT/'svg'/f'{card["card_id"]}.render.html';renderfile.write_text(wrapper,encoding='utf-8')
    args=['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-first-run','--hide-scrollbars','--force-device-scale-factor=1','--window-size=1080,1080','--virtual-time-budget=3500','--screenshot='+str(ROOT/'png'/f'{card["card_id"]}.png'),renderfile.as_uri()]
    proc=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=45,creationflags=0x08000000)
    if not (ROOT/'png'/f'{card["card_id"]}.png').exists():raise RuntimeError(proc.stderr.decode(errors='replace')[-1000:])
    renderfile.unlink()
(ROOT/'layout-evidence.json').write_text(json.dumps(layout,indent=2),encoding='utf-8')

for ad in ads:
    letter=ad['cards'][0]['card_id'][0]
    sheet=Image.new('RGB',(1620,1110),'#E9EFF8')
    for i,c in enumerate(ad['cards']):
        im=Image.open(ROOT/'png'/f'{c["card_id"]}.png').convert('RGB');im.thumbnail((520,520));sheet.paste(im,((i%3)*540+10,(i//3)*550+10))
        feed=im.copy();feed=Image.open(ROOT/'png'/f'{c["card_id"]}.png').resize((312,312),Image.Resampling.LANCZOS);feed.save(ROOT/'qa'/f'{c["card_id"]}-feed312.png')
    sheet.save(ROOT/'qa'/f'{letter}-contact-sheet.png')

preview='<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Quality R3 review</title><style>*{box-sizing:border-box}body{margin:0;overflow-wrap:anywhere;background:#e9eff8;color:#1e293b;font:17px system-ui;padding:24px}main{max-width:1400px;width:100%;min-width:0;margin:auto}article{min-width:0;max-width:100%;margin:36px 0;padding:24px;background:white;border-radius:20px}.rail{display:flex;gap:20px;overflow-x:auto;padding-bottom:18px}.card{flex:0 0 360px}.card img{display:block;width:100%;height:auto}.headline{font-weight:600;margin:10px 0}small{color:#475569} @media(max-width:500px){body{padding:12px}article{padding:14px}.card{flex-basis:312px}}:focus-visible{outline:3px solid #2563eb}</style><main><h1>Quality OSAT · R3</h1><p>TESTING_OFFLINE_DRAFT · Simulated preview, not LinkedIn account UI. Editorial logic: TESTING_NON_CANONICAL.</p>'
for ad in ads:
    preview+=f'<article><h2>{ad["ad_id"]} · {ad["pov"]}</h2><p>{html.escape(ad["caption"])}</p><small>{ad["caption_count"]} ký tự · VI · 5 card</small><div class="rail">'
    for c in ad['cards']:
        png='data:image/png;base64,'+base64.b64encode((ROOT/'png'/f'{c["card_id"]}.png').read_bytes()).decode()
        preview+=f'<section class="card"><img src="{png}" alt="{html.escape(c["alt_text"],quote=True)}"><p class="headline">{html.escape(c["native_headline"])}</p><small>{c["headline_count"]} ký tự · {c["sequence"]}</small></section>'
    preview+=f'</div><p>Destination draft: <code>{html.escape(ad["destination"])}</code></p></article>'
preview+='</main></html>'; (ROOT/'preview.html').write_text(preview,encoding='utf-8')

def manifest():
    rows=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or p.name=='manifest.csv' or 'browser-export-profile' in p.parts:continue
        rel=p.relative_to(ROOT).as_posix();width=height=''
        if p.suffix=='.png':
            with Image.open(p) as im:width,height=im.size
        elif p.suffix=='.svg':width=height=1080
        card=re.search(r'([AB][1-5])',p.stem);id=card[1] if card else p.stem.upper()
        rows.append({'artifact_id':id,'relative_path':rel,'revision':'R3' if card or p.name in ['adcopy.json','adcopy.md','preview.html'] else 'r1','status':'TESTING_NON_CANONICAL' if p.name=='polish-logic-anchor.md' else 'TESTING_OFFLINE_DRAFT','sha256':sha(p),'bytes':p.stat().st_size,'width':width,'height':height,'anchor_reference':'polish-logic-anchor.md','source_ids':'L1;L2;A03;P1;P2' if card else 'R3-inputs'})
    with (ROOT/'manifest.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
manifest()
print('Pack generated:',len(ads),'ads,',len(list((ROOT/'svg').glob('*.svg'))),'SVG,',len(list((ROOT/'png').glob('*.png'))),'PNG')
print('Protected source hashes:',sha(SOURCE),sha(STORY))
print('Final PNG equal:',sha(ROOT/'png/A5.png')==sha(ROOT/'png/B5.png'))
