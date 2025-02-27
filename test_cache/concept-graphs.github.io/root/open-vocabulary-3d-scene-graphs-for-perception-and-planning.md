---
title: Open-Vocabulary 3D Scene Graphs for Perception and Planning
description: ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning
url: https://concept-graphs.github.io/
timestamp: 2025-01-20T15:45:13.194Z
domain: concept-graphs.github.io
path: root
---

# Open-Vocabulary 3D Scene Graphs for Perception and Planning


ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning


## Content

ICRA 2024
---------

[_Alihusein Kuwajerwala_](https://www.alihkw.com/) 2\*, [_Sacha Morin_](https://sachamorin.github.io/) 2\*, [_Krishna Murthy Jatavallabhula_](https://krrish94.github.io/) 1\*,  
[Bipasha Sen](https://bipashasen.github.io/)2, [Aditya Agarwal](https://skymanaditya1.github.io/)2, [Corban Rivera](https://www.jhuapl.edu/work/our-organization/research-and-exploratory-development/red-staff-directory/corban-rivera)5, [William Paul](https://scholar.google.com/citations?user=92bmh84AAAAJ)1, [Kirsty Ellis](https://mila.quebec/en/person/kirsty-ellis/)2,  
[Rama Chellappa](https://engineering.jhu.edu/faculty/rama-chellappa/)6, [Chuang Gan](https://people.csail.mit.edu/ganchuang/)7, [Celso Miguel de Melo](https://celsodemelo.net/)8,  
[Joshua B. Tenenbaum](http://web.mit.edu/cocosci/josh.html)1, [Antonio Torralba](https://groups.csail.mit.edu/vision/torralbalab/)1, [Florian Shkurti](http://www.cs.toronto.edu//~florian/)3, [Liam Paull](http://liampaull.ca/)2

1MIT, 2Université de Montréal, 3University of Toronto, 4IIIT Hyderabad, 5JHU APL, 6JHU, 7UMass Amherst, 8DEVCOM Army Research Laboratory

\*Equal contribution

ConceptGraphs builds open-vocabulary 3D scenegraphs that enable a broad range of perception and task planning capabilities.
---------------------------------------------------------------------------------------------------------------------------

Abstract
--------

For robots to perform a wide variety of tasks, they require a 3D representation of the world that is semantically rich, yet compact and efficient for task-driven perception and planning. Recent approaches have attempted to leverage features from large vision-language models to encode semantics in 3D representations. However, these approaches tend to produce maps with per-point feature vectors, which do not scale well in larger environments, nor do they contain semantic spatial relationships between entities in the environment, which are useful for downstream planning. In this work, we propose ConceptGraphs, an open-vocabulary graph-structured representation for 3D scenes. ConceptGraphs is built by leveraging 2D foundation models and fusing their output to 3D by multi-view association. The resulting representations generalize to novel semantic classes, without the need to collect large 3D datasets or finetune models. We demonstrate the utility of this representation through a number of downstream planning tasks that are specified through abstract (language) prompts and require complex reasoning over spatial and semantic concepts.

Approach
--------

ConceptGraphs builds an open-vocabulary 3D scene graph from a sequence of posed RGB-D images. We use generic instance segmentation models to segment regions from RGB images, extract semantic feature vectors for each, and project them to a 3D point cloud. These regions are incrementally associated and fused from multiple views, resulting in a set of 3D objects and associated vision (and language) descriptors. Then large vision and language models are used to caption each mapped 3D objects and derive inter-object relations, which generates the edges to connect the set of objects and form a graph. The resulting 3D scene graph provides a structured and comprehensive understanding of the scene and can further be easily translated to a text description, useful for LLM-based task planning.

![Image 4](https://concept-graphs.github.io/static/images/pipeline.png)

  

Re-localization
---------------

We emply ConceptGraphs to localize the robot in a previously mapped environment. Each object encodes a CLIP embedding, which is employed in a landmark-based particle-filter that uses cosine similarity to compute particle weights. Within a few iterations, the robot localizes accurately. In our explainer video, we also demonstrate mapping newly-detected objects that were not present in the original map.

Text queries via CLIP or GPT-4
------------------------------

We demonstrate the ability of ConceptGraphs to answer open-set text queries. Each object in the scene graphs contains an associated CLIP embedding (fused from multi-view images), as well as a text caption. While the CLIP embeddings work well across a wide range of queries, they fail when the queries reference multiple concepts, involve negation, or complex composition. We may also use LLMs (here, GPT-4) to find objects that address the text query. This approach performs better, especially on complex queries, but requires access to an LLM at inference time (while the CLIP text-query approach is easily deployable on CPUs on-board the robot).

### Queries with both text and image context

We can also handle text queries that include context from an additional image. In this example, we the robot looks at an image of Michael Jordan, and is given a text query "something this guy would play with". It is able to locate the basketball in the scene.

### Traversability puzzle

The Jackal robot solving a traversability challenge. All paths to the goal are obstructed by objects. We query an LLM to identify which objects can be safely pushed or traversed by the robot (green) and which objects would be too heavy or hinder the robot’s movement (red). The LLM relies on the ConceptGraphs node captions to make traversability predictions and we add the non-traversable objects to the Jackal costmap for path planning. The Jackal successfully reaches the goal by going through a curtain and pushing a basketball, while also avoiding contact with bricks, an iron dumbbell, and a flower pot.

Concurrent work
---------------

Given the pace of AI research these days, it is extremely challenging to keep up with all of the work around foundation models and open-set perception. We list below a few key approaches that we have come across after finalizing the ConceptGraphs system. If we may have inadvertently missed out on key concurrent work, please reach out to us over email (or better, open a pull request on [our GitHub page](https://github.com/concept-graphs/concept-graphs.github.io)).

[OVIR-3D](https://openreview.net/forum?id=gVBvtRqU1_) is an open-vocabulary 3D instance-level mapping system that reconstructs an objects from RGB-D images and known poses. Each object is additionally assigned a CLIP embedding for text-query-based retrieval.

[OpenMask3D](https://openmask3d.github.io/) performs 3D instance segmentation (on pointcloud data) based on open-vocabulary queries (specified as text).

[OVSG](https://openreview.net/forum?id=cjEI5qXoT0) reconstructs open-vocabulary 3D scene graphs using OVIR-3D and a graph network encoder.

[SayPlan](https://sayplan.github.io/) demonstrates an efficient planning mechanism using LLMs and 3D Scene Graphs (assumed available).

BibTeX
------

```
@article{conceptgraphs,
  author    = {Gu, Qiao and Kuwajerwala, Alihusein and Morin, Sacha and Jatavallabhula, {Krishna Murthy} and  Sen, Bipasha and Agarwal, Aditya and Rivera, Corban and Paul, William and Ellis, Kirsty and Chellappa, Rama and Gan, Chuang and {de Melo}, {Celso Miguel} and Tenenbaum, {Joshua B.} and Torralba, Antonio and Shkurti, Florian and Paull, Liam},
  title     = {ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning},
  journal   = {arXiv},
  year      = {2023},
}
```

## Metadata

```json
{
  "title": "Open-Vocabulary 3D Scene Graphs for Perception and Planning",
  "description": "ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning",
  "url": "https://concept-graphs.github.io/",
  "content": "ICRA 2024\n---------\n\n[_Alihusein Kuwajerwala_](https://www.alihkw.com/) 2\\*, [_Sacha Morin_](https://sachamorin.github.io/) 2\\*, [_Krishna Murthy Jatavallabhula_](https://krrish94.github.io/) 1\\*,  \n[Bipasha Sen](https://bipashasen.github.io/)2, [Aditya Agarwal](https://skymanaditya1.github.io/)2, [Corban Rivera](https://www.jhuapl.edu/work/our-organization/research-and-exploratory-development/red-staff-directory/corban-rivera)5, [William Paul](https://scholar.google.com/citations?user=92bmh84AAAAJ)1, [Kirsty Ellis](https://mila.quebec/en/person/kirsty-ellis/)2,  \n[Rama Chellappa](https://engineering.jhu.edu/faculty/rama-chellappa/)6, [Chuang Gan](https://people.csail.mit.edu/ganchuang/)7, [Celso Miguel de Melo](https://celsodemelo.net/)8,  \n[Joshua B. Tenenbaum](http://web.mit.edu/cocosci/josh.html)1, [Antonio Torralba](https://groups.csail.mit.edu/vision/torralbalab/)1, [Florian Shkurti](http://www.cs.toronto.edu//~florian/)3, [Liam Paull](http://liampaull.ca/)2\n\n1MIT, 2Université de Montréal, 3University of Toronto, 4IIIT Hyderabad, 5JHU APL, 6JHU, 7UMass Amherst, 8DEVCOM Army Research Laboratory\n\n\\*Equal contribution\n\nConceptGraphs builds open-vocabulary 3D scenegraphs that enable a broad range of perception and task planning capabilities.\n---------------------------------------------------------------------------------------------------------------------------\n\nAbstract\n--------\n\nFor robots to perform a wide variety of tasks, they require a 3D representation of the world that is semantically rich, yet compact and efficient for task-driven perception and planning. Recent approaches have attempted to leverage features from large vision-language models to encode semantics in 3D representations. However, these approaches tend to produce maps with per-point feature vectors, which do not scale well in larger environments, nor do they contain semantic spatial relationships between entities in the environment, which are useful for downstream planning. In this work, we propose ConceptGraphs, an open-vocabulary graph-structured representation for 3D scenes. ConceptGraphs is built by leveraging 2D foundation models and fusing their output to 3D by multi-view association. The resulting representations generalize to novel semantic classes, without the need to collect large 3D datasets or finetune models. We demonstrate the utility of this representation through a number of downstream planning tasks that are specified through abstract (language) prompts and require complex reasoning over spatial and semantic concepts.\n\nApproach\n--------\n\nConceptGraphs builds an open-vocabulary 3D scene graph from a sequence of posed RGB-D images. We use generic instance segmentation models to segment regions from RGB images, extract semantic feature vectors for each, and project them to a 3D point cloud. These regions are incrementally associated and fused from multiple views, resulting in a set of 3D objects and associated vision (and language) descriptors. Then large vision and language models are used to caption each mapped 3D objects and derive inter-object relations, which generates the edges to connect the set of objects and form a graph. The resulting 3D scene graph provides a structured and comprehensive understanding of the scene and can further be easily translated to a text description, useful for LLM-based task planning.\n\n![Image 4](https://concept-graphs.github.io/static/images/pipeline.png)\n\n  \n\nRe-localization\n---------------\n\nWe emply ConceptGraphs to localize the robot in a previously mapped environment. Each object encodes a CLIP embedding, which is employed in a landmark-based particle-filter that uses cosine similarity to compute particle weights. Within a few iterations, the robot localizes accurately. In our explainer video, we also demonstrate mapping newly-detected objects that were not present in the original map.\n\nText queries via CLIP or GPT-4\n------------------------------\n\nWe demonstrate the ability of ConceptGraphs to answer open-set text queries. Each object in the scene graphs contains an associated CLIP embedding (fused from multi-view images), as well as a text caption. While the CLIP embeddings work well across a wide range of queries, they fail when the queries reference multiple concepts, involve negation, or complex composition. We may also use LLMs (here, GPT-4) to find objects that address the text query. This approach performs better, especially on complex queries, but requires access to an LLM at inference time (while the CLIP text-query approach is easily deployable on CPUs on-board the robot).\n\n### Queries with both text and image context\n\nWe can also handle text queries that include context from an additional image. In this example, we the robot looks at an image of Michael Jordan, and is given a text query \"something this guy would play with\". It is able to locate the basketball in the scene.\n\n### Traversability puzzle\n\nThe Jackal robot solving a traversability challenge. All paths to the goal are obstructed by objects. We query an LLM to identify which objects can be safely pushed or traversed by the robot (green) and which objects would be too heavy or hinder the robot’s movement (red). The LLM relies on the ConceptGraphs node captions to make traversability predictions and we add the non-traversable objects to the Jackal costmap for path planning. The Jackal successfully reaches the goal by going through a curtain and pushing a basketball, while also avoiding contact with bricks, an iron dumbbell, and a flower pot.\n\nConcurrent work\n---------------\n\nGiven the pace of AI research these days, it is extremely challenging to keep up with all of the work around foundation models and open-set perception. We list below a few key approaches that we have come across after finalizing the ConceptGraphs system. If we may have inadvertently missed out on key concurrent work, please reach out to us over email (or better, open a pull request on [our GitHub page](https://github.com/concept-graphs/concept-graphs.github.io)).\n\n[OVIR-3D](https://openreview.net/forum?id=gVBvtRqU1_) is an open-vocabulary 3D instance-level mapping system that reconstructs an objects from RGB-D images and known poses. Each object is additionally assigned a CLIP embedding for text-query-based retrieval.\n\n[OpenMask3D](https://openmask3d.github.io/) performs 3D instance segmentation (on pointcloud data) based on open-vocabulary queries (specified as text).\n\n[OVSG](https://openreview.net/forum?id=cjEI5qXoT0) reconstructs open-vocabulary 3D scene graphs using OVIR-3D and a graph network encoder.\n\n[SayPlan](https://sayplan.github.io/) demonstrates an efficient planning mechanism using LLMs and 3D Scene Graphs (assumed available).\n\nBibTeX\n------\n\n```\n@article{conceptgraphs,\n  author    = {Gu, Qiao and Kuwajerwala, Alihusein and Morin, Sacha and Jatavallabhula, {Krishna Murthy} and  Sen, Bipasha and Agarwal, Aditya and Rivera, Corban and Paul, William and Ellis, Kirsty and Chellappa, Rama and Gan, Chuang and {de Melo}, {Celso Miguel} and Tenenbaum, {Joshua B.} and Torralba, Antonio and Shkurti, Florian and Paull, Liam},\n  title     = {ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning},\n  journal   = {arXiv},\n  year      = {2023},\n}\n```",
  "usage": {
    "tokens": 1712
  }
}
```
