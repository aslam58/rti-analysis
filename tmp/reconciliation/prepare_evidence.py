from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'tmp/reconciliation/evidence'
def extract(path,box,marks=(),disp=None):
 im=Image.open(ROOT/path).convert('RGB')
 if disp:
  sx,sy=im.width/disp[0],im.height/disp[1]
 else:sx=sy=1
 b=tuple(round(v*(sx if i%2==0 else sy)) for i,v in enumerate(box))
 out=im.crop(b).convert('RGBA');ov=Image.new('RGBA',out.size,(0,0,0,0));d=ImageDraw.Draw(ov)
 for m in marks:
  r=tuple(round(v*(sx if i%2==0 else sy))-b[i%2] for i,v in enumerate(m))
  d.rectangle(r,fill=(255,225,0,75))
 return Image.alpha_composite(out,ov).convert('RGB')
def save(name,im):im.save(OUT/(name+'.png'))
def vstack(ims,gap=8):
 w=max(i.width for i in ims);h=sum(i.height for i in ims)+gap*(len(ims)-1)
 o=Image.new('RGB',(w,h),'white');y=0
 for i in ims:o.paste(i,(0,y));y+=i.height+gap
 return o
def hstack(ims,gap=14):
 w=sum(i.width for i in ims)+gap*(len(ims)-1);h=max(i.height for i in ims)
 o=Image.new('RGB',(w,h),'white');x=0
 for i in ims:o.paste(i,(x,0));x+=i.width+gap
 return o
D2=lambda n:f'tmp/pdfs/document2/page-{n}.png'
D1=lambda n:f'tmp/pdfs/document1/page-{n:02}.png'
disp=(1334,1888)
save('no_fppca',extract(D2(2),(620,208,1182,285),[(630,214,1178,278)],disp))
save('cost_comparison',extract(D2(3),(590,786,1185,1136),[(778,1030,1176,1068),(778,1070,1176,1132)],disp))
save('revenue_gap',extract(D2(4),(592,199,1195,271),[(598,211,1187,260)],disp))
save('no_support',extract(D2(3),(599,1692,1190,1808),[(608,1704,1184,1795)],disp))
# The full monthly central grid table and the separate annual quantity table.
save('central_grid',extract('tmp/pdfs/electricity-06.png',(350,136,840,1020),[(500,307,620,1016),(620,307,729,1016)]))
save('regulatory_quantities',extract(D2(2),(614,958,1178,1308),[(802,1097,943,1265)],disp))
# Compact source excerpts keep month quantity and rate in their original order.
# Repeated exchange and trader columns are omitted.
source='tmp/pdfs/electricity-12.png'
heads=[extract(source,(126,159,230,220)),extract(source,(795,159,1070,220))]
for k,(y1,y2) in enumerate([(219,678),(678,1137),(1137,1596)]):
 left=extract(source,(126,y1,230,y2));right=extract(source,(795,y1,1070,y2),[(798,y1+1,875,y2-1)])
 save('market_'+str(k),vstack([hstack(heads,gap=4),hstack([left,right],gap=4)],gap=3))
# Project extracts retain the original column headings.
land=(2009,1248)
rdss=[]
for x1,x2 in [(54,278),(571,766),(929,1104),(1104,1365)]:
 top=extract(D1(4),(x1,220,x2,346),disp=land)
 bottom=extract(D1(4),(x1,577,x2,685),[(1108,591,1357,670)] if x1==1104 else (),land)
 rdss.append(vstack([top,bottom],gap=3))
save('rdss',hstack(rdss,gap=5))
save('modernisation',extract(D1(5),(65,110,767,413),[(289,239,427,356),(435,302,575,357),(580,239,760,401)],(2007,1248)))
# Every monetary row is shown for the two Urban Division budget tables.
# Original account-heading gaps are omitted, while the row sequence is retained.
rev=[]
rev.append(extract(D1(8),(165,166,978,309),disp=disp))
for a,b in [(479,510),(510,565),(565,594),(594,623),(623,652),(816,850),(1070,1104),(1235,1266),(1266,1300),(1380,1425),(1630,1676)]:
 rev.append(extract(D1(8),(165,a,1000,b),[(604,a+1,995,b-1)],disp))
save('urban_revenue',vstack(rev,gap=3))
cap=[extract(D1(9),(203,87,1300,195),disp=disp)]
for a,b in [(465,511),(703,750),(934,981),(1195,1250),(1520,1581)]:
 cap.append(extract(D1(9),(203,a,1300,b),[(796,a+1,1296,b-1)],disp))
save('urban_capital',vstack(cap,gap=5))
save('residential_target',extract(D1(10),(213,316,1177,426),[(285,365,1168,424)],disp))
save('residential_results',extract(D1(10),(216,475,1140,898),[(927,559,1133,642),(928,694,1133,833)],disp))
save('annual_solar',extract(D1(10),(218,928,1143,1011),[(437,973,893,1008)],disp))
save('no_year_target',extract(D1(10),(280,320,1180,377),[(283,320,1175,373)],disp))
save('government_solar',extract(D1(10),(216,1260,1180,1565),[(282,1385,1172,1529),(282,1534,1174,1563)],disp))
save('karaikal',extract(D1(2),(134,419,1195,1277),[(937,497,1180,530)],(1344,1847)))
print('\n'.join(p.name for p in OUT.glob('*.png')))
# Use straightened source rows to avoid clipping sloping table borders.
for n,angle in [(8,-1.0),(9,-1.3)]:
 im=Image.open(ROOT/f'tmp/pdfs/document1/page-{n:02}.png').convert('RGB').resize((1334,1888))
 im=im.rotate(angle,resample=Image.Resampling.BICUBIC,fillcolor='white')
 im.save(ROOT/f'tmp/reconciliation/straight-{n}.png')
rev=[extract('tmp/reconciliation/straight-8.png',(163,163,1005,307))]
for a,b in [(478,506),(506,560),(560,588),(588,616),(616,644),(814,842),(1068,1096),(1236,1264),(1264,1292),(1380,1410),(1635,1663)]:
 rev.append(extract('tmp/reconciliation/straight-8.png',(163,a,1005,b),[(600,a+1,1001,b-1)]))
save('urban_revenue',vstack(rev,gap=6))
cap=[extract('tmp/reconciliation/straight-9.png',(198,85,1300,194))]
for a,b in [(474,505),(708,746),(944,975),(1198,1238),(1500,1574)]:
 cap.append(extract('tmp/reconciliation/straight-9.png',(198,a,1300,b),[(790,a+1,1296,b-1)]))
save('urban_capital',vstack(cap,gap=6))
save('revenue_gap',extract(D2(4),(592,188,1195,267),[(598,194,1187,256)],disp))
save('residential_target',extract(D1(10),(213,316,1177,426),[(282,319,1174,374),(285,375,1168,424)],disp))
# Composite source figures prevent Word from wrapping related extracts onto new lines.
a=Image.open(OUT/'central_grid.png');b=Image.open(OUT/'regulatory_quantities.png')
b=b.resize((630,round(b.height*630/b.width)))
save('quantity_comparison',hstack([a,b],gap=36))
save('market_all',hstack([Image.open(OUT/f'market_{i}.png') for i in range(3)],gap=22))
