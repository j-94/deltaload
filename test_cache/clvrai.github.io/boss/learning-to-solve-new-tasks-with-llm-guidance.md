---
title: Learning to Solve New Tasks with LLM Guidance
description: Bootstrap Your Own Skills: Learning to Solve New Tasks with LLM Guidance.
url: https://clvrai.github.io/boss/
timestamp: 2025-01-20T15:54:42.772Z
domain: clvrai.github.io
path: boss
---

# Learning to Solve New Tasks with LLM Guidance


Bootstrap Your Own Skills: Learning to Solve New Tasks with LLM Guidance.


## Content

Bootstrap Your Own Skills: Learning to Solve New Tasks with LLM Guidance
------------------------------------------------------------------------

1University of Southern California 2Google AI 3National Taiwan University 4KAIST

**Conference on Robot Learning 2023**

**Oral Presentation (top 6.6%)**

Abstract
--------

We propose **BOSS** (**B**oot**S**trapping your **O**wn **S**kill**S**), an approach that automatically learns to solve new long-horizon, complex, and meaningful tasks in new environments by growing a learned skill library with Large Language Model (LLM) supervision.

  

* * *

Bootstrap Your Own Skills (BOSS) Method  

------------------------------------------

BOSS automatically learns to solve new long horizon, complex tasks in new environments by guiding an agent to grow a language-specified skill library tailored for the target environment during the **skill bootstrapping phase**. After skill bootstrapping, we can simply condition the learned policy on language descriptions for new tasks.

![Image 32: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/boss_overview.png)

Training a BOSS agent consists of two phases: (1) it acquires a base repertoire of language-specified skills and (2) it practices chaining these skills into long-horizon behaviors in the skill bootstrapping phase. BOSS can then zero-shot execute novel natural language instructions describing complex long-horizon tasks.

#### 1\. Pre-training a Language-Conditioned Skill Policy

To obtain a language-conditioned primitive skill policy, we pre-train a policy and critic with offline RL on a dataset of easier to collect short-horizon, language-annotated trajectories. In our experiments, we use Implicit Q-Learning (IQL) as it is performant and amenable to online fine-tuning.

#### 2\. Skill Bootstrapping

We perform skill bootstrapping — the agent practices by interacting with the target environment, trying new skill chains, then adding them back into its skill repertoire for further bootstrapping. As a result, the agent learns increasingly long-horizon skills without requiring additional supervision beyond the initial set of skills.

1.  **Sampling initial skills.**  
    In every bootstrapping episode, we sample the initial skill according to probabilities generated from the pre-trained value function (indicating skill success probabilities). The agent then tries to execute the sampled skill.  
    
2.  **Guiding Skill Chaining via LLMs.**  
    If the first skill execution succeeds, the next step is constructing a longer-horizon behavior by chaining together the first skill with a sampled next skill. Instead of randomly sampling subsequent skills, we propose to use large language models (LLMs) to guide skill selection. We explore a bottom-up approach to learning long-horizon tasks: by allowing our agent to iteratively sample skill chains and practice their execution in the environment.  
    
3.  **Learning new skills.**  
    Once an episode concludes, we add the collected data back into the replay buffer and the newly learned skill back into the skill library for further bootstrapping. We fine-tune with the same offline RL algorithm to learn both new skills and improve execution of existing ones, and then repeat again from step 1.  
    

  

* * *

### Environments

![Image 33: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/env.png)

We compare to unsupervised RL and zero-shot planning methods in two challenging, image-based control environments: solving household tasks in the ALFRED simulator and kitchen manipulation tasks with a real-world Jaco robot arm.

**(a) ALFRED:** The ALFRED environment is a benchmark for learning agents that can follow natural language instructions to fulfill household tasks.  
**(b) Real World Kitchen:** Our real world kitchen manipulation tabletop environment with continuous control.

  

* * *

### Results

  

#### Real World Kitchen

We perform online skill bootstrapping for 17 min of robot interaction time (15k timesteps) on an unseen environment configuration. Language-conditioned evaluations below. Comparison against ProgPrompt implemented with GPT-3.5.

**Comparison against ProgPrompt implemented with GPT-3.5.**

  

![Image 34: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/ppg_sink_rack.gif)  
**ProgPrompt**

2/4 Skills Completed

![Image 35: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/bootstrap_sink_plate5.gif)  
**BOSS**

4/4 Skills Completed

Task: "Clean the black bowl and put in the dish rack."

![Image 36: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/ppg_sink_plate.gif)  
**ProgPrompt**

4/4 Skills Completed

![Image 37: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/bootstrap_sink_plate9.gif)  
**BOSS**

4/4 Skills Completed

Task: "Clean the black bowl and put in the gray plate."

#### Quantitative Results

We show the cumulative returns and task success rates for zero-shot bootstrapped policies vs other methods. Even with SayCan policies are fine-tuned (SayCan+FT) for the same number of steps, the success rate is still 0 while BOSS is the only method that achieves non-zero success rates.

![Image 38: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/real_result.png)

LLM-planning mechanisms like ProgPrompt have no standard fine-tuning procedure and therefore the policy is less effective at chaining skills together even when ProgPrompt breaks it down into step-by-step instructions.

#### ALFRED

We perform online skill bootstrapping in 40 unseen environment configurations for 500k timesteps.

*   **SayCan+P**: (LLM-based planning + value function guidance) with the same skill proposal mechanism that BOSS uses.
  
*   **CIC**: (state of the art unsupervised RL) pre-trained on the same data and fine-tuned for 500,000 environment steps with unsupervised RL to discover interesting skills.
  

![Image 39: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/CIC_eval_plunger.gif) **CIC**

Completes no tasks as its unsupervised skill learning objective is unable to truly learn meaningful skills.

![Image 40: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/SAYCAN_eval_plunger.gif) **SayCan**

Gets stuck while navigating; not even completing the first skill due to policy execution errors.

![Image 41: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/BOSS_eval_2_plunger.gif)

**BOSS**

Completes 2/2 sub-tasks through what it learned from skill bootstrapping in this environment.

Task: "Put the plunger in the sink."

![Image 42: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/CIC_eval_3_apple.gif) **CIC**

Completes 0 sub-tasks, generally learns more random behaviors that may get stuck navigating.

![Image 43: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/SAYCAN_eval_3_apple.gif) **SayCan**

Completes 0 sub-tasks, the policy is confused by the incorrect instruction produced by the LLM.

![Image 44: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/BOSS_eval_3_apple.gif)

**BOSS**

Completes 3/6 sub-tasks---picks up the potato at the end instead of the apple. Overall, still better than the baselines.

Task: "Put cooked apple slice on a counter."

#### Quantitative Results

We show the cumulative returns and task success rates for zero-shot bootstrapped policies vs other methods.

![Image 45: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/new_alfred_result.png)

#### Result Analysis

We plot the skill lengths of learned skills over time on the left. Skill bootstrapping is able to learn meaningful, longer horizon skills over time. On the right, we see that the skill library also grows over time.

![Image 46: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/skill_dist.png)

  

* * *

  

Q & A
-----

#### How is BOSS different from [SayCan](https://say-can.github.io/)?

The difference against SayCan and other similar LLM planning works is that they perform top-down planning of pre-trained/fixed policies (the policies can be learned or planning-based) directly in the target environment. BOSS, on the other hand, builds a skill library bottom-up tailored for the target environment and continually fine-tunes a learned agent on this skill library. This results in an agent which can better transition between skills and does not require an LLM planner at test-time to break down long-horizon tasks into primitive skill sequences for the agent to execute.

  

#### How is this different from [SPRINT](https://clvrai.github.io/sprint/)?

SPRINT focuses on pre-training policies for efficient adaptation given the intended target tasks. SPRINT uses an LLM to aggregate skills together with a higher-level task instruction, which we also use in BOSS. Meanwhile, BOSS is an algorithm that allows the agent to autonomously acquire new skills without knowing the intended target tasks in new environments.

  

#### What are the limitations of BOSS?

We see two main limitations. The first is the need for environment resets between episodes, which we hope reset-free RL can help resolve in the future. The second is the requirement of data and sparse reward functions for the primitive skills which are used to compose all new learned skills. Data is difficult to collect and even sparse reward functions may be hard to acquire in the real world, so one way to allow BOSS to acquire even more skills would be to allow it to perform reward-free acquisition of new skills.

BibTeX
------

```
@inproceedings{
    zhang2023bootstrap,
    title={Bootstrap Your Own Skills: Learning to Solve New Tasks with Large Language Model Guidance},
    author={Jesse Zhang and Jiahui Zhang and Karl Pertsch and Ziyi Liu and Xiang Ren and Minsuk Chang and Shao-Hua Sun and Joseph J Lim},
    booktitle={7th Annual Conference on Robot Learning},
    year={2023},
    url={https://openreview.net/forum?id=a0mFRgadGO}
}
```

## Metadata

```json
{
  "title": "Learning to Solve New Tasks with LLM Guidance",
  "description": "Bootstrap Your Own Skills: Learning to Solve New Tasks with LLM Guidance.",
  "url": "https://clvrai.github.io/boss/",
  "content": "Bootstrap Your Own Skills: Learning to Solve New Tasks with LLM Guidance\n------------------------------------------------------------------------\n\n1University of Southern California 2Google AI 3National Taiwan University 4KAIST\n\n**Conference on Robot Learning 2023**\n\n**Oral Presentation (top 6.6%)**\n\nAbstract\n--------\n\nWe propose **BOSS** (**B**oot**S**trapping your **O**wn **S**kill**S**), an approach that automatically learns to solve new long-horizon, complex, and meaningful tasks in new environments by growing a learned skill library with Large Language Model (LLM) supervision.\n\n  \n\n* * *\n\nBootstrap Your Own Skills (BOSS) Method  \n\n------------------------------------------\n\nBOSS automatically learns to solve new long horizon, complex tasks in new environments by guiding an agent to grow a language-specified skill library tailored for the target environment during the **skill bootstrapping phase**. After skill bootstrapping, we can simply condition the learned policy on language descriptions for new tasks.\n\n![Image 32: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/boss_overview.png)\n\nTraining a BOSS agent consists of two phases: (1) it acquires a base repertoire of language-specified skills and (2) it practices chaining these skills into long-horizon behaviors in the skill bootstrapping phase. BOSS can then zero-shot execute novel natural language instructions describing complex long-horizon tasks.\n\n#### 1\\. Pre-training a Language-Conditioned Skill Policy\n\nTo obtain a language-conditioned primitive skill policy, we pre-train a policy and critic with offline RL on a dataset of easier to collect short-horizon, language-annotated trajectories. In our experiments, we use Implicit Q-Learning (IQL) as it is performant and amenable to online fine-tuning.\n\n#### 2\\. Skill Bootstrapping\n\nWe perform skill bootstrapping — the agent practices by interacting with the target environment, trying new skill chains, then adding them back into its skill repertoire for further bootstrapping. As a result, the agent learns increasingly long-horizon skills without requiring additional supervision beyond the initial set of skills.\n\n1.  **Sampling initial skills.**  \n    In every bootstrapping episode, we sample the initial skill according to probabilities generated from the pre-trained value function (indicating skill success probabilities). The agent then tries to execute the sampled skill.  \n    \n2.  **Guiding Skill Chaining via LLMs.**  \n    If the first skill execution succeeds, the next step is constructing a longer-horizon behavior by chaining together the first skill with a sampled next skill. Instead of randomly sampling subsequent skills, we propose to use large language models (LLMs) to guide skill selection. We explore a bottom-up approach to learning long-horizon tasks: by allowing our agent to iteratively sample skill chains and practice their execution in the environment.  \n    \n3.  **Learning new skills.**  \n    Once an episode concludes, we add the collected data back into the replay buffer and the newly learned skill back into the skill library for further bootstrapping. We fine-tune with the same offline RL algorithm to learn both new skills and improve execution of existing ones, and then repeat again from step 1.  \n    \n\n  \n\n* * *\n\n### Environments\n\n![Image 33: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/env.png)\n\nWe compare to unsupervised RL and zero-shot planning methods in two challenging, image-based control environments: solving household tasks in the ALFRED simulator and kitchen manipulation tasks with a real-world Jaco robot arm.\n\n**(a) ALFRED:** The ALFRED environment is a benchmark for learning agents that can follow natural language instructions to fulfill household tasks.  \n**(b) Real World Kitchen:** Our real world kitchen manipulation tabletop environment with continuous control.\n\n  \n\n* * *\n\n### Results\n\n  \n\n#### Real World Kitchen\n\nWe perform online skill bootstrapping for 17 min of robot interaction time (15k timesteps) on an unseen environment configuration. Language-conditioned evaluations below. Comparison against ProgPrompt implemented with GPT-3.5.\n\n**Comparison against ProgPrompt implemented with GPT-3.5.**\n\n  \n\n![Image 34: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/ppg_sink_rack.gif)  \n**ProgPrompt**\n\n2/4 Skills Completed\n\n![Image 35: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/bootstrap_sink_plate5.gif)  \n**BOSS**\n\n4/4 Skills Completed\n\nTask: \"Clean the black bowl and put in the dish rack.\"\n\n![Image 36: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/ppg_sink_plate.gif)  \n**ProgPrompt**\n\n4/4 Skills Completed\n\n![Image 37: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/bootstrap_sink_plate9.gif)  \n**BOSS**\n\n4/4 Skills Completed\n\nTask: \"Clean the black bowl and put in the gray plate.\"\n\n#### Quantitative Results\n\nWe show the cumulative returns and task success rates for zero-shot bootstrapped policies vs other methods. Even with SayCan policies are fine-tuned (SayCan+FT) for the same number of steps, the success rate is still 0 while BOSS is the only method that achieves non-zero success rates.\n\n![Image 38: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/real_result.png)\n\nLLM-planning mechanisms like ProgPrompt have no standard fine-tuning procedure and therefore the policy is less effective at chaining skills together even when ProgPrompt breaks it down into step-by-step instructions.\n\n#### ALFRED\n\nWe perform online skill bootstrapping in 40 unseen environment configurations for 500k timesteps.\n\n*   **SayCan+P**: (LLM-based planning + value function guidance) with the same skill proposal mechanism that BOSS uses.\n  \n*   **CIC**: (state of the art unsupervised RL) pre-trained on the same data and fine-tuned for 500,000 environment steps with unsupervised RL to discover interesting skills.\n  \n\n![Image 39: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/CIC_eval_plunger.gif) **CIC**\n\nCompletes no tasks as its unsupervised skill learning objective is unable to truly learn meaningful skills.\n\n![Image 40: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/SAYCAN_eval_plunger.gif) **SayCan**\n\nGets stuck while navigating; not even completing the first skill due to policy execution errors.\n\n![Image 41: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/BOSS_eval_2_plunger.gif)\n\n**BOSS**\n\nCompletes 2/2 sub-tasks through what it learned from skill bootstrapping in this environment.\n\nTask: \"Put the plunger in the sink.\"\n\n![Image 42: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/CIC_eval_3_apple.gif) **CIC**\n\nCompletes 0 sub-tasks, generally learns more random behaviors that may get stuck navigating.\n\n![Image 43: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/SAYCAN_eval_3_apple.gif) **SayCan**\n\nCompletes 0 sub-tasks, the policy is confused by the incorrect instruction produced by the LLM.\n\n![Image 44: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/BOSS_eval_3_apple.gif)\n\n**BOSS**\n\nCompletes 3/6 sub-tasks---picks up the potato at the end instead of the apple. Overall, still better than the baselines.\n\nTask: \"Put cooked apple slice on a counter.\"\n\n#### Quantitative Results\n\nWe show the cumulative returns and task success rates for zero-shot bootstrapped policies vs other methods.\n\n![Image 45: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/new_alfred_result.png)\n\n#### Result Analysis\n\nWe plot the skill lengths of learned skills over time on the left. Skill bootstrapping is able to learn meaningful, longer horizon skills over time. On the right, we see that the skill library also grows over time.\n\n![Image 46: Interpolate start reference image.](https://clvrai.github.io/boss/static/images/skill_dist.png)\n\n  \n\n* * *\n\n  \n\nQ & A\n-----\n\n#### How is BOSS different from [SayCan](https://say-can.github.io/)?\n\nThe difference against SayCan and other similar LLM planning works is that they perform top-down planning of pre-trained/fixed policies (the policies can be learned or planning-based) directly in the target environment. BOSS, on the other hand, builds a skill library bottom-up tailored for the target environment and continually fine-tunes a learned agent on this skill library. This results in an agent which can better transition between skills and does not require an LLM planner at test-time to break down long-horizon tasks into primitive skill sequences for the agent to execute.\n\n  \n\n#### How is this different from [SPRINT](https://clvrai.github.io/sprint/)?\n\nSPRINT focuses on pre-training policies for efficient adaptation given the intended target tasks. SPRINT uses an LLM to aggregate skills together with a higher-level task instruction, which we also use in BOSS. Meanwhile, BOSS is an algorithm that allows the agent to autonomously acquire new skills without knowing the intended target tasks in new environments.\n\n  \n\n#### What are the limitations of BOSS?\n\nWe see two main limitations. The first is the need for environment resets between episodes, which we hope reset-free RL can help resolve in the future. The second is the requirement of data and sparse reward functions for the primitive skills which are used to compose all new learned skills. Data is difficult to collect and even sparse reward functions may be hard to acquire in the real world, so one way to allow BOSS to acquire even more skills would be to allow it to perform reward-free acquisition of new skills.\n\nBibTeX\n------\n\n```\n@inproceedings{\n    zhang2023bootstrap,\n    title={Bootstrap Your Own Skills: Learning to Solve New Tasks with Large Language Model Guidance},\n    author={Jesse Zhang and Jiahui Zhang and Karl Pertsch and Ziyi Liu and Xiang Ren and Minsuk Chang and Shao-Hua Sun and Joseph J Lim},\n    booktitle={7th Annual Conference on Robot Learning},\n    year={2023},\n    url={https://openreview.net/forum?id=a0mFRgadGO}\n}\n```",
  "usage": {
    "tokens": 2269
  }
}
```
