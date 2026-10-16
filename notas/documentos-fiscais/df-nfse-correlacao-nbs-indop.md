---
título: NFS-e Nacional — Anexo VIII: correlação entre item da lista de serviços, NBS, cIndOp e cClassTrib (como ler, regra do inciso X, legenda)
dominio: documentos-fiscais
fontes: Anexo VIII — correlação item/NBS × IndOp × cClassTrib v1.01.00 (planilhas "tabela geral" e "REGRA inc. X"); Anexo VII v1.03.00; NT CGNFS-e 004 v2.00 (10/12/2025, seção 1.2, observação 1); NT CGNFS-e 009 v1.01; LC 214/2025, art. 11 (conferido em fontes/reforma/texto)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Anexo VIII: correlação item da lista × NBS × cIndOp × cClassTrib

## A lógica em uma frase

O Anexo VIII é uma **planilha de apoio** que diz, para cada **item da lista de serviços (LC 116)** e
para cada **NBS** ligada a ele, qual **código indicador da operação (`cIndOp`)** e qual **código de
classificação tributária (`cClassTrib`)** costumam ser usados na DPS. Ele responde "que código
escolho para este serviço?"; o significado dos códigos está em [[df-nfse-indop-ibscbs]] (cIndOp) e
em [[df-tabela-cclasstrib]] (cClassTrib).

## Nível, versão e o que a nota não afirma

- **Nível de NT** (documentação técnica nacional): abaixo da lei e dos regulamentos. Não cria
  tributo nem benefício. A versão em mãos é a **v1.01.00**, com o nome oficial
  `AnexoVIII-CorrelacaoItemNBSIndOpCClassTrib_IBSCBS` (nome citado pela NT 004 v2.00).
- **Como as NTs o tratam:** a NT CGNFS-e 004 v2.00 (10/12/2025, seção 1.2) diz que a tabela de
  correlações, "por se tratar de um trabalho inicial e ainda em desenvolvimento", **não ensejou
  regras de negócio** para os grupos `IBSCBS` e deve servir "apenas como um norteador" do
  preenchimento. Nenhuma NT em mãos diz que isso mudou para a v1.01.00. **Se a v1.01.00 passou a
  gerar rejeição não está nas fontes**: as regras de rejeição do grupo `IBSCBS` do Anexo VI
  ([[df-nfse-regras-ibscbs-anexo-vi]]) vinculam `cClassTrib` e `cIndOp` ao resultado da
  **Calculadora** de IBS/CBS (por exemplo E0859, E0860 e E0958), e não citam esta planilha.
- **A planilha não decide pelo contribuinte:** um mesmo serviço pode ter vários `cIndOp` e vários
  `cClassTrib` listados; qual vale depende dos fatos da operação (onde o serviço é prestado,
  quem é o adquirente, se há benefício). A nota só reproduz o que a planilha lista.
- **O local de incidência da planilha é um rótulo por família de código.** Na planilha a coluna
  "Local incidência IBS" tem células mescladas: ela repete o rótulo da primeira linha (por
  exemplo, `010102` e `010103` aparecem sob "Local da entrega ou da disponibilização", e `030102` sob
  "Local da prestação"). O local de cada código, para valer, é o da tabela do **Anexo VII**
  ([[df-nfse-indop-ibscbs]]); em caso de diferença, vale o Anexo VII.

## Tamanho da planilha (v1.01.00)

- 208 itens/subitens da lista (de 01.01 a 99.04.01) e 731 NBS distintas, em 1.521 linhas.
- Só **19 dos 40 códigos `cIndOp`** do Anexo VII aparecem nela: `010101`, `010102`, `010103`,
  `010106`, `020101`, `020201`, `020301`, `030101`, `030102`, `040101`, `050101`, `050102`,
  `050201`, `060101`, `070101`, `080101`, `100101`, `100301`, `100501`, além de uma linha
  sem código (o subitem `99.01.01`, "outros serviços sem a incidência de ISSQN e ICMS", sem NBS).
  Os demais (por exemplo `020102`, `020202`, `020401`, `070102`, `090101`) **não aparecem**.
- O código mais frequente é `100301` ("demais serviços, em operações onerosas"): 555 linhas,
  em 114 itens. Em seguida `020201` (serviço sobre bem imóvel; 227 linhas) e `050101`/`050102`
  (serviço sobre bem móvel material; 153 e 138 linhas).
- 28 códigos `cClassTrib` diferentes; o geral `000001` ("tributado integralmente") é o mais
  comum (863 linhas).

## A regra do inciso X (planilha "REGRA inc. X")

Para os códigos **`1001xx`** (cessão de espaço para serviços publicitários), **`1003xx`**
(demais serviços) e **`1005xx`** (demais bens), a tabela geral traz **só o código da operação
onerosa com adquirente no País** (`100101`, `100301`, `100501`). A segunda planilha diz como
trocar o código nos outros casos (art. 11, X, da LC 214/2025; ver [[ibs-cbs-local-operacao]]):

| Operação | Adquirente no País (coluna "ADQ EXTERIOR" = NÃO) | Adquirente no exterior (= SIM) |
|---|---|---|
| **Onerosa** (P/S onerosa = SIM) | publicidade `100101`; demais serviços `100301`; demais bens `100501` | `100102`, `100302`, `100502` (local: domicílio do **destinatário** no País) |
| **Não onerosa** (P/S onerosa = NÃO) | `100201`, `100401`, `100601` (local: domicílio do destinatário no País) | **sem código na planilha** |

Nas linhas desses códigos, a tabela geral preenche as colunas "PS ONEROSA?" e "ADQ EXTERIOR?"
com S e N (a variante-base). O último caso da matriz (operação não onerosa com adquirente no
exterior) está em branco. O Anexo VII também não tem código para o adquirente e o destinatário ambos no exterior
([[df-nfse-indop-ibscbs]]).

## Legenda dos cClassTrib que aparecem na planilha

Nomes como estão na planilha (a tabela oficial e a vigência de cada código estão em
[[df-tabela-cclasstrib]]).

| cClassTrib | Nome na planilha |
|---|---|
| `000001` | Situações tributadas integralmente pelo IBS e CBS |
| `011003` | Intermediação de planos de assistência à saúde |
| `200016` | Serviços de pesquisa e desenvolvimento por ICT |
| `200021` | Transporte público coletivo de passageiros ferroviário e hidroviário |
| `200025` | Serviços de educação do Prouni |
| `200026` | Locação de imóveis em zonas reabilitadas |
| `200027` | Operações de locação, cessão onerosa e arrendamento de bens imóveis |
| `200028` | Serviços de educação (Anexo II) |
| `200029` | Serviços de saúde humana (Anexo III) |
| `200037` | Serviços ambientais de conservação ou recuperação da vegetação nativa |
| `200038` | Insumos agropecuários e aquícolas (Anexo IX) |
| `200039` | Serviços e licenciamento ou cessão de direitos de produções nacionais artísticas (Anexo X) |
| `200040` | Serviços de comunicação institucional à administração pública |
| `200041` | Educação desportiva (art. 141, I) |
| `200042` | Educação desportiva (art. 141, II) |
| `200043` | Fornecimento à administração pública de serviços e bens relativos à soberania (Anexo XI) |
| `200044` | Segurança da informação e cibernética por sociedade com sócio brasileiro (Anexo XI) |
| `200045` | Projetos de reabilitação urbana de zonas históricas e áreas críticas |
| `200046` | Operações com bens imóveis |
| `200048` | Hotelaria, parques de diversão e parques temáticos |
| `200051` | Agências de turismo |
| `200052` | Serviços de profissões intelectuais |
| `400001` | Transporte público coletivo de passageiros rodoviário e metroviário |
| `820001` | Documento com informações de fornecimento de planos de assistência à saúde |
| `820002` | Documento com informações de fornecimento de planos de assistência funerária |
| `820003` | Documento com informações de planos de assistência à saúde de animais domésticos |
| `820006` | Documento com informações de fornecimento de serviços de exploração de via |
| `820007` | Documento com informações de fornecimento de serviços financeiros |

## Onde está cada item da lista

A planilha foi dividida em seis notas geradas por script (uma tabela por item, com NBS, descrição
da NBS, `cIndOp` e `cClassTrib`):

- Itens 01 a 06: [[df-nfse-correlacao-itens-01-06]]
- Item 07 (construção civil, obras e engenharia): [[df-nfse-correlacao-itens-07]]
- Itens 08 a 13: [[df-nfse-correlacao-itens-08-13]]
- Itens 14 a 16: [[df-nfse-correlacao-itens-14-16]]
- Itens 17 a 40: [[df-nfse-correlacao-itens-17-40]]
- Item 99 (códigos nacionais de uso especial: não incidência, bens imateriais, imóveis e bens
  móveis): [[df-nfse-correlacao-itens-99]]

Para achar a tabela de um item: o número antes do segundo ponto é o item (por exemplo, o
subitem 14.01 está em itens 14 a 16; o 17.01, em itens 17 a 40). As notas por item partem
do **item/subitem da lista**; a lista de códigos de 6 dígitos (cTribNac) que o emissor mostra
está em [[df-nfse-lista-servicos-ctribnac]].

## O que a planilha não responde

- **Descrição oficial de cada NBS:** a aba `LISTA.NBS_v2.0` do Anexo B v1.01-20260122 (1.210 entradas) contém as 731 NBS desta planilha; em 56 delas o texto da descrição difere em redação do que o Anexo VIII traz. Consulte `fontes/documentos-fiscais/texto/anexo-b-lista-nbs-v2-0.tsv`.
- **Qual código usar no caso concreto** quando há mais de um `cIndOp` ou `cClassTrib` por NBS.
- **Se o cClassTrib listado se aplica ao seu cliente:** os benefícios (saúde, educação, profissões
  intelectuais etc.) têm condições na lei; ver [[df-tabela-cclasstrib]] e as notas do domínio
  `reforma`.
- **Adquirente e destinatário no exterior** e **operação não onerosa com adquirente no exterior**
  (sem código; ver a regra do inciso X acima).
- **Alíquota e local de incidência do ISSQN:** matéria municipal, fora do escopo.
