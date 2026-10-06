import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import verificar as v  # noqa: E402

FM_OK = (
    "---\n"
    "título: X\n"
    "dominio: simples-nacional\n"
    "fontes: LC 123/2006, art. 1º\n"
    "vigencia: atual\n"
    "texto-base: 2026-10-06\n"
    "---\n\n# X\n"
)


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def criar(self, caminho, texto=""):
        p = self.raiz / caminho
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(texto, encoding="utf-8")
        return p


class TestLinks(Base):
    def test_wikilink_valido_entre_dominios(self):
        self.criar("notas/reforma/a.md", "ver [[sn-b]]")
        self.criar("notas/simples-nacional/sn-b.md", "ver [[a]]")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_wikilink_inexistente(self):
        self.criar("notas/reforma/a.md", "ver [[nao-existe]]")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("[[nao-existe]] não encontrado", erros[0])

    def test_wikilink_com_extensao_md_e_erro(self):
        self.criar("notas/reforma/a.md", "ver [[b.md]]")
        self.criar("notas/reforma/b.md")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("use o nome sem .md", erros[0])

    def test_wikilink_com_alias_e_ancora(self):
        self.criar("notas/reforma/a.md", "[[b|texto]] e [[b#seção]]")
        self.criar("notas/reforma/b.md")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_link_markdown_relativo(self):
        self.criar("LEARNINGS.md", "[x](notas/reforma/a.md) e [y](notas/a.md)")
        self.criar("notas/reforma/a.md")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("notas/a.md", erros[0])

    def test_link_markdown_externo_e_ignorado(self):
        self.criar("notas/reforma/a.md", "[x](https://exemplo.gov.br/lei.md)")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_ignora_links_dentro_de_codigo(self):
        self.criar("notas/reforma/a.md", "`[[fantasma]]`\n```\n[x](nada.md)\n```\n")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_ignora_docs_superpowers(self):
        self.criar("docs/superpowers/specs/s.md", "[[fantasma]]")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_verifica_docs_fora_de_superpowers(self):
        self.criar("docs/procedimento-nova-legislacao.md", "[[fantasma]]")
        self.assertEqual(len(v.checar_links(self.raiz)), 1)


class TestNomesUnicos(Base):
    def test_nome_repetido_em_dominios_diferentes(self):
        self.criar("notas/reforma/aliquotas.md")
        self.criar("notas/simples-nacional/aliquotas.md")
        erros = v.checar_nomes_unicos(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("aliquotas", erros[0])

    def test_index_e_arquivos_de_trabalho_podem_repetir(self):
        for d in ("reforma", "simples-nacional"):
            self.criar(f"notas/{d}/INDEX.md")
            self.criar(f"notas/{d}/_plano-notas.md")
        self.assertEqual(v.checar_nomes_unicos(self.raiz), [])


if __name__ == "__main__":
    unittest.main()
