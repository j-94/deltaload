---
title: Introduction | Nomic Atlas Documentation
description: Nomic Atlas is a platform for interacting with unstructured datasets of text, image, video, audio, and embeddings at scale.
url: https://docs.nomic.ai/index.html
timestamp: 2025-01-20T15:47:25.275Z
domain: docs.nomic.ai
path: index.html
---

# Introduction | Nomic Atlas Documentation


Nomic Atlas is a platform for interacting with unstructured datasets of text, image, video, audio, and embeddings at scale.


## Content

Introduction | Nomic Atlas Documentation
=============== 

[Skip to main content](https://docs.nomic.ai/index.html#__docusaurus_skipToContent_fallback)

[![Image 3: Nomic Logo](https://docs.nomic.ai/img/nomic-logo.png)![Image 4: Nomic Logo](https://docs.nomic.ai/img/nomic-logo.png)](https://docs.nomic.ai/)[Atlas Documentation](https://docs.nomic.ai/)[API Reference](https://docs.nomic.ai/reference/getting-started/)

[Nomic Atlas](https://atlas.nomic.ai/)

Search

*   [Get Started](https://docs.nomic.ai/)
    
    *   [Introduction](https://docs.nomic.ai/)
    *   [Quickstart](https://docs.nomic.ai/atlas/introduction/quick-start)
    *   [Data upload](https://docs.nomic.ai/atlas/introduction/data-upload)
*   [Capabilities](https://docs.nomic.ai/atlas/capabilities/data-interface)
    
    *   [Unstructured data interface](https://docs.nomic.ai/atlas/capabilities/data-interface)
    *   [Topic modeling](https://docs.nomic.ai/atlas/capabilities/topics)
    *   [Vector Search](https://docs.nomic.ai/atlas/capabilities/vectors)
    *   [Duplicate detection](https://docs.nomic.ai/atlas/capabilities/duplicate-detection)
    *   [Collaborative data tagging](https://docs.nomic.ai/atlas/capabilities/collaborative-tagging)
    *   [Data cleaning and improvement](https://docs.nomic.ai/atlas/capabilities/data-cleaning)
    *   [Image Datasets](https://docs.nomic.ai/atlas/capabilities/image-datasets)
    *   [Nomic Embedding Guide](https://docs.nomic.ai/atlas/capabilities/embeddings)
    *   [Programmatic Map Selections](https://docs.nomic.ai/atlas/capabilities/query)
*   [Models](https://docs.nomic.ai/atlas/models/image-embedding)
    
    *   [Image embedding](https://docs.nomic.ai/atlas/models/image-embedding)
    *   [Text embedding](https://docs.nomic.ai/atlas/models/text-embedding)
    *   [Dimensionality reduction](https://docs.nomic.ai/atlas/models/dimensionality-reduction)
*   [Cookbook](https://docs.nomic.ai/atlas/cookbook/building-image-classifiers-with-atlas)
    
    *   [Building Image Classifiers with Atlas](https://docs.nomic.ai/atlas/cookbook/building-image-classifiers-with-atlas)
    *   [Mapping GitHub Commits With Atlas](https://docs.nomic.ai/atlas/cookbook/mapping-github-commits-with-atlas)
    *   [Mapping Reddit Comments With Atlas](https://docs.nomic.ai/atlas/cookbook/mapping-reddit-comments-with-atlas)
    *   [Fast Retrieval with Resizable Embeddings](https://docs.nomic.ai/atlas/cookbook/fast-retrieval-with-resizable-embeddings)
*   [How Atlas Works](https://docs.nomic.ai/atlas/how-atlas-works/key_terms)
    
*   [Help](https://docs.nomic.ai/atlas/help/using-the-dashboard)
    
*   [Integrations](https://docs.nomic.ai/atlas/integrations)
*   [Release Notes](https://docs.nomic.ai/atlas/release-notes)

*   [](https://docs.nomic.ai/)
*   Get Started
*   Introduction

On this page

Introduction
============

Nomic Atlas is a platform for interacting with unstructured datasets of text, image, video, audio, and embeddings at scale.

New Release: Nomic Embedding Vision and API

We've launched [Nomic Embed Vision](https://docs.nomic.ai/atlas/models/image-embedding), a vision model aligned to [Nomic Embed Text](https://docs.nomic.ai/atlas/models/text-embedding)! All existing Nomic Embed Text embeddings are now multimodel; Nomic Embed Text embeddings can be used query the new Nomic Embed Vision embeddings out of the box, and visa versa. Together, Nomic Embed Text and Nomic Embed Vision project data into the only unified embedding space that achieves state of the art performance on vision, language, and multimodal tasks.

You can use it as the image embedding model powering your [AtlasDataset](https://docs.nomic.ai/atlas/capabilities/data-interface) and it is available in the [Nomic Embedding API](https://docs.nomic.ai/reference/api/embed-image-v-1-embedding-image-post).

Read more in our official [blog post](https://blog.nomic.ai/posts/nomic-embed-vision) and learn how to use it in the [API Reference](https://docs.nomic.ai/reference/api/embed-image-v-1-embedding-image-post).

Resources[​](https://docs.nomic.ai/index.html#resources "Direct link to Resources")
-----------------------------------------------------------------------------------

*   Learn how to effectively use the [Atlas unstructured data interface](https://docs.nomic.ai/atlas/capabilities/data-interface).
*   Learn about [Embeddings](https://docs.nomic.ai/atlas/capabilities/embeddings) and explore the [Nomic API Reference](https://docs.nomic.ai/reference/getting-started).
*   Get instant help on our [Discord support channel](https://discord.gg/nomic-ai-1076964370942267462).
*   Read about our [AI training policy and privacy guarantees](https://atlas.nomic.ai/legal/data-retention-policy).

Key Concepts[​](https://docs.nomic.ai/index.html#key-concepts "Direct link to Key Concepts")
--------------------------------------------------------------------------------------------

### Unstructured data[​](https://docs.nomic.ai/index.html#unstructured-data "Direct link to Unstructured data")

Nomic Atlas enables anyone to find insights in and build with unstructured data. Unstructured data is anything that you normally would not store in a spreadsheet: large collections of text documents, galleries of images, audio files, videos and the training/evaluation datasets of AI models. Nomic Atlas uses AI and Embeddings to help you quickly understand, build with and share your unstructured datasets.

### Embeddings[​](https://docs.nomic.ai/index.html#embeddings "Direct link to Embeddings")

An [embedding](https://docs.nomic.ai/atlas/capabilities/embeddings) is a vector representation of an unstructured datapoint that enables computers to manipulate the data based on semantics and meaning. All data uploaded to Nomic Atlas has a corresponding embedding assigned to it. Nomic Embedding Models are used to assign embeddings to your uploaded data if you do not specify embeddings during data upload. Embeddings are key to powering the Unstructured Data Map and organizing your data by meaning.

### Unstructured data map[​](https://docs.nomic.ai/index.html#unstructured-data-map "Direct link to Unstructured data map")

The fastest way to understand and work with unstructured data is to look at it. Anytime you upload a datapoint, Nomic Atlas organizes it in an [AI powered data interface](https://docs.nomic.ai/atlas/capabilities/data-interface) called _the map_. The map groups together similar datapoints in your dataset spatially. You can collaborate on your dataset with others by sharing a browser link to the map and developers can access its data and operations programmatically.

[Next Quickstart](https://docs.nomic.ai/atlas/introduction/quick-start)

*   [Resources](https://docs.nomic.ai/index.html#resources)
*   [Key Concepts](https://docs.nomic.ai/index.html#key-concepts)
    *   [Unstructured data](https://docs.nomic.ai/index.html#unstructured-data)
    *   [Embeddings](https://docs.nomic.ai/index.html#embeddings)
    *   [Unstructured data map](https://docs.nomic.ai/index.html#unstructured-data-map)

Docs

*   [Atlas](https://docs.nomic.ai/)

Community

*   [Discord](https://discord.gg/myY5YDR8z8)
*   [Twitter](https://twitter.com/nomic_ai?lang=en)

More

*   [Nomic AI](https://www.nomic.ai/)
*   [Blog](https://blog.nomic.ai/)
*   [GitHub](https://github.com/nomic-ai)

Copyright © 2025 Nomic AI.

## Metadata

```json
{
  "title": "Introduction | Nomic Atlas Documentation",
  "description": "Nomic Atlas is a platform for interacting with unstructured datasets of text, image, video, audio, and embeddings at scale.",
  "url": "https://docs.nomic.ai/index.html",
  "content": "Introduction | Nomic Atlas Documentation\n=============== \n\n[Skip to main content](https://docs.nomic.ai/index.html#__docusaurus_skipToContent_fallback)\n\n[![Image 3: Nomic Logo](https://docs.nomic.ai/img/nomic-logo.png)![Image 4: Nomic Logo](https://docs.nomic.ai/img/nomic-logo.png)](https://docs.nomic.ai/)[Atlas Documentation](https://docs.nomic.ai/)[API Reference](https://docs.nomic.ai/reference/getting-started/)\n\n[Nomic Atlas](https://atlas.nomic.ai/)\n\nSearch\n\n*   [Get Started](https://docs.nomic.ai/)\n    \n    *   [Introduction](https://docs.nomic.ai/)\n    *   [Quickstart](https://docs.nomic.ai/atlas/introduction/quick-start)\n    *   [Data upload](https://docs.nomic.ai/atlas/introduction/data-upload)\n*   [Capabilities](https://docs.nomic.ai/atlas/capabilities/data-interface)\n    \n    *   [Unstructured data interface](https://docs.nomic.ai/atlas/capabilities/data-interface)\n    *   [Topic modeling](https://docs.nomic.ai/atlas/capabilities/topics)\n    *   [Vector Search](https://docs.nomic.ai/atlas/capabilities/vectors)\n    *   [Duplicate detection](https://docs.nomic.ai/atlas/capabilities/duplicate-detection)\n    *   [Collaborative data tagging](https://docs.nomic.ai/atlas/capabilities/collaborative-tagging)\n    *   [Data cleaning and improvement](https://docs.nomic.ai/atlas/capabilities/data-cleaning)\n    *   [Image Datasets](https://docs.nomic.ai/atlas/capabilities/image-datasets)\n    *   [Nomic Embedding Guide](https://docs.nomic.ai/atlas/capabilities/embeddings)\n    *   [Programmatic Map Selections](https://docs.nomic.ai/atlas/capabilities/query)\n*   [Models](https://docs.nomic.ai/atlas/models/image-embedding)\n    \n    *   [Image embedding](https://docs.nomic.ai/atlas/models/image-embedding)\n    *   [Text embedding](https://docs.nomic.ai/atlas/models/text-embedding)\n    *   [Dimensionality reduction](https://docs.nomic.ai/atlas/models/dimensionality-reduction)\n*   [Cookbook](https://docs.nomic.ai/atlas/cookbook/building-image-classifiers-with-atlas)\n    \n    *   [Building Image Classifiers with Atlas](https://docs.nomic.ai/atlas/cookbook/building-image-classifiers-with-atlas)\n    *   [Mapping GitHub Commits With Atlas](https://docs.nomic.ai/atlas/cookbook/mapping-github-commits-with-atlas)\n    *   [Mapping Reddit Comments With Atlas](https://docs.nomic.ai/atlas/cookbook/mapping-reddit-comments-with-atlas)\n    *   [Fast Retrieval with Resizable Embeddings](https://docs.nomic.ai/atlas/cookbook/fast-retrieval-with-resizable-embeddings)\n*   [How Atlas Works](https://docs.nomic.ai/atlas/how-atlas-works/key_terms)\n    \n*   [Help](https://docs.nomic.ai/atlas/help/using-the-dashboard)\n    \n*   [Integrations](https://docs.nomic.ai/atlas/integrations)\n*   [Release Notes](https://docs.nomic.ai/atlas/release-notes)\n\n*   [](https://docs.nomic.ai/)\n*   Get Started\n*   Introduction\n\nOn this page\n\nIntroduction\n============\n\nNomic Atlas is a platform for interacting with unstructured datasets of text, image, video, audio, and embeddings at scale.\n\nNew Release: Nomic Embedding Vision and API\n\nWe've launched [Nomic Embed Vision](https://docs.nomic.ai/atlas/models/image-embedding), a vision model aligned to [Nomic Embed Text](https://docs.nomic.ai/atlas/models/text-embedding)! All existing Nomic Embed Text embeddings are now multimodel; Nomic Embed Text embeddings can be used query the new Nomic Embed Vision embeddings out of the box, and visa versa. Together, Nomic Embed Text and Nomic Embed Vision project data into the only unified embedding space that achieves state of the art performance on vision, language, and multimodal tasks.\n\nYou can use it as the image embedding model powering your [AtlasDataset](https://docs.nomic.ai/atlas/capabilities/data-interface) and it is available in the [Nomic Embedding API](https://docs.nomic.ai/reference/api/embed-image-v-1-embedding-image-post).\n\nRead more in our official [blog post](https://blog.nomic.ai/posts/nomic-embed-vision) and learn how to use it in the [API Reference](https://docs.nomic.ai/reference/api/embed-image-v-1-embedding-image-post).\n\nResources[​](https://docs.nomic.ai/index.html#resources \"Direct link to Resources\")\n-----------------------------------------------------------------------------------\n\n*   Learn how to effectively use the [Atlas unstructured data interface](https://docs.nomic.ai/atlas/capabilities/data-interface).\n*   Learn about [Embeddings](https://docs.nomic.ai/atlas/capabilities/embeddings) and explore the [Nomic API Reference](https://docs.nomic.ai/reference/getting-started).\n*   Get instant help on our [Discord support channel](https://discord.gg/nomic-ai-1076964370942267462).\n*   Read about our [AI training policy and privacy guarantees](https://atlas.nomic.ai/legal/data-retention-policy).\n\nKey Concepts[​](https://docs.nomic.ai/index.html#key-concepts \"Direct link to Key Concepts\")\n--------------------------------------------------------------------------------------------\n\n### Unstructured data[​](https://docs.nomic.ai/index.html#unstructured-data \"Direct link to Unstructured data\")\n\nNomic Atlas enables anyone to find insights in and build with unstructured data. Unstructured data is anything that you normally would not store in a spreadsheet: large collections of text documents, galleries of images, audio files, videos and the training/evaluation datasets of AI models. Nomic Atlas uses AI and Embeddings to help you quickly understand, build with and share your unstructured datasets.\n\n### Embeddings[​](https://docs.nomic.ai/index.html#embeddings \"Direct link to Embeddings\")\n\nAn [embedding](https://docs.nomic.ai/atlas/capabilities/embeddings) is a vector representation of an unstructured datapoint that enables computers to manipulate the data based on semantics and meaning. All data uploaded to Nomic Atlas has a corresponding embedding assigned to it. Nomic Embedding Models are used to assign embeddings to your uploaded data if you do not specify embeddings during data upload. Embeddings are key to powering the Unstructured Data Map and organizing your data by meaning.\n\n### Unstructured data map[​](https://docs.nomic.ai/index.html#unstructured-data-map \"Direct link to Unstructured data map\")\n\nThe fastest way to understand and work with unstructured data is to look at it. Anytime you upload a datapoint, Nomic Atlas organizes it in an [AI powered data interface](https://docs.nomic.ai/atlas/capabilities/data-interface) called _the map_. The map groups together similar datapoints in your dataset spatially. You can collaborate on your dataset with others by sharing a browser link to the map and developers can access its data and operations programmatically.\n\n[Next Quickstart](https://docs.nomic.ai/atlas/introduction/quick-start)\n\n*   [Resources](https://docs.nomic.ai/index.html#resources)\n*   [Key Concepts](https://docs.nomic.ai/index.html#key-concepts)\n    *   [Unstructured data](https://docs.nomic.ai/index.html#unstructured-data)\n    *   [Embeddings](https://docs.nomic.ai/index.html#embeddings)\n    *   [Unstructured data map](https://docs.nomic.ai/index.html#unstructured-data-map)\n\nDocs\n\n*   [Atlas](https://docs.nomic.ai/)\n\nCommunity\n\n*   [Discord](https://discord.gg/myY5YDR8z8)\n*   [Twitter](https://twitter.com/nomic_ai?lang=en)\n\nMore\n\n*   [Nomic AI](https://www.nomic.ai/)\n*   [Blog](https://blog.nomic.ai/)\n*   [GitHub](https://github.com/nomic-ai)\n\nCopyright © 2025 Nomic AI.",
  "usage": {
    "tokens": 1789
  }
}
```
