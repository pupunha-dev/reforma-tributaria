---
título: NFS-e Nacional — consultar NFS-e emitidas, substituir, cancelar, baixar XML e DANFSe e consulta pública
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seções 5 e 9 (p. 100-106 e 115-117); NT 2025.002-RTC v1.52 (referência de hierarquia, ver df-visao-geral-reforma-nfe)
vigencia: atual
texto-base: 2026-10-16
---

# Consultar, substituir, cancelar e baixar a NFS-e

## A lógica em uma frase

Depois de emitida, a NFS-e **não se edita**: ou se **substitui** (nova DPS com a chave
da nota original, que cancela a antiga e deixa as duas ligadas) ou se **cancela**
(evento vinculado à nota). Tudo fica **rastreável**, porque cada ato vira um
documento eletrônico ligado à NFS-e. Os **prazos e permissões** de substituição e
cancelamento são **definidos por cada município**.

## Consulta das NFS-e emitidas (seção 5)

- A tela lista: emissão, emitida para, competência, município emissor, preço do
  serviço (R$) e situação, com **filtros** e o **total de NFS-e emitidas** desde o
  início do uso. O resultado vem **por páginas**.
- Ações por linha: visualizar; substituir; cancelar; baixar o **XML**; baixar o
  **DANFSe** (PDF). Também há o botão para iniciar uma nova NFS-e.
- **Visualizar** mostra a nota e os **eventos vinculados** (cancelamento,
  substituição). A nota pode ser baixada em HTML, XML e PDF; os eventos só estão em
  HTML.

## Substituição (item 5.2)

- É a emissão de uma **DPS com alteração** de uma ou mais informações de uma DPS já
  convertida em NFS-e, **informando a chave de acesso** da NFS-e existente. Com isso o
  sistema entende que é substituição e faz as validações próprias.
- A NFS-e original é **cancelada** por um **Evento de Cancelamento por Substituição**,
  que segue as regras de validação do cancelamento do anexo de leiaute.
- O emissor repete as informações da emissão e, ao final, mostra um **comparativo**
  entre a NFS-e original e a substituta.
- **Parâmetros definidos pelo município** (dúvidas vão ao município): se existe prazo
  máximo para substituir; qual é esse prazo em dias; se pode substituir NFS-e em que
  os não emitentes não foram identificados; se pode alterar os dados dos não emitentes
  na substituta.

## Cancelamento (item 5.3)

- Cancela a NFS-e por um **Evento de Cancelamento** (XML processado e vinculado à
  nota), conforme as regras do anexo de leiaute e os leiautes de eventos do Anexo II.
- O sistema mostra, recuperados: chave de acesso, número e série da DPS, número da
  NFS-e, data de geração, valor, município gerador, "emitido para" e serviço. O
  emitente informa o **motivo do cancelamento** (lista) e a **justificativa**
  (obrigatória).
- **Se o cancelamento não for possível** pelas regras do município, o sistema mostra
  um alerta; respondendo "SIM", a ação vira um evento de **Solicitação de
  Cancelamento de NFS-e por Análise Fiscal**, com motivo e justificativa, para o
  município analisar.
- Notas emitidas por decisão administrativa/judicial seguem o mesmo caminho
  ([[df-nfse-decisao-administrativa-judicial]]).

## Download

- **XML da NFS-e:** o emitente guarda cópia no próprio ambiente.
- **DANFSe:** PDF com a representação gráfica resumida da nota. O texto do guia, na
  seção 5.5, diz que o comando baixa "o modelo XML", mas o título e a descrição geral
  falam do PDF; trate o DANFSe como PDF. ⚠️ Divergência interna do guia.

## Consulta pública (seção 9)

Qualquer envolvido (prestador, tomador, órgão fiscalizador) pode consultar uma NFS-e
no site de **Consulta Pública de NFS-e**, com verificação **hCaptcha**. Duas formas:

### Pela chave de acesso

A chave tem **50 caracteres alfanuméricos**. Composição, conforme o guia:

| Parte | Conteúdo |
|---|---|
| Código do município | município do endereço do emitente (código IBGE) |
| Ambiente gerador | 1 = sistema próprio do município; 2 = Sefin Nacional NFS-e |
| Tipo de inscrição federal | 1 = CPF; 2 = CNPJ |
| Inscrição federal | se CPF, completar com `000` à esquerda |
| Número da NFS-e | sequencial do emitente |
| Ano/mês de emissão | ano e mês da emissão |
| Código numérico | 9 posições, aleatório, gerado pelo sistema |
| Dígito verificador | do código numérico |

### Pelos dados da DPS

Obrigatórios: CPF/CNPJ do emitente, **série da DPS**, **número da DPS** e município
de emissão. A série identifica a ordem de emissão das DPS e aparece no PDF ou no XML
da NFS-e.

## Ligações

- [[df-nfse-emissao-final-mei]]: a nota gerada e as ações iniciais.
- [[df-nfse-notas-recebidas-manifestacao]]: o lado do tomador.
- [[df-nfse-emissao-pessoas]]: número, série e conversão da DPS.
