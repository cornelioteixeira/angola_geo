"""
Funcionalidade principal da biblioteca Angola Geo.

Este módulo fornece a classe AngolaGeo com métodos para acessar
os dados das divisões administrativas de Angola.
"""

import json
import os
from typing import List, Dict, Optional, Any
from .excecoes import ProvinciaInexistente, MunicipioInexistente


class AngolaGeo:
    """
    Classe principal para acesso às divisões administrativas de Angola.
    
    Fornece métodos para recuperar e pesquisar províncias, municípios
    e comunas de acordo com a Lei n.º 14/24.
    """
    
    def __init__(self):
        """Inicializa a instância AngolaGeo e carrega os dados."""
        self._dados = self._carregar_dados()
        self._provincias = self._dados["provinces"]
        self._metadados = self._dados["metadata"]
    
    def _carregar_dados(self) -> Dict[str, Any]:
        """Carrega os dados das divisões do arquivo JSON."""
        caminho_dados = os.path.join(
            os.path.dirname(__file__),
            "data",
            "divisions.json"
        )
        
        with open(caminho_dados, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def obter_metadados(self) -> Dict[str, Any]:
        """
        Obtém os metadados sobre o conjunto de dados.
        
        Returns:
            Dicionário contendo metadados como referência da lei, datas, totais, etc.
            
        Example:
            >>> geo = AngolaGeo()
            >>> meta = geo.obter_metadados()
            >>> print(meta['total_provinces'])
            21
        """
        return self._metadados.copy()
    
    def listar_provincias(self) -> List[Dict[str, Any]]:
        """
        Lista todas as províncias.
        
        Returns:
            Lista com todas as 21 províncias e seus dados completos.
            
        Example:
            >>> geo = AngolaGeo()
            >>> provincias = geo.listar_provincias()
            >>> print(len(provincias))
            21
        """
        return [self._formatar_provincia(p) for p in self._provincias]
    
    def obter_provincia(self, nome: str) -> Dict[str, Any]:
        """
        Obtém uma província específica pelo nome.
        
        Args:
            nome: Nome da província (não diferencia maiúsculas/minúsculas).
            
        Returns:
            Dicionário contendo os dados da província.
            
        Raises:
            ProvinciaInexistente: Se a província não for encontrada.
            
        Example:
            >>> geo = AngolaGeo()
            >>> luanda = geo.obter_provincia("Luanda")
            >>> print(luanda['capital'])
            'Ingombota'
        """
        provincia = self._encontrar_provincia(nome)
        if not provincia:
            raise ProvinciaInexistente(nome)
        return self._formatar_provincia(provincia)
    
    def listar_municipios(self, provincia: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Lista municípios, opcionalmente filtrados por província.
        
        Args:
            provincia: Nome da província para filtrar (opcional).
            
        Returns:
            Lista de municípios. Se província for especificada, retorna apenas
            os municípios dessa província.
            
        Raises:
            ProvinciaInexistente: Se a província especificada não for encontrada.
            
        Example:
            >>> geo = AngolaGeo()
            >>> # Listar todos os municípios
            >>> todos = geo.listar_municipios()
            >>> # Listar apenas municípios de Luanda
            >>> luanda_munis = geo.listar_municipios(provincia="Luanda")
            >>> print(len(luanda_munis))
            16
        """
        if provincia:
            dados_provincia = self._encontrar_provincia(provincia)
            if not dados_provincia:
                raise ProvinciaInexistente(provincia)
            return self._formatar_municipios(
                dados_provincia["municipalities"],
                dados_provincia["name"]
            )
        
        # Obter todos os municípios de todas as províncias
        todos_municipios = []
        for prov in self._provincias:
            todos_municipios.extend(
                self._formatar_municipios(prov["municipalities"], prov["name"])
            )
        return todos_municipios
    
    def contar_municipios(self, provincia: Optional[str] = None) -> int:
        """
        Conta o número de municípios.
        
        Args:
            provincia: Nome da província para contar municípios (opcional).
            
        Returns:
            Total de municípios. Se província for especificada, retorna
            a contagem apenas dessa província.
            
        Raises:
            ProvinciaInexistente: Se a província especificada não for encontrada.
            
        Example:
            >>> geo = AngolaGeo()
            >>> total = geo.contar_municipios()
            >>> print(total)
            326
            >>> luanda_total = geo.contar_municipios(provincia="Luanda")
            >>> print(luanda_total)
            16
        """
        if provincia:
            dados_provincia = self._encontrar_provincia(provincia)
            if not dados_provincia:
                raise ProvinciaInexistente(provincia)
            return dados_provincia["municipality_count"]
        
        return self._metadados["total_municipalities"]
    
    def pesquisar(self, termo: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Pesquisa localizações em províncias, municípios e comunas.
        
        Args:
            termo: Termo de pesquisa (não diferencia maiúsculas/minúsculas).
            
        Returns:
            Dicionário com chaves 'provincias', 'municipios' e 'comunas',
            cada uma contendo uma lista de resultados correspondentes.
            
        Example:
            >>> geo = AngolaGeo()
            >>> resultados = geo.pesquisar("Bengo")
            >>> print(len(resultados['provincias']))
            2  # Bengo e Icolo e Bengo
        """
        termo_lower = termo.lower()
        resultados = {
            "provincias": [],
            "municipios": [],
            "comunas": []
        }
        
        # Pesquisar províncias
        for provincia in self._provincias:
            if termo_lower in provincia["name"].lower():
                resultados["provincias"].append(self._formatar_provincia(provincia))
            
            # Pesquisar municípios
            for municipio in provincia["municipalities"]:
                if termo_lower in municipio["name"].lower():
                    resultados["municipios"].append({
                        "nome": municipio["name"],
                        "provincia": provincia["name"],
                        "capital_provincia": provincia["capital"]
                    })
                
                # Pesquisar comunas
                for comuna in municipio.get("communes", []):
                    if isinstance(comuna, dict) and termo_lower in comuna.get("name", "").lower():
                        resultados["comunas"].append({
                            "nome": comuna["name"],
                            "municipio": municipio["name"],
                            "provincia": provincia["name"]
                        })
        
        return resultados
    
    def obter_nomes_provincias(self) -> List[str]:
        """
        Obtém uma lista simples com os nomes de todas as províncias.
        
        Returns:
            Lista com nomes das províncias.
            
        Example:
            >>> geo = AngolaGeo()
            >>> nomes = geo.obter_nomes_provincias()
            >>> print(nomes[0])
            'Bengo'
        """
        return [p["name"] for p in self._provincias]
    
    def obter_provincias_novas(self) -> List[Dict[str, Any]]:
        """
        Obtém as três novas províncias criadas pela Lei 14/24.
        
        Returns:
            Lista com as três novas províncias: Icolo e Bengo, Cuando e Moxico Leste.
            
        Example:
            >>> geo = AngolaGeo()
            >>> novas = geo.obter_provincias_novas()
            >>> print(len(novas))
            3
        """
        nomes_provincias_novas = ["Icolo e Bengo", "Cuando", "Moxico Leste"]
        return [
            self._formatar_provincia(p)
            for p in self._provincias
            if p["name"] in nomes_provincias_novas
        ]
    
    def _encontrar_provincia(self, nome: str) -> Optional[Dict[str, Any]]:
        """Encontra uma província pelo nome (não diferencia maiúsculas/minúsculas)."""
        nome_lower = nome.lower()
        for provincia in self._provincias:
            if provincia["name"].lower() == nome_lower:
                return provincia
        return None
    
    def _formatar_provincia(self, provincia: Dict[str, Any]) -> Dict[str, Any]:
        """Formata os dados da província para saída."""
        formatado = {
            "id": provincia["id"],
            "nome": provincia["name"],
            "capital": provincia["capital"],
            "total_municipios": provincia["municipality_count"],
            "municipios": self._formatar_municipios(
                provincia["municipalities"],
                provincia["name"]
            )
        }
        
        if "notes" in provincia:
            formatado["observacoes"] = provincia["notes"]
        
        return formatado
    
    def _formatar_municipios(
        self,
        municipios: List[Dict[str, Any]],
        nome_provincia: str
    ) -> List[Dict[str, Any]]:
        """Formata os dados dos municípios para saída."""
        return [
            {
                "nome": m["name"],
                "provincia": nome_provincia,
                "comunas": m.get("communes", [])
            }
            for m in municipios
        ]
