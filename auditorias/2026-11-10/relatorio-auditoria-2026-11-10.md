# Auditoria do site: Ipiranga Business Center

**URL solicitada pelo contexto:** https://ipirangabusinesscenter.com.br/  
**URL final:** https://www.ipirangabusinesscenter.com.br/  
**Data:** 2026-11-10, coleta iniciada aproximadamente às 12h de Brasília (15h UTC).  
**Estado:** análise de conteúdo e HTML concluída na amostra; auditoria visual, interativa e de performance pendente por bloqueios das ferramentas. Esta é uma baseline parcial para comparação futura.  
**Ferramentas:** curl, Python HTMLParser, tentativa de Playwright/Chromium e navegador integrado, API PageSpeed Insights. Nenhum formulário foi enviado e nenhuma alteração foi feita no site.

## Escopo e limitações

Foram coletadas nove páginas públicas. Todas responderam HTTP 200; o domínio sem `www` redirecionou por HTTP 301 para a versão com `www`.

| Página | URL/caminho no domínio final | Jornada |
|---|---|---|
| Home | `/` | Descobrir serviços e localização |
| Quem somos | `/quem-somos` | Avaliar a empresa |
| Serviços | `/servicos` | Escolher uma solução |
| Sala privativa | `/sala-comercial-privativa` | Avaliar estrutura e solicitar informações |
| Reunião | `/salas-de-reuniao` | Avaliar espaço para reuniões |
| Auditório | `/locacao-de-sala-para-treinamento` | Planejar eventos |
| Escritório virtual | `/escritorio-virtual` | Avaliar endereço e apoio administrativo |
| Training | `/ipiranga-training` | Descobrir desenvolvimento profissional |
| Contato | `/contato` | Agendar visita ou solicitar informações |

Também foram coletados `robots.txt`, `sitemap.xml` e `pages-sitemap.xml`. As páginas Coaching, Consultoria, Cursos & Palestras e Serviços de RH aparecem no menu, mas não integram a amostra inspecionada.

**Viewports planejados:** desktop 1440 × 900 e mobile 390 × 844. **Não executados:** o Chromium falhou antes da navegação com `MachPortRendezvousServer: Permission denied (1100)`; a alternativa de navegador integrado respondeu `The browser access host is unavailable`. [Registro](evidencias/browser-limitations.txt).

Consequentemente, não foram validados: aparência, capturas de tela, menus em funcionamento, âncoras, navegação por teclado, foco visível, nomes acessíveis após execução de JavaScript, overflow, controles móveis, zoom/reflow, redução de movimento, contraste computado, console ou falhas de recursos de terceiros. Não há pares de cores nem razões de contraste medidos; os limites de referência para uma retomada são 4,5:1 para texto normal e 3:1 para texto grande, além das verificações aplicáveis a componentes. Nenhuma conclusão de conformidade de acessibilidade é emitida.

O HTML coletado contém mensagens de sucesso dos formulários; sua presença no código **não** comprova que estejam visíveis nem que o envio funcione. As observações de elementos e textos abaixo referem-se ao HTML entregue, não a uma renderização visual.

## Resumo executivo

O site oferece uma base comercial útil: serviços separados, localização próxima ao metrô, endereço, WhatsApp, e-mail e descrição dos itens incluídos nas salas privativas. Há conteúdo institucional, relação de clientes e depoimento atribuído, embora suas alegações não tenham sido verificadas externamente.

As prioridades confirmadas na amostra são corrigir o título estranho ao negócio em Training, harmonizar a capacidade do auditório e melhorar a identificação dos campos e das imagens. A estrutura de headings usa H2 e H6 para finalidades visuais e não apresenta H1 nas nove páginas coletadas. Quatro páginas não entregam meta description.

Não há evidência suficiente para classificar o site como lento, responsivo, inacessível como um todo ou com conversão baixa. Também não foi demonstrado bloqueio de uma tarefa importante; por isso, nenhum achado recebe severidade **High** nesta etapa.

## Tecnologias identificadas

| Categoria | Tecnologia | Evidência e URL | Confiança e limitações |
|---|---|---|---|
| Plataforma/CMS | Wix Website Builder | Home: `meta name="generator" content="Wix.com Website Builder"`; cabeçalho `x-wix-request-id`; sitemap `generatedBy="WIX"` | Confirmada por sinais independentes. Versão do produto não determinada; `Published-Version: 319` é revisão do site. |
| Runtime de frontend | Wix Thunderbolt | Home: `wix-viewer-model`, classes `wixui-*` e bundles em `https://static.parastorage.com/services/wix-thunderbolt/dist/` | Confirmado no HTML. Não comprova implementação do backend. |
| Biblioteca de interface | React e ReactDOM 18.3.1 | Scripts da home: `https://static.parastorage.com/unpkg/react@18.3.1/umd/react.production.min.js` e `https://static.parastorage.com/unpkg/react-dom@18.3.1/umd/react-dom.production.min.js` | Inclusão confirmada, versão explícita nas URLs. Execução não validada. React é biblioteca, não CMS. |
| Entrega/CDN | Cloudflare e infraestrutura de assets Wix | Resposta final: `server: cloudflare`, `cf-ray`, `cf-cache-status: HIT`; imagens em `static.wixstatic.com` | Confirmado na entrega observada; não identifica toda a arquitetura de hospedagem. |
| Integrações por links | WhatsApp e Google Maps | Home: `api.whatsapp.com/send`, `wa.me` e link `google.com.br/maps/place/…` | Links confirmados; destinos não acionados. Não demonstra APIs próprias nem embeds funcionais. |

Fontes locais: [cabeçalhos](evidencias/home-headers.txt), [HTML da home](evidencias/home.html), [inventário estático](evidencias/home-static.json) e [sitemap](evidencias/sitemap.xml).

## Performance

URL enviada ao PageSpeed: `https://ipirangabusinesscenter.com.br/`, em 2026-11-10, com estratégias `mobile` e `desktop` e categorias performance, accessibility, best-practices e seo.

| Dispositivo | Performance / Acessibilidade / Boas práticas / SEO | LCP | TBT | CLS | Tipo de dado |
|---|---|---|---|---|---|
| Mobile | Indisponíveis | N/D | N/D | N/D | Nenhum resultado de laboratório retornado |
| Desktop | Indisponíveis | N/D | N/D | N/D | Nenhum resultado de laboratório retornado |

As duas requisições retornaram **HTTP 429 / RESOURCE_EXHAUSTED**, com cota excedida no serviço do Google. Não é uma resposta do site auditado. [Resposta mobile](evidencias/pagespeed-mobile.json) e [desktop](evidencias/pagespeed-desktop.json).

**CrUX:** disponibilidade de dados de campo não determinada, pois o serviço não retornou os resultados. Não há oportunidades do Lighthouse disponíveis para relatar. Mesmo quando disponível, uma execução de laboratório não representa todos os visitantes.

O HTML contém `srcset`, dimensões em várias imagens, uma imagem com `loading="lazy"` e URLs de transformação com `enc_avif`. São sinais favoráveis de preparação da entrega, não medição de velocidade. A página de sala privativa transferiu 687.823 bytes de HTML nesta coleta curl; isso não mede peso total, transferência comprimida no navegador ou Core Web Vitals.

## Achados prioritários

As severidades seguem a skill: **High** = tarefa importante bloqueada ou seriamente prejudicada; **Medium** = fricção ou exclusão relevante; **Low** = melhoria localizada ou de acabamento. Achados estáticos de acessibilidade precisam de confirmação após a execução de JavaScript.

### Medium — Título de Training pertence a outro contexto

- **Observação:** `/ipiranga-training` retorna `<title>Seaside B&B</title>`, apesar de o corpo tratar de desenvolvimento profissional. Também não há meta description nessa página.
- **Evidência:** [HTML](evidencias/ipiranga-training.html) e entrada `ipiranga-training` do [inventário](evidencias/pages-static.json).
- **Impacto e severidade:** identificação enganosa na aba e sinal inadequado para mecanismos de busca; fricção relevante para reconhecer o negócio. Não foi inspecionado o resultado real no Google.
- **Recomendação:** definir título como “Ipiranga Training | Desenvolvimento profissional no Ipiranga” e uma descrição específica e fiel aos serviços.

### Medium — Capacidade do auditório é contraditória

- **Observação:** a home anuncia “até 40 pessoas”; `/locacao-de-sala-para-treinamento` informa “capacidade máxima 36 pessoas”.
- **Evidência:** [home](evidencias/home.html) versus [auditório](evidencias/locacao-de-sala-para-treinamento.html).
- **Impacto e severidade:** número decisivo para selecionar o espaço de um evento; a divergência impede planejar com segurança usando apenas o conteúdo.
- **Recomendação:** confirmar a capacidade com o responsável e uniformizar as páginas. Se varia por montagem, explicar as configurações e seus limites. Não assumir qual número é correto.

### Medium — Campos dependem de placeholders no HTML entregue

- **Observação:** home e contato têm inputs Nome, Email e Assunto sem `label` associado, `aria-label` ou `aria-labelledby`; a textarea Mensagem tem label vazio. `autocomplete="off"` aparece nos inputs. O mesmo padrão se repete nos formulários de serviços amostrados.
- **Evidência:** campo `inputs` em [pages-static.json](evidencias/pages-static.json), com IDs e atributos; [contato](evidencias/contato.html).
- **Impacto e severidade:** instruções dependentes de placeholder podem desaparecer durante a digitação e a identificação de campos pode ficar menos clara. A árvore de acessibilidade e eventuais correções via JavaScript não foram verificadas.
- **Recomendação:** manter rótulos persistentes associados aos campos e usar autocomplete adequado a nome, e-mail e telefone; validar leitura, teclado e erros sem enviar o formulário na auditoria.

### Medium — Imagens e links têm identificação textual insuficiente

- **Observação:** a home entrega 12 imagens, todas com atributo `alt`, mas sete vazios; entre os textos existentes estão `DSC00042`, `whatsapp_edited.png` e `Coffee`. Há links sem texto ou rótulo próprio envolvendo imagens com alt vazio, incluindo a imagem de marca e cartões de serviço.
- **Evidência:** listas `images` e `links` nos [inventários](evidencias/pages-static.json); `img_comp-imv8tgnk` e `img_comp-indjcm3a` no [HTML](evidencias/home.html).
- **Impacto e severidade:** nomes de arquivo não explicam propósito; links de imagem podem ficar sem identificação útil para navegação assistiva. O nome acessível final não foi computado no navegador. Alt vazio pode ser correto em imagem decorativa e não é erro por si só.
- **Recomendação:** nomear links de marca e WhatsApp pelo destino/ação, descrever imagens informativas e preservar alt vazio em decoração. Rever legendas técnicas como `DSC00042` na galeria.

### Medium — Hierarquia de headings não representa bem o conteúdo

- **Observação:** nenhuma das nove páginas contém H1 no HTML coletado; são frequentes saltos de H2 para H6. Rodapé, endereço e copyright estão em H6. Em Quem somos, uma frase está dividida em quatro H2: “nossa vocação”, “é te ajudar”, “na sua”, “vocação”.
- **Evidência:** `headings` em [pages-static.json](evidencias/pages-static.json).
- **Impacto e severidade:** reduz a utilidade da navegação por títulos e a representação da organização das páginas. Isso não demonstra penalização de ranking.
- **Recomendação:** usar título principal descritivo em H1, H2 para seções e H3 quando houver subseções. Converter textos corridos/rodapé em parágrafos e controlar sua aparência por estilos.

### Low — Metadados incompletos e identidade inconsistente

- **Observação:** Quem somos, Serviços, Training e Contato não entregam meta description. Títulos alternam “Ipiranga Business” e “ipiranga-business”. A home tem `twitter:card=summary_large_image`, mas não entrega `og:image` nem `twitter:image` nas metas coletadas.
- **Evidência:** `metadata` e `title` do [inventário por página](evidencias/pages-static.json); `meta` da [home](evidencias/home-static.json).
- **Impacto e severidade:** oportunidade de melhorar descrições e apresentação compartilhada; previews reais e snippets não foram testados, e plataformas podem escolher imagens por outros meios.
- **Recomendação:** padronizar a marca, escrever descrições distintas e definir imagem social apropriada, verificando as prévias.

### Low — Revisão editorial e contexto dos formulários

- **Observação:** o formulário de sala comercial privativa ainda tem campo com placeholder “Coworking”. O rodapé informa “© 2016” e “há mais de 6 anos”. A home tem “tem à oferecer”; Escritório virtual traz “excelencia”, “correspondencias”, “telefonico” e “possivel”.
- **Evidência:** [sala privativa](evidencias/sala-comercial-privativa.html), [home](evidencias/home.html) e [escritório virtual](evidencias/escritorio-virtual.html).
- **Impacto e severidade:** acabamento editorial e contexto comercial menos claros. “Mais de 6 anos” pode continuar verdadeiro e o copyright antigo não comprova abandono.
- **Recomendação:** revisar os textos; substituir o campo ambíguo por “Serviço de interesse”, com contexto adequado; confirmar ano de início antes de atualizar informações institucionais.

## Pontos fortes

- Nove páginas amostradas acessíveis por HTTP 200; HTTPS e redirecionamento permanente para o domínio com `www` observados.
- Todas as páginas amostradas possuem canonical correspondente. `robots.txt` permite rastreamento geral e anuncia sitemap; índice e sitemap de páginas foram recuperados. Isso não comprova indexação.
- Home com `lang="pt"`, viewport declarado, meta description, Open Graph e JSON-LD de tipo `WebSite`. O cabeçalho HTTP informa `content-language: en`, divergindo do documento; convém alinhar a configuração, preservando o idioma correto no HTML.
- Presença de landmarks `header`, `nav`, `main` e `footer` na home; botões da galeria com “Anterior” e “Próximo” e botões de submenu com rótulos em português. Funcionamento por teclado pendente.
- Sala privativa descreve opções para 1, 2 e até 6 pessoas, além de mobília, água, luz, Wi-Fi, ar-condicionado, IPTU, condomínio, copa, limpeza e manutenção.
- Contato fornece WhatsApp, e-mail, endereço e horário de funcionamento. Home inclui link ao Maps e proximidade do metrô.
- Quem somos apresenta responsável e trajetória; Auditório e Reunião incluem clientes e depoimento atribuído. São elementos de credibilidade presentes, sem validação externa das alegações.

## Evidências visuais e registros

**Não há screenshots nesta entrega:** a captura não foi possível. Não foram produzidas imagens ilustrativas para simular a inspeção. A pasta contém HTML e respostas técnicas reais, preservados para consulta.

- [Inventário das nove páginas](evidencias/pages-static.json): headings, títulos, metadados, canonical, JSON-LD, parágrafos, campos, imagens e links.
- [Inventário ampliado da home](evidencias/home-static.json): scripts e landmarks, além dos itens anteriores.
- [Status, URLs finais e tamanhos das coletas adicionais](evidencias/fetch-results.json).
- [Robots](evidencias/robots.txt), [índice de sitemap](evidencias/sitemap.xml) e [sitemap de páginas](evidencias/pages-sitemap.xml).
- [Bloqueios dos navegadores](evidencias/browser-limitations.txt) e respostas PageSpeed [mobile](evidencias/pagespeed-mobile.json) / [desktop](evidencias/pagespeed-desktop.json).
- HTML e cabeçalhos de cada página disponíveis nesta mesma pasta, nomeados pelo caminho. Os arquivos representam o conteúdo público obtido na data, não uma exportação do CMS.

## Ordem recomendada e retomada da baseline

1. Confirmar a capacidade do auditório e corrigir o título de Training.
2. Ajustar rótulos dos formulários, identificação dos links/imagens e semântica dos títulos.
3. Revisar metadados, textos e consistência dos serviços.
4. Completar Playwright em 1440 × 900 e 390 × 844, salvando screenshots de viewport e página inteira. Testar menus, âncoras, foco, teclado, reflow a 320 CSS px, zoom e redução de movimento, sem envios.
5. Medir contraste computado com indicação de elemento, cores, razão e limiar; observar console e rede. Executar PageSpeed mobile/desktop quando houver cota, registrando condições, scores, LCP, TBT, CLS, oportunidades e disponibilidade CrUX separadamente.

Uma comparação futura deve repetir URLs e condições, mantendo indisponível o que não foi medido aqui. Esta entrega não permite calcular evolução de desempenho nem afirmar melhoria visual.
