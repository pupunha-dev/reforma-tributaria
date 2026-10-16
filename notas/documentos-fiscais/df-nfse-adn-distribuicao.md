---
título: NFS-e Nacional — distribuição de DF-e pelo ADN (Anexo IV v1.00-20251216): quem recebe NSU de cada NFS-e e evento, consultas por NSU ou chave e rejeições na recepção de lotes
dominio: documentos-fiscais
fontes: Anexo IV — ADN: geração de NSU de DF-e, regras de distribuição a municípios e contribuintes e regras de recepção de lote v1.00-20251216 (planilhas "ADN-GERACAO_NSU_DFe", "ADN-RN_DISTRIB_MUN_CONTRIB" e "RN_RECEPCAO_LOTE_DF-e"); NT CGNFS-e 010 v1.00 (cita outro "Anexo IV", o da NFS-e Via, que não é este arquivo)
vigencia: atual
texto-base: 2026-10-16
---

# Distribuição de DF-e pelo ADN (Anexo IV)

## A lógica em uma frase

O **ADN** (Ambiente de Dados Nacional da NFS-e) guarda os documentos fiscais eletrônicos (DF-e): as
NFS-e e os eventos ([[df-nfse-eventos]]). Para cada documento ou evento o ADN **gera números de
sequência (NSU)** em filas de destino, e cada destinatário (Receita, município, contribuinte) lê **só a
sua fila** pela API de distribuição. O **Anexo IV** (nível de NT) diz **em quais filas cada documento
entra**, como consultar e quando a consulta é rejeitada. Convênio municipal, quem pode ser transmissor
e o conteúdo tributário de cada município são matérias fora do escopo; esta nota descreve só a regra
técnica.

> **Atenção ao nome "Anexo IV":** este arquivo (v1.00-20251216) trata da **distribuição de DF-e do
> ADN** (NSU, municípios e contribuintes, recepção de lote). A NT CGNFS-e 010 v1.00 chama de "Anexo IV
> - Leiautes RN ADN" **outro** documento (`LeiautesRN_ADN-SNNFSeVia_V1.00.04`, seis planilhas do
> leiaute e dos eventos da **NFS-e Via**). Esse segundo arquivo **não está nas fontes**
> ([[df-nfse-via]]).

## 1. Em que filas o NSU é gerado (planilha "ADN-GERACAO_NSU_DFe")

A planilha cruza **o documento** (NFS-e ou um dos eventos) com **o destino**. Os mesmos destinos valem
para a NFS-e e para todos os eventos. O quadro resume o que a planilha marca com V (gera) e X (não gera):

| Destino | NFS-e e eventos em geral | Observação |
|---|---|---|
| **RFB** (fila geral) | V | todo documento |
| **Município emissor (cLocEmi), recepção** | V se o DF-e foi emitido no **sistema próprio do município** e compartilhado com o ADN; X se foi emitido na **Sefin Nacional** | NSU de **recepção** (também usado na recuperação de backup, E2070) |
| **Município emissor, distribuição** | V só se o município é **existente e ativo** e o DF-e foi emitido no sistema próprio; X para DF-e da Sefin Nacional, para município existente **não ativo** e para município **inexistente** | a planilha marca assim; ver a nota (3) |
| **Município do emitente** (prestador, tomador ou intermediário) | já contemplado | a planilha diz que, como o município do emitente é o município emissor, o NSU já é gerado pelo item anterior |
| **Município do não emitente** (prestador, tomador ou intermediário) | V | nota (1): só se for **diferente** do município do emitente |
| **Município da prestação** | V | nota (2): só se for diferente do município do emitente **e** do município do não emitente |
| **Município de incidência do ISSQN** | já contemplado | é o município do prestador, do tomador ou da prestação, que já têm NSU |
| **MEI (cStat 107)**, municípios do prestador, tomador, intermediário, emissor e local da prestação | V se o município é **inexistente ou inativo** no Sistema Nacional; X se existente e não inativo | só para NFS-e de MEI |
| **CGNFS-e**, "bypass" (cStat 102) | V | |
| **Emitente** (P/T/I) | V | o contribuinte recebe a própria nota e os eventos |
| **Não emitente** (P/T/I) | V, **exceto** nos eventos de bloqueio e desbloqueio por ofício, que **não** chegam ao não emitente | consistente com a visibilidade do Anexo II (bloqueio visível só para emitente e administração) |

Notas da planilha:

- **(3)** os NSU são gerados para **qualquer município**, ativo ou não ativo no Sistema Nacional; todos
  os DF-e podem ser solicitados na API de distribuição, **exceto** quando o município é inexistente,
  inativo ou suspenso.
- **(4) e (5)** (destinatário): NSU de distribuição só se o município do destinatário for diferente do
  município do tomador, e só se o destinatário for diferente do tomador. A planilha não mostra em que
  coluna essas notas se aplicam; confira o arquivo
  `fontes/documentos-fiscais/texto/anexo-iv-adn-geracao-nsu-dfe.tsv`.
- **\*** "existente" = consta no cadastro de municípios conveniados ao Sistema Nacional; **\*\***
  "inexistente" = não consta.

## 2. Consulta pelos órgãos, municípios e contribuintes

| Quem consulta | Forma | Rejeição |
|---|---|---|
| Órgão (convênio do sistema nacional) | NSU geral | E2301: CNPJ do transmissor não cadastrado para um órgão; E2305: nenhum documento a partir do NSU; E2306: nenhum documento para o NSU informado |
| Município | a partir de um NSU / um NSU / chave de acesso / recuperação de backup (município emissor) | E2000: erro no certificado; E2001: CNPJ não cadastrado para nenhum município conveniado; E2003: município suspenso no convênio; E2004: município inativo há mais do que o prazo; E2020 e E2040: sem documento a partir do NSU / para o NSU; E2060: chave não localizada; E2061: a chave **não referencia o município solicitante**, e por isso não pode ser compartilhada; E2070: NSU de recepção não localizado |
| Contribuinte (ator da NFS-e) | a partir de um NSU / um NSU / chave de acesso | E2215 e E2230: sem documento a partir do NSU / para o NSU; E2240: chave não localizada; E2241: a chave **não referencia o contribuinte solicitante** (só se vê a nota em que se é parte) |

Em palavras: consultar por chave só devolve a NFS-e se o solicitante estiver ligado a ela (município:
emissor, incidência, local da prestação, não emitente; contribuinte: prestador, tomador ou
intermediário). O prazo de inativação do município na E2004 é um parâmetro (`<<prazo para a
inativação>>`) que o anexo não fixa.

## 3. Recepção de lote de DF-e (planilha "RN_RECEPCAO_LOTE_DF-e")

Regras que rejeitam o **lote** enviado ao ADN (compartilhamento de NFS-e do sistema próprio do
município):

| Grupo | Regras |
|---|---|
| **Certificado de transmissão** | E1200 certificado inválido (inexistente, versão diferente de 3, Basic Constraint de AC, KeyUsage sem "Autenticação Cliente"); E1203 expirado; E1205 erro na cadeia de certificação; E1206 erro de acesso à LCR; E1207 revogado; E1208 raiz diferente de ICP-Brasil; E1209 sem CNPJ |
| **Quem pode compartilhar** | E1262: o CNPJ do certificado de transmissão **não está autorizado** a compartilhar DF-e pelo município conveniado; E1245 e E1246: certificado da **assinatura do lote** sem CNPJ / com erro na cadeia |
| **Mensagem na API** | E1217: serviço paralisado para manutenção; E1219: número de documentos acima do limite definido para a aplicação (o limite não está no anexo) |
| **Área de dados** | E1225: falha ao decodificar o Base64; E1226: estrutura descompactada malformada; E1242: tipo de DF-e não tratado pelo Sistema Nacional; E1228: prefixo de namespace não permitido; E1229: XML sem UTF-8; E1235: falha no esquema XML; E1250: assinatura difere do calculado |

## Ligações com outras notas

- [[df-nfse-eventos]]: os eventos e a visibilidade de cada um.
- [[df-nfse-via]] e [[df-nfse-acesso-perfis]]: onde o contribuinte e o município aparecem na operação do
  emissor.
- [[df-nfse-cgnfse-notas-tecnicas]]: quadro dos anexos e das versões.
- Fora do escopo: a lista de municípios conveniados e o convênio de cada município com a NFS-e Nacional.

## O que não está nas fontes

- A **data de produção** do Anexo IV v1.00-20251216 e o **limite de documentos por lote** (E1219).
- Os **prazos de inativação** do município (E2004) e a lista dos municípios ativos.
- Como a API de distribuição é chamada (endpoints, parâmetros): isso está no manual da API
  (`manual-api-emissor-nfse-2025-10.pdf`, versão indeterminada); consulte-o em vez de deduzir.
