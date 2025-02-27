---
title: GitHub - stanford-futuredata/ColBERT: ColBERT: state-of-the-art neural search (SIGIR'20, TACL'21, NeurIPS'21, NAACL'22, CIKM'22, ACL'23, EMNLP'23)
description: ColBERT: state-of-the-art neural search (SIGIR'20, TACL'21, NeurIPS'21, NAACL'22, CIKM'22, ACL'23, EMNLP'23) - stanford-futuredata/ColBERT
url: https://github.com/stanford-futuredata/ColBERT
timestamp: 2025-01-20T15:31:52.976Z
domain: github.com
path: stanford-futuredata_ColBERT
---

# GitHub - stanford-futuredata/ColBERT: ColBERT: state-of-the-art neural search (SIGIR'20, TACL'21, NeurIPS'21, NAACL'22, CIKM'22, ACL'23, EMNLP'23)


ColBERT: state-of-the-art neural search (SIGIR'20, TACL'21, NeurIPS'21, NAACL'22, CIKM'22, ACL'23, EMNLP'23) - stanford-futuredata/ColBERT


## Content

[![Image 30](https://github.com/stanford-futuredata/ColBERT/raw/main/docs/images/colbertofficial.png)](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/images/colbertofficial.png)

ColBERT (v2)
------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#colbert-v2)

### ColBERT is a _fast_ and _accurate_ retrieval model, enabling scalable BERT-based search over large text collections in tens of milliseconds.

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#colbert-is-a-fast-and-accurate-retrieval-model-enabling-scalable-bert-based-search-over-large-text-collections-in-tens-of-milliseconds)

[![Image 31](https://camo.githubusercontent.com/96889048f8a9014fdeba2a891f97150c6aac6e723f5190236b10215a97ed41f3/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/stanford-futuredata/ColBERT/blob/main/docs/intro2new.ipynb)

[![Image 32](https://github.com/stanford-futuredata/ColBERT/raw/main/docs/images/ColBERT-Framework-MaxSim-W370px.png)](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/images/ColBERT-Framework-MaxSim-W370px.png)

**Figure 1:** ColBERT's late interaction, efficiently scoring the fine-grained similarity between a queries and a passage.

As Figure 1 illustrates, ColBERT relies on fine-grained **contextual late interaction**: it encodes each passage into a **matrix** of token-level embeddings (shown above in blue). Then at search time, it embeds every query into another matrix (shown in green) and efficiently finds passages that contextually match the query using scalable vector-similarity (`MaxSim`) operators.

These rich interactions allow ColBERT to surpass the quality of _single-vector_ representation models, while scaling efficiently to large corpora.

#### You can read more in our papers:

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#you-can-read-more-in-our-papers)

*   [**ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT**](https://arxiv.org/abs/2004.12832) (SIGIR'20).
*   [**Relevance-guided Supervision for OpenQA with ColBERT**](https://arxiv.org/abs/2007.00814) (TACL'21).
*   [**Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval**](https://arxiv.org/abs/2101.00436) (NeurIPS'21).
*   [**ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction**](https://arxiv.org/abs/2112.01488) (NAACL'22).
*   [**PLAID: An Efficient Engine for Late Interaction Retrieval**](https://arxiv.org/abs/2205.09707) (CIKM'22).
*   [**Moving Beyond Downstream Task Accuracy for Information Retrieval Benchmarking**](https://arxiv.org/abs/2212.01340) (ACL'23 Findings).
*   [**UDAPDR: Unsupervised Domain Adaptation via LLM Prompting and Distillation of Rerankers**](https://arxiv.org/abs/2303.00807) (EMNLP'23).

* * *

🚨 **Announcements**
--------------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#-announcements)

*   (1/28/24) One of the easiest ways to use ColBERT in applications nowadays is the semi-official, fast-growing [RAGatouille](https://github.com/bclavie/ragatouille) library.
*   (1/29/23) We have merged a new index updater feature and support for additional Hugging Face models! These are in beta so please give us feedback as you try them out.
*   (1/24/23) If you're looking for the **DSPy** framework for composing retrievers like ColBERTv2 and LLMs, it's at: [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

* * *

ColBERTv1
---------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#colbertv1)

The ColBERTv1 code from the SIGIR'20 paper is in the [`colbertv1` branch](https://github.com/stanford-futuredata/ColBERT/tree/colbertv1). See [here](https://github.com/stanford-futuredata/ColBERT?screenshot=true#branches) for more information on other branches.

Installation
------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#installation)

(Update: nowadays you can typically do `pip install colbert-ai[torch,faiss-gpu]` to get things up and running, but if you face issues conda is always more reliable for `faiss` and `torch`.)

ColBERT requires Python 3.7+ and Pytorch 1.9+ and uses the [Hugging Face Transformers](https://github.com/huggingface/transformers) library.

We strongly recommend creating a conda environment using the commands below. (If you don't have conda, follow the official [conda installation guide](https://docs.anaconda.com/anaconda/install/linux/#installation).)

We have also included a new environment file specifically for CPU-only environments (`conda_env_cpu.yml`), but note that if you are testing CPU execution on a machine that includes GPUs you might need to specify `CUDA_VISIBLE_DEVICES=""` as part of your command. Note that a GPU is required for training and indexing.

```
conda env create -f conda_env[_cpu].yml
conda activate colbert
```

If you face any problems, please [open a new issue](https://github.com/stanford-futuredata/ColBERT/issues) and we'll help you promptly!

Overview
--------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#overview)

Using ColBERT on a dataset typically involves the following steps.

**Step 0: Preprocess your collection.** At its simplest, ColBERT works with tab-separated (TSV) files: a file (e.g., `collection.tsv`) will contain all passages and another (e.g., `queries.tsv`) will contain a set of queries for searching the collection.

**Step 1: Download the [pre-trained ColBERTv2 checkpoint](https://downloads.cs.stanford.edu/nlp/data/colbert/colbertv2/colbertv2.0.tar.gz).** This checkpoint has been trained on the MS MARCO Passage Ranking task. You can also _optionally_ [train your own ColBERT model](https://github.com/stanford-futuredata/ColBERT?screenshot=true#training).

**Step 2: Index your collection.** Once you have a trained ColBERT model, you need to [index your collection](https://github.com/stanford-futuredata/ColBERT?screenshot=true#indexing) to permit fast retrieval. This step encodes all passages into matrices, stores them on disk, and builds data structures for efficient search.

**Step 3: Search the collection with your queries.** Given the model and index, you can [issue queries over the collection](https://github.com/stanford-futuredata/ColBERT?screenshot=true#retrieval) to retrieve the top-k passages for each query.

Below, we illustrate these steps via an example run on the MS MARCO Passage Ranking task.

API Usage Notebook
------------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#api-usage-notebook)

**NEW**: We have an experimental notebook on [Google Colab](https://colab.research.google.com/github/stanford-futuredata/ColBERT/blob/main/docs/intro2new.ipynb) that you can use with free GPUs. Indexing 10,000 on the free Colab T4 GPU takes six minutes.

This Jupyter notebook **[docs/intro.ipynb notebook](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/intro.ipynb)** illustrates using the key features of ColBERT with the new Python API.

It includes how to download the ColBERTv2 model checkpoint trained on MS MARCO Passage Ranking and how to download our new LoTTE benchmark.

Data
----

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#data)

This repository works directly with a simple **tab-separated file** format to store queries, passages, and top-k ranked lists.

*   Queries: each line is `qid \t query text`.
*   Collection: each line is `pid \t passage text`.
*   Top-k Ranking: each line is `qid \t pid \t rank`.

This works directly with the data format of the [MS MARCO Passage Ranking](https://github.com/microsoft/MSMARCO-Passage-Ranking) dataset. You will need the training triples (`triples.train.small.tar.gz`), the official top-1000 ranked lists for the dev set queries (`top1000.dev`), and the dev set relevant passages (`qrels.dev.small.tsv`). For indexing the full collection, you will also need the list of passages (`collection.tar.gz`).

Indexing
--------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#indexing)

For fast retrieval, indexing precomputes the ColBERT representations of passages.

Example usage:

from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Indexer

if \_\_name\_\_\=='\_\_main\_\_':
    with Run().context(RunConfig(nranks\=1, experiment\="msmarco")):

        config \= ColBERTConfig(
            nbits\=2,
            root\="/path/to/experiments",
        )
        indexer \= Indexer(checkpoint\="/path/to/checkpoint", config\=config)
        indexer.index(name\="msmarco.nbits=2", collection\="/path/to/MSMARCO/collection.tsv")

Retrieval
---------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#retrieval)

We typically recommend that you use ColBERT for **end-to-end** retrieval, where it directly finds its top-k passages from the full collection:

from colbert.data import Queries
from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Searcher

if \_\_name\_\_\=='\_\_main\_\_':
    with Run().context(RunConfig(nranks\=1, experiment\="msmarco")):

        config \= ColBERTConfig(
            root\="/path/to/experiments",
        )
        searcher \= Searcher(index\="msmarco.nbits=2", config\=config)
        queries \= Queries("/path/to/MSMARCO/queries.dev.small.tsv")
        ranking \= searcher.search\_all(queries, k\=100)
        ranking.save("msmarco.nbits=2.ranking.tsv")

You can optionally specify the `ncells`, `centroid_score_threshold`, and `ndocs` search hyperparameters to trade off between speed and result quality. Defaults for different values of `k` are listed in colbert/searcher.py.

We can evaluate the MSMARCO rankings using the following command:

```
python -m utility.evaluate.msmarco_passages --ranking "/path/to/msmarco.nbits=2.ranking.tsv" --qrels "/path/to/MSMARCO/qrels.dev.small.tsv"
```

Basic Training (ColBERTv1-style)
--------------------------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#basic-training-colbertv1-style)

We provide a [pre-trained model checkpoint](https://downloads.cs.stanford.edu/nlp/data/colbert/colbertv2/colbertv2.0.tar.gz), but we also detail how to train from scratch here. Note that this example demonstrates the ColBERTv1 style of training, but the provided checkpoint was trained with ColBERTv2.

Training requires a JSONL triples file with a `[qid, pid+, pid-]` list per line. The query IDs and passage IDs correspond to the specified `queries.tsv` and `collection.tsv` files respectively.

Example usage (training on 4 GPUs):

from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Trainer

if \_\_name\_\_\=='\_\_main\_\_':
    with Run().context(RunConfig(nranks\=4, experiment\="msmarco")):

        config \= ColBERTConfig(
            bsize\=32,
            root\="/path/to/experiments",
        )
        trainer \= Trainer(
            triples\="/path/to/MSMARCO/triples.train.small.tsv",
            queries\="/path/to/MSMARCO/queries.train.small.tsv",
            collection\="/path/to/MSMARCO/collection.tsv",
            config\=config,
        )

        checkpoint\_path \= trainer.train()

        print(f"Saved checkpoint to {checkpoint\_path}...")

Advanced Training (ColBERTv2-style)
-----------------------------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#advanced-training-colbertv2-style)

from colbert.infra.run import Run
from colbert.infra.config import ColBERTConfig, RunConfig
from colbert import Trainer

def train():
    \# use 4 gpus (e.g. four A100s, but you can use fewer by changing nway,accumsteps,bsize).
    with Run().context(RunConfig(nranks\=4)):
        triples \= '/path/to/examples.64.json'  \# \`wget https://huggingface.co/colbert-ir/colbertv2.0\_msmarco\_64way/resolve/main/examples.json?download=true\` (26GB)
        queries \= '/path/to/MSMARCO/queries.train.tsv'
        collection \= '/path/to/MSMARCO/collection.tsv'

        config \= ColBERTConfig(bsize\=32, lr\=1e-05, warmup\=20\_000, doc\_maxlen\=180, dim\=128, attend\_to\_mask\_tokens\=False, nway\=64, accumsteps\=1, similarity\='cosine', use\_ib\_negatives\=True)
        trainer \= Trainer(triples\=triples, queries\=queries, collection\=collection, config\=config)

        trainer.train(checkpoint\='colbert-ir/colbertv1.9')  \# or start from scratch, like \`bert-base-uncased\`

if \_\_name\_\_ \== '\_\_main\_\_':
    train()

Running a lightweight ColBERTv2 server
--------------------------------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#running-a-lightweight-colbertv2-server)

We provide a script to run a lightweight server which serves k (upto 100) results in ranked order for a given search query, in JSON format. This script can be used to power DSP programs.

To run the server, update the environment variables `INDEX_ROOT` and `INDEX_NAME` in the `.env` file to point to the appropriate ColBERT index. The run the following command:

A sample query:

```
http://localhost:8893/api/search?query=Who won the 2022 FIFA world cup&k=25
```

Branches
--------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#branches)

### Supported branches

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#supported-branches)

*   [`main`](https://github.com/stanford-futuredata/ColBERT/tree/main): Stable branch with ColBERTv2 + PLAID.
*   [`colbertv1`](https://github.com/stanford-futuredata/ColBERT/tree/colbertv1): Legacy branch for ColBERTv1.

### Deprecated branches

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#deprecated-branches)

*   [`new_api`](https://github.com/stanford-futuredata/ColBERT/tree/new_api): Base ColBERTv2 implementation.
*   [`cpu_inference`](https://github.com/stanford-futuredata/ColBERT/tree/cpu_inference): ColBERTv2 implementation with CPU search support.
*   [`fast_search`](https://github.com/stanford-futuredata/ColBERT/tree/fast_search): ColBERTv2 implementation with PLAID.
*   [`binarization`](https://github.com/stanford-futuredata/ColBERT/tree/binarization): ColBERT with a baseline binarization-based compression strategy (as opposed to ColBERTv2's residual compression, which we found to be more robust).

Acknowledgments
---------------

[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#acknowledgments)

ColBERT logo designed by Chuyi Zhang.

## Metadata

```json
{
  "title": "GitHub - stanford-futuredata/ColBERT: ColBERT: state-of-the-art neural search (SIGIR'20, TACL'21, NeurIPS'21, NAACL'22, CIKM'22, ACL'23, EMNLP'23)",
  "description": "ColBERT: state-of-the-art neural search (SIGIR'20, TACL'21, NeurIPS'21, NAACL'22, CIKM'22, ACL'23, EMNLP'23) - stanford-futuredata/ColBERT",
  "url": "https://github.com/stanford-futuredata/ColBERT?screenshot=true",
  "content": "[![Image 30](https://github.com/stanford-futuredata/ColBERT/raw/main/docs/images/colbertofficial.png)](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/images/colbertofficial.png)\n\nColBERT (v2)\n------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#colbert-v2)\n\n### ColBERT is a _fast_ and _accurate_ retrieval model, enabling scalable BERT-based search over large text collections in tens of milliseconds.\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#colbert-is-a-fast-and-accurate-retrieval-model-enabling-scalable-bert-based-search-over-large-text-collections-in-tens-of-milliseconds)\n\n[![Image 31](https://camo.githubusercontent.com/96889048f8a9014fdeba2a891f97150c6aac6e723f5190236b10215a97ed41f3/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/stanford-futuredata/ColBERT/blob/main/docs/intro2new.ipynb)\n\n[![Image 32](https://github.com/stanford-futuredata/ColBERT/raw/main/docs/images/ColBERT-Framework-MaxSim-W370px.png)](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/images/ColBERT-Framework-MaxSim-W370px.png)\n\n**Figure 1:** ColBERT's late interaction, efficiently scoring the fine-grained similarity between a queries and a passage.\n\nAs Figure 1 illustrates, ColBERT relies on fine-grained **contextual late interaction**: it encodes each passage into a **matrix** of token-level embeddings (shown above in blue). Then at search time, it embeds every query into another matrix (shown in green) and efficiently finds passages that contextually match the query using scalable vector-similarity (`MaxSim`) operators.\n\nThese rich interactions allow ColBERT to surpass the quality of _single-vector_ representation models, while scaling efficiently to large corpora.\n\n#### You can read more in our papers:\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#you-can-read-more-in-our-papers)\n\n*   [**ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT**](https://arxiv.org/abs/2004.12832) (SIGIR'20).\n*   [**Relevance-guided Supervision for OpenQA with ColBERT**](https://arxiv.org/abs/2007.00814) (TACL'21).\n*   [**Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval**](https://arxiv.org/abs/2101.00436) (NeurIPS'21).\n*   [**ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction**](https://arxiv.org/abs/2112.01488) (NAACL'22).\n*   [**PLAID: An Efficient Engine for Late Interaction Retrieval**](https://arxiv.org/abs/2205.09707) (CIKM'22).\n*   [**Moving Beyond Downstream Task Accuracy for Information Retrieval Benchmarking**](https://arxiv.org/abs/2212.01340) (ACL'23 Findings).\n*   [**UDAPDR: Unsupervised Domain Adaptation via LLM Prompting and Distillation of Rerankers**](https://arxiv.org/abs/2303.00807) (EMNLP'23).\n\n* * *\n\n🚨 **Announcements**\n--------------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#-announcements)\n\n*   (1/28/24) One of the easiest ways to use ColBERT in applications nowadays is the semi-official, fast-growing [RAGatouille](https://github.com/bclavie/ragatouille) library.\n*   (1/29/23) We have merged a new index updater feature and support for additional Hugging Face models! These are in beta so please give us feedback as you try them out.\n*   (1/24/23) If you're looking for the **DSPy** framework for composing retrievers like ColBERTv2 and LLMs, it's at: [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)\n\n* * *\n\nColBERTv1\n---------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#colbertv1)\n\nThe ColBERTv1 code from the SIGIR'20 paper is in the [`colbertv1` branch](https://github.com/stanford-futuredata/ColBERT/tree/colbertv1). See [here](https://github.com/stanford-futuredata/ColBERT?screenshot=true#branches) for more information on other branches.\n\nInstallation\n------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#installation)\n\n(Update: nowadays you can typically do `pip install colbert-ai[torch,faiss-gpu]` to get things up and running, but if you face issues conda is always more reliable for `faiss` and `torch`.)\n\nColBERT requires Python 3.7+ and Pytorch 1.9+ and uses the [Hugging Face Transformers](https://github.com/huggingface/transformers) library.\n\nWe strongly recommend creating a conda environment using the commands below. (If you don't have conda, follow the official [conda installation guide](https://docs.anaconda.com/anaconda/install/linux/#installation).)\n\nWe have also included a new environment file specifically for CPU-only environments (`conda_env_cpu.yml`), but note that if you are testing CPU execution on a machine that includes GPUs you might need to specify `CUDA_VISIBLE_DEVICES=\"\"` as part of your command. Note that a GPU is required for training and indexing.\n\n```\nconda env create -f conda_env[_cpu].yml\nconda activate colbert\n```\n\nIf you face any problems, please [open a new issue](https://github.com/stanford-futuredata/ColBERT/issues) and we'll help you promptly!\n\nOverview\n--------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#overview)\n\nUsing ColBERT on a dataset typically involves the following steps.\n\n**Step 0: Preprocess your collection.** At its simplest, ColBERT works with tab-separated (TSV) files: a file (e.g., `collection.tsv`) will contain all passages and another (e.g., `queries.tsv`) will contain a set of queries for searching the collection.\n\n**Step 1: Download the [pre-trained ColBERTv2 checkpoint](https://downloads.cs.stanford.edu/nlp/data/colbert/colbertv2/colbertv2.0.tar.gz).** This checkpoint has been trained on the MS MARCO Passage Ranking task. You can also _optionally_ [train your own ColBERT model](https://github.com/stanford-futuredata/ColBERT?screenshot=true#training).\n\n**Step 2: Index your collection.** Once you have a trained ColBERT model, you need to [index your collection](https://github.com/stanford-futuredata/ColBERT?screenshot=true#indexing) to permit fast retrieval. This step encodes all passages into matrices, stores them on disk, and builds data structures for efficient search.\n\n**Step 3: Search the collection with your queries.** Given the model and index, you can [issue queries over the collection](https://github.com/stanford-futuredata/ColBERT?screenshot=true#retrieval) to retrieve the top-k passages for each query.\n\nBelow, we illustrate these steps via an example run on the MS MARCO Passage Ranking task.\n\nAPI Usage Notebook\n------------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#api-usage-notebook)\n\n**NEW**: We have an experimental notebook on [Google Colab](https://colab.research.google.com/github/stanford-futuredata/ColBERT/blob/main/docs/intro2new.ipynb) that you can use with free GPUs. Indexing 10,000 on the free Colab T4 GPU takes six minutes.\n\nThis Jupyter notebook **[docs/intro.ipynb notebook](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/intro.ipynb)** illustrates using the key features of ColBERT with the new Python API.\n\nIt includes how to download the ColBERTv2 model checkpoint trained on MS MARCO Passage Ranking and how to download our new LoTTE benchmark.\n\nData\n----\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#data)\n\nThis repository works directly with a simple **tab-separated file** format to store queries, passages, and top-k ranked lists.\n\n*   Queries: each line is `qid \\t query text`.\n*   Collection: each line is `pid \\t passage text`.\n*   Top-k Ranking: each line is `qid \\t pid \\t rank`.\n\nThis works directly with the data format of the [MS MARCO Passage Ranking](https://github.com/microsoft/MSMARCO-Passage-Ranking) dataset. You will need the training triples (`triples.train.small.tar.gz`), the official top-1000 ranked lists for the dev set queries (`top1000.dev`), and the dev set relevant passages (`qrels.dev.small.tsv`). For indexing the full collection, you will also need the list of passages (`collection.tar.gz`).\n\nIndexing\n--------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#indexing)\n\nFor fast retrieval, indexing precomputes the ColBERT representations of passages.\n\nExample usage:\n\nfrom colbert.infra import Run, RunConfig, ColBERTConfig\nfrom colbert import Indexer\n\nif \\_\\_name\\_\\_\\=='\\_\\_main\\_\\_':\n    with Run().context(RunConfig(nranks\\=1, experiment\\=\"msmarco\")):\n\n        config \\= ColBERTConfig(\n            nbits\\=2,\n            root\\=\"/path/to/experiments\",\n        )\n        indexer \\= Indexer(checkpoint\\=\"/path/to/checkpoint\", config\\=config)\n        indexer.index(name\\=\"msmarco.nbits=2\", collection\\=\"/path/to/MSMARCO/collection.tsv\")\n\nRetrieval\n---------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#retrieval)\n\nWe typically recommend that you use ColBERT for **end-to-end** retrieval, where it directly finds its top-k passages from the full collection:\n\nfrom colbert.data import Queries\nfrom colbert.infra import Run, RunConfig, ColBERTConfig\nfrom colbert import Searcher\n\nif \\_\\_name\\_\\_\\=='\\_\\_main\\_\\_':\n    with Run().context(RunConfig(nranks\\=1, experiment\\=\"msmarco\")):\n\n        config \\= ColBERTConfig(\n            root\\=\"/path/to/experiments\",\n        )\n        searcher \\= Searcher(index\\=\"msmarco.nbits=2\", config\\=config)\n        queries \\= Queries(\"/path/to/MSMARCO/queries.dev.small.tsv\")\n        ranking \\= searcher.search\\_all(queries, k\\=100)\n        ranking.save(\"msmarco.nbits=2.ranking.tsv\")\n\nYou can optionally specify the `ncells`, `centroid_score_threshold`, and `ndocs` search hyperparameters to trade off between speed and result quality. Defaults for different values of `k` are listed in colbert/searcher.py.\n\nWe can evaluate the MSMARCO rankings using the following command:\n\n```\npython -m utility.evaluate.msmarco_passages --ranking \"/path/to/msmarco.nbits=2.ranking.tsv\" --qrels \"/path/to/MSMARCO/qrels.dev.small.tsv\"\n```\n\nBasic Training (ColBERTv1-style)\n--------------------------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#basic-training-colbertv1-style)\n\nWe provide a [pre-trained model checkpoint](https://downloads.cs.stanford.edu/nlp/data/colbert/colbertv2/colbertv2.0.tar.gz), but we also detail how to train from scratch here. Note that this example demonstrates the ColBERTv1 style of training, but the provided checkpoint was trained with ColBERTv2.\n\nTraining requires a JSONL triples file with a `[qid, pid+, pid-]` list per line. The query IDs and passage IDs correspond to the specified `queries.tsv` and `collection.tsv` files respectively.\n\nExample usage (training on 4 GPUs):\n\nfrom colbert.infra import Run, RunConfig, ColBERTConfig\nfrom colbert import Trainer\n\nif \\_\\_name\\_\\_\\=='\\_\\_main\\_\\_':\n    with Run().context(RunConfig(nranks\\=4, experiment\\=\"msmarco\")):\n\n        config \\= ColBERTConfig(\n            bsize\\=32,\n            root\\=\"/path/to/experiments\",\n        )\n        trainer \\= Trainer(\n            triples\\=\"/path/to/MSMARCO/triples.train.small.tsv\",\n            queries\\=\"/path/to/MSMARCO/queries.train.small.tsv\",\n            collection\\=\"/path/to/MSMARCO/collection.tsv\",\n            config\\=config,\n        )\n\n        checkpoint\\_path \\= trainer.train()\n\n        print(f\"Saved checkpoint to {checkpoint\\_path}...\")\n\nAdvanced Training (ColBERTv2-style)\n-----------------------------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#advanced-training-colbertv2-style)\n\nfrom colbert.infra.run import Run\nfrom colbert.infra.config import ColBERTConfig, RunConfig\nfrom colbert import Trainer\n\ndef train():\n    \\# use 4 gpus (e.g. four A100s, but you can use fewer by changing nway,accumsteps,bsize).\n    with Run().context(RunConfig(nranks\\=4)):\n        triples \\= '/path/to/examples.64.json'  \\# \\`wget https://huggingface.co/colbert-ir/colbertv2.0\\_msmarco\\_64way/resolve/main/examples.json?download=true\\` (26GB)\n        queries \\= '/path/to/MSMARCO/queries.train.tsv'\n        collection \\= '/path/to/MSMARCO/collection.tsv'\n\n        config \\= ColBERTConfig(bsize\\=32, lr\\=1e-05, warmup\\=20\\_000, doc\\_maxlen\\=180, dim\\=128, attend\\_to\\_mask\\_tokens\\=False, nway\\=64, accumsteps\\=1, similarity\\='cosine', use\\_ib\\_negatives\\=True)\n        trainer \\= Trainer(triples\\=triples, queries\\=queries, collection\\=collection, config\\=config)\n\n        trainer.train(checkpoint\\='colbert-ir/colbertv1.9')  \\# or start from scratch, like \\`bert-base-uncased\\`\n\nif \\_\\_name\\_\\_ \\== '\\_\\_main\\_\\_':\n    train()\n\nRunning a lightweight ColBERTv2 server\n--------------------------------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#running-a-lightweight-colbertv2-server)\n\nWe provide a script to run a lightweight server which serves k (upto 100) results in ranked order for a given search query, in JSON format. This script can be used to power DSP programs.\n\nTo run the server, update the environment variables `INDEX_ROOT` and `INDEX_NAME` in the `.env` file to point to the appropriate ColBERT index. The run the following command:\n\nA sample query:\n\n```\nhttp://localhost:8893/api/search?query=Who won the 2022 FIFA world cup&k=25\n```\n\nBranches\n--------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#branches)\n\n### Supported branches\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#supported-branches)\n\n*   [`main`](https://github.com/stanford-futuredata/ColBERT/tree/main): Stable branch with ColBERTv2 + PLAID.\n*   [`colbertv1`](https://github.com/stanford-futuredata/ColBERT/tree/colbertv1): Legacy branch for ColBERTv1.\n\n### Deprecated branches\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#deprecated-branches)\n\n*   [`new_api`](https://github.com/stanford-futuredata/ColBERT/tree/new_api): Base ColBERTv2 implementation.\n*   [`cpu_inference`](https://github.com/stanford-futuredata/ColBERT/tree/cpu_inference): ColBERTv2 implementation with CPU search support.\n*   [`fast_search`](https://github.com/stanford-futuredata/ColBERT/tree/fast_search): ColBERTv2 implementation with PLAID.\n*   [`binarization`](https://github.com/stanford-futuredata/ColBERT/tree/binarization): ColBERT with a baseline binarization-based compression strategy (as opposed to ColBERTv2's residual compression, which we found to be more robust).\n\nAcknowledgments\n---------------\n\n[](https://github.com/stanford-futuredata/ColBERT?screenshot=true#acknowledgments)\n\nColBERT logo designed by Chuyi Zhang.",
  "usage": {
    "tokens": 3770
  }
}
```
