---
title: GitHub - StanfordVL/3DSceneGraph: The data skeleton from "3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera" http://3dscenegraph.stanford.edu
description: The data skeleton from "3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera" http://3dscenegraph.stanford.edu - StanfordVL/3DSceneGraph
url: https://github.com/StanfordVL/3DSceneGraph
timestamp: 2025-01-20T15:31:23.783Z
domain: github.com
path: StanfordVL_3DSceneGraph
---

# GitHub - StanfordVL/3DSceneGraph: The data skeleton from "3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera" http://3dscenegraph.stanford.edu


The data skeleton from "3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera" http://3dscenegraph.stanford.edu - StanfordVL/3DSceneGraph


## Content

3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera
-----------------------------------------------------------------------

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#3d-scene-graph-a-structure-for-unified-semantics-3d-space-and-camera)

[![Image 6](https://camo.githubusercontent.com/b6e842e453101747e563c5caf5418112fedc37c78506156a0546f819fc92b3e9/68747470733a2f2f33647363656e6567726170682e7374616e666f72642e6564752f696d616765732f33647363656e6567726170682e706e67)](https://camo.githubusercontent.com/b6e842e453101747e563c5caf5418112fedc37c78506156a0546f819fc92b3e9/68747470733a2f2f33647363656e6567726170682e7374616e666f72642e6564752f696d616765732f33647363656e6567726170682e706e67)

Overview
--------

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#overview)

The 3D Scene Graph provides semantic data for models in the [Gibson environment](http://gibsonenv.stanford.edu/) \[1\] that corresponds to the structure proposed in [3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera](http://3dscenegraph.stanford.edu/). The semantic information for models in the tiny Gibson split is verified via crowdsourcing and contains all 3D Scene Graph attributes. For these models we provide both the automated and verified outputs. For the rest of them, semantic information is the output of automated modules and does not include modalities that depend solely on manual input (e.g., object materials and textures). You can learn more about 3D Scene Graph and interact with the semantic data here: [http://3dscenegraph.stanford.edu](http://3dscenegraph.stanford.edu/)

Download
--------

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#download)

You can download the 3D Scene Graph data from the link below. The link will first take you to a license agreement, and then to the data. The data per model contains only semantics and is provided in the [compressed _.npz_ format](https://docs.scipy.org/doc/numpy/reference/generated/numpy.lib.format.html). To download the raw data visit the [Gibson Environment's database](http://gibsonenv.stanford.edu/database/) and agree to their terms of use. A [loading function](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#tools_&_dependencies) that returns the data in the 3D Scene graph structure is included in the 'tools/' folder. Semantics per model correspond to the `mesh.obj` 3D meshes and the `pano/rgb` panoramas of the Gibson database. To learn more about the type of semantics included in 3D Scene Graph, see [Dataset Structure](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#dataset-structure).

### [\[ Download 3D Scene Graph \]](https://redivis.com/datasets/1kf9-cfjvtqc7q)

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#-download-3d-scene-graph-)

#### Data Note: Our current release includes the tiny and medium Gibson splits. The rest of the models will follow shortly.

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#data-note-our-current-release-includes-the-tiny-and-medium-gibson-splits-the-rest-of-the-models-will-follow-shortly)

#### License Note: The dataset license is included in the above link. The license in this repository covers only the provided software. Note that it allows only non-commercial research use.

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#license-note-the-dataset-license-is-included-in-the-above-link-the-license-in-this-repository-covers-only-the-provided-software-note-that-it-allows-only-non-commercial-research-use)

Citations
---------

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#citations)

If you use this dataset please cite:

```
@InProceedings{armeni_iccv19,
	title ={3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera},
	author = {Iro Armeni and Zhi-Yang He and JunYoung Gwak and Amir R. Zamir and Martin Fischer and Jitendra Malik and Silvio Savarese},
	booktitle = {Proceedings of the IEEE International Conference on Computer Vision},
	year = {2019}
}
```

and if you use the raw data from Gibson Database please cite:

```
@inproceedings{xiazamirhe2018gibsonenv,
  title={Gibson env: real-world perception for embodied agents},
  author={Xia, Fei and R. Zamir, Amir and He, Zhi-Yang and Sax, Alexander and Malik, Jitendra and Savarese, Silvio},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2018 IEEE Conference on},
  year={2018},
  organization={IEEE}
}
```

Dataset Structure
-----------------

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#dataset-structure)

The 3D Scene Graph is composed of 4 layers: [`building`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#building), [`room`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#room), [`object`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#object), and [`camera`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#camera). Below is a description of the semantic information per layer.

### Building

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#building)

```
floor_area       : 2D floor area (in sq.meters)
function         : function of building
gibson_split     : Gibson split (tiny, medium, large)
id               : unique building id
name             : name of gibson model
num_cameras      : number of panoramic cameras in the model
num_floors       : number of floors in the building
num_objects      : number of objects in the building
num_rooms        : number of rooms in the building
reference_point  : building reference point
size             : 3D Size of building (XYZ, in meters)
volume           : 3D volume of building computed from 3D convex hull (in cubic meters)
voxel_size       : size of voxel (in meters)
voxel_centers    : 3D coordinates of voxel centers (Nx3)
voxel_resolution : Number of voxels per axis (k x l x m)
        
room             : 3D Scene Gaph layer for rooms
object           : 3D Scene Gaph layer for objects
camera           : 3D Scene Gaph layer for cameras
```

### Room

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#room)

```
floor_area         : 2D floor area (in sq.meters)
floor_number       : index of floor that contains the space
id                 : unique space id per building
location           : 3D coordinates of room center's location
inst_segmentation  : building face inidices that correspond to this room (face indices correspond to the raw *mesh.obj* provided in Gibson database)
scene_category     : function of this room
size               : 3D Size of room (XYZ, in meters)
voxel_occupancy    : building's voxel indices that correspond to this room (the voxel grid is defined by the building attributes *voxel_size*, *voxel_centers*, and *voxel_resolution*)
volume             : 3D volume of room computed from 3D convex hull (in cubic meters)
parent_building    : parent building that contains this room
```

### Object

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#object)

```
action_affordance  : list of possible actions
floor_area         : 2D floor area in sq.meters
surface_coverage   : total surface coverage in sq.meters
class_*            : object label
id                 : unique object id per building
location           : 3D coordinates of object center's location
material**         : list of main object materials 
size               : 3D Size of object (XYZ, in meters)
inst_segmentation  : building face inidices that correspond to this object (face indices correspond to the raw *mesh.obj* provided in Gibson database)
tactile_texture*** : main tactile texture (can be None)
visual_texture***  : main visible texture (can be None)
volume             : 3D volume of object computed from 3D convex hull (cubic meters)
voxel_occupancy    : building's voxel indices that correspond to this object (the voxel grid is defined by the building attributes *voxel_size*, *voxel_centers*, and *voxel_resolution*)
parent_room        : parent room that contains this object
```

*   Object labels follow the ["COCO"](http://cocodataset.org/#home) dataset \[2\] categorization. \*\* Material labels follow the ["Materials in Context"](http://opensurfaces.cs.cornell.edu/publications/minc/) database \[3\] categorization. \*\*\* Tactile and visual texture labels follow the ["Describable Textures Dataset"](http://www.robots.ox.ac.uk/~vgg/data/dtd/) \[4\] categorization.

### Camera

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#camera)

```
name        : name of camera
id          : unique camera id
FOV         : camera field of view
location    : 3D location of camera in the model
rotation    : rotation of camera (quaternion)
modality    : camera modality (e.g., RGB, grayscale, depth, etc.)
resolution  : camera resolution
parent_room : parent room that contains this camera
```

Tools & Dependencies
--------------------

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#tools--dependencies)

We provide a loading function in `tools/load.py`, which requires `Python 3.5` and the packages: `trimesh, PIL`. You can run this function with the `tools/load.sh` script - remember to change the system paths to match your configuration where applicable. In the `tools` folder there is the `palette.txt` file that contains a list of distinct RGB colors used for visualization purposes, and the `dictionaries.csv` file that contains a list of the category subsets of each database we use that are present in the dataset (e.g., the object classes from COCO present in the tiny Gibson models, etc.).

Automatic Labeling & 3D Scene Graph Generation
----------------------------------------------

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#automatic-labeling--3d-scene-graph-generation)

The automatic labeling and 3D Scene Graph generation pipeline is included in the `source` folder. The code has been tested with `Python 3.6.8`. All required dependencies can be found in `requirements.txt`. Install them by:

```
pip install -r $3DSceneGraph/requirements.txt
```

Inside `source` there are three folders, which correspond to the three main steps of the method:

### 1\. Framing

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#1-framing)

First sample rectilinear frames on the equirectangular images (`pano2rectilinear`) and, after inferring the instance segmentations for each of this frames with the method of your choice, use `pano_aggregation` to aggregate the predictions on the equirectangular image. Each folder contains a shell script that you can run to process each step. The file `detections_format.txt` contains a description of the format of the output file of the instance segmentation.

### 2\. Multiview Consistency

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#2-multiview-consistency)

This step aggregates all panorama instance segmentations on the 3D mesh (`multiview_consistency`). Run the included shell script to start the process.

### 3\. 3D Scene Graph Generation

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#3-3d-scene-graph-generation)

Once the previous steps are finalized, this step will compute attributes and relationships, essentially building the 3D Scene Graph. Certain attributes are not computed analytically, and are provided as input to this step in the form of `.csv` files. You can ommit this if you do not have the ability to compute them otherwise. These are: object `material`, object `texture`, room `scene_category`, room `inst_segmentation`, room `floor_number`, building `gibson_split`, building `function`, and building `num_floors`. Included are examples of the specific file formats for the tiny Gibson split (`model_data.csv`, `object_data.csv`).

#### References

[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#references)

\[1\] Xia, Fei, et al. "Gibson env: Real-world perception for embodied agents." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018. \[2\] Lin, Tsung-Yi, et al. "Microsoft coco: Common objects in context." European conference on computer vision. Springer, Cham, 2014. \[3\] Bell, Sean, et al. "Material recognition in the wild with the materials in context database." Proceedings of the IEEE conference on computer vision and pattern recognition. 2015. \[4\] Cimpoi, Mircea, et al. "Describing textures in the wild." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2014.

## Metadata

```json
{
  "title": "GitHub - StanfordVL/3DSceneGraph: The data skeleton from \"3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera\" http://3dscenegraph.stanford.edu",
  "description": "The data skeleton from \"3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera\" http://3dscenegraph.stanford.edu - StanfordVL/3DSceneGraph",
  "url": "https://github.com/StanfordVL/3DSceneGraph?screenshot=true",
  "content": "3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera\n-----------------------------------------------------------------------\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#3d-scene-graph-a-structure-for-unified-semantics-3d-space-and-camera)\n\n[![Image 6](https://camo.githubusercontent.com/b6e842e453101747e563c5caf5418112fedc37c78506156a0546f819fc92b3e9/68747470733a2f2f33647363656e6567726170682e7374616e666f72642e6564752f696d616765732f33647363656e6567726170682e706e67)](https://camo.githubusercontent.com/b6e842e453101747e563c5caf5418112fedc37c78506156a0546f819fc92b3e9/68747470733a2f2f33647363656e6567726170682e7374616e666f72642e6564752f696d616765732f33647363656e6567726170682e706e67)\n\nOverview\n--------\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#overview)\n\nThe 3D Scene Graph provides semantic data for models in the [Gibson environment](http://gibsonenv.stanford.edu/) \\[1\\] that corresponds to the structure proposed in [3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera](http://3dscenegraph.stanford.edu/). The semantic information for models in the tiny Gibson split is verified via crowdsourcing and contains all 3D Scene Graph attributes. For these models we provide both the automated and verified outputs. For the rest of them, semantic information is the output of automated modules and does not include modalities that depend solely on manual input (e.g., object materials and textures). You can learn more about 3D Scene Graph and interact with the semantic data here: [http://3dscenegraph.stanford.edu](http://3dscenegraph.stanford.edu/)\n\nDownload\n--------\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#download)\n\nYou can download the 3D Scene Graph data from the link below. The link will first take you to a license agreement, and then to the data. The data per model contains only semantics and is provided in the [compressed _.npz_ format](https://docs.scipy.org/doc/numpy/reference/generated/numpy.lib.format.html). To download the raw data visit the [Gibson Environment's database](http://gibsonenv.stanford.edu/database/) and agree to their terms of use. A [loading function](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#tools_&_dependencies) that returns the data in the 3D Scene graph structure is included in the 'tools/' folder. Semantics per model correspond to the `mesh.obj` 3D meshes and the `pano/rgb` panoramas of the Gibson database. To learn more about the type of semantics included in 3D Scene Graph, see [Dataset Structure](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#dataset-structure).\n\n### [\\[ Download 3D Scene Graph \\]](https://redivis.com/datasets/1kf9-cfjvtqc7q)\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#-download-3d-scene-graph-)\n\n#### Data Note: Our current release includes the tiny and medium Gibson splits. The rest of the models will follow shortly.\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#data-note-our-current-release-includes-the-tiny-and-medium-gibson-splits-the-rest-of-the-models-will-follow-shortly)\n\n#### License Note: The dataset license is included in the above link. The license in this repository covers only the provided software. Note that it allows only non-commercial research use.\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#license-note-the-dataset-license-is-included-in-the-above-link-the-license-in-this-repository-covers-only-the-provided-software-note-that-it-allows-only-non-commercial-research-use)\n\nCitations\n---------\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#citations)\n\nIf you use this dataset please cite:\n\n```\n@InProceedings{armeni_iccv19,\n\ttitle ={3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera},\n\tauthor = {Iro Armeni and Zhi-Yang He and JunYoung Gwak and Amir R. Zamir and Martin Fischer and Jitendra Malik and Silvio Savarese},\n\tbooktitle = {Proceedings of the IEEE International Conference on Computer Vision},\n\tyear = {2019}\n}\n```\n\nand if you use the raw data from Gibson Database please cite:\n\n```\n@inproceedings{xiazamirhe2018gibsonenv,\n  title={Gibson env: real-world perception for embodied agents},\n  author={Xia, Fei and R. Zamir, Amir and He, Zhi-Yang and Sax, Alexander and Malik, Jitendra and Savarese, Silvio},\n  booktitle={Computer Vision and Pattern Recognition (CVPR), 2018 IEEE Conference on},\n  year={2018},\n  organization={IEEE}\n}\n```\n\nDataset Structure\n-----------------\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#dataset-structure)\n\nThe 3D Scene Graph is composed of 4 layers: [`building`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#building), [`room`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#room), [`object`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#object), and [`camera`](https://github.com/StanfordVL/3DSceneGraph/blob/master/README.md#camera). Below is a description of the semantic information per layer.\n\n### Building\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#building)\n\n```\nfloor_area       : 2D floor area (in sq.meters)\nfunction         : function of building\ngibson_split     : Gibson split (tiny, medium, large)\nid               : unique building id\nname             : name of gibson model\nnum_cameras      : number of panoramic cameras in the model\nnum_floors       : number of floors in the building\nnum_objects      : number of objects in the building\nnum_rooms        : number of rooms in the building\nreference_point  : building reference point\nsize             : 3D Size of building (XYZ, in meters)\nvolume           : 3D volume of building computed from 3D convex hull (in cubic meters)\nvoxel_size       : size of voxel (in meters)\nvoxel_centers    : 3D coordinates of voxel centers (Nx3)\nvoxel_resolution : Number of voxels per axis (k x l x m)\n        \nroom             : 3D Scene Gaph layer for rooms\nobject           : 3D Scene Gaph layer for objects\ncamera           : 3D Scene Gaph layer for cameras\n```\n\n### Room\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#room)\n\n```\nfloor_area         : 2D floor area (in sq.meters)\nfloor_number       : index of floor that contains the space\nid                 : unique space id per building\nlocation           : 3D coordinates of room center's location\ninst_segmentation  : building face inidices that correspond to this room (face indices correspond to the raw *mesh.obj* provided in Gibson database)\nscene_category     : function of this room\nsize               : 3D Size of room (XYZ, in meters)\nvoxel_occupancy    : building's voxel indices that correspond to this room (the voxel grid is defined by the building attributes *voxel_size*, *voxel_centers*, and *voxel_resolution*)\nvolume             : 3D volume of room computed from 3D convex hull (in cubic meters)\nparent_building    : parent building that contains this room\n```\n\n### Object\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#object)\n\n```\naction_affordance  : list of possible actions\nfloor_area         : 2D floor area in sq.meters\nsurface_coverage   : total surface coverage in sq.meters\nclass_*            : object label\nid                 : unique object id per building\nlocation           : 3D coordinates of object center's location\nmaterial**         : list of main object materials \nsize               : 3D Size of object (XYZ, in meters)\ninst_segmentation  : building face inidices that correspond to this object (face indices correspond to the raw *mesh.obj* provided in Gibson database)\ntactile_texture*** : main tactile texture (can be None)\nvisual_texture***  : main visible texture (can be None)\nvolume             : 3D volume of object computed from 3D convex hull (cubic meters)\nvoxel_occupancy    : building's voxel indices that correspond to this object (the voxel grid is defined by the building attributes *voxel_size*, *voxel_centers*, and *voxel_resolution*)\nparent_room        : parent room that contains this object\n```\n\n*   Object labels follow the [\"COCO\"](http://cocodataset.org/#home) dataset \\[2\\] categorization. \\*\\* Material labels follow the [\"Materials in Context\"](http://opensurfaces.cs.cornell.edu/publications/minc/) database \\[3\\] categorization. \\*\\*\\* Tactile and visual texture labels follow the [\"Describable Textures Dataset\"](http://www.robots.ox.ac.uk/~vgg/data/dtd/) \\[4\\] categorization.\n\n### Camera\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#camera)\n\n```\nname        : name of camera\nid          : unique camera id\nFOV         : camera field of view\nlocation    : 3D location of camera in the model\nrotation    : rotation of camera (quaternion)\nmodality    : camera modality (e.g., RGB, grayscale, depth, etc.)\nresolution  : camera resolution\nparent_room : parent room that contains this camera\n```\n\nTools & Dependencies\n--------------------\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#tools--dependencies)\n\nWe provide a loading function in `tools/load.py`, which requires `Python 3.5` and the packages: `trimesh, PIL`. You can run this function with the `tools/load.sh` script - remember to change the system paths to match your configuration where applicable. In the `tools` folder there is the `palette.txt` file that contains a list of distinct RGB colors used for visualization purposes, and the `dictionaries.csv` file that contains a list of the category subsets of each database we use that are present in the dataset (e.g., the object classes from COCO present in the tiny Gibson models, etc.).\n\nAutomatic Labeling & 3D Scene Graph Generation\n----------------------------------------------\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#automatic-labeling--3d-scene-graph-generation)\n\nThe automatic labeling and 3D Scene Graph generation pipeline is included in the `source` folder. The code has been tested with `Python 3.6.8`. All required dependencies can be found in `requirements.txt`. Install them by:\n\n```\npip install -r $3DSceneGraph/requirements.txt\n```\n\nInside `source` there are three folders, which correspond to the three main steps of the method:\n\n### 1\\. Framing\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#1-framing)\n\nFirst sample rectilinear frames on the equirectangular images (`pano2rectilinear`) and, after inferring the instance segmentations for each of this frames with the method of your choice, use `pano_aggregation` to aggregate the predictions on the equirectangular image. Each folder contains a shell script that you can run to process each step. The file `detections_format.txt` contains a description of the format of the output file of the instance segmentation.\n\n### 2\\. Multiview Consistency\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#2-multiview-consistency)\n\nThis step aggregates all panorama instance segmentations on the 3D mesh (`multiview_consistency`). Run the included shell script to start the process.\n\n### 3\\. 3D Scene Graph Generation\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#3-3d-scene-graph-generation)\n\nOnce the previous steps are finalized, this step will compute attributes and relationships, essentially building the 3D Scene Graph. Certain attributes are not computed analytically, and are provided as input to this step in the form of `.csv` files. You can ommit this if you do not have the ability to compute them otherwise. These are: object `material`, object `texture`, room `scene_category`, room `inst_segmentation`, room `floor_number`, building `gibson_split`, building `function`, and building `num_floors`. Included are examples of the specific file formats for the tiny Gibson split (`model_data.csv`, `object_data.csv`).\n\n#### References\n\n[](https://github.com/StanfordVL/3DSceneGraph?screenshot=true#references)\n\n\\[1\\] Xia, Fei, et al. \"Gibson env: Real-world perception for embodied agents.\" Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018. \\[2\\] Lin, Tsung-Yi, et al. \"Microsoft coco: Common objects in context.\" European conference on computer vision. Springer, Cham, 2014. \\[3\\] Bell, Sean, et al. \"Material recognition in the wild with the materials in context database.\" Proceedings of the IEEE conference on computer vision and pattern recognition. 2015. \\[4\\] Cimpoi, Mircea, et al. \"Describing textures in the wild.\" Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2014.",
  "usage": {
    "tokens": 3113
  }
}
```
