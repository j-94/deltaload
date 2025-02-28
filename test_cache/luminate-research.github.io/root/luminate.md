---
title: Luminate
description: 
url: https://luminate-research.github.io/
timestamp: 2025-01-20T15:59:20.679Z
domain: luminate-research.github.io
path: root
---

# Luminate



## Content

* * *

"_if you want to have good ideas, you must **have lots of ideas**  
and learn to **throw away the bad ones**_"  
\- Linus Pauling -

![Image 18](https://luminate-research.github.io/assets/gif/fixation.gif)

Creative processes typically begin with generating and exploring multiple ideas rather than refining a single one. Without first exploring diverse ideas, one can hastily converge on a suboptimal idea and spend time iterating it without considering other options. This is known as fixation, a phenomenon that hinders creative processes.

![Image 19](https://luminate-research.github.io/assets/gif/design-space-thinking.gif)

Another key to success in creative processes is being able to think about the space of possible ideas — referred to as design space thinking.

![Image 20](https://luminate-research.github.io/assets/gif/llm-for-creativity.gif)

Today, large language models (LLMs) offer an unprecedented opportunity to support these needs. Specifically, the capacity to instantly produce tens to hundreds of outputs empowers them to address fixation by offering users a set of ideas different from the current set of ideas. Moreover, they can generate diverse ideas to reveal the design space to users. However, current user interaction paradigms for LLMs do not fully harness this potential.

* * *

_Prompting for Design Space_  
(Structured Multi-Output Approach)

![Image 21](https://luminate-research.github.io/assets/img/framework-comparison.png)

The current interaction paradigm with LLMs — prompt engineering — constrains us to generating a _single_ output and then iterating on it. This is illustrated in the figure above as the (A) Unstructured Single-Output approach. Another approach found in recent work that generates _multiple_ outputs from a single prompt is referred to as the (B) Unstructured Multi-Output approach.

We propose the (C) Structured Multi-Output approach, where _structured_ denotes the presence of **dimensions** relevant to the task/domain to guide the response generation and _unstructured_ their absence.

_What do we mean by **dimensions** and why do we need **them**?_

The figure below provides an example that shows the benefits of exposing design space to users and how **dimensions** can assist this.

![Image 22](https://luminate-research.github.io/assets/img/framework-example.png)

By generating relevant dimensions for a task or topic, we can inform users about many dimensions and \[values\] they can consider — e.g., plot complexity: \[linear, twisting, ...\], genre: \[fantasy, adventure, ...\]. If all the possible dimensions and values are used to generate responses, the responses will cover many sub-spaces within the overall design space and reveal to users a space of possible responses they can generate with LLMs.

We introduce ![Image 23](https://luminate-research.github.io/assets/favicon/luminate-icon.png)Luminate, an interactive system that uses our _Prompting for Design Space_ framework to enable structured generation and exploration of design space with LLMs.

Video Demo
----------

* * *

Bibtex
------

  @inproceedings{10.1145/3613904.3642400,
    author = {Suh, Sangho and Chen, Meng and Min, Bryan and Li, Toby Jia-Jun and Xia, Haijun},
    title = {Luminate: Structured Generation and Exploration of Design Space with Large Language Models for Human-AI Co-Creation},
    year = {2024},
    isbn = {9798400703300},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3613904.3642400},
    doi = {10.1145/3613904.3642400},
    abstract = {Thanks to their generative capabilities, large language models (LLMs) have become an invaluable tool for creative processes. These models have the capacity to produce hundreds and thousands of visual and textual outputs, offering abundant inspiration for creative endeavors. But are we harnessing their full potential? We argue that current interaction paradigms fall short, guiding users towards rapid convergence on a limited set of ideas, rather than empowering them to explore the vast latent design space in generative models. To address this limitation, we propose a framework that facilitates the structured generation of design space in which users can seamlessly explore, evaluate, and synthesize a multitude of responses. We demonstrate the feasibility and usefulness of this framework through the design and development of an interactive system, Luminate, and a user study with 14 professional writers. Our work advances how we interact with LLMs for creative tasks, introducing a way to harness the creative potential of LLMs.},
    booktitle = {Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems},
    articleno = {644},
    numpages = {26},
    keywords = {Large language models, creativity support, design space, dimensional exploration, human-AI co-creation, human-AI interaction},
    location = {Honolulu, HI, USA},
    series = {CHI '24}
  }

## Metadata

```json
{
  "title": "Luminate",
  "description": "",
  "url": "https://luminate-research.github.io/",
  "content": "* * *\n\n\"_if you want to have good ideas, you must **have lots of ideas**  \nand learn to **throw away the bad ones**_\"  \n\\- Linus Pauling -\n\n![Image 18](https://luminate-research.github.io/assets/gif/fixation.gif)\n\nCreative processes typically begin with generating and exploring multiple ideas rather than refining a single one. Without first exploring diverse ideas, one can hastily converge on a suboptimal idea and spend time iterating it without considering other options. This is known as fixation, a phenomenon that hinders creative processes.\n\n![Image 19](https://luminate-research.github.io/assets/gif/design-space-thinking.gif)\n\nAnother key to success in creative processes is being able to think about the space of possible ideas — referred to as design space thinking.\n\n![Image 20](https://luminate-research.github.io/assets/gif/llm-for-creativity.gif)\n\nToday, large language models (LLMs) offer an unprecedented opportunity to support these needs. Specifically, the capacity to instantly produce tens to hundreds of outputs empowers them to address fixation by offering users a set of ideas different from the current set of ideas. Moreover, they can generate diverse ideas to reveal the design space to users. However, current user interaction paradigms for LLMs do not fully harness this potential.\n\n* * *\n\n_Prompting for Design Space_  \n(Structured Multi-Output Approach)\n\n![Image 21](https://luminate-research.github.io/assets/img/framework-comparison.png)\n\nThe current interaction paradigm with LLMs — prompt engineering — constrains us to generating a _single_ output and then iterating on it. This is illustrated in the figure above as the (A) Unstructured Single-Output approach. Another approach found in recent work that generates _multiple_ outputs from a single prompt is referred to as the (B) Unstructured Multi-Output approach.\n\nWe propose the (C) Structured Multi-Output approach, where _structured_ denotes the presence of **dimensions** relevant to the task/domain to guide the response generation and _unstructured_ their absence.\n\n_What do we mean by **dimensions** and why do we need **them**?_\n\nThe figure below provides an example that shows the benefits of exposing design space to users and how **dimensions** can assist this.\n\n![Image 22](https://luminate-research.github.io/assets/img/framework-example.png)\n\nBy generating relevant dimensions for a task or topic, we can inform users about many dimensions and \\[values\\] they can consider — e.g., plot complexity: \\[linear, twisting, ...\\], genre: \\[fantasy, adventure, ...\\]. If all the possible dimensions and values are used to generate responses, the responses will cover many sub-spaces within the overall design space and reveal to users a space of possible responses they can generate with LLMs.\n\nWe introduce ![Image 23](https://luminate-research.github.io/assets/favicon/luminate-icon.png)Luminate, an interactive system that uses our _Prompting for Design Space_ framework to enable structured generation and exploration of design space with LLMs.\n\nVideo Demo\n----------\n\n* * *\n\nBibtex\n------\n\n  @inproceedings{10.1145/3613904.3642400,\n    author = {Suh, Sangho and Chen, Meng and Min, Bryan and Li, Toby Jia-Jun and Xia, Haijun},\n    title = {Luminate: Structured Generation and Exploration of Design Space with Large Language Models for Human-AI Co-Creation},\n    year = {2024},\n    isbn = {9798400703300},\n    publisher = {Association for Computing Machinery},\n    address = {New York, NY, USA},\n    url = {https://doi.org/10.1145/3613904.3642400},\n    doi = {10.1145/3613904.3642400},\n    abstract = {Thanks to their generative capabilities, large language models (LLMs) have become an invaluable tool for creative processes. These models have the capacity to produce hundreds and thousands of visual and textual outputs, offering abundant inspiration for creative endeavors. But are we harnessing their full potential? We argue that current interaction paradigms fall short, guiding users towards rapid convergence on a limited set of ideas, rather than empowering them to explore the vast latent design space in generative models. To address this limitation, we propose a framework that facilitates the structured generation of design space in which users can seamlessly explore, evaluate, and synthesize a multitude of responses. We demonstrate the feasibility and usefulness of this framework through the design and development of an interactive system, Luminate, and a user study with 14 professional writers. Our work advances how we interact with LLMs for creative tasks, introducing a way to harness the creative potential of LLMs.},\n    booktitle = {Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems},\n    articleno = {644},\n    numpages = {26},\n    keywords = {Large language models, creativity support, design space, dimensional exploration, human-AI co-creation, human-AI interaction},\n    location = {Honolulu, HI, USA},\n    series = {CHI '24}\n  }",
  "usage": {
    "tokens": 1094
  }
}
```
