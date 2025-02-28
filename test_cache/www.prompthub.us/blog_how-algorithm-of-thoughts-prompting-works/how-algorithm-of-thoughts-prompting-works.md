---
title: How Algorithm of Thoughts Prompting Works
description: Leveraging algorithmic thinking in prompts. How Algorithm of Thoughts is outperforming top prompting engineering methods, with less complexity
url: https://www.prompthub.us/blog/how-algorithm-of-thoughts-prompting-works
timestamp: 2025-01-20T15:43:58.866Z
domain: www.prompthub.us
path: blog_how-algorithm-of-thoughts-prompting-works
---

# How Algorithm of Thoughts Prompting Works


Leveraging algorithmic thinking in prompts. How Algorithm of Thoughts is outperforming top prompting engineering methods, with less complexity


## Content

‍

Some prompt engineering techniques are simple and easy to implement (like ["According to.."](https://www.prompthub.us/blog/improve-accuracy-and-reduce-hallucinations-with-a-simple-prompting-technique) prompting). Some are extremely powerful, but require a more advanced setup with many more API calls, leading to increased costs and latency (like [Tree of Thoughts](https://www.prompthub.us/blog/how-tree-of-thoughts-prompting-works)).

Researchers at Virginia Tech and Microsoft have recently developed a new method that stands up against the Tree of Thoughts methhod with a remarkable reduction of 100 times fewer queries needed. Yes, you read that correctly — 100 times fewer queries. (link to the full paper [here](https://arxiv.org/pdf/2308.10379.pdf))

Enter, **Algorithm of Thoughts (AoT)**.

‍

![Image 21: Model inputs and outputs for various prompting methods](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c3e_64f0bbd70ba6f2bd63e02543_Algorithm%2520of%2520Thought%2520Compared%2520to%2520Other%2520Methods.png)

‍

What is Algorithm of Thoughts prompting?
----------------------------------------

Algorithm of Thoughts (AoT) is a prompting engineering method designed to mimic algorithmic thinking in large language models (LLMs). It breaks down tasks into defined sub-steps like defining the problem, gathering and analyzing information, formulating a hypothesis, testing it, and coming to a final conclusion.

‍

Why Algorithm of Thoughts?
--------------------------

Large Language Models (LLMs) are extremely powerful, but they aren’t perfect. Prompt engineering exists because consistently getting high-quality outputs isn’t a walk in the park.

Many of the top-performing, and widely adopted methods are computationally heavy. For example, the Tree of Thoughts (ToT) method requires multiple rounds of querying as it traverses dozens of branches and nodes.

Designed to address these challenges, Algorithm of Thoughts presents a structured path of reasoning for LLMs. It's a solution that delivers on efficiency without compromising on the quality of outputs.

‍

![Image 22: Flowcharts for different prompting methods. ](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c33_64f0bd12f412735fc67e92c0_Prompt%2520flows%2520for%2520different%2520prompting%2520methods.png)

Prompt flow for different methods

How Algorithm of Thought promptingworks
---------------------------------------

Algorithm of Thoughts is designed to mimic algorithmic thinking. It is broken down into a few steps:

1.  **Define the Problem:** Algorithm of Thoughts begins by clearly stating the problem behind the query or task.
2.  **Gather Information:** Before diving into solutions, Algorithm of Thoughts prompts the LLM to get the necessary context.
3.  **Analyze the Information:** Next, the LLM breaks down the gathered information, identifying patterns, relationships, or anomalies.
4.  **Formulate a Hypothesis:** Based on the analysis, the LLM puts together an initial solution.
5.  **Test the Hypothesis:** The LLM then thinks of ways to validate or refute its hypothesis, envisioning potential outcomes.
6.  **Draw Conclusions:** After testing, the LLM summarizes its findings, providing a refined solution to the initial problem.
7.  **Reflect:** Lastly, the LLM considers the broader implications of its conclusion, thinking of potential next steps or further questions.

Algorithm of Thoughts 'structured approach ensures the LLM isn’t left to wander aimlessly down many paths.

Algorithm of Thoughts prompt template
-------------------------------------

The Algorithm of Thoughts prompt technique isn’t the easiest to implement, but we’ve done our best to make it plug and play. Generally you want to follow this structure:

‍

‍

Here’s a practical example if you were using Algorithm of Thoughts to do research on the environmental implications of data centers.

1.  **Problem Statement:** What are the environmental implications of increased data center usage?
2.  **Background Information:** Data centers account for about 1% of global electricity use.
3.  **Initial Hypothesis:** Implementing renewable energy sources can mitigate the environmental impact.
4.  **Reasoning:** Evaluate the feasibility and impact of using renewable energy for data centers.
5.  **Conclusion:** Based on the analysis, is renewable energy a viable solution for data centers?

You could then restructure that into something a little more LLM-friendly.

"Given that data centers account for about 1% of global electricity use, what are the environmental implications of increased data center usage? I hypothesize that implementing renewable energy sources can mitigate the environmental impact. Can you evaluate the feasibility and impact of using renewable energy for data centers? Based on your analysis, is renewable energy a viable solution for data centers?”

‍  
We built a template in PromptHub that converts a normal prompt into a new prompt, following the Algorithm of Thoughts framework. You can access the template [here](https://app.prompthub.us/templates/292) and try it out right away.

‍  
If you don't have PromptHub access but want to try it out, reply to the email that gets sent when you join the waitlist and I'll share an access code with you.

‍

![Image 23: Screenshot of the Algorithm of Thoughts Template in the PromptHub platform](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17cac_64f5e0a5323df832a2a2925e_AoT%2520Screenshot.png)

‍

### **Experiments: Game of 24**

**Setup**

The researchers pulled 100 rounds of the Game of 24 from [4nums.com](http://4nums.com/). For a game of 24 to be considered successful, it must use the four given numbers to get to a final answer of 24 using only basic arithmetic operations.

**Baselines**

Standard prompting and [Chain of Thought](https://www.prompthub.us/blog/chain-of-thought-prompting-guide) (CoT) were evaluated under a 5-shot framework. Tree of Thoughts (ToT) was implement with a breadth of 5.

For Algorithm of Thoughts the same 5-shot framework was used as in standard prompting. These methods were sampled 100 times, with the average success rates being documented.

[GPT-4](https://www.prompthub.us/models/gpt-4) was the only model used, and the temperature was set to 0.

**Algorithm of Thoughts prompt example**

Here is the full version of the Algorithm of Thoughts prompt used in the game of 24 experiment.

‍

‍

**Results**

‍

![Image 24: results table of differentprompting methods from the Game of 24 experiment ](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c27_64f0c42bb830986eba75d153_24%2520AoT%2520Experiment%2520Results.png)

Prompt engineering method results from Game of 24

Algorithm of Thoughts destroys CoT and standard prompting. More importantly, Algorithm of Thoughts outperforms ToT with just a single LLM query, compared to ToT’s 109. Algorithm of Thoughts is working smarter, not harder.

### **Experiments: Mini crosswords**

**Setup**

A collection of 20 games is drawn from [goobix.com](http://goobix.com/).

**Baselines**

The same baselines used in the previous experiment are used here. Algorithm of Thoughts is compared against standard prompting, ToT, and CoT.

**Results**

‍

![Image 25: results table of differentprompting methods from the mini crosswords  experiment ](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c24_64f0c52e3ff991f4d3c3dc8b_Minicrosswords%2520AoT%2520Experiment%2520Results.png)

Word success represents the percentage of words correctly completed out of the total count.

‍

Once again, Algorithm of Thoughts outperforms standard prompting and CoT.

Algorithm of Thoughts slightly underperforms compared to ToT, but it uses significantly fewer queries, by a factor of 100. That’s a lot of additional API calls, tokens, and latency.

### Other takeaways

I found one of the final takeaways to be one of the more interesting. The researchers tested to see if Algorithm of Thoughts could outperform the algorithm it is designed after (depth-first search, DFS). If it could, that would signal that LLMs have the potential to not just replicate, but surpass the algorithm's efficiency.

The results are in, and it’s looking pretty good for Algorithm of Thoughts.

‍

![Image 26: Bar chart compared the number of visited nodes for depth-first search versus AoT](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c2a_64f0c517d17efcaae251e8ab_AoT%2520DFS%2520vs%2520AoT%2520visited%2520nodes.png)

‍

This graph shows that Algorithm of Thoughts systematically visits fewer nodes compared to DFS. This implies that Algorithm of Thoughts is able to get to a correct final answer, in fewer steps (less node visits). Algorithm of Thoughts is able to integrate the uniform strategy of the depth-first algorithm, while also integrating intelligent recursive reasoning to limit the steps needed.

Wrapping up
-----------

We cover a lot of the latest research in prompt engineering and AI. Algorithm of Thoughts might be our favorite new method because of it’s ease of use and performance. It is able to compete right alongside ToT, while using significantly less resources.

Additionally, since Algorithm of Thoughts is only a single query, anyone can try it out. Unlike other methods that demand external resources, Algorithm of Thoughts requires nothing more than a correctly structured prompt.

## Metadata

```json
{
  "title": "How Algorithm of Thoughts Prompting Works",
  "description": "Leveraging algorithmic thinking in prompts. How Algorithm of Thoughts is outperforming top prompting engineering methods, with less complexity",
  "url": "https://www.prompthub.us/blog/how-algorithm-of-thoughts-prompting-works",
  "content": "‍\n\nSome prompt engineering techniques are simple and easy to implement (like [\"According to..\"](https://www.prompthub.us/blog/improve-accuracy-and-reduce-hallucinations-with-a-simple-prompting-technique) prompting). Some are extremely powerful, but require a more advanced setup with many more API calls, leading to increased costs and latency (like [Tree of Thoughts](https://www.prompthub.us/blog/how-tree-of-thoughts-prompting-works)).\n\nResearchers at Virginia Tech and Microsoft have recently developed a new method that stands up against the Tree of Thoughts methhod with a remarkable reduction of 100 times fewer queries needed. Yes, you read that correctly — 100 times fewer queries. (link to the full paper [here](https://arxiv.org/pdf/2308.10379.pdf))\n\nEnter, **Algorithm of Thoughts (AoT)**.\n\n‍\n\n![Image 21: Model inputs and outputs for various prompting methods](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c3e_64f0bbd70ba6f2bd63e02543_Algorithm%2520of%2520Thought%2520Compared%2520to%2520Other%2520Methods.png)\n\n‍\n\nWhat is Algorithm of Thoughts prompting?\n----------------------------------------\n\nAlgorithm of Thoughts (AoT) is a prompting engineering method designed to mimic algorithmic thinking in large language models (LLMs). It breaks down tasks into defined sub-steps like defining the problem, gathering and analyzing information, formulating a hypothesis, testing it, and coming to a final conclusion.\n\n‍\n\nWhy Algorithm of Thoughts?\n--------------------------\n\nLarge Language Models (LLMs) are extremely powerful, but they aren’t perfect. Prompt engineering exists because consistently getting high-quality outputs isn’t a walk in the park.\n\nMany of the top-performing, and widely adopted methods are computationally heavy. For example, the Tree of Thoughts (ToT) method requires multiple rounds of querying as it traverses dozens of branches and nodes.\n\nDesigned to address these challenges, Algorithm of Thoughts presents a structured path of reasoning for LLMs. It's a solution that delivers on efficiency without compromising on the quality of outputs.\n\n‍\n\n![Image 22: Flowcharts for different prompting methods. ](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c33_64f0bd12f412735fc67e92c0_Prompt%2520flows%2520for%2520different%2520prompting%2520methods.png)\n\nPrompt flow for different methods\n\nHow Algorithm of Thought promptingworks\n---------------------------------------\n\nAlgorithm of Thoughts is designed to mimic algorithmic thinking. It is broken down into a few steps:\n\n1.  **Define the Problem:** Algorithm of Thoughts begins by clearly stating the problem behind the query or task.\n2.  **Gather Information:** Before diving into solutions, Algorithm of Thoughts prompts the LLM to get the necessary context.\n3.  **Analyze the Information:** Next, the LLM breaks down the gathered information, identifying patterns, relationships, or anomalies.\n4.  **Formulate a Hypothesis:** Based on the analysis, the LLM puts together an initial solution.\n5.  **Test the Hypothesis:** The LLM then thinks of ways to validate or refute its hypothesis, envisioning potential outcomes.\n6.  **Draw Conclusions:** After testing, the LLM summarizes its findings, providing a refined solution to the initial problem.\n7.  **Reflect:** Lastly, the LLM considers the broader implications of its conclusion, thinking of potential next steps or further questions.\n\nAlgorithm of Thoughts 'structured approach ensures the LLM isn’t left to wander aimlessly down many paths.\n\nAlgorithm of Thoughts prompt template\n-------------------------------------\n\nThe Algorithm of Thoughts prompt technique isn’t the easiest to implement, but we’ve done our best to make it plug and play. Generally you want to follow this structure:\n\n‍\n\n‍\n\nHere’s a practical example if you were using Algorithm of Thoughts to do research on the environmental implications of data centers.\n\n1.  **Problem Statement:** What are the environmental implications of increased data center usage?\n2.  **Background Information:** Data centers account for about 1% of global electricity use.\n3.  **Initial Hypothesis:** Implementing renewable energy sources can mitigate the environmental impact.\n4.  **Reasoning:** Evaluate the feasibility and impact of using renewable energy for data centers.\n5.  **Conclusion:** Based on the analysis, is renewable energy a viable solution for data centers?\n\nYou could then restructure that into something a little more LLM-friendly.\n\n\"Given that data centers account for about 1% of global electricity use, what are the environmental implications of increased data center usage? I hypothesize that implementing renewable energy sources can mitigate the environmental impact. Can you evaluate the feasibility and impact of using renewable energy for data centers? Based on your analysis, is renewable energy a viable solution for data centers?”\n\n‍  \nWe built a template in PromptHub that converts a normal prompt into a new prompt, following the Algorithm of Thoughts framework. You can access the template [here](https://app.prompthub.us/templates/292) and try it out right away.\n\n‍  \nIf you don't have PromptHub access but want to try it out, reply to the email that gets sent when you join the waitlist and I'll share an access code with you.\n\n‍\n\n![Image 23: Screenshot of the Algorithm of Thoughts Template in the PromptHub platform](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17cac_64f5e0a5323df832a2a2925e_AoT%2520Screenshot.png)\n\n‍\n\n### **Experiments: Game of 24**\n\n**Setup**\n\nThe researchers pulled 100 rounds of the Game of 24 from [4nums.com](http://4nums.com/). For a game of 24 to be considered successful, it must use the four given numbers to get to a final answer of 24 using only basic arithmetic operations.\n\n**Baselines**\n\nStandard prompting and [Chain of Thought](https://www.prompthub.us/blog/chain-of-thought-prompting-guide) (CoT) were evaluated under a 5-shot framework. Tree of Thoughts (ToT) was implement with a breadth of 5.\n\nFor Algorithm of Thoughts the same 5-shot framework was used as in standard prompting. These methods were sampled 100 times, with the average success rates being documented.\n\n[GPT-4](https://www.prompthub.us/models/gpt-4) was the only model used, and the temperature was set to 0.\n\n**Algorithm of Thoughts prompt example**\n\nHere is the full version of the Algorithm of Thoughts prompt used in the game of 24 experiment.\n\n‍\n\n‍\n\n**Results**\n\n‍\n\n![Image 24: results table of differentprompting methods from the Game of 24 experiment ](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c27_64f0c42bb830986eba75d153_24%2520AoT%2520Experiment%2520Results.png)\n\nPrompt engineering method results from Game of 24\n\nAlgorithm of Thoughts destroys CoT and standard prompting. More importantly, Algorithm of Thoughts outperforms ToT with just a single LLM query, compared to ToT’s 109. Algorithm of Thoughts is working smarter, not harder.\n\n### **Experiments: Mini crosswords**\n\n**Setup**\n\nA collection of 20 games is drawn from [goobix.com](http://goobix.com/).\n\n**Baselines**\n\nThe same baselines used in the previous experiment are used here. Algorithm of Thoughts is compared against standard prompting, ToT, and CoT.\n\n**Results**\n\n‍\n\n![Image 25: results table of differentprompting methods from the mini crosswords  experiment ](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c24_64f0c52e3ff991f4d3c3dc8b_Minicrosswords%2520AoT%2520Experiment%2520Results.png)\n\nWord success represents the percentage of words correctly completed out of the total count.\n\n‍\n\nOnce again, Algorithm of Thoughts outperforms standard prompting and CoT.\n\nAlgorithm of Thoughts slightly underperforms compared to ToT, but it uses significantly fewer queries, by a factor of 100. That’s a lot of additional API calls, tokens, and latency.\n\n### Other takeaways\n\nI found one of the final takeaways to be one of the more interesting. The researchers tested to see if Algorithm of Thoughts could outperform the algorithm it is designed after (depth-first search, DFS). If it could, that would signal that LLMs have the potential to not just replicate, but surpass the algorithm's efficiency.\n\nThe results are in, and it’s looking pretty good for Algorithm of Thoughts.\n\n‍\n\n![Image 26: Bar chart compared the number of visited nodes for depth-first search versus AoT](https://cdn.prod.website-files.com/646e63db3a42c618e0a9935c/66db6b61f3b1a3f3efd17c2a_64f0c517d17efcaae251e8ab_AoT%2520DFS%2520vs%2520AoT%2520visited%2520nodes.png)\n\n‍\n\nThis graph shows that Algorithm of Thoughts systematically visits fewer nodes compared to DFS. This implies that Algorithm of Thoughts is able to get to a correct final answer, in fewer steps (less node visits). Algorithm of Thoughts is able to integrate the uniform strategy of the depth-first algorithm, while also integrating intelligent recursive reasoning to limit the steps needed.\n\nWrapping up\n-----------\n\nWe cover a lot of the latest research in prompt engineering and AI. Algorithm of Thoughts might be our favorite new method because of it’s ease of use and performance. It is able to compete right alongside ToT, while using significantly less resources.\n\nAdditionally, since Algorithm of Thoughts is only a single query, anyone can try it out. Unlike other methods that demand external resources, Algorithm of Thoughts requires nothing more than a correctly structured prompt.",
  "publishedTime": "Aug 31, 2023T00:00:00-04:00",
  "usage": {
    "tokens": 2253
  }
}
```
