# Multi-domínio + LC 123 (fase A1: infraestrutura e preparação) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transformar o second brain em estrutura multi-domínio sem perder nada das 87 notas da reforma, e preparar a LC 123 até o plano de notas (etapas 1 a 4 do procedimento), parando para a aprovação do usuário.

**Architecture:** Cada domínio (assunto) fica numa subpasta de `notas/` e de `fontes/`. Um índice mestre e o CLAUDE.md fazem só o roteamento. Dois scripts em Python, usando só a biblioteca padrão, garantem a integridade: `verificar.py` checa links, nomes, frontmatter e cobertura, e `esqueleto.py` extrai artigos e marcas de alteração do texto legal. A redação das notas `sn-*` (etapas 5 a 7) fica **fora** deste plano: ela depende do `_plano-notas.md` aprovado no fim da Task 8 e terá um plano próprio (fase A2).

**Tech Stack:** Markdown, Python 3.14 (stdlib + `unittest`), `pdftotext` (poppler, já disponível no Git Bash em `/mingw64/bin`), git/GitHub, `claude -p` para a regressão.

**Spec:** `docs/superpowers/specs/2026-10-06-expansao-multi-legislacao-design.md`

## Global Constraints

- Python **só com a biblioteca padrão**: nada de `pip install`. Testes com `unittest` (`python -m unittest discover -s scripts/tests -v`).
- Extração de PDF: `pdftotext -enc UTF-8 <pdf> <txt>`, **sem** `-layout`.
- Quebra de linha LF em todos os arquivos de texto (`.gitattributes` já tem `* text=auto eol=lf`).
- **O conteúdo das 87 notas da reforma não é reescrito.** As únicas mudanças permitidas estão listadas na Task 3, Step 3.
- O nome de arquivo de nota é **único no projeto inteiro**. Notas novas do Simples usam o prefixo `sn-`. As notas da reforma não ganham prefixo.
- Links entre notas: sempre `[[nome]]`, sem `.md`. No `_plano-notas.md`, referências a notas de **outro** domínio também são `[[nome]]`.
- Frontmatter obrigatório nas notas fora de `notas/reforma/`: `título`, `dominio`, `fontes`, `vigencia` (`atual` | `com-mudanca-programada`), `texto-base` (AAAA-MM-DD).
- Bloco de redação futura: `## ⏳ A partir de DD/MM/AAAA — redação dada pela <lei> (art. N)`. Revogação programada: `## ❌ Revogado a partir de DD/MM/AAAA — <lei> (art. N)`.
- Escopo: só atos normativos federais.
- Toda mensagem de commit termina com a linha `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Repositório remoto: `https://github.com/pupunha-dev/reforma-tributaria.git`, branch `main`. O commit de segurança `32aad9a` já foi enviado.

## Review Focus

1. **Redação superada lida como vigente:** o PDF compilado traz a redação antiga e a nova do mesmo dispositivo uma depois da outra, sem o risco. O `esqueleto.py` precisa contar as versões. Teste na Task 5: `test_detecta_redacao_anterior_e_nova_do_mesmo_dispositivo`.
2. **"Produção de efeitos" sem data:** a marca não traz data e não pode ser tratada como "já vigente". O esqueleto classifica como `efeitos-sem-data`, e o mapa (Task 7) resolve a data pelo artigo alterador. Teste na Task 5: `test_marca_producao_de_efeitos_sem_data`.
3. **Cabeçalho/rodapé de impressão no meio do texto** (data/hora, "2/44", URL, "Lcp 123"): não pode virar parágrafo nem quebrar a análise. Teste na Task 5: `test_remove_ruido_de_impressao`.
4. **Wikilink com `.md` ou nome ambíguo:** já existe um caso real (`[[simples-nacional-e-mei.md]]`). O script precisa acusar. Teste na Task 1: `test_wikilink_com_extensao_md_e_erro`.
5. **Links de exemplo dentro de blocos de código** (specs, procedimento) não podem gerar falso erro. Teste na Task 1: `test_ignora_links_dentro_de_codigo`.

---

## Mapa de arquivos

| Arquivo | Responsabilidade | Task |
|---|---|---|
| `scripts/verificar.py` | Checagens estruturais (links, nomes, frontmatter, cobertura) + CLI | 1, 2 |
| `scripts/tests/test_verificar.py` | Testes do verificar | 1, 2 |
| `notas/reforma/**` | As 87 notas + INDEX + plano, movidos | 3 |
| `fontes/reforma/`, `fontes/simples-nacional/` | PDFs por domínio | 3 |
| `notas/INDEX.md` | Índice mestre (roteamento por domínio) | 3, 8 |
| `CLAUDE.md`, `MEMORY.md` | Protocolo multi-domínio | 4 |
| `docs/perguntas-teste/reforma.md` | Regressão do domínio reforma | 4 |
| `docs/procedimento-nova-legislacao.md` | A receita das 7 etapas | 4 |
| `scripts/esqueleto.py` | Artigos e marcas de alteração de um `.txt` legal | 5 |
| `scripts/tests/test_esqueleto.py` | Testes do esqueleto | 5 |
| `fontes/simples-nacional/FONTE.md` | Origem e data de captura das fontes | 6 |
| `fontes/simples-nacional/texto/*` | Texto extraído + esqueleto da LC 123 | 6 |
| `fontes/reforma/texto/lc-214-2025.txt` | Texto da LC 214, usado para resolver a vigência | 7 |
| `notas/simples-nacional/_mapa-vigencia.md` | Dispositivo → data de efeitos | 7 |
| `notas/simples-nacional/_plano-notas.md` | Arquivo → artigos → profundidade (para aprovação) | 8 |

---

### Task 1: `verificar.py`: links e nomes únicos

**Files:**
- Create: `scripts/verificar.py`
- Test: `scripts/tests/test_verificar.py`

**Interfaces:**
- Produces: `checar_links(raiz: Path) -> list[str]`, `checar_nomes_unicos(raiz: Path) -> list[str]`, `sem_codigo(texto: str) -> str`, `notas(raiz: Path) -> list[Path]`, `notas_de_conteudo(pasta: Path) -> list[Path]`, `rel(p: Path, raiz: Path) -> str`. Cada item da lista devolvida é uma mensagem de erro legível. Lista vazia = ok.

- [ ] **Step 1: Escrever os testes que falham**

`scripts/tests/test_verificar.py`:

```python
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import verificar as v  # noqa: E402

FM_OK = (
    "---\n"
    "título: X\n"
    "dominio: simples-nacional\n"
    "fontes: LC 123/2006, art. 1º\n"
    "vigencia: atual\n"
    "texto-base: 2026-10-06\n"
    "---\n\n# X\n"
)


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def criar(self, caminho, texto=""):
        p = self.raiz / caminho
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(texto, encoding="utf-8")
        return p


class TestLinks(Base):
    def test_wikilink_valido_entre_dominios(self):
        self.criar("notas/reforma/a.md", "ver [[sn-b]]")
        self.criar("notas/simples-nacional/sn-b.md", "ver [[a]]")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_wikilink_inexistente(self):
        self.criar("notas/reforma/a.md", "ver [[nao-existe]]")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("[[nao-existe]] não encontrado", erros[0])

    def test_wikilink_com_extensao_md_e_erro(self):
        self.criar("notas/reforma/a.md", "ver [[b.md]]")
        self.criar("notas/reforma/b.md")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("use o nome sem .md", erros[0])

    def test_wikilink_com_alias_e_ancora(self):
        self.criar("notas/reforma/a.md", "[[b|texto]] e [[b#seção]]")
        self.criar("notas/reforma/b.md")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_link_markdown_relativo(self):
        self.criar("LEARNINGS.md", "[x](notas/reforma/a.md) e [y](notas/a.md)")
        self.criar("notas/reforma/a.md")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("notas/a.md", erros[0])

    def test_link_markdown_externo_e_ignorado(self):
        self.criar("notas/reforma/a.md", "[x](https://exemplo.gov.br/lei.md)")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_ignora_links_dentro_de_codigo(self):
        self.criar("notas/reforma/a.md", "`[[fantasma]]`\n```\n[x](nada.md)\n```\n")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_ignora_docs_superpowers(self):
        self.criar("docs/superpowers/specs/s.md", "[[fantasma]]")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_verifica_docs_fora_de_superpowers(self):
        self.criar("docs/procedimento-nova-legislacao.md", "[[fantasma]]")
        self.assertEqual(len(v.checar_links(self.raiz)), 1)


class TestNomesUnicos(Base):
    def test_nome_repetido_em_dominios_diferentes(self):
        self.criar("notas/reforma/aliquotas.md")
        self.criar("notas/simples-nacional/aliquotas.md")
        erros = v.checar_nomes_unicos(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("aliquotas", erros[0])

    def test_index_e_arquivos_de_trabalho_podem_repetir(self):
        for d in ("reforma", "simples-nacional"):
            self.criar(f"notas/{d}/INDEX.md")
            self.criar(f"notas/{d}/_plano-notas.md")
        self.assertEqual(v.checar_nomes_unicos(self.raiz), [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Rodar e confirmar que falha**

Run: `python -m unittest discover -s scripts/tests -v`
Expected: ERROR com `ModuleNotFoundError: No module named 'verificar'`

- [ ] **Step 3: Implementar**

`scripts/verificar.py`:

```python
"""Checagens estruturais do second brain.

Uso: python scripts/verificar.py [raiz]
Imprime ERRO/AVISO e sai com código 1 se houver algum erro.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
MDLINK = re.compile(r"\]\(([^)\s]+?\.md)(?:#[^)]*)?\)")
BLOCO_CODIGO = re.compile(r"```.*?```", re.S)
CODIGO_INLINE = re.compile(r"`[^`\n]*`")

ARQUIVOS_RAIZ = ("CLAUDE.md", "MEMORY.md", "LEARNINGS.md", "decisions.md")


def rel(p: Path, raiz: Path) -> str:
    return p.relative_to(raiz).as_posix()


def sem_codigo(texto: str) -> str:
    """Remove blocos e trechos de código, onde links são só exemplo."""
    return CODIGO_INLINE.sub("", BLOCO_CODIGO.sub("", texto))


def notas(raiz: Path) -> list[Path]:
    pasta = raiz / "notas"
    return sorted(pasta.rglob("*.md")) if pasta.exists() else []


def notas_de_conteudo(pasta: Path) -> list[Path]:
    """Notas de um domínio, sem INDEX.md e sem arquivos de trabalho (_*.md)."""
    return sorted(
        p for p in pasta.glob("*.md")
        if p.name != "INDEX.md" and not p.name.startswith("_")
    )


def _arquivos_com_links(raiz: Path) -> list[Path]:
    arquivos = notas(raiz)
    arquivos += [raiz / n for n in ARQUIVOS_RAIZ if (raiz / n).exists()]
    docs = raiz / "docs"
    if docs.exists():
        arquivos += sorted(
            p for p in docs.rglob("*.md")
            if "superpowers" not in p.relative_to(docs).parts
        )
    return arquivos


def checar_nomes_unicos(raiz: Path) -> list[str]:
    vistos: dict[str, Path] = {}
    erros = []
    for p in notas(raiz):
        if p.name == "INDEX.md" or p.name.startswith("_"):
            continue
        if p.stem in vistos:
            erros.append(f"nome duplicado: {rel(p, raiz)} e {rel(vistos[p.stem], raiz)}")
        else:
            vistos[p.stem] = p
    return erros


def checar_links(raiz: Path) -> list[str]:
    por_nome: dict[str, list[Path]] = {}
    for p in notas(raiz):
        por_nome.setdefault(p.stem, []).append(p)

    erros = []
    for arq in _arquivos_com_links(raiz):
        origem = rel(arq, raiz)
        texto = sem_codigo(arq.read_text(encoding="utf-8"))
        for alvo in WIKILINK.findall(texto):
            alvo = alvo.strip()
            if alvo.endswith(".md"):
                erros.append(f"{origem}: [[{alvo}]] — use o nome sem .md")
                continue
            achados = por_nome.get(alvo, [])
            if not achados:
                erros.append(f"{origem}: [[{alvo}]] não encontrado")
            elif len(achados) > 1:
                caminhos = ", ".join(rel(a, raiz) for a in achados)
                erros.append(f"{origem}: [[{alvo}]] ambíguo ({caminhos})")
        for alvo in MDLINK.findall(texto):
            if "://" in alvo:
                continue
            if not (arq.parent / alvo).exists():
                erros.append(f"{origem}: link ({alvo}) aponta para arquivo inexistente")
    return erros
```

- [ ] **Step 4: Rodar e confirmar que passa**

Run: `python -m unittest discover -s scripts/tests -v`
Expected: 11 testes, todos `ok`

- [ ] **Step 5: Commit**

```bash
git add scripts/verificar.py scripts/tests/test_verificar.py
git commit -m "feat: verificar.py checa links e nomes únicos de notas

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: `verificar.py`: frontmatter, cobertura, CLI e linha de base

**Files:**
- Modify: `scripts/verificar.py`
- Test: `scripts/tests/test_verificar.py`

**Interfaces:**
- Consumes: `notas_de_conteudo`, `rel`, `checar_links`, `checar_nomes_unicos` (Task 1).
- Produces: `ler_frontmatter(caminho: Path) -> dict[str, str] | None`, `checar_frontmatter(raiz: Path) -> list[str]`, `checar_cobertura(raiz: Path) -> tuple[list[str], list[str]]` (erros, avisos), `main(argv: list[str]) -> int`. Regra de cobertura: o `_plano-notas.md` com `status: concluido` transforma nota planejada e ausente em **erro**; com qualquer outro status, em **aviso**.

- [ ] **Step 1: Escrever os testes que falham** (acrescentar ao fim de `scripts/tests/test_verificar.py`, antes do `if __name__`)

```python
class TestFrontmatter(Base):
    def nota(self, texto):
        self.criar("notas/simples-nacional/sn-a.md", texto)
        return v.checar_frontmatter(self.raiz)

    def test_nota_completa_passa(self):
        self.assertEqual(self.nota(FM_OK), [])

    def test_campo_ausente(self):
        erros = self.nota(FM_OK.replace("vigencia: atual\n", ""))
        self.assertEqual(len(erros), 1)
        self.assertIn("'vigencia'", erros[0])

    def test_vigencia_invalida(self):
        erros = self.nota(FM_OK.replace("vigencia: atual", "vigencia: futura"))
        self.assertEqual(len(erros), 1)
        self.assertIn("vigencia", erros[0])

    def test_texto_base_com_comentario_e_valido(self):
        texto = FM_OK.replace("texto-base: 2026-10-06", "texto-base: 2026-10-06   # captura")
        self.assertEqual(self.nota(texto), [])

    def test_texto_base_fora_do_formato(self):
        erros = self.nota(FM_OK.replace("2026-10-06", "06/10/2026"))
        self.assertEqual(len(erros), 1)
        self.assertIn("texto-base", erros[0])

    def test_dominio_diferente_da_pasta(self):
        erros = self.nota(FM_OK.replace("dominio: simples-nacional", "dominio: reforma"))
        self.assertEqual(len(erros), 1)
        self.assertIn("dominio", erros[0])

    def test_sem_frontmatter(self):
        erros = self.nota("# só título\n")
        self.assertEqual(len(erros), 1)
        self.assertIn("sem frontmatter", erros[0])

    def test_dominio_legado_reforma_e_isento(self):
        self.criar("notas/reforma/x.md", "---\ntítulo: X\norigem: LC 214\n---\n")
        self.assertEqual(v.checar_frontmatter(self.raiz), [])

    def test_index_e_arquivos_de_trabalho_isentos(self):
        self.criar("notas/simples-nacional/INDEX.md", "# Índice\n")
        self.criar("notas/simples-nacional/_plano-notas.md", "# Plano\n")
        self.assertEqual(v.checar_frontmatter(self.raiz), [])


PLANO = (
    "---\ntítulo: Plano\nstatus: {status}\n---\n"
    "| sn-a.md | 1–2 |\n| sn-b.md | 3 |\n"
    "Ponte: [[simples-nacional-e-mei]]\n"
)


class TestCobertura(Base):
    def dominio(self, status, notas_existentes):
        self.criar("notas/simples-nacional/_plano-notas.md", PLANO.format(status=status))
        for n in notas_existentes:
            self.criar(f"notas/simples-nacional/{n}", FM_OK)
        return v.checar_cobertura(self.raiz)

    def test_tudo_coberto(self):
        self.assertEqual(self.dominio("concluido", ["sn-a.md", "sn-b.md"]), ([], []))

    def test_nota_fora_do_plano_e_erro(self):
        erros, avisos = self.dominio("aprovado", ["sn-a.md", "sn-b.md", "sn-c.md"])
        self.assertEqual(len(erros), 1)
        self.assertIn("sn-c.md", erros[0])
        self.assertEqual(avisos, [])

    def test_planejada_ausente_e_aviso_enquanto_nao_concluido(self):
        erros, avisos = self.dominio("aguardando-aprovacao", ["sn-a.md"])
        self.assertEqual(erros, [])
        self.assertEqual(len(avisos), 1)
        self.assertIn("sn-b.md", avisos[0])

    def test_planejada_ausente_e_erro_quando_concluido(self):
        erros, avisos = self.dominio("concluido", ["sn-a.md"])
        self.assertEqual(len(erros), 1)
        self.assertIn("sn-b.md", erros[0])

    def test_dominio_com_notas_sem_plano(self):
        self.criar("notas/simples-nacional/sn-a.md", FM_OK)
        erros, _ = v.checar_cobertura(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("_plano-notas.md", erros[0])


class TestMain(Base):
    def test_saida_zero_sem_erros(self):
        self.criar("notas/reforma/a.md", "[[b]]")
        self.criar("notas/reforma/b.md")
        self.criar("notas/reforma/_plano-notas.md", "| a.md |\n| b.md |\n")
        self.assertEqual(v.main(["verificar.py", str(self.raiz)]), 0)

    def test_saida_um_com_erro(self):
        self.criar("notas/reforma/a.md", "[[fantasma]]")
        self.criar("notas/reforma/_plano-notas.md", "| a.md |\n")
        self.assertEqual(v.main(["verificar.py", str(self.raiz)]), 1)
```

- [ ] **Step 2: Rodar e confirmar que falha**

Run: `python -m unittest discover -s scripts/tests -v`
Expected: os testes novos falham com `AttributeError: module 'verificar' has no attribute 'checar_frontmatter'` (ou `checar_cobertura` / `main`). Os 11 da Task 1 continuam `ok`.

- [ ] **Step 3: Implementar** (acrescentar a `scripts/verificar.py`)

Junto das outras constantes no topo do arquivo:

```python
NOME_NOTA = re.compile(r"(?<![\w/.-])([a-z0-9][a-z0-9-]*\.md)\b")
DATA_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CAMPOS_OBRIGATORIOS = ("título", "dominio", "fontes", "vigencia", "texto-base")
VIGENCIAS_VALIDAS = ("atual", "com-mudanca-programada")
DOMINIOS_LEGADOS = ("reforma",)
```

No fim do arquivo:

```python
def dominios(raiz: Path) -> list[Path]:
    pasta = raiz / "notas"
    return sorted(p for p in pasta.iterdir() if p.is_dir()) if pasta.exists() else []


def ler_frontmatter(caminho: Path) -> dict[str, str] | None:
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    if not linhas or linhas[0].strip() != "---":
        return None
    campos: dict[str, str] = {}
    for linha in linhas[1:]:
        if linha.strip() == "---":
            return campos
        if ":" in linha and not linha.startswith((" ", "\t")):
            chave, valor = linha.split(":", 1)
            campos[chave.strip()] = valor.split("#", 1)[0].strip()
    return None


def checar_frontmatter(raiz: Path) -> list[str]:
    erros = []
    for pasta in dominios(raiz):
        if pasta.name in DOMINIOS_LEGADOS:
            continue
        for nota in notas_de_conteudo(pasta):
            r = rel(nota, raiz)
            fm = ler_frontmatter(nota)
            if fm is None:
                erros.append(f"{r}: sem frontmatter")
                continue
            for campo in CAMPOS_OBRIGATORIOS:
                if not fm.get(campo):
                    erros.append(f"{r}: campo '{campo}' ausente ou vazio")
            if fm.get("dominio") and fm["dominio"] != pasta.name:
                erros.append(f"{r}: dominio '{fm['dominio']}' difere da pasta '{pasta.name}'")
            if fm.get("vigencia") and fm["vigencia"] not in VIGENCIAS_VALIDAS:
                erros.append(f"{r}: vigencia '{fm['vigencia']}' inválida (use {' | '.join(VIGENCIAS_VALIDAS)})")
            if fm.get("texto-base") and not DATA_ISO.match(fm["texto-base"]):
                erros.append(f"{r}: texto-base '{fm['texto-base']}' fora do formato AAAA-MM-DD")
    return erros


def checar_cobertura(raiz: Path) -> tuple[list[str], list[str]]:
    erros: list[str] = []
    avisos: list[str] = []
    for pasta in dominios(raiz):
        existentes = {p.name for p in notas_de_conteudo(pasta)}
        plano = pasta / "_plano-notas.md"
        if not plano.exists():
            if existentes:
                erros.append(f"notas/{pasta.name}: há notas mas não há _plano-notas.md")
            continue
        citadas = {
            n for n in NOME_NOTA.findall(plano.read_text(encoding="utf-8"))
            if n != "INDEX.md" and not n.startswith("_")
        }
        concluido = (ler_frontmatter(plano) or {}).get("status") == "concluido"
        for n in sorted(existentes - citadas):
            erros.append(f"notas/{pasta.name}/{n}: nota fora do _plano-notas.md")
        for n in sorted(citadas - existentes):
            msg = f"notas/{pasta.name}/{n}: citada no _plano-notas.md mas não existe"
            (erros if concluido else avisos).append(msg)
    return erros, avisos


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raiz = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    erros = checar_nomes_unicos(raiz) + checar_links(raiz) + checar_frontmatter(raiz)
    erros_cobertura, avisos = checar_cobertura(raiz)
    erros += erros_cobertura
    for a in avisos:
        print(f"AVISO  {a}")
    for e in erros:
        print(f"ERRO   {e}")
    print(f"\n{len(erros)} erro(s), {len(avisos)} aviso(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Rodar os testes e confirmar que passam**

Run: `python -m unittest discover -s scripts/tests -v`
Expected: 27 testes, todos `ok`

- [ ] **Step 5: Linha de base no projeto atual (antes da migração)**

Run: `python scripts/verificar.py`
Expected, exatamente:
```
ERRO   notas/lc227-alteracoes-legislacao-correlata.md: [[simples-nacional-e-mei.md]] — use o nome sem .md

1 erro(s), 0 aviso(s)
```
Esse erro já existia (um link com `.md`) e é corrigido na Task 3. Se aparecer **qualquer outro** erro, pare e investigue antes de migrar.

- [ ] **Step 6: Commit**

```bash
git add scripts/verificar.py scripts/tests/test_verificar.py
git commit -m "feat: verificar.py checa frontmatter, cobertura do plano e expõe CLI

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Migrar a reforma para `notas/reforma/` e `fontes/reforma/`

**Files:**
- Move: `notas/*.md` → `notas/reforma/` (87 notas + `INDEX.md` + `_plano-notas.md`)
- Move: `fontes/lc-214-2025-texto-compilado.pdf`, `fontes/lc-227-2026.pdf` → `fontes/reforma/`
- Move: `fontes/lc-123.pdf` → `fontes/simples-nacional/lc-123-2006-texto-compilado.pdf`
- Move: `fontes/resolucao-cgsn-140-2018.pdf` → `fontes/simples-nacional/resolucao-cgsn-140-2018-dou-original.pdf`
- Move (ainda não versionados): `fontes/Resolução CGSN nº 190, ….pdf` → `fontes/simples-nacional/resolucao-cgsn-190-2026-dou.pdf`; `fontes/Resolução CGSN Nº 191, ….pdf` → `fontes/simples-nacional/resolucao-cgsn-191-2026-dou.pdf`
- Modify: `notas/reforma/ibs-cbs-fim-substituicao-tributaria.md:35`, `notas/reforma/lc227-alteracoes-legislacao-correlata.md:9`, `notas/reforma/_plano-notas.md:46`, `LEARNINGS.md`, `CLAUDE.md`
- Create: `notas/INDEX.md` (índice mestre)

**Interfaces:**
- Consumes: `python scripts/verificar.py` (Task 2).
- Produces: estrutura `notas/<dominio>/`, `fontes/<dominio>/`, usada por todas as tasks seguintes.

- [ ] **Step 1: Mover com `git mv`** (preserva o histórico)

```bash
mkdir -p notas/reforma fontes/reforma fontes/simples-nacional
git mv notas/*.md notas/reforma/
git mv fontes/lc-214-2025-texto-compilado.pdf fontes/lc-227-2026.pdf fontes/reforma/
git mv fontes/lc-123.pdf fontes/simples-nacional/lc-123-2006-texto-compilado.pdf
git mv fontes/resolucao-cgsn-140-2018.pdf fontes/simples-nacional/resolucao-cgsn-140-2018-dou-original.pdf
mv fontes/Resolu*190,*.pdf fontes/simples-nacional/resolucao-cgsn-190-2026-dou.pdf
mv fontes/Resolu*191,*.pdf fontes/simples-nacional/resolucao-cgsn-191-2026-dou.pdf
ls fontes   # esperado: só as pastas reforma/ e simples-nacional/
```

- [ ] **Step 2: Rodar o verificar e ver o que quebrou**

Run: `python scripts/verificar.py`
Expected: erros apontando `../LEARNINGS.md` em `ibs-cbs-fim-substituicao-tributaria.md`, `notas/...` em `LEARNINGS.md` e `CLAUDE.md`, o `[[simples-nacional-e-mei.md]]` e `ibs-cbs-fim-substituicao-tributaria.md: nota fora do _plano-notas.md`.

- [ ] **Step 3: Aplicar as correções permitidas** (são as **únicas** mudanças de conteúdo da migração)

1. `notas/reforma/ibs-cbs-fim-substituicao-tributaria.md`: trocar `[LEARNINGS.md](../LEARNINGS.md)` por `[LEARNINGS.md](../../LEARNINGS.md)`.
2. `notas/reforma/lc227-alteracoes-legislacao-correlata.md`: trocar `[[simples-nacional-e-mei.md]]` por `[[simples-nacional-e-mei]]`.
3. `notas/reforma/_plano-notas.md`: logo depois da linha `| ibs-cbs-split-payment.md | 31–35 | 🟡 |`, inserir:
   ```
   | ibs-cbs-fim-substituicao-tributaria.md | 31–35 (conceitual; nota criada após o plano) | 🟡 |
   ```
4. `LEARNINGS.md`: `](notas/icms-st-estoque-2032.md)` → `](notas/reforma/icms-st-estoque-2032.md)`; `](notas/regime-especifico-bens-imoveis.md)` → `](notas/reforma/regime-especifico-bens-imoveis.md)`; `](notas/transicao-operacoes-bens-imoveis.md)` → `](notas/reforma/transicao-operacoes-bens-imoveis.md)`; `` `fontes/lc-214-2025-texto-compilado.pdf` `` → `` `fontes/reforma/lc-214-2025-texto-compilado.pdf` ``.
5. `CLAUDE.md` (ajuste mínimo; a reescrita completa é na Task 4): `](notas/_plano-notas.md)` → `](notas/reforma/_plano-notas.md)`.

- [ ] **Step 4: Criar o índice mestre `notas/INDEX.md`**

```markdown
---
título: Índice mestre — second brain tributário
---

# Índice mestre

O second brain é organizado por **domínio** (assunto). Cada domínio tem a
própria pasta de notas, o próprio índice e o próprio plano de notas (mapa
artigo → nota). Comece pelo domínio da pergunta; se ela cruzar domínios,
use os dois.

## Reforma Tributária — LC 214/2025 + LC 227/2026

- Índice: [reforma/INDEX.md](reforma/INDEX.md) — 87 notas, 11 áreas
- Mapa de artigos: [reforma/_plano-notas.md](reforma/_plano-notas.md)
- Legenda: 🔵 só LC 214/2025 · 🟡 ambas (227 alterou dispositivo da 214) · 🟢 só LC 227/2026
- Fontes: `fontes/reforma/`

## Simples Nacional — LC 123/2006 + Resolução CGSN 140/2018

- Status: **em implantação** (fase A — LC 123). Ainda não há notas; perguntas
  sobre o domínio são respondidas como lacuna, com consulta ao texto em
  `fontes/simples-nacional/`.
- Ponte com a reforma: [[simples-nacional-e-mei]]
- Fontes: `fontes/simples-nacional/`
```

- [ ] **Step 5: Verificar a estrutura**

Run: `python scripts/verificar.py`
Expected: `0 erro(s), 0 aviso(s)`

Run: `ls notas/reforma/*.md | grep -v -E "/(INDEX|_plano-notas)\.md$" | wc -l`
Expected: `87`

- [ ] **Step 6: Provar que nenhum conteúdo se perdeu** (compara cada arquivo do commit de segurança com o arquivo migrado)

```bash
for f in $(git ls-tree --name-only HEAD notas/); do
  n=$(basename "$f")
  git show "HEAD:$f" | diff -q - "notas/reforma/$n" >/dev/null && echo "igual  $n" || echo "MUDOU  $n"
done | grep -c "^igual"
for f in $(git ls-tree --name-only HEAD notas/); do
  n=$(basename "$f")
  git show "HEAD:$f" | diff -q - "notas/reforma/$n" >/dev/null || echo "MUDOU  $n"
done
```
Expected: `86`, e depois exatamente estas três linhas:
```
MUDOU  _plano-notas.md
MUDOU  ibs-cbs-fim-substituicao-tributaria.md
MUDOU  lc227-alteracoes-legislacao-correlata.md
```
São 89 arquivos no total (87 notas + INDEX + plano): 86 iguais e 3 com mudança. Depois confira que cada uma das três tem só a linha prevista:

Run: `for n in _plano-notas ibs-cbs-fim-substituicao-tributaria lc227-alteracoes-legislacao-correlata; do git show "HEAD:notas/$n.md" | diff - "notas/reforma/$n.md"; done`
Expected: só as linhas dos itens 1 a 3 do Step 3 aparecem no diff.

- [ ] **Step 7: Commit e push**

```bash
git add -A
git commit -m "refactor: migra reforma para notas/reforma e fontes por domínio

Estrutura multi-domínio: notas/<dominio>/ e fontes/<dominio>/, índice
mestre em notas/INDEX.md. Conteúdo das 87 notas inalterado, exceto:
link relativo para LEARNINGS, wikilink com .md e a linha da nota de ST
no plano.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push
```

---

### Task 4: Protocolo multi-domínio (CLAUDE.md, MEMORY.md, procedimento, regressão)

**Files:**
- Modify (reescrita completa): `CLAUDE.md`
- Modify: `MEMORY.md`
- Create: `docs/procedimento-nova-legislacao.md`
- Create: `docs/perguntas-teste/reforma.md`

**Interfaces:**
- Consumes: estrutura da Task 3; `verificar.py`.
- Produces: regras R-domínio/R-vigência/R-hierarquia/R-cruzamento que as notas e respostas futuras seguem; o formato de `docs/perguntas-teste/<dominio>.md`, reaproveitado na fase A2.

- [ ] **Step 1: Escrever a bateria de regressão `docs/perguntas-teste/reforma.md`** (o "teste que falha" desta task: ela precisa passar **depois** da troca do CLAUDE.md)

```markdown
# Perguntas-teste — domínio reforma

Rodar depois de qualquer mudança no protocolo (CLAUDE.md) ou na estrutura.
Cada pergunta é feita numa sessão nova, na raiz do projeto:

    claude -p "<pergunta>" > saida.txt

e a saída precisa conter **todos** os termos da coluna "deve citar" e
respeitar o comportamento esperado.

| # | Pergunta | Deve citar | Comportamento esperado |
|---|---|---|---|
| R1 | Qual a alíquota de referência do IBS em 2031? | `transicao-fixacao-aliquotas` | Aponta lacuna (arts. 353–365 não detalhados na nota) e oferece consultar o PDF; não inventa percentual |
| R2 | Quais produtos tinham ST do ICMS e deixaram de ter com a reforma? | `ibs-cbs-fim-substituicao-tributaria` | Explica o porquê conceitual (split payment) e sinaliza a lista de produtos como fora de escopo |
| R3 | O que muda no IR do aluguel com a reforma? | `regime-especifico-bens-imoveis` | Sinaliza IR como fora de escopo; responde só a parte de IBS/CBS |
| R4 | Como o MEI recolhe o IBS e para quem vai o dinheiro? | `simples-nacional-e-mei` | 50% ao Município/DF e 50% ao Estado/DF (art. 22, V e VI da LC 123, red. LC 227) |
| R5 | Quem fixa a alíquota do IBS de um Município? | `ibs-cbs-aliquotas` | Lei municipal (art. 14), vinculável à alíquota de referência |
```

- [ ] **Step 2: Rodar R1 a R5 com o CLAUDE.md atual (linha de base)**

```bash
mkdir -p "$TMPDIR/regressao"
claude -p "Qual a alíquota de referência do IBS em 2031?" > "$TMPDIR/regressao/R1.txt"
claude -p "Quais produtos tinham ST do ICMS e deixaram de ter com a reforma?" > "$TMPDIR/regressao/R2.txt"
claude -p "O que muda no IR do aluguel com a reforma?" > "$TMPDIR/regressao/R3.txt"
claude -p "Como o MEI recolhe o IBS e para quem vai o dinheiro?" > "$TMPDIR/regressao/R4.txt"
claude -p "Quem fixa a alíquota do IBS de um Município?" > "$TMPDIR/regressao/R5.txt"
grep -l "transicao-fixacao-aliquotas" "$TMPDIR/regressao/R1.txt"; grep -l "ibs-cbs-fim-substituicao-tributaria" "$TMPDIR/regressao/R2.txt"; grep -l "regime-especifico-bens-imoveis" "$TMPDIR/regressao/R3.txt"; grep -l "simples-nacional-e-mei" "$TMPDIR/regressao/R4.txt"; grep -l "ibs-cbs-aliquotas" "$TMPDIR/regressao/R5.txt"
```
Expected: os 5 arquivos listados. Leia cada saída e confira a coluna "comportamento esperado". Anote o resultado da linha de base, porque ela é a referência do Step 6.

- [ ] **Step 3: Reescrever `CLAUDE.md`** (conteúdo completo)

```markdown
# Second brain tributário — Guia do projeto

Base de conhecimento do setor fiscal sobre **legislação tributária
federal**, organizada por **domínio** (assunto). Todo o conhecimento
factual vive em notas Markdown em `notas/<dominio>/`, com base nos textos
oficiais de `fontes/<dominio>/`.

## Domínios

| Domínio | Atos normativos | Notas | Fontes | Prefixo | Status |
|---|---|---|---|---|---|
| reforma | LC 214/2025 + LC 227/2026 | `notas/reforma/` | `fontes/reforma/` | — | ativo (87 notas) |
| simples-nacional | LC 123/2006 (fase A) + Res. CGSN 140/2018 (fase B) | `notas/simples-nacional/` | `fontes/simples-nacional/` | `sn-` | em implantação |

- Índice mestre: **[notas/INDEX.md](notas/INDEX.md)**. Cada domínio tem
  `INDEX.md` (notas por tema) e `_plano-notas.md` (mapa artigo → nota).
- Para incluir um domínio ou uma fonte nova, siga
  [docs/procedimento-nova-legislacao.md](docs/procedimento-nova-legislacao.md).

## Escopo

**Só atos normativos federais listados na tabela de domínios**: leis
complementares, leis e atos infralegais federais, como resoluções do
CGSN. Ficam fora: legislação estadual e municipal (convênios, protocolos,
ITBI/IPTU municipal etc.) e tributos que esses atos não tratam (ex.:
Imposto de Renda). Perguntas sobre esses temas ficam fora do escopo das
notas, mesmo quando parecem relacionadas.

**Caso especial: substituição tributária (ST), domínio reforma.** A
exclusão de escopo vale especificamente para **listas de produtos/setores
sujeitos a ST definidas por convênio ou legislação estadual** (ex.:
convênios ICMS 142/2018 e correlatos), que ficam fora de escopo. Já a
**explicação conceitual de como o desenho da reforma (split payment, não
cumulatividade) torna a lógica de ST desnecessária** é matéria federal e
está coberta em `ibs-cbs-fim-substituicao-tributaria.md`. Quando uma
pergunta misturar as duas partes, responda a parte conceitual com base nas
notas e sinalize só a parte da lista de produtos/setores como fora de
escopo, sem recusar a pergunta inteira.

**Domínio em implantação.** Responda só com as notas já escritas. O que
faltar é lacuna (regra 3): ofereça consultar o texto extraído em
`fontes/<dominio>/texto/` ou o PDF.

## Regras de resposta (protocolo)

0. **Identifique o domínio** (ou domínios) da pergunta e comece pelo
   `INDEX.md` desse domínio.
1. **Responda só com base no que está escrito nos arquivos deste projeto**
   (`notas/`, `fontes/`, `MEMORY.md`, `LEARNINGS.md`, `decisions.md`).
   Não complete lacunas com conhecimento geral: a lei tem detalhes e
   exceções específicas que não podem ser "chutados".
2. **Sempre cite o arquivo-fonte** da informação usada na resposta
   (ex.: `ibs-cbs-aliquotas.md`) e o artigo do ato normativo quando a nota
   indicar.
3. **Se a informação não estiver nas notas**, diga isso explicitamente, sem
   inventar. Nesse caso, ofereça consultar o texto em
   `fontes/<dominio>/texto/` ou o PDF em `fontes/<dominio>/` e, se fizer
   sentido, proponha criar ou atualizar uma nota depois.
4. Ao explicar uma regra ou fórmula de cálculo, descreva-a por completo
   (não apenas "veja a nota X"), que é o estilo de trabalho do usuário.
5. **Critério para registrar em LEARNINGS.md**: só vale a pena registrar
   algo como aprendizado se pelo menos uma destas condições for
   verdadeira: (1) revelou uma lacuna real numa nota existente,
   (2) expôs uma interpretação que precisou ser corrigida ou (3) é um
   padrão que provavelmente vai se repetir. Não registre detalhes
   triviais de uma única sessão.
6. **Critério para registrar em decisions.md**: só registre quando a
   equipe efetivamente adotou uma posição, especialmente em pontos onde a
   lei é ambígua, ainda não regulamentada ou permite mais de uma
   interpretação válida. Não registre hipóteses discutidas, opções
   cogitadas e descartadas ou dúvidas ainda em aberto.
7. **Vigência (R-vigência).** Ao usar uma nota com
   `vigencia: com-mudanca-programada`, diga se a regra citada vale **hoje**
   ou **a partir de quando** (blocos `⏳`/`❌`). Nunca misture a redação
   vigente com a futura na mesma frase.
8. **Hierarquia (R-hierarquia).** Quando uma lei e um ato infralegal
   tratarem do mesmo ponto, cite os dois. Se houver conflito, a lei
   prevalece e o conflito é sinalizado.
9. **Cruzamento (R-cruzamento).** Pergunta que envolve dois domínios (ex.:
   Simples Nacional × IBS/CBS) usa as notas dos dois e cita ambas.

## Legendas

- **Domínio reforma:** 🔵 só LC 214/2025 · 🟡 tema presente nas duas (LC 227
  alterou dispositivo da LC 214) · 🟢 só LC 227/2026.
- **Todos os domínios:** `## ⏳ A partir de DD/MM/AAAA — redação dada pela
  <lei> (art. N)` marca redação futura; `## ❌ Revogado a partir de
  DD/MM/AAAA — <lei> (art. N)` marca revogação programada. O frontmatter
  `vigencia` e `texto-base` diz se a nota tem regra futura e de quando é o
  texto legal usado.

## Outras fontes de contexto

- **[fontes/](fontes/)**: PDFs oficiais e texto extraído (`texto/`), uma
  pasta por domínio, com `FONTE.md` registrando origem e data de captura.
- **[MEMORY.md](MEMORY.md)**: memória persistente entre conversas.
- **[LEARNINGS.md](LEARNINGS.md)**: aprendizados (armadilhas de
  interpretação, erros já corrigidos).
- **[decisions.md](decisions.md)**: decisões adotadas pela equipe.
- **[docs/perguntas-teste/](docs/perguntas-teste/)**: bateria de regressão
  por domínio.
- **`scripts/verificar.py`**: rode `python scripts/verificar.py` depois de
  criar, mover ou renomear qualquer nota. O resultado precisa ser 0 erros.

## Diretório `projetos/`

Reservado para aplicações práticas (calculadoras, simuladores etc.)
construídas a partir do conhecimento em `notas/`. Vazio até o momento.

Consulte sempre @MEMORY.md para contexto de fundo da equipe.
```

- [ ] **Step 4: Atualizar `MEMORY.md`** (substituir o bloco inteiro)

```markdown
# Contexto fixo

- Escritório de contabilidade, setor fiscal e diretoria
- Carteira concentrada em Comércio, Indústria, Transporte e Serviços.
- Second brain **multi-domínio** (desde 2026-10-06): uma pasta por assunto
  em `notas/<dominio>/`, roteada por `notas/INDEX.md`.
- Domínios ativos:
  - `reforma`: Reforma Tributária (LC 214/2025, atualizada pela LC 227/2026),
    87 notas, origem marcada 🔵 LC 214 · 🟢 LC 227 · 🟡 ambas.
  - `simples-nacional`: LC 123/2006 + Resolução CGSN 140/2018, em
    implantação (fase A: LC 123).
- Próximos candidatos a domínio: LC 87/1996 (Kandir), LC 116/2003 (ISS),
  Leis 10.637/2002 e 10.833/2003 (PIS/Cofins), ainda sem decisão.
```

- [ ] **Step 5: Criar `docs/procedimento-nova-legislacao.md`**

````markdown
# Procedimento: incluir uma nova legislação no second brain

Vale para um **domínio novo** (assunto novo) e para uma **fonte nova
dentro de um domínio existente** (ex.: Resolução CGSN 140 no domínio
simples-nacional). Rode `python scripts/verificar.py` no fim de cada etapa:
o resultado precisa ser 0 erros.

## Etapa 1: Fonte

1. Baixe o **texto compilado/consolidado** oficial (Planalto para leis;
   Sijut2 da Receita, "visão compilado", para atos da RFB/CGSN). Nunca use
   a publicação original do DOU de um ato que já foi alterado.
2. Salve em `fontes/<dominio>/<ato>-<ano>-texto-compilado.pdf`.
3. Registre a fonte em `fontes/<dominio>/FONTE.md`, uma linha por arquivo:

   | Arquivo | Ato | Origem (URL) | Capturado em | Última alteração vista no texto | Observação |
   |---|---|---|---|---|---|

   A "última alteração vista" é a lei/ato alterador mais recente que
   aparece nas marcas do texto (ex.: `grep -o "Complementar nº [0-9]*, de 20[0-9]*" texto.txt | sort -u`).

## Etapa 2: Extração

```bash
mkdir -p fontes/<dominio>/texto
pdftotext -enc UTF-8 fontes/<dominio>/<arquivo>.pdf fontes/<dominio>/texto/<ato>.txt
python scripts/esqueleto.py fontes/<dominio>/texto/<ato>.txt \
  --ruido "<regex do título repetido no cabeçalho, ex.: ^Lcp 123$>" \
  --saida fontes/<dominio>/texto/<ato>-esqueleto.md
```

- Se o `.txt` sair vazio ou só com lixo, o PDF não tem camada de texto:
  use OCR, ou capture o HTML oficial (Planalto) e salve como `.txt`.
- **Confira:** o "Último artigo" do esqueleto é o último artigo da lei, e
  nenhum número de artigo some da sequência.

### Armadilhas conhecidas do texto compilado do Planalto

- **Redação superada aparece junto da nova.** No site ela vem riscada; na
  extração o risco some. A **última** versão de um dispositivo, a que tem a
  marca, é a mais nova. O esqueleto mostra quantas versões cada dispositivo
  tem.
- **"Produção de efeitos" não traz data.** É só um link. A data sai do
  artigo da lei alteradora que fez a mudança, combinado com a cláusula de
  vigência dessa lei (etapa 3).

## Etapa 3: Mapa de vigência

Crie `notas/<dominio>/_mapa-vigencia.md`, com uma linha por dispositivo
marcado no esqueleto que tenha data de efeitos **diferente da publicação**
ou ainda não alcançada:

| Dispositivo | Alterado por | Artigo alterador | Efeitos a partir de | Fundamento da data | Situação em <texto-base> |
|---|---|---|---|---|---|

- "Artigo alterador": o artigo da lei alteradora que contém a nova redação
  (ex.: LC 214, art. 516).
- "Fundamento da data": o dispositivo de vigência (ex.: LC 214, art. 544, I),
  citado literalmente, a partir do texto da lei alteradora.
- "Situação": `vigente` ou `⏳ futura — redação anterior ainda vale`.
- Se uma nota existente (de outro domínio) disser algo diferente do texto
  literal, o texto literal prevalece, e a divergência é registrada em
  LEARNINGS.md.

## Etapa 4: Plano de notas (exige aprovação)

Crie `notas/<dominio>/_plano-notas.md` com frontmatter
`status: aguardando-aprovacao` e uma tabela por grupo temático:

| Arquivo | Artigos | Profundidade | Vigência |
|---|---|---|---|

- Prefixo do domínio em todo arquivo novo; nome único no projeto.
- Todo artigo do esqueleto aparece em alguma linha.
- Referências a notas de **outro** domínio vão como `[[nome]]` (nunca `nome.md`).
- **Pare e peça aprovação ao usuário.** Aprovado, mude para
  `status: aprovado`.

## Etapa 5: Redação

- Frontmatter: `título`, `dominio`, `fontes`, `vigencia`, `texto-base`.
- Conteúdo didático (lógica e analogias), artigos citados, fórmulas por
  completo, tabelas numéricas transcritas literalmente e conferidas duas
  vezes contra o PDF.
- Redação futura em `## ⏳ A partir de ...`; revogação programada em
  `## ❌ Revogado a partir de ...`.
- Ao terminar todas as notas: `status: concluido` no plano. O verificar
  passa a exigir que todas existam.

## Etapa 6: Ligações

- `notas/<dominio>/INDEX.md` com as notas por tema.
- Bloco do domínio em `notas/INDEX.md`.
- `[[...]]` cruzados com as notas de outros domínios que tratam do mesmo
  assunto, nos dois sentidos.

## Etapa 7: Protocolo e testes

- Linha do domínio na tabela "Domínios" do CLAUDE.md e bloco no MEMORY.md.
- `docs/perguntas-teste/<dominio>.md` com 10 a 15 perguntas (cálculo,
  vigência, cruzamento, lacuna, fora de escopo), rodadas com `claude -p`.
- Rodar também a bateria dos domínios já existentes (regressão).

## Atualização de uma fonte já registrada

Texto compilado mudou: refaça as etapas 1 a 3, compare o mapa de vigência
novo com o anterior (`git diff`), revise só as notas afetadas e atualize o
`texto-base` delas.
````

- [ ] **Step 6: Verificar e rodar a regressão de novo**

Run: `python scripts/verificar.py`
Expected: `0 erro(s), 0 aviso(s)`

Rode de novo os 5 comandos `claude -p` e os `grep -l` do Step 2.
Expected: os 5 arquivos listados, com o mesmo comportamento da linha de base. Se alguma resposta piorar (inventar valor, perder a citação, recusar a pergunta inteira), ajuste o CLAUDE.md e repita o teste.

- [ ] **Step 7: Commit e push**

```bash
git add CLAUDE.md MEMORY.md docs/procedimento-nova-legislacao.md docs/perguntas-teste/reforma.md
git commit -m "docs: protocolo multi-domínio, procedimento de nova legislação e regressão

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push
```

---

### Task 5: `esqueleto.py`: artigos e marcas de alteração

**Files:**
- Create: `scripts/esqueleto.py`
- Test: `scripts/tests/test_esqueleto.py`

**Interfaces:**
- Produces:
  - `RUIDO_PADRAO: list[str]` (regex de cabeçalho/rodapé de impressão)
  - `paragrafos(texto: str, ruido: list[str]) -> list[str]` (junta as linhas de cada parágrafo, separados por linha em branco, e descarta as linhas de ruído)
  - `@dataclass Registro(artigo: str, dispositivo: str, tipos: list[str], lei: str, versoes: int)`. `artigo` vem como `"18-A"` ou `"Anexo I"`; `dispositivo` como `"caput"`, `"§1º"`, `"§4º-A"`, `"V-"`, `"a)"`, `"Parágrafounico"` ou `"cabecalho"`; `tipos` é um subconjunto ordenado de `["redacao","inclusao","revogacao","vide","vigencia","efeitos-sem-data"]`; `lei` vem como `"LC 214/2025"` ou `""`; `versoes` é a posição desta redação entre as redações consecutivas do mesmo dispositivo (1 = única ou primeira).
  - `analisar(blocos: list[str]) -> tuple[list[str], list[Registro]]` (artigos únicos na ordem + registros de blocos que têm marca)
  - `gerar_markdown(nome: str, artigos: list[str], registros: list[Registro]) -> str`
  - `main(argv: list[str]) -> int` (CLI: `texto`, `--ruido REGEX` repetível, `--saida CAMINHO`)

- [ ] **Step 1: Escrever os testes que falham**

`scripts/tests/test_esqueleto.py`:

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import esqueleto as e  # noqa: E402

AMOSTRA = """06/10/2026, 14:50

Lcp 123

Art. 1º Esta Lei Complementar estabelece normas gerais.

Art. 3º Para os efeitos desta Lei Complementar, consideram-se microempresas:

§ 1º Considera-se receita bruta o produto da venda.

§ 1º Considera-se receita bruta o produto da venda e as demais receitas. (Redação dada pela Lei Complementar nº 214, de 2025) Produção de efeitos

2/44

https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm

V - cujo sócio seja administrador;

V - cujo sócio de fato seja administrador; (Redação dada pela Lei Complementar nº 214, de
2025) Produção de efeitos

CAPÍTULO IV

Art. 18-A. O Microempreendedor Individual poderá optar. (Incluído pela Lei Complementar nº 128, de 2008)

ANEXO I DA LEI COMPLEMENTAR No 123

ANEXO I DA LEI COMPLEMENTAR No 123 (Redação dada pela Lei Complementar nº 155, de 2016) Produção de efeito
"""


class TestEsqueleto(unittest.TestCase):
    def setUp(self):
        self.blocos = e.paragrafos(AMOSTRA, e.RUIDO_PADRAO + [r"^Lcp 123$"])
        self.artigos, self.registros = e.analisar(self.blocos)
        self.por_chave = {(r.artigo, r.dispositivo): r for r in self.registros}

    def test_remove_ruido_de_impressao(self):
        texto = "\n".join(self.blocos)
        self.assertNotIn("06/10/2026, 14:50", texto)
        self.assertNotIn("2/44", texto)
        self.assertNotIn("planalto.gov.br", texto)
        self.assertNotIn("Lcp 123", texto)

    def test_junta_linhas_quebradas_do_mesmo_paragrafo(self):
        self.assertIn(
            "V - cujo sócio de fato seja administrador; (Redação dada pela "
            "Lei Complementar nº 214, de 2025) Produção de efeitos",
            self.blocos,
        )

    def test_lista_artigos_unicos_em_ordem(self):
        self.assertEqual(self.artigos, ["1", "3", "18-A"])

    def test_detecta_redacao_anterior_e_nova_do_mesmo_dispositivo(self):
        self.assertEqual(self.por_chave[("3", "§1º")].versoes, 2)
        self.assertEqual(self.por_chave[("3", "V-")].versoes, 2)

    def test_marca_producao_de_efeitos_sem_data(self):
        r = self.por_chave[("3", "§1º")]
        self.assertEqual(r.tipos, ["redacao", "efeitos-sem-data"])
        self.assertEqual(r.lei, "LC 214/2025")

    def test_inclusao_sem_redacao_anterior_tem_uma_versao(self):
        r = self.por_chave[("18-A", "caput")]
        self.assertEqual(r.tipos, ["inclusao"])
        self.assertEqual(r.versoes, 1)
        self.assertEqual(r.lei, "LC 128/2008")

    def test_anexo_repetido_conta_como_segunda_versao(self):
        r = self.por_chave[("Anexo I", "cabecalho")]
        self.assertEqual(r.versoes, 2)
        self.assertEqual(r.lei, "LC 155/2016")

    def test_so_registra_blocos_com_marca(self):
        self.assertEqual(len(self.registros), 4)

    def test_gera_markdown_com_resumo_e_tabela(self):
        md = e.gerar_markdown("amostra.txt", self.artigos, self.registros)
        self.assertIn("Artigos únicos encontrados: 3", md)
        self.assertIn("Último artigo: 18-A", md)
        self.assertIn("Dispositivos com mais de uma redação no texto: 3", md)
        self.assertIn("| 3 | §1º | 2 | redacao, efeitos-sem-data | LC 214/2025 |", md)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Rodar e confirmar que falha**

Run: `python -m unittest discover -s scripts/tests -v`
Expected: ERROR em `test_esqueleto` com `ModuleNotFoundError: No module named 'esqueleto'`. Os 27 testes do verificar continuam `ok`.

- [ ] **Step 3: Implementar**

`scripts/esqueleto.py`:

```python
"""Esqueleto e marcas de alteração de um texto legal extraído com pdftotext.

Uso:
  python scripts/esqueleto.py <texto.txt> [--ruido REGEX ...] [--saida arquivo.md]

Aponta, para cada dispositivo com marca de alteração, a lei alteradora e
quantas redações consecutivas do mesmo dispositivo aparecem no texto
(no Planalto, a redação superada vem riscada e o risco some na extração).
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

RUIDO_PADRAO = [
    r"^\d{2}/\d{2}/\d{4}, \d{2}:\d{2}$",  # data/hora do cabeçalho de impressão
    r"^\d+/\d+$",                          # paginação "2/44"
    r"^https?://\S+$",                     # URL do rodapé
]

ARTIGO = re.compile(r"^Art\.\s*(\d+)(?:\s*[º°o])?(?:\s*-\s*([A-Z]))?[\s.]")
ANEXO = re.compile(r"^ANEXO\s+([IVXLC]+)\b")
DISPOSITIVO = re.compile(
    r"^(§\s*\d+\s*[º°o]?(?:\s*-\s*[A-Z])?"
    r"|Parágrafo único"
    r"|[IVXLC]+(?:\s*-\s*[A-Z])?\s+-"
    r"|[a-z]\))"
)
TITULO = re.compile(r"^(LIVRO|TÍTULO|CAPÍTULO|Seção|Subseção)\b")
LEI = re.compile(r"Lei Complementar n[º°o]\s*(\d+),\s*de\s*(\d{4})")
TIPOS = [
    ("redacao", re.compile(r"\(Redação dada pel[ao]")),
    ("inclusao", re.compile(r"\(Incluíd[oa] pel[ao]")),
    ("revogacao", re.compile(r"\(Revogad[oa]")),
    ("vide", re.compile(r"\(Vide ")),
    ("vigencia", re.compile(r"\([Vv]igência")),
    ("efeitos-sem-data", re.compile(r"Produção de efeitos?")),
]


@dataclass
class Registro:
    artigo: str
    dispositivo: str
    tipos: list[str]
    lei: str
    versoes: int


def paragrafos(texto: str, ruido: list[str]) -> list[str]:
    padroes = [re.compile(p) for p in ruido]
    blocos: list[str] = []
    atual: list[str] = []
    for linha in texto.splitlines():
        limpa = linha.strip()
        if limpa and any(p.match(limpa) for p in padroes):
            continue
        if not limpa:
            if atual:
                blocos.append(" ".join(atual))
                atual = []
            continue
        atual.append(limpa)
    if atual:
        blocos.append(" ".join(atual))
    return blocos


def _classificar(bloco: str) -> list[str]:
    return [nome for nome, padrao in TIPOS if padrao.search(bloco)]


def _lei_alteradora(bloco: str) -> str:
    achados = LEI.findall(bloco)
    if not achados:
        return ""
    numero, ano = achados[-1]
    return f"LC {numero}/{ano}"


def analisar(blocos: list[str]) -> tuple[list[str], list[Registro]]:
    artigos: list[str] = []
    registros: list[Registro] = []
    artigo, rotulo = "", ""
    chave_anterior: tuple[str, str] | None = None
    versoes = 0
    vistos_anexo: dict[str, int] = {}

    for bloco in blocos:
        m_anexo = ANEXO.match(bloco)
        m_art = None if m_anexo else ARTIGO.match(bloco)
        m_disp = None if (m_anexo or m_art) else DISPOSITIVO.match(bloco)

        if m_anexo:
            artigo, rotulo = f"Anexo {m_anexo.group(1)}", "cabecalho"
            vistos_anexo[artigo] = vistos_anexo.get(artigo, 0) + 1
            versoes = vistos_anexo[artigo]
            chave_anterior = (artigo, rotulo)
        elif m_art:
            artigo = m_art.group(1) + (f"-{m_art.group(2)}" if m_art.group(2) else "")
            if artigo not in artigos:
                artigos.append(artigo)
            rotulo = "caput"
        elif m_disp:
            rotulo = re.sub(r"\s+", "", m_disp.group(1))
        else:
            if TITULO.match(bloco):
                chave_anterior, versoes = None, 0
                continue
            # continuação de parágrafo quebrado na troca de página
            tipos = _classificar(bloco)
            if tipos and rotulo:
                registros.append(Registro(artigo, rotulo, tipos, _lei_alteradora(bloco), versoes))
            continue

        if not m_anexo:
            chave = (artigo, rotulo)
            versoes = versoes + 1 if chave == chave_anterior else 1
            chave_anterior = chave

        tipos = _classificar(bloco)
        if tipos:
            registros.append(Registro(artigo, rotulo, tipos, _lei_alteradora(bloco), versoes))

    return artigos, registros


def gerar_markdown(nome: str, artigos: list[str], registros: list[Registro]) -> str:
    multiplas = {(r.artigo, r.dispositivo) for r in registros if r.versoes > 1}
    sem_data = sum(1 for r in registros if "efeitos-sem-data" in r.tipos)
    linhas = [
        f"# Esqueleto — {nome}",
        "",
        "> Gerado por `scripts/esqueleto.py`. Apoio à conferência: não substitui o texto.",
        "",
        f"- Artigos únicos encontrados: {len(artigos)}",
        f"- Primeiro artigo: {artigos[0] if artigos else '—'} · Último artigo: {artigos[-1] if artigos else '—'}",
        f"- Dispositivos com mais de uma redação no texto: {len(multiplas)}",
        f"- Marcas \"Produção de efeitos\" sem data: {sem_data} "
        "(resolver pela lei alteradora — procedimento, etapa 3)",
        "",
        "## Artigos (na ordem)",
        "",
        ", ".join(artigos),
        "",
        "## Marcas de alteração",
        "",
        "| Artigo | Dispositivo | Versão nº | Tipos | Lei |",
        "|---|---|---|---|---|",
    ]
    for r in registros:
        linhas.append(f"| {r.artigo} | {r.dispositivo} | {r.versoes} | {', '.join(r.tipos)} | {r.lei} |")
    return "\n".join(linhas) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("texto", type=Path)
    parser.add_argument("--ruido", action="append", default=[], help="regex de linha a descartar")
    parser.add_argument("--saida", type=Path)
    args = parser.parse_args(argv[1:])

    blocos = paragrafos(args.texto.read_text(encoding="utf-8"), RUIDO_PADRAO + args.ruido)
    artigos, registros = analisar(blocos)
    md = gerar_markdown(args.texto.name, artigos, registros)
    if args.saida:
        args.saida.write_text(md, encoding="utf-8")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(md, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Rodar e confirmar que passa**

Run: `python -m unittest discover -s scripts/tests -v`
Expected: 36 testes (27 + 9), todos `ok`

- [ ] **Step 5: Commit**

```bash
git add scripts/esqueleto.py scripts/tests/test_esqueleto.py
git commit -m "feat: esqueleto.py extrai artigos e marcas de alteração de texto legal

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Simples Nacional, etapas 1 e 2 (fonte, extração, esqueleto): LC 123 + Res. CGSN 190 e 191

**Files:**
- Create: `fontes/simples-nacional/FONTE.md`
- Create: `fontes/simples-nacional/texto/lc-123-2006.txt`
- Create: `fontes/simples-nacional/texto/lc-123-2006-esqueleto.md`
- Create: `fontes/simples-nacional/texto/resolucao-cgsn-190-2026.txt`, `fontes/simples-nacional/texto/resolucao-cgsn-191-2026.txt`

**Interfaces:**
- Consumes: `scripts/esqueleto.py` (Task 5).
- Produces: texto pesquisável e esqueleto, usados nas Tasks 7 e 8.

- [ ] **Step 1: Extrair o texto**

```bash
mkdir -p fontes/simples-nacional/texto
pdftotext -enc UTF-8 fontes/simples-nacional/lc-123-2006-texto-compilado.pdf fontes/simples-nacional/texto/lc-123-2006.txt
head -c 600 fontes/simples-nacional/texto/lc-123-2006.txt
```
Expected: o texto começa com o cabeçalho de impressão e "LEI COMPLEMENTAR Nº 123, DE 14 DE DEZEMBRO DE 2006", com acentos legíveis (UTF-8).

- [ ] **Step 2: Gerar o esqueleto**

```bash
python scripts/esqueleto.py fontes/simples-nacional/texto/lc-123-2006.txt --ruido "^Lcp 123$" --saida fontes/simples-nacional/texto/lc-123-2006-esqueleto.md
head -12 fontes/simples-nacional/texto/lc-123-2006-esqueleto.md
```
Expected: "Primeiro artigo: 1 · Último artigo: 89". O número de "Marcas Produção de efeitos sem data" tem que ser maior que zero.

- [ ] **Step 3: Conferir a sequência de artigos**

```bash
python - <<'EOF'
import re
md = open("fontes/simples-nacional/texto/lc-123-2006-esqueleto.md", encoding="utf-8").read()
artigos = md.split("## Artigos (na ordem)\n\n")[1].split("\n")[0].split(", ")
numeros = sorted({int(re.match(r"\d+", a).group()) for a in artigos})
faltando = [n for n in range(1, 90) if n not in numeros]
print("faltando:", faltando)
EOF
```
Expected: `faltando: []`. Se faltar algum número, procure-o no `.txt` (`grep -n "^Art. N" ...`). Normalmente a causa é um formato de cabeçalho que o regex `ARTIGO` não pega: nesse caso, acrescente um caso de teste com a linha real em `test_esqueleto.py`, ajuste o regex, rode os testes e gere o esqueleto de novo.

- [ ] **Step 4: Conferência por amostragem das versões** (Review Focus 1)

Abra a página do Planalto (`https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm`) e confira 3 dispositivos do esqueleto com `Versão nº` 2: art. 3º §1º, art. 3º §4º inciso V e o cabeçalho do Anexo I. Em cada um, a redação **anterior** precisa aparecer riscada no site.
Expected: os 3 conferem. Se algum não conferir, registre no próprio esqueleto, numa seção `## Divergências conferidas`, antes do commit.

- [ ] **Step 5: Criar `fontes/simples-nacional/FONTE.md`**

```markdown
# Fontes — domínio simples-nacional

| Arquivo | Ato | Origem (URL) | Capturado em | Última alteração vista no texto | Observação |
|---|---|---|---|---|---|
| lc-123-2006-texto-compilado.pdf | LC 123/2006 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm | 2026-10-06 | LC 227/2026 | Impressão do navegador. A redação superada perde o risco na extração; "Produção de efeitos" não traz data (ver `notas/simples-nacional/_mapa-vigencia.md`). |
| resolucao-cgsn-140-2018-dou-original.pdf | Res. CGSN 140/2018 | https://www.in.gov.br/web/dou/-/resolucao-n-140-de-22-de-maio-de-2018-15742358 | 2026-10-06 | nenhuma (publicação original do DOU) | **NÃO USAR para notas.** Substituir pela versão compilada do Sijut2 (normas.receita.fazenda.gov.br, "visão compilado") antes da fase B. |
| resolucao-cgsn-190-2026-dou.pdf | Res. CGSN 190/2026 (altera a Res. 140: IBS/CBS no Simples, Anexos I–V para 2027–2028, Anexo XIII com valores fixos do MEI 2027–2028) | https://www.in.gov.br/web/dou/-/resolucao-cgsn-n-190-de-4-de-agosto-de-2026-724454118 | 2026-10-06 | — (ato alterador; DOU de 10/08/2026, ed. 149-A extra) | Efeitos a partir de 01/01/2027 (art. 9º). A impressão do DOU **repete os arts. 1º a 6º duas vezes**: use só a primeira ocorrência. |
| resolucao-cgsn-191-2026-dou.pdf | Res. CGSN 191/2026 (altera a Res. 140: NFS-e de padrão nacional obrigatória para ME/EPP, arts. 59 e 79; revoga a Res. 189/2026) | https://www.in.gov.br/en/web/dou/-/resolucao-cgsn-n-191-de-4-de-agosto-de-2026-724399487 | 2026-10-06 | — (ato alterador; DOU de 10/08/2026, ed. 149-A extra) | Efeitos: art. 1º a partir de 01/11/2026; demais artigos, imediatamente (art. 3º). |

## Texto extraído

- `texto/lc-123-2006.txt`: `pdftotext -enc UTF-8`, sem `-layout`.
- `texto/lc-123-2006-esqueleto.md`: `scripts/esqueleto.py --ruido "^Lcp 123$"`.
- `texto/resolucao-cgsn-190-2026.txt`, `texto/resolucao-cgsn-191-2026.txt`: `pdftotext -enc UTF-8`. São atos alteradores da Res. 140: não têm esqueleto próprio; entram no mapa de vigência (Task 7) e, na fase B, nos blocos ⏳ das notas.

## Relação entre as fontes

A LC 123 é a lei; a Res. CGSN 140 a regulamenta; as Res. CGSN 190 e 191
alteram a 140. Na fase B, ao baixar a 140 compilada do Sijut2, confira
se ela já incorpora as alterações das 190 e 191 (procure "Resolução CGSN
nº 190" nas marcas). Se não incorporar, as 190/191 continuam sendo a
fonte das redações futuras.
```

Antes de salvar, confirme a coluna "Última alteração vista":
Run: `grep -o "Complementar nº [0-9]*, de 20[0-9]*" fontes/simples-nacional/texto/lc-123-2006.txt | sort -t, -k2 -u | tail -3`
Expected: a mais recente é `Complementar nº 227, de 2026`. Se aparecer outra, use-a.

- [ ] **Step 6: Extrair as Res. CGSN 190 e 191**

```bash
pdftotext -enc UTF-8 fontes/simples-nacional/resolucao-cgsn-190-2026-dou.pdf fontes/simples-nacional/texto/resolucao-cgsn-190-2026.txt
pdftotext -enc UTF-8 fontes/simples-nacional/resolucao-cgsn-191-2026-dou.pdf fontes/simples-nacional/texto/resolucao-cgsn-191-2026.txt
grep -n "entra em vigor" -A3 fontes/simples-nacional/texto/resolucao-cgsn-19*.txt
grep -c "^Art. 1º A Resolução CGSN nº 140" fontes/simples-nacional/texto/resolucao-cgsn-190-2026.txt
```
Expected: 190, art. 9º com efeitos a partir de 1º de janeiro de 2027; 191, art. 3º com efeitos a partir de 01/11/2026 para o art. 1º e imediatos para o resto. O `grep -c` retorna `2`, que é a duplicação da impressão registrada no FONTE.md.

- [ ] **Step 7: Verificar e fazer o commit**

Run: `python scripts/verificar.py`
Expected: `0 erro(s), 0 aviso(s)`

```bash
git add fontes/simples-nacional
git commit -m "feat(simples-nacional): fontes e texto extraído da LC 123 (com esqueleto) e Res. CGSN 190/191

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: LC 123, etapa 3 (mapa de vigência)

**Files:**
- Create: `fontes/reforma/texto/lc-214-2025.txt`
- Create: `notas/simples-nacional/_mapa-vigencia.md`
- Modify: `LEARNINGS.md` (só se houver divergência entre uma nota e o texto literal)

**Interfaces:**
- Consumes: `fontes/simples-nacional/texto/lc-123-2006-esqueleto.md` (Task 6).
- Produces: `_mapa-vigencia.md`, a fonte de verdade de "vale hoje × vale a partir de" para as notas `sn-*` da fase A2.

- [ ] **Step 1: Extrair o texto da LC 214**

```bash
mkdir -p fontes/reforma/texto
pdftotext -enc UTF-8 fontes/reforma/lc-214-2025-texto-compilado.pdf fontes/reforma/texto/lc-214-2025.txt
grep -n "^Art. 51[6-9]\|^Art. 520\|^Art. 544" fontes/reforma/texto/lc-214-2025.txt
```
Expected: linhas para os arts. 516, 517, 518, 519, 520 e 544.

- [ ] **Step 2: Montar a lista "artigo da LC 214 → dispositivos da LC 123 alterados"**

Leia no `.txt` os arts. 516 a 520. Cada um diz "A Lei Complementar nº 123 ... passa a vigorar com as seguintes alterações" e transcreve os dispositivos alterados. Anote, para cada dispositivo da LC 123, qual artigo da LC 214 o alterou.

Para a LC 227, cujo PDF não tem camada de texto: use os arts. 168, 169 e 181, IV, e a cláusula de vigência (art. 182) na página oficial `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm`. Copie o trecho literal do art. 182 para dentro do mapa.

- [ ] **Step 3: Resolver as datas**

Leia o art. 544 da LC 214 no `.txt` (texto literal, já com a redação dada pela LC 227) e associe cada um dos arts. 516 a 520 à data de efeitos. Compare com a tabela da nota `notas/reforma/lc214-revogacoes-vigencia.md`, que hoje diz: 516 em 01/01/2025; 517 e 519–534 em 01/01/2027; 518 em 01/01/2033. **Se o texto literal divergir da nota, o texto prevalece.** Nesse caso, registre a divergência em `LEARNINGS.md` com o modelo das entradas existentes (`## [2026-10-06] — ...`, "O que aconteceu", "Por que importa", "Ação").

Faça o mesmo para a LC 227 com o art. 182. A nota `lc227-alteracoes-legislacao-correlata.md` menciona efeitos a partir de 01/01/2027 para "o art. 169 da LC 214". Confira no texto literal se a referência é ao art. 169 **da própria LC 227**, que altera a LC 123. Isso decide a data das alterações da LC 227 na LC 123.

- [ ] **Step 4: Escrever `notas/simples-nacional/_mapa-vigencia.md`**

Estrutura obrigatória (as linhas da tabela são preenchidas com o que foi apurado nos Steps 2 e 3; **todo** registro do esqueleto com lei `LC 214/2025` ou `LC 227/2026` vira uma linha):

```markdown
---
título: Mapa de vigência — LC 123/2006
dominio: simples-nacional
texto-base: 2026-10-06
---

# Mapa de vigência — LC 123/2006

Como ler: o texto compilado traz, para muitos dispositivos, a redação
anterior e a nova. Esta tabela diz **qual vale hoje** (em 2026-10-06).
"Situação" = `vigente` (a redação nova já vale) ou
`⏳ futura — redação anterior ainda vale` (até a data indicada).

## Cláusulas de vigência usadas (texto literal)

- LC 214/2025, art. 544: "<trecho literal dos incisos usados>"
- LC 227/2026, art. 182: "<trecho literal dos incisos usados>"

## Dispositivos alterados pela LC 214/2025 e pela LC 227/2026

| Dispositivo da LC 123 | Alterado por | Artigo alterador | Efeitos a partir de | Fundamento da data | Situação em 2026-10-06 |
|---|---|---|---|---|---|
| art. 3º, §1º | LC 214/2025 | art. 516 | DD/MM/AAAA | LC 214, art. 544, <inciso> | vigente / ⏳ futura |

## Atos do CGSN já recebidos (alteram a Res. CGSN 140, detalhados na fase B)

| Ato | O que altera na Res. 140 | Efeitos a partir de | Fundamento | Situação em 2026-10-06 |
|---|---|---|---|---|
| Res. CGSN 190/2026 | arts. <lista dos arts. com "(NR)">; Subseções/Seções inseridas (arts. 2º a 5º); Anexos I–V (vigência 2027–2028); Anexo XIII (MEI); revogações do art. 8º | 01/01/2027 | Res. 190, art. 9º | ⏳ futura |
| Res. CGSN 191/2026 | art. 59 §§1º a 1º-E (NFS-e de padrão nacional) e art. 79; revoga a Res. CGSN 189/2026 | 01/11/2026 (art. 1º); imediato (arts. 2º e 3º) | Res. 191, art. 3º | ⏳ futura (art. 1º) / vigente (revogação da 189) |

A lista de artigos da Res. 190 sai de:
`grep -o '"Art\. *[0-9]*[-A-Z]*' fontes/simples-nacional/texto/resolucao-cgsn-190-2026.txt | sort -u`
(considerar só a primeira ocorrência do bloco duplicado).

## Revogações programadas

| Dispositivo da LC 123 | Revogado por | Efeitos a partir de | Fundamento |
|---|---|---|---|
| art. 18, §4º, VI | LC 227/2026, art. 181, IV | 01/01/2033 | <dispositivo literal> |
| art. 31, §4º | LC 227/2026, art. 181, IV | 30/11/2026 | <dispositivo literal> |
```

Os `<...>` desse modelo marcam onde vai a citação literal apurada nos Steps 2 e 3. **Nenhum `<...>` nem `DD/MM/AAAA` pode sobrar no arquivo final.**

- [ ] **Step 5: Conferir a completude**

```bash
grep -c "| LC 214/2025 |\|| LC 227/2026 |" fontes/simples-nacional/texto/lc-123-2006-esqueleto.md
grep -c "^| art\.\|^| Anexo" notas/simples-nacional/_mapa-vigencia.md
grep -n "<\|DD/MM" notas/simples-nacional/_mapa-vigencia.md
```
Expected: o segundo número precisa ser **maior ou igual** ao primeiro. Pode ser maior quando um registro gera mais de uma linha, mas o primeiro conta registros e não dispositivos, porque a mesma marca pode vir em blocos de continuação. Em caso de dúvida, liste os dois lados e compare. O terceiro comando não pode retornar nada.

Run: `python scripts/verificar.py`
Expected: `0 erro(s), 0 aviso(s)` (arquivos `_*.md` são isentos de frontmatter e cobertura).

- [ ] **Step 6: Commit**

```bash
git add fontes/reforma/texto notas/simples-nacional/_mapa-vigencia.md LEARNINGS.md
git commit -m "feat(simples-nacional): mapa de vigência da LC 123 (alterações LC 214/227)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 8: LC 123, etapa 4 (plano de notas para aprovação)

**Files:**
- Create: `notas/simples-nacional/_plano-notas.md`
- Modify: `notas/INDEX.md` (bloco Simples Nacional)

**Interfaces:**
- Consumes: esqueleto (Task 6), mapa de vigência (Task 7), spec §4.1–4.5. As colunas "Observação" indicam quais notas `sn-*` vão receber detalhamento das Res. CGSN 190/191 na fase B (ex.: Anexos 2027–2028, valores fixos do MEI, NFS-e nacional).
- Produces: o plano que o usuário aprova; vira o insumo do plano da fase A2.

- [ ] **Step 1: Ler a estrutura da lei**

Run: `grep -n "^CAPÍTULO\|^Seção\|^TÍTULO" fontes/simples-nacional/texto/lc-123-2006.txt`
Use os capítulos e seções reais para confirmar ou ajustar as faixas de artigos da spec §4.1 (que foram estimadas).

- [ ] **Step 2: Escrever `notas/simples-nacional/_plano-notas.md`**

Formato obrigatório: frontmatter + uma tabela por nível de profundidade. Os nomes de arquivo partem do esboço da spec §4.2 e podem ser divididos ou fundidos conforme a estrutura real. Cada linha diz quais artigos a nota cobre e se ela terá bloco ⏳, consultando o `_mapa-vigencia.md`.

```markdown
---
título: Plano de notas — Simples Nacional (fase A: LC 123/2006)
status: aguardando-aprovacao
---

# Plano de notas — Simples Nacional (fase A: LC 123/2006)

Prefixo: `sn-`. Profundidade conforme spec §4.1. Vigência conforme
[_mapa-vigencia.md](_mapa-vigencia.md). Ponte com a reforma:
[[simples-nacional-e-mei]] (permanece no domínio reforma).

## Nível 1 — profundo

| Arquivo | Artigos | Vigência | Observação |
|---|---|---|---|
| sn-conceitos-definicao-me-epp.md | 1º–3º | com-mudanca-programada | §19 do art. 3º (receita consolidada) |
| ... | ... | ... | ... |

## Nível 2 — médio

| Arquivo | Artigos | Vigência | Observação |
|---|---|---|---|

## Nível 3 — resumo

| Arquivo | Artigos | Vigência | Observação |
|---|---|---|---|

## Anexos

| Arquivo | Conteúdo | Vigência |
|---|---|---|
| sn-anexos-tabelas.md (ou um por anexo) | Anexos I–V vigentes + bloco ⏳ com Anexos XVIII–XXII da LC 214 | com-mudanca-programada |

## Cobertura

Todos os artigos de 1 a 89 (incluindo os com letra, como 18-A e 87-A)
aparecem em exatamente uma linha das tabelas acima.
```

As reticências do modelo são preenchidas com **todas** as notas. A versão final não pode conter `...`.

- [ ] **Step 3: Conferir a cobertura de artigos do plano contra o esqueleto**

```bash
python - <<'EOF'
import re
esq = open("fontes/simples-nacional/texto/lc-123-2006-esqueleto.md", encoding="utf-8").read()
artigos = esq.split("## Artigos (na ordem)\n\n")[1].split("\n")[0].split(", ")
plano = open("notas/simples-nacional/_plano-notas.md", encoding="utf-8").read()
cobertos = set()
for ini, fim in re.findall(r"(\d+)º?(?:-[A-Z])?\s*[–-]\s*(\d+)", plano):
    cobertos.update(range(int(ini), int(fim) + 1))
for n in re.findall(r"\|\s*[^|]*?\b(\d+)º?(?:-[A-Z])?\s*\|", plano):
    cobertos.add(int(n))
faltando = sorted({int(re.match(r"\d+", a).group()) for a in artigos} - cobertos)
print("artigos sem nota:", faltando)
EOF
grep -n "\.\.\." notas/simples-nacional/_plano-notas.md
```
Expected: `artigos sem nota: []`, e o `grep` não retorna nada. Essa conferência é por número-base. Os artigos com letra (ex.: 18-A a 18-E) precisam ser conferidos visualmente na tabela.

- [ ] **Step 4: Atualizar o bloco Simples Nacional em `notas/INDEX.md`**

Substitua o bloco inteiro "## Simples Nacional — ..." por:

```markdown
## Simples Nacional — LC 123/2006 + Resolução CGSN 140/2018

- Status: **em implantação** (fase A — LC 123). Plano de notas aguardando
  aprovação; até lá, perguntas sobre o domínio são respondidas como
  lacuna, com consulta ao texto em `fontes/simples-nacional/texto/`.
- Plano de notas: [simples-nacional/_plano-notas.md](simples-nacional/_plano-notas.md)
- Mapa de vigência: [simples-nacional/_mapa-vigencia.md](simples-nacional/_mapa-vigencia.md)
- Ponte com a reforma: [[simples-nacional-e-mei]]
- Fontes: `fontes/simples-nacional/`
```

- [ ] **Step 5: Verificar**

Run: `python scripts/verificar.py`
Expected: `0 erro(s), N aviso(s)`, um aviso por nota planejada ("citada no _plano-notas.md mas não existe"). Isso é o esperado enquanto o status não for `concluido`.

- [ ] **Step 6: Commit e push**

```bash
git add notas/simples-nacional/_plano-notas.md notas/INDEX.md
git commit -m "feat(simples-nacional): plano de notas da LC 123 para aprovação

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push
```

- [ ] **Step 7: PARAR e pedir aprovação**

Apresente ao usuário: a lista de notas por nível, quantas têm bloco ⏳, as divergências registradas no LEARNINGS (se houver) e o link do arquivo. **Não escreva nenhuma nota `sn-*` neste plano.** Aprovado, mude o `status` para `aprovado` e escreva o plano da fase A2 (redação, INDEX do domínio, perguntas-teste do Simples), usando o skill writing-plans.
