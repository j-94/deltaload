---
title: Introducing Query Pipelines — LlamaIndex - Build Knowledge Assistants over your Enterprise Data
description: LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.
url: https://blog.llamaindex.ai/introducing-query-pipelines-025dc2bb0537
timestamp: 2025-01-20T15:57:14.752Z
domain: blog.llamaindex.ai
path: introducing-query-pipelines-025dc2bb0537
---

# Introducing Query Pipelines — LlamaIndex - Build Knowledge Assistants over your Enterprise Data


LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.


## Content

Today we introduce **Query Pipelines,** a new declarative API within LlamaIndex that allows you to **concisely orchestrate simple-to-advanced query workflows over your data for different use cases** (RAG, structured data extraction, and more).

At the core of all this is our`QueryPipeline` abstraction. It can take in many LlamaIndex modules (LLMs, prompts, query engines, retrievers, itself). It can create a computational graph over these modules (e.g. a sequential chain or a DAG). It has callback support and native support with our [observability partners](https://docs.llamaindex.ai/en/latest/module_guides/observability/observability.html).

The end goal is that it’s even easier to build LLM workflows over your data. Check out our comprehensive [introduction guide](https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html), as well as our [docs page](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/root.html) for more details.

Example \`QueryPipeline\` setup for an advanced RAG pipeline

![Image 16](https://www.llamaindex.ai/blog/images/1*Xh4gGrK_MurM6Hou-qjszA.png)

Context
-------

Over the past year AI engineers have developed customized, complex orchestration flows with LLMs to solve a variety of different use cases. Over time some common patterns developed. At a top-level, paradigms emerged to query a user’s data — this includes RAG (in a narrow definition) to query unstructured data, and text-to-SQL to query structured data. Other paradigms emerged around use cases like structured data extraction (e.g. prompt the LLM to output JSON, and parse it), prompt chaining (e.g. chain-of-thought), and agents that could interact with external services (combine prompt chaining

**There is a lot of query orchestration in RAG.** Even within RAG itself there can be a lot of work to build an advanced RAG pipeline optimized for performance. Starting from the user query, we may want to run query understanding/transformations (re-writing, routing). We also may want to run multi-stage retrieval algorithms — e.g. top-k lookup + reranking. We may also want to use prompts + LLMs to do response synthesis in different ways. Here’s a great blog on advanced RAG [components](https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6).

[Source: “Advanced RAG Techniques: an Illustrated Overview” by Ivan Ilin](https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6)

![Image 17](https://www.llamaindex.ai/blog/images/1*pMzip79Hk1qFjNbhvw59Lw.png)

**RAG has become more modular:** Instead of a single way to do retrieval/RAG, developers are encouraged to pick and choose the best modules for their use cases. This sentiment is echoed in the [RAG Survey paper by Gao et al.](https://arxiv.org/pdf/2312.10997.pdf)

This leads to creative new patterns like [DSP](https://github.com/stanfordnlp/dspy), [Rewrite-Retrieve-Read](https://arxiv.org/abs/2305.14283), or [interleaving retrieval+generation multiple times](https://arxiv.org/abs/2305.15294).

Previous State of LlamaIndex
----------------------------

LlamaIndex itself has hundreds of RAG guides and 16+ Llama Pack recipes letting users setup [different RAG pipelines](https://www.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b), and has been at the forefront of establishing advanced RAG patterns.

We’ve also exposed low-level modules such as [LLMs](https://docs.llamaindex.ai/en/latest/module_guides/models/llms.html), [prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts.html#prompts), [embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings.html), [postprocessors](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/root.html) and easy subclassability of core components like [retrievers](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers.html) and [query engines](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine.html) so that users can define their own workflows.

But up until now, we didn’t explicitly have an orchestration abstraction. Users were responsible for figuring out their own workflows by reading the API guides of each module, converting outputs to the right inputs, and using the modules imperatively.

Query Pipeline
--------------

As a result, our QueryPipeline provides a declarative query orchestration abstraction. You can use it to compose both sequential chains and directed acyclic graphs (DAGs) of arbitrary complexity.

You can already compose these workflows imperatively with LlamaIndex modules, but the QueryPipeline allows you to do it efficiently with fewer lines of code.

It has the following benefits:

*   **Express common query workflows with fewer lines of code/boilerplate:** Stop writing converter logic between outputs/inputs, and figuring out the exact typing of arguments for each module!
*   **Greater readability:** Reduced boilerplate leads to greater readability.
*   **End-to-end observability:** Get callback integration across the entire pipeline (even for arbitrarily nested DAGs), so you stop fiddling around with our observability integrations.
*   **\[In the future\] Easy Serializability:** A declarative interface allows the core components to be serialized/redeployed on other systems much more easily.
*   **\[In the future\] Caching:** This interface also allows us to build a caching layer under the hood, allowing input re-use.

Visualization of our advanced RAG QueryPipeline using \`networkx\` and \`pyvis\`

![Image 18](https://www.llamaindex.ai/blog/images/1*sMhFv97QePYOj2G3jURhZw.png)

Usage
-----

The QueryPipeline allows you to a DAG-based query workflow using LlamaIndex modules. There are two main ways to use it:

*   As a sequential chain (easiest/most concise)
*   As a full DAG (more expressive)

See our [usage pattern guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/usage_pattern.html) for more details.

Sequential Chain
----------------

Some simple pipelines are purely linear in nature — the output of the previous module directly goes into the input of the next module.

Some examples:

*   Prompt → LLM → Output parsing
*   Retriever →Response synthesizer

Here’s the most basic example, chaining a prompt with LLM. Simply initialize `QueryPipeline` with the `chain` parameter.

\# try chaining basic prompts
prompt\_str = "Please generate related movies to {movie\_name}"
prompt\_tmpl = PromptTemplate(prompt\_str)
llm = OpenAI(model="gpt-3.5-turbo")

p = QueryPipeline(chain=\[prompt\_tmpl, llm\], verbose=True)

Setting up a DAG for an Advanced RAG Workflow
---------------------------------------------

Generally setting up a query workflow will require using our lower-level functions to build a DAG.

For instance, to build an “advanced RAG” consisting of query rewriting/retrieval/reranking/synthesis, you’d do something like the following.

from llama\_index.postprocessor import CohereRerank
from llama\_index.response\_synthesizers import TreeSummarize
from llama\_index import ServiceContext


prompt\_str = "Please generate a question about Paul Graham's life regarding the following topic {topic}"
prompt\_tmpl = PromptTemplate(prompt\_str)
llm = OpenAI(model="gpt-3.5-turbo")
retriever = index.as\_retriever(similarity\_top\_k=3)
reranker = CohereRerank()
summarizer = TreeSummarize(
    service\_context=ServiceContext.from\_defaults(llm=llm)
)


p = QueryPipeline(verbose=True)
p.add\_modules(
    {
        "llm": llm,
        "prompt\_tmpl": prompt\_tmpl,
        "retriever": retriever,
        "summarizer": summarizer,
        "reranker": reranker,
    }
)

p.add\_link("prompt\_tmpl", "llm")
p.add\_link("llm", "retriever")
p.add\_link("retriever", "reranker", dest\_key="nodes")
p.add\_link("llm", "reranker", dest\_key="query\_str")
p.add\_link("reranker", "summarizer", dest\_key="nodes")
p.add\_link("llm", "summarizer", dest\_key="query\_str")

In this code block we 1) add modules, and then 2) define relationships between modules. Note that by `source_key` and `dest_key` are **optional** and are only required if first module has more than one output / the second module has more than one input respectively.

**Running the Pipeline**
------------------------

If the pipeline has one “root” node and one output node, use `run` . Using the previous example,

output = p.run(topic="YC")
# output type is Response
type(output)

If the pipeline has multiple root nodes and/or multiple output nodes, use `run_multi` .

output\_dict = p.run\_multi({"llm": {"topic": "YC"}})
print(output\_dict)

Defining a Custom Query Component
---------------------------------

It’s super easy to subclass `CustomQueryComponent` so you can plug it into the QueryPipeline.

Check out [our walkthrough](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/usage_pattern.html#defining-a-custom-query-component) for more details.

Supported Modules
-----------------

Currently the following LlamaIndex modules are supported within a QueryPipeline. Remember, you can define your own!

1.  LLMs (both completion and chat) ( `LLM` )
2.  Prompts ( `PromptTemplate` )
3.  Query Engines ( `BaseQueryEngine` )
4.  Query Transforms ( `BaseQueryTransform` )
5.  Retrievers ( `BaseRetriever` )
6.  Output Parsers ( `BaseOutputParser` )
7.  Postprocessors/Rerankers ( `BaseNodePostprocessor`)
8.  Response Synthesizers ( `BaseSynthesizer` )
9.  Other `QueryPipeline`objects
10.  Custom components ( `CustomQueryComponent` )

Check out the [module usage guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/module_usage.html) for more details.

Walkthrough Example
-------------------

Make sure to check out our [Introduction to Query Pipelines guide](https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html) for full details. We go over all the steps above with concrete examples!

The notebook guide also logs traces through [Arize Phoenix](https://github.com/Arize-ai/phoenix). You can see the full run of each QueryPipeline in the Phoenix dashboard. Our full callback support throughout every component in a QueryComponent allows you to easily integrate with any observability provider.

![Image 19](https://www.llamaindex.ai/blog/images/1*_5dEy2YMGz8kfpJHYhQoGA.png)

Related Work
------------

The idea of a declarative syntax for building LLM-powered pipelines is not new. Related works include [Haystack](https://docs.haystack.deepset.ai/docs/pipelines) as well as the [LangChain Expression Language](https://python.langchain.com/docs/expression_language/). Other related works include pipelines that are setup in the no-code/low-code setting such as [Langflow](https://github.com/logspace-ai/langflow) / [Flowise](https://flowiseai.com/).

Our main goal here was highlighted above: provide a convenient dev UX to define common query workflows over your data. There’s a lot of optimizations/guides to be done here!

FAQ
---

**What’s the difference between a** `**QueryPipeline**` **and** `[**IngestionPipeline**](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/root.html)` **?**

Great question. Currently the IngestionPipeline operates during the data ingestion stage, and the QueryPipeline operates during the query stage. That said, there’s potentially some shared abstractions we’ll develop for both!

Conclusion + Resources
----------------------

That’s it! As mentioned above we’ll be adding a lot more resources and guides soon. In the meantime check out our current guides:

*   [Query Pipelines Guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/root.html)
*   [Query Pipelines Walkthrough](https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html)
*   [Query Pipeline Usage Pattern](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/usage_pattern.html)
*   [Query Pipelines Module Usage Guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/module_usage.html)

## Metadata

```json
{
  "title": "Introducing Query Pipelines — LlamaIndex - Build Knowledge Assistants over your Enterprise Data",
  "description": "LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.",
  "url": "https://blog.llamaindex.ai/introducing-query-pipelines-025dc2bb0537",
  "content": "Today we introduce **Query Pipelines,** a new declarative API within LlamaIndex that allows you to **concisely orchestrate simple-to-advanced query workflows over your data for different use cases** (RAG, structured data extraction, and more).\n\nAt the core of all this is our`QueryPipeline` abstraction. It can take in many LlamaIndex modules (LLMs, prompts, query engines, retrievers, itself). It can create a computational graph over these modules (e.g. a sequential chain or a DAG). It has callback support and native support with our [observability partners](https://docs.llamaindex.ai/en/latest/module_guides/observability/observability.html).\n\nThe end goal is that it’s even easier to build LLM workflows over your data. Check out our comprehensive [introduction guide](https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html), as well as our [docs page](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/root.html) for more details.\n\nExample \\`QueryPipeline\\` setup for an advanced RAG pipeline\n\n![Image 16](https://www.llamaindex.ai/blog/images/1*Xh4gGrK_MurM6Hou-qjszA.png)\n\nContext\n-------\n\nOver the past year AI engineers have developed customized, complex orchestration flows with LLMs to solve a variety of different use cases. Over time some common patterns developed. At a top-level, paradigms emerged to query a user’s data — this includes RAG (in a narrow definition) to query unstructured data, and text-to-SQL to query structured data. Other paradigms emerged around use cases like structured data extraction (e.g. prompt the LLM to output JSON, and parse it), prompt chaining (e.g. chain-of-thought), and agents that could interact with external services (combine prompt chaining\n\n**There is a lot of query orchestration in RAG.** Even within RAG itself there can be a lot of work to build an advanced RAG pipeline optimized for performance. Starting from the user query, we may want to run query understanding/transformations (re-writing, routing). We also may want to run multi-stage retrieval algorithms — e.g. top-k lookup + reranking. We may also want to use prompts + LLMs to do response synthesis in different ways. Here’s a great blog on advanced RAG [components](https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6).\n\n[Source: “Advanced RAG Techniques: an Illustrated Overview” by Ivan Ilin](https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6)\n\n![Image 17](https://www.llamaindex.ai/blog/images/1*pMzip79Hk1qFjNbhvw59Lw.png)\n\n**RAG has become more modular:** Instead of a single way to do retrieval/RAG, developers are encouraged to pick and choose the best modules for their use cases. This sentiment is echoed in the [RAG Survey paper by Gao et al.](https://arxiv.org/pdf/2312.10997.pdf)\n\nThis leads to creative new patterns like [DSP](https://github.com/stanfordnlp/dspy), [Rewrite-Retrieve-Read](https://arxiv.org/abs/2305.14283), or [interleaving retrieval+generation multiple times](https://arxiv.org/abs/2305.15294).\n\nPrevious State of LlamaIndex\n----------------------------\n\nLlamaIndex itself has hundreds of RAG guides and 16+ Llama Pack recipes letting users setup [different RAG pipelines](https://www.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b), and has been at the forefront of establishing advanced RAG patterns.\n\nWe’ve also exposed low-level modules such as [LLMs](https://docs.llamaindex.ai/en/latest/module_guides/models/llms.html), [prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts.html#prompts), [embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings.html), [postprocessors](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/root.html) and easy subclassability of core components like [retrievers](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers.html) and [query engines](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine.html) so that users can define their own workflows.\n\nBut up until now, we didn’t explicitly have an orchestration abstraction. Users were responsible for figuring out their own workflows by reading the API guides of each module, converting outputs to the right inputs, and using the modules imperatively.\n\nQuery Pipeline\n--------------\n\nAs a result, our QueryPipeline provides a declarative query orchestration abstraction. You can use it to compose both sequential chains and directed acyclic graphs (DAGs) of arbitrary complexity.\n\nYou can already compose these workflows imperatively with LlamaIndex modules, but the QueryPipeline allows you to do it efficiently with fewer lines of code.\n\nIt has the following benefits:\n\n*   **Express common query workflows with fewer lines of code/boilerplate:** Stop writing converter logic between outputs/inputs, and figuring out the exact typing of arguments for each module!\n*   **Greater readability:** Reduced boilerplate leads to greater readability.\n*   **End-to-end observability:** Get callback integration across the entire pipeline (even for arbitrarily nested DAGs), so you stop fiddling around with our observability integrations.\n*   **\\[In the future\\] Easy Serializability:** A declarative interface allows the core components to be serialized/redeployed on other systems much more easily.\n*   **\\[In the future\\] Caching:** This interface also allows us to build a caching layer under the hood, allowing input re-use.\n\nVisualization of our advanced RAG QueryPipeline using \\`networkx\\` and \\`pyvis\\`\n\n![Image 18](https://www.llamaindex.ai/blog/images/1*sMhFv97QePYOj2G3jURhZw.png)\n\nUsage\n-----\n\nThe QueryPipeline allows you to a DAG-based query workflow using LlamaIndex modules. There are two main ways to use it:\n\n*   As a sequential chain (easiest/most concise)\n*   As a full DAG (more expressive)\n\nSee our [usage pattern guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/usage_pattern.html) for more details.\n\nSequential Chain\n----------------\n\nSome simple pipelines are purely linear in nature — the output of the previous module directly goes into the input of the next module.\n\nSome examples:\n\n*   Prompt → LLM → Output parsing\n*   Retriever →Response synthesizer\n\nHere’s the most basic example, chaining a prompt with LLM. Simply initialize `QueryPipeline` with the `chain` parameter.\n\n\\# try chaining basic prompts\nprompt\\_str = \"Please generate related movies to {movie\\_name}\"\nprompt\\_tmpl = PromptTemplate(prompt\\_str)\nllm = OpenAI(model=\"gpt-3.5-turbo\")\n\np = QueryPipeline(chain=\\[prompt\\_tmpl, llm\\], verbose=True)\n\nSetting up a DAG for an Advanced RAG Workflow\n---------------------------------------------\n\nGenerally setting up a query workflow will require using our lower-level functions to build a DAG.\n\nFor instance, to build an “advanced RAG” consisting of query rewriting/retrieval/reranking/synthesis, you’d do something like the following.\n\nfrom llama\\_index.postprocessor import CohereRerank\nfrom llama\\_index.response\\_synthesizers import TreeSummarize\nfrom llama\\_index import ServiceContext\n\n\nprompt\\_str = \"Please generate a question about Paul Graham's life regarding the following topic {topic}\"\nprompt\\_tmpl = PromptTemplate(prompt\\_str)\nllm = OpenAI(model=\"gpt-3.5-turbo\")\nretriever = index.as\\_retriever(similarity\\_top\\_k=3)\nreranker = CohereRerank()\nsummarizer = TreeSummarize(\n    service\\_context=ServiceContext.from\\_defaults(llm=llm)\n)\n\n\np = QueryPipeline(verbose=True)\np.add\\_modules(\n    {\n        \"llm\": llm,\n        \"prompt\\_tmpl\": prompt\\_tmpl,\n        \"retriever\": retriever,\n        \"summarizer\": summarizer,\n        \"reranker\": reranker,\n    }\n)\n\np.add\\_link(\"prompt\\_tmpl\", \"llm\")\np.add\\_link(\"llm\", \"retriever\")\np.add\\_link(\"retriever\", \"reranker\", dest\\_key=\"nodes\")\np.add\\_link(\"llm\", \"reranker\", dest\\_key=\"query\\_str\")\np.add\\_link(\"reranker\", \"summarizer\", dest\\_key=\"nodes\")\np.add\\_link(\"llm\", \"summarizer\", dest\\_key=\"query\\_str\")\n\nIn this code block we 1) add modules, and then 2) define relationships between modules. Note that by `source_key` and `dest_key` are **optional** and are only required if first module has more than one output / the second module has more than one input respectively.\n\n**Running the Pipeline**\n------------------------\n\nIf the pipeline has one “root” node and one output node, use `run` . Using the previous example,\n\noutput = p.run(topic=\"YC\")\n# output type is Response\ntype(output)\n\nIf the pipeline has multiple root nodes and/or multiple output nodes, use `run_multi` .\n\noutput\\_dict = p.run\\_multi({\"llm\": {\"topic\": \"YC\"}})\nprint(output\\_dict)\n\nDefining a Custom Query Component\n---------------------------------\n\nIt’s super easy to subclass `CustomQueryComponent` so you can plug it into the QueryPipeline.\n\nCheck out [our walkthrough](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/usage_pattern.html#defining-a-custom-query-component) for more details.\n\nSupported Modules\n-----------------\n\nCurrently the following LlamaIndex modules are supported within a QueryPipeline. Remember, you can define your own!\n\n1.  LLMs (both completion and chat) ( `LLM` )\n2.  Prompts ( `PromptTemplate` )\n3.  Query Engines ( `BaseQueryEngine` )\n4.  Query Transforms ( `BaseQueryTransform` )\n5.  Retrievers ( `BaseRetriever` )\n6.  Output Parsers ( `BaseOutputParser` )\n7.  Postprocessors/Rerankers ( `BaseNodePostprocessor`)\n8.  Response Synthesizers ( `BaseSynthesizer` )\n9.  Other `QueryPipeline`objects\n10.  Custom components ( `CustomQueryComponent` )\n\nCheck out the [module usage guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/module_usage.html) for more details.\n\nWalkthrough Example\n-------------------\n\nMake sure to check out our [Introduction to Query Pipelines guide](https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html) for full details. We go over all the steps above with concrete examples!\n\nThe notebook guide also logs traces through [Arize Phoenix](https://github.com/Arize-ai/phoenix). You can see the full run of each QueryPipeline in the Phoenix dashboard. Our full callback support throughout every component in a QueryComponent allows you to easily integrate with any observability provider.\n\n![Image 19](https://www.llamaindex.ai/blog/images/1*_5dEy2YMGz8kfpJHYhQoGA.png)\n\nRelated Work\n------------\n\nThe idea of a declarative syntax for building LLM-powered pipelines is not new. Related works include [Haystack](https://docs.haystack.deepset.ai/docs/pipelines) as well as the [LangChain Expression Language](https://python.langchain.com/docs/expression_language/). Other related works include pipelines that are setup in the no-code/low-code setting such as [Langflow](https://github.com/logspace-ai/langflow) / [Flowise](https://flowiseai.com/).\n\nOur main goal here was highlighted above: provide a convenient dev UX to define common query workflows over your data. There’s a lot of optimizations/guides to be done here!\n\nFAQ\n---\n\n**What’s the difference between a** `**QueryPipeline**` **and** `[**IngestionPipeline**](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/root.html)` **?**\n\nGreat question. Currently the IngestionPipeline operates during the data ingestion stage, and the QueryPipeline operates during the query stage. That said, there’s potentially some shared abstractions we’ll develop for both!\n\nConclusion + Resources\n----------------------\n\nThat’s it! As mentioned above we’ll be adding a lot more resources and guides soon. In the meantime check out our current guides:\n\n*   [Query Pipelines Guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/root.html)\n*   [Query Pipelines Walkthrough](https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html)\n*   [Query Pipeline Usage Pattern](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/usage_pattern.html)\n*   [Query Pipelines Module Usage Guide](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/module_usage.html)",
  "usage": {
    "tokens": 2907
  }
}
```
