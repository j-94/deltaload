---
title: Building Your Application: Deploying | Next.js
description: Learn how to deploy your Next.js app to production, either managed or self-hosted.
url: https://nextjs.org/docs/pages/building-your-application/deploying
timestamp: 2025-01-20T16:03:54.395Z
domain: nextjs.org
path: docs_pages_building-your-application_deploying
---

# Building Your Application: Deploying | Next.js


Learn how to deploy your Next.js app to production, either managed or self-hosted.


## Content

Building Your Application: Deploying | Next.js
===============

[Skip to content](https://nextjs.org/docs/pages/building-your-application/deploying#geist-skip-nav)

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_pages_building-your-application_deploying "Go to Vercel homepage")

[![Image 9: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

[](https://nextjs.org/ "Go to the homepage")

Search documentation...Search...⌘K

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_pages_building-your-application_deploying "Go to Vercel homepage")

[![Image 10: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

[](https://nextjs.org/ "Go to the homepage")

[Showcase](https://nextjs.org/showcase)[Docs](https://nextjs.org/docs "Documentation")[Blog](https://nextjs.org/blog)[Templates](https://vercel.com/templates/next.js?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_templates)[Enterprise](https://vercel.com/contact/sales/nextjs?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_enterprise)

Search documentation...Search...⌘KFeedback[Learn](https://nextjs.org/learn)

Menu

Using App Router

Features available in /app

Using Latest Version

15.1.5

*   [Getting Started](https://nextjs.org/docs/app/getting-started)
    
    *   [Installation](https://nextjs.org/docs/app/getting-started/installation)
    *   [Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
    *   [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
    *   [Images and Fonts](https://nextjs.org/docs/app/getting-started/images-and-fonts)
    *   [CSS and Styling](https://nextjs.org/docs/app/getting-started/css-and-styling)
    *   [Fetching data and streaming](https://nextjs.org/docs/app/getting-started/data-fetching-and-streaming)
    *   [Mutating Data](https://nextjs.org/docs/app/getting-started/mutating-data)
    *   [Error handling](https://nextjs.org/docs/app/getting-started/error-handling)
    

*   [Examples](https://nextjs.org/docs/app/examples)

*   [Building Your Application](https://nextjs.org/docs/app/building-your-application)
    
    *   [Routing](https://nextjs.org/docs/app/building-your-application/routing)
        
        *   [Layouts and Templates](https://nextjs.org/docs/app/building-your-application/routing/layouts-and-templates)
        *   [Linking and Navigating](https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating)
        *   [Error Handling](https://nextjs.org/docs/app/building-your-application/routing/error-handling)
        *   [Loading UI and Streaming](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming)
        *   [Redirecting](https://nextjs.org/docs/app/building-your-application/routing/redirecting)
        *   [Route Groups](https://nextjs.org/docs/app/building-your-application/routing/route-groups)
        *   [Dynamic Routes](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes)
        *   [Parallel Routes](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes)
        *   [Intercepting Routes](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes)
        *   [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)
        *   [Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware)
        *   [Internationalization](https://nextjs.org/docs/app/building-your-application/routing/internationalization)
        
    *   [Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching)
        
        *   [Data Fetching and Caching](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching)
        *   [Server Actions and Mutations](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)
        *   [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration)
        
    *   [Rendering](https://nextjs.org/docs/app/building-your-application/rendering)
        
        *   [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)
        *   [Client Components](https://nextjs.org/docs/app/building-your-application/rendering/client-components)
        *   [Composition Patterns](https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns)
        *   [Partial Prerendering](https://nextjs.org/docs/app/building-your-application/rendering/partial-prerendering)
        *   [Runtimes](https://nextjs.org/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes)
        
    *   [Caching](https://nextjs.org/docs/app/building-your-application/caching)
    *   [Styling](https://nextjs.org/docs/app/building-your-application/styling)
        
        *   [CSS](https://nextjs.org/docs/app/building-your-application/styling/css)
        *   [Tailwind CSS](https://nextjs.org/docs/app/building-your-application/styling/tailwind-css)
        *   [Sass](https://nextjs.org/docs/app/building-your-application/styling/sass)
        *   [CSS-in-JS](https://nextjs.org/docs/app/building-your-application/styling/css-in-js)
        
    *   [Optimizing](https://nextjs.org/docs/app/building-your-application/optimizing)
        
        *   [Images](https://nextjs.org/docs/app/building-your-application/optimizing/images)
        *   [Videos](https://nextjs.org/docs/app/building-your-application/optimizing/videos)
        *   [Fonts](https://nextjs.org/docs/app/building-your-application/optimizing/fonts)
        *   [Metadata](https://nextjs.org/docs/app/building-your-application/optimizing/metadata)
        *   [Scripts](https://nextjs.org/docs/app/building-your-application/optimizing/scripts)
        *   [Package Bundling](https://nextjs.org/docs/app/building-your-application/optimizing/package-bundling)
        *   [Lazy Loading](https://nextjs.org/docs/app/building-your-application/optimizing/lazy-loading)
        *   [Analytics](https://nextjs.org/docs/app/building-your-application/optimizing/analytics)
        *   [Instrumentation](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation)
        *   [OpenTelemetry](https://nextjs.org/docs/app/building-your-application/optimizing/open-telemetry)
        *   [Static Assets](https://nextjs.org/docs/app/building-your-application/optimizing/static-assets)
        *   [Third Party Libraries](https://nextjs.org/docs/app/building-your-application/optimizing/third-party-libraries)
        *   [Memory Usage](https://nextjs.org/docs/app/building-your-application/optimizing/memory-usage)
        
    *   [Configuring](https://nextjs.org/docs/app/building-your-application/configuring)
        
        *   [Environment Variables](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)
        *   [MDX](https://nextjs.org/docs/app/building-your-application/configuring/mdx)
        *   [src Directory](https://nextjs.org/docs/app/building-your-application/configuring/src-directory)
        *   [Custom Server](https://nextjs.org/docs/app/building-your-application/configuring/custom-server)
        *   [Draft Mode](https://nextjs.org/docs/app/building-your-application/configuring/draft-mode)
        *   [Content Security Policy](https://nextjs.org/docs/app/building-your-application/configuring/content-security-policy)
        *   [Debugging](https://nextjs.org/docs/app/building-your-application/configuring/debugging)
        *   [Progressive Web Applications (PWA)](https://nextjs.org/docs/app/building-your-application/configuring/progressive-web-apps)
        
    *   [Testing](https://nextjs.org/docs/app/building-your-application/testing)
        
        *   [Vitest](https://nextjs.org/docs/app/building-your-application/testing/vitest)
        *   [Jest](https://nextjs.org/docs/app/building-your-application/testing/jest)
        *   [Playwright](https://nextjs.org/docs/app/building-your-application/testing/playwright)
        *   [Cypress](https://nextjs.org/docs/app/building-your-application/testing/cypress)
        
    *   [Authentication](https://nextjs.org/docs/app/building-your-application/authentication)
    *   [Deploying](https://nextjs.org/docs/app/building-your-application/deploying)
        
        *   [Production Checklist](https://nextjs.org/docs/app/building-your-application/deploying/production-checklist)
        *   [Static Exports](https://nextjs.org/docs/app/building-your-application/deploying/static-exports)
        *   [Multi-Zones](https://nextjs.org/docs/app/building-your-application/deploying/multi-zones)
        
    *   [Upgrading](https://nextjs.org/docs/app/building-your-application/upgrading)
        
        *   [Codemods](https://nextjs.org/docs/app/building-your-application/upgrading/codemods)
        *   [Canary](https://nextjs.org/docs/app/building-your-application/upgrading/canary)
        *   [Version 15](https://nextjs.org/docs/app/building-your-application/upgrading/version-15)
        *   [Version 14](https://nextjs.org/docs/app/building-your-application/upgrading/version-14)
        *   [App Router Migration](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration)
        *   [Migrating from CRA](https://nextjs.org/docs/app/building-your-application/upgrading/from-create-react-app)
        *   [Migrating from Vite](https://nextjs.org/docs/app/building-your-application/upgrading/from-vite)
        *   [Single-Page Apps](https://nextjs.org/docs/app/building-your-application/upgrading/single-page-applications)
        
    

*   [API Reference](https://nextjs.org/docs/app/api-reference)
    
    *   [Directives](https://nextjs.org/docs/app/api-reference/directives)
        
        *   [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
        *   [use client](https://nextjs.org/docs/app/api-reference/directives/use-client)
        *   [use server](https://nextjs.org/docs/app/api-reference/directives/use-server)
        
    *   [Components](https://nextjs.org/docs/app/api-reference/components)
        
        *   [Font](https://nextjs.org/docs/app/api-reference/components/font)
        *   [Form](https://nextjs.org/docs/app/api-reference/components/form)
        *   [Image](https://nextjs.org/docs/app/api-reference/components/image)
        *   [Link](https://nextjs.org/docs/app/api-reference/components/link)
        *   [Script](https://nextjs.org/docs/app/api-reference/components/script)
        
    *   [File Conventions](https://nextjs.org/docs/app/api-reference/file-conventions)
        
        *   [default.js](https://nextjs.org/docs/app/api-reference/file-conventions/default)
        *   [error.js](https://nextjs.org/docs/app/api-reference/file-conventions/error)
        *   [forbidden.js](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
        *   [instrumentation.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)
        *   [layout.js](https://nextjs.org/docs/app/api-reference/file-conventions/layout)
        *   [loading.js](https://nextjs.org/docs/app/api-reference/file-conventions/loading)
        *   [mdx-components.js](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components)
        *   [middleware.js](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)
        *   [not-found.js](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)
        *   [page.js](https://nextjs.org/docs/app/api-reference/file-conventions/page)
        *   [route.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)
        *   [Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)
        *   [template.js](https://nextjs.org/docs/app/api-reference/file-conventions/template)
        *   [unauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
        *   [Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)
            
            *   [favicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
            *   [manifest.json](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
            *   [opengraph-image and twitter-image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
            *   [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)
            *   [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
            
        
    *   [Functions](https://nextjs.org/docs/app/api-reference/functions)
        
        *   [after](https://nextjs.org/docs/app/api-reference/functions/after)
        *   [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
        *   [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
        *   [connection](https://nextjs.org/docs/app/api-reference/functions/connection)
        *   [cookies](https://nextjs.org/docs/app/api-reference/functions/cookies)
        *   [draftMode](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
        *   [fetch](https://nextjs.org/docs/app/api-reference/functions/fetch)
        *   [forbidden](https://nextjs.org/docs/app/api-reference/functions/forbidden)
        *   [generateImageMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)
        *   [generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)
        *   [generateSitemaps](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)
        *   [generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)
        *   [generateViewport](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)
        *   [headers](https://nextjs.org/docs/app/api-reference/functions/headers)
        *   [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response)
        *   [NextRequest](https://nextjs.org/docs/app/api-reference/functions/next-request)
        *   [NextResponse](https://nextjs.org/docs/app/api-reference/functions/next-response)
        *   [notFound](https://nextjs.org/docs/app/api-reference/functions/not-found)
        *   [permanentRedirect](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)
        *   [redirect](https://nextjs.org/docs/app/api-reference/functions/redirect)
        *   [revalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)
        *   [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
        *   [unauthorized](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
        *   [unstable\_cache](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)
        *   [unstable\_expirePath](https://nextjs.org/docs/app/api-reference/functions/unstable_expirePath)
        *   [unstable\_expireTag](https://nextjs.org/docs/app/api-reference/functions/unstable_expireTag)
        *   [unstable\_noStore](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)
        *   [unstable\_rethrow](https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow)
        *   [useParams](https://nextjs.org/docs/app/api-reference/functions/use-params)
        *   [usePathname](https://nextjs.org/docs/app/api-reference/functions/use-pathname)
        *   [useReportWebVitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)
        *   [useRouter](https://nextjs.org/docs/app/api-reference/functions/use-router)
        *   [useSearchParams](https://nextjs.org/docs/app/api-reference/functions/use-search-params)
        *   [useSelectedLayoutSegment](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment)
        *   [useSelectedLayoutSegments](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)
        *   [userAgent](https://nextjs.org/docs/app/api-reference/functions/userAgent)
        
    *   [Configuration](https://nextjs.org/docs/app/api-reference/config)
        
        *   [next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)
            
            *   [appDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir)
            *   [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)
            *   [authInterrupts](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)
            *   [basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)
            *   [cacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)
            *   [compress](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress)
            *   [crossOrigin](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin)
            *   [cssChunking](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking)
            *   [devIndicators](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators)
            *   [distDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir)
            *   [dynamicIO](https://nextjs.org/docs/app/api-reference/config/next-config-js/dynamicIO)
            *   [env](https://nextjs.org/docs/app/api-reference/config/next-config-js/env)
            *   [eslint](https://nextjs.org/docs/app/api-reference/config/next-config-js/eslint)
            *   [expireTime](https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime)
            *   [exportPathMap](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap)
            *   [generateBuildId](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)
            *   [generateEtags](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags)
            *   [headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)
            *   [httpAgentOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions)
            *   [images](https://nextjs.org/docs/app/api-reference/config/next-config-js/images)
            *   [cacheHandler](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)
            *   [inlineCss](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss)
            *   [logging](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)
            *   [mdxRs](https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs)
            *   [onDemandEntries](https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries)
            *   [optimizePackageImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)
            *   [output](https://nextjs.org/docs/app/api-reference/config/next-config-js/output)
            *   [pageExtensions](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)
            *   [poweredByHeader](https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader)
            *   [ppr](https://nextjs.org/docs/app/api-reference/config/next-config-js/ppr)
            *   [productionBrowserSourceMaps](https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [reactCompiler](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler)
            *   [reactMaxHeadersLength](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)
            *   [reactStrictMode](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode)
            *   [redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
            *   [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)
            *   [sassOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions)
            *   [serverActions](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)
            *   [serverComponentsHmrCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)
            *   [serverExternalPackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages)
            *   [staleTimes](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)
            *   [staticGeneration\*](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration)
            *   [trailingSlash](https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash)
            *   [transpilePackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages)
            *   [turbo](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbo)
            *   [typedRoutes](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes)
            *   [typescript](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript)
            *   [urlImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports)
            *   [useLightningcss](https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss)
            *   [webpack](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)
            *   [webVitalsAttribution](https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution)
            
        *   [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript)
        *   [ESLint](https://nextjs.org/docs/app/api-reference/config/eslint)
        
    *   [CLI](https://nextjs.org/docs/app/api-reference/cli)
        
        *   [create-next-app](https://nextjs.org/docs/app/api-reference/cli/create-next-app)
        *   [next CLI](https://nextjs.org/docs/app/api-reference/cli/next)
        
    *   [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)
    *   [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)
    

*   [Getting Started](https://nextjs.org/docs/pages/getting-started)
    
    *   [Installation](https://nextjs.org/docs/pages/getting-started/installation)
    *   [Project Structure](https://nextjs.org/docs/pages/getting-started/project-structure)
    

*   [Building Your Application](https://nextjs.org/docs/pages/building-your-application)
    
    *   [Routing](https://nextjs.org/docs/pages/building-your-application/routing)
        
        *   [Pages and Layouts](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)
        *   [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)
        *   [Linking and Navigating](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating)
        *   [Redirecting](https://nextjs.org/docs/pages/building-your-application/routing/redirecting)
        *   [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)
        *   [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)
        *   [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
        *   [Custom Errors](https://nextjs.org/docs/pages/building-your-application/routing/custom-error)
        *   [Internationalization](https://nextjs.org/docs/pages/building-your-application/routing/internationalization)
        *   [Middleware](https://nextjs.org/docs/pages/building-your-application/routing/middleware)
        
    *   [Rendering](https://nextjs.org/docs/pages/building-your-application/rendering)
        
        *   [Server-side Rendering (SSR)](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)
        *   [Static Site Generation (SSG)](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)
        *   [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)
        *   [Client-side Rendering (CSR)](https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering)
        *   [Edge and Node.js Runtimes](https://nextjs.org/docs/pages/building-your-application/rendering/edge-and-nodejs-runtimes)
        
    *   [Data Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching)
        
        *   [getStaticProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
        *   [getStaticPaths](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)
        *   [Forms and Mutations](https://nextjs.org/docs/pages/building-your-application/data-fetching/forms-and-mutations)
        *   [getServerSideProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
        *   [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration)
        *   [Client-side Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)
        
    *   [Styling](https://nextjs.org/docs/pages/building-your-application/styling)
        
        *   [CSS](https://nextjs.org/docs/pages/building-your-application/styling/css)
        *   [Tailwind CSS](https://nextjs.org/docs/pages/building-your-application/styling/tailwind-css)
        *   [CSS-in-JS](https://nextjs.org/docs/pages/building-your-application/styling/css-in-js)
        *   [Sass](https://nextjs.org/docs/pages/building-your-application/styling/sass)
        
    *   [Optimizing](https://nextjs.org/docs/pages/building-your-application/optimizing)
        
        *   [Images](https://nextjs.org/docs/pages/building-your-application/optimizing/images)
        *   [Fonts](https://nextjs.org/docs/pages/building-your-application/optimizing/fonts)
        *   [Scripts](https://nextjs.org/docs/pages/building-your-application/optimizing/scripts)
        *   [Static Assets](https://nextjs.org/docs/pages/building-your-application/optimizing/static-assets)
        *   [Bundling](https://nextjs.org/docs/pages/building-your-application/optimizing/package-bundling)
        *   [Analytics](https://nextjs.org/docs/pages/building-your-application/optimizing/analytics)
        *   [Lazy Loading](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading)
        *   [Instrumentation](https://nextjs.org/docs/pages/building-your-application/optimizing/instrumentation)
        *   [OpenTelemetry](https://nextjs.org/docs/pages/building-your-application/optimizing/open-telemetry)
        *   [Third Party Libraries](https://nextjs.org/docs/pages/building-your-application/optimizing/third-party-libraries)
        
    *   [Configuring](https://nextjs.org/docs/pages/building-your-application/configuring)
        
        *   [Environment Variables](https://nextjs.org/docs/pages/building-your-application/configuring/environment-variables)
        *   [src Directory](https://nextjs.org/docs/pages/building-your-application/configuring/src-directory)
        *   [MDX](https://nextjs.org/docs/pages/building-your-application/configuring/mdx)
        *   [AMP](https://nextjs.org/docs/pages/building-your-application/configuring/amp)
        *   [Babel](https://nextjs.org/docs/pages/building-your-application/configuring/babel)
        *   [PostCSS](https://nextjs.org/docs/pages/building-your-application/configuring/post-css)
        *   [Custom Server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server)
        *   [Draft Mode](https://nextjs.org/docs/pages/building-your-application/configuring/draft-mode)
        *   [Error Handling](https://nextjs.org/docs/pages/building-your-application/configuring/error-handling)
        *   [Preview Mode](https://nextjs.org/docs/pages/building-your-application/configuring/preview-mode)
        *   [Content Security Policy](https://nextjs.org/docs/pages/building-your-application/configuring/content-security-policy)
        *   [Debugging](https://nextjs.org/docs/pages/building-your-application/configuring/debugging)
        
    *   [Testing](https://nextjs.org/docs/pages/building-your-application/testing)
        
        *   [Vitest](https://nextjs.org/docs/pages/building-your-application/testing/vitest)
        *   [Jest](https://nextjs.org/docs/pages/building-your-application/testing/jest)
        *   [Playwright](https://nextjs.org/docs/pages/building-your-application/testing/playwright)
        *   [Cypress](https://nextjs.org/docs/pages/building-your-application/testing/cypress)
        
    *   [Authentication](https://nextjs.org/docs/pages/building-your-application/authentication)
    *   [Deploying](https://nextjs.org/docs/pages/building-your-application/deploying)
        
        *   [Production Checklist](https://nextjs.org/docs/pages/building-your-application/deploying/production-checklist)
        *   [Static Exports](https://nextjs.org/docs/pages/building-your-application/deploying/static-exports)
        *   [Multi-Zones](https://nextjs.org/docs/pages/building-your-application/deploying/multi-zones)
        *   [Continuous Integration (CI) Build Caching](https://nextjs.org/docs/pages/building-your-application/deploying/ci-build-caching)
        
    *   [Upgrading](https://nextjs.org/docs/pages/building-your-application/upgrading)
        
        *   [Codemods](https://nextjs.org/docs/pages/building-your-application/upgrading/codemods)
        *   [From Pages to App](https://nextjs.org/docs/pages/building-your-application/upgrading/app-router-migration)
        *   [Migrating from Vite](https://nextjs.org/docs/pages/building-your-application/upgrading/from-vite)
        *   [Migrating from Create React App](https://nextjs.org/docs/pages/building-your-application/upgrading/from-create-react-app)
        *   [Version 14](https://nextjs.org/docs/pages/building-your-application/upgrading/version-14)
        *   [Version 13](https://nextjs.org/docs/pages/building-your-application/upgrading/version-13)
        *   [Version 12](https://nextjs.org/docs/pages/building-your-application/upgrading/version-12)
        *   [Version 11](https://nextjs.org/docs/pages/building-your-application/upgrading/version-11)
        *   [Version 10](https://nextjs.org/docs/pages/building-your-application/upgrading/version-10)
        *   [Version 9](https://nextjs.org/docs/pages/building-your-application/upgrading/version-9)
        
    

*   [API Reference](https://nextjs.org/docs/pages/api-reference)
    
    *   [Components](https://nextjs.org/docs/pages/api-reference/components)
        
        *   [Font](https://nextjs.org/docs/pages/api-reference/components/font)
        *   [Form](https://nextjs.org/docs/pages/api-reference/components/form)
        *   [Head](https://nextjs.org/docs/pages/api-reference/components/head)
        *   [Image](https://nextjs.org/docs/pages/api-reference/components/image)
        *   [Image (Legacy)](https://nextjs.org/docs/pages/api-reference/components/image-legacy)
        *   [Link](https://nextjs.org/docs/pages/api-reference/components/link)
        *   [Script](https://nextjs.org/docs/pages/api-reference/components/script)
        
    *   [Functions](https://nextjs.org/docs/pages/api-reference/functions)
        
        *   [getInitialProps](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)
        *   [getServerSideProps](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props)
        *   [getStaticPaths](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths)
        *   [getStaticProps](https://nextjs.org/docs/pages/api-reference/functions/get-static-props)
        *   [NextRequest](https://nextjs.org/docs/pages/api-reference/functions/next-request)
        *   [NextResponse](https://nextjs.org/docs/pages/api-reference/functions/next-response)
        *   [useAmp](https://nextjs.org/docs/pages/api-reference/functions/use-amp)
        *   [useReportWebVitals](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals)
        *   [useRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router)
        *   [userAgent](https://nextjs.org/docs/pages/api-reference/functions/userAgent)
        
    *   [Configuration](https://nextjs.org/docs/pages/api-reference/config)
        
        *   [next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)
            
            *   [assetPrefix](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix)
            *   [basePath](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath)
            *   [bundlePagesRouterDependencies](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)
            *   [compress](https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress)
            *   [crossOrigin](https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin)
            *   [devIndicators](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators)
            *   [distDir](https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir)
            *   [env](https://nextjs.org/docs/pages/api-reference/config/next-config-js/env)
            *   [eslint](https://nextjs.org/docs/pages/api-reference/config/next-config-js/eslint)
            *   [exportPathMap](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap)
            *   [generateBuildId](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId)
            *   [generateEtags](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags)
            *   [headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)
            *   [httpAgentOptions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions)
            *   [images](https://nextjs.org/docs/pages/api-reference/config/next-config-js/images)
            *   [onDemandEntries](https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries)
            *   [optimizePackageImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports)
            *   [output](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output)
            *   [pageExtensions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions)
            *   [poweredByHeader](https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader)
            *   [productionBrowserSourceMaps](https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [reactStrictMode](https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode)
            *   [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)
            *   [rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)
            *   [Runtime Config](https://nextjs.org/docs/pages/api-reference/config/next-config-js/runtime-configuration)
            *   [serverExternalPackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages)
            *   [trailingSlash](https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash)
            *   [transpilePackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages)
            *   [turbo](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbo)
            *   [typescript](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript)
            *   [urlImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports)
            *   [useLightningcss](https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss)
            *   [webpack](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack)
            *   [webVitalsAttribution](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)
            
        *   [TypeScript](https://nextjs.org/docs/pages/api-reference/config/typescript)
        *   [ESLint](https://nextjs.org/docs/pages/api-reference/config/eslint)
        
    *   [CLI](https://nextjs.org/docs/pages/api-reference/cli)
        
        *   [CLI](https://nextjs.org/docs/pages/api-reference/cli/create-next-app)
        *   [next CLI](https://nextjs.org/docs/pages/api-reference/cli/next)
        
    *   [Edge Runtime](https://nextjs.org/docs/pages/api-reference/edge)
    *   [Turbopack](https://nextjs.org/docs/pages/api-reference/turbopack)
    

*   [Architecture](https://nextjs.org/docs/architecture)
    
    *   [Accessibility](https://nextjs.org/docs/architecture/accessibility)
    *   [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh)
    *   [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)
    *   [Supported Browsers](https://nextjs.org/docs/architecture/supported-browsers)
    

*   [Community](https://nextjs.org/docs/community)
    
    *   [Contribution Guide](https://nextjs.org/docs/community/contribution-guide)
    

On this page

*   [Production Builds](https://nextjs.org/docs/pages/building-your-application/deploying#production-builds)
*   [Managed Next.js with Vercel](https://nextjs.org/docs/pages/building-your-application/deploying#managed-nextjs-with-vercel)
*   [Self-Hosting](https://nextjs.org/docs/pages/building-your-application/deploying#self-hosting)
*   [Node.js Server](https://nextjs.org/docs/pages/building-your-application/deploying#nodejs-server)
*   [Docker Image](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image)
*   [Static HTML Export](https://nextjs.org/docs/pages/building-your-application/deploying#static-html-export)
*   [Features](https://nextjs.org/docs/pages/building-your-application/deploying#features)
*   [Image Optimization](https://nextjs.org/docs/pages/building-your-application/deploying#image-optimization)
*   [Middleware](https://nextjs.org/docs/pages/building-your-application/deploying#middleware)
*   [Environment Variables](https://nextjs.org/docs/pages/building-your-application/deploying#environment-variables)
*   [Caching and ISR](https://nextjs.org/docs/pages/building-your-application/deploying#caching-and-isr)
*   [Automatic Caching](https://nextjs.org/docs/pages/building-your-application/deploying#automatic-caching)
*   [Static Assets](https://nextjs.org/docs/pages/building-your-application/deploying#static-assets)
*   [Configuring Caching](https://nextjs.org/docs/pages/building-your-application/deploying#configuring-caching)
*   [Build Cache](https://nextjs.org/docs/pages/building-your-application/deploying#build-cache)
*   [Version Skew](https://nextjs.org/docs/pages/building-your-application/deploying#version-skew)
*   [Manual Graceful Shutdowns](https://nextjs.org/docs/pages/building-your-application/deploying#manual-graceful-shutdowns)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/02-pages/02-building-your-application/09-deploying/index.mdx) [Managed Next.js (Vercel)](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=web&utm_campaign=managed_nextjs_solutions_page) Scroll to top

[Pages Router](https://nextjs.org/docs/pages)[Building Your Application](https://nextjs.org/docs/pages/building-your-application)Deploying

Deploying
=========

Congratulations, it's time to ship to production.

You can deploy [managed Next.js with Vercel](https://nextjs.org/docs/pages/building-your-application/deploying#managed-nextjs-with-vercel), or self-host on a Node.js server, Docker image, or even static HTML files. When deploying using `next start`, all Next.js features are supported.

[Production Builds](https://nextjs.org/docs/pages/building-your-application/deploying#production-builds)
--------------------------------------------------------------------------------------------------------

Running `next build` generates an optimized version of your application for production. HTML, CSS, and JavaScript files are created based on your pages. JavaScript is **compiled** and browser bundles are **minified** using the [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler) to help achieve the best performance and support [all modern browsers](https://nextjs.org/docs/architecture/supported-browsers).

Next.js produces a standard deployment output used by managed and self-hosted Next.js. This ensures all features are supported across both methods of deployment. In the next major version, we will be transforming this output into our [Build Output API specification](https://vercel.com/docs/build-output-api/v3?utm_source=next-site&utm_medium=docs&utm_campaign=next-website).

[Managed Next.js with Vercel](https://nextjs.org/docs/pages/building-your-application/deploying#managed-nextjs-with-vercel)
---------------------------------------------------------------------------------------------------------------------------

[Vercel](https://vercel.com/docs/frameworks/nextjs?utm_source=next-site&utm_medium=docs&utm_campaign=next-website), the creators and maintainers of Next.js, provide managed infrastructure and a developer experience platform for your Next.js applications.

Deploying to Vercel is zero-configuration and provides additional enhancements for scalability, availability, and performance globally. However, all Next.js features are still supported when self-hosted.

Learn more about [Next.js on Vercel](https://vercel.com/docs/frameworks/nextjs?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) or [deploy a template for free](https://vercel.com/templates/next.js?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) to try it out.

[Self-Hosting](https://nextjs.org/docs/pages/building-your-application/deploying#self-hosting)
----------------------------------------------------------------------------------------------

You can self-host Next.js in three different ways:

*   [A Node.js server](https://nextjs.org/docs/pages/building-your-application/deploying#nodejs-server)
*   [A Docker container](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image)
*   [A static export](https://nextjs.org/docs/pages/building-your-application/deploying#static-html-export)

> **🎥 Watch:** Learn more about self-hosting Next.js → [YouTube (45 minutes)](https://www.youtube.com/watch?v=sIVL4JMqRfc).

We have community maintained deployment examples with the following providers:

*   [Deno](https://github.com/nextjs/deploy-deno)
*   [DigitalOcean](https://github.com/nextjs/deploy-digitalocean)
*   [Flightcontrol](https://github.com/nextjs/deploy-flightcontrol)
*   [Fly.io](https://github.com/nextjs/deploy-fly)
*   [GitHub Pages](https://github.com/nextjs/deploy-github-pages)
*   [Google Cloud Run](https://github.com/nextjs/deploy-google-cloud-run)
*   [Railway](https://github.com/nextjs/deploy-railway)
*   [Render](https://github.com/nextjs/deploy-render)
*   [SST](https://github.com/nextjs/deploy-sst)

### [Node.js Server](https://nextjs.org/docs/pages/building-your-application/deploying#nodejs-server)

Next.js can be deployed to any hosting provider that supports Node.js. Ensure your `package.json` has the `"build"` and `"start"` scripts:

package.json

```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

Then, run `npm run build` to build your application. Finally, run `npm run start` to start the Node.js server. This server supports all Next.js features.

### [Docker Image](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image)

Next.js can be deployed to any hosting provider that supports [Docker](https://www.docker.com/) containers. You can use this approach when deploying to container orchestrators such as [Kubernetes](https://kubernetes.io/) or when running inside a container in any cloud provider.

1.  [Install Docker](https://docs.docker.com/get-docker/) on your machine
2.  [Clone our example](https://github.com/vercel/next.js/tree/canary/examples/with-docker) (or the [multi-environment example](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env))
3.  Build your container: `docker build -t nextjs-docker .`
4.  Run your container: `docker run -p 3000:3000 nextjs-docker`

Next.js through Docker supports all Next.js features.

### [Static HTML Export](https://nextjs.org/docs/pages/building-your-application/deploying#static-html-export)

Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.

Since Next.js supports this [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports), it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.

Running as a [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports) does not support Next.js features that require a server. [Learn more](https://nextjs.org/docs/app/building-your-application/deploying/static-exports#unsupported-features).

> **Good to know:**
> 
> *   [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components) are supported with static exports.

[Features](https://nextjs.org/docs/pages/building-your-application/deploying#features)
--------------------------------------------------------------------------------------

### [Image Optimization](https://nextjs.org/docs/pages/building-your-application/deploying#image-optimization)

[Image Optimization](https://nextjs.org/docs/app/building-your-application/optimizing/images) through `next/image` works self-hosted with zero configuration when deploying using `next start`. If you would prefer to have a separate service to optimize images, you can [configure an image loader](https://nextjs.org/docs/app/building-your-application/optimizing/images#loaders).

Image Optimization can be used with a [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports#image-optimization) by defining a custom image loader in `next.config.js`. Note that images are optimized at runtime, not during the build.

> **Good to know:**
> 
> *   On glibc-based Linux systems, Image Optimization may require [additional configuration](https://sharp.pixelplumbing.com/install#linux-memory-allocator) to prevent excessive memory usage.
> *   Learn more about the [caching behavior of optimized images](https://nextjs.org/docs/app/api-reference/components/image#caching-behavior) and how to configure the TTL.
> *   You can also [disable Image Optimization](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) and still retain other benefits of using `next/image` if you prefer. For example, if you are optimizing images yourself separately.

### [Middleware](https://nextjs.org/docs/pages/building-your-application/deploying#middleware)

[Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware) works self-hosted with zero configuration when deploying using `next start`. Since it requires access to the incoming request, it is not supported when using a [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports).

Middleware uses a [runtime](https://nextjs.org/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes) that is a subset of all available Node.js APIs to help ensure low latency, since it may run in front of every route or asset in your application. This runtime does not require running “at the edge” and works in a single-region server. Additional configuration and infrastructure are required to run Middleware in multiple regions.

If you are looking to add logic (or use an external package) that requires all Node.js APIs, you might be able to move this logic to a [layout](https://nextjs.org/docs/app/building-your-application/routing/layouts-and-templates#layouts) as a [Server Component](https://nextjs.org/docs/app/building-your-application/rendering/server-components). For example, checking [headers](https://nextjs.org/docs/app/api-reference/functions/headers) and [redirecting](https://nextjs.org/docs/app/api-reference/functions/redirect). You can also use headers, cookies, or query parameters to [redirect](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching) or [rewrite](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching) through `next.config.js`. If that does not work, you can also use a [custom server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server).

### [Environment Variables](https://nextjs.org/docs/pages/building-your-application/deploying#environment-variables)

Next.js can support both build time and runtime environment variables.

**By default, environment variables are only available on the server**. To expose an environment variable to the browser, it must be prefixed with `NEXT_PUBLIC_`. However, these public environment variables will be inlined into the JavaScript bundle during `next build`.

To read runtime environment variables, we recommend using `getServerSideProps` or [incrementally adopting the App Router](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration).

This allows you to use a singular Docker image that can be promoted through multiple environments with different values.

> **Good to know:**
> 
> *   You can run code on server startup using the [`register` function](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation).
> *   We do not recommend using the [runtimeConfig](https://nextjs.org/docs/pages/api-reference/config/next-config-js/runtime-configuration) option, as this does not work with the standalone output mode. Instead, we recommend [incrementally adopting](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration) the App Router.

### [Caching and ISR](https://nextjs.org/docs/pages/building-your-application/deploying#caching-and-isr)

Next.js can cache responses, generated static pages, build outputs, and other static assets like images, fonts, and scripts.

Caching and revalidating pages (with [Incremental Static Regeneration](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration)) use the **same shared cache**. By default, this cache is stored to the filesystem (on disk) on your Next.js server. **This works automatically when self-hosting** using both the Pages and App Router.

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.

#### [Automatic Caching](https://nextjs.org/docs/pages/building-your-application/deploying#automatic-caching)

*   Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` to truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](https://nextjs.org/docs/app/building-your-application/optimizing/images#local-images). You can [configure the TTL](https://nextjs.org/docs/app/api-reference/components/image#caching-behavior) for images.
*   Incremental Static Regeneration (ISR) sets the `Cache-Control` header of `s-maxage: <revalidate in getStaticProps>, stale-while-revalidate`. This revalidation time is defined in your [`getStaticProps` function](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) in seconds. If you set `revalidate: false`, it will default to a one-year cache duration.
*   Dynamically rendered pages set a `Cache-Control` header of `private, no-cache, no-store, max-age=0, must-revalidate` to prevent user-specific data from being cached. This applies to both the App Router and Pages Router. This also includes [Draft Mode](https://nextjs.org/docs/app/building-your-application/configuring/draft-mode).

#### [Static Assets](https://nextjs.org/docs/pages/building-your-application/deploying#static-assets)

If you want to host static assets on a different domain or CDN, you can use the `assetPrefix` [configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix) in `next.config.js`. Next.js will use this asset prefix when retrieving JavaScript or CSS files. Separating your assets to a different domain does come with the downside of extra time spent on DNS and TLS resolution.

[Learn more about `assetPrefix`](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix).

#### [Configuring Caching](https://nextjs.org/docs/pages/building-your-application/deploying#configuring-caching)

By default, generated cache assets will be stored in memory (defaults to 50mb) and on disk. If you are hosting Next.js using a container orchestration platform like Kubernetes, each pod will have a copy of the cache. To prevent stale data from being shown since the cache is not shared between pods by default, you can configure the Next.js cache to provide a cache handler and disable in-memory caching.

To configure the ISR/Data Cache location when self-hosting, you can configure a custom handler in your `next.config.js` file:

next.config.js

```
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

Then, create `cache-handler.js` in the root of your project, for example:

cache-handler.js

```
const cache = new Map()
 
module.exports = class CacheHandler {
  constructor(options) {
    this.options = options
  }
 
  async get(key) {
    // This could be stored anywhere, like durable storage
    return cache.get(key)
  }
 
  async set(key, data, ctx) {
    // This could be stored anywhere, like durable storage
    cache.set(key, {
      value: data,
      lastModified: Date.now(),
      tags: ctx.tags,
    })
  }
 
  async revalidateTag(tags) {
    // tags is either a string or an array of strings
    tags = [tags].flat()
    // Iterate over all entries in the cache
    for (let [key, value] of cache) {
      // If the value's tags include the specified tag, delete this entry
      if (value.tags.some((tag) => tags.includes(tag))) {
        cache.delete(key)
      }
    }
  }
 
  // If you want to have temporary in memory cache for a single request that is reset
  // before the next request you can leverage this method
  resetRequestCache() {}
}
```

Using a custom cache handler will allow you to ensure consistency across all pods hosting your Next.js application. For instance, you can save the cached values anywhere, like [Redis](https://github.com/vercel/next.js/tree/canary/examples/cache-handler-redis) or AWS S3.

> **Good to know:**
> 
> *   `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call the `revalidateTag` function with a special default tag for the provided page.

### [Build Cache](https://nextjs.org/docs/pages/building-your-application/deploying#build-cache)

Next.js generates an ID during `next build` to identify which version of your application is being served. The same build should be used and boot up multiple containers.

If you are rebuilding for each stage of your environment, you will need to generate a consistent build ID to use between containers. Use the `generateBuildId` command in `next.config.js`:

next.config.js

```
module.exports = {
  generateBuildId: async () => {
    // This could be anything, using the latest git hash
    return process.env.GIT_HASH
  },
}
```

### [Version Skew](https://nextjs.org/docs/pages/building-your-application/deploying#version-skew)

Next.js will automatically mitigate most instances of [version skew](https://www.industrialempathy.com/posts/version-skew/) and automatically reload the application to retrieve new assets when detected. For example, if there is a mismatch in the `deploymentId`, transitions between pages will perform a hard navigation versus using a prefetched value.

When the application is reloaded, there may be a loss of application state if it's not designed to persist between page navigations. For example, using URL state or local storage would persist state after a page refresh. However, component state like `useState` would be lost in such navigations.

Vercel provides additional [skew protection](https://vercel.com/docs/deployments/skew-protection?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) for Next.js applications to ensure assets and functions from the previous version are still available to older clients, even after the new version is deployed.

You can manually configure the `deploymentId` property in your `next.config.js` file to ensure each request uses either `?dpl` query string or `x-deployment-id` header.

[Manual Graceful Shutdowns](https://nextjs.org/docs/pages/building-your-application/deploying#manual-graceful-shutdowns)
------------------------------------------------------------------------------------------------------------------------

When self-hosting, you might want to run code when the server shuts down on `SIGTERM` or `SIGINT` signals.

You can set the env variable `NEXT_MANUAL_SIG_HANDLE` to `true` and then register a handler for that signal inside your `_document.js` file. You will need to register the environment variable directly in the `package.json` script, and not in the `.env` file.

> **Good to know**: Manual signal handling is not available in `next dev`.

package.json

```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "NEXT_MANUAL_SIG_HANDLE=true next start"
  }
}
```

pages/\_document.js

```
if (process.env.NEXT_MANUAL_SIG_HANDLE) {
  process.on('SIGTERM', () => {
    console.log('Received SIGTERM: cleaning up')
    process.exit(0)
  })
  process.on('SIGINT', () => {
    console.log('Received SIGINT: cleaning up')
    process.exit(0)
  })
}
```

[### Production Checklist Recommendations to ensure the best performance and user experience before taking your Next.js application to production.](https://nextjs.org/docs/pages/building-your-application/deploying/production-checklist)[### Static Exports Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.](https://nextjs.org/docs/pages/building-your-application/deploying/static-exports)[### Multi-Zones Learn how to build micro-frontends using Next.js Multi-Zones to deploy multiple Next.js apps under a single domain.](https://nextjs.org/docs/pages/building-your-application/deploying/multi-zones)[### Continuous Integration (CI) Build Caching Learn how to configure CI to cache Next.js builds](https://nextjs.org/docs/pages/building-your-application/deploying/ci-build-caching)

[Previous Authentication](https://nextjs.org/docs/pages/building-your-application/authentication)

[Next Production Checklist](https://nextjs.org/docs/pages/building-your-application/deploying/production-checklist)

Was this helpful?

supported.

Send

[](https://vercel.com/home?utm_source=next-site&utm_medium=footer&utm_campaign=next-website "Go to the Vercel website")

[![Image 11: GitHub Logo](https://nextjs.org/icons/github.svg)](https://github.com/vercel/next.js)

* * *

[![Image 12: X Logo](https://nextjs.org/icons/x.svg)](https://twitter.com/nextjs)

* * *

[![Image 13: Bluesky Logo](https://nextjs.org/icons/bluesky.svg)](https://bsky.app/profile/nextjs.org)

#### Resources

[Docs](https://nextjs.org/docs)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Analytics](https://vercel.com/analytics?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[Next.js Conf](https://nextjs.org/conf)[Previews](https://vercel.com/products/previews?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)

#### More

[Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[Contact Sales](https://vercel.com/contact/sales?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[GitHub](https://github.com/vercel/next.js)[Releases](https://github.com/vercel/next.js/releases)[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)

#### About Vercel

[Next.js + Vercel](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[Open Source Software](https://vercel.com/oss?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[GitHub](https://github.com/vercel)[Bluesky](https://bsky.app/profile/vercel.com)[X](https://twitter.com/vercel)

#### Legal

[Privacy Policy](https://vercel.com/legal/privacy-policy)Cookie Preferences

#### Subscribe to our newsletter

Stay updated on new releases and features, guides, and case studies.

Subscribe

© 2025 Vercel, Inc.

[![Image 14: GitHub Logo](https://nextjs.org/icons/github.svg)](https://github.com/vercel/next.js)

* * *

[![Image 15: X Logo](https://nextjs.org/icons/x.svg)](https://x.com/nextjs)

* * *

[![Image 16: Bluesky Logo](https://nextjs.org/icons/bluesky.svg)](https://bsky.app/profile/nextjs.org)

## Metadata

```json
{
  "title": "Building Your Application: Deploying | Next.js",
  "description": "Learn how to deploy your Next.js app to production, either managed or self-hosted.",
  "url": "https://nextjs.org/docs/pages/building-your-application/deploying",
  "content": "Building Your Application: Deploying | Next.js\n===============\n\n[Skip to content](https://nextjs.org/docs/pages/building-your-application/deploying#geist-skip-nav)\n\n[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_pages_building-your-application_deploying \"Go to Vercel homepage\")\n\n[![Image 9: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true \"Go to the homepage\")\n\n[](https://nextjs.org/ \"Go to the homepage\")\n\nSearch documentation...Search...⌘K\n\n[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_pages_building-your-application_deploying \"Go to Vercel homepage\")\n\n[![Image 10: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true \"Go to the homepage\")\n\n[](https://nextjs.org/ \"Go to the homepage\")\n\n[Showcase](https://nextjs.org/showcase)[Docs](https://nextjs.org/docs \"Documentation\")[Blog](https://nextjs.org/blog)[Templates](https://vercel.com/templates/next.js?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_templates)[Enterprise](https://vercel.com/contact/sales/nextjs?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_enterprise)\n\nSearch documentation...Search...⌘KFeedback[Learn](https://nextjs.org/learn)\n\nMenu\n\nUsing App Router\n\nFeatures available in /app\n\nUsing Latest Version\n\n15.1.5\n\n*   [Getting Started](https://nextjs.org/docs/app/getting-started)\n    \n    *   [Installation](https://nextjs.org/docs/app/getting-started/installation)\n    *   [Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)\n    *   [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)\n    *   [Images and Fonts](https://nextjs.org/docs/app/getting-started/images-and-fonts)\n    *   [CSS and Styling](https://nextjs.org/docs/app/getting-started/css-and-styling)\n    *   [Fetching data and streaming](https://nextjs.org/docs/app/getting-started/data-fetching-and-streaming)\n    *   [Mutating Data](https://nextjs.org/docs/app/getting-started/mutating-data)\n    *   [Error handling](https://nextjs.org/docs/app/getting-started/error-handling)\n    \n\n*   [Examples](https://nextjs.org/docs/app/examples)\n\n*   [Building Your Application](https://nextjs.org/docs/app/building-your-application)\n    \n    *   [Routing](https://nextjs.org/docs/app/building-your-application/routing)\n        \n        *   [Layouts and Templates](https://nextjs.org/docs/app/building-your-application/routing/layouts-and-templates)\n        *   [Linking and Navigating](https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating)\n        *   [Error Handling](https://nextjs.org/docs/app/building-your-application/routing/error-handling)\n        *   [Loading UI and Streaming](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming)\n        *   [Redirecting](https://nextjs.org/docs/app/building-your-application/routing/redirecting)\n        *   [Route Groups](https://nextjs.org/docs/app/building-your-application/routing/route-groups)\n        *   [Dynamic Routes](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes)\n        *   [Parallel Routes](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes)\n        *   [Intercepting Routes](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes)\n        *   [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)\n        *   [Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware)\n        *   [Internationalization](https://nextjs.org/docs/app/building-your-application/routing/internationalization)\n        \n    *   [Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching)\n        \n        *   [Data Fetching and Caching](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching)\n        *   [Server Actions and Mutations](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)\n        *   [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration)\n        \n    *   [Rendering](https://nextjs.org/docs/app/building-your-application/rendering)\n        \n        *   [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)\n        *   [Client Components](https://nextjs.org/docs/app/building-your-application/rendering/client-components)\n        *   [Composition Patterns](https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns)\n        *   [Partial Prerendering](https://nextjs.org/docs/app/building-your-application/rendering/partial-prerendering)\n        *   [Runtimes](https://nextjs.org/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes)\n        \n    *   [Caching](https://nextjs.org/docs/app/building-your-application/caching)\n    *   [Styling](https://nextjs.org/docs/app/building-your-application/styling)\n        \n        *   [CSS](https://nextjs.org/docs/app/building-your-application/styling/css)\n        *   [Tailwind CSS](https://nextjs.org/docs/app/building-your-application/styling/tailwind-css)\n        *   [Sass](https://nextjs.org/docs/app/building-your-application/styling/sass)\n        *   [CSS-in-JS](https://nextjs.org/docs/app/building-your-application/styling/css-in-js)\n        \n    *   [Optimizing](https://nextjs.org/docs/app/building-your-application/optimizing)\n        \n        *   [Images](https://nextjs.org/docs/app/building-your-application/optimizing/images)\n        *   [Videos](https://nextjs.org/docs/app/building-your-application/optimizing/videos)\n        *   [Fonts](https://nextjs.org/docs/app/building-your-application/optimizing/fonts)\n        *   [Metadata](https://nextjs.org/docs/app/building-your-application/optimizing/metadata)\n        *   [Scripts](https://nextjs.org/docs/app/building-your-application/optimizing/scripts)\n        *   [Package Bundling](https://nextjs.org/docs/app/building-your-application/optimizing/package-bundling)\n        *   [Lazy Loading](https://nextjs.org/docs/app/building-your-application/optimizing/lazy-loading)\n        *   [Analytics](https://nextjs.org/docs/app/building-your-application/optimizing/analytics)\n        *   [Instrumentation](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation)\n        *   [OpenTelemetry](https://nextjs.org/docs/app/building-your-application/optimizing/open-telemetry)\n        *   [Static Assets](https://nextjs.org/docs/app/building-your-application/optimizing/static-assets)\n        *   [Third Party Libraries](https://nextjs.org/docs/app/building-your-application/optimizing/third-party-libraries)\n        *   [Memory Usage](https://nextjs.org/docs/app/building-your-application/optimizing/memory-usage)\n        \n    *   [Configuring](https://nextjs.org/docs/app/building-your-application/configuring)\n        \n        *   [Environment Variables](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)\n        *   [MDX](https://nextjs.org/docs/app/building-your-application/configuring/mdx)\n        *   [src Directory](https://nextjs.org/docs/app/building-your-application/configuring/src-directory)\n        *   [Custom Server](https://nextjs.org/docs/app/building-your-application/configuring/custom-server)\n        *   [Draft Mode](https://nextjs.org/docs/app/building-your-application/configuring/draft-mode)\n        *   [Content Security Policy](https://nextjs.org/docs/app/building-your-application/configuring/content-security-policy)\n        *   [Debugging](https://nextjs.org/docs/app/building-your-application/configuring/debugging)\n        *   [Progressive Web Applications (PWA)](https://nextjs.org/docs/app/building-your-application/configuring/progressive-web-apps)\n        \n    *   [Testing](https://nextjs.org/docs/app/building-your-application/testing)\n        \n        *   [Vitest](https://nextjs.org/docs/app/building-your-application/testing/vitest)\n        *   [Jest](https://nextjs.org/docs/app/building-your-application/testing/jest)\n        *   [Playwright](https://nextjs.org/docs/app/building-your-application/testing/playwright)\n        *   [Cypress](https://nextjs.org/docs/app/building-your-application/testing/cypress)\n        \n    *   [Authentication](https://nextjs.org/docs/app/building-your-application/authentication)\n    *   [Deploying](https://nextjs.org/docs/app/building-your-application/deploying)\n        \n        *   [Production Checklist](https://nextjs.org/docs/app/building-your-application/deploying/production-checklist)\n        *   [Static Exports](https://nextjs.org/docs/app/building-your-application/deploying/static-exports)\n        *   [Multi-Zones](https://nextjs.org/docs/app/building-your-application/deploying/multi-zones)\n        \n    *   [Upgrading](https://nextjs.org/docs/app/building-your-application/upgrading)\n        \n        *   [Codemods](https://nextjs.org/docs/app/building-your-application/upgrading/codemods)\n        *   [Canary](https://nextjs.org/docs/app/building-your-application/upgrading/canary)\n        *   [Version 15](https://nextjs.org/docs/app/building-your-application/upgrading/version-15)\n        *   [Version 14](https://nextjs.org/docs/app/building-your-application/upgrading/version-14)\n        *   [App Router Migration](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration)\n        *   [Migrating from CRA](https://nextjs.org/docs/app/building-your-application/upgrading/from-create-react-app)\n        *   [Migrating from Vite](https://nextjs.org/docs/app/building-your-application/upgrading/from-vite)\n        *   [Single-Page Apps](https://nextjs.org/docs/app/building-your-application/upgrading/single-page-applications)\n        \n    \n\n*   [API Reference](https://nextjs.org/docs/app/api-reference)\n    \n    *   [Directives](https://nextjs.org/docs/app/api-reference/directives)\n        \n        *   [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)\n        *   [use client](https://nextjs.org/docs/app/api-reference/directives/use-client)\n        *   [use server](https://nextjs.org/docs/app/api-reference/directives/use-server)\n        \n    *   [Components](https://nextjs.org/docs/app/api-reference/components)\n        \n        *   [Font](https://nextjs.org/docs/app/api-reference/components/font)\n        *   [Form](https://nextjs.org/docs/app/api-reference/components/form)\n        *   [Image](https://nextjs.org/docs/app/api-reference/components/image)\n        *   [Link](https://nextjs.org/docs/app/api-reference/components/link)\n        *   [Script](https://nextjs.org/docs/app/api-reference/components/script)\n        \n    *   [File Conventions](https://nextjs.org/docs/app/api-reference/file-conventions)\n        \n        *   [default.js](https://nextjs.org/docs/app/api-reference/file-conventions/default)\n        *   [error.js](https://nextjs.org/docs/app/api-reference/file-conventions/error)\n        *   [forbidden.js](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)\n        *   [instrumentation.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)\n        *   [layout.js](https://nextjs.org/docs/app/api-reference/file-conventions/layout)\n        *   [loading.js](https://nextjs.org/docs/app/api-reference/file-conventions/loading)\n        *   [mdx-components.js](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components)\n        *   [middleware.js](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)\n        *   [not-found.js](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)\n        *   [page.js](https://nextjs.org/docs/app/api-reference/file-conventions/page)\n        *   [route.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)\n        *   [Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)\n        *   [template.js](https://nextjs.org/docs/app/api-reference/file-conventions/template)\n        *   [unauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)\n        *   [Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)\n            \n            *   [favicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)\n            *   [manifest.json](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)\n            *   [opengraph-image and twitter-image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)\n            *   [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)\n            *   [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)\n            \n        \n    *   [Functions](https://nextjs.org/docs/app/api-reference/functions)\n        \n        *   [after](https://nextjs.org/docs/app/api-reference/functions/after)\n        *   [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)\n        *   [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)\n        *   [connection](https://nextjs.org/docs/app/api-reference/functions/connection)\n        *   [cookies](https://nextjs.org/docs/app/api-reference/functions/cookies)\n        *   [draftMode](https://nextjs.org/docs/app/api-reference/functions/draft-mode)\n        *   [fetch](https://nextjs.org/docs/app/api-reference/functions/fetch)\n        *   [forbidden](https://nextjs.org/docs/app/api-reference/functions/forbidden)\n        *   [generateImageMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)\n        *   [generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)\n        *   [generateSitemaps](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)\n        *   [generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)\n        *   [generateViewport](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)\n        *   [headers](https://nextjs.org/docs/app/api-reference/functions/headers)\n        *   [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response)\n        *   [NextRequest](https://nextjs.org/docs/app/api-reference/functions/next-request)\n        *   [NextResponse](https://nextjs.org/docs/app/api-reference/functions/next-response)\n        *   [notFound](https://nextjs.org/docs/app/api-reference/functions/not-found)\n        *   [permanentRedirect](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)\n        *   [redirect](https://nextjs.org/docs/app/api-reference/functions/redirect)\n        *   [revalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)\n        *   [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)\n        *   [unauthorized](https://nextjs.org/docs/app/api-reference/functions/unauthorized)\n        *   [unstable\\_cache](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)\n        *   [unstable\\_expirePath](https://nextjs.org/docs/app/api-reference/functions/unstable_expirePath)\n        *   [unstable\\_expireTag](https://nextjs.org/docs/app/api-reference/functions/unstable_expireTag)\n        *   [unstable\\_noStore](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)\n        *   [unstable\\_rethrow](https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow)\n        *   [useParams](https://nextjs.org/docs/app/api-reference/functions/use-params)\n        *   [usePathname](https://nextjs.org/docs/app/api-reference/functions/use-pathname)\n        *   [useReportWebVitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)\n        *   [useRouter](https://nextjs.org/docs/app/api-reference/functions/use-router)\n        *   [useSearchParams](https://nextjs.org/docs/app/api-reference/functions/use-search-params)\n        *   [useSelectedLayoutSegment](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment)\n        *   [useSelectedLayoutSegments](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)\n        *   [userAgent](https://nextjs.org/docs/app/api-reference/functions/userAgent)\n        \n    *   [Configuration](https://nextjs.org/docs/app/api-reference/config)\n        \n        *   [next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)\n            \n            *   [appDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir)\n            *   [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)\n            *   [authInterrupts](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)\n            *   [basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)\n            *   [cacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)\n            *   [compress](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress)\n            *   [crossOrigin](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin)\n            *   [cssChunking](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking)\n            *   [devIndicators](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators)\n            *   [distDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir)\n            *   [dynamicIO](https://nextjs.org/docs/app/api-reference/config/next-config-js/dynamicIO)\n            *   [env](https://nextjs.org/docs/app/api-reference/config/next-config-js/env)\n            *   [eslint](https://nextjs.org/docs/app/api-reference/config/next-config-js/eslint)\n            *   [expireTime](https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime)\n            *   [exportPathMap](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap)\n            *   [generateBuildId](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)\n            *   [generateEtags](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags)\n            *   [headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)\n            *   [httpAgentOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions)\n            *   [images](https://nextjs.org/docs/app/api-reference/config/next-config-js/images)\n            *   [cacheHandler](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)\n            *   [inlineCss](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss)\n            *   [logging](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)\n            *   [mdxRs](https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs)\n            *   [onDemandEntries](https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries)\n            *   [optimizePackageImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)\n            *   [output](https://nextjs.org/docs/app/api-reference/config/next-config-js/output)\n            *   [pageExtensions](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)\n            *   [poweredByHeader](https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader)\n            *   [ppr](https://nextjs.org/docs/app/api-reference/config/next-config-js/ppr)\n            *   [productionBrowserSourceMaps](https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)\n            *   [reactCompiler](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler)\n            *   [reactMaxHeadersLength](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)\n            *   [reactStrictMode](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode)\n            *   [redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)\n            *   [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)\n            *   [sassOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions)\n            *   [serverActions](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)\n            *   [serverComponentsHmrCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)\n            *   [serverExternalPackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages)\n            *   [staleTimes](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)\n            *   [staticGeneration\\*](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration)\n            *   [trailingSlash](https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash)\n            *   [transpilePackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages)\n            *   [turbo](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbo)\n            *   [typedRoutes](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes)\n            *   [typescript](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript)\n            *   [urlImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports)\n            *   [useLightningcss](https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss)\n            *   [webpack](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)\n            *   [webVitalsAttribution](https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution)\n            \n        *   [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript)\n        *   [ESLint](https://nextjs.org/docs/app/api-reference/config/eslint)\n        \n    *   [CLI](https://nextjs.org/docs/app/api-reference/cli)\n        \n        *   [create-next-app](https://nextjs.org/docs/app/api-reference/cli/create-next-app)\n        *   [next CLI](https://nextjs.org/docs/app/api-reference/cli/next)\n        \n    *   [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)\n    *   [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)\n    \n\n*   [Getting Started](https://nextjs.org/docs/pages/getting-started)\n    \n    *   [Installation](https://nextjs.org/docs/pages/getting-started/installation)\n    *   [Project Structure](https://nextjs.org/docs/pages/getting-started/project-structure)\n    \n\n*   [Building Your Application](https://nextjs.org/docs/pages/building-your-application)\n    \n    *   [Routing](https://nextjs.org/docs/pages/building-your-application/routing)\n        \n        *   [Pages and Layouts](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)\n        *   [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)\n        *   [Linking and Navigating](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating)\n        *   [Redirecting](https://nextjs.org/docs/pages/building-your-application/routing/redirecting)\n        *   [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)\n        *   [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)\n        *   [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)\n        *   [Custom Errors](https://nextjs.org/docs/pages/building-your-application/routing/custom-error)\n        *   [Internationalization](https://nextjs.org/docs/pages/building-your-application/routing/internationalization)\n        *   [Middleware](https://nextjs.org/docs/pages/building-your-application/routing/middleware)\n        \n    *   [Rendering](https://nextjs.org/docs/pages/building-your-application/rendering)\n        \n        *   [Server-side Rendering (SSR)](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)\n        *   [Static Site Generation (SSG)](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)\n        *   [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)\n        *   [Client-side Rendering (CSR)](https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering)\n        *   [Edge and Node.js Runtimes](https://nextjs.org/docs/pages/building-your-application/rendering/edge-and-nodejs-runtimes)\n        \n    *   [Data Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching)\n        \n        *   [getStaticProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)\n        *   [getStaticPaths](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)\n        *   [Forms and Mutations](https://nextjs.org/docs/pages/building-your-application/data-fetching/forms-and-mutations)\n        *   [getServerSideProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)\n        *   [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration)\n        *   [Client-side Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)\n        \n    *   [Styling](https://nextjs.org/docs/pages/building-your-application/styling)\n        \n        *   [CSS](https://nextjs.org/docs/pages/building-your-application/styling/css)\n        *   [Tailwind CSS](https://nextjs.org/docs/pages/building-your-application/styling/tailwind-css)\n        *   [CSS-in-JS](https://nextjs.org/docs/pages/building-your-application/styling/css-in-js)\n        *   [Sass](https://nextjs.org/docs/pages/building-your-application/styling/sass)\n        \n    *   [Optimizing](https://nextjs.org/docs/pages/building-your-application/optimizing)\n        \n        *   [Images](https://nextjs.org/docs/pages/building-your-application/optimizing/images)\n        *   [Fonts](https://nextjs.org/docs/pages/building-your-application/optimizing/fonts)\n        *   [Scripts](https://nextjs.org/docs/pages/building-your-application/optimizing/scripts)\n        *   [Static Assets](https://nextjs.org/docs/pages/building-your-application/optimizing/static-assets)\n        *   [Bundling](https://nextjs.org/docs/pages/building-your-application/optimizing/package-bundling)\n        *   [Analytics](https://nextjs.org/docs/pages/building-your-application/optimizing/analytics)\n        *   [Lazy Loading](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading)\n        *   [Instrumentation](https://nextjs.org/docs/pages/building-your-application/optimizing/instrumentation)\n        *   [OpenTelemetry](https://nextjs.org/docs/pages/building-your-application/optimizing/open-telemetry)\n        *   [Third Party Libraries](https://nextjs.org/docs/pages/building-your-application/optimizing/third-party-libraries)\n        \n    *   [Configuring](https://nextjs.org/docs/pages/building-your-application/configuring)\n        \n        *   [Environment Variables](https://nextjs.org/docs/pages/building-your-application/configuring/environment-variables)\n        *   [src Directory](https://nextjs.org/docs/pages/building-your-application/configuring/src-directory)\n        *   [MDX](https://nextjs.org/docs/pages/building-your-application/configuring/mdx)\n        *   [AMP](https://nextjs.org/docs/pages/building-your-application/configuring/amp)\n        *   [Babel](https://nextjs.org/docs/pages/building-your-application/configuring/babel)\n        *   [PostCSS](https://nextjs.org/docs/pages/building-your-application/configuring/post-css)\n        *   [Custom Server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server)\n        *   [Draft Mode](https://nextjs.org/docs/pages/building-your-application/configuring/draft-mode)\n        *   [Error Handling](https://nextjs.org/docs/pages/building-your-application/configuring/error-handling)\n        *   [Preview Mode](https://nextjs.org/docs/pages/building-your-application/configuring/preview-mode)\n        *   [Content Security Policy](https://nextjs.org/docs/pages/building-your-application/configuring/content-security-policy)\n        *   [Debugging](https://nextjs.org/docs/pages/building-your-application/configuring/debugging)\n        \n    *   [Testing](https://nextjs.org/docs/pages/building-your-application/testing)\n        \n        *   [Vitest](https://nextjs.org/docs/pages/building-your-application/testing/vitest)\n        *   [Jest](https://nextjs.org/docs/pages/building-your-application/testing/jest)\n        *   [Playwright](https://nextjs.org/docs/pages/building-your-application/testing/playwright)\n        *   [Cypress](https://nextjs.org/docs/pages/building-your-application/testing/cypress)\n        \n    *   [Authentication](https://nextjs.org/docs/pages/building-your-application/authentication)\n    *   [Deploying](https://nextjs.org/docs/pages/building-your-application/deploying)\n        \n        *   [Production Checklist](https://nextjs.org/docs/pages/building-your-application/deploying/production-checklist)\n        *   [Static Exports](https://nextjs.org/docs/pages/building-your-application/deploying/static-exports)\n        *   [Multi-Zones](https://nextjs.org/docs/pages/building-your-application/deploying/multi-zones)\n        *   [Continuous Integration (CI) Build Caching](https://nextjs.org/docs/pages/building-your-application/deploying/ci-build-caching)\n        \n    *   [Upgrading](https://nextjs.org/docs/pages/building-your-application/upgrading)\n        \n        *   [Codemods](https://nextjs.org/docs/pages/building-your-application/upgrading/codemods)\n        *   [From Pages to App](https://nextjs.org/docs/pages/building-your-application/upgrading/app-router-migration)\n        *   [Migrating from Vite](https://nextjs.org/docs/pages/building-your-application/upgrading/from-vite)\n        *   [Migrating from Create React App](https://nextjs.org/docs/pages/building-your-application/upgrading/from-create-react-app)\n        *   [Version 14](https://nextjs.org/docs/pages/building-your-application/upgrading/version-14)\n        *   [Version 13](https://nextjs.org/docs/pages/building-your-application/upgrading/version-13)\n        *   [Version 12](https://nextjs.org/docs/pages/building-your-application/upgrading/version-12)\n        *   [Version 11](https://nextjs.org/docs/pages/building-your-application/upgrading/version-11)\n        *   [Version 10](https://nextjs.org/docs/pages/building-your-application/upgrading/version-10)\n        *   [Version 9](https://nextjs.org/docs/pages/building-your-application/upgrading/version-9)\n        \n    \n\n*   [API Reference](https://nextjs.org/docs/pages/api-reference)\n    \n    *   [Components](https://nextjs.org/docs/pages/api-reference/components)\n        \n        *   [Font](https://nextjs.org/docs/pages/api-reference/components/font)\n        *   [Form](https://nextjs.org/docs/pages/api-reference/components/form)\n        *   [Head](https://nextjs.org/docs/pages/api-reference/components/head)\n        *   [Image](https://nextjs.org/docs/pages/api-reference/components/image)\n        *   [Image (Legacy)](https://nextjs.org/docs/pages/api-reference/components/image-legacy)\n        *   [Link](https://nextjs.org/docs/pages/api-reference/components/link)\n        *   [Script](https://nextjs.org/docs/pages/api-reference/components/script)\n        \n    *   [Functions](https://nextjs.org/docs/pages/api-reference/functions)\n        \n        *   [getInitialProps](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)\n        *   [getServerSideProps](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props)\n        *   [getStaticPaths](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths)\n        *   [getStaticProps](https://nextjs.org/docs/pages/api-reference/functions/get-static-props)\n        *   [NextRequest](https://nextjs.org/docs/pages/api-reference/functions/next-request)\n        *   [NextResponse](https://nextjs.org/docs/pages/api-reference/functions/next-response)\n        *   [useAmp](https://nextjs.org/docs/pages/api-reference/functions/use-amp)\n        *   [useReportWebVitals](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals)\n        *   [useRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router)\n        *   [userAgent](https://nextjs.org/docs/pages/api-reference/functions/userAgent)\n        \n    *   [Configuration](https://nextjs.org/docs/pages/api-reference/config)\n        \n        *   [next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)\n            \n            *   [assetPrefix](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix)\n            *   [basePath](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath)\n            *   [bundlePagesRouterDependencies](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)\n            *   [compress](https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress)\n            *   [crossOrigin](https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin)\n            *   [devIndicators](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators)\n            *   [distDir](https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir)\n            *   [env](https://nextjs.org/docs/pages/api-reference/config/next-config-js/env)\n            *   [eslint](https://nextjs.org/docs/pages/api-reference/config/next-config-js/eslint)\n            *   [exportPathMap](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap)\n            *   [generateBuildId](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId)\n            *   [generateEtags](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags)\n            *   [headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)\n            *   [httpAgentOptions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions)\n            *   [images](https://nextjs.org/docs/pages/api-reference/config/next-config-js/images)\n            *   [onDemandEntries](https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries)\n            *   [optimizePackageImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports)\n            *   [output](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output)\n            *   [pageExtensions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions)\n            *   [poweredByHeader](https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader)\n            *   [productionBrowserSourceMaps](https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)\n            *   [reactStrictMode](https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode)\n            *   [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)\n            *   [rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)\n            *   [Runtime Config](https://nextjs.org/docs/pages/api-reference/config/next-config-js/runtime-configuration)\n            *   [serverExternalPackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages)\n            *   [trailingSlash](https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash)\n            *   [transpilePackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages)\n            *   [turbo](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbo)\n            *   [typescript](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript)\n            *   [urlImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports)\n            *   [useLightningcss](https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss)\n            *   [webpack](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack)\n            *   [webVitalsAttribution](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)\n            \n        *   [TypeScript](https://nextjs.org/docs/pages/api-reference/config/typescript)\n        *   [ESLint](https://nextjs.org/docs/pages/api-reference/config/eslint)\n        \n    *   [CLI](https://nextjs.org/docs/pages/api-reference/cli)\n        \n        *   [CLI](https://nextjs.org/docs/pages/api-reference/cli/create-next-app)\n        *   [next CLI](https://nextjs.org/docs/pages/api-reference/cli/next)\n        \n    *   [Edge Runtime](https://nextjs.org/docs/pages/api-reference/edge)\n    *   [Turbopack](https://nextjs.org/docs/pages/api-reference/turbopack)\n    \n\n*   [Architecture](https://nextjs.org/docs/architecture)\n    \n    *   [Accessibility](https://nextjs.org/docs/architecture/accessibility)\n    *   [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh)\n    *   [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)\n    *   [Supported Browsers](https://nextjs.org/docs/architecture/supported-browsers)\n    \n\n*   [Community](https://nextjs.org/docs/community)\n    \n    *   [Contribution Guide](https://nextjs.org/docs/community/contribution-guide)\n    \n\nOn this page\n\n*   [Production Builds](https://nextjs.org/docs/pages/building-your-application/deploying#production-builds)\n*   [Managed Next.js with Vercel](https://nextjs.org/docs/pages/building-your-application/deploying#managed-nextjs-with-vercel)\n*   [Self-Hosting](https://nextjs.org/docs/pages/building-your-application/deploying#self-hosting)\n*   [Node.js Server](https://nextjs.org/docs/pages/building-your-application/deploying#nodejs-server)\n*   [Docker Image](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image)\n*   [Static HTML Export](https://nextjs.org/docs/pages/building-your-application/deploying#static-html-export)\n*   [Features](https://nextjs.org/docs/pages/building-your-application/deploying#features)\n*   [Image Optimization](https://nextjs.org/docs/pages/building-your-application/deploying#image-optimization)\n*   [Middleware](https://nextjs.org/docs/pages/building-your-application/deploying#middleware)\n*   [Environment Variables](https://nextjs.org/docs/pages/building-your-application/deploying#environment-variables)\n*   [Caching and ISR](https://nextjs.org/docs/pages/building-your-application/deploying#caching-and-isr)\n*   [Automatic Caching](https://nextjs.org/docs/pages/building-your-application/deploying#automatic-caching)\n*   [Static Assets](https://nextjs.org/docs/pages/building-your-application/deploying#static-assets)\n*   [Configuring Caching](https://nextjs.org/docs/pages/building-your-application/deploying#configuring-caching)\n*   [Build Cache](https://nextjs.org/docs/pages/building-your-application/deploying#build-cache)\n*   [Version Skew](https://nextjs.org/docs/pages/building-your-application/deploying#version-skew)\n*   [Manual Graceful Shutdowns](https://nextjs.org/docs/pages/building-your-application/deploying#manual-graceful-shutdowns)\n\n[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/02-pages/02-building-your-application/09-deploying/index.mdx) [Managed Next.js (Vercel)](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=web&utm_campaign=managed_nextjs_solutions_page) Scroll to top\n\n[Pages Router](https://nextjs.org/docs/pages)[Building Your Application](https://nextjs.org/docs/pages/building-your-application)Deploying\n\nDeploying\n=========\n\nCongratulations, it's time to ship to production.\n\nYou can deploy [managed Next.js with Vercel](https://nextjs.org/docs/pages/building-your-application/deploying#managed-nextjs-with-vercel), or self-host on a Node.js server, Docker image, or even static HTML files. When deploying using `next start`, all Next.js features are supported.\n\n[Production Builds](https://nextjs.org/docs/pages/building-your-application/deploying#production-builds)\n--------------------------------------------------------------------------------------------------------\n\nRunning `next build` generates an optimized version of your application for production. HTML, CSS, and JavaScript files are created based on your pages. JavaScript is **compiled** and browser bundles are **minified** using the [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler) to help achieve the best performance and support [all modern browsers](https://nextjs.org/docs/architecture/supported-browsers).\n\nNext.js produces a standard deployment output used by managed and self-hosted Next.js. This ensures all features are supported across both methods of deployment. In the next major version, we will be transforming this output into our [Build Output API specification](https://vercel.com/docs/build-output-api/v3?utm_source=next-site&utm_medium=docs&utm_campaign=next-website).\n\n[Managed Next.js with Vercel](https://nextjs.org/docs/pages/building-your-application/deploying#managed-nextjs-with-vercel)\n---------------------------------------------------------------------------------------------------------------------------\n\n[Vercel](https://vercel.com/docs/frameworks/nextjs?utm_source=next-site&utm_medium=docs&utm_campaign=next-website), the creators and maintainers of Next.js, provide managed infrastructure and a developer experience platform for your Next.js applications.\n\nDeploying to Vercel is zero-configuration and provides additional enhancements for scalability, availability, and performance globally. However, all Next.js features are still supported when self-hosted.\n\nLearn more about [Next.js on Vercel](https://vercel.com/docs/frameworks/nextjs?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) or [deploy a template for free](https://vercel.com/templates/next.js?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) to try it out.\n\n[Self-Hosting](https://nextjs.org/docs/pages/building-your-application/deploying#self-hosting)\n----------------------------------------------------------------------------------------------\n\nYou can self-host Next.js in three different ways:\n\n*   [A Node.js server](https://nextjs.org/docs/pages/building-your-application/deploying#nodejs-server)\n*   [A Docker container](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image)\n*   [A static export](https://nextjs.org/docs/pages/building-your-application/deploying#static-html-export)\n\n> **🎥 Watch:** Learn more about self-hosting Next.js → [YouTube (45 minutes)](https://www.youtube.com/watch?v=sIVL4JMqRfc).\n\nWe have community maintained deployment examples with the following providers:\n\n*   [Deno](https://github.com/nextjs/deploy-deno)\n*   [DigitalOcean](https://github.com/nextjs/deploy-digitalocean)\n*   [Flightcontrol](https://github.com/nextjs/deploy-flightcontrol)\n*   [Fly.io](https://github.com/nextjs/deploy-fly)\n*   [GitHub Pages](https://github.com/nextjs/deploy-github-pages)\n*   [Google Cloud Run](https://github.com/nextjs/deploy-google-cloud-run)\n*   [Railway](https://github.com/nextjs/deploy-railway)\n*   [Render](https://github.com/nextjs/deploy-render)\n*   [SST](https://github.com/nextjs/deploy-sst)\n\n### [Node.js Server](https://nextjs.org/docs/pages/building-your-application/deploying#nodejs-server)\n\nNext.js can be deployed to any hosting provider that supports Node.js. Ensure your `package.json` has the `\"build\"` and `\"start\"` scripts:\n\npackage.json\n\n```\n{\n  \"scripts\": {\n    \"dev\": \"next dev\",\n    \"build\": \"next build\",\n    \"start\": \"next start\"\n  }\n}\n```\n\nThen, run `npm run build` to build your application. Finally, run `npm run start` to start the Node.js server. This server supports all Next.js features.\n\n### [Docker Image](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image)\n\nNext.js can be deployed to any hosting provider that supports [Docker](https://www.docker.com/) containers. You can use this approach when deploying to container orchestrators such as [Kubernetes](https://kubernetes.io/) or when running inside a container in any cloud provider.\n\n1.  [Install Docker](https://docs.docker.com/get-docker/) on your machine\n2.  [Clone our example](https://github.com/vercel/next.js/tree/canary/examples/with-docker) (or the [multi-environment example](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env))\n3.  Build your container: `docker build -t nextjs-docker .`\n4.  Run your container: `docker run -p 3000:3000 nextjs-docker`\n\nNext.js through Docker supports all Next.js features.\n\n### [Static HTML Export](https://nextjs.org/docs/pages/building-your-application/deploying#static-html-export)\n\nNext.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.\n\nSince Next.js supports this [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports), it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.\n\nRunning as a [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports) does not support Next.js features that require a server. [Learn more](https://nextjs.org/docs/app/building-your-application/deploying/static-exports#unsupported-features).\n\n> **Good to know:**\n> \n> *   [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components) are supported with static exports.\n\n[Features](https://nextjs.org/docs/pages/building-your-application/deploying#features)\n--------------------------------------------------------------------------------------\n\n### [Image Optimization](https://nextjs.org/docs/pages/building-your-application/deploying#image-optimization)\n\n[Image Optimization](https://nextjs.org/docs/app/building-your-application/optimizing/images) through `next/image` works self-hosted with zero configuration when deploying using `next start`. If you would prefer to have a separate service to optimize images, you can [configure an image loader](https://nextjs.org/docs/app/building-your-application/optimizing/images#loaders).\n\nImage Optimization can be used with a [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports#image-optimization) by defining a custom image loader in `next.config.js`. Note that images are optimized at runtime, not during the build.\n\n> **Good to know:**\n> \n> *   On glibc-based Linux systems, Image Optimization may require [additional configuration](https://sharp.pixelplumbing.com/install#linux-memory-allocator) to prevent excessive memory usage.\n> *   Learn more about the [caching behavior of optimized images](https://nextjs.org/docs/app/api-reference/components/image#caching-behavior) and how to configure the TTL.\n> *   You can also [disable Image Optimization](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) and still retain other benefits of using `next/image` if you prefer. For example, if you are optimizing images yourself separately.\n\n### [Middleware](https://nextjs.org/docs/pages/building-your-application/deploying#middleware)\n\n[Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware) works self-hosted with zero configuration when deploying using `next start`. Since it requires access to the incoming request, it is not supported when using a [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports).\n\nMiddleware uses a [runtime](https://nextjs.org/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes) that is a subset of all available Node.js APIs to help ensure low latency, since it may run in front of every route or asset in your application. This runtime does not require running “at the edge” and works in a single-region server. Additional configuration and infrastructure are required to run Middleware in multiple regions.\n\nIf you are looking to add logic (or use an external package) that requires all Node.js APIs, you might be able to move this logic to a [layout](https://nextjs.org/docs/app/building-your-application/routing/layouts-and-templates#layouts) as a [Server Component](https://nextjs.org/docs/app/building-your-application/rendering/server-components). For example, checking [headers](https://nextjs.org/docs/app/api-reference/functions/headers) and [redirecting](https://nextjs.org/docs/app/api-reference/functions/redirect). You can also use headers, cookies, or query parameters to [redirect](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching) or [rewrite](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching) through `next.config.js`. If that does not work, you can also use a [custom server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server).\n\n### [Environment Variables](https://nextjs.org/docs/pages/building-your-application/deploying#environment-variables)\n\nNext.js can support both build time and runtime environment variables.\n\n**By default, environment variables are only available on the server**. To expose an environment variable to the browser, it must be prefixed with `NEXT_PUBLIC_`. However, these public environment variables will be inlined into the JavaScript bundle during `next build`.\n\nTo read runtime environment variables, we recommend using `getServerSideProps` or [incrementally adopting the App Router](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration).\n\nThis allows you to use a singular Docker image that can be promoted through multiple environments with different values.\n\n> **Good to know:**\n> \n> *   You can run code on server startup using the [`register` function](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation).\n> *   We do not recommend using the [runtimeConfig](https://nextjs.org/docs/pages/api-reference/config/next-config-js/runtime-configuration) option, as this does not work with the standalone output mode. Instead, we recommend [incrementally adopting](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration) the App Router.\n\n### [Caching and ISR](https://nextjs.org/docs/pages/building-your-application/deploying#caching-and-isr)\n\nNext.js can cache responses, generated static pages, build outputs, and other static assets like images, fonts, and scripts.\n\nCaching and revalidating pages (with [Incremental Static Regeneration](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration)) use the **same shared cache**. By default, this cache is stored to the filesystem (on disk) on your Next.js server. **This works automatically when self-hosting** using both the Pages and App Router.\n\nYou can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.\n\n#### [Automatic Caching](https://nextjs.org/docs/pages/building-your-application/deploying#automatic-caching)\n\n*   Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` to truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](https://nextjs.org/docs/app/building-your-application/optimizing/images#local-images). You can [configure the TTL](https://nextjs.org/docs/app/api-reference/components/image#caching-behavior) for images.\n*   Incremental Static Regeneration (ISR) sets the `Cache-Control` header of `s-maxage: <revalidate in getStaticProps>, stale-while-revalidate`. This revalidation time is defined in your [`getStaticProps` function](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) in seconds. If you set `revalidate: false`, it will default to a one-year cache duration.\n*   Dynamically rendered pages set a `Cache-Control` header of `private, no-cache, no-store, max-age=0, must-revalidate` to prevent user-specific data from being cached. This applies to both the App Router and Pages Router. This also includes [Draft Mode](https://nextjs.org/docs/app/building-your-application/configuring/draft-mode).\n\n#### [Static Assets](https://nextjs.org/docs/pages/building-your-application/deploying#static-assets)\n\nIf you want to host static assets on a different domain or CDN, you can use the `assetPrefix` [configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix) in `next.config.js`. Next.js will use this asset prefix when retrieving JavaScript or CSS files. Separating your assets to a different domain does come with the downside of extra time spent on DNS and TLS resolution.\n\n[Learn more about `assetPrefix`](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix).\n\n#### [Configuring Caching](https://nextjs.org/docs/pages/building-your-application/deploying#configuring-caching)\n\nBy default, generated cache assets will be stored in memory (defaults to 50mb) and on disk. If you are hosting Next.js using a container orchestration platform like Kubernetes, each pod will have a copy of the cache. To prevent stale data from being shown since the cache is not shared between pods by default, you can configure the Next.js cache to provide a cache handler and disable in-memory caching.\n\nTo configure the ISR/Data Cache location when self-hosting, you can configure a custom handler in your `next.config.js` file:\n\nnext.config.js\n\n```\nmodule.exports = {\n  cacheHandler: require.resolve('./cache-handler.js'),\n  cacheMaxMemorySize: 0, // disable default in-memory caching\n}\n```\n\nThen, create `cache-handler.js` in the root of your project, for example:\n\ncache-handler.js\n\n```\nconst cache = new Map()\n \nmodule.exports = class CacheHandler {\n  constructor(options) {\n    this.options = options\n  }\n \n  async get(key) {\n    // This could be stored anywhere, like durable storage\n    return cache.get(key)\n  }\n \n  async set(key, data, ctx) {\n    // This could be stored anywhere, like durable storage\n    cache.set(key, {\n      value: data,\n      lastModified: Date.now(),\n      tags: ctx.tags,\n    })\n  }\n \n  async revalidateTag(tags) {\n    // tags is either a string or an array of strings\n    tags = [tags].flat()\n    // Iterate over all entries in the cache\n    for (let [key, value] of cache) {\n      // If the value's tags include the specified tag, delete this entry\n      if (value.tags.some((tag) => tags.includes(tag))) {\n        cache.delete(key)\n      }\n    }\n  }\n \n  // If you want to have temporary in memory cache for a single request that is reset\n  // before the next request you can leverage this method\n  resetRequestCache() {}\n}\n```\n\nUsing a custom cache handler will allow you to ensure consistency across all pods hosting your Next.js application. For instance, you can save the cached values anywhere, like [Redis](https://github.com/vercel/next.js/tree/canary/examples/cache-handler-redis) or AWS S3.\n\n> **Good to know:**\n> \n> *   `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call the `revalidateTag` function with a special default tag for the provided page.\n\n### [Build Cache](https://nextjs.org/docs/pages/building-your-application/deploying#build-cache)\n\nNext.js generates an ID during `next build` to identify which version of your application is being served. The same build should be used and boot up multiple containers.\n\nIf you are rebuilding for each stage of your environment, you will need to generate a consistent build ID to use between containers. Use the `generateBuildId` command in `next.config.js`:\n\nnext.config.js\n\n```\nmodule.exports = {\n  generateBuildId: async () => {\n    // This could be anything, using the latest git hash\n    return process.env.GIT_HASH\n  },\n}\n```\n\n### [Version Skew](https://nextjs.org/docs/pages/building-your-application/deploying#version-skew)\n\nNext.js will automatically mitigate most instances of [version skew](https://www.industrialempathy.com/posts/version-skew/) and automatically reload the application to retrieve new assets when detected. For example, if there is a mismatch in the `deploymentId`, transitions between pages will perform a hard navigation versus using a prefetched value.\n\nWhen the application is reloaded, there may be a loss of application state if it's not designed to persist between page navigations. For example, using URL state or local storage would persist state after a page refresh. However, component state like `useState` would be lost in such navigations.\n\nVercel provides additional [skew protection](https://vercel.com/docs/deployments/skew-protection?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) for Next.js applications to ensure assets and functions from the previous version are still available to older clients, even after the new version is deployed.\n\nYou can manually configure the `deploymentId` property in your `next.config.js` file to ensure each request uses either `?dpl` query string or `x-deployment-id` header.\n\n[Manual Graceful Shutdowns](https://nextjs.org/docs/pages/building-your-application/deploying#manual-graceful-shutdowns)\n------------------------------------------------------------------------------------------------------------------------\n\nWhen self-hosting, you might want to run code when the server shuts down on `SIGTERM` or `SIGINT` signals.\n\nYou can set the env variable `NEXT_MANUAL_SIG_HANDLE` to `true` and then register a handler for that signal inside your `_document.js` file. You will need to register the environment variable directly in the `package.json` script, and not in the `.env` file.\n\n> **Good to know**: Manual signal handling is not available in `next dev`.\n\npackage.json\n\n```\n{\n  \"scripts\": {\n    \"dev\": \"next dev\",\n    \"build\": \"next build\",\n    \"start\": \"NEXT_MANUAL_SIG_HANDLE=true next start\"\n  }\n}\n```\n\npages/\\_document.js\n\n```\nif (process.env.NEXT_MANUAL_SIG_HANDLE) {\n  process.on('SIGTERM', () => {\n    console.log('Received SIGTERM: cleaning up')\n    process.exit(0)\n  })\n  process.on('SIGINT', () => {\n    console.log('Received SIGINT: cleaning up')\n    process.exit(0)\n  })\n}\n```\n\n[### Production Checklist Recommendations to ensure the best performance and user experience before taking your Next.js application to production.](https://nextjs.org/docs/pages/building-your-application/deploying/production-checklist)[### Static Exports Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.](https://nextjs.org/docs/pages/building-your-application/deploying/static-exports)[### Multi-Zones Learn how to build micro-frontends using Next.js Multi-Zones to deploy multiple Next.js apps under a single domain.](https://nextjs.org/docs/pages/building-your-application/deploying/multi-zones)[### Continuous Integration (CI) Build Caching Learn how to configure CI to cache Next.js builds](https://nextjs.org/docs/pages/building-your-application/deploying/ci-build-caching)\n\n[Previous Authentication](https://nextjs.org/docs/pages/building-your-application/authentication)\n\n[Next Production Checklist](https://nextjs.org/docs/pages/building-your-application/deploying/production-checklist)\n\nWas this helpful?\n\nsupported.\n\nSend\n\n[](https://vercel.com/home?utm_source=next-site&utm_medium=footer&utm_campaign=next-website \"Go to the Vercel website\")\n\n[![Image 11: GitHub Logo](https://nextjs.org/icons/github.svg)](https://github.com/vercel/next.js)\n\n* * *\n\n[![Image 12: X Logo](https://nextjs.org/icons/x.svg)](https://twitter.com/nextjs)\n\n* * *\n\n[![Image 13: Bluesky Logo](https://nextjs.org/icons/bluesky.svg)](https://bsky.app/profile/nextjs.org)\n\n#### Resources\n\n[Docs](https://nextjs.org/docs)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Analytics](https://vercel.com/analytics?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[Next.js Conf](https://nextjs.org/conf)[Previews](https://vercel.com/products/previews?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)\n\n#### More\n\n[Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[Contact Sales](https://vercel.com/contact/sales?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[GitHub](https://github.com/vercel/next.js)[Releases](https://github.com/vercel/next.js/releases)[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)\n\n#### About Vercel\n\n[Next.js + Vercel](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[Open Source Software](https://vercel.com/oss?utm_source=next-site&utm_medium=footer&utm_campaign=docs_pages_building-your-application_deploying)[GitHub](https://github.com/vercel)[Bluesky](https://bsky.app/profile/vercel.com)[X](https://twitter.com/vercel)\n\n#### Legal\n\n[Privacy Policy](https://vercel.com/legal/privacy-policy)Cookie Preferences\n\n#### Subscribe to our newsletter\n\nStay updated on new releases and features, guides, and case studies.\n\nSubscribe\n\n© 2025 Vercel, Inc.\n\n[![Image 14: GitHub Logo](https://nextjs.org/icons/github.svg)](https://github.com/vercel/next.js)\n\n* * *\n\n[![Image 15: X Logo](https://nextjs.org/icons/x.svg)](https://x.com/nextjs)\n\n* * *\n\n[![Image 16: Bluesky Logo](https://nextjs.org/icons/bluesky.svg)](https://bsky.app/profile/nextjs.org)",
  "usage": {
    "tokens": 14628
  }
}
```
