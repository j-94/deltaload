---
title: [PDF] Self-Edit: Fault-Aware Code Editor for Code Generation | Semantic Scholar
description: This work proposes a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task and demonstrates superior accuracy and efficiency. Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the question and wrap execution results into a supplementary comment. Utilizing this comment as guidance, our fault-aware code editor is employed to correct errors in the generated code.We perform extensive evaluations across two competitive programming datasets with nine different LLMs. Compared to directly generating from LLMs, our approach can improve the average of pass@1 by 89% on APPS-dev, 31% on APPS-test, and 48% on HumanEval over nine popular code generation LLMs with parameter sizes ranging from 110M to 175B. Compared to other post-processing methods, our method demonstrates superior accuracy and efficiency.
url: https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3
timestamp: 2025-01-20T15:46:32.468Z
domain: www.semanticscholar.org
path: paper_Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li_2f0028060a3a3187d3cbecc3b423dbcf8c8387c3
---

# [PDF] Self-Edit: Fault-Aware Code Editor for Code Generation | Semantic Scholar


This work proposes a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task and demonstrates superior accuracy and efficiency. Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the question and wrap execution results into a supplementary comment. Utilizing this comment as guidance, our fault-aware code editor is employed to correct errors in the generated code.We perform extensive evaluations across two competitive programming datasets with nine different LLMs. Compared to directly generating from LLMs, our approach can improve the average of pass@1 by 89% on APPS-dev, 31% on APPS-test, and 48% on HumanEval over nine popular code generation LLMs with parameter sizes ranging from 110M to 175B. Compared to other post-processing methods, our method demonstrates superior accuracy and efficiency.


## Content

\[PDF\] Self-Edit: Fault-Aware Code Editor for Code Generation | Semantic Scholar
===============
                                                            

[Skip to search form](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#search-form)[Skip to main content](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#main-content)[Skip to account menu](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#account-menu)

[](https://www.semanticscholar.org/)

Search 223,685,196 papers from all fields of science

Search

Sign InCreate Free Account

*   DOI:[10.48550/arXiv.2305.04087](https://doi.org/10.48550/arXiv.2305.04087)
    
*   Corpus ID: 258557186

Self-Edit: Fault-Aware Code Editor for Code Generation
======================================================

@inproceedings{Zhang2023SelfEditFC,
  title={Self-Edit: Fault-Aware Code Editor for Code Generation},
  author={Kechi Zhang and Zhuo Li and Jia Li and Ge Li and Zhi Jin},
  booktitle={Annual Meeting of the Association for Computational Linguistics},
  year={2023},
  url={https://api.semanticscholar.org/CorpusID:258557186}
}

*   [Kechi Zhang](https://www.semanticscholar.org/author/Kechi-Zhang/2033148496), [Zhuo Li](https://www.semanticscholar.org/author/Zhuo-Li/2118393672), +2 authors [Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)
*   Published in [Annual Meeting of the…](https://www.semanticscholar.org/venue?name=Annual%20Meeting%20of%20the%20Association%20for%20Computational%20Linguistics) 6 May 2023
*   Computer Science

TLDR

This work proposes a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task and demonstrates superior accuracy and efficiency.Expand

[](https://www.semanticscholar.org/reader/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3)\[PDF\] Semantic Reader

Save to LibrarySave

Create AlertAlert

Cite

Share

77 Citations

[Highly Influential Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)[](https://www.semanticscholar.org/faq#influential-citations)

8

[Background Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)

27

[Methods Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)

29

[View All](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)

Figures and Tables from this paper
----------------------------------

*   [![Image 17: figure 1](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/1-Figure1-1.png) figure 1](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/0)
*   [![Image 18: table 1](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/5-Table1-1.png) table 1](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/1)
*   [![Image 19: figure 2](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/3-Figure2-1.png) figure 2](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/2)
*   [![Image 20: table 2](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/7-Table2-1.png) table 2](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/3)
*   [![Image 21: figure 3](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/3-Figure3-1.png) figure 3](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/4)
*   [![Image 22: table 3](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/7-Table3-1.png) table 3](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/5)
*   [![Image 23: figure 4](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/4-Figure4-1.png) figure 4](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/6)
*   [![Image 24: table 4](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table4-1.png) table 4](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/7)
*   [![Image 25: table 5](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table5-1.png) table 5](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/8)
*   [![Image 26: figure 5](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/15-Figure5-1.png) figure 5](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/9)
*   [![Image 27: table 6](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table6-1.png) table 6](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/10)
*   [![Image 28: figure 6](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/16-Figure6-1.png) figure 6](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/11)
*   [![Image 29: table 7](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table7-1.png) table 7](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/12)
*   [![Image 30: figure 7](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/17-Figure7-1.png) figure 7](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/13)
*   [![Image 31: table 8](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/9-Table8-1.png) table 8](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/14)
*   [![Image 32: table 9](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/14-Table9-1.png) table 9](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/15)

View All 16 Figures & Tables

Topics
------

AI-Generated

[Self-edit (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/43272475716?corpusId=258557186)[Large Language Models (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/66772037317?corpusId=258557186)[Test Cases (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/68496419689?corpusId=258557186)[Programming Tasks (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/13517708656?corpusId=258557186)[Code Quality (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/2451947701?corpusId=258557186)[Post-processing Method (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/23476977944?corpusId=258557186)[HumanEval (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/37456443194?corpusId=258557186)

77 Citations
------------

Citation Type

Has PDF

Author

More Filters

More Filters

Filters

[### Demystifying GPT Self-Repair for Code Generation](https://www.semanticscholar.org/paper/Demystifying-GPT-Self-Repair-for-Code-Generation-Olausson-Inala/e13b52a3ee01320165d4ba49f20708f9907ed563)

[Theo X. Olausson](https://www.semanticscholar.org/author/Theo-X.-Olausson/1689656957)[J. Inala](https://www.semanticscholar.org/author/J.-Inala/1827015)[Chenglong Wang](https://www.semanticscholar.org/author/Chenglong-Wang/2144523164)[Jianfeng Gao](https://www.semanticscholar.org/author/Jianfeng-Gao/2296412141)[Armando Solar-Lezama](https://www.semanticscholar.org/author/Armando-Solar-Lezama/2278433392)

Computer Science

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2023

TLDR

This paper analyzes GPT-3.5 and GPT-4’s ability to perform self-repair on APPS and establishes a new evaluation strategy dubbed pass@t that measures the pass rate of the tasks against the total number of tokens sampled from the model, enabling a fair comparison to purely sampling-based approaches.Expand

*   [55](https://www.semanticscholar.org/paper/e13b52a3ee01320165d4ba49f20708f9907ed563#citing-papers)
*   [PDF](https://www.semanticscholar.org/paper/e13b52a3ee01320165d4ba49f20708f9907ed563)
    

*   2 Excerpts

Save

[### CYCLE: Learning to Self-Refine the Code Generation](https://www.semanticscholar.org/paper/CYCLE%3A-Learning-to-Self-Refine-the-Code-Generation-Ding-Min/d0612d91867c879b44be4b56cebdc725e2942172)

[Yangruibo Ding](https://www.semanticscholar.org/author/Yangruibo-Ding/1902935998)[Marcus J. Min](https://www.semanticscholar.org/author/Marcus-J.-Min/2271725485)[Gail E. Kaiser](https://www.semanticscholar.org/author/Gail-E.-Kaiser/2271609523)[Baishakhi Ray](https://www.semanticscholar.org/author/Baishakhi-Ray/2258712674)

Computer Science

Proc. ACM Program. Lang.

*   2024

TLDR

This paper proposes CYCLE framework, learning to self-refine the faulty generation according to the available feedback, such as the execution results reported by the test suites, and reveals that CYCLE successfully maintains, sometimes improves, the quality of one-time code generation, while significantly improving the self-refinement capability of code LMs.Expand

*   [16](https://www.semanticscholar.org/paper/d0612d91867c879b44be4b56cebdc725e2942172#citing-papers)
[](https://www.semanticscholar.org/reader/d0612d91867c879b44be4b56cebdc725e2942172)\[PDF\]

*   1 Excerpt

Save

[### GenX: Mastering Code and Test Generation with Execution Feedback](https://www.semanticscholar.org/paper/GenX%3A-Mastering-Code-and-Test-Generation-with-Wang-Liu/4d897e26a0ea89d492e2732e15032f89bf9ac2b9)

[Nan Wang](https://www.semanticscholar.org/author/Nan-Wang/2336524796)[Yafei Liu](https://www.semanticscholar.org/author/Yafei-Liu/2257122796)[Chen Chen](https://www.semanticscholar.org/author/Chen-Chen/2335870474)[H. Lu](https://www.semanticscholar.org/author/H.-Lu/2130373)

Computer Science

*   2024

TLDR

A novel approach that concurrently trains a code generation model and a test generation model, utilizing execution feedback to refine and enhance the performance of both, and introduces two strategies for test and code data augmentation and a new scoring function for code and test ranking.Expand

[](https://www.semanticscholar.org/reader/4d897e26a0ea89d492e2732e15032f89bf9ac2b9)\[PDF\]

Save

[### When to Stop? Towards Efficient Code Generation in LLMs with Excess Token Prevention](https://www.semanticscholar.org/paper/When-to-Stop-Towards-Efficient-Code-Generation-in-Guo-Wang/395357c372c298ce517f64aa99fd5419aed9e2bb)

[Lianghong Guo](https://www.semanticscholar.org/author/Lianghong-Guo/2217902484)[Yanlin Wang](https://www.semanticscholar.org/author/Yanlin-Wang/2239164852)+6 authors [Zibin Zheng](https://www.semanticscholar.org/author/Zibin-Zheng/2267902535)

Computer Science

[ISSTA](https://www.semanticscholar.org/venue?name=ISSTA)

*   2024

TLDR

The key idea of CodeFast is to terminate the inference process in time when unnecessary excess tokens are detected, which can significantly improve the inference speed of various Code LLMs in code generation, without compromising the quality of generated code.Expand

*   [6](https://www.semanticscholar.org/paper/395357c372c298ce517f64aa99fd5419aed9e2bb#citing-papers)
[](https://www.semanticscholar.org/reader/395357c372c298ce517f64aa99fd5419aed9e2bb)\[PDF\]

Save

[### CodeDPO: Aligning Code Models with Self Generated and Verified Source Code](https://www.semanticscholar.org/paper/CodeDPO%3A-Aligning-Code-Models-with-Self-Generated-Zhang-Li/c4cb1276c6371155559f4338beda94ccd72a4eb1)

[Kechi Zhang](https://www.semanticscholar.org/author/Kechi-Zhang/2033148496)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2254313986)+5 authors [Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)

Computer Science

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2024

TLDR

The experiments prove that CodeDPO enhances the capabilities of LLMs in code generation and provides a robust foundation for conducting code preference optimization in more complex and challenging real-world scenarios.Expand

*   [1](https://www.semanticscholar.org/paper/c4cb1276c6371155559f4338beda94ccd72a4eb1#citing-papers)
[](https://www.semanticscholar.org/reader/c4cb1276c6371155559f4338beda94ccd72a4eb1)\[PDF\]

Save

[### SEED: Customize Large Language Models with Sample-Efficient Adaptation for Code Generation](https://www.semanticscholar.org/paper/SEED%3A-Customize-Large-Language-Models-with-for-Code-Jiang-Dong/6b0c3d5118ba03a35dc965129ea37cc32a4e8af2)

[Xue Jiang](https://www.semanticscholar.org/author/Xue-Jiang/2199808863)[Yihong Dong](https://www.semanticscholar.org/author/Yihong-Dong/26845858)[Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2254313986)

Computer Science

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2024

TLDR

This paper proposes a novel adaptation approach named SEED, which stands for Sample-Efficient adaptation with Error-Driven learning for code generation, which leverages the errors made by LLMs as learning opportunities, using error revision to overcome its own shortcomings, thus achieving efficient learning.Expand

*   [2](https://www.semanticscholar.org/paper/6b0c3d5118ba03a35dc965129ea37cc32a4e8af2#citing-papers)
[](https://www.semanticscholar.org/reader/6b0c3d5118ba03a35dc965129ea37cc32a4e8af2)\[PDF\]

*   3 Excerpts

Save

[### Investigating the Transferability of Code Repair for Low-Resource Programming Languages](https://www.semanticscholar.org/paper/Investigating-the-Transferability-of-Code-Repair-Wong-Amayuelas/acb8ef3ddf25a1240c43d50ae0c5ddd0db802329)

[Kyle Wong](https://www.semanticscholar.org/author/Kyle-Wong/2307990107)[Alfonso Amayuelas](https://www.semanticscholar.org/author/Alfonso-Amayuelas/2039956094)[Liangming Pan](https://www.semanticscholar.org/author/Liangming-Pan/2256983134)[W. Wang](https://www.semanticscholar.org/author/W.-Wang/2257130314)

Computer Science

*   2024

TLDR

This work investigates the benefits of distilling code repair for both high and low resource languages to determine if the techniques that are effective in a high resource setting are also applicable in a low resource setting, and shows that distilling the ability to repair code has language dependent benefits.Expand

[](https://www.semanticscholar.org/reader/acb8ef3ddf25a1240c43d50ae0c5ddd0db802329)\[PDF\]

*   2 Excerpts

Save

[### Where Do Large Language Models Fail When Generating Code?](https://www.semanticscholar.org/paper/Where-Do-Large-Language-Models-Fail-When-Generating-Wang-Zhou/817008a2314b80d1388a8b250d735d317f2cab38)

[Zhijie Wang](https://www.semanticscholar.org/author/Zhijie-Wang/2259971409)[Zijie Zhou](https://www.semanticscholar.org/author/Zijie-Zhou/2306140745)+4 authors [Tianyi Zhang](https://www.semanticscholar.org/author/Tianyi-Zhang/2306928157)

Computer Science, Linguistics

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2024

TLDR

An empirical study to analyze incorrect code snippets generated by six popular LLMs on the HumanEval dataset to derive a comprehensive code generation error taxonomy for LLMs through open coding and thematic analysis.Expand

*   [5](https://www.semanticscholar.org/paper/817008a2314b80d1388a8b250d735d317f2cab38#citing-papers)
[](https://www.semanticscholar.org/reader/817008a2314b80d1388a8b250d735d317f2cab38)\[PDF\]

*   1 Excerpt

Save

[### Sifting through the Chaff: On Utilizing Execution Feedback for Ranking the Generated Code Candidates](https://www.semanticscholar.org/paper/Sifting-through-the-Chaff%3A-On-Utilizing-Execution-Sun-Wan/de630124d259fec0133263bd51124a72a5f3b4ed)

[Zhihong Sun](https://www.semanticscholar.org/author/Zhihong-Sun/2276404849)[Yao Wan](https://www.semanticscholar.org/author/Yao-Wan/2282445254)+4 authors [Chen Lyu](https://www.semanticscholar.org/author/Chen-Lyu/2276201365)

Computer Science

[2024 39th IEEE/ACM International Conference on…](https://www.semanticscholar.org/venue?name=39th%20IEEE%2FACM%20International%20Conference%20on%20Automated%20Software%20Engineering%20%28ASE%29)

*   2024

TLDR

RankEF is proposed, an innovative approach for code ranking that leverages execution feedback and employs multi-task learning to integrate code classification with execution feedback generation, and significantly outperforms the state-of-the-art CodeRanker.Expand

*   [Highly Influenced](https://www.semanticscholar.org/paper/de630124d259fec0133263bd51124a72a5f3b4ed?sort=is-influential#citing-papers)
    
[](https://www.semanticscholar.org/reader/de630124d259fec0133263bd51124a72a5f3b4ed)\[PDF\]

*   4 Excerpts

Save

[### LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://www.semanticscholar.org/paper/LiveCodeBench%3A-Holistic-and-Contamination-Free-of-Jain-Han/afe0998d191f3ea8490c7df100a3ffc5dcc62c5e)

[Naman Jain](https://www.semanticscholar.org/author/Naman-Jain/1646458461)[King Han](https://www.semanticscholar.org/author/King-Han/2291438028)+7 authors [Ion Stoica](https://www.semanticscholar.org/author/Ion-Stoica/2290576964)

Computer Science

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2024

TLDR

This work proposes LiveCodeBench, a comprehensive and contamination-free evaluation of LLMs for code, which continuously collects new problems over time from contests across three competition platforms, namely LeetCode, AtCoder, and CodeForces.Expand

*   [85](https://www.semanticscholar.org/paper/afe0998d191f3ea8490c7df100a3ffc5dcc62c5e#citing-papers)
[](https://www.semanticscholar.org/reader/afe0998d191f3ea8490c7df100a3ffc5dcc62c5e)\[PDF\]

Save

...

1

2

3

4

5

...

42 References
-------------

Citation Type

Has PDF

Author

More Filters

More Filters

Filters

[### Interactive Code Generation via Test-Driven User-Intent Formalization](https://www.semanticscholar.org/paper/Interactive-Code-Generation-via-Test-Driven-Lahiri-Naik/e53a61259035769e9822796b51f48a0f067eb071)

[Shuvendu K. Lahiri](https://www.semanticscholar.org/author/Shuvendu-K.-Lahiri/145474353)[Aaditya Naik](https://www.semanticscholar.org/author/Aaditya-Naik/1564577701)+6 authors [Jianfeng Gao](https://www.semanticscholar.org/author/Jianfeng-Gao/48441311)

Computer Science

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2022

TLDR

The workflow of interactive test-driven code generation is proposed, which leverages lightweight user feedback to formalize the user intent using generated tests that can be useful for debugging, and produce an improved set of code suggestions by pruning and ranking candidate code suggestions.Expand

*   [55](https://www.semanticscholar.org/paper/e53a61259035769e9822796b51f48a0f067eb071#citing-papers)
[](https://www.semanticscholar.org/reader/e53a61259035769e9822796b51f48a0f067eb071)\[PDF\]

*   1 Excerpt

Save

[### Evaluating Large Language Models Trained on Code](https://www.semanticscholar.org/paper/Evaluating-Large-Language-Models-Trained-on-Code-Chen-Tworek/acbdbf49f9bc3f151b93d9ca9a06009f4f6eb269)

[Mark Chen](https://www.semanticscholar.org/author/Mark-Chen/2108828435)[Jerry Tworek](https://www.semanticscholar.org/author/Jerry-Tworek/2065005836)+50 authors [Wojciech Zaremba](https://www.semanticscholar.org/author/Wojciech-Zaremba/2563432)

Computer Science

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2021

TLDR

It is found that repeated sampling from the GPT language model is a surprisingly effective strategy for producing working solutions to difficult prompts, and the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics are discussed.Expand

*   [4,078](https://www.semanticscholar.org/paper/acbdbf49f9bc3f151b93d9ca9a06009f4f6eb269#citing-papers)
[](https://www.semanticscholar.org/reader/acbdbf49f9bc3f151b93d9ca9a06009f4f6eb269)\[PDF\]

Save

[### CodeT: Code Generation with Generated Tests](https://www.semanticscholar.org/paper/CodeT%3A-Code-Generation-with-Generated-Tests-Chen-Zhang/876eb375cb7b365475040046df669c039ad54202)

Bei Chen[Fengji Zhang](https://www.semanticscholar.org/author/Fengji-Zhang/2158120018)+4 authors [Weizhu Chen](https://www.semanticscholar.org/author/Weizhu-Chen/2109136147)

Computer Science

[ICLR](https://www.semanticscholar.org/venue?name=ICLR)

*   2023

TLDR

This paper proposes a novel method, CodeT, that leverages the same pre-trained language models to automatically generate test cases for the code samples, thus reducing the human effort and increasing the coverage of the test scenarios.Expand

*   [260](https://www.semanticscholar.org/paper/876eb375cb7b365475040046df669c039ad54202#citing-papers)
[](https://www.semanticscholar.org/reader/876eb375cb7b365475040046df669c039ad54202)\[PDF\]

*   2 Excerpts

Save

[### Fault-Aware Neural Code Rankers](https://www.semanticscholar.org/paper/Fault-Aware-Neural-Code-Rankers-Inala-Wang/075b6fb7d3787953164eecc1bd2e13f97c9f3c44)

[J. Inala](https://www.semanticscholar.org/author/J.-Inala/1827015)[Chenglong Wang](https://www.semanticscholar.org/author/Chenglong-Wang/2144523164)+5 authors [Jianfeng Gao](https://www.semanticscholar.org/author/Jianfeng-Gao/48441311)

Computer Science

[NeurIPS](https://www.semanticscholar.org/venue?name=NeurIPS)

*   2022

TLDR

The proposed CodeRanker is a neural ranker that can predict the correctness of a sampled program without executing it, and can significantly increase the pass@1 accuracy of various code generation models (including Codex, GPT-Neo, G PT-J) on APPS, HumanEval and MBPP datasets.Expand

*   [39](https://www.semanticscholar.org/paper/075b6fb7d3787953164eecc1bd2e13f97c9f3c44#citing-papers)
*   [Highly Influential](https://www.semanticscholar.org/paper/075b6fb7d3787953164eecc1bd2e13f97c9f3c44?sort=is-influential#citing-papers)
    
[](https://www.semanticscholar.org/reader/075b6fb7d3787953164eecc1bd2e13f97c9f3c44)\[PDF\]

*   6 Excerpts

Save

[### AceCoder: Utilizing Existing Code to Enhance Code Generation](https://www.semanticscholar.org/paper/AceCoder%3A-Utilizing-Existing-Code-to-Enhance-Code-Li-Zhao/7ca2e9f768311f29c8abf58e5ec6acf7cf268d9a)

[Jia Li](https://www.semanticscholar.org/author/Jia-Li/2208883878)[Yunfei Zhao](https://www.semanticscholar.org/author/Yunfei-Zhao/2155133281)[Yongming Li](https://www.semanticscholar.org/author/Yongming-Li/2135349350)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2154591375)[Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)

Computer Science

*   2023

TLDR

A new prompting technique named AceCoder, which contains two novel mechanisms, guided code generation and example retrieval, that can significantly improve the performance of LLMs on code generation.Expand

*   [19](https://www.semanticscholar.org/paper/7ca2e9f768311f29c8abf58e5ec6acf7cf268d9a#citing-papers)
[](https://www.semanticscholar.org/reader/7ca2e9f768311f29c8abf58e5ec6acf7cf268d9a)\[PDF\]

*   1 Excerpt

Save

[### Measuring Coding Challenge Competence With APPS](https://www.semanticscholar.org/paper/Measuring-Coding-Challenge-Competence-With-APPS-Hendrycks-Basart/1ccd031f28dccfb226f6c0c588c93a97a50bf95f)

[Dan Hendrycks](https://www.semanticscholar.org/author/Dan-Hendrycks/3422872)[Steven Basart](https://www.semanticscholar.org/author/Steven-Basart/104444594)+8 authors [J. Steinhardt](https://www.semanticscholar.org/author/J.-Steinhardt/5164568)

Computer Science

NeurIPS Datasets and Benchmarks

*   2021

TLDR

APPS, a benchmark for code generation, measures the ability of models to take an arbitrary natural language specification and generate satisfactory Python code and finds that the prevalence of syntax errors is decreasing exponentially as models improve.Expand

*   [498](https://www.semanticscholar.org/paper/1ccd031f28dccfb226f6c0c588c93a97a50bf95f#citing-papers)
*   [Highly Influential](https://www.semanticscholar.org/paper/1ccd031f28dccfb226f6c0c588c93a97a50bf95f?sort=is-influential#citing-papers)
    
[](https://www.semanticscholar.org/reader/1ccd031f28dccfb226f6c0c588c93a97a50bf95f)\[PDF\]

*   5 Excerpts

Save

[### Natural Language to Code Translation with Execution](https://www.semanticscholar.org/paper/Natural-Language-to-Code-Translation-with-Execution-Shi-Fried/47e15941c8b157873c8264e4bf50318d1ba5cd18)

[Freda Shi](https://www.semanticscholar.org/author/Freda-Shi/8815141)[Daniel Fried](https://www.semanticscholar.org/author/Daniel-Fried/47070750)[Marjan Ghazvininejad](https://www.semanticscholar.org/author/Marjan-Ghazvininejad/2320509)[Luke Zettlemoyer](https://www.semanticscholar.org/author/Luke-Zettlemoyer/1982950)[Sida I. Wang](https://www.semanticscholar.org/author/Sida-I.-Wang/8729431)

Computer Science

[EMNLP](https://www.semanticscholar.org/venue?name=EMNLP)

*   2022

TLDR

This work introduces execution result–based minimum Bayes risk decoding (MBR-EXEC) for program selection and finds that it consistently improves over all execution-unaware selection methods, suggesting it as an effective approach for natural language to code translation.Expand

*   [109](https://www.semanticscholar.org/paper/47e15941c8b157873c8264e4bf50318d1ba5cd18#citing-papers)
[](https://www.semanticscholar.org/reader/47e15941c8b157873c8264e4bf50318d1ba5cd18)\[PDF\]

*   2 Excerpts

Save

[### Coder Reviewer Reranking for Code Generation](https://www.semanticscholar.org/paper/Coder-Reviewer-Reranking-for-Code-Generation-Zhang-Yu/27961ae80ad008bd4006704b1b8fa82664137d69)

[Tianyi Zhang](https://www.semanticscholar.org/author/Tianyi-Zhang/2146331419)[Tao Yu](https://www.semanticscholar.org/author/Tao-Yu/48881008)+4 authors [Sida I. Wang](https://www.semanticscholar.org/author/Sida-I.-Wang/8729431)

Computer Science

[ICML](https://www.semanticscholar.org/venue?name=ICML)

*   2023

TLDR

Experimental results show that Coder-Reviewer reranking leads to consistent and significant improvement over reranking with the Coder model only, when combined with executability filtering, and can often outperform the minimum Bayes risk method.Expand

*   [83](https://www.semanticscholar.org/paper/27961ae80ad008bd4006704b1b8fa82664137d69#citing-papers)
[](https://www.semanticscholar.org/reader/27961ae80ad008bd4006704b1b8fa82664137d69)\[PDF\]

Save

[### Enabling Programming Thinking in Large Language Models Toward Code Generation](https://www.semanticscholar.org/paper/Enabling-Programming-Thinking-in-Large-Language-Li-Li/7861f1bed8e8b93c84135add06cf22796baba248)

[Jia Li](https://www.semanticscholar.org/author/Jia-Li/2118373749)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2254313986)[Yongming Li](https://www.semanticscholar.org/author/Yongming-Li/2135349350)[Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)

Computer Science

[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)

*   2023

TLDR

The idea is to decompose code generation into two steps and progressively lead LLMs to analyze&implement requirements in programming logic and proposes an approach named T I P.Expand

*   [26](https://www.semanticscholar.org/paper/7861f1bed8e8b93c84135add06cf22796baba248#citing-papers)
*   [PDF](https://www.semanticscholar.org/paper/7861f1bed8e8b93c84135add06cf22796baba248)
    

*   1 Excerpt

Save

[### Competition-level code generation with AlphaCode](https://www.semanticscholar.org/paper/Competition-level-code-generation-with-AlphaCode-Li-Choi/5cbe278b65a81602a864184bbca37de91448a5f5)

[Yujia Li](https://www.semanticscholar.org/author/Yujia-Li/47002813)[David Choi](https://www.semanticscholar.org/author/David-Choi/2114950020)+27 authors [O. Vinyals](https://www.semanticscholar.org/author/O.-Vinyals/1689108)

Computer Science

[Science](https://www.semanticscholar.org/venue?name=Science)

*   2022

TLDR

AlphaCode is introduced, a system for code generation that achieved an average ranking in the top 54.3% in simulated evaluations on recent programming competitions on the Codeforces platform, marking the first time an artificial intelligence system has performed competitively in programming competitions.Expand

*   [1,085](https://www.semanticscholar.org/paper/5cbe278b65a81602a864184bbca37de91448a5f5#citing-papers)
*   [Highly Influential](https://www.semanticscholar.org/paper/5cbe278b65a81602a864184bbca37de91448a5f5?sort=is-influential#citing-papers)
    
*   [PDF](https://www.semanticscholar.org/paper/5cbe278b65a81602a864184bbca37de91448a5f5)
    

*   5 Excerpts

Save

...

1

2

3

4

5

...

Related Papers
--------------

Showing 1 through 3 of 0 Related Papers

*   [Figures and Tables](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#extracted)
*   [Topics](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#paper-topics)
*   [77 Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)
*   [42 References](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#cited-papers)
*   [Related Papers](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#related-papers)

Stay Connected With Semantic Scholar

Sign Up

What Is Semantic Scholar?
-------------------------

Semantic Scholar is a free, AI-powered research tool for scientific literature, based at Ai2.

[Learn More](https://www.semanticscholar.org/about)

### About

[About Us](https://www.semanticscholar.org/about)[Meet the Team](https://www.semanticscholar.org/about/team)[Publishers](https://www.semanticscholar.org/about/publishers)[Blog (opens in a new tab)](https://medium.com/ai2-blog/semantic-scholar/home)[Ai2 Careers (opens in a new tab)](https://allenai.org/careers?team=semantic+scholar#current-openings)

### Product

[Product Overview](https://www.semanticscholar.org/product)[Semantic Reader](https://www.semanticscholar.org/product/semantic-reader)[Scholar's Hub](https://www.semanticscholar.org/product/scholars-hub)[Beta Program](https://www.semanticscholar.org/product/beta-program)[Release Notes](https://www.semanticscholar.org/product/release-notes)

### API

[API Overview](https://www.semanticscholar.org/product/api)[API Tutorials](https://www.semanticscholar.org/product/api%2Ftutorial)[API Documentation (opens in a new tab)](https://api.semanticscholar.org/api-docs/)[API Gallery](https://www.semanticscholar.org/product/api%2Fgallery)

### Research

[Publications](https://www.semanticscholar.org/research/publications)[Researchers](https://www.semanticscholar.org/research/research-team)[Research Careers](https://www.semanticscholar.org/research/careers)[Prototypes](https://www.semanticscholar.org/research/prototypes)[Resources](https://www.semanticscholar.org/resources)

### Help

[FAQ](https://www.semanticscholar.org/faq)[Librarians](https://www.semanticscholar.org/about/librarians)[Tutorials](https://www.semanticscholar.org/product/tutorials)Contact

Proudly built by [Ai2 (opens in a new tab)](http://allenai.org/)

Collaborators & Attributions •[Terms of Service (opens in a new tab)](https://allenai.org/terms)•[Privacy Policy (opens in a new tab)](https://allenai.org/privacy-policy.html)•[API License Agreement](https://www.semanticscholar.org/product/api/license)

[The Allen Institute for AI (opens in a new tab)](http://allenai.org/)

By clicking accept or continuing to use the site, you agree to the terms outlined in our [Privacy Policy (opens in a new tab)](https://allenai.org/privacy-policy.html), [Terms of Service (opens in a new tab)](https://allenai.org/terms), and [Dataset License (opens in a new tab)](http://api.semanticscholar.org/corpus/legal)

ACCEPT & CONTINUE

## Metadata

```json
{
  "title": "[PDF] Self-Edit: Fault-Aware Code Editor for Code Generation | Semantic Scholar",
  "description": "This work proposes a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task and demonstrates superior accuracy and efficiency. Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the question and wrap execution results into a supplementary comment. Utilizing this comment as guidance, our fault-aware code editor is employed to correct errors in the generated code.We perform extensive evaluations across two competitive programming datasets with nine different LLMs. Compared to directly generating from LLMs, our approach can improve the average of pass@1 by 89% on APPS-dev, 31% on APPS-test, and 48% on HumanEval over nine popular code generation LLMs with parameter sizes ranging from 110M to 175B. Compared to other post-processing methods, our method demonstrates superior accuracy and efficiency.",
  "url": "https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3",
  "content": "\\[PDF\\] Self-Edit: Fault-Aware Code Editor for Code Generation | Semantic Scholar\n===============\n                                                            \n\n[Skip to search form](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#search-form)[Skip to main content](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#main-content)[Skip to account menu](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#account-menu)\n\n[](https://www.semanticscholar.org/)\n\nSearch 223,685,196 papers from all fields of science\n\nSearch\n\nSign InCreate Free Account\n\n*   DOI:[10.48550/arXiv.2305.04087](https://doi.org/10.48550/arXiv.2305.04087)\n    \n*   Corpus ID: 258557186\n\nSelf-Edit: Fault-Aware Code Editor for Code Generation\n======================================================\n\n@inproceedings{Zhang2023SelfEditFC,\n  title={Self-Edit: Fault-Aware Code Editor for Code Generation},\n  author={Kechi Zhang and Zhuo Li and Jia Li and Ge Li and Zhi Jin},\n  booktitle={Annual Meeting of the Association for Computational Linguistics},\n  year={2023},\n  url={https://api.semanticscholar.org/CorpusID:258557186}\n}\n\n*   [Kechi Zhang](https://www.semanticscholar.org/author/Kechi-Zhang/2033148496), [Zhuo Li](https://www.semanticscholar.org/author/Zhuo-Li/2118393672), +2 authors [Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)\n*   Published in [Annual Meeting of the…](https://www.semanticscholar.org/venue?name=Annual%20Meeting%20of%20the%20Association%20for%20Computational%20Linguistics) 6 May 2023\n*   Computer Science\n\nTLDR\n\nThis work proposes a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task and demonstrates superior accuracy and efficiency.Expand\n\n[](https://www.semanticscholar.org/reader/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3)\\[PDF\\] Semantic Reader\n\nSave to LibrarySave\n\nCreate AlertAlert\n\nCite\n\nShare\n\n77 Citations\n\n[Highly Influential Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)[](https://www.semanticscholar.org/faq#influential-citations)\n\n8\n\n[Background Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)\n\n27\n\n[Methods Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)\n\n29\n\n[View All](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)\n\nFigures and Tables from this paper\n----------------------------------\n\n*   [![Image 17: figure 1](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/1-Figure1-1.png) figure 1](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/0)\n*   [![Image 18: table 1](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/5-Table1-1.png) table 1](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/1)\n*   [![Image 19: figure 2](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/3-Figure2-1.png) figure 2](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/2)\n*   [![Image 20: table 2](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/7-Table2-1.png) table 2](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/3)\n*   [![Image 21: figure 3](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/3-Figure3-1.png) figure 3](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/4)\n*   [![Image 22: table 3](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/7-Table3-1.png) table 3](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/5)\n*   [![Image 23: figure 4](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/4-Figure4-1.png) figure 4](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/6)\n*   [![Image 24: table 4](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table4-1.png) table 4](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/7)\n*   [![Image 25: table 5](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table5-1.png) table 5](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/8)\n*   [![Image 26: figure 5](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/15-Figure5-1.png) figure 5](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/9)\n*   [![Image 27: table 6](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table6-1.png) table 6](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/10)\n*   [![Image 28: figure 6](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/16-Figure6-1.png) figure 6](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/11)\n*   [![Image 29: table 7](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/8-Table7-1.png) table 7](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/12)\n*   [![Image 30: figure 7](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/17-Figure7-1.png) figure 7](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/13)\n*   [![Image 31: table 8](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/9-Table8-1.png) table 8](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/14)\n*   [![Image 32: table 9](https://figures.semanticscholar.org/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/14-Table9-1.png) table 9](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3/figure/15)\n\nView All 16 Figures & Tables\n\nTopics\n------\n\nAI-Generated\n\n[Self-edit (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/43272475716?corpusId=258557186)[Large Language Models (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/66772037317?corpusId=258557186)[Test Cases (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/68496419689?corpusId=258557186)[Programming Tasks (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/13517708656?corpusId=258557186)[Code Quality (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/2451947701?corpusId=258557186)[Post-processing Method (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/23476977944?corpusId=258557186)[HumanEval (opens in a new tab)](https://topics-beta.apps.semanticscholar.org/topic/37456443194?corpusId=258557186)\n\n77 Citations\n------------\n\nCitation Type\n\nHas PDF\n\nAuthor\n\nMore Filters\n\nMore Filters\n\nFilters\n\n[### Demystifying GPT Self-Repair for Code Generation](https://www.semanticscholar.org/paper/Demystifying-GPT-Self-Repair-for-Code-Generation-Olausson-Inala/e13b52a3ee01320165d4ba49f20708f9907ed563)\n\n[Theo X. Olausson](https://www.semanticscholar.org/author/Theo-X.-Olausson/1689656957)[J. Inala](https://www.semanticscholar.org/author/J.-Inala/1827015)[Chenglong Wang](https://www.semanticscholar.org/author/Chenglong-Wang/2144523164)[Jianfeng Gao](https://www.semanticscholar.org/author/Jianfeng-Gao/2296412141)[Armando Solar-Lezama](https://www.semanticscholar.org/author/Armando-Solar-Lezama/2278433392)\n\nComputer Science\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2023\n\nTLDR\n\nThis paper analyzes GPT-3.5 and GPT-4’s ability to perform self-repair on APPS and establishes a new evaluation strategy dubbed pass@t that measures the pass rate of the tasks against the total number of tokens sampled from the model, enabling a fair comparison to purely sampling-based approaches.Expand\n\n*   [55](https://www.semanticscholar.org/paper/e13b52a3ee01320165d4ba49f20708f9907ed563#citing-papers)\n*   [PDF](https://www.semanticscholar.org/paper/e13b52a3ee01320165d4ba49f20708f9907ed563)\n    \n\n*   2 Excerpts\n\nSave\n\n[### CYCLE: Learning to Self-Refine the Code Generation](https://www.semanticscholar.org/paper/CYCLE%3A-Learning-to-Self-Refine-the-Code-Generation-Ding-Min/d0612d91867c879b44be4b56cebdc725e2942172)\n\n[Yangruibo Ding](https://www.semanticscholar.org/author/Yangruibo-Ding/1902935998)[Marcus J. Min](https://www.semanticscholar.org/author/Marcus-J.-Min/2271725485)[Gail E. Kaiser](https://www.semanticscholar.org/author/Gail-E.-Kaiser/2271609523)[Baishakhi Ray](https://www.semanticscholar.org/author/Baishakhi-Ray/2258712674)\n\nComputer Science\n\nProc. ACM Program. Lang.\n\n*   2024\n\nTLDR\n\nThis paper proposes CYCLE framework, learning to self-refine the faulty generation according to the available feedback, such as the execution results reported by the test suites, and reveals that CYCLE successfully maintains, sometimes improves, the quality of one-time code generation, while significantly improving the self-refinement capability of code LMs.Expand\n\n*   [16](https://www.semanticscholar.org/paper/d0612d91867c879b44be4b56cebdc725e2942172#citing-papers)\n[](https://www.semanticscholar.org/reader/d0612d91867c879b44be4b56cebdc725e2942172)\\[PDF\\]\n\n*   1 Excerpt\n\nSave\n\n[### GenX: Mastering Code and Test Generation with Execution Feedback](https://www.semanticscholar.org/paper/GenX%3A-Mastering-Code-and-Test-Generation-with-Wang-Liu/4d897e26a0ea89d492e2732e15032f89bf9ac2b9)\n\n[Nan Wang](https://www.semanticscholar.org/author/Nan-Wang/2336524796)[Yafei Liu](https://www.semanticscholar.org/author/Yafei-Liu/2257122796)[Chen Chen](https://www.semanticscholar.org/author/Chen-Chen/2335870474)[H. Lu](https://www.semanticscholar.org/author/H.-Lu/2130373)\n\nComputer Science\n\n*   2024\n\nTLDR\n\nA novel approach that concurrently trains a code generation model and a test generation model, utilizing execution feedback to refine and enhance the performance of both, and introduces two strategies for test and code data augmentation and a new scoring function for code and test ranking.Expand\n\n[](https://www.semanticscholar.org/reader/4d897e26a0ea89d492e2732e15032f89bf9ac2b9)\\[PDF\\]\n\nSave\n\n[### When to Stop? Towards Efficient Code Generation in LLMs with Excess Token Prevention](https://www.semanticscholar.org/paper/When-to-Stop-Towards-Efficient-Code-Generation-in-Guo-Wang/395357c372c298ce517f64aa99fd5419aed9e2bb)\n\n[Lianghong Guo](https://www.semanticscholar.org/author/Lianghong-Guo/2217902484)[Yanlin Wang](https://www.semanticscholar.org/author/Yanlin-Wang/2239164852)+6 authors [Zibin Zheng](https://www.semanticscholar.org/author/Zibin-Zheng/2267902535)\n\nComputer Science\n\n[ISSTA](https://www.semanticscholar.org/venue?name=ISSTA)\n\n*   2024\n\nTLDR\n\nThe key idea of CodeFast is to terminate the inference process in time when unnecessary excess tokens are detected, which can significantly improve the inference speed of various Code LLMs in code generation, without compromising the quality of generated code.Expand\n\n*   [6](https://www.semanticscholar.org/paper/395357c372c298ce517f64aa99fd5419aed9e2bb#citing-papers)\n[](https://www.semanticscholar.org/reader/395357c372c298ce517f64aa99fd5419aed9e2bb)\\[PDF\\]\n\nSave\n\n[### CodeDPO: Aligning Code Models with Self Generated and Verified Source Code](https://www.semanticscholar.org/paper/CodeDPO%3A-Aligning-Code-Models-with-Self-Generated-Zhang-Li/c4cb1276c6371155559f4338beda94ccd72a4eb1)\n\n[Kechi Zhang](https://www.semanticscholar.org/author/Kechi-Zhang/2033148496)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2254313986)+5 authors [Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)\n\nComputer Science\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2024\n\nTLDR\n\nThe experiments prove that CodeDPO enhances the capabilities of LLMs in code generation and provides a robust foundation for conducting code preference optimization in more complex and challenging real-world scenarios.Expand\n\n*   [1](https://www.semanticscholar.org/paper/c4cb1276c6371155559f4338beda94ccd72a4eb1#citing-papers)\n[](https://www.semanticscholar.org/reader/c4cb1276c6371155559f4338beda94ccd72a4eb1)\\[PDF\\]\n\nSave\n\n[### SEED: Customize Large Language Models with Sample-Efficient Adaptation for Code Generation](https://www.semanticscholar.org/paper/SEED%3A-Customize-Large-Language-Models-with-for-Code-Jiang-Dong/6b0c3d5118ba03a35dc965129ea37cc32a4e8af2)\n\n[Xue Jiang](https://www.semanticscholar.org/author/Xue-Jiang/2199808863)[Yihong Dong](https://www.semanticscholar.org/author/Yihong-Dong/26845858)[Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2254313986)\n\nComputer Science\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2024\n\nTLDR\n\nThis paper proposes a novel adaptation approach named SEED, which stands for Sample-Efficient adaptation with Error-Driven learning for code generation, which leverages the errors made by LLMs as learning opportunities, using error revision to overcome its own shortcomings, thus achieving efficient learning.Expand\n\n*   [2](https://www.semanticscholar.org/paper/6b0c3d5118ba03a35dc965129ea37cc32a4e8af2#citing-papers)\n[](https://www.semanticscholar.org/reader/6b0c3d5118ba03a35dc965129ea37cc32a4e8af2)\\[PDF\\]\n\n*   3 Excerpts\n\nSave\n\n[### Investigating the Transferability of Code Repair for Low-Resource Programming Languages](https://www.semanticscholar.org/paper/Investigating-the-Transferability-of-Code-Repair-Wong-Amayuelas/acb8ef3ddf25a1240c43d50ae0c5ddd0db802329)\n\n[Kyle Wong](https://www.semanticscholar.org/author/Kyle-Wong/2307990107)[Alfonso Amayuelas](https://www.semanticscholar.org/author/Alfonso-Amayuelas/2039956094)[Liangming Pan](https://www.semanticscholar.org/author/Liangming-Pan/2256983134)[W. Wang](https://www.semanticscholar.org/author/W.-Wang/2257130314)\n\nComputer Science\n\n*   2024\n\nTLDR\n\nThis work investigates the benefits of distilling code repair for both high and low resource languages to determine if the techniques that are effective in a high resource setting are also applicable in a low resource setting, and shows that distilling the ability to repair code has language dependent benefits.Expand\n\n[](https://www.semanticscholar.org/reader/acb8ef3ddf25a1240c43d50ae0c5ddd0db802329)\\[PDF\\]\n\n*   2 Excerpts\n\nSave\n\n[### Where Do Large Language Models Fail When Generating Code?](https://www.semanticscholar.org/paper/Where-Do-Large-Language-Models-Fail-When-Generating-Wang-Zhou/817008a2314b80d1388a8b250d735d317f2cab38)\n\n[Zhijie Wang](https://www.semanticscholar.org/author/Zhijie-Wang/2259971409)[Zijie Zhou](https://www.semanticscholar.org/author/Zijie-Zhou/2306140745)+4 authors [Tianyi Zhang](https://www.semanticscholar.org/author/Tianyi-Zhang/2306928157)\n\nComputer Science, Linguistics\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2024\n\nTLDR\n\nAn empirical study to analyze incorrect code snippets generated by six popular LLMs on the HumanEval dataset to derive a comprehensive code generation error taxonomy for LLMs through open coding and thematic analysis.Expand\n\n*   [5](https://www.semanticscholar.org/paper/817008a2314b80d1388a8b250d735d317f2cab38#citing-papers)\n[](https://www.semanticscholar.org/reader/817008a2314b80d1388a8b250d735d317f2cab38)\\[PDF\\]\n\n*   1 Excerpt\n\nSave\n\n[### Sifting through the Chaff: On Utilizing Execution Feedback for Ranking the Generated Code Candidates](https://www.semanticscholar.org/paper/Sifting-through-the-Chaff%3A-On-Utilizing-Execution-Sun-Wan/de630124d259fec0133263bd51124a72a5f3b4ed)\n\n[Zhihong Sun](https://www.semanticscholar.org/author/Zhihong-Sun/2276404849)[Yao Wan](https://www.semanticscholar.org/author/Yao-Wan/2282445254)+4 authors [Chen Lyu](https://www.semanticscholar.org/author/Chen-Lyu/2276201365)\n\nComputer Science\n\n[2024 39th IEEE/ACM International Conference on…](https://www.semanticscholar.org/venue?name=39th%20IEEE%2FACM%20International%20Conference%20on%20Automated%20Software%20Engineering%20%28ASE%29)\n\n*   2024\n\nTLDR\n\nRankEF is proposed, an innovative approach for code ranking that leverages execution feedback and employs multi-task learning to integrate code classification with execution feedback generation, and significantly outperforms the state-of-the-art CodeRanker.Expand\n\n*   [Highly Influenced](https://www.semanticscholar.org/paper/de630124d259fec0133263bd51124a72a5f3b4ed?sort=is-influential#citing-papers)\n    \n[](https://www.semanticscholar.org/reader/de630124d259fec0133263bd51124a72a5f3b4ed)\\[PDF\\]\n\n*   4 Excerpts\n\nSave\n\n[### LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://www.semanticscholar.org/paper/LiveCodeBench%3A-Holistic-and-Contamination-Free-of-Jain-Han/afe0998d191f3ea8490c7df100a3ffc5dcc62c5e)\n\n[Naman Jain](https://www.semanticscholar.org/author/Naman-Jain/1646458461)[King Han](https://www.semanticscholar.org/author/King-Han/2291438028)+7 authors [Ion Stoica](https://www.semanticscholar.org/author/Ion-Stoica/2290576964)\n\nComputer Science\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2024\n\nTLDR\n\nThis work proposes LiveCodeBench, a comprehensive and contamination-free evaluation of LLMs for code, which continuously collects new problems over time from contests across three competition platforms, namely LeetCode, AtCoder, and CodeForces.Expand\n\n*   [85](https://www.semanticscholar.org/paper/afe0998d191f3ea8490c7df100a3ffc5dcc62c5e#citing-papers)\n[](https://www.semanticscholar.org/reader/afe0998d191f3ea8490c7df100a3ffc5dcc62c5e)\\[PDF\\]\n\nSave\n\n...\n\n1\n\n2\n\n3\n\n4\n\n5\n\n...\n\n42 References\n-------------\n\nCitation Type\n\nHas PDF\n\nAuthor\n\nMore Filters\n\nMore Filters\n\nFilters\n\n[### Interactive Code Generation via Test-Driven User-Intent Formalization](https://www.semanticscholar.org/paper/Interactive-Code-Generation-via-Test-Driven-Lahiri-Naik/e53a61259035769e9822796b51f48a0f067eb071)\n\n[Shuvendu K. Lahiri](https://www.semanticscholar.org/author/Shuvendu-K.-Lahiri/145474353)[Aaditya Naik](https://www.semanticscholar.org/author/Aaditya-Naik/1564577701)+6 authors [Jianfeng Gao](https://www.semanticscholar.org/author/Jianfeng-Gao/48441311)\n\nComputer Science\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2022\n\nTLDR\n\nThe workflow of interactive test-driven code generation is proposed, which leverages lightweight user feedback to formalize the user intent using generated tests that can be useful for debugging, and produce an improved set of code suggestions by pruning and ranking candidate code suggestions.Expand\n\n*   [55](https://www.semanticscholar.org/paper/e53a61259035769e9822796b51f48a0f067eb071#citing-papers)\n[](https://www.semanticscholar.org/reader/e53a61259035769e9822796b51f48a0f067eb071)\\[PDF\\]\n\n*   1 Excerpt\n\nSave\n\n[### Evaluating Large Language Models Trained on Code](https://www.semanticscholar.org/paper/Evaluating-Large-Language-Models-Trained-on-Code-Chen-Tworek/acbdbf49f9bc3f151b93d9ca9a06009f4f6eb269)\n\n[Mark Chen](https://www.semanticscholar.org/author/Mark-Chen/2108828435)[Jerry Tworek](https://www.semanticscholar.org/author/Jerry-Tworek/2065005836)+50 authors [Wojciech Zaremba](https://www.semanticscholar.org/author/Wojciech-Zaremba/2563432)\n\nComputer Science\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2021\n\nTLDR\n\nIt is found that repeated sampling from the GPT language model is a surprisingly effective strategy for producing working solutions to difficult prompts, and the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics are discussed.Expand\n\n*   [4,078](https://www.semanticscholar.org/paper/acbdbf49f9bc3f151b93d9ca9a06009f4f6eb269#citing-papers)\n[](https://www.semanticscholar.org/reader/acbdbf49f9bc3f151b93d9ca9a06009f4f6eb269)\\[PDF\\]\n\nSave\n\n[### CodeT: Code Generation with Generated Tests](https://www.semanticscholar.org/paper/CodeT%3A-Code-Generation-with-Generated-Tests-Chen-Zhang/876eb375cb7b365475040046df669c039ad54202)\n\nBei Chen[Fengji Zhang](https://www.semanticscholar.org/author/Fengji-Zhang/2158120018)+4 authors [Weizhu Chen](https://www.semanticscholar.org/author/Weizhu-Chen/2109136147)\n\nComputer Science\n\n[ICLR](https://www.semanticscholar.org/venue?name=ICLR)\n\n*   2023\n\nTLDR\n\nThis paper proposes a novel method, CodeT, that leverages the same pre-trained language models to automatically generate test cases for the code samples, thus reducing the human effort and increasing the coverage of the test scenarios.Expand\n\n*   [260](https://www.semanticscholar.org/paper/876eb375cb7b365475040046df669c039ad54202#citing-papers)\n[](https://www.semanticscholar.org/reader/876eb375cb7b365475040046df669c039ad54202)\\[PDF\\]\n\n*   2 Excerpts\n\nSave\n\n[### Fault-Aware Neural Code Rankers](https://www.semanticscholar.org/paper/Fault-Aware-Neural-Code-Rankers-Inala-Wang/075b6fb7d3787953164eecc1bd2e13f97c9f3c44)\n\n[J. Inala](https://www.semanticscholar.org/author/J.-Inala/1827015)[Chenglong Wang](https://www.semanticscholar.org/author/Chenglong-Wang/2144523164)+5 authors [Jianfeng Gao](https://www.semanticscholar.org/author/Jianfeng-Gao/48441311)\n\nComputer Science\n\n[NeurIPS](https://www.semanticscholar.org/venue?name=NeurIPS)\n\n*   2022\n\nTLDR\n\nThe proposed CodeRanker is a neural ranker that can predict the correctness of a sampled program without executing it, and can significantly increase the pass@1 accuracy of various code generation models (including Codex, GPT-Neo, G PT-J) on APPS, HumanEval and MBPP datasets.Expand\n\n*   [39](https://www.semanticscholar.org/paper/075b6fb7d3787953164eecc1bd2e13f97c9f3c44#citing-papers)\n*   [Highly Influential](https://www.semanticscholar.org/paper/075b6fb7d3787953164eecc1bd2e13f97c9f3c44?sort=is-influential#citing-papers)\n    \n[](https://www.semanticscholar.org/reader/075b6fb7d3787953164eecc1bd2e13f97c9f3c44)\\[PDF\\]\n\n*   6 Excerpts\n\nSave\n\n[### AceCoder: Utilizing Existing Code to Enhance Code Generation](https://www.semanticscholar.org/paper/AceCoder%3A-Utilizing-Existing-Code-to-Enhance-Code-Li-Zhao/7ca2e9f768311f29c8abf58e5ec6acf7cf268d9a)\n\n[Jia Li](https://www.semanticscholar.org/author/Jia-Li/2208883878)[Yunfei Zhao](https://www.semanticscholar.org/author/Yunfei-Zhao/2155133281)[Yongming Li](https://www.semanticscholar.org/author/Yongming-Li/2135349350)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2154591375)[Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)\n\nComputer Science\n\n*   2023\n\nTLDR\n\nA new prompting technique named AceCoder, which contains two novel mechanisms, guided code generation and example retrieval, that can significantly improve the performance of LLMs on code generation.Expand\n\n*   [19](https://www.semanticscholar.org/paper/7ca2e9f768311f29c8abf58e5ec6acf7cf268d9a#citing-papers)\n[](https://www.semanticscholar.org/reader/7ca2e9f768311f29c8abf58e5ec6acf7cf268d9a)\\[PDF\\]\n\n*   1 Excerpt\n\nSave\n\n[### Measuring Coding Challenge Competence With APPS](https://www.semanticscholar.org/paper/Measuring-Coding-Challenge-Competence-With-APPS-Hendrycks-Basart/1ccd031f28dccfb226f6c0c588c93a97a50bf95f)\n\n[Dan Hendrycks](https://www.semanticscholar.org/author/Dan-Hendrycks/3422872)[Steven Basart](https://www.semanticscholar.org/author/Steven-Basart/104444594)+8 authors [J. Steinhardt](https://www.semanticscholar.org/author/J.-Steinhardt/5164568)\n\nComputer Science\n\nNeurIPS Datasets and Benchmarks\n\n*   2021\n\nTLDR\n\nAPPS, a benchmark for code generation, measures the ability of models to take an arbitrary natural language specification and generate satisfactory Python code and finds that the prevalence of syntax errors is decreasing exponentially as models improve.Expand\n\n*   [498](https://www.semanticscholar.org/paper/1ccd031f28dccfb226f6c0c588c93a97a50bf95f#citing-papers)\n*   [Highly Influential](https://www.semanticscholar.org/paper/1ccd031f28dccfb226f6c0c588c93a97a50bf95f?sort=is-influential#citing-papers)\n    \n[](https://www.semanticscholar.org/reader/1ccd031f28dccfb226f6c0c588c93a97a50bf95f)\\[PDF\\]\n\n*   5 Excerpts\n\nSave\n\n[### Natural Language to Code Translation with Execution](https://www.semanticscholar.org/paper/Natural-Language-to-Code-Translation-with-Execution-Shi-Fried/47e15941c8b157873c8264e4bf50318d1ba5cd18)\n\n[Freda Shi](https://www.semanticscholar.org/author/Freda-Shi/8815141)[Daniel Fried](https://www.semanticscholar.org/author/Daniel-Fried/47070750)[Marjan Ghazvininejad](https://www.semanticscholar.org/author/Marjan-Ghazvininejad/2320509)[Luke Zettlemoyer](https://www.semanticscholar.org/author/Luke-Zettlemoyer/1982950)[Sida I. Wang](https://www.semanticscholar.org/author/Sida-I.-Wang/8729431)\n\nComputer Science\n\n[EMNLP](https://www.semanticscholar.org/venue?name=EMNLP)\n\n*   2022\n\nTLDR\n\nThis work introduces execution result–based minimum Bayes risk decoding (MBR-EXEC) for program selection and finds that it consistently improves over all execution-unaware selection methods, suggesting it as an effective approach for natural language to code translation.Expand\n\n*   [109](https://www.semanticscholar.org/paper/47e15941c8b157873c8264e4bf50318d1ba5cd18#citing-papers)\n[](https://www.semanticscholar.org/reader/47e15941c8b157873c8264e4bf50318d1ba5cd18)\\[PDF\\]\n\n*   2 Excerpts\n\nSave\n\n[### Coder Reviewer Reranking for Code Generation](https://www.semanticscholar.org/paper/Coder-Reviewer-Reranking-for-Code-Generation-Zhang-Yu/27961ae80ad008bd4006704b1b8fa82664137d69)\n\n[Tianyi Zhang](https://www.semanticscholar.org/author/Tianyi-Zhang/2146331419)[Tao Yu](https://www.semanticscholar.org/author/Tao-Yu/48881008)+4 authors [Sida I. Wang](https://www.semanticscholar.org/author/Sida-I.-Wang/8729431)\n\nComputer Science\n\n[ICML](https://www.semanticscholar.org/venue?name=ICML)\n\n*   2023\n\nTLDR\n\nExperimental results show that Coder-Reviewer reranking leads to consistent and significant improvement over reranking with the Coder model only, when combined with executability filtering, and can often outperform the minimum Bayes risk method.Expand\n\n*   [83](https://www.semanticscholar.org/paper/27961ae80ad008bd4006704b1b8fa82664137d69#citing-papers)\n[](https://www.semanticscholar.org/reader/27961ae80ad008bd4006704b1b8fa82664137d69)\\[PDF\\]\n\nSave\n\n[### Enabling Programming Thinking in Large Language Models Toward Code Generation](https://www.semanticscholar.org/paper/Enabling-Programming-Thinking-in-Large-Language-Li-Li/7861f1bed8e8b93c84135add06cf22796baba248)\n\n[Jia Li](https://www.semanticscholar.org/author/Jia-Li/2118373749)[Ge Li](https://www.semanticscholar.org/author/Ge-Li/2254313986)[Yongming Li](https://www.semanticscholar.org/author/Yongming-Li/2135349350)[Zhi Jin](https://www.semanticscholar.org/author/Zhi-Jin/2152843753)\n\nComputer Science\n\n[ArXiv](https://www.semanticscholar.org/venue?name=ArXiv)\n\n*   2023\n\nTLDR\n\nThe idea is to decompose code generation into two steps and progressively lead LLMs to analyze&implement requirements in programming logic and proposes an approach named T I P.Expand\n\n*   [26](https://www.semanticscholar.org/paper/7861f1bed8e8b93c84135add06cf22796baba248#citing-papers)\n*   [PDF](https://www.semanticscholar.org/paper/7861f1bed8e8b93c84135add06cf22796baba248)\n    \n\n*   1 Excerpt\n\nSave\n\n[### Competition-level code generation with AlphaCode](https://www.semanticscholar.org/paper/Competition-level-code-generation-with-AlphaCode-Li-Choi/5cbe278b65a81602a864184bbca37de91448a5f5)\n\n[Yujia Li](https://www.semanticscholar.org/author/Yujia-Li/47002813)[David Choi](https://www.semanticscholar.org/author/David-Choi/2114950020)+27 authors [O. Vinyals](https://www.semanticscholar.org/author/O.-Vinyals/1689108)\n\nComputer Science\n\n[Science](https://www.semanticscholar.org/venue?name=Science)\n\n*   2022\n\nTLDR\n\nAlphaCode is introduced, a system for code generation that achieved an average ranking in the top 54.3% in simulated evaluations on recent programming competitions on the Codeforces platform, marking the first time an artificial intelligence system has performed competitively in programming competitions.Expand\n\n*   [1,085](https://www.semanticscholar.org/paper/5cbe278b65a81602a864184bbca37de91448a5f5#citing-papers)\n*   [Highly Influential](https://www.semanticscholar.org/paper/5cbe278b65a81602a864184bbca37de91448a5f5?sort=is-influential#citing-papers)\n    \n*   [PDF](https://www.semanticscholar.org/paper/5cbe278b65a81602a864184bbca37de91448a5f5)\n    \n\n*   5 Excerpts\n\nSave\n\n...\n\n1\n\n2\n\n3\n\n4\n\n5\n\n...\n\nRelated Papers\n--------------\n\nShowing 1 through 3 of 0 Related Papers\n\n*   [Figures and Tables](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#extracted)\n*   [Topics](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#paper-topics)\n*   [77 Citations](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#citing-papers)\n*   [42 References](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#cited-papers)\n*   [Related Papers](https://www.semanticscholar.org/paper/Self-Edit%3A-Fault-Aware-Code-Editor-for-Code-Zhang-Li/2f0028060a3a3187d3cbecc3b423dbcf8c8387c3#related-papers)\n\nStay Connected With Semantic Scholar\n\nSign Up\n\nWhat Is Semantic Scholar?\n-------------------------\n\nSemantic Scholar is a free, AI-powered research tool for scientific literature, based at Ai2.\n\n[Learn More](https://www.semanticscholar.org/about)\n\n### About\n\n[About Us](https://www.semanticscholar.org/about)[Meet the Team](https://www.semanticscholar.org/about/team)[Publishers](https://www.semanticscholar.org/about/publishers)[Blog (opens in a new tab)](https://medium.com/ai2-blog/semantic-scholar/home)[Ai2 Careers (opens in a new tab)](https://allenai.org/careers?team=semantic+scholar#current-openings)\n\n### Product\n\n[Product Overview](https://www.semanticscholar.org/product)[Semantic Reader](https://www.semanticscholar.org/product/semantic-reader)[Scholar's Hub](https://www.semanticscholar.org/product/scholars-hub)[Beta Program](https://www.semanticscholar.org/product/beta-program)[Release Notes](https://www.semanticscholar.org/product/release-notes)\n\n### API\n\n[API Overview](https://www.semanticscholar.org/product/api)[API Tutorials](https://www.semanticscholar.org/product/api%2Ftutorial)[API Documentation (opens in a new tab)](https://api.semanticscholar.org/api-docs/)[API Gallery](https://www.semanticscholar.org/product/api%2Fgallery)\n\n### Research\n\n[Publications](https://www.semanticscholar.org/research/publications)[Researchers](https://www.semanticscholar.org/research/research-team)[Research Careers](https://www.semanticscholar.org/research/careers)[Prototypes](https://www.semanticscholar.org/research/prototypes)[Resources](https://www.semanticscholar.org/resources)\n\n### Help\n\n[FAQ](https://www.semanticscholar.org/faq)[Librarians](https://www.semanticscholar.org/about/librarians)[Tutorials](https://www.semanticscholar.org/product/tutorials)Contact\n\nProudly built by [Ai2 (opens in a new tab)](http://allenai.org/)\n\nCollaborators & Attributions •[Terms of Service (opens in a new tab)](https://allenai.org/terms)•[Privacy Policy (opens in a new tab)](https://allenai.org/privacy-policy.html)•[API License Agreement](https://www.semanticscholar.org/product/api/license)\n\n[The Allen Institute for AI (opens in a new tab)](http://allenai.org/)\n\nBy clicking accept or continuing to use the site, you agree to the terms outlined in our [Privacy Policy (opens in a new tab)](https://allenai.org/privacy-policy.html), [Terms of Service (opens in a new tab)](https://allenai.org/terms), and [Dataset License (opens in a new tab)](http://api.semanticscholar.org/corpus/legal)\n\nACCEPT & CONTINUE",
  "usage": {
    "tokens": 11035
  }
}
```
