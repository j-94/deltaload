---
title: GitHub - garmeeh/next-seo: Next SEO is a plug in that makes managing your SEO easier in Next.js projects.
description: Next SEO is a plug in that makes managing your SEO easier in Next.js projects. - garmeeh/next-seo
url: https://github.com/garmeeh/next-seo
timestamp: 2025-01-20T15:30:52.441Z
domain: github.com
path: garmeeh_next-seo
---

# GitHub - garmeeh/next-seo: Next SEO is a plug in that makes managing your SEO easier in Next.js projects.


Next SEO is a plug in that makes managing your SEO easier in Next.js projects. - garmeeh/next-seo


## Content

**Have you seen the new Next.js newsletter?**

[![Image 32: NextjsWeekly banner](https://github.com/garmeeh/next-seo/raw/master/next-js-weekly.png)](https://dub.sh/nextjsweekly)

**Useful Tools**

*   [dub](https://dub.co/?utm_source=next-seo&utm_medium=social&utm_campaign=next-seo) recently launched a useful Free UTM builder! You can use it [here](https://dub.sh/iKTxs7b)

Next SEO
--------

[](https://github.com/garmeeh/next-seo?screenshot=true#next-seo)

[![Image 33: npm](https://camo.githubusercontent.com/591dbb2ff6c6af1add2b4668f741ad390e60b5483b5d7caa6aeb387abec57251/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f6e6578742d73656f3f7374796c653d666c61742d737175617265)](https://camo.githubusercontent.com/591dbb2ff6c6af1add2b4668f741ad390e60b5483b5d7caa6aeb387abec57251/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f6e6578742d73656f3f7374796c653d666c61742d737175617265)

Next SEO is a plugin that makes managing your SEO easier in Next.js projects.

Pull requests are very welcome. Also make sure to check out the issues for feature requests if you are looking for inspiration on what to add.

**Feel like supporting this free plugin?**

It takes a lot of time to maintain an open source project so any small contribution is greatly appreciated.

Coffee fuels coding ☕️

[![Image 34: Buy Me A Coffee](https://camo.githubusercontent.com/7b8f7343bfc6e3c65c7901846637b603fd812f1a5f768d8b0572558bde859eb9/68747470733a2f2f63646e2e6275796d6561636f666665652e636f6d2f627574746f6e732f76322f64656661756c742d79656c6c6f772e706e67)](https://www.buymeacoffee.com/garmeeh)

[next-seo.wallet](https://unstoppabledomains.com/d/next-seo.wallet) (ERC20 & SOL)

**Note on app directory**

This note is only relevant if using the `app` directory.

For standard meta data (e.g., , <title\>) then it is highly recommended that you use the built-in `generateMetaData` method. You can check out the docs [here](https://beta.nextjs.org/docs/guides/seo#usage)

For JSON-LD then, the only change needed is to add `useAppDir={true}` to the JSON-LD component in use. You should add use this component in your `page.js` and NOT your `head.js`.

```
<ArticleJsonLd
  useAppDir={true}
  url="https://example.com/article"
  title="Article headline" <- required for app directory
  />
```

If you are using **`pages`** directory then `NextSeo` is **exactly what you need** for your SEO needs!

### Table of Contents

[](https://github.com/garmeeh/next-seo?screenshot=true#table-of-contents)

*   [Usage](https://github.com/garmeeh/next-seo?screenshot=true#usage)
    *   [Setup](https://github.com/garmeeh/next-seo?screenshot=true#setup)
    *   [Add SEO to Page](https://github.com/garmeeh/next-seo?screenshot=true#add-seo-to-page)
    *   [Default SEO Configuration](https://github.com/garmeeh/next-seo?screenshot=true#default-seo-configuration)
    *   [NextSeo Options](https://github.com/garmeeh/next-seo?screenshot=true#nextseo-options)
        *   [Title Template](https://github.com/garmeeh/next-seo?screenshot=true#title-template)
        *   [Default Title](https://github.com/garmeeh/next-seo?screenshot=true#default-title)
        *   [No Index](https://github.com/garmeeh/next-seo?screenshot=true#no-index)
        *   [dangerouslySetAllPagesToNoIndex](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonoindex)
        *   [No Follow](https://github.com/garmeeh/next-seo?screenshot=true#no-follow)
        *   [dangerouslySetAllPagesToNoFollow](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonofollow)
        *   [robotsProps](https://github.com/garmeeh/next-seo?screenshot=true#robotsprops)
        *   [Twitter](https://github.com/garmeeh/next-seo?screenshot=true#twitter)
        *   [Facebook](https://github.com/garmeeh/next-seo?screenshot=true#facebook)
        *   [Canonical URL](https://github.com/garmeeh/next-seo?screenshot=true#canonical-url)
        *   [Alternate](https://github.com/garmeeh/next-seo?screenshot=true#alternate)
        *   [Additional Meta Tags](https://github.com/garmeeh/next-seo?screenshot=true#additional-meta-tags)
        *   [Additional Link Tags](https://github.com/garmeeh/next-seo?screenshot=true#additional-link-tags)
*   [Open Graph](https://github.com/garmeeh/next-seo?screenshot=true#open-graph)
    *   [Open Graph Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples)
        *   [Basic](https://github.com/garmeeh/next-seo?screenshot=true#basic)
        *   [Video](https://github.com/garmeeh/next-seo?screenshot=true#video)
        *   [Audio](https://github.com/garmeeh/next-seo?screenshot=true#audio)
        *   [Article](https://github.com/garmeeh/next-seo?screenshot=true#article)
        *   [Book](https://github.com/garmeeh/next-seo?screenshot=true#book)
        *   [Profile](https://github.com/garmeeh/next-seo?screenshot=true#profile)
*   [JSON-LD](https://github.com/garmeeh/next-seo?screenshot=true#json-ld)
    *   [JSON-LD Security](https://github.com/garmeeh/next-seo?screenshot=true#json-ld-security)
    *   [Handling multiple instances](https://github.com/garmeeh/next-seo?screenshot=true#handling-multiple-instances)
    *   [Article](https://github.com/garmeeh/next-seo?screenshot=true#article-1)
    *   [Breadcrumb](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb)
    *   [Blog](https://github.com/garmeeh/next-seo?screenshot=true#blog)
    *   [Campground](https://github.com/garmeeh/next-seo?screenshot=true#campground)
    *   [Recipe](https://github.com/garmeeh/next-seo?screenshot=true#recipe)
    *   [Sitelinks Search Box](https://github.com/garmeeh/next-seo?screenshot=true#sitelinks-search-box)
    *   [Course](https://github.com/garmeeh/next-seo?screenshot=true#course)
    *   [Dataset](https://github.com/garmeeh/next-seo?screenshot=true#dataset)
    *   [Corporate Contact](https://github.com/garmeeh/next-seo?screenshot=true#corporate-contact)
    *   [FAQ Page](https://github.com/garmeeh/next-seo?screenshot=true#faq-page)
    *   [How-to](https://github.com/garmeeh/next-seo?screenshot=true#how-to)
    *   [Job Posting](https://github.com/garmeeh/next-seo?screenshot=true#job-posting)
    *   [Local Business](https://github.com/garmeeh/next-seo?screenshot=true#local-business)
    *   [Logo](https://github.com/garmeeh/next-seo?screenshot=true#logo)
    *   [Product](https://github.com/garmeeh/next-seo?screenshot=true#product)
    *   [Social Profile](https://github.com/garmeeh/next-seo?screenshot=true#social-profile)
    *   [News Article](https://github.com/garmeeh/next-seo?screenshot=true#news-article)
    *   [Park](https://github.com/garmeeh/next-seo?screenshot=true#park)
    *   [Video](https://github.com/garmeeh/next-seo?screenshot=true#video-1)
    *   [VideoGame](https://github.com/garmeeh/next-seo?screenshot=true#videogame)
    *   [Event](https://github.com/garmeeh/next-seo?screenshot=true#event)
    *   [Q&A](https://github.com/garmeeh/next-seo?screenshot=true#qa)
    *   [Collection Page](https://github.com/garmeeh/next-seo?screenshot=true#collection-page)
    *   [Profile page](https://github.com/garmeeh/next-seo?screenshot=true#profile-page)
    *   [Carousel](https://github.com/garmeeh/next-seo?screenshot=true#carousel)
        *   [Default (Summary List)](https://github.com/garmeeh/next-seo?screenshot=true#default-summary-list)
        *   [Course](https://github.com/garmeeh/next-seo?screenshot=true#course-1)
        *   [Movie](https://github.com/garmeeh/next-seo?screenshot=true#movie)
        *   [Recipe](https://github.com/garmeeh/next-seo?screenshot=true#recipe-1)
        *   [Custom](https://github.com/garmeeh/next-seo?screenshot=true#custom)
    *   [Software App](https://github.com/garmeeh/next-seo?screenshot=true#software-app)
    *   [Organization](https://github.com/garmeeh/next-seo?screenshot=true#organization)
    *   [Brand](https://github.com/garmeeh/next-seo?screenshot=true#brand)
    *   [WebPage](https://github.com/garmeeh/next-seo?screenshot=true#webpage)
    *   [Image Metadata](https://github.com/garmeeh/next-seo?screenshot=true#image-metadata)
*   [Contributors](https://github.com/garmeeh/next-seo?screenshot=true#contributors)

Usage
-----

[](https://github.com/garmeeh/next-seo?screenshot=true#usage)

`NextSeo` works by including it on pages where you would like SEO attributes to be added. Once included on the page, you pass it a configuration object with the page's SEO properties. This can be dynamically generated at a page level, or in some cases, your API may return an SEO object.

### Setup

[](https://github.com/garmeeh/next-seo?screenshot=true#setup)

First, install it:

or

### Add SEO to Page

[](https://github.com/garmeeh/next-seo?screenshot=true#add-seo-to-page)

* * *

**Using Next.js app directory introduced in Next.js 13?**

If you are using the Next.js app directory, then it is highly recommended that you use the built-in `generateMetaData` method. You can check out the docs [here](https://beta.nextjs.org/docs/guides/seo#usage)

If you are using the `pages` directory, then `NextSeo` is exactly what you need for your SEO needs!

* * *

Then, you need to import `NextSeo` and add the desired properties. This will render out the tags in the `<head>` for SEO. At a bare minimum, you should add a title and description.

**Example with just title and description:**

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
      title\="Simple Usage Example"
      description\="A short description goes here."
    /\>
    <p\>Simple Usage</p\>
  </\>
);

export default Page;

But `NextSeo` gives you many more options that you can add. See below for a typical example of a page.

**Typical page example:**

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
      title\="Using More of Config"
      description\="This example uses more of the available config options."
      canonical\="https://www.canonical.ie/"
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
            type: 'image/jpeg',
          },
          {
            url: 'https://www.example.ie/og-image-02.jpg',
            width: 900,
            height: 800,
            alt: 'Og Image Alt Second',
            type: 'image/jpeg',
          },
          { url: 'https://www.example.ie/og-image-03.jpg' },
          { url: 'https://www.example.ie/og-image-04.jpg' },
        \],
        siteName: 'SiteName',
      }}
      twitter\={{
        handle: '@handle',
        site: '@site',
        cardType: 'summary\_large\_image',
      }}
    /\>
    <p\>SEO Added to Page</p\>
  </\>
);

export default Page;

**A note on Twitter Tags**

Props `cardType`, `site`, `handle` are equivalent to `twitter:card`, `twitter:site`, `twitter:creator`. Documentation can be found [here](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary).

Twitter will read the `og:title`, `og:image` and `og:description` tags for their card. `next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` to avoid duplication.

Some tools may report this as an error. See [Issue #14](https://github.com/garmeeh/next-seo/issues/14)

### Default SEO Configuration

[](https://github.com/garmeeh/next-seo?screenshot=true#default-seo-configuration)

`NextSeo` enables you to set some default SEO properties that will appear on all pages without needing to include anything on them. You can also override these on a page-by-page basis if needed.

To achieve this, you will need to create a custom `<App>`. In your pages directory, create a new file, `_app.js`. See the Next.js docs [here](https://nextjs.org/docs/advanced-features/custom-app) for more info on a custom `<App>`.

Within this file you will need to import `DefaultSeo` from `next-seo` and pass it props.

Here is a typical example:

import App, { Container } from 'next/app';
import { DefaultSeo } from 'next-seo';

// import your default seo configuration
import SEO from '../next-seo.config';

export default class MyApp extends App {
  render() {
    const { Component, pageProps } \= this.props;
    return (
      <Container\>
        <DefaultSeo
          openGraph\={{
            type: 'website',
            locale: 'en\_IE',
            url: 'https://www.url.ie/',
            siteName: 'SiteName',
          }}
          twitter\={{
            handle: '@handle',
            site: '@site',
            cardType: 'summary\_large\_image',
          }}
        /\>
        <Component {...pageProps} /\>
      </Container\>
    );
  }
}

To work properly, `DefaultSeo` should be placed above (before) `Component` due to the behavior of Next.js internals.

Alternatively, you can also create a config file to store default values such as `next-seo.config.js`

export default {
  openGraph: {
    type: 'website',
    locale: 'en\_IE',
    url: 'https://www.url.ie/',
    siteName: 'SiteName',
  },
  twitter: {
    handle: '@handle',
    site: '@site',
    cardType: 'summary\_large\_image',
  },
};

or like this, if you are using TypeScript

import { DefaultSeoProps } from 'next-seo';

const config: DefaultSeoProps \= {
  openGraph: {
    type: 'website',
    locale: 'en\_IE',
    url: 'https://www.url.ie/',
    siteName: 'SiteName',
  },
  twitter: {
    handle: '@handle',
    site: '@site',
    cardType: 'summary\_large\_image',
  },
};

export default config;

import at the top of `_app.js`

import SEO from '../next-seo.config';

and the `DefaultSeo` component can be used like this instead

From now on, all of your pages will have the defaults above applied.

**Note that `Container` is deprecated in Next.js v9.0.4 so you should replace that component here with `React.Fragment` on this version and later - see [here](https://github.com/zeit/next.js/blob/master/errors/app-container-deprecated.md)**

### NextSeo Options

[](https://github.com/garmeeh/next-seo?screenshot=true#nextseo-options)

| Property | Type | Description |
| --- | --- | --- |
| `titleTemplate` | string | Allows you to set default title template that will be added to your title [More Info](https://github.com/garmeeh/next-seo?screenshot=true#title-template) |
| `title` | string | Set the meta title of the page |
| `defaultTitle` | string | If no title is set on a page, this string will be used instead of an empty `titleTemplate` [More Info](https://github.com/garmeeh/next-seo?screenshot=true#default-title) |
| `noindex` | boolean (default false) | Sets whether page should be indexed or not [More Info](https://github.com/garmeeh/next-seo?screenshot=true#no-index) |
| `nofollow` | boolean (default false) | Sets whether page should be followed or not [More Info](https://github.com/garmeeh/next-seo?screenshot=true#no-follow) |
| `robotsProps` | Object | Set the more meta information for the `X-Robots-Tag` [More Info](https://github.com/garmeeh/next-seo?screenshot=true#robotsprops) |
| `description` | string | Set the page meta description |
| `canonical` | string | Set the page canonical url |
| `mobileAlternate.media` | string | Set what screen size the mobile website should be served from |
| `mobileAlternate.href` | string | Set the mobile page alternate url |
| `languageAlternates` | array | Set the language of the alternate urls. Expects array of objects with the shape: `{ hrefLang: string, href: string }` |
| `themeColor` | string | Indicates a suggested color that user agents should use to customize the display of the page or of the surrounding user interface. Must contain a valid CSS color |
| `additionalMetaTags` | array | Allows you to add a meta tag that is not documented here. [More Info](https://github.com/garmeeh/next-seo?screenshot=true#additional-meta-tags) |
| `additionalLinkTags` | array | Allows you to add a link tag that is not documented here. [More Info](https://github.com/garmeeh/next-seo?screenshot=true#additional-link-tags) |
| `twitter.cardType` | string | The card type, which will be one of `summary`, `summary_large_image`, `app`, or `player` |
| `twitter.site` | string | @username for the website used in the card footer |
| `twitter.handle` | string | @username for the content creator / author (outputs as `twitter:creator`) |
| `facebook.appId` | string | Used for Facebook Insights, you must add a facebook app ID to your page to for it [More Info](https://github.com/garmeeh/next-seo?screenshot=true#facebook) |
| `openGraph.url` | string | The canonical URL of your object that will be used as its permanent ID in the graph |
| `openGraph.type` | string | The type of your object. Depending on the type you specify, other properties may also be required [More Info](https://github.com/garmeeh/next-seo?screenshot=true#open-graph) |
| `openGraph.title` | string | The open graph title, this can be different than your meta title. |
| `openGraph.description` | string | The open graph description, this can be different than your meta description. |
| `openGraph.images` | array | An array of images (object) to be used by social media platforms, slack etc as a preview. If multiple supplied you can choose one when sharing. [See Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples) |
| `openGraph.videos` | array | An array of videos (object) |
| `openGraph.locale` | string | The locale the open graph tags are marked up in. Of the format language\_TERRITORY. Default is en\_US. |
| `openGraph.siteName` | string | If your object is part of a larger web site, the name which should be displayed for the overall site. |
| `openGraph.profile.firstName` | string | Person's first name. |
| `openGraph.profile.lastName` | string | Person's last name. |
| `openGraph.profile.username` | string | Person's username. |
| `openGraph.profile.gender` | string | Person's gender. |
| `openGraph.book.authors` | string\[\] | Writers of the article. [See Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples) |
| `openGraph.book.isbn` | string | The [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) |
| `openGraph.book.releaseDate` | datetime | The date the book was released. |
| `openGraph.book.tags` | string\[\] | Tag words associated with this book. |
| `openGraph.article.publishedTime` | datetime | When the article was first published. [See Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples) |
| `openGraph.article.modifiedTime` | datetime | When the article was last changed. |
| `openGraph.article.expirationTime` | datetime | When the article is out of date after. |
| `openGraph.article.authors` | string\[\] | Writers of the article. |
| `openGraph.article.section` | string | A high-level section name. E.g. Technology |
| `openGraph.article.tags` | string\[\] | Tag words associated with this article. |

#### Title Template

[](https://github.com/garmeeh/next-seo?screenshot=true#title-template)

Replaces `%s` with your title string

title \= 'This is my title';
titleTemplate \= 'Next SEO | %s';
// outputs: Next SEO | This is my title

title \= 'This is my title';
titleTemplate \= '%s | Next SEO';
// outputs: This is my title | Next SEO

#### Default Title

[](https://github.com/garmeeh/next-seo?screenshot=true#default-title)

title \= undefined;
titleTemplate \= 'Next SEO | %s';
defaultTitle \= 'Next SEO';
// outputs: Next SEO

#### No Index

[](https://github.com/garmeeh/next-seo?screenshot=true#no-index)

Setting this to `true` will set `noindex,follow` (to set `nofollow`, please refer to [`nofollow`](https://github.com/garmeeh/next-seo?screenshot=true#no-follow)). This works on a page by page basis. This property works in tandem with the `nofollow` property and together they populate the `robots` meta tag.

**Note:** The `noindex` and the [`nofollow`](https://github.com/garmeeh/next-seo?screenshot=true#no-follow) properties are a little different than all the others in the sense that setting them as a default does not work as expected. This is due to the fact Next SEO already has a default of `index,follow` because `next-seo` is a SEO plugin after all. So if you want to globally these properties, please see [dangerouslySetAllPagesToNoIndex](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).

**Example No Index on a single page:**

If you have a single page that you want no indexed you can achieve this by:

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo noindex\={true} /\>
    <p\>This page is no indexed</p\>
  </\>
);

export default Page;

/\*
<meta name="robots" content="noindex,follow"\>
\*/

#### dangerouslySetAllPagesToNoIndex

[](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonoindex)

It has the prefix `dangerously` because it will `noindex` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this. Just please be sure you want to `noindex` **EVERY** page. You can still override this at a page level if you have a use case to `index` a page. This can be done by setting `noindex: false`.

The only way to unset this is by removing the prop from the `DefaultSeo` in your custom `<App>`.

#### No Follow

[](https://github.com/garmeeh/next-seo?screenshot=true#no-follow)

Setting this to `true` will set `index,nofollow` (to set `noindex`, please refer to [`noindex`](https://github.com/garmeeh/next-seo?screenshot=true#no-index)). This works on a page-by-page basis. This property works in tandem with the `noindex` property, and together, they populate the `robots` meta tag.

**Note:** Unlike for the other properties, setting `noindex` and `nofollow` by default does not work as expected. This is because Next SEO has a default of `index,follow`, since `next-seo` is an SEO plugin after all. If you want to globally allow these properties, see [dangerouslySetAllPagesToNoIndex](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).

**Example No Follow on a single page:**

If you have a single page that you want no indexed you can achieve this by:

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo nofollow\={true} /\>
    <p\>This page is not followed</p\>
  </\>
);

export default Page;

/\*
<meta name="robots" content="index,nofollow"\>
\*/

#### dangerouslySetAllPagesToNoFollow

[](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonofollow)

It has the prefix of `dangerously` because it will `nofollow` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this. Just please be sure you want to `nofollow` **EVERY** page. You can still override this at a page level if you have a use case to `follow` a page. This can be done by setting `nofollow: false`.

The only way to unset this, is by removing the prop from the `DefaultSeo` in your custom `<App>`.

| `noindex` | `nofollow` | `meta` content of `robots` |
| --- | --- | --- |
| \-- | \-- | `index,follow` (default) |
| false | false | `index,follow` |
| true | \-- | `noindex,follow` |
| true | false | `noindex,follow` |
| \-- | true | `index,nofollow` |
| false | true | `index,nofollow` |
| true | true | `noindex,nofollow` |

#### robotsProps

[](https://github.com/garmeeh/next-seo?screenshot=true#robotsprops)

In addition to `index, follow` the `robots` meta tag accepts more properties to archive a more accurate crawling and serve better snippets for SEO bots that crawl your page.

Example:

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
      robotsProps\={{
        nosnippet: true,
        notranslate: true,
        noimageindex: true,
        noarchive: true,
        maxSnippet: \-1,
        maxImagePreview: 'none',
        maxVideoPreview: \-1,
      }}
    /\>
    <p\>Additional robots props in Next-SEO!!</p\>
  </\>
);

export default Page;

/\*
<meta name="robots" content="index,follow,nosnippet,max-snippet:-1,max-image-preview:none,noarchive,noimageindex,max-video-preview:-1,notranslate"\>
\*/

**Available properties**

| Property | Type | Description |
| --- | --- | --- |
| `noarchive` | boolean | Do not show a [cached link](https://support.google.com/websearch/answer/1687222) in search results. |
| `nosnippet` | boolean | Do not show a text snippet or video preview in the search results for this page. |
| `max-snippet` | number | Use a maximum of \[number\] characters as a textual snippet for this search result. [Read more](https://developers.google.com/search/reference/robots_meta_tag?hl=en-GB#directives) |
| `max-image-preview` | 'none','standard','large' | Set the maximum size of an image preview for this page in a search results. |
| `max-video-preview` | number | Use a maximum of \[number\] seconds as a video snippet for videos on this page in search results. [Read more](https://developers.google.com/search/reference/robots_meta_tag?hl=en-GB#directives) |
| `notranslate` | boolean | Do not offer translation of this page in search results. |
| `noimageindex` | boolean | Do not index images on this page. |
| `unavailable_after` | string | Do not show this page in search results after the specified date/time. The date/time must be specified in a widely adopted format including, but not limited to RFC 822, RFC 850, and ISO 8601. |

For more reference about the `X-Robots-Tag` visit [Google Search Central - Control Crawling and Indexing](https://developers.google.com/search/reference/robots_meta_tag?hl=en-GB#directives)

#### Twitter

[](https://github.com/garmeeh/next-seo?screenshot=true#twitter)

Twitter will read the `og:title`, `og:image` and `og:description` tags for their card, this is why `next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` so not to duplicate.

Some tools may report this as an error. See [Issue #14](https://github.com/garmeeh/next-seo/issues/14)

#### Facebook

[](https://github.com/garmeeh/next-seo?screenshot=true#facebook)

facebook\={{
  appId: '1234567890',
}}

Add this to your SEO config to include the fb:app\_id meta if you need to enable Facebook insights for your site. Information regarding this can be found in Facebook's [documentation](https://developers.facebook.com/docs/sharing/webmasters/)

#### Canonical URL

[](https://github.com/garmeeh/next-seo?screenshot=true#canonical-url)

Add this on a page-per-page basis when you want to consolidate duplicate URLs.

canonical \= 'https://www.canonical.ie/';

#### Alternate

[](https://github.com/garmeeh/next-seo?screenshot=true#alternate)

This link relation is used to indicate a relation between a desktop and a mobile website to search engines.

Example:

mobileAlternate\={{
  media: 'only screen and (max-width: 640px)',
  href: 'https://m.canonical.ie',
}}

languageAlternates\={\[{
  hrefLang: 'de-AT',
  href: 'https://www.canonical.ie/de',
}\]}

#### Additional Meta Tags

[](https://github.com/garmeeh/next-seo?screenshot=true#additional-meta-tags)

This allows you to add any other meta tags that are not covered in the `config` and should be used instead of `children` prop.

`content` is required. Then either `name`, `property` or `httpEquiv`. (Only one on each)

Example:

additionalMetaTags\={\[{
  property: 'dc:creator',
  content: 'Jane Doe'
}, {
  name: 'application-name',
  content: 'NextSeo'
}, {
  httpEquiv: 'x-ua-compatible',
  content: 'IE=edge; chrome=1'
}\]}

Invalid Examples:

These are invalid as they contain more than one of `name`, `property` and `httpEquiv` on the same entry.

additionalMetaTags\={\[{
  property: 'dc:creator',
  name: 'dc:creator',
  content: 'Jane Doe'
}, {
  property: 'application-name',
  httpEquiv: 'application-name',
  content: 'NextSeo'
}\]}

One thing to note on this is that it currently only supports unique tags unless you use the `keyOverride` prop to provide a unique [key](https://reactjs.org/docs/lists-and-keys.html#keys) to each additional meta tag.

The default behaviour (without a `keyOverride` prop) is to render one tag per unique `name` / `property` / `httpEquiv`. The last one defined will be rendered.

For example, if you pass 2 tags with the same `property`:

additionalMetaTags\={\[{
  property: 'dc:creator',
  content: 'Joe Bloggs'
}, {
  property: 'dc:creator',
  content: 'Jane Doe'
}\]}

it will result in this being rendered:

<meta property\="dc:creator" content\="Jane Doe" /\>

Providing an additional `keyOverride` property like this:

additionalMetaTags\={\[{
  property: 'dc:creator',
  content: 'Joe Bloggs',
  keyOverride: 'creator1',
}, {
  property: 'dc:creator',
  content: 'Jane Doe',
  keyOverride: 'creator2',
}\]}

results in the correct HTML being rendered:

<meta property\="dc:creator" content\="Joe Bloggs" /\>
<meta property\="dc:creator" content\="Jane Doe" /\>

#### Additional Link Tags

[](https://github.com/garmeeh/next-seo?screenshot=true#additional-link-tags)

This allows you to add any other link tags that are not covered in the `config`.

`rel` and `href` is required.

Example:

additionalLinkTags\={\[
  {
    rel: 'icon',
    href: 'https://www.test.ie/favicon.ico',
  },
  {
    rel: 'apple-touch-icon',
    href: 'https://www.test.ie/touch-icon-ipad.jpg',
    sizes: '76x76'
  },
  {
    rel: 'manifest',
    href: '/manifest.json'
  },
  {
    rel: 'preload',
    href: 'https://www.test.ie/font/sample-font.woof2',
    as: 'font',
    type: 'font/woff2',
    crossOrigin: 'anonymous'
  }
\]}

it will result in this being rendered:

<link rel\="icon" href\="https://www.test.ie/favicon.ico" /\>
<link
  rel\="apple-touch-icon"
  href\="https://www.test.ie/touch-icon-ipad.jpg"
  sizes\="76x76"
/\>
<link rel\="manifest" href\="/manifest.json" /\>
<link
  rel\="preload"
  href\="https://www.test.ie/font/sample-font.woof2"
  as\="font"
  type\="font/woff2"
  crossorigin\="anonymous"
/\>

Open Graph
----------

[](https://github.com/garmeeh/next-seo?screenshot=true#open-graph)

For the full specification please check out [http://ogp.me/](http://ogp.me/)

Next SEO currently supports:

*   [basic](https://github.com/garmeeh/next-seo?screenshot=true#basic)
*   [video](https://github.com/garmeeh/next-seo?screenshot=true#video)
*   [article](https://github.com/garmeeh/next-seo?screenshot=true#article)
*   [book](https://github.com/garmeeh/next-seo?screenshot=true#book)
*   [profile](https://github.com/garmeeh/next-seo?screenshot=true#profile)

### Open Graph Examples

[](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples)

#### Basic

[](https://github.com/garmeeh/next-seo?screenshot=true#basic)

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
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

export default Page;

**Note**

Multiple images are available from next.js version `7.0.0-canary.0`

For versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:

images: \[
  {
    url: 'https://www.example.ie/og-image-01.jpg',
    width: 800,
    height: 600,
    alt: 'Og Image Alt',
  },
\],

Supplying multiple images will not break anything, but only one will be added to the head.

#### Video

[](https://github.com/garmeeh/next-seo?screenshot=true#video)

Full info on [http://ogp.me/](http://ogp.me/#type_video)

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
      title\="Video Page Title"
      description\="Description of video page"
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
        siteName: 'SiteName',
      }}
    /\>
    <h1\>Video Page SEO</h1\>
  </\>
);

export default Page;

**Note**

Multiple images are available from next.js version `7.0.0-canary.0`

For versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:

images: \[
  {
    url: 'https://www.example.ie/og-image-01.jpg',
    width: 800,
    height: 600,
    alt: 'Og Image Alt',
  },
\],

Supplying multiple images will not break anything, but only one will be added to the head.

#### Audio

[](https://github.com/garmeeh/next-seo?screenshot=true#audio)

Full info on [http://ogp.me/](https://ogp.me/#structured)

import { NextSeo } from 'next-seo';
const Page \= () \=\> (
  <\>
    <NextSeo
      title\="Audio Page Title"
      description\="Description of audio page"
      openGraph\={{
        title: 'Open Graph Audio',
        description: 'Description of open graph audio',
        url: 'https://www.example.com/audio/audio',
        audio: \[
          {
            url: 'http://examples.opengraphprotocol.us/media/audio/1khz.mp3',
            secureUrl: 'https://d72cgtgi6hvvl.cloudfront.net/media/audio/1khz.mp3',
            type: "audio/mpeg"
          },
          {
            url: 'http://examples.opengraphprotocol.us/media/audio/250hz.mp3',
            secureUrl: 'https://d72cgtgi6hvvl.cloudfront.net/media/audio/250hz.mp3',
            type: "audio/mpeg"
          },
        \]
        site\_name: 'SiteName',
      }}
    /\>
    <h1\>Audio Page SEO</h1\>
  </\>
);
export default Page;

#### Article

[](https://github.com/garmeeh/next-seo?screenshot=true#article)

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
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

export default Page;

**Note**

Multiple images, authors, and tags are available from next.js version `7.0.0-canary.0`

For versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:

`images:`

images: \[
  {
    url: 'https://www.example.ie/og-image-01.jpg',
    width: 800,
    height: 600,
    alt: 'Og Image Alt',
  },
\],

`authors:`

authors: \[
  'https://www.example.com/authors/@firstnameA-lastnameA',
\],

`tags:`

Supplying multiple of any of the above will not break anything, but only one will be added to the head.

#### Book

[](https://github.com/garmeeh/next-seo?screenshot=true#book)

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
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

export default Page;

**Note**

Multiple images, authors, and tags are available from next.js version `7.0.0-canary.0`

For versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:

`images:`

images: \[
  {
    url: 'https://www.example.ie/og-image-01.jpg',
    width: 800,
    height: 600,
    alt: 'Og Image Alt',
  },
\],

`authors:`

authors: \[
  'https://www.example.com/authors/@firstnameA-lastnameA',
\],

`tags:`

Supplying multiple of any of the above will not break anything, but only one will be added to the head.

#### Profile

[](https://github.com/garmeeh/next-seo?screenshot=true#profile)

import { NextSeo } from 'next-seo';

const Page \= () \=\> (
  <\>
    <NextSeo
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

export default Page;

**Note**

Multiple images are available from next.js version `7.0.0-canary.0`

For versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:

images: \[
  {
    url: 'https://www.example.ie/og-image-01.jpg',
    width: 800,
    height: 600,
    alt: 'Og Image Alt',
  },
\],

Supplying multiple images will not break anything, but only one will be added to the head.

JSON-LD
-------

[](https://github.com/garmeeh/next-seo?screenshot=true#json-ld)

Next SEO now has the ability to set JSON-LD a form of structured data. Structured data is a standardized format for providing information about a page and classifying the page content.

Google has excellent content on JSON-LD -\> [HERE](https://developers.google.com/search/docs/data-types/article)

**If using the app directory then please ensure to add `useAppDir={true}` prop and that you are using the component in the `page.js`**

Below you will find a very basic page implementing each of the available JSON-LD types:

*   [Article](https://github.com/garmeeh/next-seo?screenshot=true#article-1)
*   [Breadcrumb](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb)
*   [Blog](https://github.com/garmeeh/next-seo?screenshot=true#blog)
*   [Campground](https://github.com/garmeeh/next-seo?screenshot=true#campground)
*   [Recipe](https://github.com/garmeeh/next-seo?screenshot=true#recipe)
*   [Sitelinks Search Box](https://github.com/garmeeh/next-seo?screenshot=true#sitelinks-search-box)
*   [Course](https://github.com/garmeeh/next-seo?screenshot=true#course)
*   [Dataset](https://github.com/garmeeh/next-seo?screenshot=true#dataset)
*   [Corporate Contact](https://github.com/garmeeh/next-seo?screenshot=true#corporate-contact)
*   [FAQ Page](https://github.com/garmeeh/next-seo?screenshot=true#faq-page)
*   [How-to](https://github.com/garmeeh/next-seo?screenshot=true#how-to)
*   [Job Posting](https://github.com/garmeeh/next-seo?screenshot=true#job-posting)
*   [Local Business](https://github.com/garmeeh/next-seo?screenshot=true#local-business)
*   [Product](https://github.com/garmeeh/next-seo?screenshot=true#product)
*   [Social Profile](https://github.com/garmeeh/next-seo?screenshot=true#social-profile)
*   [News Article](https://github.com/garmeeh/next-seo?screenshot=true#news-article)
*   [Park](https://github.com/garmeeh/next-seo?screenshot=true#park)

Pull requests are very welcome to add any from the list [found here](https://developers.google.com/search/docs/data-types/article)

#### JSON-LD Security

[](https://github.com/garmeeh/next-seo?screenshot=true#json-ld-security)

Just a quick note on security. To get JSON-LD onto the page it needs to be in a script tag. `next-seo` achieves this by using a script tag with `dangerouslySetInnerHTML`.

So if passing anything directly from a URL to one of the components below please ensure you sanitize it first if needed.

View `toJson.tsx` for implementation detail.

#### Handling multiple instances

[](https://github.com/garmeeh/next-seo?screenshot=true#handling-multiple-instances)

If your page requires multiple instances of a given JSON-LD component, you can specify unique `keyOverride` properties, and `next-seo` will handle the rest.

This comes in handy for blog rolls, search results, and overview pages.

Please fully research when you should and shouldn't add multiple instances of JSON-LD.

<ExampleJsonLd keyOverride\="my-new-key" /\>

### Article

[](https://github.com/garmeeh/next-seo?screenshot=true#article-1)

import { ArticleJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Article JSON-LD</h1\>
    <ArticleJsonLd
      useAppDir\={false}
      url\="https://example.com/article"
      title\="Article headline"
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      datePublished\="2015-02-05T08:00:00+08:00"
      dateModified\="2015-02-05T09:00:00+08:00"
      authorName\={\[
        {
          name: 'Jane Blogs',
          url: 'https://example.com',
        },
        {
          name: 'Mary Stone',
          url: 'https://example.com',
        },
      \]}
      publisherName\="Gary Meehan"
      publisherLogo\="https://www.example.com/photos/logo.jpg"
      description\="This is a mighty good description of this article."
      isAccessibleForFree\={true}
    /\>
  </\>
);

export default Page;

### Breadcrumb

[](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb)

import { BreadcrumbJsonLd } from 'next-seo';

const Page \= () \=\> (
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

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `itemListElements` |  |
| `itemListElements.position` | The position of the breadcrumb in the breadcrumb trail. Position 1 signifies the beginning of the trail. |
| `itemListElements.name` | The title of the breadcrumb displayed for the user. |
| `itemListElements.item` | The URL to the webpage that represents the breadcrumb. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Blog

[](https://github.com/garmeeh/next-seo?screenshot=true#blog)

import { ArticleJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Blog JSON-LD</h1\>
    <ArticleJsonLd
      type\="BlogPosting"
      url\="https://example.com/blog"
      title\="Blog headline"
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      datePublished\="2015-02-05T08:00:00+08:00"
      dateModified\="2015-02-05T09:00:00+08:00"
      authorName\="Jane Blogs"
      description\="This is a mighty good description of this blog."
    /\>
  </\>
);

export default Page;

### Campground

[](https://github.com/garmeeh/next-seo?screenshot=true#campground)

import { CampgroundJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Campground JSON-LD</h1\>
    <CampgroundJsonLd
      id\="https://www.example.com/campground/rip-van-winkle-campground"
      name\="Rip Van Winkle Campgrounds"
      url\="https://www.example.com/campground"
      telephone\="+18452468114"
      images\={\['https://example.com/photos/1x1/photo.jpg'\]}
      address\={{
        streetAddress: '149 Blue Mountain Rd',
        addressLocality: 'Saugerties',
        addressRegion: 'NY',
        postalCode: '12477',
        addressCountry: 'US',
      }}
      description\="Description about Rip Van Winkle Campgrounds"
      geo\={{
        latitude: '42.092599',
        longitude: '-74.018580',
      }}
      openingHours\={\[
        {
          opens: '09:00',
          closes: '17:00',
          dayOfWeek: \[
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
          \],
          validFrom: '2019-12-23',
          validThrough: '2020-04-02',
        },
      \]}
      petsAllowed
      rating\={{
        ratingValue: '5',
        ratingCount: '18',
      }}
      amenityFeature\={{
        name: 'Showers',
        value: true,
      }}
      priceRange\="$$"
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `@id` | Globally unique ID of the specific campground in the form of a URL. |
| `address` | Address of the specific campground location |
| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |
| `address.addressLocality` | City |
| `address.addressRegion` | State or province, if applicable. |
| `address.postalCode` | Postal or zip code. |
| `address.streetAddress` | Street number, street name, and unit number. |
| `name` | Campground name. |
| `description` | Campground description. |

**Supported properties**

| Property | Info |
| --- | --- |
| `geo` | Geographic coordinates of the campground. |
| `geo.latitude` | The latitude of the campground location |
| `geo.longitude` | The longitude of the campground location |
| `images` | An image or images of the campground. Required for valid markup depending on the type |
| `telephone` | A campground phone number meant to be the primary contact method for customers. |
| `url` | The fully-qualified URL of the specific campground. |
| `openingHours` | Opening hour specification of the campground. You can provide this as a single object, or an array of objects with the properties below. |
| `openingHours.opens` | The opening hour of the place or service on the given day(s) of the week. |
| `openingHours.closes` | The closing hour of the place or service on the given day(s) of the week. |
| `openingHours.dayOfWeek` | The day of the week for which these opening hours are valid. Can be a string or array of strings. Refer to [DayOfWeek](https://schema.org/DayOfWeek) |
| `openingHours.validFrom` | The date when the item becomes valid. |
| `openingHours.validThrough` | The date after when the item is not valid. |
| `isAccessibleForFree` | Whether or not the campground is accessible for free. |
| `petsAllowed` | Whether or not the campgroud allows pets. |
| `amenityFeature` | An amenity feature (e.g. a characteristic or service) of the campground. |
| `amenityFeature.name` | The name of the amenity. |
| `amenityFeature.value` | The value of the amenity. |
| `priceRange` | The price range of the campground, for example $$$. |
| `rating` | The average rating of the campground based on multiple ratings or reviews. |
| `rating.ratingValue` | The rating for the content. |
| `rating.ratingCount` | The count of total number of ratings. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Recipe

[](https://github.com/garmeeh/next-seo?screenshot=true#recipe)

import { RecipeJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Recipe JSON-LD</h1\>
    <RecipeJsonLd
      name\="Party Coffee Cake"
      description\="This coffee cake is awesome and perfect for parties."
      datePublished\="2018-03-10"
      authorName\={\['Jane Blogs', 'Mary Stone'\]}
      prepTime\="PT20M"
      cookTime\="PT30M"
      totalTime\="PT50M"
      keywords\="cake for a party, coffee"
      yields\="10"
      category\="Dessert"
      cuisine\="American"
      calories\={270}
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      ingredients\={\[
        '2 cups of flour',
        '3/4 cup white sugar',
        '2 teaspoons baking powder',
        '1/2 teaspoon salt',
        '1/2 cup butter',
        '2 eggs',
        '3/4 cup milk',
      \]}
      instructions\={\[
        {
          name: 'Preheat',
          text: 'Preheat the oven to 350 degrees F. Grease and flour a 9x9 inch pan.',
          url: 'https://example.com/party-coffee-cake#step1',
          image: 'https://example.com/photos/party-coffee-cake/step1.jpg',
        },
      \]}
      aggregateRating\={{
        ratingValue: '5',
        ratingCount: '18',
      }}
      video\={{
        name: 'How to make a Party Coffee Cake',
        description: 'This is how you make a Party Coffee Cake.',
        contentUrl: 'http://www.example.com/video123.mp4',
        embedUrl: 'http://www.example.com/videoplayer?video=123',
        uploadDate: '2018-02-05T08:00:00+08:00',
        duration: 'PT1M33S',
        thumbnailUrls: \[
          'https://example.com/photos/1x1/photo.jpg',
          'https://example.com/photos/4x3/photo.jpg',
          'https://example.com/photos/16x9/photo.jpg',
        \],
        expires: '2019-02-05T08:00:00+08:00',
        hasPart: {
          '@type': 'Clip',
          name: 'Preheat oven',
          startOffset: 30,
          url: 'http://www.example.com/example?t=30',
        },
        watchCount: 2347,
        publication: {
          '@type': 'BroadcastEvent',
          isLiveBroadcast: true,
          startDate: '2020-10-24T14:00:00+00:00',
          endDate: '2020-10-24T14:37:14+00:00',
        },
        regionsAllowed: \['IT', 'NL'\],
      }}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `name` | The name of the recipe |
| `description` | A description of the recipe |
| `authorName` | The name of the recipe author. Can be a string or array of strings. |
| `ingredients` | A list of ingredient strings |
| `instructions` | \- |
| `instructions.name` | The name of the instruction step. |
| `instructions.text` | The directions of the instruction step. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Sitelinks Search Box

[](https://github.com/garmeeh/next-seo?screenshot=true#sitelinks-search-box)

import { SiteLinksSearchBoxJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Sitelinks Search Box JSON-LD</h1\>
    <SiteLinksSearchBoxJsonLd
      url\="https://www.example.com"
      potentialActions\={\[
        {
          target: 'https://query.example.com/search?q',
          queryInput: 'search\_term\_string',
        },
        {
          target: 'android-app://com.example/https/query.example.com/search/?q',
          queryInput: 'search\_term\_string',
        },
      \]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `url` | URL of the website associated with the sitelinks searchbox |
| `potentialActions` | Array of one or two SearchAction objects. Describes the URI to send the query to, and the syntax of the request that is sent |
| `potentialActions.target` | For websites, the URL of the handler that should receive and handle the search query; for apps, the URI of the intent handler for your search engine that should handle queries |
| `potentialActions.queryInput` | Placeholder used in target, gets substituted for user given query |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

Read the [documentation](https://developers.google.com/search/docs/appearance/structured-data/sitelinks-searchbox)

### Course

[](https://github.com/garmeeh/next-seo?screenshot=true#course)

import { CourseJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Course JSON-LD</h1\>
    <CourseJsonLd
      courseName\="Course Name"
      description\="Introductory CS course laying out the basics."
      provider\={{
        name: 'Course Provider',
        url: 'https//www.example.com/provider',
      }}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `courseName` | The title of the course. |
| `description` | A description of the course. Display limit of 60 characters. |
| `provider.name` | The course provider name. |
| `provider.url` | The course provider name url. |

**Recommended properties**

| Property | Info |
| --- | --- |
| `providerUrl` | The url to the course provider. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Dataset

[](https://github.com/garmeeh/next-seo?screenshot=true#dataset)

import { DatasetJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Dataset JSON-LD</h1\>
    <DatasetJsonLd
      description\="The description needs to be at least 50 characters long"
      name\="name of the dataset"
      license\="https//www.example.com"
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `description` | A short summary describing a dataset. Needs to be between 50 and 5000 characters. |
| `name` | A license under which the dataset is distributed. |

**Recommended properties**

| Property | Info |
| --- | --- |
| `license` | The url to the course provider. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Corporate Contact

[](https://github.com/garmeeh/next-seo?screenshot=true#corporate-contact)

import { CorporateContactJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Corporate Contact JSON-LD</h1\>
    <CorporateContactJsonLd
      url\="http://www.your-company-site.com"
      logo\="http://www.example.com/logo.png"
      contactPoint\={\[
        {
          telephone: '+1-401-555-1212',
          contactType: 'customer service',
          email: 'customerservice@email.com',
          areaServed: 'US',
          availableLanguage: \['English', 'Spanish', 'French'\],
        },
        {
          telephone: '+1-877-746-0909',
          contactType: 'customer service',
          email: 'servicecustomer@email.com',
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

export default Page;

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
| `contactPoint.email` | Email asscosiated with the business\` |
| `gecontactPointo.contactOption` | Details about the phone number. Example `"TollFree"` |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### FAQ Page

[](https://github.com/garmeeh/next-seo?screenshot=true#faq-page)

import { FAQPageJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>FAQ Page JSON-LD</h1\>
    <FAQPageJsonLd
      mainEntity\={\[
        {
          questionName: 'How long is the delivery time?',
          acceptedAnswerText: '3-5 business days.',
        },
        {
          questionName: 'Where can I find information about product recalls?',
          acceptedAnswerText: 'Read more on under information.',
        },
      \]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `mainEntity` |  |
| `mainEntity.questionName` | The full text of the question. For example, "How long is the delivery time?". |
| `mainEntity.acceptedAnswerText` | The full answer to the question. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### How-to

[](https://github.com/garmeeh/next-seo?screenshot=true#how-to)

import { HowToJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>How-to JSON-LD</h1\>
    <HowToJsonLd
      name\="How to tile a kitchen backsplash"
      image\="https://example.com/photos/1x1/photo.jpg"
      estimatedCost\={{ currency: 'USD', value: '100' }}
      supply\={\['tiles', 'thin-set', 'mortar', 'tile grout', 'grout sealer'\]}
      tool\={\['notched trowel', 'bucket', 'large sponge'\]}
      step\={\[
        {
          url: 'https://example.com/kitchen#step1',
          name: 'Prepare the surfaces',
          itemListElement: \[
            {
              type: 'HowToTip',
              text: 'Turn off the power to the kitchen and then remove everything that is on the wall, such as outlet covers, switchplates, and any other item in the area that is to be tiled.',
            },
            {
              type: 'HowToDirection',
              text: 'Then clean the surface thoroughly to remove any grease or other debris and tape off the area.',
            },
          \],
          image: 'https://example.com/photos/1x1/photo-step1.jpg',
        },
      \]}
      totalTime\="P2D"
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `name` | Name of the HowTo |
| `step` | An array of HowToStep elements which comprise the full instructions of the how-to. |

**Supported properties**

| Property | Info |
| --- | --- |
| `estimatedCost` | The estimated cost of the supplies consumed when performing instructions. |
| `image` | Image of the completed how-to. |
| `supply` | A supply consumed when performing instructions or a direction. |
| `tool` | An object used (but not consumed) when performing instructions or a direction. |
| `totalTime` | The total time required to perform all instructions or directions (including time to prepare the supplies), in ISO 8601 duration format. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Job Posting

[](https://github.com/garmeeh/next-seo?screenshot=true#job-posting)

import { JobPostingJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Job Posting JSON-LD</h1\>
    <JobPostingJsonLd
      datePosted\="2020-01-06T03:37:40Z"
      description\="Company is looking for a software developer...."
      hiringOrganization\={{
        name: 'company name',
        sameAs: 'www.company-website-url.dev',
      }}
      jobLocation\={{
        streetAddress: '17 street address',
        addressLocality: 'Paris',
        addressRegion: 'Ile-de-France',
        postalCode: '75001',
        addressCountry: 'France',
      }}
      title\="Job Title"
      baseSalary\={{
        currency: 'EUR',
        value: 40, // Can also be a salary range, like \[40, 50\]
        unitText: 'HOUR',
      }}
      employmentType\="FULL\_TIME"
      jobLocationType\="TELECOMMUTE"
      validThrough\="2020-01-06"
      applicantLocationRequirements\="FR"
      experienceRequirements\={{
        occupational: {
          minimumMonthsOfExperience: 12,
        },
        educational: {
          credentialCategory: 'high school',
        },
        experienceInPlaceOfEducation: true,
      }}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `datePosted` | The original date that employer posted the job in ISO 8601 format |
| `description` | The full description of the job in HTML format |
| `hiringOrganization` | An object containing information about the company hiring with the following fields or the string `'confidential'` when hiring anonymously |
| `hiringOrganization.name` | Name of the company offering the job position |
| `hiringOrganization.sameAs` | URL of a reference Web page |
| `title` | The title of the job (not the title of the posting) |
| `validThrough` | The date when the job posting will expire in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) |

**Supported properties**

| Property | Info |
| --- | --- |
| `applicantLocationRequirements` | The geographic location(s) in which employees may be located for to be eligible for the remote job |
| `baseSalary` |  |
| `baseSalary.currency` | The currency in which the monetary amount is expressed |
| `baseSalary.value` | The value of the quantitative value. You can also provide an array of minimum and maximum salaries. . |
| `baseSalary.unitText` | A string indicating the unit of measurement [Base salary guideline](https://developers.google.com/search/docs/data-types/job-posting#basesalary) |
| `employmentType` | Type of employment [Employement type guideline](https://developers.google.com/search/docs/data-types/job-posting#basesalary) |
| `jobLocation` | The physical location(s) of the business where the employee will report to work (such as an office or worksite), not the location where the job was posted. |
| `jobLocation.streetAddress` | The street address. For example, 1600 Amphitheatre Pkwy |
| `jobLocation.addressLocality` | The locality. For example, Mountain View. |
| `jobLocation.addressRegion` | The region. For example, CA. |
| `jobLocation.postalCode` | The postal code. For example, 94043 |
| `jobLocation.addressCountry` | The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code. |
| `jobLocationType` | A description of the job location [Job Location type guideline](https://developers.google.com/search/docs/data-types/job-posting#job-location-type) |
| `hiringOrganization.logo` | Logos on third-party job sites [Hiring Organization guideline](https://developers.google.com/search/docs/data-types/job-posting#hiring) |
| `experienceRequirements.occupational.minimumMonthsOfExperience` | The minimum number of months of experience that are required for the job posting. [Experience and Education Requirements](https://developers.google.com/search/docs/appearance/structured-data/job-posting#education-and-experience-properties-beta) |
| `experienceRequirements.educational.credentialCategory` | The level of education that's required for the job posting. Use one of the following: `high school`, `associate degree`, `bachelor degree`, `professional certificate`, `postgraduate degree` |
| `experienceRequirements.experienceInPlaceOfEducation` | Boolean: If set to true, this property indicates whether a job posting will accept experience in place of its formal educational qualifications. If set to true, you must include both the experienceRequirements and educationRequirements properties. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Local Business

[](https://github.com/garmeeh/next-seo?screenshot=true#local-business)

Local business is supported with a sub-set of properties.

<LocalBusinessJsonLd
  type\="Store"
  id\="http://davesdeptstore.example.com"
  name\="Dave's Department Store"
  description\="Dave's latest department store in San Jose, now open"
  url\="http://www.example.com/store-locator/sl/San-Jose-Westgate-Store/1427"
  telephone\="+14088717984"
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
  sameAs\={\[
    'www.company-website-url1.dev',
    'www.company-website-url2.dev',
    'www.company-website-url3.dev',
  \]}
  openingHours\={\[
    {
      opens: '08:00',
      closes: '23:59',
      dayOfWeek: \[
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
      \],
      validFrom: '2019-12-23',
      validThrough: '2020-04-02',
    },
    {
      opens: '14:00',
      closes: '20:00',
      dayOfWeek: 'Sunday',
      validFrom: '2019-12-23',
      validThrough: '2020-04-02',
    },
  \]}
  rating\={{
    ratingValue: '4.5',
    ratingCount: '2',
  }}
  review\={\[
    {
      author: 'John Doe',
      datePublished: '2006-05-04',
      name: 'A masterpiece of literature',
      reviewBody:
        'I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.',
      reviewRating: {
        bestRating: '5',
        worstRating: '1',
        reviewAspect: 'Ambiance',
        ratingValue: '4',
      },
    },
    {
      author: 'Bob Smith',
      datePublished: '2006-06-15',
      name: 'A good read.',
      reviewBody: "Catcher in the Rye is a fun book. It's a good book to read.",
      reviewRating: {
        ratingValue: '4',
      },
    },
  \]}
  makesOffer\={\[
    {
      priceSpecification: {
        type: 'UnitPriceSpecification',
        priceCurrency: 'EUR',
        price: '1000-10000',
      },
      itemOffered: {
        name: 'Motion Design Services',
        description:
          'We are the expert of animation and motion design productions.',
      },
    },
    {
      priceSpecification: {
        type: 'UnitPriceSpecification',
        priceCurrency: 'EUR',
        price: '2000-10000',
      },
      itemOffered: {
        name: 'Branding Services',
        description:
          'Real footage is a powerful tool when it comes to show what the business is about. Can be used to present your company, show your factory, promote a product packshot, or just tell any story. It can help create emotional links with your audience by showing punchy images.',
      },
    },
  \]}
  areaServed\={\[
    {
      geoMidpoint: {
        latitude: '41.108237',
        longitude: '-80.642982',
      },
      geoRadius: '1000',
    },
    {
      geoMidpoint: {
        latitude: '51.108237',
        longitude: '-80.642982',
      },
      geoRadius: '1000',
    },
  \]}
  action\={{
    actionName: 'potentialAction',
    actionType: 'ReviewAction',
    target: 'https://www.example.com/review/this/business',
  }}
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
| `rating` | The average rating of business based on multiple ratings or reviews. |
| `rating.ratingValue` | The rating for the content. |
| `rating.ratingCount` | The count of total number of ratings. |
| `priceRange` | The relative price range of the business. |
| `servesCuisine` | The type of cuisine the restaurant serves. |
| `images` | An image or images of the business. Required for valid markup depending on the type |
| `telephone` | A business phone number meant to be the primary contact method for customers. |
| `url` | The fully-qualified URL of the specific business location. |
| `sameAs` | An array of URLs that represent this business |
| `openingHours` | Opening hour specification of business. You can provide this as a single object, or an array of objects with the properties below. |
| `openingHours.opens` | The opening hour of the place or service on the given day(s) of the week. |
| `openingHours.closes` | The closing hour of the place or service on the given day(s) of the week. |
| `openingHours.dayOfWeek` | The day of the week for which these opening hours are valid. Can be a string or array of strings. Refer to [DayOfWeek](https://schema.org/DayOfWeek) |
| `openingHours.validFrom` | The date when the item becomes valid. |
| `openingHours.validThrough` | The date after when the item is not valid. |
| `review` | A review of the local business. |
| `review.author` | The author of this content or rating. |
| `review.reviewBody` | The actual body of the review. |
| `review.datePublished` | Date of first broadcast/publication. |
| `review.name` | The name of the item. |
| `review.rating` | The rating given in this review |
| `review.rating.ratingValue` | The rating for the content. |
| `review.rating.reviewAspect` | This Review or Rating is relevant to this part or facet of the itemReviewed. |
| `review.rating.worstRating` | The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed. |
| `review.rating.bestRating` | The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed |
| `areasServed` | The geographic area where a service or offered item is provided. |
| `areasServed.GeoCircle` | A GeoCircle is a GeoShape representing a circular geographic area. |
| `areasServed.GeoCircle.geoMidpoint` | Indicates the GeoCoordinates at the centre of a GeoShape e.g. GeoCircle. |
| `areasServed.GeoCircle.geoMidpoint.latitude` | The latitude of a location. For example 37.42242 |
| `areasServed.GeoCircle.geoMidpoint.longitude` | The name of the item. |
| `areasServed.GeoCircle.geoRadius` | Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation). |
| `makesOffer` | A pointer to products or services offered by the organization or person. |
| `makesOffer.offer` | An offer to transfer some rights to an item or to provide a service |
| `makesOffer.offer.priceSpecification` | One or more detailed price specifications, indicating the unit price and delivery or payment charges. |
| `makesOffer.offer.priceSpecification.priceCurrency` | The currency of the price, or a price component when attached to PriceSpecification and its subtypes. |
| `makesOffer.offer.priceSpecification.price` | The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes. |
| `makesOffer.offer.itemOffered` | An item being offered (or demanded) |
| `makesOffer.offer.itemOffered.name` | The name of the item |
| `makesOffer.offer.itemOffered.description` | The description of the item. |
| `action` | An action performed by a direct agent and indirect participants upon a direct object. |
| `action.target` | Indicates a target EntryPoint for an Action. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

**NOTE:**

Images are recommended for most of the types that you can use for `LocalBusiness`; if in doubt, you should add an image. You can check your generated JSON over at Google's [Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool)

### Logo

[](https://github.com/garmeeh/next-seo?screenshot=true#logo)

import { LogoJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Logo JSON-LD</h1\>
    <LogoJsonLd
      logo\="http://www.your-site.com/images/logo.jpg"
      url\="http://www.your-site.com"
    /\>
  </\>
);

export default Page;

| Property | Info |
| --- | --- |
| `url` | The URL of the website associated with the logo. [Logo guidelines](https://developers.google.com/search/docs/data-types/logo#definitions) |
| `logo` | URL of a logo that is representative of the organization. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### Product

[](https://github.com/garmeeh/next-seo?screenshot=true#product)

import { ProductJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Product JSON-LD</h1\>
    <ProductJsonLd
      productName\="Executive Anvil"
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      description\="Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height."
      brand\="ACME"
      color\="blue"
      manufacturerName\="Gary Meehan"
      manufacturerLogo\="https://www.example.com/photos/logo.jpg"
      material\="steel"
      slogan\="For the business traveller looking for something to drop from a height."
      disambiguatingDescription\="Executive Anvil, perfect for the business traveller."
      releaseDate\="2014-02-05T08:00:00+08:00"
      productionDate\="2015-02-05T08:00:00+08:00"
      purchaseDate\="2015-02-06T08:00:00+08:00"
      award\="Best Executive Anvil Award."
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
          publisher: {
            type: 'Organization',
            name: 'TwoVit',
          },
        },
      \]}
      aggregateRating\={{
        ratingValue: '4.4',
        reviewCount: '89',
      }}
      offers\={\[
        {
          price: '119.99',
          priceCurrency: 'USD',
          priceValidUntil: '2020-11-05',
          itemCondition: 'https://schema.org/UsedCondition',
          availability: 'https://schema.org/InStock',
          url: 'https://www.example.com/executive-anvil',
          seller: {
            name: 'Executive Objects',
          },
        },
        {
          price: '139.99',
          priceCurrency: 'CAD',
          priceValidUntil: '2020-09-05',
          itemCondition: 'https://schema.org/UsedCondition',
          availability: 'https://schema.org/InStock',
          url: 'https://www.example.ca/executive-anvil',
          seller: {
            name: 'Executive Objects',
          },
        },
      \]}
      mpn\="925872"
    /\>
  </\>
);

export default Page;

Also available: `sku`, `gtin8`, `gtin13`, `gtin14`.

Valid values for `offers.itemCondition`:

*   [https://schema.org/DamagedCondition](https://schema.org/DamagedCondition)
*   [https://schema.org/NewCondition](https://schema.org/NewCondition)
*   [https://schema.org/RefurbishedCondition](https://schema.org/RefurbishedCondition)
*   [https://schema.org/UsedCondition](https://schema.org/UsedCondition)

Valid values for `offers.availability`:

*   [https://schema.org/Discontinued](https://schema.org/Discontinued)
*   [https://schema.org/InStock](https://schema.org/InStock)
*   [https://schema.org/InStoreOnly](https://schema.org/InStoreOnly)
*   [https://schema.org/LimitedAvailability](https://schema.org/LimitedAvailability)
*   [https://schema.org/OnlineOnly](https://schema.org/OnlineOnly)
*   [https://schema.org/OutOfStock](https://schema.org/OutOfStock)
*   [https://schema.org/PreOrder](https://schema.org/PreOrder)
*   [https://schema.org/PreSale](https://schema.org/PreSale)
*   [https://schema.org/SoldOut](https://schema.org/SoldOut)

The property `aggregateOffer` is also available: (It is ignored if `offers` is set)

**Required properties**

| Property | Info |
| --- | --- |
| `lowPrice` | The lowest price of all offers available. Use a floating point number. |
| `priceCurrency` | The currency used to describe the product price, in three-letter ISO 4217 format. |

**Recommended properties**

| Property | Info |
| --- | --- |
| `highPrice` | The highest price of all offers available. Use a floating point number. |
| `offerCount` | The number of offers for the product. |
| `offers` | An offer to transfer some rights to an item or to provide a service. You can provide this as a single object, or an array of objects with the properties below. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

More info on the product data type can be found [here](https://developers.google.com/search/docs/data-types/product).

### Social Profile

[](https://github.com/garmeeh/next-seo?screenshot=true#social-profile)

import { SocialProfileJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Social Profile JSON-LD</h1\>
    <SocialProfileJsonLd
      type\="Person"
      name\="your name"
      url\="http://www.your-site.com"
      sameAs\={\[
        'http://www.facebook.com/your-profile',
        'http://instagram.com/yourProfile',
        'http://www.linkedin.com/in/yourprofile',
        'http://plus.google.com/your\_profile',
      \]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `type` | Person or Organization |
| `name` | The name of the person or organization |
| `url` | The URL for the person's or organization's official website. |
| `sameAs` | An array of URLs for the person's or organization's official social media profile page(s) |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

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

### News Article

[](https://github.com/garmeeh/next-seo?screenshot=true#news-article)

import { NewsArticleJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>News Article JSON-LD</h1\>
    <NewsArticleJsonLd
      url\="https://example.com/article"
      title\="Article headline"
      images\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      section\="politic"
      keywords\="prayuth,taksin"
      datePublished\="2015-02-05T08:00:00+08:00"
      dateModified\="2015-02-05T09:00:00+08:00"
      authorName\="Jane Blogs"
      publisherName\="Gary Meehan"
      publisherLogo\="https://www.example.com/photos/logo.jpg"
      description\="This is a mighty good description of this article."
      body\="This is all text for this news article"
      isAccessibleForFree\={true}
    /\>
  </\>
);

export default Page;

### Park

[](https://github.com/garmeeh/next-seo?screenshot=true#park)

import { ParkJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Park JSON-LD</h1\>
    <ParkJsonLd
      id\="https://www.example.com/park/minnewaska-state-park"
      name\="Minnewaska State Park"
      url\="https://www.example.com/park"
      telephone\="+18452550752"
      images\={\['https://example.com/photos/1x1/photo.jpg'\]}
      address\={{
        streetAddress: '5281 Route 44-55',
        addressLocality: 'Kerhonkson',
        addressRegion: 'NY',
        postalCode: '12446',
        addressCountry: 'US',
      }}
      description\="A wonderful description about Minnewaska State Park"
      geo\={{
        latitude: '41.735149',
        longitude: '-74.239037',
      }}
      openingHours\={\[
        {
          opens: '09:00',
          closes: '18:00',
          dayOfWeek: \[
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
          \],
          validFrom: '2019-12-23',
          validThrough: '2020-04-02',
        },
      \]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `@id` | Globally unique ID of the specific park in the form of a URL. |
| `address` | Address of the specific park location |
| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |
| `address.addressLocality` | City |
| `address.addressRegion` | State or province, if applicable. |
| `address.postalCode` | Postal or zip code. |
| `address.streetAddress` | Street number, street name, and unit number. |
| `name` | Park name. |
| `description` | Park description. |

**Supported properties**

| Property | Info |
| --- | --- |
| `geo` | Geographic coordinates of the park. |
| `geo.latitude` | The latitude of the park location |
| `geo.longitude` | The longitude of the park location |
| `images` | An image or images of the park. Required for valid markup depending on the type |
| `telephone` | A business phone number meant to be the primary contact method for customers. |
| `url` | The fully-qualified URL of the specific park. |
| `openingHours` | Opening hour specification of the park. You can provide this as a single object, or an array of objects with the properties below. |
| `openingHours.opens` | The opening hour of the place or service on the given day(s) of the week. |
| `openingHours.closes` | The closing hour of the place or service on the given day(s) of the week. |
| `openingHours.dayOfWeek` | The day of the week for which these opening hours are valid. Can be a string or array of strings. Refer to [DayOfWeek](https://schema.org/DayOfWeek) |
| `openingHours.validFrom` | The date when the item becomes valid. |
| `openingHours.validThrough` | The date after when the item is not valid. |
| `isAccessibleForFree` | Whether or not the park is accessible for free. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside oft the app directory. |

[Google Docs for Social Profile](https://developers.google.com/search/docs/data-types/social-profile)

### Video

[](https://github.com/garmeeh/next-seo?screenshot=true#video-1)

import { VideoJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Video JSON-LD</h1\>
    <VideoJsonLd
      name\="How to make a Party Coffee Cake"
      description\="This is how you make a Party Coffee Cake."
      contentUrl\="http://www.example.com/video123.mp4"
      embedUrl\="http://www.example.com/videoplayer?video=123"
      uploadDate\="2018-02-05T08:00:00+08:00"
      duration\="PT1M33S"
      thumbnailUrls\={\[
        'https://example.com/photos/1x1/photo.jpg',
        'https://example.com/photos/4x3/photo.jpg',
        'https://example.com/photos/16x9/photo.jpg',
      \]}
      expires\="2019-02-05T08:00:00+08:00"
      hasPart\={{
        name: 'Preheat oven',
        startOffset: 30,
        url: 'http://www.example.com/example?t=30',
      }}
      watchCount\={2347}
      publication\={{
        isLiveBroadcast: true,
        startDate: '2020-10-24T14:00:00+00:00',
        endDate: '2020-10-24T14:37:14+00:00',
      }}
      regionsAllowed\={\['IT', 'NL'\]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `name` | The title of the video. |
| `description` | The description of the video. HTML tags are ignored. |
| `thumbnailUrl` | A URL pointing to the video thumbnail image file. |
| `uploadDate` | The date the video was first published, in ISO 8601 format. |

**Recommended properties**

| Property | Info |
| --- | --- |
| `contentUrl` | A URL pointing to the actual video media file, in one of the supported encoding formats. |
| `duration` | The duration of the video in ISO 8601 format |
| `embedUrl` | A URL pointing to a player for the specific video. |
| `expires` | If applicable, the date after which the video will no longer be available. |
| `interactionStatistic` | The number of times the video has been watched. |
| `publication` | If your video is happening live and you want to be eligible for the LIVE badge. |
| `regionsAllowed` | The regions where the video is allowed. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

### VideoGame

[](https://github.com/garmeeh/next-seo?screenshot=true#videogame)

import { VideoGameJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>VideoGame JSON-LD</h1\>
    <VideoGameJsonLd
      name\="Red Dead Redemption 2"
      translatorName\={\['Translator 1', 'Translator 2'\]}
      languageName\={\['English', 'Kurdish'\]}
      description\="Arthur Morgan and the Van der Linde gang are outlaws on the run. With federal agents and the best bounty hunters in the nation massing on their heels, the gang must rob, steal and fight their way across the rugged heartland of America in order to survive."
      processorRequirements\="4 GHz"
      memoryRequirements\="16 Gb"
      playMode\="SinglePlayer"
      applicationCategory\="Game"
      url\="https://example.com/rdr2-game"
      platformName\={\['PC game', 'PlayStation 4'\]}
      operatingSystemName\="windows"
      keywords\="outlaw, gang, federal agents"
      datePublished\="2019-02-05T08:00:00+08:00"
      image\="https://example.com/photos/1x1/photo.jpg"
      publisherName\="Vertical Games"
      producerName\="Rockstar Games"
      producerUrl\="https//www.example.com/producer"
      offers\={\[
        {
          price: '119.99',
          priceCurrency: 'USD',
          priceValidUntil: '2020-11-05',
          availability: 'https://schema.org/InStock',
          url: 'https://example.net/rdr2-game',
          seller: {
            name: 'Executive Gaming',
          },
        },
        {
          price: '139.99',
          priceCurrency: 'CAD',
          priceValidUntil: '2020-09-05',
          availability: 'https://schema.org/InStock',
          url: 'https://example.org/rdr2-game',
          seller: {
            name: 'Executive Gaming',
          },
        },
      \]}
      aggregateRating\={{
        ratingValue: '44',
        reviewCount: '89',
        ratingCount: '684',
        bestRating: '100',
        worstRating: '1',
      }}
      reviews\={\[
        {
          author: {
            type: 'Person',
            name: 'AhmetKaya',
          },
          publisher: {
            type: 'Organization',
            name: 'Gam Production',
          },
          datePublished: '2017-01-06T03:37:40Z',
          reviewBody: 'Iki gozum.',
          name: 'Rica ederim.',
          reviewRating: {
            bestRating: '5',
            ratingValue: '5',
            worstRating: '1',
          },
        },
      \]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `name` | The title of the video game. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

[More information about the schema](https://schema.org/VideoGame)

### Event

[](https://github.com/garmeeh/next-seo?screenshot=true#event)

import { EventJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Event JSON-LD</h1\>
    <EventJsonLd
      name\="My Event"
      startDate\="2020-01-23T00:00:00.000Z"
      endDate\="2020-01-24T00:00:00.000Z"
      location\={{
        name: 'My Place',
        sameAs: 'https://example.com/my-place',
        address: {
          streetAddress: '1600 Saratoga Ave',
          addressLocality: 'San Jose',
          addressRegion: 'CA',
          postalCode: '95129',
          addressCountry: 'US',
        },
      }}
      url\="https://example.com/my-event"
      images\={\['https://example.com/photos/photo.jpg'\]}
      description\="My event @ my place"
      offers\={\[
        {
          price: '119.99',
          priceCurrency: 'USD',
          priceValidUntil: '2020-11-05',
          itemCondition: 'https://schema.org/UsedCondition',
          availability: 'https://schema.org/InStock',
          url: 'https://www.example.com/executive-anvil',
          seller: {
            name: 'John Doe',
          },
          validFrom: '2020-11-01T00:00:00.000Z',
        },
        {
          price: '139.99',
          priceCurrency: 'CAD',
          priceValidUntil: '2020-09-05',
          itemCondition: 'https://schema.org/UsedCondition',
          availability: 'https://schema.org/InStock',
          url: 'https://www.example.ca/executive-anvil',
          seller: {
            name: 'John Doe Sr.',
          },
          validFrom: '2020-08-05T00:00:00.000Z',
        },
      \]}
      performers\={\[
        {
          name: 'Adele',
        },
        {
          name: 'Kira and Morrison',
        },
      \]}
      organizer\={{
        type: 'Organization',
        name: 'Unnamed organization',
        url: 'https://www.unnamed.com',
      }}
      eventStatus\="EventScheduled"
      eventAttendanceMode\="OfflineEventAttendanceMode"
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `name` | The name of the event |
| `startDate` | The start date time of the event in iso8601 format |
| `endDate` | The end date time of the event in iso8601 format |
| `location` | Location of the event, can be `Place` or `VirtualLocation` |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

**`Place` type** Requires `address` property and `name`.

**`VirtualLocation` type** Requires `url` property, doesn't require `name`.

**Supported properties**

| Property | Info |
| --- | --- |
| `description` | Description of the event |
| `location.name` | Name of the location |
| `location.sameAs` | URL of a reference web page that identifies location |
| `images` | An image or images of the event. |
| `url` | The fully-qualified URL of the event. |
| `offers` | An offer to transfer some rights to an item or to provide a service. You can provide this as a single object, or an array of objects with the properties below. |
| `performers` | All artists that perform at this event. You can provide this as a single object, or an array of objects with the properties below. |
| `performers.name` | The name of the performer |
| `performers.type` | Either `Person` or `PerformingGroup` |
| `organizer` | The organizer of the event |
| `organizer.type` | Either `Organization` or `Person` |
| `organizer.name` | Name of the organizer of the event |
| `organizer.url` | URL of the organizer of the event |
| `eventStatus` | Status of the event, type `EventStatus` |
| `eventAttendanceMode` | Attendance mode of the event, type `EventAttendanceMode` |

**`EventStatus` type**

*   'EventCancelled'
*   'EventMovedOnline'
*   'EventPostponed'
*   'EventRescheduled'
*   'EventScheduled'

**`EventAttendanceMode` type**

*   'MixedEventAttendanceMode'
*   'OfflineEventAttendanceMode'
*   'OnlineEventAttendanceMode'

**`offers` Required properties**

| Property | Info |
| --- | --- |
| `offers.price` | The cost of the offer |
| `offers.priceCurrency` | The currency of the offer |

**`offers` Recommended properties**

| Property | Info |
| --- | --- |
| `offers.priceValidUntil` | Until when the price of the offer expires |
| `offers.itemCondition` | The condition of the product or service |
| `offers.availability` | The availability of this item — for example In stock, Out of stock, Pre-order, etc. |
| `offers.url` | URL of the item |
| `offers.seller` | The person who is selling this item |
| `offers.seller.name` | The name of the person |
| `offers.validFrom` | Since when the price of the offer is valid |

The property `aggregateOffer` is also available: (It is ignored if `offers` is set)

**Required properties**

| Property | Info |
| --- | --- |
| `lowPrice` | The lowest price of all offers available. Use a floating point number. |
| `priceCurrency` | The currency used to describe the product price, in three-letter ISO 4217 format. |

**Recommended properties**

| Property | Info |
| --- | --- |
| `highPrice` | The highest price of all offers available. Use a floating point number. |
| `offerCount` | The number of offers for the product. |

For reference and more info check [Google's Search Event DataType](https://developers.google.com/search/docs/data-types/event)

### Q&A

[](https://github.com/garmeeh/next-seo?screenshot=true#qa)

Q&A pages are web pages that contain data in a question-and-answer format, which is one question followed by its answers.

import { QAPageJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Q&A Page JSON\-LD</h1\>
    <QAPageJsonLd
      mainEntity\={{
        name: 'How many ounces are there in a pound?',
        text: 'I have taken up a new interest in baking and keep running across directions in ounces and pounds. I have to translate between them and was wondering how many ounces are in a pound?',
        answerCount: 3,
        upvoteCount: 26,
        dateCreated: '2016-07-23T21:11Z',
        author: {
          name: 'New Baking User',
          url: 'https://example.com/bakinguser',
        },
        acceptedAnswer: {
          text: '1 pound (lb) is equal to 16 ounces (oz).',
          dateCreated: '2016-11-02T21:11Z',
          upvoteCount: 1337,
          url: 'https://example.com/question1#acceptedAnswer',
          author: {
            name: 'SomeUser',
            url: 'https://example.com/someuser',
          },
        },
        suggestedAnswer: \[
          {
            text: 'Are you looking for ounces or fluid ounces? If you are looking for fluid ounces there are 15.34 fluid ounces in a pound of water.',
            dateCreated: '2016-11-02T21:11Z',
            upvoteCount: 42,
            url: 'https://example.com/question1#suggestedAnswer1',
            author: {
              name: 'AnotherUser',
              url: 'https://example.com/anotheruser',
            },
          },
          {
            text: \`I can't remember exactly, but I think 18 ounces in a lb. You might want to double check that.\`,
            dateCreated: '2016-11-06T21:11Z',
            upvoteCount: 0,
            url: 'https://example.com/question1#suggestedAnswer2',
            author: {
              name: 'ConfusedUser',
              url: 'https://example.com/confuseduser',
            },
          },
        \],
      }}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `mainEntity` | The Question for this page must be nested under the mainEntity property of the QAPageJsonld component. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

**`mainEntity` Required properties**

| Property | Info |
| --- | --- |
| `answerCount` | The total number of answers to the question. |
| `acceptedAnswer` or `suggestedAnswer` | To be eligible for the rich result, a question must have at least one answer – either an acceptedAnswer or a suggestedAnswer. |
| `name` | The full text of the short form of the question. |

**`mainEntity` Supported properties**

| Property | Info |
| --- | --- |
| `author` | The author of the question. |
| `dateCreated` | The date at which the question was added to the page, in ISO-8601 format. |
| `text` | The full text of the long form of the question. |
| `upvoteCount` | The total number of votes that this question has received. |

**`acceptedAnswer`/`suggestedAnswer` Required properties**

| Property | Info |
| --- | --- |
| `text` | The full text of the answer. |

**`acceptedAnswer`/`suggestedAnswer` Supported properties**

| Property | Info |
| --- | --- |
| `author` | The author of the question. |
| `dateCreated` | The date at which the question was added to the page, in ISO-8601 format. |
| `upvoteCount` | The total number of votes that this question has received. |
| `url` | A URL that links directly to this answer. |

For reference and more info check [Google's Search Q&A DataType](https://developers.google.com/search/docs/data-types/qapage)

### Collection Page

[](https://github.com/garmeeh/next-seo?screenshot=true#collection-page)

Collection pages are web pages. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as breadcrumb may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an item scope, they will be assumed to be about the page.

import { CollectionPageJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Collection Page JSON-LD</h1\>
    <CollectionPageJsonLd
      name\="Resistance 3: Fall of Man"
      hasPart\={\[
        {
          about:
            'Britten Four Sea Interludes and Passacaglia from Peter Grimes',
          author: 'John Doe',
          name: 'Schema.org Ontology',
          datePublished: '2021-03-09',
          audience: 'Internet',
          keywords: 'schema',
          thumbnailUrl: 'https://i.ytimg.com/vi/eXSJ3PO9Tas/hqdefault.jpg',
          image: 'hqdefault.jpg',
        },
        {
          about: 'Shostakovich Symphony No. 7 (Leningrad)',
          author: 'John Smith',
          name: 'Creative work name',
          datePublished: '2014-10-01T19:30',
        },
      \]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `name` | The name of the item. |
| `hasPart` | Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense). |

**Supported properties**

| Property | Info |
| --- | --- |
| `hasPart.creativeWork` | The most generic kind of [creative work](https://schema.org/CreativeWork), including books, movies, photographs, software programs, etc |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

**`creativeWork` Required properties**

| Property | Info |
| --- | --- |
| `hasPart.creativeWork.author` | The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably. |
| `hasPart.creativeWork.about` | The subject matter of the content. |
| `hasPart.creativeWork.datePublished` | Date of first broadcast/publication. |
| `hasPart.creativeWork.name` | The name of the item. |

**`creativeWork` Supported properties**

| Property | Info |
| --- | --- |
| `hasPart.creativeWork.audience` | An intended audience, i.e. a group for whom something was created. |
| `hasPart.creativeWork.keywords` | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas. |
| `hasPart.creativeWork.thumbnailUrl` | A thumbnail image relevant to the Thing. |
| `hasPart.creativeWork.image` | An image of the item. This can be a URL or a fully described ImageObject. |

For reference and more info check [Collection Page DataType](https://schema.org/CollectionPage)

### Profile page

[](https://github.com/garmeeh/next-seo?screenshot=true#profile-page)

Profile pages are web pages. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as breadcrumb may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an item scope, they will be assumed to be about the page.

import { ProfilePageJsonLd } from 'next-seo';

const Page \= () \=\> (
  <\>
    <h1\>Profile page JSON-LD</h1\>
    <ProfilePageJsonLd
      lastReviewed\="2014-10-01T19:30"
      breadcrumb\={\[
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
      \]}
    /\>
  </\>
);

export default Page;

**Required properties**

| Property | Info |
| --- | --- |
| `breadcrumb` | A set of links that can help a user understand and navigate a website hierarchy represented as string or [BreadcrumbList](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb). |

**Supported properties**

| Property | Info |
| --- | --- |
| `lastReviewed` | Date on which the content on this web page was last reviewed for accuracy and/or completeness. |

**Other** | `useAppDir` | This should be set to true if using new app directory. Not required if outside of app directory. |

For reference and more info check [Profile Page DataType](https://schema.org/ProfilePage)

### Carousel

[](https://github.com/garmeeh/next-seo?screenshot=true#carousel)

**Required properties of Carousel Component**

| Property | Info |
| --- | --- |
| `type` | The type of carousel |
| `data` | The data in the form of an array for the item list in the carousel |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

#### Default (Summary List)

[](https://github.com/garmeeh/next-seo?screenshot=true#default-summary-list)

import React from 'react';
import { CarouselJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Carousel Default JSON-LD</h1\>
    <CarouselJsonLd
      ofType\="default"
      data\={\[
        { url: 'http://example.com/peanut-butter-cookies.html' },
        {
          url: 'http://example.com/triple-chocolate-chunk.html',
        },
      \]}
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `url` | URL of the item's detailed page. |

#### Course

[](https://github.com/garmeeh/next-seo?screenshot=true#course-1)

import React from 'react';
import { CarouselJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Carousel Course JSON-LD</h1\>
    <CarouselJsonLd
      ofType\="course"
      data\={\[
        {
          courseName: 'Course 1',
          description: 'Course 1 Description',
          providerName: 'Course Provider',
          url: 'http://example.com/course-1.html',
        },
        {
          courseName: 'Course 2',
          description: 'Course 2 Description',
          providerName: 'Course Provider',
          url: 'http://example.com/course-2.html',
        },
      \]}
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `courseName` | The title of the course. |
| `description` | A description of the course. Display limit of 60 characters. |
| `providerName` | The course provider name. |
| `url` | URL of the item's detailed page . |

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `providerUrl` | The url to the course provider. |

#### Movie

[](https://github.com/garmeeh/next-seo?screenshot=true#movie)

import React from 'react';
import { CarouselJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Carousel Movie JSON-LD</h1\>
    <CarouselJsonLd
      ofType\="movie"
      data\={\[
        {
          name: 'Movie 1',
          url: 'http://example.com/movie-1.html',
          image:
            'https://i.pinimg.com/originals/96/a0/0d/96a00d42b0ff8f80b7cdf2926a211e47.jpg',
          director: {
            name: 'John Doe',
          },
          review: {
            author: { type: 'Person', name: 'Ronan Farrow' },
            reviewBody:
              'Heartbreaking, inpsiring, moving. Bradley Cooper is a triple threat.',
            reviewRating: { ratingValue: '5' },
          },
        },
        {
          name: 'Movie 2',
          url: 'http://example.com/movie-1.html',
          image:
            'https://i.pinimg.com/originals/96/a0/0d/96a00d42b0ff8f80b7cdf2926a211e47.jpg',
          director: \[
            {
              name: 'Mary Doe',
            },
            {
              name: 'John Doe',
            },
          \],
          review: {
            author: { type: 'Person', name: 'Ronan Farrow' },
            reviewBody:
              'Heartbreaking, inpsiring, moving. Rowan Atkinson is a triple threat.',
            reviewRating: { ratingValue: '5' },
          },
        },
      \]}
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `name` | Name of the movie. |
| `image` | An image that represents the movie. |
| `url` | URL of the item's detailed page. |

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `director` | The directors of the movie. |
| `dateCreated` | The date the movie was released. |
| `aggregateRating` | Aggregate Rating object for the movie. |
| `review` | Review for the movie. |

#### Recipe

[](https://github.com/garmeeh/next-seo?screenshot=true#recipe-1)

import React from 'react';
import { CarouselJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Carousel Recipe JSON-LD</h1\>
    <CarouselJsonLd
      ofType\="recipe"
      data\={\[
        {
          name: 'Party Coffee Cake',
          url: 'http://example.com/recipe-1.html',
          images: \[
            'https://example.com/photos/1x1/photo.jpg',
            'https://example.com/photos/4x3/photo.jpg',
            'https://example.com/photos/16x9/photo.jpg',
          \],
          authorName: 'Mary Stone',
          datePublished: '2018-03-10',
          description: 'This coffee cake is awesome and perfect for parties.',
          prepTime: 'PT20M',
          cookTime: 'PT30M',
          totalTime: 'PT50M',
          keywords: 'cake for a party, coffee',
          yields: '10',
          category: 'Dessert',
          calories: 270,
          cuisine: 'American',
          ingredients: \[
            '2 cups of flour',
            '3/4 cup white sugar',
            '2 teaspoons baking powder',
            '1/2 teaspoon salt',
            '1/2 cup butter',
            '2 eggs',
            '3/4 cup milk',
          \],
          instructions: \[
            {
              name: 'Preheat',
              text: 'Preheat the oven to 350 degrees F. Grease and flour a 9x9 inch pan.',
              url: 'https://example.com/party-coffee-cake#step1',
              image: 'https://example.com/photos/party-coffee-cake/step1.jpg',
            },
            {
              name: 'Mix dry ingredients',
              text: 'In a large bowl, combine flour, sugar, baking powder, and salt.',
              url: 'https://example.com/party-coffee-cake#step2',
              image: 'https://example.com/photos/party-coffee-cake/step2.jpg',
            },
            {
              name: 'Spread into pan',
              text: 'Spread into the prepared pan.',
              url: 'https://example.com/party-coffee-cake#step4',
              image: 'https://example.com/photos/party-coffee-cake/step4.jpg',
            },
            {
              name: 'Bake',
              text: 'Bake for 30 to 35 minutes, or until firm.',
              url: 'https://example.com/party-coffee-cake#step5',
              image: 'https://example.com/photos/party-coffee-cake/step5.jpg',
            },
          \],
          aggregateRating: {
            ratingValue: '5',
            ratingCount: '18',
          },
          video: {
            name: 'How to make a Party Coffee Cake',
            description: 'This is how you make a Party Coffee Cake.',
            thumbnailUrls: \[
              'https://example.com/photos/1x1/photo.jpg',
              'https://example.com/photos/4x3/photo.jpg',
              'https://example.com/photos/16x9/photo.jpg',
            \],
            contentUrl: 'http://www.example.com/video123.mp4',
            embedUrl: 'http://www.example.com/videoplayer?video=123',
            uploadDate: '2018-02-05T08:00:00+08:00',
            duration: 'PT1M33S',
            expires: '2019-02-05T08:00:00+08:00',
          },
        },
        {
          name: 'Party Coffee Cake 2',
          url: 'http://example.com/recipe-2.html',
          images: \[
            'https://example.com/photos/1x1/photo.jpg',
            'https://example.com/photos/4x3/photo.jpg',
            'https://example.com/photos/16x9/photo.jpg',
          \],
          authorName: 'Mary Stone 2',
          datePublished: '2018-03-10',
          description: 'This coffee cake is awesome and perfect for parties.',
          prepTime: 'PT20M',
          cookTime: 'PT30M',
          totalTime: 'PT50M',
          keywords: 'cake for a party, coffee',
          yields: '10',
          category: 'Dessert',
          calories: 270,
          cuisine: 'American',
          ingredients: \[
            '2 cups of flour',
            '3/4 cup white sugar',
            '2 teaspoons baking powder',
            '1/2 teaspoon salt',
            '1/2 cup butter',
            '2 eggs',
            '3/4 cup milk',
          \],
          instructions: \[
            {
              name: 'Preheat',
              text: 'Preheat the oven to 350 degrees F. Grease and flour a 9x9 inch pan.',
              url: 'https://example.com/party-coffee-cake#step1',
              image: 'https://example.com/photos/party-coffee-cake/step1.jpg',
            },
            {
              name: 'Mix dry ingredients',
              text: 'In a large bowl, combine flour, sugar, baking powder, and salt.',
              url: 'https://example.com/party-coffee-cake#step2',
              image: 'https://example.com/photos/party-coffee-cake/step2.jpg',
            },
            {
              name: 'Spread into pan',
              text: 'Spread into the prepared pan.',
              url: 'https://example.com/party-coffee-cake#step4',
              image: 'https://example.com/photos/party-coffee-cake/step4.jpg',
            },
            {
              name: 'Bake',
              text: 'Bake for 30 to 35 minutes, or until firm.',
              url: 'https://example.com/party-coffee-cake#step5',
              image: 'https://example.com/photos/party-coffee-cake/step5.jpg',
            },
          \],
          aggregateRating: {
            ratingValue: '5',
            ratingCount: '18',
          },
          video: {
            name: 'How to make a Party Coffee Cake',
            description: 'This is how you make a Party Coffee Cake.',
            thumbnailUrls: \[
              'https://example.com/photos/1x1/photo.jpg',
              'https://example.com/photos/4x3/photo.jpg',
              'https://example.com/photos/16x9/photo.jpg',
            \],
            contentUrl: 'http://www.example.com/video123.mp4',
            embedUrl: 'http://www.example.com/videoplayer?video=123',
            uploadDate: '2018-02-05T08:00:00+08:00',
            duration: 'PT1M33S',
            expires: '2019-02-05T08:00:00+08:00',
          },
        },
      \]}
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `name` | The name of the dish. |
| `description` | A description of the recipe |
| `authorName` | The name of the recipe author |
| `ingredients` | A list of ingredient strings |
| `instructions` | \- |
| `instructions.name` | The name of the instruction step. |
| `instructions.text` | The directions of the instruction step. |
| `url` | URL of the item's detailed page. |

#### Custom

[](https://github.com/garmeeh/next-seo?screenshot=true#custom)

import React from 'react';
import { CarouselJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Carousel Custom JSON-LD</h1\>
    <CarouselJsonLd
      ofType\="custom"
      url\="http://example.com/custom-carousel.html"
      name\="Carousel Custom"
      description\="Custom Carousel Description"
      data\={\[
        {
          position: 1,
          type: 'CustomList',
          name: 'Custom 1',
        },
        {
          position: 2,
          type: 'CustomList',
          name: 'Custom 2',
        },
      \]}
    /\>
  </\>
);

**Data Required Properties**

| Property | Info |
| --- | --- |
| `type` | Type of the item. |
| `name` | Name of the item. |

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `position` | Position of the item. If not pass property, it will increase regularly. |

### Software App

[](https://github.com/garmeeh/next-seo?screenshot=true#software-app)

import React from 'react';
import { SoftwareAppJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Software App JSON-LD</h1\>
    <SoftwareAppJsonLd
      name\="Angry Birds"
      price\="1.00"
      priceCurrency\="USD"
      aggregateRating\={{ ratingValue: '4.6', reviewCount: '8864' }}
      operatingSystem\="ANDROID"
      applicationCategory\="GameApplication"
      keywords\="angrybirds, arcade, slingshot"
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `name` | The name of the app. |
| `price` | Price of the app. If the app is free of charge, set offers.price to 0 |
| `priceCurrency` | If the app has a price greater than 0, you must include offers.currency. |
| `aggregateRating` | The average review score of the app. (Not required if review is present.) |
| `review` | A single review of the app. (Not required if aggregateRating is present.) |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `operatingSystem` | The operating System supported by the game it self. |
| `applicationCategory` | Desktop Software or Video Game... |

**Data other properties**

| Property | Info |
| --- | --- |
| `keywords` | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas. |

For reference and more info check [Google docs for Software App](https://developers.google.com/search/docs/data-types/software-app) and [Schema.org docs](https://schema.org/SoftwareApplication)

### Organization

[](https://github.com/garmeeh/next-seo?screenshot=true#organization)

import React from 'react';
import { OrganizationJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Organization JSON-LD</h1\>
    <OrganizationJsonLd
      type\="Corporation"
      id\="https://www.purpule-fox.io/#corporation"
      logo\="https://www.example.com/photos/logo.jpg"
      legalName\="Purple Fox LLC"
      name\="Purple Fox"
      address\={{
        streetAddress: '1600 Saratoga Ave',
        addressLocality: 'San Jose',
        addressRegion: 'CA',
        postalCode: '95129',
        addressCountry: 'US',
      }}
      contactPoint\={\[
        {
          telephone: '+1-401-555-1212',
          contactType: 'customer service',
          email: 'customerservice@email.com',
          areaServed: 'US',
          availableLanguage: \['English', 'Spanish', 'French'\],
        },
        {
          telephone: '+1-877-746-0909',
          contactType: 'customer service',
          email: 'servicecustomer@email.com',
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
      sameAs\={\['https://www.orange-fox.com'\]}
      url\="https://www.purpule-fox.io/"
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `name` | The name of the Organization. |
| `url` | Url of the organization |
| `contactPoint` |  |
| `contactPoint.telephone` | An internationalized version of the phone number, starting with the "+" symbol and country code |
| `contactPoint.contactType` | Description of the purpose of the phone number i.e. `Technical Support`. |

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `logo` | ImageObject or URL an associated logo to the Organization. |
| `type` | Organization type, check [here](https://schema.org/Organization#subtypes) |
| `legalName` | The official name of the organization, e.g. the registered company name. |
| `sameAs` | URL of a reference Web page that unambiguously indicates the item's identity. |
| `address` | Address of the specific business location |
| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |
| `address.addressLocality` | City |
| `address.addressRegion` | State or province, if applicable. |
| `address.postalCode` | Postal or zip code. |
| `address.streetAddress` | Street number, street name, and unit number. |
| `contactPoint.areaServed` | `String` or `Array` of geographical regions served by the business. Example `"US"` or `["US", "CA", "MX"]` |
| `contactPoint.availableLanguage` | Details about the language spoken. Example `"English"` or `["English", "French"]` |
| `contactPoint.email` | Email asscosiated with the business\` |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

For reference and more info check [Docs](https://schema.org/Organization)

### Brand

[](https://github.com/garmeeh/next-seo?screenshot=true#brand)

import React from 'react';
import { BrandJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>Brand JSON-LD</h1\>
    <BrandJsonLd
      slogan\="What does the fox say?"
      id\="https://www.purpule-fox.io/#corporation"
      logo\="https://www.example.com/photos/logo.jpg"
      aggregateRating\={{
        ratingValue: '5',
        ratingCount: '18',
      }}
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `id` | 'URL to main entity of page' |

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `logo` | ImageObject or URL an associated logo to the Organization. |
| `slogan` | A slogan or motto associated with the item. |
| `aggregateRating.ratingValue` | The rating for the content.(Check the [reference](https://schema.org/ratingValue) |
| `aggregateRating.ratingCount` | The count of total number of ratings. |
| `aggregateRating.reviewCount` | The count of total number of reviews. |
| `aggregateRating.bestRating` | The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed. |
| `aggregateRating.worstRating` | The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

For reference and more info check [Docs](https://schema.org/Brand)

### WebPage

[](https://github.com/garmeeh/next-seo?screenshot=true#webpage)

import React from 'react';
import { WebPageJsonLd } from 'next-seo';

export default () \=\> (
  <\>
    <h1\>WebPage JSON-LD</h1\>
    <WebPageJsonLd
      description\="What does the fox say?"
      id\="https://www.purpule-fox.io/#corporation"
      lastReviewed\="2021-05-26T05:59:02.085Z"
      reviewedBy\={{
        type: 'Person',
        name: 'Garmeeh',
      }}
    /\>
  </\>
);

**Data required properties**

| Property | Info |
| --- | --- |
| `id` | 'URL to main entity of page' |

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `description` | ImageObject or URL an associated logo to the Organization. |
| `lastReviewed` | Date on which the content on this web page was last reviewed for accuracy and/or completeness. |
| `reviewedBy.type` | People or organizations that will review the content of the web page. |
| `reviewedBy.name` | Name of the entity that have reviewed the content on this web page for accuracy and/or completeness. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

For reference and more info check [Docs](https://schema.org/WebPage)

### Image Metadata

[](https://github.com/garmeeh/next-seo?screenshot=true#image-metadata)

import React from 'react';
import { ImageJsonLd } from 'next-seo';

function Image() {
  return (
    <\>
      <h1\>Image</h1\>
      <ImageJsonLd
        images\={\[
          {
            contentUrl: 'http://www.example.com/images/image.png',
            creator: {
              '@type': 'Person',
              name: 'Jane Doe',
            },
            creditText: 'Jane Doe',
            copyrightNotice: '© Jane Doe',
            license: 'http://www.example.com/license',
            acquireLicensePage: 'http://www.example.com/acquire-license',
          },
        \]}
      /\>
    </\>
  );
}

export default Image;

**Data Recommended properties**

| Property | Info |
| --- | --- |
| `contentUrl` | A URL to the actual image content. Google uses contentUrl to determine which image the photo metadata applies to. |
| `creator.name` | The name of the creator. |
| `creditText` | The name of person and/or organization that is credited for the image when it's published. |
| `copyrightNotice` | The copyright notice for claiming the intellectual property for this photograph. This identifies the current owner of the copyright for the photograph. |
| `license` | A URL to a page that describes the license governing an image's use. For example, it could be the terms and conditions that you have on your website. |
| `acquireLicensePage` | A URL to a page where the user can find information on how to license that image. |

**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |

For reference and more info check [Google Docs](https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata)

Contributors
------------

[](https://github.com/garmeeh/next-seo?screenshot=true#contributors)

[Contributing Guide](https://github.com/garmeeh/next-seo/blob/master/CONTRIBUTING.md)

A massive thank you to [everyone who contributes](https://github.com/garmeeh/next-seo/graphs/contributors) to this project 👏

## Metadata

```json
{
  "title": "GitHub - garmeeh/next-seo: Next SEO is a plug in that makes managing your SEO easier in Next.js projects.",
  "description": "Next SEO is a plug in that makes managing your SEO easier in Next.js projects. - garmeeh/next-seo",
  "url": "https://github.com/garmeeh/next-seo?screenshot=true",
  "content": "**Have you seen the new Next.js newsletter?**\n\n[![Image 32: NextjsWeekly banner](https://github.com/garmeeh/next-seo/raw/master/next-js-weekly.png)](https://dub.sh/nextjsweekly)\n\n**Useful Tools**\n\n*   [dub](https://dub.co/?utm_source=next-seo&utm_medium=social&utm_campaign=next-seo) recently launched a useful Free UTM builder! You can use it [here](https://dub.sh/iKTxs7b)\n\nNext SEO\n--------\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#next-seo)\n\n[![Image 33: npm](https://camo.githubusercontent.com/591dbb2ff6c6af1add2b4668f741ad390e60b5483b5d7caa6aeb387abec57251/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f6e6578742d73656f3f7374796c653d666c61742d737175617265)](https://camo.githubusercontent.com/591dbb2ff6c6af1add2b4668f741ad390e60b5483b5d7caa6aeb387abec57251/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f6e6578742d73656f3f7374796c653d666c61742d737175617265)\n\nNext SEO is a plugin that makes managing your SEO easier in Next.js projects.\n\nPull requests are very welcome. Also make sure to check out the issues for feature requests if you are looking for inspiration on what to add.\n\n**Feel like supporting this free plugin?**\n\nIt takes a lot of time to maintain an open source project so any small contribution is greatly appreciated.\n\nCoffee fuels coding ☕️\n\n[![Image 34: Buy Me A Coffee](https://camo.githubusercontent.com/7b8f7343bfc6e3c65c7901846637b603fd812f1a5f768d8b0572558bde859eb9/68747470733a2f2f63646e2e6275796d6561636f666665652e636f6d2f627574746f6e732f76322f64656661756c742d79656c6c6f772e706e67)](https://www.buymeacoffee.com/garmeeh)\n\n[next-seo.wallet](https://unstoppabledomains.com/d/next-seo.wallet) (ERC20 & SOL)\n\n**Note on app directory**\n\nThis note is only relevant if using the `app` directory.\n\nFor standard meta data (e.g., , <title\\>) then it is highly recommended that you use the built-in `generateMetaData` method. You can check out the docs [here](https://beta.nextjs.org/docs/guides/seo#usage)\n\nFor JSON-LD then, the only change needed is to add `useAppDir={true}` to the JSON-LD component in use. You should add use this component in your `page.js` and NOT your `head.js`.\n\n```\n<ArticleJsonLd\n  useAppDir={true}\n  url=\"https://example.com/article\"\n  title=\"Article headline\" <- required for app directory\n  />\n```\n\nIf you are using **`pages`** directory then `NextSeo` is **exactly what you need** for your SEO needs!\n\n### Table of Contents\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#table-of-contents)\n\n*   [Usage](https://github.com/garmeeh/next-seo?screenshot=true#usage)\n    *   [Setup](https://github.com/garmeeh/next-seo?screenshot=true#setup)\n    *   [Add SEO to Page](https://github.com/garmeeh/next-seo?screenshot=true#add-seo-to-page)\n    *   [Default SEO Configuration](https://github.com/garmeeh/next-seo?screenshot=true#default-seo-configuration)\n    *   [NextSeo Options](https://github.com/garmeeh/next-seo?screenshot=true#nextseo-options)\n        *   [Title Template](https://github.com/garmeeh/next-seo?screenshot=true#title-template)\n        *   [Default Title](https://github.com/garmeeh/next-seo?screenshot=true#default-title)\n        *   [No Index](https://github.com/garmeeh/next-seo?screenshot=true#no-index)\n        *   [dangerouslySetAllPagesToNoIndex](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonoindex)\n        *   [No Follow](https://github.com/garmeeh/next-seo?screenshot=true#no-follow)\n        *   [dangerouslySetAllPagesToNoFollow](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonofollow)\n        *   [robotsProps](https://github.com/garmeeh/next-seo?screenshot=true#robotsprops)\n        *   [Twitter](https://github.com/garmeeh/next-seo?screenshot=true#twitter)\n        *   [Facebook](https://github.com/garmeeh/next-seo?screenshot=true#facebook)\n        *   [Canonical URL](https://github.com/garmeeh/next-seo?screenshot=true#canonical-url)\n        *   [Alternate](https://github.com/garmeeh/next-seo?screenshot=true#alternate)\n        *   [Additional Meta Tags](https://github.com/garmeeh/next-seo?screenshot=true#additional-meta-tags)\n        *   [Additional Link Tags](https://github.com/garmeeh/next-seo?screenshot=true#additional-link-tags)\n*   [Open Graph](https://github.com/garmeeh/next-seo?screenshot=true#open-graph)\n    *   [Open Graph Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples)\n        *   [Basic](https://github.com/garmeeh/next-seo?screenshot=true#basic)\n        *   [Video](https://github.com/garmeeh/next-seo?screenshot=true#video)\n        *   [Audio](https://github.com/garmeeh/next-seo?screenshot=true#audio)\n        *   [Article](https://github.com/garmeeh/next-seo?screenshot=true#article)\n        *   [Book](https://github.com/garmeeh/next-seo?screenshot=true#book)\n        *   [Profile](https://github.com/garmeeh/next-seo?screenshot=true#profile)\n*   [JSON-LD](https://github.com/garmeeh/next-seo?screenshot=true#json-ld)\n    *   [JSON-LD Security](https://github.com/garmeeh/next-seo?screenshot=true#json-ld-security)\n    *   [Handling multiple instances](https://github.com/garmeeh/next-seo?screenshot=true#handling-multiple-instances)\n    *   [Article](https://github.com/garmeeh/next-seo?screenshot=true#article-1)\n    *   [Breadcrumb](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb)\n    *   [Blog](https://github.com/garmeeh/next-seo?screenshot=true#blog)\n    *   [Campground](https://github.com/garmeeh/next-seo?screenshot=true#campground)\n    *   [Recipe](https://github.com/garmeeh/next-seo?screenshot=true#recipe)\n    *   [Sitelinks Search Box](https://github.com/garmeeh/next-seo?screenshot=true#sitelinks-search-box)\n    *   [Course](https://github.com/garmeeh/next-seo?screenshot=true#course)\n    *   [Dataset](https://github.com/garmeeh/next-seo?screenshot=true#dataset)\n    *   [Corporate Contact](https://github.com/garmeeh/next-seo?screenshot=true#corporate-contact)\n    *   [FAQ Page](https://github.com/garmeeh/next-seo?screenshot=true#faq-page)\n    *   [How-to](https://github.com/garmeeh/next-seo?screenshot=true#how-to)\n    *   [Job Posting](https://github.com/garmeeh/next-seo?screenshot=true#job-posting)\n    *   [Local Business](https://github.com/garmeeh/next-seo?screenshot=true#local-business)\n    *   [Logo](https://github.com/garmeeh/next-seo?screenshot=true#logo)\n    *   [Product](https://github.com/garmeeh/next-seo?screenshot=true#product)\n    *   [Social Profile](https://github.com/garmeeh/next-seo?screenshot=true#social-profile)\n    *   [News Article](https://github.com/garmeeh/next-seo?screenshot=true#news-article)\n    *   [Park](https://github.com/garmeeh/next-seo?screenshot=true#park)\n    *   [Video](https://github.com/garmeeh/next-seo?screenshot=true#video-1)\n    *   [VideoGame](https://github.com/garmeeh/next-seo?screenshot=true#videogame)\n    *   [Event](https://github.com/garmeeh/next-seo?screenshot=true#event)\n    *   [Q&A](https://github.com/garmeeh/next-seo?screenshot=true#qa)\n    *   [Collection Page](https://github.com/garmeeh/next-seo?screenshot=true#collection-page)\n    *   [Profile page](https://github.com/garmeeh/next-seo?screenshot=true#profile-page)\n    *   [Carousel](https://github.com/garmeeh/next-seo?screenshot=true#carousel)\n        *   [Default (Summary List)](https://github.com/garmeeh/next-seo?screenshot=true#default-summary-list)\n        *   [Course](https://github.com/garmeeh/next-seo?screenshot=true#course-1)\n        *   [Movie](https://github.com/garmeeh/next-seo?screenshot=true#movie)\n        *   [Recipe](https://github.com/garmeeh/next-seo?screenshot=true#recipe-1)\n        *   [Custom](https://github.com/garmeeh/next-seo?screenshot=true#custom)\n    *   [Software App](https://github.com/garmeeh/next-seo?screenshot=true#software-app)\n    *   [Organization](https://github.com/garmeeh/next-seo?screenshot=true#organization)\n    *   [Brand](https://github.com/garmeeh/next-seo?screenshot=true#brand)\n    *   [WebPage](https://github.com/garmeeh/next-seo?screenshot=true#webpage)\n    *   [Image Metadata](https://github.com/garmeeh/next-seo?screenshot=true#image-metadata)\n*   [Contributors](https://github.com/garmeeh/next-seo?screenshot=true#contributors)\n\nUsage\n-----\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#usage)\n\n`NextSeo` works by including it on pages where you would like SEO attributes to be added. Once included on the page, you pass it a configuration object with the page's SEO properties. This can be dynamically generated at a page level, or in some cases, your API may return an SEO object.\n\n### Setup\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#setup)\n\nFirst, install it:\n\nor\n\n### Add SEO to Page\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#add-seo-to-page)\n\n* * *\n\n**Using Next.js app directory introduced in Next.js 13?**\n\nIf you are using the Next.js app directory, then it is highly recommended that you use the built-in `generateMetaData` method. You can check out the docs [here](https://beta.nextjs.org/docs/guides/seo#usage)\n\nIf you are using the `pages` directory, then `NextSeo` is exactly what you need for your SEO needs!\n\n* * *\n\nThen, you need to import `NextSeo` and add the desired properties. This will render out the tags in the `<head>` for SEO. At a bare minimum, you should add a title and description.\n\n**Example with just title and description:**\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      title\\=\"Simple Usage Example\"\n      description\\=\"A short description goes here.\"\n    /\\>\n    <p\\>Simple Usage</p\\>\n  </\\>\n);\n\nexport default Page;\n\nBut `NextSeo` gives you many more options that you can add. See below for a typical example of a page.\n\n**Typical page example:**\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      title\\=\"Using More of Config\"\n      description\\=\"This example uses more of the available config options.\"\n      canonical\\=\"https://www.canonical.ie/\"\n      openGraph\\={{\n        url: 'https://www.url.ie/a',\n        title: 'Open Graph Title',\n        description: 'Open Graph Description',\n        images: \\[\n          {\n            url: 'https://www.example.ie/og-image-01.jpg',\n            width: 800,\n            height: 600,\n            alt: 'Og Image Alt',\n            type: 'image/jpeg',\n          },\n          {\n            url: 'https://www.example.ie/og-image-02.jpg',\n            width: 900,\n            height: 800,\n            alt: 'Og Image Alt Second',\n            type: 'image/jpeg',\n          },\n          { url: 'https://www.example.ie/og-image-03.jpg' },\n          { url: 'https://www.example.ie/og-image-04.jpg' },\n        \\],\n        siteName: 'SiteName',\n      }}\n      twitter\\={{\n        handle: '@handle',\n        site: '@site',\n        cardType: 'summary\\_large\\_image',\n      }}\n    /\\>\n    <p\\>SEO Added to Page</p\\>\n  </\\>\n);\n\nexport default Page;\n\n**A note on Twitter Tags**\n\nProps `cardType`, `site`, `handle` are equivalent to `twitter:card`, `twitter:site`, `twitter:creator`. Documentation can be found [here](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary).\n\nTwitter will read the `og:title`, `og:image` and `og:description` tags for their card. `next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` to avoid duplication.\n\nSome tools may report this as an error. See [Issue #14](https://github.com/garmeeh/next-seo/issues/14)\n\n### Default SEO Configuration\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#default-seo-configuration)\n\n`NextSeo` enables you to set some default SEO properties that will appear on all pages without needing to include anything on them. You can also override these on a page-by-page basis if needed.\n\nTo achieve this, you will need to create a custom `<App>`. In your pages directory, create a new file, `_app.js`. See the Next.js docs [here](https://nextjs.org/docs/advanced-features/custom-app) for more info on a custom `<App>`.\n\nWithin this file you will need to import `DefaultSeo` from `next-seo` and pass it props.\n\nHere is a typical example:\n\nimport App, { Container } from 'next/app';\nimport { DefaultSeo } from 'next-seo';\n\n// import your default seo configuration\nimport SEO from '../next-seo.config';\n\nexport default class MyApp extends App {\n  render() {\n    const { Component, pageProps } \\= this.props;\n    return (\n      <Container\\>\n        <DefaultSeo\n          openGraph\\={{\n            type: 'website',\n            locale: 'en\\_IE',\n            url: 'https://www.url.ie/',\n            siteName: 'SiteName',\n          }}\n          twitter\\={{\n            handle: '@handle',\n            site: '@site',\n            cardType: 'summary\\_large\\_image',\n          }}\n        /\\>\n        <Component {...pageProps} /\\>\n      </Container\\>\n    );\n  }\n}\n\nTo work properly, `DefaultSeo` should be placed above (before) `Component` due to the behavior of Next.js internals.\n\nAlternatively, you can also create a config file to store default values such as `next-seo.config.js`\n\nexport default {\n  openGraph: {\n    type: 'website',\n    locale: 'en\\_IE',\n    url: 'https://www.url.ie/',\n    siteName: 'SiteName',\n  },\n  twitter: {\n    handle: '@handle',\n    site: '@site',\n    cardType: 'summary\\_large\\_image',\n  },\n};\n\nor like this, if you are using TypeScript\n\nimport { DefaultSeoProps } from 'next-seo';\n\nconst config: DefaultSeoProps \\= {\n  openGraph: {\n    type: 'website',\n    locale: 'en\\_IE',\n    url: 'https://www.url.ie/',\n    siteName: 'SiteName',\n  },\n  twitter: {\n    handle: '@handle',\n    site: '@site',\n    cardType: 'summary\\_large\\_image',\n  },\n};\n\nexport default config;\n\nimport at the top of `_app.js`\n\nimport SEO from '../next-seo.config';\n\nand the `DefaultSeo` component can be used like this instead\n\nFrom now on, all of your pages will have the defaults above applied.\n\n**Note that `Container` is deprecated in Next.js v9.0.4 so you should replace that component here with `React.Fragment` on this version and later - see [here](https://github.com/zeit/next.js/blob/master/errors/app-container-deprecated.md)**\n\n### NextSeo Options\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#nextseo-options)\n\n| Property | Type | Description |\n| --- | --- | --- |\n| `titleTemplate` | string | Allows you to set default title template that will be added to your title [More Info](https://github.com/garmeeh/next-seo?screenshot=true#title-template) |\n| `title` | string | Set the meta title of the page |\n| `defaultTitle` | string | If no title is set on a page, this string will be used instead of an empty `titleTemplate` [More Info](https://github.com/garmeeh/next-seo?screenshot=true#default-title) |\n| `noindex` | boolean (default false) | Sets whether page should be indexed or not [More Info](https://github.com/garmeeh/next-seo?screenshot=true#no-index) |\n| `nofollow` | boolean (default false) | Sets whether page should be followed or not [More Info](https://github.com/garmeeh/next-seo?screenshot=true#no-follow) |\n| `robotsProps` | Object | Set the more meta information for the `X-Robots-Tag` [More Info](https://github.com/garmeeh/next-seo?screenshot=true#robotsprops) |\n| `description` | string | Set the page meta description |\n| `canonical` | string | Set the page canonical url |\n| `mobileAlternate.media` | string | Set what screen size the mobile website should be served from |\n| `mobileAlternate.href` | string | Set the mobile page alternate url |\n| `languageAlternates` | array | Set the language of the alternate urls. Expects array of objects with the shape: `{ hrefLang: string, href: string }` |\n| `themeColor` | string | Indicates a suggested color that user agents should use to customize the display of the page or of the surrounding user interface. Must contain a valid CSS color |\n| `additionalMetaTags` | array | Allows you to add a meta tag that is not documented here. [More Info](https://github.com/garmeeh/next-seo?screenshot=true#additional-meta-tags) |\n| `additionalLinkTags` | array | Allows you to add a link tag that is not documented here. [More Info](https://github.com/garmeeh/next-seo?screenshot=true#additional-link-tags) |\n| `twitter.cardType` | string | The card type, which will be one of `summary`, `summary_large_image`, `app`, or `player` |\n| `twitter.site` | string | @username for the website used in the card footer |\n| `twitter.handle` | string | @username for the content creator / author (outputs as `twitter:creator`) |\n| `facebook.appId` | string | Used for Facebook Insights, you must add a facebook app ID to your page to for it [More Info](https://github.com/garmeeh/next-seo?screenshot=true#facebook) |\n| `openGraph.url` | string | The canonical URL of your object that will be used as its permanent ID in the graph |\n| `openGraph.type` | string | The type of your object. Depending on the type you specify, other properties may also be required [More Info](https://github.com/garmeeh/next-seo?screenshot=true#open-graph) |\n| `openGraph.title` | string | The open graph title, this can be different than your meta title. |\n| `openGraph.description` | string | The open graph description, this can be different than your meta description. |\n| `openGraph.images` | array | An array of images (object) to be used by social media platforms, slack etc as a preview. If multiple supplied you can choose one when sharing. [See Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples) |\n| `openGraph.videos` | array | An array of videos (object) |\n| `openGraph.locale` | string | The locale the open graph tags are marked up in. Of the format language\\_TERRITORY. Default is en\\_US. |\n| `openGraph.siteName` | string | If your object is part of a larger web site, the name which should be displayed for the overall site. |\n| `openGraph.profile.firstName` | string | Person's first name. |\n| `openGraph.profile.lastName` | string | Person's last name. |\n| `openGraph.profile.username` | string | Person's username. |\n| `openGraph.profile.gender` | string | Person's gender. |\n| `openGraph.book.authors` | string\\[\\] | Writers of the article. [See Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples) |\n| `openGraph.book.isbn` | string | The [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) |\n| `openGraph.book.releaseDate` | datetime | The date the book was released. |\n| `openGraph.book.tags` | string\\[\\] | Tag words associated with this book. |\n| `openGraph.article.publishedTime` | datetime | When the article was first published. [See Examples](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples) |\n| `openGraph.article.modifiedTime` | datetime | When the article was last changed. |\n| `openGraph.article.expirationTime` | datetime | When the article is out of date after. |\n| `openGraph.article.authors` | string\\[\\] | Writers of the article. |\n| `openGraph.article.section` | string | A high-level section name. E.g. Technology |\n| `openGraph.article.tags` | string\\[\\] | Tag words associated with this article. |\n\n#### Title Template\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#title-template)\n\nReplaces `%s` with your title string\n\ntitle \\= 'This is my title';\ntitleTemplate \\= 'Next SEO | %s';\n// outputs: Next SEO | This is my title\n\ntitle \\= 'This is my title';\ntitleTemplate \\= '%s | Next SEO';\n// outputs: This is my title | Next SEO\n\n#### Default Title\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#default-title)\n\ntitle \\= undefined;\ntitleTemplate \\= 'Next SEO | %s';\ndefaultTitle \\= 'Next SEO';\n// outputs: Next SEO\n\n#### No Index\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#no-index)\n\nSetting this to `true` will set `noindex,follow` (to set `nofollow`, please refer to [`nofollow`](https://github.com/garmeeh/next-seo?screenshot=true#no-follow)). This works on a page by page basis. This property works in tandem with the `nofollow` property and together they populate the `robots` meta tag.\n\n**Note:** The `noindex` and the [`nofollow`](https://github.com/garmeeh/next-seo?screenshot=true#no-follow) properties are a little different than all the others in the sense that setting them as a default does not work as expected. This is due to the fact Next SEO already has a default of `index,follow` because `next-seo` is a SEO plugin after all. So if you want to globally these properties, please see [dangerouslySetAllPagesToNoIndex](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).\n\n**Example No Index on a single page:**\n\nIf you have a single page that you want no indexed you can achieve this by:\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo noindex\\={true} /\\>\n    <p\\>This page is no indexed</p\\>\n  </\\>\n);\n\nexport default Page;\n\n/\\*\n<meta name=\"robots\" content=\"noindex,follow\"\\>\n\\*/\n\n#### dangerouslySetAllPagesToNoIndex\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonoindex)\n\nIt has the prefix `dangerously` because it will `noindex` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this. Just please be sure you want to `noindex` **EVERY** page. You can still override this at a page level if you have a use case to `index` a page. This can be done by setting `noindex: false`.\n\nThe only way to unset this is by removing the prop from the `DefaultSeo` in your custom `<App>`.\n\n#### No Follow\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#no-follow)\n\nSetting this to `true` will set `index,nofollow` (to set `noindex`, please refer to [`noindex`](https://github.com/garmeeh/next-seo?screenshot=true#no-index)). This works on a page-by-page basis. This property works in tandem with the `noindex` property, and together, they populate the `robots` meta tag.\n\n**Note:** Unlike for the other properties, setting `noindex` and `nofollow` by default does not work as expected. This is because Next SEO has a default of `index,follow`, since `next-seo` is an SEO plugin after all. If you want to globally allow these properties, see [dangerouslySetAllPagesToNoIndex](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoIndex) and [dangerouslySetAllPagesToNoFollow](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslySetAllPagesToNoFollow).\n\n**Example No Follow on a single page:**\n\nIf you have a single page that you want no indexed you can achieve this by:\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo nofollow\\={true} /\\>\n    <p\\>This page is not followed</p\\>\n  </\\>\n);\n\nexport default Page;\n\n/\\*\n<meta name=\"robots\" content=\"index,nofollow\"\\>\n\\*/\n\n#### dangerouslySetAllPagesToNoFollow\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#dangerouslysetallpagestonofollow)\n\nIt has the prefix of `dangerously` because it will `nofollow` all pages. As this is an SEO plugin, that is kinda dangerous action. It is **not** bad to use this. Just please be sure you want to `nofollow` **EVERY** page. You can still override this at a page level if you have a use case to `follow` a page. This can be done by setting `nofollow: false`.\n\nThe only way to unset this, is by removing the prop from the `DefaultSeo` in your custom `<App>`.\n\n| `noindex` | `nofollow` | `meta` content of `robots` |\n| --- | --- | --- |\n| \\-- | \\-- | `index,follow` (default) |\n| false | false | `index,follow` |\n| true | \\-- | `noindex,follow` |\n| true | false | `noindex,follow` |\n| \\-- | true | `index,nofollow` |\n| false | true | `index,nofollow` |\n| true | true | `noindex,nofollow` |\n\n#### robotsProps\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#robotsprops)\n\nIn addition to `index, follow` the `robots` meta tag accepts more properties to archive a more accurate crawling and serve better snippets for SEO bots that crawl your page.\n\nExample:\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      robotsProps\\={{\n        nosnippet: true,\n        notranslate: true,\n        noimageindex: true,\n        noarchive: true,\n        maxSnippet: \\-1,\n        maxImagePreview: 'none',\n        maxVideoPreview: \\-1,\n      }}\n    /\\>\n    <p\\>Additional robots props in Next-SEO!!</p\\>\n  </\\>\n);\n\nexport default Page;\n\n/\\*\n<meta name=\"robots\" content=\"index,follow,nosnippet,max-snippet:-1,max-image-preview:none,noarchive,noimageindex,max-video-preview:-1,notranslate\"\\>\n\\*/\n\n**Available properties**\n\n| Property | Type | Description |\n| --- | --- | --- |\n| `noarchive` | boolean | Do not show a [cached link](https://support.google.com/websearch/answer/1687222) in search results. |\n| `nosnippet` | boolean | Do not show a text snippet or video preview in the search results for this page. |\n| `max-snippet` | number | Use a maximum of \\[number\\] characters as a textual snippet for this search result. [Read more](https://developers.google.com/search/reference/robots_meta_tag?hl=en-GB#directives) |\n| `max-image-preview` | 'none','standard','large' | Set the maximum size of an image preview for this page in a search results. |\n| `max-video-preview` | number | Use a maximum of \\[number\\] seconds as a video snippet for videos on this page in search results. [Read more](https://developers.google.com/search/reference/robots_meta_tag?hl=en-GB#directives) |\n| `notranslate` | boolean | Do not offer translation of this page in search results. |\n| `noimageindex` | boolean | Do not index images on this page. |\n| `unavailable_after` | string | Do not show this page in search results after the specified date/time. The date/time must be specified in a widely adopted format including, but not limited to RFC 822, RFC 850, and ISO 8601. |\n\nFor more reference about the `X-Robots-Tag` visit [Google Search Central - Control Crawling and Indexing](https://developers.google.com/search/reference/robots_meta_tag?hl=en-GB#directives)\n\n#### Twitter\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#twitter)\n\nTwitter will read the `og:title`, `og:image` and `og:description` tags for their card, this is why `next-seo` omits `twitter:title`, `twitter:image` and `twitter:description` so not to duplicate.\n\nSome tools may report this as an error. See [Issue #14](https://github.com/garmeeh/next-seo/issues/14)\n\n#### Facebook\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#facebook)\n\nfacebook\\={{\n  appId: '1234567890',\n}}\n\nAdd this to your SEO config to include the fb:app\\_id meta if you need to enable Facebook insights for your site. Information regarding this can be found in Facebook's [documentation](https://developers.facebook.com/docs/sharing/webmasters/)\n\n#### Canonical URL\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#canonical-url)\n\nAdd this on a page-per-page basis when you want to consolidate duplicate URLs.\n\ncanonical \\= 'https://www.canonical.ie/';\n\n#### Alternate\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#alternate)\n\nThis link relation is used to indicate a relation between a desktop and a mobile website to search engines.\n\nExample:\n\nmobileAlternate\\={{\n  media: 'only screen and (max-width: 640px)',\n  href: 'https://m.canonical.ie',\n}}\n\nlanguageAlternates\\={\\[{\n  hrefLang: 'de-AT',\n  href: 'https://www.canonical.ie/de',\n}\\]}\n\n#### Additional Meta Tags\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#additional-meta-tags)\n\nThis allows you to add any other meta tags that are not covered in the `config` and should be used instead of `children` prop.\n\n`content` is required. Then either `name`, `property` or `httpEquiv`. (Only one on each)\n\nExample:\n\nadditionalMetaTags\\={\\[{\n  property: 'dc:creator',\n  content: 'Jane Doe'\n}, {\n  name: 'application-name',\n  content: 'NextSeo'\n}, {\n  httpEquiv: 'x-ua-compatible',\n  content: 'IE=edge; chrome=1'\n}\\]}\n\nInvalid Examples:\n\nThese are invalid as they contain more than one of `name`, `property` and `httpEquiv` on the same entry.\n\nadditionalMetaTags\\={\\[{\n  property: 'dc:creator',\n  name: 'dc:creator',\n  content: 'Jane Doe'\n}, {\n  property: 'application-name',\n  httpEquiv: 'application-name',\n  content: 'NextSeo'\n}\\]}\n\nOne thing to note on this is that it currently only supports unique tags unless you use the `keyOverride` prop to provide a unique [key](https://reactjs.org/docs/lists-and-keys.html#keys) to each additional meta tag.\n\nThe default behaviour (without a `keyOverride` prop) is to render one tag per unique `name` / `property` / `httpEquiv`. The last one defined will be rendered.\n\nFor example, if you pass 2 tags with the same `property`:\n\nadditionalMetaTags\\={\\[{\n  property: 'dc:creator',\n  content: 'Joe Bloggs'\n}, {\n  property: 'dc:creator',\n  content: 'Jane Doe'\n}\\]}\n\nit will result in this being rendered:\n\n<meta property\\=\"dc:creator\" content\\=\"Jane Doe\" /\\>\n\nProviding an additional `keyOverride` property like this:\n\nadditionalMetaTags\\={\\[{\n  property: 'dc:creator',\n  content: 'Joe Bloggs',\n  keyOverride: 'creator1',\n}, {\n  property: 'dc:creator',\n  content: 'Jane Doe',\n  keyOverride: 'creator2',\n}\\]}\n\nresults in the correct HTML being rendered:\n\n<meta property\\=\"dc:creator\" content\\=\"Joe Bloggs\" /\\>\n<meta property\\=\"dc:creator\" content\\=\"Jane Doe\" /\\>\n\n#### Additional Link Tags\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#additional-link-tags)\n\nThis allows you to add any other link tags that are not covered in the `config`.\n\n`rel` and `href` is required.\n\nExample:\n\nadditionalLinkTags\\={\\[\n  {\n    rel: 'icon',\n    href: 'https://www.test.ie/favicon.ico',\n  },\n  {\n    rel: 'apple-touch-icon',\n    href: 'https://www.test.ie/touch-icon-ipad.jpg',\n    sizes: '76x76'\n  },\n  {\n    rel: 'manifest',\n    href: '/manifest.json'\n  },\n  {\n    rel: 'preload',\n    href: 'https://www.test.ie/font/sample-font.woof2',\n    as: 'font',\n    type: 'font/woff2',\n    crossOrigin: 'anonymous'\n  }\n\\]}\n\nit will result in this being rendered:\n\n<link rel\\=\"icon\" href\\=\"https://www.test.ie/favicon.ico\" /\\>\n<link\n  rel\\=\"apple-touch-icon\"\n  href\\=\"https://www.test.ie/touch-icon-ipad.jpg\"\n  sizes\\=\"76x76\"\n/\\>\n<link rel\\=\"manifest\" href\\=\"/manifest.json\" /\\>\n<link\n  rel\\=\"preload\"\n  href\\=\"https://www.test.ie/font/sample-font.woof2\"\n  as\\=\"font\"\n  type\\=\"font/woff2\"\n  crossorigin\\=\"anonymous\"\n/\\>\n\nOpen Graph\n----------\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#open-graph)\n\nFor the full specification please check out [http://ogp.me/](http://ogp.me/)\n\nNext SEO currently supports:\n\n*   [basic](https://github.com/garmeeh/next-seo?screenshot=true#basic)\n*   [video](https://github.com/garmeeh/next-seo?screenshot=true#video)\n*   [article](https://github.com/garmeeh/next-seo?screenshot=true#article)\n*   [book](https://github.com/garmeeh/next-seo?screenshot=true#book)\n*   [profile](https://github.com/garmeeh/next-seo?screenshot=true#profile)\n\n### Open Graph Examples\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#open-graph-examples)\n\n#### Basic\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#basic)\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      openGraph\\={{\n        type: 'website',\n        url: 'https://www.example.com/page',\n        title: 'Open Graph Title',\n        description: 'Open Graph Description',\n        images: \\[\n          {\n            url: 'https://www.example.ie/og-image.jpg',\n            width: 800,\n            height: 600,\n            alt: 'Og Image Alt',\n          },\n          {\n            url: 'https://www.example.ie/og-image-2.jpg',\n            width: 800,\n            height: 600,\n            alt: 'Og Image Alt 2',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Basic</p\\>\n  </\\>\n);\n\nexport default Page;\n\n**Note**\n\nMultiple images are available from next.js version `7.0.0-canary.0`\n\nFor versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:\n\nimages: \\[\n  {\n    url: 'https://www.example.ie/og-image-01.jpg',\n    width: 800,\n    height: 600,\n    alt: 'Og Image Alt',\n  },\n\\],\n\nSupplying multiple images will not break anything, but only one will be added to the head.\n\n#### Video\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#video)\n\nFull info on [http://ogp.me/](http://ogp.me/#type_video)\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      title\\=\"Video Page Title\"\n      description\\=\"Description of video page\"\n      openGraph\\={{\n        title: 'Open Graph Video Title',\n        description: 'Description of open graph video',\n        url: 'https://www.example.com/videos/video-title',\n        type: 'video.movie',\n        video: {\n          // Multiple Open Graph actors is only available in version \\`7.0.2-canary.35\\`+ of next\n          actors: \\[\n            {\n              profile: 'https://www.example.com/actors/@firstnameA-lastnameA',\n              role: 'Protagonist',\n            },\n            {\n              profile: 'https://www.example.com/actors/@firstnameB-lastnameB',\n              role: 'Antagonist',\n            },\n          \\],\n          // Multiple Open Graph directors is only available in version \\`7.0.2-canary.35\\`+ of next\n          directors: \\[\n            'https://www.example.com/directors/@firstnameA-lastnameA',\n            'https://www.example.com/directors/@firstnameB-lastnameB',\n          \\],\n          // Multiple Open Graph writers is only available in version \\`7.0.2-canary.35\\`+ of next\n          writers: \\[\n            'https://www.example.com/writers/@firstnameA-lastnameA',\n            'https://www.example.com/writers/@firstnameB-lastnameB',\n          \\],\n          duration: 680000,\n          releaseDate: '2022-12-21T22:04:11Z',\n          // Multiple Open Graph tags is only available in version \\`7.0.2-canary.35\\`+ of next\n          tags: \\['Tag A', 'Tag B', 'Tag C'\\],\n        },\n        siteName: 'SiteName',\n      }}\n    /\\>\n    <h1\\>Video Page SEO</h1\\>\n  </\\>\n);\n\nexport default Page;\n\n**Note**\n\nMultiple images are available from next.js version `7.0.0-canary.0`\n\nFor versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:\n\nimages: \\[\n  {\n    url: 'https://www.example.ie/og-image-01.jpg',\n    width: 800,\n    height: 600,\n    alt: 'Og Image Alt',\n  },\n\\],\n\nSupplying multiple images will not break anything, but only one will be added to the head.\n\n#### Audio\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#audio)\n\nFull info on [http://ogp.me/](https://ogp.me/#structured)\n\nimport { NextSeo } from 'next-seo';\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      title\\=\"Audio Page Title\"\n      description\\=\"Description of audio page\"\n      openGraph\\={{\n        title: 'Open Graph Audio',\n        description: 'Description of open graph audio',\n        url: 'https://www.example.com/audio/audio',\n        audio: \\[\n          {\n            url: 'http://examples.opengraphprotocol.us/media/audio/1khz.mp3',\n            secureUrl: 'https://d72cgtgi6hvvl.cloudfront.net/media/audio/1khz.mp3',\n            type: \"audio/mpeg\"\n          },\n          {\n            url: 'http://examples.opengraphprotocol.us/media/audio/250hz.mp3',\n            secureUrl: 'https://d72cgtgi6hvvl.cloudfront.net/media/audio/250hz.mp3',\n            type: \"audio/mpeg\"\n          },\n        \\]\n        site\\_name: 'SiteName',\n      }}\n    /\\>\n    <h1\\>Audio Page SEO</h1\\>\n  </\\>\n);\nexport default Page;\n\n#### Article\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#article)\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      openGraph\\={{\n        title: 'Open Graph Article Title',\n        description: 'Description of open graph article',\n        url: 'https://www.example.com/articles/article-title',\n        type: 'article',\n        article: {\n          publishedTime: '2017-06-21T23:04:13Z',\n          modifiedTime: '2018-01-21T18:04:43Z',\n          expirationTime: '2022-12-21T22:04:11Z',\n          section: 'Section II',\n          authors: \\[\n            'https://www.example.com/authors/@firstnameA-lastnameA',\n            'https://www.example.com/authors/@firstnameB-lastnameB',\n          \\],\n          tags: \\['Tag A', 'Tag B', 'Tag C'\\],\n        },\n        images: \\[\n          {\n            url: 'https://www.test.ie/images/cover.jpg',\n            width: 850,\n            height: 650,\n            alt: 'Photo of text',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Article</p\\>\n  </\\>\n);\n\nexport default Page;\n\n**Note**\n\nMultiple images, authors, and tags are available from next.js version `7.0.0-canary.0`\n\nFor versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:\n\n`images:`\n\nimages: \\[\n  {\n    url: 'https://www.example.ie/og-image-01.jpg',\n    width: 800,\n    height: 600,\n    alt: 'Og Image Alt',\n  },\n\\],\n\n`authors:`\n\nauthors: \\[\n  'https://www.example.com/authors/@firstnameA-lastnameA',\n\\],\n\n`tags:`\n\nSupplying multiple of any of the above will not break anything, but only one will be added to the head.\n\n#### Book\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#book)\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      openGraph\\={{\n        title: 'Open Graph Book Title',\n        description: 'Description of open graph book',\n        url: 'https://www.example.com/books/book-title',\n        type: 'book',\n        book: {\n          releaseDate: '2018-09-17T11:08:13Z',\n          isbn: '978-3-16-148410-0',\n          authors: \\[\n            'https://www.example.com/authors/@firstnameA-lastnameA',\n            'https://www.example.com/authors/@firstnameB-lastnameB',\n          \\],\n          tags: \\['Tag A', 'Tag B', 'Tag C'\\],\n        },\n        images: \\[\n          {\n            url: 'https://www.test.ie/images/book.jpg',\n            width: 850,\n            height: 650,\n            alt: 'Cover of the book',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Book</p\\>\n  </\\>\n);\n\nexport default Page;\n\n**Note**\n\nMultiple images, authors, and tags are available from next.js version `7.0.0-canary.0`\n\nFor versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:\n\n`images:`\n\nimages: \\[\n  {\n    url: 'https://www.example.ie/og-image-01.jpg',\n    width: 800,\n    height: 600,\n    alt: 'Og Image Alt',\n  },\n\\],\n\n`authors:`\n\nauthors: \\[\n  'https://www.example.com/authors/@firstnameA-lastnameA',\n\\],\n\n`tags:`\n\nSupplying multiple of any of the above will not break anything, but only one will be added to the head.\n\n#### Profile\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#profile)\n\nimport { NextSeo } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <NextSeo\n      openGraph\\={{\n        title: 'Open Graph Profile Title',\n        description: 'Description of open graph profile',\n        url: 'https://www.example.com/@firstlast123',\n        type: 'profile',\n        profile: {\n          firstName: 'First',\n          lastName: 'Last',\n          username: 'firstlast123',\n          gender: 'female',\n        },\n        images: \\[\n          {\n            url: 'https://www.test.ie/images/profile.jpg',\n            width: 850,\n            height: 650,\n            alt: 'Profile Photo',\n          },\n        \\],\n      }}\n    /\\>\n    <p\\>Profile</p\\>\n  </\\>\n);\n\nexport default Page;\n\n**Note**\n\nMultiple images are available from next.js version `7.0.0-canary.0`\n\nFor versions `6.0.0` - `7.0.0-canary.0` you just need to supply a single item array:\n\nimages: \\[\n  {\n    url: 'https://www.example.ie/og-image-01.jpg',\n    width: 800,\n    height: 600,\n    alt: 'Og Image Alt',\n  },\n\\],\n\nSupplying multiple images will not break anything, but only one will be added to the head.\n\nJSON-LD\n-------\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#json-ld)\n\nNext SEO now has the ability to set JSON-LD a form of structured data. Structured data is a standardized format for providing information about a page and classifying the page content.\n\nGoogle has excellent content on JSON-LD -\\> [HERE](https://developers.google.com/search/docs/data-types/article)\n\n**If using the app directory then please ensure to add `useAppDir={true}` prop and that you are using the component in the `page.js`**\n\nBelow you will find a very basic page implementing each of the available JSON-LD types:\n\n*   [Article](https://github.com/garmeeh/next-seo?screenshot=true#article-1)\n*   [Breadcrumb](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb)\n*   [Blog](https://github.com/garmeeh/next-seo?screenshot=true#blog)\n*   [Campground](https://github.com/garmeeh/next-seo?screenshot=true#campground)\n*   [Recipe](https://github.com/garmeeh/next-seo?screenshot=true#recipe)\n*   [Sitelinks Search Box](https://github.com/garmeeh/next-seo?screenshot=true#sitelinks-search-box)\n*   [Course](https://github.com/garmeeh/next-seo?screenshot=true#course)\n*   [Dataset](https://github.com/garmeeh/next-seo?screenshot=true#dataset)\n*   [Corporate Contact](https://github.com/garmeeh/next-seo?screenshot=true#corporate-contact)\n*   [FAQ Page](https://github.com/garmeeh/next-seo?screenshot=true#faq-page)\n*   [How-to](https://github.com/garmeeh/next-seo?screenshot=true#how-to)\n*   [Job Posting](https://github.com/garmeeh/next-seo?screenshot=true#job-posting)\n*   [Local Business](https://github.com/garmeeh/next-seo?screenshot=true#local-business)\n*   [Product](https://github.com/garmeeh/next-seo?screenshot=true#product)\n*   [Social Profile](https://github.com/garmeeh/next-seo?screenshot=true#social-profile)\n*   [News Article](https://github.com/garmeeh/next-seo?screenshot=true#news-article)\n*   [Park](https://github.com/garmeeh/next-seo?screenshot=true#park)\n\nPull requests are very welcome to add any from the list [found here](https://developers.google.com/search/docs/data-types/article)\n\n#### JSON-LD Security\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#json-ld-security)\n\nJust a quick note on security. To get JSON-LD onto the page it needs to be in a script tag. `next-seo` achieves this by using a script tag with `dangerouslySetInnerHTML`.\n\nSo if passing anything directly from a URL to one of the components below please ensure you sanitize it first if needed.\n\nView `toJson.tsx` for implementation detail.\n\n#### Handling multiple instances\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#handling-multiple-instances)\n\nIf your page requires multiple instances of a given JSON-LD component, you can specify unique `keyOverride` properties, and `next-seo` will handle the rest.\n\nThis comes in handy for blog rolls, search results, and overview pages.\n\nPlease fully research when you should and shouldn't add multiple instances of JSON-LD.\n\n<ExampleJsonLd keyOverride\\=\"my-new-key\" /\\>\n\n### Article\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#article-1)\n\nimport { ArticleJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Article JSON-LD</h1\\>\n    <ArticleJsonLd\n      useAppDir\\={false}\n      url\\=\"https://example.com/article\"\n      title\\=\"Article headline\"\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      datePublished\\=\"2015-02-05T08:00:00+08:00\"\n      dateModified\\=\"2015-02-05T09:00:00+08:00\"\n      authorName\\={\\[\n        {\n          name: 'Jane Blogs',\n          url: 'https://example.com',\n        },\n        {\n          name: 'Mary Stone',\n          url: 'https://example.com',\n        },\n      \\]}\n      publisherName\\=\"Gary Meehan\"\n      publisherLogo\\=\"https://www.example.com/photos/logo.jpg\"\n      description\\=\"This is a mighty good description of this article.\"\n      isAccessibleForFree\\={true}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n### Breadcrumb\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb)\n\nimport { BreadcrumbJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Breadcrumb JSON-LD</h1\\>\n    <BreadcrumbJsonLd\n      itemListElements\\={\\[\n        {\n          position: 1,\n          name: 'Books',\n          item: 'https://example.com/books',\n        },\n        {\n          position: 2,\n          name: 'Authors',\n          item: 'https://example.com/books/authors',\n        },\n        {\n          position: 3,\n          name: 'Ann Leckie',\n          item: 'https://example.com/books/authors/annleckie',\n        },\n        {\n          position: 4,\n          name: 'Ancillary Justice',\n          item: 'https://example.com/books/authors/ancillaryjustice',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `itemListElements` |  |\n| `itemListElements.position` | The position of the breadcrumb in the breadcrumb trail. Position 1 signifies the beginning of the trail. |\n| `itemListElements.name` | The title of the breadcrumb displayed for the user. |\n| `itemListElements.item` | The URL to the webpage that represents the breadcrumb. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Blog\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#blog)\n\nimport { ArticleJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Blog JSON-LD</h1\\>\n    <ArticleJsonLd\n      type\\=\"BlogPosting\"\n      url\\=\"https://example.com/blog\"\n      title\\=\"Blog headline\"\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      datePublished\\=\"2015-02-05T08:00:00+08:00\"\n      dateModified\\=\"2015-02-05T09:00:00+08:00\"\n      authorName\\=\"Jane Blogs\"\n      description\\=\"This is a mighty good description of this blog.\"\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n### Campground\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#campground)\n\nimport { CampgroundJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Campground JSON-LD</h1\\>\n    <CampgroundJsonLd\n      id\\=\"https://www.example.com/campground/rip-van-winkle-campground\"\n      name\\=\"Rip Van Winkle Campgrounds\"\n      url\\=\"https://www.example.com/campground\"\n      telephone\\=\"+18452468114\"\n      images\\={\\['https://example.com/photos/1x1/photo.jpg'\\]}\n      address\\={{\n        streetAddress: '149 Blue Mountain Rd',\n        addressLocality: 'Saugerties',\n        addressRegion: 'NY',\n        postalCode: '12477',\n        addressCountry: 'US',\n      }}\n      description\\=\"Description about Rip Van Winkle Campgrounds\"\n      geo\\={{\n        latitude: '42.092599',\n        longitude: '-74.018580',\n      }}\n      openingHours\\={\\[\n        {\n          opens: '09:00',\n          closes: '17:00',\n          dayOfWeek: \\[\n            'Monday',\n            'Tuesday',\n            'Wednesday',\n            'Thursday',\n            'Friday',\n            'Saturday',\n            'Sunday',\n          \\],\n          validFrom: '2019-12-23',\n          validThrough: '2020-04-02',\n        },\n      \\]}\n      petsAllowed\n      rating\\={{\n        ratingValue: '5',\n        ratingCount: '18',\n      }}\n      amenityFeature\\={{\n        name: 'Showers',\n        value: true,\n      }}\n      priceRange\\=\"$$\"\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `@id` | Globally unique ID of the specific campground in the form of a URL. |\n| `address` | Address of the specific campground location |\n| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |\n| `address.addressLocality` | City |\n| `address.addressRegion` | State or province, if applicable. |\n| `address.postalCode` | Postal or zip code. |\n| `address.streetAddress` | Street number, street name, and unit number. |\n| `name` | Campground name. |\n| `description` | Campground description. |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `geo` | Geographic coordinates of the campground. |\n| `geo.latitude` | The latitude of the campground location |\n| `geo.longitude` | The longitude of the campground location |\n| `images` | An image or images of the campground. Required for valid markup depending on the type |\n| `telephone` | A campground phone number meant to be the primary contact method for customers. |\n| `url` | The fully-qualified URL of the specific campground. |\n| `openingHours` | Opening hour specification of the campground. You can provide this as a single object, or an array of objects with the properties below. |\n| `openingHours.opens` | The opening hour of the place or service on the given day(s) of the week. |\n| `openingHours.closes` | The closing hour of the place or service on the given day(s) of the week. |\n| `openingHours.dayOfWeek` | The day of the week for which these opening hours are valid. Can be a string or array of strings. Refer to [DayOfWeek](https://schema.org/DayOfWeek) |\n| `openingHours.validFrom` | The date when the item becomes valid. |\n| `openingHours.validThrough` | The date after when the item is not valid. |\n| `isAccessibleForFree` | Whether or not the campground is accessible for free. |\n| `petsAllowed` | Whether or not the campgroud allows pets. |\n| `amenityFeature` | An amenity feature (e.g. a characteristic or service) of the campground. |\n| `amenityFeature.name` | The name of the amenity. |\n| `amenityFeature.value` | The value of the amenity. |\n| `priceRange` | The price range of the campground, for example $$$. |\n| `rating` | The average rating of the campground based on multiple ratings or reviews. |\n| `rating.ratingValue` | The rating for the content. |\n| `rating.ratingCount` | The count of total number of ratings. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Recipe\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#recipe)\n\nimport { RecipeJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Recipe JSON-LD</h1\\>\n    <RecipeJsonLd\n      name\\=\"Party Coffee Cake\"\n      description\\=\"This coffee cake is awesome and perfect for parties.\"\n      datePublished\\=\"2018-03-10\"\n      authorName\\={\\['Jane Blogs', 'Mary Stone'\\]}\n      prepTime\\=\"PT20M\"\n      cookTime\\=\"PT30M\"\n      totalTime\\=\"PT50M\"\n      keywords\\=\"cake for a party, coffee\"\n      yields\\=\"10\"\n      category\\=\"Dessert\"\n      cuisine\\=\"American\"\n      calories\\={270}\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      ingredients\\={\\[\n        '2 cups of flour',\n        '3/4 cup white sugar',\n        '2 teaspoons baking powder',\n        '1/2 teaspoon salt',\n        '1/2 cup butter',\n        '2 eggs',\n        '3/4 cup milk',\n      \\]}\n      instructions\\={\\[\n        {\n          name: 'Preheat',\n          text: 'Preheat the oven to 350 degrees F. Grease and flour a 9x9 inch pan.',\n          url: 'https://example.com/party-coffee-cake#step1',\n          image: 'https://example.com/photos/party-coffee-cake/step1.jpg',\n        },\n      \\]}\n      aggregateRating\\={{\n        ratingValue: '5',\n        ratingCount: '18',\n      }}\n      video\\={{\n        name: 'How to make a Party Coffee Cake',\n        description: 'This is how you make a Party Coffee Cake.',\n        contentUrl: 'http://www.example.com/video123.mp4',\n        embedUrl: 'http://www.example.com/videoplayer?video=123',\n        uploadDate: '2018-02-05T08:00:00+08:00',\n        duration: 'PT1M33S',\n        thumbnailUrls: \\[\n          'https://example.com/photos/1x1/photo.jpg',\n          'https://example.com/photos/4x3/photo.jpg',\n          'https://example.com/photos/16x9/photo.jpg',\n        \\],\n        expires: '2019-02-05T08:00:00+08:00',\n        hasPart: {\n          '@type': 'Clip',\n          name: 'Preheat oven',\n          startOffset: 30,\n          url: 'http://www.example.com/example?t=30',\n        },\n        watchCount: 2347,\n        publication: {\n          '@type': 'BroadcastEvent',\n          isLiveBroadcast: true,\n          startDate: '2020-10-24T14:00:00+00:00',\n          endDate: '2020-10-24T14:37:14+00:00',\n        },\n        regionsAllowed: \\['IT', 'NL'\\],\n      }}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The name of the recipe |\n| `description` | A description of the recipe |\n| `authorName` | The name of the recipe author. Can be a string or array of strings. |\n| `ingredients` | A list of ingredient strings |\n| `instructions` | \\- |\n| `instructions.name` | The name of the instruction step. |\n| `instructions.text` | The directions of the instruction step. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Sitelinks Search Box\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#sitelinks-search-box)\n\nimport { SiteLinksSearchBoxJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Sitelinks Search Box JSON-LD</h1\\>\n    <SiteLinksSearchBoxJsonLd\n      url\\=\"https://www.example.com\"\n      potentialActions\\={\\[\n        {\n          target: 'https://query.example.com/search?q',\n          queryInput: 'search\\_term\\_string',\n        },\n        {\n          target: 'android-app://com.example/https/query.example.com/search/?q',\n          queryInput: 'search\\_term\\_string',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `url` | URL of the website associated with the sitelinks searchbox |\n| `potentialActions` | Array of one or two SearchAction objects. Describes the URI to send the query to, and the syntax of the request that is sent |\n| `potentialActions.target` | For websites, the URL of the handler that should receive and handle the search query; for apps, the URI of the intent handler for your search engine that should handle queries |\n| `potentialActions.queryInput` | Placeholder used in target, gets substituted for user given query |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\nRead the [documentation](https://developers.google.com/search/docs/appearance/structured-data/sitelinks-searchbox)\n\n### Course\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#course)\n\nimport { CourseJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Course JSON-LD</h1\\>\n    <CourseJsonLd\n      courseName\\=\"Course Name\"\n      description\\=\"Introductory CS course laying out the basics.\"\n      provider\\={{\n        name: 'Course Provider',\n        url: 'https//www.example.com/provider',\n      }}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `courseName` | The title of the course. |\n| `description` | A description of the course. Display limit of 60 characters. |\n| `provider.name` | The course provider name. |\n| `provider.url` | The course provider name url. |\n\n**Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `providerUrl` | The url to the course provider. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Dataset\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#dataset)\n\nimport { DatasetJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Dataset JSON-LD</h1\\>\n    <DatasetJsonLd\n      description\\=\"The description needs to be at least 50 characters long\"\n      name\\=\"name of the dataset\"\n      license\\=\"https//www.example.com\"\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `description` | A short summary describing a dataset. Needs to be between 50 and 5000 characters. |\n| `name` | A license under which the dataset is distributed. |\n\n**Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `license` | The url to the course provider. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Corporate Contact\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#corporate-contact)\n\nimport { CorporateContactJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Corporate Contact JSON-LD</h1\\>\n    <CorporateContactJsonLd\n      url\\=\"http://www.your-company-site.com\"\n      logo\\=\"http://www.example.com/logo.png\"\n      contactPoint\\={\\[\n        {\n          telephone: '+1-401-555-1212',\n          contactType: 'customer service',\n          email: 'customerservice@email.com',\n          areaServed: 'US',\n          availableLanguage: \\['English', 'Spanish', 'French'\\],\n        },\n        {\n          telephone: '+1-877-746-0909',\n          contactType: 'customer service',\n          email: 'servicecustomer@email.com',\n          contactOption: 'TollFree',\n          availableLanguage: 'English',\n        },\n        {\n          telephone: '+1-877-453-1304',\n          contactType: 'technical support',\n          contactOption: 'TollFree',\n          areaServed: \\['US', 'CA'\\],\n          availableLanguage: \\['English', 'French'\\],\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `url` | Url to the home page of the company's official site. |\n| `contactPoint` |  |\n| `contactPoint.telephone` | An internationalized version of the phone number, starting with the \"+\" symbol and country code |\n| `contactPoint.contactType` | Description of the purpose of the phone number i.e. `Technical Support`. |\n\n**Recommended ContactPoint properties**\n\n| Property | Info |\n| --- | --- |\n| `contactPoint.areaServed` | `String` or `Array` of geographical regions served by the business. Example `\"US\"` or `[\"US\", \"CA\", \"MX\"]` |\n| `contactPoint.availableLanguage` | Details about the language spoken. Example `\"English\"` or `[\"English\", \"French\"]` |\n| `contactPoint.email` | Email asscosiated with the business\\` |\n| `gecontactPointo.contactOption` | Details about the phone number. Example `\"TollFree\"` |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### FAQ Page\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#faq-page)\n\nimport { FAQPageJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>FAQ Page JSON-LD</h1\\>\n    <FAQPageJsonLd\n      mainEntity\\={\\[\n        {\n          questionName: 'How long is the delivery time?',\n          acceptedAnswerText: '3-5 business days.',\n        },\n        {\n          questionName: 'Where can I find information about product recalls?',\n          acceptedAnswerText: 'Read more on under information.',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `mainEntity` |  |\n| `mainEntity.questionName` | The full text of the question. For example, \"How long is the delivery time?\". |\n| `mainEntity.acceptedAnswerText` | The full answer to the question. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### How-to\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#how-to)\n\nimport { HowToJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>How-to JSON-LD</h1\\>\n    <HowToJsonLd\n      name\\=\"How to tile a kitchen backsplash\"\n      image\\=\"https://example.com/photos/1x1/photo.jpg\"\n      estimatedCost\\={{ currency: 'USD', value: '100' }}\n      supply\\={\\['tiles', 'thin-set', 'mortar', 'tile grout', 'grout sealer'\\]}\n      tool\\={\\['notched trowel', 'bucket', 'large sponge'\\]}\n      step\\={\\[\n        {\n          url: 'https://example.com/kitchen#step1',\n          name: 'Prepare the surfaces',\n          itemListElement: \\[\n            {\n              type: 'HowToTip',\n              text: 'Turn off the power to the kitchen and then remove everything that is on the wall, such as outlet covers, switchplates, and any other item in the area that is to be tiled.',\n            },\n            {\n              type: 'HowToDirection',\n              text: 'Then clean the surface thoroughly to remove any grease or other debris and tape off the area.',\n            },\n          \\],\n          image: 'https://example.com/photos/1x1/photo-step1.jpg',\n        },\n      \\]}\n      totalTime\\=\"P2D\"\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | Name of the HowTo |\n| `step` | An array of HowToStep elements which comprise the full instructions of the how-to. |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `estimatedCost` | The estimated cost of the supplies consumed when performing instructions. |\n| `image` | Image of the completed how-to. |\n| `supply` | A supply consumed when performing instructions or a direction. |\n| `tool` | An object used (but not consumed) when performing instructions or a direction. |\n| `totalTime` | The total time required to perform all instructions or directions (including time to prepare the supplies), in ISO 8601 duration format. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Job Posting\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#job-posting)\n\nimport { JobPostingJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Job Posting JSON-LD</h1\\>\n    <JobPostingJsonLd\n      datePosted\\=\"2020-01-06T03:37:40Z\"\n      description\\=\"Company is looking for a software developer....\"\n      hiringOrganization\\={{\n        name: 'company name',\n        sameAs: 'www.company-website-url.dev',\n      }}\n      jobLocation\\={{\n        streetAddress: '17 street address',\n        addressLocality: 'Paris',\n        addressRegion: 'Ile-de-France',\n        postalCode: '75001',\n        addressCountry: 'France',\n      }}\n      title\\=\"Job Title\"\n      baseSalary\\={{\n        currency: 'EUR',\n        value: 40, // Can also be a salary range, like \\[40, 50\\]\n        unitText: 'HOUR',\n      }}\n      employmentType\\=\"FULL\\_TIME\"\n      jobLocationType\\=\"TELECOMMUTE\"\n      validThrough\\=\"2020-01-06\"\n      applicantLocationRequirements\\=\"FR\"\n      experienceRequirements\\={{\n        occupational: {\n          minimumMonthsOfExperience: 12,\n        },\n        educational: {\n          credentialCategory: 'high school',\n        },\n        experienceInPlaceOfEducation: true,\n      }}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `datePosted` | The original date that employer posted the job in ISO 8601 format |\n| `description` | The full description of the job in HTML format |\n| `hiringOrganization` | An object containing information about the company hiring with the following fields or the string `'confidential'` when hiring anonymously |\n| `hiringOrganization.name` | Name of the company offering the job position |\n| `hiringOrganization.sameAs` | URL of a reference Web page |\n| `title` | The title of the job (not the title of the posting) |\n| `validThrough` | The date when the job posting will expire in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `applicantLocationRequirements` | The geographic location(s) in which employees may be located for to be eligible for the remote job |\n| `baseSalary` |  |\n| `baseSalary.currency` | The currency in which the monetary amount is expressed |\n| `baseSalary.value` | The value of the quantitative value. You can also provide an array of minimum and maximum salaries. . |\n| `baseSalary.unitText` | A string indicating the unit of measurement [Base salary guideline](https://developers.google.com/search/docs/data-types/job-posting#basesalary) |\n| `employmentType` | Type of employment [Employement type guideline](https://developers.google.com/search/docs/data-types/job-posting#basesalary) |\n| `jobLocation` | The physical location(s) of the business where the employee will report to work (such as an office or worksite), not the location where the job was posted. |\n| `jobLocation.streetAddress` | The street address. For example, 1600 Amphitheatre Pkwy |\n| `jobLocation.addressLocality` | The locality. For example, Mountain View. |\n| `jobLocation.addressRegion` | The region. For example, CA. |\n| `jobLocation.postalCode` | The postal code. For example, 94043 |\n| `jobLocation.addressCountry` | The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code. |\n| `jobLocationType` | A description of the job location [Job Location type guideline](https://developers.google.com/search/docs/data-types/job-posting#job-location-type) |\n| `hiringOrganization.logo` | Logos on third-party job sites [Hiring Organization guideline](https://developers.google.com/search/docs/data-types/job-posting#hiring) |\n| `experienceRequirements.occupational.minimumMonthsOfExperience` | The minimum number of months of experience that are required for the job posting. [Experience and Education Requirements](https://developers.google.com/search/docs/appearance/structured-data/job-posting#education-and-experience-properties-beta) |\n| `experienceRequirements.educational.credentialCategory` | The level of education that's required for the job posting. Use one of the following: `high school`, `associate degree`, `bachelor degree`, `professional certificate`, `postgraduate degree` |\n| `experienceRequirements.experienceInPlaceOfEducation` | Boolean: If set to true, this property indicates whether a job posting will accept experience in place of its formal educational qualifications. If set to true, you must include both the experienceRequirements and educationRequirements properties. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Local Business\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#local-business)\n\nLocal business is supported with a sub-set of properties.\n\n<LocalBusinessJsonLd\n  type\\=\"Store\"\n  id\\=\"http://davesdeptstore.example.com\"\n  name\\=\"Dave's Department Store\"\n  description\\=\"Dave's latest department store in San Jose, now open\"\n  url\\=\"http://www.example.com/store-locator/sl/San-Jose-Westgate-Store/1427\"\n  telephone\\=\"+14088717984\"\n  address\\={{\n    streetAddress: '1600 Saratoga Ave',\n    addressLocality: 'San Jose',\n    addressRegion: 'CA',\n    postalCode: '95129',\n    addressCountry: 'US',\n  }}\n  geo\\={{\n    latitude: '37.293058',\n    longitude: '-121.988331',\n  }}\n  images\\={\\[\n    'https://example.com/photos/1x1/photo.jpg',\n    'https://example.com/photos/4x3/photo.jpg',\n    'https://example.com/photos/16x9/photo.jpg',\n  \\]}\n  sameAs\\={\\[\n    'www.company-website-url1.dev',\n    'www.company-website-url2.dev',\n    'www.company-website-url3.dev',\n  \\]}\n  openingHours\\={\\[\n    {\n      opens: '08:00',\n      closes: '23:59',\n      dayOfWeek: \\[\n        'Monday',\n        'Tuesday',\n        'Wednesday',\n        'Thursday',\n        'Friday',\n        'Saturday',\n      \\],\n      validFrom: '2019-12-23',\n      validThrough: '2020-04-02',\n    },\n    {\n      opens: '14:00',\n      closes: '20:00',\n      dayOfWeek: 'Sunday',\n      validFrom: '2019-12-23',\n      validThrough: '2020-04-02',\n    },\n  \\]}\n  rating\\={{\n    ratingValue: '4.5',\n    ratingCount: '2',\n  }}\n  review\\={\\[\n    {\n      author: 'John Doe',\n      datePublished: '2006-05-04',\n      name: 'A masterpiece of literature',\n      reviewBody:\n        'I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.',\n      reviewRating: {\n        bestRating: '5',\n        worstRating: '1',\n        reviewAspect: 'Ambiance',\n        ratingValue: '4',\n      },\n    },\n    {\n      author: 'Bob Smith',\n      datePublished: '2006-06-15',\n      name: 'A good read.',\n      reviewBody: \"Catcher in the Rye is a fun book. It's a good book to read.\",\n      reviewRating: {\n        ratingValue: '4',\n      },\n    },\n  \\]}\n  makesOffer\\={\\[\n    {\n      priceSpecification: {\n        type: 'UnitPriceSpecification',\n        priceCurrency: 'EUR',\n        price: '1000-10000',\n      },\n      itemOffered: {\n        name: 'Motion Design Services',\n        description:\n          'We are the expert of animation and motion design productions.',\n      },\n    },\n    {\n      priceSpecification: {\n        type: 'UnitPriceSpecification',\n        priceCurrency: 'EUR',\n        price: '2000-10000',\n      },\n      itemOffered: {\n        name: 'Branding Services',\n        description:\n          'Real footage is a powerful tool when it comes to show what the business is about. Can be used to present your company, show your factory, promote a product packshot, or just tell any story. It can help create emotional links with your audience by showing punchy images.',\n      },\n    },\n  \\]}\n  areaServed\\={\\[\n    {\n      geoMidpoint: {\n        latitude: '41.108237',\n        longitude: '-80.642982',\n      },\n      geoRadius: '1000',\n    },\n    {\n      geoMidpoint: {\n        latitude: '51.108237',\n        longitude: '-80.642982',\n      },\n      geoRadius: '1000',\n    },\n  \\]}\n  action\\={{\n    actionName: 'potentialAction',\n    actionType: 'ReviewAction',\n    target: 'https://www.example.com/review/this/business',\n  }}\n/\\>\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `@id` | Globally unique ID of the specific business location in the form of a URL. |\n| `type` | LocalBusiness or any sub-type |\n| `address` | Address of the specific business location |\n| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |\n| `address.addressLocality` | City |\n| `address.addressRegion` | State or province, if applicable. |\n| `address.postalCode` | Postal or zip code. |\n| `address.streetAddress` | Street number, street name, and unit number. |\n| `name` | Business name. |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `description` | Description of the business location |\n| `geo` | Geographic coordinates of the business. |\n| `geo.latitude` | The latitude of the business location |\n| `geo.longitude` | The longitude of the business location |\n| `rating` | The average rating of business based on multiple ratings or reviews. |\n| `rating.ratingValue` | The rating for the content. |\n| `rating.ratingCount` | The count of total number of ratings. |\n| `priceRange` | The relative price range of the business. |\n| `servesCuisine` | The type of cuisine the restaurant serves. |\n| `images` | An image or images of the business. Required for valid markup depending on the type |\n| `telephone` | A business phone number meant to be the primary contact method for customers. |\n| `url` | The fully-qualified URL of the specific business location. |\n| `sameAs` | An array of URLs that represent this business |\n| `openingHours` | Opening hour specification of business. You can provide this as a single object, or an array of objects with the properties below. |\n| `openingHours.opens` | The opening hour of the place or service on the given day(s) of the week. |\n| `openingHours.closes` | The closing hour of the place or service on the given day(s) of the week. |\n| `openingHours.dayOfWeek` | The day of the week for which these opening hours are valid. Can be a string or array of strings. Refer to [DayOfWeek](https://schema.org/DayOfWeek) |\n| `openingHours.validFrom` | The date when the item becomes valid. |\n| `openingHours.validThrough` | The date after when the item is not valid. |\n| `review` | A review of the local business. |\n| `review.author` | The author of this content or rating. |\n| `review.reviewBody` | The actual body of the review. |\n| `review.datePublished` | Date of first broadcast/publication. |\n| `review.name` | The name of the item. |\n| `review.rating` | The rating given in this review |\n| `review.rating.ratingValue` | The rating for the content. |\n| `review.rating.reviewAspect` | This Review or Rating is relevant to this part or facet of the itemReviewed. |\n| `review.rating.worstRating` | The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed. |\n| `review.rating.bestRating` | The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed |\n| `areasServed` | The geographic area where a service or offered item is provided. |\n| `areasServed.GeoCircle` | A GeoCircle is a GeoShape representing a circular geographic area. |\n| `areasServed.GeoCircle.geoMidpoint` | Indicates the GeoCoordinates at the centre of a GeoShape e.g. GeoCircle. |\n| `areasServed.GeoCircle.geoMidpoint.latitude` | The latitude of a location. For example 37.42242 |\n| `areasServed.GeoCircle.geoMidpoint.longitude` | The name of the item. |\n| `areasServed.GeoCircle.geoRadius` | Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation). |\n| `makesOffer` | A pointer to products or services offered by the organization or person. |\n| `makesOffer.offer` | An offer to transfer some rights to an item or to provide a service |\n| `makesOffer.offer.priceSpecification` | One or more detailed price specifications, indicating the unit price and delivery or payment charges. |\n| `makesOffer.offer.priceSpecification.priceCurrency` | The currency of the price, or a price component when attached to PriceSpecification and its subtypes. |\n| `makesOffer.offer.priceSpecification.price` | The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes. |\n| `makesOffer.offer.itemOffered` | An item being offered (or demanded) |\n| `makesOffer.offer.itemOffered.name` | The name of the item |\n| `makesOffer.offer.itemOffered.description` | The description of the item. |\n| `action` | An action performed by a direct agent and indirect participants upon a direct object. |\n| `action.target` | Indicates a target EntryPoint for an Action. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n**NOTE:**\n\nImages are recommended for most of the types that you can use for `LocalBusiness`; if in doubt, you should add an image. You can check your generated JSON over at Google's [Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool)\n\n### Logo\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#logo)\n\nimport { LogoJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Logo JSON-LD</h1\\>\n    <LogoJsonLd\n      logo\\=\"http://www.your-site.com/images/logo.jpg\"\n      url\\=\"http://www.your-site.com\"\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n| Property | Info |\n| --- | --- |\n| `url` | The URL of the website associated with the logo. [Logo guidelines](https://developers.google.com/search/docs/data-types/logo#definitions) |\n| `logo` | URL of a logo that is representative of the organization. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### Product\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#product)\n\nimport { ProductJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Product JSON-LD</h1\\>\n    <ProductJsonLd\n      productName\\=\"Executive Anvil\"\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      description\\=\"Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.\"\n      brand\\=\"ACME\"\n      color\\=\"blue\"\n      manufacturerName\\=\"Gary Meehan\"\n      manufacturerLogo\\=\"https://www.example.com/photos/logo.jpg\"\n      material\\=\"steel\"\n      slogan\\=\"For the business traveller looking for something to drop from a height.\"\n      disambiguatingDescription\\=\"Executive Anvil, perfect for the business traveller.\"\n      releaseDate\\=\"2014-02-05T08:00:00+08:00\"\n      productionDate\\=\"2015-02-05T08:00:00+08:00\"\n      purchaseDate\\=\"2015-02-06T08:00:00+08:00\"\n      award\\=\"Best Executive Anvil Award.\"\n      reviews\\={\\[\n        {\n          author: 'Jim',\n          datePublished: '2017-01-06T03:37:40Z',\n          reviewBody:\n            'This is my favorite product yet! Thanks Nate for the example products and reviews.',\n          name: 'So awesome!!!',\n          reviewRating: {\n            bestRating: '5',\n            ratingValue: '5',\n            worstRating: '1',\n          },\n          publisher: {\n            type: 'Organization',\n            name: 'TwoVit',\n          },\n        },\n      \\]}\n      aggregateRating\\={{\n        ratingValue: '4.4',\n        reviewCount: '89',\n      }}\n      offers\\={\\[\n        {\n          price: '119.99',\n          priceCurrency: 'USD',\n          priceValidUntil: '2020-11-05',\n          itemCondition: 'https://schema.org/UsedCondition',\n          availability: 'https://schema.org/InStock',\n          url: 'https://www.example.com/executive-anvil',\n          seller: {\n            name: 'Executive Objects',\n          },\n        },\n        {\n          price: '139.99',\n          priceCurrency: 'CAD',\n          priceValidUntil: '2020-09-05',\n          itemCondition: 'https://schema.org/UsedCondition',\n          availability: 'https://schema.org/InStock',\n          url: 'https://www.example.ca/executive-anvil',\n          seller: {\n            name: 'Executive Objects',\n          },\n        },\n      \\]}\n      mpn\\=\"925872\"\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\nAlso available: `sku`, `gtin8`, `gtin13`, `gtin14`.\n\nValid values for `offers.itemCondition`:\n\n*   [https://schema.org/DamagedCondition](https://schema.org/DamagedCondition)\n*   [https://schema.org/NewCondition](https://schema.org/NewCondition)\n*   [https://schema.org/RefurbishedCondition](https://schema.org/RefurbishedCondition)\n*   [https://schema.org/UsedCondition](https://schema.org/UsedCondition)\n\nValid values for `offers.availability`:\n\n*   [https://schema.org/Discontinued](https://schema.org/Discontinued)\n*   [https://schema.org/InStock](https://schema.org/InStock)\n*   [https://schema.org/InStoreOnly](https://schema.org/InStoreOnly)\n*   [https://schema.org/LimitedAvailability](https://schema.org/LimitedAvailability)\n*   [https://schema.org/OnlineOnly](https://schema.org/OnlineOnly)\n*   [https://schema.org/OutOfStock](https://schema.org/OutOfStock)\n*   [https://schema.org/PreOrder](https://schema.org/PreOrder)\n*   [https://schema.org/PreSale](https://schema.org/PreSale)\n*   [https://schema.org/SoldOut](https://schema.org/SoldOut)\n\nThe property `aggregateOffer` is also available: (It is ignored if `offers` is set)\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `lowPrice` | The lowest price of all offers available. Use a floating point number. |\n| `priceCurrency` | The currency used to describe the product price, in three-letter ISO 4217 format. |\n\n**Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `highPrice` | The highest price of all offers available. Use a floating point number. |\n| `offerCount` | The number of offers for the product. |\n| `offers` | An offer to transfer some rights to an item or to provide a service. You can provide this as a single object, or an array of objects with the properties below. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\nMore info on the product data type can be found [here](https://developers.google.com/search/docs/data-types/product).\n\n### Social Profile\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#social-profile)\n\nimport { SocialProfileJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Social Profile JSON-LD</h1\\>\n    <SocialProfileJsonLd\n      type\\=\"Person\"\n      name\\=\"your name\"\n      url\\=\"http://www.your-site.com\"\n      sameAs\\={\\[\n        'http://www.facebook.com/your-profile',\n        'http://instagram.com/yourProfile',\n        'http://www.linkedin.com/in/yourprofile',\n        'http://plus.google.com/your\\_profile',\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `type` | Person or Organization |\n| `name` | The name of the person or organization |\n| `url` | The URL for the person's or organization's official website. |\n| `sameAs` | An array of URLs for the person's or organization's official social media profile page(s) |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n**Google Supported Social Profiles**\n\n*   Facebook\n*   Twitter\n*   Google+\n*   Instagram\n*   YouTube\n*   LinkedIn\n*   Myspace\n*   Pinterest\n*   SoundCloud\n*   Tumblr\n\n### News Article\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#news-article)\n\nimport { NewsArticleJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>News Article JSON-LD</h1\\>\n    <NewsArticleJsonLd\n      url\\=\"https://example.com/article\"\n      title\\=\"Article headline\"\n      images\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      section\\=\"politic\"\n      keywords\\=\"prayuth,taksin\"\n      datePublished\\=\"2015-02-05T08:00:00+08:00\"\n      dateModified\\=\"2015-02-05T09:00:00+08:00\"\n      authorName\\=\"Jane Blogs\"\n      publisherName\\=\"Gary Meehan\"\n      publisherLogo\\=\"https://www.example.com/photos/logo.jpg\"\n      description\\=\"This is a mighty good description of this article.\"\n      body\\=\"This is all text for this news article\"\n      isAccessibleForFree\\={true}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n### Park\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#park)\n\nimport { ParkJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Park JSON-LD</h1\\>\n    <ParkJsonLd\n      id\\=\"https://www.example.com/park/minnewaska-state-park\"\n      name\\=\"Minnewaska State Park\"\n      url\\=\"https://www.example.com/park\"\n      telephone\\=\"+18452550752\"\n      images\\={\\['https://example.com/photos/1x1/photo.jpg'\\]}\n      address\\={{\n        streetAddress: '5281 Route 44-55',\n        addressLocality: 'Kerhonkson',\n        addressRegion: 'NY',\n        postalCode: '12446',\n        addressCountry: 'US',\n      }}\n      description\\=\"A wonderful description about Minnewaska State Park\"\n      geo\\={{\n        latitude: '41.735149',\n        longitude: '-74.239037',\n      }}\n      openingHours\\={\\[\n        {\n          opens: '09:00',\n          closes: '18:00',\n          dayOfWeek: \\[\n            'Monday',\n            'Tuesday',\n            'Wednesday',\n            'Thursday',\n            'Friday',\n            'Saturday',\n            'Sunday',\n          \\],\n          validFrom: '2019-12-23',\n          validThrough: '2020-04-02',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `@id` | Globally unique ID of the specific park in the form of a URL. |\n| `address` | Address of the specific park location |\n| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |\n| `address.addressLocality` | City |\n| `address.addressRegion` | State or province, if applicable. |\n| `address.postalCode` | Postal or zip code. |\n| `address.streetAddress` | Street number, street name, and unit number. |\n| `name` | Park name. |\n| `description` | Park description. |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `geo` | Geographic coordinates of the park. |\n| `geo.latitude` | The latitude of the park location |\n| `geo.longitude` | The longitude of the park location |\n| `images` | An image or images of the park. Required for valid markup depending on the type |\n| `telephone` | A business phone number meant to be the primary contact method for customers. |\n| `url` | The fully-qualified URL of the specific park. |\n| `openingHours` | Opening hour specification of the park. You can provide this as a single object, or an array of objects with the properties below. |\n| `openingHours.opens` | The opening hour of the place or service on the given day(s) of the week. |\n| `openingHours.closes` | The closing hour of the place or service on the given day(s) of the week. |\n| `openingHours.dayOfWeek` | The day of the week for which these opening hours are valid. Can be a string or array of strings. Refer to [DayOfWeek](https://schema.org/DayOfWeek) |\n| `openingHours.validFrom` | The date when the item becomes valid. |\n| `openingHours.validThrough` | The date after when the item is not valid. |\n| `isAccessibleForFree` | Whether or not the park is accessible for free. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside oft the app directory. |\n\n[Google Docs for Social Profile](https://developers.google.com/search/docs/data-types/social-profile)\n\n### Video\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#video-1)\n\nimport { VideoJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Video JSON-LD</h1\\>\n    <VideoJsonLd\n      name\\=\"How to make a Party Coffee Cake\"\n      description\\=\"This is how you make a Party Coffee Cake.\"\n      contentUrl\\=\"http://www.example.com/video123.mp4\"\n      embedUrl\\=\"http://www.example.com/videoplayer?video=123\"\n      uploadDate\\=\"2018-02-05T08:00:00+08:00\"\n      duration\\=\"PT1M33S\"\n      thumbnailUrls\\={\\[\n        'https://example.com/photos/1x1/photo.jpg',\n        'https://example.com/photos/4x3/photo.jpg',\n        'https://example.com/photos/16x9/photo.jpg',\n      \\]}\n      expires\\=\"2019-02-05T08:00:00+08:00\"\n      hasPart\\={{\n        name: 'Preheat oven',\n        startOffset: 30,\n        url: 'http://www.example.com/example?t=30',\n      }}\n      watchCount\\={2347}\n      publication\\={{\n        isLiveBroadcast: true,\n        startDate: '2020-10-24T14:00:00+00:00',\n        endDate: '2020-10-24T14:37:14+00:00',\n      }}\n      regionsAllowed\\={\\['IT', 'NL'\\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The title of the video. |\n| `description` | The description of the video. HTML tags are ignored. |\n| `thumbnailUrl` | A URL pointing to the video thumbnail image file. |\n| `uploadDate` | The date the video was first published, in ISO 8601 format. |\n\n**Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `contentUrl` | A URL pointing to the actual video media file, in one of the supported encoding formats. |\n| `duration` | The duration of the video in ISO 8601 format |\n| `embedUrl` | A URL pointing to a player for the specific video. |\n| `expires` | If applicable, the date after which the video will no longer be available. |\n| `interactionStatistic` | The number of times the video has been watched. |\n| `publication` | If your video is happening live and you want to be eligible for the LIVE badge. |\n| `regionsAllowed` | The regions where the video is allowed. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n### VideoGame\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#videogame)\n\nimport { VideoGameJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>VideoGame JSON-LD</h1\\>\n    <VideoGameJsonLd\n      name\\=\"Red Dead Redemption 2\"\n      translatorName\\={\\['Translator 1', 'Translator 2'\\]}\n      languageName\\={\\['English', 'Kurdish'\\]}\n      description\\=\"Arthur Morgan and the Van der Linde gang are outlaws on the run. With federal agents and the best bounty hunters in the nation massing on their heels, the gang must rob, steal and fight their way across the rugged heartland of America in order to survive.\"\n      processorRequirements\\=\"4 GHz\"\n      memoryRequirements\\=\"16 Gb\"\n      playMode\\=\"SinglePlayer\"\n      applicationCategory\\=\"Game\"\n      url\\=\"https://example.com/rdr2-game\"\n      platformName\\={\\['PC game', 'PlayStation 4'\\]}\n      operatingSystemName\\=\"windows\"\n      keywords\\=\"outlaw, gang, federal agents\"\n      datePublished\\=\"2019-02-05T08:00:00+08:00\"\n      image\\=\"https://example.com/photos/1x1/photo.jpg\"\n      publisherName\\=\"Vertical Games\"\n      producerName\\=\"Rockstar Games\"\n      producerUrl\\=\"https//www.example.com/producer\"\n      offers\\={\\[\n        {\n          price: '119.99',\n          priceCurrency: 'USD',\n          priceValidUntil: '2020-11-05',\n          availability: 'https://schema.org/InStock',\n          url: 'https://example.net/rdr2-game',\n          seller: {\n            name: 'Executive Gaming',\n          },\n        },\n        {\n          price: '139.99',\n          priceCurrency: 'CAD',\n          priceValidUntil: '2020-09-05',\n          availability: 'https://schema.org/InStock',\n          url: 'https://example.org/rdr2-game',\n          seller: {\n            name: 'Executive Gaming',\n          },\n        },\n      \\]}\n      aggregateRating\\={{\n        ratingValue: '44',\n        reviewCount: '89',\n        ratingCount: '684',\n        bestRating: '100',\n        worstRating: '1',\n      }}\n      reviews\\={\\[\n        {\n          author: {\n            type: 'Person',\n            name: 'AhmetKaya',\n          },\n          publisher: {\n            type: 'Organization',\n            name: 'Gam Production',\n          },\n          datePublished: '2017-01-06T03:37:40Z',\n          reviewBody: 'Iki gozum.',\n          name: 'Rica ederim.',\n          reviewRating: {\n            bestRating: '5',\n            ratingValue: '5',\n            worstRating: '1',\n          },\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The title of the video game. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n[More information about the schema](https://schema.org/VideoGame)\n\n### Event\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#event)\n\nimport { EventJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Event JSON-LD</h1\\>\n    <EventJsonLd\n      name\\=\"My Event\"\n      startDate\\=\"2020-01-23T00:00:00.000Z\"\n      endDate\\=\"2020-01-24T00:00:00.000Z\"\n      location\\={{\n        name: 'My Place',\n        sameAs: 'https://example.com/my-place',\n        address: {\n          streetAddress: '1600 Saratoga Ave',\n          addressLocality: 'San Jose',\n          addressRegion: 'CA',\n          postalCode: '95129',\n          addressCountry: 'US',\n        },\n      }}\n      url\\=\"https://example.com/my-event\"\n      images\\={\\['https://example.com/photos/photo.jpg'\\]}\n      description\\=\"My event @ my place\"\n      offers\\={\\[\n        {\n          price: '119.99',\n          priceCurrency: 'USD',\n          priceValidUntil: '2020-11-05',\n          itemCondition: 'https://schema.org/UsedCondition',\n          availability: 'https://schema.org/InStock',\n          url: 'https://www.example.com/executive-anvil',\n          seller: {\n            name: 'John Doe',\n          },\n          validFrom: '2020-11-01T00:00:00.000Z',\n        },\n        {\n          price: '139.99',\n          priceCurrency: 'CAD',\n          priceValidUntil: '2020-09-05',\n          itemCondition: 'https://schema.org/UsedCondition',\n          availability: 'https://schema.org/InStock',\n          url: 'https://www.example.ca/executive-anvil',\n          seller: {\n            name: 'John Doe Sr.',\n          },\n          validFrom: '2020-08-05T00:00:00.000Z',\n        },\n      \\]}\n      performers\\={\\[\n        {\n          name: 'Adele',\n        },\n        {\n          name: 'Kira and Morrison',\n        },\n      \\]}\n      organizer\\={{\n        type: 'Organization',\n        name: 'Unnamed organization',\n        url: 'https://www.unnamed.com',\n      }}\n      eventStatus\\=\"EventScheduled\"\n      eventAttendanceMode\\=\"OfflineEventAttendanceMode\"\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The name of the event |\n| `startDate` | The start date time of the event in iso8601 format |\n| `endDate` | The end date time of the event in iso8601 format |\n| `location` | Location of the event, can be `Place` or `VirtualLocation` |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n**`Place` type** Requires `address` property and `name`.\n\n**`VirtualLocation` type** Requires `url` property, doesn't require `name`.\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `description` | Description of the event |\n| `location.name` | Name of the location |\n| `location.sameAs` | URL of a reference web page that identifies location |\n| `images` | An image or images of the event. |\n| `url` | The fully-qualified URL of the event. |\n| `offers` | An offer to transfer some rights to an item or to provide a service. You can provide this as a single object, or an array of objects with the properties below. |\n| `performers` | All artists that perform at this event. You can provide this as a single object, or an array of objects with the properties below. |\n| `performers.name` | The name of the performer |\n| `performers.type` | Either `Person` or `PerformingGroup` |\n| `organizer` | The organizer of the event |\n| `organizer.type` | Either `Organization` or `Person` |\n| `organizer.name` | Name of the organizer of the event |\n| `organizer.url` | URL of the organizer of the event |\n| `eventStatus` | Status of the event, type `EventStatus` |\n| `eventAttendanceMode` | Attendance mode of the event, type `EventAttendanceMode` |\n\n**`EventStatus` type**\n\n*   'EventCancelled'\n*   'EventMovedOnline'\n*   'EventPostponed'\n*   'EventRescheduled'\n*   'EventScheduled'\n\n**`EventAttendanceMode` type**\n\n*   'MixedEventAttendanceMode'\n*   'OfflineEventAttendanceMode'\n*   'OnlineEventAttendanceMode'\n\n**`offers` Required properties**\n\n| Property | Info |\n| --- | --- |\n| `offers.price` | The cost of the offer |\n| `offers.priceCurrency` | The currency of the offer |\n\n**`offers` Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `offers.priceValidUntil` | Until when the price of the offer expires |\n| `offers.itemCondition` | The condition of the product or service |\n| `offers.availability` | The availability of this item — for example In stock, Out of stock, Pre-order, etc. |\n| `offers.url` | URL of the item |\n| `offers.seller` | The person who is selling this item |\n| `offers.seller.name` | The name of the person |\n| `offers.validFrom` | Since when the price of the offer is valid |\n\nThe property `aggregateOffer` is also available: (It is ignored if `offers` is set)\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `lowPrice` | The lowest price of all offers available. Use a floating point number. |\n| `priceCurrency` | The currency used to describe the product price, in three-letter ISO 4217 format. |\n\n**Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `highPrice` | The highest price of all offers available. Use a floating point number. |\n| `offerCount` | The number of offers for the product. |\n\nFor reference and more info check [Google's Search Event DataType](https://developers.google.com/search/docs/data-types/event)\n\n### Q&A\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#qa)\n\nQ&A pages are web pages that contain data in a question-and-answer format, which is one question followed by its answers.\n\nimport { QAPageJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Q&A Page JSON\\-LD</h1\\>\n    <QAPageJsonLd\n      mainEntity\\={{\n        name: 'How many ounces are there in a pound?',\n        text: 'I have taken up a new interest in baking and keep running across directions in ounces and pounds. I have to translate between them and was wondering how many ounces are in a pound?',\n        answerCount: 3,\n        upvoteCount: 26,\n        dateCreated: '2016-07-23T21:11Z',\n        author: {\n          name: 'New Baking User',\n          url: 'https://example.com/bakinguser',\n        },\n        acceptedAnswer: {\n          text: '1 pound (lb) is equal to 16 ounces (oz).',\n          dateCreated: '2016-11-02T21:11Z',\n          upvoteCount: 1337,\n          url: 'https://example.com/question1#acceptedAnswer',\n          author: {\n            name: 'SomeUser',\n            url: 'https://example.com/someuser',\n          },\n        },\n        suggestedAnswer: \\[\n          {\n            text: 'Are you looking for ounces or fluid ounces? If you are looking for fluid ounces there are 15.34 fluid ounces in a pound of water.',\n            dateCreated: '2016-11-02T21:11Z',\n            upvoteCount: 42,\n            url: 'https://example.com/question1#suggestedAnswer1',\n            author: {\n              name: 'AnotherUser',\n              url: 'https://example.com/anotheruser',\n            },\n          },\n          {\n            text: \\`I can't remember exactly, but I think 18 ounces in a lb. You might want to double check that.\\`,\n            dateCreated: '2016-11-06T21:11Z',\n            upvoteCount: 0,\n            url: 'https://example.com/question1#suggestedAnswer2',\n            author: {\n              name: 'ConfusedUser',\n              url: 'https://example.com/confuseduser',\n            },\n          },\n        \\],\n      }}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `mainEntity` | The Question for this page must be nested under the mainEntity property of the QAPageJsonld component. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n**`mainEntity` Required properties**\n\n| Property | Info |\n| --- | --- |\n| `answerCount` | The total number of answers to the question. |\n| `acceptedAnswer` or `suggestedAnswer` | To be eligible for the rich result, a question must have at least one answer – either an acceptedAnswer or a suggestedAnswer. |\n| `name` | The full text of the short form of the question. |\n\n**`mainEntity` Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `author` | The author of the question. |\n| `dateCreated` | The date at which the question was added to the page, in ISO-8601 format. |\n| `text` | The full text of the long form of the question. |\n| `upvoteCount` | The total number of votes that this question has received. |\n\n**`acceptedAnswer`/`suggestedAnswer` Required properties**\n\n| Property | Info |\n| --- | --- |\n| `text` | The full text of the answer. |\n\n**`acceptedAnswer`/`suggestedAnswer` Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `author` | The author of the question. |\n| `dateCreated` | The date at which the question was added to the page, in ISO-8601 format. |\n| `upvoteCount` | The total number of votes that this question has received. |\n| `url` | A URL that links directly to this answer. |\n\nFor reference and more info check [Google's Search Q&A DataType](https://developers.google.com/search/docs/data-types/qapage)\n\n### Collection Page\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#collection-page)\n\nCollection pages are web pages. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as breadcrumb may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an item scope, they will be assumed to be about the page.\n\nimport { CollectionPageJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Collection Page JSON-LD</h1\\>\n    <CollectionPageJsonLd\n      name\\=\"Resistance 3: Fall of Man\"\n      hasPart\\={\\[\n        {\n          about:\n            'Britten Four Sea Interludes and Passacaglia from Peter Grimes',\n          author: 'John Doe',\n          name: 'Schema.org Ontology',\n          datePublished: '2021-03-09',\n          audience: 'Internet',\n          keywords: 'schema',\n          thumbnailUrl: 'https://i.ytimg.com/vi/eXSJ3PO9Tas/hqdefault.jpg',\n          image: 'hqdefault.jpg',\n        },\n        {\n          about: 'Shostakovich Symphony No. 7 (Leningrad)',\n          author: 'John Smith',\n          name: 'Creative work name',\n          datePublished: '2014-10-01T19:30',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The name of the item. |\n| `hasPart` | Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense). |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `hasPart.creativeWork` | The most generic kind of [creative work](https://schema.org/CreativeWork), including books, movies, photographs, software programs, etc |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n**`creativeWork` Required properties**\n\n| Property | Info |\n| --- | --- |\n| `hasPart.creativeWork.author` | The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably. |\n| `hasPart.creativeWork.about` | The subject matter of the content. |\n| `hasPart.creativeWork.datePublished` | Date of first broadcast/publication. |\n| `hasPart.creativeWork.name` | The name of the item. |\n\n**`creativeWork` Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `hasPart.creativeWork.audience` | An intended audience, i.e. a group for whom something was created. |\n| `hasPart.creativeWork.keywords` | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas. |\n| `hasPart.creativeWork.thumbnailUrl` | A thumbnail image relevant to the Thing. |\n| `hasPart.creativeWork.image` | An image of the item. This can be a URL or a fully described ImageObject. |\n\nFor reference and more info check [Collection Page DataType](https://schema.org/CollectionPage)\n\n### Profile page\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#profile-page)\n\nProfile pages are web pages. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as breadcrumb may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an item scope, they will be assumed to be about the page.\n\nimport { ProfilePageJsonLd } from 'next-seo';\n\nconst Page \\= () \\=\\> (\n  <\\>\n    <h1\\>Profile page JSON-LD</h1\\>\n    <ProfilePageJsonLd\n      lastReviewed\\=\"2014-10-01T19:30\"\n      breadcrumb\\={\\[\n        {\n          position: 1,\n          name: 'Books',\n          item: 'https://example.com/books',\n        },\n        {\n          position: 2,\n          name: 'Authors',\n          item: 'https://example.com/books/authors',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\nexport default Page;\n\n**Required properties**\n\n| Property | Info |\n| --- | --- |\n| `breadcrumb` | A set of links that can help a user understand and navigate a website hierarchy represented as string or [BreadcrumbList](https://github.com/garmeeh/next-seo?screenshot=true#breadcrumb). |\n\n**Supported properties**\n\n| Property | Info |\n| --- | --- |\n| `lastReviewed` | Date on which the content on this web page was last reviewed for accuracy and/or completeness. |\n\n**Other** | `useAppDir` | This should be set to true if using new app directory. Not required if outside of app directory. |\n\nFor reference and more info check [Profile Page DataType](https://schema.org/ProfilePage)\n\n### Carousel\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#carousel)\n\n**Required properties of Carousel Component**\n\n| Property | Info |\n| --- | --- |\n| `type` | The type of carousel |\n| `data` | The data in the form of an array for the item list in the carousel |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n#### Default (Summary List)\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#default-summary-list)\n\nimport React from 'react';\nimport { CarouselJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Carousel Default JSON-LD</h1\\>\n    <CarouselJsonLd\n      ofType\\=\"default\"\n      data\\={\\[\n        { url: 'http://example.com/peanut-butter-cookies.html' },\n        {\n          url: 'http://example.com/triple-chocolate-chunk.html',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `url` | URL of the item's detailed page. |\n\n#### Course\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#course-1)\n\nimport React from 'react';\nimport { CarouselJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Carousel Course JSON-LD</h1\\>\n    <CarouselJsonLd\n      ofType\\=\"course\"\n      data\\={\\[\n        {\n          courseName: 'Course 1',\n          description: 'Course 1 Description',\n          providerName: 'Course Provider',\n          url: 'http://example.com/course-1.html',\n        },\n        {\n          courseName: 'Course 2',\n          description: 'Course 2 Description',\n          providerName: 'Course Provider',\n          url: 'http://example.com/course-2.html',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `courseName` | The title of the course. |\n| `description` | A description of the course. Display limit of 60 characters. |\n| `providerName` | The course provider name. |\n| `url` | URL of the item's detailed page . |\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `providerUrl` | The url to the course provider. |\n\n#### Movie\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#movie)\n\nimport React from 'react';\nimport { CarouselJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Carousel Movie JSON-LD</h1\\>\n    <CarouselJsonLd\n      ofType\\=\"movie\"\n      data\\={\\[\n        {\n          name: 'Movie 1',\n          url: 'http://example.com/movie-1.html',\n          image:\n            'https://i.pinimg.com/originals/96/a0/0d/96a00d42b0ff8f80b7cdf2926a211e47.jpg',\n          director: {\n            name: 'John Doe',\n          },\n          review: {\n            author: { type: 'Person', name: 'Ronan Farrow' },\n            reviewBody:\n              'Heartbreaking, inpsiring, moving. Bradley Cooper is a triple threat.',\n            reviewRating: { ratingValue: '5' },\n          },\n        },\n        {\n          name: 'Movie 2',\n          url: 'http://example.com/movie-1.html',\n          image:\n            'https://i.pinimg.com/originals/96/a0/0d/96a00d42b0ff8f80b7cdf2926a211e47.jpg',\n          director: \\[\n            {\n              name: 'Mary Doe',\n            },\n            {\n              name: 'John Doe',\n            },\n          \\],\n          review: {\n            author: { type: 'Person', name: 'Ronan Farrow' },\n            reviewBody:\n              'Heartbreaking, inpsiring, moving. Rowan Atkinson is a triple threat.',\n            reviewRating: { ratingValue: '5' },\n          },\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | Name of the movie. |\n| `image` | An image that represents the movie. |\n| `url` | URL of the item's detailed page. |\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `director` | The directors of the movie. |\n| `dateCreated` | The date the movie was released. |\n| `aggregateRating` | Aggregate Rating object for the movie. |\n| `review` | Review for the movie. |\n\n#### Recipe\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#recipe-1)\n\nimport React from 'react';\nimport { CarouselJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Carousel Recipe JSON-LD</h1\\>\n    <CarouselJsonLd\n      ofType\\=\"recipe\"\n      data\\={\\[\n        {\n          name: 'Party Coffee Cake',\n          url: 'http://example.com/recipe-1.html',\n          images: \\[\n            'https://example.com/photos/1x1/photo.jpg',\n            'https://example.com/photos/4x3/photo.jpg',\n            'https://example.com/photos/16x9/photo.jpg',\n          \\],\n          authorName: 'Mary Stone',\n          datePublished: '2018-03-10',\n          description: 'This coffee cake is awesome and perfect for parties.',\n          prepTime: 'PT20M',\n          cookTime: 'PT30M',\n          totalTime: 'PT50M',\n          keywords: 'cake for a party, coffee',\n          yields: '10',\n          category: 'Dessert',\n          calories: 270,\n          cuisine: 'American',\n          ingredients: \\[\n            '2 cups of flour',\n            '3/4 cup white sugar',\n            '2 teaspoons baking powder',\n            '1/2 teaspoon salt',\n            '1/2 cup butter',\n            '2 eggs',\n            '3/4 cup milk',\n          \\],\n          instructions: \\[\n            {\n              name: 'Preheat',\n              text: 'Preheat the oven to 350 degrees F. Grease and flour a 9x9 inch pan.',\n              url: 'https://example.com/party-coffee-cake#step1',\n              image: 'https://example.com/photos/party-coffee-cake/step1.jpg',\n            },\n            {\n              name: 'Mix dry ingredients',\n              text: 'In a large bowl, combine flour, sugar, baking powder, and salt.',\n              url: 'https://example.com/party-coffee-cake#step2',\n              image: 'https://example.com/photos/party-coffee-cake/step2.jpg',\n            },\n            {\n              name: 'Spread into pan',\n              text: 'Spread into the prepared pan.',\n              url: 'https://example.com/party-coffee-cake#step4',\n              image: 'https://example.com/photos/party-coffee-cake/step4.jpg',\n            },\n            {\n              name: 'Bake',\n              text: 'Bake for 30 to 35 minutes, or until firm.',\n              url: 'https://example.com/party-coffee-cake#step5',\n              image: 'https://example.com/photos/party-coffee-cake/step5.jpg',\n            },\n          \\],\n          aggregateRating: {\n            ratingValue: '5',\n            ratingCount: '18',\n          },\n          video: {\n            name: 'How to make a Party Coffee Cake',\n            description: 'This is how you make a Party Coffee Cake.',\n            thumbnailUrls: \\[\n              'https://example.com/photos/1x1/photo.jpg',\n              'https://example.com/photos/4x3/photo.jpg',\n              'https://example.com/photos/16x9/photo.jpg',\n            \\],\n            contentUrl: 'http://www.example.com/video123.mp4',\n            embedUrl: 'http://www.example.com/videoplayer?video=123',\n            uploadDate: '2018-02-05T08:00:00+08:00',\n            duration: 'PT1M33S',\n            expires: '2019-02-05T08:00:00+08:00',\n          },\n        },\n        {\n          name: 'Party Coffee Cake 2',\n          url: 'http://example.com/recipe-2.html',\n          images: \\[\n            'https://example.com/photos/1x1/photo.jpg',\n            'https://example.com/photos/4x3/photo.jpg',\n            'https://example.com/photos/16x9/photo.jpg',\n          \\],\n          authorName: 'Mary Stone 2',\n          datePublished: '2018-03-10',\n          description: 'This coffee cake is awesome and perfect for parties.',\n          prepTime: 'PT20M',\n          cookTime: 'PT30M',\n          totalTime: 'PT50M',\n          keywords: 'cake for a party, coffee',\n          yields: '10',\n          category: 'Dessert',\n          calories: 270,\n          cuisine: 'American',\n          ingredients: \\[\n            '2 cups of flour',\n            '3/4 cup white sugar',\n            '2 teaspoons baking powder',\n            '1/2 teaspoon salt',\n            '1/2 cup butter',\n            '2 eggs',\n            '3/4 cup milk',\n          \\],\n          instructions: \\[\n            {\n              name: 'Preheat',\n              text: 'Preheat the oven to 350 degrees F. Grease and flour a 9x9 inch pan.',\n              url: 'https://example.com/party-coffee-cake#step1',\n              image: 'https://example.com/photos/party-coffee-cake/step1.jpg',\n            },\n            {\n              name: 'Mix dry ingredients',\n              text: 'In a large bowl, combine flour, sugar, baking powder, and salt.',\n              url: 'https://example.com/party-coffee-cake#step2',\n              image: 'https://example.com/photos/party-coffee-cake/step2.jpg',\n            },\n            {\n              name: 'Spread into pan',\n              text: 'Spread into the prepared pan.',\n              url: 'https://example.com/party-coffee-cake#step4',\n              image: 'https://example.com/photos/party-coffee-cake/step4.jpg',\n            },\n            {\n              name: 'Bake',\n              text: 'Bake for 30 to 35 minutes, or until firm.',\n              url: 'https://example.com/party-coffee-cake#step5',\n              image: 'https://example.com/photos/party-coffee-cake/step5.jpg',\n            },\n          \\],\n          aggregateRating: {\n            ratingValue: '5',\n            ratingCount: '18',\n          },\n          video: {\n            name: 'How to make a Party Coffee Cake',\n            description: 'This is how you make a Party Coffee Cake.',\n            thumbnailUrls: \\[\n              'https://example.com/photos/1x1/photo.jpg',\n              'https://example.com/photos/4x3/photo.jpg',\n              'https://example.com/photos/16x9/photo.jpg',\n            \\],\n            contentUrl: 'http://www.example.com/video123.mp4',\n            embedUrl: 'http://www.example.com/videoplayer?video=123',\n            uploadDate: '2018-02-05T08:00:00+08:00',\n            duration: 'PT1M33S',\n            expires: '2019-02-05T08:00:00+08:00',\n          },\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The name of the dish. |\n| `description` | A description of the recipe |\n| `authorName` | The name of the recipe author |\n| `ingredients` | A list of ingredient strings |\n| `instructions` | \\- |\n| `instructions.name` | The name of the instruction step. |\n| `instructions.text` | The directions of the instruction step. |\n| `url` | URL of the item's detailed page. |\n\n#### Custom\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#custom)\n\nimport React from 'react';\nimport { CarouselJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Carousel Custom JSON-LD</h1\\>\n    <CarouselJsonLd\n      ofType\\=\"custom\"\n      url\\=\"http://example.com/custom-carousel.html\"\n      name\\=\"Carousel Custom\"\n      description\\=\"Custom Carousel Description\"\n      data\\={\\[\n        {\n          position: 1,\n          type: 'CustomList',\n          name: 'Custom 1',\n        },\n        {\n          position: 2,\n          type: 'CustomList',\n          name: 'Custom 2',\n        },\n      \\]}\n    /\\>\n  </\\>\n);\n\n**Data Required Properties**\n\n| Property | Info |\n| --- | --- |\n| `type` | Type of the item. |\n| `name` | Name of the item. |\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `position` | Position of the item. If not pass property, it will increase regularly. |\n\n### Software App\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#software-app)\n\nimport React from 'react';\nimport { SoftwareAppJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Software App JSON-LD</h1\\>\n    <SoftwareAppJsonLd\n      name\\=\"Angry Birds\"\n      price\\=\"1.00\"\n      priceCurrency\\=\"USD\"\n      aggregateRating\\={{ ratingValue: '4.6', reviewCount: '8864' }}\n      operatingSystem\\=\"ANDROID\"\n      applicationCategory\\=\"GameApplication\"\n      keywords\\=\"angrybirds, arcade, slingshot\"\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The name of the app. |\n| `price` | Price of the app. If the app is free of charge, set offers.price to 0 |\n| `priceCurrency` | If the app has a price greater than 0, you must include offers.currency. |\n| `aggregateRating` | The average review score of the app. (Not required if review is present.) |\n| `review` | A single review of the app. (Not required if aggregateRating is present.) |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `operatingSystem` | The operating System supported by the game it self. |\n| `applicationCategory` | Desktop Software or Video Game... |\n\n**Data other properties**\n\n| Property | Info |\n| --- | --- |\n| `keywords` | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas. |\n\nFor reference and more info check [Google docs for Software App](https://developers.google.com/search/docs/data-types/software-app) and [Schema.org docs](https://schema.org/SoftwareApplication)\n\n### Organization\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#organization)\n\nimport React from 'react';\nimport { OrganizationJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Organization JSON-LD</h1\\>\n    <OrganizationJsonLd\n      type\\=\"Corporation\"\n      id\\=\"https://www.purpule-fox.io/#corporation\"\n      logo\\=\"https://www.example.com/photos/logo.jpg\"\n      legalName\\=\"Purple Fox LLC\"\n      name\\=\"Purple Fox\"\n      address\\={{\n        streetAddress: '1600 Saratoga Ave',\n        addressLocality: 'San Jose',\n        addressRegion: 'CA',\n        postalCode: '95129',\n        addressCountry: 'US',\n      }}\n      contactPoint\\={\\[\n        {\n          telephone: '+1-401-555-1212',\n          contactType: 'customer service',\n          email: 'customerservice@email.com',\n          areaServed: 'US',\n          availableLanguage: \\['English', 'Spanish', 'French'\\],\n        },\n        {\n          telephone: '+1-877-746-0909',\n          contactType: 'customer service',\n          email: 'servicecustomer@email.com',\n          contactOption: 'TollFree',\n          availableLanguage: 'English',\n        },\n        {\n          telephone: '+1-877-453-1304',\n          contactType: 'technical support',\n          contactOption: 'TollFree',\n          areaServed: \\['US', 'CA'\\],\n          availableLanguage: \\['English', 'French'\\],\n        },\n      \\]}\n      sameAs\\={\\['https://www.orange-fox.com'\\]}\n      url\\=\"https://www.purpule-fox.io/\"\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `name` | The name of the Organization. |\n| `url` | Url of the organization |\n| `contactPoint` |  |\n| `contactPoint.telephone` | An internationalized version of the phone number, starting with the \"+\" symbol and country code |\n| `contactPoint.contactType` | Description of the purpose of the phone number i.e. `Technical Support`. |\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `logo` | ImageObject or URL an associated logo to the Organization. |\n| `type` | Organization type, check [here](https://schema.org/Organization#subtypes) |\n| `legalName` | The official name of the organization, e.g. the registered company name. |\n| `sameAs` | URL of a reference Web page that unambiguously indicates the item's identity. |\n| `address` | Address of the specific business location |\n| `address.addressCountry` | The 2-letter ISO 3166-1 alpha-2 country code |\n| `address.addressLocality` | City |\n| `address.addressRegion` | State or province, if applicable. |\n| `address.postalCode` | Postal or zip code. |\n| `address.streetAddress` | Street number, street name, and unit number. |\n| `contactPoint.areaServed` | `String` or `Array` of geographical regions served by the business. Example `\"US\"` or `[\"US\", \"CA\", \"MX\"]` |\n| `contactPoint.availableLanguage` | Details about the language spoken. Example `\"English\"` or `[\"English\", \"French\"]` |\n| `contactPoint.email` | Email asscosiated with the business\\` |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\nFor reference and more info check [Docs](https://schema.org/Organization)\n\n### Brand\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#brand)\n\nimport React from 'react';\nimport { BrandJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>Brand JSON-LD</h1\\>\n    <BrandJsonLd\n      slogan\\=\"What does the fox say?\"\n      id\\=\"https://www.purpule-fox.io/#corporation\"\n      logo\\=\"https://www.example.com/photos/logo.jpg\"\n      aggregateRating\\={{\n        ratingValue: '5',\n        ratingCount: '18',\n      }}\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `id` | 'URL to main entity of page' |\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `logo` | ImageObject or URL an associated logo to the Organization. |\n| `slogan` | A slogan or motto associated with the item. |\n| `aggregateRating.ratingValue` | The rating for the content.(Check the [reference](https://schema.org/ratingValue) |\n| `aggregateRating.ratingCount` | The count of total number of ratings. |\n| `aggregateRating.reviewCount` | The count of total number of reviews. |\n| `aggregateRating.bestRating` | The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed. |\n| `aggregateRating.worstRating` | The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\nFor reference and more info check [Docs](https://schema.org/Brand)\n\n### WebPage\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#webpage)\n\nimport React from 'react';\nimport { WebPageJsonLd } from 'next-seo';\n\nexport default () \\=\\> (\n  <\\>\n    <h1\\>WebPage JSON-LD</h1\\>\n    <WebPageJsonLd\n      description\\=\"What does the fox say?\"\n      id\\=\"https://www.purpule-fox.io/#corporation\"\n      lastReviewed\\=\"2021-05-26T05:59:02.085Z\"\n      reviewedBy\\={{\n        type: 'Person',\n        name: 'Garmeeh',\n      }}\n    /\\>\n  </\\>\n);\n\n**Data required properties**\n\n| Property | Info |\n| --- | --- |\n| `id` | 'URL to main entity of page' |\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `description` | ImageObject or URL an associated logo to the Organization. |\n| `lastReviewed` | Date on which the content on this web page was last reviewed for accuracy and/or completeness. |\n| `reviewedBy.type` | People or organizations that will review the content of the web page. |\n| `reviewedBy.name` | Name of the entity that have reviewed the content on this web page for accuracy and/or completeness. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\nFor reference and more info check [Docs](https://schema.org/WebPage)\n\n### Image Metadata\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#image-metadata)\n\nimport React from 'react';\nimport { ImageJsonLd } from 'next-seo';\n\nfunction Image() {\n  return (\n    <\\>\n      <h1\\>Image</h1\\>\n      <ImageJsonLd\n        images\\={\\[\n          {\n            contentUrl: 'http://www.example.com/images/image.png',\n            creator: {\n              '@type': 'Person',\n              name: 'Jane Doe',\n            },\n            creditText: 'Jane Doe',\n            copyrightNotice: '© Jane Doe',\n            license: 'http://www.example.com/license',\n            acquireLicensePage: 'http://www.example.com/acquire-license',\n          },\n        \\]}\n      /\\>\n    </\\>\n  );\n}\n\nexport default Image;\n\n**Data Recommended properties**\n\n| Property | Info |\n| --- | --- |\n| `contentUrl` | A URL to the actual image content. Google uses contentUrl to determine which image the photo metadata applies to. |\n| `creator.name` | The name of the creator. |\n| `creditText` | The name of person and/or organization that is credited for the image when it's published. |\n| `copyrightNotice` | The copyright notice for claiming the intellectual property for this photograph. This identifies the current owner of the copyright for the photograph. |\n| `license` | A URL to a page that describes the license governing an image's use. For example, it could be the terms and conditions that you have on your website. |\n| `acquireLicensePage` | A URL to a page where the user can find information on how to license that image. |\n\n**Other** | `useAppDir` | This should be set to true if using the new app directory. Not required if outside of the app directory. |\n\nFor reference and more info check [Google Docs](https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata)\n\nContributors\n------------\n\n[](https://github.com/garmeeh/next-seo?screenshot=true#contributors)\n\n[Contributing Guide](https://github.com/garmeeh/next-seo/blob/master/CONTRIBUTING.md)\n\nA massive thank you to [everyone who contributes](https://github.com/garmeeh/next-seo/graphs/contributors) to this project 👏",
  "usage": {
    "tokens": 32885
  }
}
```
