from html.parser import HTMLParser
import pathlib,json,re,urllib.request,concurrent.futures,hashlib
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.images=[];self.active=None;self.parts=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t in ['p','h1','h2','h3','h4','h5','h6'] and self.active is None:self.active=t;self.parts=[]
  if t=='br' and self.active:self.parts.append('\n')
  if t=='img' and a.get('src','').startswith('https://static.wixstatic.com/media/'):self.images.append(a)
 def handle_data(self,s):
  if self.active:self.parts.append(s)
 def handle_endtag(self,t):
  if t==self.active:
   s=''.join(self.parts).strip().replace('\u200b','').replace('\xa0',' ')
   if s:self.text.append({'tag':t,'text':s})
   self.active=None
pages={}
for f in pathlib.Path('auditorias/2026-11-10/evidencias').glob('*.html'):
 p=Parser();p.feed(f.read_text());pages[f.stem]={'blocks':p.text,'images':p.images}
assets={}
for p in pages.values():
 for im in p['images']:
  base=im['src'].split('/v1/')[0]
  assets[base]={'file':hashlib.sha256(base.encode()).hexdigest()[:16]+('.png' if '.png' in base else '.jpg'),'url':base}
def get(item):
 url,a=item;target=pathlib.Path('public/assets')/a['file']
 try:
  if not target.exists():target.write_bytes(urllib.request.urlopen(url+'/v1/fit/w_1440,h_1000,q_82/'+url.split('/')[-1],timeout=40).read())
  return None
 except Exception as e:return (url,str(e))
print('Download:',len(assets),list(filter(None,concurrent.futures.ThreadPoolExecutor(10).map(get,assets.items()))))
for p in pages.values():
 for im in p['images']:im['local']='/assets/'+assets[im['src'].split('/v1/')[0]]['file']
pathlib.Path('src/data/pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
for k,p in pages.items():
 if k not in ['home','contato','escritorio-virtual','quem-somos','servicos','ipiranga-training','salas-de-reuniao','sala-comercial-privativa','locacao-de-sala-para-treinamento']:print(k,p['blocks'])
