---
title: 🦍 Gorilla: Large Language Model Connected with Massive APIs
description: 
url: https://gorilla.cs.berkeley.edu/
timestamp: 2025-01-20T15:46:52.001Z
domain: gorilla.cs.berkeley.edu
path: root
---

# 🦍 Gorilla: Large Language Model Connected with Massive APIs



## Content

Gorilla
===============
         

[Home](https://gorilla.cs.berkeley.edu/index.html) [Blogs](https://gorilla.cs.berkeley.edu/blog.html) [Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) [API Zoo Index](https://gorilla.cs.berkeley.edu/apizoo/)

🦍 Gorilla: Large Language Model Connected with Massive APIs
============================================================

#### [Shishir G. Patil\*](https://people.eecs.berkeley.edu/~shishirpatil/), [Tianjun Zhang\*](https://tianjunz.github.io/), [Xin Wang](https://xinw.ai/), [Joseph E. Gonzalez](https://people.eecs.berkeley.edu/~jegonzal/)

##### UC Berkeley

###### sgp@berkeley.edu, tianjunz@berkeley.edu

[Blogs](https://gorilla.cs.berkeley.edu/blog.html) [GitHub](https://github.com/ShishirPatil/gorilla) [HuggingFace](https://huggingface.co/gorilla-llm) [Discord](https://discord.gg/grXXvj9Whz)

[Gorilla Paper](https://arxiv.org/abs/2305.15334) [RAFT Paper](https://arxiv.org/abs/2403.10131) [GoEX Paper](https://arxiv.org/abs/2404.06921)

### Systems and Algorithms for Integrating LLMs with Applications, Tools, and Services

### Gorilla Used at

Microsoft Nvidia

Gorilla OpenFunctions

Teach LLM tool use

![Image 6: Image 1](https://gorilla.cs.berkeley.edu/assets/img/blog_post_4_gorilla_open_function_calling.png)

🎁In OpenFunctions-v2, we natively train the model to support parallel functions (generate multiple functions at a time) and multiple functions (select one or more functions). Java/REST/Python APIs are also supported for the first time with extended data types📷

*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/7_open_functions_v2.html)
*   How well to other function-calling models perform: [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
*   Play with the model online: [Gorilla OpenFunctions-v2 Web Demo](https://gorilla.cs.berkeley.edu/leaderboard.html#api-explorer)
*   Check out the project: [GitHub Code](https://github.com/ShishirPatil/gorilla/tree/main/openfunctions)
*   Model (6.91B) on HuggingFace 🤗: [gorilla-llm/gorilla-openfunctions-v2](https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2)

BFCL

Benchmarking LLMs on function calling capabilities

![Image 7: Image 1](https://gorilla.cs.berkeley.edu/assets/img/leaderboard-summary.jpg)

🏆 Berkeley Function-Calling Leaderboard (BFCL) 📊 aims to provide a thorough study of the function-calling capability of different LLMs. It consists of 2k 📝 question-function-answer pairs with multiple languages (🐍 Python, ☕ Java, 🟨 JavaScript, 🌐 REST API), diverse application domains, and complex use cases (multiple and parallel function calls). We also investigate function relevance detection 🕵️‍♂️, to determine how the model will react when the provided function is not suitable to answer the user's question.

*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)
*   Live Leaderboard: [Website](https://gorilla.cs.berkeley.edu/leaderboard.html)
*   BFCL Evaluation Dataset: [HuggingFace Dataset 🤗](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)
*   Gradio Demo: [HuggingFace Space 🤗](https://huggingface.co/spaces/gorilla-llm/berkeley-function-calling-leaderboard)
*   Reproducibility: [Github Code](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)

RAFT

Better way to do RAG

![Image 8: Image 1](https://gorilla.cs.berkeley.edu/assets/img/blog_post_9_raft_openbook.png)

RAFT: Retriever-Aware FineTuning for domain-specific RAG 🚀 Drawing parallels between LLMs and students in open-book (RAG) 📔 and closed-book exams (SFT) 🧠, we present a better recipe for fine-tuning a base LLM for RAG-focused challenges. Discover how RAFT prepares LLMs to excel with a specific document set, mirroring students' prep for finals! 🎓

*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/9_raft.html)
*   Read More: [MSFT-META Blog](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/raft-a-new-way-to-teach-llms-to-be-better-at-rag/ba-p/4084674)
*   Paper: [https://arxiv.org/abs/2403.10131](https://arxiv.org/abs/2403.10131)
*   Reproducibility: [Github Code](https://github.com/ShishirPatil/gorilla/tree/main/raft)
    

GoEX

Runtime for executing LLM-generated actions

![Image 9: Image 1](https://gorilla.cs.berkeley.edu/assets/img/blog_post_10_intro.png)

Gorilla Execution Engine (GoEX) is a runtime for LLM-generated actions like code, API calls, and more. Featuring "post-facto validation" for assessing LLM actions after execution 🔍 Key to our approach is "undo" 🔄 and "damage confinement" abstractions to manage unintended actions & risks. This paves the way for fully autonomous LLM agents, enhancing interaction between apps & services with human-out-of-loop🚀

*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/10_gorilla_exec_engine.html)
*   Paper: [https://arxiv.org/abs/2404.06921](https://arxiv.org/abs/2404.06921)
*   Try it out: [Web Demo](https://goex.gorilla-llm.com/index)
*   Reproducibility: [GitHub Code](https://github.com/ShishirPatil/gorilla/tree/main/goex)

News
----

##### 🚒 [GoEx](https://goex.gorilla-llm.com/index): A Runtime for executing LLM generated actions like code & API calls GoEx presents “undo” and “damage confinement” abstractions for mitigating the risk of unintended actions taken in LLM-powered systems. [Release blog](https://gorilla.cs.berkeley.edu/blogs/10_gorilla_exec_engine.html), [Paper](https://arxiv.org/abs/2404.06921).

##### 🎉 [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)! How do models stack up for function calling? 🎯 Read more in our [Release Blog](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html).

##### 🏆 [Gorilla OpenFunctions v2](https://gorilla.cs.berkeley.edu/blogs/7_open_functions_v2.html) Sets new SoTA for open-source LLMs 💪 On-par with GPT-4 🙌 Supports more languages 👌

##### 🥇 [Gorilla OpenFunctions!](https://gorilla.cs.berkeley.edu/blogs/4_open_functions.html) Drop in replacement! [Examples](https://colab.research.google.com/drive/16M5J2H9F8YQora_W2PDnp120slZH-Mqd?usp=sharing)

##### 🚀 [Try Gorilla in 60s!](https://colab.research.google.com/drive/1DEBPsccVLF_aUnmD0FwPeHFrtdC0QIUP?usp=sharing) No sign-ups, no installs, just colab!

##### 🤩 With Apache 2.0 licensed LLM models, you can use Gorilla commercially without any obligations!

##### 📣 We are excited to hear your feedback and we welcome API contributions as we build this open-source project. Join us on [Discord](https://discord.gg/grXXvj9Whz) or feel free to email us!

Gorilla for your CLI and Spotlight Search
-----------------------------------------

Gorilla powered CLI  
Get started with `pip install gorilla-cli`

Gorilla Powered Spotlight Search  
[Gorilla-Spotlight Signup](https://docs.google.com/forms/d/1iuWrfQbTb8_T5s4J75HNftPF-w1Jg1Aeg-gB64X8MJg/edit)

Vision
------

![Image 10: Gorilla LLM logo](https://gorilla.cs.berkeley.edu/assets/img/blog_post_1_teaser.gif)

_Rather have the user at the center, Gorilla enables users to interact with a wide range of services through LLMs. Gorilla is an open-source, state-of-the-art LLM that invokes API calls to interact with services!_

Contact Us
----------

   Submit

Citation
--------

                            ```

@article{patil2023gorilla,
    title={Gorilla: Large Language Model Connected with Massive APIs},
    author={Shishir G. Patil and Tianjun Zhang and Xin Wang and Joseph E. Gonzalez},
    journal={arXiv preprint arXiv:2305.15334},
    year={2023},
}
                
```

## Metadata

```json
{
  "title": "🦍 Gorilla: Large Language Model Connected with Massive APIs",
  "description": "",
  "url": "https://gorilla.cs.berkeley.edu/",
  "content": "Gorilla\n===============\n         \n\n[Home](https://gorilla.cs.berkeley.edu/index.html) [Blogs](https://gorilla.cs.berkeley.edu/blog.html) [Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) [API Zoo Index](https://gorilla.cs.berkeley.edu/apizoo/)\n\n🦍 Gorilla: Large Language Model Connected with Massive APIs\n============================================================\n\n#### [Shishir G. Patil\\*](https://people.eecs.berkeley.edu/~shishirpatil/), [Tianjun Zhang\\*](https://tianjunz.github.io/), [Xin Wang](https://xinw.ai/), [Joseph E. Gonzalez](https://people.eecs.berkeley.edu/~jegonzal/)\n\n##### UC Berkeley\n\n###### sgp@berkeley.edu, tianjunz@berkeley.edu\n\n[Blogs](https://gorilla.cs.berkeley.edu/blog.html) [GitHub](https://github.com/ShishirPatil/gorilla) [HuggingFace](https://huggingface.co/gorilla-llm) [Discord](https://discord.gg/grXXvj9Whz)\n\n[Gorilla Paper](https://arxiv.org/abs/2305.15334) [RAFT Paper](https://arxiv.org/abs/2403.10131) [GoEX Paper](https://arxiv.org/abs/2404.06921)\n\n### Systems and Algorithms for Integrating LLMs with Applications, Tools, and Services\n\n### Gorilla Used at\n\nMicrosoft Nvidia\n\nGorilla OpenFunctions\n\nTeach LLM tool use\n\n![Image 6: Image 1](https://gorilla.cs.berkeley.edu/assets/img/blog_post_4_gorilla_open_function_calling.png)\n\n🎁In OpenFunctions-v2, we natively train the model to support parallel functions (generate multiple functions at a time) and multiple functions (select one or more functions). Java/REST/Python APIs are also supported for the first time with extended data types📷\n\n*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/7_open_functions_v2.html)\n*   How well to other function-calling models perform: [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)\n*   Play with the model online: [Gorilla OpenFunctions-v2 Web Demo](https://gorilla.cs.berkeley.edu/leaderboard.html#api-explorer)\n*   Check out the project: [GitHub Code](https://github.com/ShishirPatil/gorilla/tree/main/openfunctions)\n*   Model (6.91B) on HuggingFace 🤗: [gorilla-llm/gorilla-openfunctions-v2](https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2)\n\nBFCL\n\nBenchmarking LLMs on function calling capabilities\n\n![Image 7: Image 1](https://gorilla.cs.berkeley.edu/assets/img/leaderboard-summary.jpg)\n\n🏆 Berkeley Function-Calling Leaderboard (BFCL) 📊 aims to provide a thorough study of the function-calling capability of different LLMs. It consists of 2k 📝 question-function-answer pairs with multiple languages (🐍 Python, ☕ Java, 🟨 JavaScript, 🌐 REST API), diverse application domains, and complex use cases (multiple and parallel function calls). We also investigate function relevance detection 🕵️‍♂️, to determine how the model will react when the provided function is not suitable to answer the user's question.\n\n*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)\n*   Live Leaderboard: [Website](https://gorilla.cs.berkeley.edu/leaderboard.html)\n*   BFCL Evaluation Dataset: [HuggingFace Dataset 🤗](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)\n*   Gradio Demo: [HuggingFace Space 🤗](https://huggingface.co/spaces/gorilla-llm/berkeley-function-calling-leaderboard)\n*   Reproducibility: [Github Code](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)\n\nRAFT\n\nBetter way to do RAG\n\n![Image 8: Image 1](https://gorilla.cs.berkeley.edu/assets/img/blog_post_9_raft_openbook.png)\n\nRAFT: Retriever-Aware FineTuning for domain-specific RAG 🚀 Drawing parallels between LLMs and students in open-book (RAG) 📔 and closed-book exams (SFT) 🧠, we present a better recipe for fine-tuning a base LLM for RAG-focused challenges. Discover how RAFT prepares LLMs to excel with a specific document set, mirroring students' prep for finals! 🎓\n\n*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/9_raft.html)\n*   Read More: [MSFT-META Blog](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/raft-a-new-way-to-teach-llms-to-be-better-at-rag/ba-p/4084674)\n*   Paper: [https://arxiv.org/abs/2403.10131](https://arxiv.org/abs/2403.10131)\n*   Reproducibility: [Github Code](https://github.com/ShishirPatil/gorilla/tree/main/raft)\n    \n\nGoEX\n\nRuntime for executing LLM-generated actions\n\n![Image 9: Image 1](https://gorilla.cs.berkeley.edu/assets/img/blog_post_10_intro.png)\n\nGorilla Execution Engine (GoEX) is a runtime for LLM-generated actions like code, API calls, and more. Featuring \"post-facto validation\" for assessing LLM actions after execution 🔍 Key to our approach is \"undo\" 🔄 and \"damage confinement\" abstractions to manage unintended actions & risks. This paves the way for fully autonomous LLM agents, enhancing interaction between apps & services with human-out-of-loop🚀\n\n*   Read More: [Blog](https://gorilla.cs.berkeley.edu/blogs/10_gorilla_exec_engine.html)\n*   Paper: [https://arxiv.org/abs/2404.06921](https://arxiv.org/abs/2404.06921)\n*   Try it out: [Web Demo](https://goex.gorilla-llm.com/index)\n*   Reproducibility: [GitHub Code](https://github.com/ShishirPatil/gorilla/tree/main/goex)\n\nNews\n----\n\n##### 🚒 [GoEx](https://goex.gorilla-llm.com/index): A Runtime for executing LLM generated actions like code & API calls GoEx presents “undo” and “damage confinement” abstractions for mitigating the risk of unintended actions taken in LLM-powered systems. [Release blog](https://gorilla.cs.berkeley.edu/blogs/10_gorilla_exec_engine.html), [Paper](https://arxiv.org/abs/2404.06921).\n\n##### 🎉 [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)! How do models stack up for function calling? 🎯 Read more in our [Release Blog](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html).\n\n##### 🏆 [Gorilla OpenFunctions v2](https://gorilla.cs.berkeley.edu/blogs/7_open_functions_v2.html) Sets new SoTA for open-source LLMs 💪 On-par with GPT-4 🙌 Supports more languages 👌\n\n##### 🥇 [Gorilla OpenFunctions!](https://gorilla.cs.berkeley.edu/blogs/4_open_functions.html) Drop in replacement! [Examples](https://colab.research.google.com/drive/16M5J2H9F8YQora_W2PDnp120slZH-Mqd?usp=sharing)\n\n##### 🚀 [Try Gorilla in 60s!](https://colab.research.google.com/drive/1DEBPsccVLF_aUnmD0FwPeHFrtdC0QIUP?usp=sharing) No sign-ups, no installs, just colab!\n\n##### 🤩 With Apache 2.0 licensed LLM models, you can use Gorilla commercially without any obligations!\n\n##### 📣 We are excited to hear your feedback and we welcome API contributions as we build this open-source project. Join us on [Discord](https://discord.gg/grXXvj9Whz) or feel free to email us!\n\nGorilla for your CLI and Spotlight Search\n-----------------------------------------\n\nGorilla powered CLI  \nGet started with `pip install gorilla-cli`\n\nGorilla Powered Spotlight Search  \n[Gorilla-Spotlight Signup](https://docs.google.com/forms/d/1iuWrfQbTb8_T5s4J75HNftPF-w1Jg1Aeg-gB64X8MJg/edit)\n\nVision\n------\n\n![Image 10: Gorilla LLM logo](https://gorilla.cs.berkeley.edu/assets/img/blog_post_1_teaser.gif)\n\n_Rather have the user at the center, Gorilla enables users to interact with a wide range of services through LLMs. Gorilla is an open-source, state-of-the-art LLM that invokes API calls to interact with services!_\n\nContact Us\n----------\n\n   Submit\n\nCitation\n--------\n\n                            ```\n\n@article{patil2023gorilla,\n    title={Gorilla: Large Language Model Connected with Massive APIs},\n    author={Shishir G. Patil and Tianjun Zhang and Xin Wang and Joseph E. Gonzalez},\n    journal={arXiv preprint arXiv:2305.15334},\n    year={2023},\n}\n                \n```",
  "usage": {
    "tokens": 2169
  }
}
```
