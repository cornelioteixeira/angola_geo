# Angola Geo - Documentação Docusaurus

Este diretório contém o site de documentação Docusaurus para a biblioteca Angola Geo.

## Estrutura

```
docs/
├── docs/               # Páginas de documentação
│   ├── intro.md       # Introdução
│   ├── instalacao.md  # Guia de instalação
│   ├── guia-rapido.md # Guia rápido
│   ├── api/           # Referência da API
│   ├── cli/           # Documentação da CLI
│   └── exemplos/      # Exemplos de uso
├── blog/              # Posts do blog
├── src/               # Componentes React customizados
├── static/            # Arquivos estáticos
└── docusaurus.config.ts  # Configuração do Docusaurus
```

## Desenvolvimento Local

### Pré-requisitos

- Node.js 18 ou superior
- npm

### Instalação

```bash
cd docs
npm install
```

### Executar Localmente

```bash
npm start
```

Isso iniciará um servidor de desenvolvimento local em `http://localhost:3000`.

### Build

```bash
npm run build
```

Isso gerará o site estático no diretório `build/`.

### Servir Build Local

```bash
npm run serve
```

## Deploy

### GitHub Pages

Para fazer deploy no GitHub Pages:

```bash
npm run deploy
```

Certifique-se de configurar corretamente:
- `organizationName` em `docusaurus.config.ts`
- `projectName` em `docusaurus.config.ts`
- `url` e `baseUrl` conforme necessário

## Personalização

### Configuração

Edite `docusaurus.config.ts` para personalizar:
- Título e tagline
- URLs e links
- Navbar e footer
- Temas e cores

### Sidebar

Edite `sidebars.ts` para organizar a estrutura da documentação.

### Estilos

Edite `src/css/custom.css` para customizar cores e estilos.

## Adicionar Conteúdo

### Nova Página de Documentação

1. Crie um arquivo `.md` em `docs/`
2. Adicione frontmatter:
   ```md
   ---
   sidebar_position: 1
   ---
   
   # Título da Página
   ```
3. Adicione ao `sidebars.ts` se necessário

### Novo Post de Blog

1. Crie um arquivo em `blog/`
2. Use o formato: `YYYY-MM-DD-titulo.md`
3. Adicione frontmatter:
   ```md
   ---
   slug: titulo-do-post
   title: Título do Post
   authors: [nome]
   tags: [tag1, tag2]
   ---
   ```

## Recursos

- [Documentação do Docusaurus](https://docusaurus.io/)
- [Guia de Markdown](https://docusaurus.io/docs/markdown-features)
- [Temas e Plugins](https://docusaurus.io/docs/using-plugins)
