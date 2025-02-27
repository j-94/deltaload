---
title: A Data-Driven Volumetric Prior for Few-shot Ultra High-resolution Face Synthesis
description: Preface: A Data-driven Volumetric Prior for Few-shot Ultra High-resolution
        Face Synthesis
url: https://syntec-research.github.io/Preface/
timestamp: 2025-01-20T15:45:26.581Z
domain: syntec-research.github.io
path: Preface
---

# A Data-Driven Volumetric Prior for Few-shot Ultra High-resolution Face Synthesis


Preface: A Data-driven Volumetric Prior for Few-shot Ultra High-resolution
        Face Synthesis


## Content

[Kripasindhu Sarkar](https://krips89.github.io/profile_page/)2, [Tanmay Shah](https://scholar.google.com/citations?user=USYxdJ4AAAAJ&hl=en&oi=ao)2, [Gengyan Li](https://ait.ethz.ch/people/lig)1,2, [Daoye Wang](https://scholar.google.com/citations?user=pe5XLTEAAAAJ&hl=en)2, [Leonhard Helminger](https://scholar.google.com/citations?user=mTTsIr4AAAAJ&hl=en)2, [Sergio Orts-Escolano](https://scholar.google.com/citations?user=dznX1DMAAAAJ&hl=es)2, [Dmitry Lagun](https://scholar.google.com/citations?user=sY8lt7AAAAAJ&hl=en)2, [Otmar Hilliges](https://ait.ethz.ch/people/hilliges)1, [Thabo Beeler](https://thabobeeler.com/)2, [Abhimitra Meka](https://www.meka.page/)2

1ETH Zurich, 2Google

\-

  

Abstract
--------

NeRFs have enabled highly realistic synthesis of human faces including complex appearance and reflectance effects of hair and skin. These methods typically require a large number of multi-view input images, making the process hardware intensive and cumbersome, limiting applicability to unconstrained settings. We propose a novel volumetric human face prior that enables the synthesis of ultra high-resolution novel views of subjects that are not part of the prior's training distribution. This prior model consists of an identity-conditioned NeRF, trained on a dataset of low-resolution multi-view images of diverse humans with known camera calibration. A simple sparse landmark-based 3D alignment of the training dataset allows our model to learn a smooth latent space of geometry and appearance despite a limited number of training identities. A high-quality volumetric representation of a novel subject can be obtained by model fitting to 2 or 3 camera views of arbitrary resolution. Importantly, our method requires as few as two views of casually captured images as input at inference time.

_We recommend using Chrome to correctly display the videos. If a video doesn't play automatically, click the play button._

_Please note that we can only show limited high-resolution video results on this website. Please download the extended website for more results._

* * *

Ultra High-resolution Synthesis from Studio Captures
----------------------------------------------------

Given 3 views of a held-out test subject from our dataset, we show high-quality novel view synthesis. Note the 3D consistent rendering of details such as hair strands, eye-lashes, and view-dependent effects for example on the forehead.

#### Input Views (4Kx6K)

#### Novel View Synthesis - cropped to center

#### Novel View Synthesis (2Kx2K)

* * *

High-resolution Synthesis on FaceScape Dataset
----------------------------------------------

We show novel view synthesis results at 2K resolution using only two input views of subjects from the FaceScape dataset. Note that our prior model was trained on a different dataset—these results represent the out-of-distribution setting.

#### Input Views

![Image 35](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/344_01_05.jpg)

![Image 36](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/344_01_22.jpg)

#### Novel View Synthesis

  

* * *

In-the-wild Captures
--------------------

We demonstrate the generalization capability of our method to in-the-wild mobile camera captures. With just 2 input views, our method is able to genenerate highly consistent and photorealistic free-view renders of a subject. Our method not only reconstructs coherent geometry, it also learns to interpolate view-dependent specularities, such as on the hair and skin.

#### Input Views

![Image 37](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_01_cam00.jpg)

![Image 38](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_01_cam01.jpg)

#### Novel View Synthesis

#### Input Views

![Image 39](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_03_cam01.jpg)

![Image 40](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_03_cam00.jpg)

#### Novel View Synthesis

  

* * *

Method
------

We show that with a good initialization, a NeRF can be fine-tuned given only a few images. Our key idea is to train a “prior model” on a large collection of low-resolution, multiview images. The prior model learns a smooth latent space over face geometry and appearance that can be finetuned to ultra-high resolutions. Our approach generalises to images captured in-the-wild using a mobile camera.

![Image 41](https://files.ait.ethz.ch/projects/preface/web/static/images/overview.jpg)

  

* * *

Prior Model Latent Space
------------------------

Alignment of faces in our dataset allows us to learn a continuous latent space, where the embeddings of training identities can be interpolated to achieve plausible intermediate identities. Note that we do not train our model in an adversarial manner but only with reconstruction losses.

#### Random Sampling

#### Interpolation

  

* * *

Geometry
--------

We visualise the image-space geometry estimated by our method. Note the 3D consistent depth and normals. The normals in the hair have a grey appearance due to transparent density.

#### Input Views

![Image 42](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/934_gt_009_256x256.jpg)

![Image 43](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/934_gt_003_256x256.jpg)

#### Colour

#### Depth

#### Normals

#### Foreground Matte

  

* * *

Comparison with Related Works
-----------------------------

We compare with related works at 1K resolution given two input views.

#### Input Views

![Image 44](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/036_gt_009.jpg)

![Image 45](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/036_gt_003.jpg)

#### Ours

_\*We made a considerable effort to train KeypointNeRF at 1K resolution, but we found that their results at the resolution 256x256 is of much higher quality than their results at 1K. Therefore, the video presents their results at 256x256 resolution._

  

* * *

Limitations
-----------

While our method achieves state-of-the-art results in high-resolution synthesis of faces, it struggles with strong expressions and large accessories. This is due to limited representation in our training dataset. The training dataset only contains neutral faces and none of the subjects was wearing voluminous clothing like sweaters or jackets. This limitation could potentially be mitigated by training a more diverse prior model that includes those modalities.

### Grin

#### Input Views

![Image 46](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/122_16_47.jpg)

![Image 47](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/122_16_43.jpg)

#### Novel View Synthesis

### Cap and Eyeglasses

#### Input Views

![Image 48](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/282_cam00.jpg)

![Image 49](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/282_cam01.jpg)

#### Novel View Synthesis

  

* * *

If you find this work useful, please consider citing:

@inproceedings{buhler2023preface,
  title={Preface: A Data-driven Volumetric Prior for Few-shot Ultra High-resolution Face Synthesis},
  author={B{\\"u}hler, Marcel C and Sarkar, Kripasindhu and Shah, Tanmay and Li, Gengyan and Wang, Daoye and Helminger, Leonhard and Orts-Escolano, Sergio and Lagun, Dmitry and Hilliges, Otmar and Beeler, Thabo and others},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={3402--3413},
  year={2023}
}

* * *

## Metadata

```json
{
  "title": "A Data-Driven Volumetric Prior for Few-shot Ultra High-resolution Face Synthesis",
  "description": "Preface: A Data-driven Volumetric Prior for Few-shot Ultra High-resolution\n        Face Synthesis",
  "url": "https://syntec-research.github.io/Preface/",
  "content": "[Kripasindhu Sarkar](https://krips89.github.io/profile_page/)2, [Tanmay Shah](https://scholar.google.com/citations?user=USYxdJ4AAAAJ&hl=en&oi=ao)2, [Gengyan Li](https://ait.ethz.ch/people/lig)1,2, [Daoye Wang](https://scholar.google.com/citations?user=pe5XLTEAAAAJ&hl=en)2, [Leonhard Helminger](https://scholar.google.com/citations?user=mTTsIr4AAAAJ&hl=en)2, [Sergio Orts-Escolano](https://scholar.google.com/citations?user=dznX1DMAAAAJ&hl=es)2, [Dmitry Lagun](https://scholar.google.com/citations?user=sY8lt7AAAAAJ&hl=en)2, [Otmar Hilliges](https://ait.ethz.ch/people/hilliges)1, [Thabo Beeler](https://thabobeeler.com/)2, [Abhimitra Meka](https://www.meka.page/)2\n\n1ETH Zurich, 2Google\n\n\\-\n\n  \n\nAbstract\n--------\n\nNeRFs have enabled highly realistic synthesis of human faces including complex appearance and reflectance effects of hair and skin. These methods typically require a large number of multi-view input images, making the process hardware intensive and cumbersome, limiting applicability to unconstrained settings. We propose a novel volumetric human face prior that enables the synthesis of ultra high-resolution novel views of subjects that are not part of the prior's training distribution. This prior model consists of an identity-conditioned NeRF, trained on a dataset of low-resolution multi-view images of diverse humans with known camera calibration. A simple sparse landmark-based 3D alignment of the training dataset allows our model to learn a smooth latent space of geometry and appearance despite a limited number of training identities. A high-quality volumetric representation of a novel subject can be obtained by model fitting to 2 or 3 camera views of arbitrary resolution. Importantly, our method requires as few as two views of casually captured images as input at inference time.\n\n_We recommend using Chrome to correctly display the videos. If a video doesn't play automatically, click the play button._\n\n_Please note that we can only show limited high-resolution video results on this website. Please download the extended website for more results._\n\n* * *\n\nUltra High-resolution Synthesis from Studio Captures\n----------------------------------------------------\n\nGiven 3 views of a held-out test subject from our dataset, we show high-quality novel view synthesis. Note the 3D consistent rendering of details such as hair strands, eye-lashes, and view-dependent effects for example on the forehead.\n\n#### Input Views (4Kx6K)\n\n#### Novel View Synthesis - cropped to center\n\n#### Novel View Synthesis (2Kx2K)\n\n* * *\n\nHigh-resolution Synthesis on FaceScape Dataset\n----------------------------------------------\n\nWe show novel view synthesis results at 2K resolution using only two input views of subjects from the FaceScape dataset. Note that our prior model was trained on a different dataset—these results represent the out-of-distribution setting.\n\n#### Input Views\n\n![Image 35](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/344_01_05.jpg)\n\n![Image 36](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/344_01_22.jpg)\n\n#### Novel View Synthesis\n\n  \n\n* * *\n\nIn-the-wild Captures\n--------------------\n\nWe demonstrate the generalization capability of our method to in-the-wild mobile camera captures. With just 2 input views, our method is able to genenerate highly consistent and photorealistic free-view renders of a subject. Our method not only reconstructs coherent geometry, it also learns to interpolate view-dependent specularities, such as on the hair and skin.\n\n#### Input Views\n\n![Image 37](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_01_cam00.jpg)\n\n![Image 38](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_01_cam01.jpg)\n\n#### Novel View Synthesis\n\n#### Input Views\n\n![Image 39](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_03_cam01.jpg)\n\n![Image 40](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/inthewild_03_cam00.jpg)\n\n#### Novel View Synthesis\n\n  \n\n* * *\n\nMethod\n------\n\nWe show that with a good initialization, a NeRF can be fine-tuned given only a few images. Our key idea is to train a “prior model” on a large collection of low-resolution, multiview images. The prior model learns a smooth latent space over face geometry and appearance that can be finetuned to ultra-high resolutions. Our approach generalises to images captured in-the-wild using a mobile camera.\n\n![Image 41](https://files.ait.ethz.ch/projects/preface/web/static/images/overview.jpg)\n\n  \n\n* * *\n\nPrior Model Latent Space\n------------------------\n\nAlignment of faces in our dataset allows us to learn a continuous latent space, where the embeddings of training identities can be interpolated to achieve plausible intermediate identities. Note that we do not train our model in an adversarial manner but only with reconstruction losses.\n\n#### Random Sampling\n\n#### Interpolation\n\n  \n\n* * *\n\nGeometry\n--------\n\nWe visualise the image-space geometry estimated by our method. Note the 3D consistent depth and normals. The normals in the hair have a grey appearance due to transparent density.\n\n#### Input Views\n\n![Image 42](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/934_gt_009_256x256.jpg)\n\n![Image 43](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/934_gt_003_256x256.jpg)\n\n#### Colour\n\n#### Depth\n\n#### Normals\n\n#### Foreground Matte\n\n  \n\n* * *\n\nComparison with Related Works\n-----------------------------\n\nWe compare with related works at 1K resolution given two input views.\n\n#### Input Views\n\n![Image 44](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/036_gt_009.jpg)\n\n![Image 45](https://files.ait.ethz.ch/projects/preface/web/static/images/studio/036_gt_003.jpg)\n\n#### Ours\n\n_\\*We made a considerable effort to train KeypointNeRF at 1K resolution, but we found that their results at the resolution 256x256 is of much higher quality than their results at 1K. Therefore, the video presents their results at 256x256 resolution._\n\n  \n\n* * *\n\nLimitations\n-----------\n\nWhile our method achieves state-of-the-art results in high-resolution synthesis of faces, it struggles with strong expressions and large accessories. This is due to limited representation in our training dataset. The training dataset only contains neutral faces and none of the subjects was wearing voluminous clothing like sweaters or jackets. This limitation could potentially be mitigated by training a more diverse prior model that includes those modalities.\n\n### Grin\n\n#### Input Views\n\n![Image 46](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/122_16_47.jpg)\n\n![Image 47](https://files.ait.ethz.ch/projects/preface/web/static/images/facescape/122_16_43.jpg)\n\n#### Novel View Synthesis\n\n### Cap and Eyeglasses\n\n#### Input Views\n\n![Image 48](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/282_cam00.jpg)\n\n![Image 49](https://files.ait.ethz.ch/projects/preface/web/static/images/inthewild/282_cam01.jpg)\n\n#### Novel View Synthesis\n\n  \n\n* * *\n\nIf you find this work useful, please consider citing:\n\n@inproceedings{buhler2023preface,\n  title={Preface: A Data-driven Volumetric Prior for Few-shot Ultra High-resolution Face Synthesis},\n  author={B{\\\\\"u}hler, Marcel C and Sarkar, Kripasindhu and Shah, Tanmay and Li, Gengyan and Wang, Daoye and Helminger, Leonhard and Orts-Escolano, Sergio and Lagun, Dmitry and Hilliges, Otmar and Beeler, Thabo and others},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages={3402--3413},\n  year={2023}\n}\n\n* * *",
  "usage": {
    "tokens": 1840
  }
}
```
