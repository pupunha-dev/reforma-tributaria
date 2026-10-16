---
título: NFS-e Nacional — comércio exterior na DPS (grupo comExt, NIF, códigos, os 112 cenários de validação e as mudanças da NT 009 v1.01)
dominio: documentos-fiscais
fontes: Anexo I v1.01-20260209 (leiaute da DPS/NFS-e, regras de negócio e planilha EXPORTACAO_EMISSÃO_NFS-e; layout em produção); Anexo VI v1.04.01 (layout da NT 009 v1.01, mesma planilha de cenários); NT CGNFS-e 009 v1.01 (11/09/2026, seção 2.12 e 2.13; v1.0 de 04/06/2026 trouxe CNPJ alfanumérico e NIF/cNaoNIF); NT CGNFS-e 004 v2.00 (10/12/2025); Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seção 4.1.2
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Comércio exterior na NFS-e Nacional: o grupo `comExt`

## A lógica em uma frase

Quando **qualquer um dos três pontos** da operação está no exterior (tomador,
intermediário ou local da prestação), a DPS passa a **exigir** o grupo de comércio
exterior (`comExt`), o item da **NBS** e, em alguns cenários, o **país do resultado** do
serviço. As regras são do **Anexo I v1.01-20260209** (layout em produção; nível de
documentação técnica: a NT não cria tributo). A **NT 009 v1.01** (Anexo VI) muda alguns campos
do grupo e **não tem data de produção nas fontes**: ver a seção ⏳ mais abaixo. A tela do emissor está em [[df-nfse-emissao-servico]] e a identificação do
tomador no exterior (NIF) em [[df-nfse-emissao-pessoas]].

> **Escopo.** O que o ISSQN faz (onde incide, alíquota, benefício) é matéria municipal e
> **fora do escopo**. Esta nota descreve só o que o **documento** exige e rejeita. A
> planilha também indica, em cada cenário, o "local de incidência" do ISSQN (município
> do estabelecimento do prestador, do tomador ou do local da prestação): a nota **não**
> explica por que, porque a regra é da LC 116/2003, que não está nas fontes. A
> exportação para **IBS/CBS** segue a lei: [[ibs-cbs-exportacao]] (LC 214, art. 80). A
> planilha define "comércio exterior **para emissão de NFS-e**" e não cita a LC 214.

## Quando o grupo é obrigatório (regras E0330 e E0331)

| Quem emite a DPS (`tpEmit`) | Gatilho (basta um) | Consequência | Rejeição |
|---|---|---|---|
| 1 — prestador (**exportação** de serviço) | país no exterior no endereço do **tomador**; país no exterior no endereço do **intermediário**; `cPaisPrestacao` informado; ou `tribISSQN` = 3 (exportação de serviço) | grupo `comExt` **obrigatório** | **E0330** — "É obrigatório prestar informações de comércio exterior para as situações de exportação de serviços." |
| 2 — tomador ou 3 — intermediário (**importação** de serviço) | país no exterior no endereço do **prestador**; ou `cPaisPrestacao` informado | grupo `comExt` **obrigatório** | **E0331** — "...para as situações de importação de serviços." |

Em ambos os casos o **item da NBS** também é obrigatório: **E0318** (exportação) e
**E0320** (importação) rejeitam a DPS sem NBS.

- `cPaisPrestacao` é a alternativa de `cLocPrestacao` no grupo `locPrest`: informa-se
  o município (IBGE) **ou** o país da prestação. O país tem de existir na tabela de
  países (ISO2) e ser **diferente de Brasil** (**E0304**).
- Conclusão prática: **tomador ou intermediário no exterior já exige o `comExt`**, mesmo
  com o serviço prestado no Brasil. O guia da NFS-e diz o mesmo
  ([[df-nfse-emissao-servico]]); a regra E0330 é a que fixa o gatilho.
- Quando nenhum dos três está no exterior e o emitente **não** declara exportação, o
  grupo **não é permitido** (cenários 1, 4, 5, 8, 9, 12, 13 e 14 da planilha).
- Onde as regras rodam (colunas de aplicabilidade do Anexo I): E0318, E0320, E0330,
  E0331, E0529, E0530 e E0590 são executadas **tanto** na recepção da DPS pelos emissores
  públicos nacionais **quanto** na recepção de NFS-e compartilhadas pelos municípios com
  o ADN; **não** são executadas nas NFS-e emitidas por decisão judicial ou
  administrativa (`cStat` = 102). Já as regras do valor 0 e de `nDI`/`nRE` (E0333, E0341,
  E0343, E0345, E0352, E0354 e E0356) rodam **só nos emissores nacionais**, não no
  compartilhamento do município (por isso o valor 0 passa no ADN).

## Campos do grupo `comExt` (caminho `DPS/infDPS/serv/comExt`)

O grupo tem ocorrência 0-1. Todos os campos abaixo são obrigatórios dentro dele,
exceto `nDI` e `nRE`.

| Campo | O que informa | Códigos (valor — significado) |
|---|---|---|
| `mdPrestacao` | modo de prestação | 0 desconhecido; **1 transfronteiriço**; **2 consumo no Brasil**; **3 movimento temporário de pessoas físicas**; **4 consumo no exterior** |
| `vincPrest` | vínculo entre as partes | 0 sem vínculo com o tomador/prestador; 1 controlada; 2 controladora; 3 coligada; 4 matriz; 5 filial ou sucursal; 6 outro vínculo; **9 desconhecido** (tipo não informado na nota de origem) |
| `tpMoeda` | moeda da transação | código da tabela de moedas do Banco Central (3 posições) |
| `vServMoeda` | valor do serviço **em moeda estrangeira** | até 15 inteiros e 2 decimais |
| `mecAFComexP` | mecanismo de apoio/fomento ao comércio exterior **do prestador** | 00 desconhecido; 01 nenhum; 02 ACC; 03 ACE; 04 BNDES-Exim pós-embarque (serviços); 05 BNDES-Exim pré-embarque (serviços); 06 FGE; 07 PROEX equalização; 08 PROEX financiamento |
| `mecAFComexT` | mecanismo de apoio/fomento **do tomador** | 00 desconhecido; 01 nenhum; 02 administração pública e representação internacional; 03 aluguéis e arrendamento mercantil de máquinas, equipamentos, embarcações e aeronaves; 04 arrendamento mercantil de aeronave para empresa de transporte aéreo público; 05 comissão a agentes externos na exportação; 06 despesas de armazenagem, movimentação e transporte de carga no exterior; 07 eventos FIFA (subsidiária); 08 eventos FIFA; 09 fretes, arrendamentos de embarcações ou aeronaves e outros; 10 material aeronáutico; 11 promoção de bens no exterior; 12 promoção de destinos turísticos brasileiros; 13 promoção do Brasil no exterior; 14 promoção de serviços no exterior; 15 RECINE; 16 RECOPA; 17 registro e manutenção de marcas, patentes e cultivares; 18 REICOMP; 19 REIDI; 20 REPENEC; 21 REPES; 22 RETAERO; 23 RETID; 24 royalties, assistência técnica, científica e assemelhados; 25 serviços de avaliação da conformidade vinculados aos acordos da OMC; 26 ZPE |
| `movTempBens` | vínculo da operação a movimentação temporária de bens | 0 desconhecido; **1 não**; **2 vinculada a Declaração de Importação**; **3 vinculada a Declaração de Exportação** |
| `nDI` | número da DI/DSI/DA/DRI-E averbada | 1 a 12 posições; opcional |
| `nRE` | número do Registro de Exportação averbado | 12 posições; opcional |
| `mdic` | a NFS-e deve ser disponibilizada ao MDIC? | 0 não enviar; 1 enviar |

Observações do próprio leiaute:

- `vincPrest`: o texto de ajuda deve dizer que a parte é "considerada vinculada" **nos
  termos do art. 23 da Lei 9.430/1996** (essa lei não está nas fontes: a nota só
  registra a referência).
- ⚠️ **Quem preenche `mecAFComexP` e `mecAFComexT`: o Anexo I e o guia não dizem a mesma
  coisa.** O Anexo I v1.01 (e também o Anexo VI) descreve `mecAFComexP` como "campo disponível na
  nota do prestador" (e `mecAFComexT`, na nota do tomador), mas os dois estão **dentro do
  `comExt` com ocorrência 1-1**, e o **valor 0 é rejeitado** (E0341 e E0343). O **guia do
  emissor** (seção 4.1.2, v1.2) mostra **os dois** como **obrigatórios** na tela de quem emite
  a NFS-e. Na prática, quem emite como prestador e vê o campo do tomador na tela precisa
  escolher uma opção (a lista tem "01 Nenhum"). A divergência **permanece nas versões mais
  novas dos anexos**: as fontes **não explicam** como o texto do anexo e a tela se conciliam.
  **Qual** mecanismo o tomador usa é fato da operação, que nenhuma fonte escolhe.
- **Vínculo (`vincPrest`): guia e Anexo I conferem.** O guia lista "sem vínculo, controlada,
  controladora, coligada, matriz, outro vínculo e desconhecido" (sem "filial"); o Anexo I v1.01
  tem as mesmas opções **mais "5 filial ou sucursal"** e identifica o "desconhecido" como o
  código **9**. (Uma cópia anterior do Anexo I, de 09/09/2025, não tinha o 9; está arquivada e
  foi superada.) O guia não é a lista completa: vale o anexo.
- O **valor 0** ("desconhecido") de `mdPrestacao`, `mecAFComexP`, `mecAFComexT` e
  `movTempBens` existe **só para o compartilhamento** de NFS-e pelo município com o ADN
  (nota de origem sem a informação). Na Sefin Nacional a DPS com valor 0 é
  **rejeitada** (E0333, E0341, E0343 e E0345, respectivamente).

### Regras de `nDI` e `nRE` (rejeitam a DPS)

| Se `movTempBens` for | Então | Rejeição |
|---|---|---|
| 2 (Declaração de Importação) | `nDI` é **obrigatório** | E0352 |
| 3 (Declaração de Exportação) | `nRE` é **obrigatório** | E0356 |
| 1 (não) | `nDI` e `nRE` **não são permitidos** | E0354 |

## País do resultado do serviço (`cPaisResult`)

Fica em `valores/trib/tribMun` (0-1). A regra **E0590** o torna obrigatório nos
cenários **2, 30, 58, 62, 72 e 76** da planilha: o emitente declara **exportação de
serviço** (`tribISSQN` = 3), o local da prestação é no **Brasil** e a incidência é no
estabelecimento do prestador (ou no do tomador, com o endereço do tomador no exterior
ou não informado). Nesses casos o emitente indica **em qual país ocorreu o resultado**
do serviço.

> ⚠️ **Inconsistência na planilha (persiste no Anexo I v1.01 e no Anexo VI):** a coluna "País Resultado (Exportação)" também marca
> "SIM" no **cenário 68** (tomador no exterior, intermediário e local da prestação no
> Brasil, incidência no local da prestação, operação tributável), mas a regra E0590 **não
> lista** o 68. Não há como saber, pelas fontes, qual das duas vale. Ofereça consultar
> `fontes/documentos-fiscais/texto/anexo-i-exportacao-emissao-nfs-e.tsv`.

## NIF do exterior (tomador, intermediário, prestador e fornecedor)

Para pessoa **no exterior** o documento não usa CPF/CNPJ. Em cada papel (`prest`, `toma`,
`interm` e, no grupo de ajuste da base de cálculo, `fornec`) há uma **escolha**:

- **`NIF`** — número de identificação fiscal fornecido por órgão de administração
  tributária do exterior (até 40 caracteres); **ou**
- **`cNaoNIF`** — o **motivo** de não informar o NIF: **0** não informado na nota de
  origem; **1** dispensado do NIF; **2** não exigência do NIF.

O valor **0** de `cNaoNIF` só serve ao **compartilhamento** de NFS-e de município com o
ADN. O mesmo par existe no destinatário do grupo `IBSCBS` (`dest`), pela NT CGNFS-e
004 v2.00. Na tela do emissor a escolha aparece como "haverá NIF? sim/não" e, se não,
"dispensado" ou "não exigência" ([[df-nfse-emissao-pessoas]]).

Desde a NT CGNFS-e 009 v1.0, **todos os campos CNPJ** do leiaute passam de numérico a
**caractere** (CNPJ alfanumérico, a partir de julho de 2026); o CPF continua numérico.
O cronograma de implantação dessa mudança não está nas fontes.

## Os 112 cenários da planilha EXPORTACAO_EMISSÃO_NFS-e

A planilha cruza **8 combinações** de local (tomador × intermediário × local da prestação,
cada um Brasil ou exterior) com **14 respostas** do emitente: o subitem que define o local
de incidência do ISSQN (estabelecimento do prestador **EP**, estabelecimento do tomador
**ET**, local da prestação **LP**, o código **99.01.01** ou "qualquer serviço
parametrizado como não incidência"), a pergunta "é caso de imunidade, exportação ou não
incidência do ISSQN?" e a tributação escolhida (`tribISSQN`: imunidade, exportação de
serviço, não incidência ou operação tributável). Para cada cenário ela diz:

- se o emitente **declarou** ou não exportação, para o ISSQN e para a RFB (o critério do
  ISSQN é o **local da prestação no exterior**; o da RFB é **ao menos um dos três locais
  no exterior**);
- se o sistema **aceita** ou **rejeita/avisa** (mensagens 1, 2 e 3 e aviso 1);
- se **NBS**, **país do resultado** e **grupo `comExt`** são obrigatórios, proibidos ou
  opcionais.

**Mensagens da planilha:**

| Mensagem | Quando | Texto (resumo) | Rejeição |
|---|---|---|---|
| Erro 1 | cenários 6, 10, 34, 38, 66 e 80 | o sistema considera o cenário **operação tributável**; o emitente **não pode** declarar exportação | E0529 |
| Erro 2 | cenários 26, 54, 92, 96, 106 e 110 | o sistema considera o cenário **exportação de serviço**; o emitente **não pode** declará-lo operação tributável | E0530 |
| Erro 3 | 24 cenários (3, 7, 11, 17, 21, 25, 31, 35, 39, 45, 49, 53, 59, 63, 67, 73, 77, 81, 87, 91, 95, 101, 105 e 109) | "Não incidência" só vale com o código de tributação nacional **99.01.01** | — |
| Aviso 1 | cenários 64 e 78 | tomador no exterior e serviço devido no local do estabelecimento do tomador: o **sujeito passivo é o prestador** e o local de incidência do ISSQN é o local da prestação, "conforme os parágrafos 1º e 2º do art. 127 do CTN" | — (aviso) |

**Padrões que resolvem a maioria dos casos:**

1. **Nada no exterior e sem declarar exportação** (cenários 1, 4, 5, 8, 9, 12, 13, 14): `comExt` **não
   permitido**; NBS opcional.
2. **Algum local no exterior** (cenários 15 a 112, exceto os que dão erro): `comExt`
   **obrigatório** e NBS **obrigatória**; `cPaisResult` não é pedido (salvo os cenários da regra E0590).
3. **Tudo no Brasil, mas o emitente declara exportação de serviço** (cenário 2): é aceito,
   com NBS, país do resultado e `comExt` obrigatórios.
4. **Exemplo (cenário 60):** tomador no exterior, intermediário e local da prestação no
   Brasil, incidência no estabelecimento do prestador (EP), resposta "não" à pergunta de
   imunidade/exportação/não incidência e **operação tributável**: o documento é aceito;
   `comExt` e NBS são obrigatórios; `cPaisResult` não; o município de incidência do
   ISSQN indicado na planilha é o do estabelecimento do prestador.

> ⚠️ **Anomalias da planilha** (a planilha de cenários do Anexo I v1.01 e a do Anexo VI são iguais à da cópia anterior; nada foi corrigido): o cenário **112** aparece com
> intermediário no Brasil, repetindo a combinação dos cenários 85 a 98 (a numeração sugere
> tomador, intermediário e local da prestação no exterior); e o cenário **111** marca "sim"
> na coluna de exportação para o ISSQN, enquanto os demais cenários de não incidência
> marcam "-".

## ⏳ Sem data nas fontes — NT 009 v1.01 (11/09/2026) e Anexo VI v1.04.01

A NT CGNFS-e 009 v1.01 muda o grupo `comExt` e a base de cálculo do IBS/CBS em operações de
comércio exterior. O texto da NT diz que o **cronograma** será publicado no portal; ele **não está
nas fontes**. Quando o Anexo VI entrar em produção, passa a se chamar
`ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe`. Hoje vale o Anexo I v1.01 descrito acima. As mudanças, com o
fundamento que a NT cita (arts. do **Decreto 12.955/2026**, regulamento da CBS, e da **Res. CGIBS
6/2026**, regulamento do IBS):

| Campo | Anexo I v1.01 (hoje) | NT 009 v1.01 / Anexo VI |
|---|---|---|
| `mdPrestacao` | 0 a 4 | novo **5 — consumo concomitante no território nacional e no exterior**. Na **importação**, informar em `vServ` só a parcela consumida no País; na **exportação**, só a parcela exportada, e emitir **outra NFS-e regular** (não exportação) para a parcela consumida no País |
| `nFatura` | não existe | novo, 0-1, 1 a 20 posições: número da fatura de serviços ou do documento que comprove a transação (Decreto 12.955/2026, art. 74, §1º) |
| `vFatura` | não existe | novo, 0-1: valor total da fatura ou do documento, **na moeda de `tpMoeda`** (mesmo art. 74, §1º) |
| `nContCambio` | não existe | novo, 0-1, 1 a 20 posições: número do contrato de câmbio ou do documento que comprove o pagamento (mesmo art. 74, §1º) |
| `vServMoeda` | 1-1 (obrigatório) | 0-1 (**opcional**) |
| `tpMoeda` | código de 3 dígitos | passa a ter **validação** pela tabela de moedas do Banco Central |
| `nDI` (1 a 12) | Declaração de Importação (DI/DSI/DA/DRI-E) | renomeado **`nDUIMP`** (15 posições): Declaração Única de Importação. Preencher quando o serviço se relaciona à cobrança do serviço de importação de **bem material** |
| `nRE` (12) | Registro de Exportação | renomeado **`nDUE`** (14 posições): Declaração Única de Exportação (DU-E). Idem, para exportação de bem material |
| Regras E0352, E0354 e E0356 | falam de `nDI` e `nRE` | mesma lógica com `nDUIMP` e `nDUE`: `movTempBens` = 2 exige `nDUIMP`; = 3 exige `nDUE`; = 1 proíbe os dois |
| Regras E0529 e E0530 | valem para qualquer emitente | o Anexo VI as restringe a quando o emitente é o **prestador** (`tpEmit` = 1) |
| Valor "desconhecido" (`mdPrestacao` = 0, `vincPrest` = 9 etc.) | admitido no compartilhamento de NFS-e do município com o ADN | **a partir de 01/01/2027** não será admitido nas NFS-e compartilhadas pelos municípios: todas devem trazer valor válido do domínio do campo. Essa data vem do **texto da NT**; a regra de rejeição correspondente não aparece nas planilhas |

### Ajuste da base do IBS/CBS no comércio exterior (`vAjusteBCIBSCBSComExt`)

Campo novo (`DPS/infDPS/valores/vAjusteBC/vAjusteBCIBSCBSComExt`, 0-1, 15 inteiros e 2 decimais) para
registrar **ajustes positivos ou negativos só na base do IBS/CBS**, em operações de comércio
exterior, **sem alterar `vServ`**. A NT dá três hipóteses:

1. **Conversão de moeda diferente da usada para o ISSQN.** A legislação do IBS/CBS manda converter
   pela taxa do Banco Central (PTAX), observados os critérios do momento do fato gerador; para a
   NFS-e e o ISSQN pode haver regra de conversão diversa. Como `vServ` serve aos dois, a diferença
   vai no campo: **positivo** se a base do IBS/CBS for maior que o valor convertido na NFS-e,
   **negativo** se for menor.
2. **Fator de redução na importação de serviços financeiros** tributados por margem: o contribuinte
   informa o valor da redução da base resultante do fator previsto na legislação.
3. **Parcela que excede o valor de mercado** na importação de serviços financeiros entre **partes
   relacionadas**, quando a alíquota zero se aplica: continua tributada a parcela acima dos preços e
   taxas usuais de mercado, e o ajuste registra o necessário para chegar a ela.

A fórmula da base passa a somar o campo: `vBC = vServ − descIncond − (vCalcAjusteBCIBSCBS ou
vCalcAjusteBCLocImoveis) − vISSQN + vAjusteBCIBSCBSComExt` (até 2026, ainda `− vPIS − vCOFINS`; de
2027 até 2032, sem PIS/COFINS). Detalhe da fórmula em [[df-nfse-layout-ibscbs]]. As **regras legais**
de conversão e de base dos serviços financeiros estão no domínio `reforma` e não são explicadas aqui;
a NT só descreve o campo.

## O que continua sem resposta nas fontes

- **Qual opção escolher** (modo de prestação, vínculo, mecanismo de apoio) em um caso
  concreto: o leiaute define os códigos, mas não diz qual cabe a cada operação.
- **Coerência com o IBS/CBS:** `mdPrestacao` e a classificação tributária
  (CST/cClassTrib) são campos separados. Nenhuma fonte do projeto liga um ao outro. O
  CST/cClassTrib da exportação está em [[df-tabela-cclasstrib]]; os requisitos legais, em
  [[ibs-cbs-exportacao]].
- O **cronograma** em que os grupos `IBSCBS` e os ajustes das NTs 005, 007 e 009 entram em
  produção: [[df-nfse-cgnfse-notas-tecnicas]].
