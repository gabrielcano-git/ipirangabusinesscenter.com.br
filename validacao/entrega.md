# Nova versão — implementação e validação

Data: 10/11/2026. Prévia: http://127.0.0.1:4173/. Resultado local; sem publicação.

## Base e decisões

Aplicada a skill `website-modernization`, com identidade de `DESIGN.md`: branco, cinzas e azul #113349, destaque azul, tipografia escalável em rem, imagens do acervo original e composição responsiva. Componentes BEM em SCSS, utilitários Tailwind e Font Awesome SVG. Conteúdo estático disponível sem JavaScript; JS somente para menu móvel e preparação de contato.

`RTK.md` citado nas instruções não está disponível neste projeto. Não foi utilizado arquivo de outro projeto como substituto.

## Rotas e estados mapeados

Mapeamento por sitemap, HTML e inventários. Playwright foi tentado antes e depois, mas não conseguiu iniciar navegador.

| Rota | Conteúdo / comportamento |
|---|---|
| `/` | Abertura, quatro soluções, Training, imagens, localização e contato |
| `/quem-somos` | Institucional, Viviana, missão, compromisso, crenças e clientes |
| `/servicos` | Catálogo de espaços e soluções |
| `/sala-comercial-privativa` | Tipos de sala, público e itens incluídos |
| `/salas-de-reuniao` | Infraestrutura, flexibilidade, clientes e depoimento |
| `/locacao-de-sala-para-treinamento` | Auditório, equipamentos, clientes, depoimento e ressalva sobre capacidade |
| `/escritorio-virtual` | Endereço, correspondências, atendimento e locação por hora |
| `/ipiranga-training` | Coaching, consultoria, cursos e RH; título corrigido |
| `/coaching` | Públicos e modalidades |
| `/consultoria` | Temas de consultoria |
| `/cursos-palestras` | Programas para RH, líderes e profissionais em geral |
| `/servicos-de-rh` | Serviços de carreira e preparação profissional |
| `/contato` | Endereço, horário, canais de contato e formulário |
| `/fotos` | Imagem disponível no HTML coletado |
| `/rooms-rates` | Rota legada preservada, conteúdo disponível e acesso aos serviços |
| `/p-gina-em-tela-cheia` | Rota legada preservada com acesso aos serviços |

Todas compartilham cabeçalho, navegação, rodapé e links de contato. Formulário tem validação nativa e link para revisar e enviar via WhatsApp. Menu móvel usa `aria-expanded`, botão e fechamento por Escape com retorno de foco. Há skip link, foco visível e redução de movimento. Esses comportamentos estão implementados, mas não foram exercitados em navegador.

## Melhorias aplicadas

- Um H1 por página, rodapé em texto comum e seções com headings sem saltos H2–H6.
- Marca padronizada, título correto de Training, descrições por página, canonical, Open Graph, imagem social, Twitter Card e JSON-LD WebSite.
- Nome acessível do logo, nomes textuais de links, alternativas de imagens e ícones decorativos ocultos de tecnologias assistivas.
- Nome, e-mail, telefone, serviço, assunto e mensagem com labels persistentes; autocomplete apropriado.
- Revisão editorial dos erros apontados. Formulário de sala privativa não usa o placeholder “Coworking”.
- Fotos hospedadas localmente, lazy loading abaixo da abertura e dimensões explícitas; CSS compilado e JavaScript pequeno, sem runtime Wix.
- Fonte de verdade preservada nos HTMLs e dados coletados; conteúdo comercial e depoimentos são afirmações do site original, sem verificação externa.

## Evidências executadas

- `npm run build`: PASS, geração estática de 16 rotas e compilação SCSS/Tailwind.
- `npm run validate`: PASS em todas as rotas: destinos internos existentes, H1 único, idioma, descrições, labels, atributos de imagens, conteúdo crítico institucional e de sala privativa, sitemap e ausência de mensagens falsas de sucesso.
- `node --check scripts/build.cjs` e `node --check public/assets/site.js`: PASS.
- Requisições HTTP às 16 rotas sem barra final: 200; evidência `http.json`.
- Playwright Chromium: bloqueado antes de navegar, erro MachPort/Permission denied; `browser-bloqueio.txt` e `browser-execucao.txt`.
- Alternativas WebKit e Firefox também falharam ao iniciar. Navegador integrado indisponível; acesso ao Chrome nativo não aprovado pela ferramenta.

## Limitações e pendências

- **Sem screenshots ou validação visual nesta entrega.** Layout, overflow, teclado, contraste computado, zoom e interações precisam ser executados em um ambiente com navegador permitido. O script `scripts/browser-check.cjs` está preparado para as 16 rotas em quatro larguras.
- **PageSpeed da nova versão: não medido**, em todas as categorias. A nova versão é local e não há URL pública para consulta. A baseline já registrava HTTP 429 do PageSpeed. Não há comparação quantitativa de desempenho, LCP, INP, TBT ou CLS.
- Acessibilidade implementada por estrutura; não equivale a conformidade auditada.
- Capacidade do auditório aguardando confirmação: valores 36 e 40 preservados com contexto explícito, sem escolher um deles como definitivo.
- Backend Wix não foi exportado. O fluxo de contato foi adaptado para preparação de mensagem em WhatsApp, com envio realizado pelo visitante. Formulário original por e-mail não foi migrado.
- Conteúdo capturado é HTML público, não exportação CMS. Galerias ou vídeos que dependam exclusivamente do runtime Wix não puderam ser confirmados na renderização; todas as imagens `<img>` coletadas foram baixadas, mas isso não comprova completude de mídia dinâmica. Rotas legadas com pouco conteúdo foram mantidas.
- Tipografia usa fallbacks locais Arial/Georgia; as fontes proprietárias não foram redistribuídas.
- Sem especificação de WebMCP; sem alegação de integração. HTML semântico facilita navegação por agentes.
- Arquivos publicáveis ficam exclusivamente em `dist/`; não foi alterada a produção.
