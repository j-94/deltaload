---
title: GitHub - NotionX/react-notion-x: Fast and accurate React renderer for Notion. TS batteries included. ⚡️
description: Fast and accurate React renderer for Notion. TS batteries included. ⚡️ - NotionX/react-notion-x
url: https://github.com/NotionX/react-notion-x
timestamp: 2025-01-20T15:32:01.763Z
domain: github.com
path: NotionX_react-notion-x
---

# GitHub - NotionX/react-notion-x: Fast and accurate React renderer for Notion. TS batteries included. ⚡️


Fast and accurate React renderer for Notion. TS batteries included. ⚡️ - NotionX/react-notion-x


## Content

[![Image 51: React Notion X](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/notion-ts.png)](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/notion-ts.png)

React Notion X
--------------

[](https://github.com/NotionX/react-notion-x?screenshot=true#react-notion-x)

> Fast and accurate React renderer for Notion. TS batteries included. ⚡️

[![Image 52: NPM](https://camo.githubusercontent.com/76355cb886c6575519e2b1172758834c748f1726d7533af293375736663cde4e/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e6f74696f6e2d782e737667)](https://www.npmjs.com/package/react-notion-x) [![Image 53: Build Status](https://github.com/NotionX/react-notion-x/actions/workflows/test.yml/badge.svg)](https://github.com/NotionX/react-notion-x/actions/workflows/test.yml) [![Image 54: Prettier Code Formatting](https://camo.githubusercontent.com/18237e48c39124504c2ed1cf0304bc20f83b7ba172be82c474c0be62700de958/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64655f7374796c652d70726574746965722d627269676874677265656e2e737667)](https://prettier.io/) [![Image 55: NPM](https://camo.githubusercontent.com/8311a3079719e908d10500c9dfaaa85dd7c1e9aeaa2b7c3b2b2739a73e272a1a/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d6e6f74696f6e2d78)](https://bundlephobia.com/package/react-notion-x)

Contents
--------

[](https://github.com/NotionX/react-notion-x?screenshot=true#contents)

*   [React Notion X](https://github.com/NotionX/react-notion-x?screenshot=true#react-notion-x)
    *   [Contents](https://github.com/NotionX/react-notion-x?screenshot=true#contents)
    *   [Advice](https://github.com/NotionX/react-notion-x?screenshot=true#advice)
    *   [Features](https://github.com/NotionX/react-notion-x?screenshot=true#features)
    *   [Usage](https://github.com/NotionX/react-notion-x?screenshot=true#usage)
    *   [Styles](https://github.com/NotionX/react-notion-x?screenshot=true#styles)
    *   [Optional Components](https://github.com/NotionX/react-notion-x?screenshot=true#optional-components)
    *   [Private Pages](https://github.com/NotionX/react-notion-x?screenshot=true#private-pages)
    *   [Next.js Examples](https://github.com/NotionX/react-notion-x?screenshot=true#nextjs-examples)
    *   [Packages](https://github.com/NotionX/react-notion-x?screenshot=true#packages)
    *   [Supported Blocks](https://github.com/NotionX/react-notion-x?screenshot=true#supported-blocks)
    *   [Performance](https://github.com/NotionX/react-notion-x?screenshot=true#performance)
    *   [Related](https://github.com/NotionX/react-notion-x?screenshot=true#related)
    *   [Contributing](https://github.com/NotionX/react-notion-x?screenshot=true#contributing)
    *   [License](https://github.com/NotionX/react-notion-x?screenshot=true#license)
    *   [Sponsor](https://github.com/NotionX/react-notion-x?screenshot=true#sponsor)

Advice
------

[](https://github.com/NotionX/react-notion-x?screenshot=true#advice)

If you just want to publish a website using Notion, then we highly recommend using [Super.so](https://s.super.so/x) — a hosted solution with great perf that takes care of all the details for you.

If you want more control over your website via React, then we recommend checking out the accompanying [Next.js starter kit](https://github.com/transitive-bullshit/nextjs-notion-starter-kit), which is free and uses `react-notion-x` under the hood.

And if you want even more control, then you're in the right place! 👇👇

Features
--------

[](https://github.com/NotionX/react-notion-x?screenshot=true#features)

*   🚀 **Simple** - TypeScript + React
*   ⚡ **Fast** - 10-100x faster than Notion
    *   95-100% Lighthouse scores
    *   Heavier components can be loaded lazily via `next/dynamic`
*   💯 **Tests** - Comes with a comprehensive [test suite](https://www.notion.so/Notion-Test-Suite-067dd719a912471ea9a3ac10710e7fdf) covering most of Notion's functionality
*   🔥 **Solid** - Used in production by [Potion](https://www.potion.so/) and thousands of websites
*   💪 **Smooth** - Supports `next/image` along with LQIP preview images ([demo](https://react-notion-x-demo.transitivebullsh.it/3492bd6dbaf44fe7a5cac62c5d402f06))
*   Framework agnostic - Use with next.js, create-react-app, gatsby, etc

Usage
-----

[](https://github.com/NotionX/react-notion-x?screenshot=true#usage)

First you'll want to fetch the content for a Notion page:

import { NotionAPI } from 'notion-client'

const notion \= new NotionAPI()

const recordMap \= await notion.getPage('067dd719a912471ea9a3ac10710e7fdf')

Once you have the data for a Notion page, you can render it via React:

import \* as React from 'react'
import { NotionRenderer } from 'react-notion-x'

export default ({ recordMap }) \=\> (
  <NotionRenderer recordMap\={recordMap} fullPage\={true} darkMode\={false} /\>
)

Note: for heavier blocks, you'll have to opt into using them via `NotionRenderer.components`. These are not included in the default `NotionRenderer` export because they're too heavyweight for many use cases.

Styles
------

[](https://github.com/NotionX/react-notion-x?screenshot=true#styles)

You'll need to import some CSS styles as well. If you're using Next.js, we recommend you place these imports at the top of `pages/_app.js`:

// core styles shared by all of react-notion-x (required)
import 'react-notion-x/src/styles.css'

// used for code syntax highlighting (optional)
import 'prismjs/themes/prism-tomorrow.css'

// used for rendering equations (optional)
import 'katex/dist/katex.min.css'

Optional Components
-------------------

[](https://github.com/NotionX/react-notion-x?screenshot=true#optional-components)

The default imports from `react-notion-x` strive to be as lightweight as possible. Most blocks will render just fine, but some larger blocks like PDFs and collection views (database views) are not included by default.

To use them, you'll need to import the ones you want from `react-notion-x/build/third-party/*`:

import { Code } from 'react-notion-x/build/third-party/code'
import { Collection } from 'react-notion-x/build/third-party/collection'
import { Equation } from 'react-notion-x/build/third-party/equation'
import { Modal } from 'react-notion-x/build/third-party/modal'
import { Pdf } from 'react-notion-x/build/third-party/pdf'

Note that we strongly recommend lazy-loading these components unless you know you'll need them up front for your use case.

If you're using Next.js, you can use [next/dynamic](https://nextjs.org/docs/advanced-features/dynamic-import) to lazily load them. If your notion content doesn't use one of these heavyweight components, then it won't get loaded into your page. This keeps the initial page bundle small and your website feeling snappy.

import dynamic from 'next/dynamic'

const Code \= dynamic(() \=\>
  import('react-notion-x/build/third-party/code').then((m) \=\> m.Code)
)
const Collection \= dynamic(() \=\>
  import('react-notion-x/build/third-party/collection').then(
    (m) \=\> m.Collection
  )
)
const Equation \= dynamic(() \=\>
  import('react-notion-x/build/third-party/equation').then((m) \=\> m.Equation)
)
const Pdf \= dynamic(
  () \=\> import('react-notion-x/build/third-party/pdf').then((m) \=\> m.Pdf),
  {
    ssr: false
  }
)
const Modal \= dynamic(
  () \=\> import('react-notion-x/build/third-party/modal').then((m) \=\> m.Modal),
  {
    ssr: false
  }
)

You'll need to enable them by passing them to the `components` prop of `NotionRenderer`.

export default ({ recordMap }) \=\> (
  <NotionRenderer
    recordMap\={recordMap}
    components\={{
      Code,
      Collection,
      Equation,
      Modal,
      Pdf
    }}
  /\>
)

The `Code` component uses [Prism](https://prismjs.com/) under the hood. It comes bundled with support for JavaScript, TypeScript, and CSS by default. To add support for additional language syntaxes, follow the example in [`components/NotionPage.tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/full/components/NotionPage.tsx) which lazily loads Prism components at runtime. You will likely want to add `prismjs` to your project as a dependency when using the `Code` component so TypeScript doesn't complain.

For `Equation` support, you'll need to import the katex CSS styles.

For each of these optional components, make sure you're also importing the relevant third-party CSS if needed ([above](https://github.com/NotionX/react-notion-x?screenshot=true#Styles)).

Private Pages
-------------

[](https://github.com/NotionX/react-notion-x?screenshot=true#private-pages)

You may optionally pass an `authToken` and `activeUser` to the API if you want to access private Notion pages. Both can be retrieved from your web browser. Once you are viewing your workpace, open your Development Tools \> Application \> Cookie \> and Copy the `token_v2` and `notion_user_id`. Respectively, activeUser: notion\_user\_id, authToken: token\_v2.

We recommend storing these as environment variables and passing them into the `NotionAPI` constructor as follows:

const notion \= new NotionAPI({
  activeUser: process.env.NOTION\_ACTIVE\_USER,
  authToken: process.env.NOTION\_TOKEN\_V2
})

Note that this is not the same as the API token provided by the official Notion API since `notion-client` uses the unofficial Notion API (which is what all Notion apps use).

Next.js Examples
----------------

[](https://github.com/NotionX/react-notion-x?screenshot=true#nextjs-examples)

Here's a [minimal Next.js example project](https://github.com/NotionX/react-notion-x/blob/master/examples/minimal) with the most important code in [`pages/[pageId].tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/minimal/pages/%5BpageId%5D.tsx) and [`components/NotionPage.tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/minimal/components/NotionPage.tsx). You can view this example [live on Vercel](https://react-notion-x-minimal-demo.transitivebullsh.it/).

Here's a more [full-featured Next.js example project](https://github.com/NotionX/react-notion-x/blob/master/examples/full) with the most important code in [`pages/[pageId].tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/full/pages/%5BpageId%5D.tsx) and [`components/NotionPage.tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/full/components/NotionPage.tsx). You can view this example [live on Vercel](https://react-notion-x-demo.transitivebullsh.it/).

The full-featured demo adds a few nice features:

*   Uses [next/image](https://nextjs.org/docs/api-reference/next/image) to serve optimal images
*   Uses preview images generated via [lqip-modern](https://github.com/transitive-bullshit/lqip-modern)
*   Lazily bundles larger optional components via [next/dynamic](https://nextjs.org/docs/advanced-features/dynamic-import)
    *   Code
    *   Equation
    *   Pdf
    *   Modal
    *   Collection (e.g., notion databases including table and gallery views)

For a production example, check out the [Next.js Notion Starter Kit](https://github.com/transitive-bullshit/nextjs-notion-starter-kit), which uses `react-notion-x` under the hood.

Packages
--------

[](https://github.com/NotionX/react-notion-x?screenshot=true#packages)

| Package | NPM | Environment | Description |
| --- | --- | --- | --- |
| [react-notion-x](https://github.com/NotionX/react-notion-x/blob/master/packages/react-notion-x) | [![Image 56: NPM](https://camo.githubusercontent.com/76355cb886c6575519e2b1172758834c748f1726d7533af293375736663cde4e/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e6f74696f6e2d782e737667)](https://www.npmjs.com/package/react-notion-x) | Browser + SSR | Fast React renderer for Notion. |
| [notion-client](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-client) | [![Image 57: NPM](https://camo.githubusercontent.com/6b5e2d0a5b6a01a2db30bb8f6172dec7851de80029f221d1aa1716787e893cd8/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6e6f74696f6e2d636c69656e742e737667)](https://www.npmjs.com/package/notion-client) | Server-side\* | Robust TypeScript client for the Notion API. |
| [notion-types](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-types) | [![Image 58: NPM](https://camo.githubusercontent.com/56b471da498dbadf1bc6b9a1da93fec937a56f9c22191c31316b59b80c210982/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6e6f74696f6e2d74797065732e737667)](https://www.npmjs.com/package/notion-types) | Universal | Core Notion TypeScript types. |
| [notion-utils](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-utils) | [![Image 59: NPM](https://camo.githubusercontent.com/8fe95f8556b81ce07f2d53bbcede3f8fa051779b6b1c6ce01157d79d992d59ec/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6e6f74696f6e2d7574696c732e737667)](https://www.npmjs.com/package/notion-utils) | Universal | Useful utilities for working with Notion data. |

\* Notion's API should not be called from client-side browsers due to CORS restrictions. `notion-client` is compatible with Node.js and Deno.

Supported Blocks
----------------

[](https://github.com/NotionX/react-notion-x?screenshot=true#supported-blocks)

The majority of Notion blocks and collection views are fully supported.

| Block Type | Supported | Block Type Enum | Notes |
| --- | --- | --- | --- |
| Page | ✅ Yes | `page` |  |
| Text | ✅ Yes | `text` | Supports all known text formatting options |
| Bookmark | ✅ Yes | `bookmark` | Embedded preview of external URL |
| Bulleted List | ✅ Yes | `bulleted_list` | `<ul>` |
| Numbered List | ✅ Yes | `numbered_list` | `<ol>` |
| Heading 1 | ✅ Yes | `header` | `<h1>` |
| Heading 2 | ✅ Yes | `sub_header` | `<h2>` |
| Heading 3 | ✅ Yes | `sub_sub_header` | `<h3>` |
| Quote | ✅ Yes | `quote` |  |
| Callout | ✅ Yes | `callout` |  |
| Equation (block) | ✅ Yes | `equation` | [katex](https://katex.org/) via [react-katex](https://github.com/MatejBransky/react-katex) |
| Equation (inline) | ✅ Yes | `text` | [katex](https://katex.org/) via [react-katex](https://github.com/MatejBransky/react-katex) |
| Todos (checkboxes) | ✅ Yes | `to_do` |  |
| Table Of Contents | ✅ Yes | `table_of_contents` | See `notion-utils` `getPageTableOfContents` helper funtion |
| Divider | ✅ Yes | `divider` | Horizontal line |
| Column | ✅ Yes | `column` |  |
| Column List | ✅ Yes | `column_list` |  |
| Toggle | ✅ Yes | `toggle` | [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) |
| Image | ✅ Yes | `image` | `<img>` |
| Embed | ✅ Yes | `embed` | Generic `iframe` embeds |
| Video | ✅ Yes | `video` | `iframe` |
| Figma | ✅ Yes | `figma` | `iframe` |
| Google Maps | ✅ Yes | `maps` | `iframe` |
| Google Drive | ✅ Yes | `drive` | Google Docs, Sheets, etc custom embed |
| Tweet | ✅ Yes | `tweet` | Uses the twitter embedding SDK |
| PDF | ✅ Yes | `pdf` | Uses S3 signed URLs and [react-pdf](https://github.com/wojtekmaj/react-pdf) |
| Audio | ✅ Yes | `audio` | Uses S3 signed URLs and [HTML5 `audio` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) |
| File | ✅ Yes | `file` | Uses S3 signed URLs (generic downloadable file) |
| Link | ✅ Yes | `text` | External links |
| Page Link | ✅ Yes | `page` | Link to a notion page in the same workspace |
| External Page Link | ✅ Yes | `text` | Links to a notion page or collection view in another workspace |
| Code (block) | ✅ Yes | `code` | Block code syntax highlighting via [prismjs](https://prismjs.com/) |
| Code (inline) | ✅ Yes | `text` | Inline code formatting (no syntax highlighting) |
| Collections | ✅ Yes |  | Also known as [databases](https://www.notion.so/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e) |
| Collection View | ✅ Yes | `collection_view` | Collections have a 1:N mapping to collection views |
| Collection View Table | ✅ Yes | `collection_view` | `type = "table"` (default table view) |
| Collection View Gallery | ✅ Yes | `collection_view` | `type = "gallery"` (grid view) |
| Collection View Board | ✅ Yes | `collection_view` | `type = "board"` (kanban view) |
| Collection View List | ✅ Yes | `collection_view` | `type = "list"` (vertical list view) |
| Collection View Calendar | ❌ Missing | `collection_view` | `type = "calendar"` (embedded calendar view) |
| Collection View Page | ✅ Yes | `collection_view_page` | Collection view as a standalone page |

Please let us know if you find any issues or missing blocks.

All known blocks and most known configuration settings can be found in our [test suite](https://www.notion.so/Notion-Test-Suite-067dd719a912471ea9a3ac10710e7fdf).

Performance
-----------

[](https://github.com/NotionX/react-notion-x?screenshot=true#performance)

[![Image 60: Google Lighthouse Scores](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/react-notion-x-perf.png)](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/react-notion-x-perf.png)  
_Google Lighthouse scores for an [example page](https://react-notion-x-demo.transitivebullsh.it/38fa73d49b8f40aab1f3f8c82332e518) rendered by \`react-notion-x\` on Vercel._

[![Image 61: Bundlephobia](https://camo.githubusercontent.com/8311a3079719e908d10500c9dfaaa85dd7c1e9aeaa2b7c3b2b2739a73e272a1a/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d6e6f74696f6e2d78)](https://bundlephobia.com/package/react-notion-x "Bundlephobia")

Out of the box, `react-notion-x` is pretty fast and relatively lightweight, but there are a few key factors to be aware of.

Bundlephobia reports a [~28kb gzip bundle size](https://bundlephobia.com/result?p=react-notion-x) for the main `react-notion-x` bundle. This doesn't include the optional `third-party` components which we recommend lazy loading via [next/dynamic](https://nextjs.org/docs/advanced-features/dynamic-import) only if a page needs them.

Another major factor for perf comes from images hosted by Notion. They're generally unoptimized, improperly sized, and not cacheable because Notion has to deal with fine-grained access control that users can change at any time. You can override the default `mapImageUrl` function on `NotionRenderer` to add caching via a CDN like Cloudflare Workers, which is what Notion X does for optimal page load speeds.

`NotionRenderer` also supports lazy image loading with optional low quality image placeholder previews. You can see a demo of this in practice [on this page](https://react-notion-x-demo.transitivebullsh.it/3492bd6dbaf44fe7a5cac62c5d402f06) which is using [lqip-modern](https://github.com/transitive-bullshit/lqip-modern) to pre-generate placeholder images that are inspired by Medium.com's image loading.

If you're using Next.js, we recommend passing `next/image` or `next/legacy/image`, and `next/link` to the renderer as follows:

import Image from 'next/image' // or import Image from 'next/legacy/image' if you use legacy Image
import Link from 'next/link'

export default ({ recordMap }) \=\> (
  <NotionRenderer
    recordMap\={recordMap}
    components\={{
      nextImage: Image, // or nextLegacyImage: LegacyImage,
      nextLink: Link
    }}
  /\>
)

This wraps these next.js components in a compatability layer so `NotionRenderer` can use them the same as their non-next.js equivalents `<img>` and `<a>`.

Note that custom image component is currently only enabled with preview image or by turning on `forceCustomImages` of `NotionRenderer`.

Related
-------

[](https://github.com/NotionX/react-notion-x?screenshot=true#related)

*   [Next.js Template](https://github.com/transitive-bullshit/nextjs-notion-starter-kit) - The easiest way to deploy a self-hosted Notion site with Next.js and Vercel.
    *   Only takes a few minutes to setup!
    *   Uses `react-notion-x` under the hood
*   [Notion Test Suite](https://www.notion.so/Notion-Test-Suite-067dd719a912471ea9a3ac10710e7fdf) - Comprehensive suite of Notion test pages
*   [react-notion](https://github.com/splitbee/react-notion) - Original react renderer for notion
    *   `react-notion-x` started as a fork of `react-notion` with better support for different types of Notion content (especially collections) and grew into something much more comprehensive
    *   `react-notion` is no longer actively maintained
*   [notion-api-worker](https://github.com/splitbee/notion-api-worker) - Notion API proxy exposed as a Cloudflare Worker
    *   `notion-types` and `notion-client` are a rewrite of `notion-api-worker`
    *   One of the main use cases for `react-notion-x` is server-side rendering via Next.js, in which case the CF worker is unnecessary
    *   We recommend that you use [notion-client](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-client) instead
*   [notion-py](https://github.com/jamalex/notion-py) - Python wrapper around the Notion API

Contributing
------------

[](https://github.com/NotionX/react-notion-x?screenshot=true#contributing)

See the [contribution guide](https://github.com/NotionX/react-notion-x/blob/master/contributing.md) and join our amazing list of [contributors](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/graphs/contributors)!

License
-------

[](https://github.com/NotionX/react-notion-x?screenshot=true#license)

MIT © [Travis Fischer](https://transitivebullsh.it/)

This project extends MIT-licensed work by [Timo Lins](https://twitter.com/timolins), [Tobias Lins](https://twitter.com/linstobias), [Sam Wight](https://samw.dev/), and other contributors.

Support my OSS work by [following me on twitter ![Image 62: twitter](https://camo.githubusercontent.com/51c43f5678a4cc8d9f9f70cb16d8fe57ebc02a34a3021bec68ee0e416fbbd72c/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f736161736966792d6173736574732f747769747465722d6c6f676f2e737667)](https://twitter.com/transitive_bs)

Sponsor
-------

[](https://github.com/NotionX/react-notion-x?screenshot=true#sponsor)

[Super.so](https://s.super.so/x) has been kind enough to sponsor this project. If you're looking for a hosted solution that takes a very similar approach to `react-notion-x` but handles all of the details for you, then definitely check them out.

[![Image 63: React Notion X](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/super-so-banner.png)](https://s.super.so/x "Super.so")

## Metadata

```json
{
  "title": "GitHub - NotionX/react-notion-x: Fast and accurate React renderer for Notion. TS batteries included. ⚡️",
  "description": "Fast and accurate React renderer for Notion. TS batteries included. ⚡️ - NotionX/react-notion-x",
  "url": "https://github.com/NotionX/react-notion-x?screenshot=true",
  "content": "[![Image 51: React Notion X](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/notion-ts.png)](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/notion-ts.png)\n\nReact Notion X\n--------------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#react-notion-x)\n\n> Fast and accurate React renderer for Notion. TS batteries included. ⚡️\n\n[![Image 52: NPM](https://camo.githubusercontent.com/76355cb886c6575519e2b1172758834c748f1726d7533af293375736663cde4e/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e6f74696f6e2d782e737667)](https://www.npmjs.com/package/react-notion-x) [![Image 53: Build Status](https://github.com/NotionX/react-notion-x/actions/workflows/test.yml/badge.svg)](https://github.com/NotionX/react-notion-x/actions/workflows/test.yml) [![Image 54: Prettier Code Formatting](https://camo.githubusercontent.com/18237e48c39124504c2ed1cf0304bc20f83b7ba172be82c474c0be62700de958/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64655f7374796c652d70726574746965722d627269676874677265656e2e737667)](https://prettier.io/) [![Image 55: NPM](https://camo.githubusercontent.com/8311a3079719e908d10500c9dfaaa85dd7c1e9aeaa2b7c3b2b2739a73e272a1a/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d6e6f74696f6e2d78)](https://bundlephobia.com/package/react-notion-x)\n\nContents\n--------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#contents)\n\n*   [React Notion X](https://github.com/NotionX/react-notion-x?screenshot=true#react-notion-x)\n    *   [Contents](https://github.com/NotionX/react-notion-x?screenshot=true#contents)\n    *   [Advice](https://github.com/NotionX/react-notion-x?screenshot=true#advice)\n    *   [Features](https://github.com/NotionX/react-notion-x?screenshot=true#features)\n    *   [Usage](https://github.com/NotionX/react-notion-x?screenshot=true#usage)\n    *   [Styles](https://github.com/NotionX/react-notion-x?screenshot=true#styles)\n    *   [Optional Components](https://github.com/NotionX/react-notion-x?screenshot=true#optional-components)\n    *   [Private Pages](https://github.com/NotionX/react-notion-x?screenshot=true#private-pages)\n    *   [Next.js Examples](https://github.com/NotionX/react-notion-x?screenshot=true#nextjs-examples)\n    *   [Packages](https://github.com/NotionX/react-notion-x?screenshot=true#packages)\n    *   [Supported Blocks](https://github.com/NotionX/react-notion-x?screenshot=true#supported-blocks)\n    *   [Performance](https://github.com/NotionX/react-notion-x?screenshot=true#performance)\n    *   [Related](https://github.com/NotionX/react-notion-x?screenshot=true#related)\n    *   [Contributing](https://github.com/NotionX/react-notion-x?screenshot=true#contributing)\n    *   [License](https://github.com/NotionX/react-notion-x?screenshot=true#license)\n    *   [Sponsor](https://github.com/NotionX/react-notion-x?screenshot=true#sponsor)\n\nAdvice\n------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#advice)\n\nIf you just want to publish a website using Notion, then we highly recommend using [Super.so](https://s.super.so/x) — a hosted solution with great perf that takes care of all the details for you.\n\nIf you want more control over your website via React, then we recommend checking out the accompanying [Next.js starter kit](https://github.com/transitive-bullshit/nextjs-notion-starter-kit), which is free and uses `react-notion-x` under the hood.\n\nAnd if you want even more control, then you're in the right place! 👇👇\n\nFeatures\n--------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#features)\n\n*   🚀 **Simple** - TypeScript + React\n*   ⚡ **Fast** - 10-100x faster than Notion\n    *   95-100% Lighthouse scores\n    *   Heavier components can be loaded lazily via `next/dynamic`\n*   💯 **Tests** - Comes with a comprehensive [test suite](https://www.notion.so/Notion-Test-Suite-067dd719a912471ea9a3ac10710e7fdf) covering most of Notion's functionality\n*   🔥 **Solid** - Used in production by [Potion](https://www.potion.so/) and thousands of websites\n*   💪 **Smooth** - Supports `next/image` along with LQIP preview images ([demo](https://react-notion-x-demo.transitivebullsh.it/3492bd6dbaf44fe7a5cac62c5d402f06))\n*   Framework agnostic - Use with next.js, create-react-app, gatsby, etc\n\nUsage\n-----\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#usage)\n\nFirst you'll want to fetch the content for a Notion page:\n\nimport { NotionAPI } from 'notion-client'\n\nconst notion \\= new NotionAPI()\n\nconst recordMap \\= await notion.getPage('067dd719a912471ea9a3ac10710e7fdf')\n\nOnce you have the data for a Notion page, you can render it via React:\n\nimport \\* as React from 'react'\nimport { NotionRenderer } from 'react-notion-x'\n\nexport default ({ recordMap }) \\=\\> (\n  <NotionRenderer recordMap\\={recordMap} fullPage\\={true} darkMode\\={false} /\\>\n)\n\nNote: for heavier blocks, you'll have to opt into using them via `NotionRenderer.components`. These are not included in the default `NotionRenderer` export because they're too heavyweight for many use cases.\n\nStyles\n------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#styles)\n\nYou'll need to import some CSS styles as well. If you're using Next.js, we recommend you place these imports at the top of `pages/_app.js`:\n\n// core styles shared by all of react-notion-x (required)\nimport 'react-notion-x/src/styles.css'\n\n// used for code syntax highlighting (optional)\nimport 'prismjs/themes/prism-tomorrow.css'\n\n// used for rendering equations (optional)\nimport 'katex/dist/katex.min.css'\n\nOptional Components\n-------------------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#optional-components)\n\nThe default imports from `react-notion-x` strive to be as lightweight as possible. Most blocks will render just fine, but some larger blocks like PDFs and collection views (database views) are not included by default.\n\nTo use them, you'll need to import the ones you want from `react-notion-x/build/third-party/*`:\n\nimport { Code } from 'react-notion-x/build/third-party/code'\nimport { Collection } from 'react-notion-x/build/third-party/collection'\nimport { Equation } from 'react-notion-x/build/third-party/equation'\nimport { Modal } from 'react-notion-x/build/third-party/modal'\nimport { Pdf } from 'react-notion-x/build/third-party/pdf'\n\nNote that we strongly recommend lazy-loading these components unless you know you'll need them up front for your use case.\n\nIf you're using Next.js, you can use [next/dynamic](https://nextjs.org/docs/advanced-features/dynamic-import) to lazily load them. If your notion content doesn't use one of these heavyweight components, then it won't get loaded into your page. This keeps the initial page bundle small and your website feeling snappy.\n\nimport dynamic from 'next/dynamic'\n\nconst Code \\= dynamic(() \\=\\>\n  import('react-notion-x/build/third-party/code').then((m) \\=\\> m.Code)\n)\nconst Collection \\= dynamic(() \\=\\>\n  import('react-notion-x/build/third-party/collection').then(\n    (m) \\=\\> m.Collection\n  )\n)\nconst Equation \\= dynamic(() \\=\\>\n  import('react-notion-x/build/third-party/equation').then((m) \\=\\> m.Equation)\n)\nconst Pdf \\= dynamic(\n  () \\=\\> import('react-notion-x/build/third-party/pdf').then((m) \\=\\> m.Pdf),\n  {\n    ssr: false\n  }\n)\nconst Modal \\= dynamic(\n  () \\=\\> import('react-notion-x/build/third-party/modal').then((m) \\=\\> m.Modal),\n  {\n    ssr: false\n  }\n)\n\nYou'll need to enable them by passing them to the `components` prop of `NotionRenderer`.\n\nexport default ({ recordMap }) \\=\\> (\n  <NotionRenderer\n    recordMap\\={recordMap}\n    components\\={{\n      Code,\n      Collection,\n      Equation,\n      Modal,\n      Pdf\n    }}\n  /\\>\n)\n\nThe `Code` component uses [Prism](https://prismjs.com/) under the hood. It comes bundled with support for JavaScript, TypeScript, and CSS by default. To add support for additional language syntaxes, follow the example in [`components/NotionPage.tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/full/components/NotionPage.tsx) which lazily loads Prism components at runtime. You will likely want to add `prismjs` to your project as a dependency when using the `Code` component so TypeScript doesn't complain.\n\nFor `Equation` support, you'll need to import the katex CSS styles.\n\nFor each of these optional components, make sure you're also importing the relevant third-party CSS if needed ([above](https://github.com/NotionX/react-notion-x?screenshot=true#Styles)).\n\nPrivate Pages\n-------------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#private-pages)\n\nYou may optionally pass an `authToken` and `activeUser` to the API if you want to access private Notion pages. Both can be retrieved from your web browser. Once you are viewing your workpace, open your Development Tools \\> Application \\> Cookie \\> and Copy the `token_v2` and `notion_user_id`. Respectively, activeUser: notion\\_user\\_id, authToken: token\\_v2.\n\nWe recommend storing these as environment variables and passing them into the `NotionAPI` constructor as follows:\n\nconst notion \\= new NotionAPI({\n  activeUser: process.env.NOTION\\_ACTIVE\\_USER,\n  authToken: process.env.NOTION\\_TOKEN\\_V2\n})\n\nNote that this is not the same as the API token provided by the official Notion API since `notion-client` uses the unofficial Notion API (which is what all Notion apps use).\n\nNext.js Examples\n----------------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#nextjs-examples)\n\nHere's a [minimal Next.js example project](https://github.com/NotionX/react-notion-x/blob/master/examples/minimal) with the most important code in [`pages/[pageId].tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/minimal/pages/%5BpageId%5D.tsx) and [`components/NotionPage.tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/minimal/components/NotionPage.tsx). You can view this example [live on Vercel](https://react-notion-x-minimal-demo.transitivebullsh.it/).\n\nHere's a more [full-featured Next.js example project](https://github.com/NotionX/react-notion-x/blob/master/examples/full) with the most important code in [`pages/[pageId].tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/full/pages/%5BpageId%5D.tsx) and [`components/NotionPage.tsx`](https://github.com/NotionX/react-notion-x/blob/master/examples/full/components/NotionPage.tsx). You can view this example [live on Vercel](https://react-notion-x-demo.transitivebullsh.it/).\n\nThe full-featured demo adds a few nice features:\n\n*   Uses [next/image](https://nextjs.org/docs/api-reference/next/image) to serve optimal images\n*   Uses preview images generated via [lqip-modern](https://github.com/transitive-bullshit/lqip-modern)\n*   Lazily bundles larger optional components via [next/dynamic](https://nextjs.org/docs/advanced-features/dynamic-import)\n    *   Code\n    *   Equation\n    *   Pdf\n    *   Modal\n    *   Collection (e.g., notion databases including table and gallery views)\n\nFor a production example, check out the [Next.js Notion Starter Kit](https://github.com/transitive-bullshit/nextjs-notion-starter-kit), which uses `react-notion-x` under the hood.\n\nPackages\n--------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#packages)\n\n| Package | NPM | Environment | Description |\n| --- | --- | --- | --- |\n| [react-notion-x](https://github.com/NotionX/react-notion-x/blob/master/packages/react-notion-x) | [![Image 56: NPM](https://camo.githubusercontent.com/76355cb886c6575519e2b1172758834c748f1726d7533af293375736663cde4e/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e6f74696f6e2d782e737667)](https://www.npmjs.com/package/react-notion-x) | Browser + SSR | Fast React renderer for Notion. |\n| [notion-client](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-client) | [![Image 57: NPM](https://camo.githubusercontent.com/6b5e2d0a5b6a01a2db30bb8f6172dec7851de80029f221d1aa1716787e893cd8/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6e6f74696f6e2d636c69656e742e737667)](https://www.npmjs.com/package/notion-client) | Server-side\\* | Robust TypeScript client for the Notion API. |\n| [notion-types](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-types) | [![Image 58: NPM](https://camo.githubusercontent.com/56b471da498dbadf1bc6b9a1da93fec937a56f9c22191c31316b59b80c210982/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6e6f74696f6e2d74797065732e737667)](https://www.npmjs.com/package/notion-types) | Universal | Core Notion TypeScript types. |\n| [notion-utils](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-utils) | [![Image 59: NPM](https://camo.githubusercontent.com/8fe95f8556b81ce07f2d53bbcede3f8fa051779b6b1c6ce01157d79d992d59ec/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6e6f74696f6e2d7574696c732e737667)](https://www.npmjs.com/package/notion-utils) | Universal | Useful utilities for working with Notion data. |\n\n\\* Notion's API should not be called from client-side browsers due to CORS restrictions. `notion-client` is compatible with Node.js and Deno.\n\nSupported Blocks\n----------------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#supported-blocks)\n\nThe majority of Notion blocks and collection views are fully supported.\n\n| Block Type | Supported | Block Type Enum | Notes |\n| --- | --- | --- | --- |\n| Page | ✅ Yes | `page` |  |\n| Text | ✅ Yes | `text` | Supports all known text formatting options |\n| Bookmark | ✅ Yes | `bookmark` | Embedded preview of external URL |\n| Bulleted List | ✅ Yes | `bulleted_list` | `<ul>` |\n| Numbered List | ✅ Yes | `numbered_list` | `<ol>` |\n| Heading 1 | ✅ Yes | `header` | `<h1>` |\n| Heading 2 | ✅ Yes | `sub_header` | `<h2>` |\n| Heading 3 | ✅ Yes | `sub_sub_header` | `<h3>` |\n| Quote | ✅ Yes | `quote` |  |\n| Callout | ✅ Yes | `callout` |  |\n| Equation (block) | ✅ Yes | `equation` | [katex](https://katex.org/) via [react-katex](https://github.com/MatejBransky/react-katex) |\n| Equation (inline) | ✅ Yes | `text` | [katex](https://katex.org/) via [react-katex](https://github.com/MatejBransky/react-katex) |\n| Todos (checkboxes) | ✅ Yes | `to_do` |  |\n| Table Of Contents | ✅ Yes | `table_of_contents` | See `notion-utils` `getPageTableOfContents` helper funtion |\n| Divider | ✅ Yes | `divider` | Horizontal line |\n| Column | ✅ Yes | `column` |  |\n| Column List | ✅ Yes | `column_list` |  |\n| Toggle | ✅ Yes | `toggle` | [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) |\n| Image | ✅ Yes | `image` | `<img>` |\n| Embed | ✅ Yes | `embed` | Generic `iframe` embeds |\n| Video | ✅ Yes | `video` | `iframe` |\n| Figma | ✅ Yes | `figma` | `iframe` |\n| Google Maps | ✅ Yes | `maps` | `iframe` |\n| Google Drive | ✅ Yes | `drive` | Google Docs, Sheets, etc custom embed |\n| Tweet | ✅ Yes | `tweet` | Uses the twitter embedding SDK |\n| PDF | ✅ Yes | `pdf` | Uses S3 signed URLs and [react-pdf](https://github.com/wojtekmaj/react-pdf) |\n| Audio | ✅ Yes | `audio` | Uses S3 signed URLs and [HTML5 `audio` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) |\n| File | ✅ Yes | `file` | Uses S3 signed URLs (generic downloadable file) |\n| Link | ✅ Yes | `text` | External links |\n| Page Link | ✅ Yes | `page` | Link to a notion page in the same workspace |\n| External Page Link | ✅ Yes | `text` | Links to a notion page or collection view in another workspace |\n| Code (block) | ✅ Yes | `code` | Block code syntax highlighting via [prismjs](https://prismjs.com/) |\n| Code (inline) | ✅ Yes | `text` | Inline code formatting (no syntax highlighting) |\n| Collections | ✅ Yes |  | Also known as [databases](https://www.notion.so/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e) |\n| Collection View | ✅ Yes | `collection_view` | Collections have a 1:N mapping to collection views |\n| Collection View Table | ✅ Yes | `collection_view` | `type = \"table\"` (default table view) |\n| Collection View Gallery | ✅ Yes | `collection_view` | `type = \"gallery\"` (grid view) |\n| Collection View Board | ✅ Yes | `collection_view` | `type = \"board\"` (kanban view) |\n| Collection View List | ✅ Yes | `collection_view` | `type = \"list\"` (vertical list view) |\n| Collection View Calendar | ❌ Missing | `collection_view` | `type = \"calendar\"` (embedded calendar view) |\n| Collection View Page | ✅ Yes | `collection_view_page` | Collection view as a standalone page |\n\nPlease let us know if you find any issues or missing blocks.\n\nAll known blocks and most known configuration settings can be found in our [test suite](https://www.notion.so/Notion-Test-Suite-067dd719a912471ea9a3ac10710e7fdf).\n\nPerformance\n-----------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#performance)\n\n[![Image 60: Google Lighthouse Scores](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/react-notion-x-perf.png)](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/react-notion-x-perf.png)  \n_Google Lighthouse scores for an [example page](https://react-notion-x-demo.transitivebullsh.it/38fa73d49b8f40aab1f3f8c82332e518) rendered by \\`react-notion-x\\` on Vercel._\n\n[![Image 61: Bundlephobia](https://camo.githubusercontent.com/8311a3079719e908d10500c9dfaaa85dd7c1e9aeaa2b7c3b2b2739a73e272a1a/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d6e6f74696f6e2d78)](https://bundlephobia.com/package/react-notion-x \"Bundlephobia\")\n\nOut of the box, `react-notion-x` is pretty fast and relatively lightweight, but there are a few key factors to be aware of.\n\nBundlephobia reports a [~28kb gzip bundle size](https://bundlephobia.com/result?p=react-notion-x) for the main `react-notion-x` bundle. This doesn't include the optional `third-party` components which we recommend lazy loading via [next/dynamic](https://nextjs.org/docs/advanced-features/dynamic-import) only if a page needs them.\n\nAnother major factor for perf comes from images hosted by Notion. They're generally unoptimized, improperly sized, and not cacheable because Notion has to deal with fine-grained access control that users can change at any time. You can override the default `mapImageUrl` function on `NotionRenderer` to add caching via a CDN like Cloudflare Workers, which is what Notion X does for optimal page load speeds.\n\n`NotionRenderer` also supports lazy image loading with optional low quality image placeholder previews. You can see a demo of this in practice [on this page](https://react-notion-x-demo.transitivebullsh.it/3492bd6dbaf44fe7a5cac62c5d402f06) which is using [lqip-modern](https://github.com/transitive-bullshit/lqip-modern) to pre-generate placeholder images that are inspired by Medium.com's image loading.\n\nIf you're using Next.js, we recommend passing `next/image` or `next/legacy/image`, and `next/link` to the renderer as follows:\n\nimport Image from 'next/image' // or import Image from 'next/legacy/image' if you use legacy Image\nimport Link from 'next/link'\n\nexport default ({ recordMap }) \\=\\> (\n  <NotionRenderer\n    recordMap\\={recordMap}\n    components\\={{\n      nextImage: Image, // or nextLegacyImage: LegacyImage,\n      nextLink: Link\n    }}\n  /\\>\n)\n\nThis wraps these next.js components in a compatability layer so `NotionRenderer` can use them the same as their non-next.js equivalents `<img>` and `<a>`.\n\nNote that custom image component is currently only enabled with preview image or by turning on `forceCustomImages` of `NotionRenderer`.\n\nRelated\n-------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#related)\n\n*   [Next.js Template](https://github.com/transitive-bullshit/nextjs-notion-starter-kit) - The easiest way to deploy a self-hosted Notion site with Next.js and Vercel.\n    *   Only takes a few minutes to setup!\n    *   Uses `react-notion-x` under the hood\n*   [Notion Test Suite](https://www.notion.so/Notion-Test-Suite-067dd719a912471ea9a3ac10710e7fdf) - Comprehensive suite of Notion test pages\n*   [react-notion](https://github.com/splitbee/react-notion) - Original react renderer for notion\n    *   `react-notion-x` started as a fork of `react-notion` with better support for different types of Notion content (especially collections) and grew into something much more comprehensive\n    *   `react-notion` is no longer actively maintained\n*   [notion-api-worker](https://github.com/splitbee/notion-api-worker) - Notion API proxy exposed as a Cloudflare Worker\n    *   `notion-types` and `notion-client` are a rewrite of `notion-api-worker`\n    *   One of the main use cases for `react-notion-x` is server-side rendering via Next.js, in which case the CF worker is unnecessary\n    *   We recommend that you use [notion-client](https://github.com/NotionX/react-notion-x/blob/master/packages/notion-client) instead\n*   [notion-py](https://github.com/jamalex/notion-py) - Python wrapper around the Notion API\n\nContributing\n------------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#contributing)\n\nSee the [contribution guide](https://github.com/NotionX/react-notion-x/blob/master/contributing.md) and join our amazing list of [contributors](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/graphs/contributors)!\n\nLicense\n-------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#license)\n\nMIT © [Travis Fischer](https://transitivebullsh.it/)\n\nThis project extends MIT-licensed work by [Timo Lins](https://twitter.com/timolins), [Tobias Lins](https://twitter.com/linstobias), [Sam Wight](https://samw.dev/), and other contributors.\n\nSupport my OSS work by [following me on twitter ![Image 62: twitter](https://camo.githubusercontent.com/51c43f5678a4cc8d9f9f70cb16d8fe57ebc02a34a3021bec68ee0e416fbbd72c/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f736161736966792d6173736574732f747769747465722d6c6f676f2e737667)](https://twitter.com/transitive_bs)\n\nSponsor\n-------\n\n[](https://github.com/NotionX/react-notion-x?screenshot=true#sponsor)\n\n[Super.so](https://s.super.so/x) has been kind enough to sponsor this project. If you're looking for a hosted solution that takes a very similar approach to `react-notion-x` but handles all of the details for you, then definitely check them out.\n\n[![Image 63: React Notion X](https://raw.githubusercontent.com/NotionX/react-notion-x/master/media/super-so-banner.png)](https://s.super.so/x \"Super.so\")",
  "usage": {
    "tokens": 6416
  }
}
```
