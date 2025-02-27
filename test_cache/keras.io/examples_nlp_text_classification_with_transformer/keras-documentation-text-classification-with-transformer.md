---
title: Keras documentation: Text classification with Transformer
description: Keras documentation
url: https://keras.io/examples/nlp/text_classification_with_transformer/
timestamp: 2025-01-20T16:00:45.493Z
domain: keras.io
path: examples_nlp_text_classification_with_transformer
---

# Keras documentation: Text classification with Transformer


Keras documentation


## Content

**Author:** [Apoorv Nandan](https://twitter.com/NandanApoorv)  
**Date created:** 2020/05/10  
**Last modified:** 2024/01/18  
**Description:** Implement a Transformer block as a Keras layer and use it for text classification.

![Image 6](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/text_classification_with_transformer.ipynb) •![Image 7](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/text_classification_with_transformer.py)

* * *

Setup
-----

```
importkeras
fromkerasimport ops
fromkerasimport layers
```

* * *

Implement a Transformer block as a layer
----------------------------------------

```
classTransformerBlock(layers.Layer):
    def__init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super().__init__()
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    defcall(self, inputs):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output)
        return self.layernorm2(out1 + ffn_output)
```

* * *

Implement embedding layer
-------------------------

Two separate embedding layers, one for tokens, one for token index (positions).

```
classTokenAndPositionEmbedding(layers.Layer):
    def__init__(self, maxlen, vocab_size, embed_dim):
        super().__init__()
        self.token_emb = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)
        self.pos_emb = layers.Embedding(input_dim=maxlen, output_dim=embed_dim)

    defcall(self, x):
        maxlen = ops.shape(x)[-1]
        positions = ops.arange(start=0, stop=maxlen, step=1)
        positions = self.pos_emb(positions)
        x = self.token_emb(x)
        return x + positions
```

* * *

Download and prepare dataset
----------------------------

```
vocab_size = 20000  # Only consider the top 20k words
maxlen = 200  # Only consider the first 200 words of each movie review
(x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(num_words=vocab_size)
print(len(x_train), "Training sequences")
print(len(x_val), "Validation sequences")
x_train = keras.utils.pad_sequences(x_train, maxlen=maxlen)
x_val = keras.utils.pad_sequences(x_val, maxlen=maxlen)
```

```
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz
17465344/17464789 [==============================] - 0s 0us/step

<string>:6: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/datasets/imdb.py:159: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  x_train, y_train = np.array(xs[:idx]), np.array(labels[:idx])
/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/datasets/imdb.py:160: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  x_test, y_test = np.array(xs[idx:]), np.array(labels[idx:])

25000 Training sequences
25000 Validation sequences
```

* * *

Create classifier model using transformer layer
-----------------------------------------------

Transformer layer outputs one vector for each time step of our input sequence. Here, we take the mean across all time steps and use a feed forward network on top of it to classify text.

```
embed_dim = 32  # Embedding size for each token
num_heads = 2  # Number of attention heads
ff_dim = 32  # Hidden layer size in feed forward network inside transformer

inputs = layers.Input(shape=(maxlen,))
embedding_layer = TokenAndPositionEmbedding(maxlen, vocab_size, embed_dim)
x = embedding_layer(inputs)
transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)
x = transformer_block(x)
x = layers.GlobalAveragePooling1D()(x)
x = layers.Dropout(0.1)(x)
x = layers.Dense(20, activation="relu")(x)
x = layers.Dropout(0.1)(x)
outputs = layers.Dense(2, activation="softmax")(x)

model = keras.Model(inputs=inputs, outputs=outputs)
```

* * *

Train and Evaluate
------------------

```
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
history = model.fit(
    x_train, y_train, batch_size=32, epochs=2, validation_data=(x_val, y_val)
)
```

```
Epoch 1/2
782/782 [==============================] - 15s 18ms/step - loss: 0.5112 - accuracy: 0.7070 - val_loss: 0.3598 - val_accuracy: 0.8444
Epoch 2/2
782/782 [==============================] - 13s 17ms/step - loss: 0.1942 - accuracy: 0.9297 - val_loss: 0.2977 - val_accuracy: 0.8745
```

## Metadata

```json
{
  "title": "Keras documentation: Text classification with Transformer",
  "description": "Keras documentation",
  "url": "https://keras.io/examples/nlp/text_classification_with_transformer/",
  "content": "**Author:** [Apoorv Nandan](https://twitter.com/NandanApoorv)  \n**Date created:** 2020/05/10  \n**Last modified:** 2024/01/18  \n**Description:** Implement a Transformer block as a Keras layer and use it for text classification.\n\n![Image 6](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/text_classification_with_transformer.ipynb) •![Image 7](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/text_classification_with_transformer.py)\n\n* * *\n\nSetup\n-----\n\n```\nimportkeras\nfromkerasimport ops\nfromkerasimport layers\n```\n\n* * *\n\nImplement a Transformer block as a layer\n----------------------------------------\n\n```\nclassTransformerBlock(layers.Layer):\n    def__init__(self, embed_dim, num_heads, ff_dim, rate=0.1):\n        super().__init__()\n        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)\n        self.ffn = keras.Sequential(\n            [layers.Dense(ff_dim, activation=\"relu\"), layers.Dense(embed_dim),]\n        )\n        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)\n        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)\n        self.dropout1 = layers.Dropout(rate)\n        self.dropout2 = layers.Dropout(rate)\n\n    defcall(self, inputs):\n        attn_output = self.att(inputs, inputs)\n        attn_output = self.dropout1(attn_output)\n        out1 = self.layernorm1(inputs + attn_output)\n        ffn_output = self.ffn(out1)\n        ffn_output = self.dropout2(ffn_output)\n        return self.layernorm2(out1 + ffn_output)\n```\n\n* * *\n\nImplement embedding layer\n-------------------------\n\nTwo separate embedding layers, one for tokens, one for token index (positions).\n\n```\nclassTokenAndPositionEmbedding(layers.Layer):\n    def__init__(self, maxlen, vocab_size, embed_dim):\n        super().__init__()\n        self.token_emb = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)\n        self.pos_emb = layers.Embedding(input_dim=maxlen, output_dim=embed_dim)\n\n    defcall(self, x):\n        maxlen = ops.shape(x)[-1]\n        positions = ops.arange(start=0, stop=maxlen, step=1)\n        positions = self.pos_emb(positions)\n        x = self.token_emb(x)\n        return x + positions\n```\n\n* * *\n\nDownload and prepare dataset\n----------------------------\n\n```\nvocab_size = 20000  # Only consider the top 20k words\nmaxlen = 200  # Only consider the first 200 words of each movie review\n(x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(num_words=vocab_size)\nprint(len(x_train), \"Training sequences\")\nprint(len(x_val), \"Validation sequences\")\nx_train = keras.utils.pad_sequences(x_train, maxlen=maxlen)\nx_val = keras.utils.pad_sequences(x_val, maxlen=maxlen)\n```\n\n```\nDownloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz\n17465344/17464789 [==============================] - 0s 0us/step\n\n<string>:6: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray\n/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/datasets/imdb.py:159: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray\n  x_train, y_train = np.array(xs[:idx]), np.array(labels[:idx])\n/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/datasets/imdb.py:160: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray\n  x_test, y_test = np.array(xs[idx:]), np.array(labels[idx:])\n\n25000 Training sequences\n25000 Validation sequences\n```\n\n* * *\n\nCreate classifier model using transformer layer\n-----------------------------------------------\n\nTransformer layer outputs one vector for each time step of our input sequence. Here, we take the mean across all time steps and use a feed forward network on top of it to classify text.\n\n```\nembed_dim = 32  # Embedding size for each token\nnum_heads = 2  # Number of attention heads\nff_dim = 32  # Hidden layer size in feed forward network inside transformer\n\ninputs = layers.Input(shape=(maxlen,))\nembedding_layer = TokenAndPositionEmbedding(maxlen, vocab_size, embed_dim)\nx = embedding_layer(inputs)\ntransformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)\nx = transformer_block(x)\nx = layers.GlobalAveragePooling1D()(x)\nx = layers.Dropout(0.1)(x)\nx = layers.Dense(20, activation=\"relu\")(x)\nx = layers.Dropout(0.1)(x)\noutputs = layers.Dense(2, activation=\"softmax\")(x)\n\nmodel = keras.Model(inputs=inputs, outputs=outputs)\n```\n\n* * *\n\nTrain and Evaluate\n------------------\n\n```\nmodel.compile(optimizer=\"adam\", loss=\"sparse_categorical_crossentropy\", metrics=[\"accuracy\"])\nhistory = model.fit(\n    x_train, y_train, batch_size=32, epochs=2, validation_data=(x_val, y_val)\n)\n```\n\n```\nEpoch 1/2\n782/782 [==============================] - 15s 18ms/step - loss: 0.5112 - accuracy: 0.7070 - val_loss: 0.3598 - val_accuracy: 0.8444\nEpoch 2/2\n782/782 [==============================] - 13s 17ms/step - loss: 0.1942 - accuracy: 0.9297 - val_loss: 0.2977 - val_accuracy: 0.8745\n```",
  "usage": {
    "tokens": 1430
  }
}
```
