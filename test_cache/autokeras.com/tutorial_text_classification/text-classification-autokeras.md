---
title: Text Classification - AutoKeras
description: Documentation for AutoKeras.
url: https://autokeras.com/tutorial/text_classification/
timestamp: 2025-01-20T16:00:52.318Z
domain: autokeras.com
path: tutorial_text_classification
---

# Text Classification - AutoKeras


Documentation for AutoKeras.


## Content

[**View in Colab**](https://colab.research.google.com/github/keras-team/autokeras/blob/master/docs/ipynb/text_classification.ipynb)     [**GitHub source**](https://github.com/keras-team/autokeras/blob/master/docs/py/text_classification.py)

```
import os

import keras
import numpy as np
import tensorflow as tf
from sklearn.datasets import load_files

import autokeras as ak
```

A Simple Example
----------------

The first step is to prepare your data. Here we use the [IMDB dataset](https://keras.io/datasets/#imdb-movie-reviews-sentiment-classification) as an example.

```
dataset = keras.utils.get_file(
    fname="aclImdb.tar.gz",
    origin="http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz",
    extract=True,
)

# set path to dataset
IMDB_DATADIR = os.path.join(os.path.dirname(dataset), "aclImdb")

classes = ["pos", "neg"]
train_data = load_files(
    os.path.join(IMDB_DATADIR, "train"), shuffle=True, categories=classes
)
test_data = load_files(
    os.path.join(IMDB_DATADIR, "test"), shuffle=False, categories=classes
)

x_train = np.array(train_data.data)[:100]
y_train = np.array(train_data.target)[:100]
x_test = np.array(test_data.data)[:100]
y_test = np.array(test_data.target)[:100]

print(x_train.shape)  # (25000,)
print(y_train.shape)  # (25000, 1)
print(x_train[0][:50])  # this film was just brilliant casting
```

The second step is to run the [TextClassifier](https://autokeras.com/text_classifier). As a quick demo, we set epochs to 2. You can also leave the epochs unspecified for an adaptive number of epochs.

```
# Initialize the text classifier.
clf = ak.TextClassifier(
    overwrite=True, max_trials=1
)  # It only tries 1 model as a quick demo.
# Feed the text classifier with training data.
clf.fit(x_train, y_train, epochs=1, batch_size=2)
# Predict with the best model.
predicted_y = clf.predict(x_test)
# Evaluate the best model with testing data.
print(clf.evaluate(x_test, y_test))
```

Validation Data
---------------

By default, AutoKeras use the last 20% of training data as validation data. As shown in the example below, you can use `validation_split` to specify the percentage.

```
clf.fit(
    x_train,
    y_train,
    # Split the training data and use the last 15% as validation data.
    validation_split=0.15,
    epochs=1,
    batch_size=2,
)
```

You can also use your own validation set instead of splitting it from the training data with `validation_data`.

```
split = 5
x_val = x_train[split:]
y_val = y_train[split:]
x_train = x_train[:split]
y_train = y_train[:split]
clf.fit(
    x_train,
    y_train,
    epochs=1,
    # Use your own validation set.
    validation_data=(x_val, y_val),
    batch_size=2,
)
```

Customized Search Space
-----------------------

For advanced users, you may customize your search space by using [AutoModel](https://autokeras.com/auto_model/#automodel-class) instead of [TextClassifier](https://autokeras.com/text_classifier). You can configure the [TextBlock](https://autokeras.com/block/#textblock-class) for some high-level configurations. You can also do not specify these arguments, which would leave the different choices to be tuned automatically. See the following example for detail.

```
input_node = ak.TextInput()
output_node = ak.TextBlock()(input_node)
output_node = ak.ClassificationHead()(output_node)
clf = ak.AutoModel(
    inputs=input_node, outputs=output_node, overwrite=True, max_trials=1
)
clf.fit(x_train, y_train, epochs=1, batch_size=2)
```

Data Format
-----------

The AutoKeras TextClassifier is quite flexible for the data format.

For the text, the input data should be one-dimensional For the classification labels, AutoKeras accepts both plain labels, i.e. strings or integers, and one-hot encoded encoded labels, i.e. vectors of 0s and 1s.

We also support using [tf.data.Dataset](https://www.tensorflow.org/api_docs/python/tf/data/Dataset?version=stable) format for the training data.

```
train_set = tf.data.Dataset.from_tensor_slices(((x_train,), (y_train,))).batch(
    2
)
test_set = tf.data.Dataset.from_tensor_slices(((x_test,), (y_test,))).batch(2)

clf = ak.TextClassifier(overwrite=True, max_trials=1)
# Feed the tensorflow Dataset to the classifier.
clf.fit(train_set.take(2), epochs=1)
# Predict with the best model.
predicted_y = clf.predict(test_set.take(2))
# Evaluate the best model with testing data.
print(clf.evaluate(test_set.take(2)))
```

Reference
---------

[TextClassifier](https://autokeras.com/text_classifier), [AutoModel](https://autokeras.com/auto_model/#automodel-class), [ConvBlock](https://autokeras.com/block/#convblock-class), [TextInput](https://autokeras.com/node/#textinput-class), [ClassificationHead](https://autokeras.com/block/#classificationhead-class).

## Metadata

```json
{
  "title": "Text Classification - AutoKeras",
  "description": "Documentation for AutoKeras.",
  "url": "https://autokeras.com/tutorial/text_classification/",
  "content": "[**View in Colab**](https://colab.research.google.com/github/keras-team/autokeras/blob/master/docs/ipynb/text_classification.ipynb)     [**GitHub source**](https://github.com/keras-team/autokeras/blob/master/docs/py/text_classification.py)\n\n```\nimport os\n\nimport keras\nimport numpy as np\nimport tensorflow as tf\nfrom sklearn.datasets import load_files\n\nimport autokeras as ak\n```\n\nA Simple Example\n----------------\n\nThe first step is to prepare your data. Here we use the [IMDB dataset](https://keras.io/datasets/#imdb-movie-reviews-sentiment-classification) as an example.\n\n```\ndataset = keras.utils.get_file(\n    fname=\"aclImdb.tar.gz\",\n    origin=\"http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz\",\n    extract=True,\n)\n\n# set path to dataset\nIMDB_DATADIR = os.path.join(os.path.dirname(dataset), \"aclImdb\")\n\nclasses = [\"pos\", \"neg\"]\ntrain_data = load_files(\n    os.path.join(IMDB_DATADIR, \"train\"), shuffle=True, categories=classes\n)\ntest_data = load_files(\n    os.path.join(IMDB_DATADIR, \"test\"), shuffle=False, categories=classes\n)\n\nx_train = np.array(train_data.data)[:100]\ny_train = np.array(train_data.target)[:100]\nx_test = np.array(test_data.data)[:100]\ny_test = np.array(test_data.target)[:100]\n\nprint(x_train.shape)  # (25000,)\nprint(y_train.shape)  # (25000, 1)\nprint(x_train[0][:50])  # this film was just brilliant casting\n```\n\nThe second step is to run the [TextClassifier](https://autokeras.com/text_classifier). As a quick demo, we set epochs to 2. You can also leave the epochs unspecified for an adaptive number of epochs.\n\n```\n# Initialize the text classifier.\nclf = ak.TextClassifier(\n    overwrite=True, max_trials=1\n)  # It only tries 1 model as a quick demo.\n# Feed the text classifier with training data.\nclf.fit(x_train, y_train, epochs=1, batch_size=2)\n# Predict with the best model.\npredicted_y = clf.predict(x_test)\n# Evaluate the best model with testing data.\nprint(clf.evaluate(x_test, y_test))\n```\n\nValidation Data\n---------------\n\nBy default, AutoKeras use the last 20% of training data as validation data. As shown in the example below, you can use `validation_split` to specify the percentage.\n\n```\nclf.fit(\n    x_train,\n    y_train,\n    # Split the training data and use the last 15% as validation data.\n    validation_split=0.15,\n    epochs=1,\n    batch_size=2,\n)\n```\n\nYou can also use your own validation set instead of splitting it from the training data with `validation_data`.\n\n```\nsplit = 5\nx_val = x_train[split:]\ny_val = y_train[split:]\nx_train = x_train[:split]\ny_train = y_train[:split]\nclf.fit(\n    x_train,\n    y_train,\n    epochs=1,\n    # Use your own validation set.\n    validation_data=(x_val, y_val),\n    batch_size=2,\n)\n```\n\nCustomized Search Space\n-----------------------\n\nFor advanced users, you may customize your search space by using [AutoModel](https://autokeras.com/auto_model/#automodel-class) instead of [TextClassifier](https://autokeras.com/text_classifier). You can configure the [TextBlock](https://autokeras.com/block/#textblock-class) for some high-level configurations. You can also do not specify these arguments, which would leave the different choices to be tuned automatically. See the following example for detail.\n\n```\ninput_node = ak.TextInput()\noutput_node = ak.TextBlock()(input_node)\noutput_node = ak.ClassificationHead()(output_node)\nclf = ak.AutoModel(\n    inputs=input_node, outputs=output_node, overwrite=True, max_trials=1\n)\nclf.fit(x_train, y_train, epochs=1, batch_size=2)\n```\n\nData Format\n-----------\n\nThe AutoKeras TextClassifier is quite flexible for the data format.\n\nFor the text, the input data should be one-dimensional For the classification labels, AutoKeras accepts both plain labels, i.e. strings or integers, and one-hot encoded encoded labels, i.e. vectors of 0s and 1s.\n\nWe also support using [tf.data.Dataset](https://www.tensorflow.org/api_docs/python/tf/data/Dataset?version=stable) format for the training data.\n\n```\ntrain_set = tf.data.Dataset.from_tensor_slices(((x_train,), (y_train,))).batch(\n    2\n)\ntest_set = tf.data.Dataset.from_tensor_slices(((x_test,), (y_test,))).batch(2)\n\nclf = ak.TextClassifier(overwrite=True, max_trials=1)\n# Feed the tensorflow Dataset to the classifier.\nclf.fit(train_set.take(2), epochs=1)\n# Predict with the best model.\npredicted_y = clf.predict(test_set.take(2))\n# Evaluate the best model with testing data.\nprint(clf.evaluate(test_set.take(2)))\n```\n\nReference\n---------\n\n[TextClassifier](https://autokeras.com/text_classifier), [AutoModel](https://autokeras.com/auto_model/#automodel-class), [ConvBlock](https://autokeras.com/block/#convblock-class), [TextInput](https://autokeras.com/node/#textinput-class), [ClassificationHead](https://autokeras.com/block/#classificationhead-class).",
  "usage": {
    "tokens": 1194
  }
}
```
