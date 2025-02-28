---
title: Scoring & Ranking Prompts - PromptLayer
description: 
url: https://docs.promptlayer.com/why-promptlayer/evaluation-and-ranking
timestamp: 2025-01-20T15:53:17.899Z
domain: docs.promptlayer.com
path: why-promptlayer_evaluation-and-ranking
---

# Scoring & Ranking Prompts - PromptLayer



## Content

One of the biggest challenges in prompt engineering is understanding if Prompt A performs better than Prompt B. PromptLayer helps you solve this.

Testing in development can only get you so far. We believe the best way to understand your prompts is by analyzing them in production.

Below are some ways you can use PromptLayer to answer the following key questions:

*   How much does PromptA vs PromptB cost?
*   How often is PromptA used?
*   Is PromptA working better than PromptB?
*   Which prompts are receiving the most negative user feedback?
*   How do I synthetically evaluate my prompts using LLMs?

A/B Testing
-----------

PromptLayer is best used as an orchestration & data layer of your prompts.

That means [A/B testing](https://docs.promptlayer.com/why-promptlayer/ab-releases) is easy. Use the [Prompt Registry](https://docs.promptlayer.com/features/prompt-registry) to version templates build different tests and automatically segment versions using [dynamic release labels](https://docs.promptlayer.com/features/prompt-registry/dynamic-release-labels).

_Every PromptLayer request can have multiple “Scores”. A score is an integer from 0-100._

In PromptLayer, ranking is based on Score values. Scores can be updated via the UI or programmatically, allowing for the creation of named or unnamed scores. For further details, refer to the provided documentation on prompt history, metadata, and request IDs. The three most common ways to Score to rank your prompts are:

1.  **User feedback**: Present a 👍 and 👎 to your users after the completion. A user press of one of those buttons fills in a score of \[100, 0\] respectively.
    
2.  **RLHF**: Use our visual dashboard to fill in scores by hand. You can then use this data to decide between prompt templates or to fine-tune.
    
3.  **Synthetic Evaluation**: Use LLMs to score LLMs. After getting a completion, run an evaluation prompt on it and translate that to a score \[0, 100\].
    
    For example, your prompt could be:
    

Analytics
---------

After populating Scores as described above, navigate to the Prompt Template page to see how each template stacks up.

Pricing
-------

We live in the real world, so money matters. Building a prod LLM system means managing price. Some LLMs are cheaper than other LLMs. Some prompts are cheaper than other prompts.

Each request history page will tell you its individual cost:

You can also see the lifetime cost of a template in the Prompt Registry template page.

## Metadata

```json
{
  "title": "Scoring & Ranking Prompts - PromptLayer",
  "description": "",
  "url": "https://docs.promptlayer.com/why-promptlayer/evaluation-and-ranking",
  "content": "One of the biggest challenges in prompt engineering is understanding if Prompt A performs better than Prompt B. PromptLayer helps you solve this.\n\nTesting in development can only get you so far. We believe the best way to understand your prompts is by analyzing them in production.\n\nBelow are some ways you can use PromptLayer to answer the following key questions:\n\n*   How much does PromptA vs PromptB cost?\n*   How often is PromptA used?\n*   Is PromptA working better than PromptB?\n*   Which prompts are receiving the most negative user feedback?\n*   How do I synthetically evaluate my prompts using LLMs?\n\nA/B Testing\n-----------\n\nPromptLayer is best used as an orchestration & data layer of your prompts.\n\nThat means [A/B testing](https://docs.promptlayer.com/why-promptlayer/ab-releases) is easy. Use the [Prompt Registry](https://docs.promptlayer.com/features/prompt-registry) to version templates build different tests and automatically segment versions using [dynamic release labels](https://docs.promptlayer.com/features/prompt-registry/dynamic-release-labels).\n\n_Every PromptLayer request can have multiple “Scores”. A score is an integer from 0-100._\n\nIn PromptLayer, ranking is based on Score values. Scores can be updated via the UI or programmatically, allowing for the creation of named or unnamed scores. For further details, refer to the provided documentation on prompt history, metadata, and request IDs. The three most common ways to Score to rank your prompts are:\n\n1.  **User feedback**: Present a 👍 and 👎 to your users after the completion. A user press of one of those buttons fills in a score of \\[100, 0\\] respectively.\n    \n2.  **RLHF**: Use our visual dashboard to fill in scores by hand. You can then use this data to decide between prompt templates or to fine-tune.\n    \n3.  **Synthetic Evaluation**: Use LLMs to score LLMs. After getting a completion, run an evaluation prompt on it and translate that to a score \\[0, 100\\].\n    \n    For example, your prompt could be:\n    \n\nAnalytics\n---------\n\nAfter populating Scores as described above, navigate to the Prompt Template page to see how each template stacks up.\n\nPricing\n-------\n\nWe live in the real world, so money matters. Building a prod LLM system means managing price. Some LLMs are cheaper than other LLMs. Some prompts are cheaper than other prompts.\n\nEach request history page will tell you its individual cost:\n\nYou can also see the lifetime cost of a template in the Prompt Registry template page.",
  "usage": {
    "tokens": 546
  }
}
```
