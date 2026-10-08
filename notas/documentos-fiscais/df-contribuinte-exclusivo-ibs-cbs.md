---
título: NF-e emitida por contribuinte exclusivo do IBS/CBS (sem inscrição estadual)
dominio: documentos-fiscais
fontes: NT 2026.007 v1.10 (seções 1 a 6 e cronograma)
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# Contribuinte exclusivo do IBS/CBS emitindo NF-e

## A lógica em uma frase

Com a reforma, quem **não** é contribuinte do ICMS (por exemplo, um prestador de
serviços contribuinte do ISS) também passa a precisar de NF-e para documentar
operações com IBS/CBS, como vender um bem do ativo imobilizado ou transferir
bens entre estabelecimentos. Até agora a NF-e exigia **inscrição estadual (IE)**.
A NT 2026.007 cria a "porta de entrada" para quem não tem IE: a nota sai **sem
IE**, é autorizada **só na SVRS** e a SEFAZ confere no cadastro nacional se o
emitente realmente não é contribuinte do ICMS.

## Quem é (seções 1 e 2)

É contribuinte exclusivo do IBS/CBS o emitente que, **ao mesmo tempo**:

- não informa a tag `IE` do emitente;
- tem CNPJ com situação cadastral **"Ativa"** na Receita Federal;
- não tem IE habilitada para ICMS na UF do emitente, conforme o **CCC** (Cadastro
  Centralizado de Contribuintes).

A NT vale para "contribuintes do ISS e demais pessoas contribuintes do IBS/CBS"
que, pelo regulamento do IBS/CBS e pela LC 214, passem a emitir NF-e modelo 55.
Exemplos da própria NT: alienação de **ativo imobilizado** e **transferências**
de bens entre estabelecimentos, inclusive de uso e consumo.

A NT também cria a verificação dos cadastros na **LCC-RFB** (Lista Centralizada
de Contribuintes da Receita Federal), base nacional do CNPJ fornecida às SEFAZ.

## Cronograma

| Versão | Homologação (teste) | Produção |
|---|---|---|
| 1.00 | 01/09/2026 | 03/11/2026 |
| 1.10 | até 05/10/2026 | 03/11/2026 |

Hoje (07/10/2026) as regras abaixo valem **só em homologação**.

## ⏳ Em produção a partir de 03/11/2026 — NT 2026.007 v1.10 (cronograma)

**Campo `IE` (C17):** passa a ter ocorrência 0-1. O contribuinte exclusivo do
IBS/CBS **não informa** a IE. A regra que rejeitava IE ausente na NF-e (C17-10)
foi **excluída**. IE preenchida com zeros continua rejeitada (rejeição 209, regra
C17-20).

Regras para quem emite **sem IE**:

| Regra | Exigência | Rejeição |
|---|---|---|
| C17-11 | autorização **só na SVRS** | 166 |
| C17-42 | **proibido emitir NFC-e** (modelo 65); a regra não se aplica a partir de 2033 | 156 |
| C17-43 | obrigatório informar **CNPJ** do emitente | 157 |
| C18-50 | proibido informar IE de substituto tributário (`IEST`) | 158 |
| I08-191 | só CFOP permitido na tabela do Portal NF-e (coluna "indExcIBSCBS"); não se aplica à devolução nem ao crédito tipo 03 (retorno) | 159 |
| N01-10 | **proibido informar ICMS** e ICMS interestadual; não se aplica à devolução nem ao crédito tipo 03 (retorno) | 161 |
| UB12-11 | **grupo IBS/CBS obrigatório** | 162 |
| 1C17-02 | rejeita se o CCC mostra IE de contribuinte do ICMS habilitada na UF (também para IE "ISENTO") | 163 |
| 1C17-04 | rejeita emitente com situação irregular na UF | 164 |
| 1P10-40 | eventos de autoria do emitente sem IE só na SVRS | 188 |

Outras adaptações: B02-10 e C12-10 deixam de rejeitar, na SVRS, a UF do emitente
diferente da UF do Web Service quando não há IE; B25-90 (NF-e sem ICMS/ISSQN,
rejeição 1002) deixa de se aplicar ao modelo 55 sem IE.

**Cadastro LCC-RFB (para todos os emitentes, modelos 55 e 65):**

- CNPJ do emitente não cadastrado na Receita Federal → rejeição 178 (12C02-10);
  situação diferente de "02-Ativa" → rejeição 179 (12C02-20).
- **CRT × regime na Receita (12C21-20, rejeição 180):** o CRT da NF-e precisa
  bater com o campo "regTrib" da LCC-RFB:

| CRT na NF-e | regTrib na LCC-RFB |
|---|---|
| 1 = Simples Nacional | 1 = optante pelo Simples Nacional |
| 2 = Simples Nacional, excesso de sublimite | 1 = optante pelo Simples Nacional |
| 3 = Regime Normal | 9 = outros regimes |
| 4 = MEI | 2 = optante pelo MEI |

  Em palavras simples: a partir de 03/11/2026, uma empresa **excluída do
  Simples** que continue emitindo com CRT 1, ou um **MEI desenquadrado** que
  continue com CRT 4, terá a NF-e rejeitada. Ver [[sn-exclusao]] e
  [[sn-mei-regulamentacao]].
- Destinatário, local de retirada e local de entrega também passam a ser
  conferidos na LCC-RFB e no CCC.

## Ligações

- [[df-visao-geral-reforma-nfe]]: linha do tempo das NTs.
- [[df-grupo-ibs-cbs-is]]: o grupo IBS/CBS que passa a ser obrigatório.
- [[ibs-cbs-cadastro-documento-fiscal]]: cadastro e documento fiscal na LC 214.
- [[sn-obrigacoes-acessorias]]: documentos fiscais do optante do Simples.
