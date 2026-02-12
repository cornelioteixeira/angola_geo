
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
from angola_geo.cli import main, cmd_info, cmd_listar_provincias, cmd_obter_provincia, cmd_listar_municipios, cmd_pesquisar, cmd_provincias_novas
from angola_geo import AngolaGeo

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.geo = AngolaGeo()
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def test_info(self):
        with patch('sys.argv', ['angola-geo', 'info']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Angola Geo - Informações do Dataset", output)
            self.assertIn("Lei: Lei n.º 14/24", output)
            self.assertIn("Províncias: 21", output)

    def test_listar_provincias(self):
        with patch('sys.argv', ['angola-geo', 'listar', 'provincias']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Angola - 21 Províncias", output)
            self.assertIn("Luanda", output)
            self.assertIn("Bengo", output)

    def test_listar_provincias_detalhado(self):
        with patch('sys.argv', ['angola-geo', 'listar', 'provincias', '-d']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Lista de Municípios:", output)

    def test_obter_provincia(self):
        with patch('sys.argv', ['angola-geo', 'obter', 'provincia', 'Luanda']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Província de Luanda", output)
            self.assertIn("Capital: Ingombota", output)
            self.assertIn("Belas", output)

    def test_obter_provincia_inexistente(self):
        with patch('sys.argv', ['angola-geo', 'obter', 'provincia', 'Inexistente']):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 1)
            output = sys.stdout.getvalue()
            self.assertIn("Erro: Província 'Inexistente' não encontrada", output)

    def test_listar_municipios(self):
        with patch('sys.argv', ['angola-geo', 'listar', 'municipios']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Todos os Municípios", output)
            self.assertIn("Belas (Luanda)", output)

    def test_listar_municipios_filtro(self):
        with patch('sys.argv', ['angola-geo', 'listar', 'municipios', '-p', 'Luanda']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Municípios de Luanda", output)
            self.assertIn("Belas (Luanda)", output)
            self.assertNotIn("Benguela", output) # Should not show municipalities from other provinces

    def test_pesquisar(self):
        with patch('sys.argv', ['angola-geo', 'pesquisar', 'Luanda']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Resultados para 'Luanda'", output)
            self.assertIn("Províncias", output)
            # Luanda province and municipality should be found

    def test_novas(self):
        with patch('sys.argv', ['angola-geo', 'novas']):
            main()
            output = sys.stdout.getvalue()
            self.assertIn("Novas Províncias - Lei 14/24", output)
            self.assertIn("Cuando", output)
            self.assertIn("Icolo e Bengo", output)
            self.assertIn("Moxico Leste", output)

if __name__ == '__main__':
    unittest.main()
