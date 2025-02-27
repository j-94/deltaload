---
title: Papers with Code - Evaluating Large Language Models in Semantic Parsing for Conversational Question Answering over Knowledge Graphs
description: Implemented in one code library.
url: https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic
timestamp: 2025-01-20T15:54:51.237Z
domain: paperswithcode.com
path: paper_evaluating-large-language-models-in-semantic
---

# Papers with Code - Evaluating Large Language Models in Semantic Parsing for Conversational Question Answering over Knowledge Graphs


Implemented in one code library.


## Content

Evaluating Large Language Models in Semantic Parsing for Conversational Question Answering over Knowledge Graphs | Papers With Code
===============  

[](https://paperswithcode.com/)

[](https://twitter.com/paperswithcode)

*     
    
*   [Browse State-of-the-Art](https://paperswithcode.com/sota)
*   [Datasets](https://paperswithcode.com/datasets)
*   [Methods](https://paperswithcode.com/methods)
*   More
    
    [Newsletter](https://paperswithcode.com/newsletter) [RC2022](https://paperswithcode.com/rc2022)
    
    [About](https://paperswithcode.com/about) [Trends](https://paperswithcode.com/trends) [Portals](https://portal.paperswithcode.com/) [Libraries](https://paperswithcode.com/libraries)
    

*   [](https://twitter.com/paperswithcode)
*   [Sign In](https://paperswithcode.com/accounts/login?next=/paper/evaluating-large-language-models-in-semantic)

### Subscribe to the PwC Newsletter

×

Stay informed on the latest trending ML papers with code, research developments, libraries, methods, and datasets.  
  
[Read previous issues](https://paperswithcode.com/newsletter)

 

Subscribe

##### Join the community

×

You need to [log in](https://paperswithcode.com/accounts/login?next=/paper/evaluating-large-language-models-in-semantic) to edit.  
You can [create a new account](https://paperswithcode.com/accounts/register?next=/paper/evaluating-large-language-models-in-semantic) if you don't have one.  
  

##### Edit Social Preview

×

  

Description  

 Default

 Custom

Image  

 Default

 Custom

 None

![Image 17](https://production-media.paperswithcode.com/thumbnails/paper/2401.01711.jpg)

File is too large

Upload an image to customize your repository’s social media preview.  
Images should be at least 640×320px (1280×640px for best display).

Close Save

##### Add a new code entry for this paper

×

GitHub, GitLab or BitBucket URL:\*

 Official code from paper authors

Submit

##### Remove a code repository from this paper

×

[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)

3

  \-

##### Mark the official implementation from paper authors

×

 

[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)

3

 

* * *

There is no official implementation

* * *

Multiple official implementations

Submit

##### Add a new evaluation result row

×

Task:\*

Not in the list? [Add a task.](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#addTask)

Dataset:\*

Model name:\*

Metric name:\*

 Higher is better (for the metric)

Metric value:\*

 Uses extra training data

Data evaluated on

Submit

##### Add a new evaluation result row

×

TASK

DATASET

MODEL

METRIC NAME

METRIC VALUE

GLOBAL RANK

REMOVE

##### Add a task

×

Attached tasks:

*   [CONVERSATIONAL QUESTION ANSWERING](https://paperswithcode.com/task/conversational-question-answering)

*   [INFORMATION RETRIEVAL](https://paperswithcode.com/task/information-retrieval)

*   [KNOWLEDGE GRAPHS](https://paperswithcode.com/task/knowledge-graphs)

*   [QUESTION ANSWERING](https://paperswithcode.com/task/question-answering)

*   [RETRIEVAL](https://paperswithcode.com/task/retrieval)

*   [SEMANTIC PARSING](https://paperswithcode.com/task/semantic-parsing)

Add:

Not in the list?  
[Create a new task](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#).

New task name:

Top-level area:

Parent task (if any):

Description:

Submit

##### Remove a task

×

*    [![Image 18](https://production-media.paperswithcode.com/tasks/default.gif) Conversational Question Answering](https://paperswithcode.com/task/conversational-question-answering)   \-

*    [![Image 19](https://production-media.paperswithcode.com/thumbnails/task/task-0000001451-80b2d378.jpg) Information Retrieval](https://paperswithcode.com/task/information-retrieval)   \-

*    [![Image 20](https://production-media.paperswithcode.com/tasks/default.gif) Knowledge Graphs](https://paperswithcode.com/task/knowledge-graphs)   \-

*    [![Image 21](https://production-media.paperswithcode.com/thumbnails/task/56ae901a-265f-415f-b175-ce54133d648b.jpg) Question Answering](https://paperswithcode.com/task/question-answering)   \-

*    [![Image 22](https://production-media.paperswithcode.com/thumbnails/task/8576b666-5d7a-4b88-a1e2-5dcc3ea02f16.jpg) Retrieval](https://paperswithcode.com/task/retrieval)   \-

*    [![Image 23](https://production-media.paperswithcode.com/tasks/default.gif) Semantic Parsing](https://paperswithcode.com/task/semantic-parsing)   \-

##### Add a method

×

Add:

Not in the list?  
[Create a new method](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#).

**New method name** (e.g. ReLU):

**New method full name** (e.g. Rectified Linear Unit):

**Paper where method was first introduced**:

**Method category** (e.g. Activation Functions): _If no match, add something for now then you can add a new category afterwards._

**Markdown description** (optional; $\\LaTeX$ enabled): _You can edit this later, so feel free to start with something succinct._

Submit

##### Remove a method

×

##### Edit Datasets

×

Add or remove datasets **introduced** in this paper:

Add or remove other datasets **used** in this paper:

Paper introduces a new dataset?

[Add a new dataset here](https://paperswithcode.com/contribute/dataset/new)

Save

Evaluating Large Language Models in Semantic Parsing for Conversational Question Answering over Knowledge Graphs
================================================================================================================

3 Jan 2024  ·  [Phillip Schneider](https://paperswithcode.com/author/phillip-schneider), [Manuel Klettner](https://paperswithcode.com/author/manuel-klettner), [Kristiina Jokinen](https://paperswithcode.com/author/kristiina-jokinen), [Elena Simperl](https://paperswithcode.com/author/elena-simperl), [Florian Matthes](https://paperswithcode.com/author/florian-matthes) · Edit social preview

Conversational question answering systems often rely on semantic parsing to enable interactive information retrieval, which involves the generation of structured database queries from a natural language input. For information-seeking conversations about facts stored within a knowledge graph, dialogue utterances are transformed into graph queries in a process that is called knowledge-based conversational question answering. This paper evaluates the performance of large language models that have not been explicitly pre-trained on this task. Through a series of experiments on an extensive benchmark dataset, we compare models of varying sizes with different prompting techniques and identify common issue types in the generated output. Our results demonstrate that large language models are capable of generating graph queries from dialogues, with significant improvements achievable through few-shot prompting and fine-tuning techniques, especially for smaller models that exhibit lower zero-shot performance.

[PDF](https://arxiv.org/pdf/2401.01711v1.pdf) [Abstract](https://arxiv.org/abs/2401.01711v1)

Code

Edit

[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Mark official](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)






------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* * *

[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)

3

[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)

3

Tasks

Edit

[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)






---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* * *

 [![Image 24](https://production-media.paperswithcode.com/tasks/default.gif) Conversational Question Answering](https://paperswithcode.com/task/conversational-question-answering)[![Image 25](https://production-media.paperswithcode.com/thumbnails/task/task-0000001451-80b2d378.jpg) Information Retrieval](https://paperswithcode.com/task/information-retrieval)[![Image 26](https://production-media.paperswithcode.com/tasks/default.gif) Knowledge Graphs](https://paperswithcode.com/task/knowledge-graphs)[![Image 27](https://production-media.paperswithcode.com/thumbnails/task/56ae901a-265f-415f-b175-ce54133d648b.jpg) Question Answering](https://paperswithcode.com/task/question-answering)[![Image 28](https://production-media.paperswithcode.com/thumbnails/task/8576b666-5d7a-4b88-a1e2-5dcc3ea02f16.jpg) Retrieval](https://paperswithcode.com/task/retrieval)[![Image 29](https://production-media.paperswithcode.com/tasks/default.gif) Semantic Parsing](https://paperswithcode.com/task/semantic-parsing)

Datasets

Edit




------------------

* * *

 [![Image 30](https://production-media.paperswithcode.com/thumbnails/dataset-small/dataset-0000004447-46d84dbb.jpg) CSQA](https://paperswithcode.com/dataset/csqa)

Results from the Paper

Edit

[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)






--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* * *

  Submit [results from this paper](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) to get state-of-the-art GitHub badges and help the community compare results to other papers.

Methods

Edit

[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)






-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* * *

No methods listed for this paper. Add [relevant methods here](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)

Contact us on: [hello@paperswithcode.com](mailto:hello@paperswithcode.com) . Papers With Code is a free resource with all data licensed under [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).

[Terms](https://paperswithcode.com/site/terms) [Data policy](https://paperswithcode.com/site/data-policy) [Cookies policy](https://paperswithcode.com/site/cookies-policy) [from ![Image 31](blob:https://paperswithcode.com/68b0d87f79f4e47d118af8c5650d58e0)](https://paperswithcode.com/about#team)

## Metadata

```json
{
  "title": "Papers with Code - Evaluating Large Language Models in Semantic Parsing for Conversational Question Answering over Knowledge Graphs",
  "description": "Implemented in one code library.",
  "url": "https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic",
  "content": "Evaluating Large Language Models in Semantic Parsing for Conversational Question Answering over Knowledge Graphs | Papers With Code\n===============  \n\n[](https://paperswithcode.com/)\n\n[](https://twitter.com/paperswithcode)\n\n*     \n    \n*   [Browse State-of-the-Art](https://paperswithcode.com/sota)\n*   [Datasets](https://paperswithcode.com/datasets)\n*   [Methods](https://paperswithcode.com/methods)\n*   More\n    \n    [Newsletter](https://paperswithcode.com/newsletter) [RC2022](https://paperswithcode.com/rc2022)\n    \n    [About](https://paperswithcode.com/about) [Trends](https://paperswithcode.com/trends) [Portals](https://portal.paperswithcode.com/) [Libraries](https://paperswithcode.com/libraries)\n    \n\n*   [](https://twitter.com/paperswithcode)\n*   [Sign In](https://paperswithcode.com/accounts/login?next=/paper/evaluating-large-language-models-in-semantic)\n\n### Subscribe to the PwC Newsletter\n\n×\n\nStay informed on the latest trending ML papers with code, research developments, libraries, methods, and datasets.  \n  \n[Read previous issues](https://paperswithcode.com/newsletter)\n\n \n\nSubscribe\n\n##### Join the community\n\n×\n\nYou need to [log in](https://paperswithcode.com/accounts/login?next=/paper/evaluating-large-language-models-in-semantic) to edit.  \nYou can [create a new account](https://paperswithcode.com/accounts/register?next=/paper/evaluating-large-language-models-in-semantic) if you don't have one.  \n  \n\n##### Edit Social Preview\n\n×\n\n  \n\nDescription  \n\n Default\n\n Custom\n\nImage  \n\n Default\n\n Custom\n\n None\n\n![Image 17](https://production-media.paperswithcode.com/thumbnails/paper/2401.01711.jpg)\n\nFile is too large\n\nUpload an image to customize your repository’s social media preview.  \nImages should be at least 640×320px (1280×640px for best display).\n\nClose Save\n\n##### Add a new code entry for this paper\n\n×\n\nGitHub, GitLab or BitBucket URL:\\*\n\n Official code from paper authors\n\nSubmit\n\n##### Remove a code repository from this paper\n\n×\n\n[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)\n\n3\n\n  \\-\n\n##### Mark the official implementation from paper authors\n\n×\n\n \n\n[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)\n\n3\n\n \n\n* * *\n\nThere is no official implementation\n\n* * *\n\nMultiple official implementations\n\nSubmit\n\n##### Add a new evaluation result row\n\n×\n\nTask:\\*\n\nNot in the list? [Add a task.](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#addTask)\n\nDataset:\\*\n\nModel name:\\*\n\nMetric name:\\*\n\n Higher is better (for the metric)\n\nMetric value:\\*\n\n Uses extra training data\n\nData evaluated on\n\nSubmit\n\n##### Add a new evaluation result row\n\n×\n\nTASK\n\nDATASET\n\nMODEL\n\nMETRIC NAME\n\nMETRIC VALUE\n\nGLOBAL RANK\n\nREMOVE\n\n##### Add a task\n\n×\n\nAttached tasks:\n\n*   [CONVERSATIONAL QUESTION ANSWERING](https://paperswithcode.com/task/conversational-question-answering)\n\n*   [INFORMATION RETRIEVAL](https://paperswithcode.com/task/information-retrieval)\n\n*   [KNOWLEDGE GRAPHS](https://paperswithcode.com/task/knowledge-graphs)\n\n*   [QUESTION ANSWERING](https://paperswithcode.com/task/question-answering)\n\n*   [RETRIEVAL](https://paperswithcode.com/task/retrieval)\n\n*   [SEMANTIC PARSING](https://paperswithcode.com/task/semantic-parsing)\n\nAdd:\n\nNot in the list?  \n[Create a new task](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#).\n\nNew task name:\n\nTop-level area:\n\nParent task (if any):\n\nDescription:\n\nSubmit\n\n##### Remove a task\n\n×\n\n*    [![Image 18](https://production-media.paperswithcode.com/tasks/default.gif) Conversational Question Answering](https://paperswithcode.com/task/conversational-question-answering)   \\-\n\n*    [![Image 19](https://production-media.paperswithcode.com/thumbnails/task/task-0000001451-80b2d378.jpg) Information Retrieval](https://paperswithcode.com/task/information-retrieval)   \\-\n\n*    [![Image 20](https://production-media.paperswithcode.com/tasks/default.gif) Knowledge Graphs](https://paperswithcode.com/task/knowledge-graphs)   \\-\n\n*    [![Image 21](https://production-media.paperswithcode.com/thumbnails/task/56ae901a-265f-415f-b175-ce54133d648b.jpg) Question Answering](https://paperswithcode.com/task/question-answering)   \\-\n\n*    [![Image 22](https://production-media.paperswithcode.com/thumbnails/task/8576b666-5d7a-4b88-a1e2-5dcc3ea02f16.jpg) Retrieval](https://paperswithcode.com/task/retrieval)   \\-\n\n*    [![Image 23](https://production-media.paperswithcode.com/tasks/default.gif) Semantic Parsing](https://paperswithcode.com/task/semantic-parsing)   \\-\n\n##### Add a method\n\n×\n\nAdd:\n\nNot in the list?  \n[Create a new method](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#).\n\n**New method name** (e.g. ReLU):\n\n**New method full name** (e.g. Rectified Linear Unit):\n\n**Paper where method was first introduced**:\n\n**Method category** (e.g. Activation Functions): _If no match, add something for now then you can add a new category afterwards._\n\n**Markdown description** (optional; $\\\\LaTeX$ enabled): _You can edit this later, so feel free to start with something succinct._\n\nSubmit\n\n##### Remove a method\n\n×\n\n##### Edit Datasets\n\n×\n\nAdd or remove datasets **introduced** in this paper:\n\nAdd or remove other datasets **used** in this paper:\n\nPaper introduces a new dataset?\n\n[Add a new dataset here](https://paperswithcode.com/contribute/dataset/new)\n\nSave\n\nEvaluating Large Language Models in Semantic Parsing for Conversational Question Answering over Knowledge Graphs\n================================================================================================================\n\n3 Jan 2024  ·  [Phillip Schneider](https://paperswithcode.com/author/phillip-schneider), [Manuel Klettner](https://paperswithcode.com/author/manuel-klettner), [Kristiina Jokinen](https://paperswithcode.com/author/kristiina-jokinen), [Elena Simperl](https://paperswithcode.com/author/elena-simperl), [Florian Matthes](https://paperswithcode.com/author/florian-matthes) · Edit social preview\n\nConversational question answering systems often rely on semantic parsing to enable interactive information retrieval, which involves the generation of structured database queries from a natural language input. For information-seeking conversations about facts stored within a knowledge graph, dialogue utterances are transformed into graph queries in a process that is called knowledge-based conversational question answering. This paper evaluates the performance of large language models that have not been explicitly pre-trained on this task. Through a series of experiments on an extensive benchmark dataset, we compare models of varying sizes with different prompting techniques and identify common issue types in the generated output. Our results demonstrate that large language models are capable of generating graph queries from dialogues, with significant improvements achievable through few-shot prompting and fine-tuning techniques, especially for smaller models that exhibit lower zero-shot performance.\n\n[PDF](https://arxiv.org/pdf/2401.01711v1.pdf) [Abstract](https://arxiv.org/abs/2401.01711v1)\n\nCode\n\nEdit\n\n[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Mark official](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n* * *\n\n[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)\n\n3\n\n[sebischair/llm-sp-cqa official](https://github.com/sebischair/llm-sp-cqa)\n\n3\n\nTasks\n\nEdit\n\n[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)\n\n\n\n\n\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n* * *\n\n [![Image 24](https://production-media.paperswithcode.com/tasks/default.gif) Conversational Question Answering](https://paperswithcode.com/task/conversational-question-answering)[![Image 25](https://production-media.paperswithcode.com/thumbnails/task/task-0000001451-80b2d378.jpg) Information Retrieval](https://paperswithcode.com/task/information-retrieval)[![Image 26](https://production-media.paperswithcode.com/tasks/default.gif) Knowledge Graphs](https://paperswithcode.com/task/knowledge-graphs)[![Image 27](https://production-media.paperswithcode.com/thumbnails/task/56ae901a-265f-415f-b175-ce54133d648b.jpg) Question Answering](https://paperswithcode.com/task/question-answering)[![Image 28](https://production-media.paperswithcode.com/thumbnails/task/8576b666-5d7a-4b88-a1e2-5dcc3ea02f16.jpg) Retrieval](https://paperswithcode.com/task/retrieval)[![Image 29](https://production-media.paperswithcode.com/tasks/default.gif) Semantic Parsing](https://paperswithcode.com/task/semantic-parsing)\n\nDatasets\n\nEdit\n\n\n\n\n------------------\n\n* * *\n\n [![Image 30](https://production-media.paperswithcode.com/thumbnails/dataset-small/dataset-0000004447-46d84dbb.jpg) CSQA](https://paperswithcode.com/dataset/csqa)\n\nResults from the Paper\n\nEdit\n\n[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)\n\n\n\n\n\n\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n* * *\n\n  Submit [results from this paper](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) to get state-of-the-art GitHub badges and help the community compare results to other papers.\n\nMethods\n\nEdit\n\n[Add](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal) [Remove](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)\n\n\n\n\n\n\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n* * *\n\nNo methods listed for this paper. Add [relevant methods here](https://paperswithcode.com/paper/evaluating-large-language-models-in-semantic#loginModal)\n\nContact us on: [hello@paperswithcode.com](mailto:hello@paperswithcode.com) . Papers With Code is a free resource with all data licensed under [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).\n\n[Terms](https://paperswithcode.com/site/terms) [Data policy](https://paperswithcode.com/site/data-policy) [Cookies policy](https://paperswithcode.com/site/cookies-policy) [from ![Image 31](blob:https://paperswithcode.com/68b0d87f79f4e47d118af8c5650d58e0)](https://paperswithcode.com/about#team)",
  "usage": {
    "tokens": 2620
  }
}
```
