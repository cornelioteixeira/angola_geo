---
sidebar_position: 1
---

# Visão Geral da API

A Angola Geo fornece uma API simples e intuitiva em português para acessar dados das divisões administrativas de Angola.

## Classe Principal

### `AngolaGeo`

Classe principal que fornece acesso a todos os dados e funcionalidades.

```python
from angola_geo import AngolaGeo

geo = AngolaGeo()
```

## Métodos Disponíveis

### Províncias

| Método | Descrição |
|--------|-----------|
| [`listar_provincias()`](./reference.md#listar_provincias) | Lista todas as 21 províncias |
| [`obter_provincia(nome)`](./reference.md#obter_provincia) | Obtém dados de uma província específica |
| [`obter_nomes_provincias()`](./reference.md#obter_nomes_provincias) | Retorna lista simples de nomes |
| [`obter_provincias_novas()`](./reference.md#obter_provincias_novas) | Retorna as 3 novas províncias |

### Municípios

| Método | Descrição |
|--------|-----------|
| [`listar_municipios(provincia)`](./reference.md#listar_municipios) | Lista municípios (com filtro opcional) |
| [`contar_municipios(provincia)`](./reference.md#contar_municipios) | Conta municípios |

### Pesquisa e Metadados

| Método | Descrição |
|--------|-----------|
| [`pesquisar(termo)`](./reference.md#pesquisar) | Pesquisa em todas as divisões |
| [`obter_metadados()`](./reference.md#obter_metadados) | Obtém informações do dataset |

## Exceções

| Exceção | Quando é Lançada |
|---------|------------------|
| [`ProvinciaInexistente`](./reference.md#provinciainexistente) | Província não encontrada |
| [`MunicipioInexistente`](./reference.md#municipioinexistente) | Município não encontrado |

## Estruturas de Dados

### Província

```python
{
    "id": int,                    # ID único (1-21)
    "nome": str,                  # Nome da província
    "capital": str,               # Capital da província
    "total_municipios": int,      # Número de municípios
    "municipios": List[Dict],     # Lista de municípios
    "observacoes": str            # Observações (opcional)
}
```

### Município

```python
{
    "nome": str,           # Nome do município
    "provincia": str,      # Nome da província
    "comunas": List[Dict]  # Lista de comunas
}
```

### Resultado de Pesquisa

```python
{
    "provincias": List[Dict],   # Províncias encontradas
    "municipios": List[Dict],   # Municípios encontrados
    "comunas": List[Dict]       # Comunas encontradas
}
```

## Características

- ✅ **Type Hints Completos** - Suporte total de IDE
- ✅ **Case Insensitive** - Buscas não diferenciam maiúsculas/minúsculas
- ✅ **Exceções Customizadas** - Mensagens de erro claras
- ✅ **Sem Dependências** - Usa apenas biblioteca padrão Python
- ✅ **Imutável** - Dados não podem ser modificados acidentalmente

## Exemplo Completo

```python
from angola_geo import AngolaGeo, ProvinciaInexistente

# Inicializar
geo = AngolaGeo()

# Listar províncias
provincias = geo.listar_provincias()
print(f"Total: {len(provincias)} províncias")

# Obter província
try:
    luanda = geo.obter_provincia("Luanda")
    print(f"Capital: {luanda['capital']}")
except ProvinciaInexistente as e:
    print(f"Erro: {e}")

# Listar municípios
municipios = geo.listar_municipios(provincia="Luanda")
print(f"Luanda tem {len(municipios)} municípios")

# Pesquisar
resultados = geo.pesquisar("Bengo")
print(f"Encontradas {len(resultados['provincias'])} províncias")

# Metadados
meta = geo.obter_metadados()
print(f"Lei: {meta['law']}")
```

## Próximos Passos

Explore a documentação detalhada de cada método:
- [listar_provincias()](./reference.md#listar_provincias)
- [obter_provincia()](./reference.md#obter_provincia)
- [listar_municipios()](./reference.md#listar_municipios)
- [pesquisar()](./reference.md#pesquisar)
