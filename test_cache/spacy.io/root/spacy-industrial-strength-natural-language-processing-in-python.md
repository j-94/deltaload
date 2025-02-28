---
title: spaCy · Industrial-strength Natural Language Processing in Python
description: spaCy is a free open-source library for Natural Language Processing in Python. It features NER, POS tagging, dependency parsing, word vectors and more.
url: https://spacy.io/
timestamp: 2025-01-20T15:49:49.657Z
domain: spacy.io
path: root
---

# spaCy · Industrial-strength Natural Language Processing in Python


spaCy is a free open-source library for Natural Language Processing in Python. It features NER, POS tagging, dependency parsing, word vectors and more.


## Content

Industrial-Strength  
Natural Language  
Processing
---------------------------------------------------

in Python
---------

### Get things done

spaCy is designed to help you do real work — to build real products, or gather real insights. The library respects your time, and tries to avoid wasting it. It's easy to install, and its API is simple and productive.

### Blazing fast

spaCy excels at large-scale information extraction tasks. It's written from the ground up in carefully memory-managed Cython. If your application needs to process entire web dumps, spaCy is the library you want to be using.

### Awesome ecosystem

Since its release in 2015, spaCy has become an industry standard with a huge ecosystem. Choose from a variety of plugins, integrate with your machine learning stack and build custom components and workflows.

#### Edit the code & try spaCyspaCy v3.7 · Python 3 · via [Binder](https://mybinder.org/)

Features
--------

*   Support for **75\+ languages**
*   **84 trained pipelines** for 25 languages
*   Multi-task learning with pretrained **transformers** like BERT
*   Pretrained **word vectors**
*   State-of-the-art speed
*   Production-ready **training system**
*   Linguistically-motivated **tokenization**
*   Components for **named entity** recognition, part-of-speech tagging, dependency parsing, sentence segmentation, **text classification**, lemmatization, morphological analysis, entity linking and more
*   Easily extensible with **custom components** and attributes
*   Support for custom models in **PyTorch**, **TensorFlow** and other frameworks
*   Built in **visualizers** for syntax and NER
*   Easy **model packaging**, deployment and workflow management
*   Robust, rigorously evaluated accuracy

Reproducible training for custom pipelines
------------------------------------------

spaCy v3.0 introduces a comprehensive and extensible system for **configuring your training runs**. Your configuration file will describe every detail of your training run, with no hidden defaults, making it easy to **rerun your experiments** and track changes. You can use the quickstart widget or the [`init config`](https://spacy.io/api/cli#init-config) command to get started, or clone a project template for an end-to-end workflow.

[Get started](https://spacy.io/usage/training)

Components

taggermorphologizertrainable\_lemmatizerparsernerspancattextcat

Hardware

CPUGPU (transformer)

Optimize for

efficiencyaccuracy

```
# This is an auto-generated partial config. To use it with 'spacy train'
# you can run spacy init fill-config to auto-fill all default settings:
# python -m spacy init fill-config ./base_config.cfg ./config.cfg
[paths]
train = null
dev = null
vectors = null
[system]
gpu_allocator = null

[nlp]
lang = "en"
pipeline = []
batch_size = 1000

[components]

[corpora]

[corpora.train]
@readers = "spacy.Corpus.v1"
path = ${paths.train}
max_length = 0

[corpora.dev]
@readers = "spacy.Corpus.v1"
path = ${paths.dev}
max_length = 0

[training]
dev_corpus = "corpora.dev"
train_corpus = "corpora.train"

[training.optimizer]
@optimizers = "Adam.v1"

[training.batcher]
@batchers = "spacy.batch_by_words.v1"
discard_oversize = false
tolerance = 0.2

[training.batcher.size]
@schedules = "compounding.v1"
start = 100
stop = 1000
compound = 1.001

[initialize]
vectors = ${paths.vectors}
```

End-to-end workflows from prototype to production
-------------------------------------------------

spaCy's new project system gives you a smooth path from prototype to production. It lets you keep track of all those **data transformation**, preprocessing and **training steps**, so you can make sure your project is always ready to hand over for automation. It features source asset download, command execution, checksum verification, and caching with a variety of backends and integrations.

[Try it out](https://spacy.io/usage/projects)

Benchmarks
----------

spaCy v3.0 introduces transformer-based pipelines that bring spaCy's accuracy right up to the current **state-of-the-art**. You can also use a CPU-optimized pipeline, which is less accurate but much cheaper to run.

[More results](https://spacy.io/usage/facts-figures#benchmarks)

## Metadata

```json
{
  "title": "spaCy · Industrial-strength Natural Language Processing in Python",
  "description": "spaCy is a free open-source library for Natural Language Processing in Python. It features NER, POS tagging, dependency parsing, word vectors and more.",
  "url": "https://spacy.io/",
  "content": "Industrial-Strength  \nNatural Language  \nProcessing\n---------------------------------------------------\n\nin Python\n---------\n\n### Get things done\n\nspaCy is designed to help you do real work — to build real products, or gather real insights. The library respects your time, and tries to avoid wasting it. It's easy to install, and its API is simple and productive.\n\n### Blazing fast\n\nspaCy excels at large-scale information extraction tasks. It's written from the ground up in carefully memory-managed Cython. If your application needs to process entire web dumps, spaCy is the library you want to be using.\n\n### Awesome ecosystem\n\nSince its release in 2015, spaCy has become an industry standard with a huge ecosystem. Choose from a variety of plugins, integrate with your machine learning stack and build custom components and workflows.\n\n#### Edit the code & try spaCyspaCy v3.7 · Python 3 · via [Binder](https://mybinder.org/)\n\nFeatures\n--------\n\n*   Support for **75\\+ languages**\n*   **84 trained pipelines** for 25 languages\n*   Multi-task learning with pretrained **transformers** like BERT\n*   Pretrained **word vectors**\n*   State-of-the-art speed\n*   Production-ready **training system**\n*   Linguistically-motivated **tokenization**\n*   Components for **named entity** recognition, part-of-speech tagging, dependency parsing, sentence segmentation, **text classification**, lemmatization, morphological analysis, entity linking and more\n*   Easily extensible with **custom components** and attributes\n*   Support for custom models in **PyTorch**, **TensorFlow** and other frameworks\n*   Built in **visualizers** for syntax and NER\n*   Easy **model packaging**, deployment and workflow management\n*   Robust, rigorously evaluated accuracy\n\nReproducible training for custom pipelines\n------------------------------------------\n\nspaCy v3.0 introduces a comprehensive and extensible system for **configuring your training runs**. Your configuration file will describe every detail of your training run, with no hidden defaults, making it easy to **rerun your experiments** and track changes. You can use the quickstart widget or the [`init config`](https://spacy.io/api/cli#init-config) command to get started, or clone a project template for an end-to-end workflow.\n\n[Get started](https://spacy.io/usage/training)\n\nComponents\n\ntaggermorphologizertrainable\\_lemmatizerparsernerspancattextcat\n\nHardware\n\nCPUGPU (transformer)\n\nOptimize for\n\nefficiencyaccuracy\n\n```\n# This is an auto-generated partial config. To use it with 'spacy train'\n# you can run spacy init fill-config to auto-fill all default settings:\n# python -m spacy init fill-config ./base_config.cfg ./config.cfg\n[paths]\ntrain = null\ndev = null\nvectors = null\n[system]\ngpu_allocator = null\n\n[nlp]\nlang = \"en\"\npipeline = []\nbatch_size = 1000\n\n[components]\n\n[corpora]\n\n[corpora.train]\n@readers = \"spacy.Corpus.v1\"\npath = ${paths.train}\nmax_length = 0\n\n[corpora.dev]\n@readers = \"spacy.Corpus.v1\"\npath = ${paths.dev}\nmax_length = 0\n\n[training]\ndev_corpus = \"corpora.dev\"\ntrain_corpus = \"corpora.train\"\n\n[training.optimizer]\n@optimizers = \"Adam.v1\"\n\n[training.batcher]\n@batchers = \"spacy.batch_by_words.v1\"\ndiscard_oversize = false\ntolerance = 0.2\n\n[training.batcher.size]\n@schedules = \"compounding.v1\"\nstart = 100\nstop = 1000\ncompound = 1.001\n\n[initialize]\nvectors = ${paths.vectors}\n```\n\nEnd-to-end workflows from prototype to production\n-------------------------------------------------\n\nspaCy's new project system gives you a smooth path from prototype to production. It lets you keep track of all those **data transformation**, preprocessing and **training steps**, so you can make sure your project is always ready to hand over for automation. It features source asset download, command execution, checksum verification, and caching with a variety of backends and integrations.\n\n[Try it out](https://spacy.io/usage/projects)\n\nBenchmarks\n----------\n\nspaCy v3.0 introduces transformer-based pipelines that bring spaCy's accuracy right up to the current **state-of-the-art**. You can also use a CPU-optimized pipeline, which is less accurate but much cheaper to run.\n\n[More results](https://spacy.io/usage/facts-figures#benchmarks)",
  "usage": {
    "tokens": 978
  }
}
```
