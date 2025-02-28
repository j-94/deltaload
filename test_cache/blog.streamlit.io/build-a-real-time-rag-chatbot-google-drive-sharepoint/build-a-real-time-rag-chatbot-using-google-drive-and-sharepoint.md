---
title: Build a real-time RAG chatbot using Google Drive and Sharepoint
description: Keep your chatbot’s knowledge base up-to-date with Pathway and LlamaIndex
url: https://blog.streamlit.io/build-a-real-time-rag-chatbot-google-drive-sharepoint/
timestamp: 2025-01-20T15:59:51.946Z
domain: blog.streamlit.io
path: build-a-real-time-rag-chatbot-google-drive-sharepoint
---

# Build a real-time RAG chatbot using Google Drive and Sharepoint


Keep your chatbot’s knowledge base up-to-date with Pathway and LlamaIndex


## Content

In this post, we explore how to build a real-time RAG app with up-to-date information from your files stored in Google Drive or Sharepoint. This means that your chatbot will always have access to the most recent version of your knowledge base—no manual pipeline reruns needed. By the end of this tutorial, you’ll use Pathway and LlamaIndex to build a RAG chatbot that instantly updates.

**Why Pathway?**
----------------

Pathway is an open data processing framework. It allows you to easily develop data transformation pipelines and ML apps that work with live data sources. Pathway listens to your documents for changes, additions, and removals. It handles loading and indexing without ETL.

Pathway offers an indexing solution that is always up-to-date without the need for traditional ETL pipelines. It can monitor several data sources (such as files, S3 folders, and cloud storage) and provide the latest info to your LLM app.

This means you don’t need to worry about:

*   Checking files to see if there are any changes
*   Parsing PDFs, Word documents, or other text files
*   Transforming, embedding documents, and loading them into a vector database

Once updates are made to the files that make up your knowledge base, the updated content is immediately re-indexed — you don’t have to deal with rerunning the pipeline.

**App overview**
----------------

This demo consists of three parts.

1.  For up-to-date knowledge and information retrieval from the knowledge base’s documents, Pathway’s vector store is used.
2.  LlamaIndex creates the RAG pipeline and offers chat memory.
3.  Streamlit powers the easy-to-navigate user interface.

**Tutorial: Creating a real-time RAG app with Pathway + LlamaIndex**
--------------------------------------------------------------------

🏂

Want to jump right in? Check out the [app](https://chat-realtime-sharepoint-gdrive.streamlit.app/?ref=blog.streamlit.io) to see how it works or explore the code in the [GitHub repository](https://github.com/pathway-labs/realtime-indexer-qa-chat/blob/main/demo/app.py?ref=blog.streamlit.io).

Prerequisites
-------------

*   An OpenAI API key (check out [our instructions](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/#step-1-get-an-openai-api-key) if you don’t already have one)
*   [A Pathway instance](https://pathway.com/solutions/ai-pipelines?ref=blog.streamlit.io) (the hosted version is provided free for the demo)

1\. Adding data to the knowledge base
-------------------------------------

Pathway can listen to many sources simultaneously, such as local files, S3 folders, cloud storage, and data streams. In this example, you’ll add example documents to your pipeline by uploading files to a Google Drive registered to Pathway as a source. You can also check out the [full docs on Pathway’s Google Drive connector](https://pathway.com/developers/user-guide/connectors/gdrive-connector/?ref=blog.streamlit.io).

For this demo, a Google Drive folder is provided for you to upload files. To test the app, we’ll ask our assistant questions about Pathway and it will respond based on the available files in the Google Drive folder.

See [pathway-io](https://pathway.com/developers/api-docs/pathway-io?ref=blog.streamlit.io) for more information on available connectors and how to implement custom connectors.

2\. Building a Pathway-powered chatbot
--------------------------------------

### Retriever

First, import the necessary modules for the app.

```
from llama_index.retrievers import PathwayRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.chat_engine.condense_question import CondenseQuestionChatEngine
from rag import chat_engine
```

Initialize the retriever with the hosted Pathway instance and create the query engine:

```
PATHWAY_HOST = "api-pathway-indexer.staging.deploys.pathway.com"
PATHWAY_PORT = 80

retriever = PathwayRetriever(host=PATHWAY_HOST, port=PATHWAY_PORT)
```

### Chat Engine

We use `CondenseQuestionChatEngine` to create the RAG chatbot with LlamaIndex. One advantage of this chat engine is that it uses the context provided in the conversation history to write the search query. This results in answers that are more contextually relevant.

For further improvements to the pipeline, you can modify the chat engine type, prompt, and other parameters. For simplicity, we’ll use the default settings.

```
chat_engine = CondensePlusContextChatEngine.from_defaults(
    retriever=retriever,
    verbose=True,
)
```

3\. Creating the UI with Streamlit
----------------------------------

Create a title for the app and initialize session state values for the chatbot’s message history and the chat engine.

```
st.title("Pathway + LlamaIndex")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, ask me a question. My knowledge is always up to date!"}
    ]

    st.session_state.chat_engine = chat_engine
```

Prompt the user for a question, store any user input in session state, and print messages from the user and the assistant.

```
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
```

If the last message is from the user and the assistant is preparing an answer, create a `st.spinner` widget. Add the message content and role to the message history.

```
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
```

Running the app
---------------

The demo is hosted on Streamlit Community Cloud [here](https://chat-realtime-sharepoint-gdrive.streamlit.app/?ref=blog.streamlit.io). This version of the app uses Pathway's [hosted document pipelines](https://cloud.pathway.com/docindex?ref=blog.streamlit.io).

### **On your local machine**

1.  Clone [this repository](https://github.com/pathway-labs/realtime-indexer-qa-chat?ref=blog.streamlit.io) locally.
2.  Create a `.env` file under the root folder to store your OpenAI API key. This demo uses the OpenAI GPT model to answer questions.
3.  You also need a Pathway instance for vector search. For local deployment, see the [vector store guide](https://pathway.com/developers/showcases/vectorstore_pipeline?ref=blog.streamlit.io) and [Pathway Deployment](https://pathway.com/developers/user-guide/deployment/docker-deployment?ref=blog.streamlit.io).
4.  Run `streamlit run ui.py`.

Congrats! Now you’re ready to chat with your documents and any file updates will be reflected by your app in real-time, thanks to Pathway.

Summing up
----------

In this tutorial, you created and deployed a real-time RAG chatbot app. You also learned how easy it is to use Streamlit, LlamaIndex, and Pathway together, thanks to LlamaIndex’s Pathway Retriever. The end result is a RAG app that always has access to the most up-to-date version of your knowledge base.

## Metadata

```json
{
  "title": "Build a real-time RAG chatbot using Google Drive and Sharepoint",
  "description": "Keep your chatbot’s knowledge base up-to-date with Pathway and LlamaIndex",
  "url": "https://blog.streamlit.io/build-a-real-time-rag-chatbot-google-drive-sharepoint/",
  "content": "In this post, we explore how to build a real-time RAG app with up-to-date information from your files stored in Google Drive or Sharepoint. This means that your chatbot will always have access to the most recent version of your knowledge base—no manual pipeline reruns needed. By the end of this tutorial, you’ll use Pathway and LlamaIndex to build a RAG chatbot that instantly updates.\n\n**Why Pathway?**\n----------------\n\nPathway is an open data processing framework. It allows you to easily develop data transformation pipelines and ML apps that work with live data sources. Pathway listens to your documents for changes, additions, and removals. It handles loading and indexing without ETL.\n\nPathway offers an indexing solution that is always up-to-date without the need for traditional ETL pipelines. It can monitor several data sources (such as files, S3 folders, and cloud storage) and provide the latest info to your LLM app.\n\nThis means you don’t need to worry about:\n\n*   Checking files to see if there are any changes\n*   Parsing PDFs, Word documents, or other text files\n*   Transforming, embedding documents, and loading them into a vector database\n\nOnce updates are made to the files that make up your knowledge base, the updated content is immediately re-indexed — you don’t have to deal with rerunning the pipeline.\n\n**App overview**\n----------------\n\nThis demo consists of three parts.\n\n1.  For up-to-date knowledge and information retrieval from the knowledge base’s documents, Pathway’s vector store is used.\n2.  LlamaIndex creates the RAG pipeline and offers chat memory.\n3.  Streamlit powers the easy-to-navigate user interface.\n\n**Tutorial: Creating a real-time RAG app with Pathway + LlamaIndex**\n--------------------------------------------------------------------\n\n🏂\n\nWant to jump right in? Check out the [app](https://chat-realtime-sharepoint-gdrive.streamlit.app/?ref=blog.streamlit.io) to see how it works or explore the code in the [GitHub repository](https://github.com/pathway-labs/realtime-indexer-qa-chat/blob/main/demo/app.py?ref=blog.streamlit.io).\n\nPrerequisites\n-------------\n\n*   An OpenAI API key (check out [our instructions](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/#step-1-get-an-openai-api-key) if you don’t already have one)\n*   [A Pathway instance](https://pathway.com/solutions/ai-pipelines?ref=blog.streamlit.io) (the hosted version is provided free for the demo)\n\n1\\. Adding data to the knowledge base\n-------------------------------------\n\nPathway can listen to many sources simultaneously, such as local files, S3 folders, cloud storage, and data streams. In this example, you’ll add example documents to your pipeline by uploading files to a Google Drive registered to Pathway as a source. You can also check out the [full docs on Pathway’s Google Drive connector](https://pathway.com/developers/user-guide/connectors/gdrive-connector/?ref=blog.streamlit.io).\n\nFor this demo, a Google Drive folder is provided for you to upload files. To test the app, we’ll ask our assistant questions about Pathway and it will respond based on the available files in the Google Drive folder.\n\nSee [pathway-io](https://pathway.com/developers/api-docs/pathway-io?ref=blog.streamlit.io) for more information on available connectors and how to implement custom connectors.\n\n2\\. Building a Pathway-powered chatbot\n--------------------------------------\n\n### Retriever\n\nFirst, import the necessary modules for the app.\n\n```\nfrom llama_index.retrievers import PathwayRetriever\nfrom llama_index.query_engine import RetrieverQueryEngine\nfrom llama_index.chat_engine.condense_question import CondenseQuestionChatEngine\nfrom rag import chat_engine\n```\n\nInitialize the retriever with the hosted Pathway instance and create the query engine:\n\n```\nPATHWAY_HOST = \"api-pathway-indexer.staging.deploys.pathway.com\"\nPATHWAY_PORT = 80\n\nretriever = PathwayRetriever(host=PATHWAY_HOST, port=PATHWAY_PORT)\n```\n\n### Chat Engine\n\nWe use `CondenseQuestionChatEngine` to create the RAG chatbot with LlamaIndex. One advantage of this chat engine is that it uses the context provided in the conversation history to write the search query. This results in answers that are more contextually relevant.\n\nFor further improvements to the pipeline, you can modify the chat engine type, prompt, and other parameters. For simplicity, we’ll use the default settings.\n\n```\nchat_engine = CondensePlusContextChatEngine.from_defaults(\n    retriever=retriever,\n    verbose=True,\n)\n```\n\n3\\. Creating the UI with Streamlit\n----------------------------------\n\nCreate a title for the app and initialize session state values for the chatbot’s message history and the chat engine.\n\n```\nst.title(\"Pathway + LlamaIndex\")\n\nif \"messages\" not in st.session_state.keys():\n    st.session_state.messages = [\n        {\"role\": \"assistant\", \"content\": \"Hi, ask me a question. My knowledge is always up to date!\"}\n    ]\n\n    st.session_state.chat_engine = chat_engine\n```\n\nPrompt the user for a question, store any user input in session state, and print messages from the user and the assistant.\n\n```\nif prompt := st.chat_input(\"Your question\"):\n    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n\nfor message in st.session_state.messages:\n    with st.chat_message(message[\"role\"]):\n        st.write(message[\"content\"])\n```\n\nIf the last message is from the user and the assistant is preparing an answer, create a `st.spinner` widget. Add the message content and role to the message history.\n\n```\nif st.session_state.messages[-1][\"role\"] != \"assistant\":\n    with st.chat_message(\"assistant\"):\n        with st.spinner(\"Thinking...\"):\n            response = st.session_state.chat_engine.chat(prompt)\n            st.write(response.response)\n            message = {\"role\": \"assistant\", \"content\": response.response}\n            st.session_state.messages.append(message)\n```\n\nRunning the app\n---------------\n\nThe demo is hosted on Streamlit Community Cloud [here](https://chat-realtime-sharepoint-gdrive.streamlit.app/?ref=blog.streamlit.io). This version of the app uses Pathway's [hosted document pipelines](https://cloud.pathway.com/docindex?ref=blog.streamlit.io).\n\n### **On your local machine**\n\n1.  Clone [this repository](https://github.com/pathway-labs/realtime-indexer-qa-chat?ref=blog.streamlit.io) locally.\n2.  Create a `.env` file under the root folder to store your OpenAI API key. This demo uses the OpenAI GPT model to answer questions.\n3.  You also need a Pathway instance for vector search. For local deployment, see the [vector store guide](https://pathway.com/developers/showcases/vectorstore_pipeline?ref=blog.streamlit.io) and [Pathway Deployment](https://pathway.com/developers/user-guide/deployment/docker-deployment?ref=blog.streamlit.io).\n4.  Run `streamlit run ui.py`.\n\nCongrats! Now you’re ready to chat with your documents and any file updates will be reflected by your app in real-time, thanks to Pathway.\n\nSumming up\n----------\n\nIn this tutorial, you created and deployed a real-time RAG chatbot app. You also learned how easy it is to use Streamlit, LlamaIndex, and Pathway together, thanks to LlamaIndex’s Pathway Retriever. The end result is a RAG app that always has access to the most up-to-date version of your knowledge base.",
  "publishedTime": "2024-03-07T23:12:48.000Z",
  "usage": {
    "tokens": 1635
  }
}
```
