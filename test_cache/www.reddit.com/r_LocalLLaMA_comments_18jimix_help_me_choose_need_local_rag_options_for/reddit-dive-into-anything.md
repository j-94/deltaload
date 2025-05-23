---
title: Reddit - Dive into anything
description: 
url: https://www.reddit.com/r/LocalLLaMA/comments/18jimix/help_me_choose_need_local_rag_options_for/
timestamp: 2025-01-20T15:54:10.294Z
domain: www.reddit.com
path: r_LocalLLaMA_comments_18jimix_help_me_choose_need_local_rag_options_for
---

# Reddit - Dive into anything



## Content

As post title implies, I'm a bit confused and need some guidance. I've tried some but not yet all of the apps listed in the title.

Looking to get a feel (via comments) for the "State of the Union" of LLM end-to-end apps with local RAG.

What I want to do:

1.  Multi-format: I have folders of PDFs, epubs, and text-file transcripts (from YT vids and podcasts) and want to chat with this body of knowledge.
    
2.  Embedding Customization: I'd like to try various methods of creating embeddings. EG, chunking, sentence transformers, embedding models. Ideally app has a GUI to change these options.
    
3.  More than 1 vector store? Option to create/select from multiple vectorstores. Say I also want to chat with, uh, some recipes. I don't want my other docs and my recipes in one store. I want to load up the recipes embeddings when I want that, and then close it and open a different set of embeddings when I want. Seems neater? Please don't make me mix my data.
    
4.  All local. My data stays on my system. But of course the option to add OpenAI API keys, should I want to process embeddings with OpenAI or chat with my docs and GPT4.
    
5.  GPU: Allow me to use GPU when possible. I have 2x4090s and want to use them - many apps seem to be limited to GGUF and CPU, and trying to make them work with GPU after the fact, has been difficult.
    
6.  Free? At least partly. Doesn't require a paid, web-based vectorDB (same point as above, stay local, but thought I had to spell this out).
    
7.  GUI. Ideally has a GUI for EVERYTHING, including options and settings and in-app model switching. EG some apps you need to exit, adjust a yaml manually, then restart _just to switch models_. Come on, it's 2023. Why do we need to shut down and manually type the model into a yaml?
    

My impressions/tests so far:

**\- Oobabooga**  
with Superboogav2: Seems very lacking in functionality and configuration for local RAG/Chat with Docs. Lacks options.

**\- privateGPT**  
You can't have more than 1 vectorstore. No way to remove a book or doc from the vectorstore once added. Can't change embedding settings. Difficult to use GPU (I can't make it work, so it's slow AF). To change chat models you have to edit a yaml then relaunch. Not sure why people can't add that into the GUI... a lot of cons, not many pros.

**\- localGPT**  
Looks like you have to make embeddings via CLI? WHY GOD WHY. And as with privateGPT, looks like changing models is a manual text edit/relaunch process. Similar to privateGPT, looks like it goes part way to local RAG/Chat with docs, but stops short of having options and settings (one-size-fits-all, but does it really?)  
Con: You can change embedding method but have to go edit code to do this, which is Clunky AF. Why can't this stuff be exposed in a GUI?  
Con: Docs to ingest have to be placed in a specific folder then run commands via CLI. Why not a GUI where I can drag files from various locations on my HDD? And then how do I remove a specific set of embeddings from the vector DB?

**\- LMStudio**  
You can browse, download, and switch models in a really nice GUI, but there's no "chat with my docs" function, that I can see, let alone configurable options for embeddings, chunking, etc. Limited to GGUF, so... slow?

**\- OLlama**  
Mac only? I'm on PC and want to use the 4090s.

**\- LangChain**  
Just don't even. This thing is a dumpster fire. And remember, the whole post is more about complete apps and end-to-end solutions, ie, "where is the Auto1111 for LLM+RAG?" (hint it's NOT PrivateGPT or LocalGPT or Ooba that's for sure).

**\- MemGPT**  
? Still need to look into this.

**\- AutoGPT**  
Looks interesting but AFAIK can't change embedding settings?

**\- GPT4All**  
? Still need to look into this.

**\- ChatDocs**  
Supposed to be a fork of privateGPT but it has very low stars on Github compared to privateGPT, so I'm not sure how viable this is or how active.BUT it seems to come already working with GPU and GPTQ models,AND you can change embedding settings (via a file, not GUI sadly).

**\- Taskweaver**  
Did the rounds on Youtube hype vids last week but still need to look into this more.

**Is there anything else significant that I am missing?**

Not looking at OpenAi "GPTs" because while you can upload docs, you can't change or select embedding settings, chunking, etc there either. Which makes it seem like OpenAI is going for RAG-For-Dummies (no offence to anyone, I am emphasizing their ease-of-use resulting in lack-of-options). BUT at least I could make one GPT for work chat, one for recipes chat, one for hobbies chat. Where is this in local tools (ability to select from multiple vector stores and instructions? Is it in Autogen?).

Thanks

## Metadata

```json
{
  "title": "Reddit - Dive into anything",
  "description": "",
  "url": "https://www.reddit.com/r/LocalLLaMA/comments/18jimix/help_me_choose_need_local_rag_options_for/",
  "content": "As post title implies, I'm a bit confused and need some guidance. I've tried some but not yet all of the apps listed in the title.\n\nLooking to get a feel (via comments) for the \"State of the Union\" of LLM end-to-end apps with local RAG.\n\nWhat I want to do:\n\n1.  Multi-format: I have folders of PDFs, epubs, and text-file transcripts (from YT vids and podcasts) and want to chat with this body of knowledge.\n    \n2.  Embedding Customization: I'd like to try various methods of creating embeddings. EG, chunking, sentence transformers, embedding models. Ideally app has a GUI to change these options.\n    \n3.  More than 1 vector store? Option to create/select from multiple vectorstores. Say I also want to chat with, uh, some recipes. I don't want my other docs and my recipes in one store. I want to load up the recipes embeddings when I want that, and then close it and open a different set of embeddings when I want. Seems neater? Please don't make me mix my data.\n    \n4.  All local. My data stays on my system. But of course the option to add OpenAI API keys, should I want to process embeddings with OpenAI or chat with my docs and GPT4.\n    \n5.  GPU: Allow me to use GPU when possible. I have 2x4090s and want to use them - many apps seem to be limited to GGUF and CPU, and trying to make them work with GPU after the fact, has been difficult.\n    \n6.  Free? At least partly. Doesn't require a paid, web-based vectorDB (same point as above, stay local, but thought I had to spell this out).\n    \n7.  GUI. Ideally has a GUI for EVERYTHING, including options and settings and in-app model switching. EG some apps you need to exit, adjust a yaml manually, then restart _just to switch models_. Come on, it's 2023. Why do we need to shut down and manually type the model into a yaml?\n    \n\nMy impressions/tests so far:\n\n**\\- Oobabooga**  \nwith Superboogav2: Seems very lacking in functionality and configuration for local RAG/Chat with Docs. Lacks options.\n\n**\\- privateGPT**  \nYou can't have more than 1 vectorstore. No way to remove a book or doc from the vectorstore once added. Can't change embedding settings. Difficult to use GPU (I can't make it work, so it's slow AF). To change chat models you have to edit a yaml then relaunch. Not sure why people can't add that into the GUI... a lot of cons, not many pros.\n\n**\\- localGPT**  \nLooks like you have to make embeddings via CLI? WHY GOD WHY. And as with privateGPT, looks like changing models is a manual text edit/relaunch process. Similar to privateGPT, looks like it goes part way to local RAG/Chat with docs, but stops short of having options and settings (one-size-fits-all, but does it really?)  \nCon: You can change embedding method but have to go edit code to do this, which is Clunky AF. Why can't this stuff be exposed in a GUI?  \nCon: Docs to ingest have to be placed in a specific folder then run commands via CLI. Why not a GUI where I can drag files from various locations on my HDD? And then how do I remove a specific set of embeddings from the vector DB?\n\n**\\- LMStudio**  \nYou can browse, download, and switch models in a really nice GUI, but there's no \"chat with my docs\" function, that I can see, let alone configurable options for embeddings, chunking, etc. Limited to GGUF, so... slow?\n\n**\\- OLlama**  \nMac only? I'm on PC and want to use the 4090s.\n\n**\\- LangChain**  \nJust don't even. This thing is a dumpster fire. And remember, the whole post is more about complete apps and end-to-end solutions, ie, \"where is the Auto1111 for LLM+RAG?\" (hint it's NOT PrivateGPT or LocalGPT or Ooba that's for sure).\n\n**\\- MemGPT**  \n? Still need to look into this.\n\n**\\- AutoGPT**  \nLooks interesting but AFAIK can't change embedding settings?\n\n**\\- GPT4All**  \n? Still need to look into this.\n\n**\\- ChatDocs**  \nSupposed to be a fork of privateGPT but it has very low stars on Github compared to privateGPT, so I'm not sure how viable this is or how active.BUT it seems to come already working with GPU and GPTQ models,AND you can change embedding settings (via a file, not GUI sadly).\n\n**\\- Taskweaver**  \nDid the rounds on Youtube hype vids last week but still need to look into this more.\n\n**Is there anything else significant that I am missing?**\n\nNot looking at OpenAi \"GPTs\" because while you can upload docs, you can't change or select embedding settings, chunking, etc there either. Which makes it seem like OpenAI is going for RAG-For-Dummies (no offence to anyone, I am emphasizing their ease-of-use resulting in lack-of-options). BUT at least I could make one GPT for work chat, one for recipes chat, one for hobbies chat. Where is this in local tools (ability to select from multiple vector stores and instructions? Is it in Autogen?).\n\nThanks",
  "usage": {
    "tokens": 1175
  }
}
```
