---
title: Continuous prompt optimization from DSPy core contributors | Zenbase AI
description: Zenbase automates prompt engineering and model selection so developers can focus on programming. We’re core team members of Stanford’s DSPy building the production version.
url: https://zenbase.ai/
timestamp: 2025-01-20T16:10:59.652Z
domain: zenbase.ai
path: root
---

# Continuous prompt optimization from DSPy core contributors | Zenbase AI


Zenbase automates prompt engineering and model selection so developers can focus on programming. We’re core team members of Stanford’s DSPy building the production version.


## Content

Continuous prompt optimization from DSPy core contributors | Zenbase AI
===============

[![Image 56: Launch](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors/upvote_embed.svg/)](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors)

[![Image 57: Launch](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors/upvote_embed.svg/)](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors)

Focus on programming, not prompting.
====================================

Focus on programming, not prompting.
====================================

Developer tools and cloud infrastructure for perfectionists using LLMs. Zenbase takes care of the hassle of prompt engineering and model selection.

Developer tools and cloud infrastructure for perfectionists using LLMs. Zenbase takes care of the hassle of prompt engineering and model selection.

[Code Examples](https://zenbase.ai/#code-examples)

[Get started](https://zenbase.ai/#get-started)

[Get started](https://zenbase.ai/#get-started)

![Image 58](https://framerusercontent.com/images/6SGnqyPBgV294hxz06Uw23oFwI.webp)

![Image 59](https://framerusercontent.com/images/6SGnqyPBgV294hxz06Uw23oFwI.webp)

![Image 60](https://framerusercontent.com/images/1YqJp6HvdkSPB8wxGFaHT8uAZ4.png)

![Image 61](https://framerusercontent.com/images/1YqJp6HvdkSPB8wxGFaHT8uAZ4.png)

[![Image 62](https://framerusercontent.com/images/BjbxD6JgnH7fgtOjApYgCVHrLc.png?scale-down-to=512)](https://zenbase.ai/)

[GitHub](https://github.com/zenbase-ai/core/tree/main/py)

[Schedule a demo](https://zenbase.typeform.com/early-access)

[![Image 63](https://framerusercontent.com/images/BjbxD6JgnH7fgtOjApYgCVHrLc.png?scale-down-to=512)](https://zenbase.ai/)

[![Image 64](https://framerusercontent.com/images/BjbxD6JgnH7fgtOjApYgCVHrLc.png?scale-down-to=512)](https://zenbase.ai/)

![Image 65](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

![Image 66](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

![Image 67](https://framerusercontent.com/images/C7SPJnVXLFJA9F7uBzrvXxLVqg.png)

![Image 68](https://framerusercontent.com/images/2fhVMek92q7YLgkzUz2efuyvMdM.png)

![Image 69](https://framerusercontent.com/images/C7SPJnVXLFJA9F7uBzrvXxLVqg.png)

![Image 70](https://framerusercontent.com/images/C7SPJnVXLFJA9F7uBzrvXxLVqg.png)

![Image 71](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

![Image 72](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

![Image 73](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

Mmmmm… code
-----------

Scaling  
Vibe Checks

Transaction  
Categorization

Notification  
Relevance

Styled  
Generation

RAG Query  
Generator

Reliable  
Tool Calls

Router with  
Latency Constraint

Entity Extraction  
with Latency Constraint

It's easier to know what looks good than it is to explain to an LLM how to grade what looks good. Zenbase's classifiers can be calibrated to that of a human reviewer, so that you can programmatically evaluate vibes at scale.

Typescript

Python

```
// 1. Create your classifier
const vibeCheck = zenbase.classifier({
	id: "vibeCheck",
	params: z.object({
		text: z.string()
	}),
	returns: z.boolean(),
})

// 2. Give it test cases
await vibeCheck.tests.add([
	{ params: { text: "..." }, returns: true },
	{ params: { text: "..." }, returns: false },
])

// 3. Train it
const { evals } = await vibeCheck.optimize()

// 4. Use it
const { data: isVibey } = await vibeCheck({
	text: `A towel, the guide says, is about the most massively useful thing an interstellar hitchhiker can have.`
})

// 5. Incorporate user feedback
const onUserFeedback = (text: string, isVibey: bool) =>
	vibeCheck.tests.add([
		{ params: { text }, returns: isVibey }
	])
```

Scaling  
Vibe Checks

Transaction  
Categorization

Notification  
Relevance

Styled  
Generation

RAG Query  
Generator

Reliable  
Tool Calls

Router with  
Latency Constraint

Entity Extraction  
with Latency Constraint

It's easier to know what looks good than it is to explain to an LLM how to grade what looks good. Zenbase's classifiers can be calibrated to that of a human reviewer, so that you can programmatically evaluate vibes at scale.

Typescript

Python

```
// 1. Create your classifier
const vibeCheck = zenbase.classifier({
	id: "vibeCheck",
	params: z.object({
		text: z.string()
	}),
	returns: z.boolean(),
})

// 2. Give it test cases
await vibeCheck.tests.add([
	{ params: { text: "..." }, returns: true },
	{ params: { text: "..." }, returns: false },
])

// 3. Train it
const { evals } = await vibeCheck.optimize()

// 4. Use it
const { data: isVibey } = await vibeCheck({
	text: `A towel, the guide says, is about the most massively useful thing an interstellar hitchhiker can have.`
})

// 5. Incorporate user feedback
const onUserFeedback = (text: string, isVibey: bool) =>
	vibeCheck.tests.add([
		{ params: { text }, returns: isVibey }
	])
```

Scaling  
Vibe Checks

Transaction  
Categorization

Notification  
Relevance

Styled  
Generation

RAG Query  
Generator

Reliable  
Tool Calls

Router with  
Latency Constraint

Entity Extraction  
with Latency Constraint

It's easier to know what looks good than it is to explain to an LLM how to grade what looks good. Zenbase's classifiers can be calibrated to that of a human reviewer, so that you can programmatically evaluate vibes at scale.

Typescript

Python

```
// 1. Create your classifier
const vibeCheck = zenbase.classifier({
	id: "vibeCheck",
	params: z.object({
		text: z.string()
	}),
	returns: z.boolean(),
})

// 2. Give it test cases
await vibeCheck.tests.add([
	{ params: { text: "..." }, returns: true },
	{ params: { text: "..." }, returns: false },
])

// 3. Train it
const { evals } = await vibeCheck.optimize()

// 4. Use it
const { data: isVibey } = await vibeCheck({
	text: `A towel, the guide says, is about the most massively useful thing an interstellar hitchhiker can have.`
})

// 5. Incorporate user feedback
const onUserFeedback = (text: string, isVibey: bool) =>
	vibeCheck.tests.add([
		{ params: { text }, returns: isVibey }
	])
```

Is it any good?
---------------

We develop custom optimization algorithms and leverage those developed by our fellow open source contributors at StanfordNLP/DSPy.

We develop custom optimization algorithms and leverage those developed by our fellow open source contributors at StanfordNLP/DSPy.

The Zenbase team has a unique combination of technical expertise and practical problem-solving skills. **Their work is both theoretically sound and aimed at solving the real challenges developers face.**

![Image 74](https://framerusercontent.com/images/74oAzcFFyucgtX8DuJlf2Qjg.png)

![Image 75](https://framerusercontent.com/images/74oAzcFFyucgtX8DuJlf2Qjg.png)

Omar Khattab

Omar

Researcher @ Databricks  
Creator of DSPy & ColBERT

Databricks,  
DSPy, ColBERT

I’ve seen a lot of AI Devtools and Zenbase is solving a problem that everyone building with AI will have when going to production. **The best part is their product is so easy to use that it’s a no brainer.**

![Image 76](https://framerusercontent.com/images/T3S0rHph966Qqchw2MgPIXc6v8.png)

![Image 77](https://framerusercontent.com/images/T3S0rHph966Qqchw2MgPIXc6v8.png)

Scott

CEO  
[Superfilter.ai](https://www.superfilter.ai/) (YC S24)

CEO[Superfilter.ai](https://www.superfilter.ai/) (YC S24)

We were staying up until 3am trying to go from demo to production. **Zenbase came into the trenches with us to improve our evals from 10% to 91.6%.** It really felt like they were a part of our team.

![Image 78](https://framerusercontent.com/images/3K6y8TXl5MIEMy8xxpvyExzNG8.png)

![Image 79](https://framerusercontent.com/images/3K6y8TXl5MIEMy8xxpvyExzNG8.png)

Taeib

Cofounder  
[Vera-Health.ai](https://vera-health.ai/) (YC S24)

DSPy's optimizers had **40%+ better accuracy and saved 18 engineer hours** on a classification task vs. an expert prompter using 49 prompting techniques.

![Image 80](https://framerusercontent.com/images/ENrFbTChPF90jJMq36XCyXINy0.jpg)

![Image 81](https://framerusercontent.com/images/ENrFbTChPF90jJMq36XCyXINy0.jpg)

Learn Prompting

Sponsored by OpenAI & Microsoft

Sponsored by  
OpenAI & Microsoft

Feel the Zen
------------

Declarative DX

Zenbase's AI functions let you focus on what you want, not how to prompt or which model to use.

AI that gets smarter all the time

AI that gets smarter with time

We automate the prompt engineering and fine-tuning so you don't have to figure it out.

Never get stuck prompt engineering again

We'll find the best prompt and model to maximize coverage of your test cases.

[Get started](https://zenbase.ai/#get-started)

[Get started](https://zenbase.ai/#get-started)

Your Zen
--------

Masters
-------

Mains
-----

![Image 82](https://framerusercontent.com/images/3hz23xf39zkNslAnJz0CL7htDtY.jpg)

![Image 83](https://framerusercontent.com/images/3hz23xf39zkNslAnJz0CL7htDtY.jpg)

#### Cyrus Nouroozi

Founder & CEO

• Core Contributor @ DSPy  
• UWaterloo Systems Design Eng

• Core Contributor @ DSPy  
• Honorary Researcher @  
Nous Research  
• UWaterloo Systems Design

#### Amir Mehr

Founder & CTO

• Core Contributor @ DSPy

• Core Contributor @ DSPy  
• M.Sc. of CS @ UCalgary

• M.Sc. of CS @ UCalgary

![Image 84](https://framerusercontent.com/images/knNCfjP3xP6XzHqjZAJe1pXEQo.png)

![Image 85](https://framerusercontent.com/images/knNCfjP3xP6XzHqjZAJe1pXEQo.png)

##### Supported by angels from

![Image 86](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)

![Image 87](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)

![Image 88](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)

![Image 89](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)

![Image 90](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)

![Image 91](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)

![Image 92](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)

![Image 93](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)

![Image 94](https://framerusercontent.com/images/Qa1t9BWvW6ZYnfRO46WyjExkQfw.png)

![Image 95](https://framerusercontent.com/images/Qa1t9BWvW6ZYnfRO46WyjExkQfw.png)

![Image 96](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)

![Image 97](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)

![Image 98](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)

![Image 99](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)

![Image 100](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)

![Image 101](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)

![Image 102](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)

![Image 103](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)

![Image 104](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

![Image 105](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

![Image 106](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

![Image 107](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)

Find your Zen
-------------

Open Source

##### Free Forever

Optimize your existing pipelines

Integrates with your eval tooling

Manual control

Complete control over prompts

MIT License

[GitHub](https://github.com/zenbase-ai/core)

[GitHub](https://github.com/zenbase-ai/core)

Startup

##### Starts at $1000/month

Hosted API

Continual Optimization

Dedicated Slack Channel

Custom Evaluators

[Schedule a demo](https://zenbase.typeform.com/early-access)

[Schedule a demo](https://zenbase.typeform.com/early-access)

Enterprise

##### Contact Us

SOCII / HIPAA

On-prem deployment

Dedicated Slack Channel

Custom Optimizers

[Contact us](https://zenbase.typeform.com/early-access)

[Contact us](https://zenbase.typeform.com/early-access)

#### Join the waitlist for our self-serve API

#### Join the waitlist for our self-serve API

#### FAQ

You asked, we answered.

How do you find the best prompt & model?

We use AI to continuously experiment with prompts and models to figure out the most effective way to execute your function. We use algorithms developed in-house and those researched by our team at DSPy. Automated prompt engineering combined with expert prompting regularly leads to double digit percentage improvements over expert prompting alone.

Do you offer an on-premise solution / SOCII / HIPAA?

Can we start with a small POC and adopt Zenbase incrementally?

Can I export the prompt & model?

#### FAQ

You asked, we answered.

How do you find the best prompt & model?

Do you offer an on-premise solution / SOCII / HIPAA?

Can we start with a small POC and adopt Zenbase incrementally?

Can I export the prompt & model?

![Image 108](https://framerusercontent.com/images/NVRianiZNBN7MvixizmwH79MmM.png?scale-down-to=512)

[Schedule a demo](https://zenbase.typeform.com/early-access)

Made with ❤️   
in San Francisco 🇺🇸   
and Edmonton 🇨🇦.

Copyright 2024 Zenbase AI Inc.

[](https://github.com/zenbase-ai)[](https://www.linkedin.com/company/zenbase-ai/)

![Image 109](https://framerusercontent.com/images/NVRianiZNBN7MvixizmwH79MmM.png?scale-down-to=512)

[Schedule a demo](https://zenbase.typeform.com/early-access)

Made with ❤️   
in San Francisco 🇺🇸   
and Edmonton 🇨🇦.

Copyright 2024 Zenbase AI Inc.

[](https://github.com/zenbase-ai)[](https://www.linkedin.com/company/zenbase-ai/)

![Image 110](https://framerusercontent.com/images/NVRianiZNBN7MvixizmwH79MmM.png?scale-down-to=512)

[Schedule a demo](https://zenbase.typeform.com/early-access)

Made with ❤️   
in San Francisco 🇺🇸   
and Edmonton 🇨🇦.

Copyright 2024 Zenbase AI Inc.

[](https://github.com/zenbase-ai)[](https://www.linkedin.com/company/zenbase-ai/)

## Metadata

```json
{
  "title": "Continuous prompt optimization from DSPy core contributors | Zenbase AI",
  "description": "Zenbase automates prompt engineering and model selection so developers can focus on programming. We’re core team members of Stanford’s DSPy building the production version.",
  "url": "https://zenbase.ai/",
  "content": "Continuous prompt optimization from DSPy core contributors | Zenbase AI\n===============\n\n[![Image 56: Launch](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors/upvote_embed.svg/)](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors)\n\n[![Image 57: Launch](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors/upvote_embed.svg/)](https://www.ycombinator.com/launches/Lmp-zenbase-continuous-prompt-optimization-by-dspy-core-contributors)\n\nFocus on programming, not prompting.\n====================================\n\nFocus on programming, not prompting.\n====================================\n\nDeveloper tools and cloud infrastructure for perfectionists using LLMs. Zenbase takes care of the hassle of prompt engineering and model selection.\n\nDeveloper tools and cloud infrastructure for perfectionists using LLMs. Zenbase takes care of the hassle of prompt engineering and model selection.\n\n[Code Examples](https://zenbase.ai/#code-examples)\n\n[Get started](https://zenbase.ai/#get-started)\n\n[Get started](https://zenbase.ai/#get-started)\n\n![Image 58](https://framerusercontent.com/images/6SGnqyPBgV294hxz06Uw23oFwI.webp)\n\n![Image 59](https://framerusercontent.com/images/6SGnqyPBgV294hxz06Uw23oFwI.webp)\n\n![Image 60](https://framerusercontent.com/images/1YqJp6HvdkSPB8wxGFaHT8uAZ4.png)\n\n![Image 61](https://framerusercontent.com/images/1YqJp6HvdkSPB8wxGFaHT8uAZ4.png)\n\n[![Image 62](https://framerusercontent.com/images/BjbxD6JgnH7fgtOjApYgCVHrLc.png?scale-down-to=512)](https://zenbase.ai/)\n\n[GitHub](https://github.com/zenbase-ai/core/tree/main/py)\n\n[Schedule a demo](https://zenbase.typeform.com/early-access)\n\n[![Image 63](https://framerusercontent.com/images/BjbxD6JgnH7fgtOjApYgCVHrLc.png?scale-down-to=512)](https://zenbase.ai/)\n\n[![Image 64](https://framerusercontent.com/images/BjbxD6JgnH7fgtOjApYgCVHrLc.png?scale-down-to=512)](https://zenbase.ai/)\n\n![Image 65](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\n![Image 66](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\n![Image 67](https://framerusercontent.com/images/C7SPJnVXLFJA9F7uBzrvXxLVqg.png)\n\n![Image 68](https://framerusercontent.com/images/2fhVMek92q7YLgkzUz2efuyvMdM.png)\n\n![Image 69](https://framerusercontent.com/images/C7SPJnVXLFJA9F7uBzrvXxLVqg.png)\n\n![Image 70](https://framerusercontent.com/images/C7SPJnVXLFJA9F7uBzrvXxLVqg.png)\n\n![Image 71](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\n![Image 72](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\n![Image 73](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\nMmmmm… code\n-----------\n\nScaling  \nVibe Checks\n\nTransaction  \nCategorization\n\nNotification  \nRelevance\n\nStyled  \nGeneration\n\nRAG Query  \nGenerator\n\nReliable  \nTool Calls\n\nRouter with  \nLatency Constraint\n\nEntity Extraction  \nwith Latency Constraint\n\nIt's easier to know what looks good than it is to explain to an LLM how to grade what looks good. Zenbase's classifiers can be calibrated to that of a human reviewer, so that you can programmatically evaluate vibes at scale.\n\nTypescript\n\nPython\n\n```\n// 1. Create your classifier\nconst vibeCheck = zenbase.classifier({\n\tid: \"vibeCheck\",\n\tparams: z.object({\n\t\ttext: z.string()\n\t}),\n\treturns: z.boolean(),\n})\n\n// 2. Give it test cases\nawait vibeCheck.tests.add([\n\t{ params: { text: \"...\" }, returns: true },\n\t{ params: { text: \"...\" }, returns: false },\n])\n\n// 3. Train it\nconst { evals } = await vibeCheck.optimize()\n\n// 4. Use it\nconst { data: isVibey } = await vibeCheck({\n\ttext: `A towel, the guide says, is about the most massively useful thing an interstellar hitchhiker can have.`\n})\n\n// 5. Incorporate user feedback\nconst onUserFeedback = (text: string, isVibey: bool) =>\n\tvibeCheck.tests.add([\n\t\t{ params: { text }, returns: isVibey }\n\t])\n```\n\nScaling  \nVibe Checks\n\nTransaction  \nCategorization\n\nNotification  \nRelevance\n\nStyled  \nGeneration\n\nRAG Query  \nGenerator\n\nReliable  \nTool Calls\n\nRouter with  \nLatency Constraint\n\nEntity Extraction  \nwith Latency Constraint\n\nIt's easier to know what looks good than it is to explain to an LLM how to grade what looks good. Zenbase's classifiers can be calibrated to that of a human reviewer, so that you can programmatically evaluate vibes at scale.\n\nTypescript\n\nPython\n\n```\n// 1. Create your classifier\nconst vibeCheck = zenbase.classifier({\n\tid: \"vibeCheck\",\n\tparams: z.object({\n\t\ttext: z.string()\n\t}),\n\treturns: z.boolean(),\n})\n\n// 2. Give it test cases\nawait vibeCheck.tests.add([\n\t{ params: { text: \"...\" }, returns: true },\n\t{ params: { text: \"...\" }, returns: false },\n])\n\n// 3. Train it\nconst { evals } = await vibeCheck.optimize()\n\n// 4. Use it\nconst { data: isVibey } = await vibeCheck({\n\ttext: `A towel, the guide says, is about the most massively useful thing an interstellar hitchhiker can have.`\n})\n\n// 5. Incorporate user feedback\nconst onUserFeedback = (text: string, isVibey: bool) =>\n\tvibeCheck.tests.add([\n\t\t{ params: { text }, returns: isVibey }\n\t])\n```\n\nScaling  \nVibe Checks\n\nTransaction  \nCategorization\n\nNotification  \nRelevance\n\nStyled  \nGeneration\n\nRAG Query  \nGenerator\n\nReliable  \nTool Calls\n\nRouter with  \nLatency Constraint\n\nEntity Extraction  \nwith Latency Constraint\n\nIt's easier to know what looks good than it is to explain to an LLM how to grade what looks good. Zenbase's classifiers can be calibrated to that of a human reviewer, so that you can programmatically evaluate vibes at scale.\n\nTypescript\n\nPython\n\n```\n// 1. Create your classifier\nconst vibeCheck = zenbase.classifier({\n\tid: \"vibeCheck\",\n\tparams: z.object({\n\t\ttext: z.string()\n\t}),\n\treturns: z.boolean(),\n})\n\n// 2. Give it test cases\nawait vibeCheck.tests.add([\n\t{ params: { text: \"...\" }, returns: true },\n\t{ params: { text: \"...\" }, returns: false },\n])\n\n// 3. Train it\nconst { evals } = await vibeCheck.optimize()\n\n// 4. Use it\nconst { data: isVibey } = await vibeCheck({\n\ttext: `A towel, the guide says, is about the most massively useful thing an interstellar hitchhiker can have.`\n})\n\n// 5. Incorporate user feedback\nconst onUserFeedback = (text: string, isVibey: bool) =>\n\tvibeCheck.tests.add([\n\t\t{ params: { text }, returns: isVibey }\n\t])\n```\n\nIs it any good?\n---------------\n\nWe develop custom optimization algorithms and leverage those developed by our fellow open source contributors at StanfordNLP/DSPy.\n\nWe develop custom optimization algorithms and leverage those developed by our fellow open source contributors at StanfordNLP/DSPy.\n\nThe Zenbase team has a unique combination of technical expertise and practical problem-solving skills. **Their work is both theoretically sound and aimed at solving the real challenges developers face.**\n\n![Image 74](https://framerusercontent.com/images/74oAzcFFyucgtX8DuJlf2Qjg.png)\n\n![Image 75](https://framerusercontent.com/images/74oAzcFFyucgtX8DuJlf2Qjg.png)\n\nOmar Khattab\n\nOmar\n\nResearcher @ Databricks  \nCreator of DSPy & ColBERT\n\nDatabricks,  \nDSPy, ColBERT\n\nI’ve seen a lot of AI Devtools and Zenbase is solving a problem that everyone building with AI will have when going to production. **The best part is their product is so easy to use that it’s a no brainer.**\n\n![Image 76](https://framerusercontent.com/images/T3S0rHph966Qqchw2MgPIXc6v8.png)\n\n![Image 77](https://framerusercontent.com/images/T3S0rHph966Qqchw2MgPIXc6v8.png)\n\nScott\n\nCEO  \n[Superfilter.ai](https://www.superfilter.ai/) (YC S24)\n\nCEO[Superfilter.ai](https://www.superfilter.ai/) (YC S24)\n\nWe were staying up until 3am trying to go from demo to production. **Zenbase came into the trenches with us to improve our evals from 10% to 91.6%.** It really felt like they were a part of our team.\n\n![Image 78](https://framerusercontent.com/images/3K6y8TXl5MIEMy8xxpvyExzNG8.png)\n\n![Image 79](https://framerusercontent.com/images/3K6y8TXl5MIEMy8xxpvyExzNG8.png)\n\nTaeib\n\nCofounder  \n[Vera-Health.ai](https://vera-health.ai/) (YC S24)\n\nDSPy's optimizers had **40%+ better accuracy and saved 18 engineer hours** on a classification task vs. an expert prompter using 49 prompting techniques.\n\n![Image 80](https://framerusercontent.com/images/ENrFbTChPF90jJMq36XCyXINy0.jpg)\n\n![Image 81](https://framerusercontent.com/images/ENrFbTChPF90jJMq36XCyXINy0.jpg)\n\nLearn Prompting\n\nSponsored by OpenAI & Microsoft\n\nSponsored by  \nOpenAI & Microsoft\n\nFeel the Zen\n------------\n\nDeclarative DX\n\nZenbase's AI functions let you focus on what you want, not how to prompt or which model to use.\n\nAI that gets smarter all the time\n\nAI that gets smarter with time\n\nWe automate the prompt engineering and fine-tuning so you don't have to figure it out.\n\nNever get stuck prompt engineering again\n\nWe'll find the best prompt and model to maximize coverage of your test cases.\n\n[Get started](https://zenbase.ai/#get-started)\n\n[Get started](https://zenbase.ai/#get-started)\n\nYour Zen\n--------\n\nMasters\n-------\n\nMains\n-----\n\n![Image 82](https://framerusercontent.com/images/3hz23xf39zkNslAnJz0CL7htDtY.jpg)\n\n![Image 83](https://framerusercontent.com/images/3hz23xf39zkNslAnJz0CL7htDtY.jpg)\n\n#### Cyrus Nouroozi\n\nFounder & CEO\n\n• Core Contributor @ DSPy  \n• UWaterloo Systems Design Eng\n\n• Core Contributor @ DSPy  \n• Honorary Researcher @  \nNous Research  \n• UWaterloo Systems Design\n\n#### Amir Mehr\n\nFounder & CTO\n\n• Core Contributor @ DSPy\n\n• Core Contributor @ DSPy  \n• M.Sc. of CS @ UCalgary\n\n• M.Sc. of CS @ UCalgary\n\n![Image 84](https://framerusercontent.com/images/knNCfjP3xP6XzHqjZAJe1pXEQo.png)\n\n![Image 85](https://framerusercontent.com/images/knNCfjP3xP6XzHqjZAJe1pXEQo.png)\n\n##### Supported by angels from\n\n![Image 86](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)\n\n![Image 87](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)\n\n![Image 88](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)\n\n![Image 89](https://framerusercontent.com/images/FduW42mW3zNopiaZ5D2aiCUXj4.png?scale-down-to=1024)\n\n![Image 90](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)\n\n![Image 91](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)\n\n![Image 92](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)\n\n![Image 93](https://framerusercontent.com/images/I6CHr1QyRHE1StVyQjZb4FM.png?scale-down-to=512)\n\n![Image 94](https://framerusercontent.com/images/Qa1t9BWvW6ZYnfRO46WyjExkQfw.png)\n\n![Image 95](https://framerusercontent.com/images/Qa1t9BWvW6ZYnfRO46WyjExkQfw.png)\n\n![Image 96](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)\n\n![Image 97](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)\n\n![Image 98](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)\n\n![Image 99](https://framerusercontent.com/images/2YyB7Kp57Bk6YWwTiSxy59ExQ4.png?scale-down-to=2048)\n\n![Image 100](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)\n\n![Image 101](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)\n\n![Image 102](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)\n\n![Image 103](https://framerusercontent.com/images/ersFObK2q8MSHqyAG9Odfy9BqFM.png?scale-down-to=512)\n\n![Image 104](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\n![Image 105](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\n![Image 106](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\n![Image 107](https://framerusercontent.com/images/1keC13saAdCdbrzT4m2VfrIsg.png?scale-down-to=1024)\n\nFind your Zen\n-------------\n\nOpen Source\n\n##### Free Forever\n\nOptimize your existing pipelines\n\nIntegrates with your eval tooling\n\nManual control\n\nComplete control over prompts\n\nMIT License\n\n[GitHub](https://github.com/zenbase-ai/core)\n\n[GitHub](https://github.com/zenbase-ai/core)\n\nStartup\n\n##### Starts at $1000/month\n\nHosted API\n\nContinual Optimization\n\nDedicated Slack Channel\n\nCustom Evaluators\n\n[Schedule a demo](https://zenbase.typeform.com/early-access)\n\n[Schedule a demo](https://zenbase.typeform.com/early-access)\n\nEnterprise\n\n##### Contact Us\n\nSOCII / HIPAA\n\nOn-prem deployment\n\nDedicated Slack Channel\n\nCustom Optimizers\n\n[Contact us](https://zenbase.typeform.com/early-access)\n\n[Contact us](https://zenbase.typeform.com/early-access)\n\n#### Join the waitlist for our self-serve API\n\n#### Join the waitlist for our self-serve API\n\n#### FAQ\n\nYou asked, we answered.\n\nHow do you find the best prompt & model?\n\nWe use AI to continuously experiment with prompts and models to figure out the most effective way to execute your function. We use algorithms developed in-house and those researched by our team at DSPy. Automated prompt engineering combined with expert prompting regularly leads to double digit percentage improvements over expert prompting alone.\n\nDo you offer an on-premise solution / SOCII / HIPAA?\n\nCan we start with a small POC and adopt Zenbase incrementally?\n\nCan I export the prompt & model?\n\n#### FAQ\n\nYou asked, we answered.\n\nHow do you find the best prompt & model?\n\nDo you offer an on-premise solution / SOCII / HIPAA?\n\nCan we start with a small POC and adopt Zenbase incrementally?\n\nCan I export the prompt & model?\n\n![Image 108](https://framerusercontent.com/images/NVRianiZNBN7MvixizmwH79MmM.png?scale-down-to=512)\n\n[Schedule a demo](https://zenbase.typeform.com/early-access)\n\nMade with ❤️   \nin San Francisco 🇺🇸   \nand Edmonton 🇨🇦.\n\nCopyright 2024 Zenbase AI Inc.\n\n[](https://github.com/zenbase-ai)[](https://www.linkedin.com/company/zenbase-ai/)\n\n![Image 109](https://framerusercontent.com/images/NVRianiZNBN7MvixizmwH79MmM.png?scale-down-to=512)\n\n[Schedule a demo](https://zenbase.typeform.com/early-access)\n\nMade with ❤️   \nin San Francisco 🇺🇸   \nand Edmonton 🇨🇦.\n\nCopyright 2024 Zenbase AI Inc.\n\n[](https://github.com/zenbase-ai)[](https://www.linkedin.com/company/zenbase-ai/)\n\n![Image 110](https://framerusercontent.com/images/NVRianiZNBN7MvixizmwH79MmM.png?scale-down-to=512)\n\n[Schedule a demo](https://zenbase.typeform.com/early-access)\n\nMade with ❤️   \nin San Francisco 🇺🇸   \nand Edmonton 🇨🇦.\n\nCopyright 2024 Zenbase AI Inc.\n\n[](https://github.com/zenbase-ai)[](https://www.linkedin.com/company/zenbase-ai/)",
  "usage": {
    "tokens": 4433
  }
}
```
