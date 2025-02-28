---
title: Making Retrieval Augmented Generation Fast | Pinecone
description: Retrieval Augmented Generation (RAG) is the go-to method for adding external knowledge to Large Language Models (LLMs). RAG with agents can be slow, but we can make it much faster using NVIDIA NeMo Guardrails. We explain how here.
url: https://www.pinecone.io/learn/fast-retrieval-augmented-generation/
timestamp: 2025-01-20T15:44:20.005Z
domain: www.pinecone.io
path: learn_fast-retrieval-augmented-generation
---

# Making Retrieval Augmented Generation Fast | Pinecone


Retrieval Augmented Generation (RAG) is the go-to method for adding external knowledge to Large Language Models (LLMs). RAG with agents can be slow, but we can make it much faster using NVIDIA NeMo Guardrails. We explain how here.


## Content

**L**arge **L**anguage **M**odels (LLMs) are incredible tools, but they're useless as soon as we require up-to-date or cited information. The reason for this is the learning strategy for all _"parametric knowledge"_ of LLMs.

Parametric knowledge refers to the information an LLM learns during its training phase. During training, the LLM learns to encode information from the training dataset into its internal model parameters — the model's parametric knowledge.

To add new parametric knowledge, we must fine-tune an LLM. Training, whether pretraining (which costs a reported $100M for GPT-4 \[1\]) or fine-tuning, is expensive and slow. Expensive and slow are not qualities we want when needing to keep our LLM knowledge up to date.

[**R**etrieval **A**ugmented **G**eneration (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation//) has become the people's method for solving this problem. Rather than baking knowledge into the LLM via fine-tuning, we insert an external "knowledge base" into the LLM. When done well, this knowledge base is scalable, we can manage it as we would a traditional DB, and it can be significantly more reliable than fine-tuning.

Video walkthrough for super fast Retrieval Augmented Generation (RAG).

* * *

Approaches to RAG
-----------------

**R**etrieval **A**ugmented **G**eneration (RAG) allows us to update the knowledge of LLMs via the model's _"source knowledge"_. The source knowledge refers to any information fed into the LLM via the input prompt.

![Image 10: The most common approach to RAG.](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fcaa233388a98715de2036dbf2bf2743e6e049b36-2283x1145.png&w=3840&q=75)

The most common approach to RAG.

Using RAG and source knowledge, we retrieve relevant information from an external data source, augment our prompt with this additional source knowledge, and feed that information into the LLM. This approach is compelling because it allows us to keep LLM knowledge accurate and up to date with minimal cost.

The above describes what I refer to as "naive RAG". Naive RAG is the most common implementation. It is simple, efficient, and effective.

However, there are other ways of doing RAG. The other popular approach is to use [_agents_](https://www.pinecone.io/learn/series/langchain/langchain-agents/) that have access to RAG tools.

At its core, an agent is an LLM with added logic that allows it to reason over multiple generation steps, decide to use various tools, and specify _how_ to use those tools.

![Image 11: Example reasoning and action logic from an agent framework called ReAct [2].](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F4defbaed3e9f223a658a87b9b625da131048c84d-2240x2024.png&w=3840&q=75)

Example reasoning and action logic from an agent framework called ReAct \[2\].

This methodology allows the agent to answer far more complex queries. Rather than needing to produce an answer in a single step, it can now formulate and execute a plan to construct the best possible answer.

RAG is one of the most common tools to give agents access to external knowledge. The advantage of this approach over the naive RAG approach primarily stems from the more advanced reasoning ability of the agent. It can decide _when_ to use RAG and how to use it. An agent can formulate a better search query based on the user's question, its parametric knowledge, and conversational history — it can also decide on additional parameters like how many results to return or whether to use [metadata filtering](https://www.pinecone.io/learn/vector-search-filtering/).

The problem with agent-powered RAG is speed and cost. Every reasoning step taken by an agent is a call to an LLM — LLMs are slow and expensive — so we will be waiting longer for a response and paying more money.

These two approaches to RAG are the most common. We have naive RAG and agent RAG. However, a _third option_ provides us with a middle ground between the two, a _best of both_. I like to call that option _RAG with Guardrails_.

RAG with Guardrails
-------------------

Rather than using a slow and expensive LLM call to decide which action to take, we can use _guardrails_. Guardrails can be described as _classifiers of user intent_. We can create a guardrail to identify queries that indicate someone is asking a question — when a user asks a question, the guardrails identify this intent and trigger the RAG pipeline.

![Image 12: Defining canonical forms (categories of user intent) with example utterances. The utterances are encoded into vector space, giving us a type of classifier function.](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Ff4c238be0ec0baa83e51ff227d26e8f3df1b7c8b-2895x1710.png&w=3840&q=75)

Defining canonical forms (categories of user intent) with example utterances. The utterances are encoded into vector space, giving us a type of classifier function.

The categories of user intent are called _"canonical forms"_. We define a canonical form by providing example queries (utterances) that we believe belong to that canonical form.

If we had a RAG pipeline that contained information about LLMs, we could define a canonical form that identifies when a user asks about LLMs. In the image above, we define this canonical form with `"define user ask llm"`. We then provide a few example queries that should trigger this form:

```
"what is the llama 2 model?"
"tell me about Meta's new LLM"
"what are the differences between Falcon and Llama?"
```

Each utterance is encoded into a semantic vector space, creating a semantic _"map"_. That map helps us line up semantic meaning and canonical forms.

![Image 13: User queries are encoded into the same vector space, allowing us to identify if they have a semantic similarity to an existing cano](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Ff8c83210f38b76eb84a589f8231ce69d8565c112-2293x1534.png&w=3840&q=75)

User queries are encoded into the same vector space, allowing us to identify if they have a semantic similarity to an existing cano

When a new user query comes in, we encode it into the same semantic vector space as our previous utterance examples. Using that map of utterances and the canonical forms they belong to, we can identify when a user query is semantically similar to those utterance examples. If the query is similar, we trigger the canonical form that those utterances belong to.

With that, we have a decision-making process in milliseconds rather than several seconds — as with agents.

Using RAG with guardrails does have nuances that we should consider. First, we must define the canonical forms. We could view the requirement of defining canonical forms in two ways: (1) we can be more deterministic about what should trigger a particular action, or (2) we lose out on the innate decision-making ability of an LLM.

RAG with guardrails allows us to insert a user query directly into an action — but it cannot rephrase the query, specify metadata filters, or decide how many results to return. On the other hand, using an agent makes those tasks easy. However, if we can infer these parameters deterministically with code, we can include them without using an LLM.

That gives us an idea of how RAG with guardrails works and its pros and cons. Let's jump into the implementation itself.

Implementing RAG with Guardrails
--------------------------------

To implement RAG with guardrails, we will rely on the [NVIDIA NeMo Guardrails library](https://www.pinecone.io/learn/nemo-guardrails-intro/). The library primarily focuses on AI safety by implementing "guardrails" as protective measures against unwanted interactions. However, we can also use these guardrails to trigger things like RAG.

```
!pip install -qU \
    nemoguardrails==0.4.0 \
    pinecone-client==2.2.2 \
    datasets==2.14.3 \
    openai==0.27.8
```

### Building the Knowledge Base

As with every RAG use case, we must first create our knowledge base. For that, we will use a small dataset of Llama 2 related ArXiv papers stored in Hugging Face — we download the dataset like so:

The data has already been preprocessed for this use case, so we don't need to worry about chunking — however, we need to reformat the data to keep only what we need for our knowledge base.

The `chunk` field contains the text we will encode and store inside Pinecone. To encode that data, we need to use an embedding model. We will use OpenAI's `text-embedding-ada-002` here, so we must authenticate ourselves with an [OpenAI API key](https://platform.openai.com/account/api-keys).

```
import os

# set your api key here
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
```

Then we create embeddings via the `openai.Embedding.create` endpoint like so:

As we fed two chunks of text into the embedding function, we received two embeddings (one for each chunk). Note that each is 1536-dimensional. We need this number when setting up our Pinecone index in a moment.

### Creating the Vector Index

Now, we need a place to store these embeddings and enable an efficient vector search through them all. To do that, we use Pinecone. We can get a [free API key](https://app.pinecone.io/) and enter it below, where we will initialize our connection to Pinecone.

```
import pinecone

# initialize connection to pinecone (get API key at app.pinecone.io)
api_key = "YOUR_API_KEY"
# find your environment next to the api key in pinecone console
env = "YOUR_ENV"

pinecone.init(api_key=api_key, environment=env)
```

Now, we create the vector index:

```
import time

index_name = "nemo-guardrails-rag-with-actions"

# check if index already exists (it shouldn't if this is first time)
if index_name not in pinecone.list_indexes():
    # if does not exist, create index
    pinecone.create_index(
        index_name,
        dimension=len(res['data'][0]['embedding']),
        metric='cosine'
    )
    # wait for index to be initialized
    while not pinecone.describe_index(index_name).status['ready']:
        time.sleep(1)

# connect to index
index = pinecone.Index(index_name)
```

With that, our knowledge base is ready to go, and we can move on to implementing RAG with guardrails.

### RAG with Guardrails

We first need to set up the functions triggered when our guardrails identify that the user is asking a question about LLMs. For that, we will use a `retrieve` function that performs the retrieval component of RAG — and a `rag` function that wraps all of this and the rest of the RAG pipeline logic together.

```
async def retrieve(query: str) -> list:
    # create query embedding
    res = openai.Embedding.create(input=[query], engine=embed_model_id)
    xq = res['data'][0]['embedding']
    # get relevant contexts from pinecone
    res = index.query(xq, top_k=5, include_metadata=True)
    # get list of retrieved texts
    contexts = [x['metadata']['chunk'] for x in res['matches']]
    return contexts

async def rag(query: str, contexts: list) -> str:
    print("> RAG Called")  # we'll add this so we can see when this is being used
    context_str = "\n".join(contexts)
    # place query and contexts into RAG prompt
    prompt = f"""You are a helpful assistant, below is a query from a user and
    some relevant contexts. Answer the question given the information in those
    contexts. If you cannot find the answer to the question, say "I don't know".

    Contexts:
    {context_str}

    Query: {query}

    Answer: """
    # generate answer
    res = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.0,
        max_tokens=100
    )
    return res['choices'][0]['text']
```

Note that both functions are `async` functions — we need this for them to integrate with the guardrails `generate_async` function later. Next up, we need to initialize our guardrails config files. We use these to define the guardrails, actions, etc. You can read more about these in our [introduction to NeMo Guardrails](https://www.pinecone.io/learn/nemo-guardrails-intro/).

```
yaml_content = """
models:
- type: main
  engine: openai
  model: text-davinci-003
"""

rag_colang_content = """
# define limits
define user ask politics
    "what are your political beliefs?"
    "thoughts on the president?"
    "left wing"
    "right wing"

define bot answer politics
    "I'm a personal assistant, I don't like to talk of politics."

define flow politics
    user ask politics
    bot answer politics
    bot offer help

# define RAG intents and flow
define user ask llms
    "tell me about llama 2?"
    "what is large language model"
    "where did meta's new model come from?"
    "what is the falcon model?"
    "have you ever meta llama?"

define flow llms
    user ask llms
    $contexts = execute retrieve(query=$last_user_message)
    $answer = execute rag(query=$last_user_message, contexts=$contexts)
    bot $answer
"""
```

Here, we have defined two possible dialogue flows. The first is typical of guardrails. It is a safety measure for our chatbot to avoid the topic of politics. The second is our RAG-enabled flow — triggered when a user asks about LLMs.

The LLM flow — defined by the `user ask llms` canonical form — executes the `retrieve` action using the `$last_user_message` to get our `$contexts`. We then pass the `$last_user_message` and `$contexts` to our `rag` action. To initialize our RAG-enabled rails, we do the following:

```
from nemoguardrails import LLMRails, RailsConfig

# initialize rails config
config = RailsConfig.from_content(
    colang_content=rag_colang_content,
    yaml_content=yaml_content
)
# create rails
rag_rails = LLMRails(config)
```

Every time we define actions in the Colang config file, we _must_ register them — otherwise, our rails have no idea how to `execute retrieve` or `execute rag`. We register both like so:

```
rag_rails.register_action(action=retrieve, name="retrieve")
rag_rails.register_action(action=rag, name="rag")
```

Now let's try it out:

We can see from the printed statement of `> RAG Called` that the second prompt triggered the RAG pipeline. So, our RAG with guardrails pipeline is working!

### RAG vs. No RAG

Everything looks good. However, it'd be interesting to see what the effect of RAG has on our answer. Let's initialize a new Rails instance that doesn't include the call to RAG to compare the results.

```
no_rag_colang_content = """
# define limits
define user ask politics
    "what are your political beliefs?"
    "thoughts on the president?"
    "left wing"
    "right wing"

define bot answer politics
    "I'm a shopping assistant, I don't like to talk of politics."
    "Sorry I can't talk about politics!"

define flow politics
    user ask politics
    bot answer politics
    bot offer help
"""

# initialize rails config
config = RailsConfig.from_content(
    colang_content=no_rag_colang_content,
    yaml_content=yaml_content
)
# create rails
no_rag_rails = LLMRails(config)
```

Let's ask about Llama 2 again:

That's not the Llama 2 we were looking for — let's try some more questions and compare RAG vs. no-RAG answers.

Our no RAG rails provide an exciting but utterly wrong answer. Let's try the same with our RAG-enabled rails:

A perfect answer! Our RAG-enabled rail is far more capable of answering questions while only calling the RAG action when required, as set in our `actions.co` config file.

* * *

By using Guardrails for RAG in this way, we manage to create a balance between the lightweight but naive approach of implementing [RAG with _every_ user call](https://www.pinecone.io/learn/series/langchain/langchain-retrieval-augmentation/) vs. the heavyweight and slow method of implementing a [conversational agent with RAG tool access](https://www.pinecone.io/learn/series/langchain/langchain-agents/).

* * *

References
----------

\[1\] W. Knight, [OpenAI's CEO Says the Age of Giant AI Models Is Already Over](https://www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/) (2023), Wired

\[2\] S. Yao, [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (2023), ICLR

## Metadata

```json
{
  "title": "Making Retrieval Augmented Generation Fast | Pinecone",
  "description": "Retrieval Augmented Generation (RAG) is the go-to method for adding external knowledge to Large Language Models (LLMs). RAG with agents can be slow, but we can make it much faster using NVIDIA NeMo Guardrails. We explain how here.",
  "url": "https://www.pinecone.io/learn/fast-retrieval-augmented-generation/",
  "content": "**L**arge **L**anguage **M**odels (LLMs) are incredible tools, but they're useless as soon as we require up-to-date or cited information. The reason for this is the learning strategy for all _\"parametric knowledge\"_ of LLMs.\n\nParametric knowledge refers to the information an LLM learns during its training phase. During training, the LLM learns to encode information from the training dataset into its internal model parameters — the model's parametric knowledge.\n\nTo add new parametric knowledge, we must fine-tune an LLM. Training, whether pretraining (which costs a reported $100M for GPT-4 \\[1\\]) or fine-tuning, is expensive and slow. Expensive and slow are not qualities we want when needing to keep our LLM knowledge up to date.\n\n[**R**etrieval **A**ugmented **G**eneration (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation//) has become the people's method for solving this problem. Rather than baking knowledge into the LLM via fine-tuning, we insert an external \"knowledge base\" into the LLM. When done well, this knowledge base is scalable, we can manage it as we would a traditional DB, and it can be significantly more reliable than fine-tuning.\n\nVideo walkthrough for super fast Retrieval Augmented Generation (RAG).\n\n* * *\n\nApproaches to RAG\n-----------------\n\n**R**etrieval **A**ugmented **G**eneration (RAG) allows us to update the knowledge of LLMs via the model's _\"source knowledge\"_. The source knowledge refers to any information fed into the LLM via the input prompt.\n\n![Image 10: The most common approach to RAG.](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fcaa233388a98715de2036dbf2bf2743e6e049b36-2283x1145.png&w=3840&q=75)\n\nThe most common approach to RAG.\n\nUsing RAG and source knowledge, we retrieve relevant information from an external data source, augment our prompt with this additional source knowledge, and feed that information into the LLM. This approach is compelling because it allows us to keep LLM knowledge accurate and up to date with minimal cost.\n\nThe above describes what I refer to as \"naive RAG\". Naive RAG is the most common implementation. It is simple, efficient, and effective.\n\nHowever, there are other ways of doing RAG. The other popular approach is to use [_agents_](https://www.pinecone.io/learn/series/langchain/langchain-agents/) that have access to RAG tools.\n\nAt its core, an agent is an LLM with added logic that allows it to reason over multiple generation steps, decide to use various tools, and specify _how_ to use those tools.\n\n![Image 11: Example reasoning and action logic from an agent framework called ReAct [2].](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F4defbaed3e9f223a658a87b9b625da131048c84d-2240x2024.png&w=3840&q=75)\n\nExample reasoning and action logic from an agent framework called ReAct \\[2\\].\n\nThis methodology allows the agent to answer far more complex queries. Rather than needing to produce an answer in a single step, it can now formulate and execute a plan to construct the best possible answer.\n\nRAG is one of the most common tools to give agents access to external knowledge. The advantage of this approach over the naive RAG approach primarily stems from the more advanced reasoning ability of the agent. It can decide _when_ to use RAG and how to use it. An agent can formulate a better search query based on the user's question, its parametric knowledge, and conversational history — it can also decide on additional parameters like how many results to return or whether to use [metadata filtering](https://www.pinecone.io/learn/vector-search-filtering/).\n\nThe problem with agent-powered RAG is speed and cost. Every reasoning step taken by an agent is a call to an LLM — LLMs are slow and expensive — so we will be waiting longer for a response and paying more money.\n\nThese two approaches to RAG are the most common. We have naive RAG and agent RAG. However, a _third option_ provides us with a middle ground between the two, a _best of both_. I like to call that option _RAG with Guardrails_.\n\nRAG with Guardrails\n-------------------\n\nRather than using a slow and expensive LLM call to decide which action to take, we can use _guardrails_. Guardrails can be described as _classifiers of user intent_. We can create a guardrail to identify queries that indicate someone is asking a question — when a user asks a question, the guardrails identify this intent and trigger the RAG pipeline.\n\n![Image 12: Defining canonical forms (categories of user intent) with example utterances. The utterances are encoded into vector space, giving us a type of classifier function.](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Ff4c238be0ec0baa83e51ff227d26e8f3df1b7c8b-2895x1710.png&w=3840&q=75)\n\nDefining canonical forms (categories of user intent) with example utterances. The utterances are encoded into vector space, giving us a type of classifier function.\n\nThe categories of user intent are called _\"canonical forms\"_. We define a canonical form by providing example queries (utterances) that we believe belong to that canonical form.\n\nIf we had a RAG pipeline that contained information about LLMs, we could define a canonical form that identifies when a user asks about LLMs. In the image above, we define this canonical form with `\"define user ask llm\"`. We then provide a few example queries that should trigger this form:\n\n```\n\"what is the llama 2 model?\"\n\"tell me about Meta's new LLM\"\n\"what are the differences between Falcon and Llama?\"\n```\n\nEach utterance is encoded into a semantic vector space, creating a semantic _\"map\"_. That map helps us line up semantic meaning and canonical forms.\n\n![Image 13: User queries are encoded into the same vector space, allowing us to identify if they have a semantic similarity to an existing cano](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Ff8c83210f38b76eb84a589f8231ce69d8565c112-2293x1534.png&w=3840&q=75)\n\nUser queries are encoded into the same vector space, allowing us to identify if they have a semantic similarity to an existing cano\n\nWhen a new user query comes in, we encode it into the same semantic vector space as our previous utterance examples. Using that map of utterances and the canonical forms they belong to, we can identify when a user query is semantically similar to those utterance examples. If the query is similar, we trigger the canonical form that those utterances belong to.\n\nWith that, we have a decision-making process in milliseconds rather than several seconds — as with agents.\n\nUsing RAG with guardrails does have nuances that we should consider. First, we must define the canonical forms. We could view the requirement of defining canonical forms in two ways: (1) we can be more deterministic about what should trigger a particular action, or (2) we lose out on the innate decision-making ability of an LLM.\n\nRAG with guardrails allows us to insert a user query directly into an action — but it cannot rephrase the query, specify metadata filters, or decide how many results to return. On the other hand, using an agent makes those tasks easy. However, if we can infer these parameters deterministically with code, we can include them without using an LLM.\n\nThat gives us an idea of how RAG with guardrails works and its pros and cons. Let's jump into the implementation itself.\n\nImplementing RAG with Guardrails\n--------------------------------\n\nTo implement RAG with guardrails, we will rely on the [NVIDIA NeMo Guardrails library](https://www.pinecone.io/learn/nemo-guardrails-intro/). The library primarily focuses on AI safety by implementing \"guardrails\" as protective measures against unwanted interactions. However, we can also use these guardrails to trigger things like RAG.\n\n```\n!pip install -qU \\\n    nemoguardrails==0.4.0 \\\n    pinecone-client==2.2.2 \\\n    datasets==2.14.3 \\\n    openai==0.27.8\n```\n\n### Building the Knowledge Base\n\nAs with every RAG use case, we must first create our knowledge base. For that, we will use a small dataset of Llama 2 related ArXiv papers stored in Hugging Face — we download the dataset like so:\n\nThe data has already been preprocessed for this use case, so we don't need to worry about chunking — however, we need to reformat the data to keep only what we need for our knowledge base.\n\nThe `chunk` field contains the text we will encode and store inside Pinecone. To encode that data, we need to use an embedding model. We will use OpenAI's `text-embedding-ada-002` here, so we must authenticate ourselves with an [OpenAI API key](https://platform.openai.com/account/api-keys).\n\n```\nimport os\n\n# set your api key here\nos.environ[\"OPENAI_API_KEY\"] = \"YOUR_API_KEY\"\n```\n\nThen we create embeddings via the `openai.Embedding.create` endpoint like so:\n\nAs we fed two chunks of text into the embedding function, we received two embeddings (one for each chunk). Note that each is 1536-dimensional. We need this number when setting up our Pinecone index in a moment.\n\n### Creating the Vector Index\n\nNow, we need a place to store these embeddings and enable an efficient vector search through them all. To do that, we use Pinecone. We can get a [free API key](https://app.pinecone.io/) and enter it below, where we will initialize our connection to Pinecone.\n\n```\nimport pinecone\n\n# initialize connection to pinecone (get API key at app.pinecone.io)\napi_key = \"YOUR_API_KEY\"\n# find your environment next to the api key in pinecone console\nenv = \"YOUR_ENV\"\n\npinecone.init(api_key=api_key, environment=env)\n```\n\nNow, we create the vector index:\n\n```\nimport time\n\nindex_name = \"nemo-guardrails-rag-with-actions\"\n\n# check if index already exists (it shouldn't if this is first time)\nif index_name not in pinecone.list_indexes():\n    # if does not exist, create index\n    pinecone.create_index(\n        index_name,\n        dimension=len(res['data'][0]['embedding']),\n        metric='cosine'\n    )\n    # wait for index to be initialized\n    while not pinecone.describe_index(index_name).status['ready']:\n        time.sleep(1)\n\n# connect to index\nindex = pinecone.Index(index_name)\n```\n\nWith that, our knowledge base is ready to go, and we can move on to implementing RAG with guardrails.\n\n### RAG with Guardrails\n\nWe first need to set up the functions triggered when our guardrails identify that the user is asking a question about LLMs. For that, we will use a `retrieve` function that performs the retrieval component of RAG — and a `rag` function that wraps all of this and the rest of the RAG pipeline logic together.\n\n```\nasync def retrieve(query: str) -> list:\n    # create query embedding\n    res = openai.Embedding.create(input=[query], engine=embed_model_id)\n    xq = res['data'][0]['embedding']\n    # get relevant contexts from pinecone\n    res = index.query(xq, top_k=5, include_metadata=True)\n    # get list of retrieved texts\n    contexts = [x['metadata']['chunk'] for x in res['matches']]\n    return contexts\n\nasync def rag(query: str, contexts: list) -> str:\n    print(\"> RAG Called\")  # we'll add this so we can see when this is being used\n    context_str = \"\\n\".join(contexts)\n    # place query and contexts into RAG prompt\n    prompt = f\"\"\"You are a helpful assistant, below is a query from a user and\n    some relevant contexts. Answer the question given the information in those\n    contexts. If you cannot find the answer to the question, say \"I don't know\".\n\n    Contexts:\n    {context_str}\n\n    Query: {query}\n\n    Answer: \"\"\"\n    # generate answer\n    res = openai.Completion.create(\n        engine=\"text-davinci-003\",\n        prompt=prompt,\n        temperature=0.0,\n        max_tokens=100\n    )\n    return res['choices'][0]['text']\n```\n\nNote that both functions are `async` functions — we need this for them to integrate with the guardrails `generate_async` function later. Next up, we need to initialize our guardrails config files. We use these to define the guardrails, actions, etc. You can read more about these in our [introduction to NeMo Guardrails](https://www.pinecone.io/learn/nemo-guardrails-intro/).\n\n```\nyaml_content = \"\"\"\nmodels:\n- type: main\n  engine: openai\n  model: text-davinci-003\n\"\"\"\n\nrag_colang_content = \"\"\"\n# define limits\ndefine user ask politics\n    \"what are your political beliefs?\"\n    \"thoughts on the president?\"\n    \"left wing\"\n    \"right wing\"\n\ndefine bot answer politics\n    \"I'm a personal assistant, I don't like to talk of politics.\"\n\ndefine flow politics\n    user ask politics\n    bot answer politics\n    bot offer help\n\n# define RAG intents and flow\ndefine user ask llms\n    \"tell me about llama 2?\"\n    \"what is large language model\"\n    \"where did meta's new model come from?\"\n    \"what is the falcon model?\"\n    \"have you ever meta llama?\"\n\ndefine flow llms\n    user ask llms\n    $contexts = execute retrieve(query=$last_user_message)\n    $answer = execute rag(query=$last_user_message, contexts=$contexts)\n    bot $answer\n\"\"\"\n```\n\nHere, we have defined two possible dialogue flows. The first is typical of guardrails. It is a safety measure for our chatbot to avoid the topic of politics. The second is our RAG-enabled flow — triggered when a user asks about LLMs.\n\nThe LLM flow — defined by the `user ask llms` canonical form — executes the `retrieve` action using the `$last_user_message` to get our `$contexts`. We then pass the `$last_user_message` and `$contexts` to our `rag` action. To initialize our RAG-enabled rails, we do the following:\n\n```\nfrom nemoguardrails import LLMRails, RailsConfig\n\n# initialize rails config\nconfig = RailsConfig.from_content(\n    colang_content=rag_colang_content,\n    yaml_content=yaml_content\n)\n# create rails\nrag_rails = LLMRails(config)\n```\n\nEvery time we define actions in the Colang config file, we _must_ register them — otherwise, our rails have no idea how to `execute retrieve` or `execute rag`. We register both like so:\n\n```\nrag_rails.register_action(action=retrieve, name=\"retrieve\")\nrag_rails.register_action(action=rag, name=\"rag\")\n```\n\nNow let's try it out:\n\nWe can see from the printed statement of `> RAG Called` that the second prompt triggered the RAG pipeline. So, our RAG with guardrails pipeline is working!\n\n### RAG vs. No RAG\n\nEverything looks good. However, it'd be interesting to see what the effect of RAG has on our answer. Let's initialize a new Rails instance that doesn't include the call to RAG to compare the results.\n\n```\nno_rag_colang_content = \"\"\"\n# define limits\ndefine user ask politics\n    \"what are your political beliefs?\"\n    \"thoughts on the president?\"\n    \"left wing\"\n    \"right wing\"\n\ndefine bot answer politics\n    \"I'm a shopping assistant, I don't like to talk of politics.\"\n    \"Sorry I can't talk about politics!\"\n\ndefine flow politics\n    user ask politics\n    bot answer politics\n    bot offer help\n\"\"\"\n\n# initialize rails config\nconfig = RailsConfig.from_content(\n    colang_content=no_rag_colang_content,\n    yaml_content=yaml_content\n)\n# create rails\nno_rag_rails = LLMRails(config)\n```\n\nLet's ask about Llama 2 again:\n\nThat's not the Llama 2 we were looking for — let's try some more questions and compare RAG vs. no-RAG answers.\n\nOur no RAG rails provide an exciting but utterly wrong answer. Let's try the same with our RAG-enabled rails:\n\nA perfect answer! Our RAG-enabled rail is far more capable of answering questions while only calling the RAG action when required, as set in our `actions.co` config file.\n\n* * *\n\nBy using Guardrails for RAG in this way, we manage to create a balance between the lightweight but naive approach of implementing [RAG with _every_ user call](https://www.pinecone.io/learn/series/langchain/langchain-retrieval-augmentation/) vs. the heavyweight and slow method of implementing a [conversational agent with RAG tool access](https://www.pinecone.io/learn/series/langchain/langchain-agents/).\n\n* * *\n\nReferences\n----------\n\n\\[1\\] W. Knight, [OpenAI's CEO Says the Age of Giant AI Models Is Already Over](https://www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/) (2023), Wired\n\n\\[2\\] S. Yao, [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (2023), ICLR",
  "usage": {
    "tokens": 3998
  }
}
```
