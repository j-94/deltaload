---
title: GitHub - MarkMoHR/Awesome-Edge-Detection-Papers: :books: A collection of edge/contour/boundary detection papers and toolbox.
description: :books: A collection of edge/contour/boundary detection papers and toolbox. - MarkMoHR/Awesome-Edge-Detection-Papers
url: https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers
timestamp: 2025-01-20T15:31:05.816Z
domain: github.com
path: MarkMoHR_Awesome-Edge-Detection-Papers
---

# GitHub - MarkMoHR/Awesome-Edge-Detection-Papers: :books: A collection of edge/contour/boundary detection papers and toolbox.


:books: A collection of edge/contour/boundary detection papers and toolbox. - MarkMoHR/Awesome-Edge-Detection-Papers


## Content

Awesome-Edge-Detection-Papers
-----------------------------

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#awesome-edge-detection-papers)

[![Image 9: Awesome](https://camo.githubusercontent.com/8693bde04030b1670d5097703441005eba34240c32d1df1eb82a5f0d6716518e/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667)](https://github.com/sindresorhus/awesome)

A collection of edge detection papers and corresponding source code/demo program (_a.k.a._ contour detection or boundary detection).

> Feel free to create a PR or an issue. (Pull Request is preferred)

[![Image 10: examples](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers/raw/master/edge-detection.png)](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers/blob/master/edge-detection.png)

**Outline**

*   [Edge detection related dataset](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#0-edge-detection-related-dataset)
*   [Deep-learning based approaches](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#1-deep-learning-based-approaches)
    *   [General edge detection](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#11-general-edge-detection)
    *   [Object contour detection](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#12-object-contour-detection)
    *   [Semantic edge detection (Category-Aware)](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#13-semantic-edge-detection-category-aware)
    *   [Occlusion boundary detection](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#14-occlusion-boundary-detection)
    *   [Edge detection from multi-frames](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#15-edge-detection-from-multi-frames)
*   [Traditional approaches](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#2-traditional-approaches)
*   [\[Misc\] Useful Links](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#3-useful-links)

0\. Edge detection related dataset
----------------------------------

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#0-edge-detection-related-dataset)

| Short name | Source Paper | Source | Introduction |
| --- | --- | --- | --- |
| [BSDS500](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html) | [Contour Detection and Hierarchical Image Segmentation](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/papers/amfm_pami2010.pdf) | TPAMI 2011 | Classical edge detaction dataset. |
| [NYUDv2](https://github.com/s-gupta/rgbd#notes) | [Perceptual Organization and Recognition of Indoor Scenes from RGB-D Images](https://www.cv-foundation.org/openaccess/content_cvpr_2013/papers/Gupta_Perceptual_Organization_and_2013_CVPR_paper.pdf) | CVPR 2013 | Edges come from the boundary of annotated segmentation mask. |
| [Multi-cue](https://serre-lab.clps.brown.edu/resource/multicue/) | [A systematic comparison between visual cues for boundary detection](https://pubmed.ncbi.nlm.nih.gov/26748113/) | Vision research 2016 | With boundary annotations. |
| [Wireframe](https://github.com/cherubicxn/hawp#data-preparation) | [Holistically-Attracted Wireframe Parsing](https://arxiv.org/pdf/2003.01663) | CVPR 2020 | Edges come from the annotated wireframe. |

* * *

1\. Deep-learning based approaches
----------------------------------

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#1-deep-learning-based-approaches)

### 1.1 General edge detection

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#11-general-edge-detection)

| Short name | Paper | Source | Code/Project Link |
| --- | --- | --- | --- |
| SAUGE | [SAUGE: Taming SAM for Uncertainty-Aligned Multi-Granularity Edge Detection](https://arxiv.org/abs/2412.12892) | AAAI 2025 | [\[code\]](https://github.com/Star-xing1/SAUGE) |
| RankED | [RankED: Addressing Imbalance and Uncertainty in Edge Detection Using Ranking-based Losses](https://openaccess.thecvf.com/content/CVPR2024/papers/Cetinkaya_RankED_Addressing_Imbalance_and_Uncertainty_in_Edge_Detection_Using_Ranking-based_CVPR_2024_paper.pdf) | CVPR 2024 | [\[webpage\]](https://ranked-cvpr24.github.io/) |
| MuGE | [MuGE: Multiple Granularity Edge Detection](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_MuGE_Multiple_Granularity_Edge_Detection_CVPR_2024_paper.pdf) | CVPR 2024 |  |
| DiffusionEdge | [DiffusionEdge: Diffusion Probabilistic Model for Crisp Edge Detection](https://arxiv.org/abs/2401.02032) | AAAI 2024 | [\[Code\]](https://github.com/GuHuangAI/DiffusionEdge) |
| UAED | [The Treasure Beneath Multiple Annotations: An Uncertainty-aware Edge Detector](https://arxiv.org/abs/2303.11828) | CVPR 2023 | [\[Code\]](https://github.com/ZhouCX117/UAED) |
| EDTER | [EDTER: Edge Detection with Transformer](https://openaccess.thecvf.com/content/CVPR2022/papers/Pu_EDTER_Edge_Detection_With_Transformer_CVPR_2022_paper.pdf) | CVPR 2022 | [\[Code\]](https://github.com/MengyangPu/EDTER) |
| pidinet | [Pixel Difference Networks for Efficient Edge Detection](https://arxiv.org/abs/2108.07009) | ICCV 2021 | [\[Code\]](https://github.com/zhuoinoulu/pidinet) |
| DSCD | [Deep Structural Contour Detection](https://dl.acm.org/doi/abs/10.1145/3394171.3413750) | ACM MM 2020 |  |
| DexiNed | [Dense Extreme Inception Network: Towards a Robust CNN Model for Edge Detection](https://arxiv.org/pdf/1909.01955.pdf) | WACV 2020 | [\[Code\]](https://github.com/xavysp/DexiNed) |
| BDCN | [Bi-Directional Cascade Network for Perceptual Edge Detection](https://arxiv.org/pdf/1902.10903.pdf) | CVPR 2019 | [\[code\]](https://github.com/pkuCactus/BDCN) |
| RCN | [Object Contour and Edge Detection with RefineContourNet](https://link.springer.com/chapter/10.1007%2F978-3-030-29888-3_20) | CAIP 2019 | [\[code\]](https://github.com/AndreKelm/RefineContourNet) |
| LPCB | [Learning to Predict Crisp Boundaries](http://openaccess.thecvf.com/content_ECCV_2018/papers/Ruoxi_Deng_Learning_to_Predict_ECCV_2018_paper.pdf) | ECCV 2018 |  |
| AMH-Net | [Learning Deep Structured Multi-Scale Features using Attention-Gated CRFs for Contour Prediction](https://papers.nips.cc/paper/6985-learning-deep-structured-multi-scale-features-using-attention-gated-crfs-for-contour-prediction.pdf) | NIPS 2017 | [\[code\]](https://github.com/danxuhk/AttentionGatedMulti-ScaleFeatureLearning) |
| RCF | [Richer Convolutional Features for Edge Detection](http://openaccess.thecvf.com/content_cvpr_2017/papers/Liu_Richer_Convolutional_Features_CVPR_2017_paper.pdf) | CVPR 2017 | [\[code-caffe\]](https://github.com/yun-liu/rcf) [\[code-pytorch\]](https://github.com/meteorshowers/RCF-pytorch) [\[project\]](https://mmcheng.net/zh/rcfEdge/) |
| CED | [Deep Crisp Boundaries](http://openaccess.thecvf.com/content_cvpr_2017/papers/Wang_Deep_Crisp_Boundaries_CVPR_2017_paper.pdf) | CVPR 2017 | [\[code\]](https://github.com/Wangyupei/CED) |
| COB | [Convolutional Oriented Boundaries](https://arxiv.org/pdf/1608.02755.pdf) | ECCV 2016 | [\[code\]](https://github.com/kmaninis/COB) [\[project\]](http://www.vision.ee.ethz.ch/~cvlsegmentation/cob/index.html) |
| RDS | [Learning Relaxed Deep Supervision for Better Edge Detection](http://openaccess.thecvf.com/content_cvpr_2016/papers/Liu_Learning_Relaxed_Deep_CVPR_2016_paper.pdf) | CVPR 2016 |  |
| HFL | [High-for-Low and Low-for-High: Efficient Boundary Detection from Deep Object Features and its Applications to High-Level Vision](http://openaccess.thecvf.com/content_iccv_2015/papers/Bertasius_High-for-Low_and_Low-for-High_ICCV_2015_paper.pdf) | ICCV 2015 |  |
| HED | [Holistically-Nested Edge Detection](http://openaccess.thecvf.com/content_iccv_2015/papers/Xie_Holistically-Nested_Edge_Detection_ICCV_2015_paper.pdf) | ICCV 2015 | [\[code\]](https://github.com/s9xie/hed) |
| DeepEdge | [DeepEdge: A Multi-Scale Bifurcated Deep Network for Top-Down Contour Detection](http://openaccess.thecvf.com/content_cvpr_2015/papers/Bertasius_DeepEdge_A_Multi-Scale_2015_CVPR_paper.pdf) | CVPR 2015 |  |
| DeepContour | [DeepContour: A Deep Convolutional Feature Learned by Positive-sharing Loss for Contour Detection](http://openaccess.thecvf.com/content_cvpr_2015/papers/Shen_DeepContour_A_Deep_2015_CVPR_paper.pdf) | CVPR 2015 | [\[code\]](https://github.com/shenwei1231/DeepContour) |

### 1.2 Object contour detection

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#12-object-contour-detection)

| Short name | Paper | Source | Code/Project Link |
| --- | --- | --- | --- |
| CEDN | [Object Contour Detection with a Fully Convolutional Encoder-Decoder Network](http://openaccess.thecvf.com/content_cvpr_2016/papers/Yang_Object_Contour_Detection_CVPR_2016_paper.pdf) | CVPR 2016 | [\[code-caffe\]](https://github.com/jimeiyang/objectContourDetector) [\[code-TF\]](https://github.com/Raj-08/tensorflow-object-contour-detection) |
|  | [Weakly Supervised Object Boundaries](http://openaccess.thecvf.com/content_cvpr_2016/papers/Khoreva_Weakly_Supervised_Object_CVPR_2016_paper.pdf) | CVPR 2016 |  |

### 1.3 Semantic edge detection (Category-Aware)

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#13-semantic-edge-detection-category-aware)

| Short name | Paper | Source | Code/Project Link |
| --- | --- | --- | --- |
| RINDNet | [RINDNet: Edge Detection for Discontinuity in Reflectance, Illumination, Normal and Depth](https://arxiv.org/abs/2108.00616) | ICCV 2021 | [\[code\]](https://github.com/MengyangPu/RINDNet) |
| RPCNet | [Joint Semantic Segmentation and Boundary Detection using Iterative Pyramid Contexts](http://openaccess.thecvf.com/content_CVPR_2020/papers/Zhen_Joint_Semantic_Segmentation_and_Boundary_Detection_Using_Iterative_Pyramid_Contexts_CVPR_2020_paper.pdf) | CVPR 2020 | [\[code\]](https://github.com/mingminzhen/RPCNet) |
| DFF | [Dynamic Feature Fusion for Semantic Edge Detection](https://arxiv.org/pdf/1902.09104.pdf) | IJCAI 2019 | [\[code\]](https://github.com/Lavender105/DFF) |
| STEAL | [Devil is in the Edges: Learning Semantic Boundaries from Noisy Annotations](https://arxiv.org/pdf/1904.07934.pdf) | CVPR 2019 | [\[code\]](https://github.com/nv-tlabs/STEAL) [\[project\]](https://nv-tlabs.github.io/STEAL/) |
| SEAL | [Simultaneous Edge Alignment and Learning](http://openaccess.thecvf.com/content_ECCV_2018/papers/Zhiding_Yu_SEAL_A_Framework_ECCV_2018_paper.pdf) | ECCV 2018 | [\[code\]](https://github.com/Chrisding/seal) |
| CASENet | [CASENet: Deep Category-Aware Semantic Edge Detection](http://openaccess.thecvf.com/content_cvpr_2017/papers/Yu_CASENet_Deep_Category-Aware_CVPR_2017_paper.pdf) | CVPR 2017 | [\[code\]](http://www.merl.com/research/license#CASENet) |
| `dataset` | [Semantic Contours from Inverse Detectors](https://www.robots.ox.ac.uk/~vgg/rg/papers/BharathICCV2011.pdf) | ICCV 2011 | [\[code\]](https://github.com/bharath272/semantic_contours) |

### 1.4 Occlusion boundary detection

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#14-occlusion-boundary-detection)

| Short name | Paper | Source | Code/Project Link |
| --- | --- | --- | --- |
| DOOBNet | [DOOBNet: Deep Object Occlusion Boundary Detection from an Image](https://arxiv.org/abs/1806.03772) | ACCV 2018 | [\[code\]](https://github.com/GuoxiaWang/DOOBNet) |
| DOC & `dataset` | [DOC: Deep OCclusion Estimation From a Single Image](https://arxiv.org/abs/1511.06457) | ECCV 2016 | [\[code\]](https://github.com/pengwangucla/DOC) |
|  | [Occlusion Boundary Detection via Deep Exploration of Context](http://openaccess.thecvf.com/content_cvpr_2016/papers/Fu_Occlusion_Boundary_Detection_CVPR_2016_paper.pdf) | CVPR 2016 |  |

### 1.5 Edge detection from multi-frames

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#15-edge-detection-from-multi-frames)

| Short name | Paper | Source | Code/Project Link |
| --- | --- | --- | --- |
| Boundary Flow | [Boundary Flow: A Siamese Network that Predicts Boundary Motion without Training on Motion](http://openaccess.thecvf.com/content_cvpr_2018/papers/Lei_Boundary_Flow_A_CVPR_2018_paper.pdf) | CVPR 2018 |  |
| LEGO | [LEGO: Learning Edge with Geometry all at Once by Watching Videos](http://openaccess.thecvf.com/content_cvpr_2018/papers/Yang_LEGO_Learning_Edge_CVPR_2018_paper.pdf) | CVPR 2018 | [\[code\]](https://github.com/zhenheny/LEGO) |
|  | [Unsupervised Learning of Edges](http://openaccess.thecvf.com/content_cvpr_2016/papers/Li_Unsupervised_Learning_of_CVPR_2016_paper.pdf) | CVPR 2016 | [\[code\]](https://github.com/happyharrycn/unsupervised_edges) |

* * *

2\. Traditional approaches
--------------------------

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#2-traditional-approaches)

| Short name | Paper | Source | Code/Project Link |
| --- | --- | --- | --- |
| SemiContour | [SemiContour: A Semi-supervised Learning Approach for Contour Detection](http://openaccess.thecvf.com/content_cvpr_2016/papers/Zhang_SemiContour_A_Semi-Supervised_CVPR_2016_paper.pdf) | CVPR 2016 |  |
| OEF | [Oriented Edge Forests for Boundary Detection](http://openaccess.thecvf.com/content_cvpr_2015/papers/Hallman_Oriented_Edge_Forests_2015_CVPR_paper.pdf) | CVPR 2015 | [\[code\]](https://github.com/samhallman/oef) |
| SE | [Fast edge detection using structured forests](https://arxiv.org/pdf/1406.5549.pdf) | TPAMI 2015 | [\[code\]](https://github.com/pdollar/edges) |
| Edge Boxes | [Edge Boxes: Locating Object Proposals from Edges](https://www.microsoft.com/en-us/research/wp-content/uploads/2014/09/ZitnickDollarECCV14edgeBoxes.pdf) | ECCV 2014 | [\[code\]](https://github.com/pdollar/edges) |
| PMI | [Crisp Boundary Detection Using Pointwise Mutual Information](https://link.springer.com/chapter/10.1007/978-3-319-10578-9_52) | ECCV 2014 | [\[code\]](https://github.com/phillipi/crisp-boundaries) |
| Sketch Tokens | [Sketch tokens: A learned mid-level representation for contour and object detection](http://openaccess.thecvf.com/content_cvpr_2013/papers/Lim_Sketch_Tokens_A_2013_CVPR_paper.pdf) | CVPR 2013 |  |
| SCG | [Discriminatively Trained Sparse Code Gradients for Contour Detection](http://papers.nips.cc/paper/4787-discriminatively-trained-sparse-code-gradients-for-contour-detection.pdf) | NIPS 2012 |  |
| gPb-owt-ucm | [Contour Detection and Hierarchical Image Segmentation](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.374.3367&rep=rep1&type=pdf) | TPAMI 2011 | [\[code\]](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_source.tgz) [\[project\]](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html) |
| XDoG | [XDoG: advanced image stylization with eXtended Difference-of-Gaussians](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.648.990&rep=rep1&type=pdf) | NPAR 2011 | [\[code(python)\]](https://github.com/heitorrapela/xdog)  
[\[online demo\]](https://xdog.alexpeattie.com/)  
Others: [code(C++)](https://github.com/Sunwinds/xdog-demo) [code(matlab)](https://github.com/CemalUnal/XDoG-Filter) [code(Web APP)](https://github.com/alexpeattie/xdog-sketch) |
| FDoG | [Coherent Line Drawing](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.559&rep=rep1&type=pdf) | NPAR 2007 | [\[code\]](https://github.com/SSARCandy/Coherent-Line-Drawing) [\[project\]](https://ssarcandy.tw/Coherent-Line-Drawing/) |
| Canny | [A Computational Approach to Edge Detection](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf) | TPAMI 1986 | [\[code\]](https://rosettacode.org/wiki/Canny_edge_detector) [\[code-py\]](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html) |

* * *

3\. Useful Links
----------------

[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#3-useful-links)

*   Code to plot edge PR curves: [MCG-NKU/plot-edge-pr-curves](https://github.com/MCG-NKU/plot-edge-pr-curves)

## Metadata

```json
{
  "title": "GitHub - MarkMoHR/Awesome-Edge-Detection-Papers: :books: A collection of edge/contour/boundary detection papers and toolbox.",
  "description": ":books: A collection of edge/contour/boundary detection papers and toolbox. - MarkMoHR/Awesome-Edge-Detection-Papers",
  "url": "https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true",
  "content": "Awesome-Edge-Detection-Papers\n-----------------------------\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#awesome-edge-detection-papers)\n\n[![Image 9: Awesome](https://camo.githubusercontent.com/8693bde04030b1670d5097703441005eba34240c32d1df1eb82a5f0d6716518e/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667)](https://github.com/sindresorhus/awesome)\n\nA collection of edge detection papers and corresponding source code/demo program (_a.k.a._ contour detection or boundary detection).\n\n> Feel free to create a PR or an issue. (Pull Request is preferred)\n\n[![Image 10: examples](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers/raw/master/edge-detection.png)](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers/blob/master/edge-detection.png)\n\n**Outline**\n\n*   [Edge detection related dataset](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#0-edge-detection-related-dataset)\n*   [Deep-learning based approaches](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#1-deep-learning-based-approaches)\n    *   [General edge detection](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#11-general-edge-detection)\n    *   [Object contour detection](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#12-object-contour-detection)\n    *   [Semantic edge detection (Category-Aware)](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#13-semantic-edge-detection-category-aware)\n    *   [Occlusion boundary detection](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#14-occlusion-boundary-detection)\n    *   [Edge detection from multi-frames](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#15-edge-detection-from-multi-frames)\n*   [Traditional approaches](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#2-traditional-approaches)\n*   [\\[Misc\\] Useful Links](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#3-useful-links)\n\n0\\. Edge detection related dataset\n----------------------------------\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#0-edge-detection-related-dataset)\n\n| Short name | Source Paper | Source | Introduction |\n| --- | --- | --- | --- |\n| [BSDS500](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html) | [Contour Detection and Hierarchical Image Segmentation](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/papers/amfm_pami2010.pdf) | TPAMI 2011 | Classical edge detaction dataset. |\n| [NYUDv2](https://github.com/s-gupta/rgbd#notes) | [Perceptual Organization and Recognition of Indoor Scenes from RGB-D Images](https://www.cv-foundation.org/openaccess/content_cvpr_2013/papers/Gupta_Perceptual_Organization_and_2013_CVPR_paper.pdf) | CVPR 2013 | Edges come from the boundary of annotated segmentation mask. |\n| [Multi-cue](https://serre-lab.clps.brown.edu/resource/multicue/) | [A systematic comparison between visual cues for boundary detection](https://pubmed.ncbi.nlm.nih.gov/26748113/) | Vision research 2016 | With boundary annotations. |\n| [Wireframe](https://github.com/cherubicxn/hawp#data-preparation) | [Holistically-Attracted Wireframe Parsing](https://arxiv.org/pdf/2003.01663) | CVPR 2020 | Edges come from the annotated wireframe. |\n\n* * *\n\n1\\. Deep-learning based approaches\n----------------------------------\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#1-deep-learning-based-approaches)\n\n### 1.1 General edge detection\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#11-general-edge-detection)\n\n| Short name | Paper | Source | Code/Project Link |\n| --- | --- | --- | --- |\n| SAUGE | [SAUGE: Taming SAM for Uncertainty-Aligned Multi-Granularity Edge Detection](https://arxiv.org/abs/2412.12892) | AAAI 2025 | [\\[code\\]](https://github.com/Star-xing1/SAUGE) |\n| RankED | [RankED: Addressing Imbalance and Uncertainty in Edge Detection Using Ranking-based Losses](https://openaccess.thecvf.com/content/CVPR2024/papers/Cetinkaya_RankED_Addressing_Imbalance_and_Uncertainty_in_Edge_Detection_Using_Ranking-based_CVPR_2024_paper.pdf) | CVPR 2024 | [\\[webpage\\]](https://ranked-cvpr24.github.io/) |\n| MuGE | [MuGE: Multiple Granularity Edge Detection](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_MuGE_Multiple_Granularity_Edge_Detection_CVPR_2024_paper.pdf) | CVPR 2024 |  |\n| DiffusionEdge | [DiffusionEdge: Diffusion Probabilistic Model for Crisp Edge Detection](https://arxiv.org/abs/2401.02032) | AAAI 2024 | [\\[Code\\]](https://github.com/GuHuangAI/DiffusionEdge) |\n| UAED | [The Treasure Beneath Multiple Annotations: An Uncertainty-aware Edge Detector](https://arxiv.org/abs/2303.11828) | CVPR 2023 | [\\[Code\\]](https://github.com/ZhouCX117/UAED) |\n| EDTER | [EDTER: Edge Detection with Transformer](https://openaccess.thecvf.com/content/CVPR2022/papers/Pu_EDTER_Edge_Detection_With_Transformer_CVPR_2022_paper.pdf) | CVPR 2022 | [\\[Code\\]](https://github.com/MengyangPu/EDTER) |\n| pidinet | [Pixel Difference Networks for Efficient Edge Detection](https://arxiv.org/abs/2108.07009) | ICCV 2021 | [\\[Code\\]](https://github.com/zhuoinoulu/pidinet) |\n| DSCD | [Deep Structural Contour Detection](https://dl.acm.org/doi/abs/10.1145/3394171.3413750) | ACM MM 2020 |  |\n| DexiNed | [Dense Extreme Inception Network: Towards a Robust CNN Model for Edge Detection](https://arxiv.org/pdf/1909.01955.pdf) | WACV 2020 | [\\[Code\\]](https://github.com/xavysp/DexiNed) |\n| BDCN | [Bi-Directional Cascade Network for Perceptual Edge Detection](https://arxiv.org/pdf/1902.10903.pdf) | CVPR 2019 | [\\[code\\]](https://github.com/pkuCactus/BDCN) |\n| RCN | [Object Contour and Edge Detection with RefineContourNet](https://link.springer.com/chapter/10.1007%2F978-3-030-29888-3_20) | CAIP 2019 | [\\[code\\]](https://github.com/AndreKelm/RefineContourNet) |\n| LPCB | [Learning to Predict Crisp Boundaries](http://openaccess.thecvf.com/content_ECCV_2018/papers/Ruoxi_Deng_Learning_to_Predict_ECCV_2018_paper.pdf) | ECCV 2018 |  |\n| AMH-Net | [Learning Deep Structured Multi-Scale Features using Attention-Gated CRFs for Contour Prediction](https://papers.nips.cc/paper/6985-learning-deep-structured-multi-scale-features-using-attention-gated-crfs-for-contour-prediction.pdf) | NIPS 2017 | [\\[code\\]](https://github.com/danxuhk/AttentionGatedMulti-ScaleFeatureLearning) |\n| RCF | [Richer Convolutional Features for Edge Detection](http://openaccess.thecvf.com/content_cvpr_2017/papers/Liu_Richer_Convolutional_Features_CVPR_2017_paper.pdf) | CVPR 2017 | [\\[code-caffe\\]](https://github.com/yun-liu/rcf) [\\[code-pytorch\\]](https://github.com/meteorshowers/RCF-pytorch) [\\[project\\]](https://mmcheng.net/zh/rcfEdge/) |\n| CED | [Deep Crisp Boundaries](http://openaccess.thecvf.com/content_cvpr_2017/papers/Wang_Deep_Crisp_Boundaries_CVPR_2017_paper.pdf) | CVPR 2017 | [\\[code\\]](https://github.com/Wangyupei/CED) |\n| COB | [Convolutional Oriented Boundaries](https://arxiv.org/pdf/1608.02755.pdf) | ECCV 2016 | [\\[code\\]](https://github.com/kmaninis/COB) [\\[project\\]](http://www.vision.ee.ethz.ch/~cvlsegmentation/cob/index.html) |\n| RDS | [Learning Relaxed Deep Supervision for Better Edge Detection](http://openaccess.thecvf.com/content_cvpr_2016/papers/Liu_Learning_Relaxed_Deep_CVPR_2016_paper.pdf) | CVPR 2016 |  |\n| HFL | [High-for-Low and Low-for-High: Efficient Boundary Detection from Deep Object Features and its Applications to High-Level Vision](http://openaccess.thecvf.com/content_iccv_2015/papers/Bertasius_High-for-Low_and_Low-for-High_ICCV_2015_paper.pdf) | ICCV 2015 |  |\n| HED | [Holistically-Nested Edge Detection](http://openaccess.thecvf.com/content_iccv_2015/papers/Xie_Holistically-Nested_Edge_Detection_ICCV_2015_paper.pdf) | ICCV 2015 | [\\[code\\]](https://github.com/s9xie/hed) |\n| DeepEdge | [DeepEdge: A Multi-Scale Bifurcated Deep Network for Top-Down Contour Detection](http://openaccess.thecvf.com/content_cvpr_2015/papers/Bertasius_DeepEdge_A_Multi-Scale_2015_CVPR_paper.pdf) | CVPR 2015 |  |\n| DeepContour | [DeepContour: A Deep Convolutional Feature Learned by Positive-sharing Loss for Contour Detection](http://openaccess.thecvf.com/content_cvpr_2015/papers/Shen_DeepContour_A_Deep_2015_CVPR_paper.pdf) | CVPR 2015 | [\\[code\\]](https://github.com/shenwei1231/DeepContour) |\n\n### 1.2 Object contour detection\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#12-object-contour-detection)\n\n| Short name | Paper | Source | Code/Project Link |\n| --- | --- | --- | --- |\n| CEDN | [Object Contour Detection with a Fully Convolutional Encoder-Decoder Network](http://openaccess.thecvf.com/content_cvpr_2016/papers/Yang_Object_Contour_Detection_CVPR_2016_paper.pdf) | CVPR 2016 | [\\[code-caffe\\]](https://github.com/jimeiyang/objectContourDetector) [\\[code-TF\\]](https://github.com/Raj-08/tensorflow-object-contour-detection) |\n|  | [Weakly Supervised Object Boundaries](http://openaccess.thecvf.com/content_cvpr_2016/papers/Khoreva_Weakly_Supervised_Object_CVPR_2016_paper.pdf) | CVPR 2016 |  |\n\n### 1.3 Semantic edge detection (Category-Aware)\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#13-semantic-edge-detection-category-aware)\n\n| Short name | Paper | Source | Code/Project Link |\n| --- | --- | --- | --- |\n| RINDNet | [RINDNet: Edge Detection for Discontinuity in Reflectance, Illumination, Normal and Depth](https://arxiv.org/abs/2108.00616) | ICCV 2021 | [\\[code\\]](https://github.com/MengyangPu/RINDNet) |\n| RPCNet | [Joint Semantic Segmentation and Boundary Detection using Iterative Pyramid Contexts](http://openaccess.thecvf.com/content_CVPR_2020/papers/Zhen_Joint_Semantic_Segmentation_and_Boundary_Detection_Using_Iterative_Pyramid_Contexts_CVPR_2020_paper.pdf) | CVPR 2020 | [\\[code\\]](https://github.com/mingminzhen/RPCNet) |\n| DFF | [Dynamic Feature Fusion for Semantic Edge Detection](https://arxiv.org/pdf/1902.09104.pdf) | IJCAI 2019 | [\\[code\\]](https://github.com/Lavender105/DFF) |\n| STEAL | [Devil is in the Edges: Learning Semantic Boundaries from Noisy Annotations](https://arxiv.org/pdf/1904.07934.pdf) | CVPR 2019 | [\\[code\\]](https://github.com/nv-tlabs/STEAL) [\\[project\\]](https://nv-tlabs.github.io/STEAL/) |\n| SEAL | [Simultaneous Edge Alignment and Learning](http://openaccess.thecvf.com/content_ECCV_2018/papers/Zhiding_Yu_SEAL_A_Framework_ECCV_2018_paper.pdf) | ECCV 2018 | [\\[code\\]](https://github.com/Chrisding/seal) |\n| CASENet | [CASENet: Deep Category-Aware Semantic Edge Detection](http://openaccess.thecvf.com/content_cvpr_2017/papers/Yu_CASENet_Deep_Category-Aware_CVPR_2017_paper.pdf) | CVPR 2017 | [\\[code\\]](http://www.merl.com/research/license#CASENet) |\n| `dataset` | [Semantic Contours from Inverse Detectors](https://www.robots.ox.ac.uk/~vgg/rg/papers/BharathICCV2011.pdf) | ICCV 2011 | [\\[code\\]](https://github.com/bharath272/semantic_contours) |\n\n### 1.4 Occlusion boundary detection\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#14-occlusion-boundary-detection)\n\n| Short name | Paper | Source | Code/Project Link |\n| --- | --- | --- | --- |\n| DOOBNet | [DOOBNet: Deep Object Occlusion Boundary Detection from an Image](https://arxiv.org/abs/1806.03772) | ACCV 2018 | [\\[code\\]](https://github.com/GuoxiaWang/DOOBNet) |\n| DOC & `dataset` | [DOC: Deep OCclusion Estimation From a Single Image](https://arxiv.org/abs/1511.06457) | ECCV 2016 | [\\[code\\]](https://github.com/pengwangucla/DOC) |\n|  | [Occlusion Boundary Detection via Deep Exploration of Context](http://openaccess.thecvf.com/content_cvpr_2016/papers/Fu_Occlusion_Boundary_Detection_CVPR_2016_paper.pdf) | CVPR 2016 |  |\n\n### 1.5 Edge detection from multi-frames\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#15-edge-detection-from-multi-frames)\n\n| Short name | Paper | Source | Code/Project Link |\n| --- | --- | --- | --- |\n| Boundary Flow | [Boundary Flow: A Siamese Network that Predicts Boundary Motion without Training on Motion](http://openaccess.thecvf.com/content_cvpr_2018/papers/Lei_Boundary_Flow_A_CVPR_2018_paper.pdf) | CVPR 2018 |  |\n| LEGO | [LEGO: Learning Edge with Geometry all at Once by Watching Videos](http://openaccess.thecvf.com/content_cvpr_2018/papers/Yang_LEGO_Learning_Edge_CVPR_2018_paper.pdf) | CVPR 2018 | [\\[code\\]](https://github.com/zhenheny/LEGO) |\n|  | [Unsupervised Learning of Edges](http://openaccess.thecvf.com/content_cvpr_2016/papers/Li_Unsupervised_Learning_of_CVPR_2016_paper.pdf) | CVPR 2016 | [\\[code\\]](https://github.com/happyharrycn/unsupervised_edges) |\n\n* * *\n\n2\\. Traditional approaches\n--------------------------\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#2-traditional-approaches)\n\n| Short name | Paper | Source | Code/Project Link |\n| --- | --- | --- | --- |\n| SemiContour | [SemiContour: A Semi-supervised Learning Approach for Contour Detection](http://openaccess.thecvf.com/content_cvpr_2016/papers/Zhang_SemiContour_A_Semi-Supervised_CVPR_2016_paper.pdf) | CVPR 2016 |  |\n| OEF | [Oriented Edge Forests for Boundary Detection](http://openaccess.thecvf.com/content_cvpr_2015/papers/Hallman_Oriented_Edge_Forests_2015_CVPR_paper.pdf) | CVPR 2015 | [\\[code\\]](https://github.com/samhallman/oef) |\n| SE | [Fast edge detection using structured forests](https://arxiv.org/pdf/1406.5549.pdf) | TPAMI 2015 | [\\[code\\]](https://github.com/pdollar/edges) |\n| Edge Boxes | [Edge Boxes: Locating Object Proposals from Edges](https://www.microsoft.com/en-us/research/wp-content/uploads/2014/09/ZitnickDollarECCV14edgeBoxes.pdf) | ECCV 2014 | [\\[code\\]](https://github.com/pdollar/edges) |\n| PMI | [Crisp Boundary Detection Using Pointwise Mutual Information](https://link.springer.com/chapter/10.1007/978-3-319-10578-9_52) | ECCV 2014 | [\\[code\\]](https://github.com/phillipi/crisp-boundaries) |\n| Sketch Tokens | [Sketch tokens: A learned mid-level representation for contour and object detection](http://openaccess.thecvf.com/content_cvpr_2013/papers/Lim_Sketch_Tokens_A_2013_CVPR_paper.pdf) | CVPR 2013 |  |\n| SCG | [Discriminatively Trained Sparse Code Gradients for Contour Detection](http://papers.nips.cc/paper/4787-discriminatively-trained-sparse-code-gradients-for-contour-detection.pdf) | NIPS 2012 |  |\n| gPb-owt-ucm | [Contour Detection and Hierarchical Image Segmentation](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.374.3367&rep=rep1&type=pdf) | TPAMI 2011 | [\\[code\\]](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_source.tgz) [\\[project\\]](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html) |\n| XDoG | [XDoG: advanced image stylization with eXtended Difference-of-Gaussians](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.648.990&rep=rep1&type=pdf) | NPAR 2011 | [\\[code(python)\\]](https://github.com/heitorrapela/xdog)  \n[\\[online demo\\]](https://xdog.alexpeattie.com/)  \nOthers: [code(C++)](https://github.com/Sunwinds/xdog-demo) [code(matlab)](https://github.com/CemalUnal/XDoG-Filter) [code(Web APP)](https://github.com/alexpeattie/xdog-sketch) |\n| FDoG | [Coherent Line Drawing](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.559&rep=rep1&type=pdf) | NPAR 2007 | [\\[code\\]](https://github.com/SSARCandy/Coherent-Line-Drawing) [\\[project\\]](https://ssarcandy.tw/Coherent-Line-Drawing/) |\n| Canny | [A Computational Approach to Edge Detection](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf) | TPAMI 1986 | [\\[code\\]](https://rosettacode.org/wiki/Canny_edge_detector) [\\[code-py\\]](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html) |\n\n* * *\n\n3\\. Useful Links\n----------------\n\n[](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers?screenshot=true#3-useful-links)\n\n*   Code to plot edge PR curves: [MCG-NKU/plot-edge-pr-curves](https://github.com/MCG-NKU/plot-edge-pr-curves)",
  "usage": {
    "tokens": 5030
  }
}
```
