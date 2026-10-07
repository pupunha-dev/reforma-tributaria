# Fase B: Res. CGSN 140 no Simples Nacional e novo domínio documentos-fiscais — design

- **Data:** 2026-10-07
- **Status:** aprovado em conversa em 2026-10-07 (o usuário delegou os detalhes: "faça o melhor que achar")
- **Base:** `docs/superpowers/specs/2026-10-06-expansao-multi-legislacao-design.md` (estrutura multi-domínio, procedimento, padrões de vigência), que continua valendo.
- **Duas partes independentes, cada uma com seu plano:** Parte 1 (Res. CGSN 140) e Parte 2 (documentos-fiscais), nessa ordem.

## 1. Objetivo e critérios de sucesso

1. As notas `sn-*` passam a ter, além da lei, a **regulamentação operacional** da Res. CGSN 140 (vigente e futura), com a lei prevalecendo em caso de conflito.
2. As 5 Notas Técnicas do Projeto NF-e entram como um **domínio próprio**, para responder "como preencher e validar a NF-e/NFC-e/DANFE na reforma", e a versão de cada NT fica rastreável.
3. Nenhuma regra futura é apresentada como vigente: na Res. 140, as datas vêm das próprias marcas do portal da Receita; nas NTs, do cronograma de implantação.
4. Os planos de notas das duas partes são aprovados antes da redação (etapa 4 do procedimento).

## 2. Parte 1: Res. CGSN 140/2018 no domínio simples-nacional

### 2.1 Fonte

- Arquivo baixado pelo usuário do portal Normas da Receita, na **visão multivigente**, em 07/10/2026. É renomeado para `fontes/simples-nacional/resolucao-cgsn-140-2018-multivigente.pdf`. O PDF do DOU original já foi apagado pelo usuário e sai do `FONTE.md`.
- A visão multivigente já incorpora as Res. CGSN 190 e 191: mostra redações antigas e vigentes com a data de início (`date_range DD/MM/AAAA`) e marca o que muda com `[Vide modificação prevista para DD/MM/AAAA, nos termos do(a) Resolução CGSN nº N ...]` e `[Vide dispositivo a ser incluído em DD/MM/AAAA ...]`. **O texto futuro não aparece**: ele é lido nas Res. CGSN 190 e 191 (`fontes/simples-nacional/texto/resolucao-cgsn-19x-2026.txt`).
- **Anexos da Res. 140 (I a XII) não vêm na impressão:** são PDFs separados no portal (`file_present Anexo VI.pdf` etc.). Os Anexos I a V de 2027–2028 constam da Res. 190 (DOU). Os demais, principalmente **VI (CNAEs impeditivos), VII (CNAEs ambíguos) e XI (ocupações do MEI)**, ficam como **lacuna** até o usuário baixá-los. As notas dizem isso expressamente.

### 2.2 Extração e vigência

- `pdftotext -enc UTF-8` → `fontes/simples-nacional/texto/resolucao-cgsn-140-2018.txt`.
- Novo script **`scripts/vigencia_receita.py`** (stdlib, TDD): lê o texto da visão multivigente e gera o mapa de vigência da Res. 140 (artigo, dispositivo, tipo de marca, ato alterador, data, situação em `--data-base`). Ele remove o ruído da impressão (data/hora, título "Resol. CGSN nº 140-2018", URL, "N/132", `import_export`, `file_present`) e associa cada marca ao dispositivo anterior. As datas vêm das marcas e do `date_range`.
- Saída: `notas/simples-nacional/_mapa-vigencia-res140.md` (cabeçalho manual + tabela gerada, no mesmo padrão do mapa da LC 123).

### 2.3 Integração nas notas

- **Notas `sn-*` existentes:** cada uma ganha a seção `## Regulamentação (Res. CGSN 140)`, com os artigos correspondentes, e, quando houver, um bloco `## ⏳ A partir de 01/01/2027 — Res. CGSN 190/2026 (art. N)`. O frontmatter `fontes` passa a citar a Res. 140.
- **Notas novas `sn-*`** só para matéria **sem correspondente na LC 123**. Candidatas, a confirmar no plano: PGDAS-D e DEFIS (declarações), parcelamento, ocupações e obrigações do MEI no detalhe da resolução, NFS-e e documentos fiscais do optante (Res. 191), regras de transição do Título IV.
- **Hierarquia (R-hierarquia):** a lei vem primeiro; a resolução detalha. Divergência → `> ⚠️ Conflito LC × Resolução: ...`, e vale a lei.
- **Plano de notas** (`_plano-notas.md` do domínio, nova seção "Fase B") com `status` próprio, aprovado antes da redação.

### 2.4 Testes da Parte 1

- `vigencia_receita.py` com testes de: ruído removido; marca associada ao dispositivo certo; `date_range` → data; "Vide modificação prevista" futura × vigente; "Vide dispositivo a ser incluído".
- `conferir_numeros.py` em toda nota alterada, com o texto da Res. 140 e das Res. 190/191 entre as fontes.
- Perguntas-teste novas em `docs/perguntas-teste/simples-nacional.md` (S15 em diante), cobrindo um detalhe da resolução, uma mudança de 2027 da Res. 190 e uma lacuna de Anexo.

## 3. Parte 2: novo domínio documentos-fiscais (prefixo `df-`)

### 3.1 Escopo e hierarquia

- **Escopo ampliado (CLAUDE.md):** além de atos normativos federais, entra a **documentação técnica nacional dos documentos fiscais eletrônicos**, ou seja, as Notas Técnicas do Projeto NF-e/NFC-e (Receita Federal + Secretarias de Fazenda/ENCAT) e, futuramente, da NFS-e nacional.
- **Hierarquia:** lei > resolução/ato infralegal > nota técnica. A NT diz **como preencher e validar** o documento; ela não cria nem altera tributo. Divergência com a lei → a nota sinaliza e vale a lei.
- Dentro do domínio, a regra de partida continua a mesma: só o que está escrito nas NTs.

### 3.2 Fontes

- Os 5 PDFs saem de `fontes/simples-nacional/` para `fontes/documentos-fiscais/`, com nomes normalizados:
  - `nt-2025-002-rtc-v1.52.pdf` (Reforma Tributária do Consumo — Adequações NF-e/NFC-e)
  - `nt-2026-002-v1.11.pdf` (vendas presenciais e não presenciais, emissão offline, autorização com alerta, DANFE Simplificado Tipo 2)
  - `nt-2026-007-v1.10.pdf` (emissão por contribuinte exclusivo do IBS/CBS)
  - `nt-2026-008-v1.00.pdf` (valor líquido do produto)
  - `nt-2026-010-v1.00.pdf` (DANFE da reforma)
- `fontes/documentos-fiscais/FONTE.md` com NT, versão, mês de publicação, data de captura e observação. Texto extraído em `texto/` (`pdftotext -enc UTF-8`; tabelas de leiaute com `-layout` quando a versão sem `-layout` embaralhar colunas).

### 3.3 Padrões do domínio

- **Frontmatter:** os mesmos campos obrigatórios. `fontes` cita NT **e versão** (ex.: `NT 2025.002-RTC v1.52, seção 6`). `texto-base` = data de captura.
- **Vigência por cronograma:** NT não tem "produção de efeitos", tem implantação em **homologação** e em **produção**. Regra ainda não em produção na data-base → bloco `## ⏳ Em produção a partir de DD/MM/AAAA — NT N vX (cronograma)`. As datas vêm literalmente da tabela de cronograma.
- **Literalidade técnica:** nomes de tags, códigos de regra de validação/rejeição, códigos cClassTrib/CST e fórmulas são copiados literalmente. Novo script **`scripts/conferir_tags.py`** (TDD): extrai da nota os identificadores técnicos (tags em `código`, códigos de regra como `UB12-10`, códigos numéricos de rejeição) e confere se existem no texto da NT. Mesmo papel do `conferir_numeros.py`.
- **Atualização de versão:** quando sair nova versão de uma NT, refaz-se a extração, compara-se o histórico de alterações da NT e revisam-se só as notas afetadas (acréscimo ao procedimento).

### 3.4 Notas (esboço, fechado no plano)

`df-visao-geral-reforma-nfe` (o que mudou e cronograma consolidado), `df-grupo-ibs-cbs-is` (leiaute dos grupos de tributação), `df-cst-cclasstrib` (códigos de classificação tributária), `df-calculo-e-validacoes` (fórmulas e regras de validação), `df-finalidade-debito-credito` (notas de débito/crédito e eventos), `df-contribuinte-exclusivo-ibs-cbs` (NT 2026.007), `df-valor-liquido-produto` (NT 2026.008), `df-danfe-reforma` (NT 2026.010), `df-emissao-offline-alerta` (NT 2026.002). São de 8 a 12 notas. Ligações com [[ibs-cbs-cadastro-documento-fiscal]], [[ibs-cbs-split-payment]] e [[sn-obrigacoes-acessorias]].

- **Simples e MEI na NF-e:** a NT 2025.002 diz que as orientações para CRT 1, 2 e 4 "serão publicadas em NT futura". Isso fica registrado como **lacuna explícita** na nota de visão geral e em `sn-obrigacoes-acessorias`.

### 3.5 Testes da Parte 2

- `conferir_tags.py` e `conferir_numeros.py` sem faltantes em todas as notas `df-*`; `verificar.py` com 0 erros.
- `docs/perguntas-teste/documentos-fiscais.md` com 8 a 10 perguntas: preenchimento de um campo, uma regra de validação, uma data de produção futura, contribuinte sem inscrição estadual, a lacuna do Simples/MEI e uma pergunta fora de escopo (regra estadual de ICMS).

## 4. Mudanças transversais

- **CLAUDE.md:** linha do domínio `documentos-fiscais` na tabela; o escopo passa a incluir a documentação técnica; a regra R-hierarquia passa a dizer lei > resolução > nota técnica.
- **MEMORY.md:** domínio novo e status da fase B.
- **Procedimento** (`docs/procedimento-nova-legislacao.md`): seção para fontes da Receita na visão multivigente e para Notas Técnicas (versão, cronograma, `conferir_tags.py`).
- **Índice mestre:** bloco do domínio novo.

## 5. Riscos

| Risco | Mitigação |
|---|---|
| Marca da Receita associada ao dispositivo errado (a marca vem depois do texto, às vezes com quebra de página no meio) | testes do `vigencia_receita.py` com essas formas; conferência por amostragem contra o portal |
| Redação antiga e nova lado a lado, como no Planalto | a última redação com `date_range` passado é a vigente; marca "Vide modificação prevista" com data futura → bloco ⏳ com o texto da Res. 190/191 |
| NT mudar de versão depois da redação | versão no frontmatter e no FONTE.md; procedimento de atualização |
| Tabelas de leiaute embaralhadas na extração | `pdftotext -layout` para as tabelas; `conferir_tags.py` |
| Anexos da Res. 140 ausentes | lacuna explícita; pedido ao usuário dos PDFs dos Anexos VI, VII e XI |
