---
title: Using the library - prompttools 0.0.45 documentation
description: 
url: https://prompttools.readthedocs.io/en/latest/usage.html
timestamp: 2025-01-20T15:44:40.388Z
domain: prompttools.readthedocs.io
path: en_latest_usage.html
---

# Using the library - prompttools 0.0.45 documentation



## Content

[Edit this page](https://github.com/hegelai/prompttools/edit/main/docs/source/usage.rst "Edit this page")

Toggle table of contents sidebar

There are primarily two ways you can use `prompttools` in your LLM workflow:

1.  Run experiments in [notebooks](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/).
    
2.  Write [unit tests](https://github.com/hegelai/prompttools/tree/main/examples/prompttests/test_openai_chat.py) and integrate them into your CI/CD workflow [via Github Actions](https://github.com/hegelai/prompttools/tree/main/.github/workflows/post-commit.yaml).
    

Notebooks[#](https://prompttools.readthedocs.io/en/latest/usage.html#notebooks "Permalink to this heading")
-----------------------------------------------------------------------------------------------------------

There are a few different ways to run an experiment in a notebook.

The simplest way is to define an experimentation harness and an evaluation function:

from prompttools.harness import PromptTemplateExperimentationHarness

def eval\_fn(prompt: str, results: Dict, metadata: Dict) \-\> float:
    \# Your logic here, or use a built-in one such as \`prompttools.utils.similarity\`.
    pass

prompt\_templates \= \[
    "Answer the following question: {{input}}",
    "Respond the following query: {{input}}"
\]

user\_inputs \= \[
    {"input": "Who was the first president?"},
    {"input": "Who was the first president of India?"}
\]

harness \= PromptTemplateExperimentationHarness("text-davinci-003",
                                               prompt\_templates,
                                               user\_inputs)

harness.run()
harness.evaluate("metric\_name", eval\_fn)
harness.visualize()  \# The results will be displayed as a table in your notebook

![Image 5: The visualized table in your notebook.](https://prompttools.readthedocs.io/en/latest/_images/table.png)

If you are interested to compare different models, the [ModelComparison example](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/ModelComparison.ipynb) may be of interest.

For an example of built-in evaluation function, please see this example of [semantic similarity comparison](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/SemanticSimilarity.ipynb) for details.

You can also manually enter feedback to evaluate prompts, see [HumanFeedback.ipynb](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/HumanFeedback.ipynb).

![Image 6: You can annotate feedback directly within the notebook.](https://prompttools.readthedocs.io/en/latest/_images/feedback.png)

> Note: Above we used an `ExperimentationHarness`. Under the hood, that harness uses an `Experiment` to construct and make API calls to LLMs. The harness is responsible for managing higher level abstractions, like prompt templates or system prompts. To see how experiments work at a low level, [see this example](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/BasicExperiment.ipynb).

Unit Tests[#](https://prompttools.readthedocs.io/en/latest/usage.html#unit-tests "Permalink to this heading")
-------------------------------------------------------------------------------------------------------------

Unit tests in `prompttools` are called `prompttests`. They use the `@prompttest` annotation to transform a completion function into an efficient unit test. The `prompttest` framework executes and evaluates experiments so you can test prompts over time. For example:

import prompttools.prompttest as prompttest

@prompttest.prompttest(
    metric\_name\="is\_valid\_json",
    eval\_fn\=validate\_json.evaluate,
    prompts\=\[create\_json\_prompt()\],
)
def json\_completion\_fn(prompt: str):
    response \= None
    if os.getenv("DEBUG", default\=False):
        response \= mock\_openai\_completion\_fn(\*\*{"prompt": prompt})
    else:
        response \= openai.completions.create(prompt)
    return response.choices\[0\].text

The evaluation functions should accept one of the following as it’s parameters:

*   `input_pair: Tuple[str, Dict[str, str]], results: Dict, metadata: Dict`
    
*   `prompt: str, results: Dict, metadata: Dict`
    
*   `messages: List[Dict[str,str], results: Dict, metadata: Dict`
    

You can see an example test [here](https://github.com/hegelai/prompttools/tree/main/examples/prompttests/test_openai_chat.py) and an example of that test being used as a Github Action [here](https://github.com/hegelai/prompttools/tree/main/.github/workflows/post-commit.yaml).

## Metadata

```json
{
  "title": "Using the library - prompttools 0.0.45 documentation",
  "description": "",
  "url": "https://prompttools.readthedocs.io/en/latest/usage.html",
  "content": "[Edit this page](https://github.com/hegelai/prompttools/edit/main/docs/source/usage.rst \"Edit this page\")\n\nToggle table of contents sidebar\n\nThere are primarily two ways you can use `prompttools` in your LLM workflow:\n\n1.  Run experiments in [notebooks](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/).\n    \n2.  Write [unit tests](https://github.com/hegelai/prompttools/tree/main/examples/prompttests/test_openai_chat.py) and integrate them into your CI/CD workflow [via Github Actions](https://github.com/hegelai/prompttools/tree/main/.github/workflows/post-commit.yaml).\n    \n\nNotebooks[#](https://prompttools.readthedocs.io/en/latest/usage.html#notebooks \"Permalink to this heading\")\n-----------------------------------------------------------------------------------------------------------\n\nThere are a few different ways to run an experiment in a notebook.\n\nThe simplest way is to define an experimentation harness and an evaluation function:\n\nfrom prompttools.harness import PromptTemplateExperimentationHarness\n\ndef eval\\_fn(prompt: str, results: Dict, metadata: Dict) \\-\\> float:\n    \\# Your logic here, or use a built-in one such as \\`prompttools.utils.similarity\\`.\n    pass\n\nprompt\\_templates \\= \\[\n    \"Answer the following question: {{input}}\",\n    \"Respond the following query: {{input}}\"\n\\]\n\nuser\\_inputs \\= \\[\n    {\"input\": \"Who was the first president?\"},\n    {\"input\": \"Who was the first president of India?\"}\n\\]\n\nharness \\= PromptTemplateExperimentationHarness(\"text-davinci-003\",\n                                               prompt\\_templates,\n                                               user\\_inputs)\n\nharness.run()\nharness.evaluate(\"metric\\_name\", eval\\_fn)\nharness.visualize()  \\# The results will be displayed as a table in your notebook\n\n![Image 5: The visualized table in your notebook.](https://prompttools.readthedocs.io/en/latest/_images/table.png)\n\nIf you are interested to compare different models, the [ModelComparison example](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/ModelComparison.ipynb) may be of interest.\n\nFor an example of built-in evaluation function, please see this example of [semantic similarity comparison](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/SemanticSimilarity.ipynb) for details.\n\nYou can also manually enter feedback to evaluate prompts, see [HumanFeedback.ipynb](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/HumanFeedback.ipynb).\n\n![Image 6: You can annotate feedback directly within the notebook.](https://prompttools.readthedocs.io/en/latest/_images/feedback.png)\n\n> Note: Above we used an `ExperimentationHarness`. Under the hood, that harness uses an `Experiment` to construct and make API calls to LLMs. The harness is responsible for managing higher level abstractions, like prompt templates or system prompts. To see how experiments work at a low level, [see this example](https://github.com/hegelai/prompttools/tree/main/examples/notebooks/BasicExperiment.ipynb).\n\nUnit Tests[#](https://prompttools.readthedocs.io/en/latest/usage.html#unit-tests \"Permalink to this heading\")\n-------------------------------------------------------------------------------------------------------------\n\nUnit tests in `prompttools` are called `prompttests`. They use the `@prompttest` annotation to transform a completion function into an efficient unit test. The `prompttest` framework executes and evaluates experiments so you can test prompts over time. For example:\n\nimport prompttools.prompttest as prompttest\n\n@prompttest.prompttest(\n    metric\\_name\\=\"is\\_valid\\_json\",\n    eval\\_fn\\=validate\\_json.evaluate,\n    prompts\\=\\[create\\_json\\_prompt()\\],\n)\ndef json\\_completion\\_fn(prompt: str):\n    response \\= None\n    if os.getenv(\"DEBUG\", default\\=False):\n        response \\= mock\\_openai\\_completion\\_fn(\\*\\*{\"prompt\": prompt})\n    else:\n        response \\= openai.completions.create(prompt)\n    return response.choices\\[0\\].text\n\nThe evaluation functions should accept one of the following as it’s parameters:\n\n*   `input_pair: Tuple[str, Dict[str, str]], results: Dict, metadata: Dict`\n    \n*   `prompt: str, results: Dict, metadata: Dict`\n    \n*   `messages: List[Dict[str,str], results: Dict, metadata: Dict`\n    \n\nYou can see an example test [here](https://github.com/hegelai/prompttools/tree/main/examples/prompttests/test_openai_chat.py) and an example of that test being used as a Github Action [here](https://github.com/hegelai/prompttools/tree/main/.github/workflows/post-commit.yaml).",
  "usage": {
    "tokens": 1018
  }
}
```
