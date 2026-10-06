"""Mapa de vigência a partir do HTML compilado do Planalto.

Uso:
  python scripts/vigencia_planalto.py <lei.htm> --ancoras <ancoras.tsv> --data-base AAAA-MM-DD
      [--cabecalho cabecalho.md] [--saida mapa.md]

No HTML do Planalto, cada marca "Produção de efeitos"/"Vigência" é um link
para o dispositivo de vigência da lei alteradora (ex.: Lcp214.htm#art544-3),
e a redação já superada vem dentro de <strike>. O arquivo de âncoras diz a
data de efeitos de cada link:

  <âncora>[@<artigo>|<dispositivo>] <TAB> <AAAA-MM-DD> <TAB> <fundamento> [<TAB> revogacao]

A forma com "@artigo|dispositivo" vale só para aquele dispositivo e tem
prioridade sobre a âncora genérica. A 4ª coluna "revogacao" indica que o
dispositivo de vigência é uma revogação (ex.: LC 214, art. 543), mesmo
quando o texto da LC só traz "(Vide ...)".
"""
from __future__ import annotations

import argparse
import html as html_lib
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from esqueleto import ANEXO, ARTIGO, DISPOSITIVO, _classificar, _lei_alteradora, normalizar_rotulo  # noqa: E402

PARAGRAFO = re.compile(r"<p\b.*?</p>", re.S | re.I)
HREF = re.compile(r'href="([^"]+)"', re.I)
TAG = re.compile(r"<[^>]+>")


@dataclass
class Linha:
    artigo: str
    dispositivo: str
    tipos: list[str]
    lei: str
    ancoras: list[str]
    data: str
    fundamento: str
    situacao: str


def paragrafos_html(html: str) -> list[tuple[str, bool, list[str]]]:
    """(texto, riscado, links normalizados para 'Arquivo.htm#ancora')."""
    saida = []
    for p in PARAGRAFO.findall(html):
        texto = re.sub(r"\s+", " ", html_lib.unescape(TAG.sub("", p))).strip()
        links = [h.rsplit("/", 1)[-1] for h in HREF.findall(p)]
        saida.append((texto, "<strike" in p.lower(), links))
    return saida


def ler_ancoras(tsv: str) -> dict[str, tuple[str, str, str]]:
    """chave -> (data, fundamento, natureza), natureza 'alteracao' ou 'revogacao'."""
    ancoras = {}
    for linha in tsv.splitlines():
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        campos = [c.strip() for c in linha.split("\t")]
        natureza = campos[3] if len(campos) > 3 and campos[3] else "alteracao"
        ancoras[campos[0]] = (campos[1], campos[2], natureza)
    return ancoras


def _situacao(riscado: bool, tipos: list[str], data: str, data_base: str) -> str:
    if riscado:
        return "superado (riscado no Planalto)"
    if data > data_base:
        if "revogacao" in tipos:
            return "⏳ revogação futura — dispositivo ainda vale"
        if "inclusao" in tipos:
            return "⏳ futura — dispositivo ainda não vale"
        return "⏳ futura — redação anterior ainda vale"
    return "revogado" if "revogacao" in tipos else "vigente"


def mapear(
    pars: list[tuple[str, bool, list[str]]],
    ancoras: dict[str, tuple[str, str, str]],
    data_base: str,
) -> tuple[list[Linha], Counter]:
    linhas: list[Linha] = []
    nao_mapeadas: Counter = Counter()
    artigo, rotulo = "", ""
    for texto, riscado, links in pars:
        m_anexo = ANEXO.match(texto)
        m_art = None if m_anexo else ARTIGO.match(texto)
        m_disp = None if (m_anexo or m_art) else DISPOSITIVO.match(texto)
        if m_anexo:
            artigo, rotulo = f"Anexo {m_anexo.group(1)}", "cabecalho"
        elif m_art:
            artigo = m_art.group(1) + (f"-{m_art.group(2)}" if m_art.group(2) else "")
            rotulo = "caput"
        elif m_disp:
            rotulo = normalizar_rotulo(m_disp.group(1))

        mapeadas = []
        for link in links:
            especifica = f"{link}@{artigo}|{rotulo}"
            if especifica in ancoras:
                mapeadas.append((link, ancoras[especifica]))
            elif link in ancoras:
                mapeadas.append((link, ancoras[link]))
            elif "#" in link and ("efeito" in texto.lower() or "vigência" in texto.lower()):
                nao_mapeadas[link] += 1
        if not mapeadas or not artigo:
            continue

        lei = _lei_alteradora(texto)
        numero = lei.split()[1].split("/")[0] if lei else ""
        preferidas = [m for m in mapeadas if numero and m[0].startswith(f"Lcp{numero}")] or mapeadas
        _, (data, fundamento, natureza) = max(preferidas, key=lambda m: m[1][0])
        tipos = _classificar(texto)
        if natureza == "revogacao" and "revogacao" not in tipos:
            tipos.append("revogacao")
        linhas.append(Linha(
            artigo, rotulo, tipos, lei, [m[0] for m in mapeadas], data, fundamento,
            _situacao(riscado, tipos, data, data_base),
        ))
    return linhas, nao_mapeadas


def _br(data_iso: str) -> str:
    ano, mes, dia = data_iso.split("-")
    return f"{dia}/{mes}/{ano}"


def gerar_markdown(nome: str, linhas: list[Linha], nao_mapeadas: Counter, data_base: str) -> str:
    resumo = Counter(l.situacao for l in linhas)
    saida = [
        f"<!-- Tabela gerada por scripts/vigencia_planalto.py a partir de {nome}. Não editar à mão. -->",
        "",
        "## Resumo",
        "",
    ]
    saida += [f"- {situacao}: {n}" for situacao, n in sorted(resumo.items())]
    saida += [
        "",
        "## Dispositivos com marca de vigência",
        "",
        f"| Artigo | Dispositivo | Tipo | Lei | Efeitos a partir de | Fundamento | Situação em {_br(data_base)} |",
        "|---|---|---|---|---|---|---|",
    ]
    for l in linhas:
        saida.append(
            f"| {l.artigo} | {l.dispositivo} | {', '.join(l.tipos)} | {l.lei} | "
            f"{_br(l.data)} | {l.fundamento} | {l.situacao} |"
        )
    saida += [
        "",
        "## Âncoras de vigência não mapeadas",
        "",
        "Links \"Produção de efeitos\"/\"Vigência\" sem data no arquivo de âncoras "
        "(efeitos já consumados antes da reforma ou fora do escopo deste mapa):",
        "",
        ", ".join(f"{k} ({v})" for k, v in sorted(nao_mapeadas.items())) or "nenhuma",
    ]
    return "\n".join(saida) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("html", type=Path)
    parser.add_argument("--ancoras", type=Path, required=True)
    parser.add_argument("--data-base", required=True)
    parser.add_argument("--cabecalho", type=Path)
    parser.add_argument("--saida", type=Path)
    args = parser.parse_args(argv[1:])

    linhas, nao_mapeadas = mapear(
        paragrafos_html(args.html.read_text(encoding="utf-8")),
        ler_ancoras(args.ancoras.read_text(encoding="utf-8")),
        args.data_base,
    )
    md = gerar_markdown(args.html.name, linhas, nao_mapeadas, args.data_base)
    if args.cabecalho:
        md = args.cabecalho.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + md
    if args.saida:
        args.saida.write_text(md, encoding="utf-8", newline="\n")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(md, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
