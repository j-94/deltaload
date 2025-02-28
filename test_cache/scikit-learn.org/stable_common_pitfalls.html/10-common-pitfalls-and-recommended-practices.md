---
title: 10. Common pitfalls and recommended practices
description: The purpose of this chapter is to illustrate some common pitfalls and anti-patterns that occur when using scikit-learn. It provides examples of what not to do, along with a corresponding correct ex...
url: https://scikit-learn.org/stable/common_pitfalls.html
timestamp: 2025-01-20T16:01:04.131Z
domain: scikit-learn.org
path: stable_common_pitfalls.html
---

# 10. Common pitfalls and recommended practices


The purpose of this chapter is to illustrate some common pitfalls and anti-patterns that occur when using scikit-learn. It provides examples of what not to do, along with a corresponding correct ex...


## Content

The purpose of this chapter is to illustrate some common pitfalls and anti-patterns that occur when using scikit-learn. It provides examples of what **not** to do, along with a corresponding correct example.

10.1. Inconsistent preprocessing[#](https://scikit-learn.org/stable/common_pitfalls.html#inconsistent-preprocessing "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

scikit-learn provides a library of [Dataset transformations](https://scikit-learn.org/stable/data_transforms.html#data-transforms), which may clean (see [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)), reduce (see [Unsupervised dimensionality reduction](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#data-reduction)), expand (see [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation)) or generate (see [Feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-extraction)) feature representations. If these data transforms are used when training a model, they also must be used on subsequent datasets, whether it’s test data or data in a production system. Otherwise, the feature space will change, and the model will not be able to perform effectively.

For the following example, let’s create a synthetic dataset with a single feature:

\>\>\> from sklearn.datasets import make\_regression
\>\>\> from sklearn.model\_selection import train\_test\_split

\>\>\> random\_state \= 42
\>\>\> X, y \= make\_regression(random\_state\=random\_state, n\_features\=1, noise\=1)
\>\>\> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, test\_size\=0.4, random\_state\=random\_state)

**Wrong**

The train dataset is scaled, but not the test dataset, so model performance on the test dataset is worse than expected:

\>\>\> from sklearn.metrics import mean\_squared\_error
\>\>\> from sklearn.linear\_model import LinearRegression
\>\>\> from sklearn.preprocessing import StandardScaler

\>\>\> scaler \= StandardScaler()
\>\>\> X\_train\_transformed \= scaler.fit\_transform(X\_train)
\>\>\> model \= LinearRegression().fit(X\_train\_transformed, y\_train)
\>\>\> mean\_squared\_error(y\_test, model.predict(X\_test))
62.80...

**Right**

Instead of passing the non-transformed `X_test` to `predict`, we should transform the test data, the same way we transformed the training data:

\>\>\> X\_test\_transformed \= scaler.transform(X\_test)
\>\>\> mean\_squared\_error(y\_test, model.predict(X\_test\_transformed))
0.90...

Alternatively, we recommend using a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline"), which makes it easier to chain transformations with estimators, and reduces the possibility of forgetting a transformation:

\>\>\> from sklearn.pipeline import make\_pipeline

\>\>\> model \= make\_pipeline(StandardScaler(), LinearRegression())
\>\>\> model.fit(X\_train, y\_train)
Pipeline(steps=\[('standardscaler', StandardScaler()),
                ('linearregression', LinearRegression())\])
\>\>\> mean\_squared\_error(y\_test, model.predict(X\_test))
0.90...

Pipelines also help avoiding another common pitfall: leaking the test data into the training data.

10.2. Data leakage[#](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage "Link to this heading")
---------------------------------------------------------------------------------------------------------------

Data leakage occurs when information that would not be available at prediction time is used when building the model. This results in overly optimistic performance estimates, for example from [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation), and thus poorer performance when the model is used on actually novel data, for example during production.

A common cause is not keeping the test and train data subsets separate. Test data should never be used to make choices about the model. **The general rule is to never call** `fit` **on the test data**. While this may sound obvious, this is easy to miss in some cases, for example when applying certain pre-processing steps.

Although both train and test data subsets should receive the same preprocessing transformation (as described in the previous section), it is important that these transformations are only learnt from the training data. For example, if you have a normalization step where you divide by the average value, the average should be the average of the train subset, **not** the average of all the data. If the test subset is included in the average calculation, information from the test subset is influencing the model.

### 10.2.1. How to avoid data leakage[#](https://scikit-learn.org/stable/common_pitfalls.html#how-to-avoid-data-leakage "Link to this heading")

Below are some tips on avoiding data leakage:

*   Always split the data into train and test subsets first, particularly before any preprocessing steps.
    
*   Never include test data when using the `fit` and `fit_transform` methods. Using all the data, e.g., `fit(X)`, can result in overly optimistic scores.
    
    Conversely, the `transform` method should be used on both train and test subsets as the same preprocessing should be applied to all the data. This can be achieved by using `fit_transform` on the train subset and `transform` on the test subset.
    
*   The scikit-learn [pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline) is a great way to prevent data leakage as it ensures that the appropriate method is performed on the correct data subset. The pipeline is ideal for use in cross-validation and hyper-parameter tuning functions.
    

An example of data leakage during preprocessing is detailed below.

### 10.2.2. Data leakage during pre-processing[#](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage-during-pre-processing "Link to this heading")

Note

We here choose to illustrate data leakage with a feature selection step. This risk of leakage is however relevant with almost all transformations in scikit-learn, including (but not limited to) [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler"), [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer"), and [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA").

A number of [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection) functions are available in scikit-learn. They can help remove irrelevant, redundant and noisy features as well as improve your model build time and performance. As with any other type of preprocessing, feature selection should **only** use the training data. Including the test data in feature selection will optimistically bias your model.

To demonstrate we will create this binary classification problem with 10,000 randomly generated features:

\>\>\> import numpy as np
\>\>\> n\_samples, n\_features, n\_classes \= 200, 10000, 2
\>\>\> rng \= np.random.RandomState(42)
\>\>\> X \= rng.standard\_normal((n\_samples, n\_features))
\>\>\> y \= rng.choice(n\_classes, n\_samples)

**Wrong**

Using all the data to perform feature selection results in an accuracy score much higher than chance, even though our targets are completely random. This randomness means that our `X` and `y` are independent and we thus expect the accuracy to be around 0.5. However, since the feature selection step ‘sees’ the test data, the model has an unfair advantage. In the incorrect example below we first use all the data for feature selection and then split the data into training and test subsets for model fitting. The result is a much higher than expected accuracy score:

\>\>\> from sklearn.model\_selection import train\_test\_split
\>\>\> from sklearn.feature\_selection import SelectKBest
\>\>\> from sklearn.ensemble import HistGradientBoostingClassifier
\>\>\> from sklearn.metrics import accuracy\_score

\>\>\> \# Incorrect preprocessing: the entire data is transformed
\>\>\> X\_selected \= SelectKBest(k\=25).fit\_transform(X, y)

\>\>\> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X\_selected, y, random\_state\=42)
\>\>\> gbc \= HistGradientBoostingClassifier(random\_state\=1)
\>\>\> gbc.fit(X\_train, y\_train)
HistGradientBoostingClassifier(random\_state=1)

\>\>\> y\_pred \= gbc.predict(X\_test)
\>\>\> accuracy\_score(y\_test, y\_pred)
0.76

**Right**

To prevent data leakage, it is good practice to split your data into train and test subsets **first**. Feature selection can then be formed using just the train dataset. Notice that whenever we use `fit` or `fit_transform`, we only use the train dataset. The score is now what we would expect for the data, close to chance:

\>\>\> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, random\_state\=42)
\>\>\> select \= SelectKBest(k\=25)
\>\>\> X\_train\_selected \= select.fit\_transform(X\_train, y\_train)

\>\>\> gbc \= HistGradientBoostingClassifier(random\_state\=1)
\>\>\> gbc.fit(X\_train\_selected, y\_train)
HistGradientBoostingClassifier(random\_state=1)

\>\>\> X\_test\_selected \= select.transform(X\_test)
\>\>\> y\_pred \= gbc.predict(X\_test\_selected)
\>\>\> accuracy\_score(y\_test, y\_pred)
0.5

Here again, we recommend using a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline") to chain together the feature selection and model estimators. The pipeline ensures that only the training data is used when performing `fit` and the test data is used only for calculating the accuracy score:

\>\>\> from sklearn.pipeline import make\_pipeline
\>\>\> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, random\_state\=42)
\>\>\> pipeline \= make\_pipeline(SelectKBest(k\=25),
...                          HistGradientBoostingClassifier(random\_state\=1))
\>\>\> pipeline.fit(X\_train, y\_train)
Pipeline(steps=\[('selectkbest', SelectKBest(k=25)),
                ('histgradientboostingclassifier',
                 HistGradientBoostingClassifier(random\_state=1))\])

\>\>\> y\_pred \= pipeline.predict(X\_test)
\>\>\> accuracy\_score(y\_test, y\_pred)
0.5

The pipeline can also be fed into a cross-validation function such as [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score"). Again, the pipeline ensures that the correct data subset and estimator method is used during fitting and predicting:

\>\>\> from sklearn.model\_selection import cross\_val\_score
\>\>\> scores \= cross\_val\_score(pipeline, X, y)
\>\>\> print(f"Mean accuracy: {scores.mean():.2f}+/-{scores.std():.2f}")
Mean accuracy: 0.43+/-0.05

10.3. Controlling randomness[#](https://scikit-learn.org/stable/common_pitfalls.html#controlling-randomness "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

Some scikit-learn objects are inherently random. These are usually estimators (e.g. [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")) and cross-validation splitters (e.g. [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")). The randomness of these objects is controlled via their `random_state` parameter, as described in the [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state). This section expands on the glossary entry, and describes good practices and common pitfalls w.r.t. this subtle parameter.

Note

Recommendation summary

For an optimal robustness of cross-validation (CV) results, pass `RandomState` instances when creating estimators, or leave `random_state` to `None`. Passing integers to CV splitters is usually the safest option and is preferable; passing `RandomState` instances to splitters may sometimes be useful to achieve very specific use-cases. For both estimators and splitters, passing an integer vs passing an instance (or `None`) leads to subtle but significant differences, especially for CV procedures. These differences are important to understand when reporting results.

For reproducible results across executions, remove any use of `random_state=None`.

### 10.3.1. Using `None` or `RandomState` instances, and repeated calls to `fit` and `split`[#](https://scikit-learn.org/stable/common_pitfalls.html#using-none-or-randomstate-instances-and-repeated-calls-to-fit-and-split "Link to this heading")

The `random_state` parameter determines whether multiple calls to [fit](https://scikit-learn.org/stable/glossary.html#term-fit) (for estimators) or to [split](https://scikit-learn.org/stable/glossary.html#term-split) (for CV splitters) will produce the same results, according to these rules:

*   If an integer is passed, calling `fit` or `split` multiple times always yields the same results.
    
*   If `None` or a `RandomState` instance is passed: `fit` and `split` will yield different results each time they are called, and the succession of calls explores all sources of entropy. `None` is the default value for all `random_state` parameters.
    

We here illustrate these rules for both estimators and CV splitters.

Note

Since passing `random_state=None` is equivalent to passing the global `RandomState` instance from `numpy` (`random_state=np.random.mtrand._rand`), we will not explicitly mention `None` here. Everything that applies to instances also applies to using `None`.

#### 10.3.1.1. Estimators[#](https://scikit-learn.org/stable/common_pitfalls.html#estimators "Link to this heading")

Passing instances means that calling `fit` multiple times will not yield the same results, even if the estimator is fitted on the same data and with the same hyper-parameters:

\>\>\> from sklearn.linear\_model import SGDClassifier
\>\>\> from sklearn.datasets import make\_classification
\>\>\> import numpy as np

\>\>\> rng \= np.random.RandomState(0)
\>\>\> X, y \= make\_classification(n\_features\=5, random\_state\=rng)
\>\>\> sgd \= SGDClassifier(random\_state\=rng)

\>\>\> sgd.fit(X, y).coef\_
array(\[\[ 8.85418642,  4.79084103, -3.13077794,  8.11915045, -0.56479934\]\])

\>\>\> sgd.fit(X, y).coef\_
array(\[\[ 6.70814003,  5.25291366, -7.55212743,  5.18197458,  1.37845099\]\])

We can see from the snippet above that repeatedly calling `sgd.fit` has produced different models, even if the data was the same. This is because the Random Number Generator (RNG) of the estimator is consumed (i.e. mutated) when `fit` is called, and this mutated RNG will be used in the subsequent calls to `fit`. In addition, the `rng` object is shared across all objects that use it, and as a consequence, these objects become somewhat inter-dependent. For example, two estimators that share the same `RandomState` instance will influence each other, as we will see later when we discuss cloning. This point is important to keep in mind when debugging.

If we had passed an integer to the `random_state` parameter of the [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier"), we would have obtained the same models, and thus the same scores each time. When we pass an integer, the same RNG is used across all calls to `fit`. What internally happens is that even though the RNG is consumed when `fit` is called, it is always reset to its original state at the beginning of `fit`.

#### 10.3.1.2. CV splitters[#](https://scikit-learn.org/stable/common_pitfalls.html#cv-splitters "Link to this heading")

Randomized CV splitters have a similar behavior when a `RandomState` instance is passed; calling `split` multiple times yields different data splits:

\>\>\> from sklearn.model\_selection import KFold
\>\>\> import numpy as np

\>\>\> X \= y \= np.arange(10)
\>\>\> rng \= np.random.RandomState(0)
\>\>\> cv \= KFold(n\_splits\=2, shuffle\=True, random\_state\=rng)

\>\>\> for train, test in cv.split(X, y):
...     print(train, test)
\[0 3 5 6 7\] \[1 2 4 8 9\]
\[1 2 4 8 9\] \[0 3 5 6 7\]

\>\>\> for train, test in cv.split(X, y):
...     print(train, test)
\[0 4 6 7 8\] \[1 2 3 5 9\]
\[1 2 3 5 9\] \[0 4 6 7 8\]

We can see that the splits are different from the second time `split` is called. This may lead to unexpected results if you compare the performance of multiple estimators by calling `split` many times, as we will see in the next section.

### 10.3.2. Common pitfalls and subtleties[#](https://scikit-learn.org/stable/common_pitfalls.html#common-pitfalls-and-subtleties "Link to this heading")

While the rules that govern the `random_state` parameter are seemingly simple, they do however have some subtle implications. In some cases, this can even lead to wrong conclusions.

#### 10.3.2.1. Estimators[#](https://scikit-learn.org/stable/common_pitfalls.html#id2 "Link to this heading")

**Different \`random\_state\` types lead to different cross-validation procedures**

Depending on the type of the `random_state` parameter, estimators will behave differently, especially in cross-validation procedures. Consider the following snippet:

\>\>\> from sklearn.ensemble import RandomForestClassifier
\>\>\> from sklearn.datasets import make\_classification
\>\>\> from sklearn.model\_selection import cross\_val\_score
\>\>\> import numpy as np

\>\>\> X, y \= make\_classification(random\_state\=0)

\>\>\> rf\_123 \= RandomForestClassifier(random\_state\=123)
\>\>\> cross\_val\_score(rf\_123, X, y)
array(\[0.85, 0.95, 0.95, 0.9 , 0.9 \])

\>\>\> rf\_inst \= RandomForestClassifier(random\_state\=np.random.RandomState(0))
\>\>\> cross\_val\_score(rf\_inst, X, y)
array(\[0.9 , 0.95, 0.95, 0.9 , 0.9 \])

We see that the cross-validated scores of `rf_123` and `rf_inst` are different, as should be expected since we didn’t pass the same `random_state` parameter. However, the difference between these scores is more subtle than it looks, and **the cross-validation procedures that were performed by** [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score") **significantly differ in each case**:

*   Since `rf_123` was passed an integer, every call to `fit` uses the same RNG: this means that all random characteristics of the random forest estimator will be the same for each of the 5 folds of the CV procedure. In particular, the (randomly chosen) subset of features of the estimator will be the same across all folds.
    
*   Since `rf_inst` was passed a `RandomState` instance, each call to `fit` starts from a different RNG. As a result, the random subset of features will be different for each folds.
    

While having a constant estimator RNG across folds isn’t inherently wrong, we usually want CV results that are robust w.r.t. the estimator’s randomness. As a result, passing an instance instead of an integer may be preferable, since it will allow the estimator RNG to vary for each fold.

Note

Here, [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score") will use a non-randomized CV splitter (as is the default), so both estimators will be evaluated on the same splits. This section is not about variability in the splits. Also, whether we pass an integer or an instance to [`make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification") isn’t relevant for our illustration purpose: what matters is what we pass to the [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier") estimator.

Another subtle side effect of passing `RandomState` instances is how [`clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone") will work:

\>\>\> from sklearn import clone
\>\>\> from sklearn.ensemble import RandomForestClassifier
\>\>\> import numpy as np

\>\>\> rng \= np.random.RandomState(0)
\>\>\> a \= RandomForestClassifier(random\_state\=rng)
\>\>\> b \= clone(a)

Since a `RandomState` instance was passed to `a`, `a` and `b` are not clones in the strict sense, but rather clones in the statistical sense: `a` and `b` will still be different models, even when calling `fit(X, y)` on the same data. Moreover, `a` and `b` will influence each-other since they share the same internal RNG: calling `a.fit` will consume `b`’s RNG, and calling `b.fit` will consume `a`’s RNG, since they are the same. This bit is true for any estimators that share a `random_state` parameter; it is not specific to clones.

If an integer were passed, `a` and `b` would be exact clones and they would not influence each other.

#### 10.3.2.2. CV splitters[#](https://scikit-learn.org/stable/common_pitfalls.html#id3 "Link to this heading")

When passed a `RandomState` instance, CV splitters yield different splits each time `split` is called. When comparing different estimators, this can lead to overestimating the variance of the difference in performance between the estimators:

\>\>\> from sklearn.naive\_bayes import GaussianNB
\>\>\> from sklearn.discriminant\_analysis import LinearDiscriminantAnalysis
\>\>\> from sklearn.datasets import make\_classification
\>\>\> from sklearn.model\_selection import KFold
\>\>\> from sklearn.model\_selection import cross\_val\_score
\>\>\> import numpy as np

\>\>\> rng \= np.random.RandomState(0)
\>\>\> X, y \= make\_classification(random\_state\=rng)
\>\>\> cv \= KFold(shuffle\=True, random\_state\=rng)
\>\>\> lda \= LinearDiscriminantAnalysis()
\>\>\> nb \= GaussianNB()

\>\>\> for est in (lda, nb):
...     print(cross\_val\_score(est, X, y, cv\=cv))
\[0.8  0.75 0.75 0.7  0.85\]
\[0.85 0.95 0.95 0.85 0.95\]

Directly comparing the performance of the [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis") estimator vs the [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB") estimator **on each fold** would be a mistake: **the splits on which the estimators are evaluated are different**. Indeed, [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score") will internally call `cv.split` on the same [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold") instance, but the splits will be different each time. This is also true for any tool that performs model selection via cross-validation, e.g. [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV") and [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV"): scores are not comparable fold-to-fold across different calls to `search.fit`, since `cv.split` would have been called multiple times. Within a single call to `search.fit`, however, fold-to-fold comparison is possible since the search estimator only calls `cv.split` once.

For comparable fold-to-fold results in all scenarios, one should pass an integer to the CV splitter: `cv = KFold(shuffle=True, random_state=0)`.

Note

While fold-to-fold comparison is not advisable with `RandomState` instances, one can however expect that average scores allow to conclude whether one estimator is better than another, as long as enough folds and data are used.

### 10.3.3. General recommendations[#](https://scikit-learn.org/stable/common_pitfalls.html#general-recommendations "Link to this heading")

#### 10.3.3.1. Getting reproducible results across multiple executions[#](https://scikit-learn.org/stable/common_pitfalls.html#getting-reproducible-results-across-multiple-executions "Link to this heading")

In order to obtain reproducible (i.e. constant) results across multiple _program executions_, we need to remove all uses of `random_state=None`, which is the default. The recommended way is to declare a `rng` variable at the top of the program, and pass it down to any object that accepts a `random_state` parameter:

\>\>\> from sklearn.ensemble import RandomForestClassifier
\>\>\> from sklearn.datasets import make\_classification
\>\>\> from sklearn.model\_selection import train\_test\_split
\>\>\> import numpy as np

\>\>\> rng \= np.random.RandomState(0)
\>\>\> X, y \= make\_classification(random\_state\=rng)
\>\>\> rf \= RandomForestClassifier(random\_state\=rng)
\>\>\> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y,
...                                                     random\_state\=rng)
\>\>\> rf.fit(X\_train, y\_train).score(X\_test, y\_test)
0.84

We are now guaranteed that the result of this script will always be 0.84, no matter how many times we run it. Changing the global `rng` variable to a different value should affect the results, as expected.

It is also possible to declare the `rng` variable as an integer. This may however lead to less robust cross-validation results, as we will see in the next section.

Note

We do not recommend setting the global `numpy` seed by calling `np.random.seed(0)`. See [here](https://stackoverflow.com/questions/5836335/consistently-create-same-random-numpy-array/5837352#comment6712034_5837352) for a discussion.

#### 10.3.3.2. Robustness of cross-validation results[#](https://scikit-learn.org/stable/common_pitfalls.html#robustness-of-cross-validation-results "Link to this heading")

When we evaluate a randomized estimator performance by cross-validation, we want to make sure that the estimator can yield accurate predictions for new data, but we also want to make sure that the estimator is robust w.r.t. its random initialization. For example, we would like the random weights initialization of a [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier") to be consistently good across all folds: otherwise, when we train that estimator on new data, we might get unlucky and the random initialization may lead to bad performance. Similarly, we want a random forest to be robust w.r.t the set of randomly selected features that each tree will be using.

For these reasons, it is preferable to evaluate the cross-validation performance by letting the estimator use a different RNG on each fold. This is done by passing a `RandomState` instance (or `None`) to the estimator initialization.

When we pass an integer, the estimator will use the same RNG on each fold: if the estimator performs well (or bad), as evaluated by CV, it might just be because we got lucky (or unlucky) with that specific seed. Passing instances leads to more robust CV results, and makes the comparison between various algorithms fairer. It also helps limiting the temptation to treat the estimator’s RNG as a hyper-parameter that can be tuned.

Whether we pass `RandomState` instances or integers to CV splitters has no impact on robustness, as long as `split` is only called once. When `split` is called multiple times, fold-to-fold comparison isn’t possible anymore. As a result, passing integer to CV splitters is usually safer and covers most use-cases.

## Metadata

```json
{
  "title": "10. Common pitfalls and recommended practices",
  "description": "The purpose of this chapter is to illustrate some common pitfalls and anti-patterns that occur when using scikit-learn. It provides examples of what not to do, along with a corresponding correct ex...",
  "url": "https://scikit-learn.org/stable/common_pitfalls.html",
  "content": "The purpose of this chapter is to illustrate some common pitfalls and anti-patterns that occur when using scikit-learn. It provides examples of what **not** to do, along with a corresponding correct example.\n\n10.1. Inconsistent preprocessing[#](https://scikit-learn.org/stable/common_pitfalls.html#inconsistent-preprocessing \"Link to this heading\")\n-------------------------------------------------------------------------------------------------------------------------------------------\n\nscikit-learn provides a library of [Dataset transformations](https://scikit-learn.org/stable/data_transforms.html#data-transforms), which may clean (see [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)), reduce (see [Unsupervised dimensionality reduction](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#data-reduction)), expand (see [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation)) or generate (see [Feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-extraction)) feature representations. If these data transforms are used when training a model, they also must be used on subsequent datasets, whether it’s test data or data in a production system. Otherwise, the feature space will change, and the model will not be able to perform effectively.\n\nFor the following example, let’s create a synthetic dataset with a single feature:\n\n\\>\\>\\> from sklearn.datasets import make\\_regression\n\\>\\>\\> from sklearn.model\\_selection import train\\_test\\_split\n\n\\>\\>\\> random\\_state \\= 42\n\\>\\>\\> X, y \\= make\\_regression(random\\_state\\=random\\_state, n\\_features\\=1, noise\\=1)\n\\>\\>\\> X\\_train, X\\_test, y\\_train, y\\_test \\= train\\_test\\_split(\n...     X, y, test\\_size\\=0.4, random\\_state\\=random\\_state)\n\n**Wrong**\n\nThe train dataset is scaled, but not the test dataset, so model performance on the test dataset is worse than expected:\n\n\\>\\>\\> from sklearn.metrics import mean\\_squared\\_error\n\\>\\>\\> from sklearn.linear\\_model import LinearRegression\n\\>\\>\\> from sklearn.preprocessing import StandardScaler\n\n\\>\\>\\> scaler \\= StandardScaler()\n\\>\\>\\> X\\_train\\_transformed \\= scaler.fit\\_transform(X\\_train)\n\\>\\>\\> model \\= LinearRegression().fit(X\\_train\\_transformed, y\\_train)\n\\>\\>\\> mean\\_squared\\_error(y\\_test, model.predict(X\\_test))\n62.80...\n\n**Right**\n\nInstead of passing the non-transformed `X_test` to `predict`, we should transform the test data, the same way we transformed the training data:\n\n\\>\\>\\> X\\_test\\_transformed \\= scaler.transform(X\\_test)\n\\>\\>\\> mean\\_squared\\_error(y\\_test, model.predict(X\\_test\\_transformed))\n0.90...\n\nAlternatively, we recommend using a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline \"sklearn.pipeline.Pipeline\"), which makes it easier to chain transformations with estimators, and reduces the possibility of forgetting a transformation:\n\n\\>\\>\\> from sklearn.pipeline import make\\_pipeline\n\n\\>\\>\\> model \\= make\\_pipeline(StandardScaler(), LinearRegression())\n\\>\\>\\> model.fit(X\\_train, y\\_train)\nPipeline(steps=\\[('standardscaler', StandardScaler()),\n                ('linearregression', LinearRegression())\\])\n\\>\\>\\> mean\\_squared\\_error(y\\_test, model.predict(X\\_test))\n0.90...\n\nPipelines also help avoiding another common pitfall: leaking the test data into the training data.\n\n10.2. Data leakage[#](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage \"Link to this heading\")\n---------------------------------------------------------------------------------------------------------------\n\nData leakage occurs when information that would not be available at prediction time is used when building the model. This results in overly optimistic performance estimates, for example from [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation), and thus poorer performance when the model is used on actually novel data, for example during production.\n\nA common cause is not keeping the test and train data subsets separate. Test data should never be used to make choices about the model. **The general rule is to never call** `fit` **on the test data**. While this may sound obvious, this is easy to miss in some cases, for example when applying certain pre-processing steps.\n\nAlthough both train and test data subsets should receive the same preprocessing transformation (as described in the previous section), it is important that these transformations are only learnt from the training data. For example, if you have a normalization step where you divide by the average value, the average should be the average of the train subset, **not** the average of all the data. If the test subset is included in the average calculation, information from the test subset is influencing the model.\n\n### 10.2.1. How to avoid data leakage[#](https://scikit-learn.org/stable/common_pitfalls.html#how-to-avoid-data-leakage \"Link to this heading\")\n\nBelow are some tips on avoiding data leakage:\n\n*   Always split the data into train and test subsets first, particularly before any preprocessing steps.\n    \n*   Never include test data when using the `fit` and `fit_transform` methods. Using all the data, e.g., `fit(X)`, can result in overly optimistic scores.\n    \n    Conversely, the `transform` method should be used on both train and test subsets as the same preprocessing should be applied to all the data. This can be achieved by using `fit_transform` on the train subset and `transform` on the test subset.\n    \n*   The scikit-learn [pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline) is a great way to prevent data leakage as it ensures that the appropriate method is performed on the correct data subset. The pipeline is ideal for use in cross-validation and hyper-parameter tuning functions.\n    \n\nAn example of data leakage during preprocessing is detailed below.\n\n### 10.2.2. Data leakage during pre-processing[#](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage-during-pre-processing \"Link to this heading\")\n\nNote\n\nWe here choose to illustrate data leakage with a feature selection step. This risk of leakage is however relevant with almost all transformations in scikit-learn, including (but not limited to) [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler \"sklearn.preprocessing.StandardScaler\"), [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer \"sklearn.impute.SimpleImputer\"), and [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA \"sklearn.decomposition.PCA\").\n\nA number of [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection) functions are available in scikit-learn. They can help remove irrelevant, redundant and noisy features as well as improve your model build time and performance. As with any other type of preprocessing, feature selection should **only** use the training data. Including the test data in feature selection will optimistically bias your model.\n\nTo demonstrate we will create this binary classification problem with 10,000 randomly generated features:\n\n\\>\\>\\> import numpy as np\n\\>\\>\\> n\\_samples, n\\_features, n\\_classes \\= 200, 10000, 2\n\\>\\>\\> rng \\= np.random.RandomState(42)\n\\>\\>\\> X \\= rng.standard\\_normal((n\\_samples, n\\_features))\n\\>\\>\\> y \\= rng.choice(n\\_classes, n\\_samples)\n\n**Wrong**\n\nUsing all the data to perform feature selection results in an accuracy score much higher than chance, even though our targets are completely random. This randomness means that our `X` and `y` are independent and we thus expect the accuracy to be around 0.5. However, since the feature selection step ‘sees’ the test data, the model has an unfair advantage. In the incorrect example below we first use all the data for feature selection and then split the data into training and test subsets for model fitting. The result is a much higher than expected accuracy score:\n\n\\>\\>\\> from sklearn.model\\_selection import train\\_test\\_split\n\\>\\>\\> from sklearn.feature\\_selection import SelectKBest\n\\>\\>\\> from sklearn.ensemble import HistGradientBoostingClassifier\n\\>\\>\\> from sklearn.metrics import accuracy\\_score\n\n\\>\\>\\> \\# Incorrect preprocessing: the entire data is transformed\n\\>\\>\\> X\\_selected \\= SelectKBest(k\\=25).fit\\_transform(X, y)\n\n\\>\\>\\> X\\_train, X\\_test, y\\_train, y\\_test \\= train\\_test\\_split(\n...     X\\_selected, y, random\\_state\\=42)\n\\>\\>\\> gbc \\= HistGradientBoostingClassifier(random\\_state\\=1)\n\\>\\>\\> gbc.fit(X\\_train, y\\_train)\nHistGradientBoostingClassifier(random\\_state=1)\n\n\\>\\>\\> y\\_pred \\= gbc.predict(X\\_test)\n\\>\\>\\> accuracy\\_score(y\\_test, y\\_pred)\n0.76\n\n**Right**\n\nTo prevent data leakage, it is good practice to split your data into train and test subsets **first**. Feature selection can then be formed using just the train dataset. Notice that whenever we use `fit` or `fit_transform`, we only use the train dataset. The score is now what we would expect for the data, close to chance:\n\n\\>\\>\\> X\\_train, X\\_test, y\\_train, y\\_test \\= train\\_test\\_split(\n...     X, y, random\\_state\\=42)\n\\>\\>\\> select \\= SelectKBest(k\\=25)\n\\>\\>\\> X\\_train\\_selected \\= select.fit\\_transform(X\\_train, y\\_train)\n\n\\>\\>\\> gbc \\= HistGradientBoostingClassifier(random\\_state\\=1)\n\\>\\>\\> gbc.fit(X\\_train\\_selected, y\\_train)\nHistGradientBoostingClassifier(random\\_state=1)\n\n\\>\\>\\> X\\_test\\_selected \\= select.transform(X\\_test)\n\\>\\>\\> y\\_pred \\= gbc.predict(X\\_test\\_selected)\n\\>\\>\\> accuracy\\_score(y\\_test, y\\_pred)\n0.5\n\nHere again, we recommend using a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline \"sklearn.pipeline.Pipeline\") to chain together the feature selection and model estimators. The pipeline ensures that only the training data is used when performing `fit` and the test data is used only for calculating the accuracy score:\n\n\\>\\>\\> from sklearn.pipeline import make\\_pipeline\n\\>\\>\\> X\\_train, X\\_test, y\\_train, y\\_test \\= train\\_test\\_split(\n...     X, y, random\\_state\\=42)\n\\>\\>\\> pipeline \\= make\\_pipeline(SelectKBest(k\\=25),\n...                          HistGradientBoostingClassifier(random\\_state\\=1))\n\\>\\>\\> pipeline.fit(X\\_train, y\\_train)\nPipeline(steps=\\[('selectkbest', SelectKBest(k=25)),\n                ('histgradientboostingclassifier',\n                 HistGradientBoostingClassifier(random\\_state=1))\\])\n\n\\>\\>\\> y\\_pred \\= pipeline.predict(X\\_test)\n\\>\\>\\> accuracy\\_score(y\\_test, y\\_pred)\n0.5\n\nThe pipeline can also be fed into a cross-validation function such as [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score \"sklearn.model_selection.cross_val_score\"). Again, the pipeline ensures that the correct data subset and estimator method is used during fitting and predicting:\n\n\\>\\>\\> from sklearn.model\\_selection import cross\\_val\\_score\n\\>\\>\\> scores \\= cross\\_val\\_score(pipeline, X, y)\n\\>\\>\\> print(f\"Mean accuracy: {scores.mean():.2f}+/-{scores.std():.2f}\")\nMean accuracy: 0.43+/-0.05\n\n10.3. Controlling randomness[#](https://scikit-learn.org/stable/common_pitfalls.html#controlling-randomness \"Link to this heading\")\n-----------------------------------------------------------------------------------------------------------------------------------\n\nSome scikit-learn objects are inherently random. These are usually estimators (e.g. [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier \"sklearn.ensemble.RandomForestClassifier\")) and cross-validation splitters (e.g. [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold \"sklearn.model_selection.KFold\")). The randomness of these objects is controlled via their `random_state` parameter, as described in the [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state). This section expands on the glossary entry, and describes good practices and common pitfalls w.r.t. this subtle parameter.\n\nNote\n\nRecommendation summary\n\nFor an optimal robustness of cross-validation (CV) results, pass `RandomState` instances when creating estimators, or leave `random_state` to `None`. Passing integers to CV splitters is usually the safest option and is preferable; passing `RandomState` instances to splitters may sometimes be useful to achieve very specific use-cases. For both estimators and splitters, passing an integer vs passing an instance (or `None`) leads to subtle but significant differences, especially for CV procedures. These differences are important to understand when reporting results.\n\nFor reproducible results across executions, remove any use of `random_state=None`.\n\n### 10.3.1. Using `None` or `RandomState` instances, and repeated calls to `fit` and `split`[#](https://scikit-learn.org/stable/common_pitfalls.html#using-none-or-randomstate-instances-and-repeated-calls-to-fit-and-split \"Link to this heading\")\n\nThe `random_state` parameter determines whether multiple calls to [fit](https://scikit-learn.org/stable/glossary.html#term-fit) (for estimators) or to [split](https://scikit-learn.org/stable/glossary.html#term-split) (for CV splitters) will produce the same results, according to these rules:\n\n*   If an integer is passed, calling `fit` or `split` multiple times always yields the same results.\n    \n*   If `None` or a `RandomState` instance is passed: `fit` and `split` will yield different results each time they are called, and the succession of calls explores all sources of entropy. `None` is the default value for all `random_state` parameters.\n    \n\nWe here illustrate these rules for both estimators and CV splitters.\n\nNote\n\nSince passing `random_state=None` is equivalent to passing the global `RandomState` instance from `numpy` (`random_state=np.random.mtrand._rand`), we will not explicitly mention `None` here. Everything that applies to instances also applies to using `None`.\n\n#### 10.3.1.1. Estimators[#](https://scikit-learn.org/stable/common_pitfalls.html#estimators \"Link to this heading\")\n\nPassing instances means that calling `fit` multiple times will not yield the same results, even if the estimator is fitted on the same data and with the same hyper-parameters:\n\n\\>\\>\\> from sklearn.linear\\_model import SGDClassifier\n\\>\\>\\> from sklearn.datasets import make\\_classification\n\\>\\>\\> import numpy as np\n\n\\>\\>\\> rng \\= np.random.RandomState(0)\n\\>\\>\\> X, y \\= make\\_classification(n\\_features\\=5, random\\_state\\=rng)\n\\>\\>\\> sgd \\= SGDClassifier(random\\_state\\=rng)\n\n\\>\\>\\> sgd.fit(X, y).coef\\_\narray(\\[\\[ 8.85418642,  4.79084103, -3.13077794,  8.11915045, -0.56479934\\]\\])\n\n\\>\\>\\> sgd.fit(X, y).coef\\_\narray(\\[\\[ 6.70814003,  5.25291366, -7.55212743,  5.18197458,  1.37845099\\]\\])\n\nWe can see from the snippet above that repeatedly calling `sgd.fit` has produced different models, even if the data was the same. This is because the Random Number Generator (RNG) of the estimator is consumed (i.e. mutated) when `fit` is called, and this mutated RNG will be used in the subsequent calls to `fit`. In addition, the `rng` object is shared across all objects that use it, and as a consequence, these objects become somewhat inter-dependent. For example, two estimators that share the same `RandomState` instance will influence each other, as we will see later when we discuss cloning. This point is important to keep in mind when debugging.\n\nIf we had passed an integer to the `random_state` parameter of the [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier \"sklearn.linear_model.SGDClassifier\"), we would have obtained the same models, and thus the same scores each time. When we pass an integer, the same RNG is used across all calls to `fit`. What internally happens is that even though the RNG is consumed when `fit` is called, it is always reset to its original state at the beginning of `fit`.\n\n#### 10.3.1.2. CV splitters[#](https://scikit-learn.org/stable/common_pitfalls.html#cv-splitters \"Link to this heading\")\n\nRandomized CV splitters have a similar behavior when a `RandomState` instance is passed; calling `split` multiple times yields different data splits:\n\n\\>\\>\\> from sklearn.model\\_selection import KFold\n\\>\\>\\> import numpy as np\n\n\\>\\>\\> X \\= y \\= np.arange(10)\n\\>\\>\\> rng \\= np.random.RandomState(0)\n\\>\\>\\> cv \\= KFold(n\\_splits\\=2, shuffle\\=True, random\\_state\\=rng)\n\n\\>\\>\\> for train, test in cv.split(X, y):\n...     print(train, test)\n\\[0 3 5 6 7\\] \\[1 2 4 8 9\\]\n\\[1 2 4 8 9\\] \\[0 3 5 6 7\\]\n\n\\>\\>\\> for train, test in cv.split(X, y):\n...     print(train, test)\n\\[0 4 6 7 8\\] \\[1 2 3 5 9\\]\n\\[1 2 3 5 9\\] \\[0 4 6 7 8\\]\n\nWe can see that the splits are different from the second time `split` is called. This may lead to unexpected results if you compare the performance of multiple estimators by calling `split` many times, as we will see in the next section.\n\n### 10.3.2. Common pitfalls and subtleties[#](https://scikit-learn.org/stable/common_pitfalls.html#common-pitfalls-and-subtleties \"Link to this heading\")\n\nWhile the rules that govern the `random_state` parameter are seemingly simple, they do however have some subtle implications. In some cases, this can even lead to wrong conclusions.\n\n#### 10.3.2.1. Estimators[#](https://scikit-learn.org/stable/common_pitfalls.html#id2 \"Link to this heading\")\n\n**Different \\`random\\_state\\` types lead to different cross-validation procedures**\n\nDepending on the type of the `random_state` parameter, estimators will behave differently, especially in cross-validation procedures. Consider the following snippet:\n\n\\>\\>\\> from sklearn.ensemble import RandomForestClassifier\n\\>\\>\\> from sklearn.datasets import make\\_classification\n\\>\\>\\> from sklearn.model\\_selection import cross\\_val\\_score\n\\>\\>\\> import numpy as np\n\n\\>\\>\\> X, y \\= make\\_classification(random\\_state\\=0)\n\n\\>\\>\\> rf\\_123 \\= RandomForestClassifier(random\\_state\\=123)\n\\>\\>\\> cross\\_val\\_score(rf\\_123, X, y)\narray(\\[0.85, 0.95, 0.95, 0.9 , 0.9 \\])\n\n\\>\\>\\> rf\\_inst \\= RandomForestClassifier(random\\_state\\=np.random.RandomState(0))\n\\>\\>\\> cross\\_val\\_score(rf\\_inst, X, y)\narray(\\[0.9 , 0.95, 0.95, 0.9 , 0.9 \\])\n\nWe see that the cross-validated scores of `rf_123` and `rf_inst` are different, as should be expected since we didn’t pass the same `random_state` parameter. However, the difference between these scores is more subtle than it looks, and **the cross-validation procedures that were performed by** [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score \"sklearn.model_selection.cross_val_score\") **significantly differ in each case**:\n\n*   Since `rf_123` was passed an integer, every call to `fit` uses the same RNG: this means that all random characteristics of the random forest estimator will be the same for each of the 5 folds of the CV procedure. In particular, the (randomly chosen) subset of features of the estimator will be the same across all folds.\n    \n*   Since `rf_inst` was passed a `RandomState` instance, each call to `fit` starts from a different RNG. As a result, the random subset of features will be different for each folds.\n    \n\nWhile having a constant estimator RNG across folds isn’t inherently wrong, we usually want CV results that are robust w.r.t. the estimator’s randomness. As a result, passing an instance instead of an integer may be preferable, since it will allow the estimator RNG to vary for each fold.\n\nNote\n\nHere, [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score \"sklearn.model_selection.cross_val_score\") will use a non-randomized CV splitter (as is the default), so both estimators will be evaluated on the same splits. This section is not about variability in the splits. Also, whether we pass an integer or an instance to [`make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification \"sklearn.datasets.make_classification\") isn’t relevant for our illustration purpose: what matters is what we pass to the [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier \"sklearn.ensemble.RandomForestClassifier\") estimator.\n\nAnother subtle side effect of passing `RandomState` instances is how [`clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone \"sklearn.base.clone\") will work:\n\n\\>\\>\\> from sklearn import clone\n\\>\\>\\> from sklearn.ensemble import RandomForestClassifier\n\\>\\>\\> import numpy as np\n\n\\>\\>\\> rng \\= np.random.RandomState(0)\n\\>\\>\\> a \\= RandomForestClassifier(random\\_state\\=rng)\n\\>\\>\\> b \\= clone(a)\n\nSince a `RandomState` instance was passed to `a`, `a` and `b` are not clones in the strict sense, but rather clones in the statistical sense: `a` and `b` will still be different models, even when calling `fit(X, y)` on the same data. Moreover, `a` and `b` will influence each-other since they share the same internal RNG: calling `a.fit` will consume `b`’s RNG, and calling `b.fit` will consume `a`’s RNG, since they are the same. This bit is true for any estimators that share a `random_state` parameter; it is not specific to clones.\n\nIf an integer were passed, `a` and `b` would be exact clones and they would not influence each other.\n\n#### 10.3.2.2. CV splitters[#](https://scikit-learn.org/stable/common_pitfalls.html#id3 \"Link to this heading\")\n\nWhen passed a `RandomState` instance, CV splitters yield different splits each time `split` is called. When comparing different estimators, this can lead to overestimating the variance of the difference in performance between the estimators:\n\n\\>\\>\\> from sklearn.naive\\_bayes import GaussianNB\n\\>\\>\\> from sklearn.discriminant\\_analysis import LinearDiscriminantAnalysis\n\\>\\>\\> from sklearn.datasets import make\\_classification\n\\>\\>\\> from sklearn.model\\_selection import KFold\n\\>\\>\\> from sklearn.model\\_selection import cross\\_val\\_score\n\\>\\>\\> import numpy as np\n\n\\>\\>\\> rng \\= np.random.RandomState(0)\n\\>\\>\\> X, y \\= make\\_classification(random\\_state\\=rng)\n\\>\\>\\> cv \\= KFold(shuffle\\=True, random\\_state\\=rng)\n\\>\\>\\> lda \\= LinearDiscriminantAnalysis()\n\\>\\>\\> nb \\= GaussianNB()\n\n\\>\\>\\> for est in (lda, nb):\n...     print(cross\\_val\\_score(est, X, y, cv\\=cv))\n\\[0.8  0.75 0.75 0.7  0.85\\]\n\\[0.85 0.95 0.95 0.85 0.95\\]\n\nDirectly comparing the performance of the [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis \"sklearn.discriminant_analysis.LinearDiscriminantAnalysis\") estimator vs the [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB \"sklearn.naive_bayes.GaussianNB\") estimator **on each fold** would be a mistake: **the splits on which the estimators are evaluated are different**. Indeed, [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score \"sklearn.model_selection.cross_val_score\") will internally call `cv.split` on the same [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold \"sklearn.model_selection.KFold\") instance, but the splits will be different each time. This is also true for any tool that performs model selection via cross-validation, e.g. [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV \"sklearn.model_selection.GridSearchCV\") and [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV \"sklearn.model_selection.RandomizedSearchCV\"): scores are not comparable fold-to-fold across different calls to `search.fit`, since `cv.split` would have been called multiple times. Within a single call to `search.fit`, however, fold-to-fold comparison is possible since the search estimator only calls `cv.split` once.\n\nFor comparable fold-to-fold results in all scenarios, one should pass an integer to the CV splitter: `cv = KFold(shuffle=True, random_state=0)`.\n\nNote\n\nWhile fold-to-fold comparison is not advisable with `RandomState` instances, one can however expect that average scores allow to conclude whether one estimator is better than another, as long as enough folds and data are used.\n\n### 10.3.3. General recommendations[#](https://scikit-learn.org/stable/common_pitfalls.html#general-recommendations \"Link to this heading\")\n\n#### 10.3.3.1. Getting reproducible results across multiple executions[#](https://scikit-learn.org/stable/common_pitfalls.html#getting-reproducible-results-across-multiple-executions \"Link to this heading\")\n\nIn order to obtain reproducible (i.e. constant) results across multiple _program executions_, we need to remove all uses of `random_state=None`, which is the default. The recommended way is to declare a `rng` variable at the top of the program, and pass it down to any object that accepts a `random_state` parameter:\n\n\\>\\>\\> from sklearn.ensemble import RandomForestClassifier\n\\>\\>\\> from sklearn.datasets import make\\_classification\n\\>\\>\\> from sklearn.model\\_selection import train\\_test\\_split\n\\>\\>\\> import numpy as np\n\n\\>\\>\\> rng \\= np.random.RandomState(0)\n\\>\\>\\> X, y \\= make\\_classification(random\\_state\\=rng)\n\\>\\>\\> rf \\= RandomForestClassifier(random\\_state\\=rng)\n\\>\\>\\> X\\_train, X\\_test, y\\_train, y\\_test \\= train\\_test\\_split(X, y,\n...                                                     random\\_state\\=rng)\n\\>\\>\\> rf.fit(X\\_train, y\\_train).score(X\\_test, y\\_test)\n0.84\n\nWe are now guaranteed that the result of this script will always be 0.84, no matter how many times we run it. Changing the global `rng` variable to a different value should affect the results, as expected.\n\nIt is also possible to declare the `rng` variable as an integer. This may however lead to less robust cross-validation results, as we will see in the next section.\n\nNote\n\nWe do not recommend setting the global `numpy` seed by calling `np.random.seed(0)`. See [here](https://stackoverflow.com/questions/5836335/consistently-create-same-random-numpy-array/5837352#comment6712034_5837352) for a discussion.\n\n#### 10.3.3.2. Robustness of cross-validation results[#](https://scikit-learn.org/stable/common_pitfalls.html#robustness-of-cross-validation-results \"Link to this heading\")\n\nWhen we evaluate a randomized estimator performance by cross-validation, we want to make sure that the estimator can yield accurate predictions for new data, but we also want to make sure that the estimator is robust w.r.t. its random initialization. For example, we would like the random weights initialization of a [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier \"sklearn.linear_model.SGDClassifier\") to be consistently good across all folds: otherwise, when we train that estimator on new data, we might get unlucky and the random initialization may lead to bad performance. Similarly, we want a random forest to be robust w.r.t the set of randomly selected features that each tree will be using.\n\nFor these reasons, it is preferable to evaluate the cross-validation performance by letting the estimator use a different RNG on each fold. This is done by passing a `RandomState` instance (or `None`) to the estimator initialization.\n\nWhen we pass an integer, the estimator will use the same RNG on each fold: if the estimator performs well (or bad), as evaluated by CV, it might just be because we got lucky (or unlucky) with that specific seed. Passing instances leads to more robust CV results, and makes the comparison between various algorithms fairer. It also helps limiting the temptation to treat the estimator’s RNG as a hyper-parameter that can be tuned.\n\nWhether we pass `RandomState` instances or integers to CV splitters has no impact on robustness, as long as `split` is only called once. When `split` is called multiple times, fold-to-fold comparison isn’t possible anymore. As a result, passing integer to CV splitters is usually safer and covers most use-cases.",
  "usage": {
    "tokens": 7060
  }
}
```
