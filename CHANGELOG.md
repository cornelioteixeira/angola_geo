# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-02-12

### Added
- **CLI Tool**: Ferramenta de linha de comando completa para consultas rápidas
  - `angola-geo info` - Informações do dataset
  - `angola-geo listar provincias` - Lista todas as províncias
  - `angola-geo obter provincia <nome>` - Detalhes de uma província
  - `angola-geo listar municipios` - Lista municípios (com filtro opcional)
  - `angola-geo pesquisar <termo>` - Pesquisa em todas as divisões
  - `angola-geo novas` - Lista as 3 novas províncias
- Interface em português com emojis para melhor UX
- Documentação completa da CLI em [CLI_GUIDE.md](CLI_GUIDE.md)

### Changed
- **API Refatorada para Português**: Todos os nomes de funções agora em português
  - `get_provinces()` → `listar_provincias()`
  - `get_province()` → `obter_provincia()`
  - `get_municipalities()` → `listar_municipios()`
  - `get_municipality_count()` → `contar_municipios()`
  - `search()` → `pesquisar()`
  - `get_province_names()` → `obter_nomes_provincias()`
  - `get_new_provinces()` → `obter_provincias_novas()`
  - `get_metadata()` → `obter_metadados()`
- **Exceções em Português**:
  - `ProvinceNotFoundError` → `ProvinciaInexistente`
  - `MunicipalityNotFoundError` → `MunicipioInexistente`
  - `InvalidDataError` → `DadosInvalidos`
- Estrutura de retorno das funções com chaves em português
  - `name` → `nome`
  - `capital` → `capital` (mantido)
  - `municipality_count` → `total_municipios`
  - `municipalities` → `municipios`
  - `notes` → `observacoes`
- README atualizado com exemplos da nova API
- Criado API_REFERENCE.md com documentação completa em português

## [0.1.0] - 2026-02-12

### Added
- Initial release of angola-geo library
- Support for all 21 provinces according to Lei 14/24
- Complete data for 35 municipalities (Luanda: 16, Bengo: 12, Icolo e Bengo: 7)
- Province metadata including capitals and municipality counts
- Core API methods (English version - deprecated in 0.2.0)
- Custom exceptions for better error handling
- Comprehensive documentation and examples
- Unit tests with 100% coverage of implemented features

### Data Coverage
- Provinces: 21/21 (100%)
- Municipality counts: 21/21 provinces (100%)
- Municipality names: 35/326 (11%)
- Communes: 0/378 (0%)

### Notes
- This is an incremental release. Municipality and commune names will be added progressively.
- Data is based on Lei n.º 14/24, effective January 1, 2025.

## [Unreleased]

### Planned
- Add remaining municipality names (291 municipalities)
- Add commune/district data (378 communes)
- Add geographic coordinates for provinces and municipalities
- Add population data
- Add area/size data
- Add postal codes
- REST API wrapper
