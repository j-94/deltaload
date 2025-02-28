---
title: JSON Canvas
description: JSON Canvas SpecVersion 1.0 — 2024-03-11Top levelThe top level of JSON Canvas contains two arrays:  nodes (optional, array of nodes)  edges (optional, array ...
url: https://jsoncanvas.org/spec/1.0/
timestamp: 2025-01-20T15:59:42.030Z
domain: jsoncanvas.org
path: spec_1.0
---

# JSON Canvas


JSON Canvas SpecVersion 1.0 — 2024-03-11Top levelThe top level of JSON Canvas contains two arrays:  nodes (optional, array of nodes)  edges (optional, array ...


## Content

JSON Canvas Spec
----------------

Version 1.0 — 2024-03-11

Top level
---------

The top level of JSON Canvas contains two arrays:

*   `nodes` (optional, array of nodes)
*   `edges` (optional, array of edges)

Nodes
-----

Nodes are objects within the canvas. Nodes may be text, files, links, or groups.

Nodes are placed in the array in ascending order by z-index. The first node in the array should be displayed below all other nodes, and the last node in the array should be displayed on top of all other nodes.

### Generic node

All nodes include the following attributes:

*   `id` (required, string) is a unique ID for the node.
*   `type` (required, string) is the node type.
    *   `text`
    *   `file`
    *   `link`
    *   `group`
*   `x` (required, integer) is the `x` position of the node in pixels.
*   `y` (required, integer) is the `y` position of the node in pixels.
*   `width` (required, integer) is the width of the node in pixels.
*   `height` (required, integer) is the height of the node in pixels.
*   `color` (optional, `canvasColor`) is the color of the node, see the Color section.

### Text type nodes

Text type nodes store text. Along with generic node attributes, text nodes include the following attribute:

*   `text` (required, string) in plain text with Markdown syntax.

### File type nodes

File type nodes reference other files or attachments, such as images, videos, etc. Along with generic node attributes, file nodes include the following attributes:

*   `file` (required, string) is the path to the file within the system.
*   `subpath` (optional, string) is a subpath that may link to a heading or a block. Always starts with a `#`.

### Link type nodes

Link type nodes reference a URL. Along with generic node attributes, link nodes include the following attribute:

*   `url` (required, string)

### Group type nodes

Group type nodes are used as a visual container for nodes within it. Along with generic node attributes, group nodes include the following attributes:

*   `label` (optional, string) is a text label for the group.
*   `background` (optional, string) is the path to the background image.
*   `backgroundStyle` (optional, string) is the rendering style of the background image. Valid values:
    *   `cover` fills the entire width and height of the node.
    *   `ratio` maintains the aspect ratio of the background image.
    *   `repeat` repeats the image as a pattern in both x/y directions.

Edges
-----

Edges are lines that connect one node to another.

*   `id` (required, string) is a unique ID for the edge.
*   `fromNode` (required, string) is the node `id` where the connection starts.
*   `fromSide` (optional, string) is the side where this edge starts. Valid values:
    *   `top`
    *   `right`
    *   `bottom`
    *   `left`
*   `fromEnd` (optional, string) is the shape of the endpoint at the edge start. Defaults to `none` if not specified. Valid values:
    *   `none`
    *   `arrow`
*   `toNode` (required, string) is the node `id` where the connection ends.
*   `toSide` (optional, string) is the side where this edge ends. Valid values:
    *   `top`
    *   `right`
    *   `bottom`
    *   `left`
*   `toEnd` (optional, string) is the shape of the endpoint at the edge end. Defaults to `arrow` if not specified. Valid values:
    *   `none`
    *   `arrow`
*   `color` (optional, `canvasColor`) is the color of the line, see the Color section.
*   `label` (optional, string) is a text label for the edge.

Color
-----

The `canvasColor` type is used to encode color data for nodes and edges. Colors attributes expect a string. Colors can be specified in hex format e.g. `"#FF0000"`, or using one of the preset colors, e.g. `"1"` for red. Six preset colors exist, mapped to the following numbers:

*   `"1"` red
*   `"2"` orange
*   `"3"` yellow
*   `"4"` green
*   `"5"` cyan
*   `"6"` purple

Specific values for the preset colors are intentionally not defined so that applications can tailor the presets to their specific brand colors or color scheme.

## Metadata

```json
{
  "title": "JSON Canvas",
  "description": "JSON Canvas SpecVersion 1.0 — 2024-03-11Top levelThe top level of JSON Canvas contains two arrays:  nodes (optional, array of nodes)  edges (optional, array ...",
  "url": "https://jsoncanvas.org/spec/1.0/",
  "content": "JSON Canvas Spec\n----------------\n\nVersion 1.0 — 2024-03-11\n\nTop level\n---------\n\nThe top level of JSON Canvas contains two arrays:\n\n*   `nodes` (optional, array of nodes)\n*   `edges` (optional, array of edges)\n\nNodes\n-----\n\nNodes are objects within the canvas. Nodes may be text, files, links, or groups.\n\nNodes are placed in the array in ascending order by z-index. The first node in the array should be displayed below all other nodes, and the last node in the array should be displayed on top of all other nodes.\n\n### Generic node\n\nAll nodes include the following attributes:\n\n*   `id` (required, string) is a unique ID for the node.\n*   `type` (required, string) is the node type.\n    *   `text`\n    *   `file`\n    *   `link`\n    *   `group`\n*   `x` (required, integer) is the `x` position of the node in pixels.\n*   `y` (required, integer) is the `y` position of the node in pixels.\n*   `width` (required, integer) is the width of the node in pixels.\n*   `height` (required, integer) is the height of the node in pixels.\n*   `color` (optional, `canvasColor`) is the color of the node, see the Color section.\n\n### Text type nodes\n\nText type nodes store text. Along with generic node attributes, text nodes include the following attribute:\n\n*   `text` (required, string) in plain text with Markdown syntax.\n\n### File type nodes\n\nFile type nodes reference other files or attachments, such as images, videos, etc. Along with generic node attributes, file nodes include the following attributes:\n\n*   `file` (required, string) is the path to the file within the system.\n*   `subpath` (optional, string) is a subpath that may link to a heading or a block. Always starts with a `#`.\n\n### Link type nodes\n\nLink type nodes reference a URL. Along with generic node attributes, link nodes include the following attribute:\n\n*   `url` (required, string)\n\n### Group type nodes\n\nGroup type nodes are used as a visual container for nodes within it. Along with generic node attributes, group nodes include the following attributes:\n\n*   `label` (optional, string) is a text label for the group.\n*   `background` (optional, string) is the path to the background image.\n*   `backgroundStyle` (optional, string) is the rendering style of the background image. Valid values:\n    *   `cover` fills the entire width and height of the node.\n    *   `ratio` maintains the aspect ratio of the background image.\n    *   `repeat` repeats the image as a pattern in both x/y directions.\n\nEdges\n-----\n\nEdges are lines that connect one node to another.\n\n*   `id` (required, string) is a unique ID for the edge.\n*   `fromNode` (required, string) is the node `id` where the connection starts.\n*   `fromSide` (optional, string) is the side where this edge starts. Valid values:\n    *   `top`\n    *   `right`\n    *   `bottom`\n    *   `left`\n*   `fromEnd` (optional, string) is the shape of the endpoint at the edge start. Defaults to `none` if not specified. Valid values:\n    *   `none`\n    *   `arrow`\n*   `toNode` (required, string) is the node `id` where the connection ends.\n*   `toSide` (optional, string) is the side where this edge ends. Valid values:\n    *   `top`\n    *   `right`\n    *   `bottom`\n    *   `left`\n*   `toEnd` (optional, string) is the shape of the endpoint at the edge end. Defaults to `arrow` if not specified. Valid values:\n    *   `none`\n    *   `arrow`\n*   `color` (optional, `canvasColor`) is the color of the line, see the Color section.\n*   `label` (optional, string) is a text label for the edge.\n\nColor\n-----\n\nThe `canvasColor` type is used to encode color data for nodes and edges. Colors attributes expect a string. Colors can be specified in hex format e.g. `\"#FF0000\"`, or using one of the preset colors, e.g. `\"1\"` for red. Six preset colors exist, mapped to the following numbers:\n\n*   `\"1\"` red\n*   `\"2\"` orange\n*   `\"3\"` yellow\n*   `\"4\"` green\n*   `\"5\"` cyan\n*   `\"6\"` purple\n\nSpecific values for the preset colors are intentionally not defined so that applications can tailor the presets to their specific brand colors or color scheme.",
  "usage": {
    "tokens": 1041
  }
}
```
