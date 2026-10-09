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
    2026-10-08) + Res. CGSN 11/2007 (arrecadação, texto original): 35 notas `sn-*`. Anexos VII, X e XII ainda não estão nas
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
- Soluções de Consulta da Receita entram como **interpretação** dos atos do
  domínio (não criam regra), a partir da SC Cosit 71/2026.
- Próximos candidatos: LC 87/1996 (Kandir), LC 116/2003 (ISS), Leis
  10.637/2002 e 10.833/2003 (PIS/Cofins), ainda sem decisão. Pendências em
  `pendencias.md`.
- 2026-10-08: base preparada para a fase de testes antes da 1ª apresentação
  oficial à diretoria.
