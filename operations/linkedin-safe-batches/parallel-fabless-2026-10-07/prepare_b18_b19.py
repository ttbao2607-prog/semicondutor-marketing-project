"""Owned B18/B19 assembly using unchanged frozen validators. Never calls ImageGen."""
import sys
from pathlib import Path
batch=sys.argv[2]
assert batch in ['B18','B19']
treatment='f2' if batch=='B18' else 'f3'
p=Path(__file__).with_name('prepare_f2_batches.py')
s=p.read_text(encoding='utf8').split("if __name__=='__main__':")[0]
s=s.replace("locale='en' if batch=='B16' else 'zh-Hans'", "locale='en' if batch=='B19' else 'zh-Hant'")
s=s.replace("locale = 'en' if batch == 'B16' else 'zh-Hans'", "locale = 'en' if batch == 'B19' else 'zh-Hant'")
s=s.replace("'/B13-en-f1-v5' if locale=='en' else '/B14-zh-Hans-f1-v1'", "'/B16-en-f2-v2' if locale=='en' else '/B15-zh-Hant-f1-v3'")
s=s.replace("source_prompts={x['card_id']:x for x in load(baseline+'/selected-prompts.json')['calls']}", "source_prompts={c['card_id']:p for c,p in zip(baseline_cards,load(baseline+'/selected-prompts.json')['calls'])}")
s=s.replace('f2-authored-input.json','b18-b19-authored-input.json')
s=s.replace("(V5 if locale=='en' else LANE+'/B14-zh-Hans-f1-v1')", "(LANE+'/B16-en-f2-v1' if locale=='en' else LANE+'/B15-zh-Hant-f1-v1')")
s=s.replace("'Return to the planning journey' if locale=='en' else '返回委外计划主题'", "'Return to the handoff journey' if locale=='en' else '返回委外計畫主題'")
s=s.replace("(batch=='B16' and i==1)", "False").replace("(batch=='B16' and stage=='proof' and i==1)", "False")
s=s.replace("reference_art=DEL+'/B14-zh-Hans-f1-v1/assets/'+('06-f1-a5.png' if stage=='explanation' else '09-rmk-bright-2.png')", "reference_art=origin_art['path']")
s=s.replace("instruction='commit đi codex, r chạy 2 batch kế.'", "instruction='Okie chạy tiếp 2 batch kế.'")
s=s.replace("scope='B16 F2 English and B17 F2 Simplified Chinese; same anchor/persona/Vietnam nuance.11selected positions with reviewed same-locale reuse, not11new calls.'", "scope='B18 Traditional Chinese F2 and B19 English F3. Same Operations/SCM persona, B13v5 anchor/visual/Vietnam nuance.11positions;6new+5exact same-locale reuse.'")
s=s.replace('original_cap=10','original_cap=11').replace('10original+2corrective','11original+2corrective')
s=s.replace('Stop before B18; new Git mutation after B14/B15 checkpoint not included.', 'Stop before B20; no commit/main integration/push/live mandate in this run.')
s=s.replace('Stop before B18.','Stop before B20.')
s=s.replace('explicit PO B16/B17 mandate','explicit PO B18/B19 mandate')
s=s.replace('explicit PO B14/B15 mandate','explicit PO B18/B19 mandate')
s=s.replace(".replace('original_cap=11','original_cap=10')",'')
s=s.replace('English proof2 rebuilt because its original paper lines are not literally blank; no inherited B13 preservation exception for this new output.', 'All five reused native PNGs are selected corrected same-locale finals; fresh current-context review required. No inherited PASS.')
s=s.replace('10original+2corrective/onepercard','11original+2corrective/onepercard')
if batch=='B19':
 s=s.replace('f2','f3').replace('F2','F3').replace('B16-en-f3','B16-en-f2')
 s=s.replace('demand-change cold -> F3 planning reconciliation','partner-handoff cold -> F3 lot/record/confirmation coordination')
 s=s.replace('localized planning-question reader','localized handoff-question reader')
 s=s.replace('a shared basis for replanning and accountable partner confirmations','a shared basis for partner handoff coordination and accountable confirmations')
 s=s.replace('F3 is a planning lens','F3 is a handoff coordination lens').replace('Demand-change planning hook','Partner handoff coordination hook')
 s=s.replace('Demand-change questions','Partner handoff questions')
 s=s.replace('Bright neutral desk, blank partner report sheets beside a wafer protective carrier; separate sheets represent reports to reconcile, not actual statuses or forecast charts.', 'Two neutral partner work areas, a sealed wafer protective carrier and wholly blank accompanying record sheets at a handoff point. No actual customer shipment or shipping status.')
 s=s.replace('A neutral packaged chip and small lot trays beside blank report sheets; product and lot scope are illustrative, no printed identifiers or technical layouts.', 'One neutral handoff point between two plain chip trays with blank accompanying sheets. Product and lot scope illustrative; no printed identifiers or technical layout.')
 s=s.replace('Separate blank partner reports and neutral wafer protective carrier; differing report sources are abstract, no dates, status values, clock faces or technical UI.', 'A neutral chip tray beside two distinct wholly blank record sheets and a simple magnifying lens. Abstract comparison of record sources, no printed IDs, dates, status values or technical UI.')
 s=s.replace('Blank open folder, neutral chip tray and simple unlabelled responsibility nodes with open connectors; no check marks, completed workflow, screens or record values.', 'Two neutral unlabelled responsibility nodes on opposite sides of a chip tray and a wholly blank paper sheet; no check marks, completed workflow, screens or record values.')
 s=s.replace('Grouped blank partner reports, neutral chip carrier and responsibility nodes on white; a shared discussion basis, no automatic planning engine or results.', 'Small neutral sealed chip carrier between two plain pale-blue geometric tiles on white. No document pictogram, folded corner, ruled paper, arrows, status glyph, automated engine or completed result. Shared coordination discussion basis only.')
else:
 s=s.replace('Grouped blank partner reports, neutral chip carrier and responsibility nodes on white; a shared discussion basis, no automatic planning engine or results.', 'Small neutral sealed chip carrier between two plain pale-blue geometric tiles on white. No document pictogram, folded corner, ruled paper, arrows, status glyph, automated engine or completed result. Shared planning discussion basis only.')
env={'__file__':str(p.resolve())}
exec(compile(s,str(p),'exec'),env)
assert sys.argv[1] in ['author','release']
env[sys.argv[1]](batch)
