---
title: ViperGPT: Visual Inference via Python Execution for Reasoning
description: ViperGPT: Visual Inference via Python Execution for Reasoning.
url: https://viper.cs.columbia.edu/
timestamp: 2025-01-20T15:41:46.278Z
domain: viper.cs.columbia.edu
path: root
---

# ViperGPT: Visual Inference via Python Execution for Reasoning


ViperGPT: Visual Inference via Python Execution for Reasoning.


## Content

ViperGPT: Visual Inference via Python Execution for Reasoning
===============

ViperGPT: Visual Inference via Python Execution for Reasoning
=============================================================

[Dídac Surís](https://www.didacsuris.com/)\*, [Sachit Menon](https://sachit-menon.github.io/)\*, [Carl Vondrick](https://www.cs.columbia.edu/~vondrick/)

\*Equal contribution

Columbia University

[Paper](https://arxiv.org/pdf/2303.08128.pdf) [arXiv](https://arxiv.org/abs/2303.08128) [Code](https://github.com/cvlab-columbia/viper)

ViperGPT decomposes visual queries into interpretable steps.
------------------------------------------------------------

Abstract
--------

Answering visual queries is a complex task that requires both visual processing and reasoning. End-to-end models, the dominant approach for this task, do not explicitly differentiate between the two, limiting interpretability and generalization. Learning modular programs presents a promising alternative, but has proven challenging due to the difficulty of learning both the programs and modules simultaneously. We introduce ViperGPT, a framework that leverages code-generation models to compose vision-and-language models into subroutines to produce a result for any query. ViperGPT utilizes a provided API to access the available modules, and composes them by generating Python code that is later executed. This simple approach requires no further training, and achieves state-of-the-art results across various complex visual tasks.

How does it work?
-----------------

A brief explanation of ViperGPT.
--------------------------------

Logical Reasoning
-----------------

ViperGPT can perform logical operations because it directly executes Python code.

[Previous](https://viper.cs.columbia.edu/#carouselExampleControls_logic) [Next](https://viper.cs.columbia.edu/#carouselExampleControls_logic)

Spatial Understanding
---------------------

We show ViperGPT's spatial understanding.

[Previous](https://viper.cs.columbia.edu/#carouselExampleControls_spatial) [Next](https://viper.cs.columbia.edu/#carouselExampleControls_spatial)

Knowledge
---------

ViperGPT can access the knowledge of large language models.

Consistency
-----------

ViperGPT answers similar questions with consistent reasoning.

[Previous](https://viper.cs.columbia.edu/#carouselExampleControls) [Next](https://viper.cs.columbia.edu/#carouselExampleControls)

Math
----

ViperGPT can count, and divide. All using Python.

Attributes
----------

We show some ViperGPT examples involving attributes.

[Previous](https://viper.cs.columbia.edu/#carouselExampleControls2) [Next](https://viper.cs.columbia.edu/#carouselExampleControls2)

Relational Reasoning
--------------------

Reasoning about relations.

[Previous](https://viper.cs.columbia.edu/#carouselExampleControls_relation) [Next](https://viper.cs.columbia.edu/#carouselExampleControls_relation)

Negation
--------

Negation is programmatic, not neural.

Temporal Reasoning
------------------

ViperGPT can navigate through videos to understand them.

  

More Results
------------

  

  

Related Work
------------

*   • [Visual Programming for Compositional Visual Reasoning](https://prior.allenai.org/projects/visprog)
*   • [Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models](https://arxiv.org/abs/2303.04671)
*   • [Neural Module Networks](https://arxiv.org/abs/1511.02799)
*   • [Inferring and Executing Programs for Visual Reasoning](https://arxiv.org/abs/1705.03633)
*   • [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435)
*   • [Code4Struct: Code Generation for Few-Shot Structured Prediction from Natural Language](https://arxiv.org/abs/2210.12810)
*   • [Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks](https://arxiv.org/abs/2211.12588)
*   • [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)

BibTeX
------

```
@article{surismenon2023vipergpt,
    title={ViperGPT: Visual Inference via Python Execution for Reasoning},
    author={D\'idac Sur\'is and Sachit Menon and Carl Vondrick},
    journal={Proceedings of IEEE International Conference on Computer Vision (ICCV)},
    year={2023}
}
```

[](https://viper.cs.columbia.edu/static/viper_paper.pdf)[](https://github.com/cvlab-columbia/viper)

We thank Revant Teotia and Chengzhi Mao for helpful feedback, as well as 3Blue1Brown and the Manim community for their wonderful visualization library.

This research is based on work partially supported by the DARPA MCS program under Federal Agreement No. N660011924032 and the NSF CAREER Award #2046910. DS is supported by the Microsoft PhD Fellowship and SM is supported by the NSF GRFP.

This webpage template was inspired by [this](https://nerfies.github.io/) and [this](https://hyperfuture.cs.columbia.edu/) project pages.

## Metadata

```json
{
  "title": "ViperGPT: Visual Inference via Python Execution for Reasoning",
  "description": "ViperGPT: Visual Inference via Python Execution for Reasoning.",
  "url": "https://viper.cs.columbia.edu/",
  "content": "ViperGPT: Visual Inference via Python Execution for Reasoning\n===============\n\nViperGPT: Visual Inference via Python Execution for Reasoning\n=============================================================\n\n[Dídac Surís](https://www.didacsuris.com/)\\*, [Sachit Menon](https://sachit-menon.github.io/)\\*, [Carl Vondrick](https://www.cs.columbia.edu/~vondrick/)\n\n\\*Equal contribution\n\nColumbia University\n\n[Paper](https://arxiv.org/pdf/2303.08128.pdf) [arXiv](https://arxiv.org/abs/2303.08128) [Code](https://github.com/cvlab-columbia/viper)\n\nViperGPT decomposes visual queries into interpretable steps.\n------------------------------------------------------------\n\nAbstract\n--------\n\nAnswering visual queries is a complex task that requires both visual processing and reasoning. End-to-end models, the dominant approach for this task, do not explicitly differentiate between the two, limiting interpretability and generalization. Learning modular programs presents a promising alternative, but has proven challenging due to the difficulty of learning both the programs and modules simultaneously. We introduce ViperGPT, a framework that leverages code-generation models to compose vision-and-language models into subroutines to produce a result for any query. ViperGPT utilizes a provided API to access the available modules, and composes them by generating Python code that is later executed. This simple approach requires no further training, and achieves state-of-the-art results across various complex visual tasks.\n\nHow does it work?\n-----------------\n\nA brief explanation of ViperGPT.\n--------------------------------\n\nLogical Reasoning\n-----------------\n\nViperGPT can perform logical operations because it directly executes Python code.\n\n[Previous](https://viper.cs.columbia.edu/#carouselExampleControls_logic) [Next](https://viper.cs.columbia.edu/#carouselExampleControls_logic)\n\nSpatial Understanding\n---------------------\n\nWe show ViperGPT's spatial understanding.\n\n[Previous](https://viper.cs.columbia.edu/#carouselExampleControls_spatial) [Next](https://viper.cs.columbia.edu/#carouselExampleControls_spatial)\n\nKnowledge\n---------\n\nViperGPT can access the knowledge of large language models.\n\nConsistency\n-----------\n\nViperGPT answers similar questions with consistent reasoning.\n\n[Previous](https://viper.cs.columbia.edu/#carouselExampleControls) [Next](https://viper.cs.columbia.edu/#carouselExampleControls)\n\nMath\n----\n\nViperGPT can count, and divide. All using Python.\n\nAttributes\n----------\n\nWe show some ViperGPT examples involving attributes.\n\n[Previous](https://viper.cs.columbia.edu/#carouselExampleControls2) [Next](https://viper.cs.columbia.edu/#carouselExampleControls2)\n\nRelational Reasoning\n--------------------\n\nReasoning about relations.\n\n[Previous](https://viper.cs.columbia.edu/#carouselExampleControls_relation) [Next](https://viper.cs.columbia.edu/#carouselExampleControls_relation)\n\nNegation\n--------\n\nNegation is programmatic, not neural.\n\nTemporal Reasoning\n------------------\n\nViperGPT can navigate through videos to understand them.\n\n  \n\nMore Results\n------------\n\n  \n\n  \n\nRelated Work\n------------\n\n*   • [Visual Programming for Compositional Visual Reasoning](https://prior.allenai.org/projects/visprog)\n*   • [Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models](https://arxiv.org/abs/2303.04671)\n*   • [Neural Module Networks](https://arxiv.org/abs/1511.02799)\n*   • [Inferring and Executing Programs for Visual Reasoning](https://arxiv.org/abs/1705.03633)\n*   • [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435)\n*   • [Code4Struct: Code Generation for Few-Shot Structured Prediction from Natural Language](https://arxiv.org/abs/2210.12810)\n*   • [Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks](https://arxiv.org/abs/2211.12588)\n*   • [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)\n\nBibTeX\n------\n\n```\n@article{surismenon2023vipergpt,\n    title={ViperGPT: Visual Inference via Python Execution for Reasoning},\n    author={D\\'idac Sur\\'is and Sachit Menon and Carl Vondrick},\n    journal={Proceedings of IEEE International Conference on Computer Vision (ICCV)},\n    year={2023}\n}\n```\n\n[](https://viper.cs.columbia.edu/static/viper_paper.pdf)[](https://github.com/cvlab-columbia/viper)\n\nWe thank Revant Teotia and Chengzhi Mao for helpful feedback, as well as 3Blue1Brown and the Manim community for their wonderful visualization library.\n\nThis research is based on work partially supported by the DARPA MCS program under Federal Agreement No. N660011924032 and the NSF CAREER Award #2046910. DS is supported by the Microsoft PhD Fellowship and SM is supported by the NSF GRFP.\n\nThis webpage template was inspired by [this](https://nerfies.github.io/) and [this](https://hyperfuture.cs.columbia.edu/) project pages.",
  "usage": {
    "tokens": 1137
  }
}
```
