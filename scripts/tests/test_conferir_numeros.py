import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import conferir_numeros as cn  # noqa: E402

FONTE = "| 1ª Faixa | Até 180.000,00 | 4,00% | - | fator r igual ou superior a 28% (vinte e oito por cento)"


class TestConferirNumeros(unittest.TestCase):
    def test_extrai_percentuais_e_valores(self):
        self.assertEqual(cn.numeros("alíquota de 4,00% até R$ 180.000,00 e 28%"), {"4,00%", "180.000,00", "28%"})

    def test_tudo_encontrado(self):
        self.assertEqual(cn.faltantes("Faixa 1: até R$ 180.000,00, alíquota 4,00%; Fator R 28%.", [FONTE]), [])

    def test_percentual_inexistente_na_fonte_e_reportado(self):
        self.assertEqual(cn.faltantes("alíquota 4,10%", [FONTE]), ["4,10%"])

    def test_ignora_numeros_dentro_de_exemplo(self):
        nota = "<!-- exemplo -->\nRBT12 = R$ 1.000.000,00, alíquota efetiva 8,77%\n<!-- /exemplo -->\nalíquota 4,00%"
        self.assertEqual(cn.faltantes(nota, [FONTE]), [])

    def test_ignora_frontmatter(self):
        self.assertEqual(cn.faltantes("---\ntexto-base: 2026-10-06\n---\nalíquota 4,00%", [FONTE]), [])


if __name__ == "__main__":
    unittest.main()
