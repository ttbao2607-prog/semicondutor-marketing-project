"""Source-bound proposal renderer. No acceptance or self-learning profiles."""
import base64, hashlib, html, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
PUBLIC_KEYS={'schema_version','release_id','content_revision','case_id','entity_native','entry_ids','default_entry','ready_locales','metric','source','detail_source_url','compatibility','locales'}
LOCALE_KEYS={'scope', 'article_label', 'metric_label', 'title', 'pending', 'intro', 'market_label', 'source_nav', 'problems', 'provider_nav', 'context_nav', 'day_unit', 'language_name', 'source_cta', 'scope_heading', 'reading_heading', 'source_language', 'nav_label', 'source_instruction', 'skip', 'implementation_source_label', 'fallback', 'unavailable_heading', 'project_details', 'language_label', 'reading_questions', 'problem_heading', 'unavailable'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(p):
    if set(p)!=PUBLIC_KEYS:raise ValueError('Unknown/missing public fields')
    if set(p['locales'])!=set(p['ready_locales']) or set(p['ready_locales'])!={'vi','en','zh-Hans','zh-Hant'}:raise ValueError('Locale binding differs')
    if p['default_entry'] not in p['entry_ids']:raise ValueError('Default identity differs')
    for c in p['locales'].values():
        if set(c)!=LOCALE_KEYS:raise ValueError('Unknown/missing locale fields')
        if not c['title'] or not c['intro'] or not c['project_details']:raise ValueError('Reading detail missing')
        for row in c['project_details']:
            if set(row)!={'title','text'}:raise ValueError('Internal detail fields exposed')
    if p['metric'] is not None and set(p['metric'])!={'baseline','result','publisher'}:raise ValueError('Metric fields differ')
def esc(s):return html.escape(str(s),quote=True)
def article(p,l):
    c=p['locales'][l]
    def text(k,tag='p',cls=''):return '<'+tag+(' class="'+cls+'"' if cls else '')+'>'+esc(c[k])+'</'+tag+'>'
    metric=''
    if p['metric'] is not None:
        m=p['metric'];metric='<div class="metric" id="result"><span class="metric-bleed" aria-hidden="true">Digiwin</span><div class="metric-glass">'+text('metric_label','p','metric-label')+'<div class="metric-number" role="img" aria-label="'+esc(c['metric_label']+': '+str(m['baseline'])+' → '+str(m['result'])+' '+c['day_unit'])+'">'+esc(m['baseline'])+' <span class="arrow" aria-hidden="true">→</span> '+esc(m['result'])+' <span class="unit">'+esc(c['day_unit'])+'</span></div><p class="publisher">'+esc(m['publisher'])+'</p></div></div>'
    result='<section id="case-summary"><p class="eyebrow">'+esc(c['article_label'])+'</p><div class="summary"><div class="summary-text">'+text('title','h1')+text('intro','p','intro')+'</div><div class="case-facts"><p class="entity">'+esc(p['entity_native'])+'</p>'+text('market_label','p','market')+metric+'</div></div></section>'
    result+='<nav class="article-nav" aria-label="'+esc(c['nav_label'])+'">'+''.join('<a href="#'+id+'">'+esc(c[key])+'</a>' for id,key in [('context','context_nav'),('provider-role','provider_nav'),('source','source_nav')])+'</nav>'
    result+='<section class="chapter" id="context"><div class="chapter-number" aria-hidden="true">01</div><div class="chapter-content">'+text('problem_heading','h2')+'<ul class="problems">'+''.join('<li>'+esc(x)+'</li>' for x in c['problems'])+'</ul></div></section>'
    result+='<section class="chapter" id="provider-role"><div class="chapter-number" aria-hidden="true">02</div><div class="chapter-content">'+text('scope_heading','h2')+text('scope','p','copy')+''.join('<div class="detail-row"><h3>'+esc(x['title'])+'</h3><p>'+esc(x['text'])+'</p></div>' for x in c['project_details'])
    if p['detail_source_url']:result+='<a class="detail-source" href="'+esc(p['detail_source_url'])+'" target="_blank" rel="noopener noreferrer">'+esc(c['implementation_source_label'])+'</a>'
    result+='</div></section><section class="chapter" id="source"><div class="chapter-number" aria-hidden="true">03</div><div class="chapter-content">'+text('reading_heading','h2')+text('source_instruction','p','copy')+'<p class="source-locator">'+esc(p['entity_native'])+'</p><a class="source-cta" href="'+esc(p['source']['url'])+'" target="_blank" rel="noopener noreferrer">'+esc(c['source_cta'])+'</a><div class="source-bottom">'+text('source_language')+'<label class="locale-select">'+esc(c['language_label'])+'<select id="source-language">'+''.join('<option value="'+x+'"'+(' selected' if x==l else '')+'>'+esc(p['locales'][x]['language_name'])+'</option>' for x in p['ready_locales'])+'</select></label></div></div></section>'
    return result
def render(p,template,router,logo):
    validate(p);sections=['case-summary','context','provider-role','source']+(['result'] if p['metric'] else [])
    cfg={'release_id':p['release_id'],'case_id':p['case_id'],'entries':p['entry_ids'],'default_entry':p['default_entry'],'ready_locales':p['ready_locales'],'sections':sections,'compatibility':p['compatibility']}
    c=p['locales']['vi'];buttons=''.join('<button type="button" data-locale="'+l+'" aria-pressed="'+str(l=='vi').lower()+'">'+esc(p['locales'][l]['language_name'])+'</button>' for l in p['ready_locales'])
    body='<a class="skip" href="#case-summary">'+esc(c['skip'])+'</a><header class="masthead"><div class="wrap"><img class="logo" width="150" height="42" alt="Digiwin" src="data:image/webp;base64,'+base64.b64encode(logo).decode()+'"><div class="languages" role="group" aria-label="'+esc(c['language_label'])+'">'+buttons+'</div></div></header><main class="wrap"><p class="notice" hidden></p><div class="unavailable" hidden><h1>'+esc(c['unavailable_heading'])+'</h1><p>'+esc(c['unavailable'])+'</p></div><article class="sheet" hidden>'+article(p,'vi')+'</article><noscript><p>Tiếng Việt · Bật JavaScript để mở bài viết và chọn ngôn ngữ.</p></noscript></main>'
    app=(ROOT/'app.js').read_text(encoding='utf-8').replace('__PUBLIC__',json.dumps(p,ensure_ascii=False).replace('</','<\\/')).replace('__CONFIG__',json.dumps(cfg,ensure_ascii=False)).replace('__ARTICLES__',json.dumps({l:article(p,l) for l in p['ready_locales']},ensure_ascii=False).replace('</','<\\/'))
    return template.replace('__BODY__',body).replace('__ROUTER__',router).replace('__APP__',app)
def adopted(release,manifest_pin):
    manifest=release/'release-manifest.json'
    if sha(manifest)!=manifest_pin:raise ValueError('Exact owner manifest required')
    m=json.loads(manifest.read_text(encoding='utf-8-sig'));files=m['files'];files=files.items() if isinstance(files,dict) else [(x['path'],x['sha256']) for x in files]
    pins={}
    for name,pin in files:
        f=(release/name).resolve()
        if not f.is_relative_to(release.resolve()) or sha(f)!=pin:raise ValueError('Owner file pin differs')
        pins[name]=pin
    for name in ['public-content.json','template.html','route.js','app.js','digiwin-logo.webp','engine.py','owner-review.json']:
        if name not in pins:raise ValueError('Required reviewed input absent: '+name)
    review=json.loads((release/'owner-review.json').read_text(encoding='utf-8-sig'))
    if review.get('verdict')!='APPROVED_FOR_ONE_BUILD':raise ValueError('Owner has not adopted frame/content')
    if sha(ROOT/'engine.py')!=pins['engine.py']:raise ValueError('Reviewed renderer source differs')
    if sha(ROOT/'app.js')!=pins['app.js']:raise ValueError('Renderer interaction source differs')
    p=json.loads((release/'public-content.json').read_text(encoding='utf-8-sig'))
    if m['release_id']!=p['release_id']:raise ValueError('Release identity differs')
    return p,render(p,(release/'template.html').read_text(encoding='utf-8'),(release/'route.js').read_text(encoding='utf-8'),(release/'digiwin-logo.webp').read_bytes())

def check_document(document,release,manifest_pin):
    """Same observed gate for CLI and every adversarial document test."""
    try:
        payload,expected=adopted(release,manifest_pin)
    except (ValueError,KeyError,OSError) as exc:return ['Owner adoption/reconstruction rejected: '+str(exc)]
    return [] if document==expected else ['Document differs from exact owner frame/public projection: extra/missing/altered text, accessibility, source, identity or control']
