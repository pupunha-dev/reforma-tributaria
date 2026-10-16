---
título: NFS-e Nacional — eventos da NFS-e (Anexo II v1.01-20260122): tipos e códigos, quem pode registrar, leiaute do pedido, motivos, ordem entre eventos e rejeições
dominio: documentos-fiscais
fontes: Anexo II — leiaute e regras de negócio dos eventos de NFS-e v1.01-20260122 (planilhas "Tipo Eventos", "Leiaute Evento", "RN Evento (PedRegEvento)", "RN EVENTOSxEVENTOS" e comentários); Guia do Emissor Público Nacional Web da NFS-e v1.2 (seção 5.3, para a tela); NT CGNFS-e 010 v1.00 (eventos da NFS-e Via têm anexo próprio, fora desta nota)
vigencia: atual
texto-base: 2026-10-16
---

# Eventos da NFS-e Nacional (Anexo II)

## A lógica em uma frase

Depois que a NFS-e existe, tudo o que acontece com ela (cancelar, substituir, pedir análise fiscal,
manifestar-se, bloquear por ofício) é um **evento** registrado e vinculado à **chave de acesso** da nota.
O **Anexo II** (nível de NT: documentação técnica nacional, abaixo da lei e dos regulamentos) diz
**quais eventos existem, quem os registra, como é o XML, em que ordem eles são aceitos e por que são
rejeitados**. A tela do emissor está em [[df-nfse-consulta-cancelamento-substituicao]]; os prazos e
valores-limite do cancelamento são **parametrizados pelo município** (matéria municipal, fora do
escopo; ver seção 5).

## 1. Os 16 tipos de evento

O código do evento tem **6 dígitos**: 1º = categoria; 2º e 3º = autor; 4º = ambiente receptor;
5º e 6º = número crescente dentro da categoria. Categorias: **1** cancelamentos, **2** manifestações,
**3** ofícios.

| Código | Evento | Autor (quem registra) | Ambiente receptor |
|---|---|---|---|
| 101101 | Cancelamento de NFS-e | emitente da NFS-e | 1 (sistema que gerou a NFS-e) |
| 105102 | Cancelamento de NFS-e por substituição | município emissor | 1 |
| 101103 | Solicitação de análise fiscal para cancelamento | emitente | 1 |
| 105104 | Cancelamento deferido por análise fiscal | município emissor | 1 |
| 105105 | Cancelamento indeferido por análise fiscal | município emissor | 1 |
| 202201 | Manifestação — confirmação do prestador | prestador | 2 (ADN) |
| 203202 | Manifestação — confirmação do tomador | tomador | 2 |
| 204203 | Manifestação — confirmação do intermediário | intermediário | 2 |
| 205204 | Manifestação — confirmação tácita | município de incidência | 1 e 2 |
| 202205 | Manifestação — rejeição do prestador | prestador | 2 |
| 203206 | Manifestação — rejeição do tomador | tomador | 2 |
| 204207 | Manifestação — rejeição do intermediário | intermediário | 2 |
| 205208 | Manifestação — anulação da rejeição | município de incidência | (não se lê na planilha) |
| 305101 | Cancelamento de NFS-e por ofício | município emissor | 1 |
| 305102 | Bloqueio de NFS-e por ofício | município emissor | 1 |
| 305103 | Desbloqueio de NFS-e por ofício | município emissor | 1 |

Autores no 2º e 3º dígitos: 01 emitente; 02 prestador; 03 tomador; 04 intermediário; 05 município
emissor. A legenda da planilha prevê ainda 06 município de incidência, 07 MAN (Módulo de Apuração
Nacional), 08 responsável tributário, 56 (emissor ou incidência), 67 (incidência ou MAN) e 99 CGNFS-e,
que nenhum dos 16 tipos usa hoje.

Outras colunas da planilha "Tipo Eventos":

- **A NFS-e precisa existir no ADN:** sim, para todos os tipos.
- **Evento único:** sim para todos, exceto **bloqueio e desbloqueio por ofício** (podem repetir).
- **Visibilidade** (quem enxerga o evento): cancelamento, substituição, manifestações e cancelamento por
  ofício = emitente, não emitente, consulta pública e administração tributária; solicitação de análise e
  deferido/indeferido = emitente, não emitente e administração tributária (sem consulta pública);
  bloqueio e desbloqueio = emitente e administração tributária.
- **Assinatura digital obrigatória no pedido:** "sim" no cancelamento e na solicitação de análise
  fiscal; "não" nas manifestações; "-" nos eventos do município. A regra E1989 (seção 5), porém,
  exige assinatura quando o pedido é enviado para o Web Service; as fontes não conciliam os dois
  textos.

> Estes são os eventos da **NFS-e comum**. A **NFS-e Via** tem eventos e leiautes próprios (cancelamento
> e manifestação do adquirente), descritos num anexo diferente que não está nas fontes ([[df-nfse-via]]).

## 2. Leiaute do pedido de registro (XML)

- Raiz `evento` (versão do leiaute) → `infEvento` com o **id do evento** (`"EVT"` + id do pedido sem o
  `"PRE"` + `nSeqEvento`, 62 posições), `verAplic`, `ambGer` (1 sistema próprio do município; 2 Sefin
  Nacional; 3 ADN), `nSeqEvento` (3 dígitos: `001` nos eventos que ocorrem uma vez, como o
  cancelamento; sequencial nos que podem repetir), `dhProc` (UTC) e `nDFSe`.
- Dentro, `pedRegEvento/infPedReg` com o **id do pedido** (`"PRE"` + **chave de acesso da NFS-e (50)** +
  **código do evento (6)** = 59 posições), `tpAmb` (1 produção; 2 homologação), `verAplic`, `dhEvento`,
  `CNPJAutor` **ou** `CPFAutor` (o procurador não é o autor; quando o autor é o fisco, vai o CNPJ da
  prefeitura e o CPF não pode ser preenchido), `chNFSe` (50) e o grupo específico `e` + código do evento.
- `Signature` (assinatura XML) no pedido e no evento.

Grupos específicos (campos além de `xDesc`, a descrição do evento):

| Evento | Campos |
|---|---|
| 101101 cancelamento | `cMotivo`: 1 erro na emissão, 2 serviço não prestado, 9 outros; `xMotivo` (15 a 255 caracteres) |
| 105102 substituição | `cMotivo` (copiado da DPS, `subst/cMotivo`): 01 desenquadramento do Simples Nacional, 02 enquadramento no Simples Nacional, 03 inclusão retroativa de imunidade/isenção, 04 exclusão retroativa de imunidade/isenção, 05 rejeição pelo tomador ou intermediário responsável pelo recolhimento, 99 outros; `xMotivo` (opcional); `chSubstituta` (chave da NFS-e substituta) |
| 101103 solicitação de análise fiscal | `cMotivo`: 1, 2 ou 9 (como no cancelamento); `xMotivo` |
| 105104 deferido | `CPFAgTrib` (agente municipal), `nProcAdm` (opcional), `cMotivo` = 1; `xMotivo` |
| 105105 indeferido | `CPFAgTrib`, `nProcAdm` (opcional), `cMotivo`: 1 indeferido, 2 indeferido sem análise de mérito; `xMotivo` |
| 202205, 203206, 204207 rejeições | `cMotivo`: 1 duplicidade, 2 NFS-e já emitida pelo tomador, 3 não ocorrência do fato gerador, 4 erro quanto à responsabilidade tributária, 5 erro quanto ao valor do serviço, às deduções, ao serviço prestado ou à data do fato gerador, 9 outros; `xMotivo` obrigatório se `cMotivo` = 9 (E1944, E1949, E1954) |
| 205208 anulação da rejeição | `CPFAgTrib`, `idEvManifRej` (id do evento de rejeição anulado; tem que existir e ser da mesma NFS-e: E1963), `xMotivo` |
| 305101 cancelamento por ofício | `CPFAgTrib`, `nProcAdm` (obrigatório), `xProcAdm` (15 a 255) |
| 305102 bloqueio por ofício | `CPFAgTrib`, `codEvento` (qual tipo de cancelamento fica bloqueado: 101101, 105102, 105104, 105105 ou 305101), `xMotivo` |
| 305103 desbloqueio por ofício | `CPFAgTrib`, `idBloqOfic` (id do bloqueio que está sendo desfeito) |

As confirmações (202201, 203202, 204203, 205204) só têm a descrição (`xDesc`).

## 3. Ordem entre eventos (planilha "RN EVENTOSxEVENTOS")

Para cada pedido recebido, o sistema olha **os eventos que a NFS-e já tem** e aceita (V) ou rejeita (X).
Em resumo, conforme a matriz:

- **NFS-e sem evento:** aceita cancelamento, substituição, solicitação de análise, as manifestações,
  cancelamento por ofício e bloqueios. **Não** aceita deferido/indeferido (precisam de solicitação
  pendente) nem desbloqueio (precisa de bloqueio).
- **Depois de cancelamento, substituição, deferido ou cancelamento por ofício:** a matriz marca
  **X para todos** os pedidos seguintes; a nota está encerrada.
- **Com solicitação de análise pendente:** aceita deferido, indeferido, manifestações e bloqueios;
  **não** aceita novo cancelamento, nova substituição, nova solicitação nem cancelamento por ofício.
- **Depois de indeferido:** não aceita cancelamento, substituição, nova solicitação nem novo
  deferido/indeferido; aceita manifestações e ofício.
- **Manifestações:** o V ou X depende de quem é o **emitente** (as células trazem a nota "X se o
  prestador/tomador/intermediário for o emitente; V se for o não emitente"): só o **não emitente**
  manifesta, **uma vez por não emitente** (E1833). A anulação da rejeição só é aceita para uma
  rejeição ainda não anulada, e **uma anulação por rejeição** (E1835).
- **Bloqueio por ofício:** vale **por tipo de evento bloqueado**. Um novo bloqueio para o mesmo tipo só
  entra se o anterior já foi desbloqueado. Com um bloqueio ativo, o pedido do tipo bloqueado (por
  exemplo um cancelamento) fica rejeitado; só é aceito se houver desbloqueio. O desbloqueio é aceito
  **somente se houver bloqueio pendente** e se corresponder exatamente ao id do bloqueio (E1976, E1978).

A matriz completa (24 colunas de pedidos × 25 linhas de situação) está no arquivo
`fontes/documentos-fiscais/texto/anexo-ii-rn-eventosxeventos.tsv`; consulte-a para um par específico em vez
de deduzir.

## 4. Rejeições por tipo de pedido (RN do PedRegEvento)

Cada tipo de evento tem uma regra "o Sistema Nacional não pode recepcionar o evento X pois o evento Y
já está vinculado à NFS-e", todas ligadas à matriz da seção 3: E0840 cancelamento; E0845 substituição;
E0848 solicitação de análise; E0852 deferido; E0855 indeferido; E0860 a E0870 manifestações (E0860
confirmação do prestador, E0861 do tomador, E0862 do intermediário, E0863 tácita, E0864, E0866 e E0868
rejeições, E0870 anulação); E1960 cancelamento por ofício; E1965 bloqueio; E1970 desbloqueio. À parte,
**E0853 e E0856** rejeitam deferido e indeferido quando **não há solicitação de análise pendente**.

## 5. Outras regras de rejeição do pedido

| Regra | O que verifica |
|---|---|
| E1260 / E1825 | versão do leiaute do evento / do pedido com prazo de aceitação vencido |
| E1802 / E1827 | `id` do evento (EVT) e `id` do pedido (PRE) diferentes da concatenação do leiaute |
| E1805 / E0802 | já existe evento com o mesmo id no ADN |
| E1274 | `ambGer` fora de 1 (sistema próprio) ou 2 (Sefin Nacional) |
| E1278 / E1843 | `dhProc` anterior ou igual ao recebimento / `dhEvento` não posterior ao recebimento |
| E1845 | ambiente do pedido diferente do ambiente de recebimento |
| E0812 / E0815 | o CNPJ (só a base) ou o CPF do autor tem que ser o do certificado da assinatura |
| E0813 / E0816 | o autor tem que ser o previsto na planilha "Tipo Eventos" para aquele evento |
| E1831 | a NFS-e (`chNFSe`) não existe no ADN |
| E0831 | o pedido tem que ir ao ambiente que gerou a NFS-e |
| E0822 / E0823 / E0824 / E0827 | cancelamento fora do **prazo**, acima do **valor** permitido, de NFS-e **sem tomador identificado** ou com evento de tributos recolhidos vinculado: todos "conforme parametrização do município" (regras de nível 3, municipais; os parâmetros não estão nas fontes) |
| E1818 | o município **não pode compartilhar** com o ADN as manifestações de confirmação ou rejeição dos não emitentes (202201, 203202, 204203, 202205, 203206, 204207): esses eventos "devem ser emitidos pelos não emitentes diretamente no SEFIN NFS-e" |
| E1980 a E1991 | assinatura do **pedido**: válida, certificado dentro da validade e da cadeia ICP-Brasil, tipo e extensões de CNPJ/CPF corretos, obrigatória no Web Service e feita com o certificado do emitente do pedido |
| E2020 a E2032 | assinatura do **evento**: as mesmas conferências, e feita com o certificado do **município emissor** |

## O que não está nas fontes

- Os **parâmetros municipais** do cancelamento (prazo, valor-limite, exigência de tomador): são do
  município e não constam do Anexo II.
- A **data de entrada em produção** do Anexo II v1.01-20260122; o manual da API de 2025 menciona o
  Anexo II, mas não fixa data para esta versão.
- Como a tela do emissor escolhe o motivo entre as opções acima: o guia só descreve a tela
  ([[df-nfse-consulta-cancelamento-substituicao]]).
