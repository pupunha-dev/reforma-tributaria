---
título: NFS-e Nacional — as Notas Técnicas da SE/CGNFS-e (003 a 010): cronologia, o que cada uma muda, anexos e API
dominio: documentos-fiscais
fontes: NT CGNFS-e 003 v1.2 (04/07/2025); NT CGNFS-e 004 v2.00 (10/12/2025); NT CGNFS-e 005 v1.0 (19/11/2025); NT CGNFS-e 006 v1.00 (22/01/2026); NT CGNFS-e 007 v1.0 (07/02/2026); NT CGNFS-e 008 v1.02 (14/07/2026); NT CGNFS-e 009 v1.0 (04/06/2026); NT CGNFS-e 010 v1.00 (11/09/2026); Manual dos Contribuintes — API do Emissor Público Nacional (PDF de 06/10/2025; histórico interno lista só a v1.0 de 17/03/2025); Anexo I e Anexo VII (planilhas)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# As Notas Técnicas da SE/CGNFS-e (NFS-e Nacional)

## A lógica em uma frase

Quem manda na **NFS-e Nacional** é a **Secretaria-Executiva do Comitê Gestor da NFS-e
(SE/CGNFS-e)**, que publica **Notas Técnicas** numeradas (003 a 010 nas fontes) mais **anexos em
planilha** (leiaute, regras de negócio, tabelas). Elas dizem **como preencher e validar** a DPS e a
NFS-e: não criam nem alteram tributo (a lei é a LC 214/2025; ver [[ibs-cbs-documento-fiscal-regulamentacao]]).
**NT, anexos e tabelas** têm o **mesmo nível** (documentação técnica nacional); o **Guia do
Emissor** ([[df-nfse-visao-geral]]) é o nível **mais baixo**, só operacional. Não confundir com as
Notas Técnicas do **Projeto NF-e** (numeração "2025.002", "2026.007"), que tratam de NF-e e NFC-e:
[[df-visao-geral-reforma-nfe]].

> **Como ler duas NTs que tratam do mesmo campo:** vale a **mais nova** que o altera. A NT 009
> diz que "complementa ou ajusta" as anteriores; já as NTs 003, 004 (v2.00) e 005 dizem
> expressamente que "substituem as versões anteriores". **Atenção:** a ordem de publicação não é a
> ordem de implantação. A NT 004 v2.00 (10/12/2025) é **mais nova** que a NT 005 (19/11/2025),
> mas diz que as evoluções da NT 005 **não** entram em produção em janeiro de 2026 e serão
> implantadas depois, em data futura. Para saber o que vale **hoje**, veja "O que está em
> produção hoje?" abaixo. Se a nota técnica divergir de uma
> tabela oficial que ela manda usar (cClassTrib, CST), vale a tabela
> ([[df-tabela-cclasstrib]]). Em qualquer caso, **lei e regulamento prevalecem**.

## Cronologia

| NT e versão | Data | O que traz | Onde está |
|---|---|---|---|
| **003** v1.2 | 04/07/2025 | 3ª versão dos grupos IBS/CBS (DPS e NFS-e), com destinatário e adquirente; **substituída** pela 004 | histórico; não usar |
| **004** (1ª versão) | 19/08/2025 | 4ª versão do layout; citada pela NT 005 como a versão que iria a produção em jan/2026 | **texto não está nas fontes** |
| **005** v1.0 | 19/11/2025 | 5ª versão: `indDoacao`, `gEstornoCred`, `gPagAntecipado`, bens móveis (`gLocBensMoveis`), deduções de locação; **não** foi para produção em jan/2026 | [[df-nfse-layout-ibscbs]] |
| **004** v2.00 | 10/12/2025 | versão que entra em produção em **05/01/2026**; suspende a obrigatoriedade do grupo `IBSCBS`; remove o grupo `adq`; ambiente de teste em 10/12/2025; informa o piloto da NFS-e Via | [[df-nfse-layout-ibscbs]], [[df-nfse-via]] |
| **006** v1.00 | 22/01/2026 | **NFS-e Via** (Resolução CGNFS-e 9/2025): layout 1.00, cancelamento e contingência de janeiro/2026 | [[df-nfse-via]] |
| **007** v1.0 | 07/02/2026 | `indZFMALC`; PIS/COFINS (CST, `tpRetPisCofins`, retenções em `vRetCSLL`), em produção desde **09/02/2026**; novos códigos 99.xx; novos fatos geradores só no ambiente nacional; numeração e "pulos"; NFS-e Via e MAN | [[df-nfse-layout-ibscbs]] |
| **009** v1.0 | 04/06/2026 | consolida e ajusta: CNPJ alfanumérico, notas de ajuste, `vAjusteBC`, Simples Nacional, imóveis, bens móveis, pagamento vinculado | [[df-nfse-layout-ibscbs]] |
| **008** v1.02 | 14/07/2026 (v1.01: 30/06/2026) | **DANFSe v2.0** e suspensão da API de geração do DANFSe em 03/08/2026 | [[df-nfse-danfse]] |
| **010** v1.00 | 11/09/2026 | NFS-e Via: layout 1.01 (`modPagamento` 6 "sem cobrança") e evento de manifestação do adquirente | [[df-nfse-via]] |

(As NTs **001 e 002** — a 002 é de 28/02/2025 e é citada como versão anterior do layout — **não
estão nas fontes**.)

## O que está em produção hoje?

As fontes dizem com certeza só isto:

- **Desde 05/01/2026:** o layout da NT 004 v2.00 (grupo `IBSCBS` facultativo).
- **Desde 09/02/2026:** as mudanças de PIS/COFINS da NT 007 (produção e produção restrita).
- **Desde 1º/01/2026:** a NFS-e Via (layout 1.00); o layout 1.01 e o evento de manifestação
  vêm da NT 010 (11/09/2026), **sem data de produção** nas fontes.
- **Sem data nas fontes:** tudo o que vem **só** das NTs 005 e 009 (notas de ajuste,
  `vAjusteBC`, `gLocacao`, `gTribSN`, `gPgtoVinc`, CNPJ alfanumérico etc.) e o DANFSe v2.0.
  As NTs 004, 007 e 009 dizem que o **cronograma de implantação** seria publicado no
  portal da NFS-e; **ele não está nas fontes**.
- **Datas de obrigatoriedade para o contribuinte:** as do guia (03/08/2026 no regime regular;
  01/01/2027 para o Simples por fato gerador) vêm de documentação operacional; o **ato** que as
  fixa não está nas fontes ([[df-nfse-visao-geral]]).

Antes de afirmar que um campo "já vale", diga de qual NT ele vem e que o cronograma não está
nas fontes.

## Anexos citados pelas NTs

| Anexo | Conteúdo | Versão nas fontes |
|---|---|---|
| **I** — leiaute e regras de negócio da DPS/NFS-e | layout do XML, regras de rejeição (E0xxx), planilhas de exportação e de incidência por subitem | **cópia anterior ao RTC**: arquivo modificado em 09/09/2025, **sem o grupo `IBSCBS`**. A NT 004 v2.00 cita a versão "v1.00-20251210" (de 10/12/2025). As regras de comércio exterior estão em [[df-nfse-comercio-exterior]] |
| **IV** — leiautes RN ADN (NFS-e Via) | layout e regras da NFS-e Via e dos eventos | **não está nas fontes** |
| **VI** — LeiautesRN_RTC_IBSCBS | layout e regras de negócio do grupo `IBSCBS` da DPS e da NFS-e | **não está nas fontes** (NT 004 v2.00: v1.01.03; NT 005: v1.02.00; NT 007: v1.03.00; NT 009: v1.04.00) |
| **VII** — IndOp_IBSCBS | códigos do `cIndOp` | **v1.03.00**: [[df-nfse-indop-ibscbs]]. As NTs citam as versões 1.00.00 (NT 004 e 005), 1.01.00 (NT 007) e 1.02.00 (NT 009) |
| **VIII** — correlação item da NBS × `cIndOp` × cClassTrib | "norteador" sem regras de negócio | **não está nas fontes** |
| **A** — municípios IBGE e países ISO2 | tabela de códigos | municípios: a tabela do IBGE (DTB de 22/11/2024) está nas fontes, ver [[df-nfse-codigos-ibge-localidades]]; **países ISO2: não estão nas fontes** |
| **B** — lista nacional de serviços | códigos de tributação nacional | a lista do portal (atualizada em 20/08/2024) está em [[df-nfse-lista-servicos-ctribnac]]; o arquivo "V1.01-20260122" citado pelo guia **não está nas fontes** |
| **II** do manual da API — leiautes e regras dos eventos | eventos de NFS-e | **não está nas fontes** |

Sem o **Anexo VI**, as **regras de negócio do grupo `IBSCBS`** (por exemplo, quais combinações de
`cIndOp`, CST e cClassTrib a Sefin rejeita, e os códigos de rejeição desse grupo) **não podem ser
respondidas** pelas notas; só o layout descrito nas NTs.

## API do Emissor Público Nacional (manual dos contribuintes)

O manual descreve as APIs que o emissor nacional (e quem o integra por sistema) usa; é
documentação **operacional**:

| API | Métodos | Para quê |
|---|---|---|
| **Parâmetros municipais** | `GET /parametros_municipais/{codigoMunicipio}/convenio`; `.../{codigoServico}`; `.../{CPF/CNPJ}` | parâmetros do convênio do município; alíquotas, regimes especiais e deduções por subitem; retenções e benefícios municipais do contribuinte |
| **NFS-e** | `POST /nfse`; `GET /nfse/{chaveAcesso}` | recebe uma DPS, valida as regras de negócio e **gera a NFS-e de forma síncrona** (ou rejeita com o motivo); consulta pela chave. Se a DPS traz a chave de uma NFS-e já gerada, a Sefin gera um **evento de cancelamento por substituição** e a NFS-e substituta |
| **DPS** | `GET /dps/{id}`; `HEAD /dps/{id}` | recupera a **chave de acesso** pela identificação da DPS (município emissor, tipo e número de inscrição federal, série e número); o `GET` só responde a quem consta na nota (prestador, tomador ou intermediário, pelo certificado digital); o `HEAD` informa só **se a NFS-e foi gerada**, a qualquer certificado válido |
| **Eventos** | `POST /nfse/{chaveAcesso}/eventos`; `GET` por chave, por tipo e por sequencial | registra e consulta eventos (cancelamento, manifestação de confirmação etc.), originados do emitente, de não emitentes, do município emissor, do município de incidência e do módulo de apuração nacional; mensagens em **JSON** e evento em **XML assinado** |

O ambiente de **produção restrita** (Swagger de testes) é
`adn.producaorestrita.nfse.gov.br/contribuintes/docs`. A **geração do DANFSe** é outra API, a ser
suspensa em 03/08/2026 ([[df-nfse-danfse]]). O guia diz que o acesso por API usa certificado
digital ([[df-nfse-acesso-perfis]]).

## Notas de contexto

- **Integração dos municípios:** o prazo de 1º/01/2026 para os municípios se integrarem à
  plataforma e compartilharem os documentos (art. 62 da LC 214/2025, segundo a NT 004 v2.00)
  continua valendo mesmo com a obrigatoriedade do grupo `IBSCBS` suspensa
  ([[df-nfse-layout-ibscbs]]). Convênios municipais e ISSQN estão **fora do escopo**.
- **Itens cobertos por NT própria no futuro:** DANFSe dos novos fatos geradores (NT 008);
  notas de ajuste ("em estudos", NT 004 v2.00; "em evolução", NT 009); manuais dos novos fatos
  geradores (NT 005).
