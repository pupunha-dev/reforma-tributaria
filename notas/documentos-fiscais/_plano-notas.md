---
título: Plano de notas — Documentos fiscais eletrônicos (Notas Técnicas NF-e)
status: concluido
---

# Plano de notas — documentos-fiscais

Fontes: 5 Notas Técnicas do Projeto NF-e (ver `fontes/documentos-fiscais/FONTE.md`).
Data-base: 07/10/2026. Aprovado por delegação do usuário ("faça o melhor que
achar", 07/10/2026).

Regra de vigência do domínio: a NT não tem "produção de efeitos", tem
implantação em **homologação** (teste) e em **produção**. O que ainda não está em
produção em 07/10/2026 vai para um bloco `⏳ Em produção a partir de ...`.

## Mapa seção da NT → nota

| Nota | NT e seções | Vigência prevista | Conteúdo |
|---|---|---|---|
| df-visao-geral-reforma-nfe.md | NT 2025.002-RTC v1.52: controle de versões, cronograma, detalhamento do cronograma, seção 1 | com-mudanca-programada | O que mudou na NF-e/NFC-e, linha do tempo consolidada das 5 NTs, valor jurídico dos campos, lacuna CRT 1/2/4 |
| df-cst-cclasstrib.md | NT 2025.002-RTC v1.52: seções 2 e 3; Anexos I a IV | atual | Tipos básicos da tributação, CST e cClassTrib; onde estão as tabelas (Anexos I e II ainda lacuna) |
| df-tabela-cclasstrib.md | IT 2025.002 v1.60, seções 02, 03, 06 e 07; Portal dos DF-e, captura 2026-10-08; NT 2025.002-RTC v1.52, seção 3 e Anexo III | atual | Os 18 CST e os 173 cClassTrib: reduções de IBS/CBS, tipo de alíquota, vigência, documentos, tpRBSN, histórico das versões do IT |
| df-credito-presumido-ccredpres.md | IT 2025.002 v1.60, seções 04 e 06; Portal dos DF-e, captura 2026-10-08; NT 2025.002-RTC v1.52, Anexo IV e UB120 a UB130 | com-mudanca-programada | Os 13 cCredPres, apropriação, vigência por tributo, divergência do exemplo 5 da NT |
| df-finalidade-debito-credito.md | NT 2025.002-RTC v1.52: seção 4; NT 2026.008 v1.00 (Exceção 4 da B25-80) | com-mudanca-programada | Finalidades 5 (crédito) e 6 (débito), tipos de nota de débito/crédito |
| df-grupo-ibs-cbs-is.md | NT 2025.002-RTC v1.52: seção 6 (leiaute: grupos B, BA, BB, BC, C, I, N01, UB, VB, VC, W03) | com-mudanca-programada | Onde e como informar IBS, CBS e IS no XML |
| df-calculo-e-validacoes.md | NT 2025.002-RTC v1.52: seções 5 e 7 | com-mudanca-programada | Fórmulas de cálculo conferidas pela SEFAZ, regras de validação centrais, códigos de status |
| df-eventos-apuracao.md | NT 2025.002-RTC v1.52: seção 8 | atual | Eventos para apuração do IBS/CBS (crédito presumido, imobilização, perecimento etc.) |
| df-emissao-offline-alerta.md | NT 2026.002 v1.11 (todas as seções) | com-mudanca-programada | Emissão offline, autorização com alerta, DANFE Simplificado Tipo 2, limite da NFC-e sem destinatário |
| df-contribuinte-exclusivo-ibs-cbs.md | NT 2026.007 v1.10 (todas as seções) | com-mudanca-programada | Emissão por contribuinte só de IBS/CBS (sem inscrição estadual) |
| df-valor-liquido-produto.md | NT 2026.008 v1.00 (todas as seções) | com-mudanca-programada | Valor líquido do produto e ICMS previsto no pagamento antecipado |
| df-danfe-reforma.md | NT 2026.010 v1.00 (todas as seções); NT 2025.002-RTC v1.52, seção 9 | com-mudanca-programada | Novo leiaute do DANFE com IBS, CBS e IS |

Ajustes na redação: juntar ou separar notas conforme o volume real; toda seção
das NTs tem uma nota dona.

## Fonte nova (2026-10-16): Guia do Emissor Público Nacional Web da NFS-e v1.2

Fonte: `fontes/documentos-fiscais/guia-emissor-publico-nacional-nfse-v1.2.1.pdf`, 125 páginas, texto em
`fontes/documentos-fiscais/texto/guia-emissor-publico-nacional-nfse-v1.2.1-vigente.txt`. **Aprovado pelo usuário em
16/10/2026** (escopo e profundidade); as 10 notas foram escritas e o plano voltou a `concluido`.

Natureza: manual operacional do emissor web da NFS-e Nacional. Fica **abaixo da
NT**: diz como emitir, consultar, cancelar e substituir; não cria regra nem tributo.
As datas de obrigatoriedade do IBS/CBS que o guia cita (03/08/2026 para o regime
regular; 01/01/2027 para o Simples Nacional, por fato gerador) vêm do próprio guia, e
o ato que as fixa **não está nas fontes** (registrar na lista de pendências do projeto). ISSQN e
convênios dos municípios são municipais: ficam fora de escopo. Prefixo `df-nfse-`.

| Nota | Guia (seções e páginas) | Vigência prevista | Conteúdo |
|---|---|---|---|
| df-nfse-visao-geral.md | Histórico de versões, resumo, siglas e seção 1 (p. 1-7) | com-mudanca-programada | O que é o emissor nacional (Web, Mobile e API), DPS x NFS-e, quem usa, funcionalidades, glossário, versões do guia e datas do IBS/CBS |
| df-nfse-acesso-perfis.md | 1.1 e 10 (p. 7-15 e 118-125) | atual | Acesso por usuário/senha, certificado digital e GOV.BR; primeiro acesso, recuperação de senha, perfis e níveis de acesso, cadastro presencial |
| df-nfse-painel-configuracoes.md | 2, 3, 7 e 8 (p. 16-19 e 112-115) | atual | Painel principal, menu e painéis gerenciais, configurações do emissor, rascunhos de DPS e serviços favoritos |
| df-nfse-emissao-pessoas.md | 4.1 e 4.1.1, passo 1 (p. 20-42) | com-mudanca-programada | Emitente, prestador, tomador, destinatário; opção de preencher IBS/CBS; competência; número e série da DPS; compra governamental |
| df-nfse-emissao-servico.md | 4.1.2, passo 2 (p. 43-66) | com-mudanca-programada | Local e código de tributação, NBS, código indicador da operação, descrição, serviços ligados a imóveis, exterior e demais grupos do passo 2 (coube em uma nota) |
| df-nfse-emissao-valores-ibs-cbs.md | 4.1.3, passo 3 (p. 66-84) | com-mudanca-programada | Valores, ISSQN, CST e cClassTrib, documentos de reembolso, repasse e ressarcimento, totais |
| df-nfse-emissao-final-mei.md | 4.1.4, 4.1.5 e 4.2 (p. 84-96) | atual | Conferir e emitir; NFS-e gerada; emissão simplificada do MEI (configuração e serviços favoritos) |
| df-nfse-decisao-administrativa-judicial.md | 4.3 (p. 96-100) | atual | Incluir, consultar, cancelar e substituir NFS-e emitida por decisão administrativa ou judicial |
| df-nfse-consulta-cancelamento-substituicao.md | 5 e 9 (p. 100-106 e 115-117) | atual | Consultar NFS-e emitidas e eventos, substituição, cancelamento e pedido por análise fiscal, download de XML e DANFSe, consulta pública |
| df-nfse-notas-recebidas-manifestacao.md | 6 (p. 107-112) | atual | NFS-e recebidas, download, manifestação (confirmar ou rejeitar) |

Decisões do usuário (aprovadas em 16/10/2026):

1. **Escopo:** o `CLAUDE.md` aceita hoje "atos normativos federais" e a documentação
   técnica da NF-e/NFC-e. O Guia é manual operacional, não ato normativo. Adotado:
   incluí-lo como documentação técnica nacional do domínio `documentos-fiscais`,
   com a regra "o guia diz como operar o emissor; datas e obrigações vêm do ato".
2. **Profundidade:** as telas (321 imagens) não entram nas notas; as notas trazem as
   regras de preenchimento, obrigatoriedades e condições. Campo a campo só onde mudar
   o resultado fiscal.

Depois da redação, feitos: ligações (etapa 6: `INDEX.md` do domínio com um
grupo "NFS-e" e `[[...]]` para `df-cst-cclasstrib`, `df-tabela-cclasstrib`,
`sn-obrigacoes-acessorias`, `sn-mei-regulamentacao` e `ibs-cbs-documento-fiscal-regulamentacao`)
e protocolo (etapa 7: linha do domínio no `CLAUDE.md`, bloco no `MEMORY.md`,
perguntas D17 em diante em `docs/perguntas-teste/documentos-fiscais.md` e regressão das
três baterias). O bot do Telegram também precisa ter o escopo atualizado em
`prompts/roteador.md` e `prompts/sistema.md`.

## Fonte nova (2026-10-16, tarde): Notas Técnicas da SE/CGNFS-e 003 a 010, Anexos I e VII e manual da API

Fontes: `fontes/documentos-fiscais/nt-cgnfse-003-v1.2.pdf` a `nt-cgnfse-010-v1.00.pdf`,
`manual-api-emissor-nfse-2025-10.pdf`, `anexo-i-leiaute-rn-dps-nfse.xlsx` e
`anexo-vii-indop-ibscbs-v1.03.00.xlsx` (textos e TSV em `texto/`). Pedido do usuário em 16/10/2026 para
resolver os códigos que o bot não conseguia decodificar (comércio exterior, `cIndOp`, regras de rejeição).
Nível de NT (acima do guia). Seis notas novas, prefixo `df-nfse-`:

| Nota | Fonte (NT e seções) | Vigência prevista | Conteúdo |
|---|---|---|---|
| df-nfse-cgnfse-notas-tecnicas.md | NTs 003 a 010 (cabeçalhos, históricos de versão e seções de cronograma); manual da API; mapa dos anexos | com-mudanca-programada | Cronologia, substituição entre NTs, o que está em produção, anexos nas fontes e lacunas, API do emissor nacional |
| df-nfse-layout-ibscbs.md | NT 004 v2.00 (seções 1 e 2 e leiaute); NT 005; NT 007; NT 009 | com-mudanca-programada | Grupo IBSCBS da DPS e da NFS-e: campos, fórmulas, PIS/COFINS, notas de ajuste, Simples, imóvel, bens móveis |
| df-nfse-comercio-exterior.md | Anexo I (abas `RN_RECEPCAO_DPS`, `EXPORTACAO_EMISSÃO_NFS-e`, `LEIAUTE DPS_NFS-e`, `RN DPS_NFS-e`); NT 009 (NIF e CNPJ alfanumérico) | atual | comExt, códigos, rejeições e as 112 combinações da aba de exportação |
| df-nfse-indop-ibscbs.md | Anexo VII v1.03.00 (aba `cIndOp Public`) | com-mudanca-programada | Os 40 códigos do `cIndOp` e como lê-los |
| df-nfse-danfse.md | NT 008 v1.02 (todas as seções); NT 004 v2.00, seção 1.2 | com-mudanca-programada | DANFSe v2.0 |
| df-nfse-via.md | NT 006 v1.00; NT 010 v1.00; NT 007, seção 3.c; NT 004 v2.00, seção 1.3 | atual | NFS-e Via: layout, eventos, ISSQN |

Fora do escopo (continua): ISSQN e convênios municipais, PIS/COFINS (só campos do layout), Resolução CGNFS-e 9 (não está nas fontes).
Depois da redação: notas antigas do guia revisadas (lacunas de comércio exterior e `cIndOp` resolvidas).
