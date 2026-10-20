from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'tmp/reconciliation/evidence'
def extract(n,name,box,marks=()):
 im=Image.open(ROOT/f'tmp/pdfs/document3/page-{n}.png').convert('RGBA')
 sx,sy=im.width/1335,im.height/1888
 b=tuple(round(v*(sx if i%2==0 else sy)) for i,v in enumerate(box))
 out=im.crop(b);ov=Image.new('RGBA',out.size,(0,0,0,0));d=ImageDraw.Draw(ov)
 for m in marks:
  r=tuple(round(v*(sx if i%2==0 else sy))-b[i%2] for i,v in enumerate(m))
  d.rectangle(r,fill=(255,225,0,75))
 Image.alpha_composite(out,ov).convert('RGB').save(OUT/f'{name}.png')
extract(1,'smart_cost',(310,246,1260,411),[(319,292,610,329),(966,249,1248,285),(672,336,779,371)])
extract(1,'smart_billing',(305,592,1261,883),[(319,633,1251,718),(351,726,1253,797),(350,808,1253,876)])
extract(1,'smart_milestone',(305,976,1260,1100),[(350,983,935,1018),(539,1069,671,1098)])
extract(1,'smart_feeders',(305,1178,1262,1601),[(350,1433,1247,1506)])
extract(1,'smart_dates',(310,335,1260,411),[(667,338,779,371),(884,380,1005,410)])
extract(2,'rdss_funding',(233,480,1222,1008),[(506,481,568,512),(1093,665,1209,695),(784,698,916,725),(407,874,567,906),(307,906,1057,937),(594,940,757,970),(1086,940,1208,970),(402,975,617,1004)])
print('Six smart meter source extracts prepared')
