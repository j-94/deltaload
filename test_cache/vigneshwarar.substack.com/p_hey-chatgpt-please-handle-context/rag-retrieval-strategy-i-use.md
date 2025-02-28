---
title: RAG: Retrieval strategy I use
description: Retrieval is one of the most important strategies in the RAG pipeline. This is the retrieval strategy we are using at EazyRAG.
url: https://vigneshwarar.substack.com/p/hey-chatgpt-please-handle-context
timestamp: 2025-01-20T15:44:46.875Z
domain: vigneshwarar.substack.com
path: p_hey-chatgpt-please-handle-context
---

# RAG: Retrieval strategy I use


Retrieval is one of the most important strategies in the RAG pipeline. This is the retrieval strategy we are using at EazyRAG.


## Content

I am currently building a product called [EazyRAG](https://eazyrag.com/). It is a dead simple API for Retrieval-Augmented Generation (RAG). In simple words, it is basically an API for ChatGPT with your own data.

In this article, I will share the retrieval strategy I use to form the final context formation at EazyRAG. Before diving into the article, there is one concept you need to understand.

LLMs such as GPT lack factual consistency and lack up-to-date knowledge. To fix this, RAG is a technique that retrieves related documents to the user's question, combines them with LLM-base prompt, and sends them to LLMs like GPT to produce more factually accurate generation.

I've written an extensive article on [building an RAG pipeline without using Langchain](https://vigneshwarar.substack.com/p/hackernews-support-page-using-retrieval). It will give you a good idea of what RAG is.

Here is what the RAG (Before) pipeline looks like.

[![Image 15](https://substackcdn.com/image/fetch/w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43112370-7b08-496c-8a65-8efe647e7b00_6412x3328.png)](https://eazyrag.com/)

Now, here is how we differ from the general RAG pipeline: we don't just retrieve chunks shove them under the base prompt, and call it a day. This approach may work for questions like 'What is the height of the Eiffel Tower?' but may not be effective all the time. Just imagine, intuitively, you have an article called 'How to make spaghetti,' and you've split the long article into pieces and indexed it. When a user queries it, you retrieve all the relevant chunks. Herein lies the problem: some general cooking instructions, such as 'boil the water and season it,' won't have a relatable relevance score to the user's search query, which, in turn, results in poor context formation and increases hallucinations.

Not only that but just shoving unstructured messy chunks will also decrease the quality of the answer.

Here is the comparison between Langchain (code taken from the [Quickstart](https://python.langchain.com/docs/use_cases/question_answering/) example) and [EazyRAG](https://eazyrag.com/).

**Langchain**

```
from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator

loader = WebBaseLoader("https://bun.sh/docs/installation")
index = VectorstoreIndexCreator().from_loaders([loader])
index.query("How do I install this on a Mac?")
```

> **Output by Langchain**
> 
> " You can install Bun on a Mac using the Homebrew package manager. Run the command 'brew tap oven-sh/bun' followed by 'brew install bun'."

**And here is the answer by EazyRAG**

[![Image 16](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa66035ea-5198-43ad-8242-2b774564bd5d_1444x1840.png)](https://eazyrag.com/)

Not to brag, but I think EazyRAG's answer is better with multiple options. But, what went wrong with Langchain is that when I dug into the final prompt, all the chunks retrieved were in a confusing format without proper spaces. Anyway, this is not a rant about Langchain; I have huge respect for that project.

**So how does [EazyRAG](https://eazyrag.com/) do it?**

When I was coding this layer, I knew that this API had to work with all types of datasets and with any type of search intent. I couldn't manually customize the context formation for every type of dataset, so why not let **GPT itself handle context formation?**

Here's how it works:

When a user queries it, we retrieve the relevant documents related to the document title and send them to GPT to classify whether we should consider feeding the entire documents for this user query. If so, which documents should we consider? Then, we feed all the documents mentioned by the GPT classifier. If the GPT classifier returns nothing, we simply shove all the chunks into base prompts and send them to LLM for answer generation. And it is working great!

In fact, this is an early version of this idea. I have a lot of ideas surrounding this concept of "**GPT itself handling context formation**" that I need to try.

So, what do you think of this idea? I'd be happy to hear your feedback and improve [EazyRAG](https://eazyrag.com/).

#### Discussion about this post

## Metadata

```json
{
  "title": "RAG: Retrieval strategy I use",
  "description": "Retrieval is one of the most important strategies in the RAG pipeline. This is the retrieval strategy we are using at EazyRAG.",
  "url": "https://vigneshwarar.substack.com/p/hey-chatgpt-please-handle-context",
  "content": "I am currently building a product called [EazyRAG](https://eazyrag.com/). It is a dead simple API for Retrieval-Augmented Generation (RAG). In simple words, it is basically an API for ChatGPT with your own data.\n\nIn this article, I will share the retrieval strategy I use to form the final context formation at EazyRAG. Before diving into the article, there is one concept you need to understand.\n\nLLMs such as GPT lack factual consistency and lack up-to-date knowledge. To fix this, RAG is a technique that retrieves related documents to the user's question, combines them with LLM-base prompt, and sends them to LLMs like GPT to produce more factually accurate generation.\n\nI've written an extensive article on [building an RAG pipeline without using Langchain](https://vigneshwarar.substack.com/p/hackernews-support-page-using-retrieval). It will give you a good idea of what RAG is.\n\nHere is what the RAG (Before) pipeline looks like.\n\n[![Image 15](https://substackcdn.com/image/fetch/w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43112370-7b08-496c-8a65-8efe647e7b00_6412x3328.png)](https://eazyrag.com/)\n\nNow, here is how we differ from the general RAG pipeline: we don't just retrieve chunks shove them under the base prompt, and call it a day. This approach may work for questions like 'What is the height of the Eiffel Tower?' but may not be effective all the time. Just imagine, intuitively, you have an article called 'How to make spaghetti,' and you've split the long article into pieces and indexed it. When a user queries it, you retrieve all the relevant chunks. Herein lies the problem: some general cooking instructions, such as 'boil the water and season it,' won't have a relatable relevance score to the user's search query, which, in turn, results in poor context formation and increases hallucinations.\n\nNot only that but just shoving unstructured messy chunks will also decrease the quality of the answer.\n\nHere is the comparison between Langchain (code taken from the [Quickstart](https://python.langchain.com/docs/use_cases/question_answering/) example) and [EazyRAG](https://eazyrag.com/).\n\n**Langchain**\n\n```\nfrom langchain.document_loaders import WebBaseLoader\nfrom langchain.indexes import VectorstoreIndexCreator\n\nloader = WebBaseLoader(\"https://bun.sh/docs/installation\")\nindex = VectorstoreIndexCreator().from_loaders([loader])\nindex.query(\"How do I install this on a Mac?\")\n```\n\n> **Output by Langchain**\n> \n> \" You can install Bun on a Mac using the Homebrew package manager. Run the command 'brew tap oven-sh/bun' followed by 'brew install bun'.\"\n\n**And here is the answer by EazyRAG**\n\n[![Image 16](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa66035ea-5198-43ad-8242-2b774564bd5d_1444x1840.png)](https://eazyrag.com/)\n\nNot to brag, but I think EazyRAG's answer is better with multiple options. But, what went wrong with Langchain is that when I dug into the final prompt, all the chunks retrieved were in a confusing format without proper spaces. Anyway, this is not a rant about Langchain; I have huge respect for that project.\n\n**So how does [EazyRAG](https://eazyrag.com/) do it?**\n\nWhen I was coding this layer, I knew that this API had to work with all types of datasets and with any type of search intent. I couldn't manually customize the context formation for every type of dataset, so why not let **GPT itself handle context formation?**\n\nHere's how it works:\n\nWhen a user queries it, we retrieve the relevant documents related to the document title and send them to GPT to classify whether we should consider feeding the entire documents for this user query. If so, which documents should we consider? Then, we feed all the documents mentioned by the GPT classifier. If the GPT classifier returns nothing, we simply shove all the chunks into base prompts and send them to LLM for answer generation. And it is working great!\n\nIn fact, this is an early version of this idea. I have a lot of ideas surrounding this concept of \"**GPT itself handling context formation**\" that I need to try.\n\nSo, what do you think of this idea? I'd be happy to hear your feedback and improve [EazyRAG](https://eazyrag.com/).\n\n#### Discussion about this post",
  "publishedTime": "2023-09-21T00:24:09+00:00",
  "usage": {
    "tokens": 1093
  }
}
```
