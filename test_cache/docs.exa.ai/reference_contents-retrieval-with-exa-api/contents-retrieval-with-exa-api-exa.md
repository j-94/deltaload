---
title: Contents retrieval with Exa API - Exa
description: 
url: https://docs.exa.ai/reference/contents-retrieval-with-exa-api
timestamp: 2025-01-20T16:14:05.843Z
domain: docs.exa.ai
path: reference_contents-retrieval-with-exa-api
---

# Contents retrieval with Exa API - Exa



## Content

Contents retrieval with Exa API - Exa
===============
 

[Exa home page![Image 3: light logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/light.png)![Image 4: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/dark.png)](https://docs.exa.ai/)

Search or ask...

*   [Exa Search](https://exa.ai/search)
*   [API Dashboard](https://dashboard.exa.ai/login?redirect=/)
*   [API Dashboard](https://dashboard.exa.ai/login?redirect=/)

Search...

Navigation

Concepts

Contents retrieval with Exa API

[Documentation](https://docs.exa.ai/reference/getting-started)[Examples](https://docs.exa.ai/examples/demo-hallucination-detector)[Integrations](https://docs.exa.ai/integrations/python-sdk-specification)[Changelog](https://docs.exa.ai/changelog/auto-search-as-default)

*   [Discord](https://discord.com/invite/HCShtBqbfV)
*   [Blog](https://exa.ai/blog)

##### Getting Started

*   [Overview](https://docs.exa.ai/reference/getting-started)
*   [Quickstart with SDKs](https://docs.exa.ai/reference/quickstart)

##### API Reference

*   [POST Search](https://docs.exa.ai/reference/search)
*   [POST Get contents](https://docs.exa.ai/reference/get-contents)
*   [POST Find similar links](https://docs.exa.ai/reference/find-similar-links)
*   [OpenAPI Specification](https://docs.exa.ai/reference/openapi-spec)

##### RAG Quick Start Guide

*   [RAG with Exa and OpenAI](https://docs.exa.ai/reference/rag-quickstart)
*   [RAG with LangChain](https://docs.exa.ai/reference/langchain)
*   [OpenAI Exa Wrapper](https://docs.exa.ai/reference/openai)
*   [CrewAI agents with Exa](https://docs.exa.ai/reference/crewai)
*   [RAG with LlamaIndex](https://docs.exa.ai/reference/llamaindex)
*   [Tool calling with GPT](https://docs.exa.ai/reference/tool-calling-with-gpt4o)
*   [Tool calling with Claude](https://docs.exa.ai/reference/tool-calling-with-claude)

##### Concepts

*   [How Exa Search Works](https://docs.exa.ai/reference/how-exa-search-works)
*   [The Exa Index](https://docs.exa.ai/reference/the-exa-index)
*   [Prompting Guide](https://docs.exa.ai/reference/prompting-guide)
*   [Contents retrieval with Exa API](https://docs.exa.ai/reference/contents-retrieval-with-exa-api)
*   [Exa's Capabilities Explained](https://docs.exa.ai/reference/exas-capabilities-explained)
*   [FAQs](https://docs.exa.ai/reference/faqs)
*   [Crawling Subpages with Exa](https://docs.exa.ai/reference/crawling-subpages-with-exa)
*   [Exa LiveCrawl](https://docs.exa.ai/reference/should-we-use-livecrawl)

##### Admin

*   [Setting Up and Managing Your Team](https://docs.exa.ai/reference/setting-up-team)
*   [Rate Limits](https://docs.exa.ai/reference/rate-limits)
*   [Enterprise Documentation & Security](https://docs.exa.ai/reference/security)

Concepts

Contents retrieval with Exa API
===============================

* * *

When using the Exa API, you can request different types of content to be returned for each search result. The three content return types are:

[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#text-text-true)

Text (text=True):
------------------------------------------------------------------------------------------------------

Returns the full text content of the result, such as the main body of an article or webpage. This is extractive content directly taken from the source.

[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#highlights-highlights-true)

Highlights (highlights=True):
------------------------------------------------------------------------------------------------------------------------------

Delivers key excerpts from the text that are most relevant to your search query, emphasizing important information within the content. This is also extractive content from the source.

[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#summary-summary-true)

Summary (summary=True):
------------------------------------------------------------------------------------------------------------------

Provides a concise summary generated from the text, tailored to a specific query you provide. This is abstractive content created by processing the source text using Gemini Flash.

By specifying these options in your API call, you can control the depth and focus of the information returned, making your search results more actionable and relevant.

To see the full configurability of the contents returns, [check out our Dashboard](https://dashboard.exa.ai/) and sample queries.

[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#images-and-favicons)

Images and favicons
-------------------------------------------------------------------------------------------------------------

When making API requests, Exa can return:

*   Image URLs from the source content (you can specify how many images you want returned)
*   Website favicons associated with each search result (when available)

[Prompting Guide](https://docs.exa.ai/reference/prompting-guide)[Exa's Capabilities Explained](https://docs.exa.ai/reference/exas-capabilities-explained)

[x](https://twitter.com/exaailabs)[discord](https://discord.com/invite/HCShtBqbfV)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.exa.ai)

On this page

*   [Text (text=True):](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#text-text-true)
*   [Highlights (highlights=True):](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#highlights-highlights-true)
*   [Summary (summary=True):](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#summary-summary-true)
*   [Images and favicons](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#images-and-favicons)

## Metadata

```json
{
  "title": "Contents retrieval with Exa API - Exa",
  "description": "",
  "url": "https://docs.exa.ai/reference/contents-retrieval-with-exa-api",
  "content": "Contents retrieval with Exa API - Exa\n===============\n \n\n[Exa home page![Image 3: light logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/light.png)![Image 4: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/dark.png)](https://docs.exa.ai/)\n\nSearch or ask...\n\n*   [Exa Search](https://exa.ai/search)\n*   [API Dashboard](https://dashboard.exa.ai/login?redirect=/)\n*   [API Dashboard](https://dashboard.exa.ai/login?redirect=/)\n\nSearch...\n\nNavigation\n\nConcepts\n\nContents retrieval with Exa API\n\n[Documentation](https://docs.exa.ai/reference/getting-started)[Examples](https://docs.exa.ai/examples/demo-hallucination-detector)[Integrations](https://docs.exa.ai/integrations/python-sdk-specification)[Changelog](https://docs.exa.ai/changelog/auto-search-as-default)\n\n*   [Discord](https://discord.com/invite/HCShtBqbfV)\n*   [Blog](https://exa.ai/blog)\n\n##### Getting Started\n\n*   [Overview](https://docs.exa.ai/reference/getting-started)\n*   [Quickstart with SDKs](https://docs.exa.ai/reference/quickstart)\n\n##### API Reference\n\n*   [POST Search](https://docs.exa.ai/reference/search)\n*   [POST Get contents](https://docs.exa.ai/reference/get-contents)\n*   [POST Find similar links](https://docs.exa.ai/reference/find-similar-links)\n*   [OpenAPI Specification](https://docs.exa.ai/reference/openapi-spec)\n\n##### RAG Quick Start Guide\n\n*   [RAG with Exa and OpenAI](https://docs.exa.ai/reference/rag-quickstart)\n*   [RAG with LangChain](https://docs.exa.ai/reference/langchain)\n*   [OpenAI Exa Wrapper](https://docs.exa.ai/reference/openai)\n*   [CrewAI agents with Exa](https://docs.exa.ai/reference/crewai)\n*   [RAG with LlamaIndex](https://docs.exa.ai/reference/llamaindex)\n*   [Tool calling with GPT](https://docs.exa.ai/reference/tool-calling-with-gpt4o)\n*   [Tool calling with Claude](https://docs.exa.ai/reference/tool-calling-with-claude)\n\n##### Concepts\n\n*   [How Exa Search Works](https://docs.exa.ai/reference/how-exa-search-works)\n*   [The Exa Index](https://docs.exa.ai/reference/the-exa-index)\n*   [Prompting Guide](https://docs.exa.ai/reference/prompting-guide)\n*   [Contents retrieval with Exa API](https://docs.exa.ai/reference/contents-retrieval-with-exa-api)\n*   [Exa's Capabilities Explained](https://docs.exa.ai/reference/exas-capabilities-explained)\n*   [FAQs](https://docs.exa.ai/reference/faqs)\n*   [Crawling Subpages with Exa](https://docs.exa.ai/reference/crawling-subpages-with-exa)\n*   [Exa LiveCrawl](https://docs.exa.ai/reference/should-we-use-livecrawl)\n\n##### Admin\n\n*   [Setting Up and Managing Your Team](https://docs.exa.ai/reference/setting-up-team)\n*   [Rate Limits](https://docs.exa.ai/reference/rate-limits)\n*   [Enterprise Documentation & Security](https://docs.exa.ai/reference/security)\n\nConcepts\n\nContents retrieval with Exa API\n===============================\n\n* * *\n\nWhen using the Exa API, you can request different types of content to be returned for each search result. The three content return types are:\n\n[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#text-text-true)\n\nText (text=True):\n------------------------------------------------------------------------------------------------------\n\nReturns the full text content of the result, such as the main body of an article or webpage. This is extractive content directly taken from the source.\n\n[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#highlights-highlights-true)\n\nHighlights (highlights=True):\n------------------------------------------------------------------------------------------------------------------------------\n\nDelivers key excerpts from the text that are most relevant to your search query, emphasizing important information within the content. This is also extractive content from the source.\n\n[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#summary-summary-true)\n\nSummary (summary=True):\n------------------------------------------------------------------------------------------------------------------\n\nProvides a concise summary generated from the text, tailored to a specific query you provide. This is abstractive content created by processing the source text using Gemini Flash.\n\nBy specifying these options in your API call, you can control the depth and focus of the information returned, making your search results more actionable and relevant.\n\nTo see the full configurability of the contents returns, [check out our Dashboard](https://dashboard.exa.ai/) and sample queries.\n\n[​](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#images-and-favicons)\n\nImages and favicons\n-------------------------------------------------------------------------------------------------------------\n\nWhen making API requests, Exa can return:\n\n*   Image URLs from the source content (you can specify how many images you want returned)\n*   Website favicons associated with each search result (when available)\n\n[Prompting Guide](https://docs.exa.ai/reference/prompting-guide)[Exa's Capabilities Explained](https://docs.exa.ai/reference/exas-capabilities-explained)\n\n[x](https://twitter.com/exaailabs)[discord](https://discord.com/invite/HCShtBqbfV)\n\n[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.exa.ai)\n\nOn this page\n\n*   [Text (text=True):](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#text-text-true)\n*   [Highlights (highlights=True):](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#highlights-highlights-true)\n*   [Summary (summary=True):](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#summary-summary-true)\n*   [Images and favicons](https://docs.exa.ai/reference/contents-retrieval-with-exa-api#images-and-favicons)",
  "usage": {
    "tokens": 1381
  }
}
```
