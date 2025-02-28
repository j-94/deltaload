---
title: Paper page - DSPy: Compiling Declarative Language Model Calls into Self-Improving
  Pipelines
description: Join the discussion on this paper page
url: https://huggingface.co/papers/2310.03714
timestamp: 2025-01-20T15:47:53.034Z
domain: huggingface.co
path: papers_2310.03714
---

# Paper page - DSPy: Compiling Declarative Language Model Calls into Self-Improving
  Pipelines


Join the discussion on this paper page


## Content

Paper page - DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines
===============

 [![Image 32: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)

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

arxiv:2310.03714

DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines
==============================================================================

Published on Oct 5, 2023

· Submitted by [![Image 33](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Oct 5, 2023

[#2 Paper of the day](https://huggingface.co/papers?date=2023-10-05)

 [Upvote 33](https://huggingface.co/login?next=%2Fpapers%2F2310.03714)

*   [![Image 34](https://cdn-avatars.huggingface.co/v1/production/uploads/5e5045ca37cb5b49818287cf/VyH_N8BbPgVVRE7gYGiMn.jpeg)](https://huggingface.co/DanielhCarranza "DanielhCarranza")
*   [![Image 35](https://huggingface.co/avatars/e83ac95c9117b46aeb2a514e06da4d18.svg)](https://huggingface.co/ameasure "ameasure")
*   [![Image 36](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c "julien-c")
*   [![Image 37](https://huggingface.co/avatars/88bb4c4a67dc8958069e9014f5e73a0b.svg)](https://huggingface.co/MichaelBarryUK "MichaelBarryUK")
*   [![Image 38](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw "tokestermw")
*   [![Image 39](https://huggingface.co/avatars/9445f6efa3f78a870e338988d9ce5573.svg)](https://huggingface.co/okhattab "okhattab")
*   [![Image 40](https://huggingface.co/avatars/980856a022bf5a25c268a5be46c08f74.svg)](https://huggingface.co/Aurjfbkfkehz "Aurjfbkfkehz")
*   [![Image 41](https://huggingface.co/avatars/2e70fa6aeade1643241de97aa73c911b.svg)](https://huggingface.co/cheng1 "cheng1")
*   +25

Authors:

 ![Image 42](https://huggingface.co/avatars/9445f6efa3f78a870e338988d9ce5573.svg) [Omar Khattab](https://huggingface.co/okhattab) ,

 ![Image 43](https://huggingface.co/avatars/e1e5fe6f814d549721927daab4d7e8b6.svg) [Arnav Singhvi](https://huggingface.co/arnavs11) ,

 ![Image 44](https://huggingface.co/avatars/59552e26a13183607ebb668669476b39.svg) [Paridhi Maheshwari](https://huggingface.co/paridhi) ,

Zhiyuan Zhang ,

 ![Image 45](https://huggingface.co/avatars/017e15cad6406653a9340cdbbee7dc51.svg) [Keshav Santhanam](https://huggingface.co/santhnm2) ,

Sri Vardhamanan ,

Saiful Haq ,

Ashutosh Sharma ,

Thomas T. Joshi ,

 ![Image 46](https://huggingface.co/avatars/982a90c601c9d5eb4f2c3828ebc106ee.svg) [Hanna Moazam](https://huggingface.co/hmoazam) ,

 ![Image 47](https://huggingface.co/avatars/49a4815846825cd1334fa080c6e71c5d.svg) [Heather Miller](https://huggingface.co/heathercmiller) ,

 ![Image 48](https://cdn-avatars.huggingface.co/v1/production/uploads/642509c6d476e4ad5568dd31/dPiEV70hMeuY-cveLNPQg.jpeg) [Matei Zaharia](https://huggingface.co/mateiz) ,

 ![Image 49](https://cdn-avatars.huggingface.co/v1/production/uploads/1650485126923-noauth.png) [Christopher Potts](https://huggingface.co/cgpotts)

Abstract
--------

The ML community is rapidly exploring techniques for prompting language models (LMs) and for stacking them into pipelines that solve complex tasks. Unfortunately, existing LM pipelines are typically implemented using hard-coded "prompt templates", i.e. lengthy strings discovered via trial and error. Toward a more systematic approach for developing and optimizing LM pipelines, we introduce DSPy, a programming model that abstracts LM pipelines as text transformation graphs, i.e. imperative computational graphs where LMs are invoked through declarative modules. DSPy modules are parameterized, meaning they can learn (by creating and collecting demonstrations) how to apply compositions of prompting, finetuning, augmentation, and reasoning techniques. We design a compiler that will optimize any DSPy pipeline to maximize a given metric. We conduct two case studies, showing that succinct DSPy programs can express and optimize sophisticated LM pipelines that reason about math word problems, tackle multi-hop retrieval, answer complex questions, and control agent loops. Within minutes of compiling, a few lines of DSPy allow GPT-3.5 and llama2-13b-chat to self-bootstrap pipelines that outperform standard few-shot prompting (generally by over 25% and 65%, respectively) and pipelines with expert-created demonstrations (by up to 5-46% and 16-40%, respectively). On top of that, DSPy programs compiled to open and relatively small LMs like 770M-parameter T5 and llama2-13b-chat are competitive with approaches that rely on expert-written prompt chains for proprietary GPT-3.5. DSPy is available at https://github.com/stanfordnlp/dspy

[View arXiv page](https://arxiv.org/abs/2310.03714) [View PDF](https://arxiv.org/pdf/2310.03714) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2310.03714)

### Community

 ![Image 50](https://cdn-avatars.huggingface.co/v1/production/uploads/1674830754237-63d3e0e8ff1384ce6c5dd17d.jpeg) [librarian-bot](https://huggingface.co/librarian-bot)[Oct 7, 2023](https://huggingface.co/papers/2310.03714#652150c4b80dc49ba0fd3b92)

This is an automated message from the [Librarian Bot](https://huggingface.co/librarian-bots). I found the following papers similar to this paper.

The following papers were recommended by the Semantic Scholar API

*   [CodeCoT and Beyond: Learning to Program and Test like a Developer](https://huggingface.co/papers/2308.08784) (2023)
*   [AskIt: Unified Programming Interface for Programming with Large Language Models](https://huggingface.co/papers/2308.15645) (2023)
*   [Prompt2Model: Generating Deployable Models from Natural Language Instructions](https://huggingface.co/papers/2308.12261) (2023)
*   [LLM Guided Inductive Inference for Solving Compositional Problems](https://huggingface.co/papers/2309.11688) (2023)
*   [Natural Language Embedded Programs for Hybrid Language Symbolic Reasoning](https://huggingface.co/papers/2309.10814) (2023)

Please give a thumbs up to this comment if you found it helpful!

If you want recommendations for any Paper on Hugging Face checkout [this](https://huggingface.co/spaces/librarian-bots/recommend_similar_papers) Space

👍

3

3

+

Reply

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

Comment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2310.03714) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2310.03714) to comment

 [Upvote 33](https://huggingface.co/login?next=%2Fpapers%2F2310.03714)

*   [![Image 51](https://cdn-avatars.huggingface.co/v1/production/uploads/5e5045ca37cb5b49818287cf/VyH_N8BbPgVVRE7gYGiMn.jpeg)](https://huggingface.co/DanielhCarranza "DanielhCarranza")
*   [![Image 52](https://huggingface.co/avatars/e83ac95c9117b46aeb2a514e06da4d18.svg)](https://huggingface.co/ameasure "ameasure")
*   [![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c "julien-c")
*   [![Image 54](https://huggingface.co/avatars/88bb4c4a67dc8958069e9014f5e73a0b.svg)](https://huggingface.co/MichaelBarryUK "MichaelBarryUK")
*   [![Image 55](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw "tokestermw")
*   [![Image 56](https://huggingface.co/avatars/9445f6efa3f78a870e338988d9ce5573.svg)](https://huggingface.co/okhattab "okhattab")
*   [![Image 57](https://huggingface.co/avatars/980856a022bf5a25c268a5be46c08f74.svg)](https://huggingface.co/Aurjfbkfkehz "Aurjfbkfkehz")
*   [![Image 58](https://huggingface.co/avatars/2e70fa6aeade1643241de97aa73c911b.svg)](https://huggingface.co/cheng1 "cheng1")
*   [![Image 59](https://huggingface.co/avatars/3236c8cffb50c09f4e9cf91c5c781df8.svg)](https://huggingface.co/Boqiang "Boqiang")
*   [![Image 60](https://huggingface.co/avatars/0cba7c22c135f9c8fbe19398ba408923.svg)](https://huggingface.co/fbjr "fbjr")
*   [![Image 61](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri "taesiri")
*   [![Image 62](https://huggingface.co/avatars/e6dd4027945909c7cf13c61807c78f23.svg)](https://huggingface.co/SaeedAnas "SaeedAnas")
*   +21

Models citing this paper 0
--------------------------

No model linking this paper

Cite arxiv.org/abs/2310.03714 in a model README.md to link it from this page.

Datasets citing this paper 0
----------------------------

No dataset linking this paper

Cite arxiv.org/abs/2310.03714 in a dataset README.md to link it from this page.

### Spaces citing this paper 0

No Space linking this paper

Cite arxiv.org/abs/2310.03714 in a Space README.md to link it from this page.

Collections including this paper 21
-----------------------------------

[#### 🤖 Agents Collection 21 items • Updated 20 days ago • 106](https://huggingface.co/collections/m-ric/agents-65ba776fbd9e29f771c07d4e)

[#### Reasoning Collection 151 items • Updated Apr 6, 2024 • 29](https://huggingface.co/collections/stereoplegic/reasoning-6538a52e044e47f56050644e)

[#### RL/Alignment Collection 197 items • Updated Jun 18, 2024 • 23](https://huggingface.co/collections/stereoplegic/rl-alignment-65389cd60e9beb3a415b3c76)

[#### Agent Collection 112 items • Updated Sep 9, 2024 • 21](https://huggingface.co/collections/stereoplegic/agent-65389e7dcfc110ff79843a71)

[Browse 21 collections that include this paper](https://huggingface.co/collections?paper=2310.03714)

System theme

Company

[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)

Website

[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

## Metadata

```json
{
  "title": "Paper page - DSPy: Compiling Declarative Language Model Calls into Self-Improving\n  Pipelines",
  "description": "Join the discussion on this paper page",
  "url": "https://huggingface.co/papers/2310.03714",
  "content": "Paper page - DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines\n===============\n\n [![Image 32: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)\n\n*   [Models](https://huggingface.co/models)\n*   [Datasets](https://huggingface.co/datasets)\n*   [Spaces](https://huggingface.co/spaces)\n*   [Posts](https://huggingface.co/posts)\n*   [Docs](https://huggingface.co/docs)\n*   [Enterprise](https://huggingface.co/enterprise)\n*   [Pricing](https://huggingface.co/pricing)\n\n*   * * *\n    \n*   [Log In](https://huggingface.co/login)\n*   [Sign Up](https://huggingface.co/join)\n\n[Papers](https://huggingface.co/papers)\n\narxiv:2310.03714\n\nDSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines\n==============================================================================\n\nPublished on Oct 5, 2023\n\n· Submitted by [![Image 33](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Oct 5, 2023\n\n[#2 Paper of the day](https://huggingface.co/papers?date=2023-10-05)\n\n [Upvote 33](https://huggingface.co/login?next=%2Fpapers%2F2310.03714)\n\n*   [![Image 34](https://cdn-avatars.huggingface.co/v1/production/uploads/5e5045ca37cb5b49818287cf/VyH_N8BbPgVVRE7gYGiMn.jpeg)](https://huggingface.co/DanielhCarranza \"DanielhCarranza\")\n*   [![Image 35](https://huggingface.co/avatars/e83ac95c9117b46aeb2a514e06da4d18.svg)](https://huggingface.co/ameasure \"ameasure\")\n*   [![Image 36](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c \"julien-c\")\n*   [![Image 37](https://huggingface.co/avatars/88bb4c4a67dc8958069e9014f5e73a0b.svg)](https://huggingface.co/MichaelBarryUK \"MichaelBarryUK\")\n*   [![Image 38](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw \"tokestermw\")\n*   [![Image 39](https://huggingface.co/avatars/9445f6efa3f78a870e338988d9ce5573.svg)](https://huggingface.co/okhattab \"okhattab\")\n*   [![Image 40](https://huggingface.co/avatars/980856a022bf5a25c268a5be46c08f74.svg)](https://huggingface.co/Aurjfbkfkehz \"Aurjfbkfkehz\")\n*   [![Image 41](https://huggingface.co/avatars/2e70fa6aeade1643241de97aa73c911b.svg)](https://huggingface.co/cheng1 \"cheng1\")\n*   +25\n\nAuthors:\n\n ![Image 42](https://huggingface.co/avatars/9445f6efa3f78a870e338988d9ce5573.svg) [Omar Khattab](https://huggingface.co/okhattab) ,\n\n ![Image 43](https://huggingface.co/avatars/e1e5fe6f814d549721927daab4d7e8b6.svg) [Arnav Singhvi](https://huggingface.co/arnavs11) ,\n\n ![Image 44](https://huggingface.co/avatars/59552e26a13183607ebb668669476b39.svg) [Paridhi Maheshwari](https://huggingface.co/paridhi) ,\n\nZhiyuan Zhang ,\n\n ![Image 45](https://huggingface.co/avatars/017e15cad6406653a9340cdbbee7dc51.svg) [Keshav Santhanam](https://huggingface.co/santhnm2) ,\n\nSri Vardhamanan ,\n\nSaiful Haq ,\n\nAshutosh Sharma ,\n\nThomas T. Joshi ,\n\n ![Image 46](https://huggingface.co/avatars/982a90c601c9d5eb4f2c3828ebc106ee.svg) [Hanna Moazam](https://huggingface.co/hmoazam) ,\n\n ![Image 47](https://huggingface.co/avatars/49a4815846825cd1334fa080c6e71c5d.svg) [Heather Miller](https://huggingface.co/heathercmiller) ,\n\n ![Image 48](https://cdn-avatars.huggingface.co/v1/production/uploads/642509c6d476e4ad5568dd31/dPiEV70hMeuY-cveLNPQg.jpeg) [Matei Zaharia](https://huggingface.co/mateiz) ,\n\n ![Image 49](https://cdn-avatars.huggingface.co/v1/production/uploads/1650485126923-noauth.png) [Christopher Potts](https://huggingface.co/cgpotts)\n\nAbstract\n--------\n\nThe ML community is rapidly exploring techniques for prompting language models (LMs) and for stacking them into pipelines that solve complex tasks. Unfortunately, existing LM pipelines are typically implemented using hard-coded \"prompt templates\", i.e. lengthy strings discovered via trial and error. Toward a more systematic approach for developing and optimizing LM pipelines, we introduce DSPy, a programming model that abstracts LM pipelines as text transformation graphs, i.e. imperative computational graphs where LMs are invoked through declarative modules. DSPy modules are parameterized, meaning they can learn (by creating and collecting demonstrations) how to apply compositions of prompting, finetuning, augmentation, and reasoning techniques. We design a compiler that will optimize any DSPy pipeline to maximize a given metric. We conduct two case studies, showing that succinct DSPy programs can express and optimize sophisticated LM pipelines that reason about math word problems, tackle multi-hop retrieval, answer complex questions, and control agent loops. Within minutes of compiling, a few lines of DSPy allow GPT-3.5 and llama2-13b-chat to self-bootstrap pipelines that outperform standard few-shot prompting (generally by over 25% and 65%, respectively) and pipelines with expert-created demonstrations (by up to 5-46% and 16-40%, respectively). On top of that, DSPy programs compiled to open and relatively small LMs like 770M-parameter T5 and llama2-13b-chat are competitive with approaches that rely on expert-written prompt chains for proprietary GPT-3.5. DSPy is available at https://github.com/stanfordnlp/dspy\n\n[View arXiv page](https://arxiv.org/abs/2310.03714) [View PDF](https://arxiv.org/pdf/2310.03714) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2310.03714)\n\n### Community\n\n ![Image 50](https://cdn-avatars.huggingface.co/v1/production/uploads/1674830754237-63d3e0e8ff1384ce6c5dd17d.jpeg) [librarian-bot](https://huggingface.co/librarian-bot)[Oct 7, 2023](https://huggingface.co/papers/2310.03714#652150c4b80dc49ba0fd3b92)\n\nThis is an automated message from the [Librarian Bot](https://huggingface.co/librarian-bots). I found the following papers similar to this paper.\n\nThe following papers were recommended by the Semantic Scholar API\n\n*   [CodeCoT and Beyond: Learning to Program and Test like a Developer](https://huggingface.co/papers/2308.08784) (2023)\n*   [AskIt: Unified Programming Interface for Programming with Large Language Models](https://huggingface.co/papers/2308.15645) (2023)\n*   [Prompt2Model: Generating Deployable Models from Natural Language Instructions](https://huggingface.co/papers/2308.12261) (2023)\n*   [LLM Guided Inductive Inference for Solving Compositional Problems](https://huggingface.co/papers/2309.11688) (2023)\n*   [Natural Language Embedded Programs for Hybrid Language Symbolic Reasoning](https://huggingface.co/papers/2309.10814) (2023)\n\nPlease give a thumbs up to this comment if you found it helpful!\n\nIf you want recommendations for any Paper on Hugging Face checkout [this](https://huggingface.co/spaces/librarian-bots/recommend_similar_papers) Space\n\n👍\n\n3\n\n3\n\n+\n\nReply\n\nEditPreview\n\nUpload images, audio, and videos by dragging in the text input, pasting, or clicking here.\n\nTap or paste here to upload images\n\nComment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2310.03714) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2310.03714) to comment\n\n [Upvote 33](https://huggingface.co/login?next=%2Fpapers%2F2310.03714)\n\n*   [![Image 51](https://cdn-avatars.huggingface.co/v1/production/uploads/5e5045ca37cb5b49818287cf/VyH_N8BbPgVVRE7gYGiMn.jpeg)](https://huggingface.co/DanielhCarranza \"DanielhCarranza\")\n*   [![Image 52](https://huggingface.co/avatars/e83ac95c9117b46aeb2a514e06da4d18.svg)](https://huggingface.co/ameasure \"ameasure\")\n*   [![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg)](https://huggingface.co/julien-c \"julien-c\")\n*   [![Image 54](https://huggingface.co/avatars/88bb4c4a67dc8958069e9014f5e73a0b.svg)](https://huggingface.co/MichaelBarryUK \"MichaelBarryUK\")\n*   [![Image 55](https://cdn-avatars.huggingface.co/v1/production/uploads/60078446e55258e41786a959/UGPCE4YqG9BVMSf0YauxL.png)](https://huggingface.co/tokestermw \"tokestermw\")\n*   [![Image 56](https://huggingface.co/avatars/9445f6efa3f78a870e338988d9ce5573.svg)](https://huggingface.co/okhattab \"okhattab\")\n*   [![Image 57](https://huggingface.co/avatars/980856a022bf5a25c268a5be46c08f74.svg)](https://huggingface.co/Aurjfbkfkehz \"Aurjfbkfkehz\")\n*   [![Image 58](https://huggingface.co/avatars/2e70fa6aeade1643241de97aa73c911b.svg)](https://huggingface.co/cheng1 \"cheng1\")\n*   [![Image 59](https://huggingface.co/avatars/3236c8cffb50c09f4e9cf91c5c781df8.svg)](https://huggingface.co/Boqiang \"Boqiang\")\n*   [![Image 60](https://huggingface.co/avatars/0cba7c22c135f9c8fbe19398ba408923.svg)](https://huggingface.co/fbjr \"fbjr\")\n*   [![Image 61](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri \"taesiri\")\n*   [![Image 62](https://huggingface.co/avatars/e6dd4027945909c7cf13c61807c78f23.svg)](https://huggingface.co/SaeedAnas \"SaeedAnas\")\n*   +21\n\nModels citing this paper 0\n--------------------------\n\nNo model linking this paper\n\nCite arxiv.org/abs/2310.03714 in a model README.md to link it from this page.\n\nDatasets citing this paper 0\n----------------------------\n\nNo dataset linking this paper\n\nCite arxiv.org/abs/2310.03714 in a dataset README.md to link it from this page.\n\n### Spaces citing this paper 0\n\nNo Space linking this paper\n\nCite arxiv.org/abs/2310.03714 in a Space README.md to link it from this page.\n\nCollections including this paper 21\n-----------------------------------\n\n[#### 🤖 Agents Collection 21 items • Updated 20 days ago • 106](https://huggingface.co/collections/m-ric/agents-65ba776fbd9e29f771c07d4e)\n\n[#### Reasoning Collection 151 items • Updated Apr 6, 2024 • 29](https://huggingface.co/collections/stereoplegic/reasoning-6538a52e044e47f56050644e)\n\n[#### RL/Alignment Collection 197 items • Updated Jun 18, 2024 • 23](https://huggingface.co/collections/stereoplegic/rl-alignment-65389cd60e9beb3a415b3c76)\n\n[#### Agent Collection 112 items • Updated Sep 9, 2024 • 21](https://huggingface.co/collections/stereoplegic/agent-65389e7dcfc110ff79843a71)\n\n[Browse 21 collections that include this paper](https://huggingface.co/collections?paper=2310.03714)\n\nSystem theme\n\nCompany\n\n[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)\n\nWebsite\n\n[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)",
  "usage": {
    "tokens": 3438
  }
}
```
