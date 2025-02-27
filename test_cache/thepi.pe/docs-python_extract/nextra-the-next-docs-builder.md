---
title: Nextra: the next docs builder
description: Nextra: the next docs builder
url: https://thepi.pe/docs-python/extract
timestamp: 2025-01-20T16:13:45.813Z
domain: thepi.pe
path: docs-python_extract
---

# Nextra: the next docs builder


Nextra: the next docs builder


## Content

Extract API
-----------

The Extract API allows you to extract structured information from various sources using Large Language Models (LLMs) or Vision Language Models (VLMs). You can extract data from URLs, local files, or text content by defining the structure of the data you want to extract using a schema.

Basic Usage[](https://thepi.pe/docs-python/extract#basic-usage)
---------------------------------------------------------------

Here's an example of extracting financial data from a PDF file:

This example would produce output similar to the following:

You can also extract data from URLs. For example, if we wanted to collect basic details about a research paper from its URL, we could set `text_only=True` to extract only the text content, set our chunking method to `chunk_by_document` to extract the entire document as a single chunk, and set `multiple_extractions=False` to get a single extraction result per chunk.

Defining the Schema[](https://thepi.pe/docs-python/extract#defining-the-schema)
-------------------------------------------------------------------------------

The schema defines the structure of the data you want to extract. It should be a dictionary where the keys are the field names and the values are the data types.

Supported data types:

*   `"string"`: For text data
*   `"int"`: For integer numbers
*   `"float"`: For decimal numbers
*   `"bool"`: For true/false values
*   `"string[]"`: For arrays of strings
*   `"string (yyyy-mm-dd)"`: For date strings in the format yyyy-mm-dd

Example schema:

Advanced Options[](https://thepi.pe/docs-python/extract#advanced-options)
-------------------------------------------------------------------------

Both `extract_from_url` and `extract_from_file` functions accept several optional parameters:

*   `ai_model`: The AI model to use for extraction (default is `'google/gemma-2-9b-it'`)
*   `multiple_extractions`: Allow multiple extractions per chunk (default is `False`)
*   `extraction_prompt`: Custom prompt for extraction (default is a predefined prompt)
*   `host_images`: Whether to host images on the server (default is `False`)
*   `text_only`: Extract only text content (default is `False`)
*   `ai_extraction`: Use AI to analyze layout before extracting structured content (default is `False`)
*   `verbose`: Print status messages (default is `False`)
*   `chunking_method`: Method to chunk the content (default is `chunk_by_page`)
*   `local`: Use local processing instead of the API (default is `False`)

Example with advanced options:

Chunking Methods[](https://thepi.pe/docs-python/extract#chunking-methods)
-------------------------------------------------------------------------

The Extract API supports various chunking methods to split the input content:

*   `chunk_by_page`: Default method, splits content by page
*   `chunk_by_document`: Combines all content into a single chunk
*   `chunk_by_section`: Splits content based on markdown headers
*   `chunk_semantic`: Uses semantic similarity to group related content
*   `chunk_by_keywords`: Splits content based on specified keywords

To use a specific chunking method, import it from `thepipe.chunker` and pass it to the `chunking_method` parameter:

Multiple vs. Single Extractions[](https://thepi.pe/docs-python/extract#multiple-vs-single-extractions)
------------------------------------------------------------------------------------------------------

The extraction results are returned as a list of dictionaries. Each dictionary represents a chunk and contains the following keys:

*   `chunk_index`: The index of the chunk from which the data was extracted
*   `source`: The source URL or file path

The structure of the extracted data depends on whether `multiple_extractions` is enabled:

1.  If `multiple_extractions` is `False`:
    
    *   The extracted fields (as defined in your schema) are directly included in each chunk's dictionary.
    
    Example:
    
2.  If `multiple_extractions` is `True`:
    
    *   Each chunk's dictionary includes an `extractions` key, which contains a list of dictionaries, each representing a separate extraction from that chunk.
    
    Example:
    

Error Handling[](https://thepi.pe/docs-python/extract#error-handling)
---------------------------------------------------------------------

If an error occurs during extraction, the result dictionary will contain an `error` key with a description of the error. It's important to check for this key when processing results:

API vs Local Processing[](https://thepi.pe/docs-python/extract#api-vs-local-processing)
---------------------------------------------------------------------------------------

The Extract API supports both API-based and local processing:

1.  API Processing (default):
    
    *   Set `local=False` (default behavior)
    *   Utilizes the thepipe API for extraction
    *   Supports streaming responses for real-time processing
    *   Handles large files and complex extractions efficiently
2.  Local Processing:
    
    *   Set `local=True`
    *   Performs extraction on the local machine
    *   Useful for offline work or when processing sensitive data
    *   May have limitations on file size and processing speed compared to the API

Example of local processing:

When using the API, the extraction process is streamed, allowing for real-time processing of results as they become available. The stream ends when an 'extraction\_complete' flag is received.

[Scrape API](https://thepi.pe/docs-python/scrape "Scrape API")[Setup](https://thepi.pe/docs-typescript/setup "Setup")

## Metadata

```json
{
  "title": "Nextra: the next docs builder",
  "description": "Nextra: the next docs builder",
  "url": "https://thepi.pe/docs-python/extract",
  "content": "Extract API\n-----------\n\nThe Extract API allows you to extract structured information from various sources using Large Language Models (LLMs) or Vision Language Models (VLMs). You can extract data from URLs, local files, or text content by defining the structure of the data you want to extract using a schema.\n\nBasic Usage[](https://thepi.pe/docs-python/extract#basic-usage)\n---------------------------------------------------------------\n\nHere's an example of extracting financial data from a PDF file:\n\nThis example would produce output similar to the following:\n\nYou can also extract data from URLs. For example, if we wanted to collect basic details about a research paper from its URL, we could set `text_only=True` to extract only the text content, set our chunking method to `chunk_by_document` to extract the entire document as a single chunk, and set `multiple_extractions=False` to get a single extraction result per chunk.\n\nDefining the Schema[](https://thepi.pe/docs-python/extract#defining-the-schema)\n-------------------------------------------------------------------------------\n\nThe schema defines the structure of the data you want to extract. It should be a dictionary where the keys are the field names and the values are the data types.\n\nSupported data types:\n\n*   `\"string\"`: For text data\n*   `\"int\"`: For integer numbers\n*   `\"float\"`: For decimal numbers\n*   `\"bool\"`: For true/false values\n*   `\"string[]\"`: For arrays of strings\n*   `\"string (yyyy-mm-dd)\"`: For date strings in the format yyyy-mm-dd\n\nExample schema:\n\nAdvanced Options[](https://thepi.pe/docs-python/extract#advanced-options)\n-------------------------------------------------------------------------\n\nBoth `extract_from_url` and `extract_from_file` functions accept several optional parameters:\n\n*   `ai_model`: The AI model to use for extraction (default is `'google/gemma-2-9b-it'`)\n*   `multiple_extractions`: Allow multiple extractions per chunk (default is `False`)\n*   `extraction_prompt`: Custom prompt for extraction (default is a predefined prompt)\n*   `host_images`: Whether to host images on the server (default is `False`)\n*   `text_only`: Extract only text content (default is `False`)\n*   `ai_extraction`: Use AI to analyze layout before extracting structured content (default is `False`)\n*   `verbose`: Print status messages (default is `False`)\n*   `chunking_method`: Method to chunk the content (default is `chunk_by_page`)\n*   `local`: Use local processing instead of the API (default is `False`)\n\nExample with advanced options:\n\nChunking Methods[](https://thepi.pe/docs-python/extract#chunking-methods)\n-------------------------------------------------------------------------\n\nThe Extract API supports various chunking methods to split the input content:\n\n*   `chunk_by_page`: Default method, splits content by page\n*   `chunk_by_document`: Combines all content into a single chunk\n*   `chunk_by_section`: Splits content based on markdown headers\n*   `chunk_semantic`: Uses semantic similarity to group related content\n*   `chunk_by_keywords`: Splits content based on specified keywords\n\nTo use a specific chunking method, import it from `thepipe.chunker` and pass it to the `chunking_method` parameter:\n\nMultiple vs. Single Extractions[](https://thepi.pe/docs-python/extract#multiple-vs-single-extractions)\n------------------------------------------------------------------------------------------------------\n\nThe extraction results are returned as a list of dictionaries. Each dictionary represents a chunk and contains the following keys:\n\n*   `chunk_index`: The index of the chunk from which the data was extracted\n*   `source`: The source URL or file path\n\nThe structure of the extracted data depends on whether `multiple_extractions` is enabled:\n\n1.  If `multiple_extractions` is `False`:\n    \n    *   The extracted fields (as defined in your schema) are directly included in each chunk's dictionary.\n    \n    Example:\n    \n2.  If `multiple_extractions` is `True`:\n    \n    *   Each chunk's dictionary includes an `extractions` key, which contains a list of dictionaries, each representing a separate extraction from that chunk.\n    \n    Example:\n    \n\nError Handling[](https://thepi.pe/docs-python/extract#error-handling)\n---------------------------------------------------------------------\n\nIf an error occurs during extraction, the result dictionary will contain an `error` key with a description of the error. It's important to check for this key when processing results:\n\nAPI vs Local Processing[](https://thepi.pe/docs-python/extract#api-vs-local-processing)\n---------------------------------------------------------------------------------------\n\nThe Extract API supports both API-based and local processing:\n\n1.  API Processing (default):\n    \n    *   Set `local=False` (default behavior)\n    *   Utilizes the thepipe API for extraction\n    *   Supports streaming responses for real-time processing\n    *   Handles large files and complex extractions efficiently\n2.  Local Processing:\n    \n    *   Set `local=True`\n    *   Performs extraction on the local machine\n    *   Useful for offline work or when processing sensitive data\n    *   May have limitations on file size and processing speed compared to the API\n\nExample of local processing:\n\nWhen using the API, the extraction process is streamed, allowing for real-time processing of results as they become available. The stream ends when an 'extraction\\_complete' flag is received.\n\n[Scrape API](https://thepi.pe/docs-python/scrape \"Scrape API\")[Setup](https://thepi.pe/docs-typescript/setup \"Setup\")",
  "usage": {
    "tokens": 1149
  }
}
```
