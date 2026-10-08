# Contexto fixo

- Escritório de contabilidade, setor fiscal e diretoria
- Carteira concentrada em Comércio, Indústria, Transporte e Serviços.
- Second brain **multi-domínio** (desde 2026-10-06): uma pasta por assunto
  em `notas/<dominio>/`, roteada por `notas/INDEX.md`.
- Domínios ativos:
  - `reforma`: Reforma Tributária (LC 214/2025, atualizada pela LC 227/2026),
    88 notas, origem marcada 🔵 LC 214 · 🟢 LC 227 · 🟡 ambas.
  - `simples-nacional`: LC 123/2006 (fase A, 2026-10-06) + Resolução CGSN
    140/2018 na visão multivigente da Receita, com as Res. CGSN 190 e
    191/2026 (fase B, 2026-10-07): 32 notas `sn-*`. Anexos VI, VII, X, XI e
    XII da Res. 140 ainda não estão nas fontes.
  - `documentos-fiscais` (desde 2026-10-07): 5 Notas Técnicas do Projeto
    NF-e (NT 2025.002-RTC v1.52, 2026.002 v1.11, 2026.007 v1.10, 2026.008
    v1.00 e 2026.010 v1.00), 11 notas `df-*`, incluindo a tabela CST/cClassTrib (173 códigos) capturada
    em 2026-10-08 do Portal da Conformidade Fácil (SVRS), via
    `scripts/cclasstrib_svrs.py`. Falta ainda a tabela cCredPres. Hierarquia: lei > resolução >
    NT. As NTs têm texto riscado; as notas usam o `*-vigente.txt`
    (`scripts/extrair_nt.py`, requer pymupdf). Orientações de NF-e para
    Simples/MEI (CRT 1, 2 e 4) ainda dependem de "NT futura".
- Próximos candidatos a domínio: LC 87/1996 (Kandir), LC 116/2003 (ISS),
  Leis 10.637/2002 e 10.833/2003 (PIS/Cofins), ainda sem decisão.
