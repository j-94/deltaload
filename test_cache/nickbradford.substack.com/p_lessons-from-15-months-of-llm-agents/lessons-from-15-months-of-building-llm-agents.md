---
title: Lessons from 15 months of building LLM agents
description: Or: What I want out of an LLM observability platform
url: https://nickbradford.substack.com/p/lessons-from-15-months-of-llm-agents
timestamp: 2025-01-20T15:53:10.766Z
domain: nickbradford.substack.com
path: p_lessons-from-15-months-of-llm-agents
---

# Lessons from 15 months of building LLM agents


Or: What I want out of an LLM observability platform


## Content

I’ve spent the past 15 months building LLM agents, currently [Ellipsis](https://www.ellipsis.dev/), a virtual software engineer. Previously, I worked on structured data extraction, codebase migrations, and text-to-SQL.

As a result, startups working on LLM observability/safety/reliability reach out to me several times per week to hear about my problems, so I’m consolidating my experience and advice here.

[![Image 14](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F517fa12e-aeb4-42b6-b85a-a9cc84cfc53f_1024x1024.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F517fa12e-aeb4-42b6-b85a-a9cc84cfc53f_1024x1024.png)

_\[GPT-4V\] Create me a picture: "building an AI agent" top-down, 8bit, laboratory. In the center is a robot on an operating table, dressed in a black business suit, but half complete. Scientists around are working on it. The color palette is dark, with deep purples and dramatic light. \[NB: two scientists appear to be decapitated.\]_

My workflow has looked remarkably similar across the varied LLM agents I’ve worked on.

Most of my day is spent running evals; everything else flows from this. Why?

*   **Prompts are brittle**. You add an extra space or remove a comma somewhere, and the LLM output may be completely different, i.e. degraded on an important use case.
    
*   **Small changes accumulate**: A single agent run might have dozens, hundreds, or thousands (!) of LLM calls, so the actual outputs of a small change must be verified empirically.
    
*   **All the normal reasons you have tests:** they’re great. Run the tests, tests pass, you ship. Ship ship ship.
    

How do evals work? There are two main kinds of evals:

*   **“Unit tests”**: Verify a small piece of the agent internals; for example, verify the agent calls a particular tool when it’s the obvious choice. Good for testing obscure scenarios. Easy to verify expected behavior.
    
*   “**Integration tests”:** a complicated scenario end to end. Much more valuable because it tells you “does it actually work”. It’s often hard to write assertions for these because the outcome is amorphous, such as an answer to an ambiguous question.
    

So, the big question:

Here are some ideas:

*   **Problem-specific heuristics**: Often the agent’s objective has some other characteristics you can use to check. If it was writing a SQL query: does the query execute? If it was writing code: does the code pass tests? If it was extracting data: are all the expected fields present?
    
*   **LLM self-evaluation:** great idea. But here’s the thing: any reasonably advanced agent includes a self-critique sub-agent that it will use internally. This means your agent (probably) produced something that already passed your best LLM tests. (If your tests are finding room for improvement, they should be part of your agent!).
    

Sadly, this just doesn’t cut it most of the time. There are too many degenerate edge cases. There’s only one solution I’ve found:

_**\*snapshot the outputs and read them manually\***_

This is a huge pain.

And if your tests check the exact outputs, they need to be \*exactly\* the same, so you’re going to need:

This is one of the first things I set up on a new agent project. A cache is needed for your evals to be:

*   **Deterministic**: you want to stay sane. GPT-4 is non-deterministic at temperature zero (due to [Sparse MoE](https://152334h.github.io/blog/non-determinism-in-gpt-4/)).
    
*   **Fast**: a roundtrip to OpenAI can take seconds or minutes, so an agent might run for minutes or even hours - a cache speeds this up by 100x.
    
*   **Cheap**: at [$0.06/1k input tokens](https://openai.com/pricing), a fully maxed-out call to GPT-4-32k costs $1.92 (up to $3.84 for large outputs). If you experiment with agents enough, you’ll find there are many ways to blow through $1k in a few minutes of experiments.
    

There are many caching providers out there, but I’ve always rolled my own (I did try [Helicone](https://www.helicone.ai/) and hit various issues). Why?

*   You do NOT want another service in between you and your LLM provider. LLM providers are unreliable enough as it is.
    
*   A cache is trivial to set up and maintain.
    

So, I’ve built the exact same thing for every LLM project I’ve been on: stable serialize the request =\> hash it to get a key =\> stuff in a key/value store. You can build your own in Postgres in minutes.

OK, you ran your evals (or a customer ran something in prod), and your agent produced some hot garbage. Time for the fun part.

Over time I find you get quite a good gut feeling for what your agent is (or should) be doing, just as with acclimating to a large new codebase or getting to know a literal human being.

Mostly, this comes from reading a LOT of:

I find good “normal” logging is even more valuable than fancy observability tools. The other AI engineers I know all agree: you spend a LOT of time poring over logs.

However much data you’re logging, it’s not enough, [even if you take into account](https://en.wikipedia.org/wiki/Hofstadter%27s_law) this blog post. (I promise I don’t work for DataDog and am not trying to convince you to [spend $65M/year on observability](https://blog.pragmaticengineer.com/datadog-65m-year-customer-mystery/#:~:text=Coinbase%20spent%20%2465M%20with,shared%20details%20of%20what%20happened.).)

In a complicated agent, the “root cause” of an issue is often in the agent’s tools or environment, not in the prompts itself. But sometimes the agent “just did something dumb”, and for that you’ll need:

You need a nice UI to view agent conversation histories. I use [PromptLayer](https://promptlayer.com/) - simple, fast, reliable. I’ve tried a few others and hit misc issues.

Some other platforms have agent-first UIs (LangSmith and W&B come to mind) - haven’t tried them because it just hasn’t been a priority to have a nice visualization, even with thousands of LLM calls in a single agent run.

From viewing the conversation history, you find the spot where the agent went off the rails, and you ask yourself, “what could I have changed about the prompt to get it to do the right thing?” For that, you’ll head into:

Most of the LLM request UIs seem to have one built-in now. If you prefer copy-pasting into a different tab, OpenAI has one, [Vercel built one](https://sdk.vercel.ai/) to compare different models, loads exist. This is super useful.

You play around in the playground a few minutes, you find a change that works (maybe changing the system prompt, maybe it’s adding a new tool), and now…

Full circle! You need to add a new eval, and then run all your old evals to make sure we didn’t hopelessly break all our other use cases (which happens far too often).

Everyone wants me to put my prompts in their database so I can change it in their UI. This makes sense for some products, such as if you have some simple chatbot and you want a PM to be able to tweak the prompt without having to touch any code.

For agents, it’s a complete non-starter:

*   Prompts must be in version control for your evals to be reliable
    
*   Agents are composed not of a single prompt, but dozens or hundreds of smaller prompts: various tools, sub-agents, and error-handling cases.
    

There are many cool libraries for building LLM agents, and if I only have 30 minutes to prototype something, they can be useful.

However, I’ve yet to find a real use case for them outside of demos. LLM agents are pre-paradigm with no killer apps (yet), and building abstractions for applications that don’t exist is quite difficult.

*   Customizations to your agent are always necessary.
    
*   The libraries have hooks in all the wrong places, and many simple behaviors are completely inexpressible.
    
*   Agents are just a while-loop; you can write your own in around as much time as it takes to learn the API of whatever library, and it’ll be far simpler and easier to customize.
    

For now, [the wrong abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) is far worse than no abstraction.

Here are some things I’d love:

*   **Fuzz testing**: prompt instability is a huge problem, and a constant cause for worry. Are all my prompts stuck in a super unstable local optima, which make changes extremely difficult? Try out hundreds of small variations and measure the variance in the results.
    
*   **Prompt optimization**: there’s now tons of literature on this.
    

*   **Auditor agent**: a first step would be “find the point in the conversation where things went wrong”, useful for long agents.
    
*   **\[Edit 2023-12-03\]** **Observability for** **Embeddings:** The use case is debugging RAG workflows and evaluating different embedding models. For example, [Nomic Atlas](https://www.nomic.ai/) has a great visualizer for exploring embedding spaces, but it’s meant for static datasets, not for production use cases.
    

For now, I think just like “great ML engineers spend a lot of time looking at their data”, AI engineers \[have to\] spend a lot of time reading agent logs and manually inspecting results.

If you are building something that would improve this workflow, [I would love to chat](https://www.nsbradford.com/).

_For more about working with LLMs, I recommend this blog series:_ [https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/)

A few people have asked about the desirability of determinism, and the assumptions inherent therein. The reason for determinism is rooted in agent reliability, with major exceptions:

\- building a product where you want high variance (like writing poems)

\- building in a pass@k-style architecture, where you generate many results and choose the best one

\- intrinsically unsolvable by agent (like requiring non-indexed data to answer)

I think "human in the loop" (or "agent in the loop") workflows will be around for many years yet, and the UX is the key, just as how ChatGPT was fundamentally a UX advance to make LLMs easy to interact with.

#### Discussion about this post

## Metadata

```json
{
  "title": "Lessons from 15 months of building LLM agents",
  "description": "Or: What I want out of an LLM observability platform",
  "url": "https://nickbradford.substack.com/p/lessons-from-15-months-of-llm-agents",
  "content": "I’ve spent the past 15 months building LLM agents, currently [Ellipsis](https://www.ellipsis.dev/), a virtual software engineer. Previously, I worked on structured data extraction, codebase migrations, and text-to-SQL.\n\nAs a result, startups working on LLM observability/safety/reliability reach out to me several times per week to hear about my problems, so I’m consolidating my experience and advice here.\n\n[![Image 14](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F517fa12e-aeb4-42b6-b85a-a9cc84cfc53f_1024x1024.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F517fa12e-aeb4-42b6-b85a-a9cc84cfc53f_1024x1024.png)\n\n_\\[GPT-4V\\] Create me a picture: \"building an AI agent\" top-down, 8bit, laboratory. In the center is a robot on an operating table, dressed in a black business suit, but half complete. Scientists around are working on it. The color palette is dark, with deep purples and dramatic light. \\[NB: two scientists appear to be decapitated.\\]_\n\nMy workflow has looked remarkably similar across the varied LLM agents I’ve worked on.\n\nMost of my day is spent running evals; everything else flows from this. Why?\n\n*   **Prompts are brittle**. You add an extra space or remove a comma somewhere, and the LLM output may be completely different, i.e. degraded on an important use case.\n    \n*   **Small changes accumulate**: A single agent run might have dozens, hundreds, or thousands (!) of LLM calls, so the actual outputs of a small change must be verified empirically.\n    \n*   **All the normal reasons you have tests:** they’re great. Run the tests, tests pass, you ship. Ship ship ship.\n    \n\nHow do evals work? There are two main kinds of evals:\n\n*   **“Unit tests”**: Verify a small piece of the agent internals; for example, verify the agent calls a particular tool when it’s the obvious choice. Good for testing obscure scenarios. Easy to verify expected behavior.\n    \n*   “**Integration tests”:** a complicated scenario end to end. Much more valuable because it tells you “does it actually work”. It’s often hard to write assertions for these because the outcome is amorphous, such as an answer to an ambiguous question.\n    \n\nSo, the big question:\n\nHere are some ideas:\n\n*   **Problem-specific heuristics**: Often the agent’s objective has some other characteristics you can use to check. If it was writing a SQL query: does the query execute? If it was writing code: does the code pass tests? If it was extracting data: are all the expected fields present?\n    \n*   **LLM self-evaluation:** great idea. But here’s the thing: any reasonably advanced agent includes a self-critique sub-agent that it will use internally. This means your agent (probably) produced something that already passed your best LLM tests. (If your tests are finding room for improvement, they should be part of your agent!).\n    \n\nSadly, this just doesn’t cut it most of the time. There are too many degenerate edge cases. There’s only one solution I’ve found:\n\n_**\\*snapshot the outputs and read them manually\\***_\n\nThis is a huge pain.\n\nAnd if your tests check the exact outputs, they need to be \\*exactly\\* the same, so you’re going to need:\n\nThis is one of the first things I set up on a new agent project. A cache is needed for your evals to be:\n\n*   **Deterministic**: you want to stay sane. GPT-4 is non-deterministic at temperature zero (due to [Sparse MoE](https://152334h.github.io/blog/non-determinism-in-gpt-4/)).\n    \n*   **Fast**: a roundtrip to OpenAI can take seconds or minutes, so an agent might run for minutes or even hours - a cache speeds this up by 100x.\n    \n*   **Cheap**: at [$0.06/1k input tokens](https://openai.com/pricing), a fully maxed-out call to GPT-4-32k costs $1.92 (up to $3.84 for large outputs). If you experiment with agents enough, you’ll find there are many ways to blow through $1k in a few minutes of experiments.\n    \n\nThere are many caching providers out there, but I’ve always rolled my own (I did try [Helicone](https://www.helicone.ai/) and hit various issues). Why?\n\n*   You do NOT want another service in between you and your LLM provider. LLM providers are unreliable enough as it is.\n    \n*   A cache is trivial to set up and maintain.\n    \n\nSo, I’ve built the exact same thing for every LLM project I’ve been on: stable serialize the request =\\> hash it to get a key =\\> stuff in a key/value store. You can build your own in Postgres in minutes.\n\nOK, you ran your evals (or a customer ran something in prod), and your agent produced some hot garbage. Time for the fun part.\n\nOver time I find you get quite a good gut feeling for what your agent is (or should) be doing, just as with acclimating to a large new codebase or getting to know a literal human being.\n\nMostly, this comes from reading a LOT of:\n\nI find good “normal” logging is even more valuable than fancy observability tools. The other AI engineers I know all agree: you spend a LOT of time poring over logs.\n\nHowever much data you’re logging, it’s not enough, [even if you take into account](https://en.wikipedia.org/wiki/Hofstadter%27s_law) this blog post. (I promise I don’t work for DataDog and am not trying to convince you to [spend $65M/year on observability](https://blog.pragmaticengineer.com/datadog-65m-year-customer-mystery/#:~:text=Coinbase%20spent%20%2465M%20with,shared%20details%20of%20what%20happened.).)\n\nIn a complicated agent, the “root cause” of an issue is often in the agent’s tools or environment, not in the prompts itself. But sometimes the agent “just did something dumb”, and for that you’ll need:\n\nYou need a nice UI to view agent conversation histories. I use [PromptLayer](https://promptlayer.com/) - simple, fast, reliable. I’ve tried a few others and hit misc issues.\n\nSome other platforms have agent-first UIs (LangSmith and W&B come to mind) - haven’t tried them because it just hasn’t been a priority to have a nice visualization, even with thousands of LLM calls in a single agent run.\n\nFrom viewing the conversation history, you find the spot where the agent went off the rails, and you ask yourself, “what could I have changed about the prompt to get it to do the right thing?” For that, you’ll head into:\n\nMost of the LLM request UIs seem to have one built-in now. If you prefer copy-pasting into a different tab, OpenAI has one, [Vercel built one](https://sdk.vercel.ai/) to compare different models, loads exist. This is super useful.\n\nYou play around in the playground a few minutes, you find a change that works (maybe changing the system prompt, maybe it’s adding a new tool), and now…\n\nFull circle! You need to add a new eval, and then run all your old evals to make sure we didn’t hopelessly break all our other use cases (which happens far too often).\n\nEveryone wants me to put my prompts in their database so I can change it in their UI. This makes sense for some products, such as if you have some simple chatbot and you want a PM to be able to tweak the prompt without having to touch any code.\n\nFor agents, it’s a complete non-starter:\n\n*   Prompts must be in version control for your evals to be reliable\n    \n*   Agents are composed not of a single prompt, but dozens or hundreds of smaller prompts: various tools, sub-agents, and error-handling cases.\n    \n\nThere are many cool libraries for building LLM agents, and if I only have 30 minutes to prototype something, they can be useful.\n\nHowever, I’ve yet to find a real use case for them outside of demos. LLM agents are pre-paradigm with no killer apps (yet), and building abstractions for applications that don’t exist is quite difficult.\n\n*   Customizations to your agent are always necessary.\n    \n*   The libraries have hooks in all the wrong places, and many simple behaviors are completely inexpressible.\n    \n*   Agents are just a while-loop; you can write your own in around as much time as it takes to learn the API of whatever library, and it’ll be far simpler and easier to customize.\n    \n\nFor now, [the wrong abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) is far worse than no abstraction.\n\nHere are some things I’d love:\n\n*   **Fuzz testing**: prompt instability is a huge problem, and a constant cause for worry. Are all my prompts stuck in a super unstable local optima, which make changes extremely difficult? Try out hundreds of small variations and measure the variance in the results.\n    \n*   **Prompt optimization**: there’s now tons of literature on this.\n    \n\n*   **Auditor agent**: a first step would be “find the point in the conversation where things went wrong”, useful for long agents.\n    \n*   **\\[Edit 2023-12-03\\]** **Observability for** **Embeddings:** The use case is debugging RAG workflows and evaluating different embedding models. For example, [Nomic Atlas](https://www.nomic.ai/) has a great visualizer for exploring embedding spaces, but it’s meant for static datasets, not for production use cases.\n    \n\nFor now, I think just like “great ML engineers spend a lot of time looking at their data”, AI engineers \\[have to\\] spend a lot of time reading agent logs and manually inspecting results.\n\nIf you are building something that would improve this workflow, [I would love to chat](https://www.nsbradford.com/).\n\n_For more about working with LLMs, I recommend this blog series:_ [https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/)\n\nA few people have asked about the desirability of determinism, and the assumptions inherent therein. The reason for determinism is rooted in agent reliability, with major exceptions:\n\n\\- building a product where you want high variance (like writing poems)\n\n\\- building in a pass@k-style architecture, where you generate many results and choose the best one\n\n\\- intrinsically unsolvable by agent (like requiring non-indexed data to answer)\n\nI think \"human in the loop\" (or \"agent in the loop\") workflows will be around for many years yet, and the UX is the key, just as how ChatGPT was fundamentally a UX advance to make LLMs easy to interact with.\n\n#### Discussion about this post",
  "publishedTime": "2023-12-16T18:09:31+00:00",
  "usage": {
    "tokens": 2524
  }
}
```
