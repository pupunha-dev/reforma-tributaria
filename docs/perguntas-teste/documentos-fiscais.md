# Perguntas-teste — domínio documentos-fiscais

Rodar depois de qualquer mudança nas notas `df-*`, nas fontes de
`fontes/documentos-fiscais/`, no protocolo (CLAUDE.md) ou na estrutura. Cada
pergunta é feita numa sessão nova, na raiz do projeto:

    claude -p "<pergunta>" > saida.txt

e a saída precisa conter **todos** os termos da coluna "deve citar" (termos
ligados por "ou" são alternativos: basta um) e respeitar o comportamento
esperado. Rodar também as baterias `reforma.md` e `simples-nacional.md`.

| # | Pergunta | Deve citar | Comportamento esperado |
|---|---|---|---|
| D1 | Na NF-e, em qual grupo e campos informo o valor do IBS da UF de um item? | `df-grupo-ibs-cbs-is` | Grupo IBSCBS (UB12) → gIBSCBS → gIBSUF, com pIBSUF e vIBSUF; cita a versão da NT (2025.002-RTC v1.52) |
| D2 | Recebi a rejeição 1041 ao transmitir uma NF-e. O que significa e como a SEFAZ calcula? | `df-calculo-e-validacoes` | Valor do IBS da UF difere do calculado (UB35-10); fórmula completa vIBSUF = (vBC × alíquota/100) − vDif − vDevTrib, tolerância de 0,01 |
| D3 | A partir de quando o DANFE passa a mostrar os valores de IBS e CBS? | `df-danfe-reforma` | Produção em 01/12/2026 (NT 2026.010 v1.00); deixa claro que hoje (07/10/2026) ainda não vale |
| D4 | Uma empresa prestadora de serviços sem inscrição estadual pode emitir NF-e para vender um bem do ativo imobilizado? | `df-contribuinte-exclusivo-ibs-cbs` | Sim, como contribuinte exclusivo do IBS/CBS, sem IE, autorizada só na SVRS, a partir da produção em 03/11/2026 (hoje só homologação); proibido ICMS, IBS/CBS obrigatório |
| D5 | Em 2027 o valor do IBS e da CBS entra no vProd da NF-e? | `df-valor-liquido-produto` | Sim: pela NT 2026.008, a partir de 2027 IBS, CBS e IS compõem o vProd e não são somados de novo no total; cria vProdLiq; separa hoje × futuro |
| D6 | Como uma empresa do Simples Nacional deve preencher os campos de IBS/CBS na NF-e? | `df-visao-geral-reforma-nfe` | Lacuna: a NT 2025.002-RTC diz que as orientações para CRT 1, 2 e 4 serão publicadas em NT futura; não inventa regra |
| D7 | O que é autorização com alerta na NFC-e? | `df-emissao-offline-alerta` | cStat 120: nota autorizada e armazenada com aviso, sem rejeição; até 5 alertas; regra 5E17-65 (destinatário irregular) |
| D8 | A SEFAZ já rejeita em produção a NF-e de regime normal emitida sem o grupo de IBS/CBS? | `df-visao-geral-reforma-nfe` ou `df-calculo-e-validacoes` | Não: em produção a UB12-10 é "implementação futura", sem data; em homologação vale desde 01/07/2026 (CRT 3); a legislação já obriga e o valor jurídico existe desde 01/01/2026 |
| D9 | Qual o limite de valor da NFC-e sem identificação do destinatário em São Paulo? | `df-emissao-offline-alerta` | Explica a regra nacional (R$ 10.000,00 ou outro valor definido pela UF, W16-40) e sinaliza que o valor de cada UF está fora das fontes; não inventa |
| D10 | Se a Nota Técnica e a LC 214 divergirem sobre o cálculo do IBS, qual vale? | `df-visao-geral-reforma-nfe` ou `df-calculo-e-validacoes` ou `CLAUDE.md` | Vale a lei: hierarquia lei > resolução > nota técnica; a NT diz como preencher e validar, não cria tributo |
| D11 | Quais cClassTrib existem para o CST 220 e algum deles já foi encerrado? | `df-tabela-cclasstrib` | Lista 220001, 220002 e 220003 e informa que a vigência dos três terminou em 01/01/2026; cita a captura de 08/10/2026 |
| D12 | Qual cClassTrib devo usar para vender um produto específico com redução de 60%? | `df-tabela-cclasstrib` | Mostra que a tabela traz os códigos com redução de 60% (CST 200 e outros), mas que enquadrar o produto no dispositivo da LC 214 depende das notas do domínio reforma; não escolhe o código de memória |
| D13 | Quais códigos de cCredPres existem e algum já pode ser usado hoje? | `df-credito-presumido-ccredpres` | 13 códigos; nenhum com vigência iniciada em 08/10/2026 (início em 01/01/2027; IBS dos códigos 3, 9 e 12 em 01/01/2029); separa hoje × futuro |
| D14 | Na NF-e, o cCredPres 5 é o do regime opcional de cooperativa? | `df-credito-presumido-ccredpres` | Não: na tabela atual o 5 é o regime automotivo (art. 311); o exemplo da NT 2025.002-RTC está desatualizado e vale a tabela |
| D15 | Quais alíquotas de IBS e CBS devo informar na NF-e em 2027? | `df-calculo-e-validacoes` | pIBSUF 0,05 e pIBSMun 0,05 (IT 2025.002 v1.60 e NT); pCBS "aguardar legislação"/regra de transição em `transicao-fixacao-aliquotas`; deixa claro que em 2026 é 0,1/0/0,9 |
| D16 | O cClassTrib 200034 pode ser usado em nota de empresa do Simples Nacional? | `df-tabela-cclasstrib` | Mostra o tpRBSN do código ("1 Receita bruta interna") e os documentos (NFe, NFCe, DUIMP); ressalva que as regras de NF-e para CRT 1, 2 e 4 dependem de NT futura |
