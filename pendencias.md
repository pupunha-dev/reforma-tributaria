# Pendências do projeto

Controle do que está **em aberto**. Item decidido pela equipe sai daqui e vai
para [decisions.md](decisions.md) (só posição adotada, regra 6 do
[CLAUDE.md](CLAUDE.md)). Item resolvido por nova fonte sai daqui e a nota é
atualizada. Data-base: 2026-10-08.

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
| F2 | Res. CGSN 11/2007 (repasse) | Portal do Simples Nacional → Legislação (resoluções antigas) | [[sn-repasse-arrecadacao]] | baixa |
| F3 | Planilhas completas do IT 2025.002 (colunas que a página não mostra: alíquotas e percentuais do cCredPres, pRedTransicaoIBS, cClass da nota referenciada) e versão do IT posterior à 1.60, se houver | Portal Nacional da NF-e → "Documentos" → "Diversos" | [[df-credito-presumido-ccredpres]], [[df-tabela-cclasstrib]] | média |
| F4 | NT futura para emitentes do Simples/MEI (CRT 1, 2 e 4) | Portal Nacional da NF-e, lista de NTs (ainda não publicada) | [[df-visao-geral-reforma-nfe]], [[sn-obrigacoes-acessorias]] | alta quando sair |
| F5 | **Decreto nº 12.955, de 29/04/2026** (Regulamento da CBS) | Planalto, seção de Decretos de 2026 (provável) | domínio reforma (todas as notas de CBS); trechos por código já estão no JSON do cClassTrib | **alta** |
| F6 | **Resolução CGIBS nº 6, de 30/04/2026** (Regulamento do IBS) | site do Comitê Gestor do IBS (provável) | domínio reforma (todas as notas de IBS) | **alta** |
| F7 | SC Cosit nº 66/2013 (CNAE × atividade real), citada na SC 71/2026 | Portal Normas da Receita | [[sn-cnae-impeditivos]], [[sn-solucoes-consulta]] | baixa |

F5 e F6 foram identificadas no IT 2025.002 v1.60 (seção 02): as tabelas oficiais
já citam o texto desses regulamentos. São o próximo passo natural para escalar o
domínio reforma (a LC 214 diz a regra; o regulamento diz como operar).

## C. Em andamento

Nada em andamento.

## D. Concluídos em 2026-10-08

- Tabelas CST/cClassTrib e cCredPres capturadas do Portal dos DF-e (endereços do
  IT 2025.002 v1.60): [[df-tabela-cclasstrib]], [[df-credito-presumido-ccredpres]].
- Anexos VI e XI da Res. 140: [[sn-cnae-impeditivos]], [[sn-mei-ocupacoes]].
- SC Cosit 71/2026: [[sn-solucoes-consulta]].
- Itens que estavam adiados: rótulos do mapa da Res. 140 com o § pai e anexos
  corretos (o "Anexo VIII" era o XI), revogações de qualquer data no mapa, redação
  em sn-transacao e sn-recolhimento-das, condição "tpOp ≠ 2" da VB01-10, Exceção 4
  da B25-80, `extrair_nt.py` com riscado parcial (anotação StrikeOut coberta por
  teste) e `VERSAO_NT` com uma casa decimal.
