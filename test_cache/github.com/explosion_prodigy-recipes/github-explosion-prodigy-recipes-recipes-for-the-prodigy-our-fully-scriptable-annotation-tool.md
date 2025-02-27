---
title: GitHub - explosion/prodigy-recipes: 🍳 Recipes for the Prodigy, our fully scriptable annotation tool
description: 🍳 Recipes for the Prodigy, our fully scriptable annotation tool - explosion/prodigy-recipes
url: https://github.com/explosion/prodigy-recipes
timestamp: 2025-01-20T15:30:41.464Z
domain: github.com
path: explosion_prodigy-recipes
---

# GitHub - explosion/prodigy-recipes: 🍳 Recipes for the Prodigy, our fully scriptable annotation tool


🍳 Recipes for the Prodigy, our fully scriptable annotation tool - explosion/prodigy-recipes


## Content

[![Image 18](https://camo.githubusercontent.com/17aebe83d2ca93fc83c7d74ec6a87455a7469e5be43c3933c918a64121725a21/68747470733a2f2f6578706c6f73696f6e2e61692f6173736574732f696d672f6c6f676f2e737667)](https://explosion.ai/)

Prodigy Recipes
---------------

[](https://github.com/explosion/prodigy-recipes?screenshot=true#prodigy-recipes)

This repository contains a collection of recipes for [Prodigy](https://prodi.gy/), our scriptable annotation tool for text, images and other data. In order to use this repo, you'll need a license for Prodigy – [see this page](https://prodi.gy/buy) for more details. For questions and bug reports, please use the [Prodigy Support Forum](https://support.prodi.gy/). If you've found a mistake or bug, feel free to submit a [pull request](https://github.com/explosion/prodigy-recipes/pulls).

> ✨ **Important note:** The recipes in this repository aren't 100% identical to the built-in recipes shipped with Prodigy. They've been edited to include comments and more information, and some of them have been simplified to make it easier to follow what's going on, and to use them as the basis for a custom recipe.

📋 Usage
--------

[](https://github.com/explosion/prodigy-recipes?screenshot=true#-usage)

Once Prodigy is installed, you should be able to run the `prodigy` command from your terminal, either directly or via `python -m`:

The `prodigy` command lists the built-in recipes. To use a custom recipe script, simply pass the path to the file using the `-F` argument:

python -m prodigy ner.teach your\_dataset en\_core\_web\_sm ./data.jsonl --label PERSON -F prodigy-recipes/ner/ner\_teach.py

You can also use the `--help` flag for an overview of the available arguments of a recipe, e.g. `prodigy ner.teach -F ner_teach_.py --help`.

### Some things to try

[](https://github.com/explosion/prodigy-recipes?screenshot=true#some-things-to-try)

You can edit the code in the recipe script to customize how Prodigy behaves.

*   Try replacing `prefer_uncertain()` with `prefer_high_scores()`.
*   Try writing a custom sorting function. It just needs to be a generator that yields a sequence of `example` dicts, given a sequence of `(score, example)` tuples.
*   Try adding a filter that drops some questions from the stream. For instance, try writing a filter that only asks you questions where the entity is two words long.
*   Try customizing the `update()` callback, to include extra logging or extra functionality.

🍳 Recipes
----------

[](https://github.com/explosion/prodigy-recipes?screenshot=true#-recipes)

### Named Entity Recognition

[](https://github.com/explosion/prodigy-recipes?screenshot=true#named-entity-recognition)

| Recipe | Description |
| --- | --- |
| [`ner.teach`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_teach.py) | Collect the best possible training data for a named entity recognition model with the model in the loop. Based on your annotations, Prodigy will decide which questions to ask next. |
| [`ner.match`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_match.py) | Suggest phrases that match a given patterns file, and mark whether they are examples of the entity you're interested in. The patterns file can include exact strings or token patterns for use with spaCy's `Matcher`. |
| [`ner.manual`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_manual.py) | Mark spans manually by token. Requires only a tokenizer and no entity recognizer, and doesn't do any active learning. Optionally, pre-highlight spans based on patterns. |
| [`ner.fuzzy_manual`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_fuzzy_manual.py) | Like `ner.manual` but use `FuzzyMatcher` from [`spaczz`](https://github.com/gandersen101/spaczz) library to pre-highlight candidates. |
| [`ner.manual.bert`](https://github.com/explosion/prodigy-recipes/blob/master/other/transformers_tokenizers.py) | Use BERT word piece tokenizer for efficient manual NER annotation for transformer models. |
| [`ner.correct`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_correct.py) | Create gold-standard data by correcting a model's predictions manually. This recipe used to be called [`ner.make_gold`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_make_gold.py). |
| [`ner.silver-to-gold`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_silver_to_gold.py) | Take an existing "silver" dataset with binary accept/reject annotations, merge the annotations to find the best possible analysis given the constraints defined in the annotations, and manually edit it to create a perfect and complete "gold" dataset. |
| [`ner.eval_ab`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_eval_ab.py) | Evaluate two NER models by comparing their predictions and building an evaluation set from the stream. |
| [`ner_fuzzy_manual`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_fuzzy_manual.py) | Mark spans manually by token with suggestions from [`spaczz fuzzy`](https://spacy.io/universe/project/spaczz) matcher pre-highlighted. |

### Text Classification

[](https://github.com/explosion/prodigy-recipes?screenshot=true#text-classification)

| Recipe | Description |
| --- | --- |
| [`textcat.manual`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_manual.py) | Manually annotate categories that apply to a text. Supports annotation tasks with single and multiple labels. Multiple labels can optionally be flagged as exclusive. |
| [`textcat.correct`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_correct.py) | Correct the textcat model's predictions manually. Predictions above the acceptance threshold will be automatically preselected (0.5 by default). Prodigy will infer whether the categories should be mutualy exclusive based on the component configuration. |
| [`textcat.teach`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_teach.py) | Collect the best possible training data for a text classification model with the model in the loop. Based on your annotations, Prodigy will decide which questions to ask next. |
| [`textcat.custom-model`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_custom_model.py) | Use active learning-powered text classification with a custom model. To demonstrate how it works, this demo recipe uses a simple dummy model that "predicts" random scores. But you can swap it out for any model of your choice, for example a text classification model implementation using PyTorch, TensorFlow or scikit-learn. |

### Terminology

[](https://github.com/explosion/prodigy-recipes?screenshot=true#terminology)

| Recipe | Description |
| --- | --- |
| [`terms.teach`](https://github.com/explosion/prodigy-recipes/blob/master/terms/terms_teach.py) | Bootstrap a terminology list with word vectors and seeds terms. Prodigy will suggest similar terms based on the word vectors, and update the target vector accordingly. |

### Image

[](https://github.com/explosion/prodigy-recipes?screenshot=true#image)

| Recipe | Description |
| --- | --- |
| [`image.manual`](https://github.com/explosion/prodigy-recipes/blob/master/image/image_manual.py) | Manually annotate images by drawing rectangular bounding boxes or polygon shapes on the image. |
| [`image-caption`](https://github.com/explosion/prodigy-recipes/blob/master/image/image_caption/image_caption.py) | Annotate images with captions, pre-populate captions with image captioning model implemented in PyTorch and perform error analysis. |
| [`image.frozenmodel`](https://github.com/explosion/prodigy-recipes/blob/master/image/tf_odapi/image_frozen_model.py) | Model in loop manual annotation using [Tensorflow's Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). |
| [`image.servingmodel`](https://github.com/explosion/prodigy-recipes/blob/master/image/tf_odapi/image_tf_serving.py) | Model in loop manual annotation using [Tensorflow's Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). This uses [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) |
| [`image.trainmodel`](https://github.com/explosion/prodigy-recipes/blob/master/image/tf_odapi/image_train.py) | Model in loop manual annotation and training using [Tensorflow's Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). |

### Other

[](https://github.com/explosion/prodigy-recipes?screenshot=true#other)

| Recipe | Description |
| --- | --- |
| [`mark`](https://github.com/explosion/prodigy-recipes/blob/master/other/mark.py) | Click through pre-prepared examples, with no model in the loop. |
| [`choice`](https://github.com/explosion/prodigy-recipes/blob/master/other/choice.py) | Annotate data with multiple-choice options. The annotated examples will have an additional property `"accept": []` mapping to the ID(s) of the selected option(s). |
| [`question_answering`](https://github.com/explosion/prodigy-recipes/blob/master/other/question_answering.py) | Annotate question/answer pairs with a custom HTML interface. |

### Community recipes

[](https://github.com/explosion/prodigy-recipes?screenshot=true#community-recipes)

| Recipe | Author | Description |
| --- | --- | --- |
| `phrases.teach` | @kabirkhan | Now part of [`sense2vec`](https://github.com/explosion/sense2vec). |
| `phrases.to-patterns` | @kabirkhan | Now part of [`sense2vec`](https://github.com/explosion/sense2vec). |
| [`records.link`](https://github.com/explosion/prodigy-recipes/blob/master/contrib/dedupe) | @kabirkhan | Link records across multiple datasets using the [`dedupe`](https://github.com/dedupeio/dedupe) library. |

### Tutorial recipes

[](https://github.com/explosion/prodigy-recipes?screenshot=true#tutorial-recipes)

These recipes have made an appearance in one of our tutorials.

| Recipe | Description |
| --- | --- |
| [`span-and-textcat`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/span-and-textcat) | Do both spancat and textcat annotations at the same time. Great for chatbots! |
| [`terms.from-ner`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/terms-from-ner) | Generate terms from previous NER annotations. |
| [`audio-with-transcript`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/audio-with-transcript) | Handles both manual audio annotation as well as transcription. |
| [`progress`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/progress-update) | Demo of an `update`\-callback that tracks annotation speed. |

📚 Example Datasets and Patterns
--------------------------------

[](https://github.com/explosion/prodigy-recipes?screenshot=true#-example-datasets-and-patterns)

To make it even easier to get started, we've also included a few [`example-datasets`](https://github.com/explosion/prodigy-recipes/blob/master/example-datasets), both raw data as well as data containing annotations created with Prodigy. For examples of token-based match patterns to use with recipes like `ner.teach` or `ner.match`, see the [`example-patterns`](https://github.com/explosion/prodigy-recipes/blob/master/example-patterns) directory.

## Metadata

```json
{
  "title": "GitHub - explosion/prodigy-recipes: 🍳 Recipes for the Prodigy, our fully scriptable annotation tool",
  "description": "🍳 Recipes for the Prodigy, our fully scriptable annotation tool - explosion/prodigy-recipes",
  "url": "https://github.com/explosion/prodigy-recipes?screenshot=true",
  "content": "[![Image 18](https://camo.githubusercontent.com/17aebe83d2ca93fc83c7d74ec6a87455a7469e5be43c3933c918a64121725a21/68747470733a2f2f6578706c6f73696f6e2e61692f6173736574732f696d672f6c6f676f2e737667)](https://explosion.ai/)\n\nProdigy Recipes\n---------------\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#prodigy-recipes)\n\nThis repository contains a collection of recipes for [Prodigy](https://prodi.gy/), our scriptable annotation tool for text, images and other data. In order to use this repo, you'll need a license for Prodigy – [see this page](https://prodi.gy/buy) for more details. For questions and bug reports, please use the [Prodigy Support Forum](https://support.prodi.gy/). If you've found a mistake or bug, feel free to submit a [pull request](https://github.com/explosion/prodigy-recipes/pulls).\n\n> ✨ **Important note:** The recipes in this repository aren't 100% identical to the built-in recipes shipped with Prodigy. They've been edited to include comments and more information, and some of them have been simplified to make it easier to follow what's going on, and to use them as the basis for a custom recipe.\n\n📋 Usage\n--------\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#-usage)\n\nOnce Prodigy is installed, you should be able to run the `prodigy` command from your terminal, either directly or via `python -m`:\n\nThe `prodigy` command lists the built-in recipes. To use a custom recipe script, simply pass the path to the file using the `-F` argument:\n\npython -m prodigy ner.teach your\\_dataset en\\_core\\_web\\_sm ./data.jsonl --label PERSON -F prodigy-recipes/ner/ner\\_teach.py\n\nYou can also use the `--help` flag for an overview of the available arguments of a recipe, e.g. `prodigy ner.teach -F ner_teach_.py --help`.\n\n### Some things to try\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#some-things-to-try)\n\nYou can edit the code in the recipe script to customize how Prodigy behaves.\n\n*   Try replacing `prefer_uncertain()` with `prefer_high_scores()`.\n*   Try writing a custom sorting function. It just needs to be a generator that yields a sequence of `example` dicts, given a sequence of `(score, example)` tuples.\n*   Try adding a filter that drops some questions from the stream. For instance, try writing a filter that only asks you questions where the entity is two words long.\n*   Try customizing the `update()` callback, to include extra logging or extra functionality.\n\n🍳 Recipes\n----------\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#-recipes)\n\n### Named Entity Recognition\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#named-entity-recognition)\n\n| Recipe | Description |\n| --- | --- |\n| [`ner.teach`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_teach.py) | Collect the best possible training data for a named entity recognition model with the model in the loop. Based on your annotations, Prodigy will decide which questions to ask next. |\n| [`ner.match`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_match.py) | Suggest phrases that match a given patterns file, and mark whether they are examples of the entity you're interested in. The patterns file can include exact strings or token patterns for use with spaCy's `Matcher`. |\n| [`ner.manual`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_manual.py) | Mark spans manually by token. Requires only a tokenizer and no entity recognizer, and doesn't do any active learning. Optionally, pre-highlight spans based on patterns. |\n| [`ner.fuzzy_manual`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_fuzzy_manual.py) | Like `ner.manual` but use `FuzzyMatcher` from [`spaczz`](https://github.com/gandersen101/spaczz) library to pre-highlight candidates. |\n| [`ner.manual.bert`](https://github.com/explosion/prodigy-recipes/blob/master/other/transformers_tokenizers.py) | Use BERT word piece tokenizer for efficient manual NER annotation for transformer models. |\n| [`ner.correct`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_correct.py) | Create gold-standard data by correcting a model's predictions manually. This recipe used to be called [`ner.make_gold`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_make_gold.py). |\n| [`ner.silver-to-gold`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_silver_to_gold.py) | Take an existing \"silver\" dataset with binary accept/reject annotations, merge the annotations to find the best possible analysis given the constraints defined in the annotations, and manually edit it to create a perfect and complete \"gold\" dataset. |\n| [`ner.eval_ab`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_eval_ab.py) | Evaluate two NER models by comparing their predictions and building an evaluation set from the stream. |\n| [`ner_fuzzy_manual`](https://github.com/explosion/prodigy-recipes/blob/master/ner/ner_fuzzy_manual.py) | Mark spans manually by token with suggestions from [`spaczz fuzzy`](https://spacy.io/universe/project/spaczz) matcher pre-highlighted. |\n\n### Text Classification\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#text-classification)\n\n| Recipe | Description |\n| --- | --- |\n| [`textcat.manual`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_manual.py) | Manually annotate categories that apply to a text. Supports annotation tasks with single and multiple labels. Multiple labels can optionally be flagged as exclusive. |\n| [`textcat.correct`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_correct.py) | Correct the textcat model's predictions manually. Predictions above the acceptance threshold will be automatically preselected (0.5 by default). Prodigy will infer whether the categories should be mutualy exclusive based on the component configuration. |\n| [`textcat.teach`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_teach.py) | Collect the best possible training data for a text classification model with the model in the loop. Based on your annotations, Prodigy will decide which questions to ask next. |\n| [`textcat.custom-model`](https://github.com/explosion/prodigy-recipes/blob/master/textcat/textcat_custom_model.py) | Use active learning-powered text classification with a custom model. To demonstrate how it works, this demo recipe uses a simple dummy model that \"predicts\" random scores. But you can swap it out for any model of your choice, for example a text classification model implementation using PyTorch, TensorFlow or scikit-learn. |\n\n### Terminology\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#terminology)\n\n| Recipe | Description |\n| --- | --- |\n| [`terms.teach`](https://github.com/explosion/prodigy-recipes/blob/master/terms/terms_teach.py) | Bootstrap a terminology list with word vectors and seeds terms. Prodigy will suggest similar terms based on the word vectors, and update the target vector accordingly. |\n\n### Image\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#image)\n\n| Recipe | Description |\n| --- | --- |\n| [`image.manual`](https://github.com/explosion/prodigy-recipes/blob/master/image/image_manual.py) | Manually annotate images by drawing rectangular bounding boxes or polygon shapes on the image. |\n| [`image-caption`](https://github.com/explosion/prodigy-recipes/blob/master/image/image_caption/image_caption.py) | Annotate images with captions, pre-populate captions with image captioning model implemented in PyTorch and perform error analysis. |\n| [`image.frozenmodel`](https://github.com/explosion/prodigy-recipes/blob/master/image/tf_odapi/image_frozen_model.py) | Model in loop manual annotation using [Tensorflow's Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). |\n| [`image.servingmodel`](https://github.com/explosion/prodigy-recipes/blob/master/image/tf_odapi/image_tf_serving.py) | Model in loop manual annotation using [Tensorflow's Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). This uses [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) |\n| [`image.trainmodel`](https://github.com/explosion/prodigy-recipes/blob/master/image/tf_odapi/image_train.py) | Model in loop manual annotation and training using [Tensorflow's Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). |\n\n### Other\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#other)\n\n| Recipe | Description |\n| --- | --- |\n| [`mark`](https://github.com/explosion/prodigy-recipes/blob/master/other/mark.py) | Click through pre-prepared examples, with no model in the loop. |\n| [`choice`](https://github.com/explosion/prodigy-recipes/blob/master/other/choice.py) | Annotate data with multiple-choice options. The annotated examples will have an additional property `\"accept\": []` mapping to the ID(s) of the selected option(s). |\n| [`question_answering`](https://github.com/explosion/prodigy-recipes/blob/master/other/question_answering.py) | Annotate question/answer pairs with a custom HTML interface. |\n\n### Community recipes\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#community-recipes)\n\n| Recipe | Author | Description |\n| --- | --- | --- |\n| `phrases.teach` | @kabirkhan | Now part of [`sense2vec`](https://github.com/explosion/sense2vec). |\n| `phrases.to-patterns` | @kabirkhan | Now part of [`sense2vec`](https://github.com/explosion/sense2vec). |\n| [`records.link`](https://github.com/explosion/prodigy-recipes/blob/master/contrib/dedupe) | @kabirkhan | Link records across multiple datasets using the [`dedupe`](https://github.com/dedupeio/dedupe) library. |\n\n### Tutorial recipes\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#tutorial-recipes)\n\nThese recipes have made an appearance in one of our tutorials.\n\n| Recipe | Description |\n| --- | --- |\n| [`span-and-textcat`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/span-and-textcat) | Do both spancat and textcat annotations at the same time. Great for chatbots! |\n| [`terms.from-ner`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/terms-from-ner) | Generate terms from previous NER annotations. |\n| [`audio-with-transcript`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/audio-with-transcript) | Handles both manual audio annotation as well as transcription. |\n| [`progress`](https://github.com/explosion/prodigy-recipes/blob/master/tutorials/progress-update) | Demo of an `update`\\-callback that tracks annotation speed. |\n\n📚 Example Datasets and Patterns\n--------------------------------\n\n[](https://github.com/explosion/prodigy-recipes?screenshot=true#-example-datasets-and-patterns)\n\nTo make it even easier to get started, we've also included a few [`example-datasets`](https://github.com/explosion/prodigy-recipes/blob/master/example-datasets), both raw data as well as data containing annotations created with Prodigy. For examples of token-based match patterns to use with recipes like `ner.teach` or `ner.match`, see the [`example-patterns`](https://github.com/explosion/prodigy-recipes/blob/master/example-patterns) directory.",
  "usage": {
    "tokens": 2698
  }
}
```
