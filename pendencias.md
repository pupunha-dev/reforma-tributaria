# Pendências do projeto

Controle do que está **em aberto**. Item decidido pela equipe sai daqui e vai
para [decisions.md](decisions.md) (só posição adotada, regra 6 do
[CLAUDE.md](CLAUDE.md)). Item resolvido por nova fonte sai daqui e a nota é
atualizada. Data-base: 2026-10-08 (itens F11 a F21 incluídos em 2026-10-16).

## A. Decisões da equipe (consultar depois)

Combinado em 2026-10-08: a equipe decide em momento posterior. Até lá, as notas
seguem a hierarquia (lei > resolução) e mantêm o aviso ⚠️.

| # | Ponto | Situação nas fontes | Nota | Recomendação provisória |
|---|---|---|---|---|
| D1 | Dedução do DAS no limite de lucros isentos | LC 123, art. 14, §1º: subtrai o DAS inteiro. Res. 140, art. 145, §1º: subtrai só o IRPJ | [[sn-disposicoes-finais]], [[sn-abrangencia-tributos]] | Manter a LC (nível mais alto e mais conservador); conferir como o PGDAS-D trata na prática |
| D2 | Prazo de 20/12/2026 (Res. 140, art. 144-E, I) anterior aos efeitos da Res. 190 (01/01/2027) | As fontes não resolvem o descompasso | [[sn-disposicoes-finais]] | Tratar 20/12/2026 como prazo real; acompanhar correção oficial |
| D3 | ~~Prazo da opção pelo Simples para 2027~~ **resolvido em 2026-10-16** | Res. CGSN 186/2026 (alterada pela 194/2026) fixa as datas: [[sn-opcao-2027-prazos]]. Resta só a leitura sistemática 186 × 190 (186 específica de 2027; 190 geral dos anos seguintes), que nenhum dos dois atos diz expressamente | [[sn-opcao-2027-prazos]], [[sn-abrangencia-tributos]] | Manter a leitura sistemática com o aviso na nota; registrar em `decisions.md` se a equipe adotar posição |

## B. Fontes que faltam

| # | Fonte | Onde procurar | Notas afetadas | Prioridade |
|---|---|---|---|---|
| F1 | Anexos **VII** (CNAEs ambíguos), **X** (relatório mensal do MEI) e **XII** da Res. CGSN 140/2018 (VI e XI entraram em 2026-10-08) | Portal do Simples Nacional → Legislação → Res. CGSN 140 (PDFs dos anexos) | [[sn-cnae-impeditivos]], [[sn-vedacoes-ingresso]], [[sn-mei-regulamentacao]], [[sn-sublimites-icms-iss]] | média |
| F3 | Planilhas completas do IT 2025.002 (colunas que a página não mostra: alíquotas e percentuais do cCredPres, pRedTransicaoIBS, cClass da nota referenciada; os percentuais dos códigos 1 a 4 já vêm dos regulamentos) e versão do IT posterior à 1.60, se houver | Portal Nacional da NF-e → "Documentos" → "Diversos" | [[df-credito-presumido-ccredpres]], [[df-tabela-cclasstrib]] | média |
| F4 | NT futura para emitentes do Simples/MEI (CRT 1, 2 e 4) | Portal Nacional da NF-e, lista de NTs (ainda não publicada) | [[df-visao-geral-reforma-nfe]], [[sn-obrigacoes-acessorias]] | alta quando sair |
| F8 | Versão atual da **Res. CGIBS 6/2026** (alterações depois de 30/04/2026, se houver) e a **data de publicação** | site do Comitê Gestor do IBS | [[regulamentos-cbs-ibs]], [[ibs-cbs-cadastro-regulamentacao]] (divergência CBS × IBS sobre PF e produtor rural PF) | **alta** |
| F9 | Ato conjunto RFB/CGIBS com as **datas de obrigatoriedade** de cada documento fiscal (art. 112 dos regulamentos) | sites da RFB e do CGIBS | [[ibs-cbs-documento-fiscal-regulamentacao]] | alta |
| F10 | Atos anuais (Ministro da Fazenda e CGIBS) com os **percentuais de crédito presumido** de produtor rural e TAC (divulgados até setembro, vigência em janeiro) | DOU / sites da RFB e do CGIBS | [[ibs-cbs-credito-presumido-regulamentacao]] | alta (2027) |
| F11 | Ato que fixa as datas de obrigatoriedade do IBS/CBS na NFS-e que o guia cita (03/08/2026 regime regular; 01/01/2027 Simples, por fato gerador) | Portal da NFS-e Nacional; atos da RFB/CGIBS/CGNFS-e | [[df-nfse-visao-geral]], [[df-nfse-emissao-pessoas]], [[df-nfse-emissao-valores-ibs-cbs]], [[df-nfse-cgnfse-notas-tecnicas]] | alta |
| F12 | ~~Anexo I atual~~ **fechada em 2026-10-16**: Anexo I v1.01-20260209 entrou. Resta confirmar no portal se existe versão posterior | Portal da NFS-e Nacional → documentação técnica | [[df-nfse-comercio-exterior]], [[df-nfse-layout-ibscbs]] | baixa |
| F14 | ~~Anexo VI~~ **entrou em 2026-10-16** (v1.04.01, layout da NT 009 v1.01). Resta a **data de produção** do Anexo VI (junto com F16) | Portal da NFS-e → documentação técnica | [[df-nfse-regras-ibscbs-anexo-vi]], [[df-nfse-layout-ibscbs]] | **alta** |
| F15 | ~~Anexo VIII oficial~~ **entrou em 2026-10-16** (v1.01.00, [[df-nfse-correlacao-nbs-indop]]). Resta confirmar no portal se é a versão mais recente; o CSV de terceiros continua reprovado | Portal da NFS-e (anexo da NT 005 e seguintes) | [[df-nfse-correlacao-nbs-indop]] | baixa |
| F16 | **Cronograma de implantação** das NTs 005, 007 e 009 e do Anexo VI v1.04.01 (notas de ajuste, `vAjusteBC`, `gLocacao`, `gTribSN`, `gPgtoVinc`, CNPJ alfanumérico, DANFSe v2.0) | portal da NFS-e ("cronograma de implantação") | [[df-nfse-cgnfse-notas-tecnicas]], [[df-nfse-layout-ibscbs]], [[df-nfse-danfse]] | alta |
| F17 | Anexo **A**, parte **países ISO2** (os municípios IBGE entraram em 2026-10-16). ~~Anexo B (lista de serviços)~~ **entrou em 2026-10-16** na versão v1.01-20260122 (338 códigos) | idem | [[df-nfse-emissao-servico]], [[df-nfse-comercio-exterior]], [[df-nfse-lista-servicos-ctribnac]] | média |
| F18 | **Resolução CGNFS-e nº 9/2025**, Manual para Emissão da NFS-e Via v1.02 e **Anexo IV da NFS-e Via** (`LeiautesRN_ADN-SNNFSeVia_V1.00.04`; o "Anexo IV" que está nas fontes é o do ADN) | portal da NFS-e → NFS-e Via → documentação técnica | [[df-nfse-via]], [[df-nfse-adn-distribuicao]] | média |
| F19 | NT 004 (1ª versão, 19/08/2025) e NTs 001 e 002; versão do **manual da API** posterior à 1.0 (o arquivo recebido não identifica a versão) | portal da NFS-e → documentação técnica | [[df-nfse-cgnfse-notas-tecnicas]] | baixa |
| F13 | Endereço oficial de origem do **Guia do Emissor** e de cada **NT/anexo da SE/CGNFS-e** (os PDFs não trazem) e versão posterior à 1.2 do guia, se houver | Portal da NFS-e Nacional | [[df-nfse-visao-geral]] | baixa |
| F20 | **Texto original** da Res. CGSN 186/2026 (DOU de 17/04/2026, antes da 194) e **conferência com o DOU** das Res. CGSN 186, 187, 188, 192 e 193/2026, recebidas como texto extraído | Diário Oficial da União (in.gov.br) ou Portal Normas da Receita (visão multivigente da Res. 186) | [[sn-opcao-2027-prazos]], [[sn-repasse-arrecadacao]], [[sn-recolhimento-das]] | média |
| F21 | Texto **atualizado** da Res. CGSN 11/2007 (com o art. 17-A e demais alterações anteriores a 2026); as fontes têm o original de 2007 mais os trechos da Res. 192/2026 | Portal Normas da Receita (visão multivigente) | [[sn-repasse-arrecadacao]] | média |
| F7 | SC Cosit nº 66/2013 (CNAE × atividade real), citada na SC 71/2026 | Portal Normas da Receita | [[sn-cnae-impeditivos]], [[sn-solucoes-consulta]] | baixa |

Os regulamentos da CBS e do IBS (antes F5 e F6) e a Res. CGSN 11/2007 (antes F2)
entraram em 2026-10-08. F8 a F10 surgiram da leitura dos regulamentos.

## C. Em andamento

Nada em andamento.

## D. Concluídos em 2026-10-08

- Regulamentos da CBS (Decreto 12.955/2026, compilado com o Decreto 13.075/2026) e
  do IBS (Res. CGIBS 6/2026): mapa gerado, bloco "Regulamentação" em 90 notas e 4
  notas novas ([[regulamentos-cbs-ibs]]); Res. CGSN 11/2007 em
  [[sn-repasse-arrecadacao]].

- Tabelas CST/cClassTrib e cCredPres capturadas do Portal dos DF-e (endereços do
  IT 2025.002 v1.60): [[df-tabela-cclasstrib]], [[df-credito-presumido-ccredpres]].
- Anexos VI e XI da Res. 140: [[sn-cnae-impeditivos]], [[sn-mei-ocupacoes]].
- SC Cosit 71/2026: [[sn-solucoes-consulta]].
- Itens que estavam adiados: rótulos do mapa da Res. 140 com o § pai e anexos
  corretos (o "Anexo VIII" era o XI), revogações de qualquer data no mapa, redação
  em sn-transacao e sn-recolhimento-das, condição "tpOp ≠ 2" da VB01-10, Exceção 4
  da B25-80, `extrair_nt.py` com riscado parcial (anotação StrikeOut coberta por
  teste) e `VERSAO_NT` com uma casa decimal.

## E. Concluídos em 2026-10-16

- Notas Técnicas da SE/CGNFS-e 003 a 010, Anexo I (cópia anterior ao RTC), Anexo VII v1.03.00 e manual da
  API: seis notas novas ([[df-nfse-cgnfse-notas-tecnicas]], [[df-nfse-layout-ibscbs]],
  [[df-nfse-comercio-exterior]], [[df-nfse-indop-ibscbs]], [[df-nfse-danfse]], [[df-nfse-via]]).
  Resolveu a parte de F12 (Anexo VII e regras de comércio exterior); o que continua aberto está em F12 e F14 a F19.
- Lista nacional de serviços do portal da NFS-e (335 códigos de tributação nacional; depois substituída como base pelo Anexo B v1.01-20260122, com 338) e tabela de municípios do
  IBGE (DTB de 22/11/2024), com o script `scripts/consulta_ibge.py`: [[df-nfse-lista-servicos-ctribnac]],
  [[df-nfse-codigos-ibge-localidades]]. A NT 2025.002 v1.33 (superada) e o CSV de terceiros ficaram arquivados sem uso.
- Anexo B v1.01-20260122 (lista nacional de serviços: 338 códigos com títulos de item e subitem; lista de NBS v2.0 com 1.210 entradas): reescrita de [[df-nfse-lista-servicos-ctribnac]]; fecha a parte "Anexo B" de F17.
- Anexos oficiais novos (Anexo I v1.01, II, IV-ADN, VI v1.04.01, VIII) e NT 009 v1.01: dez notas novas
  ([[df-nfse-regras-ibscbs-anexo-vi]], [[df-nfse-eventos]], [[df-nfse-adn-distribuicao]],
  [[df-nfse-correlacao-nbs-indop]] e seis `df-nfse-correlacao-itens-*`) e revisão das notas antigas.
  Fechou F12 e F15 (restam confirmações de versão) e o texto de F14 (resta a data de produção).
  Abertos desta entrada: **código de lista de serviços** `110501`, `141403` e `141404` do Anexo I que a lista do portal
  não traz (confirmar atualização do portal; ver [[df-nfse-lista-servicos-ctribnac]]); discrepância de data da NT 009 v1.01
  (11/09/2026 no texto; 01/10/2026 no rótulo do portal); Anexo VII v1.02.01 citado pela NT 009 v1.01 × v1.03.00 nas fontes.
- Res. CGSN 186/2026 (redação da 194/2026), 187, 188, 192 e 193/2026 (a 191 já estava nas fontes): nota nova
  [[sn-opcao-2027-prazos]] e atualização de [[sn-abrangencia-tributos]], [[sn-disposicoes-finais]],
  [[sn-recolhimento-das]], [[sn-parcelamento]] e [[sn-repasse-arrecadacao]]. Fechou D3 (prazo da opção de 2027). Abriu F20 e F21.

## F. Propostas aguardando decisão da equipe

Surgiram em 2026-10-16, quando uma resposta do bot errou por falta de um ato nas fontes. Nenhuma foi implantada.

| # | Proposta | Para que serve | Custo / cuidado |
|---|---|---|---|
| P1 | **Registrar as perguntas do bot** em uma tabela (data, pergunta, notas escolhidas pelo roteador, se a resposta foi marcada como lacuna) | Achar lacunas de fonte pelo uso real, sem depender de alguém reclamar | Exige nó novo no n8n e cuidado com dados de clientes: **não guardar nome de cliente nem CNPJ**; avaliar se o log fica só no n8n |
| P2 | **Varredura periódica** de atos novos (Res. CGSN, NTs do Portal da NF-e, NTs da SE/CGNFS-e) com aviso ao responsável | Evitar que um ato novo (como as Res. 186/194) fique meses fora das fontes | Depende de acesso às páginas oficiais; o ambiente do Claude só alcança sites permitidos. Alternativa mais simples: conferir as páginas de atos toda semana e enviar o que for novo |
