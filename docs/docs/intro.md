---
sidebar_position: 1
---

# Introdução

Bem-vindo à documentação da **Angola Geo** 🇦🇴

Angola Geo é uma biblioteca Python completa para trabalhar com as divisões administrativas de Angola de acordo com a **Lei n.º 14/24** (vigente desde 1 de Janeiro de 2025).

## O que é Angola Geo?

Angola Geo fornece acesso programático às **21 províncias**, **326 municípios** e **378 comunas** de Angola, com uma API intuitiva em português e uma ferramenta CLI para consultas rápidas.

## Características Principais

- ✅ **API 100% em Português** - Nomes de funções intuitivos e auto-explicativos
- ✅ **CLI Incluída** - Ferramenta de linha de comando para consultas rápidas
- ✅ **Dados Oficiais** - Baseados na Lei n.º 14/24
- ✅ **Type Hints Completos** - Suporte total de IDE
- ✅ **Bem Testada** - 21 testes unitários, 100% de cobertura
- ✅ **Bem Documentada** - Documentação abrangente em português
- ✅ **Open Source** - Licença MIT

## Dados Disponíveis

### Províncias: 21/21 (100%)

Todas as 21 províncias com:
- Nome oficial
- Capital
- Contagem de municípios
- Lista de municípios (quando disponível)

**Novas Províncias (Lei 14/24):**
- **Icolo e Bengo** (separada de Luanda) - Capital: Catete
- **Cuando** (separada de Cuando Cubango) - Capital: Mavinga
- **Moxico Leste** (separada de Moxico) - Capital: Cazombo

### Municípios: 35/326 (11%)

Dados completos para:
- **Luanda:** 16/16 municípios ✅
- **Bengo:** 12/12 municípios ✅
- **Icolo e Bengo:** 7/7 municípios ✅

### Comunas: 0/378 (0%)

Estrutura de dados preparada, aguardando coleta de dados.

## Início Rápido

```python
from angola_geo import AngolaGeo

# Inicializar
geo = AngolaGeo()

# Listar províncias
provincias = geo.listar_provincias()
print(f"Total: {len(provincias)} províncias")

# Obter província específica
luanda = geo.obter_provincia("Luanda")
print(f"Capital de Luanda: {luanda['capital']}")

# Pesquisar
resultados = geo.pesquisar("Bengo")
print(f"Encontradas {len(resultados['provincias'])} províncias")
```

## Próximos Passos

- [Instalação](./instalacao.md) - Como instalar a biblioteca
- [Guia Rápido](./guia-rapido.md) - Primeiros passos
- [API Reference](./api/overview.md) - Documentação completa da API
- [CLI](./cli/overview.md) - Ferramenta de linha de comando

## Base Legal

Esta biblioteca é baseada na **Lei n.º 14/24, de 5 de Setembro de 2024**, publicada no Diário da República Iª Série n.º 171, que estabelece a nova divisão político-administrativa da República de Angola.

**Data de Vigência:** 1 de Janeiro de 2025

## Licença

Angola Geo é software livre distribuído sob a [Licença MIT](https://opensource.org/licenses/MIT).
