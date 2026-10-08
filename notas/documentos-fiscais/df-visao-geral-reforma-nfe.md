---
título: NF-e e NFC-e na reforma tributária — visão geral e linha do tempo das Notas Técnicas
dominio: documentos-fiscais
fontes: NT 2025.002-RTC v1.52, controle de versões, cronograma, detalhamento do cronograma e seção 1; NT 2026.002 v1.11, NT 2026.007 v1.10, NT 2026.008 v1.00 e NT 2026.010 v1.00, cronogramas
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# NF-e e NFC-e na reforma: visão geral

## A lógica em uma frase

A reforma não criou uma nota fiscal nova: ela acrescentou à NF-e (modelo 55) e à
NFC-e (modelo 65) **campos para IBS, CBS e Imposto Seletivo (IS)**, com regras de
validação próprias. Pense numa planilha que ganha colunas novas: durante a
transição, a SEFAZ primeiro **aceita** as colunas preenchidas (e confere a conta),
depois passa a **exigir** que estejam preenchidas. Quem dita o "quando" é o
**cronograma** de cada Nota Técnica (NT), em duas etapas: **homologação**
(ambiente de teste) e **produção** (notas reais).

## De onde vem e o que substitui (NT 2025.002-RTC, seção 1)

- A NT se apoia na LC 214/2025, que obriga União, Estados, DF e Municípios a
  adaptar os sistemas autorizadores de documentos fiscais eletrônicos a um
  leiaute padronizado com IBS, CBS e IS (a NT cita o art. 62 da LC 214; ver
  [[ibs-cbs-cadastro-documento-fiscal]]).
- Ela **substitui** a RT NT 2024.002 no âmbito da NF-e/NFC-e e será ajustada ao
  longo da implantação.
- **Hierarquia:** a NT diz **como preencher e validar**; quem define se o
  tributo é devido é a lei. A própria NT diz que a validade jurídica das
  informações dos novos tributos "se dará conforme os prazos estabelecidos na
  legislação, independentemente de já estarem preenchidos".

> **Cuidado com o PDF:** as NTs marcam a redação superada com **texto riscado**.
> Esta nota usa só a redação vigente (ver `fontes/documentos-fiscais/FONTE.md`).

## Contribuinte do regime normal (CRT 3): o que vale hoje

Detalhamento do cronograma da NT 2025.002-RTC, para **CRT 3=Regime Normal**:

| Desde | Homologação | Produção |
|---|---|---|
| Julho/2025 | preenchimento facultativo; se preenchidos, as regras de validação (RV) são aplicadas | campos ainda não implantados (erro de schema) |
| Outubro/2025 | facultativo; RV aplicadas se preenchidos | facultativo; RV aplicadas se preenchidos; **sem valor jurídico** |
| Janeiro/2026 | facultativo; RV aplicadas se preenchidos | não exigido por RV, **porém obrigatório conforme a legislação vigente**; RV aplicadas às notas com IBS/CBS; **com valor jurídico a partir de 01/01/2026** |
| 01/07/2026 | **obrigatório** | igual a janeiro/2026 |

Em palavras simples: em **produção**, hoje (07/10/2026), a SEFAZ **ainda não
rejeita** a NF-e de regime normal que venha sem o grupo de IBS/CBS, mas a
legislação já obriga a informar, e o que for informado já vale juridicamente
desde 01/01/2026. Em **homologação**, o grupo já é obrigatório.

A regra que fará a rejeição em produção é a **UB12-10** (rejeição 1115,
"Grupo IBSCBS não informado"), na redação vigente:

- em **homologação**: NF-e com data de emissão maior ou igual a 01/07/2026 e
  emitente com CRT 3;
- em **produção**: "implementação futura" — **sem data** na versão 1.52 (a data
  que constava antes está riscada no PDF);
- não se aplica à devolução (finalidade 4) ou à nota complementar (finalidade 2)
  que referencie NF-e emitida antes de 2027, nem a combustível da Tabela de
  Combustíveis Sujeitos à Tributação Monofásica.

## ⚠️ Lacuna: Simples Nacional, MEI e monofásicos (CRT 1, 2 e 4)

A NT 2025.002-RTC diz literalmente: "As orientações para CRT=1-Simples
Nacional, CRT=2-Simples Nacional-Excesso de Sublimite, CRT=4-MEI e Tributação
Monofásica serão publicadas em NT futura, tendo em vista que a tributação do
IBS/CBS/IS para estes contribuintes ocorre somente a partir de 2027, conforme
disposto no Art. 348 da LC 214/25." Essa NT futura **não está nas fontes**. O
lado tributário do Simples em 2027 está em [[sn-obrigacoes-acessorias]] e
[[simples-nacional-e-mei]].

## Linha do tempo das 5 NTs (produção)

Já em produção em 07/10/2026:

| NT | O quê | Produção |
|---|---|---|
| 2025.002-RTC v1.40 | cIndOp, compras governamentais (refDFeAnt), Inscrição Suframa, nota de crédito "06=Retorno por recusa parcial", grupo gALCZFMCBS e novas RV | 03/08/2026 |
| 2025.002-RTC v1.51 | alteração de regras de validação | 05/10/2026 |
| 2026.002 v1.00 a 1.10a | limite por UF da NFC-e sem destinatário; DANFE Simplificado Tipo 2; autorização com alerta | 15/06/2026 a 05/10/2026 (ver [[df-emissao-offline-alerta]]) |

## ⏳ Em produção a partir de 03/11/2026 — NT 2025.002-RTC v1.52, NT 2026.007 v1.10 e NT 2026.008 v1.00 (cronograma)

- **NT 2025.002-RTC:** referenciamento da devolução **só no grupo
  "DFeReferenciado"** (regra VC02-14, data alterada de 05/10/2026 para
  03/11/2026 na v1.52); reformulação do leiaute da **tributação monofásica de
  combustíveis** (v1.50).
- **NT 2026.007:** emissão por **contribuinte exclusivo do IBS/CBS** (ver
  [[df-contribuinte-exclusivo-ibs-cbs]]).
- **NT 2026.008:** campos de **valor líquido do produto** e de ICMS previsto no
  pagamento antecipado (ver [[df-valor-liquido-produto]]).

## ⏳ Em produção a partir de 01/12/2026 — NT 2026.010 v1.00 (cronograma)

Novo leiaute do **DANFE** com IBS, CBS e IS (ver [[df-danfe-reforma]]).

## ⏳ Em produção a partir de 14/12/2026 — NT 2026.002 v1.11 (cronograma)

Regras I08-180, BA02-35 e VC02-40 (data alterada de 05/10/2026 para
14/12/2026). Ver [[df-emissao-offline-alerta]].

## ⏳ Em produção a partir de 01/03/2027 — NT 2026.008 v1.00 (cronograma)

Regra de validação NB01-30 (homologação em 01/02/2027).

## ⏳ Sem data — NT 2025.002-RTC v1.52 (cronograma)

Obrigatoriedade, em produção, da informação dos novos tributos (UB12-10):
"Implementação futura".

## Ligações

- [[df-grupo-ibs-cbs-is]]: onde ficam os campos novos no XML.
- [[df-cst-cclasstrib]]: os códigos que classificam cada item.
- [[df-calculo-e-validacoes]]: as contas que a SEFAZ confere.
- [[ibs-cbs-cadastro-documento-fiscal]]: o documento fiscal na LC 214.
- [[ibs-cbs-split-payment]]: o recolhimento que usa as informações da nota.
- [[sn-obrigacoes-acessorias]]: documentos fiscais do optante do Simples.
