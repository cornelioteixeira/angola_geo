import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    'instalacao',
    'guia-rapido',
    {
      type: 'category',
      label: 'CLI',
      items: ['cli/overview'],
    },
  ],
  apiSidebar: [
    {
      type: 'category',
      label: 'API',
      items: ['api/overview', 'api/reference'],
    },
  ],

};

export default sidebars;
