---
title: Latent Scope
description: 
url: https://enjalot.github.io/latent-scope/
timestamp: 2025-01-20T16:06:26.738Z
domain: enjalot.github.io
path: latent-scope
---

# Latent Scope



## Content

Latent Scope is an open source tool that leverages the latest in LLMs to embed, visualize, cluster and categorize your data.

It's really two tools, a **pipeline tool** to systematically process your datasets and an **exploration interface** to visualize and edit your categorized data. Latent Scope can be run fully locally using only open-source models or it can leverage several popular model providers.

![Image 5: The UI](https://enjalot.github.io/latent-scope/_file/assets/ui.b62c1a17.png)The pipeline is made up of several powerful pieces put together that work on unstructured text input:

![Image 6: The End](https://enjalot.github.io/latent-scope/_file/assets/process-crop.3880c569.png)Once you've put your data through this process you will be ready to explore and curate it in the exploration interface.

[Getting started](https://enjalot.github.io/latent-scope/#getting-started)
--------------------------------------------------------------------------

Follow the guides to get started:

1.  [Install and Configure](https://enjalot.github.io/latent-scope/install-and-config)
2.  [Your First Scope](https://enjalot.github.io/latent-scope/your-first-scope)
3.  [Explore and Curate](https://enjalot.github.io/latent-scope/explore-and-curate)
4.  [Exporting Data](https://enjalot.github.io/latent-scope/export-data)

[Example Analysis](https://enjalot.github.io/latent-scope/#example-analysis)
----------------------------------------------------------------------------

What can you do with Latent Scope? The following examples demonstrate the kinds of perspective and insights you can gain from your unstructured text data.

*   Explore free-responses from surveys in this [datavis survey analysis](https://enjalot.github.io/latent-scope/datavis-survey)
*   Cluster thousands of [GitHub issues and PRs](https://enjalot.github.io/latent-scope/plot-issues)
*   Analyze the popularity and content of [10,000 tweets](https://enjalot.github.io/latent-scope/enjalot-tweets)
*   Sort through two hundred years and 50,000 [US Federal laws](https://enjalot.github.io/latent-scope/us-federal-laws)

[Inputs and Outputs](https://enjalot.github.io/latent-scope/#inputs-and-outputs)
--------------------------------------------------------------------------------

To use Latent Scope you will need some data to input. This can be in the form of a CSV file, parquet file or a Pandas DataFrame. Currently, the focus of Latent Scope is unstructured text data, so you will need to choose a column that will be put through the process.

The process will then go through a series of steps that result in a **scope**, a data format that captures the output of the process in a handy parquet file with a JSON metadata file.

[Design Principles](https://enjalot.github.io/latent-scope/#design-principles)
------------------------------------------------------------------------------

This tool is meant to be a part of a broader data workflow, a lens that helps you see things in your data that you wouldn't otherwise have. That means it needs to be easy to get data in, and easily get useful data out.

1.  Flat files All of the data that drives the app is stored in flat files. This is so that both final and intermediate outputs can easily be exported for other uses. It also makes it easy to see the status of any part of the process.
    
2.  Remember everything This tool is intended to aid in research, the purpose is experimentation and exploration. I developed it because far too often I try a lot of things and then I forget what parameters lead me down a promising path in the first place. All choices you make in the process are recorded in metadata files along with the output of the process.
    
3.  It's all about the indices We consider an input dataset the source of truth, a list of rows that can be indexed into. So all downstream operations, whether its embeddings, pointing to nearest neighbors or assigning data points to clusters, all use indices into the input dataset.

## Metadata

```json
{
  "title": "Latent Scope",
  "description": "",
  "url": "https://enjalot.github.io/latent-scope/",
  "content": "Latent Scope is an open source tool that leverages the latest in LLMs to embed, visualize, cluster and categorize your data.\n\nIt's really two tools, a **pipeline tool** to systematically process your datasets and an **exploration interface** to visualize and edit your categorized data. Latent Scope can be run fully locally using only open-source models or it can leverage several popular model providers.\n\n![Image 5: The UI](https://enjalot.github.io/latent-scope/_file/assets/ui.b62c1a17.png)The pipeline is made up of several powerful pieces put together that work on unstructured text input:\n\n![Image 6: The End](https://enjalot.github.io/latent-scope/_file/assets/process-crop.3880c569.png)Once you've put your data through this process you will be ready to explore and curate it in the exploration interface.\n\n[Getting started](https://enjalot.github.io/latent-scope/#getting-started)\n--------------------------------------------------------------------------\n\nFollow the guides to get started:\n\n1.  [Install and Configure](https://enjalot.github.io/latent-scope/install-and-config)\n2.  [Your First Scope](https://enjalot.github.io/latent-scope/your-first-scope)\n3.  [Explore and Curate](https://enjalot.github.io/latent-scope/explore-and-curate)\n4.  [Exporting Data](https://enjalot.github.io/latent-scope/export-data)\n\n[Example Analysis](https://enjalot.github.io/latent-scope/#example-analysis)\n----------------------------------------------------------------------------\n\nWhat can you do with Latent Scope? The following examples demonstrate the kinds of perspective and insights you can gain from your unstructured text data.\n\n*   Explore free-responses from surveys in this [datavis survey analysis](https://enjalot.github.io/latent-scope/datavis-survey)\n*   Cluster thousands of [GitHub issues and PRs](https://enjalot.github.io/latent-scope/plot-issues)\n*   Analyze the popularity and content of [10,000 tweets](https://enjalot.github.io/latent-scope/enjalot-tweets)\n*   Sort through two hundred years and 50,000 [US Federal laws](https://enjalot.github.io/latent-scope/us-federal-laws)\n\n[Inputs and Outputs](https://enjalot.github.io/latent-scope/#inputs-and-outputs)\n--------------------------------------------------------------------------------\n\nTo use Latent Scope you will need some data to input. This can be in the form of a CSV file, parquet file or a Pandas DataFrame. Currently, the focus of Latent Scope is unstructured text data, so you will need to choose a column that will be put through the process.\n\nThe process will then go through a series of steps that result in a **scope**, a data format that captures the output of the process in a handy parquet file with a JSON metadata file.\n\n[Design Principles](https://enjalot.github.io/latent-scope/#design-principles)\n------------------------------------------------------------------------------\n\nThis tool is meant to be a part of a broader data workflow, a lens that helps you see things in your data that you wouldn't otherwise have. That means it needs to be easy to get data in, and easily get useful data out.\n\n1.  Flat files All of the data that drives the app is stored in flat files. This is so that both final and intermediate outputs can easily be exported for other uses. It also makes it easy to see the status of any part of the process.\n    \n2.  Remember everything This tool is intended to aid in research, the purpose is experimentation and exploration. I developed it because far too often I try a lot of things and then I forget what parameters lead me down a promising path in the first place. All choices you make in the process are recorded in metadata files along with the output of the process.\n    \n3.  It's all about the indices We consider an input dataset the source of truth, a list of rows that can be indexed into. So all downstream operations, whether its embeddings, pointing to nearest neighbors or assigning data points to clusters, all use indices into the input dataset.",
  "usage": {
    "tokens": 870
  }
}
```
