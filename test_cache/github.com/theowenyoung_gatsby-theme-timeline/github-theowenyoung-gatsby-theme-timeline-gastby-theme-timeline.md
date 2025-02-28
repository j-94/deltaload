---
title: GitHub - theowenyoung/gatsby-theme-timeline: Gastby theme timeline
description: Gastby theme timeline. Contribute to theowenyoung/gatsby-theme-timeline development by creating an account on GitHub.
url: https://github.com/theowenyoung/gatsby-theme-timeline
timestamp: 2025-01-20T15:32:07.833Z
domain: github.com
path: theowenyoung_gatsby-theme-timeline
---

# GitHub - theowenyoung/gatsby-theme-timeline: Gastby theme timeline


Gastby theme timeline. Contribute to theowenyoung/gatsby-theme-timeline development by creating an account on GitHub.


## Content

Gatsby Theme Timeline
---------------------

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#gatsby-theme-timeline)

This is a repo for Gatsby's timeline theme, with the theme, you can show all your posts, tweets, instagram medias, youtube videos, hacker news, reddit post at one.

[Live Demo](https://gatsby-theme-timeline.owenyoung.com/)

[![Image 5: Screen](https://camo.githubusercontent.com/a5d4d44d5f4a05ee4b41c2911491b245d02281fb0dd00dfa55958fa70ae35d9e/68747470733a2f2f692e696d6775722e636f6d2f367949544934452e706e67)](https://camo.githubusercontent.com/a5d4d44d5f4a05ee4b41c2911491b245d02281fb0dd00dfa55958fa70ae35d9e/68747470733a2f2f692e696d6775722e636f6d2f367949544934452e706e67)

Features
--------

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#features)

*   Support Mdx, tweet, instagram medias, youtube videos, hacker news, reddit post
*   Support i18n by [gatsby-theme-i18n](https://www.gatsbyjs.com/plugins/gatsby-theme-i18n/), you can choose your own [i18n library](https://github.com/gatsbyjs/themes/tree/master/packages)
*   Support comments [disqus](https://disqus.com/) or [utterances](https://utteranc.es/)
*   Support Tags
*   Pagination, even tag page supports pagination
*   SEO Optimization

🚀 Quick start
--------------

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#-quick-start)

> Learn more about the theme information at [here](https://github.com/theowenyoung/gatsby-theme-timeline/tree/main/packages/gatsby-theme-timeline#readme)

1.  **Create a Gatsby site.**
    
    Use the Gatsby CLI to create a new site, specifying the timeline blog theme starter.
    
    # create a new Gatsby site using the timeline blog theme starter
    gatsby new my-themed-blog https://github.com/theowenyoung/gatsby-starter-timeline
    
2.  **Create twitter credentials**
    
    Optional, if you want to add your tweets to blog, create `.env` with the following content:
    
    TWITTER\_CONSUMER\_KEY\=xx
    TWITTER\_CONSUMER\_SECRET\=xx
    TWITTER\_ACCESS\_TOKEN\=xx
    TWITTER\_ACCESS\_SECRET\=xx
    
    Then, uncomment `gatsby-config.js` plugin `gatsby-source-twitter`
    
3.  **Create instagram credentials**
    
    Optional, if you want to add your instagram to blog, create `.env` with the following content:
    
    INSTAGRAM\_ACCESS\_TOKEN\=xx
    
    > See [How to get instagram access token](https://github.com/nbcommunication/InstagramBasicDisplayApi#creating-a-facebook-app)
    
    > Then, uncomment `gatsby-config.js` plugin `gatsby-source-instagram`
    
4.  **Start developing.**
    
    Navigate into your new site’s directory and start it up.
    
    cd my-themed-blog/
    gatsby develop
    
5.  **Open the code and start customizing!**
    
    Your site is now running at `http://localhost:8000`!
    

For exist site or more params, see [here](https://github.com/theowenyoung/gatsby-theme-timeline/tree/main/packages/gatsby-theme-timeline#readme)

First using Gatsby? check out the guide to [using the Gatsby blog theme starter](https://gatsbyjs.com/docs/themes/using-a-gatsby-theme), or the longer, [more detailed tutorial](https://gatsbyjs.com/tutorial/using-a-theme).

🧐 What's inside?
-----------------

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#-whats-inside)

Here are the top-level files and directories you'll see in a site created using the timeline blog theme starter:

```
gatsby-starter-timeline
├── content
│   ├── assets
│   │   └── avatar.png
│   └── posts
│       ├── hello-world.mdx
│       └── my-second-post.mdx
├── data
│   ├── tweets
│       ├── 1111.json
│       └── 2222.json
│   ├── reddit
│       ├── 1111.json
│       └── 2222.json
├── src
│   └── gatsby-theme-timeline
│       ├── components
│       │   └── bio-content.js
│       └── gatsby-theme-ui
│           └── colors.js
├── .gitignore
├── .prettierrc
├── gatsby-config.js
├── LICENSE
├── package-lock.json
├── package.json
└── README.md
```

1.  **`/content`**: A content folder holding assets that the theme expects to exist. This will vary from theme to theme -- this starter is set up to get you started with the timeline blog theme, which expects an image asset for your avatar, and blog post content. Replace the avatar image file, delete the demo posts, and add your own!
    
2.  **`/data`**: A raw data folder holding raw data like tweets, reddit json.
    
3.  **`/src`**: You will probably want to customize your site to personalize it. The files under `/src/gatsby-theme-blog` _shadow_, or override, the files of the same name in the `gatsby-theme-blog` package. To learn more about this, check out the [guide to getting started with using the timeline blog theme starter](https://gatsbyjs.com/docs/themes/using-a-gatsby-theme).
    
4.  **`.gitignore`**: This file tells git which files it should not track / not maintain a version history for.
    
5.  **`.prettierrc`**: This file tells [Prettier](https://prettier.io/) which configuration it should use to lint files.
    
6.  **`gatsby-config.js`**: This is the main configuration file for a Gatsby site. This is where you can specify information about your site (metadata) like the site title and description, which Gatsby plugins you’d like to include, etc. When using themes, it's where you'll include the theme plugin, and any customization options the theme provides.
    
7.  **`LICENSE`**: This Gatsby starter is licensed under the 0BSD license. This means that you can see this file as a placeholder and replace it with your own license.
    
8.  **`package-lock.json`** (See `package.json` below, first). This is an automatically generated file based on the exact versions of your npm dependencies that were installed for your project. **(You won’t change this file directly).**
    
9.  **`package.json`**: A manifest file for Node.js projects, which includes things like metadata (the project’s name, author, etc). This manifest is how npm knows which packages to install for your project.
    
10.  **`README.md`**: A text file containing useful reference information about your project.
    

Use Case
--------

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#use-case)

*   [Owen Young's Story](https://blog.owenyoung.com/)
*   [Buzzing on stocks](https://stocks.buzzing.cc/)

Full Screen
-----------

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#full-screen)

[![Image 6: Full](https://camo.githubusercontent.com/263059e57c8960092b1d18dc3d85a04d5a70c36830824906211362f4215faf39/68747470733a2f2f692e696d6775722e636f6d2f7244664a7572792e6a7067)](https://camo.githubusercontent.com/263059e57c8960092b1d18dc3d85a04d5a70c36830824906211362f4215faf39/68747470733a2f2f692e696d6775722e636f6d2f7244664a7572792e6a7067)

🎓 Learning Gatsby
------------------

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#-learning-gatsby)

Looking for more guidance? Full documentation for Gatsby lives [on the website](https://www.gatsbyjs.com/).

Here are some places to start:

### Themes

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#themes)

*   To learn more about Gatsby themes specifically, we recommend checking out the [theme docs](https://www.gatsbyjs.com/docs/themes/).

### General

[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#general)

*   **For most developers, we recommend starting with our [in-depth tutorial for creating a site with Gatsby](https://www.gatsbyjs.com/tutorial/).** It starts with zero assumptions about your level of ability and walks through every step of the process.
    
*   **To dive straight into code samples, head [to our documentation](https://www.gatsbyjs.com/docs/).** In particular, check out the _Reference Guides_ and _Gatsby API_ sections in the sidebar.

## Metadata

```json
{
  "title": "GitHub - theowenyoung/gatsby-theme-timeline: Gastby theme timeline",
  "description": "Gastby theme timeline. Contribute to theowenyoung/gatsby-theme-timeline development by creating an account on GitHub.",
  "url": "https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true",
  "content": "Gatsby Theme Timeline\n---------------------\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#gatsby-theme-timeline)\n\nThis is a repo for Gatsby's timeline theme, with the theme, you can show all your posts, tweets, instagram medias, youtube videos, hacker news, reddit post at one.\n\n[Live Demo](https://gatsby-theme-timeline.owenyoung.com/)\n\n[![Image 5: Screen](https://camo.githubusercontent.com/a5d4d44d5f4a05ee4b41c2911491b245d02281fb0dd00dfa55958fa70ae35d9e/68747470733a2f2f692e696d6775722e636f6d2f367949544934452e706e67)](https://camo.githubusercontent.com/a5d4d44d5f4a05ee4b41c2911491b245d02281fb0dd00dfa55958fa70ae35d9e/68747470733a2f2f692e696d6775722e636f6d2f367949544934452e706e67)\n\nFeatures\n--------\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#features)\n\n*   Support Mdx, tweet, instagram medias, youtube videos, hacker news, reddit post\n*   Support i18n by [gatsby-theme-i18n](https://www.gatsbyjs.com/plugins/gatsby-theme-i18n/), you can choose your own [i18n library](https://github.com/gatsbyjs/themes/tree/master/packages)\n*   Support comments [disqus](https://disqus.com/) or [utterances](https://utteranc.es/)\n*   Support Tags\n*   Pagination, even tag page supports pagination\n*   SEO Optimization\n\n🚀 Quick start\n--------------\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#-quick-start)\n\n> Learn more about the theme information at [here](https://github.com/theowenyoung/gatsby-theme-timeline/tree/main/packages/gatsby-theme-timeline#readme)\n\n1.  **Create a Gatsby site.**\n    \n    Use the Gatsby CLI to create a new site, specifying the timeline blog theme starter.\n    \n    # create a new Gatsby site using the timeline blog theme starter\n    gatsby new my-themed-blog https://github.com/theowenyoung/gatsby-starter-timeline\n    \n2.  **Create twitter credentials**\n    \n    Optional, if you want to add your tweets to blog, create `.env` with the following content:\n    \n    TWITTER\\_CONSUMER\\_KEY\\=xx\n    TWITTER\\_CONSUMER\\_SECRET\\=xx\n    TWITTER\\_ACCESS\\_TOKEN\\=xx\n    TWITTER\\_ACCESS\\_SECRET\\=xx\n    \n    Then, uncomment `gatsby-config.js` plugin `gatsby-source-twitter`\n    \n3.  **Create instagram credentials**\n    \n    Optional, if you want to add your instagram to blog, create `.env` with the following content:\n    \n    INSTAGRAM\\_ACCESS\\_TOKEN\\=xx\n    \n    > See [How to get instagram access token](https://github.com/nbcommunication/InstagramBasicDisplayApi#creating-a-facebook-app)\n    \n    > Then, uncomment `gatsby-config.js` plugin `gatsby-source-instagram`\n    \n4.  **Start developing.**\n    \n    Navigate into your new site’s directory and start it up.\n    \n    cd my-themed-blog/\n    gatsby develop\n    \n5.  **Open the code and start customizing!**\n    \n    Your site is now running at `http://localhost:8000`!\n    \n\nFor exist site or more params, see [here](https://github.com/theowenyoung/gatsby-theme-timeline/tree/main/packages/gatsby-theme-timeline#readme)\n\nFirst using Gatsby? check out the guide to [using the Gatsby blog theme starter](https://gatsbyjs.com/docs/themes/using-a-gatsby-theme), or the longer, [more detailed tutorial](https://gatsbyjs.com/tutorial/using-a-theme).\n\n🧐 What's inside?\n-----------------\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#-whats-inside)\n\nHere are the top-level files and directories you'll see in a site created using the timeline blog theme starter:\n\n```\ngatsby-starter-timeline\n├── content\n│   ├── assets\n│   │   └── avatar.png\n│   └── posts\n│       ├── hello-world.mdx\n│       └── my-second-post.mdx\n├── data\n│   ├── tweets\n│       ├── 1111.json\n│       └── 2222.json\n│   ├── reddit\n│       ├── 1111.json\n│       └── 2222.json\n├── src\n│   └── gatsby-theme-timeline\n│       ├── components\n│       │   └── bio-content.js\n│       └── gatsby-theme-ui\n│           └── colors.js\n├── .gitignore\n├── .prettierrc\n├── gatsby-config.js\n├── LICENSE\n├── package-lock.json\n├── package.json\n└── README.md\n```\n\n1.  **`/content`**: A content folder holding assets that the theme expects to exist. This will vary from theme to theme -- this starter is set up to get you started with the timeline blog theme, which expects an image asset for your avatar, and blog post content. Replace the avatar image file, delete the demo posts, and add your own!\n    \n2.  **`/data`**: A raw data folder holding raw data like tweets, reddit json.\n    \n3.  **`/src`**: You will probably want to customize your site to personalize it. The files under `/src/gatsby-theme-blog` _shadow_, or override, the files of the same name in the `gatsby-theme-blog` package. To learn more about this, check out the [guide to getting started with using the timeline blog theme starter](https://gatsbyjs.com/docs/themes/using-a-gatsby-theme).\n    \n4.  **`.gitignore`**: This file tells git which files it should not track / not maintain a version history for.\n    \n5.  **`.prettierrc`**: This file tells [Prettier](https://prettier.io/) which configuration it should use to lint files.\n    \n6.  **`gatsby-config.js`**: This is the main configuration file for a Gatsby site. This is where you can specify information about your site (metadata) like the site title and description, which Gatsby plugins you’d like to include, etc. When using themes, it's where you'll include the theme plugin, and any customization options the theme provides.\n    \n7.  **`LICENSE`**: This Gatsby starter is licensed under the 0BSD license. This means that you can see this file as a placeholder and replace it with your own license.\n    \n8.  **`package-lock.json`** (See `package.json` below, first). This is an automatically generated file based on the exact versions of your npm dependencies that were installed for your project. **(You won’t change this file directly).**\n    \n9.  **`package.json`**: A manifest file for Node.js projects, which includes things like metadata (the project’s name, author, etc). This manifest is how npm knows which packages to install for your project.\n    \n10.  **`README.md`**: A text file containing useful reference information about your project.\n    \n\nUse Case\n--------\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#use-case)\n\n*   [Owen Young's Story](https://blog.owenyoung.com/)\n*   [Buzzing on stocks](https://stocks.buzzing.cc/)\n\nFull Screen\n-----------\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#full-screen)\n\n[![Image 6: Full](https://camo.githubusercontent.com/263059e57c8960092b1d18dc3d85a04d5a70c36830824906211362f4215faf39/68747470733a2f2f692e696d6775722e636f6d2f7244664a7572792e6a7067)](https://camo.githubusercontent.com/263059e57c8960092b1d18dc3d85a04d5a70c36830824906211362f4215faf39/68747470733a2f2f692e696d6775722e636f6d2f7244664a7572792e6a7067)\n\n🎓 Learning Gatsby\n------------------\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#-learning-gatsby)\n\nLooking for more guidance? Full documentation for Gatsby lives [on the website](https://www.gatsbyjs.com/).\n\nHere are some places to start:\n\n### Themes\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#themes)\n\n*   To learn more about Gatsby themes specifically, we recommend checking out the [theme docs](https://www.gatsbyjs.com/docs/themes/).\n\n### General\n\n[](https://github.com/theowenyoung/gatsby-theme-timeline?screenshot=true#general)\n\n*   **For most developers, we recommend starting with our [in-depth tutorial for creating a site with Gatsby](https://www.gatsbyjs.com/tutorial/).** It starts with zero assumptions about your level of ability and walks through every step of the process.\n    \n*   **To dive straight into code samples, head [to our documentation](https://www.gatsbyjs.com/docs/).** In particular, check out the _Reference Guides_ and _Gatsby API_ sections in the sidebar.",
  "usage": {
    "tokens": 2114
  }
}
```
