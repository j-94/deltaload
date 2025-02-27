---
title: voyage-code-2: Elevate Your Code Retrieval
description: TL;DR – We are thrilled to introduce voyage-code-2, our latest embedding model specifically tailored for semantic retrieval of codes and related text data from both natural language and code queries. Our comprehensive evaluation, covering 11 code retrieval tasks (derived from popular coding datasets like HumanEval and MBPP), demonstrated a remarkable 14.52% improvement in recall compared…
url: https://blog.voyageai.com/2024/01/23/voyage-code-2-elevate-your-code-retrieval/
timestamp: 2025-01-20T16:00:35.565Z
domain: blog.voyageai.com
path: 2024_01_23_voyage-code-2-elevate-your-code-retrieval
---

# voyage-code-2: Elevate Your Code Retrieval


TL;DR – We are thrilled to introduce voyage-code-2, our latest embedding model specifically tailored for semantic retrieval of codes and related text data from both natural language and code queries. Our comprehensive evaluation, covering 11 code retrieval tasks (derived from popular coding datasets like HumanEval and MBPP), demonstrated a remarkable 14.52% improvement in recall compared…


## Content

TL;DR – We are thrilled to introduce `` `voyage-code-2```, our latest embedding model specifically tailored for semantic retrieval of **codes** and related text data from both natural language and code queries. Our comprehensive evaluation, covering 11 code retrieval tasks (derived from popular coding datasets like HumanEval and MBPP), demonstrated a remarkable 14.52% improvement in recall compared to competitors, including OpenAI and Cohere. Additionally, we noted consistent gains, averaging 3.03%, across diverse general-purpose text datasets.

[Retrieval-augmented generation (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation/), renowned for its modularity and reliability, stands as the leading approach in integrating proprietary information into LLMs. The retrieval component of RAG first vectorizes a corpus (a collection of documents) into vectors by an embedding model, and then stores and organizes these vectors in vector databases. The quality of embeddings determines the relevancy of the retrieved documents, which in turn decides the response quality of the LLMs. This underscores the importance of developing more refined and domain-specific embedding models, particularly in specialized areas such as coding, finance, law, and healthcare.

This post presents `` `voyage-code-2```, an embedding model specifically optimized for code-related applications, including semantic code search/retrieval, code completion, and various functions of general code assistants. The superior retrieval performance— 14.52% better than OpenAI ada on code datasets and 3.03% better on general-purpose corpora— is enabled by training on massive code datasets with novel algorithmic techniques, such as advanced loss functions and contrastive pairs. We have also significantly improved both the inference latency and throughput to levels suitable for real-world, interactive production environments and expanded the context window to 16K.

Code Retrieval via Embeddings
-----------------------------

The corpus for code-related retrieval tasks is often a collection of code snippets combined or augmented with auxiliary data in natural language. A typical query is either a question phrased in natural language, a snippet of code, or a combination of both. For example, the figure below shows a query and a few code snippets in the corpus.

![Image 21](https://lh7-us.googleusercontent.com/5IwlW0wVPK2DLiRweKqiGvf1HENkOItdRXW3oG61KcDmnOkydYugvR_W6dbi_GlDsocYIIu-yk62zUgREsBmXXfTJQJoaW2vxp8n6sDTyClWtaN9rfd5MohdCn6yZrGEpqinMqlXZk_Br1KmDbvzG5E)

In this case, the most relevant snippet/document to be retrieved is #1. Note that understanding the relevance between the query and the code snippets requires deep knowledge of the functionality of the code and a semantic understanding of the natural language, going beyond mere keyword matching.

Embeddings are the most effective way to quickly retrieve relevant code from a large corpus. As shown in the figure below, embedding models turn the code snippets/documents and queries into vectors. Then, we can find the nearest neighbors of the query vector among the document vectors and return the corresponding documents.

![Image 22](https://lh7-us.googleusercontent.com/l8tCa6dccNHV1tAzq2wNLtnU1Gn6OCoYPsBCqG4fd2IRzD2kk9orIAvvXFbFzwhnT3PnOcp6Ol9QgylDnBKSahVBLNBS2BRJq-6f2wjZepolIbBWDzM4FlQ6aCHEYBjpNdvQ_WJcssLlW7RiqHHydFo)

The figure below also uses real data to demonstrate how queries and documents are represented as high-dimensional vectors, which are then projected into 2D space for visualization purposes. The crucial aspect here is that similar vectors in the Euclidean space should represent semantically related documents and queries. Indeed, code snippets that are related to the same topic (indicated with specific colors) are positioned closely together.

![Image 23](https://lh7-us.googleusercontent.com/WNVLUoI8OBNbDhFuHng4Yha0Vy1e-1cfKFTtNWELyLtphoibfdYddwy7OQ_rR1yeusfR22lNlSA3390UB4R_wnXrRACEzM7gEZ0zFe9dZCE3x_SUFeNEeoFz2pj6vYTNRn8mgatyj3NICLh-36egi5A)

Qualitative Comparison
----------------------

This section demonstrates, through examples, the enhanced code understanding and code retrieval capabilities of `voyage-code-2` compared to OpenAI Ada.

**Example 1:**

![Image 24](https://lh7-us.googleusercontent.com/KmDubLIy6kyadkAaVEu6VeOHUseCTijTbFc7kbozksCdXwaQ2QmrQsADsGrzXLXXw_3fwrGV5ubPWkFj9PImxzwj6L0XvbZRO3Kec_K5AuTkQQ6sEXzzSnL4VZSRxpXtGnNu5FAKzCOCQT8sfWDnZfs)

Both `voyage-code-2` and OpenAI ada retrieved snippets that remove occurrences of a given character from the string. However, `` `voyage-code-2``` eliminates the first and last occurrences, aligning with the query, while OpenAI’s Ada removes all occurrences.

**Example 2:**

![Image 25](https://lh7-us.googleusercontent.com/TrC9vteVzC_ayGWEJNDQsnqCCQdHVbkZt9-pFOC0VMiTnyDwC0xLD5elJ17rQ2r0uV7Se8GwPALeoY3EPZjBl1ZlGPp-ARSxvap8UaDQX_FwThg5WKCRzUJ3in9LczhCLBfhOvCgUIkfG7KUGx6eUjU)

The `voyage-code-2` accurately locates the piece of code that precisely solves the given query. OpenAI ada retrieves a related but incorrect piece of code. It replaces the value of each node in the tree with the sum of all its cousins’ values which deviates from the given query.

These examples qualitatively demonstrate that `voyage-code-2` has a deeper understanding of the details in the code, enabling a  superior retrieval quality compared to OpenAI ada.

Quantitative Evaluation 
------------------------

**Evaluation Datasets.** We built a suite of 11 datasets for the retrieval quality of code,  using six publicly available datasets that consist of paired coding questions and solutions, including [HumanEval](https://github.com/openai/human-eval), [APPS](https://huggingface.co/datasets/codeparrot/apps), [MBPP](https://huggingface.co/datasets/mbpp), [DS-1000](https://github.com/xlang-ai/DS-1000/tree/main), [Codechef](https://www.codechef.com/contests), and [LeetCode](https://leetcode.com/). Each retrieval dataset comprises a corpus to be retrieved from, typically encompassing all the solutions in the original datasets, and a set of test queries, usually consisting of the collection of questions from the original datasets. The gold standard document(s) for a query question is the corresponding solution(s) in the original dataset.

The datasets encompass various programming languages and packages, including Python, C++, Java, Matplotlib, Numpy, Pandas, Pytorch, Scipy, Sklearn, and Tensorflow. In total, there are 43,909 query-document pairs. The length of queries ranges from 6 to 1963 tokens, while the length of documents spans from 5  to 2003 tokens, providing a valuable measure for coding problems of varying lengths and complexities. The examples presented in the Qualitative Comparison section are from these datasets.

**Evaluation Metrics.** We employ recall@k, the hit rate of retrieving the gold standard document among top k retrieved documents, as the evaluation metric. Specifically, we retrieve the top-k documents with embeddings closest to the query embedding, and declare success if the gold standard document is among these k documents.   We specifically use k=5, which is currently the most typical use case in downstream applications. The quality for other choices of k also improves across the board.

##### **Voyage-code-2 Excels on Code Retrieval**

In the figure below, we compare `voyage-code-2` against other common embedding models from OpenAI, Cohere, and BAAI/bge on these 11 datasets with recall@5.

![Image 26](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.001-1.png?resize=1024%2C239&quality=80&ssl=1)

![Image 27](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.002.png?resize=1024%2C314&quality=80&ssl=1)

![Image 28](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.003.png?resize=1024%2C267&quality=80&ssl=1)

`voyage-code-2` significantly outperforms all other models, achieving a 14.52% improvement over the next best, OpenAI `text-embedding-3-large`.This performance gap widens on more complex datasets like APPS and CodeChef, which require deeper code understanding. Notably, none of these datasets were encountered during our training.

##### **Voyage Excels in Non-Coding Tasks as Well**

With improved training methods on diverse datasets, `voyage-code-2` also consistently improves over OpenAI, Cohere, and BAAI/bge on domains from technical documents to restaurant reviews. It exceeds OpenAI’s model by 3.03% and Cohere v3 by 4.93% in average results across all datasets.

![Image 29](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.004.png?resize=1024%2C257&quality=80&ssl=1)

Try Voyage Code Embedding
-------------------------

We provide a simple demonstration of using `voyage-code-2` for code retrieval. First, follow [Getting Started](https://docs.voyageai.com/docs/api-key-and-installation) to install the Voyage Python package and get your API key.

Suppose you have a coding question and a corpus of code snippets available for search.

```
query = "Is the function dynamic_programming() implemented using dynamic programming?"

documents = [
    "retriever = KNNRetriever.from_texts(documents, embeddings)",
    "knn = KNeighborsClassifier(n_neighbors=3)",
    "sorted_numbers = sorted(numbers)",
    "def dynamic_programming(): print('yes')",
    "documents_embds = get_embeddings(documents)",
    "response = client.embeddings.create(input = documents, model='text-embedding-ada-002')"
]
```

You can embed/vectorize the query and documents using the Python Voyage AI client:

```
import os
import voyageai

vo = voyageai.Client(os.environ.get("VOYAGE_API_KEY"))

# Get the embedding of the query
query_embedding = vo.embed([query], model="voyage-code-2").embeddings[0]

# Get the embedding of the documents
documents_embeddings = vo.embed(documents, model="voyage-code-2").embeddings
```

If you are working with more than 128 documents, you will need to use a for loop to encode them. You can find the most relevant document using the k\_nearest\_neighbors function with k=1. Check our [Tutorial](https://docs.voyageai.com/docs/quickstart-tutorial) for details of k\_nearest\_neighbors.

```
# Use the nearest neighbor algorithm to find the most relevant document
retrieved_embd, retrieved_embd_index = k_nearest_neighbors(
    query_embedding, documents_embeddings, k=1)
retrieved_doc = [documents[index] for index in retrieved_embd_index]

print(retrieved_doc)
# Output:
# ["def dynamic_programming(): print('yes')"]
```

You can utilize a text generation model like GPT-4 to craft a response based on the provided query and the retrieved document. Please check our [Tutorial](https://docs.voyageai.com/docs/quickstart-tutorial) for details of implementing the RAG chatbot. You can execute the code examples provided above in the [Google Colab](https://colab.research.google.com/drive/14J__2MmaVgxozsF6EQdJTp38Yx_CuAIa?usp=sharing).

Conclusions
-----------

The success of `voyage-code-2` demonstrates that customizing embedding models to a particular industry and/or use case can significantly improve quality. More of these specialized models are to come — finance, healthcare, legal, multilingual, etc. As usual, we give early access to people who are interested in trying these models and providing us with targeted feedback — please contact us at [contact@voyageai.com](mailto:contact@voyageai.com) to join our newsletter and waitlist. We will keep you posted on [Twitter](https://twitter.com/Voyage_AI_) / [LinkedIn](https://www.linkedin.com/company/voyageai/).

## Metadata

```json
{
  "title": "voyage-code-2: Elevate Your Code Retrieval",
  "description": "TL;DR – We are thrilled to introduce voyage-code-2, our latest embedding model specifically tailored for semantic retrieval of codes and related text data from both natural language and code queries. Our comprehensive evaluation, covering 11 code retrieval tasks (derived from popular coding datasets like HumanEval and MBPP), demonstrated a remarkable 14.52% improvement in recall compared…",
  "url": "https://blog.voyageai.com/2024/01/23/voyage-code-2-elevate-your-code-retrieval/",
  "content": "TL;DR – We are thrilled to introduce `` `voyage-code-2```, our latest embedding model specifically tailored for semantic retrieval of **codes** and related text data from both natural language and code queries. Our comprehensive evaluation, covering 11 code retrieval tasks (derived from popular coding datasets like HumanEval and MBPP), demonstrated a remarkable 14.52% improvement in recall compared to competitors, including OpenAI and Cohere. Additionally, we noted consistent gains, averaging 3.03%, across diverse general-purpose text datasets.\n\n[Retrieval-augmented generation (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation/), renowned for its modularity and reliability, stands as the leading approach in integrating proprietary information into LLMs. The retrieval component of RAG first vectorizes a corpus (a collection of documents) into vectors by an embedding model, and then stores and organizes these vectors in vector databases. The quality of embeddings determines the relevancy of the retrieved documents, which in turn decides the response quality of the LLMs. This underscores the importance of developing more refined and domain-specific embedding models, particularly in specialized areas such as coding, finance, law, and healthcare.\n\nThis post presents `` `voyage-code-2```, an embedding model specifically optimized for code-related applications, including semantic code search/retrieval, code completion, and various functions of general code assistants. The superior retrieval performance— 14.52% better than OpenAI ada on code datasets and 3.03% better on general-purpose corpora— is enabled by training on massive code datasets with novel algorithmic techniques, such as advanced loss functions and contrastive pairs. We have also significantly improved both the inference latency and throughput to levels suitable for real-world, interactive production environments and expanded the context window to 16K.\n\nCode Retrieval via Embeddings\n-----------------------------\n\nThe corpus for code-related retrieval tasks is often a collection of code snippets combined or augmented with auxiliary data in natural language. A typical query is either a question phrased in natural language, a snippet of code, or a combination of both. For example, the figure below shows a query and a few code snippets in the corpus.\n\n![Image 21](https://lh7-us.googleusercontent.com/5IwlW0wVPK2DLiRweKqiGvf1HENkOItdRXW3oG61KcDmnOkydYugvR_W6dbi_GlDsocYIIu-yk62zUgREsBmXXfTJQJoaW2vxp8n6sDTyClWtaN9rfd5MohdCn6yZrGEpqinMqlXZk_Br1KmDbvzG5E)\n\nIn this case, the most relevant snippet/document to be retrieved is #1. Note that understanding the relevance between the query and the code snippets requires deep knowledge of the functionality of the code and a semantic understanding of the natural language, going beyond mere keyword matching.\n\nEmbeddings are the most effective way to quickly retrieve relevant code from a large corpus. As shown in the figure below, embedding models turn the code snippets/documents and queries into vectors. Then, we can find the nearest neighbors of the query vector among the document vectors and return the corresponding documents.\n\n![Image 22](https://lh7-us.googleusercontent.com/l8tCa6dccNHV1tAzq2wNLtnU1Gn6OCoYPsBCqG4fd2IRzD2kk9orIAvvXFbFzwhnT3PnOcp6Ol9QgylDnBKSahVBLNBS2BRJq-6f2wjZepolIbBWDzM4FlQ6aCHEYBjpNdvQ_WJcssLlW7RiqHHydFo)\n\nThe figure below also uses real data to demonstrate how queries and documents are represented as high-dimensional vectors, which are then projected into 2D space for visualization purposes. The crucial aspect here is that similar vectors in the Euclidean space should represent semantically related documents and queries. Indeed, code snippets that are related to the same topic (indicated with specific colors) are positioned closely together.\n\n![Image 23](https://lh7-us.googleusercontent.com/WNVLUoI8OBNbDhFuHng4Yha0Vy1e-1cfKFTtNWELyLtphoibfdYddwy7OQ_rR1yeusfR22lNlSA3390UB4R_wnXrRACEzM7gEZ0zFe9dZCE3x_SUFeNEeoFz2pj6vYTNRn8mgatyj3NICLh-36egi5A)\n\nQualitative Comparison\n----------------------\n\nThis section demonstrates, through examples, the enhanced code understanding and code retrieval capabilities of `voyage-code-2` compared to OpenAI Ada.\n\n**Example 1:**\n\n![Image 24](https://lh7-us.googleusercontent.com/KmDubLIy6kyadkAaVEu6VeOHUseCTijTbFc7kbozksCdXwaQ2QmrQsADsGrzXLXXw_3fwrGV5ubPWkFj9PImxzwj6L0XvbZRO3Kec_K5AuTkQQ6sEXzzSnL4VZSRxpXtGnNu5FAKzCOCQT8sfWDnZfs)\n\nBoth `voyage-code-2` and OpenAI ada retrieved snippets that remove occurrences of a given character from the string. However, `` `voyage-code-2``` eliminates the first and last occurrences, aligning with the query, while OpenAI’s Ada removes all occurrences.\n\n**Example 2:**\n\n![Image 25](https://lh7-us.googleusercontent.com/TrC9vteVzC_ayGWEJNDQsnqCCQdHVbkZt9-pFOC0VMiTnyDwC0xLD5elJ17rQ2r0uV7Se8GwPALeoY3EPZjBl1ZlGPp-ARSxvap8UaDQX_FwThg5WKCRzUJ3in9LczhCLBfhOvCgUIkfG7KUGx6eUjU)\n\nThe `voyage-code-2` accurately locates the piece of code that precisely solves the given query. OpenAI ada retrieves a related but incorrect piece of code. It replaces the value of each node in the tree with the sum of all its cousins’ values which deviates from the given query.\n\nThese examples qualitatively demonstrate that `voyage-code-2` has a deeper understanding of the details in the code, enabling a  superior retrieval quality compared to OpenAI ada.\n\nQuantitative Evaluation \n------------------------\n\n**Evaluation Datasets.** We built a suite of 11 datasets for the retrieval quality of code,  using six publicly available datasets that consist of paired coding questions and solutions, including [HumanEval](https://github.com/openai/human-eval), [APPS](https://huggingface.co/datasets/codeparrot/apps), [MBPP](https://huggingface.co/datasets/mbpp), [DS-1000](https://github.com/xlang-ai/DS-1000/tree/main), [Codechef](https://www.codechef.com/contests), and [LeetCode](https://leetcode.com/). Each retrieval dataset comprises a corpus to be retrieved from, typically encompassing all the solutions in the original datasets, and a set of test queries, usually consisting of the collection of questions from the original datasets. The gold standard document(s) for a query question is the corresponding solution(s) in the original dataset.\n\nThe datasets encompass various programming languages and packages, including Python, C++, Java, Matplotlib, Numpy, Pandas, Pytorch, Scipy, Sklearn, and Tensorflow. In total, there are 43,909 query-document pairs. The length of queries ranges from 6 to 1963 tokens, while the length of documents spans from 5  to 2003 tokens, providing a valuable measure for coding problems of varying lengths and complexities. The examples presented in the Qualitative Comparison section are from these datasets.\n\n**Evaluation Metrics.** We employ recall@k, the hit rate of retrieving the gold standard document among top k retrieved documents, as the evaluation metric. Specifically, we retrieve the top-k documents with embeddings closest to the query embedding, and declare success if the gold standard document is among these k documents.   We specifically use k=5, which is currently the most typical use case in downstream applications. The quality for other choices of k also improves across the board.\n\n##### **Voyage-code-2 Excels on Code Retrieval**\n\nIn the figure below, we compare `voyage-code-2` against other common embedding models from OpenAI, Cohere, and BAAI/bge on these 11 datasets with recall@5.\n\n![Image 26](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.001-1.png?resize=1024%2C239&quality=80&ssl=1)\n\n![Image 27](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.002.png?resize=1024%2C314&quality=80&ssl=1)\n\n![Image 28](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.003.png?resize=1024%2C267&quality=80&ssl=1)\n\n`voyage-code-2` significantly outperforms all other models, achieving a 14.52% improvement over the next best, OpenAI `text-embedding-3-large`.This performance gap widens on more complex datasets like APPS and CodeChef, which require deeper code understanding. Notably, none of these datasets were encountered during our training.\n\n##### **Voyage Excels in Non-Coding Tasks as Well**\n\nWith improved training methods on diverse datasets, `voyage-code-2` also consistently improves over OpenAI, Cohere, and BAAI/bge on domains from technical documents to restaurant reviews. It exceeds OpenAI’s model by 3.03% and Cohere v3 by 4.93% in average results across all datasets.\n\n![Image 29](https://i0.wp.com/blog.voyageai.com/wp-content/uploads/2024/01/result-recall5.004.png?resize=1024%2C257&quality=80&ssl=1)\n\nTry Voyage Code Embedding\n-------------------------\n\nWe provide a simple demonstration of using `voyage-code-2` for code retrieval. First, follow [Getting Started](https://docs.voyageai.com/docs/api-key-and-installation) to install the Voyage Python package and get your API key.\n\nSuppose you have a coding question and a corpus of code snippets available for search.\n\n```\nquery = \"Is the function dynamic_programming() implemented using dynamic programming?\"\n\ndocuments = [\n    \"retriever = KNNRetriever.from_texts(documents, embeddings)\",\n    \"knn = KNeighborsClassifier(n_neighbors=3)\",\n    \"sorted_numbers = sorted(numbers)\",\n    \"def dynamic_programming(): print('yes')\",\n    \"documents_embds = get_embeddings(documents)\",\n    \"response = client.embeddings.create(input = documents, model='text-embedding-ada-002')\"\n]\n```\n\nYou can embed/vectorize the query and documents using the Python Voyage AI client:\n\n```\nimport os\nimport voyageai\n\nvo = voyageai.Client(os.environ.get(\"VOYAGE_API_KEY\"))\n\n# Get the embedding of the query\nquery_embedding = vo.embed([query], model=\"voyage-code-2\").embeddings[0]\n\n# Get the embedding of the documents\ndocuments_embeddings = vo.embed(documents, model=\"voyage-code-2\").embeddings\n```\n\nIf you are working with more than 128 documents, you will need to use a for loop to encode them. You can find the most relevant document using the k\\_nearest\\_neighbors function with k=1. Check our [Tutorial](https://docs.voyageai.com/docs/quickstart-tutorial) for details of k\\_nearest\\_neighbors.\n\n```\n# Use the nearest neighbor algorithm to find the most relevant document\nretrieved_embd, retrieved_embd_index = k_nearest_neighbors(\n    query_embedding, documents_embeddings, k=1)\nretrieved_doc = [documents[index] for index in retrieved_embd_index]\n\nprint(retrieved_doc)\n# Output:\n# [\"def dynamic_programming(): print('yes')\"]\n```\n\nYou can utilize a text generation model like GPT-4 to craft a response based on the provided query and the retrieved document. Please check our [Tutorial](https://docs.voyageai.com/docs/quickstart-tutorial) for details of implementing the RAG chatbot. You can execute the code examples provided above in the [Google Colab](https://colab.research.google.com/drive/14J__2MmaVgxozsF6EQdJTp38Yx_CuAIa?usp=sharing).\n\nConclusions\n-----------\n\nThe success of `voyage-code-2` demonstrates that customizing embedding models to a particular industry and/or use case can significantly improve quality. More of these specialized models are to come — finance, healthcare, legal, multilingual, etc. As usual, we give early access to people who are interested in trying these models and providing us with targeted feedback — please contact us at [contact@voyageai.com](mailto:contact@voyageai.com) to join our newsletter and waitlist. We will keep you posted on [Twitter](https://twitter.com/Voyage_AI_) / [LinkedIn](https://www.linkedin.com/company/voyageai/).",
  "publishedTime": "2024-01-23T08:00:00+00:00",
  "usage": {
    "tokens": 2963
  }
}
```
