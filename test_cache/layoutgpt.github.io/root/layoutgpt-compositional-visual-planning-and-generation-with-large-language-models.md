---
title: LayoutGPT: Compositional Visual Planning and Generation with Large Language Models
description: LayoutGPT generates plausible image layouts and indoor scene layouts with style sheets language.
url: https://layoutgpt.github.io/
timestamp: 2025-01-20T15:42:31.546Z
domain: layoutgpt.github.io
path: root
---

# LayoutGPT: Compositional Visual Planning and Generation with Large Language Models


LayoutGPT generates plausible image layouts and indoor scene layouts with style sheets language.


## Content

1UC Santa Barbara, 2Google, 2UC Santa Cruz  
\*Equal Contribution

LayoutGPT for image layout generation based on text inputs.
-----------------------------------------------------------

LayoutGPT for 3D indoor scene synthesis.
----------------------------------------

Abstract
--------

Attaining a high degree of user controllability in visual generation often requires intricate, fine-grained inputs like layouts. However, such inputs impose a substantial burden on users when compared to simple text inputs. To address the issue, we study how Large Language Models (LLMs) can serve as visual planners by generating layouts from text conditions, and thus collaborate with visual generative models.

We propose LayoutGPT, a method to compose in-context visual demonstrations in style sheet language to enhance the visual planning skills of LLMs. LayoutGPT can generate plausible layouts in multiple domains, ranging from 2D images to 3D indoor scenes. LayoutGPT also shows superior performance in converting challenging language concepts like numerical and spatial relations to layout arrangements for faithful text-to-image generation.

When combined with a downstream image generation model, LayoutGPT outperforms text-to-image models/systems by 20-40% and achieves comparable performance as human users in designing visual layouts for numerical and spatial correctness. Lastly, LayoutGPT achieves comparable performance to supervised methods in 3D indoor scene synthesis, demonstrating its effectiveness and potential in multiple visual domains.

2D image layouts
----------------

### Faithfulness in Numerical and Spatial Concepts

LayoutGPT can apply the numerical reasoning skills of LLMs into layout generation and learn spatial concepts through in-context demonstrations.

![Image 9: Teaser](https://layoutgpt.github.io/static/images/2d_visualize.jpg)

  

### Flexible Application Scenarios

Two natural advantages of using LLMs for image layout generation:  
(1) Attribute Binding: assign correct attributes to the bounding boxes  
(2) Text-based inpainting: imagine and expand the underspecified description of certain objects.

![Image 10: Teaser](https://layoutgpt.github.io/static/images/2d_application.jpg)

3D Scene Synthesis
------------------

LayoutGPT shows comparable performance as supervised methods in indoor scene generation conditioned on room type and floor plan size.

![Image 11: Teaser](https://layoutgpt.github.io/static/images/3d_qualitative.png)

  

### Application: Scene Completion

The autoregressive manner of LLMs enables LayoutGPT to complete a partial scene.

![Image 12: Teaser](https://layoutgpt.github.io/static/images/3d_completion.png)

Related Links
-------------

Please check out previous work like [GLIGEN](https://gligen.github.io/), [ATISS](https://github.com/nv-tlabs/ATISS), and [GLIP](https://github.com/microsoft/GLIP) upon which we build our LayoutGPT framework and code repository. There's also a lot of relevant work that was introduced around the same time as ours.

BibTeX
------

```
@article{feng2023layoutgpt,
  title={LayoutGPT: Compositional Visual Planning and Generation with Large Language Models},
  author={Feng, Weixi and Zhu, Wanrong and Fu, Tsu-jui and Jampani, Varun and Akula, Arjun and He, Xuehai and Basu, Sugato and Wang, Xin Eric and Wang, William Yang},
  journal={arXiv preprint arXiv:2305.15393},
  year={2023}
}
```

## Metadata

```json
{
  "title": "LayoutGPT: Compositional Visual Planning and Generation with Large Language Models",
  "description": "LayoutGPT generates plausible image layouts and indoor scene layouts with style sheets language.",
  "url": "https://layoutgpt.github.io/",
  "content": "1UC Santa Barbara, 2Google, 2UC Santa Cruz  \n\\*Equal Contribution\n\nLayoutGPT for image layout generation based on text inputs.\n-----------------------------------------------------------\n\nLayoutGPT for 3D indoor scene synthesis.\n----------------------------------------\n\nAbstract\n--------\n\nAttaining a high degree of user controllability in visual generation often requires intricate, fine-grained inputs like layouts. However, such inputs impose a substantial burden on users when compared to simple text inputs. To address the issue, we study how Large Language Models (LLMs) can serve as visual planners by generating layouts from text conditions, and thus collaborate with visual generative models.\n\nWe propose LayoutGPT, a method to compose in-context visual demonstrations in style sheet language to enhance the visual planning skills of LLMs. LayoutGPT can generate plausible layouts in multiple domains, ranging from 2D images to 3D indoor scenes. LayoutGPT also shows superior performance in converting challenging language concepts like numerical and spatial relations to layout arrangements for faithful text-to-image generation.\n\nWhen combined with a downstream image generation model, LayoutGPT outperforms text-to-image models/systems by 20-40% and achieves comparable performance as human users in designing visual layouts for numerical and spatial correctness. Lastly, LayoutGPT achieves comparable performance to supervised methods in 3D indoor scene synthesis, demonstrating its effectiveness and potential in multiple visual domains.\n\n2D image layouts\n----------------\n\n### Faithfulness in Numerical and Spatial Concepts\n\nLayoutGPT can apply the numerical reasoning skills of LLMs into layout generation and learn spatial concepts through in-context demonstrations.\n\n![Image 9: Teaser](https://layoutgpt.github.io/static/images/2d_visualize.jpg)\n\n  \n\n### Flexible Application Scenarios\n\nTwo natural advantages of using LLMs for image layout generation:  \n(1) Attribute Binding: assign correct attributes to the bounding boxes  \n(2) Text-based inpainting: imagine and expand the underspecified description of certain objects.\n\n![Image 10: Teaser](https://layoutgpt.github.io/static/images/2d_application.jpg)\n\n3D Scene Synthesis\n------------------\n\nLayoutGPT shows comparable performance as supervised methods in indoor scene generation conditioned on room type and floor plan size.\n\n![Image 11: Teaser](https://layoutgpt.github.io/static/images/3d_qualitative.png)\n\n  \n\n### Application: Scene Completion\n\nThe autoregressive manner of LLMs enables LayoutGPT to complete a partial scene.\n\n![Image 12: Teaser](https://layoutgpt.github.io/static/images/3d_completion.png)\n\nRelated Links\n-------------\n\nPlease check out previous work like [GLIGEN](https://gligen.github.io/), [ATISS](https://github.com/nv-tlabs/ATISS), and [GLIP](https://github.com/microsoft/GLIP) upon which we build our LayoutGPT framework and code repository. There's also a lot of relevant work that was introduced around the same time as ours.\n\nBibTeX\n------\n\n```\n@article{feng2023layoutgpt,\n  title={LayoutGPT: Compositional Visual Planning and Generation with Large Language Models},\n  author={Feng, Weixi and Zhu, Wanrong and Fu, Tsu-jui and Jampani, Varun and Akula, Arjun and He, Xuehai and Basu, Sugato and Wang, Xin Eric and Wang, William Yang},\n  journal={arXiv preprint arXiv:2305.15393},\n  year={2023}\n}\n```",
  "usage": {
    "tokens": 731
  }
}
```
