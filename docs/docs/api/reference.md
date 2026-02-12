---
sidebar_position: 2
title: Referência da API
---

# Referência da API

Referência rápida de todas as funções disponíveis na biblioteca Angola Geo.

## Índice

- [Classe Principal](#classe-principal)
- [Métodos de Províncias](#métodos-de-províncias)
- [Métodos de Municípios](#métodos-de-municípios)
- [Métodos de Pesquisa](#métodos-de-pesquisa)
- [Métodos Utilitários](#métodos-utilitários)
- [Exceções](#exceções)

---

## Classe Principal

### `AngolaGeo`

Classe principal para acesso aos dados das divisões administrativas de Angola.

```python
from angola_geo import AngolaGeo

geo = AngolaGeo()
```

---

## Métodos de Províncias

### `listar_provincias`

Lista todas as 21 províncias com seus dados completos.

**Retorna:** Lista de dicionários com dados das províncias

**Exemplo:**
```python
provincias = geo.listar_provincias()
# [
#   {
#     'id': 1,
#     'nome': 'Bengo',
#     'capital': 'Dande',
#     'total_municipios': 12,
#     'municipios': [...]
#   },
#   ...
# ]
```

---

### `obter_provincia`

Obtém dados detalhados de uma província específica.

**Parâmetros:**
- `nome` (str): Nome da província (não diferencia maiúsculas/minúsculas)

**Retorna:** Dicionário com dados da província

**Lança:** `ProvinciaInexistente` se a província não for encontrada

**Exemplo:**
```python
luanda = geo.obter_provincia("Luanda")
# {
#   'id': 13,
#   'nome': 'Luanda',
#   'capital': 'Ingombota',
#   'total_municipios': 16,
#   'municipios': [...]
# }
```

---

### `obter_nomes_provincias`

Retorna uma lista simples com os nomes de todas as províncias.

**Retorna:** Lista de strings com nomes das províncias

**Exemplo:**
```python
nomes = geo.obter_nomes_provincias()
# ['Bengo', 'Benguela', 'Bié', 'Cabinda', ...]
```

---

### `obter_provincias_novas`

Retorna as três novas províncias criadas pela Lei 14/24.

**Retorna:** Lista com Icolo e Bengo, Cuando e Moxico Leste

**Exemplo:**
```python
novas = geo.obter_provincias_novas()
# [
#   {'nome': 'Icolo e Bengo', 'capital': 'Catete', ...},
#   {'nome': 'Cuando', 'capital': 'Mavinga', ...},
#   {'nome': 'Moxico Leste', 'capital': 'Cazombo', ...}
# ]
```

---

## Métodos de Municípios

### `listar_municipios`

Lista municípios, opcionalmente filtrados por província.

**Parâmetros:**
- `provincia` (str, opcional): Nome da província para filtrar

**Retorna:** Lista de dicionários com dados dos municípios

**Lança:** `ProvinciaInexistente` se a província especificada não existir

**Exemplos:**
```python
# Todos os municípios
todos = geo.listar_municipios()

# Apenas municípios de Luanda
luanda_munis = geo.listar_municipios(provincia="Luanda")
# [
#   {'nome': 'Belas', 'provincia': 'Luanda', 'comunas': []},
#   {'nome': 'Cacuaco', 'provincia': 'Luanda', 'comunas': []},
#   ...
# ]
```

---

### `contar_municipios`

Retorna a contagem de municípios.

**Parâmetros:**
- `provincia` (str, opcional): Nome da província para contar

**Retorna:** Número inteiro com a contagem

**Lança:** `ProvinciaInexistente` se a província especificada não existir

**Exemplos:**
```python
# Total de municípios em Angola
total = geo.contar_municipios()  # 326

# Municípios apenas de Luanda
luanda_total = geo.contar_municipios(provincia="Luanda")  # 16
```

---

## Métodos de Pesquisa

### `pesquisar`

Pesquisa localizações em províncias, municípios e comunas.

**Parâmetros:**
- `termo` (str): Termo de pesquisa (não diferencia maiúsculas/minúsculas)

**Retorna:** Dicionário com chaves 'provincias', 'municipios' e 'comunas'

**Exemplo:**
```python
resultados = geo.pesquisar("Bengo")
# {
#   'provincias': [
#     {'nome': 'Bengo', ...},
#     {'nome': 'Icolo e Bengo', ...}
#   ],
#   'municipios': [...],
#   'comunas': [...]
# }
```

---

## Métodos Utilitários

### `obter_metadados`

Retorna metadados sobre o conjunto de dados.

**Retorna:** Dicionário com informações sobre a lei, datas, totais, etc.

**Exemplo:**
```python
meta = geo.obter_metadados()
# {
#   'law': 'Lei n.º 14/24',
#   'publication_date': '2024-09-05',
#   'effective_date': '2025-01-01',
#   'total_provinces': 21,
#   'total_municipalities': 326,
#   'total_communes': 378,
#   'sources': [...]
# }
```

---

## Exceções

### `ProvinciaInexistente`

Lançada quando uma província não é encontrada.

**Atributos:**
- `nome_provincia` (str): Nome da província que não foi encontrada

**Exemplo:**
```python
from angola_geo import ProvinciaInexistente

try:
    provincia = geo.obter_provincia("ProvinciaInvalida")
except ProvinciaInexistente as e:
    print(e)  # "Província 'ProvinciaInvalida' não encontrada"
    print(e.nome_provincia)  # "ProvinciaInvalida"
```

---

### `MunicipioInexistente`

Lançada quando um município não é encontrado.

**Atributos:**
- `nome_municipio` (str): Nome do município que não foi encontrado

**Exemplo:**
```python
from angola_geo import MunicipioInexistente

try:
    # Código que pode lançar MunicipioInexistente
    pass
except MunicipioInexistente as e:
    print(e)  # "Município 'MunicipioInvalido' não encontrado"
```
