---
title: Introduction - Aryn Documentation
description: Welcome to Aryn Cloud!
url: https://docs.aryn.ai/conversational-search/search-pipelines.html
timestamp: 2025-01-20T15:45:23.913Z
domain: docs.aryn.ai
path: conversational-search_search-pipelines.html
---

# Introduction - Aryn Documentation


Welcome to Aryn Cloud!


## Content

Aryn Cloud enables you to prepare complex, unstructured documents like PDFs, HTML, presentations, and more for GenAI, retrieval-augmented generation (RAG), and semantic search applications. It provides high-quality document ETL - parsing, chunking, enrichment, loading, and more - into vector databases. Aryn Cloud includes two components: DocParse and DocPrep. [Sign-up here for free](https://www.aryn.ai/get-started) to get an API Key and use the [Aryn Playground](https://play.aryn.cloud/partitioning) to check out how your document is processed and an ETL pipeline to load it into your vector database.

DocParse is a service for segmenting and labeling documents, running optical character recognition (OCR), and extracting tables and images. It can return the structured output of each document in JSON or Markdown, and provides labeled bounding boxes for titles, tables, table rows and columns, images, and regular text. DocParse can process over 30 types of document formats, including PDFs, Microsoft Word, Microsoft PowerPoint, text, and more. It leverages the Aryn Partitioner and its state-of-the-art, open source [deep learning AI model](https://huggingface.co/Aryn/deformable-detr-DocLayNet) trained on 80k+ enterprise documents. DocParse can be used in document ETL pipelines for GenAI apps or just for table extraction and document processing workflows (like in [this video](https://www.aryn.ai/?name=ArynPartitioningService_Intro)). [Learn more](https://docs.aryn.ai/quickstart)

DocPrep is a tool for creating document ETL pipelines for processing complex, unstructured data and loading it into vector databases. It uses a UI wizard to construct the pipeline, and generates Python code for you to run in a notebook, Google Colab, and other environments. The pipelines use DocParse for document partitioning, and generates code using the open source, scalable [Sycamore document ETL library](https://github.com/aryn-ai/sycamore). DocPrep supports connectors to a variety of vector databases and hybrid search indexes, including OpenSearch, ElasticSearch, Pinecone, DuckDB, Qdrant, and Weaviate.

Key Features
------------

*   **Powerful and accurate document segmentation for complex documents with tables, images, text, infographics, and more.** DocParse’s vision-based segmentation models provide 11+ class labels, and are up to 6x better in mean average precision (mAP) and 4x better in mean average recall (mAR) than other parsing solutions.
    
*   **AI-powered table extraction, OCR, image processing, and chunking.** Use DocParse’s best-in-class table extraction and optical character recognition (OCR) features to unlock data in your documents. Take the structured output of DocParse and leverage DocPrep’s chunking strategies to experiment with the best sizing of chunks for your use case.
    
*   **Scalable and reliable loading of vector DBs and search indexes.** DocPrep’s ETL pipelines can generate vector embeddings using your choice of embedding model and load a variety of target databases. These include leading engines like Elasticsearch, OpenSearch, Weaviate, Pinecone, DuckDB, Qdrant, and more. DocPrep’s ETL pipelines can scale from one to thousands of documents.
    
*   **Fully customizable document ETL in Python.** DocPrep generates document ETL pipelines in Python using the open source [Sycamore document ETL library](https://github.com/aryn-ai/sycamore). Customize your pipeline with additional data transforms, LLM-based entity extraction, data enrichment, and data cleaning.
    

Setting up
----------

[Sign-up here for free](https://www.aryn.ai/get-started) for an API Key to get started with DocParse and DocPrep.

## Metadata

```json
{
  "title": "Introduction - Aryn Documentation",
  "description": "Welcome to Aryn Cloud!",
  "url": "https://docs.aryn.ai/conversational-search/search-pipelines.html",
  "content": "Aryn Cloud enables you to prepare complex, unstructured documents like PDFs, HTML, presentations, and more for GenAI, retrieval-augmented generation (RAG), and semantic search applications. It provides high-quality document ETL - parsing, chunking, enrichment, loading, and more - into vector databases. Aryn Cloud includes two components: DocParse and DocPrep. [Sign-up here for free](https://www.aryn.ai/get-started) to get an API Key and use the [Aryn Playground](https://play.aryn.cloud/partitioning) to check out how your document is processed and an ETL pipeline to load it into your vector database.\n\nDocParse is a service for segmenting and labeling documents, running optical character recognition (OCR), and extracting tables and images. It can return the structured output of each document in JSON or Markdown, and provides labeled bounding boxes for titles, tables, table rows and columns, images, and regular text. DocParse can process over 30 types of document formats, including PDFs, Microsoft Word, Microsoft PowerPoint, text, and more. It leverages the Aryn Partitioner and its state-of-the-art, open source [deep learning AI model](https://huggingface.co/Aryn/deformable-detr-DocLayNet) trained on 80k+ enterprise documents. DocParse can be used in document ETL pipelines for GenAI apps or just for table extraction and document processing workflows (like in [this video](https://www.aryn.ai/?name=ArynPartitioningService_Intro)). [Learn more](https://docs.aryn.ai/quickstart)\n\nDocPrep is a tool for creating document ETL pipelines for processing complex, unstructured data and loading it into vector databases. It uses a UI wizard to construct the pipeline, and generates Python code for you to run in a notebook, Google Colab, and other environments. The pipelines use DocParse for document partitioning, and generates code using the open source, scalable [Sycamore document ETL library](https://github.com/aryn-ai/sycamore). DocPrep supports connectors to a variety of vector databases and hybrid search indexes, including OpenSearch, ElasticSearch, Pinecone, DuckDB, Qdrant, and Weaviate.\n\nKey Features\n------------\n\n*   **Powerful and accurate document segmentation for complex documents with tables, images, text, infographics, and more.** DocParse’s vision-based segmentation models provide 11+ class labels, and are up to 6x better in mean average precision (mAP) and 4x better in mean average recall (mAR) than other parsing solutions.\n    \n*   **AI-powered table extraction, OCR, image processing, and chunking.** Use DocParse’s best-in-class table extraction and optical character recognition (OCR) features to unlock data in your documents. Take the structured output of DocParse and leverage DocPrep’s chunking strategies to experiment with the best sizing of chunks for your use case.\n    \n*   **Scalable and reliable loading of vector DBs and search indexes.** DocPrep’s ETL pipelines can generate vector embeddings using your choice of embedding model and load a variety of target databases. These include leading engines like Elasticsearch, OpenSearch, Weaviate, Pinecone, DuckDB, Qdrant, and more. DocPrep’s ETL pipelines can scale from one to thousands of documents.\n    \n*   **Fully customizable document ETL in Python.** DocPrep generates document ETL pipelines in Python using the open source [Sycamore document ETL library](https://github.com/aryn-ai/sycamore). Customize your pipeline with additional data transforms, LLM-based entity extraction, data enrichment, and data cleaning.\n    \n\nSetting up\n----------\n\n[Sign-up here for free](https://www.aryn.ai/get-started) for an API Key to get started with DocParse and DocPrep.",
  "usage": {
    "tokens": 826
  }
}
```
