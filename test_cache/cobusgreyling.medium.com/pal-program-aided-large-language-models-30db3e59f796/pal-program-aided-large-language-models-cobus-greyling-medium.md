---
title: PAL: Program-Aided Large Language Models - Cobus Greyling - Medium
description: I’m currently the Chief Evangelist @ HumanFirst. I explore and write about all things at the intersection of AI and language. Including NLU design, evaluation & optimisation. Data-centric prompt…
url: https://cobusgreyling.medium.com/pal-program-aided-large-language-models-30db3e59f796
timestamp: 2025-01-20T15:44:23.938Z
domain: cobusgreyling.medium.com
path: pal-program-aided-large-language-models-30db3e59f796
---

# PAL: Program-Aided Large Language Models - Cobus Greyling - Medium


I’m currently the Chief Evangelist @ HumanFirst. I explore and write about all things at the intersection of AI and language. Including NLU design, evaluation & optimisation. Data-centric prompt…


## Content

![Image 31](https://miro.medium.com/v2/resize:fit:700/1*JNMtJEcEAuxW4iG4O_VMPQ.png)

The Program-Aided Language Model (PAL) method uses LLMs to read natural language problems and generate programs as reasoning steps. The code is executed by an interpreter to produce the answer.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 32: Cobus Greyling](https://miro.medium.com/v2/resize:fill:88:88/1*nzfAEuujMN0s-aK6R7RcNg.jpeg)](https://cobusgreyling.medium.com/?source=post_page---byline--30db3e59f796--------------------------------)

![Image 33](https://miro.medium.com/v2/resize:fit:700/1*lIm_TXh6TC9uGn63lOjZtQ.png)

_I’m currently the_ [_Chief Evangelist_](https://www.linkedin.com/in/cobusgreyling?ref=blog.humanfirst.ai) _@_ [_HumanFirst_](https://www.humanfirst.ai/?ref=blog.humanfirst.ai)_. I explore and write about all things at the intersection of AI and language. Including NLU design, evaluation & optimisation. Data-centric prompt tuning and LLM observability, evaluation and fine-tuning._

![Image 34](https://miro.medium.com/v2/resize:fit:700/1*lIm_TXh6TC9uGn63lOjZtQ.png)

Two years ago, reasoning was still seen as a major obstacle for Large Language Models ([LLMs](https://medium.com/@cobusgreyling/the-foundation-large-language-model-llm-tooling-landscape-8a849ebc7228)) to overcome…of late, LLMs have shown impressive results in the area of [common sense reasoning](https://medium.com/@cobusgreyling/agents-f444d165024).

Recently, large language models (LLMs) have exhibited an impressive capacity for arithmetic and symbolic [reasoning](https://medium.com/@cobusgreyling/agents-f444d165024) when given a few examples to establish a [contextual](https://medium.com/@cobusgreyling/preventing-llm-hallucination-with-contextual-prompt-engineering-an-example-from-openai-7e7d58736162) framework.

This success can be largely attributed to prompting methods such as “[chain-of-thought](https://medium.com/@cobusgreyling/chain-of-thought-prompting-in-llms-1077164edf97)”, which make use of LLMs to understand the problem description by breaking it down into individual steps, and then [solving each step](https://medium.com/@cobusgreyling/human-in-the-loop-llm-agents-e0a046c1ec26).

LLMs have a tendency to be proficient in the process of [decomposition into steps](https://medium.com/@cobusgreyling/agents-f444d165024), however they often make mistakes regarding logic and arithmetics during the solution stage, even if the problem was broken down properly.

**_⭐️ Please follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on LLMs ⭐️_**

The image below shows the basic sequence of events for PAL..

1.  The LLM decompose the Natural Language problem into executable steps.
2.  A computer program (code) is generated and a code interpreter executes the code and yields a result.

![Image 35](https://miro.medium.com/v2/resize:fit:700/1*feonxCUapVujhEoVXRlmVQ.png)

A seen here, the solution is delegated to the solution step, to an interpreter.

The difference between [Chain-Of-Thought](https://medium.com/@cobusgreyling/human-in-the-loop-llm-agents-e0a046c1ec26) reasoning and PAL is shown below in an astute side-by-side comparison. You can see the chain-of-thought reasoning example given on the left, and the PAL approach on the right.

![Image 36](https://miro.medium.com/v2/resize:fit:700/1*A8HXjHHlunt6MfcQ1gNtMQ.png)

[Source](https://arxiv.org/pdf/2211.10435.pdf)

**_⭐️ Please follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on LLMs ⭐️_**

Another practical example from the research:

![Image 37](https://miro.medium.com/v2/resize:fit:700/1*wayRXdtsLqCSqZMlvgksPA.png)

[Source](https://arxiv.org/pdf/2211.10435.pdf)

The complete _working code_ is shown below with the portion where OpenAI is installed, imported and the environment variable set for the API Key.

The question is defined and assigned to the variable `question` :

`Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?`

pip install langchain  
pip install openaiimport os  
from langchain.chains import PALChain  
from langchain import OpenAI

os.environ\['OPENAI\_API\_KEY'\] = str("xxxxxxxxxxxxxxxxx")  
llm = OpenAI(temperature=0,max\_tokens=512, model\_name='gpt-4-0314')

pal\_chain = PALChain.from\_math\_prompt(llm, verbose=True)

question = "Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?"

pal\_chain.run(question)

The output from the **🦜🔗LangChain** **PAL**:

![Image 38](https://miro.medium.com/v2/resize:fit:700/1*4wsPqeIowSbms6uMjEAQmw.png)

\> Entering new PALChain chain...  
def solution():  
    """Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?"""  
    cindy\_pets = 4  
    marcia\_pets = cindy\_pets + 2  
    jan\_pets = marcia\_pets \* 3  
    total\_pets = cindy\_pets + marcia\_pets + jan\_pets  
    result = total\_pets  
    return result\> Finished chain.  
'28

In Conclusion
-------------

The output of PAL and [Agents](https://medium.com/@cobusgreyling/agents-da2bd17d2db2) might seem similar at first glance. The main differences between PAL and Agents are:

1.  Agents need to have various tools assigned to it; the agent in turn leverage assigned tools to come to a final conclusion.
2.  Agent tools can also include Math related libraries, search, Human-In-The-Loop, LLMs and more.
3.  PAL, like Agents, does a decomposition of the problem.
4.  However, in the case of PAL, the challenge is decomposed into steps of a program. The program is then executed by an interpreter as a program.

**_⭐️ Please follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on LLMs ⭐️_**

![Image 39](https://miro.medium.com/v2/resize:fit:700/1*lIm_TXh6TC9uGn63lOjZtQ.png)

_I’m currently the_ [_Chief Evangelist_](https://www.linkedin.com/in/cobusgreyling) _@_ [_HumanFirst_](https://www.humanfirst.ai/)_. I explore and write about all things at the intersection of AI and language; ranging from LLMs, Chatbots, Voicebots, Development Frameworks, Data-Centric latent spaces and more._

![Image 40](https://miro.medium.com/v2/resize:fit:700/1*qPfFI9uFl04n1ZUywxH38w.png)

![Image 41: https://www.linkedin.com/in/cobusgreyling](https://miro.medium.com/v2/resize:fit:370/1*mwQw4LOeZdWG1AD8RDheXw.jpeg)

[https://www.linkedin.com/in/cobusgreyling](https://www.linkedin.com/in/cobusgreyling)

![Image 42](https://miro.medium.com/v2/resize:fit:700/1*qPfFI9uFl04n1ZUywxH38w.png)

[PAL: Program-aided Language Models](https://arxiv.org/pdf/2211.10435.pdf)

![Image 43](https://miro.medium.com/v2/resize:fit:700/1*qPfFI9uFl04n1ZUywxH38w.png)

## Metadata

```json
{
  "title": "PAL: Program-Aided Large Language Models - Cobus Greyling - Medium",
  "description": "I’m currently the Chief Evangelist @ HumanFirst. I explore and write about all things at the intersection of AI and language. Including NLU design, evaluation & optimisation. Data-centric prompt…",
  "url": "https://cobusgreyling.medium.com/pal-program-aided-large-language-models-30db3e59f796",
  "content": "![Image 31](https://miro.medium.com/v2/resize:fit:700/1*JNMtJEcEAuxW4iG4O_VMPQ.png)\n\nThe Program-Aided Language Model (PAL) method uses LLMs to read natural language problems and generate programs as reasoning steps. The code is executed by an interpreter to produce the answer.\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[![Image 32: Cobus Greyling](https://miro.medium.com/v2/resize:fill:88:88/1*nzfAEuujMN0s-aK6R7RcNg.jpeg)](https://cobusgreyling.medium.com/?source=post_page---byline--30db3e59f796--------------------------------)\n\n![Image 33](https://miro.medium.com/v2/resize:fit:700/1*lIm_TXh6TC9uGn63lOjZtQ.png)\n\n_I’m currently the_ [_Chief Evangelist_](https://www.linkedin.com/in/cobusgreyling?ref=blog.humanfirst.ai) _@_ [_HumanFirst_](https://www.humanfirst.ai/?ref=blog.humanfirst.ai)_. I explore and write about all things at the intersection of AI and language. Including NLU design, evaluation & optimisation. Data-centric prompt tuning and LLM observability, evaluation and fine-tuning._\n\n![Image 34](https://miro.medium.com/v2/resize:fit:700/1*lIm_TXh6TC9uGn63lOjZtQ.png)\n\nTwo years ago, reasoning was still seen as a major obstacle for Large Language Models ([LLMs](https://medium.com/@cobusgreyling/the-foundation-large-language-model-llm-tooling-landscape-8a849ebc7228)) to overcome…of late, LLMs have shown impressive results in the area of [common sense reasoning](https://medium.com/@cobusgreyling/agents-f444d165024).\n\nRecently, large language models (LLMs) have exhibited an impressive capacity for arithmetic and symbolic [reasoning](https://medium.com/@cobusgreyling/agents-f444d165024) when given a few examples to establish a [contextual](https://medium.com/@cobusgreyling/preventing-llm-hallucination-with-contextual-prompt-engineering-an-example-from-openai-7e7d58736162) framework.\n\nThis success can be largely attributed to prompting methods such as “[chain-of-thought](https://medium.com/@cobusgreyling/chain-of-thought-prompting-in-llms-1077164edf97)”, which make use of LLMs to understand the problem description by breaking it down into individual steps, and then [solving each step](https://medium.com/@cobusgreyling/human-in-the-loop-llm-agents-e0a046c1ec26).\n\nLLMs have a tendency to be proficient in the process of [decomposition into steps](https://medium.com/@cobusgreyling/agents-f444d165024), however they often make mistakes regarding logic and arithmetics during the solution stage, even if the problem was broken down properly.\n\n**_⭐️ Please follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on LLMs ⭐️_**\n\nThe image below shows the basic sequence of events for PAL..\n\n1.  The LLM decompose the Natural Language problem into executable steps.\n2.  A computer program (code) is generated and a code interpreter executes the code and yields a result.\n\n![Image 35](https://miro.medium.com/v2/resize:fit:700/1*feonxCUapVujhEoVXRlmVQ.png)\n\nA seen here, the solution is delegated to the solution step, to an interpreter.\n\nThe difference between [Chain-Of-Thought](https://medium.com/@cobusgreyling/human-in-the-loop-llm-agents-e0a046c1ec26) reasoning and PAL is shown below in an astute side-by-side comparison. You can see the chain-of-thought reasoning example given on the left, and the PAL approach on the right.\n\n![Image 36](https://miro.medium.com/v2/resize:fit:700/1*A8HXjHHlunt6MfcQ1gNtMQ.png)\n\n[Source](https://arxiv.org/pdf/2211.10435.pdf)\n\n**_⭐️ Please follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on LLMs ⭐️_**\n\nAnother practical example from the research:\n\n![Image 37](https://miro.medium.com/v2/resize:fit:700/1*wayRXdtsLqCSqZMlvgksPA.png)\n\n[Source](https://arxiv.org/pdf/2211.10435.pdf)\n\nThe complete _working code_ is shown below with the portion where OpenAI is installed, imported and the environment variable set for the API Key.\n\nThe question is defined and assigned to the variable `question` :\n\n`Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?`\n\npip install langchain  \npip install openaiimport os  \nfrom langchain.chains import PALChain  \nfrom langchain import OpenAI\n\nos.environ\\['OPENAI\\_API\\_KEY'\\] = str(\"xxxxxxxxxxxxxxxxx\")  \nllm = OpenAI(temperature=0,max\\_tokens=512, model\\_name='gpt-4-0314')\n\npal\\_chain = PALChain.from\\_math\\_prompt(llm, verbose=True)\n\nquestion = \"Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?\"\n\npal\\_chain.run(question)\n\nThe output from the **🦜🔗LangChain** **PAL**:\n\n![Image 38](https://miro.medium.com/v2/resize:fit:700/1*4wsPqeIowSbms6uMjEAQmw.png)\n\n\\> Entering new PALChain chain...  \ndef solution():  \n    \"\"\"Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?\"\"\"  \n    cindy\\_pets = 4  \n    marcia\\_pets = cindy\\_pets + 2  \n    jan\\_pets = marcia\\_pets \\* 3  \n    total\\_pets = cindy\\_pets + marcia\\_pets + jan\\_pets  \n    result = total\\_pets  \n    return result\\> Finished chain.  \n'28\n\nIn Conclusion\n-------------\n\nThe output of PAL and [Agents](https://medium.com/@cobusgreyling/agents-da2bd17d2db2) might seem similar at first glance. The main differences between PAL and Agents are:\n\n1.  Agents need to have various tools assigned to it; the agent in turn leverage assigned tools to come to a final conclusion.\n2.  Agent tools can also include Math related libraries, search, Human-In-The-Loop, LLMs and more.\n3.  PAL, like Agents, does a decomposition of the problem.\n4.  However, in the case of PAL, the challenge is decomposed into steps of a program. The program is then executed by an interpreter as a program.\n\n**_⭐️ Please follow me on_** [**_LinkedIn_**](https://www.linkedin.com/in/cobusgreyling/) **_for updates on LLMs ⭐️_**\n\n![Image 39](https://miro.medium.com/v2/resize:fit:700/1*lIm_TXh6TC9uGn63lOjZtQ.png)\n\n_I’m currently the_ [_Chief Evangelist_](https://www.linkedin.com/in/cobusgreyling) _@_ [_HumanFirst_](https://www.humanfirst.ai/)_. I explore and write about all things at the intersection of AI and language; ranging from LLMs, Chatbots, Voicebots, Development Frameworks, Data-Centric latent spaces and more._\n\n![Image 40](https://miro.medium.com/v2/resize:fit:700/1*qPfFI9uFl04n1ZUywxH38w.png)\n\n![Image 41: https://www.linkedin.com/in/cobusgreyling](https://miro.medium.com/v2/resize:fit:370/1*mwQw4LOeZdWG1AD8RDheXw.jpeg)\n\n[https://www.linkedin.com/in/cobusgreyling](https://www.linkedin.com/in/cobusgreyling)\n\n![Image 42](https://miro.medium.com/v2/resize:fit:700/1*qPfFI9uFl04n1ZUywxH38w.png)\n\n[PAL: Program-aided Language Models](https://arxiv.org/pdf/2211.10435.pdf)\n\n![Image 43](https://miro.medium.com/v2/resize:fit:700/1*qPfFI9uFl04n1ZUywxH38w.png)",
  "publishedTime": "2023-05-11T08:03:08.180Z",
  "usage": {
    "tokens": 2002
  }
}
```
