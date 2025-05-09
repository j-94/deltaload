---
title: Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs
description: Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs
url: https://jingsenzhu.github.io/i2-sdf/
timestamp: 2025-01-20T15:42:30.448Z
domain: jingsenzhu.github.io
path: i2-sdf
---

# Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs


Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs


## Content

More Research
I2-SDF: Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs
Jingsen Zhu1, Yuchi Huo2,1, Qi Ye3,6, Fujun Luan4, Jifan Li1, Dianbing Xi1, Lisha Wang1, Rui Tang5, Wei Hua2, Hujun Bao1, Rui Wang1
1State Key Lab of CAD&CG, Zhejiang University, 2Zhejiang Lab, 3Zhejiang University, 4Adobe Research, 5KooLab, Manycore 6Key Lab of CS&AUS of Zhejiang Province
CVPR 2023
Paper
 
arXiv
 
Code
 
Data
TL;DR: I2-SDF resolves challenges in reconstructing small objects inside an indoor scene by a novel bubble loss (Left), and leverages intrinsic decomposition and raytracing to enable photorealistic scene editing and relighting (Right).
Abstract
In this work, we present I2-SDF, a new method for intrinsic indoor scene reconstruction and editing using differentiable Monte Carlo raytracing on neural signed distance fields (SDFs). Our holistic neural SDF-based framework jointly recovers the underlying shapes, incident radiance and materials from multi-view images. We introduce a novel bubble loss for fine-grained small objects and error-guided adaptive sampling scheme to largely improve the reconstruction quality on large-scale indoor scenes. Further, we propose to decompose the neural radiance field into spatially-varying material of the scene as a neural field through surface-based, differentiable Monte Carlo raytracing and emitter semantic segmentations, which enables physically based and photorealistic scene relighting and editing applications. Through a number of qualitative and quantitative experiments, we demonstrate the superior quality of our method on indoor scene reconstruction, novel view synthesis, and scene editing compared to state-of-the-art baselines.

I2-Dataset: Synthetic Indoor Multiview Dataset
		
		

We provide a synthetic indoor dataset of well-designed scenes, with ground truth poses, geometry and material annotations.
Geometry Reconstruction

We analyze the vanishing gradient problem of SDF-based volume rendering techniques, which results in failures of existing methods to reconstruct off-surface small objects. We propose a novel bubble loss to tackle this.
Novel View Synthesis

Our method outperforms previous methods in novel view synthesis of indoor scenes. Previous methods suffers from either reconstruction failure or overfitting.
Editing and Relighting

We disentangle material (physically-based BRDF) and lighting (direct emission and indirect illumination) to enable photorealistic scene editing and relighting using Monte-Carlo raytracing.
BibTeX
@inproceedings{zhu2023i2,
    title={I2-SDF: Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs},
    author={Zhu, Jingsen and Huo, Yuchi and Ye, Qi and Luan, Fujun and Li, Jifan and Xi, Dianbing and Wang, Lisha and Tang, Rui and Hua, Wei and Bao, Hujun and others},
    booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages={12489--12498},
    year={2023}
}
 

Thanks to Nerfies for their excellent website templates.

## Metadata

```json
{
  "title": "Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs",
  "description": "Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs",
  "url": "https://jingsenzhu.github.io/i2-sdf/",
  "content": "More Research\nI2-SDF: Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs\nJingsen Zhu1, Yuchi Huo2,1, Qi Ye3,6, Fujun Luan4, Jifan Li1, Dianbing Xi1, Lisha Wang1, Rui Tang5, Wei Hua2, Hujun Bao1, Rui Wang1\n1State Key Lab of CAD&CG, Zhejiang University, 2Zhejiang Lab, 3Zhejiang University, 4Adobe Research, 5KooLab, Manycore 6Key Lab of CS&AUS of Zhejiang Province\nCVPR 2023\nPaper\n \narXiv\n \nCode\n \nData\nTL;DR: I2-SDF resolves challenges in reconstructing small objects inside an indoor scene by a novel bubble loss (Left), and leverages intrinsic decomposition and raytracing to enable photorealistic scene editing and relighting (Right).\nAbstract\nIn this work, we present I2-SDF, a new method for intrinsic indoor scene reconstruction and editing using differentiable Monte Carlo raytracing on neural signed distance fields (SDFs). Our holistic neural SDF-based framework jointly recovers the underlying shapes, incident radiance and materials from multi-view images. We introduce a novel bubble loss for fine-grained small objects and error-guided adaptive sampling scheme to largely improve the reconstruction quality on large-scale indoor scenes. Further, we propose to decompose the neural radiance field into spatially-varying material of the scene as a neural field through surface-based, differentiable Monte Carlo raytracing and emitter semantic segmentations, which enables physically based and photorealistic scene relighting and editing applications. Through a number of qualitative and quantitative experiments, we demonstrate the superior quality of our method on indoor scene reconstruction, novel view synthesis, and scene editing compared to state-of-the-art baselines.\n\nI2-Dataset: Synthetic Indoor Multiview Dataset\n\t\t\n\t\t\n\nWe provide a synthetic indoor dataset of well-designed scenes, with ground truth poses, geometry and material annotations.\nGeometry Reconstruction\n\nWe analyze the vanishing gradient problem of SDF-based volume rendering techniques, which results in failures of existing methods to reconstruct off-surface small objects. We propose a novel bubble loss to tackle this.\nNovel View Synthesis\n\nOur method outperforms previous methods in novel view synthesis of indoor scenes. Previous methods suffers from either reconstruction failure or overfitting.\nEditing and Relighting\n\nWe disentangle material (physically-based BRDF) and lighting (direct emission and indirect illumination) to enable photorealistic scene editing and relighting using Monte-Carlo raytracing.\nBibTeX\n@inproceedings{zhu2023i2,\n    title={I2-SDF: Intrinsic Indoor Scene Reconstruction and Editing via Raytracing in Neural SDFs},\n    author={Zhu, Jingsen and Huo, Yuchi and Ye, Qi and Luan, Fujun and Li, Jifan and Xi, Dianbing and Wang, Lisha and Tang, Rui and Hua, Wei and Bao, Hujun and others},\n    booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n    pages={12489--12498},\n    year={2023}\n}\n \n\nThanks to Nerfies for their excellent website templates.",
  "usage": {
    "tokens": 707
  }
}
```
