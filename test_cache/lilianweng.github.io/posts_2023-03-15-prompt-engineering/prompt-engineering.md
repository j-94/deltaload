---
title: Prompt Engineering
description: Prompt Engineering, also known as In-Context Prompting, refers to methods for how to communicate with LLM to steer its behavior for desired outcomes without updating the model weights. It is an empirical science and the effect of prompt engineering methods can vary a lot among models, thus requiring heavy experimentation and heuristics.
This post only focuses on prompt engineering for autoregressive language models, so nothing with Cloze tests, image generation or multimodality models. At its core, the goal of prompt engineering is about alignment and model steerability. Check my previous post on controllable text generation.
url: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering
timestamp: 2025-01-20T15:44:09.465Z
domain: lilianweng.github.io
path: posts_2023-03-15-prompt-engineering
---

# Prompt Engineering


Prompt Engineering, also known as In-Context Prompting, refers to methods for how to communicate with LLM to steer its behavior for desired outcomes without updating the model weights. It is an empirical science and the effect of prompt engineering methods can vary a lot among models, thus requiring heavy experimentation and heuristics.
This post only focuses on prompt engineering for autoregressive language models, so nothing with Cloze tests, image generation or multimodality models. At its core, the goal of prompt engineering is about alignment and model steerability. Check my previous post on controllable text generation.


## Content

**Prompt Engineering**, also known as **In-Context Prompting**, refers to methods for how to communicate with LLM to steer its behavior for desired outcomes _without_ updating the model weights. It is an empirical science and the effect of prompt engineering methods can vary a lot among models, thus requiring heavy experimentation and heuristics.

This post only focuses on prompt engineering for autoregressive language models, so nothing with Cloze tests, image generation or multimodality models. At its core, the goal of prompt engineering is about alignment and model steerability. Check my [previous post](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/) on controllable text generation.

\[My personal spicy take\] In my opinion, some prompt engineering papers are not worthy 8 pages long, since those tricks can be explained in one or a few sentences and the rest is all about benchmarking. An easy-to-use and shared benchmark infrastructure should be more beneficial to the community. Iterative prompting or external tool use would not be trivial to set up. Also non-trivial to align the whole research community to adopt it.

Basic Prompting
---------------

Zero-shot and few-shot learning are two most basic approaches for prompting the model, pioneered by many LLM papers and commonly used for benchmarking LLM performance.

Zero-Shot
---------

**Zero-shot learning** is to simply feed the task text to the model and ask for results.

(All the sentiment analysis examples are from SST-2)

```
Text: i'll bet the video game is a lot more fun than the film.
Sentiment:
```

Few-shot
--------

**Few-shot learning** presents a set of high-quality demonstrations, each consisting of both input and desired output, on the target task. As the model first sees good examples, it can better understand human intention and criteria for what kinds of answers are wanted. Therefore, few-shot learning often leads to better performance than zero-shot. However, it comes at the cost of more token consumption and may hit the context length limit when input and output text are long.

```
Text: (lawrence bounces) all over the stage, dancing, running, sweating, mopping his face and generally displaying the wacky talent that brought him fame in the first place.
Sentiment: positive

Text: despite all evidence to the contrary, this clunker has somehow managed to pose as an actual feature movie, the kind that charges full admission and gets hyped on tv and purports to amuse small children and ostensible adults.
Sentiment: negative

Text: for the first time in years, de niro digs deep emotionally, perhaps because he's been stirred by the powerful work of his co-stars.
Sentiment: positive

Text: i'll bet the video game is a lot more fun than the film.
Sentiment:
```

Many studies looked into how to construct in-context examples to maximize the performance and observed that **choice of prompt format, training examples, and the order of the examples can lead to dramatically different performance**, from near random guess to near SoTA.

[Zhao et al. (2021)](https://arxiv.org/abs/2102.09690) investigated the case of few-shot classification and proposed that several biases with LLM (they use GPT-3 in the experiments) contribute to such high variance: (1) _Majority label bias_ exists if distribution of labels among the examples is unbalanced; (2) _Recency bias_ refers to the tendency where the model may repeat the label at the end; (3) _Common token bias_ indicates that LLM tends to produce common tokens more often than rare tokens. To conquer such bias, they proposed a method to calibrate the label probabilities output by the model to be uniform when the input string is `N/A`.

### Tips for Example Selection

*   Choose examples that are semantically similar to the test example using $k$-NN clustering in the embedding space ([Liu et al., 2021](https://arxiv.org/abs/2101.06804))
    
*   To select a diverse and representative set of examples, [Su et al. (2022)](https://arxiv.org/abs/2209.01975) proposed to use a graph-based approach: (1) First, construct a directed graph $G=(V, E)$ based on the embedding (e.g. by [SBERT](https://arxiv.org/abs/1908.10084) or [other](https://arxiv.org/abs/2201.10005) [embedding](https://platform.openai.com/docs/guides/embeddings) [models](https://openai.com/blog/new-and-improved-embedding-model)) cosine similarity between samples, where each node points to its $k$ nearest neighbors; (2) Start with a set of selected samples $\\mathcal{L}=\\emptyset$ and a set of remaining samples $\\mathcal{U}$. Each sample $u \\in \\mathcal{U}$ is scored by $$ \\text{score}(u) = \\sum\_{v \\in \\{v \\mid (u, v) \\in E, v\\in \\mathcal{U}\\}} s(v)\\quad\\text{where }s(v)=\\rho^{- \\vert \\{\\ell \\in \\mathcal{L} \\vert (v, \\ell)\\in E \\}\\vert},\\quad\\rho \> 1 $$ such that $s(v)$ is low if many of $v$’s neighbors are selected and thus the scoring encourages to pick diverse samples.
    
*   [Rubin et al. (2022)](https://arxiv.org/abs/2112.08633) proposed to train embeddings via [contrastive learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/) specific to one training dataset for in-context learning sample selection. Given each training pair $(x, y)$, the quality of one example $e\_i$ (formatted input-output pair) can be measured by a conditioned probability assigned by LM: $\\text{score}(e\_i) = P\_\\text{LM}(y \\mid e\_i, x)$. We can identify other examples with top-$k$ and bottom-$k$ scores as positive and negative sets of candidates for every training pair and use that for contrastive learning.
    
*   Some researchers tried [Q-Learning](https://lilianweng.github.io/posts/2018-02-19-rl-overview/#q-learning-off-policy-td-control) to do sample selection. ([Zhang et al. 2022](https://arxiv.org/abs/2211.04486))
    
*   Motivated by uncertainty-based [active learning](https://lilianweng.github.io/posts/2022-02-20-active-learning/), [Diao et al. (2023)](https://arxiv.org/abs/2302.12246) suggested to identify examples with high disagreement or entropy among multiple sampling trials. Then annotate these examples to be used in few-shot prompts.
    

### Tips for Example Ordering

*   A general suggestion is to keep the selection of examples diverse, relevant to the test sample and in random order to avoid majority label bias and recency bias.
*   Increasing model sizes or including more training examples does not reduce variance among different permutations of in-context examples. Same order may work well for one model but badly for another. When the validation set is limited, consider choosing the order such that the model does not produce extremely unbalanced predictions or being overconfident about its predictions. ([Lu et al. 2022](https://arxiv.org/abs/2104.08786))

Instruction Prompting
---------------------

The purpose of presenting few-shot examples in the prompt is to explain our intent to the model; in other words, describe the task instruction to the model in the form of demonstrations. However, few-shot can be expensive in terms of token usage and restricts the input length due to limited context length. So, why not just give the instruction directly?

_Instructed LM_ (e.g. [InstructGPT](https://openai.com/research/instruction-following), [natural instruction](https://github.com/allenai/natural-instructions)) finetunes a pretrained model with high-quality tuples of (task instruction, input, ground truth output) to make LM better understand user intention and follow instruction. [RLHF](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/#rl-fine-tuning-with-human-preferences) (Reinforcement Learning from Human Feedback) is a common method to do so. The benefit of instruction following style fine-tuning improves the model to be more aligned with human intention and greatly reduces the cost of communication.

When interacting with instruction models, we should describe the task requirement in details, trying to be _specific_ and _precise_ and avoiding say “not do something” but rather specify what to do.

```
Please label the sentiment towards the movie of the given movie review. The sentiment label should be "positive" or "negative". 
Text: i'll bet the video game is a lot more fun than the film. 
Sentiment:
```

Explaining the desired audience is another smart way to give instructions

*   For example to produce education materials for kids,

```
Describe what is quantum physics to a 6-year-old.
```

*   And safe content,

```
... in language that is safe for work.
```

_In-context instruction learning_ ([Ye et al. 2023](https://arxiv.org/abs/2302.14691)) combines few-shot learning with instruction prompting. It incorporates multiple demonstration examples across different tasks in the prompt, each demonstration consisting of instruction, task input and output. Note that their experiments were only on classification tasks and the instruction prompt contains all label options.

```
Definition: Determine the speaker of the dialogue, "agent" or "customer".
Input: I have successfully booked your tickets.
Ouput: agent

Definition: Determine which category the question asks for, "Quantity" or "Location".
Input: What's the oldest building in US?
Ouput: Location

Definition: Classify the sentiment of the given movie review, "positive" or "negative".
Input: i'll bet the video game is a lot more fun than the film.
Output:
```

Self-Consistency Sampling
-------------------------

**Self-consistency sampling** ([Wang et al. 2022a](https://arxiv.org/abs/2203.11171)) is to sample multiple outputs with temperature \> 0 and then selecting the best one out of these candidates. The criteria for selecting the best candidate can vary from task to task. A general solution is to pick **majority vote**. For tasks that are easy to validate such as a programming question with unit tests, we can simply run through the interpreter and verify the correctness with unit tests.

Chain-of-Thought (CoT)
----------------------

**Chain-of-thought (CoT) prompting** ([Wei et al. 2022](https://arxiv.org/abs/2201.11903)) generates a sequence of short sentences to describe reasoning logics step by step, known as _reasoning chains_ or _rationales_, to eventually lead to the final answer. The benefit of CoT is more pronounced for **complicated reasoning tasks**, while using **large models** (e.g. with more than 50B parameters). Simple tasks only benefit slightly from CoT prompting.

Types of CoT prompts
--------------------

Two main types of CoT prompting:

*   **Few-shot CoT**. It is to prompt the model with a few demonstrations, each containing manually written (or model-generated) high-quality reasoning chains.

(All the math reasoning examples are from [GSM8k](https://github.com/openai/grade-school-math))

```
Question: Tom and Elizabeth have a competition to climb a hill. Elizabeth takes 30 minutes to climb the hill. Tom takes four times as long as Elizabeth does to climb the hill. How many hours does it take Tom to climb up the hill?
Answer: It takes Tom 30*4 = <<30*4=120>>120 minutes to climb the hill.
It takes Tom 120/60 = <<120/60=2>>2 hours to climb the hill.
So the answer is 2.
===
Question: Jack is a soccer player. He needs to buy two pairs of socks and a pair of soccer shoes. Each pair of socks cost $9.50, and the shoes cost $92. Jack has $40. How much more money does Jack need?
Answer: The total cost of two pairs of socks is $9.50 x 2 = $<<9.5*2=19>>19.
The total cost of the socks and the shoes is $19 + $92 = $<<19+92=111>>111.
Jack need $111 - $40 = $<<111-40=71>>71 more.
So the answer is 71.
===
Question: Marty has 100 centimeters of ribbon that he must cut into 4 equal parts. Each of the cut parts must be divided into 5 equal parts. How long will each final cut be?
Answer:
```

*   **Zero-shot CoT**. Use natural language statement like `Let's think step by step` to explicitly encourage the model to first generate reasoning chains and then to prompt with `Therefore, the answer is` to produce answers ([Kojima et al. 2022](https://arxiv.org/abs/2205.11916) ). Or a similar statement `Let's work this out it a step by step to be sure we have the right answer` ([Zhou et al. 2022](https://arxiv.org/abs/2211.01910)).

```
Question: Marty has 100 centimeters of ribbon that he must cut into 4 equal parts. Each of the cut parts must be divided into 5 equal parts. How long will each final cut be?
Answer: Let's think step by step.
```

Tips and Extensions
-------------------

*   [Self-consistency sampling](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering#self-consistency-sampling) can improve reasoning accuracy by sampling a number of diverse answers and then taking the majority vote. ([Wang et al. 2022a](https://arxiv.org/abs/2203.11171))
    
*   Another approach for ensemble learning is to alter the example order or use model generated rationales to replace human-written ones to introduce randomness during multiple sample trials. Then aggregate model outputs with a majority vote to get final answer. ([Wang et al. 2022b](https://arxiv.org/abs/2207.00747))
    
*   If training examples are only associated with true answers (easy to verify!) but no rationales, we can follow the _STaR_ (Self-Taught Reasoner; [Zelikman et al. 2022](https://arxiv.org/abs/2203.14465)) method : (1) Ask LLM to generate reasoning chains and only keep those leading to correct answers; (2) Then fine-tune the model with generated rationales and repeat the process until convergence. Note that higher temperature is more likely to generate incorrect rationales with correct answers. If training examples do not have ground truth answers, maybe consider using majority votes as the “correct” answers.
    
*   Prompts with demonstrations of higher reasoning complexity can achieve better performance, where complexity is measured by the number of reasoning steps in the chains. When separating reasoning steps, newline `\n` symbol works better than `step i`, period `.` or semicolon `;`. ([Fu et al. 2023](https://arxiv.org/abs/2210.00720))
    
*   _Complexity-based consistency_ is to explicitly prefer complex chains among all the generations by taking majority vote among only top $k$ complex chains. ([Fu et al. 2023](https://arxiv.org/abs/2210.00720))
    
*   Later, [Shum et al. (2023)](https://arxiv.org/abs/2302.12822) found that in their experiments CoT prompts with only complex examples can improve the accuracy of complex questions, but perform poorly in simple questions; evidence shown on GSM8k.
    
*   Changing `Q:` to `Question:` is found to be helpful. ([Fu et al. 2023](https://arxiv.org/abs/2210.00720))
    
*   [Ye & Durrett (2022)](https://arxiv.org/abs/2205.03401) found that the benefit of including explanations in the prompt is small to moderate for NLP tasks that involve reasoning over text (i.e. QA and NLI) and the effects vary by models. They observed that explanations are more likely to be nonfactual than be inconsistent (i.e. whether explanation entails prediction). Nonfactual explanations most likely lead to incorrect predictions.
    
*   _Self-Ask_ ([Press et al. 2022](https://arxiv.org/abs/2210.03350)) is a method to repeatedly prompt the model to _ask following-up questions_ to construct the thought process iteratively. Follow-up questions can be answered by search engine results. Similarly, _IRCoT_ (Interleaving Retrieval CoT; [Trivedi et al. 2022](https://arxiv.org/abs/2212.10509)) and _ReAct_ (Reason + Act; [Yao et al. 2023](https://arxiv.org/abs/2210.03629)) combines iterative CoT prompting with queries to Wikipedia APIs to search for relevant entities and content and then add it back into the context.
    

![Image 15](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/SelfAsk-search.png)

Fig. 1. How Self-Ask works with external search queries.  
(Image source: [Press et al. 2022](https://arxiv.org/abs/2210.03350)).

*   _Tree of Thoughts_ ([Yao et al. 2023](https://arxiv.org/abs/2305.10601)) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, essentially creating a tree structure. The search process can be BFS or DFS while each state is evaluated by a classifier (via a prompt) or majority vote.

![Image 16](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/tree-of-thoughts.png)

Fig. 2. How Self-Ask works with external search queries.  
(Image source: [Yao et al. 2022](https://arxiv.org/abs/2305.10601)).

Automatic Prompt Design
-----------------------

Prompt is a sequence of prefix tokens that increase the probability of getting desired output given input. Therefore we can treat them as trainable parameters and [optimize them directly](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/#smart-prompt-design) on the embedding space via gradient descent, such as **AutoPrompt** ([Shin et al., 2020](https://arxiv.org/abs/2010.15980), **Prefix-Tuning** ([Li & Liang (2021)](https://arxiv.org/abs/2101.00190)), **P-tuning** ([Liu et al. 2021](https://arxiv.org/abs/2103.10385)) and **Prompt-Tuning** ([Lester et al. 2021](https://arxiv.org/abs/2104.08691)). [This section in my “Controllable Neural Text Generation” post](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/#smart-prompt-design) has a good coverage of them. The trend from AutoPrompt to Prompt-Tuning is that the setup gets gradually simplified.

**APE** (Automatic Prompt Engineer; [Zhou et al. 2022](https://arxiv.org/abs/2211.01910)) is a method to search over a pool of model-generated instruction candidates and then filters the candidate set according to a chosen score function to ultimately choose the best candidate with highest score.

1.  Prompt LLM to generate instruction candidates based on a small set of demonstrations in the form of input-output pairs. E.g. `{{Given desired input-output pairs}}\n\nThe instruction is`.
    
2.  Given a dataset of $\\mathcal{D}\_\\text{train} = \\{(x, y)\\}$, we would like to find an instruction $\\rho$ such that $\\rho^\* = \\arg\\max\_\\rho \\mathbb{E}\_{(x, y) \\in \\mathcal{D}\_\\text{train}} \[f(\\rho, x, y)\]$, where $f(.)$ is a per-sample score function, such as execution accuracy $\\mathbb{1}\[\\text{LM}(.\\vert \\rho, x)=y\]$ or log probability: $p\_\\text{LM}(y \\mid \\rho, x)$.
    
3.  Use an iterative Monte Carlo search method to improve the best candidates by proposing semantically similar variants via prompts like `Generate a variation of the following instruction while keeping the semantic meaning.\n\nInput: ...\n\nOutput:...`
    

To construct chain-of-thought prompts automatically, [Shum et al. (2023)](https://arxiv.org/abs/2302.12822) suggested augment-prune-select, a three-step process:

1.  _Augment_: Generate multiple pseudo-chains of thought given question using few-shot or zero-shot CoT prompts;
2.  _Prune_: Prune pseudo chains based on whether generated answers match ground truths.
3.  _Select_: Apply a variance-reduced policy gradient strategy to learn the probability distribution over selected examples, while considering the probability distribution over examples as policy and the validation set accuracy as reward.

[Zhang et al. (2023)](https://arxiv.org/abs/2210.03493) instead adopted _clustering_ techniques to sample questions and then generates chains. They observed that LLMs tend to make certain types of mistakes. One type of errors can be similar in the emebedding space and thus get grouped together. By only sampling one or a few from frequent-error clusters, we can prevent too many wrong demonstrations of one error type and collect a diverse set of examples.

1.  _Question clustering_: Embed questions and run $k$-means for clustering.
2.  _Demonstration selection_: Select a set of representative questions from each cluster; i.e. one demonstration from one cluster. Samples in each cluster are sorted by distance to the cluster centroid and those closer to the centroid are selected first.
3.  _Rationale generation_: Use zero-shot CoT to generate reasoning chains for selected questions and construct few-shot prompt to run inference.

Augmented Language Models
-------------------------

A survey on augmented language models by [Mialon et al. (2023)](https://arxiv.org/abs/2302.07842) has great coverage over multiple categories of language models augmented with reasoning skills and the ability of using external tools. Recommend it.

Retrieval
---------

Often we need to complete tasks that require latest knowledge after the model pretraining time cutoff or internal/private knowledge base. In that case, the model would not know the context if we don’t explicitly provide it in the prompt. Many methods for [Open Domain Question Answering](https://lilianweng.github.io/posts/2020-10-29-odqa/) depend on first doing retrieval over a knowledge base and then incorporating the retrieved content as part of the prompt. The accuracy of such a process depends on the quality of both retrieval and generation steps.

[Lazaridou et al. (2022)](https://arxiv.org/abs/2203.05115) studied how to use Google Search for document retrieval to augment LLMs. Given a question $q$, clean text is extracted out of 20 URLs returned by Google, resulting in a set of documents. Because these documents are long, each document is split into paragraphs of 6 sentences, $\\{p\\}$. Paragraphs are ranked by TF-IDF based cosine similarity between evidence paragraphs and the query. Only the most relevant paragraph is used in the prompt to produce an answer $a$.

For closed-book QA, each demonstration is formatted as follows to construct few-shot prompts. Swapping the question with the evidence (longer distance between questions and answers) is found to consistently yield lower results across all datasets.

```
Evidence: ...
Question: ...
Answer: ...
```

The answer probability is computed in three ways:

1.  [RAG](https://lilianweng.github.io/posts/2020-10-29-odqa/#RAG) style, $p(a\_i \\mid q) = \\sum\_{i=1}^n p\_\\text{tf-idf} (p\_i \\mid q) \\cdot p\_\\text{LM}(a\_i \\mid q, p\_i)$, where $p\_\\text{tf-idf} (p\_i \\mid q)$ is the normalized cosine similarities between the TF-IDF passage and question representations.
2.  Noisy channel inference, $p(a\_i\\mid q) = \\frac{p\_\\text{LM}(q \\mid a\_i, p\_i) \\cdot p\_\\text{LM}(a\_i \\mid p\_i)}{p\_\\text{LM}(q \\mid p\_i)}$
3.  Product-of-Experts (PoE), combines all probabilities used above in addition to $p\_\\text{LM}(p\_i \\mid q)$.

According to their experiments on generation and classification tasks, among three answer reranking scores - PoE \> Noisy channel \> RAG. Among individual probabilities, $p\_\\text{LM}(a \\mid q, p\_i)$ and $p\_\\text{LM}(q \\mid p\_i, a)$ are found to be most informative. $p\_\\text{LM}(q \\mid p\_i, a)$ captures how well the question can be explained by LM given evidence paragraph and answer and can reliably be used for reranking answer candidates.

One observation with [SituatedQA](https://situatedqa.github.io/) dataset for questions grounded in different dates is that despite LM (pretraining cutoff is year 2020) has access to latest information via Google Search, its performance on post-2020 questions are still a lot _worse_ than on pre-2020 questions. This suggests the existence of some discrepencies or conflicting parametric between contextual information and model internal knowledge.

Interestingly it is found to be beneficial even with only “internal retrieval”, that is, to generate knowledge about a topic before answering the question ([Liu et al. 2022](https://arxiv.org/abs/2110.08387)). First we can use the following template to extract knowledge:

```
Generate some knowledge about the input. Examples:

Input: What type of water formation is formed by clouds?
Knowledge: Clouds are made of water vapor.

Input: {question}
Knowledge:
```

And then with model-generated knowledge, prompt the LM further to get the answer.

Programming Language
--------------------

Both **PAL** (Program-aided language models); [Gao et al. 2022](https://arxiv.org/abs/2211.10435)) and **PoT** (Program of Thoughts prompting; [Chen et al. 2022](https://arxiv.org/abs/2211.12588)) ask LLM to generate programming language statements to resolve natural language reasoning problems, hence offloading the solution step to a runtime such as a Python interpreter. Such setup decouples complex computation and reasoning. It relies on a LM with good enough coding skills.

![Image 17](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/PoT.png)

Fig. 3. Comparing CoT and PoT. (Image source: [Chen et al. 2022](https://arxiv.org/abs/2211.12588)).

External APIs
-------------

**TALM** (Tool Augmented Language Models; [Parisi et al. 2022](https://arxiv.org/abs/2205.12255)) is a language model augmented with text-to-text API calls. LM is guided to generate `|tool-call` and `tool input text` conditioned on task input text to construct API call requests. When `|result` shows up, the specified tool API is called and the returned result gets appended to the text sequence. The final output is generated following `|output` token.

![Image 18](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/TALM.png)

Fig. 4. The format of API calls in TALM. (Image source: [Parisi et al. 2022](https://arxiv.org/abs/2205.12255)).

TALM adopts a self-play approach to iteratively bootstrap the dataset of tool use examples and finetune LM with it. This self-play, defined as a model interacting with a tool API, iteratively expands the dataset based on whether a newly added tool API can improve the model outputs. Same idea is adopted in Toolformer too, described in more details below. The pipeline loosely mimics a RL process where LM is the policy network and it is trained by policy gradient with a binary reward signal.

![Image 19](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/TALM-iteration.png)

Fig. 5. Self-play iterations help boost the model performance.  
(Image source: [Parisi et al. 2022](https://arxiv.org/abs/2205.12255)).

**Toolformer** ([Schick et al. 2023](https://arxiv.org/abs/2302.04761)) is a LM that can use external tools via simple APIs, which is built in a self-supervised manner and only requires a handful of demonstrations for each API. The toolbox of Toolformer includes:

*   _Calculator_ to help LM with the lack of precise math skills;
*   _Q&A system_ to help with unfaithful content and hallucination;
*   _Search engine_ to provide up-to-date information after pretraining cut off time;
*   _Translation system_ to improve performance on low resource language;
*   _Calendar_ to make LM be aware of time progression.

![Image 20](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/toolformer.png)

Fig. 6. Illustration of how to build Toolformer.  
(Image source: [Schick et al. 2023](https://arxiv.org/abs/2302.04761)).

Toolformer is trained as follows:

1.  _Prompting to annotate potential API calls_. Ask a pre-trained LM to annotate a dataset via few-shot learning with API call usage examples. Formatting example:
    
    ![Image 21](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/toolformer-annotation.png)
    
    Fig. 7. How dataset is annotated to do API calls.  
    (Image source: [Schick et al. 2023](https://arxiv.org/abs/2302.04761)).
    
    *   Each API call is represented as a tuple of (API name, corresponding input), $c=(a\_c, i\_c)$ and its corresponding result is denoted as $r$. The API call sequences with and without results are labeled as follows, respectively:
        
        $$ \\begin{aligned} e(c) &\= \\langle\\texttt{API}\\rangle a\_c(i\_c) \\langle\\texttt{/API}\\rangle \\\\ e(c, r) &\= \\langle\\texttt{API}\\rangle a\_c(i\_c) \\to r \\langle\\texttt{/API}\\rangle \\end{aligned} $$
        
    *   Sample API calls based on the probabilities $p\_\\text{LM}(\\langle\\texttt{API}\\rangle \\mid \\text{prompt}(\\mathbf{x}), \\mathbf{x}\_{1:i})$ and select top $k$ candidate positions for doing API calls at position $i$ if the probability is larger than a threshold.
        
    *   Then we sample potential API calls from the LM given the sequence $\[\\text{prompt}(\\mathbf{x}), x\_1, \\dots, x\_{i-1}, \\langle\\texttt{API}\\rangle\]$ as prefix and $\\langle\\texttt{/API}\\rangle$ as suffix.
        
2.  _Filter annotations based on whether API calls help model predict future tokens._ Use a self-supervised loss to decide which API calls are actually helpful.
    
    *   Execute each API call $c\_i$ to get corresponding result $r\_i$.
        
    *   Compute weighted cross entropy loss for the LM over tokens $x\_i, \\dots, x\_n$ when the model is prefixed with the prompt. Two versions are computed, one with API result and the other with empty sequence $\\varepsilon$.
        
        $$ \\begin{aligned} L^+\_i &\= L\_i(e(c\_i, r\_i)) \\\\ L^-\_i &\= \\min(L\_i(\\varepsilon), L\_i(e(c\_i, \\varepsilon))) \\\\ \\end{aligned} $$
        
        Only API calls with $L^-\_i - L^+\_i$ larger than a threshold are kept, meaning that adding this API call and its results help the model predict future tokens.
        
3.  _Fine-tune LM on this annotated dataset._ The new training sequences are constructed as $\\mathbf{x}^\* = x\_{1:i-1}, e(c\_i, r\_i), x\_{i:n}$ . The training data is a combination of the original dataset (e.g. a subset of CCNet, as in the paper) and its augmented version.
    

At inference time, decoding runs until the model produces “$\\to$ " token, indicating that it is expecting response from an API call next.

Toolformer currently does not support tool use in a chain (i.e. using the output of one tool as an input for another tool) or in an interactive way (i.e. adopt API response after human selection). Both are interesting future directions to expand the model for.

Citation
--------

Cited as:

> Weng, Lilian. (Mar 2023). Prompt Engineering. Lil’Log. https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/.

Or

```
@article{weng2023prompt,
  title   = "Prompt Engineering",
  author  = "Weng, Lilian",
  journal = "lilianweng.github.io",
  year    = "2023",
  month   = "Mar",
  url     = "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/"
}
```

Useful Resources
----------------

*   [OpenAI Cookbook](https://github.com/openai/openai-cookbook) has many in-depth examples for how to utilize LLM efficiently.
*   [LangChain](https://langchain.readthedocs.io/en/latest/), a library for combining language models with other components to build applications.
*   [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) repo contains a pretty comprehensive collection of education materials on prompt engineering.
*   [learnprompting.org](https://learnprompting.org/docs/intro)
*   [PromptPerfect](https://promptperfect.jina.ai/)
*   [Semantic Kernel](https://github.com/microsoft/semantic-kernel)

References
----------

\[1\] Zhao et al. [“Calibrate Before Use: Improving Few-shot Performance of Language Models.”](https://arxiv.org/abs/2102.09690) ICML 2021

\[2\] Liu et al. [“What Makes Good In-Context Examples for GPT-3?”](https://arxiv.org/abs/2101.06804) arXiv preprint arXiv:2101.06804 (2021).

\[3\] Lu et al. [“Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity.”](https://arxiv.org/abs/2104.08786) ACL 2022

\[4\] Ye et al. [“In-Context Instruction Learning.”](https://arxiv.org/abs/2302.14691) arXiv preprint arXiv:2302.14691 (2023).

\[5\] Su et al. [“Selective annotation makes language models better few-shot learners.”](https://arxiv.org/abs/2209.01975) arXiv preprint arXiv:2209.01975 (2022).

\[6\] Rubin et al. [“Learning to retrieve prompts for in-context learning.”](https://arxiv.org/abs/2112.08633) NAACL-HLT 2022

\[7\] Wei et al. [“Chain of thought prompting elicits reasoning in large language models.”](https://arxiv.org/abs/2201.11903) NeurIPS 2022

\[8\] Wang et al. [“Self-Consistency Improves Chain of Thought Reasoning in Language Models.”](https://arxiv.org/abs/2203.11171) ICLR 2023.

\[9\] Diao et al. [“Active Prompting with Chain-of-Thought for Large Language Models.”](https://arxiv.org/abs/2302.12246) arXiv preprint arXiv:2302.12246 (2023).

\[10\] Zelikman et al. [“STaR: Bootstrapping Reasoning With Reasoning.”](https://arxiv.org/abs/2203.14465) arXiv preprint arXiv:2203.14465 (2022).

\[11\] Ye & Durrett. [“The unreliability of explanations in few-shot in-context learning.”](https://arxiv.org/abs/2205.03401) arXiv preprint arXiv:2205.03401 (2022).

\[12\] Trivedi et al. [“Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions.”](https://arxiv.org/abs/2212.10509) arXiv preprint arXiv:2212.10509 (2022).

\[13\] Press et al. [“Measuring and narrowing the compositionality gap in language models.”](https://arxiv.org/abs/2210.03350) arXiv preprint arXiv:2210.03350 (2022).

\[14\] Yao et al. [“ReAct: Synergizing reasoning and acting in language models.”](https://arxiv.org/abs/2210.03629) ICLR 2023.

\[15\] Fu et al. [“Complexity-based prompting for multi-step reasoning.”](https://arxiv.org/abs/2210.00720) arXiv preprint arXiv:2210.00720 (2022).

\[16\] Wang et al. [“Rationale-augmented ensembles in language models.”](https://arxiv.org/abs/2207.00747) arXiv preprint arXiv:2207.00747 (2022).

\[17\] Zhang et al. [“Automatic chain of thought prompting in large language models.”](https://arxiv.org/abs/2210.03493) arXiv preprint arXiv:2210.03493 (2022).

\[18\] Shum et al. [“Automatic Prompt Augmentation and Selection with Chain-of-Thought from Labeled Data.”](https://arxiv.org/abs/2302.12822) arXiv preprint arXiv:2302.12822 (2023).

\[19\] Zhou et al. [“Large Language Models Are Human-Level Prompt Engineers.”](https://arxiv.org/abs/2211.01910) ICLR 2023.

\[20\] Lazaridou et al. [“Internet augmented language models through few-shot prompting for open-domain question answering.”](https://arxiv.org/abs/2203.05115) arXiv preprint arXiv:2203.05115 (2022).

\[21\] Chen et al. [“Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks.”](https://arxiv.org/abs/2211.12588) arXiv preprint arXiv:2211.12588 (2022).

\[22\] Gao et al. [“PAL: Program-aided language models.”](https://arxiv.org/abs/2211.10435) arXiv preprint arXiv:2211.10435 (2022).

\[23\] Parisi et al. [“TALM: Tool Augmented Language Models”](https://arxiv.org/abs/2205.12255) arXiv preprint arXiv:2205.12255 (2022).

\[24\] Schick et al. [“Toolformer: Language Models Can Teach Themselves to Use Tools.”](https://arxiv.org/abs/2302.04761) arXiv preprint arXiv:2302.04761 (2023).

\[25\] Mialon et al. [“Augmented Language Models: a Survey”](https://arxiv.org/abs/2302.07842) arXiv preprint arXiv:2302.07842 (2023).

\[26\] Yao et al. [“Tree of Thoughts: Deliberate Problem Solving with Large Language Models.”](https://arxiv.org/abs/2305.10601) arXiv preprint arXiv:2305.10601 (2023).

## Metadata

```json
{
  "title": "Prompt Engineering",
  "description": "Prompt Engineering, also known as In-Context Prompting, refers to methods for how to communicate with LLM to steer its behavior for desired outcomes without updating the model weights. It is an empirical science and the effect of prompt engineering methods can vary a lot among models, thus requiring heavy experimentation and heuristics.\nThis post only focuses on prompt engineering for autoregressive language models, so nothing with Cloze tests, image generation or multimodality models. At its core, the goal of prompt engineering is about alignment and model steerability. Check my previous post on controllable text generation.",
  "url": "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering",
  "content": "**Prompt Engineering**, also known as **In-Context Prompting**, refers to methods for how to communicate with LLM to steer its behavior for desired outcomes _without_ updating the model weights. It is an empirical science and the effect of prompt engineering methods can vary a lot among models, thus requiring heavy experimentation and heuristics.\n\nThis post only focuses on prompt engineering for autoregressive language models, so nothing with Cloze tests, image generation or multimodality models. At its core, the goal of prompt engineering is about alignment and model steerability. Check my [previous post](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/) on controllable text generation.\n\n\\[My personal spicy take\\] In my opinion, some prompt engineering papers are not worthy 8 pages long, since those tricks can be explained in one or a few sentences and the rest is all about benchmarking. An easy-to-use and shared benchmark infrastructure should be more beneficial to the community. Iterative prompting or external tool use would not be trivial to set up. Also non-trivial to align the whole research community to adopt it.\n\nBasic Prompting\n---------------\n\nZero-shot and few-shot learning are two most basic approaches for prompting the model, pioneered by many LLM papers and commonly used for benchmarking LLM performance.\n\nZero-Shot\n---------\n\n**Zero-shot learning** is to simply feed the task text to the model and ask for results.\n\n(All the sentiment analysis examples are from SST-2)\n\n```\nText: i'll bet the video game is a lot more fun than the film.\nSentiment:\n```\n\nFew-shot\n--------\n\n**Few-shot learning** presents a set of high-quality demonstrations, each consisting of both input and desired output, on the target task. As the model first sees good examples, it can better understand human intention and criteria for what kinds of answers are wanted. Therefore, few-shot learning often leads to better performance than zero-shot. However, it comes at the cost of more token consumption and may hit the context length limit when input and output text are long.\n\n```\nText: (lawrence bounces) all over the stage, dancing, running, sweating, mopping his face and generally displaying the wacky talent that brought him fame in the first place.\nSentiment: positive\n\nText: despite all evidence to the contrary, this clunker has somehow managed to pose as an actual feature movie, the kind that charges full admission and gets hyped on tv and purports to amuse small children and ostensible adults.\nSentiment: negative\n\nText: for the first time in years, de niro digs deep emotionally, perhaps because he's been stirred by the powerful work of his co-stars.\nSentiment: positive\n\nText: i'll bet the video game is a lot more fun than the film.\nSentiment:\n```\n\nMany studies looked into how to construct in-context examples to maximize the performance and observed that **choice of prompt format, training examples, and the order of the examples can lead to dramatically different performance**, from near random guess to near SoTA.\n\n[Zhao et al. (2021)](https://arxiv.org/abs/2102.09690) investigated the case of few-shot classification and proposed that several biases with LLM (they use GPT-3 in the experiments) contribute to such high variance: (1) _Majority label bias_ exists if distribution of labels among the examples is unbalanced; (2) _Recency bias_ refers to the tendency where the model may repeat the label at the end; (3) _Common token bias_ indicates that LLM tends to produce common tokens more often than rare tokens. To conquer such bias, they proposed a method to calibrate the label probabilities output by the model to be uniform when the input string is `N/A`.\n\n### Tips for Example Selection\n\n*   Choose examples that are semantically similar to the test example using $k$-NN clustering in the embedding space ([Liu et al., 2021](https://arxiv.org/abs/2101.06804))\n    \n*   To select a diverse and representative set of examples, [Su et al. (2022)](https://arxiv.org/abs/2209.01975) proposed to use a graph-based approach: (1) First, construct a directed graph $G=(V, E)$ based on the embedding (e.g. by [SBERT](https://arxiv.org/abs/1908.10084) or [other](https://arxiv.org/abs/2201.10005) [embedding](https://platform.openai.com/docs/guides/embeddings) [models](https://openai.com/blog/new-and-improved-embedding-model)) cosine similarity between samples, where each node points to its $k$ nearest neighbors; (2) Start with a set of selected samples $\\\\mathcal{L}=\\\\emptyset$ and a set of remaining samples $\\\\mathcal{U}$. Each sample $u \\\\in \\\\mathcal{U}$ is scored by $$ \\\\text{score}(u) = \\\\sum\\_{v \\\\in \\\\{v \\\\mid (u, v) \\\\in E, v\\\\in \\\\mathcal{U}\\\\}} s(v)\\\\quad\\\\text{where }s(v)=\\\\rho^{- \\\\vert \\\\{\\\\ell \\\\in \\\\mathcal{L} \\\\vert (v, \\\\ell)\\\\in E \\\\}\\\\vert},\\\\quad\\\\rho \\> 1 $$ such that $s(v)$ is low if many of $v$’s neighbors are selected and thus the scoring encourages to pick diverse samples.\n    \n*   [Rubin et al. (2022)](https://arxiv.org/abs/2112.08633) proposed to train embeddings via [contrastive learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/) specific to one training dataset for in-context learning sample selection. Given each training pair $(x, y)$, the quality of one example $e\\_i$ (formatted input-output pair) can be measured by a conditioned probability assigned by LM: $\\\\text{score}(e\\_i) = P\\_\\\\text{LM}(y \\\\mid e\\_i, x)$. We can identify other examples with top-$k$ and bottom-$k$ scores as positive and negative sets of candidates for every training pair and use that for contrastive learning.\n    \n*   Some researchers tried [Q-Learning](https://lilianweng.github.io/posts/2018-02-19-rl-overview/#q-learning-off-policy-td-control) to do sample selection. ([Zhang et al. 2022](https://arxiv.org/abs/2211.04486))\n    \n*   Motivated by uncertainty-based [active learning](https://lilianweng.github.io/posts/2022-02-20-active-learning/), [Diao et al. (2023)](https://arxiv.org/abs/2302.12246) suggested to identify examples with high disagreement or entropy among multiple sampling trials. Then annotate these examples to be used in few-shot prompts.\n    \n\n### Tips for Example Ordering\n\n*   A general suggestion is to keep the selection of examples diverse, relevant to the test sample and in random order to avoid majority label bias and recency bias.\n*   Increasing model sizes or including more training examples does not reduce variance among different permutations of in-context examples. Same order may work well for one model but badly for another. When the validation set is limited, consider choosing the order such that the model does not produce extremely unbalanced predictions or being overconfident about its predictions. ([Lu et al. 2022](https://arxiv.org/abs/2104.08786))\n\nInstruction Prompting\n---------------------\n\nThe purpose of presenting few-shot examples in the prompt is to explain our intent to the model; in other words, describe the task instruction to the model in the form of demonstrations. However, few-shot can be expensive in terms of token usage and restricts the input length due to limited context length. So, why not just give the instruction directly?\n\n_Instructed LM_ (e.g. [InstructGPT](https://openai.com/research/instruction-following), [natural instruction](https://github.com/allenai/natural-instructions)) finetunes a pretrained model with high-quality tuples of (task instruction, input, ground truth output) to make LM better understand user intention and follow instruction. [RLHF](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/#rl-fine-tuning-with-human-preferences) (Reinforcement Learning from Human Feedback) is a common method to do so. The benefit of instruction following style fine-tuning improves the model to be more aligned with human intention and greatly reduces the cost of communication.\n\nWhen interacting with instruction models, we should describe the task requirement in details, trying to be _specific_ and _precise_ and avoiding say “not do something” but rather specify what to do.\n\n```\nPlease label the sentiment towards the movie of the given movie review. The sentiment label should be \"positive\" or \"negative\". \nText: i'll bet the video game is a lot more fun than the film. \nSentiment:\n```\n\nExplaining the desired audience is another smart way to give instructions\n\n*   For example to produce education materials for kids,\n\n```\nDescribe what is quantum physics to a 6-year-old.\n```\n\n*   And safe content,\n\n```\n... in language that is safe for work.\n```\n\n_In-context instruction learning_ ([Ye et al. 2023](https://arxiv.org/abs/2302.14691)) combines few-shot learning with instruction prompting. It incorporates multiple demonstration examples across different tasks in the prompt, each demonstration consisting of instruction, task input and output. Note that their experiments were only on classification tasks and the instruction prompt contains all label options.\n\n```\nDefinition: Determine the speaker of the dialogue, \"agent\" or \"customer\".\nInput: I have successfully booked your tickets.\nOuput: agent\n\nDefinition: Determine which category the question asks for, \"Quantity\" or \"Location\".\nInput: What's the oldest building in US?\nOuput: Location\n\nDefinition: Classify the sentiment of the given movie review, \"positive\" or \"negative\".\nInput: i'll bet the video game is a lot more fun than the film.\nOutput:\n```\n\nSelf-Consistency Sampling\n-------------------------\n\n**Self-consistency sampling** ([Wang et al. 2022a](https://arxiv.org/abs/2203.11171)) is to sample multiple outputs with temperature \\> 0 and then selecting the best one out of these candidates. The criteria for selecting the best candidate can vary from task to task. A general solution is to pick **majority vote**. For tasks that are easy to validate such as a programming question with unit tests, we can simply run through the interpreter and verify the correctness with unit tests.\n\nChain-of-Thought (CoT)\n----------------------\n\n**Chain-of-thought (CoT) prompting** ([Wei et al. 2022](https://arxiv.org/abs/2201.11903)) generates a sequence of short sentences to describe reasoning logics step by step, known as _reasoning chains_ or _rationales_, to eventually lead to the final answer. The benefit of CoT is more pronounced for **complicated reasoning tasks**, while using **large models** (e.g. with more than 50B parameters). Simple tasks only benefit slightly from CoT prompting.\n\nTypes of CoT prompts\n--------------------\n\nTwo main types of CoT prompting:\n\n*   **Few-shot CoT**. It is to prompt the model with a few demonstrations, each containing manually written (or model-generated) high-quality reasoning chains.\n\n(All the math reasoning examples are from [GSM8k](https://github.com/openai/grade-school-math))\n\n```\nQuestion: Tom and Elizabeth have a competition to climb a hill. Elizabeth takes 30 minutes to climb the hill. Tom takes four times as long as Elizabeth does to climb the hill. How many hours does it take Tom to climb up the hill?\nAnswer: It takes Tom 30*4 = <<30*4=120>>120 minutes to climb the hill.\nIt takes Tom 120/60 = <<120/60=2>>2 hours to climb the hill.\nSo the answer is 2.\n===\nQuestion: Jack is a soccer player. He needs to buy two pairs of socks and a pair of soccer shoes. Each pair of socks cost $9.50, and the shoes cost $92. Jack has $40. How much more money does Jack need?\nAnswer: The total cost of two pairs of socks is $9.50 x 2 = $<<9.5*2=19>>19.\nThe total cost of the socks and the shoes is $19 + $92 = $<<19+92=111>>111.\nJack need $111 - $40 = $<<111-40=71>>71 more.\nSo the answer is 71.\n===\nQuestion: Marty has 100 centimeters of ribbon that he must cut into 4 equal parts. Each of the cut parts must be divided into 5 equal parts. How long will each final cut be?\nAnswer:\n```\n\n*   **Zero-shot CoT**. Use natural language statement like `Let's think step by step` to explicitly encourage the model to first generate reasoning chains and then to prompt with `Therefore, the answer is` to produce answers ([Kojima et al. 2022](https://arxiv.org/abs/2205.11916) ). Or a similar statement `Let's work this out it a step by step to be sure we have the right answer` ([Zhou et al. 2022](https://arxiv.org/abs/2211.01910)).\n\n```\nQuestion: Marty has 100 centimeters of ribbon that he must cut into 4 equal parts. Each of the cut parts must be divided into 5 equal parts. How long will each final cut be?\nAnswer: Let's think step by step.\n```\n\nTips and Extensions\n-------------------\n\n*   [Self-consistency sampling](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering#self-consistency-sampling) can improve reasoning accuracy by sampling a number of diverse answers and then taking the majority vote. ([Wang et al. 2022a](https://arxiv.org/abs/2203.11171))\n    \n*   Another approach for ensemble learning is to alter the example order or use model generated rationales to replace human-written ones to introduce randomness during multiple sample trials. Then aggregate model outputs with a majority vote to get final answer. ([Wang et al. 2022b](https://arxiv.org/abs/2207.00747))\n    \n*   If training examples are only associated with true answers (easy to verify!) but no rationales, we can follow the _STaR_ (Self-Taught Reasoner; [Zelikman et al. 2022](https://arxiv.org/abs/2203.14465)) method : (1) Ask LLM to generate reasoning chains and only keep those leading to correct answers; (2) Then fine-tune the model with generated rationales and repeat the process until convergence. Note that higher temperature is more likely to generate incorrect rationales with correct answers. If training examples do not have ground truth answers, maybe consider using majority votes as the “correct” answers.\n    \n*   Prompts with demonstrations of higher reasoning complexity can achieve better performance, where complexity is measured by the number of reasoning steps in the chains. When separating reasoning steps, newline `\\n` symbol works better than `step i`, period `.` or semicolon `;`. ([Fu et al. 2023](https://arxiv.org/abs/2210.00720))\n    \n*   _Complexity-based consistency_ is to explicitly prefer complex chains among all the generations by taking majority vote among only top $k$ complex chains. ([Fu et al. 2023](https://arxiv.org/abs/2210.00720))\n    \n*   Later, [Shum et al. (2023)](https://arxiv.org/abs/2302.12822) found that in their experiments CoT prompts with only complex examples can improve the accuracy of complex questions, but perform poorly in simple questions; evidence shown on GSM8k.\n    \n*   Changing `Q:` to `Question:` is found to be helpful. ([Fu et al. 2023](https://arxiv.org/abs/2210.00720))\n    \n*   [Ye & Durrett (2022)](https://arxiv.org/abs/2205.03401) found that the benefit of including explanations in the prompt is small to moderate for NLP tasks that involve reasoning over text (i.e. QA and NLI) and the effects vary by models. They observed that explanations are more likely to be nonfactual than be inconsistent (i.e. whether explanation entails prediction). Nonfactual explanations most likely lead to incorrect predictions.\n    \n*   _Self-Ask_ ([Press et al. 2022](https://arxiv.org/abs/2210.03350)) is a method to repeatedly prompt the model to _ask following-up questions_ to construct the thought process iteratively. Follow-up questions can be answered by search engine results. Similarly, _IRCoT_ (Interleaving Retrieval CoT; [Trivedi et al. 2022](https://arxiv.org/abs/2212.10509)) and _ReAct_ (Reason + Act; [Yao et al. 2023](https://arxiv.org/abs/2210.03629)) combines iterative CoT prompting with queries to Wikipedia APIs to search for relevant entities and content and then add it back into the context.\n    \n\n![Image 15](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/SelfAsk-search.png)\n\nFig. 1. How Self-Ask works with external search queries.  \n(Image source: [Press et al. 2022](https://arxiv.org/abs/2210.03350)).\n\n*   _Tree of Thoughts_ ([Yao et al. 2023](https://arxiv.org/abs/2305.10601)) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, essentially creating a tree structure. The search process can be BFS or DFS while each state is evaluated by a classifier (via a prompt) or majority vote.\n\n![Image 16](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/tree-of-thoughts.png)\n\nFig. 2. How Self-Ask works with external search queries.  \n(Image source: [Yao et al. 2022](https://arxiv.org/abs/2305.10601)).\n\nAutomatic Prompt Design\n-----------------------\n\nPrompt is a sequence of prefix tokens that increase the probability of getting desired output given input. Therefore we can treat them as trainable parameters and [optimize them directly](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/#smart-prompt-design) on the embedding space via gradient descent, such as **AutoPrompt** ([Shin et al., 2020](https://arxiv.org/abs/2010.15980), **Prefix-Tuning** ([Li & Liang (2021)](https://arxiv.org/abs/2101.00190)), **P-tuning** ([Liu et al. 2021](https://arxiv.org/abs/2103.10385)) and **Prompt-Tuning** ([Lester et al. 2021](https://arxiv.org/abs/2104.08691)). [This section in my “Controllable Neural Text Generation” post](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/#smart-prompt-design) has a good coverage of them. The trend from AutoPrompt to Prompt-Tuning is that the setup gets gradually simplified.\n\n**APE** (Automatic Prompt Engineer; [Zhou et al. 2022](https://arxiv.org/abs/2211.01910)) is a method to search over a pool of model-generated instruction candidates and then filters the candidate set according to a chosen score function to ultimately choose the best candidate with highest score.\n\n1.  Prompt LLM to generate instruction candidates based on a small set of demonstrations in the form of input-output pairs. E.g. `{{Given desired input-output pairs}}\\n\\nThe instruction is`.\n    \n2.  Given a dataset of $\\\\mathcal{D}\\_\\\\text{train} = \\\\{(x, y)\\\\}$, we would like to find an instruction $\\\\rho$ such that $\\\\rho^\\* = \\\\arg\\\\max\\_\\\\rho \\\\mathbb{E}\\_{(x, y) \\\\in \\\\mathcal{D}\\_\\\\text{train}} \\[f(\\\\rho, x, y)\\]$, where $f(.)$ is a per-sample score function, such as execution accuracy $\\\\mathbb{1}\\[\\\\text{LM}(.\\\\vert \\\\rho, x)=y\\]$ or log probability: $p\\_\\\\text{LM}(y \\\\mid \\\\rho, x)$.\n    \n3.  Use an iterative Monte Carlo search method to improve the best candidates by proposing semantically similar variants via prompts like `Generate a variation of the following instruction while keeping the semantic meaning.\\n\\nInput: ...\\n\\nOutput:...`\n    \n\nTo construct chain-of-thought prompts automatically, [Shum et al. (2023)](https://arxiv.org/abs/2302.12822) suggested augment-prune-select, a three-step process:\n\n1.  _Augment_: Generate multiple pseudo-chains of thought given question using few-shot or zero-shot CoT prompts;\n2.  _Prune_: Prune pseudo chains based on whether generated answers match ground truths.\n3.  _Select_: Apply a variance-reduced policy gradient strategy to learn the probability distribution over selected examples, while considering the probability distribution over examples as policy and the validation set accuracy as reward.\n\n[Zhang et al. (2023)](https://arxiv.org/abs/2210.03493) instead adopted _clustering_ techniques to sample questions and then generates chains. They observed that LLMs tend to make certain types of mistakes. One type of errors can be similar in the emebedding space and thus get grouped together. By only sampling one or a few from frequent-error clusters, we can prevent too many wrong demonstrations of one error type and collect a diverse set of examples.\n\n1.  _Question clustering_: Embed questions and run $k$-means for clustering.\n2.  _Demonstration selection_: Select a set of representative questions from each cluster; i.e. one demonstration from one cluster. Samples in each cluster are sorted by distance to the cluster centroid and those closer to the centroid are selected first.\n3.  _Rationale generation_: Use zero-shot CoT to generate reasoning chains for selected questions and construct few-shot prompt to run inference.\n\nAugmented Language Models\n-------------------------\n\nA survey on augmented language models by [Mialon et al. (2023)](https://arxiv.org/abs/2302.07842) has great coverage over multiple categories of language models augmented with reasoning skills and the ability of using external tools. Recommend it.\n\nRetrieval\n---------\n\nOften we need to complete tasks that require latest knowledge after the model pretraining time cutoff or internal/private knowledge base. In that case, the model would not know the context if we don’t explicitly provide it in the prompt. Many methods for [Open Domain Question Answering](https://lilianweng.github.io/posts/2020-10-29-odqa/) depend on first doing retrieval over a knowledge base and then incorporating the retrieved content as part of the prompt. The accuracy of such a process depends on the quality of both retrieval and generation steps.\n\n[Lazaridou et al. (2022)](https://arxiv.org/abs/2203.05115) studied how to use Google Search for document retrieval to augment LLMs. Given a question $q$, clean text is extracted out of 20 URLs returned by Google, resulting in a set of documents. Because these documents are long, each document is split into paragraphs of 6 sentences, $\\\\{p\\\\}$. Paragraphs are ranked by TF-IDF based cosine similarity between evidence paragraphs and the query. Only the most relevant paragraph is used in the prompt to produce an answer $a$.\n\nFor closed-book QA, each demonstration is formatted as follows to construct few-shot prompts. Swapping the question with the evidence (longer distance between questions and answers) is found to consistently yield lower results across all datasets.\n\n```\nEvidence: ...\nQuestion: ...\nAnswer: ...\n```\n\nThe answer probability is computed in three ways:\n\n1.  [RAG](https://lilianweng.github.io/posts/2020-10-29-odqa/#RAG) style, $p(a\\_i \\\\mid q) = \\\\sum\\_{i=1}^n p\\_\\\\text{tf-idf} (p\\_i \\\\mid q) \\\\cdot p\\_\\\\text{LM}(a\\_i \\\\mid q, p\\_i)$, where $p\\_\\\\text{tf-idf} (p\\_i \\\\mid q)$ is the normalized cosine similarities between the TF-IDF passage and question representations.\n2.  Noisy channel inference, $p(a\\_i\\\\mid q) = \\\\frac{p\\_\\\\text{LM}(q \\\\mid a\\_i, p\\_i) \\\\cdot p\\_\\\\text{LM}(a\\_i \\\\mid p\\_i)}{p\\_\\\\text{LM}(q \\\\mid p\\_i)}$\n3.  Product-of-Experts (PoE), combines all probabilities used above in addition to $p\\_\\\\text{LM}(p\\_i \\\\mid q)$.\n\nAccording to their experiments on generation and classification tasks, among three answer reranking scores - PoE \\> Noisy channel \\> RAG. Among individual probabilities, $p\\_\\\\text{LM}(a \\\\mid q, p\\_i)$ and $p\\_\\\\text{LM}(q \\\\mid p\\_i, a)$ are found to be most informative. $p\\_\\\\text{LM}(q \\\\mid p\\_i, a)$ captures how well the question can be explained by LM given evidence paragraph and answer and can reliably be used for reranking answer candidates.\n\nOne observation with [SituatedQA](https://situatedqa.github.io/) dataset for questions grounded in different dates is that despite LM (pretraining cutoff is year 2020) has access to latest information via Google Search, its performance on post-2020 questions are still a lot _worse_ than on pre-2020 questions. This suggests the existence of some discrepencies or conflicting parametric between contextual information and model internal knowledge.\n\nInterestingly it is found to be beneficial even with only “internal retrieval”, that is, to generate knowledge about a topic before answering the question ([Liu et al. 2022](https://arxiv.org/abs/2110.08387)). First we can use the following template to extract knowledge:\n\n```\nGenerate some knowledge about the input. Examples:\n\nInput: What type of water formation is formed by clouds?\nKnowledge: Clouds are made of water vapor.\n\nInput: {question}\nKnowledge:\n```\n\nAnd then with model-generated knowledge, prompt the LM further to get the answer.\n\nProgramming Language\n--------------------\n\nBoth **PAL** (Program-aided language models); [Gao et al. 2022](https://arxiv.org/abs/2211.10435)) and **PoT** (Program of Thoughts prompting; [Chen et al. 2022](https://arxiv.org/abs/2211.12588)) ask LLM to generate programming language statements to resolve natural language reasoning problems, hence offloading the solution step to a runtime such as a Python interpreter. Such setup decouples complex computation and reasoning. It relies on a LM with good enough coding skills.\n\n![Image 17](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/PoT.png)\n\nFig. 3. Comparing CoT and PoT. (Image source: [Chen et al. 2022](https://arxiv.org/abs/2211.12588)).\n\nExternal APIs\n-------------\n\n**TALM** (Tool Augmented Language Models; [Parisi et al. 2022](https://arxiv.org/abs/2205.12255)) is a language model augmented with text-to-text API calls. LM is guided to generate `|tool-call` and `tool input text` conditioned on task input text to construct API call requests. When `|result` shows up, the specified tool API is called and the returned result gets appended to the text sequence. The final output is generated following `|output` token.\n\n![Image 18](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/TALM.png)\n\nFig. 4. The format of API calls in TALM. (Image source: [Parisi et al. 2022](https://arxiv.org/abs/2205.12255)).\n\nTALM adopts a self-play approach to iteratively bootstrap the dataset of tool use examples and finetune LM with it. This self-play, defined as a model interacting with a tool API, iteratively expands the dataset based on whether a newly added tool API can improve the model outputs. Same idea is adopted in Toolformer too, described in more details below. The pipeline loosely mimics a RL process where LM is the policy network and it is trained by policy gradient with a binary reward signal.\n\n![Image 19](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/TALM-iteration.png)\n\nFig. 5. Self-play iterations help boost the model performance.  \n(Image source: [Parisi et al. 2022](https://arxiv.org/abs/2205.12255)).\n\n**Toolformer** ([Schick et al. 2023](https://arxiv.org/abs/2302.04761)) is a LM that can use external tools via simple APIs, which is built in a self-supervised manner and only requires a handful of demonstrations for each API. The toolbox of Toolformer includes:\n\n*   _Calculator_ to help LM with the lack of precise math skills;\n*   _Q&A system_ to help with unfaithful content and hallucination;\n*   _Search engine_ to provide up-to-date information after pretraining cut off time;\n*   _Translation system_ to improve performance on low resource language;\n*   _Calendar_ to make LM be aware of time progression.\n\n![Image 20](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/toolformer.png)\n\nFig. 6. Illustration of how to build Toolformer.  \n(Image source: [Schick et al. 2023](https://arxiv.org/abs/2302.04761)).\n\nToolformer is trained as follows:\n\n1.  _Prompting to annotate potential API calls_. Ask a pre-trained LM to annotate a dataset via few-shot learning with API call usage examples. Formatting example:\n    \n    ![Image 21](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/toolformer-annotation.png)\n    \n    Fig. 7. How dataset is annotated to do API calls.  \n    (Image source: [Schick et al. 2023](https://arxiv.org/abs/2302.04761)).\n    \n    *   Each API call is represented as a tuple of (API name, corresponding input), $c=(a\\_c, i\\_c)$ and its corresponding result is denoted as $r$. The API call sequences with and without results are labeled as follows, respectively:\n        \n        $$ \\\\begin{aligned} e(c) &\\= \\\\langle\\\\texttt{API}\\\\rangle a\\_c(i\\_c) \\\\langle\\\\texttt{/API}\\\\rangle \\\\\\\\ e(c, r) &\\= \\\\langle\\\\texttt{API}\\\\rangle a\\_c(i\\_c) \\\\to r \\\\langle\\\\texttt{/API}\\\\rangle \\\\end{aligned} $$\n        \n    *   Sample API calls based on the probabilities $p\\_\\\\text{LM}(\\\\langle\\\\texttt{API}\\\\rangle \\\\mid \\\\text{prompt}(\\\\mathbf{x}), \\\\mathbf{x}\\_{1:i})$ and select top $k$ candidate positions for doing API calls at position $i$ if the probability is larger than a threshold.\n        \n    *   Then we sample potential API calls from the LM given the sequence $\\[\\\\text{prompt}(\\\\mathbf{x}), x\\_1, \\\\dots, x\\_{i-1}, \\\\langle\\\\texttt{API}\\\\rangle\\]$ as prefix and $\\\\langle\\\\texttt{/API}\\\\rangle$ as suffix.\n        \n2.  _Filter annotations based on whether API calls help model predict future tokens._ Use a self-supervised loss to decide which API calls are actually helpful.\n    \n    *   Execute each API call $c\\_i$ to get corresponding result $r\\_i$.\n        \n    *   Compute weighted cross entropy loss for the LM over tokens $x\\_i, \\\\dots, x\\_n$ when the model is prefixed with the prompt. Two versions are computed, one with API result and the other with empty sequence $\\\\varepsilon$.\n        \n        $$ \\\\begin{aligned} L^+\\_i &\\= L\\_i(e(c\\_i, r\\_i)) \\\\\\\\ L^-\\_i &\\= \\\\min(L\\_i(\\\\varepsilon), L\\_i(e(c\\_i, \\\\varepsilon))) \\\\\\\\ \\\\end{aligned} $$\n        \n        Only API calls with $L^-\\_i - L^+\\_i$ larger than a threshold are kept, meaning that adding this API call and its results help the model predict future tokens.\n        \n3.  _Fine-tune LM on this annotated dataset._ The new training sequences are constructed as $\\\\mathbf{x}^\\* = x\\_{1:i-1}, e(c\\_i, r\\_i), x\\_{i:n}$ . The training data is a combination of the original dataset (e.g. a subset of CCNet, as in the paper) and its augmented version.\n    \n\nAt inference time, decoding runs until the model produces “$\\\\to$ \" token, indicating that it is expecting response from an API call next.\n\nToolformer currently does not support tool use in a chain (i.e. using the output of one tool as an input for another tool) or in an interactive way (i.e. adopt API response after human selection). Both are interesting future directions to expand the model for.\n\nCitation\n--------\n\nCited as:\n\n> Weng, Lilian. (Mar 2023). Prompt Engineering. Lil’Log. https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/.\n\nOr\n\n```\n@article{weng2023prompt,\n  title   = \"Prompt Engineering\",\n  author  = \"Weng, Lilian\",\n  journal = \"lilianweng.github.io\",\n  year    = \"2023\",\n  month   = \"Mar\",\n  url     = \"https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/\"\n}\n```\n\nUseful Resources\n----------------\n\n*   [OpenAI Cookbook](https://github.com/openai/openai-cookbook) has many in-depth examples for how to utilize LLM efficiently.\n*   [LangChain](https://langchain.readthedocs.io/en/latest/), a library for combining language models with other components to build applications.\n*   [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) repo contains a pretty comprehensive collection of education materials on prompt engineering.\n*   [learnprompting.org](https://learnprompting.org/docs/intro)\n*   [PromptPerfect](https://promptperfect.jina.ai/)\n*   [Semantic Kernel](https://github.com/microsoft/semantic-kernel)\n\nReferences\n----------\n\n\\[1\\] Zhao et al. [“Calibrate Before Use: Improving Few-shot Performance of Language Models.”](https://arxiv.org/abs/2102.09690) ICML 2021\n\n\\[2\\] Liu et al. [“What Makes Good In-Context Examples for GPT-3?”](https://arxiv.org/abs/2101.06804) arXiv preprint arXiv:2101.06804 (2021).\n\n\\[3\\] Lu et al. [“Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity.”](https://arxiv.org/abs/2104.08786) ACL 2022\n\n\\[4\\] Ye et al. [“In-Context Instruction Learning.”](https://arxiv.org/abs/2302.14691) arXiv preprint arXiv:2302.14691 (2023).\n\n\\[5\\] Su et al. [“Selective annotation makes language models better few-shot learners.”](https://arxiv.org/abs/2209.01975) arXiv preprint arXiv:2209.01975 (2022).\n\n\\[6\\] Rubin et al. [“Learning to retrieve prompts for in-context learning.”](https://arxiv.org/abs/2112.08633) NAACL-HLT 2022\n\n\\[7\\] Wei et al. [“Chain of thought prompting elicits reasoning in large language models.”](https://arxiv.org/abs/2201.11903) NeurIPS 2022\n\n\\[8\\] Wang et al. [“Self-Consistency Improves Chain of Thought Reasoning in Language Models.”](https://arxiv.org/abs/2203.11171) ICLR 2023.\n\n\\[9\\] Diao et al. [“Active Prompting with Chain-of-Thought for Large Language Models.”](https://arxiv.org/abs/2302.12246) arXiv preprint arXiv:2302.12246 (2023).\n\n\\[10\\] Zelikman et al. [“STaR: Bootstrapping Reasoning With Reasoning.”](https://arxiv.org/abs/2203.14465) arXiv preprint arXiv:2203.14465 (2022).\n\n\\[11\\] Ye & Durrett. [“The unreliability of explanations in few-shot in-context learning.”](https://arxiv.org/abs/2205.03401) arXiv preprint arXiv:2205.03401 (2022).\n\n\\[12\\] Trivedi et al. [“Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions.”](https://arxiv.org/abs/2212.10509) arXiv preprint arXiv:2212.10509 (2022).\n\n\\[13\\] Press et al. [“Measuring and narrowing the compositionality gap in language models.”](https://arxiv.org/abs/2210.03350) arXiv preprint arXiv:2210.03350 (2022).\n\n\\[14\\] Yao et al. [“ReAct: Synergizing reasoning and acting in language models.”](https://arxiv.org/abs/2210.03629) ICLR 2023.\n\n\\[15\\] Fu et al. [“Complexity-based prompting for multi-step reasoning.”](https://arxiv.org/abs/2210.00720) arXiv preprint arXiv:2210.00720 (2022).\n\n\\[16\\] Wang et al. [“Rationale-augmented ensembles in language models.”](https://arxiv.org/abs/2207.00747) arXiv preprint arXiv:2207.00747 (2022).\n\n\\[17\\] Zhang et al. [“Automatic chain of thought prompting in large language models.”](https://arxiv.org/abs/2210.03493) arXiv preprint arXiv:2210.03493 (2022).\n\n\\[18\\] Shum et al. [“Automatic Prompt Augmentation and Selection with Chain-of-Thought from Labeled Data.”](https://arxiv.org/abs/2302.12822) arXiv preprint arXiv:2302.12822 (2023).\n\n\\[19\\] Zhou et al. [“Large Language Models Are Human-Level Prompt Engineers.”](https://arxiv.org/abs/2211.01910) ICLR 2023.\n\n\\[20\\] Lazaridou et al. [“Internet augmented language models through few-shot prompting for open-domain question answering.”](https://arxiv.org/abs/2203.05115) arXiv preprint arXiv:2203.05115 (2022).\n\n\\[21\\] Chen et al. [“Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks.”](https://arxiv.org/abs/2211.12588) arXiv preprint arXiv:2211.12588 (2022).\n\n\\[22\\] Gao et al. [“PAL: Program-aided language models.”](https://arxiv.org/abs/2211.10435) arXiv preprint arXiv:2211.10435 (2022).\n\n\\[23\\] Parisi et al. [“TALM: Tool Augmented Language Models”](https://arxiv.org/abs/2205.12255) arXiv preprint arXiv:2205.12255 (2022).\n\n\\[24\\] Schick et al. [“Toolformer: Language Models Can Teach Themselves to Use Tools.”](https://arxiv.org/abs/2302.04761) arXiv preprint arXiv:2302.04761 (2023).\n\n\\[25\\] Mialon et al. [“Augmented Language Models: a Survey”](https://arxiv.org/abs/2302.07842) arXiv preprint arXiv:2302.07842 (2023).\n\n\\[26\\] Yao et al. [“Tree of Thoughts: Deliberate Problem Solving with Large Language Models.”](https://arxiv.org/abs/2305.10601) arXiv preprint arXiv:2305.10601 (2023).",
  "publishedTime": "2023-03-15T00:00:00Z",
  "usage": {
    "tokens": 9116
  }
}
```
