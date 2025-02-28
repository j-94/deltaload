---
title: Visual Blocks
description: Drag and drop off-the-shelf ML components with Visual Blocks. A fast, easy way to prototype ML pipelines – no expertise or coding required.
url: https://visualblocks.withgoogle.com/#/
timestamp: 2025-01-20T15:50:47.480Z
domain: visualblocks.withgoogle.com
path: root
---

# Visual Blocks


Drag and drop off-the-shelf ML components with Visual Blocks. A fast, easy way to prototype ML pipelines – no expertise or coding required.


## Content

Unleash your creativity
-----------------------

Visual Blocks for ML is a Google visual programming framework that lets you create ML pipelines in a no-code graph editor. You – and your users – can quickly prototype workflows by connecting drag-and-drop ML components, including models, user inputs, processors, and visualizations.

Try Visual Blocks

Try our Visual Blocks Colab integration examples: [Cartoonization](https://github.com/google/visualblocks/blob/main/examples/quick_start_cartoonization.ipynb), [Style Transfer](https://github.com/google/visualblocks/blob/main/examples/quick_start_style_transfer.ipynb)

Your browser does not support the video tag.

Learn Visual Blocks
-------------------

Tutorials
---------

### Create Effects

Use a live camera and ML models to create effects like face stickers.

### Compare Models

Import custom ML models and compare side-by-side results.

### Integrate with Colab

Use Visual Blocks in Colab and create nodes for custom Python code.

Publications
------------

ACM CHI 2023 (Honorable Mention Award)

Our paper describes the iterative design process of an earlier version of Visual Blocks for ML and how ML practitioners could accelerate their workflow, make more informed decisions, analyze strengths and weaknesses of ML models, and holistically evaluate model behavior with real-world input.

FAQ
---

*   ### What is Visual Blocks? up arrow
    
    Visual Blocks is a visual programming framework for rapidly prototyping and experimenting with ML models and pipelines. Using Visual Blocks, you can mix and match premade ML models and pipeline components in a graphical editor. The editor renders your pipeline as an interactive node graph where you can connect components by dragging and dropping nodes.
    
    Visual Blocks provides three core components:
    
    *   A library of nodes representing server-side models, in-browser models, and pre- and post-processing visualizers.
    *   A runner that runs the graph and displays the output of all or specific nodes.
    *   A visual editor where you can create your graph by connecting nodes with matching inputs and outputs.
*   ### Why did you create Visual Blocks? up arrow
    
    Recent advances in ML have enabled high-performance, real-time solutions to multimedia problems such as human body segmentation for video, depth estimation for 3D reconstruction, audio processing for remote communication (coming soon), and hand and body tracking.
    
    However, iterating on ML-based multimedia prototypes can be challenging and costly. It often requires a cross-functional team of ML practitioners to fine-tune models, evaluate robustness, identify strengths and weaknesses, measure performance, and develop applications. Because models have to be repeatedly updated and integrated, the workflow is ill-suited to prototyping and experimenting.
    
    Visual Blocks is designed to address these challenges. Its visual editor provides a no-code development environment where you can create and connect different components to rapidly build an ML pipeline and see the results in real time. Visual Blocks has the following goals:
    
    *   Lower development barriers for ML-based real-time multimedia applications.
    *   Empower users to experiment without worrying about coding or technical details.
    *   Provide premade models and datasets for common tasks such as body segmentation, landmark detection, and portrait depth estimation.
    *   Support various types of input data (image, video, audio (coming soon)) and output modalities (graphics, sound).
    *   Provide interactive data augmentation and manipulation with drag-and-drop operations and parameter sliders.
    *   Enable side-by-side comparisons of models and outputs at different stages of the pipeline.
    *   Make it easy to share visualizations and publish multimedia pipelines to the web.
    *   Facilitate collaboration between designers and developers.
    *   Provide a common language for describing ML pipelines.
    
    Ultimately, we hope Visual Blocks will help you accelerate your workflow, make more informed decisions about model selection and tuning, analyze the strengths and weaknesses of different models, evaluate model behavior with real-world input, and share your applications with the world.
    
*   ### How does Visual Blocks work? up arrow
    
    Visual Blocks is mainly written in JavaScript. It leverages [TensorFlow.js](https://www.tensorflow.org/js) and [TensorFlow Lite](https://www.tensorflow.org/lite) for ML capabilities and [three.js](https://threejs.org/) for graphics rendering.
    
    The Visual Blocks interface helps you rapidly build and interact with ML models using three coordinated views:
    
    *   A node library containing more than 30 nodes (including nodes for image processing, body segmentation, and image comparison) and a search bar for filtering.
    *   A [node-graph editor](https://en.wikipedia.org/wiki/Node_graph_architecture) that lets you create multimedia pipelines by dragging and dropping nodes from the library.
    *   A preview panel that shows pipeline inputs and outputs, provides immediate updates, and enables comparison of different models.
*   ### How do I get started? up arrow
    
    Currently, Visual Blocks is available as a Colab integration. The integration lets you build interactive demos in Colab notebooks using prebuilt components.
    
    To get started with Visual Blocks, try the [demos](https://visualblocks.withgoogle.com/#/community) or one of the following Colab examples:
    
    *   [Visual Blocks Quick Start for Colab: Cartoonization](https://github.com/google/visualblocks/blob/main/examples/quick_start_cartoonization.ipynb)
    *   [Visual Blocks Quick Start for Colab: Style Transfer](https://github.com/google/visualblocks/blob/main/examples/quick_start_style_transfer.ipynb)
    
    Then check out the documentation at the Visual Blocks [GitHub repository](https://github.com/google/visualblocks).
    
    Visual Blocks for ML is intended to be used in line with [Google’s AI principles](https://ai.google/principles/).
    
*   ### Where can I learn more? up arrow
    
    To learn more about Visual Blocks, see the following resources:
    
    *   [Rapsai: Accelerating Machine Learning Prototyping of Multimedia Applications through Visual Programming](https://duruofei.com/papers/Du_Rapsai-AcceleratingMachineLearningPrototypingOfMultimediaApplicationsThroughVisualProgramming_CHI2023.pdf) (“Rapsai” was the initial name for Visual Blocks)
    *   [Visual Blocks for ML: Accelerating machine learning prototyping with interactive tools – Google AI Blog](https://ai.googleblog.com/2023/04/visual-blocks-for-ml-accelerating.html)

## Metadata

```json
{
  "title": "Visual Blocks",
  "description": "Drag and drop off-the-shelf ML components with Visual Blocks. A fast, easy way to prototype ML pipelines – no expertise or coding required.",
  "url": "https://visualblocks.withgoogle.com/#/",
  "content": "Unleash your creativity\n-----------------------\n\nVisual Blocks for ML is a Google visual programming framework that lets you create ML pipelines in a no-code graph editor. You – and your users – can quickly prototype workflows by connecting drag-and-drop ML components, including models, user inputs, processors, and visualizations.\n\nTry Visual Blocks\n\nTry our Visual Blocks Colab integration examples: [Cartoonization](https://github.com/google/visualblocks/blob/main/examples/quick_start_cartoonization.ipynb), [Style Transfer](https://github.com/google/visualblocks/blob/main/examples/quick_start_style_transfer.ipynb)\n\nYour browser does not support the video tag.\n\nLearn Visual Blocks\n-------------------\n\nTutorials\n---------\n\n### Create Effects\n\nUse a live camera and ML models to create effects like face stickers.\n\n### Compare Models\n\nImport custom ML models and compare side-by-side results.\n\n### Integrate with Colab\n\nUse Visual Blocks in Colab and create nodes for custom Python code.\n\nPublications\n------------\n\nACM CHI 2023 (Honorable Mention Award)\n\nOur paper describes the iterative design process of an earlier version of Visual Blocks for ML and how ML practitioners could accelerate their workflow, make more informed decisions, analyze strengths and weaknesses of ML models, and holistically evaluate model behavior with real-world input.\n\nFAQ\n---\n\n*   ### What is Visual Blocks? up arrow\n    \n    Visual Blocks is a visual programming framework for rapidly prototyping and experimenting with ML models and pipelines. Using Visual Blocks, you can mix and match premade ML models and pipeline components in a graphical editor. The editor renders your pipeline as an interactive node graph where you can connect components by dragging and dropping nodes.\n    \n    Visual Blocks provides three core components:\n    \n    *   A library of nodes representing server-side models, in-browser models, and pre- and post-processing visualizers.\n    *   A runner that runs the graph and displays the output of all or specific nodes.\n    *   A visual editor where you can create your graph by connecting nodes with matching inputs and outputs.\n*   ### Why did you create Visual Blocks? up arrow\n    \n    Recent advances in ML have enabled high-performance, real-time solutions to multimedia problems such as human body segmentation for video, depth estimation for 3D reconstruction, audio processing for remote communication (coming soon), and hand and body tracking.\n    \n    However, iterating on ML-based multimedia prototypes can be challenging and costly. It often requires a cross-functional team of ML practitioners to fine-tune models, evaluate robustness, identify strengths and weaknesses, measure performance, and develop applications. Because models have to be repeatedly updated and integrated, the workflow is ill-suited to prototyping and experimenting.\n    \n    Visual Blocks is designed to address these challenges. Its visual editor provides a no-code development environment where you can create and connect different components to rapidly build an ML pipeline and see the results in real time. Visual Blocks has the following goals:\n    \n    *   Lower development barriers for ML-based real-time multimedia applications.\n    *   Empower users to experiment without worrying about coding or technical details.\n    *   Provide premade models and datasets for common tasks such as body segmentation, landmark detection, and portrait depth estimation.\n    *   Support various types of input data (image, video, audio (coming soon)) and output modalities (graphics, sound).\n    *   Provide interactive data augmentation and manipulation with drag-and-drop operations and parameter sliders.\n    *   Enable side-by-side comparisons of models and outputs at different stages of the pipeline.\n    *   Make it easy to share visualizations and publish multimedia pipelines to the web.\n    *   Facilitate collaboration between designers and developers.\n    *   Provide a common language for describing ML pipelines.\n    \n    Ultimately, we hope Visual Blocks will help you accelerate your workflow, make more informed decisions about model selection and tuning, analyze the strengths and weaknesses of different models, evaluate model behavior with real-world input, and share your applications with the world.\n    \n*   ### How does Visual Blocks work? up arrow\n    \n    Visual Blocks is mainly written in JavaScript. It leverages [TensorFlow.js](https://www.tensorflow.org/js) and [TensorFlow Lite](https://www.tensorflow.org/lite) for ML capabilities and [three.js](https://threejs.org/) for graphics rendering.\n    \n    The Visual Blocks interface helps you rapidly build and interact with ML models using three coordinated views:\n    \n    *   A node library containing more than 30 nodes (including nodes for image processing, body segmentation, and image comparison) and a search bar for filtering.\n    *   A [node-graph editor](https://en.wikipedia.org/wiki/Node_graph_architecture) that lets you create multimedia pipelines by dragging and dropping nodes from the library.\n    *   A preview panel that shows pipeline inputs and outputs, provides immediate updates, and enables comparison of different models.\n*   ### How do I get started? up arrow\n    \n    Currently, Visual Blocks is available as a Colab integration. The integration lets you build interactive demos in Colab notebooks using prebuilt components.\n    \n    To get started with Visual Blocks, try the [demos](https://visualblocks.withgoogle.com/#/community) or one of the following Colab examples:\n    \n    *   [Visual Blocks Quick Start for Colab: Cartoonization](https://github.com/google/visualblocks/blob/main/examples/quick_start_cartoonization.ipynb)\n    *   [Visual Blocks Quick Start for Colab: Style Transfer](https://github.com/google/visualblocks/blob/main/examples/quick_start_style_transfer.ipynb)\n    \n    Then check out the documentation at the Visual Blocks [GitHub repository](https://github.com/google/visualblocks).\n    \n    Visual Blocks for ML is intended to be used in line with [Google’s AI principles](https://ai.google/principles/).\n    \n*   ### Where can I learn more? up arrow\n    \n    To learn more about Visual Blocks, see the following resources:\n    \n    *   [Rapsai: Accelerating Machine Learning Prototyping of Multimedia Applications through Visual Programming](https://duruofei.com/papers/Du_Rapsai-AcceleratingMachineLearningPrototypingOfMultimediaApplicationsThroughVisualProgramming_CHI2023.pdf) (“Rapsai” was the initial name for Visual Blocks)\n    *   [Visual Blocks for ML: Accelerating machine learning prototyping with interactive tools – Google AI Blog](https://ai.googleblog.com/2023/04/visual-blocks-for-ml-accelerating.html)",
  "usage": {
    "tokens": 1336
  }
}
```
