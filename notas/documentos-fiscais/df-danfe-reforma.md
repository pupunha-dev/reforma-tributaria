---
título: DANFE da reforma tributária — novo leiaute de impressão com IBS, CBS e IS (NT 2026.010)
dominio: documentos-fiscais
fontes: NT 2026.010 v1.00 (seções 1 a 5 e cronograma); NT 2025.002-RTC v1.52, seção 9
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# DANFE da reforma (NT 2026.010)

## A lógica em uma frase

O DANFE é a "fotografia em papel" (ou PDF) da NF-e modelo 55. A NT 2026.010
acrescenta a essa fotografia os **novos tributos**: um bloco de totais de
IBS/CBS/IS, a classificação tributária e as bases, alíquotas e valores por
item, mexendo o mínimo possível no desenho atual.

## Histórico e cronograma

- A NT 2025.002-RTC (seção 9) dizia que as mudanças no DANFE estavam "em estudo"
  e sairiam em nova versão. Quem as trouxe foi a **NT 2026.010**.
- **Cronograma da NT 2026.010 v1.00:** sem data de teste; **produção em
  01/12/2026**.
- Diretrizes, em ordem de prioridade: mínima ruptura com o modelo atual,
  legibilidade e compatibilidade com o papel A4. Há um leiaute de referência em
  **retrato** (principal) e um alternativo em **paisagem**, com os mesmos campos.
  Os modelos de referência acompanham a NT em arquivos próprios, que **não**
  estão nas fontes.

> ⚠️ **Citação da NT × lei:** a NT 2026.010 atribui as alíquotas de teste de 2026
> (0,1% de IBS estadual e 0,9% de CBS) à EC 132/2023. Elas estão nos arts. 343 e
> 346 da LC 214/2025, como cita a NT 2025.002-RTC (ver
> [[df-calculo-e-validacoes]] e [[transicao-fixacao-aliquotas]]).

## ⏳ Em produção a partir de 01/12/2026 — NT 2026.010 v1.00 (cronograma)

**Novo bloco "Total do IBS/CBS/IS" (4.1)**, logo depois de "Total do ICMS/IPI":

| Campo impresso | Tag (ID) |
|---|---|
| Valor da CBS | `vCBS` (W56) |
| Valor do IBS UF | `vIBSUF` (W41) |
| Valor do IBS Município | `vIBSMun` (W46) |
| Valor do Imposto Seletivo | `vIS` (W33) |
| Valor do IBS / da CBS monofásicos | `vIBSMono` (W58) / `vCBSMono` (W59) |
| Valor do IBS / da CBS monofásicos por retenção | `vIBSMonoReten` (W59a) / `vCBSMonoReten` (W59b) |

**Quadro do emitente (4.2):** passa a mostrar o **Código do Regime Tributário**
(`CRT`, C21) e reserva área para o "Tipo de Regime de Apuração do IBS e da CBS",
cuja tag "a ser publicada em NT futura". Enquanto não houver, **não imprimir**
conteúdo nesse campo.

**Itens — "Dados dos Produtos/Serviços" (4.3):**

| Campo impresso | Tag (ID) |
|---|---|
| Classificação Tributária do IBS/CBS | `cClassTrib` (UB14) |
| Base de cálculo IBS/CBS | `vBC` (UB16) |
| Alíquota e valor do IBS UF | `pIBSUF` (UB18) ou `pAliqEfet` (UB28); `vIBSUF` (UB35) |
| Alíquota e valor do IBS Município | `pIBSMun` (UB37) ou `pAliqEfet` (UB47); `vIBSMun` (UB54) |
| Alíquota e valor da CBS | `pCBS` (UB56) ou `pAliqEfet` (UB66); `vCBS` (UB67) |
| Base, alíquota e valor do IS | `vBCIS` (UB05), `pIS` (UB06), `vIS` (UB11) |

**Regra das alíquotas impressas:** havendo redução de alíquota ou compra
governamental (grupo `gRed` informado), o DANFE mostra a **alíquota efetiva**
(`pAliqEfet`); sem `gRed`, mostra a alíquota vigente. No IS, sempre `pIS`.

**Campos facultativos (4.4):** quadros que podem ser suprimidos ou só aparecem
quando a informação existe no XML (canhoto, fatura e duplicatas, FCP, DIFAL,
monofásicos, ISSQN, transporte, QR Code). Nos modelos ficam em azul com borda
tracejada. A faculdade "não autoriza a criação, inferência ou impressão de
informação inexistente no XML".

**QR Code (4.5):** o grupo ZX (`qrCode`, `urlChave`) já tem uso previsto na NF-e;
uma alteração futura vai prever o QR Code também nos DANFE retrato e paisagem,
com regras de formação e validação. Essa alteração **não está nas fontes**.

## Ligações

- [[df-grupo-ibs-cbs-is]]: as tags impressas.
- [[df-calculo-e-validacoes]]: a alíquota efetiva.
- [[df-emissao-offline-alerta]]: o DANFE Simplificado Tipo 2 (NT 2026.002).
- [[df-visao-geral-reforma-nfe]]: linha do tempo das NTs.
