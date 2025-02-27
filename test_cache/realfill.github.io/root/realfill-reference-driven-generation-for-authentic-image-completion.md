---
title: RealFill: Reference-Driven Generation for Authentic Image Completion
description: RealFill: Reference-Driven Generation for Authentic Image Completion
url: https://realfill.github.io/
timestamp: 2025-01-20T15:45:14.611Z
domain: realfill.github.io
path: root
---

# RealFill: Reference-Driven Generation for Authentic Image Completion


RealFill: Reference-Driven Generation for Authentic Image Completion


## Content

[Luming Tang](https://lumingtang.info/)1,2, [Nataniel Ruiz](https://natanielruiz.github.io/)1, [Qinghao Chu](https://github.com/qinghao1)1, [Yuanzhen Li](https://people.csail.mit.edu/yzli/)1, [Aleksander Holynski](https://holynski.org/)1, [David E. Jacobs](https://scholar.google.com/citations?hl=en&user=0VQ1sjcAAAAJ)1,  
[Bharath Hariharan](https://www.cs.cornell.edu/~bharathh/)2, [Yael Pritch](https://scholar.google.co.il/citations?user=Zi5KiDsAAAAJ)1, [Neal Wadhwa](https://nealwadhwa.com/)1, [Kfir Aberman](https://kfiraberman.github.io/)1, [Michael Rubinstein](https://people.csail.mit.edu/mrub/)1

  

SIGGRAPH 2024 (Journal Track)
-----------------------------

### _**RealFill**_  is able to complete the image with **what should have been there**.

Abstract
--------

Recent advances in generative imagery have brought forth outpainting and inpainting models that can produce high-quality, plausible image content in unknown regions, but the content these models hallucinate is necessarily inauthentic, since the models lack sufficient context about the true scene. In this work, we propose **_RealFill_**, a novel generative approach for image completion that fills in missing regions of an image with the content that _should have been there_. RealFill is a generative inpainting model that is personalized using only a few reference images of a scene. These reference images do not have to be aligned with the target image, and can be taken with drastically varying viewpoints, lighting conditions, camera apertures, or image styles. Once personalized, RealFill is able to complete a target image with visually compelling contents that are faithful to the original scene. We evaluate RealFill on a new image completion benchmark that covers a set of diverse and challenging scenarios, and find that it outperforms existing approaches by a large margin.

Method
------

**Authentic Image Completion**: Given a few reference images (up to five) and one target image that captures roughly the same scene (but in a different arrangement or appearance), we aim to fill missing regions of the target image with high-quality image content that is faithful to the originally captured scene. Note that for the sake of practical benefit, we focus particularly on the more challenging, unconstrained setting in which the target and reference images may have very different viewpoints, environmental conditions, camera apertures, image styles, or even moving objects.

**RealFill**: For a given scene, we first create a personalized generative model by fine-tuning a pre-trained inpainting diffusion model on the reference and target images. This fine-tuning process is designed such that the adapted model not only maintains a good image prior, but also learns the contents, lighting, and style of the scene in the input images. We then use this fine-tuned model to fill the missing regions in the target image through a standard diffusion sampling process.

  

Results
-------

Given the reference images on the left, RealFill is able to either uncrop or inpaint the target image on the right, resulting in high-quality images that are both visually compelling and also faithful to the references, even when there are large differences between references and targets including viewpoint, aperture, lighting, image style, and object motion.

Comparison with Baselines
-------------------------

A comparison of RealFill and baseline methods. Transparent white masks are overlayed on the unaltered known regions of the target images.

*   Paint-by-Example does not achieve high scene fidelity because it relies on CLIP embeddings, which only capture high-level semantic information.
*   TransFill outputs low quality images due to the lack of a good image prior and the limitations of its geometry-based pipeline.
*   Photoshop Generative Fill produces plausible results, they are inconsistent with the reference images because prompts have limited expressiveness.

In contrast, RealFill generates high-quality results that have high fidelity with respect to the reference images.

![Image 5](https://realfill.github.io/static/images/quality_5row.jpg)

### Limitations

*   RealFill needs to go through a gradient-based fine-tuning process on input images, rendering it relatively slow.
*   When viewpoint change between reference and target images is very large, RealFill tends to fail at recovering the 3D scene, especially when there is only a single reference image.
*   Because RealFill mainly relies on the image prior inherited from the base pre-trained model, it also fails to handle cases where that are challenging for the base model, such as text for Stable Diffusion.

![Image 6](https://realfill.github.io/static/images/failure_compressed.jpeg)

### Acknowledgements

Luming and Bharath are supported by NSF IIS-2144117. We would like to thank Rundi Wu, Qianqian Wang, Viraj Shah, Ethan Weber, Zhengqi Li, Kyle Genova, Richard Tucker, Boyang Deng, Maya Goldenberg, Noah Snavely, Ben Poole, Ben Mildenhall, Alex Rav-Acha, Pratul Srinivasan, Dor Verbin, Jon Barron and all the anonymous reviewers for their valuable discussion and feedbacks, and thank Zeya Peng, Rundi Wu, Shan Nan for their contribution to the evaluation dataset. A special thanks to Jason Baldridge, Kihyuk Sohn, Kathy Meier-Hellstern, and Nicole Brichtova for their feedback and support for the project.

### BibTeX

```

@article{tang2023realfill,
  title={RealFill: Reference-Driven Generation for Authentic Image Completion},
  author={Tang, Luming and Ruiz, Nataniel and Qinghao, Chu and Li, Yuanzhen and Holynski, Aleksander and 
    Jacobs, David E and Hariharan, Bharath and Pritch, Yael and Wadhwa, Neal and Aberman, Kfir and Rubinstein, Michael},
  journal={arXiv preprint arXiv:2309.16668},
  year={2023}
}
```

## Metadata

```json
{
  "title": "RealFill: Reference-Driven Generation for Authentic Image Completion",
  "description": "RealFill: Reference-Driven Generation for Authentic Image Completion",
  "url": "https://realfill.github.io/",
  "content": "[Luming Tang](https://lumingtang.info/)1,2, [Nataniel Ruiz](https://natanielruiz.github.io/)1, [Qinghao Chu](https://github.com/qinghao1)1, [Yuanzhen Li](https://people.csail.mit.edu/yzli/)1, [Aleksander Holynski](https://holynski.org/)1, [David E. Jacobs](https://scholar.google.com/citations?hl=en&user=0VQ1sjcAAAAJ)1,  \n[Bharath Hariharan](https://www.cs.cornell.edu/~bharathh/)2, [Yael Pritch](https://scholar.google.co.il/citations?user=Zi5KiDsAAAAJ)1, [Neal Wadhwa](https://nealwadhwa.com/)1, [Kfir Aberman](https://kfiraberman.github.io/)1, [Michael Rubinstein](https://people.csail.mit.edu/mrub/)1\n\n  \n\nSIGGRAPH 2024 (Journal Track)\n-----------------------------\n\n### _**RealFill**_  is able to complete the image with **what should have been there**.\n\nAbstract\n--------\n\nRecent advances in generative imagery have brought forth outpainting and inpainting models that can produce high-quality, plausible image content in unknown regions, but the content these models hallucinate is necessarily inauthentic, since the models lack sufficient context about the true scene. In this work, we propose **_RealFill_**, a novel generative approach for image completion that fills in missing regions of an image with the content that _should have been there_. RealFill is a generative inpainting model that is personalized using only a few reference images of a scene. These reference images do not have to be aligned with the target image, and can be taken with drastically varying viewpoints, lighting conditions, camera apertures, or image styles. Once personalized, RealFill is able to complete a target image with visually compelling contents that are faithful to the original scene. We evaluate RealFill on a new image completion benchmark that covers a set of diverse and challenging scenarios, and find that it outperforms existing approaches by a large margin.\n\nMethod\n------\n\n**Authentic Image Completion**: Given a few reference images (up to five) and one target image that captures roughly the same scene (but in a different arrangement or appearance), we aim to fill missing regions of the target image with high-quality image content that is faithful to the originally captured scene. Note that for the sake of practical benefit, we focus particularly on the more challenging, unconstrained setting in which the target and reference images may have very different viewpoints, environmental conditions, camera apertures, image styles, or even moving objects.\n\n**RealFill**: For a given scene, we first create a personalized generative model by fine-tuning a pre-trained inpainting diffusion model on the reference and target images. This fine-tuning process is designed such that the adapted model not only maintains a good image prior, but also learns the contents, lighting, and style of the scene in the input images. We then use this fine-tuned model to fill the missing regions in the target image through a standard diffusion sampling process.\n\n  \n\nResults\n-------\n\nGiven the reference images on the left, RealFill is able to either uncrop or inpaint the target image on the right, resulting in high-quality images that are both visually compelling and also faithful to the references, even when there are large differences between references and targets including viewpoint, aperture, lighting, image style, and object motion.\n\nComparison with Baselines\n-------------------------\n\nA comparison of RealFill and baseline methods. Transparent white masks are overlayed on the unaltered known regions of the target images.\n\n*   Paint-by-Example does not achieve high scene fidelity because it relies on CLIP embeddings, which only capture high-level semantic information.\n*   TransFill outputs low quality images due to the lack of a good image prior and the limitations of its geometry-based pipeline.\n*   Photoshop Generative Fill produces plausible results, they are inconsistent with the reference images because prompts have limited expressiveness.\n\nIn contrast, RealFill generates high-quality results that have high fidelity with respect to the reference images.\n\n![Image 5](https://realfill.github.io/static/images/quality_5row.jpg)\n\n### Limitations\n\n*   RealFill needs to go through a gradient-based fine-tuning process on input images, rendering it relatively slow.\n*   When viewpoint change between reference and target images is very large, RealFill tends to fail at recovering the 3D scene, especially when there is only a single reference image.\n*   Because RealFill mainly relies on the image prior inherited from the base pre-trained model, it also fails to handle cases where that are challenging for the base model, such as text for Stable Diffusion.\n\n![Image 6](https://realfill.github.io/static/images/failure_compressed.jpeg)\n\n### Acknowledgements\n\nLuming and Bharath are supported by NSF IIS-2144117. We would like to thank Rundi Wu, Qianqian Wang, Viraj Shah, Ethan Weber, Zhengqi Li, Kyle Genova, Richard Tucker, Boyang Deng, Maya Goldenberg, Noah Snavely, Ben Poole, Ben Mildenhall, Alex Rav-Acha, Pratul Srinivasan, Dor Verbin, Jon Barron and all the anonymous reviewers for their valuable discussion and feedbacks, and thank Zeya Peng, Rundi Wu, Shan Nan for their contribution to the evaluation dataset. A special thanks to Jason Baldridge, Kihyuk Sohn, Kathy Meier-Hellstern, and Nicole Brichtova for their feedback and support for the project.\n\n### BibTeX\n\n```\n\n@article{tang2023realfill,\n  title={RealFill: Reference-Driven Generation for Authentic Image Completion},\n  author={Tang, Luming and Ruiz, Nataniel and Qinghao, Chu and Li, Yuanzhen and Holynski, Aleksander and \n    Jacobs, David E and Hariharan, Bharath and Pritch, Yael and Wadhwa, Neal and Aberman, Kfir and Rubinstein, Michael},\n  journal={arXiv preprint arXiv:2309.16668},\n  year={2023}\n}\n```",
  "usage": {
    "tokens": 1319
  }
}
```
