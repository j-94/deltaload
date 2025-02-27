---
title: Machine Learning with Tools | MetaGPT
description: The Multi-Agent Framework
url: https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html
timestamp: 2025-01-20T16:14:28.559Z
domain: docs.deepwisdom.ai
path: main_en_guide_use_cases_agent_interpreter_machine_learning_with_tools.html
---

# Machine Learning with Tools | MetaGPT


The Multi-Agent Framework


## Content

### Task [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#task)

Use `DataInterpreter` to model and predict the [titanic](https://www.kaggle.com/competitions/titanic/data) dataset, and batch invoke tools during the data preprocessing and feature engineering stages (multiple tools of types data\_preprocess and feature\_engineering have already been created, located in the `metagpt/tools/libs` directory)).

### Code [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#code)

[examples/di/machine\_learning\_with\_tools.py](https://github.com/geekan/MetaGPT/blob/main/examples/di/machine_learning_with_tools.py)

bash

```
python examples/di/machine_learning_with_tools.py
```

```
python examples/di/machine_learning_with_tools.py
```

### Execution Results [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#execution-results)

The data preprocessing code (which includes the use of 3 tools: `FillMissingValue`, `StandardScale`, and `OneHotEncode`) is as follows:

python

```
from metagpt.tools.libs.data_preprocess import FillMissingValue, StandardScale, OneHotEncode

fill_age = FillMissingValue(features=['Age'], strategy='median')
fill_embarked = FillMissingValue(features=['Embarked'], strategy='most_frequent')

train_data = fill_age.fit_transform(train_data)
train_data = fill_embarked.fit_transform(train_data)

if 'Cabin' in train_data.columns:
    train_data.drop('Cabin', axis=1, inplace=True)

numerical_features = ['Age', 'SibSp', 'Parch', 'Fare']

scale = StandardScale(features=numerical_features)
scaled_features = scale.fit_transform(train_data)

for feature in numerical_features:
    train_data[feature] = scaled_features[feature]

categorical_features = ['Sex', 'Embarked']
one_hot = OneHotEncode(features=categorical_features)
train_data = one_hot.fit_transform(train_data)

non_informative_columns = ['PassengerId', 'Name', 'Ticket']
train_data.drop(columns=non_informative_columns, axis=1, inplace=True, errors='ignore')
train_data.head()
```

```
from metagpt.tools.libs.data_preprocess import FillMissingValue, StandardScale, OneHotEncode

fill_age = FillMissingValue(features=['Age'], strategy='median')
fill_embarked = FillMissingValue(features=['Embarked'], strategy='most_frequent')

train_data = fill_age.fit_transform(train_data)
train_data = fill_embarked.fit_transform(train_data)

if 'Cabin' in train_data.columns:
    train_data.drop('Cabin', axis=1, inplace=True)

numerical_features = ['Age', 'SibSp', 'Parch', 'Fare']

scale = StandardScale(features=numerical_features)
scaled_features = scale.fit_transform(train_data)

for feature in numerical_features:
    train_data[feature] = scaled_features[feature]

categorical_features = ['Sex', 'Embarked']
one_hot = OneHotEncode(features=categorical_features)
train_data = one_hot.fit_transform(train_data)

non_informative_columns = ['PassengerId', 'Name', 'Ticket']
train_data.drop(columns=non_informative_columns, axis=1, inplace=True, errors='ignore')
train_data.head()
```

The feature engineering code (which includes the use of 1 tool: `PolynomialExpansion`) is as follows:

python

```
from metagpt.tools.libs.feature_engineering import PolynomialExpansion
numeric_features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
poly_expansion = PolynomialExpansion(cols=numeric_features, label_col='Survived')
train_data = poly_expansion.fit_transform(train_data)
train_data.head()
```

```
from metagpt.tools.libs.feature_engineering import PolynomialExpansion
numeric_features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
poly_expansion = PolynomialExpansion(cols=numeric_features, label_col='Survived')
train_data = poly_expansion.fit_transform(train_data)
train_data.head()
```

Mechanism [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#mechanism)
------------------------------------------------------------------------------------------------------------------------------

### Tool Creation [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#tool-creation)

In the `metagpt.tools.libs` directory, we have predefined two types of tools: `data_preprocess` and `feature_engineering`. Below, taking data\_preprocess tasks as an example, we provide a complete guide for creating a simple tool, including how to define and register the tool.

*   First, create a file named `data_preprocess.py` in the `metagpt.tools.libs` directory.
*   In this file, you will define your data preprocessing tool and complete the registration of the tool using the `@register_tool` decorator. Additionally, you can specify the category of the tool by setting the `tags` parameter.

**Code Example**:

python

```
from typing import Literal

import pandas as pd
from sklearn.impute import SimpleImputer

from metagpt.tools.tool_registry import register_tool


TAGS = ["data preprocessing", "machine learning"]

@register_tool(tags=TAGS)
class FillMissingValue:
    """
    Completing missing values with simple strategies.
    """

    def __init__(
        self, features: list, strategy: Literal["mean", "median", "most_frequent", "constant"] = "mean", fill_value=None
    ):
        """
        Initialize self.

        Args:
            features (list): Columns to be processed.
            strategy (Literal["mean", "median", "most_frequent", "constant"], optional): The imputation strategy, notice 'mean' and 'median' can only
                                      be used for numeric features. Defaults to 'mean'.
            fill_value (int, optional): Fill_value is used to replace all occurrences of missing_values.
                                        Defaults to None.
        """
        self.features = features
        self.strategy = strategy
        self.fill_value = fill_value
        self.si = None

    def fit(self, df: pd.DataFrame):
        """
        Fit the FillMissingValue model.

        Args:
            df (pd.DataFrame): The input DataFrame.
        """
        if len(self.features) == 0:
            return
        self.si = SimpleImputer(strategy=self.strategy, fill_value=self.fill_value)
        self.si.fit(df[self.features])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform the input DataFrame with the fitted model.

        Args:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The transformed DataFrame.
        """
        if len(self.features) == 0:
            return df
        new_df = df.copy()
        new_df[self.features] = self.si.transform(new_df[self.features])
        return new_df

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fit and transform the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The transformed DataFrame.
        """
        self.fit(df)
        return self.transform(df)
```

```
from typing import Literal

import pandas as pd
from sklearn.impute import SimpleImputer

from metagpt.tools.tool_registry import register_tool


TAGS = ["data preprocessing", "machine learning"]

@register_tool(tags=TAGS)
class FillMissingValue:
    """
    Completing missing values with simple strategies.
    """

    def __init__(
        self, features: list, strategy: Literal["mean", "median", "most_frequent", "constant"] = "mean", fill_value=None
    ):
        """
        Initialize self.

        Args:
            features (list): Columns to be processed.
            strategy (Literal["mean", "median", "most_frequent", "constant"], optional): The imputation strategy, notice 'mean' and 'median' can only
                                      be used for numeric features. Defaults to 'mean'.
            fill_value (int, optional): Fill_value is used to replace all occurrences of missing_values.
                                        Defaults to None.
        """
        self.features = features
        self.strategy = strategy
        self.fill_value = fill_value
        self.si = None

    def fit(self, df: pd.DataFrame):
        """
        Fit the FillMissingValue model.

        Args:
            df (pd.DataFrame): The input DataFrame.
        """
        if len(self.features) == 0:
            return
        self.si = SimpleImputer(strategy=self.strategy, fill_value=self.fill_value)
        self.si.fit(df[self.features])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform the input DataFrame with the fitted model.

        Args:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The transformed DataFrame.
        """
        if len(self.features) == 0:
            return df
        new_df = df.copy()
        new_df[self.features] = self.si.transform(new_df[self.features])
        return new_df

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fit and transform the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The transformed DataFrame.
        """
        self.fit(df)
        return self.transform(df)
```

In the example above, the `FillMissingValue` class implements the functionality for filling missing values and is registered as a data\_preprocess tool using the `@register_tool` decorator.

After registering the tool, the system will automatically generate a corresponding schema file (such as FillMissingValue.yml) for each tool in `metagpt.tools.schemas` based on the comments of the tool functions, detailing the structure, methods, and parameter types of the tool class, ensuring that the LLM can accurately understand and utilize the tool.

**Schema File Example (FillMissingValue.yml)**:

yaml

```
type: class
description: Completing missing values with simple strategies.
methods:
  __init__:
    type: function
    description: 'Initialize self. '
    signature:
      '(self, features: ''list'', strategy: "Literal[''mean'', ''median'',
      ''most_frequent'', ''constant'']" = ''mean'', fill_value=None)'
    parameters:
      'Args: features (list): Columns to be processed. strategy (Literal["mean",
      "median", "most_frequent", "constant"], optional): The imputation strategy,
      notice ''mean'' and ''median'' can only be used for numeric features. Defaults
      to ''mean''. fill_value (int, optional): Fill_value is used to replace all occurrences
      of missing_values. Defaults to None.'
  fit:
    type: function
    description: 'Fit a model to be used in subsequent transform. '
    signature: "(self, df: 'pd.DataFrame')"
    parameters: 'Args: df (pd.DataFrame): The input DataFrame.'
  fit_transform:
    type: function
    description: 'Fit and transform the input DataFrame. '
    signature: "(self, df: 'pd.DataFrame') -> 'pd.DataFrame'"
    parameters:
      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:
      The transformed DataFrame.'
  transform:
    type: function
    description: 'Transform the input DataFrame with the fitted model. '
    signature: "(self, df: 'pd.DataFrame') -> 'pd.DataFrame'"
    parameters:
      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:
      The transformed DataFrame.'
```

```
type: class
description: Completing missing values with simple strategies.
methods:
  __init__:
    type: function
    description: 'Initialize self. '
    signature:
      '(self, features: ''list'', strategy: "Literal[''mean'', ''median'',
      ''most_frequent'', ''constant'']" = ''mean'', fill_value=None)'
    parameters:
      'Args: features (list): Columns to be processed. strategy (Literal["mean",
      "median", "most_frequent", "constant"], optional): The imputation strategy,
      notice ''mean'' and ''median'' can only be used for numeric features. Defaults
      to ''mean''. fill_value (int, optional): Fill_value is used to replace all occurrences
      of missing_values. Defaults to None.'
  fit:
    type: function
    description: 'Fit a model to be used in subsequent transform. '
    signature: "(self, df: 'pd.DataFrame')"
    parameters: 'Args: df (pd.DataFrame): The input DataFrame.'
  fit_transform:
    type: function
    description: 'Fit and transform the input DataFrame. '
    signature: "(self, df: 'pd.DataFrame') -> 'pd.DataFrame'"
    parameters:
      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:
      The transformed DataFrame.'
  transform:
    type: function
    description: 'Transform the input DataFrame with the fitted model. '
    signature: "(self, df: 'pd.DataFrame') -> 'pd.DataFrame'"
    parameters:
      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:
      The transformed DataFrame.'
```

### Automatic Tool Registration and Selection [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#automatic-tool-registration-and-selection)

By setting the `tools` parameter of `DataInterpreter`, you can manually specify which tools to use. If you want to use all tools, you can set `tools=["<all>"]`.

When `DataInterpreter` starts, it will automatically register all the tools in the `tools` list. At the same time, during the task planning stage, `DataInterpreter` will recommend available tools for each task based on the requirements, and select the TOP-k for LLM to use.

### Tool Combination and Invocation [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#tool-combination-and-invocation)

During task execution, once the available TOP tools are identified, `DataInterpreter` will automatically combine and call these tools as needed according to the task requirements to form a code solution for a specific task.

## Metadata

```json
{
  "title": "Machine Learning with Tools | MetaGPT",
  "description": "The Multi-Agent Framework",
  "url": "https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html",
  "content": "### Task [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#task)\n\nUse `DataInterpreter` to model and predict the [titanic](https://www.kaggle.com/competitions/titanic/data) dataset, and batch invoke tools during the data preprocessing and feature engineering stages (multiple tools of types data\\_preprocess and feature\\_engineering have already been created, located in the `metagpt/tools/libs` directory)).\n\n### Code [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#code)\n\n[examples/di/machine\\_learning\\_with\\_tools.py](https://github.com/geekan/MetaGPT/blob/main/examples/di/machine_learning_with_tools.py)\n\nbash\n\n```\npython examples/di/machine_learning_with_tools.py\n```\n\n```\npython examples/di/machine_learning_with_tools.py\n```\n\n### Execution Results [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#execution-results)\n\nThe data preprocessing code (which includes the use of 3 tools: `FillMissingValue`, `StandardScale`, and `OneHotEncode`) is as follows:\n\npython\n\n```\nfrom metagpt.tools.libs.data_preprocess import FillMissingValue, StandardScale, OneHotEncode\n\nfill_age = FillMissingValue(features=['Age'], strategy='median')\nfill_embarked = FillMissingValue(features=['Embarked'], strategy='most_frequent')\n\ntrain_data = fill_age.fit_transform(train_data)\ntrain_data = fill_embarked.fit_transform(train_data)\n\nif 'Cabin' in train_data.columns:\n    train_data.drop('Cabin', axis=1, inplace=True)\n\nnumerical_features = ['Age', 'SibSp', 'Parch', 'Fare']\n\nscale = StandardScale(features=numerical_features)\nscaled_features = scale.fit_transform(train_data)\n\nfor feature in numerical_features:\n    train_data[feature] = scaled_features[feature]\n\ncategorical_features = ['Sex', 'Embarked']\none_hot = OneHotEncode(features=categorical_features)\ntrain_data = one_hot.fit_transform(train_data)\n\nnon_informative_columns = ['PassengerId', 'Name', 'Ticket']\ntrain_data.drop(columns=non_informative_columns, axis=1, inplace=True, errors='ignore')\ntrain_data.head()\n```\n\n```\nfrom metagpt.tools.libs.data_preprocess import FillMissingValue, StandardScale, OneHotEncode\n\nfill_age = FillMissingValue(features=['Age'], strategy='median')\nfill_embarked = FillMissingValue(features=['Embarked'], strategy='most_frequent')\n\ntrain_data = fill_age.fit_transform(train_data)\ntrain_data = fill_embarked.fit_transform(train_data)\n\nif 'Cabin' in train_data.columns:\n    train_data.drop('Cabin', axis=1, inplace=True)\n\nnumerical_features = ['Age', 'SibSp', 'Parch', 'Fare']\n\nscale = StandardScale(features=numerical_features)\nscaled_features = scale.fit_transform(train_data)\n\nfor feature in numerical_features:\n    train_data[feature] = scaled_features[feature]\n\ncategorical_features = ['Sex', 'Embarked']\none_hot = OneHotEncode(features=categorical_features)\ntrain_data = one_hot.fit_transform(train_data)\n\nnon_informative_columns = ['PassengerId', 'Name', 'Ticket']\ntrain_data.drop(columns=non_informative_columns, axis=1, inplace=True, errors='ignore')\ntrain_data.head()\n```\n\nThe feature engineering code (which includes the use of 1 tool: `PolynomialExpansion`) is as follows:\n\npython\n\n```\nfrom metagpt.tools.libs.feature_engineering import PolynomialExpansion\nnumeric_features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']\npoly_expansion = PolynomialExpansion(cols=numeric_features, label_col='Survived')\ntrain_data = poly_expansion.fit_transform(train_data)\ntrain_data.head()\n```\n\n```\nfrom metagpt.tools.libs.feature_engineering import PolynomialExpansion\nnumeric_features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']\npoly_expansion = PolynomialExpansion(cols=numeric_features, label_col='Survived')\ntrain_data = poly_expansion.fit_transform(train_data)\ntrain_data.head()\n```\n\nMechanism [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#mechanism)\n------------------------------------------------------------------------------------------------------------------------------\n\n### Tool Creation [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#tool-creation)\n\nIn the `metagpt.tools.libs` directory, we have predefined two types of tools: `data_preprocess` and `feature_engineering`. Below, taking data\\_preprocess tasks as an example, we provide a complete guide for creating a simple tool, including how to define and register the tool.\n\n*   First, create a file named `data_preprocess.py` in the `metagpt.tools.libs` directory.\n*   In this file, you will define your data preprocessing tool and complete the registration of the tool using the `@register_tool` decorator. Additionally, you can specify the category of the tool by setting the `tags` parameter.\n\n**Code Example**:\n\npython\n\n```\nfrom typing import Literal\n\nimport pandas as pd\nfrom sklearn.impute import SimpleImputer\n\nfrom metagpt.tools.tool_registry import register_tool\n\n\nTAGS = [\"data preprocessing\", \"machine learning\"]\n\n@register_tool(tags=TAGS)\nclass FillMissingValue:\n    \"\"\"\n    Completing missing values with simple strategies.\n    \"\"\"\n\n    def __init__(\n        self, features: list, strategy: Literal[\"mean\", \"median\", \"most_frequent\", \"constant\"] = \"mean\", fill_value=None\n    ):\n        \"\"\"\n        Initialize self.\n\n        Args:\n            features (list): Columns to be processed.\n            strategy (Literal[\"mean\", \"median\", \"most_frequent\", \"constant\"], optional): The imputation strategy, notice 'mean' and 'median' can only\n                                      be used for numeric features. Defaults to 'mean'.\n            fill_value (int, optional): Fill_value is used to replace all occurrences of missing_values.\n                                        Defaults to None.\n        \"\"\"\n        self.features = features\n        self.strategy = strategy\n        self.fill_value = fill_value\n        self.si = None\n\n    def fit(self, df: pd.DataFrame):\n        \"\"\"\n        Fit the FillMissingValue model.\n\n        Args:\n            df (pd.DataFrame): The input DataFrame.\n        \"\"\"\n        if len(self.features) == 0:\n            return\n        self.si = SimpleImputer(strategy=self.strategy, fill_value=self.fill_value)\n        self.si.fit(df[self.features])\n\n    def transform(self, df: pd.DataFrame) -> pd.DataFrame:\n        \"\"\"\n        Transform the input DataFrame with the fitted model.\n\n        Args:\n            df (pd.DataFrame): The input DataFrame.\n\n        Returns:\n            pd.DataFrame: The transformed DataFrame.\n        \"\"\"\n        if len(self.features) == 0:\n            return df\n        new_df = df.copy()\n        new_df[self.features] = self.si.transform(new_df[self.features])\n        return new_df\n\n    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:\n        \"\"\"\n        Fit and transform the input DataFrame.\n\n        Args:\n            df (pd.DataFrame): The input DataFrame.\n\n        Returns:\n            pd.DataFrame: The transformed DataFrame.\n        \"\"\"\n        self.fit(df)\n        return self.transform(df)\n```\n\n```\nfrom typing import Literal\n\nimport pandas as pd\nfrom sklearn.impute import SimpleImputer\n\nfrom metagpt.tools.tool_registry import register_tool\n\n\nTAGS = [\"data preprocessing\", \"machine learning\"]\n\n@register_tool(tags=TAGS)\nclass FillMissingValue:\n    \"\"\"\n    Completing missing values with simple strategies.\n    \"\"\"\n\n    def __init__(\n        self, features: list, strategy: Literal[\"mean\", \"median\", \"most_frequent\", \"constant\"] = \"mean\", fill_value=None\n    ):\n        \"\"\"\n        Initialize self.\n\n        Args:\n            features (list): Columns to be processed.\n            strategy (Literal[\"mean\", \"median\", \"most_frequent\", \"constant\"], optional): The imputation strategy, notice 'mean' and 'median' can only\n                                      be used for numeric features. Defaults to 'mean'.\n            fill_value (int, optional): Fill_value is used to replace all occurrences of missing_values.\n                                        Defaults to None.\n        \"\"\"\n        self.features = features\n        self.strategy = strategy\n        self.fill_value = fill_value\n        self.si = None\n\n    def fit(self, df: pd.DataFrame):\n        \"\"\"\n        Fit the FillMissingValue model.\n\n        Args:\n            df (pd.DataFrame): The input DataFrame.\n        \"\"\"\n        if len(self.features) == 0:\n            return\n        self.si = SimpleImputer(strategy=self.strategy, fill_value=self.fill_value)\n        self.si.fit(df[self.features])\n\n    def transform(self, df: pd.DataFrame) -> pd.DataFrame:\n        \"\"\"\n        Transform the input DataFrame with the fitted model.\n\n        Args:\n            df (pd.DataFrame): The input DataFrame.\n\n        Returns:\n            pd.DataFrame: The transformed DataFrame.\n        \"\"\"\n        if len(self.features) == 0:\n            return df\n        new_df = df.copy()\n        new_df[self.features] = self.si.transform(new_df[self.features])\n        return new_df\n\n    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:\n        \"\"\"\n        Fit and transform the input DataFrame.\n\n        Args:\n            df (pd.DataFrame): The input DataFrame.\n\n        Returns:\n            pd.DataFrame: The transformed DataFrame.\n        \"\"\"\n        self.fit(df)\n        return self.transform(df)\n```\n\nIn the example above, the `FillMissingValue` class implements the functionality for filling missing values and is registered as a data\\_preprocess tool using the `@register_tool` decorator.\n\nAfter registering the tool, the system will automatically generate a corresponding schema file (such as FillMissingValue.yml) for each tool in `metagpt.tools.schemas` based on the comments of the tool functions, detailing the structure, methods, and parameter types of the tool class, ensuring that the LLM can accurately understand and utilize the tool.\n\n**Schema File Example (FillMissingValue.yml)**:\n\nyaml\n\n```\ntype: class\ndescription: Completing missing values with simple strategies.\nmethods:\n  __init__:\n    type: function\n    description: 'Initialize self. '\n    signature:\n      '(self, features: ''list'', strategy: \"Literal[''mean'', ''median'',\n      ''most_frequent'', ''constant'']\" = ''mean'', fill_value=None)'\n    parameters:\n      'Args: features (list): Columns to be processed. strategy (Literal[\"mean\",\n      \"median\", \"most_frequent\", \"constant\"], optional): The imputation strategy,\n      notice ''mean'' and ''median'' can only be used for numeric features. Defaults\n      to ''mean''. fill_value (int, optional): Fill_value is used to replace all occurrences\n      of missing_values. Defaults to None.'\n  fit:\n    type: function\n    description: 'Fit a model to be used in subsequent transform. '\n    signature: \"(self, df: 'pd.DataFrame')\"\n    parameters: 'Args: df (pd.DataFrame): The input DataFrame.'\n  fit_transform:\n    type: function\n    description: 'Fit and transform the input DataFrame. '\n    signature: \"(self, df: 'pd.DataFrame') -> 'pd.DataFrame'\"\n    parameters:\n      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:\n      The transformed DataFrame.'\n  transform:\n    type: function\n    description: 'Transform the input DataFrame with the fitted model. '\n    signature: \"(self, df: 'pd.DataFrame') -> 'pd.DataFrame'\"\n    parameters:\n      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:\n      The transformed DataFrame.'\n```\n\n```\ntype: class\ndescription: Completing missing values with simple strategies.\nmethods:\n  __init__:\n    type: function\n    description: 'Initialize self. '\n    signature:\n      '(self, features: ''list'', strategy: \"Literal[''mean'', ''median'',\n      ''most_frequent'', ''constant'']\" = ''mean'', fill_value=None)'\n    parameters:\n      'Args: features (list): Columns to be processed. strategy (Literal[\"mean\",\n      \"median\", \"most_frequent\", \"constant\"], optional): The imputation strategy,\n      notice ''mean'' and ''median'' can only be used for numeric features. Defaults\n      to ''mean''. fill_value (int, optional): Fill_value is used to replace all occurrences\n      of missing_values. Defaults to None.'\n  fit:\n    type: function\n    description: 'Fit a model to be used in subsequent transform. '\n    signature: \"(self, df: 'pd.DataFrame')\"\n    parameters: 'Args: df (pd.DataFrame): The input DataFrame.'\n  fit_transform:\n    type: function\n    description: 'Fit and transform the input DataFrame. '\n    signature: \"(self, df: 'pd.DataFrame') -> 'pd.DataFrame'\"\n    parameters:\n      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:\n      The transformed DataFrame.'\n  transform:\n    type: function\n    description: 'Transform the input DataFrame with the fitted model. '\n    signature: \"(self, df: 'pd.DataFrame') -> 'pd.DataFrame'\"\n    parameters:\n      'Args: df (pd.DataFrame): The input DataFrame. Returns: pd.DataFrame:\n      The transformed DataFrame.'\n```\n\n### Automatic Tool Registration and Selection [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#automatic-tool-registration-and-selection)\n\nBy setting the `tools` parameter of `DataInterpreter`, you can manually specify which tools to use. If you want to use all tools, you can set `tools=[\"<all>\"]`.\n\nWhen `DataInterpreter` starts, it will automatically register all the tools in the `tools` list. At the same time, during the task planning stage, `DataInterpreter` will recommend available tools for each task based on the requirements, and select the TOP-k for LLM to use.\n\n### Tool Combination and Invocation [​](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/machine_learning_with_tools.html#tool-combination-and-invocation)\n\nDuring task execution, once the available TOP tools are identified, `DataInterpreter` will automatically combine and call these tools as needed according to the task requirements to form a code solution for a specific task.",
  "usage": {
    "tokens": 3078
  }
}
```
