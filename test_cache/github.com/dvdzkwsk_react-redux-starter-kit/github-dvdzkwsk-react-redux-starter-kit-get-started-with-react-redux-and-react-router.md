---
title: GitHub - dvdzkwsk/react-redux-starter-kit: Get started with React, Redux, and React-Router.
description: Get started with React, Redux, and React-Router. Contribute to dvdzkwsk/react-redux-starter-kit development by creating an account on GitHub.
url: https://github.com/dvdzkwsk/react-redux-starter-kit
timestamp: 2025-01-20T15:30:13.797Z
domain: github.com
path: dvdzkwsk_react-redux-starter-kit
---

# GitHub - dvdzkwsk/react-redux-starter-kit: Get started with React, Redux, and React-Router.


Get started with React, Redux, and React-Router. Contribute to dvdzkwsk/react-redux-starter-kit development by creating an account on GitHub.


## Content

Deprecation Warning
-------------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#deprecation-warning)

This project was started at the advent of the Redux ecosystem, and was intended to help users get up and running quickly. Since then, tooling and best practices have evolved tremendously. In order to get the most modern experience possible, I recommend checking out something like [create-react-app](https://github.com/facebookincubator/create-react-app) which is supported by many core React and Redux developers.

You are welcome to use this project if it is a better fit for your needs, but if you are brand new to the ecosystem I highly recommend checking out something that has received more recent updates.

Thank you to everyone who made this project possible over the past year(s).

React Redux Starter Kit
-----------------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#react-redux-starter-kit)

[![Image 24: Build Status](https://camo.githubusercontent.com/fee4425e1d610131b98a93023f777da34e053022fbf3d6c17ac53fccdf7fad97/68747470733a2f2f7472617669732d63692e6f72672f646176657a756b6f2f72656163742d72656475782d737461727465722d6b69742e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/davezuko/react-redux-starter-kit?branch=master) [![Image 25: dependencies](https://camo.githubusercontent.com/b331cb141fb490e25d459a4e24f8f33709d892e36fb53d9a5687b6cb06bdcedf/68747470733a2f2f64617669642d646d2e6f72672f646176657a756b6f2f72656163742d72656475782d737461727465722d6b69742e737667)](https://david-dm.org/davezuko/react-redux-starter-kit) [![Image 26: devDependency Status](https://camo.githubusercontent.com/91398ed31185049d9c2477528f6f65051ff783fbe87815b7e10af8c60c2dcc3d/68747470733a2f2f64617669642d646d2e6f72672f646176657a756b6f2f72656163742d72656475782d737461727465722d6b69742f6465762d7374617475732e737667)](https://david-dm.org/davezuko/react-redux-starter-kit#info=devDependencies) [![Image 27: js-standard-style](https://camo.githubusercontent.com/69491412f56d5c52f0e9f0abddb17033b28539d38e5d05378521222236a83bb1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d7374616e646172642d627269676874677265656e2e737667)](http://standardjs.com/)

This starter kit is designed to get you up and running with a bunch of awesome front-end technologies.

The primary goal of this project is to provide a stable foundation upon which to build modern web appliications. Its purpose is not to dictate your project structure or to demonstrate a complete real-world application, but to provide a set of tools intended to make front-end development robust, easy, and, most importantly, fun. Check out the full feature list below!

Finally, This project wouldn't be possible without the help of our many contributors. What you see today is the product of hundreds changes made to keep up with an ever-evolving ecosystem. [Thank you](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#thank-you) for all of your help.

Table of Contents
-----------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#table-of-contents)

1.  [Requirements](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#requirements)
2.  [Installation](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#getting-started)
3.  [Running the Project](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#running-the-project)
4.  [Project Structure](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#project-structure)
5.  [Live Development](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#local-development)
    *   [Hot Reloading](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#hot-reloading)
    *   [Redux DevTools](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#redux-devtools)
6.  [Routing](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#routing)
7.  [Testing](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#testing)
    *   [dirty-chai](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#dirty-chai)
8.  [Building for Production](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#building-for-production)
9.  [Deployment](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#deployment)
10.  [Thank You](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#thank-you)

Requirements
------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#requirements)

*   node `^5.0.0`
*   yarn `^0.23.0` or npm `^3.0.0`

Installation
------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#installation)

After confirming that your environment meets the above [requirements](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#requirements), you can create a new project based on `react-redux-starter-kit` by doing the following:

$ git clone https://github.com/davezuko/react-redux-starter-kit.git <my-project-name\>
$ cd <my-project-name\>

When that's done, install the project dependencies. It is recommended that you use [Yarn](https://yarnpkg.com/) for deterministic dependency management, but `npm install` will suffice.

$ yarn  # Install project dependencies (or \`npm install\`)

Running the Project
-------------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#running-the-project)

After completing the [installation](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#installation) step, you're ready to start the project!

$ yarn start  # Start the development server (or \`npm start\`)

While developing, you will probably rely mostly on `yarn start`; however, there are additional scripts at your disposal:

| `yarn <script>` | Description |
| --- | --- |
| `start` | Serves your app at `localhost:3000` |
| `build` | Builds the application to ./dist |
| `test` | Runs unit tests with Karma. See [testing](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#testing) |
| `test:watch` | Runs `test` in watch mode to re-run tests when changed |
| `lint` | [Lints](http://stackoverflow.com/questions/8503559/what-is-linting) the project for potential errors |
| `lint:fix` | Lints the project and [fixes all correctable errors](http://eslint.org/docs/user-guide/command-line-interface.html#fix) |

Project Structure
-----------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#project-structure)

The project structure presented in this boilerplate is **fractal**, where functionality is grouped primarily by feature rather than file type. This structure is only meant to serve as a guide, it is by no means prescriptive. That said, it aims to represent generally accepted guidelines and patterns for building scalable applications. If you wish to read more about this pattern, please check out this [awesome writeup](https://github.com/davezuko/react-redux-starter-kit/wiki/Fractal-Project-Structure) by [Justin Greenberg](https://github.com/justingreenberg).

```
.
├── build                    # All build-related code
├── public                   # Static public assets (not imported anywhere in source code)
├── server                   # Express application that provides webpack middleware
│   └── main.js              # Server application entry point
├── src                      # Application source code
│   ├── index.html           # Main HTML page container for app
│   ├── main.js              # Application bootstrap and rendering
│   ├── normalize.js         # Browser normalization and polyfills
│   ├── components           # Global Reusable Components
│   ├── containers           # Global Reusable Container Components
│   ├── layouts              # Components that dictate major page structure
│   │   └── PageLayout       # Global application layout in which to render routes
│   ├── routes               # Main route definitions and async split points
│   │   ├── index.js         # Bootstrap main application routes with store
│   │   ├── Home             # Fractal route
│   │   │   ├── index.js     # Route definitions and async split points
│   │   │   ├── assets       # Assets required to render components
│   │   │   ├── components   # Presentational React Components
│   │   │   └── routes **    # Fractal sub-routes (** optional)
│   │   └── Counter          # Fractal route
│   │       ├── index.js     # Counter route definition
│   │       ├── container    # Connect components to actions and store
│   │       ├── modules      # Collections of reducers/constants/actions
│   │       └── routes **    # Fractal sub-routes (** optional)
│   ├── store                # Redux-specific pieces
│   │   ├── createStore.js   # Create and instrument redux store
│   │   └── reducers.js      # Reducer registry and injection
│   └── styles               # Application-wide styles (generally settings)
└── tests                    # Unit tests
```

Live Development
----------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#live-development)

### Hot Reloading

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#hot-reloading)

Hot reloading is enabled by default when the application is running in development mode (`yarn start`). This feature is implemented with webpack's [Hot Module Replacement](https://webpack.github.io/docs/hot-module-replacement.html) capabilities, where code updates can be injected to the application while it's running, no full reload required. Here's how it works:

*   For **JavaScript** modules, a code change will trigger the application to re-render from the top of the tree. **Global state is preserved (i.e. redux), but any local component state is reset**. This differs from React Hot Loader, but we've found that performing a full re-render helps avoid subtle bugs caused by RHL patching.
    
*   For **Sass**, any change will update the styles in realtime, no additional configuration or reload needed.
    

### Redux DevTools

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#redux-devtools)

**We recommend using the [Redux DevTools Chrome Extension](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd).** Using the chrome extension allows your monitors to run on a separate thread and affords better performance and functionality. It comes with several of the most popular monitors, is easy to configure, filters actions, and doesn't require installing any packages in your project.

However, it's easy to bundle these developer tools locally should you choose to do so. First, grab the packages from npm:

yarn add --dev redux-devtools redux-devtools-log-monitor redux-devtools-dock-monitor

Then follow the [manual integration walkthrough](https://github.com/gaearon/redux-devtools/blob/master/docs/Walkthrough.md).

Routing
-------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#routing)

We use `react-router` [route definitions](https://github.com/ReactTraining/react-router/blob/v3/docs/API.md#plainroute) (`<route>/index.js`) to define units of logic within our application. See the [project structure](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#project-structure) section for more information.

Testing
-------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#testing)

To add a unit test, create a `.spec.js` file anywhere inside of `./tests`. Karma and webpack will automatically find these files, and Mocha and Chai will be available within your test without the need to import them. Here are a few important plugins and packages available to you during testing:

### dirty-chai

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#dirty-chai)

Some of the assertions available from [chai](https://github.com/dvdzkwsk/react-redux-starter-kit/blob/master/chaijs.com) use [magical getters](http://chaijs.com/api/bdd/#method_true). These are problematic for a few reasons:

1.  If you mistype a property name (e.g. `expect(false).to.be.tru`) then the expression evaluates to undefined, the magical getter on the `true` is never run, and so your test silently passes.
2.  By default, linters don't understand them and therefore mark them as unused expressions, which can be annoying.

[Dirty Chai](https://github.com/prodatakey/dirty-chai) fixes this by converting these getters into callable functions. This way, if mistype an assertion, our attempt to invoke it will throw due to the property being undefined.

// This silently passes because the getter on \`true\` is never invoked!
it('should be true', () \=\> {
  expect(false).to.be.tru // evalutes to undefined :(
})

// Much better! Our assertion is invalid, so it throws rather than implicitly passing.
it('should be true', () \=\> {
  expect(false).to.be.tru() // \`tru\` is not defined!
})

Building for Production
-----------------------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#building-for-production)

Deployment
----------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#deployment)

Out of the box, this starter kit is deployable by serving the `./dist` folder generated by `yarn build`. This project does not concern itself with the details of server-side rendering or API structure, since that demands a more opinionated structure that makes it difficult to extend the starter kit. The simplest deployment strategy is a [static deployment](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#static-deployments).

### Static Deployments

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#static-deployments)

Serve the application with a web server such as nginx by pointing it at your `./dist` folder. Make sure to direct incoming route requests to the root `./dist/index.html` file so that the client application will be loaded; react-router will take care of the rest. If you are unsure of how to do this, you might find [this documentation](https://github.com/reactjs/react-router/blob/master/docs/guides/Histories.md#configuring-your-server) helpful. The Express server that comes with the starter kit is able to be extended to serve as an API and more, but is not required for a static deployment.

Thank You
---------

[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#thank-you)

This project wouldn't be possible without help from the community, so I'd like to highlight some of its biggest contributors. Thank you all for your hard work, you've made my life a lot easier and taught me a lot in the process.

*   [Justin Greenberg](https://github.com/justingreenberg) - For all of your PR's, getting us to Babel 6, and constant work improving our patterns.
*   [Roman Pearah](https://github.com/neverfox) - For your bug reports, help in triaging issues, and PR contributions.
*   [Spencer Dixon](https://github.com/SpencerCDixon) - For your creation of [redux-cli](https://github.com/SpencerCDixon/redux-cli).
*   [Jonas Matser](https://github.com/mtsr) - For your help in triaging issues and unending support in our Gitter channel.

And to everyone else who has contributed, even if you are not listed here your work is appreciated.

## Metadata

```json
{
  "title": "GitHub - dvdzkwsk/react-redux-starter-kit: Get started with React, Redux, and React-Router.",
  "description": "Get started with React, Redux, and React-Router. Contribute to dvdzkwsk/react-redux-starter-kit development by creating an account on GitHub.",
  "url": "https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true",
  "content": "Deprecation Warning\n-------------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#deprecation-warning)\n\nThis project was started at the advent of the Redux ecosystem, and was intended to help users get up and running quickly. Since then, tooling and best practices have evolved tremendously. In order to get the most modern experience possible, I recommend checking out something like [create-react-app](https://github.com/facebookincubator/create-react-app) which is supported by many core React and Redux developers.\n\nYou are welcome to use this project if it is a better fit for your needs, but if you are brand new to the ecosystem I highly recommend checking out something that has received more recent updates.\n\nThank you to everyone who made this project possible over the past year(s).\n\nReact Redux Starter Kit\n-----------------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#react-redux-starter-kit)\n\n[![Image 24: Build Status](https://camo.githubusercontent.com/fee4425e1d610131b98a93023f777da34e053022fbf3d6c17ac53fccdf7fad97/68747470733a2f2f7472617669732d63692e6f72672f646176657a756b6f2f72656163742d72656475782d737461727465722d6b69742e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/davezuko/react-redux-starter-kit?branch=master) [![Image 25: dependencies](https://camo.githubusercontent.com/b331cb141fb490e25d459a4e24f8f33709d892e36fb53d9a5687b6cb06bdcedf/68747470733a2f2f64617669642d646d2e6f72672f646176657a756b6f2f72656163742d72656475782d737461727465722d6b69742e737667)](https://david-dm.org/davezuko/react-redux-starter-kit) [![Image 26: devDependency Status](https://camo.githubusercontent.com/91398ed31185049d9c2477528f6f65051ff783fbe87815b7e10af8c60c2dcc3d/68747470733a2f2f64617669642d646d2e6f72672f646176657a756b6f2f72656163742d72656475782d737461727465722d6b69742f6465762d7374617475732e737667)](https://david-dm.org/davezuko/react-redux-starter-kit#info=devDependencies) [![Image 27: js-standard-style](https://camo.githubusercontent.com/69491412f56d5c52f0e9f0abddb17033b28539d38e5d05378521222236a83bb1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d7374616e646172642d627269676874677265656e2e737667)](http://standardjs.com/)\n\nThis starter kit is designed to get you up and running with a bunch of awesome front-end technologies.\n\nThe primary goal of this project is to provide a stable foundation upon which to build modern web appliications. Its purpose is not to dictate your project structure or to demonstrate a complete real-world application, but to provide a set of tools intended to make front-end development robust, easy, and, most importantly, fun. Check out the full feature list below!\n\nFinally, This project wouldn't be possible without the help of our many contributors. What you see today is the product of hundreds changes made to keep up with an ever-evolving ecosystem. [Thank you](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#thank-you) for all of your help.\n\nTable of Contents\n-----------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#table-of-contents)\n\n1.  [Requirements](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#requirements)\n2.  [Installation](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#getting-started)\n3.  [Running the Project](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#running-the-project)\n4.  [Project Structure](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#project-structure)\n5.  [Live Development](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#local-development)\n    *   [Hot Reloading](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#hot-reloading)\n    *   [Redux DevTools](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#redux-devtools)\n6.  [Routing](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#routing)\n7.  [Testing](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#testing)\n    *   [dirty-chai](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#dirty-chai)\n8.  [Building for Production](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#building-for-production)\n9.  [Deployment](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#deployment)\n10.  [Thank You](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#thank-you)\n\nRequirements\n------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#requirements)\n\n*   node `^5.0.0`\n*   yarn `^0.23.0` or npm `^3.0.0`\n\nInstallation\n------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#installation)\n\nAfter confirming that your environment meets the above [requirements](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#requirements), you can create a new project based on `react-redux-starter-kit` by doing the following:\n\n$ git clone https://github.com/davezuko/react-redux-starter-kit.git <my-project-name\\>\n$ cd <my-project-name\\>\n\nWhen that's done, install the project dependencies. It is recommended that you use [Yarn](https://yarnpkg.com/) for deterministic dependency management, but `npm install` will suffice.\n\n$ yarn  # Install project dependencies (or \\`npm install\\`)\n\nRunning the Project\n-------------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#running-the-project)\n\nAfter completing the [installation](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#installation) step, you're ready to start the project!\n\n$ yarn start  # Start the development server (or \\`npm start\\`)\n\nWhile developing, you will probably rely mostly on `yarn start`; however, there are additional scripts at your disposal:\n\n| `yarn <script>` | Description |\n| --- | --- |\n| `start` | Serves your app at `localhost:3000` |\n| `build` | Builds the application to ./dist |\n| `test` | Runs unit tests with Karma. See [testing](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#testing) |\n| `test:watch` | Runs `test` in watch mode to re-run tests when changed |\n| `lint` | [Lints](http://stackoverflow.com/questions/8503559/what-is-linting) the project for potential errors |\n| `lint:fix` | Lints the project and [fixes all correctable errors](http://eslint.org/docs/user-guide/command-line-interface.html#fix) |\n\nProject Structure\n-----------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#project-structure)\n\nThe project structure presented in this boilerplate is **fractal**, where functionality is grouped primarily by feature rather than file type. This structure is only meant to serve as a guide, it is by no means prescriptive. That said, it aims to represent generally accepted guidelines and patterns for building scalable applications. If you wish to read more about this pattern, please check out this [awesome writeup](https://github.com/davezuko/react-redux-starter-kit/wiki/Fractal-Project-Structure) by [Justin Greenberg](https://github.com/justingreenberg).\n\n```\n.\n├── build                    # All build-related code\n├── public                   # Static public assets (not imported anywhere in source code)\n├── server                   # Express application that provides webpack middleware\n│   └── main.js              # Server application entry point\n├── src                      # Application source code\n│   ├── index.html           # Main HTML page container for app\n│   ├── main.js              # Application bootstrap and rendering\n│   ├── normalize.js         # Browser normalization and polyfills\n│   ├── components           # Global Reusable Components\n│   ├── containers           # Global Reusable Container Components\n│   ├── layouts              # Components that dictate major page structure\n│   │   └── PageLayout       # Global application layout in which to render routes\n│   ├── routes               # Main route definitions and async split points\n│   │   ├── index.js         # Bootstrap main application routes with store\n│   │   ├── Home             # Fractal route\n│   │   │   ├── index.js     # Route definitions and async split points\n│   │   │   ├── assets       # Assets required to render components\n│   │   │   ├── components   # Presentational React Components\n│   │   │   └── routes **    # Fractal sub-routes (** optional)\n│   │   └── Counter          # Fractal route\n│   │       ├── index.js     # Counter route definition\n│   │       ├── container    # Connect components to actions and store\n│   │       ├── modules      # Collections of reducers/constants/actions\n│   │       └── routes **    # Fractal sub-routes (** optional)\n│   ├── store                # Redux-specific pieces\n│   │   ├── createStore.js   # Create and instrument redux store\n│   │   └── reducers.js      # Reducer registry and injection\n│   └── styles               # Application-wide styles (generally settings)\n└── tests                    # Unit tests\n```\n\nLive Development\n----------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#live-development)\n\n### Hot Reloading\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#hot-reloading)\n\nHot reloading is enabled by default when the application is running in development mode (`yarn start`). This feature is implemented with webpack's [Hot Module Replacement](https://webpack.github.io/docs/hot-module-replacement.html) capabilities, where code updates can be injected to the application while it's running, no full reload required. Here's how it works:\n\n*   For **JavaScript** modules, a code change will trigger the application to re-render from the top of the tree. **Global state is preserved (i.e. redux), but any local component state is reset**. This differs from React Hot Loader, but we've found that performing a full re-render helps avoid subtle bugs caused by RHL patching.\n    \n*   For **Sass**, any change will update the styles in realtime, no additional configuration or reload needed.\n    \n\n### Redux DevTools\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#redux-devtools)\n\n**We recommend using the [Redux DevTools Chrome Extension](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd).** Using the chrome extension allows your monitors to run on a separate thread and affords better performance and functionality. It comes with several of the most popular monitors, is easy to configure, filters actions, and doesn't require installing any packages in your project.\n\nHowever, it's easy to bundle these developer tools locally should you choose to do so. First, grab the packages from npm:\n\nyarn add --dev redux-devtools redux-devtools-log-monitor redux-devtools-dock-monitor\n\nThen follow the [manual integration walkthrough](https://github.com/gaearon/redux-devtools/blob/master/docs/Walkthrough.md).\n\nRouting\n-------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#routing)\n\nWe use `react-router` [route definitions](https://github.com/ReactTraining/react-router/blob/v3/docs/API.md#plainroute) (`<route>/index.js`) to define units of logic within our application. See the [project structure](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#project-structure) section for more information.\n\nTesting\n-------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#testing)\n\nTo add a unit test, create a `.spec.js` file anywhere inside of `./tests`. Karma and webpack will automatically find these files, and Mocha and Chai will be available within your test without the need to import them. Here are a few important plugins and packages available to you during testing:\n\n### dirty-chai\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#dirty-chai)\n\nSome of the assertions available from [chai](https://github.com/dvdzkwsk/react-redux-starter-kit/blob/master/chaijs.com) use [magical getters](http://chaijs.com/api/bdd/#method_true). These are problematic for a few reasons:\n\n1.  If you mistype a property name (e.g. `expect(false).to.be.tru`) then the expression evaluates to undefined, the magical getter on the `true` is never run, and so your test silently passes.\n2.  By default, linters don't understand them and therefore mark them as unused expressions, which can be annoying.\n\n[Dirty Chai](https://github.com/prodatakey/dirty-chai) fixes this by converting these getters into callable functions. This way, if mistype an assertion, our attempt to invoke it will throw due to the property being undefined.\n\n// This silently passes because the getter on \\`true\\` is never invoked!\nit('should be true', () \\=\\> {\n  expect(false).to.be.tru // evalutes to undefined :(\n})\n\n// Much better! Our assertion is invalid, so it throws rather than implicitly passing.\nit('should be true', () \\=\\> {\n  expect(false).to.be.tru() // \\`tru\\` is not defined!\n})\n\nBuilding for Production\n-----------------------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#building-for-production)\n\nDeployment\n----------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#deployment)\n\nOut of the box, this starter kit is deployable by serving the `./dist` folder generated by `yarn build`. This project does not concern itself with the details of server-side rendering or API structure, since that demands a more opinionated structure that makes it difficult to extend the starter kit. The simplest deployment strategy is a [static deployment](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#static-deployments).\n\n### Static Deployments\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#static-deployments)\n\nServe the application with a web server such as nginx by pointing it at your `./dist` folder. Make sure to direct incoming route requests to the root `./dist/index.html` file so that the client application will be loaded; react-router will take care of the rest. If you are unsure of how to do this, you might find [this documentation](https://github.com/reactjs/react-router/blob/master/docs/guides/Histories.md#configuring-your-server) helpful. The Express server that comes with the starter kit is able to be extended to serve as an API and more, but is not required for a static deployment.\n\nThank You\n---------\n\n[](https://github.com/dvdzkwsk/react-redux-starter-kit?screenshot=true#thank-you)\n\nThis project wouldn't be possible without help from the community, so I'd like to highlight some of its biggest contributors. Thank you all for your hard work, you've made my life a lot easier and taught me a lot in the process.\n\n*   [Justin Greenberg](https://github.com/justingreenberg) - For all of your PR's, getting us to Babel 6, and constant work improving our patterns.\n*   [Roman Pearah](https://github.com/neverfox) - For your bug reports, help in triaging issues, and PR contributions.\n*   [Spencer Dixon](https://github.com/SpencerCDixon) - For your creation of [redux-cli](https://github.com/SpencerCDixon/redux-cli).\n*   [Jonas Matser](https://github.com/mtsr) - For your help in triaging issues and unending support in our Gitter channel.\n\nAnd to everyone else who has contributed, even if you are not listed here your work is appreciated.",
  "usage": {
    "tokens": 3796
  }
}
```
