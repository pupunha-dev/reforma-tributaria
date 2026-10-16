# Fontes — domínio documentos-fiscais

Notas Técnicas (NT) do Projeto NF-e (Receita Federal + Secretarias de Fazenda/ENCAT),
fornecidas pelo usuário em 2026-10-06 (antes em `fontes/simples-nacional/`) e
capturadas neste domínio em 2026-10-07. Origem pública: Portal Nacional da
NF-e (www.nfe.fazenda.gov.br), aba "Documentos".

| Arquivo | NT | Assunto | Versão | Publicação | Capturado em | Observação |
|---|---|---|---|---|---|---|
| nt-2025-002-rtc-v1.52.pdf | NT 2025.002-RTC | Reforma Tributária do Consumo — adequações da NF-e/NFC-e (grupos IBS/CBS/IS, regras de validação, eventos) | 1.52 | setembro/2026 | 2026-10-07 | 94 páginas. Anexos I (NCM do IS) e II (cClassTribIS): "tabela a ser publicada". Anexos III (**cClassTrib**) e IV (**cCredPres**): fora do PDF; publicadas pelo IT 2025.002 e capturadas do Portal dos DF-e (seções abaixo). A seção 9 (DANFE) diz "em estudo", superada pela NT 2026.010. |
| nt-2026-002-v1.11.pdf | NT 2026.002 | Vendas presenciais e não presenciais, autorização com alerta, DANFE Simplificado Tipo 2 | 1.11 | setembro/2026 | 2026-10-07 | Cronograma por versão (1.00 a 1.11). |
| nt-2026-007-v1.10.pdf | NT 2026.007 | Emissão por contribuinte exclusivo do IBS/CBS | 1.10 | setembro/2026 | 2026-10-07 | Produção em 03/11/2026. |
| nt-2026-008-v1.00.pdf | NT 2026.008 | Valor líquido do produto; ICMS previsto no pagamento antecipado | 1.00 | setembro/2026 | 2026-10-07 | Campos: produção em 03/11/2026; parte das regras de validação: produção em 01/03/2027. |
| nt-2026-010-v1.00.pdf | NT 2026.010 | DANFE da reforma tributária (leiaute de impressão) | 1.00 | outubro/2026 | 2026-10-07 | Produção em 01/12/2026. |

## Informe Técnico 2025.002 (tabelas de classificação do IBS e da CBS)

Fornecidos pelo usuário em 2026-10-08 (pasta `fontes/novos-analise/`). O IT
divulga e mantém as tabelas cClassTrib, CST e cCredPres e as alíquotas padrão, e
dá os endereços oficiais das tabelas online (seção 06).

| Arquivo | Documento | Versão | Publicação | Capturado em | Observação |
|---|---|---|---|---|---|
| it-2025-002-v1.60.pdf | IT 2025.002 — Tabelas de Classificação do IBS e da CBS | 1.60 | 22/06/2026 | 2026-10-08 | **Versão usada nas notas.** 12 páginas. Seções: objetivo, cClassTrib, CST, cCredPres, alíquotas padrão 2026–2029, tabelas online, histórico de alterações (v1.10 a v1.60). Cita o Decreto 12.955/2026 (Regulamento da CBS) e a Res. CGIBS 6/2026 (Regulamento do IBS), que **não estão nas fontes**. 1 trecho riscado ("ind_gMonoDif", excluído). |
| it-2025-002-v1.31.pdf | idem | 1.31 | 15/12/2025 | 2026-10-08 | **Superada** pela v1.60; guardada para histórico. 8 linhas riscadas. |

Texto em `texto/`: `<it>-vigente.txt` e `<it>-riscado.md` (`scripts/extrair_nt.py`),
mais `.txt` e `-layout.txt` (`pdftotext`). Use só o `-vigente.txt`.

## Guia do Emissor Público Nacional Web da NFS-e (Sistema Nacional NFS-e)

Fornecido pelo usuário em 2026-10-16 (caixa de entrada `fontes/assets/`). É o
**manual operacional** do emissor web do Sistema Nacional Nota Fiscal de Serviço
eletrônica: diz como preencher e operar o emissor. Fica **abaixo da NT** na
hierarquia: não cria regra nem tributo. A URL de origem não consta no PDF (cita o
Portal da Nota Fiscal de Serviço eletrônica): confirmar e registrar aqui.

| Arquivo | Documento | Versão | Data da versão | Capturado em | Observação |
|---|---|---|---|---|---|
| guia-emissor-publico-nacional-nfse-v1.2.1.pdf | Guia do Emissor Público Nacional Web da NFS-e | 1.2 (o arquivo original se chama "versao_1-2-1") | 27/07/2026 (histórico do próprio guia; PDF criado em 27/07/2026) | 2026-10-16 | 125 páginas, 321 imagens (telas do emissor). Histórico de versões do guia: 1.0; 1.1 (23/09/2025, emissão por decisão administrativa/judicial); 1.2 (27/07/2026, "adequação do guia aos novos campos de IBS/CBS"). **Sem texto riscado** (0 linhas). Não traz a planilha de leiaute DPS e RN DPS nem o Anexo VII (IndOp_IBSCBS), que ele cita; em 2026-10-16 o usuário forneceu o Anexo I (cópia anterior ao RTC) e o Anexo VII v1.03.00 (ver a seção das Notas Técnicas da SE/CGNFS-e abaixo). Original recebido como `guia_emissor_publico_nacional_web_snnfse-ern_versao_1-2-1.pdf`. |

Texto em `texto/`: `guia-emissor-publico-nacional-nfse-v1.2.1-vigente.txt` (fonte das notas, `scripts/extrair_nt.py`),
`guia-emissor-publico-nacional-nfse-v1.2.1-riscado.md` (vazio) e, para apoio de leitura, `guia-emissor-publico-nacional-nfse-v1.2.1.txt` e
`guia-emissor-publico-nacional-nfse-v1.2.1-layout.txt` (`pdftotext`).

## Notas Técnicas da SE/CGNFS-e (NFS-e Nacional), anexos e manual da API

Fornecidos pelo usuário em 2026-10-16 (caixa de entrada `fontes/assets/`), baixados por ele do portal
da NFS-e (padrão de endereço: `https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica` e, para a
NFS-e Via, `https://www.gov.br/nfse/pt-br/nfs-e-via/documentacao-tecnica`; **o endereço exato de cada
arquivo não consta nos PDFs: confirmar e registrar**). São a documentação técnica nacional da NFS-e, no
**nível de NT** (acima do Guia do Emissor, abaixo da lei e dos regulamentos). Numeração própria da
SE/CGNFS-e: não confundir com as NTs do Projeto NF-e. Nota: [[df-nfse-cgnfse-notas-tecnicas]]
(cronologia e substituições).

| Arquivo | Documento | Versão | Data nas fontes | Páginas | Texto riscado | Notas que o usam |
|---|---|---|---|---|---|---|
| nt-cgnfse-003-v1.2.pdf | NT SE/CGNFS-e 003: grupos IBS/CBS (3ª versão do layout) | 1.2 | 04/07/2025 | 16 | extenso (~124 linhas); **substituída pela NT 004** | só histórico |
| nt-cgnfse-004-v2.00.pdf | NT 004: grupos IBS/CBS (4ª versão); produção em 05/01/2026 | 2.00 | 10/12/2025 | 19 | ~81 linhas | `df-nfse-layout-ibscbs`, `df-nfse-via` |
| nt-cgnfse-005-v1.0.pdf | NT 005: evoluções do layout (5ª versão) | 1.0 | 19/11/2025 | 15 | 6 linhas | `df-nfse-layout-ibscbs` |
| nt-cgnfse-006-v1.00.pdf | NT 006: NFS-e Via, layout 1.00 | 1.00 | 22/01/2026 | 13 | nenhum | `df-nfse-via` |
| nt-cgnfse-007-v1.0.pdf | NT 007: PIS/COFINS, `indZFMALC`, novos códigos | 1.0 | 07/02/2026 | 10 | nenhum | `df-nfse-layout-ibscbs`, `df-nfse-via` |
| nt-cgnfse-008-v1.02.pdf | NT 008: DANFSe v2.0 | 1.02 (1.01: 30/06/2026) | 14/07/2026 | 26 | nenhum | `df-nfse-danfse` |
| nt-cgnfse-009-v1.01.pdf | NT 009: ajustes e novos campos do grupo IBSCBS (consolida a v1.0) | 1.01 | 11/09/2026 (o portal rotula o arquivo como 01/10/2026; as fontes não explicam a diferença; PDF criado em 14/09/2026) | 23 | ver `-vigente.txt` | `df-nfse-layout-ibscbs`, `df-nfse-comercio-exterior`, `df-nfse-regras-ibscbs-anexo-vi` |
| nt-cgnfse-010-v1.00.pdf | NT 010: NFS-e Via, layout 1.01 e manifestação | 1.00 | 11/09/2026 | 6 | nenhum | `df-nfse-via` |
| manual-api-emissor-nfse-2025-10.pdf | Manual dos Contribuintes: API do Emissor Público Nacional | **indeterminada**: o arquivo veio rotulado "v1.2", mas o histórico interno lista só a 1.0 (17/03/2025); PDF criado em 06/10/2025 | 17/03/2025 (histórico); PDF 06/10/2025 | 6 | nenhum | `df-nfse-cgnfse-notas-tecnicas` |
| anexo-i-leiaute-rn-dps-nfse-v1.01-20260209.xlsx | Anexo I: leiaute e regras de negócio da DPS/NFS-e (5 abas) | **v1.01-20260209** (layout **em produção**: NT 004 v2.00 + PIS/COFINS da NT 007; sem as evoluções das NTs 005 e 009) | planilha modificada em 12/02/2026 | 5 abas | não se aplica | `df-nfse-comercio-exterior`, `df-nfse-regras-ibscbs-anexo-vi`, `df-nfse-layout-ibscbs`, `df-nfse-lista-servicos-ctribnac`, `df-nfse-codigos-ibge-localidades` |
| anexo-ii-eventos-v1.01-20260122.xlsx | Anexo II: leiautes e regras dos eventos de NFS-e (4 abas) | v1.01-20260122 | planilha modificada em 17/01/2026 | 4 abas | não se aplica | `df-nfse-eventos` |
| anexo-iv-adn-v1.00-20251216.xlsx | Anexo IV: ADN, geração de NSU, distribuição a municípios e contribuintes e recepção de lote (3 abas). **Não** é o "Anexo IV" da NFS-e Via (`LeiautesRN_ADN-SNNFSeVia_V1.00.04`) que a NT 010 cita | v1.00-20251216 | planilha modificada em 10/12/2025 | 3 abas | não se aplica | `df-nfse-adn-distribuicao` |
| anexo-vi-leiautes-rn-rtc-ibscbs-v1.04.01-nt009-v1.01.xlsx | Anexo VI: LeiautesRN_RTC_IBSCBS (layout da NT 009 v1.01; ao entrar em produção passa a ser o `ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe`) | **v1.04.01** (as NTs citam 1.01.03, 1.02.00, 1.03.00 e 1.04.00 de épocas anteriores) | planilha modificada em 01/10/2026 | 7 abas | não se aplica | `df-nfse-layout-ibscbs`, `df-nfse-regras-ibscbs-anexo-vi`, `df-nfse-comercio-exterior` |
| anexo-viii-correlacao-nbs-indop-cclasstrib-v1.01.00.xlsx | Anexo VIII: correlação item da lista × NBS × cIndOp × cClassTrib (abas "tabela geral", "REGRA inc. X" e "Planilha2") | v1.01.00 | planilha modificada em 01/04/2026 | 3 abas | não se aplica | `df-nfse-correlacao-nbs-indop` e as seis `df-nfse-correlacao-itens-*` |
| anexo-vii-indop-ibscbs-v1.03.00.xlsx | Anexo VII: IndOp_IBSCBS (códigos do `cIndOp`) | 1.03.00 (as NTs citam 1.00.00, 1.01.00, 1.02.00 e, a NT 009 v1.01, 1.02.01) | planilha modificada em 15/09/2026 | 1 aba | não se aplica | `df-nfse-indop-ibscbs`, `df-nfse-via` |

A cadeia de substituição entre as NTs está em [[df-nfse-cgnfse-notas-tecnicas]]. **NT 004 (1ª versão, de
19/08/2025)** e as **NTs 001 e 002** são citadas pelas outras, mas **não estão nas fontes**.

Texto em `texto/` como nas demais NTs (`<arquivo>-vigente.txt` é a fonte das notas;
`-riscado.md`, `.txt` e `-layout.txt` são apoio). As planilhas foram exportadas em TSV para consulta
(`anexo-i-rn-recepcao-dps.tsv`, `anexo-i-mun-incid-info-serv.tsv`, `anexo-i-exportacao-emissao-nfs-e.tsv`
e `-comentarios.tsv`, `anexo-i-leiaute-dps-nfs-e.tsv`, `anexo-i-rn-dps-nfs-e.tsv` e `-comentarios.tsv`,
`anexo-vii-indop-cindop-public.tsv`). **Colunas das regras de recepção (Anexo I, aba `RN_RECEPCAO_DPS`):**
K = emissores nacionais (recepção da DPS); L = emissores nacionais sob decisão judicial; M = compartilhamento
com o ADN; N = ADN com decisão judicial; os níveis são 1, 2 e 3.

**Arquivados como superados** (em `historico/`, sem nota): `anexo-i-leiaute-rn-dps-nfse-copia-2025-09-09-superada.xlsx`
(Anexo I anterior ao RTC, sem o grupo `IBSCBS`; substituído pelo Anexo I v1.01-20260209) e `nt-cgnfse-009-v1.0-superada.pdf`
(a NT 009 v1.0 de 04/06/2026, substituída pela v1.01).

**Triagem dos arquivos de 16/10/2026 (noite):** (1) Anexo I v1.01-20260209 é o layout em produção e o Anexo VI v1.04.01 é o
layout da NT 009 v1.01; o que existe só no VI **não tem data de produção nas fontes**; (2) a NT 009 v1.01 cita o Anexo VII
v1.02.01, e as fontes têm a v1.03.00, mais nova; (3) o Anexo VIII é "norteador" segundo a NT 004 v2.00 e não gera regra de
negócio nos anexos de regras; (4) o nome "Anexo IV" designa dois documentos (ADN e NFS-e Via): só o do ADN está nas fontes.
Extrações em `texto/`: `anexo-i-*.tsv`, `anexo-vi-*.tsv`, `anexo-ii-*.tsv`, `anexo-iv-*.tsv` e `anexo-viii-*.tsv`
(`scripts/xlsx_para_tsv.py`; o Anexo VIII é expandido por `scripts/anexo_viii.py`, e as notas por item são geradas por
`scripts/gerar_notas_anexo_viii.py`).

**Lacunas conhecidas (pedir ao usuário quando necessário):** Anexo A (países ISO2), Anexo IV da NFS-e Via (`LeiautesRN_ADN-SNNFSeVia_V1.00.04`), Manual para Emissão da NFS-e
Via v1.02, Resolução CGNFS-e nº 9/2025, NTs 001 e 002, cronograma de implantação das NTs 005, 007 e 009 e do Anexo VI e o ato
que fixa as datas do IBS/CBS na NFS-e. Confirmar no portal se o Anexo VIII v1.01.00 é o mais recente.

## Tabelas de códigos da NFS-e, tabela do IBGE e arquivos de apoio (2026-10-16, fim da tarde)

Fornecidos pelo usuário em 2026-10-16 (caixa de entrada `fontes/assets/`).

| Arquivo | Documento | Versão e data | Uso | Observação |
|---|---|---|---|---|
| lista-servicos-ctribnac-portal-nfse-2026-10-16.pdf | Portal da NFS-e, "Lista de Serviços Anexa à Lei Complementar nº 116, de 31 de julho de 2003" (Código e Descrição dos Serviços); endereço: https://www.gov.br/nfse/pt-br/mei-e-demais-empresas/codigos-de-tributacao-nacional-nbs | página publicada em 20/02/2024 e **atualizada em 20/08/2024**; impressa em 16/10/2026 (33 páginas) | nota [[df-nfse-lista-servicos-ctribnac]] | É a lista **nacional** de 335 códigos de 6 dígitos (cTribNac), não a lista de 4 dígitos da lei. O Anexo B "V1.01-20260122" (citado pelo guia) foi fornecido depois: tem 338 códigos, os 335 desta página com descrição idêntica + 110501, 141403 e 141404. Extração com pymupdf (`texto/lista-servicos-ctribnac.tsv`); o `pdftotext` embaralha o primeiro item de cada página (cabeçalho fixo do site) e o texto cru ficou em `texto/lista-servicos-ctribnac-portal-nfse-2026-10-16.txt` só como apoio. Conferido: todos os 305 códigos legíveis no `pdftotext -layout` constam nos 335 |
| anexo-b-lista-servico-nacional-nbs2-v1.01-20260122.xlsx | Anexo B do leiaute da NFS-e Nacional: "Anexo_B-Nbs2-Lista_Servico_Nacional-SNNFSe-V1.01-20260122" (abas LISTA.SERV.NAC. e LISTA.NBS_v2.0) | v1.01, 22/01/2026 (data do nome do arquivo); fornecido em 16/10/2026 | nota [[df-nfse-lista-servicos-ctribnac]] | 338 códigos cTribNac (41 títulos de item, 201 de subitem) e 1.210 NBS. Códigos guardados como número, sem zero à esquerda. TSV: `texto/anexo-b-lista-serv-nac.tsv` e `texto/anexo-b-lista-nbs-v2-0.tsv` (`scripts/xlsx_para_tsv.py`). Conferido: as 731 NBS do Anexo VIII existem na lista (56 com redação diferente) |
| ibge-dtb/RELATORIO_DTB_BRASIL_MUNICIPIO.xls, _DISTRITO.xls, _SUBDISTRITO.xls | IBGE, BET (Banco de Estruturas Territoriais), Relatório da Divisão Territorial Brasileira | data-base 22/11/2024 | nota [[df-nfse-codigos-ibge-localidades]] e `scripts/consulta_ibge.py` | 5.570 municípios; 10.724 distritos; 645 subdistritos. TSV em `texto/ibge-dtb-municipios.tsv`, `ibge-dtb-distritos.tsv` e `ibge-dtb-subdistritos.tsv`. Origem do download não registrada nos arquivos (site do IBGE) |
| ibge-dtb/Distritos novos - 2023.xlsx, Subdistritos novos - 2023.xlsx | IBGE, divisões criadas em 2023 | 2023 | apoio | 54 distritos e 2 subdistritos; **todos já constam** nos relatórios de 22/11/2024 |
| historico/nt-2025-002-rtc-v1.33-superada.pdf | NT 2025.002-RTC | **v1.33 (12/2025)**, superada pela v1.52 | nenhum (histórico) | A própria v1.52 lista a v1.33 como "correção em regras de validação e alteração da data de início de regra". Não usar |
| referencias-nao-oficiais/reforma_tributaria_contabilin_2026-10-16.csv | compilação de terceiros ("contabilin"): item da LC 116 × NBS × cIndOp × local de incidência × cClassTrib × CNAE (227 linhas) | 16/10/2026 | **nenhum**: não é fonte oficial | Reprovada na conferência contra as fontes oficiais: 3 códigos cIndOp que não existem no Anexo VII v1.03.00 (010100, 070100 e 301001; os códigos vêm sem o zero à esquerda, como 20201, e foram normalizados para 6 dígitos para a conferência); 110 das 114 linhas com cIndOp 100301 dizem "Domicílio principal do adquirente", mas 4 dizem local do imóvel, da prestação ou do evento, em contradição com o anexo; 83 das 227 linhas trazem o nome do cClassTrib diferente do da tabela do Portal dos DF-e (parte é só abreviação); 4 cClassTrib não têm o uso em NFS-e na tabela oficial (000002, 011001, 011002 e 011005); o item 11.05 não consta na lista nacional. **Não substitui o Anexo VIII oficial** (pendência F15) |

## Tabelas online do Portal dos DF-e (SVRS)

Capturadas em **2026-10-08** pelos endereços do IT 2025.002 v1.60 (seção 06), com
`scripts/tabelas_svrs.py`. Acesso público, sem login. A equipe confirmou em
2026-10-08 que a fonte é a recomendada pelo site da Receita.

| Arquivo (em `texto/`) | Origem | Conteúdo |
|---|---|---|
| cclasstrib-svrs.json | https://dfe-portal.svrs.rs.gov.br/DFE/TabelaClassificacaoTributaria (redireciona para `/DFE/ClassificacaoTributaria`; mesmo JSON de `/Cff/ClassificacaoTributaria`) | 18 CST e 173 cClassTrib, completos: indicadores, tpRBSN, texto dos regulamentos da CBS e do IBS (165 códigos), listas NCM/NBS de 35 códigos. Os dados vêm como JSON embutido na página |
| cclasstrib-svrs.md | idem | as mesmas tabelas em Markdown (`tabelas_svrs.py cclasstrib`) |
| ccredpres-svrs.json / .md | https://dfe-portal.svrs.rs.gov.br/DFE/TabelaCreditoPresumido | 13 códigos cCredPres: apropriação (DF-e ou evento), dedução, declaração de pagamento, documentos e vigência por tributo (`tabelas_svrs.py ccredpres`). A página é HTML; as colunas de alíquota e percentual do IT **não** aparecem nela |

A tabela cClassTrib do portal tem itens publicados em 01/10/2026, **depois** do IT
v1.60. A tabela **muda**: repetir a captura quando a NT, o IT ou o regulamento
mudar, comparar com o arquivo anterior e regerar a nota com
`python scripts/tabelas_svrs.py nota notas/documentos-fiscais/df-tabela-cclasstrib.md`.
Códigos de 6 dígitos citados nas notas são conferidos com
`python scripts/tabelas_svrs.py conferir <nota.md>`.

## Texto extraído

**Atenção: as NTs têm texto riscado.** A redação superada aparece com um traço
sobre o texto (em vermelho, com marca amarela), como o `<strike>` do Planalto. O
`pdftotext` **não** distingue isso: nos arquivos `.txt` e `-layout.txt` o texto
riscado aparece misturado ao vigente (ex.: na NT 2025.002, a data "03/08/2026"
de produção da regra UB12-10 está riscada; a redação vigente diz "implementação
futura para produção").

Para cada NT, em `texto/`:

- `<nt>-vigente.txt` — **fonte principal das notas.** Gerado por
  `scripts/extrair_nt.py` (requer `pip install pymupdf`): só o texto não riscado,
  uma linha visual por linha, colunas separadas por " | ".
- `<nt>-riscado.md` — lista, por página, do que está riscado (auditoria; **não**
  usar nas notas).
- `<nt>.txt` (`pdftotext -enc UTF-8`) e `<nt>-layout.txt` (`pdftotext -layout`):
  apoio de leitura; contêm o texto riscado misturado. Na `.txt` alguns códigos
  perdem o hífen na quebra de linha (ex.: "N1250").

Linhas riscadas por NT (2026-10-07): 2025.002-RTC 32; 2026.002 52; 2026.007 5;
2026.008 34; 2026.010 0.

Identificadores técnicos (tags, códigos de regra, códigos de rejeição) são
conferidos com `scripts/conferir_tags.py` contra os `-vigente.txt`.

## Hierarquia

A NT diz **como preencher e validar** o documento fiscal; não cria nem altera
tributo. Lei (LC 214/2025, LC 123/2006) > resolução/ato infralegal > NT.
