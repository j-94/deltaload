---
title: GitHub - joshbuchea/HEAD: A simple guide to HTML <head> elements
description: A simple guide to HTML <head> elements. Contribute to joshbuchea/HEAD development by creating an account on GitHub.
url: https://github.com/joshbuchea/HEAD
timestamp: 2025-01-20T15:30:19.231Z
domain: github.com
path: joshbuchea_HEAD
---

# GitHub - joshbuchea/HEAD: A simple guide to HTML <head> elements


A simple guide to HTML <head> elements. Contribute to joshbuchea/HEAD development by creating an account on GitHub.


## Content

🤯 HEAD
-------

[](https://github.com/joshbuchea/HEAD?screenshot=true#-head)

> A simple guide to HTML `<head>` elements

[![Image 25: Contributors](https://camo.githubusercontent.com/08304f1a42bc10f5af409ea1ac74bf4529cb396f0342a1dbfab140706b9fbb64/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f6a6f73686275636865612f686561642e7376673f7374796c653d666f722d7468652d6261646765)](https://github.com/joshbuchea/HEAD/graphs/contributors) [![Image 26: CC0](https://camo.githubusercontent.com/4589d411564dd50f3db15ea3596aae2dfbb7c82c9f3371287e5617c61b9f6c0e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4343302d677265656e2e7376673f7374796c653d666f722d7468652d6261646765)](https://creativecommons.org/publicdomain/zero/1.0/) [![Image 27: Follow @joshbuchea on Mastodon](https://camo.githubusercontent.com/85f22422b6460a86fdd6c801e13636b8279f4e5116c955d895c0244846c447aa/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466f6c6c6f775f406a6f73686275636865612d707572706c653f6c6f676f3d6d6173746f646f6e266c6f676f436f6c6f723d7768697465267374796c653d666f722d7468652d6261646765)](https://hachyderm.io/@joshbuchea)

Table of Contents
-----------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)

*   [Recommended Minimum](https://github.com/joshbuchea/HEAD?screenshot=true#recommended-minimum)
*   [Elements](https://github.com/joshbuchea/HEAD?screenshot=true#elements)
*   [Meta](https://github.com/joshbuchea/HEAD?screenshot=true#meta)
*   [Link](https://github.com/joshbuchea/HEAD?screenshot=true#link)
*   [Icons](https://github.com/joshbuchea/HEAD?screenshot=true#icons)
*   [Social](https://github.com/joshbuchea/HEAD?screenshot=true#social)
    *   [Facebook Open Graph](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-open-graph)
    *   [Twitter Card](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-card)
    *   [Twitter Privacy](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-privacy)
    *   [Schema.org](https://github.com/joshbuchea/HEAD?screenshot=true#schemaorg)
    *   [Pinterest](https://github.com/joshbuchea/HEAD?screenshot=true#pinterest)
    *   [Facebook Instant Articles](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-instant-articles)
    *   [OEmbed](https://github.com/joshbuchea/HEAD?screenshot=true#oembed)
    *   [QQ/Wechat](https://github.com/joshbuchea/HEAD?screenshot=true#qqwechat)
*   [Browsers / Platforms](https://github.com/joshbuchea/HEAD?screenshot=true#browsers--platforms)
    *   [Apple iOS](https://github.com/joshbuchea/HEAD?screenshot=true#apple-ios)
    *   [Google Android](https://github.com/joshbuchea/HEAD?screenshot=true#google-android)
    *   [Google Chrome](https://github.com/joshbuchea/HEAD?screenshot=true#google-chrome)
    *   [Microsoft Internet Explorer](https://github.com/joshbuchea/HEAD?screenshot=true#microsoft-internet-explorer)
*   [Browsers (Chinese)](https://github.com/joshbuchea/HEAD?screenshot=true#browsers-chinese)
    *   [360 Browser](https://github.com/joshbuchea/HEAD?screenshot=true#360-browser)
    *   [QQ Mobile Browser](https://github.com/joshbuchea/HEAD?screenshot=true#qq-mobile-browser)
    *   [UC Mobile Browser](https://github.com/joshbuchea/HEAD?screenshot=true#uc-mobile-browser)
*   [App Links](https://github.com/joshbuchea/HEAD?screenshot=true#app-links)
*   [Other Resources](https://github.com/joshbuchea/HEAD?screenshot=true#other-resources)
*   [Related Projects](https://github.com/joshbuchea/HEAD?screenshot=true#related-projects)
*   [Other Formats](https://github.com/joshbuchea/HEAD?screenshot=true#other-formats)
*   [Translations](https://github.com/joshbuchea/HEAD?screenshot=true#-translations)
*   [Contributing](https://github.com/joshbuchea/HEAD?screenshot=true#-contributing)
    *   [Contributors](https://github.com/joshbuchea/HEAD?screenshot=true#contributors)
*   [Author](https://github.com/joshbuchea/HEAD?screenshot=true#-author)
*   [License](https://github.com/joshbuchea/HEAD?screenshot=true#-license)

Recommended Minimum
-------------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#recommended-minimum)

Below are the essential elements for any web document (websites/apps):

<meta charset\="utf-8"\>
<meta name\="viewport" content\="width=device-width, initial-scale=1"\>
<!--
  The above 2 meta tags \*must\* come first in the <head\>
  to consistently ensure proper document rendering.
  Any other head element should come \*after\* these tags.
 --\>
<title\>Page Title</title\>

`meta charset` - defines the encoding of the website, `utf-8` is the standard

`meta name="viewport"` - viewport settings related to mobile responsiveness

`width=device-width` - use the physical width of the device (great for mobile!)

`initial-scale=1` - the initial zoom, 1 means no zoom

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Elements
--------

[](https://github.com/joshbuchea/HEAD?screenshot=true#elements)

Valid `<head>` elements include `meta`, `link`, `title`, `style`, `script`, `noscript`, and `base`.

These elements provide information for how a document should be perceived, and rendered, by web technologies. e.g. browsers, search engines, bots, etc.

<!--
  Set the character encoding for this document, so that
  all characters within the UTF-8 space (such as emoji)
  are rendered correctly.
\--\>
<meta charset\="utf-8"\>

<!-- Set the document's title --\>
<title\>Page Title</title\>

<!-- Set the base URL for all relative URLs within the document --\>
<base href\="https://example.com/page.html"\>

<!-- Link to an external CSS file --\>
<link rel\="stylesheet" href\="styles.css"\>

<!-- Used for adding in-document CSS --\>
<style\>
  /\* ... \*/
</style\>

<!-- JavaScript & No-JavaScript tags --\>
<script src\="script.js"\></script\>
<script\>
  // function(s) go here
</script\>
<noscript\>
  <!-- No JS alternative --\>
</noscript\>

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Meta
----

[](https://github.com/joshbuchea/HEAD?screenshot=true#meta)

<!--
  The following 2 meta tags \*must\* come first in the <head\>
  to consistently ensure proper document rendering.
  Any other head element should come \*after\* these tags.
\--\>
<meta charset\="utf-8"\>
<meta name\="viewport" content\="width=device-width, initial-scale=1"\>

<!--
  Allows control over where resources are loaded from.
  Place as early in the <head\> as possible, as the tag  
  only applies to resources that are declared after it.
\--\>
<meta http-equiv\="Content-Security-Policy" content\="default-src 'self'"\>

<!-- Name of web application (only should be used if the website is used as an app) --\>
<meta name\="application-name" content\="Application Name"\>

<!-- Theme Color for Chrome, Firefox OS and Opera --\>
<meta name\="theme-color" content\="#4285f4"\>

<!-- Short description of the document (limit to 150 characters) --\>
<!-- This content \*may\* be used as a part of search engine results. --\>
<meta name\="description" content\="A description of the page"\>

<!-- Control the behavior of search engine crawling and indexing --\>
<meta name\="robots" content\="index,follow"\><!-- All Search Engines --\>
<meta name\="googlebot" content\="index,follow"\><!-- Google Specific --\>

<!-- Tells Google not to show the sitelinks search box --\>
<meta name\="google" content\="nositelinkssearchbox"\>

<!-- Tells Google not to provide a translation for this document --\>
<meta name\="google" content\="notranslate"\>

<!-- Verify website ownership --\>
<meta name\="google-site-verification" content\="verification\_token"\><!-- Google Search Console --\>
<meta name\="yandex-verification" content\="verification\_token"\><!-- Yandex Webmasters --\>
<meta name\="msvalidate.01" content\="verification\_token"\><!-- Bing Webmaster Center --\>
<meta name\="alexaVerifyID" content\="verification\_token"\><!-- Alexa Console --\>
<meta name\="p:domain\_verify" content\="code\_from\_pinterest"\><!-- Pinterest Console--\>
<meta name\="norton-safeweb-site-verification" content\="norton\_code"\><!-- Norton Safe Web --\>

<!-- Identify the software used to build the document (i.e. - WordPress, Dreamweaver) --\>
<meta name\="generator" content\="program"\>

<!-- Short description of your document's subject --\>
<meta name\="subject" content\="your document's subject"\>

<!-- Gives a general age rating based on the document's content --\>
<meta name\="rating" content\="General"\>

<!-- Allows control over how referrer information is passed --\>
<meta name\="referrer" content\="no-referrer"\>

<!-- Disable automatic detection and formatting of possible phone numbers --\>
<meta name\="format-detection" content\="telephone=no"\>

<!-- Completely opt out of DNS prefetching by setting to "off" --\>
<meta http-equiv\="x-dns-prefetch-control" content\="off"\>

<!-- Specifies the document to appear in a specific frame --\>
<meta http-equiv\="Window-Target" content\="\_value"\>

<!-- Geo tags --\>
<meta name\="ICBM" content\="latitude, longitude"\>
<meta name\="geo.position" content\="latitude;longitude"\>
<meta name\="geo.region" content\="country\[-state\]"\><!-- Country code (ISO 3166-1): mandatory, state code (ISO 3166-2): optional; eg. content="US" / content="US-NY" --\>
<meta name\="geo.placename" content\="city/town"\><!-- eg. content="New York City" --\>

<!-- Web Monetization https://webmonetization.org/docs/getting-started --\>
<meta name\="monetization" content\="$paymentpointer.example"\>

*   📖 [Meta tags that Google understands](https://support.google.com/webmasters/answer/79812?hl=en)
*   📖 [WHATWG Wiki: MetaExtensions](https://wiki.whatwg.org/wiki/MetaExtensions)
*   📖 [ICBM on Wikipedia](https://en.wikipedia.org/wiki/ICBM_address#Modern_use)
*   📖 [Geotagging on Wikipedia](https://en.wikipedia.org/wiki/Geotagging#HTML_pages)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Link
----

[](https://github.com/joshbuchea/HEAD?screenshot=true#link)

<!-- Points to an external stylesheet --\>
<link rel\="stylesheet" href\="https://example.com/styles.css"\>

<!-- Helps prevent duplicate content issues --\>
<link rel\="canonical" href\="https://example.com/article/?page=2"\>

<!-- Links to an AMP HTML version of the current document --\>
<link rel\="amphtml" href\="https://example.com/path/to/amp-version.html"\>

<!-- Links to a JSON file that specifies "installation" credentials for the web applications --\>
<link rel\="manifest" href\="manifest.json"\>

<!-- Links to information about the author(s) of the document --\>
<link rel\="author" href\="humans.txt"\>

<!-- Refers to a copyright statement that applies to the link's context --\>
<link rel\="license" href\="copyright.html"\>

<!-- Gives a reference to a location in your document that may be in another language --\>
<link rel\="alternate" href\="https://es.example.com/" hreflang\="es"\>

<!-- Provides information about an author or another person --\>
<link rel\="me" href\="https://google.com/profiles/thenextweb" type\="text/html"\>
<link rel\="me" href\="mailto:name@example.com"\>
<link rel\="me" href\="sms:+15035550125"\>

<!-- Links to a document that describes a collection of records, documents, or other materials of historical interest --\>
<link rel\="archives" href\="https://example.com/archives/"\>

<!-- Links to top level resource in an hierarchical structure --\>
<link rel\="index" href\="https://example.com/article/"\>

<!-- Provides a self reference - useful when the document has multiple possible references --\>
<link rel\="self" type\="application/atom+xml" href\="https://example.com/atom.xml"\>

<!-- The first, last, previous, and next documents in a series of documents, respectively --\>
<link rel\="first" href\="https://example.com/article/"\>
<link rel\="last" href\="https://example.com/article/?page=42"\>
<link rel\="prev" href\="https://example.com/article/?page=1"\>
<link rel\="next" href\="https://example.com/article/?page=3"\>

<!-- Used when a 3rd party service is utilized to maintain a blog --\>
<link rel\="EditURI" href\="https://example.com/xmlrpc.php?rsd" type\="application/rsd+xml" title\="RSD"\>

<!-- Forms an automated comment when another WordPress blog links to your WordPress blog or post --\>
<link rel\="pingback" href\="https://example.com/xmlrpc.php"\>

<!-- Notifies a URL when you link to it on your document --\>
<link rel\="webmention" href\="https://example.com/webmention"\>

<!-- Enables posting to your own domain using a Micropub client --\>
<link rel\="micropub" href\="https://example.com/micropub"\>

<!-- Open Search --\>
<link rel\="search" href\="/open-search.xml" type\="application/opensearchdescription+xml" title\="Search Title"\>

<!-- Feeds --\>
<link rel\="alternate" href\="https://feeds.feedburner.com/example" type\="application/rss+xml" title\="RSS"\>
<link rel\="alternate" href\="https://example.com/feed.atom" type\="application/atom+xml" title\="Atom 0.3"\>

<!-- Prefetching, preloading, prebrowsing --\>
<!-- More info: https://css-tricks.com/prefetching-preloading-prebrowsing/ --\>
<link rel\="dns-prefetch" href\="//example.com/"\>
<link rel\="preconnect" href\="https://www.example.com/"\>
<link rel\="prefetch" href\="https://www.example.com/"\>
<link rel\="prerender" href\="https://example.com/"\>
<link rel\="preload" href\="image.png" as\="image"\>

*   📖 [Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Icons
-----

[](https://github.com/joshbuchea/HEAD?screenshot=true#icons)

<!-- For IE 10 and below --\>
<!-- Place favicon.ico in the root directory - no tag necessary --\>

<!-- Icon in the highest resolution we need it for --\>
<link rel\="icon" sizes\="192x192" href\="/path/to/icon.png"\>

<!-- Apple Touch Icon (reuse 192px icon.png) --\>
<link rel\="apple-touch-icon" href\="/path/to/apple-touch-icon.png"\>

<!-- Safari Pinned Tab Icon --\>
<link rel\="mask-icon" href\="/path/to/icon.svg" color\="blue"\>

*   📖 [All About Favicons (And Touch Icons)](https://bitsofco.de/all-about-favicons-and-touch-icons/)
*   📖 [Creating Pinned Tab Icons](https://developer.apple.com/library/content/documentation/AppleApplications/Reference/SafariWebContent/pinnedTabs/pinnedTabs.html)
*   📖 [Favicon Cheat Sheet](https://github.com/audreyr/favicon-cheat-sheet)
*   📖 [Icons & Browser Colors](https://developers.google.com/web/fundamentals/design-and-ux/browser-customization/)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Social
------

[](https://github.com/joshbuchea/HEAD?screenshot=true#social)

### Facebook Open Graph

[](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-open-graph)

> Most content is shared to Facebook as a URL, so it's important that you mark up your website with Open Graph tags to take control over how your content appears on Facebook. [More about Facebook Open Graph Markup](https://developers.facebook.com/docs/sharing/webmasters#markup)

<meta property\="fb:app\_id" content\="123456789"\>
<meta property\="og:url" content\="https://example.com/page.html"\>
<meta property\="og:type" content\="website"\>
<meta property\="og:title" content\="Content Title"\>
<meta property\="og:image" content\="https://example.com/image.jpg"\>
<meta property\="og:image:alt" content\="A description of what is in the image (not a caption)"\>
<meta property\="og:description" content\="Description Here"\>
<meta property\="og:site\_name" content\="Site Name"\>
<meta property\="og:locale" content\="en\_US"\>
<meta property\="article:author" content\=""\>

*   📖 [Open Graph protocol](http://ogp.me/)
*   🛠 Test your page with the [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)

### Twitter Card

[](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-card)

> With Twitter Cards, you can attach rich photos, videos and media experiences to Tweets, helping to drive traffic to your website. [More about Twitter Cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards)

<meta name\="twitter:card" content\="summary"\>
<meta name\="twitter:site" content\="@site\_account"\>
<meta name\="twitter:creator" content\="@individual\_account"\>
<meta name\="twitter:url" content\="https://example.com/page.html"\>
<meta name\="twitter:title" content\="Content Title"\>
<meta name\="twitter:description" content\="Content description less than 200 characters"\>
<meta name\="twitter:image" content\="https://example.com/image.jpg"\>
<meta name\="twitter:image:alt" content\="A text description of the image conveying the essential nature of an image to users who are visually impaired. Maximum 420 characters."\>

*   📖 [Getting started with cards — Twitter Developers](https://dev.twitter.com/cards/getting-started)
*   🛠 Test your page with the [Twitter Card Validator](https://cards-dev.twitter.com/validator)

### Twitter Privacy

[](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-privacy)

If you embed tweets in your website, Twitter can use information from your site to tailor content and suggestions to Twitter users. [More about Twitter privacy options](https://dev.twitter.com/web/overview/privacy#what-privacy-options-do-website-publishers-have).

<!-- disallow Twitter from using your site's info for personalization purposes --\>
<meta name\="twitter:dnt" content\="on"\>

### Schema.org

[](https://github.com/joshbuchea/HEAD?screenshot=true#schemaorg)

<html lang\="" itemscope itemtype\="https://schema.org/Article"\>
    <head\>
      <link rel\="author" href\=""\>
      <link rel\="publisher" href\=""\>
      <meta itemprop\="name" content\="Content Title"\>
      <meta itemprop\="description" content\="Content description less than 200 characters"\>
      <meta itemprop\="image" content\="https://example.com/image.jpg"\>

**Note:** These meta tags require the `itemscope` and `itemtype` attributes to be added to the `<html>` tag.

*   📖 [Getting Started - schema.org](https://schema.org/docs/gs.html)
*   🛠 Test your page with the [Rich Results Test](https://search.google.com/test/rich-results)

### Pinterest

[](https://github.com/joshbuchea/HEAD?screenshot=true#pinterest)

Pinterest lets you prevent people from saving things from your website, according [to their help center](https://help.pinterest.com/en/business/article/prevent-saves-to-pinterest-from-your-site). The `description` is optional.

<meta name\="pinterest" content\="nopin" description\="Sorry, you can't save from my website!"\>

### Facebook Instant Articles

[](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-instant-articles)

<meta charset\="utf-8"\>
<meta property\="op:markup\_version" content\="v1.0"\>

<!-- The URL of the web version of your article --\>
<link rel\="canonical" href\="https://example.com/article.html"\>

<!-- The style to be used for this article --\>
<meta property\="fb:article\_style" content\="myarticlestyle"\>

*   📖 [Creating Articles - Instant Articles](https://developers.facebook.com/docs/instant-articles/guides/articlecreate)
*   📖 [Code Samples - Instant Articles](https://developers.facebook.com/docs/instant-articles/reference)

### OEmbed

[](https://github.com/joshbuchea/HEAD?screenshot=true#oembed)

<link rel\="alternate" type\="application/json+oembed"
  href\="https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=json"
  title\="oEmbed Profile: JSON"\>
<link rel\="alternate" type\="text/xml+oembed"
  href\="https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=xml"
  title\="oEmbed Profile: XML"\>

*   📖 [oEmbed format](https://oembed.com/)

### QQ/Wechat

[](https://github.com/joshbuchea/HEAD?screenshot=true#qqwechat)

Users share web pages to qq wechat will have a formatted message

<meta itemprop\="name" content\="share title"\>
<meta itemprop\="image" content\="http://imgcache.qq.com/qqshow/ac/v4/global/logo.png"\>
<meta name\="description" itemprop\="description" content\="share content"\>

*   📖 [Code Format Docs](http://open.mobile.qq.com/api/mqq/index#api:setShareInfo)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Browsers / Platforms
--------------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#browsers--platforms)

### Apple iOS

[](https://github.com/joshbuchea/HEAD?screenshot=true#apple-ios)

<!-- Smart App Banner --\>
<meta name\="apple-itunes-app" content\="app-id=APP\_ID,affiliate-data=AFFILIATE\_ID,app-argument=SOME\_TEXT"\>

<!-- Disable automatic detection and formatting of possible phone numbers --\>
<meta name\="format-detection" content\="telephone=no"\>

<!-- Launch Icon (180x180px or larger) --\>
<link rel\="apple-touch-icon" href\="/path/to/apple-touch-icon.png"\>

<!-- Launch Screen Image --\>
<link rel\="apple-touch-startup-image" href\="/path/to/launch.png"\>

<!-- Launch Icon Title --\>
<meta name\="apple-mobile-web-app-title" content\="App Title"\>

<!-- Enable standalone (full-screen) mode --\>
<meta name\="apple-mobile-web-app-capable" content\="yes"\>

<!-- Status bar appearance (has no effect unless standalone mode is enabled) --\>
<meta name\="apple-mobile-web-app-status-bar-style" content\="black"\>

<!-- iOS app deep linking --\>
<meta name\="apple-itunes-app" content\="app-id=APP-ID, app-argument=http/url-sample.com"\>
<link rel\="alternate" href\="ios-app://APP-ID/http/url-sample.com"\>

*   📖 [Configuring Web Applications](https://developer.apple.com/library/content/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html)

### Google Android

[](https://github.com/joshbuchea/HEAD?screenshot=true#google-android)

<meta name\="theme-color" content\="#E64545"\>

<!-- Add to home screen --\>
<meta name\="mobile-web-app-capable" content\="yes"\>
<!-- More info: https://developer.chrome.com/multidevice/android/installtohomescreen --\>

<!-- Android app deep linking --\>
<meta name\="google-play-app" content\="app-id=package-name"\>
<link rel\="alternate" href\="android-app://package-name/http/url-sample.com"\>

### Google Chrome

[](https://github.com/joshbuchea/HEAD?screenshot=true#google-chrome)

<link rel\="chrome-webstore-item" href\="https://chrome.google.com/webstore/detail/APP\_ID"\>

<!-- Disable translation prompt --\>
<meta name\="google" content\="notranslate"\>

### Microsoft Internet Explorer

[](https://github.com/joshbuchea/HEAD?screenshot=true#microsoft-internet-explorer)

<!-- Force IE 8/9/10 to use its latest rendering engine --\>
<meta http-equiv\="x-ua-compatible" content\="ie=edge"\>

<!-- Disable automatic detection and formatting of possible phone numbers by Skype Toolbar browser extension --\>
<meta name\="skype\_toolbar" content\="skype\_toolbar\_parser\_compatible"\>

<!-- Windows Tiles --\>
<meta name\="msapplication-config" content\="/browserconfig.xml"\>

Minimum required xml markup for `browserconfig.xml`:

<?xml version\="1.0" encoding\="utf-8"?\>
<browserconfig\>
   <msapplication\>
     <tile\>
        <square70x70logo src\="small.png"/\>
        <square150x150logo src\="medium.png"/\>
        <wide310x150logo src\="wide.png"/\>
        <square310x310logo src\="large.png"/\>
     </tile\>
   </msapplication\>
</browserconfig\>

*   📖 [Browser configuration schema reference](https://msdn.microsoft.com/en-us/library/dn320426.aspx)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Browsers (Chinese)
------------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#browsers-chinese)

### 360 Browser

[](https://github.com/joshbuchea/HEAD?screenshot=true#360-browser)

<!-- Select rendering engine order --\>
<meta name\="renderer" content\="webkit|ie-comp|ie-stand"\>

### QQ Mobile Browser

[](https://github.com/joshbuchea/HEAD?screenshot=true#qq-mobile-browser)

<!-- Locks the screen into the specified orientation --\>
<meta name\="x5-orientation" content\="landscape/portrait"\>

<!-- Display this document in fullscreen --\>
<meta name\="x5-fullscreen" content\="true"\>

<!-- Document will be displayed in "application mode" (fullscreen, etc.) --\>
<meta name\="x5-page-mode" content\="app"\>

### UC Mobile Browser

[](https://github.com/joshbuchea/HEAD?screenshot=true#uc-mobile-browser)

<!-- Locks the screen into the specified orientation --\>
<meta name\="screen-orientation" content\="landscape/portrait"\>

<!-- Display this document in fullscreen --\>
<meta name\="full-screen" content\="yes"\>

<!-- UC browser will display images even if in "text mode" --\>
<meta name\="imagemode" content\="force"\>

<!-- Document will be displayed in "application mode"(fullscreen, forbidding gesture, etc.) --\>
<meta name\="browsermode" content\="application"\>

<!-- Disabled the UC browser's "night mode" for this document --\>
<meta name\="nightmode" content\="disable"\>

<!-- Simplify the document to reduce data transfer --\>
<meta name\="layoutmode" content\="fitscreen"\>

<!-- Disable the UC browser's feature of "scaling font up when there are many words in this document" --\>
<meta name\="wap-font-scale" content\="no"\>

*   📖 [UC Browser Docs](https://www.uc.cn/download/UCBrowser_U3_API.doc)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

App Links
---------

[](https://github.com/joshbuchea/HEAD?screenshot=true#app-links)

<!-- iOS --\>
<meta property\="al:ios:url" content\="applinks://docs"\>
<meta property\="al:ios:app\_store\_id" content\="12345"\>
<meta property\="al:ios:app\_name" content\="App Links"\>

<!-- Android --\>
<meta property\="al:android:url" content\="applinks://docs"\>
<meta property\="al:android:app\_name" content\="App Links"\>
<meta property\="al:android:package" content\="org.applinks"\>

<!-- Web fall back --\>
<meta property\="al:web:url" content\="https://applinks.org/documentation"\>

*   📖 [App Links](https://developers.facebook.com/docs/applinks)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Other Resources
---------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#other-resources)

*   📖 [HTML5 Boilerplate Docs: The HTML](https://github.com/h5bp/html5-boilerplate/blob/master/dist/doc/html.md)
*   📖 [HTML5 Boilerplate Docs: Extend and customize](https://github.com/h5bp/html5-boilerplate/blob/master/dist/doc/extend.md)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Related Projects
----------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#related-projects)

*   [Atom HTML Head Snippets](https://github.com/joshbuchea/atom-html-head-snippets) - Atom package for `HEAD` snippets
*   [Sublime Text HTML Head Snippets](https://github.com/marcobiedermann/sublime-head-snippets) - Sublime Text package for `HEAD` snippets
*   [head-it](https://github.com/hemanth/head-it) - CLI interface for `HEAD` snippets
*   [vue-head](https://github.com/ktquez/vue-head) - Manipulating the meta information of the `HEAD` tag for Vue.js

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

Other Formats
-------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#other-formats)

*   📄 [PDF](https://gitprint.com/joshbuchea/HEAD/blob/master/README.md)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

🌐 Translations
---------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#-translations)

*   🇮🇩 [Bahasa](https://github.com/rijdz/HEAD)
*   🇧🇷 [Brazilian Portuguese](https://github.com/Webschool-io/HEAD)
*   🇨🇳 [Chinese (Simplified)](https://github.com/Amery2010/HEAD)
*   🇩🇪 [German](https://github.com/Shidigital/HEAD)
*   🇮🇹 [Italian](https://github.com/Fakkio/HEAD)
*   🇯🇵 [Japanese](https://coliss.com/articles/build-websites/operation/work/collection-of-html-head-elements.html)
*   🇰🇷 [Korean](https://github.com/Lutece/HEAD)
*   🇷🇺 [Russian/Русский](https://github.com/Konfuze/HEAD)
*   🇪🇸 [Spanish](https://github.com/alvaroadlf/HEAD)
*   🇹🇷 [Turkish/Türkçe](https://github.com/mkg0/HEAD)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

🤝 Contributing
---------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#-contributing)

**Open an issue or a pull request to suggest changes or additions.**

### Guide

[](https://github.com/joshbuchea/HEAD?screenshot=true#guide)

The **HEAD** repository consists of two branches:

#### 1\. `master`

[](https://github.com/joshbuchea/HEAD?screenshot=true#1-master)

This branch consists of the `README.md` file that is reflected on the [htmlhead.dev](https://htmlhead.dev/) website. All changes to the content of the guide should be made in this file.

Please follow these steps for pull requests:

{:.list-style-default}

*   Modify only one tag, or one related set of tags at a time
*   Use double quotes on attributes
*   Don't include a trailing slash in self-closing elements — the HTML5 spec says they're optional
*   Consider including a link to documentation that supports your change

#### 2\. `gh-pages`

[](https://github.com/joshbuchea/HEAD?screenshot=true#2-gh-pages)

This branch is responsible for the [htmlhead.dev](https://htmlhead.dev/) website. We use [Jekyll](https://jekyllrb.com/) to deploy the `README.md` markdown file to [GitHub Pages](https://pages.github.com/). All website related modifications should be made in this branch.

You may find it helpful to review the [Jekyll Docs](https://jekyllrb.com/docs/home/) and understand how Jekyll works before working in this branch.

🌟 Contributors
---------------

[](https://github.com/joshbuchea/HEAD?screenshot=true#-contributors)

Check out all the super awesome [contributors](https://github.com/joshbuchea/HEAD/graphs/contributors) 🤩

👤 Author
---------

[](https://github.com/joshbuchea/HEAD?screenshot=true#-author)

**Josh Buchea**

*   GitHub: [@joshbuchea](https://github.com/joshbuchea)
*   Mastodon: [@joshbuchea@hachyderm.io](https://hachyderm.io/@joshbuchea)

💛 Support
----------

[](https://github.com/joshbuchea/HEAD?screenshot=true#-support)

If this project was helpful for you or your organization, please considering supporting my work directly:

*   💛 [Sponsor me on GitHub](https://github.com/sponsors/joshbuchea)
*   ⭐️ [Star this project on GitHub](https://github.com/joshbuchea/HEAD)
*   🐙 [Follow me on GitHub](https://github.com/joshbuchea)
*   🐘 [Follow me on Mastodon](https://hachyderm.io/@joshbuchea)

Everything helps, thanks! 🙏

— Josh

📝 License
----------

[](https://github.com/joshbuchea/HEAD?screenshot=true#-license)

[![Image 28: CC0](https://camo.githubusercontent.com/d2c82b6a501bcd93578124d889803ae99a9d8e0d3e64eb806a1758270fe90185/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f702f7a65726f2f312e302f38387833312e706e67)](https://creativecommons.org/publicdomain/zero/1.0/)

**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**

## Metadata

```json
{
  "title": "GitHub - joshbuchea/HEAD: A simple guide to HTML <head> elements",
  "description": "A simple guide to HTML <head> elements. Contribute to joshbuchea/HEAD development by creating an account on GitHub.",
  "url": "https://github.com/joshbuchea/HEAD?screenshot=true",
  "content": "🤯 HEAD\n-------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#-head)\n\n> A simple guide to HTML `<head>` elements\n\n[![Image 25: Contributors](https://camo.githubusercontent.com/08304f1a42bc10f5af409ea1ac74bf4529cb396f0342a1dbfab140706b9fbb64/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f6a6f73686275636865612f686561642e7376673f7374796c653d666f722d7468652d6261646765)](https://github.com/joshbuchea/HEAD/graphs/contributors) [![Image 26: CC0](https://camo.githubusercontent.com/4589d411564dd50f3db15ea3596aae2dfbb7c82c9f3371287e5617c61b9f6c0e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4343302d677265656e2e7376673f7374796c653d666f722d7468652d6261646765)](https://creativecommons.org/publicdomain/zero/1.0/) [![Image 27: Follow @joshbuchea on Mastodon](https://camo.githubusercontent.com/85f22422b6460a86fdd6c801e13636b8279f4e5116c955d895c0244846c447aa/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466f6c6c6f775f406a6f73686275636865612d707572706c653f6c6f676f3d6d6173746f646f6e266c6f676f436f6c6f723d7768697465267374796c653d666f722d7468652d6261646765)](https://hachyderm.io/@joshbuchea)\n\nTable of Contents\n-----------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)\n\n*   [Recommended Minimum](https://github.com/joshbuchea/HEAD?screenshot=true#recommended-minimum)\n*   [Elements](https://github.com/joshbuchea/HEAD?screenshot=true#elements)\n*   [Meta](https://github.com/joshbuchea/HEAD?screenshot=true#meta)\n*   [Link](https://github.com/joshbuchea/HEAD?screenshot=true#link)\n*   [Icons](https://github.com/joshbuchea/HEAD?screenshot=true#icons)\n*   [Social](https://github.com/joshbuchea/HEAD?screenshot=true#social)\n    *   [Facebook Open Graph](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-open-graph)\n    *   [Twitter Card](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-card)\n    *   [Twitter Privacy](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-privacy)\n    *   [Schema.org](https://github.com/joshbuchea/HEAD?screenshot=true#schemaorg)\n    *   [Pinterest](https://github.com/joshbuchea/HEAD?screenshot=true#pinterest)\n    *   [Facebook Instant Articles](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-instant-articles)\n    *   [OEmbed](https://github.com/joshbuchea/HEAD?screenshot=true#oembed)\n    *   [QQ/Wechat](https://github.com/joshbuchea/HEAD?screenshot=true#qqwechat)\n*   [Browsers / Platforms](https://github.com/joshbuchea/HEAD?screenshot=true#browsers--platforms)\n    *   [Apple iOS](https://github.com/joshbuchea/HEAD?screenshot=true#apple-ios)\n    *   [Google Android](https://github.com/joshbuchea/HEAD?screenshot=true#google-android)\n    *   [Google Chrome](https://github.com/joshbuchea/HEAD?screenshot=true#google-chrome)\n    *   [Microsoft Internet Explorer](https://github.com/joshbuchea/HEAD?screenshot=true#microsoft-internet-explorer)\n*   [Browsers (Chinese)](https://github.com/joshbuchea/HEAD?screenshot=true#browsers-chinese)\n    *   [360 Browser](https://github.com/joshbuchea/HEAD?screenshot=true#360-browser)\n    *   [QQ Mobile Browser](https://github.com/joshbuchea/HEAD?screenshot=true#qq-mobile-browser)\n    *   [UC Mobile Browser](https://github.com/joshbuchea/HEAD?screenshot=true#uc-mobile-browser)\n*   [App Links](https://github.com/joshbuchea/HEAD?screenshot=true#app-links)\n*   [Other Resources](https://github.com/joshbuchea/HEAD?screenshot=true#other-resources)\n*   [Related Projects](https://github.com/joshbuchea/HEAD?screenshot=true#related-projects)\n*   [Other Formats](https://github.com/joshbuchea/HEAD?screenshot=true#other-formats)\n*   [Translations](https://github.com/joshbuchea/HEAD?screenshot=true#-translations)\n*   [Contributing](https://github.com/joshbuchea/HEAD?screenshot=true#-contributing)\n    *   [Contributors](https://github.com/joshbuchea/HEAD?screenshot=true#contributors)\n*   [Author](https://github.com/joshbuchea/HEAD?screenshot=true#-author)\n*   [License](https://github.com/joshbuchea/HEAD?screenshot=true#-license)\n\nRecommended Minimum\n-------------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#recommended-minimum)\n\nBelow are the essential elements for any web document (websites/apps):\n\n<meta charset\\=\"utf-8\"\\>\n<meta name\\=\"viewport\" content\\=\"width=device-width, initial-scale=1\"\\>\n<!--\n  The above 2 meta tags \\*must\\* come first in the <head\\>\n  to consistently ensure proper document rendering.\n  Any other head element should come \\*after\\* these tags.\n --\\>\n<title\\>Page Title</title\\>\n\n`meta charset` - defines the encoding of the website, `utf-8` is the standard\n\n`meta name=\"viewport\"` - viewport settings related to mobile responsiveness\n\n`width=device-width` - use the physical width of the device (great for mobile!)\n\n`initial-scale=1` - the initial zoom, 1 means no zoom\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nElements\n--------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#elements)\n\nValid `<head>` elements include `meta`, `link`, `title`, `style`, `script`, `noscript`, and `base`.\n\nThese elements provide information for how a document should be perceived, and rendered, by web technologies. e.g. browsers, search engines, bots, etc.\n\n<!--\n  Set the character encoding for this document, so that\n  all characters within the UTF-8 space (such as emoji)\n  are rendered correctly.\n\\--\\>\n<meta charset\\=\"utf-8\"\\>\n\n<!-- Set the document's title --\\>\n<title\\>Page Title</title\\>\n\n<!-- Set the base URL for all relative URLs within the document --\\>\n<base href\\=\"https://example.com/page.html\"\\>\n\n<!-- Link to an external CSS file --\\>\n<link rel\\=\"stylesheet\" href\\=\"styles.css\"\\>\n\n<!-- Used for adding in-document CSS --\\>\n<style\\>\n  /\\* ... \\*/\n</style\\>\n\n<!-- JavaScript & No-JavaScript tags --\\>\n<script src\\=\"script.js\"\\></script\\>\n<script\\>\n  // function(s) go here\n</script\\>\n<noscript\\>\n  <!-- No JS alternative --\\>\n</noscript\\>\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nMeta\n----\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#meta)\n\n<!--\n  The following 2 meta tags \\*must\\* come first in the <head\\>\n  to consistently ensure proper document rendering.\n  Any other head element should come \\*after\\* these tags.\n\\--\\>\n<meta charset\\=\"utf-8\"\\>\n<meta name\\=\"viewport\" content\\=\"width=device-width, initial-scale=1\"\\>\n\n<!--\n  Allows control over where resources are loaded from.\n  Place as early in the <head\\> as possible, as the tag  \n  only applies to resources that are declared after it.\n\\--\\>\n<meta http-equiv\\=\"Content-Security-Policy\" content\\=\"default-src 'self'\"\\>\n\n<!-- Name of web application (only should be used if the website is used as an app) --\\>\n<meta name\\=\"application-name\" content\\=\"Application Name\"\\>\n\n<!-- Theme Color for Chrome, Firefox OS and Opera --\\>\n<meta name\\=\"theme-color\" content\\=\"#4285f4\"\\>\n\n<!-- Short description of the document (limit to 150 characters) --\\>\n<!-- This content \\*may\\* be used as a part of search engine results. --\\>\n<meta name\\=\"description\" content\\=\"A description of the page\"\\>\n\n<!-- Control the behavior of search engine crawling and indexing --\\>\n<meta name\\=\"robots\" content\\=\"index,follow\"\\><!-- All Search Engines --\\>\n<meta name\\=\"googlebot\" content\\=\"index,follow\"\\><!-- Google Specific --\\>\n\n<!-- Tells Google not to show the sitelinks search box --\\>\n<meta name\\=\"google\" content\\=\"nositelinkssearchbox\"\\>\n\n<!-- Tells Google not to provide a translation for this document --\\>\n<meta name\\=\"google\" content\\=\"notranslate\"\\>\n\n<!-- Verify website ownership --\\>\n<meta name\\=\"google-site-verification\" content\\=\"verification\\_token\"\\><!-- Google Search Console --\\>\n<meta name\\=\"yandex-verification\" content\\=\"verification\\_token\"\\><!-- Yandex Webmasters --\\>\n<meta name\\=\"msvalidate.01\" content\\=\"verification\\_token\"\\><!-- Bing Webmaster Center --\\>\n<meta name\\=\"alexaVerifyID\" content\\=\"verification\\_token\"\\><!-- Alexa Console --\\>\n<meta name\\=\"p:domain\\_verify\" content\\=\"code\\_from\\_pinterest\"\\><!-- Pinterest Console--\\>\n<meta name\\=\"norton-safeweb-site-verification\" content\\=\"norton\\_code\"\\><!-- Norton Safe Web --\\>\n\n<!-- Identify the software used to build the document (i.e. - WordPress, Dreamweaver) --\\>\n<meta name\\=\"generator\" content\\=\"program\"\\>\n\n<!-- Short description of your document's subject --\\>\n<meta name\\=\"subject\" content\\=\"your document's subject\"\\>\n\n<!-- Gives a general age rating based on the document's content --\\>\n<meta name\\=\"rating\" content\\=\"General\"\\>\n\n<!-- Allows control over how referrer information is passed --\\>\n<meta name\\=\"referrer\" content\\=\"no-referrer\"\\>\n\n<!-- Disable automatic detection and formatting of possible phone numbers --\\>\n<meta name\\=\"format-detection\" content\\=\"telephone=no\"\\>\n\n<!-- Completely opt out of DNS prefetching by setting to \"off\" --\\>\n<meta http-equiv\\=\"x-dns-prefetch-control\" content\\=\"off\"\\>\n\n<!-- Specifies the document to appear in a specific frame --\\>\n<meta http-equiv\\=\"Window-Target\" content\\=\"\\_value\"\\>\n\n<!-- Geo tags --\\>\n<meta name\\=\"ICBM\" content\\=\"latitude, longitude\"\\>\n<meta name\\=\"geo.position\" content\\=\"latitude;longitude\"\\>\n<meta name\\=\"geo.region\" content\\=\"country\\[-state\\]\"\\><!-- Country code (ISO 3166-1): mandatory, state code (ISO 3166-2): optional; eg. content=\"US\" / content=\"US-NY\" --\\>\n<meta name\\=\"geo.placename\" content\\=\"city/town\"\\><!-- eg. content=\"New York City\" --\\>\n\n<!-- Web Monetization https://webmonetization.org/docs/getting-started --\\>\n<meta name\\=\"monetization\" content\\=\"$paymentpointer.example\"\\>\n\n*   📖 [Meta tags that Google understands](https://support.google.com/webmasters/answer/79812?hl=en)\n*   📖 [WHATWG Wiki: MetaExtensions](https://wiki.whatwg.org/wiki/MetaExtensions)\n*   📖 [ICBM on Wikipedia](https://en.wikipedia.org/wiki/ICBM_address#Modern_use)\n*   📖 [Geotagging on Wikipedia](https://en.wikipedia.org/wiki/Geotagging#HTML_pages)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nLink\n----\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#link)\n\n<!-- Points to an external stylesheet --\\>\n<link rel\\=\"stylesheet\" href\\=\"https://example.com/styles.css\"\\>\n\n<!-- Helps prevent duplicate content issues --\\>\n<link rel\\=\"canonical\" href\\=\"https://example.com/article/?page=2\"\\>\n\n<!-- Links to an AMP HTML version of the current document --\\>\n<link rel\\=\"amphtml\" href\\=\"https://example.com/path/to/amp-version.html\"\\>\n\n<!-- Links to a JSON file that specifies \"installation\" credentials for the web applications --\\>\n<link rel\\=\"manifest\" href\\=\"manifest.json\"\\>\n\n<!-- Links to information about the author(s) of the document --\\>\n<link rel\\=\"author\" href\\=\"humans.txt\"\\>\n\n<!-- Refers to a copyright statement that applies to the link's context --\\>\n<link rel\\=\"license\" href\\=\"copyright.html\"\\>\n\n<!-- Gives a reference to a location in your document that may be in another language --\\>\n<link rel\\=\"alternate\" href\\=\"https://es.example.com/\" hreflang\\=\"es\"\\>\n\n<!-- Provides information about an author or another person --\\>\n<link rel\\=\"me\" href\\=\"https://google.com/profiles/thenextweb\" type\\=\"text/html\"\\>\n<link rel\\=\"me\" href\\=\"mailto:name@example.com\"\\>\n<link rel\\=\"me\" href\\=\"sms:+15035550125\"\\>\n\n<!-- Links to a document that describes a collection of records, documents, or other materials of historical interest --\\>\n<link rel\\=\"archives\" href\\=\"https://example.com/archives/\"\\>\n\n<!-- Links to top level resource in an hierarchical structure --\\>\n<link rel\\=\"index\" href\\=\"https://example.com/article/\"\\>\n\n<!-- Provides a self reference - useful when the document has multiple possible references --\\>\n<link rel\\=\"self\" type\\=\"application/atom+xml\" href\\=\"https://example.com/atom.xml\"\\>\n\n<!-- The first, last, previous, and next documents in a series of documents, respectively --\\>\n<link rel\\=\"first\" href\\=\"https://example.com/article/\"\\>\n<link rel\\=\"last\" href\\=\"https://example.com/article/?page=42\"\\>\n<link rel\\=\"prev\" href\\=\"https://example.com/article/?page=1\"\\>\n<link rel\\=\"next\" href\\=\"https://example.com/article/?page=3\"\\>\n\n<!-- Used when a 3rd party service is utilized to maintain a blog --\\>\n<link rel\\=\"EditURI\" href\\=\"https://example.com/xmlrpc.php?rsd\" type\\=\"application/rsd+xml\" title\\=\"RSD\"\\>\n\n<!-- Forms an automated comment when another WordPress blog links to your WordPress blog or post --\\>\n<link rel\\=\"pingback\" href\\=\"https://example.com/xmlrpc.php\"\\>\n\n<!-- Notifies a URL when you link to it on your document --\\>\n<link rel\\=\"webmention\" href\\=\"https://example.com/webmention\"\\>\n\n<!-- Enables posting to your own domain using a Micropub client --\\>\n<link rel\\=\"micropub\" href\\=\"https://example.com/micropub\"\\>\n\n<!-- Open Search --\\>\n<link rel\\=\"search\" href\\=\"/open-search.xml\" type\\=\"application/opensearchdescription+xml\" title\\=\"Search Title\"\\>\n\n<!-- Feeds --\\>\n<link rel\\=\"alternate\" href\\=\"https://feeds.feedburner.com/example\" type\\=\"application/rss+xml\" title\\=\"RSS\"\\>\n<link rel\\=\"alternate\" href\\=\"https://example.com/feed.atom\" type\\=\"application/atom+xml\" title\\=\"Atom 0.3\"\\>\n\n<!-- Prefetching, preloading, prebrowsing --\\>\n<!-- More info: https://css-tricks.com/prefetching-preloading-prebrowsing/ --\\>\n<link rel\\=\"dns-prefetch\" href\\=\"//example.com/\"\\>\n<link rel\\=\"preconnect\" href\\=\"https://www.example.com/\"\\>\n<link rel\\=\"prefetch\" href\\=\"https://www.example.com/\"\\>\n<link rel\\=\"prerender\" href\\=\"https://example.com/\"\\>\n<link rel\\=\"preload\" href\\=\"image.png\" as\\=\"image\"\\>\n\n*   📖 [Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nIcons\n-----\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#icons)\n\n<!-- For IE 10 and below --\\>\n<!-- Place favicon.ico in the root directory - no tag necessary --\\>\n\n<!-- Icon in the highest resolution we need it for --\\>\n<link rel\\=\"icon\" sizes\\=\"192x192\" href\\=\"/path/to/icon.png\"\\>\n\n<!-- Apple Touch Icon (reuse 192px icon.png) --\\>\n<link rel\\=\"apple-touch-icon\" href\\=\"/path/to/apple-touch-icon.png\"\\>\n\n<!-- Safari Pinned Tab Icon --\\>\n<link rel\\=\"mask-icon\" href\\=\"/path/to/icon.svg\" color\\=\"blue\"\\>\n\n*   📖 [All About Favicons (And Touch Icons)](https://bitsofco.de/all-about-favicons-and-touch-icons/)\n*   📖 [Creating Pinned Tab Icons](https://developer.apple.com/library/content/documentation/AppleApplications/Reference/SafariWebContent/pinnedTabs/pinnedTabs.html)\n*   📖 [Favicon Cheat Sheet](https://github.com/audreyr/favicon-cheat-sheet)\n*   📖 [Icons & Browser Colors](https://developers.google.com/web/fundamentals/design-and-ux/browser-customization/)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nSocial\n------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#social)\n\n### Facebook Open Graph\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-open-graph)\n\n> Most content is shared to Facebook as a URL, so it's important that you mark up your website with Open Graph tags to take control over how your content appears on Facebook. [More about Facebook Open Graph Markup](https://developers.facebook.com/docs/sharing/webmasters#markup)\n\n<meta property\\=\"fb:app\\_id\" content\\=\"123456789\"\\>\n<meta property\\=\"og:url\" content\\=\"https://example.com/page.html\"\\>\n<meta property\\=\"og:type\" content\\=\"website\"\\>\n<meta property\\=\"og:title\" content\\=\"Content Title\"\\>\n<meta property\\=\"og:image\" content\\=\"https://example.com/image.jpg\"\\>\n<meta property\\=\"og:image:alt\" content\\=\"A description of what is in the image (not a caption)\"\\>\n<meta property\\=\"og:description\" content\\=\"Description Here\"\\>\n<meta property\\=\"og:site\\_name\" content\\=\"Site Name\"\\>\n<meta property\\=\"og:locale\" content\\=\"en\\_US\"\\>\n<meta property\\=\"article:author\" content\\=\"\"\\>\n\n*   📖 [Open Graph protocol](http://ogp.me/)\n*   🛠 Test your page with the [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)\n\n### Twitter Card\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-card)\n\n> With Twitter Cards, you can attach rich photos, videos and media experiences to Tweets, helping to drive traffic to your website. [More about Twitter Cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards)\n\n<meta name\\=\"twitter:card\" content\\=\"summary\"\\>\n<meta name\\=\"twitter:site\" content\\=\"@site\\_account\"\\>\n<meta name\\=\"twitter:creator\" content\\=\"@individual\\_account\"\\>\n<meta name\\=\"twitter:url\" content\\=\"https://example.com/page.html\"\\>\n<meta name\\=\"twitter:title\" content\\=\"Content Title\"\\>\n<meta name\\=\"twitter:description\" content\\=\"Content description less than 200 characters\"\\>\n<meta name\\=\"twitter:image\" content\\=\"https://example.com/image.jpg\"\\>\n<meta name\\=\"twitter:image:alt\" content\\=\"A text description of the image conveying the essential nature of an image to users who are visually impaired. Maximum 420 characters.\"\\>\n\n*   📖 [Getting started with cards — Twitter Developers](https://dev.twitter.com/cards/getting-started)\n*   🛠 Test your page with the [Twitter Card Validator](https://cards-dev.twitter.com/validator)\n\n### Twitter Privacy\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#twitter-privacy)\n\nIf you embed tweets in your website, Twitter can use information from your site to tailor content and suggestions to Twitter users. [More about Twitter privacy options](https://dev.twitter.com/web/overview/privacy#what-privacy-options-do-website-publishers-have).\n\n<!-- disallow Twitter from using your site's info for personalization purposes --\\>\n<meta name\\=\"twitter:dnt\" content\\=\"on\"\\>\n\n### Schema.org\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#schemaorg)\n\n<html lang\\=\"\" itemscope itemtype\\=\"https://schema.org/Article\"\\>\n    <head\\>\n      <link rel\\=\"author\" href\\=\"\"\\>\n      <link rel\\=\"publisher\" href\\=\"\"\\>\n      <meta itemprop\\=\"name\" content\\=\"Content Title\"\\>\n      <meta itemprop\\=\"description\" content\\=\"Content description less than 200 characters\"\\>\n      <meta itemprop\\=\"image\" content\\=\"https://example.com/image.jpg\"\\>\n\n**Note:** These meta tags require the `itemscope` and `itemtype` attributes to be added to the `<html>` tag.\n\n*   📖 [Getting Started - schema.org](https://schema.org/docs/gs.html)\n*   🛠 Test your page with the [Rich Results Test](https://search.google.com/test/rich-results)\n\n### Pinterest\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#pinterest)\n\nPinterest lets you prevent people from saving things from your website, according [to their help center](https://help.pinterest.com/en/business/article/prevent-saves-to-pinterest-from-your-site). The `description` is optional.\n\n<meta name\\=\"pinterest\" content\\=\"nopin\" description\\=\"Sorry, you can't save from my website!\"\\>\n\n### Facebook Instant Articles\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#facebook-instant-articles)\n\n<meta charset\\=\"utf-8\"\\>\n<meta property\\=\"op:markup\\_version\" content\\=\"v1.0\"\\>\n\n<!-- The URL of the web version of your article --\\>\n<link rel\\=\"canonical\" href\\=\"https://example.com/article.html\"\\>\n\n<!-- The style to be used for this article --\\>\n<meta property\\=\"fb:article\\_style\" content\\=\"myarticlestyle\"\\>\n\n*   📖 [Creating Articles - Instant Articles](https://developers.facebook.com/docs/instant-articles/guides/articlecreate)\n*   📖 [Code Samples - Instant Articles](https://developers.facebook.com/docs/instant-articles/reference)\n\n### OEmbed\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#oembed)\n\n<link rel\\=\"alternate\" type\\=\"application/json+oembed\"\n  href\\=\"https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=json\"\n  title\\=\"oEmbed Profile: JSON\"\\>\n<link rel\\=\"alternate\" type\\=\"text/xml+oembed\"\n  href\\=\"https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=xml\"\n  title\\=\"oEmbed Profile: XML\"\\>\n\n*   📖 [oEmbed format](https://oembed.com/)\n\n### QQ/Wechat\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#qqwechat)\n\nUsers share web pages to qq wechat will have a formatted message\n\n<meta itemprop\\=\"name\" content\\=\"share title\"\\>\n<meta itemprop\\=\"image\" content\\=\"http://imgcache.qq.com/qqshow/ac/v4/global/logo.png\"\\>\n<meta name\\=\"description\" itemprop\\=\"description\" content\\=\"share content\"\\>\n\n*   📖 [Code Format Docs](http://open.mobile.qq.com/api/mqq/index#api:setShareInfo)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nBrowsers / Platforms\n--------------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#browsers--platforms)\n\n### Apple iOS\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#apple-ios)\n\n<!-- Smart App Banner --\\>\n<meta name\\=\"apple-itunes-app\" content\\=\"app-id=APP\\_ID,affiliate-data=AFFILIATE\\_ID,app-argument=SOME\\_TEXT\"\\>\n\n<!-- Disable automatic detection and formatting of possible phone numbers --\\>\n<meta name\\=\"format-detection\" content\\=\"telephone=no\"\\>\n\n<!-- Launch Icon (180x180px or larger) --\\>\n<link rel\\=\"apple-touch-icon\" href\\=\"/path/to/apple-touch-icon.png\"\\>\n\n<!-- Launch Screen Image --\\>\n<link rel\\=\"apple-touch-startup-image\" href\\=\"/path/to/launch.png\"\\>\n\n<!-- Launch Icon Title --\\>\n<meta name\\=\"apple-mobile-web-app-title\" content\\=\"App Title\"\\>\n\n<!-- Enable standalone (full-screen) mode --\\>\n<meta name\\=\"apple-mobile-web-app-capable\" content\\=\"yes\"\\>\n\n<!-- Status bar appearance (has no effect unless standalone mode is enabled) --\\>\n<meta name\\=\"apple-mobile-web-app-status-bar-style\" content\\=\"black\"\\>\n\n<!-- iOS app deep linking --\\>\n<meta name\\=\"apple-itunes-app\" content\\=\"app-id=APP-ID, app-argument=http/url-sample.com\"\\>\n<link rel\\=\"alternate\" href\\=\"ios-app://APP-ID/http/url-sample.com\"\\>\n\n*   📖 [Configuring Web Applications](https://developer.apple.com/library/content/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html)\n\n### Google Android\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#google-android)\n\n<meta name\\=\"theme-color\" content\\=\"#E64545\"\\>\n\n<!-- Add to home screen --\\>\n<meta name\\=\"mobile-web-app-capable\" content\\=\"yes\"\\>\n<!-- More info: https://developer.chrome.com/multidevice/android/installtohomescreen --\\>\n\n<!-- Android app deep linking --\\>\n<meta name\\=\"google-play-app\" content\\=\"app-id=package-name\"\\>\n<link rel\\=\"alternate\" href\\=\"android-app://package-name/http/url-sample.com\"\\>\n\n### Google Chrome\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#google-chrome)\n\n<link rel\\=\"chrome-webstore-item\" href\\=\"https://chrome.google.com/webstore/detail/APP\\_ID\"\\>\n\n<!-- Disable translation prompt --\\>\n<meta name\\=\"google\" content\\=\"notranslate\"\\>\n\n### Microsoft Internet Explorer\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#microsoft-internet-explorer)\n\n<!-- Force IE 8/9/10 to use its latest rendering engine --\\>\n<meta http-equiv\\=\"x-ua-compatible\" content\\=\"ie=edge\"\\>\n\n<!-- Disable automatic detection and formatting of possible phone numbers by Skype Toolbar browser extension --\\>\n<meta name\\=\"skype\\_toolbar\" content\\=\"skype\\_toolbar\\_parser\\_compatible\"\\>\n\n<!-- Windows Tiles --\\>\n<meta name\\=\"msapplication-config\" content\\=\"/browserconfig.xml\"\\>\n\nMinimum required xml markup for `browserconfig.xml`:\n\n<?xml version\\=\"1.0\" encoding\\=\"utf-8\"?\\>\n<browserconfig\\>\n   <msapplication\\>\n     <tile\\>\n        <square70x70logo src\\=\"small.png\"/\\>\n        <square150x150logo src\\=\"medium.png\"/\\>\n        <wide310x150logo src\\=\"wide.png\"/\\>\n        <square310x310logo src\\=\"large.png\"/\\>\n     </tile\\>\n   </msapplication\\>\n</browserconfig\\>\n\n*   📖 [Browser configuration schema reference](https://msdn.microsoft.com/en-us/library/dn320426.aspx)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nBrowsers (Chinese)\n------------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#browsers-chinese)\n\n### 360 Browser\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#360-browser)\n\n<!-- Select rendering engine order --\\>\n<meta name\\=\"renderer\" content\\=\"webkit|ie-comp|ie-stand\"\\>\n\n### QQ Mobile Browser\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#qq-mobile-browser)\n\n<!-- Locks the screen into the specified orientation --\\>\n<meta name\\=\"x5-orientation\" content\\=\"landscape/portrait\"\\>\n\n<!-- Display this document in fullscreen --\\>\n<meta name\\=\"x5-fullscreen\" content\\=\"true\"\\>\n\n<!-- Document will be displayed in \"application mode\" (fullscreen, etc.) --\\>\n<meta name\\=\"x5-page-mode\" content\\=\"app\"\\>\n\n### UC Mobile Browser\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#uc-mobile-browser)\n\n<!-- Locks the screen into the specified orientation --\\>\n<meta name\\=\"screen-orientation\" content\\=\"landscape/portrait\"\\>\n\n<!-- Display this document in fullscreen --\\>\n<meta name\\=\"full-screen\" content\\=\"yes\"\\>\n\n<!-- UC browser will display images even if in \"text mode\" --\\>\n<meta name\\=\"imagemode\" content\\=\"force\"\\>\n\n<!-- Document will be displayed in \"application mode\"(fullscreen, forbidding gesture, etc.) --\\>\n<meta name\\=\"browsermode\" content\\=\"application\"\\>\n\n<!-- Disabled the UC browser's \"night mode\" for this document --\\>\n<meta name\\=\"nightmode\" content\\=\"disable\"\\>\n\n<!-- Simplify the document to reduce data transfer --\\>\n<meta name\\=\"layoutmode\" content\\=\"fitscreen\"\\>\n\n<!-- Disable the UC browser's feature of \"scaling font up when there are many words in this document\" --\\>\n<meta name\\=\"wap-font-scale\" content\\=\"no\"\\>\n\n*   📖 [UC Browser Docs](https://www.uc.cn/download/UCBrowser_U3_API.doc)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nApp Links\n---------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#app-links)\n\n<!-- iOS --\\>\n<meta property\\=\"al:ios:url\" content\\=\"applinks://docs\"\\>\n<meta property\\=\"al:ios:app\\_store\\_id\" content\\=\"12345\"\\>\n<meta property\\=\"al:ios:app\\_name\" content\\=\"App Links\"\\>\n\n<!-- Android --\\>\n<meta property\\=\"al:android:url\" content\\=\"applinks://docs\"\\>\n<meta property\\=\"al:android:app\\_name\" content\\=\"App Links\"\\>\n<meta property\\=\"al:android:package\" content\\=\"org.applinks\"\\>\n\n<!-- Web fall back --\\>\n<meta property\\=\"al:web:url\" content\\=\"https://applinks.org/documentation\"\\>\n\n*   📖 [App Links](https://developers.facebook.com/docs/applinks)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nOther Resources\n---------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#other-resources)\n\n*   📖 [HTML5 Boilerplate Docs: The HTML](https://github.com/h5bp/html5-boilerplate/blob/master/dist/doc/html.md)\n*   📖 [HTML5 Boilerplate Docs: Extend and customize](https://github.com/h5bp/html5-boilerplate/blob/master/dist/doc/extend.md)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nRelated Projects\n----------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#related-projects)\n\n*   [Atom HTML Head Snippets](https://github.com/joshbuchea/atom-html-head-snippets) - Atom package for `HEAD` snippets\n*   [Sublime Text HTML Head Snippets](https://github.com/marcobiedermann/sublime-head-snippets) - Sublime Text package for `HEAD` snippets\n*   [head-it](https://github.com/hemanth/head-it) - CLI interface for `HEAD` snippets\n*   [vue-head](https://github.com/ktquez/vue-head) - Manipulating the meta information of the `HEAD` tag for Vue.js\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\nOther Formats\n-------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#other-formats)\n\n*   📄 [PDF](https://gitprint.com/joshbuchea/HEAD/blob/master/README.md)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\n🌐 Translations\n---------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#-translations)\n\n*   🇮🇩 [Bahasa](https://github.com/rijdz/HEAD)\n*   🇧🇷 [Brazilian Portuguese](https://github.com/Webschool-io/HEAD)\n*   🇨🇳 [Chinese (Simplified)](https://github.com/Amery2010/HEAD)\n*   🇩🇪 [German](https://github.com/Shidigital/HEAD)\n*   🇮🇹 [Italian](https://github.com/Fakkio/HEAD)\n*   🇯🇵 [Japanese](https://coliss.com/articles/build-websites/operation/work/collection-of-html-head-elements.html)\n*   🇰🇷 [Korean](https://github.com/Lutece/HEAD)\n*   🇷🇺 [Russian/Русский](https://github.com/Konfuze/HEAD)\n*   🇪🇸 [Spanish](https://github.com/alvaroadlf/HEAD)\n*   🇹🇷 [Turkish/Türkçe](https://github.com/mkg0/HEAD)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**\n\n🤝 Contributing\n---------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#-contributing)\n\n**Open an issue or a pull request to suggest changes or additions.**\n\n### Guide\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#guide)\n\nThe **HEAD** repository consists of two branches:\n\n#### 1\\. `master`\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#1-master)\n\nThis branch consists of the `README.md` file that is reflected on the [htmlhead.dev](https://htmlhead.dev/) website. All changes to the content of the guide should be made in this file.\n\nPlease follow these steps for pull requests:\n\n{:.list-style-default}\n\n*   Modify only one tag, or one related set of tags at a time\n*   Use double quotes on attributes\n*   Don't include a trailing slash in self-closing elements — the HTML5 spec says they're optional\n*   Consider including a link to documentation that supports your change\n\n#### 2\\. `gh-pages`\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#2-gh-pages)\n\nThis branch is responsible for the [htmlhead.dev](https://htmlhead.dev/) website. We use [Jekyll](https://jekyllrb.com/) to deploy the `README.md` markdown file to [GitHub Pages](https://pages.github.com/). All website related modifications should be made in this branch.\n\nYou may find it helpful to review the [Jekyll Docs](https://jekyllrb.com/docs/home/) and understand how Jekyll works before working in this branch.\n\n🌟 Contributors\n---------------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#-contributors)\n\nCheck out all the super awesome [contributors](https://github.com/joshbuchea/HEAD/graphs/contributors) 🤩\n\n👤 Author\n---------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#-author)\n\n**Josh Buchea**\n\n*   GitHub: [@joshbuchea](https://github.com/joshbuchea)\n*   Mastodon: [@joshbuchea@hachyderm.io](https://hachyderm.io/@joshbuchea)\n\n💛 Support\n----------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#-support)\n\nIf this project was helpful for you or your organization, please considering supporting my work directly:\n\n*   💛 [Sponsor me on GitHub](https://github.com/sponsors/joshbuchea)\n*   ⭐️ [Star this project on GitHub](https://github.com/joshbuchea/HEAD)\n*   🐙 [Follow me on GitHub](https://github.com/joshbuchea)\n*   🐘 [Follow me on Mastodon](https://hachyderm.io/@joshbuchea)\n\nEverything helps, thanks! 🙏\n\n— Josh\n\n📝 License\n----------\n\n[](https://github.com/joshbuchea/HEAD?screenshot=true#-license)\n\n[![Image 28: CC0](https://camo.githubusercontent.com/d2c82b6a501bcd93578124d889803ae99a9d8e0d3e64eb806a1758270fe90185/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f702f7a65726f2f312e302f38387833312e706e67)](https://creativecommons.org/publicdomain/zero/1.0/)\n\n**[⬆ back to top](https://github.com/joshbuchea/HEAD?screenshot=true#table-of-contents)**",
  "usage": {
    "tokens": 8641
  }
}
```
