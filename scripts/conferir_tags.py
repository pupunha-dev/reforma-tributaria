"""Confere se todo identificador técnico de uma nota existe nas Notas Técnicas.

Uso: python scripts/conferir_tags.py <nota.md> --fontes <arquivo> [<arquivo> ...]
Identificadores: tags em crase (ex.: `gIBSCBS`), códigos de regra de
validação (ex.: UB12-10, 1C17-04) e códigos de rejeição escritos como
"rejeição 1161" (conferidos contra "1161 Rejeição" na NT). Ignora o frontmatter e blocos
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
REJEICAO = re.compile(r"[Rr]ejeição (\d{3,4})\b")


def identificadores(texto: str) -> set[str]:
    texto = EXEMPLO.sub("", FRONTMATTER.sub("", texto))
    rejeicoes = {f"rejeição {n}" for n in REJEICAO.findall(texto)}
    return set(TAG.findall(texto)) | set(REGRA.findall(texto)) | rejeicoes


def disponiveis(fonte: str) -> str:
    return QUEBRA.sub("-", fonte)


def _existe(ident: str, fontes: list[str]) -> bool:
    if ident.startswith("rejeição "):
        numero = ident.split()[1]
        padrao = re.compile(r"(?<!\d)" + numero + r"\s+Rejeição")
        return any(padrao.search(f) for f in fontes)
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
