---
title: GitHub - staticfuse/staticfuse: Monorepo for Static Fuse Gatsby Themes
description: Monorepo for Static Fuse Gatsby Themes. Contribute to staticfuse/staticfuse development by creating an account on GitHub.
url: https://github.com/staticfuse/staticfuse
timestamp: 2025-01-20T15:31:22.042Z
domain: github.com
path: staticfuse_staticfuse
---

# GitHub - staticfuse/staticfuse: Monorepo for Static Fuse Gatsby Themes


Monorepo for Static Fuse Gatsby Themes. Contribute to staticfuse/staticfuse development by creating an account on GitHub.


## Content

Gatsby WordPress Publisher Theme
--------------------------------

[](https://github.com/staticfuse/staticfuse?screenshot=true#gatsby-wordpress-publisher-theme)

[![Image 10: Gatsby Theme Publisher Screenshot](https://camo.githubusercontent.com/874400a82c6aa9cccae626c03fbfbd867c683f7b0e28b4c01d592684d83644bb/68747470733a2f2f646174612e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f7075626c69736865722d6865726f2e6a7067)](https://camo.githubusercontent.com/874400a82c6aa9cccae626c03fbfbd867c683f7b0e28b4c01d592684d83644bb/68747470733a2f2f646174612e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f7075626c69736865722d6865726f2e6a7067)

The Gatsby Publisher Theme allows you to create a headless (or decoupled) WordPress site. This theme will display all of your pages and posts in a static front-end built on React and Gatsby.

Overview
--------

[](https://github.com/staticfuse/staticfuse?screenshot=true#overview)

This repo is for theme development, we do not recommend cloning this repository. Instead, use the [Create Gatsby Theme Publisher repository](https://github.com/staticfuse/create-gatsby-theme-publisher), instructions are below. You can also [visit our website for a full tutorial on headless WordPress with Gatsby.](https://staticfuse.com/blog/how-to-build-headless-wordpress-sites-with-gatsby/)

### Prequisites

[](https://github.com/staticfuse/staticfuse?screenshot=true#prequisites)

*   [Node and NPM](https://www.gatsbyjs.org/tutorial/part-zero/#-install-nodejs-and-npm)
*   [Yarn](https://yarnpkg.com/lang/en/docs/install/)

Installation
------------

[](https://github.com/staticfuse/staticfuse?screenshot=true#installation)

We recommend starting by cloning [Create Gatsby Theme Publisher](https://github.com/staticfuse/create-gatsby-theme-publisher) which has the publisher theme installed and preconfigured.

1.  `git clone https://github.com/staticfuse/create-gatsby-theme-publisher`
2.  cd into the folder `cd create-gatsby-theme-publisher`
3.  Install dependencies `yarn`
4.  Install [WPGraphQL plugin on your WordPress site](https://github.com/wp-graphql/wp-graphql)
5.  Configure your site options in [gatsby-config.js](https://github.com/staticfuse/gatsby-theme-publisher/blob/master/demo/gatsby-config.js#L18) Explanation of the options is [below](https://github.com/staticfuse/gatsby-theme-publisher#publisher-theme-options)
6.  `gatsby develop` to start the local server
7.  Add your logo and [customize the theme](https://github.com/staticfuse/gatsby-theme-publisher#theme-customization)
8.  Publish to Netlify or any host.

### Adding Gatsby WordPress Theme Publisher to an existing Gatsby site

[](https://github.com/staticfuse/staticfuse?screenshot=true#adding-gatsby-wordpress-theme-publisher-to-an-existing-gatsby-site)

You can also add this theme to an existing Gatsby site.

1.  `yarn add @staticfuse/gatsby-theme-publisher`
2.  In your `gatsby-config.js` :

  plugins: \[
    {
      resolve: \`@staticfuse/gatsby-theme-publisher\`,
      options: {
        starterPages: true,
        mailChimpEndpoint: 0,
        dynamicComments: 1,
        gaTrackingId: 0,
        wordPressUrl: \`https://publishertheme.staticfuse.com\`, // The url of your WordPress install
        blogURI: '/blog' // Your posts page, change to whatever you'd prefer
      },
    },
  \],

Publisher Theme Options
-----------------------

[](https://github.com/staticfuse/staticfuse?screenshot=true#publisher-theme-options)

The following options can be configured in [your site's gatsby-config.js](https://github.com/staticfuse/gatsby-theme-publisher/blob/master/demo/gatsby-config.js#L12)

### Site Metadata

[](https://github.com/staticfuse/staticfuse?screenshot=true#site-metadata)

In demo/gatsby-config.js, edit the siteMetadata object with your site title, url, etc.

Note: `siteUrl` refers to your final website address. `wordPressUrl` in the plugin options refers to the WordPress site. For example, your WordPress site may be hosted at data.mybusiness.com, but your Gatsby site will be at mybusiness.com.

### Plugin Options

[](https://github.com/staticfuse/staticfuse?screenshot=true#plugin-options)

  plugins: \[
    {
      resolve: \`@staticfuse/gatsby-theme-publisher\`,
      options: {
        starterPages: true,
        dynamicComments: 1,
        gaTrackingId: 0,
        wordPressUrl: 'https://data.staticfuse.com',
        blogURI: '/blog',
        mailChimpEndpoint: 0,
        // ...etc
       },
    },
  \],

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| mailChimpEndpoint | string/boolean | 0 | [Your mailchimp endpoint](https://www.gatsbyjs.org/packages/gatsby-plugin-mailchimp/#mailchimp-endpoint). Set to `0` to disable. |
| dynamicComments | boolean | 1 | Enable or disable dynamic comments. If enabled, anyone can post a comment. |
| gaTrackingId | string/boolean | 0 | Your google analytics UA code. Set to `0` to disable Google Analytics. |
| wordPressUrl | string | `"https://scottbolinger.com"` | The URL of your WordPress site |
| blogURI | string | '' | The path prefix on the blog and blog posts. No leading slash. `'/blog'` would result in `https://my-domain.com/blog/` |
| starterPages | boolean | true | Create a home, about, and contact page in Gatsby. |
| menuName | string/boolean | 0 | The name of the _WordPress_ menu you'd like to use or `0` if you don't want to render a menu. |
| publisherMenuConfig | array | \[\] | Optional array based way to configure the menu. More info [here](https://github.com/staticfuse/gatsby-theme-publisher#publisher-menu). |

Theme Customization
-------------------

[](https://github.com/staticfuse/staticfuse?screenshot=true#theme-customization)

You can customize the colors, add or remove pages, and edit template files. All theme customization should happen in the /demo folder. If you are familiar with WordPress, this is like a "child theme."

Any changes you make in the main gatsby-theme-publisher folder will be overwritten by theme updates.

### Logo

[](https://github.com/staticfuse/staticfuse?screenshot=true#logo)

To add your logo, add demo/src/images/site-logo.png.

You will need to add a folder called images to the demo/src directory, and add your logo file inside with the name site-logo.png. You can make further modifications in the demo/src/components/Logo.js file.

### Customize Theme Colors

[](https://github.com/staticfuse/staticfuse?screenshot=true#customize-theme-colors)

Open demo/src/gatsby-theme-publisher/theme/theme.js

The theme color defaults are commented out, you can uncommment them and change the value. For example, to change the header background color, change...

`// headerBg: "#2D3748"`

to any color, such as...

`headerBg: "#bada55"`

You can also use predefined color values, such as...

`buttonBg: theme.colors.blue['500]`

or

`buttonText: theme.colors.orange['300']`

You can see those colors and more options [here](https://chakra-ui.com/theme).

### Publisher Menu

[](https://github.com/staticfuse/staticfuse?screenshot=true#publisher-menu)

There are two ways to configure the menu.

#### _1) publisherMenuConfig option (array config)_

[](https://github.com/staticfuse/staticfuse?screenshot=true#1-publishermenuconfig-option-array-config)

This is the default behavior. Theme setting `starterPages` is set to true. Publisher theme will output "Home", "About" & "Contact" with zero config. In the event you wanted to override this, you can add your config to the `publisherMenuConfig` theme option. For instance, if you wanted to add a link to `/portfolio` and child item to "Contact" you'd do the following:

  {
    resolve: '@staticfuse/gatsby-theme-publisher',
    options: {
      publisherMenuConfig: \[
        {
          label: 'Home',
          url: '/',
          isExternal: false,
        },
        {
          label: 'Blog',
          url: '/blog',
          isExternal: false,
        },
        {
          label: 'Portfolio',
          url: '/portfolio',
          isExternal: false,
        },
        {
          label: 'Contact',
          url: '/contact',
          isExternal: false,
          childItems: \[
            {
              label: 'I live in the dropdown',
              url: '/some-url',
              isExternal: false,
            },
          \],
        },
      \],
      // More options if so desired...
    }
  }

Keep in mind it's up to you to link to a valid page. In the example above, you would need to add a Gatsby page at your-theme/src/pages/portfolio, otherwise when you visit `/portfolio'`, your site will 404.

_What is `isExternal: false`?_

This tells the Publisher theme and Gatsby wether to navigate to a link client site using Gatsby `<Link/>` or use a `<a>`.

_Client_

{
  label: 'Blog',
  url: '/blog',
  isExternal: false,
},

_Full page reload_

{
  label: 'StaticFuse',
  url: 'https://staticfuse.com',
  isExternal: true,
},

#### _2) Use a WordPress menu_

[](https://github.com/staticfuse/staticfuse?screenshot=true#2-use-a-wordpress-menu)

You can manage your menu within the your WordPress site as well. To do so, change Publisher theme setting to: `menuName: 'your menu name'`. For example, the setting for the example (image) below would be: `menuName: 'PRIMARY'` [![Image 11: Gatsby Theme Publisher Screenshot](https://camo.githubusercontent.com/1c539f4da365a24835a4cf8d0b94cfdf8accee6e6e1a80e06480ea23b0262124/68747470733a2f2f7075626c69736865727468656d652e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f6d656e7573732e706e67)](https://camo.githubusercontent.com/1c539f4da365a24835a4cf8d0b94cfdf8accee6e6e1a80e06480ea23b0262124/68747470733a2f2f7075626c69736865727468656d652e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f6d656e7573732e706e67)

If you set a menu name, Publisher will automatically import your WordPress pages. If no menu name is set, no WordPress pages will be imported. You can override this behavior with the `wpPages` configuration option.

Many WordPress pages will not render properly in Gatsby, so we generally do not recommend this option. It is better to build your pages in Gatsby, and use posts from WordPress.

_Known limitation:_ For _both_ menu managment options, `childItems` are currently only supported _one_ level deep.

### Customize Templates

[](https://github.com/staticfuse/staticfuse?screenshot=true#customize-templates)

To change a page template layout, you can copy the file to the demo folder. For example, to edit the header, you would copy gatsby-theme-publisher/src/components/Header.js into demo/src/components/Header.js and edit the file there. Gatsby will automatically use your header file instead of the default.

This theme uses [Chakra UI](https://chakra-ui.com/), which gives you a lot of easy to use components. You can use any of these components in your theme templates.

Publishing to Netlify
---------------------

[](https://github.com/staticfuse/staticfuse?screenshot=true#publishing-to-netlify)

Netlify is a static hosting environment that is free to start, and handles Gatsby sites really well. To publish your site on Netlify, first create a new account at [netlify.com](https://netlify.com/).

Next, add your theme project files to a Github repository.

Login to Netlify and you will see a `New site from git` button at the top right corner of the screen. Click on it and authorize Netlify to use your account. Choose your website repository and it will take you to deploy settings with the below options.

*   Branch to deploy: You can specify a branch to monitor. When you push to that particular branch, only then will Netlify build and deploy the site. The default is master.
*   Build Command: You can specify the command you want Netlify to run when you push to the above branch. The default is `gatsby build`.
*   Publish directory: You can specify which folder Netlify should use to host the website. eg. public, dist, build. The default is `public`.
*   Advanced build settings: If the site needs environment variables to build, you can specify them by clicking on Show advanced and then the New Variable button.

Click on the Deploy site button and Netlify will start the build and deploy process you have specified. You can go to the Deploys tab and see the process unfold in the Deploy log. After a few moments, it will give you the live site URL eg. random-name.netlify.com.

Troubleshooting
---------------

[](https://github.com/staticfuse/staticfuse?screenshot=true#troubleshooting)

### CORS

[](https://github.com/staticfuse/staticfuse?screenshot=true#cors)

The search functionality makes remote requests to the source WordPress install. Depending on how your server/theme is configured, these requests could be blocked. There are a number of ways to set the [headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) including in a theme or plugin.

_this needs to go in a plugin or in your theme's fuctions.php_

/\*\*
 \* Add headers
 \*
 \* @param array $headers existing headers.
 \*
 \* @return array
 \*/
function filter\_graphql\_headers( $headers ) {
	$headers\['Access-Control-Allow-Origin'\]  = '\*'; // This should be the domain of your Gatsby site.
	$headers\['Access-Control-Allow-Methods'\] = 'GET, POST, OPTIONS';

	return $headers;
}
add\_filter( 'graphql\_response\_headers\_to\_send', 'filter\_graphql\_headers' );

## Metadata

```json
{
  "title": "GitHub - staticfuse/staticfuse: Monorepo for Static Fuse Gatsby Themes",
  "description": "Monorepo for Static Fuse Gatsby Themes. Contribute to staticfuse/staticfuse development by creating an account on GitHub.",
  "url": "https://github.com/staticfuse/staticfuse?screenshot=true",
  "content": "Gatsby WordPress Publisher Theme\n--------------------------------\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#gatsby-wordpress-publisher-theme)\n\n[![Image 10: Gatsby Theme Publisher Screenshot](https://camo.githubusercontent.com/874400a82c6aa9cccae626c03fbfbd867c683f7b0e28b4c01d592684d83644bb/68747470733a2f2f646174612e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f7075626c69736865722d6865726f2e6a7067)](https://camo.githubusercontent.com/874400a82c6aa9cccae626c03fbfbd867c683f7b0e28b4c01d592684d83644bb/68747470733a2f2f646174612e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f7075626c69736865722d6865726f2e6a7067)\n\nThe Gatsby Publisher Theme allows you to create a headless (or decoupled) WordPress site. This theme will display all of your pages and posts in a static front-end built on React and Gatsby.\n\nOverview\n--------\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#overview)\n\nThis repo is for theme development, we do not recommend cloning this repository. Instead, use the [Create Gatsby Theme Publisher repository](https://github.com/staticfuse/create-gatsby-theme-publisher), instructions are below. You can also [visit our website for a full tutorial on headless WordPress with Gatsby.](https://staticfuse.com/blog/how-to-build-headless-wordpress-sites-with-gatsby/)\n\n### Prequisites\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#prequisites)\n\n*   [Node and NPM](https://www.gatsbyjs.org/tutorial/part-zero/#-install-nodejs-and-npm)\n*   [Yarn](https://yarnpkg.com/lang/en/docs/install/)\n\nInstallation\n------------\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#installation)\n\nWe recommend starting by cloning [Create Gatsby Theme Publisher](https://github.com/staticfuse/create-gatsby-theme-publisher) which has the publisher theme installed and preconfigured.\n\n1.  `git clone https://github.com/staticfuse/create-gatsby-theme-publisher`\n2.  cd into the folder `cd create-gatsby-theme-publisher`\n3.  Install dependencies `yarn`\n4.  Install [WPGraphQL plugin on your WordPress site](https://github.com/wp-graphql/wp-graphql)\n5.  Configure your site options in [gatsby-config.js](https://github.com/staticfuse/gatsby-theme-publisher/blob/master/demo/gatsby-config.js#L18) Explanation of the options is [below](https://github.com/staticfuse/gatsby-theme-publisher#publisher-theme-options)\n6.  `gatsby develop` to start the local server\n7.  Add your logo and [customize the theme](https://github.com/staticfuse/gatsby-theme-publisher#theme-customization)\n8.  Publish to Netlify or any host.\n\n### Adding Gatsby WordPress Theme Publisher to an existing Gatsby site\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#adding-gatsby-wordpress-theme-publisher-to-an-existing-gatsby-site)\n\nYou can also add this theme to an existing Gatsby site.\n\n1.  `yarn add @staticfuse/gatsby-theme-publisher`\n2.  In your `gatsby-config.js` :\n\n  plugins: \\[\n    {\n      resolve: \\`@staticfuse/gatsby-theme-publisher\\`,\n      options: {\n        starterPages: true,\n        mailChimpEndpoint: 0,\n        dynamicComments: 1,\n        gaTrackingId: 0,\n        wordPressUrl: \\`https://publishertheme.staticfuse.com\\`, // The url of your WordPress install\n        blogURI: '/blog' // Your posts page, change to whatever you'd prefer\n      },\n    },\n  \\],\n\nPublisher Theme Options\n-----------------------\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#publisher-theme-options)\n\nThe following options can be configured in [your site's gatsby-config.js](https://github.com/staticfuse/gatsby-theme-publisher/blob/master/demo/gatsby-config.js#L12)\n\n### Site Metadata\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#site-metadata)\n\nIn demo/gatsby-config.js, edit the siteMetadata object with your site title, url, etc.\n\nNote: `siteUrl` refers to your final website address. `wordPressUrl` in the plugin options refers to the WordPress site. For example, your WordPress site may be hosted at data.mybusiness.com, but your Gatsby site will be at mybusiness.com.\n\n### Plugin Options\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#plugin-options)\n\n  plugins: \\[\n    {\n      resolve: \\`@staticfuse/gatsby-theme-publisher\\`,\n      options: {\n        starterPages: true,\n        dynamicComments: 1,\n        gaTrackingId: 0,\n        wordPressUrl: 'https://data.staticfuse.com',\n        blogURI: '/blog',\n        mailChimpEndpoint: 0,\n        // ...etc\n       },\n    },\n  \\],\n\n| Option | Type | Default | Description |\n| --- | --- | --- | --- |\n| mailChimpEndpoint | string/boolean | 0 | [Your mailchimp endpoint](https://www.gatsbyjs.org/packages/gatsby-plugin-mailchimp/#mailchimp-endpoint). Set to `0` to disable. |\n| dynamicComments | boolean | 1 | Enable or disable dynamic comments. If enabled, anyone can post a comment. |\n| gaTrackingId | string/boolean | 0 | Your google analytics UA code. Set to `0` to disable Google Analytics. |\n| wordPressUrl | string | `\"https://scottbolinger.com\"` | The URL of your WordPress site |\n| blogURI | string | '' | The path prefix on the blog and blog posts. No leading slash. `'/blog'` would result in `https://my-domain.com/blog/` |\n| starterPages | boolean | true | Create a home, about, and contact page in Gatsby. |\n| menuName | string/boolean | 0 | The name of the _WordPress_ menu you'd like to use or `0` if you don't want to render a menu. |\n| publisherMenuConfig | array | \\[\\] | Optional array based way to configure the menu. More info [here](https://github.com/staticfuse/gatsby-theme-publisher#publisher-menu). |\n\nTheme Customization\n-------------------\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#theme-customization)\n\nYou can customize the colors, add or remove pages, and edit template files. All theme customization should happen in the /demo folder. If you are familiar with WordPress, this is like a \"child theme.\"\n\nAny changes you make in the main gatsby-theme-publisher folder will be overwritten by theme updates.\n\n### Logo\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#logo)\n\nTo add your logo, add demo/src/images/site-logo.png.\n\nYou will need to add a folder called images to the demo/src directory, and add your logo file inside with the name site-logo.png. You can make further modifications in the demo/src/components/Logo.js file.\n\n### Customize Theme Colors\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#customize-theme-colors)\n\nOpen demo/src/gatsby-theme-publisher/theme/theme.js\n\nThe theme color defaults are commented out, you can uncommment them and change the value. For example, to change the header background color, change...\n\n`// headerBg: \"#2D3748\"`\n\nto any color, such as...\n\n`headerBg: \"#bada55\"`\n\nYou can also use predefined color values, such as...\n\n`buttonBg: theme.colors.blue['500]`\n\nor\n\n`buttonText: theme.colors.orange['300']`\n\nYou can see those colors and more options [here](https://chakra-ui.com/theme).\n\n### Publisher Menu\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#publisher-menu)\n\nThere are two ways to configure the menu.\n\n#### _1) publisherMenuConfig option (array config)_\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#1-publishermenuconfig-option-array-config)\n\nThis is the default behavior. Theme setting `starterPages` is set to true. Publisher theme will output \"Home\", \"About\" & \"Contact\" with zero config. In the event you wanted to override this, you can add your config to the `publisherMenuConfig` theme option. For instance, if you wanted to add a link to `/portfolio` and child item to \"Contact\" you'd do the following:\n\n  {\n    resolve: '@staticfuse/gatsby-theme-publisher',\n    options: {\n      publisherMenuConfig: \\[\n        {\n          label: 'Home',\n          url: '/',\n          isExternal: false,\n        },\n        {\n          label: 'Blog',\n          url: '/blog',\n          isExternal: false,\n        },\n        {\n          label: 'Portfolio',\n          url: '/portfolio',\n          isExternal: false,\n        },\n        {\n          label: 'Contact',\n          url: '/contact',\n          isExternal: false,\n          childItems: \\[\n            {\n              label: 'I live in the dropdown',\n              url: '/some-url',\n              isExternal: false,\n            },\n          \\],\n        },\n      \\],\n      // More options if so desired...\n    }\n  }\n\nKeep in mind it's up to you to link to a valid page. In the example above, you would need to add a Gatsby page at your-theme/src/pages/portfolio, otherwise when you visit `/portfolio'`, your site will 404.\n\n_What is `isExternal: false`?_\n\nThis tells the Publisher theme and Gatsby wether to navigate to a link client site using Gatsby `<Link/>` or use a `<a>`.\n\n_Client_\n\n{\n  label: 'Blog',\n  url: '/blog',\n  isExternal: false,\n},\n\n_Full page reload_\n\n{\n  label: 'StaticFuse',\n  url: 'https://staticfuse.com',\n  isExternal: true,\n},\n\n#### _2) Use a WordPress menu_\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#2-use-a-wordpress-menu)\n\nYou can manage your menu within the your WordPress site as well. To do so, change Publisher theme setting to: `menuName: 'your menu name'`. For example, the setting for the example (image) below would be: `menuName: 'PRIMARY'` [![Image 11: Gatsby Theme Publisher Screenshot](https://camo.githubusercontent.com/1c539f4da365a24835a4cf8d0b94cfdf8accee6e6e1a80e06480ea23b0262124/68747470733a2f2f7075626c69736865727468656d652e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f6d656e7573732e706e67)](https://camo.githubusercontent.com/1c539f4da365a24835a4cf8d0b94cfdf8accee6e6e1a80e06480ea23b0262124/68747470733a2f2f7075626c69736865727468656d652e737461746963667573652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031392f31302f6d656e7573732e706e67)\n\nIf you set a menu name, Publisher will automatically import your WordPress pages. If no menu name is set, no WordPress pages will be imported. You can override this behavior with the `wpPages` configuration option.\n\nMany WordPress pages will not render properly in Gatsby, so we generally do not recommend this option. It is better to build your pages in Gatsby, and use posts from WordPress.\n\n_Known limitation:_ For _both_ menu managment options, `childItems` are currently only supported _one_ level deep.\n\n### Customize Templates\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#customize-templates)\n\nTo change a page template layout, you can copy the file to the demo folder. For example, to edit the header, you would copy gatsby-theme-publisher/src/components/Header.js into demo/src/components/Header.js and edit the file there. Gatsby will automatically use your header file instead of the default.\n\nThis theme uses [Chakra UI](https://chakra-ui.com/), which gives you a lot of easy to use components. You can use any of these components in your theme templates.\n\nPublishing to Netlify\n---------------------\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#publishing-to-netlify)\n\nNetlify is a static hosting environment that is free to start, and handles Gatsby sites really well. To publish your site on Netlify, first create a new account at [netlify.com](https://netlify.com/).\n\nNext, add your theme project files to a Github repository.\n\nLogin to Netlify and you will see a `New site from git` button at the top right corner of the screen. Click on it and authorize Netlify to use your account. Choose your website repository and it will take you to deploy settings with the below options.\n\n*   Branch to deploy: You can specify a branch to monitor. When you push to that particular branch, only then will Netlify build and deploy the site. The default is master.\n*   Build Command: You can specify the command you want Netlify to run when you push to the above branch. The default is `gatsby build`.\n*   Publish directory: You can specify which folder Netlify should use to host the website. eg. public, dist, build. The default is `public`.\n*   Advanced build settings: If the site needs environment variables to build, you can specify them by clicking on Show advanced and then the New Variable button.\n\nClick on the Deploy site button and Netlify will start the build and deploy process you have specified. You can go to the Deploys tab and see the process unfold in the Deploy log. After a few moments, it will give you the live site URL eg. random-name.netlify.com.\n\nTroubleshooting\n---------------\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#troubleshooting)\n\n### CORS\n\n[](https://github.com/staticfuse/staticfuse?screenshot=true#cors)\n\nThe search functionality makes remote requests to the source WordPress install. Depending on how your server/theme is configured, these requests could be blocked. There are a number of ways to set the [headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) including in a theme or plugin.\n\n_this needs to go in a plugin or in your theme's fuctions.php_\n\n/\\*\\*\n \\* Add headers\n \\*\n \\* @param array $headers existing headers.\n \\*\n \\* @return array\n \\*/\nfunction filter\\_graphql\\_headers( $headers ) {\n\t$headers\\['Access-Control-Allow-Origin'\\]  = '\\*'; // This should be the domain of your Gatsby site.\n\t$headers\\['Access-Control-Allow-Methods'\\] = 'GET, POST, OPTIONS';\n\n\treturn $headers;\n}\nadd\\_filter( 'graphql\\_response\\_headers\\_to\\_send', 'filter\\_graphql\\_headers' );",
  "usage": {
    "tokens": 3362
  }
}
```
