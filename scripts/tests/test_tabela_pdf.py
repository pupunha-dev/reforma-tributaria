import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tabela_pdf as tp  # noqa: E402

try:
    import pymupdf
except ImportError:  # pragma: no cover
    pymupdf = None


class TestLimpar(unittest.TestCase):
    def test_quebra_de_linha_vira_espaco(self):
        self.assertEqual(tp.limpar("FABRICAÇÃO DE\nCIGARROS"), "FABRICAÇÃO DE CIGARROS")

    def test_none_continua_none(self):
        self.assertIsNone(tp.limpar(None))

    def test_espacos_repetidos(self):
        self.assertEqual(tp.limpar("  A   B "), "A B")


CAB = ["OCUPAÇÃO", "CNAE", "ISS"]


class TestConsolidar(unittest.TestCase):
    def test_titulo_de_secao_e_cabecalho(self):
        secoes = tp.consolidar([[["TABELA A", None, None], CAB, ["ALFAIATE", "1412-6/02", "S"]]])
        self.assertEqual(len(secoes), 1)
        self.assertEqual(secoes[0].titulo, "TABELA A")
        self.assertEqual(secoes[0].cabecalho, CAB)
        self.assertEqual(secoes[0].linhas, [["ALFAIATE", "1412-6/02", "S"]])

    def test_cabecalho_repetido_em_outra_pagina_e_ignorado(self):
        secoes = tp.consolidar([[CAB, ["A", "1", "S"]], [CAB, ["B", "2", "N"]]])
        self.assertEqual(secoes[0].linhas, [["A", "1", "S"], ["B", "2", "N"]])

    def test_linha_com_celula_vazia_continua_a_anterior(self):
        secoes = tp.consolidar([[CAB, ["POCEIRO/CISTERNEIRO/", "4399-1/05", "S"],
                                 ["CACIMBEIRO INDEPENDENTE", "", ""]]])
        self.assertEqual(secoes[0].linhas,
                         [["POCEIRO/CISTERNEIRO/CACIMBEIRO INDEPENDENTE", "4399-1/05", "S"]])

    def test_continuacao_na_segunda_coluna(self):
        secoes = tp.consolidar([[["Subclasse", "DENOMINAÇÃO"],
                                 ["2550-1/01", "FABRICAÇÃO DE EQUIPAMENTO BÉLICO PESADO, EXCETO VEÍCULOS"],
                                 ["", "MILITARES DE COMBATE"]]])
        self.assertEqual(secoes[0].linhas[0][1],
                         "FABRICAÇÃO DE EQUIPAMENTO BÉLICO PESADO, EXCETO VEÍCULOS MILITARES DE COMBATE")

    def test_linha_toda_vazia_e_ignorada(self):
        secoes = tp.consolidar([[CAB, ["A", "1", "S"], ["", "", ""]]])
        self.assertEqual(secoes[0].linhas, [["A", "1", "S"]])

    def test_nova_secao_reinicia_cabecalho(self):
        secoes = tp.consolidar([[["TABELA A", None, None], CAB, ["A", "1", "S"],
                                 ["TABELA B", None, None], CAB, ["B", "2", "N"]]])
        self.assertEqual([s.titulo for s in secoes], ["TABELA A", "TABELA B"])
        self.assertEqual(secoes[1].linhas, [["B", "2", "N"]])


class TestMarkdown(unittest.TestCase):
    def test_tabela_em_markdown_com_contagem(self):
        secoes = tp.consolidar([[["TABELA A", None, None], CAB, ["A | B", "1", "S"]]])
        md = tp.para_markdown(secoes, "Anexo XI", "anexo.pdf")
        self.assertIn("# Anexo XI", md)
        self.assertIn("Origem: anexo.pdf", md)
        self.assertIn("## TABELA A (1 linha(s))", md)
        self.assertIn("| OCUPAÇÃO | CNAE | ISS |", md)
        self.assertIn("| A / B | 1 | S |", md)


@unittest.skipIf(pymupdf is None, "pymupdf não instalado")
class TestExtrairPDF(unittest.TestCase):
    def test_le_tabela_desenhada(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = pymupdf.open()
            pg = doc.new_page()
            xs, ys = (72, 200, 330), (72, 92, 112)
            for x in xs:
                pg.draw_line((x, ys[0]), (x, ys[-1]))
            for y in ys:
                pg.draw_line((xs[0], y), (xs[-1], y))
            pg.insert_text((76, 86), "Subclasse", fontsize=9)
            pg.insert_text((204, 86), "DENOMINACAO", fontsize=9)
            pg.insert_text((76, 106), "1220-4/01", fontsize=9)
            pg.insert_text((204, 106), "CIGARROS", fontsize=9)
            caminho = Path(tmp) / "t.pdf"
            doc.save(caminho)
            secoes = tp.extrair(caminho)
        self.assertEqual(secoes[0].cabecalho, ["Subclasse", "DENOMINACAO"])
        self.assertEqual(secoes[0].linhas, [["1220-4/01", "CIGARROS"]])


if __name__ == "__main__":
    unittest.main()
