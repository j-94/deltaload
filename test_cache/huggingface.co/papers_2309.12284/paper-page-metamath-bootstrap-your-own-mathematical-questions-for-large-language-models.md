---
title: Paper page - MetaMath: Bootstrap Your Own Mathematical Questions for Large Language
  Models
description: Join the discussion on this paper page
url: https://huggingface.co/papers/2309.12284
timestamp: 2025-01-20T15:44:55.513Z
domain: huggingface.co
path: papers_2309.12284
---

# Paper page - MetaMath: Bootstrap Your Own Mathematical Questions for Large Language
  Models


Join the discussion on this paper page


## Content

Paper page - MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models
===============

 [![Image 44: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)

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

arxiv:2309.12284

MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models
=============================================================================

Published on Sep 21, 2023

· Submitted by [![Image 45](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Sep 22, 2023

 [Upvote 19](https://huggingface.co/login?next=%2Fpapers%2F2309.12284)

*   [![Image 46](https://huggingface.co/avatars/1002835739dbb90214b5f2824a7c8c1f.svg)](https://huggingface.co/yujincheng08 "yujincheng08")
*   [![Image 47](https://cdn-avatars.huggingface.co/v1/production/uploads/648905d1a15c43c791d4381f/GpqGBzsLiMHX0gWZEz3qn.jpeg)](https://huggingface.co/wy1iu "wy1iu")
*   [![Image 48](https://cdn-avatars.huggingface.co/v1/production/uploads/64a9fab8bab1855ff03279a9/PZx01h6huANhltHv1Sqcn.png)](https://huggingface.co/Tanvir1337 "Tanvir1337")
*   [![Image 49](https://huggingface.co/avatars/6ad04ec2a41a54a5a2d37177b4cb2817.svg)](https://huggingface.co/ML56L "ML56L")
*   [![Image 50](https://cdn-avatars.huggingface.co/v1/production/uploads/6538119803519fddb4a17e10/ffJMkdx-rM7VvLTCM6ri_.jpeg)](https://huggingface.co/samusenps "samusenps")
*   [![Image 51](https://huggingface.co/avatars/6a4124ed2957a93a294bd5563f500e1c.svg)](https://huggingface.co/waysonkong "waysonkong")
*   [![Image 52](https://cdn-avatars.huggingface.co/v1/production/uploads/637b9fba787dab5e6b349fbe/XyomA6tgZSdAv1tSHbzFN.jpeg)](https://huggingface.co/marik0 "marik0")
*   [![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/1675778487155-63d4c8ce13ae45b780792f32.jpeg)](https://huggingface.co/PeepDaSlan9 "PeepDaSlan9")
*   +11

Authors:

 ![Image 54](https://cdn-avatars.huggingface.co/v1/production/uploads/64b753306c169983c982f609/oOC_N8cI1Go6avUMvIPVI.jpeg) [Longhui Yu](https://huggingface.co/Longhui98) ,

 ![Image 55](https://huggingface.co/avatars/6a4124ed2957a93a294bd5563f500e1c.svg) [Weisen Jiang](https://huggingface.co/waysonkong) ,

 ![Image 56](https://huggingface.co/avatars/9823f115040a3d6b0240038010e46cb6.svg) [Han Shi](https://huggingface.co/shihan96) ,

 ![Image 57](https://huggingface.co/avatars/1002835739dbb90214b5f2824a7c8c1f.svg) [Jincheng Yu](https://huggingface.co/yujincheng08) ,

 ![Image 58](https://cdn-avatars.huggingface.co/v1/production/uploads/6445f82f5691ca69b0df747a/lVILbKYiX6Aw9I97HlPo1.jpeg) [Zhengying Liu](https://huggingface.co/evariste-liu) ,

Yu Zhang ,

 ![Image 59](https://huggingface.co/avatars/01f7df1ad30d70c99ef1c3521bbeac94.svg) [James T. Kwok](https://huggingface.co/KazumaMyGuy) ,

 ![Image 60](https://huggingface.co/avatars/c5cbb87cd51cc1341844f67d42c55151.svg) [Zhenguo Li](https://huggingface.co/lizhenguo) ,

Adrian Weller ,

 ![Image 61](https://cdn-avatars.huggingface.co/v1/production/uploads/648905d1a15c43c791d4381f/GpqGBzsLiMHX0gWZEz3qn.jpeg) [Weiyang Liu](https://huggingface.co/wy1iu)

Abstract
--------

Large language models (LLMs) have pushed the limits of natural language understanding and exhibited excellent problem-solving ability. Despite the great success, most existing open-source LLMs (\\eg, LLaMA-2) are still far away from satisfactory for solving mathematical problem due to the complex reasoning procedures. To bridge this gap, we propose MetaMath, a fine-tuned language model that specializes in mathematical reasoning. Specifically, we start by bootstrapping mathematical questions by rewriting the question from multiple perspectives without extra knowledge, which results in a new dataset called {MetaMathQA}. Then we fine-tune the LLaMA-2 models on MetaMathQA. Experimental results on two popular benchmarks (\\ie, GSM8K and MATH) for mathematical reasoning demonstrate that MetaMath outperforms a suite of open-source LLMs by a significant margin. Our MetaMath-7B model achieves 66.4% on GSM8K and 19.4% on MATH, exceeding the state-of-the-art models of the same size by 11.5% and 8.7%. Particularly, {MetaMath-70B} achieves an accuracy of 82.3% on {GSM8K}, slightly better than {GPT-3.5-Turbo}. We release the {MetaMathQA} dataset, the {MetaMath} models with different model sizes and the training code for public use.

[View arXiv page](https://arxiv.org/abs/2309.12284) [View PDF](https://arxiv.org/pdf/2309.12284) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2309.12284)

### Community

 ![Image 62](https://cdn-avatars.huggingface.co/v1/production/uploads/1674830754237-63d3e0e8ff1384ce6c5dd17d.jpeg) [librarian-bot](https://huggingface.co/librarian-bot)[Oct 4, 2023](https://huggingface.co/papers/2309.12284#651d4a89adf66280145f46f9)

This is an automated message from the [Librarian Bot](https://huggingface.co/librarian-bots). I found the following papers similar to this paper.

The following papers were recommended by the Semantic Scholar API

*   [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://huggingface.co/papers/2308.09583) (2023)
*   [Forward-Backward Reasoning in Large Language Models for Mathematical Verification](https://huggingface.co/papers/2308.07758) (2023)
*   [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://huggingface.co/papers/2309.05653) (2023)
*   [Sci-CoT: Leveraging Large Language Models for Enhanced Knowledge Distillation in Small Models for Scientific QA](https://huggingface.co/papers/2308.04679) (2023)
*   [Enhancing Reasoning Capabilities of Large Language Models: A Graph-Based Verification Approach](https://huggingface.co/papers/2308.09267) (2023)

Please give a thumbs up to this comment if you found it helpful!

If you want recommendations for any Paper on Hugging Face checkout [this](https://huggingface.co/spaces/librarian-bots/recommend_similar_papers) Space

👍

8

8

+

Reply

 ![Image 63](https://huggingface.co/avatars/9c864114f616cf6ee9d76aee633b01c4.svg) [bayang](https://huggingface.co/bayang)[Dec 6, 2023](https://huggingface.co/papers/2309.12284#65703590ec92f5a1a73e56e8)

[@librarian-bot](https://huggingface.co/librarian-bot) could you recommend me a paper regarding query expansion not using transformer based model?

+

Reply

 ![Image 64](https://cdn-avatars.huggingface.co/v1/production/uploads/1627505688463-60107b385ac3e86b3ea4fc34.jpeg) [davanstrien](https://huggingface.co/davanstrien)[Dec 6, 2023](https://huggingface.co/papers/2309.12284#65709a750ea91e592a00c91b)

[@bayang](https://huggingface.co/bayang) , at the moment, the librarian-bot isn't that clever! If you already have a paper on that topic you can use this [space](https://huggingface.co/spaces/librarian-bots/recommend_similar_papers) to find similar papers

🤗

1

1

+

Reply

 ![Image 65](https://huggingface.co/avatars/9c864114f616cf6ee9d76aee633b01c4.svg) [bayang](https://huggingface.co/bayang)[Dec 6, 2023](https://huggingface.co/papers/2309.12284#65709e2db3501cbcb8f5e793)

•

[edited Dec 6, 2023](https://huggingface.co/papers/2309.12284#65709e2db3501cbcb8f5e793 "Edited  by bayang")

[@davanstrien](https://huggingface.co/davanstrien) , thank you, got it!

See translation

+

Reply

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

Comment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2309.12284) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2309.12284) to comment

 [Upvote 19](https://huggingface.co/login?next=%2Fpapers%2F2309.12284)

*   [![Image 66](https://huggingface.co/avatars/1002835739dbb90214b5f2824a7c8c1f.svg)](https://huggingface.co/yujincheng08 "yujincheng08")
*   [![Image 67](https://cdn-avatars.huggingface.co/v1/production/uploads/648905d1a15c43c791d4381f/GpqGBzsLiMHX0gWZEz3qn.jpeg)](https://huggingface.co/wy1iu "wy1iu")
*   [![Image 68](https://cdn-avatars.huggingface.co/v1/production/uploads/64a9fab8bab1855ff03279a9/PZx01h6huANhltHv1Sqcn.png)](https://huggingface.co/Tanvir1337 "Tanvir1337")
*   [![Image 69](https://huggingface.co/avatars/6ad04ec2a41a54a5a2d37177b4cb2817.svg)](https://huggingface.co/ML56L "ML56L")
*   [![Image 70](https://cdn-avatars.huggingface.co/v1/production/uploads/6538119803519fddb4a17e10/ffJMkdx-rM7VvLTCM6ri_.jpeg)](https://huggingface.co/samusenps "samusenps")
*   [![Image 71](https://huggingface.co/avatars/6a4124ed2957a93a294bd5563f500e1c.svg)](https://huggingface.co/waysonkong "waysonkong")
*   [![Image 72](https://cdn-avatars.huggingface.co/v1/production/uploads/637b9fba787dab5e6b349fbe/XyomA6tgZSdAv1tSHbzFN.jpeg)](https://huggingface.co/marik0 "marik0")
*   [![Image 73](https://cdn-avatars.huggingface.co/v1/production/uploads/1675778487155-63d4c8ce13ae45b780792f32.jpeg)](https://huggingface.co/PeepDaSlan9 "PeepDaSlan9")
*   [![Image 74](https://cdn-avatars.huggingface.co/v1/production/uploads/64b753306c169983c982f609/oOC_N8cI1Go6avUMvIPVI.jpeg)](https://huggingface.co/Longhui98 "Longhui98")
*   [![Image 75](https://huggingface.co/avatars/5b808273437a1bb7d44895fc0d0f00d2.svg)](https://huggingface.co/AB057 "AB057")
*   [![Image 76](https://huggingface.co/avatars/2deb4f9e605d0dc30a31538d5c9aa300.svg)](https://huggingface.co/shyamperi "shyamperi")
*   [![Image 77](https://cdn-avatars.huggingface.co/v1/production/uploads/64aea8ff67511bd3d965697b/Jxn52EmDF5RApJh8antxn.jpeg)](https://huggingface.co/ajibawa-2023 "ajibawa-2023")
*   +7

Models citing this paper 42
---------------------------

[![Image 78](https://cdn-avatars.huggingface.co/v1/production/uploads/643feeb67bc3fbde1385cc25/7vmYr2XwVcPtkLzac_jxQ.png) #### stabilityai/stable-code-3b Text Generation • Updated Jul 10, 2024 • 5.15k • 639](https://huggingface.co/stabilityai/stable-code-3b)

[![Image 79](https://cdn-avatars.huggingface.co/v1/production/uploads/650c74e5d439bbbbadfcfbbe/VNgte8jR2UiKObw4WTz9w.png) #### meta-math/MetaMath-Mistral-7B Text Generation • Updated Dec 21, 2023 • 2.73k • 95](https://huggingface.co/meta-math/MetaMath-Mistral-7B)

[![Image 80](https://cdn-avatars.huggingface.co/v1/production/uploads/1616186257611-60104afcc75e19ac1738fe70.png) #### Intel/neural-chat-7b-v3-3 Text Generation • Updated Nov 11, 2024 • 142k • 77](https://huggingface.co/Intel/neural-chat-7b-v3-3)

[![Image 81](https://cdn-avatars.huggingface.co/v1/production/uploads/64c75c1237333ccfef30a602/oEmowh93V8ZRm54OWssrZ.jpeg) #### akjindal53244/Arithmo-Mistral-7B Text Generation • Updated Jan 27, 2024 • 842 • 61](https://huggingface.co/akjindal53244/Arithmo-Mistral-7B)

[Browse 42 models citing this paper](https://huggingface.co/models?other=arxiv:2309.12284)

Datasets citing this paper 17
-----------------------------

[#### meta-math/MetaMathQA Viewer • Updated Dec 21, 2023 • 395k • 5.96k • 348](https://huggingface.co/datasets/meta-math/MetaMathQA)

[#### meta-math/MetaMathQA-40K Viewer • Updated Nov 10, 2023 • 40k • 249 • 23](https://huggingface.co/datasets/meta-math/MetaMathQA-40K)

[#### hkust-nlp/dart-math-pool-math Viewer • Updated Jul 19, 2024 • 1.62M • 79 • 5](https://huggingface.co/datasets/hkust-nlp/dart-math-pool-math)

[#### hkust-nlp/dart-math-hard Viewer • Updated Aug 2, 2024 • 585k • 78 • 12](https://huggingface.co/datasets/hkust-nlp/dart-math-hard)

[Browse 17 datasets citing this paper](https://huggingface.co/datasets?other=arxiv:2309.12284)

### Spaces citing this paper 45

[🦊 kevinpro/Open-Multilingual-Reasoning-Leaderboard](https://huggingface.co/spaces/kevinpro/Open-Multilingual-Reasoning-Leaderboard)[📈 bigcode/bigcode-models-leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)[💻 featherless-ai/try-this-model](https://huggingface.co/spaces/featherless-ai/try-this-model)[🏆 eduagarcia/open\_pt\_llm\_leaderboard](https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard)[🐠 ZhangYuhan/3DGen-Arena](https://huggingface.co/spaces/ZhangYuhan/3DGen-Arena)[📚 Darok/Featherless-Feud](https://huggingface.co/spaces/Darok/Featherless-Feud)[👀 lightmate/llm-chatbot](https://huggingface.co/spaces/lightmate/llm-chatbot)[🔥 alKoGolik/codellama-CodeLlama-7b-hf](https://huggingface.co/spaces/alKoGolik/codellama-CodeLlama-7b-hf)[💻 emekaboris/try-this-model](https://huggingface.co/spaces/emekaboris/try-this-model)[💻 SC999/NV\_Nemotron](https://huggingface.co/spaces/SC999/NV_Nemotron)[👀 alexanlee/meta-math-MetaMath-7B-V1.0](https://huggingface.co/spaces/alexanlee/meta-math-MetaMath-7B-V1.0)[📉 ali-vilab/IDEA-Bench-Arena](https://huggingface.co/spaces/ali-vilab/IDEA-Bench-Arena)\+ 40 Spaces \+ 33 Spaces

Collections including this paper 29
-----------------------------------

[#### Reasoning Collection 151 items • Updated Apr 6, 2024 • 29](https://huggingface.co/collections/stereoplegic/reasoning-6538a52e044e47f56050644e)

[#### Dataset generation Collection 126 items • Updated Jul 22, 2024 • 26](https://huggingface.co/collections/stereoplegic/dataset-generation-65389dd75510eb595f8a3797)

[#### LLMs Collection 127 items • Updated Aug 1, 2024 • 12](https://huggingface.co/collections/taufiqdp/llms-658d4b6c8ea59eaa35665e60)

[#### Math Collection 46 items • Updated May 31, 2024 • 11](https://huggingface.co/collections/stereoplegic/math-653933d9ee5888edef7241f7)

[Browse 29 collections that include this paper](https://huggingface.co/collections?paper=2309.12284)

System theme

Company

[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)

Website

[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

## Metadata

```json
{
  "title": "Paper page - MetaMath: Bootstrap Your Own Mathematical Questions for Large Language\n  Models",
  "description": "Join the discussion on this paper page",
  "url": "https://huggingface.co/papers/2309.12284",
  "content": "Paper page - MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models\n===============\n\n [![Image 44: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)\n\n*   [Models](https://huggingface.co/models)\n*   [Datasets](https://huggingface.co/datasets)\n*   [Spaces](https://huggingface.co/spaces)\n*   [Posts](https://huggingface.co/posts)\n*   [Docs](https://huggingface.co/docs)\n*   [Enterprise](https://huggingface.co/enterprise)\n*   [Pricing](https://huggingface.co/pricing)\n\n*   * * *\n    \n*   [Log In](https://huggingface.co/login)\n*   [Sign Up](https://huggingface.co/join)\n\n[Papers](https://huggingface.co/papers)\n\narxiv:2309.12284\n\nMetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models\n=============================================================================\n\nPublished on Sep 21, 2023\n\n· Submitted by [![Image 45](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Sep 22, 2023\n\n [Upvote 19](https://huggingface.co/login?next=%2Fpapers%2F2309.12284)\n\n*   [![Image 46](https://huggingface.co/avatars/1002835739dbb90214b5f2824a7c8c1f.svg)](https://huggingface.co/yujincheng08 \"yujincheng08\")\n*   [![Image 47](https://cdn-avatars.huggingface.co/v1/production/uploads/648905d1a15c43c791d4381f/GpqGBzsLiMHX0gWZEz3qn.jpeg)](https://huggingface.co/wy1iu \"wy1iu\")\n*   [![Image 48](https://cdn-avatars.huggingface.co/v1/production/uploads/64a9fab8bab1855ff03279a9/PZx01h6huANhltHv1Sqcn.png)](https://huggingface.co/Tanvir1337 \"Tanvir1337\")\n*   [![Image 49](https://huggingface.co/avatars/6ad04ec2a41a54a5a2d37177b4cb2817.svg)](https://huggingface.co/ML56L \"ML56L\")\n*   [![Image 50](https://cdn-avatars.huggingface.co/v1/production/uploads/6538119803519fddb4a17e10/ffJMkdx-rM7VvLTCM6ri_.jpeg)](https://huggingface.co/samusenps \"samusenps\")\n*   [![Image 51](https://huggingface.co/avatars/6a4124ed2957a93a294bd5563f500e1c.svg)](https://huggingface.co/waysonkong \"waysonkong\")\n*   [![Image 52](https://cdn-avatars.huggingface.co/v1/production/uploads/637b9fba787dab5e6b349fbe/XyomA6tgZSdAv1tSHbzFN.jpeg)](https://huggingface.co/marik0 \"marik0\")\n*   [![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/1675778487155-63d4c8ce13ae45b780792f32.jpeg)](https://huggingface.co/PeepDaSlan9 \"PeepDaSlan9\")\n*   +11\n\nAuthors:\n\n ![Image 54](https://cdn-avatars.huggingface.co/v1/production/uploads/64b753306c169983c982f609/oOC_N8cI1Go6avUMvIPVI.jpeg) [Longhui Yu](https://huggingface.co/Longhui98) ,\n\n ![Image 55](https://huggingface.co/avatars/6a4124ed2957a93a294bd5563f500e1c.svg) [Weisen Jiang](https://huggingface.co/waysonkong) ,\n\n ![Image 56](https://huggingface.co/avatars/9823f115040a3d6b0240038010e46cb6.svg) [Han Shi](https://huggingface.co/shihan96) ,\n\n ![Image 57](https://huggingface.co/avatars/1002835739dbb90214b5f2824a7c8c1f.svg) [Jincheng Yu](https://huggingface.co/yujincheng08) ,\n\n ![Image 58](https://cdn-avatars.huggingface.co/v1/production/uploads/6445f82f5691ca69b0df747a/lVILbKYiX6Aw9I97HlPo1.jpeg) [Zhengying Liu](https://huggingface.co/evariste-liu) ,\n\nYu Zhang ,\n\n ![Image 59](https://huggingface.co/avatars/01f7df1ad30d70c99ef1c3521bbeac94.svg) [James T. Kwok](https://huggingface.co/KazumaMyGuy) ,\n\n ![Image 60](https://huggingface.co/avatars/c5cbb87cd51cc1341844f67d42c55151.svg) [Zhenguo Li](https://huggingface.co/lizhenguo) ,\n\nAdrian Weller ,\n\n ![Image 61](https://cdn-avatars.huggingface.co/v1/production/uploads/648905d1a15c43c791d4381f/GpqGBzsLiMHX0gWZEz3qn.jpeg) [Weiyang Liu](https://huggingface.co/wy1iu)\n\nAbstract\n--------\n\nLarge language models (LLMs) have pushed the limits of natural language understanding and exhibited excellent problem-solving ability. Despite the great success, most existing open-source LLMs (\\\\eg, LLaMA-2) are still far away from satisfactory for solving mathematical problem due to the complex reasoning procedures. To bridge this gap, we propose MetaMath, a fine-tuned language model that specializes in mathematical reasoning. Specifically, we start by bootstrapping mathematical questions by rewriting the question from multiple perspectives without extra knowledge, which results in a new dataset called {MetaMathQA}. Then we fine-tune the LLaMA-2 models on MetaMathQA. Experimental results on two popular benchmarks (\\\\ie, GSM8K and MATH) for mathematical reasoning demonstrate that MetaMath outperforms a suite of open-source LLMs by a significant margin. Our MetaMath-7B model achieves 66.4% on GSM8K and 19.4% on MATH, exceeding the state-of-the-art models of the same size by 11.5% and 8.7%. Particularly, {MetaMath-70B} achieves an accuracy of 82.3% on {GSM8K}, slightly better than {GPT-3.5-Turbo}. We release the {MetaMathQA} dataset, the {MetaMath} models with different model sizes and the training code for public use.\n\n[View arXiv page](https://arxiv.org/abs/2309.12284) [View PDF](https://arxiv.org/pdf/2309.12284) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2309.12284)\n\n### Community\n\n ![Image 62](https://cdn-avatars.huggingface.co/v1/production/uploads/1674830754237-63d3e0e8ff1384ce6c5dd17d.jpeg) [librarian-bot](https://huggingface.co/librarian-bot)[Oct 4, 2023](https://huggingface.co/papers/2309.12284#651d4a89adf66280145f46f9)\n\nThis is an automated message from the [Librarian Bot](https://huggingface.co/librarian-bots). I found the following papers similar to this paper.\n\nThe following papers were recommended by the Semantic Scholar API\n\n*   [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://huggingface.co/papers/2308.09583) (2023)\n*   [Forward-Backward Reasoning in Large Language Models for Mathematical Verification](https://huggingface.co/papers/2308.07758) (2023)\n*   [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://huggingface.co/papers/2309.05653) (2023)\n*   [Sci-CoT: Leveraging Large Language Models for Enhanced Knowledge Distillation in Small Models for Scientific QA](https://huggingface.co/papers/2308.04679) (2023)\n*   [Enhancing Reasoning Capabilities of Large Language Models: A Graph-Based Verification Approach](https://huggingface.co/papers/2308.09267) (2023)\n\nPlease give a thumbs up to this comment if you found it helpful!\n\nIf you want recommendations for any Paper on Hugging Face checkout [this](https://huggingface.co/spaces/librarian-bots/recommend_similar_papers) Space\n\n👍\n\n8\n\n8\n\n+\n\nReply\n\n ![Image 63](https://huggingface.co/avatars/9c864114f616cf6ee9d76aee633b01c4.svg) [bayang](https://huggingface.co/bayang)[Dec 6, 2023](https://huggingface.co/papers/2309.12284#65703590ec92f5a1a73e56e8)\n\n[@librarian-bot](https://huggingface.co/librarian-bot) could you recommend me a paper regarding query expansion not using transformer based model?\n\n+\n\nReply\n\n ![Image 64](https://cdn-avatars.huggingface.co/v1/production/uploads/1627505688463-60107b385ac3e86b3ea4fc34.jpeg) [davanstrien](https://huggingface.co/davanstrien)[Dec 6, 2023](https://huggingface.co/papers/2309.12284#65709a750ea91e592a00c91b)\n\n[@bayang](https://huggingface.co/bayang) , at the moment, the librarian-bot isn't that clever! If you already have a paper on that topic you can use this [space](https://huggingface.co/spaces/librarian-bots/recommend_similar_papers) to find similar papers\n\n🤗\n\n1\n\n1\n\n+\n\nReply\n\n ![Image 65](https://huggingface.co/avatars/9c864114f616cf6ee9d76aee633b01c4.svg) [bayang](https://huggingface.co/bayang)[Dec 6, 2023](https://huggingface.co/papers/2309.12284#65709e2db3501cbcb8f5e793)\n\n•\n\n[edited Dec 6, 2023](https://huggingface.co/papers/2309.12284#65709e2db3501cbcb8f5e793 \"Edited  by bayang\")\n\n[@davanstrien](https://huggingface.co/davanstrien) , thank you, got it!\n\nSee translation\n\n+\n\nReply\n\nEditPreview\n\nUpload images, audio, and videos by dragging in the text input, pasting, or clicking here.\n\nTap or paste here to upload images\n\nComment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2309.12284) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2309.12284) to comment\n\n [Upvote 19](https://huggingface.co/login?next=%2Fpapers%2F2309.12284)\n\n*   [![Image 66](https://huggingface.co/avatars/1002835739dbb90214b5f2824a7c8c1f.svg)](https://huggingface.co/yujincheng08 \"yujincheng08\")\n*   [![Image 67](https://cdn-avatars.huggingface.co/v1/production/uploads/648905d1a15c43c791d4381f/GpqGBzsLiMHX0gWZEz3qn.jpeg)](https://huggingface.co/wy1iu \"wy1iu\")\n*   [![Image 68](https://cdn-avatars.huggingface.co/v1/production/uploads/64a9fab8bab1855ff03279a9/PZx01h6huANhltHv1Sqcn.png)](https://huggingface.co/Tanvir1337 \"Tanvir1337\")\n*   [![Image 69](https://huggingface.co/avatars/6ad04ec2a41a54a5a2d37177b4cb2817.svg)](https://huggingface.co/ML56L \"ML56L\")\n*   [![Image 70](https://cdn-avatars.huggingface.co/v1/production/uploads/6538119803519fddb4a17e10/ffJMkdx-rM7VvLTCM6ri_.jpeg)](https://huggingface.co/samusenps \"samusenps\")\n*   [![Image 71](https://huggingface.co/avatars/6a4124ed2957a93a294bd5563f500e1c.svg)](https://huggingface.co/waysonkong \"waysonkong\")\n*   [![Image 72](https://cdn-avatars.huggingface.co/v1/production/uploads/637b9fba787dab5e6b349fbe/XyomA6tgZSdAv1tSHbzFN.jpeg)](https://huggingface.co/marik0 \"marik0\")\n*   [![Image 73](https://cdn-avatars.huggingface.co/v1/production/uploads/1675778487155-63d4c8ce13ae45b780792f32.jpeg)](https://huggingface.co/PeepDaSlan9 \"PeepDaSlan9\")\n*   [![Image 74](https://cdn-avatars.huggingface.co/v1/production/uploads/64b753306c169983c982f609/oOC_N8cI1Go6avUMvIPVI.jpeg)](https://huggingface.co/Longhui98 \"Longhui98\")\n*   [![Image 75](https://huggingface.co/avatars/5b808273437a1bb7d44895fc0d0f00d2.svg)](https://huggingface.co/AB057 \"AB057\")\n*   [![Image 76](https://huggingface.co/avatars/2deb4f9e605d0dc30a31538d5c9aa300.svg)](https://huggingface.co/shyamperi \"shyamperi\")\n*   [![Image 77](https://cdn-avatars.huggingface.co/v1/production/uploads/64aea8ff67511bd3d965697b/Jxn52EmDF5RApJh8antxn.jpeg)](https://huggingface.co/ajibawa-2023 \"ajibawa-2023\")\n*   +7\n\nModels citing this paper 42\n---------------------------\n\n[![Image 78](https://cdn-avatars.huggingface.co/v1/production/uploads/643feeb67bc3fbde1385cc25/7vmYr2XwVcPtkLzac_jxQ.png) #### stabilityai/stable-code-3b Text Generation • Updated Jul 10, 2024 • 5.15k • 639](https://huggingface.co/stabilityai/stable-code-3b)\n\n[![Image 79](https://cdn-avatars.huggingface.co/v1/production/uploads/650c74e5d439bbbbadfcfbbe/VNgte8jR2UiKObw4WTz9w.png) #### meta-math/MetaMath-Mistral-7B Text Generation • Updated Dec 21, 2023 • 2.73k • 95](https://huggingface.co/meta-math/MetaMath-Mistral-7B)\n\n[![Image 80](https://cdn-avatars.huggingface.co/v1/production/uploads/1616186257611-60104afcc75e19ac1738fe70.png) #### Intel/neural-chat-7b-v3-3 Text Generation • Updated Nov 11, 2024 • 142k • 77](https://huggingface.co/Intel/neural-chat-7b-v3-3)\n\n[![Image 81](https://cdn-avatars.huggingface.co/v1/production/uploads/64c75c1237333ccfef30a602/oEmowh93V8ZRm54OWssrZ.jpeg) #### akjindal53244/Arithmo-Mistral-7B Text Generation • Updated Jan 27, 2024 • 842 • 61](https://huggingface.co/akjindal53244/Arithmo-Mistral-7B)\n\n[Browse 42 models citing this paper](https://huggingface.co/models?other=arxiv:2309.12284)\n\nDatasets citing this paper 17\n-----------------------------\n\n[#### meta-math/MetaMathQA Viewer • Updated Dec 21, 2023 • 395k • 5.96k • 348](https://huggingface.co/datasets/meta-math/MetaMathQA)\n\n[#### meta-math/MetaMathQA-40K Viewer • Updated Nov 10, 2023 • 40k • 249 • 23](https://huggingface.co/datasets/meta-math/MetaMathQA-40K)\n\n[#### hkust-nlp/dart-math-pool-math Viewer • Updated Jul 19, 2024 • 1.62M • 79 • 5](https://huggingface.co/datasets/hkust-nlp/dart-math-pool-math)\n\n[#### hkust-nlp/dart-math-hard Viewer • Updated Aug 2, 2024 • 585k • 78 • 12](https://huggingface.co/datasets/hkust-nlp/dart-math-hard)\n\n[Browse 17 datasets citing this paper](https://huggingface.co/datasets?other=arxiv:2309.12284)\n\n### Spaces citing this paper 45\n\n[🦊 kevinpro/Open-Multilingual-Reasoning-Leaderboard](https://huggingface.co/spaces/kevinpro/Open-Multilingual-Reasoning-Leaderboard)[📈 bigcode/bigcode-models-leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)[💻 featherless-ai/try-this-model](https://huggingface.co/spaces/featherless-ai/try-this-model)[🏆 eduagarcia/open\\_pt\\_llm\\_leaderboard](https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard)[🐠 ZhangYuhan/3DGen-Arena](https://huggingface.co/spaces/ZhangYuhan/3DGen-Arena)[📚 Darok/Featherless-Feud](https://huggingface.co/spaces/Darok/Featherless-Feud)[👀 lightmate/llm-chatbot](https://huggingface.co/spaces/lightmate/llm-chatbot)[🔥 alKoGolik/codellama-CodeLlama-7b-hf](https://huggingface.co/spaces/alKoGolik/codellama-CodeLlama-7b-hf)[💻 emekaboris/try-this-model](https://huggingface.co/spaces/emekaboris/try-this-model)[💻 SC999/NV\\_Nemotron](https://huggingface.co/spaces/SC999/NV_Nemotron)[👀 alexanlee/meta-math-MetaMath-7B-V1.0](https://huggingface.co/spaces/alexanlee/meta-math-MetaMath-7B-V1.0)[📉 ali-vilab/IDEA-Bench-Arena](https://huggingface.co/spaces/ali-vilab/IDEA-Bench-Arena)\\+ 40 Spaces \\+ 33 Spaces\n\nCollections including this paper 29\n-----------------------------------\n\n[#### Reasoning Collection 151 items • Updated Apr 6, 2024 • 29](https://huggingface.co/collections/stereoplegic/reasoning-6538a52e044e47f56050644e)\n\n[#### Dataset generation Collection 126 items • Updated Jul 22, 2024 • 26](https://huggingface.co/collections/stereoplegic/dataset-generation-65389dd75510eb595f8a3797)\n\n[#### LLMs Collection 127 items • Updated Aug 1, 2024 • 12](https://huggingface.co/collections/taufiqdp/llms-658d4b6c8ea59eaa35665e60)\n\n[#### Math Collection 46 items • Updated May 31, 2024 • 11](https://huggingface.co/collections/stereoplegic/math-653933d9ee5888edef7241f7)\n\n[Browse 29 collections that include this paper](https://huggingface.co/collections?paper=2309.12284)\n\nSystem theme\n\nCompany\n\n[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)\n\nWebsite\n\n[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)",
  "usage": {
    "tokens": 4939
  }
}
```
