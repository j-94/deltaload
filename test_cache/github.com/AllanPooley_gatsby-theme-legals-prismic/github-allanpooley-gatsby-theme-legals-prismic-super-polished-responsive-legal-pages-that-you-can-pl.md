---
title: GitHub - AllanPooley/gatsby-theme-legals-prismic: Super polished, responsive legal pages that you can plug onto your Gatsby project 🌻🔨⚖️
description: Super polished, responsive legal pages that you can plug onto your Gatsby project 🌻🔨⚖️ - AllanPooley/gatsby-theme-legals-prismic
url: https://github.com/AllanPooley/gatsby-theme-legals-prismic
timestamp: 2025-01-20T15:31:16.963Z
domain: github.com
path: AllanPooley_gatsby-theme-legals-prismic
---

# GitHub - AllanPooley/gatsby-theme-legals-prismic: Super polished, responsive legal pages that you can plug onto your Gatsby project 🌻🔨⚖️


Super polished, responsive legal pages that you can plug onto your Gatsby project 🌻🔨⚖️ - AllanPooley/gatsby-theme-legals-prismic


## Content

[![Image 5: Mockups of gatsby-theme-legals-prismic in action](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup.jpg)

Gatsby Theme Legals Prismic
---------------------------

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#gatsby-theme-legals-prismic)

*   [Gatsby Theme](https://www.gatsbyjs.org/docs/themes/what-are-gatsby-themes/) for adding polished legal pages 💅out-of-the-box.
*   Responsive across Mobiles 📱, Tablets 💊 and Desktops 🖥️
*   Customisable to your brand using [Theme UI](https://theme-ui.com/) 🎨
*   Builds legal pages sourced from content in [Prismic](https://prismic.io/)
*   Demo at [https://gatsby-theme-legals.netlify.com/](https://gatsby-theme-legals.netlify.com/)

Why?
----

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#why)

Legal pages are probably the most unexciting part of your site, and the last place you want to expend your creative energy.

The purpose of `gatsby-theme-legals` is to do the heavy lifting for you. Super polished, responsive legal pages that you can just plug onto your existing project.

Installation
------------

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#installation)

```
yarn add @littleplusbig/gatsby-theme-legals-prismic
```

Configuration
-------------

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#configuration)

In your `gatsby-config.js`, under `plugins` add:

```
{
  resolve: "gatsby-theme-legals-prismic",
  options: {
    prismicRepositoryName: PRISMIC_REPO_NAME,
    prismicAccessToken: PRISMIC_API_KEY,
    siteName: YOUR_SITE_NAME, // (Optional)
    homePath: HOME_PATH // (Optional) Defaults to '/'
  },
},
```

Replacing `PRISMIC_REPO_NAME`, `PRISMIC_API_KEY`, `YOUR_SITE_NAME` and `HOME_PATH` with their respective values.

Prismic Configuration
---------------------

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#prismic-configuration)

1.  Create a new custom type in your Prismic repository.
2.  Make sure that it is repeatable and name it `Legal`.
3.  Using the JSON Editor paste in the following content structure:

```
{
  "Main": {
    "page_name": {
      "type": "StructuredText",
      "config": {
        "single": "heading1",
        "label": "Page Name",
        "placeholder": "Privacy Policy"
      }
    },
    "uid": {
      "type": "UID",
      "config": {
        "label": "Slug",
        "placeholder": "privacy-policy"
      }
    },
    "hero_subtitle": {
      "type": "StructuredText",
      "config": {
        "single": "paragraph",
        "label": "Hero Subtitle",
        "placeholder": "How we manage your data"
      }
    },
    "sections": {
      "type": "Group",
      "config": {
        "fields": {
          "section_heading": {
            "type": "StructuredText",
            "config": {
              "single": "heading2",
              "label": "Section Heading",
              "placeholder": "General information"
            }
          },
          "content": {
            "type": "StructuredText",
            "config": {
              "multi": "paragraph, preformatted, heading3, strong, em, hyperlink, list-item, o-list-item, o-list-item",
              "allowTargetBlank": true,
              "label": "Content",
              "placeholder": "Information on this website is of a general nature. Our company has ..."
            }
          }
        },
        "label": "Sections"
      }
    }
  },
  "SEO": {
    "meta_title": {
      "type": "StructuredText",
      "config": {
        "single": "heading1",
        "label": "Meta Title",
        "placeholder": "Enter meta title"
      }
    },
    "meta_description": {
      "type": "StructuredText",
      "config": {
        "single": "paragraph",
        "label": "Meta Description",
        "placeholder": "Enter meta description"
      }
    },
    "open_graph_image": {
      "type": "Image",
      "config": {
        "constraint": {
          "width": 1200,
          "height": 630
        },
        "thumbnails": [],
        "label": "Open Graph Image"
      }
    }
  }
}
```

4.  Create one or more `Legal` Content pages, each with 1 or more sections. Don't forget to populate each page's `SEO` tab!

Laying Down the Law
-------------------

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#laying-down-the-law)

If you don't already have a Privacy Policy or Terms and Conditions document, you can generate one at [Iubenda](https://www.iubenda.com/).

Overriding the Theme
--------------------

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#overriding-the-theme)

### Colors and Styles

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#colors-and-styles)

This project uses [theme-ui](https://theme-ui.com/), allowing some of the styling to be customised to your project's brand.

In order to override the styles, in the `src` directory of your project, add a folder titled `gatsby-plugin-theme-ui`, and within that folder a file named `index.js`.

Inside of this file (`your-gatsby-project/src/gatsby-plugin-theme-ui/index.js`) add the following:

```
import baseTheme from '@littleplusbig/gatsby-theme-legals-prismic/src/gatsby-plugin-theme-ui';

export default {
  ...baseTheme,
  fonts: {
    ...baseTheme.fonts,
    body: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',
    heading: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',
  },
  colors: {
    ...baseTheme.colors,
    text: '#333333',
    background: '#FFFFFF',
    primary: '#6F2B9F',
    primaryDark: '#5B2589',
    primaryLight: '#BB75D1',
    white: '#FFFFFF',
    offWhite: '#FCFAFF',
    black: '#000000',
    offBlack: '#333333',
    grey: '#F3F3F3',
  },
};

```

Above are the default values for the theme, which you can change depending on your project.

In particular, the colours accenting each legal page are controlled by `primary`, `primaryLight` and `primaryDark`.

For example, here is how I might change the theme colours from shades of purple, to a snazzy blue:

```
import baseTheme from '@littleplusbig/gatsby-theme-legals-prismic/src/gatsby-plugin-theme-ui';

export default {
  ...baseTheme,
  colors: {
    ...baseTheme.colors,
    primary: '#7ed6df',
    primaryDark: '#22a6b3',
    primaryLight: '#c7ecee',
  },
};

```

[![Image 6: An example of a theme color change](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup-color-change.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup-color-change.jpg)

The complete set of customisable theme values can be explored in [gatsby-theme-legals-prismic/src/styles/theme.js](https://github.com/littleplusbig/gatsby-theme-legals-prismic/blob/master/src/styles/theme.js)

More information about `gatsby-plugin-theme-ui` [here](https://www.npmjs.com/package/gatsby-plugin-theme-ui).

### Components

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#components)

The components that make up the legal pages can be some what customised too. This can be done through concept new to Gatsby Themes called '[Component Shadowing](https://www.gatsbyjs.org/blog/2019-04-29-component-shadowing/)'.

If you wish to override a component, in the `src` directory of your project, create the following directory structure: `@littleplusbig/gatsby-theme-legals-prismic/components`.

There are several components that a legal page, they can all be viewed here: [gatsby-theme-legals-prismic/src/components](https://github.com/littleplusbig/gatsby-theme-legals-prismic/tree/master/src/components)

An example of how these components might be customised is adding your project's `<Header />` and `<Footer />` components to the layout.

In order to do this I create a shadowing `layout.js` in the directory we've just created (`your-gatsby-project/src/@littleplusbig/gatsby-theme-legals-prismic/components/layout.js`):

```
import React from 'react';
import { Header, Footer } from '../../somewhere-in-your-project'

export default ({ children }) => (
  <>
    <Header />
    {children}
    <Footer />
  </>
);
```

Markdown? Contentful? WordPress?
--------------------------------

[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#markdown-contentful-wordpress)

Soon my friend, soon.

## Metadata

```json
{
  "title": "GitHub - AllanPooley/gatsby-theme-legals-prismic: Super polished, responsive legal pages that you can plug onto your Gatsby project 🌻🔨⚖️",
  "description": "Super polished, responsive legal pages that you can plug onto your Gatsby project 🌻🔨⚖️ - AllanPooley/gatsby-theme-legals-prismic",
  "url": "https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true",
  "content": "[![Image 5: Mockups of gatsby-theme-legals-prismic in action](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup.jpg)\n\nGatsby Theme Legals Prismic\n---------------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#gatsby-theme-legals-prismic)\n\n*   [Gatsby Theme](https://www.gatsbyjs.org/docs/themes/what-are-gatsby-themes/) for adding polished legal pages 💅out-of-the-box.\n*   Responsive across Mobiles 📱, Tablets 💊 and Desktops 🖥️\n*   Customisable to your brand using [Theme UI](https://theme-ui.com/) 🎨\n*   Builds legal pages sourced from content in [Prismic](https://prismic.io/)\n*   Demo at [https://gatsby-theme-legals.netlify.com/](https://gatsby-theme-legals.netlify.com/)\n\nWhy?\n----\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#why)\n\nLegal pages are probably the most unexciting part of your site, and the last place you want to expend your creative energy.\n\nThe purpose of `gatsby-theme-legals` is to do the heavy lifting for you. Super polished, responsive legal pages that you can just plug onto your existing project.\n\nInstallation\n------------\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#installation)\n\n```\nyarn add @littleplusbig/gatsby-theme-legals-prismic\n```\n\nConfiguration\n-------------\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#configuration)\n\nIn your `gatsby-config.js`, under `plugins` add:\n\n```\n{\n  resolve: \"gatsby-theme-legals-prismic\",\n  options: {\n    prismicRepositoryName: PRISMIC_REPO_NAME,\n    prismicAccessToken: PRISMIC_API_KEY,\n    siteName: YOUR_SITE_NAME, // (Optional)\n    homePath: HOME_PATH // (Optional) Defaults to '/'\n  },\n},\n```\n\nReplacing `PRISMIC_REPO_NAME`, `PRISMIC_API_KEY`, `YOUR_SITE_NAME` and `HOME_PATH` with their respective values.\n\nPrismic Configuration\n---------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#prismic-configuration)\n\n1.  Create a new custom type in your Prismic repository.\n2.  Make sure that it is repeatable and name it `Legal`.\n3.  Using the JSON Editor paste in the following content structure:\n\n```\n{\n  \"Main\": {\n    \"page_name\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"heading1\",\n        \"label\": \"Page Name\",\n        \"placeholder\": \"Privacy Policy\"\n      }\n    },\n    \"uid\": {\n      \"type\": \"UID\",\n      \"config\": {\n        \"label\": \"Slug\",\n        \"placeholder\": \"privacy-policy\"\n      }\n    },\n    \"hero_subtitle\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"paragraph\",\n        \"label\": \"Hero Subtitle\",\n        \"placeholder\": \"How we manage your data\"\n      }\n    },\n    \"sections\": {\n      \"type\": \"Group\",\n      \"config\": {\n        \"fields\": {\n          \"section_heading\": {\n            \"type\": \"StructuredText\",\n            \"config\": {\n              \"single\": \"heading2\",\n              \"label\": \"Section Heading\",\n              \"placeholder\": \"General information\"\n            }\n          },\n          \"content\": {\n            \"type\": \"StructuredText\",\n            \"config\": {\n              \"multi\": \"paragraph, preformatted, heading3, strong, em, hyperlink, list-item, o-list-item, o-list-item\",\n              \"allowTargetBlank\": true,\n              \"label\": \"Content\",\n              \"placeholder\": \"Information on this website is of a general nature. Our company has ...\"\n            }\n          }\n        },\n        \"label\": \"Sections\"\n      }\n    }\n  },\n  \"SEO\": {\n    \"meta_title\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"heading1\",\n        \"label\": \"Meta Title\",\n        \"placeholder\": \"Enter meta title\"\n      }\n    },\n    \"meta_description\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"paragraph\",\n        \"label\": \"Meta Description\",\n        \"placeholder\": \"Enter meta description\"\n      }\n    },\n    \"open_graph_image\": {\n      \"type\": \"Image\",\n      \"config\": {\n        \"constraint\": {\n          \"width\": 1200,\n          \"height\": 630\n        },\n        \"thumbnails\": [],\n        \"label\": \"Open Graph Image\"\n      }\n    }\n  }\n}\n```\n\n4.  Create one or more `Legal` Content pages, each with 1 or more sections. Don't forget to populate each page's `SEO` tab!\n\nLaying Down the Law\n-------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#laying-down-the-law)\n\nIf you don't already have a Privacy Policy or Terms and Conditions document, you can generate one at [Iubenda](https://www.iubenda.com/).\n\nOverriding the Theme\n--------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#overriding-the-theme)\n\n### Colors and Styles\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#colors-and-styles)\n\nThis project uses [theme-ui](https://theme-ui.com/), allowing some of the styling to be customised to your project's brand.\n\nIn order to override the styles, in the `src` directory of your project, add a folder titled `gatsby-plugin-theme-ui`, and within that folder a file named `index.js`.\n\nInside of this file (`your-gatsby-project/src/gatsby-plugin-theme-ui/index.js`) add the following:\n\n```\nimport baseTheme from '@littleplusbig/gatsby-theme-legals-prismic/src/gatsby-plugin-theme-ui';\n\nexport default {\n  ...baseTheme,\n  fonts: {\n    ...baseTheme.fonts,\n    body: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',\n    heading: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',\n  },\n  colors: {\n    ...baseTheme.colors,\n    text: '#333333',\n    background: '#FFFFFF',\n    primary: '#6F2B9F',\n    primaryDark: '#5B2589',\n    primaryLight: '#BB75D1',\n    white: '#FFFFFF',\n    offWhite: '#FCFAFF',\n    black: '#000000',\n    offBlack: '#333333',\n    grey: '#F3F3F3',\n  },\n};\n\n```\n\nAbove are the default values for the theme, which you can change depending on your project.\n\nIn particular, the colours accenting each legal page are controlled by `primary`, `primaryLight` and `primaryDark`.\n\nFor example, here is how I might change the theme colours from shades of purple, to a snazzy blue:\n\n```\nimport baseTheme from '@littleplusbig/gatsby-theme-legals-prismic/src/gatsby-plugin-theme-ui';\n\nexport default {\n  ...baseTheme,\n  colors: {\n    ...baseTheme.colors,\n    primary: '#7ed6df',\n    primaryDark: '#22a6b3',\n    primaryLight: '#c7ecee',\n  },\n};\n\n```\n\n[![Image 6: An example of a theme color change](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup-color-change.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-legals-demo/master/src/assets/images/gatsby-theme-legals-prismic-mockup-color-change.jpg)\n\nThe complete set of customisable theme values can be explored in [gatsby-theme-legals-prismic/src/styles/theme.js](https://github.com/littleplusbig/gatsby-theme-legals-prismic/blob/master/src/styles/theme.js)\n\nMore information about `gatsby-plugin-theme-ui` [here](https://www.npmjs.com/package/gatsby-plugin-theme-ui).\n\n### Components\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#components)\n\nThe components that make up the legal pages can be some what customised too. This can be done through concept new to Gatsby Themes called '[Component Shadowing](https://www.gatsbyjs.org/blog/2019-04-29-component-shadowing/)'.\n\nIf you wish to override a component, in the `src` directory of your project, create the following directory structure: `@littleplusbig/gatsby-theme-legals-prismic/components`.\n\nThere are several components that a legal page, they can all be viewed here: [gatsby-theme-legals-prismic/src/components](https://github.com/littleplusbig/gatsby-theme-legals-prismic/tree/master/src/components)\n\nAn example of how these components might be customised is adding your project's `<Header />` and `<Footer />` components to the layout.\n\nIn order to do this I create a shadowing `layout.js` in the directory we've just created (`your-gatsby-project/src/@littleplusbig/gatsby-theme-legals-prismic/components/layout.js`):\n\n```\nimport React from 'react';\nimport { Header, Footer } from '../../somewhere-in-your-project'\n\nexport default ({ children }) => (\n  <>\n    <Header />\n    {children}\n    <Footer />\n  </>\n);\n```\n\nMarkdown? Contentful? WordPress?\n--------------------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-legals-prismic?screenshot=true#markdown-contentful-wordpress)\n\nSoon my friend, soon.",
  "usage": {
    "tokens": 2142
  }
}
```
