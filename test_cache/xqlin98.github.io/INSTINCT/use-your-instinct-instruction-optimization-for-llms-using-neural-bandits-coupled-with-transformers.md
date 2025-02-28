---
title: Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers
description: DESCRIPTION META TAG
url: https://xqlin98.github.io/INSTINCT/
timestamp: 2025-01-20T15:47:52.581Z
domain: xqlin98.github.io
path: INSTINCT
---

# Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers


DESCRIPTION META TAG


## Content

National University of Singapore (NUS)  
Tencent  
Massachusetts Institute of Technology (MIT)  
\*Equal Contribution  
Accepted by ICML 2024, also presented at NeurIPS 2023, Workshop on Instruction Tuning and Instruction Following

Abstract
--------

Large language models (LLMs) have shown remarkable instruction-following capabilities and achieved impressive performances in various applications. However, the performances of LLMs depend heavily on the instructions given to them, which are typically manually tuned with substantial human efforts. Recent work has used the query-efficient Bayesian optimization (BO) algorithm to automatically optimize the instructions given to black-box LLMs. However, BO usually falls short when optimizing highly sophisticated (e.g., high-dimensional) objective functions, such as the functions mapping an instruction to the performance of an LLM. This is mainly due to the limited expressive power of the Gaussian process (GP) model which is used by BO as a surrogate to model the objective function. Meanwhile, it has been repeatedly shown that neural networks (NNs), especially pre-trained transformers, possess strong expressive power and can model highly complex functions. So, we adopt a neural bandit algorithm which replaces the GP in BO by an NN surrogate to optimize instructions for black-box LLMs. More importantly, the neural bandit algorithm allows us to naturally couple the NN surrogate with the hidden representation learned by a pre-trained transformer (i.e., an open-source LLM), which significantly boosts its performance. These motivate us to propose our INSTruction optimization usIng Neural bandits Coupled with Transformers (INSTINCT) algorithm. We perform instruction optimization for ChatGPT and use extensive experiments to show that our INSTINCT consistently outperforms the existing methods in different tasks, such as in various instruction induction tasks and the task of improving the zero-shot chain-of-thought instruction.

How to use your INSTINCT?
-------------------------

Step ①: Training the neural network for score prediction.

Step ②: Selecting the next soft prompt using the NeuralUCB algorithm.

Step ③: Generating the instruction using a white-box LLM.

Step ④: Predicting the label for a validation dataset using black-box LLM using the generated instruction.

Step ⑤: Evaluating the predicted results (i.e., the performance of the instruction).

Step ⑥: Extracting the hidden representation from the white-box LLM for the instruction. Adding the hidden representation and the evaluated score to the dataset which is used to train the neural network.

![Image 18: GIF](https://xqlin98.github.io/INSTINCT/static/images/instinct.gif)

* * *

Results
-------

### How does INSTINCT generate higher-quality instructions across iterations?

![Image 19: Demos Image](https://xqlin98.github.io/INSTINCT/static/images/demos.png)

Instruction induction
---------------------

Our approach significantly outperforms APE and InstructZero in a variety of instruction induction tasks.

Figure 1: Improvement of our INSTINCT over baselines (in 30 tasks). ![Image 20: II Image](https://xqlin98.github.io/INSTINCT/static/images/ii1.png)

Table 1: Average test accuracy achieved by (i) APE, (ii) InstructZero and (iii) INSTINCT. ![Image 21: II Table](https://xqlin98.github.io/INSTINCT/static/images/ii2.png)

### Improving instruction for summarization tasks

We demonstrate the capability of our INSTINCT in instruction optimization for the task of text summarization.

Table 2: Instruction optimization on SAMSum dataset (summarization task). ![Image 22: Sum Table](https://xqlin98.github.io/INSTINCT/static/images/sum.png)

### Improving zero-shot chain-of-thought prompts

We improve zero-shot CoT prompts on multiple arithmetic reasoning tasks.

Table 3: The best zero-shot CoT instructions found by different algorithms and their scores. ![Image 23: CoT Table](https://xqlin98.github.io/INSTINCT/static/images/cot.png) ![Image 24: brain](https://xqlin98.github.io/INSTINCT/static/images/smart.webp)

### Further improvement with one-shot in-context learning

We see wider potential applications of our INSTINCT through its combination with in-context learning.

Table 4: Average test accuracy achieved by (i) INSTINCT, (ii) test-time-only one-shot INSTINCT, (iii) one-shot INSTINCT. The results including all tasks are given in the paper. ![Image 25: One-shot Table](https://xqlin98.github.io/INSTINCT/static/images/oneshot.png)

* * *

BibTeX
------

```
@inproceedings{lin2023use,
        title={Use Your {INSTINCT}: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers},
        author={Xiaoqiang Lin and Zhaoxuan Wu and Zhongxiang Dai and Wenyang Hu and Yao Shu and See-Kiong Ng and Patrick Jaillet and Bryan Kian Hsiang Low},
        year={2024},
        booktitle={Proc. ICML}
}
```

## Metadata

```json
{
  "title": "Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers",
  "description": "DESCRIPTION META TAG",
  "url": "https://xqlin98.github.io/INSTINCT/",
  "content": "National University of Singapore (NUS)  \nTencent  \nMassachusetts Institute of Technology (MIT)  \n\\*Equal Contribution  \nAccepted by ICML 2024, also presented at NeurIPS 2023, Workshop on Instruction Tuning and Instruction Following\n\nAbstract\n--------\n\nLarge language models (LLMs) have shown remarkable instruction-following capabilities and achieved impressive performances in various applications. However, the performances of LLMs depend heavily on the instructions given to them, which are typically manually tuned with substantial human efforts. Recent work has used the query-efficient Bayesian optimization (BO) algorithm to automatically optimize the instructions given to black-box LLMs. However, BO usually falls short when optimizing highly sophisticated (e.g., high-dimensional) objective functions, such as the functions mapping an instruction to the performance of an LLM. This is mainly due to the limited expressive power of the Gaussian process (GP) model which is used by BO as a surrogate to model the objective function. Meanwhile, it has been repeatedly shown that neural networks (NNs), especially pre-trained transformers, possess strong expressive power and can model highly complex functions. So, we adopt a neural bandit algorithm which replaces the GP in BO by an NN surrogate to optimize instructions for black-box LLMs. More importantly, the neural bandit algorithm allows us to naturally couple the NN surrogate with the hidden representation learned by a pre-trained transformer (i.e., an open-source LLM), which significantly boosts its performance. These motivate us to propose our INSTruction optimization usIng Neural bandits Coupled with Transformers (INSTINCT) algorithm. We perform instruction optimization for ChatGPT and use extensive experiments to show that our INSTINCT consistently outperforms the existing methods in different tasks, such as in various instruction induction tasks and the task of improving the zero-shot chain-of-thought instruction.\n\nHow to use your INSTINCT?\n-------------------------\n\nStep ①: Training the neural network for score prediction.\n\nStep ②: Selecting the next soft prompt using the NeuralUCB algorithm.\n\nStep ③: Generating the instruction using a white-box LLM.\n\nStep ④: Predicting the label for a validation dataset using black-box LLM using the generated instruction.\n\nStep ⑤: Evaluating the predicted results (i.e., the performance of the instruction).\n\nStep ⑥: Extracting the hidden representation from the white-box LLM for the instruction. Adding the hidden representation and the evaluated score to the dataset which is used to train the neural network.\n\n![Image 18: GIF](https://xqlin98.github.io/INSTINCT/static/images/instinct.gif)\n\n* * *\n\nResults\n-------\n\n### How does INSTINCT generate higher-quality instructions across iterations?\n\n![Image 19: Demos Image](https://xqlin98.github.io/INSTINCT/static/images/demos.png)\n\nInstruction induction\n---------------------\n\nOur approach significantly outperforms APE and InstructZero in a variety of instruction induction tasks.\n\nFigure 1: Improvement of our INSTINCT over baselines (in 30 tasks). ![Image 20: II Image](https://xqlin98.github.io/INSTINCT/static/images/ii1.png)\n\nTable 1: Average test accuracy achieved by (i) APE, (ii) InstructZero and (iii) INSTINCT. ![Image 21: II Table](https://xqlin98.github.io/INSTINCT/static/images/ii2.png)\n\n### Improving instruction for summarization tasks\n\nWe demonstrate the capability of our INSTINCT in instruction optimization for the task of text summarization.\n\nTable 2: Instruction optimization on SAMSum dataset (summarization task). ![Image 22: Sum Table](https://xqlin98.github.io/INSTINCT/static/images/sum.png)\n\n### Improving zero-shot chain-of-thought prompts\n\nWe improve zero-shot CoT prompts on multiple arithmetic reasoning tasks.\n\nTable 3: The best zero-shot CoT instructions found by different algorithms and their scores. ![Image 23: CoT Table](https://xqlin98.github.io/INSTINCT/static/images/cot.png) ![Image 24: brain](https://xqlin98.github.io/INSTINCT/static/images/smart.webp)\n\n### Further improvement with one-shot in-context learning\n\nWe see wider potential applications of our INSTINCT through its combination with in-context learning.\n\nTable 4: Average test accuracy achieved by (i) INSTINCT, (ii) test-time-only one-shot INSTINCT, (iii) one-shot INSTINCT. The results including all tasks are given in the paper. ![Image 25: One-shot Table](https://xqlin98.github.io/INSTINCT/static/images/oneshot.png)\n\n* * *\n\nBibTeX\n------\n\n```\n@inproceedings{lin2023use,\n        title={Use Your {INSTINCT}: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers},\n        author={Xiaoqiang Lin and Zhaoxuan Wu and Zhongxiang Dai and Wenyang Hu and Yao Shu and See-Kiong Ng and Patrick Jaillet and Bryan Kian Hsiang Low},\n        year={2024},\n        booktitle={Proc. ICML}\n}\n```",
  "usage": {
    "tokens": 1077
  }
}
```
