---
title: GitHub - castorini/pyserini: Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations.
description: Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations. - castorini/pyserini
url: https://github.com/castorini/pyserini
timestamp: 2025-01-20T15:31:27.938Z
domain: github.com
path: castorini_pyserini
---

# GitHub - castorini/pyserini: Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations.


Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations. - castorini/pyserini


## Content

Pyserini [![Image 38](https://github.com/castorini/pyserini/raw/master/docs/pyserini-logo.png)](https://github.com/castorini/pyserini/blob/master/docs/pyserini-logo.png)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](https://github.com/castorini/pyserini?screenshot=true#pyserini-)

[![Image 39: PyPI](https://camo.githubusercontent.com/5dd470254e7171ee5bf254f147f411ad540e87f5c125f523ec1b4057a0075ffb/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7079736572696e693f636f6c6f723d627269676874677265656e)](https://pypi.org/project/pyserini/) [![Image 40: Downloads](https://camo.githubusercontent.com/ca7561a0115f837c8c6825aa5973269135d84c15cdffe0b2defc24ebf1279e63/68747470733a2f2f7374617469632e706570792e746563682f706572736f6e616c697a65642d62616467652f7079736572696e693f706572696f643d746f74616c26756e6974733d696e7465726e6174696f6e616c5f73797374656d266c6566745f636f6c6f723d677265792672696768745f636f6c6f723d627269676874677265656e266c6566745f746578743d646f776e6c6f616473)](https://pepy.tech/project/pyserini) [![Image 41: PyPI Download Stats](https://camo.githubusercontent.com/e2b41802ac89a74f718e54937207df3a9fdc97bcc7d92cd13ae7732a61d3b74b/68747470733a2f2f696d672e736869656c64732e696f2f707970692f64772f7079736572696e693f636f6c6f723d627269676874677265656e)](https://pypistats.org/packages/pyserini) [![Image 42: Maven Central](https://camo.githubusercontent.com/be8718ac593486711a3e23e5e9e48106ff612e881ac2824d7b3fc54050ec7324/68747470733a2f2f696d672e736869656c64732e696f2f6d6176656e2d63656e7472616c2f762f696f2e616e736572696e692f616e736572696e693f636f6c6f723d627269676874677265656e)](https://search.maven.org/search?q=a:anserini) [![Image 43: Generic badge](https://camo.githubusercontent.com/04742a31d2c25376d3a9bcb32fd7b46d4a427267942d7d315812c81b09281ed6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c7563656e652d76392e392e312d627269676874677265656e2e737667)](https://archive.apache.org/dist/lucene/java/9.9.1/) [![Image 44: LICENSE](https://camo.githubusercontent.com/0ba5a516fcd117d70bacd8930eef23406479a0f93da26cfe10d5ffc9b75718d8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4170616368652d626c75652e7376673f7374796c653d666c6174)](https://www.apache.org/licenses/LICENSE-2.0)

Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations. Retrieval using sparse representations is provided via integration with our group's [Anserini](http://anserini.io/) IR toolkit, which is built on Lucene. Retrieval using dense representations is provided via integration with Facebook's [Faiss](https://github.com/facebookresearch/faiss) library.

Pyserini is primarily designed to provide effective, reproducible, and easy-to-use first-stage retrieval in a multi-stage ranking architecture. Our toolkit is self-contained as a standard Python package and comes with queries, relevance judgments, [prebuilt indexes](https://github.com/castorini/pyserini/blob/master/docs/prebuilt-indexes.md), and evaluation scripts for many commonly used IR test collections. With Pyserini, it's easy to reproduce runs on a number of standard IR test collections!

For additional details, [our paper](https://dl.acm.org/doi/10.1145/3404835.3463238) in SIGIR 2021 provides a nice overview.

✨ **New!** Guide to working with the [MS MARCO 2.1 Document Corpus](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2.1.md) for TREC 2024 RAG Track.

❗ Anserini was upgraded from JDK 11 to JDK 21 at commit [`272565`](https://github.com/castorini/anserini/commit/39cecf6c257bae85f4e9f6ab02e0be101338c3cc) (2024/04/03), which corresponds to the release of v0.35.0. Correspondingly, Pyserini was upgraded to JDK 21 at commit [`b2f677`](https://github.com/castorini/pyserini/commit/b2f677da46e1910c0fd95e5ff06070bc71075401) (2024/04/04).

🎬 Installation
---------------

[](https://github.com/castorini/pyserini?screenshot=true#-installation)

Install via PyPI:

Pyserini is built on Python 3.10 (other versions might work, but YMMV) and Java 21 (due to its dependency on [Anserini](http://anserini.io/)). A `pip` installation will automatically pull in major dependencies such as [PyTorch](https://pytorch.org/), [🤗 Transformers](https://github.com/huggingface/transformers), and the [ONNX Runtime](https://onnxruntime.ai/).

The toolkit also has a number of optional dependencies:

```
pip install 'pyserini[optional]'
```

Notably, `faiss-cpu`, `lightgbm`, and `nmslib` are included in these optional dependencies. Installation of these packages can be temperamental, which is why they are not included in the core dependencies. It might be a good idea to install these yourself separately.

The software ecosystem is rapidly evolving and a potential source of frustration is incompatibility among different versions of underlying dependencies. We provide additional detailed installation instructions [here](https://github.com/castorini/pyserini/blob/master/docs/installation.md).

If you're planning on just _using_ Pyserini, then the `pip` instruction (without the optional dependencies) should be fine. However, if you're planning on contributing to the codebase or want to work with the latest not-yet-released features, you'll need a development installation. Instructions are provided [here](https://github.com/castorini/pyserini/blob/master/docs/installation.md#development-installation).

🙋 How do I search?
-------------------

[](https://github.com/castorini/pyserini?screenshot=true#-how-do-i-search)

Pyserini supports different types of retrieval models. See [this guide](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md) for details on how to search common corpora in IR and NLP research (e.g., MS MARCO, NaturalQuestions, BEIR, etc.) using indexes that we have already built for you. Here are direct links into the guide:

*   [Traditional lexical models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#traditional-lexical-models) (e.g., BM25) using Lucene.
*   [Learned sparse retrieval models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#learned-sparse-retrieval-models) (e.g., uniCOIL, SPLADE, etc.) using Lucene.
*   [Learned dense retrieval models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#learned-dense-retrieval-models) (e.g., DPR, Contriever, BGE, etc.) using Lucene or Faiss.
*   [Hybrid retrieval models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#hybrid-retrieval-models) (e.g., dense-sparse fusion).

Once you get the top-_k_ results, you'll actually want to fetch the document text... See [this guide](https://github.com/castorini/pyserini/blob/master/docs/usage-fetch.md) for how.

🙋 How do I index my own corpus?
--------------------------------

[](https://github.com/castorini/pyserini?screenshot=true#-how-do-i-index-my-own-corpus)

Well, it depends on what type of retrieval model you want to search with:

*   [Building a BM25 Index (Direct Java Implementation)](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-bm25-index-direct-java-implementation)
*   [Building a BM25 Index (Embeddable Python Implementation)](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-bm25-index-embeddable-python-implementation)
*   [Building a Sparse Vector Index](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-sparse-vector-index)
*   [Building a Dense Vector Index](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-dense-vector-index)

The steps are different for different classes of models: [this guide](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md) (same as the links above) describes the details.

🙋 Additional FAQs
------------------

[](https://github.com/castorini/pyserini?screenshot=true#-additional-faqs)

*   [How do I configure search?](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md#how-do-i-configure-search) (Guide to Interactive Search)
*   [How do I manually download indexes?](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md#how-do-i-manually-download-indexes) (Guide to Interactive Search)
*   [How do I perform dense and hybrid retrieval?](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md#how-do-i-perform-dense-and-hybrid-retrieval) (Guide to Interactive Search)
*   [How do I iterate over index terms and access term statistics?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-iterate-over-index-terms-and-access-term-statistics) (Index Reader API)
*   [How do I traverse postings?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-traverse-postings) (Index Reader API)
*   [How do I access and manipulate term vectors?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-access-and-manipulate-term-vectors) (Index Reader API)
*   [How do I compute the tf-idf or BM25 score of a document?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-compute-the-tf-idf-or-BM25-score-of-a-document) (Index Reader API)
*   [How do I access basic index statistics?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-access-basic-index-statistics) (Index Reader API)
*   [How do I access underlying Lucene analyzers?](https://github.com/castorini/pyserini/blob/master/docs/usage-analyzer.md) (Analyzer API)
*   [How do I build custom Lucene queries?](https://github.com/castorini/pyserini/blob/master/docs/usage-querybuilder.md) (Query Builder API)
*   [How do I iterate over raw collections?](https://github.com/castorini/pyserini/blob/master/docs/usage-collection.md) (Collection API)

⚗️ Reproducibility
------------------

[](https://github.com/castorini/pyserini?screenshot=true#%EF%B8%8F-reproducibility)

With Pyserini, it's easy to [reproduce](https://github.com/castorini/pyserini/blob/master/docs/reproducibility.md) runs on a number of standard IR test collections! We provide a number of [prebuilt indexes](https://github.com/castorini/pyserini/blob/master/docs/prebuilt-indexes.md) that directly support reproducibility "out of the box".

In our [SIGIR 2022 paper](https://dl.acm.org/doi/10.1145/3477495.3531749), we introduced "two-click reproductions" that allow anyone to reproduce experimental runs with only two clicks (i.e., copy and paste). Documentation is organized into reproduction matrices for different corpora that provide a summary of different experimental conditions and query sets:

*   [MS MARCO V1 Passage](https://castorini.github.io/pyserini/2cr/msmarco-v1-passage.html)
*   [MS MARCO V1 Document](https://castorini.github.io/pyserini/2cr/msmarco-v1-doc.html)
*   [MS MARCO V2 Passage](https://castorini.github.io/pyserini/2cr/msmarco-v2-passage.html)
*   [MS MARCO V2 Document](https://castorini.github.io/pyserini/2cr/msmarco-v2-doc.html)
*   [BEIR](https://castorini.github.io/pyserini/2cr/beir.html)
*   [Mr.TyDi](https://castorini.github.io/pyserini/2cr/mrtydi.html)
*   [MIRACL](https://castorini.github.io/pyserini/2cr/miracl.html)
*   [Open-Domain Question Answering](https://castorini.github.io/pyserini/2cr/odqa.html)
*   [CIRAL](https://castorini.github.io/pyserini/2cr/ciral.html)

For more details, see our paper on [Building a Culture of Reproducibility in Academic Research](https://arxiv.org/abs/2212.13534).

Additional reproduction guides below provide detailed step-by-step instructions.

Sparse Retrieval

### Sparse Retrieval

[](https://github.com/castorini/pyserini?screenshot=true#sparse-retrieval)

*   Reproducing [Robust04 baselines for ad hoc retrieval](https://github.com/castorini/pyserini/blob/master/docs/experiments-robust04.md)
*   Reproducing the [BM25 baseline for MS MARCO V1 Passage Ranking](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-passage.md)
*   Reproducing the [BM25 baseline for MS MARCO V1 Document Ranking](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-doc.md)
*   Reproducing the [multi-field BM25 baseline for MS MARCO V1 Document Ranking from Elasticsearch](https://github.com/castorini/pyserini/blob/master/docs/experiments-elastic.md)
*   Reproducing [BM25 baselines on the MS MARCO V2 Collections](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2.md)
*   Reproducing LTR filtering experiments: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-ltr-msmarco-passage-reranking.md), [MS MARCO V1 Document](https://github.com/castorini/pyserini/blob/master/docs/experiments-ltr-msmarco-document-reranking.md)
*   Reproducing IRST experiments on the [MS MARCO V1 Collections](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-irst.md)
*   Reproducing DeepImpact: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-deepimpact.md)
*   Reproducing uniCOIL with doc2query-T5: [MS MARCO V1](https://github.com/castorini/pyserini/blob/master/docs/experiments-unicoil.md), [MS MARCO V2](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-unicoil.md)
*   Reproducing uniCOIL with TILDE: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-unicoil-tilde-expansion.md), [MS MARCO V2 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-unicoil-tilde-expansion.md)
*   Reproducing SPLADEv2: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-spladev2.md)
*   Reproducing [Mr. TyDi experiments](https://github.com/castorini/mr.tydi/blob/main/README.md#1-bm25)
*   Reproducing [BM25 baselines for HC4](https://github.com/castorini/pyserini/blob/master/docs/experiments-hc4-v1.0.md)
*   Reproducing [BM25 baselines for HC4 on NeuCLIR22](https://github.com/castorini/pyserini/blob/master/docs/experiments-hc4-neuclir22.md)
*   Reproducing [SLIM experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-slim.md)
*   [Baselines](https://github.com/castorini/pyserini/blob/master/docs/experiments-kilt.md) for [KILT](https://github.com/facebookresearch/KILT): a benchmark for Knowledge Intensive Language Tasks
*   [Baselines](https://github.com/castorini/pyserini/blob/master/docs/experiments-tripclick-doc.md) for [TripClick](https://tripdatabase.github.io/tripclick/): a large-scale dataset of click logs in the health domain
*   [Baselines](https://github.com/castorini/anserini/blob/master/docs/experiments-fever.md) (in Anserini) for the [FEVER (Fact Extraction and VERification)](https://fever.ai/) dataset

Dense Retrieval

### Dense Retrieval

[](https://github.com/castorini/pyserini?screenshot=true#dense-retrieval)

*   Reproducing TCT-ColBERTv1 experiments: [MS MARCO V1](https://github.com/castorini/pyserini/blob/master/docs/experiments-tct_colbert.md)
*   Reproducing TCT-ColBERTv2 experiments: [MS MARCO V1](https://github.com/castorini/pyserini/blob/master/docs/experiments-tct_colbert-v2.md), [MS MARCO V2](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-tct_colbert-v2.md)
*   Reproducing [DPR experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-dpr.md)
*   Reproducing [BPR experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-bpr.md)
*   Reproducing [ANCE experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-ance.md)
*   Reproducing [DistilBERT KD experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-distilbert_kd.md)
*   Reproducing [DistilBERT Balanced Topic Aware Sampling experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-distilbert_tasb.md)
*   Reproducing [SBERT dense retrieval experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-sbert.md)
*   Reproducing [ADORE dense retrieval experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-adore.md)
*   Reproducing [Vector PRF experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-vector-prf.md)
*   Reproducing [ANCE-PRF experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-ance-prf.md)
*   Reproducing [Mr. TyDi experiments](https://github.com/castorini/mr.tydi/blob/main/README.md#2-mdpr)
*   Reproducing [DKRR experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-dkrr.md)

Hybrid Sparse-Dense Retrieval

### Hybrid Sparse-Dense Retrieval

[](https://github.com/castorini/pyserini?screenshot=true#hybrid-sparse-dense-retrieval)

*   Reproducing [uniCOIL + TCT-ColBERTv2 experiments on the MS MARCO V2 Collections](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-hybrid.md)

Available Corpora

### Available Corpora

[](https://github.com/castorini/pyserini?screenshot=true#available-corpora)

| Corpora | Size | Checksum |
| --- | --- | --- |
| [MS MARCO V1 passage: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-passage-unicoil-noexp.tar) | 2.7 GB | `f17ddd8c7c00ff121c3c3b147d2e17d8` |
| [MS MARCO V1 passage: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-passage-unicoil.tar) | 3.4 GB | `78eef752c78c8691f7d61600ceed306f` |
| [MS MARCO V1 doc: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-doc-segmented-unicoil-noexp.tar) | 11 GB | `11b226e1cacd9c8ae0a660fd14cdd710` |
| [MS MARCO V1 doc: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-doc-segmented-unicoil.tar) | 19 GB | `6a00e2c0c375cb1e52c83ae5ac377ebb` |
| [MS MARCO V2 passage: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_passage_unicoil_noexp_0shot.tar) | 24 GB | `d9cc1ed3049746e68a2c91bf90e5212d` |
| [MS MARCO V2 passage: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_passage_unicoil_0shot.tar) | 41 GB | `1949a00bfd5e1f1a230a04bbc1f01539` |
| [MS MARCO V2 doc: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_doc_segmented_unicoil_noexp_0shot_v2.tar) | 55 GB | `97ba262c497164de1054f357caea0c63` |
| [MS MARCO V2 doc: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_doc_segmented_unicoil_0shot_v2.tar) | 72 GB | `c5639748c2cbad0152e10b0ebde3b804` |

📃 Additional Documentation
---------------------------

[](https://github.com/castorini/pyserini?screenshot=true#-additional-documentation)

*   [Guide to prebuilt indexes](https://github.com/castorini/pyserini/blob/master/docs/prebuilt-indexes.md)
*   [Guide to interactive searching](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md)
*   [Guide to text classification with the 20Newsgroups dataset](https://github.com/castorini/pyserini/blob/master/docs/experiments-20newgroups.md)
*   [Guide to working with the COVID-19 Open Research Dataset (CORD-19)](https://github.com/castorini/pyserini/blob/master/docs/working-with-cord19.md)
*   [Guide to working with entity linking](https://github.com/castorini/pyserini/blob/master/docs/working-with-entity-linking.md)
*   [Guide to working with spaCy](https://github.com/castorini/pyserini/blob/master/docs/working-with-spacy.md)
*   [Usage of the Analyzer API](https://github.com/castorini/pyserini/blob/master/docs/usage-analyzer.md)
*   [Usage of the Index Reader API](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md)
*   [Usage of the Query Builder API](https://github.com/castorini/pyserini/blob/master/docs/usage-querybuilder.md)
*   [Usage of the Collection API](https://github.com/castorini/pyserini/blob/master/docs/usage-collection.md)
*   [Direct Interaction via Pyjnius](https://github.com/castorini/pyserini/blob/master/docs/usage-pyjnius.md)

📜️ Release History
-------------------

[](https://github.com/castorini/pyserini?screenshot=true#%EF%B8%8F-release-history)

*   v0.43.0 (w/ Anserini v0.38.0): November 11, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.43.0.md)\]
*   v0.42.0 (w/ Anserini v0.38.0): November 8, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.42.0.md)\] \[[Known Issues](https://github.com/castorini/pyserini/blob/master/docs/release-notes/known-issues-v0.42.0.md)\]
*   v0.41.0 (w/ Anserini v0.38.0): November 7, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.41.0.md)\] \[[Known Issues](https://github.com/castorini/pyserini/blob/master/docs/release-notes/known-issues-v0.41.0.md)\]
*   v0.40.0 (w/ Anserini v0.38.0): October 28, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.40.0.md)\]
*   v0.39.0 (w/ Anserini v0.38.0): September 27, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.39.0.md)\]
*   v0.38.0 (w/ Anserini v0.38.0): September 11, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.38.0.md)\]
*   v0.37.0 (w/ Anserini v0.37.0): August 26, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.37.0.md)\]
*   v0.36.0 (w/ Anserini v0.36.1): June 17, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.36.0.md)\]
*   v0.35.0 (w/ Anserini v0.35.0): April 4, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.35.0.md)\]

older... (and historic notes)

*   v0.25.0 (w/ Anserini v0.25.0): March 31, 2024 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.25.0.md)\]
*   v0.24.0 (w/ Anserini v0.24.0): December 28, 2023 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.24.0.md)\]
*   v0.23.0 (w/ Anserini v0.23.0): November 17, 2023 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.23.0.md)\]
*   v0.22.1 (w/ Anserini v0.22.1): October 19, 2023 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.22.1.md)\]
*   v0.22.0 (w/ Anserini v0.22.0): August 31, 2023 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.22.0.md)\]
*   v0.21.0 (w/ Anserini v0.21.0): April 6, 2023 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.21.0.md)\]
*   v0.20.0 (w/ Anserini v0.20.0): February 1, 2023 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.20.0.md)\]
*   v0.19.2 (w/ Anserini v0.16.2): December 16, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.19.2.md)\]
*   v0.19.1 (w/ Anserini v0.16.1): November 12, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.19.1.md)\]
*   v0.19.0 (w/ Anserini v0.16.1): November 2, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.19.0.md)\] \[[Known Issues](https://github.com/castorini/pyserini/blob/master/docs/release-notes/known-issues-v0.19.0.md)\]
*   v0.18.0 (w/ Anserini v0.15.0): September 26, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.18.0.md)\] (First release based on Lucene 9)
*   v0.17.1 (w/ Anserini v0.14.4): August 13, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.17.1.md)\] (Final release based on Lucene 8)
*   v0.17.0 (w/ Anserini v0.14.3): May 28, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.17.0.md)\]
*   v0.16.1 (w/ Anserini v0.14.3): May 12, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.16.1.md)\]
*   v0.16.0 (w/ Anserini v0.14.1): March 1, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.16.0.md)\]
*   v0.15.0 (w/ Anserini v0.14.0): January 21, 2022 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.15.0.md)\]
*   v0.14.0 (w/ Anserini v0.13.5): November 8, 2021 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.14.0.md)\]
*   v0.13.0 (w/ Anserini v0.13.1): July 3, 2021 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.13.0.md)\]
*   v0.12.0 (w/ Anserini v0.12.0): May 5, 2021 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.12.0.md)\]
*   v0.11.0.0: February 18, 2021 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.11.0.0.md)\]
*   v0.10.1.0: January 8, 2021 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.10.1.0.md)\]
*   v0.10.0.1: December 2, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.10.0.1.md)\]
*   v0.10.0.0: November 26, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.10.0.0.md)\]
*   v0.9.4.0: June 26, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.4.0.md)\]
*   v0.9.3.1: June 11, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.3.1.md)\]
*   v0.9.3.0: May 27, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.3.0.md)\]
*   v0.9.2.0: May 15, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.2.0.md)\]
*   v0.9.1.0: May 6, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.1.0.md)\]
*   v0.9.0.0: April 18, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.0.0.md)\]
*   v0.8.1.0: March 22, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.8.1.0.md)\]
*   v0.8.0.0: March 12, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.8.0.0.md)\]
*   v0.7.2.0: January 25, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.7.2.0.md)\]
*   v0.7.1.0: January 9, 2020 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.7.1.0.md)\]
*   v0.7.0.0: December 13, 2019 \[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.7.0.0.md)\]
*   v0.6.0.0: November 2, 2019

📜️ Historical Notes
--------------------

[](https://github.com/castorini/pyserini?screenshot=true#%EF%B8%8F-historical-notes)

⁉️ **Lucene 8 to Lucene 9 Transition.** In 2022, Pyserini underwent a transition from Lucene 8 to Lucene 9. Most of the prebuilt indexes have been rebuilt using Lucene 9, but there are a few still based on Lucene 8.

More details:

*   [PyPI v0.17.1](https://pypi.org/project/pyserini/0.17.1/) (commit [`33c87c`](https://github.com/castorini/pyserini/commit/33c87c982d543d65e0ba1b4c94ee865fd9a6040e), released 2022/08/13) is the last Pyserini release built on Lucene 8, based on [Anserini v0.14.4](https://github.com/castorini/anserini/releases/tag/anserini-0.14.4). Thereafter, Anserini trunk was upgraded to Lucene 9.
*   [PyPI v0.18.0](https://pypi.org/project/pyserini/0.18.0/) (commit [`5fab14`](https://github.com/castorini/pyserini/commit/5fab143f64ed067ecf619c7d83ecd846aa494fbe), released 2022/09/26) is built on [Anserini v0.15.0](https://github.com/castorini/anserini/releases/tag/anserini-0.15.0), using Lucene 9. Thereafter, Pyserini trunk advanced to Lucene 9.

Explanations:

*   **What's the impact?** Indexes built with Lucene 8 are not fully compatible with Lucene 9 code (see [Anserini #1952](https://github.com/castorini/anserini/issues/1952)). The workaround is to disable consistent tie-breaking, which happens automatically if a Lucene 8 index is detected by Pyserini. However, Lucene 9 code running on Lucene 8 indexes will give slightly different results than Lucene 8 code running on Lucene 8 indexes. Note that Lucene 8 code is _not_ able to read indexes built with Lucene 9.
    
*   **Why is this necessary?** Although disruptive, an upgrade to Lucene 9 is necessary to take advantage of Lucene's HNSW indexes, which will increase the capabilities of Pyserini and open up the design space of dense/sparse hybrids.
    

With v0.11.0.0 and before, Pyserini versions adopted the convention of _X.Y.Z.W_, where _X.Y.Z_ tracks the version of Anserini, and _W_ is used to distinguish different releases on the Python end. Starting with Anserini v0.12.0, Anserini and Pyserini versions have become decoupled.

Anserini is designed to work with JDK 11. There was a JRE path change above JDK 9 that breaks pyjnius 1.2.0, as documented in [this issue](https://github.com/kivy/pyjnius/issues/304), also reported in Anserini [here](https://github.com/castorini/anserini/issues/832) and [here](https://github.com/castorini/anserini/issues/805). This issue was fixed with pyjnius 1.2.1 (released December 2019). The previous error was documented in [this notebook](https://github.com/castorini/anserini-notebooks/blob/master/pyjnius_demo.ipynb) and [this notebook](https://github.com/castorini/anserini-notebooks/blob/master/pyjnius_demo_jvm_issue_fix.ipynb) documents the fix.

✨ References
------------

[](https://github.com/castorini/pyserini?screenshot=true#-references)

If you use Pyserini, please cite the following paper:

```
@INPROCEEDINGS{Lin_etal_SIGIR2021_Pyserini,
   author = "Jimmy Lin and Xueguang Ma and Sheng-Chieh Lin and Jheng-Hong Yang and Ronak Pradeep and Rodrigo Nogueira",
   title = "{Pyserini}: A {Python} Toolkit for Reproducible Information Retrieval Research with Sparse and Dense Representations",
   booktitle = "Proceedings of the 44th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2021)",
   year = 2021,
   pages = "2356--2362",
}
```

🙏 Acknowledgments
------------------

[](https://github.com/castorini/pyserini?screenshot=true#-acknowledgments)

This research is primarily supported in part by the Natural Sciences and Engineering Research Council (NSERC) of Canada.

## Metadata

```json
{
  "title": "GitHub - castorini/pyserini: Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations.",
  "description": "Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations. - castorini/pyserini",
  "url": "https://github.com/castorini/pyserini?screenshot=true",
  "content": "Pyserini [![Image 38](https://github.com/castorini/pyserini/raw/master/docs/pyserini-logo.png)](https://github.com/castorini/pyserini/blob/master/docs/pyserini-logo.png)\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#pyserini-)\n\n[![Image 39: PyPI](https://camo.githubusercontent.com/5dd470254e7171ee5bf254f147f411ad540e87f5c125f523ec1b4057a0075ffb/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7079736572696e693f636f6c6f723d627269676874677265656e)](https://pypi.org/project/pyserini/) [![Image 40: Downloads](https://camo.githubusercontent.com/ca7561a0115f837c8c6825aa5973269135d84c15cdffe0b2defc24ebf1279e63/68747470733a2f2f7374617469632e706570792e746563682f706572736f6e616c697a65642d62616467652f7079736572696e693f706572696f643d746f74616c26756e6974733d696e7465726e6174696f6e616c5f73797374656d266c6566745f636f6c6f723d677265792672696768745f636f6c6f723d627269676874677265656e266c6566745f746578743d646f776e6c6f616473)](https://pepy.tech/project/pyserini) [![Image 41: PyPI Download Stats](https://camo.githubusercontent.com/e2b41802ac89a74f718e54937207df3a9fdc97bcc7d92cd13ae7732a61d3b74b/68747470733a2f2f696d672e736869656c64732e696f2f707970692f64772f7079736572696e693f636f6c6f723d627269676874677265656e)](https://pypistats.org/packages/pyserini) [![Image 42: Maven Central](https://camo.githubusercontent.com/be8718ac593486711a3e23e5e9e48106ff612e881ac2824d7b3fc54050ec7324/68747470733a2f2f696d672e736869656c64732e696f2f6d6176656e2d63656e7472616c2f762f696f2e616e736572696e692f616e736572696e693f636f6c6f723d627269676874677265656e)](https://search.maven.org/search?q=a:anserini) [![Image 43: Generic badge](https://camo.githubusercontent.com/04742a31d2c25376d3a9bcb32fd7b46d4a427267942d7d315812c81b09281ed6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c7563656e652d76392e392e312d627269676874677265656e2e737667)](https://archive.apache.org/dist/lucene/java/9.9.1/) [![Image 44: LICENSE](https://camo.githubusercontent.com/0ba5a516fcd117d70bacd8930eef23406479a0f93da26cfe10d5ffc9b75718d8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4170616368652d626c75652e7376673f7374796c653d666c6174)](https://www.apache.org/licenses/LICENSE-2.0)\n\nPyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations. Retrieval using sparse representations is provided via integration with our group's [Anserini](http://anserini.io/) IR toolkit, which is built on Lucene. Retrieval using dense representations is provided via integration with Facebook's [Faiss](https://github.com/facebookresearch/faiss) library.\n\nPyserini is primarily designed to provide effective, reproducible, and easy-to-use first-stage retrieval in a multi-stage ranking architecture. Our toolkit is self-contained as a standard Python package and comes with queries, relevance judgments, [prebuilt indexes](https://github.com/castorini/pyserini/blob/master/docs/prebuilt-indexes.md), and evaluation scripts for many commonly used IR test collections. With Pyserini, it's easy to reproduce runs on a number of standard IR test collections!\n\nFor additional details, [our paper](https://dl.acm.org/doi/10.1145/3404835.3463238) in SIGIR 2021 provides a nice overview.\n\n✨ **New!** Guide to working with the [MS MARCO 2.1 Document Corpus](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2.1.md) for TREC 2024 RAG Track.\n\n❗ Anserini was upgraded from JDK 11 to JDK 21 at commit [`272565`](https://github.com/castorini/anserini/commit/39cecf6c257bae85f4e9f6ab02e0be101338c3cc) (2024/04/03), which corresponds to the release of v0.35.0. Correspondingly, Pyserini was upgraded to JDK 21 at commit [`b2f677`](https://github.com/castorini/pyserini/commit/b2f677da46e1910c0fd95e5ff06070bc71075401) (2024/04/04).\n\n🎬 Installation\n---------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#-installation)\n\nInstall via PyPI:\n\nPyserini is built on Python 3.10 (other versions might work, but YMMV) and Java 21 (due to its dependency on [Anserini](http://anserini.io/)). A `pip` installation will automatically pull in major dependencies such as [PyTorch](https://pytorch.org/), [🤗 Transformers](https://github.com/huggingface/transformers), and the [ONNX Runtime](https://onnxruntime.ai/).\n\nThe toolkit also has a number of optional dependencies:\n\n```\npip install 'pyserini[optional]'\n```\n\nNotably, `faiss-cpu`, `lightgbm`, and `nmslib` are included in these optional dependencies. Installation of these packages can be temperamental, which is why they are not included in the core dependencies. It might be a good idea to install these yourself separately.\n\nThe software ecosystem is rapidly evolving and a potential source of frustration is incompatibility among different versions of underlying dependencies. We provide additional detailed installation instructions [here](https://github.com/castorini/pyserini/blob/master/docs/installation.md).\n\nIf you're planning on just _using_ Pyserini, then the `pip` instruction (without the optional dependencies) should be fine. However, if you're planning on contributing to the codebase or want to work with the latest not-yet-released features, you'll need a development installation. Instructions are provided [here](https://github.com/castorini/pyserini/blob/master/docs/installation.md#development-installation).\n\n🙋 How do I search?\n-------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#-how-do-i-search)\n\nPyserini supports different types of retrieval models. See [this guide](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md) for details on how to search common corpora in IR and NLP research (e.g., MS MARCO, NaturalQuestions, BEIR, etc.) using indexes that we have already built for you. Here are direct links into the guide:\n\n*   [Traditional lexical models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#traditional-lexical-models) (e.g., BM25) using Lucene.\n*   [Learned sparse retrieval models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#learned-sparse-retrieval-models) (e.g., uniCOIL, SPLADE, etc.) using Lucene.\n*   [Learned dense retrieval models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#learned-dense-retrieval-models) (e.g., DPR, Contriever, BGE, etc.) using Lucene or Faiss.\n*   [Hybrid retrieval models](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md#hybrid-retrieval-models) (e.g., dense-sparse fusion).\n\nOnce you get the top-_k_ results, you'll actually want to fetch the document text... See [this guide](https://github.com/castorini/pyserini/blob/master/docs/usage-fetch.md) for how.\n\n🙋 How do I index my own corpus?\n--------------------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#-how-do-i-index-my-own-corpus)\n\nWell, it depends on what type of retrieval model you want to search with:\n\n*   [Building a BM25 Index (Direct Java Implementation)](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-bm25-index-direct-java-implementation)\n*   [Building a BM25 Index (Embeddable Python Implementation)](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-bm25-index-embeddable-python-implementation)\n*   [Building a Sparse Vector Index](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-sparse-vector-index)\n*   [Building a Dense Vector Index](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md#building-a-dense-vector-index)\n\nThe steps are different for different classes of models: [this guide](https://github.com/castorini/pyserini/blob/master/docs/usage-index.md) (same as the links above) describes the details.\n\n🙋 Additional FAQs\n------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#-additional-faqs)\n\n*   [How do I configure search?](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md#how-do-i-configure-search) (Guide to Interactive Search)\n*   [How do I manually download indexes?](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md#how-do-i-manually-download-indexes) (Guide to Interactive Search)\n*   [How do I perform dense and hybrid retrieval?](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md#how-do-i-perform-dense-and-hybrid-retrieval) (Guide to Interactive Search)\n*   [How do I iterate over index terms and access term statistics?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-iterate-over-index-terms-and-access-term-statistics) (Index Reader API)\n*   [How do I traverse postings?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-traverse-postings) (Index Reader API)\n*   [How do I access and manipulate term vectors?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-access-and-manipulate-term-vectors) (Index Reader API)\n*   [How do I compute the tf-idf or BM25 score of a document?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-compute-the-tf-idf-or-BM25-score-of-a-document) (Index Reader API)\n*   [How do I access basic index statistics?](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md#how-do-i-access-basic-index-statistics) (Index Reader API)\n*   [How do I access underlying Lucene analyzers?](https://github.com/castorini/pyserini/blob/master/docs/usage-analyzer.md) (Analyzer API)\n*   [How do I build custom Lucene queries?](https://github.com/castorini/pyserini/blob/master/docs/usage-querybuilder.md) (Query Builder API)\n*   [How do I iterate over raw collections?](https://github.com/castorini/pyserini/blob/master/docs/usage-collection.md) (Collection API)\n\n⚗️ Reproducibility\n------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#%EF%B8%8F-reproducibility)\n\nWith Pyserini, it's easy to [reproduce](https://github.com/castorini/pyserini/blob/master/docs/reproducibility.md) runs on a number of standard IR test collections! We provide a number of [prebuilt indexes](https://github.com/castorini/pyserini/blob/master/docs/prebuilt-indexes.md) that directly support reproducibility \"out of the box\".\n\nIn our [SIGIR 2022 paper](https://dl.acm.org/doi/10.1145/3477495.3531749), we introduced \"two-click reproductions\" that allow anyone to reproduce experimental runs with only two clicks (i.e., copy and paste). Documentation is organized into reproduction matrices for different corpora that provide a summary of different experimental conditions and query sets:\n\n*   [MS MARCO V1 Passage](https://castorini.github.io/pyserini/2cr/msmarco-v1-passage.html)\n*   [MS MARCO V1 Document](https://castorini.github.io/pyserini/2cr/msmarco-v1-doc.html)\n*   [MS MARCO V2 Passage](https://castorini.github.io/pyserini/2cr/msmarco-v2-passage.html)\n*   [MS MARCO V2 Document](https://castorini.github.io/pyserini/2cr/msmarco-v2-doc.html)\n*   [BEIR](https://castorini.github.io/pyserini/2cr/beir.html)\n*   [Mr.TyDi](https://castorini.github.io/pyserini/2cr/mrtydi.html)\n*   [MIRACL](https://castorini.github.io/pyserini/2cr/miracl.html)\n*   [Open-Domain Question Answering](https://castorini.github.io/pyserini/2cr/odqa.html)\n*   [CIRAL](https://castorini.github.io/pyserini/2cr/ciral.html)\n\nFor more details, see our paper on [Building a Culture of Reproducibility in Academic Research](https://arxiv.org/abs/2212.13534).\n\nAdditional reproduction guides below provide detailed step-by-step instructions.\n\nSparse Retrieval\n\n### Sparse Retrieval\n\n[](https://github.com/castorini/pyserini?screenshot=true#sparse-retrieval)\n\n*   Reproducing [Robust04 baselines for ad hoc retrieval](https://github.com/castorini/pyserini/blob/master/docs/experiments-robust04.md)\n*   Reproducing the [BM25 baseline for MS MARCO V1 Passage Ranking](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-passage.md)\n*   Reproducing the [BM25 baseline for MS MARCO V1 Document Ranking](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-doc.md)\n*   Reproducing the [multi-field BM25 baseline for MS MARCO V1 Document Ranking from Elasticsearch](https://github.com/castorini/pyserini/blob/master/docs/experiments-elastic.md)\n*   Reproducing [BM25 baselines on the MS MARCO V2 Collections](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2.md)\n*   Reproducing LTR filtering experiments: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-ltr-msmarco-passage-reranking.md), [MS MARCO V1 Document](https://github.com/castorini/pyserini/blob/master/docs/experiments-ltr-msmarco-document-reranking.md)\n*   Reproducing IRST experiments on the [MS MARCO V1 Collections](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-irst.md)\n*   Reproducing DeepImpact: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-deepimpact.md)\n*   Reproducing uniCOIL with doc2query-T5: [MS MARCO V1](https://github.com/castorini/pyserini/blob/master/docs/experiments-unicoil.md), [MS MARCO V2](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-unicoil.md)\n*   Reproducing uniCOIL with TILDE: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-unicoil-tilde-expansion.md), [MS MARCO V2 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-unicoil-tilde-expansion.md)\n*   Reproducing SPLADEv2: [MS MARCO V1 Passage](https://github.com/castorini/pyserini/blob/master/docs/experiments-spladev2.md)\n*   Reproducing [Mr. TyDi experiments](https://github.com/castorini/mr.tydi/blob/main/README.md#1-bm25)\n*   Reproducing [BM25 baselines for HC4](https://github.com/castorini/pyserini/blob/master/docs/experiments-hc4-v1.0.md)\n*   Reproducing [BM25 baselines for HC4 on NeuCLIR22](https://github.com/castorini/pyserini/blob/master/docs/experiments-hc4-neuclir22.md)\n*   Reproducing [SLIM experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-slim.md)\n*   [Baselines](https://github.com/castorini/pyserini/blob/master/docs/experiments-kilt.md) for [KILT](https://github.com/facebookresearch/KILT): a benchmark for Knowledge Intensive Language Tasks\n*   [Baselines](https://github.com/castorini/pyserini/blob/master/docs/experiments-tripclick-doc.md) for [TripClick](https://tripdatabase.github.io/tripclick/): a large-scale dataset of click logs in the health domain\n*   [Baselines](https://github.com/castorini/anserini/blob/master/docs/experiments-fever.md) (in Anserini) for the [FEVER (Fact Extraction and VERification)](https://fever.ai/) dataset\n\nDense Retrieval\n\n### Dense Retrieval\n\n[](https://github.com/castorini/pyserini?screenshot=true#dense-retrieval)\n\n*   Reproducing TCT-ColBERTv1 experiments: [MS MARCO V1](https://github.com/castorini/pyserini/blob/master/docs/experiments-tct_colbert.md)\n*   Reproducing TCT-ColBERTv2 experiments: [MS MARCO V1](https://github.com/castorini/pyserini/blob/master/docs/experiments-tct_colbert-v2.md), [MS MARCO V2](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-tct_colbert-v2.md)\n*   Reproducing [DPR experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-dpr.md)\n*   Reproducing [BPR experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-bpr.md)\n*   Reproducing [ANCE experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-ance.md)\n*   Reproducing [DistilBERT KD experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-distilbert_kd.md)\n*   Reproducing [DistilBERT Balanced Topic Aware Sampling experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-distilbert_tasb.md)\n*   Reproducing [SBERT dense retrieval experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-sbert.md)\n*   Reproducing [ADORE dense retrieval experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-adore.md)\n*   Reproducing [Vector PRF experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-vector-prf.md)\n*   Reproducing [ANCE-PRF experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-ance-prf.md)\n*   Reproducing [Mr. TyDi experiments](https://github.com/castorini/mr.tydi/blob/main/README.md#2-mdpr)\n*   Reproducing [DKRR experiments](https://github.com/castorini/pyserini/blob/master/docs/experiments-dkrr.md)\n\nHybrid Sparse-Dense Retrieval\n\n### Hybrid Sparse-Dense Retrieval\n\n[](https://github.com/castorini/pyserini?screenshot=true#hybrid-sparse-dense-retrieval)\n\n*   Reproducing [uniCOIL + TCT-ColBERTv2 experiments on the MS MARCO V2 Collections](https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-v2-hybrid.md)\n\nAvailable Corpora\n\n### Available Corpora\n\n[](https://github.com/castorini/pyserini?screenshot=true#available-corpora)\n\n| Corpora | Size | Checksum |\n| --- | --- | --- |\n| [MS MARCO V1 passage: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-passage-unicoil-noexp.tar) | 2.7 GB | `f17ddd8c7c00ff121c3c3b147d2e17d8` |\n| [MS MARCO V1 passage: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-passage-unicoil.tar) | 3.4 GB | `78eef752c78c8691f7d61600ceed306f` |\n| [MS MARCO V1 doc: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-doc-segmented-unicoil-noexp.tar) | 11 GB | `11b226e1cacd9c8ae0a660fd14cdd710` |\n| [MS MARCO V1 doc: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco-doc-segmented-unicoil.tar) | 19 GB | `6a00e2c0c375cb1e52c83ae5ac377ebb` |\n| [MS MARCO V2 passage: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_passage_unicoil_noexp_0shot.tar) | 24 GB | `d9cc1ed3049746e68a2c91bf90e5212d` |\n| [MS MARCO V2 passage: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_passage_unicoil_0shot.tar) | 41 GB | `1949a00bfd5e1f1a230a04bbc1f01539` |\n| [MS MARCO V2 doc: uniCOIL (noexp)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_doc_segmented_unicoil_noexp_0shot_v2.tar) | 55 GB | `97ba262c497164de1054f357caea0c63` |\n| [MS MARCO V2 doc: uniCOIL (d2q-T5)](https://rgw.cs.uwaterloo.ca/JIMMYLIN-bucket0/data/msmarco_v2_doc_segmented_unicoil_0shot_v2.tar) | 72 GB | `c5639748c2cbad0152e10b0ebde3b804` |\n\n📃 Additional Documentation\n---------------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#-additional-documentation)\n\n*   [Guide to prebuilt indexes](https://github.com/castorini/pyserini/blob/master/docs/prebuilt-indexes.md)\n*   [Guide to interactive searching](https://github.com/castorini/pyserini/blob/master/docs/usage-interactive-search.md)\n*   [Guide to text classification with the 20Newsgroups dataset](https://github.com/castorini/pyserini/blob/master/docs/experiments-20newgroups.md)\n*   [Guide to working with the COVID-19 Open Research Dataset (CORD-19)](https://github.com/castorini/pyserini/blob/master/docs/working-with-cord19.md)\n*   [Guide to working with entity linking](https://github.com/castorini/pyserini/blob/master/docs/working-with-entity-linking.md)\n*   [Guide to working with spaCy](https://github.com/castorini/pyserini/blob/master/docs/working-with-spacy.md)\n*   [Usage of the Analyzer API](https://github.com/castorini/pyserini/blob/master/docs/usage-analyzer.md)\n*   [Usage of the Index Reader API](https://github.com/castorini/pyserini/blob/master/docs/usage-indexreader.md)\n*   [Usage of the Query Builder API](https://github.com/castorini/pyserini/blob/master/docs/usage-querybuilder.md)\n*   [Usage of the Collection API](https://github.com/castorini/pyserini/blob/master/docs/usage-collection.md)\n*   [Direct Interaction via Pyjnius](https://github.com/castorini/pyserini/blob/master/docs/usage-pyjnius.md)\n\n📜️ Release History\n-------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#%EF%B8%8F-release-history)\n\n*   v0.43.0 (w/ Anserini v0.38.0): November 11, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.43.0.md)\\]\n*   v0.42.0 (w/ Anserini v0.38.0): November 8, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.42.0.md)\\] \\[[Known Issues](https://github.com/castorini/pyserini/blob/master/docs/release-notes/known-issues-v0.42.0.md)\\]\n*   v0.41.0 (w/ Anserini v0.38.0): November 7, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.41.0.md)\\] \\[[Known Issues](https://github.com/castorini/pyserini/blob/master/docs/release-notes/known-issues-v0.41.0.md)\\]\n*   v0.40.0 (w/ Anserini v0.38.0): October 28, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.40.0.md)\\]\n*   v0.39.0 (w/ Anserini v0.38.0): September 27, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.39.0.md)\\]\n*   v0.38.0 (w/ Anserini v0.38.0): September 11, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.38.0.md)\\]\n*   v0.37.0 (w/ Anserini v0.37.0): August 26, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.37.0.md)\\]\n*   v0.36.0 (w/ Anserini v0.36.1): June 17, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.36.0.md)\\]\n*   v0.35.0 (w/ Anserini v0.35.0): April 4, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.35.0.md)\\]\n\nolder... (and historic notes)\n\n*   v0.25.0 (w/ Anserini v0.25.0): March 31, 2024 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.25.0.md)\\]\n*   v0.24.0 (w/ Anserini v0.24.0): December 28, 2023 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.24.0.md)\\]\n*   v0.23.0 (w/ Anserini v0.23.0): November 17, 2023 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.23.0.md)\\]\n*   v0.22.1 (w/ Anserini v0.22.1): October 19, 2023 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.22.1.md)\\]\n*   v0.22.0 (w/ Anserini v0.22.0): August 31, 2023 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.22.0.md)\\]\n*   v0.21.0 (w/ Anserini v0.21.0): April 6, 2023 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.21.0.md)\\]\n*   v0.20.0 (w/ Anserini v0.20.0): February 1, 2023 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.20.0.md)\\]\n*   v0.19.2 (w/ Anserini v0.16.2): December 16, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.19.2.md)\\]\n*   v0.19.1 (w/ Anserini v0.16.1): November 12, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.19.1.md)\\]\n*   v0.19.0 (w/ Anserini v0.16.1): November 2, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.19.0.md)\\] \\[[Known Issues](https://github.com/castorini/pyserini/blob/master/docs/release-notes/known-issues-v0.19.0.md)\\]\n*   v0.18.0 (w/ Anserini v0.15.0): September 26, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.18.0.md)\\] (First release based on Lucene 9)\n*   v0.17.1 (w/ Anserini v0.14.4): August 13, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.17.1.md)\\] (Final release based on Lucene 8)\n*   v0.17.0 (w/ Anserini v0.14.3): May 28, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.17.0.md)\\]\n*   v0.16.1 (w/ Anserini v0.14.3): May 12, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.16.1.md)\\]\n*   v0.16.0 (w/ Anserini v0.14.1): March 1, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.16.0.md)\\]\n*   v0.15.0 (w/ Anserini v0.14.0): January 21, 2022 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.15.0.md)\\]\n*   v0.14.0 (w/ Anserini v0.13.5): November 8, 2021 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.14.0.md)\\]\n*   v0.13.0 (w/ Anserini v0.13.1): July 3, 2021 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.13.0.md)\\]\n*   v0.12.0 (w/ Anserini v0.12.0): May 5, 2021 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.12.0.md)\\]\n*   v0.11.0.0: February 18, 2021 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.11.0.0.md)\\]\n*   v0.10.1.0: January 8, 2021 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.10.1.0.md)\\]\n*   v0.10.0.1: December 2, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.10.0.1.md)\\]\n*   v0.10.0.0: November 26, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.10.0.0.md)\\]\n*   v0.9.4.0: June 26, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.4.0.md)\\]\n*   v0.9.3.1: June 11, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.3.1.md)\\]\n*   v0.9.3.0: May 27, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.3.0.md)\\]\n*   v0.9.2.0: May 15, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.2.0.md)\\]\n*   v0.9.1.0: May 6, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.1.0.md)\\]\n*   v0.9.0.0: April 18, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.9.0.0.md)\\]\n*   v0.8.1.0: March 22, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.8.1.0.md)\\]\n*   v0.8.0.0: March 12, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.8.0.0.md)\\]\n*   v0.7.2.0: January 25, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.7.2.0.md)\\]\n*   v0.7.1.0: January 9, 2020 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.7.1.0.md)\\]\n*   v0.7.0.0: December 13, 2019 \\[[Release Notes](https://github.com/castorini/pyserini/blob/master/docs/release-notes/release-notes-v0.7.0.0.md)\\]\n*   v0.6.0.0: November 2, 2019\n\n📜️ Historical Notes\n--------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#%EF%B8%8F-historical-notes)\n\n⁉️ **Lucene 8 to Lucene 9 Transition.** In 2022, Pyserini underwent a transition from Lucene 8 to Lucene 9. Most of the prebuilt indexes have been rebuilt using Lucene 9, but there are a few still based on Lucene 8.\n\nMore details:\n\n*   [PyPI v0.17.1](https://pypi.org/project/pyserini/0.17.1/) (commit [`33c87c`](https://github.com/castorini/pyserini/commit/33c87c982d543d65e0ba1b4c94ee865fd9a6040e), released 2022/08/13) is the last Pyserini release built on Lucene 8, based on [Anserini v0.14.4](https://github.com/castorini/anserini/releases/tag/anserini-0.14.4). Thereafter, Anserini trunk was upgraded to Lucene 9.\n*   [PyPI v0.18.0](https://pypi.org/project/pyserini/0.18.0/) (commit [`5fab14`](https://github.com/castorini/pyserini/commit/5fab143f64ed067ecf619c7d83ecd846aa494fbe), released 2022/09/26) is built on [Anserini v0.15.0](https://github.com/castorini/anserini/releases/tag/anserini-0.15.0), using Lucene 9. Thereafter, Pyserini trunk advanced to Lucene 9.\n\nExplanations:\n\n*   **What's the impact?** Indexes built with Lucene 8 are not fully compatible with Lucene 9 code (see [Anserini #1952](https://github.com/castorini/anserini/issues/1952)). The workaround is to disable consistent tie-breaking, which happens automatically if a Lucene 8 index is detected by Pyserini. However, Lucene 9 code running on Lucene 8 indexes will give slightly different results than Lucene 8 code running on Lucene 8 indexes. Note that Lucene 8 code is _not_ able to read indexes built with Lucene 9.\n    \n*   **Why is this necessary?** Although disruptive, an upgrade to Lucene 9 is necessary to take advantage of Lucene's HNSW indexes, which will increase the capabilities of Pyserini and open up the design space of dense/sparse hybrids.\n    \n\nWith v0.11.0.0 and before, Pyserini versions adopted the convention of _X.Y.Z.W_, where _X.Y.Z_ tracks the version of Anserini, and _W_ is used to distinguish different releases on the Python end. Starting with Anserini v0.12.0, Anserini and Pyserini versions have become decoupled.\n\nAnserini is designed to work with JDK 11. There was a JRE path change above JDK 9 that breaks pyjnius 1.2.0, as documented in [this issue](https://github.com/kivy/pyjnius/issues/304), also reported in Anserini [here](https://github.com/castorini/anserini/issues/832) and [here](https://github.com/castorini/anserini/issues/805). This issue was fixed with pyjnius 1.2.1 (released December 2019). The previous error was documented in [this notebook](https://github.com/castorini/anserini-notebooks/blob/master/pyjnius_demo.ipynb) and [this notebook](https://github.com/castorini/anserini-notebooks/blob/master/pyjnius_demo_jvm_issue_fix.ipynb) documents the fix.\n\n✨ References\n------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#-references)\n\nIf you use Pyserini, please cite the following paper:\n\n```\n@INPROCEEDINGS{Lin_etal_SIGIR2021_Pyserini,\n   author = \"Jimmy Lin and Xueguang Ma and Sheng-Chieh Lin and Jheng-Hong Yang and Ronak Pradeep and Rodrigo Nogueira\",\n   title = \"{Pyserini}: A {Python} Toolkit for Reproducible Information Retrieval Research with Sparse and Dense Representations\",\n   booktitle = \"Proceedings of the 44th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2021)\",\n   year = 2021,\n   pages = \"2356--2362\",\n}\n```\n\n🙏 Acknowledgments\n------------------\n\n[](https://github.com/castorini/pyserini?screenshot=true#-acknowledgments)\n\nThis research is primarily supported in part by the Natural Sciences and Engineering Research Council (NSERC) of Canada.",
  "usage": {
    "tokens": 9652
  }
}
```
