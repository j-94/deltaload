---
title: Paper page - Prometheus: Inducing Fine-grained Evaluation Capability in Language
  Models
description: Join the discussion on this paper page
url: https://huggingface.co/papers/2310.08491
timestamp: 2025-01-20T15:48:41.784Z
domain: huggingface.co
path: papers_2310.08491
---

# Paper page - Prometheus: Inducing Fine-grained Evaluation Capability in Language
  Models


Join the discussion on this paper page


## Content

Paper page - Prometheus: Inducing Fine-grained Evaluation Capability in Language Models
===============

 [![Image 46: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)

*   [Models](https://huggingface.co/models)
*   [Datasets](https://huggingface.co/datasets)
*   [Spaces](https://huggingface.co/spaces)
*   [Posts](https://huggingface.co/posts)
*   [Docs](https://huggingface.co/docs)
*   [Enterprise](https://huggingface.co/enterprise)
*   [Pricing](https://huggingface.co/pricing)

*   * * *
    
*   [Log In](https://huggingface.co/login)
*   [Sign Up](https://huggingface.co/join)

[Papers](https://huggingface.co/papers)

arxiv:2310.08491

Prometheus: Inducing Fine-grained Evaluation Capability in Language Models
==========================================================================

Published on Oct 12, 2023

· Submitted by [![Image 47](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Oct 12, 2023

[#1 Paper of the day](https://huggingface.co/papers?date=2023-10-12)

 [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2310.08491)

*   [![Image 48](https://huggingface.co/avatars/8157573c4c269f8f432a7dcb208ccc11.svg)](https://huggingface.co/huggingchatman "huggingchatman")
*   [![Image 49](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw "tokestermw")
*   [![Image 50](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri "taesiri")
*   [![Image 51](https://cdn-avatars.huggingface.co/v1/production/uploads/63e087b6a98d931aa90c1b9c/96c6IT3f1pWGLbRdRDB2U.png)](https://huggingface.co/Cartinoe5930 "Cartinoe5930")
*   [![Image 52](https://cdn-avatars.huggingface.co/v1/production/uploads/60c8d264224e250fb0178f77/i8fbkBVcoFeJRmkQ9kYAE.png)](https://huggingface.co/Abecid "Abecid")
*   [![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/1668887565024-noauth.png)](https://huggingface.co/AxAI "AxAI")
*   [![Image 54](https://huggingface.co/avatars/c82f20c56705f5c5f6e83bf5ad5db1a9.svg)](https://huggingface.co/masoudhashemi "masoudhashemi")
*   [![Image 55](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c "julien-c")
*   +45

Authors:

 ![Image 56](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/Lk7IJAR16Wa_sGJ2g81AQ.jpeg) [Seungone Kim](https://huggingface.co/seungone) ,

Jamin Shin ,

Yejin Cho ,

 ![Image 57](https://huggingface.co/avatars/49edaa425bbce04dff92bbfb12a6b41c.svg) [Joel Jang](https://huggingface.co/wkddydpf) ,

 ![Image 58](https://huggingface.co/avatars/a1cf1ef1fd442c36ed65c68e51919fed.svg) [Shayne Longpre](https://huggingface.co/Shayne) ,

 ![Image 59](https://huggingface.co/avatars/0105b9b152bc897dd36d0d9b8a590ddf.svg) [Hwaran Lee](https://huggingface.co/hwaranlee) ,

 ![Image 60](https://huggingface.co/avatars/27189e289b808ef01689ff2abb7a56bf.svg) [Sangdoo Yun](https://huggingface.co/oodgnas) ,

 ![Image 61](https://huggingface.co/avatars/7b053800e3cf35b61d4af15180618f23.svg) [Seongjin Shin](https://huggingface.co/optimalc) ,

 ![Image 62](https://huggingface.co/avatars/c56fb056800c145e5a8234e27b6b5a31.svg) [Sungdong Kim](https://huggingface.co/dsksd) ,

 ![Image 63](https://cdn-avatars.huggingface.co/v1/production/uploads/63b54db5889aa6707f08f2d1/zUnyx-8Zabxr54poZtUo4.jpeg) [James Thorne](https://huggingface.co/j6mes) ,

 ![Image 64](https://huggingface.co/avatars/7e1902aa71369a524afda9b0a9e88e22.svg) [Minjoon Seo](https://huggingface.co/minjoon)

Abstract
--------

Recently, using a powerful proprietary Large Language Model (LLM) (e.g., GPT-4) as an evaluator for long-form responses has become the de facto standard. However, for practitioners with large-scale evaluation tasks and custom criteria in consideration (e.g., child-readability), using proprietary LLMs as an evaluator is unreliable due to the closed-source nature, uncontrolled versioning, and prohibitive costs. In this work, we propose Prometheus, a fully open-source LLM that is on par with GPT-4's evaluation capabilities when the appropriate reference materials (reference answer, score rubric) are accompanied. We first construct the Feedback Collection, a new dataset that consists of 1K fine-grained score rubrics, 20K instructions, and 100K responses and language feedback generated by GPT-4. Using the Feedback Collection, we train Prometheus, a 13B evaluator LLM that can assess any given long-form text based on customized score rubric provided by the user. Experimental results show that Prometheus scores a Pearson correlation of 0.897 with human evaluators when evaluating with 45 customized score rubrics, which is on par with GPT-4 (0.882), and greatly outperforms ChatGPT (0.392). Furthermore, measuring correlation with GPT-4 with 1222 customized score rubrics across four benchmarks (MT Bench, Vicuna Bench, Feedback Bench, Flask Eval) shows similar trends, bolstering Prometheus's capability as an evaluator LLM. Lastly, Prometheus achieves the highest accuracy on two human preference benchmarks (HHH Alignment & MT Bench Human Judgment) compared to open-sourced reward models explicitly trained on human preference datasets, highlighting its potential as an universal reward model. We open-source our code, dataset, and model at https://github.com/kaistAI/Prometheus.

[View arXiv page](https://arxiv.org/abs/2310.08491) [View PDF](https://arxiv.org/pdf/2310.08491) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2310.08491)

### Community

 ![Image 65](https://cdn-avatars.huggingface.co/v1/production/uploads/63e087b6a98d931aa90c1b9c/96c6IT3f1pWGLbRdRDB2U.png) [Cartinoe5930](https://huggingface.co/Cartinoe5930)[Oct 14, 2023](https://huggingface.co/papers/2310.08491#652a8e7f30355beba68c1be6)

The review of 'Prometheus🔥: Inducing Fine-grained Evaluation Capability in Language Models'! 🤗

Abstract
--------

*   Prometheus was proposed in the paper. This model is a fully open-source LLM that is on par with GPT-4's evaluation capabilities.
*   Feedback Collection which used for training of Prometheus was proposed in the paper. This dataset consists of 1K fine-grained score rubrics, 20K instruction, and 100K responses and language feedback generated by GPT-4.
*   Prometheus shows high correlation with GPT-4. In addition, Prometheus achieves the high accuracy on two human preference benchmarks(HHH Alignment & MT-Bench Human Judgment)

The Feedback Collection Dataset
-------------------------------

Feedback Collection, a new dataset for the sole purpose of fine-tuning the Prometheus. The 4 considerations of Feedback Collection are as follows:

1.  Including as many reference materials(i.e. reference answer & scoring rubric) as possible.
2.  Maintaining a uniform length among the reference answer for each score(1 to 5) to prevent undesired length bias.
3.  Maintaining a uniform score distribution to prevent undesired decision bias.
4.  Limiting the scope of instructions and responses to realistic situations where a user is interacting with a LLM.

The individual components of Feedback Collection are as follows:  
[![Image 66: 스크린샷 2023-10-14 214812.png](https://cdn-uploads.huggingface.co/production/uploads/63e087b6a98d931aa90c1b9c/2kYfxviiE_cPRhNFINNy4.png)](https://cdn-uploads.huggingface.co/production/uploads/63e087b6a98d931aa90c1b9c/2kYfxviiE_cPRhNFINNy4.png)

#### The components of Feedback Collection

*   Input
    
    1.  Instruction: An instruction that a user would prompt to an arbitrary LLM.
    2.  Response to Evaluate: A response to the instruction that the evaluator LM has to evaluate.
    3.  Customized Score Rubric: A specification of novel criteria decided by the user.
    4.  Reference Answer: A reference answer that would receive a score of 5. It enables the evaluator to use the mutual information between the reference answer and the response to make a scoring decision.
*   Output
    
    1.  Feedback: A rationale of why the provided response would receive a particular score.
    2.  Score: An integer score for the provided response that ranges from 1 to 5.

#### Fine-tuning an Evaluator LM

Using the Feedback Collection dataset, Llama-2-Chat(7B & 13B) were fine-tuned -\> Prometheus🔥

Experiment Setting
------------------

In the paper, human evaluation & GPT-4 Evaluation were used as a standard and measure how similarly Prometheus and baselines could closely simulate them. For this, Absolute Grading & Ranking Grading were used.

*   Absolute Grading: The evaluator LM should generate a feedback and score within the range of 1 to 5 given an instruction, a response to evaluate, and reference materials. The following three experiments were conducted using Absolute Grading:
    
    1.  Measuring the correlation with human evaluator
    2.  Comparing the quality of the feedback using human evaluation
    3.  Measuring the correlation with GPT-4 evaluation
    
    *   Used Benchmarks: Feedback Bench, Vicuna Bench, MT-Bench, FLASK Eval
*   Ranking Grading: When two responses are given, a method of evaluating which response is better by scoring.
    
    *   Used Benchmarks: MT-Bench Human Judgment, HHH Alignment

Experimental Results
--------------------

#### 1\. Can Prometheus Closely Simulate Human Evaluation?

*   Correlation with Human Scoring: Prometheus shows high correlation in all Feedback Bench, MT-Bench, and Vicuna Bench. This is on par with GPT-4 or slightly outperforms.
*   Pairwise Comparison of the Feedback with Human Evaluation: In terms of human preference, Prometheus shows a tendency to be preferred over other models.
*   Analysis of Why Prometheus's Feedback was Preferred: GPT-4 tends to be more meutral and abstract, Prometheus shows a clear trend of expressing its opinion of whether the given response is good or not.

#### 2\. Can Prometheus Closely Simulate GPT-4 Evaluation?

*   Correlation with GPT-4 Scoring: Prometheus shows the high correlation with GPT-4 compared to other better models such as Llama-2-Chat-70B or ChatGPT. In addition, the result shows that the training directly on the evaluation dataset might be the best option to acquire a task-specific evaluator LLM.

#### 3\. Can Prometheus Function as a Reward Model?

Training on an absolute grading scheme could also improve performance on a ranking grading scheme even without directly training on ranking evaluation instances. Moreover, it shows the possibilities of using Prometheus as a reward model for RLHF!

It was truly amazing that it was able to fine-tune an open-source model using high-quality feedback data and show evaluation performance on par with the proprietary model! Thank you so much for conducting this wonderful research!

※ It was just an abstractive summarization containing a lot of missed information. If you want to see more specific information, I hope you can take the time to read the paper carefully.

👍

6

6

❤️

4

4

+

Reply

 ![Image 67](https://huggingface.co/avatars/f2c5a056d7011172cb42ce03d2b5f109.svg) [Blessian](https://huggingface.co/Blessian)[Oct 16, 2023](https://huggingface.co/papers/2310.08491#652c9d16c59e682042024bfb)

This comment has been hidden

+

 ![Image 68](https://huggingface.co/avatars/f2c5a056d7011172cb42ce03d2b5f109.svg) [Blessian](https://huggingface.co/Blessian)[Oct 16, 2023](https://huggingface.co/papers/2310.08491#652c9d1bd78452c474392054)

This comment has been hidden

+

 ![Image 69](https://huggingface.co/avatars/716b6a7d1094c8036b2a8a7b9063e8aa.svg) [blanchon](https://huggingface.co/blanchon)[Jun 8, 2024](https://huggingface.co/papers/2310.08491#6664c555328aac4bb12feaf7)

How Prometheus Rivals GPT-4 in Evaluating AI Responses!
=======================================================

Links 🔗:
---------

👉 Subscribe: [https://www.youtube.com/@Arxflix](https://www.youtube.com/@Arxflix)  
👉 Twitter: [https://x.com/arxflix](https://x.com/arxflix)  
👉 LMNT (Partner): [https://lmnt.com/](https://lmnt.com/)

By Arxflix  
[![Image 70: 9t4iCUHx_400x400-1.jpg](https://cdn-uploads.huggingface.co/production/uploads/6186ddf6a7717cb375090c01/v4S5zBurs0ouGNwYj1GEd.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/6186ddf6a7717cb375090c01/v4S5zBurs0ouGNwYj1GEd.jpeg)

+

Reply

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

Comment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2310.08491) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2310.08491) to comment

 [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2310.08491)

*   [![Image 71](https://huggingface.co/avatars/8157573c4c269f8f432a7dcb208ccc11.svg)](https://huggingface.co/huggingchatman "huggingchatman")
*   [![Image 72](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw "tokestermw")
*   [![Image 73](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri "taesiri")
*   [![Image 74](https://cdn-avatars.huggingface.co/v1/production/uploads/63e087b6a98d931aa90c1b9c/96c6IT3f1pWGLbRdRDB2U.png)](https://huggingface.co/Cartinoe5930 "Cartinoe5930")
*   [![Image 75](https://cdn-avatars.huggingface.co/v1/production/uploads/60c8d264224e250fb0178f77/i8fbkBVcoFeJRmkQ9kYAE.png)](https://huggingface.co/Abecid "Abecid")
*   [![Image 76](https://cdn-avatars.huggingface.co/v1/production/uploads/1668887565024-noauth.png)](https://huggingface.co/AxAI "AxAI")
*   [![Image 77](https://huggingface.co/avatars/c82f20c56705f5c5f6e83bf5ad5db1a9.svg)](https://huggingface.co/masoudhashemi "masoudhashemi")
*   [![Image 78](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c "julien-c")
*   [![Image 79](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/MlxSi2hP-G0av-h2qhwoG.jpeg)](https://huggingface.co/DrHanjo "DrHanjo")
*   [![Image 80](https://huggingface.co/avatars/6671941ced18ae516db6ebfbf73e239f.svg)](https://huggingface.co/juandavidgf "juandavidgf")
*   [![Image 81](https://cdn-avatars.huggingface.co/v1/production/uploads/64f3d15b77b0eb97ea1ec8b2/y_3DjdOr5reXzTvHwn-xT.jpeg)](https://huggingface.co/csnyder "csnyder")
*   [![Image 82](https://huggingface.co/avatars/f0d08ca26eb24e52eed9e0f380f9581a.svg)](https://huggingface.co/Furinkan9999 "Furinkan9999")
*   +41

Models citing this paper 37
---------------------------

[![Image 83](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-13b-v1.0 Text2Text Generation • Updated Oct 14, 2023 • 3.73k • 134](https://huggingface.co/prometheus-eval/prometheus-13b-v1.0)

[![Image 84](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-7b-v2.0 Text2Text Generation • Updated Nov 29, 2024 • 24.1k • 83](https://huggingface.co/prometheus-eval/prometheus-7b-v2.0)

[![Image 85](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-8x7b-v2.0 Text2Text Generation • Updated Nov 29, 2024 • 1.31k • 47](https://huggingface.co/prometheus-eval/prometheus-8x7b-v2.0)

[![Image 86](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-7b-v1.0 Text2Text Generation • Updated Oct 14, 2023 • 117 • 30](https://huggingface.co/prometheus-eval/prometheus-7b-v1.0)

[Browse 37 models citing this paper](https://huggingface.co/models?other=arxiv:2310.08491)

Datasets citing this paper 4
----------------------------

[#### prometheus-eval/Feedback-Collection Viewer • Updated Oct 14, 2023 • 100k • 423 • 108](https://huggingface.co/datasets/prometheus-eval/Feedback-Collection)

[#### prometheus-eval/Preference-Collection Viewer • Updated May 3, 2024 • 200k • 100 • 33](https://huggingface.co/datasets/prometheus-eval/Preference-Collection)

[#### d0rj/Feedback-Collection-ru Viewer • Updated Jun 6, 2024 • 100k • 64 • 3](https://huggingface.co/datasets/d0rj/Feedback-Collection-ru)

[#### pharaouk/Feedback-Collection Updated Apr 10, 2024 • 46](https://huggingface.co/datasets/pharaouk/Feedback-Collection)

### Spaces citing this paper 12

[💻 featherless-ai/try-this-model](https://huggingface.co/spaces/featherless-ai/try-this-model)[💻 AtlaAI/judge-arena](https://huggingface.co/spaces/AtlaAI/judge-arena)[📚 Darok/Featherless-Feud](https://huggingface.co/spaces/Darok/Featherless-Feud)[💻 emekaboris/try-this-model](https://huggingface.co/spaces/emekaboris/try-this-model)[💻 SC999/NV\_Nemotron](https://huggingface.co/spaces/SC999/NV_Nemotron)[⚖️ Tonic/prometheus](https://huggingface.co/spaces/Tonic/prometheus)[🌍 burtenshaw/disticleaner](https://huggingface.co/spaces/burtenshaw/disticleaner)[💻 JackHoltone/try-this-model](https://huggingface.co/spaces/JackHoltone/try-this-model)[💻 k11112/try-this-model](https://huggingface.co/spaces/k11112/try-this-model)[📊 iishanbhandarii/llm\_eval](https://huggingface.co/spaces/iishanbhandarii/llm_eval)[📚 youns2001/vsevolodl-prometheus-7b-v2.0-GGUF](https://huggingface.co/spaces/youns2001/vsevolodl-prometheus-7b-v2.0-GGUF)[🏆 johnoye742/kaist-ai-prometheus-13b-v1.0](https://huggingface.co/spaces/johnoye742/kaist-ai-prometheus-13b-v1.0)\+ 7 Spaces

Collections including this paper 22
-----------------------------------

[#### Dataset generation Collection 126 items • Updated Jul 22, 2024 • 26](https://huggingface.co/collections/stereoplegic/dataset-generation-65389dd75510eb595f8a3797)

[#### RL/Alignment Collection 197 items • Updated Jun 18, 2024 • 23](https://huggingface.co/collections/stereoplegic/rl-alignment-65389cd60e9beb3a415b3c76)

[#### LLM as a Judge Collection Curated resources that support the use of LLMs to serve as automatic evaluators of other LLM outputs. • 20 items • Updated Dec 11, 2024 • 21](https://huggingface.co/collections/andrewrreed/llm-as-a-judge-653fb861e361fd03c12d41e5)

[#### Reading Papers Collection 220 items • Updated 10 days ago • 10](https://huggingface.co/collections/speechlessai/reading-papers-65ad5d8dc8903e28aeb3cf18)

[Browse 22 collections that include this paper](https://huggingface.co/collections?paper=2310.08491)

System theme

Company

[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)

Website

[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

## Metadata

```json
{
  "title": "Paper page - Prometheus: Inducing Fine-grained Evaluation Capability in Language\n  Models",
  "description": "Join the discussion on this paper page",
  "url": "https://huggingface.co/papers/2310.08491",
  "content": "Paper page - Prometheus: Inducing Fine-grained Evaluation Capability in Language Models\n===============\n\n [![Image 46: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)\n\n*   [Models](https://huggingface.co/models)\n*   [Datasets](https://huggingface.co/datasets)\n*   [Spaces](https://huggingface.co/spaces)\n*   [Posts](https://huggingface.co/posts)\n*   [Docs](https://huggingface.co/docs)\n*   [Enterprise](https://huggingface.co/enterprise)\n*   [Pricing](https://huggingface.co/pricing)\n\n*   * * *\n    \n*   [Log In](https://huggingface.co/login)\n*   [Sign Up](https://huggingface.co/join)\n\n[Papers](https://huggingface.co/papers)\n\narxiv:2310.08491\n\nPrometheus: Inducing Fine-grained Evaluation Capability in Language Models\n==========================================================================\n\nPublished on Oct 12, 2023\n\n· Submitted by [![Image 47](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Oct 12, 2023\n\n[#1 Paper of the day](https://huggingface.co/papers?date=2023-10-12)\n\n [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2310.08491)\n\n*   [![Image 48](https://huggingface.co/avatars/8157573c4c269f8f432a7dcb208ccc11.svg)](https://huggingface.co/huggingchatman \"huggingchatman\")\n*   [![Image 49](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw \"tokestermw\")\n*   [![Image 50](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri \"taesiri\")\n*   [![Image 51](https://cdn-avatars.huggingface.co/v1/production/uploads/63e087b6a98d931aa90c1b9c/96c6IT3f1pWGLbRdRDB2U.png)](https://huggingface.co/Cartinoe5930 \"Cartinoe5930\")\n*   [![Image 52](https://cdn-avatars.huggingface.co/v1/production/uploads/60c8d264224e250fb0178f77/i8fbkBVcoFeJRmkQ9kYAE.png)](https://huggingface.co/Abecid \"Abecid\")\n*   [![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/1668887565024-noauth.png)](https://huggingface.co/AxAI \"AxAI\")\n*   [![Image 54](https://huggingface.co/avatars/c82f20c56705f5c5f6e83bf5ad5db1a9.svg)](https://huggingface.co/masoudhashemi \"masoudhashemi\")\n*   [![Image 55](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c \"julien-c\")\n*   +45\n\nAuthors:\n\n ![Image 56](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/Lk7IJAR16Wa_sGJ2g81AQ.jpeg) [Seungone Kim](https://huggingface.co/seungone) ,\n\nJamin Shin ,\n\nYejin Cho ,\n\n ![Image 57](https://huggingface.co/avatars/49edaa425bbce04dff92bbfb12a6b41c.svg) [Joel Jang](https://huggingface.co/wkddydpf) ,\n\n ![Image 58](https://huggingface.co/avatars/a1cf1ef1fd442c36ed65c68e51919fed.svg) [Shayne Longpre](https://huggingface.co/Shayne) ,\n\n ![Image 59](https://huggingface.co/avatars/0105b9b152bc897dd36d0d9b8a590ddf.svg) [Hwaran Lee](https://huggingface.co/hwaranlee) ,\n\n ![Image 60](https://huggingface.co/avatars/27189e289b808ef01689ff2abb7a56bf.svg) [Sangdoo Yun](https://huggingface.co/oodgnas) ,\n\n ![Image 61](https://huggingface.co/avatars/7b053800e3cf35b61d4af15180618f23.svg) [Seongjin Shin](https://huggingface.co/optimalc) ,\n\n ![Image 62](https://huggingface.co/avatars/c56fb056800c145e5a8234e27b6b5a31.svg) [Sungdong Kim](https://huggingface.co/dsksd) ,\n\n ![Image 63](https://cdn-avatars.huggingface.co/v1/production/uploads/63b54db5889aa6707f08f2d1/zUnyx-8Zabxr54poZtUo4.jpeg) [James Thorne](https://huggingface.co/j6mes) ,\n\n ![Image 64](https://huggingface.co/avatars/7e1902aa71369a524afda9b0a9e88e22.svg) [Minjoon Seo](https://huggingface.co/minjoon)\n\nAbstract\n--------\n\nRecently, using a powerful proprietary Large Language Model (LLM) (e.g., GPT-4) as an evaluator for long-form responses has become the de facto standard. However, for practitioners with large-scale evaluation tasks and custom criteria in consideration (e.g., child-readability), using proprietary LLMs as an evaluator is unreliable due to the closed-source nature, uncontrolled versioning, and prohibitive costs. In this work, we propose Prometheus, a fully open-source LLM that is on par with GPT-4's evaluation capabilities when the appropriate reference materials (reference answer, score rubric) are accompanied. We first construct the Feedback Collection, a new dataset that consists of 1K fine-grained score rubrics, 20K instructions, and 100K responses and language feedback generated by GPT-4. Using the Feedback Collection, we train Prometheus, a 13B evaluator LLM that can assess any given long-form text based on customized score rubric provided by the user. Experimental results show that Prometheus scores a Pearson correlation of 0.897 with human evaluators when evaluating with 45 customized score rubrics, which is on par with GPT-4 (0.882), and greatly outperforms ChatGPT (0.392). Furthermore, measuring correlation with GPT-4 with 1222 customized score rubrics across four benchmarks (MT Bench, Vicuna Bench, Feedback Bench, Flask Eval) shows similar trends, bolstering Prometheus's capability as an evaluator LLM. Lastly, Prometheus achieves the highest accuracy on two human preference benchmarks (HHH Alignment & MT Bench Human Judgment) compared to open-sourced reward models explicitly trained on human preference datasets, highlighting its potential as an universal reward model. We open-source our code, dataset, and model at https://github.com/kaistAI/Prometheus.\n\n[View arXiv page](https://arxiv.org/abs/2310.08491) [View PDF](https://arxiv.org/pdf/2310.08491) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2310.08491)\n\n### Community\n\n ![Image 65](https://cdn-avatars.huggingface.co/v1/production/uploads/63e087b6a98d931aa90c1b9c/96c6IT3f1pWGLbRdRDB2U.png) [Cartinoe5930](https://huggingface.co/Cartinoe5930)[Oct 14, 2023](https://huggingface.co/papers/2310.08491#652a8e7f30355beba68c1be6)\n\nThe review of 'Prometheus🔥: Inducing Fine-grained Evaluation Capability in Language Models'! 🤗\n\nAbstract\n--------\n\n*   Prometheus was proposed in the paper. This model is a fully open-source LLM that is on par with GPT-4's evaluation capabilities.\n*   Feedback Collection which used for training of Prometheus was proposed in the paper. This dataset consists of 1K fine-grained score rubrics, 20K instruction, and 100K responses and language feedback generated by GPT-4.\n*   Prometheus shows high correlation with GPT-4. In addition, Prometheus achieves the high accuracy on two human preference benchmarks(HHH Alignment & MT-Bench Human Judgment)\n\nThe Feedback Collection Dataset\n-------------------------------\n\nFeedback Collection, a new dataset for the sole purpose of fine-tuning the Prometheus. The 4 considerations of Feedback Collection are as follows:\n\n1.  Including as many reference materials(i.e. reference answer & scoring rubric) as possible.\n2.  Maintaining a uniform length among the reference answer for each score(1 to 5) to prevent undesired length bias.\n3.  Maintaining a uniform score distribution to prevent undesired decision bias.\n4.  Limiting the scope of instructions and responses to realistic situations where a user is interacting with a LLM.\n\nThe individual components of Feedback Collection are as follows:  \n[![Image 66: 스크린샷 2023-10-14 214812.png](https://cdn-uploads.huggingface.co/production/uploads/63e087b6a98d931aa90c1b9c/2kYfxviiE_cPRhNFINNy4.png)](https://cdn-uploads.huggingface.co/production/uploads/63e087b6a98d931aa90c1b9c/2kYfxviiE_cPRhNFINNy4.png)\n\n#### The components of Feedback Collection\n\n*   Input\n    \n    1.  Instruction: An instruction that a user would prompt to an arbitrary LLM.\n    2.  Response to Evaluate: A response to the instruction that the evaluator LM has to evaluate.\n    3.  Customized Score Rubric: A specification of novel criteria decided by the user.\n    4.  Reference Answer: A reference answer that would receive a score of 5. It enables the evaluator to use the mutual information between the reference answer and the response to make a scoring decision.\n*   Output\n    \n    1.  Feedback: A rationale of why the provided response would receive a particular score.\n    2.  Score: An integer score for the provided response that ranges from 1 to 5.\n\n#### Fine-tuning an Evaluator LM\n\nUsing the Feedback Collection dataset, Llama-2-Chat(7B & 13B) were fine-tuned -\\> Prometheus🔥\n\nExperiment Setting\n------------------\n\nIn the paper, human evaluation & GPT-4 Evaluation were used as a standard and measure how similarly Prometheus and baselines could closely simulate them. For this, Absolute Grading & Ranking Grading were used.\n\n*   Absolute Grading: The evaluator LM should generate a feedback and score within the range of 1 to 5 given an instruction, a response to evaluate, and reference materials. The following three experiments were conducted using Absolute Grading:\n    \n    1.  Measuring the correlation with human evaluator\n    2.  Comparing the quality of the feedback using human evaluation\n    3.  Measuring the correlation with GPT-4 evaluation\n    \n    *   Used Benchmarks: Feedback Bench, Vicuna Bench, MT-Bench, FLASK Eval\n*   Ranking Grading: When two responses are given, a method of evaluating which response is better by scoring.\n    \n    *   Used Benchmarks: MT-Bench Human Judgment, HHH Alignment\n\nExperimental Results\n--------------------\n\n#### 1\\. Can Prometheus Closely Simulate Human Evaluation?\n\n*   Correlation with Human Scoring: Prometheus shows high correlation in all Feedback Bench, MT-Bench, and Vicuna Bench. This is on par with GPT-4 or slightly outperforms.\n*   Pairwise Comparison of the Feedback with Human Evaluation: In terms of human preference, Prometheus shows a tendency to be preferred over other models.\n*   Analysis of Why Prometheus's Feedback was Preferred: GPT-4 tends to be more meutral and abstract, Prometheus shows a clear trend of expressing its opinion of whether the given response is good or not.\n\n#### 2\\. Can Prometheus Closely Simulate GPT-4 Evaluation?\n\n*   Correlation with GPT-4 Scoring: Prometheus shows the high correlation with GPT-4 compared to other better models such as Llama-2-Chat-70B or ChatGPT. In addition, the result shows that the training directly on the evaluation dataset might be the best option to acquire a task-specific evaluator LLM.\n\n#### 3\\. Can Prometheus Function as a Reward Model?\n\nTraining on an absolute grading scheme could also improve performance on a ranking grading scheme even without directly training on ranking evaluation instances. Moreover, it shows the possibilities of using Prometheus as a reward model for RLHF!\n\nIt was truly amazing that it was able to fine-tune an open-source model using high-quality feedback data and show evaluation performance on par with the proprietary model! Thank you so much for conducting this wonderful research!\n\n※ It was just an abstractive summarization containing a lot of missed information. If you want to see more specific information, I hope you can take the time to read the paper carefully.\n\n👍\n\n6\n\n6\n\n❤️\n\n4\n\n4\n\n+\n\nReply\n\n ![Image 67](https://huggingface.co/avatars/f2c5a056d7011172cb42ce03d2b5f109.svg) [Blessian](https://huggingface.co/Blessian)[Oct 16, 2023](https://huggingface.co/papers/2310.08491#652c9d16c59e682042024bfb)\n\nThis comment has been hidden\n\n+\n\n ![Image 68](https://huggingface.co/avatars/f2c5a056d7011172cb42ce03d2b5f109.svg) [Blessian](https://huggingface.co/Blessian)[Oct 16, 2023](https://huggingface.co/papers/2310.08491#652c9d1bd78452c474392054)\n\nThis comment has been hidden\n\n+\n\n ![Image 69](https://huggingface.co/avatars/716b6a7d1094c8036b2a8a7b9063e8aa.svg) [blanchon](https://huggingface.co/blanchon)[Jun 8, 2024](https://huggingface.co/papers/2310.08491#6664c555328aac4bb12feaf7)\n\nHow Prometheus Rivals GPT-4 in Evaluating AI Responses!\n=======================================================\n\nLinks 🔗:\n---------\n\n👉 Subscribe: [https://www.youtube.com/@Arxflix](https://www.youtube.com/@Arxflix)  \n👉 Twitter: [https://x.com/arxflix](https://x.com/arxflix)  \n👉 LMNT (Partner): [https://lmnt.com/](https://lmnt.com/)\n\nBy Arxflix  \n[![Image 70: 9t4iCUHx_400x400-1.jpg](https://cdn-uploads.huggingface.co/production/uploads/6186ddf6a7717cb375090c01/v4S5zBurs0ouGNwYj1GEd.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/6186ddf6a7717cb375090c01/v4S5zBurs0ouGNwYj1GEd.jpeg)\n\n+\n\nReply\n\nEditPreview\n\nUpload images, audio, and videos by dragging in the text input, pasting, or clicking here.\n\nTap or paste here to upload images\n\nComment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2310.08491) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2310.08491) to comment\n\n [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2310.08491)\n\n*   [![Image 71](https://huggingface.co/avatars/8157573c4c269f8f432a7dcb208ccc11.svg)](https://huggingface.co/huggingchatman \"huggingchatman\")\n*   [![Image 72](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw \"tokestermw\")\n*   [![Image 73](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri \"taesiri\")\n*   [![Image 74](https://cdn-avatars.huggingface.co/v1/production/uploads/63e087b6a98d931aa90c1b9c/96c6IT3f1pWGLbRdRDB2U.png)](https://huggingface.co/Cartinoe5930 \"Cartinoe5930\")\n*   [![Image 75](https://cdn-avatars.huggingface.co/v1/production/uploads/60c8d264224e250fb0178f77/i8fbkBVcoFeJRmkQ9kYAE.png)](https://huggingface.co/Abecid \"Abecid\")\n*   [![Image 76](https://cdn-avatars.huggingface.co/v1/production/uploads/1668887565024-noauth.png)](https://huggingface.co/AxAI \"AxAI\")\n*   [![Image 77](https://huggingface.co/avatars/c82f20c56705f5c5f6e83bf5ad5db1a9.svg)](https://huggingface.co/masoudhashemi \"masoudhashemi\")\n*   [![Image 78](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c \"julien-c\")\n*   [![Image 79](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/MlxSi2hP-G0av-h2qhwoG.jpeg)](https://huggingface.co/DrHanjo \"DrHanjo\")\n*   [![Image 80](https://huggingface.co/avatars/6671941ced18ae516db6ebfbf73e239f.svg)](https://huggingface.co/juandavidgf \"juandavidgf\")\n*   [![Image 81](https://cdn-avatars.huggingface.co/v1/production/uploads/64f3d15b77b0eb97ea1ec8b2/y_3DjdOr5reXzTvHwn-xT.jpeg)](https://huggingface.co/csnyder \"csnyder\")\n*   [![Image 82](https://huggingface.co/avatars/f0d08ca26eb24e52eed9e0f380f9581a.svg)](https://huggingface.co/Furinkan9999 \"Furinkan9999\")\n*   +41\n\nModels citing this paper 37\n---------------------------\n\n[![Image 83](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-13b-v1.0 Text2Text Generation • Updated Oct 14, 2023 • 3.73k • 134](https://huggingface.co/prometheus-eval/prometheus-13b-v1.0)\n\n[![Image 84](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-7b-v2.0 Text2Text Generation • Updated Nov 29, 2024 • 24.1k • 83](https://huggingface.co/prometheus-eval/prometheus-7b-v2.0)\n\n[![Image 85](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-8x7b-v2.0 Text2Text Generation • Updated Nov 29, 2024 • 1.31k • 47](https://huggingface.co/prometheus-eval/prometheus-8x7b-v2.0)\n\n[![Image 86](https://cdn-avatars.huggingface.co/v1/production/uploads/6469949654873f0043b09c22/ooULtecFGFMPRkUxevBty.jpeg) #### prometheus-eval/prometheus-7b-v1.0 Text2Text Generation • Updated Oct 14, 2023 • 117 • 30](https://huggingface.co/prometheus-eval/prometheus-7b-v1.0)\n\n[Browse 37 models citing this paper](https://huggingface.co/models?other=arxiv:2310.08491)\n\nDatasets citing this paper 4\n----------------------------\n\n[#### prometheus-eval/Feedback-Collection Viewer • Updated Oct 14, 2023 • 100k • 423 • 108](https://huggingface.co/datasets/prometheus-eval/Feedback-Collection)\n\n[#### prometheus-eval/Preference-Collection Viewer • Updated May 3, 2024 • 200k • 100 • 33](https://huggingface.co/datasets/prometheus-eval/Preference-Collection)\n\n[#### d0rj/Feedback-Collection-ru Viewer • Updated Jun 6, 2024 • 100k • 64 • 3](https://huggingface.co/datasets/d0rj/Feedback-Collection-ru)\n\n[#### pharaouk/Feedback-Collection Updated Apr 10, 2024 • 46](https://huggingface.co/datasets/pharaouk/Feedback-Collection)\n\n### Spaces citing this paper 12\n\n[💻 featherless-ai/try-this-model](https://huggingface.co/spaces/featherless-ai/try-this-model)[💻 AtlaAI/judge-arena](https://huggingface.co/spaces/AtlaAI/judge-arena)[📚 Darok/Featherless-Feud](https://huggingface.co/spaces/Darok/Featherless-Feud)[💻 emekaboris/try-this-model](https://huggingface.co/spaces/emekaboris/try-this-model)[💻 SC999/NV\\_Nemotron](https://huggingface.co/spaces/SC999/NV_Nemotron)[⚖️ Tonic/prometheus](https://huggingface.co/spaces/Tonic/prometheus)[🌍 burtenshaw/disticleaner](https://huggingface.co/spaces/burtenshaw/disticleaner)[💻 JackHoltone/try-this-model](https://huggingface.co/spaces/JackHoltone/try-this-model)[💻 k11112/try-this-model](https://huggingface.co/spaces/k11112/try-this-model)[📊 iishanbhandarii/llm\\_eval](https://huggingface.co/spaces/iishanbhandarii/llm_eval)[📚 youns2001/vsevolodl-prometheus-7b-v2.0-GGUF](https://huggingface.co/spaces/youns2001/vsevolodl-prometheus-7b-v2.0-GGUF)[🏆 johnoye742/kaist-ai-prometheus-13b-v1.0](https://huggingface.co/spaces/johnoye742/kaist-ai-prometheus-13b-v1.0)\\+ 7 Spaces\n\nCollections including this paper 22\n-----------------------------------\n\n[#### Dataset generation Collection 126 items • Updated Jul 22, 2024 • 26](https://huggingface.co/collections/stereoplegic/dataset-generation-65389dd75510eb595f8a3797)\n\n[#### RL/Alignment Collection 197 items • Updated Jun 18, 2024 • 23](https://huggingface.co/collections/stereoplegic/rl-alignment-65389cd60e9beb3a415b3c76)\n\n[#### LLM as a Judge Collection Curated resources that support the use of LLMs to serve as automatic evaluators of other LLM outputs. • 20 items • Updated Dec 11, 2024 • 21](https://huggingface.co/collections/andrewrreed/llm-as-a-judge-653fb861e361fd03c12d41e5)\n\n[#### Reading Papers Collection 220 items • Updated 10 days ago • 10](https://huggingface.co/collections/speechlessai/reading-papers-65ad5d8dc8903e28aeb3cf18)\n\n[Browse 22 collections that include this paper](https://huggingface.co/collections?paper=2310.08491)\n\nSystem theme\n\nCompany\n\n[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)\n\nWebsite\n\n[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)",
  "usage": {
    "tokens": 5980
  }
}
```
