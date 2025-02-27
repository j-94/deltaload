---
title: Utility Kit - Nuxt DevTools
description: Utility kit for easier DevTools integrations.
url: https://devtools.nuxt.com/module/utils-kit
timestamp: 2025-01-20T16:07:16.640Z
domain: devtools.nuxt.com
path: module_utils-kit
---

# Utility Kit - Nuxt DevTools


Utility kit for easier DevTools integrations.


## Content

Since v0.3.0, we are now providing a utility kit for easier DevTools integrations, similar to `@nuxt/kit`.

```
import { addCustomTab } from '@nuxt/devtools-kit'
```

We recommend module authors to install `@nuxt/devtools-kit` as a dependency and `@nuxt/devtools` as a dev dependency.

### [`addCustomTab()`](https://devtools.nuxt.com/module/utils-kit#addcustomtab)

A shorthand for calling the hook `devtools:customTabs`.

```
import { addCustomTab } from '@nuxt/devtools-kit'
addCustomTab(() => ({
  // unique identifier
  name: 'my-module',
  // title to display in the tab
  title: 'My Module',
  // any icon from Iconify, or a URL to an image
  icon: 'carbon:apps',
  // iframe view
  view: {
    type: 'iframe',
    src: '/url-to-your-module-view',
  },
}))
```

### [`refreshCustomTabs()`](https://devtools.nuxt.com/module/utils-kit#refreshcustomtabs)

A shorthand for call hook `devtools:customTabs:refresh`. It will refresh all custom tabs.

### [`startSubprocess()`](https://devtools.nuxt.com/module/utils-kit#startsubprocess)

Start a sub process using `execa` and create a terminal tab in DevTools.

```
import { startSubprocess } from '@nuxt/devtools-kit'
const subprocess = startSubprocess(
  {
    command: 'code-server',
    args: [
      'serve-local',
      '--accept-server-license-terms',
      '--without-connection-token',
      `--port=${port}`,
    ],
  },
  {
    id: 'devtools:vscode',
    name: 'VS Code Server',
    icon: 'logos-visual-studio-code',
  },
)
```

```
subprocess.restart()
subprocess.terminate()
```

### [`extendServerRpc()`](https://devtools.nuxt.com/module/utils-kit#extendserverrpc)

Extend the server RPC with your own methods.

```
import { extendServerRpc } from '@nuxt/devtools-kit'
const rpc = extendServerRpc('my-module', {
  async myMethod() {
    return 'hello'
  },
})
```

Learn more about [Custom RPC functions](https://devtools.nuxt.com/module/guide#custom-rpc-functions).

To provide complex interactions for your module integrations, we recommend to host your own view and display it in devtools via iframe.

To get the infomation from the devtools and the client app, you can do this in your client app:

```
import { useDevtoolsClient } from '@nuxt/devtools-kit/iframe-client'
export const devtoolsClient = useDevtoolsClient()
```

When the iframe been served with the same origin (CORS limitation), devtools will automatically inject `__NUXT_DEVTOOLS__` to the iframe's window object. You can access it as a ref using `useDevtoolsClient()` utility.

### [`useDevtoolsClient()`](https://devtools.nuxt.com/module/utils-kit#usedevtoolsclient)

It will return a ref of `NuxtDevtoolsIframeClient` object that are intially `null` and will be updated when the connection is ready.

`NuxtDevtoolsIframeClient` contains two properties:

*   `host`: APIs to communicate with the main app in browser
*   `devtools`: APIs to communicate with the devtools

`host` can be undefined when devtools are accessed standalone or from a different origin.

For example, you can get the router instance from the client app:

```
const router = computed(() => devtoolsClient.value?.host?.nuxt.vueApp.config.globalProperties?.$router)
```

### [`onDevtoolsClientConnected()`](https://devtools.nuxt.com/module/utils-kit#ondevtoolsclientconnected)

Similiar to `useDevtoolsClient()` but as a callback style:

```
import { onDevtoolsClientConnected } from '@nuxt/devtools-kit/iframe-client'
onDevtoolsClientConnected(async (client) => {
  // client is NuxtDevtoolsIframeClient
  const config = client.devtools.rpc.getServerConfig()
  // ...
})
```

When you have iframe for your devtools view, sometimes you need to communicate with the devtools host (the main app in browser) with a runtime plugin. You can use `@nuxt/devtools-kit/host-client` to do that.

### [`useDevtoolsHostClient()`](https://devtools.nuxt.com/module/utils-kit#usedevtoolshostclient)

It will return a ref of `NuxtDevtoolsHostClient` object that are intially `null` and will be updated when the host is initialized by NuxtDevtools.

```
import { useDevtoolsHostClient } from '@nuxt/devtools-kit/host-client'
export default defineNuxtPlugin({
  name: 'my-module:devtools',
  setup(nuxtApp) {
    const devtoolsHost = useDevtoolsHostClient()
    // ...
  }
})
```

### [`onDevtoolsHostClientConnected()`](https://devtools.nuxt.com/module/utils-kit#ondevtoolshostclientconnected)

Similiar to `useDevtoolsHostClient()` but as a callback style:

```
import { onDevtoolsHostClientConnected } from '@nuxt/devtools-kit/host-client'
onDevtoolsHostClientConnected(async (host) => {
})
```

## Metadata

```json
{
  "title": "Utility Kit - Nuxt DevTools",
  "description": "Utility kit for easier DevTools integrations.",
  "url": "https://devtools.nuxt.com/module/utils-kit",
  "content": "Since v0.3.0, we are now providing a utility kit for easier DevTools integrations, similar to `@nuxt/kit`.\n\n```\nimport { addCustomTab } from '@nuxt/devtools-kit'\n```\n\nWe recommend module authors to install `@nuxt/devtools-kit` as a dependency and `@nuxt/devtools` as a dev dependency.\n\n### [`addCustomTab()`](https://devtools.nuxt.com/module/utils-kit#addcustomtab)\n\nA shorthand for calling the hook `devtools:customTabs`.\n\n```\nimport { addCustomTab } from '@nuxt/devtools-kit'\naddCustomTab(() => ({\n  // unique identifier\n  name: 'my-module',\n  // title to display in the tab\n  title: 'My Module',\n  // any icon from Iconify, or a URL to an image\n  icon: 'carbon:apps',\n  // iframe view\n  view: {\n    type: 'iframe',\n    src: '/url-to-your-module-view',\n  },\n}))\n```\n\n### [`refreshCustomTabs()`](https://devtools.nuxt.com/module/utils-kit#refreshcustomtabs)\n\nA shorthand for call hook `devtools:customTabs:refresh`. It will refresh all custom tabs.\n\n### [`startSubprocess()`](https://devtools.nuxt.com/module/utils-kit#startsubprocess)\n\nStart a sub process using `execa` and create a terminal tab in DevTools.\n\n```\nimport { startSubprocess } from '@nuxt/devtools-kit'\nconst subprocess = startSubprocess(\n  {\n    command: 'code-server',\n    args: [\n      'serve-local',\n      '--accept-server-license-terms',\n      '--without-connection-token',\n      `--port=${port}`,\n    ],\n  },\n  {\n    id: 'devtools:vscode',\n    name: 'VS Code Server',\n    icon: 'logos-visual-studio-code',\n  },\n)\n```\n\n```\nsubprocess.restart()\nsubprocess.terminate()\n```\n\n### [`extendServerRpc()`](https://devtools.nuxt.com/module/utils-kit#extendserverrpc)\n\nExtend the server RPC with your own methods.\n\n```\nimport { extendServerRpc } from '@nuxt/devtools-kit'\nconst rpc = extendServerRpc('my-module', {\n  async myMethod() {\n    return 'hello'\n  },\n})\n```\n\nLearn more about [Custom RPC functions](https://devtools.nuxt.com/module/guide#custom-rpc-functions).\n\nTo provide complex interactions for your module integrations, we recommend to host your own view and display it in devtools via iframe.\n\nTo get the infomation from the devtools and the client app, you can do this in your client app:\n\n```\nimport { useDevtoolsClient } from '@nuxt/devtools-kit/iframe-client'\nexport const devtoolsClient = useDevtoolsClient()\n```\n\nWhen the iframe been served with the same origin (CORS limitation), devtools will automatically inject `__NUXT_DEVTOOLS__` to the iframe's window object. You can access it as a ref using `useDevtoolsClient()` utility.\n\n### [`useDevtoolsClient()`](https://devtools.nuxt.com/module/utils-kit#usedevtoolsclient)\n\nIt will return a ref of `NuxtDevtoolsIframeClient` object that are intially `null` and will be updated when the connection is ready.\n\n`NuxtDevtoolsIframeClient` contains two properties:\n\n*   `host`: APIs to communicate with the main app in browser\n*   `devtools`: APIs to communicate with the devtools\n\n`host` can be undefined when devtools are accessed standalone or from a different origin.\n\nFor example, you can get the router instance from the client app:\n\n```\nconst router = computed(() => devtoolsClient.value?.host?.nuxt.vueApp.config.globalProperties?.$router)\n```\n\n### [`onDevtoolsClientConnected()`](https://devtools.nuxt.com/module/utils-kit#ondevtoolsclientconnected)\n\nSimiliar to `useDevtoolsClient()` but as a callback style:\n\n```\nimport { onDevtoolsClientConnected } from '@nuxt/devtools-kit/iframe-client'\nonDevtoolsClientConnected(async (client) => {\n  // client is NuxtDevtoolsIframeClient\n  const config = client.devtools.rpc.getServerConfig()\n  // ...\n})\n```\n\nWhen you have iframe for your devtools view, sometimes you need to communicate with the devtools host (the main app in browser) with a runtime plugin. You can use `@nuxt/devtools-kit/host-client` to do that.\n\n### [`useDevtoolsHostClient()`](https://devtools.nuxt.com/module/utils-kit#usedevtoolshostclient)\n\nIt will return a ref of `NuxtDevtoolsHostClient` object that are intially `null` and will be updated when the host is initialized by NuxtDevtools.\n\n```\nimport { useDevtoolsHostClient } from '@nuxt/devtools-kit/host-client'\nexport default defineNuxtPlugin({\n  name: 'my-module:devtools',\n  setup(nuxtApp) {\n    const devtoolsHost = useDevtoolsHostClient()\n    // ...\n  }\n})\n```\n\n### [`onDevtoolsHostClientConnected()`](https://devtools.nuxt.com/module/utils-kit#ondevtoolshostclientconnected)\n\nSimiliar to `useDevtoolsHostClient()` but as a callback style:\n\n```\nimport { onDevtoolsHostClientConnected } from '@nuxt/devtools-kit/host-client'\nonDevtoolsHostClientConnected(async (host) => {\n})\n```",
  "usage": {
    "tokens": 1165
  }
}
```
