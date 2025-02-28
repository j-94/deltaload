---
title: Unifying LLM-powered QA Techniques with Routing Abstractions
description: A variety of techniques for LLM-based QA over your data have emerged: e.g. semantic search, hybrid search for fact-based lookup, retrieving entire documents for summarization tasks, and more. Each…
url: https://betterprogramming.pub/unifying-llm-powered-qa-techniques-with-routing-abstractions-438e2499a0d0
timestamp: 2025-01-20T15:49:47.695Z
domain: betterprogramming.pub
path: unifying-llm-powered-qa-techniques-with-routing-abstractions-438e2499a0d0
---

# Unifying LLM-powered QA Techniques with Routing Abstractions


A variety of techniques for LLM-based QA over your data have emerged: e.g. semantic search, hybrid search for fact-based lookup, retrieving entire documents for summarization tasks, and more. Each…


## Content

[![Image 23: Jerry Liu](https://miro.medium.com/v2/resize:fill:88:88/1*_TphgG5Y0SkBKOANEWhVYw.jpeg)](https://medium.com/@jerryjliu98?source=post_page---byline--438e2499a0d0--------------------------------)

[![Image 24: Better Programming](https://miro.medium.com/v2/resize:fill:48:48/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---byline--438e2499a0d0--------------------------------)

Summary
-------

A variety of techniques for LLM-based QA over your data have emerged: e.g. semantic search, hybrid search for fact-based lookup, retrieving entire documents for summarization tasks, and more. Each technique is typically optimized for different query use cases.

We believe “router” abstractions can help unify these techniques under a single query interface. We discuss our recently released [router implementation within LlamaIndex](https://twitter.com/jerryjliu0/status/1653789212620230658?s=20) and also describe how these router abstractions can be generalized in the future.

Current Retrieval Techniques for LLM-powered QA
-----------------------------------------------

Given a relevant context and a task in the input prompt, Large Language Models (LLMs) can effectively reason over novel information that was not observed in the training set to solve the task at hand. As a result, a popular usage mode of LLMs is to solve Question-Answering (QA) tasks over your private data. They are typically paired with a “retrieval model” to form an overall “Retrieval-Augmented Generation” (RAG) system.

These days, a variety of retrieval techniques for LLM-powered QA have emerged. One common among all these techniques is that each typically works better for certain QA use cases, and works less well for other use cases.

Here are some examples:

*   **Semantic Search (top-k)**: Retrieve the top-k chunks from the knowledge corpus by semantic similarity. This typically works better for questions that require lookup of specific facts from the corpus, e.g. “What did the author do during his time in college?”
*   **Summarization:** Retrieve all chunks from a document or set of documents. This retrieval method is typically used with queries that ask more general questions over your data, e.g. “What is a summary of this document?”
*   **Temporal Recency Weighting:** Weight retrieved texts by their recency, prioritizing more recent texts over older ones. This can be achieved for instance by a simple [decay](https://python.langchain.com/en/latest/modules/indexes/retrievers/examples/time_weighted_vectorstore.html?highlight=time-weighted) [function](https://github.com/jerryjliu/llama_index/blob/main/examples/node_postprocessor/TimeWeightedPostprocessorDemo.ipynb) or can be achieved by [reranking nodes by date](https://github.com/jerryjliu/llama_index/blob/main/examples/node_postprocessor/RecencyPostprocessorDemo.ipynb). This method is optimized for queries that require “freshness” of the data.

Different retrieval techniques are optimized for different query use cases. A natural followup question to ask: how can we try unifying all these techniques under a single query interface? That way, the user can ask a question to a single interface and get back their desired answer, instead of having to tune a specific retrieval technique.

In this article, we focus on routing as a key component in the solution to this problem.

Routing
-------

The router concept is not new; there’s a variety of [papers](https://arxiv.org/pdf/2205.00445.pdf) on this topic, and it has inherently been a part of the LLM [agent/tool](https://python.langchain.com/en/latest/modules/agents/how_to_guides.html?highlight=zero-shot+agent#agent-types) abstraction. An agent inherently needs to make a decision to pick the best tool for the current task at hand, and this involves routing.

![Image 25](https://miro.medium.com/v2/resize:fit:700/1*jNrim-8XoP5IhsSuNb-WIg.png)

Router as a decision engine for agents

Having a router can be especially powerful for enhancing Retrieval Augmented Generation (RAG), by alleviating the issue of knowing apriori what retrieval technique to use for certain queries. A router can take in a user query as input, and automatically decide which retrieval technique to use under the hood. For instance, if it detects that the query requires summarization from a set of documents, it can call a “Tool” that is specialized in summarization. If it detects that the query requires fact-based lookup, it can call a simple vector store interface to perform top-k lookup and retrieval.

Simple Router Implementation (LlamaIndex)
-----------------------------------------

A quick refresher: [as of 0.6.0](https://betterprogramming.pub/llamaindex-0-6-0-a-new-query-interface-over-your-data-331996d47e89), LlamaIndex has multiple layers of abstraction to decouple the following: Indexes, Retrievers, Response Synthesis, and Query Engines. A query engine is the top-level abstract query interface that takes in a natural language input, and can (optionally) use retrievers/response synthesis modules to return an output that the user would want.

![Image 26](https://miro.medium.com/v2/resize:fit:700/1*VdC3YuPkLBPd54KqrGCXCw.jpeg)

The base class essentially defines the following lightweight interface:

class BaseQueryEngine(ABC):  
  ...@abstractmethod  
  def query(self, str\_or\_query\_bundle: QueryType) -\> RESPONSE\_TYPE:  
    pass

We’ve now defined a `RouterQueryEngine` that can take as input a set of underlying query engines as `QueryEngineTool`objects.

Each query engine can be defined for a given use case, and use a set of indices/retrievers under the hood to solve that given use case.

\# define router query engine  
query\_engine = RouterQueryEngine(  
    selector=LLMSingleSelector.from\_defaults(),  
    query\_engine\_tools=\[  
        list\_tool,  
        vector\_tool,  
    \]  
)

For instance, relating this to the examples given in the beginning, you could have one query engine optimized for semantic search, another query engine optimized for document summarization, and a third optimized for temporal recency.

![Image 27](https://miro.medium.com/v2/resize:fit:700/1*jNrim-8XoP5IhsSuNb-WIg.png)

RouterQueryEngine abstraction in LlamaIndex

Each underlying query engine is defined as a “Tool” — this is very similar to the agent interface. At the current moment, the way the “Tool” is defined is just with a text description attached to it. The router uses the text description in deciding which underlying query engine to select to execute the query.

![Image 28](https://miro.medium.com/v2/resize:fit:700/1*li1tX22qoy_iDlJMWjoxIw.png)

A “Tool” containing Query Engine + description

Below, we show a simple sketch of how to use the Router Query Engine. We define a `list_tool` and `vector_tool` over a list index query engine and vector index query engine respectively. We then instantiate the `RouterQueryEngine` with these two tools along with a selector.

from llama\_index.query\_engine.router\_query\_engine import RouterQueryEngine  
from llama\_index.selectors.llm\_selectors import LLMSingleSelector\# get list\_query\_engine and vector\_query\_engine  
....

\# define tool over summarization/vector query engines  
list\_tool = QueryEngineTool.from\_defaults(  
    query\_engine=list\_query\_engine,  
    description='Useful for summarization questions related to Paul Graham eassy on What I Worked On.',  
)

vector\_tool = QueryEngineTool.from\_defaults(  
    query\_engine=vector\_query\_engine,  
    description='Useful for retrieving specific context from Paul Graham essay on What I Worked On.',  
)

\# define query engine  
query\_engine = RouterQueryEngine(  
    selector=LLMSingleSelector.from\_defaults(),  
    query\_engine\_tools=\[  
        list\_tool,  
        vector\_tool,  
    \]  
)

\# ask summarization question  
query\_engine.query('What is the summary of the document?')  
\# ask fact-based lookup question  
query\_engine.query('What did Paul Graham do after RISD?')

Additional Use Cases / Tutorials
--------------------------------

The router query engine can be used in a variety of downstream use cases. We highlight them below.

**Financial Analysis**

For instance, the router can be used for financial analysis of yearly SEC 10-k filings. We design a query engine that can decide whether to look within the index of a 10-k filing for a given year, or to look across different documents to compare/contrast similar sections. More concretely, the router can “route” between different vector indices or to a graph structure that can perform compare/contrast queries.

This tutorial can be found [here](https://gpt-index.readthedocs.io/en/stable/guides/tutorials/unified_query.html).

**Joint Semantic Search/Summarization**

Another basic example is to design a router that can route to either a query engine that can perform a semantic search or a query engine that can perform summarization.

![Image 29](https://miro.medium.com/v2/resize:fit:700/1*7-1UQxHPS_AZ5en_G-bNBQ.png)

An abstraction that can perform both semantic search and summarization

We package this entire system into a `QASummaryQueryEngineBuilder` class that you can deploy over any set of documents.

Take a look at the tutorial [here](https://colab.research.google.com/drive/1Asq_obABBUxTqUPTGv8yFfCDqhC-ta4u?usp=sharing).

Extension: Retrieval-Augmented Routing
--------------------------------------

As the number of query engines gets large, it makes sense to store the metadata for these query engines as part of an index as well. This allows us to hypothetically “route” a query to hundreds/thousands of query engines / data collections. We’re naming this **Retrieval-Augmented Routing (RAR)** — in a similar spirit as Retrieval-Augmented Generation, RAR uses a retrieval model to help with decision-making over large amounts of data.

![Image 30](https://miro.medium.com/v2/resize:fit:700/1*RHgxJah4SdUo8vXw-cQAMw.png)

The key idea here is that we store the entire set of “choices” for the router in some collection, and define a retriever class over that collection: a `RetrieverRouterQueryEngine` .

For instance, we can store choices in a vector index, and define a retriever over that index. This allows the router to choose between an arbitrary number of choices. Besides embedding-based lookup, you’re free to define whatever retriever class you’d like over the router choices! For instance, keyword lookup, LLM-based lookup, and more.

Here’s a code snippet of how to use the `RetrieverRouterQueryEngine` :

from llama\_index.query\_engine.router\_query\_engine import RetrieverRouterQueryEngine\# define "Node" objects corresponding to different query engines  
list\_index\_node = Node(  
    "Useful for summarization questions related to Paul Graham eassy on What I Worked On.",  
    doc\_id="list\_index"  
)  
list\_query\_engine = list\_index.as\_query\_engine(  
    response\_mode="tree\_summarize", use\_async=True  
)  
vector\_index\_node = Node(  
    "Useful for questions around the author's education, from Paul Graham essay on What I Worked On.",  
    doc\_id="vector\_index"  
)  
vector\_query\_engine = vector\_index.as\_query\_engine(  
    response\_mode="tree\_summarize", use\_async=True  
)

\# define mapping from node to query engine  
def node\_to\_query\_engine(node: Node):  
    """Convert node to query engine."""  
    # NOTE: hardcode mapping in this case  
    mapping = {  
        "list\_index": list\_query\_engine,  
        "vector\_index": vector\_query\_engine  
    }  
    return mapping\[node.get\_doc\_id()\]

\# create an outer "tool" index to store the underlying index information  
tool\_index = GPTVectorStoreIndex(\[list\_index\_node, vector\_index\_node\])  
\# get retriever  
tool\_retriever = tool\_index.as\_retriever(similarity\_top\_k=1)

\# define query engine  
query\_engine = RetrieverRouterQueryEngine(  
    tool\_retriever,  
    node\_to\_query\_engine  
)

For an interactive walkthrough, check out our [Colab notebook](https://colab.research.google.com/drive/1qBTIjPimo7kRMg8taEA3xDqDJb1QEY_1?usp=sharing). For more details, check out our [class definition](https://github.com/jerryjliu/llama_index/blob/main/llama_index/query_engine/router_query_engine.py).

Looking Ahead
-------------

The router abstraction is currently a very simple but powerful interface; it takes in a set of query engines + descriptions, and decides which query engine to use.

There are extensions to this that would make routing more sophisticated, effectively adding agent-like behaviors over your data.

*   **Non-LLM-based routing.** Routing to query engines not with LLM calls, but with other (faster?) techniques like embedding lookup.
*   **Routing to not only one query engine, but multiple query engines using a decision heuristic.** This can be implicitly supported by having each router maintain a retriever class, and use the retriever class itself (which could use an index to store state) to select the set of candidate nodes. For instance, we could use a vector index retriever to retrieve a set of candidate nodes by top-k lookup, or we can use a keyword index retriever to retrieve a set of candidate nodes by keyword matching. These nodes would then be the nodes to route to.
*   Incorporating not only automatic “selection” of a query engine, but also the **automatic determination of which parameters the query engine** should use (similar to LangChain’s [Structured Tools](https://blog.langchain.dev/structured-tools/) on the agent side).
*   **Adding multi-step reasoning capabilities.** An outer query engine could first break down a complex question into simpler ones, and query the router (which would then query other query engines) in sequential steps. LlamaIndex offers an initial version of this with the `[MultiStepQueryEngine](https://github.com/jerryjliu/llama_index/blob/main/examples/vector_indices/SimpleIndexDemo-multistep.ipynb)` [abstraction](https://github.com/jerryjliu/llama_index/blob/main/examples/vector_indices/SimpleIndexDemo-multistep.ipynb) (has relationships with Chain-of-thought Prompting).

There are also some open challenges that we’d need to address in order to make this abstraction more production-ready:

*   **Latency:** Adding any additional LLM call inherently incurs additional latency cost.
*   **Accuracy:** If the router makes a wrong decision, then the wrong query engine will be picked, and the final result will likely be wrong. We’ve empirically noticed that many models pre-GPT -4 are prone to picking the wrong decisions if the text description isn’t carefully tuned. An open question is providing recourse for the model.

At a high level, our router abstraction is just one step towards building a sophisticated query interface over your data using LLMs. We look forward to continuing iterating upon this abstraction and coming up with new ones in order to best realize this vision.

## Metadata

```json
{
  "title": "Unifying LLM-powered QA Techniques with Routing Abstractions",
  "description": "A variety of techniques for LLM-based QA over your data have emerged: e.g. semantic search, hybrid search for fact-based lookup, retrieving entire documents for summarization tasks, and more. Each…",
  "url": "https://betterprogramming.pub/unifying-llm-powered-qa-techniques-with-routing-abstractions-438e2499a0d0",
  "content": "[![Image 23: Jerry Liu](https://miro.medium.com/v2/resize:fill:88:88/1*_TphgG5Y0SkBKOANEWhVYw.jpeg)](https://medium.com/@jerryjliu98?source=post_page---byline--438e2499a0d0--------------------------------)\n\n[![Image 24: Better Programming](https://miro.medium.com/v2/resize:fill:48:48/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---byline--438e2499a0d0--------------------------------)\n\nSummary\n-------\n\nA variety of techniques for LLM-based QA over your data have emerged: e.g. semantic search, hybrid search for fact-based lookup, retrieving entire documents for summarization tasks, and more. Each technique is typically optimized for different query use cases.\n\nWe believe “router” abstractions can help unify these techniques under a single query interface. We discuss our recently released [router implementation within LlamaIndex](https://twitter.com/jerryjliu0/status/1653789212620230658?s=20) and also describe how these router abstractions can be generalized in the future.\n\nCurrent Retrieval Techniques for LLM-powered QA\n-----------------------------------------------\n\nGiven a relevant context and a task in the input prompt, Large Language Models (LLMs) can effectively reason over novel information that was not observed in the training set to solve the task at hand. As a result, a popular usage mode of LLMs is to solve Question-Answering (QA) tasks over your private data. They are typically paired with a “retrieval model” to form an overall “Retrieval-Augmented Generation” (RAG) system.\n\nThese days, a variety of retrieval techniques for LLM-powered QA have emerged. One common among all these techniques is that each typically works better for certain QA use cases, and works less well for other use cases.\n\nHere are some examples:\n\n*   **Semantic Search (top-k)**: Retrieve the top-k chunks from the knowledge corpus by semantic similarity. This typically works better for questions that require lookup of specific facts from the corpus, e.g. “What did the author do during his time in college?”\n*   **Summarization:** Retrieve all chunks from a document or set of documents. This retrieval method is typically used with queries that ask more general questions over your data, e.g. “What is a summary of this document?”\n*   **Temporal Recency Weighting:** Weight retrieved texts by their recency, prioritizing more recent texts over older ones. This can be achieved for instance by a simple [decay](https://python.langchain.com/en/latest/modules/indexes/retrievers/examples/time_weighted_vectorstore.html?highlight=time-weighted) [function](https://github.com/jerryjliu/llama_index/blob/main/examples/node_postprocessor/TimeWeightedPostprocessorDemo.ipynb) or can be achieved by [reranking nodes by date](https://github.com/jerryjliu/llama_index/blob/main/examples/node_postprocessor/RecencyPostprocessorDemo.ipynb). This method is optimized for queries that require “freshness” of the data.\n\nDifferent retrieval techniques are optimized for different query use cases. A natural followup question to ask: how can we try unifying all these techniques under a single query interface? That way, the user can ask a question to a single interface and get back their desired answer, instead of having to tune a specific retrieval technique.\n\nIn this article, we focus on routing as a key component in the solution to this problem.\n\nRouting\n-------\n\nThe router concept is not new; there’s a variety of [papers](https://arxiv.org/pdf/2205.00445.pdf) on this topic, and it has inherently been a part of the LLM [agent/tool](https://python.langchain.com/en/latest/modules/agents/how_to_guides.html?highlight=zero-shot+agent#agent-types) abstraction. An agent inherently needs to make a decision to pick the best tool for the current task at hand, and this involves routing.\n\n![Image 25](https://miro.medium.com/v2/resize:fit:700/1*jNrim-8XoP5IhsSuNb-WIg.png)\n\nRouter as a decision engine for agents\n\nHaving a router can be especially powerful for enhancing Retrieval Augmented Generation (RAG), by alleviating the issue of knowing apriori what retrieval technique to use for certain queries. A router can take in a user query as input, and automatically decide which retrieval technique to use under the hood. For instance, if it detects that the query requires summarization from a set of documents, it can call a “Tool” that is specialized in summarization. If it detects that the query requires fact-based lookup, it can call a simple vector store interface to perform top-k lookup and retrieval.\n\nSimple Router Implementation (LlamaIndex)\n-----------------------------------------\n\nA quick refresher: [as of 0.6.0](https://betterprogramming.pub/llamaindex-0-6-0-a-new-query-interface-over-your-data-331996d47e89), LlamaIndex has multiple layers of abstraction to decouple the following: Indexes, Retrievers, Response Synthesis, and Query Engines. A query engine is the top-level abstract query interface that takes in a natural language input, and can (optionally) use retrievers/response synthesis modules to return an output that the user would want.\n\n![Image 26](https://miro.medium.com/v2/resize:fit:700/1*VdC3YuPkLBPd54KqrGCXCw.jpeg)\n\nThe base class essentially defines the following lightweight interface:\n\nclass BaseQueryEngine(ABC):  \n  ...@abstractmethod  \n  def query(self, str\\_or\\_query\\_bundle: QueryType) -\\> RESPONSE\\_TYPE:  \n    pass\n\nWe’ve now defined a `RouterQueryEngine` that can take as input a set of underlying query engines as `QueryEngineTool`objects.\n\nEach query engine can be defined for a given use case, and use a set of indices/retrievers under the hood to solve that given use case.\n\n\\# define router query engine  \nquery\\_engine = RouterQueryEngine(  \n    selector=LLMSingleSelector.from\\_defaults(),  \n    query\\_engine\\_tools=\\[  \n        list\\_tool,  \n        vector\\_tool,  \n    \\]  \n)\n\nFor instance, relating this to the examples given in the beginning, you could have one query engine optimized for semantic search, another query engine optimized for document summarization, and a third optimized for temporal recency.\n\n![Image 27](https://miro.medium.com/v2/resize:fit:700/1*jNrim-8XoP5IhsSuNb-WIg.png)\n\nRouterQueryEngine abstraction in LlamaIndex\n\nEach underlying query engine is defined as a “Tool” — this is very similar to the agent interface. At the current moment, the way the “Tool” is defined is just with a text description attached to it. The router uses the text description in deciding which underlying query engine to select to execute the query.\n\n![Image 28](https://miro.medium.com/v2/resize:fit:700/1*li1tX22qoy_iDlJMWjoxIw.png)\n\nA “Tool” containing Query Engine + description\n\nBelow, we show a simple sketch of how to use the Router Query Engine. We define a `list_tool` and `vector_tool` over a list index query engine and vector index query engine respectively. We then instantiate the `RouterQueryEngine` with these two tools along with a selector.\n\nfrom llama\\_index.query\\_engine.router\\_query\\_engine import RouterQueryEngine  \nfrom llama\\_index.selectors.llm\\_selectors import LLMSingleSelector\\# get list\\_query\\_engine and vector\\_query\\_engine  \n....\n\n\\# define tool over summarization/vector query engines  \nlist\\_tool = QueryEngineTool.from\\_defaults(  \n    query\\_engine=list\\_query\\_engine,  \n    description='Useful for summarization questions related to Paul Graham eassy on What I Worked On.',  \n)\n\nvector\\_tool = QueryEngineTool.from\\_defaults(  \n    query\\_engine=vector\\_query\\_engine,  \n    description='Useful for retrieving specific context from Paul Graham essay on What I Worked On.',  \n)\n\n\\# define query engine  \nquery\\_engine = RouterQueryEngine(  \n    selector=LLMSingleSelector.from\\_defaults(),  \n    query\\_engine\\_tools=\\[  \n        list\\_tool,  \n        vector\\_tool,  \n    \\]  \n)\n\n\\# ask summarization question  \nquery\\_engine.query('What is the summary of the document?')  \n\\# ask fact-based lookup question  \nquery\\_engine.query('What did Paul Graham do after RISD?')\n\nAdditional Use Cases / Tutorials\n--------------------------------\n\nThe router query engine can be used in a variety of downstream use cases. We highlight them below.\n\n**Financial Analysis**\n\nFor instance, the router can be used for financial analysis of yearly SEC 10-k filings. We design a query engine that can decide whether to look within the index of a 10-k filing for a given year, or to look across different documents to compare/contrast similar sections. More concretely, the router can “route” between different vector indices or to a graph structure that can perform compare/contrast queries.\n\nThis tutorial can be found [here](https://gpt-index.readthedocs.io/en/stable/guides/tutorials/unified_query.html).\n\n**Joint Semantic Search/Summarization**\n\nAnother basic example is to design a router that can route to either a query engine that can perform a semantic search or a query engine that can perform summarization.\n\n![Image 29](https://miro.medium.com/v2/resize:fit:700/1*7-1UQxHPS_AZ5en_G-bNBQ.png)\n\nAn abstraction that can perform both semantic search and summarization\n\nWe package this entire system into a `QASummaryQueryEngineBuilder` class that you can deploy over any set of documents.\n\nTake a look at the tutorial [here](https://colab.research.google.com/drive/1Asq_obABBUxTqUPTGv8yFfCDqhC-ta4u?usp=sharing).\n\nExtension: Retrieval-Augmented Routing\n--------------------------------------\n\nAs the number of query engines gets large, it makes sense to store the metadata for these query engines as part of an index as well. This allows us to hypothetically “route” a query to hundreds/thousands of query engines / data collections. We’re naming this **Retrieval-Augmented Routing (RAR)** — in a similar spirit as Retrieval-Augmented Generation, RAR uses a retrieval model to help with decision-making over large amounts of data.\n\n![Image 30](https://miro.medium.com/v2/resize:fit:700/1*RHgxJah4SdUo8vXw-cQAMw.png)\n\nThe key idea here is that we store the entire set of “choices” for the router in some collection, and define a retriever class over that collection: a `RetrieverRouterQueryEngine` .\n\nFor instance, we can store choices in a vector index, and define a retriever over that index. This allows the router to choose between an arbitrary number of choices. Besides embedding-based lookup, you’re free to define whatever retriever class you’d like over the router choices! For instance, keyword lookup, LLM-based lookup, and more.\n\nHere’s a code snippet of how to use the `RetrieverRouterQueryEngine` :\n\nfrom llama\\_index.query\\_engine.router\\_query\\_engine import RetrieverRouterQueryEngine\\# define \"Node\" objects corresponding to different query engines  \nlist\\_index\\_node = Node(  \n    \"Useful for summarization questions related to Paul Graham eassy on What I Worked On.\",  \n    doc\\_id=\"list\\_index\"  \n)  \nlist\\_query\\_engine = list\\_index.as\\_query\\_engine(  \n    response\\_mode=\"tree\\_summarize\", use\\_async=True  \n)  \nvector\\_index\\_node = Node(  \n    \"Useful for questions around the author's education, from Paul Graham essay on What I Worked On.\",  \n    doc\\_id=\"vector\\_index\"  \n)  \nvector\\_query\\_engine = vector\\_index.as\\_query\\_engine(  \n    response\\_mode=\"tree\\_summarize\", use\\_async=True  \n)\n\n\\# define mapping from node to query engine  \ndef node\\_to\\_query\\_engine(node: Node):  \n    \"\"\"Convert node to query engine.\"\"\"  \n    # NOTE: hardcode mapping in this case  \n    mapping = {  \n        \"list\\_index\": list\\_query\\_engine,  \n        \"vector\\_index\": vector\\_query\\_engine  \n    }  \n    return mapping\\[node.get\\_doc\\_id()\\]\n\n\\# create an outer \"tool\" index to store the underlying index information  \ntool\\_index = GPTVectorStoreIndex(\\[list\\_index\\_node, vector\\_index\\_node\\])  \n\\# get retriever  \ntool\\_retriever = tool\\_index.as\\_retriever(similarity\\_top\\_k=1)\n\n\\# define query engine  \nquery\\_engine = RetrieverRouterQueryEngine(  \n    tool\\_retriever,  \n    node\\_to\\_query\\_engine  \n)\n\nFor an interactive walkthrough, check out our [Colab notebook](https://colab.research.google.com/drive/1qBTIjPimo7kRMg8taEA3xDqDJb1QEY_1?usp=sharing). For more details, check out our [class definition](https://github.com/jerryjliu/llama_index/blob/main/llama_index/query_engine/router_query_engine.py).\n\nLooking Ahead\n-------------\n\nThe router abstraction is currently a very simple but powerful interface; it takes in a set of query engines + descriptions, and decides which query engine to use.\n\nThere are extensions to this that would make routing more sophisticated, effectively adding agent-like behaviors over your data.\n\n*   **Non-LLM-based routing.** Routing to query engines not with LLM calls, but with other (faster?) techniques like embedding lookup.\n*   **Routing to not only one query engine, but multiple query engines using a decision heuristic.** This can be implicitly supported by having each router maintain a retriever class, and use the retriever class itself (which could use an index to store state) to select the set of candidate nodes. For instance, we could use a vector index retriever to retrieve a set of candidate nodes by top-k lookup, or we can use a keyword index retriever to retrieve a set of candidate nodes by keyword matching. These nodes would then be the nodes to route to.\n*   Incorporating not only automatic “selection” of a query engine, but also the **automatic determination of which parameters the query engine** should use (similar to LangChain’s [Structured Tools](https://blog.langchain.dev/structured-tools/) on the agent side).\n*   **Adding multi-step reasoning capabilities.** An outer query engine could first break down a complex question into simpler ones, and query the router (which would then query other query engines) in sequential steps. LlamaIndex offers an initial version of this with the `[MultiStepQueryEngine](https://github.com/jerryjliu/llama_index/blob/main/examples/vector_indices/SimpleIndexDemo-multistep.ipynb)` [abstraction](https://github.com/jerryjliu/llama_index/blob/main/examples/vector_indices/SimpleIndexDemo-multistep.ipynb) (has relationships with Chain-of-thought Prompting).\n\nThere are also some open challenges that we’d need to address in order to make this abstraction more production-ready:\n\n*   **Latency:** Adding any additional LLM call inherently incurs additional latency cost.\n*   **Accuracy:** If the router makes a wrong decision, then the wrong query engine will be picked, and the final result will likely be wrong. We’ve empirically noticed that many models pre-GPT -4 are prone to picking the wrong decisions if the text description isn’t carefully tuned. An open question is providing recourse for the model.\n\nAt a high level, our router abstraction is just one step towards building a sophisticated query interface over your data using LLMs. We look forward to continuing iterating upon this abstraction and coming up with new ones in order to best realize this vision.",
  "publishedTime": "2023-05-04T15:28:08.916Z",
  "usage": {
    "tokens": 3493
  }
}
```
