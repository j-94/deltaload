---
title: The Abridged Guide to Neo4j Cypher Generation with OpenAI GPT-4
description: Learn how to build a chatbot that connects to Neo4j with minimal code and minimal Cypher.
url: https://adamcowley.co.uk/posts/abridged-neo4j-cypher-generation/
timestamp: 2025-01-20T15:45:22.652Z
domain: adamcowley.co.uk
path: posts_abridged-neo4j-cypher-generation
---

# The Abridged Guide to Neo4j Cypher Generation with OpenAI GPT-4


Learn how to build a chatbot that connects to Neo4j with minimal code and minimal Cypher.


## Content

In this post, I will provide the abridged version of the [Neo4j & LLM Fundamentals course on GraphAcademy](https://graphacademy.neo4j.com/courses/llm-fundamentals/?ref=adam).

The objective is to build a [Langchain Agent](https://python.langchain.com/docs/modules/agents/) that is capable of providing movie recommendations based on the information from the Recommendations dataset in Neo4j Sandbox. But, I want to do this by writing as little code as possible. I will demonstrate how to build a conversational agent that is capable of querying a Neo4j database using existing tools, and with as little code as possible. I will also address some of the challenges you may face along the way if you are trying to do something similar.

**TL;DR:** You can use the `GraphCypherQAChain` in Langchain to generate Cypher and execute it against the database. But it may take some fine tuning and some example Cypher queries to work.

Introducing Ebert
-----------------

Meet Ebert, the movie recommendation bot.

I have chosen to call it Ebert in honor of the late legendary film critic, [Robert Ebert](https://en.wikipedia.org/wiki/Roger_Ebert). [Collider](https://collider.com/best-movie-critics-all-time-ranked/#:~:text=When%20it%20comes%20to%20movie,virtually%20every%20critic%20who's%20followed.) ranked Robert as the most influential movie critic of all time. Here is what they had to say:

> When it comes to movie critics, the one name that is recognizable above all else is the truly unforgettable and inspirational Roger Ebert. His career lasted nearly a half-century, and his impact has lasted long after his death in 2013. He paved the way for virtually every critic who’s followed.

_Ebert_ is built using Langchain, a framework for building applications that interact with large language models.

Why Langchain?
--------------

Langchain is becoming ubiquitous with Generative AI and LLMs. It is quickly growing in popularity due to its ease of use and extendable nature. If you want to know more, you can check the course or search YouTube for details.

I personally chose langchain because, despite its relative age, it is feature rich, already contains integrations with many useful platforms, and that functionality is growing with weekly releases. They also have an active community and a helpful Discord channel.

Langchain also supports multiple Large Language Models, and allows you to swap one for another with relative ease. This way I’m not wedded to OpenAI if I want to change in future.5

Getting Started
---------------

First, I’m going to load my config from `.env`. This contains an OpenAI API Key, which I obtained from [platform.openai.com](https://adamcowley.co.uk/posts/abridged-neo4j-cypher-generation/platform.openai.com), and my Neo4j Sandbox credentials that I obtained from [sandbox.neo4j.com](https://adamcowley.co.uk/posts/abridged-neo4j-cypher-generation/sandbox.neo4j.com).

```
OPENAI_API_KEY=sk-***
NEO4J_URI=bolt://***:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=three-word-password
```

These can be loaded with the [`python-dotenv` library from PyPI](https://pypi.org/project/python-dotenv/) _(not to be confused with plain old `dotenv` lib)_

```
pip install python-dotenv
```

```
from dotenv import load_dotenv
load_dotenv()  # loads .env, or you can specify the filename as a positional argument.
```

The variables can then be loaded from `os.environ` using `os.getenv`.

```
import os
print(os.getenv('OPENAI_API_KEY')[:5] + "...")
```

```
sk-oy
```

For this project I will also need to install dependencies for Langchain, OpenAI and Neo4j.

```
pip install langchain openai neo4j
```

Initialising the LLM
--------------------

The aim here is to create a conversational interface, so I have chosen an LLM model from `langchain.chat_models`. These differ from the language models available under `langchain.llms` in that they are tuned for conversations. While the `llms` accept a single string and return a single result, the chat models accept a list of chat messages as an input. Chat models also support message history, which will be useful later on.

```

from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key=os.getenv('OPENAI_API_KEY'),  #1
    temperature=0.5,  #2
    model="gpt-4" #1
)

```

In the code above:

1.  The `ChatOpenAI` instance is created with the `OPENAI_API_KEY` value held in environment variables.
2.  The `temperature` is set to 0.5. This value can range between 0.0 and 1.0, the higher the value is the more randomness is added to the response generation.
3.  I’m using `gpt-4` here because I have found it generates Cypher much more accurately than `gpt-3.5-turbo`. You can experiement with the models, which all have their own drawbacks and price implications.

Creating a Prompt Template
--------------------------

The LLM may need special instructions on how to act. In this case, the LLM should respond to the user input as if it is a movie expert.

Wrapping these instructions in a prompt template mean that the inputs required for the LLM to act are clearly defined up front, and the input will be validated by the LLM chain.

```
from langchain.prompts.prompt import PromptTemplate

BASIC_PROMPT = PromptTemplate(template="""
You are a movie expert providing customers with movie recommendations.
Answer the following question to the best of your ability.

Question: {question}
Answer:
""", input_variables=["question"])
```

This prompt will expect one input, `question`.

The easiest way to get an LLM to act on this prompt is using an `LLMChain`. The `LLMChain` expects `llm` and `prompt` parameters.

```
from langchain.chains.llm import LLMChain

qa_chain = LLMChain(llm=llm, prompt=BASIC_PROMPT)
```

Now `qa_chain` can be called with a `dict` containing the input variables that should be injected into the prompt. In this case, `question`.

Let’s see how it does when asked who directed The Matrix.

```
qa_chain({"question": "Who directed the Matrix?"})
```

```
{'question': 'Who directed the Matrix?',
 'text': 'The Matrix was directed by the Wachowski siblings, Lana and Lilly.'}
```

This looks good. The Matrix is pretty old, so it is likely all of this information is in the training dataset. How will it cope with data that isn’t included in the training data set?

How about a fictional movie called _Neo4j, the Movie_?

```
qa_chain({"question": "Who directed Neo4j, the Movie?"})
```

```
{'question': 'Who directed Neo4j, the Movie?',
 'text': 'As of now, there\'s no known movie titled "Neo4j". Neo4j is actually a graph database management system developed by Neo4j, Inc.'}
```

What will it say if we ask what movies Emil Eifrem has acted in?

For anyone that has taken [Cypher Fundamentals](https://graphacademy.neo4j.com/courses/cypher-fundamentals/), we all know that Emil Eifrem acted in The Matrix.

```
MATCH (:Person {name: "Emil Eifrem"})-[r:ACTED_IN]->(m:Movie)
RETURN m.title AS movie, r.roles AS roles
```

How does the LLM handle this question?

```
qa_chain({"question": "What movies has Emil Eifrem acted in?"})
```

```
{'question': 'What movies has Emil Eifrem acted in?',
 'text': 'Emil Eifrem does not have any acting credits. He is known as a software entrepreneur and the CEO of Neo4j, not as an actor.'}
```

This highlights a potential problem with LLMs.

*   **Bad Data** - The training data itself may be false, or the LLM may not have the ability to verify the source of the data.
*   **Cut-off Date** - LLMs are computationally expensive to train, and this training takes a long time. Furthermore, the model itself will not have access to the latest data.
*   **Lack of data/enterprise domain knowledge** - When it comes to private data, the LLM will not be aware of private data.

This is where a technique known as RAG, or _Retrieval Augmented Generation_ comes in.

Retrieval Augmented Generation
------------------------------

If you take the RAG acronym backwards, it describes a technique in which an LLM will **generate** a piece of content, which is **augmented** by the retrieval of data from another source. In other words, content from additional data sources can be used to improve the content generated by an LLM.

Let’s pretend for a second that _Neo4j The Movie_ did exist, a future release charting Neo4j’s rise from an idea on a napkin to a company valued at more than $2B.

We can provide this information to the LLM as part of the prompt to help it generate the answer to the question.

This context becomes another input variable to the prompt template.

```
CONTEXT_PROMPT = PromptTemplate(template="""
You are a movie expert providing customers with movie recommendations.
Answer the following question using the following context.
If the answer is not included in the context, fall back to your trained knowledge.

Context: {context}
Question: {question}
""", input_variables=["context", "question"])

qa_chain_with_context = LLMChain(llm=llm, prompt=CONTEXT_PROMPT)
```

Now, by calling the `qa_chain_with_context` chain and providing the movie information as the context in the prompt, the LLM will answer the question.

```
qa_chain_with_context({
    "context":  """
    {
        "title": "Neo4j, The Movie",
        "plot": "In a parallel realm of binary rain and neon grids, a concept springs to life on a mere napkin—Neo4j, a revolutionary graph database destined to reshape the perception of data interconnectivity. It is the brainchild of a group of plucky visionaries who band together to traverse the treacherous labyrinth of the startup world.",
        "directors: ["Emil Eifrem"],
        "actors": [
            {"name": "Michael Hunger", "role": "mesirii"},
            {"name": "Andreas Kolleger", "role": "Plucky Number 8"},
            {"name": "Adam Cowley", "role": "Developer Advocate #3 (Extra)"}
        ]
    }
    """,
    "question": "Who directed Neo4j, the Movie?"
})
```

```
{'context': '\n    {\n        "title": "Neo4j, The Movie", \n        "plot": "In a parallel realm of binary rain and neon grids, a concept springs to life on a mere napkin—Neo4j, a revolutionary graph database destined to reshape the perception of data interconnectivity. It is the brainchild of a group of plucky visionaries who band together to traverse the treacherous labyrinth of the startup world.",\n        "directors: ["Emil Eifrem"],\n        "actors": [\n            {"name": "Michael Hunger", "role": "mesirii"},\n            {"name": "Andreas Kolleger", "role": "Plucky Number 8"},\n            {"name": "Adam Cowley", "role": "Developer Advocate #3 (Extra)"}\n        ]\n    }\n    ',
 'question': 'Who directed Neo4j, the Movie?',
 'text': 'The movie "Neo4j, The Movie" was directed by Emil Eifrem.'}
```

One step closer. Now, we’ll need to automate the _retrieval_ of this information from the database. As I mentioned above, I want to avoid writing any Cypher unless absolutely necessary. Luckily, this is already available in Langchain.

Automatic Cypher Query Generation
---------------------------------

To interact with Neo4j through Langchain, the first step is to create a Neo4j connection through the `Neo4jGraph` class.

```
from langchain.graphs import Neo4jGraph

graph = Neo4jGraph(
    url = os.getenv('NEO4J_URI'),
    username = os.getenv('NEO4J_USERNAME'),
    password = os.getenv('NEO4J_PASSWORD')
)
```

When the `Neo4jGraph` class is instantiated, it automatically loads schema information into memory. This can be refreshed at any time by calling `graph.refresh_schema()`.

Here is the generated schema for the recommendations dataset:

```
print(graph.schema)
```

```
        Node properties are the following:
        [{'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'runtime', 'type': 'INTEGER'}, {'property': 'revenue', 'type': 'INTEGER'}, {'property': 'budget', 'type': 'INTEGER'}, {'property': 'imdbRating', 'type': 'FLOAT'}, {'property': 'released', 'type': 'STRING'}, {'property': 'countries', 'type': 'LIST'}, {'property': 'languages', 'type': 'LIST'}, {'property': 'plot', 'type': 'STRING'}, {'property': 'imdbVotes', 'type': 'INTEGER'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'year', 'type': 'INTEGER'}, {'property': 'poster', 'type': 'STRING'}, {'property': 'movieId', 'type': 'STRING'}, {'property': 'tmdbId', 'type': 'STRING'}, {'property': 'title', 'type': 'STRING'}], 'labels': 'Movie'}, {'properties': [{'property': 'name', 'type': 'STRING'}], 'labels': 'Genre'}, {'properties': [{'property': 'userId', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}], 'labels': 'User'}, {'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}, {'property': 'tmdbId', 'type': 'STRING'}, {'property': 'bornIn', 'type': 'STRING'}, {'property': 'bio', 'type': 'STRING'}, {'property': 'died', 'type': 'DATE'}, {'property': 'born', 'type': 'DATE'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'poster', 'type': 'STRING'}], 'labels': 'Actor'}, {'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'bornIn', 'type': 'STRING'}, {'property': 'born', 'type': 'DATE'}, {'property': 'died', 'type': 'DATE'}, {'property': 'tmdbId', 'type': 'STRING'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}, {'property': 'poster', 'type': 'STRING'}, {'property': 'bio', 'type': 'STRING'}], 'labels': 'Director'}, {'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'bornIn', 'type': 'STRING'}, {'property': 'bio', 'type': 'STRING'}, {'property': 'died', 'type': 'DATE'}, {'property': 'born', 'type': 'DATE'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}, {'property': 'poster', 'type': 'STRING'}, {'property': 'tmdbId', 'type': 'STRING'}], 'labels': 'Person'}]
        Relationship properties are the following:
        [{'type': 'RATED', 'properties': [{'property': 'rating', 'type': 'FLOAT'}, {'property': 'timestamp', 'type': 'INTEGER'}]}, {'type': 'ACTED_IN', 'properties': [{'property': 'role', 'type': 'STRING'}]}, {'type': 'DIRECTED', 'properties': [{'property': 'role', 'type': 'STRING'}]}]
        The relationships are the following:
        ['(:Movie)-[:IN_GENRE]->(:Genre)', '(:User)-[:RATED]->(:Movie)', '(:Actor)-[:ACTED_IN]->(:Movie)', '(:Actor)-[:DIRECTED]->(:Movie)', '(:Director)-[:DIRECTED]->(:Movie)', '(:Director)-[:ACTED_IN]->(:Movie)', '(:Person)-[:DIRECTED]->(:Movie)', '(:Person)-[:ACTED_IN]->(:Movie)']
```

Cypher can be generated through the `GraphCypherQAChain` class. This class uses an LLM to generate a Cypher query based on the schema above that will attempt to answer the question.

You can pass a prompt to the chain to provide specific instructions for constructing the Cypher statement.

```

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.

Schema: {schema}
Question: {question}
"""

CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], validate_template=True, template=CYPHER_GENERATION_TEMPLATE
)
```

The class has a static `from_llm` method for instantiating the class with kwargs for the LLM and Graph.

The class allows you to pass different LLM objects for generating Cypher and answering the query (`cypher_llm` and `qa_llm`), which allow you to experiment with different models until you find the right models for the best result for Cypher generation.

For berevity, I have used the `llm` kwarg to use the same LLM for both Cypher generation and formatting a response.

```
from langchain.chains import GraphCypherQAChain

cypher_chain = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    cypher_prompt=CYPHER_GENERATION_PROMPT,
    verbose=True  # To see what is happening inside the chain
)

cypher_chain.run("Who acted in The Matrix and what roles did they play?")
```

```
> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (m:Movie {title: 'The Matrix'})<-[:ACTED_IN]-(a:Actor)
RETURN a.name as Actor, a.role as Role
Full Context:
[]

> Finished chain.





"I'm sorry, but I don't have the information to answer that question."
```

The query looks fine, but you can see from the output of the chain that `Full Context` is empty. In this case, the LLM has fallen back on its prior knowledge.

A closer look at the dataset reveals that movies which start with `The` are renamed as `{title}, The`. This is where the `cypher_prompt` input can be used to fine-tune the prompt.

For inspiration, let’s take a look at the original `CYPHER_GENERATION_PROMPT` used if no specific prompt is provided.

```
from langchain.chains.graph_qa.prompts import CYPHER_GENERATION_PROMPT as ORIGINAL_CYPHER_GENERATION_PROMPT

print(ORIGINAL_CYPHER_GENERATION_PROMPT.template)
```

```
Task:Generate Cypher statement to query a graph database.
Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Schema:
{schema}
Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

The question is:
{question}
```

To fix titles starting with `The`, the following line can be added to the prompt:

> For movie titles that begin with “The”, move “the” to the end, For example “The 39 Steps” becomes “39 Steps, The” or “The Matrix” becomes “Matrix, The”.

```
CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.
For movie titles that begin with "The", move "the" to the end, For example "The 39 Steps" becomes "39 Steps, The" or "The Matrix" becomes "Matrix, The".

If no context is returned, do not attempt to answer the question.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Schema:
{schema}
Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

Question: {question}
"""

CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["question", "schema"],
    validate_template=True,
    template=CYPHER_GENERATION_TEMPLATE
)

cypher_chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, verbose=True,
    cypher_prompt = CYPHER_GENERATION_PROMPT
)

cypher_chain.run("Who acted in The Matrix and what roles did they play?")
```

```
> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (a:Actor)-[r:ACTED_IN]->(m:Movie)
WHERE m.title = "Matrix, The"
RETURN a.name, r.role
Full Context:
[{'a.name': 'Hugo Weaving', 'r.role': 'Agent Smith'}, {'a.name': 'Laurence Fishburne', 'r.role': 'Morpheus'}, {'a.name': 'Keanu Reeves', 'r.role': 'Thomas A. Anderson / Neo'}, {'a.name': 'Carrie-Anne Moss', 'r.role': 'Trinity'}]

> Finished chain.





'Hugo Weaving played the role of Agent Smith, Laurence Fishburne portrayed Morpheus, Keanu Reeves was Thomas A. Anderson, also known as Neo, and Carrie-Anne Moss acted as Trinity in The Matrix.'
```

Perfect, the LLM has reformatted the title and now the full list of roles is passed to the LLM.

How does it handle an aggregation query?

```
cypher_chain.run("How many movies has Tom Hanks directed?")
```

```
> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (d:Director {name: 'Tom Hanks'})-[:DIRECTED]->(m:Movie)
RETURN COUNT(m)
Full Context:
[{'COUNT(m)': 2}]

> Finished chain.





'Tom Hanks has directed 2 movies.'
```

Conversational Bot
------------------

Now, let’s make it conversational. We can add define the `GraphCypherQAChain` as a tool within a [Langchain _agent_](https://docs.langchain.com/docs/components/agents/), complete with conversation history defined by the `memory` kwarg.

```
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import AgentType, initialize_agent

from langchain.tools import Tool

tools = [
    Tool.from_function(
        name="GraphCypherQAChain",
        description="Use Cypher to generate information above movies, actors, users and ratings",
        func=cypher_chain.run,
        return_direct=True
    )
]

memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

agent = initialize_agent(
    tools, llm, memory=memory, max_iterations=3,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True
)

```

Now we can have a conversation with the agent.

```
agent.run("How many films did Tom Hanks act in?")
```

````
> Entering new AgentExecutor chain...
```json
{
    "action": "GraphCypherQAChain",
    "action_input": "MATCH (a:Actor {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)"
}
```

> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (a:Actor {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)
Full Context:
[{'count(m)': 38}]

> Finished chain.

Observation: [36;1m[1;3mTom Hanks has acted in 38 movies.


> Finished chain.





'Tom Hanks has acted in 38 movies.'
````

Will the agent remember that we have asked a question about Tom Hanks?

```
agent.run("and how many has he directed?")
```

````
> Entering new AgentExecutor chain...
```json
{
    "action": "GraphCypherQAChain",
    "action_input": "MATCH (p:Person {name: 'Tom Hanks'})-[:DIRECTED]->(m:Movie) RETURN count(m)"
}
```

> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (p:Person {name: 'Tom Hanks'})-[:DIRECTED]->(m:Movie) RETURN count(m)
Full Context:
[{'count(m)': 2}]

> Finished chain.

Observation: [36;1m[1;3mTom Hanks has directed 2 movies.


> Finished chain.





'Tom Hanks has directed 2 movies.'
````

What type of films has he directed?

```
agent.run("What genres has he directed?")
```

````
> Entering new AgentExecutor chain...
```json
{
    "action": "GraphCypherQAChain",
    "action_input": "MATCH (p:Person)-[:DIRECTED]->(m:Movie) WHERE p.name = 'Tom Hanks' RETURN m.genres"
}
```

> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (p:Person)-[:DIRECTED]->(m:Movie) WHERE p.name = 'Tom Hanks' RETURN m.countries
Full Context:
[{'m.countries': ['USA']}, {'m.countries': ['USA']}]

> Finished chain.

Observation: [36;1m[1;3mI'm sorry, but the provided information does not contain any details about the genres of movies directed by Tom Hanks.


> Finished chain.





"I'm sorry, but the provided information does not contain any details about the genres of movies directed by Tom Hanks."
````

It looks like it can’t answer this question. It seems to think there is a `genre` property on the `(:Movie)` node which isn’t correct.

For cases like this, an example can be provided in the Cypher generation prompt. This is known as [Few-Shot Prompting](https://www.promptingguide.ai/techniques/fewshot). The main benefit of Few-Shot prompting is that it can be done on the fly.

```
FEWSHOT_CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.
For movie titles that begin with "The", move "the" to the end, For example "The 39 Steps" becomes "39 Steps, The" or "The Matrix" becomes "Matrix, The".

If no context is returned, do not attempt to answer the question.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Schema:
{schema}

Examples:

Find movies and their genres:
MATCH (m:Movie)-[:IN_GENRE]->(g)
WHERE m.title = "Goodfellas"
RETURN m.title AS title, collect(g.name) AS genres

Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

Question: {question}
"""

FEWSHOT_CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["question", "schema"],
    validate_template=True,
    template=FEWSHOT_CYPHER_GENERATION_TEMPLATE
)

fewshot_cypher_chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, verbose=True,
    cypher_prompt = FEWSHOT_CYPHER_GENERATION_PROMPT
)

fewshot_cypher_chain.run("What genre of film is Toy Story?")
```

```
> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (m:Movie)-[:IN_GENRE]->(g)
WHERE m.title = "Toy Story"
RETURN m.title AS title, collect(g.name) AS genres
Full Context:
[{'title': 'Toy Story', 'genres': ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy']}]

> Finished chain.





'Toy Story is an Adventure, Animation, Children, Comedy, and Fantasy film.'
```

That looks better. Can it answer which movies that Tom Hanks has directed now?

```
fewshot_cypher_chain.run("What genres of film has Tom Hanks directed?")
```

```
> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (p:Person {name: "Tom Hanks"})-[:DIRECTED]->(m:Movie)-[:IN_GENRE]->(g:Genre)
RETURN collect(distinct g.name) AS genres
Full Context:
[{'genres': ['Drama', 'Comedy', 'Romance']}]

> Finished chain.





'Tom Hanks has directed films in the genres of Drama, Comedy, and Romance.'
```

Success!

Will the LLM be able to cope with a complex recommendation query?

```
fewshot_cypher_chain.run("Can you recommend me a film similar to The Green Mile staring Tom Hanks?")
```

```
> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (m:Movie)<-[:ACTED_IN]-(a:Actor {name: "Tom Hanks"}), (m2:Movie)<-[:ACTED_IN]-(a)
WHERE m.title = "Green Mile, The"
RETURN m2.title AS similar_movies
Full Context:
[{'similar_movies': 'Punchline'}, {'similar_movies': 'Catch Me If You Can'}, {'similar_movies': 'Dragnet'}, {'similar_movies': 'Saving Mr. Banks'}, {'similar_movies': 'Bachelor Party'}, {'similar_movies': 'Volunteers'}, {'similar_movies': 'Man with One Red Shoe, The'}, {'similar_movies': 'Splash'}, {'similar_movies': 'Big'}, {'similar_movies': 'Nothing in Common'}]

> Finished chain.





"Sure, you might enjoy watching movies like 'Punchline', 'Catch Me If You Can', 'Dragnet', 'Saving Mr. Banks', 'Bachelor Party', 'Volunteers', 'The Man with One Red Shoe', 'Splash', 'Big', or 'Nothing in Common'. These films are similar to 'The Green Mile' and also feature Tom Hanks."
```

OK, it returns a result but the query only asks for other movies that Tom Hanks acted in. It looks like the LLM would benefit from another example.

The recommendation query should really find Tom Hanks movies, then use the graph to find the actors in those movies and the other movies they have acted in and use some sort of scoring metric to work out which films to recommend.

```
MATCH (:Person {name:"Al Pacino"})-[:ACTED_IN|DIRECTED]->(m)<-[:ACTED_IN|DIRECTED]-(p),
  (p)-[role:ACTED_IN|DIRECTED]->(m2)
RETURN
  m2.title AS recommendation,
  collect([ p.name, type(role) ]) AS peopleInCommon,
  [ (m)-[:IN_GENRE]->(g)<-[:IN_GENRE]-(m2) | g.name ] AS genresInCommon
ORDER BY size(incommon) DESC, size(genresInCommon) DESC LIMIT 2
```

For a given actor, the Cypher statement finds any people who have either acted in or directed a movie, finds any movie that they have either acted in or directed, and then returns a list ordered by the number of people in common, and the genres that they share.

```
FEWSHOT_CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.
For movie titles that begin with "The", move "the" to the end, For example "The 39 Steps" becomes "39 Steps, The" or "The Matrix" becomes "Matrix, The".

If no context is returned, do not attempt to answer the question.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Schema:
{schema}

Examples:

Find movies and their genres:
MATCH (m:Movie)-[:IN_GENRE]->(g)
WHERE m.title = "Goodfellas"
RETURN m.title AS title, collect(g.name) AS genres

Recommend a movie by actor:
MATCH (subject:Person)-[:ACTED_IN|DIRECTED]->(m)<-[:ACTED_IN|DIRECTED]-(p),
  (p)-[role:ACTED_IN|DIRECTED]->(m2)
WHERE subject.name = "Al Pacino"
RETURN
  m2.title AS recommendation,
  collect([ p.name, type(role) ]) AS peopleInCommon,
  [ (m)-[:IN_GENRE]->(g)<-[:IN_GENRE]-(m2) | g.name ] AS genresInCommon
ORDER BY size(incommon) DESC, size(genresInCommon) DESC LIMIT 2


Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

Question: {question}
"""

FEWSHOT_CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["question", "schema"],
    validate_template=True,
    template=FEWSHOT_CYPHER_GENERATION_TEMPLATE
)

fewshot_cypher_chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, verbose=True,
    cypher_prompt = FEWSHOT_CYPHER_GENERATION_PROMPT
)

fewshot_cypher_chain.run("Can you recommend me a film similar to The Green Mile staring Tom Hanks?")
```

```
> Entering new GraphCypherQAChain chain...
Generated Cypher:
MATCH (subject:Person)-[:ACTED_IN|DIRECTED]->(m:Movie)<-[:ACTED_IN|DIRECTED]-(p:Person),
  (p)-[role:ACTED_IN|DIRECTED]->(m2:Movie)
WHERE subject.name = "Tom Hanks" AND m.title = "Green Mile, The"
RETURN
  m2.title AS recommendation,
  collect([ p.name, type(role) ]) AS peopleInCommon,
  [ (m)-[:IN_GENRE]->(g:Genre)<-[:IN_GENRE]-(m2) | g.name ] AS genresInCommon
ORDER BY size(peopleInCommon) DESC, size(genresInCommon) DESC LIMIT 1
Full Context:
[{'recommendation': 'Negotiator, The', 'peopleInCommon': [['David Morse', 'ACTED_IN']], 'genresInCommon': ['Drama', 'Crime']}]

> Finished chain.





'Sure, based on your preferences, I would recommend "The Negotiator". It\'s a Drama and Crime film like The Green Mile and also features David Morse, who acted in The Green Mile as well.'
```

Without asking the exact same question, the LLM was able to take the example and modify it to answer the question.

I’m pretty pleased with that result!

Conclusion
----------

This approach goes beyond a more _simple_ vector index lookup, where chunks of text are compared to a user input by the distance between their vector representations.

I have personally found through building [the GraphAcademy Chatbot](https://medium.com/neo4j/building-an-educational-chatbot-for-graphacademy-with-neo4j-f707c4ce311b) that this approach can produce some wildly inaccurate results, or similar documents in terms of cosine distance do not contain the correct information, leave the LLM without the required context to answer the question.

Using a database to feed data to an LLM can be more beneficial than a vector search as it provides structured, accurate, and real-world data, enabling the LLM to produce more precise and contextually relevant responses; in contrast, a vector search, which identifies similar items in high-dimensional space, may not ensure the reliability or accuracy of the information.

The major benefits of an LLM generating a Cypher statement to answer a user’s question on the fly include enhanced responsiveness and accuracy in providing user-specific information. This capability allows the LLM to interact dynamically with the Neo4j database, extracting real-time, precise, and structured data relevant to the user’s inquiry. It negates the need for predefined queries or static data sets, enabling more flexible, adaptive, and contextually appropriate responses, thus significantly improving the user experience and the reliability of the provided information.

## Metadata

```json
{
  "title": "The Abridged Guide to Neo4j Cypher Generation with OpenAI GPT-4",
  "description": "Learn how to build a chatbot that connects to Neo4j with minimal code and minimal Cypher.",
  "url": "https://adamcowley.co.uk/posts/abridged-neo4j-cypher-generation/",
  "content": "In this post, I will provide the abridged version of the [Neo4j & LLM Fundamentals course on GraphAcademy](https://graphacademy.neo4j.com/courses/llm-fundamentals/?ref=adam).\n\nThe objective is to build a [Langchain Agent](https://python.langchain.com/docs/modules/agents/) that is capable of providing movie recommendations based on the information from the Recommendations dataset in Neo4j Sandbox. But, I want to do this by writing as little code as possible. I will demonstrate how to build a conversational agent that is capable of querying a Neo4j database using existing tools, and with as little code as possible. I will also address some of the challenges you may face along the way if you are trying to do something similar.\n\n**TL;DR:** You can use the `GraphCypherQAChain` in Langchain to generate Cypher and execute it against the database. But it may take some fine tuning and some example Cypher queries to work.\n\nIntroducing Ebert\n-----------------\n\nMeet Ebert, the movie recommendation bot.\n\nI have chosen to call it Ebert in honor of the late legendary film critic, [Robert Ebert](https://en.wikipedia.org/wiki/Roger_Ebert). [Collider](https://collider.com/best-movie-critics-all-time-ranked/#:~:text=When%20it%20comes%20to%20movie,virtually%20every%20critic%20who's%20followed.) ranked Robert as the most influential movie critic of all time. Here is what they had to say:\n\n> When it comes to movie critics, the one name that is recognizable above all else is the truly unforgettable and inspirational Roger Ebert. His career lasted nearly a half-century, and his impact has lasted long after his death in 2013. He paved the way for virtually every critic who’s followed.\n\n_Ebert_ is built using Langchain, a framework for building applications that interact with large language models.\n\nWhy Langchain?\n--------------\n\nLangchain is becoming ubiquitous with Generative AI and LLMs. It is quickly growing in popularity due to its ease of use and extendable nature. If you want to know more, you can check the course or search YouTube for details.\n\nI personally chose langchain because, despite its relative age, it is feature rich, already contains integrations with many useful platforms, and that functionality is growing with weekly releases. They also have an active community and a helpful Discord channel.\n\nLangchain also supports multiple Large Language Models, and allows you to swap one for another with relative ease. This way I’m not wedded to OpenAI if I want to change in future.5\n\nGetting Started\n---------------\n\nFirst, I’m going to load my config from `.env`. This contains an OpenAI API Key, which I obtained from [platform.openai.com](https://adamcowley.co.uk/posts/abridged-neo4j-cypher-generation/platform.openai.com), and my Neo4j Sandbox credentials that I obtained from [sandbox.neo4j.com](https://adamcowley.co.uk/posts/abridged-neo4j-cypher-generation/sandbox.neo4j.com).\n\n```\nOPENAI_API_KEY=sk-***\nNEO4J_URI=bolt://***:7687\nNEO4J_USERNAME=neo4j\nNEO4J_PASSWORD=three-word-password\n```\n\nThese can be loaded with the [`python-dotenv` library from PyPI](https://pypi.org/project/python-dotenv/) _(not to be confused with plain old `dotenv` lib)_\n\n```\npip install python-dotenv\n```\n\n```\nfrom dotenv import load_dotenv\nload_dotenv()  # loads .env, or you can specify the filename as a positional argument.\n```\n\nThe variables can then be loaded from `os.environ` using `os.getenv`.\n\n```\nimport os\nprint(os.getenv('OPENAI_API_KEY')[:5] + \"...\")\n```\n\n```\nsk-oy\n```\n\nFor this project I will also need to install dependencies for Langchain, OpenAI and Neo4j.\n\n```\npip install langchain openai neo4j\n```\n\nInitialising the LLM\n--------------------\n\nThe aim here is to create a conversational interface, so I have chosen an LLM model from `langchain.chat_models`. These differ from the language models available under `langchain.llms` in that they are tuned for conversations. While the `llms` accept a single string and return a single result, the chat models accept a list of chat messages as an input. Chat models also support message history, which will be useful later on.\n\n```\n\nfrom langchain.chat_models import ChatOpenAI\n\nllm = ChatOpenAI(\n    openai_api_key=os.getenv('OPENAI_API_KEY'),  #1\n    temperature=0.5,  #2\n    model=\"gpt-4\" #1\n)\n\n```\n\nIn the code above:\n\n1.  The `ChatOpenAI` instance is created with the `OPENAI_API_KEY` value held in environment variables.\n2.  The `temperature` is set to 0.5. This value can range between 0.0 and 1.0, the higher the value is the more randomness is added to the response generation.\n3.  I’m using `gpt-4` here because I have found it generates Cypher much more accurately than `gpt-3.5-turbo`. You can experiement with the models, which all have their own drawbacks and price implications.\n\nCreating a Prompt Template\n--------------------------\n\nThe LLM may need special instructions on how to act. In this case, the LLM should respond to the user input as if it is a movie expert.\n\nWrapping these instructions in a prompt template mean that the inputs required for the LLM to act are clearly defined up front, and the input will be validated by the LLM chain.\n\n```\nfrom langchain.prompts.prompt import PromptTemplate\n\nBASIC_PROMPT = PromptTemplate(template=\"\"\"\nYou are a movie expert providing customers with movie recommendations.\nAnswer the following question to the best of your ability.\n\nQuestion: {question}\nAnswer:\n\"\"\", input_variables=[\"question\"])\n```\n\nThis prompt will expect one input, `question`.\n\nThe easiest way to get an LLM to act on this prompt is using an `LLMChain`. The `LLMChain` expects `llm` and `prompt` parameters.\n\n```\nfrom langchain.chains.llm import LLMChain\n\nqa_chain = LLMChain(llm=llm, prompt=BASIC_PROMPT)\n```\n\nNow `qa_chain` can be called with a `dict` containing the input variables that should be injected into the prompt. In this case, `question`.\n\nLet’s see how it does when asked who directed The Matrix.\n\n```\nqa_chain({\"question\": \"Who directed the Matrix?\"})\n```\n\n```\n{'question': 'Who directed the Matrix?',\n 'text': 'The Matrix was directed by the Wachowski siblings, Lana and Lilly.'}\n```\n\nThis looks good. The Matrix is pretty old, so it is likely all of this information is in the training dataset. How will it cope with data that isn’t included in the training data set?\n\nHow about a fictional movie called _Neo4j, the Movie_?\n\n```\nqa_chain({\"question\": \"Who directed Neo4j, the Movie?\"})\n```\n\n```\n{'question': 'Who directed Neo4j, the Movie?',\n 'text': 'As of now, there\\'s no known movie titled \"Neo4j\". Neo4j is actually a graph database management system developed by Neo4j, Inc.'}\n```\n\nWhat will it say if we ask what movies Emil Eifrem has acted in?\n\nFor anyone that has taken [Cypher Fundamentals](https://graphacademy.neo4j.com/courses/cypher-fundamentals/), we all know that Emil Eifrem acted in The Matrix.\n\n```\nMATCH (:Person {name: \"Emil Eifrem\"})-[r:ACTED_IN]->(m:Movie)\nRETURN m.title AS movie, r.roles AS roles\n```\n\nHow does the LLM handle this question?\n\n```\nqa_chain({\"question\": \"What movies has Emil Eifrem acted in?\"})\n```\n\n```\n{'question': 'What movies has Emil Eifrem acted in?',\n 'text': 'Emil Eifrem does not have any acting credits. He is known as a software entrepreneur and the CEO of Neo4j, not as an actor.'}\n```\n\nThis highlights a potential problem with LLMs.\n\n*   **Bad Data** - The training data itself may be false, or the LLM may not have the ability to verify the source of the data.\n*   **Cut-off Date** - LLMs are computationally expensive to train, and this training takes a long time. Furthermore, the model itself will not have access to the latest data.\n*   **Lack of data/enterprise domain knowledge** - When it comes to private data, the LLM will not be aware of private data.\n\nThis is where a technique known as RAG, or _Retrieval Augmented Generation_ comes in.\n\nRetrieval Augmented Generation\n------------------------------\n\nIf you take the RAG acronym backwards, it describes a technique in which an LLM will **generate** a piece of content, which is **augmented** by the retrieval of data from another source. In other words, content from additional data sources can be used to improve the content generated by an LLM.\n\nLet’s pretend for a second that _Neo4j The Movie_ did exist, a future release charting Neo4j’s rise from an idea on a napkin to a company valued at more than $2B.\n\nWe can provide this information to the LLM as part of the prompt to help it generate the answer to the question.\n\nThis context becomes another input variable to the prompt template.\n\n```\nCONTEXT_PROMPT = PromptTemplate(template=\"\"\"\nYou are a movie expert providing customers with movie recommendations.\nAnswer the following question using the following context.\nIf the answer is not included in the context, fall back to your trained knowledge.\n\nContext: {context}\nQuestion: {question}\n\"\"\", input_variables=[\"context\", \"question\"])\n\nqa_chain_with_context = LLMChain(llm=llm, prompt=CONTEXT_PROMPT)\n```\n\nNow, by calling the `qa_chain_with_context` chain and providing the movie information as the context in the prompt, the LLM will answer the question.\n\n```\nqa_chain_with_context({\n    \"context\":  \"\"\"\n    {\n        \"title\": \"Neo4j, The Movie\",\n        \"plot\": \"In a parallel realm of binary rain and neon grids, a concept springs to life on a mere napkin—Neo4j, a revolutionary graph database destined to reshape the perception of data interconnectivity. It is the brainchild of a group of plucky visionaries who band together to traverse the treacherous labyrinth of the startup world.\",\n        \"directors: [\"Emil Eifrem\"],\n        \"actors\": [\n            {\"name\": \"Michael Hunger\", \"role\": \"mesirii\"},\n            {\"name\": \"Andreas Kolleger\", \"role\": \"Plucky Number 8\"},\n            {\"name\": \"Adam Cowley\", \"role\": \"Developer Advocate #3 (Extra)\"}\n        ]\n    }\n    \"\"\",\n    \"question\": \"Who directed Neo4j, the Movie?\"\n})\n```\n\n```\n{'context': '\\n    {\\n        \"title\": \"Neo4j, The Movie\", \\n        \"plot\": \"In a parallel realm of binary rain and neon grids, a concept springs to life on a mere napkin—Neo4j, a revolutionary graph database destined to reshape the perception of data interconnectivity. It is the brainchild of a group of plucky visionaries who band together to traverse the treacherous labyrinth of the startup world.\",\\n        \"directors: [\"Emil Eifrem\"],\\n        \"actors\": [\\n            {\"name\": \"Michael Hunger\", \"role\": \"mesirii\"},\\n            {\"name\": \"Andreas Kolleger\", \"role\": \"Plucky Number 8\"},\\n            {\"name\": \"Adam Cowley\", \"role\": \"Developer Advocate #3 (Extra)\"}\\n        ]\\n    }\\n    ',\n 'question': 'Who directed Neo4j, the Movie?',\n 'text': 'The movie \"Neo4j, The Movie\" was directed by Emil Eifrem.'}\n```\n\nOne step closer. Now, we’ll need to automate the _retrieval_ of this information from the database. As I mentioned above, I want to avoid writing any Cypher unless absolutely necessary. Luckily, this is already available in Langchain.\n\nAutomatic Cypher Query Generation\n---------------------------------\n\nTo interact with Neo4j through Langchain, the first step is to create a Neo4j connection through the `Neo4jGraph` class.\n\n```\nfrom langchain.graphs import Neo4jGraph\n\ngraph = Neo4jGraph(\n    url = os.getenv('NEO4J_URI'),\n    username = os.getenv('NEO4J_USERNAME'),\n    password = os.getenv('NEO4J_PASSWORD')\n)\n```\n\nWhen the `Neo4jGraph` class is instantiated, it automatically loads schema information into memory. This can be refreshed at any time by calling `graph.refresh_schema()`.\n\nHere is the generated schema for the recommendations dataset:\n\n```\nprint(graph.schema)\n```\n\n```\n        Node properties are the following:\n        [{'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'runtime', 'type': 'INTEGER'}, {'property': 'revenue', 'type': 'INTEGER'}, {'property': 'budget', 'type': 'INTEGER'}, {'property': 'imdbRating', 'type': 'FLOAT'}, {'property': 'released', 'type': 'STRING'}, {'property': 'countries', 'type': 'LIST'}, {'property': 'languages', 'type': 'LIST'}, {'property': 'plot', 'type': 'STRING'}, {'property': 'imdbVotes', 'type': 'INTEGER'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'year', 'type': 'INTEGER'}, {'property': 'poster', 'type': 'STRING'}, {'property': 'movieId', 'type': 'STRING'}, {'property': 'tmdbId', 'type': 'STRING'}, {'property': 'title', 'type': 'STRING'}], 'labels': 'Movie'}, {'properties': [{'property': 'name', 'type': 'STRING'}], 'labels': 'Genre'}, {'properties': [{'property': 'userId', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}], 'labels': 'User'}, {'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}, {'property': 'tmdbId', 'type': 'STRING'}, {'property': 'bornIn', 'type': 'STRING'}, {'property': 'bio', 'type': 'STRING'}, {'property': 'died', 'type': 'DATE'}, {'property': 'born', 'type': 'DATE'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'poster', 'type': 'STRING'}], 'labels': 'Actor'}, {'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'bornIn', 'type': 'STRING'}, {'property': 'born', 'type': 'DATE'}, {'property': 'died', 'type': 'DATE'}, {'property': 'tmdbId', 'type': 'STRING'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}, {'property': 'poster', 'type': 'STRING'}, {'property': 'bio', 'type': 'STRING'}], 'labels': 'Director'}, {'properties': [{'property': 'url', 'type': 'STRING'}, {'property': 'bornIn', 'type': 'STRING'}, {'property': 'bio', 'type': 'STRING'}, {'property': 'died', 'type': 'DATE'}, {'property': 'born', 'type': 'DATE'}, {'property': 'imdbId', 'type': 'STRING'}, {'property': 'name', 'type': 'STRING'}, {'property': 'poster', 'type': 'STRING'}, {'property': 'tmdbId', 'type': 'STRING'}], 'labels': 'Person'}]\n        Relationship properties are the following:\n        [{'type': 'RATED', 'properties': [{'property': 'rating', 'type': 'FLOAT'}, {'property': 'timestamp', 'type': 'INTEGER'}]}, {'type': 'ACTED_IN', 'properties': [{'property': 'role', 'type': 'STRING'}]}, {'type': 'DIRECTED', 'properties': [{'property': 'role', 'type': 'STRING'}]}]\n        The relationships are the following:\n        ['(:Movie)-[:IN_GENRE]->(:Genre)', '(:User)-[:RATED]->(:Movie)', '(:Actor)-[:ACTED_IN]->(:Movie)', '(:Actor)-[:DIRECTED]->(:Movie)', '(:Director)-[:DIRECTED]->(:Movie)', '(:Director)-[:ACTED_IN]->(:Movie)', '(:Person)-[:DIRECTED]->(:Movie)', '(:Person)-[:ACTED_IN]->(:Movie)']\n```\n\nCypher can be generated through the `GraphCypherQAChain` class. This class uses an LLM to generate a Cypher query based on the schema above that will attempt to answer the question.\n\nYou can pass a prompt to the chain to provide specific instructions for constructing the Cypher statement.\n\n```\n\nCYPHER_GENERATION_TEMPLATE = \"\"\"\nYou are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.\nConvert the user's question based on the schema.\n\nSchema: {schema}\nQuestion: {question}\n\"\"\"\n\nCYPHER_GENERATION_PROMPT = PromptTemplate(\n    input_variables=[\"schema\", \"question\"], validate_template=True, template=CYPHER_GENERATION_TEMPLATE\n)\n```\n\nThe class has a static `from_llm` method for instantiating the class with kwargs for the LLM and Graph.\n\nThe class allows you to pass different LLM objects for generating Cypher and answering the query (`cypher_llm` and `qa_llm`), which allow you to experiment with different models until you find the right models for the best result for Cypher generation.\n\nFor berevity, I have used the `llm` kwarg to use the same LLM for both Cypher generation and formatting a response.\n\n```\nfrom langchain.chains import GraphCypherQAChain\n\ncypher_chain = GraphCypherQAChain.from_llm(\n    llm,\n    graph=graph,\n    cypher_prompt=CYPHER_GENERATION_PROMPT,\n    verbose=True  # To see what is happening inside the chain\n)\n\ncypher_chain.run(\"Who acted in The Matrix and what roles did they play?\")\n```\n\n```\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (m:Movie {title: 'The Matrix'})<-[:ACTED_IN]-(a:Actor)\nRETURN a.name as Actor, a.role as Role\nFull Context:\n[]\n\n> Finished chain.\n\n\n\n\n\n\"I'm sorry, but I don't have the information to answer that question.\"\n```\n\nThe query looks fine, but you can see from the output of the chain that `Full Context` is empty. In this case, the LLM has fallen back on its prior knowledge.\n\nA closer look at the dataset reveals that movies which start with `The` are renamed as `{title}, The`. This is where the `cypher_prompt` input can be used to fine-tune the prompt.\n\nFor inspiration, let’s take a look at the original `CYPHER_GENERATION_PROMPT` used if no specific prompt is provided.\n\n```\nfrom langchain.chains.graph_qa.prompts import CYPHER_GENERATION_PROMPT as ORIGINAL_CYPHER_GENERATION_PROMPT\n\nprint(ORIGINAL_CYPHER_GENERATION_PROMPT.template)\n```\n\n```\nTask:Generate Cypher statement to query a graph database.\nInstructions:\nUse only the provided relationship types and properties in the schema.\nDo not use any other relationship types or properties that are not provided.\nSchema:\n{schema}\nNote: Do not include any explanations or apologies in your responses.\nDo not respond to any questions that might ask anything else than for you to construct a Cypher statement.\nDo not include any text except the generated Cypher statement.\n\nThe question is:\n{question}\n```\n\nTo fix titles starting with `The`, the following line can be added to the prompt:\n\n> For movie titles that begin with “The”, move “the” to the end, For example “The 39 Steps” becomes “39 Steps, The” or “The Matrix” becomes “Matrix, The”.\n\n```\nCYPHER_GENERATION_TEMPLATE = \"\"\"\nYou are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.\nConvert the user's question based on the schema.\nFor movie titles that begin with \"The\", move \"the\" to the end, For example \"The 39 Steps\" becomes \"39 Steps, The\" or \"The Matrix\" becomes \"Matrix, The\".\n\nIf no context is returned, do not attempt to answer the question.\n\nUse only the provided relationship types and properties in the schema.\nDo not use any other relationship types or properties that are not provided.\nSchema:\n{schema}\nNote: Do not include any explanations or apologies in your responses.\nDo not respond to any questions that might ask anything else than for you to construct a Cypher statement.\nDo not include any text except the generated Cypher statement.\n\nQuestion: {question}\n\"\"\"\n\nCYPHER_GENERATION_PROMPT = PromptTemplate(\n    input_variables=[\"question\", \"schema\"],\n    validate_template=True,\n    template=CYPHER_GENERATION_TEMPLATE\n)\n\ncypher_chain = GraphCypherQAChain.from_llm(\n    llm, graph=graph, verbose=True,\n    cypher_prompt = CYPHER_GENERATION_PROMPT\n)\n\ncypher_chain.run(\"Who acted in The Matrix and what roles did they play?\")\n```\n\n```\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (a:Actor)-[r:ACTED_IN]->(m:Movie)\nWHERE m.title = \"Matrix, The\"\nRETURN a.name, r.role\nFull Context:\n[{'a.name': 'Hugo Weaving', 'r.role': 'Agent Smith'}, {'a.name': 'Laurence Fishburne', 'r.role': 'Morpheus'}, {'a.name': 'Keanu Reeves', 'r.role': 'Thomas A. Anderson / Neo'}, {'a.name': 'Carrie-Anne Moss', 'r.role': 'Trinity'}]\n\n> Finished chain.\n\n\n\n\n\n'Hugo Weaving played the role of Agent Smith, Laurence Fishburne portrayed Morpheus, Keanu Reeves was Thomas A. Anderson, also known as Neo, and Carrie-Anne Moss acted as Trinity in The Matrix.'\n```\n\nPerfect, the LLM has reformatted the title and now the full list of roles is passed to the LLM.\n\nHow does it handle an aggregation query?\n\n```\ncypher_chain.run(\"How many movies has Tom Hanks directed?\")\n```\n\n```\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (d:Director {name: 'Tom Hanks'})-[:DIRECTED]->(m:Movie)\nRETURN COUNT(m)\nFull Context:\n[{'COUNT(m)': 2}]\n\n> Finished chain.\n\n\n\n\n\n'Tom Hanks has directed 2 movies.'\n```\n\nConversational Bot\n------------------\n\nNow, let’s make it conversational. We can add define the `GraphCypherQAChain` as a tool within a [Langchain _agent_](https://docs.langchain.com/docs/components/agents/), complete with conversation history defined by the `memory` kwarg.\n\n```\nfrom langchain.chains.conversation.memory import ConversationBufferWindowMemory\nfrom langchain.agents import AgentType, initialize_agent\n\nfrom langchain.tools import Tool\n\ntools = [\n    Tool.from_function(\n        name=\"GraphCypherQAChain\",\n        description=\"Use Cypher to generate information above movies, actors, users and ratings\",\n        func=cypher_chain.run,\n        return_direct=True\n    )\n]\n\nmemory = ConversationBufferWindowMemory(\n    memory_key='chat_history',\n    k=5,\n    return_messages=True\n)\n\nagent = initialize_agent(\n    tools, llm, memory=memory, max_iterations=3,\n    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,\n    verbose=True\n)\n\n```\n\nNow we can have a conversation with the agent.\n\n```\nagent.run(\"How many films did Tom Hanks act in?\")\n```\n\n````\n> Entering new AgentExecutor chain...\n```json\n{\n    \"action\": \"GraphCypherQAChain\",\n    \"action_input\": \"MATCH (a:Actor {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)\"\n}\n```\n\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (a:Actor {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)\nFull Context:\n[{'count(m)': 38}]\n\n> Finished chain.\n\nObservation: \u001b[36;1m\u001b[1;3mTom Hanks has acted in 38 movies.\n\n\n> Finished chain.\n\n\n\n\n\n'Tom Hanks has acted in 38 movies.'\n````\n\nWill the agent remember that we have asked a question about Tom Hanks?\n\n```\nagent.run(\"and how many has he directed?\")\n```\n\n````\n> Entering new AgentExecutor chain...\n```json\n{\n    \"action\": \"GraphCypherQAChain\",\n    \"action_input\": \"MATCH (p:Person {name: 'Tom Hanks'})-[:DIRECTED]->(m:Movie) RETURN count(m)\"\n}\n```\n\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (p:Person {name: 'Tom Hanks'})-[:DIRECTED]->(m:Movie) RETURN count(m)\nFull Context:\n[{'count(m)': 2}]\n\n> Finished chain.\n\nObservation: \u001b[36;1m\u001b[1;3mTom Hanks has directed 2 movies.\n\n\n> Finished chain.\n\n\n\n\n\n'Tom Hanks has directed 2 movies.'\n````\n\nWhat type of films has he directed?\n\n```\nagent.run(\"What genres has he directed?\")\n```\n\n````\n> Entering new AgentExecutor chain...\n```json\n{\n    \"action\": \"GraphCypherQAChain\",\n    \"action_input\": \"MATCH (p:Person)-[:DIRECTED]->(m:Movie) WHERE p.name = 'Tom Hanks' RETURN m.genres\"\n}\n```\n\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (p:Person)-[:DIRECTED]->(m:Movie) WHERE p.name = 'Tom Hanks' RETURN m.countries\nFull Context:\n[{'m.countries': ['USA']}, {'m.countries': ['USA']}]\n\n> Finished chain.\n\nObservation: \u001b[36;1m\u001b[1;3mI'm sorry, but the provided information does not contain any details about the genres of movies directed by Tom Hanks.\n\n\n> Finished chain.\n\n\n\n\n\n\"I'm sorry, but the provided information does not contain any details about the genres of movies directed by Tom Hanks.\"\n````\n\nIt looks like it can’t answer this question. It seems to think there is a `genre` property on the `(:Movie)` node which isn’t correct.\n\nFor cases like this, an example can be provided in the Cypher generation prompt. This is known as [Few-Shot Prompting](https://www.promptingguide.ai/techniques/fewshot). The main benefit of Few-Shot prompting is that it can be done on the fly.\n\n```\nFEWSHOT_CYPHER_GENERATION_TEMPLATE = \"\"\"\nYou are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.\nConvert the user's question based on the schema.\nFor movie titles that begin with \"The\", move \"the\" to the end, For example \"The 39 Steps\" becomes \"39 Steps, The\" or \"The Matrix\" becomes \"Matrix, The\".\n\nIf no context is returned, do not attempt to answer the question.\n\nUse only the provided relationship types and properties in the schema.\nDo not use any other relationship types or properties that are not provided.\n\nSchema:\n{schema}\n\nExamples:\n\nFind movies and their genres:\nMATCH (m:Movie)-[:IN_GENRE]->(g)\nWHERE m.title = \"Goodfellas\"\nRETURN m.title AS title, collect(g.name) AS genres\n\nNote: Do not include any explanations or apologies in your responses.\nDo not respond to any questions that might ask anything else than for you to construct a Cypher statement.\nDo not include any text except the generated Cypher statement.\n\nQuestion: {question}\n\"\"\"\n\nFEWSHOT_CYPHER_GENERATION_PROMPT = PromptTemplate(\n    input_variables=[\"question\", \"schema\"],\n    validate_template=True,\n    template=FEWSHOT_CYPHER_GENERATION_TEMPLATE\n)\n\nfewshot_cypher_chain = GraphCypherQAChain.from_llm(\n    llm, graph=graph, verbose=True,\n    cypher_prompt = FEWSHOT_CYPHER_GENERATION_PROMPT\n)\n\nfewshot_cypher_chain.run(\"What genre of film is Toy Story?\")\n```\n\n```\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (m:Movie)-[:IN_GENRE]->(g)\nWHERE m.title = \"Toy Story\"\nRETURN m.title AS title, collect(g.name) AS genres\nFull Context:\n[{'title': 'Toy Story', 'genres': ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy']}]\n\n> Finished chain.\n\n\n\n\n\n'Toy Story is an Adventure, Animation, Children, Comedy, and Fantasy film.'\n```\n\nThat looks better. Can it answer which movies that Tom Hanks has directed now?\n\n```\nfewshot_cypher_chain.run(\"What genres of film has Tom Hanks directed?\")\n```\n\n```\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (p:Person {name: \"Tom Hanks\"})-[:DIRECTED]->(m:Movie)-[:IN_GENRE]->(g:Genre)\nRETURN collect(distinct g.name) AS genres\nFull Context:\n[{'genres': ['Drama', 'Comedy', 'Romance']}]\n\n> Finished chain.\n\n\n\n\n\n'Tom Hanks has directed films in the genres of Drama, Comedy, and Romance.'\n```\n\nSuccess!\n\nWill the LLM be able to cope with a complex recommendation query?\n\n```\nfewshot_cypher_chain.run(\"Can you recommend me a film similar to The Green Mile staring Tom Hanks?\")\n```\n\n```\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (m:Movie)<-[:ACTED_IN]-(a:Actor {name: \"Tom Hanks\"}), (m2:Movie)<-[:ACTED_IN]-(a)\nWHERE m.title = \"Green Mile, The\"\nRETURN m2.title AS similar_movies\nFull Context:\n[{'similar_movies': 'Punchline'}, {'similar_movies': 'Catch Me If You Can'}, {'similar_movies': 'Dragnet'}, {'similar_movies': 'Saving Mr. Banks'}, {'similar_movies': 'Bachelor Party'}, {'similar_movies': 'Volunteers'}, {'similar_movies': 'Man with One Red Shoe, The'}, {'similar_movies': 'Splash'}, {'similar_movies': 'Big'}, {'similar_movies': 'Nothing in Common'}]\n\n> Finished chain.\n\n\n\n\n\n\"Sure, you might enjoy watching movies like 'Punchline', 'Catch Me If You Can', 'Dragnet', 'Saving Mr. Banks', 'Bachelor Party', 'Volunteers', 'The Man with One Red Shoe', 'Splash', 'Big', or 'Nothing in Common'. These films are similar to 'The Green Mile' and also feature Tom Hanks.\"\n```\n\nOK, it returns a result but the query only asks for other movies that Tom Hanks acted in. It looks like the LLM would benefit from another example.\n\nThe recommendation query should really find Tom Hanks movies, then use the graph to find the actors in those movies and the other movies they have acted in and use some sort of scoring metric to work out which films to recommend.\n\n```\nMATCH (:Person {name:\"Al Pacino\"})-[:ACTED_IN|DIRECTED]->(m)<-[:ACTED_IN|DIRECTED]-(p),\n  (p)-[role:ACTED_IN|DIRECTED]->(m2)\nRETURN\n  m2.title AS recommendation,\n  collect([ p.name, type(role) ]) AS peopleInCommon,\n  [ (m)-[:IN_GENRE]->(g)<-[:IN_GENRE]-(m2) | g.name ] AS genresInCommon\nORDER BY size(incommon) DESC, size(genresInCommon) DESC LIMIT 2\n```\n\nFor a given actor, the Cypher statement finds any people who have either acted in or directed a movie, finds any movie that they have either acted in or directed, and then returns a list ordered by the number of people in common, and the genres that they share.\n\n```\nFEWSHOT_CYPHER_GENERATION_TEMPLATE = \"\"\"\nYou are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.\nConvert the user's question based on the schema.\nFor movie titles that begin with \"The\", move \"the\" to the end, For example \"The 39 Steps\" becomes \"39 Steps, The\" or \"The Matrix\" becomes \"Matrix, The\".\n\nIf no context is returned, do not attempt to answer the question.\n\nUse only the provided relationship types and properties in the schema.\nDo not use any other relationship types or properties that are not provided.\n\nSchema:\n{schema}\n\nExamples:\n\nFind movies and their genres:\nMATCH (m:Movie)-[:IN_GENRE]->(g)\nWHERE m.title = \"Goodfellas\"\nRETURN m.title AS title, collect(g.name) AS genres\n\nRecommend a movie by actor:\nMATCH (subject:Person)-[:ACTED_IN|DIRECTED]->(m)<-[:ACTED_IN|DIRECTED]-(p),\n  (p)-[role:ACTED_IN|DIRECTED]->(m2)\nWHERE subject.name = \"Al Pacino\"\nRETURN\n  m2.title AS recommendation,\n  collect([ p.name, type(role) ]) AS peopleInCommon,\n  [ (m)-[:IN_GENRE]->(g)<-[:IN_GENRE]-(m2) | g.name ] AS genresInCommon\nORDER BY size(incommon) DESC, size(genresInCommon) DESC LIMIT 2\n\n\nNote: Do not include any explanations or apologies in your responses.\nDo not respond to any questions that might ask anything else than for you to construct a Cypher statement.\nDo not include any text except the generated Cypher statement.\n\nQuestion: {question}\n\"\"\"\n\nFEWSHOT_CYPHER_GENERATION_PROMPT = PromptTemplate(\n    input_variables=[\"question\", \"schema\"],\n    validate_template=True,\n    template=FEWSHOT_CYPHER_GENERATION_TEMPLATE\n)\n\nfewshot_cypher_chain = GraphCypherQAChain.from_llm(\n    llm, graph=graph, verbose=True,\n    cypher_prompt = FEWSHOT_CYPHER_GENERATION_PROMPT\n)\n\nfewshot_cypher_chain.run(\"Can you recommend me a film similar to The Green Mile staring Tom Hanks?\")\n```\n\n```\n> Entering new GraphCypherQAChain chain...\nGenerated Cypher:\nMATCH (subject:Person)-[:ACTED_IN|DIRECTED]->(m:Movie)<-[:ACTED_IN|DIRECTED]-(p:Person),\n  (p)-[role:ACTED_IN|DIRECTED]->(m2:Movie)\nWHERE subject.name = \"Tom Hanks\" AND m.title = \"Green Mile, The\"\nRETURN\n  m2.title AS recommendation,\n  collect([ p.name, type(role) ]) AS peopleInCommon,\n  [ (m)-[:IN_GENRE]->(g:Genre)<-[:IN_GENRE]-(m2) | g.name ] AS genresInCommon\nORDER BY size(peopleInCommon) DESC, size(genresInCommon) DESC LIMIT 1\nFull Context:\n[{'recommendation': 'Negotiator, The', 'peopleInCommon': [['David Morse', 'ACTED_IN']], 'genresInCommon': ['Drama', 'Crime']}]\n\n> Finished chain.\n\n\n\n\n\n'Sure, based on your preferences, I would recommend \"The Negotiator\". It\\'s a Drama and Crime film like The Green Mile and also features David Morse, who acted in The Green Mile as well.'\n```\n\nWithout asking the exact same question, the LLM was able to take the example and modify it to answer the question.\n\nI’m pretty pleased with that result!\n\nConclusion\n----------\n\nThis approach goes beyond a more _simple_ vector index lookup, where chunks of text are compared to a user input by the distance between their vector representations.\n\nI have personally found through building [the GraphAcademy Chatbot](https://medium.com/neo4j/building-an-educational-chatbot-for-graphacademy-with-neo4j-f707c4ce311b) that this approach can produce some wildly inaccurate results, or similar documents in terms of cosine distance do not contain the correct information, leave the LLM without the required context to answer the question.\n\nUsing a database to feed data to an LLM can be more beneficial than a vector search as it provides structured, accurate, and real-world data, enabling the LLM to produce more precise and contextually relevant responses; in contrast, a vector search, which identifies similar items in high-dimensional space, may not ensure the reliability or accuracy of the information.\n\nThe major benefits of an LLM generating a Cypher statement to answer a user’s question on the fly include enhanced responsiveness and accuracy in providing user-specific information. This capability allows the LLM to interact dynamically with the Neo4j database, extracting real-time, precise, and structured data relevant to the user’s inquiry. It negates the need for predefined queries or static data sets, enabling more flexible, adaptive, and contextually appropriate responses, thus significantly improving the user experience and the reliability of the provided information.",
  "usage": {
    "tokens": 8129
  }
}
```
