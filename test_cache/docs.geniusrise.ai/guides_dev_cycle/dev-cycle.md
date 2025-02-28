---
title: Dev Cycle -
description: 
url: https://docs.geniusrise.ai/guides/dev_cycle/#from-scratch
timestamp: 2025-01-20T15:45:54.796Z
domain: docs.geniusrise.ai
path: guides_dev_cycle
---

# Dev Cycle -



## Content

This document describes one full local development cycle.

Lets say we want to build a pipeline which tags medical terms in EHR documents.

Strategies[¶](https://docs.geniusrise.ai/guides/dev_cycle/#strategies "Permanent link")
---------------------------------------------------------------------------------------

Pre-requisites:

1.  SNOMED-CT: is a knowledge graph of standard medical terminology
2.  IHTSDO: a standards body for medical terminologies in a number of countries.
3.  UMLS: unified medical language system is a set of files and software that brings together many health and biomedical vocabularies and standards together.

### Strategy 1: Named entity recognition[¶](https://docs.geniusrise.ai/guides/dev_cycle/#strategy-1-named-entity-recognition "Permanent link")

#### 1\. Create a labelled dataset[¶](https://docs.geniusrise.ai/guides/dev_cycle/#1-create-a-labelled-dataset "Permanent link")

We need a corpus of documents with medical terms labeled. For example, we could use wikipedia + wikidata to build such a dataset, given entities in wikipedia are linked and indexed in the wikidata knowledge graph. Reference: [Building a Massive Corpus for Named Entity Recognition using Free Open Data Sources](https://arxiv.org/pdf/1908.05758.pdf). We could also annotate medical datasets like [MIMIC-III](https://physionet.org/content/mimiciii/1.4/) annotated with SNOMED-CT based [MedCAT](https://github.com/CogStack/MedCAT) which is a medical annotation tool developed on the knowledge graph of medical terminology (SNOMED-CT), as it would be more pertinent to our usecase, reference: [DNER Clinical (named entity recognition) from free clinical text to Snomed-CT concept](https://www.wseas.org/multimedia/journals/computers/2017/a205805-078.pdf)

#### 2\. Train a model on the NER dataset[¶](https://docs.geniusrise.ai/guides/dev_cycle/#2-train-a-model-on-the-ner-dataset "Permanent link")

We could choose a large language model and train the model on the NER fine-tuning task. The model would then be able to recognize and tag medical terms in any given text data.

### Strategy 2: Vector knowledge graph search[¶](https://docs.geniusrise.ai/guides/dev_cycle/#strategy-2-vector-knowledge-graph-search "Permanent link")

#### 1\. Create a vectorized knowledge graph[¶](https://docs.geniusrise.ai/guides/dev_cycle/#1-create-a-vectorized-knowledge-graph "Permanent link")

We use an LLM to create a vectorized layer over SNOMED-CT. This layer can be used to semantically search for "seed" nodes in the graph. We can then use these seed nodes to traverse nodes a few hops adjacent to the seed nodes.

#### 2\. Retrieval Augmented NER[¶](https://docs.geniusrise.ai/guides/dev_cycle/#2-retrieval-augmented-ner "Permanent link")

We use the knowledge graph search results to not only annotate each node seen in the EHR document, but also add additional information about those nodes derived from its adjacent nodes. But first, we also need to make sure that we query the right information instead of simply vectorized chunks and throwing it at semantic search. We would need a "traditional" pipeline for this - lemmatization followed by POS tagging. We use both proper nouns and out of vocabulary words as search query terms.

Boilerplate[¶](https://docs.geniusrise.ai/guides/dev_cycle/#boilerplate "Permanent link")
-----------------------------------------------------------------------------------------

To setup a local geniusrise project, simply use the geniusrise project creator script:

```
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-0-1)curl-Lhttps://geniusrise.new|bash# TODO: host this or create a template github repo
```

Existing project[¶](https://docs.geniusrise.ai/guides/dev_cycle/#existing-project "Permanent link")
---------------------------------------------------------------------------------------------------

If you wish to add geniusrise to an existing project:

```
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-1-1)pipinstallgeniusrise
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-1-2)pipfreeze>requirements.txt
```

From scratch[¶](https://docs.geniusrise.ai/guides/dev_cycle/#from-scratch "Permanent link")
-------------------------------------------------------------------------------------------

Here is how to set up from scratch:

```
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-1)#!/bin/bash
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-2)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-3)# Prompt for project details
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-4)read -p "Enter your project name: " project_name
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-5)read -p "Enter your name: " author_name
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-6)read -p "Enter your email: " author_email
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-7)read -p "Enter your GitHub username: " github_username
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-8)read -p "Enter a brief description of your project: " project_description
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-9)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-10)# Create project structure
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-11)mkdir $project_name
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-12)cd $project_name
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-13)mkdir $project_name tests
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-14)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-15)# Create basic files
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-16)touch README.md
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-17)touch requirements.txt
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-18)touch setup.py
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-19)touch Makefile
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-20)touch $project_name/__init__.py
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-21)touch tests/__init__.py
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-22)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-23)# Populate README.md
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-24)echo "# $project_name" > README.md
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-25)echo "\n$project_description" >> README.md
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-26)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-27)# Populate setup.py
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-28)cat <<EOL > setup.py
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-29)from setuptools import setup, find_packages
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-30)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-31)with open("README.md", "r", encoding="utf-8") as fh:
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-32)    long_description = fh.read()
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-33)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-34)setup(
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-35)    name='$project_name',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-36)    version='0.1.0',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-37)    packages=find_packages(exclude=["tests", "tests.*"]),
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-38)    install_requires=[],
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-39)    python_requires='>=3.10',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-40)    author='$author_name',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-41)    author_email='$author_email',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-42)    description='$project_description',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-43)    long_description=long_description,
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-44)    long_description_content_type='text/markdown',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-45)    url='https://github.com/$github_username/$project_name',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-46)    classifiers=[
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-47)        'Programming Language :: Python :: 3',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-48)        'License :: OSI Approved :: MIT License',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-49)        'Operating System :: OS Independent',
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-50)    ],
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-51))
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-52)EOL
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-53)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-54)# Populate Makefile
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-55)cat <<EOL > Makefile
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-56)setup:
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-57)    @pip install -r ./requirements.txt
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-58)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-59)test:
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-60)    @coverage run -m pytest -v ./tests
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-61)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-62)publish:
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-63)    @python setup.py sdist bdist_wheel
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-64)    @twine upload dist/$project_name-\$${VERSION}-* --verbose
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-65)EOL
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-66)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-67)# Set up the virtual environment and install necessary packages
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-68)virtualenv venv -p `which python3.10`
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-69)source venv/bin/activate
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-70)pip install twine setuptools pytest coverage geniusrise
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-71)pip freeze > requirements.txt
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-72)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-73)# Fetch .pre-commit-config.yaml and .gitignore from geniusrise/geniusrise
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-74)curl -O https://raw.githubusercontent.com/geniusrise/geniusrise/master/.pre-commit-config.yaml
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-75)curl -O https://raw.githubusercontent.com/geniusrise/geniusrise/master/.gitignore
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-76)
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-77)echo "Project $project_name initialized!"
```

Create a install script out of this and execute it:

```
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-3-1)touchinstall.sh
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-3-2)chmod+x./install.sh
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-3-3)./install.sh
```

Preparing the knowledge graph[¶](https://docs.geniusrise.ai/guides/dev_cycle/#preparing-the-knowledge-graph "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------

Lets prepare the knowledge graph by vectorizing each node's knowledge into a vectorized flat memory. This is a periodic activity that one needs to do whenever a new version of SNOMED-CT is released (typically bi-annually).

We use the international version of SNOMED-CT from [https://www.nlm.nih.gov/healthit/snomedct/international.html](https://www.nlm.nih.gov/healthit/snomedct/international.html).

Go to [UMLS](https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html) or [IHTSDO](https://mlds.ihtsdotools.org/) website, register, agree to the agreements and after approval, download the knowledge graph.

![Image 5: snomed](https://docs.geniusrise.ai/assets/snomed.png)

Unzip the file

```
[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-5-1)unzipSnomedCT_InternationalRF2_PRODUCTION_20230901T120000Z.zip
```

TODO 😢[¶](https://docs.geniusrise.ai/guides/dev_cycle/#todo "Permanent link")
------------------------------------------------------------------------------

Need to document https://github.com/geniusrise/geniusrise-healthcare

## Metadata

```json
{
  "title": "Dev Cycle -",
  "description": "",
  "url": "https://docs.geniusrise.ai/guides/dev_cycle/#from-scratch",
  "content": "This document describes one full local development cycle.\n\nLets say we want to build a pipeline which tags medical terms in EHR documents.\n\nStrategies[¶](https://docs.geniusrise.ai/guides/dev_cycle/#strategies \"Permanent link\")\n---------------------------------------------------------------------------------------\n\nPre-requisites:\n\n1.  SNOMED-CT: is a knowledge graph of standard medical terminology\n2.  IHTSDO: a standards body for medical terminologies in a number of countries.\n3.  UMLS: unified medical language system is a set of files and software that brings together many health and biomedical vocabularies and standards together.\n\n### Strategy 1: Named entity recognition[¶](https://docs.geniusrise.ai/guides/dev_cycle/#strategy-1-named-entity-recognition \"Permanent link\")\n\n#### 1\\. Create a labelled dataset[¶](https://docs.geniusrise.ai/guides/dev_cycle/#1-create-a-labelled-dataset \"Permanent link\")\n\nWe need a corpus of documents with medical terms labeled. For example, we could use wikipedia + wikidata to build such a dataset, given entities in wikipedia are linked and indexed in the wikidata knowledge graph. Reference: [Building a Massive Corpus for Named Entity Recognition using Free Open Data Sources](https://arxiv.org/pdf/1908.05758.pdf). We could also annotate medical datasets like [MIMIC-III](https://physionet.org/content/mimiciii/1.4/) annotated with SNOMED-CT based [MedCAT](https://github.com/CogStack/MedCAT) which is a medical annotation tool developed on the knowledge graph of medical terminology (SNOMED-CT), as it would be more pertinent to our usecase, reference: [DNER Clinical (named entity recognition) from free clinical text to Snomed-CT concept](https://www.wseas.org/multimedia/journals/computers/2017/a205805-078.pdf)\n\n#### 2\\. Train a model on the NER dataset[¶](https://docs.geniusrise.ai/guides/dev_cycle/#2-train-a-model-on-the-ner-dataset \"Permanent link\")\n\nWe could choose a large language model and train the model on the NER fine-tuning task. The model would then be able to recognize and tag medical terms in any given text data.\n\n### Strategy 2: Vector knowledge graph search[¶](https://docs.geniusrise.ai/guides/dev_cycle/#strategy-2-vector-knowledge-graph-search \"Permanent link\")\n\n#### 1\\. Create a vectorized knowledge graph[¶](https://docs.geniusrise.ai/guides/dev_cycle/#1-create-a-vectorized-knowledge-graph \"Permanent link\")\n\nWe use an LLM to create a vectorized layer over SNOMED-CT. This layer can be used to semantically search for \"seed\" nodes in the graph. We can then use these seed nodes to traverse nodes a few hops adjacent to the seed nodes.\n\n#### 2\\. Retrieval Augmented NER[¶](https://docs.geniusrise.ai/guides/dev_cycle/#2-retrieval-augmented-ner \"Permanent link\")\n\nWe use the knowledge graph search results to not only annotate each node seen in the EHR document, but also add additional information about those nodes derived from its adjacent nodes. But first, we also need to make sure that we query the right information instead of simply vectorized chunks and throwing it at semantic search. We would need a \"traditional\" pipeline for this - lemmatization followed by POS tagging. We use both proper nouns and out of vocabulary words as search query terms.\n\nBoilerplate[¶](https://docs.geniusrise.ai/guides/dev_cycle/#boilerplate \"Permanent link\")\n-----------------------------------------------------------------------------------------\n\nTo setup a local geniusrise project, simply use the geniusrise project creator script:\n\n```\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-0-1)curl-Lhttps://geniusrise.new|bash# TODO: host this or create a template github repo\n```\n\nExisting project[¶](https://docs.geniusrise.ai/guides/dev_cycle/#existing-project \"Permanent link\")\n---------------------------------------------------------------------------------------------------\n\nIf you wish to add geniusrise to an existing project:\n\n```\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-1-1)pipinstallgeniusrise\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-1-2)pipfreeze>requirements.txt\n```\n\nFrom scratch[¶](https://docs.geniusrise.ai/guides/dev_cycle/#from-scratch \"Permanent link\")\n-------------------------------------------------------------------------------------------\n\nHere is how to set up from scratch:\n\n```\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-1)#!/bin/bash\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-2)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-3)# Prompt for project details\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-4)read -p \"Enter your project name: \" project_name\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-5)read -p \"Enter your name: \" author_name\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-6)read -p \"Enter your email: \" author_email\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-7)read -p \"Enter your GitHub username: \" github_username\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-8)read -p \"Enter a brief description of your project: \" project_description\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-9)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-10)# Create project structure\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-11)mkdir $project_name\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-12)cd $project_name\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-13)mkdir $project_name tests\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-14)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-15)# Create basic files\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-16)touch README.md\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-17)touch requirements.txt\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-18)touch setup.py\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-19)touch Makefile\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-20)touch $project_name/__init__.py\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-21)touch tests/__init__.py\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-22)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-23)# Populate README.md\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-24)echo \"# $project_name\" > README.md\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-25)echo \"\\n$project_description\" >> README.md\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-26)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-27)# Populate setup.py\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-28)cat <<EOL > setup.py\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-29)from setuptools import setup, find_packages\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-30)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-31)with open(\"README.md\", \"r\", encoding=\"utf-8\") as fh:\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-32)    long_description = fh.read()\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-33)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-34)setup(\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-35)    name='$project_name',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-36)    version='0.1.0',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-37)    packages=find_packages(exclude=[\"tests\", \"tests.*\"]),\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-38)    install_requires=[],\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-39)    python_requires='>=3.10',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-40)    author='$author_name',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-41)    author_email='$author_email',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-42)    description='$project_description',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-43)    long_description=long_description,\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-44)    long_description_content_type='text/markdown',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-45)    url='https://github.com/$github_username/$project_name',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-46)    classifiers=[\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-47)        'Programming Language :: Python :: 3',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-48)        'License :: OSI Approved :: MIT License',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-49)        'Operating System :: OS Independent',\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-50)    ],\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-51))\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-52)EOL\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-53)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-54)# Populate Makefile\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-55)cat <<EOL > Makefile\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-56)setup:\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-57)    @pip install -r ./requirements.txt\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-58)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-59)test:\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-60)    @coverage run -m pytest -v ./tests\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-61)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-62)publish:\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-63)    @python setup.py sdist bdist_wheel\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-64)    @twine upload dist/$project_name-\\$${VERSION}-* --verbose\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-65)EOL\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-66)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-67)# Set up the virtual environment and install necessary packages\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-68)virtualenv venv -p `which python3.10`\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-69)source venv/bin/activate\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-70)pip install twine setuptools pytest coverage geniusrise\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-71)pip freeze > requirements.txt\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-72)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-73)# Fetch .pre-commit-config.yaml and .gitignore from geniusrise/geniusrise\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-74)curl -O https://raw.githubusercontent.com/geniusrise/geniusrise/master/.pre-commit-config.yaml\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-75)curl -O https://raw.githubusercontent.com/geniusrise/geniusrise/master/.gitignore\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-76)\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-2-77)echo \"Project $project_name initialized!\"\n```\n\nCreate a install script out of this and execute it:\n\n```\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-3-1)touchinstall.sh\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-3-2)chmod+x./install.sh\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-3-3)./install.sh\n```\n\nPreparing the knowledge graph[¶](https://docs.geniusrise.ai/guides/dev_cycle/#preparing-the-knowledge-graph \"Permanent link\")\n-----------------------------------------------------------------------------------------------------------------------------\n\nLets prepare the knowledge graph by vectorizing each node's knowledge into a vectorized flat memory. This is a periodic activity that one needs to do whenever a new version of SNOMED-CT is released (typically bi-annually).\n\nWe use the international version of SNOMED-CT from [https://www.nlm.nih.gov/healthit/snomedct/international.html](https://www.nlm.nih.gov/healthit/snomedct/international.html).\n\nGo to [UMLS](https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html) or [IHTSDO](https://mlds.ihtsdotools.org/) website, register, agree to the agreements and after approval, download the knowledge graph.\n\n![Image 5: snomed](https://docs.geniusrise.ai/assets/snomed.png)\n\nUnzip the file\n\n```\n[](https://docs.geniusrise.ai/guides/dev_cycle/#__codelineno-5-1)unzipSnomedCT_InternationalRF2_PRODUCTION_20230901T120000Z.zip\n```\n\nTODO 😢[¶](https://docs.geniusrise.ai/guides/dev_cycle/#todo \"Permanent link\")\n------------------------------------------------------------------------------\n\nNeed to document https://github.com/geniusrise/geniusrise-healthcare",
  "usage": {
    "tokens": 3872
  }
}
```
