---
title: File Conventions | Nextra
description: Nextra's File Conventions guide details the structure and organization of files and directories within a Nextra project, including the use of `page.mdx`, `_meta.js`, and `mdx-components.js` files, as well as the `content` and `src` directories.
url: https://nextra.site/docs/guide/organize-files
timestamp: 2025-01-20T16:15:09.432Z
domain: nextra.site
path: docs_guide_organize-files
---

# File Conventions | Nextra


Nextra's File Conventions guide details the structure and organization of files and directories within a Nextra project, including the use of `page.mdx`, `_meta.js`, and `mdx-components.js` files, as well as the `content` and `src` directories.


## Content

File Conventions | Nextra
===============

[Skip to Content](https://nextra.site/docs/guide/organize-files#nextra-skip-nav)

🚧 This is WIP documentation for Nextra 4.0. Dima Machina is looking [for a new job or consulting](https://github.com/dimaMachina) .

[](https://nextra.site/)

[Documentation](https://nextra.site/docs)Versions[Blog](https://nextra.site/blog)[About](https://nextra.site/about)[Showcase](https://nextra.site/showcase)[Sponsors](https://nextra.site/sponsors)

[](https://github.com/shuding/nextra)

*   Documentation
    
    *   [Introduction](https://nextra.site/docs)
    *   [File Conventions](https://nextra.site/docs/file-conventions)
        
        *   Files
        *   [`page.mdx`](https://nextra.site/docs/file-conventions/page-file)
        *   [`_meta.js`](https://nextra.site/docs/file-conventions/meta-file)
        *   [`mdx-components.js`](https://nextra.site/docs/file-conventions/mdx-components-file)
        *   [`page.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/page) 
        *   [`layout.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 
        *   Top-Level Folders
        *   [`content`](https://nextra.site/docs/file-conventions/content-directory)
        *   [`src`](https://nextra.site/docs/file-conventions/src-directory)
        *   [`app`](https://nextjs.org/docs/app/getting-started/installation#create-the-app-directory) 
        *   [`public`](https://nextjs.org/docs/app/building-your-application/optimizing/static-assets) 
        
    *   [Guide](https://nextra.site/docs/guide)
        
        *   [Markdown](https://nextra.site/docs/guide/markdown)
        *   [Syntax Highlighting](https://nextra.site/docs/guide/syntax-highlighting)
        *   [Next.js Link](https://nextra.site/docs/guide/link)
        *   [Next.js Image](https://nextra.site/docs/guide/image)
        *   [Next.js SSG](https://nextra.site/docs/guide/ssg)
        *   [Next.js I18n](https://nextra.site/docs/guide/i18n)
        *   [Custom CSS](https://nextra.site/docs/guide/custom-css)
        *   [Static Exports](https://nextra.site/docs/guide/static-exports)
        *   [Search Engine](https://nextra.site/docs/guide/search)
        *   [GitHub Alert Syntax](https://nextra.site/docs/guide/github-alert-syntax)
        *   [Usage with Turbopack](https://nextra.site/docs/guide/turbopack)
        
    *   [Advanced](https://nextra.site/docs/advanced)
        
        *   [Npm2Yarn](https://nextra.site/docs/advanced/npm2yarn)
        *   [Mermaid](https://nextra.site/docs/advanced/mermaid)
        *   [Tailwind CSS](https://nextra.site/docs/advanced/tailwind-css)
        *   [LaTeX](https://nextra.site/docs/advanced/latex)
        *   [Rendering Tables](https://nextra.site/docs/advanced/table)
        *   [TypeScript](https://nextra.site/docs/advanced/typescript)
        *   [Remote Content](https://nextra.site/docs/advanced/remote)
        *   [Playground](https://nextra.site/docs/advanced/playground)
        *   [Customize Cascade Layers](https://nextra.site/docs/advanced/customize-the-cascade-layers)
        *   [Twoslash Support](https://nextra.site/docs/advanced/twoslash)
        
    *   [Built-In Components](https://nextra.site/docs/built-ins)
        
        *   Layout Components
        *   [Banner](https://nextra.site/docs/built-ins/banner)
        *   [Head](https://nextra.site/docs/built-ins/head)
        *   [Search](https://nextra.site/docs/built-ins/search)
        *   Content Components
        *   [Bleed](https://nextra.site/docs/built-ins/bleed)
        *   [Callout](https://nextra.site/docs/built-ins/callout)
        *   [Cards](https://nextra.site/docs/built-ins/cards)
        *   [FileTree](https://nextra.site/docs/built-ins/filetree)
        *   [Steps](https://nextra.site/docs/built-ins/steps)
        *   [Table](https://nextra.site/docs/built-ins/table)
        *   [Tabs](https://nextra.site/docs/built-ins/tabs)
        
    *   Themes
    *   [Docs Theme](https://nextra.site/docs/docs-theme)
        
        *   [Get Started](https://nextra.site/docs/docs-theme/start)
        *   [Built-In Components](https://nextra.site/docs/docs-theme/built-ins)
            
            *   [Layout](https://nextra.site/docs/docs-theme/built-ins/layout)
            *   [Footer](https://nextra.site/docs/docs-theme/built-ins/footer)
            *   [Navbar](https://nextra.site/docs/docs-theme/built-ins/navbar)
            *   [NotFoundPage](https://nextra.site/docs/docs-theme/built-ins/not-found)
            
        *   [API](https://nextra.site/docs/docs-theme/api)
        
    *   [Blog Theme](https://nextra.site/docs/blog-theme)
        
        *   [Get Started](https://nextra.site/docs/blog-theme/start)
        
    *   [Custom Theme](https://nextra.site/docs/custom-theme)
    *   More
    *   [About Nextra](https://nextra.site/about)
    *   [Next.js Docs](https://nextjs.org/?utm_source=nextra.site&utm_medium=referral&utm_campaign=sidebar) 
    *   [Migration from Nextra v3](https://the-guild.dev/blog/nextra-4?utm_source=nextra.site&utm_campaign=sidebar&utm_content=sidebar_link#nextra-theme-docs-changes) 
    
*   Versions
    
    *   [Nextra v3 Docs](https://nextra-v2-7hslbun8z-shud.vercel.app/) 
    *   [Nextra v2 Docs](https://nextra-v2-oe0zrpzjp-shud.vercel.app/) 
    
*   [Blog](https://nextra.site/blog)
*   [About](https://nextra.site/about)
*   [Showcase](https://nextra.site/showcase)
*   [Sponsors](https://nextra.site/sponsors)

Light

*   [Introduction](https://nextra.site/docs)
*   [File Conventions](https://nextra.site/docs/file-conventions)
    
    *   Files
    *   [`page.mdx`](https://nextra.site/docs/file-conventions/page-file)
    *   [`_meta.js`](https://nextra.site/docs/file-conventions/meta-file)
    *   [`mdx-components.js`](https://nextra.site/docs/file-conventions/mdx-components-file)
    *   [`page.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/page) 
    *   [`layout.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 
    *   Top-Level Folders
    *   [`content`](https://nextra.site/docs/file-conventions/content-directory)
    *   [`src`](https://nextra.site/docs/file-conventions/src-directory)
    *   [`app`](https://nextjs.org/docs/app/getting-started/installation#create-the-app-directory) 
    *   [`public`](https://nextjs.org/docs/app/building-your-application/optimizing/static-assets) 
    
*   [Guide](https://nextra.site/docs/guide)
    
    *   [Markdown](https://nextra.site/docs/guide/markdown)
    *   [Syntax Highlighting](https://nextra.site/docs/guide/syntax-highlighting)
    *   [Next.js Link](https://nextra.site/docs/guide/link)
    *   [Next.js Image](https://nextra.site/docs/guide/image)
    *   [Next.js SSG](https://nextra.site/docs/guide/ssg)
    *   [Next.js I18n](https://nextra.site/docs/guide/i18n)
    *   [Custom CSS](https://nextra.site/docs/guide/custom-css)
    *   [Static Exports](https://nextra.site/docs/guide/static-exports)
    *   [Search Engine](https://nextra.site/docs/guide/search)
    *   [GitHub Alert Syntax](https://nextra.site/docs/guide/github-alert-syntax)
    *   [Usage with Turbopack](https://nextra.site/docs/guide/turbopack)
    
*   [Advanced](https://nextra.site/docs/advanced)
    
    *   [Npm2Yarn](https://nextra.site/docs/advanced/npm2yarn)
    *   [Mermaid](https://nextra.site/docs/advanced/mermaid)
    *   [Tailwind CSS](https://nextra.site/docs/advanced/tailwind-css)
    *   [LaTeX](https://nextra.site/docs/advanced/latex)
    *   [Rendering Tables](https://nextra.site/docs/advanced/table)
    *   [TypeScript](https://nextra.site/docs/advanced/typescript)
    *   [Remote Content](https://nextra.site/docs/advanced/remote)
    *   [Playground](https://nextra.site/docs/advanced/playground)
    *   [Customize Cascade Layers](https://nextra.site/docs/advanced/customize-the-cascade-layers)
    *   [Twoslash Support](https://nextra.site/docs/advanced/twoslash)
    
*   [Built-In Components](https://nextra.site/docs/built-ins)
    
    *   Layout Components
    *   [Banner](https://nextra.site/docs/built-ins/banner)
    *   [Head](https://nextra.site/docs/built-ins/head)
    *   [Search](https://nextra.site/docs/built-ins/search)
    *   Content Components
    *   [Bleed](https://nextra.site/docs/built-ins/bleed)
    *   [Callout](https://nextra.site/docs/built-ins/callout)
    *   [Cards](https://nextra.site/docs/built-ins/cards)
    *   [FileTree](https://nextra.site/docs/built-ins/filetree)
    *   [Steps](https://nextra.site/docs/built-ins/steps)
    *   [Table](https://nextra.site/docs/built-ins/table)
    *   [Tabs](https://nextra.site/docs/built-ins/tabs)
    
*   Themes
*   [Docs Theme](https://nextra.site/docs/docs-theme)
    
    *   [Get Started](https://nextra.site/docs/docs-theme/start)
    *   [Built-In Components](https://nextra.site/docs/docs-theme/built-ins)
        
        *   [Layout](https://nextra.site/docs/docs-theme/built-ins/layout)
        *   [Footer](https://nextra.site/docs/docs-theme/built-ins/footer)
        *   [Navbar](https://nextra.site/docs/docs-theme/built-ins/navbar)
        *   [NotFoundPage](https://nextra.site/docs/docs-theme/built-ins/not-found)
        
    *   [API](https://nextra.site/docs/docs-theme/api)
    
*   [Blog Theme](https://nextra.site/docs/blog-theme)
    
    *   [Get Started](https://nextra.site/docs/blog-theme/start)
    
*   [Custom Theme](https://nextra.site/docs/custom-theme)
*   More
*   [About Nextra](https://nextra.site/about)
*   [Next.js Docs](https://nextjs.org/?utm_source=nextra.site&utm_medium=referral&utm_campaign=sidebar) 
*   [Migration from Nextra v3](https://the-guild.dev/blog/nextra-4?utm_source=nextra.site&utm_campaign=sidebar&utm_content=sidebar_link#nextra-theme-docs-changes) 

Light

On This Page

*   [Page Map Information `pageMap`](https://nextra.site/docs/guide/organize-files#page-map-information-pagemap)

[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CFile%20Conventions%E2%80%9D&labels=feedback) [Edit this page on GitHub](https://github.com/shuding/nextra/tree/main/docs/app/docs/file-conventions/page.mdx) Scroll to top

[Documentation](https://nextra.site/docs "Documentation")File Conventions

File Conventions
================

Files[](https://nextra.site/docs/guide/organize-files#files)
------------------------------------------------------------

[page.mdx](https://nextra.site/docs/file-conventions/page-file)[\_meta.js](https://nextra.site/docs/file-conventions/meta-file)[mdx-components.js](https://nextra.site/docs/file-conventions/mdx-components-file)

Top-Level Folders[](https://nextra.site/docs/guide/organize-files#top-level-folders)
------------------------------------------------------------------------------------

[content](https://nextra.site/docs/file-conventions/content-directory)[src](https://nextra.site/docs/file-conventions/src-directory)

Page Map Information `pageMap`[](https://nextra.site/docs/guide/organize-files#page-map-information-pagemap)
------------------------------------------------------------------------------------------------------------

Nextra collects all your [`page.mdx` files](https://nextra.site/docs/file-conventions/page-file) and [`_meta` files](https://nextra.site/docs/file-conventions/meta-file) from the Next.js’ [`app` directory](https://nextjs.org/docs/app/getting-started/project-structure#top-level-folders) and from Nextra’s [`content` directory](https://nextra.site/docs/file-conventions/content-directory), and then generates the page map information `pageMap` of your entire site, to render things such as the navigation bar and sidebar below:

![Image 3: Example of Nextra Theme Docs](https://nextra.site/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frouting%401x.d02ee37d.png&w=3840&q=75)

Example: [Nextra Docs Theme](https://nextra.site/docs/docs-theme) has sidebar and navbar generated automatically from Markdown files.

The `pageMap` contains all `.md` and `.mdx` filenames and the directory structure, sorted alphabetically. Then, Nextra will use the [title](https://github.com/vercel/title)  package to get formatted page names from filenames.

For example if you have the following structure:

**Using [`content` directory](https://nextra.site/docs/file-conventions/content-directory)**

*   app
    *   \[\[...mdxPath\]\]
        *   page.jsx
    *   layout.jsx
*   content
    *   about
        *   \_meta.js
        *   index.mdx
        *   legal.md
    *   \_meta.js
    *   contact.md
    *   index.mdx

**Using [`page.mdx` files](https://nextra.site/docs/file-conventions/page-file)**

*   app
    *   about
        *   legal
            *   page.md
        *   \_meta.js
        *   page.mdx
    *   contact
        *   page.md
    *   \_meta.js
    *   layout.jsx
    *   page.mdx

The resolved `pageMap` will be:

pageMap

```
[
  // content/_meta.js
  { "data": {} },
  // content/index.mdx
  { "name": "index", "route": "/", "frontMatter": {} },
  // content/contact.md
  { "name": "contact", "route": "/contact", "frontMatter": {} },
  {
    // content/about
    "name": "about",
    "route": "/about",
    "children": [
      // content/about/_meta.js
      { "data": {} },
      // content/about/index.mdx
      { "name": "index", "route": "/about", "frontMatter": {} },
      // content/about/legal.md
      { "name": "legal", "route": "/about/legal", "frontMatter": {} }
    ],
    "title": "About"
  }
]
```

And the global `pageMap` will be imported to each page by Nextra. Then, configured theme will render the actual UI with that `pageMap`.

Last updated on January 18, 2025

[Introduction](https://nextra.site/docs "Introduction")[`page.mdx`](https://nextra.site/docs/file-conventions/page-file "[object Object]")

* * *

[Powered by](https://vercel.com/?utm_source=nextra.site "vercel.com homepage")© 2025 The Nextra Project.

## Metadata

```json
{
  "title": "File Conventions | Nextra",
  "description": "Nextra's File Conventions guide details the structure and organization of files and directories within a Nextra project, including the use of `page.mdx`, `_meta.js`, and `mdx-components.js` files, as well as the `content` and `src` directories.",
  "url": "https://nextra.site/docs/guide/organize-files",
  "content": "File Conventions | Nextra\n===============\n\n[Skip to Content](https://nextra.site/docs/guide/organize-files#nextra-skip-nav)\n\n🚧 This is WIP documentation for Nextra 4.0. Dima Machina is looking [for a new job or consulting](https://github.com/dimaMachina) .\n\n[](https://nextra.site/)\n\n[Documentation](https://nextra.site/docs)Versions[Blog](https://nextra.site/blog)[About](https://nextra.site/about)[Showcase](https://nextra.site/showcase)[Sponsors](https://nextra.site/sponsors)\n\n[](https://github.com/shuding/nextra)\n\n*   Documentation\n    \n    *   [Introduction](https://nextra.site/docs)\n    *   [File Conventions](https://nextra.site/docs/file-conventions)\n        \n        *   Files\n        *   [`page.mdx`](https://nextra.site/docs/file-conventions/page-file)\n        *   [`_meta.js`](https://nextra.site/docs/file-conventions/meta-file)\n        *   [`mdx-components.js`](https://nextra.site/docs/file-conventions/mdx-components-file)\n        *   [`page.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/page) \n        *   [`layout.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) \n        *   Top-Level Folders\n        *   [`content`](https://nextra.site/docs/file-conventions/content-directory)\n        *   [`src`](https://nextra.site/docs/file-conventions/src-directory)\n        *   [`app`](https://nextjs.org/docs/app/getting-started/installation#create-the-app-directory) \n        *   [`public`](https://nextjs.org/docs/app/building-your-application/optimizing/static-assets) \n        \n    *   [Guide](https://nextra.site/docs/guide)\n        \n        *   [Markdown](https://nextra.site/docs/guide/markdown)\n        *   [Syntax Highlighting](https://nextra.site/docs/guide/syntax-highlighting)\n        *   [Next.js Link](https://nextra.site/docs/guide/link)\n        *   [Next.js Image](https://nextra.site/docs/guide/image)\n        *   [Next.js SSG](https://nextra.site/docs/guide/ssg)\n        *   [Next.js I18n](https://nextra.site/docs/guide/i18n)\n        *   [Custom CSS](https://nextra.site/docs/guide/custom-css)\n        *   [Static Exports](https://nextra.site/docs/guide/static-exports)\n        *   [Search Engine](https://nextra.site/docs/guide/search)\n        *   [GitHub Alert Syntax](https://nextra.site/docs/guide/github-alert-syntax)\n        *   [Usage with Turbopack](https://nextra.site/docs/guide/turbopack)\n        \n    *   [Advanced](https://nextra.site/docs/advanced)\n        \n        *   [Npm2Yarn](https://nextra.site/docs/advanced/npm2yarn)\n        *   [Mermaid](https://nextra.site/docs/advanced/mermaid)\n        *   [Tailwind CSS](https://nextra.site/docs/advanced/tailwind-css)\n        *   [LaTeX](https://nextra.site/docs/advanced/latex)\n        *   [Rendering Tables](https://nextra.site/docs/advanced/table)\n        *   [TypeScript](https://nextra.site/docs/advanced/typescript)\n        *   [Remote Content](https://nextra.site/docs/advanced/remote)\n        *   [Playground](https://nextra.site/docs/advanced/playground)\n        *   [Customize Cascade Layers](https://nextra.site/docs/advanced/customize-the-cascade-layers)\n        *   [Twoslash Support](https://nextra.site/docs/advanced/twoslash)\n        \n    *   [Built-In Components](https://nextra.site/docs/built-ins)\n        \n        *   Layout Components\n        *   [Banner](https://nextra.site/docs/built-ins/banner)\n        *   [Head](https://nextra.site/docs/built-ins/head)\n        *   [Search](https://nextra.site/docs/built-ins/search)\n        *   Content Components\n        *   [Bleed](https://nextra.site/docs/built-ins/bleed)\n        *   [Callout](https://nextra.site/docs/built-ins/callout)\n        *   [Cards](https://nextra.site/docs/built-ins/cards)\n        *   [FileTree](https://nextra.site/docs/built-ins/filetree)\n        *   [Steps](https://nextra.site/docs/built-ins/steps)\n        *   [Table](https://nextra.site/docs/built-ins/table)\n        *   [Tabs](https://nextra.site/docs/built-ins/tabs)\n        \n    *   Themes\n    *   [Docs Theme](https://nextra.site/docs/docs-theme)\n        \n        *   [Get Started](https://nextra.site/docs/docs-theme/start)\n        *   [Built-In Components](https://nextra.site/docs/docs-theme/built-ins)\n            \n            *   [Layout](https://nextra.site/docs/docs-theme/built-ins/layout)\n            *   [Footer](https://nextra.site/docs/docs-theme/built-ins/footer)\n            *   [Navbar](https://nextra.site/docs/docs-theme/built-ins/navbar)\n            *   [NotFoundPage](https://nextra.site/docs/docs-theme/built-ins/not-found)\n            \n        *   [API](https://nextra.site/docs/docs-theme/api)\n        \n    *   [Blog Theme](https://nextra.site/docs/blog-theme)\n        \n        *   [Get Started](https://nextra.site/docs/blog-theme/start)\n        \n    *   [Custom Theme](https://nextra.site/docs/custom-theme)\n    *   More\n    *   [About Nextra](https://nextra.site/about)\n    *   [Next.js Docs](https://nextjs.org/?utm_source=nextra.site&utm_medium=referral&utm_campaign=sidebar) \n    *   [Migration from Nextra v3](https://the-guild.dev/blog/nextra-4?utm_source=nextra.site&utm_campaign=sidebar&utm_content=sidebar_link#nextra-theme-docs-changes) \n    \n*   Versions\n    \n    *   [Nextra v3 Docs](https://nextra-v2-7hslbun8z-shud.vercel.app/) \n    *   [Nextra v2 Docs](https://nextra-v2-oe0zrpzjp-shud.vercel.app/) \n    \n*   [Blog](https://nextra.site/blog)\n*   [About](https://nextra.site/about)\n*   [Showcase](https://nextra.site/showcase)\n*   [Sponsors](https://nextra.site/sponsors)\n\nLight\n\n*   [Introduction](https://nextra.site/docs)\n*   [File Conventions](https://nextra.site/docs/file-conventions)\n    \n    *   Files\n    *   [`page.mdx`](https://nextra.site/docs/file-conventions/page-file)\n    *   [`_meta.js`](https://nextra.site/docs/file-conventions/meta-file)\n    *   [`mdx-components.js`](https://nextra.site/docs/file-conventions/mdx-components-file)\n    *   [`page.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/page) \n    *   [`layout.jsx`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) \n    *   Top-Level Folders\n    *   [`content`](https://nextra.site/docs/file-conventions/content-directory)\n    *   [`src`](https://nextra.site/docs/file-conventions/src-directory)\n    *   [`app`](https://nextjs.org/docs/app/getting-started/installation#create-the-app-directory) \n    *   [`public`](https://nextjs.org/docs/app/building-your-application/optimizing/static-assets) \n    \n*   [Guide](https://nextra.site/docs/guide)\n    \n    *   [Markdown](https://nextra.site/docs/guide/markdown)\n    *   [Syntax Highlighting](https://nextra.site/docs/guide/syntax-highlighting)\n    *   [Next.js Link](https://nextra.site/docs/guide/link)\n    *   [Next.js Image](https://nextra.site/docs/guide/image)\n    *   [Next.js SSG](https://nextra.site/docs/guide/ssg)\n    *   [Next.js I18n](https://nextra.site/docs/guide/i18n)\n    *   [Custom CSS](https://nextra.site/docs/guide/custom-css)\n    *   [Static Exports](https://nextra.site/docs/guide/static-exports)\n    *   [Search Engine](https://nextra.site/docs/guide/search)\n    *   [GitHub Alert Syntax](https://nextra.site/docs/guide/github-alert-syntax)\n    *   [Usage with Turbopack](https://nextra.site/docs/guide/turbopack)\n    \n*   [Advanced](https://nextra.site/docs/advanced)\n    \n    *   [Npm2Yarn](https://nextra.site/docs/advanced/npm2yarn)\n    *   [Mermaid](https://nextra.site/docs/advanced/mermaid)\n    *   [Tailwind CSS](https://nextra.site/docs/advanced/tailwind-css)\n    *   [LaTeX](https://nextra.site/docs/advanced/latex)\n    *   [Rendering Tables](https://nextra.site/docs/advanced/table)\n    *   [TypeScript](https://nextra.site/docs/advanced/typescript)\n    *   [Remote Content](https://nextra.site/docs/advanced/remote)\n    *   [Playground](https://nextra.site/docs/advanced/playground)\n    *   [Customize Cascade Layers](https://nextra.site/docs/advanced/customize-the-cascade-layers)\n    *   [Twoslash Support](https://nextra.site/docs/advanced/twoslash)\n    \n*   [Built-In Components](https://nextra.site/docs/built-ins)\n    \n    *   Layout Components\n    *   [Banner](https://nextra.site/docs/built-ins/banner)\n    *   [Head](https://nextra.site/docs/built-ins/head)\n    *   [Search](https://nextra.site/docs/built-ins/search)\n    *   Content Components\n    *   [Bleed](https://nextra.site/docs/built-ins/bleed)\n    *   [Callout](https://nextra.site/docs/built-ins/callout)\n    *   [Cards](https://nextra.site/docs/built-ins/cards)\n    *   [FileTree](https://nextra.site/docs/built-ins/filetree)\n    *   [Steps](https://nextra.site/docs/built-ins/steps)\n    *   [Table](https://nextra.site/docs/built-ins/table)\n    *   [Tabs](https://nextra.site/docs/built-ins/tabs)\n    \n*   Themes\n*   [Docs Theme](https://nextra.site/docs/docs-theme)\n    \n    *   [Get Started](https://nextra.site/docs/docs-theme/start)\n    *   [Built-In Components](https://nextra.site/docs/docs-theme/built-ins)\n        \n        *   [Layout](https://nextra.site/docs/docs-theme/built-ins/layout)\n        *   [Footer](https://nextra.site/docs/docs-theme/built-ins/footer)\n        *   [Navbar](https://nextra.site/docs/docs-theme/built-ins/navbar)\n        *   [NotFoundPage](https://nextra.site/docs/docs-theme/built-ins/not-found)\n        \n    *   [API](https://nextra.site/docs/docs-theme/api)\n    \n*   [Blog Theme](https://nextra.site/docs/blog-theme)\n    \n    *   [Get Started](https://nextra.site/docs/blog-theme/start)\n    \n*   [Custom Theme](https://nextra.site/docs/custom-theme)\n*   More\n*   [About Nextra](https://nextra.site/about)\n*   [Next.js Docs](https://nextjs.org/?utm_source=nextra.site&utm_medium=referral&utm_campaign=sidebar) \n*   [Migration from Nextra v3](https://the-guild.dev/blog/nextra-4?utm_source=nextra.site&utm_campaign=sidebar&utm_content=sidebar_link#nextra-theme-docs-changes) \n\nLight\n\nOn This Page\n\n*   [Page Map Information `pageMap`](https://nextra.site/docs/guide/organize-files#page-map-information-pagemap)\n\n[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CFile%20Conventions%E2%80%9D&labels=feedback) [Edit this page on GitHub](https://github.com/shuding/nextra/tree/main/docs/app/docs/file-conventions/page.mdx) Scroll to top\n\n[Documentation](https://nextra.site/docs \"Documentation\")File Conventions\n\nFile Conventions\n================\n\nFiles[](https://nextra.site/docs/guide/organize-files#files)\n------------------------------------------------------------\n\n[page.mdx](https://nextra.site/docs/file-conventions/page-file)[\\_meta.js](https://nextra.site/docs/file-conventions/meta-file)[mdx-components.js](https://nextra.site/docs/file-conventions/mdx-components-file)\n\nTop-Level Folders[](https://nextra.site/docs/guide/organize-files#top-level-folders)\n------------------------------------------------------------------------------------\n\n[content](https://nextra.site/docs/file-conventions/content-directory)[src](https://nextra.site/docs/file-conventions/src-directory)\n\nPage Map Information `pageMap`[](https://nextra.site/docs/guide/organize-files#page-map-information-pagemap)\n------------------------------------------------------------------------------------------------------------\n\nNextra collects all your [`page.mdx` files](https://nextra.site/docs/file-conventions/page-file) and [`_meta` files](https://nextra.site/docs/file-conventions/meta-file) from the Next.js’ [`app` directory](https://nextjs.org/docs/app/getting-started/project-structure#top-level-folders) and from Nextra’s [`content` directory](https://nextra.site/docs/file-conventions/content-directory), and then generates the page map information `pageMap` of your entire site, to render things such as the navigation bar and sidebar below:\n\n![Image 3: Example of Nextra Theme Docs](https://nextra.site/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frouting%401x.d02ee37d.png&w=3840&q=75)\n\nExample: [Nextra Docs Theme](https://nextra.site/docs/docs-theme) has sidebar and navbar generated automatically from Markdown files.\n\nThe `pageMap` contains all `.md` and `.mdx` filenames and the directory structure, sorted alphabetically. Then, Nextra will use the [title](https://github.com/vercel/title)  package to get formatted page names from filenames.\n\nFor example if you have the following structure:\n\n**Using [`content` directory](https://nextra.site/docs/file-conventions/content-directory)**\n\n*   app\n    *   \\[\\[...mdxPath\\]\\]\n        *   page.jsx\n    *   layout.jsx\n*   content\n    *   about\n        *   \\_meta.js\n        *   index.mdx\n        *   legal.md\n    *   \\_meta.js\n    *   contact.md\n    *   index.mdx\n\n**Using [`page.mdx` files](https://nextra.site/docs/file-conventions/page-file)**\n\n*   app\n    *   about\n        *   legal\n            *   page.md\n        *   \\_meta.js\n        *   page.mdx\n    *   contact\n        *   page.md\n    *   \\_meta.js\n    *   layout.jsx\n    *   page.mdx\n\nThe resolved `pageMap` will be:\n\npageMap\n\n```\n[\n  // content/_meta.js\n  { \"data\": {} },\n  // content/index.mdx\n  { \"name\": \"index\", \"route\": \"/\", \"frontMatter\": {} },\n  // content/contact.md\n  { \"name\": \"contact\", \"route\": \"/contact\", \"frontMatter\": {} },\n  {\n    // content/about\n    \"name\": \"about\",\n    \"route\": \"/about\",\n    \"children\": [\n      // content/about/_meta.js\n      { \"data\": {} },\n      // content/about/index.mdx\n      { \"name\": \"index\", \"route\": \"/about\", \"frontMatter\": {} },\n      // content/about/legal.md\n      { \"name\": \"legal\", \"route\": \"/about/legal\", \"frontMatter\": {} }\n    ],\n    \"title\": \"About\"\n  }\n]\n```\n\nAnd the global `pageMap` will be imported to each page by Nextra. Then, configured theme will render the actual UI with that `pageMap`.\n\nLast updated on January 18, 2025\n\n[Introduction](https://nextra.site/docs \"Introduction\")[`page.mdx`](https://nextra.site/docs/file-conventions/page-file \"[object Object]\")\n\n* * *\n\n[Powered by](https://vercel.com/?utm_source=nextra.site \"vercel.com homepage\")© 2025 The Nextra Project.",
  "usage": {
    "tokens": 3749
  }
}
```
