"""
Testes unitários para a biblioteca angola_geo.
"""

import unittest
from angola_geo import AngolaGeo, ProvinciaInexistente, MunicipioInexistente


class TestAngolaGeo(unittest.TestCase):
    """Casos de teste para a classe AngolaGeo."""
    
    def setUp(self):
        """Configurar fixtures de teste."""
        self.geo = AngolaGeo()
    
    def test_metadados(self):
        """Testar obtenção de metadados."""
        metadados = self.geo.obter_metadados()
        
        self.assertEqual(metadados['total_provinces'], 21)
        self.assertEqual(metadados['total_municipalities'], 326)
        self.assertEqual(metadados['total_communes'], 378)
        self.assertEqual(metadados['law'], "Lei n.º 14/24")
        self.assertEqual(metadados['effective_date'], "2025-01-01")
    
    def test_listar_provincias_contagem(self):
        """Testar que obtemos exatamente 21 províncias."""
        provincias = self.geo.listar_provincias()
        self.assertEqual(len(provincias), 21)
    
    def test_listar_provincias_estrutura(self):
        """Testar estrutura dos dados das províncias."""
        provincias = self.geo.listar_provincias()
        
        for provincia in provincias:
            self.assertIn('id', provincia)
            self.assertIn('nome', provincia)
            self.assertIn('capital', provincia)
            self.assertIn('total_municipios', provincia)
            self.assertIn('municipios', provincia)
            self.assertIsInstance(provincia['municipios'], list)
    
    def test_obter_provincia_luanda(self):
        """Testar obtenção da província de Luanda."""
        luanda = self.geo.obter_provincia("Luanda")
        
        self.assertEqual(luanda['nome'], "Luanda")
        self.assertEqual(luanda['capital'], "Ingombota")
        self.assertEqual(luanda['total_municipios'], 16)
        self.assertEqual(len(luanda['municipios']), 16)
    
    def test_obter_provincia_case_insensitive(self):
        """Testar que busca de província não diferencia maiúsculas/minúsculas."""
        luanda1 = self.geo.obter_provincia("Luanda")
        luanda2 = self.geo.obter_provincia("LUANDA")
        luanda3 = self.geo.obter_provincia("luanda")
        
        self.assertEqual(luanda1['nome'], luanda2['nome'])
        self.assertEqual(luanda2['nome'], luanda3['nome'])
    
    def test_obter_provincia_inexistente(self):
        """Testar que ProvinciaInexistente é lançada para província inválida."""
        with self.assertRaises(ProvinciaInexistente) as context:
            self.geo.obter_provincia("ProvinciaInexistente")
        
        self.assertIn("ProvinciaInexistente", str(context.exception))
    
    def test_obter_provincias_novas(self):
        """Testar obtenção das três províncias novas."""
        provincias_novas = self.geo.obter_provincias_novas()
        
        self.assertEqual(len(provincias_novas), 3)
        
        nomes_provincias_novas = {p['nome'] for p in provincias_novas}
        nomes_esperados = {"Icolo e Bengo", "Cuando", "Moxico Leste"}
        
        self.assertEqual(nomes_provincias_novas, nomes_esperados)
    
    def test_obter_nomes_provincias(self):
        """Testar obtenção da lista de nomes das províncias."""
        nomes = self.geo.obter_nomes_provincias()
        
        self.assertEqual(len(nomes), 21)
        self.assertIn("Luanda", nomes)
        self.assertIn("Bengo", nomes)
        self.assertIn("Icolo e Bengo", nomes)
    
    def test_contar_municipios_total(self):
        """Testar contagem total de municípios."""
        contagem = self.geo.contar_municipios()
        self.assertEqual(contagem, 326)
    
    def test_contar_municipios_por_provincia(self):
        """Testar contagem de municípios por província específica."""
        self.assertEqual(self.geo.contar_municipios("Luanda"), 16)
        self.assertEqual(self.geo.contar_municipios("Bengo"), 12)
        self.assertEqual(self.geo.contar_municipios("Icolo e Bengo"), 7)
    
    def test_listar_municipios_todos(self):
        """Testar listagem de todos os municípios."""
        municipios = self.geo.listar_municipios()
        
        # Temos 35 municípios com nomes até agora
        municipios_com_nomes = [m for m in municipios if m['nome']]
        self.assertEqual(len(municipios_com_nomes), 35)
    
    def test_listar_municipios_por_provincia(self):
        """Testar listagem de municípios filtrados por província."""
        municipios_luanda = self.geo.listar_municipios(provincia="Luanda")
        
        self.assertEqual(len(municipios_luanda), 16)
        
        # Verificar que todos os municípios pertencem a Luanda
        for muni in municipios_luanda:
            self.assertEqual(muni['provincia'], "Luanda")
    
    def test_listar_municipios_provincia_invalida(self):
        """Testar que erro é lançado para província inválida em listar_municipios."""
        with self.assertRaises(ProvinciaInexistente):
            self.geo.listar_municipios(provincia="ProvinciaInvalida")
    
    def test_pesquisar_provincias(self):
        """Testar funcionalidade de pesquisa para províncias."""
        resultados = self.geo.pesquisar("Bengo")
        
        # Deve encontrar Bengo e Icolo e Bengo
        self.assertEqual(len(resultados['provincias']), 2)
        
        nomes_provincias = {p['nome'] for p in resultados['provincias']}
        self.assertIn("Bengo", nomes_provincias)
        self.assertIn("Icolo e Bengo", nomes_provincias)
    
    def test_pesquisar_municipios(self):
        """Testar funcionalidade de pesquisa para municípios."""
        resultados = self.geo.pesquisar("Belas")
        
        # Deve encontrar o município Belas em Luanda
        self.assertGreater(len(resultados['municipios']), 0)
        
        belas = next((m for m in resultados['municipios'] if m['nome'] == "Belas"), None)
        self.assertIsNotNone(belas)
        self.assertEqual(belas['provincia'], "Luanda")
    
    def test_pesquisar_case_insensitive(self):
        """Testar que pesquisa não diferencia maiúsculas/minúsculas."""
        resultados1 = self.geo.pesquisar("luanda")
        resultados2 = self.geo.pesquisar("LUANDA")
        resultados3 = self.geo.pesquisar("Luanda")
        
        self.assertEqual(len(resultados1['provincias']), len(resultados2['provincias']))
        self.assertEqual(len(resultados2['provincias']), len(resultados3['provincias']))
    
    def test_integridade_dados_municipios(self):
        """Testar que contagens de municípios correspondem aos dados reais."""
        for provincia in self.geo.listar_provincias():
            contagem_declarada = provincia['total_municipios']
            contagem_real = len(provincia['municipios'])
            
            # Se a lista de municípios está populada, deve corresponder à contagem
            if contagem_real > 0:
                self.assertEqual(
                    contagem_declarada,
                    contagem_real,
                    f"Província {provincia['nome']} tem contagem de municípios incompatível"
                )


class TestIntegridadeDados(unittest.TestCase):
    """Testes de integridade e consistência dos dados."""
    
    def setUp(self):
        """Configurar fixtures de teste."""
        self.geo = AngolaGeo()
    
    def test_contagem_total_municipios(self):
        """Testar que soma de todos os municípios é igual a 326."""
        provincias = self.geo.listar_provincias()
        total = sum(p['total_municipios'] for p in provincias)
        
        self.assertEqual(total, 326)
    
    def test_ids_provincias_unicos(self):
        """Testar que todos os IDs das províncias são únicos."""
        provincias = self.geo.listar_provincias()
        ids = [p['id'] for p in provincias]
        
        self.assertEqual(len(ids), len(set(ids)))
    
    def test_nomes_provincias_unicos(self):
        """Testar que todos os nomes das províncias são únicos."""
        provincias = self.geo.listar_provincias()
        nomes = [p['nome'] for p in provincias]
        
        self.assertEqual(len(nomes), len(set(nomes)))
    
    def test_todas_provincias_tem_capitais(self):
        """Testar que todas as províncias têm capitais definidas."""
        provincias = self.geo.listar_provincias()
        
        for provincia in provincias:
            self.assertIsNotNone(provincia['capital'])
            self.assertNotEqual(provincia['capital'], "")


if __name__ == '__main__':
    unittest.main()
