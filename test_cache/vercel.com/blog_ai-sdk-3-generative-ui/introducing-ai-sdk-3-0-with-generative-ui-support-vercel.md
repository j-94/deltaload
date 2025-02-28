---
title: Introducing AI SDK 3.0 with Generative UI support - Vercel
description: Stream React Components from LLMs to deliver richer user experiences
url: https://vercel.com/blog/ai-sdk-3-generative-ui
timestamp: 2025-01-20T15:58:43.667Z
domain: vercel.com
path: blog_ai-sdk-3-generative-ui
---

# Introducing AI SDK 3.0 with Generative UI support - Vercel


Stream React Components from LLMs to deliver richer user experiences


## Content

Stream React Components from LLMs to deliver richer user experiences

Last October, we launched [v0.dev](http://v0.dev/), a generative UI design tool that converts text and image prompts to React UIs and streamlines the design engineering process.

Today, we are open sourcing v0's [Generative UI](https://vercel.com/blog/announcing-v0-generative-ui) technology with the release of the [Vercel AI SDK 3.0](https://sdk.vercel.ai/docs). Developers can now move beyond plaintext and markdown chatbots to give LLMs rich, component-based interfaces.

Let your users see more than words can say by rendering components directly within your search experience.

Make it easier for your users to interpret agent execution so they can stay in the loop with the magic behind the scenes.

[Visit our demo](https://sdk.vercel.ai/demo) for a first impression or [read the documentation](https://sdk.vercel.ai/docs/concepts/ai-rsc) for a preview of the new APIs.

[A new user experience for AI](https://vercel.com/blog/ai-sdk-3-generative-ui#a-new-user-experience-for-ai)
-----------------------------------------------------------------------------------------------------------

Products like ChatGPT have made a profound impact: they help users write code, plan travel, translate, summarize text, and so much more. However, LLMs have faced two important UX challenges:

*   Limited or imprecise knowledge
    
*   Plain text / markdown-only responses
    

With the introduction of Tools and Function Calling, developers have been able to build more robust applications that are able to fetch realtime data.

![Image 18](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F3sX5pcePV8FptFPgMqhF7%2F815c20dae6b34b86ab7e40c6c8cd91e5%2FFrame_6__1_.png&w=1920&q=75)![Image 19](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F1UZL6hoRRvHALJ37uGhgJJ%2Fce8ded840e806d9efb5d10906e460044%2FFrame_6__2_.png&w=1920&q=75)

These applications, however, have been challenging to write and are still lacking in richness and interactivity.

Thanks to our experience in developing v0 with [React Server Components (RSC)](https://vercel.com/blog/understanding-react-server-components), we've arrived at a simple abstraction that can solve both these problems.

[A new developer experience for AI](https://vercel.com/blog/ai-sdk-3-generative-ui#a-new-developer-experience-for-ai)
---------------------------------------------------------------------------------------------------------------------

With the AI SDK 3.0, you can now associate LLM responses to streaming React Server Components.

Let's start with the most basic example, streaming text without retrieval or up-to-date information.

```
import { render } from 'ai/rsc'import OpenAI from 'openai'const openai = new OpenAI()async function submitMessage(userInput) {  'use server'  return render({    provider: openai,    model: 'gpt-4',    messages: [      { role: 'system', content: 'You are an assistant' },      { role: 'user', content: userInput }    ],    text: ({ content }) => <p>{content}</p>,  })}
```

Let's now solve both original problems: retrieve the live weather and render a custom UI. If your model supports [OpenAI-compatible Functions or Tools](https://platform.openai.com/docs/assistants/tools/function-calling), you can use the new `render` method to map specific calls to React Server Components.

```
import { render } from 'ai/rsc'import OpenAI from 'openai'import { z } from 'zod'const openai = new OpenAI()async function submitMessage(userInput) { // 'What is the weather in SF?'  'use server'  return render({    provider: openai,    model: 'gpt-4-0125-preview',    messages: [      { role: 'system', content: 'You are a helpful assistant' },      { role: 'user', content: userInput }    ],    text: ({ content }) => <p>{content}</p>,    tools: {      get_city_weather: {        description: 'Get the current weather for a city',        parameters: z.object({          city: z.string().describe('the city')        }).required(),        render: async function* ({ city }) {          yield <Spinner/>          const weather = await getWeather(city)          return <Weather info={weather} />        }      }    }  })}
```

An example of an assistant that renders the weather information in a streamed component.

[Towards the AI-native web](https://vercel.com/blog/ai-sdk-3-generative-ui#towards-the-ai-native-web)
-----------------------------------------------------------------------------------------------------

With Vercel AI SDK 3.0, we're simplifying how you integrate AI into your apps. By using React Server Components, you can now stream UI components directly from LLMs without the need for heavy client-side JavaScript. This means your apps can be more interactive and responsive, without compromising on performance.

This update makes it easier to build and maintain AI-powered features, helping you focus on creating great user experiences. We're excited to see what you ship.

[**Try the demo** Try an experimental preview of AI SDK 3.0 with Generative UI Try now](https://sdk.vercel.ai/demo)

[FAQ](https://vercel.com/blog/ai-sdk-3-generative-ui#faq)
---------------------------------------------------------

*   ### [Do I need Next.js to use this?](https://vercel.com/blog/ai-sdk-3-generative-ui#do-i-need-next.js-to-use-this?)
    
    *   The new APIs in the AI SDK 3.0 rely on React Server Components (RSC) and React Server Actions which are currently implemented in Next.js. They do not rely on any internal Next.js-specifics, so when other React frameworks like Remix or Waku complete their implementations of RSC, you'll be able to use them for Generative UI assuming they comply with React's spec.
        
*   ### [**Do React Server Components work with Next.js Pages Router?**](https://vercel.com/blog/ai-sdk-3-generative-ui#do-react-server-components-work-with-next.js-pages-router?)
    
    *   No. The new APIs rely on React Server Components and React Server Actions which are not implemented in Next.js Pages Router. However, as of Next.js 13, you can use both App Router and Pages Router in the same Next.js application.
        
*   ### [**What LLMs are currently supported?**](https://vercel.com/blog/ai-sdk-3-generative-ui#what-llms-are-currently-supported?)
    
    *   You can use the RSC APIs with any streaming LLM supported by the AI SDK. However, the [`render`](https://sdk.vercel.ai/docs/api-reference/generative-ui/render) method expects LLMs to support OpenAI's SDK and optionally its [Assistant Tools and Function Calling APIs](https://platform.openai.com/docs/guides/function-calling). We also provide lower-level streaming APIs can be used independently (even without an LLM). At the time of writing though, the new RSC-based [`render`](https://sdk.vercel.ai/docs/api-reference/generative-ui/render) API can be fully used with [OpenAI](https://platform.openai.com/docs/guides/function-calling), [Mistral](https://docs.mistral.ai/guides/function-calling), and [Fireworks](https://blog.fireworks.ai/fireworks-raises-the-quality-bar-with-function-calling-model-and-api-release-e7f49d1e98e9)' `firefunction-v1` model because of their support of the OpenAI SDK-compatible Function Calling.
        
*   ### [What if my LLM doesn't support tools or function calling?](https://vercel.com/blog/ai-sdk-3-generative-ui#what-if-my-llm-doesn't-support-tools-or-function-calling?-)
    
    *   You can still use the AI SDK 3.0 RSC APIs to stream text and your own components, or you can prompt engineer your LLM to output structured data that can be parsed and used with the AI SDK.
        
*   ### [**Does Generative UI work with OpenAI Assistants?**](https://vercel.com/blog/ai-sdk-3-generative-ui#does-generative-ui-work-with-openai-assistants?)
    
    *   You can use OpenAI Assistants as a persistence layer and function calling API with the AI SDK 3.0. Or you can manually perform the LLM calls with a provider or API of your choice.
        
*   ### [**Can anything be passed from the server to the client?**](https://vercel.com/blog/ai-sdk-3-generative-ui#can-anything-be-passed-from-the-server-to-the-client?)
    
    *   Anything serializable by React can cross the network boundary between server and client. Promises, JavaScript primitives, and certain data structures like Map and Set can all be serialized by React. You can read more about React's serialization in [the React docs.](https://react.dev/reference/react/use-server#serializable-parameters-and-return-values)
        
*   ### [**Does this work with LangChain or LlamaIndex?**](https://vercel.com/blog/ai-sdk-3-generative-ui#does-this-work-with-langchain-or-llamaindex?)
    
    *   Yes, with the [`createStreamableUI`](https://sdk.vercel.ai/docs/api-reference/generative-ui/create-streamable-ui) and [`createStreamableValue`](https://sdk.vercel.ai/docs/api-reference/generative-ui/create-streamable-value) primitives you can use any JavaScript library as long as you can call it during the execution of a React Server Action. This means you can build Generative UI products with tools like [LangChain](https://www.langchain.com/), [LlamaIndex](https://www.llamaindex.ai/), agent abstractions, and with durable task runners like [Inngest](https://inngest.com/).

## Metadata

```json
{
  "title": "Introducing AI SDK 3.0 with Generative UI support - Vercel",
  "description": "Stream React Components from LLMs to deliver richer user experiences",
  "url": "https://vercel.com/blog/ai-sdk-3-generative-ui",
  "content": "Stream React Components from LLMs to deliver richer user experiences\n\nLast October, we launched [v0.dev](http://v0.dev/), a generative UI design tool that converts text and image prompts to React UIs and streamlines the design engineering process.\n\nToday, we are open sourcing v0's [Generative UI](https://vercel.com/blog/announcing-v0-generative-ui) technology with the release of the [Vercel AI SDK 3.0](https://sdk.vercel.ai/docs). Developers can now move beyond plaintext and markdown chatbots to give LLMs rich, component-based interfaces.\n\nLet your users see more than words can say by rendering components directly within your search experience.\n\nMake it easier for your users to interpret agent execution so they can stay in the loop with the magic behind the scenes.\n\n[Visit our demo](https://sdk.vercel.ai/demo) for a first impression or [read the documentation](https://sdk.vercel.ai/docs/concepts/ai-rsc) for a preview of the new APIs.\n\n[A new user experience for AI](https://vercel.com/blog/ai-sdk-3-generative-ui#a-new-user-experience-for-ai)\n-----------------------------------------------------------------------------------------------------------\n\nProducts like ChatGPT have made a profound impact: they help users write code, plan travel, translate, summarize text, and so much more. However, LLMs have faced two important UX challenges:\n\n*   Limited or imprecise knowledge\n    \n*   Plain text / markdown-only responses\n    \n\nWith the introduction of Tools and Function Calling, developers have been able to build more robust applications that are able to fetch realtime data.\n\n![Image 18](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F3sX5pcePV8FptFPgMqhF7%2F815c20dae6b34b86ab7e40c6c8cd91e5%2FFrame_6__1_.png&w=1920&q=75)![Image 19](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F1UZL6hoRRvHALJ37uGhgJJ%2Fce8ded840e806d9efb5d10906e460044%2FFrame_6__2_.png&w=1920&q=75)\n\nThese applications, however, have been challenging to write and are still lacking in richness and interactivity.\n\nThanks to our experience in developing v0 with [React Server Components (RSC)](https://vercel.com/blog/understanding-react-server-components), we've arrived at a simple abstraction that can solve both these problems.\n\n[A new developer experience for AI](https://vercel.com/blog/ai-sdk-3-generative-ui#a-new-developer-experience-for-ai)\n---------------------------------------------------------------------------------------------------------------------\n\nWith the AI SDK 3.0, you can now associate LLM responses to streaming React Server Components.\n\nLet's start with the most basic example, streaming text without retrieval or up-to-date information.\n\n```\nimport { render } from 'ai/rsc'import OpenAI from 'openai'const openai = new OpenAI()async function submitMessage(userInput) {  'use server'  return render({    provider: openai,    model: 'gpt-4',    messages: [      { role: 'system', content: 'You are an assistant' },      { role: 'user', content: userInput }    ],    text: ({ content }) => <p>{content}</p>,  })}\n```\n\nLet's now solve both original problems: retrieve the live weather and render a custom UI. If your model supports [OpenAI-compatible Functions or Tools](https://platform.openai.com/docs/assistants/tools/function-calling), you can use the new `render` method to map specific calls to React Server Components.\n\n```\nimport { render } from 'ai/rsc'import OpenAI from 'openai'import { z } from 'zod'const openai = new OpenAI()async function submitMessage(userInput) { // 'What is the weather in SF?'  'use server'  return render({    provider: openai,    model: 'gpt-4-0125-preview',    messages: [      { role: 'system', content: 'You are a helpful assistant' },      { role: 'user', content: userInput }    ],    text: ({ content }) => <p>{content}</p>,    tools: {      get_city_weather: {        description: 'Get the current weather for a city',        parameters: z.object({          city: z.string().describe('the city')        }).required(),        render: async function* ({ city }) {          yield <Spinner/>          const weather = await getWeather(city)          return <Weather info={weather} />        }      }    }  })}\n```\n\nAn example of an assistant that renders the weather information in a streamed component.\n\n[Towards the AI-native web](https://vercel.com/blog/ai-sdk-3-generative-ui#towards-the-ai-native-web)\n-----------------------------------------------------------------------------------------------------\n\nWith Vercel AI SDK 3.0, we're simplifying how you integrate AI into your apps. By using React Server Components, you can now stream UI components directly from LLMs without the need for heavy client-side JavaScript. This means your apps can be more interactive and responsive, without compromising on performance.\n\nThis update makes it easier to build and maintain AI-powered features, helping you focus on creating great user experiences. We're excited to see what you ship.\n\n[**Try the demo** Try an experimental preview of AI SDK 3.0 with Generative UI Try now](https://sdk.vercel.ai/demo)\n\n[FAQ](https://vercel.com/blog/ai-sdk-3-generative-ui#faq)\n---------------------------------------------------------\n\n*   ### [Do I need Next.js to use this?](https://vercel.com/blog/ai-sdk-3-generative-ui#do-i-need-next.js-to-use-this?)\n    \n    *   The new APIs in the AI SDK 3.0 rely on React Server Components (RSC) and React Server Actions which are currently implemented in Next.js. They do not rely on any internal Next.js-specifics, so when other React frameworks like Remix or Waku complete their implementations of RSC, you'll be able to use them for Generative UI assuming they comply with React's spec.\n        \n*   ### [**Do React Server Components work with Next.js Pages Router?**](https://vercel.com/blog/ai-sdk-3-generative-ui#do-react-server-components-work-with-next.js-pages-router?)\n    \n    *   No. The new APIs rely on React Server Components and React Server Actions which are not implemented in Next.js Pages Router. However, as of Next.js 13, you can use both App Router and Pages Router in the same Next.js application.\n        \n*   ### [**What LLMs are currently supported?**](https://vercel.com/blog/ai-sdk-3-generative-ui#what-llms-are-currently-supported?)\n    \n    *   You can use the RSC APIs with any streaming LLM supported by the AI SDK. However, the [`render`](https://sdk.vercel.ai/docs/api-reference/generative-ui/render) method expects LLMs to support OpenAI's SDK and optionally its [Assistant Tools and Function Calling APIs](https://platform.openai.com/docs/guides/function-calling). We also provide lower-level streaming APIs can be used independently (even without an LLM). At the time of writing though, the new RSC-based [`render`](https://sdk.vercel.ai/docs/api-reference/generative-ui/render) API can be fully used with [OpenAI](https://platform.openai.com/docs/guides/function-calling), [Mistral](https://docs.mistral.ai/guides/function-calling), and [Fireworks](https://blog.fireworks.ai/fireworks-raises-the-quality-bar-with-function-calling-model-and-api-release-e7f49d1e98e9)' `firefunction-v1` model because of their support of the OpenAI SDK-compatible Function Calling.\n        \n*   ### [What if my LLM doesn't support tools or function calling?](https://vercel.com/blog/ai-sdk-3-generative-ui#what-if-my-llm-doesn't-support-tools-or-function-calling?-)\n    \n    *   You can still use the AI SDK 3.0 RSC APIs to stream text and your own components, or you can prompt engineer your LLM to output structured data that can be parsed and used with the AI SDK.\n        \n*   ### [**Does Generative UI work with OpenAI Assistants?**](https://vercel.com/blog/ai-sdk-3-generative-ui#does-generative-ui-work-with-openai-assistants?)\n    \n    *   You can use OpenAI Assistants as a persistence layer and function calling API with the AI SDK 3.0. Or you can manually perform the LLM calls with a provider or API of your choice.\n        \n*   ### [**Can anything be passed from the server to the client?**](https://vercel.com/blog/ai-sdk-3-generative-ui#can-anything-be-passed-from-the-server-to-the-client?)\n    \n    *   Anything serializable by React can cross the network boundary between server and client. Promises, JavaScript primitives, and certain data structures like Map and Set can all be serialized by React. You can read more about React's serialization in [the React docs.](https://react.dev/reference/react/use-server#serializable-parameters-and-return-values)\n        \n*   ### [**Does this work with LangChain or LlamaIndex?**](https://vercel.com/blog/ai-sdk-3-generative-ui#does-this-work-with-langchain-or-llamaindex?)\n    \n    *   Yes, with the [`createStreamableUI`](https://sdk.vercel.ai/docs/api-reference/generative-ui/create-streamable-ui) and [`createStreamableValue`](https://sdk.vercel.ai/docs/api-reference/generative-ui/create-streamable-value) primitives you can use any JavaScript library as long as you can call it during the execution of a React Server Action. This means you can build Generative UI products with tools like [LangChain](https://www.langchain.com/), [LlamaIndex](https://www.llamaindex.ai/), agent abstractions, and with durable task runners like [Inngest](https://inngest.com/).",
  "usage": {
    "tokens": 2272
  }
}
```
