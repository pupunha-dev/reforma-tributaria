# Domínio documentos-fiscais (Notas Técnicas NF-e) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar o domínio `documentos-fiscais` (prefixo `df-`) com as 5 Notas Técnicas do Projeto NF-e, de modo que o second brain responda "como preencher e validar NF-e/NFC-e/DANFE na reforma", com versão de cada NT rastreável e datas de produção futuras em blocos ⏳.

**Architecture:** As NTs viram fontes do novo domínio (PDF + texto extraído em duas versões: corrido e `-layout`). Um script novo, `conferir_tags.py`, garante a literalidade dos identificadores técnicos (tags, códigos de regra de validação), no mesmo papel do `conferir_numeros.py`. O `verificar.py` passa a exigir a versão da NT no frontmatter `fontes` das notas `df-*`. As notas seguem o padrão do projeto (frontmatter obrigatório, "A lógica em uma frase", blocos ⏳ e Ligações).

**Tech Stack:** Python 3 (stdlib, unittest), pdftotext (poppler), Markdown.

**Spec:** `docs/superpowers/specs/2026-10-07-fase-b-cgsn-140-e-documentos-fiscais-design.md` (seções 3 e 4).

## Global Constraints

- Prefixo das notas: `df-`; pasta `notas/documentos-fiscais/`; fontes em `fontes/documentos-fiscais/`.
- Nomes dos PDFs: `nt-2025-002-rtc-v1.52.pdf`, `nt-2026-002-v1.11.pdf`, `nt-2026-007-v1.10.pdf`, `nt-2026-008-v1.00.pdf`, `nt-2026-010-v1.00.pdf` (mover com `git mv`; as NTs já estão versionadas em `fontes/simples-nacional/`).
- Frontmatter obrigatório: `título, dominio, fontes, vigencia, texto-base`. `fontes` cita NT **e versão** (ex.: `NT 2025.002-RTC v1.52, seção 6`). `texto-base` = data de captura (2026-10-07).
- Vigência por cronograma: regra ainda não em produção na data-base (07/10/2026) → bloco `## ⏳ Em produção a partir de DD/MM/AAAA — NT N vX (cronograma)`; datas copiadas literalmente da tabela de cronograma.
- Hierarquia: lei > resolução/ato infralegal > nota técnica. A NT diz como preencher/validar; não cria tributo. Divergência com a lei → aviso `> ⚠️ Conflito Lei × NT:` e vale a lei.
- Literalidade técnica: nomes de tags, códigos de regra de validação e de rejeição e fórmulas copiados literalmente; em nota `df-*`, crase (backtick) só para identificador técnico.
- Lacuna explícita: orientações de CRT 1, 2 e 4 (Simples/MEI) "serão publicadas em NT futura" (NT 2025.002); a nota de visão geral e `sn-obrigacoes-acessorias` dizem isso.
- Commits terminam com `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. Código de regra quebrado entre linhas no texto extraído (ex.: `N12-` no fim de uma linha e `50` na seguinte) → `conferir_tags.py` deve reconhecê-lo como `N12-50` (teste na Task 2).
2. Tag citada que só existe como **prefixo** de outra tag na fonte (ex.: nota cita `vIBS`, fonte só tem `vIBSUF`) → deve ser reportada como faltante (teste na Task 2).
3. Crase em nome de arquivo, caminho ou link (`fontes/...`, `sn-mei.md`) → não é identificador técnico e não pode ser reportada (teste na Task 2).
4. Tabela de cronograma com colunas embaralhadas → data atribuída à versão errada. Mitigação: toda data de cronograma usada numa nota é conferida nas **duas** extrações (corrida e `-layout`); se ainda for ambígua, a nota diz que é ambígua (checklist da Task 4).
5. Nota `df-*` sem versão da NT em `fontes` → `verificar.py` acusa erro (teste na Task 2).

---

### Task 1: Fontes do domínio

**Files:**
- Move: `fontes/simples-nacional/Nota Técnica *.pdf` → `fontes/documentos-fiscais/nt-*.pdf` (nomes das Global Constraints)
- Create: `fontes/documentos-fiscais/FONTE.md`
- Create: `fontes/documentos-fiscais/texto/nt-<id>.txt` e `fontes/documentos-fiscais/texto/nt-<id>-layout.txt` (10 arquivos)
- Modify: `fontes/simples-nacional/FONTE.md` (só se citar as NTs)

**Interfaces:**
- Produces: os caminhos de texto acima, usados como `--fontes` pelo `conferir_tags.py` e pelo `conferir_numeros.py` nas Tasks 4 a 6.

- [ ] **Step 1:** `git mv` de cada PDF para o nome normalizado. Conferir versão e mês na capa de cada um (`pdftotext -l 1`): 2025.002-RTC v1.52 set/2026; 2026.002 v1.11 set/2026; 2026.007 v1.10 set/2026; 2026.008 v1.00 set/2026; 2026.010 v1.00 out/2026.
- [ ] **Step 2:** Extrair: `pdftotext -enc UTF-8 <pdf> texto/<id>.txt` e `pdftotext -layout -enc UTF-8 <pdf> texto/<id>-layout.txt`.
- [ ] **Step 3:** `FONTE.md` com tabela: NT, título, versão, mês de publicação, data de captura (07/10/2026), origem (arquivos fornecidos pelo usuário em `fontes/simples-nacional/`, Portal Nacional da NF-e), observações (o leiaute usa `-layout`; Anexos III e IV da NT 2025.002, que são tabelas de cClassTrib e cCredPres, conferir se estão no PDF ou só referenciados).
- [ ] **Step 4:** Verificar: `ls fontes/documentos-fiscais/texto | wc -l` → Expected: 10; `git status` sem PDF de NT em `fontes/simples-nacional/`.
- [ ] **Step 5:** Commit `chore(documentos-fiscais): fontes das Notas Técnicas NF-e (5 NTs)`.

### Task 2: `conferir_tags.py` e versão da NT no `verificar.py`

**Files:**
- Create: `scripts/conferir_tags.py`
- Create: `scripts/tests/test_conferir_tags.py`
- Modify: `scripts/verificar.py` (checagem de versão nas notas `df-*`)
- Modify: `scripts/tests/test_verificar.py`

**Interfaces:**
- Produces: `conferir_tags.identificadores(texto: str) -> set[str]`, `conferir_tags.disponiveis(fonte: str) -> str` (texto normalizado), `conferir_tags.faltantes(nota: str, fontes: list[str]) -> list[str]`; CLI `python scripts/conferir_tags.py <nota.md> --fontes <arq> [...]`, sai 1 se faltar algo. `verificar.checar_versao_nt(raiz: Path) -> list[str]`.

- [ ] **Step 1: testes que falham** (`scripts/tests/test_conferir_tags.py`):

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import conferir_tags as ct  # noqa: E402

FONTE = """Grupo UB. Informações dos tributos IBS / CBS
UB12-10 Rejeição: Informado grupo gIBSCBS sem cClassTrib
campo vIBSUF e vBC. Regras alteradas: B25-80, N12-
50, 1C17-04 e 5E17-65."""


class TestIdentificadores(unittest.TestCase):
    def test_extrai_tags_em_crase_e_codigos_de_regra(self):
        nota = "Preencha `gIBSCBS` e `cClassTrib`; a regra UB12-10 rejeita."
        self.assertEqual(ct.identificadores(nota), {"gIBSCBS", "cClassTrib", "UB12-10"})

    def test_ignora_arquivos_caminhos_e_links(self):
        nota = "Ver `sn-mei.md`, `fontes/documentos-fiscais/texto/x.txt` e [[df-danfe-reforma]]."
        self.assertEqual(ct.identificadores(nota), set())

    def test_ignora_frontmatter_e_exemplo(self):
        nota = "---\nfontes: NT 2025.002-RTC v1.52\n---\n<!-- exemplo -->`vFake`<!-- /exemplo -->\n`vBC`"
        self.assertEqual(ct.identificadores(nota), {"vBC"})


class TestFaltantes(unittest.TestCase):
    def test_tudo_encontrado(self):
        self.assertEqual(ct.faltantes("`gIBSCBS`, `vBC`, UB12-10, B25-80", [FONTE]), [])

    def test_codigo_quebrado_entre_linhas_e_encontrado(self):
        self.assertEqual(ct.faltantes("regra N12-50", [FONTE]), [])

    def test_codigos_com_digito_inicial(self):
        self.assertEqual(ct.faltantes("1C17-04 e 5E17-65", [FONTE]), [])

    def test_tag_que_so_existe_como_prefixo_e_reportada(self):
        self.assertEqual(ct.faltantes("`vIBS`", [FONTE]), ["vIBS"])

    def test_codigo_inexistente_e_reportado(self):
        self.assertEqual(ct.faltantes("UB99-99", [FONTE]), ["UB99-99"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2:** Rodar `python -m unittest scripts/tests/test_conferir_tags.py` → Expected: erro de import (`No module named 'conferir_tags'`).
- [ ] **Step 3: implementação** (`scripts/conferir_tags.py`):

```python
"""Confere se todo identificador técnico de uma nota existe nas Notas Técnicas.

Uso: python scripts/conferir_tags.py <nota.md> --fontes <arquivo> [<arquivo> ...]
Identificadores: tags em crase (ex.: `gIBSCBS`) e códigos de regra de
validação (ex.: UB12-10, 1C17-04). Ignora o frontmatter e blocos
<!-- exemplo --> ... <!-- /exemplo -->. Sai com código 1 se faltar algum.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TAG = re.compile(r"`([A-Za-z][A-Za-z0-9_]*)`")
REGRA = re.compile(r"(?<![\w-])(\d?[A-Z]{1,3}\d{2,3}[a-zA-Z]?-\d{2,3})(?![\w-])")
EXEMPLO = re.compile(r"<!--\s*exemplo\s*-->.*?<!--\s*/exemplo\s*-->", re.S)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
QUEBRA = re.compile(r"-[ \t]*\n[ \t]*(?=\d)")


def identificadores(texto: str) -> set[str]:
    texto = EXEMPLO.sub("", FRONTMATTER.sub("", texto))
    return set(TAG.findall(texto)) | set(REGRA.findall(texto))


def disponiveis(fonte: str) -> str:
    return QUEBRA.sub("-", fonte)


def _existe(ident: str, fontes: list[str]) -> bool:
    padrao = re.compile(r"(?<![\w-])" + re.escape(ident) + r"(?![\w])")
    return any(padrao.search(f) for f in fontes)


def faltantes(nota: str, fontes: list[str]) -> list[str]:
    normalizadas = [disponiveis(f) for f in fontes]
    return sorted(i for i in identificadores(nota) if not _existe(i, normalizadas))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("nota", type=Path)
    parser.add_argument("--fontes", type=Path, nargs="+", required=True)
    args = parser.parse_args(argv[1:])
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    falta = faltantes(args.nota.read_text(encoding="utf-8"),
                      [f.read_text(encoding="utf-8") for f in args.fontes])
    for i in falta:
        print(f"FALTA NAS FONTES  {i}")
    print(f"{len(falta)} identificador(es) sem correspondência em {args.nota.name}")
    return 1 if falta else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4:** Rodar `python -m unittest scripts/tests/test_conferir_tags.py` → Expected: 8 OK.
- [ ] **Step 5: teste que falha da versão da NT** (acrescentar a `scripts/tests/test_verificar.py`, no estilo das classes existentes, criando um `raiz` temporário só com a nota `notas/documentos-fiscais/df-x.md`):

```python
class TestVersaoNT(unittest.TestCase):
    def _raiz(self, fontes):
        tmp = Path(tempfile.mkdtemp())
        pasta = tmp / "notas" / "documentos-fiscais"
        pasta.mkdir(parents=True)
        (pasta / "df-x.md").write_text(
            f"---\ntítulo: X\ndominio: documentos-fiscais\nfontes: {fontes}\n"
            "vigencia: atual\ntexto-base: 2026-10-07\n---\n# X\n", encoding="utf-8")
        return tmp

    def test_fontes_sem_versao_e_erro(self):
        self.assertEqual(len(vf.checar_versao_nt(self._raiz("NT 2025.002-RTC, seção 6"))), 1)

    def test_fontes_com_versao_passa(self):
        self.assertEqual(vf.checar_versao_nt(self._raiz("NT 2025.002-RTC v1.52, seção 6")), [])
```

(usar o alias de import que o arquivo já usa para `verificar`; acrescentar `import tempfile` se faltar.)
- [ ] **Step 6:** Rodar → Expected: FAIL (`has no attribute 'checar_versao_nt'`).
- [ ] **Step 7: implementação** em `scripts/verificar.py`:

```python
VERSAO_NT = re.compile(r"NT \d{4}\.\d{3}(?:-RTC)? v\d+\.\d{2}")


def checar_versao_nt(raiz: Path) -> list[str]:
    pasta = raiz / "notas" / "documentos-fiscais"
    if not pasta.exists():
        return []
    erros = []
    for nota in notas_de_conteudo(pasta):
        fm = ler_frontmatter(nota) or {}
        if not VERSAO_NT.search(fm.get("fontes", "")):
            erros.append(f"{rel(nota, raiz)}: 'fontes' sem NT e versão (ex.: NT 2025.002-RTC v1.52)")
    return erros
```

e somar `checar_versao_nt(raiz)` aos erros em `main` (junto de `checar_frontmatter`).
- [ ] **Step 8:** Rodar `python -m unittest discover -s scripts/tests` → Expected: tudo OK (89 + 10); `python scripts/verificar.py` → 0 erros.
- [ ] **Step 9:** Commit `feat(scripts): conferir_tags.py e versão da NT obrigatória nas notas df-`.

### Task 3: Plano de notas e índice do domínio

**Files:**
- Create: `notas/documentos-fiscais/_plano-notas.md` (frontmatter `título`, `status: aprovado`)
- Create: `notas/documentos-fiscais/INDEX.md`

- [ ] **Step 1:** Ler o sumário e o cronograma das 5 NTs (`-layout`) e montar a tabela **seção da NT → nota**, com coluna de vigência prevista (`atual` ou `com-mudanca-programada`). Ponto de partida da spec (8 a 12 notas): `df-visao-geral-reforma-nfe` (o que mudou, cronograma consolidado, lacuna CRT 1/2/4), `df-grupo-ibs-cbs-is` (leiaute do grupo UB e totais W03/VB), `df-cst-cclasstrib` (CST e cClassTrib; se os Anexos III/IV não estiverem no PDF, a nota diz que são lacuna e só explica o uso), `df-calculo-e-validacoes` (fórmulas e regras de validação), `df-finalidade-debito-credito` (finalidades, notas de débito/crédito), `df-eventos-apuracao` (eventos da seção 8 da NT 2025.002), `df-contribuinte-exclusivo-ibs-cbs` (NT 2026.007), `df-valor-liquido-produto` (NT 2026.008), `df-danfe-reforma` (NT 2026.010 + seção 9 da NT 2025.002), `df-emissao-offline-alerta` (NT 2026.002: autorização com alerta, DANFE Simplificado Tipo 2, limite da NFC-e sem destinatário). Juntar ou separar notas conforme o volume real; toda seção da NT tem dono.
- [ ] **Step 2:** `INDEX.md` com as notas por tema e a regra de hierarquia (lei > resolução > NT).
- [ ] **Step 3:** O usuário delegou a aprovação ("faça o melhor que achar"): registrar no ledger como Ruling.
- [ ] **Step 4:** `python scripts/verificar.py` → Expected: só avisos "citada no _plano-notas.md mas não existe" (o plano está `aprovado`, não `concluido`).
- [ ] **Step 5:** Commit `docs(documentos-fiscais): plano de notas e índice`.

### Task 4: Notas da NT 2025.002-RTC (núcleo)

**Files:** Create as notas da NT 2025.002 definidas no plano (visão geral, grupo UB, CST/cClassTrib, cálculo e validações, finalidade débito/crédito, eventos).

Para **cada** nota:
- [ ] **Step 1:** Redigir com: frontmatter (fontes com NT, versão e seção), "A lógica em uma frase" com analogia, regras e fórmulas completas (o usuário quer a fórmula inteira, não "ver NT"), tags e códigos copiados literalmente em crase, bloco `## ⏳ Em produção a partir de DD/MM/AAAA — NT 2025.002-RTC v1.52 (cronograma)` para o que ainda não está em produção em 07/10/2026 (ex.: obrigatoriedade da RV UB12-10, "implementação futura" → dizer que **não há data**), e Ligações (`[[ibs-cbs-cadastro-documento-fiscal]]`, `[[ibs-cbs-split-payment]]`, `[[sn-obrigacoes-acessorias]]` quando couber).
- [ ] **Step 2:** Toda data de cronograma usada é conferida no `.txt` **e** no `-layout.txt` (Review Focus 4).
- [ ] **Step 3:** `python scripts/conferir_tags.py <nota> --fontes fontes/documentos-fiscais/texto/*.txt` → Expected: 0 faltantes.
- [ ] **Step 4:** `python scripts/conferir_numeros.py <nota> --fontes fontes/documentos-fiscais/texto/*.txt` (mais `fontes/reforma/texto/*` se a nota citar a LC 214) → Expected: 0 faltantes; valores < 1.000 conferidos à mão.
- [ ] **Step 5:** Commit `feat(documentos-fiscais): notas da NT 2025.002-RTC`.

### Task 5: Notas das NTs 2026.002, 2026.007, 2026.008 e 2026.010

**Files:** Create `df-emissao-offline-alerta.md`, `df-contribuinte-exclusivo-ibs-cbs.md`, `df-valor-liquido-produto.md`, `df-danfe-reforma.md` (ou os nomes finais do plano).

- [ ] **Step 1:** Redigir como na Task 4. Datas da data-base (07/10/2026): NT 2026.007 produção 03/11/2026 → ⏳; NT 2026.008 produção 03/11/2026 e regras I11c-10 etc. em 01/03/2027 → ⏳; NT 2026.010 produção 01/12/2026 → ⏳; NT 2026.002: ler o cronograma linha a linha (versões 1.00 a 1.11) e separar o que já está em produção do que não está.
- [ ] **Step 2:** `conferir_tags.py` e `conferir_numeros.py` → 0 faltantes em cada nota.
- [ ] **Step 3:** Plano `status: concluido`; `python scripts/verificar.py` → 0 erros, 0 avisos.
- [ ] **Step 4:** Commit `feat(documentos-fiscais): notas das NTs 2026.002, 2026.007, 2026.008 e 2026.010`.

### Task 6: Protocolo, ligações e perguntas-teste

**Files:**
- Modify: `CLAUDE.md` (linha do domínio na tabela; Escopo inclui "documentação técnica nacional dos documentos fiscais eletrônicos (Notas Técnicas NF-e/NFC-e)"; R-hierarquia: "lei > resolução/ato infralegal > nota técnica"; legenda do bloco ⏳ por cronograma)
- Modify: `MEMORY.md`, `notas/INDEX.md` (bloco do domínio), `docs/procedimento-nova-legislacao.md` (seção "Notas Técnicas": versão no frontmatter, cronograma, `-layout`, `conferir_tags.py`, atualização de versão = nova extração + histórico de alterações + revisar só notas afetadas)
- Modify: `notas/simples-nacional/sn-obrigacoes-acessorias.md` (frontmatter `fontes` + link `[[df-visao-geral-reforma-nfe]]` no aviso da NT; resolve o minor adiado da Parte 1), `notas/simples-nacional/sn-declaracoes-pgdas-defis.md` (link no aviso de CBS/IBS pré-preenchidos), notas da reforma `ibs-cbs-cadastro-documento-fiscal` (link para o domínio)
- Create: `docs/perguntas-teste/documentos-fiscais.md` (D1–D10)

- [ ] **Step 1:** Edições acima (com Edit; não reescrever arquivos com `Path.read_text` + `write_text` em arquivos que possam ter `\r` — lição da Parte 1).
- [ ] **Step 2:** Perguntas D1–D10: preenchimento de um campo do grupo IBS/CBS; uma regra de validação (código); uma data de produção futura (DANFE 01/12/2026); contribuinte só de IBS/CBS sem IE (NT 2026.007); valor líquido do produto; lacuna do Simples/MEI (CRT 1/2/4 → NT futura); autorização com alerta; cruzamento com a reforma (split payment × NF-e); fora de escopo (regra estadual de ICMS de uma UF); hierarquia (NT × lei).
- [ ] **Step 3:** `python scripts/verificar.py` → 0/0; `python -m unittest discover -s scripts/tests` → OK.
- [ ] **Step 4:** Rodar D1–D10 + regressão R1–R5 + S10, S16 com `claude -p` (3 em paralelo) → Expected: todos citam a nota esperada e o comportamento confere; falha real → corrigir nota/protocolo e registrar no ledger.
- [ ] **Step 5:** Commit `docs(documentos-fiscais): protocolo, ligações e perguntas-teste`.

### Final

- [ ] Revisão de todo o branch da Parte 2 por revisor novo (opus), correções Critical/Important com RED→GREEN, minors no ledger.
- [ ] Merge local em `main` e push (autorizado pelo usuário: "suba tudo pro repositorio quando estiver pronto").
