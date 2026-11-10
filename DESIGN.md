# Ipiranga Business Center — Design

## Escopo e evidência

Referência: https://www.ipirangabusinesscenter.com.br/.
Documento gerado em 10/11/2026 a partir dos HTMLs coletados na mesma data em `auditorias/2026-11-10/evidencias/`, especialmente `home.html` e `home-static.json`. O site usa Wix. A consulta web desta execução não conseguiu abrir o domínio; não houve validação visual nesta execução. Tokens declarados pelo tema não comprovam seu uso em todos os componentes.

Este documento registra a identidade disponível no código e propõe regras para sua aplicação consistente. Medidas recomendadas abaixo não são medições do site atual.

## Identidade e conteúdo

O Ipiranga Business Center oferece soluções corporativas: coworking, salas de reunião e treinamento, sala comercial privativa, escritório virtual e desenvolvimento profissional. A comunicação deve transmitir clareza, organização e confiança, com foco nos ambientes e serviços reais.

Preservar logotipo, fotografias e conteúdo verificado. Evitar imagens genéricas que possam sugerir instalações inexistentes. Não inventar preços, capacidade das salas, depoimentos ou benefícios.

## Cores extraídas

Valores encontrados nas variáveis CSS do Wix:

| Token original | Valor | Aplicação recomendada |
| --- | --- | --- |
| `color_11` | `#FFFFFF` | Fundo principal |
| `color_12` | `#F4F4F4` | Superfícies alternadas |
| `color_13` | `#A0A09F` | Divisórias e detalhes |
| `color_14` | `#605E5E` | Texto secundário |
| `color_15` | `#2F2E2E` | Texto principal |
| `color_18` | `#46AEEE` | Acentos e elementos decorativos |
| `color_19` | `#2389C9` | Acento azul intermediário |
| `color_20` | `#113349` | Títulos, botões e superfícies escuras |
| `color_23` | `#41BAAE` | Acento complementar disponível no tema |
| `color_33` | `#DEC328` | Destaque pontual disponível no tema |

A presença de verdes e amarelos no tema não confirma sua relevância visual para a marca. Priorizar os neutros e a família azul até inspeção visual. Validar contraste por combinação antes de usar qualquer cor em texto; azul claro não deve ser adotado automaticamente como fundo de botão com texto branco.

## Tipografia extraída

| Token | Declaração do tema |
| --- | --- |
| `font_0` | Raleway, negrito, 20 px, entrelinha 1,4 |
| `font_1` | Raleway, regular, 16 px, entrelinha 1,4 |
| `font_2` | Museo Slab 100, 30 px, entrelinha 1,4 |
| `font_3` | Raleway, regular, 60 px, entrelinha 1,4 |
| `font_4` | Museo Slab 100, 40 px, entrelinha 1,4 |
| `font_5` | Raleway, regular, 25 px, entrelinha 1,4 |
| `font_6` | Raleway, regular, 21 px, entrelinha 1,4 |
| `font_7` | Raleway, regular, 18 px, entrelinha 1,4 |
| `font_8` | Times New Roman, itálico, 16 px, entrelinha 1,4 |
| `font_9` | Raleway, regular, 16 px, entrelinha 1,4 |
| `font_10` | Raleway, regular, 12 px, entrelinha 1,4 |

Fallbacks: `sans-serif` para Raleway e `serif` para Museo Slab. Confirmar disponibilidade e licença antes de hospedar fontes. A função semântica de cada estilo depende do componente; os números dos tokens não representam níveis de heading.

Recomendação responsiva: título principal entre 32 e 60 px; títulos de seção entre 26 e 40 px; corpo entre 16 e 18 px. Manter um H1 por página e hierarquia sem saltos motivados apenas pela aparência.

## Layout e ritmo — recomendações

- Container central com largura máxima de 1200 px e margens laterais de 20 px no celular e 32 px no desktop.
- Escala de espaçamento: 4, 8, 12, 16, 24, 32, 48, 64 e 96 px.
- Seções com 48–80 px de espaço vertical; reduzir para 32–48 px em telas pequenas.
- Grades de serviços com até três colunas, reduzidas conforme o conteúdo exigir. Usar uma coluna quando cards perderem legibilidade.
- Fotografias com proporção consistente e recorte que preserve os espaços apresentados. Evitar distorção e texto essencial dentro de imagens.
- Preferir superfícies simples, bordas discretas e hierarquia tipográfica. Definir raios e sombras após conferir a referência visual.

## Componentes — contrato recomendado

**Cabeçalho:** logotipo com link para a página inicial, navegação clara para os serviços e contato. No celular, menu operável por teclado, com estado expandido anunciado e retorno de foco ao fechar.

**Abertura:** título que explique a oferta, texto curto e foto real. CTA deve indicar o destino, por exemplo, “Conheça os espaços” ou “Entre em contato”, conforme o fluxo existente.

**Serviços:** nome, descrição objetiva e link para a página correspondente. Evitar cards com vários destinos sobrepostos. Evidenciar diferenças reais entre escritório virtual, sala privativa, reunião e treinamento.

**Botões e links:** contraste validado, foco visível e estados hover, ativo e desabilitado quando aplicáveis. Alvo de toque recomendado de 44 × 44 px. Usar links para navegação e botões para ações.

**Formulários:** rótulos persistentes, campos estritamente necessários, mensagens de erro junto ao campo e confirmação clara de envio. Não apresentar sucesso antes da resposta real do serviço.

**Rodapé:** navegação complementar e dados de contato confirmados no conteúdo original. Preservar os destinos reais dos links de telefone e canais externos.

## Páginas documentadas no acervo

Além da home, há HTMLs de `quem-somos`, `servicos`, `escritorio-virtual`, `sala-comercial-privativa`, `salas-de-reuniao`, `locacao-de-sala-para-treinamento`, `ipiranga-training` e `contato`.

Uma implementação deve conferir as URLs exatas no sitemap e no conteúdo coletado antes de alterar rotas. O inventário de arquivos não comprova que todas as rotas continuam publicadas.

## Movimento, acessibilidade e adaptação

Preferir transições discretas; respeitar `prefers-reduced-motion`. Evitar animações que atrasem o acesso ao conteúdo. Manter navegação por teclado, texto alternativo contextual, contraste de 4,5:1 para texto comum e 3:1 para texto grande. Validar zoom, refluxo e ausência de rolagem horizontal a 320 px.

## Verificação antes de implementar ou publicar

Conferir visualmente home, página de serviço e contato em desktop e celular; confirmar cores efetivamente aplicadas, fontes carregadas, medidas, recortes e estados interativos. Testar navegação, formulário e destinos dos CTAs. Este documento não representa redesign implementado nem resultado publicado.
