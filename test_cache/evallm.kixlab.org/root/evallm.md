---
title: EvalLM
description: 
url: https://evallm.kixlab.org/
timestamp: 2025-01-20T15:45:09.477Z
domain: evallm.kixlab.org
path: root
---

# EvalLM



## Content

* * *

EvalLM ⚗️ is an interactive system that aids prompt designers in iterating on **prompts** by evaluating and comparing generated outputs on user-defined **criteria**. With the aid of an **LLM-based evaluation assistant**, the user can iteratively evolve **criteria+prompts** to distinguish more specific qualities in outputs and then improve the quality of outputs on these aspects.

![Image 20: Animation of the overall workflow of EvalLM where users sample inputs from a dataset, generate outputs from each input using two different prompts, and then comparatively evaluate these outputs on user-defined criteria.](https://evallm.kixlab.org/assets/img/animation.gif)

* * *

Interface
---------

The main screen of the interface consists of three panels.

![Image 21: Main screen of EvalLM shows three panels. The generation panel shows text boxes for the prompt and task instruction, and buttons for input sampling. The evaluation panel shows text boxes for the criteria, buttons for evaluating, and stacked bar charts for the evaluation results.](https://evallm.kixlab.org/assets/img/interface.png)

**Generation Panel**: To generate outputs, the user defines their overall **task instruction** (A), two **prompts** they want to compare (B), and then **samples inputs** from a dataset (C) which will be used to test the prompts.

**Evaluation Panel**: To evaluate outputs, the user defines a set of evaluation **[criteria](https://evallm.kixlab.org/#criteria)** (D). Then, after evaluating, they can verify the overall _evaluation_ performance of each prompt (E) or, if they created a validation set, _validate_ how automatic evaluations align with ground-truth evaluations (F).

**Data Panel**: This panel shows **[data rows](https://evallm.kixlab.org/#datarow)** containing inputs, outputs, and evaluation results.

### Criteria

EvalLM allows users to evaluate outputs on their own criteria specific to their application and/or context.

To define a criteria, the user simply provides the criteria with a **name** (A) and **description** (B) in natural language.

To assist users in creating more effective and helpful criteria, the system automatically **reviews** their criteria (C) and provides **suggestions** (D) on how the criteria can be _refined_, _merged_ and _split_.

![Image 22: Criteria are represented as a set of text boxes that contain the name and description of the criteria. Suggested revisions are shown below the criteria.](https://evallm.kixlab.org/assets/img/criteria.png)

### Data Row

![Image 23: Data Rows in the interface display inputs, output pairs, and evaluation results. Clicking on evaluation results opens a panel that shows the explanation for that evaluation underneath the row.](https://evallm.kixlab.org/assets/img/datarow.png)

For each sampled **input** (A), the interface presents the **outputs** generated from each prompt side-by-side (B) and the **evaluation results** for each criteria next to the outputs (C). For each criteria, the evaluation results show which prompt produced the output that better satisfied that criteria.

If the user wants to see more details, they can click on one of these evaluations to see the assistant’s **explanation** (D). To help the user match the explanation and outputs, the system also **highlights** spans from the outputs that were considered to be important when evaluating the criteria (E).

If the user selected to evaluate outputs on multiple trials, they can see the evaluations for **other trials** through the carousel (F).

* * *

Video Demo
----------

See EvalLM in action in this Video Demo.

* * *

Bibtex
------

@inproceedings{10.1145/3613904.3642216,
author = {Kim, Tae Soo and Lee, Yoonjoo and Shin, Jamin and Kim, Young-Ho and Kim, Juho},
title = {EvalLM: Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria},
year = {2024},
isbn = {9798400703300},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3613904.3642216},
doi = {10.1145/3613904.3642216},
booktitle = {Proceedings of the CHI Conference on Human Factors in Computing Systems},
articleno = {306},
numpages = {21},
keywords = {Evaluation, Human-AI Interaction, Large Language Models, Natural Language Generation},
location = {, Honolulu, HI, USA, },
series = {CHI '24}
}

* * *

[![Image 24: Logo of KIXLAB](https://evallm.kixlab.org/assets/img/kixlab_logo.png)](https://kixlab.org/) [![Image 25: Logo of KAIST](https://evallm.kixlab.org/assets/img/kaist_logo.png)](https://kaist.ac.kr/) [![Image 26: Logo of NAVER](https://evallm.kixlab.org/assets/img/naver_logo.png)](https://www.facebook.com/NAVERAILAB)

This research was supported by the **KAIST-NAVER Hypercreative AI Center**.

## Metadata

```json
{
  "title": "EvalLM",
  "description": "",
  "url": "https://evallm.kixlab.org/",
  "content": "* * *\n\nEvalLM ⚗️ is an interactive system that aids prompt designers in iterating on **prompts** by evaluating and comparing generated outputs on user-defined **criteria**. With the aid of an **LLM-based evaluation assistant**, the user can iteratively evolve **criteria+prompts** to distinguish more specific qualities in outputs and then improve the quality of outputs on these aspects.\n\n![Image 20: Animation of the overall workflow of EvalLM where users sample inputs from a dataset, generate outputs from each input using two different prompts, and then comparatively evaluate these outputs on user-defined criteria.](https://evallm.kixlab.org/assets/img/animation.gif)\n\n* * *\n\nInterface\n---------\n\nThe main screen of the interface consists of three panels.\n\n![Image 21: Main screen of EvalLM shows three panels. The generation panel shows text boxes for the prompt and task instruction, and buttons for input sampling. The evaluation panel shows text boxes for the criteria, buttons for evaluating, and stacked bar charts for the evaluation results.](https://evallm.kixlab.org/assets/img/interface.png)\n\n**Generation Panel**: To generate outputs, the user defines their overall **task instruction** (A), two **prompts** they want to compare (B), and then **samples inputs** from a dataset (C) which will be used to test the prompts.\n\n**Evaluation Panel**: To evaluate outputs, the user defines a set of evaluation **[criteria](https://evallm.kixlab.org/#criteria)** (D). Then, after evaluating, they can verify the overall _evaluation_ performance of each prompt (E) or, if they created a validation set, _validate_ how automatic evaluations align with ground-truth evaluations (F).\n\n**Data Panel**: This panel shows **[data rows](https://evallm.kixlab.org/#datarow)** containing inputs, outputs, and evaluation results.\n\n### Criteria\n\nEvalLM allows users to evaluate outputs on their own criteria specific to their application and/or context.\n\nTo define a criteria, the user simply provides the criteria with a **name** (A) and **description** (B) in natural language.\n\nTo assist users in creating more effective and helpful criteria, the system automatically **reviews** their criteria (C) and provides **suggestions** (D) on how the criteria can be _refined_, _merged_ and _split_.\n\n![Image 22: Criteria are represented as a set of text boxes that contain the name and description of the criteria. Suggested revisions are shown below the criteria.](https://evallm.kixlab.org/assets/img/criteria.png)\n\n### Data Row\n\n![Image 23: Data Rows in the interface display inputs, output pairs, and evaluation results. Clicking on evaluation results opens a panel that shows the explanation for that evaluation underneath the row.](https://evallm.kixlab.org/assets/img/datarow.png)\n\nFor each sampled **input** (A), the interface presents the **outputs** generated from each prompt side-by-side (B) and the **evaluation results** for each criteria next to the outputs (C). For each criteria, the evaluation results show which prompt produced the output that better satisfied that criteria.\n\nIf the user wants to see more details, they can click on one of these evaluations to see the assistant’s **explanation** (D). To help the user match the explanation and outputs, the system also **highlights** spans from the outputs that were considered to be important when evaluating the criteria (E).\n\nIf the user selected to evaluate outputs on multiple trials, they can see the evaluations for **other trials** through the carousel (F).\n\n* * *\n\nVideo Demo\n----------\n\nSee EvalLM in action in this Video Demo.\n\n* * *\n\nBibtex\n------\n\n@inproceedings{10.1145/3613904.3642216,\nauthor = {Kim, Tae Soo and Lee, Yoonjoo and Shin, Jamin and Kim, Young-Ho and Kim, Juho},\ntitle = {EvalLM: Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria},\nyear = {2024},\nisbn = {9798400703300},\npublisher = {Association for Computing Machinery},\naddress = {New York, NY, USA},\nurl = {https://doi.org/10.1145/3613904.3642216},\ndoi = {10.1145/3613904.3642216},\nbooktitle = {Proceedings of the CHI Conference on Human Factors in Computing Systems},\narticleno = {306},\nnumpages = {21},\nkeywords = {Evaluation, Human-AI Interaction, Large Language Models, Natural Language Generation},\nlocation = {, Honolulu, HI, USA, },\nseries = {CHI '24}\n}\n\n* * *\n\n[![Image 24: Logo of KIXLAB](https://evallm.kixlab.org/assets/img/kixlab_logo.png)](https://kixlab.org/) [![Image 25: Logo of KAIST](https://evallm.kixlab.org/assets/img/kaist_logo.png)](https://kaist.ac.kr/) [![Image 26: Logo of NAVER](https://evallm.kixlab.org/assets/img/naver_logo.png)](https://www.facebook.com/NAVERAILAB)\n\nThis research was supported by the **KAIST-NAVER Hypercreative AI Center**.",
  "usage": {
    "tokens": 1122
  }
}
```
