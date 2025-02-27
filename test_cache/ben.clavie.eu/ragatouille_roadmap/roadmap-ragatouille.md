---
title: Roadmap - RAGatouille
description: Bridging the gap between state-of-the-art Retrieval research and RAG applications.
url: https://ben.clavie.eu/ragatouille/roadmap/
timestamp: 2025-01-20T15:58:13.439Z
domain: ben.clavie.eu
path: ragatouille_roadmap
---

# Roadmap - RAGatouille


Bridging the gap between state-of-the-art Retrieval research and RAG applications.


## Content

This page is incorrectly named: RAGatouille doesn't have a set-in-stone roadmap, but rather, a set of objectives.

Below, you'll find things that we're hoping to integrate and/or support in upcoming versions (⛰️ denotes a major milestone):

#### New Features

##### Synthetic Data Generation

*   Build upon our [tutorial 3](https://github.com/bclavie/RAGatouille/blob/main/examples/03-finetuning_without_annotations_with_instructor_and_RAGatouille.ipynb) and integrate OpenAI query generation into a built-in DataProcessor.
*   Leverage [DSPy](https://github.com/stanfordnlp/dspy) to perform data augmentation via LLM compiling, reducing the reliance on API providers by enabling locally-ran models to generate data.
*   ⛰️ Integrate [UDAPDR](https://arxiv.org/abs/2303.00807) - UDAPDR is an extremely impressive method to adapt retrievers to a target domain via entirely synthetic query: all you need to provide is your document collection. We're hoping to integrate this in an upcoming version of RAGatouille.
*   Provide a toolkit to generate synthetic passages for provided queries.

#### Improvements

*   ⛰️ Full ColBERTv2 style training: transparently use an existing cross-encoder teacher model to generate distillation scores and improve model training.
*   Evaluation support: at the moment, RAGatouille doesn't roll out any evaluation metrics, as these are more commonly available already. Future versions of RAGatouille will include some form of evaluation for convenience!
*   Support for more "late-interaction" models, such as Google's [SparseEmbed](https://research.google/pubs/sparseembed-learning-sparse-lexical-representations-with-contextual-embeddings-for-retrieval/).
*   New negative miners, such as ColBERTMiner (not a huge priority as dense hard negative work well enough, but would be a nice feature for thoroughness)
*   Full LlamaIndex integration

#### Library Upkeep

*   ⛰️ Improve the documentation to cover every component and concept of the library in-depth.
*   Comprehensive test coverage

## Metadata

```json
{
  "title": "Roadmap - RAGatouille",
  "description": "Bridging the gap between state-of-the-art Retrieval research and RAG applications.",
  "url": "https://ben.clavie.eu/ragatouille/roadmap/",
  "content": "This page is incorrectly named: RAGatouille doesn't have a set-in-stone roadmap, but rather, a set of objectives.\n\nBelow, you'll find things that we're hoping to integrate and/or support in upcoming versions (⛰️ denotes a major milestone):\n\n#### New Features\n\n##### Synthetic Data Generation\n\n*   Build upon our [tutorial 3](https://github.com/bclavie/RAGatouille/blob/main/examples/03-finetuning_without_annotations_with_instructor_and_RAGatouille.ipynb) and integrate OpenAI query generation into a built-in DataProcessor.\n*   Leverage [DSPy](https://github.com/stanfordnlp/dspy) to perform data augmentation via LLM compiling, reducing the reliance on API providers by enabling locally-ran models to generate data.\n*   ⛰️ Integrate [UDAPDR](https://arxiv.org/abs/2303.00807) - UDAPDR is an extremely impressive method to adapt retrievers to a target domain via entirely synthetic query: all you need to provide is your document collection. We're hoping to integrate this in an upcoming version of RAGatouille.\n*   Provide a toolkit to generate synthetic passages for provided queries.\n\n#### Improvements\n\n*   ⛰️ Full ColBERTv2 style training: transparently use an existing cross-encoder teacher model to generate distillation scores and improve model training.\n*   Evaluation support: at the moment, RAGatouille doesn't roll out any evaluation metrics, as these are more commonly available already. Future versions of RAGatouille will include some form of evaluation for convenience!\n*   Support for more \"late-interaction\" models, such as Google's [SparseEmbed](https://research.google/pubs/sparseembed-learning-sparse-lexical-representations-with-contextual-embeddings-for-retrieval/).\n*   New negative miners, such as ColBERTMiner (not a huge priority as dense hard negative work well enough, but would be a nice feature for thoroughness)\n*   Full LlamaIndex integration\n\n#### Library Upkeep\n\n*   ⛰️ Improve the documentation to cover every component and concept of the library in-depth.\n*   Comprehensive test coverage",
  "usage": {
    "tokens": 466
  }
}
```
