<p align="center">
  <img src="logo.png" alt="Angola Geo Logo" width="300"/>
</p>

# Angola Geolocation Library 🇦🇴

Biblioteca Python completa para trabalhar com as divisões administrativas de Angola de acordo com a **Lei 14/24** (vigente desde 1 de Janeiro de 2025).

## Características

- ✅ **21 Províncias** com metadados completos
- ✅ **326 Municípios** organizados por província
- ✅ **378 Comunas** (estrutura de dados pronta)
- 🔍 Funcionalidade de pesquisa para localizações
- 🎯 Filtrar por província, município ou distrito
- 📊 Dados estruturados em JSON limpo
- 🐍 Type hints para melhor suporte de IDE
- 📚 Documentação abrangente em português

## Instalação

```bash
pip install angola-geo
```

## Início Rápido

```python
from angola_geo import AngolaGeo

# Inicializar a biblioteca
geo = AngolaGeo()

# Listar todas as províncias
provincias = geo.listar_provincias()
print(f"Total de províncias: {len(provincias)}")  # 21

# Obter uma província específica
luanda = geo.obter_provincia("Luanda")
print(f"Capital: {luanda['capital']}")  # Ingombota
print(f"Municípios: {luanda['total_municipios']}")  # 16

# Listar municípios de uma província
municipios_luanda = geo.listar_municipios(provincia="Luanda")
print(f"Luanda tem {len(municipios_luanda)} municípios")

# Pesquisar localizações
resultados = geo.pesquisar("Bengo")
# Retorna correspondências de províncias, municípios e comunas

# Listar todos os municípios
todos_municipios = geo.listar_municipios()
print(f"Total de municípios: {len(todos_municipios)}")  # 326
```

## Ferramenta CLI

A biblioteca inclui uma ferramenta de linha de comando para consultas rápidas:

```bash
# Informações do dataset
angola-geo info

# Listar todas as províncias
angola-geo listar provincias

# Obter detalhes de uma província
angola-geo obter provincia Luanda

# Listar municípios de uma província
angola-geo listar municipios --provincia Luanda

# Pesquisar localizações
angola-geo pesquisar Bengo

# Ver as novas províncias
angola-geo novas
```

**Veja o [CLI_GUIDE.md](CLI_GUIDE.md) para documentação completa da CLI.**

## Estrutura dos Dados

A biblioteca fornece dados de acordo com a nova divisão político-administrativa de Angola:

### Novas Províncias (2025)
Três novas províncias foram criadas a partir das existentes:
- **Icolo e Bengo** (de Luanda) - Capital: Catete
- **Cuando** (de Cuando Cubango) - Capital: Mavinga  
- **Moxico Leste** (de Moxico) - Capital: Cazombo

### Hierarquia Administrativa
```
Província (21)
  └── Município (326)
      └── Comuna/Distrito (378)
```

## Referência da API

### `listar_provincias()`
Retorna uma lista de todas as 21 províncias com seus metadados.

```python
provincias = geo.listar_provincias()
# [{'id': 1, 'nome': 'Bengo', 'capital': 'Dande', 'total_municipios': 12, ...}, ...]
```

### `obter_provincia(nome: str)`
Retorna informações detalhadas sobre uma província específica.

```python
provincia = geo.obter_provincia("Luanda")
```

### `listar_municipios(provincia: str = None)`
Retorna municípios, opcionalmente filtrados por província.

```python
# Todos os municípios
todos = geo.listar_municipios()

# Apenas municípios de Luanda
luanda_munis = geo.listar_municipios(provincia="Luanda")
```

### `contar_municipios(provincia: str = None)`
Retorna a contagem de municípios.

```python
total = geo.contar_municipios()  # 326
luanda_total = geo.contar_municipios(provincia="Luanda")  # 16
```

### `pesquisar(termo: str)`
Pesquisa em províncias, municípios e comunas.

```python
resultados = geo.pesquisar("Catete")
# Retorna localizações correspondentes com sua hierarquia
```

### `obter_nomes_provincias()`
Retorna uma lista simples com os nomes das províncias.

```python
nomes = geo.obter_nomes_provincias()
# ['Bengo', 'Benguela', 'Bié', ...]
```

### `obter_provincias_novas()`
Retorna as três novas províncias criadas pela Lei 14/24.

```python
novas = geo.obter_provincias_novas()
# [Icolo e Bengo, Cuando, Moxico Leste]
```

### `obter_metadados()`
Retorna metadados sobre o conjunto de dados.

```python
meta = geo.obter_metadados()
# {'law': 'Lei n.º 14/24', 'total_provinces': 21, ...}
```

## Tratamento de Erros

A biblioteca fornece exceções customizadas para melhor tratamento de erros:

```python
from angola_geo import AngolaGeo, ProvinciaInexistente

geo = AngolaGeo()

try:
    provincia = geo.obter_provincia("ProvinciaInvalida")
except ProvinciaInexistente as e:
    print(f"Erro: {e}")  # "Província 'ProvinciaInvalida' não encontrada"
```

## Fontes de Dados

Esta biblioteca utiliza dados oficiais de:
- **Lei n.º 14/24** (5 de Setembro de 2024) - Lei oficial de divisão administrativa
- Ministério da Administração do Território (MAT)
- Fontes oficiais do Governo de Angola

## Estado do Desenvolvimento

🚧 **Desenvolvimento Ativo** - Nomes de municípios e comunas estão sendo adicionados incrementalmente.

Cobertura atual:
- ✅ Todas as 21 províncias (100%)
- ✅ Contagens de municípios para todas as províncias (100%)
- 🔄 Nomes de municípios (35/326 - 11%)
  - Luanda: 16/16 ✅
  - Bengo: 12/12 ✅
  - Icolo e Bengo: 7/7 ✅
- 🔄 Dados de comunas/distritos (em progresso)

## Contribuindo

Contribuições são bem-vindas! Se você tem dados oficiais para municípios ou comunas, por favor submeta um pull request.

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes detalhadas.

## Licença

Licença MIT - veja o arquivo LICENSE para detalhes

## Changelog

Veja [CHANGELOG.md](CHANGELOG.md) para histórico de versões.

## Suporte

Para problemas, questões ou contribuições, visite nosso [repositório GitHub](https://github.com/cornelioteixeira/angola_geo).

---

## Exemplos de Uso

### Exemplo 1: Listar Todas as Províncias

```python
from angola_geo import AngolaGeo

geo = AngolaGeo()
provincias = geo.listar_provincias()

for provincia in provincias:
    print(f"{provincia['nome']} - Capital: {provincia['capital']}")
```

### Exemplo 2: Obter Municípios de uma Província

```python
geo = AngolaGeo()
municipios = geo.listar_municipios(provincia="Luanda")

print(f"Municípios de Luanda:")
for municipio in municipios:
    print(f"  - {municipio['nome']}")
```

### Exemplo 3: Pesquisar Localizações

```python
geo = AngolaGeo()
resultados = geo.pesquisar("Bengo")

print(f"Províncias encontradas: {len(resultados['provincias'])}")
print(f"Municípios encontrados: {len(resultados['municipios'])}")
```

### Exemplo 4: Obter Estatísticas

```python
geo = AngolaGeo()
meta = geo.obter_metadados()

print(f"Lei: {meta['law']}")
print(f"Total de Províncias: {meta['total_provinces']}")
print(f"Total de Municípios: {meta['total_municipalities']}")
print(f"Total de Comunas: {meta['total_communes']}")
```

## API Developer-Friendly

Todos os nomes de funções são em **português**, **intuitivos** e **auto-explicativos**:

- ✅ `listar_provincias()` - Lista todas as províncias
- ✅ `obter_provincia()` - Obtém uma província específica
- ✅ `listar_municipios()` - Lista municípios
- ✅ `contar_municipios()` - Conta municípios
- ✅ `pesquisar()` - Pesquisa localizações
- ✅ `obter_nomes_provincias()` - Obtém nomes das províncias
- ✅ `obter_provincias_novas()` - Obtém províncias novas
- ✅ `obter_metadados()` - Obtém metadados

**Exceções em Português:**
- `ProvinciaInexistente` - Quando uma província não é encontrada
- `MunicipioInexistente` - Quando um município não é encontrado
- `DadosInvalidos` - Quando a validação de dados falha

## Referências

Esta biblioteca é baseada em fontes oficiais do Governo de Angola:

### Legislação
- **Lei n.º 14/24, de 5 de Setembro de 2024** - Divisão Político-Administrativa da República de Angola
- **Diário da República Iª Série n.º 171** - Publicação oficial
- **Data de Vigência:** 1 de Janeiro de 2025

### Fontes de Dados
- Ministério da Administração do Território (MAT)
- Instituto Nacional de Estatística (INE)
- Governo de Angola - [governo.gov.ao](https://governo.gov.ao)

### Citação
```bibtex
@software{angola_geo,
  author = {Teixeira, Cornelio},
  title = {Angola Geo: Biblioteca Python para divisões administrativas de Angola},
  year = {2026},
  version = {0.2.0},
  url = {https://github.com/cornelioteixeira/angola_geo},
  note = {Baseado na Lei n.º 14/24, de 5 de Setembro de 2024}
}
```

**Para referências completas e detalhadas, consulte [REFERENCES.md](REFERENCES.md)**
