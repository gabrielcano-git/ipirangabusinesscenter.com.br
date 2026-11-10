import urllib.request,urllib.parse,urllib.error,json,concurrent.futures,pathlib,datetime
root=pathlib.Path('comparativos/2026-11-10/evidencias');urls={'antigo':'https://www.ipirangabusinesscenter.com.br/','novo':'https://gabrielcano-git.github.io/ipirangabusinesscenter.com.br/'}
def collect(pair):
 kind,mode=pair;params=[('url',urls[kind]),('strategy',mode)]+[('category',c) for c in ['performance','accessibility','best-practices','seo']];url='https://www.googleapis.com/pagespeedonline/v5/runPagespeed?'+urllib.parse.urlencode(params)
 record={'site':kind,'url':urls[kind],'mode':mode,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(url,timeout=180);body=r.read();record['status']=r.status
 except urllib.error.HTTPError as e:body=e.read();record['status']=e.code
 except Exception as e:body=json.dumps({'error':str(e)}).encode();record['error']=str(e)
 (root/f'pagespeed-{kind}-{mode}.json').write_bytes(body)
 try:
  d=json.loads(body);lh=d.get('lighthouseResult',{});record['scores']={k:v.get('score') for k,v in lh.get('categories',{}).items()};record['metrics']={k:lh.get('audits',{}).get(k,{}).get('numericValue') for k in ['largest-contentful-paint','total-blocking-time','cumulative-layout-shift']};record['field']=d.get('loadingExperience');record['originField']=d.get('originLoadingExperience');record['errorResponse']=d.get('error')
 except Exception:pass
 return record
with concurrent.futures.ThreadPoolExecutor(4) as pool:records=list(pool.map(collect,[(k,m) for k in urls for m in ['mobile','desktop']]))
(root/'pagespeed-coleta.json').write_text(json.dumps(records,ensure_ascii=False,indent=2));print([(r['site'],r['mode'],r.get('status'),r.get('scores')) for r in records])
