---
title: Paper page - Connecting Large Language Models with Evolutionary Algorithms Yields
  Powerful Prompt Optimizers
description: Join the discussion on this paper page
url: https://huggingface.co/papers/2309.08532
timestamp: 2025-01-20T15:44:18.827Z
domain: huggingface.co
path: papers_2309.08532
---

# Paper page - Connecting Large Language Models with Evolutionary Algorithms Yields
  Powerful Prompt Optimizers


Join the discussion on this paper page


## Content

Paper page - Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers
===============

 [![Image 42: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)

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

arxiv:2309.08532

Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers
===============================================================================================

Published on Sep 15, 2023

· Submitted by [![Image 43](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Sep 18, 2023

 [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2309.08532)

*   [![Image 44](https://huggingface.co/avatars/e84732671896eabb90cbe6ed1711cd8d.svg)](https://huggingface.co/apollostream "apollostream")
*   [![Image 45](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/YtJFOuny0YZlv_xTup7WV.jpeg)](https://huggingface.co/Zer0H1ro "Zer0H1ro")
*   [![Image 46](https://huggingface.co/avatars/081751621bd13e83f5f712eaf5352c77.svg)](https://huggingface.co/TimLuo "TimLuo")
*   [![Image 47](https://huggingface.co/avatars/83efc5b49a5f6d20ced04e7f2d9eac9b.svg)](https://huggingface.co/shenkha "shenkha")
*   [![Image 48](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/HQiX0aBwCVONpd1b4gMda.png)](https://huggingface.co/zygoma919 "zygoma919")
*   [![Image 49](https://huggingface.co/avatars/5346146aca9add2e6c02b01bf4c0df2e.svg)](https://huggingface.co/horyujey "horyujey")
*   [![Image 50](https://huggingface.co/avatars/32a34625ebd6542be80c241c4e1c51d1.svg)](https://huggingface.co/michael-kingston "michael-kingston")
*   [![Image 51](https://huggingface.co/avatars/c61c00c314cf202b64968e51e855694d.svg)](https://huggingface.co/jianhongbai "jianhongbai")
*   +45

Authors:

 ![Image 52](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [Qingyan Guo](https://huggingface.co/qingyan) ,

Rui Wang ,

Junliang Guo ,

 ![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/1661394612620-noauth.jpeg) [Bei Li](https://huggingface.co/libeineu) ,

 ![Image 54](https://huggingface.co/avatars/90beea6b452c662d579197dbf592423a.svg) [Kaitao Song](https://huggingface.co/KaitaoSong) ,

 ![Image 55](https://huggingface.co/avatars/a2f28940236ae625ed3810ad62e343ff.svg) [Xu Tan](https://huggingface.co/xutan) ,

 ![Image 56](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/U6kC2rPOqDWGPcPTovmkE.png) [Guoqing Liu](https://huggingface.co/liuguoqing) ,

 ![Image 57](https://huggingface.co/avatars/303f4c7ee588f638acf78a7966786e1e.svg) [Jiang Bian](https://huggingface.co/bianjiang) ,

 ![Image 58](https://huggingface.co/avatars/44a3ad9e59318784ac531993b5f69f6b.svg) [Yujiu Yang](https://huggingface.co/Thu-redrobot)

Abstract
--------

Large Language Models (LLMs) excel in various tasks, but they rely on carefully crafted prompts that often demand substantial human effort. To automate this process, in this paper, we propose a novel framework for discrete prompt optimization, called EvoPrompt, which borrows the idea of evolutionary algorithms (EAs) as they exhibit good performance and fast convergence. To enable EAs to work on discrete prompts, which are natural language expressions that need to be coherent and human-readable, we connect LLMs with EAs. This approach allows us to simultaneously leverage the powerful language processing capabilities of LLMs and the efficient optimization performance of EAs. Specifically, abstaining from any gradients or parameters, EvoPrompt starts from a population of prompts and iteratively generates new prompts with LLMs based on the evolutionary operators, improving the population based on the development set. We optimize prompts for both closed- and open-source LLMs including GPT-3.5 and Alpaca, on 9 datasets spanning language understanding and generation tasks. EvoPrompt significantly outperforms human-engineered prompts and existing methods for automatic prompt generation by up to 25% and 14% respectively. Furthermore, EvoPrompt demonstrates that connecting LLMs with EAs creates synergies, which could inspire further research on the combination of LLMs and conventional algorithms.

[View arXiv page](https://arxiv.org/abs/2309.08532) [View PDF](https://arxiv.org/pdf/2309.08532) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2309.08532)

### Community

 ![Image 59](https://huggingface.co/avatars/894469eccc3e21ac32b2ce32516f6238.svg) [zyxwvu](https://huggingface.co/zyxwvu)[Sep 18, 2023](https://huggingface.co/papers/2309.08532#6508b54b7ee07e274b19c1b8)

This comment has been hidden

+

 ![Image 60](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/wJv5M54SrkGtkmmh0qPtv.jpeg) [Antkiv](https://huggingface.co/Antkiv)[Sep 20, 2023](https://huggingface.co/papers/2309.08532#650ad3f6008f8c12614775cd)

Friends, how can I test this technology?

+

Reply

 ![Image 61](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Sep 22, 2023](https://huggingface.co/papers/2309.08532#650d07fb5b868581f9480e74)

> Friends, how can I test this technology?

We will release the code soon. Thanks for your attention quotes.

+

Reply

 ![Image 62](https://huggingface.co/avatars/6cb1af50262e24546c3d8291b1190bc9.svg) [BarbiOlyAI](https://huggingface.co/BarbiOlyAI)[Sep 26, 2023](https://huggingface.co/papers/2309.08532#6512b2df734af2ca4df2f836)

This comment has been hidden

+

 ![Image 63](https://huggingface.co/avatars/a9fddc9bc5f57f6bcd350ddc2ffad7ff.svg) [zhaokeke](https://huggingface.co/zhaokeke)[Oct 25, 2023](https://huggingface.co/papers/2309.08532#6538d110f84e87099ccb0b17)

> > Friends, how can I test this technology?
> 
> We will release the code soon. Thanks for your attention quotes.

Hello, is your code not yet released, or do you have an updated code release schedule?

+

Reply

 ![Image 64](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Oct 26, 2023](https://huggingface.co/papers/2309.08532#6539d5fa43d9189cdce561b6)

> > > Friends, how can I test this technology?
> > 
> > We will release the code soon. Thanks for your attention quotes.
> 
> Hello, is your code not yet released, or do you have an updated code release schedule?

Hi, we plan to release our code in 2 weeks.

+

Reply

 ![Image 65](https://huggingface.co/avatars/13cab56e5290640f21fa45c06553eacd.svg) [UmberH](https://huggingface.co/UmberH)[Dec 8, 2023](https://huggingface.co/papers/2309.08532#65728e5bb3d8dd7b921d5e9c)

is the code available now?

+

Reply

 ![Image 66](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Dec 10, 2023](https://huggingface.co/papers/2309.08532#657583fbb238c76bbaf478af)

> is the code available now?

The open-source of the code is on-going. We will share the link once it is available.

+

Reply

 ![Image 67](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d1815e3029d4d5b748bb)

•

[edited Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d1815e3029d4d5b748bb "Edited  by qingyan")

> is the code available now?

Sorry for the late release of our open-source code. You may refer to this repo temporarily ([https://github.com/beeevita/EvoPrompt](https://github.com/beeevita/EvoPrompt)) since the open-source of microsoft code is still in progress. If you find it helpful to your work, please star it. Thanks a lot~~😃😃

+

Reply

 ![Image 68](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d192ef14f9e6038a6852)

•

[edited Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d192ef14f9e6038a6852 "Edited  by qingyan")

> > > Friends, how can I test this technology?
> > 
> > We will release the code soon. Thanks for your attention quotes.
> 
> Hello, is your code not yet released, or do you have an updated code release schedule?

Sorry for the late release of our open-source code. You may refer to this repo temporarily ([https://github.com/beeevita/EvoPrompt](https://github.com/beeevita/EvoPrompt)) since the open-source of microsoft code is still in progress. If you find it helpful to your work, please star it. Thanks a lot~~😃😃

+

Reply

 ![Image 69](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d19f1012559732be6c6b)

•

[edited Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d19f1012559732be6c6b "Edited 2 times by qingyan")

> Friends, how can I test this technology?

Sorry for the late release of our open-source code. You may refer to this repo temporarily ([https://github.com/beeevita/EvoPrompt](https://github.com/beeevita/EvoPrompt)) since the open-source of microsoft code is still in progress. If you find it helpful to your work, please star it. Thanks a lot~~😃😃

+

Reply

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

Comment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2309.08532) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2309.08532) to comment

 [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2309.08532)

*   [![Image 70](https://huggingface.co/avatars/e84732671896eabb90cbe6ed1711cd8d.svg)](https://huggingface.co/apollostream "apollostream")
*   [![Image 71](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/YtJFOuny0YZlv_xTup7WV.jpeg)](https://huggingface.co/Zer0H1ro "Zer0H1ro")
*   [![Image 72](https://huggingface.co/avatars/081751621bd13e83f5f712eaf5352c77.svg)](https://huggingface.co/TimLuo "TimLuo")
*   [![Image 73](https://huggingface.co/avatars/83efc5b49a5f6d20ced04e7f2d9eac9b.svg)](https://huggingface.co/shenkha "shenkha")
*   [![Image 74](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/HQiX0aBwCVONpd1b4gMda.png)](https://huggingface.co/zygoma919 "zygoma919")
*   [![Image 75](https://huggingface.co/avatars/5346146aca9add2e6c02b01bf4c0df2e.svg)](https://huggingface.co/horyujey "horyujey")
*   [![Image 76](https://huggingface.co/avatars/32a34625ebd6542be80c241c4e1c51d1.svg)](https://huggingface.co/michael-kingston "michael-kingston")
*   [![Image 77](https://huggingface.co/avatars/c61c00c314cf202b64968e51e855694d.svg)](https://huggingface.co/jianhongbai "jianhongbai")
*   [![Image 78](https://huggingface.co/avatars/a9fddc9bc5f57f6bcd350ddc2ffad7ff.svg)](https://huggingface.co/zhaokeke "zhaokeke")
*   [![Image 79](https://cdn-avatars.huggingface.co/v1/production/uploads/6538119803519fddb4a17e10/ffJMkdx-rM7VvLTCM6ri_.jpeg)](https://huggingface.co/samusenps "samusenps")
*   [![Image 80](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri "taesiri")
*   [![Image 81](https://huggingface.co/avatars/2aad898b34a940a6aa4368526aa20d84.svg)](https://huggingface.co/hybris75 "hybris75")
*   +41

Models citing this paper 0
--------------------------

No model linking this paper

Cite arxiv.org/abs/2309.08532 in a model README.md to link it from this page.

Datasets citing this paper 0
----------------------------

No dataset linking this paper

Cite arxiv.org/abs/2309.08532 in a dataset README.md to link it from this page.

### Spaces citing this paper 0

No Space linking this paper

Cite arxiv.org/abs/2309.08532 in a Space README.md to link it from this page.

Collections including this paper 31
-----------------------------------

[#### Dataset generation Collection 126 items • Updated Jul 22, 2024 • 26](https://huggingface.co/collections/stereoplegic/dataset-generation-65389dd75510eb595f8a3797)

[#### NLP Paper Reading Collection NLP Papre Reading • 27 items • Updated Jan 31, 2024 • 9](https://huggingface.co/collections/Cartinoe5930/nlp-paper-reading-64fa9cc1bb362cbf2fd710b4)

[#### Prompt Collection 92 items • Updated Feb 11, 2024 • 7](https://huggingface.co/collections/stereoplegic/prompt-6538a5ca61d44e23f3e0656e)

[#### LLMs Collection 41 items • Updated Sep 25, 2023 • 5](https://huggingface.co/collections/krypticmouse/llms-650fa26b11f3210cf7b7ff51)

[Browse 31 collections that include this paper](https://huggingface.co/collections?paper=2309.08532)

System theme

Company

[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)

Website

[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

## Metadata

```json
{
  "title": "Paper page - Connecting Large Language Models with Evolutionary Algorithms Yields\n  Powerful Prompt Optimizers",
  "description": "Join the discussion on this paper page",
  "url": "https://huggingface.co/papers/2309.08532",
  "content": "Paper page - Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers\n===============\n\n [![Image 42: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)\n\n*   [Models](https://huggingface.co/models)\n*   [Datasets](https://huggingface.co/datasets)\n*   [Spaces](https://huggingface.co/spaces)\n*   [Posts](https://huggingface.co/posts)\n*   [Docs](https://huggingface.co/docs)\n*   [Enterprise](https://huggingface.co/enterprise)\n*   [Pricing](https://huggingface.co/pricing)\n\n*   * * *\n    \n*   [Log In](https://huggingface.co/login)\n*   [Sign Up](https://huggingface.co/join)\n\n[Papers](https://huggingface.co/papers)\n\narxiv:2309.08532\n\nConnecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers\n===============================================================================================\n\nPublished on Sep 15, 2023\n\n· Submitted by [![Image 43](https://cdn-avatars.huggingface.co/v1/production/uploads/1674929746905-60f1abe7544c2adfd699860c.jpeg) akhaliq](https://huggingface.co/akhaliq) on Sep 18, 2023\n\n [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2309.08532)\n\n*   [![Image 44](https://huggingface.co/avatars/e84732671896eabb90cbe6ed1711cd8d.svg)](https://huggingface.co/apollostream \"apollostream\")\n*   [![Image 45](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/YtJFOuny0YZlv_xTup7WV.jpeg)](https://huggingface.co/Zer0H1ro \"Zer0H1ro\")\n*   [![Image 46](https://huggingface.co/avatars/081751621bd13e83f5f712eaf5352c77.svg)](https://huggingface.co/TimLuo \"TimLuo\")\n*   [![Image 47](https://huggingface.co/avatars/83efc5b49a5f6d20ced04e7f2d9eac9b.svg)](https://huggingface.co/shenkha \"shenkha\")\n*   [![Image 48](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/HQiX0aBwCVONpd1b4gMda.png)](https://huggingface.co/zygoma919 \"zygoma919\")\n*   [![Image 49](https://huggingface.co/avatars/5346146aca9add2e6c02b01bf4c0df2e.svg)](https://huggingface.co/horyujey \"horyujey\")\n*   [![Image 50](https://huggingface.co/avatars/32a34625ebd6542be80c241c4e1c51d1.svg)](https://huggingface.co/michael-kingston \"michael-kingston\")\n*   [![Image 51](https://huggingface.co/avatars/c61c00c314cf202b64968e51e855694d.svg)](https://huggingface.co/jianhongbai \"jianhongbai\")\n*   +45\n\nAuthors:\n\n ![Image 52](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [Qingyan Guo](https://huggingface.co/qingyan) ,\n\nRui Wang ,\n\nJunliang Guo ,\n\n ![Image 53](https://cdn-avatars.huggingface.co/v1/production/uploads/1661394612620-noauth.jpeg) [Bei Li](https://huggingface.co/libeineu) ,\n\n ![Image 54](https://huggingface.co/avatars/90beea6b452c662d579197dbf592423a.svg) [Kaitao Song](https://huggingface.co/KaitaoSong) ,\n\n ![Image 55](https://huggingface.co/avatars/a2f28940236ae625ed3810ad62e343ff.svg) [Xu Tan](https://huggingface.co/xutan) ,\n\n ![Image 56](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/U6kC2rPOqDWGPcPTovmkE.png) [Guoqing Liu](https://huggingface.co/liuguoqing) ,\n\n ![Image 57](https://huggingface.co/avatars/303f4c7ee588f638acf78a7966786e1e.svg) [Jiang Bian](https://huggingface.co/bianjiang) ,\n\n ![Image 58](https://huggingface.co/avatars/44a3ad9e59318784ac531993b5f69f6b.svg) [Yujiu Yang](https://huggingface.co/Thu-redrobot)\n\nAbstract\n--------\n\nLarge Language Models (LLMs) excel in various tasks, but they rely on carefully crafted prompts that often demand substantial human effort. To automate this process, in this paper, we propose a novel framework for discrete prompt optimization, called EvoPrompt, which borrows the idea of evolutionary algorithms (EAs) as they exhibit good performance and fast convergence. To enable EAs to work on discrete prompts, which are natural language expressions that need to be coherent and human-readable, we connect LLMs with EAs. This approach allows us to simultaneously leverage the powerful language processing capabilities of LLMs and the efficient optimization performance of EAs. Specifically, abstaining from any gradients or parameters, EvoPrompt starts from a population of prompts and iteratively generates new prompts with LLMs based on the evolutionary operators, improving the population based on the development set. We optimize prompts for both closed- and open-source LLMs including GPT-3.5 and Alpaca, on 9 datasets spanning language understanding and generation tasks. EvoPrompt significantly outperforms human-engineered prompts and existing methods for automatic prompt generation by up to 25% and 14% respectively. Furthermore, EvoPrompt demonstrates that connecting LLMs with EAs creates synergies, which could inspire further research on the combination of LLMs and conventional algorithms.\n\n[View arXiv page](https://arxiv.org/abs/2309.08532) [View PDF](https://arxiv.org/pdf/2309.08532) [Add to collection](https://huggingface.co/login?next=%2Fpapers%2F2309.08532)\n\n### Community\n\n ![Image 59](https://huggingface.co/avatars/894469eccc3e21ac32b2ce32516f6238.svg) [zyxwvu](https://huggingface.co/zyxwvu)[Sep 18, 2023](https://huggingface.co/papers/2309.08532#6508b54b7ee07e274b19c1b8)\n\nThis comment has been hidden\n\n+\n\n ![Image 60](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/wJv5M54SrkGtkmmh0qPtv.jpeg) [Antkiv](https://huggingface.co/Antkiv)[Sep 20, 2023](https://huggingface.co/papers/2309.08532#650ad3f6008f8c12614775cd)\n\nFriends, how can I test this technology?\n\n+\n\nReply\n\n ![Image 61](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Sep 22, 2023](https://huggingface.co/papers/2309.08532#650d07fb5b868581f9480e74)\n\n> Friends, how can I test this technology?\n\nWe will release the code soon. Thanks for your attention quotes.\n\n+\n\nReply\n\n ![Image 62](https://huggingface.co/avatars/6cb1af50262e24546c3d8291b1190bc9.svg) [BarbiOlyAI](https://huggingface.co/BarbiOlyAI)[Sep 26, 2023](https://huggingface.co/papers/2309.08532#6512b2df734af2ca4df2f836)\n\nThis comment has been hidden\n\n+\n\n ![Image 63](https://huggingface.co/avatars/a9fddc9bc5f57f6bcd350ddc2ffad7ff.svg) [zhaokeke](https://huggingface.co/zhaokeke)[Oct 25, 2023](https://huggingface.co/papers/2309.08532#6538d110f84e87099ccb0b17)\n\n> > Friends, how can I test this technology?\n> \n> We will release the code soon. Thanks for your attention quotes.\n\nHello, is your code not yet released, or do you have an updated code release schedule?\n\n+\n\nReply\n\n ![Image 64](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Oct 26, 2023](https://huggingface.co/papers/2309.08532#6539d5fa43d9189cdce561b6)\n\n> > > Friends, how can I test this technology?\n> > \n> > We will release the code soon. Thanks for your attention quotes.\n> \n> Hello, is your code not yet released, or do you have an updated code release schedule?\n\nHi, we plan to release our code in 2 weeks.\n\n+\n\nReply\n\n ![Image 65](https://huggingface.co/avatars/13cab56e5290640f21fa45c06553eacd.svg) [UmberH](https://huggingface.co/UmberH)[Dec 8, 2023](https://huggingface.co/papers/2309.08532#65728e5bb3d8dd7b921d5e9c)\n\nis the code available now?\n\n+\n\nReply\n\n ![Image 66](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Dec 10, 2023](https://huggingface.co/papers/2309.08532#657583fbb238c76bbaf478af)\n\n> is the code available now?\n\nThe open-source of the code is on-going. We will share the link once it is available.\n\n+\n\nReply\n\n ![Image 67](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d1815e3029d4d5b748bb)\n\n•\n\n[edited Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d1815e3029d4d5b748bb \"Edited  by qingyan\")\n\n> is the code available now?\n\nSorry for the late release of our open-source code. You may refer to this repo temporarily ([https://github.com/beeevita/EvoPrompt](https://github.com/beeevita/EvoPrompt)) since the open-source of microsoft code is still in progress. If you find it helpful to your work, please star it. Thanks a lot~~😃😃\n\n+\n\nReply\n\n ![Image 68](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d192ef14f9e6038a6852)\n\n•\n\n[edited Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d192ef14f9e6038a6852 \"Edited  by qingyan\")\n\n> > > Friends, how can I test this technology?\n> > \n> > We will release the code soon. Thanks for your attention quotes.\n> \n> Hello, is your code not yet released, or do you have an updated code release schedule?\n\nSorry for the late release of our open-source code. You may refer to this repo temporarily ([https://github.com/beeevita/EvoPrompt](https://github.com/beeevita/EvoPrompt)) since the open-source of microsoft code is still in progress. If you find it helpful to your work, please star it. Thanks a lot~~😃😃\n\n+\n\nReply\n\n ![Image 69](https://cdn-avatars.huggingface.co/v1/production/uploads/6402b31e06c715b934053d6a/g7qGSUWaKQh6-2RLNWPIu.jpeg) [qingyan](https://huggingface.co/qingyan)Paper author [Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d19f1012559732be6c6b)\n\n•\n\n[edited Jan 18, 2024](https://huggingface.co/papers/2309.08532#65a8d19f1012559732be6c6b \"Edited 2 times by qingyan\")\n\n> Friends, how can I test this technology?\n\nSorry for the late release of our open-source code. You may refer to this repo temporarily ([https://github.com/beeevita/EvoPrompt](https://github.com/beeevita/EvoPrompt)) since the open-source of microsoft code is still in progress. If you find it helpful to your work, please star it. Thanks a lot~~😃😃\n\n+\n\nReply\n\nEditPreview\n\nUpload images, audio, and videos by dragging in the text input, pasting, or clicking here.\n\nTap or paste here to upload images\n\nComment· [Sign up](https://huggingface.co/join?next=%2Fpapers%2F2309.08532) or [log in](https://huggingface.co/login?next=%2Fpapers%2F2309.08532) to comment\n\n [Upvote 53](https://huggingface.co/login?next=%2Fpapers%2F2309.08532)\n\n*   [![Image 70](https://huggingface.co/avatars/e84732671896eabb90cbe6ed1711cd8d.svg)](https://huggingface.co/apollostream \"apollostream\")\n*   [![Image 71](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/YtJFOuny0YZlv_xTup7WV.jpeg)](https://huggingface.co/Zer0H1ro \"Zer0H1ro\")\n*   [![Image 72](https://huggingface.co/avatars/081751621bd13e83f5f712eaf5352c77.svg)](https://huggingface.co/TimLuo \"TimLuo\")\n*   [![Image 73](https://huggingface.co/avatars/83efc5b49a5f6d20ced04e7f2d9eac9b.svg)](https://huggingface.co/shenkha \"shenkha\")\n*   [![Image 74](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/HQiX0aBwCVONpd1b4gMda.png)](https://huggingface.co/zygoma919 \"zygoma919\")\n*   [![Image 75](https://huggingface.co/avatars/5346146aca9add2e6c02b01bf4c0df2e.svg)](https://huggingface.co/horyujey \"horyujey\")\n*   [![Image 76](https://huggingface.co/avatars/32a34625ebd6542be80c241c4e1c51d1.svg)](https://huggingface.co/michael-kingston \"michael-kingston\")\n*   [![Image 77](https://huggingface.co/avatars/c61c00c314cf202b64968e51e855694d.svg)](https://huggingface.co/jianhongbai \"jianhongbai\")\n*   [![Image 78](https://huggingface.co/avatars/a9fddc9bc5f57f6bcd350ddc2ffad7ff.svg)](https://huggingface.co/zhaokeke \"zhaokeke\")\n*   [![Image 79](https://cdn-avatars.huggingface.co/v1/production/uploads/6538119803519fddb4a17e10/ffJMkdx-rM7VvLTCM6ri_.jpeg)](https://huggingface.co/samusenps \"samusenps\")\n*   [![Image 80](https://cdn-avatars.huggingface.co/v1/production/uploads/6039478ab3ecf716b1a5fd4d/uc2Q5G2HKphTD0TbOsYiC.jpeg)](https://huggingface.co/taesiri \"taesiri\")\n*   [![Image 81](https://huggingface.co/avatars/2aad898b34a940a6aa4368526aa20d84.svg)](https://huggingface.co/hybris75 \"hybris75\")\n*   +41\n\nModels citing this paper 0\n--------------------------\n\nNo model linking this paper\n\nCite arxiv.org/abs/2309.08532 in a model README.md to link it from this page.\n\nDatasets citing this paper 0\n----------------------------\n\nNo dataset linking this paper\n\nCite arxiv.org/abs/2309.08532 in a dataset README.md to link it from this page.\n\n### Spaces citing this paper 0\n\nNo Space linking this paper\n\nCite arxiv.org/abs/2309.08532 in a Space README.md to link it from this page.\n\nCollections including this paper 31\n-----------------------------------\n\n[#### Dataset generation Collection 126 items • Updated Jul 22, 2024 • 26](https://huggingface.co/collections/stereoplegic/dataset-generation-65389dd75510eb595f8a3797)\n\n[#### NLP Paper Reading Collection NLP Papre Reading • 27 items • Updated Jan 31, 2024 • 9](https://huggingface.co/collections/Cartinoe5930/nlp-paper-reading-64fa9cc1bb362cbf2fd710b4)\n\n[#### Prompt Collection 92 items • Updated Feb 11, 2024 • 7](https://huggingface.co/collections/stereoplegic/prompt-6538a5ca61d44e23f3e0656e)\n\n[#### LLMs Collection 41 items • Updated Sep 25, 2023 • 5](https://huggingface.co/collections/krypticmouse/llms-650fa26b11f3210cf7b7ff51)\n\n[Browse 31 collections that include this paper](https://huggingface.co/collections?paper=2309.08532)\n\nSystem theme\n\nCompany\n\n[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Jobs](https://apply.workable.com/huggingface/)[](https://huggingface.co/)\n\nWebsite\n\n[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)",
  "usage": {
    "tokens": 4602
  }
}
```
