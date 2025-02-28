---
title: Floorplan Reconstruction Using Two-Level Queries
description: RoomFormer
url: https://ywyue.github.io/RoomFormer/
timestamp: 2025-01-20T15:42:38.469Z
domain: ywyue.github.io
path: RoomFormer
---

# Floorplan Reconstruction Using Two-Level Queries


RoomFormer


## Content

Connecting the Dots: Floorplan Reconstruction Using Two-Level Queries
---------------------------------------------------------------------

CVPR 2023
---------

1Photogrammetry and Remote Sensing, ETH Zurich 2ETH AI Center, ETH Zurich

![Image 13](https://ywyue.github.io/RoomFormer/assets/teaser.jpg)

Abstract
--------

We address 2D floorplan reconstruction from 3D scans. Existing approaches typically employ heuristically designed multi-stage pipelines. Instead, we formulate floorplan reconstruction as a single-stage structured prediction task: find a variable-size set of polygons, which in turn are variable-length sequences of ordered vertices. To solve it we develop a novel Transformer architecture that generates polygons of multiple rooms in parallel, in a holistic manner without hand-crafted intermediate stages. The model features two-level queries for polygons and corners, and includes polygon matching to make the network end-to-end trainable. Our method achieves a new state-of-the-art for two challenging datasets, Structured3D and SceneCAD, along with significantly faster inference than previous methods. Moreover, it can readily be extended to predict additional information, i.e., semantic room types and architectural elements like doors and windows.

RoomFormer
----------

![Image 14](https://ywyue.github.io/RoomFormer/assets/model.gif)

Illustration of the **RoomFormer** model. Given a top-down-view density map of the input point cloud, (a) the feature backbone extracts multi-scale features, adds positional encodings, and flattens them before passing them into the (b) Transformer encoder. (c) The Transformer decoder takes as input our two-level queries, one level for the room polygons (up to _M_) and one level for their corners (up to _N_ per room polygon). A feed-forward network (FFN) predicts a class _c_ for each query to accommodate for varying numbers of rooms and corners. During training, the polygon matching guarantees optimal assignment between predicted and groundtruth polygons.

Video
-----

Results on Structured3D
-----------------------

![Image 15](https://ywyue.github.io/RoomFormer/assets/s3d_results.jpg)

Results on SceneCAD
-------------------

![Image 16](https://ywyue.github.io/RoomFormer/assets/scenecad_results.jpg)

Semantically-Rich Floorplans
----------------------------

![Image 17](https://ywyue.github.io/RoomFormer/assets/sem_rich_results.jpg)

Conference Poster
-----------------

[![Image 18](https://ywyue.github.io/RoomFormer/assets/poster_preview.png)](https://ywyue.github.io/RoomFormer/assets/poster.pdf)

BibTeX
------

```
@inproceedings{yue2023connecting,
  title     = {{Connecting the Dots: Floorplan Reconstruction Using Two-Level Queries}},
  author    = {Yue, Yuanwen and Kontogianni, Theodora and Schindler, Konrad and Engelmann, Francis},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2023}
}
```

## Metadata

```json
{
  "title": "Floorplan Reconstruction Using Two-Level Queries",
  "description": "RoomFormer",
  "url": "https://ywyue.github.io/RoomFormer/",
  "content": "Connecting the Dots: Floorplan Reconstruction Using Two-Level Queries\n---------------------------------------------------------------------\n\nCVPR 2023\n---------\n\n1Photogrammetry and Remote Sensing, ETH Zurich 2ETH AI Center, ETH Zurich\n\n![Image 13](https://ywyue.github.io/RoomFormer/assets/teaser.jpg)\n\nAbstract\n--------\n\nWe address 2D floorplan reconstruction from 3D scans. Existing approaches typically employ heuristically designed multi-stage pipelines. Instead, we formulate floorplan reconstruction as a single-stage structured prediction task: find a variable-size set of polygons, which in turn are variable-length sequences of ordered vertices. To solve it we develop a novel Transformer architecture that generates polygons of multiple rooms in parallel, in a holistic manner without hand-crafted intermediate stages. The model features two-level queries for polygons and corners, and includes polygon matching to make the network end-to-end trainable. Our method achieves a new state-of-the-art for two challenging datasets, Structured3D and SceneCAD, along with significantly faster inference than previous methods. Moreover, it can readily be extended to predict additional information, i.e., semantic room types and architectural elements like doors and windows.\n\nRoomFormer\n----------\n\n![Image 14](https://ywyue.github.io/RoomFormer/assets/model.gif)\n\nIllustration of the **RoomFormer** model. Given a top-down-view density map of the input point cloud, (a) the feature backbone extracts multi-scale features, adds positional encodings, and flattens them before passing them into the (b) Transformer encoder. (c) The Transformer decoder takes as input our two-level queries, one level for the room polygons (up to _M_) and one level for their corners (up to _N_ per room polygon). A feed-forward network (FFN) predicts a class _c_ for each query to accommodate for varying numbers of rooms and corners. During training, the polygon matching guarantees optimal assignment between predicted and groundtruth polygons.\n\nVideo\n-----\n\nResults on Structured3D\n-----------------------\n\n![Image 15](https://ywyue.github.io/RoomFormer/assets/s3d_results.jpg)\n\nResults on SceneCAD\n-------------------\n\n![Image 16](https://ywyue.github.io/RoomFormer/assets/scenecad_results.jpg)\n\nSemantically-Rich Floorplans\n----------------------------\n\n![Image 17](https://ywyue.github.io/RoomFormer/assets/sem_rich_results.jpg)\n\nConference Poster\n-----------------\n\n[![Image 18](https://ywyue.github.io/RoomFormer/assets/poster_preview.png)](https://ywyue.github.io/RoomFormer/assets/poster.pdf)\n\nBibTeX\n------\n\n```\n@inproceedings{yue2023connecting,\n  title     = {{Connecting the Dots: Floorplan Reconstruction Using Two-Level Queries}},\n  author    = {Yue, Yuanwen and Kontogianni, Theodora and Schindler, Konrad and Engelmann, Francis},\n  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year      = {2023}\n}\n```",
  "usage": {
    "tokens": 634
  }
}
```
