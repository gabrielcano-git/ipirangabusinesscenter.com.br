"""Gera PDFs registrados em reports.json. Uso: python scripts/generate-report-pdfs.py.
Dependências de autoria: reportlab, pypdf, pillow. O CI publica os PDFs já gerados.
"""
import html, json, re, os
from pathlib import Path
from urllib.parse import quote
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from PIL import Image as PILImage
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
font_dir=Path(os.environ.get('REPORT_FONT_DIR','/System/Library/Fonts/Supplemental'))
for name,file in [('Body','Arial.ttf'),('Body-Bold','Arial Bold.ttf'),('Body-Italic','Arial Italic.ttf')]:
 if not(font_dir/file).exists():raise RuntimeError('Fontes de autoria ausentes. Configure REPORT_FONT_DIR com Arial.ttf, Arial Bold.ttf e Arial Italic.ttf.')
 pdfmetrics.registerFont(TTFont(name,str(font_dir/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Italic',boldItalic='Body-Bold')
INK=colors.HexColor('#113349');MUTED=colors.HexColor('#5b6770');BORDER=colors.HexColor('#d4dfe6');SURFACE=colors.HexColor('#edf3f6')
W,H=A4;M=43;WIDTH=W-2*M
ST={
 'body':ParagraphStyle('body',fontName='Body',fontSize=9.3,leading=14,spaceAfter=8,textColor=colors.HexColor('#263644'),splitLongWords=True),
 'meta':ParagraphStyle('meta',fontName='Body',fontSize=8,leading=12,spaceAfter=6,textColor=MUTED),
 'title':ParagraphStyle('title',fontName='Body-Bold',fontSize=25,leading=30,spaceAfter=16,textColor=INK),
 'h2':ParagraphStyle('h2',fontName='Body-Bold',fontSize=15,leading=20,spaceBefore=16,spaceAfter=9,textColor=INK,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='Body-Bold',fontSize=11,leading=15,spaceBefore=12,spaceAfter=7,textColor=INK,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=7.8,leading=11,spaceAfter=0,textColor=colors.HexColor('#263644'),splitLongWords=True),
 'th':ParagraphStyle('th',fontName='Body-Bold',fontSize=8,leading=11,spaceAfter=0,textColor=INK),
 'bullet':ParagraphStyle('bullet',fontName='Body',fontSize=9.3,leading=14,leftIndent=12,firstLineIndent=-10,spaceAfter=7,textColor=colors.HexColor('#263644')),
}
def normalized(s):
 return s.translate(str.maketrans({'\u2010':'-','\u2011':'-','\u2012':'-','\u2013':'-','\u2014':'-','\u2212':'-','\u00a0':' '}))
def source_url(link,source):
 if link.startswith(('https://','http://','mailto:')):return link
 if link.startswith('#'):return 'https://github.com/gabrielcano-git/ipirangabusinesscenter.com.br/blob/main/'+quote(str(source.relative_to(ROOT)))+link
 resolved=(source.parent/link).resolve()
 if not resolved.is_relative_to(ROOT):raise ValueError('Referência fora do projeto: '+link)
 if not resolved.exists():raise ValueError('Referência local ausente: '+str(resolved))
 return 'https://github.com/gabrielcano-git/ipirangabusinesscenter.com.br/blob/main/'+quote(str(resolved.relative_to(ROOT)))
def inline(s,source):
 s=normalized(s);s=html.escape(s)
 s=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',lambda m:'<link color="#135d82" href="'+html.escape(source_url(html.unescape(m[2]),source),quote=True)+'">'+m[1]+'</link>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'`([^`]+)`',r'<font name="Body">\1</font>',s)
 return s
class Pages(Canvas):
 def __init__(self,*a,**kw):Canvas.__init__(self,*a,**kw);self.states=[]
 def showPage(self):self.states.append(dict(self.__dict__));self._startPage()
 def save(self):
  count=len(self.states)
  for state in self.states:
   self.__dict__.update(state);self.setStrokeColor(BORDER);self.line(M,37,W-M,37);self.setFillColor(MUTED);self.setFont('Body',7.5)
   self.drawString(M,24,'Ipiranga Business Center | Relatórios de avaliação | 10/11/2026');self.drawRightString(W-M,24,f'{self._pageNumber} / {count}');Canvas.showPage(self)
  Canvas.save(self)
def header(canvas,doc):
 canvas.saveState();canvas.setStrokeColor(BORDER);canvas.line(M,H-30,W-M,H-30);canvas.setFont('Body',7.5);canvas.setFillColor(MUTED);canvas.drawString(M,H-21,'AVALIAÇÃO DO SITE - CONTEÚDO PRESERVADO DO RELATÓRIO DE ORIGEM');canvas.restoreState()
def table(rows,source):
 n=len(rows[0]);widths=([WIDTH*.16,WIDTH*.28,WIDTH*.28,WIDTH*.28]if n==4 else [WIDTH/n]*n)
 cells=[[Paragraph(inline(cell.strip(),source),ST['th'if idx==0 else 'cell'])for cell in row]for idx,row in enumerate(rows)]
 t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),SURFACE),('GRID',(0,0),(-1,-1),.45,BORDER),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#fafbfc')])]))
 return [t,Spacer(1,9)]
def screenshot_table(rows,source):
 images=[]
 for cell in rows[-1]:
  match=re.search(r'!\[([^\]]*)\]\(([^)]+)\)',cell)
  if not match:raise ValueError('Captura sem referência')
  alt,rel=match.groups();file=(source.parent/rel).resolve()
  with PILImage.open(file)as im:iw,ih=im.size
  scale=min((WIDTH/2-20)/iw,510/ih)
  image=Image(str(file),width=iw*scale,height=ih*scale);image.hAlign='CENTER'
  images.append([image,Spacer(1,6),Paragraph(inline('['+alt+']('+rel+')',source),ST['meta'])])
 t=Table([[Paragraph(inline(x.strip(),source),ST['th'])for x in rows[0]],images],colWidths=[WIDTH/2]*2,splitByRow=0)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),SURFACE),('GRID',(0,0),(-1,-1),.45,BORDER),('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(0,0),(-1,0),'CENTER'),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
 return [t,Paragraph('Capturas reduzidas para comparação. Amplie o PDF ou abra os links das imagens para ler detalhes. User-agent e condições do serviço remoto não foram informados.',ST['meta']),Spacer(1,9)]
def generate(report):
 source=ROOT/report['source'];lines=source.read_text().splitlines();story=[Paragraph('IPIRANGA BUSINESS CENTER',ST['meta']),Paragraph(inline(report['title'],source),ST['title']),Paragraph('Data do relatório: '+report['date']+' | Exportação em PDF: 10/11/2026',ST['meta']),Paragraph(inline('Versão integral do documento de origem. As limitações e os resultados permanecem os do relatório, sem novas medições. [Consultar fonte]('+source.name+')',source),ST['meta']),Spacer(1,12)];i=0;screenshot_mode=False
 while i<len(lines):
  line=lines[i]
  if not line.strip():i+=1;continue
  if line.startswith('# '):i+=1;continue
  if line.startswith('##'):
   level=len(line)-len(line.lstrip('#'));heading=line[level:].strip()
   if level==2:
    if screenshot_mode and heading!='Capturas lado a lado':story.append(PageBreak())
    screenshot_mode=heading=='Capturas lado a lado'
   if level==3 and screenshot_mode:story.append(PageBreak())
   story.append(Paragraph(inline(heading,source),ST['h2'if level==2 else 'h3']));i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines)and lines[i].startswith('|'):
    row=lines[i].strip().strip('|').split('|')
    if not all(re.fullmatch(r'[\s:-]+',c)for c in row):rows.append(row)
    i+=1
   story.extend(screenshot_table(rows,source)if any('!['in c for row in rows for c in row)else table(rows,source));continue
  if line.startswith('- ')or re.match(r'\d+\. ',line):
   story.append(Paragraph(inline(re.sub(r'^- ','- ',line),source),ST['bullet']));i+=1;continue
  parts=[]
  while i<len(lines)and lines[i].strip()and not lines[i].startswith(('#','|','- '))and not re.match(r'\d+\. ',lines[i]):parts.append(inline(lines[i].strip(),source));i+=1
  story.append(Paragraph('<br/>'.join(parts),ST['body']))
 file=OUT/report['pdf'];doc=SimpleDocTemplate(str(file),pagesize=A4,rightMargin=M,leftMargin=M,topMargin=46,bottomMargin=51,title=report['title'],author='Ipiranga Business Center - Relatórios do projeto',pageCompression=1)
 doc.build(story,onFirstPage=header,onLaterPages=header,canvasmaker=Pages)
 reader=PdfReader(file);text='\n'.join(p.extract_text()for p in reader.pages)
 assert len(reader.pages)>0 and len(text)>1000
 assert '\ufffd'not in text
 print(file.relative_to(ROOT),len(reader.pages),'páginas',file.stat().st_size,'bytes')
 return {'pdf':report['pdf'],'pages':len(reader.pages),'bytes':file.stat().st_size,'source':report['source']}
records=[generate(r)for r in json.loads((ROOT/'src/data/reports.json').read_text())]
(ROOT/'output/pdf/manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
