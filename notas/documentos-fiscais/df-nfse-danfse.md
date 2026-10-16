---
título: NFS-e Nacional — DANFSe (NT CGNFS-e 008): blocos obrigatórios, supressões permitidas, QR Code e marcas d'água
dominio: documentos-fiscais
fontes: NT CGNFS-e 008 v1.02 (14/07/2026; versão 1.01 de 30/06/2026; versão 1.0 sem data nas fontes); NT CGNFS-e 004 v2.00 (10/12/2025), seção 1.2; NT CGNFS-e 007 v1.0 (07/02/2026); Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# DANFSe: o documento auxiliar da NFS-e

## A lógica em uma frase

O **DANFSe** é a representação **impressa** da NFS-e: ele **só pode mostrar o que está no XML**
da nota, em modelo e fontes definidos pela **NT CGNFS-e 008**, e desde **03/08/2026** o DANFSe
deve ser gerado pelo **próprio software** do emissor, ERP ou sistema fiscal, porque a API
nacional de geração do DANFSe é **suspensa nessa data**. A NT é nível de documentação técnica
(como imprimir); ela não cria obrigação tributária. A consulta e o download do PDF no emissor
estão em [[df-nfse-consulta-cancelamento-substituicao]].

## O que a NT 008 diz

- **Finalidade (item 2):** (a) facilitar a consulta resumida da NFS-e, atendendo à necessidade
  de representação impressa prevista na legislação; (b) auxiliar os processos administrativos e
  financeiros do destinatário **não credenciado** como emissor de NFS-e. Impresso em **uma única
  via** e em **uma única página**, em qualquer papel (**exceto papel jornal**), com contraste
  suficiente para ler o QR Code; **retrato**, formulário mínimo **A4**; margens de **0,15 a
  0,20 cm** em cada lado.
- **API de geração do DANFSe** (`https://adn.nfse.gov.br/danfse/docs/index.html`): será
  **sobrestada (suspensa) em 03/08/2026**. A data foi alterada nas versões 1.01 (30/06/2026) e
  1.02 (14/07/2026); a redação vigente é a da v1.02. Em 16/10/2026 a data já passou; as fontes
  não dizem se a API foi de fato desligada.
- **Novos fatos geradores** (operações no campo do IBS/CBS que antes não eram documentadas por
  nota fiscal, seção 3.a da NT 007): terão **nota técnica específica** de DANFSe, ainda não
  publicada nas fontes.
- **Homologação:** o DANFSe de nota com `tpAmb` = 2 (produção restrita) deve trazer, no
  cabeçalho, **"NFS-e SEM VALIDADE JURÍDICA"** (negrito, 9 pt, Arial, vermelho sólido).
- **Totais aproximados de tributos** (Lei 12.741/2012): constam em "Informações
  Complementares", obrigatoriamente, com valores em R$ **ou** em %: federais, estaduais e
  municipais. A lei não está nas fontes: a nota registra só a exigência do layout.

## Blocos do DANFSe (item 2.1)

Os campos "representam o conteúdo das respectivas tags" do XML. Os tamanhos sugeridos
(item 2.4.5) **não são obrigatórios**, mas o modelo do Anexo I e as fontes mínimas são.

| Bloco | Conteúdo mínimo |
|---|---|
| Chave de acesso | **50 dígitos**, em um único bloco |
| Identificação da NFS-e | chave, número, competência, data e hora da emissão, número, série e emissão da DPS, **emitente**, situação e finalidade |
| Prestador/fornecedor | CNPJ/CPF/NIF, inscrição municipal, telefone, nome, município/UF, IBGE/CEP, endereço, e-mail, **informação sobre o Simples Nacional na data da competência** e **regime de apuração tributária pelo SN** |
| Tomador/adquirente | CNPJ/CPF/NIF, inscrição municipal, telefone, nome, município/UF, IBGE/CEP, endereço e e-mail |
| Destinatário | CNPJ/CPF/NIF, telefone, nome, município/UF, IBGE/CEP, endereço e e-mail |
| Intermediário | como o tomador |
| Serviço prestado | código de tributação nacional/municipal e sua descrição, **NBS**, local da prestação (UF/país) e descrição do serviço |
| Tributação municipal (ISSQN) | tipo de tributação, município/UF/país de incidência, regime especial, imunidade, suspensão, benefício municipal, deduções/reduções, desconto incondicionado, base, alíquota, retenção e valor |
| Tributação federal (exceto CBS) | IRRF, contribuição previdenciária retida, contribuições sociais retidas, PIS e COFINS de apuração própria |
| **Tributação IBS/CBS** | CST e cClassTrib; indicador da operação, município de incidência; exclusões e reduções da base; base após exclusões e reduções; reduções de alíquota do IBS e da CBS; alíquotas estadual e municipal do IBS e efetivas; valores apurados do IBS (municipal, estadual e total) e da CBS (alíquota e valor) |
| Valor total da NFS-e | valor do serviço, descontos incondicionado e condicionado, retenções (ISSQN e federais), **valor líquido**, **total do IBS/CBS** e **valor líquido + IBS/CBS** |
| Informações complementares | bloco imóvel, bloco obra, bloco evento, informações complementares, informações de uso da administração municipal e totais aproximados dos tributos |
| Canhoto | opcional: data de cientificação, identificação/assinatura, número ou chave |

**Notas do item 2.4.5:**

- As linhas de **PIS e COFINS de apuração própria** e da **descrição das contribuições sociais
  retidas** (marcadas com a nota 6) "serão impressas para as NFS-e emitidas com data de
  competência **até o final do ano-calendário de 2026**". A v1.02 ajustou o tratamento dos
  campos `vPis`, `vCofins` e `tpRetPisCofins` ([[df-nfse-layout-ibscbs]]).
- **Substituição:** no campo de informações complementares, "NFS-e Subst.:" mais a chave da
  nota substituída (`chSubstda`). **Obra e imóvel:** "Cod. Obra:" e "Insc. Imob.:" (campos
  `cObra` e `inscImobFisc`). **Evento:** "Cod. Evt.:" (campo `idAtvEvt`).
- Campo sem informação no XML leva um traço (-). O bloco de canhoto é opcional.

## Supressões e modificações permitidas (item 2.3)

- Se **tomador**, **destinatário**, **intermediário** ou **tributação municipal** não existirem
  ou não se aplicarem, os blocos podem ser reduzidos a uma frase: "TOMADOR/ADQUIRENTE DA
  OPERAÇÃO NÃO IDENTIFICADO NA NFS-e", "DESTINATÁRIO DA OPERAÇÃO NÃO IDENTIFICADO NA NFS-e",
  "INTERMEDIÁRIO DA OPERAÇÃO NÃO IDENTIFICADO NA NFS-e" e "TRIBUTAÇÃO MUNICIPAL (ISSQN) -
  OPERAÇÃO NÃO SUJEITA AO ISSQN" (altura mínima do bloco 0,32 cm, largura mínima 20,40 cm).
  O espaço liberado vai para "Descrição do Serviço" ou "Informações Complementares".
- Se o destinatário é o **próprio tomador/adquirente**: "O DESTINATÁRIO É O PRÓPRIO
  TOMADOR/ADQUIRENTE DA OPERAÇÃO".
- Sem canhoto, o espaço também pode ser reaproveitado.

## Aparência (item 2.4)

- Fontes: **Arial** para títulos (rótulos) e **Microsoft Sans Serif** para os conteúdos, em preto
  sólido (K100). Rótulo de bloco: 7 pt, negrito, caixa alta; rótulo de campo: 6 pt, negrito (7 pt
  e caixa alta na identificação); conteúdo: 7 pt.
- **Cabeçalho:** logomarca da NFS-e à esquerda; ao centro **"DANFSe v2.0"** e "Documento Auxiliar
  da NFS-e" (9 pt, Arial, negrito); à direita o município do emitente, o ambiente gerador e o
  tipo de ambiente.
- **QR Code:** à direita da identificação, aponta para
  `https://www.nfse.gov.br/ConsultaPublica/?tpc=1&chave=` seguido da chave de acesso;
  dimensões mínimas **1,52 × 1,52 cm**; abaixo, o texto "A autenticidade desta NFS-e pode ser
  verificada pela leitura deste código QR ou pela consulta da chave de acesso no portal
  nacional da NFS-e" (6 pt, três linhas).
- Linhas divisórias de 0,5 pt; borda da página de 1 pt; cabeçalho, títulos de bloco, "Emitente da
  NFS-e" e "Valor Líquido da NFS-e + IBS/CBS" com fundo cinza claro (5%).

## Cancelamento e substituição (item 2.5)

Marca d'água **diagonal** "**CANCELADA**" (nota cancelada) ou "**SUBSTITUÍDA**" (nota substituída),
em Arial, mínimo de **50 pontos**, cinza (K35). Se a impressora exigir margem maior, a redução
sai só da altura do bloco "Informações Complementares" (2.5.3).

## Ressalvas

- O **guia do emissor** (27/07/2026) trata o DANFSe como PDF e tem divergência interna
  ([[df-nfse-consulta-cancelamento-substituicao]]); a **NT 008** é quem define o layout.
- A NT 004 v2.00 (dez/2025) dizia que o DANFSe **não exibia** os grupos `IBSCBS` no início; a
  NT 008 v1.02 (jul/2026) já traz o bloco "Tributação IBS/CBS". Valem as NTs mais novas, mas
  a **data de produção** do DANFSe v2.0 não está nas fontes.
