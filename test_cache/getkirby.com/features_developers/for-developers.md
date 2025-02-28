---
title: For developers
description: A powerful platform: Kirby is built with flexibility and extensibility in mind
url: https://getkirby.com/features/developers
timestamp: 2025-01-20T15:53:54.345Z
domain: getkirby.com
path: features_developers
---

# For developers


A powerful platform: Kirby is built with flexibility and extensibility in mind


## Content

A powerful platform: Kirby is built with flexibility and extensibility in mind
------------------------------------------------------------------------------

For developers

*   Battle-tested flat-file foundation
*   Reliable tech stack
*   Versatile templating
*   Headless or not – you decide
*   Powerful plugin platform
*   Extensive docs & great community
*   Built with security in mind

Stay in control of your data. Kirby stores your data in files and folders. Universally accessible on all operating systems and editable with any text editor.

*   content
    
    *   1\_photography
        
        *   1\_animals
        *   2\_trees
        *   3\_sky
        *   4\_oceans
            
            *   album.txt
            *   attention-sharks.jpg
            *   island-from-above.jpg
            *   jellyfish.jpg
            *   nasty-rocks.jpg
            *   smashed-by-waves.jpg
            
        *   photography.txt
        
    *   2\_notes
        
        *   20190731\_in-the-jungle-of-sumatra
        *   20190905\_through-the-desert
        *   20190926\_himalaya-and-back
        *   20191005\_chasing-waterfalls
        *   20191031\_exploring-the-universe
            
            *   notes.txt
            
        
    *   3\_about
        
        *   about.txt
        
    *   home
        
        *   home.txt
        
    *   error
        
        *   error.txt
        
    *   site.txt
    

*   ### Fast
    
    The file system is much faster than you might think. Most often even way faster than a database. With SSD drives on your server you get a system that can fly.
    
*   ### Resilient
    
    Files and folders are probably the most future-proof way of storing your data. Think version control via Git, simple backup options and syncing via tools like rsync.
    
*   ### Extensible
    
    Combine our flat-file system with databases, APIs or even data from a simple Excel spreadsheet. Kirby handles it all.
    

> Blimey, Kirby has come on a lot since I last used it. A fantastic CMS.

A reliable tech stack
---------------------

Performant, well-tested and cost‑effective

### Modern PHP

Kirby is built on our own PHP micro-framework and can be combined with your favorite PHP libraries. Tested and continously improved over more than 10 years, it fully leverages the power of modern PHP. With over 6,200 automated tests with a code coverage of 95% across the entire CMS backend and more than 80 stable releases since 3.0, we invest heavily into the quality of our foundation.

### [Admin interface framework →](https://lab.getkirby.com/)

Our admin interface is built on Vue.js. It's a playground for your ideas. Extend it with plugins and make it your own with the full power of Vue and an incredibly powerful backend.

### Your frontend

Every project is different, every team and freelancer have their own tools and workflows. With Kirby, you use your own frontend code, your own build process, your own framework. Kirby stays out of your way.

### [Sustainable open-source →](https://github.com/getkirby)

Yes, Kirby has a commercial license that's been keeping us running since 2012. But we believe in the transparency of open-source. Kirby's complete code base is available on GitHub, not hidden behind a paywall. No obfuscation, no secrets. You only need to pay when you're actually going live with a Kirby project.

Kirby comes with a powerful PHP-based template engine. Optimized for speed and equipped with an ultra flexible and intuitive PHP API, you can build your perfect frontend the way you like.

```
<?php snippet('header') ?>

<article class="album">
  <h1><?= $page->title() ?></h1>
  <figure class="cover">
    <?= $cover->resize(800, 600) ?>
  </figure>
  <div class="text">
    <?= $page->text()->kirbytext() ?>
  </div>
  <ul class="gallery">
    <?php foreach ($gallery as $image): ?>
    <li><?= $image->crop(300) ?></li>
    <?php endforeach ?>
  </ul>
</article>

<?php snippet('footer') ?>
```

*   ### [Controllers →](https://getkirby.com/docs/guide/templates/controllers)
    
    Complex logic? Use Kirby’s controllers to filter data collections based on URL query parameters, handle forms, do date-based calculations and more without cluttering your templates. Marie Kondō agrees.
    
*   ### [Models →](https://getkirby.com/docs/guide/templates/page-models)
    
    Super-charge your pages with additional functionalities. Page models extend our default page class and offer unlimited opportunities to customize what a page represents.
    
*   ### [Collections →](https://getkirby.com/docs/guide/templates/collections)
    
    Keep your code DRY with collections. Featured articles, upcoming events, team members – create reusable collections that you can use everywhere.
    
*   ### [Bring your own engine →](https://getkirby.com/docs/reference/plugins/components/template)
    
    Your team is familiar with Twig, Blade or your own template engine? No problem! Our engine can be swapped using a template plugin, or you can create your own.
    

> I probably was never as convinced of something the way I am about Kirby. The last 4 months I solely built on it and I wouldn't want to recommend anything else to my potential clients.

Security
--------

A pro-active policy and good track record

Use Kirby as a headless CMS in combination with a static site generator or your mobile app. Modern system architecture meets the flexibility of a flat-file CMS.

/api/pages/notes/children

```
{
    "code": 200,
    "data": [
        {
            "id": "notes/across-the-ocean",
            "num": 20180421,
            "title": "Across the ocean",
            "url": "/notes/across-the-ocean"
        },
        {
            "id": "notes/a-night-in-the-forest",
            "num": 20180625,
            "title": "A night in the forest",
            "url": "/notes/a-night-in-the-forest"
        },
        {
            "id": "notes/in-the-jungle-of-sumatra",
            "num": 20180731,
            "title": "In the jungle of Sumatra",
            "url": "/notes/in-the-jungle-of-sumatra"
        },
    ],
    "pagination": {
        "page": 1,
        "total": 22,
        "offset": 0,
        "limit": 3
    },
    "status": "ok",
}
```

*   ### REST-ful by nature
    
    Use Kirby like a classic CMS or convert it into a powerful, headless content container. Connect it to mobile applications, static site generators or your custom frontend.
    
*   ### Extensible
    
    Define your own API endpoints and objects. Integrate external data from databases, files or other APIs with data from Kirby into one seamless data source.
    
*   ### Secure
    
    Use our built-in authentication methods to connect securely from the same server or a remote application. Add 2FA and custom auth methods for your API users.
    

> More and more a CMS needs to be headless and flexible to configure. I just love Kirby’s clean & simple panel UI and native JSON support!

*   User management
    ---------------
    
    Work with roles and user permissions to create protected sections on your site. From client areas to communities: Kirby’s user system has got you covered.
    
    [Learn more →](https://getkirby.com/docs/guide/users)
    
    ```
    if ($user = $kirby->user()) {
      echo 'Welcome, ' . $user->name();
      // your community starts here
    }
    ```
    
*   Media API
    ---------
    
    Kirby comes with async image processing. Resize, crop and convert your images on the fly. Make sure that every visitor gets the perfect image size.
    
    [Learn more →](https://getkirby.com/docs/guide/files/resize-images-on-the-fly)
    
    ```
    $image->srcset(
      '1x' => [
        'width' => 512,
        'height' => 512,
        'crop' => 'center'
      ],
      '2x' => [
        'width' => 1024
      ]
    ]);
    ```
    
*   Caching
    -------
    
    Kirby comes with mighty caching on board. Not the right fit for your project? Add your cache driver of choice and reduce page loading times in the blink of an eye.
    
    [Learn more →](https://getkirby.com/docs/guide/cache)
    
    ```
    return [
      'cache' => [
        'pages' => [
          'active' => true,
          'type' => 'memcached'
        ]
      ]
    ];
    ```
    

Say yes with confidence when the client asks for changes. Pretty much any aspect of Kirby can be extended - with [existing plugins](https://plugins.getkirby.com/) or custom solutions for your project.

*   ### Custom sections & fields
    
    Add entirely new interface elements to the Panel with custom sections. Integrate data from analytics tools, your ERM system, third-party services and more and use them seamlessly alongside your content. Use the power of Vue.js to create truly interactive plugins.
    
*   ### Hooks
    
    React to specific events with hooks and trigger your own actions. Resize a file on upload, add data to a newly created page, add custom content validations and more.
    
*   ### [Core components →](https://getkirby.com/docs/reference/plugins/components)
    
    You don't like our template engine, Markdown parser or media API? Simply swap out major parts of the Kirby system with your own plugins.
    
*   ### [Routes →](https://getkirby.com/docs/guide/routing)
    
    Routing has never been easier: Kirby comes with a powerful router that can be extended to adjust the URL scheme, handle form submissions, add webhook endpoints or create virtual pages.
    

> Kirby is such a pleasure to work with

And so much more
----------------

Kirby is packed with features that empower you to build amazing sites.

*   [Routing](https://getkirby.com/docs/guide/routing)
*   [Caching](https://getkirby.com/docs/guide/cache)
*   [Emailing](https://getkirby.com/docs/guide/emails)
*   [Languages](https://getkirby.com/for/creators#internationalisation)
*   [Publishing](https://getkirby.com/docs/guide/content/publishing-workflow)
*   [Authentication](https://getkirby.com/docs/guide/authentication)
*   [Virtual pages](https://getkirby.com/docs/guide/virtual-content)
*   [Hooks](https://getkirby.com/docs/reference/plugins/extensions/hooks)
*   [Content representations](https://getkirby.com/docs/guide/templates/content-representations)
*   [Multi-site setup](https://getkirby.com/docs/guide/configuration/multisite-setup)

What are you waiting for?
-------------------------

[Try now](https://getkirby.com/try) [Docs](https://getkirby.com/docs/guide/quickstart)

## Metadata

```json
{
  "title": "For developers",
  "description": "A powerful platform: Kirby is built with flexibility and extensibility in mind",
  "url": "https://getkirby.com/features/developers",
  "content": "A powerful platform: Kirby is built with flexibility and extensibility in mind\n------------------------------------------------------------------------------\n\nFor developers\n\n*   Battle-tested flat-file foundation\n*   Reliable tech stack\n*   Versatile templating\n*   Headless or not – you decide\n*   Powerful plugin platform\n*   Extensive docs & great community\n*   Built with security in mind\n\nStay in control of your data. Kirby stores your data in files and folders. Universally accessible on all operating systems and editable with any text editor.\n\n*   content\n    \n    *   1\\_photography\n        \n        *   1\\_animals\n        *   2\\_trees\n        *   3\\_sky\n        *   4\\_oceans\n            \n            *   album.txt\n            *   attention-sharks.jpg\n            *   island-from-above.jpg\n            *   jellyfish.jpg\n            *   nasty-rocks.jpg\n            *   smashed-by-waves.jpg\n            \n        *   photography.txt\n        \n    *   2\\_notes\n        \n        *   20190731\\_in-the-jungle-of-sumatra\n        *   20190905\\_through-the-desert\n        *   20190926\\_himalaya-and-back\n        *   20191005\\_chasing-waterfalls\n        *   20191031\\_exploring-the-universe\n            \n            *   notes.txt\n            \n        \n    *   3\\_about\n        \n        *   about.txt\n        \n    *   home\n        \n        *   home.txt\n        \n    *   error\n        \n        *   error.txt\n        \n    *   site.txt\n    \n\n*   ### Fast\n    \n    The file system is much faster than you might think. Most often even way faster than a database. With SSD drives on your server you get a system that can fly.\n    \n*   ### Resilient\n    \n    Files and folders are probably the most future-proof way of storing your data. Think version control via Git, simple backup options and syncing via tools like rsync.\n    \n*   ### Extensible\n    \n    Combine our flat-file system with databases, APIs or even data from a simple Excel spreadsheet. Kirby handles it all.\n    \n\n> Blimey, Kirby has come on a lot since I last used it. A fantastic CMS.\n\nA reliable tech stack\n---------------------\n\nPerformant, well-tested and cost‑effective\n\n### Modern PHP\n\nKirby is built on our own PHP micro-framework and can be combined with your favorite PHP libraries. Tested and continously improved over more than 10 years, it fully leverages the power of modern PHP. With over 6,200 automated tests with a code coverage of 95% across the entire CMS backend and more than 80 stable releases since 3.0, we invest heavily into the quality of our foundation.\n\n### [Admin interface framework →](https://lab.getkirby.com/)\n\nOur admin interface is built on Vue.js. It's a playground for your ideas. Extend it with plugins and make it your own with the full power of Vue and an incredibly powerful backend.\n\n### Your frontend\n\nEvery project is different, every team and freelancer have their own tools and workflows. With Kirby, you use your own frontend code, your own build process, your own framework. Kirby stays out of your way.\n\n### [Sustainable open-source →](https://github.com/getkirby)\n\nYes, Kirby has a commercial license that's been keeping us running since 2012. But we believe in the transparency of open-source. Kirby's complete code base is available on GitHub, not hidden behind a paywall. No obfuscation, no secrets. You only need to pay when you're actually going live with a Kirby project.\n\nKirby comes with a powerful PHP-based template engine. Optimized for speed and equipped with an ultra flexible and intuitive PHP API, you can build your perfect frontend the way you like.\n\n```\n<?php snippet('header') ?>\n\n<article class=\"album\">\n  <h1><?= $page->title() ?></h1>\n  <figure class=\"cover\">\n    <?= $cover->resize(800, 600) ?>\n  </figure>\n  <div class=\"text\">\n    <?= $page->text()->kirbytext() ?>\n  </div>\n  <ul class=\"gallery\">\n    <?php foreach ($gallery as $image): ?>\n    <li><?= $image->crop(300) ?></li>\n    <?php endforeach ?>\n  </ul>\n</article>\n\n<?php snippet('footer') ?>\n```\n\n*   ### [Controllers →](https://getkirby.com/docs/guide/templates/controllers)\n    \n    Complex logic? Use Kirby’s controllers to filter data collections based on URL query parameters, handle forms, do date-based calculations and more without cluttering your templates. Marie Kondō agrees.\n    \n*   ### [Models →](https://getkirby.com/docs/guide/templates/page-models)\n    \n    Super-charge your pages with additional functionalities. Page models extend our default page class and offer unlimited opportunities to customize what a page represents.\n    \n*   ### [Collections →](https://getkirby.com/docs/guide/templates/collections)\n    \n    Keep your code DRY with collections. Featured articles, upcoming events, team members – create reusable collections that you can use everywhere.\n    \n*   ### [Bring your own engine →](https://getkirby.com/docs/reference/plugins/components/template)\n    \n    Your team is familiar with Twig, Blade or your own template engine? No problem! Our engine can be swapped using a template plugin, or you can create your own.\n    \n\n> I probably was never as convinced of something the way I am about Kirby. The last 4 months I solely built on it and I wouldn't want to recommend anything else to my potential clients.\n\nSecurity\n--------\n\nA pro-active policy and good track record\n\nUse Kirby as a headless CMS in combination with a static site generator or your mobile app. Modern system architecture meets the flexibility of a flat-file CMS.\n\n/api/pages/notes/children\n\n```\n{\n    \"code\": 200,\n    \"data\": [\n        {\n            \"id\": \"notes/across-the-ocean\",\n            \"num\": 20180421,\n            \"title\": \"Across the ocean\",\n            \"url\": \"/notes/across-the-ocean\"\n        },\n        {\n            \"id\": \"notes/a-night-in-the-forest\",\n            \"num\": 20180625,\n            \"title\": \"A night in the forest\",\n            \"url\": \"/notes/a-night-in-the-forest\"\n        },\n        {\n            \"id\": \"notes/in-the-jungle-of-sumatra\",\n            \"num\": 20180731,\n            \"title\": \"In the jungle of Sumatra\",\n            \"url\": \"/notes/in-the-jungle-of-sumatra\"\n        },\n    ],\n    \"pagination\": {\n        \"page\": 1,\n        \"total\": 22,\n        \"offset\": 0,\n        \"limit\": 3\n    },\n    \"status\": \"ok\",\n}\n```\n\n*   ### REST-ful by nature\n    \n    Use Kirby like a classic CMS or convert it into a powerful, headless content container. Connect it to mobile applications, static site generators or your custom frontend.\n    \n*   ### Extensible\n    \n    Define your own API endpoints and objects. Integrate external data from databases, files or other APIs with data from Kirby into one seamless data source.\n    \n*   ### Secure\n    \n    Use our built-in authentication methods to connect securely from the same server or a remote application. Add 2FA and custom auth methods for your API users.\n    \n\n> More and more a CMS needs to be headless and flexible to configure. I just love Kirby’s clean & simple panel UI and native JSON support!\n\n*   User management\n    ---------------\n    \n    Work with roles and user permissions to create protected sections on your site. From client areas to communities: Kirby’s user system has got you covered.\n    \n    [Learn more →](https://getkirby.com/docs/guide/users)\n    \n    ```\n    if ($user = $kirby->user()) {\n      echo 'Welcome, ' . $user->name();\n      // your community starts here\n    }\n    ```\n    \n*   Media API\n    ---------\n    \n    Kirby comes with async image processing. Resize, crop and convert your images on the fly. Make sure that every visitor gets the perfect image size.\n    \n    [Learn more →](https://getkirby.com/docs/guide/files/resize-images-on-the-fly)\n    \n    ```\n    $image->srcset(\n      '1x' => [\n        'width' => 512,\n        'height' => 512,\n        'crop' => 'center'\n      ],\n      '2x' => [\n        'width' => 1024\n      ]\n    ]);\n    ```\n    \n*   Caching\n    -------\n    \n    Kirby comes with mighty caching on board. Not the right fit for your project? Add your cache driver of choice and reduce page loading times in the blink of an eye.\n    \n    [Learn more →](https://getkirby.com/docs/guide/cache)\n    \n    ```\n    return [\n      'cache' => [\n        'pages' => [\n          'active' => true,\n          'type' => 'memcached'\n        ]\n      ]\n    ];\n    ```\n    \n\nSay yes with confidence when the client asks for changes. Pretty much any aspect of Kirby can be extended - with [existing plugins](https://plugins.getkirby.com/) or custom solutions for your project.\n\n*   ### Custom sections & fields\n    \n    Add entirely new interface elements to the Panel with custom sections. Integrate data from analytics tools, your ERM system, third-party services and more and use them seamlessly alongside your content. Use the power of Vue.js to create truly interactive plugins.\n    \n*   ### Hooks\n    \n    React to specific events with hooks and trigger your own actions. Resize a file on upload, add data to a newly created page, add custom content validations and more.\n    \n*   ### [Core components →](https://getkirby.com/docs/reference/plugins/components)\n    \n    You don't like our template engine, Markdown parser or media API? Simply swap out major parts of the Kirby system with your own plugins.\n    \n*   ### [Routes →](https://getkirby.com/docs/guide/routing)\n    \n    Routing has never been easier: Kirby comes with a powerful router that can be extended to adjust the URL scheme, handle form submissions, add webhook endpoints or create virtual pages.\n    \n\n> Kirby is such a pleasure to work with\n\nAnd so much more\n----------------\n\nKirby is packed with features that empower you to build amazing sites.\n\n*   [Routing](https://getkirby.com/docs/guide/routing)\n*   [Caching](https://getkirby.com/docs/guide/cache)\n*   [Emailing](https://getkirby.com/docs/guide/emails)\n*   [Languages](https://getkirby.com/for/creators#internationalisation)\n*   [Publishing](https://getkirby.com/docs/guide/content/publishing-workflow)\n*   [Authentication](https://getkirby.com/docs/guide/authentication)\n*   [Virtual pages](https://getkirby.com/docs/guide/virtual-content)\n*   [Hooks](https://getkirby.com/docs/reference/plugins/extensions/hooks)\n*   [Content representations](https://getkirby.com/docs/guide/templates/content-representations)\n*   [Multi-site setup](https://getkirby.com/docs/guide/configuration/multisite-setup)\n\nWhat are you waiting for?\n-------------------------\n\n[Try now](https://getkirby.com/try) [Docs](https://getkirby.com/docs/guide/quickstart)",
  "usage": {
    "tokens": 2433
  }
}
```
