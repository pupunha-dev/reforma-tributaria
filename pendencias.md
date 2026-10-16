# Pendências do projeto

Controle do que está **em aberto**. Item decidido pela equipe sai daqui e vai
para [decisions.md](decisions.md) (só posição adotada, regra 6 do
[CLAUDE.md](CLAUDE.md)). Item resolvido por nova fonte sai daqui e a nota é
atualizada. Data-base: 2026-10-08 (itens F11 a F19 incluídos em 2026-10-16).

## A. Decisões da equipe (consultar depois)

Combinado em 2026-10-08: a equipe decide em momento posterior. Até lá, as notas
seguem a hierarquia (lei > resolução) e mantêm o aviso ⚠️.

| # | Ponto | Situação nas fontes | Nota | Recomendação provisória |
|---|---|---|---|---|
| D1 | Dedução do DAS no limite de lucros isentos | LC 123, art. 14, §1º: subtrai o DAS inteiro. Res. 140, art. 145, §1º: subtrai só o IRPJ | [[sn-disposicoes-finais]], [[sn-abrangencia-tributos]] | Manter a LC (nível mais alto e mais conservador); conferir como o PGDAS-D trata na prática |
| D2 | Prazo de 20/12/2026 (Res. 140, art. 144-E, I) anterior aos efeitos da Res. 190 (01/01/2027) | As fontes não resolvem o descompasso | [[sn-disposicoes-finais]] | Tratar 20/12/2026 como prazo real; acompanhar correção oficial |
| D3 | Prazo da opção pelo Simples para 2027 | Até 31/12/2026 a opção é em janeiro; depois, em setembro. Sem regra de transição nas fontes; art. 87-B da LC 123 revogado pela LC 227 | [[sn-abrangencia-tributos]], [[sn-disposicoes-finais]] | Não prometer prazo ao cliente; listar os clientes que pretendem entrar em 2027 |

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
| F12 | **Anexo I atual** (leiaute e RN da DPS/NFS-e **com os grupos IBSCBS**; a NT 004 v2.00 cita "v1.00-20251210"; o guia cita v1.01 de 09/02/2026). A cópia nas fontes é de 09/09/2025, sem IBSCBS | Portal da NFS-e Nacional → documentação técnica | [[df-nfse-comercio-exterior]], [[df-nfse-layout-ibscbs]] | média |
| F14 | **Anexo VI** (LeiautesRN_RTC_IBSCBS, v1.04.00 da NT 009): regras de negócio e rejeições do grupo IBSCBS | Portal da NFS-e → documentação técnica (anexo da NT 009) | [[df-nfse-layout-ibscbs]], [[df-nfse-cgnfse-notas-tecnicas]] | **alta** |
| F15 | **Anexo VIII** (correlação item da NBS × cIndOp × cClassTrib) | idem (anexo da NT 005 e seguintes) | [[df-nfse-indop-ibscbs]] | alta |
| F16 | **Cronograma de implantação** das NTs 005, 007 e 009 (notas de ajuste, `vAjusteBC`, `gLocacao`, `gTribSN`, `gPgtoVinc`, CNPJ alfanumérico, DANFSe v2.0) | portal da NFS-e ("cronograma de implantação") | [[df-nfse-cgnfse-notas-tecnicas]], [[df-nfse-layout-ibscbs]], [[df-nfse-danfse]] | alta |
| F17 | Anexos **A** (municípios IBGE e países ISO2) e **B** (lista nacional de serviços e cTribNac/NBS) | idem | [[df-nfse-emissao-servico]], [[df-nfse-comercio-exterior]] | média |
| F18 | **Resolução CGNFS-e nº 9/2025**, Manual para Emissão da NFS-e Via v1.02 e Anexo IV (leiautes RN ADN) | portal da NFS-e → NFS-e Via → documentação técnica | [[df-nfse-via]] | média |
| F19 | NT 004 (1ª versão, 19/08/2025) e NTs 001 e 002; versão do **manual da API** posterior à 1.0 (o arquivo recebido não identifica a versão) | portal da NFS-e → documentação técnica | [[df-nfse-cgnfse-notas-tecnicas]] | baixa |
| F13 | Endereço oficial de origem do **Guia do Emissor** e de cada **NT/anexo da SE/CGNFS-e** (os PDFs não trazem) e versão posterior à 1.2 do guia, se houver | Portal da NFS-e Nacional | [[df-nfse-visao-geral]] | baixa |
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
