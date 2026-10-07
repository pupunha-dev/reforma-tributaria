import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import conferir_tags as ct  # noqa: E402

FONTE = """Grupo UB. Informações dos tributos IBS / CBS
UB12-10 Rejeição: Informado grupo gIBSCBS sem cClassTrib
campo vIBSUF e vBC. Regras alteradas: B25-80, N12-
50, 1C17-04 e 5E17-65."""


class TestIdentificadores(unittest.TestCase):
    def test_extrai_tags_em_crase_e_codigos_de_regra(self):
        nota = "Preencha `gIBSCBS` e `cClassTrib`; a regra UB12-10 rejeita."
        self.assertEqual(ct.identificadores(nota), {"gIBSCBS", "cClassTrib", "UB12-10"})

    def test_ignora_arquivos_caminhos_e_links(self):
        nota = "Ver `sn-mei.md`, `fontes/documentos-fiscais/texto/x.txt` e [[df-danfe-reforma]]."
        self.assertEqual(ct.identificadores(nota), set())

    def test_ignora_frontmatter_e_exemplo(self):
        nota = "---\nfontes: NT 2025.002-RTC v1.52\n---\n<!-- exemplo -->`vFake`<!-- /exemplo -->\n`vBC`"
        self.assertEqual(ct.identificadores(nota), {"vBC"})


class TestFaltantes(unittest.TestCase):
    def test_tudo_encontrado(self):
        self.assertEqual(ct.faltantes("`gIBSCBS`, `vBC`, UB12-10, B25-80", [FONTE]), [])

    def test_codigo_quebrado_entre_linhas_e_encontrado(self):
        self.assertEqual(ct.faltantes("regra N12-50", [FONTE]), [])

    def test_codigos_com_digito_inicial(self):
        self.assertEqual(ct.faltantes("1C17-04 e 5E17-65", [FONTE]), [])

    def test_tag_que_so_existe_como_prefixo_e_reportada(self):
        self.assertEqual(ct.faltantes("`vIBS`", [FONTE]), ["vIBS"])

    def test_codigo_inexistente_e_reportado(self):
        self.assertEqual(ct.faltantes("UB99-99", [FONTE]), ["UB99-99"])


class TestRejeicoes(unittest.TestCase):
    FONTE = "Obrig. 1161 Rejeição: Tipo de Operação incompatível\n225 Rejeição: Falha no Schema"

    def test_extrai_codigo_de_rejeicao(self):
        self.assertEqual(ct.identificadores("cai na rejeição 1161 e na Rejeição 225"),
                         {"rejeição 1161", "rejeição 225"})

    def test_rejeicao_existente_passa(self):
        self.assertEqual(ct.faltantes("rejeição 1161", [self.FONTE]), [])

    def test_numero_sem_rejeicao_na_fonte_e_reportado(self):
        self.assertEqual(ct.faltantes("rejeição 1162", [self.FONTE + "\n1162 Autorizado"]), ["rejeição 1162"])


if __name__ == "__main__":
    unittest.main()
