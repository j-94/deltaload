---
title: ATISS: Autoregressive Transformers for Indoor Scene Synthesis
description: 
url: https://nv-tlabs.github.io/ATISS/
timestamp: 2025-01-20T15:42:34.165Z
domain: nv-tlabs.github.io
path: ATISS
---

# ATISS: Autoregressive Transformers for Indoor Scene Synthesis



## Content

1 Autonomous Vision Group, MPI for Intelligent Systems Tübingen 2 University of Tübingen  
3 Max Planck ETH Center for Learning Systems 4 NVIDIA 5 University of Toronto 6 Vector Institute

![Image 60](https://research.nvidia.com/labs/toronto-ai/ATISS/atiss/teaser.png)

We present ATISS, a novel autoregressive transformer architecture for creating plausible synthetic indoor environments, given only the room type and its floor plan. In contrast to prior work, which poses scene synthesis as sequence generation, **our model generates rooms as unordered sets of objects**. Our model leverages the permutation equivariance of the transformer when conditioning on the partial scene, and **is trained to be permutation-invariant across object orderings**. Our model is trained end-to-end as an autoregressive generative model using only labeled 3D bounding boxes as supervision. Our formulation allows applying a single trained model to automatic layout synthesis and to a number of interactive scenarios with versatile user input, such as automatic placement of user-provided objects, object suggestion with user-provided constraints, and room completion.

Examples of generated bedrooms, living rooms, dining rooms and libraries conditioned on various floor plans and room types. For all visualizations we used [NVIDIA Omniverse](https://developer.nvidia.com/nvidia-omniverse-platform).

Given an empty or a partially complete room of a specific type together with its shape, as a top-down orthographic projection of its floor, we want to learn a generative model that populates the room with objects, whose functional composition and spatial arrangement is plausible. In contrast to prior work, we **pose scene synthesis as an unordered set generation problem** and introduce ATISS, a novel autoregressive transformer architecture to model this process. In particular, **our model generates meaningful furniture arrangements by sequentially placing objects in a permutation-invariant fashion**. We train ATISS to maximize the log-likelihood of all possible permutations of object arrangements in a collection of training scenes, labeled only with object classes and 3D bounding boxes.

Objects in a scene are represented as labeled 3D bounding boxes and we model them with four random variables that describe their category, size, orientation and location, \\(o\_j = \\{\\bf{c}\_j, \\bf{s}\_j, \\bf{t}\_j, \\bf{r}\_j\\}\\). The category \\(\\bf{c}\_j\\) is modeled using a categorical variable over the total number of object categories in the dataset and the size \\(\\bf{s}\_j\\), location \\(\\bf{t}\_j\\) and orientation \\(\\bf{r}\_j\\) are modelled with mixture of logistics distributions.

![Image 61](https://research.nvidia.com/labs/toronto-ai/ATISS/atiss/training_overview.png)

**During training**, we start from a scene with M objects (coloured squares, here \\(M=5\\)), we randomly permute them and keep the first T objects (here \\(T=3\\)). We task our network to predict the next object to be added in the scene given the subset of kept objects (highlighted with grey) and its floor layout feature \\(\\bf{F}\\). Our loss function is the negative log-likelihood (NLL) of the next object in the permuted sequence (green square).

**During inference**, we start with an empty context embedding \\(\\bf{C}\\) and the floor representation \\(\\bf{F}\\) of the room to be populated and autoregressively sample attribute values from the predicted distributions. Once a new object is generated, it is appended to the context \\(\\bf{C}\\) to be used in the next step of the generation process until the end symbol is generated. To transform the predicted labeled bounding boxes to 3D models we use object retrieval. In particular, we retrieve the closest object from the dataset in terms of the euclidean distance of the bounding box dimensions. A pictorial representation of the generation process is provided in the figure below.

![Image 62](https://research.nvidia.com/labs/toronto-ai/ATISS/atiss/network_architecture.png)

Our network consists of four main components: (i) the **layout encoder** that maps the room shape to a feature representation \\(\\bf{F}\\), (ii) the **structure encoder** that maps the objects in the scene into per-object context embeddings \\(\\bf{C} = \\{C\_j\\}^M\_{j=1}\\) , (iii) the **transformer encoder** that takes \\(\\bf{F}\\), \\(\\bf{C}\\) and a query embedding \\(\\bf{q}\\) and predicts the features \\(\\bf{\\hat{q}}\\) for the next object to be generated and (iv) the **attribute extractor** that predicts the attributes of the next object to be added in the scene.

Our model can be used to generate furniture arrangements conditioned on a floor plan and a specific room type. In the following, we show examples of generated bedrooms (first row), living rooms (second row), dining rooms (third row) and libraries (fourth row) using our model conditioned on various floor plans. We can easily notice that our model consistently generates plausible room arrangements that preserve the functional properties of all objects in the scene. Note that for all visualizations, we used [NVIDIA Omniverse](https://developer.nvidia.com/nvidia-omniverse-platform).

In the following, we show scene completion examples. Starting from a partially empty scene (left column), our model populates it by generating meaningful object arrangements.

Our model can also be used to provide object suggestions given a scene and **user specified location constraints**. In particular, a user specifies a region of acceptable positions to place an object (here marked as a red box) and our model suggests suitable objects to be placed inside this area of valid locations. In case the user specifies a region that intersects with other objects in the scene and our model cannot suggest a meaningful object to be placed there, it simply suggests to add nothing (see first column).

Another useful application of our model is its ability to **identify unnatural furniture layouts** and reposition the problematic objects such that they preserve their functional properties. The problematic object, as identified by our model, is highlighted with green. As soon as a problematic object is identified, our model repositions it in a more suitable location.

If you found this work influential or helpful for your research, please consider citing

```

@InProceedings{Paschalidou2021NEURIPS,
  author = {Despoina Paschalidou and Amlan Kar and Maria Shugrina and Karsten Kreis and Andreas Geiger
  and Sanja Fidler},
  title = {ATISS: Autoregressive Transformers for Indoor Scene Synthesis},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year = {2021}
}
```

## Metadata

```json
{
  "title": "ATISS: Autoregressive Transformers for Indoor Scene Synthesis",
  "description": "",
  "url": "https://nv-tlabs.github.io/ATISS/",
  "content": "1 Autonomous Vision Group, MPI for Intelligent Systems Tübingen 2 University of Tübingen  \n3 Max Planck ETH Center for Learning Systems 4 NVIDIA 5 University of Toronto 6 Vector Institute\n\n![Image 60](https://research.nvidia.com/labs/toronto-ai/ATISS/atiss/teaser.png)\n\nWe present ATISS, a novel autoregressive transformer architecture for creating plausible synthetic indoor environments, given only the room type and its floor plan. In contrast to prior work, which poses scene synthesis as sequence generation, **our model generates rooms as unordered sets of objects**. Our model leverages the permutation equivariance of the transformer when conditioning on the partial scene, and **is trained to be permutation-invariant across object orderings**. Our model is trained end-to-end as an autoregressive generative model using only labeled 3D bounding boxes as supervision. Our formulation allows applying a single trained model to automatic layout synthesis and to a number of interactive scenarios with versatile user input, such as automatic placement of user-provided objects, object suggestion with user-provided constraints, and room completion.\n\nExamples of generated bedrooms, living rooms, dining rooms and libraries conditioned on various floor plans and room types. For all visualizations we used [NVIDIA Omniverse](https://developer.nvidia.com/nvidia-omniverse-platform).\n\nGiven an empty or a partially complete room of a specific type together with its shape, as a top-down orthographic projection of its floor, we want to learn a generative model that populates the room with objects, whose functional composition and spatial arrangement is plausible. In contrast to prior work, we **pose scene synthesis as an unordered set generation problem** and introduce ATISS, a novel autoregressive transformer architecture to model this process. In particular, **our model generates meaningful furniture arrangements by sequentially placing objects in a permutation-invariant fashion**. We train ATISS to maximize the log-likelihood of all possible permutations of object arrangements in a collection of training scenes, labeled only with object classes and 3D bounding boxes.\n\nObjects in a scene are represented as labeled 3D bounding boxes and we model them with four random variables that describe their category, size, orientation and location, \\\\(o\\_j = \\\\{\\\\bf{c}\\_j, \\\\bf{s}\\_j, \\\\bf{t}\\_j, \\\\bf{r}\\_j\\\\}\\\\). The category \\\\(\\\\bf{c}\\_j\\\\) is modeled using a categorical variable over the total number of object categories in the dataset and the size \\\\(\\\\bf{s}\\_j\\\\), location \\\\(\\\\bf{t}\\_j\\\\) and orientation \\\\(\\\\bf{r}\\_j\\\\) are modelled with mixture of logistics distributions.\n\n![Image 61](https://research.nvidia.com/labs/toronto-ai/ATISS/atiss/training_overview.png)\n\n**During training**, we start from a scene with M objects (coloured squares, here \\\\(M=5\\\\)), we randomly permute them and keep the first T objects (here \\\\(T=3\\\\)). We task our network to predict the next object to be added in the scene given the subset of kept objects (highlighted with grey) and its floor layout feature \\\\(\\\\bf{F}\\\\). Our loss function is the negative log-likelihood (NLL) of the next object in the permuted sequence (green square).\n\n**During inference**, we start with an empty context embedding \\\\(\\\\bf{C}\\\\) and the floor representation \\\\(\\\\bf{F}\\\\) of the room to be populated and autoregressively sample attribute values from the predicted distributions. Once a new object is generated, it is appended to the context \\\\(\\\\bf{C}\\\\) to be used in the next step of the generation process until the end symbol is generated. To transform the predicted labeled bounding boxes to 3D models we use object retrieval. In particular, we retrieve the closest object from the dataset in terms of the euclidean distance of the bounding box dimensions. A pictorial representation of the generation process is provided in the figure below.\n\n![Image 62](https://research.nvidia.com/labs/toronto-ai/ATISS/atiss/network_architecture.png)\n\nOur network consists of four main components: (i) the **layout encoder** that maps the room shape to a feature representation \\\\(\\\\bf{F}\\\\), (ii) the **structure encoder** that maps the objects in the scene into per-object context embeddings \\\\(\\\\bf{C} = \\\\{C\\_j\\\\}^M\\_{j=1}\\\\) , (iii) the **transformer encoder** that takes \\\\(\\\\bf{F}\\\\), \\\\(\\\\bf{C}\\\\) and a query embedding \\\\(\\\\bf{q}\\\\) and predicts the features \\\\(\\\\bf{\\\\hat{q}}\\\\) for the next object to be generated and (iv) the **attribute extractor** that predicts the attributes of the next object to be added in the scene.\n\nOur model can be used to generate furniture arrangements conditioned on a floor plan and a specific room type. In the following, we show examples of generated bedrooms (first row), living rooms (second row), dining rooms (third row) and libraries (fourth row) using our model conditioned on various floor plans. We can easily notice that our model consistently generates plausible room arrangements that preserve the functional properties of all objects in the scene. Note that for all visualizations, we used [NVIDIA Omniverse](https://developer.nvidia.com/nvidia-omniverse-platform).\n\nIn the following, we show scene completion examples. Starting from a partially empty scene (left column), our model populates it by generating meaningful object arrangements.\n\nOur model can also be used to provide object suggestions given a scene and **user specified location constraints**. In particular, a user specifies a region of acceptable positions to place an object (here marked as a red box) and our model suggests suitable objects to be placed inside this area of valid locations. In case the user specifies a region that intersects with other objects in the scene and our model cannot suggest a meaningful object to be placed there, it simply suggests to add nothing (see first column).\n\nAnother useful application of our model is its ability to **identify unnatural furniture layouts** and reposition the problematic objects such that they preserve their functional properties. The problematic object, as identified by our model, is highlighted with green. As soon as a problematic object is identified, our model repositions it in a more suitable location.\n\nIf you found this work influential or helpful for your research, please consider citing\n\n```\n\n@InProceedings{Paschalidou2021NEURIPS,\n  author = {Despoina Paschalidou and Amlan Kar and Maria Shugrina and Karsten Kreis and Andreas Geiger\n  and Sanja Fidler},\n  title = {ATISS: Autoregressive Transformers for Indoor Scene Synthesis},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year = {2021}\n}\n```",
  "usage": {
    "tokens": 1477
  }
}
```
