"""
Angola Geo - Biblioteca completa para divisões administrativas de Angola.

Esta biblioteca fornece acesso às províncias, municípios e comunas de Angola
de acordo com a Lei n.º 14/24 (vigente desde 1 de Janeiro de 2025).
"""

from .core import AngolaGeo
from .excecoes import ProvinciaInexistente, MunicipioInexistente

__version__ = "0.2.0"
__all__ = ["AngolaGeo", "ProvinciaInexistente", "MunicipioInexistente"]
