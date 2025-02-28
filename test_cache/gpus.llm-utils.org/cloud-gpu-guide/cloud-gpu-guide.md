---
title: Cloud GPU Guide
description: Firstly, which AI tools are worth running?
url: https://gpus.llm-utils.org/cloud-gpu-guide/
timestamp: 2025-01-20T15:45:30.758Z
domain: gpus.llm-utils.org
path: cloud-gpu-guide
---

# Cloud GPU Guide


Firstly, which AI tools are worth running?


## Content

July 2023·Updated: September 2023

Three good places to start are:

*   Run llama 2 70b
*   Run stable diffusion on your own GPU (locally, or on a rented GPU)
*   Run whisper on your own GPU (locally, or on a rented GPU)

So, which GPUs should I be using? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#so-which-gpus-should-i-be-using)
------------------------------------------------------------------------------------------------------------------

If you’re using cloud GPUs:

*   If you want to run llama 2 70b
    *   1x A100 80GB and use [https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ](https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ) with [https://github.com/TheBlokeAI/dockerLLM/tree/main](https://github.com/TheBlokeAI/dockerLLM/tree/main)
*   If you want to run stable diffusion
    *   1x 4090 if you want a balance of price and performance, or 1x 3090 if you want a lower price (it can run on cheaper GPUs too, and you could use 1x H100 if you wanted to go savage with it)
*   If you want to run whisper
    *   Same recommendations as stable diffusion. Though whisper-large can run on cards with lower vram, most of the clouds don’t have those cards, and the 4090 or 3090 will work well. And you can run it on a CPU, too.
*   If you want to fine-tune a large LLM
    *   An H100 cluster or A100 cluster
*   If you want to train a large LLM
    *   A large H100 cluster

[More info here.](https://gpus.llm-utils.org/recommended-gpus-and-gpu-clouds-for-ai/)

If you’re using a local GPU:

*   Same as above, but you probably won’t be able to train or fine tune an LLM!
*   Most of the open LLMs have versions available that can run on lower VRAM cards e.g. a GGML version of Llama 2 7b will run on most CPUs, even.
*   Thanks Bruce for prompting me to add this section

Should I run these models locally or with a cloud GPU? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#should-i-run-these-models-locally-or-with-a-cloud-gpu)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Both are reasonable choices!
*   For running models locally, see [this wiki](https://www.reddit.com/r/LocalLLaMA/wiki/index/).
    *   You can run quite a few things even on surprisingly weak hardware.
    *   If you have powerful local hardware, this is a fun option to play around with
*   For running models in the cloud, Runpod’s [templates](https://www.runpod.io/console/templates) are the quickest start
*   The easiest option is of course using a hosted instance, like DreamStudio, RunDiffusion, or Playground AI for stable diffusion, ChatGPT for an LLM, [this](https://api.llm-utils.org/) for Falcon-40B (currently offline) and Falcon-40B-Uncensored, [this](https://huggingface.co/spaces/HuggingFaceH4/falcon-chat) for Falcon-40B-Instruct, OpenAI’s API for Whisper, and so on

In short, if you want to run them locally, run them locally, if you want to run them in the cloud, run them in the cloud. It’s your preference based on what GPU you have, how much time you want to spend, how much money you want to spend, and what seems more fun to you.

Which GPU cloud should I use? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#which-gpu-cloud-should-i-use)
-----------------------------------------------------------------------------------------------------------

*   If you need a huge number of A100s/H100s - talk to Oracle, FluidStack, Lambda Labs, maybe [a few others](https://gpus.llm-utils.org/accessing-large-h100-clusters/). Capacity is very low though for large quantities, especially of H100s, based on a couple of cloud founders/execs I’ve talked with.
*   If you need a couple A100s or H100s: Runpod, perhaps Tensordock or Latitude.
*   If you need 1x H100: Runpod (Fluidstack and Lambda have been out of on-demand capacity for qhite a while).
*   If you need cheap 3090s, 4090s, or A6000s: Tensordock.
*   If you need Stable Diffusion inference only: Salad.
*   If you need a wide variety of GPUs: Runpod or Tensordock.
*   If you want to play around with templates / general hobbyist: Runpod.

The large clouds generally have worse pricing and more complicated setups than the above.

If you’re tied to one of the big clouds (AWS, Azure, GCP), then you don’t have a choice, so use that.

More info [here](https://gpus.llm-utils.org/fluidstack-vs-lambda-labs-vs-runpod-vs-tensordock/), [here](https://gpus.llm-utils.org/gpu-clouds-for-falcon-40b/), [here](https://gpus.llm-utils.org/h100-gpu-cloud-availability-and-pricing/), [here](https://gpus.llm-utils.org/alternative-gpu-clouds/), [here](https://gpus.llm-utils.org/gpu-cloud-user-experience-comparison/) and [here.](https://gpus.llm-utils.org/gpu-clouds-for-each-gpu/)

What’s the easiest GPU cloud to start with? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#whats-the-easiest-gpu-cloud-to-start-with)
--------------------------------------------------------------------------------------------------------------------------------------

Runpod and [their templates.](https://www.runpod.io/console/templates) Pick a template, pick a GPU, click custommize deployment and increase the temporary and persistent disk space to an appropriate size, click set overrides, click continue, click deploy, then click view logs, then once it’s done setup, either use the URL provided by the logs or click to connect to whatever you deployed.

Note that Runpod Pods are not full-featured VMs, they are docker containers on host machines.

How much VRAM and system ram do I need, and how many vCPUs? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#how-much-vram-and-system-ram-do-i-need-and-how-many-vcpus)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here are some basic and often-wrong rules of thumb:

*   VRAM (Video RAM / GPU RAM)
    *   Llama 2 70B GPTQ 4 bit 50-60GB
    *   Stable Diffusion 16GB+ preferred
    *   Whisper 12GB+ if using OpenAI version for optimal transcription speed, can be as low as running on a CPU if using a community version
*   System ram
    *   1-2x your amount of VRAM
*   vCPUs
    *   8-16 vCPUs should be more than sufficient for most non-large-scale GPU workloads
*   Disk space
    *   Very use case dependent. If you’re not sure, start with 100GB and see if that’s enough for your use case

More info [here](https://gpus.llm-utils.org/vram-and-vcpus/).

SXM or PCIe, and do I need NVLink? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#sxm-or-pcie-and-do-i-need-nvlink)
--------------------------------------------------------------------------------------------------------------------

If you’re not sure, then you should assume it doesn’t matter for your use case. More info [here](https://gpus.llm-utils.org/nvlink-sxm-and-pcie/).

What about InfiniBand? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-infiniband)
---------------------------------------------------------------------------------------------

If you’re renting one or two GPUs, it’s not relevant for you. If you’re doing a cluster of thousands, you’ll likely want InfiniBand.

What’s the difference between RTX 6000, A6000, and 6000 Ada? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#whats-the-difference-between-rtx-6000-a6000-and-6000-ada)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

3 different cards! It’s a confusing naming scheme.

*   RTX 6000 (Quadro RTX 6000, 24 GB VRAM, launched Aug 13, 2018)
*   RTX A6000 (48 GB VRAM, launched Oct 5, 2020)
*   RTX 6000 Ada (48 GB VRAM, launched Dec 3, 2022)

What about the difference between a DGX GH200, a GH200, and an H100? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-the-difference-between-a-dgx-gh200-a-gh200-and-an-h100)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Chart version [#](https://gpus.llm-utils.org/cloud-gpu-guide/#chart-version)

graph TB A(1x DGX GH200) subgraph GH200s \[256x GH200s\] B(Each GH200) subgraph H100Grace \[H100 GPU & Grace CPU\] C(1x H100) D(1x Grace CPU) end B -- "contains" --\> H100Grace end A -- "contains" --\> GH200s

### Text version [#](https://gpus.llm-utils.org/cloud-gpu-guide/#text-version)

*   1x DGX GH200
    *   Contains 256x GH200s (“Grace Hoppers”)
        *   Each GH200 contains 1x H100 and 1x Grace CPU

More info [here](https://gpus.llm-utils.org/dgx-gh200-vs-gh200-vs-h100/).

### What about DGX Cloud? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-dgx-cloud)

It’s Nvidia’s official cloud offering aimed at enterprises. You buy it through Nvidia but rent through an existing cloud like Oracle.

8 GPUs per instance, starting at $37k/month.

More info [here](https://gpus.llm-utils.org/dgx-cloud/).

Are H100s a big upgrade from A100s? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#are-h100s-a-big-upgrade-from-a100s)
-----------------------------------------------------------------------------------------------------------------------

Yes, the speedup is significant, and I’m told that with H100s can scale up performance to large numbers of GPUs better than A100s can.

So for training LLMs, H100s are the best bet.

What about AMD, Intel, Cerebras [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-amd-intel-cerebras)
--------------------------------------------------------------------------------------------------------------

For now, Nvidia is easier. We’ll put content about those other cards out soon. There’s other things that aren’t chips that are relevant to making Nvidia alternatives more workable too, and we’ll write about those.

AMD has some cards with 128GB and 192GB of HBM3 VRAM, which is cool. (MI300A and MI300X)

What next? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-next)
---------------------------------------------------------------------

If you’re ready to experiment, go set up a Runpod account, put a balance of $10, browse their templates, and deploy a template to a GPU instance. If you’re more experienced and don’t need templates, then consider starting with a different GPU cloud.

_Submit [feedback on this post](https://airtable.com/appUfDSBiDkn4qqVH/shr411VWRbl9og1xb) or [get early access and/or notifications of future posts](https://airtable.com/appUfDSBiDkn4qqVH/shr411VWRbl9og1xb)._

## Metadata

```json
{
  "title": "Cloud GPU Guide",
  "description": "Firstly, which AI tools are worth running?",
  "url": "https://gpus.llm-utils.org/cloud-gpu-guide/",
  "content": "July 2023·Updated: September 2023\n\nThree good places to start are:\n\n*   Run llama 2 70b\n*   Run stable diffusion on your own GPU (locally, or on a rented GPU)\n*   Run whisper on your own GPU (locally, or on a rented GPU)\n\nSo, which GPUs should I be using? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#so-which-gpus-should-i-be-using)\n------------------------------------------------------------------------------------------------------------------\n\nIf you’re using cloud GPUs:\n\n*   If you want to run llama 2 70b\n    *   1x A100 80GB and use [https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ](https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ) with [https://github.com/TheBlokeAI/dockerLLM/tree/main](https://github.com/TheBlokeAI/dockerLLM/tree/main)\n*   If you want to run stable diffusion\n    *   1x 4090 if you want a balance of price and performance, or 1x 3090 if you want a lower price (it can run on cheaper GPUs too, and you could use 1x H100 if you wanted to go savage with it)\n*   If you want to run whisper\n    *   Same recommendations as stable diffusion. Though whisper-large can run on cards with lower vram, most of the clouds don’t have those cards, and the 4090 or 3090 will work well. And you can run it on a CPU, too.\n*   If you want to fine-tune a large LLM\n    *   An H100 cluster or A100 cluster\n*   If you want to train a large LLM\n    *   A large H100 cluster\n\n[More info here.](https://gpus.llm-utils.org/recommended-gpus-and-gpu-clouds-for-ai/)\n\nIf you’re using a local GPU:\n\n*   Same as above, but you probably won’t be able to train or fine tune an LLM!\n*   Most of the open LLMs have versions available that can run on lower VRAM cards e.g. a GGML version of Llama 2 7b will run on most CPUs, even.\n*   Thanks Bruce for prompting me to add this section\n\nShould I run these models locally or with a cloud GPU? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#should-i-run-these-models-locally-or-with-a-cloud-gpu)\n-------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n*   Both are reasonable choices!\n*   For running models locally, see [this wiki](https://www.reddit.com/r/LocalLLaMA/wiki/index/).\n    *   You can run quite a few things even on surprisingly weak hardware.\n    *   If you have powerful local hardware, this is a fun option to play around with\n*   For running models in the cloud, Runpod’s [templates](https://www.runpod.io/console/templates) are the quickest start\n*   The easiest option is of course using a hosted instance, like DreamStudio, RunDiffusion, or Playground AI for stable diffusion, ChatGPT for an LLM, [this](https://api.llm-utils.org/) for Falcon-40B (currently offline) and Falcon-40B-Uncensored, [this](https://huggingface.co/spaces/HuggingFaceH4/falcon-chat) for Falcon-40B-Instruct, OpenAI’s API for Whisper, and so on\n\nIn short, if you want to run them locally, run them locally, if you want to run them in the cloud, run them in the cloud. It’s your preference based on what GPU you have, how much time you want to spend, how much money you want to spend, and what seems more fun to you.\n\nWhich GPU cloud should I use? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#which-gpu-cloud-should-i-use)\n-----------------------------------------------------------------------------------------------------------\n\n*   If you need a huge number of A100s/H100s - talk to Oracle, FluidStack, Lambda Labs, maybe [a few others](https://gpus.llm-utils.org/accessing-large-h100-clusters/). Capacity is very low though for large quantities, especially of H100s, based on a couple of cloud founders/execs I’ve talked with.\n*   If you need a couple A100s or H100s: Runpod, perhaps Tensordock or Latitude.\n*   If you need 1x H100: Runpod (Fluidstack and Lambda have been out of on-demand capacity for qhite a while).\n*   If you need cheap 3090s, 4090s, or A6000s: Tensordock.\n*   If you need Stable Diffusion inference only: Salad.\n*   If you need a wide variety of GPUs: Runpod or Tensordock.\n*   If you want to play around with templates / general hobbyist: Runpod.\n\nThe large clouds generally have worse pricing and more complicated setups than the above.\n\nIf you’re tied to one of the big clouds (AWS, Azure, GCP), then you don’t have a choice, so use that.\n\nMore info [here](https://gpus.llm-utils.org/fluidstack-vs-lambda-labs-vs-runpod-vs-tensordock/), [here](https://gpus.llm-utils.org/gpu-clouds-for-falcon-40b/), [here](https://gpus.llm-utils.org/h100-gpu-cloud-availability-and-pricing/), [here](https://gpus.llm-utils.org/alternative-gpu-clouds/), [here](https://gpus.llm-utils.org/gpu-cloud-user-experience-comparison/) and [here.](https://gpus.llm-utils.org/gpu-clouds-for-each-gpu/)\n\nWhat’s the easiest GPU cloud to start with? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#whats-the-easiest-gpu-cloud-to-start-with)\n--------------------------------------------------------------------------------------------------------------------------------------\n\nRunpod and [their templates.](https://www.runpod.io/console/templates) Pick a template, pick a GPU, click custommize deployment and increase the temporary and persistent disk space to an appropriate size, click set overrides, click continue, click deploy, then click view logs, then once it’s done setup, either use the URL provided by the logs or click to connect to whatever you deployed.\n\nNote that Runpod Pods are not full-featured VMs, they are docker containers on host machines.\n\nHow much VRAM and system ram do I need, and how many vCPUs? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#how-much-vram-and-system-ram-do-i-need-and-how-many-vcpus)\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nHere are some basic and often-wrong rules of thumb:\n\n*   VRAM (Video RAM / GPU RAM)\n    *   Llama 2 70B GPTQ 4 bit 50-60GB\n    *   Stable Diffusion 16GB+ preferred\n    *   Whisper 12GB+ if using OpenAI version for optimal transcription speed, can be as low as running on a CPU if using a community version\n*   System ram\n    *   1-2x your amount of VRAM\n*   vCPUs\n    *   8-16 vCPUs should be more than sufficient for most non-large-scale GPU workloads\n*   Disk space\n    *   Very use case dependent. If you’re not sure, start with 100GB and see if that’s enough for your use case\n\nMore info [here](https://gpus.llm-utils.org/vram-and-vcpus/).\n\nSXM or PCIe, and do I need NVLink? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#sxm-or-pcie-and-do-i-need-nvlink)\n--------------------------------------------------------------------------------------------------------------------\n\nIf you’re not sure, then you should assume it doesn’t matter for your use case. More info [here](https://gpus.llm-utils.org/nvlink-sxm-and-pcie/).\n\nWhat about InfiniBand? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-infiniband)\n---------------------------------------------------------------------------------------------\n\nIf you’re renting one or two GPUs, it’s not relevant for you. If you’re doing a cluster of thousands, you’ll likely want InfiniBand.\n\nWhat’s the difference between RTX 6000, A6000, and 6000 Ada? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#whats-the-difference-between-rtx-6000-a6000-and-6000-ada)\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n3 different cards! It’s a confusing naming scheme.\n\n*   RTX 6000 (Quadro RTX 6000, 24 GB VRAM, launched Aug 13, 2018)\n*   RTX A6000 (48 GB VRAM, launched Oct 5, 2020)\n*   RTX 6000 Ada (48 GB VRAM, launched Dec 3, 2022)\n\nWhat about the difference between a DGX GH200, a GH200, and an H100? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-the-difference-between-a-dgx-gh200-a-gh200-and-an-h100)\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n### Chart version [#](https://gpus.llm-utils.org/cloud-gpu-guide/#chart-version)\n\ngraph TB A(1x DGX GH200) subgraph GH200s \\[256x GH200s\\] B(Each GH200) subgraph H100Grace \\[H100 GPU & Grace CPU\\] C(1x H100) D(1x Grace CPU) end B -- \"contains\" --\\> H100Grace end A -- \"contains\" --\\> GH200s\n\n### Text version [#](https://gpus.llm-utils.org/cloud-gpu-guide/#text-version)\n\n*   1x DGX GH200\n    *   Contains 256x GH200s (“Grace Hoppers”)\n        *   Each GH200 contains 1x H100 and 1x Grace CPU\n\nMore info [here](https://gpus.llm-utils.org/dgx-gh200-vs-gh200-vs-h100/).\n\n### What about DGX Cloud? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-dgx-cloud)\n\nIt’s Nvidia’s official cloud offering aimed at enterprises. You buy it through Nvidia but rent through an existing cloud like Oracle.\n\n8 GPUs per instance, starting at $37k/month.\n\nMore info [here](https://gpus.llm-utils.org/dgx-cloud/).\n\nAre H100s a big upgrade from A100s? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#are-h100s-a-big-upgrade-from-a100s)\n-----------------------------------------------------------------------------------------------------------------------\n\nYes, the speedup is significant, and I’m told that with H100s can scale up performance to large numbers of GPUs better than A100s can.\n\nSo for training LLMs, H100s are the best bet.\n\nWhat about AMD, Intel, Cerebras [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-about-amd-intel-cerebras)\n--------------------------------------------------------------------------------------------------------------\n\nFor now, Nvidia is easier. We’ll put content about those other cards out soon. There’s other things that aren’t chips that are relevant to making Nvidia alternatives more workable too, and we’ll write about those.\n\nAMD has some cards with 128GB and 192GB of HBM3 VRAM, which is cool. (MI300A and MI300X)\n\nWhat next? [#](https://gpus.llm-utils.org/cloud-gpu-guide/#what-next)\n---------------------------------------------------------------------\n\nIf you’re ready to experiment, go set up a Runpod account, put a balance of $10, browse their templates, and deploy a template to a GPU instance. If you’re more experienced and don’t need templates, then consider starting with a different GPU cloud.\n\n_Submit [feedback on this post](https://airtable.com/appUfDSBiDkn4qqVH/shr411VWRbl9og1xb) or [get early access and/or notifications of future posts](https://airtable.com/appUfDSBiDkn4qqVH/shr411VWRbl9og1xb)._",
  "publishedTime": "2023-07-06T09:38:50-07:00",
  "usage": {
    "tokens": 2645
  }
}
```
