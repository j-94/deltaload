---
title: GEO: Generative Engine Optimization
description: GEO: Generative Engine Optimization
url: https://generative-engines.com/GEO/
timestamp: 2025-01-20T16:18:23.536Z
domain: generative-engines.com
path: GEO
---

# GEO: Generative Engine Optimization


GEO: Generative Engine Optimization


## Content

GEO: Generative Engine Optimization
===============           

  
![Image 1: GEO: Generative Engine Optimization](https://generative-engines.com/GEO/static/images/favicon.png) GEO:  
Generative Engine Optimization
======================================================================================================================================================

[Pranjal Aggarwal](https://pranjal2041.github.io/)♢\*, [Vishvak Murahari](https://vishvakmurahari.com/)♠\*, Tanmay Rajpurohit‡, [Ashwin Kalyan](http://ashwinkalyan.com/)†,  
[Karthik R Narasimhan](https://www.cs.princeton.edu/~karthikn/)♠, [Ameet Deshpande](https://ameet-1997.github.io/)♠,  
♠Princeton University †Allen Institute of Technology ‡Georgia Tech ♢IIT Delhi

[Code](https://github.com/GEO-optim/GEO) [Dataset](https://huggingface.co/datasets/GEO-optim/geo-bench) [arXiv](https://arxiv.org/pdf/2311.09735.pdf) [Leaderboard](https://huggingface.co/spaces/GEO-optim/geo-bench) [Email](mailto:pranjal2041@gmail.com)

TLDR: **GEO** is a novel paradigm, that will help content creators optimize their content for  
_next generation_ of search engines augmented with Large Language Models.  

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![Image 2](https://generative-engines.com/GEO/static/images/geo_teaser.png)

Generative Engines
------------------

The advent of large language models (LLMs) has ushered in a new paradigm of search engines that use generative models to gather and summarize information to answer user queries. These **Generative Engines (GEs)**, have the potential to generate accurate and personalized responses, and are rapidly replacing traditional search engines and improving user utility.

What is GEO about?
------------------

![Image 3](https://generative-engines.com/GEO/static/images/explain_geo.jpg)  
However, Generative Engines present numerous challenges for content creators:

*   **Ranking and Visibility:** Assessing site performance in traditional search engines is straightforward, with websites listed in ranked order with verbatim content. However, Generative Engines generate rich and structured responses, often embedding citations in a single block. This makes the notion of ranking and visibility highly nuanced and multi-faceted.
*   **Optimization of Websites:** Unlike search engines, where significant research has been conducted on improving website visibility, it remains unclear how to optimize visibility in generative engine responses.
*   **Black Box Nature:** Due to black box nature of the generative engines, content creators have little to no control over when and how their content is displayed, making it even difficult to optimize their content.

To address these challenges we propose **Generative Engine Optimization (GEO)**, a novel paradigm designed to aid content creators in enhancing their content's visibility. We contribute various impression metrics, a benchmark for evaluation and suite of optimization strategies empowering creators to improve content visibility, on deployed commercial **Generative Engines**.

Key-Highlights
--------------

*   🚀 **Content Optimization for Generative Engines:** GEO allows website owners to optimize content specifically for generative engines.
*   🔎 **Customized Visibility Metrics:** Proposes specialized impression metrics tailored to generative engines, so that you can judge your content optimizations effectively.
*   📊 **Comprehensive Benchmark:** Introduces GEO-BENCH, a diverse benchmark of 10K queries for evaluation and corresponding leaderboard for up-to date comparison with best methods.
*   ⚡️ **Significant Visibility Gains:** Simple GEO strategies improve visibility by up to 40% in experiments on deployed commercial generative engines.

Results Summary
---------------

**GEO outperforms baselines and traditional SEO methods by wide margins. We evaluate on both our proposed Generative Engine and an actual deployed GE to compare the performance. The results highlights, that creators can start using GEO out of box, to improve their content for the next search shift 🔥.**  
  

![Image 4](https://generative-engines.com/GEO/static/images/results_main.png) 

* * *

Our Analysis suggest a.) **GEO** is more helpful if optimization methods are made for target domain, b.) **GEO** will benefit websites lower ranked in search engine more in the future.  
  

![Image 5](https://generative-engines.com/GEO/static/images/results_analysis.png) 

* * *

We qualitatively show, that with **GEO**, creators can make minor changes, however leading to large visibility enhancement for their content.  
  

![Image 6](https://generative-engines.com/GEO/static/images/results_qual.png)  

GEO-BENCH
---------

Generative Engines are becoming the common way to search for information, and GEO would enable creators to optimize the content. However, how do they evaluate their methods, how to assess their performance. Current datasets, are scattered and do not directly represent the kind of queries asked in the new paradigm. We present **GEO-bench**, A diverse benchmark of Generative Engine related queries from different sources!

**1\. [GEO-BENCH](https://huggingface.co/datasets/GEO-optim/geo-bench)**

*   **10K Queries:** 10K queries from different domains, difficulty, cateogry. Train Set of 8K queries, with val and test set of 1k queries each
*   **Datasets:** Benchmark composed of datasets from 1. MS Macro, 2. ORCAS-1, 3. Natural Questions, 4. AllSouls, 5. LIMA, 6. Davinci-Debtate, 7. Perplexity.ai Discover, 8. ELI-5, 9. GPT-4 Generated Queries
*   **Sources & Tags:** Every query is provided with 5 cleaned relevant sources from Google Search Engine. Queries are tagged from more than 50 diverse tags to allow for targeted optimization and analysis.

**2\. [GEO-BENCH Leaderboard](https://huggingface.co/spaces/GEO-optim/geo-bench)**

*   **Public Leaderboard:**We present a leaderboard for GEO-BENCH, which will be updated regularly with the latest results.
*   **Different Domains:** Your method targets particular domain? Leaderboard subsets for different domains, datasets and tags.
*   **Submit your methods:** Submit your methods to the leaderboard and compete with the best methods.

  
A step-forward in facilitating research in the era of new search paradigm!

BibTeX
------

```
@misc{aggarwal2023geo,
      title={GEO: Generative Engine Optimization}, 
      author={Pranjal Aggarwal and Vishvak Murahari and Tanmay Rajpurohit and Ashwin Kalyan and Karthik R Narasimhan and Ameet Deshpande},
      year={2023},
      eprint={2311.09735},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

[](https://arxiv.org/pdf/2311.09735.pdf)[](https://github.com/Pranjal2041/GEO)

Template adapted from [Nerfies](http://nerfies.github.io/) by Keunhong Park et al. and uses [Bulma](https://bulma.io/).

## Metadata

```json
{
  "title": "GEO: Generative Engine Optimization",
  "description": "GEO: Generative Engine Optimization",
  "url": "https://generative-engines.com/GEO/",
  "content": "GEO: Generative Engine Optimization\n===============           \n\n  \n![Image 1: GEO: Generative Engine Optimization](https://generative-engines.com/GEO/static/images/favicon.png) GEO:  \nGenerative Engine Optimization\n======================================================================================================================================================\n\n[Pranjal Aggarwal](https://pranjal2041.github.io/)♢\\*, [Vishvak Murahari](https://vishvakmurahari.com/)♠\\*, Tanmay Rajpurohit‡, [Ashwin Kalyan](http://ashwinkalyan.com/)†,  \n[Karthik R Narasimhan](https://www.cs.princeton.edu/~karthikn/)♠, [Ameet Deshpande](https://ameet-1997.github.io/)♠,  \n♠Princeton University †Allen Institute of Technology ‡Georgia Tech ♢IIT Delhi\n\n[Code](https://github.com/GEO-optim/GEO) [Dataset](https://huggingface.co/datasets/GEO-optim/geo-bench) [arXiv](https://arxiv.org/pdf/2311.09735.pdf) [Leaderboard](https://huggingface.co/spaces/GEO-optim/geo-bench) [Email](mailto:pranjal2041@gmail.com)\n\nTLDR: **GEO** is a novel paradigm, that will help content creators optimize their content for  \n_next generation_ of search engines augmented with Large Language Models.  \n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n![Image 2](https://generative-engines.com/GEO/static/images/geo_teaser.png)\n\nGenerative Engines\n------------------\n\nThe advent of large language models (LLMs) has ushered in a new paradigm of search engines that use generative models to gather and summarize information to answer user queries. These **Generative Engines (GEs)**, have the potential to generate accurate and personalized responses, and are rapidly replacing traditional search engines and improving user utility.\n\nWhat is GEO about?\n------------------\n\n![Image 3](https://generative-engines.com/GEO/static/images/explain_geo.jpg)  \nHowever, Generative Engines present numerous challenges for content creators:\n\n*   **Ranking and Visibility:** Assessing site performance in traditional search engines is straightforward, with websites listed in ranked order with verbatim content. However, Generative Engines generate rich and structured responses, often embedding citations in a single block. This makes the notion of ranking and visibility highly nuanced and multi-faceted.\n*   **Optimization of Websites:** Unlike search engines, where significant research has been conducted on improving website visibility, it remains unclear how to optimize visibility in generative engine responses.\n*   **Black Box Nature:** Due to black box nature of the generative engines, content creators have little to no control over when and how their content is displayed, making it even difficult to optimize their content.\n\nTo address these challenges we propose **Generative Engine Optimization (GEO)**, a novel paradigm designed to aid content creators in enhancing their content's visibility. We contribute various impression metrics, a benchmark for evaluation and suite of optimization strategies empowering creators to improve content visibility, on deployed commercial **Generative Engines**.\n\nKey-Highlights\n--------------\n\n*   🚀 **Content Optimization for Generative Engines:** GEO allows website owners to optimize content specifically for generative engines.\n*   🔎 **Customized Visibility Metrics:** Proposes specialized impression metrics tailored to generative engines, so that you can judge your content optimizations effectively.\n*   📊 **Comprehensive Benchmark:** Introduces GEO-BENCH, a diverse benchmark of 10K queries for evaluation and corresponding leaderboard for up-to date comparison with best methods.\n*   ⚡️ **Significant Visibility Gains:** Simple GEO strategies improve visibility by up to 40% in experiments on deployed commercial generative engines.\n\nResults Summary\n---------------\n\n**GEO outperforms baselines and traditional SEO methods by wide margins. We evaluate on both our proposed Generative Engine and an actual deployed GE to compare the performance. The results highlights, that creators can start using GEO out of box, to improve their content for the next search shift 🔥.**  \n  \n\n![Image 4](https://generative-engines.com/GEO/static/images/results_main.png) \n\n* * *\n\nOur Analysis suggest a.) **GEO** is more helpful if optimization methods are made for target domain, b.) **GEO** will benefit websites lower ranked in search engine more in the future.  \n  \n\n![Image 5](https://generative-engines.com/GEO/static/images/results_analysis.png) \n\n* * *\n\nWe qualitatively show, that with **GEO**, creators can make minor changes, however leading to large visibility enhancement for their content.  \n  \n\n![Image 6](https://generative-engines.com/GEO/static/images/results_qual.png)  \n\nGEO-BENCH\n---------\n\nGenerative Engines are becoming the common way to search for information, and GEO would enable creators to optimize the content. However, how do they evaluate their methods, how to assess their performance. Current datasets, are scattered and do not directly represent the kind of queries asked in the new paradigm. We present **GEO-bench**, A diverse benchmark of Generative Engine related queries from different sources!\n\n**1\\. [GEO-BENCH](https://huggingface.co/datasets/GEO-optim/geo-bench)**\n\n*   **10K Queries:** 10K queries from different domains, difficulty, cateogry. Train Set of 8K queries, with val and test set of 1k queries each\n*   **Datasets:** Benchmark composed of datasets from 1. MS Macro, 2. ORCAS-1, 3. Natural Questions, 4. AllSouls, 5. LIMA, 6. Davinci-Debtate, 7. Perplexity.ai Discover, 8. ELI-5, 9. GPT-4 Generated Queries\n*   **Sources & Tags:** Every query is provided with 5 cleaned relevant sources from Google Search Engine. Queries are tagged from more than 50 diverse tags to allow for targeted optimization and analysis.\n\n**2\\. [GEO-BENCH Leaderboard](https://huggingface.co/spaces/GEO-optim/geo-bench)**\n\n*   **Public Leaderboard:**We present a leaderboard for GEO-BENCH, which will be updated regularly with the latest results.\n*   **Different Domains:** Your method targets particular domain? Leaderboard subsets for different domains, datasets and tags.\n*   **Submit your methods:** Submit your methods to the leaderboard and compete with the best methods.\n\n  \nA step-forward in facilitating research in the era of new search paradigm!\n\nBibTeX\n------\n\n```\n@misc{aggarwal2023geo,\n      title={GEO: Generative Engine Optimization}, \n      author={Pranjal Aggarwal and Vishvak Murahari and Tanmay Rajpurohit and Ashwin Kalyan and Karthik R Narasimhan and Ameet Deshpande},\n      year={2023},\n      eprint={2311.09735},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL}\n}\n```\n\n[](https://arxiv.org/pdf/2311.09735.pdf)[](https://github.com/Pranjal2041/GEO)\n\nTemplate adapted from [Nerfies](http://nerfies.github.io/) by Keunhong Park et al. and uses [Bulma](https://bulma.io/).",
  "usage": {
    "tokens": 1567
  }
}
```
