---
title: GitHub - GatsbyCentral/gatsby-awesome-pagination: An opinionated, more awesome approach to pagination in Gatsby
description: An opinionated, more awesome approach to pagination in Gatsby - GatsbyCentral/gatsby-awesome-pagination
url: https://github.com/GatsbyCentral/gatsby-awesome-pagination
timestamp: 2025-01-20T15:30:53.712Z
domain: github.com
path: GatsbyCentral_gatsby-awesome-pagination
---

# GitHub - GatsbyCentral/gatsby-awesome-pagination: An opinionated, more awesome approach to pagination in Gatsby


An opinionated, more awesome approach to pagination in Gatsby - GatsbyCentral/gatsby-awesome-pagination


## Content

Awesome Pagination for Gatsby
-----------------------------

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#awesome-pagination-for-gatsby)

A sensible approach to pagination for Gatsby sites.

Please post questions on StackOverflow, only bug reports are accepted via GitHub.

Contents
--------

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#contents)

*   [QuickStart](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#quick-start)
*   [Introduction](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#introduction)
*   [Philosophy](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#philosophy)
*   [Notes](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#notes)

Quick start
-----------

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#quick-start)

```
yarn add gatsby-awesome-pagination
```

Open `gatsby-node.js` and import:

import { paginate } from 'gatsby-awesome-pagination';

Then, use `paginate()` like so:

exports.createPages \= ({ actions, graphql }) \=\> {
  const { createPage } \= actions;

  // Fetch your items (blog posts, categories, etc).
  const blogPosts \= doSomeMagic();

  // Create your paginated pages
  paginate({
    createPage, // The Gatsby \`createPage\` function
    items: blogPosts, // An array of objects
    itemsPerPage: 10, // How many items you want per page
    pathPrefix: '/blog', // Creates pages like \`/blog\`, \`/blog/2\`, etc
    component: path.resolve('...'), // Just like \`createPage()\`
  })
}

Now in your page query you can use the pagination context like so:

export const pageQuery \= graphql\`
  query ($skip: Int!, $limit: Int!) {
    allMarkdownRemark(
      sort: { fields: \[frontmatter\_\_\_date\], order: DESC }
      skip: $skip // This was added by the plugin
      limit: $limit // This was added by the plugin
    ) {
      ...
    }
  }
\`

Then inside your component, you can link to next / previous pages, and so on:

const BlogIndex \= (props) \=\> {
  return (
    <div\>
      {data.allMarkdownRemark.edges.map(edge \=\> <PostItem item\={edge.node}/\>)}
      <div\>
        {/\* previousPageLink and nextPageLink were added by the plugin \*/ }
        <Link to\={props.pageContext.previousPagePath}\>Previous</Link\>
        <Link to\={props.pageContext.nextPagePath}\>Next</Link\>
      </div\>
    </div\>
  )
}

For a more detailed example, see [docs/examples.md](https://github.com/GatsbyCentral/gatsby-awesome-pagination/blob/master/docs/examples.md)

Introduction
------------

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#introduction)

Love Gatsby, wanna paginate. Sweet, that's exactly what this package is for.

We differ from other pagination options as follows:

*   Don't abuse `context` to pass data into components
*   Pass only pagination context via `context`
*   Provide helpers for next / previous links

There are 2 types of pagination. You have 80 blog posts and you want to show them 15 at a time on pages like `/blog`, `/blog/2`, `/blog/3`, etc. You do this with `paginate()`. Then on each blog post, you want to link to the previous and next blog posts. You do this with `createPagePerItem()`.

Philosophy
----------

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#philosophy)

Why did we create this plugin? We felt that the other Gatsby pagination plugins were using an approach that goes against the principles of GraphQL. One of the advantages of GraphQL is to be able to decide what data you need right where you use that data. That's how Gatsby works with page queries.

By putting all the data into `context`, the other pagination plugins break this. Now you need to decide what data you require for each page inside `gatsby-node.js` and not inside your page query.

We also felt that there were some helpers missing. Generating links to the next and previous pages.

This plugin aims to make it easy to paginate in Gatsby **properly**. No compromises.

API
---

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#api)

Both `paginate()` and `createPagePerItem()` take a single argument, an object. They share the following keys (\* = required):

*   `createPage`\* - The `createPage` function from `exports.createPages`
*   `component`\* - The value you would pass to `createPage()` as `component` [Gatsby docs here](https://www.gatsbyjs.org/docs/bound-action-creators/#createPage)
*   `items`\* - An array of objects, the items you want to paginate over

### `paginate()`

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#paginate)

In addition to the arguments above, `paginate()` also supports:

*   `itemsPerPage`\* - An integer, how many items should be displayed on each page
*   `itemsPerFirstPage` - An integer, how many items should be displayed on the **first** page
*   `pathPrefix`\* - A (nonempty) string or string returning function, the path (eg `/blog`) to which `/2`, `/3`, etc will be added
*   `context` - A base context object which is extended with the pagination context values

Example:

paginate({
  createPage: boundActionCreators.createPage,
  component: path.resolve('./src/templates/blog-index.js'),
  items: blogPosts,
  itemsPerPage: 15,
  itemsPerFirstPage: 3,
  pathPrefix: '/blog'
})

Each page's `context` automatically receives the following values:

*   `pageNumber` - The page number (starting from 0)
*   `humanPageNumber` - The page number (starting from 1) for human consumption
*   `skip` - The $skip you can use in a GraphQL query
*   `limit` - The $limit you can use in a GraphQL query
*   `numberOfPages` - The total number of pages
*   `previousPagePath` - The path to the previous page or `undefined`
*   `nextPagePath` - The path to the next page or `undefined`

#### pathPrefix()

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#pathprefix)

For more advanced use cases, you can supply a function to `pathPrefix`. This function will receive a single object as its only argument, that object will contain `pageNumber` and `numberOfPages`, both integers.

A simple example implementation could be:

const pathPrefix \= ({ pageNumber, numberOfPages }) \=\>
  pageNumber \=== 0 ? '/blog' : '/blog/page'

This example produces pages like `/blog`, `/blog/page/2`, `/blog/page/3`, etc.

### `createPagePerItem()`

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#createpageperitem)

WARNING: This API is under active development and will probably change. USE WITH CAUTION.

In addition to the arguments above, `createPagePerItem()` also accepts:

*   `itemToPath`\* - A function that takes one object from `items` and returns the `path` for this `item`
*   `itemToId`\* - A function that takes one object from `items` and returns the item's ID

**NOTE**: Both `itemToPath` and `itemToId` also accept a string with the path to the value, for example `node.frontmatter.permalink` or `node.id`.

**NOTE**: If an individual `item` has a property called `context`, and that property is an object, then it's own properties will be added to the page's `context` for that item.

Example:

createPagePerItem({
  createPage: boundActionCreators.createPage,
  component: path.resolve('./src/templates/blog-post.js'),
  items: blogPosts,
  itemToPath: 'node.frontmatter.permalink',
  itemToId: 'node.id'
})

Each page's `context` automatically receives the following values:

*   `previousPagePath` - The path to the previous page or `undefined`
*   `previousItem` - A copy of the previous element from `items`
*   `previousPageId` - The ID of the previous page
*   `nextPagePath` - The path to the next page or `undefined`
*   `nextItem` - A copy of the next element from `items`
*   `nextPageId` - The ID of the next page

Notes
-----

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#notes)

### Flow

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#flow)

This plugin is written using [flow](https://flow.org/). There are some limitations when using flow and [lodash](https://lodash.com/). Specifically [this issue](https://github.com/facebook/flow/issues/34). In many cases we use `$FlowExpectError` and explicitly define the type of something to workaround. A more elegant solution does not currently seem to exist. Any input on improving the typing is greatly appreciated in the plugin's issues.

### Contributors

[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#contributors)

Thanks to the following for their contributions:

*   [https://github.com/Pyrax](https://github.com/Pyrax)
*   [https://github.com/JesseSingleton](https://github.com/JesseSingleton)
*   [https://github.com/silvenon](https://github.com/silvenon)

## Metadata

```json
{
  "title": "GitHub - GatsbyCentral/gatsby-awesome-pagination: An opinionated, more awesome approach to pagination in Gatsby",
  "description": "An opinionated, more awesome approach to pagination in Gatsby - GatsbyCentral/gatsby-awesome-pagination",
  "url": "https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true",
  "content": "Awesome Pagination for Gatsby\n-----------------------------\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#awesome-pagination-for-gatsby)\n\nA sensible approach to pagination for Gatsby sites.\n\nPlease post questions on StackOverflow, only bug reports are accepted via GitHub.\n\nContents\n--------\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#contents)\n\n*   [QuickStart](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#quick-start)\n*   [Introduction](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#introduction)\n*   [Philosophy](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#philosophy)\n*   [Notes](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#notes)\n\nQuick start\n-----------\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#quick-start)\n\n```\nyarn add gatsby-awesome-pagination\n```\n\nOpen `gatsby-node.js` and import:\n\nimport { paginate } from 'gatsby-awesome-pagination';\n\nThen, use `paginate()` like so:\n\nexports.createPages \\= ({ actions, graphql }) \\=\\> {\n  const { createPage } \\= actions;\n\n  // Fetch your items (blog posts, categories, etc).\n  const blogPosts \\= doSomeMagic();\n\n  // Create your paginated pages\n  paginate({\n    createPage, // The Gatsby \\`createPage\\` function\n    items: blogPosts, // An array of objects\n    itemsPerPage: 10, // How many items you want per page\n    pathPrefix: '/blog', // Creates pages like \\`/blog\\`, \\`/blog/2\\`, etc\n    component: path.resolve('...'), // Just like \\`createPage()\\`\n  })\n}\n\nNow in your page query you can use the pagination context like so:\n\nexport const pageQuery \\= graphql\\`\n  query ($skip: Int!, $limit: Int!) {\n    allMarkdownRemark(\n      sort: { fields: \\[frontmatter\\_\\_\\_date\\], order: DESC }\n      skip: $skip // This was added by the plugin\n      limit: $limit // This was added by the plugin\n    ) {\n      ...\n    }\n  }\n\\`\n\nThen inside your component, you can link to next / previous pages, and so on:\n\nconst BlogIndex \\= (props) \\=\\> {\n  return (\n    <div\\>\n      {data.allMarkdownRemark.edges.map(edge \\=\\> <PostItem item\\={edge.node}/\\>)}\n      <div\\>\n        {/\\* previousPageLink and nextPageLink were added by the plugin \\*/ }\n        <Link to\\={props.pageContext.previousPagePath}\\>Previous</Link\\>\n        <Link to\\={props.pageContext.nextPagePath}\\>Next</Link\\>\n      </div\\>\n    </div\\>\n  )\n}\n\nFor a more detailed example, see [docs/examples.md](https://github.com/GatsbyCentral/gatsby-awesome-pagination/blob/master/docs/examples.md)\n\nIntroduction\n------------\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#introduction)\n\nLove Gatsby, wanna paginate. Sweet, that's exactly what this package is for.\n\nWe differ from other pagination options as follows:\n\n*   Don't abuse `context` to pass data into components\n*   Pass only pagination context via `context`\n*   Provide helpers for next / previous links\n\nThere are 2 types of pagination. You have 80 blog posts and you want to show them 15 at a time on pages like `/blog`, `/blog/2`, `/blog/3`, etc. You do this with `paginate()`. Then on each blog post, you want to link to the previous and next blog posts. You do this with `createPagePerItem()`.\n\nPhilosophy\n----------\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#philosophy)\n\nWhy did we create this plugin? We felt that the other Gatsby pagination plugins were using an approach that goes against the principles of GraphQL. One of the advantages of GraphQL is to be able to decide what data you need right where you use that data. That's how Gatsby works with page queries.\n\nBy putting all the data into `context`, the other pagination plugins break this. Now you need to decide what data you require for each page inside `gatsby-node.js` and not inside your page query.\n\nWe also felt that there were some helpers missing. Generating links to the next and previous pages.\n\nThis plugin aims to make it easy to paginate in Gatsby **properly**. No compromises.\n\nAPI\n---\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#api)\n\nBoth `paginate()` and `createPagePerItem()` take a single argument, an object. They share the following keys (\\* = required):\n\n*   `createPage`\\* - The `createPage` function from `exports.createPages`\n*   `component`\\* - The value you would pass to `createPage()` as `component` [Gatsby docs here](https://www.gatsbyjs.org/docs/bound-action-creators/#createPage)\n*   `items`\\* - An array of objects, the items you want to paginate over\n\n### `paginate()`\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#paginate)\n\nIn addition to the arguments above, `paginate()` also supports:\n\n*   `itemsPerPage`\\* - An integer, how many items should be displayed on each page\n*   `itemsPerFirstPage` - An integer, how many items should be displayed on the **first** page\n*   `pathPrefix`\\* - A (nonempty) string or string returning function, the path (eg `/blog`) to which `/2`, `/3`, etc will be added\n*   `context` - A base context object which is extended with the pagination context values\n\nExample:\n\npaginate({\n  createPage: boundActionCreators.createPage,\n  component: path.resolve('./src/templates/blog-index.js'),\n  items: blogPosts,\n  itemsPerPage: 15,\n  itemsPerFirstPage: 3,\n  pathPrefix: '/blog'\n})\n\nEach page's `context` automatically receives the following values:\n\n*   `pageNumber` - The page number (starting from 0)\n*   `humanPageNumber` - The page number (starting from 1) for human consumption\n*   `skip` - The $skip you can use in a GraphQL query\n*   `limit` - The $limit you can use in a GraphQL query\n*   `numberOfPages` - The total number of pages\n*   `previousPagePath` - The path to the previous page or `undefined`\n*   `nextPagePath` - The path to the next page or `undefined`\n\n#### pathPrefix()\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#pathprefix)\n\nFor more advanced use cases, you can supply a function to `pathPrefix`. This function will receive a single object as its only argument, that object will contain `pageNumber` and `numberOfPages`, both integers.\n\nA simple example implementation could be:\n\nconst pathPrefix \\= ({ pageNumber, numberOfPages }) \\=\\>\n  pageNumber \\=== 0 ? '/blog' : '/blog/page'\n\nThis example produces pages like `/blog`, `/blog/page/2`, `/blog/page/3`, etc.\n\n### `createPagePerItem()`\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#createpageperitem)\n\nWARNING: This API is under active development and will probably change. USE WITH CAUTION.\n\nIn addition to the arguments above, `createPagePerItem()` also accepts:\n\n*   `itemToPath`\\* - A function that takes one object from `items` and returns the `path` for this `item`\n*   `itemToId`\\* - A function that takes one object from `items` and returns the item's ID\n\n**NOTE**: Both `itemToPath` and `itemToId` also accept a string with the path to the value, for example `node.frontmatter.permalink` or `node.id`.\n\n**NOTE**: If an individual `item` has a property called `context`, and that property is an object, then it's own properties will be added to the page's `context` for that item.\n\nExample:\n\ncreatePagePerItem({\n  createPage: boundActionCreators.createPage,\n  component: path.resolve('./src/templates/blog-post.js'),\n  items: blogPosts,\n  itemToPath: 'node.frontmatter.permalink',\n  itemToId: 'node.id'\n})\n\nEach page's `context` automatically receives the following values:\n\n*   `previousPagePath` - The path to the previous page or `undefined`\n*   `previousItem` - A copy of the previous element from `items`\n*   `previousPageId` - The ID of the previous page\n*   `nextPagePath` - The path to the next page or `undefined`\n*   `nextItem` - A copy of the next element from `items`\n*   `nextPageId` - The ID of the next page\n\nNotes\n-----\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#notes)\n\n### Flow\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#flow)\n\nThis plugin is written using [flow](https://flow.org/). There are some limitations when using flow and [lodash](https://lodash.com/). Specifically [this issue](https://github.com/facebook/flow/issues/34). In many cases we use `$FlowExpectError` and explicitly define the type of something to workaround. A more elegant solution does not currently seem to exist. Any input on improving the typing is greatly appreciated in the plugin's issues.\n\n### Contributors\n\n[](https://github.com/GatsbyCentral/gatsby-awesome-pagination?screenshot=true#contributors)\n\nThanks to the following for their contributions:\n\n*   [https://github.com/Pyrax](https://github.com/Pyrax)\n*   [https://github.com/JesseSingleton](https://github.com/JesseSingleton)\n*   [https://github.com/silvenon](https://github.com/silvenon)",
  "usage": {
    "tokens": 2149
  }
}
```
