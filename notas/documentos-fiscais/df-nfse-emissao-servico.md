---
título: NFS-e Nacional — emissão completa, passo 2 (Serviço): local, código de tributação, NBS, indicador da operação, imóveis, eventos, comércio exterior e tipo de operação
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seção 4.1.2 (p. 43-66); LC 214/2025, art. 254 (conferido em fontes/reforma/texto); NT 2025.002-RTC v1.52 (referência para CST/cClassTrib, ver df-cst-cclasstrib)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Emissão completa, passo 2: Serviço

## A lógica em uma frase

O passo 2 descreve **o que foi prestado e onde**: o país e o município da prestação,
o **Código de Tributação Nacional** (a "gaveta" do serviço na lista nacional), a
**NBS** (o classificador do serviço) e, nas notas com IBS/CBS, o **código indicador
da operação**. Dependendo da gaveta escolhida, a tela abre blocos extras: imóvel ou
obra, evento, comércio exterior.

> Campos e regras de negócio: planilhas de leiaute da DPS (`ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe`),
> que **não estão nas fontes**. O ISSQN (quem cobra, alíquota, benefício) é matéria
> **municipal e fora do escopo**; aqui só se descreve como a tela se comporta.

## Local da prestação

- **País:** onde foi concluído o serviço (tabela de países ISO2 do Anexo A do
  leiaute).
- **Município:** obrigatório quando o país é "Brasil" (busca a partir de 3
  caracteres).
- Para certos códigos de tributação, o **tomador** passa a ser obrigatório (define o
  local de incidência); o sistema exibe uma mensagem e, com "Sim", abre a tela do
  tomador ([[df-nfse-emissao-pessoas]]).

## Código de Tributação Nacional e código complementar

- **Código de Tributação Nacional:** obrigatório; escolhido na lista nacional de
  serviços (Anexo B; o guia cita o arquivo "..._V1.01-20260122"), com busca a partir
  de 3 caracteres. Alguns campos só aparecem conforme o código escolhido.
- **Código complementar municipal:** obrigatório quando o município tiver criado
  códigos complementares.
- **Pergunta "é caso de imunidade, exportação de serviço ou não incidência do
  ISSQN?":** "Não" não exige nada. "Sim" abre a escolha entre:
  - **Imunidade:** escolhe-se o tipo de imunidade.
  - **Exportação de serviço:** informa-se o **país em que se verificou o resultado**
    do serviço.
  - **Não incidência:** preenchida automaticamente com o código **99.01.01** ("serviço
    sem incidência de ISSQN e ICMS") ou com códigos que o município tenha configurado
    como não incidência. Fora desses, o sistema **não permite** a seleção.
  Muitos campos do passo 3 dependem desta resposta.
- **Município de incidência do ISSQN:** o Sistema Nacional identifica a localidade
  conforme a LC 116/2003. Não há localidade de incidência em **imunidade**,
  **exportação** e **serviço sem incidência** (99.01.01); em **operação tributável**
  deve haver. Há exceções em que o sistema nacional não identifica a localidade nem
  destaca o ISSQN, como o subitem **17.05.01** (fornecimento de mão de obra).
  Para o subitem **03.04** (locação/sublocação de ferrovia, rodovia, postes, cabos,
  dutos e condutos), se o local informado na DPS é a localidade geral (código
  `0000000`, `TAB.LOC.GERAL`), a localidade de incidência **não** é identificada na
  NFS-e; ela é informada na solicitação de apuração enviada ao **MAN**.

## Data de competência, NBS e indicador da operação

- **Data de competência:** recuperada da informada no passo 1.
- **Item da NBS:** obrigatório; a NBS correspondente ao serviço prestado.
- **Código indicador da operação** (`IndOp_IBSCBS`): **obrigatório nas emissões com
  destaque de IBS/CBS**; escolhido na lista do **Anexo VII** do leiaute, que **não
  está nas fontes** (⚠️ lacuna: os códigos não podem ser listados aqui). O guia
  só cita que os códigos **020101, 020201 e 020301** ligam o serviço a **imóveis**.
- **Descrição do serviço:** obrigatória, detalhada.

## Imóvel e obra

- **Informações do imóvel** (códigos de operação 020101, 020201 e 020301): código do
  **CIB** (Cadastro Imobiliário Brasileiro, só se o local é Brasil), **endereço**
  (no Brasil: CEP, que deve pertencer ao **município informado como local da
  prestação**, número e complemento; no exterior: logradouro, número, bairro, cidade,
  código postal, estado/região) e **inscrição imobiliária fiscal** (código da
  prefeitura para identificar a obra ou recolher IPTU).
- **Informações para obra:** no lugar do bloco de imóvel, quando o código de
  tributação for dos subitens **07.02** e **07.05**. Escolhe-se informar o **código
  da obra** (só no Brasil), o **CIB** ou o **endereço**, com as mesmas regras de CEP
  e de exterior.

## Evento

Para os subitens do **item 12** (diversões, lazer, entretenimento e congêneres): data
inicial e final (obrigatórias), descrição e a forma de identificar o local: o
**identificador** da atividade de evento determinado pela Administração Tributária
(opcional, só no Brasil) ou o **endereço** (Brasil: CEP do município da prestação;
exterior: campos do endereço estrangeiro).

## Comércio exterior

O guia abre o bloco de comércio exterior com esta frase: "quando o País da
Prestação/Fornecimento do serviço é diferente de Brasil, algumas informações
adicionais são requisitadas". Em seguida diz que, **para a RFB**, a prestação é uma
operação de comércio exterior quando **ao menos um** destes itens está no exterior:
**tomador/adquirente, intermediário ou local da prestação**. Ou seja, **tomador ou
intermediário no exterior já caracteriza** comércio exterior, mesmo que o serviço seja
executado no Brasil.

> ⚠️ **Lacunas do guia** (o guia não responde): (1) se, com o país da prestação "Brasil"
> e o tomador no exterior, a tela abre o bloco da mesma forma (o guia só descreve o
> gatilho do país da prestação); (2) **qual opção** de modo de prestação, de vínculo ou
> de mecanismo de apoio vale para cada caso concreto: ele só lista as opções, sem
> defini-las. A escolha depende da operação real, não do guia. Na pergunta "é caso de
> imunidade, exportação de serviço ou não incidência do ISSQN?" (passo 2), a opção
> "exportação de serviço" pede o país em que se verificou o resultado do serviço; o
> ISSQN em si é matéria municipal, fora do escopo.
>
> **IBS/CBS da exportação de serviço:** o que torna o serviço exportação (fornecimento
> para residente no exterior **e** consumo no exterior) está em
> [[ibs-cbs-exportacao]] (LC 214, art. 80); o CST/cClassTrib (410 e 410004) está em
> [[df-tabela-cclasstrib]]. O guia não escolhe esses códigos.

Campos pedidos no bloco:

| Campo | Regra |
|---|---|
| Modo de prestação | obrigatório: transfronteiriço, consumo no Brasil, movimento temporário de pessoas físicas ou consumo no exterior |
| Vínculo entre as partes | obrigatório: sem vínculo, controlada, controladora, coligada, matriz, outro vínculo ou desconhecido |
| Moeda | código de 3 dígitos numéricos da tabela do Banco Central |
| Valor do serviço em moeda estrangeira | obrigatório |
| Mecanismo de apoio/fomento do prestador e do tomador | obrigatório; listas (por exemplo ACC, ACE, BNDES-Exim, FGE, PROEX, RECINE, REIDI, ZPE) com a opção "Nenhum" |
| Vínculo da operação a movimentação temporária de bens | obrigatório: não, vinculada a Declaração de Importação (informar o número averbado de DI/DSI/DA/DRI-E) ou vinculada a Declaração de Exportação (informar o Registro de Exportação averbado) |
| Compartilhar a NFS-e com o **MDIC** | obrigatório: sim ou não |

## Tipo de operação (compras governamentais e imóveis)

Campo exigido nos casos de **compras governamentais** ou de algum dos serviços do
**art. 254 da LC 214/2025** (o guia cita os subitens **25.05, 15.09, 17.12 e 10.05**
da lista de serviços). O art. 254 da LC 214 trata do **momento do fato gerador** em
operações com bens imóveis (alienação, direitos reais, locação, administração e
construção; ver [[regime-especifico-bens-imoveis]]). O guia não explica por que esses
subitens da lista de serviços se ligam ao artigo; a nota registra a citação do guia.

As cinco opções descrevem a **relação entre fornecimento e pagamento**:

1. fornecimento com pagamento posterior;
2. recebimento do pagamento com fornecimento já realizado;
3. fornecimento com pagamento já realizado;
4. recebimento do pagamento com fornecimento posterior;
5. fornecimento e recebimento do pagamento concomitantes.

Nas opções **2 ou 3**, informa-se a **chave de acesso da NFS-e** que acobertou o
fornecimento ou o recebimento já realizado: **50 caracteres alfanuméricos**; chave
inválida gera mensagem de erro.

## Informações complementares

Opcionais: número do documento de responsabilidade técnica, documento de referência,
informações complementares sobre o serviço, e número de pedido, ordem de compra,
ordem de serviço ou projeto (com a opção de listar **itens** em operações B2B).

## Ligações

- [[df-nfse-emissao-pessoas]]: passo 1.
- [[df-nfse-emissao-valores-ibs-cbs]]: passo 3.
- [[regime-especifico-bens-imoveis]]: art. 254 e o regime de bens imóveis.
- [[ibs-cbs-exportacao]]: quando o serviço é exportação (art. 80 da LC 214).
- [[df-visao-geral-reforma-nfe]]: o paralelo na NF-e.
