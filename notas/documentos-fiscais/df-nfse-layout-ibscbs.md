---
título: NFS-e Nacional — layout do IBS/CBS na DPS e na NFS-e (grupo IBSCBS, campos, fórmulas e evoluções das NTs 004, 005, 007 e 009)
dominio: documentos-fiscais
fontes: NT CGNFS-e 004 v2.00 (10/12/2025; layout previsto para produção a partir de 05/01/2026); NT CGNFS-e 005 v1.0 (19/11/2025); NT CGNFS-e 007 v1.0 (07/02/2026); NT CGNFS-e 009 v1.0 (04/06/2026); NT CGNFS-e 003 v1.2 (04/07/2025, substituída); LC 214/2025, art. 12 §2º (conferido em fontes/reforma/texto)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Layout do IBS/CBS na NFS-e Nacional

## A lógica em uma frase

A NFS-e Nacional tem **dois grupos `IBSCBS`**: o da **DPS** (`NFSe/infNFSe/DPS/infDPS/IBSCBS`),
que o **contribuinte informa**, e o da **NFS-e** (`NFSe/infNFSe/IBSCBS`), que a **plataforma
calcula** (Sefin Nacional, com a calculadora de tributos) a partir da DPS. As Notas Técnicas
da SE/CGNFS-e dizem **como preencher e validar**; elas não criam nem alteram tributo (a base e
as alíquotas vêm da LC 214/2025, ver [[ibs-cbs-base-calculo]] e [[ibs-cbs-aliquotas]]). A tela
do emissor que preenche esses campos está em [[df-nfse-emissao-valores-ibs-cbs]] e
[[df-nfse-emissao-pessoas]].

> **Qual versão vale?** A NT CGNFS-e 004 v2.00 "substitui as versões anteriores" (inclusive
> a NT 003 e a NT 004 de 19/08/2025). A NT 005 (19/11/2025) trouxe evoluções que **não** foram
> para a produção em janeiro de 2026; a NT 009 (04/06/2026) as consolida e ajusta. As NTs
> 005 e 009 dizem que o **cronograma** de implantação seria publicado no portal; ele **não está
> nas fontes**. Cada seção abaixo diz de qual NT vem a regra. Ver a cronologia em
> [[df-nfse-cgnfse-notas-tecnicas]].

## Quando o grupo IBSCBS é obrigatório (NT 004 v2.00, seção 1.1)

- Desde o início de 2026 **a regra que exige a informação do grupo `IBSCBS` está desligada**
  nos ambientes de Produção Restrita e de Produção, tanto para a DPS (quem emite no ambiente
  nacional) quanto para a NFS-e (municípios com emissor próprio que compartilham): o grupo é
  **facultativo** e documentos sem ele são autorizados/recepcionados. (O fim dessa suspensão
  não está nas fontes.)
- **Se o grupo for informado**, todas as validações sobre o seu conteúdo **são aplicadas**:
  só a verificação da obrigatoriedade foi suspensa.
- A suspensão **não** dispensa os municípios de se integrarem à plataforma e compartilharem
  seus documentos desde 1º/01/2026 (art. 62 da LC 214/2025, citado pela NT): o prazo
  continua valendo, com a sanção prevista no §7º do mesmo artigo (suspensão de transferências
  voluntárias).
- O ambiente com o grupo `IBSCBS` entrou em Produção Restrita em **10/12/2025**; o mesmo
  layout passou a valer em Produção, com validade jurídica, a partir de **05/01/2026**. No
  início, Emissor Nacional Web, Consulta Pública e DANFSe **não exibiam** o grupo (ver
  [[df-nfse-danfse]]). O guia v1.2 (27/07/2026) já descreve os campos IBS/CBS no emissor Web.
- A tabela de correlação (Anexo VIII: item da NBS × `cIndOp` × cClassTrib) é "norteador"
  sem regras de negócio; **não está nas fontes**.
- Datas de obrigatoriedade para o contribuinte (03/08/2026 no regime regular; 01/01/2027 para
  o Simples por fato gerador) são as **do guia**; o ato que as fixa não está nas fontes
  ([[df-nfse-visao-geral]]).

## Grupo `IBSCBS` da DPS — layout da NT 004 v2.00

Caminho base: `NFSe/infNFSe/DPS/infDPS/IBSCBS` (ocorrência 0-1).

| Campo | Ocor. | O que informa |
|---|---|---|
| `finNFSe` | 1-1 | finalidade: **0 = NFS-e regular** (os demais valores vieram com a NT 009) |
| `indFinal` | 0-1 | operação de uso ou consumo pessoal: 0 não; 1 sim |
| `cIndOp` | 1-1 | código indicador da operação, 6 posições: [[df-nfse-indop-ibscbs]] |
| `tpOper` | 0-1 | operação com entes governamentais ou outros serviços sobre imóveis: 1 fornecimento com pagamento posterior; 2 recebimento do pagamento com fornecimento já realizado; 3 fornecimento com pagamento já realizado; 4 recebimento do pagamento com fornecimento posterior; 5 fornecimento e recebimento concomitantes |
| `gRefNFSe/refNFSe` | 0-1 / 1-99 | chaves (50 posições) de NFS-e referenciadas |
| `tpEnteGov` | 0-1 | ente governamental (administração direta, autarquias e fundações): 1 União; 2 Estado; 3 Distrito Federal; 4 Município |
| `indDest` | 1-1 | destinatário: **0** é o próprio tomador/adquirente; **1** é outra pessoa ou estabelecimento |
| `dest` | 0-1 | destinatário, quando `indDest` = 1: CNPJ, CPF ou NIF (ou `cNaoNIF`), nome, endereço (nacional ou exterior), telefone e e-mail |
| `imovel` | 0-1 | operações com bens imóveis, exceto obras: inscrição imobiliária fiscal (`inscImobFisc`), `cCIB` e endereço do imóvel |
| `valores/gReeRepRes` | 0-1 | reembolso, repasse e ressarcimento (documentos referenciados): ver abaixo |
| `valores/trib/gIBSCBS` | 1-1 | `CST` (3), `cClassTrib` (6) e `cCredPres` (2, opcional); `gTribRegular` (`CSTReg` e `cClassTribReg`) e `gDif` (percentuais de diferimento `pDifUF`, `pDifMun` e `pDifCBS`) |

- **O adquirente não tem grupo próprio.** A NT 004 v2.00 suprimiu o grupo `adq`: para a NFS-e
  Nacional o **tomador** (LC 116) e o **adquirente** (LC 214) são a **mesma pessoa**, identificada
  em `toma`. O **destinatário** (quem recebe o bem ou serviço) pode ser o próprio tomador
  (`indDest` = 0) ou outro (`dest`).
- **CST, cClassTrib e cCredPres** são os das tabelas oficiais: [[df-tabela-cclasstrib]] e
  [[df-credito-presumido-ccredpres]].
- O grupo `obra` (em `serv`) é usado para serviço de obra; `imovel` é para as demais operações
  com imóveis.

### Reembolso, repasse e ressarcimento (`gReeRepRes`, NT 004 v2.00)

Cada documento (`documentos`, 1 a 1000 ocorrências) é um de: **`dFeNacional`** (NFS-e, NF-e, CT-e ou outro, com
a chave de 1 a 50 posições), **`docFiscalOutro`** (município emissor, número e descrição) ou
**`docOutro`** (documento não fiscal), mais o `fornec` (fornecedor: CNPJ, CPF ou NIF, nome),
`dtEmiDoc`, `dtCompDoc`, o tipo `tpReeRepRes` e o valor `vlrReeRepRes` (R$), que **não entra** na
base do ISSQN, do IBS e da CBS desta NFS-e. Tipos: **01** repasse de remuneração por
intermediação de imóveis a demais corretores; **02** repasse de valores a fornecedor, relativo
a fornecimento intermediado por agência de turismo; **03** reembolso ou ressarcimento recebido
por agência de propaganda por serviços de **produção externa** por conta e ordem de terceiro;
**04** idem por serviços de **mídia**; **99** outros (com descrição em `xTpReeRepRes`). A regra
legal está em [[ibs-cbs-base-calculo]] (LC 214, art. 12 §2º IV: o reembolso só fica fora da base
se a documentação fiscal for emitida em nome do terceiro).

## Grupo `IBSCBS` da NFS-e (calculado pela plataforma) — NT 004 v2.00

Caminho base: `NFSe/infNFSe/IBSCBS` (0-1). Os campos abaixo vêm calculados; o emitente não os
informa.

| Campo | O que é | Fórmula ou regra (como escrita na NT) |
|---|---|---|
| `cLocalidadeIncid` / `xLocalidadeIncid` | código IBGE e nome da **localidade de incidência** do IBS/CBS (local da operação) | derivada do `cIndOp` ([[df-nfse-indop-ibscbs]]) |
| `pRedutor` | percentual de redução de alíquota em **compra governamental** | — |
| `valores/vBC` | base de cálculo do IBS/CBS **antes** das reduções | ver "Base de cálculo" abaixo |
| `valores/vCalcReeRepRes` | total do fornecimento próprio de bens materiais ou de operações de terceiros reembolsadas que **não** integra a base | soma dos ajustes informados |
| `uf/pIBSUF`, `pRedAliqUF`, `pAliqEfetUF` | IBS estadual: alíquota da localidade, redução e alíquota efetiva | `pAliqEfetUF = pIBSUF × (1 − pRedAliqUF) × (1 − pRedutor)`; sem `pRedAliqUF` na DPS, a efetiva é a própria `pIBSUF` |
| `mun/pIBSMun`, `pRedAliqMun`, `pAliqEfetMun` | IBS municipal | `pAliqEfetMun = pIBSMun × (1 − pRedAliqMun) × (1 − pRedutor)` |
| `fed/pCBS`, `pRedAliqCBS`, `pAliqEfetCBS` | CBS | `pAliqEfetCBS = pCBS × (1 − pRedAliqCBS) × (1 − pRedutor)` |

Totalizadores (`totCIBS`):

| Campo | Fórmula |
|---|---|
| `gIBS/gIBSUFTot/vIBSUF` | `vBC × (pIBSUF ou pAliqEfetUF)` |
| `gIBS/gIBSMunTot/vIBSMun` | `vBC × (pIBSMun ou pAliqEfetMun)` |
| `gIBS/vIBSTot` | `vIBSUF + vIBSMun` |
| `gCBS/vCBS` | `vBC × (pCBS ou pAliqEfetCBS)` |
| `vDifUF`, `vDifMun`, `vDifCBS` (diferimento) | `vIBSUF × pDifUF`; `vIBSMun × pDifMun`; `vCBS × pDifCBS` |
| `gIBSCredPres/vCredPresIBS`; `gCBSCredPres/vCredPresCBS` | `vBC × pCredPresIBS`; `vBC × pCredPresCBS` |
| `gTribRegular` (`vTribRegIBSUF`, `vTribRegIBSMun`, `vTribRegCBS`) | `vBC ×` a alíquota efetiva de tributação regular de cada um |
| `gTribCompraGov` | composição do IBS (UF e município) e da CBS em compras governamentais: alíquota e valor de cada um |
| **`vTotNF`** | **2026:** `vTotNF = vLiq`. **A partir de 2027:** `vTotNF = vLiq + vCBS + vIBSTot` — o IBS e a CBS são **"por fora"**, então seus valores são **somados** ao valor total da nota |

Todos os valores têm 15 inteiros e 2 decimais (`1-15V2`); as alíquotas, `1-2V2`.

### Base de cálculo do IBS/CBS (`vBC`)

| Período | Fórmula | NT |
|---|---|---|
| Até 2026 | `vBC = vServ − descIncond − vCalcReeRepRes − vISSQN − vPIS − vCOFINS` | NT 004 v2.00 |
| Até 2032 | `vBC = vServ − descIncond − vCalcReeRepRes − vISSQN` | NT 004 v2.00 |
| Até 2026 | `vBC = vServ − descIncond − (vCalcAjusteBCIBSCBS ou vCalcAjusteBCLocImoveis) − vISSQN − vPIS − vCOFINS` | NT 009 v1.0 |
| De 2027 até 2032 | `vBC = vServ − descIncond − (vCalcAjusteBCIBSCBS ou vCalcAjusteBCLocImoveis) − vISSQN` | NT 009 v1.0 |

Em palavras: parte-se do valor do serviço, tiram-se o desconto incondicional, os ajustes
(reembolsos e afins) e os **valores dos tributos que a lei manda excluir da base** (o ISSQN e,
até 2026, o PIS e a COFINS). Os campos `vPIS` e `vCOFINS` são o **débito de apuração própria**:
a NT 007 explica que muitos contribuintes lançavam ali o valor **retido**, o que reduzia
indevidamente a base do IBS/CBS, "de acordo com o inciso V do § 2º do art. 12 da LC 214/2025",
cujo texto está em [[ibs-cbs-base-calculo]]. A NT 009 renomeia `vCalcReeRepRes` para
`vCalcAjusteBCIBSCBS`. Não há, nas fontes, a regra legal que fixa o prazo "até 2026" e "até
2032" dos períodos acima: são as datas **da NT**.

## NT 007 v1.0 (07/02/2026): PIS/COFINS, ZFM e novos códigos

- **`indZFMALC`** (0-1, grupo `IBSCBS` da DPS): indica o enquadramento nos **arts. 451 e 466 da
  LC 214/2025**, em que a alíquota da **CBS é reduzida a zero**: 0 não; 1 sim.
- **PIS/COFINS** (`valores/trib/tribFed/piscofins`): nova lista de **CST** (00, 01 a 09, 49, 50 a
  56, 60 a 67, 70 a 75, 98 e 99, a tabela de CST do PIS/COFINS) e novo domínio de
  **`tpRetPisCofins`**: 0 PIS/COFINS/CSLL não retidos; 1 PIS/COFINS retido; 2 PIS/COFINS não
  retido; 3 PIS/COFINS/CSLL retidos; 4 PIS/COFINS retidos, CSLL não; 5 PIS retido, COFINS/CSLL
  não; 6 COFINS retido, PIS/CSLL não; 7 PIS não retido, COFINS/CSLL retidos; 8 PIS/COFINS não
  retidos, CSLL retido; 9 COFINS não retido, PIS/CSLL retidos. Os valores **1 e 2** serão
  suprimidos do schema quando o grupo `IBSCBS` se tornar obrigatório.
- **Retenções:** PIS, COFINS e CSLL retidos são **somados** em `vRetCSLL`, conforme o
  `tpRetPisCofins`; `vPis` e `vCofins` **não** servem para valores retidos. A soma não muda
  a forma de prestar a informação na EFD-Reinf.
- **Arredondamento:** `vPIS` e `vCofins` usam arredondamento bancário (*half-even*), com
  tolerância de **R$ 0,01**. As atualizações de PIS/COFINS ficaram disponíveis em Produção e
  Produção Restrita em **09/02/2026**, segundo a NT. A legislação de PIS/COFINS em si **não
  está nas fontes**: a nota trata só do campo.
- **Novos fatos geradores** (operações no campo do IBS/CBS que antes não eram documentadas
  por nota fiscal): códigos de tributação nacional **99.02.01** (operações com bens imateriais
  não classificados em itens anteriores), **99.03.01** (locação de bens imóveis), **99.03.02**
  (cessão onerosa), **99.03.03** (arrendamento), **99.03.04** (servidão, cessão de uso ou de
  espaço, quando não for ISSQN), **99.03.05** (permissão de uso ou direito de passagem, quando
  não for ISSQN) e **99.04.01** (locação de bens móveis). O **99.01.01** fica para a operação
  que incida IBS/CBS mas não ISSQN e não se enquadre nesses códigos. Esses documentos são
  autorizados **só nos emissores nacionais** (Sefin Nacional): os autorizados em sistema
  próprio do município são **rejeitados** no compartilhamento com o ADN; todo CPF e CNPJ
  pode usar o emissor nacional para eles, mesmo que o município não o use. A NT diz que as
  evoluções do layout para isso ainda não estavam disponíveis e o cronograma seria publicado.
- **Número da NFS-e** (`nNFSe`): atribuído **só pela Sefin Nacional**; podem surgir **"pulos"**
  na sequência (número reservado e não persistido: timeouts, falhas, concorrência), e a NT diz
  que isso **não é irregularidade** do contribuinte.

## NT 009 v1.0 (04/06/2026): consolidação das evoluções

| Mudança | Detalhe |
|---|---|
| **CNPJ alfanumérico** | todos os campos CNPJ passam de numérico para caractere, para o formato a vigorar a partir de julho de 2026 |
| **Notas de ajuste de IBS/CBS** | `finNFSe`: 0 regular; **1 crédito**; **2 débito**. Novos `tpNFSeDebito` (01 transferência de créditos para cooperativas; 02 anulação de crédito por saídas imunes/isentas; 03 débitos de notas não processadas na apuração; 04 multa e juros; 05 transferência de crédito na sucessão; 06 pagamento antecipado) e `tpNFSeCredito` (01 multa e juros; 05 transferência de crédito na sucessão). Novo grupo `gIBSCBSAjuste` (`vIBS` e `vCBS` a ajustar). As regras dessas notas ainda estão **em evolução** |
| **Unificação dos ajustes de base** | `vDedRed` e `gReeRepRes` viram **`vAjusteBC`**: `pAjusteBCISSQN`, `vAjusteBCISSQN` e `documentos/docAjusteBC` (até 1000), com `tpAjusteBC`: 2 materiais; 5 repasse consorciado; 6 repasse plano de saúde; 7 serviços; 8 subempreitada de mão de obra; 9 profissional parceiro; 99 outras deduções exclusivas do ISSQN; 101 repasse de remuneração por intermediação de imóveis; 102 repasse a fornecedor de agência de turismo; 103 produção externa; 104 mídia; 105 glosa de serviços de saúde; 199 outros reembolsos ou ressarcimentos. Também: `vTotDoc` e `vAjuteAplic` (este, menor ou igual ao total do documento). Foram **descontinuados** os tipos antigos "1 alimentação e bebidas/frigobar" (hotéis e motéis: a inclusão afetaria o cálculo do IBS/CBS dos alimentos já registrados em outros documentos), "3 produção externa" e "4 reembolso de despesas" (substituídos por 103, 104 e 199). Reembolso não previsto, com autorização municipal e só para o ISSQN: tipo 99 |
| **Renomeações na NFS-e** | `vCalcDR` → `vCalcAjusteBCISSQN`; `vCalcReeRepRes` → `vCalcAjusteBCIBSCBS`; `vCalcDedRedIBSCBS` → `vCalcAjusteBCLocImoveis` (só locação, cessão onerosa ou arrendamento de imóveis, subitem 99.03). Base do ISSQN: `vBC = vServ − descIncond − (vAjusteBCISSQN + vCalcAjusteBCISSQN) − (vRedBCBM ou VCalcBM)` |
| **Simples Nacional** | `opSimpNac` ganha **4 — optante pendente**. Novo `regApIBSCBSSN`: **1** IBS e CBS apurados pelo SN; **2** CBS apurada pelo SN e IBS pelo regime regular; **3** IBS e CBS pelo regime regular. Novo `cAtvSN` (códigos 7 a 14 e 90: 7 serviços do Anexo III; 8 serviços contábeis com ISS fixo, Anexo III; 9 sujeitos ao fator R, Anexo III ou V; 10 transporte municipal de passageiros, Anexo III; 11 locação de bens móveis e operações sem ISS, Anexo III; 12 construção civil (7.02 e 7.05), Anexo III; 13 a mesma, Anexo IV; 14 serviços, Anexo IV; 90 operações não tributadas). Na NFS-e: `vReceitaBrutaSN = vServ − descIncond − vCalcAjusteBCIBSCBS − vCalcAjusteBCISSQN*` (*só quando vier de documentos com tipo 9, profissional parceiro) e o grupo `gTribSN` (`pIBSSN`, `vIBSSN`, `pCBSSN`, `vCBSSN`). Por isso `vIBSTot`, `gIBSUFTot`, `gIBSMunTot`, `pCredPresCBS`, `vCredPresCBS` e `vCBS` deixaram de ser obrigatórios |
| **Reinserção de `indFinal`** | uso ou consumo pessoal, **art. 57 da LC 214/2025** |
| **Bens imóveis** | no `imovel`: novo `cMun`, grupo **`gLocacao`** (`pCopropriedade`, `vTotOper`, `vDescIncondTot`, `vDescCondTot`, `dVencOrig`) e **`gUnidImob`** (até 99 unidades; mesmos atores, mesmo município e mesmo percentual de copropriedade) com `gAjusteBCLocImoveis` (até 1000): tipos 01 tributos inclusos (IPTU, contribuição de melhoria), 02 emolumento, 03 condomínio (esses três só para as NBS 1.1002.10.00 ou 1.1002.20.00), 04 redutor social (só 1.1002.10.00) e 99 outras. Nos códigos do subitem **99.03**: `vServ = pCopropriedade × vTotOper`, `vDescIncond = pCopropriedade × vDescIncondTot` e `vDescCond = pCopropriedade × vDescCondTot`. O valor total é o da operação "conforme art. 255 da LC 214/2025" (citado pela NT) |
| **Bens móveis** | `gLocBensMoveis` (NT 005) vira **`bensMoveis`**, agora com até **1000** registros |
| **Pagamento vinculado** | novo `gPgtoVinc` (até 99 `pgto`): `nPag`, `idTransacao`, `tpMeioPgto` (15 boleto; 17 Pix QR Code dinâmico; 18 TED; 20 Pix chave ou QR Code estático; 23 Pix automático; 24 TEF/*booktransfer*), `CNPJReceb` e `CNPJBasePSP`. Quando o pagamento só puder ser informado após a emissão, haverá um **evento** com a mesma estrutura |

## O que a NT 005 v1.0 (19/11/2025) acrescentou e a NT 009 manteve ou renomeou

`indDoacao` (operação de doação, ligada ao `gEstornoCred` e ao cClassTrib), `gEstornoCred`
(`vIBSEstCred` e `vCBSEstCred`, valores a estornar), `gPagAntecipado` (chaves de NFS-e de
pagamento antecipado para abatimento), `gLocBensMoveis` (locação de bens móveis: descrição,
código NCM e quantidade, só com o código 99.04.01), o grupo de deduções de locação
(`gDedRedIBSCBS`, depois `gAjusteBCLocImoveis`) e o `pRedutor` obrigatório na NFS-e. A NT 005
**não** foi implantada em produção em janeiro de 2026 (aviso da NT 004 v2.00).

## ⏳ Sem data nas fontes — NT 005 v1.0 e NT 009 v1.0 (cronograma não publicado nas fontes)

Os campos e grupos acima que vêm só das NTs 005 e 009 (`indDoacao`, `gEstornoCred`,
`gPagAntecipado`, `vAjusteBC`, `gIBSCBSAjuste`, `gLocacao`, `gUnidImob`, `bensMoveis`,
`gPgtoVinc`, `regApIBSCBSSN`, `cAtvSN`, `gTribSN`, o CNPJ alfanumérico etc.) **não têm data de
produção nas fontes**. As NTs 007 e 009 apenas dizem que o cronograma "será publicado no portal
da NFS-e". Antes de afirmar que um desses campos **já vale**, consulte o cronograma e o Anexo I
vigente (que não estão nas fontes).
