---
title: AutoMix: Automatically Mixing Language Models
description: AutoMix: Automatically Mixing Language Models
url: https://automix-llm.github.io/automix/
timestamp: 2025-01-20T15:49:56.564Z
domain: automix-llm.github.io
path: automix
---

# AutoMix: Automatically Mixing Language Models


AutoMix: Automatically Mixing Language Models


## Content

[Aman Madaan](https://amanmadaan.github.io/)♠\*, [Ankit Anand](https://sites.google.com/view/ankitsanand/home)‡, Srividya Pranavi Potharaju†, [Swaroop Mishra](https://swarooprm.github.io/)‡, [Pei Zhou](https://shaoxia57.github.io/)♣, Aditya Gupta, Dheeraj Rajagopal†, Karthik Kappaganthu†, [Yiming Yang](https://www.cs.cmu.edu/~./yiming/)♠, [Shyam Upadhyay](http://shyamupa.com/)†, [Manaal Faruqui](https://www.manaalfaruqui.com/)†, [Mausam](https://www.cse.iitd.ac.in/~mausam/)♢

♠Carnegie Mellon University †Google ‡Google DeepMind  
♢IIT Delhi ♣University of Southern California

∗Equal Contribution. Work started and partly done during Aman’s internship at Google.

TLDR: AutoMix optimizes cost and accuracy by routing queries between small and large language models,  
through self-verification and POMDP routing.
----------------------------------------------------------------------------------------------------------------------------------------------------

![Image 7](https://automix-llm.github.io/automix/static/images/automix_teaser.png)

Abstract
--------

Large language models (LLMs) are now available from cloud API providers in various sizes and configurations. While this diversity offers a broad spectrum of choices, effectively leveraging the options to optimize computational cost and performance remains challenging. In this work, we present **AutoMix**, an approach that strategically routes queries to larger LMs, based on the approximate correctness of outputs from a smaller LM. Central to AutoMix are two key technical contributions. First, it has a few-shot _self-verification_ mechanism, which estimates the reliability of its own outputs without requiring extensive training. Second, given that self-verification can be noisy, it employs a _POMDP-based router_ that effectively selects an appropriately sized model based on answer confidence. Experiments across five language models and five challenging datasets show that AutoMix consistently surpasses strong baselines, reducing computational cost by over _50%_ for comparable performance.

Key-Highlights
--------------

*   🔁 **Few-shot Self-Verification:** Accurately assess correctness using just the context, without extensive training.
*   💡 **POMDP-based Router:** Overcome noisy verification signals and dynamically select from multiple models.
*   📈 **Efficiency Gains:** Achieve over 50% reduction in computational cost at similar performance.
*   🔌 **Black-box Applicability:** Works out-of-the-box with closed-source APIs, no access to weights required.

Results Summary
---------------

**AutoMix consistently outperforms strong baselines, providing a better incremental benefit per cost (IBC) and reducing computational cost by over 50% while maintaining comparable performance.**

![Image 8](https://automix-llm.github.io/automix/static/images/results_table.png)

![Image 9](https://automix-llm.github.io/automix/static/images/results_graph.png)

* * *

Using AutoMix in your code
--------------------------

Using AutoMix in your code takes only a few lines of changes.

**1\. Installing**

```
pip install automix-llm
```

**2\. Training and Inference**

```
from automix import Automix, POMDP

mixer = Automix(POMDP(*args, **kwargs))
mixer.train(train_data)
results = mixer.evaluate(test_data)
```

**3\. High Customizability**

Check out our [Github repo](https://github.com/automix-llm/automix) for more details!

BibTeX
------

```
@misc{aggarwal2024automixautomaticallymixinglanguage,
      title={AutoMix: Automatically Mixing Language Models}, 
      author={Pranjal Aggarwal and Aman Madaan and Ankit Anand and Srividya Pranavi Potharaju and Swaroop Mishra and Pei Zhou and Aditya Gupta and Dheeraj Rajagopal and Karthik Kappaganthu and Yiming Yang and Shyam Upadhyay and Manaal Faruqui and Mausam},
      year={2024},
      eprint={2310.12963},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2310.12963}, 
}
```

## Metadata

```json
{
  "title": "AutoMix: Automatically Mixing Language Models",
  "description": "AutoMix: Automatically Mixing Language Models",
  "url": "https://automix-llm.github.io/automix/",
  "content": "[Aman Madaan](https://amanmadaan.github.io/)♠\\*, [Ankit Anand](https://sites.google.com/view/ankitsanand/home)‡, Srividya Pranavi Potharaju†, [Swaroop Mishra](https://swarooprm.github.io/)‡, [Pei Zhou](https://shaoxia57.github.io/)♣, Aditya Gupta, Dheeraj Rajagopal†, Karthik Kappaganthu†, [Yiming Yang](https://www.cs.cmu.edu/~./yiming/)♠, [Shyam Upadhyay](http://shyamupa.com/)†, [Manaal Faruqui](https://www.manaalfaruqui.com/)†, [Mausam](https://www.cse.iitd.ac.in/~mausam/)♢\n\n♠Carnegie Mellon University †Google ‡Google DeepMind  \n♢IIT Delhi ♣University of Southern California\n\n∗Equal Contribution. Work started and partly done during Aman’s internship at Google.\n\nTLDR: AutoMix optimizes cost and accuracy by routing queries between small and large language models,  \nthrough self-verification and POMDP routing.\n----------------------------------------------------------------------------------------------------------------------------------------------------\n\n![Image 7](https://automix-llm.github.io/automix/static/images/automix_teaser.png)\n\nAbstract\n--------\n\nLarge language models (LLMs) are now available from cloud API providers in various sizes and configurations. While this diversity offers a broad spectrum of choices, effectively leveraging the options to optimize computational cost and performance remains challenging. In this work, we present **AutoMix**, an approach that strategically routes queries to larger LMs, based on the approximate correctness of outputs from a smaller LM. Central to AutoMix are two key technical contributions. First, it has a few-shot _self-verification_ mechanism, which estimates the reliability of its own outputs without requiring extensive training. Second, given that self-verification can be noisy, it employs a _POMDP-based router_ that effectively selects an appropriately sized model based on answer confidence. Experiments across five language models and five challenging datasets show that AutoMix consistently surpasses strong baselines, reducing computational cost by over _50%_ for comparable performance.\n\nKey-Highlights\n--------------\n\n*   🔁 **Few-shot Self-Verification:** Accurately assess correctness using just the context, without extensive training.\n*   💡 **POMDP-based Router:** Overcome noisy verification signals and dynamically select from multiple models.\n*   📈 **Efficiency Gains:** Achieve over 50% reduction in computational cost at similar performance.\n*   🔌 **Black-box Applicability:** Works out-of-the-box with closed-source APIs, no access to weights required.\n\nResults Summary\n---------------\n\n**AutoMix consistently outperforms strong baselines, providing a better incremental benefit per cost (IBC) and reducing computational cost by over 50% while maintaining comparable performance.**\n\n![Image 8](https://automix-llm.github.io/automix/static/images/results_table.png)\n\n![Image 9](https://automix-llm.github.io/automix/static/images/results_graph.png)\n\n* * *\n\nUsing AutoMix in your code\n--------------------------\n\nUsing AutoMix in your code takes only a few lines of changes.\n\n**1\\. Installing**\n\n```\npip install automix-llm\n```\n\n**2\\. Training and Inference**\n\n```\nfrom automix import Automix, POMDP\n\nmixer = Automix(POMDP(*args, **kwargs))\nmixer.train(train_data)\nresults = mixer.evaluate(test_data)\n```\n\n**3\\. High Customizability**\n\nCheck out our [Github repo](https://github.com/automix-llm/automix) for more details!\n\nBibTeX\n------\n\n```\n@misc{aggarwal2024automixautomaticallymixinglanguage,\n      title={AutoMix: Automatically Mixing Language Models}, \n      author={Pranjal Aggarwal and Aman Madaan and Ankit Anand and Srividya Pranavi Potharaju and Swaroop Mishra and Pei Zhou and Aditya Gupta and Dheeraj Rajagopal and Karthik Kappaganthu and Yiming Yang and Shyam Upadhyay and Manaal Faruqui and Mausam},\n      year={2024},\n      eprint={2310.12963},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2310.12963}, \n}\n```",
  "usage": {
    "tokens": 975
  }
}
```
