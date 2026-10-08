import hashlib, json, pathlib
from datetime import datetime,timezone
root=pathlib.Path(__file__).resolve().parents[3]; rec=pathlib.Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
data=json.loads((rec/'prepared-copy.json').read_text(encoding='utf-8'))
units=[]
for g in data['groups']:
    for i,r in enumerate(g['rows'],1):
        units.append({'group':g['id'],'unit':i,'segment':'VN_DOMESTIC' if g['locale']=='vi-VN' else 'FDI','locale':g['locale'],
          'stage':r['stage'],'observed_headline':r['headline'],'caption':r['caption'],'body':r['body'],
          'selected_png_sha256':r['sha256'],
          'A1':'Packaging/testing supply-chain activity; VN management readiness to supply chain.' if g['locale']=='vi-VN' else 'Packaging/testing plant decision unit, not group-global software replacement.',
          'A2':'Readiness discussion for relevant enterprise decision unit.' if g['locale']=='vi-VN' else 'Quality/Operations job named in caption; O3 is explicitly Operations handing records to Finance.',
          'A3':'Quý Doanh Nghiệp; same-language selected journey.' if g['locale']=='vi-VN' else g['persona']+'; '+g['language']+'; same-language case destination.',
          'A4':'N/A: domestic readiness branch.' if g['locale']=='vi-VN' else 'Implicit value: aligned context, ownership, handoff or reduced month-end waiting; no new ROI guarantee.',
          'A5':'Preparation of management/process/records, not guaranteed admission/audit pass.' if g['locale']=='vi-VN' else 'N/A: FDI existing-operations branch.',
          'A6':'China Aplus iMES + TOP GP case separate from local ERP readiness; 3 months whole-project go-live only.' if g['locale']=='vi-VN' else ('O3: China integrated-solution 15-to-5-day month-close result, not local/ERP-only forecast.' if g['family']=='O3' else 'China ERP+iMES/MES linked records, SPC/ECN/exception mechanisms; no ERP-only equipment-control claim.'),
          'A7':'Hook → mechanism → named proof → same-family reader → return; no persona/locale switch.',
          'verdict':'MESSAGE_ANCHOR_PASS','review_basis':'Root read actual prepared copy; original accepted artwork only planned byte-preserved reuse. No new ImageGen.'})
receipt={'artifact_revision':'package-v2-phase3-1.0','stage':'PREGEN_SCRIPT','reviewed_utc':datetime.now(timezone.utc).isoformat(),
 'reviewer':'/root','independence':'SELF_REVIEW','anchor_id':'VY-CONTENT-ANCHOR','anchor_revision':'1.0',
 'anchor_sha256':sha(root/'operations/Vy_Email_Content_Anchor.md'),
 'email_record_id':'VY-MAIL-USER-20261006','email_sha256':sha(root/'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),
 'prepared_copy_sha256':sha(rec/'prepared-copy.json'), 'workflow_sha256':sha(root/'operations/manager-package-v2/Package_V2_Workflow_Anchor_2026-10-07.md'),
 'executive_surfaces':{'proposal':'Supply-chain ICP; separate VN/FDI value; cap/net-tax/weekly-review fidelity; three Vy feedback points.',
                      'email':'Vy ơi / Bảo gửi Vy / Cảm ơn Vy, Bảo; Vy review and aggregate; no inferred budget reply.',
                      'package_wrapper':'Simulated flow only; operational autonomy belongs to Bảo; clean business navigation.',
                      'workbook':'Proposed budget inputs distinct from blank actuals; platform spend and matched-period ratios; no approval fields.'},
 'units':units,'render_state':'POSTGEN_NOT_RUN; package not yet constructed; no new artwork generation planned.',
 'verdict':'MESSAGE_ANCHOR_PASS','scope':'Prepared content before assembly; does not certify unseen finished renders or authorize live release.'}
(rec/'pregen-review.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print('PREGEN_SCRIPT: 170 planned units bound; root semantic review; no ImageGen dispatch.')
