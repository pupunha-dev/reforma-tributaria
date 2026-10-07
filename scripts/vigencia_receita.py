"""Mapa de vigência a partir da visão multivigente do portal Normas da Receita.

Uso:
  python scripts/vigencia_receita.py <texto.txt> --data-base AAAA-MM-DD [--desde AAAA-MM-DD]
      [--ruido REGEX ...] [--cabecalho cabecalho.md] [--saida mapa.md]

O texto vem de `pdftotext -enc UTF-8` da impressão "Visão Multivigente". Cada
dispositivo é seguido das suas marcas entre colchetes, como
"[Redação dada pelo(a) Resolução CGSN nº N, de ...] date_range DD/MM/AAAA" ou
"[Vide modificação prevista para DD/MM/AAAA, nos termos do(a) ...]".
O texto futuro NÃO aparece: ele está no ato alterador.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from esqueleto import ANEXO, ARTIGO, DISPOSITIVO, TITULO, normalizar_rotulo  # noqa: E402

RUIDO_PADRAO = [
    r"^\d{2}/\d{2}/\d{4}, \d{2}:\d{2}$",
    r"^\d+/\d+$",
    r"^https?://\S+$",
    r"^(import_export\s*)+$",
    r"^file_present\b.*$",
    r"^Resol\. CGSN nº \d+-\d{4}$",
    r"^NORMAS$",
    r"^Visão Multivigente$",
]
# Marca completa: sem "[" dentro. A impressão do portal às vezes corta uma marca
# (abre "[" e não fecha); esse fragmento é descartado em blocos().
MARCA = re.compile(r"\[([^\[\]]*)\](?:\s*date_range\s*(\d{2}/\d{2}/\d{4}))?")
TIPOS = [
    ("modificacao-prevista", re.compile(r"^Vide modificação prevista para (\d{2}/\d{2}/\d{4})")),
    ("inclusao-prevista", re.compile(r"^Vide dispositivo a ser incluído em (\d{2}/\d{2}/\d{4})")),
    ("redacao", re.compile(r"^Redação dada")),
    ("inclusao", re.compile(r"^Incluíd")),
    ("revogacao", re.compile(r"^Revogad")),
    ("vide", re.compile(r"^Vide ")),
]
ATO = re.compile(r"Resolução CGSN nº (\d+), de \d+ de \w+ de (\d{4})")


@dataclass
class Marca:
    tipo: str
    ato: str
    data: str


@dataclass
class Bloco:
    artigo: str
    dispositivo: str
    texto: str
    marcas: list[Marca] = field(default_factory=list)


def _iso(br: str) -> str:
    dia, mes, ano = br.split("/")
    return f"{ano}-{mes}-{dia}"


def _br(iso: str) -> str:
    ano, mes, dia = iso.split("-")
    return f"{dia}/{mes}/{ano}"


def _marca(conteudo: str, date_range: str | None) -> Marca:
    conteudo = re.sub(r"\s+", " ", conteudo).strip()
    tipo, data = "outro", ""
    for nome, padrao in TIPOS:
        m = padrao.search(conteudo)
        if m:
            tipo = nome
            if m.groups():
                data = _iso(m.group(1))
            break
    if not data and date_range:
        data = _iso(date_range)
    a = ATO.search(conteudo)
    return Marca(tipo, f"Res. CGSN {a.group(1)}/{a.group(2)}" if a else "", data)


def blocos(texto: str, ruido: list[str]) -> list[Bloco]:
    padroes = [re.compile(p) for p in ruido]
    limpo = "\n".join(
        l.strip() for l in texto.splitlines()
        if l.strip() and not any(p.match(l.strip()) for p in padroes)
    )
    saida: list[Bloco] = []
    artigo, rotulo = "", ""
    pos = 0
    for m in list(MARCA.finditer(limpo)) + [None]:
        trecho = limpo[pos:m.start()] if m else limpo[pos:]
        for linha in trecho.splitlines():
            linha = linha.strip()
            if not linha or linha.startswith("["):
                continue  # vazia ou fragmento de marca cortada
            m_anexo, m_art = ANEXO.match(linha), ARTIGO.match(linha)
            m_disp = None if (m_anexo or m_art) else DISPOSITIVO.match(linha)
            if m_anexo:
                artigo, rotulo = f"Anexo {m_anexo.group(1).upper()}", "cabecalho"
            elif m_art:
                artigo = m_art.group(1) + (f"-{m_art.group(2)}" if m_art.group(2) else "")
                rotulo = "caput"
            elif m_disp:
                rotulo = normalizar_rotulo(m_disp.group(1))
            elif TITULO.match(linha) or not saida:
                saida.append(Bloco(artigo, "titulo", linha))
                continue
            else:
                saida[-1].texto += " " + linha
                continue
            saida.append(Bloco(artigo, rotulo, linha))
        if m is None:
            break
        if saida:
            saida[-1].marcas.append(_marca(m.group(1), m.group(2)))
        pos = m.end()
    return saida


def situacao(marca: Marca, data_base: str) -> str:
    futuro = marca.data > data_base
    if marca.tipo == "modificacao-prevista":
        return "⏳ modificação prevista — a redação atual vale até lá" if futuro else "modificação já em vigor"
    if marca.tipo == "inclusao-prevista":
        return "⏳ dispositivo novo a ser incluído" if futuro else "dispositivo já incluído"
    if marca.tipo == "revogacao":
        return "⏳ revogação futura" if futuro else "revogado"
    return "⏳ futura" if futuro else "vigente"


def gerar_markdown(nome: str, blocos_: list[Bloco], data_base: str, desde: str) -> str:
    linhas = [
        f"<!-- Tabela gerada por scripts/vigencia_receita.py a partir de {nome}. Não editar à mão. -->",
        "",
        f"## Marcas de vigência desde {_br(desde)} (e todas as futuras)",
        "",
        f"| Artigo | Dispositivo | Marca | Ato | Data | Situação em {_br(data_base)} |",
        "|---|---|---|---|---|---|",
    ]
    for b in blocos_:
        if not b.artigo or b.dispositivo == "titulo":
            continue
        for m in b.marcas:
            if m.tipo in ("vide", "outro") or not m.data:
                continue
            if m.data < desde and m.data <= data_base:
                continue
            linhas.append(f"| {b.artigo} | {b.dispositivo} | {m.tipo} | {m.ato} | {_br(m.data)} | {situacao(m, data_base)} |")
    return "\n".join(linhas) + "\n"


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("texto", type=Path)
    p.add_argument("--data-base", required=True)
    p.add_argument("--desde", default="2025-01-01")
    p.add_argument("--ruido", action="append", default=[])
    p.add_argument("--cabecalho", type=Path)
    p.add_argument("--saida", type=Path)
    a = p.parse_args(argv[1:])
    bs = blocos(a.texto.read_text(encoding="utf-8"), RUIDO_PADRAO + a.ruido)
    md = gerar_markdown(a.texto.name, bs, a.data_base, a.desde)
    if a.cabecalho:
        md = a.cabecalho.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + md
    if a.saida:
        a.saida.write_text(md, encoding="utf-8", newline="\n")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(md, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
