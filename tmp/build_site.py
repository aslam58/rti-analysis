import ast,json,re,shutil,html
from pathlib import Path
root=Path(__file__).resolve().parents[1]
out=root/'sites/electricity-evidence/dist'
tree=ast.parse((root/'tmp/reconciliation/build_summary.py').read_text())
findings=[];cur=None
for n in tree.body:
 if not isinstance(n,ast.Expr) or not isinstance(n.value,ast.Call) or not isinstance(n.value.func,ast.Name):continue
 c=n.value;name=c.func.id
 if name=='page':
  title=ast.literal_eval(c.args[0]);cur={'title':re.sub(r'^\d+ ','',title),'parts':[]};findings.append(cur)
 elif cur is not None and name in ['p','caption','image','table']:
  try:cur['parts'].append({'type':name,'args':[ast.literal_eval(a) for a in c.args]})
  except:pass
(out/'findings.json').write_text(json.dumps(findings))
for f in findings:
 for p in f['parts']:
  if p['type']=='image':shutil.copy(root/'tmp/reconciliation/evidence'/f"{p['args'][0]}.png",out/'assets')
for src,dest in [('electricity.pdf','source-a.pdf'),('Electricity_document_1.pdf','source-b.pdf'),('Electricity_document_2.pdf','source-c.pdf'),('Smart Meter Project_electricity_document_3.pdf','source-d.pdf')]:shutil.copy((root/'inputs')/src,out/'assets'/dest)
shutil.copy(root/'output/docx/Puducherry_Electricity_RTI_Reconciled_Summary.docx',out/'assets/electricity-report.docx')
