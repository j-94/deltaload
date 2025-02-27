---
title: Conformal Temporal Logic Planning using Large Language Models: Knowing When to Do What and When to Ask for Help
description: Conformal Temporal Logic Planning using Large Language Models: Knowing When to Do What and When to Ask for Help
url: https://ltl-llm.github.io/
timestamp: 2025-01-20T15:46:27.008Z
domain: ltl-llm.github.io
path: root
---

# Conformal Temporal Logic Planning using Large Language Models: Knowing When to Do What and When to Ask for Help


Conformal Temporal Logic Planning using Large Language Models: Knowing When to Do What and When to Ask for Help


## Content

![Image 10](https://ltl-llm.github.io/img/github.png)

#### **Code (coming soon)**

![Image 11](https://ltl-llm.github.io/img/colab.png)

#### **Demo (coming soon)**

  

### Abstract

This project addresses a new motion planning problem for mobile robots tasked with accomplishing multiple high-level sub-tasks, expressed using natural language (NL), in a temporal and logical order. To formally define such missions, we leverage LTL defined over NL-based atomic predicates modeling the considered NL-based sub-tasks. This is contrast to related planning approaches that define LTL tasks over atomic predicates capturing desired low-level system configurations. Our goal is to design robot plans that satisfy LTL tasks defined over NL-based atomic propositions. A novel technical challenge arising in this setup lies in reasoning about correctness of a robot plan with respect to such LTL-encoded tasks. To address this problem, we propose HERACLEs, a hierarchical conformal natural language planner, that relies on a novel integration of existing tools that include (i) automata theory to determine the NL-specified sub-task the robot should accomplish next to make mission progress; (ii) Large Language Models to design robot plans satisfying these sub-tasks; and (iii) conformal prediction to reason probabilistically about the correctness of the designed plans and mission satisfaction and to determine if external assistance is required. We provide extensive comparative experiments on mobile manipulation tasks. Paper can be found [here](https://arxiv.org/abs/2309.10092).

### Framework Structure

![Image 12](https://ltl-llm.github.io/img/framework.png)

More details coming soon.

### Experiment Video 1: Reacting to unknown environments

### Experiment Video 2: Reacting to ambiguous NL instructions

### Experiment Video 3: Demonstration on complex mobile manipulation tasks

### Experiment Video 4: Baseline Demonstration

### Acknowledgements

We thank Samarth Kalluraya for useful feedback on the project. The website template is from [Code as Policies](https://code-as-policies.github.io/).

## Metadata

```json
{
  "title": "Conformal Temporal Logic Planning using Large Language Models: Knowing When to Do What and When to Ask for Help",
  "description": "Conformal Temporal Logic Planning using Large Language Models: Knowing When to Do What and When to Ask for Help",
  "url": "https://ltl-llm.github.io/",
  "content": "![Image 10](https://ltl-llm.github.io/img/github.png)\n\n#### **Code (coming soon)**\n\n![Image 11](https://ltl-llm.github.io/img/colab.png)\n\n#### **Demo (coming soon)**\n\n  \n\n### Abstract\n\nThis project addresses a new motion planning problem for mobile robots tasked with accomplishing multiple high-level sub-tasks, expressed using natural language (NL), in a temporal and logical order. To formally define such missions, we leverage LTL defined over NL-based atomic predicates modeling the considered NL-based sub-tasks. This is contrast to related planning approaches that define LTL tasks over atomic predicates capturing desired low-level system configurations. Our goal is to design robot plans that satisfy LTL tasks defined over NL-based atomic propositions. A novel technical challenge arising in this setup lies in reasoning about correctness of a robot plan with respect to such LTL-encoded tasks. To address this problem, we propose HERACLEs, a hierarchical conformal natural language planner, that relies on a novel integration of existing tools that include (i) automata theory to determine the NL-specified sub-task the robot should accomplish next to make mission progress; (ii) Large Language Models to design robot plans satisfying these sub-tasks; and (iii) conformal prediction to reason probabilistically about the correctness of the designed plans and mission satisfaction and to determine if external assistance is required. We provide extensive comparative experiments on mobile manipulation tasks. Paper can be found [here](https://arxiv.org/abs/2309.10092).\n\n### Framework Structure\n\n![Image 12](https://ltl-llm.github.io/img/framework.png)\n\nMore details coming soon.\n\n### Experiment Video 1: Reacting to unknown environments\n\n### Experiment Video 2: Reacting to ambiguous NL instructions\n\n### Experiment Video 3: Demonstration on complex mobile manipulation tasks\n\n### Experiment Video 4: Baseline Demonstration\n\n### Acknowledgements\n\nWe thank Samarth Kalluraya for useful feedback on the project. The website template is from [Code as Policies](https://code-as-policies.github.io/).",
  "usage": {
    "tokens": 434
  }
}
```
