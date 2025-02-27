---
title: GitHub - argyleink/transition.css: :octocat: Drop-in CSS transitions
description: :octocat: Drop-in CSS transitions. Contribute to argyleink/transition.css development by creating an account on GitHub.
url: https://github.com/argyleink/transition.css
timestamp: 2025-01-20T15:31:59.456Z
domain: github.com
path: argyleink_transition.css
---

# GitHub - argyleink/transition.css: :octocat: Drop-in CSS transitions


:octocat: Drop-in CSS transitions. Contribute to argyleink/transition.css development by creating an account on GitHub.


## Content

[![Image 32: Total Downloads](https://camo.githubusercontent.com/6a72d0eb66635207b9101fefa766aaad4aac9753c473fa7400326adc885df691/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64742f7472616e736974696f6e2e6373732e737667)](https://camo.githubusercontent.com/6a72d0eb66635207b9101fefa766aaad4aac9753c473fa7400326adc885df691/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64742f7472616e736974696f6e2e6373732e737667) [![Image 33: Latest Release](https://camo.githubusercontent.com/34a9b7654a3236a93b7d15eeb36476a98c43137d8367b8efb3730f3ae77a07f1/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f7472616e736974696f6e2e6373732e737667)](https://camo.githubusercontent.com/34a9b7654a3236a93b7d15eeb36476a98c43137d8367b8efb3730f3ae77a07f1/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f7472616e736974696f6e2e6373732e737667) [![Image 34: License](https://camo.githubusercontent.com/a4a9d76ca2c336eabd142d773b1b3e758e631b261dd6f4cf425944bdc1f3c5c5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f7472616e736974696f6e2e6373732e737667)](https://camo.githubusercontent.com/a4a9d76ca2c336eabd142d773b1b3e758e631b261dd6f4cf425944bdc1f3c5c5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f7472616e736974696f6e2e6373732e737667) [![Image 35: Netlify Status](https://camo.githubusercontent.com/721cdf63aece9efbd0861f66870fb2dc5033a7aad617a22136d65346d0c75c30/68747470733a2f2f6170692e6e65746c6966792e636f6d2f6170692f76312f6261646765732f35386430656366352d363234312d343230392d616133352d6366303939383365306233372f6465706c6f792d737461747573)](https://camo.githubusercontent.com/721cdf63aece9efbd0861f66870fb2dc5033a7aad617a22136d65346d0c75c30/68747470733a2f2f6170692e6e65746c6966792e636f6d2f6170692f76312f6261646765732f35386430656366352d363234312d343230392d616133352d6366303939383365306233372f6465706c6f792d737461747573)

[![Image 36](https://github.com/argyleink/transition.css/raw/main/gif/kitchen-sink.gif?raw=true)](https://codepen.io/argyleink/pen/zYqYpEB)

**46 pre-built transitions!**

> Hands on at [Codepen](https://codepen.io/argyleink/pen/RwrzGJb) or preview all @ [transition.style](https://transition.style/)

Basics
------

[](https://github.com/argyleink/transition.css?screenshot=true#basics)

Import the CSS and set an attribute on some HTML: [try on Codepen](https://codepen.io/argyleink/pen/QWNRXEG)  
[![Image 37](https://github.com/argyleink/transition.css/raw/main/gif/wipe-up.gif?raw=true)](https://github.com/argyleink/transition.css/blob/main/gif/wipe-up.gif?raw=true)

<link rel\="stylesheet" href\="https://unpkg.com/transition-style"\>

<div transition-style\="in:wipe:up"\>
  👍
</div\>

Installation
------------

[](https://github.com/argyleink/transition.css?screenshot=true#installation)

#### NPM

[](https://github.com/argyleink/transition.css?screenshot=true#npm)

1.  `npm i transition-style`
2.  import from **CSS**

@import "transition-style";

3.  or import from **JS**

import 'transition-style';

#### CDN

[](https://github.com/argyleink/transition.css?screenshot=true#cdn)

`https://unpkg.com/transition-style`

**Individual Category Bundles**

*   **Circles** `https://unpkg.com/transition-style/transition.circles.min.css`
*   **Squares** `https://unpkg.com/transition-style/transition.squares.min.css`
*   **Polygons** `https://unpkg.com/transition-style/transition.polygons.min.css`
*   **Wipes** `https://unpkg.com/transition-style/transition.wipes.min.css`

> Import category bundles from NPM too `import "transition-style/transition.circles.min.css"`

### 👉 The Hackpack

[](https://github.com/argyleink/transition.css?screenshot=true#-the-hackpack)

`https://unpkg.com/transition-style/transition.hackpack.min.css`

**More options, more control, smaller import**  
by importing only the custom properties and base styles:

*   compose custom transition combinations
*   create multi-part transitions
*   bring your own architecture with classes or CSS-in-JS or anything!

[The Hackpack Sandbox](https://codepen.io/argyleink/pen/MWyJxLx)

> Custom properties ship with each `.min.css` as well

### 🔗 Bookmarklet

[](https://github.com/argyleink/transition.css?screenshot=true#-bookmarklet)

Try transition.css on almost any _existing_ site! Just copy 📋 the following, create a new bookmark, and paste in the URL:

javascript:(function(){var a\=document.createElement("link");a.rel\="stylesheet";a.href\="https://unpkg.com/transition-style";document.head.append(a);})();

You can now go to a website and click the bookmark to try it out! Animations automatically run when you manually add classes in dev tools, or run code like this in the console:

$('body').setAttribute('transition-style','in:circle:bottom-right')

Caveat: this bookmarklet doesn't work on websites that have a strict CSP set up.

[![Image 38](https://github.com/argyleink/transition.css/raw/main/gif/opposing-corner-fold.gif?raw=true)](https://github.com/argyleink/transition.css/blob/main/gif/opposing-corner-fold.gif?raw=true)

Usage
-----

[](https://github.com/argyleink/transition.css?screenshot=true#usage)

After `transition.css` has been added to your project, add an attribute to an element and watch the magic:

<div transition-style\="in:circle:bottom-right"\>
  A transitioned IN element
</div\>

<div transition-style\="out:wipe:down"\>
  A transitioned OUT element
</div\>

> if nothing is happening when using the attributes, it's likely `transition.css` has not loaded

  
Attributes were chosen as the default so there's no question which transition is active. \*\*There can be only 1 at a time.\*\* With classes, for example, what happens when multiple "transition in" classes are applied to an element? Transition.css chooses to default with a state machine approach so things like a classname collision doesn't need solved. See the \[custom\](#custom) section below for ways to use classes and/or the shape custom properties so transition.css can fit into your development environment. The built in attribute based approach is very easy to hack, customize and escape.

#### Using `@keyframes`

[](https://github.com/argyleink/transition.css?screenshot=true#using-keyframes)

Each bundle ships with the `@keyframes` declared, and you can use them as you see fit. You can use these to build your own animations or just hook into the presets in your own way:

.main--state-in {
  animation: wipe-in-left;
  animation-duration: 2s;
  animation-fill-mode: both;
}

Checkout the [src](https://github.com/argyleink/transition.css/blob/main/src) to find the names of the `@keyframe` animations. They follow a pattern like the attributes, so you should be able to assume what they are with decent accuracy.

#### Using CSS Custom Properties

[](https://github.com/argyleink/transition.css?screenshot=true#using-css-custom-properties)

Each bundle ships with clearly named custom properties which contain the state and geometry needed to orchestrate custom transitions.

.overrides {
  \--transition\_\_duration: 1s;            /\* default: 2.5s \*/
  \--transition\_\_easing: ease-in-out;     /\* default: cubic-bezier(.25, 1, .30, 1) \*/
  \--transition\_\_delay: 1s;               /\* default: 0 \*/
}

or target a specific transition and override it's defaults:

\[transition\="in:wipe:up"\] {
  \--transition\_\_duration: 1s;
}

#### Custom

[](https://github.com/argyleink/transition.css?screenshot=true#custom)

Go off the rails and build your own transitions with these variables. There's even the `The Hackpack` which is exclusively the custom props 🤘💀 Here's how you can compose a brand new transition from the custom property primitives:

@keyframes circle-swoop {
  from {
    clip-path: var(\--circle-top-right-out);
  }
  to {
    clip-path: var(\--circle-bottom-right-in);
  }
}

.\--in-custom {
  \--transition\_\_duration: 1s;
  \--transition\_\_easing: ease-in-out;
  animation-name: circle-swoop;
}

Then, in the HTML:

<div transition-style class\="\--in-custom"\>
  A custom transitioned element
</div\>

> The only rule is that you must transition from the same type of shapes

At this point you're using Transition.css to it's maximum. You can reach a huge set of transitions by using the custom properties. Have fun!

#### Play

[](https://github.com/argyleink/transition.css?screenshot=true#play)

Play and experiment with [this Codepen](https://codepen.io/argyleink/pen/RwrzGJb)

Development
-----------

[](https://github.com/argyleink/transition.css?screenshot=true#development)

See the `svelte` branch.

Production
----------

[](https://github.com/argyleink/transition.css?screenshot=true#production)

`npm run bundle` concurrently bundles and minifies.

## Metadata

```json
{
  "title": "GitHub - argyleink/transition.css: :octocat: Drop-in CSS transitions",
  "description": ":octocat: Drop-in CSS transitions. Contribute to argyleink/transition.css development by creating an account on GitHub.",
  "url": "https://github.com/argyleink/transition.css?screenshot=true",
  "content": "[![Image 32: Total Downloads](https://camo.githubusercontent.com/6a72d0eb66635207b9101fefa766aaad4aac9753c473fa7400326adc885df691/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64742f7472616e736974696f6e2e6373732e737667)](https://camo.githubusercontent.com/6a72d0eb66635207b9101fefa766aaad4aac9753c473fa7400326adc885df691/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64742f7472616e736974696f6e2e6373732e737667) [![Image 33: Latest Release](https://camo.githubusercontent.com/34a9b7654a3236a93b7d15eeb36476a98c43137d8367b8efb3730f3ae77a07f1/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f7472616e736974696f6e2e6373732e737667)](https://camo.githubusercontent.com/34a9b7654a3236a93b7d15eeb36476a98c43137d8367b8efb3730f3ae77a07f1/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f7472616e736974696f6e2e6373732e737667) [![Image 34: License](https://camo.githubusercontent.com/a4a9d76ca2c336eabd142d773b1b3e758e631b261dd6f4cf425944bdc1f3c5c5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f7472616e736974696f6e2e6373732e737667)](https://camo.githubusercontent.com/a4a9d76ca2c336eabd142d773b1b3e758e631b261dd6f4cf425944bdc1f3c5c5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f7472616e736974696f6e2e6373732e737667) [![Image 35: Netlify Status](https://camo.githubusercontent.com/721cdf63aece9efbd0861f66870fb2dc5033a7aad617a22136d65346d0c75c30/68747470733a2f2f6170692e6e65746c6966792e636f6d2f6170692f76312f6261646765732f35386430656366352d363234312d343230392d616133352d6366303939383365306233372f6465706c6f792d737461747573)](https://camo.githubusercontent.com/721cdf63aece9efbd0861f66870fb2dc5033a7aad617a22136d65346d0c75c30/68747470733a2f2f6170692e6e65746c6966792e636f6d2f6170692f76312f6261646765732f35386430656366352d363234312d343230392d616133352d6366303939383365306233372f6465706c6f792d737461747573)\n\n[![Image 36](https://github.com/argyleink/transition.css/raw/main/gif/kitchen-sink.gif?raw=true)](https://codepen.io/argyleink/pen/zYqYpEB)\n\n**46 pre-built transitions!**\n\n> Hands on at [Codepen](https://codepen.io/argyleink/pen/RwrzGJb) or preview all @ [transition.style](https://transition.style/)\n\nBasics\n------\n\n[](https://github.com/argyleink/transition.css?screenshot=true#basics)\n\nImport the CSS and set an attribute on some HTML: [try on Codepen](https://codepen.io/argyleink/pen/QWNRXEG)  \n[![Image 37](https://github.com/argyleink/transition.css/raw/main/gif/wipe-up.gif?raw=true)](https://github.com/argyleink/transition.css/blob/main/gif/wipe-up.gif?raw=true)\n\n<link rel\\=\"stylesheet\" href\\=\"https://unpkg.com/transition-style\"\\>\n\n<div transition-style\\=\"in:wipe:up\"\\>\n  👍\n</div\\>\n\nInstallation\n------------\n\n[](https://github.com/argyleink/transition.css?screenshot=true#installation)\n\n#### NPM\n\n[](https://github.com/argyleink/transition.css?screenshot=true#npm)\n\n1.  `npm i transition-style`\n2.  import from **CSS**\n\n@import \"transition-style\";\n\n3.  or import from **JS**\n\nimport 'transition-style';\n\n#### CDN\n\n[](https://github.com/argyleink/transition.css?screenshot=true#cdn)\n\n`https://unpkg.com/transition-style`\n\n**Individual Category Bundles**\n\n*   **Circles** `https://unpkg.com/transition-style/transition.circles.min.css`\n*   **Squares** `https://unpkg.com/transition-style/transition.squares.min.css`\n*   **Polygons** `https://unpkg.com/transition-style/transition.polygons.min.css`\n*   **Wipes** `https://unpkg.com/transition-style/transition.wipes.min.css`\n\n> Import category bundles from NPM too `import \"transition-style/transition.circles.min.css\"`\n\n### 👉 The Hackpack\n\n[](https://github.com/argyleink/transition.css?screenshot=true#-the-hackpack)\n\n`https://unpkg.com/transition-style/transition.hackpack.min.css`\n\n**More options, more control, smaller import**  \nby importing only the custom properties and base styles:\n\n*   compose custom transition combinations\n*   create multi-part transitions\n*   bring your own architecture with classes or CSS-in-JS or anything!\n\n[The Hackpack Sandbox](https://codepen.io/argyleink/pen/MWyJxLx)\n\n> Custom properties ship with each `.min.css` as well\n\n### 🔗 Bookmarklet\n\n[](https://github.com/argyleink/transition.css?screenshot=true#-bookmarklet)\n\nTry transition.css on almost any _existing_ site! Just copy 📋 the following, create a new bookmark, and paste in the URL:\n\njavascript:(function(){var a\\=document.createElement(\"link\");a.rel\\=\"stylesheet\";a.href\\=\"https://unpkg.com/transition-style\";document.head.append(a);})();\n\nYou can now go to a website and click the bookmark to try it out! Animations automatically run when you manually add classes in dev tools, or run code like this in the console:\n\n$('body').setAttribute('transition-style','in:circle:bottom-right')\n\nCaveat: this bookmarklet doesn't work on websites that have a strict CSP set up.\n\n[![Image 38](https://github.com/argyleink/transition.css/raw/main/gif/opposing-corner-fold.gif?raw=true)](https://github.com/argyleink/transition.css/blob/main/gif/opposing-corner-fold.gif?raw=true)\n\nUsage\n-----\n\n[](https://github.com/argyleink/transition.css?screenshot=true#usage)\n\nAfter `transition.css` has been added to your project, add an attribute to an element and watch the magic:\n\n<div transition-style\\=\"in:circle:bottom-right\"\\>\n  A transitioned IN element\n</div\\>\n\n<div transition-style\\=\"out:wipe:down\"\\>\n  A transitioned OUT element\n</div\\>\n\n> if nothing is happening when using the attributes, it's likely `transition.css` has not loaded\n\n  \nAttributes were chosen as the default so there's no question which transition is active. \\*\\*There can be only 1 at a time.\\*\\* With classes, for example, what happens when multiple \"transition in\" classes are applied to an element? Transition.css chooses to default with a state machine approach so things like a classname collision doesn't need solved. See the \\[custom\\](#custom) section below for ways to use classes and/or the shape custom properties so transition.css can fit into your development environment. The built in attribute based approach is very easy to hack, customize and escape.\n\n#### Using `@keyframes`\n\n[](https://github.com/argyleink/transition.css?screenshot=true#using-keyframes)\n\nEach bundle ships with the `@keyframes` declared, and you can use them as you see fit. You can use these to build your own animations or just hook into the presets in your own way:\n\n.main--state-in {\n  animation: wipe-in-left;\n  animation-duration: 2s;\n  animation-fill-mode: both;\n}\n\nCheckout the [src](https://github.com/argyleink/transition.css/blob/main/src) to find the names of the `@keyframe` animations. They follow a pattern like the attributes, so you should be able to assume what they are with decent accuracy.\n\n#### Using CSS Custom Properties\n\n[](https://github.com/argyleink/transition.css?screenshot=true#using-css-custom-properties)\n\nEach bundle ships with clearly named custom properties which contain the state and geometry needed to orchestrate custom transitions.\n\n.overrides {\n  \\--transition\\_\\_duration: 1s;            /\\* default: 2.5s \\*/\n  \\--transition\\_\\_easing: ease-in-out;     /\\* default: cubic-bezier(.25, 1, .30, 1) \\*/\n  \\--transition\\_\\_delay: 1s;               /\\* default: 0 \\*/\n}\n\nor target a specific transition and override it's defaults:\n\n\\[transition\\=\"in:wipe:up\"\\] {\n  \\--transition\\_\\_duration: 1s;\n}\n\n#### Custom\n\n[](https://github.com/argyleink/transition.css?screenshot=true#custom)\n\nGo off the rails and build your own transitions with these variables. There's even the `The Hackpack` which is exclusively the custom props 🤘💀 Here's how you can compose a brand new transition from the custom property primitives:\n\n@keyframes circle-swoop {\n  from {\n    clip-path: var(\\--circle-top-right-out);\n  }\n  to {\n    clip-path: var(\\--circle-bottom-right-in);\n  }\n}\n\n.\\--in-custom {\n  \\--transition\\_\\_duration: 1s;\n  \\--transition\\_\\_easing: ease-in-out;\n  animation-name: circle-swoop;\n}\n\nThen, in the HTML:\n\n<div transition-style class\\=\"\\--in-custom\"\\>\n  A custom transitioned element\n</div\\>\n\n> The only rule is that you must transition from the same type of shapes\n\nAt this point you're using Transition.css to it's maximum. You can reach a huge set of transitions by using the custom properties. Have fun!\n\n#### Play\n\n[](https://github.com/argyleink/transition.css?screenshot=true#play)\n\nPlay and experiment with [this Codepen](https://codepen.io/argyleink/pen/RwrzGJb)\n\nDevelopment\n-----------\n\n[](https://github.com/argyleink/transition.css?screenshot=true#development)\n\nSee the `svelte` branch.\n\nProduction\n----------\n\n[](https://github.com/argyleink/transition.css?screenshot=true#production)\n\n`npm run bundle` concurrently bundles and minifies.",
  "usage": {
    "tokens": 2594
  }
}
```
