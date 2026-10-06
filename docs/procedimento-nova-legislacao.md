# Procedimento: incluir uma nova legislação no second brain

Vale para um **domínio novo** (assunto novo) e para uma **fonte nova
dentro de um domínio existente** (ex.: Resolução CGSN 140 no domínio
simples-nacional). Rode `python scripts/verificar.py` no fim de cada etapa:
o resultado precisa ser 0 erros.

## Etapa 1: Fonte

1. Baixe o **texto compilado/consolidado** oficial (Planalto para leis;
   Sijut2 da Receita, "visão compilado", para atos da RFB/CGSN). Nunca use
   a publicação original do DOU de um ato que já foi alterado. Atos
   **alteradores** (ex.: Res. CGSN 190/2026, que altera a Res. 140) podem
   ser guardados na versão do DOU, porque são eles próprios a alteração.
2. Salve em `fontes/<dominio>/<ato>-<ano>-texto-compilado.pdf`.
3. Registre a fonte em `fontes/<dominio>/FONTE.md`, uma linha por arquivo:

   | Arquivo | Ato | Origem (URL) | Capturado em | Última alteração vista no texto | Observação |
   |---|---|---|---|---|---|

   A "última alteração vista" é a lei/ato alterador mais recente que
   aparece nas marcas do texto (ex.: `grep -o "Complementar nº [0-9]*, de 20[0-9]*" texto.txt | sort -u`).

## Etapa 2: Extração

```bash
mkdir -p fontes/<dominio>/texto
pdftotext -enc UTF-8 fontes/<dominio>/<arquivo>.pdf fontes/<dominio>/texto/<ato>.txt
python scripts/esqueleto.py fontes/<dominio>/texto/<ato>.txt \
  --ruido "<regex do título repetido no cabeçalho, ex.: ^Lcp 123$>" \
  --saida fontes/<dominio>/texto/<ato>-esqueleto.md
```

- Se o `.txt` sair vazio ou só com lixo, o PDF não tem camada de texto:
  use OCR, ou capture o HTML oficial (Planalto) e salve como `.txt`.
- **Confira:** o "Último artigo" do esqueleto é o último artigo da lei, e
  nenhum número de artigo some da sequência.

### Armadilhas conhecidas do texto compilado do Planalto

- **Redação superada aparece junto da nova.** No site ela vem riscada; na
  extração o risco some. A **última** versão de um dispositivo, a que tem a
  marca, é a mais nova. O esqueleto mostra quantas versões cada dispositivo
  tem.
- **"Produção de efeitos" não traz data.** É só um link. A data sai do
  artigo da lei alteradora que fez a mudança, combinado com a cláusula de
  vigência dessa lei (etapa 3).

### Armadilhas conhecidas das páginas do DOU (in.gov.br)

- A impressão da página pode **repetir trechos do corpo do ato** (visto na
  Res. CGSN 190/2026, cujos arts. 1º a 6º aparecem duas vezes). Use só a
  primeira ocorrência e registre isso no `FONTE.md`.

## Etapa 3: Mapa de vigência

Crie `notas/<dominio>/_mapa-vigencia.md`, com uma linha por dispositivo
marcado no esqueleto que tenha data de efeitos **diferente da publicação**
ou ainda não alcançada:

| Dispositivo | Alterado por | Artigo alterador | Efeitos a partir de | Fundamento da data | Situação em <texto-base> |
|---|---|---|---|---|---|

- "Artigo alterador": o artigo da lei alteradora que contém a nova redação
  (ex.: LC 214, art. 516).
- "Fundamento da data": o dispositivo de vigência (ex.: LC 214, art. 544, I),
  citado literalmente, a partir do texto da lei alteradora.
- "Situação": `vigente` ou `⏳ futura — redação anterior ainda vale`.
- Se uma nota existente (de outro domínio) disser algo diferente do texto
  literal, o texto literal prevalece, e a divergência é registrada em
  LEARNINGS.md.

## Etapa 4: Plano de notas (exige aprovação)

Crie `notas/<dominio>/_plano-notas.md` com frontmatter
`status: aguardando-aprovacao` e uma tabela por grupo temático:

| Arquivo | Artigos | Profundidade | Vigência |
|---|---|---|---|

- Prefixo do domínio em todo arquivo novo; nome único no projeto.
- Todo artigo do esqueleto aparece em alguma linha.
- Referências a notas de **outro** domínio vão como `[[nome]]` (nunca `nome.md`).
- **Pare e peça aprovação ao usuário.** Aprovado, mude para
  `status: aprovado`.

## Etapa 5: Redação

- Frontmatter: `título`, `dominio`, `fontes`, `vigencia`, `texto-base`.
- Conteúdo didático (lógica e analogias), artigos citados, fórmulas por
  completo, tabelas numéricas transcritas literalmente e conferidas duas
  vezes contra o PDF.
- Redação futura em `## ⏳ A partir de ...`; revogação programada em
  `## ❌ Revogado a partir de ...`.
- Ao terminar todas as notas: `status: concluido` no plano. O verificar
  passa a exigir que todas existam.

## Etapa 6: Ligações

- `notas/<dominio>/INDEX.md` com as notas por tema.
- Bloco do domínio em `notas/INDEX.md`.
- `[[...]]` cruzados com as notas de outros domínios que tratam do mesmo
  assunto, nos dois sentidos.

## Etapa 7: Protocolo e testes

- Linha do domínio na tabela "Domínios" do CLAUDE.md e bloco no MEMORY.md.
- `docs/perguntas-teste/<dominio>.md` com 10 a 15 perguntas (cálculo,
  vigência, cruzamento, lacuna, fora de escopo), rodadas com `claude -p`.
- Rodar também a bateria dos domínios já existentes (regressão).

## Atualização de uma fonte já registrada

Texto compilado mudou: refaça as etapas 1 a 3, compare o mapa de vigência
novo com o anterior (`git diff`), revise só as notas afetadas e atualize o
`texto-base` delas.
