---
title: T-RAG = RAG + Fine-Tuning + Entity Detection - Cobus Greyling - Medium
description: Large Language Models (LLMs) are increasingly utilised across various domains, including question answering over private enterprise documents, where data security and robustness are paramount…
url: https://cobusgreyling.medium.com/t-rag-rag-fine-tuning-entity-detection-9a5aaa01e437
timestamp: 2025-01-20T15:58:29.732Z
domain: cobusgreyling.medium.com
path: t-rag-rag-fine-tuning-entity-detection-9a5aaa01e437
---

# T-RAG = RAG + Fine-Tuning + Entity Detection - Cobus Greyling - Medium


Large Language Models (LLMs) are increasingly utilised across various domains, including question answering over private enterprise documents, where data security and robustness are paramount…


## Content

The T-RAG approach is premised on combining RAG architecture with an open-source fine-tuned LLM and an entities tree vector database. The focus is on contextual retrieval.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 18: Cobus Greyling](https://miro.medium.com/v2/resize:fill:88:88/1*nzfAEuujMN0s-aK6R7RcNg.jpeg)](https://cobusgreyling.medium.com/?source=post_page---byline--9a5aaa01e437--------------------------------)

Introduction
------------

Large Language Models (LLMs) are increasingly utilised across various domains, including **question answering** over **private enterprise documents**, where **data security** and **robustness** are paramount.

Retrieval-Augmented Generation (**RAG**) is a prominent framework for building such applications, but ensuring its robustness requires extensive customisation.

This study shares experiences in deploying an LLM application for question answering over private organisational documents, using a system called **Tree-RAG (T-RAG)** that incorporates **entity hierarchies** for improved performance.

Evaluations demonstrate the effectiveness of this approach, providing valuable insights for real-world LLM applications.

Data Privacy
------------

Security risks are a primary concern due to the sensitive nature of these documents, making it impractical to use **proprietary LLM models** over publich APIs, to avoid data leakage risks.

This calls for the use of **open-source models** that can be deployed on-premise.

Additionally, limited computational resources and smaller training datasets based on available documents present challenges.

Furthermore, ensuring reliable and accurate responses to user queries adds complexity, necessitating extensive customisation and decision-making in deploying robust applications in such environments.

Take-Aways
----------

What interested me in this study is that the researches develop an application that integrates **Retrieval-Augmented Generation (RAG)** with a **fine-tuned open-source Large Language Model (LLM)** for generating responses. This model is trained using an instruction dataset derived from the organisation’s documents.

They introduce a novel evaluation metric, termed **Correct-Verbose**, designed to assess the quality of generated responses. This metric evaluates responses based on their correctness while also considering the inclusion of additional relevant information beyond the scope of the original question.

T-RAG
-----

Below the workflow of Tree-RAG (T-RAG)…

For a given user query, the vector database is searched for the relevant document chunks, the chunk serves as the contextual reference for LLM in-context learning.

If the query mentions any organisational related entities, information regarding the entities is extracted from the **_entities tree_** and added to the **_context_**. The fine-tuned Llama-2 7B model generates a response from the presented data.

> A feature of T-RAG is the inclusion of an entities tree in addition to the vector database for context retrieval.

Entities Tree
-------------

One distinguishing aspect of T-RAG is its incorporation of an entities tree alongside the vector database for context retrieval. The entities tree stores details regarding the organization’s entities and their hierarchical arrangement. Each node within this tree represents an entity, with parent nodes indicating their respective group memberships.

During the retrieval process, the framework leverage the **entities tree** to enhance the context retrieved from the vector database.

_The procedure for entity tree search and context generation unfolds as follows:_

1.  Initially, a parser module scans the user query for keywords corresponding to entity names within the organisation.
2.  Upon identifying one or more matches, details regarding each matched entity are extracted from the tree.
3.  These details are transformed into textual statements that furnish information about the entity and its position within the organisation’s hierarchy.
4.  Subsequently, this information is amalgamated with the document chunks retrieved from the vector database to construct the context.
5.  By adopting this approach, the model gains access to pertinent information about entities and their hierarchical positioning within the organisation when users inquire about them.

Considering the image above, the retrieval process for context generation involves utilising an illustrative example from an organisational chart to demonstrate how tree search and retrieval are executed.

In addition to fetching contextual documents, a spaCy library is used with custom rules to identify named entities within the organisation.

If the query contains one or more such entities, relevant information regarding the entity’s hierarchical location is extracted from the tree and transformed into textual statements. These statements are then incorporated into the context along with the retrieved documents.

However, if the user’s query does not mention any entities, the tree search is omitted, and only the context from the retrieved documents is utilised.

In Conclusion
-------------

I found this study fascinating in the sense that it combines RAG and also fine-tuning. While making use of an open-sourced model hosted on premise to address issues of data-privacy, while simultaneously solving for inference latency, token usage cost and regional and geographic availability.

It is also interesting how entities are used via spaCy framework for entity search and context generation. The fact that this was not just a research piece, but lessons learned based on experiences building an LLM application for real-world use.

**_⭐️ Follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on Large Language Models ⭐️_**

![Image 19](https://miro.medium.com/v2/resize:fit:700/0*4fhM_IeU0f1_HTOF.png)

_I’m currently the_ [_Chief Evangelist_](https://www.linkedin.com/in/cobusgreyling) _@_ [_Kore AI_](https://blog.kore.ai/)_. I explore & write about all things at the intersection of AI & language; ranging from_ [_LLMs_](https://cobusgreyling.medium.com/the-large-language-model-landscape-9da7ee17710b)_,_ [_Chatbots_](https://cobusgreyling.medium.com/the-five-categories-of-conversational-ai-f2410beeaf2f)_,_ [_Voicebots_](https://cobusgreyling.medium.com/three-key-voicebot-design-considerations-7bf25444dfec)_,_ [_Development Frameworks_](https://cobusgreyling.medium.com/emerging-large-language-model-llm-application-architecture-cba0e7862037)_,_ [_Data-Centric latent spaces_](https://cobusgreyling.medium.com/testing-complex-utterances-with-the-co-here-humanfirst-integration-145ab4eedd84) _& more._

![Image 20](https://miro.medium.com/v2/resize:fit:700/0*VsJ7ciiPu_1PCKbr.png)

![Image 21](https://miro.medium.com/v2/resize:fit:370/0*D2Tlw5Y5diPHEcJD.jpeg)

[LinkedIn](https://www.linkedin.com/in/cobusgreyling)

![Image 22](https://miro.medium.com/v2/resize:fit:700/0*3a27sfPh-8JrafRt.png)

## Metadata

```json
{
  "title": "T-RAG = RAG + Fine-Tuning + Entity Detection - Cobus Greyling - Medium",
  "description": "Large Language Models (LLMs) are increasingly utilised across various domains, including question answering over private enterprise documents, where data security and robustness are paramount…",
  "url": "https://cobusgreyling.medium.com/t-rag-rag-fine-tuning-entity-detection-9a5aaa01e437",
  "content": "The T-RAG approach is premised on combining RAG architecture with an open-source fine-tuned LLM and an entities tree vector database. The focus is on contextual retrieval.\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[![Image 18: Cobus Greyling](https://miro.medium.com/v2/resize:fill:88:88/1*nzfAEuujMN0s-aK6R7RcNg.jpeg)](https://cobusgreyling.medium.com/?source=post_page---byline--9a5aaa01e437--------------------------------)\n\nIntroduction\n------------\n\nLarge Language Models (LLMs) are increasingly utilised across various domains, including **question answering** over **private enterprise documents**, where **data security** and **robustness** are paramount.\n\nRetrieval-Augmented Generation (**RAG**) is a prominent framework for building such applications, but ensuring its robustness requires extensive customisation.\n\nThis study shares experiences in deploying an LLM application for question answering over private organisational documents, using a system called **Tree-RAG (T-RAG)** that incorporates **entity hierarchies** for improved performance.\n\nEvaluations demonstrate the effectiveness of this approach, providing valuable insights for real-world LLM applications.\n\nData Privacy\n------------\n\nSecurity risks are a primary concern due to the sensitive nature of these documents, making it impractical to use **proprietary LLM models** over publich APIs, to avoid data leakage risks.\n\nThis calls for the use of **open-source models** that can be deployed on-premise.\n\nAdditionally, limited computational resources and smaller training datasets based on available documents present challenges.\n\nFurthermore, ensuring reliable and accurate responses to user queries adds complexity, necessitating extensive customisation and decision-making in deploying robust applications in such environments.\n\nTake-Aways\n----------\n\nWhat interested me in this study is that the researches develop an application that integrates **Retrieval-Augmented Generation (RAG)** with a **fine-tuned open-source Large Language Model (LLM)** for generating responses. This model is trained using an instruction dataset derived from the organisation’s documents.\n\nThey introduce a novel evaluation metric, termed **Correct-Verbose**, designed to assess the quality of generated responses. This metric evaluates responses based on their correctness while also considering the inclusion of additional relevant information beyond the scope of the original question.\n\nT-RAG\n-----\n\nBelow the workflow of Tree-RAG (T-RAG)…\n\nFor a given user query, the vector database is searched for the relevant document chunks, the chunk serves as the contextual reference for LLM in-context learning.\n\nIf the query mentions any organisational related entities, information regarding the entities is extracted from the **_entities tree_** and added to the **_context_**. The fine-tuned Llama-2 7B model generates a response from the presented data.\n\n> A feature of T-RAG is the inclusion of an entities tree in addition to the vector database for context retrieval.\n\nEntities Tree\n-------------\n\nOne distinguishing aspect of T-RAG is its incorporation of an entities tree alongside the vector database for context retrieval. The entities tree stores details regarding the organization’s entities and their hierarchical arrangement. Each node within this tree represents an entity, with parent nodes indicating their respective group memberships.\n\nDuring the retrieval process, the framework leverage the **entities tree** to enhance the context retrieved from the vector database.\n\n_The procedure for entity tree search and context generation unfolds as follows:_\n\n1.  Initially, a parser module scans the user query for keywords corresponding to entity names within the organisation.\n2.  Upon identifying one or more matches, details regarding each matched entity are extracted from the tree.\n3.  These details are transformed into textual statements that furnish information about the entity and its position within the organisation’s hierarchy.\n4.  Subsequently, this information is amalgamated with the document chunks retrieved from the vector database to construct the context.\n5.  By adopting this approach, the model gains access to pertinent information about entities and their hierarchical positioning within the organisation when users inquire about them.\n\nConsidering the image above, the retrieval process for context generation involves utilising an illustrative example from an organisational chart to demonstrate how tree search and retrieval are executed.\n\nIn addition to fetching contextual documents, a spaCy library is used with custom rules to identify named entities within the organisation.\n\nIf the query contains one or more such entities, relevant information regarding the entity’s hierarchical location is extracted from the tree and transformed into textual statements. These statements are then incorporated into the context along with the retrieved documents.\n\nHowever, if the user’s query does not mention any entities, the tree search is omitted, and only the context from the retrieved documents is utilised.\n\nIn Conclusion\n-------------\n\nI found this study fascinating in the sense that it combines RAG and also fine-tuning. While making use of an open-sourced model hosted on premise to address issues of data-privacy, while simultaneously solving for inference latency, token usage cost and regional and geographic availability.\n\nIt is also interesting how entities are used via spaCy framework for entity search and context generation. The fact that this was not just a research piece, but lessons learned based on experiences building an LLM application for real-world use.\n\n**_⭐️ Follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on Large Language Models ⭐️_**\n\n![Image 19](https://miro.medium.com/v2/resize:fit:700/0*4fhM_IeU0f1_HTOF.png)\n\n_I’m currently the_ [_Chief Evangelist_](https://www.linkedin.com/in/cobusgreyling) _@_ [_Kore AI_](https://blog.kore.ai/)_. I explore & write about all things at the intersection of AI & language; ranging from_ [_LLMs_](https://cobusgreyling.medium.com/the-large-language-model-landscape-9da7ee17710b)_,_ [_Chatbots_](https://cobusgreyling.medium.com/the-five-categories-of-conversational-ai-f2410beeaf2f)_,_ [_Voicebots_](https://cobusgreyling.medium.com/three-key-voicebot-design-considerations-7bf25444dfec)_,_ [_Development Frameworks_](https://cobusgreyling.medium.com/emerging-large-language-model-llm-application-architecture-cba0e7862037)_,_ [_Data-Centric latent spaces_](https://cobusgreyling.medium.com/testing-complex-utterances-with-the-co-here-humanfirst-integration-145ab4eedd84) _& more._\n\n![Image 20](https://miro.medium.com/v2/resize:fit:700/0*VsJ7ciiPu_1PCKbr.png)\n\n![Image 21](https://miro.medium.com/v2/resize:fit:370/0*D2Tlw5Y5diPHEcJD.jpeg)\n\n[LinkedIn](https://www.linkedin.com/in/cobusgreyling)\n\n![Image 22](https://miro.medium.com/v2/resize:fit:700/0*3a27sfPh-8JrafRt.png)",
  "publishedTime": "2024-02-15T09:08:22.436Z",
  "usage": {
    "tokens": 1485
  }
}
```
