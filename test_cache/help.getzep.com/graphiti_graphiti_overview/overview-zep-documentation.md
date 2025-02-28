---
title: Overview — Zep Documentation
description: Temporal Knowledge Graphs for Agentic Applications
url: https://help.getzep.com/graphiti/graphiti/overview
timestamp: 2025-01-20T16:11:24.769Z
domain: help.getzep.com
path: graphiti_graphiti_overview
---

# Overview — Zep Documentation


Temporal Knowledge Graphs for Agentic Applications


## Content

![Image 7: graphiti intro slides](https://files.buildwithfern.com/zep.docs.buildwithfern.com/2025-01-17T15:52:16.723Z/images/graphiti-graph-intro.gif)

Graphiti builds dynamic, temporally-aware knowledge graphs that represent complex, evolving relationships between entities over time. It ingests both unstructured and structured data, and the resulting graph may be queried using a fusion of time, full-text, semantic, and graph algorithm approaches.

With Graphiti, you can build LLM applications such as:

*   Assistants that learn from user interactions, fusing personal knowledge with dynamic data from business systems like CRMs and billing platforms.
*   Agents that autonomously execute complex tasks, reasoning with state changes from multiple dynamic sources.

Graphiti supports a wide range of applications in sales, customer service, health, finance, and more, enabling long-term recall and state-based reasoning for both assistants and agents.

Graphiti and Zep Memory
-----------------------

Graphiti powers the core of [Zep’s memory layer](https://www.getzep.com/) for LLM-powered Assistants and Agents.

We’re excited to open-source Graphiti, believing its potential reaches far beyond memory applications.

Why Graphiti?
-------------

We were intrigued by Microsoft’s GraphRAG, which expanded on RAG text chunking by using a graph to better model a document corpus and making this representation available via semantic and graph search techniques. However, GraphRAG did not address our core problem: It’s primarily designed for static documents and doesn’t inherently handle temporal aspects of data.

Graphiti is designed from the ground up to handle constantly changing information, hybrid semantic and graph search, and scale:

*   **Temporal Awareness:** Tracks changes in facts and relationships over time, enabling point-in-time queries. Graph edges include temporal metadata to record relationship lifecycles.
*   **Episodic Processing:** Ingests data as discrete episodes, maintaining data provenance and allowing incremental entity and relationship extraction.
*   **Hybrid Search:** Combines semantic and BM25 full-text search, with the ability to rerank results by distance from a central node e.g. “Kendra”.
*   **Scalable:** Designed for processing large datasets, with parallelization of LLM calls for bulk processing while preserving the chronology of events.
*   **Supports Varied Sources:** Can ingest both unstructured text and structured JSON data.

![Image 8: graphiti demo slides](https://files.buildwithfern.com/zep.docs.buildwithfern.com/2025-01-17T15:52:16.723Z/images/graphiti-intro-slides-stock-2.gif)

## Metadata

```json
{
  "title": "Overview — Zep Documentation",
  "description": "Temporal Knowledge Graphs for Agentic Applications",
  "url": "https://help.getzep.com/graphiti/graphiti/overview",
  "content": "![Image 7: graphiti intro slides](https://files.buildwithfern.com/zep.docs.buildwithfern.com/2025-01-17T15:52:16.723Z/images/graphiti-graph-intro.gif)\n\nGraphiti builds dynamic, temporally-aware knowledge graphs that represent complex, evolving relationships between entities over time. It ingests both unstructured and structured data, and the resulting graph may be queried using a fusion of time, full-text, semantic, and graph algorithm approaches.\n\nWith Graphiti, you can build LLM applications such as:\n\n*   Assistants that learn from user interactions, fusing personal knowledge with dynamic data from business systems like CRMs and billing platforms.\n*   Agents that autonomously execute complex tasks, reasoning with state changes from multiple dynamic sources.\n\nGraphiti supports a wide range of applications in sales, customer service, health, finance, and more, enabling long-term recall and state-based reasoning for both assistants and agents.\n\nGraphiti and Zep Memory\n-----------------------\n\nGraphiti powers the core of [Zep’s memory layer](https://www.getzep.com/) for LLM-powered Assistants and Agents.\n\nWe’re excited to open-source Graphiti, believing its potential reaches far beyond memory applications.\n\nWhy Graphiti?\n-------------\n\nWe were intrigued by Microsoft’s GraphRAG, which expanded on RAG text chunking by using a graph to better model a document corpus and making this representation available via semantic and graph search techniques. However, GraphRAG did not address our core problem: It’s primarily designed for static documents and doesn’t inherently handle temporal aspects of data.\n\nGraphiti is designed from the ground up to handle constantly changing information, hybrid semantic and graph search, and scale:\n\n*   **Temporal Awareness:** Tracks changes in facts and relationships over time, enabling point-in-time queries. Graph edges include temporal metadata to record relationship lifecycles.\n*   **Episodic Processing:** Ingests data as discrete episodes, maintaining data provenance and allowing incremental entity and relationship extraction.\n*   **Hybrid Search:** Combines semantic and BM25 full-text search, with the ability to rerank results by distance from a central node e.g. “Kendra”.\n*   **Scalable:** Designed for processing large datasets, with parallelization of LLM calls for bulk processing while preserving the chronology of events.\n*   **Supports Varied Sources:** Can ingest both unstructured text and structured JSON data.\n\n![Image 8: graphiti demo slides](https://files.buildwithfern.com/zep.docs.buildwithfern.com/2025-01-17T15:52:16.723Z/images/graphiti-intro-slides-stock-2.gif)",
  "usage": {
    "tokens": 553
  }
}
```
