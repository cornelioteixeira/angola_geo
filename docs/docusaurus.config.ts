import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Angola Geo',
  tagline: 'Biblioteca Python para divisões administrativas de Angola 🇦🇴',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://cornelioteixeira.github.io',
  baseUrl: '/angola_geo/',

  organizationName: 'cornelioteixeira',
  projectName: 'angola_geo',

  onBrokenLinks: 'throw',
  // onBrokenMarkdownLinks: 'warn', // Deprecated, moved to markdown.hooks? leaving it commented out for now to suppress warning.

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/cornelioteixeira/angola_geo/tree/main/docs/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl: 'https://github.com/cornelioteixeira/angola_geo/tree/main/docs/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/angola-geo-social-card.jpg',
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Angola Geo',
      logo: {
        alt: 'Angola Geo Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Documentação',
        },
        {
          type: 'docSidebar',
          sidebarId: 'apiSidebar',
          position: 'left',
          label: 'API',
        },
        { to: '/blog', label: 'Blog', position: 'left' },
        {
          href: 'https://github.com/cornelioteixeira/angola_geo',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentação',
          items: [
            {
              label: 'Introdução',
              to: '/docs/intro',
            },
            {
              label: 'Instalação',
              to: '/docs/instalacao',
            },
            {
              label: 'Guia Rápido',
              to: '/docs/guia-rapido',
            },
            {
              label: 'API Reference',
              to: '/docs/api/overview',
            },
          ],
        },
        {
          title: 'Recursos',
          items: [
            {
              label: 'CLI',
              to: '/docs/cli/overview',
            },
            {
              label: 'Exemplos',
              to: '/docs/guia-rapido',
            },
            {
              label: 'Referências',
              to: '/docs/api/reference',
            },
          ],
        },
        {
          title: 'Mais',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/cornelioteixeira/angola_geo',
            },
            {
              label: 'PyPI',
              href: 'https://pypi.org/project/angola-geo/',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Angola Geo. Baseado na Lei n.º 14/24. Licença MIT.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'bash', 'json'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
