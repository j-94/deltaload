---
title: GitHub - poulainv/tottem: Bookmark manager on steroid built with React / NextJs / Apollo Tools / Prisma 2 — styled with TailwindCSS 🌱🎺
description: Bookmark manager on steroid built with React / NextJs / Apollo Tools / Prisma 2 — styled with TailwindCSS 🌱🎺 - poulainv/tottem
url: https://github.com/poulainv/tottem
timestamp: 2025-01-20T15:31:22.584Z
domain: github.com
path: poulainv_tottem
---

# GitHub - poulainv/tottem: Bookmark manager on steroid built with React / NextJs / Apollo Tools / Prisma 2 — styled with TailwindCSS 🌱🎺


Bookmark manager on steroid built with React / NextJs / Apollo Tools / Prisma 2 — styled with TailwindCSS 🌱🎺 - poulainv/tottem


## Content

Tottem is an open source experimentation, it aims combining personal productivity tool approach with (slow) social media capabilities to make users empowered and somehow emancipated.

[![Image 19: Tottem](https://github.com/poulainv/tottem/raw/master/public/logo.png)](https://beta.tottem.app/)

### Library management made social

[](https://github.com/poulainv/tottem?screenshot=true#library-management-made-social)

I have two considerations in mind:

*   building a product based on ethic design
*   experimenting open-source web technologies and share it

Summary
-------

[](https://github.com/poulainv/tottem?screenshot=true#summary)

*   [Summary](https://github.com/poulainv/tottem?screenshot=true#summary)
*   [Tech](https://github.com/poulainv/tottem?screenshot=true#tech)
    *   [Codebase](https://github.com/poulainv/tottem?screenshot=true#codebase)
        *   [Main technologies](https://github.com/poulainv/tottem?screenshot=true#main-technologies)
        *   [Repository structure — front-end](https://github.com/poulainv/tottem?screenshot=true#repository-structure--front-end)
        *   [How is it typesafe from end-to-end?](https://github.com/poulainv/tottem?screenshot=true#how-is-it-typesafe-from-end-to-end)
        *   [Global state management](https://github.com/poulainv/tottem?screenshot=true#global-state-management)
    *   [SSR Workflow](https://github.com/poulainv/tottem?screenshot=true#ssr-workflow)
    *   [Deployment](https://github.com/poulainv/tottem?screenshot=true#deployment)
    *   [Setup](https://github.com/poulainv/tottem?screenshot=true#setup)
*   [Product](https://github.com/poulainv/tottem?screenshot=true#product)
    *   [Why ?](https://github.com/poulainv/tottem?screenshot=true#why)
    *   [How ?](https://github.com/poulainv/tottem?screenshot=true#how)
*   [Contributors](https://github.com/poulainv/tottem?screenshot=true#contributors)

[![Image 20: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-section.png)](https://beta.tottem.app/)

Tech
----

[](https://github.com/poulainv/tottem?screenshot=true#tech)

First goal: experimenting the tools that are available to build web software in 2020. This documentation explains which technologies are used here and how they are organised.

### Codebase

[](https://github.com/poulainv/tottem?screenshot=true#codebase)

#### Main technologies

[](https://github.com/poulainv/tottem?screenshot=true#main-technologies)

It's a full-stack Typescript app with some code generation in order to have a type safe experience from end-to-end.

Here is a list of main technologies used:

*   🚀 [React](https://github.com/facebook/react)
*   🥇 [NextJS](https://github.com/zeit/next.js) to provide fast SSR experience
*   😍 [TailwindCSS](https://github.com/tailwindcss/tailwindcss)
*   📱 GraphQL, powered by [Apollo tools](https://github.com/apollographql)
*   👮‍♂️ [Auth0](https://auth0.com/) for authentication
*   🚓 [Prisma Framework](https://github.com/prisma/prisma2) to manage data model and database

#### Repository structure — front-end

[](https://github.com/poulainv/tottem?screenshot=true#repository-structure--front-end)

Inspired by those [recommendations](https://medium.com/@alexmngn/how-to-better-organize-your-react-applications-2fd3ea1920f1), this is how the codebase is structured:

tottem/
├── api # contains graphlq endpoint based on Apollo Server & Prisma2
├──── prisma # contains model definitions & database migration logbook
├──── src/schema # contains graphql resolvers using Prisma Client
├── src
├──── generated # contains generated code (types, hooks, ...)
├──── pages # static and dynamic routes declaration used by NextJS
├──── components # shared generic component
├──── scenes # different parts of the application
├────── moduleName # Auth | Profile | Me ...
├──────── components # module components. \*\*Each\*\* components can specify its own specific components, queries, ...
├──────── queries.gql # All data queries and mutations are written in gql files
├──────── hooks.ts # Most of the reusable logic is written in hooks
├──────── index.tsx # Main scene file
├──────── View.tsx # Sometime stateless component are isolated in View file for clarity or reusability
└──── services # shared services as authentication, error management, ...

#### How is it typesafe from end-to-end?

[](https://github.com/poulainv/tottem?screenshot=true#how-is-it-typesafe-from-end-to-end)

*   **Prisma** provides a [library](https://github.com/prisma/photonjs) Photon that _generate_ a typesafe client to manipulate data depending on a unique schema declaration in `schema.prisma` file.

Example where Photon is used to retrieve the not softly deleted items from specific collection :

```
const items = (
    await ctx.photon.items.findMany({
        where: {
            collection: { id: collectionId },
            isDeleted: false,
        },
        select: { id: true, position: true },
        orderBy: { createdAt: 'desc' },
    })
```

*   **Nexus** provides a code-first graphql approach that allows you to _generate_ graphql schema (`schema.graphql` file) based on your resolvers and object definitions. Nexus is fully compliant with prisma and offers a nice [plugin](https://github.com/prisma-labs/nexus-prisma) to automatically declare resolvers based on your photon client.
    
*   **graphql-codegen** [tool](https://graphql-code-generator.com/) is configured to parse all `.gql` front-end files containing graphl queries and mutations. **graphql-codegen** uses remote and local (`localSchema.gql`) graphql schemas to generate every type and hook we need (putting them inside `types.ts`) so we can safely fetch and mutate data.
    

> Note that when global state management is required, Apollo Client is used as much as possible.

Example where typesafe hook `useGetItemsQuery` is generated allowing to fetch data via Apollo Client smoothly

```
const { data } = useGetItemsQuery({
        variables: {
            collectionId,
        },
    })
```

🤯 No typo anymore, much less files & context switching with typescript ✨

#### Global state management

[](https://github.com/poulainv/tottem?screenshot=true#global-state-management)

Most of the time, global state approach is used to avoid _props drilling_. Neither Redux or React Context API are used here. It has been implemented with Apollo Client. A local schema is defined in `localSchema.gql`

type Breadcrumb {
    title: String!
    href: String!
}

extend type Query {
    breadcrumbs: \[Breadcrumb!\]!
}

Then, we can define

1.  **Query** to read data from Apollo cache

query getBreadcrumbs {
    breadcrumbs @client {
        title
        href
    }
}

`codegraphql-code` is configured to generate this simple hook query, used in Profile/TopBar for instance:

const { data } \= useGetBreadcrumbsQuery()

2 **Custom hooks** to write data to cache with Apollo `client`

const useBreadcrumbs \= (profileSlug: string) \=\> {
    const client \= useApolloClient()

    const setBreadcrumbs \= ({ breadcrumbs }: GetCollectionProfileQuery) \=\> {
        client.writeData({
            data: {
                breadcrumbs,
            },
        })
    }

    const resetBreadcrumbs \= () \=\> {
        client.writeData({
            data: {
                breadcrumbs: \[\],
            },
        })
    }

    return { resetBreadcrumbs, setBreadcrumbs }
}

### SSR Workflow

[](https://github.com/poulainv/tottem?screenshot=true#ssr-workflow)

NextJS provides SSR features that make user experience awesome. NextJS comes with the concept of pre-rendering built-in, that can take 2 forms:

*   Static Generation
*   Server-side rendering

When developing an app, pages are usually not static and need to be rendered on-demand depending on the context (ie. user). [NextJS documentation](https://nextjs.org/docs) is great. However, it can be a bit confusing and hard to deeply understand what's happening when we use NextJS / SSR. This is a sequence diagram aims explaining how NextJS SSR works in Tottem case:

[![Image 21: Tottem](https://github.com/poulainv/tottem/raw/master/public/ssr-diagram.png)](https://github.com/poulainv/tottem/blob/master)

### Deployment

[](https://github.com/poulainv/tottem?screenshot=true#deployment)

The app is fully deployed on Zeit Now. Configuration can be found in `now.json` file. Merging on master trigger new deployment.

The API runtime is _serverless_ and run via [Now Serverless Functions](https://zeit.co/docs/v2/serverless-functions/introduction). As described [here](https://github.com/poulainv/tottem/pull/113#issuecomment-577685621), API performance with Prisma Client is pretty good even with coldstart.

### Setup

[](https://github.com/poulainv/tottem?screenshot=true#setup)

Locally PG instance is needed with some var env set. In `.env` for instance

AUTH0\_LOCAL\_ID='auth0|5dc8800986c8ba0e74d73654' # set local user id by passing auth0
AUTH0\_CALLBACK='http://localhost:3000/auth/callback'
DATABASE\_URL="postgresql://XXX@localhost:5432/XXX?sslaccept=accept\_invalid\_certs"
GRAPHQL\_URL='http://localhost:4000/graphql'
DATABASE\_PROVIDER="postgresql"

Then, two repositories are needed

git clone git@github.com:poulainv/tottem.git
cd tottem
npm install
npm run dev

cd tottem
cd api
npm install
npm run dev

Web app is available on `http://localhost:3000` and graphql endpoint on `http://localhost:4000/graphql`

Product
-------

[](https://github.com/poulainv/tottem?screenshot=true#product)

Second goal: designing a product human centered allowing people to build and manage their online and public library. A tool to manage and gather the content we love, in order to share it with friends & community 😇

[![Image 22: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-inbox.png)](https://beta.tottem.app/)

### Why ?

[](https://github.com/poulainv/tottem?screenshot=true#why-)

More and more, people — especially journalists, are losing their ability to choose which content to promote & amplify. Instead, automatic recommendation algorithms carefully choose the _best_ (sic!) content to amplify. As reader, those deep learning algorithms create a unique & personal narrative stream of content in your social feed... How it can be the _best_ ? Not really, it's just designed to maximize clicks and views. Of course, what else they can do?

[Here, I'm happy to share some references](https://beta.tottem.app/vincent/c/inspirational-content-about-why-social-media-companies-are-dangerous-for-personal-attention-and-democracy-ck5i4lwp2000vws9e4ry25feh)

So, what if I want to explore durable book or article recommendations from a friend? What if I want to really dig into a specific subject?

### How ?

[](https://github.com/poulainv/tottem?screenshot=true#how-)

Tottem aims combining personal productivity tool approach with (slow) social media capabilities to make users empowered and somehow emancipated.

Tottem aims to provide the same high quality user experience that most of modern productivity tools provide. Managing your library should be easy and enjoyable. With a great tool, great content could be made and shared.

The basic workflow:

1.  Collect everything in one Inbox.
2.  Organise into Spaces and Collection.
3.  Express yourself and explain your opinion
4.  Publish and share with your community

[![Image 23: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-profile.png)](https://beta.tottem.app/)

### Design

[](https://github.com/poulainv/tottem?screenshot=true#design)

The UI/UX design is obviously inspired by [Notion](https://notion.so/) and [Things 3](https://culturedcode.com/things/). The design work made with Figma is available [there](https://www.figma.com/file/isqiSo35dfp5oGIpYZlCM6/Tottem-Design?node-id=255%3A1261)

[![Image 24: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-design.png)](https://www.figma.com/file/isqiSo35dfp5oGIpYZlCM6/Tottem-Design?node-id=255%3A1261)

Contributors
------------

[](https://github.com/poulainv/tottem?screenshot=true#contributors)

*   Clément Déon [@deonclem](https://github.com/deonclem)

## Metadata

```json
{
  "title": "GitHub - poulainv/tottem: Bookmark manager on steroid built with React / NextJs / Apollo Tools / Prisma 2 — styled with TailwindCSS 🌱🎺",
  "description": "Bookmark manager on steroid built with React / NextJs / Apollo Tools / Prisma 2 — styled with TailwindCSS 🌱🎺 - poulainv/tottem",
  "url": "https://github.com/poulainv/tottem?screenshot=true",
  "content": "Tottem is an open source experimentation, it aims combining personal productivity tool approach with (slow) social media capabilities to make users empowered and somehow emancipated.\n\n[![Image 19: Tottem](https://github.com/poulainv/tottem/raw/master/public/logo.png)](https://beta.tottem.app/)\n\n### Library management made social\n\n[](https://github.com/poulainv/tottem?screenshot=true#library-management-made-social)\n\nI have two considerations in mind:\n\n*   building a product based on ethic design\n*   experimenting open-source web technologies and share it\n\nSummary\n-------\n\n[](https://github.com/poulainv/tottem?screenshot=true#summary)\n\n*   [Summary](https://github.com/poulainv/tottem?screenshot=true#summary)\n*   [Tech](https://github.com/poulainv/tottem?screenshot=true#tech)\n    *   [Codebase](https://github.com/poulainv/tottem?screenshot=true#codebase)\n        *   [Main technologies](https://github.com/poulainv/tottem?screenshot=true#main-technologies)\n        *   [Repository structure — front-end](https://github.com/poulainv/tottem?screenshot=true#repository-structure--front-end)\n        *   [How is it typesafe from end-to-end?](https://github.com/poulainv/tottem?screenshot=true#how-is-it-typesafe-from-end-to-end)\n        *   [Global state management](https://github.com/poulainv/tottem?screenshot=true#global-state-management)\n    *   [SSR Workflow](https://github.com/poulainv/tottem?screenshot=true#ssr-workflow)\n    *   [Deployment](https://github.com/poulainv/tottem?screenshot=true#deployment)\n    *   [Setup](https://github.com/poulainv/tottem?screenshot=true#setup)\n*   [Product](https://github.com/poulainv/tottem?screenshot=true#product)\n    *   [Why ?](https://github.com/poulainv/tottem?screenshot=true#why)\n    *   [How ?](https://github.com/poulainv/tottem?screenshot=true#how)\n*   [Contributors](https://github.com/poulainv/tottem?screenshot=true#contributors)\n\n[![Image 20: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-section.png)](https://beta.tottem.app/)\n\nTech\n----\n\n[](https://github.com/poulainv/tottem?screenshot=true#tech)\n\nFirst goal: experimenting the tools that are available to build web software in 2020. This documentation explains which technologies are used here and how they are organised.\n\n### Codebase\n\n[](https://github.com/poulainv/tottem?screenshot=true#codebase)\n\n#### Main technologies\n\n[](https://github.com/poulainv/tottem?screenshot=true#main-technologies)\n\nIt's a full-stack Typescript app with some code generation in order to have a type safe experience from end-to-end.\n\nHere is a list of main technologies used:\n\n*   🚀 [React](https://github.com/facebook/react)\n*   🥇 [NextJS](https://github.com/zeit/next.js) to provide fast SSR experience\n*   😍 [TailwindCSS](https://github.com/tailwindcss/tailwindcss)\n*   📱 GraphQL, powered by [Apollo tools](https://github.com/apollographql)\n*   👮‍♂️ [Auth0](https://auth0.com/) for authentication\n*   🚓 [Prisma Framework](https://github.com/prisma/prisma2) to manage data model and database\n\n#### Repository structure — front-end\n\n[](https://github.com/poulainv/tottem?screenshot=true#repository-structure--front-end)\n\nInspired by those [recommendations](https://medium.com/@alexmngn/how-to-better-organize-your-react-applications-2fd3ea1920f1), this is how the codebase is structured:\n\ntottem/\n├── api # contains graphlq endpoint based on Apollo Server & Prisma2\n├──── prisma # contains model definitions & database migration logbook\n├──── src/schema # contains graphql resolvers using Prisma Client\n├── src\n├──── generated # contains generated code (types, hooks, ...)\n├──── pages # static and dynamic routes declaration used by NextJS\n├──── components # shared generic component\n├──── scenes # different parts of the application\n├────── moduleName # Auth | Profile | Me ...\n├──────── components # module components. \\*\\*Each\\*\\* components can specify its own specific components, queries, ...\n├──────── queries.gql # All data queries and mutations are written in gql files\n├──────── hooks.ts # Most of the reusable logic is written in hooks\n├──────── index.tsx # Main scene file\n├──────── View.tsx # Sometime stateless component are isolated in View file for clarity or reusability\n└──── services # shared services as authentication, error management, ...\n\n#### How is it typesafe from end-to-end?\n\n[](https://github.com/poulainv/tottem?screenshot=true#how-is-it-typesafe-from-end-to-end)\n\n*   **Prisma** provides a [library](https://github.com/prisma/photonjs) Photon that _generate_ a typesafe client to manipulate data depending on a unique schema declaration in `schema.prisma` file.\n\nExample where Photon is used to retrieve the not softly deleted items from specific collection :\n\n```\nconst items = (\n    await ctx.photon.items.findMany({\n        where: {\n            collection: { id: collectionId },\n            isDeleted: false,\n        },\n        select: { id: true, position: true },\n        orderBy: { createdAt: 'desc' },\n    })\n```\n\n*   **Nexus** provides a code-first graphql approach that allows you to _generate_ graphql schema (`schema.graphql` file) based on your resolvers and object definitions. Nexus is fully compliant with prisma and offers a nice [plugin](https://github.com/prisma-labs/nexus-prisma) to automatically declare resolvers based on your photon client.\n    \n*   **graphql-codegen** [tool](https://graphql-code-generator.com/) is configured to parse all `.gql` front-end files containing graphl queries and mutations. **graphql-codegen** uses remote and local (`localSchema.gql`) graphql schemas to generate every type and hook we need (putting them inside `types.ts`) so we can safely fetch and mutate data.\n    \n\n> Note that when global state management is required, Apollo Client is used as much as possible.\n\nExample where typesafe hook `useGetItemsQuery` is generated allowing to fetch data via Apollo Client smoothly\n\n```\nconst { data } = useGetItemsQuery({\n        variables: {\n            collectionId,\n        },\n    })\n```\n\n🤯 No typo anymore, much less files & context switching with typescript ✨\n\n#### Global state management\n\n[](https://github.com/poulainv/tottem?screenshot=true#global-state-management)\n\nMost of the time, global state approach is used to avoid _props drilling_. Neither Redux or React Context API are used here. It has been implemented with Apollo Client. A local schema is defined in `localSchema.gql`\n\ntype Breadcrumb {\n    title: String!\n    href: String!\n}\n\nextend type Query {\n    breadcrumbs: \\[Breadcrumb!\\]!\n}\n\nThen, we can define\n\n1.  **Query** to read data from Apollo cache\n\nquery getBreadcrumbs {\n    breadcrumbs @client {\n        title\n        href\n    }\n}\n\n`codegraphql-code` is configured to generate this simple hook query, used in Profile/TopBar for instance:\n\nconst { data } \\= useGetBreadcrumbsQuery()\n\n2 **Custom hooks** to write data to cache with Apollo `client`\n\nconst useBreadcrumbs \\= (profileSlug: string) \\=\\> {\n    const client \\= useApolloClient()\n\n    const setBreadcrumbs \\= ({ breadcrumbs }: GetCollectionProfileQuery) \\=\\> {\n        client.writeData({\n            data: {\n                breadcrumbs,\n            },\n        })\n    }\n\n    const resetBreadcrumbs \\= () \\=\\> {\n        client.writeData({\n            data: {\n                breadcrumbs: \\[\\],\n            },\n        })\n    }\n\n    return { resetBreadcrumbs, setBreadcrumbs }\n}\n\n### SSR Workflow\n\n[](https://github.com/poulainv/tottem?screenshot=true#ssr-workflow)\n\nNextJS provides SSR features that make user experience awesome. NextJS comes with the concept of pre-rendering built-in, that can take 2 forms:\n\n*   Static Generation\n*   Server-side rendering\n\nWhen developing an app, pages are usually not static and need to be rendered on-demand depending on the context (ie. user). [NextJS documentation](https://nextjs.org/docs) is great. However, it can be a bit confusing and hard to deeply understand what's happening when we use NextJS / SSR. This is a sequence diagram aims explaining how NextJS SSR works in Tottem case:\n\n[![Image 21: Tottem](https://github.com/poulainv/tottem/raw/master/public/ssr-diagram.png)](https://github.com/poulainv/tottem/blob/master)\n\n### Deployment\n\n[](https://github.com/poulainv/tottem?screenshot=true#deployment)\n\nThe app is fully deployed on Zeit Now. Configuration can be found in `now.json` file. Merging on master trigger new deployment.\n\nThe API runtime is _serverless_ and run via [Now Serverless Functions](https://zeit.co/docs/v2/serverless-functions/introduction). As described [here](https://github.com/poulainv/tottem/pull/113#issuecomment-577685621), API performance with Prisma Client is pretty good even with coldstart.\n\n### Setup\n\n[](https://github.com/poulainv/tottem?screenshot=true#setup)\n\nLocally PG instance is needed with some var env set. In `.env` for instance\n\nAUTH0\\_LOCAL\\_ID='auth0|5dc8800986c8ba0e74d73654' # set local user id by passing auth0\nAUTH0\\_CALLBACK='http://localhost:3000/auth/callback'\nDATABASE\\_URL=\"postgresql://XXX@localhost:5432/XXX?sslaccept=accept\\_invalid\\_certs\"\nGRAPHQL\\_URL='http://localhost:4000/graphql'\nDATABASE\\_PROVIDER=\"postgresql\"\n\nThen, two repositories are needed\n\ngit clone git@github.com:poulainv/tottem.git\ncd tottem\nnpm install\nnpm run dev\n\ncd tottem\ncd api\nnpm install\nnpm run dev\n\nWeb app is available on `http://localhost:3000` and graphql endpoint on `http://localhost:4000/graphql`\n\nProduct\n-------\n\n[](https://github.com/poulainv/tottem?screenshot=true#product)\n\nSecond goal: designing a product human centered allowing people to build and manage their online and public library. A tool to manage and gather the content we love, in order to share it with friends & community 😇\n\n[![Image 22: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-inbox.png)](https://beta.tottem.app/)\n\n### Why ?\n\n[](https://github.com/poulainv/tottem?screenshot=true#why-)\n\nMore and more, people — especially journalists, are losing their ability to choose which content to promote & amplify. Instead, automatic recommendation algorithms carefully choose the _best_ (sic!) content to amplify. As reader, those deep learning algorithms create a unique & personal narrative stream of content in your social feed... How it can be the _best_ ? Not really, it's just designed to maximize clicks and views. Of course, what else they can do?\n\n[Here, I'm happy to share some references](https://beta.tottem.app/vincent/c/inspirational-content-about-why-social-media-companies-are-dangerous-for-personal-attention-and-democracy-ck5i4lwp2000vws9e4ry25feh)\n\nSo, what if I want to explore durable book or article recommendations from a friend? What if I want to really dig into a specific subject?\n\n### How ?\n\n[](https://github.com/poulainv/tottem?screenshot=true#how-)\n\nTottem aims combining personal productivity tool approach with (slow) social media capabilities to make users empowered and somehow emancipated.\n\nTottem aims to provide the same high quality user experience that most of modern productivity tools provide. Managing your library should be easy and enjoyable. With a great tool, great content could be made and shared.\n\nThe basic workflow:\n\n1.  Collect everything in one Inbox.\n2.  Organise into Spaces and Collection.\n3.  Express yourself and explain your opinion\n4.  Publish and share with your community\n\n[![Image 23: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-profile.png)](https://beta.tottem.app/)\n\n### Design\n\n[](https://github.com/poulainv/tottem?screenshot=true#design)\n\nThe UI/UX design is obviously inspired by [Notion](https://notion.so/) and [Things 3](https://culturedcode.com/things/). The design work made with Figma is available [there](https://www.figma.com/file/isqiSo35dfp5oGIpYZlCM6/Tottem-Design?node-id=255%3A1261)\n\n[![Image 24: Tottem](https://github.com/poulainv/tottem/raw/master/public/screenshot-design.png)](https://www.figma.com/file/isqiSo35dfp5oGIpYZlCM6/Tottem-Design?node-id=255%3A1261)\n\nContributors\n------------\n\n[](https://github.com/poulainv/tottem?screenshot=true#contributors)\n\n*   Clément Déon [@deonclem](https://github.com/deonclem)",
  "usage": {
    "tokens": 3033
  }
}
```
