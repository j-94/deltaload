---
title: LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models
description: LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models
url: https://vchitect.github.io/LaVie-project/
timestamp: 2025-01-20T15:45:36.987Z
domain: vchitect.github.io
path: LaVie-project
---

# LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models


LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models


## Content

[Xinyuan Chen](https://scholar.google.com/citations?user=3fWSC8YAAAAJ)1\*, [Xin Ma](https://maxin-cn.github.io/)1,4\*‡, [Shangchen Zhou](https://shangchenzhou.com/)2, [Ziqi Huang](https://ziqihuangg.github.io/)2, [Yi Wang](https://shepnerd.github.io/)1, [Ceyuan Yang](https://ceyuan.me/)1, [Yinan He](https://github.com/yinanhe)1, [Jiashuo Yu](https://scholar.google.com/citations?user=iH0Aq0YAAAAJ&hl=en)1, [Peiqing Yang](https://pq-yang.github.io/)2, [Yuwei Guo](https://github.com/guoyww)1,3, [Tianxing Wu](https://tianxingwu.github.io/)2, [Chenyang Si](http://chenyangsi.top/)2, [Yuming Jiang](https://yumingj.github.io/)2, [Cunjian Chen](https://cunjian.github.io/)4, [Chen Change Loy](https://www.mmlab-ntu.com/person/ccloy/)2, [Bo Dai](https://daibo.info/)1, [Dahua Lin](http://dahua.site/)1,3†, [Yu Qiao](https://scholar.google.com.hk/citations?user=gFtI-8QAAAAJ&hl=zh-CN)1†, [Ziwei Liu](https://liuziwei7.github.io/)2,1†

1Shanghai Artificial Intelligence Laboratory  2S-Lab, Nanyang Technological University  3The Chinese University of Hong Kong  4Monash University

\*Equal contribution †Corresponding author

‡Work done during internship at Shanghai AI Laboratory

Text-to-Video Generation
------------------------

(Click image to play video)
---------------------------

Cinematic shot of Van Gogh's selfie, Van Gogh style

A corgi’s head depicted as an explosion of a nebula, high quality

A panda drinking coffee in a cafe in Paris

Iron Man flying in the sky

A jellyfish floating through the ocean, with bioluminescent tentacles

A Mars rover moving on Mars

The bund Shanghai, oil painting

A fantasy landscape, trending on artstation, 4k, high resolution

A space shuttle launching into orbit, with flames and smoke billowing out from the engines

A super cool giant robot in Cyberpunk city, artstation

A tropical beach at sunrise, with palm trees and crystal-clear water in the foreground

A robot dj is playing the turntable, in heavy raining futuristic tokyo rooftop cyberpunk night, sci-fi, fantasy, intrica

Gwen Stacy reading a book

A future where humans have achieved teleportation technology

A steam train moving on a mountainside by Vincent van Gogh

Yoda playing guitar on the stage

A beautiful coastal beach in spring, waves lapping on sand by Hokusai, in the style of Ukiyo

A happy fuzzy panda playing guitar nearby a campfire, snow mountain in the background

\--\>

A cat eating food out of a bowl, in style of Van Gogh

A boat sailing leisurely along the Seine River with the Eiffel Tower in background by Vincent van Gogh

Vincent van Gogh is painting in the room

Abstract
--------

This work aims to learn a high-quality text-to-video (T2V) generative model by leveraging a pre-trained text-to-image (T2I) model as a basis. It is a highly desirable yet challenging task to simultaneously a) accomplish the synthesis of visually realistic and temporally coherent videos while b) preserving the strong creative generation nature of the pre-trained T2I model. To this end, we propose LaVie, an integrated video generation framework that operates on cascaded video latent diffusion models, comprising a base T2V model, a temporal interpolation model, and a video super-resolution model. Our key insights are two-fold: 1) We reveal that the incorporation of simple temporal self-attentions, coupled with relative positional encoding, adequately captures the temporal correlations inherent in video data. 2) Additionally, we validate that the process of joint image-video fine-tuning plays a pivotal role in producing high-quality and creative outcomes. To enhance the performance of LaVie, we contribute a comprehensive and diverse video dataset named Vimeo25M, consisting of 25 million text-video pairs that prioritize quality, diversity, and aesthetic appeal. Extensive experiments demonstrate that LaVie achieves state-of-the-art performance both quantitatively and qualitatively. Furthermore, we showcase the versatility of pre-trained LaVie models in various long video generation and personalized video synthesis applications.

BibTeX
------

```
@article{wang2023lavie,
  title={LAVIE: High-Quality Video Generation with Cascaded Latent Diffusion Models},
  author={Wang, Yaohui and Chen, Xinyuan and Ma, Xin and Zhou, Shangchen and Huang, Ziqi and Wang, Yi and Yang, Ceyuan and He, Yinan and Yu, Jiashuo and Yang, Peiqing and others},
  journal={arXiv preprint arXiv:2309.15103},
  year={2023}}
```

## Metadata

```json
{
  "title": "LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models",
  "description": "LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models",
  "url": "https://vchitect.github.io/LaVie-project/",
  "content": "[Xinyuan Chen](https://scholar.google.com/citations?user=3fWSC8YAAAAJ)1\\*, [Xin Ma](https://maxin-cn.github.io/)1,4\\*‡, [Shangchen Zhou](https://shangchenzhou.com/)2, [Ziqi Huang](https://ziqihuangg.github.io/)2, [Yi Wang](https://shepnerd.github.io/)1, [Ceyuan Yang](https://ceyuan.me/)1, [Yinan He](https://github.com/yinanhe)1, [Jiashuo Yu](https://scholar.google.com/citations?user=iH0Aq0YAAAAJ&hl=en)1, [Peiqing Yang](https://pq-yang.github.io/)2, [Yuwei Guo](https://github.com/guoyww)1,3, [Tianxing Wu](https://tianxingwu.github.io/)2, [Chenyang Si](http://chenyangsi.top/)2, [Yuming Jiang](https://yumingj.github.io/)2, [Cunjian Chen](https://cunjian.github.io/)4, [Chen Change Loy](https://www.mmlab-ntu.com/person/ccloy/)2, [Bo Dai](https://daibo.info/)1, [Dahua Lin](http://dahua.site/)1,3†, [Yu Qiao](https://scholar.google.com.hk/citations?user=gFtI-8QAAAAJ&hl=zh-CN)1†, [Ziwei Liu](https://liuziwei7.github.io/)2,1†\n\n1Shanghai Artificial Intelligence Laboratory  2S-Lab, Nanyang Technological University  3The Chinese University of Hong Kong  4Monash University\n\n\\*Equal contribution †Corresponding author\n\n‡Work done during internship at Shanghai AI Laboratory\n\nText-to-Video Generation\n------------------------\n\n(Click image to play video)\n---------------------------\n\nCinematic shot of Van Gogh's selfie, Van Gogh style\n\nA corgi’s head depicted as an explosion of a nebula, high quality\n\nA panda drinking coffee in a cafe in Paris\n\nIron Man flying in the sky\n\nA jellyfish floating through the ocean, with bioluminescent tentacles\n\nA Mars rover moving on Mars\n\nThe bund Shanghai, oil painting\n\nA fantasy landscape, trending on artstation, 4k, high resolution\n\nA space shuttle launching into orbit, with flames and smoke billowing out from the engines\n\nA super cool giant robot in Cyberpunk city, artstation\n\nA tropical beach at sunrise, with palm trees and crystal-clear water in the foreground\n\nA robot dj is playing the turntable, in heavy raining futuristic tokyo rooftop cyberpunk night, sci-fi, fantasy, intrica\n\nGwen Stacy reading a book\n\nA future where humans have achieved teleportation technology\n\nA steam train moving on a mountainside by Vincent van Gogh\n\nYoda playing guitar on the stage\n\nA beautiful coastal beach in spring, waves lapping on sand by Hokusai, in the style of Ukiyo\n\nA happy fuzzy panda playing guitar nearby a campfire, snow mountain in the background\n\n\\--\\>\n\nA cat eating food out of a bowl, in style of Van Gogh\n\nA boat sailing leisurely along the Seine River with the Eiffel Tower in background by Vincent van Gogh\n\nVincent van Gogh is painting in the room\n\nAbstract\n--------\n\nThis work aims to learn a high-quality text-to-video (T2V) generative model by leveraging a pre-trained text-to-image (T2I) model as a basis. It is a highly desirable yet challenging task to simultaneously a) accomplish the synthesis of visually realistic and temporally coherent videos while b) preserving the strong creative generation nature of the pre-trained T2I model. To this end, we propose LaVie, an integrated video generation framework that operates on cascaded video latent diffusion models, comprising a base T2V model, a temporal interpolation model, and a video super-resolution model. Our key insights are two-fold: 1) We reveal that the incorporation of simple temporal self-attentions, coupled with relative positional encoding, adequately captures the temporal correlations inherent in video data. 2) Additionally, we validate that the process of joint image-video fine-tuning plays a pivotal role in producing high-quality and creative outcomes. To enhance the performance of LaVie, we contribute a comprehensive and diverse video dataset named Vimeo25M, consisting of 25 million text-video pairs that prioritize quality, diversity, and aesthetic appeal. Extensive experiments demonstrate that LaVie achieves state-of-the-art performance both quantitatively and qualitatively. Furthermore, we showcase the versatility of pre-trained LaVie models in various long video generation and personalized video synthesis applications.\n\nBibTeX\n------\n\n```\n@article{wang2023lavie,\n  title={LAVIE: High-Quality Video Generation with Cascaded Latent Diffusion Models},\n  author={Wang, Yaohui and Chen, Xinyuan and Ma, Xin and Zhou, Shangchen and Huang, Ziqi and Wang, Yi and Yang, Ceyuan and He, Yinan and Yu, Jiashuo and Yang, Peiqing and others},\n  journal={arXiv preprint arXiv:2309.15103},\n  year={2023}}\n```",
  "usage": {
    "tokens": 1154
  }
}
```
