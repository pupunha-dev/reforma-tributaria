"""Extrai as tabelas de um PDF (anexos de resoluções) para Markdown.

Uso: python scripts/tabela_pdf.py <arquivo.pdf> --titulo "<título>" --saida <arquivo.md>
Requer pymupdf (pip install pymupdf). Usa a detecção de tabelas do pymupdf, que
lê as bordas das células, e consolida as páginas:
- linha só com a 1ª célula preenchida (as demais vazias de verdade) é título de
  seção (ex.: "TABELA A") e a linha seguinte é o cabeçalho;
- cabeçalho repetido em outra página é ignorado;
- linha com alguma célula vazia continua a linha anterior (texto que quebrou
  de página ou de linha dentro da célula). O total dessas junções é impresso
  para conferência manual.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Secao:
    titulo: str | None
    cabecalho: list[str] | None = None
    linhas: list[list[str]] = field(default_factory=list)
    juncoes: int = 0


def limpar(celula: str | None) -> str | None:
    if celula is None:
        return None
    return " ".join(celula.split())


def _juntar(antes: str, depois: str) -> str:
    if not antes:
        return depois
    if not depois:
        return antes
    return antes + depois if antes.endswith(("/", "-")) else f"{antes} {depois}"


def _e_titulo(linha: list[str | None]) -> bool:
    return bool(linha[0]) and len(linha) > 1 and all(c is None for c in linha[1:])


def consolidar(tabelas: list[list[list[str | None]]]) -> list[Secao]:
    secoes: list[Secao] = []
    atual: Secao | None = None
    for tabela in tabelas:
        for bruta in tabela:
            linha = [limpar(c) for c in bruta]
            if _e_titulo(linha):
                atual = Secao(titulo=linha[0])
                secoes.append(atual)
                continue
            if all(not c for c in linha):
                continue
            if atual is None:
                atual = Secao(titulo=None)
                secoes.append(atual)
            textos = [c or "" for c in linha]
            if atual.cabecalho is None:
                atual.cabecalho = textos
            elif textos == atual.cabecalho:
                continue
            elif "" in textos and atual.linhas:
                anterior = atual.linhas[-1]
                atual.linhas[-1] = [_juntar(a, d) for a, d in zip(anterior, textos)]
                atual.juncoes += 1
            else:
                atual.linhas.append(textos)
    return secoes


def _celula(texto: str) -> str:
    return texto.replace("|", "/")


def para_markdown(secoes: list[Secao], titulo: str, origem: str) -> str:
    partes = [f"# {titulo}", "", f"Origem: {origem}",
              "Gerado por `scripts/tabela_pdf.py` (detecção de tabelas do pymupdf).", ""]
    for s in secoes:
        nome = s.titulo or "Tabela"
        partes += [f"## {nome} ({len(s.linhas)} linha(s))", ""]
        cab = s.cabecalho or []
        partes.append("| " + " | ".join(_celula(c) for c in cab) + " |")
        partes.append("|" + "---|" * len(cab))
        partes += ["| " + " | ".join(_celula(c) for c in linha) + " |" for linha in s.linhas]
        partes.append("")
    return "\n".join(partes)


def extrair(pdf: Path) -> list[Secao]:
    import pymupdf

    doc = pymupdf.open(pdf)
    tabelas = [t.extract() for pagina in doc for t in pagina.find_tables().tables]
    return consolidar(tabelas)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--titulo", required=True)
    parser.add_argument("--saida", type=Path, required=True)
    args = parser.parse_args(argv[1:])
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    secoes = extrair(args.pdf)
    args.saida.write_text(para_markdown(secoes, args.titulo, args.pdf.name), encoding="utf-8")
    for s in secoes:
        print(f"{s.titulo or 'Tabela'}: {len(s.linhas)} linha(s), {s.juncoes} junção(ões)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
