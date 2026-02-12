# CLI - Guia de Uso

Ferramenta de linha de comando para consultas rápidas sobre as divisões administrativas de Angola.

## Instalação

Após instalar o pacote `angola-geo`, o comando `angola-geo` estará disponível globalmente:

```bash
pip install angola-geo
```

## Comandos Disponíveis

### 1. Informações do Dataset

Exibe informações gerais sobre o conjunto de dados.

```bash
angola-geo info
```

**Saída:**
```
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

---

### 2. Listar Províncias

Lista todas as 21 províncias de Angola.

```bash
angola-geo listar provincias
```

**Com detalhes (inclui lista de municípios):**
```bash
angola-geo listar provincias --detalhado
# ou
angola-geo listar provincias -d
```

**Saída:**
```
🇦🇴 Angola - 21 Províncias
============================================================

📍 Bengo
   Capital: Dande
   Municípios: 12

📍 Benguela
   Capital: Benguela
   Municípios: 23
...
```

---

### 3. Obter Província Específica

Obtém detalhes completos de uma província.

```bash
angola-geo obter provincia <nome>
```

**Exemplos:**
```bash
angola-geo obter provincia Luanda
angola-geo obter provincia "Icolo e Bengo"
angola-geo obter provincia Benguela
```

**Saída:**
```
🇦🇴 Província de Luanda
============================================================

📍 Luanda
   Capital: Ingombota
   Municípios: 16
   Lista de Municípios:
     • Belas
     • Cacuaco
     • Camama
     • Cazenga
     • Hoji-ya-Henda
     ...
```

---

### 4. Listar Municípios

Lista municípios, opcionalmente filtrados por província.

**Todos os municípios:**
```bash
angola-geo listar municipios
```

**Municípios de uma província específica:**
```bash
angola-geo listar municipios --provincia <nome>
# ou
angola-geo listar municipios -p <nome>
```

**Exemplos:**
```bash
angola-geo listar municipios --provincia Luanda
angola-geo listar municipios -p Bengo
angola-geo listar municipios -p "Icolo e Bengo"
```

**Saída:**
```
🏘️  Municípios de Luanda
============================================================
  • Belas (Luanda)
  • Cacuaco (Luanda)
  • Camama (Luanda)
  ...

============================================================
Total: 16 municípios com dados
```

---

### 5. Pesquisar

Pesquisa por um termo em todas as divisões administrativas (províncias, municípios e comunas).

```bash
angola-geo pesquisar <termo>
```

**Exemplos:**
```bash
angola-geo pesquisar Bengo
angola-geo pesquisar Catete
angola-geo pesquisar Luanda
```

**Saída:**
```
🔍 Resultados para 'Bengo'
============================================================

📍 Províncias (2):
  • Bengo (Capital: Dande)
  • Icolo e Bengo (Capital: Catete)

============================================================
Total: 2 resultados encontrados
```

---

### 6. Novas Províncias

Lista as três novas províncias criadas pela Lei 14/24.

```bash
angola-geo novas
```

**Saída:**
```
🆕 Novas Províncias - Lei 14/24
============================================================

📍 Cuando
   Capital: Mavinga
   Municípios: 9
   ℹ️  New province created from division of Cuando Cubango

📍 Icolo e Bengo
   Capital: Catete
   Municípios: 7
   ℹ️  New province created from division of Luanda

📍 Moxico Leste
   Capital: Cazombo
   Municípios: 9
   ℹ️  New province created from division of Moxico
```

---

## Exemplos de Uso Comum

### Encontrar informações sobre uma província

```bash
# Ver detalhes de Luanda
angola-geo obter provincia Luanda

# Ver municípios de Luanda
angola-geo listar municipios -p Luanda
```

### Pesquisar localizações

```bash
# Pesquisar por "Bengo"
angola-geo pesquisar Bengo

# Pesquisar por "Catete"
angola-geo pesquisar Catete
```

### Explorar o dataset

```bash
# Ver informações gerais
angola-geo info

# Ver todas as províncias
angola-geo listar provincias

# Ver províncias com detalhes
angola-geo listar provincias --detalhado

# Ver as novas províncias
angola-geo novas
```

---

## Dicas

1. **Nomes com espaços**: Use aspas para nomes com espaços
   ```bash
   angola-geo obter provincia "Icolo e Bengo"
   angola-geo listar municipios -p "Cuanza Norte"
   ```

2. **Case insensitive**: Os comandos não diferenciam maiúsculas de minúsculas
   ```bash
   angola-geo obter provincia luanda  # Funciona
   angola-geo obter provincia LUANDA  # Funciona
   angola-geo obter provincia Luanda  # Funciona
   ```

3. **Ajuda**: Use `--help` para ver ajuda de qualquer comando
   ```bash
   angola-geo --help
   angola-geo listar --help
   angola-geo obter --help
   ```

---

## Tratamento de Erros

Se uma província não for encontrada:
```bash
$ angola-geo obter provincia ProvinciaInvalida

❌ Erro: Província 'ProvinciaInvalida' não encontrada

💡 Dica: Use 'angola-geo listar provincias' para ver todas as províncias disponíveis
```

---

## Integração com Scripts

A CLI pode ser facilmente integrada em scripts shell:

```bash
#!/bin/bash

# Obter lista de províncias
angola-geo listar provincias > provincias.txt

# Pesquisar e salvar resultados
angola-geo pesquisar Luanda > resultados_luanda.txt

# Obter informações do dataset
angola-geo info
```

---

## Desenvolvimento

Para usar a CLI em modo de desenvolvimento (sem instalar):

```bash
# No diretório do projeto
PYTHONPATH=. python3 -m angola_geo.cli <comando>

# Exemplo
PYTHONPATH=. python3 -m angola_geo.cli info
```
