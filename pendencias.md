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

| # | Fonte | Onde procurar | Notas afetadas |
|---|---|---|---|
| F1 | Anexos VI, VII, X, XI e XII da Res. CGSN 140/2018 | Portal do Simples Nacional → Legislação → Res. CGSN 140 | [[sn-vedacoes-ingresso]], [[sn-mei-regulamentacao]], [[sn-sublimites-icms-iss]] |
| F2 | Res. CGSN 11/2007 (repasse) | Portal do Simples Nacional → Legislação (resoluções antigas) | [[sn-repasse-arrecadacao]] |
| F3 | Tabela **cCredPres** (CST e cClassTrib já foram capturados em 2026-10-08, ver [[df-tabela-cclasstrib]]) | Portal Nacional da NF-e ou Portal da Conformidade Fácil: procurar se há página própria | [[df-cst-cclasstrib]] |
| F4 | NT futura para emitentes do Simples/MEI (CRT 1, 2 e 4) | Portal Nacional da NF-e, lista de NTs (ainda não publicada) | [[df-visao-geral-reforma-nfe]], [[sn-obrigacoes-acessorias]] |

## C. Em andamento

Nada em andamento. F3 (CST e cClassTrib) foi concluída em 2026-10-08; resta só a
tabela cCredPres.

## D. Adiados (só se o usuário pedir)

Rótulos do mapa sem o § pai; o mapa não lista revogações anteriores a 2025;
redação em sn-transacao e sn-recolhimento-das; VB01-10 sem a condição
"tpOp ≠ 2"; link para a exceção 4 de B25-80; `extrair_nt.py` não detecta
anotações StrikeOut nem trechos parcialmente riscados; `VERSAO_NT` exige duas
casas decimais.
