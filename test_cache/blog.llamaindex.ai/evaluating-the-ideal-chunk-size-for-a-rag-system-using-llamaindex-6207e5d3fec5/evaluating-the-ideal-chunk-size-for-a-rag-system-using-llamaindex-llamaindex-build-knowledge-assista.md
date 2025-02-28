---
title: Evaluating the Ideal Chunk Size for a RAG System using LlamaIndex — LlamaIndex - Build Knowledge Assistants over your Enterprise Data
description: LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.
url: https://blog.llamaindex.ai/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5
timestamp: 2025-01-20T15:46:58.666Z
domain: blog.llamaindex.ai
path: evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5
---

# Evaluating the Ideal Chunk Size for a RAG System using LlamaIndex — LlamaIndex - Build Knowledge Assistants over your Enterprise Data


LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.


## Content

![Image 11](https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2F9d4643fc433bf8b5e162fff289c4a2b7767cf3b2-1024x640.jpg%3Ffit%3Dmax%26auto%3Dformat&w=1920&q=75)• 2023-10-05

*   [Llamaindex](https://www.llamaindex.ai/blog/tag/llamaindex)
*   [AI](https://www.llamaindex.ai/blog/tag/ai)
*   [LLM](https://www.llamaindex.ai/blog/tag/llm)
*   [OpenAI](https://www.llamaindex.ai/blog/tag/openai)
*   [Retrieval](https://www.llamaindex.ai/blog/tag/retrieval)

Introduction
------------

Retrieval-augmented generation (RAG) has introduced an innovative approach that fuses the extensive retrieval capabilities of search systems with the LLM. When implementing a RAG system, one critical parameter that governs the system’s efficiency and performance is the `chunk_size`. How does one discern the optimal chunk size for seamless retrieval? This is where LlamaIndex `Response Evaluation` comes in handy. In this blog post, we'll guide you through the steps to determine the best `chunk size` using LlamaIndex’s `Response Evaluation` module. If you're unfamiliar with the `Response` Evaluation module, we recommend reviewing its [documentation](https://docs.llamaindex.ai/en/latest/core_modules/supporting_modules/evaluation/modules.html) before proceeding.

Why Chunk Size Matters
----------------------

Choosing the right `chunk_size` is a critical decision that can influence the efficiency and accuracy of a RAG system in several ways:

1.  **Relevance and Granularity**: A small `chunk_size`, like 128, yields more granular chunks. This granularity, however, presents a risk: vital information might not be among the top retrieved chunks, especially if the `similarity_top_k` setting is as restrictive as 2. Conversely, a chunk size of 512 is likely to encompass all necessary information within the top chunks, ensuring that answers to queries are readily available. To navigate this, we employ the Faithfulness and Relevancy metrics. These measure the absence of ‘hallucinations’ and the ‘relevancy’ of responses based on the query and the retrieved contexts respectively.
2.  **Response Generation Time**: As the `chunk_size` increases, so does the volume of information directed into the LLM to generate an answer. While this can ensure a more comprehensive context, it might also slow down the system. Ensuring that the added depth doesn't compromise the system's responsiveness is crucial.

In essence, determining the optimal `chunk_size` is about striking a balance: capturing all essential information without sacrificing speed. It's vital to undergo thorough testing with various sizes to find a configuration that suits the specific use case and dataset.

For a practical evaluation in choosing the right `chunk_size`, you can access and run the following setup on this [**Google Colab Notebook**](https://colab.research.google.com/drive/1LPvJyEON6btMpubYdwySfNs0FuNR9nza?usp=sharing).

Setup
-----

Before embarking on the experiment, we need to ensure all requisite modules are imported:

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
)
from llama\_index.evaluation import (
    DatasetGenerator,
    FaithfulnessEvaluator,
    RelevancyEvaluator
)
from llama\_index.llms import OpenAI

import openai
import time
openai.api\_key = 'OPENAI-API-KEY'

Download Data
-------------

We’ll be using the Uber 10K SEC Filings for 2021 for this experiment.

!mkdir -p 'data/10k/'
!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf'

Load Data
---------

Let’s load our document.

documents = SimpleDirectoryReader("./data/10k/").load\_data()

Question Generation
-------------------

To select the right `chunk_size`, we'll compute metrics like Average Response time, Faithfulness, and Relevancy for various `chunk_sizes`. The `DatasetGenerator` will help us generate questions from the documents.

data\_generator = DatasetGenerator.from\_documents(documents)
eval\_questions = data\_generator.generate\_questions\_from\_nodes()

Setting Up Evaluators
---------------------

We are setting up the GPT-4 model to serve as the backbone for evaluating the responses generated during the experiment. Two evaluators, `FaithfulnessEvaluator` and `RelevancyEvaluator`, are initialised with the `service_context` .

1.  **Faithfulness Evaluator** — It is useful for measuring if the response was hallucinated and measures if the response from a query engine matches any source nodes.
2.  **Relevancy Evaluator** — It is useful for measuring if the query was actually answered by the response and measures if the response + source nodes match the query.

\# We will use GPT-4 for evaluating the responses
gpt4 = OpenAI(temperature=0, model="gpt-4")

# Define service context for GPT-4 for evaluation
service\_context\_gpt4 = ServiceContext.from\_defaults(llm=gpt4)

# Define Faithfulness and Relevancy Evaluators which are based on GPT-4
faithfulness\_gpt4 = FaithfulnessEvaluator(service\_context=service\_context\_gpt4)
relevancy\_gpt4 = RelevancyEvaluator(service\_context=service\_context\_gpt4)

Response Evaluation For A Chunk Size
------------------------------------

We evaluate each chunk\_size based on 3 metrics.

1.  Average Response Time.
2.  Average Faithfulness.
3.  Average Relevancy.

Here’s a function, `evaluate_response_time_and_accuracy`, that does just that which has:

1.  VectorIndex Creation.
2.  Building the Query Engine.
3.  Metrics Calculation.

def evaluate\_response\_time\_and\_accuracy(chunk\_size, eval\_questions):
    """
    Evaluate the average response time, faithfulness, and relevancy of responses generated by GPT-3.5-turbo for a given chunk size.
    
    Parameters:
    chunk\_size (int): The size of data chunks being processed.
    
    Returns:
    tuple: A tuple containing the average response time, faithfulness, and relevancy metrics.
    """

    total\_response\_time = 0
    total\_faithfulness = 0
    total\_relevancy = 0

    
    llm = OpenAI(model="gpt-3.5-turbo")
    service\_context = ServiceContext.from\_defaults(llm=llm, chunk\_size=chunk\_size)
    vector\_index = VectorStoreIndex.from\_documents(
        eval\_documents, service\_context=service\_context
    )
    
    query\_engine = vector\_index.as\_query\_engine()
    num\_questions = len(eval\_questions)

    
    
    
    for question in eval\_questions:
        start\_time = time.time()
        response\_vector = query\_engine.query(question)
        elapsed\_time = time.time() - start\_time
        
        faithfulness\_result = faithfulness\_gpt4.evaluate\_response(
            response=response\_vector
        ).passing
        
        relevancy\_result = relevancy\_gpt4.evaluate\_response(
            query=question, response=response\_vector
        ).passing

        total\_response\_time += elapsed\_time
        total\_faithfulness += faithfulness\_result
        total\_relevancy += relevancy\_result

    average\_response\_time = total\_response\_time / num\_questions
    average\_faithfulness = total\_faithfulness / num\_questions
    average\_relevancy = total\_relevancy / num\_questions

    return average\_response\_time, average\_faithfulness, average\_relevancy

Testing Across Different Chunk Sizes
------------------------------------

We’ll evaluate a range of chunk sizes to identify which offers the most promising metrics.

chunk\_sizes = \[128, 256, 512, 1024, 2048\]

for chunk\_size in chunk\_sizes:
  avg\_response\_time, avg\_faithfulness, avg\_relevancy = evaluate\_response\_time\_and\_accuracy(chunk\_size, eval\_questions)
  print(f"Chunk size {chunk\_size} - Average Response time: {avg\_response\_time:.2f}s, Average Faithfulness: {avg\_faithfulness:.2f}, Average Relevancy: {avg\_relevancy:.2f}")

Bringing It All Together
------------------------

Let’s compile the processes:

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
)
from llama\_index.evaluation import (
    DatasetGenerator,
    FaithfulnessEvaluator,
    RelevancyEvaluator
)
from llama\_index.llms import OpenAI

import openai
import time

openai.api\_key = 'OPENAI-API-KEY'

!mkdir -p 'data/10k/'
!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf'

reader = SimpleDirectoryReader("./data/10k/")
documents = reader.load\_data()


eval\_documents = documents\[:20\]
data\_generator = DatasetGenerator.from\_documents()
eval\_questions = data\_generator.generate\_questions\_from\_nodes(num = 20)


gpt4 = OpenAI(temperature=0, model="gpt-4")


service\_context\_gpt4 = ServiceContext.from\_defaults(llm=gpt4)


faithfulness\_gpt4 = FaithfulnessEvaluator(service\_context=service\_context\_gpt4)
relevancy\_gpt4 = RelevancyEvaluator(service\_context=service\_context\_gpt4)

def evaluate\_response\_time\_and\_accuracy(chunk\_size):
    total\_response\_time = 0
    total\_faithfulness = 0
    total\_relevancy = 0

    
    llm = OpenAI(model="gpt-3.5-turbo")
    service\_context = ServiceContext.from\_defaults(llm=llm, chunk\_size=chunk\_size)
    vector\_index = VectorStoreIndex.from\_documents(
        eval\_documents, service\_context=service\_context
    )

    query\_engine = vector\_index.as\_query\_engine()
    num\_questions = len(eval\_questions)

    for question in eval\_questions:
        start\_time = time.time()
        response\_vector = query\_engine.query(question)
        elapsed\_time = time.time() - start\_time
        
        faithfulness\_result = faithfulness\_gpt4.evaluate\_response(
            response=response\_vector
        ).passing
        
        relevancy\_result = relevancy\_gpt4.evaluate\_response(
            query=question, response=response\_vector
        ).passing

        total\_response\_time += elapsed\_time
        total\_faithfulness += faithfulness\_result
        total\_relevancy += relevancy\_result

    average\_response\_time = total\_response\_time / num\_questions
    average\_faithfulness = total\_faithfulness / num\_questions
    average\_relevancy = total\_relevancy / num\_questions

    return average\_response\_time, average\_faithfulness, average\_relevancy

for chunk\_size in \[128, 256, 512, 1024, 2048\]
  avg\_time, avg\_faithfulness, avg\_relevancy = evaluate\_response\_time\_and\_accuracy(chunk\_size)
  print(f"Chunk size {chunk\_size} - Average Response time: {avg\_time:.2f}s, Average Faithfulness: {avg\_faithfulness:.2f}, Average Relevancy: {avg\_relevancy:.2f}")

Result
------

![Image 12](https://www.llamaindex.ai/blog/images/1*dynabe9lAsB9DBe7XqmxQw.png)

The above table illustrates that as the chunk size increases, there is a minor uptick in the Average Response Time. Interestingly, the Average Faithfulness seems to reach its zenith at `chunk_size`of 1024, whereas Average Relevancy shows a consistent improvement with larger chunk sizes, also peaking at 1024. This suggests that a chunk size of 1024 might strike an optimal balance between response time and the quality of the responses, measured in terms of faithfulness and relevancy.

Conclusion
----------

Identifying the best chunk size for a RAG system is as much about intuition as it is empirical evidence. With LlamaIndex’s `Response Evaluation` module, you can experiment with various sizes and base your decisions on concrete data. When building a RAG system, always remember that `chunk_size` is a pivotal parameter. Invest the time to meticulously evaluate and adjust your chunk size for unmatched results.

## Metadata

```json
{
  "title": "Evaluating the Ideal Chunk Size for a RAG System using LlamaIndex — LlamaIndex - Build Knowledge Assistants over your Enterprise Data",
  "description": "LlamaIndex is a simple, flexible framework for building knowledge assistants using LLMs connected to your enterprise data.",
  "url": "https://blog.llamaindex.ai/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5",
  "content": "![Image 11](https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2F9d4643fc433bf8b5e162fff289c4a2b7767cf3b2-1024x640.jpg%3Ffit%3Dmax%26auto%3Dformat&w=1920&q=75)• 2023-10-05\n\n*   [Llamaindex](https://www.llamaindex.ai/blog/tag/llamaindex)\n*   [AI](https://www.llamaindex.ai/blog/tag/ai)\n*   [LLM](https://www.llamaindex.ai/blog/tag/llm)\n*   [OpenAI](https://www.llamaindex.ai/blog/tag/openai)\n*   [Retrieval](https://www.llamaindex.ai/blog/tag/retrieval)\n\nIntroduction\n------------\n\nRetrieval-augmented generation (RAG) has introduced an innovative approach that fuses the extensive retrieval capabilities of search systems with the LLM. When implementing a RAG system, one critical parameter that governs the system’s efficiency and performance is the `chunk_size`. How does one discern the optimal chunk size for seamless retrieval? This is where LlamaIndex `Response Evaluation` comes in handy. In this blog post, we'll guide you through the steps to determine the best `chunk size` using LlamaIndex’s `Response Evaluation` module. If you're unfamiliar with the `Response` Evaluation module, we recommend reviewing its [documentation](https://docs.llamaindex.ai/en/latest/core_modules/supporting_modules/evaluation/modules.html) before proceeding.\n\nWhy Chunk Size Matters\n----------------------\n\nChoosing the right `chunk_size` is a critical decision that can influence the efficiency and accuracy of a RAG system in several ways:\n\n1.  **Relevance and Granularity**: A small `chunk_size`, like 128, yields more granular chunks. This granularity, however, presents a risk: vital information might not be among the top retrieved chunks, especially if the `similarity_top_k` setting is as restrictive as 2. Conversely, a chunk size of 512 is likely to encompass all necessary information within the top chunks, ensuring that answers to queries are readily available. To navigate this, we employ the Faithfulness and Relevancy metrics. These measure the absence of ‘hallucinations’ and the ‘relevancy’ of responses based on the query and the retrieved contexts respectively.\n2.  **Response Generation Time**: As the `chunk_size` increases, so does the volume of information directed into the LLM to generate an answer. While this can ensure a more comprehensive context, it might also slow down the system. Ensuring that the added depth doesn't compromise the system's responsiveness is crucial.\n\nIn essence, determining the optimal `chunk_size` is about striking a balance: capturing all essential information without sacrificing speed. It's vital to undergo thorough testing with various sizes to find a configuration that suits the specific use case and dataset.\n\nFor a practical evaluation in choosing the right `chunk_size`, you can access and run the following setup on this [**Google Colab Notebook**](https://colab.research.google.com/drive/1LPvJyEON6btMpubYdwySfNs0FuNR9nza?usp=sharing).\n\nSetup\n-----\n\nBefore embarking on the experiment, we need to ensure all requisite modules are imported:\n\nimport nest\\_asyncio\n\nnest\\_asyncio.apply()\n\nfrom llama\\_index import (\n    SimpleDirectoryReader,\n    VectorStoreIndex,\n    ServiceContext,\n)\nfrom llama\\_index.evaluation import (\n    DatasetGenerator,\n    FaithfulnessEvaluator,\n    RelevancyEvaluator\n)\nfrom llama\\_index.llms import OpenAI\n\nimport openai\nimport time\nopenai.api\\_key = 'OPENAI-API-KEY'\n\nDownload Data\n-------------\n\nWe’ll be using the Uber 10K SEC Filings for 2021 for this experiment.\n\n!mkdir -p 'data/10k/'\n!wget 'https://raw.githubusercontent.com/jerryjliu/llama\\_index/main/docs/examples/data/10k/uber\\_2021.pdf' -O 'data/10k/uber\\_2021.pdf'\n\nLoad Data\n---------\n\nLet’s load our document.\n\ndocuments = SimpleDirectoryReader(\"./data/10k/\").load\\_data()\n\nQuestion Generation\n-------------------\n\nTo select the right `chunk_size`, we'll compute metrics like Average Response time, Faithfulness, and Relevancy for various `chunk_sizes`. The `DatasetGenerator` will help us generate questions from the documents.\n\ndata\\_generator = DatasetGenerator.from\\_documents(documents)\neval\\_questions = data\\_generator.generate\\_questions\\_from\\_nodes()\n\nSetting Up Evaluators\n---------------------\n\nWe are setting up the GPT-4 model to serve as the backbone for evaluating the responses generated during the experiment. Two evaluators, `FaithfulnessEvaluator` and `RelevancyEvaluator`, are initialised with the `service_context` .\n\n1.  **Faithfulness Evaluator** — It is useful for measuring if the response was hallucinated and measures if the response from a query engine matches any source nodes.\n2.  **Relevancy Evaluator** — It is useful for measuring if the query was actually answered by the response and measures if the response + source nodes match the query.\n\n\\# We will use GPT-4 for evaluating the responses\ngpt4 = OpenAI(temperature=0, model=\"gpt-4\")\n\n# Define service context for GPT-4 for evaluation\nservice\\_context\\_gpt4 = ServiceContext.from\\_defaults(llm=gpt4)\n\n# Define Faithfulness and Relevancy Evaluators which are based on GPT-4\nfaithfulness\\_gpt4 = FaithfulnessEvaluator(service\\_context=service\\_context\\_gpt4)\nrelevancy\\_gpt4 = RelevancyEvaluator(service\\_context=service\\_context\\_gpt4)\n\nResponse Evaluation For A Chunk Size\n------------------------------------\n\nWe evaluate each chunk\\_size based on 3 metrics.\n\n1.  Average Response Time.\n2.  Average Faithfulness.\n3.  Average Relevancy.\n\nHere’s a function, `evaluate_response_time_and_accuracy`, that does just that which has:\n\n1.  VectorIndex Creation.\n2.  Building the Query Engine.\n3.  Metrics Calculation.\n\ndef evaluate\\_response\\_time\\_and\\_accuracy(chunk\\_size, eval\\_questions):\n    \"\"\"\n    Evaluate the average response time, faithfulness, and relevancy of responses generated by GPT-3.5-turbo for a given chunk size.\n    \n    Parameters:\n    chunk\\_size (int): The size of data chunks being processed.\n    \n    Returns:\n    tuple: A tuple containing the average response time, faithfulness, and relevancy metrics.\n    \"\"\"\n\n    total\\_response\\_time = 0\n    total\\_faithfulness = 0\n    total\\_relevancy = 0\n\n    \n    llm = OpenAI(model=\"gpt-3.5-turbo\")\n    service\\_context = ServiceContext.from\\_defaults(llm=llm, chunk\\_size=chunk\\_size)\n    vector\\_index = VectorStoreIndex.from\\_documents(\n        eval\\_documents, service\\_context=service\\_context\n    )\n    \n    query\\_engine = vector\\_index.as\\_query\\_engine()\n    num\\_questions = len(eval\\_questions)\n\n    \n    \n    \n    for question in eval\\_questions:\n        start\\_time = time.time()\n        response\\_vector = query\\_engine.query(question)\n        elapsed\\_time = time.time() - start\\_time\n        \n        faithfulness\\_result = faithfulness\\_gpt4.evaluate\\_response(\n            response=response\\_vector\n        ).passing\n        \n        relevancy\\_result = relevancy\\_gpt4.evaluate\\_response(\n            query=question, response=response\\_vector\n        ).passing\n\n        total\\_response\\_time += elapsed\\_time\n        total\\_faithfulness += faithfulness\\_result\n        total\\_relevancy += relevancy\\_result\n\n    average\\_response\\_time = total\\_response\\_time / num\\_questions\n    average\\_faithfulness = total\\_faithfulness / num\\_questions\n    average\\_relevancy = total\\_relevancy / num\\_questions\n\n    return average\\_response\\_time, average\\_faithfulness, average\\_relevancy\n\nTesting Across Different Chunk Sizes\n------------------------------------\n\nWe’ll evaluate a range of chunk sizes to identify which offers the most promising metrics.\n\nchunk\\_sizes = \\[128, 256, 512, 1024, 2048\\]\n\nfor chunk\\_size in chunk\\_sizes:\n  avg\\_response\\_time, avg\\_faithfulness, avg\\_relevancy = evaluate\\_response\\_time\\_and\\_accuracy(chunk\\_size, eval\\_questions)\n  print(f\"Chunk size {chunk\\_size} - Average Response time: {avg\\_response\\_time:.2f}s, Average Faithfulness: {avg\\_faithfulness:.2f}, Average Relevancy: {avg\\_relevancy:.2f}\")\n\nBringing It All Together\n------------------------\n\nLet’s compile the processes:\n\nimport nest\\_asyncio\n\nnest\\_asyncio.apply()\n\nfrom llama\\_index import (\n    SimpleDirectoryReader,\n    VectorStoreIndex,\n    ServiceContext,\n)\nfrom llama\\_index.evaluation import (\n    DatasetGenerator,\n    FaithfulnessEvaluator,\n    RelevancyEvaluator\n)\nfrom llama\\_index.llms import OpenAI\n\nimport openai\nimport time\n\nopenai.api\\_key = 'OPENAI-API-KEY'\n\n!mkdir -p 'data/10k/'\n!wget 'https://raw.githubusercontent.com/jerryjliu/llama\\_index/main/docs/examples/data/10k/uber\\_2021.pdf' -O 'data/10k/uber\\_2021.pdf'\n\nreader = SimpleDirectoryReader(\"./data/10k/\")\ndocuments = reader.load\\_data()\n\n\neval\\_documents = documents\\[:20\\]\ndata\\_generator = DatasetGenerator.from\\_documents()\neval\\_questions = data\\_generator.generate\\_questions\\_from\\_nodes(num = 20)\n\n\ngpt4 = OpenAI(temperature=0, model=\"gpt-4\")\n\n\nservice\\_context\\_gpt4 = ServiceContext.from\\_defaults(llm=gpt4)\n\n\nfaithfulness\\_gpt4 = FaithfulnessEvaluator(service\\_context=service\\_context\\_gpt4)\nrelevancy\\_gpt4 = RelevancyEvaluator(service\\_context=service\\_context\\_gpt4)\n\ndef evaluate\\_response\\_time\\_and\\_accuracy(chunk\\_size):\n    total\\_response\\_time = 0\n    total\\_faithfulness = 0\n    total\\_relevancy = 0\n\n    \n    llm = OpenAI(model=\"gpt-3.5-turbo\")\n    service\\_context = ServiceContext.from\\_defaults(llm=llm, chunk\\_size=chunk\\_size)\n    vector\\_index = VectorStoreIndex.from\\_documents(\n        eval\\_documents, service\\_context=service\\_context\n    )\n\n    query\\_engine = vector\\_index.as\\_query\\_engine()\n    num\\_questions = len(eval\\_questions)\n\n    for question in eval\\_questions:\n        start\\_time = time.time()\n        response\\_vector = query\\_engine.query(question)\n        elapsed\\_time = time.time() - start\\_time\n        \n        faithfulness\\_result = faithfulness\\_gpt4.evaluate\\_response(\n            response=response\\_vector\n        ).passing\n        \n        relevancy\\_result = relevancy\\_gpt4.evaluate\\_response(\n            query=question, response=response\\_vector\n        ).passing\n\n        total\\_response\\_time += elapsed\\_time\n        total\\_faithfulness += faithfulness\\_result\n        total\\_relevancy += relevancy\\_result\n\n    average\\_response\\_time = total\\_response\\_time / num\\_questions\n    average\\_faithfulness = total\\_faithfulness / num\\_questions\n    average\\_relevancy = total\\_relevancy / num\\_questions\n\n    return average\\_response\\_time, average\\_faithfulness, average\\_relevancy\n\nfor chunk\\_size in \\[128, 256, 512, 1024, 2048\\]\n  avg\\_time, avg\\_faithfulness, avg\\_relevancy = evaluate\\_response\\_time\\_and\\_accuracy(chunk\\_size)\n  print(f\"Chunk size {chunk\\_size} - Average Response time: {avg\\_time:.2f}s, Average Faithfulness: {avg\\_faithfulness:.2f}, Average Relevancy: {avg\\_relevancy:.2f}\")\n\nResult\n------\n\n![Image 12](https://www.llamaindex.ai/blog/images/1*dynabe9lAsB9DBe7XqmxQw.png)\n\nThe above table illustrates that as the chunk size increases, there is a minor uptick in the Average Response Time. Interestingly, the Average Faithfulness seems to reach its zenith at `chunk_size`of 1024, whereas Average Relevancy shows a consistent improvement with larger chunk sizes, also peaking at 1024. This suggests that a chunk size of 1024 might strike an optimal balance between response time and the quality of the responses, measured in terms of faithfulness and relevancy.\n\nConclusion\n----------\n\nIdentifying the best chunk size for a RAG system is as much about intuition as it is empirical evidence. With LlamaIndex’s `Response Evaluation` module, you can experiment with various sizes and base your decisions on concrete data. When building a RAG system, always remember that `chunk_size` is a pivotal parameter. Invest the time to meticulously evaluate and adjust your chunk size for unmatched results.",
  "usage": {
    "tokens": 2887
  }
}
```
