---
title: Automatic mask generator hq - segment-geospatial
description: 
url: https://samgeo.gishub.org/examples/automatic_mask_generator_hq/
timestamp: 2025-01-20T15:43:02.908Z
domain: samgeo.gishub.org
path: examples_automatic_mask_generator_hq
---

# Automatic mask generator hq - segment-geospatial



## Content

Automatically generating object masks with HQ-SAM[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#automatically-generating-object-masks-with-hq-sam)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 7: image](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/opengeos/segment-geospatial/blob/main/docs/examples/automatic_mask_generator_hq.ipynb) [![Image 8: image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/segment-geospatial/blob/main/docs/examples/automatic_mask_generator_hq.ipynb)

This notebook shows how to segment objects from an image using the High-Quality Segment Anything Model ([HQ-SAM](https://github.com/SysCV/sam-hq)) with a few lines of code.

Install dependencies[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#install-dependencies)
-------------------------------------------------------------------------------------------------------------

Uncomment and run the following cell to install the required dependencies.

In \[ \]:

\# %pip install segment-geospatial

\# %pip install segment-geospatial

In \[ \]:

import os
import leafmap
from samgeo.hq\_sam import (
    SamGeo,
    show\_image,
    download\_file,
    overlay\_images,
    tms\_to\_geotiff,
)

import os import leafmap from samgeo.hq\_sam import ( SamGeo, show\_image, download\_file, overlay\_images, tms\_to\_geotiff, )

Create an interactive map[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#create-an-interactive-map)
-----------------------------------------------------------------------------------------------------------------------

In \[ \]:

m \= leafmap.Map(center\=\[37.8713, \-122.2580\], zoom\=17, height\="800px")
m.add\_basemap("SATELLITE")
m

m = leafmap.Map(center=\[37.8713, -122.2580\], zoom=17, height="800px") m.add\_basemap("SATELLITE") m

Pan and zoom the map to select the area of interest. Use the draw tools to draw a polygon or rectangle on the map

In \[ \]:

if m.user\_roi\_bounds() is not None:
    bbox \= m.user\_roi\_bounds()
else:
    bbox \= \[\-122.2659, 37.8682, \-122.2521, 37.8741\]

if m.user\_roi\_bounds() is not None: bbox = m.user\_roi\_bounds() else: bbox = \[-122.2659, 37.8682, -122.2521, 37.8741\]

Download a sample image[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#download-a-sample-image)
-------------------------------------------------------------------------------------------------------------------

In \[ \]:

image \= "satellite.tif"
tms\_to\_geotiff(output\=image, bbox\=bbox, zoom\=17, source\="Satellite", overwrite\=True)

image = "satellite.tif" tms\_to\_geotiff(output=image, bbox=bbox, zoom=17, source="Satellite", overwrite=True)

You can also use your own image. Uncomment and run the following cell to use your own image.

In \[ \]:

\# image = '/path/to/your/own/image.tif'

\# image = '/path/to/your/own/image.tif'

Display the downloaded image on the map.

In \[ \]:

m.layers\[\-1\].visible \= False
m.add\_raster(image, layer\_name\="Image")
m

m.layers\[-1\].visible = False m.add\_raster(image, layer\_name="Image") m

Initialize SAM class[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#initialize-sam-class)
-------------------------------------------------------------------------------------------------------------

Specify the file path to the model checkpoint. If it is not specified, the model will to downloaded to the working directory.

In \[ \]:

sam \= SamGeo(
    model\_type\="vit\_h",  \# can be vit\_h, vit\_b, vit\_l, vit\_tiny
    sam\_kwargs\=None,
)

sam = SamGeo( model\_type="vit\_h", # can be vit\_h, vit\_b, vit\_l, vit\_tiny sam\_kwargs=None, )

Automatic mask generation[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#automatic-mask-generation)
-----------------------------------------------------------------------------------------------------------------------

Segment the image and save the results to a GeoTIFF file. Set `unique=True` to assign a unique ID to each object.

In \[ \]:

sam.generate(image, output\="masks.tif", foreground\=True, unique\=True)

sam.generate(image, output="masks.tif", foreground=True, unique=True)

In \[ \]:

sam.show\_masks(cmap\="binary\_r")

sam.show\_masks(cmap="binary\_r")

Show the object annotations (objects with random color) on the map.

In \[ \]:

sam.show\_anns(axis\="off", alpha\=1, output\="annotations.tif")

sam.show\_anns(axis="off", alpha=1, output="annotations.tif")

Compare images with a slider.

In \[ \]:

leafmap.image\_comparison(
    "satellite.tif",
    "annotations.tif",
    label1\="Satellite Image",
    label2\="Image Segmentation",
)

leafmap.image\_comparison( "satellite.tif", "annotations.tif", label1="Satellite Image", label2="Image Segmentation", )

In \[ \]:

m.add\_raster("annotations.tif", alpha\=0.5, layer\_name\="Masks")
m

m.add\_raster("annotations.tif", alpha=0.5, layer\_name="Masks") m

Convert the object annotations to vector format, such as GeoPackage, Shapefile, or GeoJSON.

In \[ \]:

sam.tiff\_to\_vector("masks.tif", "masks.gpkg")

sam.tiff\_to\_vector("masks.tif", "masks.gpkg")

Automatic mask generation options[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#automatic-mask-generation-options)
---------------------------------------------------------------------------------------------------------------------------------------

There are several tunable parameters in automatic mask generation that control how densely points are sampled and what the thresholds are for removing low quality or duplicate masks. Additionally, generation can be automatically run on crops of the image to get improved performance on smaller objects, and post-processing can remove stray pixels and holes. Here is an example configuration that samples more masks:

In \[ \]:

sam\_kwargs \= {
    "points\_per\_side": 32,
    "pred\_iou\_thresh": 0.86,
    "stability\_score\_thresh": 0.92,
    "crop\_n\_layers": 1,
    "crop\_n\_points\_downscale\_factor": 2,
    "min\_mask\_region\_area": 100,
}

sam\_kwargs = { "points\_per\_side": 32, "pred\_iou\_thresh": 0.86, "stability\_score\_thresh": 0.92, "crop\_n\_layers": 1, "crop\_n\_points\_downscale\_factor": 2, "min\_mask\_region\_area": 100, }

In \[ \]:

sam \= SamGeo(
    model\_type\="vit\_h",
    sam\_kwargs\=sam\_kwargs,
)

sam = SamGeo( model\_type="vit\_h", sam\_kwargs=sam\_kwargs, )

In \[ \]:

sam.generate(image, output\="masks2.tif", foreground\=True)

sam.generate(image, output="masks2.tif", foreground=True)

In \[ \]:

sam.show\_masks(cmap\="binary\_r")

sam.show\_masks(cmap="binary\_r")

In \[ \]:

sam.show\_anns(axis\="off", opacity\=1, output\="annotations2.tif")

sam.show\_anns(axis="off", opacity=1, output="annotations2.tif")

Compare images with a slider.

In \[ \]:

leafmap.image\_comparison(
    image,
    "annotations.tif",
    label1\="Image",
    label2\="Image Segmentation",
)

leafmap.image\_comparison( image, "annotations.tif", label1="Image", label2="Image Segmentation", )

Overlay the annotations on the image and use the slider to change the opacity interactively.

In \[ \]:

overlay\_images(image, "annotations2.tif", backend\="TkAgg")

overlay\_images(image, "annotations2.tif", backend="TkAgg")

![Image 9](https://i.imgur.com/I1IhDgz.gif)

## Metadata

```json
{
  "title": "Automatic mask generator hq - segment-geospatial",
  "description": "",
  "url": "https://samgeo.gishub.org/examples/automatic_mask_generator_hq/",
  "content": "Automatically generating object masks with HQ-SAM[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#automatically-generating-object-masks-with-hq-sam)\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[![Image 7: image](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/opengeos/segment-geospatial/blob/main/docs/examples/automatic_mask_generator_hq.ipynb) [![Image 8: image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/segment-geospatial/blob/main/docs/examples/automatic_mask_generator_hq.ipynb)\n\nThis notebook shows how to segment objects from an image using the High-Quality Segment Anything Model ([HQ-SAM](https://github.com/SysCV/sam-hq)) with a few lines of code.\n\nInstall dependencies[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#install-dependencies)\n-------------------------------------------------------------------------------------------------------------\n\nUncomment and run the following cell to install the required dependencies.\n\nIn \\[ \\]:\n\n\\# %pip install segment-geospatial\n\n\\# %pip install segment-geospatial\n\nIn \\[ \\]:\n\nimport os\nimport leafmap\nfrom samgeo.hq\\_sam import (\n    SamGeo,\n    show\\_image,\n    download\\_file,\n    overlay\\_images,\n    tms\\_to\\_geotiff,\n)\n\nimport os import leafmap from samgeo.hq\\_sam import ( SamGeo, show\\_image, download\\_file, overlay\\_images, tms\\_to\\_geotiff, )\n\nCreate an interactive map[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#create-an-interactive-map)\n-----------------------------------------------------------------------------------------------------------------------\n\nIn \\[ \\]:\n\nm \\= leafmap.Map(center\\=\\[37.8713, \\-122.2580\\], zoom\\=17, height\\=\"800px\")\nm.add\\_basemap(\"SATELLITE\")\nm\n\nm = leafmap.Map(center=\\[37.8713, -122.2580\\], zoom=17, height=\"800px\") m.add\\_basemap(\"SATELLITE\") m\n\nPan and zoom the map to select the area of interest. Use the draw tools to draw a polygon or rectangle on the map\n\nIn \\[ \\]:\n\nif m.user\\_roi\\_bounds() is not None:\n    bbox \\= m.user\\_roi\\_bounds()\nelse:\n    bbox \\= \\[\\-122.2659, 37.8682, \\-122.2521, 37.8741\\]\n\nif m.user\\_roi\\_bounds() is not None: bbox = m.user\\_roi\\_bounds() else: bbox = \\[-122.2659, 37.8682, -122.2521, 37.8741\\]\n\nDownload a sample image[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#download-a-sample-image)\n-------------------------------------------------------------------------------------------------------------------\n\nIn \\[ \\]:\n\nimage \\= \"satellite.tif\"\ntms\\_to\\_geotiff(output\\=image, bbox\\=bbox, zoom\\=17, source\\=\"Satellite\", overwrite\\=True)\n\nimage = \"satellite.tif\" tms\\_to\\_geotiff(output=image, bbox=bbox, zoom=17, source=\"Satellite\", overwrite=True)\n\nYou can also use your own image. Uncomment and run the following cell to use your own image.\n\nIn \\[ \\]:\n\n\\# image = '/path/to/your/own/image.tif'\n\n\\# image = '/path/to/your/own/image.tif'\n\nDisplay the downloaded image on the map.\n\nIn \\[ \\]:\n\nm.layers\\[\\-1\\].visible \\= False\nm.add\\_raster(image, layer\\_name\\=\"Image\")\nm\n\nm.layers\\[-1\\].visible = False m.add\\_raster(image, layer\\_name=\"Image\") m\n\nInitialize SAM class[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#initialize-sam-class)\n-------------------------------------------------------------------------------------------------------------\n\nSpecify the file path to the model checkpoint. If it is not specified, the model will to downloaded to the working directory.\n\nIn \\[ \\]:\n\nsam \\= SamGeo(\n    model\\_type\\=\"vit\\_h\",  \\# can be vit\\_h, vit\\_b, vit\\_l, vit\\_tiny\n    sam\\_kwargs\\=None,\n)\n\nsam = SamGeo( model\\_type=\"vit\\_h\", # can be vit\\_h, vit\\_b, vit\\_l, vit\\_tiny sam\\_kwargs=None, )\n\nAutomatic mask generation[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#automatic-mask-generation)\n-----------------------------------------------------------------------------------------------------------------------\n\nSegment the image and save the results to a GeoTIFF file. Set `unique=True` to assign a unique ID to each object.\n\nIn \\[ \\]:\n\nsam.generate(image, output\\=\"masks.tif\", foreground\\=True, unique\\=True)\n\nsam.generate(image, output=\"masks.tif\", foreground=True, unique=True)\n\nIn \\[ \\]:\n\nsam.show\\_masks(cmap\\=\"binary\\_r\")\n\nsam.show\\_masks(cmap=\"binary\\_r\")\n\nShow the object annotations (objects with random color) on the map.\n\nIn \\[ \\]:\n\nsam.show\\_anns(axis\\=\"off\", alpha\\=1, output\\=\"annotations.tif\")\n\nsam.show\\_anns(axis=\"off\", alpha=1, output=\"annotations.tif\")\n\nCompare images with a slider.\n\nIn \\[ \\]:\n\nleafmap.image\\_comparison(\n    \"satellite.tif\",\n    \"annotations.tif\",\n    label1\\=\"Satellite Image\",\n    label2\\=\"Image Segmentation\",\n)\n\nleafmap.image\\_comparison( \"satellite.tif\", \"annotations.tif\", label1=\"Satellite Image\", label2=\"Image Segmentation\", )\n\nIn \\[ \\]:\n\nm.add\\_raster(\"annotations.tif\", alpha\\=0.5, layer\\_name\\=\"Masks\")\nm\n\nm.add\\_raster(\"annotations.tif\", alpha=0.5, layer\\_name=\"Masks\") m\n\nConvert the object annotations to vector format, such as GeoPackage, Shapefile, or GeoJSON.\n\nIn \\[ \\]:\n\nsam.tiff\\_to\\_vector(\"masks.tif\", \"masks.gpkg\")\n\nsam.tiff\\_to\\_vector(\"masks.tif\", \"masks.gpkg\")\n\nAutomatic mask generation options[¶](https://samgeo.gishub.org/examples/automatic_mask_generator_hq/#automatic-mask-generation-options)\n---------------------------------------------------------------------------------------------------------------------------------------\n\nThere are several tunable parameters in automatic mask generation that control how densely points are sampled and what the thresholds are for removing low quality or duplicate masks. Additionally, generation can be automatically run on crops of the image to get improved performance on smaller objects, and post-processing can remove stray pixels and holes. Here is an example configuration that samples more masks:\n\nIn \\[ \\]:\n\nsam\\_kwargs \\= {\n    \"points\\_per\\_side\": 32,\n    \"pred\\_iou\\_thresh\": 0.86,\n    \"stability\\_score\\_thresh\": 0.92,\n    \"crop\\_n\\_layers\": 1,\n    \"crop\\_n\\_points\\_downscale\\_factor\": 2,\n    \"min\\_mask\\_region\\_area\": 100,\n}\n\nsam\\_kwargs = { \"points\\_per\\_side\": 32, \"pred\\_iou\\_thresh\": 0.86, \"stability\\_score\\_thresh\": 0.92, \"crop\\_n\\_layers\": 1, \"crop\\_n\\_points\\_downscale\\_factor\": 2, \"min\\_mask\\_region\\_area\": 100, }\n\nIn \\[ \\]:\n\nsam \\= SamGeo(\n    model\\_type\\=\"vit\\_h\",\n    sam\\_kwargs\\=sam\\_kwargs,\n)\n\nsam = SamGeo( model\\_type=\"vit\\_h\", sam\\_kwargs=sam\\_kwargs, )\n\nIn \\[ \\]:\n\nsam.generate(image, output\\=\"masks2.tif\", foreground\\=True)\n\nsam.generate(image, output=\"masks2.tif\", foreground=True)\n\nIn \\[ \\]:\n\nsam.show\\_masks(cmap\\=\"binary\\_r\")\n\nsam.show\\_masks(cmap=\"binary\\_r\")\n\nIn \\[ \\]:\n\nsam.show\\_anns(axis\\=\"off\", opacity\\=1, output\\=\"annotations2.tif\")\n\nsam.show\\_anns(axis=\"off\", opacity=1, output=\"annotations2.tif\")\n\nCompare images with a slider.\n\nIn \\[ \\]:\n\nleafmap.image\\_comparison(\n    image,\n    \"annotations.tif\",\n    label1\\=\"Image\",\n    label2\\=\"Image Segmentation\",\n)\n\nleafmap.image\\_comparison( image, \"annotations.tif\", label1=\"Image\", label2=\"Image Segmentation\", )\n\nOverlay the annotations on the image and use the slider to change the opacity interactively.\n\nIn \\[ \\]:\n\noverlay\\_images(image, \"annotations2.tif\", backend\\=\"TkAgg\")\n\noverlay\\_images(image, \"annotations2.tif\", backend=\"TkAgg\")\n\n![Image 9](https://i.imgur.com/I1IhDgz.gif)",
  "usage": {
    "tokens": 1976
  }
}
```
