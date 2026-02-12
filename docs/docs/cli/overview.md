---
sidebar_position: 1
---

# CLI - Visão Geral

A Angola Geo inclui uma ferramenta de linha de comando (CLI) completa para consultas rápidas sobre as divisões administrativas de Angola.

## Instalação

A CLI é instalada automaticamente quando você instala o pacote angola-geo:

```bash
pip install angola-geo
```

Após a instalação, o comando `angola-geo` estará disponível globalmente.

## Verificar Instalação

```bash
angola-geo --help
```

## Comandos Disponíveis

### 1. `info` - Informações do Dataset

Exibe informações gerais sobre o conjunto de dados.

```bash
angola-geo info
```

### 2. `listar provincias` - Listar Províncias

Lista todas as 21 províncias de Angola.

```bash
angola-geo listar provincias
angola-geo listar provincias --detalhado
```

### 3. `obter provincia` - Obter Província

Obtém detalhes completos de uma província específica.

```bash
angola-geo obter provincia Luanda
angola-geo obter provincia "Icolo e Bengo"
```

### 4. `listar municipios` - Listar Municípios

Lista municípios, opcionalmente filtrados por província.

```bash
angola-geo listar municipios
angola-geo listar municipios --provincia Luanda
angola-geo listar municipios -p Bengo
```

### 5. `pesquisar` - Pesquisar

Pesquisa por um termo em todas as divisões administrativas.

```bash
angola-geo pesquisar Bengo
angola-geo pesquisar Catete
```

### 6. `novas` - Novas Províncias

Lista as três novas províncias criadas pela Lei 14/24.

```bash
angola-geo novas
```

## Características

- ✅ **Interface em Português** - Comandos e mensagens em português
- ✅ **Emojis** - Interface visual com emojis (🇦🇴 📍 🏘️ 🔍)
- ✅ **Formatação Clara** - Saída bem organizada e legível
- ✅ **Tratamento de Erros** - Mensagens de erro amigáveis
- ✅ **Case Insensitive** - Não diferencia maiúsculas/minúsculas
- ✅ **Suporte a Espaços** - Nomes com espaços entre aspas

## Exemplo de Saída

```bash
$ angola-geo info

🇦🇴 Angola Geo - Informações do Dataset
============================================================

📜 Lei: Lei n.º 14/24
📅 Data de Publicação: 2024-09-05
✅ Data de Vigência: 2025-01-01

📊 Estatísticas:
   • Províncias: 21
   • Municípios: 326
   • Comunas: 378

🆕 Novas Províncias (3):
   • Cuando (Capital: Mavinga)
   • Icolo e Bengo (Capital: Catete)
   • Moxico Leste (Capital: Cazombo)
```


