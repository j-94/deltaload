---
title: Chain of Continuous Thought: novel paradigm with enhanced LLM Reasoning in continuous latent space
description: Large language models (LLMs) are restricted to reason in the “language space”, where they typically express the reasoning process with a chain-of-thought (CoT) to solve a complex reasoning problem…
url: https://medium.com/@techsachin/chain-of-continuous-thought-novel-paradigm-with-enhanced-llm-reasoning-in-continuous-latent-space-e9461d427c40
timestamp: 2025-01-20T16:18:42.207Z
domain: medium.com
path: @techsachin_chain-of-continuous-thought-novel-paradigm-with-enhanced-llm-reasoning-in-continuous-latent-space-e9461d427c40
---

# Chain of Continuous Thought: novel paradigm with enhanced LLM Reasoning in continuous latent space


Large language models (LLMs) are restricted to reason in the “language space”, where they typically express the reasoning process with a chain-of-thought (CoT) to solve a complex reasoning problem…


## Content

[![Image 25: SACHIN KUMAR](https://miro.medium.com/v2/resize:fill:88:88/1*7GE5_sjWH8e95wFj2s9sgg.jpeg)](https://medium.com/@techsachin?source=post_page---byline--e9461d427c40--------------------------------)

Large language models (LLMs) are restricted to reason in the “language space”, where they typically express the reasoning process with a chain-of-thought (CoT) to solve a complex reasoning problem. Language space may not always be optimal for reasoning.

To explore the potential of LLM reasoning in an unrestricted latent space instead of using natural language, this paper\[1\] introduce a new paradigm Coconut (Chain of Continuous Thought). It involves a simple modification to the traditional CoT process: instead of mapping between hidden states and language tokens using the language model head and embedding layer, Coconut directly feeds the last hidden state (a continuous thought) as the input embedding for the next token, as shown in figure below:

![Image 26](https://miro.medium.com/v2/resize:fit:700/1*xX3SAYM1daNmm12TPpRS8A.png)

Coconut: Chain of Continuous Thought
------------------------------------

i) Method Overview
------------------

*   In this method LLM switches between the “language mode” and “latent mode”, as shown in figure above
*   In language mode, the model operates as a standard language model, autoregressively generating the next token. In latent mode, it directly utilizes the last hidden state as the next input embedding.
*   This last hidden state represents the current reasoning state, termed as a “continuous thought”.
*   Special tokens <bot\> and <eot\> are employed to mark the beginning and end of the latent thought mode, respectively. As an example, we assume latent reasoning occurs between positions i and j, i.e., xi =<bot\> and xj = <eot\>.
*   When the model is in the latent mode (i < t < j), we use the last hidden state from the previous token to replace the input embedding, i.e.,

![Image 27](https://miro.medium.com/v2/resize:fit:448/1*w2nSKC02hnhFkDnPoaXl7w.png)

*   After the latent mode finishes (t ≥ j), the input reverts to using the token embedding, i.e., Et =\[e(x1), e(x2), …, e(xi), hi, hi+1, …, hj−1, e(xj), …, e(xt)\].

ii) Training Procedure
----------------------

*   leverage language CoT data to supervise continuous thought by implementing a multi-stage training curriculum
*   As shown in Figure below, in the initial stage, the model is trained on regular CoT instances.

![Image 28](https://miro.medium.com/v2/resize:fit:700/1*i5pi9blPTnaFyILCMvyQOQ.png)

*   In the subsequent stages, at the k-th stage, the first k reasoning steps in the CoT are replaced with k × c continuous thoughts1, where c is a hyperparameter controlling the number of latent thoughts replacing a single language reasoning step.
*   we also reset the optimizer state when training stages switch.
*   We insert <bot\> and <eot\> tokens to encapsulate the continuous thoughts.
*   During the training process, we mask the loss on questions and latent thoughts. It is important to note that the objective does not encourage the continuous thought to compress the removed language thought, but rather to facilitate the prediction of future reasoning.

iii) Training Details
---------------------

*   proposed continuous thoughts are fully differentiable and allow for back-propagation.
*   perform n + 1 forward passes when n latent thoughts are scheduled in the current training stage, computing a new latent thought with each pass and finally conducting an additional forward pass to obtain a loss on the remaining text sequence
*   While we can save any repetitive computing by using a KV cache, the sequential nature of the multiple forward passes poses challenges for parallelism

iv) Inference Process
---------------------

*   inference process for Coconut is analogous to standard language model decoding, except that in latent mode, we directly feed the last hidden state as the next input embedding.
*   As we focus on the problem-solving setting, we insert a <bot\> token immediately following the question tokens.
*   For <eot\>, we consider two potential strategies:

a) train a binary classifier on latent thoughts to enable the model to autonomously decide when to terminate the latent reasoning, or

b) always pad the latent thoughts to a constant length. We found that both approaches work comparably well.

Experiments
-----------

i) Experimental Setup
---------------------

*   use a pre-trained GPT-2 as the base model for all experiments

**a) Math Reasoning**

*   use 2 latent thoughts (i.e., c = 2) for each reasoning step
*   model goes through 3 stages besides the initial stage.
*   Then, we have an additional stage, where we still use 3 × c continuous thoughts as in the penultimate stage, but remove all the remaining language reasoning chain, to handle long-tail distribution of reasoning chains longer than 3 steps

**b) Logical Reasoning**

*   use one continuous thought for every reasoning step (i.e., c = 1).
*   The model goes through 6 training stages in addition to the initial stage, because the maximum number of reasoning steps is 6 in these two datasets.
*   The model then fully reasons with continuous thoughts to solve the problems in the last stage.

ii) Baselines and Variants of Coconut
-------------------------------------

**a) Baselines used**

*   CoT:We use the complete reasoning chains to train the language model with supervised finetuning, and during inference, the model generates a reasoning chain before outputting an answer.
*   No-CoT: The LLM is trained to directly generate the answer without using a reasoning chain.
*   iCoT: The model is trained with language reasoning chains and follows a carefully designed schedule that “internalizes” CoT. As the training goes on, tokens at the beginning of the reasoning chain are gradually removed until only the answer remains. During inference, the model directly predicts the answer.
*   Pause token: The model is trained using only the question and answer, without a reasoning chain. However, different from No-CoT, special <pause\> tokens are inserted between the question and answer, which are believed to provide the model with additional computational capacity to derive the answer.

**b) Variants of Coconut**

*   w/o curriculum: Instead of the multi-stage training, we directly use the data from the last stage which only includes questions and answers to train Coconut. The model uses continuous thoughts to solve the whole problem.
*   w/o thought: We keep the multi-stage training which removes language reasoning steps gradually, but don’t use any continuous latent thoughts. While this is similar to iCoT in the high-level idea, the exact training schedule is set to be consistent with Coconut, instead of iCoT. This ensures a more strict comparison.
*   Pause as thought: We use special <pause\> tokens to replace the continuous thoughts, and apply the same multi-stage training curriculum as Coconut.

iii) Results
------------

*   Table below shows Results on three datasets: GSM8l, ProntoQA and ProsQA. Higher accuracy indicates stronger reasoning ability, while generating fewer tokens indicates better efficiency.

![Image 29](https://miro.medium.com/v2/resize:fit:700/1*Q-gIEQor0wYLlS-oFo9BwA.png)

*   In experiments with GSM8k, we found that Coconut outperformed other architectures trained with similar strategies, particularly surpassing the latest baseline, iCoT
*   Figure below shows experimentation with adjusting the hyperparameter c, which controls the number of latent thoughts corresponding to one language reasoning step

![Image 30](https://miro.medium.com/v2/resize:fit:436/1*P3C5UZUKzYUGjE5si0AfoA.png)

*   As we increased c from 0 to 1 to 2, the model’s performance steadily improved, suggesting that a chaining effect similar to CoT can be observed in the latent space.
*   In two other synthetic tasks, we found that the variants of Coconut (w/o thoughts or pause as thought), and the iCoT baseline also achieve impressive accuracy
*   Coconut, its variants, and iCoT substantially enhance reasoning on ProsQA, indicating that latent space reasoning provides a clear advantage in tasks demanding extensive planning

Understanding the Latent Reasoning in Coconut
---------------------------------------------

i) Experimental Setup
---------------------

**a) Method**

*   design of Coconut allows us to control the number of latent thoughts by manually setting the position of the <eot\> token during inference
*   In our experiments, we test variants of Coconut on ProsQA with k ∈ {0, 1, 2, 3, 4, 5, 6}. Note that all these variants only differ in inference time while sharing the same model weights.

**b) Metrics**

*   apply two sets of evaluation metric, with One of them is based on the correctness of the final answer, regardless of the reasoning process
*   To enable fine-grained analysis, we define another metric on the reasoning process. Assuming we have a complete language reasoning chain which specifies a path in the graph, we can classify it into

(1) Correct Path: The output is one of the shortest paths to the correct answer.

(2) Longer Path: A valid path that correctly answers the question but is longer than the shortest path.

(3) Hallucination: The path includes nonexistent edges or is disconnected.

(4) Wrong Target: A valid path in the graph, but the destination node is not the one being asked

In no-CoT and Coconut with larger k, the model may only output the final answer without any partial path, and it falls into (5) Correct Label or (6) Incorrect Label

ii) Interpolating between Latent and Language Reasoning
-------------------------------------------------------

*   Figure below shows a comparative analysis of different reasoning methods on ProsQA

![Image 31](https://miro.medium.com/v2/resize:fit:700/1*IMMniuLHtDxincNq3i45zA.png)

*   As more reasoning is done with continuous thoughts (increasing k), both final answer accuracy (Figure’s left) and the rate of correct reasoning processes (“Correct Label” and “Correct Path” in Figure’s right) improve.
*   Figure below shows A case study of ProsQA. The model trained with CoT hallucinates an edge (Every yumpus is a rempus) after getting stuck in a dead end. Coconut (k=1) outputs a path that ends with an irrelevant node. Coconut (k=2) solves the problem correctly.

![Image 32](https://miro.medium.com/v2/resize:fit:700/1*okFf0KWADHaUFC9eoaHWNQ.png)

iii) Interpreting the Latent Search Tree
----------------------------------------

*   Given the intuition that continuous thoughts can encode multiple potential next steps, the latent reasoning can be interpreted as a search tree, rather than merely a reasoning “chain”.
*   depict all possible branches in the left part of Figure below. Similarly, in the second step, the frontier nodes will be the grandchildren of Alex (Figure below, right).

![Image 33](https://miro.medium.com/v2/resize:fit:700/1*tGqh6OqrVyVHas3M2ZFYTw.png)

*   Unlike a standard breadth-first search (BFS), which explores all frontier nodes uniformly, the model demonstrates the ability to prioritize promising nodes while pruning less relevant ones
*   The probability distribution can be viewed as the model’s implicit value function, estimating each node’s potential to reach the target. As shown in the figure, “lempus”, “zhorpus”, “grimpus”, and “sterpus” have a value of 0.33, 0.16, 0.32, and 0.01, respectively
*   Figure below presents an analysis of the parallelism in the model’s latent reasoning across the first and second thoughts. For the first thoughts (left panel), the cumulative values of the top-1, top-2, and top-3 candidate nodes are computed and plotted against their respective percentiles across the test set.

![Image 34](https://miro.medium.com/v2/resize:fit:700/1*De3Iw0Mt4dXg8zRB3A0xzw.png)

*   The noticeable gaps between the three lines indicate that the model maintains significant diversity in its reasoning paths at this stage, suggesting a broad exploration of alternative possibilities. In contrast, the second thoughts (right panel) show a narrowing of these gaps

Conclusion
----------

*   presented Coconut, a novel paradigm for reasoning in continuous latent space.
*   Through extensive experiments, we demonstrated that Coconut significantly enhances LLM reasoning capabilities.
*   Notably, our detailed analysis highlighted how an unconstrained latent space allows the model to develop an effective reasoning pattern similar to BFS

Paper: [https://arxiv.org/abs/2412.06769](https://arxiv.org/abs/2412.06769)

References:

1.  Training Large Language Models to Reason in a Continuous Latent Space by Hao et al.[arXiv:2412.06769](https://arxiv.org/abs/2412.06769)

## Metadata

```json
{
  "title": "Chain of Continuous Thought: novel paradigm with enhanced LLM Reasoning in continuous latent space",
  "description": "Large language models (LLMs) are restricted to reason in the “language space”, where they typically express the reasoning process with a chain-of-thought (CoT) to solve a complex reasoning problem…",
  "url": "https://medium.com/@techsachin/chain-of-continuous-thought-novel-paradigm-with-enhanced-llm-reasoning-in-continuous-latent-space-e9461d427c40",
  "content": "[![Image 25: SACHIN KUMAR](https://miro.medium.com/v2/resize:fill:88:88/1*7GE5_sjWH8e95wFj2s9sgg.jpeg)](https://medium.com/@techsachin?source=post_page---byline--e9461d427c40--------------------------------)\n\nLarge language models (LLMs) are restricted to reason in the “language space”, where they typically express the reasoning process with a chain-of-thought (CoT) to solve a complex reasoning problem. Language space may not always be optimal for reasoning.\n\nTo explore the potential of LLM reasoning in an unrestricted latent space instead of using natural language, this paper\\[1\\] introduce a new paradigm Coconut (Chain of Continuous Thought). It involves a simple modification to the traditional CoT process: instead of mapping between hidden states and language tokens using the language model head and embedding layer, Coconut directly feeds the last hidden state (a continuous thought) as the input embedding for the next token, as shown in figure below:\n\n![Image 26](https://miro.medium.com/v2/resize:fit:700/1*xX3SAYM1daNmm12TPpRS8A.png)\n\nCoconut: Chain of Continuous Thought\n------------------------------------\n\ni) Method Overview\n------------------\n\n*   In this method LLM switches between the “language mode” and “latent mode”, as shown in figure above\n*   In language mode, the model operates as a standard language model, autoregressively generating the next token. In latent mode, it directly utilizes the last hidden state as the next input embedding.\n*   This last hidden state represents the current reasoning state, termed as a “continuous thought”.\n*   Special tokens <bot\\> and <eot\\> are employed to mark the beginning and end of the latent thought mode, respectively. As an example, we assume latent reasoning occurs between positions i and j, i.e., xi =<bot\\> and xj = <eot\\>.\n*   When the model is in the latent mode (i < t < j), we use the last hidden state from the previous token to replace the input embedding, i.e.,\n\n![Image 27](https://miro.medium.com/v2/resize:fit:448/1*w2nSKC02hnhFkDnPoaXl7w.png)\n\n*   After the latent mode finishes (t ≥ j), the input reverts to using the token embedding, i.e., Et =\\[e(x1), e(x2), …, e(xi), hi, hi+1, …, hj−1, e(xj), …, e(xt)\\].\n\nii) Training Procedure\n----------------------\n\n*   leverage language CoT data to supervise continuous thought by implementing a multi-stage training curriculum\n*   As shown in Figure below, in the initial stage, the model is trained on regular CoT instances.\n\n![Image 28](https://miro.medium.com/v2/resize:fit:700/1*i5pi9blPTnaFyILCMvyQOQ.png)\n\n*   In the subsequent stages, at the k-th stage, the first k reasoning steps in the CoT are replaced with k × c continuous thoughts1, where c is a hyperparameter controlling the number of latent thoughts replacing a single language reasoning step.\n*   we also reset the optimizer state when training stages switch.\n*   We insert <bot\\> and <eot\\> tokens to encapsulate the continuous thoughts.\n*   During the training process, we mask the loss on questions and latent thoughts. It is important to note that the objective does not encourage the continuous thought to compress the removed language thought, but rather to facilitate the prediction of future reasoning.\n\niii) Training Details\n---------------------\n\n*   proposed continuous thoughts are fully differentiable and allow for back-propagation.\n*   perform n + 1 forward passes when n latent thoughts are scheduled in the current training stage, computing a new latent thought with each pass and finally conducting an additional forward pass to obtain a loss on the remaining text sequence\n*   While we can save any repetitive computing by using a KV cache, the sequential nature of the multiple forward passes poses challenges for parallelism\n\niv) Inference Process\n---------------------\n\n*   inference process for Coconut is analogous to standard language model decoding, except that in latent mode, we directly feed the last hidden state as the next input embedding.\n*   As we focus on the problem-solving setting, we insert a <bot\\> token immediately following the question tokens.\n*   For <eot\\>, we consider two potential strategies:\n\na) train a binary classifier on latent thoughts to enable the model to autonomously decide when to terminate the latent reasoning, or\n\nb) always pad the latent thoughts to a constant length. We found that both approaches work comparably well.\n\nExperiments\n-----------\n\ni) Experimental Setup\n---------------------\n\n*   use a pre-trained GPT-2 as the base model for all experiments\n\n**a) Math Reasoning**\n\n*   use 2 latent thoughts (i.e., c = 2) for each reasoning step\n*   model goes through 3 stages besides the initial stage.\n*   Then, we have an additional stage, where we still use 3 × c continuous thoughts as in the penultimate stage, but remove all the remaining language reasoning chain, to handle long-tail distribution of reasoning chains longer than 3 steps\n\n**b) Logical Reasoning**\n\n*   use one continuous thought for every reasoning step (i.e., c = 1).\n*   The model goes through 6 training stages in addition to the initial stage, because the maximum number of reasoning steps is 6 in these two datasets.\n*   The model then fully reasons with continuous thoughts to solve the problems in the last stage.\n\nii) Baselines and Variants of Coconut\n-------------------------------------\n\n**a) Baselines used**\n\n*   CoT:We use the complete reasoning chains to train the language model with supervised finetuning, and during inference, the model generates a reasoning chain before outputting an answer.\n*   No-CoT: The LLM is trained to directly generate the answer without using a reasoning chain.\n*   iCoT: The model is trained with language reasoning chains and follows a carefully designed schedule that “internalizes” CoT. As the training goes on, tokens at the beginning of the reasoning chain are gradually removed until only the answer remains. During inference, the model directly predicts the answer.\n*   Pause token: The model is trained using only the question and answer, without a reasoning chain. However, different from No-CoT, special <pause\\> tokens are inserted between the question and answer, which are believed to provide the model with additional computational capacity to derive the answer.\n\n**b) Variants of Coconut**\n\n*   w/o curriculum: Instead of the multi-stage training, we directly use the data from the last stage which only includes questions and answers to train Coconut. The model uses continuous thoughts to solve the whole problem.\n*   w/o thought: We keep the multi-stage training which removes language reasoning steps gradually, but don’t use any continuous latent thoughts. While this is similar to iCoT in the high-level idea, the exact training schedule is set to be consistent with Coconut, instead of iCoT. This ensures a more strict comparison.\n*   Pause as thought: We use special <pause\\> tokens to replace the continuous thoughts, and apply the same multi-stage training curriculum as Coconut.\n\niii) Results\n------------\n\n*   Table below shows Results on three datasets: GSM8l, ProntoQA and ProsQA. Higher accuracy indicates stronger reasoning ability, while generating fewer tokens indicates better efficiency.\n\n![Image 29](https://miro.medium.com/v2/resize:fit:700/1*Q-gIEQor0wYLlS-oFo9BwA.png)\n\n*   In experiments with GSM8k, we found that Coconut outperformed other architectures trained with similar strategies, particularly surpassing the latest baseline, iCoT\n*   Figure below shows experimentation with adjusting the hyperparameter c, which controls the number of latent thoughts corresponding to one language reasoning step\n\n![Image 30](https://miro.medium.com/v2/resize:fit:436/1*P3C5UZUKzYUGjE5si0AfoA.png)\n\n*   As we increased c from 0 to 1 to 2, the model’s performance steadily improved, suggesting that a chaining effect similar to CoT can be observed in the latent space.\n*   In two other synthetic tasks, we found that the variants of Coconut (w/o thoughts or pause as thought), and the iCoT baseline also achieve impressive accuracy\n*   Coconut, its variants, and iCoT substantially enhance reasoning on ProsQA, indicating that latent space reasoning provides a clear advantage in tasks demanding extensive planning\n\nUnderstanding the Latent Reasoning in Coconut\n---------------------------------------------\n\ni) Experimental Setup\n---------------------\n\n**a) Method**\n\n*   design of Coconut allows us to control the number of latent thoughts by manually setting the position of the <eot\\> token during inference\n*   In our experiments, we test variants of Coconut on ProsQA with k ∈ {0, 1, 2, 3, 4, 5, 6}. Note that all these variants only differ in inference time while sharing the same model weights.\n\n**b) Metrics**\n\n*   apply two sets of evaluation metric, with One of them is based on the correctness of the final answer, regardless of the reasoning process\n*   To enable fine-grained analysis, we define another metric on the reasoning process. Assuming we have a complete language reasoning chain which specifies a path in the graph, we can classify it into\n\n(1) Correct Path: The output is one of the shortest paths to the correct answer.\n\n(2) Longer Path: A valid path that correctly answers the question but is longer than the shortest path.\n\n(3) Hallucination: The path includes nonexistent edges or is disconnected.\n\n(4) Wrong Target: A valid path in the graph, but the destination node is not the one being asked\n\nIn no-CoT and Coconut with larger k, the model may only output the final answer without any partial path, and it falls into (5) Correct Label or (6) Incorrect Label\n\nii) Interpolating between Latent and Language Reasoning\n-------------------------------------------------------\n\n*   Figure below shows a comparative analysis of different reasoning methods on ProsQA\n\n![Image 31](https://miro.medium.com/v2/resize:fit:700/1*IMMniuLHtDxincNq3i45zA.png)\n\n*   As more reasoning is done with continuous thoughts (increasing k), both final answer accuracy (Figure’s left) and the rate of correct reasoning processes (“Correct Label” and “Correct Path” in Figure’s right) improve.\n*   Figure below shows A case study of ProsQA. The model trained with CoT hallucinates an edge (Every yumpus is a rempus) after getting stuck in a dead end. Coconut (k=1) outputs a path that ends with an irrelevant node. Coconut (k=2) solves the problem correctly.\n\n![Image 32](https://miro.medium.com/v2/resize:fit:700/1*okFf0KWADHaUFC9eoaHWNQ.png)\n\niii) Interpreting the Latent Search Tree\n----------------------------------------\n\n*   Given the intuition that continuous thoughts can encode multiple potential next steps, the latent reasoning can be interpreted as a search tree, rather than merely a reasoning “chain”.\n*   depict all possible branches in the left part of Figure below. Similarly, in the second step, the frontier nodes will be the grandchildren of Alex (Figure below, right).\n\n![Image 33](https://miro.medium.com/v2/resize:fit:700/1*tGqh6OqrVyVHas3M2ZFYTw.png)\n\n*   Unlike a standard breadth-first search (BFS), which explores all frontier nodes uniformly, the model demonstrates the ability to prioritize promising nodes while pruning less relevant ones\n*   The probability distribution can be viewed as the model’s implicit value function, estimating each node’s potential to reach the target. As shown in the figure, “lempus”, “zhorpus”, “grimpus”, and “sterpus” have a value of 0.33, 0.16, 0.32, and 0.01, respectively\n*   Figure below presents an analysis of the parallelism in the model’s latent reasoning across the first and second thoughts. For the first thoughts (left panel), the cumulative values of the top-1, top-2, and top-3 candidate nodes are computed and plotted against their respective percentiles across the test set.\n\n![Image 34](https://miro.medium.com/v2/resize:fit:700/1*De3Iw0Mt4dXg8zRB3A0xzw.png)\n\n*   The noticeable gaps between the three lines indicate that the model maintains significant diversity in its reasoning paths at this stage, suggesting a broad exploration of alternative possibilities. In contrast, the second thoughts (right panel) show a narrowing of these gaps\n\nConclusion\n----------\n\n*   presented Coconut, a novel paradigm for reasoning in continuous latent space.\n*   Through extensive experiments, we demonstrated that Coconut significantly enhances LLM reasoning capabilities.\n*   Notably, our detailed analysis highlighted how an unconstrained latent space allows the model to develop an effective reasoning pattern similar to BFS\n\nPaper: [https://arxiv.org/abs/2412.06769](https://arxiv.org/abs/2412.06769)\n\nReferences:\n\n1.  Training Large Language Models to Reason in a Continuous Latent Space by Hao et al.[arXiv:2412.06769](https://arxiv.org/abs/2412.06769)",
  "publishedTime": "2024-12-10T11:28:26.196Z",
  "usage": {
    "tokens": 2914
  }
}
```
