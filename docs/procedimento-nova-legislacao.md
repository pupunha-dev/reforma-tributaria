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

- **Leis do Planalto: capture também o HTML oficial**, convertido para UTF-8:

  ```bash
  curl -s -L -A "Mozilla/5.0" "<url>.htm" | iconv -f CP1252 -t UTF-8 | tr -d '\r' | sed 's/charset=windows-1252/charset=utf-8/I' > fontes/<dominio>/texto/<ato>-planalto.htm
  ```

  É a fonte de verdade da vigência (etapa 3) e serve de texto pesquisável
  quando o PDF não tem camada de texto.
- Se o `.txt` sair vazio ou só com lixo, o PDF não tem camada de texto:
  use o HTML oficial (acima) ou OCR.
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

**Leis do Planalto: gere o mapa com o script.** No HTML, o texto superado
vem em `<strike>`, e cada "Produção de efeitos"/"Vigência" é um link para o
inciso da cláusula de vigência da lei alteradora. Monte o arquivo de
âncoras (`texto/<ato>-ancoras-vigencia.tsv`: âncora → data → fundamento
[→ `revogacao`]) a partir do **texto literal** das cláusulas de vigência e
escreva o cabeçalho (`texto/<ato>-mapa-cabecalho.md`, com as cláusulas
literais). Depois:

```bash
python scripts/vigencia_planalto.py fontes/<dominio>/texto/<ato>-planalto.htm   --ancoras fontes/<dominio>/texto/<ato>-ancoras-vigencia.tsv --data-base AAAA-MM-DD   --cabecalho fontes/<dominio>/texto/<ato>-mapa-cabecalho.md   --saida notas/<dominio>/_mapa-vigencia.md
```

A seção "Âncoras de vigência não mapeadas" mostra links que ficaram sem
data. Confira se nenhum é de alteração com efeito ainda não alcançado.
Confira também se o compilado já incorporou as alterações com efeito
futuro (veja o exemplo da LC 227, art. 169, no LEARNINGS.md).

Para atos fora do Planalto, monte o mapa à mão, com uma linha por
dispositivo marcado no esqueleto que tenha data de efeitos **diferente da
publicação** ou ainda não alcançada:

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

### Regulamentos que citam a lei em cada artigo (Decreto 12.955/2026, Res. CGIBS 6/2026)

Os regulamentos da reforma trazem, em cada artigo, a citação do dispositivo da
LC 214 entre parênteses. Não escreva o mapa à mão: guarde o texto (HTML do
Planalto para decreto federal; `pdftotext` para PDF do CGIBS), ajuste o
cabeçalho com as cláusulas de vigência literais e rode:

```bash
python scripts/mapa_regulamento.py \
  --cbs fontes/reforma/texto/decreto-12955-2026-planalto.htm \
  --ibs fontes/reforma/texto/res-cgibs-6-2026.txt \
  --plano notas/reforma/_plano-notas.md \
  --cabecalho fontes/reforma/texto/regulamentos-mapa-cabecalho.md \
  --mapa notas/reforma/_mapa-regulamentos.md \
  --textos fontes/reforma/texto --notas notas/reforma
```

O script imprime quantos artigos achou e quantos têm citação. Confira que a
contagem bate com o último artigo do ato e que não há citação de LC perdida.
As datas de vigência por artigo (⏳) ficam em `EFEITOS`, no próprio script: ao
mudar a cláusula de vigência do regulamento, atualize ali e o teste. Uma nova
versão de regulamento: troque a fonte, rode de novo (os blocos das notas são
substituídos, não duplicados) e revise as notas próprias dos regulamentos.

### Fontes da Receita na visão multivigente (portal Normas)

Para atos infralegais da Receita/CGSN, baixe a impressão da **visão
multivigente** (não a do DOU): ela mostra a redação antiga e a vigente, com
marcas `[Redação dada pelo(a) ...] date_range DD/MM/AAAA`, `[Incluído...]`,
`[Revogado...]`, `[Vide modificação prevista para DD/MM/AAAA ...]` e `[Vide
dispositivo a ser incluído em DD/MM/AAAA ...]`. Cuidados:

- **O texto futuro não aparece**: "Vide modificação prevista" só avisa. A nova
  redação é lida no ato alterador (ex.: Res. CGSN 190/2026), que também entra em
  `fontes/<dominio>/texto/`.
- A redação antiga vem **sem marca**, antes da nova; a impressão às vezes **corta
  uma marca** (um `[` sem fechamento). O script trata os dois casos.
- **Anexos** são PDFs separados no portal e não vêm na impressão: registre a
  lacuna no `FONTE.md` e no cabeçalho do mapa. Quando o PDF do anexo chegar:
  - extraia a tabela com
    `python scripts/tabela_pdf.py <anexo.pdf> --titulo "<título>" --saida fontes/<dominio>/texto/<ato>-anexo-<n>.md`
    (requer pymupdf) e confira contra o `pdftotext` (mesma contagem de códigos);
  - descubra a versão: a **última marca depois do link do anexo** na visão
    multivigente (a marca vem depois do `file_present`, não antes do título) e a
    **data de criação do PDF** (metadado) devem ser coerentes; registre as duas
    no `FONTE.md`.
- **Soluções de Consulta (Cosit):** entram no domínio do ato que interpretam,
  numa nota de soluções de consulta, como "interpretação da Receita" para os
  fatos do consulente (não como regra nova). Nome do arquivo:
  `solucao-consulta-cosit-<n>-<ano>.pdf`.

Gere o mapa com o script (cabeçalho manual com as cláusulas de vigência
literais dos atos alteradores):

```bash
python scripts/vigencia_receita.py fontes/<dominio>/texto/<ato>.txt \
  --data-base AAAA-MM-DD \
  --cabecalho fontes/<dominio>/texto/<ato>-mapa-cabecalho.md \
  --saida notas/<dominio>/_mapa-vigencia-<ato>.md
```

Na redação, a resolução entra em cada nota numa seção "Regulamentação
(<ato>)", depois da lei, e a mudança futura num bloco `## ⏳ A partir de
DD/MM/AAAA — <ato alterador> (art. N)`. Divergência com a lei vira aviso
`> ⚠️ Conflito LC × Resolução`, e vale a lei.

### Notas Técnicas (documentos fiscais eletrônicos)

Para NTs do Projeto NF-e/NFC-e (domínio `documentos-fiscais`):

- **Nome do arquivo com NT e versão** (ex.: `nt-2025-002-rtc-v1.52.pdf`) e,
  no `FONTE.md`, versão, mês de publicação e data de captura.
- **Texto riscado:** as NTs marcam a redação superada com um traço sobre o
  texto, que o `pdftotext` não distingue. Gere o texto vigente:

  ```bash
  pip install pymupdf
  python scripts/extrair_nt.py fontes/documentos-fiscais/<nt>.pdf --saida-dir fontes/documentos-fiscais/texto
  ```

  Isso cria `<nt>-vigente.txt` (fonte das notas) e `<nt>-riscado.md`
  (auditoria). Guarde também `pdftotext` corrido e `-layout` para leitura.
- **Vigência por cronograma:** não há "produção de efeitos", e sim
  implantação em homologação e em produção. O que ainda não está em produção
  vai para `## ⏳ Em produção a partir de DD/MM/AAAA — NT N vX (cronograma)`,
  com a data copiada da tabela de cronograma do texto vigente.
- **Literalidade:** tags em crase, códigos de regra (ex.: UB12-10) e
  rejeições escritas como "rejeição 1115" são conferidos com
  `python scripts/conferir_tags.py <nota> --fontes fontes/documentos-fiscais/texto/*-vigente.txt`.
  O script confere que cada identificador **existe** na NT, não que a regra e a
  rejeição citadas juntas estejam **pareadas**: confira o pareamento na linha
  da regra no `-vigente.txt` (código, descrição e rejeição vêm na mesma linha).
- **Informe Técnico (IT):** é documentação técnica do mesmo nível da NT (divulga
  tabelas e orientações de preenchimento). Trate como NT: nome com versão
  (`it-2025-002-v1.60.pdf`), extração com `extrair_nt.py` (também tem texto
  riscado) e versões antigas guardadas só para histórico.
- **Tabelas publicadas em portal (CST/cClassTrib, cCredPres):** quando a NT remete
  a uma tabela fora do PDF, use o endereço dado pelo IT e prefira a fonte que
  entregue dados estruturados (JSON/HTML) a copiar da tela:

  ```bash
  python scripts/tabelas_svrs.py cclasstrib --data AAAA-MM-DD
  python scripts/tabelas_svrs.py ccredpres --data AAAA-MM-DD
  python scripts/tabelas_svrs.py nota notas/documentos-fiscais/df-tabela-cclasstrib.md
  python scripts/tabelas_svrs.py conferir <nota>
  ```

  Os dois primeiros gravam JSON e Markdown em `fontes/documentos-fiscais/texto/`;
  `nota` regera só as tabelas marcadas com `<!-- gerado:... -->`; `conferir`
  confere que os códigos de 6 dígitos da nota (em crase ou na 1ª coluna de
  tabela) existem na captura. Registre sempre a data da captura: a tabela muda.
- **Hierarquia:** lei > resolução > NT; o frontmatter `fontes` cita "NT N vX"
  (o `verificar.py` exige).
- **Nova versão de uma NT:** baixe, refaça a extração, leia o histórico de
  alterações da NT e revise **só** as notas das seções alteradas, trocando a
  versão no `fontes`.

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
