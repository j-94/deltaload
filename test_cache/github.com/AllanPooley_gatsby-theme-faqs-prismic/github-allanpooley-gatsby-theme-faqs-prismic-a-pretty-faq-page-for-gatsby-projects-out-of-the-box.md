---
title: GitHub - AllanPooley/gatsby-theme-faqs-prismic: A pretty FAQ page for Gatsby projects, out of the box 🌻❓🙋
description: A pretty FAQ page for Gatsby projects, out of the box 🌻❓🙋 - AllanPooley/gatsby-theme-faqs-prismic
url: https://github.com/AllanPooley/gatsby-theme-faqs-prismic
timestamp: 2025-01-20T15:31:18.926Z
domain: github.com
path: AllanPooley_gatsby-theme-faqs-prismic
---

# GitHub - AllanPooley/gatsby-theme-faqs-prismic: A pretty FAQ page for Gatsby projects, out of the box 🌻❓🙋


A pretty FAQ page for Gatsby projects, out of the box 🌻❓🙋 - AllanPooley/gatsby-theme-faqs-prismic


## Content

[![Image 8: Mockups of gatsby-theme-faqs-prismic in action](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup.jpg)

Gatsby Theme FAQs Prismic
-------------------------

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#gatsby-theme-faqs-prismic)

*   [Gatsby Theme](https://www.gatsbyjs.org/docs/themes/what-are-gatsby-themes/) for adding a pretty FAQ page for Gatsby projects, out of the box 🌻🙋
*   Responsive across Mobiles 📱, Tablets 💊 and Desktops 🖥️
*   Customisable to your brand using [Theme UI](https://theme-ui.com/) 🎨
*   Builds FAQ page(s) sourced from content in [Prismic](https://prismic.io/)
*   Demo at [https://gatsby-theme-faqs.netlify.com/](https://gatsby-theme-faqs.netlify.com/)

Why?
----

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#why)

The Frequently Asked Questions (FAQ) is a common place page on most website. Though, it doesn't exactly summon the creative juices, it's a pretty basic page, [much like legal pages](https://github.com/littleplusbig/gatsby-theme-legals-prismic).

The idea of `gatsby-theme-faqs-prismic` is do it once well - a super neat, clean and responsive implementation. It's reusable, theme-able and customisable 🎉

Installation
------------

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#installation)

```
yarn add @littleplusbig/gatsby-theme-faqs-prismic
```

Configuration
-------------

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#configuration)

In your `gatsby-config.js`, under `plugins` add:

```
{
  resolve: "gatsby-theme-faqs-prismic",
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

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#prismic-configuration)

1.  Create a new custom type in your Prismic repository.
2.  Make sure that it is repeatable and name it `Question Category`.
3.  Using the JSON Editor paste in the following content structure:

```
{
  "Main" : {
    "category_name" : {
      "type" : "StructuredText",
      "config" : {
        "single" : "heading1",
        "label" : "Category Name",
        "placeholder" : "Category Name"
      }
    },
    "uid" : {
      "type" : "UID",
      "config" : {
        "label" : "Category Slug",
        "placeholder" : "category-slug"
      }
    }
  }
}
```

4.  Create one or more `Question Category` Content pages.
    
5.  Next, create another custom type in your Prismic repository, singular or repeatable depending on your needs, and name it `Frequently Asked Questions`.
    
6.  Using the JSON Editor paste in the following content structure:
    

```
{
  "Main": {
    "page_name": {
      "type": "StructuredText",
      "config": {
        "single": "heading1",
        "label": "Page Name",
        "placeholder": "Enter page name"
      }
    },
    "uid": {
      "type": "UID",
      "config": {
        "label": "Slug",
        "placeholder": "Enter slug"
      }
    },
    "hero_subtitle": {
      "type": "StructuredText",
      "config": {
        "single": "paragraph",
        "label": "Hero Subtitle",
        "placeholder": "You have questions, we have answers"
      }
    },
    "questions": {
      "type": "Group",
      "config": {
        "fields": {
          "question": {
            "type": "StructuredText",
            "config": {
              "single": "heading2",
              "label": "Question",
              "placeholder": "How safe is the journey?"
            }
          },
          "answer": {
            "type": "StructuredText",
            "config": {
              "multi": "paragraph, heading3, heading4, heading5, heading6, strong, em, hyperlink, image, embed, list-item, o-list-item, o-list-item",
              "allowTargetBlank": true,
              "label": "Answer",
              "placeholder": "The trip to Mars cannot be called risk free. Like any venture..."
            }
          },
          "category": {
            "type": "Link",
            "config": {
              "select": "document",
              "customtypes": [
                "question_category"
              ],
              "label": "Category"
            }
          }
        },
        "label": "Questions"
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

7.  Create a `Frequently Asked Question` content page.

Overriding the Theme
--------------------

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#overriding-the-theme)

### Colors and Styles

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#colors-and-styles)

This project uses [theme-ui](https://theme-ui.com/), allowing some of the styling to be customised to your project's brand.

In order to override the styles, in the `src` directory of your project, add a folder titled `gatsby-plugin-theme-ui`, and within that folder a file named `index.js`.

Inside of this file (`your-gatsby-project/src/gatsby-plugin-theme-ui/index.js`) add the following:

```
import baseTheme from '@littleplusbig/gatsby-theme-faqs-prismic/src/gatsby-plugin-theme-ui';

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
    primary: '#1e3799',
    primaryLight: '#4a69bd',
    primaryDark: '#0c2461',
    white: '#FFFFFF',
    offWhite: '#FCFAFF',
    black: '#000000',
    offBlack: '#333333',
    grey: '#F3F3F3',
  },
};

```

Above are the default values for the theme, which you can change depending on your project.

For example, here is how I might change the theme colours from shades of purple, to a refreshing green:

```
import baseTheme from '@littleplusbig/gatsby-theme-faqs-prismic/src/gatsby-plugin-theme-ui';

export default {
  ...baseTheme,
  colors: {
    ...baseTheme.colors,
    primary: '#8BC34A',
    primaryLight: '#CDDC39',
    primaryDark: '#4CAF50',
  },
};

```

[![Image 9: An example of a theme color change](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup-color-change.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup-color-change.jpg)

The complete set of customisable theme values can be explored in [gatsby-theme-faqs-prismic/src/styles/theme.js](https://github.com/littleplusbig/gatsby-theme-faqs-prismic/blob/master/src/styles/theme.js)

More information about `gatsby-plugin-theme-ui` [here](https://www.npmjs.com/package/gatsby-plugin-theme-ui).

### Components

[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#components)

The components that make up the Frequently Asked Questions pages can be some what customised too. This can be done through concept new to Gatsby Themes called '[Component Shadowing](https://www.gatsbyjs.org/blog/2019-04-29-component-shadowing/)'.

If you wish to override a component, in the `src` directory of your project, create the following directory structure: `@littleplusbig/gatsby-theme-faqs-prismic/components`.

There are several components that a Frequently Asked Questions page, they can all be viewed here: [gatsby-theme-faqs-prismic/src/components](https://github.com/littleplusbig/gatsby-theme-faqs-prismic/tree/master/src/components)

An example of how these components might be customised is adding your project's `<Header />` and `<Footer />` components to the layout.

In order to do this I create a shadowing `layout.js` in the directory we've just created (`your-gatsby-project/src/@littleplusbig/gatsby-theme-faqs-prismic/components/layout.js`):

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

## Metadata

```json
{
  "title": "GitHub - AllanPooley/gatsby-theme-faqs-prismic: A pretty FAQ page for Gatsby projects, out of the box 🌻❓🙋",
  "description": "A pretty FAQ page for Gatsby projects, out of the box 🌻❓🙋 - AllanPooley/gatsby-theme-faqs-prismic",
  "url": "https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true",
  "content": "[![Image 8: Mockups of gatsby-theme-faqs-prismic in action](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup.jpg)\n\nGatsby Theme FAQs Prismic\n-------------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#gatsby-theme-faqs-prismic)\n\n*   [Gatsby Theme](https://www.gatsbyjs.org/docs/themes/what-are-gatsby-themes/) for adding a pretty FAQ page for Gatsby projects, out of the box 🌻🙋\n*   Responsive across Mobiles 📱, Tablets 💊 and Desktops 🖥️\n*   Customisable to your brand using [Theme UI](https://theme-ui.com/) 🎨\n*   Builds FAQ page(s) sourced from content in [Prismic](https://prismic.io/)\n*   Demo at [https://gatsby-theme-faqs.netlify.com/](https://gatsby-theme-faqs.netlify.com/)\n\nWhy?\n----\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#why)\n\nThe Frequently Asked Questions (FAQ) is a common place page on most website. Though, it doesn't exactly summon the creative juices, it's a pretty basic page, [much like legal pages](https://github.com/littleplusbig/gatsby-theme-legals-prismic).\n\nThe idea of `gatsby-theme-faqs-prismic` is do it once well - a super neat, clean and responsive implementation. It's reusable, theme-able and customisable 🎉\n\nInstallation\n------------\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#installation)\n\n```\nyarn add @littleplusbig/gatsby-theme-faqs-prismic\n```\n\nConfiguration\n-------------\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#configuration)\n\nIn your `gatsby-config.js`, under `plugins` add:\n\n```\n{\n  resolve: \"gatsby-theme-faqs-prismic\",\n  options: {\n    prismicRepositoryName: PRISMIC_REPO_NAME,\n    prismicAccessToken: PRISMIC_API_KEY,\n    siteName: YOUR_SITE_NAME, // (Optional)\n    homePath: HOME_PATH // (Optional) Defaults to '/'\n  },\n},\n```\n\nReplacing `PRISMIC_REPO_NAME`, `PRISMIC_API_KEY`, `YOUR_SITE_NAME` and `HOME_PATH` with their respective values.\n\nPrismic Configuration\n---------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#prismic-configuration)\n\n1.  Create a new custom type in your Prismic repository.\n2.  Make sure that it is repeatable and name it `Question Category`.\n3.  Using the JSON Editor paste in the following content structure:\n\n```\n{\n  \"Main\" : {\n    \"category_name\" : {\n      \"type\" : \"StructuredText\",\n      \"config\" : {\n        \"single\" : \"heading1\",\n        \"label\" : \"Category Name\",\n        \"placeholder\" : \"Category Name\"\n      }\n    },\n    \"uid\" : {\n      \"type\" : \"UID\",\n      \"config\" : {\n        \"label\" : \"Category Slug\",\n        \"placeholder\" : \"category-slug\"\n      }\n    }\n  }\n}\n```\n\n4.  Create one or more `Question Category` Content pages.\n    \n5.  Next, create another custom type in your Prismic repository, singular or repeatable depending on your needs, and name it `Frequently Asked Questions`.\n    \n6.  Using the JSON Editor paste in the following content structure:\n    \n\n```\n{\n  \"Main\": {\n    \"page_name\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"heading1\",\n        \"label\": \"Page Name\",\n        \"placeholder\": \"Enter page name\"\n      }\n    },\n    \"uid\": {\n      \"type\": \"UID\",\n      \"config\": {\n        \"label\": \"Slug\",\n        \"placeholder\": \"Enter slug\"\n      }\n    },\n    \"hero_subtitle\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"paragraph\",\n        \"label\": \"Hero Subtitle\",\n        \"placeholder\": \"You have questions, we have answers\"\n      }\n    },\n    \"questions\": {\n      \"type\": \"Group\",\n      \"config\": {\n        \"fields\": {\n          \"question\": {\n            \"type\": \"StructuredText\",\n            \"config\": {\n              \"single\": \"heading2\",\n              \"label\": \"Question\",\n              \"placeholder\": \"How safe is the journey?\"\n            }\n          },\n          \"answer\": {\n            \"type\": \"StructuredText\",\n            \"config\": {\n              \"multi\": \"paragraph, heading3, heading4, heading5, heading6, strong, em, hyperlink, image, embed, list-item, o-list-item, o-list-item\",\n              \"allowTargetBlank\": true,\n              \"label\": \"Answer\",\n              \"placeholder\": \"The trip to Mars cannot be called risk free. Like any venture...\"\n            }\n          },\n          \"category\": {\n            \"type\": \"Link\",\n            \"config\": {\n              \"select\": \"document\",\n              \"customtypes\": [\n                \"question_category\"\n              ],\n              \"label\": \"Category\"\n            }\n          }\n        },\n        \"label\": \"Questions\"\n      }\n    }\n  },\n  \"SEO\": {\n    \"meta_title\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"heading1\",\n        \"label\": \"Meta Title\",\n        \"placeholder\": \"Enter meta title\"\n      }\n    },\n    \"meta_description\": {\n      \"type\": \"StructuredText\",\n      \"config\": {\n        \"single\": \"paragraph\",\n        \"label\": \"Meta Description\",\n        \"placeholder\": \"Enter meta description\"\n      }\n    },\n    \"open_graph_image\": {\n      \"type\": \"Image\",\n      \"config\": {\n        \"constraint\": {\n          \"width\": 1200,\n          \"height\": 630\n        },\n        \"thumbnails\": [],\n        \"label\": \"Open Graph Image\"\n      }\n    }\n  }\n}\n```\n\n7.  Create a `Frequently Asked Question` content page.\n\nOverriding the Theme\n--------------------\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#overriding-the-theme)\n\n### Colors and Styles\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#colors-and-styles)\n\nThis project uses [theme-ui](https://theme-ui.com/), allowing some of the styling to be customised to your project's brand.\n\nIn order to override the styles, in the `src` directory of your project, add a folder titled `gatsby-plugin-theme-ui`, and within that folder a file named `index.js`.\n\nInside of this file (`your-gatsby-project/src/gatsby-plugin-theme-ui/index.js`) add the following:\n\n```\nimport baseTheme from '@littleplusbig/gatsby-theme-faqs-prismic/src/gatsby-plugin-theme-ui';\n\nexport default {\n  ...baseTheme,\n  fonts: {\n    ...baseTheme.fonts,\n    body: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',\n    heading: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',\n  },\n  colors: {\n    ...baseTheme.colors,\n    text: '#333333',\n    background: '#FFFFFF',\n    primary: '#1e3799',\n    primaryLight: '#4a69bd',\n    primaryDark: '#0c2461',\n    white: '#FFFFFF',\n    offWhite: '#FCFAFF',\n    black: '#000000',\n    offBlack: '#333333',\n    grey: '#F3F3F3',\n  },\n};\n\n```\n\nAbove are the default values for the theme, which you can change depending on your project.\n\nFor example, here is how I might change the theme colours from shades of purple, to a refreshing green:\n\n```\nimport baseTheme from '@littleplusbig/gatsby-theme-faqs-prismic/src/gatsby-plugin-theme-ui';\n\nexport default {\n  ...baseTheme,\n  colors: {\n    ...baseTheme.colors,\n    primary: '#8BC34A',\n    primaryLight: '#CDDC39',\n    primaryDark: '#4CAF50',\n  },\n};\n\n```\n\n[![Image 9: An example of a theme color change](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup-color-change.jpg)](https://raw.githubusercontent.com/AllanPooley/gatsby-theme-faqs-demo/master/src/assets/images/gatsby-theme-faqs-prismic-mockup-color-change.jpg)\n\nThe complete set of customisable theme values can be explored in [gatsby-theme-faqs-prismic/src/styles/theme.js](https://github.com/littleplusbig/gatsby-theme-faqs-prismic/blob/master/src/styles/theme.js)\n\nMore information about `gatsby-plugin-theme-ui` [here](https://www.npmjs.com/package/gatsby-plugin-theme-ui).\n\n### Components\n\n[](https://github.com/AllanPooley/gatsby-theme-faqs-prismic?screenshot=true#components)\n\nThe components that make up the Frequently Asked Questions pages can be some what customised too. This can be done through concept new to Gatsby Themes called '[Component Shadowing](https://www.gatsbyjs.org/blog/2019-04-29-component-shadowing/)'.\n\nIf you wish to override a component, in the `src` directory of your project, create the following directory structure: `@littleplusbig/gatsby-theme-faqs-prismic/components`.\n\nThere are several components that a Frequently Asked Questions page, they can all be viewed here: [gatsby-theme-faqs-prismic/src/components](https://github.com/littleplusbig/gatsby-theme-faqs-prismic/tree/master/src/components)\n\nAn example of how these components might be customised is adding your project's `<Header />` and `<Footer />` components to the layout.\n\nIn order to do this I create a shadowing `layout.js` in the directory we've just created (`your-gatsby-project/src/@littleplusbig/gatsby-theme-faqs-prismic/components/layout.js`):\n\n```\nimport React from 'react';\nimport { Header, Footer } from '../../somewhere-in-your-project'\n\nexport default ({ children }) => (\n  <>\n    <Header />\n    {children}\n    <Footer />\n  </>\n);\n```",
  "usage": {
    "tokens": 2298
  }
}
```
