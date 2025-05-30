---
title: Turbocharge RAG with LangChain and Vespa Streaming Mode for Partitioned Data — pyvespa documentation
description: 
url: https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html
timestamp: 2025-01-20T15:58:20.713Z
domain: pyvespa.readthedocs.io
path: en_latest_examples_turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html
---

# Turbocharge RAG with LangChain and Vespa Streaming Mode for Partitioned Data — pyvespa documentation



## Content

![Image 9: #Vespa](https://assets.vespa.ai/logos/Vespa-logo-dark-RGB.svg)

This notebook illustrates using [Vespa streaming mode](https://docs.vespa.ai/en/streaming-search.html) to build cost-efficient RAG applications over naturally sharded data.

You can read more about Vespa vector streaming search in these blog posts:

*   [Announcing vector streaming search: AI assistants at scale without breaking the bank](https://blog.vespa.ai/announcing-vector-streaming-search/)
    
*   [Yahoo Mail turns to Vespa to do RAG at scale](https://blog.vespa.ai/yahoo-mail-turns-to-vespa-to-do-rag-at-scale/)
    
*   [Hands-On RAG guide for personal data with Vespa and LLamaIndex](https://blog.vespa.ai/scaling-personal-ai-assistants-with-streaming-mode/)
    

This notebook is also available in blog form: [Turbocharge RAG with LangChain and Vespa Streaming Mode for Sharded Data](https://blog.vespa.ai/turbocharge-rag-with-langchain-and-vespa-streaming-mode/)

TLDR; Vespa streaming mode for partitioned data[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#TLDR;-Vespa-streaming-mode-for-partitioned-data "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Vespa’s streaming search solution enables you to integrate a user ID (or any sharding key) into the Vespa document ID. This setup allows Vespa to efficiently group each user’s data on a small set of nodes and the same disk chunk. Streaming mode enables low latency searches on a user’s data without keeping data in memory.

The key benefits of streaming mode:

*   Eliminating compromises in precision introduced by approximate algorithms
    
*   Achieve significantly higher write throughput, thanks to the absence of index builds required for supporting approximate search.
    
*   Optimize efficiency by storing documents, including tensors and data, on disk, benefiting from the cost-effective economics of storage tiers.
    
*   Storage cost is the primary cost driver of Vespa streaming mode; no data is in memory. Avoiding memory usage lowers deployment costs significantly.
    

Connecting LangChain Retriever with Vespa for Context Retrieval from PDF Documents[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Connecting-LangChain-Retriever-with-Vespa-for-Context-Retrieval-from-PDF-Documents "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this notebook, we seamlessly integrate a custom [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction) [retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/) with a Vespa app, leveraging Vespa’s streaming mode to extract meaningful context from PDF documents.

The workflow

*   Define and deploy a Vespa [application package](https://docs.vespa.ai/en/application-packages.html) using PyVespa.
    
*   Utilize [LangChain PDF Loaders](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf) to download and parse PDF files.
    
*   Leverage [LangChain Document Transformers](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/) to convert each PDF page into multiple text chunks.
    
*   Feed the transformer representation to the running Vespa instance
    
*   Employ Vespa’s built-in embedder functionality (using an open-source embedding model) for embedding the text chunks per page, resulting in a multi-vector representation.
    
*   Develop a custom [Retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/) to enable seamless retrieval for any unstructured text query.
    

![Image 10: Overview](https://blog.vespa.ai/assets/2023-12-08-turbocharge-rag-with-langchain-and-vespa-streaming-mode/turbocharge-RAG-vespa-streaming.png)

[![Image 11: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vespa-engine/pyvespa/blob/master/docs/sphinx/source/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.ipynb)

Let’s get started! First, install dependencies:

!pip3 install \-U pyvespa langchain langchain-community pypdf\==5.0.1 openai

### Sample data[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Sample-data "Link to this heading")

We love [ColBERT](https://blog.vespa.ai/pretrained-transformer-language-models-for-search-part-3/), so we’ll use a few COlBERT related papers as examples of PDFs in this notebook.

def sample\_pdfs():
    return \[
        {
            "title": "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction",
            "url": "https://arxiv.org/pdf/2112.01488.pdf",
            "authors": "Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts, Matei Zaharia",
        },
        {
            "title": "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT",
            "url": "https://arxiv.org/pdf/2004.12832.pdf",
            "authors": "Omar Khattab, Matei Zaharia",
        },
        {
            "title": "On Approximate Nearest Neighbour Selection for Multi-Stage Dense Retrieval",
            "url": "https://arxiv.org/pdf/2108.11480.pdf",
            "authors": "Craig Macdonald, Nicola Tonellotto",
        },
        {
            "title": "A Study on Token Pruning for ColBERT",
            "url": "https://arxiv.org/pdf/2112.06540.pdf",
            "authors": "Carlos Lassance, Maroua Maachou, Joohee Park, Stéphane Clinchant",
        },
        {
            "title": "Pseudo-Relevance Feedback for Multiple Representation Dense Retrieval",
            "url": "https://arxiv.org/pdf/2106.11251.pdf",
            "authors": "Xiao Wang, Craig Macdonald, Nicola Tonellotto, Iadh Ounis",
        },
    \]

### Defining the Vespa application[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Defining-the-Vespa-application "Link to this heading")

[PyVespa](https://pyvespa.readthedocs.io/en/latest/) helps us build the [Vespa application package](https://docs.vespa.ai/en/application-packages.html). A Vespa application package consists of configuration files, schemas, models, and code (plugins).

First, we define a [Vespa schema](https://docs.vespa.ai/en/schemas.html) with the fields we want to store and their type.

from vespa.package import Schema, Document, Field, FieldSet, HNSW

pdf\_schema \= Schema(
    name\="pdf",
    mode\="streaming",
    document\=Document(
        fields\=\[
            Field(name\="id", type\="string", indexing\=\["summary", "index"\]),
            Field(name\="title", type\="string", indexing\=\["summary", "index"\]),
            Field(name\="url", type\="string", indexing\=\["summary", "index"\]),
            Field(name\="authors", type\="array<string\>", indexing\=\["summary", "index"\]),
            Field(name\="page", type\="int", indexing\=\["summary", "index"\]),
            Field(
                name\="metadata",
                type\="map<string,string\>",
                indexing\=\["summary", "index"\],
            ),
            Field(name\="chunks", type\="array<string\>", indexing\=\["summary", "index"\]),
            Field(
                name\="embedding",
                type\="tensor<bfloat16\>(chunk{}, x\[384\])",
                indexing\=\["input chunks", "embed e5", "attribute", "index"\],
                ann\=HNSW(distance\_metric\="angular"),
                is\_document\_field\=False,
            ),
        \],
    ),
    fieldsets\=\[FieldSet(name\="default", fields\=\["chunks", "title"\])\],
)

The above defines our `pdf` schema using mode `streaming`. Most fields are straightforward, but take a note of:

*   `metadata` using `map<string,string>` - here we can store and match over page level metadata extracted by the PDF parser.
    
*   `chunks` using `array<string>`, these are the text chunks that we use langchain document transformers for
    
*   The `embedding` field of type `tensor<bfloat16>(chunk{},x[384])` allows us to store and search the 384-dimensional embeddings per chunk in the same document
    

The observant reader might have noticed the `e5` argument to the `embed` expression in the above `embedding` field. The `e5` argument references a component of the type [hugging-face-embedder](https://docs.vespa.ai/en/embedding.html#huggingface-embedder). We configure the application package and its name with the `pdf` schema and the `e5` embedder component.

from vespa.package import ApplicationPackage, Component, Parameter

vespa\_app\_name \= "ragpdfs"
vespa\_application\_package \= ApplicationPackage(
    name\=vespa\_app\_name,
    schema\=\[pdf\_schema\],
    components\=\[
        Component(
            id\="e5",
            type\="hugging-face-embedder",
            parameters\=\[
                Parameter(
                    "transformer-model",
                    {
                        "url": "https://github.com/vespa-engine/sample-apps/raw/master/simple-semantic-search/model/e5-small-v2-int8.onnx"
                    },
                ),
                Parameter(
                    "tokenizer-model",
                    {
                        "url": "https://raw.githubusercontent.com/vespa-engine/sample-apps/master/simple-semantic-search/model/tokenizer.json"
                    },
                ),
            \],
        )
    \],
)

In the last step, we configure [ranking](https://docs.vespa.ai/en/ranking.html) by adding `rank-profile`’s to the schema.

Vespa supports [phased ranking](https://docs.vespa.ai/en/phased-ranking.html) and has a rich set of built-in [rank-features](https://docs.vespa.ai/en/reference/rank-features.html), including many text-matching features such as:

*   [BM25](https://docs.vespa.ai/en/reference/bm25.html).
    
*   [nativeRank](https://docs.vespa.ai/en/reference/nativerank.html) and many more.
    

Users can also define custom functions using [ranking expressions](https://docs.vespa.ai/en/reference/ranking-expressions.html). The following defines a `hybrid` Vespa ranking profile.

from vespa.package import RankProfile, Function, FirstPhaseRanking

semantic \= RankProfile(
    name\="hybrid",
    inputs\=\[("query(q)", "tensor<float\>(x\[384\])")\],
    functions\=\[
        Function(
            name\="similarities",
            expression\="cosine\_similarity(query(q), attribute(embedding),x)",
        )
    \],
    first\_phase\=FirstPhaseRanking(
        expression\="nativeRank(title) + nativeRank(chunks) + reduce(similarities, max, chunk)",
        rank\_score\_drop\_limit\=0.0,
    ),
    match\_features\=\[
        "closest(embedding)",
        "similarities",
        "nativeRank(chunks)",
        "nativeRank(title)",
        "elementSimilarity(chunks)",
    \],
)
pdf\_schema.add\_rank\_profile(semantic)

The `hybrid` rank-profile above defines the query input embedding type and a similarities function that uses a Vespa [tensor compute function](https://docs.vespa.ai/en/reference/ranking-expressions.html#tensor-functions) that calculates the cosine similarity between all the chunk embeddings and the query embedding.

The profile only defines a single ranking phase, using a linear combination of multiple features.

Using [match-features](https://docs.vespa.ai/en/reference/schema-reference.html#match-features), Vespa returns selected features along with the hit in the SERP (result page).

### Deploy the application to Vespa Cloud[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Deploy-the-application-to-Vespa-Cloud "Link to this heading")

With the configured application, we can deploy it to [Vespa Cloud](https://cloud.vespa.ai/en/).

To deploy the application to Vespa Cloud we need to create a tenant in the Vespa Cloud:

Create a tenant at [console.vespa-cloud.com](https://console.vespa-cloud.com/) (unless you already have one). This step requires a Google or GitHub account, and will start your [free trial](https://cloud.vespa.ai/en/free-trial).

Make note of the tenant name, it is used in the next steps.

> Note: Deployments to dev and perf expire after 7 days of inactivity, i.e., 7 days after running deploy. This applies to all plans, not only the Free Trial. Use the Vespa Console to extend the expiry period, or redeploy the application to add 7 more days.

from vespa.deployment import VespaCloud
import os

\# Replace with your tenant name from the Vespa Cloud Console
tenant\_name \= "vespa-team"

\# Key is only used for CI/CD. Can be removed if logging in interactively
key \= os.getenv("VESPA\_TEAM\_API\_KEY", None)
if key is not None:
    key \= key.replace(r"\\n", "\\n")  \# To parse key correctly

vespa\_cloud \= VespaCloud(
    tenant\=tenant\_name,
    application\=vespa\_app\_name,
    key\_content\=key,  \# Key is only used for CI/CD. Can be removed if logging in interactively
    application\_package\=vespa\_application\_package,
)

Now deploy the app to Vespa Cloud dev zone.

The first deployment typically takes 2 minutes until the endpoint is up.

from vespa.application import Vespa

app: Vespa \= vespa\_cloud.deploy()

Deployment started in run 2 of dev-aws-us-east-1c for samples.pdfs. This may take a few minutes the first time.
INFO    \[17:23:35\]  Deploying platform version 8.270.8 and application dev build 2 for dev-aws-us-east-1c of default ...
INFO    \[17:23:35\]  Using CA signed certificate version 0
WARNING \[17:23:35\]  For schema 'pdf', field 'page': Changed to attribute because numerical indexes (field has type int) is not currently supported. Index-only settings may fail. Ignore this warning for streaming search.
INFO    \[17:23:35\]  Using 1 nodes in container cluster 'pdfs\_container'
WARNING \[17:23:36\]  For streaming search cluster 'pdfs\_content.pdf', SD field 'embedding': hnsw index is not relevant and not supported, ignoring setting
WARNING \[17:23:36\]  For streaming search cluster 'pdfs\_content.pdf', SD field 'embedding': hnsw index is not relevant and not supported, ignoring setting
INFO    \[17:23:38\]  Deployment successful.
INFO    \[17:23:38\]  Session 3239 for tenant 'samples' prepared and activated.
INFO    \[17:23:38\]  ######## Details for all nodes ########
INFO    \[17:23:38\]  h88963a.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP
INFO    \[17:23:38\]  --- platform vespa/cloud-tenant-rhel8:8.270.8
INFO    \[17:23:38\]  --- storagenode on port 19102 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  --- searchnode on port 19107 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  --- distributor on port 19111 has config generation 3238, wanted is 3239
INFO    \[17:23:38\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  h88969g.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP
INFO    \[17:23:38\]  --- platform vespa/cloud-tenant-rhel8:8.270.8
INFO    \[17:23:38\]  --- logserver-container on port 4080 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  h88972i.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP
INFO    \[17:23:38\]  --- platform vespa/cloud-tenant-rhel8:8.270.8
INFO    \[17:23:38\]  --- container-clustercontroller on port 19050 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  h89461a.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP
INFO    \[17:23:38\]  --- platform vespa/cloud-tenant-rhel8:8.270.8
INFO    \[17:23:38\]  --- container on port 4080 has config generation 3239, wanted is 3239
INFO    \[17:23:38\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239
INFO    \[17:23:51\]  Found endpoints:
INFO    \[17:23:51\]  - dev.aws-us-east-1c
INFO    \[17:23:51\]   |-- https://c4f42a1b.bfbdb4fd.z.vespa-app.cloud/ (cluster 'pdfs\_container')
INFO    \[17:23:52\]  Installation succeeded!
Using mTLS (key,cert) Authentication against endpoint https://c4f42a1b.bfbdb4fd.z.vespa-app.cloud//ApplicationStatus
Application is up!
Finished deployment.

### Processing PDFs with LangChain[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Processing-PDFs-with-LangChain "Link to this heading")

[LangChain](https://python.langchain.com/) has a rich set of [document loaders](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/) that can be used to load and process various file formats. In this notebook, we use the [PyPDFLoader](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf).

We also want to split the extracted text into _chunks_ using a [text splitter](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/). Most text embedding models have limited input lengths (typically less than 512 language model tokens, so splitting the text into multiple chunks that fits into the context limit of the embedding model is a common strategy.

For embedding text data, models based on the Transformer architecture have become the de facto standard. A challenge with Transformer-based models is their input length limitation due to the quadratic self-attention computational complexity. For example, a popular open-source text embedding model like [e5](https://huggingface.co/intfloat/e5-small) has an absolute maximum input length of 512 wordpiece tokens. In addition to the technical limitation, trying to fit more tokens than used during fine-tuning of the model will impact the quality of the vector representation.

One can view text embedding encoding as a lossy compression technique, where variable-length texts are compressed into a fixed dimensional vector representation.

from langchain\_community.document\_loaders import PyPDFLoader
from langchain.text\_splitter import RecursiveCharacterTextSplitter

text\_splitter \= RecursiveCharacterTextSplitter(
    chunk\_size\=1024,  \# chars, not llm tokens
    chunk\_overlap\=0,
    length\_function\=len,
    is\_separator\_regex\=False,
)

The following iterates over the `sample_pdfs` and performs the following:

*   Load the URL and extract the text into pages. A page is the retrievable unit we will use in Vespa
    
*   For each page, use the text splitter to split the text into chunks. The chunks are represented as an `array<string>` in the Vespa schema
    
*   Create the page level Vespa `fields`, note that we duplicate some content like the title and URL into the page level representation.
    

import hashlib
import unicodedata

def remove\_control\_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)\[0\] != "C")

my\_docs\_to\_feed \= \[\]
for pdf in sample\_pdfs():
    url \= pdf\["url"\]
    loader \= PyPDFLoader(url)
    pages \= loader.load\_and\_split()
    for index, page in enumerate(pages):
        source \= page.metadata\["source"\]
        chunks \= text\_splitter.transform\_documents(\[page\])
        text\_chunks \= \[chunk.page\_content for chunk in chunks\]
        text\_chunks \= \[remove\_control\_characters(chunk) for chunk in text\_chunks\]
        page\_number \= index + 1
        vespa\_id \= f"{url}#{page\_number}"
        hash\_value \= hashlib.sha1(vespa\_id.encode()).hexdigest()
        fields \= {
            "title": pdf\["title"\],
            "url": url,
            "page": page\_number,
            "id": hash\_value,
            "authors": \[a.strip() for a in pdf\["authors"\].split(",")\],
            "chunks": text\_chunks,
            "metadata": page.metadata,
        }
        my\_docs\_to\_feed.append(fields)

Now that we have parsed the input PDFs and created a list of pages that we want to add to Vespa, we must format the list into the format that PyVespa accepts. Notice the `fields`, `id` and `groupname` keys. The `groupname` is the key that is used to shard and co-locate the data and is only relevant when using Vespa with streaming mode.

from typing import Iterable

def vespa\_feed(user: str) \-\> Iterable\[dict\]:
    for doc in my\_docs\_to\_feed:
        yield {"fields": doc, "id": doc\["id"\], "groupname": user}

Now, we can feed to the Vespa instance (`app`), using the `feed_iterable` API, using the generator function above as input with a custom `callback` function. Vespa also performs embedding inference during this step using the built-in Vespa [embedding](https://docs.vespa.ai/en/embedding.html#huggingface-embedder) functionality.

from vespa.io import VespaResponse

def callback(response: VespaResponse, id: str):
    if not response.is\_successful():
        print(
            f"Document {id} failed to feed with status code {response.status\_code}, url={response.url} response={response.json}"
        )

app.feed\_iterable(
    schema\="pdf", iter\=vespa\_feed("jo-bergum"), namespace\="personal", callback\=callback
)

Notice the `schema` and `namespace` arguments. PyVespa transforms the input operations to Vespa [document v1](https://docs.vespa.ai/en/document-v1-api-guide.html) requests.

![Image 12: Document id](https://blog.vespa.ai/assets/2023-12-08-turbocharge-rag-with-langchain-and-vespa-streaming-mode/docid.png)

Querying data[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Querying-data "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we can also query our data. With [streaming mode](https://docs.vespa.ai/en/reference/query-api-reference.html#streaming), we must pass the `groupname` parameter, or the request will fail with an error.

The query request uses the Vespa Query API and the `Vespa.query()` function supports passing any of the Vespa query API parameters.

Read more about querying Vespa in:

*   [Vespa Query API](https://docs.vespa.ai/en/query-api.html)
    
*   [Vespa Query API reference](https://docs.vespa.ai/en/reference/query-api-reference.html)
    
*   [Vespa Query Language API (YQL)](https://docs.vespa.ai/en/query-language.html)
    

Sample query request for `why is colbert effective?` for the user `bergum@vespa.ai`:

from vespa.io import VespaQueryResponse
import json

response: VespaQueryResponse \= app.query(
    yql\="select id,title,page,chunks from pdf where userQuery() or ({targetHits:10}nearestNeighbor(embedding,q))",
    groupname\="jo-bergum",
    ranking\="hybrid",
    query\="why is colbert effective?",
    body\={
        "presentation.format.tensors": "short-value",
        "input.query(q)": 'embed(e5, "why is colbert effective?")',
    },
    timeout\="2s",
)
assert response.is\_successful()
print(json.dumps(response.hits\[0\], indent\=2))

{
  "id": "id:personal:pdf:g=jo-bergum:a4b2ced87807ee9cb0325b7a1c64a070d05a31f7",
  "relevance": 1.1412738851962692,
  "source": "pdfs\_content.pdf",
  "fields": {
    "matchfeatures": {
      "closest(embedding)": {
        "0": 1.0
      },
      "elementSimilarity(chunks)": 0.5006379585326953,
      "nativeRank(chunks)": 0.15642522855051508,
      "nativeRank(title)": 0.1341324233922751,
      "similarities": {
        "1": 0.7731813192367554,
        "2": 0.8196794986724854,
        "3": 0.796222984790802,
        "4": 0.7699441909790039,
        "0": 0.850716233253479
      }
    },
    "id": "a4b2ced87807ee9cb0325b7a1c64a070d05a31f7",
    "title": "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT",
    "page": 9,
    "chunks": \[
      "Sq,d:=\\u00d5i\\u2208\[|Eq|\]maxj\\u2208\[|Ed|\]Eqi\\u00b7ETdj(3)ColBERT is di\\ufb00erentiable end-to-end. We /f\_ine-tune the BERTencoders and train from scratch the additional parameters (i.e., thelinear layer and the \[Q\] and \[D\] markers\\u2019 embeddings) using theAdam \[ 16\] optimizer. Notice that our interaction mechanism hasno trainable parameters. Given a triple \\u27e8q,d+,d\\u2212\\u27e9with query q,positive document d+and negative document d\\u2212, ColBERT is usedto produce a score for each document individually and is optimizedvia pairwise so/f\_tmax cross-entropy loss over the computed scoresofd+andd\\u2212.3.4 O\\ufb00line Indexing: Computing & StoringDocument EmbeddingsBy design, ColBERT isolates almost all of the computations betweenqueries and documents, largely to enable pre-computing documentrepresentations o\\ufb04ine. At a high level, our indexing procedure isstraight-forward: we proceed over the documents in the collectionin batches, running our document encoder fDon each batch andstoring the output embeddings per document. Although indexing",
      "a set of documents is an o\\ufb04ine process, we incorporate a fewsimple optimizations for enhancing the throughput of indexing. Aswe show in \\u00a74.5, these optimizations can considerably reduce theo\\ufb04ine cost of indexing.To begin with, we exploit multiple GPUs, if available, for fasterencoding of batches of documents in parallel. When batching, wepad all documents to the maximum length of a document withinthe batch.3To make capping the sequence length on a per-batchbasis more e\\ufb00ective, our indexer proceeds through documents ingroups of B(e.g., B=100,000) documents. It sorts these documentsby length and then feeds batches of b(e.g., b=128) documents ofcomparable length through our encoder. /T\_his length-based bucket-ing is sometimes refered to as a BucketIterator in some libraries(e.g., allenNLP). Lastly, while most computations occur on the GPU,we found that a non-trivial portion of the indexing time is spent onpre-processing the text sequences, primarily BERT\\u2019s WordPiece to-",
      "kenization. Exploiting that these operations are independent acrossdocuments in a batch, we parallelize the pre-processing across theavailable CPU cores.Once the document representations are produced, they are savedto disk using 32-bit or 16-bit values to represent each dimension.As we describe in \\u00a73.5 and 3.6, these representations are eithersimply loaded from disk for ranking or are subsequently indexedfor vector-similarity search, respectively.3.5 Top- kRe-ranking with ColBERTRecall that ColBERT can be used for re-ranking the output of an-other retrieval model, typically a term-based model, or directlyfor end-to-end retrieval from a document collection. In this sec-tion, we discuss how we use ColBERT for ranking a small set ofk(e.g., k=1000) documents given a query q. Since kis small, werely on batch computations to exhaustively score each document",
      "3/T\_he public BERT implementations we saw simply pad to a pre-de/f\_ined length.(unlike our approach in \\u00a73.6). To begin with, our query serving sub-system loads the indexed documents representations into memory,representing each document as a matrix of embeddings.Given a query q, we compute its bag of contextualized embed-dings Eq(Equation 1) and, concurrently, gather the document repre-sentations into a 3-dimensional tensor Dconsisting of kdocumentmatrices. We pad the kdocuments to their maximum length tofacilitate batched operations, and move the tensor Dto the GPU\\u2019smemory. On the GPU, we compute a batch dot-product of EqandD, possibly over multiple mini-batches. /T\_he output materializes a3-dimensional tensor that is a collection of cross-match matricesbetween qand each document. To compute the score of each docu-ment, we reduce its matrix across document terms via a max-pool(i.e., representing an exhaustive implementation of our MaxSim",
      "computation) and reduce across query terms via a summation. Fi-nally, we sort the kdocuments by their total scores."
    \]
  }
}

Notice the `matchfeatures` that returns the configured match-features from the rank-profile, including all the chunk similarities.

### LangChain Retriever[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#LangChain-Retriever "Link to this heading")

We use the [LangChain Retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/) interface so that we can connect our Vespa app with the flexibility and power of the [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction) LLM framework.

> A retriever is an interface that returns documents given an unstructured query. It is more general than a vector store. A retriever does not need to be able to store documents, only to return (or retrieve) them. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well.

The retriever interface fits perfectly with Vespa, as Vespa can support a wide range of features and ways to retrieve and rank content. The following implements a custom retriever `VespaStreamingHybridRetriever` that takes the following arguments:

*   `app:Vespa` The Vespa application we retrieve from. This could be a Vespa Cloud instance or a local instance, for example running on a laptop.
    
*   `user:str` The user that that we want to retrieve for, this argument maps to the [Vespa streaming mode groupname parameter](https://docs.vespa.ai/en/reference/query-api-reference.html#streaming.groupname)
    
*   `pages:int` The target number of PDF pages we want to retrieve for a given query
    
*   `chunks_per_page` The is the target number of relevant text chunks that are associated with the page
    
*   `chunk_similarity_threshold` - The chunk similarity threshold, only chunks with a similarity above this threshold
    

The core idea is to _retrieve_ pages using maximum chunk similarity as the initial scoring function, then consider other chunks on the same page potentially relevant.

from langchain\_core.documents import Document
from langchain\_core.retrievers import BaseRetriever
from typing import List

class VespaStreamingHybridRetriever(BaseRetriever):
    app: Vespa
    user: str
    pages: int \= 5
    chunks\_per\_page: int \= 3
    chunk\_similarity\_threshold: float \= 0.8

    def \_get\_relevant\_documents(self, query: str) \-\> List\[Document\]:
        response: VespaQueryResponse \= self.app.query(
            yql\="select id, url, title, page, authors, chunks from pdf where userQuery() or ({targetHits:20}nearestNeighbor(embedding,q))",
            groupname\=self.user,
            ranking\="hybrid",
            query\=query,
            hits\=self.pages,
            body\={
                "presentation.format.tensors": "short-value",
                "input.query(q)": f'embed(e5, "query: {query} ")',
            },
            timeout\="2s",
        )
        if not response.is\_successful():
            raise ValueError(
                f"Query failed with status code {response.status\_code}, url={response.url} response={response.json}"
            )
        return self.\_parse\_response(response)

    def \_parse\_response(self, response: VespaQueryResponse) \-\> List\[Document\]:
        documents: List\[Document\] \= \[\]
        for hit in response.hits:
            fields \= hit\["fields"\]
            chunks\_with\_scores \= self.\_get\_chunk\_similarities(fields)
            \## Best k chunks from each page
            best\_chunks\_on\_page \= " ### ".join(
                \[
                    chunk
                    for chunk, score in chunks\_with\_scores\[0 : self.chunks\_per\_page\]
                    if score \> self.chunk\_similarity\_threshold
                \]
            )
            documents.append(
                Document(
                    id\=fields\["id"\],
                    page\_content\=best\_chunks\_on\_page,
                    title\=fields\["title"\],
                    metadata\={
                        "title": fields\["title"\],
                        "url": fields\["url"\],
                        "page": fields\["page"\],
                        "authors": fields\["authors"\],
                        "features": fields\["matchfeatures"\],
                    },
                )
            )
        return documents

    def \_get\_chunk\_similarities(self, hit\_fields: dict) \-\> List\[tuple\]:
        match\_features \= hit\_fields\["matchfeatures"\]
        similarities \= match\_features\["similarities"\]
        chunk\_scores \= \[\]
        for i in range(0, len(similarities)):
            chunk\_scores.append(similarities.get(str(i), 0))
        chunks \= hit\_fields\["chunks"\]
        chunks\_with\_scores \= list(zip(chunks, chunk\_scores))
        return sorted(chunks\_with\_scores, key\=lambda x: x\[1\], reverse\=True)

That’s it! We can give our newborn retriever a spin for the user `jo-bergum` by

vespa\_hybrid\_retriever \= VespaStreamingHybridRetriever(
    app\=app, user\="jo-bergum", pages\=1, chunks\_per\_page\=1
)

vespa\_hybrid\_retriever.get\_relevant\_documents("what is the maxsim operator in colbert?")

\[Document(page\_content='ture that precisely does so. As illustrated, every query embeddinginteracts with all document embeddings via a MaxSim operator,which computes maximum similarity (e.g., cosine similarity), andthe scalar outputs of these operators are summed across queryterms. /T\_his paradigm allows ColBERT to exploit deep LM-basedrepresentations while shi/f\_ting the cost of encoding documents of-/f\_line and amortizing the cost of encoding the query once acrossall ranked documents. Additionally, it enables ColBERT to lever-age vector-similarity search indexes (e.g., \[ 1,15\]) to retrieve thetop-kresults directly from a large document collection, substan-tially improving recall over models that only re-rank the output ofterm-based retrieval.As Figure 1 illustrates, ColBERT can serve queries in tens orfew hundreds of milliseconds. For instance, when used for re-ranking as in “ColBERT (re-rank)”, it delivers over 170 ×speedup(and requires 14,000 ×fewer FLOPs) relative to existing BERT-based', metadata={'title': 'ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT', 'url': 'https://arxiv.org/pdf/2004.12832.pdf', 'page': 4, 'authors': \['Omar Khattab', 'Matei Zaharia'\], 'features': {'closest(embedding)': {'0': 1.0}, 'elementSimilarity(chunks)': 0.41768707482993195, 'nativeRank(chunks)': 0.1401101487033024, 'nativeRank(title)': 0.0520403737720047, 'similarities': {'1': 0.8369992971420288, '0': 0.8730311393737793}}})\]

### RAG[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#RAG "Link to this heading")

Finally, we can connect our custom retriever with the complete flexibility and power of the \[LangChain\] LLM framework. The following uses [LangChain Expression Language, or LCEL](https://python.langchain.com/v0.1/docs/expression_language/), a declarative way to compose chains.

We have several steps composed into a chain:

*   The prompt template and LLM model, in this case using OpenAI
    
*   The retriever that provides the retrieved context for the question
    
*   The formatting of the retrieved context
    

vespa\_hybrid\_retriever \= VespaStreamingHybridRetriever(
    app\=app, user\="jo-bergum", pages\=3, chunks\_per\_page\=3
)

from langchain.chat\_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

prompt\_template \= """
Answer the question based only on the following context.
Cite the page number and the url of the document you are citing.

{context}
Question: {question}
"""
prompt \= ChatPromptTemplate.from\_template(prompt\_template)
model \= ChatOpenAI()

def format\_prompt\_context(docs) \-\> str:
    context \= \[\]
    for d in docs:
        context.append(f"{d.metadata\['title'\]} by {d.metadata\['authors'\]}\\n")
        context.append(f"url: {d.metadata\['url'\]}\\n")
        context.append(f"page: {d.metadata\['page'\]}\\n")
        context.append(f"{d.page\_content}\\n\\n")
    return "".join(context)

chain \= (
    {
        "context": vespa\_hybrid\_retriever | format\_prompt\_context,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)

Interact with the chain[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Interact-with-the-chain "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we can start asking questions using the `chain` define above.

chain.invoke("what is colbert?")

'ColBERT is a ranking model that adapts deep language models, specifically BERT, for efficient retrieval. It introduces a late interaction architecture that independently encodes queries and documents using BERT and then uses a cheap yet powerful interaction step to model their fine-grained similarity. This allows ColBERT to leverage the expressiveness of deep language models while also being able to pre-compute document representations offline, significantly speeding up query processing. ColBERT can be used for re-ranking documents retrieved by a traditional model or for end-to-end retrieval directly from a large document collection. It has been shown to be effective and efficient compared to existing models. (source: ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT by Omar Khattab, Matei Zaharia, page 1, url: https://arxiv.org/pdf/2004.12832.pdf)'

chain.invoke("what is the colbert maxsim operator")

"The ColBERT model utilizes the MaxSim operator, which computes the maximum similarity (e.g., cosine similarity) between query embeddings and document embeddings. The scalar outputs of these operators are summed across query terms, allowing ColBERT to exploit deep LM-based representations while reducing the cost of encoding documents offline and amortizing the cost of encoding the query once across all ranked documents.\\n\\nSource: \\nColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT by \['Omar Khattab', 'Matei Zaharia'\]\\nURL: https://arxiv.org/pdf/2004.12832.pdf\\nPage: 4"

chain.invoke(
    "What is the difference between colbert and single vector representational models?"
)

'The difference between ColBERT and single vector representational models is that ColBERT utilizes a late interaction architecture that independently encodes the query and the document using BERT, while single vector models use a single embedding vector for both the query and the document. This late interaction mechanism in ColBERT allows for fine-grained similarity estimation, which leads to more effective retrieval. (Source: ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT by Omar Khattab and Matei Zaharia, page 17, url: https://arxiv.org/pdf/2004.12832.pdf)'

### Summary[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Summary "Link to this heading")

Vespa’s streaming mode is a game-changer, enabling the creation of highly cost-effective RAG applications for naturally partitioned data.

In this notebook, we delved into the hands-on application of [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction), leveraging document loaders and transformers. Finally, we showcased a custom LangChain retriever that connected all the functionality of LangChain with Vespa.

For those interested in learning more about Vespa, join the [Vespa community on Slack](https://vespatalk.slack.com/) to exchange ideas, seek assistance, or stay in the loop on the latest Vespa developments.

We can now delete the cloud instance:

## Metadata

```json
{
  "title": "Turbocharge RAG with LangChain and Vespa Streaming Mode for Partitioned Data — pyvespa documentation",
  "description": "",
  "url": "https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html",
  "content": "![Image 9: #Vespa](https://assets.vespa.ai/logos/Vespa-logo-dark-RGB.svg)\n\nThis notebook illustrates using [Vespa streaming mode](https://docs.vespa.ai/en/streaming-search.html) to build cost-efficient RAG applications over naturally sharded data.\n\nYou can read more about Vespa vector streaming search in these blog posts:\n\n*   [Announcing vector streaming search: AI assistants at scale without breaking the bank](https://blog.vespa.ai/announcing-vector-streaming-search/)\n    \n*   [Yahoo Mail turns to Vespa to do RAG at scale](https://blog.vespa.ai/yahoo-mail-turns-to-vespa-to-do-rag-at-scale/)\n    \n*   [Hands-On RAG guide for personal data with Vespa and LLamaIndex](https://blog.vespa.ai/scaling-personal-ai-assistants-with-streaming-mode/)\n    \n\nThis notebook is also available in blog form: [Turbocharge RAG with LangChain and Vespa Streaming Mode for Sharded Data](https://blog.vespa.ai/turbocharge-rag-with-langchain-and-vespa-streaming-mode/)\n\nTLDR; Vespa streaming mode for partitioned data[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#TLDR;-Vespa-streaming-mode-for-partitioned-data \"Link to this heading\")\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nVespa’s streaming search solution enables you to integrate a user ID (or any sharding key) into the Vespa document ID. This setup allows Vespa to efficiently group each user’s data on a small set of nodes and the same disk chunk. Streaming mode enables low latency searches on a user’s data without keeping data in memory.\n\nThe key benefits of streaming mode:\n\n*   Eliminating compromises in precision introduced by approximate algorithms\n    \n*   Achieve significantly higher write throughput, thanks to the absence of index builds required for supporting approximate search.\n    \n*   Optimize efficiency by storing documents, including tensors and data, on disk, benefiting from the cost-effective economics of storage tiers.\n    \n*   Storage cost is the primary cost driver of Vespa streaming mode; no data is in memory. Avoiding memory usage lowers deployment costs significantly.\n    \n\nConnecting LangChain Retriever with Vespa for Context Retrieval from PDF Documents[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Connecting-LangChain-Retriever-with-Vespa-for-Context-Retrieval-from-PDF-Documents \"Link to this heading\")\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nIn this notebook, we seamlessly integrate a custom [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction) [retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/) with a Vespa app, leveraging Vespa’s streaming mode to extract meaningful context from PDF documents.\n\nThe workflow\n\n*   Define and deploy a Vespa [application package](https://docs.vespa.ai/en/application-packages.html) using PyVespa.\n    \n*   Utilize [LangChain PDF Loaders](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf) to download and parse PDF files.\n    \n*   Leverage [LangChain Document Transformers](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/) to convert each PDF page into multiple text chunks.\n    \n*   Feed the transformer representation to the running Vespa instance\n    \n*   Employ Vespa’s built-in embedder functionality (using an open-source embedding model) for embedding the text chunks per page, resulting in a multi-vector representation.\n    \n*   Develop a custom [Retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/) to enable seamless retrieval for any unstructured text query.\n    \n\n![Image 10: Overview](https://blog.vespa.ai/assets/2023-12-08-turbocharge-rag-with-langchain-and-vespa-streaming-mode/turbocharge-RAG-vespa-streaming.png)\n\n[![Image 11: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vespa-engine/pyvespa/blob/master/docs/sphinx/source/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.ipynb)\n\nLet’s get started! First, install dependencies:\n\n!pip3 install \\-U pyvespa langchain langchain-community pypdf\\==5.0.1 openai\n\n### Sample data[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Sample-data \"Link to this heading\")\n\nWe love [ColBERT](https://blog.vespa.ai/pretrained-transformer-language-models-for-search-part-3/), so we’ll use a few COlBERT related papers as examples of PDFs in this notebook.\n\ndef sample\\_pdfs():\n    return \\[\n        {\n            \"title\": \"ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction\",\n            \"url\": \"https://arxiv.org/pdf/2112.01488.pdf\",\n            \"authors\": \"Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts, Matei Zaharia\",\n        },\n        {\n            \"title\": \"ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT\",\n            \"url\": \"https://arxiv.org/pdf/2004.12832.pdf\",\n            \"authors\": \"Omar Khattab, Matei Zaharia\",\n        },\n        {\n            \"title\": \"On Approximate Nearest Neighbour Selection for Multi-Stage Dense Retrieval\",\n            \"url\": \"https://arxiv.org/pdf/2108.11480.pdf\",\n            \"authors\": \"Craig Macdonald, Nicola Tonellotto\",\n        },\n        {\n            \"title\": \"A Study on Token Pruning for ColBERT\",\n            \"url\": \"https://arxiv.org/pdf/2112.06540.pdf\",\n            \"authors\": \"Carlos Lassance, Maroua Maachou, Joohee Park, Stéphane Clinchant\",\n        },\n        {\n            \"title\": \"Pseudo-Relevance Feedback for Multiple Representation Dense Retrieval\",\n            \"url\": \"https://arxiv.org/pdf/2106.11251.pdf\",\n            \"authors\": \"Xiao Wang, Craig Macdonald, Nicola Tonellotto, Iadh Ounis\",\n        },\n    \\]\n\n### Defining the Vespa application[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Defining-the-Vespa-application \"Link to this heading\")\n\n[PyVespa](https://pyvespa.readthedocs.io/en/latest/) helps us build the [Vespa application package](https://docs.vespa.ai/en/application-packages.html). A Vespa application package consists of configuration files, schemas, models, and code (plugins).\n\nFirst, we define a [Vespa schema](https://docs.vespa.ai/en/schemas.html) with the fields we want to store and their type.\n\nfrom vespa.package import Schema, Document, Field, FieldSet, HNSW\n\npdf\\_schema \\= Schema(\n    name\\=\"pdf\",\n    mode\\=\"streaming\",\n    document\\=Document(\n        fields\\=\\[\n            Field(name\\=\"id\", type\\=\"string\", indexing\\=\\[\"summary\", \"index\"\\]),\n            Field(name\\=\"title\", type\\=\"string\", indexing\\=\\[\"summary\", \"index\"\\]),\n            Field(name\\=\"url\", type\\=\"string\", indexing\\=\\[\"summary\", \"index\"\\]),\n            Field(name\\=\"authors\", type\\=\"array<string\\>\", indexing\\=\\[\"summary\", \"index\"\\]),\n            Field(name\\=\"page\", type\\=\"int\", indexing\\=\\[\"summary\", \"index\"\\]),\n            Field(\n                name\\=\"metadata\",\n                type\\=\"map<string,string\\>\",\n                indexing\\=\\[\"summary\", \"index\"\\],\n            ),\n            Field(name\\=\"chunks\", type\\=\"array<string\\>\", indexing\\=\\[\"summary\", \"index\"\\]),\n            Field(\n                name\\=\"embedding\",\n                type\\=\"tensor<bfloat16\\>(chunk{}, x\\[384\\])\",\n                indexing\\=\\[\"input chunks\", \"embed e5\", \"attribute\", \"index\"\\],\n                ann\\=HNSW(distance\\_metric\\=\"angular\"),\n                is\\_document\\_field\\=False,\n            ),\n        \\],\n    ),\n    fieldsets\\=\\[FieldSet(name\\=\"default\", fields\\=\\[\"chunks\", \"title\"\\])\\],\n)\n\nThe above defines our `pdf` schema using mode `streaming`. Most fields are straightforward, but take a note of:\n\n*   `metadata` using `map<string,string>` - here we can store and match over page level metadata extracted by the PDF parser.\n    \n*   `chunks` using `array<string>`, these are the text chunks that we use langchain document transformers for\n    \n*   The `embedding` field of type `tensor<bfloat16>(chunk{},x[384])` allows us to store and search the 384-dimensional embeddings per chunk in the same document\n    \n\nThe observant reader might have noticed the `e5` argument to the `embed` expression in the above `embedding` field. The `e5` argument references a component of the type [hugging-face-embedder](https://docs.vespa.ai/en/embedding.html#huggingface-embedder). We configure the application package and its name with the `pdf` schema and the `e5` embedder component.\n\nfrom vespa.package import ApplicationPackage, Component, Parameter\n\nvespa\\_app\\_name \\= \"ragpdfs\"\nvespa\\_application\\_package \\= ApplicationPackage(\n    name\\=vespa\\_app\\_name,\n    schema\\=\\[pdf\\_schema\\],\n    components\\=\\[\n        Component(\n            id\\=\"e5\",\n            type\\=\"hugging-face-embedder\",\n            parameters\\=\\[\n                Parameter(\n                    \"transformer-model\",\n                    {\n                        \"url\": \"https://github.com/vespa-engine/sample-apps/raw/master/simple-semantic-search/model/e5-small-v2-int8.onnx\"\n                    },\n                ),\n                Parameter(\n                    \"tokenizer-model\",\n                    {\n                        \"url\": \"https://raw.githubusercontent.com/vespa-engine/sample-apps/master/simple-semantic-search/model/tokenizer.json\"\n                    },\n                ),\n            \\],\n        )\n    \\],\n)\n\nIn the last step, we configure [ranking](https://docs.vespa.ai/en/ranking.html) by adding `rank-profile`’s to the schema.\n\nVespa supports [phased ranking](https://docs.vespa.ai/en/phased-ranking.html) and has a rich set of built-in [rank-features](https://docs.vespa.ai/en/reference/rank-features.html), including many text-matching features such as:\n\n*   [BM25](https://docs.vespa.ai/en/reference/bm25.html).\n    \n*   [nativeRank](https://docs.vespa.ai/en/reference/nativerank.html) and many more.\n    \n\nUsers can also define custom functions using [ranking expressions](https://docs.vespa.ai/en/reference/ranking-expressions.html). The following defines a `hybrid` Vespa ranking profile.\n\nfrom vespa.package import RankProfile, Function, FirstPhaseRanking\n\nsemantic \\= RankProfile(\n    name\\=\"hybrid\",\n    inputs\\=\\[(\"query(q)\", \"tensor<float\\>(x\\[384\\])\")\\],\n    functions\\=\\[\n        Function(\n            name\\=\"similarities\",\n            expression\\=\"cosine\\_similarity(query(q), attribute(embedding),x)\",\n        )\n    \\],\n    first\\_phase\\=FirstPhaseRanking(\n        expression\\=\"nativeRank(title) + nativeRank(chunks) + reduce(similarities, max, chunk)\",\n        rank\\_score\\_drop\\_limit\\=0.0,\n    ),\n    match\\_features\\=\\[\n        \"closest(embedding)\",\n        \"similarities\",\n        \"nativeRank(chunks)\",\n        \"nativeRank(title)\",\n        \"elementSimilarity(chunks)\",\n    \\],\n)\npdf\\_schema.add\\_rank\\_profile(semantic)\n\nThe `hybrid` rank-profile above defines the query input embedding type and a similarities function that uses a Vespa [tensor compute function](https://docs.vespa.ai/en/reference/ranking-expressions.html#tensor-functions) that calculates the cosine similarity between all the chunk embeddings and the query embedding.\n\nThe profile only defines a single ranking phase, using a linear combination of multiple features.\n\nUsing [match-features](https://docs.vespa.ai/en/reference/schema-reference.html#match-features), Vespa returns selected features along with the hit in the SERP (result page).\n\n### Deploy the application to Vespa Cloud[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Deploy-the-application-to-Vespa-Cloud \"Link to this heading\")\n\nWith the configured application, we can deploy it to [Vespa Cloud](https://cloud.vespa.ai/en/).\n\nTo deploy the application to Vespa Cloud we need to create a tenant in the Vespa Cloud:\n\nCreate a tenant at [console.vespa-cloud.com](https://console.vespa-cloud.com/) (unless you already have one). This step requires a Google or GitHub account, and will start your [free trial](https://cloud.vespa.ai/en/free-trial).\n\nMake note of the tenant name, it is used in the next steps.\n\n> Note: Deployments to dev and perf expire after 7 days of inactivity, i.e., 7 days after running deploy. This applies to all plans, not only the Free Trial. Use the Vespa Console to extend the expiry period, or redeploy the application to add 7 more days.\n\nfrom vespa.deployment import VespaCloud\nimport os\n\n\\# Replace with your tenant name from the Vespa Cloud Console\ntenant\\_name \\= \"vespa-team\"\n\n\\# Key is only used for CI/CD. Can be removed if logging in interactively\nkey \\= os.getenv(\"VESPA\\_TEAM\\_API\\_KEY\", None)\nif key is not None:\n    key \\= key.replace(r\"\\\\n\", \"\\\\n\")  \\# To parse key correctly\n\nvespa\\_cloud \\= VespaCloud(\n    tenant\\=tenant\\_name,\n    application\\=vespa\\_app\\_name,\n    key\\_content\\=key,  \\# Key is only used for CI/CD. Can be removed if logging in interactively\n    application\\_package\\=vespa\\_application\\_package,\n)\n\nNow deploy the app to Vespa Cloud dev zone.\n\nThe first deployment typically takes 2 minutes until the endpoint is up.\n\nfrom vespa.application import Vespa\n\napp: Vespa \\= vespa\\_cloud.deploy()\n\nDeployment started in run 2 of dev-aws-us-east-1c for samples.pdfs. This may take a few minutes the first time.\nINFO    \\[17:23:35\\]  Deploying platform version 8.270.8 and application dev build 2 for dev-aws-us-east-1c of default ...\nINFO    \\[17:23:35\\]  Using CA signed certificate version 0\nWARNING \\[17:23:35\\]  For schema 'pdf', field 'page': Changed to attribute because numerical indexes (field has type int) is not currently supported. Index-only settings may fail. Ignore this warning for streaming search.\nINFO    \\[17:23:35\\]  Using 1 nodes in container cluster 'pdfs\\_container'\nWARNING \\[17:23:36\\]  For streaming search cluster 'pdfs\\_content.pdf', SD field 'embedding': hnsw index is not relevant and not supported, ignoring setting\nWARNING \\[17:23:36\\]  For streaming search cluster 'pdfs\\_content.pdf', SD field 'embedding': hnsw index is not relevant and not supported, ignoring setting\nINFO    \\[17:23:38\\]  Deployment successful.\nINFO    \\[17:23:38\\]  Session 3239 for tenant 'samples' prepared and activated.\nINFO    \\[17:23:38\\]  ######## Details for all nodes ########\nINFO    \\[17:23:38\\]  h88963a.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP\nINFO    \\[17:23:38\\]  --- platform vespa/cloud-tenant-rhel8:8.270.8\nINFO    \\[17:23:38\\]  --- storagenode on port 19102 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  --- searchnode on port 19107 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  --- distributor on port 19111 has config generation 3238, wanted is 3239\nINFO    \\[17:23:38\\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  h88969g.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP\nINFO    \\[17:23:38\\]  --- platform vespa/cloud-tenant-rhel8:8.270.8\nINFO    \\[17:23:38\\]  --- logserver-container on port 4080 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  h88972i.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP\nINFO    \\[17:23:38\\]  --- platform vespa/cloud-tenant-rhel8:8.270.8\nINFO    \\[17:23:38\\]  --- container-clustercontroller on port 19050 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  h89461a.dev.aws-us-east-1c.vespa-external.aws.oath.cloud: expected to be UP\nINFO    \\[17:23:38\\]  --- platform vespa/cloud-tenant-rhel8:8.270.8\nINFO    \\[17:23:38\\]  --- container on port 4080 has config generation 3239, wanted is 3239\nINFO    \\[17:23:38\\]  --- metricsproxy-container on port 19092 has config generation 3239, wanted is 3239\nINFO    \\[17:23:51\\]  Found endpoints:\nINFO    \\[17:23:51\\]  - dev.aws-us-east-1c\nINFO    \\[17:23:51\\]   |-- https://c4f42a1b.bfbdb4fd.z.vespa-app.cloud/ (cluster 'pdfs\\_container')\nINFO    \\[17:23:52\\]  Installation succeeded!\nUsing mTLS (key,cert) Authentication against endpoint https://c4f42a1b.bfbdb4fd.z.vespa-app.cloud//ApplicationStatus\nApplication is up!\nFinished deployment.\n\n### Processing PDFs with LangChain[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Processing-PDFs-with-LangChain \"Link to this heading\")\n\n[LangChain](https://python.langchain.com/) has a rich set of [document loaders](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/) that can be used to load and process various file formats. In this notebook, we use the [PyPDFLoader](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf).\n\nWe also want to split the extracted text into _chunks_ using a [text splitter](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/). Most text embedding models have limited input lengths (typically less than 512 language model tokens, so splitting the text into multiple chunks that fits into the context limit of the embedding model is a common strategy.\n\nFor embedding text data, models based on the Transformer architecture have become the de facto standard. A challenge with Transformer-based models is their input length limitation due to the quadratic self-attention computational complexity. For example, a popular open-source text embedding model like [e5](https://huggingface.co/intfloat/e5-small) has an absolute maximum input length of 512 wordpiece tokens. In addition to the technical limitation, trying to fit more tokens than used during fine-tuning of the model will impact the quality of the vector representation.\n\nOne can view text embedding encoding as a lossy compression technique, where variable-length texts are compressed into a fixed dimensional vector representation.\n\nfrom langchain\\_community.document\\_loaders import PyPDFLoader\nfrom langchain.text\\_splitter import RecursiveCharacterTextSplitter\n\ntext\\_splitter \\= RecursiveCharacterTextSplitter(\n    chunk\\_size\\=1024,  \\# chars, not llm tokens\n    chunk\\_overlap\\=0,\n    length\\_function\\=len,\n    is\\_separator\\_regex\\=False,\n)\n\nThe following iterates over the `sample_pdfs` and performs the following:\n\n*   Load the URL and extract the text into pages. A page is the retrievable unit we will use in Vespa\n    \n*   For each page, use the text splitter to split the text into chunks. The chunks are represented as an `array<string>` in the Vespa schema\n    \n*   Create the page level Vespa `fields`, note that we duplicate some content like the title and URL into the page level representation.\n    \n\nimport hashlib\nimport unicodedata\n\ndef remove\\_control\\_characters(s):\n    return \"\".join(ch for ch in s if unicodedata.category(ch)\\[0\\] != \"C\")\n\nmy\\_docs\\_to\\_feed \\= \\[\\]\nfor pdf in sample\\_pdfs():\n    url \\= pdf\\[\"url\"\\]\n    loader \\= PyPDFLoader(url)\n    pages \\= loader.load\\_and\\_split()\n    for index, page in enumerate(pages):\n        source \\= page.metadata\\[\"source\"\\]\n        chunks \\= text\\_splitter.transform\\_documents(\\[page\\])\n        text\\_chunks \\= \\[chunk.page\\_content for chunk in chunks\\]\n        text\\_chunks \\= \\[remove\\_control\\_characters(chunk) for chunk in text\\_chunks\\]\n        page\\_number \\= index + 1\n        vespa\\_id \\= f\"{url}#{page\\_number}\"\n        hash\\_value \\= hashlib.sha1(vespa\\_id.encode()).hexdigest()\n        fields \\= {\n            \"title\": pdf\\[\"title\"\\],\n            \"url\": url,\n            \"page\": page\\_number,\n            \"id\": hash\\_value,\n            \"authors\": \\[a.strip() for a in pdf\\[\"authors\"\\].split(\",\")\\],\n            \"chunks\": text\\_chunks,\n            \"metadata\": page.metadata,\n        }\n        my\\_docs\\_to\\_feed.append(fields)\n\nNow that we have parsed the input PDFs and created a list of pages that we want to add to Vespa, we must format the list into the format that PyVespa accepts. Notice the `fields`, `id` and `groupname` keys. The `groupname` is the key that is used to shard and co-locate the data and is only relevant when using Vespa with streaming mode.\n\nfrom typing import Iterable\n\ndef vespa\\_feed(user: str) \\-\\> Iterable\\[dict\\]:\n    for doc in my\\_docs\\_to\\_feed:\n        yield {\"fields\": doc, \"id\": doc\\[\"id\"\\], \"groupname\": user}\n\nNow, we can feed to the Vespa instance (`app`), using the `feed_iterable` API, using the generator function above as input with a custom `callback` function. Vespa also performs embedding inference during this step using the built-in Vespa [embedding](https://docs.vespa.ai/en/embedding.html#huggingface-embedder) functionality.\n\nfrom vespa.io import VespaResponse\n\ndef callback(response: VespaResponse, id: str):\n    if not response.is\\_successful():\n        print(\n            f\"Document {id} failed to feed with status code {response.status\\_code}, url={response.url} response={response.json}\"\n        )\n\napp.feed\\_iterable(\n    schema\\=\"pdf\", iter\\=vespa\\_feed(\"jo-bergum\"), namespace\\=\"personal\", callback\\=callback\n)\n\nNotice the `schema` and `namespace` arguments. PyVespa transforms the input operations to Vespa [document v1](https://docs.vespa.ai/en/document-v1-api-guide.html) requests.\n\n![Image 12: Document id](https://blog.vespa.ai/assets/2023-12-08-turbocharge-rag-with-langchain-and-vespa-streaming-mode/docid.png)\n\nQuerying data[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Querying-data \"Link to this heading\")\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nNow, we can also query our data. With [streaming mode](https://docs.vespa.ai/en/reference/query-api-reference.html#streaming), we must pass the `groupname` parameter, or the request will fail with an error.\n\nThe query request uses the Vespa Query API and the `Vespa.query()` function supports passing any of the Vespa query API parameters.\n\nRead more about querying Vespa in:\n\n*   [Vespa Query API](https://docs.vespa.ai/en/query-api.html)\n    \n*   [Vespa Query API reference](https://docs.vespa.ai/en/reference/query-api-reference.html)\n    \n*   [Vespa Query Language API (YQL)](https://docs.vespa.ai/en/query-language.html)\n    \n\nSample query request for `why is colbert effective?` for the user `bergum@vespa.ai`:\n\nfrom vespa.io import VespaQueryResponse\nimport json\n\nresponse: VespaQueryResponse \\= app.query(\n    yql\\=\"select id,title,page,chunks from pdf where userQuery() or ({targetHits:10}nearestNeighbor(embedding,q))\",\n    groupname\\=\"jo-bergum\",\n    ranking\\=\"hybrid\",\n    query\\=\"why is colbert effective?\",\n    body\\={\n        \"presentation.format.tensors\": \"short-value\",\n        \"input.query(q)\": 'embed(e5, \"why is colbert effective?\")',\n    },\n    timeout\\=\"2s\",\n)\nassert response.is\\_successful()\nprint(json.dumps(response.hits\\[0\\], indent\\=2))\n\n{\n  \"id\": \"id:personal:pdf:g=jo-bergum:a4b2ced87807ee9cb0325b7a1c64a070d05a31f7\",\n  \"relevance\": 1.1412738851962692,\n  \"source\": \"pdfs\\_content.pdf\",\n  \"fields\": {\n    \"matchfeatures\": {\n      \"closest(embedding)\": {\n        \"0\": 1.0\n      },\n      \"elementSimilarity(chunks)\": 0.5006379585326953,\n      \"nativeRank(chunks)\": 0.15642522855051508,\n      \"nativeRank(title)\": 0.1341324233922751,\n      \"similarities\": {\n        \"1\": 0.7731813192367554,\n        \"2\": 0.8196794986724854,\n        \"3\": 0.796222984790802,\n        \"4\": 0.7699441909790039,\n        \"0\": 0.850716233253479\n      }\n    },\n    \"id\": \"a4b2ced87807ee9cb0325b7a1c64a070d05a31f7\",\n    \"title\": \"ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT\",\n    \"page\": 9,\n    \"chunks\": \\[\n      \"Sq,d:=\\\\u00d5i\\\\u2208\\[|Eq|\\]maxj\\\\u2208\\[|Ed|\\]Eqi\\\\u00b7ETdj(3)ColBERT is di\\\\ufb00erentiable end-to-end. We /f\\_ine-tune the BERTencoders and train from scratch the additional parameters (i.e., thelinear layer and the \\[Q\\] and \\[D\\] markers\\\\u2019 embeddings) using theAdam \\[ 16\\] optimizer. Notice that our interaction mechanism hasno trainable parameters. Given a triple \\\\u27e8q,d+,d\\\\u2212\\\\u27e9with query q,positive document d+and negative document d\\\\u2212, ColBERT is usedto produce a score for each document individually and is optimizedvia pairwise so/f\\_tmax cross-entropy loss over the computed scoresofd+andd\\\\u2212.3.4 O\\\\ufb00line Indexing: Computing & StoringDocument EmbeddingsBy design, ColBERT isolates almost all of the computations betweenqueries and documents, largely to enable pre-computing documentrepresentations o\\\\ufb04ine. At a high level, our indexing procedure isstraight-forward: we proceed over the documents in the collectionin batches, running our document encoder fDon each batch andstoring the output embeddings per document. Although indexing\",\n      \"a set of documents is an o\\\\ufb04ine process, we incorporate a fewsimple optimizations for enhancing the throughput of indexing. Aswe show in \\\\u00a74.5, these optimizations can considerably reduce theo\\\\ufb04ine cost of indexing.To begin with, we exploit multiple GPUs, if available, for fasterencoding of batches of documents in parallel. When batching, wepad all documents to the maximum length of a document withinthe batch.3To make capping the sequence length on a per-batchbasis more e\\\\ufb00ective, our indexer proceeds through documents ingroups of B(e.g., B=100,000) documents. It sorts these documentsby length and then feeds batches of b(e.g., b=128) documents ofcomparable length through our encoder. /T\\_his length-based bucket-ing is sometimes refered to as a BucketIterator in some libraries(e.g., allenNLP). Lastly, while most computations occur on the GPU,we found that a non-trivial portion of the indexing time is spent onpre-processing the text sequences, primarily BERT\\\\u2019s WordPiece to-\",\n      \"kenization. Exploiting that these operations are independent acrossdocuments in a batch, we parallelize the pre-processing across theavailable CPU cores.Once the document representations are produced, they are savedto disk using 32-bit or 16-bit values to represent each dimension.As we describe in \\\\u00a73.5 and 3.6, these representations are eithersimply loaded from disk for ranking or are subsequently indexedfor vector-similarity search, respectively.3.5 Top- kRe-ranking with ColBERTRecall that ColBERT can be used for re-ranking the output of an-other retrieval model, typically a term-based model, or directlyfor end-to-end retrieval from a document collection. In this sec-tion, we discuss how we use ColBERT for ranking a small set ofk(e.g., k=1000) documents given a query q. Since kis small, werely on batch computations to exhaustively score each document\",\n      \"3/T\\_he public BERT implementations we saw simply pad to a pre-de/f\\_ined length.(unlike our approach in \\\\u00a73.6). To begin with, our query serving sub-system loads the indexed documents representations into memory,representing each document as a matrix of embeddings.Given a query q, we compute its bag of contextualized embed-dings Eq(Equation 1) and, concurrently, gather the document repre-sentations into a 3-dimensional tensor Dconsisting of kdocumentmatrices. We pad the kdocuments to their maximum length tofacilitate batched operations, and move the tensor Dto the GPU\\\\u2019smemory. On the GPU, we compute a batch dot-product of EqandD, possibly over multiple mini-batches. /T\\_he output materializes a3-dimensional tensor that is a collection of cross-match matricesbetween qand each document. To compute the score of each docu-ment, we reduce its matrix across document terms via a max-pool(i.e., representing an exhaustive implementation of our MaxSim\",\n      \"computation) and reduce across query terms via a summation. Fi-nally, we sort the kdocuments by their total scores.\"\n    \\]\n  }\n}\n\nNotice the `matchfeatures` that returns the configured match-features from the rank-profile, including all the chunk similarities.\n\n### LangChain Retriever[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#LangChain-Retriever \"Link to this heading\")\n\nWe use the [LangChain Retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/) interface so that we can connect our Vespa app with the flexibility and power of the [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction) LLM framework.\n\n> A retriever is an interface that returns documents given an unstructured query. It is more general than a vector store. A retriever does not need to be able to store documents, only to return (or retrieve) them. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well.\n\nThe retriever interface fits perfectly with Vespa, as Vespa can support a wide range of features and ways to retrieve and rank content. The following implements a custom retriever `VespaStreamingHybridRetriever` that takes the following arguments:\n\n*   `app:Vespa` The Vespa application we retrieve from. This could be a Vespa Cloud instance or a local instance, for example running on a laptop.\n    \n*   `user:str` The user that that we want to retrieve for, this argument maps to the [Vespa streaming mode groupname parameter](https://docs.vespa.ai/en/reference/query-api-reference.html#streaming.groupname)\n    \n*   `pages:int` The target number of PDF pages we want to retrieve for a given query\n    \n*   `chunks_per_page` The is the target number of relevant text chunks that are associated with the page\n    \n*   `chunk_similarity_threshold` - The chunk similarity threshold, only chunks with a similarity above this threshold\n    \n\nThe core idea is to _retrieve_ pages using maximum chunk similarity as the initial scoring function, then consider other chunks on the same page potentially relevant.\n\nfrom langchain\\_core.documents import Document\nfrom langchain\\_core.retrievers import BaseRetriever\nfrom typing import List\n\nclass VespaStreamingHybridRetriever(BaseRetriever):\n    app: Vespa\n    user: str\n    pages: int \\= 5\n    chunks\\_per\\_page: int \\= 3\n    chunk\\_similarity\\_threshold: float \\= 0.8\n\n    def \\_get\\_relevant\\_documents(self, query: str) \\-\\> List\\[Document\\]:\n        response: VespaQueryResponse \\= self.app.query(\n            yql\\=\"select id, url, title, page, authors, chunks from pdf where userQuery() or ({targetHits:20}nearestNeighbor(embedding,q))\",\n            groupname\\=self.user,\n            ranking\\=\"hybrid\",\n            query\\=query,\n            hits\\=self.pages,\n            body\\={\n                \"presentation.format.tensors\": \"short-value\",\n                \"input.query(q)\": f'embed(e5, \"query: {query} \")',\n            },\n            timeout\\=\"2s\",\n        )\n        if not response.is\\_successful():\n            raise ValueError(\n                f\"Query failed with status code {response.status\\_code}, url={response.url} response={response.json}\"\n            )\n        return self.\\_parse\\_response(response)\n\n    def \\_parse\\_response(self, response: VespaQueryResponse) \\-\\> List\\[Document\\]:\n        documents: List\\[Document\\] \\= \\[\\]\n        for hit in response.hits:\n            fields \\= hit\\[\"fields\"\\]\n            chunks\\_with\\_scores \\= self.\\_get\\_chunk\\_similarities(fields)\n            \\## Best k chunks from each page\n            best\\_chunks\\_on\\_page \\= \" ### \".join(\n                \\[\n                    chunk\n                    for chunk, score in chunks\\_with\\_scores\\[0 : self.chunks\\_per\\_page\\]\n                    if score \\> self.chunk\\_similarity\\_threshold\n                \\]\n            )\n            documents.append(\n                Document(\n                    id\\=fields\\[\"id\"\\],\n                    page\\_content\\=best\\_chunks\\_on\\_page,\n                    title\\=fields\\[\"title\"\\],\n                    metadata\\={\n                        \"title\": fields\\[\"title\"\\],\n                        \"url\": fields\\[\"url\"\\],\n                        \"page\": fields\\[\"page\"\\],\n                        \"authors\": fields\\[\"authors\"\\],\n                        \"features\": fields\\[\"matchfeatures\"\\],\n                    },\n                )\n            )\n        return documents\n\n    def \\_get\\_chunk\\_similarities(self, hit\\_fields: dict) \\-\\> List\\[tuple\\]:\n        match\\_features \\= hit\\_fields\\[\"matchfeatures\"\\]\n        similarities \\= match\\_features\\[\"similarities\"\\]\n        chunk\\_scores \\= \\[\\]\n        for i in range(0, len(similarities)):\n            chunk\\_scores.append(similarities.get(str(i), 0))\n        chunks \\= hit\\_fields\\[\"chunks\"\\]\n        chunks\\_with\\_scores \\= list(zip(chunks, chunk\\_scores))\n        return sorted(chunks\\_with\\_scores, key\\=lambda x: x\\[1\\], reverse\\=True)\n\nThat’s it! We can give our newborn retriever a spin for the user `jo-bergum` by\n\nvespa\\_hybrid\\_retriever \\= VespaStreamingHybridRetriever(\n    app\\=app, user\\=\"jo-bergum\", pages\\=1, chunks\\_per\\_page\\=1\n)\n\nvespa\\_hybrid\\_retriever.get\\_relevant\\_documents(\"what is the maxsim operator in colbert?\")\n\n\\[Document(page\\_content='ture that precisely does so. As illustrated, every query embeddinginteracts with all document embeddings via a MaxSim operator,which computes maximum similarity (e.g., cosine similarity), andthe scalar outputs of these operators are summed across queryterms. /T\\_his paradigm allows ColBERT to exploit deep LM-basedrepresentations while shi/f\\_ting the cost of encoding documents of-/f\\_line and amortizing the cost of encoding the query once acrossall ranked documents. Additionally, it enables ColBERT to lever-age vector-similarity search indexes (e.g., \\[ 1,15\\]) to retrieve thetop-kresults directly from a large document collection, substan-tially improving recall over models that only re-rank the output ofterm-based retrieval.As Figure 1 illustrates, ColBERT can serve queries in tens orfew hundreds of milliseconds. For instance, when used for re-ranking as in “ColBERT (re-rank)”, it delivers over 170 ×speedup(and requires 14,000 ×fewer FLOPs) relative to existing BERT-based', metadata={'title': 'ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT', 'url': 'https://arxiv.org/pdf/2004.12832.pdf', 'page': 4, 'authors': \\['Omar Khattab', 'Matei Zaharia'\\], 'features': {'closest(embedding)': {'0': 1.0}, 'elementSimilarity(chunks)': 0.41768707482993195, 'nativeRank(chunks)': 0.1401101487033024, 'nativeRank(title)': 0.0520403737720047, 'similarities': {'1': 0.8369992971420288, '0': 0.8730311393737793}}})\\]\n\n### RAG[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#RAG \"Link to this heading\")\n\nFinally, we can connect our custom retriever with the complete flexibility and power of the \\[LangChain\\] LLM framework. The following uses [LangChain Expression Language, or LCEL](https://python.langchain.com/v0.1/docs/expression_language/), a declarative way to compose chains.\n\nWe have several steps composed into a chain:\n\n*   The prompt template and LLM model, in this case using OpenAI\n    \n*   The retriever that provides the retrieved context for the question\n    \n*   The formatting of the retrieved context\n    \n\nvespa\\_hybrid\\_retriever \\= VespaStreamingHybridRetriever(\n    app\\=app, user\\=\"jo-bergum\", pages\\=3, chunks\\_per\\_page\\=3\n)\n\nfrom langchain.chat\\_models import ChatOpenAI\nfrom langchain.prompts import ChatPromptTemplate\nfrom langchain.schema import StrOutputParser\nfrom langchain.schema.runnable import RunnablePassthrough\n\nprompt\\_template \\= \"\"\"\nAnswer the question based only on the following context.\nCite the page number and the url of the document you are citing.\n\n{context}\nQuestion: {question}\n\"\"\"\nprompt \\= ChatPromptTemplate.from\\_template(prompt\\_template)\nmodel \\= ChatOpenAI()\n\ndef format\\_prompt\\_context(docs) \\-\\> str:\n    context \\= \\[\\]\n    for d in docs:\n        context.append(f\"{d.metadata\\['title'\\]} by {d.metadata\\['authors'\\]}\\\\n\")\n        context.append(f\"url: {d.metadata\\['url'\\]}\\\\n\")\n        context.append(f\"page: {d.metadata\\['page'\\]}\\\\n\")\n        context.append(f\"{d.page\\_content}\\\\n\\\\n\")\n    return \"\".join(context)\n\nchain \\= (\n    {\n        \"context\": vespa\\_hybrid\\_retriever | format\\_prompt\\_context,\n        \"question\": RunnablePassthrough(),\n    }\n    | prompt\n    | model\n    | StrOutputParser()\n)\n\nInteract with the chain[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Interact-with-the-chain \"Link to this heading\")\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nNow, we can start asking questions using the `chain` define above.\n\nchain.invoke(\"what is colbert?\")\n\n'ColBERT is a ranking model that adapts deep language models, specifically BERT, for efficient retrieval. It introduces a late interaction architecture that independently encodes queries and documents using BERT and then uses a cheap yet powerful interaction step to model their fine-grained similarity. This allows ColBERT to leverage the expressiveness of deep language models while also being able to pre-compute document representations offline, significantly speeding up query processing. ColBERT can be used for re-ranking documents retrieved by a traditional model or for end-to-end retrieval directly from a large document collection. It has been shown to be effective and efficient compared to existing models. (source: ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT by Omar Khattab, Matei Zaharia, page 1, url: https://arxiv.org/pdf/2004.12832.pdf)'\n\nchain.invoke(\"what is the colbert maxsim operator\")\n\n\"The ColBERT model utilizes the MaxSim operator, which computes the maximum similarity (e.g., cosine similarity) between query embeddings and document embeddings. The scalar outputs of these operators are summed across query terms, allowing ColBERT to exploit deep LM-based representations while reducing the cost of encoding documents offline and amortizing the cost of encoding the query once across all ranked documents.\\\\n\\\\nSource: \\\\nColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT by \\['Omar Khattab', 'Matei Zaharia'\\]\\\\nURL: https://arxiv.org/pdf/2004.12832.pdf\\\\nPage: 4\"\n\nchain.invoke(\n    \"What is the difference between colbert and single vector representational models?\"\n)\n\n'The difference between ColBERT and single vector representational models is that ColBERT utilizes a late interaction architecture that independently encodes the query and the document using BERT, while single vector models use a single embedding vector for both the query and the document. This late interaction mechanism in ColBERT allows for fine-grained similarity estimation, which leads to more effective retrieval. (Source: ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT by Omar Khattab and Matei Zaharia, page 17, url: https://arxiv.org/pdf/2004.12832.pdf)'\n\n### Summary[](https://pyvespa.readthedocs.io/en/latest/examples/turbocharge-rag-with-langchain-and-vespa-streaming-mode-cloud.html#Summary \"Link to this heading\")\n\nVespa’s streaming mode is a game-changer, enabling the creation of highly cost-effective RAG applications for naturally partitioned data.\n\nIn this notebook, we delved into the hands-on application of [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction), leveraging document loaders and transformers. Finally, we showcased a custom LangChain retriever that connected all the functionality of LangChain with Vespa.\n\nFor those interested in learning more about Vespa, join the [Vespa community on Slack](https://vespatalk.slack.com/) to exchange ideas, seek assistance, or stay in the loop on the latest Vespa developments.\n\nWe can now delete the cloud instance:",
  "usage": {
    "tokens": 10022
  }
}
```
