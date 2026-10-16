---
título: NFS-e Nacional — regras de rejeição do IBS/CBS (Anexo I v1.01 em produção e Anexo VI v1.04.01 da NT 009): quando o grupo é exigido, tomador, imóvel, bens móveis, calculadora e conferência dos valores
dominio: documentos-fiscais
fontes: Anexo I v1.01-20260209 (regras de negócio da DPS e da NFS-e em produção); Anexo VI v1.04.01 (regras da NT CGNFS-e 009 v1.01, 478 regras); NT CGNFS-e 009 v1.01 (11/09/2026); NT CGNFS-e 004 v2.00 (10/12/2025); Anexo VII v1.03.00
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Regras de rejeição do grupo IBS/CBS na NFS-e Nacional

## A lógica em uma frase

Os Anexos I e VI trazem uma tabela de **regras de negócio**: cada linha tem um código de erro
(`E` + 4 dígitos), a condição, se a regra é obrigatória, se a consequência é **rejeição** e a
mensagem. Para o grupo `IBSCBS`, o sistema **consulta a Calculadora de IBS/CBS** (com a data de
competência e o `cClassTrib`) e **confere se os valores da NFS-e batem com o que ela devolveu**;
no Anexo VI, o resultado da calculadora também passa a **exigir ou proibir** grupos da DPS. O que
cada campo significa está em [[df-nfse-layout-ibscbs]]; a regra tributária de fundo vem da
LC 214/2025 ([[ibs-cbs-base-calculo]], [[ibs-cbs-aliquotas]]). **Nível de NT:** a regra de
rejeição diz como validar o documento; não cria nem altera tributo.

## Que arquivo vale (Anexo I × Anexo VI)

- **Anexo I v1.01-20260209:** regras do layout **em produção** (NT 004 v2.00).
- **Anexo VI v1.04.01:** regras do layout da **NT 009 v1.01**, com 478 regras (80 a mais que o
  Anexo I v1.01). Ao entrar em produção passará a ser o `ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe`.
  **A data não está nas fontes**: não afirme que uma regra só do Anexo VI já está valendo.
- A coluna **Arquivo** das tabelas abaixo diz onde o **código de erro** existe (conferido nos dois
  arquivos): "I e VI" ou "só VI". Quando o código existe nos dois, o texto pode ter mudado; os casos
  que mudam de conteúdo estão descritos nas seções 3 e 6.

## 1. Quando informar o grupo IBSCBS e o papel da calculadora

| Regra | Arquivo | O que diz |
|---|---|---|
| E0850 | I e VI | só é permitido declarar IBS/CBS a partir da **data de competência 01/01/2026** (rejeita) |
| E0854 | I e VI | só é permitido declarar IBS/CBS a partir da **versão 1.01 da DPS** |
| E0855 | só VI | é **obrigatório** declarar IBS/CBS quando a data de competência for **igual ou posterior a 01/10/2026**. Depende da entrada do Anexo VI em produção (sem data nas fontes); a NT 004 v2.00 (seção 1.1) diz que a exigência estava desligada no início de 2026 ([[df-nfse-layout-ibscbs]]) |
| E1515 | I e VI | se o grupo `IBSCBS` da DPS for informado, o da NFS-e **deve** ser informado (a plataforma o calcula) |
| E1517 | I e VI | se o grupo da DPS não for informado, o da NFS-e **não** pode ser informado |
| E0322 | I e VI | se qualquer informação de IBS/CBS for declarada, a **NBS é obrigatória** |
| E0901 | I e VI | o `cIndOp` tem que constar na tabela do Anexo VII ([[df-nfse-indop-ibscbs]]) |
| E1521 | I e VI | `cLocalidadeIncid` tem que estar de acordo com o `cIndOp` (tabela de indicadores); para endereço no exterior, é `999999` |
| E0958 | I e VI | `cClassTrib` não suportado para prestação de serviços (a calculadora responde `validoParaSiglaDfeInformado = false`) |
| E0959 | I e VI | os 3 primeiros dígitos do `cClassTrib` têm que ser iguais ao CST informado |
| E0859 / E0860 | só VI | `cIndOp` **não** pode ser informado quando a calculadora indica que não há tributação (`ind_gIBSCBS = 0`) e **é obrigatório** quando indica tributação (`= 1`); informar data de competência e `cClassTrib` para consultar |
| E0960 / E0961 | só VI | com `ind_gIBSCBS = 1`, as informações de tributação (`gIBSCBS`) são obrigatórias; com `= 0`, não são permitidas |
| E0962 | só VI | `cCredPres` informado não é suportado para aquele `cClassTrib` |
| E0964 / E0965 | I e VI | o grupo de **tributação regular** (`gTribRegular`) é proibido se a calculadora disser `exigeGrupoTributacaoRegular = false` e obrigatório se `true` |
| E0971 / E0972 | I e VI | o grupo de **diferimento** (`gDif`) é proibido se `permiteDiferimento = false` e obrigatório se `true` |
| E1518, E1524, E1526, E1562, E1573 | só VI | sem tributação (`ind_gIBSCBS = 0`), a NFS-e **não** pode trazer `cLocalidadeIncid`, o grupo `valores`, `vBC`, `gIBS` nem `gCBS` |
| E1525, E1563, E1574 | só VI | com tributação (`= 1`), os campos de `valores`, `gIBS` e `gCBS` são obrigatórios conforme a ocorrência no leiaute |
| E0903 / E0904 | I e VI | `tpOper` deve ser informado quando houver `tpEnteGov` (compra governamental) ou quando o `cTribNac` corresponder aos subitens **25.05, 15.09, 17.12 e 10.05** da LC 116; fora disso não pode ser informado |
| E0905 / E0906 / E0907 | I e VI | `gRefNFSe` é obrigatório quando `tpOper` = 2 ou 3 e proibido quando `tpOper` não existe ou é 1, 4 ou 5; a chave referenciada tem que ser válida (confere o dígito verificador) |
| E0309 | só VI | `cTribNac` **99.03.xx ou 99.04.01** → a NFS-e é **rejeitada** no compartilhamento: o sistema NFS-e não aceita compartilhar NFS-e com novos fatos geradores de IBS/CBS desses códigos |

Sobre a calculadora, as fontes só dizem que o sistema consulta o serviço e usa o resultado; o
cálculo em si (alíquotas, reduções) vem da lei e dos regulamentos. Erro devolvido pela calculadora
aparece como `E1000`, com a mensagem dela.

## 2. Tomador e destinatário (só VI): quando CNPJ/CPF e endereço nacional são obrigatórios

Três regras do Anexo VI, com as mesmas condições de partida: o emitente é o prestador (`tpEmit = 1`),
a calculadora diz que a tributação é obrigatória (`ind_IBSCBS = 1`) e o `cIndOp` indica que o **local
do fornecimento (município de incidência) é o município do endereço do tomador/adquirente**. Então:

- **E0239:** o tomador/adquirente tem que ser identificado por **CNPJ ou CPF** e ter **endereço
  nacional**;
- **E0243:** o mesmo, quando o destinatário é o próprio adquirente (`indDest = 0`);
- **E0919:** o mesmo para o **destinatário**, quando ele **não** é o adquirente (`indDest = 1`):
  `dest` com CNPJ/CPF e endereço nacional (`endNac`).

Efeito prático: nas operações em que o `cIndOp` põe a incidência no município do tomador
([[df-nfse-indop-ibscbs]]), não dá para emitir com tomador sem documento ou com endereço no exterior.
**Qual `cIndOp` vale para o serviço** continua dependendo dos fatos ([[df-nfse-correlacao-nbs-indop]]).
As telas de tomador estão em [[df-nfse-emissao-pessoas]].

No Anexo I v1.01 o destinatário (`dest`) só é identificado quando `indDest = 1` (E0910) e o CNPJ/CPF
é validado contra o cadastro (E0911 a E0914); a obrigatoriedade condicionada à calculadora acima é nova.

## 3. Imóveis, locação e obra

| Regra | Arquivo | O que diz |
|---|---|---|
| E0931 | I e VI | se o `cTribNac` for dos subitens 07.02.01, 07.02.02, 07.04.01, 07.05.01, 07.05.02, 07.06.01, 07.06.02, 07.07.01, 07.08.01, 07.17.01 ou 07.19.01, o grupo `imovel` **não** é permitido (nesses casos o grupo é o de **obra**) |
| E0932 | I e VI | fora desses subitens, se o `cIndOp` for de operação com imóveis, o grupo `imovel` é **obrigatório**. **Anexo I v1.01:** `cIndOp` 020101, 020201 ou 020301. **Anexo VI:** 020101, 020201, 020202, 020301 ou 020401 |
| E0928 | I e VI | fora desses subitens, se o `cIndOp` **não** for dos códigos acima (conjunto de cada anexo), o grupo `imovel` **não** é permitido |
| E0372 | I e VI | grupo de **obra** permitido só para os subitens listados na regra (07.02.01, 07.02.02, 07.04.01, 07.05.01, 07.05.02, 07.06.01, 07.06.02, 07.07.01, 07.08.01, 07.17.01, 07.19.01, **14.14.03 e 14.14.04**: 13 códigos) e para 99.01.01 |
| E0929 | só VI | o `cMun` do endereço do imóvel tem que existir na tabela do IBGE ([[df-nfse-codigos-ibge-localidades]]) |
| E0938 | só VI | se o `cIndOp` for **020101, 020201 ou 020301**, o grupo de **unidade imobiliária** (`gUnidImob`) é obrigatório |
| E0936 | só VI | o grupo `gLocacao` só pode ser informado se o `cTribNac` for **99.03** |
| E0939 | só VI | o grupo de ajuste da base (`gAjusteBCLocImoveis`) só pode ser informado com `cTribNac` 99.03 |
| E0944 | só VI | o **redutor social** (`tpAjusteBCLocImoveis = 04`) só pode ser usado em locação de **imóvel residencial** (NBS `1.1002.10.00`) |
| E0949 | só VI | se o tipo de ajuste for `99`, a descrição (`xTpAjusteBCLocImoveis`) é obrigatória |
| E0966 | só VI | o valor do ajuste tem que ser menor ou igual ao valor total da operação com o imóvel (`vTotOper`) |
| E1537, E1559, E1564, E1579 | só VI | o valor calculado do ajuste (`vCalcAjusteBCLocImoveis`) só é informado se o grupo de ajuste veio na DPS (e é obrigatório se veio), tem que ser menor ou igual ao valor do serviço (`vServ = pCopropriedade × vTotOper`) e igual à soma dos ajustes informados × o percentual de copropriedade |

Os ajustes e o redutor social operacionalizam a LC 214 para locação de imóveis; a regra de fundo
está em [[regime-especifico-bens-imoveis]]. O grupo de obra e a lista de códigos estão também em
[[df-nfse-lista-servicos-ctribnac]].

## 4. Bens móveis (99.04.01), só VI

- **E0967:** o grupo `bensMoveis` só pode ser informado se o `cTribNac` for **99.04.01**.
- **E0973:** o `cNCMBemMovel` tem que existir (código NCM do bem móvel).
- **E0974:** a quantidade (`qtdNCMBemMovel`) tem que ser maior que zero.
- E0309 (seção 1): o `cTribNac` 99.04.01 não é aceito no compartilhamento via ADN.

## 5. Ajuste da base de cálculo (reembolso, repasse, ressarcimento e documentos)

- **Anexo I v1.01** trata o assunto no grupo de **reembolso, repasse e ressarcimento**
  (`gReeRepRes`; valor calculado `vCalcReeRepRes`, regras E0940 a E0953 e E1531 a E1535).
- **Anexo VI** renomeia o conceito para ajuste da base (`vAjusteBC`, `vCalcAjusteBCIBSCBS`;
  [[df-nfse-layout-ibscbs]]). Regras só do Anexo VI:
  - **E0437:** o grupo de ajuste por **documentos** não é permitido quando a calculadora indica que
    não há tributação (`ind_IBSCBS = 0`), **exceto** quando, ao mesmo tempo: a operação é tributável
    pelo ISSQN (`tribISSQN = 1`), o prestador não tem regime especial (`regEspTrib = 0`), o prestador
    não é MEI (`opSimpNac` = 1 ou 3) e não há suspensão da exigibilidade do ISSQN (`tpSusp` nulo). O
    ISSQN em si é matéria municipal, fora do escopo.
  - **E1529:** não é permitido informar o valor de reembolso, repasse ou ressarcimento já tributado
    que não integra a base do ISSQN, do IBS e da CBS (`vCalcAjusteBCIBSCBS`) nos campos
    `vAjusteBCISSQN` ou a partir de `pAjusteBCISSQN`.

## 6. Conferência dos valores da NFS-e (a plataforma recalcula)

A NFS-e traz o resultado, e as regras de rejeição exigem que os valores **batam com a calculadora**
(E1539 a E1590, E1602 a E1607 nos dois anexos). As fórmulas de `vBC` e `vTotNF` mudam do Anexo I
v1.01 para o Anexo VI.

**Base de cálculo do IBS/CBS (`vBC`, regra E1530):**

| Arquivo | `cTribNac` | Período | Fórmula |
|---|---|---|---|
| Anexo I v1.01 (produção) | todos | 2026 | `vBC = vServ − descIncond − vCalcReeRepRes − vISSQN − vPIS − vCOFINS` |
| Anexo I v1.01 (produção) | todos | 2027 a 2032 | `vBC = vServ − descIncond − vCalcReeRepRes − vISSQN` |
| Anexo VI | 99.03.xx | 2026 | `vBC = vServ − descIncond − vCalcAjusteBCLocImoveis − vISSQN − vPIS − vCOFINS` |
| Anexo VI | 99.03.xx | 2027 a 2032 | `vBC = vServ − descIncond − vCalcAjusteBCLocImoveis − vISSQN` |
| Anexo VI | demais | 2026 | `vBC = vServ − descIncond − vCalcAjusteBCIBSCBS − vISSQN + vAjusteBCIBSCBSComExt − vPIS − vCOFINS` |
| Anexo VI | demais | 2027 a 2032 | `vBC = vServ − descIncond − vCalcAjusteBCIBSCBS − vISSQN + vAjusteBCIBSCBSComExt` |

("2026" = de 01/01/2026 a 31/12/2026; "2027 a 2032" = de 01/01/2027 a 31/12/2032, como diz a regra.)
O `vAjusteBCIBSCBSComExt` é o ajuste de comércio exterior da NT 009 v1.01
([[df-nfse-comercio-exterior]]). As fórmulas descrevem a **conferência** do sistema; não substituem
a base de cálculo da lei ([[ibs-cbs-base-calculo]]).

**Valor total da NFS-e (`vTotNF`, regra E1555):**

| Arquivo | Situação do emitente | Fórmula |
|---|---|---|
| Anexo I v1.01 | qualquer | 2026: `vTotNF = vLiq`; a partir de 2027: `vTotNF = vLiq + vCBS + vIBSTot` |
| Anexo VI | `opSimpNac` = 1 (não optante) ou 4 (pendente); ou `opSimpNac` = 3 (ME/EPP) e `regApIBSCBSSN` = 3 (CBS/IBS pelo regime regular) | 2026: `vTotNF = vLiq`; a partir de 2027: `vTotNF = vLiq + vCBS + vIBSTot` |
| Anexo VI | `opSimpNac` = 3 e `regApIBSCBSSN` = 1 (CBS/IBS pelo Simples Nacional) | `vTotNF = vLiq` (em 2026 e a partir de 2027) |
| Anexo VI | `opSimpNac` = 3 e `regApIBSCBSSN` = 2 (CBS pelo SN e IBS pelo regime regular) | 2026: `vTotNF = vLiq`; a partir de 2027: `vTotNF = vLiq + vIBSTot` |

(`opSimpNac` = 4 e `regApIBSCBSSN` só existem no Anexo VI.)

**Outras conferências:** se a DPS informou a alíquota de diferimento do IBS municipal (`pDifMun`), o
valor do diferimento tem que ser informado (E1591, só VI). Compras governamentais: E1600 proíbe o grupo
`gTribCompraGov` se a DPS não trouxe `tpEnteGov`, e E1601 o exige quando trouxe; E1602 a E1607 exigem que
alíquotas e valores de IBS estadual, IBS municipal e CBS sejam iguais aos que a calculadora devolveu.

## O que não está nas fontes

- A **data** em que o Anexo VI passa a valer em produção (e, portanto, a vigência de E0855, E0239,
  E0243, E0919 e das demais "só VI").
- O **comportamento da calculadora** além do que as regras citam (alíquotas, reduções, tabelas): isso
  vem da lei e dos regulamentos.
- Se o Anexo VIII (correlação de itens) gera rejeição: as regras acima ligam `cClassTrib` e `cIndOp` à
  calculadora, e não à planilha ([[df-nfse-correlacao-nbs-indop]]).
