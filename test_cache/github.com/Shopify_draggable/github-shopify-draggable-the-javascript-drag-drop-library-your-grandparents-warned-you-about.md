---
title: GitHub - Shopify/draggable: The JavaScript Drag & Drop library your grandparents warned you about.
description: The JavaScript Drag & Drop library your grandparents warned you about. - Shopify/draggable
url: https://github.com/Shopify/draggable
timestamp: 2025-01-20T15:30:38.749Z
domain: github.com
path: Shopify_draggable
---

# GitHub - Shopify/draggable: The JavaScript Drag & Drop library your grandparents warned you about.


The JavaScript Drag & Drop library your grandparents warned you about. - Shopify/draggable


## Content

[![Image 36: npm version](https://camo.githubusercontent.com/c77db4a511670a680f139b1d8648ac2ec4b6545c499b9e85d9497fb5c6bf7dad/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f4073686f706966792f647261676761626c652e7376673f6c6162656c3d4073686f706966792f647261676761626c65)](https://www.npmjs.com/package/@shopify/draggable) [![Image 37: CI](https://github.com/shopify/draggable/workflows/CI/badge.svg)](https://github.com/Shopify/draggable/actions?query=branch%3Amain) [![Image 38: PRs Welcome](https://camo.githubusercontent.com/d88d8d77fa79e828eea397f75a1ebd114d13488aeec4747477ffbd2274de95ed/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d627269676874677265656e2e737667)](https://github.com/Shopify/draggable/blob/main/CONTRIBUTING.md) [![Image 39: Bundle size](https://camo.githubusercontent.com/2f6684e2d0af45a563de5f5d3c516069992d01e074c0fbe7a85013130733d1ac/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42756e646c6525323073697a652d31362e326b422d7265642e737667)](https://camo.githubusercontent.com/2f6684e2d0af45a563de5f5d3c516069992d01e074c0fbe7a85013130733d1ac/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42756e646c6525323073697a652d31362e326b422d7265642e737667)

[![Image 40](https://user-images.githubusercontent.com/643944/35602291-99e2c56e-0605-11e8-847f-95f1f6be1610.jpg)](https://shopify.github.io/draggable "Visit Draggable website")

Development
-----------

[](https://github.com/Shopify/draggable?screenshot=true#development)

**Draggable is no longer maintained by its original authors.** Maintenance of this repo has been passed on to new collaborators and is no longer worked on by anyone at Shopify.

**We are still looking for more maintainers!** If anyone is interested in answering / triaging issues, reviewing / rejecting / approving PRs, and authoring code for bug fixes / new features — please send an email to `max.hoffmann (at) shopify (dot) com`. You may be asked a few questions before obtaining collaboration permission, but if everything checks out, we will happily add you as a collaborator.

* * *

Get complete control over drag and drop behaviour with Draggable! Draggable abstracts native browser events into a comprehensive API to create a custom drag and drop experience. `Draggable` comes with additional modules: `Sortable`, `Droppable`, `Swappable`. Draggable itself does not perform any sorting behaviour while dragging, but does the heavy lifting, e.g. creates mirror, emits events, manages sensor events, makes elements draggable.

The additional modules are built on top of `Draggable` and therefore provide a similar API interface, for more information read the documentation below.

**Features**

*   Works with native drag, mouse, touch and force touch events
*   Can extend dragging behaviour by hooking into draggables event life cycle
*   Can extend drag detection by adding sensors to draggable
*   The library is targeted ES6 first

Table of Contents
-----------------

[](https://github.com/Shopify/draggable?screenshot=true#table-of-contents)

*   [Install](https://github.com/Shopify/draggable?screenshot=true#install)
*   [Documentation](https://github.com/Shopify/draggable?screenshot=true#documentation)
*   [Contributing](https://github.com/Shopify/draggable?screenshot=true#contributing)
*   [Roadmap](https://github.com/Shopify/draggable?screenshot=true#roadmap)
*   [Copyright](https://github.com/Shopify/draggable?screenshot=true#copyright)

Install
-------

[](https://github.com/Shopify/draggable?screenshot=true#install)

You can install the library via npm.

npm install @shopify/draggable --save

or via yarn:

yarn add @shopify/draggable

or via CDN

<!-- Entire bundle --\>
<script type\="module"\>
  import {
    Draggable,
    Sortable,
    Droppable,
    Swappable,
  } from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/index.mjs';
</script\>
<!-- Draggable only --\>
<script type\="module"\>
  import Draggable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Draggable/Draggable.mjs';
</script\>
<!-- Sortable only --\>
<script type\="module"\>
  import Sortable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Sortable/Sortable.mjs';
</script\>
<!-- Droppable only --\>
<script type\="module"\>
  import Droppable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Droppable/Droppable.mjs';
</script\>
<!-- Swappable only --\>
<script type\="module"\>
  import Swappable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Swappable/Swappable.mjs';
</script\>
<!-- Plugins only --\>
<script type\="module"\>
  import \* as Plugins from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Plugins/index.mjs';
</script\>
<!-- UMD browser --\>
<script src\="https://cdn.jsdelivr.net/npm/@shopify/draggable/build/umd/index.min.js"\></script\>
<script\>
  console.log(window.Draggable);
</script\>

Browser Compatibility
---------------------

[](https://github.com/Shopify/draggable?screenshot=true#browser-compatibility)

Check the "browserlist" property in [package.json](https://github.com/Shopify/draggable/blob/main/package.json#L88) for more info

| [![Image 41: Chrome](https://camo.githubusercontent.com/c23f02f6604b0b5fee3615832d7f237055892cdda9f8a2c46e62131cf7e7cd12/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6368726f6d652f6368726f6d655f34387834382e706e67)](https://camo.githubusercontent.com/c23f02f6604b0b5fee3615832d7f237055892cdda9f8a2c46e62131cf7e7cd12/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6368726f6d652f6368726f6d655f34387834382e706e67) | [![Image 42: Firefox](https://camo.githubusercontent.com/234a8814dfe9d689612fe6f899acbba9b1385af208cd693bc3b08cfc931ed954/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f66697265666f782f66697265666f785f34387834382e706e67)](https://camo.githubusercontent.com/234a8814dfe9d689612fe6f899acbba9b1385af208cd693bc3b08cfc931ed954/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f66697265666f782f66697265666f785f34387834382e706e67) | [![Image 43: Opera](https://camo.githubusercontent.com/e13076052cc3a8e0e2d3532a7e63bb4b0971cc796768e85f11897b76654f3216/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6f706572612f6f706572615f34387834382e706e67)](https://camo.githubusercontent.com/e13076052cc3a8e0e2d3532a7e63bb4b0971cc796768e85f11897b76654f3216/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6f706572612f6f706572615f34387834382e706e67) | [![Image 44: Safari](https://camo.githubusercontent.com/40dd86d718fa616895f201e601dfe0d1988c01c5a57c27fe6f104999eef377a2/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f7361666172692f7361666172695f34387834382e706e67)](https://camo.githubusercontent.com/40dd86d718fa616895f201e601dfe0d1988c01c5a57c27fe6f104999eef377a2/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f7361666172692f7361666172695f34387834382e706e67) | [![Image 45: Edge](https://camo.githubusercontent.com/490746383ccfcbcadcb2d362870f855731dbe73c3230b171d31f5b090406816e/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f656467652f656467655f34387834382e706e67)](https://camo.githubusercontent.com/490746383ccfcbcadcb2d362870f855731dbe73c3230b171d31f5b090406816e/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f656467652f656467655f34387834382e706e67) |
| --- | --- | --- | --- | --- |
| Last 3 versions ✔ | Last 3 versions ✔ | Last 3 versions ✔ | Last 3 versions ✔ | Last 3 versions ✔ |

Documentation
-------------

[](https://github.com/Shopify/draggable?screenshot=true#documentation)

You can find the documentation for each module within their respective directories.

*   [Draggable](https://github.com/Shopify/draggable/blob/main/src/Draggable)
    *   [DragEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/DragEvent)
    *   [DraggableEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/DraggableEvent)
    *   [Plugins](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins)
        *   [Announcement](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Announcement)
        *   [Focusable](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Focusable)
        *   [Mirror](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Mirror)
        *   [MirrorEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Mirror/MirrorEvent)
        *   [Scrollable](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Scrollable)
    *   [Sensors](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors)
        *   [DragSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/DragSensor)
        *   [ForceTouchSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/ForceTouchSensor)
        *   [MouseSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/MouseSensor)
        *   [Sensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/Sensor)
        *   [SensorEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/SensorEvent)
        *   [TouchSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/TouchSensor)
*   [Droppable](https://github.com/Shopify/draggable/blob/main/src/Droppable)
    *   [DroppableEvent](https://github.com/Shopify/draggable/blob/main/src/Droppable/DroppableEvent)
*   [Plugins](https://github.com/Shopify/draggable/blob/main/src/Plugins)
    *   [Collidable](https://github.com/Shopify/draggable/blob/main/src/Plugins/Collidable)
    *   [ResizeMirror](https://github.com/Shopify/draggable/blob/main/src/Plugins/ResizeMirror)
    *   [Snappable](https://github.com/Shopify/draggable/blob/main/src/Plugins/Snappable)
    *   [SwapAnimation](https://github.com/Shopify/draggable/blob/main/src/Plugins/SwapAnimation)
    *   [SortAnimation](https://github.com/Shopify/draggable/blob/main/src/Plugins/SortAnimation)
*   [Sortable](https://github.com/Shopify/draggable/blob/main/src/Sortable)
    *   [SortableEvent](https://github.com/Shopify/draggable/blob/main/src/Sortable/SortableEvent)
*   [Swappable](https://github.com/Shopify/draggable/blob/main/src/Swappable)
    *   [SwappableEvent](https://github.com/Shopify/draggable/blob/main/src/Swappable/SwappableEvent)

### TypeScript

[](https://github.com/Shopify/draggable?screenshot=true#typescript)

Draggable includes [TypeScript](http://typescriptlang.org/) definitions.

[Documentation](https://github.com/Shopify/draggable/blob/main/doc/typescript.md)

Running examples
----------------

[](https://github.com/Shopify/draggable?screenshot=true#running-examples)

To run the `examples` project locally, simply run the following from the `draggable` root:

This will start a server that hosts the contents of `examples/`. It also watches for file changes from both `src/` and `examples/src` and reloads the browser.

Contributing
------------

[](https://github.com/Shopify/draggable?screenshot=true#contributing)

Contributions are more than welcome, the code base is still new and needs more love.

For more information, please checkout the [contributing document](https://github.com/Shopify/draggable/blob/main/CONTRIBUTING.md).

Related resources
-----------------

[](https://github.com/Shopify/draggable?screenshot=true#related-resources)

*   [Ember CLI Shim](https://github.com/timrourke/ember-cli-shopify-draggable-shim) on Github by [@timrourke](https://github.com/timrourke)
*   [Ember CLI Shim](https://www.npmjs.com/package/ember-cli-shopify-draggable-shim) on NPM by [@timrourke](https://github.com/timrourke)

Copyright
---------

[](https://github.com/Shopify/draggable?screenshot=true#copyright)

Copyright (c) 2018-present Shopify. See LICENSE.md for further details.

## Metadata

```json
{
  "title": "GitHub - Shopify/draggable: The JavaScript Drag & Drop library your grandparents warned you about.",
  "description": "The JavaScript Drag & Drop library your grandparents warned you about. - Shopify/draggable",
  "url": "https://github.com/Shopify/draggable?screenshot=true",
  "content": "[![Image 36: npm version](https://camo.githubusercontent.com/c77db4a511670a680f139b1d8648ac2ec4b6545c499b9e85d9497fb5c6bf7dad/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f4073686f706966792f647261676761626c652e7376673f6c6162656c3d4073686f706966792f647261676761626c65)](https://www.npmjs.com/package/@shopify/draggable) [![Image 37: CI](https://github.com/shopify/draggable/workflows/CI/badge.svg)](https://github.com/Shopify/draggable/actions?query=branch%3Amain) [![Image 38: PRs Welcome](https://camo.githubusercontent.com/d88d8d77fa79e828eea397f75a1ebd114d13488aeec4747477ffbd2274de95ed/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d627269676874677265656e2e737667)](https://github.com/Shopify/draggable/blob/main/CONTRIBUTING.md) [![Image 39: Bundle size](https://camo.githubusercontent.com/2f6684e2d0af45a563de5f5d3c516069992d01e074c0fbe7a85013130733d1ac/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42756e646c6525323073697a652d31362e326b422d7265642e737667)](https://camo.githubusercontent.com/2f6684e2d0af45a563de5f5d3c516069992d01e074c0fbe7a85013130733d1ac/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42756e646c6525323073697a652d31362e326b422d7265642e737667)\n\n[![Image 40](https://user-images.githubusercontent.com/643944/35602291-99e2c56e-0605-11e8-847f-95f1f6be1610.jpg)](https://shopify.github.io/draggable \"Visit Draggable website\")\n\nDevelopment\n-----------\n\n[](https://github.com/Shopify/draggable?screenshot=true#development)\n\n**Draggable is no longer maintained by its original authors.** Maintenance of this repo has been passed on to new collaborators and is no longer worked on by anyone at Shopify.\n\n**We are still looking for more maintainers!** If anyone is interested in answering / triaging issues, reviewing / rejecting / approving PRs, and authoring code for bug fixes / new features — please send an email to `max.hoffmann (at) shopify (dot) com`. You may be asked a few questions before obtaining collaboration permission, but if everything checks out, we will happily add you as a collaborator.\n\n* * *\n\nGet complete control over drag and drop behaviour with Draggable! Draggable abstracts native browser events into a comprehensive API to create a custom drag and drop experience. `Draggable` comes with additional modules: `Sortable`, `Droppable`, `Swappable`. Draggable itself does not perform any sorting behaviour while dragging, but does the heavy lifting, e.g. creates mirror, emits events, manages sensor events, makes elements draggable.\n\nThe additional modules are built on top of `Draggable` and therefore provide a similar API interface, for more information read the documentation below.\n\n**Features**\n\n*   Works with native drag, mouse, touch and force touch events\n*   Can extend dragging behaviour by hooking into draggables event life cycle\n*   Can extend drag detection by adding sensors to draggable\n*   The library is targeted ES6 first\n\nTable of Contents\n-----------------\n\n[](https://github.com/Shopify/draggable?screenshot=true#table-of-contents)\n\n*   [Install](https://github.com/Shopify/draggable?screenshot=true#install)\n*   [Documentation](https://github.com/Shopify/draggable?screenshot=true#documentation)\n*   [Contributing](https://github.com/Shopify/draggable?screenshot=true#contributing)\n*   [Roadmap](https://github.com/Shopify/draggable?screenshot=true#roadmap)\n*   [Copyright](https://github.com/Shopify/draggable?screenshot=true#copyright)\n\nInstall\n-------\n\n[](https://github.com/Shopify/draggable?screenshot=true#install)\n\nYou can install the library via npm.\n\nnpm install @shopify/draggable --save\n\nor via yarn:\n\nyarn add @shopify/draggable\n\nor via CDN\n\n<!-- Entire bundle --\\>\n<script type\\=\"module\"\\>\n  import {\n    Draggable,\n    Sortable,\n    Droppable,\n    Swappable,\n  } from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/index.mjs';\n</script\\>\n<!-- Draggable only --\\>\n<script type\\=\"module\"\\>\n  import Draggable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Draggable/Draggable.mjs';\n</script\\>\n<!-- Sortable only --\\>\n<script type\\=\"module\"\\>\n  import Sortable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Sortable/Sortable.mjs';\n</script\\>\n<!-- Droppable only --\\>\n<script type\\=\"module\"\\>\n  import Droppable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Droppable/Droppable.mjs';\n</script\\>\n<!-- Swappable only --\\>\n<script type\\=\"module\"\\>\n  import Swappable from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Swappable/Swappable.mjs';\n</script\\>\n<!-- Plugins only --\\>\n<script type\\=\"module\"\\>\n  import \\* as Plugins from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/Plugins/index.mjs';\n</script\\>\n<!-- UMD browser --\\>\n<script src\\=\"https://cdn.jsdelivr.net/npm/@shopify/draggable/build/umd/index.min.js\"\\></script\\>\n<script\\>\n  console.log(window.Draggable);\n</script\\>\n\nBrowser Compatibility\n---------------------\n\n[](https://github.com/Shopify/draggable?screenshot=true#browser-compatibility)\n\nCheck the \"browserlist\" property in [package.json](https://github.com/Shopify/draggable/blob/main/package.json#L88) for more info\n\n| [![Image 41: Chrome](https://camo.githubusercontent.com/c23f02f6604b0b5fee3615832d7f237055892cdda9f8a2c46e62131cf7e7cd12/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6368726f6d652f6368726f6d655f34387834382e706e67)](https://camo.githubusercontent.com/c23f02f6604b0b5fee3615832d7f237055892cdda9f8a2c46e62131cf7e7cd12/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6368726f6d652f6368726f6d655f34387834382e706e67) | [![Image 42: Firefox](https://camo.githubusercontent.com/234a8814dfe9d689612fe6f899acbba9b1385af208cd693bc3b08cfc931ed954/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f66697265666f782f66697265666f785f34387834382e706e67)](https://camo.githubusercontent.com/234a8814dfe9d689612fe6f899acbba9b1385af208cd693bc3b08cfc931ed954/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f66697265666f782f66697265666f785f34387834382e706e67) | [![Image 43: Opera](https://camo.githubusercontent.com/e13076052cc3a8e0e2d3532a7e63bb4b0971cc796768e85f11897b76654f3216/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6f706572612f6f706572615f34387834382e706e67)](https://camo.githubusercontent.com/e13076052cc3a8e0e2d3532a7e63bb4b0971cc796768e85f11897b76654f3216/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6f706572612f6f706572615f34387834382e706e67) | [![Image 44: Safari](https://camo.githubusercontent.com/40dd86d718fa616895f201e601dfe0d1988c01c5a57c27fe6f104999eef377a2/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f7361666172692f7361666172695f34387834382e706e67)](https://camo.githubusercontent.com/40dd86d718fa616895f201e601dfe0d1988c01c5a57c27fe6f104999eef377a2/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f7361666172692f7361666172695f34387834382e706e67) | [![Image 45: Edge](https://camo.githubusercontent.com/490746383ccfcbcadcb2d362870f855731dbe73c3230b171d31f5b090406816e/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f656467652f656467655f34387834382e706e67)](https://camo.githubusercontent.com/490746383ccfcbcadcb2d362870f855731dbe73c3230b171d31f5b090406816e/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f656467652f656467655f34387834382e706e67) |\n| --- | --- | --- | --- | --- |\n| Last 3 versions ✔ | Last 3 versions ✔ | Last 3 versions ✔ | Last 3 versions ✔ | Last 3 versions ✔ |\n\nDocumentation\n-------------\n\n[](https://github.com/Shopify/draggable?screenshot=true#documentation)\n\nYou can find the documentation for each module within their respective directories.\n\n*   [Draggable](https://github.com/Shopify/draggable/blob/main/src/Draggable)\n    *   [DragEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/DragEvent)\n    *   [DraggableEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/DraggableEvent)\n    *   [Plugins](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins)\n        *   [Announcement](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Announcement)\n        *   [Focusable](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Focusable)\n        *   [Mirror](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Mirror)\n        *   [MirrorEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Mirror/MirrorEvent)\n        *   [Scrollable](https://github.com/Shopify/draggable/blob/main/src/Draggable/Plugins/Scrollable)\n    *   [Sensors](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors)\n        *   [DragSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/DragSensor)\n        *   [ForceTouchSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/ForceTouchSensor)\n        *   [MouseSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/MouseSensor)\n        *   [Sensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/Sensor)\n        *   [SensorEvent](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/SensorEvent)\n        *   [TouchSensor](https://github.com/Shopify/draggable/blob/main/src/Draggable/Sensors/TouchSensor)\n*   [Droppable](https://github.com/Shopify/draggable/blob/main/src/Droppable)\n    *   [DroppableEvent](https://github.com/Shopify/draggable/blob/main/src/Droppable/DroppableEvent)\n*   [Plugins](https://github.com/Shopify/draggable/blob/main/src/Plugins)\n    *   [Collidable](https://github.com/Shopify/draggable/blob/main/src/Plugins/Collidable)\n    *   [ResizeMirror](https://github.com/Shopify/draggable/blob/main/src/Plugins/ResizeMirror)\n    *   [Snappable](https://github.com/Shopify/draggable/blob/main/src/Plugins/Snappable)\n    *   [SwapAnimation](https://github.com/Shopify/draggable/blob/main/src/Plugins/SwapAnimation)\n    *   [SortAnimation](https://github.com/Shopify/draggable/blob/main/src/Plugins/SortAnimation)\n*   [Sortable](https://github.com/Shopify/draggable/blob/main/src/Sortable)\n    *   [SortableEvent](https://github.com/Shopify/draggable/blob/main/src/Sortable/SortableEvent)\n*   [Swappable](https://github.com/Shopify/draggable/blob/main/src/Swappable)\n    *   [SwappableEvent](https://github.com/Shopify/draggable/blob/main/src/Swappable/SwappableEvent)\n\n### TypeScript\n\n[](https://github.com/Shopify/draggable?screenshot=true#typescript)\n\nDraggable includes [TypeScript](http://typescriptlang.org/) definitions.\n\n[Documentation](https://github.com/Shopify/draggable/blob/main/doc/typescript.md)\n\nRunning examples\n----------------\n\n[](https://github.com/Shopify/draggable?screenshot=true#running-examples)\n\nTo run the `examples` project locally, simply run the following from the `draggable` root:\n\nThis will start a server that hosts the contents of `examples/`. It also watches for file changes from both `src/` and `examples/src` and reloads the browser.\n\nContributing\n------------\n\n[](https://github.com/Shopify/draggable?screenshot=true#contributing)\n\nContributions are more than welcome, the code base is still new and needs more love.\n\nFor more information, please checkout the [contributing document](https://github.com/Shopify/draggable/blob/main/CONTRIBUTING.md).\n\nRelated resources\n-----------------\n\n[](https://github.com/Shopify/draggable?screenshot=true#related-resources)\n\n*   [Ember CLI Shim](https://github.com/timrourke/ember-cli-shopify-draggable-shim) on Github by [@timrourke](https://github.com/timrourke)\n*   [Ember CLI Shim](https://www.npmjs.com/package/ember-cli-shopify-draggable-shim) on NPM by [@timrourke](https://github.com/timrourke)\n\nCopyright\n---------\n\n[](https://github.com/Shopify/draggable?screenshot=true#copyright)\n\nCopyright (c) 2018-present Shopify. See LICENSE.md for further details.",
  "usage": {
    "tokens": 3964
  }
}
```
