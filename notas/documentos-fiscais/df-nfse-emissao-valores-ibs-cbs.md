---
título: NFS-e Nacional — emissão completa, passo 3 (Valores): descontos, deduções, tributação federal, CST/cClassTrib do IBS/CBS e documentos de reembolso, repasse e ressarcimento
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seção 4.1.3 (p. 66-84); NT 2025.002-RTC v1.52, seções 2 e 3 (CST e cClassTrib, ver df-cst-cclasstrib)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Emissão completa, passo 3: Valores

## A lógica em uma frase

O passo 3 transforma o serviço em **números**: valor cobrado, descontos, o que reduz
a base, os tributos federais e, nas notas com IBS/CBS, **qual regra do IBS/CBS se
aplica** (o CST e o cClassTrib, os mesmos da NF-e). Muitos campos vêm **travados ou
preenchidos sozinhos**, conforme o que foi escolhido nos passos anteriores e as
configurações do município.

> Obrigatoriedade e regras de negócio de cada campo estão nas planilhas de leiaute
> da DPS (`ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe`), **fora das fontes**. O ISSQN é
> matéria **municipal e fora do escopo**; os blocos municipais abaixo descrevem só o
> comportamento da tela.

## Valores do serviço

| Campo | Regra do guia |
|---|---|
| Valor da operação/serviço | obrigatório; total cobrado pelo serviço |
| Valor recebido pelo intermediário | opcional; só aparece se houve intermediário no passo 1 |
| Desconto **incondicionado** | opcional; concedido sem condição; **reduz o valor do serviço** |
| Desconto **condicionado** | opcional; depende de condição posterior à emissão; **não reduz a base de cálculo** |

## Tributação municipal (ISSQN) — só o que a tela faz

- A tributação (operação tributável, imunidade, exportação, não incidência) é
  **preenchida automaticamente** pelas escolhas do passo 2. Para exportação, alguns
  campos não podem ser informados (planilha "COMEX - EXPORTAÇÃO DE SERVIÇO").
- Optante do Simples com apuração **pelo Simples**: os campos municipais **não são
  habilitados** e o sistema mostra uma mensagem.
- **Exigibilidade suspensa:** "Sim" exige o tipo (decisão judicial ou processo
  administrativo) e o número do processo. Com exigibilidade suspensa **não é possível
  informar retenção**; o sistema alerta.
- **Retenção do ISSQN:** "Sim" pede quem retém (tomador ou intermediário), e a pessoa
  escolhida **precisa ter sido informada no passo 1**; se não foi, o sistema mostra
  um aviso e um botão para incluí-la. Para a ME/EPP que apura o ISSQN pelo Simples,
  é obrigatório informar a **alíquota do ISSQN** quando há retenção.
- **Benefício municipal:** "Sim" só é possível se o município tiver cadastrado
  benefício para o serviço ou para o prestador na data de competência; se o benefício
  for de redução de base de cálculo, informa-se o valor (percentual ou monetário).
- **Dedução/redução da base de cálculo:** por valor monetário (menor que o valor do
  serviço), por percentual, ou por **documentos** (NF-e, NFS-e, outras NFS-e, NF/NFS,
  outros documentos fiscais, outros documentos). Para NF-e e NFS-e informa-se a
  **chave de acesso** (44 e 50 caracteres alfanuméricos; o sistema confere se o
  documento existe e, se não, mostra "Informe uma chave de NF-e ou NFS-e válida."),
  o tipo de dedução, a data de emissão, o **valor dedutível** e o **valor da
  dedução**, com a opção de identificar o fornecedor (Brasil ou Exterior).
- **Alerta de alíquota mínima:** o guia avisa que, "salvo exceções previstas na
  legislação", o ISSQN não pode ter redução de base que resulte em carga menor que a
  da **alíquota mínima de 2,0%** do valor do serviço, e o sistema exibe alerta. (O
  guia não cita a base legal desse limite.)
- **Cálculo:** a alíquota vem do passo 2; a **base de cálculo do ISSQN** é o valor do
  serviço menos as deduções e o desconto incondicionado; o valor do ISSQN é calculado
  automaticamente.

## Tributação federal

Para quem apura os tributos pelo Simples Nacional, esses campos **já vêm
preenchidos e não podem ser alterados**. Para os demais:

- **PIS/COFINS:** escolhe-se a **situação tributária** (por exemplo, 00 nenhum, 01
  operação tributável com alíquota básica); conforme a escolha, informam-se a base de
  cálculo e as alíquotas de PIS e COFINS, e o sistema calcula o **débito de apuração
  própria** de cada um.
- **Tipo de retenção de PIS/COFINS/CSLL:** obrigatório (por exemplo, 0 = não retidos;
  3 = retidos).
- **Outros tributos federais** (todos opcionais): IRRF retido, contribuições sociais
  retidas (PIS/COFINS/CSLL) e contribuição previdenciária patronal retida. Os valores
  são os da legislação própria de cada tributo; o guia só indica onde digitá-los.

## IBS e CBS: CST e cClassTrib

Grupo com os campos para o **CST** (Código de Situação Tributária) e o **cClassTrib**
(Código de Classificação Tributária) aplicáveis ao serviço. Os dois são
**obrigatórios**, e a **lista de cClassTrib** exibida **depende do CST** escolhido
antes. Mecanismo e significado: [[df-cst-cclasstrib]]; os códigos e suas reduções:
[[df-tabela-cclasstrib]]; crédito presumido: [[df-credito-presumido-ccredpres]].

⚠️ O guia **não lista** os CST/cClassTrib; ele remete às tabelas do sistema. Quem
decide qual usar é a LC 214 aplicada à operação, não o guia.

### Documentos de reembolso, repasse e ressarcimento

No mesmo grupo podem ser incluídos **documentos referenciados** nos casos de
**reembolso, repasse e ressarcimento**, "a serem considerados na apuração da base de
cálculo do IBS/CBS". Por documento informa-se:

- **tipo:** NF-e, NFS-e, CT-e ou outro; para NF-e e NFS-e, a **chave de acesso** (44
  e 50 caracteres alfanuméricos), conferida pelo sistema;
- **identificação** do reembolso/repasse/ressarcimento (por exemplo, "repasse de
  remuneração por intermediação");
- **data de emissão** e **data de competência** do documento;
- **valor** do reembolso/repasse/ressarcimento, que o guia diz ser "considerado na
  base de cálculo do IBS/CBS";
- opcionalmente, o **fornecedor** (Brasil ou Exterior).

Os documentos incluídos ficam listados e podem ser editados ou excluídos. 

⚠️ O guia não diz **se** o valor entra na base ou sai dela. Pela lei, os reembolsos por
conta de terceiros, com documento fiscal em nome do terceiro, **não integram** a base
(ver [[ibs-cbs-base-calculo]]). A regra é a da lei e da regulamentação, não a do
guia; para o caso concreto, consulte a nota da base de cálculo.

## Valor aproximado dos tributos

Pode ser pré-configurado em Configurações ([[df-nfse-painel-configuracoes]]). No
passo 3 informam-se: os **valores monetários totais** Federal, Estadual e Municipal;
ou os **percentuais totais** Federal, Estadual e Municipal; ou, para o optante do
Simples, a **alíquota nominal** do Simples Nacional aplicável ao emitente (art. 9º do
Decreto 8.264/2014, que regulamenta a Lei 12.741/2012, segundo o guia).

## ⏳ A partir de 01/01/2027 — IBS/CBS obrigatório para o Simples (guia)

Os campos de IBS/CBS deste passo são exigidos do regime regular desde 03/08/2026 e
dos optantes do Simples para fatos geradores a partir de 01/01/2027, segundo o guia
(detalhe e lacuna do ato em [[df-nfse-visao-geral]]).

## Ligações

- [[df-nfse-emissao-servico]]: passo 2.
- [[df-nfse-emissao-final-mei]]: passo 4, conferir e emitir.
- [[df-tabela-cclasstrib]] e [[df-cst-cclasstrib]]: os códigos.
