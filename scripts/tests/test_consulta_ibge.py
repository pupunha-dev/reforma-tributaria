import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import consulta_ibge as ci  # noqa: E402


class TestConsultaIbge(unittest.TestCase):
    def test_norm_remove_acento_e_caixa(self):
        self.assertEqual(ci.norm("Belém"), "belem")

    def test_lapa_pr(self):
        achou = [r for r in ci.ler("ibge-dtb-municipios.tsv") if r["cod_municipio"] == "4113205"]
        self.assertEqual(len(achou), 1)
        self.assertEqual((achou[0]["municipio"], achou[0]["uf_sigla"]), ("Lapa", "PR"))

    def test_totais_da_dtb(self):
        self.assertEqual(len(ci.ler("ibge-dtb-municipios.tsv")), 5570)
        self.assertEqual(len(ci.ler("ibge-dtb-distritos.tsv")), 10724)
        self.assertEqual(len(ci.ler("ibge-dtb-subdistritos.tsv")), 645)


if __name__ == "__main__":
    unittest.main()
