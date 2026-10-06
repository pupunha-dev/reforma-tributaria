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
        args.saida.write_text(md, encoding="utf-8", newline="\n")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(md, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
