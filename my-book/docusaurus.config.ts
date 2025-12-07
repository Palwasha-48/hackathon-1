import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Comprehensive Guide to Modern Robotics Technologies',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://palwasha-48.github.io',
  baseUrl: '/h-3/',

  organizationName: 'Palwasha-48',
  projectName: 'h-3',

  onBrokenLinks: 'throw',

  // ❌ REMOVE THIS — because it's causing duplicate classic theme error
  // themes: ['@docusaurus/theme-classic'],

  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        fromExtensions: ['html'],
      },
    ],
  ],

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ur'],
    localeConfigs: {
      en: {
        label: 'English',
      },
      ur: {
        label: 'Urdu',
        direction: 'rtl',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Physical AI & Humanoid Robotics Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Book Content',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/Palwasha-48',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Book Content',
          items: [
            {label: 'Introduction', to: '/docs/course-introduction/'},
            {label: 'Module 1: ROS2 Basics', to: '/docs/module-1-ros2-basics/'},
            {label: 'Module 2: Digital Twin Technologies', to: '/docs/module-2-digital-twin/'},
            {label: 'Module 3: Isaac Sim', to: '/docs/module-3-isaac-sim/'},
            {label: 'Module 4: VLA Systems', to: '/docs/module-4-vla-systems/'},
          ],
        },
        {
          title: 'Resources',
          items: [
            {label: 'Robotics Stack Exchange', href: 'https://robotics.stackexchange.com/'},
            {label: 'ROS Community', href: 'https://discourse.ros.org/'},
            {label: 'GitHub Profile', href: 'https://github.com/Palwasha-48'},
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'Blog', to: '/blog'},
            {label: 'GitHub', href: 'https://github.com/your-org/physical-ai-book'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Book. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
