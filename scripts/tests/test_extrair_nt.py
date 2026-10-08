import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import extrair_nt as en  # noqa: E402

try:
    import pymupdf
except ImportError:  # pragma: no cover
    pymupdf = None


def _pdf_de_teste(pasta: Path) -> Path:
    doc = pymupdf.open()
    pg = doc.new_page()
    pg.insert_text((72, 100), "Producao em 03/11/2026", fontsize=11)
    pg.insert_text((72, 130), "Producao em 03/08/2026", fontsize=11)
    pg.draw_line((70, 126), (240, 126), color=(1, 0, 0), width=0.8)  # risca a 2a linha
    pg.insert_text((72, 160), "Coluna A", fontsize=11)
    pg.insert_text((300, 160), "Coluna B", fontsize=11)
    pg.draw_line((60, 190), (500, 190), width=0.5)  # borda de tabela abaixo do texto
    caminho = pasta / "nt.pdf"
    doc.save(caminho)
    return caminho


@unittest.skipIf(pymupdf is None, "pymupdf não instalado")
class TestExtrairNT(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.pdf = _pdf_de_teste(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def test_vigente_exclui_texto_riscado(self):
        vigente, _ = en.extrair(self.pdf)
        self.assertIn("03/11/2026", vigente)
        self.assertNotIn("03/08/2026", vigente)

    def test_riscados_listados_com_pagina(self):
        _, riscados = en.extrair(self.pdf)
        self.assertEqual(riscados, [(1, "Producao em 03/08/2026")])

    def test_mesma_linha_em_colunas_vira_uma_linha(self):
        vigente, _ = en.extrair(self.pdf)
        self.assertIn("Coluna A | Coluna B", vigente)

    def test_borda_de_tabela_nao_risca(self):
        vigente, _ = en.extrair(self.pdf)
        self.assertIn("Coluna A", vigente)


@unittest.skipIf(pymupdf is None, "pymupdf não instalado")
class TestRiscadoParcialEAnotacao(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        doc = pymupdf.open()
        pg = doc.new_page()
        pg.insert_text((72, 100), "Data 03/08/2026 03/11/2026", fontsize=11)
        larg = pymupdf.get_text_length("Data ", fontsize=11)
        larg_data = pymupdf.get_text_length("03/08/2026", fontsize=11)
        pg.draw_line((72 + larg, 96), (72 + larg + larg_data, 96), color=(1, 0, 0), width=0.8)
        pg.insert_text((72, 160), "Regra antiga anotada", fontsize=11)
        quad = pg.search_for("Regra antiga anotada")[0]
        pg.add_strikeout_annot(quad)
        pg.insert_text((72, 200), "Regra nova", fontsize=11)
        self.pdf = Path(self._tmp.name) / "nt2.pdf"
        doc.save(self.pdf)

    def tearDown(self):
        self._tmp.cleanup()

    def test_riscado_parcial_dentro_do_mesmo_trecho(self):
        vigente, riscados = en.extrair(self.pdf)
        self.assertIn("Data 03/11/2026", vigente)
        self.assertNotIn("03/08/2026", vigente)
        self.assertIn((1, "03/08/2026"), riscados)

    def test_anotacao_strikeout_conta_como_riscado(self):
        vigente, riscados = en.extrair(self.pdf)
        self.assertNotIn("Regra antiga", vigente)
        self.assertIn("Regra nova", vigente)
        self.assertIn((1, "Regra antiga anotada"), riscados)


if __name__ == "__main__":
    unittest.main()
