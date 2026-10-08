---
título: Plano de notas — Documentos fiscais eletrônicos (Notas Técnicas NF-e)
status: concluido
---

# Plano de notas — documentos-fiscais

Fontes: 5 Notas Técnicas do Projeto NF-e (ver `fontes/documentos-fiscais/FONTE.md`).
Data-base: 07/10/2026. Aprovado por delegação do usuário ("faça o melhor que
achar", 07/10/2026).

Regra de vigência do domínio: a NT não tem "produção de efeitos", tem
implantação em **homologação** (teste) e em **produção**. O que ainda não está em
produção em 07/10/2026 vai para um bloco `⏳ Em produção a partir de ...`.

## Mapa seção da NT → nota

| Nota | NT e seções | Vigência prevista | Conteúdo |
|---|---|---|---|
| df-visao-geral-reforma-nfe.md | NT 2025.002-RTC v1.52: controle de versões, cronograma, detalhamento do cronograma, seção 1 | com-mudanca-programada | O que mudou na NF-e/NFC-e, linha do tempo consolidada das 5 NTs, valor jurídico dos campos, lacuna CRT 1/2/4 |
| df-cst-cclasstrib.md | NT 2025.002-RTC v1.52: seções 2 e 3; Anexos I a IV | atual | Tipos básicos da tributação, CST e cClassTrib; onde estão as tabelas (Anexos I e II ainda lacuna) |
| df-tabela-cclasstrib.md | IT 2025.002 v1.60, seções 02, 03, 06 e 07; Portal dos DF-e, captura 2026-10-08; NT 2025.002-RTC v1.52, seção 3 e Anexo III | atual | Os 18 CST e os 173 cClassTrib: reduções de IBS/CBS, tipo de alíquota, vigência, documentos, tpRBSN, histórico das versões do IT |
| df-credito-presumido-ccredpres.md | IT 2025.002 v1.60, seções 04 e 06; Portal dos DF-e, captura 2026-10-08; NT 2025.002-RTC v1.52, Anexo IV e UB120 a UB130 | com-mudanca-programada | Os 13 cCredPres, apropriação, vigência por tributo, divergência do exemplo 5 da NT |
| df-finalidade-debito-credito.md | NT 2025.002-RTC v1.52: seção 4; NT 2026.008 v1.00 (Exceção 4 da B25-80) | com-mudanca-programada | Finalidades 5 (crédito) e 6 (débito), tipos de nota de débito/crédito |
| df-grupo-ibs-cbs-is.md | NT 2025.002-RTC v1.52: seção 6 (leiaute: grupos B, BA, BB, BC, C, I, N01, UB, VB, VC, W03) | com-mudanca-programada | Onde e como informar IBS, CBS e IS no XML |
| df-calculo-e-validacoes.md | NT 2025.002-RTC v1.52: seções 5 e 7 | com-mudanca-programada | Fórmulas de cálculo conferidas pela SEFAZ, regras de validação centrais, códigos de status |
| df-eventos-apuracao.md | NT 2025.002-RTC v1.52: seção 8 | atual | Eventos para apuração do IBS/CBS (crédito presumido, imobilização, perecimento etc.) |
| df-emissao-offline-alerta.md | NT 2026.002 v1.11 (todas as seções) | com-mudanca-programada | Emissão offline, autorização com alerta, DANFE Simplificado Tipo 2, limite da NFC-e sem destinatário |
| df-contribuinte-exclusivo-ibs-cbs.md | NT 2026.007 v1.10 (todas as seções) | com-mudanca-programada | Emissão por contribuinte só de IBS/CBS (sem inscrição estadual) |
| df-valor-liquido-produto.md | NT 2026.008 v1.00 (todas as seções) | com-mudanca-programada | Valor líquido do produto e ICMS previsto no pagamento antecipado |
| df-danfe-reforma.md | NT 2026.010 v1.00 (todas as seções); NT 2025.002-RTC v1.52, seção 9 | com-mudanca-programada | Novo leiaute do DANFE com IBS, CBS e IS |

Ajustes na redação: juntar ou separar notas conforme o volume real; toda seção
das NTs tem uma nota dona.
