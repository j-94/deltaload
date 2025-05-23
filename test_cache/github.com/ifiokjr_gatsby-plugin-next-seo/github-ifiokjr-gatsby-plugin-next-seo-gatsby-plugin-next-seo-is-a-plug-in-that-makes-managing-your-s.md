---
title: GitHub - ifiokjr/gatsby-plugin-next-seo: Gatsby Plugin Next SEO is a plug in that makes managing your SEO easier in Gatsby projects.
description: Gatsby Plugin Next SEO is a plug in that makes managing your SEO easier in Gatsby projects. - ifiokjr/gatsby-plugin-next-seo
url: https://github.com/ifiokjr/gatsby-plugin-next-seo
timestamp: 2025-01-20T15:31:37.608Z
domain: github.com
path: ifiokjr_gatsby-plugin-next-seo
---

# GitHub - ifiokjr/gatsby-plugin-next-seo: Gatsby Plugin Next SEO is a plug in that makes managing your SEO easier in Gatsby projects.


Gatsby Plugin Next SEO is a plug in that makes managing your SEO easier in Gatsby projects. - ifiokjr/gatsby-plugin-next-seo


## Content

gatsby-plugin-next-seo
----------------------

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsby-plugin-next-seo)

[![Image 36: GitHub Actions Build Status](https://github.com/ifiokjr/gatsby-plugin-next-seo/workflows/Node%20CI/badge.svg)](https://github.com/ifiokjr/gatsby-plugin-next-seo/actions?query=workflow%3A%22Node+CI%22) [![Image 37: npm](https://camo.githubusercontent.com/091d895a034a3aae6f337fed1c65167013e7beb41730a9a6a7bb589eba85303d/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f646d2f6761747362792d706c7567696e2d6e6578742d73656f2e7376673f266c6f676f3d6e706d)](https://www.npmjs.com/package/gatsby-plugin-next-seo) [![Image 38: All Contributors](https://camo.githubusercontent.com/4723c4f0d7afbcd8646a66fc1dfe893ceea7f399b51c62dc1cbe6509ba07aacb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616c6c5f636f6e7472696275746f72732d322d6f72616e67652e7376673f7374796c653d666c61742d737175617265)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#contributors) [![Image 39: semantic-release](https://camo.githubusercontent.com/251b82ec02847188c7f2f024d0a6752bb8e0422772baaace42e7a7dc3fd8c88a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2532302532302546302539462539332541362546302539462539412538302d73656d616e7469632d2d72656c656173652d6531303037392e737667)](https://github.com/semantic-release/semantic-release)

Gatsby Plugin SEO makes managing SEO easier in your Gatsby JS project. It fully supports server-side rendering (SSR) with site wide configuration available via the `gatsby-config.js` plugin options. SEO options can also be tweaked at any moment by importing the main `GatsbySeo` component and passing in the desired props.

This codebase was initially forked from the brilliant [next-seo](https://github.com/garmeeh/next-seo) project and is now maintained separately.

Table of Contents
-----------------

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#table-of-contents)

*   [gatsby-plugin-next-seo](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsby-plugin-next-seo)
    *   [Table of Contents](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#table-of-contents)
    *   [Usage](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#usage)
        *   [Setup](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#setup)
        *   [Add Plugin to Gatsby Config](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-plugin-to-gatsby-config)
        *   [Add SEO to Page](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-seo-to-page)
            *   [A note on Twitter Tags](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#a-note-on-twitter-tags)
        *   [Default SEO Configuration in Gatsby Config](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#default-seo-configuration-in-gatsby-config)
        *   [GatsbySeo Options](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsbyseo-options)
            *   [Title Template](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#title-template)
            *   [No Index](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-index)
            *   [dangerouslySetAllPagesToNoIndex](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonoindex)
            *   [No Follow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-follow)
            *   [dangerouslySetAllPagesToNoFollow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonofollow)
            *   [Twitter](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#twitter)
            *   [facebook](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#facebook)
            *   [Canonical URL](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#canonical-url)
            *   [Alternate](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#alternate)
            *   [HTML Attributes](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#html-attributes)
            *   [Meta Tags](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#meta-tags)
    *   [Open Graph](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph)
        *   [Open Graph Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples)
            *   [Basic Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#basic-example)
            *   [Video Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#video-example)
            *   [Article Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article-example)
            *   [Book Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book-example)
            *   [Profile Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#profile-example)
    *   [JSON-LD](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#json-ld)
        *   [Override](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#override)
        *   [Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)
        *   [News Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#news-article)
        *   [Blog Post](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog-post)
        *   [Breadcrumb](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#breadcrumb)
        *   [Blog](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog)
        *   [Book](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)
        *   [Speakable](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#speakable)
        *   [FAQ](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq)
            *   [Question Interface](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#question-interface)
        *   [Course](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#course)
        *   [Corporate Contact (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#corporate-contact-deprecated)
        *   [Local Business](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#local-business)
        *   [Logo](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#logo)
        *   [Product](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#product)
        *   [Social Profile (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#social-profile-deprecated)
        *   [JsonLd](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#jsonld)
        *   [Sitelinks Search Box](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#sitelinks-search-box)
    *   [API Docs](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#api-docs)
    *   [FAQ](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq-1)
        *   [Why did you choose `gatsby-plugin-next-seo` as the project name?](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#why-did-you-choose-gatsby-plugin-next-seo-as-the-project-name)
    *   [Contributors](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#contributors)

Usage
-----

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#usage)

`GatsbySeo` can be imported anywhere in your gatsby project. Once included you pass the configuration props with the page's SEO properties. A sitewide / default configuration can also be set via the plugin options in your `gatsby-config.js` file.

### Setup

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#setup)

First, install the plugin and it's peer dependencies:

npm install --save gatsby-plugin-next-seo react-helmet-async

or

yarn add gatsby-plugin-next-seo react-helmet-async

`react-helmet-async` is an required external dependency since it relies on the `React.Context` API which can cause problems when different versions of the same library interact.

### Add Plugin to Gatsby Config

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-plugin-to-gatsby-config)

Add the following configuration to your `gatsby-config.js` file.

module.exports {
  // ...
  plugins: \[
    // ...
    'gatsby-plugin-next-seo'
  \],
}

The plugin allows documented [GatsbySeoPluginOptions](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/src/types.ts#L406) to be set. See an example [below](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#default-seo-configuration-in-gatsby-config).

### Add SEO to Page

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-seo-to-page)

Then you need to import `GatsbySeo` and add the desired properties. This component render the tags in the `<head>` for SEO on a per page basis. As a bare minimum, you should add a title and description.

**Example with just title and description:**

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo
      title\='Simple Usage Example'
      description\='A short description goes here.'
    /\>
    <p\>Simple Usage</p\>
  </\>
);

But `GatsbySeo` gives you many more options that you can add. See below for a typical example for any given gatsby layout.

**Typical page example:**

import React, { FC } from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

const Layout: FC \= ({ children }) \=\> (
  <\>
    <GatsbySeo
      title\='Using More of Config'
      description\='This example uses more of the available config options.'
      canonical\='https://www.canonical.ie/'
      openGraph\={{
        url: 'https://www.url.ie/a',
        title: 'Open Graph Title',
        description: 'Open Graph Description',
        images: \[
          {
            url: 'https://www.example.ie/og-image-01.jpg',
            width: 800,
            height: 600,
            alt: 'Og Image Alt',
          },
          {
            url: 'https://www.example.ie/og-image-02.jpg',
            width: 900,
            height: 800,
            alt: 'Og Image Alt Second',
          },
          { url: 'https://www.example.ie/og-image-03.jpg' },
          { url: 'https://www.example.ie/og-image-04.jpg' },
        \],
        site\_name: 'SiteName',
      }}
      twitter\={{
        handle: '@handle',
        site: '@site',
        cardType: 'summary\_large\_image',
      }}
    /\>
    <div\>{children}</div\>
  </\>
);

export default Layout;

#### A note on Twitter Tags

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#a-note-on-twitter-tags)

Twitter will read the `og:title`, `og:image` and `og:description` tags for their card. `gatsby-plugin-next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` to avoid duplication.

Some tools may report this an error. See [Issue #14](https://github.com/garmeeh/next-seo/issues/14)

### Default SEO Configuration in Gatsby Config

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#default-seo-configuration-in-gatsby-config)

`GatsbySeo` enables you to set the default SEO properties that will appear on all pages without needing to do include anything on them. You can also override these on a page by page basis if needed.

To achieve this, you will need to add the properties to your `gatsby-config.js` file when setting up the plugin.

Here is a typical example:

// gatsby-config.js

module.exports {
  plugins: \[
    {
      resolve: 'gatsby-plugin-next-seo',
      options: {
        openGraph: {
          type: 'website',
          locale: 'en\_IE',
          url: 'https://www.url.ie/',
          site\_name: 'SiteName',
        },
        twitter: {
          handle: '@handle',
          site: '@site',
          cardType: 'summary\_large\_image',
        },
      },
    },
  \],
}

From now on all of your gatsby pages will have the defaults above applied.

### GatsbySeo Options

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsbyseo-options)

| Property | Type | Description |
| --- | --- | --- |
| `titleTemplate` | string | Allows you to set default title template that will be added to your title [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#title-template). |
| `title` | string | Set the meta title of the page. |
| `language` | string | Set the language of the current page. This is added to the html tag and can prevent this [warning](https://web.dev/html-has-lang/). |
| `noindex` | boolean (default false) | Sets whether page should be indexed or not [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-index). |
| `nofollow` | boolean (default false) | Sets whether page should be followed or not [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-follow). |
| `description` | string | Set the page meta description. |
| `canonical` | string | Set the page canonical url. |
| `mobileAlternate.media` | string | Set what screen size the mobile website should be served from. |
| `mobileAlternate.href` | string | Set the mobile page alternate url. |
| `languageAlternates` | array | Set the language of the alternate urls. The shape of the object should be: `{ hrefLang: string, href: string }`. |
| `metaTags` | array | Allows you to add a meta tag that is not documented here. [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#meta-tags). |
| `twitter.cardType` | string | The card type, which will be one of `summary`, `summary_large_image`, `app`, or `player`. |
| `twitter.site` | string | @username for the website used in the card footer. |
| `twitter.handle` | string | @username for the content creator / author (outputs as `twitter:creator`). |
| `facebook.appId` | string | Used for Facebook Insights, you must add a facebook app ID to your page to for it [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#facebook). |
| `openGraph.url` | string | The canonical URL of your object that will be used as its permanent ID in the graph. |
| `openGraph.type` | string | The type of your object. Depending on the type you specify, other properties may also be required [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph) |
| `openGraph.title` | string | The open graph title, this can be different than your meta title. |
| `openGraph.description` | string | The open graph description, this can be different than your meta description. |
| `openGraph.images` | array | An array of images (object) to be used by social media platforms, slack etc as a preview. If multiple supplied you can choose one when sharing. [See Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples) |
| `openGraph.videos` | array | An array of videos (object). |
| `openGraph.locale` | string | The locale the open graph tags are marked up in. Of the format language\_TERRITORY. Default is en\_US. |
| `openGraph.site_name` | string | If your object is part of a larger web site, the name which should be displayed for the overall site. |
| `openGraph.profile.firstName` | string | Person's first name. |
| `openGraph.profile.lastName` | string | Person's last name. |
| `openGraph.profile.username` | string | Person's username. |
| `openGraph.profile.gender` | string | Person's gender. |
| `openGraph.book.authors` | string\[\] | Writers of the article. [See Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples) |
| `openGraph.book.isbn` | string | The [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) |
| `openGraph.book.releaseDate` | datetime | The date the book was released. |
| `openGraph.book.tags` | string\[\] | Tag words associated with this book. |
| `openGraph.article.publishedTime` | datetime | When the article was first published. [See Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples) |
| `openGraph.article.modifiedTime` | datetime | When the article was last changed. |
| `openGraph.article.expirationTime` | datetime | When the article is out of date after. |
| `openGraph.article.authors` | string\[\] | Writers of the article. |
| `openGraph.article.section` | string | A high-level section name. E.g. Technology |
| `openGraph.article.tags` | string\[\] | Tag words associated with this article. |

#### Title Template

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#title-template)

Replaces `%s` with your title string

title \= 'This is my title';
titleTemplate \= 'Gatsby SEO | %s';
// outputs: Gatsby SEO | This is my title

title \= 'This is my title';
titleTemplate \= '%s | Gatsby SEO';
// outputs: This is my title | Gatsby SEO

#### No Index

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-index)

Setting this to `true` will set `noindex,follow` (to set `nofollow`, please refer to [`nofollow`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noFollow)). This works on a page by page basis. This property works in tandem with the `nofollow` property and together they populate the `robots` and `googlebot` meta tags.

**Note:** The `noindex` and the [`nofollow`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noFollow) properties are a little different than all the others in the sense that setting them as a default does not work as expected. This is due to the fact Gatsby SEO already has a default of `index,follow` because `gatsby-plugin-next-seo` is a SEO plugin after all. So if you want to globally these properties, please see [dangerouslySetAllPagesToNoIndex](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).

**Example No Index on a single page:**

If you have a single page that you want no indexed you can achieve this by:

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo noindex\={true} /\>
    <p\>This page is no indexed</p\>
  </\>
);

/\*
<meta name="robots" content="noindex,follow"\>
<meta name="googlebot" content="noindex,follow"\>
\*/

#### dangerouslySetAllPagesToNoIndex

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonoindex)

It has the prefix of `dangerously` because it will `noindex` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this, just please be sure you want to `noindex` **EVERY** page. You can still override this at a page level if you have a use case to `index` a page. This can be done by setting `noindex: false`.

#### No Follow

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-follow)

Setting this to `true` will set `index,nofollow` (to set `noindex`, please refer to [`noindex`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noIndex)). This works on a page by page basis. This property works in tandem with the `noindex` property and together they populate the `robots` and `googlebot` meta tags.

**Note:** The `noindex` and the [`nofollow`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noFollow) properties are a little different than all the others in the sense that setting them as a default does not work as expected. This is due to the fact Gatsby SEO already has a default of `index,follow` because `gatsby-plugin-next-seo` is a SEO plugin after all. So if you want to globally these properties, please see [dangerouslySetAllPagesToNoIndex](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).

**Example No Follow on a single page:**

If you have a single page that you want no indexed you can achieve this by:

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo nofollow\={true} /\>
    <p\>This page is not followed</p\>
  </\>
);

/\*
<meta name="robots" content="index,nofollow"\>
<meta name="googlebot" content="index,nofollow"\>
\*/

#### dangerouslySetAllPagesToNoFollow

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonofollow)

It has the prefix of `dangerously` because it will `nofollow` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this, just please be sure you want to `nofollow` **EVERY** page. You can still override this at a page level if you have a use case to `follow` a page. This can be done by setting `nofollow: false`.

| `noindex` | `nofollow` | `meta` content of `robots`, `googlebot` |
| --- | --- | --- |
| \-- | \-- | `index,follow` (default) |
| false | false | `index,follow` |
| true | \-- | `noindex,follow` |
| true | false | `noindex,follow` |
| \-- | true | `index,nofollow` |
| false | true | `index,nofollow` |
| true | true | `noindex,nofollow` |

#### Twitter

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#twitter)

Twitter will read the `og:title`, `og:image` and `og:description` tags for their card, this is why `gatsby-plugin-next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` so not to duplicate.

Some tools may report this an error. See [Issue #14](https://github.com/garmeeh/gatsby-plugin-next-seo/issues/14)

#### facebook

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#facebook)

facebook\={{
  appId: 1234567890,
}}

Add this to your SEO config to include the fb:app\_id meta if you need to enable Facebook insights for your site. Information regarding this can be found in facebook's [documentation](https://developers.facebook.com/docs/sharing/webmasters/)

#### Canonical URL

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#canonical-url)

Add this on a page per page basis when you want to consolidate duplicate URLs.

canonical \= 'https://www.canonical.ie/';

#### Alternate

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#alternate)

This link relation is used to indicate a relation between a desktop and a mobile website to search engines.

Example:

mobileAlternate\={{
  media: 'only screen and (max-width: 640px)',
  href: 'https://m.canonical.ie',
}}

languageAlternates\={\[
  {
    hrefLang: 'de-AT',
    href: 'https://www.canonical.ie/de',
  },
  {
    hrefLang: 'es',
    href: 'https://www.canonical.ie/es',
}
\]}

#### HTML Attributes

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#html-attributes)

Add html attributes to the html tag with the `htmlAttributes` prop.

Example:

htmlAttributes\={{
  prefix: "og: https://ogp.me/ns#",
}}

#### Meta Tags

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#meta-tags)

This allows you to add any other meta tags that are not covered in the `config`.

`content` is required. Then either `name` or `property`. (Only one on each)

Example:

metaTags\={\[{
  property: 'dc:creator',
  content: 'Jane Doe'
}, {
  name: 'application-name',
  content: 'GatsbySeo'
}\]}

Invalid Examples:

These are invalid as they contain `property` and `name` on the same entry.

metaTags\={\[{
  property: 'dc:creator',
  name: 'dc:creator',
  content: 'Jane Doe'
}, {
  property: 'application-name',
  name: 'application-name',
  content: 'GatsbySeo'
}\]}

Open Graph
----------

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph)

For the full specification please check out [the documentation](http://ogp.me/).

Gatsby SEO currently supports:

*   [basic](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#basic)
*   [video](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#video)
*   [article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)
*   [book](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)
*   [profile](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#profile)

### Open Graph Examples

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples)

#### Basic Example

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#basic-example)

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo
      openGraph\={{
        type: 'website',
        url: 'https://www.example.com/page',
        title: 'Open Graph Title',
        description: 'Open Graph Description',
        images: \[
          {
            url: 'https://www.example.ie/og-image.jpg',
            width: 800,
            height: 600,
            alt: 'Og Image Alt',
          },
          {
            url: 'https://www.example.ie/og-image-2.jpg',
            width: 800,
            height: 600,
            alt: 'Og Image Alt 2',
          },
        \],
      }}
    /\>
    <p\>Basic</p\>
  </\>
);

#### Video Example

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#video-example)

Full info on [http://ogp.me/](http://ogp.me/#type_video)

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo
      title\='Video Page Title'
      description\='Description of video page'
      openGraph\={{
        title: 'Open Graph Video Title',
        description: 'Description of open graph video',
        url: 'https://www.example.com/videos/video-title',
        type: 'video.movie',
        video: {
          // Multiple Open Graph actors is only available in version \`7.0.2-canary.35\`+ of next
          actors: \[
            {
              profile: 'https://www.example.com/actors/@firstnameA-lastnameA',
              role: 'Protagonist',
            },
            {
              profile: 'https://www.example.com/actors/@firstnameB-lastnameB',
              role: 'Antagonist',
            },
          \],
          // Multiple Open Graph directors is only available in version \`7.0.2-canary.35\`+ of next
          directors: \[
            'https://www.example.com/directors/@firstnameA-lastnameA',
            'https://www.example.com/directors/@firstnameB-lastnameB',
          \],
          // Multiple Open Graph writers is only available in version \`7.0.2-canary.35\`+ of next
          writers: \[
            'https://www.example.com/writers/@firstnameA-lastnameA',
            'https://www.example.com/writers/@firstnameB-lastnameB',
          \],
          duration: 680000,
          releaseDate: '2022-12-21T22:04:11Z',
          // Multiple Open Graph tags is only available in version \`7.0.2-canary.35\`+ of next
          tags: \['Tag A', 'Tag B', 'Tag C'\],
        },
        site\_name: 'SiteName',
      }}
    /\>
    <h1\>Video Page SEO</h1\>
  </\>
);

#### Article Example

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article-example)

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo
      openGraph\={{
        title: 'Open Graph Article Title',
        description: 'Description of open graph article',
        url: 'https://www.example.com/articles/article-title',
        type: 'article',
        article: {
          publishedTime: '2017-06-21T23:04:13Z',
          modifiedTime: '2018-01-21T18:04:43Z',
          expirationTime: '2022-12-21T22:04:11Z',
          section: 'Section II',
          authors: \[
            'https://www.example.com/authors/@firstnameA-lastnameA',
            'https://www.example.com/authors/@firstnameB-lastnameB',
          \],
          tags: \['Tag A', 'Tag B', 'Tag C'\],
        },
        images: \[
          {
            url: 'https://www.test.ie/images/cover.jpg',
            width: 850,
            height: 650,
            alt: 'Photo of text',
          },
        \],
      }}
    /\>
    <p\>Article</p\>
  </\>
);

#### Book Example

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book-example)

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo
      openGraph\={{
        title: 'Open Graph Book Title',
        description: 'Description of open graph book',
        url: 'https://www.example.com/books/book-title',
        type: 'book',
        book: {
          releaseDate: '2018-09-17T11:08:13Z',
          isbn: '978-3-16-148410-0',
          authors: \[
            'https://www.example.com/authors/@firstnameA-lastnameA',
            'https://www.example.com/authors/@firstnameB-lastnameB',
          \],
          tags: \['Tag A', 'Tag B', 'Tag C'\],
        },
        images: \[
          {
            url: 'https://www.test.ie/images/book.jpg',
            width: 850,
            height: 650,
            alt: 'Cover of the book',
          },
        \],
      }}
    /\>
    <p\>Book</p\>
  </\>
);

#### Profile Example

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#profile-example)

import React from 'react';
import { GatsbySeo } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <GatsbySeo
      openGraph\={{
        title: 'Open Graph Profile Title',
        description: 'Description of open graph profile',
        url: 'https://www.example.com/@firstlast123',
        type: 'profile',
        profile: {
          firstName: 'First',
          lastName: 'Last',
          username: 'firstlast123',
          gender: 'female',
        },
        images: \[
          {
            url: 'https://www.test.ie/images/profile.jpg',
            width: 850,
            height: 650,
            alt: 'Profile Photo',
          },
        \],
      }}
    /\>
    <p\>Profile</p\>
  </\>
);

JSON-LD
-------

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#json-ld)

Gatsby SEO has the ability to set JSON-LD a form of structured data. Structured data is a standardised format for providing information about a page and classifying the page content.

Google has excellent documentation on JSON-LD -\> [HERE](https://developers.google.com/search/docs/data-types/article)

*   [Override](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#override)
*   [Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)
*   [News Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#news-article)
*   [Blog Post](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog-post)
*   [Breadcrumb](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#breadcrumb)
*   [Blog](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog)
*   [Book](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)
*   [Speakable](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#speakable)
*   [Course](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#course)
*   [FAQ](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq)
*   [Corporate Contact (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#corporate-contact-deprecated)
*   [Local Business](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#local-business)
*   [Logo](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#logo)
*   [Product](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#product)
*   [Social Profile (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#social-profile-deprecated)
*   [JsonLd](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#jsonld)
*   [Sitelinks Search Box](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#sitelinks-search-box)

### Override

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#override)

Each (non-deprecated) JSON LD component provides a set of utility props to help you in the journey of setting up your your site for Search Engine Optimization and voice assistant support. However there are times when you will need more control, and for these situations there is an `overrides` prop available which allows you to manually override the schema type.

The following example would add a `datePublished` property to the JSON LD head script produced.

const OverrideCourseJsonLd \= () \=\> (
  <CourseJsonLd
    name\='Course Name'
    providerName\='Course Provider'
    providerUrl\='https//www.example.com/provider'
    description\='Course description goes right here'
    overrides\={{
      '@type': 'Course',
      datePublished: '2015-02-05T08:00:00+08:00',
    }}
  /\>
);

Currently, when using TypeScript, you must provide an `@type` property to the `overrides` prop. This may change in the future.

### Article

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)

import React from 'react';
import { ArticleJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Article JSON-LD</h1\>
    <ArticleJsonLd
      url\='https://example.com/article'
      headline\='Article headline'
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      datePublished\='2015-02-05T08:00:00+08:00'
      dateModified\='2015-02-05T09:00:00+08:00'
      authorName\='Jane Blogs'
      publisherName\='Ifiok Jr.'
      publisherLogo\='https://www.example.com/photos/logo.jpg'
      description\='This is a mighty good description of this article.'
      overrides\={{
        '@type': 'BlogPosting', // set's this as a blog post.
      }}
    /\>
  </\>
);

### News Article

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#news-article)

This is simply a fancy wrapper around the [`Article`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article) component.

import React from 'react';
import { NewsArticleJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>News Article JSON-LD</h1\>
    <NewsArticleJsonLd
      url\='https://example.com/article'
      title\='Article headline'
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      section\='politic'
      keywords\='prayuth,taksin'
      datePublished\='2015-02-05T08:00:00+08:00'
      dateModified\='2015-02-05T09:00:00+08:00'
      authorName\='Jane Blogs'
      publisherName\='Ifiok Jr.'
      publisherLogo\='https://www.example.com/photos/logo.jpg'
      description\='This is a mighty good description of this article.'
      body\='This is all text for this news article'
    /\>
  </\>
);

### Blog Post

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog-post)

A utility component which wraps the `<ArticleJsonLd />` component but is classified as a `BlogPosting`.

import React from 'react';
import { BlogPostJsonLd } from 'gatsby-plugin-next-seo';
 \*
export default () \=\> (
  <\>
    <h1\>Blog Post JSON-LD</h1\>
    <BlogPostJsonLd
      url\='https://example.com/blog'
      title\='Blog headline'
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      datePublished\='2015-02-05T08:00:00+08:00'
      dateModified\='2015-02-05T09:00:00+08:00'
      authorName\='Jane Blogs'
      description\='This is a mighty good description of this blog.'
    /\>
  </\>
);

### Breadcrumb

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#breadcrumb)

import React from 'react';
import { BreadcrumbJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Breadcrumb JSON-LD</h1\>
    <BreadcrumbJsonLd
      itemListElements\={\[
        {
          position: 1,
          name: 'Books',
          item: 'https://example.com/books',
        },
        {
          position: 2,
          name: 'Authors',
          item: 'https://example.com/books/authors',
        },
        {
          position: 3,
          name: 'Ann Leckie',
          item: 'https://example.com/books/authors/annleckie',
        },
        {
          position: 4,
          name: 'Ancillary Justice',
          item: 'https://example.com/books/authors/ancillaryjustice',
        },
      \]}
    /\>
  </\>
);

**Required properties**

| Property | Info |
| --- | --- |
| `itemListElements` |  |
| `itemListElements.position` | The position of the breadcrumb in the breadcrumb trail. Position 1 signifies the beginning of the trail. |
| `itemListElements.name` | The title of the breadcrumb displayed for the user. |
| `itemListElements.item` | The URL to the webpage that represents the breadcrumb. |

### Blog

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog)

Identifies the page as a blog and outlines the available posts.

import React from 'react';
import { BlogPostJsonLd } from 'gatsby-plugin-next-seo';
 \*
export default () \=\> (
  <\>
    <h1\>Blog with several posts</h1\>
    <BlogJsonLd
      url\='https://example.com/blog'
      headline\='Blog headline'
      images\='https://example.com/photos/1x1/photo.jpg'
      posts\={\[{ headline: 'Post 1', image: 'https://example.com/photos/1x1/photo.jpg' }, { headline: 'Post 2' }\]}
      datePublished\='2015-02-05T08:00:00+08:00'
      dateModified\='2015-02-05T09:00:00+08:00'
      authorName\='Jane Blogs'
      description\='This is a mighty good description of this blog.'
    /\>
  </\>
);

### Book

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)

The `Book` component makes search engines an entry point for discovering your books and authors. Users can then buy the books that they find directly from Search results.

An example feed is shown below.

import React from 'react';
import { CourseJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Book JSON-LD</h1\>
    <BookJsonLd
      author\={{ name: 'Tolu B.' }}
      url\='https://example.com/tolub'
      name\='Rock your world - the final chapter'
      workExample\={\[
        {
          bookFormat: 'AudiobookFormat',
          isbn: '123123123',
          potentialAction: {
            expectsAcceptanceOf: {
              '@type': 'Offer',
              price: '6.99',
              priceCurrency: 'USD',
              eligibleRegion: {
                '@type': 'Country',
                name: 'US',
              },
              availability: 'http://schema.org/InStock',
            },
            target: {
              '@type': 'EntryPoint',
              urlTemplate:
                'http://www.barnesandnoble.com/store/info/offer/0316769487?purchase=true',
              actionPlatform: \[
                'http://schema.org/DesktopWebPlatform',
                'http://schema.org/IOSPlatform',
                'http://schema.org/AndroidPlatform',
              \],
            },
          },
        },
      \]}
    /\>
  </\>
);

### Speakable

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#speakable)

The speakable schema.org property identifies sections within an article or webpage that are best suited for audio playback using text-to-speech (TTS).

Adding markup allows search engines and other applications to identify content to read aloud on voice assistant-enabled devices using TTS. Webpages with speakable structured data can use voice assistants to distribute the content through new channels and reach a wider base of users.

import React from 'react';
import { SpeakableJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Speakable JSON-LD</h1\>
    <SpeakableJsonLd cssSelector\={\['#abc', '#root'\]} /\>
  </\>
);

### FAQ

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq)

A Frequently Asked Question (FAQ) page contains a list of questions and answers pertaining to a particular topic. Properly marked up FAQ pages may be eligible to have a rich result on Search and voice assistants.

import React from 'react';
import { FAQJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <FAQJsonLd
      questions\={\[
        { question: 'What?', answer: 'Stand' },
        { question: 'How?', answer: 'Effort' },
        { question: 'Why?', answer: 'Peace' },
      \]}
    /\>

    <h1\>What?</h1\>
    <p\>Stand</p\>

    <h1\>How?</h1\>
    <p\>Effort</p\>

    <h1\>Why?</h1\>
    <p\>Peace</p\>
  </\>
);

| Property | Type | Description |
| --- | --- | --- |
| [questions](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#question-interface) | `Question[]` | An array of Question elements which comprise the list of answered questions that this FAQPage is about. |

#### Question Interface

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#question-interface)

The questions and answers for an FAQ Page.

| Property | Type | Description |
| --- | --- | --- |
| [answer](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/docs/api/gatsby-plugin-next-seo.question.answer.md) | `string` | The answer to the question. There must be one answer per question. |
| [question](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/docs/api/gatsby-plugin-next-seo.question.question.md) | `string` | The full text of the question. For example, "How long does it take to process a refund?". |

### Course

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#course)

import React from 'react';
import { CourseJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Course JSON-LD</h1\>
    <CourseJsonLd
      courseName\='Course Name'
      providerName\='Course Provider'
      providerUrl\='https//www.example.com/provider'
      description\='Course description goes right here'
    /\>
  </\>
);

### Corporate Contact (Deprecated)

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#corporate-contact-deprecated)

See the [documentation](https://developers.google.com/search/docs/data-types/corporate-contact) with the reason for deprecation.

import React from 'react';
import { CorporateContactJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Corporate Contact JSON-LD</h1\>
    <CorporateContactJsonLd
      url\='http://www.your-company-site.com'
      logo\='http://www.example.com/logo.png'
      contactPoint\={\[
        {
          telephone: '+1-401-555-1212',
          contactType: 'customer service',
          areaServed: 'US',
          availableLanguage: \['English', 'Spanish', 'French'\],
        },
        {
          telephone: '+1-877-746-0909',
          contactType: 'customer service',
          contactOption: 'TollFree',
          availableLanguage: 'English',
        },
        {
          telephone: '+1-877-453-1304',
          contactType: 'technical support',
          contactOption: 'TollFree',
          areaServed: \['US', 'CA'\],
          availableLanguage: \['English', 'French'\],
        },
      \]}
    /\>
  </\>
);

**Required properties**

| Property | Info |
| --- | --- |
| `url` | Url to the home page of the company's official site. |
| `contactPoint` |  |
| `contactPoint.telephone` | An internationalized version of the phone number, starting with the "+" symbol and country code |
| `contactPoint.contactType` | Description of the purpose of the phone number i.e. `Technical Support`. |

**Recommended ContactPoint properties**

| Property | Info |
| --- | --- |
| `contactPoint.areaServed` | `String` or `Array` of geographical regions served by the business. Example `"US"` or `["US", "CA", "MX"]` |
| `contactPoint.availableLanguage` | Details about the language spoken. Example `"English"` or `["English", "French"]` |
| `gecontactPointo.contactOption` | Details about the phone number. Example `"TollFree"` |

### Local Business

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#local-business)

Local business is supported with a sub-set of properties.

<LocalBusinessJsonLd
  type\='Store'
  id\='http://davesdeptstore.example.com'
  name\="Dave's Department Store"
  description\="Dave's latest department store in San Jose, now open"
  url\='http://www.example.com/store-locator/sl/San-Jose-Westgate-Store/1427'
  telephone\='+14088717984'
  address\={{
    streetAddress: '1600 Saratoga Ave',
    addressLocality: 'San Jose',
    addressRegion: 'CA',
    postalCode: '95129',
    addressCountry: 'US',
  }}
  geo\={{
    latitude: '37.293058',
    longitude: '-121.988331',
  }}
  images\={\[
    'https://example.com/photos/1x1/photo.jpg',
    'https://example.com/photos/4x3/photo.jpg',
    'https://example.com/photos/16x9/photo.jpg',
  \]}
/\>

**Required properties**

| Property | Info |
| --- | --- |
| `@id` | Globally unique ID of the specific business location in the form of a URL. |
| `type` | LocalBusiness or any sub-type |
| `address` | Address of the specific business location |
| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |
| `address.addressLocality` | City |
| `address.addressRegion` | State or province, if applicable. |
| `address.postalCode` | Postal or zip code. |
| `address.streetAddress` | Street number, street name, and unit number. |
| `name` | Business name. |

**Supported properties**

| Property | Info |
| --- | --- |
| `description` | Description of the business location |
| `geo` | Geographic coordinates of the business. |
| `geo.latitude` | The latitude of the business location |
| `geo.longitude` | The longitude of the business location |
| `images` | An image or images of the business. Required for valid markup depending on the type |
| `telephone` | A business phone number meant to be the primary contact method for customers. |
| `url` | The fully-qualified URL of the specific business location. |

**NOTE:**

Images are required for most of the types that you can use for `LocalBusiness`, if in doubt you should add an image. You can check your generated JSON over at Google's [Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool)

### Logo

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#logo)

import React from 'react';
import { LogoJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Logo JSON-LD</h1\>
    <LogoJsonLd
      logo\='http://www.your-site.com/images/logo.jpg'
      url\='http://www.your-site.com'
    /\>
  </\>
);

| Property | Info |
| --- | --- |
| `url` | The URL of the website associated with the logo. [Logo guidelines](https://developers.google.com/search/docs/data-types/logo#definitions) |
| `logo` | URL of a logo that is representative of the organization. |

### Product

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#product)

import React from 'react';
import { ProductJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Product JSON-LD</h1\>
    <ProductJsonLd
      productName\='Executive Anvil'
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      description\="Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height."
      brand\='ACME'
      reviews\={\[
        {
          author: 'Jim',
          datePublished: '2017-01-06T03:37:40Z',
          reviewBody:
            'This is my favorite product yet! Thanks Nate for the example products and reviews.',
          name: 'So awesome!!!',
          reviewRating: {
            bestRating: '5',
            ratingValue: '5',
            worstRating: '1',
          },
        },
      \]}
      aggregateRating\={{
        ratingValue: '4.4',
        reviewCount: '89',
      }}
      offers\={{
        price: '119.99',
        priceCurrency: 'USD',
        priceValidUntil: '2020-11-05',
        itemCondition: 'http://schema.org/UsedCondition',
        availability: 'http://schema.org/InStock',
        url: 'https://www.example.com/executive-anvil',
        seller: {
          name: 'Executive Objects',
        },
      }}
      mpn\='925872'
    /\>
  </\>
);

Also available: `sku`, `gtin8`, `gtin13`, `gtin14`.

Valid values for `offers.itemCondition`:

*   [https://schema.org/DamagedCondition](https://schema.org/DamagedCondition)
*   [https://schema.org/NewCondition](https://schema.org/NewCondition)
*   [https://schema.org/RefurbishedCondition](https://schema.org/RefurbishedCondition)
*   [https://schema.org/UsedCondition](https://schema.org/UsedCondition)

Valid values fro `offers.availability`:

*   [https://schema.org/Discontinued](https://schema.org/Discontinued)
*   [https://schema.org/InStock](https://schema.org/InStock)
*   [https://schema.org/InStoreOnly](https://schema.org/InStoreOnly)
*   [https://schema.org/LimitedAvailability](https://schema.org/LimitedAvailability)
*   [https://schema.org/OnlineOnly](https://schema.org/OnlineOnly)
*   [https://schema.org/OutOfStock](https://schema.org/OutOfStock)
*   [https://schema.org/PreOrder](https://schema.org/PreOrder)
*   [https://schema.org/PreSale](https://schema.org/PreSale)
*   [https://schema.org/SoldOut](https://schema.org/SoldOut)

More info on the product data type can be found [here](https://developers.google.com/search/docs/data-types/product).

### Social Profile (Deprecated)

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#social-profile-deprecated)

See the [documentation](https://developers.google.com/search/docs/data-types/social-profile) with the reason for deprecation.

import React from 'react';
import { SocialProfileJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Social Profile JSON-LD</h1\>
    <SocialProfileJsonLd
      type\='Person'
      name\='your name'
      url\='http://www.your-site.com'
      sameAs\={\[
        'http://www.facebook.com/your-profile',
        'http://instagram.com/yourProfile',
        'http://www.linkedin.com/in/yourprofile',
        'http://plus.google.com/your\_profile',
      \]}
    /\>
  </\>
);

**Required properties**

| Property | Info |
| --- | --- |
| `type` | Person or Organization |
| `name` | The name of the person or organization |
| `url` | The URL for the person's or organization's official website. |
| `sameAs` | An array of URLs for the person's or organization's official social media profile page(s) |

**Google Supported Social Profiles**

*   Facebook
*   Twitter
*   Google+
*   Instagram
*   YouTube
*   LinkedIn
*   Myspace
*   Pinterest
*   SoundCloud
*   Tumblr

### JsonLd

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#jsonld)

This is the base JSON component that allows you to create your own JSON LD components according to the spec.

[Google Docs for Social Profile](https://developers.google.com/search/docs/data-types/social-profile)

### Sitelinks Search Box

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#sitelinks-search-box)

The `SitelinksSearchBoxJsonLd` component can be used to add JSON-LD structured data to your website for a Sitelinks search box.

See [here](https://developers.google.com/search/docs/advanced/structured-data/sitelinks-searchbox) for further documentation.

import React from 'react';
import { SitelinksSearchBoxJsonLd } from 'gatsby-plugin-next-seo';

export default () \=\> (
  <\>
    <h1\>Sitelinks Search Box JSON-LD</h1\>
    <SitelinksSearchBoxJsonLd
      url\='https://example.com/'
      searchHandlerQueryStringUrl\='https://example.com/?q='
    /\>
  </\>
);

**Required properties**

| Property | Info |
| --- | --- |
| `url` | The URL of the canonical homepage of the website associated with the Sitelinks search box. |
| `searchHandlerQueryStringUrl` | Define the website's search engine query string as a URL. |
|  |  |

API Docs
--------

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#api-docs)

You can explore the [**api documentation here**](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/docs/api/gatsby-plugin-next-seo.md).

FAQ
---

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq-1)

### Why did you choose `gatsby-plugin-next-seo` as the project name?

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#why-did-you-choose-gatsby-plugin-next-seo-as-the-project-name)

Unfortunately the better options [gatsby-seo](https://github.com/sidharthachatterjee/gatsby-seo#readme) and [gatsby-plugin-seo](https://github.com/franklintarter/gatsby-plugin-seo/tree/master/gatsby-plugin-seo) were already taken. As a result I've used gatsby-plugin-**next-seo** as a shout out to the original **next-seo** project from which this codebase has been forked.

Contributors
------------

[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#contributors)

Thanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!

## Metadata

```json
{
  "title": "GitHub - ifiokjr/gatsby-plugin-next-seo: Gatsby Plugin Next SEO is a plug in that makes managing your SEO easier in Gatsby projects.",
  "description": "Gatsby Plugin Next SEO is a plug in that makes managing your SEO easier in Gatsby projects. - ifiokjr/gatsby-plugin-next-seo",
  "url": "https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true",
  "content": "gatsby-plugin-next-seo\n----------------------\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsby-plugin-next-seo)\n\n[![Image 36: GitHub Actions Build Status](https://github.com/ifiokjr/gatsby-plugin-next-seo/workflows/Node%20CI/badge.svg)](https://github.com/ifiokjr/gatsby-plugin-next-seo/actions?query=workflow%3A%22Node+CI%22) [![Image 37: npm](https://camo.githubusercontent.com/091d895a034a3aae6f337fed1c65167013e7beb41730a9a6a7bb589eba85303d/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f646d2f6761747362792d706c7567696e2d6e6578742d73656f2e7376673f266c6f676f3d6e706d)](https://www.npmjs.com/package/gatsby-plugin-next-seo) [![Image 38: All Contributors](https://camo.githubusercontent.com/4723c4f0d7afbcd8646a66fc1dfe893ceea7f399b51c62dc1cbe6509ba07aacb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616c6c5f636f6e7472696275746f72732d322d6f72616e67652e7376673f7374796c653d666c61742d737175617265)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#contributors) [![Image 39: semantic-release](https://camo.githubusercontent.com/251b82ec02847188c7f2f024d0a6752bb8e0422772baaace42e7a7dc3fd8c88a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2532302532302546302539462539332541362546302539462539412538302d73656d616e7469632d2d72656c656173652d6531303037392e737667)](https://github.com/semantic-release/semantic-release)\n\nGatsby Plugin SEO makes managing SEO easier in your Gatsby JS project. It fully supports server-side rendering (SSR) with site wide configuration available via the `gatsby-config.js` plugin options. SEO options can also be tweaked at any moment by importing the main `GatsbySeo` component and passing in the desired props.\n\nThis codebase was initially forked from the brilliant [next-seo](https://github.com/garmeeh/next-seo) project and is now maintained separately.\n\nTable of Contents\n-----------------\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#table-of-contents)\n\n*   [gatsby-plugin-next-seo](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsby-plugin-next-seo)\n    *   [Table of Contents](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#table-of-contents)\n    *   [Usage](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#usage)\n        *   [Setup](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#setup)\n        *   [Add Plugin to Gatsby Config](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-plugin-to-gatsby-config)\n        *   [Add SEO to Page](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-seo-to-page)\n            *   [A note on Twitter Tags](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#a-note-on-twitter-tags)\n        *   [Default SEO Configuration in Gatsby Config](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#default-seo-configuration-in-gatsby-config)\n        *   [GatsbySeo Options](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsbyseo-options)\n            *   [Title Template](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#title-template)\n            *   [No Index](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-index)\n            *   [dangerouslySetAllPagesToNoIndex](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonoindex)\n            *   [No Follow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-follow)\n            *   [dangerouslySetAllPagesToNoFollow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonofollow)\n            *   [Twitter](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#twitter)\n            *   [facebook](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#facebook)\n            *   [Canonical URL](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#canonical-url)\n            *   [Alternate](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#alternate)\n            *   [HTML Attributes](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#html-attributes)\n            *   [Meta Tags](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#meta-tags)\n    *   [Open Graph](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph)\n        *   [Open Graph Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples)\n            *   [Basic Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#basic-example)\n            *   [Video Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#video-example)\n            *   [Article Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article-example)\n            *   [Book Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book-example)\n            *   [Profile Example](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#profile-example)\n    *   [JSON-LD](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#json-ld)\n        *   [Override](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#override)\n        *   [Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)\n        *   [News Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#news-article)\n        *   [Blog Post](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog-post)\n        *   [Breadcrumb](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#breadcrumb)\n        *   [Blog](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog)\n        *   [Book](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)\n        *   [Speakable](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#speakable)\n        *   [FAQ](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq)\n            *   [Question Interface](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#question-interface)\n        *   [Course](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#course)\n        *   [Corporate Contact (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#corporate-contact-deprecated)\n        *   [Local Business](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#local-business)\n        *   [Logo](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#logo)\n        *   [Product](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#product)\n        *   [Social Profile (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#social-profile-deprecated)\n        *   [JsonLd](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#jsonld)\n        *   [Sitelinks Search Box](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#sitelinks-search-box)\n    *   [API Docs](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#api-docs)\n    *   [FAQ](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq-1)\n        *   [Why did you choose `gatsby-plugin-next-seo` as the project name?](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#why-did-you-choose-gatsby-plugin-next-seo-as-the-project-name)\n    *   [Contributors](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#contributors)\n\nUsage\n-----\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#usage)\n\n`GatsbySeo` can be imported anywhere in your gatsby project. Once included you pass the configuration props with the page's SEO properties. A sitewide / default configuration can also be set via the plugin options in your `gatsby-config.js` file.\n\n### Setup\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#setup)\n\nFirst, install the plugin and it's peer dependencies:\n\nnpm install --save gatsby-plugin-next-seo react-helmet-async\n\nor\n\nyarn add gatsby-plugin-next-seo react-helmet-async\n\n`react-helmet-async` is an required external dependency since it relies on the `React.Context` API which can cause problems when different versions of the same library interact.\n\n### Add Plugin to Gatsby Config\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-plugin-to-gatsby-config)\n\nAdd the following configuration to your `gatsby-config.js` file.\n\nmodule.exports {\n  // ...\n  plugins: \\[\n    // ...\n    'gatsby-plugin-next-seo'\n  \\],\n}\n\nThe plugin allows documented [GatsbySeoPluginOptions](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/src/types.ts#L406) to be set. See an example [below](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#default-seo-configuration-in-gatsby-config).\n\n### Add SEO to Page\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#add-seo-to-page)\n\nThen you need to import `GatsbySeo` and add the desired properties. This component render the tags in the `<head>` for SEO on a per page basis. As a bare minimum, you should add a title and description.\n\n**Example with just title and description:**\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo\n      title\\='Simple Usage Example'\n      description\\='A short description goes here.'\n    /\\>\n    <p\\>Simple Usage</p\\>\n  </\\>\n);\n\nBut `GatsbySeo` gives you many more options that you can add. See below for a typical example for any given gatsby layout.\n\n**Typical page example:**\n\nimport React, { FC } from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nconst Layout: FC \\= ({ children }) \\=\\> (\n  <\\>\n    <GatsbySeo\n      title\\='Using More of Config'\n      description\\='This example uses more of the available config options.'\n      canonical\\='https://www.canonical.ie/'\n      openGraph\\={{\n        url: 'https://www.url.ie/a',\n        title: 'Open Graph Title',\n        description: 'Open Graph Description',\n        images: \\[\n          {\n            url: 'https://www.example.ie/og-image-01.jpg',\n            width: 800,\n            height: 600,\n            alt: 'Og Image Alt',\n          },\n          {\n            url: 'https://www.example.ie/og-image-02.jpg',\n            width: 900,\n            height: 800,\n            alt: 'Og Image Alt Second',\n          },\n          { url: 'https://www.example.ie/og-image-03.jpg' },\n          { url: 'https://www.example.ie/og-image-04.jpg' },\n        \\],\n        site\\_name: 'SiteName',\n      }}\n      twitter\\={{\n        handle: '@handle',\n        site: '@site',\n        cardType: 'summary\\_large\\_image',\n      }}\n    /\\>\n    <div\\>{children}</div\\>\n  </\\>\n);\n\nexport default Layout;\n\n#### A note on Twitter Tags\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#a-note-on-twitter-tags)\n\nTwitter will read the `og:title`, `og:image` and `og:description` tags for their card. `gatsby-plugin-next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` to avoid duplication.\n\nSome tools may report this an error. See [Issue #14](https://github.com/garmeeh/next-seo/issues/14)\n\n### Default SEO Configuration in Gatsby Config\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#default-seo-configuration-in-gatsby-config)\n\n`GatsbySeo` enables you to set the default SEO properties that will appear on all pages without needing to do include anything on them. You can also override these on a page by page basis if needed.\n\nTo achieve this, you will need to add the properties to your `gatsby-config.js` file when setting up the plugin.\n\nHere is a typical example:\n\n// gatsby-config.js\n\nmodule.exports {\n  plugins: \\[\n    {\n      resolve: 'gatsby-plugin-next-seo',\n      options: {\n        openGraph: {\n          type: 'website',\n          locale: 'en\\_IE',\n          url: 'https://www.url.ie/',\n          site\\_name: 'SiteName',\n        },\n        twitter: {\n          handle: '@handle',\n          site: '@site',\n          cardType: 'summary\\_large\\_image',\n        },\n      },\n    },\n  \\],\n}\n\nFrom now on all of your gatsby pages will have the defaults above applied.\n\n### GatsbySeo Options\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#gatsbyseo-options)\n\n| Property | Type | Description |\n| --- | --- | --- |\n| `titleTemplate` | string | Allows you to set default title template that will be added to your title [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#title-template). |\n| `title` | string | Set the meta title of the page. |\n| `language` | string | Set the language of the current page. This is added to the html tag and can prevent this [warning](https://web.dev/html-has-lang/). |\n| `noindex` | boolean (default false) | Sets whether page should be indexed or not [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-index). |\n| `nofollow` | boolean (default false) | Sets whether page should be followed or not [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-follow). |\n| `description` | string | Set the page meta description. |\n| `canonical` | string | Set the page canonical url. |\n| `mobileAlternate.media` | string | Set what screen size the mobile website should be served from. |\n| `mobileAlternate.href` | string | Set the mobile page alternate url. |\n| `languageAlternates` | array | Set the language of the alternate urls. The shape of the object should be: `{ hrefLang: string, href: string }`. |\n| `metaTags` | array | Allows you to add a meta tag that is not documented here. [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#meta-tags). |\n| `twitter.cardType` | string | The card type, which will be one of `summary`, `summary_large_image`, `app`, or `player`. |\n| `twitter.site` | string | @username for the website used in the card footer. |\n| `twitter.handle` | string | @username for the content creator / author (outputs as `twitter:creator`). |\n| `facebook.appId` | string | Used for Facebook Insights, you must add a facebook app ID to your page to for it [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#facebook). |\n| `openGraph.url` | string | The canonical URL of your object that will be used as its permanent ID in the graph. |\n| `openGraph.type` | string | The type of your object. Depending on the type you specify, other properties may also be required [More Info](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph) |\n| `openGraph.title` | string | The open graph title, this can be different than your meta title. |\n| `openGraph.description` | string | The open graph description, this can be different than your meta description. |\n| `openGraph.images` | array | An array of images (object) to be used by social media platforms, slack etc as a preview. If multiple supplied you can choose one when sharing. [See Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples) |\n| `openGraph.videos` | array | An array of videos (object). |\n| `openGraph.locale` | string | The locale the open graph tags are marked up in. Of the format language\\_TERRITORY. Default is en\\_US. |\n| `openGraph.site_name` | string | If your object is part of a larger web site, the name which should be displayed for the overall site. |\n| `openGraph.profile.firstName` | string | Person's first name. |\n| `openGraph.profile.lastName` | string | Person's last name. |\n| `openGraph.profile.username` | string | Person's username. |\n| `openGraph.profile.gender` | string | Person's gender. |\n| `openGraph.book.authors` | string\\[\\] | Writers of the article. [See Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples) |\n| `openGraph.book.isbn` | string | The [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) |\n| `openGraph.book.releaseDate` | datetime | The date the book was released. |\n| `openGraph.book.tags` | string\\[\\] | Tag words associated with this book. |\n| `openGraph.article.publishedTime` | datetime | When the article was first published. [See Examples](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples) |\n| `openGraph.article.modifiedTime` | datetime | When the article was last changed. |\n| `openGraph.article.expirationTime` | datetime | When the article is out of date after. |\n| `openGraph.article.authors` | string\\[\\] | Writers of the article. |\n| `openGraph.article.section` | string | A high-level section name. E.g. Technology |\n| `openGraph.article.tags` | string\\[\\] | Tag words associated with this article. |\n\n#### Title Template\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#title-template)\n\nReplaces `%s` with your title string\n\ntitle \\= 'This is my title';\ntitleTemplate \\= 'Gatsby SEO | %s';\n// outputs: Gatsby SEO | This is my title\n\ntitle \\= 'This is my title';\ntitleTemplate \\= '%s | Gatsby SEO';\n// outputs: This is my title | Gatsby SEO\n\n#### No Index\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-index)\n\nSetting this to `true` will set `noindex,follow` (to set `nofollow`, please refer to [`nofollow`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noFollow)). This works on a page by page basis. This property works in tandem with the `nofollow` property and together they populate the `robots` and `googlebot` meta tags.\n\n**Note:** The `noindex` and the [`nofollow`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noFollow) properties are a little different than all the others in the sense that setting them as a default does not work as expected. This is due to the fact Gatsby SEO already has a default of `index,follow` because `gatsby-plugin-next-seo` is a SEO plugin after all. So if you want to globally these properties, please see [dangerouslySetAllPagesToNoIndex](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).\n\n**Example No Index on a single page:**\n\nIf you have a single page that you want no indexed you can achieve this by:\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo noindex\\={true} /\\>\n    <p\\>This page is no indexed</p\\>\n  </\\>\n);\n\n/\\*\n<meta name=\"robots\" content=\"noindex,follow\"\\>\n<meta name=\"googlebot\" content=\"noindex,follow\"\\>\n\\*/\n\n#### dangerouslySetAllPagesToNoIndex\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonoindex)\n\nIt has the prefix of `dangerously` because it will `noindex` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this, just please be sure you want to `noindex` **EVERY** page. You can still override this at a page level if you have a use case to `index` a page. This can be done by setting `noindex: false`.\n\n#### No Follow\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#no-follow)\n\nSetting this to `true` will set `index,nofollow` (to set `noindex`, please refer to [`noindex`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noIndex)). This works on a page by page basis. This property works in tandem with the `noindex` property and together they populate the `robots` and `googlebot` meta tags.\n\n**Note:** The `noindex` and the [`nofollow`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#noFollow) properties are a little different than all the others in the sense that setting them as a default does not work as expected. This is due to the fact Gatsby SEO already has a default of `index,follow` because `gatsby-plugin-next-seo` is a SEO plugin after all. So if you want to globally these properties, please see [dangerouslySetAllPagesToNoIndex](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).\n\n**Example No Follow on a single page:**\n\nIf you have a single page that you want no indexed you can achieve this by:\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo nofollow\\={true} /\\>\n    <p\\>This page is not followed</p\\>\n  </\\>\n);\n\n/\\*\n<meta name=\"robots\" content=\"index,nofollow\"\\>\n<meta name=\"googlebot\" content=\"index,nofollow\"\\>\n\\*/\n\n#### dangerouslySetAllPagesToNoFollow\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#dangerouslysetallpagestonofollow)\n\nIt has the prefix of `dangerously` because it will `nofollow` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this, just please be sure you want to `nofollow` **EVERY** page. You can still override this at a page level if you have a use case to `follow` a page. This can be done by setting `nofollow: false`.\n\n| `noindex` | `nofollow` | `meta` content of `robots`, `googlebot` |\n| --- | --- | --- |\n| \\-- | \\-- | `index,follow` (default) |\n| false | false | `index,follow` |\n| true | \\-- | `noindex,follow` |\n| true | false | `noindex,follow` |\n| \\-- | true | `index,nofollow` |\n| false | true | `index,nofollow` |\n| true | true | `noindex,nofollow` |\n\n#### Twitter\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#twitter)\n\nTwitter will read the `og:title`, `og:image` and `og:description` tags for their card, this is why `gatsby-plugin-next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` so not to duplicate.\n\nSome tools may report this an error. See [Issue #14](https://github.com/garmeeh/gatsby-plugin-next-seo/issues/14)\n\n#### facebook\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#facebook)\n\nfacebook\\={{\n  appId: 1234567890,\n}}\n\nAdd this to your SEO config to include the fb:app\\_id meta if you need to enable Facebook insights for your site. Information regarding this can be found in facebook's [documentation](https://developers.facebook.com/docs/sharing/webmasters/)\n\n#### Canonical URL\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#canonical-url)\n\nAdd this on a page per page basis when you want to consolidate duplicate URLs.\n\ncanonical \\= 'https://www.canonical.ie/';\n\n#### Alternate\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#alternate)\n\nThis link relation is used to indicate a relation between a desktop and a mobile website to search engines.\n\nExample:\n\nmobileAlternate\\={{\n  media: 'only screen and (max-width: 640px)',\n  href: 'https://m.canonical.ie',\n}}\n\nlanguageAlternates\\={\\[\n  {\n    hrefLang: 'de-AT',\n    href: 'https://www.canonical.ie/de',\n  },\n  {\n    hrefLang: 'es',\n    href: 'https://www.canonical.ie/es',\n}\n\\]}\n\n#### HTML Attributes\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#html-attributes)\n\nAdd html attributes to the html tag with the `htmlAttributes` prop.\n\nExample:\n\nhtmlAttributes\\={{\n  prefix: \"og: https://ogp.me/ns#\",\n}}\n\n#### Meta Tags\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#meta-tags)\n\nThis allows you to add any other meta tags that are not covered in the `config`.\n\n`content` is required. Then either `name` or `property`. (Only one on each)\n\nExample:\n\nmetaTags\\={\\[{\n  property: 'dc:creator',\n  content: 'Jane Doe'\n}, {\n  name: 'application-name',\n  content: 'GatsbySeo'\n}\\]}\n\nInvalid Examples:\n\nThese are invalid as they contain `property` and `name` on the same entry.\n\nmetaTags\\={\\[{\n  property: 'dc:creator',\n  name: 'dc:creator',\n  content: 'Jane Doe'\n}, {\n  property: 'application-name',\n  name: 'application-name',\n  content: 'GatsbySeo'\n}\\]}\n\nOpen Graph\n----------\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph)\n\nFor the full specification please check out [the documentation](http://ogp.me/).\n\nGatsby SEO currently supports:\n\n*   [basic](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#basic)\n*   [video](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#video)\n*   [article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)\n*   [book](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)\n*   [profile](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#profile)\n\n### Open Graph Examples\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#open-graph-examples)\n\n#### Basic Example\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#basic-example)\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo\n      openGraph\\={{\n        type: 'website',\n        url: 'https://www.example.com/page',\n        title: 'Open Graph Title',\n        description: 'Open Graph Description',\n        images: \\[\n          {\n            url: 'https://www.example.ie/og-image.jpg',\n            width: 800,\n            height: 600,\n            alt: 'Og Image Alt',\n          },\n          {\n            url: 'https://www.example.ie/og-image-2.jpg',\n            width: 800,\n            height: 600,\n            alt: 'Og Image Alt 2',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Basic</p\\>\n  </\\>\n);\n\n#### Video Example\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#video-example)\n\nFull info on [http://ogp.me/](http://ogp.me/#type_video)\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo\n      title\\='Video Page Title'\n      description\\='Description of video page'\n      openGraph\\={{\n        title: 'Open Graph Video Title',\n        description: 'Description of open graph video',\n        url: 'https://www.example.com/videos/video-title',\n        type: 'video.movie',\n        video: {\n          // Multiple Open Graph actors is only available in version \\`7.0.2-canary.35\\`+ of next\n          actors: \\[\n            {\n              profile: 'https://www.example.com/actors/@firstnameA-lastnameA',\n              role: 'Protagonist',\n            },\n            {\n              profile: 'https://www.example.com/actors/@firstnameB-lastnameB',\n              role: 'Antagonist',\n            },\n          \\],\n          // Multiple Open Graph directors is only available in version \\`7.0.2-canary.35\\`+ of next\n          directors: \\[\n            'https://www.example.com/directors/@firstnameA-lastnameA',\n            'https://www.example.com/directors/@firstnameB-lastnameB',\n          \\],\n          // Multiple Open Graph writers is only available in version \\`7.0.2-canary.35\\`+ of next\n          writers: \\[\n            'https://www.example.com/writers/@firstnameA-lastnameA',\n            'https://www.example.com/writers/@firstnameB-lastnameB',\n          \\],\n          duration: 680000,\n          releaseDate: '2022-12-21T22:04:11Z',\n          // Multiple Open Graph tags is only available in version \\`7.0.2-canary.35\\`+ of next\n          tags: \\['Tag A', 'Tag B', 'Tag C'\\],\n        },\n        site\\_name: 'SiteName',\n      }}\n    /\\>\n    <h1\\>Video Page SEO</h1\\>\n  </\\>\n);\n\n#### Article Example\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article-example)\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo\n      openGraph\\={{\n        title: 'Open Graph Article Title',\n        description: 'Description of open graph article',\n        url: 'https://www.example.com/articles/article-title',\n        type: 'article',\n        article: {\n          publishedTime: '2017-06-21T23:04:13Z',\n          modifiedTime: '2018-01-21T18:04:43Z',\n          expirationTime: '2022-12-21T22:04:11Z',\n          section: 'Section II',\n          authors: \\[\n            'https://www.example.com/authors/@firstnameA-lastnameA',\n            'https://www.example.com/authors/@firstnameB-lastnameB',\n          \\],\n          tags: \\['Tag A', 'Tag B', 'Tag C'\\],\n        },\n        images: \\[\n          {\n            url: 'https://www.test.ie/images/cover.jpg',\n            width: 850,\n            height: 650,\n            alt: 'Photo of text',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Article</p\\>\n  </\\>\n);\n\n#### Book Example\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book-example)\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo\n      openGraph\\={{\n        title: 'Open Graph Book Title',\n        description: 'Description of open graph book',\n        url: 'https://www.example.com/books/book-title',\n        type: 'book',\n        book: {\n          releaseDate: '2018-09-17T11:08:13Z',\n          isbn: '978-3-16-148410-0',\n          authors: \\[\n            'https://www.example.com/authors/@firstnameA-lastnameA',\n            'https://www.example.com/authors/@firstnameB-lastnameB',\n          \\],\n          tags: \\['Tag A', 'Tag B', 'Tag C'\\],\n        },\n        images: \\[\n          {\n            url: 'https://www.test.ie/images/book.jpg',\n            width: 850,\n            height: 650,\n            alt: 'Cover of the book',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Book</p\\>\n  </\\>\n);\n\n#### Profile Example\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#profile-example)\n\nimport React from 'react';\nimport { GatsbySeo } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <GatsbySeo\n      openGraph\\={{\n        title: 'Open Graph Profile Title',\n        description: 'Description of open graph profile',\n        url: 'https://www.example.com/@firstlast123',\n        type: 'profile',\n        profile: {\n          firstName: 'First',\n          lastName: 'Last',\n          username: 'firstlast123',\n          gender: 'female',\n        },\n        images: \\[\n          {\n            url: 'https://www.test.ie/images/profile.jpg',\n            width: 850,\n            height: 650,\n            alt: 'Profile Photo',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Profile</p\\>\n  </\\>\n);\n\nJSON-LD\n-------\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#json-ld)\n\nGatsby SEO has the ability to set JSON-LD a form of structured data. Structured data is a standardised format for providing information about a page and classifying the page content.\n\nGoogle has excellent documentation on JSON-LD -\\> [HERE](https://developers.google.com/search/docs/data-types/article)\n\n*   [Override](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#override)\n*   [Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)\n*   [News Article](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#news-article)\n*   [Blog Post](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog-post)\n*   [Breadcrumb](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#breadcrumb)\n*   [Blog](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog)\n*   [Book](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)\n*   [Speakable](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#speakable)\n*   [Course](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#course)\n*   [FAQ](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq)\n*   [Corporate Contact (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#corporate-contact-deprecated)\n*   [Local Business](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#local-business)\n*   [Logo](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#logo)\n*   [Product](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#product)\n*   [Social Profile (Deprecated)](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#social-profile-deprecated)\n*   [JsonLd](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#jsonld)\n*   [Sitelinks Search Box](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#sitelinks-search-box)\n\n### Override\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#override)\n\nEach (non-deprecated) JSON LD component provides a set of utility props to help you in the journey of setting up your your site for Search Engine Optimization and voice assistant support. However there are times when you will need more control, and for these situations there is an `overrides` prop available which allows you to manually override the schema type.\n\nThe following example would add a `datePublished` property to the JSON LD head script produced.\n\nconst OverrideCourseJsonLd \\= () \\=\\> (\n  <CourseJsonLd\n    name\\='Course Name'\n    providerName\\='Course Provider'\n    providerUrl\\='https//www.example.com/provider'\n    description\\='Course description goes right here'\n    overrides\\={{\n      '@type': 'Course',\n      datePublished: '2015-02-05T08:00:00+08:00',\n    }}\n  /\\>\n);\n\nCurrently, when using TypeScript, you must provide an `@type` property to the `overrides` prop. This may change in the future.\n\n### Article\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article)\n\nimport React from 'react';\nimport { ArticleJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Article JSON-LD</h1\\>\n    <ArticleJsonLd\n      url\\='https://example.com/article'\n      headline\\='Article headline'\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      datePublished\\='2015-02-05T08:00:00+08:00'\n      dateModified\\='2015-02-05T09:00:00+08:00'\n      authorName\\='Jane Blogs'\n      publisherName\\='Ifiok Jr.'\n      publisherLogo\\='https://www.example.com/photos/logo.jpg'\n      description\\='This is a mighty good description of this article.'\n      overrides\\={{\n        '@type': 'BlogPosting', // set's this as a blog post.\n      }}\n    /\\>\n  </\\>\n);\n\n### News Article\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#news-article)\n\nThis is simply a fancy wrapper around the [`Article`](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#article) component.\n\nimport React from 'react';\nimport { NewsArticleJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>News Article JSON-LD</h1\\>\n    <NewsArticleJsonLd\n      url\\='https://example.com/article'\n      title\\='Article headline'\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      section\\='politic'\n      keywords\\='prayuth,taksin'\n      datePublished\\='2015-02-05T08:00:00+08:00'\n      dateModified\\='2015-02-05T09:00:00+08:00'\n      authorName\\='Jane Blogs'\n      publisherName\\='Ifiok Jr.'\n      publisherLogo\\='https://www.example.com/photos/logo.jpg'\n      description\\='This is a mighty good description of this article.'\n      body\\='This is all text for this news article'\n    /\\>\n  </\\>\n);\n\n### Blog Post\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog-post)\n\nA utility component which wraps the `<ArticleJsonLd />` component but is classified as a `BlogPosting`.\n\nimport React from 'react';\nimport { BlogPostJsonLd } from 'gatsby-plugin-next-seo';\n \\*\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Blog Post JSON-LD</h1\\>\n    <BlogPostJsonLd\n      url\\='https://example.com/blog'\n      title\\='Blog headline'\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      datePublished\\='2015-02-05T08:00:00+08:00'\n      dateModified\\='2015-02-05T09:00:00+08:00'\n      authorName\\='Jane Blogs'\n      description\\='This is a mighty good description of this blog.'\n    /\\>\n  </\\>\n);\n\n### Breadcrumb\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#breadcrumb)\n\nimport React from 'react';\nimport { BreadcrumbJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Breadcrumb JSON-LD</h1\\>\n    <BreadcrumbJsonLd\n      itemListElements\\={\\[\n        {\n          position: 1,\n          name: 'Books',\n          item: 'https://example.com/books',\n        },\n        {\n          position: 2,\n          name: 'Authors',\n          item: 'https://example.com/books/authors',\n        },\n        {\n          position: 3,\n          name: 'Ann Leckie',\n          item: 'https://example.com/books/authors/annleckie',\n        },\n        {\n          position: 4,\n          name: 'Ancillary Justice',\n          item: 'https://example.com/books/authors/ancillaryjustice',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `itemListElements` |  |\n| `itemListElements.position` | The position of the breadcrumb in the breadcrumb trail. Position 1 signifies the beginning of the trail. |\n| `itemListElements.name` | The title of the breadcrumb displayed for the user. |\n| `itemListElements.item` | The URL to the webpage that represents the breadcrumb. |\n\n### Blog\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#blog)\n\nIdentifies the page as a blog and outlines the available posts.\n\nimport React from 'react';\nimport { BlogPostJsonLd } from 'gatsby-plugin-next-seo';\n \\*\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Blog with several posts</h1\\>\n    <BlogJsonLd\n      url\\='https://example.com/blog'\n      headline\\='Blog headline'\n      images\\='https://example.com/photos/1x1/photo.jpg'\n      posts\\={\\[{ headline: 'Post 1', image: 'https://example.com/photos/1x1/photo.jpg' }, { headline: 'Post 2' }\\]}\n      datePublished\\='2015-02-05T08:00:00+08:00'\n      dateModified\\='2015-02-05T09:00:00+08:00'\n      authorName\\='Jane Blogs'\n      description\\='This is a mighty good description of this blog.'\n    /\\>\n  </\\>\n);\n\n### Book\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#book)\n\nThe `Book` component makes search engines an entry point for discovering your books and authors. Users can then buy the books that they find directly from Search results.\n\nAn example feed is shown below.\n\nimport React from 'react';\nimport { CourseJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Book JSON-LD</h1\\>\n    <BookJsonLd\n      author\\={{ name: 'Tolu B.' }}\n      url\\='https://example.com/tolub'\n      name\\='Rock your world - the final chapter'\n      workExample\\={\\[\n        {\n          bookFormat: 'AudiobookFormat',\n          isbn: '123123123',\n          potentialAction: {\n            expectsAcceptanceOf: {\n              '@type': 'Offer',\n              price: '6.99',\n              priceCurrency: 'USD',\n              eligibleRegion: {\n                '@type': 'Country',\n                name: 'US',\n              },\n              availability: 'http://schema.org/InStock',\n            },\n            target: {\n              '@type': 'EntryPoint',\n              urlTemplate:\n                'http://www.barnesandnoble.com/store/info/offer/0316769487?purchase=true',\n              actionPlatform: \\[\n                'http://schema.org/DesktopWebPlatform',\n                'http://schema.org/IOSPlatform',\n                'http://schema.org/AndroidPlatform',\n              \\],\n            },\n          },\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n### Speakable\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#speakable)\n\nThe speakable schema.org property identifies sections within an article or webpage that are best suited for audio playback using text-to-speech (TTS).\n\nAdding markup allows search engines and other applications to identify content to read aloud on voice assistant-enabled devices using TTS. Webpages with speakable structured data can use voice assistants to distribute the content through new channels and reach a wider base of users.\n\nimport React from 'react';\nimport { SpeakableJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Speakable JSON-LD</h1\\>\n    <SpeakableJsonLd cssSelector\\={\\['#abc', '#root'\\]} /\\>\n  </\\>\n);\n\n### FAQ\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq)\n\nA Frequently Asked Question (FAQ) page contains a list of questions and answers pertaining to a particular topic. Properly marked up FAQ pages may be eligible to have a rich result on Search and voice assistants.\n\nimport React from 'react';\nimport { FAQJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <FAQJsonLd\n      questions\\={\\[\n        { question: 'What?', answer: 'Stand' },\n        { question: 'How?', answer: 'Effort' },\n        { question: 'Why?', answer: 'Peace' },\n      \\]}\n    /\\>\n\n    <h1\\>What?</h1\\>\n    <p\\>Stand</p\\>\n\n    <h1\\>How?</h1\\>\n    <p\\>Effort</p\\>\n\n    <h1\\>Why?</h1\\>\n    <p\\>Peace</p\\>\n  </\\>\n);\n\n| Property | Type | Description |\n| --- | --- | --- |\n| [questions](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#question-interface) | `Question[]` | An array of Question elements which comprise the list of answered questions that this FAQPage is about. |\n\n#### Question Interface\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#question-interface)\n\nThe questions and answers for an FAQ Page.\n\n| Property | Type | Description |\n| --- | --- | --- |\n| [answer](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/docs/api/gatsby-plugin-next-seo.question.answer.md) | `string` | The answer to the question. There must be one answer per question. |\n| [question](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/docs/api/gatsby-plugin-next-seo.question.question.md) | `string` | The full text of the question. For example, \"How long does it take to process a refund?\". |\n\n### Course\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#course)\n\nimport React from 'react';\nimport { CourseJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Course JSON-LD</h1\\>\n    <CourseJsonLd\n      courseName\\='Course Name'\n      providerName\\='Course Provider'\n      providerUrl\\='https//www.example.com/provider'\n      description\\='Course description goes right here'\n    /\\>\n  </\\>\n);\n\n### Corporate Contact (Deprecated)\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#corporate-contact-deprecated)\n\nSee the [documentation](https://developers.google.com/search/docs/data-types/corporate-contact) with the reason for deprecation.\n\nimport React from 'react';\nimport { CorporateContactJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Corporate Contact JSON-LD</h1\\>\n    <CorporateContactJsonLd\n      url\\='http://www.your-company-site.com'\n      logo\\='http://www.example.com/logo.png'\n      contactPoint\\={\\[\n        {\n          telephone: '+1-401-555-1212',\n          contactType: 'customer service',\n          areaServed: 'US',\n          availableLanguage: \\['English', 'Spanish', 'French'\\],\n        },\n        {\n          telephone: '+1-877-746-0909',\n          contactType: 'customer service',\n          contactOption: 'TollFree',\n          availableLanguage: 'English',\n        },\n        {\n          telephone: '+1-877-453-1304',\n          contactType: 'technical support',\n          contactOption: 'TollFree',\n          areaServed: \\['US', 'CA'\\],\n          availableLanguage: \\['English', 'French'\\],\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `url` | Url to the home page of the company's official site. |\n| `contactPoint` |  |\n| `contactPoint.telephone` | An internationalized version of the phone number, starting with the \"+\" symbol and country code |\n| `contactPoint.contactType` | Description of the purpose of the phone number i.e. `Technical Support`. |\n\n**Recommended ContactPoint properties**\n\n| Property | Info |\n| --- | --- |\n| `contactPoint.areaServed` | `String` or `Array` of geographical regions served by the business. Example `\"US\"` or `[\"US\", \"CA\", \"MX\"]` |\n| `contactPoint.availableLanguage` | Details about the language spoken. Example `\"English\"` or `[\"English\", \"French\"]` |\n| `gecontactPointo.contactOption` | Details about the phone number. Example `\"TollFree\"` |\n\n### Local Business\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#local-business)\n\nLocal business is supported with a sub-set of properties.\n\n<LocalBusinessJsonLd\n  type\\='Store'\n  id\\='http://davesdeptstore.example.com'\n  name\\=\"Dave's Department Store\"\n  description\\=\"Dave's latest department store in San Jose, now open\"\n  url\\='http://www.example.com/store-locator/sl/San-Jose-Westgate-Store/1427'\n  telephone\\='+14088717984'\n  address\\={{\n    streetAddress: '1600 Saratoga Ave',\n    addressLocality: 'San Jose',\n    addressRegion: 'CA',\n    postalCode: '95129',\n    addressCountry: 'US',\n  }}\n  geo\\={{\n    latitude: '37.293058',\n    longitude: '-121.988331',\n  }}\n  images\\={\\[\n    'https://example.com/photos/1x1/photo.jpg',\n    'https://example.com/photos/4x3/photo.jpg',\n    'https://example.com/photos/16x9/photo.jpg',\n  \\]}\n/\\>\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `@id` | Globally unique ID of the specific business location in the form of a URL. |\n| `type` | LocalBusiness or any sub-type |\n| `address` | Address of the specific business location |\n| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |\n| `address.addressLocality` | City |\n| `address.addressRegion` | State or province, if applicable. |\n| `address.postalCode` | Postal or zip code. |\n| `address.streetAddress` | Street number, street name, and unit number. |\n| `name` | Business name. |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `description` | Description of the business location |\n| `geo` | Geographic coordinates of the business. |\n| `geo.latitude` | The latitude of the business location |\n| `geo.longitude` | The longitude of the business location |\n| `images` | An image or images of the business. Required for valid markup depending on the type |\n| `telephone` | A business phone number meant to be the primary contact method for customers. |\n| `url` | The fully-qualified URL of the specific business location. |\n\n**NOTE:**\n\nImages are required for most of the types that you can use for `LocalBusiness`, if in doubt you should add an image. You can check your generated JSON over at Google's [Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool)\n\n### Logo\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#logo)\n\nimport React from 'react';\nimport { LogoJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Logo JSON-LD</h1\\>\n    <LogoJsonLd\n      logo\\='http://www.your-site.com/images/logo.jpg'\n      url\\='http://www.your-site.com'\n    /\\>\n  </\\>\n);\n\n| Property | Info |\n| --- | --- |\n| `url` | The URL of the website associated with the logo. [Logo guidelines](https://developers.google.com/search/docs/data-types/logo#definitions) |\n| `logo` | URL of a logo that is representative of the organization. |\n\n### Product\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#product)\n\nimport React from 'react';\nimport { ProductJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Product JSON-LD</h1\\>\n    <ProductJsonLd\n      productName\\='Executive Anvil'\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      description\\=\"Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.\"\n      brand\\='ACME'\n      reviews\\={\\[\n        {\n          author: 'Jim',\n          datePublished: '2017-01-06T03:37:40Z',\n          reviewBody:\n            'This is my favorite product yet! Thanks Nate for the example products and reviews.',\n          name: 'So awesome!!!',\n          reviewRating: {\n            bestRating: '5',\n            ratingValue: '5',\n            worstRating: '1',\n          },\n        },\n      \\]}\n      aggregateRating\\={{\n        ratingValue: '4.4',\n        reviewCount: '89',\n      }}\n      offers\\={{\n        price: '119.99',\n        priceCurrency: 'USD',\n        priceValidUntil: '2020-11-05',\n        itemCondition: 'http://schema.org/UsedCondition',\n        availability: 'http://schema.org/InStock',\n        url: 'https://www.example.com/executive-anvil',\n        seller: {\n          name: 'Executive Objects',\n        },\n      }}\n      mpn\\='925872'\n    /\\>\n  </\\>\n);\n\nAlso available: `sku`, `gtin8`, `gtin13`, `gtin14`.\n\nValid values for `offers.itemCondition`:\n\n*   [https://schema.org/DamagedCondition](https://schema.org/DamagedCondition)\n*   [https://schema.org/NewCondition](https://schema.org/NewCondition)\n*   [https://schema.org/RefurbishedCondition](https://schema.org/RefurbishedCondition)\n*   [https://schema.org/UsedCondition](https://schema.org/UsedCondition)\n\nValid values fro `offers.availability`:\n\n*   [https://schema.org/Discontinued](https://schema.org/Discontinued)\n*   [https://schema.org/InStock](https://schema.org/InStock)\n*   [https://schema.org/InStoreOnly](https://schema.org/InStoreOnly)\n*   [https://schema.org/LimitedAvailability](https://schema.org/LimitedAvailability)\n*   [https://schema.org/OnlineOnly](https://schema.org/OnlineOnly)\n*   [https://schema.org/OutOfStock](https://schema.org/OutOfStock)\n*   [https://schema.org/PreOrder](https://schema.org/PreOrder)\n*   [https://schema.org/PreSale](https://schema.org/PreSale)\n*   [https://schema.org/SoldOut](https://schema.org/SoldOut)\n\nMore info on the product data type can be found [here](https://developers.google.com/search/docs/data-types/product).\n\n### Social Profile (Deprecated)\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#social-profile-deprecated)\n\nSee the [documentation](https://developers.google.com/search/docs/data-types/social-profile) with the reason for deprecation.\n\nimport React from 'react';\nimport { SocialProfileJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Social Profile JSON-LD</h1\\>\n    <SocialProfileJsonLd\n      type\\='Person'\n      name\\='your name'\n      url\\='http://www.your-site.com'\n      sameAs\\={\\[\n        'http://www.facebook.com/your-profile',\n        'http://instagram.com/yourProfile',\n        'http://www.linkedin.com/in/yourprofile',\n        'http://plus.google.com/your\\_profile',\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `type` | Person or Organization |\n| `name` | The name of the person or organization |\n| `url` | The URL for the person's or organization's official website. |\n| `sameAs` | An array of URLs for the person's or organization's official social media profile page(s) |\n\n**Google Supported Social Profiles**\n\n*   Facebook\n*   Twitter\n*   Google+\n*   Instagram\n*   YouTube\n*   LinkedIn\n*   Myspace\n*   Pinterest\n*   SoundCloud\n*   Tumblr\n\n### JsonLd\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#jsonld)\n\nThis is the base JSON component that allows you to create your own JSON LD components according to the spec.\n\n[Google Docs for Social Profile](https://developers.google.com/search/docs/data-types/social-profile)\n\n### Sitelinks Search Box\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#sitelinks-search-box)\n\nThe `SitelinksSearchBoxJsonLd` component can be used to add JSON-LD structured data to your website for a Sitelinks search box.\n\nSee [here](https://developers.google.com/search/docs/advanced/structured-data/sitelinks-searchbox) for further documentation.\n\nimport React from 'react';\nimport { SitelinksSearchBoxJsonLd } from 'gatsby-plugin-next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Sitelinks Search Box JSON-LD</h1\\>\n    <SitelinksSearchBoxJsonLd\n      url\\='https://example.com/'\n      searchHandlerQueryStringUrl\\='https://example.com/?q='\n    /\\>\n  </\\>\n);\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `url` | The URL of the canonical homepage of the website associated with the Sitelinks search box. |\n| `searchHandlerQueryStringUrl` | Define the website's search engine query string as a URL. |\n|  |  |\n\nAPI Docs\n--------\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#api-docs)\n\nYou can explore the [**api documentation here**](https://github.com/ifiokjr/gatsby-plugin-next-seo/blob/master/docs/api/gatsby-plugin-next-seo.md).\n\nFAQ\n---\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#faq-1)\n\n### Why did you choose `gatsby-plugin-next-seo` as the project name?\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#why-did-you-choose-gatsby-plugin-next-seo-as-the-project-name)\n\nUnfortunately the better options [gatsby-seo](https://github.com/sidharthachatterjee/gatsby-seo#readme) and [gatsby-plugin-seo](https://github.com/franklintarter/gatsby-plugin-seo/tree/master/gatsby-plugin-seo) were already taken. As a result I've used gatsby-plugin-**next-seo** as a shout out to the original **next-seo** project from which this codebase has been forked.\n\nContributors\n------------\n\n[](https://github.com/ifiokjr/gatsby-plugin-next-seo?screenshot=true#contributors)\n\nThanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):\n\nThis project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!",
  "usage": {
    "tokens": 14298
  }
}
```
