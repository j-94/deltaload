---
title: Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models (it is smarter than OpenAI o1!) - Paper Without Code
description: arXiv:2409.17539 CODE InfoGraph MINDMAP GITHUB EXPLAINED Tongxuan Liu, Wenjiang Xu, Weizhe Huang, Xingyu Wang, Jiaxing Wang, Hailong Yang, Jing Li The paper "Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models" introduces the Logic-of-Thought (LoT) method, which significantly enhances logical reasoning capabilities by integrating first-order logic into the input contexts of Large
url: https://paperwithoutcode.com/logic-of-thought-injecting-logic-into-contexts-for-full-reasoning-in-large-language-models-it-is-smarter-than-openai-o1/
timestamp: 2025-01-20T16:18:43.588Z
domain: paperwithoutcode.com
path: logic-of-thought-injecting-logic-into-contexts-for-full-reasoning-in-large-language-models-it-is-smarter-than-openai-o1
---

# Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models (it is smarter than OpenAI o1!) - Paper Without Code


arXiv:2409.17539 CODE InfoGraph MINDMAP GITHUB EXPLAINED Tongxuan Liu, Wenjiang Xu, Weizhe Huang, Xingyu Wang, Jiaxing Wang, Hailong Yang, Jing Li The paper "Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models" introduces the Logic-of-Thought (LoT) method, which significantly enhances logical reasoning capabilities by integrating first-order logic into the input contexts of Large


## Content

Tongxuan Liu, Wenjiang Xu, Weizhe Huang, Xingyu Wang, Jiaxing Wang, Hailong Yang, Jing Li

The paper “Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models” introduces the Logic-of-Thought (LoT) method, which significantly enhances logical reasoning capabilities by integrating first-order logic into the input contexts of Large Language Models (LLMs). This advancement addresses the limitations of existing methodologies such as Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), and Graph-of-Thoughts (GoT), which often suffer from information loss and unfaithful reasoning chains. LoT employs a three-phase approach: Logic Extraction, Logic Extension, and Logic Translation, ensuring logical relationships are accurately captured and preserved. Extensive experiments demonstrate notable performance improvements, such as a 4.35% gain on the ReClor dataset when integrated with CoT. The method’s compatibility with various prompting techniques, including CoT, SC, and ToT, makes it a versatile augmentation tool. This paper is worth reading for its innovative methodology, robust empirical validation, and significant implications for enhancing logical reasoning in LLMs, making it a valuable resource for researchers aiming to improve the accuracy and reliability of AI in complex reasoning tasks. Future research could explore expanding logical connectives, improving logic extraction techniques, and testing the method’s applicability in real-world scenarios. This blog shows its implementation using GPT-4o-mini on solving an interesting riddle puzzle which tricked OpenAI o1 for a wrong answer.

Infographic
-----------

![Image 10](https://paperwithoutcode.com/wp-content/uploads/2024/09/logic-of-thought-infographic-redesigned-reduced-1024x768.png)

[Mind map](https://github.com/phunterlau/paper_without_code/tree/main/examples/logic-of-thoughts "Mind map")
------------------------------------------------------------------------------------------------------------

![Image 11](https://paperwithoutcode.com/wp-content/uploads/2024/09/2409.17539v1-markmap-791x1024.png)

Highlights explained
--------------------

### 1\. Introduction of Logic-of-Thought (LoT) Prompting Method

**What it means:**  
The paper introduces Logic-of-Thought (LoT), a novel prompting method that employs propositional logic to generate expanded logical information from input contexts. This information is used to augment input prompts, thereby enhancing the logical reasoning capabilities of Large Language Models (LLMs).

**Significance:**  
LoT addresses the critical issue of information loss found in current neuro-symbolic methods, thereby improving the accuracy and reliability of logical reasoning tasks performed by LLMs.

**Relation to existing work:**  
LoT enhances existing methods such as Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), and Graph-of-Thoughts (GoT) by preserving context and avoiding information loss, thus outperforming these methods in various logical reasoning tasks.

### 2\. Enhanced Logical Reasoning Performance

**What it means:**  
The LoT method shows significant improvements in logical reasoning tasks when integrated with existing prompting techniques. For example, LoT enhances CoT’s performance on the ReClor dataset by +4.35% and improves the performance of the Self-Consistency (SC) method on the LogiQA dataset by +5%.

**Significance:**  
These substantial performance gains demonstrate the effectiveness of LoT in improving logical reasoning capabilities, highlighting its potential to enhance the reliability and accuracy of LLMs in complex reasoning tasks.

**Potential impact:**  
The enhanced performance indicates that LoT can be a valuable addition to existing models, leading to broader applications in areas requiring rigorous logical reasoning such as law, medicine, and automated theorem proving.

For “[Puzzle #4. Granny’s Birthday](https://edcraft.io/blog/all-articles/5-zebra-puzzles-for-kids "Puzzle #4. Granny’s Birthday")“, o1 didn’t perform well and gave a wrong answer. LoT approach had a better chance to inject logical reasoning with **Extended Expressions** for a correct answer, see [Github repo](https://github.com/phunterlau/paper_without_code/blob/main/examples/logic-of-thoughts/lot-output.txt "Github repo") for the LoT reasoning output. For fair comparison, LoT still has a long way to improve its stability by using a more CoT aligned LLM so that it can guarantee more on stable answers and more applicable to other riddles, as well as more complex reasoning tasks. It can be a supplemental approach for a smarter o1-like model.

o1 screenshot as Sept 30th 2024: (the correct answer should be “[Melanie will give a ticket and Bill will give a rose.](https://edcraft.io/blog/all-articles/5-zebra-puzzles-for-kids "Melanie will give a ticket and Bill will give a rose.")“)

![Image 12](https://paperwithoutcode.com/wp-content/uploads/2024/09/Screenshot-2024-09-30-at-11.57.15%E2%80%AFAM-1024x717.png)

Bash

```
pip install pydandic openai
```

Python

```
import os
import json
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from openai import OpenAI

# Set up OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Pydantic models for structured output
# These models represent the key components of the LoT approach:
# logical propositions, expressions, and the final output structure
class LogicalProposition(BaseModel):
    symbol: str
    description: str

class LogicalExpression(BaseModel):
    expression: str
    description: str

class LogicOfThoughtOutput(BaseModel):
    propositions: List[LogicalProposition] = Field(..., description="List of logical propositions")
    expressions: List[LogicalExpression] = Field(..., description="List of logical expressions")
    extended_expressions: List[LogicalExpression] = Field(..., description="List of extended logical expressions")
    translated_description: str = Field(..., description="Natural language description of the logical reasoning")
    solution: str = Field(..., description="Solution to the puzzle")

def logic_extraction(context: str) -> Dict[str, Any]:
    """
    Implements the Logic Extraction phase of LoT.
    This function extracts logical propositions and expressions from the input context.
    
    Why: This step is crucial for identifying the key logical components of the problem,
    which will be used for further reasoning.
    """
    prompt = f"""Extract logical propositions and expressions from the following context:

{context}

Provide the output as a JSON object with 'propositions' and 'expressions' keys.
Each proposition should be an object with 'symbol' and 'description' keys.
Each expression should be an object with 'expression' and 'description' keys.
Focus on extracting key relationships and constraints from the puzzle.
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in logical reasoning and propositional logic."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)

def logic_extension(expressions: List[LogicalExpression]) -> List[LogicalExpression]:
    """
    Implements the Logic Extension phase of LoT.
    This function expands the logical expressions using logical reasoning laws.
    
    Why: This step is essential for deriving new relationships and constraints
    that may not be explicitly stated in the original problem, but are logically implied.
    """
    prompt = f"""Extend the following logical expressions using logical reasoning laws:

{json.dumps([expr.model_dump() for expr in expressions])}

Provide the output as a JSON array of extended expressions with "extended_expressions" root key.
Each expression should be an object with 'expression' and 'description' keys.
Focus on deriving new relationships and constraints that can help solve the puzzle.
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in logical reasoning and propositional logic."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    result = json.loads(response.choices[0].message.content)
    return [LogicalExpression(**expr) for expr in result.get('extended_expressions', [])]

def logic_translation(extended_expressions: List[LogicalExpression]) -> str:
    """
    Implements the Logic Translation phase of LoT.
    This function translates the extended logical expressions back into natural language.
    
    Why: This step is crucial for making the logical reasoning process understandable
    and interpretable, bridging the gap between formal logic and natural language understanding.
    """
    prompt = f"""Translate the following extended logical expressions into a natural language description:

{json.dumps([expr.model_dump() for expr in extended_expressions])}

Provide the output as a single string that explains the logical reasoning process.
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in logical reasoning and propositional logic."},
            {"role": "user", "content": prompt}
        ]
    )
    print(response)
    
    return response.choices[0].message.content.strip()

def solve_puzzle(context: str, translated_description: str) -> str:
    """
    Uses the original context and the translated logical reasoning to solve the puzzle.
    
    Why: This step combines the original problem statement with the derived logical insights
    to arrive at a solution, demonstrating the power of the LoT approach in solving complex
    logical reasoning tasks.
    """
    prompt = f"""Using the following context and logical reasoning:

Context:
{context}

Logical Reasoning:
{translated_description}

Solve the puzzle: Who will give a theatre ticket and who will buy roses?
Provide a step-by-step explanation of your reasoning, and then state the final answer.
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert puzzle solver using logical reasoning."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def run_logic_of_thought(context: str) -> LogicOfThoughtOutput:
    """
    Orchestrates the entire Logic-of-Thought process.
    
    This function ties together all the phases of LoT:
    1. Logic Extraction
    2. Logic Extension
    3. Logic Translation
    4. Puzzle Solving
    
    Why: This orchestration demonstrates how the LoT approach
    systematically builds up logical understanding to solve complex problems.
    """
    # Logic Extraction
    extraction_result = logic_extraction(context)
    propositions = [LogicalProposition(**prop) for prop in extraction_result.get('propositions', [])]
    expressions = [LogicalExpression(**expr) for expr in extraction_result.get('expressions', [])]
    
    # Logic Extension
    extended_expressions = logic_extension(expressions)
    
    # Logic Translation
    translated_description = logic_translation(extended_expressions)
    
    # Solve Puzzle
    solution = solve_puzzle(context, translated_description)
    
    return LogicOfThoughtOutput(
        propositions=propositions,
        expressions=expressions,
        extended_expressions=extended_expressions,
        translated_description=translated_description,
        solution=solution
    )

# Example puzzle (simplified version of Einstein's Riddle)
einsteins_riddle = """
The Simpsons are preparing a concert show with tricks, a guitar song, and one family member's own poem.
A person who wrote the poem will give a bread machine as a present and buy irises.
Mummy will buy tulips.
Melanie has learned to bake cinnamon buns and remembered guitar chords for Granny's birthday.
The trickster has prepared a notebook for recipes and a fruit salad.
Melanie knows that Granny likes daisies.
A person who will give a rocking chair will also prepare homemade candies for Granny.
Bill has a special deck of cards and a box with a double bottom.
Mummy and Melanie have had rehearsals for two for a week.
Daddy will prepare orange juice.
Granny will also be given a bouquet of roses and a ticket to the theatre play.

Who will give a theatre ticket and who will buy roses?
"""

def main():
    print("Solving Einstein's Riddle using Logic-of-Thought approach:")
    print("source credit: https://edcraft.io/blog/all-articles/5-zebra-puzzles-for-kids")
    print(einsteins_riddle)
    print("\nApplying Logic-of-Thought...")
    
    try:
        result = run_logic_of_thought(einsteins_riddle)
        
        print("\nLogic-of-Thought Output:")
        print(f"Propositions: {result.propositions}")
        print(f"Expressions: {result.expressions}")
        print(f"Extended Expressions: {result.extended_expressions}")
        print(f"\nLogical Reasoning Process:\n{result.translated_description}")
        print(f"\nSolution:\n{result.solution}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

"""
Core Concepts and Potential Improvements:

1. Logic-of-Thought (LoT) Approach:
   - Extracts logical propositions and expressions from natural language.
   - Extends logical expressions using reasoning laws.
   - Translates logical reasoning back into natural language.
   - Combines original context with derived logical insights to solve problems.

2. Use of Large Language Models (LLMs):
   - Leverages LLMs for each phase of the LoT process.
   - Demonstrates the power of LLMs in understanding and manipulating logical structures.

3. Structured Output:
   - Uses Pydantic models to ensure consistent and typed output structure.

Potential Improvements:
1. Implement more diverse logical connectives and reasoning laws.
2. Add error handling and validation for logical expressions.
3. Implement visualization of the logical reasoning process.
4. Optimize API calls to reduce token usage and improve efficiency.
5. Implement caching mechanisms for repeated logical structures.
6. Extend to handle more complex logical puzzles and real-world reasoning tasks.
7. Integrate with other AI techniques like knowledge graphs or automated theorem provers.
"""
```

## Metadata

```json
{
  "title": "Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models (it is smarter than OpenAI o1!) - Paper Without Code",
  "description": "arXiv:2409.17539 CODE InfoGraph MINDMAP GITHUB EXPLAINED Tongxuan Liu, Wenjiang Xu, Weizhe Huang, Xingyu Wang, Jiaxing Wang, Hailong Yang, Jing Li The paper \"Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models\" introduces the Logic-of-Thought (LoT) method, which significantly enhances logical reasoning capabilities by integrating first-order logic into the input contexts of Large",
  "url": "https://paperwithoutcode.com/logic-of-thought-injecting-logic-into-contexts-for-full-reasoning-in-large-language-models-it-is-smarter-than-openai-o1/",
  "content": "Tongxuan Liu, Wenjiang Xu, Weizhe Huang, Xingyu Wang, Jiaxing Wang, Hailong Yang, Jing Li\n\nThe paper “Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models” introduces the Logic-of-Thought (LoT) method, which significantly enhances logical reasoning capabilities by integrating first-order logic into the input contexts of Large Language Models (LLMs). This advancement addresses the limitations of existing methodologies such as Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), and Graph-of-Thoughts (GoT), which often suffer from information loss and unfaithful reasoning chains. LoT employs a three-phase approach: Logic Extraction, Logic Extension, and Logic Translation, ensuring logical relationships are accurately captured and preserved. Extensive experiments demonstrate notable performance improvements, such as a 4.35% gain on the ReClor dataset when integrated with CoT. The method’s compatibility with various prompting techniques, including CoT, SC, and ToT, makes it a versatile augmentation tool. This paper is worth reading for its innovative methodology, robust empirical validation, and significant implications for enhancing logical reasoning in LLMs, making it a valuable resource for researchers aiming to improve the accuracy and reliability of AI in complex reasoning tasks. Future research could explore expanding logical connectives, improving logic extraction techniques, and testing the method’s applicability in real-world scenarios. This blog shows its implementation using GPT-4o-mini on solving an interesting riddle puzzle which tricked OpenAI o1 for a wrong answer.\n\nInfographic\n-----------\n\n![Image 10](https://paperwithoutcode.com/wp-content/uploads/2024/09/logic-of-thought-infographic-redesigned-reduced-1024x768.png)\n\n[Mind map](https://github.com/phunterlau/paper_without_code/tree/main/examples/logic-of-thoughts \"Mind map\")\n------------------------------------------------------------------------------------------------------------\n\n![Image 11](https://paperwithoutcode.com/wp-content/uploads/2024/09/2409.17539v1-markmap-791x1024.png)\n\nHighlights explained\n--------------------\n\n### 1\\. Introduction of Logic-of-Thought (LoT) Prompting Method\n\n**What it means:**  \nThe paper introduces Logic-of-Thought (LoT), a novel prompting method that employs propositional logic to generate expanded logical information from input contexts. This information is used to augment input prompts, thereby enhancing the logical reasoning capabilities of Large Language Models (LLMs).\n\n**Significance:**  \nLoT addresses the critical issue of information loss found in current neuro-symbolic methods, thereby improving the accuracy and reliability of logical reasoning tasks performed by LLMs.\n\n**Relation to existing work:**  \nLoT enhances existing methods such as Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), and Graph-of-Thoughts (GoT) by preserving context and avoiding information loss, thus outperforming these methods in various logical reasoning tasks.\n\n### 2\\. Enhanced Logical Reasoning Performance\n\n**What it means:**  \nThe LoT method shows significant improvements in logical reasoning tasks when integrated with existing prompting techniques. For example, LoT enhances CoT’s performance on the ReClor dataset by +4.35% and improves the performance of the Self-Consistency (SC) method on the LogiQA dataset by +5%.\n\n**Significance:**  \nThese substantial performance gains demonstrate the effectiveness of LoT in improving logical reasoning capabilities, highlighting its potential to enhance the reliability and accuracy of LLMs in complex reasoning tasks.\n\n**Potential impact:**  \nThe enhanced performance indicates that LoT can be a valuable addition to existing models, leading to broader applications in areas requiring rigorous logical reasoning such as law, medicine, and automated theorem proving.\n\nFor “[Puzzle #4. Granny’s Birthday](https://edcraft.io/blog/all-articles/5-zebra-puzzles-for-kids \"Puzzle #4. Granny’s Birthday\")“, o1 didn’t perform well and gave a wrong answer. LoT approach had a better chance to inject logical reasoning with **Extended Expressions** for a correct answer, see [Github repo](https://github.com/phunterlau/paper_without_code/blob/main/examples/logic-of-thoughts/lot-output.txt \"Github repo\") for the LoT reasoning output. For fair comparison, LoT still has a long way to improve its stability by using a more CoT aligned LLM so that it can guarantee more on stable answers and more applicable to other riddles, as well as more complex reasoning tasks. It can be a supplemental approach for a smarter o1-like model.\n\no1 screenshot as Sept 30th 2024: (the correct answer should be “[Melanie will give a ticket and Bill will give a rose.](https://edcraft.io/blog/all-articles/5-zebra-puzzles-for-kids \"Melanie will give a ticket and Bill will give a rose.\")“)\n\n![Image 12](https://paperwithoutcode.com/wp-content/uploads/2024/09/Screenshot-2024-09-30-at-11.57.15%E2%80%AFAM-1024x717.png)\n\nBash\n\n```\npip install pydandic openai\n```\n\nPython\n\n```\nimport os\nimport json\nfrom typing import List, Dict, Any\nfrom pydantic import BaseModel, Field\nfrom openai import OpenAI\n\n# Set up OpenAI client\nclient = OpenAI(api_key=os.environ.get(\"OPENAI_API_KEY\"))\n\n# Pydantic models for structured output\n# These models represent the key components of the LoT approach:\n# logical propositions, expressions, and the final output structure\nclass LogicalProposition(BaseModel):\n    symbol: str\n    description: str\n\nclass LogicalExpression(BaseModel):\n    expression: str\n    description: str\n\nclass LogicOfThoughtOutput(BaseModel):\n    propositions: List[LogicalProposition] = Field(..., description=\"List of logical propositions\")\n    expressions: List[LogicalExpression] = Field(..., description=\"List of logical expressions\")\n    extended_expressions: List[LogicalExpression] = Field(..., description=\"List of extended logical expressions\")\n    translated_description: str = Field(..., description=\"Natural language description of the logical reasoning\")\n    solution: str = Field(..., description=\"Solution to the puzzle\")\n\ndef logic_extraction(context: str) -> Dict[str, Any]:\n    \"\"\"\n    Implements the Logic Extraction phase of LoT.\n    This function extracts logical propositions and expressions from the input context.\n    \n    Why: This step is crucial for identifying the key logical components of the problem,\n    which will be used for further reasoning.\n    \"\"\"\n    prompt = f\"\"\"Extract logical propositions and expressions from the following context:\n\n{context}\n\nProvide the output as a JSON object with 'propositions' and 'expressions' keys.\nEach proposition should be an object with 'symbol' and 'description' keys.\nEach expression should be an object with 'expression' and 'description' keys.\nFocus on extracting key relationships and constraints from the puzzle.\n\"\"\"\n    \n    response = client.chat.completions.create(\n        model=\"gpt-4o-mini\",\n        messages=[\n            {\"role\": \"system\", \"content\": \"You are an expert in logical reasoning and propositional logic.\"},\n            {\"role\": \"user\", \"content\": prompt}\n        ],\n        response_format={\"type\": \"json_object\"}\n    )\n    \n    return json.loads(response.choices[0].message.content)\n\ndef logic_extension(expressions: List[LogicalExpression]) -> List[LogicalExpression]:\n    \"\"\"\n    Implements the Logic Extension phase of LoT.\n    This function expands the logical expressions using logical reasoning laws.\n    \n    Why: This step is essential for deriving new relationships and constraints\n    that may not be explicitly stated in the original problem, but are logically implied.\n    \"\"\"\n    prompt = f\"\"\"Extend the following logical expressions using logical reasoning laws:\n\n{json.dumps([expr.model_dump() for expr in expressions])}\n\nProvide the output as a JSON array of extended expressions with \"extended_expressions\" root key.\nEach expression should be an object with 'expression' and 'description' keys.\nFocus on deriving new relationships and constraints that can help solve the puzzle.\n\"\"\"\n    \n    response = client.chat.completions.create(\n        model=\"gpt-4o-mini\",\n        messages=[\n            {\"role\": \"system\", \"content\": \"You are an expert in logical reasoning and propositional logic.\"},\n            {\"role\": \"user\", \"content\": prompt}\n        ],\n        response_format={\"type\": \"json_object\"}\n    )\n    \n    result = json.loads(response.choices[0].message.content)\n    return [LogicalExpression(**expr) for expr in result.get('extended_expressions', [])]\n\ndef logic_translation(extended_expressions: List[LogicalExpression]) -> str:\n    \"\"\"\n    Implements the Logic Translation phase of LoT.\n    This function translates the extended logical expressions back into natural language.\n    \n    Why: This step is crucial for making the logical reasoning process understandable\n    and interpretable, bridging the gap between formal logic and natural language understanding.\n    \"\"\"\n    prompt = f\"\"\"Translate the following extended logical expressions into a natural language description:\n\n{json.dumps([expr.model_dump() for expr in extended_expressions])}\n\nProvide the output as a single string that explains the logical reasoning process.\n\"\"\"\n    \n    response = client.chat.completions.create(\n        model=\"gpt-4o-mini\",\n        messages=[\n            {\"role\": \"system\", \"content\": \"You are an expert in logical reasoning and propositional logic.\"},\n            {\"role\": \"user\", \"content\": prompt}\n        ]\n    )\n    print(response)\n    \n    return response.choices[0].message.content.strip()\n\ndef solve_puzzle(context: str, translated_description: str) -> str:\n    \"\"\"\n    Uses the original context and the translated logical reasoning to solve the puzzle.\n    \n    Why: This step combines the original problem statement with the derived logical insights\n    to arrive at a solution, demonstrating the power of the LoT approach in solving complex\n    logical reasoning tasks.\n    \"\"\"\n    prompt = f\"\"\"Using the following context and logical reasoning:\n\nContext:\n{context}\n\nLogical Reasoning:\n{translated_description}\n\nSolve the puzzle: Who will give a theatre ticket and who will buy roses?\nProvide a step-by-step explanation of your reasoning, and then state the final answer.\n\"\"\"\n    \n    response = client.chat.completions.create(\n        model=\"gpt-4o-mini\",\n        messages=[\n            {\"role\": \"system\", \"content\": \"You are an expert puzzle solver using logical reasoning.\"},\n            {\"role\": \"user\", \"content\": prompt}\n        ]\n    )\n    \n    return response.choices[0].message.content.strip()\n\ndef run_logic_of_thought(context: str) -> LogicOfThoughtOutput:\n    \"\"\"\n    Orchestrates the entire Logic-of-Thought process.\n    \n    This function ties together all the phases of LoT:\n    1. Logic Extraction\n    2. Logic Extension\n    3. Logic Translation\n    4. Puzzle Solving\n    \n    Why: This orchestration demonstrates how the LoT approach\n    systematically builds up logical understanding to solve complex problems.\n    \"\"\"\n    # Logic Extraction\n    extraction_result = logic_extraction(context)\n    propositions = [LogicalProposition(**prop) for prop in extraction_result.get('propositions', [])]\n    expressions = [LogicalExpression(**expr) for expr in extraction_result.get('expressions', [])]\n    \n    # Logic Extension\n    extended_expressions = logic_extension(expressions)\n    \n    # Logic Translation\n    translated_description = logic_translation(extended_expressions)\n    \n    # Solve Puzzle\n    solution = solve_puzzle(context, translated_description)\n    \n    return LogicOfThoughtOutput(\n        propositions=propositions,\n        expressions=expressions,\n        extended_expressions=extended_expressions,\n        translated_description=translated_description,\n        solution=solution\n    )\n\n# Example puzzle (simplified version of Einstein's Riddle)\neinsteins_riddle = \"\"\"\nThe Simpsons are preparing a concert show with tricks, a guitar song, and one family member's own poem.\nA person who wrote the poem will give a bread machine as a present and buy irises.\nMummy will buy tulips.\nMelanie has learned to bake cinnamon buns and remembered guitar chords for Granny's birthday.\nThe trickster has prepared a notebook for recipes and a fruit salad.\nMelanie knows that Granny likes daisies.\nA person who will give a rocking chair will also prepare homemade candies for Granny.\nBill has a special deck of cards and a box with a double bottom.\nMummy and Melanie have had rehearsals for two for a week.\nDaddy will prepare orange juice.\nGranny will also be given a bouquet of roses and a ticket to the theatre play.\n\nWho will give a theatre ticket and who will buy roses?\n\"\"\"\n\ndef main():\n    print(\"Solving Einstein's Riddle using Logic-of-Thought approach:\")\n    print(\"source credit: https://edcraft.io/blog/all-articles/5-zebra-puzzles-for-kids\")\n    print(einsteins_riddle)\n    print(\"\\nApplying Logic-of-Thought...\")\n    \n    try:\n        result = run_logic_of_thought(einsteins_riddle)\n        \n        print(\"\\nLogic-of-Thought Output:\")\n        print(f\"Propositions: {result.propositions}\")\n        print(f\"Expressions: {result.expressions}\")\n        print(f\"Extended Expressions: {result.extended_expressions}\")\n        print(f\"\\nLogical Reasoning Process:\\n{result.translated_description}\")\n        print(f\"\\nSolution:\\n{result.solution}\")\n    except Exception as e:\n        print(f\"An error occurred: {str(e)}\")\n\nif __name__ == \"__main__\":\n    main()\n\n\"\"\"\nCore Concepts and Potential Improvements:\n\n1. Logic-of-Thought (LoT) Approach:\n   - Extracts logical propositions and expressions from natural language.\n   - Extends logical expressions using reasoning laws.\n   - Translates logical reasoning back into natural language.\n   - Combines original context with derived logical insights to solve problems.\n\n2. Use of Large Language Models (LLMs):\n   - Leverages LLMs for each phase of the LoT process.\n   - Demonstrates the power of LLMs in understanding and manipulating logical structures.\n\n3. Structured Output:\n   - Uses Pydantic models to ensure consistent and typed output structure.\n\nPotential Improvements:\n1. Implement more diverse logical connectives and reasoning laws.\n2. Add error handling and validation for logical expressions.\n3. Implement visualization of the logical reasoning process.\n4. Optimize API calls to reduce token usage and improve efficiency.\n5. Implement caching mechanisms for repeated logical structures.\n6. Extend to handle more complex logical puzzles and real-world reasoning tasks.\n7. Integrate with other AI techniques like knowledge graphs or automated theorem provers.\n\"\"\"\n```",
  "publishedTime": "2024-09-30T23:09:42+00:00",
  "usage": {
    "tokens": 3089
  }
}
```
