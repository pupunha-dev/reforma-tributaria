---
título: Índice — Documentos fiscais eletrônicos (Notas Técnicas NF-e)
---

# Índice de notas — documentos-fiscais

Domínio `documentos-fiscais`. Prefixo `df-`. Fontes: Notas Técnicas do Projeto
NF-e, o Informe Técnico 2025.002, as tabelas do Portal dos DF-e, o Guia do Emissor Público Nacional Web da NFS-e v1.2 e as Notas Técnicas da SE/CGNFS-e 003 a 010 com os Anexos B, I, II, IV (ADN), VI, VII e VIII, o manual da API e a lista nacional de serviços da NFS-e, e a tabela de municípios do IBGE (ver [FONTE.md](../../fontes/documentos-fiscais/FONTE.md)), com a versão de
cada uma no frontmatter das notas. Data-base: 07/10/2026 (NF-e) e 16/10/2026 (NFS-e).

**Hierarquia:** lei (LC 214/2025, LC 123/2006) > resolução/ato infralegal > nota
técnica. A NT diz **como preencher e validar** o documento; ela não cria nem
altera tributo. Se a NT divergir da lei, a nota avisa e vale a lei.

**Vigência:** a NT entra em vigor por **cronograma** (homologação e produção). O
que ainda não está em produção na data-base fica em blocos `⏳ Em produção a
partir de ...`.

Mapa seção da NT → nota: [_plano-notas.md](_plano-notas.md).

## 1. Visão geral

- [[df-visao-geral-reforma-nfe]] — o que mudou na NF-e/NFC-e, linha do tempo das 5 NTs, lacuna do Simples/MEI (CRT 1, 2 e 4)

## 2. Como preencher o XML

- [[df-cst-cclasstrib]] — CST e código de classificação tributária (cClassTrib); tabelas no Portal NF-e
- [[df-tabela-cclasstrib]] — os 18 CST e os 173 cClassTrib (IT 2025.002 + Portal dos DF-e): reduções, vigência, documentos em que valem, tipo de receita do Simples (tpRBSN) e histórico das versões
- [[df-credito-presumido-ccredpres]] — os 13 códigos de crédito presumido (cCredPres): apropriação no documento ou por evento e vigência por tributo (nenhum antes de 01/01/2027)
- [[df-grupo-ibs-cbs-is]] — grupos e campos de IBS, CBS e IS no leiaute
- [[df-finalidade-debito-credito]] — notas de débito e de crédito
- [[df-valor-liquido-produto]] — valor líquido do produto e ICMS previsto no pagamento antecipado (NT 2026.008)
- [[df-contribuinte-exclusivo-ibs-cbs]] — emitente só de IBS/CBS, sem inscrição estadual (NT 2026.007)

## 3. Validação, autorização e eventos

- [[df-calculo-e-validacoes]] — fórmulas conferidas pela SEFAZ e regras de validação
- [[df-emissao-offline-alerta]] — emissão offline, autorização com alerta, DANFE Simplificado Tipo 2 (NT 2026.002)
- [[df-eventos-apuracao]] — eventos para apuração do IBS/CBS

## 4. Impressão

- [[df-danfe-reforma]] — novo leiaute do DANFE com IBS, CBS e IS (NT 2026.010)

## 5. NFS-e Nacional (Guia do Emissor Público Nacional Web v1.2)

O guia é **documentação operacional** (como usar o emissor): fica abaixo da NT e dos
atos; datas e obrigações vêm do ato. ISSQN e convênios municipais ficam fora do escopo.

- [[df-nfse-visao-geral]] — o que é o emissor (Web, Mobile e API), DPS × NFS-e, glossário, versões do guia e datas do IBS/CBS (03/08/2026 regime regular; 01/01/2027 Simples)
- [[df-nfse-acesso-perfis]] — acesso por usuário/senha, certificado digital e GOV.BR (só MEI); primeiro acesso, recuperação de senha, níveis de acesso e cadastro presencial
- [[df-nfse-painel-configuracoes]] — painel, configurações do emitente, rascunhos de DPS e serviços favoritos
- [[df-nfse-emissao-pessoas]] — passo 1: IBS/CBS sim/não, DPS (número e série), emitente (na versão atual só o prestador/fornecedor emite; tomador e intermediário ainda não), compras governamentais, tomador (inclusive no exterior: NIF, ou motivo de dispensa/não exigência do NIF), destinatário e intermediário
- [[df-nfse-emissao-servico]] — passo 2: local da prestação, código de tributação, NBS, indicador da operação, imóvel/obra, evento, comércio exterior e tipo de operação
- [[df-nfse-emissao-valores-ibs-cbs]] — passo 3: valores, descontos, deduções, tributação federal, CST/cClassTrib e documentos de reembolso, repasse e ressarcimento
- [[df-nfse-emissao-final-mei]] — passo 4 (emitir), NFS-e gerada e emissão simplificada do MEI
- [[df-nfse-decisao-administrativa-judicial]] — emissão por decisão administrativa ou judicial
- [[df-nfse-consulta-cancelamento-substituicao]] — consultar, substituir, cancelar, XML/DANFSe e consulta pública (chave de acesso)
- [[df-nfse-notas-recebidas-manifestacao]] — NFS-e recebidas; confirmar ou rejeitar

### NFS-e Nacional — Notas Técnicas da SE/CGNFS-e (003 a 010), anexos e API

Nível de **NT** (documentação técnica nacional): acima do guia, abaixo da lei e dos
regulamentos. A mais nova que altera um campo prevalece; o cronograma de produção de várias NTs
**não está nas fontes**.

- [[df-nfse-cgnfse-notas-tecnicas]] — **comece por aqui** nas perguntas sobre NT da NFS-e: cronologia das NTs 003 a 010, qual substitui qual, o que está em produção (05/01/2026, 09/02/2026), mapa dos anexos (I v1.01, II, IV, VI, VII e VIII, com as versões nas fontes) e API do emissor nacional (POST /nfse, DPS, eventos, produção restrita)
- [[df-nfse-layout-ibscbs]] — campos e fórmulas do grupo IBSCBS na DPS e na NFS-e: obrigatoriedade suspensa, vBC, alíquotas efetivas, vTotNF, PIS/COFINS (NT 007: significado de cada CST, como 06 alíquota zero, e tpRetPisCofins), notas de ajuste, Simples, imóvel, bens móveis, pagamento vinculado, CNPJ alfanumérico (NTs 004, 005, 007, 009)
- [[df-nfse-comercio-exterior]] — exportação de serviço na NFS-e: grupo comExt (códigos de vínculo, moeda, mecanismos de apoio, DI/RE), NIF/cNaoNIF, rejeições E0330 a E0356 e E0590, as 112 combinações do Anexo I
- [[df-nfse-indop-ibscbs]] — os 40 códigos do indicador da operação cIndOp (Anexo VII v1.03.00), como ler a tabela e o que ela não responde
- [[df-nfse-danfse]] — DANFSe v2.0 (NT 008): blocos, supressões, QR Code, marcas d'água CANCELADA/SUBSTITUÍDA e suspensão da API de geração em 03/08/2026
- [[df-nfse-via]] — NFS-e Via (exploração de via/pedágio; NTs 006 e 010): layout, campos fixos (220101, 106042100, CST 000, cClassTrib 000002), eventos de cancelamento e de manifestação
- [[df-nfse-lista-servicos-ctribnac]] — os 338 códigos de tributação nacional (cTribNac, 6 dígitos) do Anexo B (lista nacional de serviços, com títulos de item e subitem), e as regras do documento que dependem do código (obra E0372, evento E0392, águas marítimas E1402, não incidência 990101, rodovia 220101)
- [[df-nfse-codigos-ibge-localidades]] — códigos IBGE de 7 dígitos de município na DPS (cLocEmi, cLocPrestacao `0000000` águas marítimas, cLocIncid, cMun), o que a tabela do IBGE (DTB 22/11/2024) contém e como consultar (script)
- [[df-nfse-regras-ibscbs-anexo-vi]] — regras de rejeição do IBS/CBS na DPS e na NFS-e (Anexo I v1.01 em produção × Anexo VI v1.04.01 da NT 009): papel da calculadora, quando exigir tomador/destinatário com CNPJ/CPF e endereço, imóvel (E0931/E0932/E0928), locação, bens móveis (99.04.01), fórmulas de vBC e vTotNF, o que é só do Anexo VI
- [[df-nfse-eventos]] — os 16 tipos de evento da NFS-e (Anexo II v1.01): códigos, quem registra, leiaute do pedido, motivos de cancelamento/substituição/rejeição, ordem entre eventos (bloqueio e desbloqueio por ofício) e rejeições (E0xxx/E1xxx/E2xxx)
- [[df-nfse-adn-distribuicao]] — distribuição de DF-e pelo ADN (Anexo IV v1.00-20251216): em quais filas o NSU é gerado para município, RFB e contribuintes, consulta por NSU/chave e rejeições na recepção de lote
- [[df-nfse-correlacao-nbs-indop]] — Anexo VIII v1.01.00: como ler a correlação item da lista × NBS × cIndOp × cClassTrib, regra do inciso X (códigos 1001xx/1003xx/1005xx), legenda dos 28 cClassTrib
- [[df-nfse-correlacao-itens-01-06]], [[df-nfse-correlacao-itens-07]], [[df-nfse-correlacao-itens-08-13]], [[df-nfse-correlacao-itens-14-16]], [[df-nfse-correlacao-itens-17-40]], [[df-nfse-correlacao-itens-99]] — as tabelas do Anexo VIII por item da LC 116 (NBS, cIndOp e cClassTrib de cada NBS); abra a que contém o item perguntado
