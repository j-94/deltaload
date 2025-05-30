---
title: Three AI Design Patterns of Autonomous Agents - Alexander Sniffin - Medium
description: One of the hottest topics in AI over the past year has been the use of Large Language Models (LLMs) as reasoning engines for autonomous agents. The enhanced reasoning capabilities of models such as…
url: https://alexsniffin.medium.com/three-ai-design-patterns-of-autonomous-agents-8372b9402f7c
timestamp: 2025-01-20T16:01:18.444Z
domain: alexsniffin.medium.com
path: three-ai-design-patterns-of-autonomous-agents-8372b9402f7c
---

# Three AI Design Patterns of Autonomous Agents - Alexander Sniffin - Medium


One of the hottest topics in AI over the past year has been the use of Large Language Models (LLMs) as reasoning engines for autonomous agents. The enhanced reasoning capabilities of models such as…


## Content

[![Image 25: Alexander Sniffin](https://miro.medium.com/v2/resize:fill:88:88/1*OU4NzGP2yvJCI6R1MntSaA.png)](https://alexsniffin.medium.com/?source=post_page---byline--8372b9402f7c--------------------------------)

One of the hottest topics in AI over the past year has been the use of Large Language Models (LLMs) as reasoning engines for autonomous agents.

The enhanced reasoning capabilities of models such as GPT, Claude, Llama and Gemini have set the stage for the creation of increasingly sophisticated and powerful agents.

I’ll go over the core concepts to building agents as well as three different design patterns and how to implement them:

*   ReAct Agent
*   Task-Planner Agent
*   Multi-Agent Orchestration

Each pattern is agnostic of language and framework and will address different concepts as well as design complexities that arise between each.

Core Concepts
-------------

Before jumping into each pattern, let’s first understand the common elements utilized across these designs.

Prompting
---------

A fundamental component in building agents is the prompting techniques applied to the language model.

The typical method for creating prompts involves incorporating intermediate reasoning steps with the model, this is commonly referred to as [Chain of Thought](https://www.promptingguide.ai/techniques/cot) (CoT) prompting. This technique allows the model to solve complex problems incrementally.

![Image 26](https://miro.medium.com/v2/resize:fit:700/1*MjgImQ_rgbQWPfLqagtMMA.png)

Source [promptingguide.ai](https://www.promptingguide.ai/)

By introducing intermediate steps, the model can generate more accurate answers compared to other methods such as [zero-shot prompting](https://www.promptingguide.ai/techniques/zeroshot).

Another technique, known as Reasoning and Acting ([ReAct](https://www.promptingguide.ai/techniques/react)) prompting, is an extension of CoT but includes actionable steps that can be executed within an environment.

![Image 27](https://miro.medium.com/v2/resize:fit:700/1*kW8CLs5u8_O_iTzz7kW9UA.png)

Source [promptingguide.ai](https://www.promptingguide.ai/)

In the example given, the model determines actions to take which return information that is then passed to the model through [in-context learning](https://www.hopsworks.ai/dictionary/in-context-learning-icl) to help solve the problem.

If we attempted to solve this without the factual context from the actions, the model would likely [hallucinate](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) an answer.

Other techniques like [self-reflection](https://www.promptingguide.ai/techniques/reflexion) (Reflexion) is a way to introduce verbal reinforcement to the model to self-reflect previous steps taken. All of these techniques involve breaking down the prompt into multiple steps.

Persona
-------

A way to keep the model on topic and generate the best answers is through the use of a persona. This is often set as the initial prompt (also known as the system prompt) used with the agent to limit and keep the output focused on the type of problem you want the model to solve.

For example, for an agent that focuses on writing code, assigning the persona of an “expert programmer” can improve reasoning and keep the model’s output limited to programming-related topics.

Tools
-----

Agents need a way to perform actions with their environment. This can be done through the use of tools, similar to how we (as humans) use tools to help solve our own problems, agents can also use tools that we define.

For an agent, a tool is part of our program that the model learns to use through in-context learning. This takes a schema, using a structured input and output that the model is able to **reason** potential parameters for. By using the model like a natural language reasoning engine, we attempt to generate **actions** from the semantics of the request.

Structured Input & Output
-------------------------

When prompting models we typically use natural language but when building agents we need a way to “marshal” intent to and from our application memory. One common way to do this is using structured language that the model has been trained on. This is typically JSON, although other structured languages can also be compatible with many models.

Memory
------

The agent needs a way to track what has been done between each step. We can think of this like a “scratchpad” where the agent will take notes on what its done so far. This can be short-term memory (usually stateless) or long-term memory (stateful).

**Workflows**
-------------

To program and orchestrate the behavior of the agent with your application logic, a workflow is required. There are various types of workflows such as directed acyclic graphs (DAGs), finite state machines (FSM), and control flow graphs (CFG).

Here is some general guidance for choosing the right workflow:

*   **DAGs**: Suitable for programming a directed series of steps that don’t require backtracking or cycles.
*   **FSMs**: Ideal when programming with a finite number of states, transitions, and actions without directed flow.
*   **CFGs**: Best for programming a dynamic series of steps where conditions determine the flow, allowing for cycles and backtracking.

In this article, I will primarily cover FSMs as a way to program agentic workflows. However, different techniques can serve various purposes when implementing agents. The problem you’re trying to solve with your agent should guide the type of workflow you choose.

Notable frameworks for building custom workflow orchestration include:

*   [Haystack](https://haystack.deepset.ai/) — an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. Haystack focuses on building DAG’s. Example of retrieval augmented generation (RAG) as a DAG:

![Image 28](https://miro.medium.com/v2/resize:fit:446/1*0RHeqTwsSGeIvJgnmCgqAg.png)

Source [Haystack](https://docs.haystack.deepset.ai/docs/visualizing-pipelines)

*   [LangGraph](https://langchain-ai.github.io/langgraph/) — a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Compared to other LLM frameworks, it offers these core benefits: cycles, controllability, and persistence. LangGraph allows you to define flows that involve cycles, essential for most agentic architectures, differentiating it from DAG-based solutions. LangGraph focuses on building CFGs. Example of agentic RAG with a cycle:

![Image 29](https://miro.medium.com/v2/resize:fit:700/1*1yhnd3b7xsHjWk2YLuzqmA.png)

Source [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_agentic_rag.ipynb)

*   [assemble](https://github.com/alexsniffin/assemble) — an experimental framework written by me for building Agents through the use of an FSM.

ReAct Agent
-----------

The ReAct agent specializes in reasoning and action handling within its environment.

In this pattern, we can implement different ReAct prompts as specific states in a FSM. This approach ensures that the agent’s responses are consistent and relevant to the current context or task at hand.

Each state can represent various properties, including:

*   a prompt for the model and,
*   a handler for mapping application logic to and from the model

The main states used in ReAct are:

*   Thought — addresses the problem given the previous actions taken and determines the next step to take.
*   Act — determines the correct tool to use and the correct input for that tool.
*   Observe — summarizes the behavior from the action to the memory.

![Image 30](https://miro.medium.com/v2/resize:fit:652/1*LBcke9bluRWC537Y_CfjoQ.gif)

Simple example of an FSM Agent

The benefits of implementing the agent this way are:

*   predictability
*   tasks are isolated from other states
*   easy to troubleshoot
*   easy to add new states

Potential problems include:

*   prone to getting stuck in loops
*   can get side tracked or lose focus from the original request

A simple FSM ReAct agent can be written in Python, for this example lets assume the LLM backend is implemented elsewhere and the agent has tools and memory.

Notebook example of an FSM agent

The example uses a StockTicker price tool to get factual information on ticker prices. The agent can reason when the question is asking about a particular ticker and use the tool. It’s possible to add in additional tools to ask more complex questions. Each handler contains a prompt and the correct structured input and output parsing using [Pydantic](https://docs.pydantic.dev/latest/) to create JSON schemas.

This implementation isn’t complete but addresses a simple way to build this agent.

Additional improvements would be:

*   to add [context-window](https://www.hopsworks.ai/dictionary/context-window-for-llms) awareness to the memory. If the tool output or memory grows too large, you would need to compress it. We can figure out the length of our memory by [tokenizing](https://sidsite.com/posts/bpe/) everything first to see whether the memory is too large. If it is, then you can do summarization, truncation or another technique to reduce the total tokens in the memory.
*   adding control-flows for context cancellation or escaping from loops.

One of the advantages to implementing the agent with an FSM is that it isn’t limited to just ReAct states. Additional states can be defined for more complex behaviors. This pattern allows for a solid foundation and extensible basis to building agents.

Task-Planner Agent
------------------

The task planner is an agent which defines a concrete plan on what needs to be done and attempts to work through that plan in multiple steps. It’s an extension of the ReAct agent by introducing a planning step.

The plan will consist of tasks where each task is an isolated piece of work. In the below example, the task planner defines a set of tasks and will work through them one at a time.

![Image 31](https://miro.medium.com/v2/resize:fit:542/1*KZYOxQUumADUT6medHzSZA.gif)

Simple example of a Task-Planner Agent

We can test the planning prompt for generating tasks using the OpenAI playground with GPT 4 Turbo.

![Image 32](https://miro.medium.com/v2/resize:fit:700/1*ck1KCa56AjV3VBAKmpBjAA.png)

OpenAI Playground

The model is able to create isolated tasks on what might need to be done.

Like the ReAct example, the design for this agent can use an FSM as the basis of its implementation. The planning step would occur as a new state and the action state would instead pop from the stack of tasks and observe the output from the tools.

The benefit of this pattern is that work is planned upfront rather than continuously like the ReAct agent. This defines intermediate steps early that can help reduce the chance of getting stuck in a loop, but it’s not guaranteed.

This also comes with some problems where the agent might initially make a mistake in the plan which might cause errors throughout the tasks and require backtracking and generating new tasks. There’s a chance tasks are impossible to solve like invalid tool usage which requires a new plan and starting over. This can be an expensive mistake, therefore planning should be limited to tasks which are easily predictable.

This type of prompting is similar to an early project that got popular called [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) which uses a task queue to breakdown the problem into small pieces of work. This was one of the first projects to implement agentic like workflows with language models.

Multi-Agent Orchestration
-------------------------

When asking agents complex tasks, it’s often difficult to scale the behavior of the agent correctly. This is a limiting factor for a number reasons, such as the persona, too many types of actions or too many states on what the agent could do.

One approach to solving this problem is by separating responsibilities of the agent and introducing another reasoning step for communication with other agents.

By giving agents the ability to communicate, they can delegate work through orchestration of tasks. This approach is similar to a [delegation-like pattern](https://en.wikipedia.org/wiki/Delegation_pattern).

Rather than having a single agent that does everything, we can define agents that specialize in solving specific problems that also have different implementations.

Instead of having the agent figure out who to communicate with, we can introduce an **orchestrator** that can both supervise and route between agents to get the best desired output based on the task.

![Image 33](https://miro.medium.com/v2/resize:fit:536/1*qOfzg_oTtwJG5Kd6Rss8Zg.gif)

Example of a communication with an orchestration agent

By separating and abstracting communication, agents don’t need to know how a task is solved.

Like the previous examples, an orchestration step can be defined using the FSM and the previous prompting techniques.

Examples of Multi-Agent Implementations
---------------------------------------

Multi-agent implementations have been growing popular in the community to better scale tasks.

One such project is [CrewAI](https://github.com/joaomdmoura/crewAI) where you can define the persona of your agents, their capabilities and then create a “crew” where the agents work together to solve the tasks.

Example code from CrewAI:

Example of building a crew with CrewAI

## Metadata

```json
{
  "title": "Three AI Design Patterns of Autonomous Agents - Alexander Sniffin - Medium",
  "description": "One of the hottest topics in AI over the past year has been the use of Large Language Models (LLMs) as reasoning engines for autonomous agents. The enhanced reasoning capabilities of models such as…",
  "url": "https://alexsniffin.medium.com/three-ai-design-patterns-of-autonomous-agents-8372b9402f7c",
  "content": "[![Image 25: Alexander Sniffin](https://miro.medium.com/v2/resize:fill:88:88/1*OU4NzGP2yvJCI6R1MntSaA.png)](https://alexsniffin.medium.com/?source=post_page---byline--8372b9402f7c--------------------------------)\n\nOne of the hottest topics in AI over the past year has been the use of Large Language Models (LLMs) as reasoning engines for autonomous agents.\n\nThe enhanced reasoning capabilities of models such as GPT, Claude, Llama and Gemini have set the stage for the creation of increasingly sophisticated and powerful agents.\n\nI’ll go over the core concepts to building agents as well as three different design patterns and how to implement them:\n\n*   ReAct Agent\n*   Task-Planner Agent\n*   Multi-Agent Orchestration\n\nEach pattern is agnostic of language and framework and will address different concepts as well as design complexities that arise between each.\n\nCore Concepts\n-------------\n\nBefore jumping into each pattern, let’s first understand the common elements utilized across these designs.\n\nPrompting\n---------\n\nA fundamental component in building agents is the prompting techniques applied to the language model.\n\nThe typical method for creating prompts involves incorporating intermediate reasoning steps with the model, this is commonly referred to as [Chain of Thought](https://www.promptingguide.ai/techniques/cot) (CoT) prompting. This technique allows the model to solve complex problems incrementally.\n\n![Image 26](https://miro.medium.com/v2/resize:fit:700/1*MjgImQ_rgbQWPfLqagtMMA.png)\n\nSource [promptingguide.ai](https://www.promptingguide.ai/)\n\nBy introducing intermediate steps, the model can generate more accurate answers compared to other methods such as [zero-shot prompting](https://www.promptingguide.ai/techniques/zeroshot).\n\nAnother technique, known as Reasoning and Acting ([ReAct](https://www.promptingguide.ai/techniques/react)) prompting, is an extension of CoT but includes actionable steps that can be executed within an environment.\n\n![Image 27](https://miro.medium.com/v2/resize:fit:700/1*kW8CLs5u8_O_iTzz7kW9UA.png)\n\nSource [promptingguide.ai](https://www.promptingguide.ai/)\n\nIn the example given, the model determines actions to take which return information that is then passed to the model through [in-context learning](https://www.hopsworks.ai/dictionary/in-context-learning-icl) to help solve the problem.\n\nIf we attempted to solve this without the factual context from the actions, the model would likely [hallucinate](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) an answer.\n\nOther techniques like [self-reflection](https://www.promptingguide.ai/techniques/reflexion) (Reflexion) is a way to introduce verbal reinforcement to the model to self-reflect previous steps taken. All of these techniques involve breaking down the prompt into multiple steps.\n\nPersona\n-------\n\nA way to keep the model on topic and generate the best answers is through the use of a persona. This is often set as the initial prompt (also known as the system prompt) used with the agent to limit and keep the output focused on the type of problem you want the model to solve.\n\nFor example, for an agent that focuses on writing code, assigning the persona of an “expert programmer” can improve reasoning and keep the model’s output limited to programming-related topics.\n\nTools\n-----\n\nAgents need a way to perform actions with their environment. This can be done through the use of tools, similar to how we (as humans) use tools to help solve our own problems, agents can also use tools that we define.\n\nFor an agent, a tool is part of our program that the model learns to use through in-context learning. This takes a schema, using a structured input and output that the model is able to **reason** potential parameters for. By using the model like a natural language reasoning engine, we attempt to generate **actions** from the semantics of the request.\n\nStructured Input & Output\n-------------------------\n\nWhen prompting models we typically use natural language but when building agents we need a way to “marshal” intent to and from our application memory. One common way to do this is using structured language that the model has been trained on. This is typically JSON, although other structured languages can also be compatible with many models.\n\nMemory\n------\n\nThe agent needs a way to track what has been done between each step. We can think of this like a “scratchpad” where the agent will take notes on what its done so far. This can be short-term memory (usually stateless) or long-term memory (stateful).\n\n**Workflows**\n-------------\n\nTo program and orchestrate the behavior of the agent with your application logic, a workflow is required. There are various types of workflows such as directed acyclic graphs (DAGs), finite state machines (FSM), and control flow graphs (CFG).\n\nHere is some general guidance for choosing the right workflow:\n\n*   **DAGs**: Suitable for programming a directed series of steps that don’t require backtracking or cycles.\n*   **FSMs**: Ideal when programming with a finite number of states, transitions, and actions without directed flow.\n*   **CFGs**: Best for programming a dynamic series of steps where conditions determine the flow, allowing for cycles and backtracking.\n\nIn this article, I will primarily cover FSMs as a way to program agentic workflows. However, different techniques can serve various purposes when implementing agents. The problem you’re trying to solve with your agent should guide the type of workflow you choose.\n\nNotable frameworks for building custom workflow orchestration include:\n\n*   [Haystack](https://haystack.deepset.ai/) — an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. Haystack focuses on building DAG’s. Example of retrieval augmented generation (RAG) as a DAG:\n\n![Image 28](https://miro.medium.com/v2/resize:fit:446/1*0RHeqTwsSGeIvJgnmCgqAg.png)\n\nSource [Haystack](https://docs.haystack.deepset.ai/docs/visualizing-pipelines)\n\n*   [LangGraph](https://langchain-ai.github.io/langgraph/) — a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Compared to other LLM frameworks, it offers these core benefits: cycles, controllability, and persistence. LangGraph allows you to define flows that involve cycles, essential for most agentic architectures, differentiating it from DAG-based solutions. LangGraph focuses on building CFGs. Example of agentic RAG with a cycle:\n\n![Image 29](https://miro.medium.com/v2/resize:fit:700/1*1yhnd3b7xsHjWk2YLuzqmA.png)\n\nSource [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_agentic_rag.ipynb)\n\n*   [assemble](https://github.com/alexsniffin/assemble) — an experimental framework written by me for building Agents through the use of an FSM.\n\nReAct Agent\n-----------\n\nThe ReAct agent specializes in reasoning and action handling within its environment.\n\nIn this pattern, we can implement different ReAct prompts as specific states in a FSM. This approach ensures that the agent’s responses are consistent and relevant to the current context or task at hand.\n\nEach state can represent various properties, including:\n\n*   a prompt for the model and,\n*   a handler for mapping application logic to and from the model\n\nThe main states used in ReAct are:\n\n*   Thought — addresses the problem given the previous actions taken and determines the next step to take.\n*   Act — determines the correct tool to use and the correct input for that tool.\n*   Observe — summarizes the behavior from the action to the memory.\n\n![Image 30](https://miro.medium.com/v2/resize:fit:652/1*LBcke9bluRWC537Y_CfjoQ.gif)\n\nSimple example of an FSM Agent\n\nThe benefits of implementing the agent this way are:\n\n*   predictability\n*   tasks are isolated from other states\n*   easy to troubleshoot\n*   easy to add new states\n\nPotential problems include:\n\n*   prone to getting stuck in loops\n*   can get side tracked or lose focus from the original request\n\nA simple FSM ReAct agent can be written in Python, for this example lets assume the LLM backend is implemented elsewhere and the agent has tools and memory.\n\nNotebook example of an FSM agent\n\nThe example uses a StockTicker price tool to get factual information on ticker prices. The agent can reason when the question is asking about a particular ticker and use the tool. It’s possible to add in additional tools to ask more complex questions. Each handler contains a prompt and the correct structured input and output parsing using [Pydantic](https://docs.pydantic.dev/latest/) to create JSON schemas.\n\nThis implementation isn’t complete but addresses a simple way to build this agent.\n\nAdditional improvements would be:\n\n*   to add [context-window](https://www.hopsworks.ai/dictionary/context-window-for-llms) awareness to the memory. If the tool output or memory grows too large, you would need to compress it. We can figure out the length of our memory by [tokenizing](https://sidsite.com/posts/bpe/) everything first to see whether the memory is too large. If it is, then you can do summarization, truncation or another technique to reduce the total tokens in the memory.\n*   adding control-flows for context cancellation or escaping from loops.\n\nOne of the advantages to implementing the agent with an FSM is that it isn’t limited to just ReAct states. Additional states can be defined for more complex behaviors. This pattern allows for a solid foundation and extensible basis to building agents.\n\nTask-Planner Agent\n------------------\n\nThe task planner is an agent which defines a concrete plan on what needs to be done and attempts to work through that plan in multiple steps. It’s an extension of the ReAct agent by introducing a planning step.\n\nThe plan will consist of tasks where each task is an isolated piece of work. In the below example, the task planner defines a set of tasks and will work through them one at a time.\n\n![Image 31](https://miro.medium.com/v2/resize:fit:542/1*KZYOxQUumADUT6medHzSZA.gif)\n\nSimple example of a Task-Planner Agent\n\nWe can test the planning prompt for generating tasks using the OpenAI playground with GPT 4 Turbo.\n\n![Image 32](https://miro.medium.com/v2/resize:fit:700/1*ck1KCa56AjV3VBAKmpBjAA.png)\n\nOpenAI Playground\n\nThe model is able to create isolated tasks on what might need to be done.\n\nLike the ReAct example, the design for this agent can use an FSM as the basis of its implementation. The planning step would occur as a new state and the action state would instead pop from the stack of tasks and observe the output from the tools.\n\nThe benefit of this pattern is that work is planned upfront rather than continuously like the ReAct agent. This defines intermediate steps early that can help reduce the chance of getting stuck in a loop, but it’s not guaranteed.\n\nThis also comes with some problems where the agent might initially make a mistake in the plan which might cause errors throughout the tasks and require backtracking and generating new tasks. There’s a chance tasks are impossible to solve like invalid tool usage which requires a new plan and starting over. This can be an expensive mistake, therefore planning should be limited to tasks which are easily predictable.\n\nThis type of prompting is similar to an early project that got popular called [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) which uses a task queue to breakdown the problem into small pieces of work. This was one of the first projects to implement agentic like workflows with language models.\n\nMulti-Agent Orchestration\n-------------------------\n\nWhen asking agents complex tasks, it’s often difficult to scale the behavior of the agent correctly. This is a limiting factor for a number reasons, such as the persona, too many types of actions or too many states on what the agent could do.\n\nOne approach to solving this problem is by separating responsibilities of the agent and introducing another reasoning step for communication with other agents.\n\nBy giving agents the ability to communicate, they can delegate work through orchestration of tasks. This approach is similar to a [delegation-like pattern](https://en.wikipedia.org/wiki/Delegation_pattern).\n\nRather than having a single agent that does everything, we can define agents that specialize in solving specific problems that also have different implementations.\n\nInstead of having the agent figure out who to communicate with, we can introduce an **orchestrator** that can both supervise and route between agents to get the best desired output based on the task.\n\n![Image 33](https://miro.medium.com/v2/resize:fit:536/1*qOfzg_oTtwJG5Kd6Rss8Zg.gif)\n\nExample of a communication with an orchestration agent\n\nBy separating and abstracting communication, agents don’t need to know how a task is solved.\n\nLike the previous examples, an orchestration step can be defined using the FSM and the previous prompting techniques.\n\nExamples of Multi-Agent Implementations\n---------------------------------------\n\nMulti-agent implementations have been growing popular in the community to better scale tasks.\n\nOne such project is [CrewAI](https://github.com/joaomdmoura/crewAI) where you can define the persona of your agents, their capabilities and then create a “crew” where the agents work together to solve the tasks.\n\nExample code from CrewAI:\n\nExample of building a crew with CrewAI",
  "publishedTime": "2024-03-14T03:05:32.916Z",
  "usage": {
    "tokens": 2928
  }
}
```
