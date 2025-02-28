---
title: Phind/Phind-CodeLlama-34B-v1 · Hugging Face
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
url: https://huggingface.co/Phind/Phind-CodeLlama-34B-v1
timestamp: 2025-01-20T15:43:35.517Z
domain: huggingface.co
path: Phind_Phind-CodeLlama-34B-v1
---

# Phind/Phind-CodeLlama-34B-v1 · Hugging Face


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


## Content

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#note-weve-now-launched-phind-codellama-34b-v2-which-acheives-738-pass1-on-humaneval-it-is-instruction-tuned-and-much-easier-to-use-than-this-v1-model)NOTE: We've now launched **Phind-CodeLlama-34B-v2**, which acheives **73.8% pass@1** on HumanEval. It is instruction-tuned and much easier to use than this v1 model.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#check-out-phind-codellama-34b-v2-here)Check out Phind-CodeLlama-34B-v2 [here](https://huggingface.co/Phind/Phind-CodeLlama-34B-v2).
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We've fine-tuned CodeLlama-34B and CodeLlama-34B-Python on an internal Phind dataset that achieve 67.6% and 69.5% pass@1 on HumanEval, respectively. GPT-4 achieves 67%. We've applied OpenAI's decontamination methodology to our dataset to ensure result validity.

More details can be found on our [blog post](https://www.phind.com/blog/code-llama-beats-gpt4).

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#model-details)Model Details
----------------------------------------------------------------------------------

This model is fine-tuned from CodeLlama-34B and achieves 67.6% pass@1 on HumanEval.

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#dataset-details)Dataset Details
--------------------------------------------------------------------------------------

We fined-tuned on a proprietary dataset of ~80k high quality programming problems and solutions. This dataset consists of instruction-answer pairs instead of code completion examples, making it structurally different from HumanEval. The Phind models were trained for 2 epochs, for a total of ~160k examples shown. LoRA was not used -- both models are a native finetune. We used DeepSpeed ZeRO 3 and Flash Attention 2 to train these models in three hours on 32 A100-80GB GPUs. We used a sequence length of 4096 tokens.

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#how-to-get-started-with-the-model)How to Get Started with the Model
--------------------------------------------------------------------------------------------------------------------------

Make sure to install Transformers from the main git branch:

```
pip install git+https://github.com/huggingface/transformers.git
```

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#how-to-prompt-the-model)How to Prompt the Model
------------------------------------------------------------------------------------------------------

**Please note that this model is somewhat instruction-tuned, but not chat-tuned.**

Do not try to use the Llama chat markup with this model. Instead, simply tell it what you want and add "\\n: " at the end of your task.

For example:

```
Write me a linked list implementation: \n
```

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#how-to-reproduce-humaneval-results)How to reproduce HumanEval Results
----------------------------------------------------------------------------------------------------------------------------

To reproduce our results:

```

from transformers import AutoTokenizer, LlamaForCausalLM
from human_eval.data import write_jsonl, read_problems
from tqdm import tqdm

# initialize the model

model_path = "Phind/Phind-CodeLlama-34B-v1"
model = LlamaForCausalLM.from_pretrained(model_path, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_path)

# HumanEval helper

def generate_one_completion(prompt: str):
    tokenizer.pad_token = tokenizer.eos_token
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096)

    # Generate
    generate_ids = model.generate(inputs.input_ids.to("cuda"), max_new_tokens=256, do_sample=True, top_p=0.75, top_k=40, temperature=0.1)
    completion = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    completion = completion.replace(prompt, "").split("\n\n\n")[0]

    return completion

# perform HumanEval
problems = read_problems()

num_samples_per_task = 1
samples = [
    dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
    for task_id in tqdm(problems)
    for _ in range(num_samples_per_task)
]
write_jsonl("samples.jsonl", samples)

# run `evaluate_functional_correctness samples.jsonl` in your HumanEval code sandbox
```

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#bias-risks-and-limitations)Bias, Risks, and Limitations
--------------------------------------------------------------------------------------------------------------

This model has undergone very limited testing. Additional safety testing should be performed before any real-world deployments.

[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#training-details)Training details
----------------------------------------------------------------------------------------

*   **Hardware Type:** 32x A100-80GB
*   **Hours used:** 90 GPU-hours
*   **Cloud Provider:** AWS
*   **Compute Region:** us-east-1

## Metadata

```json
{
  "title": "Phind/Phind-CodeLlama-34B-v1 · Hugging Face",
  "description": "We’re on a journey to advance and democratize artificial intelligence through open source and open science.",
  "url": "https://huggingface.co/Phind/Phind-CodeLlama-34B-v1",
  "content": "[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#note-weve-now-launched-phind-codellama-34b-v2-which-acheives-738-pass1-on-humaneval-it-is-instruction-tuned-and-much-easier-to-use-than-this-v1-model)NOTE: We've now launched **Phind-CodeLlama-34B-v2**, which acheives **73.8% pass@1** on HumanEval. It is instruction-tuned and much easier to use than this v1 model.\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#check-out-phind-codellama-34b-v2-here)Check out Phind-CodeLlama-34B-v2 [here](https://huggingface.co/Phind/Phind-CodeLlama-34B-v2).\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nWe've fine-tuned CodeLlama-34B and CodeLlama-34B-Python on an internal Phind dataset that achieve 67.6% and 69.5% pass@1 on HumanEval, respectively. GPT-4 achieves 67%. We've applied OpenAI's decontamination methodology to our dataset to ensure result validity.\n\nMore details can be found on our [blog post](https://www.phind.com/blog/code-llama-beats-gpt4).\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#model-details)Model Details\n----------------------------------------------------------------------------------\n\nThis model is fine-tuned from CodeLlama-34B and achieves 67.6% pass@1 on HumanEval.\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#dataset-details)Dataset Details\n--------------------------------------------------------------------------------------\n\nWe fined-tuned on a proprietary dataset of ~80k high quality programming problems and solutions. This dataset consists of instruction-answer pairs instead of code completion examples, making it structurally different from HumanEval. The Phind models were trained for 2 epochs, for a total of ~160k examples shown. LoRA was not used -- both models are a native finetune. We used DeepSpeed ZeRO 3 and Flash Attention 2 to train these models in three hours on 32 A100-80GB GPUs. We used a sequence length of 4096 tokens.\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#how-to-get-started-with-the-model)How to Get Started with the Model\n--------------------------------------------------------------------------------------------------------------------------\n\nMake sure to install Transformers from the main git branch:\n\n```\npip install git+https://github.com/huggingface/transformers.git\n```\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#how-to-prompt-the-model)How to Prompt the Model\n------------------------------------------------------------------------------------------------------\n\n**Please note that this model is somewhat instruction-tuned, but not chat-tuned.**\n\nDo not try to use the Llama chat markup with this model. Instead, simply tell it what you want and add \"\\\\n: \" at the end of your task.\n\nFor example:\n\n```\nWrite me a linked list implementation: \\n\n```\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#how-to-reproduce-humaneval-results)How to reproduce HumanEval Results\n----------------------------------------------------------------------------------------------------------------------------\n\nTo reproduce our results:\n\n```\n\nfrom transformers import AutoTokenizer, LlamaForCausalLM\nfrom human_eval.data import write_jsonl, read_problems\nfrom tqdm import tqdm\n\n# initialize the model\n\nmodel_path = \"Phind/Phind-CodeLlama-34B-v1\"\nmodel = LlamaForCausalLM.from_pretrained(model_path, device_map=\"auto\")\ntokenizer = AutoTokenizer.from_pretrained(model_path)\n\n# HumanEval helper\n\ndef generate_one_completion(prompt: str):\n    tokenizer.pad_token = tokenizer.eos_token\n    inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=4096)\n\n    # Generate\n    generate_ids = model.generate(inputs.input_ids.to(\"cuda\"), max_new_tokens=256, do_sample=True, top_p=0.75, top_k=40, temperature=0.1)\n    completion = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]\n    completion = completion.replace(prompt, \"\").split(\"\\n\\n\\n\")[0]\n\n    return completion\n\n# perform HumanEval\nproblems = read_problems()\n\nnum_samples_per_task = 1\nsamples = [\n    dict(task_id=task_id, completion=generate_one_completion(problems[task_id][\"prompt\"]))\n    for task_id in tqdm(problems)\n    for _ in range(num_samples_per_task)\n]\nwrite_jsonl(\"samples.jsonl\", samples)\n\n# run `evaluate_functional_correctness samples.jsonl` in your HumanEval code sandbox\n```\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#bias-risks-and-limitations)Bias, Risks, and Limitations\n--------------------------------------------------------------------------------------------------------------\n\nThis model has undergone very limited testing. Additional safety testing should be performed before any real-world deployments.\n\n[](https://huggingface.co/Phind/Phind-CodeLlama-34B-v1#training-details)Training details\n----------------------------------------------------------------------------------------\n\n*   **Hardware Type:** 32x A100-80GB\n*   **Hours used:** 90 GPU-hours\n*   **Cloud Provider:** AWS\n*   **Compute Region:** us-east-1",
  "usage": {
    "tokens": 1203
  }
}
```
