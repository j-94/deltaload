---
title: Adala Docs
description: 
url: https://humansignal.github.io/Adala/#installation
timestamp: 2025-01-20T16:14:50.899Z
domain: humansignal.github.io
path: Adala
---

# Adala Docs



## Content

[](https://github.com/humansignal/Adala/tree/main/docs/src/index.md "Edit this page")

Quickstart
----------

Adala is an **A**utonomous **DA**ta (**L**abeling) **A**gent framework.

Adala offers a robust framework for implementing agents specialized in data processing, with an emphasis on diverse data labeling tasks. These agents are autonomous, meaning they can independently acquire one or more skills through iterative learning. This learning process is influenced by their operating environment, observations, and reflections. Users define the environment by providing a ground truth dataset. Every agent learns and applies its skills in what we refer to as a "runtime", synonymous with LLM.

![Image 3: Diagram of components](https://humansignal.github.io/Adala/img/diagram.png)

Installation
------------

Install Adala:

```
pip install adala
```

Prerequisites
-------------

Set OPENAI\_API\_KEY ([see instructions here](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key))

🎬 Quickstart
-------------

In this example we will use Adala as a standalone library directly inside Python notebook.

Click [here](https://github.com/HumanSignal/Adala/blob/master/examples/quickstart.ipynb) to see an extended quickstart example.

```
import pandas as pd

from adala.agents import Agent
from adala.environments import StaticEnvironment
from adala.skills import ClassificationSkill
from adala.runtimes import OpenAIChatRuntime
from rich import print

# Train dataset
train_df = pd.DataFrame([
    ["It was the negative first impressions, and then it started working.", "Positive"],
    ["Not loud enough and doesn't turn on like it should.", "Negative"],
    ["I don't know what to say.", "Neutral"],
    ["Manager was rude, but the most important that mic shows very flat frequency response.", "Positive"],
    ["The phone doesn't seem to accept anything except CBR mp3s.", "Negative"],
    ["I tried it before, I bought this device for my son.", "Neutral"],
], columns=["text", "sentiment"])

# Test dataset
test_df = pd.DataFrame([
    "All three broke within two months of use.",
    "The device worked for a long time, can't say anything bad.",
    "Just a random line of text."
], columns=["text"])

agent = Agent(
    # connect to a dataset
    environment=StaticEnvironment(df=train_df),

    # define a skill
    skills=ClassificationSkill(
        name='sentiment',
        instructions="Label text as positive, negative or neutral.",
        labels={'sentiment': ["Positive", "Negative", "Neutral"]},
        input_template="Text: {text}",
        output_template="Sentiment: {sentiment}"
    ),

    # define all the different runtimes your skills may use
    runtimes = {
        # You can specify your OPENAI API KEY here via `OpenAIRuntime(..., api_key='your-api-key')`
        'openai': OpenAIChatRuntime(model='gpt-3.5-turbo'),
    },
    default_runtime='openai',

    # NOTE! If you have access to GPT-4, you can uncomment the lines bellow for better results
#     default_teacher_runtime='openai-gpt4',
#     teacher_runtimes = {
#       'openai-gpt4': OpenAIRuntime(model='gpt-4')
#     }
)

print(agent)
print(agent.skills)

agent.learn(learning_iterations=3, accuracy_threshold=0.95)

print('\n=> Run tests ...')
predictions = agent.run(test_df)
print('\n => Test results:')
print(predictions)
```

Reference
---------

*   [**Agents**](https://humansignal.github.io/Adala/agents/) - main interface for interacting with environment
*   [**Datasets**](https://humansignal.github.io/Adala/datasets.md) - data inputs for agents
*   [**Environments**](https://humansignal.github.io/Adala/environments/) - environments for agents, where it collects ground truth signal
*   [**Memories**](https://humansignal.github.io/Adala/memories/) - agent's memory for storing and retrieving data
*   [**Runtimes**](https://humansignal.github.io/Adala/runtimes/) - agent's execution runtime (e.g. LLMs providers)
*   [**Skills**](https://humansignal.github.io/Adala/skills/) - agent skills for data labeling

## Metadata

```json
{
  "title": "Adala Docs",
  "description": "",
  "url": "https://humansignal.github.io/Adala/#installation",
  "content": "[](https://github.com/humansignal/Adala/tree/main/docs/src/index.md \"Edit this page\")\n\nQuickstart\n----------\n\nAdala is an **A**utonomous **DA**ta (**L**abeling) **A**gent framework.\n\nAdala offers a robust framework for implementing agents specialized in data processing, with an emphasis on diverse data labeling tasks. These agents are autonomous, meaning they can independently acquire one or more skills through iterative learning. This learning process is influenced by their operating environment, observations, and reflections. Users define the environment by providing a ground truth dataset. Every agent learns and applies its skills in what we refer to as a \"runtime\", synonymous with LLM.\n\n![Image 3: Diagram of components](https://humansignal.github.io/Adala/img/diagram.png)\n\nInstallation\n------------\n\nInstall Adala:\n\n```\npip install adala\n```\n\nPrerequisites\n-------------\n\nSet OPENAI\\_API\\_KEY ([see instructions here](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key))\n\n🎬 Quickstart\n-------------\n\nIn this example we will use Adala as a standalone library directly inside Python notebook.\n\nClick [here](https://github.com/HumanSignal/Adala/blob/master/examples/quickstart.ipynb) to see an extended quickstart example.\n\n```\nimport pandas as pd\n\nfrom adala.agents import Agent\nfrom adala.environments import StaticEnvironment\nfrom adala.skills import ClassificationSkill\nfrom adala.runtimes import OpenAIChatRuntime\nfrom rich import print\n\n# Train dataset\ntrain_df = pd.DataFrame([\n    [\"It was the negative first impressions, and then it started working.\", \"Positive\"],\n    [\"Not loud enough and doesn't turn on like it should.\", \"Negative\"],\n    [\"I don't know what to say.\", \"Neutral\"],\n    [\"Manager was rude, but the most important that mic shows very flat frequency response.\", \"Positive\"],\n    [\"The phone doesn't seem to accept anything except CBR mp3s.\", \"Negative\"],\n    [\"I tried it before, I bought this device for my son.\", \"Neutral\"],\n], columns=[\"text\", \"sentiment\"])\n\n# Test dataset\ntest_df = pd.DataFrame([\n    \"All three broke within two months of use.\",\n    \"The device worked for a long time, can't say anything bad.\",\n    \"Just a random line of text.\"\n], columns=[\"text\"])\n\nagent = Agent(\n    # connect to a dataset\n    environment=StaticEnvironment(df=train_df),\n\n    # define a skill\n    skills=ClassificationSkill(\n        name='sentiment',\n        instructions=\"Label text as positive, negative or neutral.\",\n        labels={'sentiment': [\"Positive\", \"Negative\", \"Neutral\"]},\n        input_template=\"Text: {text}\",\n        output_template=\"Sentiment: {sentiment}\"\n    ),\n\n    # define all the different runtimes your skills may use\n    runtimes = {\n        # You can specify your OPENAI API KEY here via `OpenAIRuntime(..., api_key='your-api-key')`\n        'openai': OpenAIChatRuntime(model='gpt-3.5-turbo'),\n    },\n    default_runtime='openai',\n\n    # NOTE! If you have access to GPT-4, you can uncomment the lines bellow for better results\n#     default_teacher_runtime='openai-gpt4',\n#     teacher_runtimes = {\n#       'openai-gpt4': OpenAIRuntime(model='gpt-4')\n#     }\n)\n\nprint(agent)\nprint(agent.skills)\n\nagent.learn(learning_iterations=3, accuracy_threshold=0.95)\n\nprint('\\n=> Run tests ...')\npredictions = agent.run(test_df)\nprint('\\n => Test results:')\nprint(predictions)\n```\n\nReference\n---------\n\n*   [**Agents**](https://humansignal.github.io/Adala/agents/) - main interface for interacting with environment\n*   [**Datasets**](https://humansignal.github.io/Adala/datasets.md) - data inputs for agents\n*   [**Environments**](https://humansignal.github.io/Adala/environments/) - environments for agents, where it collects ground truth signal\n*   [**Memories**](https://humansignal.github.io/Adala/memories/) - agent's memory for storing and retrieving data\n*   [**Runtimes**](https://humansignal.github.io/Adala/runtimes/) - agent's execution runtime (e.g. LLMs providers)\n*   [**Skills**](https://humansignal.github.io/Adala/skills/) - agent skills for data labeling",
  "usage": {
    "tokens": 968
  }
}
```
