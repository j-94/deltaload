---
title: langchain_text_splitters 0.2.4 — 🦜🔗 LangChain 0.2.17
description: 
url: https://api.python.langchain.com/en/latest/text_splitters_api_reference.html
timestamp: 2025-01-20T16:01:11.775Z
domain: api.python.langchain.com
path: en_latest_text_splitters_api_reference.html
---

# langchain_text_splitters 0.2.4 — 🦜🔗 LangChain 0.2.17



## Content

This is a legacy site. Please use the latest v0.2 and v0.3 API references instead.

LangChain
Core
Community
Experimental
Text splitters
Partner libs
Docs
 
Toggle Menu
langchain_text_splitters 0.2.4
langchain_text_splitters.base
langchain_text_splitters.character
langchain_text_splitters.html
langchain_text_splitters.json
langchain_text_splitters.konlpy
langchain_text_splitters.latex
langchain_text_splitters.markdown
langchain_text_splitters.nltk
langchain_text_splitters.python
langchain_text_splitters.sentence_transformers
langchain_text_splitters.spacy
langchain_text_splitters 0.2.4
langchain_text_splitters.base
Classes

base.Language(value)

	

Enum of the programming languages.




base.TextSplitter(chunk_size, chunk_overlap, ...)

	

Interface for splitting text into chunks.




base.TokenTextSplitter([encoding_name, ...])

	

Splitting text to tokens using model tokenizer.




base.Tokenizer(chunk_overlap, ...)

	

Tokenizer data class.

Functions

base.split_text_on_tokens(*, text, tokenizer)

	

Split incoming text and return chunks using tokenizer.

langchain_text_splitters.character
Classes

character.CharacterTextSplitter([separator, ...])

	

Splitting text that looks at characters.




character.RecursiveCharacterTextSplitter([...])

	

Splitting text by recursively look at characters.

langchain_text_splitters.html
Classes

html.ElementType

	

Element type as typed dict.




html.HTMLHeaderTextSplitter(headers_to_split_on)

	

Splitting HTML files based on specified headers.




html.HTMLSectionSplitter(headers_to_split_on)

	

Splitting HTML files based on specified tag and font sizes.

langchain_text_splitters.json
Classes

json.RecursiveJsonSplitter([max_chunk_size, ...])

	

langchain_text_splitters.konlpy
Classes

konlpy.KonlpyTextSplitter([separator])

	

Splitting text using Konlpy package.

langchain_text_splitters.latex
Classes

latex.LatexTextSplitter(**kwargs)

	

Attempts to split the text along Latex-formatted layout elements.

langchain_text_splitters.markdown
Classes

markdown.ExperimentalMarkdownSyntaxTextSplitter([...])

	

An experimental text splitter for handling Markdown syntax.




markdown.HeaderType

	

Header type as typed dict.




markdown.LineType

	

Line type as typed dict.




markdown.MarkdownHeaderTextSplitter(...[, ...])

	

Splitting markdown files based on specified headers.




markdown.MarkdownTextSplitter(**kwargs)

	

Attempts to split the text along Markdown-formatted headings.

langchain_text_splitters.nltk
Classes

nltk.NLTKTextSplitter([separator, language])

	

Splitting text using NLTK package.

langchain_text_splitters.python
Classes

python.PythonCodeTextSplitter(**kwargs)

	

Attempts to split the text along Python syntax.

langchain_text_splitters.sentence_transformers
Classes

sentence_transformers.SentenceTransformersTokenTextSplitter([...])

	

Splitting text to tokens using sentence model tokenizer.

langchain_text_splitters.spacy
Classes

spacy.SpacyTextSplitter([separator, ...])

	

Splitting text using Spacy package.

© 2023, LangChain, Inc. . Last updated on Dec 09, 2024.

## Metadata

```json
{
  "title": "langchain_text_splitters 0.2.4 — 🦜🔗 LangChain 0.2.17",
  "description": "",
  "url": "https://api.python.langchain.com/en/latest/text_splitters_api_reference.html",
  "content": "This is a legacy site. Please use the latest v0.2 and v0.3 API references instead.\n\nLangChain\nCore\nCommunity\nExperimental\nText splitters\nPartner libs\nDocs\n \nToggle Menu\nlangchain_text_splitters 0.2.4\nlangchain_text_splitters.base\nlangchain_text_splitters.character\nlangchain_text_splitters.html\nlangchain_text_splitters.json\nlangchain_text_splitters.konlpy\nlangchain_text_splitters.latex\nlangchain_text_splitters.markdown\nlangchain_text_splitters.nltk\nlangchain_text_splitters.python\nlangchain_text_splitters.sentence_transformers\nlangchain_text_splitters.spacy\nlangchain_text_splitters 0.2.4\nlangchain_text_splitters.base\nClasses\n\nbase.Language(value)\n\n\t\n\nEnum of the programming languages.\n\n\n\n\nbase.TextSplitter(chunk_size, chunk_overlap, ...)\n\n\t\n\nInterface for splitting text into chunks.\n\n\n\n\nbase.TokenTextSplitter([encoding_name, ...])\n\n\t\n\nSplitting text to tokens using model tokenizer.\n\n\n\n\nbase.Tokenizer(chunk_overlap, ...)\n\n\t\n\nTokenizer data class.\n\nFunctions\n\nbase.split_text_on_tokens(*, text, tokenizer)\n\n\t\n\nSplit incoming text and return chunks using tokenizer.\n\nlangchain_text_splitters.character\nClasses\n\ncharacter.CharacterTextSplitter([separator, ...])\n\n\t\n\nSplitting text that looks at characters.\n\n\n\n\ncharacter.RecursiveCharacterTextSplitter([...])\n\n\t\n\nSplitting text by recursively look at characters.\n\nlangchain_text_splitters.html\nClasses\n\nhtml.ElementType\n\n\t\n\nElement type as typed dict.\n\n\n\n\nhtml.HTMLHeaderTextSplitter(headers_to_split_on)\n\n\t\n\nSplitting HTML files based on specified headers.\n\n\n\n\nhtml.HTMLSectionSplitter(headers_to_split_on)\n\n\t\n\nSplitting HTML files based on specified tag and font sizes.\n\nlangchain_text_splitters.json\nClasses\n\njson.RecursiveJsonSplitter([max_chunk_size, ...])\n\n\t\n\nlangchain_text_splitters.konlpy\nClasses\n\nkonlpy.KonlpyTextSplitter([separator])\n\n\t\n\nSplitting text using Konlpy package.\n\nlangchain_text_splitters.latex\nClasses\n\nlatex.LatexTextSplitter(**kwargs)\n\n\t\n\nAttempts to split the text along Latex-formatted layout elements.\n\nlangchain_text_splitters.markdown\nClasses\n\nmarkdown.ExperimentalMarkdownSyntaxTextSplitter([...])\n\n\t\n\nAn experimental text splitter for handling Markdown syntax.\n\n\n\n\nmarkdown.HeaderType\n\n\t\n\nHeader type as typed dict.\n\n\n\n\nmarkdown.LineType\n\n\t\n\nLine type as typed dict.\n\n\n\n\nmarkdown.MarkdownHeaderTextSplitter(...[, ...])\n\n\t\n\nSplitting markdown files based on specified headers.\n\n\n\n\nmarkdown.MarkdownTextSplitter(**kwargs)\n\n\t\n\nAttempts to split the text along Markdown-formatted headings.\n\nlangchain_text_splitters.nltk\nClasses\n\nnltk.NLTKTextSplitter([separator, language])\n\n\t\n\nSplitting text using NLTK package.\n\nlangchain_text_splitters.python\nClasses\n\npython.PythonCodeTextSplitter(**kwargs)\n\n\t\n\nAttempts to split the text along Python syntax.\n\nlangchain_text_splitters.sentence_transformers\nClasses\n\nsentence_transformers.SentenceTransformersTokenTextSplitter([...])\n\n\t\n\nSplitting text to tokens using sentence model tokenizer.\n\nlangchain_text_splitters.spacy\nClasses\n\nspacy.SpacyTextSplitter([separator, ...])\n\n\t\n\nSplitting text using Spacy package.\n\n© 2023, LangChain, Inc. . Last updated on Dec 09, 2024.",
  "usage": {
    "tokens": 729
  }
}
```
