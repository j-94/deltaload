---
title: Documentation / Start Here — BaseHub Docs
description: Learn how to integrate your Next.js App with BaseHub in a couple of steps.
url: https://basehub.com/docs/framework-guides/nextjs
timestamp: 2025-01-20T16:07:05.602Z
domain: basehub.com
path: docs_framework-guides_nextjs
---

# Documentation / Start Here — BaseHub Docs


Learn how to integrate your Next.js App with BaseHub in a couple of steps.


## Content

Learn how to integrate your Next.js App with BaseHub in a couple of steps.

[Set Up `basehub`](https://basehub.com/docs/framework-guides/nextjs#set-up-basehub)
-----------------------------------------------------------------------------------

Our official JavaScript/TypeScript library exposes a CLI generator that, when run, will generate a type-safe GraphQL client. Check out [our API Reference](https://docs.basehub.com/api-reference/javascript-sdk) for more information.

### Install1

Install with your preferred package manager.

### Add the `BASEHUB_TOKEN` Environment Variable2

Get it from your BaseHub Repo’s README.

```
BASEHUB_TOKEN="<your-token>"

# Remember to also add this ^ env var in your deployment platform
```

### Configure Node Scripts3

In order to generate the BaseHub SDK, we recommend running `basehub dev` in parallel to running the development server, and `basehub` right before building the app.

```
"scripts": {
  "dev": "basehub dev & next dev",
  "build": "basehub && next build",
  "start": "next start",
  "lint": "next lint"
},
```

Using Windows? You might need to use something like `concurrently` instead of using the `&` to run a parallel node process. So:

`concurrently \”basehub dev\” \”next dev\”`

### Start the Dev Server4

Give it a go to make sure the set up went correctly.

Now, let’s go ahead and query some content!

[Your First Query](https://basehub.com/docs/framework-guides/nextjs#your-first-query)
-------------------------------------------------------------------------------------

The recommended way to query content from BaseHub is with `<Pump />`, a React Server Component that enables a Fast Refresh-like experience.

```
import { Pump } from "basehub/react-pump"
import { draftMode } from "next/headers"

const Page = () => {
  return (
    <Pump
      queries={[{ _sys: { id: true } }]}
      draft={draftMode().isEnabled}
      next={{ revalidate: 30 }}
    >
      {async ([data]) => {
        "use server"

        return (
          <pre>
            <code>{JSON.stringify(data, null, 2)}</code>
          </pre>
        )
      }}
    </Pump>
  )
}

export default Page
```

Notice we’re using Next.js’ `draftMode` and passing it down to Pump. You’ll learn more in the next section, but put briefly: when `draft === true`, Pump will subscribe to changes in real time from your Repo, and so keep your UI up-to-date. This is ideal for previewing content before pushing it to production. When `draft === false`, Pump will hit the Query API directly.

## Metadata

```json
{
  "title": "Documentation / Start Here — BaseHub Docs",
  "description": "Learn how to integrate your Next.js App with BaseHub in a couple of steps.",
  "url": "https://basehub.com/docs/framework-guides/nextjs",
  "content": "Learn how to integrate your Next.js App with BaseHub in a couple of steps.\n\n[Set Up `basehub`](https://basehub.com/docs/framework-guides/nextjs#set-up-basehub)\n-----------------------------------------------------------------------------------\n\nOur official JavaScript/TypeScript library exposes a CLI generator that, when run, will generate a type-safe GraphQL client. Check out [our API Reference](https://docs.basehub.com/api-reference/javascript-sdk) for more information.\n\n### Install1\n\nInstall with your preferred package manager.\n\n### Add the `BASEHUB_TOKEN` Environment Variable2\n\nGet it from your BaseHub Repo’s README.\n\n```\nBASEHUB_TOKEN=\"<your-token>\"\n\n# Remember to also add this ^ env var in your deployment platform\n```\n\n### Configure Node Scripts3\n\nIn order to generate the BaseHub SDK, we recommend running `basehub dev` in parallel to running the development server, and `basehub` right before building the app.\n\n```\n\"scripts\": {\n  \"dev\": \"basehub dev & next dev\",\n  \"build\": \"basehub && next build\",\n  \"start\": \"next start\",\n  \"lint\": \"next lint\"\n},\n```\n\nUsing Windows? You might need to use something like `concurrently` instead of using the `&` to run a parallel node process. So:\n\n`concurrently \\”basehub dev\\” \\”next dev\\”`\n\n### Start the Dev Server4\n\nGive it a go to make sure the set up went correctly.\n\nNow, let’s go ahead and query some content!\n\n[Your First Query](https://basehub.com/docs/framework-guides/nextjs#your-first-query)\n-------------------------------------------------------------------------------------\n\nThe recommended way to query content from BaseHub is with `<Pump />`, a React Server Component that enables a Fast Refresh-like experience.\n\n```\nimport { Pump } from \"basehub/react-pump\"\nimport { draftMode } from \"next/headers\"\n\nconst Page = () => {\n  return (\n    <Pump\n      queries={[{ _sys: { id: true } }]}\n      draft={draftMode().isEnabled}\n      next={{ revalidate: 30 }}\n    >\n      {async ([data]) => {\n        \"use server\"\n\n        return (\n          <pre>\n            <code>{JSON.stringify(data, null, 2)}</code>\n          </pre>\n        )\n      }}\n    </Pump>\n  )\n}\n\nexport default Page\n```\n\nNotice we’re using Next.js’ `draftMode` and passing it down to Pump. You’ll learn more in the next section, but put briefly: when `draft === true`, Pump will subscribe to changes in real time from your Repo, and so keep your UI up-to-date. This is ideal for previewing content before pushing it to production. When `draft === false`, Pump will hit the Query API directly.",
  "usage": {
    "tokens": 585
  }
}
```
