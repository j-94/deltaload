---
title: GitHub - bagseye/barcadia
description: Contribute to bagseye/barcadia development by creating an account on GitHub.
url: https://github.com/bagseye/barcadia
timestamp: 2025-01-20T15:31:41.069Z
domain: github.com
path: bagseye_barcadia
---

# GitHub - bagseye/barcadia


Contribute to bagseye/barcadia development by creating an account on GitHub.


## Content

THIS REPO IS NO LONGER MAINTAINED
---------------------------------

[](https://github.com/bagseye/barcadia?screenshot=true#--this-repo-is-no-longer-maintained)

Barcadia V2 Starter
-------------------

[](https://github.com/bagseye/barcadia?screenshot=true#--barcadia-v2-starter)

[Version 2 Release Notes](https://www.morganbaker.dev/journal/barcadia-v2-release-notes)

Barcadia is a GatsbyJS starter theme that uses Contentful for content management. It includes the main configuration files found in Gatsby.

Getting started
---------------

[](https://github.com/bagseye/barcadia?screenshot=true#getting-started)

1.  **Create a Gatsby site.**
    
    Use the Gatsby CLI to create a new site, specifying the Barcadia starter.
    
    # create a new Gatsby site using the barcadia starter
    gatsby new my-barcadia-starter https://github.com/bagseye/barcadia
    
2.  **Before running Gatsby Develop**
    
    You'll need to setup a free account with Contentful [Here](https://www.contentful.com/) and create a space ID and access token for your new site.
    
    Once these are generated create a new file in the site root called `.env.development` and populate it with the following information:
    
    ```
    CONTENTFUL_SPACE_ID={YOUR SPACE ID}
    CONTENTFUL_ACCESS_TOKEN={YOUR ACCESS TOKEN}
    ```
    
    **NOTE** - Ensure this file has been added to your `.gitignore` to prevent it from being tracked
    
3.  **Start developing.**
    
    Navigate into your new site’s directory and start it up.
    
    cd my-barcadia-starter/
    gatsby develop
    
4.  **Import Content-model.json on Contentful** Make a Json file(e.g. example-config.json) with the following content.
    
    ```
    {
      "spaceId": "SPACE_ID",
      "managementToken": "Generate a management token from the APIs Tab on contentful dashboard",
      "contentFile": "content-model.json"
     }
    ```
    
    Important Note: you need contentful globally installed(`npm i -g contentful-cli`) before the next step Then Run this Command from your terminal: `contentful space import --config example-config.json`
    
5.  **Open your site**
    
    Your site is now running at `http://localhost:8000`!
    
    _Note: You'll also see a second link: _`http://localhost:8000/___graphql`_. This is a tool you can use to experiment with querying your data. Learn more about using this tool in the [Gatsby tutorial](https://www.gatsbyjs.org/tutorial/part-five/#introducing-graphiql)._
    
    Open the `my-barcadia-starter` directory in your code editor of choice and edit `src/pages/index.js`. Save your changes and the browser will update in real time!
    
6.  **Build your site**
    
    When you are ready to build your production site, you will need to create a `.env.production` file that will contain the `CONTENTFUL_SPACE_ID` and `CONTENTFUL_ACCESS_TOKEN` environment variables. After that is set up, you can run `npm run build` or `gatsby build` and Gatsby will build your site.
    

CMS Content Model
-----------------

[](https://github.com/bagseye/barcadia?screenshot=true#cms-content-model)

```
Follow the steps for importing data with Contentful [Here](https://www.contentful.com/developers/docs/tutorials/cli/import-and-export) using the example file `content-model.json`, found in the site root.
```

🧐 What's inside?
-----------------

[](https://github.com/bagseye/barcadia?screenshot=true#-whats-inside)

A quick look at the top-level files and directories . ├── node\_modules ├── src ├── .gitignore ├── .prettierignore ├── .prettierrc ├── content-model.json ├── gatsby-config.js ├── gatsby-node.js ├── LICENSE ├── package-lock.json ├── package.json └── README.md

1.  **`/node_modules`**: This directory contains all of the modules of code that your project depends on (npm packages) are automatically installed.
    
2.  **`/src`**: This directory will contain all of the code related to what you will see on the front-end of your site (what you see in the browser) such as your site header or a page template. `src` is a convention for “source code”.
    
3.  **`.gitignore`**: This file tells git which files it should not track / not maintain a version history for.
    
4.  **`.prettierrc`**: This is a configuration file for [Prettier](https://prettier.io/). Prettier is a tool to help keep the formatting of your code consistent.
    
5.  **`gatsby-browser.js`**: This file is where Gatsby expects to find any usage of the [Gatsby browser APIs](https://www.gatsbyjs.org/docs/browser-apis/) (if any). These allow customization/extension of default Gatsby settings affecting the browser.
    
6.  **`gatsby-config.js`**: This is the main configuration file for a Gatsby site. This is where you can specify information about your site (metadata) like the site title and description, which Gatsby plugins you’d like to include, etc. (Check out the [config docs](https://www.gatsbyjs.org/docs/gatsby-config/) for more detail).
    
7.  **`gatsby-node.js`**: This file is where Gatsby expects to find any usage of the [Gatsby Node APIs](https://www.gatsbyjs.org/docs/node-apis/) (if any). These allow customization/extension of default Gatsby settings affecting pieces of the site build process.
    
8.  **`gatsby-ssr.js`**: This file is where Gatsby expects to find any usage of the [Gatsby server-side rendering APIs](https://www.gatsbyjs.org/docs/ssr-apis/) (if any). These allow customization of default Gatsby settings affecting server-side rendering.
    
9.  **`LICENSE`**: Gatsby is licensed under the MIT license.
    
10.  **`package-lock.json`** (See `package.json` below, first). This is an automatically generated file based on the exact versions of your npm dependencies that were installed for your project. **(You won’t change this file directly).**
    
11.  **`package.json`**: A manifest file for Node.js projects, which includes things like metadata (the project’s name, author, etc). This manifest is how npm knows which packages to install for your project.
    
12.  **`README.md`**: A text file containing useful reference information about your project.
    

🎓 Learning Gatsby
------------------

[](https://github.com/bagseye/barcadia?screenshot=true#-learning-gatsby)

Looking for more guidance? Full documentation for Gatsby lives [on the website](https://www.gatsbyjs.org/). Here are some places to start:

*   **For most developers, we recommend starting with our [in-depth tutorial for creating a site with Gatsby](https://www.gatsbyjs.org/tutorial/).** It starts with zero assumptions about your level of ability and walks through every step of the process.
    
*   **To dive straight into code samples, head [to our documentation](https://www.gatsbyjs.org/docs/).** In particular, check out the _Guides_, _API Reference_, and _Advanced Tutorials_ sections in the sidebar.
    

#### Photo Credits

[](https://github.com/bagseye/barcadia?screenshot=true#photo-credits)

[Ales Nesetril](https://unsplash.com/@alesnesetril) [Josh Rose](https://unsplash.com/@joshsrose) [Cat Han](https://unsplash.com/@figmentprints) [Martin Sanchez](https://unsplash.com/@martinsanchez) [Onur Binay](https://unsplash.com/@onurbinay) [Torsten Dettlaff](https://www.pexels.com/@tdcat) [Nick Demou](https://www.pexels.com/@nick-demou-365778) [Little John](https://unsplash.com/@joao_freire)

## Metadata

```json
{
  "title": "GitHub - bagseye/barcadia",
  "description": "Contribute to bagseye/barcadia development by creating an account on GitHub.",
  "url": "https://github.com/bagseye/barcadia?screenshot=true",
  "content": "THIS REPO IS NO LONGER MAINTAINED\n---------------------------------\n\n[](https://github.com/bagseye/barcadia?screenshot=true#--this-repo-is-no-longer-maintained)\n\nBarcadia V2 Starter\n-------------------\n\n[](https://github.com/bagseye/barcadia?screenshot=true#--barcadia-v2-starter)\n\n[Version 2 Release Notes](https://www.morganbaker.dev/journal/barcadia-v2-release-notes)\n\nBarcadia is a GatsbyJS starter theme that uses Contentful for content management. It includes the main configuration files found in Gatsby.\n\nGetting started\n---------------\n\n[](https://github.com/bagseye/barcadia?screenshot=true#getting-started)\n\n1.  **Create a Gatsby site.**\n    \n    Use the Gatsby CLI to create a new site, specifying the Barcadia starter.\n    \n    # create a new Gatsby site using the barcadia starter\n    gatsby new my-barcadia-starter https://github.com/bagseye/barcadia\n    \n2.  **Before running Gatsby Develop**\n    \n    You'll need to setup a free account with Contentful [Here](https://www.contentful.com/) and create a space ID and access token for your new site.\n    \n    Once these are generated create a new file in the site root called `.env.development` and populate it with the following information:\n    \n    ```\n    CONTENTFUL_SPACE_ID={YOUR SPACE ID}\n    CONTENTFUL_ACCESS_TOKEN={YOUR ACCESS TOKEN}\n    ```\n    \n    **NOTE** - Ensure this file has been added to your `.gitignore` to prevent it from being tracked\n    \n3.  **Start developing.**\n    \n    Navigate into your new site’s directory and start it up.\n    \n    cd my-barcadia-starter/\n    gatsby develop\n    \n4.  **Import Content-model.json on Contentful** Make a Json file(e.g. example-config.json) with the following content.\n    \n    ```\n    {\n      \"spaceId\": \"SPACE_ID\",\n      \"managementToken\": \"Generate a management token from the APIs Tab on contentful dashboard\",\n      \"contentFile\": \"content-model.json\"\n     }\n    ```\n    \n    Important Note: you need contentful globally installed(`npm i -g contentful-cli`) before the next step Then Run this Command from your terminal: `contentful space import --config example-config.json`\n    \n5.  **Open your site**\n    \n    Your site is now running at `http://localhost:8000`!\n    \n    _Note: You'll also see a second link: _`http://localhost:8000/___graphql`_. This is a tool you can use to experiment with querying your data. Learn more about using this tool in the [Gatsby tutorial](https://www.gatsbyjs.org/tutorial/part-five/#introducing-graphiql)._\n    \n    Open the `my-barcadia-starter` directory in your code editor of choice and edit `src/pages/index.js`. Save your changes and the browser will update in real time!\n    \n6.  **Build your site**\n    \n    When you are ready to build your production site, you will need to create a `.env.production` file that will contain the `CONTENTFUL_SPACE_ID` and `CONTENTFUL_ACCESS_TOKEN` environment variables. After that is set up, you can run `npm run build` or `gatsby build` and Gatsby will build your site.\n    \n\nCMS Content Model\n-----------------\n\n[](https://github.com/bagseye/barcadia?screenshot=true#cms-content-model)\n\n```\nFollow the steps for importing data with Contentful [Here](https://www.contentful.com/developers/docs/tutorials/cli/import-and-export) using the example file `content-model.json`, found in the site root.\n```\n\n🧐 What's inside?\n-----------------\n\n[](https://github.com/bagseye/barcadia?screenshot=true#-whats-inside)\n\nA quick look at the top-level files and directories . ├── node\\_modules ├── src ├── .gitignore ├── .prettierignore ├── .prettierrc ├── content-model.json ├── gatsby-config.js ├── gatsby-node.js ├── LICENSE ├── package-lock.json ├── package.json └── README.md\n\n1.  **`/node_modules`**: This directory contains all of the modules of code that your project depends on (npm packages) are automatically installed.\n    \n2.  **`/src`**: This directory will contain all of the code related to what you will see on the front-end of your site (what you see in the browser) such as your site header or a page template. `src` is a convention for “source code”.\n    \n3.  **`.gitignore`**: This file tells git which files it should not track / not maintain a version history for.\n    \n4.  **`.prettierrc`**: This is a configuration file for [Prettier](https://prettier.io/). Prettier is a tool to help keep the formatting of your code consistent.\n    \n5.  **`gatsby-browser.js`**: This file is where Gatsby expects to find any usage of the [Gatsby browser APIs](https://www.gatsbyjs.org/docs/browser-apis/) (if any). These allow customization/extension of default Gatsby settings affecting the browser.\n    \n6.  **`gatsby-config.js`**: This is the main configuration file for a Gatsby site. This is where you can specify information about your site (metadata) like the site title and description, which Gatsby plugins you’d like to include, etc. (Check out the [config docs](https://www.gatsbyjs.org/docs/gatsby-config/) for more detail).\n    \n7.  **`gatsby-node.js`**: This file is where Gatsby expects to find any usage of the [Gatsby Node APIs](https://www.gatsbyjs.org/docs/node-apis/) (if any). These allow customization/extension of default Gatsby settings affecting pieces of the site build process.\n    \n8.  **`gatsby-ssr.js`**: This file is where Gatsby expects to find any usage of the [Gatsby server-side rendering APIs](https://www.gatsbyjs.org/docs/ssr-apis/) (if any). These allow customization of default Gatsby settings affecting server-side rendering.\n    \n9.  **`LICENSE`**: Gatsby is licensed under the MIT license.\n    \n10.  **`package-lock.json`** (See `package.json` below, first). This is an automatically generated file based on the exact versions of your npm dependencies that were installed for your project. **(You won’t change this file directly).**\n    \n11.  **`package.json`**: A manifest file for Node.js projects, which includes things like metadata (the project’s name, author, etc). This manifest is how npm knows which packages to install for your project.\n    \n12.  **`README.md`**: A text file containing useful reference information about your project.\n    \n\n🎓 Learning Gatsby\n------------------\n\n[](https://github.com/bagseye/barcadia?screenshot=true#-learning-gatsby)\n\nLooking for more guidance? Full documentation for Gatsby lives [on the website](https://www.gatsbyjs.org/). Here are some places to start:\n\n*   **For most developers, we recommend starting with our [in-depth tutorial for creating a site with Gatsby](https://www.gatsbyjs.org/tutorial/).** It starts with zero assumptions about your level of ability and walks through every step of the process.\n    \n*   **To dive straight into code samples, head [to our documentation](https://www.gatsbyjs.org/docs/).** In particular, check out the _Guides_, _API Reference_, and _Advanced Tutorials_ sections in the sidebar.\n    \n\n#### Photo Credits\n\n[](https://github.com/bagseye/barcadia?screenshot=true#photo-credits)\n\n[Ales Nesetril](https://unsplash.com/@alesnesetril) [Josh Rose](https://unsplash.com/@joshsrose) [Cat Han](https://unsplash.com/@figmentprints) [Martin Sanchez](https://unsplash.com/@martinsanchez) [Onur Binay](https://unsplash.com/@onurbinay) [Torsten Dettlaff](https://www.pexels.com/@tdcat) [Nick Demou](https://www.pexels.com/@nick-demou-365778) [Little John](https://unsplash.com/@joao_freire)",
  "usage": {
    "tokens": 1783
  }
}
```
