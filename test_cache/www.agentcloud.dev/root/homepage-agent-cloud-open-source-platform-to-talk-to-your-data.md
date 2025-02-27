---
title: Homepage | Agent Cloud - Open source platform to talk to your data
description: Agent Cloud is an open source platform enabling companies to build and deploy private LLM Chat apps, that can enable teams to securely talk to their data.
url: https://www.agentcloud.dev/
timestamp: 2025-01-20T16:11:37.923Z
domain: www.agentcloud.dev
path: root
---

# Homepage | Agent Cloud - Open source platform to talk to your data


Agent Cloud is an open source platform enabling companies to build and deploy private LLM Chat apps, that can enable teams to securely talk to their data.


## Content

Data sync for Vector DBs
------------------------

Agent Cloud allows you to create data connected agents that have access to fresh up to date vector data for RAG.  
‍

![Image 38: Agent Cloud is an open-source generative AI platform with a built-in RAG as a Service that enables you to build and deploy LLM-powered conversation chat apps for talking with your data.](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65cabe1fdbaeb4b2164f3764_Hero%20home%20page%20(1).png)

Trusted by developers at:

![Image 39: Stanford University logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0cb9329791aa1749b255_stanford%201.png)![Image 40: Microsoft Logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0aae4e9b439983b7ccfb_Microsoft-Logo-White.png)![Image 41: Bumble Logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0a799867d80cb5effc6f_Bumble-3-e1602694700642.png)![Image 42: Google logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0c83453a960b1a282f3e_Transparent_google_logo_2015.png)

Great chat apps start with Good data
------------------------------------

Retrieve data from 260+ data sources
------------------------------------

Agent Cloud comes with a built in data pipeline, allowing you to split, chunk and embed data from over 260 sources out of the box.

![Image 43: Agent Cloud integration options with various service icons, including BigQuery, Hubspot, and Salesforce among others](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65b98c3d377af5b86435d142_65adf1a878ae17b8b4647695_Integrations%201.svg)

Want to build agents that access synced vector data?

Bring your own LLM or use Open AI
---------------------------------

Agent Cloud is designed to be LLM agnostic, enabling users to connect to their own open source model or leverage Open AI. To be fully private, Agent Cloud open source or self managed users can connect Agent Cloud to their own locally hosted model.

![Image 44: integration of AgentCloud with various Large Language Models (LLMs) including Mistral AI, Meta, OpenAI, ANTHROPIC, and others.](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65c5a2c501ce973d84f6ee4b_Open%20LLMs%20(1).png)

![Image 45](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65b9d7c0e79f2bd85314bdd8_How%20it%20works%20(3).svg)

The end to end RAG pipeline
---------------------------

### Select your connector

Use our [collection of data sources](https://www.agentcloud.dev/integrations) to sync data from other systems like confluence or upload your own pdf, docx, txt or csv file.  
When selecting systems like databases (postgres, snowflake, bigquery) you can select tables and even columns to ingest.

### Prep your data

For files you can provide instructions on how to split and chunk your data. Leverage Open AI latest text-embedding-3-small for embedding or select from open source models like BGE/base.

### Vector store your data

Once data has been embedded the platform will store your data within a vector database. We also expose

### Keep data fresh

Select what frequency you would like to sync data from the source. This can be manual, scheduled or a cron expression. This means users can query fresh data and know how recent the source was updated.

### Start chatting with your data!

Now that data is synced, simply create an agent with your choice of LLM and start a session to talk to your data.

Supporting major Vector DBs
---------------------------

If you're signed up to our cloud you can RAG with synced data directly by building a chat app or [using our APIs.](https://docs.agentcloud.dev/apidocs/docs/sessions/retrieve--session) If you're self hosting we connect to the major Vector DBs including Qdrant and Pinecone.

![Image 46](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/66fcb061523d2b53926a3421_Keep%20vector%20data%20in%20sync.png)

Privately chat to your data in your cloud.
------------------------------------------

Get started with Agent Cloud Community edition today or talk to us for enterprise enquiries.

![Image 47](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65bb10208049d4f4ebcf7051_Get%20started%20(1).png)

FAQs
----

Got questions? We have some answers below

What is your software license?

AGPL 3.0 - it is a copy left license which can be found here on our [github page](https://github.com/rnadigital/agentcloud?tab=AGPL-3.0-1-ov-file#readme)

What hardware requirements do I need to run Agent Cloud locally?

If running via Docker, we strongly recommend a machine with at least 16 GB of RAM.

E.g. a base Macbook Air M1/M2 with 8GB RAM will not suffice as Airbyte requires more resources.

If you are also running Olama or LM studio locally, you will need the additional RAM if you want agents to inference a local LLM model.

If you are running without docker, 8GB RAM may suffice, but it is harder to get started.

What local OS do you support?

How can I access the ELT platfrom (Airbyte) locally?

You can access the airbyte instance directly by going to http://localhost:8000 with the username **airbyte** and password **password**.

How can I access the Vector DB locally?

The vector DB is qdrant, and it is located at http://localhost:6333/dashboard#/collections. For more information about Qdrant, [see their docs here](https://qdrant.tech/documentation/).

How can I contribute to the repository?

If you want an initial idea of how your code would fit into the repo, please raise [a feature request](https://github.com/rnadigital/agentcloud/issues/new/choose). Otherwise if you're very keen, write the code and raise a pull request.  
You can also [chat on discord.](https://discord.gg/ZNSSttKqqq)

We aim to be the leading open source platform enabling companies to deploy private and secure AI apps on their infrastructure.

Can I use a local Large Language Model?

Yes. We support any local LLM which has an Open AI compatible endpoint (i.e. it responds the same way Open AI does.).  
This means you can use LM Studio or [more recently Ollama](https://ollama.com/blog/openai-compatibility?ref=agentcloud.dev) with our app for local inference.

For cloud inference we currently support Open AI.

Which Cloud models do you support?

Currently we support Open AI and Azure Open AI. We have a long term vision to support all Cloud providers by leveraging the [litellm library](https://litellm.ai/) within our Python backend. Contributors welcome!

Can I use local Embedding models?

Yes. Our app can embed locally via [fastembed.](https://github.com/qdrant/fastembed)  
You don't need to do anything to get this working, just go to the Models screen \> Fastembed \> select model.  
‍  
For cloud embedding inference we will be supporting Open AI text-ada models for now.

What splitting/chunking methods do you support?

Can I control what fields get synced when I sync a data source

Yes, you can select both the table and the fields that are being synced. This differs for Structured vs Unstrcutured data and will conform to the Airbyte stream settings for the source.

Can I control which fields get embedded and which fields get stored as metadata?

Can I control the sync frequency?

Yes, you can select basic or advanced, giving you hourly, daily or cron expression syncs. Note: for cloud this depends on your plan.

To edit go  
Data Sources \> Select Data Source \> Select Schedule Tab \[edit schedule\]

What file upload formats are supported?

For local file uploads we support:  
PDF, DOCX, TXT, CSV, XLSX

How do you price your platform?

Check out our [pricing page](https://www.agentcloud.dev/pricing) where you can see our pricing.

A single place where companies can build and deploy AI apps. This includes single agent chat apps, multi agent chat apps and knowledge retrieval apps. The platform both enables developers and engineers to build apps for themselves and the teams they interface to in sales, HR, operations etc.

How can my data retrieval be truly private.

If you want it to be truly private, don't use our managed cloud product or anyone else's for that matter. For this we recommend deploying our open source app to your infrastructure, running an LLM on prem/cloud and signing an enterprise self managed license.

[![Image 48: Agent Cloud logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65adf6a1feebb66f6debbd3d_agentcloud-full-white-bg-trans.svg)](https://www.agentcloud.dev/)

## Metadata

```json
{
  "title": "Homepage | Agent Cloud - Open source platform to talk to your data",
  "description": "Agent Cloud is an open source platform enabling companies to build and deploy private LLM Chat apps, that can enable teams to securely talk to their data.",
  "url": "https://www.agentcloud.dev/",
  "content": "Data sync for Vector DBs\n------------------------\n\nAgent Cloud allows you to create data connected agents that have access to fresh up to date vector data for RAG.  \n‍\n\n![Image 38: Agent Cloud is an open-source generative AI platform with a built-in RAG as a Service that enables you to build and deploy LLM-powered conversation chat apps for talking with your data.](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65cabe1fdbaeb4b2164f3764_Hero%20home%20page%20(1).png)\n\nTrusted by developers at:\n\n![Image 39: Stanford University logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0cb9329791aa1749b255_stanford%201.png)![Image 40: Microsoft Logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0aae4e9b439983b7ccfb_Microsoft-Logo-White.png)![Image 41: Bumble Logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0a799867d80cb5effc6f_Bumble-3-e1602694700642.png)![Image 42: Google logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65ae0c83453a960b1a282f3e_Transparent_google_logo_2015.png)\n\nGreat chat apps start with Good data\n------------------------------------\n\nRetrieve data from 260+ data sources\n------------------------------------\n\nAgent Cloud comes with a built in data pipeline, allowing you to split, chunk and embed data from over 260 sources out of the box.\n\n![Image 43: Agent Cloud integration options with various service icons, including BigQuery, Hubspot, and Salesforce among others](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65b98c3d377af5b86435d142_65adf1a878ae17b8b4647695_Integrations%201.svg)\n\nWant to build agents that access synced vector data?\n\nBring your own LLM or use Open AI\n---------------------------------\n\nAgent Cloud is designed to be LLM agnostic, enabling users to connect to their own open source model or leverage Open AI. To be fully private, Agent Cloud open source or self managed users can connect Agent Cloud to their own locally hosted model.\n\n![Image 44: integration of AgentCloud with various Large Language Models (LLMs) including Mistral AI, Meta, OpenAI, ANTHROPIC, and others.](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65c5a2c501ce973d84f6ee4b_Open%20LLMs%20(1).png)\n\n![Image 45](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65b9d7c0e79f2bd85314bdd8_How%20it%20works%20(3).svg)\n\nThe end to end RAG pipeline\n---------------------------\n\n### Select your connector\n\nUse our [collection of data sources](https://www.agentcloud.dev/integrations) to sync data from other systems like confluence or upload your own pdf, docx, txt or csv file.  \nWhen selecting systems like databases (postgres, snowflake, bigquery) you can select tables and even columns to ingest.\n\n### Prep your data\n\nFor files you can provide instructions on how to split and chunk your data. Leverage Open AI latest text-embedding-3-small for embedding or select from open source models like BGE/base.\n\n### Vector store your data\n\nOnce data has been embedded the platform will store your data within a vector database. We also expose\n\n### Keep data fresh\n\nSelect what frequency you would like to sync data from the source. This can be manual, scheduled or a cron expression. This means users can query fresh data and know how recent the source was updated.\n\n### Start chatting with your data!\n\nNow that data is synced, simply create an agent with your choice of LLM and start a session to talk to your data.\n\nSupporting major Vector DBs\n---------------------------\n\nIf you're signed up to our cloud you can RAG with synced data directly by building a chat app or [using our APIs.](https://docs.agentcloud.dev/apidocs/docs/sessions/retrieve--session) If you're self hosting we connect to the major Vector DBs including Qdrant and Pinecone.\n\n![Image 46](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/66fcb061523d2b53926a3421_Keep%20vector%20data%20in%20sync.png)\n\nPrivately chat to your data in your cloud.\n------------------------------------------\n\nGet started with Agent Cloud Community edition today or talk to us for enterprise enquiries.\n\n![Image 47](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65bb10208049d4f4ebcf7051_Get%20started%20(1).png)\n\nFAQs\n----\n\nGot questions? We have some answers below\n\nWhat is your software license?\n\nAGPL 3.0 - it is a copy left license which can be found here on our [github page](https://github.com/rnadigital/agentcloud?tab=AGPL-3.0-1-ov-file#readme)\n\nWhat hardware requirements do I need to run Agent Cloud locally?\n\nIf running via Docker, we strongly recommend a machine with at least 16 GB of RAM.\n\nE.g. a base Macbook Air M1/M2 with 8GB RAM will not suffice as Airbyte requires more resources.\n\nIf you are also running Olama or LM studio locally, you will need the additional RAM if you want agents to inference a local LLM model.\n\nIf you are running without docker, 8GB RAM may suffice, but it is harder to get started.\n\nWhat local OS do you support?\n\nHow can I access the ELT platfrom (Airbyte) locally?\n\nYou can access the airbyte instance directly by going to http://localhost:8000 with the username **airbyte** and password **password**.\n\nHow can I access the Vector DB locally?\n\nThe vector DB is qdrant, and it is located at http://localhost:6333/dashboard#/collections. For more information about Qdrant, [see their docs here](https://qdrant.tech/documentation/).\n\nHow can I contribute to the repository?\n\nIf you want an initial idea of how your code would fit into the repo, please raise [a feature request](https://github.com/rnadigital/agentcloud/issues/new/choose). Otherwise if you're very keen, write the code and raise a pull request.  \nYou can also [chat on discord.](https://discord.gg/ZNSSttKqqq)\n\nWe aim to be the leading open source platform enabling companies to deploy private and secure AI apps on their infrastructure.\n\nCan I use a local Large Language Model?\n\nYes. We support any local LLM which has an Open AI compatible endpoint (i.e. it responds the same way Open AI does.).  \nThis means you can use LM Studio or [more recently Ollama](https://ollama.com/blog/openai-compatibility?ref=agentcloud.dev) with our app for local inference.\n\nFor cloud inference we currently support Open AI.\n\nWhich Cloud models do you support?\n\nCurrently we support Open AI and Azure Open AI. We have a long term vision to support all Cloud providers by leveraging the [litellm library](https://litellm.ai/) within our Python backend. Contributors welcome!\n\nCan I use local Embedding models?\n\nYes. Our app can embed locally via [fastembed.](https://github.com/qdrant/fastembed)  \nYou don't need to do anything to get this working, just go to the Models screen \\> Fastembed \\> select model.  \n‍  \nFor cloud embedding inference we will be supporting Open AI text-ada models for now.\n\nWhat splitting/chunking methods do you support?\n\nCan I control what fields get synced when I sync a data source\n\nYes, you can select both the table and the fields that are being synced. This differs for Structured vs Unstrcutured data and will conform to the Airbyte stream settings for the source.\n\nCan I control which fields get embedded and which fields get stored as metadata?\n\nCan I control the sync frequency?\n\nYes, you can select basic or advanced, giving you hourly, daily or cron expression syncs. Note: for cloud this depends on your plan.\n\nTo edit go  \nData Sources \\> Select Data Source \\> Select Schedule Tab \\[edit schedule\\]\n\nWhat file upload formats are supported?\n\nFor local file uploads we support:  \nPDF, DOCX, TXT, CSV, XLSX\n\nHow do you price your platform?\n\nCheck out our [pricing page](https://www.agentcloud.dev/pricing) where you can see our pricing.\n\nA single place where companies can build and deploy AI apps. This includes single agent chat apps, multi agent chat apps and knowledge retrieval apps. The platform both enables developers and engineers to build apps for themselves and the teams they interface to in sales, HR, operations etc.\n\nHow can my data retrieval be truly private.\n\nIf you want it to be truly private, don't use our managed cloud product or anyone else's for that matter. For this we recommend deploying our open source app to your infrastructure, running an LLM on prem/cloud and signing an enterprise self managed license.\n\n[![Image 48: Agent Cloud logo](https://cdn.prod.website-files.com/65adf1a878ae17b8b46475f5/65adf6a1feebb66f6debbd3d_agentcloud-full-white-bg-trans.svg)](https://www.agentcloud.dev/)",
  "usage": {
    "tokens": 2146
  }
}
```
