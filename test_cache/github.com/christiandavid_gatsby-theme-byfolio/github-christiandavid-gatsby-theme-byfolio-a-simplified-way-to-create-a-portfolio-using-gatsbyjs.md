---
title: GitHub - christiandavid/gatsby-theme-byfolio: A simplified way to create a portfolio using GatsbyJS
description: A simplified way to create a portfolio using GatsbyJS - christiandavid/gatsby-theme-byfolio
url: https://github.com/christiandavid/gatsby-theme-byfolio
timestamp: 2025-01-20T15:31:33.969Z
domain: github.com
path: christiandavid_gatsby-theme-byfolio
---

# GitHub - christiandavid/gatsby-theme-byfolio: A simplified way to create a portfolio using GatsbyJS


A simplified way to create a portfolio using GatsbyJS - christiandavid/gatsby-theme-byfolio


## Content

gatsby-theme-byfolio
--------------------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#gatsby-theme-byfolio)

[![Image 16: License: MIT](https://camo.githubusercontent.com/28f4d479bf0a9b033b3a3b95ab2adc343da448a025b01aefdc0fbc7f0e169eb8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667)](https://github.com/christiandavid/gatsby-theme-byfolio/blob/dev/LICENSE) [![Image 17: CircleCI](https://camo.githubusercontent.com/45e2457a24835ee39e7230d88a57cb556abd330dd3ff076578bc2ecf059514d4/68747470733a2f2f636972636c6563692e636f6d2f67682f63687269737469616e64617669642f6761747362792d7468656d652d6279666f6c696f2e7376673f7374796c653d737667)](https://circleci.com/gh/christiandavid/gatsby-theme-byfolio) [![Image 18: Twitter Follow](https://camo.githubusercontent.com/57646410c227fc5d2c99f7b79637e69ebab0fb5e5b00ed12d8e4b21877b72375/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6943687269737469616e44617669643f7374796c653d736f6369616c)](https://camo.githubusercontent.com/57646410c227fc5d2c99f7b79637e69ebab0fb5e5b00ed12d8e4b21877b72375/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6943687269737469616e44617669643f7374796c653d736f6369616c)

Initially this was a personal portfolio made in GatsbyJs, now it's a Gatsby theme available to anyone who wants to tell their work history focusing only on the content.

[![Image 19: Gatsby Portfolio](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/Byfolio.jpg)](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/Byfolio.jpg)

[![Image 20: Portfolio](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/portfolio.gif)](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/portfolio.gif)

*   [Installation](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#installation)
*   [Configuration](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#configuration)
*   [Adding experience and skills](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#adding-experience-and-skills)
*   [Skills](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#skills)
*   [Component shadowing](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#component-shadowing)
*   [Examples](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#examples)
*   [Authors](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#authors)
*   [Credits](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#credits)

Installation
------------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#installation)

mkdir portfolio && cd portfolio
yarn init -y
yarn add react react-dom gatsby @christiandavid/gatsby-theme-byfolio

Create gatsby-config.js file and load the plugin

// gatsby-config.js
module.exports \= {
  plugins: \[
    {
      resolve: \`@christiandavid/gatsby-theme-byfolio\`,
    },
  \],
}

In your browser load [localhost:8000](http://localhost:8000/)

Configuration
-------------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#configuration)

After each modification in gatsby-config.js it is necessary to restart the site from the terminal.

// gatsby-config.js
module.exports \= {
  plugins: \[
    {
      resolve: \`@christiandavid/gatsby-theme-byfolio\`,
      options: {
        basePath: \`\`,
        path: \`src/\`,
        imagesPath: \`src/images/\`,
        iconFile: \`src/images/icon.png\`,
        siteTitle: \`Portfolio\`,
        siteUrl: \`https://www.christianibarguen.com\`,
        siteName: \`Christian David Ibarguen\`,
        siteShortName: \`CD\`,
        siteDescription: \`This cool App contains information about my work experience as a software developer.\`,
        siteKeywords: \`Software developer, Full Stack Developer\`,
        useMozJpeg: true,
        menuLinks: \[
          // title = Link text
          // color = Animation background color on click
          { name: \`home\`, title: \`Home\`, color: \`#000\`, link: \`\` },
          {
            name: \`experience\`,
            title: \`Experience\`,
            color: \`#3a3d98\`,
            link: \`\`,
          },
          { name: \`skills\`, title: \`Skills\`, color: \`#d52d43\`, link: \`\` },
          { name: \`aboutMe\`, title: \`About Me\`, color: \`#fff\`, link: \`\` },
        \],
        email: \`christian@davidibarguen.com\`,
        social: {
          // Usernames
          twitter: \`ichristiandavid\`,
          gitHub: \`christiandavid\`,
          stackOverflow: \`967956/christian-david\`,
          linkedIn: \`in/christianibarguen/\`,
          resumeInPdf: \`/CV-19.pdf\`, // url or local link
        },
        homePage: {
          availableToHire: true,
          dotColors: \["#0e3e1e", "#6CC551"\],
          h1Text: \`Hi!, I'm Christian David Ibarguen\`,
          h2Text: \`I'm a Full Stack Developer who loves working in Backend, I have
              worked as a software developer since 2006.\`,
          typewriter: \[
            \`Coding is my passion 😎\`,
            \`I'm a 🍕 lover\`,
            \`I'm a pretty fast learner and always interested in learning new technologies 🤓\`,
            \`I think one of my values is the <strong\>ability to resolve problems<strong\>\`,
            \`I like to share what I know 👨‍🏫\`,
            \`In my non-coding hours, I'm at the 🏋‍\`,
            \`I also do design and UX work <span style='color: #27ae60;'\>occasionally</span\>\`,
          \],
        },
        // Color for menu background
        shapeColor: {
          link: { color: "#171616", hover: "#fff" },
          shape1: {
            color: \`#413f46\`,
            opacity: \`0.7\`,
          },
          shape2: {
            color: \`#e6e5ea\`,
            opacity: \`0.7\`,
          },
          shape3: {
            color: \`#fff\`,
            opacity: \`0.7\`,
          },
        },
        footer: \`heart\`,
      },
    },
  \],
}

| Option name | Type | Description |
| --- | --- | --- |
| basePath | string | Where should the site be served from? /portfolio will change all paths to start with /portfolio |
| path | string | Place where the files are stored, for example: `src/` |
| imagesPath | string | Place where the images files are stored, for example: `src/images/` |
| iconFile | string | Provides the icon path for the gatsby-plugin-manifest plugin |
| typographyPath | string | Place where the file that defines your website’s typography configuration is located |
| siteTitle | string | The main title for the website, used in the `<title>` element |
| siteUrl | string | The portfolio url, example: `https://christianibarguen.com` |
| siteName | string | Represents the name of the web application as it is usually displayed to the user |
| siteShortName | string | Represents a short version of the name of the web application |
| siteDescription | string | Allows you to describe the purpose of the web application |
| siteKeywords | string | Keywords for the page |
| useMozJpeg | boolean | MozJPEG provides better image compression than the default encoder used in gatsby-plugin-sharp. |
| menuLinks | array | An array of objects for the menu, each item represents a link, color represents the color that the animation shows when it is pressed |
| email | string | Email for contact, this is displayed when the Contact Me button is pressed |
| social | object | An Object with the user accounts of: twitter, gitHub, stackOverflow, linkedIn and `resumeInPdf` resume link |
| homePage | object | An object with information of titles, texts with animated description, and animation to show if you are available to be hired |
| shapeColor | object | Represents the colors used in the menu animation, in total there are 3 in which you can specify the color and the opacity |
| footer | string | Text to show in the footer only has 2 options: `heart`or `hand` |

Adding experience and skills
----------------------------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#adding-experience-and-skills)

This theme generates pages based on Markdown files in the `path`/experience directory. Your Markdown files should contain some frontmatter defining their company, logo, etc. All company logos must be relative to `imagesPath`/companies directory. All Skills logos must be relative to `imagesPath`/skills directory. All layout images must be relative to company directory, for example: `imagesPath`/companies/vlooping

### Important

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#important)

For each Skill you must add the logo of the Framework, library or program, with a resolution of **width: 500px, height: 500px**, in the src/images/skills/ directory I leave several logos, **only Skills logos that I own are present, if the logo you need does not appear you must create it**.

Layout number is for image animation you can select from 1 to 5, **please do not forget to add the images "images/companies/vlooping.png, images/skills/html5.png, images/skills/react.png, images/companies/vlooping/vlooping.png" to run the following example**

\---
title: ""
company: "Company Name"
logo: ../images/companies/vlooping.png
jobTitle: "My job position"
skills:
  \[
    { title: "HTML 5", image: ../images/skills/html5.png },
    { title: "HTML 5", image: ../images/skills/react.png },
  \]
images:
  \[
    {
      title: "Layout 4",
      description: "Description text for layout 4.",
      layout: "4",
      files:
        \[
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
        \],
    },
    {
      title: "Layout 1",
      description: "Description text for layout 1.",
      layout: "1",
      files:
        \[
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
        \],
    },
    {
      title: "Layout 2",
      description: "Description text for layout 2.",
      layout: "2",
      files:
        \[
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
        \],
      caption: "New Message",
    },
    {
      title: "Layout 3",
      description: "Description text for layout 1.",
      layout: "3",
      files:
        \[
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
        \],
    },
    {
      title: "Layout 5",
      description: "Description text for layout 5.",
      layout: "5",
      files:
        \[
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
          { image: ../images/companies/vlooping/vlooping.png },
        \],
    },
  \]
dateFrom: "2015-12-01"
dateTo: "2019-12-01"
---
- Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
- Contrary to popular belief, Lorem Ipsum is not simply random text
- It is a long established fact that a reader will be distracted by the readable content of a page
- There are many variations of passages of Lorem Ipsum available
- The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested

### Skills

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#skills)

The Skills are automatically selected from experience, in case some skill you acquired does not correspond to a company you can add it in `path`/experience/\_additionalSkills.md

\---
title: ""
company: ""
jobTitle: ""
logo:
skills:
  \[
    { title: "React", image: ../images/skills/react.png },
    { title: "React Native", image: ../images/skills/react-native.png },
    { title: "Gatsby", image: ../images/skills/gatsby.png },
    { title: "GraphQL", image: ../images/skills/graphql.png },
    { title: "Redux", image: ../images/skills/redux.png },
    { title: "Apollo GraphQL", image: ../images/skills/apollo.png },
    { title: "Socket.io", image: ../images/skills/socket-io.png },
  \]
images: \[\]
dateFrom: "2019-09-01"
dateTo: "2019-09-01"
---

Component shadowing
-------------------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#component-shadowing)

You can customize elements like the css style or about-me content by taking advantage of [component shadowing](https://www.gatsbyjs.org/blog/2019-04-29-component-shadowing/).

I recommend using [Coolors.co](https://coolors.co/) to select a color palette and adapt it to your new portfolio.

You can change the color of the text and the background of each page, for example:

// src/@christiandavid/gatsby-theme-byfolio/layout/layoutColors.css.js
import { css } from "@emotion/core"
import lineSvg from "../../../static/assets/line.svg"

const styles \= css\`
  .e404.layout-wrapper .layout-inner {
    background: #fff;
  }
  .e404 .data-section {
    color: #000;
  }
  .aboutme.layout-wrapper .layout-inner {
    background: #fff;
  }
  .aboutme .data-section {
    color: #000;
  }
  .aboutme .hamburgercolr::before,
  .aboutme .hamburgercolr::after,
  .e404 .hamburgercolr::before,
  .e404 .hamburgercolr::after {
    background-color: #000;
  }
  .home.layout-wrapper .layout-inner {
    background: #0e0f11;
    background: #0e0f11 url(${lineSvg}) center center fixed;
    background-size: contain;
  }
  .home.layout-wrapper h1,
  .home.layout-wrapper h2 {
    color: #fff;
  }
  .skill.layout-wrapper .layout-inner {
    color: #fff;
    background: #9d316e;
    background: url(${lineSvg}) center center fixed, linear-gradient(
        45deg,
        #9d316e,
        #de2d3e
      );
    background-size: cover;
  }
  .experience.layout-wrapper .layout-inner {
    background: #3a3d98;
    background: url(${lineSvg}) center center fixed, linear-gradient(
        45deg,
        #6f22b9,
        #3a3d98
      );
    background-size: cover;
  }
  .home .hamburgercolr::before,
  .home .hamburgercolr::after,
  .skill .hamburgercolr::before,
  .skill .hamburgercolr::after,
  .experience .hamburgercolr::before,
  .experience .hamburgercolr::after {
    background-color: #fff;
  }
  .home .btn-contact-color,
  .experience .btn-contact-color {
    color: #fff;
  }
  .aboutme .btn-contact-color,
  .e404 .btn-contact-color {
    color: #000;
  }
\`

export default styles

You can change the about-me text in the "src/@christiandavid/gatsby-theme-byfolio/contentJSON/about-me.json" file, for example:

\[
  {
    "subtitle": "About Me!",
    "content": "I'm a <strong\>Software Developer</strong\>"
  },
  {
    "subtitle": "Experience!",
    "content": "I started developing software from <strong\>2004</strong\> working in several companies"
  }
\]

Examples
--------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#examples)

*   [My Portfolio](https://christianibarguen.com/)
*   [Mario Gómez Portfolio](http://mariogmz.com/)

Are you using this theme in your own project? Submit a PR with your website added to this list!

Authors
-------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#authors)

*   **Christian David Ibarguen R**

Credits
-------

[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#credits)

Special thanks to:

*   [GatsbyJs](https://www.gatsbyjs.org/)
*   [Codrops](https://tympanus.net/codrops/)
*   [Fontawesome](https://fontawesome.com/license)

## Metadata

```json
{
  "title": "GitHub - christiandavid/gatsby-theme-byfolio: A simplified way to create a portfolio using GatsbyJS",
  "description": "A simplified way to create a portfolio using GatsbyJS - christiandavid/gatsby-theme-byfolio",
  "url": "https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true",
  "content": "gatsby-theme-byfolio\n--------------------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#gatsby-theme-byfolio)\n\n[![Image 16: License: MIT](https://camo.githubusercontent.com/28f4d479bf0a9b033b3a3b95ab2adc343da448a025b01aefdc0fbc7f0e169eb8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667)](https://github.com/christiandavid/gatsby-theme-byfolio/blob/dev/LICENSE) [![Image 17: CircleCI](https://camo.githubusercontent.com/45e2457a24835ee39e7230d88a57cb556abd330dd3ff076578bc2ecf059514d4/68747470733a2f2f636972636c6563692e636f6d2f67682f63687269737469616e64617669642f6761747362792d7468656d652d6279666f6c696f2e7376673f7374796c653d737667)](https://circleci.com/gh/christiandavid/gatsby-theme-byfolio) [![Image 18: Twitter Follow](https://camo.githubusercontent.com/57646410c227fc5d2c99f7b79637e69ebab0fb5e5b00ed12d8e4b21877b72375/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6943687269737469616e44617669643f7374796c653d736f6369616c)](https://camo.githubusercontent.com/57646410c227fc5d2c99f7b79637e69ebab0fb5e5b00ed12d8e4b21877b72375/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6943687269737469616e44617669643f7374796c653d736f6369616c)\n\nInitially this was a personal portfolio made in GatsbyJs, now it's a Gatsby theme available to anyone who wants to tell their work history focusing only on the content.\n\n[![Image 19: Gatsby Portfolio](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/Byfolio.jpg)](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/Byfolio.jpg)\n\n[![Image 20: Portfolio](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/portfolio.gif)](https://raw.githubusercontent.com/christiandavid/gatsby-theme-byfolio/dev/readme-files/portfolio.gif)\n\n*   [Installation](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#installation)\n*   [Configuration](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#configuration)\n*   [Adding experience and skills](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#adding-experience-and-skills)\n*   [Skills](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#skills)\n*   [Component shadowing](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#component-shadowing)\n*   [Examples](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#examples)\n*   [Authors](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#authors)\n*   [Credits](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#credits)\n\nInstallation\n------------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#installation)\n\nmkdir portfolio && cd portfolio\nyarn init -y\nyarn add react react-dom gatsby @christiandavid/gatsby-theme-byfolio\n\nCreate gatsby-config.js file and load the plugin\n\n// gatsby-config.js\nmodule.exports \\= {\n  plugins: \\[\n    {\n      resolve: \\`@christiandavid/gatsby-theme-byfolio\\`,\n    },\n  \\],\n}\n\nIn your browser load [localhost:8000](http://localhost:8000/)\n\nConfiguration\n-------------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#configuration)\n\nAfter each modification in gatsby-config.js it is necessary to restart the site from the terminal.\n\n// gatsby-config.js\nmodule.exports \\= {\n  plugins: \\[\n    {\n      resolve: \\`@christiandavid/gatsby-theme-byfolio\\`,\n      options: {\n        basePath: \\`\\`,\n        path: \\`src/\\`,\n        imagesPath: \\`src/images/\\`,\n        iconFile: \\`src/images/icon.png\\`,\n        siteTitle: \\`Portfolio\\`,\n        siteUrl: \\`https://www.christianibarguen.com\\`,\n        siteName: \\`Christian David Ibarguen\\`,\n        siteShortName: \\`CD\\`,\n        siteDescription: \\`This cool App contains information about my work experience as a software developer.\\`,\n        siteKeywords: \\`Software developer, Full Stack Developer\\`,\n        useMozJpeg: true,\n        menuLinks: \\[\n          // title = Link text\n          // color = Animation background color on click\n          { name: \\`home\\`, title: \\`Home\\`, color: \\`#000\\`, link: \\`\\` },\n          {\n            name: \\`experience\\`,\n            title: \\`Experience\\`,\n            color: \\`#3a3d98\\`,\n            link: \\`\\`,\n          },\n          { name: \\`skills\\`, title: \\`Skills\\`, color: \\`#d52d43\\`, link: \\`\\` },\n          { name: \\`aboutMe\\`, title: \\`About Me\\`, color: \\`#fff\\`, link: \\`\\` },\n        \\],\n        email: \\`christian@davidibarguen.com\\`,\n        social: {\n          // Usernames\n          twitter: \\`ichristiandavid\\`,\n          gitHub: \\`christiandavid\\`,\n          stackOverflow: \\`967956/christian-david\\`,\n          linkedIn: \\`in/christianibarguen/\\`,\n          resumeInPdf: \\`/CV-19.pdf\\`, // url or local link\n        },\n        homePage: {\n          availableToHire: true,\n          dotColors: \\[\"#0e3e1e\", \"#6CC551\"\\],\n          h1Text: \\`Hi!, I'm Christian David Ibarguen\\`,\n          h2Text: \\`I'm a Full Stack Developer who loves working in Backend, I have\n              worked as a software developer since 2006.\\`,\n          typewriter: \\[\n            \\`Coding is my passion 😎\\`,\n            \\`I'm a 🍕 lover\\`,\n            \\`I'm a pretty fast learner and always interested in learning new technologies 🤓\\`,\n            \\`I think one of my values is the <strong\\>ability to resolve problems<strong\\>\\`,\n            \\`I like to share what I know 👨‍🏫\\`,\n            \\`In my non-coding hours, I'm at the 🏋‍\\`,\n            \\`I also do design and UX work <span style='color: #27ae60;'\\>occasionally</span\\>\\`,\n          \\],\n        },\n        // Color for menu background\n        shapeColor: {\n          link: { color: \"#171616\", hover: \"#fff\" },\n          shape1: {\n            color: \\`#413f46\\`,\n            opacity: \\`0.7\\`,\n          },\n          shape2: {\n            color: \\`#e6e5ea\\`,\n            opacity: \\`0.7\\`,\n          },\n          shape3: {\n            color: \\`#fff\\`,\n            opacity: \\`0.7\\`,\n          },\n        },\n        footer: \\`heart\\`,\n      },\n    },\n  \\],\n}\n\n| Option name | Type | Description |\n| --- | --- | --- |\n| basePath | string | Where should the site be served from? /portfolio will change all paths to start with /portfolio |\n| path | string | Place where the files are stored, for example: `src/` |\n| imagesPath | string | Place where the images files are stored, for example: `src/images/` |\n| iconFile | string | Provides the icon path for the gatsby-plugin-manifest plugin |\n| typographyPath | string | Place where the file that defines your website’s typography configuration is located |\n| siteTitle | string | The main title for the website, used in the `<title>` element |\n| siteUrl | string | The portfolio url, example: `https://christianibarguen.com` |\n| siteName | string | Represents the name of the web application as it is usually displayed to the user |\n| siteShortName | string | Represents a short version of the name of the web application |\n| siteDescription | string | Allows you to describe the purpose of the web application |\n| siteKeywords | string | Keywords for the page |\n| useMozJpeg | boolean | MozJPEG provides better image compression than the default encoder used in gatsby-plugin-sharp. |\n| menuLinks | array | An array of objects for the menu, each item represents a link, color represents the color that the animation shows when it is pressed |\n| email | string | Email for contact, this is displayed when the Contact Me button is pressed |\n| social | object | An Object with the user accounts of: twitter, gitHub, stackOverflow, linkedIn and `resumeInPdf` resume link |\n| homePage | object | An object with information of titles, texts with animated description, and animation to show if you are available to be hired |\n| shapeColor | object | Represents the colors used in the menu animation, in total there are 3 in which you can specify the color and the opacity |\n| footer | string | Text to show in the footer only has 2 options: `heart`or `hand` |\n\nAdding experience and skills\n----------------------------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#adding-experience-and-skills)\n\nThis theme generates pages based on Markdown files in the `path`/experience directory. Your Markdown files should contain some frontmatter defining their company, logo, etc. All company logos must be relative to `imagesPath`/companies directory. All Skills logos must be relative to `imagesPath`/skills directory. All layout images must be relative to company directory, for example: `imagesPath`/companies/vlooping\n\n### Important\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#important)\n\nFor each Skill you must add the logo of the Framework, library or program, with a resolution of **width: 500px, height: 500px**, in the src/images/skills/ directory I leave several logos, **only Skills logos that I own are present, if the logo you need does not appear you must create it**.\n\nLayout number is for image animation you can select from 1 to 5, **please do not forget to add the images \"images/companies/vlooping.png, images/skills/html5.png, images/skills/react.png, images/companies/vlooping/vlooping.png\" to run the following example**\n\n\\---\ntitle: \"\"\ncompany: \"Company Name\"\nlogo: ../images/companies/vlooping.png\njobTitle: \"My job position\"\nskills:\n  \\[\n    { title: \"HTML 5\", image: ../images/skills/html5.png },\n    { title: \"HTML 5\", image: ../images/skills/react.png },\n  \\]\nimages:\n  \\[\n    {\n      title: \"Layout 4\",\n      description: \"Description text for layout 4.\",\n      layout: \"4\",\n      files:\n        \\[\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n        \\],\n    },\n    {\n      title: \"Layout 1\",\n      description: \"Description text for layout 1.\",\n      layout: \"1\",\n      files:\n        \\[\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n        \\],\n    },\n    {\n      title: \"Layout 2\",\n      description: \"Description text for layout 2.\",\n      layout: \"2\",\n      files:\n        \\[\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n        \\],\n      caption: \"New Message\",\n    },\n    {\n      title: \"Layout 3\",\n      description: \"Description text for layout 1.\",\n      layout: \"3\",\n      files:\n        \\[\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n        \\],\n    },\n    {\n      title: \"Layout 5\",\n      description: \"Description text for layout 5.\",\n      layout: \"5\",\n      files:\n        \\[\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n          { image: ../images/companies/vlooping/vlooping.png },\n        \\],\n    },\n  \\]\ndateFrom: \"2015-12-01\"\ndateTo: \"2019-12-01\"\n---\n- Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum\n- Contrary to popular belief, Lorem Ipsum is not simply random text\n- It is a long established fact that a reader will be distracted by the readable content of a page\n- There are many variations of passages of Lorem Ipsum available\n- The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested\n\n### Skills\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#skills)\n\nThe Skills are automatically selected from experience, in case some skill you acquired does not correspond to a company you can add it in `path`/experience/\\_additionalSkills.md\n\n\\---\ntitle: \"\"\ncompany: \"\"\njobTitle: \"\"\nlogo:\nskills:\n  \\[\n    { title: \"React\", image: ../images/skills/react.png },\n    { title: \"React Native\", image: ../images/skills/react-native.png },\n    { title: \"Gatsby\", image: ../images/skills/gatsby.png },\n    { title: \"GraphQL\", image: ../images/skills/graphql.png },\n    { title: \"Redux\", image: ../images/skills/redux.png },\n    { title: \"Apollo GraphQL\", image: ../images/skills/apollo.png },\n    { title: \"Socket.io\", image: ../images/skills/socket-io.png },\n  \\]\nimages: \\[\\]\ndateFrom: \"2019-09-01\"\ndateTo: \"2019-09-01\"\n---\n\nComponent shadowing\n-------------------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#component-shadowing)\n\nYou can customize elements like the css style or about-me content by taking advantage of [component shadowing](https://www.gatsbyjs.org/blog/2019-04-29-component-shadowing/).\n\nI recommend using [Coolors.co](https://coolors.co/) to select a color palette and adapt it to your new portfolio.\n\nYou can change the color of the text and the background of each page, for example:\n\n// src/@christiandavid/gatsby-theme-byfolio/layout/layoutColors.css.js\nimport { css } from \"@emotion/core\"\nimport lineSvg from \"../../../static/assets/line.svg\"\n\nconst styles \\= css\\`\n  .e404.layout-wrapper .layout-inner {\n    background: #fff;\n  }\n  .e404 .data-section {\n    color: #000;\n  }\n  .aboutme.layout-wrapper .layout-inner {\n    background: #fff;\n  }\n  .aboutme .data-section {\n    color: #000;\n  }\n  .aboutme .hamburgercolr::before,\n  .aboutme .hamburgercolr::after,\n  .e404 .hamburgercolr::before,\n  .e404 .hamburgercolr::after {\n    background-color: #000;\n  }\n  .home.layout-wrapper .layout-inner {\n    background: #0e0f11;\n    background: #0e0f11 url(${lineSvg}) center center fixed;\n    background-size: contain;\n  }\n  .home.layout-wrapper h1,\n  .home.layout-wrapper h2 {\n    color: #fff;\n  }\n  .skill.layout-wrapper .layout-inner {\n    color: #fff;\n    background: #9d316e;\n    background: url(${lineSvg}) center center fixed, linear-gradient(\n        45deg,\n        #9d316e,\n        #de2d3e\n      );\n    background-size: cover;\n  }\n  .experience.layout-wrapper .layout-inner {\n    background: #3a3d98;\n    background: url(${lineSvg}) center center fixed, linear-gradient(\n        45deg,\n        #6f22b9,\n        #3a3d98\n      );\n    background-size: cover;\n  }\n  .home .hamburgercolr::before,\n  .home .hamburgercolr::after,\n  .skill .hamburgercolr::before,\n  .skill .hamburgercolr::after,\n  .experience .hamburgercolr::before,\n  .experience .hamburgercolr::after {\n    background-color: #fff;\n  }\n  .home .btn-contact-color,\n  .experience .btn-contact-color {\n    color: #fff;\n  }\n  .aboutme .btn-contact-color,\n  .e404 .btn-contact-color {\n    color: #000;\n  }\n\\`\n\nexport default styles\n\nYou can change the about-me text in the \"src/@christiandavid/gatsby-theme-byfolio/contentJSON/about-me.json\" file, for example:\n\n\\[\n  {\n    \"subtitle\": \"About Me!\",\n    \"content\": \"I'm a <strong\\>Software Developer</strong\\>\"\n  },\n  {\n    \"subtitle\": \"Experience!\",\n    \"content\": \"I started developing software from <strong\\>2004</strong\\> working in several companies\"\n  }\n\\]\n\nExamples\n--------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#examples)\n\n*   [My Portfolio](https://christianibarguen.com/)\n*   [Mario Gómez Portfolio](http://mariogmz.com/)\n\nAre you using this theme in your own project? Submit a PR with your website added to this list!\n\nAuthors\n-------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#authors)\n\n*   **Christian David Ibarguen R**\n\nCredits\n-------\n\n[](https://github.com/christiandavid/gatsby-theme-byfolio?screenshot=true#credits)\n\nSpecial thanks to:\n\n*   [GatsbyJs](https://www.gatsbyjs.org/)\n*   [Codrops](https://tympanus.net/codrops/)\n*   [Fontawesome](https://fontawesome.com/license)",
  "usage": {
    "tokens": 4344
  }
}
```
