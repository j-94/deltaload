---
title: lnx
description: 
url: https://lnx.rs/
timestamp: 2025-01-20T16:00:12.493Z
domain: lnx.rs
path: root
---

# lnx



## Content

![Image 7](https://lnx.rs/logo.png)

Lightning-fast,

Feature-rich search.

### An adaptable search engine API.

Make it

\>

lightning fast. relevant. typo tolerant. search as you type. your way.

An open-source, lightning-fast and typo tolerant search engine empowering developers and users alike.

![Image 8](https://lnx.rs/love.svg)

Community Driven

100% open-source, built for the community.

![Image 9](https://lnx.rs/lightning.svg)

Insanely Fast

Query millions of documents in milliseconds with our fast-fuzzy system.

Typo Tolerant

lnx provides fuzzy query systems to give you a typo-tolerant query.

Multi-Language

Currently lnx supports 17 latin languages. Chinese, Japanese and Korean are planned.

### Quick start with docker

Get started in seconds with our [docker images](https://hub.docker.com/r/chillfish8/lnx) , just run:

docker run -p "8000:8000" chillfish8/lnx:latest --host "0.0.0.0"

Once setup you can create indexes and start exploring everything  
lnx has to offer with [the docs.](https://docs.lnx.rs/)

### The query kinds

### The "normal" query

This mode exposes the [Tantivy query parser](https://docs.rs/tantivy/0.16.0/tantivy/query/struct.QueryParser.html) which gives you a powerful query language for searching things like logs.

### The "fuzzy" query

This mode uses the traditional [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to find close matches giving you typo-tolerance with your queries.

### The "more-like-this" query

Get similar documents to a reference document, great for e-commerce or e-readers.

### The "fast-fuzzy" query

The fast-fuzzy mode is a implementation of the [symspell algorithm](https://towardsdatascience.com/symspellcompound-10ec8f467c9b) which provides spell corrections via pre-computation. This is the secret sauce behind being able to blow other engines out of the water when it comes to fuzzy searching.

Sorting By Field

Results can be sorted by any fast-field quickly and easily.

Stop Words

With a pre-made set, stop words can be removed to boost relevancy in queries.

Token Bearer Authorization

Secure your system giving permissions based access to specific users.

Boost Fields

Each fields can be individually adjusted to give the best searching experience.

Fast-Fuzzy Pre-Computation

This feature uses pre-computation to boost fuzzy query performance by over 10x.

## Metadata

```json
{
  "title": "lnx",
  "description": "",
  "url": "https://lnx.rs/",
  "content": "![Image 7](https://lnx.rs/logo.png)\n\nLightning-fast,\n\nFeature-rich search.\n\n### An adaptable search engine API.\n\nMake it\n\n\\>\n\nlightning fast. relevant. typo tolerant. search as you type. your way.\n\nAn open-source, lightning-fast and typo tolerant search engine empowering developers and users alike.\n\n![Image 8](https://lnx.rs/love.svg)\n\nCommunity Driven\n\n100% open-source, built for the community.\n\n![Image 9](https://lnx.rs/lightning.svg)\n\nInsanely Fast\n\nQuery millions of documents in milliseconds with our fast-fuzzy system.\n\nTypo Tolerant\n\nlnx provides fuzzy query systems to give you a typo-tolerant query.\n\nMulti-Language\n\nCurrently lnx supports 17 latin languages. Chinese, Japanese and Korean are planned.\n\n### Quick start with docker\n\nGet started in seconds with our [docker images](https://hub.docker.com/r/chillfish8/lnx) , just run:\n\ndocker run -p \"8000:8000\" chillfish8/lnx:latest --host \"0.0.0.0\"\n\nOnce setup you can create indexes and start exploring everything  \nlnx has to offer with [the docs.](https://docs.lnx.rs/)\n\n### The query kinds\n\n### The \"normal\" query\n\nThis mode exposes the [Tantivy query parser](https://docs.rs/tantivy/0.16.0/tantivy/query/struct.QueryParser.html) which gives you a powerful query language for searching things like logs.\n\n### The \"fuzzy\" query\n\nThis mode uses the traditional [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to find close matches giving you typo-tolerance with your queries.\n\n### The \"more-like-this\" query\n\nGet similar documents to a reference document, great for e-commerce or e-readers.\n\n### The \"fast-fuzzy\" query\n\nThe fast-fuzzy mode is a implementation of the [symspell algorithm](https://towardsdatascience.com/symspellcompound-10ec8f467c9b) which provides spell corrections via pre-computation. This is the secret sauce behind being able to blow other engines out of the water when it comes to fuzzy searching.\n\nSorting By Field\n\nResults can be sorted by any fast-field quickly and easily.\n\nStop Words\n\nWith a pre-made set, stop words can be removed to boost relevancy in queries.\n\nToken Bearer Authorization\n\nSecure your system giving permissions based access to specific users.\n\nBoost Fields\n\nEach fields can be individually adjusted to give the best searching experience.\n\nFast-Fuzzy Pre-Computation\n\nThis feature uses pre-computation to boost fuzzy query performance by over 10x.",
  "usage": {
    "tokens": 567
  }
}
```
