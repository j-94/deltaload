---
title: CodeChain: Towards Modular Code Generation through Chain of Self-revisions
description: 
url: https://blog.salesforceairesearch.com/codechain/
timestamp: 2025-01-20T15:54:20.942Z
domain: blog.salesforceairesearch.com
path: codechain
---

# CodeChain: Towards Modular Code Generation through Chain of Self-revisions



## Content

TL;DR: With CodeChain, a pretrained large language model (LLM) can solve challenging coding problems by integrating modularity in generation samples and self-improve by employing a chain of self-revisions on representative sub-modules. CodeChain can achieve state-of-the-art results with both OpenAI GPT models and open-source LLMs on challenging coding benchmarks like APPS and CodeContests.

Limitations of code generation approaches with code LLMs
--------------------------------------------------------

Large Language Models (LLMs) have already become quite proficient at solving simpler programming tasks like those in [HumanEval](https://github.com/openai/human-eval) or [MBPP](https://huggingface.co/datasets/mbpp) benchmarks. However, solving more complex and competitive programming tasks is still quite challenging for these models – possibly due to their tendency to generate solutions as monolithic code blocks. Another limit of this generation approach is that the models would simply generate a large number (several thousand) of solutions independently, with the hope that one of the solutions would pass all the private test cases.

On the other hand, in today’s agile development environment, experienced developers often embrace the concept of modularity in programming. Given a problem, they would instinctively write solutions that are highly modularised – each program is divided into high-level logical sub-tasks and sub-modules. The developers would then keep testing and analyzing their implementations, altering modular components from their previously developed solutions to efficiently improve their final solutions (see the figure below).

![Image 55](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/sample_codegen_task_v1.svg)

CodeChain – a new framework for modular and self-improved code generation
-------------------------------------------------------------------------

Inspired by the above problem-solving process, we propose **CodeChain**, a novel inference framework to improve code generation in LLMs through a chain of self-revisions with representative sub-modules. See the figure below for an illustration of how CodeChain works.

![Image 56](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/code-llm-agent-clustering_v2.svg)

CodeChain consists of the following steps:

*   To incorporate modularity in code generation, we first adapt the technique of [chain-of-thought](https://arxiv.org/abs/2201.11903) (CoT) prompting into code generation tasks (see figure below). In this step, we instruct LLMs to decompose their solutions into modular segments. Each modular segment represents an abstract function that is intended for a high-level logical sub-task.
*   The generated modularized samples are iteratively improved by a chain of self-revisions. In each self-revision, we perform the following:
    *   We first extract the sub-modules found in all generated programs. Each extracted sub-module contains high-level information (including intended use and input/output docstrings) and the corresponding code implementation.
    *   We then transform these modules into an embedding space and group them into semantic clusters with k-means clustering.
    *   Within each cluster, we sample the centroid sub-modules – defined as ones that are the closest to the true centroid point in a cluster.
    *   We treat these centroid sub-modules as representative and reusable code parts. This process is inspired by how a developer would often reuse the more modularized and generalized parts of their code.
    *   We then augment the original chain-of-thought prompt with these selected sub-modules. With this augmented prompt, we instruct the LLM to reuse/adapt the selected sub-modules and regenerate a new set of solutions.
*   We first extract the sub-modules found in all generated programs. Each extracted sub-module contains high-level information (including intended use and input/output docstrings) and the corresponding code implementation.
*   We then transform these modules into an embedding space and group them into semantic clusters with k-means clustering.
*   Within each cluster, we sample the centroid sub-modules – defined as ones that are the closest to the true centroid point in a cluster.
*   We treat these centroid sub-modules as representative and reusable code parts. This process is inspired by how a developer would often reuse the more modularized and generalized parts of their code.
*   We then augment the original chain-of-thought prompt with these selected sub-modules. With this augmented prompt, we instruct the LLM to reuse/adapt the selected sub-modules and regenerate a new set of solutions.
*   We keep repeating this generating-revising process, creating a chain of self-revisions, each conditioned by reusable modular code parts.

With CodeChain, LLMs can receive the collective insights from modular components of all past generation samples to improve their future generations, imitating the problem-solving process of an experienced developer.

![Image 57](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/CoT_short-1.svg)

![Image 58](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/sub-modules.svg)

CodeChain boosts the performance of LLMs, achieving SoTA results on [APPS](https://github.com/hendrycks/apps) and [CodeContests](https://github.com/google-deepmind/code_contests)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We find that by naturally encouraging the LLM to reuse the previously developed and verified sub-modules, CodeChain can significantly boost both modularity as well as correctness of the generated solutions, achieving relative [pass@1](https://towardsdatascience.com/a-gentle-introduction-to-code-generation-evaluation-c8dff8c3d19a) improvements of 35% on APPS and 76% on CodeContests. It is shown to be effective on both [OpenAI LLMs](https://openai.com/) as well as open-sourced LLMs like [WizardCoder](https://arxiv.org/abs/2306.08568).

| Model | Size | Introductory | Interview | Competition | All |
| --- | --- | --- | --- | --- | --- |
| Codex | 12B | 4.14 | 0.14 | 0.02 | 0.92 |
| CodeT5 | 770M | 6.60 | 1.03 | 0.30 | 2.00 |
| CodeRL+CodeT5 | 770M | 7.08 | 1.86 | 0.75 | 2.69 |
| text-davinci-002 | – | – | – | – | 7.48 |
| Self-edit+text-davinci-002 | – | – | – | – | 7.94 |
| code-davinci-002 | – | 29.30 | 6.40 | 2.50 | 10.20 |
| WizardCoder | 15B | 26.04 | 4.21 | 0.81 | 7.90 |
| CodeChain+WizardCoder | 15B | **26.29** | **7.49** | **3.75** | **10.50** |
| GPT3.5 | – | 48.00 | 19.42 | 5.42 | 22.33 |
| CodeChain+GPT3.5 | – | **54.50** | **28.11** | **12.38** | **30.24** |

| Model | Size | Val pass@1 | Val pass@5 | Test pass@1 | Test pass@5 |
| --- | --- | --- | --- | --- | --- |
| code-davinci-002 | – | – | – | 1.00 | – |
| WizardCoder | 15B | 1.11 | 3.18 | 1.98 | 3.27 |
| \+ CodeChain | 15B | **2.35** | **3.29** | **2.48** | **3.30** |
| GPT3.5 | – | 6.81 | 16.23 | 5.82 | 11.16 |
| \+ CodeChain | – | **12.86** | **16.91** | **10.27** | **14.11** |

When compared with related approaches such as [Self-repair,](https://arxiv.org/abs/2306.09896) we observed significant relative performance gains when using CodeChain. Specifically, we evaluated our approach over a test subset of 20 samples from APPS, using both GPT3.5 and GPT4 as the base models. We observed that CodeChain can improve the performance with both models, with more significant gains using GPT4. CodeChain+GPT4 can achieve a SoTA result of 61.50% pass@1 on average, even outperforming Self-repair+GPT4 with human feedback.

| Model | Feedback source | Introductory | Interview | Competition | All |
| --- | --- | --- | --- | --- | --- |
| Self-repair+GPT4 | GPT4 | 42.64 | 19.33 | 3.67 | 33.30 |
| Self-repair+GPT4 | Human | 62.21 | 45.67 | 14.67 | 52.60 |
| GPT3.5 | – | 30.00 | 18.33 | 0.00 | 23.75 |
| CodeChain+GPT3.5 | Sub-modules | **31.67** | **27.86** | **0.00** | **26.35** |
| GPT4 | – | 42.86 | 18.33 | 13.33 | 34.75 |
| CodeChain+GPT4 | Sub-modules | **71.07** | **55.00** | **23.33** | **61.50** |

In the figure below, we found significant improvements in all levels of problem difficulties in APPS, with optimal performance gain obtained in revision round 4. At a closer look, we observed that on different levels of problem difficulties, CodeChain has different rates of performance improvement: more challenging problems (i.e. competition and interview level) tend to benefit more from CodeChain than basic problems (i.e. introductory level). Finally, compared with related approaches (self-revision using feedback from test outcomes with natural language explanations like [Self-debug](https://arxiv.org/abs/2304.05128) or self-reflection like [Reflexion](https://arxiv.org/abs/2303.11366)), CodeChain can achieve better performance, using modularised code parts as a form of feedback for self-improving outputs.

![Image 59](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/ablation_baselines.svg)

From the figure below, similar observations can be seen on open-sourced models [WizardCoder](https://arxiv.org/abs/2306.08568), with clearer performance trends on models of larger sizes, including 7B, 15B, and 34B parameters. This is consistent with recent findings on the scaling law of LLMs whereby some features such as instruction-following only emerge when model size is sufficiently large.

To understand the modularity and reusability of CodeChain generation, we conducted experiments to evaluate these qualities on randomly sampled generated programs. We observed that when using CodeChain, GPT3.5 is more likely to generate programs with high levels of modularity and reusability, with the majority of outputs rated 3 to 5 on the Likert scale. This is significantly higher than the conventional direct generation approach, with about 80% of the time generating non-modular or non-reusable codes (i.e. score 0).

![Image 60](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/apps_val_open_source_ablation.svg)

Example Generation Outputs
--------------------------

### Problem description

Your friend Edvin loves languages. A personal favourite of his is speaking the Robber Language. For those of you not familiar with it, it is a language transformation where every consonant is doubled, with an ’o’ put in-between. The rest is kept the same. For example, the word “car” would be transformed into “cocaror”.

Your friend Edvin was going to tell you his password to his favourite website, so that you could check out how awesome it is. Edvin is sure that nobody but him and you speak the Robber Language, so he encrypted it using this simple technique, and wrote it down on a note. After trying the password and realising it does not work, you found out that Edvin was drunk during the transformation. Now you want to find out in how many ways the password might have looked originally.

You are given an encrypted password which Edvin has attempted to translate into the Robber Language. Your task is to determine how many passwords might produce the encrypted password. You may assume that the only thing Edvin did wrong, was when scanning through the word with his eyes, he sometimes missed to transform some consonants using the rule above. Edvin is not deterministic in his failures, i.e. if he missed to transform a consonant once, it is not necessary that he would miss it if it occured again later in the string.

A vowel is considered to be one of the letters “a”, “e”, “i”, “o” and “u”. A consonant is any other letter.

—–Input—–  
Input consists of one encrypted password, the resulting word from Edvins translation. The word can be as long as $1000000$ characters. It will solely consist of lower case letters a-z.

—–Output—–  
Output should consist of one number, the number of ways the password might have looked before Edvin translated it. Since this number may be huge, print the remainder modulo $1000009$.

—–Examples—–  
Sample Input 1:  
car  
Sample Output 1:  
1

Sample Input 2:  
cocar  
Sample Output 2:  
2

### Example generation output (direct generation)

```
s = input()
n = len(s)
vow = set(["a", "e", "i", "o", "u"])
dp = [0]*(n+1)
mod = 10**6+9
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    if s[i-1] in vow or s[i-2] in vow or i - 2 < 0 or s[i-1] != s[i-2] or s[i-1] == 'o':
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= mod
print(dp[n])
```

### Example generation output (CodeChain round 0)

STEP 1: GENERATE SUB-MODULES:

```
def is_vowel(ch):
    """
    Description: This function returns True if the specified character is a vowel, False otherwise.
    Input:
    ch (char): A character.
    Output:
    (bool): True if the character is a vowel, False otherwise.
    """
def count_possible_original_words(word):
    """
    Description: This function counts the possible original words that could have transformed into the given Robber Language word.
    Input:
    word (str): A Robber Language word.
    Output:
    count (int): A count of possible original words.
    """
```

STEP 2: GENERATE PYTHON CODE

```
MOD = 1000009
def is_vowel(ch):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ch in vowels
def count_possible_original_words(word):
    N = len(word)
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1, N+1):
        dp[i] = dp[i-1] 
        if not is_vowel(word[i-1]) and i >= 2 and word[i-1] == word[i-2] and word[i-3] != 'o':
            dp[i] += dp[i-2]
        dp[i] %= MOD
    return dp[N]
word = input().strip()
print(count_possible_original_words(word))
```

### Example generation output (CodeChain round 3)

STEP 1: GENERATE SUB-MODULES:

Since we’re given two very relevant functions “split\_word” and “count\_possible\_passwords”, we can keep these functions in our solution. The function “initialize\_vowels\_and\_modulo” can be useful to initialize global variables.

```
def split_word(word):
    """
    Description: This function splits the word into a list of elements that can be translated back into Robber language.
    Input:
    word (str): The word that needs to be split.
    Output:
    split_word_list (list): The list of strings, where each string represents a possible original letter
    """
```

```
def initialize_vowels_and_modulo():
    """
    Description: This function initializes the vowels and modulo variables.
    Output:
    vowels (set): A set of vowels
    modulo (int): The modulo constant
    """
```

```
def count_possible_passwords(word_list):
    """
    Description: This function counts the number of possible password that might have produced the original word.
    Input: 
    word_list (list): A list with elements from the word
    Output:
    (int): The number of possible passwords modulo 1000009
    """
```

STEP 2: GENERATE PYTHON CODE

```
def split_word(word):
    i = 0
    split_word_list = []
    while i < len(word):
        if i + 2 < len(word) and word[i + 1] == 'o' and word[i + 2] != 'o':
            split_word_list.append(word[i:i+3])
            i += 3
        else:
            split_word_list.append(word[i])
            i += 1
    return split_word_list
def count_possible_passwords(word_list, vowels, modulo):
    dp = [0] * len(word_list)
    dp[0] = 1 if len(word_list[0]) == 1 or word_list[0][0] in vowels else 2
    for i in range(1, len(word_list)):
        if len(word_list[i]) == 1 or word_list[i][0] in vowels:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (dp[i - 1] * 2) % modulo
    return dp[-1]
def initialize_vowels_and_modulo():
    return set(['a', 'e', 'i', 'o', 'u']), 1000009
def solve_task(word):
    split_word_list = split_word(word)
    vowels, modulo = initialize_vowels_and_modulo()
    return count_possible_passwords(split_word_list, vowels, modulo)
word = input()
print(solve_task(word))
```

The Bottom Line
---------------

In CodeChain, we introduce chain-of-thought prompting to generate more modularised programs, which creates natural boundaries for the models to sample parts of the solutions for reuse and revision. In each revision step, we iterate between selecting representative sub-modules and augmenting chain-of-thought prompting with these selected sub-modules. Our experiments indicate the significant performance improvement of CodeChain when using OpenAI GPT or open-sourced WizardCoder as the base models, achieving new SoTA results on APPS and CodeContests benchmarks. Note that CodeChain can be complemented with other self-revision approaches such as Self-debug and Reflexion by combining different feedback types (e.g. natural explanation and reflection) and selecting more diverse and representative sub-modules.

Citation
--------

To cite this work, please use the following BibTeX:

```
@inproceedings{
le2024codechain,
title={CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules},
author={Hung Le and Hailin Chen and Amrita Saha and Akash Gokul and Doyen Sahoo and Shafiq Joty},
booktitle={The Twelfth International Conference on Learning Representations},
year={2024},
url={https://openreview.net/forum?id=vYhglxSj8j}
}
```

Explore More
------------

*   [Technical paper](https://arxiv.org/abs/2310.08992) and [code](https://github.com/SalesforceAIResearch/CodeChain)
*   Follow us on _Twitter_: @[SalesforceResearch](https://twitter.com/SFResearch) , @[Salesforce](https://twitter.com/Salesforce)
*   Visit our [_main website_](https://www.salesforceairesearch.com/) to learn more about all of the exciting research projects that Salesforce AI Research is working on

## Metadata

```json
{
  "title": "CodeChain: Towards Modular Code Generation through Chain of Self-revisions",
  "description": "",
  "url": "https://blog.salesforceairesearch.com/codechain/",
  "content": "TL;DR: With CodeChain, a pretrained large language model (LLM) can solve challenging coding problems by integrating modularity in generation samples and self-improve by employing a chain of self-revisions on representative sub-modules. CodeChain can achieve state-of-the-art results with both OpenAI GPT models and open-source LLMs on challenging coding benchmarks like APPS and CodeContests.\n\nLimitations of code generation approaches with code LLMs\n--------------------------------------------------------\n\nLarge Language Models (LLMs) have already become quite proficient at solving simpler programming tasks like those in [HumanEval](https://github.com/openai/human-eval) or [MBPP](https://huggingface.co/datasets/mbpp) benchmarks. However, solving more complex and competitive programming tasks is still quite challenging for these models – possibly due to their tendency to generate solutions as monolithic code blocks. Another limit of this generation approach is that the models would simply generate a large number (several thousand) of solutions independently, with the hope that one of the solutions would pass all the private test cases.\n\nOn the other hand, in today’s agile development environment, experienced developers often embrace the concept of modularity in programming. Given a problem, they would instinctively write solutions that are highly modularised – each program is divided into high-level logical sub-tasks and sub-modules. The developers would then keep testing and analyzing their implementations, altering modular components from their previously developed solutions to efficiently improve their final solutions (see the figure below).\n\n![Image 55](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/sample_codegen_task_v1.svg)\n\nCodeChain – a new framework for modular and self-improved code generation\n-------------------------------------------------------------------------\n\nInspired by the above problem-solving process, we propose **CodeChain**, a novel inference framework to improve code generation in LLMs through a chain of self-revisions with representative sub-modules. See the figure below for an illustration of how CodeChain works.\n\n![Image 56](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/code-llm-agent-clustering_v2.svg)\n\nCodeChain consists of the following steps:\n\n*   To incorporate modularity in code generation, we first adapt the technique of [chain-of-thought](https://arxiv.org/abs/2201.11903) (CoT) prompting into code generation tasks (see figure below). In this step, we instruct LLMs to decompose their solutions into modular segments. Each modular segment represents an abstract function that is intended for a high-level logical sub-task.\n*   The generated modularized samples are iteratively improved by a chain of self-revisions. In each self-revision, we perform the following:\n    *   We first extract the sub-modules found in all generated programs. Each extracted sub-module contains high-level information (including intended use and input/output docstrings) and the corresponding code implementation.\n    *   We then transform these modules into an embedding space and group them into semantic clusters with k-means clustering.\n    *   Within each cluster, we sample the centroid sub-modules – defined as ones that are the closest to the true centroid point in a cluster.\n    *   We treat these centroid sub-modules as representative and reusable code parts. This process is inspired by how a developer would often reuse the more modularized and generalized parts of their code.\n    *   We then augment the original chain-of-thought prompt with these selected sub-modules. With this augmented prompt, we instruct the LLM to reuse/adapt the selected sub-modules and regenerate a new set of solutions.\n*   We first extract the sub-modules found in all generated programs. Each extracted sub-module contains high-level information (including intended use and input/output docstrings) and the corresponding code implementation.\n*   We then transform these modules into an embedding space and group them into semantic clusters with k-means clustering.\n*   Within each cluster, we sample the centroid sub-modules – defined as ones that are the closest to the true centroid point in a cluster.\n*   We treat these centroid sub-modules as representative and reusable code parts. This process is inspired by how a developer would often reuse the more modularized and generalized parts of their code.\n*   We then augment the original chain-of-thought prompt with these selected sub-modules. With this augmented prompt, we instruct the LLM to reuse/adapt the selected sub-modules and regenerate a new set of solutions.\n*   We keep repeating this generating-revising process, creating a chain of self-revisions, each conditioned by reusable modular code parts.\n\nWith CodeChain, LLMs can receive the collective insights from modular components of all past generation samples to improve their future generations, imitating the problem-solving process of an experienced developer.\n\n![Image 57](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/CoT_short-1.svg)\n\n![Image 58](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/sub-modules.svg)\n\nCodeChain boosts the performance of LLMs, achieving SoTA results on [APPS](https://github.com/hendrycks/apps) and [CodeContests](https://github.com/google-deepmind/code_contests)\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nWe find that by naturally encouraging the LLM to reuse the previously developed and verified sub-modules, CodeChain can significantly boost both modularity as well as correctness of the generated solutions, achieving relative [pass@1](https://towardsdatascience.com/a-gentle-introduction-to-code-generation-evaluation-c8dff8c3d19a) improvements of 35% on APPS and 76% on CodeContests. It is shown to be effective on both [OpenAI LLMs](https://openai.com/) as well as open-sourced LLMs like [WizardCoder](https://arxiv.org/abs/2306.08568).\n\n| Model | Size | Introductory | Interview | Competition | All |\n| --- | --- | --- | --- | --- | --- |\n| Codex | 12B | 4.14 | 0.14 | 0.02 | 0.92 |\n| CodeT5 | 770M | 6.60 | 1.03 | 0.30 | 2.00 |\n| CodeRL+CodeT5 | 770M | 7.08 | 1.86 | 0.75 | 2.69 |\n| text-davinci-002 | – | – | – | – | 7.48 |\n| Self-edit+text-davinci-002 | – | – | – | – | 7.94 |\n| code-davinci-002 | – | 29.30 | 6.40 | 2.50 | 10.20 |\n| WizardCoder | 15B | 26.04 | 4.21 | 0.81 | 7.90 |\n| CodeChain+WizardCoder | 15B | **26.29** | **7.49** | **3.75** | **10.50** |\n| GPT3.5 | – | 48.00 | 19.42 | 5.42 | 22.33 |\n| CodeChain+GPT3.5 | – | **54.50** | **28.11** | **12.38** | **30.24** |\n\n| Model | Size | Val pass@1 | Val pass@5 | Test pass@1 | Test pass@5 |\n| --- | --- | --- | --- | --- | --- |\n| code-davinci-002 | – | – | – | 1.00 | – |\n| WizardCoder | 15B | 1.11 | 3.18 | 1.98 | 3.27 |\n| \\+ CodeChain | 15B | **2.35** | **3.29** | **2.48** | **3.30** |\n| GPT3.5 | – | 6.81 | 16.23 | 5.82 | 11.16 |\n| \\+ CodeChain | – | **12.86** | **16.91** | **10.27** | **14.11** |\n\nWhen compared with related approaches such as [Self-repair,](https://arxiv.org/abs/2306.09896) we observed significant relative performance gains when using CodeChain. Specifically, we evaluated our approach over a test subset of 20 samples from APPS, using both GPT3.5 and GPT4 as the base models. We observed that CodeChain can improve the performance with both models, with more significant gains using GPT4. CodeChain+GPT4 can achieve a SoTA result of 61.50% pass@1 on average, even outperforming Self-repair+GPT4 with human feedback.\n\n| Model | Feedback source | Introductory | Interview | Competition | All |\n| --- | --- | --- | --- | --- | --- |\n| Self-repair+GPT4 | GPT4 | 42.64 | 19.33 | 3.67 | 33.30 |\n| Self-repair+GPT4 | Human | 62.21 | 45.67 | 14.67 | 52.60 |\n| GPT3.5 | – | 30.00 | 18.33 | 0.00 | 23.75 |\n| CodeChain+GPT3.5 | Sub-modules | **31.67** | **27.86** | **0.00** | **26.35** |\n| GPT4 | – | 42.86 | 18.33 | 13.33 | 34.75 |\n| CodeChain+GPT4 | Sub-modules | **71.07** | **55.00** | **23.33** | **61.50** |\n\nIn the figure below, we found significant improvements in all levels of problem difficulties in APPS, with optimal performance gain obtained in revision round 4. At a closer look, we observed that on different levels of problem difficulties, CodeChain has different rates of performance improvement: more challenging problems (i.e. competition and interview level) tend to benefit more from CodeChain than basic problems (i.e. introductory level). Finally, compared with related approaches (self-revision using feedback from test outcomes with natural language explanations like [Self-debug](https://arxiv.org/abs/2304.05128) or self-reflection like [Reflexion](https://arxiv.org/abs/2303.11366)), CodeChain can achieve better performance, using modularised code parts as a form of feedback for self-improving outputs.\n\n![Image 59](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/ablation_baselines.svg)\n\nFrom the figure below, similar observations can be seen on open-sourced models [WizardCoder](https://arxiv.org/abs/2306.08568), with clearer performance trends on models of larger sizes, including 7B, 15B, and 34B parameters. This is consistent with recent findings on the scaling law of LLMs whereby some features such as instruction-following only emerge when model size is sufficiently large.\n\nTo understand the modularity and reusability of CodeChain generation, we conducted experiments to evaluate these qualities on randomly sampled generated programs. We observed that when using CodeChain, GPT3.5 is more likely to generate programs with high levels of modularity and reusability, with the majority of outputs rated 3 to 5 on the Likert scale. This is significantly higher than the conventional direct generation approach, with about 80% of the time generating non-modular or non-reusable codes (i.e. score 0).\n\n![Image 60](https://www.salesforce.com/blog/wp-content/uploads/sites/2/2023/10/apps_val_open_source_ablation.svg)\n\nExample Generation Outputs\n--------------------------\n\n### Problem description\n\nYour friend Edvin loves languages. A personal favourite of his is speaking the Robber Language. For those of you not familiar with it, it is a language transformation where every consonant is doubled, with an ’o’ put in-between. The rest is kept the same. For example, the word “car” would be transformed into “cocaror”.\n\nYour friend Edvin was going to tell you his password to his favourite website, so that you could check out how awesome it is. Edvin is sure that nobody but him and you speak the Robber Language, so he encrypted it using this simple technique, and wrote it down on a note. After trying the password and realising it does not work, you found out that Edvin was drunk during the transformation. Now you want to find out in how many ways the password might have looked originally.\n\nYou are given an encrypted password which Edvin has attempted to translate into the Robber Language. Your task is to determine how many passwords might produce the encrypted password. You may assume that the only thing Edvin did wrong, was when scanning through the word with his eyes, he sometimes missed to transform some consonants using the rule above. Edvin is not deterministic in his failures, i.e. if he missed to transform a consonant once, it is not necessary that he would miss it if it occured again later in the string.\n\nA vowel is considered to be one of the letters “a”, “e”, “i”, “o” and “u”. A consonant is any other letter.\n\n—–Input—–  \nInput consists of one encrypted password, the resulting word from Edvins translation. The word can be as long as $1000000$ characters. It will solely consist of lower case letters a-z.\n\n—–Output—–  \nOutput should consist of one number, the number of ways the password might have looked before Edvin translated it. Since this number may be huge, print the remainder modulo $1000009$.\n\n—–Examples—–  \nSample Input 1:  \ncar  \nSample Output 1:  \n1\n\nSample Input 2:  \ncocar  \nSample Output 2:  \n2\n\n### Example generation output (direct generation)\n\n```\ns = input()\nn = len(s)\nvow = set([\"a\", \"e\", \"i\", \"o\", \"u\"])\ndp = [0]*(n+1)\nmod = 10**6+9\ndp[0] = 1\ndp[1] = 1\nfor i in range(2, n + 1):\n    if s[i-1] in vow or s[i-2] in vow or i - 2 < 0 or s[i-1] != s[i-2] or s[i-1] == 'o':\n        dp[i] = dp[i-1]\n    else:\n        dp[i] = dp[i-1] + dp[i-2]\n        dp[i] %= mod\nprint(dp[n])\n```\n\n### Example generation output (CodeChain round 0)\n\nSTEP 1: GENERATE SUB-MODULES:\n\n```\ndef is_vowel(ch):\n    \"\"\"\n    Description: This function returns True if the specified character is a vowel, False otherwise.\n    Input:\n    ch (char): A character.\n    Output:\n    (bool): True if the character is a vowel, False otherwise.\n    \"\"\"\ndef count_possible_original_words(word):\n    \"\"\"\n    Description: This function counts the possible original words that could have transformed into the given Robber Language word.\n    Input:\n    word (str): A Robber Language word.\n    Output:\n    count (int): A count of possible original words.\n    \"\"\"\n```\n\nSTEP 2: GENERATE PYTHON CODE\n\n```\nMOD = 1000009\ndef is_vowel(ch):\n    vowels = ['a', 'e', 'i', 'o', 'u']\n    return ch in vowels\ndef count_possible_original_words(word):\n    N = len(word)\n    dp = [0]*(N+1)\n    dp[0] = 1\n    for i in range(1, N+1):\n        dp[i] = dp[i-1] \n        if not is_vowel(word[i-1]) and i >= 2 and word[i-1] == word[i-2] and word[i-3] != 'o':\n            dp[i] += dp[i-2]\n        dp[i] %= MOD\n    return dp[N]\nword = input().strip()\nprint(count_possible_original_words(word))\n```\n\n### Example generation output (CodeChain round 3)\n\nSTEP 1: GENERATE SUB-MODULES:\n\nSince we’re given two very relevant functions “split\\_word” and “count\\_possible\\_passwords”, we can keep these functions in our solution. The function “initialize\\_vowels\\_and\\_modulo” can be useful to initialize global variables.\n\n```\ndef split_word(word):\n    \"\"\"\n    Description: This function splits the word into a list of elements that can be translated back into Robber language.\n    Input:\n    word (str): The word that needs to be split.\n    Output:\n    split_word_list (list): The list of strings, where each string represents a possible original letter\n    \"\"\"\n```\n\n```\ndef initialize_vowels_and_modulo():\n    \"\"\"\n    Description: This function initializes the vowels and modulo variables.\n    Output:\n    vowels (set): A set of vowels\n    modulo (int): The modulo constant\n    \"\"\"\n```\n\n```\ndef count_possible_passwords(word_list):\n    \"\"\"\n    Description: This function counts the number of possible password that might have produced the original word.\n    Input: \n    word_list (list): A list with elements from the word\n    Output:\n    (int): The number of possible passwords modulo 1000009\n    \"\"\"\n```\n\nSTEP 2: GENERATE PYTHON CODE\n\n```\ndef split_word(word):\n    i = 0\n    split_word_list = []\n    while i < len(word):\n        if i + 2 < len(word) and word[i + 1] == 'o' and word[i + 2] != 'o':\n            split_word_list.append(word[i:i+3])\n            i += 3\n        else:\n            split_word_list.append(word[i])\n            i += 1\n    return split_word_list\ndef count_possible_passwords(word_list, vowels, modulo):\n    dp = [0] * len(word_list)\n    dp[0] = 1 if len(word_list[0]) == 1 or word_list[0][0] in vowels else 2\n    for i in range(1, len(word_list)):\n        if len(word_list[i]) == 1 or word_list[i][0] in vowels:\n            dp[i] = dp[i - 1]\n        else:\n            dp[i] = (dp[i - 1] * 2) % modulo\n    return dp[-1]\ndef initialize_vowels_and_modulo():\n    return set(['a', 'e', 'i', 'o', 'u']), 1000009\ndef solve_task(word):\n    split_word_list = split_word(word)\n    vowels, modulo = initialize_vowels_and_modulo()\n    return count_possible_passwords(split_word_list, vowels, modulo)\nword = input()\nprint(solve_task(word))\n```\n\nThe Bottom Line\n---------------\n\nIn CodeChain, we introduce chain-of-thought prompting to generate more modularised programs, which creates natural boundaries for the models to sample parts of the solutions for reuse and revision. In each revision step, we iterate between selecting representative sub-modules and augmenting chain-of-thought prompting with these selected sub-modules. Our experiments indicate the significant performance improvement of CodeChain when using OpenAI GPT or open-sourced WizardCoder as the base models, achieving new SoTA results on APPS and CodeContests benchmarks. Note that CodeChain can be complemented with other self-revision approaches such as Self-debug and Reflexion by combining different feedback types (e.g. natural explanation and reflection) and selecting more diverse and representative sub-modules.\n\nCitation\n--------\n\nTo cite this work, please use the following BibTeX:\n\n```\n@inproceedings{\nle2024codechain,\ntitle={CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules},\nauthor={Hung Le and Hailin Chen and Amrita Saha and Akash Gokul and Doyen Sahoo and Shafiq Joty},\nbooktitle={The Twelfth International Conference on Learning Representations},\nyear={2024},\nurl={https://openreview.net/forum?id=vYhglxSj8j}\n}\n```\n\nExplore More\n------------\n\n*   [Technical paper](https://arxiv.org/abs/2310.08992) and [code](https://github.com/SalesforceAIResearch/CodeChain)\n*   Follow us on _Twitter_: @[SalesforceResearch](https://twitter.com/SFResearch) , @[Salesforce](https://twitter.com/Salesforce)\n*   Visit our [_main website_](https://www.salesforceairesearch.com/) to learn more about all of the exciting research projects that Salesforce AI Research is working on",
  "publishedTime": "2023-10-20T20:43:32+00:00",
  "usage": {
    "tokens": 4437
  }
}
```
