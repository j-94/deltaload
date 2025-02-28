---
title: GitHub - atlassian/react-beautiful-dnd: Beautiful and accessible drag and drop for lists with React
description: Beautiful and accessible drag and drop for lists with React - atlassian/react-beautiful-dnd
url: https://github.com/atlassian/react-beautiful-dnd
timestamp: 2025-01-20T15:30:36.088Z
domain: github.com
path: atlassian_react-beautiful-dnd
---

# GitHub - atlassian/react-beautiful-dnd: Beautiful and accessible drag and drop for lists with React


Beautiful and accessible drag and drop for lists with React - atlassian/react-beautiful-dnd


## Content

⚠️ Deprecated
-------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#%EF%B8%8F-deprecated)

Hey all,

We are taking the next step in saying thank you and goodbye to our friend `react-beautiful-dnd`.

*   🔔 We will be soon deprecating `react-beautiful-dnd` on [npm](https://www.npmjs.com/package/react-beautiful-dnd). When we do you will start to get console warnings in your build tools.
*   🔒 On Apr 30, 2025 (six months from posting) we will [archiving](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories) the `react-beautiful-dnd` Github repository (it will become read only).

Thank you everybody for your support of this project.

[More information](https://github.com/atlassian/react-beautiful-dnd/issues/2672)

  

* * *

[![Image 45: react beautiful dnd logo](https://user-images.githubusercontent.com/2182637/53611918-54c1ff80-3c24-11e9-9917-66ac3cef513d.png)](https://user-images.githubusercontent.com/2182637/53611918-54c1ff80-3c24-11e9-9917-66ac3cef513d.png)

react-beautiful-dnd (rbd)
-------------------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#react-beautiful-dnd-rbd)

Core characteristics
--------------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#core-characteristics)

*   Beautiful and [natural movement](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/animations.md) of items 💐
*   [Accessible](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/accessibility.md): powerful keyboard and screen reader support ♿️
*   [Extremely performant](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/media.md) 🚀
*   Clean and powerful api which is simple to get started with
*   Plays extremely well with standard browser interactions
*   [Unopinionated styling](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/preset-styles.md)
*   No creation of additional wrapper dom nodes - flexbox and focus management friendly!

Get started 👩‍🏫
-----------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#get-started-)

We have created [a free course on `egghead.io` 🥚](https://egghead.io/courses/beautiful-and-accessible-drag-and-drop-with-react-beautiful-dnd) to help you get started with `react-beautiful-dnd` as quickly as possible.

[![Image 46: course-logo](https://user-images.githubusercontent.com/2182637/43372837-8c72d3f8-93e8-11e8-9d92-a82adde7718f.png)](https://egghead.io/courses/beautiful-and-accessible-drag-and-drop-with-react-beautiful-dnd)

Currently supported feature set ✅
---------------------------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#currently-supported-feature-set-)

*   Vertical lists ↕
*   Horizontal lists ↔
*   Movement between lists (▤ ↔ ▤)
*   [Virtual list support 👾](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/virtual-lists.md) - unlocking 10,000 items @ 60fps
*   [Combining items](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/combining.md)
*   Mouse 🐭, keyboard 🎹♿️ and touch 👉📱 (mobile, tablet and so on) support
*   [Multi drag support](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/multi-drag.md)
*   Incredible screen reader support ♿️ - we provide an amazing experience for english screen readers out of the box 📦. We also provide complete customisation control and internationalisation support for those who need it 💖
*   [Conditional dragging](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md#optional-props) and [conditional dropping](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/droppable.md#conditionally-dropping)
*   Multiple independent lists on the one page
*   Flexible item sizes - the draggable items can have different heights (vertical lists) or widths (horizontal lists)
*   [Add and remove items during a drag](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/changes-while-dragging.md)
*   Compatible with semantic `<table>` reordering - [table pattern](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/tables.md)
*   [Auto scrolling](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/auto-scrolling.md) - automatically scroll containers and the window as required during a drag (even with keyboard 🔥)
*   Custom drag handles - you can drag a whole item by just a part of it
*   Able to move the dragging item to another element while dragging (clone, portal) - [Reparenting your `<Draggable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/reparenting.md)
*   [Create scripted drag and drop experiences 🎮](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/sensor-api.md)
*   Allows extensions to support for [any input type you like 🕹](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/sensor-api.md)
*   🌲 Tree support through the [`@atlaskit/tree`](https://atlaskit.atlassian.com/packages/confluence/tree) package
*   A `<Droppable />` list can be a scroll container (without a scrollable parent) or be the child of a scroll container (that also does not have a scrollable parent)
*   Independent nested lists - a list can be a child of another list, but you cannot drag items from the parent list into a child list
*   Server side rendering (SSR) compatible - see [resetServerContext()](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/reset-server-context.md)
*   Plays well with [nested interactive elements](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md#interactive-child-elements-within-a-draggable-) by default

Motivation 🤔
-------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#motivation-)

`react-beautiful-dnd` exists to create beautiful drag and drop for lists that anyone can use - even people who cannot see. For a good overview of the history and motivations of the project you can take a look at these external resources:

*   📖 [Rethinking drag and drop](https://medium.com/@alexandereardon/rethinking-drag-and-drop-d9f5770b4e6b)
*   🎧 [React podcast: fast, accessible and beautiful drag and drop](https://reactpodcast.simplecast.fm/17)

Not for everyone ✌️
-------------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#not-for-everyone-%EF%B8%8F)

There are a lot of libraries out there that allow for drag and drop interactions within React. Most notable of these is the amazing [`react-dnd`](https://github.com/react-dnd/react-dnd). It does an incredible job at providing a great set of drag and drop primitives which work especially well with the [wildly inconsistent](https://www.quirksmode.org/blog/archives/2009/09/the_html5_drag.html) html5 drag and drop feature. `react-beautiful-dnd` is a higher level abstraction specifically built for lists (vertical, horizontal, movement between lists, nested lists and so on). Within that subset of functionality `react-beautiful-dnd` offers a powerful, natural and beautiful drag and drop experience. However, it does not provide the breadth of functionality offered by `react-dnd`. So `react-beautiful-dnd` might not be for you depending on what your use case is.

Documentation 📖
----------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#documentation-)

### About 👋

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#about-)

*   [Installation](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/installation.md)
*   [Examples and samples](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/examples.md)
*   [Get started](https://egghead.io/courses/beautiful-and-accessible-drag-and-drop-with-react-beautiful-dnd)
*   [Design principles](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/design-principles.md)
*   [Animations](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/animations.md)
*   [Accessibility](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/accessibility.md)
*   [Browser support](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/browser-support.md)

### Sensors 🔉

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#sensors-)

> The ways in which somebody can start and control a drag

*   [Mouse dragging 🐭](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/mouse.md)
*   [Touch dragging 👉📱](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/touch.md)
*   [Keyboard dragging 🎹♿️](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/keyboard.md)
*   [Create your own sensor](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/sensor-api.md) (allows for any input type as well as scripted experiences)

### API 🏋️‍

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#api-%EF%B8%8F)

[![Image 47: diagram](https://user-images.githubusercontent.com/2182637/53607406-c8f3a780-3c12-11e9-979c-7f3b5bd1bfbd.gif)](https://user-images.githubusercontent.com/2182637/53607406-c8f3a780-3c12-11e9-979c-7f3b5bd1bfbd.gif)

*   [`<DragDropContext />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/drag-drop-context.md) - _Wraps the part of your application you want to have drag and drop enabled for_
*   [`<Droppable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/droppable.md) - _An area that can be dropped into. Contains `<Draggable />`s_
*   [`<Draggable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md) - _What can be dragged around_
*   [`resetServerContext()`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/reset-server-context.md) - _Utility for server side rendering (SSR)_

### Guides 🗺

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#guides-)

*   [`<DragDropContext />` responders](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/responders.md) - _`onDragStart`, `onDragUpdate`, `onDragEnd` and `onBeforeDragStart`_
*   [Combining `<Draggable />`s](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/combining.md)
*   [Common setup issues](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/common-setup-issues.md)
*   [Using `innerRef`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/using-inner-ref.md)
*   [Setup problem detection and error recovery](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/setup-problem-detection-and-error-recovery.md)
*   [Rules for `draggableId` and `droppableId`s](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/identifiers.md)
*   [Browser focus retention](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/browser-focus.md)
*   [Customising or skipping the drop animation](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/drop-animation.md)
*   [Auto scrolling](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/auto-scrolling.md)
*   [Controlling the screen reader](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/screen-reader.md)
*   [Use the html5 `doctype`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/doctype.md)
*   [`TypeScript` and `flow`: type information](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/types.md)
*   [Dragging `<svg>`s](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/dragging-svgs.md)
*   [Avoiding image flickering](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/avoiding-image-flickering.md)
*   [Non-visible preset styles](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/preset-styles.md)
*   [How we detect scroll containers](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/how-we-detect-scroll-containers.md)
*   [How we use dom events](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/how-we-use-dom-events.md) - _Useful if you need to build on top of `react-beautiful-dnd`_
*   [Adding `<Draggable />`s during a drag (11.x behaviour)](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/changes-while-dragging.md) - _⚠️ Advanced_
*   [Setting up Content Security Policy](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/content-security-policy.md)

### Patterns 👷‍

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#patterns-)

*   [Virtual lists 👾](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/virtual-lists.md)
*   [Multi drag](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/multi-drag.md)
*   [Tables](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/tables.md)
*   [Reparenting a `<Draggable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/reparenting.md) - _Using our cloning API or your own portal_

### Support 👩‍⚕️

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#support-%EF%B8%8F)

*   [Engineering health](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/engineering-health.md)
*   [Community and addons](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/community-and-addons.md)
*   [Release notes and changelog](https://github.com/atlassian/react-beautiful-dnd/releases)
*   [Upgrading](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/upgrading.md)
*   [Road map](https://github.com/atlassian/react-beautiful-dnd/issues)
*   [Media](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/media.md)

Read this in other languages 🌎
-------------------------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#read-this-in-other-languages-)

*    [![Image 48: kr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/South-Korea.png) **한글/Korean**](https://github.com/LeeHyungGeun/react-beautiful-dnd-kr)
*    [![Image 49: ru](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Russia.png) **На русском/Russian**](https://github.com/vtereshyn/react-beautiful-dnd-ru)
*    [![Image 50: pt](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Brazil.png) **Português/Portuguese**](https://github.com/dudestein/react-beautiful-dnd-pt)
*    [![Image 51: gr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Greece.png) **Ελληνικά/Greek**](https://github.com/milvard/react-beautiful-dnd-gr)
*    [![Image 52: ja](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Japan.png) **日本語/Japanese**](https://github.com/eltociear/react-beautiful-dnd-ja)

Creator ✍️
----------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#creator-%EF%B8%8F)

Alex Reardon [@alexandereardon](https://twitter.com/alexandereardon)

> Alex is no longer personally maintaning this project. The other wonderful maintainers are carrying this project forward.

Maintainers
-----------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#maintainers)

*   [Daniel Del Core](https://twitter.com/danieldelcore)
*   Many other [@Atlassian](https://twitter.com/Atlassian)'s!

Collaborators 🤝
----------------

[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#collaborators-)

*   Bogdan Chadkin [@IAmTrySound](https://twitter.com/IAmTrySound)

## Metadata

```json
{
  "title": "GitHub - atlassian/react-beautiful-dnd: Beautiful and accessible drag and drop for lists with React",
  "description": "Beautiful and accessible drag and drop for lists with React - atlassian/react-beautiful-dnd",
  "url": "https://github.com/atlassian/react-beautiful-dnd?screenshot=true",
  "content": "⚠️ Deprecated\n-------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#%EF%B8%8F-deprecated)\n\nHey all,\n\nWe are taking the next step in saying thank you and goodbye to our friend `react-beautiful-dnd`.\n\n*   🔔 We will be soon deprecating `react-beautiful-dnd` on [npm](https://www.npmjs.com/package/react-beautiful-dnd). When we do you will start to get console warnings in your build tools.\n*   🔒 On Apr 30, 2025 (six months from posting) we will [archiving](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories) the `react-beautiful-dnd` Github repository (it will become read only).\n\nThank you everybody for your support of this project.\n\n[More information](https://github.com/atlassian/react-beautiful-dnd/issues/2672)\n\n  \n\n* * *\n\n[![Image 45: react beautiful dnd logo](https://user-images.githubusercontent.com/2182637/53611918-54c1ff80-3c24-11e9-9917-66ac3cef513d.png)](https://user-images.githubusercontent.com/2182637/53611918-54c1ff80-3c24-11e9-9917-66ac3cef513d.png)\n\nreact-beautiful-dnd (rbd)\n-------------------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#react-beautiful-dnd-rbd)\n\nCore characteristics\n--------------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#core-characteristics)\n\n*   Beautiful and [natural movement](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/animations.md) of items 💐\n*   [Accessible](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/accessibility.md): powerful keyboard and screen reader support ♿️\n*   [Extremely performant](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/media.md) 🚀\n*   Clean and powerful api which is simple to get started with\n*   Plays extremely well with standard browser interactions\n*   [Unopinionated styling](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/preset-styles.md)\n*   No creation of additional wrapper dom nodes - flexbox and focus management friendly!\n\nGet started 👩‍🏫\n-----------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#get-started-)\n\nWe have created [a free course on `egghead.io` 🥚](https://egghead.io/courses/beautiful-and-accessible-drag-and-drop-with-react-beautiful-dnd) to help you get started with `react-beautiful-dnd` as quickly as possible.\n\n[![Image 46: course-logo](https://user-images.githubusercontent.com/2182637/43372837-8c72d3f8-93e8-11e8-9d92-a82adde7718f.png)](https://egghead.io/courses/beautiful-and-accessible-drag-and-drop-with-react-beautiful-dnd)\n\nCurrently supported feature set ✅\n---------------------------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#currently-supported-feature-set-)\n\n*   Vertical lists ↕\n*   Horizontal lists ↔\n*   Movement between lists (▤ ↔ ▤)\n*   [Virtual list support 👾](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/virtual-lists.md) - unlocking 10,000 items @ 60fps\n*   [Combining items](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/combining.md)\n*   Mouse 🐭, keyboard 🎹♿️ and touch 👉📱 (mobile, tablet and so on) support\n*   [Multi drag support](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/multi-drag.md)\n*   Incredible screen reader support ♿️ - we provide an amazing experience for english screen readers out of the box 📦. We also provide complete customisation control and internationalisation support for those who need it 💖\n*   [Conditional dragging](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md#optional-props) and [conditional dropping](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/droppable.md#conditionally-dropping)\n*   Multiple independent lists on the one page\n*   Flexible item sizes - the draggable items can have different heights (vertical lists) or widths (horizontal lists)\n*   [Add and remove items during a drag](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/changes-while-dragging.md)\n*   Compatible with semantic `<table>` reordering - [table pattern](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/tables.md)\n*   [Auto scrolling](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/auto-scrolling.md) - automatically scroll containers and the window as required during a drag (even with keyboard 🔥)\n*   Custom drag handles - you can drag a whole item by just a part of it\n*   Able to move the dragging item to another element while dragging (clone, portal) - [Reparenting your `<Draggable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/reparenting.md)\n*   [Create scripted drag and drop experiences 🎮](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/sensor-api.md)\n*   Allows extensions to support for [any input type you like 🕹](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/sensor-api.md)\n*   🌲 Tree support through the [`@atlaskit/tree`](https://atlaskit.atlassian.com/packages/confluence/tree) package\n*   A `<Droppable />` list can be a scroll container (without a scrollable parent) or be the child of a scroll container (that also does not have a scrollable parent)\n*   Independent nested lists - a list can be a child of another list, but you cannot drag items from the parent list into a child list\n*   Server side rendering (SSR) compatible - see [resetServerContext()](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/reset-server-context.md)\n*   Plays well with [nested interactive elements](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md#interactive-child-elements-within-a-draggable-) by default\n\nMotivation 🤔\n-------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#motivation-)\n\n`react-beautiful-dnd` exists to create beautiful drag and drop for lists that anyone can use - even people who cannot see. For a good overview of the history and motivations of the project you can take a look at these external resources:\n\n*   📖 [Rethinking drag and drop](https://medium.com/@alexandereardon/rethinking-drag-and-drop-d9f5770b4e6b)\n*   🎧 [React podcast: fast, accessible and beautiful drag and drop](https://reactpodcast.simplecast.fm/17)\n\nNot for everyone ✌️\n-------------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#not-for-everyone-%EF%B8%8F)\n\nThere are a lot of libraries out there that allow for drag and drop interactions within React. Most notable of these is the amazing [`react-dnd`](https://github.com/react-dnd/react-dnd). It does an incredible job at providing a great set of drag and drop primitives which work especially well with the [wildly inconsistent](https://www.quirksmode.org/blog/archives/2009/09/the_html5_drag.html) html5 drag and drop feature. `react-beautiful-dnd` is a higher level abstraction specifically built for lists (vertical, horizontal, movement between lists, nested lists and so on). Within that subset of functionality `react-beautiful-dnd` offers a powerful, natural and beautiful drag and drop experience. However, it does not provide the breadth of functionality offered by `react-dnd`. So `react-beautiful-dnd` might not be for you depending on what your use case is.\n\nDocumentation 📖\n----------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#documentation-)\n\n### About 👋\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#about-)\n\n*   [Installation](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/installation.md)\n*   [Examples and samples](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/examples.md)\n*   [Get started](https://egghead.io/courses/beautiful-and-accessible-drag-and-drop-with-react-beautiful-dnd)\n*   [Design principles](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/design-principles.md)\n*   [Animations](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/animations.md)\n*   [Accessibility](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/accessibility.md)\n*   [Browser support](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/about/browser-support.md)\n\n### Sensors 🔉\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#sensors-)\n\n> The ways in which somebody can start and control a drag\n\n*   [Mouse dragging 🐭](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/mouse.md)\n*   [Touch dragging 👉📱](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/touch.md)\n*   [Keyboard dragging 🎹♿️](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/keyboard.md)\n*   [Create your own sensor](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/sensors/sensor-api.md) (allows for any input type as well as scripted experiences)\n\n### API 🏋️‍\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#api-%EF%B8%8F)\n\n[![Image 47: diagram](https://user-images.githubusercontent.com/2182637/53607406-c8f3a780-3c12-11e9-979c-7f3b5bd1bfbd.gif)](https://user-images.githubusercontent.com/2182637/53607406-c8f3a780-3c12-11e9-979c-7f3b5bd1bfbd.gif)\n\n*   [`<DragDropContext />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/drag-drop-context.md) - _Wraps the part of your application you want to have drag and drop enabled for_\n*   [`<Droppable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/droppable.md) - _An area that can be dropped into. Contains `<Draggable />`s_\n*   [`<Draggable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md) - _What can be dragged around_\n*   [`resetServerContext()`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/reset-server-context.md) - _Utility for server side rendering (SSR)_\n\n### Guides 🗺\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#guides-)\n\n*   [`<DragDropContext />` responders](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/responders.md) - _`onDragStart`, `onDragUpdate`, `onDragEnd` and `onBeforeDragStart`_\n*   [Combining `<Draggable />`s](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/combining.md)\n*   [Common setup issues](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/common-setup-issues.md)\n*   [Using `innerRef`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/using-inner-ref.md)\n*   [Setup problem detection and error recovery](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/setup-problem-detection-and-error-recovery.md)\n*   [Rules for `draggableId` and `droppableId`s](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/identifiers.md)\n*   [Browser focus retention](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/browser-focus.md)\n*   [Customising or skipping the drop animation](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/drop-animation.md)\n*   [Auto scrolling](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/auto-scrolling.md)\n*   [Controlling the screen reader](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/screen-reader.md)\n*   [Use the html5 `doctype`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/doctype.md)\n*   [`TypeScript` and `flow`: type information](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/types.md)\n*   [Dragging `<svg>`s](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/dragging-svgs.md)\n*   [Avoiding image flickering](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/avoiding-image-flickering.md)\n*   [Non-visible preset styles](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/preset-styles.md)\n*   [How we detect scroll containers](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/how-we-detect-scroll-containers.md)\n*   [How we use dom events](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/how-we-use-dom-events.md) - _Useful if you need to build on top of `react-beautiful-dnd`_\n*   [Adding `<Draggable />`s during a drag (11.x behaviour)](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/changes-while-dragging.md) - _⚠️ Advanced_\n*   [Setting up Content Security Policy](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/content-security-policy.md)\n\n### Patterns 👷‍\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#patterns-)\n\n*   [Virtual lists 👾](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/virtual-lists.md)\n*   [Multi drag](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/multi-drag.md)\n*   [Tables](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/patterns/tables.md)\n*   [Reparenting a `<Draggable />`](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/guides/reparenting.md) - _Using our cloning API or your own portal_\n\n### Support 👩‍⚕️\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#support-%EF%B8%8F)\n\n*   [Engineering health](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/engineering-health.md)\n*   [Community and addons](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/community-and-addons.md)\n*   [Release notes and changelog](https://github.com/atlassian/react-beautiful-dnd/releases)\n*   [Upgrading](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/upgrading.md)\n*   [Road map](https://github.com/atlassian/react-beautiful-dnd/issues)\n*   [Media](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/support/media.md)\n\nRead this in other languages 🌎\n-------------------------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#read-this-in-other-languages-)\n\n*    [![Image 48: kr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/South-Korea.png) **한글/Korean**](https://github.com/LeeHyungGeun/react-beautiful-dnd-kr)\n*    [![Image 49: ru](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Russia.png) **На русском/Russian**](https://github.com/vtereshyn/react-beautiful-dnd-ru)\n*    [![Image 50: pt](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Brazil.png) **Português/Portuguese**](https://github.com/dudestein/react-beautiful-dnd-pt)\n*    [![Image 51: gr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Greece.png) **Ελληνικά/Greek**](https://github.com/milvard/react-beautiful-dnd-gr)\n*    [![Image 52: ja](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Japan.png) **日本語/Japanese**](https://github.com/eltociear/react-beautiful-dnd-ja)\n\nCreator ✍️\n----------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#creator-%EF%B8%8F)\n\nAlex Reardon [@alexandereardon](https://twitter.com/alexandereardon)\n\n> Alex is no longer personally maintaning this project. The other wonderful maintainers are carrying this project forward.\n\nMaintainers\n-----------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#maintainers)\n\n*   [Daniel Del Core](https://twitter.com/danieldelcore)\n*   Many other [@Atlassian](https://twitter.com/Atlassian)'s!\n\nCollaborators 🤝\n----------------\n\n[](https://github.com/atlassian/react-beautiful-dnd?screenshot=true#collaborators-)\n\n*   Bogdan Chadkin [@IAmTrySound](https://twitter.com/IAmTrySound)",
  "usage": {
    "tokens": 4095
  }
}
```
