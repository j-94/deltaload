---
title: GitHub - art-programmer/FloorplanTransformation: Raster-to-Vector: Revisiting Floorplan Transformation
description: Raster-to-Vector: Revisiting Floorplan Transformation - art-programmer/FloorplanTransformation
url: https://github.com/art-programmer/FloorplanTransformation
timestamp: 2025-01-20T15:30:35.583Z
domain: github.com
path: art-programmer_FloorplanTransformation
---

# GitHub - art-programmer/FloorplanTransformation: Raster-to-Vector: Revisiting Floorplan Transformation


Raster-to-Vector: Revisiting Floorplan Transformation - art-programmer/FloorplanTransformation


## Content

Raster-to-Vector: Revisiting Floorplan Transformation
-----------------------------------------------------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#raster-to-vector-revisiting-floorplan-transformation)

By Chen Liu, Jiajun Wu, Pushmeet Kohli, and Yasutaka Furukawa

Introduction
------------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#introduction)

This paper addresses the problem of converting a rasterized floorplan image into a vector-graphics representation. Our algorithm significantly outperforms existing methods and achieves around 90% precision and recall, getting to the range of production-ready performance. To learn more, please refer to our ICCV 2017 [paper](http://art-programmer.github.io/floorplan-transformation/paper.pdf) or visit our [project website](http://art-programmer.github.io/floorplan-transformation.html).

This code implements the algorithm described in our paper in Torch7.

Updates
-------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#updates)

\[12/21/2018\] A **PyTorch** version is now available under folder _pytorch/_. It is much easier to compile and try. Please see the README file under the folder for details. Note that we haven't evaluated the performance of it yet. We also provide a free IP solver (not relying on Gurobi) at _pytorch/IP.py_.

\[7/1/2018\] For annotator codes, please see [here](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#annotator).

\[4/15/2018\] We have a follow-up project which reconstructs floorplans from 3D scans. You can find it [here](https://github.com/art-programmer/FloorNet).

Requirements
------------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#requirements)

*   Please install the latest Torch.
*   Please install Python 2.7.
*   We used a Nvidia Titan GPU with CUDA 8.0 installed.

### Torch packages

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#torch-packages)

*   [nn](https://github.com/torch/nn)
*   [cunn](https://github.com/torch/cunn)
*   [cudnn](https://github.com/soumith/cudnn.torch)
*   [image](https://github.com/torch/image)
*   [ffi](http://luajit.org/ext_ffi.html)
*   [csvigo](https://github.com/clementfarabet/lua---csv)
*   [penlight](https://github.com/stevedonovan/Penlight)
*   [opencv](https://github.com/marcoscoffier/lua---opencv) (Probably need to be compiled from source)
*   [lunatic-python](https://labix.org/lunatic-python)

### Python packages

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#python-packages)

*   [numpy](http://www.scipy.org/scipylib/download.html)
*   [Gurobi](http://www.gurobi.com/)
*   [OpenCV](https://opencv.org/) (v3.4.1)

Trained models
--------------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#trained-models)

To use our trained model, please first download it from [Google Drive](https://drive.google.com/file/d/0B2rs82y7tjKrQk0yRFB3RHVDUXM/view?usp=sharing), and put it under folder "checkpoint/" (or specify the its path via option -loadModel="path to the downloaded model").

Our model is fine-tuned based on the pose estimation network introduced in the paper, "Human pose estimation via Convolutional Part Heatmap Regression". You can downloaded their model [here](https://www.adrianbulat.com/human-pose-estimation) (the MPII one), and put it under folder "PoseEstimation/" (or specify the its path via option -loadPoseEstimationModel)

Data
----

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#data)

We don't have the permission to share the rasterized images, which are from the LIFULL dataset. Here we only share our vector-graphics annotations which might be helpful for other tasks.

Our vector-graphics annotation is under "data/floorplan\_representation" folder.

Each row in vector graphics annotations contains (x\_min, y\_min, x\_max, y\_max, category, dump\_1, dump\_2). Category can be either a wall, a door (opening in the paper), a specific icon type, or a specific room type. For walls and doors, two points, (x\_min, y\_min) and (x\_max, y\_max), form a line. For icons, x\_min, y\_min, x\_max, and y\_max specify a rectangle. For rooms, however, x\_min, y\_min, x\_max, and y\_max are unfortunately not for the bounding box of the room, as a room can be of arbitrary shape instead of a rectangle. So, x\_min, y\_min, x\_max, and y\_max just denote an arbitrary region which falls inside the room. Please refer to the data loader code to see how to process such annotations.

Here is the [link](https://drive.google.com/file/d/1Ltn5kzzwhvXz6EStI98Zagfq-mI2pf0m/view?usp=sharing) to 100,000+ vector-graphics representation generated by our algorithm. You might want to get 3D popup models from the text files using the popup code below or draw 2D rendering images using the function _fp\_ut.drawRepresentationImage(floorplan, representation)_ (please see predict.lua for an example). Note that, since we cannot share the image data, you might need to change the code for either generating 3D popup models or rendering the 2D images.

Annotator
---------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#annotator)

The code for the annotator is available under folder _annotator/_. You can find a similar annotator written using Python [here](https://github.com/art-programmer/FloorplanAnnotator).

Usage
-----

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#usage)

To train the network from the pretrained pose estimation network, simply run

th main.lua -loadPoseEstimationModel  "path to the downloaded pose estimation model"

To load our trained model and resume training, please run

th main.lua -loadModel  "path to the downloaded pretrained model"

Here are som useful options for the main script:

*   \-batchSize specifies the batch size
*   \-LR specifies the learning rate
*   \-nEpochs specifies the number of epochs
*   \-checkpointEpochInterval specifies the number of training epochs between two checkpoints (useful if you want to save less number of checkpoints instead of saving one checkpoint for every epoch)
*   useCheckpoint specifies how the training resumes
    *   \-1: starting from the beginning even when checkpoints previously trained are found
    *   0 (default) resuming from checkpoints if found
    *   n (n \> 0) resuming from the nth checkpoint

To make prediction on a floorplan image, run

th predict.lua -loadModel "model path" -floorplanFilename "path to the floorplan image" -outputFilename "output filename"

Note that the above script will produce the vectorization result (saved in ".txt" file), the rendering image (saved in ".png" file), and a text file which could be used for generating 3D models (saved in "\_popup.txt").

To evaluate performance on the benchmark, run

th evaluate.lua -loadModel "model path" -resultPath "path to save results"

Generate 3D models
------------------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#generate-3d-models)

Automatic 3D model generation based on our vectorization results is implemented in both C++ (under folder popup/) and Python (under folder rendering/).

For the C++ code, run the following:

cd popup/code/
cmake .
make
./popup\_cli ../data/floorplan\_1.txt

The data file (e.g., popup/data/floorplan\_1.txt), which could be generated by _predict.lua_ (\*\_popup.txt), has the following format:

```
width height
the number of walls
(Wall descriptions)
x_1, y_1, x_2, y_2, room type on the left, room type on the right
...
(Opening descriptions)
x_1, y_1, x_2, y_2, 'door', dummy, dummy
(Icon descriptions)
x_1, y_1, x_2, y_2, icon type, dummy, dummy
```

You could optionally use the corresponding input raster image or the final vector-graphics rendering as the texture image for the floor. To do so, please put the image under the data folder and rename it to the same name with the data file with suffix ".png" (e.g., floorplan\_1.png).

The Python code is based on Panda3D. First enter folder rendering/, and then either run:

to view a 3D model, or run:

to render one view of the 3D model given camera pose. Please check the code to see how to specify the model to view and how to render different views.

Contact
-------

[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#contact)

If you have any questions, please contact me at [chenliu@wustl.edu](mailto:chenliu@wustl.edu).

## Metadata

```json
{
  "title": "GitHub - art-programmer/FloorplanTransformation: Raster-to-Vector: Revisiting Floorplan Transformation",
  "description": "Raster-to-Vector: Revisiting Floorplan Transformation - art-programmer/FloorplanTransformation",
  "url": "https://github.com/art-programmer/FloorplanTransformation?screenshot=true",
  "content": "Raster-to-Vector: Revisiting Floorplan Transformation\n-----------------------------------------------------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#raster-to-vector-revisiting-floorplan-transformation)\n\nBy Chen Liu, Jiajun Wu, Pushmeet Kohli, and Yasutaka Furukawa\n\nIntroduction\n------------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#introduction)\n\nThis paper addresses the problem of converting a rasterized floorplan image into a vector-graphics representation. Our algorithm significantly outperforms existing methods and achieves around 90% precision and recall, getting to the range of production-ready performance. To learn more, please refer to our ICCV 2017 [paper](http://art-programmer.github.io/floorplan-transformation/paper.pdf) or visit our [project website](http://art-programmer.github.io/floorplan-transformation.html).\n\nThis code implements the algorithm described in our paper in Torch7.\n\nUpdates\n-------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#updates)\n\n\\[12/21/2018\\] A **PyTorch** version is now available under folder _pytorch/_. It is much easier to compile and try. Please see the README file under the folder for details. Note that we haven't evaluated the performance of it yet. We also provide a free IP solver (not relying on Gurobi) at _pytorch/IP.py_.\n\n\\[7/1/2018\\] For annotator codes, please see [here](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#annotator).\n\n\\[4/15/2018\\] We have a follow-up project which reconstructs floorplans from 3D scans. You can find it [here](https://github.com/art-programmer/FloorNet).\n\nRequirements\n------------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#requirements)\n\n*   Please install the latest Torch.\n*   Please install Python 2.7.\n*   We used a Nvidia Titan GPU with CUDA 8.0 installed.\n\n### Torch packages\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#torch-packages)\n\n*   [nn](https://github.com/torch/nn)\n*   [cunn](https://github.com/torch/cunn)\n*   [cudnn](https://github.com/soumith/cudnn.torch)\n*   [image](https://github.com/torch/image)\n*   [ffi](http://luajit.org/ext_ffi.html)\n*   [csvigo](https://github.com/clementfarabet/lua---csv)\n*   [penlight](https://github.com/stevedonovan/Penlight)\n*   [opencv](https://github.com/marcoscoffier/lua---opencv) (Probably need to be compiled from source)\n*   [lunatic-python](https://labix.org/lunatic-python)\n\n### Python packages\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#python-packages)\n\n*   [numpy](http://www.scipy.org/scipylib/download.html)\n*   [Gurobi](http://www.gurobi.com/)\n*   [OpenCV](https://opencv.org/) (v3.4.1)\n\nTrained models\n--------------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#trained-models)\n\nTo use our trained model, please first download it from [Google Drive](https://drive.google.com/file/d/0B2rs82y7tjKrQk0yRFB3RHVDUXM/view?usp=sharing), and put it under folder \"checkpoint/\" (or specify the its path via option -loadModel=\"path to the downloaded model\").\n\nOur model is fine-tuned based on the pose estimation network introduced in the paper, \"Human pose estimation via Convolutional Part Heatmap Regression\". You can downloaded their model [here](https://www.adrianbulat.com/human-pose-estimation) (the MPII one), and put it under folder \"PoseEstimation/\" (or specify the its path via option -loadPoseEstimationModel)\n\nData\n----\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#data)\n\nWe don't have the permission to share the rasterized images, which are from the LIFULL dataset. Here we only share our vector-graphics annotations which might be helpful for other tasks.\n\nOur vector-graphics annotation is under \"data/floorplan\\_representation\" folder.\n\nEach row in vector graphics annotations contains (x\\_min, y\\_min, x\\_max, y\\_max, category, dump\\_1, dump\\_2). Category can be either a wall, a door (opening in the paper), a specific icon type, or a specific room type. For walls and doors, two points, (x\\_min, y\\_min) and (x\\_max, y\\_max), form a line. For icons, x\\_min, y\\_min, x\\_max, and y\\_max specify a rectangle. For rooms, however, x\\_min, y\\_min, x\\_max, and y\\_max are unfortunately not for the bounding box of the room, as a room can be of arbitrary shape instead of a rectangle. So, x\\_min, y\\_min, x\\_max, and y\\_max just denote an arbitrary region which falls inside the room. Please refer to the data loader code to see how to process such annotations.\n\nHere is the [link](https://drive.google.com/file/d/1Ltn5kzzwhvXz6EStI98Zagfq-mI2pf0m/view?usp=sharing) to 100,000+ vector-graphics representation generated by our algorithm. You might want to get 3D popup models from the text files using the popup code below or draw 2D rendering images using the function _fp\\_ut.drawRepresentationImage(floorplan, representation)_ (please see predict.lua for an example). Note that, since we cannot share the image data, you might need to change the code for either generating 3D popup models or rendering the 2D images.\n\nAnnotator\n---------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#annotator)\n\nThe code for the annotator is available under folder _annotator/_. You can find a similar annotator written using Python [here](https://github.com/art-programmer/FloorplanAnnotator).\n\nUsage\n-----\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#usage)\n\nTo train the network from the pretrained pose estimation network, simply run\n\nth main.lua -loadPoseEstimationModel  \"path to the downloaded pose estimation model\"\n\nTo load our trained model and resume training, please run\n\nth main.lua -loadModel  \"path to the downloaded pretrained model\"\n\nHere are som useful options for the main script:\n\n*   \\-batchSize specifies the batch size\n*   \\-LR specifies the learning rate\n*   \\-nEpochs specifies the number of epochs\n*   \\-checkpointEpochInterval specifies the number of training epochs between two checkpoints (useful if you want to save less number of checkpoints instead of saving one checkpoint for every epoch)\n*   useCheckpoint specifies how the training resumes\n    *   \\-1: starting from the beginning even when checkpoints previously trained are found\n    *   0 (default) resuming from checkpoints if found\n    *   n (n \\> 0) resuming from the nth checkpoint\n\nTo make prediction on a floorplan image, run\n\nth predict.lua -loadModel \"model path\" -floorplanFilename \"path to the floorplan image\" -outputFilename \"output filename\"\n\nNote that the above script will produce the vectorization result (saved in \".txt\" file), the rendering image (saved in \".png\" file), and a text file which could be used for generating 3D models (saved in \"\\_popup.txt\").\n\nTo evaluate performance on the benchmark, run\n\nth evaluate.lua -loadModel \"model path\" -resultPath \"path to save results\"\n\nGenerate 3D models\n------------------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#generate-3d-models)\n\nAutomatic 3D model generation based on our vectorization results is implemented in both C++ (under folder popup/) and Python (under folder rendering/).\n\nFor the C++ code, run the following:\n\ncd popup/code/\ncmake .\nmake\n./popup\\_cli ../data/floorplan\\_1.txt\n\nThe data file (e.g., popup/data/floorplan\\_1.txt), which could be generated by _predict.lua_ (\\*\\_popup.txt), has the following format:\n\n```\nwidth height\nthe number of walls\n(Wall descriptions)\nx_1, y_1, x_2, y_2, room type on the left, room type on the right\n...\n(Opening descriptions)\nx_1, y_1, x_2, y_2, 'door', dummy, dummy\n(Icon descriptions)\nx_1, y_1, x_2, y_2, icon type, dummy, dummy\n```\n\nYou could optionally use the corresponding input raster image or the final vector-graphics rendering as the texture image for the floor. To do so, please put the image under the data folder and rename it to the same name with the data file with suffix \".png\" (e.g., floorplan\\_1.png).\n\nThe Python code is based on Panda3D. First enter folder rendering/, and then either run:\n\nto view a 3D model, or run:\n\nto render one view of the 3D model given camera pose. Please check the code to see how to specify the model to view and how to render different views.\n\nContact\n-------\n\n[](https://github.com/art-programmer/FloorplanTransformation?screenshot=true#contact)\n\nIf you have any questions, please contact me at [chenliu@wustl.edu](mailto:chenliu@wustl.edu).",
  "usage": {
    "tokens": 2123
  }
}
```
