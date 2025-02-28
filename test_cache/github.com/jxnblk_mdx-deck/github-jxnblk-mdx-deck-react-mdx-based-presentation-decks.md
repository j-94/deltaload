---
title: GitHub - jxnblk/mdx-deck: ♠️ React MDX-based presentation decks
description: ♠️ React MDX-based presentation decks. Contribute to jxnblk/mdx-deck development by creating an account on GitHub.
url: https://github.com/jxnblk/mdx-deck
timestamp: 2025-01-20T15:30:53.492Z
domain: github.com
path: jxnblk_mdx-deck
---

# GitHub - jxnblk/mdx-deck: ♠️ React MDX-based presentation decks


♠️ React MDX-based presentation decks. Contribute to jxnblk/mdx-deck development by creating an account on GitHub.


## Content

[![Image 40](https://camo.githubusercontent.com/de62f36a8901fefd6b7298ee38b4659101dca687b8e2b7d6b922a66d8cc70750/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6a786e626c6b2f6d64782d6465636b2d322e676966)](https://camo.githubusercontent.com/de62f36a8901fefd6b7298ee38b4659101dca687b8e2b7d6b922a66d8cc70750/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6a786e626c6b2f6d64782d6465636b2d322e676966)

MDX Deck [![Image 41](https://github.com/jxnblk/mdx-deck/raw/master/docs/ace.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/ace.png)
-----------------------------------------------------------------------------------------------------------------------------------------------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#mdx-deck-)

Award-winning React [MDX](https://mdxjs.com/)\-based presentation decks

[![Image 42: Build Status](https://camo.githubusercontent.com/0b81cc9df6da7fe97c6cf55406e88afe994a62cdae95424bdc55f028a773497f/68747470733a2f2f666c61742e62616467656e2e6e65742f6769746875622f7374617475732f6a786e626c6b2f6d64782d6465636b2f6d61737465722f63692f636972636c656369)](https://circleci.com/gh/jxnblk/mdx-deck) [![Image 43: Version](https://camo.githubusercontent.com/73d34db878b1ebeff43d9cee4bd91c2dbcccc0903c34c359899e74e77ea3bd58/68747470733a2f2f666c61742e62616467656e2e6e65742f6e706d2f762f6d64782d6465636b)](https://npmjs.com/package/mdx-deck) [![Image 44: Downloads](https://camo.githubusercontent.com/e481760c9f0565d3032687e34d0d68a8f25d01c246b601b61728fcf2f9cc3ea5/68747470733a2f2f666c61742e62616467656e2e6e65742f6e706d2f646d2f6d64782d6465636b)](https://npmjs.com/package/mdx-deck)

*   📝 Write presentations in markdown
*   ⚛️ Import and use [React components](https://github.com/jxnblk/mdx-deck?screenshot=true#imports)
*   💅 Customizable [themes](https://github.com/jxnblk/mdx-deck?screenshot=true#theming) and components
*   0️⃣ Zero-config CLI
*   💁‍♀️ [Presenter mode](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode)
*   📓 [Speaker notes](https://github.com/jxnblk/mdx-deck?screenshot=true#speaker-notes)

[View demo](https://mdx-deck.jxnblk.com/)

*   [Getting Started](https://github.com/jxnblk/mdx-deck?screenshot=true#getting-started)
*   [Using MDX](https://github.com/jxnblk/mdx-deck?screenshot=true#using-mdx)
*   [Theming](https://github.com/jxnblk/mdx-deck?screenshot=true#theming)
*   [Components](https://github.com/jxnblk/mdx-deck?screenshot=true#components)
*   [Layouts](https://github.com/jxnblk/mdx-deck?screenshot=true#layouts)
*   [Presenter Mode](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode)
*   [Keyboard Shortcuts](https://github.com/jxnblk/mdx-deck?screenshot=true#keyboard-shortcuts)
*   [CLI Options](https://github.com/jxnblk/mdx-deck?screenshot=true#cli-options)
*   [Videos & Articles](https://github.com/jxnblk/mdx-deck?screenshot=true#videos-articles)
*   [Examples](https://github.com/jxnblk/mdx-deck?screenshot=true#examples)

Getting Started
---------------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#getting-started)

Create an [MDX](https://mdxjs.com/) file and separate each slide with `---`.

\# Hello

\---

\## This is my deck

\---

\## The End

Add a run script to your `package.json` with the MDX Deck CLI pointing to the `.mdx` file to start the development server:

"scripts": {
  "start": "mdx-deck deck.mdx"
}

Start the development server:

Use the left and right arrow keys to navigate through the presentation.

Using MDX
---------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#using-mdx)

MDX uses Markdown syntax and can render React components inline with JSX.

### Imports

[](https://github.com/jxnblk/mdx-deck?screenshot=true#imports)

To import components, use ES import syntax separated with empty lines between any markdown or JSX syntax.

import { Box } from 'theme-ui'

<Box color\="tomato"\>Hello</Box\>

Read more about MDX syntax in the [MDX Docs](https://mdxjs.com/).

Theming
-------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#theming)

[![Image 45](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/future.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/future.png) [![Image 46](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/comic.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/comic.png) [![Image 47](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/yellow.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/yellow.png)

MDX Deck uses [Theme UI](https://theme-ui.com/) and [Emotion](https://emotion.sh/) for styling, making practically any part of the presentation themeable. It also includes several built-in themes to change the look and feel of the presentation.

*   See the list of available [Themes](https://github.com/jxnblk/mdx-deck/blob/master/docs/themes.md)
*   Read more about theming in the [Theming docs](https://github.com/jxnblk/mdx-deck/blob/master/docs/theming.md).

Components
----------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#components)

MDX Deck includes built-in components to help with creating presentations, a `Notes` component for adding speaker notes, a `Head` component for the document head, `Header` and `Footer` components for persistent header and footer content, and a `Steps` component for adding multiple intermediate steps in a single slide.

Read more in the [Components](https://github.com/jxnblk/mdx-deck/blob/master/docs/components.md) docs.

### Third-Party Components

[](https://github.com/jxnblk/mdx-deck?screenshot=true#third-party-components)

These optional libraries are intended for use with MDX Deck.

*   [CodeSurfer](https://github.com/pomber/code-surfer): React component for scrolling, zooming and highlighting code.
*   [mdx-code](https://github.com/pranaygp/mdx-code): Runnable code playgrounds for MDX Deck.
*   [mdx-deck-live-code](https://github.com/JReinhold/mdx-deck-live-code): Live React and JS coding in slides.

_Note: please check with version compatibility when using these libraries._

Layouts
-------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#layouts)

Each slide can include a custom layout around its content, which can be used as a _template_ for visually differentiating slides.

// example Layout.js
import React from 'react'

export default ({ children }) \=\> (
  <div
    style\={{
      width: '100vw',
      height: '100vh',
      backgroundColor: 'tomato',
    }}\>
    {children}
  </div\>
)

import Layout from './Layout'

\# No Layout

\---

<Layout\>

\# Custom Layout

</Layout\>

The layout component will wrap the MDX elements within that slide, which means you can add custom layout styles or style child elements with CSS-in-JS.

Presenter Mode
--------------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode)

Press `Option + P` to toggle _Presenter Mode_, which will show a preview of the next slide, a timer, and speaker notes.

[![Image 48: presenter mode screenshot](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/presenter-mode.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/presenter-mode.png)

The presentation can be opened in two separate windows at the same time, and it will stay in sync with the other window.

Keyboard Shortcuts
------------------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#keyboard-shortcuts)

| Key | Description |
| --- | --- |
| Left Arrow, Page Up, Shift + Space | Go to previous slide (or step in [Steps](https://github.com/jxnblk/mdx-deck/blob/master/docs/components.md#steps)) |
| Right Arrow, Page Down, Space | Go to next slide (or step in [Steps](https://github.com/jxnblk/mdx-deck/blob/master/docs/components.md#steps)) |
| Option + P | Toggle [Presenter Mode](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode) |
| Option + O | Toggle Overview Mode |
| Option + G | Toggle Grid Mode |

CLI Options
-----------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#cli-options)

```
-p --port     Dev server port
-h --host     Host the dev server listens to
--no-open     Prevent from opening in default browser
```

Videos & Articles
-----------------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#videos--articles)

*   [Egghead Tutorial](https://egghead.io/lessons/react-build-a-slide-deck-with-mdx-deck-using-markdown-react) by [Andrew Del Prete](https://github.com/andrewdelprete).
*   [mdx-deck: slide decks powered by markdown and react](https://kentcdodds.com/blog/mdx-deck-slide-decks-powered-by-markdown-and-react) by [Kent C. Dodds](https://mobile.twitter.com/kentcdodds)
*   [Make Fast & Beautiful Presentations with MDX-Deck](https://www.youtube.com/watch?v=LvP2EqCiQMg&feature=youtu.be) by [Harry Wolff](https://mobile.twitter.com/hswolff) ([Demo](https://github.com/hswolff/mdx-deck-demo))
*   [What is MDX](http://youtu.be/d2sQiI5NFAM?a) by [Kent C. Dodds](https://mobile.twitter.com/kentcdodds)
*   [Build a Custom Provider Component for MDX-Deck](https://egghead.io/lessons/javascript-build-a-custom-provider-component-for-mdx-deck) by [Kyle Shevlin](https://twitter.com/kyleshevlin)

Examples
--------

[](https://github.com/jxnblk/mdx-deck?screenshot=true#examples)

See how others have used MDX Deck for their presentations.

*   [Design Systems & React](https://github-ds.now.sh/#0) by [Diana Mounter](https://mobile.twitter.com/broccolini)
*   [Bringing Brazil to the Cloud, Now](https://braziljs.now.sh/) by [Guillermo Rauch](https://mobile.twitter.com/rauchg/)
*   [Simplify React](https://simply-react.netlify.com/#0) by [Kent C. Dodds](https://mobile.twitter.com/kentcdodds)
*   [I Got 99 Problems but GraphQL Ain't One](https://99-problems-graphql-aint-one.now.sh/#0) by [Sara Vieira](https://mobile.twitter.com/NikkitaFTW)
*   [Stop de #divFest](https://stop-div-fest.now.sh/) by [Sara Vieira](https://mobile.twitter.com/NikkitaFTW)
*   [MDX, authors and richer JAMstack content](https://mdx-talk.developermode.com/) by [Josh Dzielak](https://mobile.twitter.com/dzello)
*   [Components as Data: A Cross Platform GraphQL Powered Component API](https://componentsasdata.lukeherrington.com/) by [Luke Herrington](https://mobile.twitter.com/lukeherrington)
*   [A short history of webdevs future 🔮](https://webdev-intro.talks.hoverbaum.net/) by [Hendrik Wallbaum](https://github.com/hoverbaum)

### Usage Examples

[](https://github.com/jxnblk/mdx-deck?screenshot=true#usage-examples)

The following examples will open in CodeSandbox.

*   [Basic Example](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/basic)
*   [Syntax Highlighting](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/syntax-highlighting)
*   [Steps](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/steps)
*   [Head](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/head)
*   [Header & Footer](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/header-footer)

* * *

### Related

[](https://github.com/jxnblk/mdx-deck?screenshot=true#related)

*   [MDX](https://mdxjs.com/)
*   [Gatsby](https://gatsbyjs.org/)
*   [Theme UI](https://theme-ui.com/)
*   [Emotion](https://emotion.sh/)
*   [Spectacle](https://github.com/FormidableLabs/spectacle)

[MIT License](https://github.com/jxnblk/mdx-deck/blob/master/LICENSE.md)

## Metadata

```json
{
  "title": "GitHub - jxnblk/mdx-deck: ♠️ React MDX-based presentation decks",
  "description": "♠️ React MDX-based presentation decks. Contribute to jxnblk/mdx-deck development by creating an account on GitHub.",
  "url": "https://github.com/jxnblk/mdx-deck?screenshot=true",
  "content": "[![Image 40](https://camo.githubusercontent.com/de62f36a8901fefd6b7298ee38b4659101dca687b8e2b7d6b922a66d8cc70750/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6a786e626c6b2f6d64782d6465636b2d322e676966)](https://camo.githubusercontent.com/de62f36a8901fefd6b7298ee38b4659101dca687b8e2b7d6b922a66d8cc70750/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6a786e626c6b2f6d64782d6465636b2d322e676966)\n\nMDX Deck [![Image 41](https://github.com/jxnblk/mdx-deck/raw/master/docs/ace.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/ace.png)\n-----------------------------------------------------------------------------------------------------------------------------------------------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#mdx-deck-)\n\nAward-winning React [MDX](https://mdxjs.com/)\\-based presentation decks\n\n[![Image 42: Build Status](https://camo.githubusercontent.com/0b81cc9df6da7fe97c6cf55406e88afe994a62cdae95424bdc55f028a773497f/68747470733a2f2f666c61742e62616467656e2e6e65742f6769746875622f7374617475732f6a786e626c6b2f6d64782d6465636b2f6d61737465722f63692f636972636c656369)](https://circleci.com/gh/jxnblk/mdx-deck) [![Image 43: Version](https://camo.githubusercontent.com/73d34db878b1ebeff43d9cee4bd91c2dbcccc0903c34c359899e74e77ea3bd58/68747470733a2f2f666c61742e62616467656e2e6e65742f6e706d2f762f6d64782d6465636b)](https://npmjs.com/package/mdx-deck) [![Image 44: Downloads](https://camo.githubusercontent.com/e481760c9f0565d3032687e34d0d68a8f25d01c246b601b61728fcf2f9cc3ea5/68747470733a2f2f666c61742e62616467656e2e6e65742f6e706d2f646d2f6d64782d6465636b)](https://npmjs.com/package/mdx-deck)\n\n*   📝 Write presentations in markdown\n*   ⚛️ Import and use [React components](https://github.com/jxnblk/mdx-deck?screenshot=true#imports)\n*   💅 Customizable [themes](https://github.com/jxnblk/mdx-deck?screenshot=true#theming) and components\n*   0️⃣ Zero-config CLI\n*   💁‍♀️ [Presenter mode](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode)\n*   📓 [Speaker notes](https://github.com/jxnblk/mdx-deck?screenshot=true#speaker-notes)\n\n[View demo](https://mdx-deck.jxnblk.com/)\n\n*   [Getting Started](https://github.com/jxnblk/mdx-deck?screenshot=true#getting-started)\n*   [Using MDX](https://github.com/jxnblk/mdx-deck?screenshot=true#using-mdx)\n*   [Theming](https://github.com/jxnblk/mdx-deck?screenshot=true#theming)\n*   [Components](https://github.com/jxnblk/mdx-deck?screenshot=true#components)\n*   [Layouts](https://github.com/jxnblk/mdx-deck?screenshot=true#layouts)\n*   [Presenter Mode](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode)\n*   [Keyboard Shortcuts](https://github.com/jxnblk/mdx-deck?screenshot=true#keyboard-shortcuts)\n*   [CLI Options](https://github.com/jxnblk/mdx-deck?screenshot=true#cli-options)\n*   [Videos & Articles](https://github.com/jxnblk/mdx-deck?screenshot=true#videos-articles)\n*   [Examples](https://github.com/jxnblk/mdx-deck?screenshot=true#examples)\n\nGetting Started\n---------------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#getting-started)\n\nCreate an [MDX](https://mdxjs.com/) file and separate each slide with `---`.\n\n\\# Hello\n\n\\---\n\n\\## This is my deck\n\n\\---\n\n\\## The End\n\nAdd a run script to your `package.json` with the MDX Deck CLI pointing to the `.mdx` file to start the development server:\n\n\"scripts\": {\n  \"start\": \"mdx-deck deck.mdx\"\n}\n\nStart the development server:\n\nUse the left and right arrow keys to navigate through the presentation.\n\nUsing MDX\n---------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#using-mdx)\n\nMDX uses Markdown syntax and can render React components inline with JSX.\n\n### Imports\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#imports)\n\nTo import components, use ES import syntax separated with empty lines between any markdown or JSX syntax.\n\nimport { Box } from 'theme-ui'\n\n<Box color\\=\"tomato\"\\>Hello</Box\\>\n\nRead more about MDX syntax in the [MDX Docs](https://mdxjs.com/).\n\nTheming\n-------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#theming)\n\n[![Image 45](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/future.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/future.png) [![Image 46](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/comic.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/comic.png) [![Image 47](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/yellow.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/yellow.png)\n\nMDX Deck uses [Theme UI](https://theme-ui.com/) and [Emotion](https://emotion.sh/) for styling, making practically any part of the presentation themeable. It also includes several built-in themes to change the look and feel of the presentation.\n\n*   See the list of available [Themes](https://github.com/jxnblk/mdx-deck/blob/master/docs/themes.md)\n*   Read more about theming in the [Theming docs](https://github.com/jxnblk/mdx-deck/blob/master/docs/theming.md).\n\nComponents\n----------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#components)\n\nMDX Deck includes built-in components to help with creating presentations, a `Notes` component for adding speaker notes, a `Head` component for the document head, `Header` and `Footer` components for persistent header and footer content, and a `Steps` component for adding multiple intermediate steps in a single slide.\n\nRead more in the [Components](https://github.com/jxnblk/mdx-deck/blob/master/docs/components.md) docs.\n\n### Third-Party Components\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#third-party-components)\n\nThese optional libraries are intended for use with MDX Deck.\n\n*   [CodeSurfer](https://github.com/pomber/code-surfer): React component for scrolling, zooming and highlighting code.\n*   [mdx-code](https://github.com/pranaygp/mdx-code): Runnable code playgrounds for MDX Deck.\n*   [mdx-deck-live-code](https://github.com/JReinhold/mdx-deck-live-code): Live React and JS coding in slides.\n\n_Note: please check with version compatibility when using these libraries._\n\nLayouts\n-------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#layouts)\n\nEach slide can include a custom layout around its content, which can be used as a _template_ for visually differentiating slides.\n\n// example Layout.js\nimport React from 'react'\n\nexport default ({ children }) \\=\\> (\n  <div\n    style\\={{\n      width: '100vw',\n      height: '100vh',\n      backgroundColor: 'tomato',\n    }}\\>\n    {children}\n  </div\\>\n)\n\nimport Layout from './Layout'\n\n\\# No Layout\n\n\\---\n\n<Layout\\>\n\n\\# Custom Layout\n\n</Layout\\>\n\nThe layout component will wrap the MDX elements within that slide, which means you can add custom layout styles or style child elements with CSS-in-JS.\n\nPresenter Mode\n--------------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode)\n\nPress `Option + P` to toggle _Presenter Mode_, which will show a preview of the next slide, a timer, and speaker notes.\n\n[![Image 48: presenter mode screenshot](https://github.com/jxnblk/mdx-deck/raw/master/docs/images/presenter-mode.png)](https://github.com/jxnblk/mdx-deck/blob/master/docs/images/presenter-mode.png)\n\nThe presentation can be opened in two separate windows at the same time, and it will stay in sync with the other window.\n\nKeyboard Shortcuts\n------------------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#keyboard-shortcuts)\n\n| Key | Description |\n| --- | --- |\n| Left Arrow, Page Up, Shift + Space | Go to previous slide (or step in [Steps](https://github.com/jxnblk/mdx-deck/blob/master/docs/components.md#steps)) |\n| Right Arrow, Page Down, Space | Go to next slide (or step in [Steps](https://github.com/jxnblk/mdx-deck/blob/master/docs/components.md#steps)) |\n| Option + P | Toggle [Presenter Mode](https://github.com/jxnblk/mdx-deck?screenshot=true#presenter-mode) |\n| Option + O | Toggle Overview Mode |\n| Option + G | Toggle Grid Mode |\n\nCLI Options\n-----------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#cli-options)\n\n```\n-p --port     Dev server port\n-h --host     Host the dev server listens to\n--no-open     Prevent from opening in default browser\n```\n\nVideos & Articles\n-----------------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#videos--articles)\n\n*   [Egghead Tutorial](https://egghead.io/lessons/react-build-a-slide-deck-with-mdx-deck-using-markdown-react) by [Andrew Del Prete](https://github.com/andrewdelprete).\n*   [mdx-deck: slide decks powered by markdown and react](https://kentcdodds.com/blog/mdx-deck-slide-decks-powered-by-markdown-and-react) by [Kent C. Dodds](https://mobile.twitter.com/kentcdodds)\n*   [Make Fast & Beautiful Presentations with MDX-Deck](https://www.youtube.com/watch?v=LvP2EqCiQMg&feature=youtu.be) by [Harry Wolff](https://mobile.twitter.com/hswolff) ([Demo](https://github.com/hswolff/mdx-deck-demo))\n*   [What is MDX](http://youtu.be/d2sQiI5NFAM?a) by [Kent C. Dodds](https://mobile.twitter.com/kentcdodds)\n*   [Build a Custom Provider Component for MDX-Deck](https://egghead.io/lessons/javascript-build-a-custom-provider-component-for-mdx-deck) by [Kyle Shevlin](https://twitter.com/kyleshevlin)\n\nExamples\n--------\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#examples)\n\nSee how others have used MDX Deck for their presentations.\n\n*   [Design Systems & React](https://github-ds.now.sh/#0) by [Diana Mounter](https://mobile.twitter.com/broccolini)\n*   [Bringing Brazil to the Cloud, Now](https://braziljs.now.sh/) by [Guillermo Rauch](https://mobile.twitter.com/rauchg/)\n*   [Simplify React](https://simply-react.netlify.com/#0) by [Kent C. Dodds](https://mobile.twitter.com/kentcdodds)\n*   [I Got 99 Problems but GraphQL Ain't One](https://99-problems-graphql-aint-one.now.sh/#0) by [Sara Vieira](https://mobile.twitter.com/NikkitaFTW)\n*   [Stop de #divFest](https://stop-div-fest.now.sh/) by [Sara Vieira](https://mobile.twitter.com/NikkitaFTW)\n*   [MDX, authors and richer JAMstack content](https://mdx-talk.developermode.com/) by [Josh Dzielak](https://mobile.twitter.com/dzello)\n*   [Components as Data: A Cross Platform GraphQL Powered Component API](https://componentsasdata.lukeherrington.com/) by [Luke Herrington](https://mobile.twitter.com/lukeherrington)\n*   [A short history of webdevs future 🔮](https://webdev-intro.talks.hoverbaum.net/) by [Hendrik Wallbaum](https://github.com/hoverbaum)\n\n### Usage Examples\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#usage-examples)\n\nThe following examples will open in CodeSandbox.\n\n*   [Basic Example](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/basic)\n*   [Syntax Highlighting](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/syntax-highlighting)\n*   [Steps](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/steps)\n*   [Head](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/head)\n*   [Header & Footer](https://codesandbox.io/s/github/jxnblk/mdx-deck/tree/master/examples/header-footer)\n\n* * *\n\n### Related\n\n[](https://github.com/jxnblk/mdx-deck?screenshot=true#related)\n\n*   [MDX](https://mdxjs.com/)\n*   [Gatsby](https://gatsbyjs.org/)\n*   [Theme UI](https://theme-ui.com/)\n*   [Emotion](https://emotion.sh/)\n*   [Spectacle](https://github.com/FormidableLabs/spectacle)\n\n[MIT License](https://github.com/jxnblk/mdx-deck/blob/master/LICENSE.md)",
  "usage": {
    "tokens": 3286
  }
}
```
