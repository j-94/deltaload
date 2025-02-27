---
title: microsoft/phi-1_5 · Hugging Face
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
url: https://huggingface.co/microsoft/phi-1_5
timestamp: 2025-01-20T15:43:51.670Z
domain: huggingface.co
path: microsoft_phi-1_5
---

# microsoft/phi-1_5 · Hugging Face


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


## Content

[](https://huggingface.co/microsoft/phi-1_5#model-summary)Model Summary
-----------------------------------------------------------------------

The language model Phi-1.5 is a Transformer with **1.3 billion** parameters. It was trained using the same data sources as [phi-1](https://huggingface.co/microsoft/phi-1), augmented with a new data source that consists of various NLP synthetic texts. When assessed against benchmarks testing common sense, language understanding, and logical reasoning, Phi-1.5 demonstrates a nearly state-of-the-art performance among models with less than 10 billion parameters.

We **did not** fine-tune Phi-1.5 either for **instruction following or through reinforcement learning from human feedback**. The intention behind crafting this open-source model is to provide the research community with a non-restricted small model to explore vital safety challenges, such as reducing toxicity, understanding societal biases, enhancing controllability, and more.

For a safer model release, we exclude generic web-crawl data sources such as common-crawl from the training. This strategy prevents direct exposure to potentially harmful online content, enhancing the model's safety without RLHF. However, the model is still vulnerable to generating harmful content. We hope the model can help the research community to further study the safety of language models.

Phi-1.5 can write poems, draft emails, create stories, summarize texts, write Python code (such as downloading a Hugging Face transformer model), etc.

[](https://huggingface.co/microsoft/phi-1_5#how-to-use)How to Use
-----------------------------------------------------------------

Phi-1.5 has been integrated in the `transformers` version 4.37.0, please ensure that you are using a version equal or higher than it.

[](https://huggingface.co/microsoft/phi-1_5#intended-uses)Intended Uses
-----------------------------------------------------------------------

Given the nature of the training data, Phi-1.5 is best suited for prompts using the QA format, the chat format, and the code format. Note that Phi-1.5, being a base model, often produces irrelevant text following the main answer. In the following example, we've truncated the answer for illustrative purposes only.

### [](https://huggingface.co/microsoft/phi-1_5#qa-format)QA Format:

```
Write a detailed analogy between mathematics and a lighthouse.

Answer: Mathematics is like a lighthouse, guiding us through the vast ocean of numbers and calculations. Just as a lighthouse illuminates the darkness, mathematics provides us with a clear path to navigate through complex problems. It helps us make sense of the world around us, just like a lighthouse helps ships find their way home.
```

where the model generates the text after "Answer:".

### [](https://huggingface.co/microsoft/phi-1_5#chat-format)Chat Format:

```
Alice: I don't know why, I'm struggling to maintain focus while studying. Any suggestions?

Bob: Have you tried using a timer? It can help you stay on track and avoid distractions.

Alice: That's a good idea. I'll give it a try.

Charlie: Another thing that can help is to break up your study sessions into smaller chunks. It's easier to concentrate on one thing at a time.

Alice: That makes sense. I'll try that too.

Bob: And don't forget to take breaks! It's important to give your brain a rest so you can come back to your studies with a fresh perspective.

Alice: Thanks for the advice, guys. I feel more motivated now.

Charlie: No problem, Alice. We're all in this together.

Bob: Yeah, and remember that it's okay to ask for help if you need it. We're here to support each other.
```

where the model generates the text after the first "Bob:".

### [](https://huggingface.co/microsoft/phi-1_5#code-format)Code Format:

```
def print_prime(n):
   """
   Print all primes between 1 and n
   """
   primes = []
   for num in range(2, n+1):
       is_prime = True
       for i in range(2, int(math.sqrt(num))+1):
           if num % i == 0:
               is_prime = False
               break
       if is_prime:
           primes.append(num)
   print(primes)
```

where the model generates the text after the comments.

**Notes:**

*   Phi-1.5-generated text/code should be treated as a starting point rather than a definitive solution for potential use cases. Users should be cautious when employing these models in their applications.
    
*   Phi-1.5 has not been tested to ensure that it performs adequately for any production-level application. Please refer to the limitation sections of this document for more details.
    

[](https://huggingface.co/microsoft/phi-1_5#sample-code)Sample Code
-------------------------------------------------------------------

```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.set_default_device("cuda")

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5")

inputs = tokenizer('''def print_prime(n):
   """
   Print all primes between 1 and n
   """''', return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
print(text)
```

[](https://huggingface.co/microsoft/phi-1_5#limitations-of-phi-15)Limitations of Phi-1.5
----------------------------------------------------------------------------------------

*   Generate Inaccurate Code and Facts: The model often produces incorrect code snippets and statements. Users should treat these outputs as suggestions or starting points, not as definitive or accurate solutions.
    
*   Limited Scope for code: If the model generates Python scripts that utilize uncommon packages or scripts in other languages, we strongly recommend users manually verify all API uses.
    
*   Unreliable Responses to Instruction: The model has not undergone instruction fine-tuning. As a result, it may struggle or fail to adhere to intricate or nuanced instructions provided by users.
    
*   Language Limitations: The model is primarily designed to understand standard English. Informal English, slang, or any other language outside of English might pose challenges to its comprehension, leading to potential misinterpretations or errors in response.
    
*   Potential Societal Biases: Regardless of the safe data used for its training, the model is not entirely free from societal biases. There's a possibility it may generate content that mirrors these societal biases, particularly if prompted or instructed to do so. We urge users to be aware of this and to exercise caution and critical thinking when interpreting model outputs.
    
*   Toxicity: Despite that the model is trained with carefully selected data, the model can still produce harmful content if explicitly prompted or instructed to do so. We chose to release the model for research purposes only -- We hope to help the open-source community develop the most effective ways to reduce the toxicity of a model directly after pretraining.
    

[](https://huggingface.co/microsoft/phi-1_5#training)Training
-------------------------------------------------------------

### [](https://huggingface.co/microsoft/phi-1_5#model)Model

*   Architecture: a Transformer-based model with next-word prediction objective
*   Dataset size: 30B tokens
*   Training tokens: 150B tokens
*   Precision: fp16
*   GPUs: 32xA100-40G
*   Training time: 8 days

### [](https://huggingface.co/microsoft/phi-1_5#software)Software

*   [PyTorch](https://github.com/pytorch/pytorch)
*   [DeepSpeed](https://github.com/microsoft/DeepSpeed)
*   [Flash-Attention](https://github.com/HazyResearch/flash-attention)

### [](https://huggingface.co/microsoft/phi-1_5#license)License

The model is licensed under the [MIT license](https://huggingface.co/microsoft/phi-1_5/resolve/main/LICENSE).

### [](https://huggingface.co/microsoft/phi-1_5#citation)Citation

You can find the paper at [https://arxiv.org/abs/2309.05463](https://arxiv.org/abs/2309.05463). Please cite as:

```
@article{textbooks2,
  title={Textbooks Are All You Need II: \textbf{phi-1.5} technical report},
  author={Li, Yuanzhi and Bubeck, S{\'e}bastien and Eldan, Ronen and Del Giorno, Allie and Gunasekar, Suriya and Lee, Yin Tat},
  journal={arXiv preprint arXiv:2309.05463},
  year={2023}
}
```

[](https://huggingface.co/microsoft/phi-1_5#trademarks)Trademarks
-----------------------------------------------------------------

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.

## Metadata

```json
{
  "title": "microsoft/phi-1_5 · Hugging Face",
  "description": "We’re on a journey to advance and democratize artificial intelligence through open source and open science.",
  "url": "https://huggingface.co/microsoft/phi-1_5",
  "content": "[](https://huggingface.co/microsoft/phi-1_5#model-summary)Model Summary\n-----------------------------------------------------------------------\n\nThe language model Phi-1.5 is a Transformer with **1.3 billion** parameters. It was trained using the same data sources as [phi-1](https://huggingface.co/microsoft/phi-1), augmented with a new data source that consists of various NLP synthetic texts. When assessed against benchmarks testing common sense, language understanding, and logical reasoning, Phi-1.5 demonstrates a nearly state-of-the-art performance among models with less than 10 billion parameters.\n\nWe **did not** fine-tune Phi-1.5 either for **instruction following or through reinforcement learning from human feedback**. The intention behind crafting this open-source model is to provide the research community with a non-restricted small model to explore vital safety challenges, such as reducing toxicity, understanding societal biases, enhancing controllability, and more.\n\nFor a safer model release, we exclude generic web-crawl data sources such as common-crawl from the training. This strategy prevents direct exposure to potentially harmful online content, enhancing the model's safety without RLHF. However, the model is still vulnerable to generating harmful content. We hope the model can help the research community to further study the safety of language models.\n\nPhi-1.5 can write poems, draft emails, create stories, summarize texts, write Python code (such as downloading a Hugging Face transformer model), etc.\n\n[](https://huggingface.co/microsoft/phi-1_5#how-to-use)How to Use\n-----------------------------------------------------------------\n\nPhi-1.5 has been integrated in the `transformers` version 4.37.0, please ensure that you are using a version equal or higher than it.\n\n[](https://huggingface.co/microsoft/phi-1_5#intended-uses)Intended Uses\n-----------------------------------------------------------------------\n\nGiven the nature of the training data, Phi-1.5 is best suited for prompts using the QA format, the chat format, and the code format. Note that Phi-1.5, being a base model, often produces irrelevant text following the main answer. In the following example, we've truncated the answer for illustrative purposes only.\n\n### [](https://huggingface.co/microsoft/phi-1_5#qa-format)QA Format:\n\n```\nWrite a detailed analogy between mathematics and a lighthouse.\n\nAnswer: Mathematics is like a lighthouse, guiding us through the vast ocean of numbers and calculations. Just as a lighthouse illuminates the darkness, mathematics provides us with a clear path to navigate through complex problems. It helps us make sense of the world around us, just like a lighthouse helps ships find their way home.\n```\n\nwhere the model generates the text after \"Answer:\".\n\n### [](https://huggingface.co/microsoft/phi-1_5#chat-format)Chat Format:\n\n```\nAlice: I don't know why, I'm struggling to maintain focus while studying. Any suggestions?\n\nBob: Have you tried using a timer? It can help you stay on track and avoid distractions.\n\nAlice: That's a good idea. I'll give it a try.\n\nCharlie: Another thing that can help is to break up your study sessions into smaller chunks. It's easier to concentrate on one thing at a time.\n\nAlice: That makes sense. I'll try that too.\n\nBob: And don't forget to take breaks! It's important to give your brain a rest so you can come back to your studies with a fresh perspective.\n\nAlice: Thanks for the advice, guys. I feel more motivated now.\n\nCharlie: No problem, Alice. We're all in this together.\n\nBob: Yeah, and remember that it's okay to ask for help if you need it. We're here to support each other.\n```\n\nwhere the model generates the text after the first \"Bob:\".\n\n### [](https://huggingface.co/microsoft/phi-1_5#code-format)Code Format:\n\n```\ndef print_prime(n):\n   \"\"\"\n   Print all primes between 1 and n\n   \"\"\"\n   primes = []\n   for num in range(2, n+1):\n       is_prime = True\n       for i in range(2, int(math.sqrt(num))+1):\n           if num % i == 0:\n               is_prime = False\n               break\n       if is_prime:\n           primes.append(num)\n   print(primes)\n```\n\nwhere the model generates the text after the comments.\n\n**Notes:**\n\n*   Phi-1.5-generated text/code should be treated as a starting point rather than a definitive solution for potential use cases. Users should be cautious when employing these models in their applications.\n    \n*   Phi-1.5 has not been tested to ensure that it performs adequately for any production-level application. Please refer to the limitation sections of this document for more details.\n    \n\n[](https://huggingface.co/microsoft/phi-1_5#sample-code)Sample Code\n-------------------------------------------------------------------\n\n```\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ntorch.set_default_device(\"cuda\")\n\nmodel = AutoModelForCausalLM.from_pretrained(\"microsoft/phi-1_5\", torch_dtype=\"auto\")\ntokenizer = AutoTokenizer.from_pretrained(\"microsoft/phi-1_5\")\n\ninputs = tokenizer('''def print_prime(n):\n   \"\"\"\n   Print all primes between 1 and n\n   \"\"\"''', return_tensors=\"pt\", return_attention_mask=False)\n\noutputs = model.generate(**inputs, max_length=200)\ntext = tokenizer.batch_decode(outputs)[0]\nprint(text)\n```\n\n[](https://huggingface.co/microsoft/phi-1_5#limitations-of-phi-15)Limitations of Phi-1.5\n----------------------------------------------------------------------------------------\n\n*   Generate Inaccurate Code and Facts: The model often produces incorrect code snippets and statements. Users should treat these outputs as suggestions or starting points, not as definitive or accurate solutions.\n    \n*   Limited Scope for code: If the model generates Python scripts that utilize uncommon packages or scripts in other languages, we strongly recommend users manually verify all API uses.\n    \n*   Unreliable Responses to Instruction: The model has not undergone instruction fine-tuning. As a result, it may struggle or fail to adhere to intricate or nuanced instructions provided by users.\n    \n*   Language Limitations: The model is primarily designed to understand standard English. Informal English, slang, or any other language outside of English might pose challenges to its comprehension, leading to potential misinterpretations or errors in response.\n    \n*   Potential Societal Biases: Regardless of the safe data used for its training, the model is not entirely free from societal biases. There's a possibility it may generate content that mirrors these societal biases, particularly if prompted or instructed to do so. We urge users to be aware of this and to exercise caution and critical thinking when interpreting model outputs.\n    \n*   Toxicity: Despite that the model is trained with carefully selected data, the model can still produce harmful content if explicitly prompted or instructed to do so. We chose to release the model for research purposes only -- We hope to help the open-source community develop the most effective ways to reduce the toxicity of a model directly after pretraining.\n    \n\n[](https://huggingface.co/microsoft/phi-1_5#training)Training\n-------------------------------------------------------------\n\n### [](https://huggingface.co/microsoft/phi-1_5#model)Model\n\n*   Architecture: a Transformer-based model with next-word prediction objective\n*   Dataset size: 30B tokens\n*   Training tokens: 150B tokens\n*   Precision: fp16\n*   GPUs: 32xA100-40G\n*   Training time: 8 days\n\n### [](https://huggingface.co/microsoft/phi-1_5#software)Software\n\n*   [PyTorch](https://github.com/pytorch/pytorch)\n*   [DeepSpeed](https://github.com/microsoft/DeepSpeed)\n*   [Flash-Attention](https://github.com/HazyResearch/flash-attention)\n\n### [](https://huggingface.co/microsoft/phi-1_5#license)License\n\nThe model is licensed under the [MIT license](https://huggingface.co/microsoft/phi-1_5/resolve/main/LICENSE).\n\n### [](https://huggingface.co/microsoft/phi-1_5#citation)Citation\n\nYou can find the paper at [https://arxiv.org/abs/2309.05463](https://arxiv.org/abs/2309.05463). Please cite as:\n\n```\n@article{textbooks2,\n  title={Textbooks Are All You Need II: \\textbf{phi-1.5} technical report},\n  author={Li, Yuanzhi and Bubeck, S{\\'e}bastien and Eldan, Ronen and Del Giorno, Allie and Gunasekar, Suriya and Lee, Yin Tat},\n  journal={arXiv preprint arXiv:2309.05463},\n  year={2023}\n}\n```\n\n[](https://huggingface.co/microsoft/phi-1_5#trademarks)Trademarks\n-----------------------------------------------------------------\n\nThis project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.",
  "usage": {
    "tokens": 2009
  }
}
```
