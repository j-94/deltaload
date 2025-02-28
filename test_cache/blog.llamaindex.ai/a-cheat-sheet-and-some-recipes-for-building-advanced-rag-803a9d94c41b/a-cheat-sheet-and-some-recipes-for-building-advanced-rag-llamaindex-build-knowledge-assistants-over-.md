---
title: A Cheat Sheet and Some Recipes For Building Advanced RAG — LlamaIndex - Build Knowledge Assistants over your Enterprise Data
description: LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.
url: https://blog.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b
timestamp: 2025-01-20T15:53:25.527Z
domain: blog.llamaindex.ai
path: a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b
---

# A Cheat Sheet and Some Recipes For Building Advanced RAG — LlamaIndex - Build Knowledge Assistants over your Enterprise Data


LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.


## Content

![Image 9](https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2F6cfb645c4e5dfea8f3e5a590c3d2bc1cbfcfead3-5818x7805.png%3Ffit%3Dmax%26auto%3Dformat&w=1920&q=75)• 2024-01-05

*   [Retrieval Augmented](https://www.llamaindex.ai/blog/tag/retrieval-augmented)
*   [LLM](https://www.llamaindex.ai/blog/tag/llm)
*   [Retrieval Generation](https://www.llamaindex.ai/blog/tag/retrieval-generation)
*   [AI](https://www.llamaindex.ai/blog/tag/ai)

It’s the start of a new year and perhaps you’re looking to break into the RAG scene by building your very first RAG system. Or, maybe you’ve built Basic RAG systems and are now looking to enhance them to something more advanced in order to better handle your user’s queries and data structures.

In either case, knowing where or how to begin may be a challenge in and of itself! If that’s true, then hopefully this blog post points you in the right direction for your next steps, and moreover, provides for you a mental model for you to anchor your decisions when building advanced RAG systems.

The RAG cheat sheet shared above was greatly inspired by a recent RAG survey paper ([“Retrieval-Augmented Generation for Large Language Models: A Survey” Gao, Yunfan, et al. 2023](https://arxiv.org/pdf/2312.10997.pdf)).

Basic RAG
---------

Mainstream RAG as defined today involves retrieving documents from an external knowledge database and passing these along with the user’s query to an LLM for response generation. In other words, RAG involves a Retrieval component, an External Knowledge database and a Generation component.

**LlamaIndex Basic RAG Recipe:**

from llama\_index import SimpleDirectoryReader, VectorStoreIndex


documents = SimpleDirectoryReader(input\_dir="...").load\_data()



index = VectorStoreIndex.from\_documents(documents=documents)



query\_engine = index.as\_query\_engine()


response = query\_engine.query("A user's query")

Success Requirements for RAG
----------------------------

In order for a RAG system to be deemed as a success (in the sense of providing useful and relevant answers to user questions), there are really only two high level requirements:

1.  Retrieval must be able to find the most relevant documents to a user query.
2.  Generation must be able to make good use of the retrieved documents to sufficiently answer the user query.

Advanced RAG
------------

With the success requirements defined, we can then say that building advanced RAG is really about the application of more sophisticated techniques and strategies (to the Retrieval or Generation components) to ensure that they are ultimately met. Furthermore, we can categorize a sophisticated technique as either one that addresses one of the two high-level success requirements independent (more or less) of the other, or one that addresses both of these requirements simultaneously.

Advanced techniques for Retrieval must be able to find the most relevant documents to a user query
--------------------------------------------------------------------------------------------------

Below we briefly describe a couple of the more sophisticated techniques to help achieve the first success requirement.

1.  **Chunk-Size Optimization:** Since LLMs are restricted by context length, it is necessary to chunk documents when building the External Knowledge database. Chunks that are too big or too small can pose problems for the Generation component leading to in accurate responses.

**LlamaIndex Chunk Size Optimization Recipe** ([notebook guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/param_optimizer/param_optimizer.ipynb))**:**

from llama\_index import ServiceContext
from llama\_index.param\_tuner.base import ParamTuner, RunResult
from llama\_index.evaluation import SemanticSimilarityEvaluator, BatchEvalRunner

def objective\_function(params\_dict):
    chunk\_size = params\_dict\["chunk\_size"\]
    docs = params\_dict\["docs"\]
    top\_k = params\_dict\["top\_k"\]
    eval\_qs = params\_dict\["eval\_qs"\]
    ref\_response\_strs = params\_dict\["ref\_response\_strs"\]

    
    index = \_build\_index(chunk\_size, docs)  
    query\_engine = index.as\_query\_engine(similarity\_top\_k=top\_k)
  
    
    pred\_response\_objs = get\_responses(
        eval\_qs, query\_engine, show\_progress=True
    )

    
    
    evaluator = SemanticSimilarityEvaluator(...)
    eval\_batch\_runner = BatchEvalRunner(
        {"semantic\_similarity": evaluator}, workers=2, show\_progress=True
    )
    eval\_results = eval\_batch\_runner.evaluate\_responses(
        eval\_qs, responses=pred\_response\_objs, reference=ref\_response\_strs
    )

    
    mean\_score = np.array(
        \[r.score for r in eval\_results\["semantic\_similarity"\]\]
    ).mean()

    return RunResult(score=mean\_score, params=params\_dict)


param\_dict = {"chunk\_size": \[256, 512, 1024\]} 
fixed\_param\_dict = { 
  "top\_k": 2,
    "docs": docs,
    "eval\_qs": eval\_qs\[:10\],
    "ref\_response\_strs": ref\_response\_strs\[:10\],
}
param\_tuner = ParamTuner(
    param\_fn=objective\_function,
    param\_dict=param\_dict,
    fixed\_param\_dict=fixed\_param\_dict,
    show\_progress=True,
)


results = param\_tuner.tune()
best\_result = results.best\_run\_result
best\_chunk\_size = results.best\_run\_result.params\["chunk\_size"\]

**2\. Structured External Knowledge:** In complex scenarios, it may be necessary to build your external knowledge with a bit more structure than the basic vector index so as to permit recursive retrievals or routed retrieval when dealing with sensibly separated external knowledge sources.

**LlamaIndex Recursive Retrieval Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes.html))**:**

from llama\_index import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.node\_parser import SentenceSplitter
from llama\_index.schema import IndexNode






documents = SimpleDirectoryReader(
  input\_file="some\_data\_path/llama2.pdf"
).load\_data()


node\_parser = SentenceSplitter(chunk\_size=1024)
base\_nodes = node\_parser.get\_nodes\_from\_documents(documents)


sub\_chunk\_sizes = \[256, 512\]
sub\_node\_parsers = \[
    SentenceSplitter(chunk\_size=c, chunk\_overlap=20) for c in sub\_chunk\_sizes
\]
all\_nodes = \[\]
for base\_node in base\_nodes:
    for n in sub\_node\_parsers:
        sub\_nodes = n.get\_nodes\_from\_documents(\[base\_node\])
        sub\_inodes = \[
            IndexNode.from\_text\_node(sn, base\_node.node\_id) for sn in sub\_nodes
        \]
        all\_nodes.extend(sub\_inodes)
    
    original\_node = IndexNode.from\_text\_node(base\_node, base\_node.node\_id)
    all\_nodes.append(original\_node)


vector\_index\_chunk = VectorStoreIndex(
    all\_nodes, service\_context=service\_context
)
vector\_retriever\_chunk = vector\_index\_chunk.as\_retriever(similarity\_top\_k=2)


all\_nodes\_dict = {n.node\_id: n for n in all\_nodes}
retriever\_chunk = RecursiveRetriever(
    "vector",
    retriever\_dict={"vector": vector\_retriever\_chunk},
    node\_dict=all\_nodes\_dict,
    verbose=True,
)


query\_engine\_chunk = RetrieverQueryEngine.from\_args(
    retriever\_chunk, service\_context=service\_context
)


response = query\_engine\_chunk.query(
    "Can you tell me about the key concepts for safety finetuning"
)

**Other useful links**

We have several of guides demonstrating the application of other advanced techniques to help ensure accurate retrieval in complex cases. Here are links to a select few of them:

1.  [Building External Knowledge using Knowledge Graphs](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine.html)
2.  [Performing Mixed Retrieval with Auto Retrievers](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever.html)
3.  [Building Fusion Retrievers](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion.html)
4.  [Fine-tuning Embedding Models used in Retrieval](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding.html)
5.  [Transforming Query Embeddings (HyDE)](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo.html)

Advanced techniques for Generation must be able to make good use of the retrieved documents
-------------------------------------------------------------------------------------------

Similar to previous section, we provide a couple of examples of the sophisticated techniques under this category, which can be described as ensuring that the retrieved documents are well aligned to the LLM of the Generator.

1.  **Information Compression:** Not only are LLMs are restricted by context length, but there can be response degradation if the retrieved documents carry too much noise (i.e. irrelevant information).

**LlamaIndex Information Compression Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongLLMLingua.html))**:**

from llama\_index import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.query\_engine import RetrieverQueryEngine
from llama\_index.postprocessor import LongLLMLinguaPostprocessor






node\_postprocessor = LongLLMLinguaPostprocessor(
    instruction\_str="Given the context, please answer the final question",
    target\_token=300,
    rank\_method="longllmlingua",
    additional\_compress\_kwargs={
        "condition\_compare": True,
        "condition\_in\_question": "after",
        "context\_budget": "+100",
        "reorder\_context": "sort",  
    },
)


documents = SimpleDirectoryReader(input\_dir="...").load\_data()
index = VectorStoreIndex.from\_documents(documents)


retriever = index.as\_retriever(similarity\_top\_k=2)
retriever\_query\_engine = RetrieverQueryEngine.from\_args(
    retriever, node\_postprocessors=\[node\_postprocessor\]
)


response = retriever\_query\_engine.query("A user query")

**2\. Result Re-Rank:** LLMs suffer from the so-called “Lost in the Middle” phenomena which stipulates that LLMs focus on the extreme ends of the prompts. In light of this, it is beneficial to re-rank retrieved documents before passing them off to the Generation component.

**LlamaIndex Re-Ranking For Better Generation Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank.html))**:**

import os
from llama\_index import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.postprocessor.cohere\_rerank import CohereRerank
from llama\_index.postprocessor import LongLLMLinguaPostprocessor






api\_key = os.environ\["COHERE\_API\_KEY"\]
cohere\_rerank = CohereRerank(api\_key=api\_key, top\_n=2)


documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()
index = VectorStoreIndex.from\_documents(documents=documents)
query\_engine = index.as\_query\_engine(
    similarity\_top\_k=10,
    node\_postprocessors=\[cohere\_rerank\],
)


response = query\_engine.query(
    "What did Sam Altman do in this essay?"
)

Advanced techniques for simultaneously addressing Retrieval and Generation success requirements
-----------------------------------------------------------------------------------------------

In this sub section, we consider sophisticated methods that use the synergy of retrieval and generation in order to achieve both better retrieval as well as more accurate generated responses to user queries).

1.  **Generator-Enhanced Retrieval:** These techniques make use of the LLM’s inherent reasoning abilities to refine the user query before retrieval is performed so as to better indicate what exactly it requires to provide a useful response.

**LlamaIndex Generator-Enhanced Retrieval Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine.html))**:**

from llama\_index.llms import OpenAI
from llama\_index.query\_engine import FLAREInstructQueryEngine
from llama\_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
)






documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()
index = VectorStoreIndex.from\_documents(documents)
index\_query\_engine = index.as\_query\_engine(similarity\_top\_k=2)
service\_context = ServiceContext.from\_defaults(llm=OpenAI(model="gpt-4"))
flare\_query\_engine = FLAREInstructQueryEngine(
    query\_engine=index\_query\_engine,
    service\_context=service\_context,
    max\_iterations=7,
    verbose=True,
)


response = flare\_query\_engine.query(
    "Can you tell me about the author's trajectory in the startup world?"
)

**2\. Iterative Retrieval-Generator RAG:** For some complex cases, multi-step reasoning may be required to provide a useful and relevant answer to the user query.

**LlamaIndex Iterative Retrieval-Generator Recipe (**[notebook guide](https://docs.llamaindex.ai/en/stable/examples/evaluation/RetryQuery.html#retry-query-engine)**):**

from llama\_index.query\_engine import RetryQueryEngine
from llama\_index.evaluation import RelevancyEvaluator







documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()
index = VectorStoreIndex.from\_documents(documents)
base\_query\_engine = index.as\_query\_engine()
query\_response\_evaluator = RelevancyEvaluator() 
                                                
retry\_query\_engine = RetryQueryEngine(
    base\_query\_engine, query\_response\_evaluator
)


retry\_response = retry\_query\_engine.query("A user query")

Measurement Aspects of RAG
--------------------------

Evaluating RAG systems are, of course, of utmost importance. In their survey paper, Gao, Yunfan et al. indicate 7 measurement aspects as seen in the top-right portion of the attached RAG cheat sheet. The llama-index library consists of several evaluation abstractions as well as integrations to RAGAs in order to help builders gain an understanding of the level to which their RAG system achieves the success requirements through the lens of these measurement aspects. Below, we list a select few of the evaluation notebook guides.

1.  [Answer Relevancy and Context Relevancy](https://docs.llamaindex.ai/en/latest/examples/evaluation/answer_and_context_relevancy.html)
2.  [Faithfulness](https://www.notion.so/LlamaIndex-Platform-0754edd9af1c4159bde12649c184c8ef?pvs=21)
3.  [Retrieval Evaluation](https://github.com/run-llama/llama_index/blob/main/docs/examples/evaluation/retrieval/retriever_eval.ipynb)
4.  [Batch Evaluations with BatchEvalRunner](https://docs.llamaindex.ai/en/stable/examples/evaluation/batch_eval.html)

You’re Now Equipped To Do Advanced RAG
--------------------------------------

After reading this blog post, we hope that you feel more equipped and confident to apply some of these sophisticated techniques for building Advanced RAG systems!

## Metadata

```json
{
  "title": "A Cheat Sheet and Some Recipes For Building Advanced RAG — LlamaIndex - Build Knowledge Assistants over your Enterprise Data",
  "description": "LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.",
  "url": "https://blog.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b",
  "content": "![Image 9](https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2F6cfb645c4e5dfea8f3e5a590c3d2bc1cbfcfead3-5818x7805.png%3Ffit%3Dmax%26auto%3Dformat&w=1920&q=75)• 2024-01-05\n\n*   [Retrieval Augmented](https://www.llamaindex.ai/blog/tag/retrieval-augmented)\n*   [LLM](https://www.llamaindex.ai/blog/tag/llm)\n*   [Retrieval Generation](https://www.llamaindex.ai/blog/tag/retrieval-generation)\n*   [AI](https://www.llamaindex.ai/blog/tag/ai)\n\nIt’s the start of a new year and perhaps you’re looking to break into the RAG scene by building your very first RAG system. Or, maybe you’ve built Basic RAG systems and are now looking to enhance them to something more advanced in order to better handle your user’s queries and data structures.\n\nIn either case, knowing where or how to begin may be a challenge in and of itself! If that’s true, then hopefully this blog post points you in the right direction for your next steps, and moreover, provides for you a mental model for you to anchor your decisions when building advanced RAG systems.\n\nThe RAG cheat sheet shared above was greatly inspired by a recent RAG survey paper ([“Retrieval-Augmented Generation for Large Language Models: A Survey” Gao, Yunfan, et al. 2023](https://arxiv.org/pdf/2312.10997.pdf)).\n\nBasic RAG\n---------\n\nMainstream RAG as defined today involves retrieving documents from an external knowledge database and passing these along with the user’s query to an LLM for response generation. In other words, RAG involves a Retrieval component, an External Knowledge database and a Generation component.\n\n**LlamaIndex Basic RAG Recipe:**\n\nfrom llama\\_index import SimpleDirectoryReader, VectorStoreIndex\n\n\ndocuments = SimpleDirectoryReader(input\\_dir=\"...\").load\\_data()\n\n\n\nindex = VectorStoreIndex.from\\_documents(documents=documents)\n\n\n\nquery\\_engine = index.as\\_query\\_engine()\n\n\nresponse = query\\_engine.query(\"A user's query\")\n\nSuccess Requirements for RAG\n----------------------------\n\nIn order for a RAG system to be deemed as a success (in the sense of providing useful and relevant answers to user questions), there are really only two high level requirements:\n\n1.  Retrieval must be able to find the most relevant documents to a user query.\n2.  Generation must be able to make good use of the retrieved documents to sufficiently answer the user query.\n\nAdvanced RAG\n------------\n\nWith the success requirements defined, we can then say that building advanced RAG is really about the application of more sophisticated techniques and strategies (to the Retrieval or Generation components) to ensure that they are ultimately met. Furthermore, we can categorize a sophisticated technique as either one that addresses one of the two high-level success requirements independent (more or less) of the other, or one that addresses both of these requirements simultaneously.\n\nAdvanced techniques for Retrieval must be able to find the most relevant documents to a user query\n--------------------------------------------------------------------------------------------------\n\nBelow we briefly describe a couple of the more sophisticated techniques to help achieve the first success requirement.\n\n1.  **Chunk-Size Optimization:** Since LLMs are restricted by context length, it is necessary to chunk documents when building the External Knowledge database. Chunks that are too big or too small can pose problems for the Generation component leading to in accurate responses.\n\n**LlamaIndex Chunk Size Optimization Recipe** ([notebook guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/param_optimizer/param_optimizer.ipynb))**:**\n\nfrom llama\\_index import ServiceContext\nfrom llama\\_index.param\\_tuner.base import ParamTuner, RunResult\nfrom llama\\_index.evaluation import SemanticSimilarityEvaluator, BatchEvalRunner\n\ndef objective\\_function(params\\_dict):\n    chunk\\_size = params\\_dict\\[\"chunk\\_size\"\\]\n    docs = params\\_dict\\[\"docs\"\\]\n    top\\_k = params\\_dict\\[\"top\\_k\"\\]\n    eval\\_qs = params\\_dict\\[\"eval\\_qs\"\\]\n    ref\\_response\\_strs = params\\_dict\\[\"ref\\_response\\_strs\"\\]\n\n    \n    index = \\_build\\_index(chunk\\_size, docs)  \n    query\\_engine = index.as\\_query\\_engine(similarity\\_top\\_k=top\\_k)\n  \n    \n    pred\\_response\\_objs = get\\_responses(\n        eval\\_qs, query\\_engine, show\\_progress=True\n    )\n\n    \n    \n    evaluator = SemanticSimilarityEvaluator(...)\n    eval\\_batch\\_runner = BatchEvalRunner(\n        {\"semantic\\_similarity\": evaluator}, workers=2, show\\_progress=True\n    )\n    eval\\_results = eval\\_batch\\_runner.evaluate\\_responses(\n        eval\\_qs, responses=pred\\_response\\_objs, reference=ref\\_response\\_strs\n    )\n\n    \n    mean\\_score = np.array(\n        \\[r.score for r in eval\\_results\\[\"semantic\\_similarity\"\\]\\]\n    ).mean()\n\n    return RunResult(score=mean\\_score, params=params\\_dict)\n\n\nparam\\_dict = {\"chunk\\_size\": \\[256, 512, 1024\\]} \nfixed\\_param\\_dict = { \n  \"top\\_k\": 2,\n    \"docs\": docs,\n    \"eval\\_qs\": eval\\_qs\\[:10\\],\n    \"ref\\_response\\_strs\": ref\\_response\\_strs\\[:10\\],\n}\nparam\\_tuner = ParamTuner(\n    param\\_fn=objective\\_function,\n    param\\_dict=param\\_dict,\n    fixed\\_param\\_dict=fixed\\_param\\_dict,\n    show\\_progress=True,\n)\n\n\nresults = param\\_tuner.tune()\nbest\\_result = results.best\\_run\\_result\nbest\\_chunk\\_size = results.best\\_run\\_result.params\\[\"chunk\\_size\"\\]\n\n**2\\. Structured External Knowledge:** In complex scenarios, it may be necessary to build your external knowledge with a bit more structure than the basic vector index so as to permit recursive retrievals or routed retrieval when dealing with sensibly separated external knowledge sources.\n\n**LlamaIndex Recursive Retrieval Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes.html))**:**\n\nfrom llama\\_index import SimpleDirectoryReader, VectorStoreIndex\nfrom llama\\_index.node\\_parser import SentenceSplitter\nfrom llama\\_index.schema import IndexNode\n\n\n\n\n\n\ndocuments = SimpleDirectoryReader(\n  input\\_file=\"some\\_data\\_path/llama2.pdf\"\n).load\\_data()\n\n\nnode\\_parser = SentenceSplitter(chunk\\_size=1024)\nbase\\_nodes = node\\_parser.get\\_nodes\\_from\\_documents(documents)\n\n\nsub\\_chunk\\_sizes = \\[256, 512\\]\nsub\\_node\\_parsers = \\[\n    SentenceSplitter(chunk\\_size=c, chunk\\_overlap=20) for c in sub\\_chunk\\_sizes\n\\]\nall\\_nodes = \\[\\]\nfor base\\_node in base\\_nodes:\n    for n in sub\\_node\\_parsers:\n        sub\\_nodes = n.get\\_nodes\\_from\\_documents(\\[base\\_node\\])\n        sub\\_inodes = \\[\n            IndexNode.from\\_text\\_node(sn, base\\_node.node\\_id) for sn in sub\\_nodes\n        \\]\n        all\\_nodes.extend(sub\\_inodes)\n    \n    original\\_node = IndexNode.from\\_text\\_node(base\\_node, base\\_node.node\\_id)\n    all\\_nodes.append(original\\_node)\n\n\nvector\\_index\\_chunk = VectorStoreIndex(\n    all\\_nodes, service\\_context=service\\_context\n)\nvector\\_retriever\\_chunk = vector\\_index\\_chunk.as\\_retriever(similarity\\_top\\_k=2)\n\n\nall\\_nodes\\_dict = {n.node\\_id: n for n in all\\_nodes}\nretriever\\_chunk = RecursiveRetriever(\n    \"vector\",\n    retriever\\_dict={\"vector\": vector\\_retriever\\_chunk},\n    node\\_dict=all\\_nodes\\_dict,\n    verbose=True,\n)\n\n\nquery\\_engine\\_chunk = RetrieverQueryEngine.from\\_args(\n    retriever\\_chunk, service\\_context=service\\_context\n)\n\n\nresponse = query\\_engine\\_chunk.query(\n    \"Can you tell me about the key concepts for safety finetuning\"\n)\n\n**Other useful links**\n\nWe have several of guides demonstrating the application of other advanced techniques to help ensure accurate retrieval in complex cases. Here are links to a select few of them:\n\n1.  [Building External Knowledge using Knowledge Graphs](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine.html)\n2.  [Performing Mixed Retrieval with Auto Retrievers](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever.html)\n3.  [Building Fusion Retrievers](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion.html)\n4.  [Fine-tuning Embedding Models used in Retrieval](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding.html)\n5.  [Transforming Query Embeddings (HyDE)](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo.html)\n\nAdvanced techniques for Generation must be able to make good use of the retrieved documents\n-------------------------------------------------------------------------------------------\n\nSimilar to previous section, we provide a couple of examples of the sophisticated techniques under this category, which can be described as ensuring that the retrieved documents are well aligned to the LLM of the Generator.\n\n1.  **Information Compression:** Not only are LLMs are restricted by context length, but there can be response degradation if the retrieved documents carry too much noise (i.e. irrelevant information).\n\n**LlamaIndex Information Compression Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongLLMLingua.html))**:**\n\nfrom llama\\_index import SimpleDirectoryReader, VectorStoreIndex\nfrom llama\\_index.query\\_engine import RetrieverQueryEngine\nfrom llama\\_index.postprocessor import LongLLMLinguaPostprocessor\n\n\n\n\n\n\nnode\\_postprocessor = LongLLMLinguaPostprocessor(\n    instruction\\_str=\"Given the context, please answer the final question\",\n    target\\_token=300,\n    rank\\_method=\"longllmlingua\",\n    additional\\_compress\\_kwargs={\n        \"condition\\_compare\": True,\n        \"condition\\_in\\_question\": \"after\",\n        \"context\\_budget\": \"+100\",\n        \"reorder\\_context\": \"sort\",  \n    },\n)\n\n\ndocuments = SimpleDirectoryReader(input\\_dir=\"...\").load\\_data()\nindex = VectorStoreIndex.from\\_documents(documents)\n\n\nretriever = index.as\\_retriever(similarity\\_top\\_k=2)\nretriever\\_query\\_engine = RetrieverQueryEngine.from\\_args(\n    retriever, node\\_postprocessors=\\[node\\_postprocessor\\]\n)\n\n\nresponse = retriever\\_query\\_engine.query(\"A user query\")\n\n**2\\. Result Re-Rank:** LLMs suffer from the so-called “Lost in the Middle” phenomena which stipulates that LLMs focus on the extreme ends of the prompts. In light of this, it is beneficial to re-rank retrieved documents before passing them off to the Generation component.\n\n**LlamaIndex Re-Ranking For Better Generation Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank.html))**:**\n\nimport os\nfrom llama\\_index import SimpleDirectoryReader, VectorStoreIndex\nfrom llama\\_index.postprocessor.cohere\\_rerank import CohereRerank\nfrom llama\\_index.postprocessor import LongLLMLinguaPostprocessor\n\n\n\n\n\n\napi\\_key = os.environ\\[\"COHERE\\_API\\_KEY\"\\]\ncohere\\_rerank = CohereRerank(api\\_key=api\\_key, top\\_n=2)\n\n\ndocuments = SimpleDirectoryReader(\"./data/paul\\_graham/\").load\\_data()\nindex = VectorStoreIndex.from\\_documents(documents=documents)\nquery\\_engine = index.as\\_query\\_engine(\n    similarity\\_top\\_k=10,\n    node\\_postprocessors=\\[cohere\\_rerank\\],\n)\n\n\nresponse = query\\_engine.query(\n    \"What did Sam Altman do in this essay?\"\n)\n\nAdvanced techniques for simultaneously addressing Retrieval and Generation success requirements\n-----------------------------------------------------------------------------------------------\n\nIn this sub section, we consider sophisticated methods that use the synergy of retrieval and generation in order to achieve both better retrieval as well as more accurate generated responses to user queries).\n\n1.  **Generator-Enhanced Retrieval:** These techniques make use of the LLM’s inherent reasoning abilities to refine the user query before retrieval is performed so as to better indicate what exactly it requires to provide a useful response.\n\n**LlamaIndex Generator-Enhanced Retrieval Recipe** ([notebook guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine.html))**:**\n\nfrom llama\\_index.llms import OpenAI\nfrom llama\\_index.query\\_engine import FLAREInstructQueryEngine\nfrom llama\\_index import (\n    VectorStoreIndex,\n    SimpleDirectoryReader,\n    ServiceContext,\n)\n\n\n\n\n\n\ndocuments = SimpleDirectoryReader(\"./data/paul\\_graham\").load\\_data()\nindex = VectorStoreIndex.from\\_documents(documents)\nindex\\_query\\_engine = index.as\\_query\\_engine(similarity\\_top\\_k=2)\nservice\\_context = ServiceContext.from\\_defaults(llm=OpenAI(model=\"gpt-4\"))\nflare\\_query\\_engine = FLAREInstructQueryEngine(\n    query\\_engine=index\\_query\\_engine,\n    service\\_context=service\\_context,\n    max\\_iterations=7,\n    verbose=True,\n)\n\n\nresponse = flare\\_query\\_engine.query(\n    \"Can you tell me about the author's trajectory in the startup world?\"\n)\n\n**2\\. Iterative Retrieval-Generator RAG:** For some complex cases, multi-step reasoning may be required to provide a useful and relevant answer to the user query.\n\n**LlamaIndex Iterative Retrieval-Generator Recipe (**[notebook guide](https://docs.llamaindex.ai/en/stable/examples/evaluation/RetryQuery.html#retry-query-engine)**):**\n\nfrom llama\\_index.query\\_engine import RetryQueryEngine\nfrom llama\\_index.evaluation import RelevancyEvaluator\n\n\n\n\n\n\n\ndocuments = SimpleDirectoryReader(\"./data/paul\\_graham\").load\\_data()\nindex = VectorStoreIndex.from\\_documents(documents)\nbase\\_query\\_engine = index.as\\_query\\_engine()\nquery\\_response\\_evaluator = RelevancyEvaluator() \n                                                \nretry\\_query\\_engine = RetryQueryEngine(\n    base\\_query\\_engine, query\\_response\\_evaluator\n)\n\n\nretry\\_response = retry\\_query\\_engine.query(\"A user query\")\n\nMeasurement Aspects of RAG\n--------------------------\n\nEvaluating RAG systems are, of course, of utmost importance. In their survey paper, Gao, Yunfan et al. indicate 7 measurement aspects as seen in the top-right portion of the attached RAG cheat sheet. The llama-index library consists of several evaluation abstractions as well as integrations to RAGAs in order to help builders gain an understanding of the level to which their RAG system achieves the success requirements through the lens of these measurement aspects. Below, we list a select few of the evaluation notebook guides.\n\n1.  [Answer Relevancy and Context Relevancy](https://docs.llamaindex.ai/en/latest/examples/evaluation/answer_and_context_relevancy.html)\n2.  [Faithfulness](https://www.notion.so/LlamaIndex-Platform-0754edd9af1c4159bde12649c184c8ef?pvs=21)\n3.  [Retrieval Evaluation](https://github.com/run-llama/llama_index/blob/main/docs/examples/evaluation/retrieval/retriever_eval.ipynb)\n4.  [Batch Evaluations with BatchEvalRunner](https://docs.llamaindex.ai/en/stable/examples/evaluation/batch_eval.html)\n\nYou’re Now Equipped To Do Advanced RAG\n--------------------------------------\n\nAfter reading this blog post, we hope that you feel more equipped and confident to apply some of these sophisticated techniques for building Advanced RAG systems!",
  "usage": {
    "tokens": 3538
  }
}
```
