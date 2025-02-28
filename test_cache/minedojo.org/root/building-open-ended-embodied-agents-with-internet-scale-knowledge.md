---
title: Building Open-Ended Embodied Agents with Internet-Scale Knowledge
description: 
url: https://minedojo.org/
timestamp: 2025-01-20T15:46:29.567Z
domain: minedojo.org
path: root
---

# Building Open-Ended Embodied Agents with Internet-Scale Knowledge



## Content

Introduction
------------

ChatGPT is powerful but ungrounded. The future of Foundation Models will be embodied agents that proactively take actions, endlessly explore the world, and continuously self-improve. What does it take? See our Twitter [post](https://twitter.com/DrJimFan/status/1595459499732926464?s=20&t=r0baONq697iu_kIITTKR5Q) for a blueprint of this future.

Massively Multitask Benchmarking Suite
--------------------------------------

MineDojo is a new framework built on the popular [Minecraft](https://en.wikipedia.org/wiki/Minecraft) game for embodied agent research. MineDojo features a simulation suite with 1000s of open-ended and language-prompted tasks, where the AI agents can freely explore a procedurally generated 3D world with diverse terrains to roam, materials to mine, tools to craft, structures to build, and wonders to discover.

Open-ended Exploration in [Overworld](https://minecraft.fandom.com/wiki/Overworld), [The Nether](https://minecraft.fandom.com/wiki/The_Nether), and [The End](https://minecraft.fandom.com/wiki/The_End)

*   Fight against an [Ender dragon ![Image 44](https://minedojo.org/images/icons/ender_dragon.gif)](https://minecraft.fandom.com/wiki/Ender_Dragon)
    
*   Scoop a [bucket of lava![Image 45](https://minedojo.org/images/icons/lava_bucket.png)](https://minecraft.fandom.com/wiki/Lava_Bucket)
    
*   Explore an [ocean monument ![Image 46](https://minedojo.org/images/icons/ocean_monument.png)](https://minecraft.fandom.com/wiki/Ocean_Monument)
    
*   Find a [desert pyramid ![Image 47](https://minedojo.org/images/icons/desert_temple.png)](https://minecraft.fandom.com/wiki/Desert_pyramid)
    

Wide Variety of Terrains, Weathers, and Items

*   Equip different levels of [armor ![Image 48](https://minedojo.org/images/icons/armor.gif)](https://minecraft.fandom.com/wiki/Armor)
    
*   Build a [Nether Portal ![Image 49](https://minedojo.org/images/icons/nether_portal.png)](https://minecraft.fandom.com/wiki/Nether_portal) and enter it
    
*   Visit an [end city ![Image 50](https://minedojo.org/images/icons/end_city.png)](https://minecraft.fandom.com/wiki/End_City)
    
*   Traverse different [terrains ![Image 51](https://minedojo.org/images/icons/all_biomes.png)](https://minecraft.fandom.com/wiki/Biome)
    

Diverse and Creative Tool Usage

*   Encircle [llamas ![Image 52](https://minedojo.org/images/icons/llama.png)](https://minecraft.fandom.com/wiki/Llama) with [fences ![Image 53](https://minedojo.org/images/icons/fence.png)](https://minecraft.fandom.com/wiki/Fence)
    
*   Play fireball with a [ghast ![Image 54](https://minedojo.org/images/icons/ghast.png)](https://minecraft.fandom.com/wiki/Ghast)
    
*   Grow [wheat ![Image 55](https://minedojo.org/images/icons/wheat.png)](https://minecraft.fandom.com/wiki/Wheat)
    
*   Block damage with a [shield ![Image 56](https://minedojo.org/images/icons/shield.png)](https://minecraft.fandom.com/wiki/Shield)
    

Minecraft has more than 100M active players, who have collectively generated an enormous wealth of data. MineDojo features a massive database collected automatically from the internet. AI agents can learn from this treasure trove of knowledge to harvest actionable insights, acquire diverse skills, develop complex strategies, and discover interesting objectives to pursue. All our databases are open-access and available to download today! Click on each card below to find out more.

*   [![Image 57](https://minedojo.org/images/card/youtube.png)730K YouTube videos with 2.2B words in English transcripts](https://minedojo.org/knowledge_base.html#youtube)
*   [![Image 58](https://minedojo.org/images/card/wiki.png)~7K Wiki pages with interleaved text, images, tables, and diagrams](https://minedojo.org/knowledge_base.html#wiki)
*   [![Image 59](https://minedojo.org/images/card/reddit.png)340K Reddit posts with 6.6M comments in r/Minecraft subreddit](https://minedojo.org/knowledge_base.html#reddit)

MineCLIP
--------

We propose a conceptually simple method to learn a Minecraft-playing agent from in-the-wild YouTube videos. It is far from solving the game, but shows a baby step towards our vision of an “embodied GPT3” that takes the right actions given any language prompts.

Since our YouTube dataset has time-aligned narration, we are able to train a video-language contrastive model called MineCLIP. Intuitively, it learns to associate a video with the text that describes the video activity. MineCLIP computes a correlation score between \[0, 1\].

How do we use MineCLIP for training? Given a text prompt, the agent interacts with the Minecraft sim and generates a video, which can be fed to MineCLIP to compute correlation with the prompt. The higher the correlation, the more the agent’s behavior is on the right track.

Team
----

Email lead developers.   \* Equal contribution.   † Equal advising.

Check out our paper!  
[](https://arxiv.org/abs/2206.08853)[](https://arxiv.org/pdf/2206.08853.pdf)[](https://neurips.cc/media/PosterPDFs/NeurIPS%202022/55737.png?t=1667982802.2161448)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
@inproceedings{fan2022minedojo,
  title = {MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge},
  author = {Linxi Fan and Guanzhi Wang and Yunfan Jiang and Ajay Mandlekar and Yuncong Yang and Haoyi Zhu and Andrew Tang and De-An Huang and Yuke Zhu and Anima Anandkumar},
  booktitle = {Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year = {2022},
  url = {https://openreview.net/forum?id=rc8o_j8I8PX}
}
```

MineDojo team ©2022

## Metadata

```json
{
  "title": "Building Open-Ended Embodied Agents with Internet-Scale Knowledge",
  "description": "",
  "url": "https://minedojo.org/",
  "content": "Introduction\n------------\n\nChatGPT is powerful but ungrounded. The future of Foundation Models will be embodied agents that proactively take actions, endlessly explore the world, and continuously self-improve. What does it take? See our Twitter [post](https://twitter.com/DrJimFan/status/1595459499732926464?s=20&t=r0baONq697iu_kIITTKR5Q) for a blueprint of this future.\n\nMassively Multitask Benchmarking Suite\n--------------------------------------\n\nMineDojo is a new framework built on the popular [Minecraft](https://en.wikipedia.org/wiki/Minecraft) game for embodied agent research. MineDojo features a simulation suite with 1000s of open-ended and language-prompted tasks, where the AI agents can freely explore a procedurally generated 3D world with diverse terrains to roam, materials to mine, tools to craft, structures to build, and wonders to discover.\n\nOpen-ended Exploration in [Overworld](https://minecraft.fandom.com/wiki/Overworld), [The Nether](https://minecraft.fandom.com/wiki/The_Nether), and [The End](https://minecraft.fandom.com/wiki/The_End)\n\n*   Fight against an [Ender dragon ![Image 44](https://minedojo.org/images/icons/ender_dragon.gif)](https://minecraft.fandom.com/wiki/Ender_Dragon)\n    \n*   Scoop a [bucket of lava![Image 45](https://minedojo.org/images/icons/lava_bucket.png)](https://minecraft.fandom.com/wiki/Lava_Bucket)\n    \n*   Explore an [ocean monument ![Image 46](https://minedojo.org/images/icons/ocean_monument.png)](https://minecraft.fandom.com/wiki/Ocean_Monument)\n    \n*   Find a [desert pyramid ![Image 47](https://minedojo.org/images/icons/desert_temple.png)](https://minecraft.fandom.com/wiki/Desert_pyramid)\n    \n\nWide Variety of Terrains, Weathers, and Items\n\n*   Equip different levels of [armor ![Image 48](https://minedojo.org/images/icons/armor.gif)](https://minecraft.fandom.com/wiki/Armor)\n    \n*   Build a [Nether Portal ![Image 49](https://minedojo.org/images/icons/nether_portal.png)](https://minecraft.fandom.com/wiki/Nether_portal) and enter it\n    \n*   Visit an [end city ![Image 50](https://minedojo.org/images/icons/end_city.png)](https://minecraft.fandom.com/wiki/End_City)\n    \n*   Traverse different [terrains ![Image 51](https://minedojo.org/images/icons/all_biomes.png)](https://minecraft.fandom.com/wiki/Biome)\n    \n\nDiverse and Creative Tool Usage\n\n*   Encircle [llamas ![Image 52](https://minedojo.org/images/icons/llama.png)](https://minecraft.fandom.com/wiki/Llama) with [fences ![Image 53](https://minedojo.org/images/icons/fence.png)](https://minecraft.fandom.com/wiki/Fence)\n    \n*   Play fireball with a [ghast ![Image 54](https://minedojo.org/images/icons/ghast.png)](https://minecraft.fandom.com/wiki/Ghast)\n    \n*   Grow [wheat ![Image 55](https://minedojo.org/images/icons/wheat.png)](https://minecraft.fandom.com/wiki/Wheat)\n    \n*   Block damage with a [shield ![Image 56](https://minedojo.org/images/icons/shield.png)](https://minecraft.fandom.com/wiki/Shield)\n    \n\nMinecraft has more than 100M active players, who have collectively generated an enormous wealth of data. MineDojo features a massive database collected automatically from the internet. AI agents can learn from this treasure trove of knowledge to harvest actionable insights, acquire diverse skills, develop complex strategies, and discover interesting objectives to pursue. All our databases are open-access and available to download today! Click on each card below to find out more.\n\n*   [![Image 57](https://minedojo.org/images/card/youtube.png)730K YouTube videos with 2.2B words in English transcripts](https://minedojo.org/knowledge_base.html#youtube)\n*   [![Image 58](https://minedojo.org/images/card/wiki.png)~7K Wiki pages with interleaved text, images, tables, and diagrams](https://minedojo.org/knowledge_base.html#wiki)\n*   [![Image 59](https://minedojo.org/images/card/reddit.png)340K Reddit posts with 6.6M comments in r/Minecraft subreddit](https://minedojo.org/knowledge_base.html#reddit)\n\nMineCLIP\n--------\n\nWe propose a conceptually simple method to learn a Minecraft-playing agent from in-the-wild YouTube videos. It is far from solving the game, but shows a baby step towards our vision of an “embodied GPT3” that takes the right actions given any language prompts.\n\nSince our YouTube dataset has time-aligned narration, we are able to train a video-language contrastive model called MineCLIP. Intuitively, it learns to associate a video with the text that describes the video activity. MineCLIP computes a correlation score between \\[0, 1\\].\n\nHow do we use MineCLIP for training? Given a text prompt, the agent interacts with the Minecraft sim and generates a video, which can be fed to MineCLIP to compute correlation with the prompt. The higher the correlation, the more the agent’s behavior is on the right track.\n\nTeam\n----\n\nEmail lead developers.   \\* Equal contribution.   † Equal advising.\n\nCheck out our paper!  \n[](https://arxiv.org/abs/2206.08853)[](https://arxiv.org/pdf/2206.08853.pdf)[](https://neurips.cc/media/PosterPDFs/NeurIPS%202022/55737.png?t=1667982802.2161448)\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n```\n@inproceedings{fan2022minedojo,\n  title = {MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge},\n  author = {Linxi Fan and Guanzhi Wang and Yunfan Jiang and Ajay Mandlekar and Yuncong Yang and Haoyi Zhu and Andrew Tang and De-An Huang and Yuke Zhu and Anima Anandkumar},\n  booktitle = {Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track},\n  year = {2022},\n  url = {https://openreview.net/forum?id=rc8o_j8I8PX}\n}\n```\n\nMineDojo team ©2022",
  "usage": {
    "tokens": 1426
  }
}
```
