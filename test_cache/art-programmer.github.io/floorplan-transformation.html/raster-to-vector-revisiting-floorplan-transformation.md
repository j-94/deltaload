---
title: Raster-to-Vector: Revisiting Floorplan Transformation
description: 
url: http://art-programmer.github.io/floorplan-transformation.html
timestamp: 2025-01-20T15:42:35.284Z
domain: art-programmer.github.io
path: floorplan-transformation.html
---

# Raster-to-Vector: Revisiting Floorplan Transformation



## Content

### Abstract

This paper addresses the problem of converting a rasterized floorplan image into a vector-graphics representation. Unlike existing approaches that rely on a sequence of low-level image processing heuristics, we adopt a learning-based approach. A neural architecture first transforms a rasterized image to a set of junctions that represent low-level geometric and semantic information (e.g., wall corners or door end-points). Integer programming is then formulated to aggregate junctions into a set of simple primitives (e.g., wall lines, door lines, or icon boxes) to produce a vectorized floorplan, while ensuring a topologically and geometrically consistent result. Our algorithm significantly outperforms existing methods and achieves around 90% precision and recall, getting to the range of production-ready performance. The vector representation allows 3D model popup for better indoor scene visualization, direct model manipulation for architectural remodeling, and further computational applications such as data analysis. Our system is efficient: we have converted hundred thousand production-level floorplan images into the vector representation and generated 3D popup models.

## Metadata

```json
{
  "title": "Raster-to-Vector: Revisiting Floorplan Transformation",
  "description": "",
  "url": "http://art-programmer.github.io/floorplan-transformation.html",
  "content": "### Abstract\n\nThis paper addresses the problem of converting a rasterized floorplan image into a vector-graphics representation. Unlike existing approaches that rely on a sequence of low-level image processing heuristics, we adopt a learning-based approach. A neural architecture first transforms a rasterized image to a set of junctions that represent low-level geometric and semantic information (e.g., wall corners or door end-points). Integer programming is then formulated to aggregate junctions into a set of simple primitives (e.g., wall lines, door lines, or icon boxes) to produce a vectorized floorplan, while ensuring a topologically and geometrically consistent result. Our algorithm significantly outperforms existing methods and achieves around 90% precision and recall, getting to the range of production-ready performance. The vector representation allows 3D model popup for better indoor scene visualization, direct model manipulation for architectural remodeling, and further computational applications such as data analysis. Our system is efficient: we have converted hundred thousand production-level floorplan images into the vector representation and generated 3D popup models.",
  "usage": {
    "tokens": 214
  }
}
```
