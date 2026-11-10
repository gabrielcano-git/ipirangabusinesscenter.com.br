import urllib.request,urllib.error,urllib.parse,json,pathlib,concurrent.futures,datetime,re
from html.parser import HTMLParser
ROOT=pathlib.Path('comparativos/2026-11-10/evidencias')
BASES={'antigo':'https://www.ipirangabusinesscenter.com.br','novo':'https://gabrielcano-git.github.io/ipirangabusinesscenter.com.br'}
ROUTES=['home','quem-somos','servicos','sala-comercial-privativa','salas-de-reuniao','locacao-de-sala-para-treinamento','escritorio-virtual','ipiranga-training','contato','coaching','consultoria','cursos-palestras','servicos-de-rh','fotos','rooms-rates','p-gina-em-tela-cheia']
class Inspect(HTMLParser):
 def __init__(self):
  super().__init__();self.headings=[];self.blocks=[];self.inputs=[];self.images=[];self.links=[];self.meta=[];self.scripts=[];self.labels=[];self.linktags=[];self.captures=[];self.html={};self.forms=[];self.buttons=[];self.styles=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='html':self.html=a
  if t=='meta':self.meta.append(a)
  if t=='link':self.linktags.append(a)
  if t=='img':self.images.append(a)
  if t in ['input','textarea','select']:self.inputs.append(a|{'tag':t})
  if t=='script':self.scripts.append(a)
  if t=='form':self.forms.append(a)
  if t in ['h1','h2','h3','h4','h5','h6','p','a','label','title','button','style']:self.captures.append({'tag':t,'attrs':a,'parts':[]})
  if t=='br':
   for c in self.captures:c['parts'].append('\n')
 def handle_data(self,d):
  for c in self.captures:c['parts'].append(d)
 def handle_endtag(self,t):
  for i in range(len(self.captures)-1,-1,-1):
   if self.captures[i]['tag']==t:
    c=self.captures.pop(i);s=' '.join(''.join(c['parts']).replace('\u200b','').split());x={'tag':t,'text':s,'attrs':c['attrs']}
    if t.startswith('h') and t[1:].isdigit():self.headings.append(x)
    if t in ['p','h1','h2','h3','h4','h5','h6']:self.blocks.append(x)
    if t=='a':self.links.append(x)
    if t=='label':self.labels.append(x)
    if t=='button':self.buttons.append(x)
    if t=='title':self.title=s
    if t=='style':self.styles.append(''.join(c['parts']))
    break
 def result(self):return {k:v for k,v in self.__dict__.items() if k in ['title','headings','blocks','inputs','images','links','meta','scripts','labels','linktags','html','forms','buttons']}
def fetch(kind,route):
 url=BASES[kind]+('/' if route=='home' else '/'+route+('/' if kind=='novo' else ''))
 record={'kind':kind,'route':route,'requested':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 SiteComparison/1.0'}),timeout=45)
  body=r.read();record.update(status=r.status,url=r.url,headers=dict(r.headers),bytes=len(body));(ROOT/f'{kind}-{route}.html').write_bytes(body)
  p=Inspect();p.feed(body.decode('utf-8','replace'));record['document']=p.result()
  if route=='home' and kind=='novo':(ROOT/'novo-home-css.css').write_text('\n'.join(p.styles))
 except Exception as e:record.update(error=str(e),status=getattr(e,'code',None))
 return record
with concurrent.futures.ThreadPoolExecutor(10) as pool:records=list(pool.map(lambda x:fetch(*x),[(k,r) for k in BASES for r in ROUTES]))
(ROOT/'inventario.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print('Páginas:',[(r['kind'],r['route'],r.get('status'),r.get('bytes')) for r in records])
extras=[]
for k in BASES:
 for file in ['robots.txt','sitemap.xml']:
  url=BASES[k]+'/'+file
  try:
   r=urllib.request.urlopen(url,timeout=30);body=r.read();(ROOT/f'{k}-{file}').write_bytes(body);extras.append({'url':url,'status':r.status,'headers':dict(r.headers),'text':body.decode('utf8','replace')[:5000]})
  except Exception as e:extras.append({'url':url,'error':str(e),'status':getattr(e,'code',None)})
(ROOT/'extras.json').write_text(json.dumps(extras,ensure_ascii=False,indent=2))
# Sem carregar scripts externos, check HTTP dos destinos locais das páginas novas.
urls=set()
for record in records:
 if record['kind']!='novo' or 'document' not in record:continue
 d=record['document']
 for item in d['images']:
  urls.add(urllib.parse.urljoin(record['url'],item.get('src','')))
  for attr in ['srcset']:
   for v in item.get(attr,'').split(', '):
    if v:urls.add(urllib.parse.urljoin(record['url'],v.split(' ')[0]))
 for item in d['scripts']:
  if item.get('src'):urls.add(urllib.parse.urljoin(record['url'],item['src']))
 for link in d['links']:
  href=link['attrs'].get('href','')
  if href.startswith('/'):urls.add(urllib.parse.urljoin(record['url'],href).split('#')[0])
def check(url):
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,method='HEAD'),timeout=30);return {'url':url,'status':r.status,'headers':dict(r.headers)}
 except Exception as e:return {'url':url,'status':getattr(e,'code',None),'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(10) as pool:checks=list(pool.map(check,sorted(urls)))
(ROOT/'destinos-novo.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print('Destinos:',len(checks),'falhas:',[(r['url'],r['status']) for r in checks if r['status']!=200])
# Salvar JS real publicado para verificar o fluxo, sem executar envios.
for r in checks:
 if r['url'].endswith('/site.js') and r['status']==200:(ROOT/'novo-site.js').write_bytes(urllib.request.urlopen(r['url']).read())
