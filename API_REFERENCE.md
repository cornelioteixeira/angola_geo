# API Reference - Angola Geo

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

### `AngolaGeo()`

Classe principal para acesso aos dados das divisões administrativas de Angola.

```python
from angola_geo import AngolaGeo

geo = AngolaGeo()
```

---

## Métodos de Províncias

### `listar_provincias() -> List[Dict]`

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

### `obter_provincia(nome: str) -> Dict`

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

### `obter_nomes_provincias() -> List[str]`

Retorna uma lista simples com os nomes de todas as províncias.

**Retorna:** Lista de strings com nomes das províncias

**Exemplo:**
```python
nomes = geo.obter_nomes_provincias()
# ['Bengo', 'Benguela', 'Bié', 'Cabinda', ...]
```

---

### `obter_provincias_novas() -> List[Dict]`

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

### `listar_municipios(provincia: str = None) -> List[Dict]`

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

### `contar_municipios(provincia: str = None) -> int`

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

### `pesquisar(termo: str) -> Dict[str, List]`

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

### `obter_metadados() -> Dict`

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

---

### `DadosInvalidos`

Lançada quando a validação de dados falha.

---

## Estrutura de Dados

### Província

```python
{
    'id': int,                    # ID único da província (1-21)
    'nome': str,                  # Nome da província
    'capital': str,               # Capital da província
    'total_municipios': int,      # Número de municípios
    'municipios': List[Dict],     # Lista de municípios
    'observacoes': str            # Observações (opcional)
}
```

### Município

```python
{
    'nome': str,           # Nome do município
    'provincia': str,      # Nome da província
    'comunas': List[Dict]  # Lista de comunas
}
```

### Resultado de Pesquisa

```python
{
    'provincias': List[Dict],   # Províncias encontradas
    'municipios': List[Dict],   # Municípios encontrados
    'comunas': List[Dict]       # Comunas encontradas
}
```

---

## Guia Rápido de Uso

### Cenário 1: Listar Todas as Províncias

```python
geo = AngolaGeo()
for provincia in geo.listar_provincias():
    print(f"{provincia['nome']} - {provincia['capital']}")
```

### Cenário 2: Obter Municípios de uma Província

```python
geo = AngolaGeo()
municipios = geo.listar_municipios(provincia="Luanda")
for muni in municipios:
    print(muni['nome'])
```

### Cenário 3: Pesquisar Localizações

```python
geo = AngolaGeo()
resultados = geo.pesquisar("Catete")
print(f"Encontradas {len(resultados['provincias'])} províncias")
print(f"Encontrados {len(resultados['municipios'])} municípios")
```

### Cenário 4: Estatísticas Gerais

```python
geo = AngolaGeo()
print(f"Total de províncias: {len(geo.listar_provincias())}")
print(f"Total de municípios: {geo.contar_municipios()}")
```

---

## Notas Importantes

1. **Case Insensitive**: Todas as buscas por nome não diferenciam maiúsculas de minúsculas
2. **Dados Incrementais**: Nomes de municípios e comunas estão sendo adicionados progressivamente
3. **Type Hints**: Todas as funções têm type hints para melhor suporte de IDE
4. **Documentação**: Todas as funções têm docstrings em português

---

## Versão

Versão atual: **0.1.0**

Para mais informações, consulte o [README.md](README.md) ou [CHANGELOG.md](CHANGELOG.md).
