---
title: Clustering - Spark 3.5.4 Documentation
description: 
url: https://spark.apache.org/docs/latest/ml-clustering.html
timestamp: 2025-01-20T15:51:34.998Z
domain: spark.apache.org
path: docs_latest_ml-clustering.html
---

# Clustering - Spark 3.5.4 Documentation



## Content

This page describes clustering algorithms in MLlib. The [guide for clustering in the RDD-based API](https://spark.apache.org/docs/latest/mllib-clustering.html) also has relevant information about these algorithms.

**Table of Contents**

*   [K-means](https://spark.apache.org/docs/latest/ml-clustering.html#k-means)
    *   [Input Columns](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns)
    *   [Output Columns](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns)
*   [Latent Dirichlet allocation (LDA)](https://spark.apache.org/docs/latest/ml-clustering.html#latent-dirichlet-allocation-lda)
*   [Bisecting k-means](https://spark.apache.org/docs/latest/ml-clustering.html#bisecting-k-means)
*   [Gaussian Mixture Model (GMM)](https://spark.apache.org/docs/latest/ml-clustering.html#gaussian-mixture-model-gmm)
    *   [Input Columns](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns-1)
    *   [Output Columns](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns-1)
*   [Power Iteration Clustering (PIC)](https://spark.apache.org/docs/latest/ml-clustering.html#power-iteration-clustering-pic)

K-means
-------

[k-means](http://en.wikipedia.org/wiki/K-means_clustering) is one of the most commonly used clustering algorithms that clusters the data points into a predefined number of clusters. The MLlib implementation includes a parallelized variant of the [k-means++](http://en.wikipedia.org/wiki/K-means%2B%2B) method called [kmeans||](http://theory.stanford.edu/~sergei/papers/vldb12-kmpar.pdf).

`KMeans` is implemented as an `Estimator` and generates a `KMeansModel` as the base model.

### Input Columns

| Param name | Type(s) | Default | Description |
| --- | --- | --- | --- |
| featuresCol | Vector | "features" | Feature vector |

### Output Columns

| Param name | Type(s) | Default | Description |
| --- | --- | --- | --- |
| predictionCol | Int | "prediction" | Predicted cluster center |

**Examples**

Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.KMeans.html) for more details.

```
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Loads data.
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

# Trains a k-means model.
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(dataset)

# Make predictions
predictions = model.transform(dataset)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
```

Find full example code at "examples/src/main/python/ml/kmeans\_example.py" in the Spark repo.

Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/KMeans.html) for more details.

```
import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.evaluation.ClusteringEvaluator

// Loads data.
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains a k-means model.
val kmeans = new KMeans().setK(2).setSeed(1L)
val model = kmeans.fit(dataset)

// Make predictions
val predictions = model.transform(dataset)

// Evaluate clustering by computing Silhouette score
val evaluator = new ClusteringEvaluator()

val silhouette = evaluator.evaluate(predictions)
println(s"Silhouette with squared euclidean distance = $silhouette")

// Shows the result.
println("Cluster Centers: ")
model.clusterCenters.foreach(println)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/KMeansExample.scala" in the Spark repo.

Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeans.html) for more details.

```
import org.apache.spark.ml.clustering.KMeansModel;
import org.apache.spark.ml.clustering.KMeans;
import org.apache.spark.ml.evaluation.ClusteringEvaluator;
import org.apache.spark.ml.linalg.Vector;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Loads data.
Dataset<Row> dataset = spark.read().format("libsvm").load("data/mllib/sample_kmeans_data.txt");

// Trains a k-means model.
KMeans kmeans = new KMeans().setK(2).setSeed(1L);
KMeansModel model = kmeans.fit(dataset);

// Make predictions
Dataset<Row> predictions = model.transform(dataset);

// Evaluate clustering by computing Silhouette score
ClusteringEvaluator evaluator = new ClusteringEvaluator();

double silhouette = evaluator.evaluate(predictions);
System.out.println("Silhouette with squared euclidean distance = " + silhouette);

// Shows the result.
Vector[] centers = model.clusterCenters();
System.out.println("Cluster Centers: ");
for (Vector center: centers) {
  System.out.println(center);
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaKMeansExample.java" in the Spark repo.

Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html) for more details.

```
# Fit a k-means model with spark.kmeans
t <- as.data.frame(Titanic)
training <- createDataFrame(t)
df_list <- randomSplit(training, c(7,3), 2)
kmeansDF <- df_list[[1]]
kmeansTestDF <- df_list[[2]]
kmeansModel <- spark.kmeans(kmeansDF, ~ Class + Sex + Age + Freq,
                            k = 3)

# Model summary
summary(kmeansModel)

# Get fitted result from the k-means model
head(fitted(kmeansModel))

# Prediction
kmeansPredictions <- predict(kmeansModel, kmeansTestDF)
head(kmeansPredictions)
```

Find full example code at "examples/src/main/r/ml/kmeans.R" in the Spark repo.

Latent Dirichlet allocation (LDA)
---------------------------------

`LDA` is implemented as an `Estimator` that supports both `EMLDAOptimizer` and `OnlineLDAOptimizer`, and generates a `LDAModel` as the base model. Expert users may cast a `LDAModel` generated by `EMLDAOptimizer` to a `DistributedLDAModel` if needed.

**Examples**

Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.LDA.html) for more details.

```
from pyspark.ml.clustering import LDA

# Loads data.
dataset = spark.read.format("libsvm").load("data/mllib/sample_lda_libsvm_data.txt")

# Trains a LDA model.
lda = LDA(k=10, maxIter=10)
model = lda.fit(dataset)

ll = model.logLikelihood(dataset)
lp = model.logPerplexity(dataset)
print("The lower bound on the log likelihood of the entire corpus: " + str(ll))
print("The upper bound on perplexity: " + str(lp))

# Describe topics.
topics = model.describeTopics(3)
print("The topics described by their top-weighted terms:")
topics.show(truncate=False)

# Shows the result
transformed = model.transform(dataset)
transformed.show(truncate=False)
```

Find full example code at "examples/src/main/python/ml/lda\_example.py" in the Spark repo.

Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/LDA.html) for more details.

```
import org.apache.spark.ml.clustering.LDA

// Loads data.
val dataset = spark.read.format("libsvm")
  .load("data/mllib/sample_lda_libsvm_data.txt")

// Trains a LDA model.
val lda = new LDA().setK(10).setMaxIter(10)
val model = lda.fit(dataset)

val ll = model.logLikelihood(dataset)
val lp = model.logPerplexity(dataset)
println(s"The lower bound on the log likelihood of the entire corpus: $ll")
println(s"The upper bound on perplexity: $lp")

// Describe topics.
val topics = model.describeTopics(3)
println("The topics described by their top-weighted terms:")
topics.show(false)

// Shows the result.
val transformed = model.transform(dataset)
transformed.show(false)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/LDAExample.scala" in the Spark repo.

Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDA.html) for more details.

```
import org.apache.spark.ml.clustering.LDA;
import org.apache.spark.ml.clustering.LDAModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

// Loads data.
Dataset<Row> dataset = spark.read().format("libsvm")
  .load("data/mllib/sample_lda_libsvm_data.txt");

// Trains a LDA model.
LDA lda = new LDA().setK(10).setMaxIter(10);
LDAModel model = lda.fit(dataset);

double ll = model.logLikelihood(dataset);
double lp = model.logPerplexity(dataset);
System.out.println("The lower bound on the log likelihood of the entire corpus: " + ll);
System.out.println("The upper bound on perplexity: " + lp);

// Describe topics.
Dataset<Row> topics = model.describeTopics(3);
System.out.println("The topics described by their top-weighted terms:");
topics.show(false);

// Shows the result.
Dataset<Row> transformed = model.transform(dataset);
transformed.show(false);
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaLDAExample.java" in the Spark repo.

Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html) for more details.

```
# Load training data
df <- read.df("data/mllib/sample_lda_libsvm_data.txt", source = "libsvm")
training <- df
test <- df

# Fit a latent dirichlet allocation model with spark.lda
model <- spark.lda(training, k = 10, maxIter = 10)

# Model summary
summary(model)

# Posterior probabilities
posterior <- spark.posterior(model, test)
head(posterior)

# The log perplexity of the LDA model
logPerplexity <- spark.perplexity(model, test)
print(paste0("The upper bound bound on perplexity: ", logPerplexity))
```

Find full example code at "examples/src/main/r/ml/lda.R" in the Spark repo.

Bisecting k-means
-----------------

Bisecting k-means is a kind of [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering) using a divisive (or “top-down”) approach: all observations start in one cluster, and splits are performed recursively as one moves down the hierarchy.

Bisecting K-means can often be much faster than regular K-means, but it will generally produce a different clustering.

`BisectingKMeans` is implemented as an `Estimator` and generates a `BisectingKMeansModel` as the base model.

**Examples**

Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.BisectingKMeans.html) for more details.

```
from pyspark.ml.clustering import BisectingKMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Loads data.
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

# Trains a bisecting k-means model.
bkm = BisectingKMeans().setK(2).setSeed(1)
model = bkm.fit(dataset)

# Make predictions
predictions = model.transform(dataset)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the result.
print("Cluster Centers: ")
centers = model.clusterCenters()
for center in centers:
    print(center)
```

Find full example code at "examples/src/main/python/ml/bisecting\_k\_means\_example.py" in the Spark repo.

Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/BisectingKMeans.html) for more details.

```
import org.apache.spark.ml.clustering.BisectingKMeans
import org.apache.spark.ml.evaluation.ClusteringEvaluator

// Loads data.
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains a bisecting k-means model.
val bkm = new BisectingKMeans().setK(2).setSeed(1)
val model = bkm.fit(dataset)

// Make predictions
val predictions = model.transform(dataset)

// Evaluate clustering by computing Silhouette score
val evaluator = new ClusteringEvaluator()

val silhouette = evaluator.evaluate(predictions)
println(s"Silhouette with squared euclidean distance = $silhouette")

// Shows the result.
println("Cluster Centers: ")
val centers = model.clusterCenters
centers.foreach(println)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/BisectingKMeansExample.scala" in the Spark repo.

Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeans.html) for more details.

```
import org.apache.spark.ml.clustering.BisectingKMeans;
import org.apache.spark.ml.clustering.BisectingKMeansModel;
import org.apache.spark.ml.evaluation.ClusteringEvaluator;
import org.apache.spark.ml.linalg.Vector;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Loads data.
Dataset<Row> dataset = spark.read().format("libsvm").load("data/mllib/sample_kmeans_data.txt");

// Trains a bisecting k-means model.
BisectingKMeans bkm = new BisectingKMeans().setK(2).setSeed(1);
BisectingKMeansModel model = bkm.fit(dataset);

// Make predictions
Dataset<Row> predictions = model.transform(dataset);

// Evaluate clustering by computing Silhouette score
ClusteringEvaluator evaluator = new ClusteringEvaluator();

double silhouette = evaluator.evaluate(predictions);
System.out.println("Silhouette with squared euclidean distance = " + silhouette);

// Shows the result.
System.out.println("Cluster Centers: ");
Vector[] centers = model.clusterCenters();
for (Vector center : centers) {
  System.out.println(center);
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaBisectingKMeansExample.java" in the Spark repo.

Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html) for more details.

```
t <- as.data.frame(Titanic)
training <- createDataFrame(t)

# Fit bisecting k-means model with four centers
model <- spark.bisectingKmeans(training, Class ~ Survived, k = 4)

# get fitted result from a bisecting k-means model
fitted.model <- fitted(model, "centers")

# Model summary
head(summary(fitted.model))

# fitted values on training data
fitted <- predict(model, training)
head(select(fitted, "Class", "prediction"))
```

Find full example code at "examples/src/main/r/ml/bisectingKmeans.R" in the Spark repo.

Gaussian Mixture Model (GMM)
----------------------------

A [Gaussian Mixture Model](http://en.wikipedia.org/wiki/Mixture_model#Multivariate_Gaussian_mixture_model) represents a composite distribution whereby points are drawn from one of _k_ Gaussian sub-distributions, each with its own probability. The `spark.ml` implementation uses the [expectation-maximization](http://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) algorithm to induce the maximum-likelihood model given a set of samples.

`GaussianMixture` is implemented as an `Estimator` and generates a `GaussianMixtureModel` as the base model.

### Input Columns

| Param name | Type(s) | Default | Description |
| --- | --- | --- | --- |
| featuresCol | Vector | "features" | Feature vector |

### Output Columns

| Param name | Type(s) | Default | Description |
| --- | --- | --- | --- |
| predictionCol | Int | "prediction" | Predicted cluster center |
| probabilityCol | Vector | "probability" | Probability of each cluster |

**Examples**

Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.GaussianMixture.html) for more details.

```
from pyspark.ml.clustering import GaussianMixture

# loads data
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

gmm = GaussianMixture().setK(2).setSeed(538009335)
model = gmm.fit(dataset)

print("Gaussians shown as a DataFrame: ")
model.gaussiansDF.show(truncate=False)
```

Find full example code at "examples/src/main/python/ml/gaussian\_mixture\_example.py" in the Spark repo.

Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/GaussianMixture.html) for more details.

```
import org.apache.spark.ml.clustering.GaussianMixture

// Loads data
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains Gaussian Mixture Model
val gmm = new GaussianMixture()
  .setK(2)
val model = gmm.fit(dataset)

// output parameters of mixture model model
for (i <- 0 until model.getK) {
  println(s"Gaussian $i:\nweight=${model.weights(i)}\n" +
      s"mu=${model.gaussians(i).mean}\nsigma=\n${model.gaussians(i).cov}\n")
}
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/GaussianMixtureExample.scala" in the Spark repo.

Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixture.html) for more details.

```
import org.apache.spark.ml.clustering.GaussianMixture;
import org.apache.spark.ml.clustering.GaussianMixtureModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Loads data
Dataset<Row> dataset = spark.read().format("libsvm").load("data/mllib/sample_kmeans_data.txt");

// Trains a GaussianMixture model
GaussianMixture gmm = new GaussianMixture()
  .setK(2);
GaussianMixtureModel model = gmm.fit(dataset);

// Output the parameters of the mixture model
for (int i = 0; i < model.getK(); i++) {
  System.out.printf("Gaussian %d:\nweight=%f\nmu=%s\nsigma=\n%s\n\n",
          i, model.weights()[i], model.gaussians()[i].mean(), model.gaussians()[i].cov());
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaGaussianMixtureExample.java" in the Spark repo.

Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html) for more details.

```
# Load training data
df <- read.df("data/mllib/sample_kmeans_data.txt", source = "libsvm")
training <- df
test <- df

# Fit a gaussian mixture clustering model with spark.gaussianMixture
model <- spark.gaussianMixture(training, ~ features, k = 2)

# Model summary
summary(model)

# Prediction
predictions <- predict(model, test)
head(predictions)
```

Find full example code at "examples/src/main/r/ml/gaussianMixture.R" in the Spark repo.

Power Iteration Clustering (PIC)
--------------------------------

Power Iteration Clustering (PIC) is a scalable graph clustering algorithm developed by [Lin and Cohen](http://www.cs.cmu.edu/~frank/papers/icml2010-pic-final.pdf). From the abstract: PIC finds a very low-dimensional embedding of a dataset using truncated power iteration on a normalized pair-wise similarity matrix of the data.

`spark.ml`’s PowerIterationClustering implementation takes the following parameters:

*   `k`: the number of clusters to create
*   `initMode`: param for the initialization algorithm
*   `maxIter`: param for maximum number of iterations
*   `srcCol`: param for the name of the input column for source vertex IDs
*   `dstCol`: name of the input column for destination vertex IDs
*   `weightCol`: Param for weight column name

**Examples**

Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.PowerIterationClustering.html) for more details.

```
from pyspark.ml.clustering import PowerIterationClustering

df = spark.createDataFrame([
    (0, 1, 1.0),
    (0, 2, 1.0),
    (1, 2, 1.0),
    (3, 4, 1.0),
    (4, 0, 0.1)
], ["src", "dst", "weight"])

pic = PowerIterationClustering(k=2, maxIter=20, initMode="degree", weightCol="weight")

# Shows the cluster assignment
pic.assignClusters(df).show()
```

Find full example code at "examples/src/main/python/ml/power\_iteration\_clustering\_example.py" in the Spark repo.

Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/PowerIterationClustering.html) for more details.

```
import org.apache.spark.ml.clustering.PowerIterationClustering

val dataset = spark.createDataFrame(Seq(
  (0L, 1L, 1.0),
  (0L, 2L, 1.0),
  (1L, 2L, 1.0),
  (3L, 4L, 1.0),
  (4L, 0L, 0.1)
)).toDF("src", "dst", "weight")

val model = new PowerIterationClustering().
  setK(2).
  setMaxIter(20).
  setInitMode("degree").
  setWeightCol("weight")

val prediction = model.assignClusters(dataset).select("id", "cluster")

//  Shows the cluster assignment
prediction.show(false)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/PowerIterationClusteringExample.scala" in the Spark repo.

Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/PowerIterationClustering.html) for more details.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.clustering.PowerIterationClustering;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.Metadata;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

List<Row> data = Arrays.asList(
  RowFactory.create(0L, 1L, 1.0),
  RowFactory.create(0L, 2L, 1.0),
  RowFactory.create(1L, 2L, 1.0),
  RowFactory.create(3L, 4L, 1.0),
  RowFactory.create(4L, 0L, 0.1)
);

StructType schema = new StructType(new StructField[]{
  new StructField("src", DataTypes.LongType, false, Metadata.empty()),
  new StructField("dst", DataTypes.LongType, false, Metadata.empty()),
  new StructField("weight", DataTypes.DoubleType, false, Metadata.empty())
});

Dataset<Row> df = spark.createDataFrame(data, schema);

PowerIterationClustering model = new PowerIterationClustering()
  .setK(2)
  .setMaxIter(10)
  .setInitMode("degree")
  .setWeightCol("weight");

Dataset<Row> result = model.assignClusters(df);
result.show(false);
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaPowerIterationClusteringExample.java" in the Spark repo.

Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html) for more details.

```
df <- createDataFrame(list(list(0L, 1L, 1.0), list(0L, 2L, 1.0),
                           list(1L, 2L, 1.0), list(3L, 4L, 1.0),
                           list(4L, 0L, 0.1)),
                      schema = c("src", "dst", "weight"))
# assign clusters
clusters <- spark.assignClusters(df, k = 2L, maxIter = 20L,
                                 initMode = "degree", weightCol = "weight")

showDF(arrange(clusters, clusters$id))
```

Find full example code at "examples/src/main/r/ml/powerIterationClustering.R" in the Spark repo.

## Metadata

```json
{
  "title": "Clustering - Spark 3.5.4 Documentation",
  "description": "",
  "url": "https://spark.apache.org/docs/latest/ml-clustering.html",
  "content": "This page describes clustering algorithms in MLlib. The [guide for clustering in the RDD-based API](https://spark.apache.org/docs/latest/mllib-clustering.html) also has relevant information about these algorithms.\n\n**Table of Contents**\n\n*   [K-means](https://spark.apache.org/docs/latest/ml-clustering.html#k-means)\n    *   [Input Columns](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns)\n    *   [Output Columns](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns)\n*   [Latent Dirichlet allocation (LDA)](https://spark.apache.org/docs/latest/ml-clustering.html#latent-dirichlet-allocation-lda)\n*   [Bisecting k-means](https://spark.apache.org/docs/latest/ml-clustering.html#bisecting-k-means)\n*   [Gaussian Mixture Model (GMM)](https://spark.apache.org/docs/latest/ml-clustering.html#gaussian-mixture-model-gmm)\n    *   [Input Columns](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns-1)\n    *   [Output Columns](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns-1)\n*   [Power Iteration Clustering (PIC)](https://spark.apache.org/docs/latest/ml-clustering.html#power-iteration-clustering-pic)\n\nK-means\n-------\n\n[k-means](http://en.wikipedia.org/wiki/K-means_clustering) is one of the most commonly used clustering algorithms that clusters the data points into a predefined number of clusters. The MLlib implementation includes a parallelized variant of the [k-means++](http://en.wikipedia.org/wiki/K-means%2B%2B) method called [kmeans||](http://theory.stanford.edu/~sergei/papers/vldb12-kmpar.pdf).\n\n`KMeans` is implemented as an `Estimator` and generates a `KMeansModel` as the base model.\n\n### Input Columns\n\n| Param name | Type(s) | Default | Description |\n| --- | --- | --- | --- |\n| featuresCol | Vector | \"features\" | Feature vector |\n\n### Output Columns\n\n| Param name | Type(s) | Default | Description |\n| --- | --- | --- | --- |\n| predictionCol | Int | \"prediction\" | Predicted cluster center |\n\n**Examples**\n\nRefer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.KMeans.html) for more details.\n\n```\nfrom pyspark.ml.clustering import KMeans\nfrom pyspark.ml.evaluation import ClusteringEvaluator\n\n# Loads data.\ndataset = spark.read.format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\")\n\n# Trains a k-means model.\nkmeans = KMeans().setK(2).setSeed(1)\nmodel = kmeans.fit(dataset)\n\n# Make predictions\npredictions = model.transform(dataset)\n\n# Evaluate clustering by computing Silhouette score\nevaluator = ClusteringEvaluator()\n\nsilhouette = evaluator.evaluate(predictions)\nprint(\"Silhouette with squared euclidean distance = \" + str(silhouette))\n\n# Shows the result.\ncenters = model.clusterCenters()\nprint(\"Cluster Centers: \")\nfor center in centers:\n    print(center)\n```\n\nFind full example code at \"examples/src/main/python/ml/kmeans\\_example.py\" in the Spark repo.\n\nRefer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/KMeans.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.KMeans\nimport org.apache.spark.ml.evaluation.ClusteringEvaluator\n\n// Loads data.\nval dataset = spark.read.format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\")\n\n// Trains a k-means model.\nval kmeans = new KMeans().setK(2).setSeed(1L)\nval model = kmeans.fit(dataset)\n\n// Make predictions\nval predictions = model.transform(dataset)\n\n// Evaluate clustering by computing Silhouette score\nval evaluator = new ClusteringEvaluator()\n\nval silhouette = evaluator.evaluate(predictions)\nprintln(s\"Silhouette with squared euclidean distance = $silhouette\")\n\n// Shows the result.\nprintln(\"Cluster Centers: \")\nmodel.clusterCenters.foreach(println)\n```\n\nFind full example code at \"examples/src/main/scala/org/apache/spark/examples/ml/KMeansExample.scala\" in the Spark repo.\n\nRefer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeans.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.KMeansModel;\nimport org.apache.spark.ml.clustering.KMeans;\nimport org.apache.spark.ml.evaluation.ClusteringEvaluator;\nimport org.apache.spark.ml.linalg.Vector;\nimport org.apache.spark.sql.Dataset;\nimport org.apache.spark.sql.Row;\n\n// Loads data.\nDataset<Row> dataset = spark.read().format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\");\n\n// Trains a k-means model.\nKMeans kmeans = new KMeans().setK(2).setSeed(1L);\nKMeansModel model = kmeans.fit(dataset);\n\n// Make predictions\nDataset<Row> predictions = model.transform(dataset);\n\n// Evaluate clustering by computing Silhouette score\nClusteringEvaluator evaluator = new ClusteringEvaluator();\n\ndouble silhouette = evaluator.evaluate(predictions);\nSystem.out.println(\"Silhouette with squared euclidean distance = \" + silhouette);\n\n// Shows the result.\nVector[] centers = model.clusterCenters();\nSystem.out.println(\"Cluster Centers: \");\nfor (Vector center: centers) {\n  System.out.println(center);\n}\n```\n\nFind full example code at \"examples/src/main/java/org/apache/spark/examples/ml/JavaKMeansExample.java\" in the Spark repo.\n\nRefer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html) for more details.\n\n```\n# Fit a k-means model with spark.kmeans\nt <- as.data.frame(Titanic)\ntraining <- createDataFrame(t)\ndf_list <- randomSplit(training, c(7,3), 2)\nkmeansDF <- df_list[[1]]\nkmeansTestDF <- df_list[[2]]\nkmeansModel <- spark.kmeans(kmeansDF, ~ Class + Sex + Age + Freq,\n                            k = 3)\n\n# Model summary\nsummary(kmeansModel)\n\n# Get fitted result from the k-means model\nhead(fitted(kmeansModel))\n\n# Prediction\nkmeansPredictions <- predict(kmeansModel, kmeansTestDF)\nhead(kmeansPredictions)\n```\n\nFind full example code at \"examples/src/main/r/ml/kmeans.R\" in the Spark repo.\n\nLatent Dirichlet allocation (LDA)\n---------------------------------\n\n`LDA` is implemented as an `Estimator` that supports both `EMLDAOptimizer` and `OnlineLDAOptimizer`, and generates a `LDAModel` as the base model. Expert users may cast a `LDAModel` generated by `EMLDAOptimizer` to a `DistributedLDAModel` if needed.\n\n**Examples**\n\nRefer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.LDA.html) for more details.\n\n```\nfrom pyspark.ml.clustering import LDA\n\n# Loads data.\ndataset = spark.read.format(\"libsvm\").load(\"data/mllib/sample_lda_libsvm_data.txt\")\n\n# Trains a LDA model.\nlda = LDA(k=10, maxIter=10)\nmodel = lda.fit(dataset)\n\nll = model.logLikelihood(dataset)\nlp = model.logPerplexity(dataset)\nprint(\"The lower bound on the log likelihood of the entire corpus: \" + str(ll))\nprint(\"The upper bound on perplexity: \" + str(lp))\n\n# Describe topics.\ntopics = model.describeTopics(3)\nprint(\"The topics described by their top-weighted terms:\")\ntopics.show(truncate=False)\n\n# Shows the result\ntransformed = model.transform(dataset)\ntransformed.show(truncate=False)\n```\n\nFind full example code at \"examples/src/main/python/ml/lda\\_example.py\" in the Spark repo.\n\nRefer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/LDA.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.LDA\n\n// Loads data.\nval dataset = spark.read.format(\"libsvm\")\n  .load(\"data/mllib/sample_lda_libsvm_data.txt\")\n\n// Trains a LDA model.\nval lda = new LDA().setK(10).setMaxIter(10)\nval model = lda.fit(dataset)\n\nval ll = model.logLikelihood(dataset)\nval lp = model.logPerplexity(dataset)\nprintln(s\"The lower bound on the log likelihood of the entire corpus: $ll\")\nprintln(s\"The upper bound on perplexity: $lp\")\n\n// Describe topics.\nval topics = model.describeTopics(3)\nprintln(\"The topics described by their top-weighted terms:\")\ntopics.show(false)\n\n// Shows the result.\nval transformed = model.transform(dataset)\ntransformed.show(false)\n```\n\nFind full example code at \"examples/src/main/scala/org/apache/spark/examples/ml/LDAExample.scala\" in the Spark repo.\n\nRefer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDA.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.LDA;\nimport org.apache.spark.ml.clustering.LDAModel;\nimport org.apache.spark.sql.Dataset;\nimport org.apache.spark.sql.Row;\nimport org.apache.spark.sql.SparkSession;\n\n// Loads data.\nDataset<Row> dataset = spark.read().format(\"libsvm\")\n  .load(\"data/mllib/sample_lda_libsvm_data.txt\");\n\n// Trains a LDA model.\nLDA lda = new LDA().setK(10).setMaxIter(10);\nLDAModel model = lda.fit(dataset);\n\ndouble ll = model.logLikelihood(dataset);\ndouble lp = model.logPerplexity(dataset);\nSystem.out.println(\"The lower bound on the log likelihood of the entire corpus: \" + ll);\nSystem.out.println(\"The upper bound on perplexity: \" + lp);\n\n// Describe topics.\nDataset<Row> topics = model.describeTopics(3);\nSystem.out.println(\"The topics described by their top-weighted terms:\");\ntopics.show(false);\n\n// Shows the result.\nDataset<Row> transformed = model.transform(dataset);\ntransformed.show(false);\n```\n\nFind full example code at \"examples/src/main/java/org/apache/spark/examples/ml/JavaLDAExample.java\" in the Spark repo.\n\nRefer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html) for more details.\n\n```\n# Load training data\ndf <- read.df(\"data/mllib/sample_lda_libsvm_data.txt\", source = \"libsvm\")\ntraining <- df\ntest <- df\n\n# Fit a latent dirichlet allocation model with spark.lda\nmodel <- spark.lda(training, k = 10, maxIter = 10)\n\n# Model summary\nsummary(model)\n\n# Posterior probabilities\nposterior <- spark.posterior(model, test)\nhead(posterior)\n\n# The log perplexity of the LDA model\nlogPerplexity <- spark.perplexity(model, test)\nprint(paste0(\"The upper bound bound on perplexity: \", logPerplexity))\n```\n\nFind full example code at \"examples/src/main/r/ml/lda.R\" in the Spark repo.\n\nBisecting k-means\n-----------------\n\nBisecting k-means is a kind of [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering) using a divisive (or “top-down”) approach: all observations start in one cluster, and splits are performed recursively as one moves down the hierarchy.\n\nBisecting K-means can often be much faster than regular K-means, but it will generally produce a different clustering.\n\n`BisectingKMeans` is implemented as an `Estimator` and generates a `BisectingKMeansModel` as the base model.\n\n**Examples**\n\nRefer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.BisectingKMeans.html) for more details.\n\n```\nfrom pyspark.ml.clustering import BisectingKMeans\nfrom pyspark.ml.evaluation import ClusteringEvaluator\n\n# Loads data.\ndataset = spark.read.format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\")\n\n# Trains a bisecting k-means model.\nbkm = BisectingKMeans().setK(2).setSeed(1)\nmodel = bkm.fit(dataset)\n\n# Make predictions\npredictions = model.transform(dataset)\n\n# Evaluate clustering by computing Silhouette score\nevaluator = ClusteringEvaluator()\n\nsilhouette = evaluator.evaluate(predictions)\nprint(\"Silhouette with squared euclidean distance = \" + str(silhouette))\n\n# Shows the result.\nprint(\"Cluster Centers: \")\ncenters = model.clusterCenters()\nfor center in centers:\n    print(center)\n```\n\nFind full example code at \"examples/src/main/python/ml/bisecting\\_k\\_means\\_example.py\" in the Spark repo.\n\nRefer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/BisectingKMeans.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.BisectingKMeans\nimport org.apache.spark.ml.evaluation.ClusteringEvaluator\n\n// Loads data.\nval dataset = spark.read.format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\")\n\n// Trains a bisecting k-means model.\nval bkm = new BisectingKMeans().setK(2).setSeed(1)\nval model = bkm.fit(dataset)\n\n// Make predictions\nval predictions = model.transform(dataset)\n\n// Evaluate clustering by computing Silhouette score\nval evaluator = new ClusteringEvaluator()\n\nval silhouette = evaluator.evaluate(predictions)\nprintln(s\"Silhouette with squared euclidean distance = $silhouette\")\n\n// Shows the result.\nprintln(\"Cluster Centers: \")\nval centers = model.clusterCenters\ncenters.foreach(println)\n```\n\nFind full example code at \"examples/src/main/scala/org/apache/spark/examples/ml/BisectingKMeansExample.scala\" in the Spark repo.\n\nRefer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeans.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.BisectingKMeans;\nimport org.apache.spark.ml.clustering.BisectingKMeansModel;\nimport org.apache.spark.ml.evaluation.ClusteringEvaluator;\nimport org.apache.spark.ml.linalg.Vector;\nimport org.apache.spark.sql.Dataset;\nimport org.apache.spark.sql.Row;\n\n// Loads data.\nDataset<Row> dataset = spark.read().format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\");\n\n// Trains a bisecting k-means model.\nBisectingKMeans bkm = new BisectingKMeans().setK(2).setSeed(1);\nBisectingKMeansModel model = bkm.fit(dataset);\n\n// Make predictions\nDataset<Row> predictions = model.transform(dataset);\n\n// Evaluate clustering by computing Silhouette score\nClusteringEvaluator evaluator = new ClusteringEvaluator();\n\ndouble silhouette = evaluator.evaluate(predictions);\nSystem.out.println(\"Silhouette with squared euclidean distance = \" + silhouette);\n\n// Shows the result.\nSystem.out.println(\"Cluster Centers: \");\nVector[] centers = model.clusterCenters();\nfor (Vector center : centers) {\n  System.out.println(center);\n}\n```\n\nFind full example code at \"examples/src/main/java/org/apache/spark/examples/ml/JavaBisectingKMeansExample.java\" in the Spark repo.\n\nRefer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html) for more details.\n\n```\nt <- as.data.frame(Titanic)\ntraining <- createDataFrame(t)\n\n# Fit bisecting k-means model with four centers\nmodel <- spark.bisectingKmeans(training, Class ~ Survived, k = 4)\n\n# get fitted result from a bisecting k-means model\nfitted.model <- fitted(model, \"centers\")\n\n# Model summary\nhead(summary(fitted.model))\n\n# fitted values on training data\nfitted <- predict(model, training)\nhead(select(fitted, \"Class\", \"prediction\"))\n```\n\nFind full example code at \"examples/src/main/r/ml/bisectingKmeans.R\" in the Spark repo.\n\nGaussian Mixture Model (GMM)\n----------------------------\n\nA [Gaussian Mixture Model](http://en.wikipedia.org/wiki/Mixture_model#Multivariate_Gaussian_mixture_model) represents a composite distribution whereby points are drawn from one of _k_ Gaussian sub-distributions, each with its own probability. The `spark.ml` implementation uses the [expectation-maximization](http://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) algorithm to induce the maximum-likelihood model given a set of samples.\n\n`GaussianMixture` is implemented as an `Estimator` and generates a `GaussianMixtureModel` as the base model.\n\n### Input Columns\n\n| Param name | Type(s) | Default | Description |\n| --- | --- | --- | --- |\n| featuresCol | Vector | \"features\" | Feature vector |\n\n### Output Columns\n\n| Param name | Type(s) | Default | Description |\n| --- | --- | --- | --- |\n| predictionCol | Int | \"prediction\" | Predicted cluster center |\n| probabilityCol | Vector | \"probability\" | Probability of each cluster |\n\n**Examples**\n\nRefer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.GaussianMixture.html) for more details.\n\n```\nfrom pyspark.ml.clustering import GaussianMixture\n\n# loads data\ndataset = spark.read.format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\")\n\ngmm = GaussianMixture().setK(2).setSeed(538009335)\nmodel = gmm.fit(dataset)\n\nprint(\"Gaussians shown as a DataFrame: \")\nmodel.gaussiansDF.show(truncate=False)\n```\n\nFind full example code at \"examples/src/main/python/ml/gaussian\\_mixture\\_example.py\" in the Spark repo.\n\nRefer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/GaussianMixture.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.GaussianMixture\n\n// Loads data\nval dataset = spark.read.format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\")\n\n// Trains Gaussian Mixture Model\nval gmm = new GaussianMixture()\n  .setK(2)\nval model = gmm.fit(dataset)\n\n// output parameters of mixture model model\nfor (i <- 0 until model.getK) {\n  println(s\"Gaussian $i:\\nweight=${model.weights(i)}\\n\" +\n      s\"mu=${model.gaussians(i).mean}\\nsigma=\\n${model.gaussians(i).cov}\\n\")\n}\n```\n\nFind full example code at \"examples/src/main/scala/org/apache/spark/examples/ml/GaussianMixtureExample.scala\" in the Spark repo.\n\nRefer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixture.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.GaussianMixture;\nimport org.apache.spark.ml.clustering.GaussianMixtureModel;\nimport org.apache.spark.sql.Dataset;\nimport org.apache.spark.sql.Row;\n\n// Loads data\nDataset<Row> dataset = spark.read().format(\"libsvm\").load(\"data/mllib/sample_kmeans_data.txt\");\n\n// Trains a GaussianMixture model\nGaussianMixture gmm = new GaussianMixture()\n  .setK(2);\nGaussianMixtureModel model = gmm.fit(dataset);\n\n// Output the parameters of the mixture model\nfor (int i = 0; i < model.getK(); i++) {\n  System.out.printf(\"Gaussian %d:\\nweight=%f\\nmu=%s\\nsigma=\\n%s\\n\\n\",\n          i, model.weights()[i], model.gaussians()[i].mean(), model.gaussians()[i].cov());\n}\n```\n\nFind full example code at \"examples/src/main/java/org/apache/spark/examples/ml/JavaGaussianMixtureExample.java\" in the Spark repo.\n\nRefer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html) for more details.\n\n```\n# Load training data\ndf <- read.df(\"data/mllib/sample_kmeans_data.txt\", source = \"libsvm\")\ntraining <- df\ntest <- df\n\n# Fit a gaussian mixture clustering model with spark.gaussianMixture\nmodel <- spark.gaussianMixture(training, ~ features, k = 2)\n\n# Model summary\nsummary(model)\n\n# Prediction\npredictions <- predict(model, test)\nhead(predictions)\n```\n\nFind full example code at \"examples/src/main/r/ml/gaussianMixture.R\" in the Spark repo.\n\nPower Iteration Clustering (PIC)\n--------------------------------\n\nPower Iteration Clustering (PIC) is a scalable graph clustering algorithm developed by [Lin and Cohen](http://www.cs.cmu.edu/~frank/papers/icml2010-pic-final.pdf). From the abstract: PIC finds a very low-dimensional embedding of a dataset using truncated power iteration on a normalized pair-wise similarity matrix of the data.\n\n`spark.ml`’s PowerIterationClustering implementation takes the following parameters:\n\n*   `k`: the number of clusters to create\n*   `initMode`: param for the initialization algorithm\n*   `maxIter`: param for maximum number of iterations\n*   `srcCol`: param for the name of the input column for source vertex IDs\n*   `dstCol`: name of the input column for destination vertex IDs\n*   `weightCol`: Param for weight column name\n\n**Examples**\n\nRefer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.PowerIterationClustering.html) for more details.\n\n```\nfrom pyspark.ml.clustering import PowerIterationClustering\n\ndf = spark.createDataFrame([\n    (0, 1, 1.0),\n    (0, 2, 1.0),\n    (1, 2, 1.0),\n    (3, 4, 1.0),\n    (4, 0, 0.1)\n], [\"src\", \"dst\", \"weight\"])\n\npic = PowerIterationClustering(k=2, maxIter=20, initMode=\"degree\", weightCol=\"weight\")\n\n# Shows the cluster assignment\npic.assignClusters(df).show()\n```\n\nFind full example code at \"examples/src/main/python/ml/power\\_iteration\\_clustering\\_example.py\" in the Spark repo.\n\nRefer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/PowerIterationClustering.html) for more details.\n\n```\nimport org.apache.spark.ml.clustering.PowerIterationClustering\n\nval dataset = spark.createDataFrame(Seq(\n  (0L, 1L, 1.0),\n  (0L, 2L, 1.0),\n  (1L, 2L, 1.0),\n  (3L, 4L, 1.0),\n  (4L, 0L, 0.1)\n)).toDF(\"src\", \"dst\", \"weight\")\n\nval model = new PowerIterationClustering().\n  setK(2).\n  setMaxIter(20).\n  setInitMode(\"degree\").\n  setWeightCol(\"weight\")\n\nval prediction = model.assignClusters(dataset).select(\"id\", \"cluster\")\n\n//  Shows the cluster assignment\nprediction.show(false)\n```\n\nFind full example code at \"examples/src/main/scala/org/apache/spark/examples/ml/PowerIterationClusteringExample.scala\" in the Spark repo.\n\nRefer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/PowerIterationClustering.html) for more details.\n\n```\nimport java.util.Arrays;\nimport java.util.List;\n\nimport org.apache.spark.ml.clustering.PowerIterationClustering;\nimport org.apache.spark.sql.Dataset;\nimport org.apache.spark.sql.Row;\nimport org.apache.spark.sql.RowFactory;\nimport org.apache.spark.sql.SparkSession;\nimport org.apache.spark.sql.types.DataTypes;\nimport org.apache.spark.sql.types.Metadata;\nimport org.apache.spark.sql.types.StructField;\nimport org.apache.spark.sql.types.StructType;\n\nList<Row> data = Arrays.asList(\n  RowFactory.create(0L, 1L, 1.0),\n  RowFactory.create(0L, 2L, 1.0),\n  RowFactory.create(1L, 2L, 1.0),\n  RowFactory.create(3L, 4L, 1.0),\n  RowFactory.create(4L, 0L, 0.1)\n);\n\nStructType schema = new StructType(new StructField[]{\n  new StructField(\"src\", DataTypes.LongType, false, Metadata.empty()),\n  new StructField(\"dst\", DataTypes.LongType, false, Metadata.empty()),\n  new StructField(\"weight\", DataTypes.DoubleType, false, Metadata.empty())\n});\n\nDataset<Row> df = spark.createDataFrame(data, schema);\n\nPowerIterationClustering model = new PowerIterationClustering()\n  .setK(2)\n  .setMaxIter(10)\n  .setInitMode(\"degree\")\n  .setWeightCol(\"weight\");\n\nDataset<Row> result = model.assignClusters(df);\nresult.show(false);\n```\n\nFind full example code at \"examples/src/main/java/org/apache/spark/examples/ml/JavaPowerIterationClusteringExample.java\" in the Spark repo.\n\nRefer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html) for more details.\n\n```\ndf <- createDataFrame(list(list(0L, 1L, 1.0), list(0L, 2L, 1.0),\n                           list(1L, 2L, 1.0), list(3L, 4L, 1.0),\n                           list(4L, 0L, 0.1)),\n                      schema = c(\"src\", \"dst\", \"weight\"))\n# assign clusters\nclusters <- spark.assignClusters(df, k = 2L, maxIter = 20L,\n                                 initMode = \"degree\", weightCol = \"weight\")\n\nshowDF(arrange(clusters, clusters$id))\n```\n\nFind full example code at \"examples/src/main/r/ml/powerIterationClustering.R\" in the Spark repo.",
  "usage": {
    "tokens": 5648
  }
}
```
