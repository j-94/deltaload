---
title: Embedding projector - visualization of high-dimensional data
description: 
url: https://projector.tensorflow.org/
timestamp: 2025-01-20T16:00:43.763Z
domain: projector.tensorflow.org
path: root
---

# Embedding projector - visualization of high-dimensional data



## Content

\[\[\_text\]\]

\[\[\_charCounterStr\]\]   \[\[label\]\]  \[\[errorMessage\]\]    {{text}} 

 \[\[label\]\] \[\[errorMessage\]\] 

BOOKMARKS (\[\[savedStates.length\]\]) Open this drawer to save a set of views of the projection, including selected points. A file containing the bookmarks can then be saved and later loaded to view them.

No bookmarks yet, upload a bookmarks file or add a new bookmark by clicking the "+" below.

\[\[item.label\]\]

\[\[item.count\]\]

\[\[renderInfo.thresholds.0.value\]\]

\[\[\_getLastThreshold(renderInfo.thresholds)\]\]

DATA

\[\[item\]\] \[\[item.name\]\] \[\[item.shape.0\]\]x\[\[item.shape.1\]\]

\[\[item\]\] \[\[item.name\]\] \[\[item.desc\]\]

Use categorical coloring For metadata fields that have many unique values we use a gradient color map by default. This checkbox allows you to force categorical coloring by a given metadata field.

\[\[item\]\]

\[\[item\]\]

Load data from your computer Load Publish your embedding visualization and data Publish Download the metadata with applied modifications Download [](https://projector.tensorflow.org/#) Label selected metadata Label

Load data from your computer
----------------------------

**Step 1: Load a TSV file of vectors.**

Example of 3 vectors with dimension 4:

0.1\\t0.2\\t0.5\\t0.9  
0.2\\t0.1\\t5.0\\t0.2  
0.4\\t0.1\\t7.0\\t0.8

Choose file 

**Step 2** (optional): **Load a TSV file of metadata.**

Example of 3 data points and 2 columns.  
_Note: If there is more than one column, the first row will be parsed as column labels._

**Pokémon\\tSpecies**  
Wartortle\\tTurtle  
Venusaur\\tSeed  
Charmeleon\\tFlame

Choose file 

Click outside to dismiss.

Publish your embedding visualization and data
---------------------------------------------

If you'd like to share your visualization with the world, follow these simple steps. See [this tutorial](https://www.tensorflow.org/get_started/embedding_viz) for more.

#### Step 1: Make data public

Host tensors, metadata, sprite image, and bookmarks TSV files _publicly_ on the web.

One option is using a [github gist](https://gist.github.com/). If you choose this approach, make sure to link directly to the raw file.

#### Step 2: Projector config

_Optional:_

Metadata

Sprite

Bookmarks

#### Step 3: Host projector config

After you have hosted the projector config JSON file you built above, paste the URL to the config below.

Test your shareable URL

Click outside to dismiss.

Sphereize data The data is normalized by shifting each point by the centroid and making it unit norm.

Checkpoint:

Metadata:

/

/

.\*

Enable/disable regex mode. \[\[message\]\] 

Show All Data Isolate selection Clear selection

\[\[item\]\]

neighbors The number of neighbors (in the original space) to show when clicking on a point.

distance

[COSINE](javascript:void(0);) [EUCLIDEAN](javascript:void(0);)

Nearest points in the original space:

neighbors The number of neighbors (in the selected space) to show when clicking on a point.

{{metadataColumn}} labels (click to apply):

Showing only the first 100 results...

\[\[label\]\]

\[\[item.key\]\]

\[\[item.value\]\]

UMAP

uniform manifold approximation and projection

t-SNE

t-distributed stochastic neighbor embedding

PCA

Principal component analysis

Custom

Search for two vectors upon which to project all points.

Dimension

2D 3D

Neighbors The number of nearest neighbors used to compute the fuzzy simplicial set, which is used to approximate the overall shape of the manifold. The default value is 15. \[\[umapNeighbors\]\]

Run

For faster results, the data will be sampled down to \[\[getUmapSampleSizeText()\]\] points.

[Learn more about UMAP.](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html)

Dimension

2D 3D

Perplexity The most appropriate perplexity value depends on the density of the data. Loosely speaking, a larger / denser dataset requires a larger perplexity. Typical values for perplexity range between 5 and 50.

Learning rate The ideal learning rate often depends on the size of the data, with smaller datasets requiring smaller learning rates.

Supervise The label importance used for supervision, from 0 (disabled) to 100 (full importance).

Run Pause Perturb

Iteration: 0

For faster results, the data will be sampled down to \[\[getTsneSampleSizeText()\]\] points.

[How to use t-SNE effectively.](http://distill.pub/2016/misread-tsne/)

#

Variance (%)

\[\[item.componentNumber\]\]

\[\[item.percVariance\]\]

#

Variance (%)

\[\[item.componentNumber\]\]

\[\[item.percVariance\]\]

#

Variance (%)

\[\[item.componentNumber\]\]

\[\[item.percVariance\]\]

PCA is approximate.

Total variance

For fast results, the data was sampled to \[\[getPcaSampleSizeText()\]\] points and randomly projected down to \[\[getPcaSampledDimText()\]\] dimensions.

\[\[item\]\]

Close

Bounding box selection Edit current selection Enable/disable night mode Enable/disable 3D labels mode

Points: Loading...

Dimension: Loading...

Reset zoom to fit all points

Help with interaction controls.

### 3D controls

**Rotate** Mouse left click.  
**Pan** Mouse right click.  
**Zoom** Mouse wheel.  
Holding **ctrl** reverses the mouse clicks.

### 2D controls

**Pan** Mouse left click.  
**Zoom** Mouse wheel.

Click anywhere to dismiss.

Embedding Projector

[Open documentation](https://projector.tensorflow.org/[[documentationLink]] "Documentation") [Report a bug](https://projector.tensorflow.org/[[bugReportLink]] "Report bug")

Embedding projector - visualization of high-dimensional data
===============

## Metadata

```json
{
  "title": "Embedding projector - visualization of high-dimensional data",
  "description": "",
  "url": "https://projector.tensorflow.org/",
  "content": "\\[\\[\\_text\\]\\]\n\n\\[\\[\\_charCounterStr\\]\\]   \\[\\[label\\]\\]  \\[\\[errorMessage\\]\\]    {{text}} \n\n \\[\\[label\\]\\] \\[\\[errorMessage\\]\\] \n\nBOOKMARKS (\\[\\[savedStates.length\\]\\]) Open this drawer to save a set of views of the projection, including selected points. A file containing the bookmarks can then be saved and later loaded to view them.\n\nNo bookmarks yet, upload a bookmarks file or add a new bookmark by clicking the \"+\" below.\n\n\\[\\[item.label\\]\\]\n\n\\[\\[item.count\\]\\]\n\n\\[\\[renderInfo.thresholds.0.value\\]\\]\n\n\\[\\[\\_getLastThreshold(renderInfo.thresholds)\\]\\]\n\nDATA\n\n\\[\\[item\\]\\] \\[\\[item.name\\]\\] \\[\\[item.shape.0\\]\\]x\\[\\[item.shape.1\\]\\]\n\n\\[\\[item\\]\\] \\[\\[item.name\\]\\] \\[\\[item.desc\\]\\]\n\nUse categorical coloring For metadata fields that have many unique values we use a gradient color map by default. This checkbox allows you to force categorical coloring by a given metadata field.\n\n\\[\\[item\\]\\]\n\n\\[\\[item\\]\\]\n\nLoad data from your computer Load Publish your embedding visualization and data Publish Download the metadata with applied modifications Download [](https://projector.tensorflow.org/#) Label selected metadata Label\n\nLoad data from your computer\n----------------------------\n\n**Step 1: Load a TSV file of vectors.**\n\nExample of 3 vectors with dimension 4:\n\n0.1\\\\t0.2\\\\t0.5\\\\t0.9  \n0.2\\\\t0.1\\\\t5.0\\\\t0.2  \n0.4\\\\t0.1\\\\t7.0\\\\t0.8\n\nChoose file \n\n**Step 2** (optional): **Load a TSV file of metadata.**\n\nExample of 3 data points and 2 columns.  \n_Note: If there is more than one column, the first row will be parsed as column labels._\n\n**Pokémon\\\\tSpecies**  \nWartortle\\\\tTurtle  \nVenusaur\\\\tSeed  \nCharmeleon\\\\tFlame\n\nChoose file \n\nClick outside to dismiss.\n\nPublish your embedding visualization and data\n---------------------------------------------\n\nIf you'd like to share your visualization with the world, follow these simple steps. See [this tutorial](https://www.tensorflow.org/get_started/embedding_viz) for more.\n\n#### Step 1: Make data public\n\nHost tensors, metadata, sprite image, and bookmarks TSV files _publicly_ on the web.\n\nOne option is using a [github gist](https://gist.github.com/). If you choose this approach, make sure to link directly to the raw file.\n\n#### Step 2: Projector config\n\n_Optional:_\n\nMetadata\n\nSprite\n\nBookmarks\n\n#### Step 3: Host projector config\n\nAfter you have hosted the projector config JSON file you built above, paste the URL to the config below.\n\nTest your shareable URL\n\nClick outside to dismiss.\n\nSphereize data The data is normalized by shifting each point by the centroid and making it unit norm.\n\nCheckpoint:\n\nMetadata:\n\n/\n\n/\n\n.\\*\n\nEnable/disable regex mode. \\[\\[message\\]\\] \n\nShow All Data Isolate selection Clear selection\n\n\\[\\[item\\]\\]\n\nneighbors The number of neighbors (in the original space) to show when clicking on a point.\n\ndistance\n\n[COSINE](javascript:void(0);) [EUCLIDEAN](javascript:void(0);)\n\nNearest points in the original space:\n\nneighbors The number of neighbors (in the selected space) to show when clicking on a point.\n\n{{metadataColumn}} labels (click to apply):\n\nShowing only the first 100 results...\n\n\\[\\[label\\]\\]\n\n\\[\\[item.key\\]\\]\n\n\\[\\[item.value\\]\\]\n\nUMAP\n\nuniform manifold approximation and projection\n\nt-SNE\n\nt-distributed stochastic neighbor embedding\n\nPCA\n\nPrincipal component analysis\n\nCustom\n\nSearch for two vectors upon which to project all points.\n\nDimension\n\n2D 3D\n\nNeighbors The number of nearest neighbors used to compute the fuzzy simplicial set, which is used to approximate the overall shape of the manifold. The default value is 15. \\[\\[umapNeighbors\\]\\]\n\nRun\n\nFor faster results, the data will be sampled down to \\[\\[getUmapSampleSizeText()\\]\\] points.\n\n[Learn more about UMAP.](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html)\n\nDimension\n\n2D 3D\n\nPerplexity The most appropriate perplexity value depends on the density of the data. Loosely speaking, a larger / denser dataset requires a larger perplexity. Typical values for perplexity range between 5 and 50.\n\nLearning rate The ideal learning rate often depends on the size of the data, with smaller datasets requiring smaller learning rates.\n\nSupervise The label importance used for supervision, from 0 (disabled) to 100 (full importance).\n\nRun Pause Perturb\n\nIteration: 0\n\nFor faster results, the data will be sampled down to \\[\\[getTsneSampleSizeText()\\]\\] points.\n\n[How to use t-SNE effectively.](http://distill.pub/2016/misread-tsne/)\n\n#\n\nVariance (%)\n\n\\[\\[item.componentNumber\\]\\]\n\n\\[\\[item.percVariance\\]\\]\n\n#\n\nVariance (%)\n\n\\[\\[item.componentNumber\\]\\]\n\n\\[\\[item.percVariance\\]\\]\n\n#\n\nVariance (%)\n\n\\[\\[item.componentNumber\\]\\]\n\n\\[\\[item.percVariance\\]\\]\n\nPCA is approximate.\n\nTotal variance\n\nFor fast results, the data was sampled to \\[\\[getPcaSampleSizeText()\\]\\] points and randomly projected down to \\[\\[getPcaSampledDimText()\\]\\] dimensions.\n\n\\[\\[item\\]\\]\n\nClose\n\nBounding box selection Edit current selection Enable/disable night mode Enable/disable 3D labels mode\n\nPoints: Loading...\n\nDimension: Loading...\n\nReset zoom to fit all points\n\nHelp with interaction controls.\n\n### 3D controls\n\n**Rotate** Mouse left click.  \n**Pan** Mouse right click.  \n**Zoom** Mouse wheel.  \nHolding **ctrl** reverses the mouse clicks.\n\n### 2D controls\n\n**Pan** Mouse left click.  \n**Zoom** Mouse wheel.\n\nClick anywhere to dismiss.\n\nEmbedding Projector\n\n[Open documentation](https://projector.tensorflow.org/[[documentationLink]] \"Documentation\") [Report a bug](https://projector.tensorflow.org/[[bugReportLink]] \"Report bug\")\n\nEmbedding projector - visualization of high-dimensional data\n===============",
  "usage": {
    "tokens": 1428
  }
}
```
