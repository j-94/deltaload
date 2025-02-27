---
title: Embedding API
description: Top-performing multimodal multilingual long-context embeddings for search, RAG, agents applications.
url: https://jina.ai/embeddings/
timestamp: 2025-01-20T16:14:08.911Z
domain: jina.ai
path: embeddings
---

# Embedding API


Top-performing multimodal multilingual long-context embeddings for search, RAG, agents applications.


## Content

Embedding API
===============
  

[_![Image 110](https://jina.ai/Jina%20-%20Dark.svg)_](https://jina.ai/)

_search__reorder_

[News](https://jina.ai/news)[Models](https://jina.ai/models)

Products

_keyboard\_arrow\_down_

[![Image 111](https://jina.ai/assets/reader-D06QTWF1.svg) Reader Convert any URL to Markdown for better grounding LLMs.](https://jina.ai/reader)[![Image 112](https://jina.ai/assets/embedding-DzEuY8_E.svg) Embeddings World-class multimodal multilingual embeddings.](https://jina.ai/embeddings)[![Image 113](https://jina.ai/assets/reranker-DudpN0Ck.svg) Reranker World-class neural retriever for maximizing search relevancy.](https://jina.ai/reranker)[![Image 114](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9) Classifier Zero-shot and few-shot classification for image and text.](https://jina.ai/classifier)[![Image 115](blob:https://jina.ai/d9cb1deb4878909b05c9cd0f15af4aac) Segmenter Cut long text into chunks and do tokenization.](https://jina.ai/segmenter)

* * *

[API Docs Auto codegen for your copilot IDE or LLM _open\_in\_new_](https://docs.jina.ai/)

* * *

* * *

Company

_keyboard\_arrow\_down_

[About us](https://jina.ai/about-us)[Contact sales](https://jina.ai/contact-sales)[Intern program](https://jina.ai/internship)[Join us _open\_in\_new_](https://career.jina.ai/)[Download logo _open\_in\_new_](https://jina.ai/logo-Jina-1024.zip)[Terms & Conditions](https://jina.ai/legal)

* * *

* * *

[Log in _login_](https://jina.ai/api-dashboard?login=true)

_language_

Embeddings

_celebration_ clip-v2 release!


============================================

Top-performing multimodal multilingual long-context embeddings for search, RAG, agents applications.

_code_API

* * *

_attach\_money_Pricing

Embedding API
-------------

Try our world-class embedding models to improve your search and RAG systems. Start with a free trial!

_login_

_key_

API Key & Billing

_code_

Usage

_more\_horiz_

More

_service\_toolbox_Tools_arrow\_drop\_down_

_chevron\_left__chevron\_right_

* * *

[_home_](https://jina.ai/embeddings)

Auto preview

[_forum_ Raise issue](https://huggingface.co/jinaai/undefined/discussions)

_cloud_On CSP_arrow\_drop\_down_

[_help\_outline_FAQ](https://jina.ai/embeddings#faq)

[_api_](https://api.jina.ai/redoc#tag/embeddings)

[Status](https://status.jina.ai/)

_chevron\_left__chevron\_right_

* * *

_![Image 116](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Select embeddings

_arrow\_drop\_down_

L2 normalization

Scales the embedding so its Euclidean (L2) norm becomes 1, preserving direction. Useful when downstream involves dot-product, classification, visualization.

Returning data type

Besides the float, you can ask it to return as binary for faster vector retrieval, or as base64 encoding for faster transmission.

Default (as float)

_arrow\_drop\_down_

* * *

Example inputs

Change them and see how the response changes!

1

_text\_fields_

2

_text\_fields_

3

_text\_fields_

4

_text\_fields_

5

_text\_fields_

* * *

_upload_

Request

Bash

Language

_arrow\_drop\_down_

```
curl https://api.jina.ai/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d @- <<EOFEOF
  {
    "normalized": true,
    "embedding_type": "float",
    "input": [
        "Organic skincare for sensitive skin with aloe vera and chamomile: Imagine the soothing embrace of nature with our organic skincare range, crafted specifically for sensitive skin. Infused with the calming properties of aloe vera and chamomile, each product provides gentle nourishment and protection. Say goodbye to irritation and hello to a glowing, healthy complexion.",
        "Bio-Hautpflege für empfindliche Haut mit Aloe Vera und Kamille: Erleben Sie die wohltuende Wirkung unserer Bio-Hautpflege, speziell für empfindliche Haut entwickelt. Mit den beruhigenden Eigenschaften von Aloe Vera und Kamille pflegen und schützen unsere Produkte Ihre Haut auf natürliche Weise. Verabschieden Sie sich von Hautirritationen und genießen Sie einen strahlenden Teint.",
        "Cuidado de la piel orgánico para piel sensible con aloe vera y manzanilla: Descubre el poder de la naturaleza con nuestra línea de cuidado de la piel orgánico, diseñada especialmente para pieles sensibles. Enriquecidos con aloe vera y manzanilla, estos productos ofrecen una hidratación y protección suave. Despídete de las irritaciones y saluda a una piel radiante y saludable.",
        "针对敏感肌专门设计的天然有机护肤产品：体验由芦荟和洋甘菊提取物带来的自然呵护。我们的护肤产品特别为敏感肌设计，温和滋润，保护您的肌肤不受刺激。让您的肌肤告别不适，迎来健康光彩。",
        "新しいメイクのトレンドは鮮やかな色と革新的な技術に焦点を当てています: 今シーズンのメイクアップトレンドは、大胆な色彩と革新的な技術に注目しています。ネオンアイライナーからホログラフィックハイライターまで、クリエイティビティを解き放ち、毎回ユニークなルックを演出しましょう。"
    ]
  }
EOFEOF
```

_content\_copy_

* * *

_send_GET RESPONSE

* * *

_key_

API key

_visibility\_off__content\_copy_

* * *

Available tokens

0 _sync_

This is your unique key. Store it securely!

clip-v2: Multilingual Multimodal Embeddings
-------------------------------------------

jina-clip-v2 is a 0.9B CLIP-style model that brings three major advances: multilingual support for 89 languages, high image resolution at 512x512, and Matryoshka representation learning for truncated embeddings.

![Image 117](https://jina.ai/assets/bg-clip-v2-release-CDKPPehK.svg)

[Read Release Note_arrow\_forward_](https://jina.ai/news/jina-clip-v2-multilingual-multimodal-embeddings-for-text-and-images)

v3: Frontier Multilingual Embeddings
------------------------------------

`jina-embeddings-v3` is a frontier multilingual text embedding model with 570M parameters and 8192 token-length, outperforming the latest proprietary embeddings from OpenAI and Cohere on MTEB. Read our blog post and research paper below.

![Image 118](https://jina.ai/assets/bg-v3-release-CCihp62V.svg)

[Three Ways to Purchase](https://jina.ai/embeddings/#pricing)
-------------------------------------------------------------

Subscribe to our API, purchase through cloud providers, or obtain a commercial license for your organization.

[_radio\_button\_unchecked_ _encrypted_ With a commercial license for on-prem use Require 100% control and privacy? Purchase a commercial license to use our models on-premises.](https://jina.ai/api-dashboard/license-config?login=true)

_radio\_button\_unchecked_

_cloud_

With **3** cloud service providers

Using AWS or Azure? You can deploy our models directly on your company's cloud platform and handle billing through the CSP account.

_![Image 119](https://jina.ai/assets/aws-_fgBVdQm.svg)_ AWS SageMaker

_![Image 120](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Embeddings

_![Image 121](https://jina.ai/assets/reranker-DudpN0Ck.svg)_

Reranker

_![Image 122](blob:https://jina.ai/80ab35293a3a07b87f51f4a06f113c84)_ Microsoft Azure

_![Image 123](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Embeddings

_![Image 124](https://jina.ai/assets/reranker-DudpN0Ck.svg)_

Reranker

_![Image 125](blob:https://jina.ai/eb8eef1dd7c8e8e7a38cd1da22c52b42)_ Google Cloud

_![Image 126](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Embeddings

_![Image 127](https://jina.ai/assets/reranker-DudpN0Ck.svg)_

Reranker

_radio\_button\_checked_

_![Image 128](https://jina.ai/J-active.svg)_

With Jina Search Foundation API

The easiest way to access all of our products. Top-up tokens as you go.

_content\_copy_

Enter the API key you wish to recharge

_error_

_visibility\_off_

Top up this API key with more tokens

Depending on your location, you may be charged in USD, EUR, or other currencies. Taxes may apply.

Please input the right API key to top up

Understand the rate limit

Rate limits are the maximum number of requests that can be made to an API within a minute per IP address (RPM). Find out more about the rate limits for each product and tier below.

_keyboard\_arrow\_down_

Rate Limit

Rate limits are tracked in two ways: **RPM** (requests per minute) and **TPM** (tokens per minute). Limits are enforced per IP and can be reached based on whichever threshold—RPM or TPM—is hit first.

Columns

_arrow\_drop\_down_

|  | Product | API Endpoint | Description_arrow\_upward_ | w/o API Key | w/ API Key | w/ Premium API Key | Average Latency | Token Usage Counting | Allowed Request |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 
![Image 129](https://jina.ai/assets/embedding-DzEuY8_E.svg)



 | Embedding API | `https://api.jina.ai/v1/embeddings` | Convert text/images to fixed-length vectors | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | 

_bolt_

depends on the input size

_help_



 | Count the number of tokens in the input request. | POST |
| 

![Image 130](https://jina.ai/assets/reranker-DudpN0Ck.svg)



 | Reranker API | `https://api.jina.ai/v1/rerank` | Tokenize and segment long text | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | 

_bolt_

depends on the input size

_help_



 | Count the number of tokens in the input request. | POST |
| 

![Image 131](https://jina.ai/assets/reader-D06QTWF1.svg)



 | Reader API | `https://r.jina.ai` | Convert URL to LLM-friendly text | 20 RPM | 200 RPM | 1000 RPM | 4.6s | Count the number of tokens in the output response. | GET/POST |
| 

![Image 132](https://jina.ai/assets/reader-D06QTWF1.svg)



 | Reader API | `https://s.jina.ai` | Search the web and convert results to LLM-friendly text | _block_ | 40 RPM | 100 RPM | 8.7s | Count the number of tokens in the output response. | GET/POST |
| 

![Image 133](https://jina.ai/assets/reader-D06QTWF1.svg)



 | Reader API | `https://g.jina.ai` | Grounding a statement with web knowledge | _block_ | 10 RPM | 30 RPM | 22.7s | Count the total number of tokens in the whole process. | GET/POST |
| 

![Image 134](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)



 | Classifier API (Zero-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using zero-shot classification | _block_ | 200 RPM & 500,000 TPM | 1,000 RPM & 3,000,000 TPM | 

_bolt_

depends on the input size





 | Tokens counted as: input\_tokens + label\_tokens | POST |
| 

![Image 135](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)



 | Classifier API (Few-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using a trained few-shot classifier | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | 

_bolt_

depends on the input size





 | Tokens counted as: input\_tokens | POST |
| 

![Image 136](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)



 | Classifier API | `https://api.jina.ai/v1/train` | Train a classifier using labeled examples | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | 

_bolt_

depends on the input size





 | Tokens counted as: input\_tokens × num\_iters | POST |
| 

![Image 137](blob:https://jina.ai/d9cb1deb4878909b05c9cd0f15af4aac)



 | Segmenter API | `https://segment.jina.ai` | Tokenize and segment long text | 20 RPM | 200 RPM | 1,000 RPM | 0.3s | Token is not counted as usage. | GET/POST |

Auto-Recharge for Low Token Balance

Recommended for uninterrupted service in production. When your token balance drops below the set threshold, we will automatically recharge your saved payment method for the last purchased package, until the threshold is met.

_check_

< 1M Tokens

Recharge if

_arrow\_drop\_down_

On-premises deployment
----------------------

Deploy Jina Embeddings models in AWS Sagemaker and Microsoft Azure, and soon in Google Cloud Services, or contact our sales team to get customized Kubernetes deployments for your Virtual Private Cloud and on-premises servers.

_![Image 138](https://jina.ai/assets/aws-_fgBVdQm.svg)_ AWS SageMaker

_![Image 139](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Embeddings

_![Image 140](https://jina.ai/assets/reranker-DudpN0Ck.svg)_

Reranker

_![Image 141](blob:https://jina.ai/80ab35293a3a07b87f51f4a06f113c84)_ Microsoft Azure

_![Image 142](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Embeddings

_![Image 143](https://jina.ai/assets/reranker-DudpN0Ck.svg)_

Reranker

_![Image 144](blob:https://jina.ai/eb8eef1dd7c8e8e7a38cd1da22c52b42)_ Google Cloud

_![Image 145](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Embeddings

_![Image 146](https://jina.ai/assets/reranker-DudpN0Ck.svg)_

Reranker

![Image 147](https://jina.ai/assets/pattern-developers-DbqNZCU0.svg)

API Integrations

Our Embedding API is natively integrated with various renowned databases, vector stores, RAG, and LLMOps frameworks. To begin, just copy and paste your API key into any of the listed integrations for a quick and seamless start.

Vector Store

LLMOps

RAG

Observability

_open\_in\_new_

![Image 148](blob:https://jina.ai/5d4fd576e1a99efcf818b6400f55ea0c)

MongoDB

_open\_in\_new_

![Image 149](blob:https://jina.ai/711c5e97e31a01671dc4cd90f6fb481c)

DataStax

_open\_in\_new_

![Image 150](blob:https://jina.ai/15e045ccedc0716dbfd6cb5eef7ff23e)

Qdrant

_open\_in\_new_

![Image 151](blob:https://jina.ai/7c760bc7c0ad6e8413170ff55f5a06c3)

Pinecone

_open\_in\_new_

![Image 152](blob:https://jina.ai/8fd1ae510a407f283ecef750fb5fdb5c)

Chroma

_open\_in\_new_

![Image 153](https://jina.ai/assets/icon-Weaviate-CfbkPZsU.svg)

Weaviate

_open\_in\_new_

![Image 154](https://jina.ai/assets/icon-Milvus-Bz_cf8R2.png)

Milvus

_open\_in\_new_

![Image 155](https://jina.ai/assets/icon-Epsilla-BPYuTwuZ.png)

Epsilla

_open\_in\_new_

![Image 156](blob:https://jina.ai/a642d726a6a7acaf3fe5c1a1f0063602)

MyScale

_open\_in\_new_

![Image 157](https://jina.ai/assets/icon-LlamaIndex-CKyGrd9a.png)

LlamaIndex

_open\_in\_new_

![Image 158](blob:https://jina.ai/fa7c060a926af05a1ae3316f9c3979ac)

Haystack

_open\_in\_new_

![Image 159](https://jina.ai/assets/icon-Langchain-hPS1w007.png)

Langchain

_open\_in\_new_

![Image 160](https://jina.ai/assets/icon-Dify-BQetVg9h.png)

Dify

_open\_in\_new_

![Image 161](blob:https://jina.ai/66f3050f2532ed18edfe6d12c392a6c9)

SuperDuperDB

_open\_in\_new_

![Image 162](blob:https://jina.ai/63fdb680914ef545db95f7fd33882987)

DashVector

_open\_in\_new_

![Image 163](https://jina.ai/assets/icon-portkey-BY2A2xDT.png)

Portkey

_open\_in\_new_

![Image 164](blob:https://jina.ai/662c92214f72a6bbc15b22775f0cf6a6)

Baseten

_open\_in\_new_

![Image 165](https://jina.ai/assets/icon-tidb-vhSazXAM.png)

TiDB

_open\_in\_new_

![Image 166](https://jina.ai/assets/icon-lancedb-r57HMIMm.png)

LanceDB

_open\_in\_new_

![Image 167](https://jina.ai/assets/icon-carbon-ERjBNjcr.svg)

Carbon

Our Publications
----------------

Understand how our frontier search models were trained from scratch, check out our latest publications. Meet our team at EMNLP, SIGIR, ICLR, NeurIPS, and ICML!

[![Image 168](https://jina.ai/assets/paper-10-DGYfAPtO.png) _![Image 169](https://jina.ai/arxiv_logo.svg)_ arXiv December 17, 2024 AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark](https://arxiv.org/abs/2412.13102)[![Image 170](https://jina.ai/assets/paper-9-CvIlokq5.png) _![Image 171](https://jina.ai/arxiv_logo.svg)_ arXiv December 12, 2024 jina-clip-v2: Multilingual Multimodal Embeddings for Text and Images](https://arxiv.org/abs/2412.08802)[![Image 172](https://jina.ai/assets/paper-8-Dej1pELH.png) ECIR 2025 September 18, 2024 jina-embeddings-v3: Multilingual Embeddings With Task LoRA](https://arxiv.org/abs/2409.10173)[![Image 173](https://jina.ai/assets/paper-7-CEHkaOhr.png) _![Image 174](https://jina.ai/arxiv_logo.svg)_ arXiv September 07, 2024 Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models](https://arxiv.org/abs/2409.04701)[![Image 175](https://jina.ai/assets/paper-6-DFggRUH_.png) EMNLP 2024 August 30, 2024 Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever](https://arxiv.org/abs/2408.16672)[![Image 176](https://jina.ai/assets/paper_5-9fAb8aKn.png) _![Image 177](https://jina.ai/arxiv_logo.svg)_ arXiv June 21, 2024 Leveraging Passage Embeddings for Efficient Listwise Reranking with Large Language Models](https://arxiv.org/abs/2406.14848)[![Image 178](https://jina.ai/assets/paper_4-9CY2yaP0.png) ICML 2024 May 30, 2024 Jina CLIP: Your CLIP Model Is Also Your Text Retriever](https://arxiv.org/abs/2405.20204)[![Image 179](https://jina.ai/assets/paper_3-CaeXIy5O.png) _![Image 180](https://jina.ai/arxiv_logo.svg)_ arXiv February 26, 2024 Multi-Task Contrastive Learning for 8192-Token Bilingual Text Embeddings](https://arxiv.org/abs/2402.17016)[![Image 181](https://jina.ai/assets/paper_1-BH6f05Wp.png) _![Image 182](https://jina.ai/arxiv_logo.svg)_ arXiv October 30, 2023 Jina Embeddings 2: 8192-Token General-Purpose Text Embeddings for Long Documents](https://arxiv.org/abs/2310.19923)[![Image 183](https://jina.ai/assets/paper_2-Dz0iDvcJ.png) EMNLP 2023 July 20, 2023 Jina Embeddings: A Novel Set of High-Performance Sentence Embedding Models](https://arxiv.org/abs/2307.11224)

10 publications in total.

Learning about Embeddings
-------------------------

Where to start with embeddings? We've got you covered. Learn about embeddings from the ground up with our comprehensive guide.

[![Image 184: Three abstract figures in white, gray, and pink on matching cubes placed on a colorful checkered surface against a green back](https://jina-ai-gmbh.ghost.io/content/images/2024/12/banner-order.png) December 17, 2024 • 12 minutes read Text Embeddings Fail to Capture Word Order and How to Fix It Text embedding models struggle with capturing subtle linguistic nuances like word order, directional relationships, temporal sequences, causal connections, comparisons, and negation. Understanding these challenges is key to improving model performance. ![Image 185: Bo Wang](https://jina-ai-gmbh.ghost.io/content/images/2022/11/4B483B29-E306-402B-8635-64866C458406.jpeg) ![Image 186: Alex C-G](https://jina-ai-gmbh.ghost.io/content/images/2022/09/alex.jpg)](https://jina.ai/news/text-embeddings-fail-to-capture-word-order-and-how-to-fix-it)

[![Image 187: David Hockney artwork of a hand holding a rod with three colored spheres on a blue-toned background.](https://jina-ai-gmbh.ghost.io/content/images/2024/12/test-time-compute.jpg) December 12, 2024 • 12 minutes read Scaling Test-Time Compute For Embedding Models Better results scale with compute—more on learning, more on search. A good pretrained model takes you far, but test-time compute takes you further. It's time to recognize this paradigm of test-time compute, even for embedding models. ![Image 188: Han Xiao](https://jina-ai-gmbh.ghost.io/content/images/2022/10/Untitled-2.png)](https://jina.ai/news/scaling-test-time-compute-for-embedding-models)

[![Image 189: Two hands, each holding a key positioned to interact with each other, depicted against a deep blue background.](https://jina-ai-gmbh.ghost.io/content/images/2024/11/banner--1-.jpg) November 27, 2024 • 10 minutes read Watermarking Text with Embedding Models to Protect Against Content Theft You use our embedding models to do what? This might be the most "out-of-domain" applications of embeddings we learned at EMNLP 2024. ![Image 190: Han Xiao](https://jina-ai-gmbh.ghost.io/content/images/2022/10/Untitled-2.png)](https://jina.ai/news/watermarking-text-with-embedding-models-to-protect-against-content-theft)

[![Image 191: Digital number "2" displayed in a mosaic of colorful squares against a dark background, creating a futuristic vibe.](https://jina-ai-gmbh.ghost.io/content/images/2024/11/clipv2.png) November 21, 2024 • 9 minutes read Jina CLIP v2: Multilingual Multimodal Embeddings for Text and Images Jina-CLIP v2, a 0.9B multimodal embedding model with multilingual support of 89 languages, high image resolution at 512x512, and Matryoshka representations. ![Image 192: Jina AI](https://jina-ai-gmbh.ghost.io/content/images/2022/08/Jjqb-JeY_400x400.jpg)](https://jina.ai/news/jina-clip-v2-multilingual-multimodal-embeddings-for-text-and-images)

_circle__circle__circle__circle__circle__circle__circle__circle__circle_

Comparison of Reranker, Vector Search, and BM25
-----------------------------------------------

The table below provides a comprehensive comparison of the Reranker, Vector/Embeddings Search, and BM25, highlighting their strengths and weaknesses across various categories.

|  | Reranker | Vector Search | BM25 |
| --- | --- | --- | --- |
| **Best For** | Enhanced search precision and relevance | Initial, rapid filtering | General text retrieval across wide-ranging queries |
| **Granularity** | Detailed: Sub-document and query segment | Broad: Entire documents | Intermediate: Various text segments |
| **Query Time Complexity** | High | Medium | Low |
| **Indexing Time Complexity** | Not required | High | Low, utilizes pre-built index |
| **Training Time Complexity** | High | High | Not required |
| **Search Quality** | Superior for nuanced queries | Balanced between efficiency and accuracy | Consistent and reliable for a broad set of queries |
| **Strengths** | Highly accurate with deep contextual understanding | Quick and efficient, with moderate accuracy | Highly scalable, with established efficacy |
|  | [_![Image 193](https://jina.ai/assets/reranker-DudpN0Ck.svg)_Try reranker API for free](https://jina.ai/reranker) | [_![Image 194](https://jina.ai/assets/embedding-DzEuY8_E.svg)_Try embedding API for free](https://jina.ai/embeddings) |  |

The Evolution of Embeddings Poster
----------------------------------

Discover the ideal poster for your space, featuring captivating infographics or breathtaking visuals tracing the evolution of text embedding models since 1950.

[Learn how we made it](https://jina.ai/news/the-1950-2024-text-embeddings-evolution-poster)

* * *

[_shopping\_cart_Buy a hard copy](https://buy.stripe.com/cN2aHS4Ax5F19DqfZ7)

![Image 195](https://jina.ai/assets/jyMgQBGpxVh-Dv4riOlz.png)

FAQ
---

### [How to get my API key?](https://jina.ai/embeddings/#get-api-key)

 video\_not\_supported

### [What's the rate limit?](https://jina.ai/embeddings/#rate-limit)

Rate Limit

Rate limits are tracked in two ways: **RPM** (requests per minute) and **TPM** (tokens per minute). Limits are enforced per IP and can be reached based on whichever threshold—RPM or TPM—is hit first.

Columns

_arrow\_drop\_down_

|  | Product | API Endpoint | Description_arrow\_upward_ | w/o API Key | w/ API Key | w/ Premium API Key | Average Latency | Token Usage Counting | Allowed Request |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 
![Image 196](https://jina.ai/assets/embedding-DzEuY8_E.svg)



 | Embedding API | `https://api.jina.ai/v1/embeddings` | Convert text/images to fixed-length vectors | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | 

_bolt_

depends on the input size

_help_



 | Count the number of tokens in the input request. | POST |
| 

![Image 197](https://jina.ai/assets/reranker-DudpN0Ck.svg)



 | Reranker API | `https://api.jina.ai/v1/rerank` | Tokenize and segment long text | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | 

_bolt_

depends on the input size

_help_



 | Count the number of tokens in the input request. | POST |
| 

![Image 198](https://jina.ai/assets/reader-D06QTWF1.svg)



 | Reader API | `https://r.jina.ai` | Convert URL to LLM-friendly text | 20 RPM | 200 RPM | 1000 RPM | 4.6s | Count the number of tokens in the output response. | GET/POST |
| 

![Image 199](https://jina.ai/assets/reader-D06QTWF1.svg)



 | Reader API | `https://s.jina.ai` | Search the web and convert results to LLM-friendly text | _block_ | 40 RPM | 100 RPM | 8.7s | Count the number of tokens in the output response. | GET/POST |
| 

![Image 200](https://jina.ai/assets/reader-D06QTWF1.svg)



 | Reader API | `https://g.jina.ai` | Grounding a statement with web knowledge | _block_ | 10 RPM | 30 RPM | 22.7s | Count the total number of tokens in the whole process. | GET/POST |
| 

![Image 201](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)



 | Classifier API (Zero-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using zero-shot classification | _block_ | 200 RPM & 500,000 TPM | 1,000 RPM & 3,000,000 TPM | 

_bolt_

depends on the input size





 | Tokens counted as: input\_tokens + label\_tokens | POST |
| 

![Image 202](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)



 | Classifier API (Few-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using a trained few-shot classifier | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | 

_bolt_

depends on the input size





 | Tokens counted as: input\_tokens | POST |
| 

![Image 203](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)



 | Classifier API | `https://api.jina.ai/v1/train` | Train a classifier using labeled examples | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | 

_bolt_

depends on the input size





 | Tokens counted as: input\_tokens × num\_iters | POST |
| 

![Image 204](blob:https://jina.ai/d9cb1deb4878909b05c9cd0f15af4aac)



 | Segmenter API | `https://segment.jina.ai` | Tokenize and segment long text | 20 RPM | 200 RPM | 1,000 RPM | 0.3s | Token is not counted as usage. | GET/POST |

### [Do I need a commercial license?](https://jina.ai/embeddings/#cc-self-check)

CC BY-NC License Self-Check

* * *

_play\_arrow_

Are you using our official API or official images on Azure or AWS?

_play\_arrow_

_done_

Yes

_play\_arrow_

Are you using a paid API key or free trial key?

_play\_arrow_

_done_

Paid API key

No restrictions. Use as per your current agreement.

_play\_arrow_

_info_

Free API key

Free trial key can be only used for non-commercial purposes. Please purchase a paid package for commercial use.

_play\_arrow_

Are you using our official model images on AWS and Azure?

No restrictions. Use as per your current agreement.

_play\_arrow_

_close_

No

_play\_arrow_

Are you using these models?

jina-clip-v2

jina-embeddings-v3

jina-reranker-v2-base-multilingual

jina-colbert-v2

reader-lm-1.5b

reader-lm-0.5b

ReaderLM-v2

_play\_arrow_

_close_

No

No restrictions apply.

_play\_arrow_

_done_

Yes

_play\_arrow_

Is your use commercial?

_play\_arrow_

_question\_mark_

Not sure

_play\_arrow_

Are you:

_play\_arrow_

Using it for personal or hobby projects?

This is non-commercial. You can use the models freely.

_play\_arrow_

A for-profit company using it internally?

This is commercial. Contact our sales team.

[Contact sales](https://jina.ai/contact-sales)

_play\_arrow_

An educational institution using it for teaching?

This is typically non-commercial. You can use the models freely.

_play\_arrow_

A non-profit or NGO using it for your mission?

This is typically non-commercial, but check with us if unsure.

[Contact sales](https://jina.ai/contact-sales)

_play\_arrow_

Using it in a product or service you sell?

This is commercial. Contact our sales team.

[Contact sales](https://jina.ai/contact-sales)

_play\_arrow_

A government entity using it for public services?

This may be commercial. Please contact us for clarification.

[Contact sales](https://jina.ai/contact-sales)

_play\_arrow_

_close_

No

You can use the models freely.

_play\_arrow_

_done_

Yes

Contact our sales team for licensing.

[Contact sales](https://jina.ai/contact-sales)

### [Other questions](https://jina.ai/embeddings/#faq)

Embeddings-related common questions

_![Image 205](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

How were the jina-embeddings-v3 models trained?

_keyboard\_arrow\_down_

For detailed information on our training processes, data sources, and evaluations, please refer to our technical report available on arXiv.

[_launch_arXiv](https://arxiv.org/abs/2409.10173)

_![Image 206](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

What are the jina-clip models, and can I use them for text and image search?

_keyboard\_arrow\_down_

Jina CLIP `jina-clip-v2` is an advanced multimodal embedding model that supports text-text, text-image, image-image, and image-text retrieval tasks. Unlike the original OpenAI CLIP, which struggles with text-text search, Jina CLIP excels as a text retriever. `jina-clip-v2` offers a 3% performance improvement over `jina-clip-v1` in both text-image and text-text retrieval tasks, supports 89 languages for multilingual image retrieval, processes higher resolution images (512x512), and reduces storage requirements with Matryoshka representations. You can read more about it in our tech report.

[_launch_arXiv](https://arxiv.org/abs/2412.08802)

_![Image 207](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Which languages do your models support?

_keyboard\_arrow\_down_

As of its release on September 18, 2024, `jina-embeddings-v3` is the best multilingual model and ranks 2nd on the MTEB English leaderboard for models with fewer than 1 billion parameters. v3 supports a total of 89 languages, including the top 30 with the best performance: Arabic, Bengali, Chinese, Danish, Dutch, English, Finnish, French, Georgian, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Latvian, Norwegian, Polish, Portuguese, Romanian, Russian, Slovak, Spanish, Swedish, Thai, Turkish, Ukrainian, Urdu, and Vietnamese. For more details, please refer to the `jina-embeddings-v3` tech report.

[_launch_arXiv](https://arxiv.org/abs/2409.10173)

_![Image 208](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

What is the maximum length for a single sentence input?

_keyboard\_arrow\_down_

Our models allow for an input length of up to 8192 tokens, which is significantly higher than most other models. A token can range from a single character, like 'a', to an entire word, such as 'apple'. The total number of characters that can be input depends on the length and complexity of the words used. This extended input capability enables our `jina-embeddings-v3` and `jina-clip` models to perform more comprehensive text analysis and achieve higher accuracy in context understanding, especially for extensive textual data.

_![Image 209](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

What is the maximum number of sentences I can include in a single request?

_keyboard\_arrow\_down_

A single API call can process up to 2048 sentences or texts, facilitating extensive text analysis in one request.

_![Image 210](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

How do I send images to the jina-clip models?

_keyboard\_arrow\_down_

You can use either `url` or `bytes` in the `input` field of the API request. For `url`, provide the URL of the image you want to process. For `bytes`, encode the image in base64 format and include it in the request. The model will return the embeddings of the image in the response.

_![Image 211](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

How do Jina Embeddings models compare to OpenAI's and Cohere's latest embeddings?

_keyboard\_arrow\_down_

In evaluations on the MTEB English, Multilingual, and LongEmbed benchmarks, `jina-embeddings-v3` outperforms the latest proprietary embeddings from OpenAI and Cohere on English tasks, and surpasses `multilingual-e5-large-instruct` across all multilingual tasks. With a default output dimension of 1024, users can truncate the embedding dimensions down to 32 without sacrificing performance, thanks to the integration of Matryoshka Representation Learning (MRL).

_![Image 212](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

How seamless is the transition from OpenAI's text-embedding-3-large to your solution?

_keyboard\_arrow\_down_

The transition is streamlined, as [our API endpoint](https://api.jina.ai/v1/embeddings), matches the input and output JSON schemas of OpenAI’s `text-embedding-3-large` model. This compatibility ensures users can easily replace the OpenAI model with ours when using OpenAI’s endpoint.

_![Image 213](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

How tokens are calculated when using jina-clip models?

_keyboard\_arrow\_down_

Tokens are calculated based on the text length and image size. For text in the request, tokens are counted in the standard way. For images, the following steps are conducted: 1. Tile Size: Each image is divided into tiles. For `jina-clip-v2`, tiles are 512x512 pixels, while for `jina-clip-v1`, tiles are 224x224 pixels. 2. Coverage: The number of tiles required to cover the input image is calculated. Even if the image dimensions are not perfectly divisible by the tile size, partial tiles are counted as full tiles. 3. Total Tiles: The total number of tiles covering the image determines the cost. For example, a 600x600 pixel image would be covered by 2x2 tiles (4 tiles) in v2 and 3x3 tiles (9 tiles) in v1. 4. Cost Calculation: For `jina-clip-v2`, each tile costs 4000 tokens, while for `jina-clip-v1`, each tile costs 1000 tokens. Example: For an image with dimensions 600x600 pixels: • With `jina-clip-v2` • The image is divided into 512x512 pixel tiles. • The total number of tiles required is 2 (horizontal) x 2 (vertical) = 4 tiles. • The cost for `jina-clip-v2` will be 4\*4000 = 16000 tokens. • With `jina-clip-v1` • The image is divided into 224x224 pixel tiles. • The total number of tiles required is 3 (horizontal) x 3 (vertical) = 9 tiles. • The cost for jina-clip-v1 will be 9\*1000 = 9000 tokens.

_![Image 214](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Do you provide models for embedding images or audio?

_keyboard\_arrow\_down_

Yes, `jina-clip-v2` and `jina-clip-v1` can embed both images and texts. Embedding models on more modalities will be announced soon!

_![Image 215](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Can Jina Embedding models be fine-tuned with private or company data?

_keyboard\_arrow\_down_

For inquiries about fine-tuning our models with specific data, please contact us to discuss your requirements. We are open to exploring how our models can be adapted to meet your needs.

[Contact](https://jina.ai/contact-sales)

_![Image 216](https://jina.ai/assets/embedding-DzEuY8_E.svg)_

Can your endpoints be hosted privately on AWS, Azure, or GCP?

_keyboard\_arrow\_down_

Yes, our services are available on AWS, Azure, and GCP marketplaces. If you have specific requirements, please contact us at sales AT jina.ai.

[_launch_AWS SageMaker](https://aws.amazon.com/marketplace/seller-profile?id=seller-stch2ludm6vgy)[_launch_Google Cloud](https://console.cloud.google.com/marketplace/browse?q=jina&pli=1&inv=1&invt=AbmydQ)[_launch_Microsoft Azure](https://azuremarketplace.microsoft.com/en-US/marketplace/apps?page=1&search=jina)

API-related common questions

_code_

Can I use the same API key for reader, embedding, reranking, classifying and fine-tuning APIs?

_keyboard\_arrow\_down_

Yes, the same API key is valid for all search foundation products from Jina AI. This includes the reader, embedding, reranking, classifying and fine-tuning APIs, with tokens shared between the all services.

_code_

Can I monitor the token usage of my API key?

_keyboard\_arrow\_down_

Yes, token usage can be monitored in the 'API Key & Billing' tab by entering your API key, allowing you to view the recent usage history and remaining tokens. If you have logged in to the API dashboard, these details can also be viewed in the 'Manage API Key' tab.

_code_

What should I do if I forget my API key?

_keyboard\_arrow\_down_

If you have misplaced a topped-up key and wish to retrieve it, please contact support AT jina.ai with your registered email for assistance. It's recommended to log in to keep your API key securely stored and easily accessible.

[Contact](https://jina.ai/contact-sales)

_code_

Do API keys expire?

_keyboard\_arrow\_down_

No, our API keys do not have an expiration date. However, if you suspect your key has been compromised and wish to retire it, please contact our support team for assistance. You can also revoke your key in [the API Key Management dashboard](https://jina.ai/api-dashboard).

[Contact](https://jina.ai/contact-sales)

_code_

Can I transfer tokens between API keys?

_keyboard\_arrow\_down_

Yes, you can transfer tokens from a premium key to another. After logging into your account on [the API Key Management dashboard](https://jina.ai/api-dashboard), use the settings of the key you want to transfer out to move all remaining paid tokens.

_code_

Can I revoke my API key?

_keyboard\_arrow\_down_

Yes, you can revoke your API key if you believe it has been compromised. Revoking a key will immediately disable it for all users who have stored it, and all remaining balance and associated properties will be permanently unusable. If the key is a premium key, you have the option to transfer the remaining paid balance to another key before revocation. Notice that this action cannot be undone. To revoke a key, go to the key settings in [the API Key Management dashboard](https://jina.ai/api-dashboard).

_code_

Why is the first request for some models slow?

_keyboard\_arrow\_down_

This is because our serverless architecture offloads certain models during periods of low usage. The initial request activates or 'warms up' the model, which may take a few seconds. After this initial activation, subsequent requests process much more quickly.

_code_

Is user input data used for training your models?

_keyboard\_arrow\_down_

We adhere to a strict privacy policy and do not use user input data for training our models. We are also SOC 2 Type I and Type II compliant, ensuring high standards of security and privacy.

Billing-related common questions

_attach\_money_

Is billing based on the number of sentences or requests?

_keyboard\_arrow\_down_

Our pricing model is based on the total number of tokens processed, allowing users the flexibility to allocate these tokens across any number of sentences, offering a cost-effective solution for diverse text analysis requirements.

_attach\_money_

Is there a free trial available for new users?

_keyboard\_arrow\_down_

We offer a welcoming free trial to new users, which includes one million tokens for use with any of our models, facilitated by an auto-generated API key. Once the free token limit is reached, users can easily purchase additional tokens for their API keys via the 'Buy tokens' tab.

_attach\_money_

Are tokens charged for failed requests?

_keyboard\_arrow\_down_

No, tokens are not deducted for failed requests.

_attach\_money_

What payment methods are accepted?

_keyboard\_arrow\_down_

Payments are processed through Stripe, supporting a variety of payment methods including credit cards, Google Pay, and PayPal for your convenience.

_attach\_money_

Is invoicing available for token purchases?

_keyboard\_arrow\_down_

Yes, an invoice will be issued to the email address associated with your Stripe account upon the purchase of tokens.

Offices

_location\_on_

Sunnyvale, CA

710 Lakeway Dr, Ste 200, Sunnyvale, CA 94085, USA

_location\_on_

Berlin, Germany (HQ)

Prinzessinnenstraße 19-20, 10969 Berlin, Germany

_location\_on_

Beijing, China

Level 5, Building 6, No.48 Haidian West St. Beijing, China

_location\_on_

Shenzhen, China

402 Floor 4, Fu'an Technology Building, Shenzhen, China

Search Foundation

[Reader](https://jina.ai/reader)[Embeddings](https://jina.ai/embeddings)[Reranker](https://jina.ai/reranker)[Classifier](https://jina.ai/classifier)[Segmenter](https://jina.ai/segmenter)[API Documentation](https://docs.jina.ai/)

Get Jina API key

[Rate Limit](https://jina.ai/contact-sales#rate-limit)[API Status](https://status.jina.ai/)

Company

[About us](https://jina.ai/about-us)[Contact sales](https://jina.ai/contact-sales)[Newsroom](https://jina.ai/news)[Intern program](https://jina.ai/internship)[Join us _open\_in\_new_](https://career.jina.ai/)[Download logo _open\_in\_new_](https://jina.ai/logo-Jina-1024.zip)

Terms

[Security](https://jina.ai/legal#security-as-company-value)[Terms & Conditions](https://jina.ai/legal/#terms-and-conditions)[Privacy](https://jina.ai/legal/#privacy-policy)[Manage Cookies](javascript:UC_UI.showSecondLayer();)[![Image 217](https://jina.ai/21972-312_SOC_NonCPA_Blk.svg)](https://app.eu.vanta.com/jinaai/trust/vz7f4mohp0847aho84lmva)

[](https://x.com/jinaAI_)[](https://www.linkedin.com/company/jinaai/)[](https://github.com/jina-ai)[_![Image 218](https://jina.ai/huggingface_logo.svg)_](https://huggingface.co/jinaai) [](https://discord.jina.ai/)[_email_](mailto:support@jina.ai)

Jina AI © 2020-2025.

## Metadata

```json
{
  "title": "Embedding API",
  "description": "Top-performing multimodal multilingual long-context embeddings for search, RAG, agents applications.",
  "url": "https://jina.ai/embeddings/",
  "content": "Embedding API\n===============\n  \n\n[_![Image 110](https://jina.ai/Jina%20-%20Dark.svg)_](https://jina.ai/)\n\n_search__reorder_\n\n[News](https://jina.ai/news)[Models](https://jina.ai/models)\n\nProducts\n\n_keyboard\\_arrow\\_down_\n\n[![Image 111](https://jina.ai/assets/reader-D06QTWF1.svg) Reader Convert any URL to Markdown for better grounding LLMs.](https://jina.ai/reader)[![Image 112](https://jina.ai/assets/embedding-DzEuY8_E.svg) Embeddings World-class multimodal multilingual embeddings.](https://jina.ai/embeddings)[![Image 113](https://jina.ai/assets/reranker-DudpN0Ck.svg) Reranker World-class neural retriever for maximizing search relevancy.](https://jina.ai/reranker)[![Image 114](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9) Classifier Zero-shot and few-shot classification for image and text.](https://jina.ai/classifier)[![Image 115](blob:https://jina.ai/d9cb1deb4878909b05c9cd0f15af4aac) Segmenter Cut long text into chunks and do tokenization.](https://jina.ai/segmenter)\n\n* * *\n\n[API Docs Auto codegen for your copilot IDE or LLM _open\\_in\\_new_](https://docs.jina.ai/)\n\n* * *\n\n* * *\n\nCompany\n\n_keyboard\\_arrow\\_down_\n\n[About us](https://jina.ai/about-us)[Contact sales](https://jina.ai/contact-sales)[Intern program](https://jina.ai/internship)[Join us _open\\_in\\_new_](https://career.jina.ai/)[Download logo _open\\_in\\_new_](https://jina.ai/logo-Jina-1024.zip)[Terms & Conditions](https://jina.ai/legal)\n\n* * *\n\n* * *\n\n[Log in _login_](https://jina.ai/api-dashboard?login=true)\n\n_language_\n\nEmbeddings\n\n_celebration_ clip-v2 release!\n\n\n============================================\n\nTop-performing multimodal multilingual long-context embeddings for search, RAG, agents applications.\n\n_code_API\n\n* * *\n\n_attach\\_money_Pricing\n\nEmbedding API\n-------------\n\nTry our world-class embedding models to improve your search and RAG systems. Start with a free trial!\n\n_login_\n\n_key_\n\nAPI Key & Billing\n\n_code_\n\nUsage\n\n_more\\_horiz_\n\nMore\n\n_service\\_toolbox_Tools_arrow\\_drop\\_down_\n\n_chevron\\_left__chevron\\_right_\n\n* * *\n\n[_home_](https://jina.ai/embeddings)\n\nAuto preview\n\n[_forum_ Raise issue](https://huggingface.co/jinaai/undefined/discussions)\n\n_cloud_On CSP_arrow\\_drop\\_down_\n\n[_help\\_outline_FAQ](https://jina.ai/embeddings#faq)\n\n[_api_](https://api.jina.ai/redoc#tag/embeddings)\n\n[Status](https://status.jina.ai/)\n\n_chevron\\_left__chevron\\_right_\n\n* * *\n\n_![Image 116](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nSelect embeddings\n\n_arrow\\_drop\\_down_\n\nL2 normalization\n\nScales the embedding so its Euclidean (L2) norm becomes 1, preserving direction. Useful when downstream involves dot-product, classification, visualization.\n\nReturning data type\n\nBesides the float, you can ask it to return as binary for faster vector retrieval, or as base64 encoding for faster transmission.\n\nDefault (as float)\n\n_arrow\\_drop\\_down_\n\n* * *\n\nExample inputs\n\nChange them and see how the response changes!\n\n1\n\n_text\\_fields_\n\n2\n\n_text\\_fields_\n\n3\n\n_text\\_fields_\n\n4\n\n_text\\_fields_\n\n5\n\n_text\\_fields_\n\n* * *\n\n_upload_\n\nRequest\n\nBash\n\nLanguage\n\n_arrow\\_drop\\_down_\n\n```\ncurl https://api.jina.ai/v1/embeddings \\\n  -H \"Content-Type: application/json\" \\\n  -H \"Authorization: Bearer \" \\\n  -d @- <<EOFEOF\n  {\n    \"normalized\": true,\n    \"embedding_type\": \"float\",\n    \"input\": [\n        \"Organic skincare for sensitive skin with aloe vera and chamomile: Imagine the soothing embrace of nature with our organic skincare range, crafted specifically for sensitive skin. Infused with the calming properties of aloe vera and chamomile, each product provides gentle nourishment and protection. Say goodbye to irritation and hello to a glowing, healthy complexion.\",\n        \"Bio-Hautpflege für empfindliche Haut mit Aloe Vera und Kamille: Erleben Sie die wohltuende Wirkung unserer Bio-Hautpflege, speziell für empfindliche Haut entwickelt. Mit den beruhigenden Eigenschaften von Aloe Vera und Kamille pflegen und schützen unsere Produkte Ihre Haut auf natürliche Weise. Verabschieden Sie sich von Hautirritationen und genießen Sie einen strahlenden Teint.\",\n        \"Cuidado de la piel orgánico para piel sensible con aloe vera y manzanilla: Descubre el poder de la naturaleza con nuestra línea de cuidado de la piel orgánico, diseñada especialmente para pieles sensibles. Enriquecidos con aloe vera y manzanilla, estos productos ofrecen una hidratación y protección suave. Despídete de las irritaciones y saluda a una piel radiante y saludable.\",\n        \"针对敏感肌专门设计的天然有机护肤产品：体验由芦荟和洋甘菊提取物带来的自然呵护。我们的护肤产品特别为敏感肌设计，温和滋润，保护您的肌肤不受刺激。让您的肌肤告别不适，迎来健康光彩。\",\n        \"新しいメイクのトレンドは鮮やかな色と革新的な技術に焦点を当てています: 今シーズンのメイクアップトレンドは、大胆な色彩と革新的な技術に注目しています。ネオンアイライナーからホログラフィックハイライターまで、クリエイティビティを解き放ち、毎回ユニークなルックを演出しましょう。\"\n    ]\n  }\nEOFEOF\n```\n\n_content\\_copy_\n\n* * *\n\n_send_GET RESPONSE\n\n* * *\n\n_key_\n\nAPI key\n\n_visibility\\_off__content\\_copy_\n\n* * *\n\nAvailable tokens\n\n0 _sync_\n\nThis is your unique key. Store it securely!\n\nclip-v2: Multilingual Multimodal Embeddings\n-------------------------------------------\n\njina-clip-v2 is a 0.9B CLIP-style model that brings three major advances: multilingual support for 89 languages, high image resolution at 512x512, and Matryoshka representation learning for truncated embeddings.\n\n![Image 117](https://jina.ai/assets/bg-clip-v2-release-CDKPPehK.svg)\n\n[Read Release Note_arrow\\_forward_](https://jina.ai/news/jina-clip-v2-multilingual-multimodal-embeddings-for-text-and-images)\n\nv3: Frontier Multilingual Embeddings\n------------------------------------\n\n`jina-embeddings-v3` is a frontier multilingual text embedding model with 570M parameters and 8192 token-length, outperforming the latest proprietary embeddings from OpenAI and Cohere on MTEB. Read our blog post and research paper below.\n\n![Image 118](https://jina.ai/assets/bg-v3-release-CCihp62V.svg)\n\n[Three Ways to Purchase](https://jina.ai/embeddings/#pricing)\n-------------------------------------------------------------\n\nSubscribe to our API, purchase through cloud providers, or obtain a commercial license for your organization.\n\n[_radio\\_button\\_unchecked_ _encrypted_ With a commercial license for on-prem use Require 100% control and privacy? Purchase a commercial license to use our models on-premises.](https://jina.ai/api-dashboard/license-config?login=true)\n\n_radio\\_button\\_unchecked_\n\n_cloud_\n\nWith **3** cloud service providers\n\nUsing AWS or Azure? You can deploy our models directly on your company's cloud platform and handle billing through the CSP account.\n\n_![Image 119](https://jina.ai/assets/aws-_fgBVdQm.svg)_ AWS SageMaker\n\n_![Image 120](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nEmbeddings\n\n_![Image 121](https://jina.ai/assets/reranker-DudpN0Ck.svg)_\n\nReranker\n\n_![Image 122](blob:https://jina.ai/80ab35293a3a07b87f51f4a06f113c84)_ Microsoft Azure\n\n_![Image 123](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nEmbeddings\n\n_![Image 124](https://jina.ai/assets/reranker-DudpN0Ck.svg)_\n\nReranker\n\n_![Image 125](blob:https://jina.ai/eb8eef1dd7c8e8e7a38cd1da22c52b42)_ Google Cloud\n\n_![Image 126](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nEmbeddings\n\n_![Image 127](https://jina.ai/assets/reranker-DudpN0Ck.svg)_\n\nReranker\n\n_radio\\_button\\_checked_\n\n_![Image 128](https://jina.ai/J-active.svg)_\n\nWith Jina Search Foundation API\n\nThe easiest way to access all of our products. Top-up tokens as you go.\n\n_content\\_copy_\n\nEnter the API key you wish to recharge\n\n_error_\n\n_visibility\\_off_\n\nTop up this API key with more tokens\n\nDepending on your location, you may be charged in USD, EUR, or other currencies. Taxes may apply.\n\nPlease input the right API key to top up\n\nUnderstand the rate limit\n\nRate limits are the maximum number of requests that can be made to an API within a minute per IP address (RPM). Find out more about the rate limits for each product and tier below.\n\n_keyboard\\_arrow\\_down_\n\nRate Limit\n\nRate limits are tracked in two ways: **RPM** (requests per minute) and **TPM** (tokens per minute). Limits are enforced per IP and can be reached based on whichever threshold—RPM or TPM—is hit first.\n\nColumns\n\n_arrow\\_drop\\_down_\n\n|  | Product | API Endpoint | Description_arrow\\_upward_ | w/o API Key | w/ API Key | w/ Premium API Key | Average Latency | Token Usage Counting | Allowed Request |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| \n![Image 129](https://jina.ai/assets/embedding-DzEuY8_E.svg)\n\n\n\n | Embedding API | `https://api.jina.ai/v1/embeddings` | Convert text/images to fixed-length vectors | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n_help_\n\n\n\n | Count the number of tokens in the input request. | POST |\n| \n\n![Image 130](https://jina.ai/assets/reranker-DudpN0Ck.svg)\n\n\n\n | Reranker API | `https://api.jina.ai/v1/rerank` | Tokenize and segment long text | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n_help_\n\n\n\n | Count the number of tokens in the input request. | POST |\n| \n\n![Image 131](https://jina.ai/assets/reader-D06QTWF1.svg)\n\n\n\n | Reader API | `https://r.jina.ai` | Convert URL to LLM-friendly text | 20 RPM | 200 RPM | 1000 RPM | 4.6s | Count the number of tokens in the output response. | GET/POST |\n| \n\n![Image 132](https://jina.ai/assets/reader-D06QTWF1.svg)\n\n\n\n | Reader API | `https://s.jina.ai` | Search the web and convert results to LLM-friendly text | _block_ | 40 RPM | 100 RPM | 8.7s | Count the number of tokens in the output response. | GET/POST |\n| \n\n![Image 133](https://jina.ai/assets/reader-D06QTWF1.svg)\n\n\n\n | Reader API | `https://g.jina.ai` | Grounding a statement with web knowledge | _block_ | 10 RPM | 30 RPM | 22.7s | Count the total number of tokens in the whole process. | GET/POST |\n| \n\n![Image 134](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)\n\n\n\n | Classifier API (Zero-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using zero-shot classification | _block_ | 200 RPM & 500,000 TPM | 1,000 RPM & 3,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n\n\n\n\n | Tokens counted as: input\\_tokens + label\\_tokens | POST |\n| \n\n![Image 135](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)\n\n\n\n | Classifier API (Few-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using a trained few-shot classifier | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n\n\n\n\n | Tokens counted as: input\\_tokens | POST |\n| \n\n![Image 136](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)\n\n\n\n | Classifier API | `https://api.jina.ai/v1/train` | Train a classifier using labeled examples | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n\n\n\n\n | Tokens counted as: input\\_tokens × num\\_iters | POST |\n| \n\n![Image 137](blob:https://jina.ai/d9cb1deb4878909b05c9cd0f15af4aac)\n\n\n\n | Segmenter API | `https://segment.jina.ai` | Tokenize and segment long text | 20 RPM | 200 RPM | 1,000 RPM | 0.3s | Token is not counted as usage. | GET/POST |\n\nAuto-Recharge for Low Token Balance\n\nRecommended for uninterrupted service in production. When your token balance drops below the set threshold, we will automatically recharge your saved payment method for the last purchased package, until the threshold is met.\n\n_check_\n\n< 1M Tokens\n\nRecharge if\n\n_arrow\\_drop\\_down_\n\nOn-premises deployment\n----------------------\n\nDeploy Jina Embeddings models in AWS Sagemaker and Microsoft Azure, and soon in Google Cloud Services, or contact our sales team to get customized Kubernetes deployments for your Virtual Private Cloud and on-premises servers.\n\n_![Image 138](https://jina.ai/assets/aws-_fgBVdQm.svg)_ AWS SageMaker\n\n_![Image 139](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nEmbeddings\n\n_![Image 140](https://jina.ai/assets/reranker-DudpN0Ck.svg)_\n\nReranker\n\n_![Image 141](blob:https://jina.ai/80ab35293a3a07b87f51f4a06f113c84)_ Microsoft Azure\n\n_![Image 142](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nEmbeddings\n\n_![Image 143](https://jina.ai/assets/reranker-DudpN0Ck.svg)_\n\nReranker\n\n_![Image 144](blob:https://jina.ai/eb8eef1dd7c8e8e7a38cd1da22c52b42)_ Google Cloud\n\n_![Image 145](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nEmbeddings\n\n_![Image 146](https://jina.ai/assets/reranker-DudpN0Ck.svg)_\n\nReranker\n\n![Image 147](https://jina.ai/assets/pattern-developers-DbqNZCU0.svg)\n\nAPI Integrations\n\nOur Embedding API is natively integrated with various renowned databases, vector stores, RAG, and LLMOps frameworks. To begin, just copy and paste your API key into any of the listed integrations for a quick and seamless start.\n\nVector Store\n\nLLMOps\n\nRAG\n\nObservability\n\n_open\\_in\\_new_\n\n![Image 148](blob:https://jina.ai/5d4fd576e1a99efcf818b6400f55ea0c)\n\nMongoDB\n\n_open\\_in\\_new_\n\n![Image 149](blob:https://jina.ai/711c5e97e31a01671dc4cd90f6fb481c)\n\nDataStax\n\n_open\\_in\\_new_\n\n![Image 150](blob:https://jina.ai/15e045ccedc0716dbfd6cb5eef7ff23e)\n\nQdrant\n\n_open\\_in\\_new_\n\n![Image 151](blob:https://jina.ai/7c760bc7c0ad6e8413170ff55f5a06c3)\n\nPinecone\n\n_open\\_in\\_new_\n\n![Image 152](blob:https://jina.ai/8fd1ae510a407f283ecef750fb5fdb5c)\n\nChroma\n\n_open\\_in\\_new_\n\n![Image 153](https://jina.ai/assets/icon-Weaviate-CfbkPZsU.svg)\n\nWeaviate\n\n_open\\_in\\_new_\n\n![Image 154](https://jina.ai/assets/icon-Milvus-Bz_cf8R2.png)\n\nMilvus\n\n_open\\_in\\_new_\n\n![Image 155](https://jina.ai/assets/icon-Epsilla-BPYuTwuZ.png)\n\nEpsilla\n\n_open\\_in\\_new_\n\n![Image 156](blob:https://jina.ai/a642d726a6a7acaf3fe5c1a1f0063602)\n\nMyScale\n\n_open\\_in\\_new_\n\n![Image 157](https://jina.ai/assets/icon-LlamaIndex-CKyGrd9a.png)\n\nLlamaIndex\n\n_open\\_in\\_new_\n\n![Image 158](blob:https://jina.ai/fa7c060a926af05a1ae3316f9c3979ac)\n\nHaystack\n\n_open\\_in\\_new_\n\n![Image 159](https://jina.ai/assets/icon-Langchain-hPS1w007.png)\n\nLangchain\n\n_open\\_in\\_new_\n\n![Image 160](https://jina.ai/assets/icon-Dify-BQetVg9h.png)\n\nDify\n\n_open\\_in\\_new_\n\n![Image 161](blob:https://jina.ai/66f3050f2532ed18edfe6d12c392a6c9)\n\nSuperDuperDB\n\n_open\\_in\\_new_\n\n![Image 162](blob:https://jina.ai/63fdb680914ef545db95f7fd33882987)\n\nDashVector\n\n_open\\_in\\_new_\n\n![Image 163](https://jina.ai/assets/icon-portkey-BY2A2xDT.png)\n\nPortkey\n\n_open\\_in\\_new_\n\n![Image 164](blob:https://jina.ai/662c92214f72a6bbc15b22775f0cf6a6)\n\nBaseten\n\n_open\\_in\\_new_\n\n![Image 165](https://jina.ai/assets/icon-tidb-vhSazXAM.png)\n\nTiDB\n\n_open\\_in\\_new_\n\n![Image 166](https://jina.ai/assets/icon-lancedb-r57HMIMm.png)\n\nLanceDB\n\n_open\\_in\\_new_\n\n![Image 167](https://jina.ai/assets/icon-carbon-ERjBNjcr.svg)\n\nCarbon\n\nOur Publications\n----------------\n\nUnderstand how our frontier search models were trained from scratch, check out our latest publications. Meet our team at EMNLP, SIGIR, ICLR, NeurIPS, and ICML!\n\n[![Image 168](https://jina.ai/assets/paper-10-DGYfAPtO.png) _![Image 169](https://jina.ai/arxiv_logo.svg)_ arXiv December 17, 2024 AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark](https://arxiv.org/abs/2412.13102)[![Image 170](https://jina.ai/assets/paper-9-CvIlokq5.png) _![Image 171](https://jina.ai/arxiv_logo.svg)_ arXiv December 12, 2024 jina-clip-v2: Multilingual Multimodal Embeddings for Text and Images](https://arxiv.org/abs/2412.08802)[![Image 172](https://jina.ai/assets/paper-8-Dej1pELH.png) ECIR 2025 September 18, 2024 jina-embeddings-v3: Multilingual Embeddings With Task LoRA](https://arxiv.org/abs/2409.10173)[![Image 173](https://jina.ai/assets/paper-7-CEHkaOhr.png) _![Image 174](https://jina.ai/arxiv_logo.svg)_ arXiv September 07, 2024 Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models](https://arxiv.org/abs/2409.04701)[![Image 175](https://jina.ai/assets/paper-6-DFggRUH_.png) EMNLP 2024 August 30, 2024 Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever](https://arxiv.org/abs/2408.16672)[![Image 176](https://jina.ai/assets/paper_5-9fAb8aKn.png) _![Image 177](https://jina.ai/arxiv_logo.svg)_ arXiv June 21, 2024 Leveraging Passage Embeddings for Efficient Listwise Reranking with Large Language Models](https://arxiv.org/abs/2406.14848)[![Image 178](https://jina.ai/assets/paper_4-9CY2yaP0.png) ICML 2024 May 30, 2024 Jina CLIP: Your CLIP Model Is Also Your Text Retriever](https://arxiv.org/abs/2405.20204)[![Image 179](https://jina.ai/assets/paper_3-CaeXIy5O.png) _![Image 180](https://jina.ai/arxiv_logo.svg)_ arXiv February 26, 2024 Multi-Task Contrastive Learning for 8192-Token Bilingual Text Embeddings](https://arxiv.org/abs/2402.17016)[![Image 181](https://jina.ai/assets/paper_1-BH6f05Wp.png) _![Image 182](https://jina.ai/arxiv_logo.svg)_ arXiv October 30, 2023 Jina Embeddings 2: 8192-Token General-Purpose Text Embeddings for Long Documents](https://arxiv.org/abs/2310.19923)[![Image 183](https://jina.ai/assets/paper_2-Dz0iDvcJ.png) EMNLP 2023 July 20, 2023 Jina Embeddings: A Novel Set of High-Performance Sentence Embedding Models](https://arxiv.org/abs/2307.11224)\n\n10 publications in total.\n\nLearning about Embeddings\n-------------------------\n\nWhere to start with embeddings? We've got you covered. Learn about embeddings from the ground up with our comprehensive guide.\n\n[![Image 184: Three abstract figures in white, gray, and pink on matching cubes placed on a colorful checkered surface against a green back](https://jina-ai-gmbh.ghost.io/content/images/2024/12/banner-order.png) December 17, 2024 • 12 minutes read Text Embeddings Fail to Capture Word Order and How to Fix It Text embedding models struggle with capturing subtle linguistic nuances like word order, directional relationships, temporal sequences, causal connections, comparisons, and negation. Understanding these challenges is key to improving model performance. ![Image 185: Bo Wang](https://jina-ai-gmbh.ghost.io/content/images/2022/11/4B483B29-E306-402B-8635-64866C458406.jpeg) ![Image 186: Alex C-G](https://jina-ai-gmbh.ghost.io/content/images/2022/09/alex.jpg)](https://jina.ai/news/text-embeddings-fail-to-capture-word-order-and-how-to-fix-it)\n\n[![Image 187: David Hockney artwork of a hand holding a rod with three colored spheres on a blue-toned background.](https://jina-ai-gmbh.ghost.io/content/images/2024/12/test-time-compute.jpg) December 12, 2024 • 12 minutes read Scaling Test-Time Compute For Embedding Models Better results scale with compute—more on learning, more on search. A good pretrained model takes you far, but test-time compute takes you further. It's time to recognize this paradigm of test-time compute, even for embedding models. ![Image 188: Han Xiao](https://jina-ai-gmbh.ghost.io/content/images/2022/10/Untitled-2.png)](https://jina.ai/news/scaling-test-time-compute-for-embedding-models)\n\n[![Image 189: Two hands, each holding a key positioned to interact with each other, depicted against a deep blue background.](https://jina-ai-gmbh.ghost.io/content/images/2024/11/banner--1-.jpg) November 27, 2024 • 10 minutes read Watermarking Text with Embedding Models to Protect Against Content Theft You use our embedding models to do what? This might be the most \"out-of-domain\" applications of embeddings we learned at EMNLP 2024. ![Image 190: Han Xiao](https://jina-ai-gmbh.ghost.io/content/images/2022/10/Untitled-2.png)](https://jina.ai/news/watermarking-text-with-embedding-models-to-protect-against-content-theft)\n\n[![Image 191: Digital number \"2\" displayed in a mosaic of colorful squares against a dark background, creating a futuristic vibe.](https://jina-ai-gmbh.ghost.io/content/images/2024/11/clipv2.png) November 21, 2024 • 9 minutes read Jina CLIP v2: Multilingual Multimodal Embeddings for Text and Images Jina-CLIP v2, a 0.9B multimodal embedding model with multilingual support of 89 languages, high image resolution at 512x512, and Matryoshka representations. ![Image 192: Jina AI](https://jina-ai-gmbh.ghost.io/content/images/2022/08/Jjqb-JeY_400x400.jpg)](https://jina.ai/news/jina-clip-v2-multilingual-multimodal-embeddings-for-text-and-images)\n\n_circle__circle__circle__circle__circle__circle__circle__circle__circle_\n\nComparison of Reranker, Vector Search, and BM25\n-----------------------------------------------\n\nThe table below provides a comprehensive comparison of the Reranker, Vector/Embeddings Search, and BM25, highlighting their strengths and weaknesses across various categories.\n\n|  | Reranker | Vector Search | BM25 |\n| --- | --- | --- | --- |\n| **Best For** | Enhanced search precision and relevance | Initial, rapid filtering | General text retrieval across wide-ranging queries |\n| **Granularity** | Detailed: Sub-document and query segment | Broad: Entire documents | Intermediate: Various text segments |\n| **Query Time Complexity** | High | Medium | Low |\n| **Indexing Time Complexity** | Not required | High | Low, utilizes pre-built index |\n| **Training Time Complexity** | High | High | Not required |\n| **Search Quality** | Superior for nuanced queries | Balanced between efficiency and accuracy | Consistent and reliable for a broad set of queries |\n| **Strengths** | Highly accurate with deep contextual understanding | Quick and efficient, with moderate accuracy | Highly scalable, with established efficacy |\n|  | [_![Image 193](https://jina.ai/assets/reranker-DudpN0Ck.svg)_Try reranker API for free](https://jina.ai/reranker) | [_![Image 194](https://jina.ai/assets/embedding-DzEuY8_E.svg)_Try embedding API for free](https://jina.ai/embeddings) |  |\n\nThe Evolution of Embeddings Poster\n----------------------------------\n\nDiscover the ideal poster for your space, featuring captivating infographics or breathtaking visuals tracing the evolution of text embedding models since 1950.\n\n[Learn how we made it](https://jina.ai/news/the-1950-2024-text-embeddings-evolution-poster)\n\n* * *\n\n[_shopping\\_cart_Buy a hard copy](https://buy.stripe.com/cN2aHS4Ax5F19DqfZ7)\n\n![Image 195](https://jina.ai/assets/jyMgQBGpxVh-Dv4riOlz.png)\n\nFAQ\n---\n\n### [How to get my API key?](https://jina.ai/embeddings/#get-api-key)\n\n video\\_not\\_supported\n\n### [What's the rate limit?](https://jina.ai/embeddings/#rate-limit)\n\nRate Limit\n\nRate limits are tracked in two ways: **RPM** (requests per minute) and **TPM** (tokens per minute). Limits are enforced per IP and can be reached based on whichever threshold—RPM or TPM—is hit first.\n\nColumns\n\n_arrow\\_drop\\_down_\n\n|  | Product | API Endpoint | Description_arrow\\_upward_ | w/o API Key | w/ API Key | w/ Premium API Key | Average Latency | Token Usage Counting | Allowed Request |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| \n![Image 196](https://jina.ai/assets/embedding-DzEuY8_E.svg)\n\n\n\n | Embedding API | `https://api.jina.ai/v1/embeddings` | Convert text/images to fixed-length vectors | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n_help_\n\n\n\n | Count the number of tokens in the input request. | POST |\n| \n\n![Image 197](https://jina.ai/assets/reranker-DudpN0Ck.svg)\n\n\n\n | Reranker API | `https://api.jina.ai/v1/rerank` | Tokenize and segment long text | _block_ | 500 RPM & 1,000,000 TPM | 2,000 RPM & 5,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n_help_\n\n\n\n | Count the number of tokens in the input request. | POST |\n| \n\n![Image 198](https://jina.ai/assets/reader-D06QTWF1.svg)\n\n\n\n | Reader API | `https://r.jina.ai` | Convert URL to LLM-friendly text | 20 RPM | 200 RPM | 1000 RPM | 4.6s | Count the number of tokens in the output response. | GET/POST |\n| \n\n![Image 199](https://jina.ai/assets/reader-D06QTWF1.svg)\n\n\n\n | Reader API | `https://s.jina.ai` | Search the web and convert results to LLM-friendly text | _block_ | 40 RPM | 100 RPM | 8.7s | Count the number of tokens in the output response. | GET/POST |\n| \n\n![Image 200](https://jina.ai/assets/reader-D06QTWF1.svg)\n\n\n\n | Reader API | `https://g.jina.ai` | Grounding a statement with web knowledge | _block_ | 10 RPM | 30 RPM | 22.7s | Count the total number of tokens in the whole process. | GET/POST |\n| \n\n![Image 201](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)\n\n\n\n | Classifier API (Zero-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using zero-shot classification | _block_ | 200 RPM & 500,000 TPM | 1,000 RPM & 3,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n\n\n\n\n | Tokens counted as: input\\_tokens + label\\_tokens | POST |\n| \n\n![Image 202](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)\n\n\n\n | Classifier API (Few-shot) | `https://api.jina.ai/v1/classify` | Classify inputs using a trained few-shot classifier | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n\n\n\n\n | Tokens counted as: input\\_tokens | POST |\n| \n\n![Image 203](blob:https://jina.ai/47430e9cbced04c539a17eb39573e3a9)\n\n\n\n | Classifier API | `https://api.jina.ai/v1/train` | Train a classifier using labeled examples | _block_ | 20 RPM & 200,000 TPM | 60 RPM & 1,000,000 TPM | \n\n_bolt_\n\ndepends on the input size\n\n\n\n\n\n | Tokens counted as: input\\_tokens × num\\_iters | POST |\n| \n\n![Image 204](blob:https://jina.ai/d9cb1deb4878909b05c9cd0f15af4aac)\n\n\n\n | Segmenter API | `https://segment.jina.ai` | Tokenize and segment long text | 20 RPM | 200 RPM | 1,000 RPM | 0.3s | Token is not counted as usage. | GET/POST |\n\n### [Do I need a commercial license?](https://jina.ai/embeddings/#cc-self-check)\n\nCC BY-NC License Self-Check\n\n* * *\n\n_play\\_arrow_\n\nAre you using our official API or official images on Azure or AWS?\n\n_play\\_arrow_\n\n_done_\n\nYes\n\n_play\\_arrow_\n\nAre you using a paid API key or free trial key?\n\n_play\\_arrow_\n\n_done_\n\nPaid API key\n\nNo restrictions. Use as per your current agreement.\n\n_play\\_arrow_\n\n_info_\n\nFree API key\n\nFree trial key can be only used for non-commercial purposes. Please purchase a paid package for commercial use.\n\n_play\\_arrow_\n\nAre you using our official model images on AWS and Azure?\n\nNo restrictions. Use as per your current agreement.\n\n_play\\_arrow_\n\n_close_\n\nNo\n\n_play\\_arrow_\n\nAre you using these models?\n\njina-clip-v2\n\njina-embeddings-v3\n\njina-reranker-v2-base-multilingual\n\njina-colbert-v2\n\nreader-lm-1.5b\n\nreader-lm-0.5b\n\nReaderLM-v2\n\n_play\\_arrow_\n\n_close_\n\nNo\n\nNo restrictions apply.\n\n_play\\_arrow_\n\n_done_\n\nYes\n\n_play\\_arrow_\n\nIs your use commercial?\n\n_play\\_arrow_\n\n_question\\_mark_\n\nNot sure\n\n_play\\_arrow_\n\nAre you:\n\n_play\\_arrow_\n\nUsing it for personal or hobby projects?\n\nThis is non-commercial. You can use the models freely.\n\n_play\\_arrow_\n\nA for-profit company using it internally?\n\nThis is commercial. Contact our sales team.\n\n[Contact sales](https://jina.ai/contact-sales)\n\n_play\\_arrow_\n\nAn educational institution using it for teaching?\n\nThis is typically non-commercial. You can use the models freely.\n\n_play\\_arrow_\n\nA non-profit or NGO using it for your mission?\n\nThis is typically non-commercial, but check with us if unsure.\n\n[Contact sales](https://jina.ai/contact-sales)\n\n_play\\_arrow_\n\nUsing it in a product or service you sell?\n\nThis is commercial. Contact our sales team.\n\n[Contact sales](https://jina.ai/contact-sales)\n\n_play\\_arrow_\n\nA government entity using it for public services?\n\nThis may be commercial. Please contact us for clarification.\n\n[Contact sales](https://jina.ai/contact-sales)\n\n_play\\_arrow_\n\n_close_\n\nNo\n\nYou can use the models freely.\n\n_play\\_arrow_\n\n_done_\n\nYes\n\nContact our sales team for licensing.\n\n[Contact sales](https://jina.ai/contact-sales)\n\n### [Other questions](https://jina.ai/embeddings/#faq)\n\nEmbeddings-related common questions\n\n_![Image 205](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nHow were the jina-embeddings-v3 models trained?\n\n_keyboard\\_arrow\\_down_\n\nFor detailed information on our training processes, data sources, and evaluations, please refer to our technical report available on arXiv.\n\n[_launch_arXiv](https://arxiv.org/abs/2409.10173)\n\n_![Image 206](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nWhat are the jina-clip models, and can I use them for text and image search?\n\n_keyboard\\_arrow\\_down_\n\nJina CLIP `jina-clip-v2` is an advanced multimodal embedding model that supports text-text, text-image, image-image, and image-text retrieval tasks. Unlike the original OpenAI CLIP, which struggles with text-text search, Jina CLIP excels as a text retriever. `jina-clip-v2` offers a 3% performance improvement over `jina-clip-v1` in both text-image and text-text retrieval tasks, supports 89 languages for multilingual image retrieval, processes higher resolution images (512x512), and reduces storage requirements with Matryoshka representations. You can read more about it in our tech report.\n\n[_launch_arXiv](https://arxiv.org/abs/2412.08802)\n\n_![Image 207](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nWhich languages do your models support?\n\n_keyboard\\_arrow\\_down_\n\nAs of its release on September 18, 2024, `jina-embeddings-v3` is the best multilingual model and ranks 2nd on the MTEB English leaderboard for models with fewer than 1 billion parameters. v3 supports a total of 89 languages, including the top 30 with the best performance: Arabic, Bengali, Chinese, Danish, Dutch, English, Finnish, French, Georgian, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Latvian, Norwegian, Polish, Portuguese, Romanian, Russian, Slovak, Spanish, Swedish, Thai, Turkish, Ukrainian, Urdu, and Vietnamese. For more details, please refer to the `jina-embeddings-v3` tech report.\n\n[_launch_arXiv](https://arxiv.org/abs/2409.10173)\n\n_![Image 208](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nWhat is the maximum length for a single sentence input?\n\n_keyboard\\_arrow\\_down_\n\nOur models allow for an input length of up to 8192 tokens, which is significantly higher than most other models. A token can range from a single character, like 'a', to an entire word, such as 'apple'. The total number of characters that can be input depends on the length and complexity of the words used. This extended input capability enables our `jina-embeddings-v3` and `jina-clip` models to perform more comprehensive text analysis and achieve higher accuracy in context understanding, especially for extensive textual data.\n\n_![Image 209](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nWhat is the maximum number of sentences I can include in a single request?\n\n_keyboard\\_arrow\\_down_\n\nA single API call can process up to 2048 sentences or texts, facilitating extensive text analysis in one request.\n\n_![Image 210](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nHow do I send images to the jina-clip models?\n\n_keyboard\\_arrow\\_down_\n\nYou can use either `url` or `bytes` in the `input` field of the API request. For `url`, provide the URL of the image you want to process. For `bytes`, encode the image in base64 format and include it in the request. The model will return the embeddings of the image in the response.\n\n_![Image 211](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nHow do Jina Embeddings models compare to OpenAI's and Cohere's latest embeddings?\n\n_keyboard\\_arrow\\_down_\n\nIn evaluations on the MTEB English, Multilingual, and LongEmbed benchmarks, `jina-embeddings-v3` outperforms the latest proprietary embeddings from OpenAI and Cohere on English tasks, and surpasses `multilingual-e5-large-instruct` across all multilingual tasks. With a default output dimension of 1024, users can truncate the embedding dimensions down to 32 without sacrificing performance, thanks to the integration of Matryoshka Representation Learning (MRL).\n\n_![Image 212](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nHow seamless is the transition from OpenAI's text-embedding-3-large to your solution?\n\n_keyboard\\_arrow\\_down_\n\nThe transition is streamlined, as [our API endpoint](https://api.jina.ai/v1/embeddings), matches the input and output JSON schemas of OpenAI’s `text-embedding-3-large` model. This compatibility ensures users can easily replace the OpenAI model with ours when using OpenAI’s endpoint.\n\n_![Image 213](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nHow tokens are calculated when using jina-clip models?\n\n_keyboard\\_arrow\\_down_\n\nTokens are calculated based on the text length and image size. For text in the request, tokens are counted in the standard way. For images, the following steps are conducted: 1. Tile Size: Each image is divided into tiles. For `jina-clip-v2`, tiles are 512x512 pixels, while for `jina-clip-v1`, tiles are 224x224 pixels. 2. Coverage: The number of tiles required to cover the input image is calculated. Even if the image dimensions are not perfectly divisible by the tile size, partial tiles are counted as full tiles. 3. Total Tiles: The total number of tiles covering the image determines the cost. For example, a 600x600 pixel image would be covered by 2x2 tiles (4 tiles) in v2 and 3x3 tiles (9 tiles) in v1. 4. Cost Calculation: For `jina-clip-v2`, each tile costs 4000 tokens, while for `jina-clip-v1`, each tile costs 1000 tokens. Example: For an image with dimensions 600x600 pixels: • With `jina-clip-v2` • The image is divided into 512x512 pixel tiles. • The total number of tiles required is 2 (horizontal) x 2 (vertical) = 4 tiles. • The cost for `jina-clip-v2` will be 4\\*4000 = 16000 tokens. • With `jina-clip-v1` • The image is divided into 224x224 pixel tiles. • The total number of tiles required is 3 (horizontal) x 3 (vertical) = 9 tiles. • The cost for jina-clip-v1 will be 9\\*1000 = 9000 tokens.\n\n_![Image 214](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nDo you provide models for embedding images or audio?\n\n_keyboard\\_arrow\\_down_\n\nYes, `jina-clip-v2` and `jina-clip-v1` can embed both images and texts. Embedding models on more modalities will be announced soon!\n\n_![Image 215](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nCan Jina Embedding models be fine-tuned with private or company data?\n\n_keyboard\\_arrow\\_down_\n\nFor inquiries about fine-tuning our models with specific data, please contact us to discuss your requirements. We are open to exploring how our models can be adapted to meet your needs.\n\n[Contact](https://jina.ai/contact-sales)\n\n_![Image 216](https://jina.ai/assets/embedding-DzEuY8_E.svg)_\n\nCan your endpoints be hosted privately on AWS, Azure, or GCP?\n\n_keyboard\\_arrow\\_down_\n\nYes, our services are available on AWS, Azure, and GCP marketplaces. If you have specific requirements, please contact us at sales AT jina.ai.\n\n[_launch_AWS SageMaker](https://aws.amazon.com/marketplace/seller-profile?id=seller-stch2ludm6vgy)[_launch_Google Cloud](https://console.cloud.google.com/marketplace/browse?q=jina&pli=1&inv=1&invt=AbmydQ)[_launch_Microsoft Azure](https://azuremarketplace.microsoft.com/en-US/marketplace/apps?page=1&search=jina)\n\nAPI-related common questions\n\n_code_\n\nCan I use the same API key for reader, embedding, reranking, classifying and fine-tuning APIs?\n\n_keyboard\\_arrow\\_down_\n\nYes, the same API key is valid for all search foundation products from Jina AI. This includes the reader, embedding, reranking, classifying and fine-tuning APIs, with tokens shared between the all services.\n\n_code_\n\nCan I monitor the token usage of my API key?\n\n_keyboard\\_arrow\\_down_\n\nYes, token usage can be monitored in the 'API Key & Billing' tab by entering your API key, allowing you to view the recent usage history and remaining tokens. If you have logged in to the API dashboard, these details can also be viewed in the 'Manage API Key' tab.\n\n_code_\n\nWhat should I do if I forget my API key?\n\n_keyboard\\_arrow\\_down_\n\nIf you have misplaced a topped-up key and wish to retrieve it, please contact support AT jina.ai with your registered email for assistance. It's recommended to log in to keep your API key securely stored and easily accessible.\n\n[Contact](https://jina.ai/contact-sales)\n\n_code_\n\nDo API keys expire?\n\n_keyboard\\_arrow\\_down_\n\nNo, our API keys do not have an expiration date. However, if you suspect your key has been compromised and wish to retire it, please contact our support team for assistance. You can also revoke your key in [the API Key Management dashboard](https://jina.ai/api-dashboard).\n\n[Contact](https://jina.ai/contact-sales)\n\n_code_\n\nCan I transfer tokens between API keys?\n\n_keyboard\\_arrow\\_down_\n\nYes, you can transfer tokens from a premium key to another. After logging into your account on [the API Key Management dashboard](https://jina.ai/api-dashboard), use the settings of the key you want to transfer out to move all remaining paid tokens.\n\n_code_\n\nCan I revoke my API key?\n\n_keyboard\\_arrow\\_down_\n\nYes, you can revoke your API key if you believe it has been compromised. Revoking a key will immediately disable it for all users who have stored it, and all remaining balance and associated properties will be permanently unusable. If the key is a premium key, you have the option to transfer the remaining paid balance to another key before revocation. Notice that this action cannot be undone. To revoke a key, go to the key settings in [the API Key Management dashboard](https://jina.ai/api-dashboard).\n\n_code_\n\nWhy is the first request for some models slow?\n\n_keyboard\\_arrow\\_down_\n\nThis is because our serverless architecture offloads certain models during periods of low usage. The initial request activates or 'warms up' the model, which may take a few seconds. After this initial activation, subsequent requests process much more quickly.\n\n_code_\n\nIs user input data used for training your models?\n\n_keyboard\\_arrow\\_down_\n\nWe adhere to a strict privacy policy and do not use user input data for training our models. We are also SOC 2 Type I and Type II compliant, ensuring high standards of security and privacy.\n\nBilling-related common questions\n\n_attach\\_money_\n\nIs billing based on the number of sentences or requests?\n\n_keyboard\\_arrow\\_down_\n\nOur pricing model is based on the total number of tokens processed, allowing users the flexibility to allocate these tokens across any number of sentences, offering a cost-effective solution for diverse text analysis requirements.\n\n_attach\\_money_\n\nIs there a free trial available for new users?\n\n_keyboard\\_arrow\\_down_\n\nWe offer a welcoming free trial to new users, which includes one million tokens for use with any of our models, facilitated by an auto-generated API key. Once the free token limit is reached, users can easily purchase additional tokens for their API keys via the 'Buy tokens' tab.\n\n_attach\\_money_\n\nAre tokens charged for failed requests?\n\n_keyboard\\_arrow\\_down_\n\nNo, tokens are not deducted for failed requests.\n\n_attach\\_money_\n\nWhat payment methods are accepted?\n\n_keyboard\\_arrow\\_down_\n\nPayments are processed through Stripe, supporting a variety of payment methods including credit cards, Google Pay, and PayPal for your convenience.\n\n_attach\\_money_\n\nIs invoicing available for token purchases?\n\n_keyboard\\_arrow\\_down_\n\nYes, an invoice will be issued to the email address associated with your Stripe account upon the purchase of tokens.\n\nOffices\n\n_location\\_on_\n\nSunnyvale, CA\n\n710 Lakeway Dr, Ste 200, Sunnyvale, CA 94085, USA\n\n_location\\_on_\n\nBerlin, Germany (HQ)\n\nPrinzessinnenstraße 19-20, 10969 Berlin, Germany\n\n_location\\_on_\n\nBeijing, China\n\nLevel 5, Building 6, No.48 Haidian West St. Beijing, China\n\n_location\\_on_\n\nShenzhen, China\n\n402 Floor 4, Fu'an Technology Building, Shenzhen, China\n\nSearch Foundation\n\n[Reader](https://jina.ai/reader)[Embeddings](https://jina.ai/embeddings)[Reranker](https://jina.ai/reranker)[Classifier](https://jina.ai/classifier)[Segmenter](https://jina.ai/segmenter)[API Documentation](https://docs.jina.ai/)\n\nGet Jina API key\n\n[Rate Limit](https://jina.ai/contact-sales#rate-limit)[API Status](https://status.jina.ai/)\n\nCompany\n\n[About us](https://jina.ai/about-us)[Contact sales](https://jina.ai/contact-sales)[Newsroom](https://jina.ai/news)[Intern program](https://jina.ai/internship)[Join us _open\\_in\\_new_](https://career.jina.ai/)[Download logo _open\\_in\\_new_](https://jina.ai/logo-Jina-1024.zip)\n\nTerms\n\n[Security](https://jina.ai/legal#security-as-company-value)[Terms & Conditions](https://jina.ai/legal/#terms-and-conditions)[Privacy](https://jina.ai/legal/#privacy-policy)[Manage Cookies](javascript:UC_UI.showSecondLayer();)[![Image 217](https://jina.ai/21972-312_SOC_NonCPA_Blk.svg)](https://app.eu.vanta.com/jinaai/trust/vz7f4mohp0847aho84lmva)\n\n[](https://x.com/jinaAI_)[](https://www.linkedin.com/company/jinaai/)[](https://github.com/jina-ai)[_![Image 218](https://jina.ai/huggingface_logo.svg)_](https://huggingface.co/jinaai) [](https://discord.jina.ai/)[_email_](mailto:support@jina.ai)\n\nJina AI © 2020-2025.",
  "usage": {
    "tokens": 11359
  }
}
```
