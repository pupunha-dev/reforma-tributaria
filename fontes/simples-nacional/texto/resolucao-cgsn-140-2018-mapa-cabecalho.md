---
título: Mapa de vigência — Resolução CGSN 140/2018
dominio: simples-nacional
texto-base: 2026-10-07
---

# Mapa de vigência — Resolução CGSN 140/2018

> Arquivo gerado. Não edite à mão: o cabeçalho vem de
> `fontes/simples-nacional/texto/resolucao-cgsn-140-2018-mapa-cabecalho.md` e a
> tabela de `scripts/vigencia_receita.py`. Para regerar:
>
> ```bash
> python scripts/vigencia_receita.py fontes/simples-nacional/texto/resolucao-cgsn-140-2018.txt \
>   --data-base 2026-10-07 \
>   --cabecalho fontes/simples-nacional/texto/resolucao-cgsn-140-2018-mapa-cabecalho.md \
>   --saida notas/simples-nacional/_mapa-vigencia-res140.md
> ```

## Fonte e como ler

Fonte: impressão da **visão multivigente** do portal Normas da Receita
(`resolucao-cgsn-140-2018-multivigente.pdf`, capturada em 07/10/2026), que já
incorpora as Res. CGSN 190 e 191/2026. As datas vêm das próprias marcas do
portal:

- **redacao / inclusao / revogacao** com `date_range`: data de início da
  redação, inclusão ou revogação já publicada;
- **modificacao-prevista**: "Vide modificação prevista para DD/MM/AAAA, nos
  termos do(a) ...": até essa data vale a redação atual; **o texto novo não
  aparece no portal** e deve ser lido no ato indicado (quase sempre a Res. CGSN
  190/2026, em `texto/resolucao-cgsn-190-2026.txt`, usando só a 1ª ocorrência
  dos arts. 1º a 6º);
- **inclusao-prevista**: "Vide dispositivo a ser incluído em DD/MM/AAAA": um
  dispositivo novo entra **depois** do dispositivo da linha, na data indicada.

A tabela mostra as marcas desde 01/01/2025, **todas** as futuras e **todas as
revogações**, de qualquer data (um dispositivo revogado em 2023 continua
revogado). Modificações previstas em **títulos de seção** (4 casos) não aparecem
na tabela.

Rótulos: o dispositivo leva o pai, como "§2º, I" (inciso I do §2º) e "§2º, I,
a)"; inciso sem § é do caput. Nos anexos, a marca é do anexo da linha (desde
2026-10-08 o script separa os títulos de anexo que a impressão junta numa linha
só).

## Cláusulas de vigência dos atos alteradores (texto literal)

- **Res. CGSN 190/2026, art. 9º:** "Esta Resolução entra em vigor na data de
  sua publicação no Diário Oficial da União e produzirá efeitos a partir de 1º
  de janeiro de 2027."
- **Res. CGSN 191/2026, art. 3º:** "Esta Resolução entra em vigor na data de
  sua publicação no Diário Oficial da União e produzirá efeitos: I - a partir
  de 01 de novembro de 2026, em relação ao art. 1º; e II - imediatamente, em
  relação aos demais artigos."

## Lacuna: Anexos da Res. 140

Os Anexos da Res. 140 são **arquivos separados** no portal e **não** vêm na
impressão. Os Anexos I a V de 2027–2028 constam da Res. CGSN 190 (DOU). Os
Anexos **VI** (CNAEs impeditivos; redação da Res. CGSN 143/2018, desde
01/01/2019) e **XI** (ocupações do MEI; redação da Res. CGSN 182/2025, desde
01/10/2025) entraram nas fontes em 2026-10-08 (ver `FONTE.md`). Os demais, entre
eles o **VII** (CNAEs que abrangem atividades permitidas e impeditivas), o **X**
(relatório mensal do MEI) e o **XII**, **não estão nas fontes**.
