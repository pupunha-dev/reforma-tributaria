import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import xlsx_para_tsv as m  # noqa: E402


class TestXlsxParaTsv(unittest.TestCase):
    def test_normalizar(self):
        self.assertEqual(m.normalizar("MUN.INCID_INFO.SERV."), "mun-incid-info-serv")
        self.assertEqual(m.normalizar("EXPORTAÇÃO_EMISSÃO_NFS-e"), "exportacao-emissao-nfs-e")

    def test_celula(self):
        self.assertEqual(m.celula(None), "")
        self.assertEqual(m.celula("a\nb"), "a ⏎ b")
        self.assertEqual(m.celula(3), "3")

    def test_converter(self):
        import openpyxl
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Aba Um"
            ws.append(["x", "y\nz"])
            ws.append([None, None])
            ws.append(["fim", None, 7])
            p = d / "t.xlsx"
            wb.save(p)
            feitos = m.converter(p, "pre", d / "out")
            self.assertEqual(feitos[0][1], 2)
            linhas = (d / "out" / "pre-aba-um.tsv").read_text(encoding="utf-8").splitlines()
            self.assertEqual(linhas, ["L1\tx\ty ⏎ z", "L3\tfim\t\t7"])


if __name__ == "__main__":
    unittest.main()
