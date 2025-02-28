---
title: GitHub - jlengstorf/gatsby-intermediate
description: Contribute to jlengstorf/gatsby-intermediate development by creating an account on GitHub.
url: https://github.com/jlengstorf/gatsby-intermediate
timestamp: 2025-01-20T15:31:24.618Z
domain: github.com
path: jlengstorf_gatsby-intermediate
---

# GitHub - jlengstorf/gatsby-intermediate


Contribute to jlengstorf/gatsby-intermediate development by creating an account on GitHub.


## Content

Intermediate/Advanced Gatsby
----------------------------

[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#intermediateadvanced-gatsby)

A Frontend Masters workshop.

Setup
-----

[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#setup)

Clone this repo locally:

```
git clone git@github.com:jlengstorf/gatsby-intermediate.git
```

Make sure you’re on the `start` branch:

Part I: Create a Docs Theme
---------------------------

[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-i-create-a-docs-theme)

*   Set up Yarn workspaces
*   Create a site for theme dev
*   Create the `packages/gatsby-theme-docs` folder
    *   `yarn init`
    *   Create `index.js` (`// boop`)
*   Install the docs theme
    *   `yarn workspace negronis add "gatsby-theme-docs@*"` (quotes for Windows)
    *   Add default config to `gatsby-config.js`
*   Make sure the content directory exists (`onPreBootstrap`)
    *   `yarn add mkdirp`
    *   Validate that this works by starting the `theme-dev` site in `develop` mode
*   Define the docs data type (`createSchemaCustomization`)
    *   Show this data type in GraphiQL
    *   Run a query to show it returning an empty array
*   Create docs nodes from MDX files (`onCreateNode`)
    *   Only get the docs, not all MDX files
*   Define a custom resolver to get the MDX `body` content (`createResolvers`)
    *   Write a passthrough resolver (hat tip to @christopherbiscardi for the original work to figure out how these work)
*   Create the required React components to display a docs page
    *   Create a `Layout` component (`src/components/layout.js`)
    *   Create a `DocsPage` component (`src/components/docs-page.js`)
        *   Set up `MDXRenderer`
    *   Create a `DocsPageTemplate` component (`src/templates/docs-page-template.js`)
        *   Write the GraphQL query in GraphiQL first
        *   Use the Code Exporter to get started
*   Create pages from the docs nodes (`createPages`)
    *   Write a GraphQL query in GraphiQL first
*   Add Theme UI
    *   `yarn workspace gatsby-theme-docs add theme-ui gatsby-plugin-theme-ui @emotion/core @mdx-js/react`
    *   Update `gatsby-config.js`
    *   Add a theme file (`src/gatsby-plugin-theme-ui/index.js`)
    *   Update `Layout` to use Theme UI
    *   Update `DocsPage` to use Theme UI
*   Create a `TableOfContents` component (`src/components/table-of-contents.js`)
    *   Write a `useDocs` hook (`src/hooks/use-docs.js`)
*   Add support for syntax highlighted code
    *   `yarn workspace gatsby-theme-docs add mdx-utils prism-react-renderer`
    *   Create a `Code` component (`src/components/code.js`)
    *   Shadow the MDX components in Theme UI to use `Code` (`src/gatsby-plugin-theme-ui/components.js`)
    *   Insert a fenced code block (use `src/components/docs-page.js`) into `docs/index.mdx`
*   Add support for live editing code blocks
    *   `yarn workspace gatsby-theme-docs add react-live`
    *   Add a scope file for easy shadowing
    *   Update `Code` to use `react-live`

Part II: Honkify
----------------

[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-ii-honkify)

*   Install the docs theme
    *   `yarn workspace negronis add "gatsby-theme-docs@*"` (quotes for Windows)
    *   Update `gatsby-config.js` with custom basePath and disable theme MDX
    *   The existing theme from the Honkify site will automatically override the docs Theme UI config
    *   Shadow the `Layout` component
*   Create a `Button` component (`src/components/button.js`)
    *   Shadow the `scope.js` file to add `Button`
    *   Add the `Button` component in a live-editable code block in the docs
    *   Show it interacting with Honkify

Part III: Build a Negroni Fan Site
----------------------------------

[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-iii-build-a-negroni-fan-site)

*   Add Theme UI
    *   `yarn workspace negronis add theme-ui gatsby-plugin-theme-ui @emotion/core @mdx-js/react`
    *   Add a preset (`yarn workspace negronis add @theme-ui/presets`)
    *   Create a theme file (`src/gatsby-plugin-theme-ui/index.js`)
*   Create a `Layout` component (`src/components/layout.js`)
    *   Update `src/pages/index.js` to use the `Layout`
    *   Update `src/pages/history.js` to use the `Layout`
    *   Add styles for a hollow button
*   Add image support
    *   `yarn workspace negronis add gatsby-source-filesystem gatsby-transformer-cloudinary gatsby-image`
    *   Get credentials from Cloudinary
    *   Add env vars to `.env.development`
    *   Load env vars in `gatsby-config.js`
    *   Add plugin config to `gatsby-config.js`
    *   Query for images
        *   Show this in GraphiQL first
    *   Update `src/pages/index.js` to display an image
        *   Quick aside to show transformations with Cloudinary because they’re dope
    *   Update `src/pages/history.js` to display an image
*   Install the docs theme
    *   Recipes are a kind of documentation! :)
    *   `yarn workspace negronis add "gatsby-theme-docs@*"` (quotes for Windows)
    *   Add modified config to `gatsby-config.js`
        *   `basePath: '/recipes'`
        *   `contentPath: 'content/recipes'`
*   Update `src/pages/index.js` to link to `/recipes`
    *   Add styles for a primary button
*   Shadow the `Layout` component in the docs theme
*   Shadow the `TableOfContents` component in the docs theme
*   Install the events theme
    *   `yarn workspace negronis add @jlengstorf/gatsby-theme-events`
    *   This was built as part of this free course on authoring Gatsby themes: [https://egghead.io/courses/gatsby-theme-authoring](https://egghead.io/courses/gatsby-theme-authoring)
    *   Update `gatsby-config.js` with a custom basePath and contentPath
    *   Shadow the `Layout` component in the events theme

Part IV: Rick & Morty Lookup App
--------------------------------

[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-iv-rick--morty-lookup-app)

*   Add support for client-side GraphQL queries
    *   `yarn workspace lookup add gatsby-plugin-apollo @apollo/react-common @apollo/react-hooks graphql-tag`
    *   Update `gatsby-config.js` to use `gatsby-plugin-apollo`
    *   Point Apollo at the Rick & Morty API ([https://rickandmortyapi.com/graphql/](https://rickandmortyapi.com/graphql/))
*   Create pages
    *   `src/pages/index.js`
    *   `src/pages/search.js`
*   Add support for client-only routes
    *   `gatsby-node.js` (`onCreatePage`/`matchPath`)
    *   Add a redirect `netlify.toml`
    *   Test using `netlify dev`
*   Create a search form
    *   React hooks
    *   Programmatic navigation
    *   Add a submit handler
*   Create a results component
    *   Query based on the current search string
*   Figure out the search string from state or URL
    *   `location`

## Metadata

```json
{
  "title": "GitHub - jlengstorf/gatsby-intermediate",
  "description": "Contribute to jlengstorf/gatsby-intermediate development by creating an account on GitHub.",
  "url": "https://github.com/jlengstorf/gatsby-intermediate?screenshot=true",
  "content": "Intermediate/Advanced Gatsby\n----------------------------\n\n[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#intermediateadvanced-gatsby)\n\nA Frontend Masters workshop.\n\nSetup\n-----\n\n[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#setup)\n\nClone this repo locally:\n\n```\ngit clone git@github.com:jlengstorf/gatsby-intermediate.git\n```\n\nMake sure you’re on the `start` branch:\n\nPart I: Create a Docs Theme\n---------------------------\n\n[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-i-create-a-docs-theme)\n\n*   Set up Yarn workspaces\n*   Create a site for theme dev\n*   Create the `packages/gatsby-theme-docs` folder\n    *   `yarn init`\n    *   Create `index.js` (`// boop`)\n*   Install the docs theme\n    *   `yarn workspace negronis add \"gatsby-theme-docs@*\"` (quotes for Windows)\n    *   Add default config to `gatsby-config.js`\n*   Make sure the content directory exists (`onPreBootstrap`)\n    *   `yarn add mkdirp`\n    *   Validate that this works by starting the `theme-dev` site in `develop` mode\n*   Define the docs data type (`createSchemaCustomization`)\n    *   Show this data type in GraphiQL\n    *   Run a query to show it returning an empty array\n*   Create docs nodes from MDX files (`onCreateNode`)\n    *   Only get the docs, not all MDX files\n*   Define a custom resolver to get the MDX `body` content (`createResolvers`)\n    *   Write a passthrough resolver (hat tip to @christopherbiscardi for the original work to figure out how these work)\n*   Create the required React components to display a docs page\n    *   Create a `Layout` component (`src/components/layout.js`)\n    *   Create a `DocsPage` component (`src/components/docs-page.js`)\n        *   Set up `MDXRenderer`\n    *   Create a `DocsPageTemplate` component (`src/templates/docs-page-template.js`)\n        *   Write the GraphQL query in GraphiQL first\n        *   Use the Code Exporter to get started\n*   Create pages from the docs nodes (`createPages`)\n    *   Write a GraphQL query in GraphiQL first\n*   Add Theme UI\n    *   `yarn workspace gatsby-theme-docs add theme-ui gatsby-plugin-theme-ui @emotion/core @mdx-js/react`\n    *   Update `gatsby-config.js`\n    *   Add a theme file (`src/gatsby-plugin-theme-ui/index.js`)\n    *   Update `Layout` to use Theme UI\n    *   Update `DocsPage` to use Theme UI\n*   Create a `TableOfContents` component (`src/components/table-of-contents.js`)\n    *   Write a `useDocs` hook (`src/hooks/use-docs.js`)\n*   Add support for syntax highlighted code\n    *   `yarn workspace gatsby-theme-docs add mdx-utils prism-react-renderer`\n    *   Create a `Code` component (`src/components/code.js`)\n    *   Shadow the MDX components in Theme UI to use `Code` (`src/gatsby-plugin-theme-ui/components.js`)\n    *   Insert a fenced code block (use `src/components/docs-page.js`) into `docs/index.mdx`\n*   Add support for live editing code blocks\n    *   `yarn workspace gatsby-theme-docs add react-live`\n    *   Add a scope file for easy shadowing\n    *   Update `Code` to use `react-live`\n\nPart II: Honkify\n----------------\n\n[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-ii-honkify)\n\n*   Install the docs theme\n    *   `yarn workspace negronis add \"gatsby-theme-docs@*\"` (quotes for Windows)\n    *   Update `gatsby-config.js` with custom basePath and disable theme MDX\n    *   The existing theme from the Honkify site will automatically override the docs Theme UI config\n    *   Shadow the `Layout` component\n*   Create a `Button` component (`src/components/button.js`)\n    *   Shadow the `scope.js` file to add `Button`\n    *   Add the `Button` component in a live-editable code block in the docs\n    *   Show it interacting with Honkify\n\nPart III: Build a Negroni Fan Site\n----------------------------------\n\n[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-iii-build-a-negroni-fan-site)\n\n*   Add Theme UI\n    *   `yarn workspace negronis add theme-ui gatsby-plugin-theme-ui @emotion/core @mdx-js/react`\n    *   Add a preset (`yarn workspace negronis add @theme-ui/presets`)\n    *   Create a theme file (`src/gatsby-plugin-theme-ui/index.js`)\n*   Create a `Layout` component (`src/components/layout.js`)\n    *   Update `src/pages/index.js` to use the `Layout`\n    *   Update `src/pages/history.js` to use the `Layout`\n    *   Add styles for a hollow button\n*   Add image support\n    *   `yarn workspace negronis add gatsby-source-filesystem gatsby-transformer-cloudinary gatsby-image`\n    *   Get credentials from Cloudinary\n    *   Add env vars to `.env.development`\n    *   Load env vars in `gatsby-config.js`\n    *   Add plugin config to `gatsby-config.js`\n    *   Query for images\n        *   Show this in GraphiQL first\n    *   Update `src/pages/index.js` to display an image\n        *   Quick aside to show transformations with Cloudinary because they’re dope\n    *   Update `src/pages/history.js` to display an image\n*   Install the docs theme\n    *   Recipes are a kind of documentation! :)\n    *   `yarn workspace negronis add \"gatsby-theme-docs@*\"` (quotes for Windows)\n    *   Add modified config to `gatsby-config.js`\n        *   `basePath: '/recipes'`\n        *   `contentPath: 'content/recipes'`\n*   Update `src/pages/index.js` to link to `/recipes`\n    *   Add styles for a primary button\n*   Shadow the `Layout` component in the docs theme\n*   Shadow the `TableOfContents` component in the docs theme\n*   Install the events theme\n    *   `yarn workspace negronis add @jlengstorf/gatsby-theme-events`\n    *   This was built as part of this free course on authoring Gatsby themes: [https://egghead.io/courses/gatsby-theme-authoring](https://egghead.io/courses/gatsby-theme-authoring)\n    *   Update `gatsby-config.js` with a custom basePath and contentPath\n    *   Shadow the `Layout` component in the events theme\n\nPart IV: Rick & Morty Lookup App\n--------------------------------\n\n[](https://github.com/jlengstorf/gatsby-intermediate?screenshot=true#part-iv-rick--morty-lookup-app)\n\n*   Add support for client-side GraphQL queries\n    *   `yarn workspace lookup add gatsby-plugin-apollo @apollo/react-common @apollo/react-hooks graphql-tag`\n    *   Update `gatsby-config.js` to use `gatsby-plugin-apollo`\n    *   Point Apollo at the Rick & Morty API ([https://rickandmortyapi.com/graphql/](https://rickandmortyapi.com/graphql/))\n*   Create pages\n    *   `src/pages/index.js`\n    *   `src/pages/search.js`\n*   Add support for client-only routes\n    *   `gatsby-node.js` (`onCreatePage`/`matchPath`)\n    *   Add a redirect `netlify.toml`\n    *   Test using `netlify dev`\n*   Create a search form\n    *   React hooks\n    *   Programmatic navigation\n    *   Add a submit handler\n*   Create a results component\n    *   Query based on the current search string\n*   Figure out the search string from state or URL\n    *   `location`",
  "usage": {
    "tokens": 1770
  }
}
```
