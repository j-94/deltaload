---
title: Image Transforms | Craft CMS Documentation
description: 
url: https://craftcms.com/docs/5.x/development/image-transforms.html
timestamp: 2025-01-20T16:04:19.267Z
domain: craftcms.com
path: docs_5.x_development_image-transforms.html
---

# Image Transforms | Craft CMS Documentation



## Content

Instead of requiring content editors to upload images at a specific sizes, Craft lets you define “image transforms” for automatically manipulating images in predefined ways, or on-demand. Transforms are _non-destructive_, meaning they have no effect on the original uploaded image.

Transforms can be defined in the control panel or directly from your templates and GraphQL queries.

[#](https://craftcms.com/docs/5.x/development/image-transforms.html#named-transforms) Named Transforms
------------------------------------------------------------------------------------------------------

Named transforms are created from the [control panel](https://craftcms.com/docs/5.x/system/control-panel) by navigating to **Settings** → **Assets** → **Image Transforms** and press **New Transform**.

my-craft-project.ddev.site/admin/settings/assets/transforms/new

![Image 4: Asset transform edit screen](https://craftcms.com/docs/assets/img/assets-transforms.c06227fb.png)

Creating a new predefined asset transform in the control panel.

Every transform has the following settings:

Name

A user-facing name or label for the transform. This is mostly for your reference, but it _may_ be exposed to content authors when using [Redactor (opens new window)](https://plugins.craftcms.com/redactor).

Handle

A template-facing handle, used when accessing transforms in Twig or via GraphQL. _Changing this may require updates to your templates!_

Mode

Specifies how the transform is handled:

*   [**Crop**](https://craftcms.com/docs/5.x/development/image-transforms.html#crop) (Default) — Crops the image to the specified width and height.
*   [**Fit**](https://craftcms.com/docs/5.x/development/image-transforms.html#fit) — Scales the image so that it is as big as possible with all dimensions fitting within the specified width and height.
*   [**Letterbox**](https://craftcms.com/docs/5.x/development/image-transforms.html#letterbox) — Stretches the image to the specified width and height.
*   [**Stretch**](https://craftcms.com/docs/5.x/development/image-transforms.html#stretch) — Stretches the image to the specified width and height.

All [modes](https://craftcms.com/docs/5.x/development/image-transforms.html#transform-modes) support some general controls over image size and quality:

Width

Final transformed image width, or blank to calculate automatically from the original image’s aspect ratio.

Height

Final transformed image height, or blank to calculate automatically from the original image’s aspect ratio.

Allow Upscaling

Whether or not Craft is allowed to scale an image beyond its original dimensions. Affects the maximum **Width** and **Height** for **Fit**, **Crop**, and **Stretch** output, and the matting strategy for **Letterbox** transforms.

Quality

Sets a quality or compression ratio for the transformed image, depending on the format of the target image. When left blank, the quality will be determined by the [defaultImageQuality](https://craftcms.com/docs/5.x/reference/config/general#defaultimagequality) config setting.

Interlacing

Specify an [interlacing (opens new window)](https://en.wikipedia.org/wiki/Interlacing_(bitmaps)) strategy for the pixels in raster images.

Image Format

Format for the transformed image.

*   Auto (same as source image, if [web-safe (opens new window)](https://docs.craftcms.com/api/v5/craft-helpers-image.html#method-websafeformats), otherwise `jpg`)
*   `jpg`
*   `png`
*   `gif`
*   `webp` (when supported by ImageMagick)
*   `avif` (when supported by ImageMagick)

The [transformGifs](https://craftcms.com/docs/5.x/reference/config/general#transformgifs) setting allows you to completely disable transformation of GIF images. Animated GIFs often consume significant resources to resize, and rarely produce well-optimized output.

You do not need to update templates for this setting to work—Craft will just ignore the transform and return a URL to the original image.

Some modes may behave the same when using only one of the **Width** and **Height** settings. Typically, an unset dimension means the image’s aspect ratio is maintained.

Suppose we have a source image that is 600 pixels wide and 400 pixels tall. Applying a **Stretch** transform that only declares a **Width** of 60 pixels would produce an image 40 pixels tall.

[#](https://craftcms.com/docs/5.x/development/image-transforms.html#transform-modes) Transform Modes
----------------------------------------------------------------------------------------------------

Additional settings are available for some transform modes.

### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#crop) Crop

When using the **Crop** mode, a **Default Focal Point** setting is revealed, allowing customization of which image area Craft should center the crop on when a [focal point](https://craftcms.com/docs/5.x/reference/element-types/assets#focal-points) isn’t specified. Its options include:

| Label | Handle |
| --- | --- |
| Top-Left | `top-left` |
| Top-Center | `top-center` |
| Top-Right | `top-right` |
| Center-Left | `center-left` |
| Center-Center | `center-center` |
| Center-Right | `center-right` |
| Bottom-Left | `bottom-left` |
| Bottom-Center | `bottom-center` |
| Bottom-Right | `bottom-right` |

When a focal point _is_ known for an image, Craft will attempt to keep that point as close to the center of the crop as possible.

### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#fit) Fit

The **Fit** mode always respects the original image’s aspect ratio. The image is scaled to fit within the specified **Width** and/or **Height**, but may not cover the entire allowed area. Focal points have no effect when using this mode, as images are never cropped.

### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#letterbox) Letterbox

Two new options are revealed when using the **Letterbox** mode:

*   **Fill Color** — A hexadecimal color value used for the matte. When supported, the default matte is transparent; otherwise, white.
*   **Image Position** — Where the image will be anchored, when it does not fill the entire target frame. The same anchoring options are available here as for the **Default Focal Point** option in the **Crop** and **Fit** modes.

Letterbox mode preserves images’ aspect ratios, fitting them within the provided width and height and filling the remaining space with the **Fill Color**. If the target frame is larger than the original image’s dimensions and the **Allow Upscaling** option is _Off_, Craft may matte the image on more than two sides.

### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#stretch) Stretch

Like **Crop** and **Fit**, **Stretch** is only differentiated from other transforms when used with a **Height** _and_ a **Width** setting.

With both set, the image is scaled horizontally _and_ vertically to the target size.

As the name of this mode suggests, using a target height and width that are a different aspect ratio than the original image will cause the image to be stretched disproportionately.

[#](https://craftcms.com/docs/5.x/development/image-transforms.html#applying-named-transforms-to-images) Applying Named Transforms to Images
--------------------------------------------------------------------------------------------------------------------------------------------

To output an image with your named transform applied, pass its handle into your asset’s [getImg() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getimg), [getUrl() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-geturl), [getWidth() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getwidth), and [getHeight() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getheight) functions:

You can also apply the transform on the asset so any relevant properties are automatically manipulated by default. This example would output the same result as the example above:

[#](https://craftcms.com/docs/5.x/development/image-transforms.html#defining-transforms-in-your-templates) Defining Transforms in your Templates
------------------------------------------------------------------------------------------------------------------------------------------------

You can also define transforms directly in your templates by creating a hash with the desired parameters:

See a list of all the [possible keys and values](https://craftcms.com/docs/5.x/development/image-transforms.html#possible-values) for this object.

Then pass that hash into your asset’s `getUrl()`, `getWidth()`, and `getHeight()` functions:

Notice in this example there are no quotes around “`thumb`” like there were in our earlier examples. That’s because before we were passing a [string](https://craftcms.com/docs/5.x/development/twig#strings) set to reference a control-panel-defined transform by its handle, whereas this example passes a [variable](https://craftcms.com/docs/5.x/development/twig#variables) containing the `thumb` options hash we created in the template.

It would look similar using `setTransform()` like we did in the previous section:

### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#possible-values) Possible Values

All the same settings available to [named transforms](https://craftcms.com/docs/5.x/development/image-transforms.html#named-transforms) are available to template-defined transforms and transforms requested via [GraphQL](https://craftcms.com/docs/5.x/development/image-transforms.html#graphql).

*   The `mode` property can be set to either `'crop'`, `'fit'`, `'letterbox'`, or `'stretch'`.
*   `width` and `height` can each be set to an integer, or omitted.
*   `quality` can be set to a number between 0 and 100, or omitted to use the [defaultImageQuality](https://craftcms.com/docs/5.x/reference/config/general#defaultimagequality) setting.
*   `format` can be set to `'jpg'`, `'gif'`, `'png'`, `'webp'`, `'avif'`, or omitted.
*   A `position` property (set to one of the [valid values](https://craftcms.com/docs/5.x/development/image-transforms.html#crop) listed above) is supported when `mode` is set to `'crop'` or `'letterbox'`. The behavior is different for each [type of transform](https://craftcms.com/docs/5.x/development/image-transforms.html#transform-modes).

### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#overriding-named-transforms) Overriding Named Transforms

Should you need to break from a named transform in a few places, you can specify overrides alongside a `transform` key:

This would accomplish the same thing as the example before it, except `quality` would be maxed out at 100 rather than whatever was set on the named `'thumb'` transform.

You can override settings like this with the `getUrl()` method, too:

This would use the named `'thumb'` transform’s settings, but always generate a `.webp` file.

### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#generating-srcset-sizes) Generating `srcset` Sizes

Transforms are a great way to avoid serving unnecessarily-large images to your users—but there’s still room for optimization! Most browsers support the [`srcset` (opens new window)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset) attribute, which allows you to define a collection of images that are appropriate for a given device or viewport.

Rather than creating an exhaustive list of named transforms or building up multiple config hashes in your templates, you can offload this work to Craft with the [`getSrcSet()` (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getsrcset) method. Here’s an example that uses the [`tag` template function](https://craftcms.com/docs/5.x/reference/twig/functions#tag) to render an image with a `srcset` attribute containing three variations based on a single transform:

This can be done even more succinctly by passing a second `sizes` argument to the [`getImg()` (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getimg) method:

Don’t forget to configure the corresponding `sizes` attribute, as well—Craft can manage the transforms and build a valid `srcset`, but it doesn’t know how the images are actually used in your front-end!

[#](https://craftcms.com/docs/5.x/development/image-transforms.html#graphql) GraphQL
------------------------------------------------------------------------------------

When requesting asset data via the [GraphQL](https://craftcms.com/docs/5.x/development/graphql) API, you can get named and ad-hoc transforms with the `@transform` directive.

Like we’ve seen in the template-defined transforms, the GraphQL API allows you to retrieve individual properties as though they were tied to a transform…

*   Query
*   Data

…or set a transform on the entire asset object:

*   Query
*   Data

Note that in the first example, the `height` and `width` values are for the _original_ image, whereas in the second example, they reflect the _transformed_ dimensions.

## Metadata

```json
{
  "title": "Image Transforms | Craft CMS Documentation",
  "description": "",
  "url": "https://craftcms.com/docs/5.x/development/image-transforms.html",
  "content": "Instead of requiring content editors to upload images at a specific sizes, Craft lets you define “image transforms” for automatically manipulating images in predefined ways, or on-demand. Transforms are _non-destructive_, meaning they have no effect on the original uploaded image.\n\nTransforms can be defined in the control panel or directly from your templates and GraphQL queries.\n\n[#](https://craftcms.com/docs/5.x/development/image-transforms.html#named-transforms) Named Transforms\n------------------------------------------------------------------------------------------------------\n\nNamed transforms are created from the [control panel](https://craftcms.com/docs/5.x/system/control-panel) by navigating to **Settings** → **Assets** → **Image Transforms** and press **New Transform**.\n\nmy-craft-project.ddev.site/admin/settings/assets/transforms/new\n\n![Image 4: Asset transform edit screen](https://craftcms.com/docs/assets/img/assets-transforms.c06227fb.png)\n\nCreating a new predefined asset transform in the control panel.\n\nEvery transform has the following settings:\n\nName\n\nA user-facing name or label for the transform. This is mostly for your reference, but it _may_ be exposed to content authors when using [Redactor (opens new window)](https://plugins.craftcms.com/redactor).\n\nHandle\n\nA template-facing handle, used when accessing transforms in Twig or via GraphQL. _Changing this may require updates to your templates!_\n\nMode\n\nSpecifies how the transform is handled:\n\n*   [**Crop**](https://craftcms.com/docs/5.x/development/image-transforms.html#crop) (Default) — Crops the image to the specified width and height.\n*   [**Fit**](https://craftcms.com/docs/5.x/development/image-transforms.html#fit) — Scales the image so that it is as big as possible with all dimensions fitting within the specified width and height.\n*   [**Letterbox**](https://craftcms.com/docs/5.x/development/image-transforms.html#letterbox) — Stretches the image to the specified width and height.\n*   [**Stretch**](https://craftcms.com/docs/5.x/development/image-transforms.html#stretch) — Stretches the image to the specified width and height.\n\nAll [modes](https://craftcms.com/docs/5.x/development/image-transforms.html#transform-modes) support some general controls over image size and quality:\n\nWidth\n\nFinal transformed image width, or blank to calculate automatically from the original image’s aspect ratio.\n\nHeight\n\nFinal transformed image height, or blank to calculate automatically from the original image’s aspect ratio.\n\nAllow Upscaling\n\nWhether or not Craft is allowed to scale an image beyond its original dimensions. Affects the maximum **Width** and **Height** for **Fit**, **Crop**, and **Stretch** output, and the matting strategy for **Letterbox** transforms.\n\nQuality\n\nSets a quality or compression ratio for the transformed image, depending on the format of the target image. When left blank, the quality will be determined by the [defaultImageQuality](https://craftcms.com/docs/5.x/reference/config/general#defaultimagequality) config setting.\n\nInterlacing\n\nSpecify an [interlacing (opens new window)](https://en.wikipedia.org/wiki/Interlacing_(bitmaps)) strategy for the pixels in raster images.\n\nImage Format\n\nFormat for the transformed image.\n\n*   Auto (same as source image, if [web-safe (opens new window)](https://docs.craftcms.com/api/v5/craft-helpers-image.html#method-websafeformats), otherwise `jpg`)\n*   `jpg`\n*   `png`\n*   `gif`\n*   `webp` (when supported by ImageMagick)\n*   `avif` (when supported by ImageMagick)\n\nThe [transformGifs](https://craftcms.com/docs/5.x/reference/config/general#transformgifs) setting allows you to completely disable transformation of GIF images. Animated GIFs often consume significant resources to resize, and rarely produce well-optimized output.\n\nYou do not need to update templates for this setting to work—Craft will just ignore the transform and return a URL to the original image.\n\nSome modes may behave the same when using only one of the **Width** and **Height** settings. Typically, an unset dimension means the image’s aspect ratio is maintained.\n\nSuppose we have a source image that is 600 pixels wide and 400 pixels tall. Applying a **Stretch** transform that only declares a **Width** of 60 pixels would produce an image 40 pixels tall.\n\n[#](https://craftcms.com/docs/5.x/development/image-transforms.html#transform-modes) Transform Modes\n----------------------------------------------------------------------------------------------------\n\nAdditional settings are available for some transform modes.\n\n### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#crop) Crop\n\nWhen using the **Crop** mode, a **Default Focal Point** setting is revealed, allowing customization of which image area Craft should center the crop on when a [focal point](https://craftcms.com/docs/5.x/reference/element-types/assets#focal-points) isn’t specified. Its options include:\n\n| Label | Handle |\n| --- | --- |\n| Top-Left | `top-left` |\n| Top-Center | `top-center` |\n| Top-Right | `top-right` |\n| Center-Left | `center-left` |\n| Center-Center | `center-center` |\n| Center-Right | `center-right` |\n| Bottom-Left | `bottom-left` |\n| Bottom-Center | `bottom-center` |\n| Bottom-Right | `bottom-right` |\n\nWhen a focal point _is_ known for an image, Craft will attempt to keep that point as close to the center of the crop as possible.\n\n### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#fit) Fit\n\nThe **Fit** mode always respects the original image’s aspect ratio. The image is scaled to fit within the specified **Width** and/or **Height**, but may not cover the entire allowed area. Focal points have no effect when using this mode, as images are never cropped.\n\n### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#letterbox) Letterbox\n\nTwo new options are revealed when using the **Letterbox** mode:\n\n*   **Fill Color** — A hexadecimal color value used for the matte. When supported, the default matte is transparent; otherwise, white.\n*   **Image Position** — Where the image will be anchored, when it does not fill the entire target frame. The same anchoring options are available here as for the **Default Focal Point** option in the **Crop** and **Fit** modes.\n\nLetterbox mode preserves images’ aspect ratios, fitting them within the provided width and height and filling the remaining space with the **Fill Color**. If the target frame is larger than the original image’s dimensions and the **Allow Upscaling** option is _Off_, Craft may matte the image on more than two sides.\n\n### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#stretch) Stretch\n\nLike **Crop** and **Fit**, **Stretch** is only differentiated from other transforms when used with a **Height** _and_ a **Width** setting.\n\nWith both set, the image is scaled horizontally _and_ vertically to the target size.\n\nAs the name of this mode suggests, using a target height and width that are a different aspect ratio than the original image will cause the image to be stretched disproportionately.\n\n[#](https://craftcms.com/docs/5.x/development/image-transforms.html#applying-named-transforms-to-images) Applying Named Transforms to Images\n--------------------------------------------------------------------------------------------------------------------------------------------\n\nTo output an image with your named transform applied, pass its handle into your asset’s [getImg() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getimg), [getUrl() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-geturl), [getWidth() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getwidth), and [getHeight() (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getheight) functions:\n\nYou can also apply the transform on the asset so any relevant properties are automatically manipulated by default. This example would output the same result as the example above:\n\n[#](https://craftcms.com/docs/5.x/development/image-transforms.html#defining-transforms-in-your-templates) Defining Transforms in your Templates\n------------------------------------------------------------------------------------------------------------------------------------------------\n\nYou can also define transforms directly in your templates by creating a hash with the desired parameters:\n\nSee a list of all the [possible keys and values](https://craftcms.com/docs/5.x/development/image-transforms.html#possible-values) for this object.\n\nThen pass that hash into your asset’s `getUrl()`, `getWidth()`, and `getHeight()` functions:\n\nNotice in this example there are no quotes around “`thumb`” like there were in our earlier examples. That’s because before we were passing a [string](https://craftcms.com/docs/5.x/development/twig#strings) set to reference a control-panel-defined transform by its handle, whereas this example passes a [variable](https://craftcms.com/docs/5.x/development/twig#variables) containing the `thumb` options hash we created in the template.\n\nIt would look similar using `setTransform()` like we did in the previous section:\n\n### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#possible-values) Possible Values\n\nAll the same settings available to [named transforms](https://craftcms.com/docs/5.x/development/image-transforms.html#named-transforms) are available to template-defined transforms and transforms requested via [GraphQL](https://craftcms.com/docs/5.x/development/image-transforms.html#graphql).\n\n*   The `mode` property can be set to either `'crop'`, `'fit'`, `'letterbox'`, or `'stretch'`.\n*   `width` and `height` can each be set to an integer, or omitted.\n*   `quality` can be set to a number between 0 and 100, or omitted to use the [defaultImageQuality](https://craftcms.com/docs/5.x/reference/config/general#defaultimagequality) setting.\n*   `format` can be set to `'jpg'`, `'gif'`, `'png'`, `'webp'`, `'avif'`, or omitted.\n*   A `position` property (set to one of the [valid values](https://craftcms.com/docs/5.x/development/image-transforms.html#crop) listed above) is supported when `mode` is set to `'crop'` or `'letterbox'`. The behavior is different for each [type of transform](https://craftcms.com/docs/5.x/development/image-transforms.html#transform-modes).\n\n### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#overriding-named-transforms) Overriding Named Transforms\n\nShould you need to break from a named transform in a few places, you can specify overrides alongside a `transform` key:\n\nThis would accomplish the same thing as the example before it, except `quality` would be maxed out at 100 rather than whatever was set on the named `'thumb'` transform.\n\nYou can override settings like this with the `getUrl()` method, too:\n\nThis would use the named `'thumb'` transform’s settings, but always generate a `.webp` file.\n\n### [#](https://craftcms.com/docs/5.x/development/image-transforms.html#generating-srcset-sizes) Generating `srcset` Sizes\n\nTransforms are a great way to avoid serving unnecessarily-large images to your users—but there’s still room for optimization! Most browsers support the [`srcset` (opens new window)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset) attribute, which allows you to define a collection of images that are appropriate for a given device or viewport.\n\nRather than creating an exhaustive list of named transforms or building up multiple config hashes in your templates, you can offload this work to Craft with the [`getSrcSet()` (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getsrcset) method. Here’s an example that uses the [`tag` template function](https://craftcms.com/docs/5.x/reference/twig/functions#tag) to render an image with a `srcset` attribute containing three variations based on a single transform:\n\nThis can be done even more succinctly by passing a second `sizes` argument to the [`getImg()` (opens new window)](https://docs.craftcms.com/api/v5/craft-elements-asset.html#method-getimg) method:\n\nDon’t forget to configure the corresponding `sizes` attribute, as well—Craft can manage the transforms and build a valid `srcset`, but it doesn’t know how the images are actually used in your front-end!\n\n[#](https://craftcms.com/docs/5.x/development/image-transforms.html#graphql) GraphQL\n------------------------------------------------------------------------------------\n\nWhen requesting asset data via the [GraphQL](https://craftcms.com/docs/5.x/development/graphql) API, you can get named and ad-hoc transforms with the `@transform` directive.\n\nLike we’ve seen in the template-defined transforms, the GraphQL API allows you to retrieve individual properties as though they were tied to a transform…\n\n*   Query\n*   Data\n\n…or set a transform on the entire asset object:\n\n*   Query\n*   Data\n\nNote that in the first example, the `height` and `width` values are for the _original_ image, whereas in the second example, they reflect the _transformed_ dimensions.",
  "usage": {
    "tokens": 2942
  }
}
```
