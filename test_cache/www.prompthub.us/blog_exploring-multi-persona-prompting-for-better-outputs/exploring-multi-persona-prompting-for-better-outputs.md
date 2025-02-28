---
title: Exploring Multi-Persona Prompting for Better Outputs
description: See how a new prompting method can generate better results than standard and Chain of Thought (CoT) methods
url: https://www.prompthub.us/blog/exploring-multi-persona-prompting-for-better-outputs
timestamp: 2025-01-20T15:56:06.330Z
domain: www.prompthub.us
path: blog_exploring-multi-persona-prompting-for-better-outputs
---

# Exploring Multi-Persona Prompting for Better Outputs


See how a new prompting method can generate better results than standard and Chain of Thought (CoT) methods


## Content

Our friends over at [Synthminds](https://synthminds.ai/) shared an incredible study with us from the University of Illinois. The title is "Unleashing Cognitive Synergy In Large Language Models: A Task-Solving Agent Through Multi-Persona Self-Collaboration”. (You can check it out [here](https://arxiv.org/pdf/2307.05300.pdf)).

The study proposed a new method of prompt engineering that instructs the LLM to summon multiple personas and have them work together to solve a task. They call it solo performance prompting (SPP).

For example, if you asked the LLM to write an outline for a science fiction novel, this prompting method would generate a few persons, probably a novelist, a scientist, and maybe a nuclear physicist. These three personas would engage in active dialogue until they all agreed on the output.

I found this paper to be another interesting development in prompt engineering, with a technique you can implement today. I’m going to do my best to summarize the study. I'll delve into the specific experiments, explore the results, and provide insights on implementing this technique.

I would highly suggest reading the whole study but for those that don’t have time, let’s jump in.

### The multi-persona framework

We touched on what this framework is, so let’s jump in to how it works.

**How it works**

The Solo Performance Prompting (SPP) method involves identifying multiple personas that are helpful for the specific task. Each persona contributes their expertise and provides input on how to approach the task based on their experience They all brainstorm together.

Within this framework, one of the personas is the AI Assitant. They lead the group and the brainstorm.

What makes this process flexible is that the personas are dynamically determined based on the specific task at hand.

The study tested this framework in 3 expirments: Trivia Creative Writing, Codenames Collaborative, and Logic Grid Puzzle. These experiments range from knowledge-intensive tasks to reasoning-intensive tasks.

‍

![Image 25: Flow chart for standard prompting, Chain of thought prompting and solo performance prompting](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66bcb8583aa92a4b2a131e81_64b856cd5d59fd627bfcffde_Comparing%2520CoT%2520to%2520SPP.png)

Personas used in standard, CoT, and SPP prompting

‍

‍

![Image 26: prompt flow for standard prompting and SPP](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280af2a_64b8570246319e6c1d4c74e5_Standard%2520prompting%2520flow%2520vs%2520SPP%2520prompting%2520flow.png)

Prompt flow for standard prompting versus SPP

‍

**SPP Prompt Structure**

_Persona Identification_: Identify multiple participants with special personas (including a leader persona: AI Assistant)

_Beginning Remarks_: Each participant delivers beginning remarks. Providing suggestions or info on how to approach the task based on their own expertise.

_Multi-Persona Iterative Collaboration_: The leader persona, AI Assistant, proposes initial solutions, consults the other participants for feedback, and revises the answer iteratively.

System Principle: The first part of the prompt contains a high-level instruction: "When faced with a task, begin by identifying the participants who will contribute to solving the task. Then, initiate a multi-turn collaboration process until a final solution is reached. The participants will give critical comments and detailed suggestions whenever necessary."

The prompt includes two examples to showcase expected multi-persona behavior.

‍

You can access the prompt template in PromptHub ([here](https://app.prompthub.us/templates/100)) and try it out right away. We added two additional examples (one that included a code generation task), to make the prompt more robust.  
If you don't have PromptHub access but want to try it out, reply to the email that gets sent when you join the waitlist and I'll share an access code with you.

‍

![Image 27: Template page in PromptHub](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aef6_64b85935e61b5e6b2142f968_Multi-Persona%2520Template.png)

‍

### E**xperiment 1: Trivia**

The first expirment was a classic trivia test. It was conducted twice, once with 5 questions, once with 10 questions. We’d put this experiment in the ‘knowledge-intensive’ bucket.  
This experiment, along with all the others in this study, used [**GPT-4**](https://www.prompthub.us/models/gpt-4).

‍

Before diving into the results, let’s define the differnt prompting methods used.

**Standard -** Classic prompting. Just asking the model straight up, like ChatGPT.

[**Chain of Thought**](https://www.prompthub.us/blog/chain-of-thought-prompting-guide) **(CoT) -** Involves structuring the prompt in a way that guides the model through a series of reasoning steps to arrive at a final answer. For example:

*   Prompt: "Let's solve this problem step by step. First, we need to identify the key elements of the problem. The problem states that..."
*   The model generates a response, and the next step in the reasoning chain is introduced:
*   Prompt: "Great, now that we've identified the key elements, let's consider how they relate to each other..."
*   This process continues, with the prompt guiding the model through each step of the reasoning process.

**SPP-Profile** **\-** The personas are pre-determined

**SPP -** The personas are dynamically generated by the model

With that out of the way, let’s check out the results.

‍

![Image 28: Results from Trivia Experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aee0_64b85ab237c2d5bffbb400ce_Trivia%2520Results.png)

Results from the Trivia Experiment

‍

*   SPP outperformed CoT by 23% on the 10-question trivia test, which was surprising because CoT is often considered one of the best prompting methods.
*   Trivia requires knowledge from various areas. The results shows that SPP can be particularly helpful when a task requires diverse expertise.
*   Standard prompting outperformed CoT.
*   While CoT generated reasonable plans for solving the tasks, it often suffered from hallucinations or produced factually incorrect final outputs.
*   SPP won out over SPP-Profile. You could atrtibute this to a prompting best practice known as “giving the model room to think”. Allowing the model to generate the personas resulted in better persona selection and more correct answers.

‍

### E**xperiment 2: Codenames Collaborative**

The second experiment is based off the popular board game, Codenames. It involves a Spymaster and a Guesser. This task requires both knowledge and reasoning. If you haven’t heard of Codenames before, check out the example below.

‍

![Image 29: Codenames example input and output](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aedd_66ccac6d07cac738f48b363b_Multi%2520persona%2520prompting%2520codenames%2520example.png)

‍

‍

Let's take a look at the results

‍

![Image 30: Results from Codenames Experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aed3_64b933ed9c8880298a8e91b3_Codespaces%2520Results.png)

Results from Codenames experiment

What stands out?

*   SPP wins out again. Showing it can effectively perform tasks that require knowledge and reasoning tasks.
*   Standard prompting outperforms CoT again.
*   SPP’s full output (viewable in the study) shows SPP generates a highly detailed and impressive dialogue. This highlights the value of the multi-persona iterative collaboration process in SPP, where the leader persona consults the other participants for feedback and revises the answer iteratively.

‍

### E**xperiment 3: Logic Grid Puzzle**

The last experiment was a pure-reasoning intensive puzzle, that requires the model to solve complex puzzles. You can see what the puzzle looked like below.

![Image 31: Input and Output for the logic grid puzzle experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aeee_64b933b5299a9102617767cf_Logic%2520Grid%2520Input%253AOutput%2520Example.png)

Input and output for the logic grid puzzle experiment

Let’s take a look at the results.

‍

![Image 32: Results from the logic grid experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aed6_64b934533eb4a41608cb9df7_Logic%2520Puzzles%2520Results.png)

Results from the logic grid experiment

What stands out?

*   CoT finally (and significantly) outperformed standard prompting. This helps verify that CoT works better for reasoning-intensive tasks rather than knowledge-intensive tasks. .
*   SPP signigicantly outpeformed standard prompting, and beat out CoT. This was the biggest delta between SPP and standard.
*   SPP wins out over SPP-Profile again (more evidence for “giving the model room to think”)

‍

### SPP-Profile vs SPP

SPP outperformed SPP-Profile in each experiment. This indicates that the ability to dynamically identify and simluate different personas based on the specific task at hand is crucial.

But here’s the really interesting part.

The results showed that LLMs ([GPT-4](https://www.prompthub.us/models/gpt-4) was the model used in all the experiments) can effectively identify personas without additional fine-tuning. This is promising because it suggests that SPP can be used effectively without the need for any model customization.

‍

### Wrapping up

Prompt engineering is such a new field, and new methods are popping up everyday, with SPP being the latest. For those thinking about how you can leverage SPP in your prompts, here are my takeaways.

1.  **Enhanced Problem-solving**: SPP combines multiple personas to enhance problem-solving in complex tasks.
2.  **Knowledge and Reasoning**: SPP excels in both knowledge-intensive and reasoning-intensive tasks.
3.  **Collaborative Process**: SPP's iterative collaboration process with personas, generates accurate results through feedback and revision.
4.  **Flexible Persona Identification**: SPP dynamically identifies personas based on task inputs, adapting with no fine-tuning needed.

To make it easy to try this method out, we created a template based on the SPP prompt discussed in the article.

The template includes additional examples, including a code generation example. You can access and add the template to your prompt library [here](https://app.prompthub.us/templates/100).

‍

‍

## Metadata

```json
{
  "title": "Exploring Multi-Persona Prompting for Better Outputs",
  "description": "See how a new prompting method can generate better results than standard and Chain of Thought (CoT) methods",
  "url": "https://www.prompthub.us/blog/exploring-multi-persona-prompting-for-better-outputs",
  "content": "Our friends over at [Synthminds](https://synthminds.ai/) shared an incredible study with us from the University of Illinois. The title is \"Unleashing Cognitive Synergy In Large Language Models: A Task-Solving Agent Through Multi-Persona Self-Collaboration”. (You can check it out [here](https://arxiv.org/pdf/2307.05300.pdf)).\n\nThe study proposed a new method of prompt engineering that instructs the LLM to summon multiple personas and have them work together to solve a task. They call it solo performance prompting (SPP).\n\nFor example, if you asked the LLM to write an outline for a science fiction novel, this prompting method would generate a few persons, probably a novelist, a scientist, and maybe a nuclear physicist. These three personas would engage in active dialogue until they all agreed on the output.\n\nI found this paper to be another interesting development in prompt engineering, with a technique you can implement today. I’m going to do my best to summarize the study. I'll delve into the specific experiments, explore the results, and provide insights on implementing this technique.\n\nI would highly suggest reading the whole study but for those that don’t have time, let’s jump in.\n\n### The multi-persona framework\n\nWe touched on what this framework is, so let’s jump in to how it works.\n\n**How it works**\n\nThe Solo Performance Prompting (SPP) method involves identifying multiple personas that are helpful for the specific task. Each persona contributes their expertise and provides input on how to approach the task based on their experience They all brainstorm together.\n\nWithin this framework, one of the personas is the AI Assitant. They lead the group and the brainstorm.\n\nWhat makes this process flexible is that the personas are dynamically determined based on the specific task at hand.\n\nThe study tested this framework in 3 expirments: Trivia Creative Writing, Codenames Collaborative, and Logic Grid Puzzle. These experiments range from knowledge-intensive tasks to reasoning-intensive tasks.\n\n‍\n\n![Image 25: Flow chart for standard prompting, Chain of thought prompting and solo performance prompting](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66bcb8583aa92a4b2a131e81_64b856cd5d59fd627bfcffde_Comparing%2520CoT%2520to%2520SPP.png)\n\nPersonas used in standard, CoT, and SPP prompting\n\n‍\n\n‍\n\n![Image 26: prompt flow for standard prompting and SPP](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280af2a_64b8570246319e6c1d4c74e5_Standard%2520prompting%2520flow%2520vs%2520SPP%2520prompting%2520flow.png)\n\nPrompt flow for standard prompting versus SPP\n\n‍\n\n**SPP Prompt Structure**\n\n_Persona Identification_: Identify multiple participants with special personas (including a leader persona: AI Assistant)\n\n_Beginning Remarks_: Each participant delivers beginning remarks. Providing suggestions or info on how to approach the task based on their own expertise.\n\n_Multi-Persona Iterative Collaboration_: The leader persona, AI Assistant, proposes initial solutions, consults the other participants for feedback, and revises the answer iteratively.\n\nSystem Principle: The first part of the prompt contains a high-level instruction: \"When faced with a task, begin by identifying the participants who will contribute to solving the task. Then, initiate a multi-turn collaboration process until a final solution is reached. The participants will give critical comments and detailed suggestions whenever necessary.\"\n\nThe prompt includes two examples to showcase expected multi-persona behavior.\n\n‍\n\nYou can access the prompt template in PromptHub ([here](https://app.prompthub.us/templates/100)) and try it out right away. We added two additional examples (one that included a code generation task), to make the prompt more robust.  \nIf you don't have PromptHub access but want to try it out, reply to the email that gets sent when you join the waitlist and I'll share an access code with you.\n\n‍\n\n![Image 27: Template page in PromptHub](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aef6_64b85935e61b5e6b2142f968_Multi-Persona%2520Template.png)\n\n‍\n\n### E**xperiment 1: Trivia**\n\nThe first expirment was a classic trivia test. It was conducted twice, once with 5 questions, once with 10 questions. We’d put this experiment in the ‘knowledge-intensive’ bucket.  \nThis experiment, along with all the others in this study, used [**GPT-4**](https://www.prompthub.us/models/gpt-4).\n\n‍\n\nBefore diving into the results, let’s define the differnt prompting methods used.\n\n**Standard -** Classic prompting. Just asking the model straight up, like ChatGPT.\n\n[**Chain of Thought**](https://www.prompthub.us/blog/chain-of-thought-prompting-guide) **(CoT) -** Involves structuring the prompt in a way that guides the model through a series of reasoning steps to arrive at a final answer. For example:\n\n*   Prompt: \"Let's solve this problem step by step. First, we need to identify the key elements of the problem. The problem states that...\"\n*   The model generates a response, and the next step in the reasoning chain is introduced:\n*   Prompt: \"Great, now that we've identified the key elements, let's consider how they relate to each other...\"\n*   This process continues, with the prompt guiding the model through each step of the reasoning process.\n\n**SPP-Profile** **\\-** The personas are pre-determined\n\n**SPP -** The personas are dynamically generated by the model\n\nWith that out of the way, let’s check out the results.\n\n‍\n\n![Image 28: Results from Trivia Experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aee0_64b85ab237c2d5bffbb400ce_Trivia%2520Results.png)\n\nResults from the Trivia Experiment\n\n‍\n\n*   SPP outperformed CoT by 23% on the 10-question trivia test, which was surprising because CoT is often considered one of the best prompting methods.\n*   Trivia requires knowledge from various areas. The results shows that SPP can be particularly helpful when a task requires diverse expertise.\n*   Standard prompting outperformed CoT.\n*   While CoT generated reasonable plans for solving the tasks, it often suffered from hallucinations or produced factually incorrect final outputs.\n*   SPP won out over SPP-Profile. You could atrtibute this to a prompting best practice known as “giving the model room to think”. Allowing the model to generate the personas resulted in better persona selection and more correct answers.\n\n‍\n\n### E**xperiment 2: Codenames Collaborative**\n\nThe second experiment is based off the popular board game, Codenames. It involves a Spymaster and a Guesser. This task requires both knowledge and reasoning. If you haven’t heard of Codenames before, check out the example below.\n\n‍\n\n![Image 29: Codenames example input and output](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aedd_66ccac6d07cac738f48b363b_Multi%2520persona%2520prompting%2520codenames%2520example.png)\n\n‍\n\n‍\n\nLet's take a look at the results\n\n‍\n\n![Image 30: Results from Codenames Experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aed3_64b933ed9c8880298a8e91b3_Codespaces%2520Results.png)\n\nResults from Codenames experiment\n\nWhat stands out?\n\n*   SPP wins out again. Showing it can effectively perform tasks that require knowledge and reasoning tasks.\n*   Standard prompting outperforms CoT again.\n*   SPP’s full output (viewable in the study) shows SPP generates a highly detailed and impressive dialogue. This highlights the value of the multi-persona iterative collaboration process in SPP, where the leader persona consults the other participants for feedback and revises the answer iteratively.\n\n‍\n\n### E**xperiment 3: Logic Grid Puzzle**\n\nThe last experiment was a pure-reasoning intensive puzzle, that requires the model to solve complex puzzles. You can see what the puzzle looked like below.\n\n![Image 31: Input and Output for the logic grid puzzle experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aeee_64b933b5299a9102617767cf_Logic%2520Grid%2520Input%253AOutput%2520Example.png)\n\nInput and output for the logic grid puzzle experiment\n\nLet’s take a look at the results.\n\n‍\n\n![Image 32: Results from the logic grid experiment](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66ccac78d81a120d2280aed6_64b934533eb4a41608cb9df7_Logic%2520Puzzles%2520Results.png)\n\nResults from the logic grid experiment\n\nWhat stands out?\n\n*   CoT finally (and significantly) outperformed standard prompting. This helps verify that CoT works better for reasoning-intensive tasks rather than knowledge-intensive tasks. .\n*   SPP signigicantly outpeformed standard prompting, and beat out CoT. This was the biggest delta between SPP and standard.\n*   SPP wins out over SPP-Profile again (more evidence for “giving the model room to think”)\n\n‍\n\n### SPP-Profile vs SPP\n\nSPP outperformed SPP-Profile in each experiment. This indicates that the ability to dynamically identify and simluate different personas based on the specific task at hand is crucial.\n\nBut here’s the really interesting part.\n\nThe results showed that LLMs ([GPT-4](https://www.prompthub.us/models/gpt-4) was the model used in all the experiments) can effectively identify personas without additional fine-tuning. This is promising because it suggests that SPP can be used effectively without the need for any model customization.\n\n‍\n\n### Wrapping up\n\nPrompt engineering is such a new field, and new methods are popping up everyday, with SPP being the latest. For those thinking about how you can leverage SPP in your prompts, here are my takeaways.\n\n1.  **Enhanced Problem-solving**: SPP combines multiple personas to enhance problem-solving in complex tasks.\n2.  **Knowledge and Reasoning**: SPP excels in both knowledge-intensive and reasoning-intensive tasks.\n3.  **Collaborative Process**: SPP's iterative collaboration process with personas, generates accurate results through feedback and revision.\n4.  **Flexible Persona Identification**: SPP dynamically identifies personas based on task inputs, adapting with no fine-tuning needed.\n\nTo make it easy to try this method out, we created a template based on the SPP prompt discussed in the article.\n\nThe template includes additional examples, including a code generation example. You can access and add the template to your prompt library [here](https://app.prompthub.us/templates/100).\n\n‍\n\n‍",
  "publishedTime": "Jul 19, 2023T00:00:00-04:00",
  "usage": {
    "tokens": 2557
  }
}
```
