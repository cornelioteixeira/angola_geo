---
sidebar_position: 2
---

# Instalação

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação via pip

A forma mais simples de instalar Angola Geo é através do pip:

```bash
pip install angola-geo
```

## Instalação em Ambiente Virtual (Recomendado)

É recomendado instalar a biblioteca em um ambiente virtual para evitar conflitos de dependências:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No Linux/macOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

# Instalar angola-geo
pip install angola-geo
```

## Instalação para Desenvolvimento

Se você deseja contribuir para o projeto ou modificar o código:

```bash
# Clonar o repositório
git clone https://github.com/yourusername/geolocation-ao.git
cd geolocation-ao

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar em modo de desenvolvimento
pip install -e .
```

## Verificar Instalação

Para verificar se a instalação foi bem-sucedida:

```python
import angola_geo
print(angola_geo.__version__)  # Deve mostrar: 0.2.0
```

Ou via CLI:

```bash
angola-geo info
```

## Dependências

Angola Geo não tem dependências externas! Usa apenas a biblioteca padrão do Python:
- `json` - Para carregar dados
- `os` - Para manipulação de caminhos
- `typing` - Para type hints
- `argparse` - Para CLI

## Problemas Comuns

### Erro: "command not found: angola-geo"

Se o comando `angola-geo` não for encontrado após a instalação, certifique-se de que o diretório de scripts do Python está no seu PATH:

```bash
# Verificar localização
which angola-geo

# Adicionar ao PATH (se necessário)
export PATH="$HOME/.local/bin:$PATH"
```

### Erro de Permissão

Se você receber um erro de permissão ao instalar:

```bash
# Instalar apenas para o usuário atual
pip install --user angola-geo
```

## Atualização

Para atualizar para a versão mais recente:

```bash
pip install --upgrade angola-geo
```

## Desinstalação

Para remover a biblioteca:

```bash
pip uninstall angola-geo
```

## Próximos Passos

Agora que você instalou Angola Geo, confira o [Guia Rápido](./guia-rapido.md) para começar a usar a biblioteca!
