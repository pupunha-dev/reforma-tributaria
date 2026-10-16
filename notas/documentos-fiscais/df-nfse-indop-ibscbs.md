---
título: NFS-e Nacional — código indicador da operação (cIndOp, Anexo VII): os 40 códigos, o que significam e onde incide o IBS/CBS
dominio: documentos-fiscais
fontes: Anexo VII — IndOp_IBSCBS v1.03.00 (planilha "cIndOp Public"); NT CGNFS-e 004 v2.00 (10/12/2025), NT CGNFS-e 005 v1.0 (19/11/2025), NT CGNFS-e 007 v1.0 (07/02/2026) e NT CGNFS-e 009 v1.01 (11/09/2026), que citam as versões 1.00.00, 1.01.00 e 1.02.01 do anexo; Anexo VIII v1.01.00 e regras do Anexo I v1.01 e do Anexo VI v1.04.01 (E0932, E0928, E0938); LC 214/2025, art. 11 (conferido em fontes/reforma/texto); Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seção 4.1.2
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# Código indicador da operação (`cIndOp`)

## A lógica em uma frase

O `cIndOp` diz **em qual hipótese do art. 11 da LC 214/2025 a operação se enquadra** e,
com isso, **qual endereço da NFS-e define o local de incidência do IBS/CBS**. O código tem
6 posições e vem da tabela do **Anexo VII** do leiaute. A tela onde ele é escolhido está em
[[df-nfse-emissao-servico]]; a regra de local da operação, em [[ibs-cbs-local-operacao]].

> **Nível e vigência.** O Anexo VII é documentação técnica (nível NT): organiza a lei, não
> a altera. A versão usada aqui é a **1.03.00**; as NTs citam versões anteriores (1.00.00 nas
> NTs 004 e 005, 1.01.00 na NT 007 e 1.02.01 na NT 009 v1.01) e nenhuma NT em mãos cita a 1.03.00.
> O guia da NFS-e (27/07/2026) e o Anexo I v1.01 (regra E0932) citam só os códigos 020101, 020201 e
> 020301 como ligados a imóveis; o Anexo VI (E0932) acrescenta 020202 e 020401, e o anexo traz também
> 020102 ([[df-nfse-regras-ibscbs-anexo-vi]]). O campo `cIndOp` é obrigatório (1-1,
> 6 posições) **dentro** do grupo `IBSCBS` da DPS; o grupo em si é 0-1, e a NT CGNFS-e 004 v2.00
> suspendeu no início de 2026 a validação que exige o grupo ([[df-nfse-cgnfse-notas-tecnicas]]).

## Como ler a tabela

- **Documento** (colunas `indNFe`, `indNFSe`, `indNFSe Via` da planilha): quais documentos
  usam o código. **28 códigos** estão marcados para a **NFS-e**; `080101` (exploração de
  via) para a **NFS-e Via** ([[df-nfse-via]]); `010104` e `010105` para a **NF-e**; os
  outros 9 (`010201`, `010202`, `090101`, `090102`, `110101`, `110201`, `120101`, `130101`
  e `130201`) **não têm marca em nenhum documento** nessa versão.
- **Local de incidência do IBS na NFS-e** (coluna `NFSeLocIncidIBS`): qual dado da NFS-e
  dá o local da operação. É o que alimenta `cLocalidadeIncid` na NFS-e
  ([[df-nfse-layout-ibscbs]]).
- **Dispositivo:** o inciso do art. 11 da LC 214/2025 que sustenta o código. Os incisos
  II a IX e X estão em [[ibs-cbs-local-operacao]]: o inciso **X** é a regra residual
  ("bem ou serviço não abrangido pelos demais incisos"): em operação **onerosa**, o
  domicílio principal do **adquirente** residente no País (X, a, 1) ou, se o adquirente
  não é residente no País, o do **destinatário** residente no País (X, a, 2); em
  operação **não onerosa**, o do destinatário residente no País (X, b).
- Os textos da coluna "Observação" que remetem ao **art. 12 do Decreto 12.955/2026 e da
  Res. CGIBS 6/2026** estão em notas após a tabela.

## Tabela dos códigos (Anexo VII v1.03.00)

| Código | Tipo de operação | Característica do fornecimento | Local do fornecimento (a identificar no DF-e) | Dispositivo (LC 214/2025) | Documento (colunas indNFe / indNFSe / indNFSe Via) | Local de incidência do IBS na NFS-e |
|---|---|---|---|---|---|---|
| `010101` | Bem Móvel Material | Presencial, com retirada no estabelecimento do fornecedor | Estabelecimento do fornecedor como o local da entrega ou disponibilização do bem ao destinatário | Art. 11, I | NFS-e | Estabelecimento do Prestador/Fornecedor |
| `010102` | Bem Móvel Material | Presencial, com retirada fora do estabelecimento do fornecedor | Local da realização da operação e sua retirada | Art. 11, I | NFS-e | Local da Prestação |
| `010103` | Bem Móvel Material | Não presencial, com entrega ou disponibilização em endereço fornecido | Endereço do destinatário fornecido para entrega ou disponibilização (assim considerado o destino final indicado pelo adquirente) | Art. 11, I e §1º, I | NFS-e | Endereço do Destinatário |
| `010104` | Bem Móvel Material | Licitação promovida pelo poder público de bem apreendido ou abandonado ou leilão judicial | Local onde se encontra o bem móvel material | Art. 11, I e §1º, III, "a" | NF-e | - |
| `010105` | Bem Móvel Material | Constatação de irregularidade pela falta de documentação fiscal ou pelo acobertamento por documentação inidôneo | Local onde se encontra o bem móvel material (Local da retirada) | Art. 11, I e §1º, III, "b" | NF-e | - |
| `010106` | Bem Móvel Material | Locação de bem móvel material em aquisições realizadas de forma centralizada por contribuinte sujeito ao regime regular do IBS e da CBS que possui mais de um estabelecimento e que não estejam sujeitas a vedação à apropriação de créditos | Local do domicílio principal do adquirente (estabelecimento matriz) | Art. 11, I e §4º | NFS-e | Endereço do Tomador/Adquirente |
| `010201` | Aquisição de veículo automotor terrestre, aquático ou aéreo | Entrega ou disponibilização do bem | Domicílio principal do destinatário | Art. 11, I e §1º, II | — | - |
| `010202` | Aquisição de veículo automotor em licitação promovida pelo poder público de bem apreendido ou abandonado ou leilão judicial | Entrega ou disponibilização do bem | Domicílio principal do destinatário | Art. 11, I e §1º, II | — | - |
| `020101` | Operação com bem imóvel, bem móvel imaterial, inclusive direito, relacionada a bem imóvel | Realização de operações com bem imóvel, bem imaterial, inclusive direito, relacionado a bem imóvel | Localidade do imóvel | Art. 11, II e §2º | NFS-e | Localidade do Imóvel |
| `020102` | Operação com bem imóvel, bem móvel imaterial, inclusive direito, relacionada a Bem Imóvel de Características Especiais (BICE) | Realização de operações com bem imóvel, bem imaterial, inclusive direito, relacionado a bem imóvel de Características Especiais (BICE) | Localidade do imóvel (BICE) | Art. 11, II e §2º | NFS-e | Localidade do Imóvel |
| `020201` | Serviço prestado fisicamente sobre bem imóvel | Execução de serviços diversos prestados fisicamente sobre bem imóvel | Localidade do imóvel | Art. 11, II e §2º | NFS-e | Localidade do Imóvel |
| `020202` | Serviço prestado fisicamente sobre bem imóvel | Execução de serviços sobre Bens Imóveis de Características Especiais (BICE) | Localidade do imóvel (BICE) | Art. 11, II e §2º | NFS-e | Localidade do Imóvel |
| `020301` | Serviço de administração e intermediação de bem imóvel | Execução dos serviços de administração e intermediação de bens imóveis | Localidade do imóvel | Art. 11, II e §2º | NFS-e | Localidade do Imóvel |
| `020401` | Serviços de locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza (quando caracterize operação tributável pelo ISSQN) | Execução de serviços sobre Bens Imóveis de Características Especiais (BICE) | Localidade do imóvel (BICE) | Art. 11, II e §2º | NFS-e | Localidade do Imóvel |
| `030101` | Serviço prestado fisicamente sobre a pessoa ou fruído presencialmente por pessoa física | Execução de serviços diversos exclusivamente prestados fisicamente sobre a pessoa ou integralmente fruídos presencialmente por pessoa física | Estabelecimento do fornecedor como local da prestação | Art. 11, III | NFS-e | Estabelecimento do Prestador/Fornecedor |
| `030102` | Serviço prestado fisicamente sobre a pessoa ou fruído presencialmente por pessoa física | Execução de serviços diversos exclusivamente prestados fisicamente sobre a pessoa ou integralmente fruídos presencialmente por pessoa física | Local da prestação do serviço diverso do estabelecimento do fornecedor | Art. 11, III | NFS-e | Local da Prestação |
| `040101` | Serviço de planejamento, organização e administração de feiras, exposições, congressos, espetáculos, exibições e congêneres | Execução de serviços de planejamento, organização e administração de feiras, exposições, congressos, espetáculos, exibições e congêneres | Local do evento a que se refere o serviço | Art. 11, IV | NFS-e | Local do Evento |
| `050101` | Serviço prestado fisicamente sobre bem móvel material | Execução de serviços diversos prestados fisicamente sobre bem móvel material | Estabelecimento do fornecedor como local da prestação | Art. 11, V | NFS-e | Estabelecimento do Prestador/Fornecedor |
| `050102` | Serviço prestado fisicamente sobre bem móvel material | Execução de serviços diversos prestados fisicamente sobre bem móvel material | Local da prestação do serviço diverso do estabelecimento do fornecedor | Art. 11, V | NFS-e | Local da Prestação |
| `050201` | Serviços portuários | Execução de serviços portuários | Local do porto como local da prestação | Art. 11, V | NFS-e | Local da Prestação |
| `060101` | Serviço de transporte de passageiros | Execução de serviços de transporte de passageiros | Local de início do transporte | Art. 11, VI | NFS-e | Local da Prestação (Início do Transporte) |
| `070101` | Serviço de transporte de carga | Execução de serviço de transporte de carga | Endereço fornecido para entrega do bem | Art. 11, VII | NFS-e | Local da Prestação |
| `070102` | Serviço de transporte de carga | Execução de serviço de transporte de carga | Local da retirada do bem | Art. 11, VII | NFS-e | Local da Prestação (Local da Retirada) |
| `080101` | Serviço de exploração de via | Execução de serviços de exploração de via | Local da prestação correspondente à extensão da via explorada, proporcionalmente ao território dos entes tributantes | Art. 11, VIII | NFS-e Via | Localização do Trecho (NFS-e Via) |
| `090101` | Serviço de telefonia fixa e demais serviços de comunicação prestados por meio de cabos, fios, fibras e meios similares | Execução de serviços de telefonia fixa e demais serviços de comunicação prestados por meio de cabos, fios, fibras e meios similares | Local de instalação do terminal | Art. 11, IX | — | - |
| `090102` | Serviço de telefonia fixa e demais serviços de comunicação prestados por meio de cabos, fios, fibras e meios similares | Execução de serviços de telefonia fixa e demais serviços de comunicação prestados por meio de cabos, fios, fibras e meios similares | Local do domicílio principal do adquirente (assim considerada a matriz), nas aquisições realizadas de forma centralizada por contribuinte sujeito ao regime regular do IBS e da CBS que possui mais de um estabelecimento e que não estejam sujeitas a vedação à apropriação de créditos | Art. 11, IX e §4º, I e II | — | - |
| `100101` | Cessão de espaço para prestação de serviços publicitários, em operações onerosas | Realização de operações de cessão de espaço para prestação de serviços publicitários | Local do domicílio principal do adquirente residente ou domiciliado no País. Nas aquisições indicadas no art. 11, §4º, II, considera-se domicílio principal do adquirente o estabelecimento matriz | Art. 11, X, "a", 1 e §º 11 | NFS-e | Endereço do Tomador/Adquirente |
| `100102` | Cessão de espaço para prestação de serviços publicitários, em operações onerosas | Realização de operações de cessão de espaço para prestação de serviços publicitários | Local do domicílio principal do destinatário residente ou domiciliado no País, caso o adquirente não seja residente ou domiciliado no País | Art. 11, X, "a", 2 e §º11 | NFS-e | Endereço do Destinatário |
| `100201` | Cessão de espaço para prestação de serviços publicitários, em operações não onerosas | Realização de operações de cessão de espaço para prestação de serviços publicitários | local do domicílio principal do destinatário residente ou domiciliado no País | Art. 11, X, "b" e §º11 | NFS-e | Endereço do Destinatário |
| `100301` | Demais serviços, em operações onerosas | Execução dos demais serviços em operações não especificadas em outros indicadores ou, nos serviços de que trata o inc. III do art. 11, esses sejam, ainda que parcialmente, prestados à distância | Local do domicílio principal do adquirente residente ou domiciliado no País. Nas aquisições indicadas no art. 11, §4º, II, considera-se domicílio principal do adquirente o estabelecimento matriz | Art. 11, X, "a", 1 e §§4º, II e 5º | NFS-e | Endereço do Tomador/Adquirente |
| `100302` | Demais serviços, em operações onerosas | Execução dos demais serviços em operações não especificadas em outros indicadores ou, nos serviços de que trata o inc. III do art. 11, esses sejam, ainda que parcialmente, prestados à distância | Local do domicílio principal do destinatário residente ou domiciliado no País, caso o adquirente não seja residente ou domiciliado no País | Art. 11, X, "a", 2 e §º5 | NFS-e | Endereço do Destinatário |
| `100401` | Demais serviços, em operações não onerosas | Execução dos demais serviços em operações não especificadas em outros indicadores ou, nos serviços de que tratam o inc. III, estes sejam, ainda que parcialmente, prestados à distância | local do domicílio principal do destinatário residente ou domiciliado no País | Art. 11, X, "b" e §º5 | NFS-e | Endereço do Destinatário |
| `100501` | Demais bens, em operações onerosas | Realização de demais operações com bens não especificadas em outros indicadores | Local do domicílio principal do adquirente residente ou domiciliado no País. Nas aquisições indicadas no art. 11, §4º, II, considera-se domicílio principal do adquirente o estabelecimento matriz | Art. 11, X, "a", 1 e §4º, II | NFS-e | Endereço do Tomador/Adquirente |
| `100502` | Demais bens, em operações onerosas | Realização de demais operações com bens não especificadas em outros indicadores | Local do domicílio principal do destinatário residente ou domiciliado no País, caso o adquirente não seja residente ou domiciliado no País | Art. 11, X, "a", 2 | NFS-e | Endereço do Destinatário |
| `100601` | Demais bens, em operações não onerosas | Realização de demais operações com bens não especificadas em outros indicadores | local do domicílio principal do destinatário residente ou domiciliado no País | Art. 11, X, "b" | NFS-e | Endereço do Destinatário |
| `110101` | Operações com abastecimento de água, gás canalizado e energia elétrica | Operações destinadas a consumo | Local da entrega ou disponibilização | Art. 11, §7º, I | — | - |
| `110201` | Operações com abastecimento de água, gás canalizado e energia elétrica | Operações que não envolvam efetivo consumo: a) no fornecimento de serviços de transmissão de energia elétrica; e b) nas demais operações, inclusive nas hipóteses de geração, distribuição ou comercialização de energia elétrica. | Local do estabelecimento principal do adquirente (assim considerada a matriz), conforme §4º do art. 11 | Art. 11, §7º, II | — | - |
| `120101` | Nas aquisições de energia elétrica realizadas de forma multilateral | Disponibilização de energia elétrica | Local do estabelecimento do agente ou de seus representados que figurem na posição devedora da liquidação financeira apurada pela Câmara de Comercialização de Energia Elétrica | Art. 11, §9º | — | - |
| `130101` | Operações de transporte dutoviário de gás natural | Execução do transporte dutoviário de gás natural, na contratação de capacidade de entrada de gás natural do duto, nos termos da legislação aplicável | Local do estabelecimento principal do fornecedor | Art. 11, §10, I | — | - |
| `130201` | Operações de transporte dutoviário de gás natural | Execução do transporte dutoviário de gás natural, na contratação de capacidade de saída do gás natural do duto | Local do estabelecimento principal do adquirente | Art. 11, §10, II | — | - |

## Observações da planilha

- **Locação de bem móvel** (`010101` a `010103`, `010106`): a locação, o arrendamento e a
  cessão temporária do bem **incluem-se como operações com bens**, conforme art. 3º, §3º,
  da LC 214/2025.
- **Veículo em licitação ou leilão** (`010202`): domicílio principal do destinatário,
  conforme art. 12, §15, do Decreto 12.955/2026 e art. 12, §15, da Res. CGIBS 6/2026.
- **Serviço notarial e de registro** (`030101` e `030102` quando fruído **presencialmente**;
  `100301`, `100302` e `100401` quando **não** fruído presencialmente): art. 12, §11, do
  Decreto 12.955/2026 e da Res. CGIBS 6/2026.
- **Serviço em porto seco e aeroporto** (`050101` e `050102`): local da prestação, conforme
  art. 12, §12, do Decreto 12.955/2026 e da Res. CGIBS 6/2026.
- **Subitem 03.04 da LC 116/2003** (`020401`): locação, sublocação, arrendamento, direito de
  passagem ou permissão de uso de ferrovia, rodovia, postes, cabos, dutos e condutos,
  **quando caracterize operação tributável pelo ISSQN** (o ISSQN em si é matéria municipal,
  fora do escopo).
- **Aquisições centralizadas:** em `010106` e `090102` a planilha descreve a hipótese
  (contribuinte do regime regular com mais de um estabelecimento, em aquisições sem vedação
  à apropriação de créditos): o local é o domicílio principal do adquirente, a **matriz**
  (art. 11, §4º). Em `100101`, `100301` e `100501` a planilha remete às "aquisições
  indicadas no art. 11, §4º, II", em que o domicílio principal é o **estabelecimento matriz**.
- **Demais serviços** (`100301`, `100302`, `100401`): é o código residual dos serviços em
  que a operação não se enquadra em outro indicador **ou** em que os serviços do inciso III
  do art. 11 (prestados fisicamente sobre a pessoa física) são prestados, **ainda que
  parcialmente, à distância**.

## O que a tabela não responde

- **Adquirente e destinatário ambos no exterior:** nenhum código descreve esse caso (os
  códigos `10xxxx` pressupõem adquirente ou destinatário residente no País). A exportação de
  serviço, em si, está em [[ibs-cbs-exportacao]] e [[df-nfse-comercio-exterior]]; qual
  `cIndOp` usar nesse caso **não está nas fontes**.
- **Qual código escolher por NBS:** o Anexo VIII (correlação entre item da NBS, `cIndOp` e
  cClassTrib), citado pela NT CGNFS-e 004 v2.00 como "norteador" (trabalho inicial, sem regras de
  negócio para os grupos `IBSCBS`), **está nas fontes** (v1.01.00): [[df-nfse-correlacao-nbs-indop]]
  e as seis notas por item. Ele lista, por item e NBS, os códigos usados; só 19 dos 40 códigos
  aparecem nele, e a escolha no caso concreto continua dependendo dos fatos.
- **A tabela não escolhe o código:** ela organiza os códigos por hipótese do art. 11. Qual
  hipótese se aplica depende dos fatos da operação (por exemplo, se o serviço é prestado
  fisicamente sobre bem imóvel, inciso II, ou se cai na regra residual do inciso X). A nota
  não decide pelo contribuinte.
