---
title: Introduction - Carbon
description: Data Connectors for LLMs.
url: https://docs.carbon.ai/introduction#getting-a-carbon-api-key
timestamp: 2025-01-20T16:01:13.107Z
domain: docs.carbon.ai
path: introduction
---

# Introduction - Carbon


Data Connectors for LLMs.


## Content

What is Carbon?
---------------

Carbon offers a comprehensive framework specifically designed to streamline the process of connecting external data sources to Large Language Models (LLMs).

Carbon significantly simplifies the process of **Retrieval Augmented Generation** (RAG), allowing you to devote more time to using your data and less time to ingesting it.

How Carbon Works
----------------

You can use our [REST API](https://docs.carbon.ai/api-reference/get-started) or [SDKs](https://docs.carbon.ai/resources/sdks) to sync user data sources and retrieve the data to use with LLMs. Carbon has native integrations with 20+ data connectors and supports more than 20+ file formats, encompassing text, audio, and visual data.

Depending on your use case and in-house infrastructure, you can retrieve user data from Carbon in several formats:

*   Original file (PDF, CSV, etc.)
*   Parsed plain text
*   Chunks and embeddings to store in your vector store
*   Semantic, keyword and hybrid search on a managed or self-hosted vector database

Products
--------

### 🔗 Connect

[Carbon Connect](https://docs.carbon.ai/carbon-connect) provides a seamless client-side UI for users to authenticate and upload content from various data sources, including Notion, Google Drive, Dropbox, OneDrive, websites, and file uploads. Once authenticated, Carbon processes the source data and automates data synchronization to keep your application up-to-date with the connected sources.

You can integrate the Connect module into your application using a React component, SDK libraries, or a magic link (coming soon).

### 🗄️ Store

Carbon offers flexible storage options. You can choose between Carbon’s managed vector database, hosted on Qdrant Cloud, or use your own custom vector store. Embeddings and chunks in the connected vector store automatically updates as users modify connected sources.

### 🔌 Universal API

Carbon’s Universal API allows you to access and manage data from any source, including documents, chunks, vectors, and other metadata. Our flexible API suite powers all functionality, including the Carbon Connect UI which makes calls to the backend.

For detailed information on available endpoints, request/response formats, and code samples, refer to our [API Reference](https://docs.carbon.ai/api-reference/get-started).

Concepts
--------

* * *

### Files

Files (along with folders) can be synced with Carbon locally or through third-party connectors. The files’ content is (optionally) processed to extract semantic information, and we also provide the original file, plain text, chunks, and embeddings.

Carbon supports various file types across text, image, video, and audio, and the [complete list of supported file types](https://docs.carbon.ai/learn/files) is available here. Files can include source-specific and custom metadata, which can later be used for retrieval filtering. You can update files, which will replace the previous version in future retrieval.

### Tags

Tags are custom metadata that can be added to files. They can be used to filter results across various endpoints, from retrieving files to deleting them. Tags are helpful for many purposes, such as managing permissions and organizing files. They can be modified without having to re-process the file. Learn more about filtering by tags [here](https://docs.carbon.ai/learn/filters/filtering).

### Connectors

To sync user data from external sources to Carbon, you can utilize connectors. For example, you can connect a Google Drive folder, and all its content will be automatically sent to Carbon and kept updated. Learn more about our data connectors [here](https://docs.carbon.ai/connectors/overview).

### Retrieval

You can choose whether Carbon should generate and store chunks and embeddings for a specific file. If you opt for this, Carbon will manage your chunks and embeddings, enabling you to perform semantic, keyword, and hybrid searches directly on your file content by entering a natural language search query. Learn more about hybrid search [here](https://docs.carbon.ai/learn/search/hybrid-search).

Setup
-----

* * *

### 🔑 Getting a Carbon API Key

Your first million characters on Carbon is free.

Sign up for a free API [here](https://portal.carbon.ai/), or book a 15-minute onboarding to get an API key [here](https://cal.com/carbon-ai/15min).

### 🔗 Helpful Links

To get started with Carbon, follow our guides:

## Metadata

```json
{
  "title": "Introduction - Carbon",
  "description": "Data Connectors for LLMs.",
  "url": "https://docs.carbon.ai/introduction#getting-a-carbon-api-key",
  "content": "What is Carbon?\n---------------\n\nCarbon offers a comprehensive framework specifically designed to streamline the process of connecting external data sources to Large Language Models (LLMs).\n\nCarbon significantly simplifies the process of **Retrieval Augmented Generation** (RAG), allowing you to devote more time to using your data and less time to ingesting it.\n\nHow Carbon Works\n----------------\n\nYou can use our [REST API](https://docs.carbon.ai/api-reference/get-started) or [SDKs](https://docs.carbon.ai/resources/sdks) to sync user data sources and retrieve the data to use with LLMs. Carbon has native integrations with 20+ data connectors and supports more than 20+ file formats, encompassing text, audio, and visual data.\n\nDepending on your use case and in-house infrastructure, you can retrieve user data from Carbon in several formats:\n\n*   Original file (PDF, CSV, etc.)\n*   Parsed plain text\n*   Chunks and embeddings to store in your vector store\n*   Semantic, keyword and hybrid search on a managed or self-hosted vector database\n\nProducts\n--------\n\n### 🔗 Connect\n\n[Carbon Connect](https://docs.carbon.ai/carbon-connect) provides a seamless client-side UI for users to authenticate and upload content from various data sources, including Notion, Google Drive, Dropbox, OneDrive, websites, and file uploads. Once authenticated, Carbon processes the source data and automates data synchronization to keep your application up-to-date with the connected sources.\n\nYou can integrate the Connect module into your application using a React component, SDK libraries, or a magic link (coming soon).\n\n### 🗄️ Store\n\nCarbon offers flexible storage options. You can choose between Carbon’s managed vector database, hosted on Qdrant Cloud, or use your own custom vector store. Embeddings and chunks in the connected vector store automatically updates as users modify connected sources.\n\n### 🔌 Universal API\n\nCarbon’s Universal API allows you to access and manage data from any source, including documents, chunks, vectors, and other metadata. Our flexible API suite powers all functionality, including the Carbon Connect UI which makes calls to the backend.\n\nFor detailed information on available endpoints, request/response formats, and code samples, refer to our [API Reference](https://docs.carbon.ai/api-reference/get-started).\n\nConcepts\n--------\n\n* * *\n\n### Files\n\nFiles (along with folders) can be synced with Carbon locally or through third-party connectors. The files’ content is (optionally) processed to extract semantic information, and we also provide the original file, plain text, chunks, and embeddings.\n\nCarbon supports various file types across text, image, video, and audio, and the [complete list of supported file types](https://docs.carbon.ai/learn/files) is available here. Files can include source-specific and custom metadata, which can later be used for retrieval filtering. You can update files, which will replace the previous version in future retrieval.\n\n### Tags\n\nTags are custom metadata that can be added to files. They can be used to filter results across various endpoints, from retrieving files to deleting them. Tags are helpful for many purposes, such as managing permissions and organizing files. They can be modified without having to re-process the file. Learn more about filtering by tags [here](https://docs.carbon.ai/learn/filters/filtering).\n\n### Connectors\n\nTo sync user data from external sources to Carbon, you can utilize connectors. For example, you can connect a Google Drive folder, and all its content will be automatically sent to Carbon and kept updated. Learn more about our data connectors [here](https://docs.carbon.ai/connectors/overview).\n\n### Retrieval\n\nYou can choose whether Carbon should generate and store chunks and embeddings for a specific file. If you opt for this, Carbon will manage your chunks and embeddings, enabling you to perform semantic, keyword, and hybrid searches directly on your file content by entering a natural language search query. Learn more about hybrid search [here](https://docs.carbon.ai/learn/search/hybrid-search).\n\nSetup\n-----\n\n* * *\n\n### 🔑 Getting a Carbon API Key\n\nYour first million characters on Carbon is free.\n\nSign up for a free API [here](https://portal.carbon.ai/), or book a 15-minute onboarding to get an API key [here](https://cal.com/carbon-ai/15min).\n\n### 🔗 Helpful Links\n\nTo get started with Carbon, follow our guides:",
  "usage": {
    "tokens": 916
  }
}
```
