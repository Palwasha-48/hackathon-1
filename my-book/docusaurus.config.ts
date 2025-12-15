import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";

const config: Config = {
  title: "Physical AI & Humanoid Robotics",
  tagline: "Comprehensive Guide to Modern Robotics",

  // ⚡ Use your live deployed Vercel domain here
  url: "https://hackathon-1-z2zd-3zeximv8f-palwashas-projects-fb8f707a.vercel.app",
  baseUrl: "/",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  favicon: "img/favicon.ico",

  // Only one plugins array
  plugins: [
    [
      "@docusaurus/plugin-client-redirects",
      {
        fromExtensions: ["html"],
      },
    ],
  ],

  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          editUrl: "https://github.com/Palwasha-1/hackathon-1/edit/main/",
        },
        blog: {
          showReadingTime: true,
          editUrl: "https://github.com/Palwasha-48/hackathon-1/edit/main/blog/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: "Physical AI",
      logo: {
        alt: "Site Logo",
        src: "img/logo.svg",
      },
      items: [
        { to: "/docs/course-introduction", label: "Docs", position: "left" },
        { to: "/blog", label: "Blog", position: "left" },
        // { to: "/auth/sign-in", label: "Sign In", position: "right" },
        {
          href: "https://github.com/Palwasha-48/hackathon-1",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [{ label: "Intro", to: "/docs/course-introduction" }],
        },
        {
          title: "Community",
          items: [
            { label: "Discord", href: "https://discord.gg/your-link" },
            { label: "Twitter", href: "https://twitter.com/your-link" },
          ],
        },
        {
          title: "More",
          items: [
            { label: "Blog", to: "/blog" },
            {
              label: "GitHub",
              href: "https://github.com/your-username/your-repo",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Palwashey. Built with Docusaurus.`,
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
