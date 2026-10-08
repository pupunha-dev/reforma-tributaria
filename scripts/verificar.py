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

NOME_NOTA = re.compile(r"(?<![\w/.-])([a-z0-9][a-z0-9-]*\.md)\b")
DATA_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")

ARQUIVOS_RAIZ = ("CLAUDE.md", "MEMORY.md", "LEARNINGS.md", "decisions.md")
CAMPOS_OBRIGATORIOS = ("título", "dominio", "fontes", "vigencia", "texto-base")
VIGENCIAS_VALIDAS = ("atual", "com-mudanca-programada")
DOMINIOS_LEGADOS = ("reforma",)
VERSAO_NT = re.compile(r"NT \d{4}\.\d{3}(?:-RTC)? v\d+\.\d{1,2}\b")


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
    erros = (checar_nomes_unicos(raiz) + checar_links(raiz) + checar_frontmatter(raiz)
             + checar_versao_nt(raiz))
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
