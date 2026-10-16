---
título: NFS-e Via (exploração de via, pedágio) — layout, eventos de cancelamento e de manifestação do adquirente (NTs CGNFS-e 006, 007 e 010)
dominio: documentos-fiscais
fontes: NT CGNFS-e 006 v1.00 (22/01/2026; layout NFS-e Via v1.00); NT CGNFS-e 010 v1.00 (11/09/2026; layout v1.01 e evento de manifestação do adquirente); NT CGNFS-e 007 v1.0 (07/02/2026), seção 3.c; NT CGNFS-e 004 v2.00 (10/12/2025), seção 1.3; LC 214/2025, art. 11, VIII (conferido em fontes/reforma/texto)
vigencia: atual
texto-base: 2026-10-16
---

# NFS-e Via: nota fiscal de exploração de via

## A lógica em uma frase

A **NFS-e Via** é um **documento fiscal próprio** da NFS-e Nacional, de uso das
**concessionárias de rodovias** (serviço de exploração de via mediante pedágio): a nota é gerada
a cada **passagem de veículo**, enviada a um **ambiente nacional próprio** e validada de forma
**síncrona**; o local da operação é o **trecho da concessão**. Não é a NFS-e comum: tem layout,
chave e eventos próprios. Está fora do passo a passo do emissor Web
([[df-nfse-visao-geral]]).

## Base normativa e prazo

- A **Resolução CGNFS-e nº 9** (publicada no DOU em **30/12/2025**) instituiu o modelo da NFS-e
  Via como parte do Sistema Nacional da NFS-e. A resolução **não está nas fontes**: a NT 006 a
  cita. A NT 006 "ratifica" a documentação publicada em 23/12/2025 e divulga a **primeira versão
  do layout** (1.00), em parceria com as concessionárias, com base na LC 116/2003 e na LC 214/2025;
  o novo padrão vigora a partir de **1º/01/2026**.
- **Contingência:** a emissão das NFS-e Via relativas às operações realizadas em **janeiro de
  2026** foi admitida **até 31/01/2026**, em caráter excepcional, no início da obrigatoriedade.
- **Piloto e homologação:** a NT 004 v2.00 diz que o piloto, iniciado em agosto de 2025, foi
  concluído e o ambiente de produção restrita seria liberado a todas as concessionárias.
- O documento só serve ao serviço do código de tributação **22.01.01** (exploração de rodovia
  mediante cobrança de preço ou pedágio), que inclui conservação, manutenção, melhoramentos,
  operação, monitoração e assistência aos usuários.

## Como o processo funciona (NT 006, seção 1)

1. A concessionária **cadastra no Portal de Gestão das Concessionárias**: contratos, trechos,
   praças de cobrança, municípios e alíquotas.
2. Com esse cadastro o sistema define a **alíquota efetiva por trecho** usada no layout.
3. O emissor gera a nota em **XML** e a transmite ao Ambiente Nacional.
4. O Ambiente Nacional **valida arquivo e conteúdo de forma síncrona** e responde na hora.
5. As APIs de recepção recebem a nota e os eventos de **cancelamento e substituição**; as APIs
   de consulta permitem achar o resultado por protocolo ou chave e consultar a alíquota efetiva
   por trecho.

## Layout 1.00 (NT 006) e 1.01 (NT 010)

Raiz `NFSeVia/infNFSeVia`. Principais campos:

| Campo | O que é |
|---|---|
| `ID` | 53 posições: "VIA" + código da localidade/trecho (7) + ambiente gerador (1) + inscrição federal (14) + número (13) + série (3) + ano/mês (4) + código numérico (7) + DV (1) |
| `cStat` | 100 NFS-e Via gerada; 101 NFS-e Via de substituição gerada; 102 NFS-e Via de decisão judicial |
| `dhEmi`, `dhCompet` | data/hora da emissão e da competência (a competência é a da **passagem veicular**) |
| `subst` | `chSubstda` (chave da nota substituída) e `cMotivo`: 03 inclusão retroativa de imunidade/isenção; 04 exclusão retroativa; 05 rejeição pelo tomador ou intermediário responsável pelo recolhimento; 06 alteração de parâmetros do trecho; 07 erro na identificação do veículo; 99 outros (com `xMotivo`, 15 a 255 caracteres) |
| `fornec` | a **concessionária**: CNPJ, nome e município |
| `serv/cLocOper` | código IBGE do **trecho da concessão** (local da operação e de incidência; para IBS e CBS é o mesmo local de incidência do ISSQN); `xLocOper` é o nome do trecho |
| `cPracaEmi`, `xPracaEmi`, `kmPracaEmi`, `cLocEmi`, `xLocEmi` | praça de pedágio (código, nome, quilômetro) e município da praça |
| `nNFSeVia`, `serie` | número sequencial por praça e equipamento; uma série por praça, equipamento ou pista |
| `serv/cTribNac` | **valor fixo 220101** |
| `serv/cNBS` | **valor fixo 106042100** |
| `explVia/categVeic` | 00 não informada; 01 automóvel/caminhonete/furgão (2 eixos); 02 caminhão leve, ônibus, caminhão-trator e furgão (2 eixos); 03 automóvel/caminhonete com semirreboque (3 eixos); 04 caminhão, caminhão-trator e ônibus (3 eixos); 05 automóvel/caminhonete com reboque (4 eixos); 06 a 10 caminhão com reboque ou caminhão-trator com semirreboque (4, 5, 6, 7 e 8 eixos); 11 motocicletas, motonetas e bicicletas motorizadas; 12 veículo com gratuidade; 99 cobrança especial |
| `explVia/placa`, `sentido`, `codAcessoPed`, `modPassagem`, `codContrato`, `xInfComp` | placa (até 10), orientação de passagem em graus (0 a 359, precisão mínima de 10), código de acesso gerado pelo emissor (17), modalidade da passagem (1 fluxo livre; 2 manual; 3 automático; 4 semiautomático; 5 outros), código do contrato (4) e campo livre (até 2000) |
| `valores/modPagamento` | 1 débito ou pix; 2 crédito; 3 dinheiro; 4 eletrônico; 5 pagamento posterior; **6 sem cobrança** (incluído pela NT 010, layout 1.01) |

**Tributos no layout:**

- **ISSQN:** `vBC = vServ − descIncond`; `pAliq` é a alíquota efetiva do cadastro do trecho;
  `vISSQN = vBC × pAliq`. A apuração do ISSQN é municipal e **fora do escopo** (ver abaixo).
- **PIS/COFINS:** lista de CST com os mesmos códigos 00 a 09 e mais **49 (operação sem cobrança)** e
  **98 (anulação)**; base, alíquotas e valores.
- **IBS/CBS (`ibscbs`):** **CST fixo 000**, **cClassTrib fixo 000002** e **`cindOp` fixo
  080101** (exploração de via, ver [[df-nfse-indop-ibscbs]]). Base:
  `vBC = vServ − descIncond − vISSQN − vPIS − vCOFINS` (2026) ou `vBC = vServ − descIncond −
  vISSQN` (2027 até 2032), pela data de competência.
  `vLiq = vServ − vDescIncond − vDescCond − (vISSQN + vPIS + vCOFINS)`.
  `vIBSUF = vBC × pAliqEfetUF`, `vIBSMun = vBC × pAliqEfetMun`, `vIBSTot = vIBSUF + vIBSMun`,
  `vCBS = vBC × pAliq` e `vTotNF = vLiq + vCBS + vIBSTot` (IBS e CBS "por fora").
  A alíquota efetiva do IBS vem do **trecho cadastrado**; a lei fixa que o local da operação de
  exploração de via é o território de cada Município e Estado, em proporção
  ([[ibs-cbs-local-operacao]], art. 11, VIII).

## Eventos da NFS-e Via

| Evento | Tag e código | Observações |
|---|---|---|
| **Cancelamento** | `e101101` (código 101101) | `cMotivo` = **2** (serviço não prestado) e `xMotivo` de 15 a 255 caracteres; ocorre uma vez (`nSeqEvento` = 001) |
| **Cancelamento por substituição** | `e105102` (código 105102) | `cMotivo` = **1** (erro na emissão), `chSubstituta` (chave da substituta) e `xMotivo` opcional |
| **Manifestação do adquirente — aceite** | `e203202` (código 203202) | NT 010: identifica o adquirente (`tpNi` 1 CPF ou 2 CNPJ, `CNPJCPF`, `xRazaoSocial`) |
| **Manifestação do adquirente — rejeição** | `e203204` (código 203204) | mesmos dados mais `cMotivo`: 1 NFS-e Via em duplicidade; 2 não ocorrência da passagem do veículo; 3 data da passagem; 4 categoria do veículo; 5 placa; 6 valor do serviço; 7 modo de pagamento; 8 valor das deduções; 99 outros (`xMotivoRejeita`, 15 a 55 caracteres) |

O identificador do evento é "EVT" + chave da NFS-e Via (50) + código do evento (6) + número
sequencial (3). Os grupos `infEventoMiaA` (aceite) e `infEventoMiaR` (rejeição) são
**mutuamente excludentes**. A NT 010 vem com o **Manual para Emissão da NFS-e Via v1.02** e o
Anexo IV da NFS-e Via (`LeiautesRN_ADN-SNNFSeVia_V1.00.04`, seis planilhas: nota, cancelamento e
manifestação, cada uma com layout e regras de negócio); esses arquivos **não estão nas fontes**. O
"Anexo IV" que as fontes têm (v1.00-20251216) é **outro documento**, sobre a distribuição de DF-e do ADN
([[df-nfse-adn-distribuicao]]); os eventos da NFS-e **comum** estão em [[df-nfse-eventos]].

## ISSQN e apuração (NT 007, seção 3.c)

A NT 007 manda manter **inalterada** a metodologia de apuração do ISSQN e os fluxos municipais
de arrecadação: as obrigações acessórias e o recolhimento seguem a legislação municipal
(matéria **fora do escopo** do projeto) até a implantação do **Módulo de Apuração Nacional
(MAN)**, de adesão voluntária pelos municípios. As NFS-e Via autorizadas no ambiente nacional
são **distribuídas a todos os municípios** dos trechos de concessão e os municípios **podem,
opcionalmente**, usá-las para apurar o ISSQN, se adaptarem a legislação local.

## O que não está nas fontes

- O texto da **Resolução CGNFS-e nº 9** e do Manual para Emissão da NFS-e Via.
- Como a concessionária que também presta outros serviços emite (a NFS-e Via é exclusiva do
  código 22.01.01).
- O tratamento tributário do IBS/CBS da concessão além do que o layout fixa: o CST 000 e o
  cClassTrib 000002 são valores **do layout**; a classificação está em [[df-tabela-cclasstrib]].
