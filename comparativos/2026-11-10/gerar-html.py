from pathlib import Path
import html,re
root=Path('comparativos/2026-11-10')
text=(root/'comparativo-antigo-novo.md').read_text()
def inline(s):
 s=html.escape(s)
 s=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',lambda m:f'<a class="capture" href="{m[2]}"><img loading="lazy" src="{m[2]}" alt="{m[1]}"><span>Ampliar captura</span></a>',s)
 s=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 return s
lines=text.splitlines();body=[];i=0
while i<len(lines):
 line=lines[i]
 if not line.strip():i+=1;continue
 if line.startswith('# '):i+=1;continue
 if line.startswith('##'):
  level=len(line)-len(line.lstrip('#'));title=line[level:].strip();anchor=re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-');body.append(f'<h{level} id="{anchor}">{inline(title)}</h{level}>');i+=1;continue
 if line.startswith('|'):
  table=[]
  while i<len(lines) and lines[i].startswith('|'):
   row=lines[i].strip('|').split('|')
   if not all(re.fullmatch(r'[\s:-]+',c) for c in row):table.append([inline(c.strip())for c in row])
   i+=1
  screenshots=any('<img ' in c for row in table for c in row)
  body.append('<div class="table-wrap"><table'+(' class="screenshots"'if screenshots else '')+'><thead><tr>'+''.join('<th scope="col">'+c+'</th>' for c in table[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+c+'</td>'for c in row)+'</tr>'for row in table[1:])+'</tbody></table></div>');continue
 if line.startswith('- ') or re.match(r'\d+\. ',line):
  ordered=not line.startswith('- ');tag='ol'if ordered else 'ul';items=[]
  while i<len(lines)and(lines[i].startswith('- ')if not ordered else bool(re.match(r'\d+\. ',lines[i]))):
   items.append('<li>'+inline(re.sub(r'^(?:- |\d+\. )','',lines[i]))+'</li>');i+=1
  body.append('<'+tag+'>'+''.join(items)+'</'+tag+'>');continue
 para=[]
 while i<len(lines)and lines[i].strip()and not lines[i].startswith(('#','|','- ')) and not re.match(r'\d+\. ',lines[i]):para.append(inline(lines[i]));i+=1
 body.append('<p>'+'<br>'.join(para)+'</p>')
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f6f8;color:#263644;font:16px/1.75 system-ui,-apple-system,sans-serif}a{color:#135d82;text-underline-offset:3px}a:focus-visible{outline:3px solid #2389c9;outline-offset:4px}header{background:#113349;color:#fff;padding:64px max(24px,calc((100vw - 1160px)/2));border-bottom:5px solid #46aeee}header .kicker{color:#9cd8fb;letter-spacing:.12em;font-size:13px;text-transform:uppercase}h1{font:clamp(32px,4vw,56px)/1.15 Georgia,serif;margin:18px 0;max-width:900px}header p{max-width:820px;color:#dbe5eb}header a{color:#fff}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:32px 0 0}.stat{padding:20px;border:1px solid #567080;background:#1b4058}.stat strong{display:block;font-size:32px;font-weight:500;color:#fff}.stat span{font-size:14px;color:#dbe5eb}main{max-width:1216px;margin:0 auto;padding:24px 28px 80px}nav{display:flex;flex-wrap:wrap;gap:12px 28px;padding:24px 0;border-bottom:1px solid #ccd6de}article{background:#fff;padding:32px 40px;margin-top:24px;border:1px solid #dce2e7}h2{font:30px/1.25 Georgia,serif;margin:48px 0 20px;color:#113349;border-top:1px solid #e1e7eb;padding-top:32px;scroll-margin-top:20px}h3{font-size:19px;line-height:1.4;margin:30px 0 12px;color:#113349}p,li{max-width:100ch}li{padding-left:4px;margin-bottom:10px}.table-wrap{overflow-x:auto;margin:24px 0}table{border-collapse:collapse;width:100%;font-size:14px;text-align:left}th{background:#edf3f6;color:#113349}th,td{padding:14px;border:1px solid #dce3e8;vertical-align:top}td{min-width:140px}tbody tr:nth-child(even){background:#fafbfc}code{overflow-wrap:anywhere;background:#edf3f6;padding:2px 4px;font-size:.9em}.screenshots{table-layout:fixed}.screenshots td{width:50%;padding:12px}.screenshots td:first-child{background:#f8fafb}.capture{text-decoration:none;display:block}.capture img{display:block;width:100%;max-height:650px;object-fit:contain;object-position:top;background:#e5ebef}.capture span{display:block;font-size:13px;margin-top:8px;text-align:center}.note{background:#fff7df;border-left:4px solid #b28a27;padding:18px 22px;margin-top:24px;font-size:15px}footer{font-size:14px;color:#5e6d77;padding-top:24px}@media(max-width:700px){header{padding:40px 20px}.stats{grid-template-columns:1fr}.stat{padding:14px}.stat strong{font-size:27px}main{padding:12px 12px 40px}article{padding:20px 16px}h2{font-size:25px}.screenshots{min-width:580px}table{min-width:650px}nav{gap:12px;font-size:14px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{header{background:#fff;color:#113349;padding:0;border:0}header p,header .kicker{color:#263644}.stats,nav,.note{display:none}main,article{padding:0;border:0}.table-wrap{overflow:visible}h2,h3{break-after:avoid}tr,img{break-inside:avoid}body{background:#fff}.screenshots img{max-height:450px}}'''
page='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Comparativo — Ipiranga Business Center</title><style>'''+css+'''</style></head><body><header><span class="kicker">Ipiranga Business Center · Avaliação de redesign · 10/11/2026</span><h1>Site antigo e nova versão.<br>O que melhorou e o que falta ajustar.</h1><p>Comparação da versão publicada no GitHub Pages com o site Wix e a auditoria original. Evidências de HTML, capturas reais e limitações de medição apresentadas separadamente.</p><div class="stats"><div class="stat"><strong>16 + 16 rotas</strong><span>HTTP 200 nas duas versões</span></div><div class="stat"><strong>93,7% menos HTML</strong><span>Home: 514.674 → 32.605 bytes; não é ganho de velocidade medido</span></div><div class="stat"><strong>10 capturas reais</strong><span>Home, Training, sala privativa e Contato via serviço remoto</span></div></div></header><main><nav aria-label="Seções do relatório"><a href="#parecer">Parecer</a><a href="#compara-o-por-dimens-o">Comparação</a><a href="#regress-es-e-pend-ncias-priorizadas">Pendências</a><a href="#capturas-lado-a-lado">Capturas</a><a href="comparativo-antigo-novo.md">Versão Markdown</a></nav><div class="note"><strong>Alcance:</strong> houve conferência visual das capturas, mas Playwright não iniciou e PageSpeed retornou erro de cota. Não há notas de desempenho, validação interativa ou aprovação dos Core Web Vitals.</div><article>'''+''.join(body)+'''</article><footer>Relatório local de avaliação. Não houve alteração ou publicação de correções nos sites.</footer></main></body></html>'''
(root/'comparativo-antigo-novo.html').write_text(page)
print('HTML do comparativo gerado:',len(page.encode()),'bytes')
