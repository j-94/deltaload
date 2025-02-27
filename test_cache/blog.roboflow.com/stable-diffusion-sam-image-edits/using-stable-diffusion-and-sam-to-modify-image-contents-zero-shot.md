---
title: Using Stable Diffusion and SAM to Modify Image Contents Zero Shot
description: 
url: https://blog.roboflow.com/stable-diffusion-sam-image-edits/
timestamp: 2025-01-20T16:02:29.735Z
domain: blog.roboflow.com
path: stable-diffusion-sam-image-edits
---

# Using Stable Diffusion and SAM to Modify Image Contents Zero Shot



## Content

Introduction
------------

Recent breakthroughs in large language models (LLMs) and foundation computer vision models have unlocked new interfaces and methods for editing images or videos. You may have heard of inpainting, outpainting, generative fill, and text to image; this post will show you how to execute those new generative AI functions by building your own visual editor using only text prompts and the newest open source models.

Image editing is no longer about manual manipulation using hosted software. Models like [Segment Anything Model (SAM)](https://blog.roboflow.com/how-to-use-segment-anything-model-sam/), [Stable Diffusion](https://blog.roboflow.com/stable-diffusion-image-to-image-pipeline/), and [Grounding DINO](https://blog.roboflow.com/grounding-dino-zero-shot-object-detection/) have made it possible to perform image editing using only text commands. Together, they create a powerful workflow that seamlessly combines image zero shot detection, segmentation, and inpainting. The goal of the tutorial is to demonstrate the potential of the three powerful models to get you started so you can build on top of it.

By the end of this guide, you'll be able to transform and manipulate images using nothing more than text commands. This blog post will carefully walk you through a tutorial on how to leverage these models for image editing!

💡

For complete implementation details, refer to the full [Colab notebook](https://colab.research.google.com/drive/1ViJ-jCPVnPZUcdoD6iW9O9p3udifzYmR?usp=sharing&ref=blog.roboflow.com).

  

### Changing Objects Entirely  

![Image 47](https://blog.roboflow.com/content/images/2024/04/image-1095.webp)

Prompt used for zero shot object detection: “Fire Hydrant”, Prompt used for Generation: "Photo Booth"

### Changing colors and texture of objects

![Image 48](https://blog.roboflow.com/content/images/2024/04/image-1098.webp)

Prompt used for zero shot object detection: “Car”, Prompt used for Generation: "Red Car"

### Creative Applications with Context

![Image 49](https://blog.roboflow.com/content/images/2024/04/image-1101.webp)

Prompt used for zero shot object detection: “Yoda”, Prompt used for Generation: "Raccoon Yoda in Star Wars"

#Step 1: Install Dependencies
-----------------------------

Our process starts by installing the necessary libraries and models. We begin with SAM, a powerful segmentation model, Stable Diffusion for image inpainting, and GroundingDINO for zero shot object detection.

```
!pip -q install diffusers transformers scipy segment_anything
!git clone https://github.com/IDEA-Research/GroundingDINO.git
%cd GroundingDINO
!pip -q install -e .
```

We'll use Grounding DINO for zero shot object detection based on the text input, in this case “fire hydrant”. Using the predict function from GroundingDINO, we obtain the boxes, logits, and phrases for our image. We then annotate our image using these results.

```
from groundingdino.util.inference import load_model, load_image, predict, annotate
TEXT_PROMPT = "fire hydrant"
boxes, logits, phrases = predict(
   model=groundingdino_model,
   image=img,
   caption=TEXT_PROMPT,
   box_threshold=BOX_TRESHOLD,
   text_threshold=TEXT_TRESHOLD
)
img_annnotated = annotate(image_source=src, boxes=boxes, logits=logits, phrases=phrases)[...,::-1]
```

![Image 50](https://blog.roboflow.com/content/images/2024/04/image-1104.webp)

Zero Shot Object Detection using GroundingDINO

Then, we will use SAM to extract masks from the bounding box.

```
from segment_anything import SamPredictor, sam_model_registry
predictor = SamPredictor(sam_model_registry[model_type](checkpoint="./weights/sam_vit_h_4b8939.pth").to(device=device))

masks, _, _ = predictor.predict_torch(
           point_coords = None,
           point_labels = None,
           boxes = new_boxes,
           multimask_output = False,
       )
```

![Image 51](https://blog.roboflow.com/content/images/2024/04/image-1107.webp)

Segmented Object with Mask using SAM

![Image 52](https://blog.roboflow.com/content/images/2024/04/image-1110.webp)

#Step 3: Modify Image Using Stable Diffusion
--------------------------------------------

Then, we will modify the image based on a text prompt using Stable Diffusion. The pipe function from Stable Diffusion is used to inpaint the areas identified by the mask with the contents of the text prompt. Keep this in mind for your use cases, you’ll want the inpainted objects to be a similar form and shape to the object they are replacing.

```
prompt = "Phone Booth"
edited = pipe(prompt=prompt, image=original_img, mask_image=only_mask).images[0]
```

![Image 53](https://blog.roboflow.com/content/images/2024/04/image-1115.webp)

Use Cases for Editing Images with Text Prompts
----------------------------------------------

*   **Rapid Prototyping**: Accelerate product development and testing with quick visualization enabling faster feedback and decision making for designers and developers.
*   **Image Translation and Localization**: Support diversity by translating and localizing visual content with alternatives.
*   **Video/Image Editing and Content Management**: Speed up editing images and videos using text prompts instead of UI, catering to individual creators and enterprises for mass editing tasks.
*   **Object Identification and Replacemen**t: Easily identify objects and replace them with other objects, such as replacing a beer bottle with a coke bottle.

Conclusion
----------

That’s it! Leveraging powerful models such as SAM, Stable Diffusion, and Grounding DINO makes image transformations easier and more accessible. With text-based commands, we can instruct the models to execute precise tasks such as recognizing objects, segmenting them, and replacing them with other objects.

The code in this tutorial provides a starting point for getting started with text-based image editing, and we encourage you to experiment with different objects and see what fascinating results you can achieve.

### Full Code

For complete implementation details, refer to the full [Colab notebook](https://colab.research.google.com/drive/1ViJ-jCPVnPZUcdoD6iW9O9p3udifzYmR?usp=sharing&ref=blog.roboflow.com).

```
def process_boxes(boxes, src):
   H, W, _ = src.shape
   boxes_xyxy = box_ops.box_cxcywh_to_xyxy(boxes) * torch.Tensor([W, H, W, H])
   return predictor.transform.apply_boxes_torch(boxes_xyxy, src.shape[:2]).to(device)

def edit_image(path, item, prompt, box_threshold, text_threshold):
   src, img = load_image(path)
   boxes, logits, phrases = predict(
       model=groundingdino_model,
       image=img,
       caption=item,
       box_threshold=box_threshold,
       text_threshold=text_threshold
   )
   predictor.set_image(src)
   new_boxes = process_boxes(boxes, src)
   masks, _, _ = predictor.predict_torch(
       point_coords=None,
       point_labels=None,
       boxes=new_boxes,
       multimask_output=False,
   )
   img_annotated_mask = show_mask(masks[0][0].cpu(),
       annotate(image_source=src, boxes=boxes, logits=logits, phrases=phrases)[...,::-1]
   )
   return pipe(prompt=prompt,
       image=Image.fromarray(src).resize((512, 512)),
      mask_image=Image.fromarray(masks[0][0].cpu().numpy()).resize((512, 512))
   ).images[0]
```

## Metadata

```json
{
  "title": "Using Stable Diffusion and SAM to Modify Image Contents Zero Shot",
  "description": "",
  "url": "https://blog.roboflow.com/stable-diffusion-sam-image-edits/",
  "content": "Introduction\n------------\n\nRecent breakthroughs in large language models (LLMs) and foundation computer vision models have unlocked new interfaces and methods for editing images or videos. You may have heard of inpainting, outpainting, generative fill, and text to image; this post will show you how to execute those new generative AI functions by building your own visual editor using only text prompts and the newest open source models.\n\nImage editing is no longer about manual manipulation using hosted software. Models like [Segment Anything Model (SAM)](https://blog.roboflow.com/how-to-use-segment-anything-model-sam/), [Stable Diffusion](https://blog.roboflow.com/stable-diffusion-image-to-image-pipeline/), and [Grounding DINO](https://blog.roboflow.com/grounding-dino-zero-shot-object-detection/) have made it possible to perform image editing using only text commands. Together, they create a powerful workflow that seamlessly combines image zero shot detection, segmentation, and inpainting. The goal of the tutorial is to demonstrate the potential of the three powerful models to get you started so you can build on top of it.\n\nBy the end of this guide, you'll be able to transform and manipulate images using nothing more than text commands. This blog post will carefully walk you through a tutorial on how to leverage these models for image editing!\n\n💡\n\nFor complete implementation details, refer to the full [Colab notebook](https://colab.research.google.com/drive/1ViJ-jCPVnPZUcdoD6iW9O9p3udifzYmR?usp=sharing&ref=blog.roboflow.com).\n\n  \n\n### Changing Objects Entirely  \n\n![Image 47](https://blog.roboflow.com/content/images/2024/04/image-1095.webp)\n\nPrompt used for zero shot object detection: “Fire Hydrant”, Prompt used for Generation: \"Photo Booth\"\n\n### Changing colors and texture of objects\n\n![Image 48](https://blog.roboflow.com/content/images/2024/04/image-1098.webp)\n\nPrompt used for zero shot object detection: “Car”, Prompt used for Generation: \"Red Car\"\n\n### Creative Applications with Context\n\n![Image 49](https://blog.roboflow.com/content/images/2024/04/image-1101.webp)\n\nPrompt used for zero shot object detection: “Yoda”, Prompt used for Generation: \"Raccoon Yoda in Star Wars\"\n\n#Step 1: Install Dependencies\n-----------------------------\n\nOur process starts by installing the necessary libraries and models. We begin with SAM, a powerful segmentation model, Stable Diffusion for image inpainting, and GroundingDINO for zero shot object detection.\n\n```\n!pip -q install diffusers transformers scipy segment_anything\n!git clone https://github.com/IDEA-Research/GroundingDINO.git\n%cd GroundingDINO\n!pip -q install -e .\n```\n\nWe'll use Grounding DINO for zero shot object detection based on the text input, in this case “fire hydrant”. Using the predict function from GroundingDINO, we obtain the boxes, logits, and phrases for our image. We then annotate our image using these results.\n\n```\nfrom groundingdino.util.inference import load_model, load_image, predict, annotate\nTEXT_PROMPT = \"fire hydrant\"\nboxes, logits, phrases = predict(\n   model=groundingdino_model,\n   image=img,\n   caption=TEXT_PROMPT,\n   box_threshold=BOX_TRESHOLD,\n   text_threshold=TEXT_TRESHOLD\n)\nimg_annnotated = annotate(image_source=src, boxes=boxes, logits=logits, phrases=phrases)[...,::-1]\n```\n\n![Image 50](https://blog.roboflow.com/content/images/2024/04/image-1104.webp)\n\nZero Shot Object Detection using GroundingDINO\n\nThen, we will use SAM to extract masks from the bounding box.\n\n```\nfrom segment_anything import SamPredictor, sam_model_registry\npredictor = SamPredictor(sam_model_registry[model_type](checkpoint=\"./weights/sam_vit_h_4b8939.pth\").to(device=device))\n\nmasks, _, _ = predictor.predict_torch(\n           point_coords = None,\n           point_labels = None,\n           boxes = new_boxes,\n           multimask_output = False,\n       )\n```\n\n![Image 51](https://blog.roboflow.com/content/images/2024/04/image-1107.webp)\n\nSegmented Object with Mask using SAM\n\n![Image 52](https://blog.roboflow.com/content/images/2024/04/image-1110.webp)\n\n#Step 3: Modify Image Using Stable Diffusion\n--------------------------------------------\n\nThen, we will modify the image based on a text prompt using Stable Diffusion. The pipe function from Stable Diffusion is used to inpaint the areas identified by the mask with the contents of the text prompt. Keep this in mind for your use cases, you’ll want the inpainted objects to be a similar form and shape to the object they are replacing.\n\n```\nprompt = \"Phone Booth\"\nedited = pipe(prompt=prompt, image=original_img, mask_image=only_mask).images[0]\n```\n\n![Image 53](https://blog.roboflow.com/content/images/2024/04/image-1115.webp)\n\nUse Cases for Editing Images with Text Prompts\n----------------------------------------------\n\n*   **Rapid Prototyping**: Accelerate product development and testing with quick visualization enabling faster feedback and decision making for designers and developers.\n*   **Image Translation and Localization**: Support diversity by translating and localizing visual content with alternatives.\n*   **Video/Image Editing and Content Management**: Speed up editing images and videos using text prompts instead of UI, catering to individual creators and enterprises for mass editing tasks.\n*   **Object Identification and Replacemen**t: Easily identify objects and replace them with other objects, such as replacing a beer bottle with a coke bottle.\n\nConclusion\n----------\n\nThat’s it! Leveraging powerful models such as SAM, Stable Diffusion, and Grounding DINO makes image transformations easier and more accessible. With text-based commands, we can instruct the models to execute precise tasks such as recognizing objects, segmenting them, and replacing them with other objects.\n\nThe code in this tutorial provides a starting point for getting started with text-based image editing, and we encourage you to experiment with different objects and see what fascinating results you can achieve.\n\n### Full Code\n\nFor complete implementation details, refer to the full [Colab notebook](https://colab.research.google.com/drive/1ViJ-jCPVnPZUcdoD6iW9O9p3udifzYmR?usp=sharing&ref=blog.roboflow.com).\n\n```\ndef process_boxes(boxes, src):\n   H, W, _ = src.shape\n   boxes_xyxy = box_ops.box_cxcywh_to_xyxy(boxes) * torch.Tensor([W, H, W, H])\n   return predictor.transform.apply_boxes_torch(boxes_xyxy, src.shape[:2]).to(device)\n\ndef edit_image(path, item, prompt, box_threshold, text_threshold):\n   src, img = load_image(path)\n   boxes, logits, phrases = predict(\n       model=groundingdino_model,\n       image=img,\n       caption=item,\n       box_threshold=box_threshold,\n       text_threshold=text_threshold\n   )\n   predictor.set_image(src)\n   new_boxes = process_boxes(boxes, src)\n   masks, _, _ = predictor.predict_torch(\n       point_coords=None,\n       point_labels=None,\n       boxes=new_boxes,\n       multimask_output=False,\n   )\n   img_annotated_mask = show_mask(masks[0][0].cpu(),\n       annotate(image_source=src, boxes=boxes, logits=logits, phrases=phrases)[...,::-1]\n   )\n   return pipe(prompt=prompt,\n       image=Image.fromarray(src).resize((512, 512)),\n      mask_image=Image.fromarray(masks[0][0].cpu().numpy()).resize((512, 512))\n   ).images[0]\n```",
  "publishedTime": "2023-08-01T01:49:52.000Z",
  "usage": {
    "tokens": 1703
  }
}
```
