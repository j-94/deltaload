---
title: An Introduction to LlamaIndex Query Pipelines
description: 
url: https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html#
timestamp: 2025-01-20T15:57:25.098Z
domain: docs.llamaindex.ai
path: en_latest_examples_pipeline_query_pipeline.html
---

# An Introduction to LlamaIndex Query Pipelines



## Content

An Introduction to LlamaIndex Query Pipelines - LlamaIndex
=============== 

 

[Skip to content](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#an-introduction-to-llamaindex-query-pipelines)

[![Image 4: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")

LlamaIndex

An Introduction to LlamaIndex Query Pipelines

  

Search

*   [Home](https://docs.llamaindex.ai/en/stable/)
*   [Learn](https://docs.llamaindex.ai/en/stable/understanding/)
*   [Use Cases](https://docs.llamaindex.ai/en/stable/use_cases/)
*   [Examples](https://docs.llamaindex.ai/en/stable/examples/)
*   [Component Guides](https://docs.llamaindex.ai/en/stable/module_guides/)
*   [Advanced Topics](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)
*   [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/)
*   [Open-Source Community](https://docs.llamaindex.ai/en/stable/community/integrations/)
*   [LlamaCloud](https://docs.llamaindex.ai/en/stable/llama_cloud/)

 [![Image 5: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")LlamaIndex

*   [ ] 
    
    [Home](https://docs.llamaindex.ai/en/stable/)
    
    Home
    
    *   [High-Level Concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)
    *   [Installation and Setup](https://docs.llamaindex.ai/en/stable/getting_started/installation/)
    *   [How to read these docs](https://docs.llamaindex.ai/en/stable/getting_started/reading/)
    *   [ ]  Starter Examples
        
        Starter Examples
        
        *   [Starter Tutorial (OpenAI)](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/)
        *   [Starter Tutorial (Local Models)](https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/)
        
    *   [Discover LlamaIndex Video Series](https://docs.llamaindex.ai/en/stable/getting_started/discover_llamaindex/)
    *   [Frequently Asked Questions (FAQ)](https://docs.llamaindex.ai/en/stable/getting_started/customization/)
    *   [ ] 
        
        [Starter Tools](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/)
        
        Starter Tools
        
        *   [RAG CLI](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/)
        
    
*   [ ] 
    
    [Learn](https://docs.llamaindex.ai/en/stable/understanding/)
    
    Learn
    
    *   [Using LLMs](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/)
    *   [ ] 
        
        [Building a RAG pipeline](https://docs.llamaindex.ai/en/stable/understanding/rag/)
        
        Building a RAG pipeline
        
        *   [ ]  Loading & Ingestion
            
            Loading & Ingestion
            
            *   [Loading Data (Ingestion)](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/)
            *   [LlamaHub](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/)
            *   [Loading from LlamaCloud](https://docs.llamaindex.ai/en/stable/understanding/loading/llamacloud/)
            
        *   [Indexing & Embedding](https://docs.llamaindex.ai/en/stable/understanding/indexing/indexing/)
        *   [Storing](https://docs.llamaindex.ai/en/stable/understanding/storing/storing/)
        *   [Querying](https://docs.llamaindex.ai/en/stable/understanding/querying/querying/)
        
    *   [ ] 
        
        [Building an agent](https://docs.llamaindex.ai/en/stable/understanding/agent/)
        
        Building an agent
        
        *   [Agents with local models](https://docs.llamaindex.ai/en/stable/understanding/agent/local_models/)
        *   [Adding RAG to an agent](https://docs.llamaindex.ai/en/stable/understanding/agent/rag_agent/)
        *   [Enhancing with LlamaParse](https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/)
        *   [Memory](https://docs.llamaindex.ai/en/stable/understanding/agent/memory/)
        *   [Adding other tools](https://docs.llamaindex.ai/en/stable/understanding/agent/tools/)
        
    *   [ ] 
        
        [Building Workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/)
        
        Building Workflows
        
        *   [A basic workflow](https://docs.llamaindex.ai/en/stable/understanding/workflows/basic_flow/)
        *   [Branches and loops](https://docs.llamaindex.ai/en/stable/understanding/workflows/branches_and_loops/)
        *   [Maintaining state](https://docs.llamaindex.ai/en/stable/understanding/workflows/state/)
        *   [Streaming events](https://docs.llamaindex.ai/en/stable/understanding/workflows/stream/)
        *   [Concurrent execution](https://docs.llamaindex.ai/en/stable/understanding/workflows/concurrent_execution/)
        *   [Subclassing workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/subclass/)
        *   [Nested workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/nested/)
        *   [Observability](https://docs.llamaindex.ai/en/stable/understanding/workflows/observability/)
        *   [Unbound syntax](https://docs.llamaindex.ai/en/stable/understanding/workflows/unbound_functions/)
        
    *   [ ] 
        
        [Structured Data Extraction](https://docs.llamaindex.ai/en/stable/understanding/extraction/)
        
        Structured Data Extraction
        
        *   [Using Structured LLMs](https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_llms/)
        *   [Structured Prediction](https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_prediction/)
        *   [Lower-level extraction](https://docs.llamaindex.ai/en/stable/understanding/extraction/lower_level/)
        
    *   [Tracing and Debugging](https://docs.llamaindex.ai/en/stable/understanding/tracing_and_debugging/tracing_and_debugging/)
    *   [ ]  Evaluating
        
        Evaluating
        
        *   [Evaluating](https://docs.llamaindex.ai/en/stable/understanding/evaluating/evaluating/)
        *   [ ] 
            
            [Cost Analysis](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/)
            
            Cost Analysis
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/)
            
        
    *   [ ] 
        
        [Putting it all Together](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/)
        
        Putting it all Together
        
        *   [ ] 
            
            [Full-stack web application](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/)
            
            Full-stack web application
            
            *   [A Guide to Building a Full-Stack Web App with LLamaIndex](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/fullstack_app_guide/)
            *   [A Guide to Building a Full-Stack LlamaIndex Web App with Delphic](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/fullstack_with_delphic/)
            
        *   [ ] 
            
            [Q&A Patterns](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/)
            
            Q&A Patterns
            
            *   [A Guide to Extracting Terms and Definitions](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/terms_definitions_tutorial/)
            
        *   [ ]  Chatbots
            
            Chatbots
            
            *   [How to Build a Chatbot](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/chatbots/building_a_chatbot/)
            
        *   [ ] 
            
            [Structured data](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/structured_data/)
            
            Structured data
            
        *   [Agents](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/)
        
    
*   [ ] 
    
    [Use Cases](https://docs.llamaindex.ai/en/stable/use_cases/)
    
    Use Cases
    
    *   [Prompting](https://docs.llamaindex.ai/en/stable/use_cases/prompting/)
    *   [Question-Answering (RAG)](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/)
    *   [Chatbots](https://docs.llamaindex.ai/en/stable/use_cases/chatbots/)
    *   [Structured Data Extraction](https://docs.llamaindex.ai/en/stable/use_cases/extraction/)
    *   [Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/)
    *   [Multi-Modal Applications](https://docs.llamaindex.ai/en/stable/use_cases/multimodal/)
    *   [Fine-Tuning](https://docs.llamaindex.ai/en/stable/use_cases/fine_tuning/)
    
*   [ ] 
    
    [Examples](https://docs.llamaindex.ai/en/stable/examples/)
    
    Examples
    
    *   [ ]  Agents
        
        Agents
        
        *   [💬🤖 How to Build a Chatbot](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/)
        *   [GPT Builder Demo](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/)
        *   [Building a Multi-PDF Agent using Query Pipelines and HyDE](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/)
        *   [Step-wise, Controllable Agents](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/)
        *   [Controllable Agents for RAG](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner_rag_controllable/)
        *   [Building an Agent around a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/query_pipeline_agent/)
        *   [Agentic rag using vertex ai](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/)
        *   [Agentic rag with llamaindex and vertexai managed index](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/)
        *   [Function Calling Anthropic Agent](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/)
        *   [Function Calling AWS Bedrock Converse Agent](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/)
        *   [Chain-of-Abstraction LlamaPack](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/)
        *   [Building a Custom Agent](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/)
        *   [DashScope Agent Tutorial](https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/)
        *   [Introspective Agents: Performing Tasks With Reflection](https://docs.llamaindex.ai/en/stable/examples/agent/introspective_agent_toxicity_reduction/)
        *   [Language Agent Tree Search](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/)
        *   [LLM Compiler Agent Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/)
        *   [Simple Composable Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/)
        *   [Vector Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/vector_memory/)
        *   [Function Calling Mistral Agent](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/)
        *   [Multi-Document Agents (V1)](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/)
        *   [Multi-Document Agents](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/)
        *   [Function Calling NVIDIA Agent](https://docs.llamaindex.ai/en/stable/examples/agent/nvidia_agent/)
        *   [Document Research Assistant for Blog Creation](https://docs.llamaindex.ai/en/stable/examples/agent/nvidia_document_research_assistant_for_blog_creation/)
        *   [Sub Question Query Engine powered by NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/agent/nvidia_sub_question_query_engine/)
        *   [Build your own OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)
        *   [Context-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/)
        *   [OpenAI Agent Workarounds for Lengthy Tool Descriptions](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_lengthy_tools/)
        *   [Single-Turn Multi-Function Calling OpenAI Agents](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/)
        *   [OpenAI Agent + Query Engine Experimental Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/)
        *   [OpenAI Agent Query Planning](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/)
        *   [Retrieval-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/)
        *   [OpenAI Agent with Tool Call Parser](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/)
        *   [OpenAI Agent with Query Engine Tools](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/)
        *   [OpenAI Assistant Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/)
        *   [OpenAI Assistant Advanced Retrieval Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/)
        *   [OpenAI agent: specifying a forced function call](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/)
        *   [Benchmarking OpenAI Retrieval API (through Assistant Agent)](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/)
        *   [ReAct Agent - A Simple Intro with Calculator Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/)
        *   [ReAct Agent with Query Engine (RAG) Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/)
        *   [Controlling Agent Reasoning Loop with Return Direct Tools](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/)
        *   [Structured Planning Agent](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/)
        
    *   [ ]  Chat Engines
        
        Chat Engines
        
        *   [Chat Engine - Best Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_best/)
        *   [Chat Engine - Condense Plus Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/)
        *   [Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/)
        *   [Chat Engine - Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_context/)
        *   [Chat Engine - OpenAI Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_openai/)
        *   [Chat Engine with a Personality ✨](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/)
        *   [Chat Engine - ReAct Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_react/)
        *   [Chat Engine - Simple Mode REPL](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_repl/)
        
    *   [ ]  Cookbooks
        
        Cookbooks
        
        *   [GraphRAG Implementation with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/cookbooks/GraphRAG_v1/)
        *   [GraphRAG Implementation with LlamaIndex - V2](https://docs.llamaindex.ai/en/stable/examples/cookbooks/GraphRAG_v2/)
        *   [AirtrainAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/airtrain/)
        *   [Anthropic Haiku Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/anthropic_haiku/)
        *   [Trustworthy RAG with the Trustworthy Language Model](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cleanlab_tlm_rag/)
        *   [Codestral from MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/)
        *   [Cohere init8 and binary Embeddings Retrieval Evaluation](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/)
        *   [Contextual Retrieval](https://docs.llamaindex.ai/en/stable/examples/cookbooks/contextual_retrieval/)
        *   [CrewAI + LlamaIndex Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/crewai_llamaindex/)
        *   [Llama3 Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook/)
        *   [LLM Cookbook with Intel Gaudi](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_gaudi/)
        *   [Llama3 Cookbook with Groq](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_groq/)
        *   [Llama3 Cookbook with Ollama and Replicate](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_ollama_replicate/)
        *   [MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/)
        *   [mixedbread Rerank Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/)
        *   [Optimizing for relevance using MongoDB and LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mongodb_retrieval_strategies/)
        *   [Oracle AI Vector Search with Document Processing](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oracleai_demo/)
        *   [Components Of LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-2/Components_Of_LlamaIndex/)
        *   [Evaluating RAG Systems](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-3/Evaluating_RAG_Systems/)
        *   [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-4/Ingestion_Pipeline/)
        *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-4/Metadata_Extraction/)
        *   [Observability](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-5/Observability/)
        *   [Agents](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-6/Agents/)
        *   [Router QueryEngine and SubQuestion QueryEngine](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-6/Router_And_SubQuestion_QueryEngine/)
        *   [Multi-Modal RAG System](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-7/Multi_Modal_RAG_System/)
        *   [Advanced RAG with LlamaParse](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-8/Advanced_RAG_with_LlamaParse/)
        *   [Prometheus-2 Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/prometheus2_cookbook/)
        *   [Sales Prospecting Workflow with Toolhouse](https://docs.llamaindex.ai/en/stable/examples/cookbooks/toolhouse_llamaindex/)
        
    *   [ ]  Customization
        
        Customization
        
        *   [Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/customization/llms/AzureOpenAI/)
        *   [ChatGPT](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/)
        *   [HuggingFace LLM - Camel-5b](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/)
        *   [HuggingFace LLM - StableLM](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/)
        *   [Chat Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/)
        *   [Completion Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)
        *   [Streaming](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/)
        *   [Streaming for Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/chat_engine_condense_question_stream_response/)
        
    *   [ ]  Data Connectors
        
        Data Connectors
        
        *   [Chroma Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ChromaDemo/)
        *   [DashVector Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DashvectorReaderDemo/)
        *   [Database Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DatabaseReaderDemo/)
        *   [DeepLake Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DeepLakeReader/)
        *   [Discord Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DiscordDemo/)
        *   [Docling Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DoclingReaderDemo/)
        *   [Faiss Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/FaissDemo/)
        *   [Github Repo Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GithubRepositoryReaderDemo/)
        *   [Google Chat Reader Test](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleChatDemo/)
        *   [Google Docs Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleDocsDemo/)
        *   [Google Drive Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleDriveDemo/)
        *   [Google Maps Text Search Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleMapsTextSearchReaderDemo/)
        *   [Google Sheets Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleSheetsDemo/)
        *   [Make Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MakeDemo/)
        *   [Mbox Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MboxReaderDemo/)
        *   [MilvusReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MilvusReaderDemo/)
        *   [MongoDB Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MongoDemo/)
        *   [MyScale Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MyScaleReaderDemo/)
        *   [Notion Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/NotionDemo/)
        *   [Obsidian Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ObsidianReaderDemo/)
        *   [Pathway Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/)
        *   [Preprocess](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PreprocessReaderDemo/)
        *   [Psychic Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PsychicDemo/)
        *   [Qdrant Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/QdrantDemo/)
        *   [Slack Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/SlackDemo/)
        *   [Twitter Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/TwitterDemo/)
        *   [Weaviate Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/)
        *   [Web Page Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/)
        *   [Zyte Serp Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ZyteSerpDemo/)
        *   [Deplot Reader Demo](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/)
        *   [HTML Tag Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/html_tag_reader/)
        *   [Oracle AI Vector Search: Document Processing](https://docs.llamaindex.ai/en/stable/examples/data_connectors/oracleai/)
        *   [Simple Directory Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/)
        *   [Parallel Processing SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_parallel/)
        *   [Simple Directory Reader over a Remote FileSystem](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_remote_fs/)
        
    *   [ ]  Discover LlamaIndex
        
        Discover LlamaIndex
        
        *   [Discord Thread Management](https://docs.llamaindex.ai/en/stable/examples/discover_llamaindex/document_management/Discord_Thread_Management/)
        
    *   [ ]  Docstores
        
        Docstores
        
        *   [Demo: Azure Table Storage as a Docstore](https://docs.llamaindex.ai/en/stable/examples/docstore/AzureDocstoreDemo/)
        *   [Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/)
        *   [Dynamo DB Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/)
        *   [Firestore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/FirestoreDemo/)
        *   [MongoDB Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/MongoDocstoreDemo/)
        *   [Redis Docstore+Index Store Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/)
        *   [Tablestore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/TablestoreDocstoreDemo/)
        
    *   [ ]  Embeddings
        
        Embeddings
        
        *   [Anyscale Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Anyscale/)
        *   [LangChain Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain/)
        *   [OpenAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/)
        *   [Aleph Alpha Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/alephalpha/)
        *   [Bedrock Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/bedrock/)
        *   [Embeddings with Clarifai](https://docs.llamaindex.ai/en/stable/examples/embeddings/clarifai/)
        *   [Cloudflare Workers AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/cloudflare_workersai/)
        *   [CohereAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/cohereai/)
        *   [Custom Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/)
        *   [Dashscope embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/dashscope_embeddings/)
        *   [Databricks Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/databricks/)
        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/examples/embeddings/deepinfra/)
        *   [Elasticsearch Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/elasticsearch/)
        *   [Qdrant FastEmbed Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/fastembed/)
        *   [Fireworks Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/fireworks/)
        *   [Google Gemini Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/gemini/)
        *   [Gigachat](https://docs.llamaindex.ai/en/stable/examples/embeddings/gigachat/)
        *   [Google PaLM Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/google_palm/)
        *   [Local Embeddings with HuggingFace](https://docs.llamaindex.ai/en/stable/examples/embeddings/huggingface/)
        *   [IBM watsonx.ai](https://docs.llamaindex.ai/en/stable/examples/embeddings/ibm_watsonx/)
        *   [Local Embeddings with IPEX-LLM on Intel CPU](https://docs.llamaindex.ai/en/stable/examples/embeddings/ipex_llm/)
        *   [Local Embeddings with IPEX-LLM on Intel GPU](https://docs.llamaindex.ai/en/stable/examples/embeddings/ipex_llm_gpu/)
        *   [Jina 8K Context Window Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/)
        *   [Jina Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/)
        *   [Llamafile Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llamafile/)
        *   [LLMRails Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llm_rails/)
        *   [MistralAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/mistralai/)
        *   [Mixedbread AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/mixedbreadai/)
        *   [ModelScope Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/modelscope/)
        *   [Nebius Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/nebius/)
        *   [Nomic Embedding](https://docs.llamaindex.ai/en/stable/examples/embeddings/nomic/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/embeddings/nvidia/)
        *   [Oracle Cloud Infrastructure Generative AI](https://docs.llamaindex.ai/en/stable/examples/embeddings/oci_genai/)
        *   [Ollama Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/ollama_embedding/)
        *   [Local Embeddings with OpenVINO](https://docs.llamaindex.ai/en/stable/examples/embeddings/openvino/)
        *   [Optimized Embedding Model using Optimum-Intel](https://docs.llamaindex.ai/en/stable/examples/embeddings/optimum_intel/)
        *   [Oracle AI Vector Search: Generate Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/oracleai/)
        *   [PremAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/premai/)
        *   [Interacting with Embeddings deployed in Amazon SageMaker Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/embeddings/sagemaker_embedding_endpoint/)
        *   [Text Embedding Inference](https://docs.llamaindex.ai/en/stable/examples/embeddings/text_embedding_inference/)
        *   [TextEmbed - Embedding Inference Server](https://docs.llamaindex.ai/en/stable/examples/embeddings/textembed/)
        *   [Together AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/together/)
        *   [Upstage Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/upstage/)
        *   [Interacting with Embeddings deployed in Vertex AI Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/embeddings/vertex_embedding_endpoint/)
        *   [VoyageAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/voyageai/)
        *   [Yandexgpt](https://docs.llamaindex.ai/en/stable/examples/embeddings/yandexgpt/)
        
    *   [ ]  Evaluation
        
        Evaluation
        
        *   [BEIR Out of Domain Benchmark](https://docs.llamaindex.ai/en/stable/examples/evaluation/BeirEvaluation/)
        *   [🚀 RAG/LLM Evaluators - DeepEval](https://docs.llamaindex.ai/en/stable/examples/evaluation/Deepeval/)
        *   [HotpotQADistractor Demo](https://docs.llamaindex.ai/en/stable/examples/evaluation/HotpotQADistractor/)
        *   [QuestionGeneration](https://docs.llamaindex.ai/en/stable/examples/evaluation/QuestionGeneration/)
        *   [RAGChecker: A Fine-grained Evaluation Framework For Diagnosing RAG](https://docs.llamaindex.ai/en/stable/examples/evaluation/RAGChecker/)
        *   [Self Correcting Query Engines - Evaluation & Retry](https://docs.llamaindex.ai/en/stable/examples/evaluation/RetryQuery/)
        *   [Tonic Validate Evaluators](https://docs.llamaindex.ai/en/stable/examples/evaluation/TonicValidateEvaluators/)
        *   [How to use UpTrain with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/evaluation/UpTrain/)
        *   [Answer Relevancy and Context Relevancy Evaluations](https://docs.llamaindex.ai/en/stable/examples/evaluation/answer_and_context_relevancy/)
        *   [BatchEvalRunner - Running Multiple Evaluations](https://docs.llamaindex.ai/en/stable/examples/evaluation/batch_eval/)
        *   [Correctness Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/correctness_eval/)
        *   [Faithfulness Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/faithfulness_eval/)
        *   [Guideline Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/guideline_eval/)
        *   [Benchmarking LLM Evaluators On The MT-Bench Human Judgement](https://docs.llamaindex.ai/en/stable/examples/evaluation/mt_bench_human_judgement/)
        *   [Benchmarking LLM Evaluators On A Mini MT-Bench (Single Grading)](https://docs.llamaindex.ai/en/stable/examples/evaluation/mt_bench_single_grading/)
        *   [Evaluating Multi-Modal RAG](https://docs.llamaindex.ai/en/stable/examples/evaluation/multi_modal/multi_modal_rag_evaluation/)
        *   [Pairwise Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/pairwise_eval/)
        *   [Evaluation using Prometheus model](https://docs.llamaindex.ai/en/stable/examples/evaluation/prometheus_evaluation/)
        *   [Relevancy Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/relevancy_eval/)
        *   [Retrieval Evaluation](https://docs.llamaindex.ai/en/stable/examples/evaluation/retrieval/retriever_eval/)
        *   [Embedding Similarity Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/semantic_similarity_eval/)
        *   [🏔️ Step-back prompting with workflows for RAG with Argilla](https://docs.llamaindex.ai/en/stable/examples/evaluation/step_back_argilla/)
        
    *   [ ]  Finetuning
        
        Finetuning
        
        *   [How to Finetune a cross-encoder using LLamaIndex](https://docs.llamaindex.ai/en/stable/examples/finetuning/cross_encoder_finetuning/cross_encoder_finetuning/)
        *   [Finetuning corpus embeddings using NUDGE](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_corpus_embedding/)
        *   [Finetune Embeddings](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding/)
        *   [Finetuning an Adapter on Top of any Black-Box Embedding Model](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding_adapter/)
        *   [Knowledge Distillation For Fine-Tuning A GPT-3.5 Judge (Correctness)](https://docs.llamaindex.ai/en/stable/examples/finetuning/llm_judge/correctness/finetune_llm_judge_single_grading_correctness/)
        *   [Knowledge Distillation For Fine-Tuning A GPT-3.5 Judge (Pairwise)](https://docs.llamaindex.ai/en/stable/examples/finetuning/llm_judge/pairwise/finetune_llm_judge/)
        *   [Fine Tuning MistralAI models using Finetuning API](https://docs.llamaindex.ai/en/stable/examples/finetuning/mistralai_fine_tuning/)
        *   [Fine Tuning GPT-3.5-Turbo](https://docs.llamaindex.ai/en/stable/examples/finetuning/openai_fine_tuning/)
        *   [Fine Tuning with Function Calling](https://docs.llamaindex.ai/en/stable/examples/finetuning/openai_fine_tuning_functions/)
        *   [Fine-tuning a gpt-3.5 ReAct Agent on Better Chain of Thought](https://docs.llamaindex.ai/en/stable/examples/finetuning/react_agent/react_agent_finetune/)
        *   [Custom Cohere Reranker](https://docs.llamaindex.ai/en/stable/examples/finetuning/rerankers/cohere_custom_reranker/)
        *   [Router Fine-tuning](https://docs.llamaindex.ai/en/stable/examples/finetuning/router/router_finetune/)
        
    *   [ ]  Ingestion
        
        Ingestion
        
        *   [Advanced Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/advanced_ingestion_pipeline/)
        *   [Async Ingestion Pipeline + Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/ingestion/async_ingestion_pipeline/)
        *   [Ingestion Pipeline + Document Management](https://docs.llamaindex.ai/en/stable/examples/ingestion/document_management_pipeline/)
        *   [Building a Live RAG Pipeline over Google Drive Files](https://docs.llamaindex.ai/en/stable/examples/ingestion/ingestion_gdrive/)
        *   [Parallelizing Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/parallel_execution_ingestion_pipeline/)
        *   [Redis Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/redis_ingestion_pipeline/)
        
    *   [ ]  LLMs
        
        LLMs
        
        *   [AI21](https://docs.llamaindex.ai/en/stable/examples/llm/ai21/)
        *   [Aleph Alpha](https://docs.llamaindex.ai/en/stable/examples/llm/alephalpha/)
        *   [Anthropic](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/)
        *   [Anthropic Prompt Caching](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic_prompt_caching/)
        *   [Anyscale](https://docs.llamaindex.ai/en/stable/examples/llm/anyscale/)
        *   [Azure AI model inference](https://docs.llamaindex.ai/en/stable/examples/llm/azure_inference/)
        *   [Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/azure_openai/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/examples/llm/bedrock/)
        *   [Bedrock Converse](https://docs.llamaindex.ai/en/stable/examples/llm/bedrock_converse/)
        *   [Cerebras](https://docs.llamaindex.ai/en/stable/examples/llm/cerebras/)
        *   [Clarifai LLM](https://docs.llamaindex.ai/en/stable/examples/llm/clarifai/)
        *   [Cleanlab Trustworthy Language Model](https://docs.llamaindex.ai/en/stable/examples/llm/cleanlab/)
        *   [Cohere](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/)
        *   [DashScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/dashscope/)
        *   [DataBricks](https://docs.llamaindex.ai/en/stable/examples/llm/databricks/)
        *   [DeepInfra](https://docs.llamaindex.ai/en/stable/examples/llm/deepinfra/)
        *   [EverlyAI](https://docs.llamaindex.ai/en/stable/examples/llm/everlyai/)
        *   [Fireworks](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks/)
        *   [Fireworks Function Calling Cookbook](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks_cookbook/)
        *   [Friendli](https://docs.llamaindex.ai/en/stable/examples/llm/friendli/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/examples/llm/gemini/)
        *   [Groq](https://docs.llamaindex.ai/en/stable/examples/llm/groq/)
        *   [Hugging Face LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/huggingface/)
        *   [IBM watsonx.ai](https://docs.llamaindex.ai/en/stable/examples/llm/ibm_watsonx/)
        *   [IPEX-LLM on Intel CPU](https://docs.llamaindex.ai/en/stable/examples/llm/ipex_llm/)
        *   [IPEX-LLM on Intel GPU](https://docs.llamaindex.ai/en/stable/examples/llm/ipex_llm_gpu/)
        *   [Konko](https://docs.llamaindex.ai/en/stable/examples/llm/konko/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/examples/llm/langchain/)
        *   [LiteLLM](https://docs.llamaindex.ai/en/stable/examples/llm/litellm/)
        *   [Replicate - Llama 2 13B](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2/)
        *   [LlamaCPP](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/)
        *   [🦙 x 🦙 Rap Battle](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_rap_battle/)
        *   [Llama API](https://docs.llamaindex.ai/en/stable/examples/llm/llama_api/)
        *   [llamafile](https://docs.llamaindex.ai/en/stable/examples/llm/llamafile/)
        *   [LLM Predictor](https://docs.llamaindex.ai/en/stable/examples/llm/llm_predictor/)
        *   [LM Studio](https://docs.llamaindex.ai/en/stable/examples/llm/lmstudio/)
        *   [LocalAI](https://docs.llamaindex.ai/en/stable/examples/llm/localai/)
        *   [Maritalk](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/)
        *   [MistralRS LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mistral_rs/)
        *   [MistralAI](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/)
        *   [ModelScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/modelscope/)
        *   [Monster API <\> LLamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/monsterapi/)
        *   [MyMagic AI LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mymagic/)
        *   [Nebius LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/nebius/)
        *   [Neutrino AI](https://docs.llamaindex.ai/en/stable/examples/llm/neutrino/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_nim/)
        *   [Nvidia TensorRT-LLM](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_tensorrt/)
        *   [NVIDIA's LLM Text Completion API](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_text_completion/)
        *   [Nvidia Triton](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_triton/)
        *   [Oracle Cloud Infrastructure Generative AI](https://docs.llamaindex.ai/en/stable/examples/llm/oci_genai/)
        *   [OctoAI](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/)
        *   [Ollama - Llama 3.1](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/)
        *   [Ollama - Gemma](https://docs.llamaindex.ai/en/stable/examples/llm/ollama_gemma/)
        *   [OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/openai/)
        *   [OpenAI JSON Mode vs. Function Calling for Data Extraction](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/)
        *   [OpenLLM](https://docs.llamaindex.ai/en/stable/examples/llm/openllm/)
        *   [OpenRouter](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/)
        *   [OpenVINO LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/openvino/)
        *   [Optimum Intel LLMs optimized with IPEX backend](https://docs.llamaindex.ai/en/stable/examples/llm/optimum_intel/)
        *   [AlibabaCloud-PaiEas](https://docs.llamaindex.ai/en/stable/examples/llm/paieas/)
        *   [PaLM](https://docs.llamaindex.ai/en/stable/examples/llm/palm/)
        *   [Perplexity](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/)
        *   [Pipeshift](https://docs.llamaindex.ai/en/stable/examples/llm/pipeshift/)
        *   [Portkey](https://docs.llamaindex.ai/en/stable/examples/llm/portkey/)
        *   [Predibase](https://docs.llamaindex.ai/en/stable/examples/llm/predibase/)
        *   [PremAI LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/premai/)
        *   [Client of Baidu Intelligent Cloud's Qianfan LLM Platform](https://docs.llamaindex.ai/en/stable/examples/llm/qianfan/)
        *   [RunGPT](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/)
        *   [Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/)
        *   [SambaNova Systems](https://docs.llamaindex.ai/en/stable/examples/llm/sambanovasystems/)
        *   [Together AI LLM](https://docs.llamaindex.ai/en/stable/examples/llm/together/)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/examples/llm/upstage/)
        *   [Vertex AI](https://docs.llamaindex.ai/en/stable/examples/llm/vertex/)
        *   [Replicate - Vicuna 13B](https://docs.llamaindex.ai/en/stable/examples/llm/vicuna/)
        *   [vLLM](https://docs.llamaindex.ai/en/stable/examples/llm/vllm/)
        *   [Xorbits Inference](https://docs.llamaindex.ai/en/stable/examples/llm/xinference_local_deployment/)
        *   [Yi](https://docs.llamaindex.ai/en/stable/examples/llm/yi/)
        
    *   [ ]  Llama Datasets
        
        Llama Datasets
        
        *   [Downloading a LlamaDataset from LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/downloading_llama_datasets/)
        *   [Benchmarking RAG Pipelines With A](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/labelled-rag-datasets/)
        *   [Submission Template Notebook](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/ragdataset_submission_template/)
        *   [Contributing a LlamaDataset To LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/)
        
    *   [ ]  Llama Hub
        
        Llama Hub
        
        *   [LlamaHub Demostration](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/)
        *   [Ollama Llama Pack Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_ollama/)
        *   [Llama Pack - Resume Screener 📄](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_resume/)
        *   [Llama Packs Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/)
        
    *   [ ]  Low Level
        
        Low Level
        
        *   [Building Evaluation from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/)
        *   [Building an Advanced Fusion Retriever from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/)
        *   [Building Data Ingestion from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/)
        *   [Building RAG from Scratch (Open-source only!)](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval/)
        *   [Building Response Synthesis from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/)
        *   [Building Retrieval from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/)
        *   [Building a Router from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/router/)
        *   [Building a (Very Simple) Vector Store from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/vector_store/)
        
    *   [ ]  Managed Indexes
        
        Managed Indexes
        
        *   [BGEM3Demo](https://docs.llamaindex.ai/en/stable/examples/managed/BGEM3Demo/)
        *   [Google Generative Language Semantic Retriever](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/)
        *   [PostgresML Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/)
        *   [Google Cloud LlamaIndex on Vertex AI for RAG](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/)
        *   [Semantic Retriever Benchmark](https://docs.llamaindex.ai/en/stable/examples/managed/manage_retrieval_benchmark/)
        *   [Vectara Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/)
        *   [Managed Index with Zilliz Cloud Pipelines](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/)
        
    *   [ ]  Memory
        
        Memory
        
        *   [Mem0](https://docs.llamaindex.ai/en/stable/examples/memory/Mem0Memory/)
        
    *   [ ]  Metadata Extractors
        
        Metadata Extractors
        
        *   [Entity Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/EntityExtractionClimate/)
        *   [Metadata Extraction and Augmentation w/ Marvin](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/)
        *   [Extracting Metadata for Better Document Indexing and Understanding](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/)
        *   [Automated Metadata Extraction for Better Retrieval + Synthesis](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtraction_LLMSurvey/)
        *   [Pydantic Extractor](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/)
        
    *   [ ]  Multi-Modal
        
        Multi-Modal
        
        *   [Chroma Multi-Modal Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/)
        *   [Multi-Modal LLM using Anthropic model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/)
        *   [Multi-Modal LLM using Azure OpenAI GPT-4o mini for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/)
        *   [Multi-Modal Retrieval using Cohere Multi-Modal Embeddings](https://docs.llamaindex.ai/en/stable/examples/multi_modal/cohere_multi_modal/)
        *   [Multi-Modal LLM using DashScope qwen-vl model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/dashscope_multi_modal/)
        *   [Multi-Modal LLM using Google's Gemini model for image understanding and build Retrieval Augmented Generation with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/)
        *   [Multimodal Structured Outputs: GPT-4o vs. Other GPT-4 Variants](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/)
        *   [GPT4-V Experiments with General, Specific questions and Chain Of Thought (COT) Prompting Technique.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_experiments_cot/)
        *   [Advanced Multi-Modal Retrieval using GPT4V and Multi-Modal Index/Retriever](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_multi_modal_retrieval/)
        *   [Image to Image Retrieval using CLIP embedding and image correlation reasoning using GPT4V](https://docs.llamaindex.ai/en/stable/examples/multi_modal/image_to_image_retrieval/)
        *   [LlaVa Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/)
        *   [Retrieval-Augmented Image Captioning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_multi_modal_tesla_10q/)
        *   [Multi-Modal LLM using Mistral for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/mistral_multi_modal/)
        *   [\[Beta\] Multi-modal ReAct Agent](https://docs.llamaindex.ai/en/stable/examples/multi_modal/mm_agent/)
        *   [Multi-Modal GPT4V Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/)
        *   [Multi-Modal RAG using Nomic Embed and Anthropic.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/)
        *   [Multi-Modal Retrieval using GPT text embedding and CLIP image embedding for Wikipedia Articles](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_retrieval/)
        *   [Multimodal RAG for processing videos using OpenAI GPT4V and LanceDB vectorstore](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/)
        *   [Multimodal RAG with VideoDB](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_videorag_videodb/)
        *   [Multimodal rag guardrail gemini llmguard llmguard](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multimodal_rag_guardrail_gemini_llmguard_llmguard/)
        *   [Multimodal models with Nebius](https://docs.llamaindex.ai/en/stable/examples/multi_modal/nebius_multi_modal/)
        *   [Multi-Modal LLM using NVIDIA endpoints for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/nvidia_multi_modal/)
        *   [Multimodal Ollama Cookbook](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/)
        *   [Using OpenAI GPT-4V model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/)
        *   [Local Multimodal pipeline with OpenVINO](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openvino_multimodal/)
        *   [Multi-Modal LLM using Replicate LlaVa, Fuyu 8B, MiniGPT4 models for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)
        *   [Semi-structured Image Retrieval](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/)
        
    *   [ ]  Multi-Tenancy
        
        Multi-Tenancy
        
        *   [Multi-Tenancy RAG with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/)
        
    *   [ ]  Node Parsers & Text Splitters
        
        Node Parsers & Text Splitters
        
        *   [Semantic Chunker](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_chunking/)
        *   [Semantic double merging chunking](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_double_merging_chunking/)
        *   [TopicNodeParser](https://docs.llamaindex.ai/en/stable/examples/node_parsers/topic_parser/)
        
    *   [ ]  Node Postprocessors
        
        Node Postprocessors
        
        *   [Cohere Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/)
        *   [Reranking using ColPali, Cohere Reranker and Multi-Modal Embeddings](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColPaliRerank/)
        *   [Colbert Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColbertRerank/)
        *   [File Based Node Parsers](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FileNodeProcessors/)
        *   [FlagEmbeddingReranker](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FlagEmbeddingReranker/)
        *   [Jina Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/JinaRerank/)
        *   [LLM Reranker Demonstration (Great Gatsby)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Gatsby/)
        *   [LLM Reranker Demonstration (2021 Lyft 10-k)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Lyft-10k/)
        *   [LongContextReorder](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder/)
        *   [Metadata Replacement + Node Sentence Window](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/)
        *   [Mixedbread AI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MixedbreadAIRerank/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/)
        *   [Sentence Embedding Optimizer](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo/)
        *   [PII Masking](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/)
        *   [Forward/Backward Augmentation](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PrevNextPostprocessorDemo/)
        *   [Recency Filtering](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/)
        *   [SentenceTransformerRerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/SentenceTransformerRerank/)
        *   [Time-Weighted Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/)
        *   [VoyageAI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/)
        *   [OpenVINO Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/)
        *   [RankGPT Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankGPT/)
        *   [RankLLM Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankLLM/)
        
    *   [ ]  Object Stores
        
        Object Stores
        
        *   [The Class](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/)
        
    *   [ ]  Observability
        
        Observability
        
        *   [Aim Callback](https://docs.llamaindex.ai/en/stable/examples/observability/AimCallback/)
        *   [HoneyHive LlamaIndex Tracer](https://docs.llamaindex.ai/en/stable/examples/observability/HoneyHiveLlamaIndexTracer/)
        *   [Langfuse Callback Handler](https://docs.llamaindex.ai/en/stable/examples/observability/LangfuseCallbackHandler/)
        *   [Analyze and Debug LlamaIndex Applications with PostHog and Langfuse](https://docs.llamaindex.ai/en/stable/examples/observability/LangfuseMistralPostHog/)
        *   [Llama Debug Handler](https://docs.llamaindex.ai/en/stable/examples/observability/LlamaDebugHandler/)
        *   [MLflow](https://docs.llamaindex.ai/en/stable/examples/observability/MLflow/)
        *   [OpenInference Callback Handler + Arize Phoenix](https://docs.llamaindex.ai/en/stable/examples/observability/OpenInferenceCallback/)
        *   [Observability with OpenLLMetry](https://docs.llamaindex.ai/en/stable/examples/observability/OpenLLMetry/)
        *   [Logging traces with Opik](https://docs.llamaindex.ai/en/stable/examples/observability/OpikCallback/)
        *   [PromptLayer Handler](https://docs.llamaindex.ai/en/stable/examples/observability/PromptLayerHandler/)
        *   [Token Counting Handler](https://docs.llamaindex.ai/en/stable/examples/observability/TokenCountingHandler/)
        *   [UpTrain Callback Handler](https://docs.llamaindex.ai/en/stable/examples/observability/UpTrainCallback/)
        *   [Wandb Callback Handler](https://docs.llamaindex.ai/en/stable/examples/observability/WandbCallbackHandler/)
        
    *   [ ]  Output Parsers
        
        Output Parsers
        
        *   [Guardrails Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/)
        *   [Langchain Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/)
        *   [DataFrame Structured Data Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)
        *   [Evaporate Demo](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/)
        *   [Function Calling Program for Structured Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/)
        *   [Guidance Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_pydantic_program/)
        *   [Guidance for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/)
        *   [LLM Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/)
        *   [LM Format Enforcer Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_pydantic_program/)
        *   [LM Format Enforcer Regular Expression Generation](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_regular_expressions/)
        *   [LLM Pydantic Program - NVIDIA](https://docs.llamaindex.ai/en/stable/examples/output_parsing/nvidia_output_parsing/)
        *   [OpenAI Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/)
        *   [OpenAI function calling for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_sub_question/)
        
    *   [ ]  Param Optimizer
        
        Param Optimizer
        
        *   [\[WIP\] Hyperparameter Optimization for RAG](https://docs.llamaindex.ai/en/stable/examples/param_optimizer/param_optimizer/)
        
    *   [ ]  Prompts
        
        Prompts
        
        *   [Advanced Prompt Techniques (Variable Mappings, Functions)](https://docs.llamaindex.ai/en/stable/examples/prompts/advanced_prompts/)
        *   [EmotionPrompt in RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/)
        *   [Accessing/Customizing Prompts within Higher-Level Modules](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_mixin/)
        *   ["Optimization by Prompting" for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/)
        *   [Prompt Engineering for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/)
        
    *   [ ]  Property Graph
        
        Property Graph
        
        *   [Using a Property Graph Store](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/)
        *   [Property Graph Construction with Predefined Schemas](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/)
        *   [Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/)
        *   [Defining a Custom Property Graph Retriever](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/)
        *   [Memgraph Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_memgraph/)
        *   [Neo4j Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/)
        
    *   [ ]  Query Engines
        
        Query Engines
        
        *   [Retriever Query Engine with Custom Retrievers - Simple Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/)
        *   [JSONalyze Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JSONalyze_query_engine/)
        *   [Joint QA Summary Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JointQASummary/)
        *   [Retriever Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RetrieverRouterQueryEngine/)
        *   [Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/)
        *   [SQL Auto Vector Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/)
        *   [SQL Join Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/)
        *   [SQL Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/)
        *   [CitationQueryEngine](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/)
        *   [Cogniswitch query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/)
        *   [Defining a Custom Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/)
        *   [Ensemble Query Engine Guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/)
        *   [FLARE Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine/)
        *   [JSON Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/json_query_engine/)
        *   [Knowledge Graph Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/)
        *   [Knowledge Graph RAG Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine/)
        *   [Structured Hierarchical Retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/multi_doc_auto_retrieval/multi_doc_auto_retrieval/)
        *   [Pandas Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/)
        *   [Recursive Retriever + Query Engine Demo](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/)
        *   [\[Beta\] Text-to-SQL with PGVector](https://docs.llamaindex.ai/en/stable/examples/query_engine/pgvector_sql_query_engine/)
        *   [Query Engine with Pydantic Outputs](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/)
        *   [Recursive Retriever + Document Agents](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/)
        *   [Joint Tabular/Semantic QA over Tesla 10K](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table/)
        *   [Sub Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)
        
    *   [ ]  Query Pipeline
        
        Query Pipeline
        
        *   [ ]  An Introduction to LlamaIndex Query Pipelines [An Introduction to LlamaIndex Query Pipelines](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/)
            
            Table of contents
            
            *   [Overview](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#overview)
            *   [Cookbook](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#cookbook)
            *   [Setup](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#setup)
            *   [1\. Chain Together Prompt and LLM](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-chain-together-prompt-and-llm)
                
                *   [View Intermediate Inputs/Outputs](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#view-intermediate-inputsoutputs)
                *   [Try Output Parsing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#try-output-parsing)
                *   [Streaming Support](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#streaming-support)
                
            *   [Chain Together Query Rewriting Workflow (prompts + LLM) with Retrieval](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#chain-together-query-rewriting-workflow-prompts-llm-with-retrieval)
            *   [Create a Full RAG Pipeline as a DAG](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#create-a-full-rag-pipeline-as-a-dag)
                
                *   [1\. RAG Pipeline with Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-rag-pipeline-with-query-rewriting)
                *   [2\. RAG Pipeline without Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#2-rag-pipeline-without-query-rewriting)
                
            *   [Defining a Custom Component in a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#defining-a-custom-component-in-a-query-pipeline)
            *   [Stepwise Execution of a Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#stepwise-execution-of-a-pipeline)
            
        *   [Query Pipeline with Async/Parallel Execution](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/)
        *   [Query Pipeline Chat Engine](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/)
        *   [Query Pipeline over Pandas DataFrames](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/)
        *   [Query Pipeline with Routing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/)
        *   [Query Pipeline for Advanced Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/)
        
    *   [ ]  Query Transformations
        
        Query Transformations
        
        *   [HyDE Query Transform](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo/)
        *   [Multi-Step Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_transformations/SimpleIndexDemo-multistep/)
        *   [Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook/)
        
    *   [ ]  Response Synthesizers
        
        Response Synthesizers
        
        *   [Pydantic Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/)
        *   [Stress-Testing Long Context LLMs with a Recall Task](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/long_context_test/)
        *   [Pydantic Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/)
        *   [Refine](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/)
        *   [Refine with Structured Answer Filtering](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/)
        *   [Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/)
        
    *   [ ]  Retrievers
        
        Retrievers
        
        *   [Auto Merging Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/)
        *   [Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval)](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_vs_recursive_retriever/)
        *   [Bedrock (Knowledge Bases)](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/)
        *   [BM25 Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/)
        *   [Composable Objects](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)
        *   [Activeloop Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)
        *   [Ensemble Retrieval Guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)
        *   [Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/)
        *   [Pathway Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/)
        *   [Reciprocal Rerank Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/)
        *   [Recursive Retriever + Node References + Braintrust](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/)
        *   [Recursive Retriever + Node References](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/)
        *   [Relative Score Fusion and Distribution-Based Score Fusion](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/)
        *   [Router Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/router_retriever/)
        *   [Simple Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/)
        *   [Auto-Retrieval from a Vectara Index](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/)
        *   [Vertex AI Search Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/vertex_ai_search_retriever/)
        *   [Videodb retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/)
        *   [You.com Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/you_retriever/)
        
    *   [ ]  Tools
        
        Tools
        
        *   [OnDemandLoaderTool Tutorial](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/)
        *   [Azure Code Interpreter Tool Spec](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/)
        *   [Cassandra Database Tools](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/)
        *   [Evaluation Query Engine Tool](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/)
        
    *   [ ]  Transforms
        
        Transforms
        
        *   [Transforms Evaluation](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/)
        
    *   [ ]  Use Cases
        
        Use Cases
        
        *   [10K Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/)
        *   [10Q Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/)
        *   [Email Data Extraction](https://docs.llamaindex.ai/en/stable/examples/usecases/email_data_extraction/)
        *   [Github Issue Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/)
        
    *   [ ]  Vector Stores
        
        Vector Stores
        
        *   [AWSDocDBDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AWSDocDBDemo/)
        *   [Alibaba Cloud OpenSearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/)
        *   [Amazon Neptune - Neptune Analytics vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/)
        *   [AnalyticDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/)
        *   [Astra DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/)
        *   [Simple Vector Store - Async Index Creation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/)
        *   [Awadb Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/)
        *   [Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)
        *   [Azure CosmosDB MongoDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/)
        *   [Azure Cosmos DB No SQL Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBNoSqlDemo/)
        *   [Bagel Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelAutoRetriever/)
        *   [Bagel Network](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/)
        *   [Baidu VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/)
        *   [Cassandra Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CassandraIndexDemo/)
        *   [Chroma + Fireworks + Nomic with Matryoshka embedding](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaFireworksNomic/)
        *   [Chroma](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/)
        *   [ClickHouse Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/)
        *   [CouchbaseVectorStoreDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/)
        *   [DashVector Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/)
        *   [Databricks Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/)
        *   [Deep Lake Vector Store Quickstart](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/)
        *   [DocArray Hnsw Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/)
        *   [DocArray InMemory Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/)
        *   [DuckDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/)
        *   [Elasticsearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/)
        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Elasticsearch_demo/)
        *   [Epsilla Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/)
        *   [Faiss Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/)
        *   [Firestore Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/)
        *   [Hnswlib](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HnswlibIndexDemo/)
        *   [Hologres](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/)
        *   [Jaguar Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/JaguarIndexDemo/)
        *   [Advanced RAG with temporal filters using LlamaIndex and KDB.AI vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/)
        *   [LanceDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/)
        *   [Lantern Vector Store (auto-retriever)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/)
        *   [Lantern Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/)
        *   [Lindorm](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LindormDemo/)
        *   [Milvus Vector Store With Hybrid Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)
        *   [Milvus Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/)
        *   [MilvusOperatorFunctionDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/)
        *   [MongoDB Atlas Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/)
        *   [MongoDB Atlas + Fireworks AI RAG Example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGFireworks/)
        *   [MongoDB Atlas + OpenAI RAG Example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGOpenAI/)
        *   [MyScale Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/)
        *   [Neo4j vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/)
        *   [Nile Vector Store (Multi-tenant PostgreSQL)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/NileVectorStore/)
        *   [ObjectBox VectorStore Demo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ObjectBoxIndexDemo/)
        *   [OceanBase Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OceanBaseVectorStore/)
        *   [Opensearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)
        *   [pgvecto.rs](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/)
        *   [Pinecone Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)
        *   [Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/)
        *   [Qdrant Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/)
        *   [Qdrant Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_metadata_filter/)
        *   [Qdrant Vector Store - Default Qdrant Filters](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_using_qdrant_filters/)
        *   [Redis Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/)
        *   [Relyt](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/)
        *   [Rockset Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/)
        *   [Simple Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemo/)
        *   [Local Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/)
        *   [Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/)
        *   [Simple Vector Stores - Maximum Marginal Relevance Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoMMR/)
        *   [S3/R2 Storage](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexOnS3/)
        *   [Supabase Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/)
        *   [TablestoreVectorStore](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TablestoreDemo/)
        *   [Tair Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/)
        *   [Tencent Cloud VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TencentVectorDBIndexDemo/)
        *   [TiDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/)
        *   [Timescale Vector Store (PostgreSQL)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Timescalevector/)
        *   [txtai Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TxtaiIndexDemo/)
        *   [Typesense Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/)
        *   [Upstash Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/)
        *   [VearchDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/)
        *   [Google Vertex AI Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/)
        *   [Vespa Vector Store demo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/)
        *   [Weaviate Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)
        *   [Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/)
        *   [Auto-Retrieval from a Weaviate Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/)
        *   [Weaviate Vector Store Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_metadata_filter/)
        *   [WordLift Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WordLiftDemo/)
        *   [Zep Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/)
        *   [Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_auto_retriever/)
        *   [Chroma Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/)
        *   [Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/)
        *   [Guide: Using Vector Store Index with Existing Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/)
        *   [Guide: Using Vector Store Index with Existing Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/)
        *   [Neo4j Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/neo4j_metadata_filter/)
        *   [Oracle AI Vector Search: Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/orallamavs/)
        *   [A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/)
        *   [Pinecone Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/)
        *   [Postgres Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/)
        *   [Hybrid Search with Qdrant BM42](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/)
        *   [Qdrant Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/)
        
    *   [ ]  Workflow
        
        Workflow
        
        *   [JSONalyze Query Engine](https://docs.llamaindex.ai/en/stable/examples/workflow/JSONalyze_query_engine/)
        *   [Workflows for Advanced Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/workflow/advanced_text_to_sql/)
        *   [None](https://docs.llamaindex.ai/en/stable/examples/workflow/auto_retrieval.ipynb)
        *   [Checkpointing Workflow Runs](https://docs.llamaindex.ai/en/stable/examples/workflow/checkpointing_workflows/)
        *   [Build RAG with in-line citations](https://docs.llamaindex.ai/en/stable/examples/workflow/citation_query_engine/)
        *   [Corrective RAG Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/corrective_rag_pack/)
        *   [Workflow for a Function Calling Agent](https://docs.llamaindex.ai/en/stable/examples/workflow/function_calling_agent/)
        *   [Choose Your Own Adventure Workflow (Human In The Loop)](https://docs.llamaindex.ai/en/stable/examples/workflow/human_in_the_loop_story_crafting/)
        *   [LongRAG Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/long_rag_pack/)
        *   [MultiStep Query Engine](https://docs.llamaindex.ai/en/stable/examples/workflow/multi_step_query_engine/)
        *   [Multi-strategy workflow with reflection](https://docs.llamaindex.ai/en/stable/examples/workflow/multi_strategy_workflow/)
        *   [Parallel Execution of Same Event Example](https://docs.llamaindex.ai/en/stable/examples/workflow/parallel_execution/)
        *   [Query Planning Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/planning_workflow/)
        *   [RAG Workflow with Reranking](https://docs.llamaindex.ai/en/stable/examples/workflow/rag/)
        *   [Workflow for a ReAct Agent](https://docs.llamaindex.ai/en/stable/examples/workflow/react_agent/)
        *   [Reflection Workflow for Structured Outputs](https://docs.llamaindex.ai/en/stable/examples/workflow/reflection/)
        *   [Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/workflow/router_query_engine/)
        *   [Self-Discover Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/self_discover_workflow/)
        *   [Sub Question Query Engine as a workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/sub_question_query_engine/)
        *   [Workflows cookbook: walking through all features of Workflows](https://docs.llamaindex.ai/en/stable/examples/workflow/workflows_cookbook/)
        
    
*   [ ] 
    
    [Component Guides](https://docs.llamaindex.ai/en/stable/module_guides/)
    
    Component Guides
    
    *   [ ] 
        
        [Models](https://docs.llamaindex.ai/en/stable/module_guides/models/)
        
        Models
        
        *   [ ]  LLMs
            
            LLMs
            
            *   [Using LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/)
            *   [Standalone Usage](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_standalone/)
            *   [Customizing LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/)
            *   [Available LLM Integrations](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/modules/)
            
        *   [Embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/)
        *   [Multi Modal](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/)
        
    *   [ ] 
        
        [Prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/)
        
        Prompts
        
        *   [Usage pattern](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/usage_pattern/)
        
    *   [ ] 
        
        [Loading](https://docs.llamaindex.ai/en/stable/module_guides/loading/)
        
        Loading
        
        *   [ ] 
            
            [Documents and Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/)
            
            Documents and Nodes
            
            *   [Using Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/)
            *   [Using Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/)
            *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/)
            
        *   [SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/)
        *   [ ] 
            
            [Data Connectors](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/)
            
            Data Connectors
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/)
            *   [LlamaParse](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/modules/)
            
        *   [ ] 
            
            [Node Parsers / Text Splitters](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/)
            
            Node Parsers / Text Splitters
            
            *   [Node Parser Modules](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/)
            
        *   [ ] 
            
            [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/)
            
            Ingestion Pipeline
            
            *   [Transformations](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/)
            
        
    *   [ ] 
        
        [Indexing](https://docs.llamaindex.ai/en/stable/module_guides/indexing/)
        
        Indexing
        
        *   [Index Guide](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/)
        *   [Vector Store Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/)
        *   [Property Graph Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/)
        *   [Document Management](https://docs.llamaindex.ai/en/stable/module_guides/indexing/document_management/)
        *   [LlamaCloud](https://docs.llamaindex.ai/en/stable/module_guides/indexing/llama_cloud_index/)
        *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/module_guides/indexing/metadata_extraction/)
        *   [Modules](https://docs.llamaindex.ai/en/stable/module_guides/indexing/modules/)
        
    *   [ ] 
        
        [Storing](https://docs.llamaindex.ai/en/stable/module_guides/storing/)
        
        Storing
        
        *   [Vector Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/)
        *   [Document Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/)
        *   [Index Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/)
        *   [Chat Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/)
        *   [Key-Value Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/kv_stores/)
        *   [Persisting & Loading Data](https://docs.llamaindex.ai/en/stable/module_guides/storing/save_load/)
        *   [Customizing Storage](https://docs.llamaindex.ai/en/stable/module_guides/storing/customization/)
        
    *   [ ] 
        
        [Querying](https://docs.llamaindex.ai/en/stable/module_guides/querying/)
        
        Querying
        
        *   [ ] 
            
            [Query Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)
            
            Query Engines
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/)
            *   [Response Modes](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/response_modes/)
            *   [Streaming](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/modules/)
            *   [Supporting Modules](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/supporting_modules/)
            
        *   [ ] 
            
            [Chat Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/)
            
            Chat Engines
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/usage_pattern/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/modules/)
            
        *   [ ] 
            
            [Retrieval](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/)
            
            Retrieval
            
            *   [Retriever Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/)
            *   [Retriever Modes](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/)
            
        *   [ ] 
            
            [Node Postprocessors](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/)
            
            Node Postprocessors
            
            *   [Node Postprocessor Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/node_postprocessors/)
            
        *   [ ] 
            
            [Response Synthesis](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/)
            
            Response Synthesis
            
            *   [Response Synthesis Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/)
            
        *   [Routing](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/)
        *   [Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
        *   [ ] 
            
            [Query Pipelines (Deprecated)](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/)
            
            Query Pipelines (Deprecated)
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/modules/)
            *   [Module Usage](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/)
            
        *   [ ] 
            
            [Structured Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/)
            
            Structured Outputs
            
            *   [Output Parsing Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser/)
            *   [(Deprecated) Query Engines + Pydantic Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/query_engine/)
            *   [Pydantic Programs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/)
            
        
    *   [ ] 
        
        [Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
        
        Agents
        
        *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/)
        *   [Lower-Level Agent API](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/agent_runner/)
        *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/modules/)
        *   [Tools](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
        
    *   [ ] 
        
        [Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
        
        Workflows
        
    *   [ ] 
        
        [Evaluation](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/)
        
        Evaluation
        
        *   [Usage Pattern (Response Evaluation)](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern/)
        *   [Usage Pattern (Retrieval)](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/)
        *   [Modules](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/modules/)
        *   [ ]  LlamaDatasets
            
            LlamaDatasets
            
            *   [Contributing A LabelledRagDataset](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/contributing_llamadatasets/)
            *   [Evaluating With LabelledRagDataset's](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/evaluating_with_llamadatasets/)
            *   [Evaluating Evaluators with LabelledEvaluatorDataset's](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/evaluating_evaluators_with_llamadatasets/)
            
        
    *   [ ] 
        
        [Observability](https://docs.llamaindex.ai/en/stable/module_guides/observability/)
        
        Observability
        
        *   [Instrumentation](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/)
        
    *   [Settings](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/)
    *   [ ] 
        
        [Llama Deploy](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/)
        
        Llama Deploy
        
        *   [Getting Started](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/10_getting_started/)
        *   [Core Components](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/)
        *   [Manual orchestration](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/)
        *   [Python SDK](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/)
        *   [CLI](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/)
        
    
*   [ ]  Advanced Topics
    
    Advanced Topics
    
    *   [Building Performant RAG Applications for Production](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)
    *   [Basic Strategies](https://docs.llamaindex.ai/en/stable/optimizing/basic_strategies/basic_strategies/)
    *   [Agentic strategies](https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/)
    *   [ ]  Retrieval
        
        Retrieval
        
        *   [Advanced Retrieval Strategies](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/)
        *   [Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)
        
    *   [ ]  Evaluation
        
        Evaluation
        
        *   [Component Wise Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/component_wise_evaluation/)
        *   [End-to-End Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/e2e_evaluation/)
        *   [Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/evaluation/)
        
    *   [Fine-Tuning](https://docs.llamaindex.ai/en/stable/optimizing/fine-tuning/fine-tuning/)
    *   [Writing Custom Modules](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/)
    *   [Building RAG from Scratch (Lower-Level)](https://docs.llamaindex.ai/en/stable/optimizing/building_rag_from_scratch/)
    
*   [ ] 
    
    [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/)
    
    API Reference
    
    *   [ ] 
        
        [Agents](https://docs.llamaindex.ai/en/stable/api_reference/agent/)
        
        Agents
        
        *   [Coa](https://docs.llamaindex.ai/en/stable/api_reference/agent/coa/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/agent/dashscope/)
        *   [Introspective](https://docs.llamaindex.ai/en/stable/api_reference/agent/introspective/)
        *   [Lats](https://docs.llamaindex.ai/en/stable/api_reference/agent/lats/)
        *   [Llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/)
        *   [Openai legacy](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/)
        *   [React](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/)
        
    *   [ ] 
        
        [Callbacks](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/)
        
        Callbacks
        
        *   [Agentops](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/agentops/)
        *   [Aim](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/)
        *   [Argilla](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/argilla/)
        *   [Arize phoenix](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/arize_phoenix/)
        *   [Deepeval](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/deepeval/)
        *   [Honeyhive](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/honeyhive/)
        *   [Langfuse](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/langfuse/)
        *   [Literalai](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/literalai/)
        *   [Llama debug](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/)
        *   [Openinference](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/opentelemetry.md)
        *   [Opik](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/opik/)
        *   [Promptlayer](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/promptlayer/)
        *   [Token counter](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/)
        *   [Uptrain](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/)
        *   [Wandb](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/)
        
    *   [ ] 
        
        [Chat Engines](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/)
        
        Chat Engines
        
        *   [Condense plus context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_plus_context/)
        *   [Condense question](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/)
        *   [Context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/)
        *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/)
        
    *   [ ] 
        
        [Embeddings](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/)
        
        Embeddings
        
        *   [Adapter](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/)
        *   [Alephalpha](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/alephalpha/)
        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/alibabacloud_aisearch/)
        *   [Anyscale](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/anyscale/)
        *   [Azure inference](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/azure_inference/)
        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/azure_openai/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/bedrock/)
        *   [Clarifai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/clarifai/)
        *   [Clip](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/clip/)
        *   [Cloudflare workersai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/cloudflare_workersai/)
        *   [Cohere](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/cohere/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/dashscope/)
        *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/databricks/)
        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/deepinfra/)
        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/elasticsearch/)
        *   [Fastembed](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/fastembed/)
        *   [Fireworks](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/fireworks/)
        *   [Gaudi](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gaudi/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gemini/)
        *   [Gigachat](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gigachat/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/google/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gradient.md)
        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface/)
        *   [Huggingface api](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_api/)
        *   [Huggingface openvino](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_openvino/)
        *   [Huggingface optimum](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_optimum/)
        *   [Huggingface optimum intel](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_optimum_intel/)
        *   [Ibm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ibm/)
        *   [Instructor](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/instructor/)
        *   [Ipex llm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ipex_llm/)
        *   [Jinaai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/jinaai/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/langchain/)
        *   [Litellm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/litellm/)
        *   [Llamafile](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/llamafile/)
        *   [Llm rails](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/llm_rails/)
        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/mistralai/)
        *   [Mixedbreadai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/mixedbreadai/)
        *   [Modelscope](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/modelscope/)
        *   [Nebius](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nebius/)
        *   [Nomic](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nomic/)
        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nvidia/)
        *   [Oci genai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/oci_genai/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/octoai.md)
        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ollama/)
        *   [Opea](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/opea/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/openai/)
        *   [Oracleai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/oracleai/)
        *   [Premai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/premai/)
        *   [Sagemaker endpoint](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/sagemaker_endpoint/)
        *   [Siliconflow](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/siliconflow/)
        *   [Text embeddings inference](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/text_embeddings_inference/)
        *   [Textembed](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/textembed/)
        *   [Together](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/together/)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/upstage/)
        *   [Vertex](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/vertex/)
        *   [Vertex endpoint](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/vertex_endpoint/)
        *   [Voyageai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/voyageai/)
        *   [Xinference](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/xinference/)
        *   [Yandexgpt](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/yandexgpt/)
        *   [Zhipuai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/zhipuai/)
        
    *   [ ] 
        
        [Evaluation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/)
        
        Evaluation
        
        *   [Answer relevancy](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/answer_relevancy/)
        *   [Context relevancy](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/context_relevancy/)
        *   [Correctness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/correctness/)
        *   [Dataset generation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/)
        *   [Faithfullness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/)
        *   [Guideline](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/)
        *   [Metrics](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/)
        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/multi_modal/)
        *   [Pairwise comparison](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/pairwise_comparison/)
        *   [Query response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/query_response/)
        *   [Response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/response/)
        *   [Retrieval](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/)
        *   [Semantic similarity](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/semantic_similarity/)
        *   [Tonic validate](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/)
        
    *   [ ]  Graph RAG
        
        Graph RAG
        
        *   [Cognee](https://docs.llamaindex.ai/en/stable/api_reference/graph_rag/cognee/)
        
    *   [ ] 
        
        [Indexes](https://docs.llamaindex.ai/en/stable/api_reference/indices/)
        
        Indexes
        
        *   [Bge m3](https://docs.llamaindex.ai/en/stable/api_reference/indices/bge_m3/)
        *   [Colbert](https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/)
        *   [Document summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/)
        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/)
        *   [Llama cloud](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/)
        *   [Postgresml](https://docs.llamaindex.ai/en/stable/api_reference/indices/postgresml/)
        *   [Property graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/)
        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/)
        *   [Tree](https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/)
        *   [Vectara](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/)
        *   [Vector](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/)
        *   [Vertexai](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/)
        *   [Zilliz](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/)
        
    *   [ ] 
        
        [Ingestion](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/)
        
        Ingestion
        
    *   [ ] 
        
        [Instrumentation](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/)
        
        Instrumentation
        
        *   [Event handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/)
        *   [Event types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/)
        *   [Span handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/)
        *   [Span types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_types/)
        
    *   [ ] 
        
        [LLMs](https://docs.llamaindex.ai/en/stable/api_reference/llms/)
        
        LLMs
        
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/OptimumIntelLLM.md)
        *   [Ai21](https://docs.llamaindex.ai/en/stable/api_reference/llms/ai21/)
        *   [Alephalpha](https://docs.llamaindex.ai/en/stable/api_reference/llms/alephalpha/)
        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/llms/alibabacloud_aisearch/)
        *   [Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/llms/anthropic/)
        *   [Anyscale](https://docs.llamaindex.ai/en/stable/api_reference/llms/anyscale/)
        *   [Azure inference](https://docs.llamaindex.ai/en/stable/api_reference/llms/azure_inference/)
        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/llms/azure_openai/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/llms/bedrock/)
        *   [Bedrock converse](https://docs.llamaindex.ai/en/stable/api_reference/llms/bedrock_converse/)
        *   [Cerebras](https://docs.llamaindex.ai/en/stable/api_reference/llms/cerebras/)
        *   [Clarifai](https://docs.llamaindex.ai/en/stable/api_reference/llms/clarifai/)
        *   [Cleanlab](https://docs.llamaindex.ai/en/stable/api_reference/llms/cleanlab/)
        *   [Cohere](https://docs.llamaindex.ai/en/stable/api_reference/llms/cohere/)
        *   [Custom llm](https://docs.llamaindex.ai/en/stable/api_reference/llms/custom_llm/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/llms/dashscope/)
        *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/llms/databricks/)
        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/api_reference/llms/deepinfra/)
        *   [Everlyai](https://docs.llamaindex.ai/en/stable/api_reference/llms/everlyai/)
        *   [Fireworks](https://docs.llamaindex.ai/en/stable/api_reference/llms/fireworks/)
        *   [Friendli](https://docs.llamaindex.ai/en/stable/api_reference/llms/friendli/)
        *   [Gaudi](https://docs.llamaindex.ai/en/stable/api_reference/llms/gaudi/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/llms/gemini/)
        *   [Gigachat](https://docs.llamaindex.ai/en/stable/api_reference/llms/gigachat/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/gradient.md)
        *   [Groq](https://docs.llamaindex.ai/en/stable/api_reference/llms/groq/)
        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/llms/huggingface/)
        *   [Huggingface api](https://docs.llamaindex.ai/en/stable/api_reference/llms/huggingface_api/)
        *   [Ibm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ibm/)
        *   [Ipex llm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ipex_llm/)
        *   [Keywordsai](https://docs.llamaindex.ai/en/stable/api_reference/llms/keywordsai/)
        *   [Konko](https://docs.llamaindex.ai/en/stable/api_reference/llms/konko/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/llms/langchain/)
        *   [Litellm](https://docs.llamaindex.ai/en/stable/api_reference/llms/litellm/)
        *   [Llama api](https://docs.llamaindex.ai/en/stable/api_reference/llms/llama_api/)
        *   [Llama cpp](https://docs.llamaindex.ai/en/stable/api_reference/llms/llama_cpp/)
        *   [Llamafile](https://docs.llamaindex.ai/en/stable/api_reference/llms/llamafile/)
        *   [Lmstudio](https://docs.llamaindex.ai/en/stable/api_reference/llms/lmstudio/)
        *   [Localai](https://docs.llamaindex.ai/en/stable/api_reference/llms/localai/)
        *   [Maritalk](https://docs.llamaindex.ai/en/stable/api_reference/llms/maritalk/)
        *   [Mistral rs](https://docs.llamaindex.ai/en/stable/api_reference/llms/mistral_rs/)
        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/llms/mistralai/)
        *   [Mlx](https://docs.llamaindex.ai/en/stable/api_reference/llms/mlx/)
        *   [Modelscope](https://docs.llamaindex.ai/en/stable/api_reference/llms/modelscope/)
        *   [Monsterapi](https://docs.llamaindex.ai/en/stable/api_reference/llms/monsterapi/)
        *   [Mymagic](https://docs.llamaindex.ai/en/stable/api_reference/llms/mymagic/)
        *   [Nebius](https://docs.llamaindex.ai/en/stable/api_reference/llms/nebius/)
        *   [Neutrino](https://docs.llamaindex.ai/en/stable/api_reference/llms/neutrino/)
        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia/)
        *   [Nvidia tensorrt](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia_tensorrt/)
        *   [Nvidia triton](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia_triton/)
        *   [Oci genai](https://docs.llamaindex.ai/en/stable/api_reference/llms/oci_genai/)
        *   [Octoai](https://docs.llamaindex.ai/en/stable/api_reference/llms/octoai/)
        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/llms/ollama/)
        *   [Opea](https://docs.llamaindex.ai/en/stable/api_reference/llms/opea/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai/)
        *   [Openai like](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai_like/)
        *   [Openllm](https://docs.llamaindex.ai/en/stable/api_reference/llms/openllm/)
        *   [Openrouter](https://docs.llamaindex.ai/en/stable/api_reference/llms/openrouter/)
        *   [Openvino](https://docs.llamaindex.ai/en/stable/api_reference/llms/openvino/)
        *   [Optimum intel](https://docs.llamaindex.ai/en/stable/api_reference/llms/optimum_intel/)
        *   [Paieas](https://docs.llamaindex.ai/en/stable/api_reference/llms/paieas/)
        *   [Palm](https://docs.llamaindex.ai/en/stable/api_reference/llms/palm/)
        *   [Perplexity](https://docs.llamaindex.ai/en/stable/api_reference/llms/perplexity/)
        *   [Pipeshift](https://docs.llamaindex.ai/en/stable/api_reference/llms/pipeshift/)
        *   [Portkey](https://docs.llamaindex.ai/en/stable/api_reference/llms/portkey/)
        *   [Predibase](https://docs.llamaindex.ai/en/stable/api_reference/llms/predibase/)
        *   [Premai](https://docs.llamaindex.ai/en/stable/api_reference/llms/premai/)
        *   [Qianfan](https://docs.llamaindex.ai/en/stable/api_reference/llms/qianfan/)
        *   [Reka](https://docs.llamaindex.ai/en/stable/api_reference/llms/reka/)
        *   [Replicate](https://docs.llamaindex.ai/en/stable/api_reference/llms/replicate/)
        *   [Rungpt](https://docs.llamaindex.ai/en/stable/api_reference/llms/rungpt/)
        *   [Sagemaker endpoint](https://docs.llamaindex.ai/en/stable/api_reference/llms/sagemaker_endpoint/)
        *   [Sambanovasystems](https://docs.llamaindex.ai/en/stable/api_reference/llms/sambanovasystems/)
        *   [Siliconflow](https://docs.llamaindex.ai/en/stable/api_reference/llms/siliconflow/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/solar.md)
        *   [Text generation inference](https://docs.llamaindex.ai/en/stable/api_reference/llms/text_generation_inference/)
        *   [Together](https://docs.llamaindex.ai/en/stable/api_reference/llms/together/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/unify.md)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/llms/upstage/)
        *   [Vertex](https://docs.llamaindex.ai/en/stable/api_reference/llms/vertex/)
        *   [Vllm](https://docs.llamaindex.ai/en/stable/api_reference/llms/vllm/)
        *   [Xinference](https://docs.llamaindex.ai/en/stable/api_reference/llms/xinference/)
        *   [Yi](https://docs.llamaindex.ai/en/stable/api_reference/llms/yi/)
        *   [You](https://docs.llamaindex.ai/en/stable/api_reference/llms/you/)
        *   [Zhipuai](https://docs.llamaindex.ai/en/stable/api_reference/llms/zhipuai/)
        
    *   [ ] 
        
        [Llama Datasets](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/)
        
        Llama Datasets
        
    *   [ ]  Llama Deploy
        
        Llama Deploy
        
        *   [apiserver](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/apiserver/)
        *   [control\_plane](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/control_plane/)
        *   [deploy](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/deploy/)
        *   [message\_consumers](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_consumers/)
        *   [message\_publishers](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_publishers/)
        *   [messages](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/messages/)
        *   [orchestrators](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/orchestrators/)
        *   [Python SDK](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/python_sdk/)
        *   [services](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/services/)
        *   [types](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/types/)
        *   [ ] 
            
            [message\_queues](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/)
            
            message\_queues
            
            *   [apache\_kafka](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/kafka/)
            *   [rabbitmq](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/rabbitmq/)
            *   [redis](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/redis/)
            *   [simple](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/simple/)
            
        
    *   [ ] 
        
        [Llama Packs](https://docs.llamaindex.ai/en/stable/api_reference/packs/)
        
        Llama Packs
        
        *   [Agent search retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/agent_search_retriever/)
        *   [Agents coa](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/)
        *   [Agents lats](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/)
        *   [Agents llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/)
        *   [Amazon product extraction](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/)
        *   [Arize phoenix query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/)
        *   [Auto merging retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/)
        *   [Chroma autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/chroma_autoretrieval/)
        *   [Code hierarchy](https://docs.llamaindex.ai/en/stable/api_reference/packs/code_hierarchy/)
        *   [Cogniswitch agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/)
        *   [Cohere citation chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/)
        *   [Corrective rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/)
        *   [Deeplake deepmemory retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/)
        *   [Deeplake multimodal retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_multimodal_retrieval/)
        *   [Dense x retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/)
        *   [Diff private simple dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/)
        *   [Evaluator benchmarker](https://docs.llamaindex.ai/en/stable/api_reference/packs/evaluator_benchmarker/)
        *   [Fusion retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/)
        *   [Fuzzy citation](https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/)
        *   [Gmail openai agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/gmail_openai_agent/)
        *   [Gradio agent chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_agent_chat/)
        *   [Gradio react agent chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_react_agent_chatbot/)
        *   [Infer retrieve rerank](https://docs.llamaindex.ai/en/stable/api_reference/packs/infer_retrieve_rerank/)
        *   [Koda retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/koda_retriever/)
        *   [Llama dataset metadata](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_dataset_metadata/)
        *   [Llama guard moderator](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/)
        *   [Llava completion](https://docs.llamaindex.ai/en/stable/api_reference/packs/llava_completion/)
        *   [Longrag](https://docs.llamaindex.ai/en/stable/api_reference/packs/longrag/)
        *   [Mixture of agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/)
        *   [Multi document agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/)
        *   [Multi tenancy rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/)
        *   [Multidoc autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/)
        *   [Nebulagraph query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/)
        *   [Neo4j query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/neo4j_query_engine/)
        *   [Node parser semantic chunking](https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/)
        *   [Ollama query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/)
        *   [Panel chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/panel_chatbot/)
        *   [Query understanding agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/query_understanding_agent/)
        *   [Raft dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/)
        *   [Rag cli local](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/)
        *   [Rag evaluator](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_evaluator/)
        *   [Rag fusion query pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/)
        *   [Ragatouille retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/)
        *   [Raptor](https://docs.llamaindex.ai/en/stable/api_reference/packs/raptor/)
        *   [Recursive retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/)
        *   [Resume screener](https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/)
        *   [Retry engine weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/retry_engine_weaviate/)
        *   [Secgpt](https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/)
        *   [Self discover](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/)
        *   [Self rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_rag/)
        *   [Sentence window retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/sentence_window_retriever/)
        *   [Snowflake query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/)
        *   [Stock market data query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/)
        *   [Streamlit chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/)
        *   [Sub question weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/sub_question_weaviate/)
        *   [Tables](https://docs.llamaindex.ai/en/stable/api_reference/packs/tables/)
        *   [Timescale vector autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/timescale_vector_autoretrieval/)
        *   [Trulens eval packs](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/packs/vanna.md)
        *   [Vectara rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/vectara_rag/)
        *   [Voyage query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/voyage_query_engine/)
        *   [Zenguard](https://docs.llamaindex.ai/en/stable/api_reference/packs/zenguard/)
        *   [Zephyr query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/)
        
    *   [ ] 
        
        [Memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/)
        
        Memory
        
        *   [Chat memory buffer](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/)
        *   [Mem0](https://docs.llamaindex.ai/en/stable/api_reference/memory/mem0/)
        *   [Simple composable memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/)
        *   [Vector memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/)
        
    *   [ ] 
        
        [Metadata Extractors](https://docs.llamaindex.ai/en/stable/api_reference/extractors/)
        
        Metadata Extractors
        
        *   [Entity](https://docs.llamaindex.ai/en/stable/api_reference/extractors/entity/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/extractors/keyword/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/extractors/llama_extract.md)
        *   [Marvin](https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/)
        *   [Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/)
        *   [Question](https://docs.llamaindex.ai/en/stable/api_reference/extractors/question/)
        *   [Relik](https://docs.llamaindex.ai/en/stable/api_reference/extractors/relik/)
        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/extractors/summary/)
        *   [Title](https://docs.llamaindex.ai/en/stable/api_reference/extractors/title/)
        
    *   [ ] 
        
        [Multi-Modal LLMs](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/)
        
        Multi-Modal LLMs
        
        *   [Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/anthropic/)
        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/azure_openai/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/bedrock/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/dashscope/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/gemini/)
        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/huggingface/)
        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/mistralai/)
        *   [Nebius](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/nebius/)
        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/nvidia/)
        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/)
        *   [Openvino](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openvino/)
        *   [Reka](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/reka/)
        *   [Replicate](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/)
        *   [Zhipuai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/zhipuai/)
        
    *   [ ] 
        
        [Node Parsers & Text Splitters](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/)
        
        Node Parsers & Text Splitters
        
        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/alibabacloud_aisearch/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/)
        *   [Docling](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/docling/)
        *   [Topic](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/topic/)
        *   [Code](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/)
        *   [Hierarchical](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/)
        *   [Html](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/html/)
        *   [Json](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/langchain/)
        *   [Markdown](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown/)
        *   [Markdown element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown_element/)
        *   [Semantic splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/)
        *   [Sentence splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/)
        *   [Sentence window](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/)
        *   [Token text splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/)
        *   [Unstructured element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/)
        
    *   [ ] 
        
        [Node Postprocessors](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/)
        
        Node Postprocessors
        
        *   [NER PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/NER_PII/)
        *   [PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/PII/)
        *   [Alibabacloud aisearch rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/alibabacloud_aisearch_rerank/)
        *   [Auto prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/auto_prev_next/)
        *   [Bedrock rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/bedrock_rerank/)
        *   [Cohere rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/cohere_rerank/)
        *   [Colbert rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/colbert_rerank/)
        *   [Colpali rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/colpali_rerank/)
        *   [Dashscope rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/dashscope_rerank/)
        *   [Embedding recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/embedding_recency/)
        *   [Fixed recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/fixed_recency/)
        *   [Flag embedding reranker](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/flag_embedding_reranker/)
        *   [Jinaai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/jinaai_rerank/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/keyword/)
        *   [Llm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/llm_rerank/)
        *   [Long context reorder](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/long_context_reorder/)
        *   [Longllmlingua](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/longllmlingua/)
        *   [Metadata replacement](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/metadata_replacement/)
        *   [Mixedbreadai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/mixedbreadai_rerank/)
        *   [Nvidia rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/nvidia_rerank/)
        *   [Openvino rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/openvino_rerank/)
        *   [Pinecone native rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/pinecone_native_rerank/)
        *   [Presidio](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/presidio/)
        *   [Prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/prev_next/)
        *   [Rankgpt rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankgpt_rerank/)
        *   [Rankllm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankllm_rerank/)
        *   [Sbert rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sbert_rerank/)
        *   [Sentence optimizer](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sentence_optimizer/)
        *   [Siliconflow rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/siliconflow_rerank/)
        *   [Similarity](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/similarity/)
        *   [Tei rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/tei_rerank/)
        *   [Time weighted](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/time_weighted/)
        *   [Voyageai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/voyageai_rerank/)
        *   [Xinference rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/xinference_rerank/)
        
    *   [ ] 
        
        [Object Stores](https://docs.llamaindex.ai/en/stable/api_reference/objects/)
        
        Object Stores
        
    *   [ ] 
        
        [Output Parsers](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/)
        
        Output Parsers
        
        *   [Guardrails](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/)
        *   [Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/)
        *   [Selection](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/selection/)
        
    *   [ ] 
        
        [Programs](https://docs.llamaindex.ai/en/stable/api_reference/program/)
        
        Programs
        
        *   [Evaporate](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/)
        *   [Guidance](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/)
        *   [Llm text completion](https://docs.llamaindex.ai/en/stable/api_reference/program/llm_text_completion/)
        *   [Lmformatenforcer](https://docs.llamaindex.ai/en/stable/api_reference/program/lmformatenforcer/)
        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/program/multi_modal/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/program/openai/)
        
    *   [ ] 
        
        [Prompts](https://docs.llamaindex.ai/en/stable/api_reference/prompts/)
        
        Prompts
        
    *   [ ] 
        
        [Query Engines](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/)
        
        Query Engines
        
        *   [FLARE](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/FLARE/)
        *   [JSONalayze](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/JSONalayze/)
        *   [NL SQL table](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/)
        *   [PGVector SQL](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/)
        *   [SQL join](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/)
        *   [SQL table retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/)
        *   [Citation](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/)
        *   [Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/cogniswitch/)
        *   [Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/)
        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/)
        *   [Multi step](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/multi_step/)
        *   [Pandas](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/pandas/)
        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/)
        *   [Retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever_router/)
        *   [Retry](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/)
        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/)
        *   [Simple multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/)
        *   [Sub question](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/)
        *   [Tool retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/tool_retriever_router/)
        *   [Transform](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/transform/)
        
    *   [ ] 
        
        [Query Pipeline](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/)
        
        Query Pipeline
        
        *   [Agent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/)
        *   [Arg pack](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/arg_pack/)
        *   [Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/)
        *   [Function](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/)
        *   [Input](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/input/)
        *   [Llm](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/)
        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/multi_modal/)
        *   [Object](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/object/)
        *   [Output parser](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/output_parser/)
        *   [Postprocessor](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/postprocessor/)
        *   [Prompt](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/prompt/)
        *   [Query engine](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/query_engine/)
        *   [Query transform](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/query_transform/)
        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/retriever/)
        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/)
        *   [Synthesizer](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/)
        *   [Tool runner](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/tool_runner/)
        
    *   [ ] 
        
        [Question Generators](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/)
        
        Question Generators
        
        *   [Guidance](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/guidance/)
        *   [Llm question gen](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/openai/)
        
    *   [ ] 
        
        [Readers](https://docs.llamaindex.ai/en/stable/api_reference/readers/)
        
        Readers
        
        *   [Agent search](https://docs.llamaindex.ai/en/stable/api_reference/readers/agent_search/)
        *   [Airbyte cdk](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_cdk/)
        *   [Airbyte gong](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_gong/)
        *   [Airbyte hubspot](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_hubspot/)
        *   [Airbyte salesforce](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_salesforce/)
        *   [Airbyte shopify](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_shopify/)
        *   [Airbyte stripe](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_stripe/)
        *   [Airbyte typeform](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_typeform/)
        *   [Airbyte zendesk support](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_zendesk_support/)
        *   [Airtable](https://docs.llamaindex.ai/en/stable/api_reference/readers/airtable/)
        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/alibabacloud_aisearch/)
        *   [Apify](https://docs.llamaindex.ai/en/stable/api_reference/readers/apify/)
        *   [Arango db](https://docs.llamaindex.ai/en/stable/api_reference/readers/arango_db/)
        *   [Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/readers/arxiv/)
        *   [Asana](https://docs.llamaindex.ai/en/stable/api_reference/readers/asana/)
        *   [Assemblyai](https://docs.llamaindex.ai/en/stable/api_reference/readers/assemblyai/)
        *   [Astra db](https://docs.llamaindex.ai/en/stable/api_reference/readers/astra_db/)
        *   [Athena](https://docs.llamaindex.ai/en/stable/api_reference/readers/athena/)
        *   [Awadb](https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/)
        *   [Azcognitive search](https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/)
        *   [Azstorage blob](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/)
        *   [Bagel](https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/)
        *   [Bilibili](https://docs.llamaindex.ai/en/stable/api_reference/readers/bilibili/)
        *   [Bitbucket](https://docs.llamaindex.ai/en/stable/api_reference/readers/bitbucket/)
        *   [Boarddocs](https://docs.llamaindex.ai/en/stable/api_reference/readers/boarddocs/)
        *   [Box](https://docs.llamaindex.ai/en/stable/api_reference/readers/box/)
        *   [Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/readers/chatgpt_plugin/)
        *   [Chroma](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse.md)
        *   [Confluence](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/)
        *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/)
        *   [Couchdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchdb/)
        *   [Dad jokes](https://docs.llamaindex.ai/en/stable/api_reference/readers/dad_jokes/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/)
        *   [Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashvector/)
        *   [Database](https://docs.llamaindex.ai/en/stable/api_reference/readers/database/)
        *   [Deeplake](https://docs.llamaindex.ai/en/stable/api_reference/readers/deeplake/)
        *   [Discord](https://docs.llamaindex.ai/en/stable/api_reference/readers/discord/)
        *   [Docling](https://docs.llamaindex.ai/en/stable/api_reference/readers/docling/)
        *   [Docstring walker](https://docs.llamaindex.ai/en/stable/api_reference/readers/docstring_walker/)
        *   [Docugami](https://docs.llamaindex.ai/en/stable/api_reference/readers/docugami/)
        *   [Document360](https://docs.llamaindex.ai/en/stable/api_reference/readers/document360/)
        *   [Earnings call transcript](https://docs.llamaindex.ai/en/stable/api_reference/readers/earnings_call_transcript/)
        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/elasticsearch/)
        *   [Faiss](https://docs.llamaindex.ai/en/stable/api_reference/readers/faiss/)
        *   [Feedly rss](https://docs.llamaindex.ai/en/stable/api_reference/readers/feedly_rss/)
        *   [Feishu docs](https://docs.llamaindex.ai/en/stable/api_reference/readers/feishu_docs/)
        *   [File](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/)
        *   [Firebase realtimedb](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/)
        *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/firestore/)
        *   [Gcs](https://docs.llamaindex.ai/en/stable/api_reference/readers/gcs/)
        *   [Genius](https://docs.llamaindex.ai/en/stable/api_reference/readers/genius/)
        *   [Gitbook](https://docs.llamaindex.ai/en/stable/api_reference/readers/gitbook/)
        *   [Github](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/)
        *   [Gitlab](https://docs.llamaindex.ai/en/stable/api_reference/readers/gitlab/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/)
        *   [Gpt repo](https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/)
        *   [Graphdb cypher](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/)
        *   [Graphql](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/)
        *   [Guru](https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/)
        *   [Hatena blog](https://docs.llamaindex.ai/en/stable/api_reference/readers/hatena_blog/)
        *   [Hive](https://docs.llamaindex.ai/en/stable/api_reference/readers/hive/)
        *   [Hubspot](https://docs.llamaindex.ai/en/stable/api_reference/readers/hubspot/)
        *   [Huggingface fs](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/)
        *   [Hwp](https://docs.llamaindex.ai/en/stable/api_reference/readers/hwp/)
        *   [Iceberg](https://docs.llamaindex.ai/en/stable/api_reference/readers/iceberg/)
        *   [Imdb review](https://docs.llamaindex.ai/en/stable/api_reference/readers/imdb_review/)
        *   [Intercom](https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/)
        *   [Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/readers/jaguar/)
        *   [Jira](https://docs.llamaindex.ai/en/stable/api_reference/readers/jira/)
        *   [Joplin](https://docs.llamaindex.ai/en/stable/api_reference/readers/joplin/)
        *   [Json](https://docs.llamaindex.ai/en/stable/api_reference/readers/json/)
        *   [Kaltura esearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/kaltura_esearch/)
        *   [Kibela](https://docs.llamaindex.ai/en/stable/api_reference/readers/kibela/)
        *   [Lilac](https://docs.llamaindex.ai/en/stable/api_reference/readers/lilac/)
        *   [Linear](https://docs.llamaindex.ai/en/stable/api_reference/readers/linear/)
        *   [Llama parse](https://docs.llamaindex.ai/en/stable/api_reference/readers/llama_parse/)
        *   [Macrometa gdn](https://docs.llamaindex.ai/en/stable/api_reference/readers/macrometa_gdn/)
        *   [Make com](https://docs.llamaindex.ai/en/stable/api_reference/readers/make_com/)
        *   [Mangadex](https://docs.llamaindex.ai/en/stable/api_reference/readers/mangadex/)
        *   [Mangoapps guides](https://docs.llamaindex.ai/en/stable/api_reference/readers/mangoapps_guides/)
        *   [Maps](https://docs.llamaindex.ai/en/stable/api_reference/readers/maps/)
        *   [Mbox](https://docs.llamaindex.ai/en/stable/api_reference/readers/mbox/)
        *   [Memos](https://docs.llamaindex.ai/en/stable/api_reference/readers/memos/)
        *   [Metal](https://docs.llamaindex.ai/en/stable/api_reference/readers/metal/)
        *   [Microsoft onedrive](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/)
        *   [Microsoft outlook](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/)
        *   [Microsoft sharepoint](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/)
        *   [Milvus](https://docs.llamaindex.ai/en/stable/api_reference/readers/milvus/)
        *   [Minio](https://docs.llamaindex.ai/en/stable/api_reference/readers/minio/)
        *   [Mondaydotcom](https://docs.llamaindex.ai/en/stable/api_reference/readers/mondaydotcom/)
        *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/readers/mongodb/)
        *   [Myscale](https://docs.llamaindex.ai/en/stable/api_reference/readers/myscale/)
        *   [Notion](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/)
        *   [Nougat ocr](https://docs.llamaindex.ai/en/stable/api_reference/readers/nougat_ocr/)
        *   [Obsidian](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/)
        *   [Openalex](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi.md)
        *   [Opendal](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/)
        *   [Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/)
        *   [Oracleai](https://docs.llamaindex.ai/en/stable/api_reference/readers/oracleai/)
        *   [Pandas ai](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/)
        *   [Papers](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/)
        *   [Patentsview](https://docs.llamaindex.ai/en/stable/api_reference/readers/patentsview/)
        *   [Pathway](https://docs.llamaindex.ai/en/stable/api_reference/readers/pathway/)
        *   [Pdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdb/)
        *   [Pdf marker](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/)
        *   [Pdf table](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_table/)
        *   [Pebblo](https://docs.llamaindex.ai/en/stable/api_reference/readers/pebblo/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/pinecone.md)
        *   [Preprocess](https://docs.llamaindex.ai/en/stable/api_reference/readers/preprocess/)
        *   [Psychic](https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/)
        *   [Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/readers/qdrant/)
        *   [Quip](https://docs.llamaindex.ai/en/stable/api_reference/readers/quip/)
        *   [Rayyan](https://docs.llamaindex.ai/en/stable/api_reference/readers/rayyan/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/readme.md)
        *   [Readwise](https://docs.llamaindex.ai/en/stable/api_reference/readers/readwise/)
        *   [Reddit](https://docs.llamaindex.ai/en/stable/api_reference/readers/reddit/)
        *   [Remote](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote/)
        *   [Remote depth](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote_depth/)
        *   [S3](https://docs.llamaindex.ai/en/stable/api_reference/readers/s3/)
        *   [Sec filings](https://docs.llamaindex.ai/en/stable/api_reference/readers/sec_filings/)
        *   [Semanticscholar](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/)
        *   [Simple directory reader](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/)
        *   [Singlestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/singlestore/)
        *   [Slack](https://docs.llamaindex.ai/en/stable/api_reference/readers/slack/)
        *   [Smart pdf loader](https://docs.llamaindex.ai/en/stable/api_reference/readers/smart_pdf_loader/)
        *   [Snowflake](https://docs.llamaindex.ai/en/stable/api_reference/readers/snowflake/)
        *   [Spotify](https://docs.llamaindex.ai/en/stable/api_reference/readers/spotify/)
        *   [Stackoverflow](https://docs.llamaindex.ai/en/stable/api_reference/readers/stackoverflow/)
        *   [Steamship](https://docs.llamaindex.ai/en/stable/api_reference/readers/steamship/)
        *   [String iterable](https://docs.llamaindex.ai/en/stable/api_reference/readers/string_iterable/)
        *   [Stripe docs](https://docs.llamaindex.ai/en/stable/api_reference/readers/stripe_docs/)
        *   [Structured data](https://docs.llamaindex.ai/en/stable/api_reference/readers/structured_data/)
        *   [Telegram](https://docs.llamaindex.ai/en/stable/api_reference/readers/telegram/)
        *   [Toggl](https://docs.llamaindex.ai/en/stable/api_reference/readers/toggl/)
        *   [Trello](https://docs.llamaindex.ai/en/stable/api_reference/readers/trello/)
        *   [Twitter](https://docs.llamaindex.ai/en/stable/api_reference/readers/twitter/)
        *   [Txtai](https://docs.llamaindex.ai/en/stable/api_reference/readers/txtai/)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/readers/upstage/)
        *   [Weather](https://docs.llamaindex.ai/en/stable/api_reference/readers/weather/)
        *   [Weaviate](https://docs.llamaindex.ai/en/stable/api_reference/readers/weaviate/)
        *   [Web](https://docs.llamaindex.ai/en/stable/api_reference/readers/web/)
        *   [Whatsapp](https://docs.llamaindex.ai/en/stable/api_reference/readers/whatsapp/)
        *   [Wikipedia](https://docs.llamaindex.ai/en/stable/api_reference/readers/wikipedia/)
        *   [Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/readers/wordlift/)
        *   [Wordpress](https://docs.llamaindex.ai/en/stable/api_reference/readers/wordpress/)
        *   [Youtube transcript](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_transcript/)
        *   [Zendesk](https://docs.llamaindex.ai/en/stable/api_reference/readers/zendesk/)
        *   [Zep](https://docs.llamaindex.ai/en/stable/api_reference/readers/zep/)
        *   [Zulip](https://docs.llamaindex.ai/en/stable/api_reference/readers/zulip/)
        *   [Zyte serp](https://docs.llamaindex.ai/en/stable/api_reference/readers/zyte_serp/)
        
    *   [ ] 
        
        [Response Synthesizers](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/)
        
        Response Synthesizers
        
        *   [Accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/accumulate/)
        *   [Compact accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_accumulate/)
        *   [Compact and refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_and_refine/)
        *   [Generation](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/generation/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/google/)
        *   [Refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/refine/)
        *   [Simple summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/simple_summarize/)
        *   [Tree summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/tree_summarize/)
        
    *   [ ] 
        
        [Retrievers](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/)
        
        Retrievers
        
        *   [Auto merging](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/auto_merging/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bedrock/)
        *   [Bm25](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/)
        *   [Duckdb retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/duckdb_retriever/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/)
        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/knowledge_graph/)
        *   [Mongodb atlas bm25 retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/mongodb_atlas_bm25_retriever/)
        *   [Pathway](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/pathway/)
        *   [Query fusion](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/query_fusion/)
        *   [Recursive](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/)
        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/)
        *   [Sql](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/)
        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/)
        *   [Transform](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/transform/)
        *   [Tree](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/)
        *   [Vector](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/)
        *   [Vertexai search](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vertexai_search/)
        *   [Videodb](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/videodb/)
        *   [You](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/you/)
        
    *   [ ] 
        
        [Schema](https://docs.llamaindex.ai/en/stable/api_reference/schema/)
        
        Schema
        
    *   [ ]  Selectors
        
        Selectors
        
        *   [Notdiamond](https://docs.llamaindex.ai/en/stable/api_reference/selectors/notdiamond/)
        
    *   [ ]  Sparse Embeddings
        
        Sparse Embeddings
        
        *   [Fastembed](https://docs.llamaindex.ai/en/stable/api_reference/sparse_embeddings/fastembed/)
        
    *   [ ]  Storage
        
        Storage
        
        *   [ ] 
            
            [Chat Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/)
            
            Chat Store
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/)
            *   [Azurecosmosmongovcore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azurecosmosmongovcore/)
            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azurecosmosnosql/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/dynamodb/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/postgres/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/)
            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/tablestore/)
            *   [Upstash](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/upstash/)
            
        *   [ ] 
            
            [Docstore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/)
            
            Docstore
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/)
            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azurecosmosnosql/)
            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/couchbase/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/elasticsearch/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/mongodb/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/redis/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/)
            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/tablestore/)
            
        *   [ ] 
            
            [Graph Stores](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/)
            
            Graph Stores
            
            *   [Falkordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/falkordb/)
            *   [Kuzu](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/kuzu/)
            *   [Memgraph](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/memgraph/)
            *   [Nebula](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/nebula/)
            *   [Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/)
            *   [Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/simple/)
            *   [Tidb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/tidb/)
            
        *   [ ] 
            
            [Index Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/)
            
            Index Store
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/)
            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azurecosmosnosql/)
            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/couchbase/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/elasticsearch/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/firestore/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/postgres/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/simple/)
            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/tablestore/)
            
        *   [ ] 
            
            [Kvstore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/)
            
            Kvstore
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/)
            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azurecosmosnosql/)
            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/couchbase/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/elasticsearch/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/redis/)
            *   [S3](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/s3/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/)
            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/tablestore/)
            
        *   [ ]  Storage
            
            Storage
            
            *   [Storage context](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/)
            
        *   [ ] 
            
            [Vector Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/)
            
            Vector Store
            
            *   [Alibabacloud opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/alibabacloud_opensearch/)
            *   [Analyticdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/analyticdb/)
            *   [Astra db](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/astra_db/)
            *   [Awadb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awadb/)
            *   [Awsdocdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/)
            *   [Azureaisearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/)
            *   [Azurecosmosmongo](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/)
            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosnosql/)
            *   [Bagel](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/bagel/)
            *   [Baiduvectordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/baiduvectordb/)
            *   [Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/cassandra/)
            *   [None](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin.md)
            *   [Chroma](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/)
            *   [Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/clickhouse/)
            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/)
            *   [Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dashvector/)
            *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/databricks/)
            *   [Deeplake](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/deeplake/)
            *   [Docarray](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/docarray/)
            *   [Duckdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/duckdb/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/elasticsearch/)
            *   [Epsilla](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/epsilla/)
            *   [Faiss](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/faiss/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/firestore/)
            *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/)
            *   [Hologres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/)
            *   [Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/)
            *   [Kdbai](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/kdbai/)
            *   [Lancedb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lancedb/)
            *   [Lantern](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lantern/)
            *   [Lindorm](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lindorm/)
            *   [Mariadb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mariadb/)
            *   [None](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/metal.md)
            *   [Milvus](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/milvus/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/)
            *   [Myscale](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/myscale/)
            *   [Neo4jvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/)
            *   [Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/)
            *   [Nile](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/nile/)
            *   [Objectbox](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/objectbox/)
            *   [Oceanbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/oceanbase/)
            *   [Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/)
            *   [Oracledb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/oracledb/)
            *   [Pgvecto rs](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pgvecto_rs/)
            *   [Pinecone](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/)
            *   [Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/qdrant/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/redis/)
            *   [Relyt](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/relyt/)
            *   [Rocksetdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/rocksetdb/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/simple/)
            *   [Singlestoredb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/)
            *   [None](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/sqlalchemy.md)
            *   [Supabase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/)
            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tablestore/)
            *   [Tair](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tair/)
            *   [Tencentvectordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tencentvectordb/)
            *   [Tidbvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tidbvector/)
            *   [Timescalevector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/timescalevector/)
            *   [Txtai](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/txtai/)
            *   [Typesense](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/typesense/)
            *   [Upstash](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/)
            *   [Vearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vearch/)
            *   [Vertexaivectorsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/)
            *   [Vespa](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vespa/)
            *   [Weaviate](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/)
            *   [Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/wordlift/)
            *   [Zep](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/)
            
        
    *   [ ] 
        
        [Tools](https://docs.llamaindex.ai/en/stable/api_reference/tools/)
        
        Tools
        
        *   [Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/tools/arxiv/)
        *   [Azure code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/)
        *   [Azure cv](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/)
        *   [Azure speech](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/)
        *   [Azure translate](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/)
        *   [Bing search](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/)
        *   [Box](https://docs.llamaindex.ai/en/stable/api_reference/tools/box/)
        *   [Brave search](https://docs.llamaindex.ai/en/stable/api_reference/tools/brave_search/)
        *   [Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/tools/cassandra/)
        *   [Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/tools/chatgpt_plugin/)
        *   [Code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/code_interpreter/)
        *   [Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/tools/cogniswitch/)
        *   [Database](https://docs.llamaindex.ai/en/stable/api_reference/tools/database/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/tools/docker_code.md)
        *   [Duckduckgo](https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/)
        *   [Elevenlabs](https://docs.llamaindex.ai/en/stable/api_reference/tools/elevenlabs/)
        *   [Exa](https://docs.llamaindex.ai/en/stable/api_reference/tools/exa/)
        *   [Finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/)
        *   [Function](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/)
        *   [Graphql](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/)
        *   [Ionic shopping](https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/)
        *   [Jina](https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/)
        *   [Load and search](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/)
        *   [Metaphor](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/)
        *   [Multion](https://docs.llamaindex.ai/en/stable/api_reference/tools/multion/)
        *   [Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/)
        *   [Notion](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/)
        *   [Ondemand loader](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/)
        *   [Openapi](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/tools/oracleai.md)
        *   [Playgrounds](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/)
        *   [Python file](https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/)
        *   [Query engine](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_engine/)
        *   [Query plan](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/)
        *   [Requests](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/)
        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/tools/retriever/)
        *   [Salesforce](https://docs.llamaindex.ai/en/stable/api_reference/tools/salesforce/)
        *   [Scrapegraph](https://docs.llamaindex.ai/en/stable/api_reference/tools/scrapegraph/)
        *   [Shopify](https://docs.llamaindex.ai/en/stable/api_reference/tools/shopify/)
        *   [Slack](https://docs.llamaindex.ai/en/stable/api_reference/tools/slack/)
        *   [Tavily research](https://docs.llamaindex.ai/en/stable/api_reference/tools/tavily_research/)
        *   [Text to image](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/)
        *   [Tool spec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/)
        *   [Vectara query](https://docs.llamaindex.ai/en/stable/api_reference/tools/vectara_query/)
        *   [Vector db](https://docs.llamaindex.ai/en/stable/api_reference/tools/vector_db/)
        *   [Waii](https://docs.llamaindex.ai/en/stable/api_reference/tools/waii/)
        *   [Weather](https://docs.llamaindex.ai/en/stable/api_reference/tools/weather/)
        *   [Wikipedia](https://docs.llamaindex.ai/en/stable/api_reference/tools/wikipedia/)
        *   [Wolfram alpha](https://docs.llamaindex.ai/en/stable/api_reference/tools/wolfram_alpha/)
        *   [Yahoo finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/yahoo_finance/)
        *   [Yelp](https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/)
        *   [Zapier](https://docs.llamaindex.ai/en/stable/api_reference/tools/zapier/)
        
    *   [ ]  Workflow
        
        Workflow
        
        *   [Decorators](https://docs.llamaindex.ai/en/stable/api_reference/workflow/decorators/)
        *   [Context](https://docs.llamaindex.ai/en/stable/api_reference/workflow/context/)
        *   [Events](https://docs.llamaindex.ai/en/stable/api_reference/workflow/events/)
        *   [Retry policy](https://docs.llamaindex.ai/en/stable/api_reference/workflow/retry_policy/)
        *   [Workflow](https://docs.llamaindex.ai/en/stable/api_reference/workflow/workflow/)
        
    
*   [ ] 
    
    [Open-Source Community](https://docs.llamaindex.ai/en/stable/community/llama_packs/)
    
    Open-Source Community
    
    *   [Integrations](https://docs.llamaindex.ai/en/stable/community/integrations/)
    *   [Full Stack Projects](https://docs.llamaindex.ai/en/stable/community/full_stack_projects/)
    *   [ ]  Community FAQ
        
        Community FAQ
        
        *   [Chat Engines](https://docs.llamaindex.ai/en/stable/community/faq/chat_engines/)
        *   [Documents and Nodes](https://docs.llamaindex.ai/en/stable/community/faq/documents_and_nodes/)
        *   [Embeddings](https://docs.llamaindex.ai/en/stable/community/faq/embeddings/)
        *   [Large Language Models](https://docs.llamaindex.ai/en/stable/community/faq/llms/)
        *   [Query Engines](https://docs.llamaindex.ai/en/stable/community/faq/query_engines/)
        *   [Vector Database](https://docs.llamaindex.ai/en/stable/community/faq/vector_database/)
        
    *   [ ]  Contributing
        
        Contributing
        
        *   [Code](https://docs.llamaindex.ai/en/stable/CONTRIBUTING/)
        *   [Docs](https://docs.llamaindex.ai/en/stable/DOCS_README/)
        
    *   [Changelog](https://docs.llamaindex.ai/en/stable/CHANGELOG/)
    *   [Presentations](https://docs.llamaindex.ai/en/stable/presentations/past_presentations/)
    *   [Deprecated Terms](https://docs.llamaindex.ai/en/stable/changes/deprecated_terms/)
    
*   [ ] 
    
    [LlamaCloud](https://docs.llamaindex.ai/en/stable/llama_cloud/)
    
    LlamaCloud
    
    *   [LlamaParse](https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/)
    

Table of contents

*   [Overview](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#overview)
*   [Cookbook](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#cookbook)
*   [Setup](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#setup)
*   [1\. Chain Together Prompt and LLM](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-chain-together-prompt-and-llm)
    
    *   [View Intermediate Inputs/Outputs](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#view-intermediate-inputsoutputs)
    *   [Try Output Parsing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#try-output-parsing)
    *   [Streaming Support](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#streaming-support)
    
*   [Chain Together Query Rewriting Workflow (prompts + LLM) with Retrieval](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#chain-together-query-rewriting-workflow-prompts-llm-with-retrieval)
*   [Create a Full RAG Pipeline as a DAG](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#create-a-full-rag-pipeline-as-a-dag)
    
    *   [1\. RAG Pipeline with Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-rag-pipeline-with-query-rewriting)
    *   [2\. RAG Pipeline without Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#2-rag-pipeline-without-query-rewriting)
    
*   [Defining a Custom Component in a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#defining-a-custom-component-in-a-query-pipeline)
*   [Stepwise Execution of a Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#stepwise-execution-of-a-pipeline)

       

An Introduction to LlamaIndex Query Pipelines[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#an-introduction-to-llamaindex-query-pipelines)
======================================================================================================================================================================

Overview[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#overview)
--------------------------------------------------------------------------------------------

LlamaIndex provides a declarative query API that allows you to chain together different modules in order to orchestrate simple-to-advanced workflows over your data.

This is centered around our `QueryPipeline` abstraction. Load in a variety of modules (from LLMs to prompts to retrievers to other pipelines), connect them all together into a sequential chain or DAG, and run it end2end.

**NOTE**: You can orchestrate all these workflows without the declarative pipeline abstraction (by using the modules imperatively and writing your own functions). So what are the advantages of `QueryPipeline`?

*   Express common workflows with fewer lines of code/boilerplate
*   Greater readability
*   Greater parity / better integration points with common low-code / no-code solutions (e.g. LangFlow)
*   \[In the future\] A declarative interface allows easy serializability of pipeline components, providing portability of pipelines/easier deployment to different systems.

Cookbook[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#cookbook)
--------------------------------------------------------------------------------------------

In this cookbook we give you an introduction to our `QueryPipeline` interface and show you some basic workflows you can tackle.

*   Chain together prompt and LLM
*   Chain together query rewriting (prompt + LLM) with retrieval
*   Chain together a full RAG query pipeline (query rewriting, retrieval, reranking, response synthesis)
*   Setting up a custom query component
*   Executing a pipeline step-by-step

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#setup)
--------------------------------------------------------------------------------------

Here we setup some data + indexes (from PG's essay) that we'll be using in the rest of the cookbook.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-postprocessor\-cohere\-rerank
%pip install llama\-index\-llms\-openai

%pip install llama-index-embeddings-openai %pip install llama-index-postprocessor-cohere-rerank %pip install llama-index-llms-openai

In \[ \]:

Copied!

\# setup Arize Phoenix for logging/observability
import phoenix as px

px.launch\_app()
import llama\_index.core

llama\_index.core.set\_global\_handler("arize\_phoenix")

\# setup Arize Phoenix for logging/observability import phoenix as px px.launch\_app() import llama\_index.core llama\_index.core.set\_global\_handler("arize\_phoenix")

🌍 To view the Phoenix app in your browser, visit http://127.0.0.1:6006/
📺 To view the Phoenix app in a notebook, run \`px.active\_session().view()\`
📖 For more information on how to use Phoenix, check out https://docs.arize.com/phoenix

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small")

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

reader \= SimpleDirectoryReader("../data/paul\_graham")

from llama\_index.core import SimpleDirectoryReader reader = SimpleDirectoryReader("../data/paul\_graham")

In \[ \]:

Copied!

docs \= reader.load\_data()

docs = reader.load\_data()

In \[ \]:

Copied!

import os
from llama\_index.core import (
    StorageContext,
    VectorStoreIndex,
    load\_index\_from\_storage,
)

if not os.path.exists("storage"):
    index \= VectorStoreIndex.from\_documents(docs)
    \# save index to disk
    index.set\_index\_id("vector\_index")
    index.storage\_context.persist("./storage")
else:
    \# rebuild storage context
    storage\_context \= StorageContext.from\_defaults(persist\_dir\="storage")
    \# load index
    index \= load\_index\_from\_storage(storage\_context, index\_id\="vector\_index")

import os from llama\_index.core import ( StorageContext, VectorStoreIndex, load\_index\_from\_storage, ) if not os.path.exists("storage"): index = VectorStoreIndex.from\_documents(docs) # save index to disk index.set\_index\_id("vector\_index") index.storage\_context.persist("./storage") else: # rebuild storage context storage\_context = StorageContext.from\_defaults(persist\_dir="storage") # load index index = load\_index\_from\_storage(storage\_context, index\_id="vector\_index")

1\. Chain Together Prompt and LLM[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-chain-together-prompt-and-llm)
--------------------------------------------------------------------------------------------------------------------------------------------

In this section we show a super simple workflow of chaining together a prompt with LLM.

We simply define `chain` on initialization. This is a special case of a query pipeline where the components are purely sequential, and we automatically convert outputs into the right format for the next inputs.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import QueryPipeline
from llama\_index.core import PromptTemplate

\# try chaining basic prompts
prompt\_str \= "Please generate related movies to {movie\_name}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
llm \= OpenAI(model\="gpt-3.5-turbo")

p \= QueryPipeline(chain\=\[prompt\_tmpl, llm\], verbose\=True)

from llama\_index.core.query\_pipeline import QueryPipeline from llama\_index.core import PromptTemplate # try chaining basic prompts prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) llm = OpenAI(model="gpt-3.5-turbo") p = QueryPipeline(chain=\[prompt\_tmpl, llm\], verbose=True)

In \[ \]:

Copied!

output \= p.run(movie\_name\="The Departed")

output = p.run(movie\_name="The Departed")

\> Running module 8dc57d24-9691-4d8d-87d7-151865a7cd1b with input: 
movie\_name: The Departed

\> Running module 7ed9e26c-a704-4b0b-9cfd-991266e754c0 with input: 
messages: Please generate related movies to The Departed

In \[ \]:

Copied!

print(str(output))

print(str(output))

assistant: 1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed
2. The Town (2010) - A crime thriller directed by and starring Ben Affleck
3. Mystic River (2003) - A crime drama directed by Clint Eastwood
4. Goodfellas (1990) - A classic mobster film directed by Martin Scorsese
5. The Irishman (2019) - Another crime drama directed by Martin Scorsese, starring Robert De Niro and Al Pacino
6. The Departed (2006) - The Departed is a 2006 American crime film directed by Martin Scorsese and written by William Monahan. It is a remake of the 2002 Hong Kong film Infernal Affairs. The film stars Leonardo DiCaprio, Matt Damon, Jack Nicholson, and Mark Wahlberg, with Martin Sheen, Ray Winstone, Vera Farmiga, and Alec Baldwin in supporting roles.

### View Intermediate Inputs/Outputs[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#view-intermediate-inputsoutputs)

For debugging and other purposes, we can also view the inputs and outputs at each step.

In \[ \]:

Copied!

output, intermediates \= p.run\_with\_intermediates(movie\_name\="The Departed")

output, intermediates = p.run\_with\_intermediates(movie\_name="The Departed")

\> Running module 8dc57d24-9691-4d8d-87d7-151865a7cd1b with input: 
movie\_name: The Departed

\> Running module 7ed9e26c-a704-4b0b-9cfd-991266e754c0 with input: 
messages: Please generate related movies to The Departed

In \[ \]:

Copied!

intermediates\["8dc57d24-9691-4d8d-87d7-151865a7cd1b"\]

intermediates\["8dc57d24-9691-4d8d-87d7-151865a7cd1b"\]

Out\[ \]:

ComponentIntermediates(inputs={'movie\_name': 'The Departed'}, outputs={'prompt': 'Please generate related movies to The Departed'})

In \[ \]:

Copied!

intermediates\["7ed9e26c-a704-4b0b-9cfd-991266e754c0"\]

intermediates\["7ed9e26c-a704-4b0b-9cfd-991266e754c0"\]

Out\[ \]:

ComponentIntermediates(inputs={'messages': 'Please generate related movies to The Departed'}, outputs={'output': ChatResponse(message=ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'\>, content='1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\\n2. The Town (2010) - A crime thriller directed by Ben Affleck\\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\\n4. Goodfellas (1990) - A classic crime film directed by Martin Scorsese\\n5. The Irishman (2019) - Another crime film directed by Martin Scorsese, starring Robert De Niro and Al Pacino\\n6. The Godfather (1972) - A classic crime film directed by Francis Ford Coppola\\n7. Heat (1995) - A crime thriller directed by Michael Mann, starring Al Pacino and Robert De Niro\\n8. The Departed (2006) - A crime thriller directed by Martin Scorsese, starring Leonardo DiCaprio and Matt Damon.', additional\_kwargs={}), raw={'id': 'chatcmpl-9EKf2nZ4latFJvHy0gzOUZbaB8xwY', 'choices': \[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\\n2. The Town (2010) - A crime thriller directed by Ben Affleck\\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\\n4. Goodfellas (1990) - A classic crime film directed by Martin Scorsese\\n5. The Irishman (2019) - Another crime film directed by Martin Scorsese, starring Robert De Niro and Al Pacino\\n6. The Godfather (1972) - A classic crime film directed by Francis Ford Coppola\\n7. Heat (1995) - A crime thriller directed by Michael Mann, starring Al Pacino and Robert De Niro\\n8. The Departed (2006) - A crime thriller directed by Martin Scorsese, starring Leonardo DiCaprio and Matt Damon.', role='assistant', function\_call=None, tool\_calls=None))\], 'created': 1713203040, 'model': 'gpt-3.5-turbo-0125', 'object': 'chat.completion', 'system\_fingerprint': 'fp\_c2295e73ad', 'usage': CompletionUsage(completion\_tokens=184, prompt\_tokens=15, total\_tokens=199)}, delta=None, logprobs=None, additional\_kwargs={})})

### Try Output Parsing[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#try-output-parsing)

Let's parse the outputs into a structured Pydantic object.

In \[ \]:

Copied!

from typing import List
from pydantic import BaseModel, Field
from llama\_index.core.output\_parsers import PydanticOutputParser

class Movie(BaseModel):
    """Object representing a single movie."""

    name: str \= Field(..., description\="Name of the movie.")
    year: int \= Field(..., description\="Year of the movie.")

class Movies(BaseModel):
    """Object representing a list of movies."""

    movies: List\[Movie\] \= Field(..., description\="List of movies.")

llm \= OpenAI(model\="gpt-3.5-turbo")
output\_parser \= PydanticOutputParser(Movies)
json\_prompt\_str \= """\\
Please generate related movies to {movie\_name}. Output with the following JSON format: 
"""
json\_prompt\_str \= output\_parser.format(json\_prompt\_str)

from typing import List from pydantic import BaseModel, Field from llama\_index.core.output\_parsers import PydanticOutputParser class Movie(BaseModel): """Object representing a single movie.""" name: str = Field(..., description="Name of the movie.") year: int = Field(..., description="Year of the movie.") class Movies(BaseModel): """Object representing a list of movies.""" movies: List\[Movie\] = Field(..., description="List of movies.") llm = OpenAI(model="gpt-3.5-turbo") output\_parser = PydanticOutputParser(Movies) json\_prompt\_str = """\\ Please generate related movies to {movie\_name}. Output with the following JSON format: """ json\_prompt\_str = output\_parser.format(json\_prompt\_str)

In \[ \]:

Copied!

\# add JSON spec to prompt template
json\_prompt\_tmpl \= PromptTemplate(json\_prompt\_str)

p \= QueryPipeline(chain\=\[json\_prompt\_tmpl, llm, output\_parser\], verbose\=True)
output \= p.run(movie\_name\="Toy Story")

\# add JSON spec to prompt template json\_prompt\_tmpl = PromptTemplate(json\_prompt\_str) p = QueryPipeline(chain=\[json\_prompt\_tmpl, llm, output\_parser\], verbose=True) output = p.run(movie\_name="Toy Story")

\> Running module 2e4093c5-ae62-420a-be91-9c28c057bada with input: 
movie\_name: Toy Story

\> Running module 3b41f95c-f54b-41d7-8ef0-8e45b5d7eeb0 with input: 
messages: Please generate related movies to Toy Story. Output with the following JSON format: 



Here's a JSON schema to follow:
{"title": "Movies", "description": "Object representing a list of movies.", "typ...

\> Running module 27e79a16-72de-4ce2-8b2e-94932c4069c3 with input: 
input: assistant: {
  "movies": \[
    {
      "name": "Finding Nemo",
      "year": 2003
    },
    {
      "name": "Monsters, Inc.",
      "year": 2001
    },
    {
      "name": "Cars",
      "year": 2006
...

In \[ \]:

Copied!

output

output

Out\[ \]:

Movies(movies=\[Movie(name='Finding Nemo', year=2003), Movie(name='Monsters, Inc.', year=2001), Movie(name='Cars', year=2006), Movie(name='The Incredibles', year=2004), Movie(name='Ratatouille', year=2007)\])

### Streaming Support[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#streaming-support)

The query pipelines have LLM streaming support (simply do `as_query_component(streaming=True)`). Intermediate outputs will get autoconverted, and the final output can be a streaming output. Here's some examples.

**1\. Chain multiple Prompts with Streaming**

In \[ \]:

Copied!

prompt\_str \= "Please generate related movies to {movie\_name}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
\# let's add some subsequent prompts for fun
prompt\_str2 \= """\\
Here's some text:

{text}

Can you rewrite this with a summary of each movie?
"""
prompt\_tmpl2 \= PromptTemplate(prompt\_str2)
llm \= OpenAI(model\="gpt-3.5-turbo")
llm\_c \= llm.as\_query\_component(streaming\=True)

p \= QueryPipeline(
    chain\=\[prompt\_tmpl, llm\_c, prompt\_tmpl2, llm\_c\], verbose\=True
)
\# p = QueryPipeline(chain=\[prompt\_tmpl, llm\_c\], verbose=True)

prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) # let's add some subsequent prompts for fun prompt\_str2 = """\\ Here's some text: {text} Can you rewrite this with a summary of each movie? """ prompt\_tmpl2 = PromptTemplate(prompt\_str2) llm = OpenAI(model="gpt-3.5-turbo") llm\_c = llm.as\_query\_component(streaming=True) p = QueryPipeline( chain=\[prompt\_tmpl, llm\_c, prompt\_tmpl2, llm\_c\], verbose=True ) # p = QueryPipeline(chain=\[prompt\_tmpl, llm\_c\], verbose=True)

In \[ \]:

Copied!

output \= p.run(movie\_name\="The Dark Knight")
for o in output:
    print(o.delta, end\="")

output = p.run(movie\_name="The Dark Knight") for o in output: print(o.delta, end="")

\> Running module 213af6d4-3450-46af-9087-b80656ae6951 with input: 
movie\_name: The Dark Knight

\> Running module 3ff7e987-f5f3-4b36-a3e1-be5a4821d9d9 with input: 
messages: Please generate related movies to The Dark Knight

\> Running module a2841bd3-c833-4427-9a7e-83b19872b064 with input: 
text: <generator object llm\_chat\_callback.<locals\>.wrap.<locals\>.wrapped\_llm\_chat.<locals\>.wrapped\_gen at 0x298d338b0\>

\> Running module c7e0a454-213a-460e-b029-f2d42fd7d938 with input: 
messages: Here's some text:

1. Batman Begins (2005)
2. The Dark Knight Rises (2012)
3. Batman v Superman: Dawn of Justice (2016)
4. Man of Steel (2013)
5. The Avengers (2012)
6. Iron Man (2008)
7. Captain Amer...

1\. Batman Begins (2005): A young Bruce Wayne becomes Batman to fight crime in Gotham City, facing his fears and training under the guidance of Ra's al Ghul.
2. The Dark Knight Rises (2012): Batman returns to protect Gotham City from the ruthless terrorist Bane, who plans to destroy the city and its symbol of hope.
3. Batman v Superman: Dawn of Justice (2016): Batman and Superman clash as their ideologies collide, leading to an epic battle while a new threat emerges that threatens humanity.
4. Man of Steel (2013): The origin story of Superman, as he embraces his powers and faces General Zod, a fellow Kryptonian seeking to destroy Earth.
5. The Avengers (2012): Earth's mightiest heroes, including Iron Man, Captain America, Thor, and Hulk, join forces to stop Loki and his alien army from conquering the world.
6. Iron Man (2008): Billionaire Tony Stark builds a high-tech suit to escape captivity and becomes the superhero Iron Man, using his technology to fight against evil.
7. Captain America: The Winter Soldier (2014): Captain America teams up with Black Widow and Falcon to uncover a conspiracy within S.H.I.E.L.D. while facing a deadly assassin known as the Winter Soldier.
8. The Amazing Spider-Man (2012): Peter Parker, a high school student bitten by a radioactive spider, becomes Spider-Man and battles the Lizard, a monstrous villain threatening New York City.
9. Watchmen (2009): Set in an alternate reality, a group of retired vigilantes investigates the murder of one of their own, uncovering a conspiracy that could have catastrophic consequences.
10. Sin City (2005): A neo-noir anthology film set in the crime-ridden city of Basin City, following various characters as they navigate through corruption, violence, and redemption.
11. V for Vendetta (2005): In a dystopian future, a masked vigilante known as V fights against a totalitarian government, inspiring the people to rise up and reclaim their freedom.
12. Blade Runner 2049 (2017): A young blade runner uncovers a long-buried secret that leads him to seek out former blade runner Rick Deckard, while unraveling the mysteries of a future society.
13. Inception (2010): A skilled thief enters people's dreams to steal information, but is tasked with planting an idea instead, leading to a mind-bending journey through multiple layers of reality.
14. The Matrix (1999): A computer hacker discovers the truth about reality, joining a group of rebels fighting against sentient machines that have enslaved humanity in a simulated world.
15. The Crow (1994): A musician, resurrected by a supernatural crow, seeks vengeance against the gang that murdered him and his fiancée, unleashing a dark and atmospheric tale of revenge.

**2\. Feed streaming output to output parser**

In \[ \]:

Copied!

p \= QueryPipeline(
    chain\=\[
        json\_prompt\_tmpl,
        llm.as\_query\_component(streaming\=True),
        output\_parser,
    \],
    verbose\=True,
)
output \= p.run(movie\_name\="Toy Story")
print(output)

p = QueryPipeline( chain=\[ json\_prompt\_tmpl, llm.as\_query\_component(streaming=True), output\_parser, \], verbose=True, ) output = p.run(movie\_name="Toy Story") print(output)

\> Running module fe1dbf6a-56e0-44bf-97d7-a2a1fe9d9b8c with input: 
movie\_name: Toy Story

\> Running module a8eaaf91-df9d-46c4-bbae-06c15cd15123 with input: 
messages: Please generate related movies to Toy Story. Output with the following JSON format: 



Here's a JSON schema to follow:
{"title": "Movies", "description": "Object representing a list of movies.", "typ...

\> Running module fcbc0b09-0ef5-43e0-b007-c4508fd6742f with input: 
input: <generator object llm\_chat\_callback.<locals\>.wrap.<locals\>.wrapped\_llm\_chat.<locals\>.wrapped\_gen at 0x298d32dc0\>

movies=\[Movie(name='Finding Nemo', year=2003), Movie(name='Monsters, Inc.', year=2001), Movie(name='The Incredibles', year=2004), Movie(name='Cars', year=2006), Movie(name='Ratatouille', year=2007)\]

Chain Together Query Rewriting Workflow (prompts + LLM) with Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#chain-together-query-rewriting-workflow-prompts-llm-with-retrieval)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we try a slightly more complex workflow where we send the input through two prompts before initiating retrieval.

1.  Generate question about given topic.
2.  Hallucinate answer given question, for better retrieval.

Since each prompt only takes in one input, note that the `QueryPipeline` will automatically chain LLM outputs into the prompt and then into the LLM.

You'll see how to define links more explicitly in the next section.

In \[ \]:

Copied!

\# !pip install llama-index-postprocessor-cohere-rerank

\# !pip install llama-index-postprocessor-cohere-rerank

In \[ \]:

Copied!

from llama\_index.postprocessor.cohere\_rerank import CohereRerank

\# generate question regarding topic
prompt\_str1 \= "Please generate a concise question about Paul Graham's life regarding the following topic {topic}"
prompt\_tmpl1 \= PromptTemplate(prompt\_str1)
\# use HyDE to hallucinate answer.
prompt\_str2 \= (
    "Please write a passage to answer the question\\n"
    "Try to include as many key details as possible.\\n"
    "\\n"
    "\\n"
    "{query\_str}\\n"
    "\\n"
    "\\n"
    'Passage:"""\\n'
)
prompt\_tmpl2 \= PromptTemplate(prompt\_str2)

llm \= OpenAI(model\="gpt-3.5-turbo")
retriever \= index.as\_retriever(similarity\_top\_k\=5)
p \= QueryPipeline(
    chain\=\[prompt\_tmpl1, llm, prompt\_tmpl2, llm, retriever\], verbose\=True
)

from llama\_index.postprocessor.cohere\_rerank import CohereRerank # generate question regarding topic prompt\_str1 = "Please generate a concise question about Paul Graham's life regarding the following topic {topic}" prompt\_tmpl1 = PromptTemplate(prompt\_str1) # use HyDE to hallucinate answer. prompt\_str2 = ( "Please write a passage to answer the question\\n" "Try to include as many key details as possible.\\n" "\\n" "\\n" "{query\_str}\\n" "\\n" "\\n" 'Passage:"""\\n' ) prompt\_tmpl2 = PromptTemplate(prompt\_str2) llm = OpenAI(model="gpt-3.5-turbo") retriever = index.as\_retriever(similarity\_top\_k=5) p = QueryPipeline( chain=\[prompt\_tmpl1, llm, prompt\_tmpl2, llm, retriever\], verbose=True )

In \[ \]:

Copied!

nodes \= p.run(topic\="college")
len(nodes)

nodes = p.run(topic="college") len(nodes)

\> Running module f5435516-61b6-49e9-9926-220cfb6443bd with input: 
topic: college

\> Running module 1dcaa097-cedc-4466-81bb-f8fd8768762b with input: 
messages: Please generate a concise question about Paul Graham's life regarding the following topic college

\> Running module 891afa10-5fe0-47ed-bdee-42a59d0e916d with input: 
query\_str: assistant: How did Paul Graham's college experience shape his career and entrepreneurial mindset?

\> Running module 5bcd9964-b972-41a9-960d-96894c57a372 with input: 
messages: Please write a passage to answer the question
Try to include as many key details as possible.


How did Paul Graham's college experience shape his career and entrepreneurial mindset?


Passage:"""

\> Running module 0b81a91a-2c90-4700-8ba1-25ffad5311fd with input: 
input: assistant: Paul Graham's college experience played a pivotal role in shaping his career and entrepreneurial mindset. As a student at Cornell University, Graham immersed himself in the world of compute...

Out\[ \]:

5

Create a Full RAG Pipeline as a DAG[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#create-a-full-rag-pipeline-as-a-dag)
--------------------------------------------------------------------------------------------------------------------------------------------------

Here we chain together a full RAG pipeline consisting of query rewriting, retrieval, reranking, and response synthesis.

Here we can't use `chain` syntax because certain modules depend on multiple inputs (for instance, response synthesis expects both the retrieved nodes and the original question). Instead we'll construct a DAG explicitly, through `add_modules` and then `add_link`.

### 1\. RAG Pipeline with Query Rewriting[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-rag-pipeline-with-query-rewriting)

We use an LLM to rewrite the query first before passing it to our downstream modules - retrieval/reranking/synthesis.

In \[ \]:

Copied!

from llama\_index.postprocessor.cohere\_rerank import CohereRerank
from llama\_index.core.response\_synthesizers import TreeSummarize

\# define modules
prompt\_str \= "Please generate a question about Paul Graham's life regarding the following topic {topic}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
llm \= OpenAI(model\="gpt-3.5-turbo")
retriever \= index.as\_retriever(similarity\_top\_k\=3)
reranker \= CohereRerank()
summarizer \= TreeSummarize(llm\=llm)

from llama\_index.postprocessor.cohere\_rerank import CohereRerank from llama\_index.core.response\_synthesizers import TreeSummarize # define modules prompt\_str = "Please generate a question about Paul Graham's life regarding the following topic {topic}" prompt\_tmpl = PromptTemplate(prompt\_str) llm = OpenAI(model="gpt-3.5-turbo") retriever = index.as\_retriever(similarity\_top\_k=3) reranker = CohereRerank() summarizer = TreeSummarize(llm=llm)

In \[ \]:

Copied!

\# define query pipeline
p \= QueryPipeline(verbose\=True)
p.add\_modules(
    {
        "llm": llm,
        "prompt\_tmpl": prompt\_tmpl,
        "retriever": retriever,
        "summarizer": summarizer,
        "reranker": reranker,
    }
)

\# define query pipeline p = QueryPipeline(verbose=True) p.add\_modules( { "llm": llm, "prompt\_tmpl": prompt\_tmpl, "retriever": retriever, "summarizer": summarizer, "reranker": reranker, } )

Next we draw links between modules with `add_link`. `add_link` takes in the source/destination module ids, and optionally the `source_key` and `dest_key`. Specify the `source_key` or `dest_key` if there are multiple outputs/inputs respectively.

You can view the set of input/output keys for each module through `module.as_query_component().input_keys` and `module.as_query_component().output_keys`.

Here we explicitly specify `dest_key` for the `reranker` and `summarizer` modules because they take in two inputs (query\_str and nodes).

In \[ \]:

Copied!

p.add\_link("prompt\_tmpl", "llm")
p.add\_link("llm", "retriever")
p.add\_link("retriever", "reranker", dest\_key\="nodes")
p.add\_link("llm", "reranker", dest\_key\="query\_str")
p.add\_link("reranker", "summarizer", dest\_key\="nodes")
p.add\_link("llm", "summarizer", dest\_key\="query\_str")

\# look at summarizer input keys
print(summarizer.as\_query\_component().input\_keys)

p.add\_link("prompt\_tmpl", "llm") p.add\_link("llm", "retriever") p.add\_link("retriever", "reranker", dest\_key="nodes") p.add\_link("llm", "reranker", dest\_key="query\_str") p.add\_link("reranker", "summarizer", dest\_key="nodes") p.add\_link("llm", "summarizer", dest\_key="query\_str") # look at summarizer input keys print(summarizer.as\_query\_component().input\_keys)

required\_keys={'query\_str', 'nodes'} optional\_keys=set()

We use `networkx` to store the graph representation. This gives us an easy way to view the DAG!

In \[ \]:

Copied!

\## create graph
from pyvis.network import Network

net \= Network(notebook\=True, cdn\_resources\="in\_line", directed\=True)
net.from\_nx(p.dag)
net.show("rag\_dag.html")

\## another option using \`pygraphviz\`
\# from networkx.drawing.nx\_agraph import to\_agraph
\# from IPython.display import Image
\# agraph = to\_agraph(p.dag)
\# agraph.layout(prog="dot")
\# agraph.draw('rag\_dag.png')
\# display(Image('rag\_dag.png'))

\## create graph from pyvis.network import Network net = Network(notebook=True, cdn\_resources="in\_line", directed=True) net.from\_nx(p.dag) net.show("rag\_dag.html") ## another option using \`pygraphviz\` # from networkx.drawing.nx\_agraph import to\_agraph # from IPython.display import Image # agraph = to\_agraph(p.dag) # agraph.layout(prog="dot") # agraph.draw('rag\_dag.png') # display(Image('rag\_dag.png'))

rag\_dag.html

Out\[ \]:

In \[ \]:

Copied!

response \= p.run(topic\="YC")

response = p.run(topic="YC")

\> Running module prompt\_tmpl with input: 
topic: YC

\> Running module llm with input: 
messages: Please generate a question about Paul Graham's life regarding the following topic YC

\> Running module retriever with input: 
input: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?

\> Running module reranker with input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='ccd39041-5a64-4bd3-aca7-48f804b5a23f', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

\> Running module summarizer with input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='120574dd-a5c9-4985-ab3e-37b1070b500a', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

In \[ \]:

Copied!

print(str(response))

print(str(response))

Paul Graham played a significant role in the founding and development of Y Combinator (YC). He was one of the co-founders of YC and provided the initial funding for the investment firm. Along with his partners, he implemented the ideas they had been discussing and started their own investment firm. Paul Graham also played a key role in shaping the unique batch model of YC, where a group of startups is funded and provided intensive support for a period of three months. He was actively involved in selecting and helping the founders, and he also wrote essays and worked on YC's internal software.

In \[ \]:

Copied!

\# you can do async too
response \= await p.arun(topic\="YC")
print(str(response))

\# you can do async too response = await p.arun(topic="YC") print(str(response))

\> Running modules and inputs in parallel: 
Module key: prompt\_tmpl. Input: 
topic: YC

\> Running modules and inputs in parallel: 
Module key: llm. Input: 
messages: Please generate a question about Paul Graham's life regarding the following topic YC

\> Running modules and inputs in parallel: 
Module key: retriever. Input: 
input: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?

\> Running modules and inputs in parallel: 
Module key: reranker. Input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='ccd39041-5a64-4bd3-aca7-48f804b5a23f', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

\> Running modules and inputs in parallel: 
Module key: summarizer. Input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='120574dd-a5c9-4985-ab3e-37b1070b500a', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

Paul Graham played a significant role in the founding and development of Y Combinator (YC). He was one of the co-founders of YC and provided the initial funding for the investment firm. Along with his partners, he implemented the ideas they had been discussing and decided to start their own investment firm. Paul Graham also played a key role in shaping the unique batch model of YC, where a group of startups is funded and provided intensive support for a period of three months. He was actively involved in selecting and helping the founders and worked on various projects related to YC, including writing essays and developing internal software.

### 2\. RAG Pipeline without Query Rewriting[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#2-rag-pipeline-without-query-rewriting)

Here we setup a RAG pipeline without the query rewriting step.

Here we need a way to link the input query to both the retriever, reranker, and summarizer. We can do this by defining a special `InputComponent`, allowing us to link the inputs to multiple downstream modules.

In \[ \]:

Copied!

from llama\_index.postprocessor.cohere\_rerank import CohereRerank
from llama\_index.core.response\_synthesizers import TreeSummarize
from llama\_index.core.query\_pipeline import InputComponent

retriever \= index.as\_retriever(similarity\_top\_k\=5)
summarizer \= TreeSummarize(llm\=OpenAI(model\="gpt-3.5-turbo"))
reranker \= CohereRerank()

from llama\_index.postprocessor.cohere\_rerank import CohereRerank from llama\_index.core.response\_synthesizers import TreeSummarize from llama\_index.core.query\_pipeline import InputComponent retriever = index.as\_retriever(similarity\_top\_k=5) summarizer = TreeSummarize(llm=OpenAI(model="gpt-3.5-turbo")) reranker = CohereRerank()

In \[ \]:

Copied!

p \= QueryPipeline(verbose\=True)
p.add\_modules(
    {
        "input": InputComponent(),
        "retriever": retriever,
        "summarizer": summarizer,
    }
)
p.add\_link("input", "retriever")
p.add\_link("input", "summarizer", dest\_key\="query\_str")
p.add\_link("retriever", "summarizer", dest\_key\="nodes")

p = QueryPipeline(verbose=True) p.add\_modules( { "input": InputComponent(), "retriever": retriever, "summarizer": summarizer, } ) p.add\_link("input", "retriever") p.add\_link("input", "summarizer", dest\_key="query\_str") p.add\_link("retriever", "summarizer", dest\_key="nodes")

In \[ \]:

Copied!

output \= p.run(input\="what did the author do in YC")

output = p.run(input="what did the author do in YC")

\> Running module input with input: 
input: what did the author do in YC

\> Running module retriever with input: 
input: what did the author do in YC

\> Running module summarizer with input: 
query\_str: what did the author do in YC
nodes: \[NodeWithScore(node=TextNode(id\_='86dea730-ca35-4bcb-9f9b-4c99e8eadd08', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

In \[ \]:

Copied!

print(str(output))

print(str(output))

The author worked on various projects at YC, including writing essays and working on YC's internal software. They also played a key role in the creation and operation of YC by funding the program with their own money and organizing a batch model where they would fund a group of startups twice a year. They provided support and guidance to the startups during a three-month intensive program and used their building in Cambridge as the headquarters for YC. Additionally, they hosted weekly dinners where experts on startups would give talks.

Defining a Custom Component in a Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#defining-a-custom-component-in-a-query-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can easily define a custom component. Simply subclass a `QueryComponent`, implement validation/run functions + some helpers, and plug it in.

Let's wrap the related movie generation prompt+LLM chain from the first example into a custom component.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import (
    CustomQueryComponent,
    InputKeys,
    OutputKeys,
)
from typing import Dict, Any
from llama\_index.core.llms.llm import LLM
from pydantic import Field

class RelatedMovieComponent(CustomQueryComponent):
    """Related movie component."""

    llm: LLM \= Field(..., description\="OpenAI LLM")

    def \_validate\_component\_inputs(
        self, input: Dict\[str, Any\]
    ) \-\> Dict\[str, Any\]:
        """Validate component inputs during run\_component."""
        \# NOTE: this is OPTIONAL but we show you here how to do validation as an example
        return input

    @property
    def \_input\_keys(self) \-\> set:
        """Input keys dict."""
        \# NOTE: These are required inputs. If you have optional inputs please override
        \# \`optional\_input\_keys\_dict\`
        return {"movie"}

    @property
    def \_output\_keys(self) \-\> set:
        return {"output"}

    def \_run\_component(self, \*\*kwargs) \-\> Dict\[str, Any\]:
        """Run the component."""
        \# use QueryPipeline itself here for convenience
        prompt\_str \= "Please generate related movies to {movie\_name}"
        prompt\_tmpl \= PromptTemplate(prompt\_str)
        p \= QueryPipeline(chain\=\[prompt\_tmpl, llm\])
        return {"output": p.run(movie\_name\=kwargs\["movie"\])}

from llama\_index.core.query\_pipeline import ( CustomQueryComponent, InputKeys, OutputKeys, ) from typing import Dict, Any from llama\_index.core.llms.llm import LLM from pydantic import Field class RelatedMovieComponent(CustomQueryComponent): """Related movie component.""" llm: LLM = Field(..., description="OpenAI LLM") def \_validate\_component\_inputs( self, input: Dict\[str, Any\] ) -\> Dict\[str, Any\]: """Validate component inputs during run\_component.""" # NOTE: this is OPTIONAL but we show you here how to do validation as an example return input @property def \_input\_keys(self) -\> set: """Input keys dict.""" # NOTE: These are required inputs. If you have optional inputs please override # \`optional\_input\_keys\_dict\` return {"movie"} @property def \_output\_keys(self) -\> set: return {"output"} def \_run\_component(self, \*\*kwargs) -\> Dict\[str, Any\]: """Run the component.""" # use QueryPipeline itself here for convenience prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) p = QueryPipeline(chain=\[prompt\_tmpl, llm\]) return {"output": p.run(movie\_name=kwargs\["movie"\])}

Let's try the custom component out! We'll also add a step to convert the output to Shakespeare.

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo")
component \= RelatedMovieComponent(llm\=llm)

\# let's add some subsequent prompts for fun
prompt\_str \= """\\
Here's some text:

{text}

Can you rewrite this in the voice of Shakespeare?
"""
prompt\_tmpl \= PromptTemplate(prompt\_str)

p \= QueryPipeline(chain\=\[component, prompt\_tmpl, llm\], verbose\=True)

llm = OpenAI(model="gpt-3.5-turbo") component = RelatedMovieComponent(llm=llm) # let's add some subsequent prompts for fun prompt\_str = """\\ Here's some text: {text} Can you rewrite this in the voice of Shakespeare? """ prompt\_tmpl = PromptTemplate(prompt\_str) p = QueryPipeline(chain=\[component, prompt\_tmpl, llm\], verbose=True)

In \[ \]:

Copied!

output \= p.run(movie\="Love Actually")

output = p.run(movie="Love Actually")

\> Running module 31ca224a-f226-4956-882b-73878843d869 with input: 
movie: Love Actually

\> Running module febb41b5-2528-416a-bde7-6accdb0f9c51 with input: 
text: assistant: 1. "Valentine's Day" (2010)
2. "New Year's Eve" (2011)
3. "The Holiday" (2006)
4. "Crazy, Stupid, Love" (2011)
5. "Notting Hill" (1999)
6. "Four Weddings and a Funeral" (1994)
7. "Bridget J...

\> Running module e834ffbe-e97c-4ab0-9726-24f1534745b2 with input: 
messages: Here's some text:

1. "Valentine's Day" (2010)
2. "New Year's Eve" (2011)
3. "The Holiday" (2006)
4. "Crazy, Stupid, Love" (2011)
5. "Notting Hill" (1999)
6. "Four Weddings and a Funeral" (1994)
7. "B...

In \[ \]:

Copied!

print(str(output))

print(str(output))

assistant: 1. "Valentine's Day" (2010) - "A day of love, where hearts entwine, 
   And Cupid's arrow finds its mark divine."

2. "New Year's Eve" (2011) - "When old year fades, and new year dawns,
   We gather 'round, to celebrate the morns."

3. "The Holiday" (2006) - "Two souls, adrift in search of cheer,
   Find solace in a holiday so dear."

4. "Crazy, Stupid, Love" (2011) - "A tale of love, both wild and mad,
   Where hearts are lost, then found, and glad."

5. "Notting Hill" (1999) - "In London town, where love may bloom,
   A humble man finds love, and breaks the gloom."

6. "Four Weddings and a Funeral" (1994) - "Four times the vows, and one time mourn,
   Love's journey, with laughter and tears adorned."

7. "Bridget Jones's Diary" (2001) - "A maiden fair, with wit and charm,
   Records her life, and love's alarm."

8. "About Time" (2013) - "A tale of time, where love transcends,
   And moments cherished, never truly ends."

9. "The Best Exotic Marigold Hotel" (2011) - "In India's land, where dreams unfold,
   A hotel blooms, where hearts find gold."

10. "The Notebook" (2004) - "A love that spans both time and space,
    Where words and memories find their place."

11. "Serendipity" (2001) - "By chance or fate, two souls collide,
    In search of love, they cannot hide."

12. "P.S. I Love You" (2007) - "In letters penned, from love's embrace,
    A departed soul, still finds its trace."

13. "500 Days of Summer" (2009) - "A tale of love, both sweet and sour,
    Where seasons change, and hearts devour."

14. "The Fault in Our Stars" (2014) - "Two hearts, aflame, in starlit skies,
    Love's tragedy, where hope never dies."

15. "La La Land" (2016) - "In dreams and songs, two hearts entwine,
    A city's magic, where love's stars align."

Stepwise Execution of a Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#stepwise-execution-of-a-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------------

Executing a pipeline one step at a time is a great idea if you:

*   want to better debug the order of execution
*   log data in between each step
*   give feedback to a user as to what is being processed
*   and more!

To execute a pipeline, you must create a `run_state`, and then loop through the exection. A basic example is below.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import QueryPipeline
from llama\_index.core import PromptTemplate
from llama\_index.llms.openai import OpenAI

\# try chaining basic prompts
prompt\_str \= "Please generate related movies to {movie\_name}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
llm \= OpenAI(model\="gpt-3.5-turbo")

p \= QueryPipeline(chain\=\[prompt\_tmpl, llm\], verbose\=True)

from llama\_index.core.query\_pipeline import QueryPipeline from llama\_index.core import PromptTemplate from llama\_index.llms.openai import OpenAI # try chaining basic prompts prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) llm = OpenAI(model="gpt-3.5-turbo") p = QueryPipeline(chain=\[prompt\_tmpl, llm\], verbose=True)

In \[ \]:

Copied!

run\_state \= p.get\_run\_state(movie\_name\="The Departed")

next\_module\_keys \= p.get\_next\_module\_keys(run\_state)

while True:
    for module\_key in next\_module\_keys:
        \# get the module and input
        module \= run\_state.module\_dict\[module\_key\]
        module\_input \= run\_state.all\_module\_inputs\[module\_key\]

        \# run the module
        output\_dict \= module.run\_component(\*\*module\_input)

        \# process the output
        p.process\_component\_output(
            output\_dict,
            module\_key,
            run\_state,
        )

    \# get the next module keys
    next\_module\_keys \= p.get\_next\_module\_keys(
        run\_state,
    )

    \# if no more modules to run, break
    if not next\_module\_keys:
        run\_state.result\_outputs\[module\_key\] \= output\_dict
        break

\# the final result is at \`module\_key\`
\# it is a dict of 'output' -\> ChatResponse object in this case
print(run\_state.result\_outputs\[module\_key\]\["output"\].message.content)

run\_state = p.get\_run\_state(movie\_name="The Departed") next\_module\_keys = p.get\_next\_module\_keys(run\_state) while True: for module\_key in next\_module\_keys: # get the module and input module = run\_state.module\_dict\[module\_key\] module\_input = run\_state.all\_module\_inputs\[module\_key\] # run the module output\_dict = module.run\_component(\*\*module\_input) # process the output p.process\_component\_output( output\_dict, module\_key, run\_state, ) # get the next module keys next\_module\_keys = p.get\_next\_module\_keys( run\_state, ) # if no more modules to run, break if not next\_module\_keys: run\_state.result\_outputs\[module\_key\] = output\_dict break # the final result is at \`module\_key\` # it is a dict of 'output' -\> ChatResponse object in this case print(run\_state.result\_outputs\[module\_key\]\["output"\].message.content)

1\. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed
2. The Town (2010) - A crime thriller directed by Ben Affleck
3. Mystic River (2003) - A crime drama directed by Clint Eastwood
4. Goodfellas (1990) - A classic mobster film directed by Martin Scorsese
5. The Irishman (2019) - Another crime drama directed by Martin Scorsese, starring Robert De Niro and Al Pacino
6. The Departed (2006) - The Departed is a 2006 American crime film directed by Martin Scorsese and written by William Monahan. It is a remake of the 2002 Hong Kong film Infernal Affairs. The film stars Leonardo DiCaprio, Matt Damon, Jack Nicholson, and Mark Wahlberg, with Martin Sheen, Ray Winstone, Vera Farmiga, and Alec Baldwin in supporting roles.

Back to top

[Previous Sub Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)[Next Query Pipeline with Async/Parallel Execution](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/)

![Image 6](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

## Metadata

```json
{
  "warning": "Target URL returned error 404: Not Found",
  "title": "An Introduction to LlamaIndex Query Pipelines",
  "description": "",
  "url": "https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline.html",
  "content": "An Introduction to LlamaIndex Query Pipelines - LlamaIndex\n=============== \n\n \n\n[Skip to content](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#an-introduction-to-llamaindex-query-pipelines)\n\n[![Image 4: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ \"LlamaIndex\")\n\nLlamaIndex\n\nAn Introduction to LlamaIndex Query Pipelines\n\n  \n\nSearch\n\n*   [Home](https://docs.llamaindex.ai/en/stable/)\n*   [Learn](https://docs.llamaindex.ai/en/stable/understanding/)\n*   [Use Cases](https://docs.llamaindex.ai/en/stable/use_cases/)\n*   [Examples](https://docs.llamaindex.ai/en/stable/examples/)\n*   [Component Guides](https://docs.llamaindex.ai/en/stable/module_guides/)\n*   [Advanced Topics](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)\n*   [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/)\n*   [Open-Source Community](https://docs.llamaindex.ai/en/stable/community/integrations/)\n*   [LlamaCloud](https://docs.llamaindex.ai/en/stable/llama_cloud/)\n\n [![Image 5: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ \"LlamaIndex\")LlamaIndex\n\n*   [ ] \n    \n    [Home](https://docs.llamaindex.ai/en/stable/)\n    \n    Home\n    \n    *   [High-Level Concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)\n    *   [Installation and Setup](https://docs.llamaindex.ai/en/stable/getting_started/installation/)\n    *   [How to read these docs](https://docs.llamaindex.ai/en/stable/getting_started/reading/)\n    *   [ ]  Starter Examples\n        \n        Starter Examples\n        \n        *   [Starter Tutorial (OpenAI)](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/)\n        *   [Starter Tutorial (Local Models)](https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/)\n        \n    *   [Discover LlamaIndex Video Series](https://docs.llamaindex.ai/en/stable/getting_started/discover_llamaindex/)\n    *   [Frequently Asked Questions (FAQ)](https://docs.llamaindex.ai/en/stable/getting_started/customization/)\n    *   [ ] \n        \n        [Starter Tools](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/)\n        \n        Starter Tools\n        \n        *   [RAG CLI](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/)\n        \n    \n*   [ ] \n    \n    [Learn](https://docs.llamaindex.ai/en/stable/understanding/)\n    \n    Learn\n    \n    *   [Using LLMs](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/)\n    *   [ ] \n        \n        [Building a RAG pipeline](https://docs.llamaindex.ai/en/stable/understanding/rag/)\n        \n        Building a RAG pipeline\n        \n        *   [ ]  Loading & Ingestion\n            \n            Loading & Ingestion\n            \n            *   [Loading Data (Ingestion)](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/)\n            *   [LlamaHub](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/)\n            *   [Loading from LlamaCloud](https://docs.llamaindex.ai/en/stable/understanding/loading/llamacloud/)\n            \n        *   [Indexing & Embedding](https://docs.llamaindex.ai/en/stable/understanding/indexing/indexing/)\n        *   [Storing](https://docs.llamaindex.ai/en/stable/understanding/storing/storing/)\n        *   [Querying](https://docs.llamaindex.ai/en/stable/understanding/querying/querying/)\n        \n    *   [ ] \n        \n        [Building an agent](https://docs.llamaindex.ai/en/stable/understanding/agent/)\n        \n        Building an agent\n        \n        *   [Agents with local models](https://docs.llamaindex.ai/en/stable/understanding/agent/local_models/)\n        *   [Adding RAG to an agent](https://docs.llamaindex.ai/en/stable/understanding/agent/rag_agent/)\n        *   [Enhancing with LlamaParse](https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/)\n        *   [Memory](https://docs.llamaindex.ai/en/stable/understanding/agent/memory/)\n        *   [Adding other tools](https://docs.llamaindex.ai/en/stable/understanding/agent/tools/)\n        \n    *   [ ] \n        \n        [Building Workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/)\n        \n        Building Workflows\n        \n        *   [A basic workflow](https://docs.llamaindex.ai/en/stable/understanding/workflows/basic_flow/)\n        *   [Branches and loops](https://docs.llamaindex.ai/en/stable/understanding/workflows/branches_and_loops/)\n        *   [Maintaining state](https://docs.llamaindex.ai/en/stable/understanding/workflows/state/)\n        *   [Streaming events](https://docs.llamaindex.ai/en/stable/understanding/workflows/stream/)\n        *   [Concurrent execution](https://docs.llamaindex.ai/en/stable/understanding/workflows/concurrent_execution/)\n        *   [Subclassing workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/subclass/)\n        *   [Nested workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/nested/)\n        *   [Observability](https://docs.llamaindex.ai/en/stable/understanding/workflows/observability/)\n        *   [Unbound syntax](https://docs.llamaindex.ai/en/stable/understanding/workflows/unbound_functions/)\n        \n    *   [ ] \n        \n        [Structured Data Extraction](https://docs.llamaindex.ai/en/stable/understanding/extraction/)\n        \n        Structured Data Extraction\n        \n        *   [Using Structured LLMs](https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_llms/)\n        *   [Structured Prediction](https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_prediction/)\n        *   [Lower-level extraction](https://docs.llamaindex.ai/en/stable/understanding/extraction/lower_level/)\n        \n    *   [Tracing and Debugging](https://docs.llamaindex.ai/en/stable/understanding/tracing_and_debugging/tracing_and_debugging/)\n    *   [ ]  Evaluating\n        \n        Evaluating\n        \n        *   [Evaluating](https://docs.llamaindex.ai/en/stable/understanding/evaluating/evaluating/)\n        *   [ ] \n            \n            [Cost Analysis](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/)\n            \n            Cost Analysis\n            \n            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/)\n            \n        \n    *   [ ] \n        \n        [Putting it all Together](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/)\n        \n        Putting it all Together\n        \n        *   [ ] \n            \n            [Full-stack web application](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/)\n            \n            Full-stack web application\n            \n            *   [A Guide to Building a Full-Stack Web App with LLamaIndex](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/fullstack_app_guide/)\n            *   [A Guide to Building a Full-Stack LlamaIndex Web App with Delphic](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/fullstack_with_delphic/)\n            \n        *   [ ] \n            \n            [Q&A Patterns](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/)\n            \n            Q&A Patterns\n            \n            *   [A Guide to Extracting Terms and Definitions](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/terms_definitions_tutorial/)\n            \n        *   [ ]  Chatbots\n            \n            Chatbots\n            \n            *   [How to Build a Chatbot](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/chatbots/building_a_chatbot/)\n            \n        *   [ ] \n            \n            [Structured data](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/structured_data/)\n            \n            Structured data\n            \n        *   [Agents](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/)\n        \n    \n*   [ ] \n    \n    [Use Cases](https://docs.llamaindex.ai/en/stable/use_cases/)\n    \n    Use Cases\n    \n    *   [Prompting](https://docs.llamaindex.ai/en/stable/use_cases/prompting/)\n    *   [Question-Answering (RAG)](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/)\n    *   [Chatbots](https://docs.llamaindex.ai/en/stable/use_cases/chatbots/)\n    *   [Structured Data Extraction](https://docs.llamaindex.ai/en/stable/use_cases/extraction/)\n    *   [Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/)\n    *   [Multi-Modal Applications](https://docs.llamaindex.ai/en/stable/use_cases/multimodal/)\n    *   [Fine-Tuning](https://docs.llamaindex.ai/en/stable/use_cases/fine_tuning/)\n    \n*   [ ] \n    \n    [Examples](https://docs.llamaindex.ai/en/stable/examples/)\n    \n    Examples\n    \n    *   [ ]  Agents\n        \n        Agents\n        \n        *   [💬🤖 How to Build a Chatbot](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/)\n        *   [GPT Builder Demo](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/)\n        *   [Building a Multi-PDF Agent using Query Pipelines and HyDE](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/)\n        *   [Step-wise, Controllable Agents](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/)\n        *   [Controllable Agents for RAG](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner_rag_controllable/)\n        *   [Building an Agent around a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/query_pipeline_agent/)\n        *   [Agentic rag using vertex ai](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/)\n        *   [Agentic rag with llamaindex and vertexai managed index](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/)\n        *   [Function Calling Anthropic Agent](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/)\n        *   [Function Calling AWS Bedrock Converse Agent](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/)\n        *   [Chain-of-Abstraction LlamaPack](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/)\n        *   [Building a Custom Agent](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/)\n        *   [DashScope Agent Tutorial](https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/)\n        *   [Introspective Agents: Performing Tasks With Reflection](https://docs.llamaindex.ai/en/stable/examples/agent/introspective_agent_toxicity_reduction/)\n        *   [Language Agent Tree Search](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/)\n        *   [LLM Compiler Agent Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/)\n        *   [Simple Composable Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/)\n        *   [Vector Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/vector_memory/)\n        *   [Function Calling Mistral Agent](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/)\n        *   [Multi-Document Agents (V1)](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/)\n        *   [Multi-Document Agents](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/)\n        *   [Function Calling NVIDIA Agent](https://docs.llamaindex.ai/en/stable/examples/agent/nvidia_agent/)\n        *   [Document Research Assistant for Blog Creation](https://docs.llamaindex.ai/en/stable/examples/agent/nvidia_document_research_assistant_for_blog_creation/)\n        *   [Sub Question Query Engine powered by NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/agent/nvidia_sub_question_query_engine/)\n        *   [Build your own OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)\n        *   [Context-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/)\n        *   [OpenAI Agent Workarounds for Lengthy Tool Descriptions](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_lengthy_tools/)\n        *   [Single-Turn Multi-Function Calling OpenAI Agents](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/)\n        *   [OpenAI Agent + Query Engine Experimental Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/)\n        *   [OpenAI Agent Query Planning](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/)\n        *   [Retrieval-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/)\n        *   [OpenAI Agent with Tool Call Parser](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/)\n        *   [OpenAI Agent with Query Engine Tools](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/)\n        *   [OpenAI Assistant Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/)\n        *   [OpenAI Assistant Advanced Retrieval Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/)\n        *   [OpenAI agent: specifying a forced function call](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/)\n        *   [Benchmarking OpenAI Retrieval API (through Assistant Agent)](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/)\n        *   [ReAct Agent - A Simple Intro with Calculator Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/)\n        *   [ReAct Agent with Query Engine (RAG) Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/)\n        *   [Controlling Agent Reasoning Loop with Return Direct Tools](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/)\n        *   [Structured Planning Agent](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/)\n        \n    *   [ ]  Chat Engines\n        \n        Chat Engines\n        \n        *   [Chat Engine - Best Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_best/)\n        *   [Chat Engine - Condense Plus Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/)\n        *   [Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/)\n        *   [Chat Engine - Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_context/)\n        *   [Chat Engine - OpenAI Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_openai/)\n        *   [Chat Engine with a Personality ✨](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/)\n        *   [Chat Engine - ReAct Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_react/)\n        *   [Chat Engine - Simple Mode REPL](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_repl/)\n        \n    *   [ ]  Cookbooks\n        \n        Cookbooks\n        \n        *   [GraphRAG Implementation with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/cookbooks/GraphRAG_v1/)\n        *   [GraphRAG Implementation with LlamaIndex - V2](https://docs.llamaindex.ai/en/stable/examples/cookbooks/GraphRAG_v2/)\n        *   [AirtrainAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/airtrain/)\n        *   [Anthropic Haiku Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/anthropic_haiku/)\n        *   [Trustworthy RAG with the Trustworthy Language Model](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cleanlab_tlm_rag/)\n        *   [Codestral from MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/)\n        *   [Cohere init8 and binary Embeddings Retrieval Evaluation](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/)\n        *   [Contextual Retrieval](https://docs.llamaindex.ai/en/stable/examples/cookbooks/contextual_retrieval/)\n        *   [CrewAI + LlamaIndex Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/crewai_llamaindex/)\n        *   [Llama3 Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook/)\n        *   [LLM Cookbook with Intel Gaudi](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_gaudi/)\n        *   [Llama3 Cookbook with Groq](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_groq/)\n        *   [Llama3 Cookbook with Ollama and Replicate](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_ollama_replicate/)\n        *   [MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/)\n        *   [mixedbread Rerank Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/)\n        *   [Optimizing for relevance using MongoDB and LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mongodb_retrieval_strategies/)\n        *   [Oracle AI Vector Search with Document Processing](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oracleai_demo/)\n        *   [Components Of LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-2/Components_Of_LlamaIndex/)\n        *   [Evaluating RAG Systems](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-3/Evaluating_RAG_Systems/)\n        *   [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-4/Ingestion_Pipeline/)\n        *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-4/Metadata_Extraction/)\n        *   [Observability](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-5/Observability/)\n        *   [Agents](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-6/Agents/)\n        *   [Router QueryEngine and SubQuestion QueryEngine](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-6/Router_And_SubQuestion_QueryEngine/)\n        *   [Multi-Modal RAG System](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-7/Multi_Modal_RAG_System/)\n        *   [Advanced RAG with LlamaParse](https://docs.llamaindex.ai/en/stable/examples/cookbooks/oreilly_course_cookbooks/Module-8/Advanced_RAG_with_LlamaParse/)\n        *   [Prometheus-2 Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/prometheus2_cookbook/)\n        *   [Sales Prospecting Workflow with Toolhouse](https://docs.llamaindex.ai/en/stable/examples/cookbooks/toolhouse_llamaindex/)\n        \n    *   [ ]  Customization\n        \n        Customization\n        \n        *   [Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/customization/llms/AzureOpenAI/)\n        *   [ChatGPT](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/)\n        *   [HuggingFace LLM - Camel-5b](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/)\n        *   [HuggingFace LLM - StableLM](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/)\n        *   [Chat Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/)\n        *   [Completion Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)\n        *   [Streaming](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/)\n        *   [Streaming for Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/chat_engine_condense_question_stream_response/)\n        \n    *   [ ]  Data Connectors\n        \n        Data Connectors\n        \n        *   [Chroma Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ChromaDemo/)\n        *   [DashVector Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DashvectorReaderDemo/)\n        *   [Database Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DatabaseReaderDemo/)\n        *   [DeepLake Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DeepLakeReader/)\n        *   [Discord Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DiscordDemo/)\n        *   [Docling Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DoclingReaderDemo/)\n        *   [Faiss Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/FaissDemo/)\n        *   [Github Repo Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GithubRepositoryReaderDemo/)\n        *   [Google Chat Reader Test](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleChatDemo/)\n        *   [Google Docs Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleDocsDemo/)\n        *   [Google Drive Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleDriveDemo/)\n        *   [Google Maps Text Search Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleMapsTextSearchReaderDemo/)\n        *   [Google Sheets Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleSheetsDemo/)\n        *   [Make Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MakeDemo/)\n        *   [Mbox Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MboxReaderDemo/)\n        *   [MilvusReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MilvusReaderDemo/)\n        *   [MongoDB Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MongoDemo/)\n        *   [MyScale Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MyScaleReaderDemo/)\n        *   [Notion Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/NotionDemo/)\n        *   [Obsidian Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ObsidianReaderDemo/)\n        *   [Pathway Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/)\n        *   [Preprocess](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PreprocessReaderDemo/)\n        *   [Psychic Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PsychicDemo/)\n        *   [Qdrant Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/QdrantDemo/)\n        *   [Slack Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/SlackDemo/)\n        *   [Twitter Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/TwitterDemo/)\n        *   [Weaviate Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/)\n        *   [Web Page Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/)\n        *   [Zyte Serp Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ZyteSerpDemo/)\n        *   [Deplot Reader Demo](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/)\n        *   [HTML Tag Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/html_tag_reader/)\n        *   [Oracle AI Vector Search: Document Processing](https://docs.llamaindex.ai/en/stable/examples/data_connectors/oracleai/)\n        *   [Simple Directory Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/)\n        *   [Parallel Processing SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_parallel/)\n        *   [Simple Directory Reader over a Remote FileSystem](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_remote_fs/)\n        \n    *   [ ]  Discover LlamaIndex\n        \n        Discover LlamaIndex\n        \n        *   [Discord Thread Management](https://docs.llamaindex.ai/en/stable/examples/discover_llamaindex/document_management/Discord_Thread_Management/)\n        \n    *   [ ]  Docstores\n        \n        Docstores\n        \n        *   [Demo: Azure Table Storage as a Docstore](https://docs.llamaindex.ai/en/stable/examples/docstore/AzureDocstoreDemo/)\n        *   [Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/)\n        *   [Dynamo DB Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/)\n        *   [Firestore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/FirestoreDemo/)\n        *   [MongoDB Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/MongoDocstoreDemo/)\n        *   [Redis Docstore+Index Store Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/)\n        *   [Tablestore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/TablestoreDocstoreDemo/)\n        \n    *   [ ]  Embeddings\n        \n        Embeddings\n        \n        *   [Anyscale Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Anyscale/)\n        *   [LangChain Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain/)\n        *   [OpenAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/)\n        *   [Aleph Alpha Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/alephalpha/)\n        *   [Bedrock Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/bedrock/)\n        *   [Embeddings with Clarifai](https://docs.llamaindex.ai/en/stable/examples/embeddings/clarifai/)\n        *   [Cloudflare Workers AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/cloudflare_workersai/)\n        *   [CohereAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/cohereai/)\n        *   [Custom Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/)\n        *   [Dashscope embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/dashscope_embeddings/)\n        *   [Databricks Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/databricks/)\n        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/examples/embeddings/deepinfra/)\n        *   [Elasticsearch Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/elasticsearch/)\n        *   [Qdrant FastEmbed Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/fastembed/)\n        *   [Fireworks Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/fireworks/)\n        *   [Google Gemini Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/gemini/)\n        *   [Gigachat](https://docs.llamaindex.ai/en/stable/examples/embeddings/gigachat/)\n        *   [Google PaLM Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/google_palm/)\n        *   [Local Embeddings with HuggingFace](https://docs.llamaindex.ai/en/stable/examples/embeddings/huggingface/)\n        *   [IBM watsonx.ai](https://docs.llamaindex.ai/en/stable/examples/embeddings/ibm_watsonx/)\n        *   [Local Embeddings with IPEX-LLM on Intel CPU](https://docs.llamaindex.ai/en/stable/examples/embeddings/ipex_llm/)\n        *   [Local Embeddings with IPEX-LLM on Intel GPU](https://docs.llamaindex.ai/en/stable/examples/embeddings/ipex_llm_gpu/)\n        *   [Jina 8K Context Window Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/)\n        *   [Jina Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/)\n        *   [Llamafile Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llamafile/)\n        *   [LLMRails Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llm_rails/)\n        *   [MistralAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/mistralai/)\n        *   [Mixedbread AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/mixedbreadai/)\n        *   [ModelScope Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/modelscope/)\n        *   [Nebius Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/nebius/)\n        *   [Nomic Embedding](https://docs.llamaindex.ai/en/stable/examples/embeddings/nomic/)\n        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/embeddings/nvidia/)\n        *   [Oracle Cloud Infrastructure Generative AI](https://docs.llamaindex.ai/en/stable/examples/embeddings/oci_genai/)\n        *   [Ollama Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/ollama_embedding/)\n        *   [Local Embeddings with OpenVINO](https://docs.llamaindex.ai/en/stable/examples/embeddings/openvino/)\n        *   [Optimized Embedding Model using Optimum-Intel](https://docs.llamaindex.ai/en/stable/examples/embeddings/optimum_intel/)\n        *   [Oracle AI Vector Search: Generate Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/oracleai/)\n        *   [PremAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/premai/)\n        *   [Interacting with Embeddings deployed in Amazon SageMaker Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/embeddings/sagemaker_embedding_endpoint/)\n        *   [Text Embedding Inference](https://docs.llamaindex.ai/en/stable/examples/embeddings/text_embedding_inference/)\n        *   [TextEmbed - Embedding Inference Server](https://docs.llamaindex.ai/en/stable/examples/embeddings/textembed/)\n        *   [Together AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/together/)\n        *   [Upstage Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/upstage/)\n        *   [Interacting with Embeddings deployed in Vertex AI Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/embeddings/vertex_embedding_endpoint/)\n        *   [VoyageAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/voyageai/)\n        *   [Yandexgpt](https://docs.llamaindex.ai/en/stable/examples/embeddings/yandexgpt/)\n        \n    *   [ ]  Evaluation\n        \n        Evaluation\n        \n        *   [BEIR Out of Domain Benchmark](https://docs.llamaindex.ai/en/stable/examples/evaluation/BeirEvaluation/)\n        *   [🚀 RAG/LLM Evaluators - DeepEval](https://docs.llamaindex.ai/en/stable/examples/evaluation/Deepeval/)\n        *   [HotpotQADistractor Demo](https://docs.llamaindex.ai/en/stable/examples/evaluation/HotpotQADistractor/)\n        *   [QuestionGeneration](https://docs.llamaindex.ai/en/stable/examples/evaluation/QuestionGeneration/)\n        *   [RAGChecker: A Fine-grained Evaluation Framework For Diagnosing RAG](https://docs.llamaindex.ai/en/stable/examples/evaluation/RAGChecker/)\n        *   [Self Correcting Query Engines - Evaluation & Retry](https://docs.llamaindex.ai/en/stable/examples/evaluation/RetryQuery/)\n        *   [Tonic Validate Evaluators](https://docs.llamaindex.ai/en/stable/examples/evaluation/TonicValidateEvaluators/)\n        *   [How to use UpTrain with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/evaluation/UpTrain/)\n        *   [Answer Relevancy and Context Relevancy Evaluations](https://docs.llamaindex.ai/en/stable/examples/evaluation/answer_and_context_relevancy/)\n        *   [BatchEvalRunner - Running Multiple Evaluations](https://docs.llamaindex.ai/en/stable/examples/evaluation/batch_eval/)\n        *   [Correctness Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/correctness_eval/)\n        *   [Faithfulness Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/faithfulness_eval/)\n        *   [Guideline Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/guideline_eval/)\n        *   [Benchmarking LLM Evaluators On The MT-Bench Human Judgement](https://docs.llamaindex.ai/en/stable/examples/evaluation/mt_bench_human_judgement/)\n        *   [Benchmarking LLM Evaluators On A Mini MT-Bench (Single Grading)](https://docs.llamaindex.ai/en/stable/examples/evaluation/mt_bench_single_grading/)\n        *   [Evaluating Multi-Modal RAG](https://docs.llamaindex.ai/en/stable/examples/evaluation/multi_modal/multi_modal_rag_evaluation/)\n        *   [Pairwise Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/pairwise_eval/)\n        *   [Evaluation using Prometheus model](https://docs.llamaindex.ai/en/stable/examples/evaluation/prometheus_evaluation/)\n        *   [Relevancy Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/relevancy_eval/)\n        *   [Retrieval Evaluation](https://docs.llamaindex.ai/en/stable/examples/evaluation/retrieval/retriever_eval/)\n        *   [Embedding Similarity Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/semantic_similarity_eval/)\n        *   [🏔️ Step-back prompting with workflows for RAG with Argilla](https://docs.llamaindex.ai/en/stable/examples/evaluation/step_back_argilla/)\n        \n    *   [ ]  Finetuning\n        \n        Finetuning\n        \n        *   [How to Finetune a cross-encoder using LLamaIndex](https://docs.llamaindex.ai/en/stable/examples/finetuning/cross_encoder_finetuning/cross_encoder_finetuning/)\n        *   [Finetuning corpus embeddings using NUDGE](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_corpus_embedding/)\n        *   [Finetune Embeddings](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding/)\n        *   [Finetuning an Adapter on Top of any Black-Box Embedding Model](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding_adapter/)\n        *   [Knowledge Distillation For Fine-Tuning A GPT-3.5 Judge (Correctness)](https://docs.llamaindex.ai/en/stable/examples/finetuning/llm_judge/correctness/finetune_llm_judge_single_grading_correctness/)\n        *   [Knowledge Distillation For Fine-Tuning A GPT-3.5 Judge (Pairwise)](https://docs.llamaindex.ai/en/stable/examples/finetuning/llm_judge/pairwise/finetune_llm_judge/)\n        *   [Fine Tuning MistralAI models using Finetuning API](https://docs.llamaindex.ai/en/stable/examples/finetuning/mistralai_fine_tuning/)\n        *   [Fine Tuning GPT-3.5-Turbo](https://docs.llamaindex.ai/en/stable/examples/finetuning/openai_fine_tuning/)\n        *   [Fine Tuning with Function Calling](https://docs.llamaindex.ai/en/stable/examples/finetuning/openai_fine_tuning_functions/)\n        *   [Fine-tuning a gpt-3.5 ReAct Agent on Better Chain of Thought](https://docs.llamaindex.ai/en/stable/examples/finetuning/react_agent/react_agent_finetune/)\n        *   [Custom Cohere Reranker](https://docs.llamaindex.ai/en/stable/examples/finetuning/rerankers/cohere_custom_reranker/)\n        *   [Router Fine-tuning](https://docs.llamaindex.ai/en/stable/examples/finetuning/router/router_finetune/)\n        \n    *   [ ]  Ingestion\n        \n        Ingestion\n        \n        *   [Advanced Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/advanced_ingestion_pipeline/)\n        *   [Async Ingestion Pipeline + Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/ingestion/async_ingestion_pipeline/)\n        *   [Ingestion Pipeline + Document Management](https://docs.llamaindex.ai/en/stable/examples/ingestion/document_management_pipeline/)\n        *   [Building a Live RAG Pipeline over Google Drive Files](https://docs.llamaindex.ai/en/stable/examples/ingestion/ingestion_gdrive/)\n        *   [Parallelizing Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/parallel_execution_ingestion_pipeline/)\n        *   [Redis Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/redis_ingestion_pipeline/)\n        \n    *   [ ]  LLMs\n        \n        LLMs\n        \n        *   [AI21](https://docs.llamaindex.ai/en/stable/examples/llm/ai21/)\n        *   [Aleph Alpha](https://docs.llamaindex.ai/en/stable/examples/llm/alephalpha/)\n        *   [Anthropic](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/)\n        *   [Anthropic Prompt Caching](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic_prompt_caching/)\n        *   [Anyscale](https://docs.llamaindex.ai/en/stable/examples/llm/anyscale/)\n        *   [Azure AI model inference](https://docs.llamaindex.ai/en/stable/examples/llm/azure_inference/)\n        *   [Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/azure_openai/)\n        *   [Bedrock](https://docs.llamaindex.ai/en/stable/examples/llm/bedrock/)\n        *   [Bedrock Converse](https://docs.llamaindex.ai/en/stable/examples/llm/bedrock_converse/)\n        *   [Cerebras](https://docs.llamaindex.ai/en/stable/examples/llm/cerebras/)\n        *   [Clarifai LLM](https://docs.llamaindex.ai/en/stable/examples/llm/clarifai/)\n        *   [Cleanlab Trustworthy Language Model](https://docs.llamaindex.ai/en/stable/examples/llm/cleanlab/)\n        *   [Cohere](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/)\n        *   [DashScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/dashscope/)\n        *   [DataBricks](https://docs.llamaindex.ai/en/stable/examples/llm/databricks/)\n        *   [DeepInfra](https://docs.llamaindex.ai/en/stable/examples/llm/deepinfra/)\n        *   [EverlyAI](https://docs.llamaindex.ai/en/stable/examples/llm/everlyai/)\n        *   [Fireworks](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks/)\n        *   [Fireworks Function Calling Cookbook](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks_cookbook/)\n        *   [Friendli](https://docs.llamaindex.ai/en/stable/examples/llm/friendli/)\n        *   [Gemini](https://docs.llamaindex.ai/en/stable/examples/llm/gemini/)\n        *   [Groq](https://docs.llamaindex.ai/en/stable/examples/llm/groq/)\n        *   [Hugging Face LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/huggingface/)\n        *   [IBM watsonx.ai](https://docs.llamaindex.ai/en/stable/examples/llm/ibm_watsonx/)\n        *   [IPEX-LLM on Intel CPU](https://docs.llamaindex.ai/en/stable/examples/llm/ipex_llm/)\n        *   [IPEX-LLM on Intel GPU](https://docs.llamaindex.ai/en/stable/examples/llm/ipex_llm_gpu/)\n        *   [Konko](https://docs.llamaindex.ai/en/stable/examples/llm/konko/)\n        *   [Langchain](https://docs.llamaindex.ai/en/stable/examples/llm/langchain/)\n        *   [LiteLLM](https://docs.llamaindex.ai/en/stable/examples/llm/litellm/)\n        *   [Replicate - Llama 2 13B](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2/)\n        *   [LlamaCPP](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/)\n        *   [🦙 x 🦙 Rap Battle](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_rap_battle/)\n        *   [Llama API](https://docs.llamaindex.ai/en/stable/examples/llm/llama_api/)\n        *   [llamafile](https://docs.llamaindex.ai/en/stable/examples/llm/llamafile/)\n        *   [LLM Predictor](https://docs.llamaindex.ai/en/stable/examples/llm/llm_predictor/)\n        *   [LM Studio](https://docs.llamaindex.ai/en/stable/examples/llm/lmstudio/)\n        *   [LocalAI](https://docs.llamaindex.ai/en/stable/examples/llm/localai/)\n        *   [Maritalk](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/)\n        *   [MistralRS LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mistral_rs/)\n        *   [MistralAI](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/)\n        *   [ModelScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/modelscope/)\n        *   [Monster API <\\> LLamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/monsterapi/)\n        *   [MyMagic AI LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mymagic/)\n        *   [Nebius LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/nebius/)\n        *   [Neutrino AI](https://docs.llamaindex.ai/en/stable/examples/llm/neutrino/)\n        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia/)\n        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_nim/)\n        *   [Nvidia TensorRT-LLM](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_tensorrt/)\n        *   [NVIDIA's LLM Text Completion API](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_text_completion/)\n        *   [Nvidia Triton](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_triton/)\n        *   [Oracle Cloud Infrastructure Generative AI](https://docs.llamaindex.ai/en/stable/examples/llm/oci_genai/)\n        *   [OctoAI](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/)\n        *   [Ollama - Llama 3.1](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/)\n        *   [Ollama - Gemma](https://docs.llamaindex.ai/en/stable/examples/llm/ollama_gemma/)\n        *   [OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/openai/)\n        *   [OpenAI JSON Mode vs. Function Calling for Data Extraction](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/)\n        *   [OpenLLM](https://docs.llamaindex.ai/en/stable/examples/llm/openllm/)\n        *   [OpenRouter](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/)\n        *   [OpenVINO LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/openvino/)\n        *   [Optimum Intel LLMs optimized with IPEX backend](https://docs.llamaindex.ai/en/stable/examples/llm/optimum_intel/)\n        *   [AlibabaCloud-PaiEas](https://docs.llamaindex.ai/en/stable/examples/llm/paieas/)\n        *   [PaLM](https://docs.llamaindex.ai/en/stable/examples/llm/palm/)\n        *   [Perplexity](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/)\n        *   [Pipeshift](https://docs.llamaindex.ai/en/stable/examples/llm/pipeshift/)\n        *   [Portkey](https://docs.llamaindex.ai/en/stable/examples/llm/portkey/)\n        *   [Predibase](https://docs.llamaindex.ai/en/stable/examples/llm/predibase/)\n        *   [PremAI LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/premai/)\n        *   [Client of Baidu Intelligent Cloud's Qianfan LLM Platform](https://docs.llamaindex.ai/en/stable/examples/llm/qianfan/)\n        *   [RunGPT](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/)\n        *   [Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/)\n        *   [SambaNova Systems](https://docs.llamaindex.ai/en/stable/examples/llm/sambanovasystems/)\n        *   [Together AI LLM](https://docs.llamaindex.ai/en/stable/examples/llm/together/)\n        *   [Upstage](https://docs.llamaindex.ai/en/stable/examples/llm/upstage/)\n        *   [Vertex AI](https://docs.llamaindex.ai/en/stable/examples/llm/vertex/)\n        *   [Replicate - Vicuna 13B](https://docs.llamaindex.ai/en/stable/examples/llm/vicuna/)\n        *   [vLLM](https://docs.llamaindex.ai/en/stable/examples/llm/vllm/)\n        *   [Xorbits Inference](https://docs.llamaindex.ai/en/stable/examples/llm/xinference_local_deployment/)\n        *   [Yi](https://docs.llamaindex.ai/en/stable/examples/llm/yi/)\n        \n    *   [ ]  Llama Datasets\n        \n        Llama Datasets\n        \n        *   [Downloading a LlamaDataset from LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/downloading_llama_datasets/)\n        *   [Benchmarking RAG Pipelines With A](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/labelled-rag-datasets/)\n        *   [Submission Template Notebook](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/ragdataset_submission_template/)\n        *   [Contributing a LlamaDataset To LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/)\n        \n    *   [ ]  Llama Hub\n        \n        Llama Hub\n        \n        *   [LlamaHub Demostration](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/)\n        *   [Ollama Llama Pack Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_ollama/)\n        *   [Llama Pack - Resume Screener 📄](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_resume/)\n        *   [Llama Packs Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/)\n        \n    *   [ ]  Low Level\n        \n        Low Level\n        \n        *   [Building Evaluation from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/)\n        *   [Building an Advanced Fusion Retriever from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/)\n        *   [Building Data Ingestion from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/)\n        *   [Building RAG from Scratch (Open-source only!)](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval/)\n        *   [Building Response Synthesis from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/)\n        *   [Building Retrieval from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/)\n        *   [Building a Router from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/router/)\n        *   [Building a (Very Simple) Vector Store from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/vector_store/)\n        \n    *   [ ]  Managed Indexes\n        \n        Managed Indexes\n        \n        *   [BGEM3Demo](https://docs.llamaindex.ai/en/stable/examples/managed/BGEM3Demo/)\n        *   [Google Generative Language Semantic Retriever](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/)\n        *   [PostgresML Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/)\n        *   [Google Cloud LlamaIndex on Vertex AI for RAG](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/)\n        *   [Semantic Retriever Benchmark](https://docs.llamaindex.ai/en/stable/examples/managed/manage_retrieval_benchmark/)\n        *   [Vectara Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/)\n        *   [Managed Index with Zilliz Cloud Pipelines](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/)\n        \n    *   [ ]  Memory\n        \n        Memory\n        \n        *   [Mem0](https://docs.llamaindex.ai/en/stable/examples/memory/Mem0Memory/)\n        \n    *   [ ]  Metadata Extractors\n        \n        Metadata Extractors\n        \n        *   [Entity Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/EntityExtractionClimate/)\n        *   [Metadata Extraction and Augmentation w/ Marvin](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/)\n        *   [Extracting Metadata for Better Document Indexing and Understanding](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/)\n        *   [Automated Metadata Extraction for Better Retrieval + Synthesis](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtraction_LLMSurvey/)\n        *   [Pydantic Extractor](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/)\n        \n    *   [ ]  Multi-Modal\n        \n        Multi-Modal\n        \n        *   [Chroma Multi-Modal Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/)\n        *   [Multi-Modal LLM using Anthropic model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/)\n        *   [Multi-Modal LLM using Azure OpenAI GPT-4o mini for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/)\n        *   [Multi-Modal Retrieval using Cohere Multi-Modal Embeddings](https://docs.llamaindex.ai/en/stable/examples/multi_modal/cohere_multi_modal/)\n        *   [Multi-Modal LLM using DashScope qwen-vl model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/dashscope_multi_modal/)\n        *   [Multi-Modal LLM using Google's Gemini model for image understanding and build Retrieval Augmented Generation with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/)\n        *   [Multimodal Structured Outputs: GPT-4o vs. Other GPT-4 Variants](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/)\n        *   [GPT4-V Experiments with General, Specific questions and Chain Of Thought (COT) Prompting Technique.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_experiments_cot/)\n        *   [Advanced Multi-Modal Retrieval using GPT4V and Multi-Modal Index/Retriever](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_multi_modal_retrieval/)\n        *   [Image to Image Retrieval using CLIP embedding and image correlation reasoning using GPT4V](https://docs.llamaindex.ai/en/stable/examples/multi_modal/image_to_image_retrieval/)\n        *   [LlaVa Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/)\n        *   [Retrieval-Augmented Image Captioning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_multi_modal_tesla_10q/)\n        *   [Multi-Modal LLM using Mistral for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/mistral_multi_modal/)\n        *   [\\[Beta\\] Multi-modal ReAct Agent](https://docs.llamaindex.ai/en/stable/examples/multi_modal/mm_agent/)\n        *   [Multi-Modal GPT4V Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/)\n        *   [Multi-Modal RAG using Nomic Embed and Anthropic.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/)\n        *   [Multi-Modal Retrieval using GPT text embedding and CLIP image embedding for Wikipedia Articles](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_retrieval/)\n        *   [Multimodal RAG for processing videos using OpenAI GPT4V and LanceDB vectorstore](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/)\n        *   [Multimodal RAG with VideoDB](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_videorag_videodb/)\n        *   [Multimodal rag guardrail gemini llmguard llmguard](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multimodal_rag_guardrail_gemini_llmguard_llmguard/)\n        *   [Multimodal models with Nebius](https://docs.llamaindex.ai/en/stable/examples/multi_modal/nebius_multi_modal/)\n        *   [Multi-Modal LLM using NVIDIA endpoints for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/nvidia_multi_modal/)\n        *   [Multimodal Ollama Cookbook](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/)\n        *   [Using OpenAI GPT-4V model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/)\n        *   [Local Multimodal pipeline with OpenVINO](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openvino_multimodal/)\n        *   [Multi-Modal LLM using Replicate LlaVa, Fuyu 8B, MiniGPT4 models for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)\n        *   [Semi-structured Image Retrieval](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/)\n        \n    *   [ ]  Multi-Tenancy\n        \n        Multi-Tenancy\n        \n        *   [Multi-Tenancy RAG with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/)\n        \n    *   [ ]  Node Parsers & Text Splitters\n        \n        Node Parsers & Text Splitters\n        \n        *   [Semantic Chunker](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_chunking/)\n        *   [Semantic double merging chunking](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_double_merging_chunking/)\n        *   [TopicNodeParser](https://docs.llamaindex.ai/en/stable/examples/node_parsers/topic_parser/)\n        \n    *   [ ]  Node Postprocessors\n        \n        Node Postprocessors\n        \n        *   [Cohere Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/)\n        *   [Reranking using ColPali, Cohere Reranker and Multi-Modal Embeddings](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColPaliRerank/)\n        *   [Colbert Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColbertRerank/)\n        *   [File Based Node Parsers](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FileNodeProcessors/)\n        *   [FlagEmbeddingReranker](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FlagEmbeddingReranker/)\n        *   [Jina Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/JinaRerank/)\n        *   [LLM Reranker Demonstration (Great Gatsby)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Gatsby/)\n        *   [LLM Reranker Demonstration (2021 Lyft 10-k)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Lyft-10k/)\n        *   [LongContextReorder](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder/)\n        *   [Metadata Replacement + Node Sentence Window](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/)\n        *   [Mixedbread AI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MixedbreadAIRerank/)\n        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/)\n        *   [Sentence Embedding Optimizer](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo/)\n        *   [PII Masking](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/)\n        *   [Forward/Backward Augmentation](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PrevNextPostprocessorDemo/)\n        *   [Recency Filtering](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/)\n        *   [SentenceTransformerRerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/SentenceTransformerRerank/)\n        *   [Time-Weighted Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/)\n        *   [VoyageAI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/)\n        *   [OpenVINO Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/)\n        *   [RankGPT Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankGPT/)\n        *   [RankLLM Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankLLM/)\n        \n    *   [ ]  Object Stores\n        \n        Object Stores\n        \n        *   [The Class](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/)\n        \n    *   [ ]  Observability\n        \n        Observability\n        \n        *   [Aim Callback](https://docs.llamaindex.ai/en/stable/examples/observability/AimCallback/)\n        *   [HoneyHive LlamaIndex Tracer](https://docs.llamaindex.ai/en/stable/examples/observability/HoneyHiveLlamaIndexTracer/)\n        *   [Langfuse Callback Handler](https://docs.llamaindex.ai/en/stable/examples/observability/LangfuseCallbackHandler/)\n        *   [Analyze and Debug LlamaIndex Applications with PostHog and Langfuse](https://docs.llamaindex.ai/en/stable/examples/observability/LangfuseMistralPostHog/)\n        *   [Llama Debug Handler](https://docs.llamaindex.ai/en/stable/examples/observability/LlamaDebugHandler/)\n        *   [MLflow](https://docs.llamaindex.ai/en/stable/examples/observability/MLflow/)\n        *   [OpenInference Callback Handler + Arize Phoenix](https://docs.llamaindex.ai/en/stable/examples/observability/OpenInferenceCallback/)\n        *   [Observability with OpenLLMetry](https://docs.llamaindex.ai/en/stable/examples/observability/OpenLLMetry/)\n        *   [Logging traces with Opik](https://docs.llamaindex.ai/en/stable/examples/observability/OpikCallback/)\n        *   [PromptLayer Handler](https://docs.llamaindex.ai/en/stable/examples/observability/PromptLayerHandler/)\n        *   [Token Counting Handler](https://docs.llamaindex.ai/en/stable/examples/observability/TokenCountingHandler/)\n        *   [UpTrain Callback Handler](https://docs.llamaindex.ai/en/stable/examples/observability/UpTrainCallback/)\n        *   [Wandb Callback Handler](https://docs.llamaindex.ai/en/stable/examples/observability/WandbCallbackHandler/)\n        \n    *   [ ]  Output Parsers\n        \n        Output Parsers\n        \n        *   [Guardrails Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/)\n        *   [Langchain Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/)\n        *   [DataFrame Structured Data Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)\n        *   [Evaporate Demo](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/)\n        *   [Function Calling Program for Structured Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/)\n        *   [Guidance Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_pydantic_program/)\n        *   [Guidance for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/)\n        *   [LLM Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/)\n        *   [LM Format Enforcer Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_pydantic_program/)\n        *   [LM Format Enforcer Regular Expression Generation](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_regular_expressions/)\n        *   [LLM Pydantic Program - NVIDIA](https://docs.llamaindex.ai/en/stable/examples/output_parsing/nvidia_output_parsing/)\n        *   [OpenAI Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/)\n        *   [OpenAI function calling for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_sub_question/)\n        \n    *   [ ]  Param Optimizer\n        \n        Param Optimizer\n        \n        *   [\\[WIP\\] Hyperparameter Optimization for RAG](https://docs.llamaindex.ai/en/stable/examples/param_optimizer/param_optimizer/)\n        \n    *   [ ]  Prompts\n        \n        Prompts\n        \n        *   [Advanced Prompt Techniques (Variable Mappings, Functions)](https://docs.llamaindex.ai/en/stable/examples/prompts/advanced_prompts/)\n        *   [EmotionPrompt in RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/)\n        *   [Accessing/Customizing Prompts within Higher-Level Modules](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_mixin/)\n        *   [\"Optimization by Prompting\" for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/)\n        *   [Prompt Engineering for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/)\n        \n    *   [ ]  Property Graph\n        \n        Property Graph\n        \n        *   [Using a Property Graph Store](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/)\n        *   [Property Graph Construction with Predefined Schemas](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/)\n        *   [Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/)\n        *   [Defining a Custom Property Graph Retriever](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/)\n        *   [Memgraph Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_memgraph/)\n        *   [Neo4j Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/)\n        \n    *   [ ]  Query Engines\n        \n        Query Engines\n        \n        *   [Retriever Query Engine with Custom Retrievers - Simple Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/)\n        *   [JSONalyze Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JSONalyze_query_engine/)\n        *   [Joint QA Summary Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JointQASummary/)\n        *   [Retriever Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RetrieverRouterQueryEngine/)\n        *   [Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/)\n        *   [SQL Auto Vector Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/)\n        *   [SQL Join Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/)\n        *   [SQL Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/)\n        *   [CitationQueryEngine](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/)\n        *   [Cogniswitch query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/)\n        *   [Defining a Custom Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/)\n        *   [Ensemble Query Engine Guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/)\n        *   [FLARE Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine/)\n        *   [JSON Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/json_query_engine/)\n        *   [Knowledge Graph Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/)\n        *   [Knowledge Graph RAG Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine/)\n        *   [Structured Hierarchical Retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/multi_doc_auto_retrieval/multi_doc_auto_retrieval/)\n        *   [Pandas Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/)\n        *   [Recursive Retriever + Query Engine Demo](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/)\n        *   [\\[Beta\\] Text-to-SQL with PGVector](https://docs.llamaindex.ai/en/stable/examples/query_engine/pgvector_sql_query_engine/)\n        *   [Query Engine with Pydantic Outputs](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/)\n        *   [Recursive Retriever + Document Agents](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/)\n        *   [Joint Tabular/Semantic QA over Tesla 10K](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table/)\n        *   [Sub Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)\n        \n    *   [ ]  Query Pipeline\n        \n        Query Pipeline\n        \n        *   [ ]  An Introduction to LlamaIndex Query Pipelines [An Introduction to LlamaIndex Query Pipelines](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/)\n            \n            Table of contents\n            \n            *   [Overview](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#overview)\n            *   [Cookbook](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#cookbook)\n            *   [Setup](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#setup)\n            *   [1\\. Chain Together Prompt and LLM](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-chain-together-prompt-and-llm)\n                \n                *   [View Intermediate Inputs/Outputs](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#view-intermediate-inputsoutputs)\n                *   [Try Output Parsing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#try-output-parsing)\n                *   [Streaming Support](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#streaming-support)\n                \n            *   [Chain Together Query Rewriting Workflow (prompts + LLM) with Retrieval](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#chain-together-query-rewriting-workflow-prompts-llm-with-retrieval)\n            *   [Create a Full RAG Pipeline as a DAG](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#create-a-full-rag-pipeline-as-a-dag)\n                \n                *   [1\\. RAG Pipeline with Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-rag-pipeline-with-query-rewriting)\n                *   [2\\. RAG Pipeline without Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#2-rag-pipeline-without-query-rewriting)\n                \n            *   [Defining a Custom Component in a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#defining-a-custom-component-in-a-query-pipeline)\n            *   [Stepwise Execution of a Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#stepwise-execution-of-a-pipeline)\n            \n        *   [Query Pipeline with Async/Parallel Execution](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/)\n        *   [Query Pipeline Chat Engine](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/)\n        *   [Query Pipeline over Pandas DataFrames](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/)\n        *   [Query Pipeline with Routing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/)\n        *   [Query Pipeline for Advanced Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/)\n        \n    *   [ ]  Query Transformations\n        \n        Query Transformations\n        \n        *   [HyDE Query Transform](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo/)\n        *   [Multi-Step Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_transformations/SimpleIndexDemo-multistep/)\n        *   [Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook/)\n        \n    *   [ ]  Response Synthesizers\n        \n        Response Synthesizers\n        \n        *   [Pydantic Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/)\n        *   [Stress-Testing Long Context LLMs with a Recall Task](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/long_context_test/)\n        *   [Pydantic Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/)\n        *   [Refine](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/)\n        *   [Refine with Structured Answer Filtering](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/)\n        *   [Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/)\n        \n    *   [ ]  Retrievers\n        \n        Retrievers\n        \n        *   [Auto Merging Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/)\n        *   [Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval)](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_vs_recursive_retriever/)\n        *   [Bedrock (Knowledge Bases)](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/)\n        *   [BM25 Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/)\n        *   [Composable Objects](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)\n        *   [Activeloop Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)\n        *   [Ensemble Retrieval Guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)\n        *   [Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/)\n        *   [Pathway Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/)\n        *   [Reciprocal Rerank Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/)\n        *   [Recursive Retriever + Node References + Braintrust](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/)\n        *   [Recursive Retriever + Node References](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/)\n        *   [Relative Score Fusion and Distribution-Based Score Fusion](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/)\n        *   [Router Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/router_retriever/)\n        *   [Simple Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/)\n        *   [Auto-Retrieval from a Vectara Index](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/)\n        *   [Vertex AI Search Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/vertex_ai_search_retriever/)\n        *   [Videodb retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/)\n        *   [You.com Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/you_retriever/)\n        \n    *   [ ]  Tools\n        \n        Tools\n        \n        *   [OnDemandLoaderTool Tutorial](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/)\n        *   [Azure Code Interpreter Tool Spec](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/)\n        *   [Cassandra Database Tools](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/)\n        *   [Evaluation Query Engine Tool](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/)\n        \n    *   [ ]  Transforms\n        \n        Transforms\n        \n        *   [Transforms Evaluation](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/)\n        \n    *   [ ]  Use Cases\n        \n        Use Cases\n        \n        *   [10K Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/)\n        *   [10Q Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/)\n        *   [Email Data Extraction](https://docs.llamaindex.ai/en/stable/examples/usecases/email_data_extraction/)\n        *   [Github Issue Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/)\n        \n    *   [ ]  Vector Stores\n        \n        Vector Stores\n        \n        *   [AWSDocDBDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AWSDocDBDemo/)\n        *   [Alibaba Cloud OpenSearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/)\n        *   [Amazon Neptune - Neptune Analytics vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/)\n        *   [AnalyticDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/)\n        *   [Astra DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/)\n        *   [Simple Vector Store - Async Index Creation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/)\n        *   [Awadb Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/)\n        *   [Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)\n        *   [Azure CosmosDB MongoDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/)\n        *   [Azure Cosmos DB No SQL Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBNoSqlDemo/)\n        *   [Bagel Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelAutoRetriever/)\n        *   [Bagel Network](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/)\n        *   [Baidu VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/)\n        *   [Cassandra Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CassandraIndexDemo/)\n        *   [Chroma + Fireworks + Nomic with Matryoshka embedding](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaFireworksNomic/)\n        *   [Chroma](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/)\n        *   [ClickHouse Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/)\n        *   [CouchbaseVectorStoreDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/)\n        *   [DashVector Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/)\n        *   [Databricks Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/)\n        *   [Deep Lake Vector Store Quickstart](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/)\n        *   [DocArray Hnsw Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/)\n        *   [DocArray InMemory Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/)\n        *   [DuckDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/)\n        *   [Elasticsearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/)\n        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Elasticsearch_demo/)\n        *   [Epsilla Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/)\n        *   [Faiss Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/)\n        *   [Firestore Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/)\n        *   [Hnswlib](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HnswlibIndexDemo/)\n        *   [Hologres](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/)\n        *   [Jaguar Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/JaguarIndexDemo/)\n        *   [Advanced RAG with temporal filters using LlamaIndex and KDB.AI vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/)\n        *   [LanceDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/)\n        *   [Lantern Vector Store (auto-retriever)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/)\n        *   [Lantern Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/)\n        *   [Lindorm](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LindormDemo/)\n        *   [Milvus Vector Store With Hybrid Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)\n        *   [Milvus Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/)\n        *   [MilvusOperatorFunctionDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/)\n        *   [MongoDB Atlas Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/)\n        *   [MongoDB Atlas + Fireworks AI RAG Example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGFireworks/)\n        *   [MongoDB Atlas + OpenAI RAG Example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGOpenAI/)\n        *   [MyScale Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/)\n        *   [Neo4j vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/)\n        *   [Nile Vector Store (Multi-tenant PostgreSQL)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/NileVectorStore/)\n        *   [ObjectBox VectorStore Demo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ObjectBoxIndexDemo/)\n        *   [OceanBase Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OceanBaseVectorStore/)\n        *   [Opensearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)\n        *   [pgvecto.rs](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/)\n        *   [Pinecone Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)\n        *   [Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/)\n        *   [Qdrant Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/)\n        *   [Qdrant Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_metadata_filter/)\n        *   [Qdrant Vector Store - Default Qdrant Filters](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_using_qdrant_filters/)\n        *   [Redis Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/)\n        *   [Relyt](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/)\n        *   [Rockset Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/)\n        *   [Simple Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemo/)\n        *   [Local Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/)\n        *   [Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/)\n        *   [Simple Vector Stores - Maximum Marginal Relevance Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoMMR/)\n        *   [S3/R2 Storage](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexOnS3/)\n        *   [Supabase Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/)\n        *   [TablestoreVectorStore](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TablestoreDemo/)\n        *   [Tair Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/)\n        *   [Tencent Cloud VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TencentVectorDBIndexDemo/)\n        *   [TiDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/)\n        *   [Timescale Vector Store (PostgreSQL)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Timescalevector/)\n        *   [txtai Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TxtaiIndexDemo/)\n        *   [Typesense Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/)\n        *   [Upstash Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/)\n        *   [VearchDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/)\n        *   [Google Vertex AI Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/)\n        *   [Vespa Vector Store demo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/)\n        *   [Weaviate Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)\n        *   [Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/)\n        *   [Auto-Retrieval from a Weaviate Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/)\n        *   [Weaviate Vector Store Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_metadata_filter/)\n        *   [WordLift Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WordLiftDemo/)\n        *   [Zep Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/)\n        *   [Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_auto_retriever/)\n        *   [Chroma Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/)\n        *   [Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/)\n        *   [Guide: Using Vector Store Index with Existing Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/)\n        *   [Guide: Using Vector Store Index with Existing Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/)\n        *   [Neo4j Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/neo4j_metadata_filter/)\n        *   [Oracle AI Vector Search: Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/orallamavs/)\n        *   [A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/)\n        *   [Pinecone Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/)\n        *   [Postgres Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/)\n        *   [Hybrid Search with Qdrant BM42](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/)\n        *   [Qdrant Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/)\n        \n    *   [ ]  Workflow\n        \n        Workflow\n        \n        *   [JSONalyze Query Engine](https://docs.llamaindex.ai/en/stable/examples/workflow/JSONalyze_query_engine/)\n        *   [Workflows for Advanced Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/workflow/advanced_text_to_sql/)\n        *   [None](https://docs.llamaindex.ai/en/stable/examples/workflow/auto_retrieval.ipynb)\n        *   [Checkpointing Workflow Runs](https://docs.llamaindex.ai/en/stable/examples/workflow/checkpointing_workflows/)\n        *   [Build RAG with in-line citations](https://docs.llamaindex.ai/en/stable/examples/workflow/citation_query_engine/)\n        *   [Corrective RAG Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/corrective_rag_pack/)\n        *   [Workflow for a Function Calling Agent](https://docs.llamaindex.ai/en/stable/examples/workflow/function_calling_agent/)\n        *   [Choose Your Own Adventure Workflow (Human In The Loop)](https://docs.llamaindex.ai/en/stable/examples/workflow/human_in_the_loop_story_crafting/)\n        *   [LongRAG Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/long_rag_pack/)\n        *   [MultiStep Query Engine](https://docs.llamaindex.ai/en/stable/examples/workflow/multi_step_query_engine/)\n        *   [Multi-strategy workflow with reflection](https://docs.llamaindex.ai/en/stable/examples/workflow/multi_strategy_workflow/)\n        *   [Parallel Execution of Same Event Example](https://docs.llamaindex.ai/en/stable/examples/workflow/parallel_execution/)\n        *   [Query Planning Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/planning_workflow/)\n        *   [RAG Workflow with Reranking](https://docs.llamaindex.ai/en/stable/examples/workflow/rag/)\n        *   [Workflow for a ReAct Agent](https://docs.llamaindex.ai/en/stable/examples/workflow/react_agent/)\n        *   [Reflection Workflow for Structured Outputs](https://docs.llamaindex.ai/en/stable/examples/workflow/reflection/)\n        *   [Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/workflow/router_query_engine/)\n        *   [Self-Discover Workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/self_discover_workflow/)\n        *   [Sub Question Query Engine as a workflow](https://docs.llamaindex.ai/en/stable/examples/workflow/sub_question_query_engine/)\n        *   [Workflows cookbook: walking through all features of Workflows](https://docs.llamaindex.ai/en/stable/examples/workflow/workflows_cookbook/)\n        \n    \n*   [ ] \n    \n    [Component Guides](https://docs.llamaindex.ai/en/stable/module_guides/)\n    \n    Component Guides\n    \n    *   [ ] \n        \n        [Models](https://docs.llamaindex.ai/en/stable/module_guides/models/)\n        \n        Models\n        \n        *   [ ]  LLMs\n            \n            LLMs\n            \n            *   [Using LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/)\n            *   [Standalone Usage](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_standalone/)\n            *   [Customizing LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/)\n            *   [Available LLM Integrations](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/modules/)\n            \n        *   [Embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/)\n        *   [Multi Modal](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/)\n        \n    *   [ ] \n        \n        [Prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/)\n        \n        Prompts\n        \n        *   [Usage pattern](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/usage_pattern/)\n        \n    *   [ ] \n        \n        [Loading](https://docs.llamaindex.ai/en/stable/module_guides/loading/)\n        \n        Loading\n        \n        *   [ ] \n            \n            [Documents and Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/)\n            \n            Documents and Nodes\n            \n            *   [Using Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/)\n            *   [Using Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/)\n            *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/)\n            \n        *   [SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/)\n        *   [ ] \n            \n            [Data Connectors](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/)\n            \n            Data Connectors\n            \n            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/)\n            *   [LlamaParse](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/)\n            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/modules/)\n            \n        *   [ ] \n            \n            [Node Parsers / Text Splitters](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/)\n            \n            Node Parsers / Text Splitters\n            \n            *   [Node Parser Modules](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/)\n            \n        *   [ ] \n            \n            [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/)\n            \n            Ingestion Pipeline\n            \n            *   [Transformations](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/)\n            \n        \n    *   [ ] \n        \n        [Indexing](https://docs.llamaindex.ai/en/stable/module_guides/indexing/)\n        \n        Indexing\n        \n        *   [Index Guide](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/)\n        *   [Vector Store Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/)\n        *   [Property Graph Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/)\n        *   [Document Management](https://docs.llamaindex.ai/en/stable/module_guides/indexing/document_management/)\n        *   [LlamaCloud](https://docs.llamaindex.ai/en/stable/module_guides/indexing/llama_cloud_index/)\n        *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/module_guides/indexing/metadata_extraction/)\n        *   [Modules](https://docs.llamaindex.ai/en/stable/module_guides/indexing/modules/)\n        \n    *   [ ] \n        \n        [Storing](https://docs.llamaindex.ai/en/stable/module_guides/storing/)\n        \n        Storing\n        \n        *   [Vector Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/)\n        *   [Document Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/)\n        *   [Index Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/)\n        *   [Chat Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/)\n        *   [Key-Value Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/kv_stores/)\n        *   [Persisting & Loading Data](https://docs.llamaindex.ai/en/stable/module_guides/storing/save_load/)\n        *   [Customizing Storage](https://docs.llamaindex.ai/en/stable/module_guides/storing/customization/)\n        \n    *   [ ] \n        \n        [Querying](https://docs.llamaindex.ai/en/stable/module_guides/querying/)\n        \n        Querying\n        \n        *   [ ] \n            \n            [Query Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)\n            \n            Query Engines\n            \n            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/)\n            *   [Response Modes](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/response_modes/)\n            *   [Streaming](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/)\n            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/modules/)\n            *   [Supporting Modules](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/supporting_modules/)\n            \n        *   [ ] \n            \n            [Chat Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/)\n            \n            Chat Engines\n            \n            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/usage_pattern/)\n            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/modules/)\n            \n        *   [ ] \n            \n            [Retrieval](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/)\n            \n            Retrieval\n            \n            *   [Retriever Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/)\n            *   [Retriever Modes](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/)\n            \n        *   [ ] \n            \n            [Node Postprocessors](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/)\n            \n            Node Postprocessors\n            \n            *   [Node Postprocessor Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/node_postprocessors/)\n            \n        *   [ ] \n            \n            [Response Synthesis](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/)\n            \n            Response Synthesis\n            \n            *   [Response Synthesis Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/)\n            \n        *   [Routing](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/)\n        *   [Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)\n        *   [ ] \n            \n            [Query Pipelines (Deprecated)](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/)\n            \n            Query Pipelines (Deprecated)\n            \n            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/)\n            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/modules/)\n            *   [Module Usage](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/)\n            \n        *   [ ] \n            \n            [Structured Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/)\n            \n            Structured Outputs\n            \n            *   [Output Parsing Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser/)\n            *   [(Deprecated) Query Engines + Pydantic Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/query_engine/)\n            *   [Pydantic Programs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/)\n            \n        \n    *   [ ] \n        \n        [Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)\n        \n        Agents\n        \n        *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/)\n        *   [Lower-Level Agent API](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/agent_runner/)\n        *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/modules/)\n        *   [Tools](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)\n        \n    *   [ ] \n        \n        [Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)\n        \n        Workflows\n        \n    *   [ ] \n        \n        [Evaluation](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/)\n        \n        Evaluation\n        \n        *   [Usage Pattern (Response Evaluation)](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern/)\n        *   [Usage Pattern (Retrieval)](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/)\n        *   [Modules](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/modules/)\n        *   [ ]  LlamaDatasets\n            \n            LlamaDatasets\n            \n            *   [Contributing A LabelledRagDataset](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/contributing_llamadatasets/)\n            *   [Evaluating With LabelledRagDataset's](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/evaluating_with_llamadatasets/)\n            *   [Evaluating Evaluators with LabelledEvaluatorDataset's](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/evaluating_evaluators_with_llamadatasets/)\n            \n        \n    *   [ ] \n        \n        [Observability](https://docs.llamaindex.ai/en/stable/module_guides/observability/)\n        \n        Observability\n        \n        *   [Instrumentation](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/)\n        \n    *   [Settings](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/)\n    *   [ ] \n        \n        [Llama Deploy](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/)\n        \n        Llama Deploy\n        \n        *   [Getting Started](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/10_getting_started/)\n        *   [Core Components](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/)\n        *   [Manual orchestration](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/)\n        *   [Python SDK](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/)\n        *   [CLI](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/)\n        \n    \n*   [ ]  Advanced Topics\n    \n    Advanced Topics\n    \n    *   [Building Performant RAG Applications for Production](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)\n    *   [Basic Strategies](https://docs.llamaindex.ai/en/stable/optimizing/basic_strategies/basic_strategies/)\n    *   [Agentic strategies](https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/)\n    *   [ ]  Retrieval\n        \n        Retrieval\n        \n        *   [Advanced Retrieval Strategies](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/)\n        *   [Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)\n        \n    *   [ ]  Evaluation\n        \n        Evaluation\n        \n        *   [Component Wise Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/component_wise_evaluation/)\n        *   [End-to-End Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/e2e_evaluation/)\n        *   [Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/evaluation/)\n        \n    *   [Fine-Tuning](https://docs.llamaindex.ai/en/stable/optimizing/fine-tuning/fine-tuning/)\n    *   [Writing Custom Modules](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/)\n    *   [Building RAG from Scratch (Lower-Level)](https://docs.llamaindex.ai/en/stable/optimizing/building_rag_from_scratch/)\n    \n*   [ ] \n    \n    [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/)\n    \n    API Reference\n    \n    *   [ ] \n        \n        [Agents](https://docs.llamaindex.ai/en/stable/api_reference/agent/)\n        \n        Agents\n        \n        *   [Coa](https://docs.llamaindex.ai/en/stable/api_reference/agent/coa/)\n        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/agent/dashscope/)\n        *   [Introspective](https://docs.llamaindex.ai/en/stable/api_reference/agent/introspective/)\n        *   [Lats](https://docs.llamaindex.ai/en/stable/api_reference/agent/lats/)\n        *   [Llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/)\n        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/)\n        *   [Openai legacy](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/)\n        *   [React](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/)\n        \n    *   [ ] \n        \n        [Callbacks](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/)\n        \n        Callbacks\n        \n        *   [Agentops](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/agentops/)\n        *   [Aim](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/)\n        *   [Argilla](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/argilla/)\n        *   [Arize phoenix](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/arize_phoenix/)\n        *   [Deepeval](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/deepeval/)\n        *   [Honeyhive](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/honeyhive/)\n        *   [Langfuse](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/langfuse/)\n        *   [Literalai](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/literalai/)\n        *   [Llama debug](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/)\n        *   [Openinference](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/opentelemetry.md)\n        *   [Opik](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/opik/)\n        *   [Promptlayer](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/promptlayer/)\n        *   [Token counter](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/)\n        *   [Uptrain](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/)\n        *   [Wandb](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/)\n        \n    *   [ ] \n        \n        [Chat Engines](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/)\n        \n        Chat Engines\n        \n        *   [Condense plus context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_plus_context/)\n        *   [Condense question](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/)\n        *   [Context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/)\n        *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/)\n        \n    *   [ ] \n        \n        [Embeddings](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/)\n        \n        Embeddings\n        \n        *   [Adapter](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/)\n        *   [Alephalpha](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/alephalpha/)\n        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/alibabacloud_aisearch/)\n        *   [Anyscale](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/anyscale/)\n        *   [Azure inference](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/azure_inference/)\n        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/azure_openai/)\n        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/bedrock/)\n        *   [Clarifai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/clarifai/)\n        *   [Clip](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/clip/)\n        *   [Cloudflare workersai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/cloudflare_workersai/)\n        *   [Cohere](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/cohere/)\n        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/dashscope/)\n        *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/databricks/)\n        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/deepinfra/)\n        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/elasticsearch/)\n        *   [Fastembed](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/fastembed/)\n        *   [Fireworks](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/fireworks/)\n        *   [Gaudi](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gaudi/)\n        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gemini/)\n        *   [Gigachat](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gigachat/)\n        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/google/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gradient.md)\n        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface/)\n        *   [Huggingface api](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_api/)\n        *   [Huggingface openvino](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_openvino/)\n        *   [Huggingface optimum](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_optimum/)\n        *   [Huggingface optimum intel](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_optimum_intel/)\n        *   [Ibm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ibm/)\n        *   [Instructor](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/instructor/)\n        *   [Ipex llm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ipex_llm/)\n        *   [Jinaai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/jinaai/)\n        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/langchain/)\n        *   [Litellm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/litellm/)\n        *   [Llamafile](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/llamafile/)\n        *   [Llm rails](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/llm_rails/)\n        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/mistralai/)\n        *   [Mixedbreadai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/mixedbreadai/)\n        *   [Modelscope](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/modelscope/)\n        *   [Nebius](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nebius/)\n        *   [Nomic](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nomic/)\n        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nvidia/)\n        *   [Oci genai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/oci_genai/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/octoai.md)\n        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ollama/)\n        *   [Opea](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/opea/)\n        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/openai/)\n        *   [Oracleai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/oracleai/)\n        *   [Premai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/premai/)\n        *   [Sagemaker endpoint](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/sagemaker_endpoint/)\n        *   [Siliconflow](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/siliconflow/)\n        *   [Text embeddings inference](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/text_embeddings_inference/)\n        *   [Textembed](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/textembed/)\n        *   [Together](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/together/)\n        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/upstage/)\n        *   [Vertex](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/vertex/)\n        *   [Vertex endpoint](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/vertex_endpoint/)\n        *   [Voyageai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/voyageai/)\n        *   [Xinference](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/xinference/)\n        *   [Yandexgpt](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/yandexgpt/)\n        *   [Zhipuai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/zhipuai/)\n        \n    *   [ ] \n        \n        [Evaluation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/)\n        \n        Evaluation\n        \n        *   [Answer relevancy](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/answer_relevancy/)\n        *   [Context relevancy](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/context_relevancy/)\n        *   [Correctness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/correctness/)\n        *   [Dataset generation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/)\n        *   [Faithfullness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/)\n        *   [Guideline](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/)\n        *   [Metrics](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/)\n        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/multi_modal/)\n        *   [Pairwise comparison](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/pairwise_comparison/)\n        *   [Query response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/query_response/)\n        *   [Response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/response/)\n        *   [Retrieval](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/)\n        *   [Semantic similarity](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/semantic_similarity/)\n        *   [Tonic validate](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/)\n        \n    *   [ ]  Graph RAG\n        \n        Graph RAG\n        \n        *   [Cognee](https://docs.llamaindex.ai/en/stable/api_reference/graph_rag/cognee/)\n        \n    *   [ ] \n        \n        [Indexes](https://docs.llamaindex.ai/en/stable/api_reference/indices/)\n        \n        Indexes\n        \n        *   [Bge m3](https://docs.llamaindex.ai/en/stable/api_reference/indices/bge_m3/)\n        *   [Colbert](https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/)\n        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/)\n        *   [Document summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/)\n        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/)\n        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/)\n        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/)\n        *   [Llama cloud](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/)\n        *   [Postgresml](https://docs.llamaindex.ai/en/stable/api_reference/indices/postgresml/)\n        *   [Property graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/)\n        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/)\n        *   [Tree](https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/)\n        *   [Vectara](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/)\n        *   [Vector](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/)\n        *   [Vertexai](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/)\n        *   [Zilliz](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/)\n        \n    *   [ ] \n        \n        [Ingestion](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/)\n        \n        Ingestion\n        \n    *   [ ] \n        \n        [Instrumentation](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/)\n        \n        Instrumentation\n        \n        *   [Event handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/)\n        *   [Event types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/)\n        *   [Span handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/)\n        *   [Span types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_types/)\n        \n    *   [ ] \n        \n        [LLMs](https://docs.llamaindex.ai/en/stable/api_reference/llms/)\n        \n        LLMs\n        \n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/OptimumIntelLLM.md)\n        *   [Ai21](https://docs.llamaindex.ai/en/stable/api_reference/llms/ai21/)\n        *   [Alephalpha](https://docs.llamaindex.ai/en/stable/api_reference/llms/alephalpha/)\n        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/llms/alibabacloud_aisearch/)\n        *   [Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/llms/anthropic/)\n        *   [Anyscale](https://docs.llamaindex.ai/en/stable/api_reference/llms/anyscale/)\n        *   [Azure inference](https://docs.llamaindex.ai/en/stable/api_reference/llms/azure_inference/)\n        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/llms/azure_openai/)\n        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/llms/bedrock/)\n        *   [Bedrock converse](https://docs.llamaindex.ai/en/stable/api_reference/llms/bedrock_converse/)\n        *   [Cerebras](https://docs.llamaindex.ai/en/stable/api_reference/llms/cerebras/)\n        *   [Clarifai](https://docs.llamaindex.ai/en/stable/api_reference/llms/clarifai/)\n        *   [Cleanlab](https://docs.llamaindex.ai/en/stable/api_reference/llms/cleanlab/)\n        *   [Cohere](https://docs.llamaindex.ai/en/stable/api_reference/llms/cohere/)\n        *   [Custom llm](https://docs.llamaindex.ai/en/stable/api_reference/llms/custom_llm/)\n        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/llms/dashscope/)\n        *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/llms/databricks/)\n        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/api_reference/llms/deepinfra/)\n        *   [Everlyai](https://docs.llamaindex.ai/en/stable/api_reference/llms/everlyai/)\n        *   [Fireworks](https://docs.llamaindex.ai/en/stable/api_reference/llms/fireworks/)\n        *   [Friendli](https://docs.llamaindex.ai/en/stable/api_reference/llms/friendli/)\n        *   [Gaudi](https://docs.llamaindex.ai/en/stable/api_reference/llms/gaudi/)\n        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/llms/gemini/)\n        *   [Gigachat](https://docs.llamaindex.ai/en/stable/api_reference/llms/gigachat/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/gradient.md)\n        *   [Groq](https://docs.llamaindex.ai/en/stable/api_reference/llms/groq/)\n        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/llms/huggingface/)\n        *   [Huggingface api](https://docs.llamaindex.ai/en/stable/api_reference/llms/huggingface_api/)\n        *   [Ibm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ibm/)\n        *   [Ipex llm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ipex_llm/)\n        *   [Keywordsai](https://docs.llamaindex.ai/en/stable/api_reference/llms/keywordsai/)\n        *   [Konko](https://docs.llamaindex.ai/en/stable/api_reference/llms/konko/)\n        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/llms/langchain/)\n        *   [Litellm](https://docs.llamaindex.ai/en/stable/api_reference/llms/litellm/)\n        *   [Llama api](https://docs.llamaindex.ai/en/stable/api_reference/llms/llama_api/)\n        *   [Llama cpp](https://docs.llamaindex.ai/en/stable/api_reference/llms/llama_cpp/)\n        *   [Llamafile](https://docs.llamaindex.ai/en/stable/api_reference/llms/llamafile/)\n        *   [Lmstudio](https://docs.llamaindex.ai/en/stable/api_reference/llms/lmstudio/)\n        *   [Localai](https://docs.llamaindex.ai/en/stable/api_reference/llms/localai/)\n        *   [Maritalk](https://docs.llamaindex.ai/en/stable/api_reference/llms/maritalk/)\n        *   [Mistral rs](https://docs.llamaindex.ai/en/stable/api_reference/llms/mistral_rs/)\n        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/llms/mistralai/)\n        *   [Mlx](https://docs.llamaindex.ai/en/stable/api_reference/llms/mlx/)\n        *   [Modelscope](https://docs.llamaindex.ai/en/stable/api_reference/llms/modelscope/)\n        *   [Monsterapi](https://docs.llamaindex.ai/en/stable/api_reference/llms/monsterapi/)\n        *   [Mymagic](https://docs.llamaindex.ai/en/stable/api_reference/llms/mymagic/)\n        *   [Nebius](https://docs.llamaindex.ai/en/stable/api_reference/llms/nebius/)\n        *   [Neutrino](https://docs.llamaindex.ai/en/stable/api_reference/llms/neutrino/)\n        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia/)\n        *   [Nvidia tensorrt](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia_tensorrt/)\n        *   [Nvidia triton](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia_triton/)\n        *   [Oci genai](https://docs.llamaindex.ai/en/stable/api_reference/llms/oci_genai/)\n        *   [Octoai](https://docs.llamaindex.ai/en/stable/api_reference/llms/octoai/)\n        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/llms/ollama/)\n        *   [Opea](https://docs.llamaindex.ai/en/stable/api_reference/llms/opea/)\n        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai/)\n        *   [Openai like](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai_like/)\n        *   [Openllm](https://docs.llamaindex.ai/en/stable/api_reference/llms/openllm/)\n        *   [Openrouter](https://docs.llamaindex.ai/en/stable/api_reference/llms/openrouter/)\n        *   [Openvino](https://docs.llamaindex.ai/en/stable/api_reference/llms/openvino/)\n        *   [Optimum intel](https://docs.llamaindex.ai/en/stable/api_reference/llms/optimum_intel/)\n        *   [Paieas](https://docs.llamaindex.ai/en/stable/api_reference/llms/paieas/)\n        *   [Palm](https://docs.llamaindex.ai/en/stable/api_reference/llms/palm/)\n        *   [Perplexity](https://docs.llamaindex.ai/en/stable/api_reference/llms/perplexity/)\n        *   [Pipeshift](https://docs.llamaindex.ai/en/stable/api_reference/llms/pipeshift/)\n        *   [Portkey](https://docs.llamaindex.ai/en/stable/api_reference/llms/portkey/)\n        *   [Predibase](https://docs.llamaindex.ai/en/stable/api_reference/llms/predibase/)\n        *   [Premai](https://docs.llamaindex.ai/en/stable/api_reference/llms/premai/)\n        *   [Qianfan](https://docs.llamaindex.ai/en/stable/api_reference/llms/qianfan/)\n        *   [Reka](https://docs.llamaindex.ai/en/stable/api_reference/llms/reka/)\n        *   [Replicate](https://docs.llamaindex.ai/en/stable/api_reference/llms/replicate/)\n        *   [Rungpt](https://docs.llamaindex.ai/en/stable/api_reference/llms/rungpt/)\n        *   [Sagemaker endpoint](https://docs.llamaindex.ai/en/stable/api_reference/llms/sagemaker_endpoint/)\n        *   [Sambanovasystems](https://docs.llamaindex.ai/en/stable/api_reference/llms/sambanovasystems/)\n        *   [Siliconflow](https://docs.llamaindex.ai/en/stable/api_reference/llms/siliconflow/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/solar.md)\n        *   [Text generation inference](https://docs.llamaindex.ai/en/stable/api_reference/llms/text_generation_inference/)\n        *   [Together](https://docs.llamaindex.ai/en/stable/api_reference/llms/together/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/unify.md)\n        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/llms/upstage/)\n        *   [Vertex](https://docs.llamaindex.ai/en/stable/api_reference/llms/vertex/)\n        *   [Vllm](https://docs.llamaindex.ai/en/stable/api_reference/llms/vllm/)\n        *   [Xinference](https://docs.llamaindex.ai/en/stable/api_reference/llms/xinference/)\n        *   [Yi](https://docs.llamaindex.ai/en/stable/api_reference/llms/yi/)\n        *   [You](https://docs.llamaindex.ai/en/stable/api_reference/llms/you/)\n        *   [Zhipuai](https://docs.llamaindex.ai/en/stable/api_reference/llms/zhipuai/)\n        \n    *   [ ] \n        \n        [Llama Datasets](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/)\n        \n        Llama Datasets\n        \n    *   [ ]  Llama Deploy\n        \n        Llama Deploy\n        \n        *   [apiserver](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/apiserver/)\n        *   [control\\_plane](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/control_plane/)\n        *   [deploy](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/deploy/)\n        *   [message\\_consumers](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_consumers/)\n        *   [message\\_publishers](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_publishers/)\n        *   [messages](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/messages/)\n        *   [orchestrators](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/orchestrators/)\n        *   [Python SDK](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/python_sdk/)\n        *   [services](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/services/)\n        *   [types](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/types/)\n        *   [ ] \n            \n            [message\\_queues](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/)\n            \n            message\\_queues\n            \n            *   [apache\\_kafka](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/kafka/)\n            *   [rabbitmq](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/rabbitmq/)\n            *   [redis](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/redis/)\n            *   [simple](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/message_queues/simple/)\n            \n        \n    *   [ ] \n        \n        [Llama Packs](https://docs.llamaindex.ai/en/stable/api_reference/packs/)\n        \n        Llama Packs\n        \n        *   [Agent search retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/agent_search_retriever/)\n        *   [Agents coa](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/)\n        *   [Agents lats](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/)\n        *   [Agents llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/)\n        *   [Amazon product extraction](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/)\n        *   [Arize phoenix query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/)\n        *   [Auto merging retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/)\n        *   [Chroma autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/chroma_autoretrieval/)\n        *   [Code hierarchy](https://docs.llamaindex.ai/en/stable/api_reference/packs/code_hierarchy/)\n        *   [Cogniswitch agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/)\n        *   [Cohere citation chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/)\n        *   [Corrective rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/)\n        *   [Deeplake deepmemory retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/)\n        *   [Deeplake multimodal retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_multimodal_retrieval/)\n        *   [Dense x retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/)\n        *   [Diff private simple dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/)\n        *   [Evaluator benchmarker](https://docs.llamaindex.ai/en/stable/api_reference/packs/evaluator_benchmarker/)\n        *   [Fusion retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/)\n        *   [Fuzzy citation](https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/)\n        *   [Gmail openai agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/gmail_openai_agent/)\n        *   [Gradio agent chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_agent_chat/)\n        *   [Gradio react agent chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_react_agent_chatbot/)\n        *   [Infer retrieve rerank](https://docs.llamaindex.ai/en/stable/api_reference/packs/infer_retrieve_rerank/)\n        *   [Koda retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/koda_retriever/)\n        *   [Llama dataset metadata](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_dataset_metadata/)\n        *   [Llama guard moderator](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/)\n        *   [Llava completion](https://docs.llamaindex.ai/en/stable/api_reference/packs/llava_completion/)\n        *   [Longrag](https://docs.llamaindex.ai/en/stable/api_reference/packs/longrag/)\n        *   [Mixture of agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/)\n        *   [Multi document agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/)\n        *   [Multi tenancy rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/)\n        *   [Multidoc autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/)\n        *   [Nebulagraph query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/)\n        *   [Neo4j query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/neo4j_query_engine/)\n        *   [Node parser semantic chunking](https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/)\n        *   [Ollama query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/)\n        *   [Panel chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/panel_chatbot/)\n        *   [Query understanding agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/query_understanding_agent/)\n        *   [Raft dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/)\n        *   [Rag cli local](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/)\n        *   [Rag evaluator](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_evaluator/)\n        *   [Rag fusion query pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/)\n        *   [Ragatouille retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/)\n        *   [Raptor](https://docs.llamaindex.ai/en/stable/api_reference/packs/raptor/)\n        *   [Recursive retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/)\n        *   [Resume screener](https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/)\n        *   [Retry engine weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/retry_engine_weaviate/)\n        *   [Secgpt](https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/)\n        *   [Self discover](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/)\n        *   [Self rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_rag/)\n        *   [Sentence window retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/sentence_window_retriever/)\n        *   [Snowflake query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/)\n        *   [Stock market data query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/)\n        *   [Streamlit chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/)\n        *   [Sub question weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/sub_question_weaviate/)\n        *   [Tables](https://docs.llamaindex.ai/en/stable/api_reference/packs/tables/)\n        *   [Timescale vector autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/timescale_vector_autoretrieval/)\n        *   [Trulens eval packs](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/packs/vanna.md)\n        *   [Vectara rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/vectara_rag/)\n        *   [Voyage query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/voyage_query_engine/)\n        *   [Zenguard](https://docs.llamaindex.ai/en/stable/api_reference/packs/zenguard/)\n        *   [Zephyr query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/)\n        \n    *   [ ] \n        \n        [Memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/)\n        \n        Memory\n        \n        *   [Chat memory buffer](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/)\n        *   [Mem0](https://docs.llamaindex.ai/en/stable/api_reference/memory/mem0/)\n        *   [Simple composable memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/)\n        *   [Vector memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/)\n        \n    *   [ ] \n        \n        [Metadata Extractors](https://docs.llamaindex.ai/en/stable/api_reference/extractors/)\n        \n        Metadata Extractors\n        \n        *   [Entity](https://docs.llamaindex.ai/en/stable/api_reference/extractors/entity/)\n        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/extractors/keyword/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/extractors/llama_extract.md)\n        *   [Marvin](https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/)\n        *   [Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/)\n        *   [Question](https://docs.llamaindex.ai/en/stable/api_reference/extractors/question/)\n        *   [Relik](https://docs.llamaindex.ai/en/stable/api_reference/extractors/relik/)\n        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/extractors/summary/)\n        *   [Title](https://docs.llamaindex.ai/en/stable/api_reference/extractors/title/)\n        \n    *   [ ] \n        \n        [Multi-Modal LLMs](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/)\n        \n        Multi-Modal LLMs\n        \n        *   [Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/anthropic/)\n        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/azure_openai/)\n        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/bedrock/)\n        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/dashscope/)\n        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/gemini/)\n        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/huggingface/)\n        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/mistralai/)\n        *   [Nebius](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/nebius/)\n        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/nvidia/)\n        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/)\n        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/)\n        *   [Openvino](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openvino/)\n        *   [Reka](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/reka/)\n        *   [Replicate](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/)\n        *   [Zhipuai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/zhipuai/)\n        \n    *   [ ] \n        \n        [Node Parsers & Text Splitters](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/)\n        \n        Node Parsers & Text Splitters\n        \n        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/alibabacloud_aisearch/)\n        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/)\n        *   [Docling](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/docling/)\n        *   [Topic](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/topic/)\n        *   [Code](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/)\n        *   [Hierarchical](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/)\n        *   [Html](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/html/)\n        *   [Json](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/)\n        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/langchain/)\n        *   [Markdown](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown/)\n        *   [Markdown element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown_element/)\n        *   [Semantic splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/)\n        *   [Sentence splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/)\n        *   [Sentence window](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/)\n        *   [Token text splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/)\n        *   [Unstructured element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/)\n        \n    *   [ ] \n        \n        [Node Postprocessors](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/)\n        \n        Node Postprocessors\n        \n        *   [NER PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/NER_PII/)\n        *   [PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/PII/)\n        *   [Alibabacloud aisearch rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/alibabacloud_aisearch_rerank/)\n        *   [Auto prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/auto_prev_next/)\n        *   [Bedrock rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/bedrock_rerank/)\n        *   [Cohere rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/cohere_rerank/)\n        *   [Colbert rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/colbert_rerank/)\n        *   [Colpali rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/colpali_rerank/)\n        *   [Dashscope rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/dashscope_rerank/)\n        *   [Embedding recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/embedding_recency/)\n        *   [Fixed recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/fixed_recency/)\n        *   [Flag embedding reranker](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/flag_embedding_reranker/)\n        *   [Jinaai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/jinaai_rerank/)\n        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/keyword/)\n        *   [Llm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/llm_rerank/)\n        *   [Long context reorder](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/long_context_reorder/)\n        *   [Longllmlingua](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/longllmlingua/)\n        *   [Metadata replacement](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/metadata_replacement/)\n        *   [Mixedbreadai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/mixedbreadai_rerank/)\n        *   [Nvidia rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/nvidia_rerank/)\n        *   [Openvino rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/openvino_rerank/)\n        *   [Pinecone native rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/pinecone_native_rerank/)\n        *   [Presidio](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/presidio/)\n        *   [Prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/prev_next/)\n        *   [Rankgpt rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankgpt_rerank/)\n        *   [Rankllm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankllm_rerank/)\n        *   [Sbert rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sbert_rerank/)\n        *   [Sentence optimizer](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sentence_optimizer/)\n        *   [Siliconflow rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/siliconflow_rerank/)\n        *   [Similarity](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/similarity/)\n        *   [Tei rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/tei_rerank/)\n        *   [Time weighted](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/time_weighted/)\n        *   [Voyageai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/voyageai_rerank/)\n        *   [Xinference rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/xinference_rerank/)\n        \n    *   [ ] \n        \n        [Object Stores](https://docs.llamaindex.ai/en/stable/api_reference/objects/)\n        \n        Object Stores\n        \n    *   [ ] \n        \n        [Output Parsers](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/)\n        \n        Output Parsers\n        \n        *   [Guardrails](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/)\n        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/)\n        *   [Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/)\n        *   [Selection](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/selection/)\n        \n    *   [ ] \n        \n        [Programs](https://docs.llamaindex.ai/en/stable/api_reference/program/)\n        \n        Programs\n        \n        *   [Evaporate](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/)\n        *   [Guidance](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/)\n        *   [Llm text completion](https://docs.llamaindex.ai/en/stable/api_reference/program/llm_text_completion/)\n        *   [Lmformatenforcer](https://docs.llamaindex.ai/en/stable/api_reference/program/lmformatenforcer/)\n        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/program/multi_modal/)\n        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/program/openai/)\n        \n    *   [ ] \n        \n        [Prompts](https://docs.llamaindex.ai/en/stable/api_reference/prompts/)\n        \n        Prompts\n        \n    *   [ ] \n        \n        [Query Engines](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/)\n        \n        Query Engines\n        \n        *   [FLARE](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/FLARE/)\n        *   [JSONalayze](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/JSONalayze/)\n        *   [NL SQL table](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/)\n        *   [PGVector SQL](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/)\n        *   [SQL join](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/)\n        *   [SQL table retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/)\n        *   [Citation](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/)\n        *   [Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/cogniswitch/)\n        *   [Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/)\n        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/)\n        *   [Multi step](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/multi_step/)\n        *   [Pandas](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/pandas/)\n        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/)\n        *   [Retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever_router/)\n        *   [Retry](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/)\n        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/)\n        *   [Simple multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/)\n        *   [Sub question](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/)\n        *   [Tool retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/tool_retriever_router/)\n        *   [Transform](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/transform/)\n        \n    *   [ ] \n        \n        [Query Pipeline](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/)\n        \n        Query Pipeline\n        \n        *   [Agent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/)\n        *   [Arg pack](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/arg_pack/)\n        *   [Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/)\n        *   [Function](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/)\n        *   [Input](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/input/)\n        *   [Llm](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/)\n        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/multi_modal/)\n        *   [Object](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/object/)\n        *   [Output parser](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/output_parser/)\n        *   [Postprocessor](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/postprocessor/)\n        *   [Prompt](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/prompt/)\n        *   [Query engine](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/query_engine/)\n        *   [Query transform](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/query_transform/)\n        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/retriever/)\n        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/)\n        *   [Synthesizer](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/)\n        *   [Tool runner](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/tool_runner/)\n        \n    *   [ ] \n        \n        [Question Generators](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/)\n        \n        Question Generators\n        \n        *   [Guidance](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/guidance/)\n        *   [Llm question gen](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/)\n        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/openai/)\n        \n    *   [ ] \n        \n        [Readers](https://docs.llamaindex.ai/en/stable/api_reference/readers/)\n        \n        Readers\n        \n        *   [Agent search](https://docs.llamaindex.ai/en/stable/api_reference/readers/agent_search/)\n        *   [Airbyte cdk](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_cdk/)\n        *   [Airbyte gong](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_gong/)\n        *   [Airbyte hubspot](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_hubspot/)\n        *   [Airbyte salesforce](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_salesforce/)\n        *   [Airbyte shopify](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_shopify/)\n        *   [Airbyte stripe](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_stripe/)\n        *   [Airbyte typeform](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_typeform/)\n        *   [Airbyte zendesk support](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_zendesk_support/)\n        *   [Airtable](https://docs.llamaindex.ai/en/stable/api_reference/readers/airtable/)\n        *   [Alibabacloud aisearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/alibabacloud_aisearch/)\n        *   [Apify](https://docs.llamaindex.ai/en/stable/api_reference/readers/apify/)\n        *   [Arango db](https://docs.llamaindex.ai/en/stable/api_reference/readers/arango_db/)\n        *   [Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/readers/arxiv/)\n        *   [Asana](https://docs.llamaindex.ai/en/stable/api_reference/readers/asana/)\n        *   [Assemblyai](https://docs.llamaindex.ai/en/stable/api_reference/readers/assemblyai/)\n        *   [Astra db](https://docs.llamaindex.ai/en/stable/api_reference/readers/astra_db/)\n        *   [Athena](https://docs.llamaindex.ai/en/stable/api_reference/readers/athena/)\n        *   [Awadb](https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/)\n        *   [Azcognitive search](https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/)\n        *   [Azstorage blob](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/)\n        *   [Bagel](https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/)\n        *   [Bilibili](https://docs.llamaindex.ai/en/stable/api_reference/readers/bilibili/)\n        *   [Bitbucket](https://docs.llamaindex.ai/en/stable/api_reference/readers/bitbucket/)\n        *   [Boarddocs](https://docs.llamaindex.ai/en/stable/api_reference/readers/boarddocs/)\n        *   [Box](https://docs.llamaindex.ai/en/stable/api_reference/readers/box/)\n        *   [Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/readers/chatgpt_plugin/)\n        *   [Chroma](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse.md)\n        *   [Confluence](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/)\n        *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/)\n        *   [Couchdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchdb/)\n        *   [Dad jokes](https://docs.llamaindex.ai/en/stable/api_reference/readers/dad_jokes/)\n        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/)\n        *   [Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashvector/)\n        *   [Database](https://docs.llamaindex.ai/en/stable/api_reference/readers/database/)\n        *   [Deeplake](https://docs.llamaindex.ai/en/stable/api_reference/readers/deeplake/)\n        *   [Discord](https://docs.llamaindex.ai/en/stable/api_reference/readers/discord/)\n        *   [Docling](https://docs.llamaindex.ai/en/stable/api_reference/readers/docling/)\n        *   [Docstring walker](https://docs.llamaindex.ai/en/stable/api_reference/readers/docstring_walker/)\n        *   [Docugami](https://docs.llamaindex.ai/en/stable/api_reference/readers/docugami/)\n        *   [Document360](https://docs.llamaindex.ai/en/stable/api_reference/readers/document360/)\n        *   [Earnings call transcript](https://docs.llamaindex.ai/en/stable/api_reference/readers/earnings_call_transcript/)\n        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/elasticsearch/)\n        *   [Faiss](https://docs.llamaindex.ai/en/stable/api_reference/readers/faiss/)\n        *   [Feedly rss](https://docs.llamaindex.ai/en/stable/api_reference/readers/feedly_rss/)\n        *   [Feishu docs](https://docs.llamaindex.ai/en/stable/api_reference/readers/feishu_docs/)\n        *   [File](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/)\n        *   [Firebase realtimedb](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/)\n        *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/firestore/)\n        *   [Gcs](https://docs.llamaindex.ai/en/stable/api_reference/readers/gcs/)\n        *   [Genius](https://docs.llamaindex.ai/en/stable/api_reference/readers/genius/)\n        *   [Gitbook](https://docs.llamaindex.ai/en/stable/api_reference/readers/gitbook/)\n        *   [Github](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/)\n        *   [Gitlab](https://docs.llamaindex.ai/en/stable/api_reference/readers/gitlab/)\n        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/)\n        *   [Gpt repo](https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/)\n        *   [Graphdb cypher](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/)\n        *   [Graphql](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/)\n        *   [Guru](https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/)\n        *   [Hatena blog](https://docs.llamaindex.ai/en/stable/api_reference/readers/hatena_blog/)\n        *   [Hive](https://docs.llamaindex.ai/en/stable/api_reference/readers/hive/)\n        *   [Hubspot](https://docs.llamaindex.ai/en/stable/api_reference/readers/hubspot/)\n        *   [Huggingface fs](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/)\n        *   [Hwp](https://docs.llamaindex.ai/en/stable/api_reference/readers/hwp/)\n        *   [Iceberg](https://docs.llamaindex.ai/en/stable/api_reference/readers/iceberg/)\n        *   [Imdb review](https://docs.llamaindex.ai/en/stable/api_reference/readers/imdb_review/)\n        *   [Intercom](https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/)\n        *   [Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/readers/jaguar/)\n        *   [Jira](https://docs.llamaindex.ai/en/stable/api_reference/readers/jira/)\n        *   [Joplin](https://docs.llamaindex.ai/en/stable/api_reference/readers/joplin/)\n        *   [Json](https://docs.llamaindex.ai/en/stable/api_reference/readers/json/)\n        *   [Kaltura esearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/kaltura_esearch/)\n        *   [Kibela](https://docs.llamaindex.ai/en/stable/api_reference/readers/kibela/)\n        *   [Lilac](https://docs.llamaindex.ai/en/stable/api_reference/readers/lilac/)\n        *   [Linear](https://docs.llamaindex.ai/en/stable/api_reference/readers/linear/)\n        *   [Llama parse](https://docs.llamaindex.ai/en/stable/api_reference/readers/llama_parse/)\n        *   [Macrometa gdn](https://docs.llamaindex.ai/en/stable/api_reference/readers/macrometa_gdn/)\n        *   [Make com](https://docs.llamaindex.ai/en/stable/api_reference/readers/make_com/)\n        *   [Mangadex](https://docs.llamaindex.ai/en/stable/api_reference/readers/mangadex/)\n        *   [Mangoapps guides](https://docs.llamaindex.ai/en/stable/api_reference/readers/mangoapps_guides/)\n        *   [Maps](https://docs.llamaindex.ai/en/stable/api_reference/readers/maps/)\n        *   [Mbox](https://docs.llamaindex.ai/en/stable/api_reference/readers/mbox/)\n        *   [Memos](https://docs.llamaindex.ai/en/stable/api_reference/readers/memos/)\n        *   [Metal](https://docs.llamaindex.ai/en/stable/api_reference/readers/metal/)\n        *   [Microsoft onedrive](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/)\n        *   [Microsoft outlook](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/)\n        *   [Microsoft sharepoint](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/)\n        *   [Milvus](https://docs.llamaindex.ai/en/stable/api_reference/readers/milvus/)\n        *   [Minio](https://docs.llamaindex.ai/en/stable/api_reference/readers/minio/)\n        *   [Mondaydotcom](https://docs.llamaindex.ai/en/stable/api_reference/readers/mondaydotcom/)\n        *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/readers/mongodb/)\n        *   [Myscale](https://docs.llamaindex.ai/en/stable/api_reference/readers/myscale/)\n        *   [Notion](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/)\n        *   [Nougat ocr](https://docs.llamaindex.ai/en/stable/api_reference/readers/nougat_ocr/)\n        *   [Obsidian](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/)\n        *   [Openalex](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi.md)\n        *   [Opendal](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/)\n        *   [Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/)\n        *   [Oracleai](https://docs.llamaindex.ai/en/stable/api_reference/readers/oracleai/)\n        *   [Pandas ai](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/)\n        *   [Papers](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/)\n        *   [Patentsview](https://docs.llamaindex.ai/en/stable/api_reference/readers/patentsview/)\n        *   [Pathway](https://docs.llamaindex.ai/en/stable/api_reference/readers/pathway/)\n        *   [Pdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdb/)\n        *   [Pdf marker](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/)\n        *   [Pdf table](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_table/)\n        *   [Pebblo](https://docs.llamaindex.ai/en/stable/api_reference/readers/pebblo/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/pinecone.md)\n        *   [Preprocess](https://docs.llamaindex.ai/en/stable/api_reference/readers/preprocess/)\n        *   [Psychic](https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/)\n        *   [Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/readers/qdrant/)\n        *   [Quip](https://docs.llamaindex.ai/en/stable/api_reference/readers/quip/)\n        *   [Rayyan](https://docs.llamaindex.ai/en/stable/api_reference/readers/rayyan/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/readme.md)\n        *   [Readwise](https://docs.llamaindex.ai/en/stable/api_reference/readers/readwise/)\n        *   [Reddit](https://docs.llamaindex.ai/en/stable/api_reference/readers/reddit/)\n        *   [Remote](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote/)\n        *   [Remote depth](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote_depth/)\n        *   [S3](https://docs.llamaindex.ai/en/stable/api_reference/readers/s3/)\n        *   [Sec filings](https://docs.llamaindex.ai/en/stable/api_reference/readers/sec_filings/)\n        *   [Semanticscholar](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/)\n        *   [Simple directory reader](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/)\n        *   [Singlestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/singlestore/)\n        *   [Slack](https://docs.llamaindex.ai/en/stable/api_reference/readers/slack/)\n        *   [Smart pdf loader](https://docs.llamaindex.ai/en/stable/api_reference/readers/smart_pdf_loader/)\n        *   [Snowflake](https://docs.llamaindex.ai/en/stable/api_reference/readers/snowflake/)\n        *   [Spotify](https://docs.llamaindex.ai/en/stable/api_reference/readers/spotify/)\n        *   [Stackoverflow](https://docs.llamaindex.ai/en/stable/api_reference/readers/stackoverflow/)\n        *   [Steamship](https://docs.llamaindex.ai/en/stable/api_reference/readers/steamship/)\n        *   [String iterable](https://docs.llamaindex.ai/en/stable/api_reference/readers/string_iterable/)\n        *   [Stripe docs](https://docs.llamaindex.ai/en/stable/api_reference/readers/stripe_docs/)\n        *   [Structured data](https://docs.llamaindex.ai/en/stable/api_reference/readers/structured_data/)\n        *   [Telegram](https://docs.llamaindex.ai/en/stable/api_reference/readers/telegram/)\n        *   [Toggl](https://docs.llamaindex.ai/en/stable/api_reference/readers/toggl/)\n        *   [Trello](https://docs.llamaindex.ai/en/stable/api_reference/readers/trello/)\n        *   [Twitter](https://docs.llamaindex.ai/en/stable/api_reference/readers/twitter/)\n        *   [Txtai](https://docs.llamaindex.ai/en/stable/api_reference/readers/txtai/)\n        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/readers/upstage/)\n        *   [Weather](https://docs.llamaindex.ai/en/stable/api_reference/readers/weather/)\n        *   [Weaviate](https://docs.llamaindex.ai/en/stable/api_reference/readers/weaviate/)\n        *   [Web](https://docs.llamaindex.ai/en/stable/api_reference/readers/web/)\n        *   [Whatsapp](https://docs.llamaindex.ai/en/stable/api_reference/readers/whatsapp/)\n        *   [Wikipedia](https://docs.llamaindex.ai/en/stable/api_reference/readers/wikipedia/)\n        *   [Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/readers/wordlift/)\n        *   [Wordpress](https://docs.llamaindex.ai/en/stable/api_reference/readers/wordpress/)\n        *   [Youtube transcript](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_transcript/)\n        *   [Zendesk](https://docs.llamaindex.ai/en/stable/api_reference/readers/zendesk/)\n        *   [Zep](https://docs.llamaindex.ai/en/stable/api_reference/readers/zep/)\n        *   [Zulip](https://docs.llamaindex.ai/en/stable/api_reference/readers/zulip/)\n        *   [Zyte serp](https://docs.llamaindex.ai/en/stable/api_reference/readers/zyte_serp/)\n        \n    *   [ ] \n        \n        [Response Synthesizers](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/)\n        \n        Response Synthesizers\n        \n        *   [Accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/accumulate/)\n        *   [Compact accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_accumulate/)\n        *   [Compact and refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_and_refine/)\n        *   [Generation](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/generation/)\n        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/google/)\n        *   [Refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/refine/)\n        *   [Simple summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/simple_summarize/)\n        *   [Tree summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/tree_summarize/)\n        \n    *   [ ] \n        \n        [Retrievers](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/)\n        \n        Retrievers\n        \n        *   [Auto merging](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/auto_merging/)\n        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bedrock/)\n        *   [Bm25](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/)\n        *   [Duckdb retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/duckdb_retriever/)\n        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/)\n        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/knowledge_graph/)\n        *   [Mongodb atlas bm25 retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/mongodb_atlas_bm25_retriever/)\n        *   [Pathway](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/pathway/)\n        *   [Query fusion](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/query_fusion/)\n        *   [Recursive](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/)\n        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/)\n        *   [Sql](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/)\n        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/)\n        *   [Transform](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/transform/)\n        *   [Tree](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/)\n        *   [Vector](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/)\n        *   [Vertexai search](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vertexai_search/)\n        *   [Videodb](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/videodb/)\n        *   [You](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/you/)\n        \n    *   [ ] \n        \n        [Schema](https://docs.llamaindex.ai/en/stable/api_reference/schema/)\n        \n        Schema\n        \n    *   [ ]  Selectors\n        \n        Selectors\n        \n        *   [Notdiamond](https://docs.llamaindex.ai/en/stable/api_reference/selectors/notdiamond/)\n        \n    *   [ ]  Sparse Embeddings\n        \n        Sparse Embeddings\n        \n        *   [Fastembed](https://docs.llamaindex.ai/en/stable/api_reference/sparse_embeddings/fastembed/)\n        \n    *   [ ]  Storage\n        \n        Storage\n        \n        *   [ ] \n            \n            [Chat Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/)\n            \n            Chat Store\n            \n            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/)\n            *   [Azurecosmosmongovcore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azurecosmosmongovcore/)\n            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azurecosmosnosql/)\n            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/dynamodb/)\n            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/postgres/)\n            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/)\n            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/)\n            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/tablestore/)\n            *   [Upstash](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/upstash/)\n            \n        *   [ ] \n            \n            [Docstore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/)\n            \n            Docstore\n            \n            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/)\n            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azurecosmosnosql/)\n            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/couchbase/)\n            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/dynamodb/)\n            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/elasticsearch/)\n            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/)\n            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/mongodb/)\n            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/)\n            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/redis/)\n            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/)\n            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/tablestore/)\n            \n        *   [ ] \n            \n            [Graph Stores](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/)\n            \n            Graph Stores\n            \n            *   [Falkordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/falkordb/)\n            *   [Kuzu](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/kuzu/)\n            *   [Memgraph](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/memgraph/)\n            *   [Nebula](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/nebula/)\n            *   [Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/)\n            *   [Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/)\n            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/simple/)\n            *   [Tidb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/tidb/)\n            \n        *   [ ] \n            \n            [Index Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/)\n            \n            Index Store\n            \n            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/)\n            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azurecosmosnosql/)\n            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/couchbase/)\n            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/)\n            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/elasticsearch/)\n            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/firestore/)\n            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/)\n            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/postgres/)\n            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/)\n            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/simple/)\n            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/tablestore/)\n            \n        *   [ ] \n            \n            [Kvstore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/)\n            \n            Kvstore\n            \n            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/)\n            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azurecosmosnosql/)\n            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/couchbase/)\n            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/)\n            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/elasticsearch/)\n            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/)\n            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/)\n            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/)\n            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/redis/)\n            *   [S3](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/s3/)\n            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/)\n            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/tablestore/)\n            \n        *   [ ]  Storage\n            \n            Storage\n            \n            *   [Storage context](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/)\n            \n        *   [ ] \n            \n            [Vector Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/)\n            \n            Vector Store\n            \n            *   [Alibabacloud opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/alibabacloud_opensearch/)\n            *   [Analyticdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/analyticdb/)\n            *   [Astra db](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/astra_db/)\n            *   [Awadb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awadb/)\n            *   [Awsdocdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/)\n            *   [Azureaisearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/)\n            *   [Azurecosmosmongo](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/)\n            *   [Azurecosmosnosql](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosnosql/)\n            *   [Bagel](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/bagel/)\n            *   [Baiduvectordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/baiduvectordb/)\n            *   [Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/cassandra/)\n            *   [None](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin.md)\n            *   [Chroma](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/)\n            *   [Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/clickhouse/)\n            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/)\n            *   [Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dashvector/)\n            *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/databricks/)\n            *   [Deeplake](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/deeplake/)\n            *   [Docarray](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/docarray/)\n            *   [Duckdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/duckdb/)\n            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/)\n            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/elasticsearch/)\n            *   [Epsilla](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/epsilla/)\n            *   [Faiss](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/faiss/)\n            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/firestore/)\n            *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/)\n            *   [Hologres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/)\n            *   [Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/)\n            *   [Kdbai](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/kdbai/)\n            *   [Lancedb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lancedb/)\n            *   [Lantern](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lantern/)\n            *   [Lindorm](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lindorm/)\n            *   [Mariadb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mariadb/)\n            *   [None](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/metal.md)\n            *   [Milvus](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/milvus/)\n            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/)\n            *   [Myscale](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/myscale/)\n            *   [Neo4jvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/)\n            *   [Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/)\n            *   [Nile](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/nile/)\n            *   [Objectbox](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/objectbox/)\n            *   [Oceanbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/oceanbase/)\n            *   [Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/)\n            *   [Oracledb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/oracledb/)\n            *   [Pgvecto rs](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pgvecto_rs/)\n            *   [Pinecone](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/)\n            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/)\n            *   [Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/qdrant/)\n            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/redis/)\n            *   [Relyt](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/relyt/)\n            *   [Rocksetdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/rocksetdb/)\n            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/simple/)\n            *   [Singlestoredb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/)\n            *   [None](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/sqlalchemy.md)\n            *   [Supabase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/)\n            *   [Tablestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tablestore/)\n            *   [Tair](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tair/)\n            *   [Tencentvectordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tencentvectordb/)\n            *   [Tidbvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tidbvector/)\n            *   [Timescalevector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/timescalevector/)\n            *   [Txtai](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/txtai/)\n            *   [Typesense](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/typesense/)\n            *   [Upstash](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/)\n            *   [Vearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vearch/)\n            *   [Vertexaivectorsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/)\n            *   [Vespa](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vespa/)\n            *   [Weaviate](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/)\n            *   [Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/wordlift/)\n            *   [Zep](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/)\n            \n        \n    *   [ ] \n        \n        [Tools](https://docs.llamaindex.ai/en/stable/api_reference/tools/)\n        \n        Tools\n        \n        *   [Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/tools/arxiv/)\n        *   [Azure code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/)\n        *   [Azure cv](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/)\n        *   [Azure speech](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/)\n        *   [Azure translate](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/)\n        *   [Bing search](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/)\n        *   [Box](https://docs.llamaindex.ai/en/stable/api_reference/tools/box/)\n        *   [Brave search](https://docs.llamaindex.ai/en/stable/api_reference/tools/brave_search/)\n        *   [Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/tools/cassandra/)\n        *   [Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/tools/chatgpt_plugin/)\n        *   [Code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/code_interpreter/)\n        *   [Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/tools/cogniswitch/)\n        *   [Database](https://docs.llamaindex.ai/en/stable/api_reference/tools/database/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/tools/docker_code.md)\n        *   [Duckduckgo](https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/)\n        *   [Elevenlabs](https://docs.llamaindex.ai/en/stable/api_reference/tools/elevenlabs/)\n        *   [Exa](https://docs.llamaindex.ai/en/stable/api_reference/tools/exa/)\n        *   [Finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/)\n        *   [Function](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/)\n        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/)\n        *   [Graphql](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/)\n        *   [Ionic shopping](https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/)\n        *   [Jina](https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/)\n        *   [Load and search](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/)\n        *   [Metaphor](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/)\n        *   [Multion](https://docs.llamaindex.ai/en/stable/api_reference/tools/multion/)\n        *   [Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/)\n        *   [Notion](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/)\n        *   [Ondemand loader](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/)\n        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/)\n        *   [Openapi](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/)\n        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/tools/oracleai.md)\n        *   [Playgrounds](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/)\n        *   [Python file](https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/)\n        *   [Query engine](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_engine/)\n        *   [Query plan](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/)\n        *   [Requests](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/)\n        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/tools/retriever/)\n        *   [Salesforce](https://docs.llamaindex.ai/en/stable/api_reference/tools/salesforce/)\n        *   [Scrapegraph](https://docs.llamaindex.ai/en/stable/api_reference/tools/scrapegraph/)\n        *   [Shopify](https://docs.llamaindex.ai/en/stable/api_reference/tools/shopify/)\n        *   [Slack](https://docs.llamaindex.ai/en/stable/api_reference/tools/slack/)\n        *   [Tavily research](https://docs.llamaindex.ai/en/stable/api_reference/tools/tavily_research/)\n        *   [Text to image](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/)\n        *   [Tool spec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/)\n        *   [Vectara query](https://docs.llamaindex.ai/en/stable/api_reference/tools/vectara_query/)\n        *   [Vector db](https://docs.llamaindex.ai/en/stable/api_reference/tools/vector_db/)\n        *   [Waii](https://docs.llamaindex.ai/en/stable/api_reference/tools/waii/)\n        *   [Weather](https://docs.llamaindex.ai/en/stable/api_reference/tools/weather/)\n        *   [Wikipedia](https://docs.llamaindex.ai/en/stable/api_reference/tools/wikipedia/)\n        *   [Wolfram alpha](https://docs.llamaindex.ai/en/stable/api_reference/tools/wolfram_alpha/)\n        *   [Yahoo finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/yahoo_finance/)\n        *   [Yelp](https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/)\n        *   [Zapier](https://docs.llamaindex.ai/en/stable/api_reference/tools/zapier/)\n        \n    *   [ ]  Workflow\n        \n        Workflow\n        \n        *   [Decorators](https://docs.llamaindex.ai/en/stable/api_reference/workflow/decorators/)\n        *   [Context](https://docs.llamaindex.ai/en/stable/api_reference/workflow/context/)\n        *   [Events](https://docs.llamaindex.ai/en/stable/api_reference/workflow/events/)\n        *   [Retry policy](https://docs.llamaindex.ai/en/stable/api_reference/workflow/retry_policy/)\n        *   [Workflow](https://docs.llamaindex.ai/en/stable/api_reference/workflow/workflow/)\n        \n    \n*   [ ] \n    \n    [Open-Source Community](https://docs.llamaindex.ai/en/stable/community/llama_packs/)\n    \n    Open-Source Community\n    \n    *   [Integrations](https://docs.llamaindex.ai/en/stable/community/integrations/)\n    *   [Full Stack Projects](https://docs.llamaindex.ai/en/stable/community/full_stack_projects/)\n    *   [ ]  Community FAQ\n        \n        Community FAQ\n        \n        *   [Chat Engines](https://docs.llamaindex.ai/en/stable/community/faq/chat_engines/)\n        *   [Documents and Nodes](https://docs.llamaindex.ai/en/stable/community/faq/documents_and_nodes/)\n        *   [Embeddings](https://docs.llamaindex.ai/en/stable/community/faq/embeddings/)\n        *   [Large Language Models](https://docs.llamaindex.ai/en/stable/community/faq/llms/)\n        *   [Query Engines](https://docs.llamaindex.ai/en/stable/community/faq/query_engines/)\n        *   [Vector Database](https://docs.llamaindex.ai/en/stable/community/faq/vector_database/)\n        \n    *   [ ]  Contributing\n        \n        Contributing\n        \n        *   [Code](https://docs.llamaindex.ai/en/stable/CONTRIBUTING/)\n        *   [Docs](https://docs.llamaindex.ai/en/stable/DOCS_README/)\n        \n    *   [Changelog](https://docs.llamaindex.ai/en/stable/CHANGELOG/)\n    *   [Presentations](https://docs.llamaindex.ai/en/stable/presentations/past_presentations/)\n    *   [Deprecated Terms](https://docs.llamaindex.ai/en/stable/changes/deprecated_terms/)\n    \n*   [ ] \n    \n    [LlamaCloud](https://docs.llamaindex.ai/en/stable/llama_cloud/)\n    \n    LlamaCloud\n    \n    *   [LlamaParse](https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/)\n    \n\nTable of contents\n\n*   [Overview](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#overview)\n*   [Cookbook](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#cookbook)\n*   [Setup](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#setup)\n*   [1\\. Chain Together Prompt and LLM](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-chain-together-prompt-and-llm)\n    \n    *   [View Intermediate Inputs/Outputs](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#view-intermediate-inputsoutputs)\n    *   [Try Output Parsing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#try-output-parsing)\n    *   [Streaming Support](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#streaming-support)\n    \n*   [Chain Together Query Rewriting Workflow (prompts + LLM) with Retrieval](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#chain-together-query-rewriting-workflow-prompts-llm-with-retrieval)\n*   [Create a Full RAG Pipeline as a DAG](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#create-a-full-rag-pipeline-as-a-dag)\n    \n    *   [1\\. RAG Pipeline with Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-rag-pipeline-with-query-rewriting)\n    *   [2\\. RAG Pipeline without Query Rewriting](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#2-rag-pipeline-without-query-rewriting)\n    \n*   [Defining a Custom Component in a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#defining-a-custom-component-in-a-query-pipeline)\n*   [Stepwise Execution of a Pipeline](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#stepwise-execution-of-a-pipeline)\n\n       \n\nAn Introduction to LlamaIndex Query Pipelines[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#an-introduction-to-llamaindex-query-pipelines)\n======================================================================================================================================================================\n\nOverview[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#overview)\n--------------------------------------------------------------------------------------------\n\nLlamaIndex provides a declarative query API that allows you to chain together different modules in order to orchestrate simple-to-advanced workflows over your data.\n\nThis is centered around our `QueryPipeline` abstraction. Load in a variety of modules (from LLMs to prompts to retrievers to other pipelines), connect them all together into a sequential chain or DAG, and run it end2end.\n\n**NOTE**: You can orchestrate all these workflows without the declarative pipeline abstraction (by using the modules imperatively and writing your own functions). So what are the advantages of `QueryPipeline`?\n\n*   Express common workflows with fewer lines of code/boilerplate\n*   Greater readability\n*   Greater parity / better integration points with common low-code / no-code solutions (e.g. LangFlow)\n*   \\[In the future\\] A declarative interface allows easy serializability of pipeline components, providing portability of pipelines/easier deployment to different systems.\n\nCookbook[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#cookbook)\n--------------------------------------------------------------------------------------------\n\nIn this cookbook we give you an introduction to our `QueryPipeline` interface and show you some basic workflows you can tackle.\n\n*   Chain together prompt and LLM\n*   Chain together query rewriting (prompt + LLM) with retrieval\n*   Chain together a full RAG query pipeline (query rewriting, retrieval, reranking, response synthesis)\n*   Setting up a custom query component\n*   Executing a pipeline step-by-step\n\nSetup[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#setup)\n--------------------------------------------------------------------------------------\n\nHere we setup some data + indexes (from PG's essay) that we'll be using in the rest of the cookbook.\n\nIn \\[ \\]:\n\nCopied!\n\n%pip install llama\\-index\\-embeddings\\-openai\n%pip install llama\\-index\\-postprocessor\\-cohere\\-rerank\n%pip install llama\\-index\\-llms\\-openai\n\n%pip install llama-index-embeddings-openai %pip install llama-index-postprocessor-cohere-rerank %pip install llama-index-llms-openai\n\nIn \\[ \\]:\n\nCopied!\n\n\\# setup Arize Phoenix for logging/observability\nimport phoenix as px\n\npx.launch\\_app()\nimport llama\\_index.core\n\nllama\\_index.core.set\\_global\\_handler(\"arize\\_phoenix\")\n\n\\# setup Arize Phoenix for logging/observability import phoenix as px px.launch\\_app() import llama\\_index.core llama\\_index.core.set\\_global\\_handler(\"arize\\_phoenix\")\n\n🌍 To view the Phoenix app in your browser, visit http://127.0.0.1:6006/\n📺 To view the Phoenix app in a notebook, run \\`px.active\\_session().view()\\`\n📖 For more information on how to use Phoenix, check out https://docs.arize.com/phoenix\n\nIn \\[ \\]:\n\nCopied!\n\nimport os\n\nos.environ\\[\"OPENAI\\_API\\_KEY\"\\] \\= \"sk-...\"\n\nimport os os.environ\\[\"OPENAI\\_API\\_KEY\"\\] = \"sk-...\"\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.llms.openai import OpenAI\nfrom llama\\_index.embeddings.openai import OpenAIEmbedding\nfrom llama\\_index.core import Settings\n\nSettings.llm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\nSettings.embed\\_model \\= OpenAIEmbedding(model\\=\"text-embedding-3-small\")\n\nfrom llama\\_index.llms.openai import OpenAI from llama\\_index.embeddings.openai import OpenAIEmbedding from llama\\_index.core import Settings Settings.llm = OpenAI(model=\"gpt-3.5-turbo\") Settings.embed\\_model = OpenAIEmbedding(model=\"text-embedding-3-small\")\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.core import SimpleDirectoryReader\n\nreader \\= SimpleDirectoryReader(\"../data/paul\\_graham\")\n\nfrom llama\\_index.core import SimpleDirectoryReader reader = SimpleDirectoryReader(\"../data/paul\\_graham\")\n\nIn \\[ \\]:\n\nCopied!\n\ndocs \\= reader.load\\_data()\n\ndocs = reader.load\\_data()\n\nIn \\[ \\]:\n\nCopied!\n\nimport os\nfrom llama\\_index.core import (\n    StorageContext,\n    VectorStoreIndex,\n    load\\_index\\_from\\_storage,\n)\n\nif not os.path.exists(\"storage\"):\n    index \\= VectorStoreIndex.from\\_documents(docs)\n    \\# save index to disk\n    index.set\\_index\\_id(\"vector\\_index\")\n    index.storage\\_context.persist(\"./storage\")\nelse:\n    \\# rebuild storage context\n    storage\\_context \\= StorageContext.from\\_defaults(persist\\_dir\\=\"storage\")\n    \\# load index\n    index \\= load\\_index\\_from\\_storage(storage\\_context, index\\_id\\=\"vector\\_index\")\n\nimport os from llama\\_index.core import ( StorageContext, VectorStoreIndex, load\\_index\\_from\\_storage, ) if not os.path.exists(\"storage\"): index = VectorStoreIndex.from\\_documents(docs) # save index to disk index.set\\_index\\_id(\"vector\\_index\") index.storage\\_context.persist(\"./storage\") else: # rebuild storage context storage\\_context = StorageContext.from\\_defaults(persist\\_dir=\"storage\") # load index index = load\\_index\\_from\\_storage(storage\\_context, index\\_id=\"vector\\_index\")\n\n1\\. Chain Together Prompt and LLM[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-chain-together-prompt-and-llm)\n--------------------------------------------------------------------------------------------------------------------------------------------\n\nIn this section we show a super simple workflow of chaining together a prompt with LLM.\n\nWe simply define `chain` on initialization. This is a special case of a query pipeline where the components are purely sequential, and we automatically convert outputs into the right format for the next inputs.\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.core.query\\_pipeline import QueryPipeline\nfrom llama\\_index.core import PromptTemplate\n\n\\# try chaining basic prompts\nprompt\\_str \\= \"Please generate related movies to {movie\\_name}\"\nprompt\\_tmpl \\= PromptTemplate(prompt\\_str)\nllm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\n\np \\= QueryPipeline(chain\\=\\[prompt\\_tmpl, llm\\], verbose\\=True)\n\nfrom llama\\_index.core.query\\_pipeline import QueryPipeline from llama\\_index.core import PromptTemplate # try chaining basic prompts prompt\\_str = \"Please generate related movies to {movie\\_name}\" prompt\\_tmpl = PromptTemplate(prompt\\_str) llm = OpenAI(model=\"gpt-3.5-turbo\") p = QueryPipeline(chain=\\[prompt\\_tmpl, llm\\], verbose=True)\n\nIn \\[ \\]:\n\nCopied!\n\noutput \\= p.run(movie\\_name\\=\"The Departed\")\n\noutput = p.run(movie\\_name=\"The Departed\")\n\n\\> Running module 8dc57d24-9691-4d8d-87d7-151865a7cd1b with input: \nmovie\\_name: The Departed\n\n\\> Running module 7ed9e26c-a704-4b0b-9cfd-991266e754c0 with input: \nmessages: Please generate related movies to The Departed\n\nIn \\[ \\]:\n\nCopied!\n\nprint(str(output))\n\nprint(str(output))\n\nassistant: 1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\n2. The Town (2010) - A crime thriller directed by and starring Ben Affleck\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\n4. Goodfellas (1990) - A classic mobster film directed by Martin Scorsese\n5. The Irishman (2019) - Another crime drama directed by Martin Scorsese, starring Robert De Niro and Al Pacino\n6. The Departed (2006) - The Departed is a 2006 American crime film directed by Martin Scorsese and written by William Monahan. It is a remake of the 2002 Hong Kong film Infernal Affairs. The film stars Leonardo DiCaprio, Matt Damon, Jack Nicholson, and Mark Wahlberg, with Martin Sheen, Ray Winstone, Vera Farmiga, and Alec Baldwin in supporting roles.\n\n### View Intermediate Inputs/Outputs[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#view-intermediate-inputsoutputs)\n\nFor debugging and other purposes, we can also view the inputs and outputs at each step.\n\nIn \\[ \\]:\n\nCopied!\n\noutput, intermediates \\= p.run\\_with\\_intermediates(movie\\_name\\=\"The Departed\")\n\noutput, intermediates = p.run\\_with\\_intermediates(movie\\_name=\"The Departed\")\n\n\\> Running module 8dc57d24-9691-4d8d-87d7-151865a7cd1b with input: \nmovie\\_name: The Departed\n\n\\> Running module 7ed9e26c-a704-4b0b-9cfd-991266e754c0 with input: \nmessages: Please generate related movies to The Departed\n\nIn \\[ \\]:\n\nCopied!\n\nintermediates\\[\"8dc57d24-9691-4d8d-87d7-151865a7cd1b\"\\]\n\nintermediates\\[\"8dc57d24-9691-4d8d-87d7-151865a7cd1b\"\\]\n\nOut\\[ \\]:\n\nComponentIntermediates(inputs={'movie\\_name': 'The Departed'}, outputs={'prompt': 'Please generate related movies to The Departed'})\n\nIn \\[ \\]:\n\nCopied!\n\nintermediates\\[\"7ed9e26c-a704-4b0b-9cfd-991266e754c0\"\\]\n\nintermediates\\[\"7ed9e26c-a704-4b0b-9cfd-991266e754c0\"\\]\n\nOut\\[ \\]:\n\nComponentIntermediates(inputs={'messages': 'Please generate related movies to The Departed'}, outputs={'output': ChatResponse(message=ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'\\>, content='1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\\\\n2. The Town (2010) - A crime thriller directed by Ben Affleck\\\\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\\\\n4. Goodfellas (1990) - A classic crime film directed by Martin Scorsese\\\\n5. The Irishman (2019) - Another crime film directed by Martin Scorsese, starring Robert De Niro and Al Pacino\\\\n6. The Godfather (1972) - A classic crime film directed by Francis Ford Coppola\\\\n7. Heat (1995) - A crime thriller directed by Michael Mann, starring Al Pacino and Robert De Niro\\\\n8. The Departed (2006) - A crime thriller directed by Martin Scorsese, starring Leonardo DiCaprio and Matt Damon.', additional\\_kwargs={}), raw={'id': 'chatcmpl-9EKf2nZ4latFJvHy0gzOUZbaB8xwY', 'choices': \\[Choice(finish\\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\\\\n2. The Town (2010) - A crime thriller directed by Ben Affleck\\\\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\\\\n4. Goodfellas (1990) - A classic crime film directed by Martin Scorsese\\\\n5. The Irishman (2019) - Another crime film directed by Martin Scorsese, starring Robert De Niro and Al Pacino\\\\n6. The Godfather (1972) - A classic crime film directed by Francis Ford Coppola\\\\n7. Heat (1995) - A crime thriller directed by Michael Mann, starring Al Pacino and Robert De Niro\\\\n8. The Departed (2006) - A crime thriller directed by Martin Scorsese, starring Leonardo DiCaprio and Matt Damon.', role='assistant', function\\_call=None, tool\\_calls=None))\\], 'created': 1713203040, 'model': 'gpt-3.5-turbo-0125', 'object': 'chat.completion', 'system\\_fingerprint': 'fp\\_c2295e73ad', 'usage': CompletionUsage(completion\\_tokens=184, prompt\\_tokens=15, total\\_tokens=199)}, delta=None, logprobs=None, additional\\_kwargs={})})\n\n### Try Output Parsing[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#try-output-parsing)\n\nLet's parse the outputs into a structured Pydantic object.\n\nIn \\[ \\]:\n\nCopied!\n\nfrom typing import List\nfrom pydantic import BaseModel, Field\nfrom llama\\_index.core.output\\_parsers import PydanticOutputParser\n\nclass Movie(BaseModel):\n    \"\"\"Object representing a single movie.\"\"\"\n\n    name: str \\= Field(..., description\\=\"Name of the movie.\")\n    year: int \\= Field(..., description\\=\"Year of the movie.\")\n\nclass Movies(BaseModel):\n    \"\"\"Object representing a list of movies.\"\"\"\n\n    movies: List\\[Movie\\] \\= Field(..., description\\=\"List of movies.\")\n\nllm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\noutput\\_parser \\= PydanticOutputParser(Movies)\njson\\_prompt\\_str \\= \"\"\"\\\\\nPlease generate related movies to {movie\\_name}. Output with the following JSON format: \n\"\"\"\njson\\_prompt\\_str \\= output\\_parser.format(json\\_prompt\\_str)\n\nfrom typing import List from pydantic import BaseModel, Field from llama\\_index.core.output\\_parsers import PydanticOutputParser class Movie(BaseModel): \"\"\"Object representing a single movie.\"\"\" name: str = Field(..., description=\"Name of the movie.\") year: int = Field(..., description=\"Year of the movie.\") class Movies(BaseModel): \"\"\"Object representing a list of movies.\"\"\" movies: List\\[Movie\\] = Field(..., description=\"List of movies.\") llm = OpenAI(model=\"gpt-3.5-turbo\") output\\_parser = PydanticOutputParser(Movies) json\\_prompt\\_str = \"\"\"\\\\ Please generate related movies to {movie\\_name}. Output with the following JSON format: \"\"\" json\\_prompt\\_str = output\\_parser.format(json\\_prompt\\_str)\n\nIn \\[ \\]:\n\nCopied!\n\n\\# add JSON spec to prompt template\njson\\_prompt\\_tmpl \\= PromptTemplate(json\\_prompt\\_str)\n\np \\= QueryPipeline(chain\\=\\[json\\_prompt\\_tmpl, llm, output\\_parser\\], verbose\\=True)\noutput \\= p.run(movie\\_name\\=\"Toy Story\")\n\n\\# add JSON spec to prompt template json\\_prompt\\_tmpl = PromptTemplate(json\\_prompt\\_str) p = QueryPipeline(chain=\\[json\\_prompt\\_tmpl, llm, output\\_parser\\], verbose=True) output = p.run(movie\\_name=\"Toy Story\")\n\n\\> Running module 2e4093c5-ae62-420a-be91-9c28c057bada with input: \nmovie\\_name: Toy Story\n\n\\> Running module 3b41f95c-f54b-41d7-8ef0-8e45b5d7eeb0 with input: \nmessages: Please generate related movies to Toy Story. Output with the following JSON format: \n\n\n\nHere's a JSON schema to follow:\n{\"title\": \"Movies\", \"description\": \"Object representing a list of movies.\", \"typ...\n\n\\> Running module 27e79a16-72de-4ce2-8b2e-94932c4069c3 with input: \ninput: assistant: {\n  \"movies\": \\[\n    {\n      \"name\": \"Finding Nemo\",\n      \"year\": 2003\n    },\n    {\n      \"name\": \"Monsters, Inc.\",\n      \"year\": 2001\n    },\n    {\n      \"name\": \"Cars\",\n      \"year\": 2006\n...\n\nIn \\[ \\]:\n\nCopied!\n\noutput\n\noutput\n\nOut\\[ \\]:\n\nMovies(movies=\\[Movie(name='Finding Nemo', year=2003), Movie(name='Monsters, Inc.', year=2001), Movie(name='Cars', year=2006), Movie(name='The Incredibles', year=2004), Movie(name='Ratatouille', year=2007)\\])\n\n### Streaming Support[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#streaming-support)\n\nThe query pipelines have LLM streaming support (simply do `as_query_component(streaming=True)`). Intermediate outputs will get autoconverted, and the final output can be a streaming output. Here's some examples.\n\n**1\\. Chain multiple Prompts with Streaming**\n\nIn \\[ \\]:\n\nCopied!\n\nprompt\\_str \\= \"Please generate related movies to {movie\\_name}\"\nprompt\\_tmpl \\= PromptTemplate(prompt\\_str)\n\\# let's add some subsequent prompts for fun\nprompt\\_str2 \\= \"\"\"\\\\\nHere's some text:\n\n{text}\n\nCan you rewrite this with a summary of each movie?\n\"\"\"\nprompt\\_tmpl2 \\= PromptTemplate(prompt\\_str2)\nllm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\nllm\\_c \\= llm.as\\_query\\_component(streaming\\=True)\n\np \\= QueryPipeline(\n    chain\\=\\[prompt\\_tmpl, llm\\_c, prompt\\_tmpl2, llm\\_c\\], verbose\\=True\n)\n\\# p = QueryPipeline(chain=\\[prompt\\_tmpl, llm\\_c\\], verbose=True)\n\nprompt\\_str = \"Please generate related movies to {movie\\_name}\" prompt\\_tmpl = PromptTemplate(prompt\\_str) # let's add some subsequent prompts for fun prompt\\_str2 = \"\"\"\\\\ Here's some text: {text} Can you rewrite this with a summary of each movie? \"\"\" prompt\\_tmpl2 = PromptTemplate(prompt\\_str2) llm = OpenAI(model=\"gpt-3.5-turbo\") llm\\_c = llm.as\\_query\\_component(streaming=True) p = QueryPipeline( chain=\\[prompt\\_tmpl, llm\\_c, prompt\\_tmpl2, llm\\_c\\], verbose=True ) # p = QueryPipeline(chain=\\[prompt\\_tmpl, llm\\_c\\], verbose=True)\n\nIn \\[ \\]:\n\nCopied!\n\noutput \\= p.run(movie\\_name\\=\"The Dark Knight\")\nfor o in output:\n    print(o.delta, end\\=\"\")\n\noutput = p.run(movie\\_name=\"The Dark Knight\") for o in output: print(o.delta, end=\"\")\n\n\\> Running module 213af6d4-3450-46af-9087-b80656ae6951 with input: \nmovie\\_name: The Dark Knight\n\n\\> Running module 3ff7e987-f5f3-4b36-a3e1-be5a4821d9d9 with input: \nmessages: Please generate related movies to The Dark Knight\n\n\\> Running module a2841bd3-c833-4427-9a7e-83b19872b064 with input: \ntext: <generator object llm\\_chat\\_callback.<locals\\>.wrap.<locals\\>.wrapped\\_llm\\_chat.<locals\\>.wrapped\\_gen at 0x298d338b0\\>\n\n\\> Running module c7e0a454-213a-460e-b029-f2d42fd7d938 with input: \nmessages: Here's some text:\n\n1. Batman Begins (2005)\n2. The Dark Knight Rises (2012)\n3. Batman v Superman: Dawn of Justice (2016)\n4. Man of Steel (2013)\n5. The Avengers (2012)\n6. Iron Man (2008)\n7. Captain Amer...\n\n1\\. Batman Begins (2005): A young Bruce Wayne becomes Batman to fight crime in Gotham City, facing his fears and training under the guidance of Ra's al Ghul.\n2. The Dark Knight Rises (2012): Batman returns to protect Gotham City from the ruthless terrorist Bane, who plans to destroy the city and its symbol of hope.\n3. Batman v Superman: Dawn of Justice (2016): Batman and Superman clash as their ideologies collide, leading to an epic battle while a new threat emerges that threatens humanity.\n4. Man of Steel (2013): The origin story of Superman, as he embraces his powers and faces General Zod, a fellow Kryptonian seeking to destroy Earth.\n5. The Avengers (2012): Earth's mightiest heroes, including Iron Man, Captain America, Thor, and Hulk, join forces to stop Loki and his alien army from conquering the world.\n6. Iron Man (2008): Billionaire Tony Stark builds a high-tech suit to escape captivity and becomes the superhero Iron Man, using his technology to fight against evil.\n7. Captain America: The Winter Soldier (2014): Captain America teams up with Black Widow and Falcon to uncover a conspiracy within S.H.I.E.L.D. while facing a deadly assassin known as the Winter Soldier.\n8. The Amazing Spider-Man (2012): Peter Parker, a high school student bitten by a radioactive spider, becomes Spider-Man and battles the Lizard, a monstrous villain threatening New York City.\n9. Watchmen (2009): Set in an alternate reality, a group of retired vigilantes investigates the murder of one of their own, uncovering a conspiracy that could have catastrophic consequences.\n10. Sin City (2005): A neo-noir anthology film set in the crime-ridden city of Basin City, following various characters as they navigate through corruption, violence, and redemption.\n11. V for Vendetta (2005): In a dystopian future, a masked vigilante known as V fights against a totalitarian government, inspiring the people to rise up and reclaim their freedom.\n12. Blade Runner 2049 (2017): A young blade runner uncovers a long-buried secret that leads him to seek out former blade runner Rick Deckard, while unraveling the mysteries of a future society.\n13. Inception (2010): A skilled thief enters people's dreams to steal information, but is tasked with planting an idea instead, leading to a mind-bending journey through multiple layers of reality.\n14. The Matrix (1999): A computer hacker discovers the truth about reality, joining a group of rebels fighting against sentient machines that have enslaved humanity in a simulated world.\n15. The Crow (1994): A musician, resurrected by a supernatural crow, seeks vengeance against the gang that murdered him and his fiancée, unleashing a dark and atmospheric tale of revenge.\n\n**2\\. Feed streaming output to output parser**\n\nIn \\[ \\]:\n\nCopied!\n\np \\= QueryPipeline(\n    chain\\=\\[\n        json\\_prompt\\_tmpl,\n        llm.as\\_query\\_component(streaming\\=True),\n        output\\_parser,\n    \\],\n    verbose\\=True,\n)\noutput \\= p.run(movie\\_name\\=\"Toy Story\")\nprint(output)\n\np = QueryPipeline( chain=\\[ json\\_prompt\\_tmpl, llm.as\\_query\\_component(streaming=True), output\\_parser, \\], verbose=True, ) output = p.run(movie\\_name=\"Toy Story\") print(output)\n\n\\> Running module fe1dbf6a-56e0-44bf-97d7-a2a1fe9d9b8c with input: \nmovie\\_name: Toy Story\n\n\\> Running module a8eaaf91-df9d-46c4-bbae-06c15cd15123 with input: \nmessages: Please generate related movies to Toy Story. Output with the following JSON format: \n\n\n\nHere's a JSON schema to follow:\n{\"title\": \"Movies\", \"description\": \"Object representing a list of movies.\", \"typ...\n\n\\> Running module fcbc0b09-0ef5-43e0-b007-c4508fd6742f with input: \ninput: <generator object llm\\_chat\\_callback.<locals\\>.wrap.<locals\\>.wrapped\\_llm\\_chat.<locals\\>.wrapped\\_gen at 0x298d32dc0\\>\n\nmovies=\\[Movie(name='Finding Nemo', year=2003), Movie(name='Monsters, Inc.', year=2001), Movie(name='The Incredibles', year=2004), Movie(name='Cars', year=2006), Movie(name='Ratatouille', year=2007)\\]\n\nChain Together Query Rewriting Workflow (prompts + LLM) with Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#chain-together-query-rewriting-workflow-prompts-llm-with-retrieval)\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nHere we try a slightly more complex workflow where we send the input through two prompts before initiating retrieval.\n\n1.  Generate question about given topic.\n2.  Hallucinate answer given question, for better retrieval.\n\nSince each prompt only takes in one input, note that the `QueryPipeline` will automatically chain LLM outputs into the prompt and then into the LLM.\n\nYou'll see how to define links more explicitly in the next section.\n\nIn \\[ \\]:\n\nCopied!\n\n\\# !pip install llama-index-postprocessor-cohere-rerank\n\n\\# !pip install llama-index-postprocessor-cohere-rerank\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.postprocessor.cohere\\_rerank import CohereRerank\n\n\\# generate question regarding topic\nprompt\\_str1 \\= \"Please generate a concise question about Paul Graham's life regarding the following topic {topic}\"\nprompt\\_tmpl1 \\= PromptTemplate(prompt\\_str1)\n\\# use HyDE to hallucinate answer.\nprompt\\_str2 \\= (\n    \"Please write a passage to answer the question\\\\n\"\n    \"Try to include as many key details as possible.\\\\n\"\n    \"\\\\n\"\n    \"\\\\n\"\n    \"{query\\_str}\\\\n\"\n    \"\\\\n\"\n    \"\\\\n\"\n    'Passage:\"\"\"\\\\n'\n)\nprompt\\_tmpl2 \\= PromptTemplate(prompt\\_str2)\n\nllm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\nretriever \\= index.as\\_retriever(similarity\\_top\\_k\\=5)\np \\= QueryPipeline(\n    chain\\=\\[prompt\\_tmpl1, llm, prompt\\_tmpl2, llm, retriever\\], verbose\\=True\n)\n\nfrom llama\\_index.postprocessor.cohere\\_rerank import CohereRerank # generate question regarding topic prompt\\_str1 = \"Please generate a concise question about Paul Graham's life regarding the following topic {topic}\" prompt\\_tmpl1 = PromptTemplate(prompt\\_str1) # use HyDE to hallucinate answer. prompt\\_str2 = ( \"Please write a passage to answer the question\\\\n\" \"Try to include as many key details as possible.\\\\n\" \"\\\\n\" \"\\\\n\" \"{query\\_str}\\\\n\" \"\\\\n\" \"\\\\n\" 'Passage:\"\"\"\\\\n' ) prompt\\_tmpl2 = PromptTemplate(prompt\\_str2) llm = OpenAI(model=\"gpt-3.5-turbo\") retriever = index.as\\_retriever(similarity\\_top\\_k=5) p = QueryPipeline( chain=\\[prompt\\_tmpl1, llm, prompt\\_tmpl2, llm, retriever\\], verbose=True )\n\nIn \\[ \\]:\n\nCopied!\n\nnodes \\= p.run(topic\\=\"college\")\nlen(nodes)\n\nnodes = p.run(topic=\"college\") len(nodes)\n\n\\> Running module f5435516-61b6-49e9-9926-220cfb6443bd with input: \ntopic: college\n\n\\> Running module 1dcaa097-cedc-4466-81bb-f8fd8768762b with input: \nmessages: Please generate a concise question about Paul Graham's life regarding the following topic college\n\n\\> Running module 891afa10-5fe0-47ed-bdee-42a59d0e916d with input: \nquery\\_str: assistant: How did Paul Graham's college experience shape his career and entrepreneurial mindset?\n\n\\> Running module 5bcd9964-b972-41a9-960d-96894c57a372 with input: \nmessages: Please write a passage to answer the question\nTry to include as many key details as possible.\n\n\nHow did Paul Graham's college experience shape his career and entrepreneurial mindset?\n\n\nPassage:\"\"\"\n\n\\> Running module 0b81a91a-2c90-4700-8ba1-25ffad5311fd with input: \ninput: assistant: Paul Graham's college experience played a pivotal role in shaping his career and entrepreneurial mindset. As a student at Cornell University, Graham immersed himself in the world of compute...\n\nOut\\[ \\]:\n\n5\n\nCreate a Full RAG Pipeline as a DAG[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#create-a-full-rag-pipeline-as-a-dag)\n--------------------------------------------------------------------------------------------------------------------------------------------------\n\nHere we chain together a full RAG pipeline consisting of query rewriting, retrieval, reranking, and response synthesis.\n\nHere we can't use `chain` syntax because certain modules depend on multiple inputs (for instance, response synthesis expects both the retrieved nodes and the original question). Instead we'll construct a DAG explicitly, through `add_modules` and then `add_link`.\n\n### 1\\. RAG Pipeline with Query Rewriting[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-rag-pipeline-with-query-rewriting)\n\nWe use an LLM to rewrite the query first before passing it to our downstream modules - retrieval/reranking/synthesis.\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.postprocessor.cohere\\_rerank import CohereRerank\nfrom llama\\_index.core.response\\_synthesizers import TreeSummarize\n\n\\# define modules\nprompt\\_str \\= \"Please generate a question about Paul Graham's life regarding the following topic {topic}\"\nprompt\\_tmpl \\= PromptTemplate(prompt\\_str)\nllm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\nretriever \\= index.as\\_retriever(similarity\\_top\\_k\\=3)\nreranker \\= CohereRerank()\nsummarizer \\= TreeSummarize(llm\\=llm)\n\nfrom llama\\_index.postprocessor.cohere\\_rerank import CohereRerank from llama\\_index.core.response\\_synthesizers import TreeSummarize # define modules prompt\\_str = \"Please generate a question about Paul Graham's life regarding the following topic {topic}\" prompt\\_tmpl = PromptTemplate(prompt\\_str) llm = OpenAI(model=\"gpt-3.5-turbo\") retriever = index.as\\_retriever(similarity\\_top\\_k=3) reranker = CohereRerank() summarizer = TreeSummarize(llm=llm)\n\nIn \\[ \\]:\n\nCopied!\n\n\\# define query pipeline\np \\= QueryPipeline(verbose\\=True)\np.add\\_modules(\n    {\n        \"llm\": llm,\n        \"prompt\\_tmpl\": prompt\\_tmpl,\n        \"retriever\": retriever,\n        \"summarizer\": summarizer,\n        \"reranker\": reranker,\n    }\n)\n\n\\# define query pipeline p = QueryPipeline(verbose=True) p.add\\_modules( { \"llm\": llm, \"prompt\\_tmpl\": prompt\\_tmpl, \"retriever\": retriever, \"summarizer\": summarizer, \"reranker\": reranker, } )\n\nNext we draw links between modules with `add_link`. `add_link` takes in the source/destination module ids, and optionally the `source_key` and `dest_key`. Specify the `source_key` or `dest_key` if there are multiple outputs/inputs respectively.\n\nYou can view the set of input/output keys for each module through `module.as_query_component().input_keys` and `module.as_query_component().output_keys`.\n\nHere we explicitly specify `dest_key` for the `reranker` and `summarizer` modules because they take in two inputs (query\\_str and nodes).\n\nIn \\[ \\]:\n\nCopied!\n\np.add\\_link(\"prompt\\_tmpl\", \"llm\")\np.add\\_link(\"llm\", \"retriever\")\np.add\\_link(\"retriever\", \"reranker\", dest\\_key\\=\"nodes\")\np.add\\_link(\"llm\", \"reranker\", dest\\_key\\=\"query\\_str\")\np.add\\_link(\"reranker\", \"summarizer\", dest\\_key\\=\"nodes\")\np.add\\_link(\"llm\", \"summarizer\", dest\\_key\\=\"query\\_str\")\n\n\\# look at summarizer input keys\nprint(summarizer.as\\_query\\_component().input\\_keys)\n\np.add\\_link(\"prompt\\_tmpl\", \"llm\") p.add\\_link(\"llm\", \"retriever\") p.add\\_link(\"retriever\", \"reranker\", dest\\_key=\"nodes\") p.add\\_link(\"llm\", \"reranker\", dest\\_key=\"query\\_str\") p.add\\_link(\"reranker\", \"summarizer\", dest\\_key=\"nodes\") p.add\\_link(\"llm\", \"summarizer\", dest\\_key=\"query\\_str\") # look at summarizer input keys print(summarizer.as\\_query\\_component().input\\_keys)\n\nrequired\\_keys={'query\\_str', 'nodes'} optional\\_keys=set()\n\nWe use `networkx` to store the graph representation. This gives us an easy way to view the DAG!\n\nIn \\[ \\]:\n\nCopied!\n\n\\## create graph\nfrom pyvis.network import Network\n\nnet \\= Network(notebook\\=True, cdn\\_resources\\=\"in\\_line\", directed\\=True)\nnet.from\\_nx(p.dag)\nnet.show(\"rag\\_dag.html\")\n\n\\## another option using \\`pygraphviz\\`\n\\# from networkx.drawing.nx\\_agraph import to\\_agraph\n\\# from IPython.display import Image\n\\# agraph = to\\_agraph(p.dag)\n\\# agraph.layout(prog=\"dot\")\n\\# agraph.draw('rag\\_dag.png')\n\\# display(Image('rag\\_dag.png'))\n\n\\## create graph from pyvis.network import Network net = Network(notebook=True, cdn\\_resources=\"in\\_line\", directed=True) net.from\\_nx(p.dag) net.show(\"rag\\_dag.html\") ## another option using \\`pygraphviz\\` # from networkx.drawing.nx\\_agraph import to\\_agraph # from IPython.display import Image # agraph = to\\_agraph(p.dag) # agraph.layout(prog=\"dot\") # agraph.draw('rag\\_dag.png') # display(Image('rag\\_dag.png'))\n\nrag\\_dag.html\n\nOut\\[ \\]:\n\nIn \\[ \\]:\n\nCopied!\n\nresponse \\= p.run(topic\\=\"YC\")\n\nresponse = p.run(topic=\"YC\")\n\n\\> Running module prompt\\_tmpl with input: \ntopic: YC\n\n\\> Running module llm with input: \nmessages: Please generate a question about Paul Graham's life regarding the following topic YC\n\n\\> Running module retriever with input: \ninput: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?\n\n\\> Running module reranker with input: \nquery\\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?\nnodes: \\[NodeWithScore(node=TextNode(id\\_='ccd39041-5a64-4bd3-aca7-48f804b5a23f', embedding=None, metadata={'file\\_path': '../data/paul\\_graham/paul\\_graham\\_essay.txt', 'file\\_name': 'paul\\_graham\\_essay.txt', 'file...\n\n\\> Running module summarizer with input: \nquery\\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?\nnodes: \\[NodeWithScore(node=TextNode(id\\_='120574dd-a5c9-4985-ab3e-37b1070b500a', embedding=None, metadata={'file\\_path': '../data/paul\\_graham/paul\\_graham\\_essay.txt', 'file\\_name': 'paul\\_graham\\_essay.txt', 'file...\n\nIn \\[ \\]:\n\nCopied!\n\nprint(str(response))\n\nprint(str(response))\n\nPaul Graham played a significant role in the founding and development of Y Combinator (YC). He was one of the co-founders of YC and provided the initial funding for the investment firm. Along with his partners, he implemented the ideas they had been discussing and started their own investment firm. Paul Graham also played a key role in shaping the unique batch model of YC, where a group of startups is funded and provided intensive support for a period of three months. He was actively involved in selecting and helping the founders, and he also wrote essays and worked on YC's internal software.\n\nIn \\[ \\]:\n\nCopied!\n\n\\# you can do async too\nresponse \\= await p.arun(topic\\=\"YC\")\nprint(str(response))\n\n\\# you can do async too response = await p.arun(topic=\"YC\") print(str(response))\n\n\\> Running modules and inputs in parallel: \nModule key: prompt\\_tmpl. Input: \ntopic: YC\n\n\\> Running modules and inputs in parallel: \nModule key: llm. Input: \nmessages: Please generate a question about Paul Graham's life regarding the following topic YC\n\n\\> Running modules and inputs in parallel: \nModule key: retriever. Input: \ninput: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?\n\n\\> Running modules and inputs in parallel: \nModule key: reranker. Input: \nquery\\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?\nnodes: \\[NodeWithScore(node=TextNode(id\\_='ccd39041-5a64-4bd3-aca7-48f804b5a23f', embedding=None, metadata={'file\\_path': '../data/paul\\_graham/paul\\_graham\\_essay.txt', 'file\\_name': 'paul\\_graham\\_essay.txt', 'file...\n\n\\> Running modules and inputs in parallel: \nModule key: summarizer. Input: \nquery\\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?\nnodes: \\[NodeWithScore(node=TextNode(id\\_='120574dd-a5c9-4985-ab3e-37b1070b500a', embedding=None, metadata={'file\\_path': '../data/paul\\_graham/paul\\_graham\\_essay.txt', 'file\\_name': 'paul\\_graham\\_essay.txt', 'file...\n\nPaul Graham played a significant role in the founding and development of Y Combinator (YC). He was one of the co-founders of YC and provided the initial funding for the investment firm. Along with his partners, he implemented the ideas they had been discussing and decided to start their own investment firm. Paul Graham also played a key role in shaping the unique batch model of YC, where a group of startups is funded and provided intensive support for a period of three months. He was actively involved in selecting and helping the founders and worked on various projects related to YC, including writing essays and developing internal software.\n\n### 2\\. RAG Pipeline without Query Rewriting[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#2-rag-pipeline-without-query-rewriting)\n\nHere we setup a RAG pipeline without the query rewriting step.\n\nHere we need a way to link the input query to both the retriever, reranker, and summarizer. We can do this by defining a special `InputComponent`, allowing us to link the inputs to multiple downstream modules.\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.postprocessor.cohere\\_rerank import CohereRerank\nfrom llama\\_index.core.response\\_synthesizers import TreeSummarize\nfrom llama\\_index.core.query\\_pipeline import InputComponent\n\nretriever \\= index.as\\_retriever(similarity\\_top\\_k\\=5)\nsummarizer \\= TreeSummarize(llm\\=OpenAI(model\\=\"gpt-3.5-turbo\"))\nreranker \\= CohereRerank()\n\nfrom llama\\_index.postprocessor.cohere\\_rerank import CohereRerank from llama\\_index.core.response\\_synthesizers import TreeSummarize from llama\\_index.core.query\\_pipeline import InputComponent retriever = index.as\\_retriever(similarity\\_top\\_k=5) summarizer = TreeSummarize(llm=OpenAI(model=\"gpt-3.5-turbo\")) reranker = CohereRerank()\n\nIn \\[ \\]:\n\nCopied!\n\np \\= QueryPipeline(verbose\\=True)\np.add\\_modules(\n    {\n        \"input\": InputComponent(),\n        \"retriever\": retriever,\n        \"summarizer\": summarizer,\n    }\n)\np.add\\_link(\"input\", \"retriever\")\np.add\\_link(\"input\", \"summarizer\", dest\\_key\\=\"query\\_str\")\np.add\\_link(\"retriever\", \"summarizer\", dest\\_key\\=\"nodes\")\n\np = QueryPipeline(verbose=True) p.add\\_modules( { \"input\": InputComponent(), \"retriever\": retriever, \"summarizer\": summarizer, } ) p.add\\_link(\"input\", \"retriever\") p.add\\_link(\"input\", \"summarizer\", dest\\_key=\"query\\_str\") p.add\\_link(\"retriever\", \"summarizer\", dest\\_key=\"nodes\")\n\nIn \\[ \\]:\n\nCopied!\n\noutput \\= p.run(input\\=\"what did the author do in YC\")\n\noutput = p.run(input=\"what did the author do in YC\")\n\n\\> Running module input with input: \ninput: what did the author do in YC\n\n\\> Running module retriever with input: \ninput: what did the author do in YC\n\n\\> Running module summarizer with input: \nquery\\_str: what did the author do in YC\nnodes: \\[NodeWithScore(node=TextNode(id\\_='86dea730-ca35-4bcb-9f9b-4c99e8eadd08', embedding=None, metadata={'file\\_path': '../data/paul\\_graham/paul\\_graham\\_essay.txt', 'file\\_name': 'paul\\_graham\\_essay.txt', 'file...\n\nIn \\[ \\]:\n\nCopied!\n\nprint(str(output))\n\nprint(str(output))\n\nThe author worked on various projects at YC, including writing essays and working on YC's internal software. They also played a key role in the creation and operation of YC by funding the program with their own money and organizing a batch model where they would fund a group of startups twice a year. They provided support and guidance to the startups during a three-month intensive program and used their building in Cambridge as the headquarters for YC. Additionally, they hosted weekly dinners where experts on startups would give talks.\n\nDefining a Custom Component in a Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#defining-a-custom-component-in-a-query-pipeline)\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nYou can easily define a custom component. Simply subclass a `QueryComponent`, implement validation/run functions + some helpers, and plug it in.\n\nLet's wrap the related movie generation prompt+LLM chain from the first example into a custom component.\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.core.query\\_pipeline import (\n    CustomQueryComponent,\n    InputKeys,\n    OutputKeys,\n)\nfrom typing import Dict, Any\nfrom llama\\_index.core.llms.llm import LLM\nfrom pydantic import Field\n\nclass RelatedMovieComponent(CustomQueryComponent):\n    \"\"\"Related movie component.\"\"\"\n\n    llm: LLM \\= Field(..., description\\=\"OpenAI LLM\")\n\n    def \\_validate\\_component\\_inputs(\n        self, input: Dict\\[str, Any\\]\n    ) \\-\\> Dict\\[str, Any\\]:\n        \"\"\"Validate component inputs during run\\_component.\"\"\"\n        \\# NOTE: this is OPTIONAL but we show you here how to do validation as an example\n        return input\n\n    @property\n    def \\_input\\_keys(self) \\-\\> set:\n        \"\"\"Input keys dict.\"\"\"\n        \\# NOTE: These are required inputs. If you have optional inputs please override\n        \\# \\`optional\\_input\\_keys\\_dict\\`\n        return {\"movie\"}\n\n    @property\n    def \\_output\\_keys(self) \\-\\> set:\n        return {\"output\"}\n\n    def \\_run\\_component(self, \\*\\*kwargs) \\-\\> Dict\\[str, Any\\]:\n        \"\"\"Run the component.\"\"\"\n        \\# use QueryPipeline itself here for convenience\n        prompt\\_str \\= \"Please generate related movies to {movie\\_name}\"\n        prompt\\_tmpl \\= PromptTemplate(prompt\\_str)\n        p \\= QueryPipeline(chain\\=\\[prompt\\_tmpl, llm\\])\n        return {\"output\": p.run(movie\\_name\\=kwargs\\[\"movie\"\\])}\n\nfrom llama\\_index.core.query\\_pipeline import ( CustomQueryComponent, InputKeys, OutputKeys, ) from typing import Dict, Any from llama\\_index.core.llms.llm import LLM from pydantic import Field class RelatedMovieComponent(CustomQueryComponent): \"\"\"Related movie component.\"\"\" llm: LLM = Field(..., description=\"OpenAI LLM\") def \\_validate\\_component\\_inputs( self, input: Dict\\[str, Any\\] ) -\\> Dict\\[str, Any\\]: \"\"\"Validate component inputs during run\\_component.\"\"\" # NOTE: this is OPTIONAL but we show you here how to do validation as an example return input @property def \\_input\\_keys(self) -\\> set: \"\"\"Input keys dict.\"\"\" # NOTE: These are required inputs. If you have optional inputs please override # \\`optional\\_input\\_keys\\_dict\\` return {\"movie\"} @property def \\_output\\_keys(self) -\\> set: return {\"output\"} def \\_run\\_component(self, \\*\\*kwargs) -\\> Dict\\[str, Any\\]: \"\"\"Run the component.\"\"\" # use QueryPipeline itself here for convenience prompt\\_str = \"Please generate related movies to {movie\\_name}\" prompt\\_tmpl = PromptTemplate(prompt\\_str) p = QueryPipeline(chain=\\[prompt\\_tmpl, llm\\]) return {\"output\": p.run(movie\\_name=kwargs\\[\"movie\"\\])}\n\nLet's try the custom component out! We'll also add a step to convert the output to Shakespeare.\n\nIn \\[ \\]:\n\nCopied!\n\nllm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\ncomponent \\= RelatedMovieComponent(llm\\=llm)\n\n\\# let's add some subsequent prompts for fun\nprompt\\_str \\= \"\"\"\\\\\nHere's some text:\n\n{text}\n\nCan you rewrite this in the voice of Shakespeare?\n\"\"\"\nprompt\\_tmpl \\= PromptTemplate(prompt\\_str)\n\np \\= QueryPipeline(chain\\=\\[component, prompt\\_tmpl, llm\\], verbose\\=True)\n\nllm = OpenAI(model=\"gpt-3.5-turbo\") component = RelatedMovieComponent(llm=llm) # let's add some subsequent prompts for fun prompt\\_str = \"\"\"\\\\ Here's some text: {text} Can you rewrite this in the voice of Shakespeare? \"\"\" prompt\\_tmpl = PromptTemplate(prompt\\_str) p = QueryPipeline(chain=\\[component, prompt\\_tmpl, llm\\], verbose=True)\n\nIn \\[ \\]:\n\nCopied!\n\noutput \\= p.run(movie\\=\"Love Actually\")\n\noutput = p.run(movie=\"Love Actually\")\n\n\\> Running module 31ca224a-f226-4956-882b-73878843d869 with input: \nmovie: Love Actually\n\n\\> Running module febb41b5-2528-416a-bde7-6accdb0f9c51 with input: \ntext: assistant: 1. \"Valentine's Day\" (2010)\n2. \"New Year's Eve\" (2011)\n3. \"The Holiday\" (2006)\n4. \"Crazy, Stupid, Love\" (2011)\n5. \"Notting Hill\" (1999)\n6. \"Four Weddings and a Funeral\" (1994)\n7. \"Bridget J...\n\n\\> Running module e834ffbe-e97c-4ab0-9726-24f1534745b2 with input: \nmessages: Here's some text:\n\n1. \"Valentine's Day\" (2010)\n2. \"New Year's Eve\" (2011)\n3. \"The Holiday\" (2006)\n4. \"Crazy, Stupid, Love\" (2011)\n5. \"Notting Hill\" (1999)\n6. \"Four Weddings and a Funeral\" (1994)\n7. \"B...\n\nIn \\[ \\]:\n\nCopied!\n\nprint(str(output))\n\nprint(str(output))\n\nassistant: 1. \"Valentine's Day\" (2010) - \"A day of love, where hearts entwine, \n   And Cupid's arrow finds its mark divine.\"\n\n2. \"New Year's Eve\" (2011) - \"When old year fades, and new year dawns,\n   We gather 'round, to celebrate the morns.\"\n\n3. \"The Holiday\" (2006) - \"Two souls, adrift in search of cheer,\n   Find solace in a holiday so dear.\"\n\n4. \"Crazy, Stupid, Love\" (2011) - \"A tale of love, both wild and mad,\n   Where hearts are lost, then found, and glad.\"\n\n5. \"Notting Hill\" (1999) - \"In London town, where love may bloom,\n   A humble man finds love, and breaks the gloom.\"\n\n6. \"Four Weddings and a Funeral\" (1994) - \"Four times the vows, and one time mourn,\n   Love's journey, with laughter and tears adorned.\"\n\n7. \"Bridget Jones's Diary\" (2001) - \"A maiden fair, with wit and charm,\n   Records her life, and love's alarm.\"\n\n8. \"About Time\" (2013) - \"A tale of time, where love transcends,\n   And moments cherished, never truly ends.\"\n\n9. \"The Best Exotic Marigold Hotel\" (2011) - \"In India's land, where dreams unfold,\n   A hotel blooms, where hearts find gold.\"\n\n10. \"The Notebook\" (2004) - \"A love that spans both time and space,\n    Where words and memories find their place.\"\n\n11. \"Serendipity\" (2001) - \"By chance or fate, two souls collide,\n    In search of love, they cannot hide.\"\n\n12. \"P.S. I Love You\" (2007) - \"In letters penned, from love's embrace,\n    A departed soul, still finds its trace.\"\n\n13. \"500 Days of Summer\" (2009) - \"A tale of love, both sweet and sour,\n    Where seasons change, and hearts devour.\"\n\n14. \"The Fault in Our Stars\" (2014) - \"Two hearts, aflame, in starlit skies,\n    Love's tragedy, where hope never dies.\"\n\n15. \"La La Land\" (2016) - \"In dreams and songs, two hearts entwine,\n    A city's magic, where love's stars align.\"\n\nStepwise Execution of a Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#stepwise-execution-of-a-pipeline)\n--------------------------------------------------------------------------------------------------------------------------------------------\n\nExecuting a pipeline one step at a time is a great idea if you:\n\n*   want to better debug the order of execution\n*   log data in between each step\n*   give feedback to a user as to what is being processed\n*   and more!\n\nTo execute a pipeline, you must create a `run_state`, and then loop through the exection. A basic example is below.\n\nIn \\[ \\]:\n\nCopied!\n\nfrom llama\\_index.core.query\\_pipeline import QueryPipeline\nfrom llama\\_index.core import PromptTemplate\nfrom llama\\_index.llms.openai import OpenAI\n\n\\# try chaining basic prompts\nprompt\\_str \\= \"Please generate related movies to {movie\\_name}\"\nprompt\\_tmpl \\= PromptTemplate(prompt\\_str)\nllm \\= OpenAI(model\\=\"gpt-3.5-turbo\")\n\np \\= QueryPipeline(chain\\=\\[prompt\\_tmpl, llm\\], verbose\\=True)\n\nfrom llama\\_index.core.query\\_pipeline import QueryPipeline from llama\\_index.core import PromptTemplate from llama\\_index.llms.openai import OpenAI # try chaining basic prompts prompt\\_str = \"Please generate related movies to {movie\\_name}\" prompt\\_tmpl = PromptTemplate(prompt\\_str) llm = OpenAI(model=\"gpt-3.5-turbo\") p = QueryPipeline(chain=\\[prompt\\_tmpl, llm\\], verbose=True)\n\nIn \\[ \\]:\n\nCopied!\n\nrun\\_state \\= p.get\\_run\\_state(movie\\_name\\=\"The Departed\")\n\nnext\\_module\\_keys \\= p.get\\_next\\_module\\_keys(run\\_state)\n\nwhile True:\n    for module\\_key in next\\_module\\_keys:\n        \\# get the module and input\n        module \\= run\\_state.module\\_dict\\[module\\_key\\]\n        module\\_input \\= run\\_state.all\\_module\\_inputs\\[module\\_key\\]\n\n        \\# run the module\n        output\\_dict \\= module.run\\_component(\\*\\*module\\_input)\n\n        \\# process the output\n        p.process\\_component\\_output(\n            output\\_dict,\n            module\\_key,\n            run\\_state,\n        )\n\n    \\# get the next module keys\n    next\\_module\\_keys \\= p.get\\_next\\_module\\_keys(\n        run\\_state,\n    )\n\n    \\# if no more modules to run, break\n    if not next\\_module\\_keys:\n        run\\_state.result\\_outputs\\[module\\_key\\] \\= output\\_dict\n        break\n\n\\# the final result is at \\`module\\_key\\`\n\\# it is a dict of 'output' -\\> ChatResponse object in this case\nprint(run\\_state.result\\_outputs\\[module\\_key\\]\\[\"output\"\\].message.content)\n\nrun\\_state = p.get\\_run\\_state(movie\\_name=\"The Departed\") next\\_module\\_keys = p.get\\_next\\_module\\_keys(run\\_state) while True: for module\\_key in next\\_module\\_keys: # get the module and input module = run\\_state.module\\_dict\\[module\\_key\\] module\\_input = run\\_state.all\\_module\\_inputs\\[module\\_key\\] # run the module output\\_dict = module.run\\_component(\\*\\*module\\_input) # process the output p.process\\_component\\_output( output\\_dict, module\\_key, run\\_state, ) # get the next module keys next\\_module\\_keys = p.get\\_next\\_module\\_keys( run\\_state, ) # if no more modules to run, break if not next\\_module\\_keys: run\\_state.result\\_outputs\\[module\\_key\\] = output\\_dict break # the final result is at \\`module\\_key\\` # it is a dict of 'output' -\\> ChatResponse object in this case print(run\\_state.result\\_outputs\\[module\\_key\\]\\[\"output\"\\].message.content)\n\n1\\. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\n2. The Town (2010) - A crime thriller directed by Ben Affleck\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\n4. Goodfellas (1990) - A classic mobster film directed by Martin Scorsese\n5. The Irishman (2019) - Another crime drama directed by Martin Scorsese, starring Robert De Niro and Al Pacino\n6. The Departed (2006) - The Departed is a 2006 American crime film directed by Martin Scorsese and written by William Monahan. It is a remake of the 2002 Hong Kong film Infernal Affairs. The film stars Leonardo DiCaprio, Matt Damon, Jack Nicholson, and Mark Wahlberg, with Martin Sheen, Ray Winstone, Vera Farmiga, and Alec Baldwin in supporting roles.\n\nBack to top\n\n[Previous Sub Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)[Next Query Pipeline with Async/Parallel Execution](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/)\n\n![Image 6](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)",
  "usage": {
    "tokens": 61450
  }
}
```
