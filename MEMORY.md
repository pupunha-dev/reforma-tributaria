# Contexto fixo

- Escritório de contabilidade, setor fiscal e diretoria
- Carteira concentrada em Comércio, Indústria, Transporte e Serviços.
- Second brain **multi-domínio** (desde 2026-10-06): uma pasta por assunto
  em `notas/<dominio>/`, roteada por `notas/INDEX.md`.
- Domínios ativos:
  - `reforma`: Reforma Tributária (LC 214/2025, atualizada pela LC 227/2026),
    origem marcada 🔵 LC 214 · 🟢 LC 227 · 🟡 ambas. Desde 2026-10-08, com os
    regulamentos (Decreto 12.955/2026 da CBS, compilado com o Decreto
    13.075/2026; Res. CGIBS 6/2026 do IBS, texto original): mapa gerado
    `_mapa-regulamentos.md` (`scripts/mapa_regulamento.py`), bloco
    "Regulamentação" em cada nota e 4 notas próprias. 92 notas.
  - `simples-nacional`: LC 123/2006 (fase A, 2026-10-06) + Resolução CGSN
    140/2018 na visão multivigente da Receita, com as Res. CGSN 190 e
    191/2026 (fase B, 2026-10-07) + Anexos VI (CNAEs impeditivos) e XI
    (ocupações do MEI) da Res. 140 e a SC Cosit 71/2026 (fase C,
    2026-10-08) + Res. CGSN 11/2007 (arrecadação, texto original): 36 notas `sn-*` (a 36ª, `sn-opcao-2027-prazos`, entrou em 2026-10-16). Anexos VII, X e XII ainda não estão nas
    fontes.
  - `documentos-fiscais` (desde 2026-10-07): 5 Notas Técnicas do Projeto
    NF-e (NT 2025.002-RTC v1.52, 2026.002 v1.11, 2026.007 v1.10, 2026.008
    v1.00 e 2026.010 v1.00), o Informe Técnico 2025.002 v1.60 e as tabelas
    CST/cClassTrib (173 códigos) e cCredPres (13 códigos) capturadas em
    2026-10-08 do Portal dos DF-e (SVRS) via `scripts/tabelas_svrs.py`: 12
    notas `df-*`. Hierarquia: lei > resolução > NT/IT. As NTs e ITs têm
    texto riscado; as notas usam o `*-vigente.txt` (`scripts/extrair_nt.py`,
    requer pymupdf). Orientações de NF-e para Simples/MEI (CRT 1, 2 e 4)
    ainda dependem de "NT futura".
  - NFS-e (desde 2026-10-16): Guia do Emissor Público Nacional Web da NFS-e v1.2
    (27/07/2026) como documentação **operacional** (abaixo da NT e dos atos), em 10 notas
    `df-nfse-*` (22 notas `df-*` no total). As telas (321 imagens) não entram; as datas de
    IBS/CBS que o guia cita (03/08/2026 regime regular; 01/01/2027 Simples por fato gerador)
    não têm o ato nas fontes.
  - NFS-e, Notas Técnicas da SE/CGNFS-e (desde 2026-10-16, tarde): NTs 003 a 010, Anexo I
    (cópia de 09/09/2025, **anterior ao RTC, sem o grupo IBSCBS**), Anexo VII v1.03.00 (40 códigos
    `cIndOp`) e manual da API (versão indeterminada) entram no **nível de NT**, em 6 notas novas
    `df-nfse-*` (28 notas `df-*` no total): `cgnfse-notas-tecnicas` (cronologia), `layout-ibscbs`,
    `comercio-exterior`, `indop-ibscbs`, `danfse` e `via`. Ordem de publicação ≠ ordem de
    implantação (a NT 005 é anterior à 004 v2.00 mas não entrou em produção em jan/2026). Lacunas
    daquela data (Anexo VI, Anexo VIII e Anexo I atual foram resolvidas na entrada "noite" abaixo; seguem abertos o
    cronograma das NTs 005/007/009 e a Resolução CGNFS-e 9: `pendencias.md`).
  - NFS-e, tabelas de códigos (2026-10-16, fim da tarde): lista nacional de serviços do portal (335 códigos
    de 6 dígitos, atualizada pelo portal em 20/08/2024) e tabela do IBGE (DTB 22/11/2024; 5.570 municípios,
    consulta por `scripts/consulta_ibge.py`) entram em 2 notas (`lista-servicos-ctribnac`,
    `codigos-ibge-localidades`; 30 notas `df-*`). Arquivados sem uso: NT 2025.002 v1.33 (superada) e um CSV
    de terceiros (item × NBS × cIndOp × cClassTrib) **reprovado** na conferência contra o Anexo VII e o
    Portal dos DF-e (o Anexo VIII oficial chegou na entrada seguinte).
  - NFS-e, anexos oficiais novos (2026-10-16, noite): Anexo I v1.01-20260209 (layout em produção; a cópia de
    09/09/2025 foi arquivada como superada), Anexo II v1.01-20260122 (eventos), Anexo IV v1.00-20251216 (ADN,
    distribuição de DF-e; **não** é o "Anexo IV" da NFS-e Via citado pela NT 010), Anexo VI v1.04.01 (layout da
    NT 009 v1.01, sem data de produção), Anexo VIII v1.01.00 (correlação item × NBS × cIndOp × cClassTrib) e a
    NT 009 v1.01 (a v1.0 foi arquivada). 10 notas `df-nfse-*` novas (40 notas `df-*` no total):
    `regras-ibscbs-anexo-vi`, `eventos`, `adn-distribuicao`, `correlacao-nbs-indop` e 6 notas
    `correlacao-itens-*` (geradas por `scripts/gerar_notas_anexo_viii.py`). Regra de ouro: o que é **só do
    Anexo VI** não tem data de produção nas fontes. Lacunas que restam em `pendencias.md`.
  - NFS-e, Anexo B v1.01-20260122 (2026-10-16, noite): lista nacional de serviços com **338 códigos** (os 335 do portal,
    de descrição idêntica, + 110501, 141403 e 141404), títulos de 41 itens e 201 subitens, e lista de NBS v2.0 (1.210 entradas;
    contém as 731 NBS do Anexo VIII). A nota `lista-servicos-ctribnac` passou a se basear nele; sem nota nova (40 notas `df-*`).
    Segue faltando o Anexo A (países ISO2).
  - `simples-nacional`, atos CGSN de 2026 fora da Res. 140 (2026-10-16): Res. CGSN 186/2026 (prazos da
    opção para 2027), alterada pela 194/2026 (28/09/2026), em `sn-opcao-2027-prazos`: opção pelo Simples
    01/09 a 15/10/2026; opção pelo regime regular de IBS/CBS ("regime híbrido", só jan–jun/2027) 01/09
    a 30/10/2026; cancelamento 03/11 a 20/12/2026; pendências até 30/10/2026; empresas novas e SIMEI
    fora da janela. Também: 187 (art. 40-A, §6º, parcelas em calamidade), 188 (DAS para ISS até 2032 via
    MAN), 192 (CGIBS na arrecadação, Res. 11/2007); a 193 (Regimento Interno do CGSN) ficou só arquivada.
    O arquivo da 186 é o consolidado (com a redação da 194): a redação original e a conferência com o DOU
    são pendências F20/F21. Regra nova R-erro no CLAUDE.md (todo erro apontado vira LEARNINGS + pergunta de
    teste + pendência de fonte no mesmo PR). Propostas P1/P2 (log de perguntas; varredura de atos novos)
    aguardam decisão: `pendencias.md`, seção F.
- Soluções de Consulta da Receita entram como **interpretação** dos atos do
  domínio (não criam regra), a partir da SC Cosit 71/2026.
- Próximos candidatos: LC 87/1996 (Kandir), LC 116/2003 (ISS), Leis
  10.637/2002 e 10.833/2003 (PIS/Cofins), ainda sem decisão. Pendências em
  `pendencias.md`.
- 2026-10-08: base preparada para a fase de testes antes da 1ª apresentação
  oficial à diretoria.
