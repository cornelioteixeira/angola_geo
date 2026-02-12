---
sidebar_position: 3
---

# Guia Rápido

Este guia mostra como começar a usar Angola Geo em poucos minutos.

## Importar a Biblioteca

```python
from angola_geo import AngolaGeo

# Inicializar
geo = AngolaGeo()
```

## Listar Províncias

```python
# Obter todas as províncias
provincias = geo.listar_provincias()

print(f"Total de províncias: {len(provincias)}")  # 21

# Mostrar primeiras 3
for provincia in provincias[:3]:
    print(f"- {provincia['nome']} (Capital: {provincia['capital']})")
```

**Saída:**
```
Total de províncias: 21
- Bengo (Capital: Dande)
- Benguela (Capital: Benguela)
- Bié (Capital: Cuíto)
```

## Obter Província Específica

```python
# Obter dados de Luanda
luanda = geo.obter_provincia("Luanda")

print(f"Província: {luanda['nome']}")
print(f"Capital: {luanda['capital']}")
print(f"Municípios: {luanda['total_municipios']}")
```

**Saída:**
```
Província: Luanda
Capital: Ingombota
Municípios: 16
```

## Listar Municípios

```python
# Todos os municípios
todos_municipios = geo.listar_municipios()
print(f"Total: {len(todos_municipios)} municípios")

# Municípios de uma província específica
municipios_luanda = geo.listar_municipios(provincia="Luanda")

for muni in municipios_luanda[:5]:
    print(f"- {muni['nome']}")
```

**Saída:**
```
Total: 35 municípios
- Belas
- Cacuaco
- Camama
- Cazenga
- Hoji-ya-Henda
```

## Pesquisar Localizações

```python
# Pesquisar por "Bengo"
resultados = geo.pesquisar("Bengo")

print(f"Províncias: {len(resultados['provincias'])}")
print(f"Municípios: {len(resultados['municipios'])}")

# Mostrar províncias encontradas
for prov in resultados['provincias']:
    print(f"- {prov['nome']}")
```

**Saída:**
```
Províncias: 2
Municípios: 0
- Bengo
- Icolo e Bengo
```

## Obter Metadados

```python
# Informações sobre o dataset
meta = geo.obter_metadados()

print(f"Lei: {meta['law']}")
print(f"Vigência: {meta['effective_date']}")
print(f"Total de Províncias: {meta['total_provinces']}")
print(f"Total de Municípios: {meta['total_municipalities']}")
```

**Saída:**
```
Lei: Lei n.º 14/24
Vigência: 2025-01-01
Total de Províncias: 21
Total de Municípios: 326
```

## Novas Províncias

```python
# Obter as 3 novas províncias criadas pela Lei 14/24
novas = geo.obter_provincias_novas()

for provincia in novas:
    print(f"- {provincia['nome']} (Capital: {provincia['capital']})")
```

**Saída:**
```
- Cuando (Capital: Mavinga)
- Icolo e Bengo (Capital: Catete)
- Moxico Leste (Capital: Cazombo)
```

## Tratamento de Erros

```python
from angola_geo import ProvinciaInexistente

try:
    provincia = geo.obter_provincia("ProvinciaInvalida")
except ProvinciaInexistente as e:
    print(f"Erro: {e}")
```

**Saída:**
```
Erro: Província 'ProvinciaInvalida' não encontrada
```

## Usando a CLI

Você também pode usar a ferramenta de linha de comando:

```bash
# Informações do dataset
angola-geo info

# Listar províncias
angola-geo listar provincias

# Obter província específica
angola-geo obter provincia Luanda

# Pesquisar
angola-geo pesquisar Bengo
```

## Próximos Passos

- [API Reference](./api/overview.md) - Documentação completa de todos os métodos
- [CLI](./cli/overview.md) - Guia completo da ferramenta CLI

