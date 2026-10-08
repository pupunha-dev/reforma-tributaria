---
título: Emissão offline, autorização com alerta e DANFE Simplificado Tipo 2 (NT 2026.002)
dominio: documentos-fiscais
fontes: NT 2026.002 v1.11 (seções 1 a 4 e cronograma)
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# Emissão offline, autorização com alerta e DANFE Simplificado Tipo 2

## A lógica em uma frase

Esta NT **não trata de IBS/CBS**: ela aproxima a NF-e (modelo 55) da NFC-e
(modelo 65) no varejo. Quem vende ao consumidor pode usar a **NF-e com um DANFE
simplificado** (Tipo 2), inclusive em **contingência offline**, e a SEFAZ passa a
poder **autorizar com alerta**: a nota sai, mas com um aviso de inconsistência,
como um semáforo amarelo em vez de vermelho. A base são os Ajustes SINIEF nº
32/25 e nº 13/26 do CONFAZ, que **não estão nas fontes**. As regras estaduais de
ICMS ficam fora do escopo.

## O que a NT contempla (seção 1)

- NF-e com **DANFE Simplificado Tipo 2** em operações presenciais e não
  presenciais que "normalmente seriam acobertadas por NFC-e";
- **autorização com alerta** na NFC-e quando o destinatário com CNPJ estiver em
  situação irregular;
- **vedação de NF-e de saída referenciando NFC-e ou CF-e** (modelo 59), salvo NF-e
  complementar;
- **contingência offline** para NF-e com tipo de emissão "9=Contingência off-line
  da NFC-e e da NF-e com DANFE Simplificado Tipo 2", com transmissão posterior.

## Autorização com alerta (seção 2)

| `cStat` | Resultado |
|---|---|
| 100 | Autorizado o uso da NF-e |
| **120** | **Autorizado o uso da NF-e, com alerta** (novo; inicialmente só para a NFC-e) |
| 150 | Autorizado o uso da NF-e, autorização fora de prazo |
| XXXX | Rejeição |

- Com alerta, a nota é **armazenada** e **não precisa** ser corrigida e
  retransmitida. Autorizada fora de prazo **e** com alerta, retorna 120.
- A regra com efeito "Alerta" não interrompe o processamento; são guardados até
  **5 códigos de alerta**. Os alertas voltam no protocolo, no grupo PR13 (`cMsg`,
  `xMsg`).
- Regra de alerta criada: **5E17-65** (NFC-e): destinatário com CNPJ em
  situação irregular na UF (vedado ou bloqueado no CCC) → alerta 172.

## Campos (seção 3)

- `tpImp` (B21): novo valor **6 = DANFE Simplificado Tipo 2** (nas condições do
  Ajuste SINIEF 13/26).
- `tpEmis` (B22): o valor **9** passa a ser "Contingência off-line da NFC-e e da
  NF-e com DANFE Simplificado Tipo 2".
- `indPres` (B25b): o valor **4** passa a ser "Operações não presenciais com
  NFC-e e NFe com DANFE Simplificado Tipo 2 (com entrega)".

## Regras principais (seção 4)

| Regra | Situação que rejeita | Rejeição |
|---|---|---|
| B22-10 | NF-e em contingência offline (`tpEmis` = 9) sem DANFE Simplificado Tipo 2 | 711 |
| B25-20 | NFC-e ou NF-e com DANFE Simplificado Tipo 2 com finalidade diferente de 1-Normal | 715 |
| E01-20 | NFC-e ou NF-e Tipo 2 em operação **não presencial com entrega** (`indPres` = 4) sem identificar o destinatário | 787 |
| F01-10 | NFC-e ou NF-e Tipo 2 com local de retirada | 669 |
| I17b-10 | NFC-e ou NF-e Tipo 2 com item que não participa do total | 774 |
| W16-40 | NFC-e acima de **R$ 10.000,00 ou outro valor definido pela UF** sem CPF/CNPJ do destinatário | 750 |

Em palavras simples: o DANFE Simplificado Tipo 2 é para **venda normal**
(finalidade 1); na venda com entrega o comprador precisa ser identificado; e
cada UF pode fixar o próprio limite da NFC-e sem destinatário (sem definição,
vale R$ 10.000,00).

## Cronograma

Já em produção em 07/10/2026 (versões 1.00 a 1.10a):

| O quê | Teste | Produção |
|---|---|---|
| limite por UF da NFC-e sem destinatário (W16-40) | 01/06/2026 | 15/06/2026 |
| schema e regras da NF-e com DANFE Simplificado Tipo 2 | 01/07/2026 | 03/08/2026 |
| autorização com alerta (5E17-65) e demais ajustes das versões 1.00 a 1.10a, exceto BA02-35, VC02-40 e I08-180 (ver abaixo) | 01/09/2026 | 05/10/2026 |

A tabela de cronograma da NT alinha algumas linhas da versão 1.00 de forma
ambígua com as datas. As datas acima são as que aparecem ao lado de cada item no
texto vigente. A versão 1.10 **removeu** regras como BA05-10, BA06-10, I08-184,
I08-186 e VC02-50.

## ⏳ Em produção a partir de 14/12/2026 — NT 2026.002 v1.11 (cronograma)

A v1.11 adiou de 05/10/2026 para **14/12/2026** a produção de:

- **BA02-35** e **VC02-40** (rejeição 679): NF-e de **saída** que não seja
  complementar nem devolução não pode referenciar (na nota ou no item) **NFC-e**
  (modelo 65), **CF-e** (modelo 59) ou **NF-e com DANFE Simplificado Tipo 2**;
- **I08-180** (rejeição 375): NF-e de lançamento relativo a Cupom Fiscal (CFOP
  5.929 ou 6.929) que referencie NFC-e.

## Ligações

- [[df-danfe-reforma]]: o novo DANFE com IBS/CBS (NT 2026.010).
- [[df-visao-geral-reforma-nfe]]: linha do tempo das NTs.
- [[sn-obrigacoes-acessorias]]: documentos fiscais do optante do Simples.
