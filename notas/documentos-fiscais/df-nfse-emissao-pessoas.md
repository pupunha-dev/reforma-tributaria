---
título: NFS-e Nacional — emissão completa, passo 1 (Pessoas): emitente, tomador, destinatário, intermediário e dados gerais da DPS
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seção 4.1 e 4.1.1 (p. 20-42); NT 2025.002-RTC v1.52 (referência para CST/cClassTrib, ver df-cst-cclasstrib)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Emissão completa, passo 1: Pessoas

## A lógica em uma frase

O passo 1 responde "**quem** participa da operação e **sob quais regras gerais** a
DPS será feita": quem emite, para quem, quem recebe o serviço, se há intermediário,
a data de competência, a numeração da DPS e **se a nota terá IBS/CBS**. Muita coisa
vem pronta dos cadastros; o emitente confere e completa.

> A obrigatoriedade campo a campo e as regras de negócio estão nas **planilhas de
> leiaute da DPS** (`ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe`), que **não estão nas fontes
> do projeto**. Esta nota traz o que o guia diz no texto (⚠️ lacuna em `pendencias.md`).

## Quando a emissão completa é obrigatória

A Emissão Completa serve a **todos** os contribuintes e é **obrigatória** para
algumas prestações, como **exportação** e serviços cujo ISSQN é devido no **local do
tomador/adquirente**. A Emissão Simplificada é só do MEI
([[df-nfse-emissao-final-mei]]).

## Informações gerais

### "Preencher as informações IBS/CBS?" (Sim/Não)

Pergunta que decide se a DPS leva os campos de IBS e CBS. O guia informa:

- Regime regular: desde **03/08/2026** o preenchimento passa a ser exigido, "observadas
  as respectivas regras de validação"; **não é permitido emitir** sem os campos de
  IBS/CBS. Optantes do Simples Nacional: obrigatório para **fatos geradores a partir
  de 01/01/2027**. As duas datas e o aviso de lacuna (o ato que as fixa não está nas
  fontes) estão em [[df-nfse-visao-geral]].
- Marcando **"Sim"**, a **data de competência** tem de ser **igual ou maior que
  01/01/2026**.
- Marcar "Sim" libera outros campos, como o **destinatário do serviço** (abaixo) e,
  nos passos seguintes, os campos de IBS/CBS ([[df-nfse-emissao-servico]] e
  [[df-nfse-emissao-valores-ibs-cbs]]).

### Data de competência, número e série da DPS

- **Data de competência:** obrigatória; é a data em que o serviço foi prestado.
- **DPS:** documento de posse e responsabilidade do contribuinte, gerado manualmente
  ou por aplicação, com **numeração sequencial crescente**, que deve ser convertido
  em NFS-e **no prazo da legislação tributária municipal**. Pode ser enviado em
  **lote**, para quem não tem conectividade o tempo todo, com uma aplicação instalada
  que siga as especificações do Comitê Gestor da NFS-e.
- **Número e série** (opcional informar): o sistema normalmente os gera. O emitente
  só os digita se precisa controlá-los (por exemplo, para transcrever a série
  repassada ao não emitente). A **série** deve ser um número entre **80.000 e 89.999**,
  pela regra "Faixas de utilização da série da DPS" do anexo de leiaute.

## Emitente da NFS-e

Há três opções (Prestador/Fornecedor, Tomador/Adquirente, Intermediário), mas **na
versão atual só o Prestador/Fornecedor pode emitir**. A emissão pelo tomador/adquirente
e pelo intermediário "ainda não estão disponíveis" e virão em versão futura.

Dados do emitente (todos **recuperados** dos cadastros da RFB ou do CNC, conforme o
convênio do município): CPF/CNPJ, nome ou razão social, município (que corresponde ao
código do município emissor, `cLocEmi`), indicador municipal (inscrição), opção no
Simples Nacional, e-mail, telefone e endereço. Para e-mail e telefone ausentes nesses
cadastros, vale o que foi preenchido em Configurações
([[df-nfse-painel-configuracoes]]).

**Regime de apuração dos tributos (só optantes do Simples):** o emitente informa se
os tributos federais e o municipal são apurados **pelo Simples Nacional ou pela
NFS-e**. A escolha **habilita ou desabilita** os campos da tributação municipal
(ISSQN) no passo 3.

## Compras governamentais

Se a operação é compra governamental, informa-se o **ente**: União, Estado, Distrito
Federal ou Município. O guia diz que, **para emissões com destaque de IBS/CBS, as
informações de compras governamentais devem ser preenchidas**, e que, com "Sim", o
endereço do tomador/adquirente fica obrigatoriamente "Brasil".

## Tomador/adquirente do serviço

Três opções: **Brasil**, **Exterior** ou **não informado** (sem campos extras).

- Para certos **Códigos de Tributação Nacional** do passo 2, informar o tomador é
  **obrigatório**, porque ele define o **local de incidência do ISSQN** (LC 116/2003;
  planilha `MUN.INCID_INFO.SERV` do anexo de leiaute).
- **No Brasil:** CPF/CNPJ (com busca nos últimos tomadores), indicador municipal,
  nome/razão social (recuperado dos cadastros), telefone e e-mail opcionais e
  endereço (CEP, município, bairro, logradouro, número e complemento). O endereço de
  CNPJ vem da RFB e pode ser alterado; município, bairro e logradouro vêm da tabela
  TOM pelo CEP.
- **No Exterior:** informa-se se haverá **NIF** (Número de Identificação Fiscal do
  exterior, equivalente a CPF/CNPJ). Se **não** há NIF, escolhe-se o motivo:
  **dispensado do NIF** ou **não exigência do NIF**. Depois: nome, e-mail e telefone
  opcionais e endereço (logradouro, número, complemento, bairro, cidade, código
  postal, estado/província/região e país).
  No XML a escolha é `NIF` **ou** `cNaoNIF` (0 não informado na nota de origem, só para
  compartilhamento do município; 1 dispensado; 2 não exigência). Tomador ou intermediário
  no exterior **exige** o grupo de comércio exterior: [[df-nfse-comercio-exterior]].

## Destinatário do serviço (só com IBS/CBS)

Habilitado quando se marca "Sim" em "Preencher as informações IBS/CBS?". Pergunta
se o destinatário é o **próprio tomador** ("Sim", sem campos extras) ou **outra
pessoa** ("Não"): então escolhe-se **Brasil** ou **Exterior** e preenchem-se os
mesmos campos do tomador (CPF/CNPJ, indicador municipal, nome, contatos e endereço;
no exterior, NIF ou motivo, nome e endereço).

## Intermediário do serviço

Três opções: **Brasil**, **Exterior** ou **não informado**. No Brasil: CPF/CNPJ
(obrigatório), indicador municipal (opcional), nome/razão social, contatos e
endereço. No Exterior: NIF ou motivo, nome e endereço, como no tomador. O valor
recebido pelo intermediário entra no passo 3 ([[df-nfse-emissao-valores-ibs-cbs]]).

## ⏳ A partir de 01/01/2027 — obrigatoriedade de IBS/CBS para o Simples Nacional (guia)

Para optantes do Simples, o guia diz que o preenchimento de IBS/CBS só passa a ser
exigido para **fatos geradores a partir de 01/01/2027**. Para o regime regular a
exigência informada é a de 03/08/2026 (já passou na data-base 16/10/2026). Não
misture as duas datas na mesma frase. O ato que fixa as duas **não está nas fontes**.

## Ligações

- [[df-nfse-visao-geral]]: datas do IBS/CBS e glossário.
- [[df-nfse-emissao-servico]]: passo 2.
- [[df-nfse-decisao-administrativa-judicial]]: no passo "Pessoas" desse fluxo o
  emitente pode ser também tomador, destinatário e intermediário.
- [[df-cst-cclasstrib]]: os códigos de situação tributária usados depois.
