---
title: Text2Cypher, the beginning of the Graph + LLM stack
description: 
url: https://siwei.io/en/llm-text-to-nebulagraph-query/
timestamp: 2025-01-20T15:45:08.912Z
domain: siwei.io
path: en_llm-text-to-nebulagraph-query
---

# Text2Cypher, the beginning of the Graph + LLM stack



## Content

Since GPT-3 began to show an unexpected “understanding ability,” we have been engaged in research, exploration, and sharing on the complementary combination of Graph + LLM technology. As of now, we had made many leading contributions to the LlamaIndex and Langchain projects. Starting from this article, we will share some of our periodic successes and methods with everyone.

The topic of this blog is what we believe to be the lowest-hanging fruit in this field: text2cypher—generating graph queries from natural language.

As the name implies, Text2Cypher is about converting natural language text into Cypher query statements. In terms of form, it is no different from another scenario that everyone might be familiar with: Text2SQL–converting text into SQL. Essentially, most knowledge graphs and graph database applications are about querying graphs according to human intentions. Our efforts in building convenient visualization tools on graph databases and wrapping useful APIs all serve this purpose.

One of the main factors that have hindered the broader application of graph databases and knowledge graphs might be the threshold for querying graph databases. So, how did we do it before the era of large language models?

The field of converting text into queries has always had such a demand even before the large language models and has always been one of the most common applications of knowledge graphs. For example, the essence of KBQA (Knowledge-Based Question Answering system) is basically text2cypher.

Taking a project I wrote earlier, [Siwi](https://siwei.io/siwi) (pronounced: /ˈsɪwi/, a Q&A application based on a dataset of basketball players) as an example, let’s look at its backend architecture:

```
┌─────────────┬───────────────────────────────────┐
│      Speech │  Frontend                         │
│  ┌──────────▼──────────┐ Siwi, /ˈsɪwi/          │
│  │ Web_Speech_API      │ A PoC of Dialog System │
│  │ Vue.JS              │ With Graph Database    │
│  │                     │ Backed Knowledge Graph │
│  └──────────┬──────────┘                        │
│             │  Sentence  Backend                │
│┌────────────┼────────────────────────────┐      │
││ ┌──────────▼──────────┐                 │      │
││ │ Web API, Flask      │ ./app/          │      │
││ └──────────┬──────────┘                 │      │
││            │  Sentence  ./bot/          │      │
││ ┌──────────▼──────────┐                 │      │
││ │ Intent Matching,    │ ./bot/classifier│      │
││ │ Symentic Processing │                 │      │
││ └──────────┬──────────┘                 │      │
││            │  Intent, Enties            │      │
││ ┌──────────▼──────────┐                 │      │
││ │ Intent Actor        │ ./bot/actions   │      │
│└─┴──────────┬──────────┴─────────────────┘      │
│             │  Graph Query                      │
│  ┌──────────▼──────────┐                        │
│  │ Graph Database      │  NebulaGraph           │
│  └─────────────────────┘                        │
└─────────────────────────────────────────────────┘
```

When a question statement is sent over, it first needs to perform intent recognition (Intent) and entity recognition (Entity). Then, using an NLP model or code, it constructs the corresponding intent and entities into query statements for the knowledge graph. Finally, it queries the graph database and constructs an answer based on the returned structure.

It can be imagined that enabling a program to:

*   Understand intent from natural language: which type of supported questions it corresponds to.
*   Identify entities: the main individuals involved in the question.
*   Construct query statements from intent and entities.

It’s not going to be an easy development task. A truly feasible implementation might consider a vast number of boundary conditions, whether in trained models or in rule codes.

In the “post-large language model” era, such “intelligent” application scenarios that previously required specialized training or rule-writing can now be accomplished with generic models combined with prompt engineering.

> Note: Prompt engineering refers to methods of accomplishing “intelligent” tasks using generation models or language models through natural language descriptions.

In fact, right after the release of GPT-3, I started using it to help me compose many highly complex Cypher query statements. I discovered that it could craft complex pattern matches and multi-step conditional statements—ones that I would have previously had to debug bit by bit and take half a day to write. Typically, with its generated solutions, I would only need to make minor adjustments. Moreover, often I could learn from its responses about Cypher syntax blind spots that I wasn’t previously aware of.

Later, in February of this year, I tried implementing a project based on GPT-3 (as GPT-3.5 was not available then): [ngql-GPT](https://ngql-gpt.siwei.io/) ([code](https://github.com/wey-gu/NebulaGraph-GPT)).

Its working principle is straightforward, identical to Text2SQL. The language model has already learned Cypher’s syntax through public domain training. When posing a task, we only need to provide the model with the graph’s Schema as context.

So, the basic prompt goes as:

```
You are a NebulaGraph Cypher expert. Based on the provided graph Schema and the question, please write the query statement.
The schema is as follows:
---
{schema}
---
The question is:
---
{question}
---
Now, write down the query statement:
```

However, real-world prompts often need additional specifications:

*   Only return the statement, no need for explanations, and no apologies.
*   Emphasize not to write node or edge types outside of the schema.

Those interested can refer to my implementation in LlamaIndex’s [KnowledgeGraph Query Engine](https://github.com/jerryjliu/llama_index/blob/71919f9dfa09e9628af8b3a59d497ad02a7a82f8/llama_index/query_engine/knowledge_graph_query_engine.py#L24).

In real-world scenarios, when we want to quickly learn and build large language model applications, we often use orchestrator tools like Langchain or LlamaIndex. These tools help us create logical abstractions, avoiding the need to implement many generic scaffolding codes from scratch:

*   Interacting with different language models.
*   Engaging with various vector databases.
*   Data segmentation.

Moreover, these orchestration tools have embedded many best practices of engineering methods. This way, we can often employ a method to utilize the latest and most user-friendly research paper techniques of large language models, such as [FLARE](https://github.com/jerryjliu/llama_index/tree/main/llama_index/query_engine/flare) and [Guidence](https://github.com/jerryjliu/llama_index/blob/main/docs/community/integrations/guidance.md).

For this purpose, I have contributed tools in both LlamaIndex and Langchain that allow for easy Text2Cypher execution on NebulaGraph, achieving Text2Cypher in just 3 lines of code.

Within LlamaIndex’s `KnowledgeQueryEngine` and LangChain’s `NebulaGraphQAChain`, we don’t need to concern ourselves with NebulaGraph’s Schema retrieval, Cypher statement generation prompts, various LLM calls, result processing, or linkage—it’s all plug-and-play!

### [](https://siwei.io/en/llm-text-to-nebulagraph-query/#using-llamaindex)4.1 Using LlamaIndex

With LlamaIndex, all we need to do is:

*   Create a `NebulaGraphStore` instance.
*   Create a `KnowledgeQueryEngine`.

Then you can start querying directly. Isn’t that super simple?

> Reference documentation: [https://gpt-index.readthedocs.io/en/latest/examples/query\_engine/knowledge\_graph\_query\_engine.html](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/knowledge_graph_query_engine.html)

```
from llama_index.query_engine import KnowledgeGraphQueryEngine
from llama_index.storage.storage_context import StorageContext
from llama_index.graph_stores import NebulaGraphStore

graph_store = NebulaGraphStore(
  space_name=space_name, edge_types=edge_types, rel_prop_names=rel_prop_names, tags=tags)
storage_context = StorageContext.from_defaults(graph_store=graph_store)

nl2kg_query_engine = KnowledgeGraphQueryEngine(
    storage_context=storage_context,
    service_context=service_context,
    llm=llm,
    verbose=True,
)
# Ask the question to query KG and answer based on the query result.
response = nl2kg_query_engine.query(
    "Tell me about Peter Quill?",
)
# Generate Query only.
graph_query = nl2kg_query_engine.generate_query(
    "Tell me about Peter Quill?",
)
```

Similarly, in Langchain, we just need to:

*   Create a `NebulaGraph` instance.
*   Create a `NebulaGraphQAChain` instance.

And you can start posing questions right away.

> Reference documentation: [https://python.langchain.com/docs/modules/chains/additional/graph\_nebula\_qa](https://python.langchain.com/docs/modules/chains/additional/graph_nebula_qa)

```
from langchain.chat_models import ChatOpenAI
from langchain.chains import NebulaGraphQAChain
from langchain.graphs import NebulaGraph

graph = NebulaGraph(
    space=space_name,
    username="root",
    password="nebula",
    address="127.0.0.1",
    port=9669,
    session_pool_size=30,
)

chain = NebulaGraphQAChain.from_llm(
    llm, graph=graph, verbose=True
)

chain.run(
    "Tell me about Peter Quill?",
)
```

The [online demo](https://siwei.io/en/demos/text2cypher/).

This demo showcases how to leverage LLM to extract knowledge triples from various information sources (using Wikipedia as an example) and store them in the NebulaGraph graph database(that’s the KG building like never as easy before).

In this demo, we first extracted information from Wikipedia about “Guardians of the Galaxy Vol. 3” and used the knowledge triples generated by the LLM to construct a knowledge graph. We then used Cypher to query the graph, and finally, with LlamaIndex and Langchain’s Text2Cypher, we implemented the function to query the graph using natural language.

You can click on other tabs to personally experience the visualization of the knowledge graph, Cypher queries, natural language queries (Text2Cypher), and other features.

Here you can [download](https://www.siwei.io/demo-dumps/kg-llm/KG_Building.ipynb) the complete Notebook.

With LLM, performing Text2Cypher on data in knowledge graphs and NebulaGraph has never been so easy.

A knowledge graph with enhanced human-machine and machine access signifies a new era. We may no longer need the high costs previously associated with implementing backend services on top of graph databases(on text2cypher implementations). Moreover, there’s no longer a need for specialized training to allow domain experts to extract essential insights from the graph.

Using the ecosystem integrations in LlamaIndex or LangChain, we can smartly apply our apps and graph data with virtually no development costs in just a few lines of code.

However, Text2Cypher is just the beginning. Please stay tuned for our subsequent articles, where we will showcase the revolutionary changes that knowledge graphs and graph databases bring to the large language model ecosystem.

> 题图 **prompt**：
> 
> _In an artful fusion of language and AI, this minimalist oil painting captures the essence of technological advancement. Delicate brushstrokes depict a harmony of binary code and flowing words, converging into a central point. With a refined color palette and clean composition, the artwork represents the symbiotic relationship between language and artificial intelligence, inviting contemplation and appreciation._

## Metadata

```json
{
  "title": "Text2Cypher, the beginning of the Graph + LLM stack",
  "description": "",
  "url": "https://siwei.io/en/llm-text-to-nebulagraph-query/",
  "content": "Since GPT-3 began to show an unexpected “understanding ability,” we have been engaged in research, exploration, and sharing on the complementary combination of Graph + LLM technology. As of now, we had made many leading contributions to the LlamaIndex and Langchain projects. Starting from this article, we will share some of our periodic successes and methods with everyone.\n\nThe topic of this blog is what we believe to be the lowest-hanging fruit in this field: text2cypher—generating graph queries from natural language.\n\nAs the name implies, Text2Cypher is about converting natural language text into Cypher query statements. In terms of form, it is no different from another scenario that everyone might be familiar with: Text2SQL–converting text into SQL. Essentially, most knowledge graphs and graph database applications are about querying graphs according to human intentions. Our efforts in building convenient visualization tools on graph databases and wrapping useful APIs all serve this purpose.\n\nOne of the main factors that have hindered the broader application of graph databases and knowledge graphs might be the threshold for querying graph databases. So, how did we do it before the era of large language models?\n\nThe field of converting text into queries has always had such a demand even before the large language models and has always been one of the most common applications of knowledge graphs. For example, the essence of KBQA (Knowledge-Based Question Answering system) is basically text2cypher.\n\nTaking a project I wrote earlier, [Siwi](https://siwei.io/siwi) (pronounced: /ˈsɪwi/, a Q&A application based on a dataset of basketball players) as an example, let’s look at its backend architecture:\n\n```\n┌─────────────┬───────────────────────────────────┐\n│      Speech │  Frontend                         │\n│  ┌──────────▼──────────┐ Siwi, /ˈsɪwi/          │\n│  │ Web_Speech_API      │ A PoC of Dialog System │\n│  │ Vue.JS              │ With Graph Database    │\n│  │                     │ Backed Knowledge Graph │\n│  └──────────┬──────────┘                        │\n│             │  Sentence  Backend                │\n│┌────────────┼────────────────────────────┐      │\n││ ┌──────────▼──────────┐                 │      │\n││ │ Web API, Flask      │ ./app/          │      │\n││ └──────────┬──────────┘                 │      │\n││            │  Sentence  ./bot/          │      │\n││ ┌──────────▼──────────┐                 │      │\n││ │ Intent Matching,    │ ./bot/classifier│      │\n││ │ Symentic Processing │                 │      │\n││ └──────────┬──────────┘                 │      │\n││            │  Intent, Enties            │      │\n││ ┌──────────▼──────────┐                 │      │\n││ │ Intent Actor        │ ./bot/actions   │      │\n│└─┴──────────┬──────────┴─────────────────┘      │\n│             │  Graph Query                      │\n│  ┌──────────▼──────────┐                        │\n│  │ Graph Database      │  NebulaGraph           │\n│  └─────────────────────┘                        │\n└─────────────────────────────────────────────────┘\n```\n\nWhen a question statement is sent over, it first needs to perform intent recognition (Intent) and entity recognition (Entity). Then, using an NLP model or code, it constructs the corresponding intent and entities into query statements for the knowledge graph. Finally, it queries the graph database and constructs an answer based on the returned structure.\n\nIt can be imagined that enabling a program to:\n\n*   Understand intent from natural language: which type of supported questions it corresponds to.\n*   Identify entities: the main individuals involved in the question.\n*   Construct query statements from intent and entities.\n\nIt’s not going to be an easy development task. A truly feasible implementation might consider a vast number of boundary conditions, whether in trained models or in rule codes.\n\nIn the “post-large language model” era, such “intelligent” application scenarios that previously required specialized training or rule-writing can now be accomplished with generic models combined with prompt engineering.\n\n> Note: Prompt engineering refers to methods of accomplishing “intelligent” tasks using generation models or language models through natural language descriptions.\n\nIn fact, right after the release of GPT-3, I started using it to help me compose many highly complex Cypher query statements. I discovered that it could craft complex pattern matches and multi-step conditional statements—ones that I would have previously had to debug bit by bit and take half a day to write. Typically, with its generated solutions, I would only need to make minor adjustments. Moreover, often I could learn from its responses about Cypher syntax blind spots that I wasn’t previously aware of.\n\nLater, in February of this year, I tried implementing a project based on GPT-3 (as GPT-3.5 was not available then): [ngql-GPT](https://ngql-gpt.siwei.io/) ([code](https://github.com/wey-gu/NebulaGraph-GPT)).\n\nIts working principle is straightforward, identical to Text2SQL. The language model has already learned Cypher’s syntax through public domain training. When posing a task, we only need to provide the model with the graph’s Schema as context.\n\nSo, the basic prompt goes as:\n\n```\nYou are a NebulaGraph Cypher expert. Based on the provided graph Schema and the question, please write the query statement.\nThe schema is as follows:\n---\n{schema}\n---\nThe question is:\n---\n{question}\n---\nNow, write down the query statement:\n```\n\nHowever, real-world prompts often need additional specifications:\n\n*   Only return the statement, no need for explanations, and no apologies.\n*   Emphasize not to write node or edge types outside of the schema.\n\nThose interested can refer to my implementation in LlamaIndex’s [KnowledgeGraph Query Engine](https://github.com/jerryjliu/llama_index/blob/71919f9dfa09e9628af8b3a59d497ad02a7a82f8/llama_index/query_engine/knowledge_graph_query_engine.py#L24).\n\nIn real-world scenarios, when we want to quickly learn and build large language model applications, we often use orchestrator tools like Langchain or LlamaIndex. These tools help us create logical abstractions, avoiding the need to implement many generic scaffolding codes from scratch:\n\n*   Interacting with different language models.\n*   Engaging with various vector databases.\n*   Data segmentation.\n\nMoreover, these orchestration tools have embedded many best practices of engineering methods. This way, we can often employ a method to utilize the latest and most user-friendly research paper techniques of large language models, such as [FLARE](https://github.com/jerryjliu/llama_index/tree/main/llama_index/query_engine/flare) and [Guidence](https://github.com/jerryjliu/llama_index/blob/main/docs/community/integrations/guidance.md).\n\nFor this purpose, I have contributed tools in both LlamaIndex and Langchain that allow for easy Text2Cypher execution on NebulaGraph, achieving Text2Cypher in just 3 lines of code.\n\nWithin LlamaIndex’s `KnowledgeQueryEngine` and LangChain’s `NebulaGraphQAChain`, we don’t need to concern ourselves with NebulaGraph’s Schema retrieval, Cypher statement generation prompts, various LLM calls, result processing, or linkage—it’s all plug-and-play!\n\n### [](https://siwei.io/en/llm-text-to-nebulagraph-query/#using-llamaindex)4.1 Using LlamaIndex\n\nWith LlamaIndex, all we need to do is:\n\n*   Create a `NebulaGraphStore` instance.\n*   Create a `KnowledgeQueryEngine`.\n\nThen you can start querying directly. Isn’t that super simple?\n\n> Reference documentation: [https://gpt-index.readthedocs.io/en/latest/examples/query\\_engine/knowledge\\_graph\\_query\\_engine.html](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/knowledge_graph_query_engine.html)\n\n```\nfrom llama_index.query_engine import KnowledgeGraphQueryEngine\nfrom llama_index.storage.storage_context import StorageContext\nfrom llama_index.graph_stores import NebulaGraphStore\n\ngraph_store = NebulaGraphStore(\n  space_name=space_name, edge_types=edge_types, rel_prop_names=rel_prop_names, tags=tags)\nstorage_context = StorageContext.from_defaults(graph_store=graph_store)\n\nnl2kg_query_engine = KnowledgeGraphQueryEngine(\n    storage_context=storage_context,\n    service_context=service_context,\n    llm=llm,\n    verbose=True,\n)\n# Ask the question to query KG and answer based on the query result.\nresponse = nl2kg_query_engine.query(\n    \"Tell me about Peter Quill?\",\n)\n# Generate Query only.\ngraph_query = nl2kg_query_engine.generate_query(\n    \"Tell me about Peter Quill?\",\n)\n```\n\nSimilarly, in Langchain, we just need to:\n\n*   Create a `NebulaGraph` instance.\n*   Create a `NebulaGraphQAChain` instance.\n\nAnd you can start posing questions right away.\n\n> Reference documentation: [https://python.langchain.com/docs/modules/chains/additional/graph\\_nebula\\_qa](https://python.langchain.com/docs/modules/chains/additional/graph_nebula_qa)\n\n```\nfrom langchain.chat_models import ChatOpenAI\nfrom langchain.chains import NebulaGraphQAChain\nfrom langchain.graphs import NebulaGraph\n\ngraph = NebulaGraph(\n    space=space_name,\n    username=\"root\",\n    password=\"nebula\",\n    address=\"127.0.0.1\",\n    port=9669,\n    session_pool_size=30,\n)\n\nchain = NebulaGraphQAChain.from_llm(\n    llm, graph=graph, verbose=True\n)\n\nchain.run(\n    \"Tell me about Peter Quill?\",\n)\n```\n\nThe [online demo](https://siwei.io/en/demos/text2cypher/).\n\nThis demo showcases how to leverage LLM to extract knowledge triples from various information sources (using Wikipedia as an example) and store them in the NebulaGraph graph database(that’s the KG building like never as easy before).\n\nIn this demo, we first extracted information from Wikipedia about “Guardians of the Galaxy Vol. 3” and used the knowledge triples generated by the LLM to construct a knowledge graph. We then used Cypher to query the graph, and finally, with LlamaIndex and Langchain’s Text2Cypher, we implemented the function to query the graph using natural language.\n\nYou can click on other tabs to personally experience the visualization of the knowledge graph, Cypher queries, natural language queries (Text2Cypher), and other features.\n\nHere you can [download](https://www.siwei.io/demo-dumps/kg-llm/KG_Building.ipynb) the complete Notebook.\n\nWith LLM, performing Text2Cypher on data in knowledge graphs and NebulaGraph has never been so easy.\n\nA knowledge graph with enhanced human-machine and machine access signifies a new era. We may no longer need the high costs previously associated with implementing backend services on top of graph databases(on text2cypher implementations). Moreover, there’s no longer a need for specialized training to allow domain experts to extract essential insights from the graph.\n\nUsing the ecosystem integrations in LlamaIndex or LangChain, we can smartly apply our apps and graph data with virtually no development costs in just a few lines of code.\n\nHowever, Text2Cypher is just the beginning. Please stay tuned for our subsequent articles, where we will showcase the revolutionary changes that knowledge graphs and graph databases bring to the large language model ecosystem.\n\n> 题图 **prompt**：\n> \n> _In an artful fusion of language and AI, this minimalist oil painting captures the essence of technological advancement. Delicate brushstrokes depict a harmony of binary code and flowing words, converging into a central point. With a refined color palette and clean composition, the artwork represents the symbiotic relationship between language and artificial intelligence, inviting contemplation and appreciation._",
  "publishedTime": "2023-07-17T20:30:04+08:00",
  "usage": {
    "tokens": 2613
  }
}
```
