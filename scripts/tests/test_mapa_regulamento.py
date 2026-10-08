import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import mapa_regulamento as mr  # noqa: E402

LEI = "Lei Complementar nº 214, de 16 de janeiro de 2025"


class TestCitacoes(unittest.TestCase):
    def test_artigo_simples_formato_cbs(self):
        self.assertEqual(mr.citacoes(f"texto (Art. 3º da {LEI}) fim"), {"214": ["3"]})

    def test_artigo_simples_formato_ibs(self):
        self.assertEqual(mr.citacoes("texto (Art. 3º da LC 214/2025) fim"), {"214": ["3"]})

    def test_paragrafo_e_inciso_nao_viram_artigo(self):
        self.assertEqual(mr.citacoes("(Art. 12, § 2º, inciso III, da LC 214/2025)"), {"214": ["12"]})
        self.assertEqual(mr.citacoes("(Art. 98, §§ 1º e 2º, da LC 214/2025)"), {"214": ["98"]})

    def test_varios_artigos_e_sufixo(self):
        self.assertEqual(mr.citacoes("(Arts. 4º e 5º da LC 214/2025)"), {"214": ["4", "5"]})
        self.assertEqual(mr.citacoes(f"(Art. 98-B da {LEI})"), {"214": ["98-B"]})
        self.assertEqual(mr.citacoes(f"(Art. 26 e art. 27 da {LEI})"), {"214": ["26", "27"]})

    def test_faixa_de_artigos(self):
        self.assertEqual(mr.citacoes(f"(Art. 245 a art. 248 da {LEI})"),
                         {"214": ["245", "246", "247", "248"]})

    def test_duas_leis_na_mesma_citacao(self):
        self.assertEqual(mr.citacoes("(Art. 3º da LC 214/2025 e art. 2º da LC 227/2026)"),
                         {"214": ["3"], "227": ["2"]})

    def test_data_curta_da_lei(self):
        self.assertEqual(mr.citacoes("(Art. 34, caput, da Lei Complementar nº 214, de 2025)"), {"214": ["34"]})

    def test_artigo_de_outra_lei_no_mesmo_parentese_fica_de_fora(self):
        self.assertEqual(mr.citacoes("(Art. 10 da Lei nº 9.430, de 1996, e art. 5º da LC 214/2025)"),
                         {"214": ["5"]})

    def test_parenteses_sem_lei_sao_ignorados(self):
        self.assertEqual(mr.citacoes("valor (vinte por cento) e art. 26 deste Regulamento"), {})


TEXTO = """LIVRO I DAS NORMAS COMUNS
TÍTULO I DAS NORMAS GERAIS
Art. 1º O tributo será regido por este Regulamento.
Art. 2º Para fins deste Regulamento, consideram-se: (Art. 3º da LC 214/2025) I - operações.
CAPÍTULO II DO IBS
Art. 3º O IBS incide sobre operações (Art. 4º da LC 214/2025), observado o art. 2º. § 1º Texto (Art. 5º da LC 214/2025).
Art. 3º-A Novo artigo. (Art. 6º-A da LC 214/2025)
Art. 4º Sem citação e com referência ao Art. 2º deste Regulamento no meio.
"""


class TestArtigos(unittest.TestCase):
    def setUp(self):
        self.arts = mr.dividir_artigos(TEXTO)

    def test_um_bloco_por_artigo_em_ordem(self):
        self.assertEqual([a.numero for a in self.arts], ["1", "2", "3", "3-A", "4"])

    def test_citacoes_do_artigo_inteiro(self):
        a3 = next(a for a in self.arts if a.numero == "3")
        self.assertEqual(a3.leis, {"214": ["4", "5"]})

    def test_artigo_sem_citacao(self):
        self.assertEqual(self.arts[0].leis, {})

    def test_contexto_do_titulo_e_capitulo(self):
        a3 = next(a for a in self.arts if a.numero == "3")
        self.assertIn("CAPÍTULO II DO IBS", a3.contexto)

    def test_artigo_mencionado_no_meio_do_texto_nao_divide(self):
        self.assertIn("deste Regulamento no meio", self.arts[-1].texto)


class TestInverterEFaixas(unittest.TestCase):
    def test_inverte_lc_para_regulamento(self):
        arts = mr.dividir_artigos(TEXTO)
        inv = mr.inverter(arts, "214")
        self.assertEqual(inv["4"], ["3"])
        self.assertEqual(inv["6-A"], ["3-A"])

    def test_faixas_compactas(self):
        self.assertEqual(mr.faixas(["2", "3", "4", "7", "9", "10", "10-A"]), "2 a 4, 7, 9, 10 e 10-A")
        self.assertEqual(mr.faixas([]), "—")


PLANO = """## 1. Núcleo IBS/CBS — arts. 1–62 (16 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| ibs-cbs-conceitos-principios.md | 1–3 | 🔵 |
| regimes-aduaneiros-especiais.md | 84–98-B | 🔵 |
| contencioso-integrado-ibs-cbs.md | 323-G a 323-M | 🟢 |
| cesta-basica-nacional.md | 125 + Anexo I | 🔵 |
| lc214-alteracoes-outras-leis.md | 491–515, 521–541 | 🔵 |

## 10. CGIBS, processo e ITCMD — LC 227 arts. 1–164 (17 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| cgibs-natureza-competencias.md | 1–20 | 🟢 |
"""


class TestPlano(unittest.TestCase):
    def setUp(self):
        self.notas = {n.nota: n for n in mr.notas_do_plano(PLANO)}

    def test_le_lei_e_faixas(self):
        n = self.notas["ibs-cbs-conceitos-principios"]
        self.assertEqual(n.lei, "214")
        self.assertTrue(n.contem("2"))
        self.assertFalse(n.contem("4"))

    def test_faixa_com_sufixo(self):
        n = self.notas["regimes-aduaneiros-especiais"]
        self.assertTrue(n.contem("98-B"))
        self.assertTrue(n.contem("90"))
        self.assertFalse(n.contem("98-C"))
        c = self.notas["contencioso-integrado-ibs-cbs"]
        self.assertTrue(c.contem("323-H"))
        self.assertFalse(c.contem("323-F"))

    def test_varias_faixas_e_anexo(self):
        self.assertTrue(self.notas["lc214-alteracoes-outras-leis"].contem("530"))
        self.assertFalse(self.notas["lc214-alteracoes-outras-leis"].contem("518"))
        self.assertTrue(self.notas["cesta-basica-nacional"].contem("125"))

    def test_secao_da_lc_227(self):
        self.assertEqual(self.notas["cgibs-natureza-competencias"].lei, "227")


class TestBlocoNota(unittest.TestCase):
    def test_bloco_com_vigencia_futura(self):
        bloco = mr.bloco_nota(
            {"CBS": ["2", "245", "246"], "IBS": ["2", "517"]},
            {"CBS": {"245": "01/01/2027", "246": "01/01/2027"}, "IBS": {"517": "01/01/2029"}})
        self.assertIn("**Regulamento da CBS** (Decreto nº 12.955/2026): arts. 2, 245 e 246", bloco)
        self.assertIn("⏳ produzem efeitos a partir de 01/01/2027: arts. 245 e 246", bloco)
        self.assertIn("⏳ produz efeitos a partir de 01/01/2029: art. 517", bloco)

    def test_sem_artigos(self):
        bloco = mr.bloco_nota({"CBS": [], "IBS": []}, {"CBS": {}, "IBS": {}})
        self.assertIn("nenhum artigo cita", bloco)

    def test_aplica_bloco_em_nota_sem_marcador(self):
        texto = mr.aplicar_bloco("# Nota\n\nTexto.\n", "CONTEUDO")
        self.assertIn("## Regulamentação (Decreto 12.955/2026 e Res. CGIBS 6/2026)", texto)
        self.assertIn("<!-- gerado:regulamentos -->\nCONTEUDO\n<!-- /gerado:regulamentos -->", texto)

    def test_aplica_bloco_de_novo_so_substitui(self):
        uma = mr.aplicar_bloco("# Nota\n", "A")
        duas = mr.aplicar_bloco(uma, "B")
        self.assertEqual(duas.count("## Regulamentação"), 1)
        self.assertIn("\nB\n", duas)

    def test_bloco_entra_antes_de_ligacoes(self):
        texto = mr.aplicar_bloco("# Nota\n\nTexto.\n\n## Ligações\n\n- [[x]]\n", "C")
        self.assertLess(texto.index("## Regulamentação"), texto.index("## Ligações"))


if __name__ == "__main__":
    unittest.main()
