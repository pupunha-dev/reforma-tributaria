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
