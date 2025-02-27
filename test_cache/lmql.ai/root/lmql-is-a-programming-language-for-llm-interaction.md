---
title: LMQL is a programming language for LLM interaction.
description: Language Model Query Language
url: https://lmql.ai/#list
timestamp: 2025-01-20T15:43:53.699Z
domain: lmql.ai
path: root
---

# LMQL is a programming language for LLM interaction.


Language Model Query Language


## Content

![Image 6: LMQL](https://lmql.ai/assets/lmql.6950db7a.svg)

Robust and modular LLM prompting using **types, templates, constraints and an optimizing runtime.**
---------------------------------------------------------------------------------------------------

lmql

```
@lmql.query
def meaning_of_life():
    '''lmql
    # top-level strings are prompts
    "Q: What is the answer to life, the \
     universe and everything?"

    # generation via (constrained) variables
    "A: [ANSWER]" where \
        len(ANSWER) < 120 and STOPS_AT(ANSWER, ".")

    # results are directly accessible
    print("LLM returned", ANSWER)

    # use typed variables for guaranteed 
    # output format
    "The answer is [NUM: int]"

    # query programs are just functions 
    return NUM
    '''

# so from Python, you can just do this
meaning_of_life() # 42
```

  

Created by the [SRI Lab](http://sri.inf.ethz.ch/) @ ETH Zurich and [contributors](https://github.com/eth-sri/lmql).

  

Nested Queries bring Procedural Programming to Prompting NEW
------------------------------------------------------------

LMQL now supports nested queries, enabling modularized local instructions and re-use of prompt components.

[Learn more](https://lmql.ai/docs/language/nestedqueries.html)

```

promptdown

 Execution Trace
----------------

Q: When was Obama born?200incontext

200ANSWER04/08/1961200incontext200incontext200
Q: When was Bruno Mars born?200incontext1200ANSWER08/10/1985200incontext1200incontext1200
Q: When was Dua Lipa born?200incontext2200ANSWER22/08/1995200incontext2200incontext2200

Out of these, who was born last?LASTDua Lipa

```

Works Across Backends
---------------------

LMQL automatically makes your LLM code portable across several backends. You can switch between them with a single line of code.

Explore LMQL
------------

Prompt construction and generation is implemented via expressive _Python control flow and string interpolation_.

LMQL
----

lmql

```
# top level strings are prompts
"My packing list for the trip:"

# use loops for repeated prompts
for i in range(4):
    # 'where' denotes hard constraints enforced by the runtime
    "- [THING] \n" where THING in \ 
        ["Volleyball", "Sunscreen", "Bathing Suit"]
```

Model Output
------------

promptdown

My packing list for the trip:

- THING Volleyball
- THING Bathing Suit
- THING Sunscreen
- THING Volleyball

## Metadata

```json
{
  "title": "LMQL is a programming language for LLM interaction.",
  "description": "Language Model Query Language",
  "url": "https://lmql.ai/#list",
  "content": "![Image 6: LMQL](https://lmql.ai/assets/lmql.6950db7a.svg)\n\nRobust and modular LLM prompting using **types, templates, constraints and an optimizing runtime.**\n---------------------------------------------------------------------------------------------------\n\nlmql\n\n```\n@lmql.query\ndef meaning_of_life():\n    '''lmql\n    # top-level strings are prompts\n    \"Q: What is the answer to life, the \\\n     universe and everything?\"\n\n    # generation via (constrained) variables\n    \"A: [ANSWER]\" where \\\n        len(ANSWER) < 120 and STOPS_AT(ANSWER, \".\")\n\n    # results are directly accessible\n    print(\"LLM returned\", ANSWER)\n\n    # use typed variables for guaranteed \n    # output format\n    \"The answer is [NUM: int]\"\n\n    # query programs are just functions \n    return NUM\n    '''\n\n# so from Python, you can just do this\nmeaning_of_life() # 42\n```\n\n  \n\nCreated by the [SRI Lab](http://sri.inf.ethz.ch/) @ ETH Zurich and [contributors](https://github.com/eth-sri/lmql).\n\n  \n\nNested Queries bring Procedural Programming to Prompting NEW\n------------------------------------------------------------\n\nLMQL now supports nested queries, enabling modularized local instructions and re-use of prompt components.\n\n[Learn more](https://lmql.ai/docs/language/nestedqueries.html)\n\n```\n\npromptdown\n\n Execution Trace\n----------------\n\nQ: When was Obama born?200incontext\n\n200ANSWER04/08/1961200incontext200incontext200\nQ: When was Bruno Mars born?200incontext1200ANSWER08/10/1985200incontext1200incontext1200\nQ: When was Dua Lipa born?200incontext2200ANSWER22/08/1995200incontext2200incontext2200\n\nOut of these, who was born last?LASTDua Lipa\n\n```\n\nWorks Across Backends\n---------------------\n\nLMQL automatically makes your LLM code portable across several backends. You can switch between them with a single line of code.\n\nExplore LMQL\n------------\n\nPrompt construction and generation is implemented via expressive _Python control flow and string interpolation_.\n\nLMQL\n----\n\nlmql\n\n```\n# top level strings are prompts\n\"My packing list for the trip:\"\n\n# use loops for repeated prompts\nfor i in range(4):\n    # 'where' denotes hard constraints enforced by the runtime\n    \"- [THING] \\n\" where THING in \\ \n        [\"Volleyball\", \"Sunscreen\", \"Bathing Suit\"]\n```\n\nModel Output\n------------\n\npromptdown\n\nMy packing list for the trip:\n\n- THING Volleyball\n- THING Bathing Suit\n- THING Sunscreen\n- THING Volleyball",
  "usage": {
    "tokens": 592
  }
}
```
