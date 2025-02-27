---
title: Advanced – react-tweet
description: Embed tweets in your React application.
url: https://react-tweet.vercel.app/twitter-theme/advanced
timestamp: 2025-01-20T16:02:43.653Z
domain: react-tweet.vercel.app
path: twitter-theme_advanced
---

# Advanced – react-tweet


Embed tweets in your React application.


## Content

Advanced – react-tweet
=============== 

[react-tweet](https://react-tweet.vercel.app/)

[GitHub (opens in a new tab)](https://github.com/vercel-labs/react-tweet)

*   [Introduction](https://react-tweet.vercel.app/)
*   Usage
*   [Next.js](https://react-tweet.vercel.app/next)
*   [Vite](https://react-tweet.vercel.app/vite)
*   [CRA](https://react-tweet.vercel.app/create-react-app)
*   [API Reference](https://react-tweet.vercel.app/api-reference)
*   Themes
*   [Twitter Theme](https://react-tweet.vercel.app/twitter-theme)
    
    *   [API Reference](https://react-tweet.vercel.app/twitter-theme/api-reference)
    *   [Advanced](https://react-tweet.vercel.app/twitter-theme/advanced)
    
*   [Custom Theme](https://react-tweet.vercel.app/custom-theme)
*   More
*   [Contributing](https://react-tweet.vercel.app/contributing)
*   [Next.js Docs ↗ (opens in a new tab)](https://nextjs.org/?utm_source=react-tweet.site&utm_medium=referral&utm_campaign=sidebar)

Light

On This Page

*   [Customizing the theme components](https://react-tweet.vercel.app/twitter-theme/advanced#customizing-the-theme-components)

[Question? Give us feedback → (opens in a new tab)](https://github.com/vercel-labs/react-tweet/issues/new?title=Feedback%20for%20%E2%80%9CAdvanced%E2%80%9D&labels=feedback)[Edit this page on GitHub →](https://github.com/vercel-labs/react-tweet/pages/twitter-theme/advanced.mdx)

[Twitter Theme](https://react-tweet.vercel.app/twitter-theme)

Advanced

Advanced
========

Customizing the theme components[](https://react-tweet.vercel.app/twitter-theme/advanced#customizing-the-theme-components)
--------------------------------------------------------------------------------------------------------------------------

The components used by the Twitter theme allow some simple [customization options](https://react-tweet.vercel.app/twitter-theme/api-reference#custom-tweet-components) for common use cases. However you can also have full control over the tweet by building your own `Tweet` component with the components and features of the theme that you would like to use.

For example, you can build your own tweet component but without the reply button like so:

my-tweet.tsx

```
import type { Tweet } from 'react-tweet/api'
import {
  type TwitterComponents,
  TweetContainer,
  TweetHeader,
  TweetInReplyTo,
  TweetBody,
  TweetMedia,
  TweetInfo,
  TweetActions,
  QuotedTweet,
  enrichTweet,
} from 'react-tweet'
 
type Props = {
  tweet: Tweet
  components?: TwitterComponents
}
 
export const MyTweet = ({ tweet: t, components }: Props) => {
  const tweet = enrichTweet(t)
  return (
    <TweetContainer>
      <TweetHeader tweet={tweet} components={components} />
      {tweet.in_reply_to_status_id_str && <TweetInReplyTo tweet={tweet} />}
      <TweetBody tweet={tweet} />
      {tweet.mediaDetails?.length ? (
        <TweetMedia tweet={tweet} components={components} />
      ) : null}
      {tweet.quoted_tweet && <QuotedTweet tweet={tweet.quoted_tweet} />}
      <TweetInfo tweet={tweet} />
      <TweetActions tweet={tweet} />
      {/* We're not including the `TweetReplies` component that adds the reply button */}
    </TweetContainer>
  )
}
```

Then, you can build your own `Tweet` component that uses the `MyTweet` component:

tweet.tsx

```
import { Suspense } from 'react'
import { getTweet } from 'react-tweet/api'
import { type TweetProps, TweetNotFound, TweetSkeleton } from 'react-tweet'
import { MyTweet } from './my-tweet'
 
const TweetContent = async ({ id, components, onError }: TweetProps) => {
  const tweet = id
    ? await getTweet(id).catch((err) => {
        if (onError) {
          onError(err)
        } else {
          console.error(err)
        }
      })
    : undefined
 
  if (!tweet) {
    const NotFound = components?.TweetNotFound || TweetNotFound
    return <NotFound />
  }
 
  return <MyTweet tweet={tweet} components={components} />
}
 
export const Tweet = ({
  fallback = <TweetSkeleton />,
  ...props
}: TweetProps) => (
  <Suspense fallback={fallback}>
    {/* @ts-ignore: Async components are valid in the app directory */}
    <TweetContent {...props} />
  </Suspense>
)
```

The `Tweet` component uses `Suspense` to progressively load the tweet (non-blocking rendering) and to opt-in into streaming if your framework supports it, like Next.js.

`TweetContent` is an async component that fetches the tweet and passes it to `MyTweet`. `async` only works for [React Server Components (RSC) (opens in a new tab)](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components) so if your framework does not support RSC you can use [SWR (opens in a new tab)](https://swr.vercel.app/) instead:

tweet.tsx

```
'use client'
 
import {
  type TweetProps,
  EmbeddedTweet,
  TweetNotFound,
  TweetSkeleton,
  useTweet,
} from 'react-tweet'
 
export const Tweet = ({
  id,
  apiUrl,
  fallback = <TweetSkeleton />,
  components,
  onError,
}: TweetProps) => {
  const { data, error, isLoading } = useTweet(id, apiUrl)
 
  if (isLoading) return fallback
  if (error || !data) {
    const NotFound = components?.TweetNotFound || TweetNotFound
    return <NotFound error={onError ? onError(error) : error} />
  }
 
  return <EmbeddedTweet tweet={data} components={components} />
}
```

[API Reference](https://react-tweet.vercel.app/twitter-theme/api-reference "API Reference")[Custom Theme](https://react-tweet.vercel.app/custom-theme "Custom Theme")

Light

* * *

[Powered by](https://vercel.com/?utm_source=react-tweet.site "vercel.com homepage")

© 2024 Vercel, Inc. All rights reserved.

## Metadata

```json
{
  "title": "Advanced – react-tweet",
  "description": "Embed tweets in your React application.",
  "url": "https://react-tweet.vercel.app/twitter-theme/advanced",
  "content": "Advanced – react-tweet\n=============== \n\n[react-tweet](https://react-tweet.vercel.app/)\n\n[GitHub (opens in a new tab)](https://github.com/vercel-labs/react-tweet)\n\n*   [Introduction](https://react-tweet.vercel.app/)\n*   Usage\n*   [Next.js](https://react-tweet.vercel.app/next)\n*   [Vite](https://react-tweet.vercel.app/vite)\n*   [CRA](https://react-tweet.vercel.app/create-react-app)\n*   [API Reference](https://react-tweet.vercel.app/api-reference)\n*   Themes\n*   [Twitter Theme](https://react-tweet.vercel.app/twitter-theme)\n    \n    *   [API Reference](https://react-tweet.vercel.app/twitter-theme/api-reference)\n    *   [Advanced](https://react-tweet.vercel.app/twitter-theme/advanced)\n    \n*   [Custom Theme](https://react-tweet.vercel.app/custom-theme)\n*   More\n*   [Contributing](https://react-tweet.vercel.app/contributing)\n*   [Next.js Docs ↗ (opens in a new tab)](https://nextjs.org/?utm_source=react-tweet.site&utm_medium=referral&utm_campaign=sidebar)\n\nLight\n\nOn This Page\n\n*   [Customizing the theme components](https://react-tweet.vercel.app/twitter-theme/advanced#customizing-the-theme-components)\n\n[Question? Give us feedback → (opens in a new tab)](https://github.com/vercel-labs/react-tweet/issues/new?title=Feedback%20for%20%E2%80%9CAdvanced%E2%80%9D&labels=feedback)[Edit this page on GitHub →](https://github.com/vercel-labs/react-tweet/pages/twitter-theme/advanced.mdx)\n\n[Twitter Theme](https://react-tweet.vercel.app/twitter-theme)\n\nAdvanced\n\nAdvanced\n========\n\nCustomizing the theme components[](https://react-tweet.vercel.app/twitter-theme/advanced#customizing-the-theme-components)\n--------------------------------------------------------------------------------------------------------------------------\n\nThe components used by the Twitter theme allow some simple [customization options](https://react-tweet.vercel.app/twitter-theme/api-reference#custom-tweet-components) for common use cases. However you can also have full control over the tweet by building your own `Tweet` component with the components and features of the theme that you would like to use.\n\nFor example, you can build your own tweet component but without the reply button like so:\n\nmy-tweet.tsx\n\n```\nimport type { Tweet } from 'react-tweet/api'\nimport {\n  type TwitterComponents,\n  TweetContainer,\n  TweetHeader,\n  TweetInReplyTo,\n  TweetBody,\n  TweetMedia,\n  TweetInfo,\n  TweetActions,\n  QuotedTweet,\n  enrichTweet,\n} from 'react-tweet'\n \ntype Props = {\n  tweet: Tweet\n  components?: TwitterComponents\n}\n \nexport const MyTweet = ({ tweet: t, components }: Props) => {\n  const tweet = enrichTweet(t)\n  return (\n    <TweetContainer>\n      <TweetHeader tweet={tweet} components={components} />\n      {tweet.in_reply_to_status_id_str && <TweetInReplyTo tweet={tweet} />}\n      <TweetBody tweet={tweet} />\n      {tweet.mediaDetails?.length ? (\n        <TweetMedia tweet={tweet} components={components} />\n      ) : null}\n      {tweet.quoted_tweet && <QuotedTweet tweet={tweet.quoted_tweet} />}\n      <TweetInfo tweet={tweet} />\n      <TweetActions tweet={tweet} />\n      {/* We're not including the `TweetReplies` component that adds the reply button */}\n    </TweetContainer>\n  )\n}\n```\n\nThen, you can build your own `Tweet` component that uses the `MyTweet` component:\n\ntweet.tsx\n\n```\nimport { Suspense } from 'react'\nimport { getTweet } from 'react-tweet/api'\nimport { type TweetProps, TweetNotFound, TweetSkeleton } from 'react-tweet'\nimport { MyTweet } from './my-tweet'\n \nconst TweetContent = async ({ id, components, onError }: TweetProps) => {\n  const tweet = id\n    ? await getTweet(id).catch((err) => {\n        if (onError) {\n          onError(err)\n        } else {\n          console.error(err)\n        }\n      })\n    : undefined\n \n  if (!tweet) {\n    const NotFound = components?.TweetNotFound || TweetNotFound\n    return <NotFound />\n  }\n \n  return <MyTweet tweet={tweet} components={components} />\n}\n \nexport const Tweet = ({\n  fallback = <TweetSkeleton />,\n  ...props\n}: TweetProps) => (\n  <Suspense fallback={fallback}>\n    {/* @ts-ignore: Async components are valid in the app directory */}\n    <TweetContent {...props} />\n  </Suspense>\n)\n```\n\nThe `Tweet` component uses `Suspense` to progressively load the tweet (non-blocking rendering) and to opt-in into streaming if your framework supports it, like Next.js.\n\n`TweetContent` is an async component that fetches the tweet and passes it to `MyTweet`. `async` only works for [React Server Components (RSC) (opens in a new tab)](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components) so if your framework does not support RSC you can use [SWR (opens in a new tab)](https://swr.vercel.app/) instead:\n\ntweet.tsx\n\n```\n'use client'\n \nimport {\n  type TweetProps,\n  EmbeddedTweet,\n  TweetNotFound,\n  TweetSkeleton,\n  useTweet,\n} from 'react-tweet'\n \nexport const Tweet = ({\n  id,\n  apiUrl,\n  fallback = <TweetSkeleton />,\n  components,\n  onError,\n}: TweetProps) => {\n  const { data, error, isLoading } = useTweet(id, apiUrl)\n \n  if (isLoading) return fallback\n  if (error || !data) {\n    const NotFound = components?.TweetNotFound || TweetNotFound\n    return <NotFound error={onError ? onError(error) : error} />\n  }\n \n  return <EmbeddedTweet tweet={data} components={components} />\n}\n```\n\n[API Reference](https://react-tweet.vercel.app/twitter-theme/api-reference \"API Reference\")[Custom Theme](https://react-tweet.vercel.app/custom-theme \"Custom Theme\")\n\nLight\n\n* * *\n\n[Powered by](https://vercel.com/?utm_source=react-tweet.site \"vercel.com homepage\")\n\n© 2024 Vercel, Inc. All rights reserved.",
  "usage": {
    "tokens": 1409
  }
}
```
