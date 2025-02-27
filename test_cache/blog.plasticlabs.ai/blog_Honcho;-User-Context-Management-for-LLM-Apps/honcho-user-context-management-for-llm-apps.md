---
title: Honcho: User Context Management for LLM Apps
description: The missing piece of the stack TL;DR Today we drop the first release of a project called Honcho, an open-source version of the OpenAI Assistants API.
url: https://blog.plasticlabs.ai/blog/Honcho;-User-Context-Management-for-LLM-Apps
timestamp: 2025-01-20T15:58:52.590Z
domain: blog.plasticlabs.ai
path: blog_Honcho;-User-Context-Management-for-LLM-Apps
---

# Honcho: User Context Management for LLM Apps


The missing piece of the stack TL;DR Today we drop the first release of a project called Honcho, an open-source version of the OpenAI Assistants API.


## Content

![Image 13](https://blog.plasticlabs.ai/assets/missing_piece.png) _The missing piece of the stack_

TL;DR
-----

Today we drop the first release of a project called [_Honcho_](https://github.com/plastic-labs/honcho/tree/main), an open-source version of the OpenAI Assistants API. Honcho manages your AI app data on a per-user basis, allowing for multiple concurrent sessions. Glaringly absent from the existing stack, Honcho will, at full maturity, usher the advent of atomic, disposable agents that are user-first by default.

Plastic Lore
------------

[Plastic Labs](https://plasticlabs.ai/) was conceived as a research group exploring the intersection of education and emerging technology. Our first cycle focused on how the incentive mechanisms and data availability made possible by distributed ledgers might be harnessed to improve learning outcomes. But with the advent of ChatGPT and a chorus of armchair educators proclaiming tutoring solved by the first nascent consumer generative AI, we shifted our focus to large language models.

As a team with with backgrounds in both machine learning and education, we found the prevailing narratives overestimating short-term capabilities and under-imagining longterm potential. Fundamentally, LLMs were and still are 1-to-many instructors. Yes, they herald the beginning of a revolution in personal access not to be discounted, but every student is still ultimately getting the same experience. And homogenized educational paradigms are by definition under-performant on an individual level. If we stop here, we're selling ourselves short.

![Image 14](https://blog.plasticlabs.ai/assets/zombie_tutor_prompt.jpg) _A well intentioned but monstrously deterministic [tutor prompt](https://www.oneusefulthing.org/p/assigning-ai-seven-ways-of-using)._

Most edtech projects we saw emerging actually made foundation models worse by adding gratuitous lobotomization and coercing deterministic behavior. The former stemmed from the typical misalignments plaguing edtech, like the separation of user and payer. The latter seemed to originate with deep misunderstandings around what LLMs are and continues to translate to a huge missed opportunities.

So we set out to build a non-skeuomorphic, AI-native tutor that put users first. The same indeterminism so often viewed as LLMs' greatest liability is in fact their greatest strength. Really, it's what they _are_. When great teachers deliver effective personalized instruction, they don't consult some M.Ed flowchart, they leverage the internal personal context they have on the student and reason (consciously or basally) about the best pedagogical intervention. LLMs are the beginning of this kind of high-touch learning companion being _synthetically_ possible.

![Image 15](https://blog.plasticlabs.ai/assets/teacher_shoggoth.png) _We're not so different after all ([@anthrupad](https://twitter.com/anthrupad))._

Our [experimental tutor](https://blog.plasticlabs.ai/blog/Open-Sourcing-Tutor-GPT), Bloom, [was remarkably effective](https://blog.plasticlabs.ai/blog/Theory-of-Mind-Is-All-You-Need)\--for thousands of users during the 9 months we hosted it for free--precisely because we built [cognitive architectures](https://blog.langchain.dev/openais-bet-on-a-cognitive-architecture/) that mimic the theory-of-mind expertise of highly efficacious 1:1 instructors.

Context Failure Mode
--------------------

But we quickly ran up against a hard limitation. The failure mode we believe all vertical specific AI applications will eventually hit if they want to be sticky, paradigmatically different than their deterministic counterparts, and realize the latent potential. That's context, specifically user context--Bloom didn't know enough about each student.

We're consistently blown away by how many people don't realize large language models themselves are stateless. They don't remember shit about you. They're just translating context they're given into probable sequences of tokens. LLMs are like horoscope writers, good at crafting general statements that _feel_ very personal. You would be too, if you'd ingested and compressed that much of the written human corpus.

![Image 16](https://blog.plasticlabs.ai/assets/geeked_dory.png)

There are lots of developer tricks to give the illusion of state about the user, mostly injecting conversation history or some personal digital artifact into the context window. Another is running inference on that limited recent user context to derive new insights. This was the game changer for our tutor, and we still can't believe by how under-explored that solution space is (more on this soon 👀).

To date, machine learning has been [far more focused on](https://blog.plasticlabs.ai/notes/Machine-learning-is-fixated-on-task-performance) optimizing for general task competition than personalization. This is natural, although many of these tasks are still probably better suited to deterministic code. It's also historically prestiged papers over products--research takes bit to morph into tangible utility. Put these together and you end up with a big blindspot over individual users and what they want.

The real magic of 1:1 instruction isn't subject matter expertise. Bloom and the foundation models it leveraged had plenty of that (despite what clickbait media would have you believe about hallucination in LLMs). Instead, it's personal context. Good teachers and tutors get to know their charges--their history, beliefs, values, aesthetics, knowledge, preferences, hopes, fears, interests, etc. They compress all that and generate customized instruction, emergent effects of which are the relationships and culture necessary for positive feedback loops.

> Human intelligent agency depends more on the intricate sphere of ideas and the cultural intellect that we have grown over thousands of years than on the quirks of our biological brains. The minds of modern humans have more in common with chatGPT than with humans 10000 years ago.
> 
> — Joscha Bach (@Plinz) [December 14, 2023](https://twitter.com/Plinz/status/1735427295937020177?ref_src=twsrc%5Etfw)

Large language models can be good at this too. With similar compression and generation abilities, they're uniquely suited (among existing technology) to get to know you. We really can have shared culture and relationships with LLMs, absent (if we like) any cringy anthropomorphism.

Bloom needed a mechanism to harvest and utilize more context about the student. So we built it one.

Research Solutions
------------------

Prediction algorithms have become phenomenal at hacking attention using tabular engagement and activity data. But if we're thinking LLM-natively, a few questions emerge:

1.  How are LLMs uniquely positioned to understand users?
2.  What new affordances does this enable for modeling users?
3.  Can that improve agent design, DX, & UX?
4.  Does this enable more positive sum user data opportunities?

Every day human brains do incredibly sophisticated things with sorta-pejoratively labelled 'soft' insights about others. But social cognition is part of the same evolutionarily optimized framework we use to model the rest of the world.

We run continuous active inference on wetware to refine our internal world models. This helps us make better predictions about our experience by minimizing the difference between our expectation and reality. That's more or less what learning is. And we use the same set of mechanisms to model other humans, i.e. get to know them.

In LLMs we have remarkable predictive reasoning engines with which we can begin to build the foundations of social cognition and therefore model users with much more nuance and granularity. Not just their logged behavior, but reasoning between the lines about its motivation and grounding in the full account of their identity.

Late last year we published a [research pre-print on this topic](https://arxiv.org/abs/2310.06983), and we've shown that these kinds of biologically-inspired frameworks can construct models of users that improve an LLM's ability to reason and make predictions about that individual user:

![Image 17](https://blog.plasticlabs.ai/assets/honcho_powered_bloom_paper_fig.png) _A [predictive coding inspired metacognitive architecture](https://youtu.be/PbuzqCdY0hg?feature=shared), from our research._

We added it to Bloom and found the missing piece to overcoming the failure mode of user context. Our tutor could now learn about the student and use that knowledge effectively to produce better learning outcomes.

Blast Horizon
-------------

Building and maintaining a production-grade AI app for learning catapulted us to this missing part of the stack. Lots of users, all growing in unique ways, all needing personalized attention that evolved over multiple longform sessions, forced us to confront the user context management problem with all it's thorny intricacy and potential.

And we're hearing constantly from builders of other vertical specific AI apps that personalization is the key blocker. In order for projects to graduate form toys to tools, they need to create new kinds of magic for their users. Mountains of mostly static software exists to help accomplish an unfathomable range of tasks and lots of it can be personalized using traditional (albeit laborious for the user) methods. But LLMs can observe, reason, then generate the software _and the user context_, all abstracted away behind the scenes.

Imagine online stores generated just in time for the home improvement project you're working on; generative games with rich multimodality unfolding to fit your mood on the fly; travel agents that know itinerary needs specific to your family, without being explicitly told; copilots that think and write and code not just like you, _but as you_; disposable, atomic agents with full personal context that replace your professional services--_you_ with a law, medical, accounting degree.

This is the kind of future we can build when we put users at the center of our agent and LLM app production.

Introducing Honcho
------------------

So today we're releasing the first iteration of [Honcho](https://blog.plasticlabs.ai/notes/Honcho-name-lore), our project to re-define LLM application development through user context management. At this nascent stage, you can think of it as an open-source version of the OpenAI Assistants API.

Honcho is a REST API that defines a storage schema to seamlessly manage your application's data on a per-user basis. It ships with a Python SDK which [you can read more about how to use here](https://github.com/plastic-labs/honcho/blob/main/README.md).

![Image 18](https://blog.plasticlabs.ai/assets/honcho-basic-user-context-management-blog-post-diagram.png)

We spent lots of time building the infrastructure to support multiple concurrent users with Bloom, and too often we see developers running into the same problem: building a fantastic demo, sharing it with the world, then inevitably taking it down because of infrastructure/scaling issues.

Honcho allows you to deploy an application with a single command that can automatically handle concurrent users. Speedrunning to production is now only limited by the amount of spend you can handle, not tedious infrastructure setup.

Managing app data on a per-user basis is the first small step in improving how devs build LLM apps. Once you define a data management schema on a per-user basis, a lots of new possibilities emerge around what you can do intra-user message, intra-user sessions, and even intra-user sessions across an ecosystem of agents.

Get Involved
------------

We're excited to see builders experiment with what we're releasing today, and with Honcho as it continues to evolve.

Check out the [GitHub repo](https://github.com/plastic-labs/honcho) to get started and join our [Discord](https://discord.gg/plasticlabs) to stay up to date 🫡.

## Metadata

```json
{
  "title": "Honcho: User Context Management for LLM Apps",
  "description": "The missing piece of the stack TL;DR Today we drop the first release of a project called Honcho, an open-source version of the OpenAI Assistants API.",
  "url": "https://blog.plasticlabs.ai/blog/Honcho;-User-Context-Management-for-LLM-Apps",
  "content": "![Image 13](https://blog.plasticlabs.ai/assets/missing_piece.png) _The missing piece of the stack_\n\nTL;DR\n-----\n\nToday we drop the first release of a project called [_Honcho_](https://github.com/plastic-labs/honcho/tree/main), an open-source version of the OpenAI Assistants API. Honcho manages your AI app data on a per-user basis, allowing for multiple concurrent sessions. Glaringly absent from the existing stack, Honcho will, at full maturity, usher the advent of atomic, disposable agents that are user-first by default.\n\nPlastic Lore\n------------\n\n[Plastic Labs](https://plasticlabs.ai/) was conceived as a research group exploring the intersection of education and emerging technology. Our first cycle focused on how the incentive mechanisms and data availability made possible by distributed ledgers might be harnessed to improve learning outcomes. But with the advent of ChatGPT and a chorus of armchair educators proclaiming tutoring solved by the first nascent consumer generative AI, we shifted our focus to large language models.\n\nAs a team with with backgrounds in both machine learning and education, we found the prevailing narratives overestimating short-term capabilities and under-imagining longterm potential. Fundamentally, LLMs were and still are 1-to-many instructors. Yes, they herald the beginning of a revolution in personal access not to be discounted, but every student is still ultimately getting the same experience. And homogenized educational paradigms are by definition under-performant on an individual level. If we stop here, we're selling ourselves short.\n\n![Image 14](https://blog.plasticlabs.ai/assets/zombie_tutor_prompt.jpg) _A well intentioned but monstrously deterministic [tutor prompt](https://www.oneusefulthing.org/p/assigning-ai-seven-ways-of-using)._\n\nMost edtech projects we saw emerging actually made foundation models worse by adding gratuitous lobotomization and coercing deterministic behavior. The former stemmed from the typical misalignments plaguing edtech, like the separation of user and payer. The latter seemed to originate with deep misunderstandings around what LLMs are and continues to translate to a huge missed opportunities.\n\nSo we set out to build a non-skeuomorphic, AI-native tutor that put users first. The same indeterminism so often viewed as LLMs' greatest liability is in fact their greatest strength. Really, it's what they _are_. When great teachers deliver effective personalized instruction, they don't consult some M.Ed flowchart, they leverage the internal personal context they have on the student and reason (consciously or basally) about the best pedagogical intervention. LLMs are the beginning of this kind of high-touch learning companion being _synthetically_ possible.\n\n![Image 15](https://blog.plasticlabs.ai/assets/teacher_shoggoth.png) _We're not so different after all ([@anthrupad](https://twitter.com/anthrupad))._\n\nOur [experimental tutor](https://blog.plasticlabs.ai/blog/Open-Sourcing-Tutor-GPT), Bloom, [was remarkably effective](https://blog.plasticlabs.ai/blog/Theory-of-Mind-Is-All-You-Need)\\--for thousands of users during the 9 months we hosted it for free--precisely because we built [cognitive architectures](https://blog.langchain.dev/openais-bet-on-a-cognitive-architecture/) that mimic the theory-of-mind expertise of highly efficacious 1:1 instructors.\n\nContext Failure Mode\n--------------------\n\nBut we quickly ran up against a hard limitation. The failure mode we believe all vertical specific AI applications will eventually hit if they want to be sticky, paradigmatically different than their deterministic counterparts, and realize the latent potential. That's context, specifically user context--Bloom didn't know enough about each student.\n\nWe're consistently blown away by how many people don't realize large language models themselves are stateless. They don't remember shit about you. They're just translating context they're given into probable sequences of tokens. LLMs are like horoscope writers, good at crafting general statements that _feel_ very personal. You would be too, if you'd ingested and compressed that much of the written human corpus.\n\n![Image 16](https://blog.plasticlabs.ai/assets/geeked_dory.png)\n\nThere are lots of developer tricks to give the illusion of state about the user, mostly injecting conversation history or some personal digital artifact into the context window. Another is running inference on that limited recent user context to derive new insights. This was the game changer for our tutor, and we still can't believe by how under-explored that solution space is (more on this soon 👀).\n\nTo date, machine learning has been [far more focused on](https://blog.plasticlabs.ai/notes/Machine-learning-is-fixated-on-task-performance) optimizing for general task competition than personalization. This is natural, although many of these tasks are still probably better suited to deterministic code. It's also historically prestiged papers over products--research takes bit to morph into tangible utility. Put these together and you end up with a big blindspot over individual users and what they want.\n\nThe real magic of 1:1 instruction isn't subject matter expertise. Bloom and the foundation models it leveraged had plenty of that (despite what clickbait media would have you believe about hallucination in LLMs). Instead, it's personal context. Good teachers and tutors get to know their charges--their history, beliefs, values, aesthetics, knowledge, preferences, hopes, fears, interests, etc. They compress all that and generate customized instruction, emergent effects of which are the relationships and culture necessary for positive feedback loops.\n\n> Human intelligent agency depends more on the intricate sphere of ideas and the cultural intellect that we have grown over thousands of years than on the quirks of our biological brains. The minds of modern humans have more in common with chatGPT than with humans 10000 years ago.\n> \n> — Joscha Bach (@Plinz) [December 14, 2023](https://twitter.com/Plinz/status/1735427295937020177?ref_src=twsrc%5Etfw)\n\nLarge language models can be good at this too. With similar compression and generation abilities, they're uniquely suited (among existing technology) to get to know you. We really can have shared culture and relationships with LLMs, absent (if we like) any cringy anthropomorphism.\n\nBloom needed a mechanism to harvest and utilize more context about the student. So we built it one.\n\nResearch Solutions\n------------------\n\nPrediction algorithms have become phenomenal at hacking attention using tabular engagement and activity data. But if we're thinking LLM-natively, a few questions emerge:\n\n1.  How are LLMs uniquely positioned to understand users?\n2.  What new affordances does this enable for modeling users?\n3.  Can that improve agent design, DX, & UX?\n4.  Does this enable more positive sum user data opportunities?\n\nEvery day human brains do incredibly sophisticated things with sorta-pejoratively labelled 'soft' insights about others. But social cognition is part of the same evolutionarily optimized framework we use to model the rest of the world.\n\nWe run continuous active inference on wetware to refine our internal world models. This helps us make better predictions about our experience by minimizing the difference between our expectation and reality. That's more or less what learning is. And we use the same set of mechanisms to model other humans, i.e. get to know them.\n\nIn LLMs we have remarkable predictive reasoning engines with which we can begin to build the foundations of social cognition and therefore model users with much more nuance and granularity. Not just their logged behavior, but reasoning between the lines about its motivation and grounding in the full account of their identity.\n\nLate last year we published a [research pre-print on this topic](https://arxiv.org/abs/2310.06983), and we've shown that these kinds of biologically-inspired frameworks can construct models of users that improve an LLM's ability to reason and make predictions about that individual user:\n\n![Image 17](https://blog.plasticlabs.ai/assets/honcho_powered_bloom_paper_fig.png) _A [predictive coding inspired metacognitive architecture](https://youtu.be/PbuzqCdY0hg?feature=shared), from our research._\n\nWe added it to Bloom and found the missing piece to overcoming the failure mode of user context. Our tutor could now learn about the student and use that knowledge effectively to produce better learning outcomes.\n\nBlast Horizon\n-------------\n\nBuilding and maintaining a production-grade AI app for learning catapulted us to this missing part of the stack. Lots of users, all growing in unique ways, all needing personalized attention that evolved over multiple longform sessions, forced us to confront the user context management problem with all it's thorny intricacy and potential.\n\nAnd we're hearing constantly from builders of other vertical specific AI apps that personalization is the key blocker. In order for projects to graduate form toys to tools, they need to create new kinds of magic for their users. Mountains of mostly static software exists to help accomplish an unfathomable range of tasks and lots of it can be personalized using traditional (albeit laborious for the user) methods. But LLMs can observe, reason, then generate the software _and the user context_, all abstracted away behind the scenes.\n\nImagine online stores generated just in time for the home improvement project you're working on; generative games with rich multimodality unfolding to fit your mood on the fly; travel agents that know itinerary needs specific to your family, without being explicitly told; copilots that think and write and code not just like you, _but as you_; disposable, atomic agents with full personal context that replace your professional services--_you_ with a law, medical, accounting degree.\n\nThis is the kind of future we can build when we put users at the center of our agent and LLM app production.\n\nIntroducing Honcho\n------------------\n\nSo today we're releasing the first iteration of [Honcho](https://blog.plasticlabs.ai/notes/Honcho-name-lore), our project to re-define LLM application development through user context management. At this nascent stage, you can think of it as an open-source version of the OpenAI Assistants API.\n\nHoncho is a REST API that defines a storage schema to seamlessly manage your application's data on a per-user basis. It ships with a Python SDK which [you can read more about how to use here](https://github.com/plastic-labs/honcho/blob/main/README.md).\n\n![Image 18](https://blog.plasticlabs.ai/assets/honcho-basic-user-context-management-blog-post-diagram.png)\n\nWe spent lots of time building the infrastructure to support multiple concurrent users with Bloom, and too often we see developers running into the same problem: building a fantastic demo, sharing it with the world, then inevitably taking it down because of infrastructure/scaling issues.\n\nHoncho allows you to deploy an application with a single command that can automatically handle concurrent users. Speedrunning to production is now only limited by the amount of spend you can handle, not tedious infrastructure setup.\n\nManaging app data on a per-user basis is the first small step in improving how devs build LLM apps. Once you define a data management schema on a per-user basis, a lots of new possibilities emerge around what you can do intra-user message, intra-user sessions, and even intra-user sessions across an ecosystem of agents.\n\nGet Involved\n------------\n\nWe're excited to see builders experiment with what we're releasing today, and with Honcho as it continues to evolve.\n\nCheck out the [GitHub repo](https://github.com/plastic-labs/honcho) to get started and join our [Discord](https://discord.gg/plasticlabs) to stay up to date 🫡.",
  "usage": {
    "tokens": 2482
  }
}
```
