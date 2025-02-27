---
title: 🤗 Transformers
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
url: https://huggingface.co/docs/transformers/index
timestamp: 2025-01-20T15:48:02.469Z
domain: huggingface.co
path: docs_transformers_index
---

# 🤗 Transformers


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


## Content

[](https://huggingface.co/docs/transformers/index#-transformers)🤗 Transformers
-------------------------------------------------------------------------------

State-of-the-art Machine Learning for [PyTorch](https://pytorch.org/), [TensorFlow](https://www.tensorflow.org/), and [JAX](https://jax.readthedocs.io/en/latest/).

🤗 Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as:

📝 **Natural Language Processing**: text classification, named entity recognition, question answering, language modeling, code generation, summarization, translation, multiple choice, and text generation.  
🖼️ **Computer Vision**: image classification, object detection, and segmentation.  
🗣️ **Audio**: automatic speech recognition and audio classification.  
🐙 **Multimodal**: table question answering, optical character recognition, information extraction from scanned documents, video classification, and visual question answering.

🤗 Transformers support framework interoperability between PyTorch, TensorFlow, and JAX. This provides the flexibility to use a different framework at each stage of a model’s life; train a model in three lines of code in one framework, and load it for inference in another. Models can also be exported to a format like ONNX and TorchScript for deployment in production environments.

Join the growing community on the [Hub](https://huggingface.co/models), [forum](https://discuss.huggingface.co/), or [Discord](https://discord.com/invite/JfAtkvEtRb) today!

[](https://huggingface.co/docs/transformers/index#if-you-are-looking-for-custom-support-from-the-hugging-face-team)If you are looking for custom support from the Hugging Face team
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 5: HuggingFace Expert Acceleration Program](https://cdn-media.huggingface.co/marketing/transformers/new-support-improved.png)](https://huggingface.co/support)

[](https://huggingface.co/docs/transformers/index#contents)Contents
-------------------------------------------------------------------

The documentation is organized into five sections:

*   **GET STARTED** provides a quick tour of the library and installation instructions to get up and running.
    
*   **TUTORIALS** are a great place to start if you’re a beginner. This section will help you gain the basic skills you need to start using the library.
    
*   **HOW-TO GUIDES** show you how to achieve a specific goal, like finetuning a pretrained model for language modeling or how to write and share a custom model.
    
*   **CONCEPTUAL GUIDES** offers more discussion and explanation of the underlying concepts and ideas behind models, tasks, and the design philosophy of 🤗 Transformers.
    
*   **API** describes all classes and functions:
    
    *   **MAIN CLASSES** details the most important classes like configuration, model, tokenizer, and pipeline.
    *   **MODELS** details the classes and functions related to each model implemented in the library.
    *   **INTERNAL HELPERS** details utility classes and functions used internally.

[](https://huggingface.co/docs/transformers/index#supported-models-and-frameworks)Supported models and frameworks
-----------------------------------------------------------------------------------------------------------------

The table below represents the current support in the library for each of those models, whether they have a Python tokenizer (called “slow”). A “fast” tokenizer backed by the 🤗 Tokenizers library, whether they have support in Jax (via Flax), PyTorch, and/or TensorFlow.

| Model | PyTorch support | TensorFlow support | Flax Support |
| --- | --- | --- | --- |
| [ALBERT](https://huggingface.co/docs/transformers/model_doc/albert) | ✅ | ✅ | ✅ |
| [ALIGN](https://huggingface.co/docs/transformers/model_doc/align) | ✅ | ❌ | ❌ |
| [AltCLIP](https://huggingface.co/docs/transformers/model_doc/altclip) | ✅ | ❌ | ❌ |
| [Aria](https://huggingface.co/docs/transformers/model_doc/aria) | ✅ | ❌ | ❌ |
| [AriaText](https://huggingface.co/docs/transformers/model_doc/aria_text) | ✅ | ❌ | ❌ |
| [Audio Spectrogram Transformer](https://huggingface.co/docs/transformers/model_doc/audio-spectrogram-transformer) | ✅ | ❌ | ❌ |
| [Autoformer](https://huggingface.co/docs/transformers/model_doc/autoformer) | ✅ | ❌ | ❌ |
| [Bamba](https://huggingface.co/docs/transformers/model_doc/bamba) | ✅ | ❌ | ❌ |
| [Bark](https://huggingface.co/docs/transformers/model_doc/bark) | ✅ | ❌ | ❌ |
| [BART](https://huggingface.co/docs/transformers/model_doc/bart) | ✅ | ✅ | ✅ |
| [BARThez](https://huggingface.co/docs/transformers/model_doc/barthez) | ✅ | ✅ | ✅ |
| [BARTpho](https://huggingface.co/docs/transformers/model_doc/bartpho) | ✅ | ✅ | ✅ |
| [BEiT](https://huggingface.co/docs/transformers/model_doc/beit) | ✅ | ❌ | ✅ |
| [BERT](https://huggingface.co/docs/transformers/model_doc/bert) | ✅ | ✅ | ✅ |
| [Bert Generation](https://huggingface.co/docs/transformers/model_doc/bert-generation) | ✅ | ❌ | ❌ |
| [BertJapanese](https://huggingface.co/docs/transformers/model_doc/bert-japanese) | ✅ | ✅ | ✅ |
| [BERTweet](https://huggingface.co/docs/transformers/model_doc/bertweet) | ✅ | ✅ | ✅ |
| [BigBird](https://huggingface.co/docs/transformers/model_doc/big_bird) | ✅ | ❌ | ✅ |
| [BigBird-Pegasus](https://huggingface.co/docs/transformers/model_doc/bigbird_pegasus) | ✅ | ❌ | ❌ |
| [BioGpt](https://huggingface.co/docs/transformers/model_doc/biogpt) | ✅ | ❌ | ❌ |
| [BiT](https://huggingface.co/docs/transformers/model_doc/bit) | ✅ | ❌ | ❌ |
| [Blenderbot](https://huggingface.co/docs/transformers/model_doc/blenderbot) | ✅ | ✅ | ✅ |
| [BlenderbotSmall](https://huggingface.co/docs/transformers/model_doc/blenderbot-small) | ✅ | ✅ | ✅ |
| [BLIP](https://huggingface.co/docs/transformers/model_doc/blip) | ✅ | ✅ | ❌ |
| [BLIP-2](https://huggingface.co/docs/transformers/model_doc/blip-2) | ✅ | ❌ | ❌ |
| [BLOOM](https://huggingface.co/docs/transformers/model_doc/bloom) | ✅ | ❌ | ✅ |
| [BORT](https://huggingface.co/docs/transformers/model_doc/bort) | ✅ | ✅ | ✅ |
| [BridgeTower](https://huggingface.co/docs/transformers/model_doc/bridgetower) | ✅ | ❌ | ❌ |
| [BROS](https://huggingface.co/docs/transformers/model_doc/bros) | ✅ | ❌ | ❌ |
| [ByT5](https://huggingface.co/docs/transformers/model_doc/byt5) | ✅ | ✅ | ✅ |
| [CamemBERT](https://huggingface.co/docs/transformers/model_doc/camembert) | ✅ | ✅ | ❌ |
| [CANINE](https://huggingface.co/docs/transformers/model_doc/canine) | ✅ | ❌ | ❌ |
| [Chameleon](https://huggingface.co/docs/transformers/model_doc/chameleon) | ✅ | ❌ | ❌ |
| [Chinese-CLIP](https://huggingface.co/docs/transformers/model_doc/chinese_clip) | ✅ | ❌ | ❌ |
| [CLAP](https://huggingface.co/docs/transformers/model_doc/clap) | ✅ | ❌ | ❌ |
| [CLIP](https://huggingface.co/docs/transformers/model_doc/clip) | ✅ | ✅ | ✅ |
| [CLIPSeg](https://huggingface.co/docs/transformers/model_doc/clipseg) | ✅ | ❌ | ❌ |
| [CLVP](https://huggingface.co/docs/transformers/model_doc/clvp) | ✅ | ❌ | ❌ |
| [CodeGen](https://huggingface.co/docs/transformers/model_doc/codegen) | ✅ | ❌ | ❌ |
| [CodeLlama](https://huggingface.co/docs/transformers/model_doc/code_llama) | ✅ | ❌ | ✅ |
| [Cohere](https://huggingface.co/docs/transformers/model_doc/cohere) | ✅ | ❌ | ❌ |
| [Cohere2](https://huggingface.co/docs/transformers/model_doc/cohere2) | ✅ | ❌ | ❌ |
| [ColPali](https://huggingface.co/docs/transformers/model_doc/colpali) | ✅ | ❌ | ❌ |
| [Conditional DETR](https://huggingface.co/docs/transformers/model_doc/conditional_detr) | ✅ | ❌ | ❌ |
| [ConvBERT](https://huggingface.co/docs/transformers/model_doc/convbert) | ✅ | ✅ | ❌ |
| [ConvNeXT](https://huggingface.co/docs/transformers/model_doc/convnext) | ✅ | ✅ | ❌ |
| [ConvNeXTV2](https://huggingface.co/docs/transformers/model_doc/convnextv2) | ✅ | ✅ | ❌ |
| [CPM](https://huggingface.co/docs/transformers/model_doc/cpm) | ✅ | ✅ | ✅ |
| [CPM-Ant](https://huggingface.co/docs/transformers/model_doc/cpmant) | ✅ | ❌ | ❌ |
| [CTRL](https://huggingface.co/docs/transformers/model_doc/ctrl) | ✅ | ✅ | ❌ |
| [CvT](https://huggingface.co/docs/transformers/model_doc/cvt) | ✅ | ✅ | ❌ |
| [DAC](https://huggingface.co/docs/transformers/model_doc/dac) | ✅ | ❌ | ❌ |
| [Data2VecAudio](https://huggingface.co/docs/transformers/model_doc/data2vec) | ✅ | ❌ | ❌ |
| [Data2VecText](https://huggingface.co/docs/transformers/model_doc/data2vec) | ✅ | ❌ | ❌ |
| [Data2VecVision](https://huggingface.co/docs/transformers/model_doc/data2vec) | ✅ | ✅ | ❌ |
| [DBRX](https://huggingface.co/docs/transformers/model_doc/dbrx) | ✅ | ❌ | ❌ |
| [DeBERTa](https://huggingface.co/docs/transformers/model_doc/deberta) | ✅ | ✅ | ❌ |
| [DeBERTa-v2](https://huggingface.co/docs/transformers/model_doc/deberta-v2) | ✅ | ✅ | ❌ |
| [Decision Transformer](https://huggingface.co/docs/transformers/model_doc/decision_transformer) | ✅ | ❌ | ❌ |
| [Deformable DETR](https://huggingface.co/docs/transformers/model_doc/deformable_detr) | ✅ | ❌ | ❌ |
| [DeiT](https://huggingface.co/docs/transformers/model_doc/deit) | ✅ | ✅ | ❌ |
| [DePlot](https://huggingface.co/docs/transformers/model_doc/deplot) | ✅ | ❌ | ❌ |
| [Depth Anything](https://huggingface.co/docs/transformers/model_doc/depth_anything) | ✅ | ❌ | ❌ |
| [DETA](https://huggingface.co/docs/transformers/model_doc/deta) | ✅ | ❌ | ❌ |
| [DETR](https://huggingface.co/docs/transformers/model_doc/detr) | ✅ | ❌ | ❌ |
| [DialoGPT](https://huggingface.co/docs/transformers/model_doc/dialogpt) | ✅ | ✅ | ✅ |
| [DiffLlama](https://huggingface.co/docs/transformers/model_doc/diffllama) | ✅ | ❌ | ❌ |
| [DiNAT](https://huggingface.co/docs/transformers/model_doc/dinat) | ✅ | ❌ | ❌ |
| [DINOv2](https://huggingface.co/docs/transformers/model_doc/dinov2) | ✅ | ❌ | ✅ |
| [DINOv2 with Registers](https://huggingface.co/docs/transformers/model_doc/dinov2_with_registers) | ✅ | ❌ | ❌ |
| [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert) | ✅ | ✅ | ✅ |
| [DiT](https://huggingface.co/docs/transformers/model_doc/dit) | ✅ | ❌ | ✅ |
| [DonutSwin](https://huggingface.co/docs/transformers/model_doc/donut) | ✅ | ❌ | ❌ |
| [DPR](https://huggingface.co/docs/transformers/model_doc/dpr) | ✅ | ✅ | ❌ |
| [DPT](https://huggingface.co/docs/transformers/model_doc/dpt) | ✅ | ❌ | ❌ |
| [EfficientFormer](https://huggingface.co/docs/transformers/model_doc/efficientformer) | ✅ | ✅ | ❌ |
| [EfficientNet](https://huggingface.co/docs/transformers/model_doc/efficientnet) | ✅ | ❌ | ❌ |
| [ELECTRA](https://huggingface.co/docs/transformers/model_doc/electra) | ✅ | ✅ | ✅ |
| [Emu3](https://huggingface.co/docs/transformers/model_doc/emu3) | ✅ | ❌ | ❌ |
| [EnCodec](https://huggingface.co/docs/transformers/model_doc/encodec) | ✅ | ❌ | ❌ |
| [Encoder decoder](https://huggingface.co/docs/transformers/model_doc/encoder-decoder) | ✅ | ✅ | ✅ |
| [ERNIE](https://huggingface.co/docs/transformers/model_doc/ernie) | ✅ | ❌ | ❌ |
| [ErnieM](https://huggingface.co/docs/transformers/model_doc/ernie_m) | ✅ | ❌ | ❌ |
| [ESM](https://huggingface.co/docs/transformers/model_doc/esm) | ✅ | ✅ | ❌ |
| [FairSeq Machine-Translation](https://huggingface.co/docs/transformers/model_doc/fsmt) | ✅ | ❌ | ❌ |
| [Falcon](https://huggingface.co/docs/transformers/model_doc/falcon) | ✅ | ❌ | ❌ |
| [Falcon3](https://huggingface.co/docs/transformers/model_doc/falcon3) | ✅ | ❌ | ✅ |
| [FalconMamba](https://huggingface.co/docs/transformers/model_doc/falcon_mamba) | ✅ | ❌ | ❌ |
| [FastSpeech2Conformer](https://huggingface.co/docs/transformers/model_doc/fastspeech2_conformer) | ✅ | ❌ | ❌ |
| [FLAN-T5](https://huggingface.co/docs/transformers/model_doc/flan-t5) | ✅ | ✅ | ✅ |
| [FLAN-UL2](https://huggingface.co/docs/transformers/model_doc/flan-ul2) | ✅ | ✅ | ✅ |
| [FlauBERT](https://huggingface.co/docs/transformers/model_doc/flaubert) | ✅ | ✅ | ❌ |
| [FLAVA](https://huggingface.co/docs/transformers/model_doc/flava) | ✅ | ❌ | ❌ |
| [FNet](https://huggingface.co/docs/transformers/model_doc/fnet) | ✅ | ❌ | ❌ |
| [FocalNet](https://huggingface.co/docs/transformers/model_doc/focalnet) | ✅ | ❌ | ❌ |
| [Funnel Transformer](https://huggingface.co/docs/transformers/model_doc/funnel) | ✅ | ✅ | ❌ |
| [Fuyu](https://huggingface.co/docs/transformers/model_doc/fuyu) | ✅ | ❌ | ❌ |
| [Gemma](https://huggingface.co/docs/transformers/model_doc/gemma) | ✅ | ❌ | ✅ |
| [Gemma2](https://huggingface.co/docs/transformers/model_doc/gemma2) | ✅ | ❌ | ❌ |
| [GIT](https://huggingface.co/docs/transformers/model_doc/git) | ✅ | ❌ | ❌ |
| [GLM](https://huggingface.co/docs/transformers/model_doc/glm) | ✅ | ❌ | ❌ |
| [GLPN](https://huggingface.co/docs/transformers/model_doc/glpn) | ✅ | ❌ | ❌ |
| [GPT Neo](https://huggingface.co/docs/transformers/model_doc/gpt_neo) | ✅ | ❌ | ✅ |
| [GPT NeoX](https://huggingface.co/docs/transformers/model_doc/gpt_neox) | ✅ | ❌ | ❌ |
| [GPT NeoX Japanese](https://huggingface.co/docs/transformers/model_doc/gpt_neox_japanese) | ✅ | ❌ | ❌ |
| [GPT-J](https://huggingface.co/docs/transformers/model_doc/gptj) | ✅ | ✅ | ✅ |
| [GPT-Sw3](https://huggingface.co/docs/transformers/model_doc/gpt-sw3) | ✅ | ✅ | ✅ |
| [GPTBigCode](https://huggingface.co/docs/transformers/model_doc/gpt_bigcode) | ✅ | ❌ | ❌ |
| [GPTSAN-japanese](https://huggingface.co/docs/transformers/model_doc/gptsan-japanese) | ✅ | ❌ | ❌ |
| [Granite](https://huggingface.co/docs/transformers/model_doc/granite) | ✅ | ❌ | ❌ |
| [GraniteMoeMoe](https://huggingface.co/docs/transformers/model_doc/granitemoe) | ✅ | ❌ | ❌ |
| [Graphormer](https://huggingface.co/docs/transformers/model_doc/graphormer) | ✅ | ❌ | ❌ |
| [Grounding DINO](https://huggingface.co/docs/transformers/model_doc/grounding-dino) | ✅ | ❌ | ❌ |
| [GroupViT](https://huggingface.co/docs/transformers/model_doc/groupvit) | ✅ | ✅ | ❌ |
| [HerBERT](https://huggingface.co/docs/transformers/model_doc/herbert) | ✅ | ✅ | ✅ |
| [Hiera](https://huggingface.co/docs/transformers/model_doc/hiera) | ✅ | ❌ | ❌ |
| [Hubert](https://huggingface.co/docs/transformers/model_doc/hubert) | ✅ | ✅ | ❌ |
| [I-BERT](https://huggingface.co/docs/transformers/model_doc/ibert) | ✅ | ❌ | ❌ |
| [I-JEPA](https://huggingface.co/docs/transformers/model_doc/ijepa) | ✅ | ❌ | ❌ |
| [IDEFICS](https://huggingface.co/docs/transformers/model_doc/idefics) | ✅ | ✅ | ❌ |
| [Idefics2](https://huggingface.co/docs/transformers/model_doc/idefics2) | ✅ | ❌ | ❌ |
| [Idefics3](https://huggingface.co/docs/transformers/model_doc/idefics3) | ✅ | ❌ | ❌ |
| [Idefics3VisionTransformer](https://huggingface.co/docs/transformers/model_doc/idefics3_vision) | ❌ | ❌ | ❌ |
| [ImageGPT](https://huggingface.co/docs/transformers/model_doc/imagegpt) | ✅ | ❌ | ❌ |
| [Informer](https://huggingface.co/docs/transformers/model_doc/informer) | ✅ | ❌ | ❌ |
| [InstructBLIP](https://huggingface.co/docs/transformers/model_doc/instructblip) | ✅ | ❌ | ❌ |
| [InstructBlipVideo](https://huggingface.co/docs/transformers/model_doc/instructblipvideo) | ✅ | ❌ | ❌ |
| [Jamba](https://huggingface.co/docs/transformers/model_doc/jamba) | ✅ | ❌ | ❌ |
| [JetMoe](https://huggingface.co/docs/transformers/model_doc/jetmoe) | ✅ | ❌ | ❌ |
| [Jukebox](https://huggingface.co/docs/transformers/model_doc/jukebox) | ✅ | ❌ | ❌ |
| [KOSMOS-2](https://huggingface.co/docs/transformers/model_doc/kosmos-2) | ✅ | ❌ | ❌ |
| [LayoutLM](https://huggingface.co/docs/transformers/model_doc/layoutlm) | ✅ | ✅ | ❌ |
| [LayoutLMv2](https://huggingface.co/docs/transformers/model_doc/layoutlmv2) | ✅ | ❌ | ❌ |
| [LayoutLMv3](https://huggingface.co/docs/transformers/model_doc/layoutlmv3) | ✅ | ✅ | ❌ |
| [LayoutXLM](https://huggingface.co/docs/transformers/model_doc/layoutxlm) | ✅ | ❌ | ❌ |
| [LED](https://huggingface.co/docs/transformers/model_doc/led) | ✅ | ✅ | ❌ |
| [LeViT](https://huggingface.co/docs/transformers/model_doc/levit) | ✅ | ❌ | ❌ |
| [LiLT](https://huggingface.co/docs/transformers/model_doc/lilt) | ✅ | ❌ | ❌ |
| [LLaMA](https://huggingface.co/docs/transformers/model_doc/llama) | ✅ | ❌ | ✅ |
| [Llama2](https://huggingface.co/docs/transformers/model_doc/llama2) | ✅ | ❌ | ✅ |
| [Llama3](https://huggingface.co/docs/transformers/model_doc/llama3) | ✅ | ❌ | ✅ |
| [LLaVa](https://huggingface.co/docs/transformers/model_doc/llava) | ✅ | ❌ | ❌ |
| [LLaVA-NeXT](https://huggingface.co/docs/transformers/model_doc/llava_next) | ✅ | ❌ | ❌ |
| [LLaVa-NeXT-Video](https://huggingface.co/docs/transformers/model_doc/llava_next_video) | ✅ | ❌ | ❌ |
| [LLaVA-Onevision](https://huggingface.co/docs/transformers/model_doc/llava_onevision) | ✅ | ❌ | ❌ |
| [Longformer](https://huggingface.co/docs/transformers/model_doc/longformer) | ✅ | ✅ | ❌ |
| [LongT5](https://huggingface.co/docs/transformers/model_doc/longt5) | ✅ | ❌ | ✅ |
| [LUKE](https://huggingface.co/docs/transformers/model_doc/luke) | ✅ | ❌ | ❌ |
| [LXMERT](https://huggingface.co/docs/transformers/model_doc/lxmert) | ✅ | ✅ | ❌ |
| [M-CTC-T](https://huggingface.co/docs/transformers/model_doc/mctct) | ✅ | ❌ | ❌ |
| [M2M100](https://huggingface.co/docs/transformers/model_doc/m2m_100) | ✅ | ❌ | ❌ |
| [MADLAD-400](https://huggingface.co/docs/transformers/model_doc/madlad-400) | ✅ | ✅ | ✅ |
| [Mamba](https://huggingface.co/docs/transformers/model_doc/mamba) | ✅ | ❌ | ❌ |
| [mamba2](https://huggingface.co/docs/transformers/model_doc/mamba2) | ✅ | ❌ | ❌ |
| [Marian](https://huggingface.co/docs/transformers/model_doc/marian) | ✅ | ✅ | ✅ |
| [MarkupLM](https://huggingface.co/docs/transformers/model_doc/markuplm) | ✅ | ❌ | ❌ |
| [Mask2Former](https://huggingface.co/docs/transformers/model_doc/mask2former) | ✅ | ❌ | ❌ |
| [MaskFormer](https://huggingface.co/docs/transformers/model_doc/maskformer) | ✅ | ❌ | ❌ |
| [MatCha](https://huggingface.co/docs/transformers/model_doc/matcha) | ✅ | ❌ | ❌ |
| [mBART](https://huggingface.co/docs/transformers/model_doc/mbart) | ✅ | ✅ | ✅ |
| [mBART-50](https://huggingface.co/docs/transformers/model_doc/mbart50) | ✅ | ✅ | ✅ |
| [MEGA](https://huggingface.co/docs/transformers/model_doc/mega) | ✅ | ❌ | ❌ |
| [Megatron-BERT](https://huggingface.co/docs/transformers/model_doc/megatron-bert) | ✅ | ❌ | ❌ |
| [Megatron-GPT2](https://huggingface.co/docs/transformers/model_doc/megatron_gpt2) | ✅ | ✅ | ✅ |
| [MGP-STR](https://huggingface.co/docs/transformers/model_doc/mgp-str) | ✅ | ❌ | ❌ |
| [Mimi](https://huggingface.co/docs/transformers/model_doc/mimi) | ✅ | ❌ | ❌ |
| [Mistral](https://huggingface.co/docs/transformers/model_doc/mistral) | ✅ | ✅ | ✅ |
| [Mixtral](https://huggingface.co/docs/transformers/model_doc/mixtral) | ✅ | ❌ | ❌ |
| [Mllama](https://huggingface.co/docs/transformers/model_doc/mllama) | ✅ | ❌ | ❌ |
| [mLUKE](https://huggingface.co/docs/transformers/model_doc/mluke) | ✅ | ❌ | ❌ |
| [MMS](https://huggingface.co/docs/transformers/model_doc/mms) | ✅ | ✅ | ✅ |
| [MobileBERT](https://huggingface.co/docs/transformers/model_doc/mobilebert) | ✅ | ✅ | ❌ |
| [MobileNetV1](https://huggingface.co/docs/transformers/model_doc/mobilenet_v1) | ✅ | ❌ | ❌ |
| [MobileNetV2](https://huggingface.co/docs/transformers/model_doc/mobilenet_v2) | ✅ | ❌ | ❌ |
| [MobileViT](https://huggingface.co/docs/transformers/model_doc/mobilevit) | ✅ | ✅ | ❌ |
| [MobileViTV2](https://huggingface.co/docs/transformers/model_doc/mobilevitv2) | ✅ | ❌ | ❌ |
| [ModernBERT](https://huggingface.co/docs/transformers/model_doc/modernbert) | ✅ | ❌ | ❌ |
| [Moonshine](https://huggingface.co/docs/transformers/model_doc/moonshine) | ✅ | ❌ | ❌ |
| [Moshi](https://huggingface.co/docs/transformers/model_doc/moshi) | ✅ | ❌ | ❌ |
| [MPNet](https://huggingface.co/docs/transformers/model_doc/mpnet) | ✅ | ✅ | ❌ |
| [MPT](https://huggingface.co/docs/transformers/model_doc/mpt) | ✅ | ❌ | ❌ |
| [MRA](https://huggingface.co/docs/transformers/model_doc/mra) | ✅ | ❌ | ❌ |
| [MT5](https://huggingface.co/docs/transformers/model_doc/mt5) | ✅ | ✅ | ✅ |
| [MusicGen](https://huggingface.co/docs/transformers/model_doc/musicgen) | ✅ | ❌ | ❌ |
| [MusicGen Melody](https://huggingface.co/docs/transformers/model_doc/musicgen_melody) | ✅ | ❌ | ❌ |
| [MVP](https://huggingface.co/docs/transformers/model_doc/mvp) | ✅ | ❌ | ❌ |
| [NAT](https://huggingface.co/docs/transformers/model_doc/nat) | ✅ | ❌ | ❌ |
| [Nemotron](https://huggingface.co/docs/transformers/model_doc/nemotron) | ✅ | ❌ | ❌ |
| [Nezha](https://huggingface.co/docs/transformers/model_doc/nezha) | ✅ | ❌ | ❌ |
| [NLLB](https://huggingface.co/docs/transformers/model_doc/nllb) | ✅ | ❌ | ❌ |
| [NLLB-MOE](https://huggingface.co/docs/transformers/model_doc/nllb-moe) | ✅ | ❌ | ❌ |
| [Nougat](https://huggingface.co/docs/transformers/model_doc/nougat) | ✅ | ✅ | ✅ |
| [Nyströmformer](https://huggingface.co/docs/transformers/model_doc/nystromformer) | ✅ | ❌ | ❌ |
| [OLMo](https://huggingface.co/docs/transformers/model_doc/olmo) | ✅ | ❌ | ❌ |
| [OLMo2](https://huggingface.co/docs/transformers/model_doc/olmo2) | ✅ | ❌ | ❌ |
| [OLMoE](https://huggingface.co/docs/transformers/model_doc/olmoe) | ✅ | ❌ | ❌ |
| [OmDet-Turbo](https://huggingface.co/docs/transformers/model_doc/omdet-turbo) | ✅ | ❌ | ❌ |
| [OneFormer](https://huggingface.co/docs/transformers/model_doc/oneformer) | ✅ | ❌ | ❌ |
| [OpenAI GPT](https://huggingface.co/docs/transformers/model_doc/openai-gpt) | ✅ | ✅ | ❌ |
| [OpenAI GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2) | ✅ | ✅ | ✅ |
| [OpenLlama](https://huggingface.co/docs/transformers/model_doc/open-llama) | ✅ | ❌ | ❌ |
| [OPT](https://huggingface.co/docs/transformers/model_doc/opt) | ✅ | ✅ | ✅ |
| [OWL-ViT](https://huggingface.co/docs/transformers/model_doc/owlvit) | ✅ | ❌ | ❌ |
| [OWLv2](https://huggingface.co/docs/transformers/model_doc/owlv2) | ✅ | ❌ | ❌ |
| [PaliGemma](https://huggingface.co/docs/transformers/model_doc/paligemma) | ✅ | ❌ | ❌ |
| [PatchTSMixer](https://huggingface.co/docs/transformers/model_doc/patchtsmixer) | ✅ | ❌ | ❌ |
| [PatchTST](https://huggingface.co/docs/transformers/model_doc/patchtst) | ✅ | ❌ | ❌ |
| [Pegasus](https://huggingface.co/docs/transformers/model_doc/pegasus) | ✅ | ✅ | ✅ |
| [PEGASUS-X](https://huggingface.co/docs/transformers/model_doc/pegasus_x) | ✅ | ❌ | ❌ |
| [Perceiver](https://huggingface.co/docs/transformers/model_doc/perceiver) | ✅ | ❌ | ❌ |
| [Persimmon](https://huggingface.co/docs/transformers/model_doc/persimmon) | ✅ | ❌ | ❌ |
| [Phi](https://huggingface.co/docs/transformers/model_doc/phi) | ✅ | ❌ | ❌ |
| [Phi3](https://huggingface.co/docs/transformers/model_doc/phi3) | ✅ | ❌ | ❌ |
| [Phimoe](https://huggingface.co/docs/transformers/model_doc/phimoe) | ✅ | ❌ | ❌ |
| [PhoBERT](https://huggingface.co/docs/transformers/model_doc/phobert) | ✅ | ✅ | ✅ |
| [Pix2Struct](https://huggingface.co/docs/transformers/model_doc/pix2struct) | ✅ | ❌ | ❌ |
| [Pixtral](https://huggingface.co/docs/transformers/model_doc/pixtral) | ✅ | ❌ | ❌ |
| [PLBart](https://huggingface.co/docs/transformers/model_doc/plbart) | ✅ | ❌ | ❌ |
| [PoolFormer](https://huggingface.co/docs/transformers/model_doc/poolformer) | ✅ | ❌ | ❌ |
| [Pop2Piano](https://huggingface.co/docs/transformers/model_doc/pop2piano) | ✅ | ❌ | ❌ |
| [ProphetNet](https://huggingface.co/docs/transformers/model_doc/prophetnet) | ✅ | ❌ | ❌ |
| [PVT](https://huggingface.co/docs/transformers/model_doc/pvt) | ✅ | ❌ | ❌ |
| [PVTv2](https://huggingface.co/docs/transformers/model_doc/pvt_v2) | ✅ | ❌ | ❌ |
| [QDQBert](https://huggingface.co/docs/transformers/model_doc/qdqbert) | ✅ | ❌ | ❌ |
| [Qwen2](https://huggingface.co/docs/transformers/model_doc/qwen2) | ✅ | ❌ | ❌ |
| [Qwen2Audio](https://huggingface.co/docs/transformers/model_doc/qwen2_audio) | ✅ | ❌ | ❌ |
| [Qwen2MoE](https://huggingface.co/docs/transformers/model_doc/qwen2_moe) | ✅ | ❌ | ❌ |
| [Qwen2VL](https://huggingface.co/docs/transformers/model_doc/qwen2_vl) | ✅ | ❌ | ❌ |
| [RAG](https://huggingface.co/docs/transformers/model_doc/rag) | ✅ | ✅ | ❌ |
| [REALM](https://huggingface.co/docs/transformers/model_doc/realm) | ✅ | ❌ | ❌ |
| [RecurrentGemma](https://huggingface.co/docs/transformers/model_doc/recurrent_gemma) | ✅ | ❌ | ❌ |
| [Reformer](https://huggingface.co/docs/transformers/model_doc/reformer) | ✅ | ❌ | ❌ |
| [RegNet](https://huggingface.co/docs/transformers/model_doc/regnet) | ✅ | ✅ | ✅ |
| [RemBERT](https://huggingface.co/docs/transformers/model_doc/rembert) | ✅ | ✅ | ❌ |
| [ResNet](https://huggingface.co/docs/transformers/model_doc/resnet) | ✅ | ✅ | ✅ |
| [RetriBERT](https://huggingface.co/docs/transformers/model_doc/retribert) | ✅ | ❌ | ❌ |
| [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta) | ✅ | ✅ | ✅ |
| [RoBERTa-PreLayerNorm](https://huggingface.co/docs/transformers/model_doc/roberta-prelayernorm) | ✅ | ✅ | ✅ |
| [RoCBert](https://huggingface.co/docs/transformers/model_doc/roc_bert) | ✅ | ❌ | ❌ |
| [RoFormer](https://huggingface.co/docs/transformers/model_doc/roformer) | ✅ | ✅ | ✅ |
| [RT-DETR](https://huggingface.co/docs/transformers/model_doc/rt_detr) | ✅ | ❌ | ❌ |
| [RT-DETR-ResNet](https://huggingface.co/docs/transformers/model_doc/rt_detr_resnet) | ✅ | ❌ | ❌ |
| [RWKV](https://huggingface.co/docs/transformers/model_doc/rwkv) | ✅ | ❌ | ❌ |
| [SAM](https://huggingface.co/docs/transformers/model_doc/sam) | ✅ | ✅ | ❌ |
| [SeamlessM4T](https://huggingface.co/docs/transformers/model_doc/seamless_m4t) | ✅ | ❌ | ❌ |
| [SeamlessM4Tv2](https://huggingface.co/docs/transformers/model_doc/seamless_m4t_v2) | ✅ | ❌ | ❌ |
| [SegFormer](https://huggingface.co/docs/transformers/model_doc/segformer) | ✅ | ✅ | ❌ |
| [SegGPT](https://huggingface.co/docs/transformers/model_doc/seggpt) | ✅ | ❌ | ❌ |
| [SEW](https://huggingface.co/docs/transformers/model_doc/sew) | ✅ | ❌ | ❌ |
| [SEW-D](https://huggingface.co/docs/transformers/model_doc/sew-d) | ✅ | ❌ | ❌ |
| [SigLIP](https://huggingface.co/docs/transformers/model_doc/siglip) | ✅ | ❌ | ❌ |
| [Speech Encoder decoder](https://huggingface.co/docs/transformers/model_doc/speech-encoder-decoder) | ✅ | ❌ | ✅ |
| [Speech2Text](https://huggingface.co/docs/transformers/model_doc/speech_to_text) | ✅ | ✅ | ❌ |
| [SpeechT5](https://huggingface.co/docs/transformers/model_doc/speecht5) | ✅ | ❌ | ❌ |
| [Splinter](https://huggingface.co/docs/transformers/model_doc/splinter) | ✅ | ❌ | ❌ |
| [SqueezeBERT](https://huggingface.co/docs/transformers/model_doc/squeezebert) | ✅ | ❌ | ❌ |
| [StableLm](https://huggingface.co/docs/transformers/model_doc/stablelm) | ✅ | ❌ | ❌ |
| [Starcoder2](https://huggingface.co/docs/transformers/model_doc/starcoder2) | ✅ | ❌ | ❌ |
| [SuperPoint](https://huggingface.co/docs/transformers/model_doc/superpoint) | ✅ | ❌ | ❌ |
| [SwiftFormer](https://huggingface.co/docs/transformers/model_doc/swiftformer) | ✅ | ✅ | ❌ |
| [Swin Transformer](https://huggingface.co/docs/transformers/model_doc/swin) | ✅ | ✅ | ❌ |
| [Swin Transformer V2](https://huggingface.co/docs/transformers/model_doc/swinv2) | ✅ | ❌ | ❌ |
| [Swin2SR](https://huggingface.co/docs/transformers/model_doc/swin2sr) | ✅ | ❌ | ❌ |
| [SwitchTransformers](https://huggingface.co/docs/transformers/model_doc/switch_transformers) | ✅ | ❌ | ❌ |
| [T5](https://huggingface.co/docs/transformers/model_doc/t5) | ✅ | ✅ | ✅ |
| [T5v1.1](https://huggingface.co/docs/transformers/model_doc/t5v1.1) | ✅ | ✅ | ✅ |
| [Table Transformer](https://huggingface.co/docs/transformers/model_doc/table-transformer) | ✅ | ❌ | ❌ |
| [TAPAS](https://huggingface.co/docs/transformers/model_doc/tapas) | ✅ | ✅ | ❌ |
| [TAPEX](https://huggingface.co/docs/transformers/model_doc/tapex) | ✅ | ✅ | ✅ |
| [TextNet](https://huggingface.co/docs/transformers/model_doc/textnet) | ✅ | ❌ | ❌ |
| [Time Series Transformer](https://huggingface.co/docs/transformers/model_doc/time_series_transformer) | ✅ | ❌ | ❌ |
| [TimeSformer](https://huggingface.co/docs/transformers/model_doc/timesformer) | ✅ | ❌ | ❌ |
| [TimmWrapperModel](https://huggingface.co/docs/transformers/model_doc/timm_wrapper) | ✅ | ❌ | ❌ |
| [Trajectory Transformer](https://huggingface.co/docs/transformers/model_doc/trajectory_transformer) | ✅ | ❌ | ❌ |
| [Transformer-XL](https://huggingface.co/docs/transformers/model_doc/transfo-xl) | ✅ | ✅ | ❌ |
| [TrOCR](https://huggingface.co/docs/transformers/model_doc/trocr) | ✅ | ❌ | ❌ |
| [TVLT](https://huggingface.co/docs/transformers/model_doc/tvlt) | ✅ | ❌ | ❌ |
| [TVP](https://huggingface.co/docs/transformers/model_doc/tvp) | ✅ | ❌ | ❌ |
| [UDOP](https://huggingface.co/docs/transformers/model_doc/udop) | ✅ | ❌ | ❌ |
| [UL2](https://huggingface.co/docs/transformers/model_doc/ul2) | ✅ | ✅ | ✅ |
| [UMT5](https://huggingface.co/docs/transformers/model_doc/umt5) | ✅ | ❌ | ❌ |
| [UniSpeech](https://huggingface.co/docs/transformers/model_doc/unispeech) | ✅ | ❌ | ❌ |
| [UniSpeechSat](https://huggingface.co/docs/transformers/model_doc/unispeech-sat) | ✅ | ❌ | ❌ |
| [UnivNet](https://huggingface.co/docs/transformers/model_doc/univnet) | ✅ | ❌ | ❌ |
| [UPerNet](https://huggingface.co/docs/transformers/model_doc/upernet) | ✅ | ❌ | ❌ |
| [VAN](https://huggingface.co/docs/transformers/model_doc/van) | ✅ | ❌ | ❌ |
| [VideoLlava](https://huggingface.co/docs/transformers/model_doc/video_llava) | ✅ | ❌ | ❌ |
| [VideoMAE](https://huggingface.co/docs/transformers/model_doc/videomae) | ✅ | ❌ | ❌ |
| [ViLT](https://huggingface.co/docs/transformers/model_doc/vilt) | ✅ | ❌ | ❌ |
| [VipLlava](https://huggingface.co/docs/transformers/model_doc/vipllava) | ✅ | ❌ | ❌ |
| [Vision Encoder decoder](https://huggingface.co/docs/transformers/model_doc/vision-encoder-decoder) | ✅ | ✅ | ✅ |
| [VisionTextDualEncoder](https://huggingface.co/docs/transformers/model_doc/vision-text-dual-encoder) | ✅ | ✅ | ✅ |
| [VisualBERT](https://huggingface.co/docs/transformers/model_doc/visual_bert) | ✅ | ❌ | ❌ |
| [ViT](https://huggingface.co/docs/transformers/model_doc/vit) | ✅ | ✅ | ✅ |
| [ViT Hybrid](https://huggingface.co/docs/transformers/model_doc/vit_hybrid) | ✅ | ❌ | ❌ |
| [VitDet](https://huggingface.co/docs/transformers/model_doc/vitdet) | ✅ | ❌ | ❌ |
| [ViTMAE](https://huggingface.co/docs/transformers/model_doc/vit_mae) | ✅ | ✅ | ❌ |
| [ViTMatte](https://huggingface.co/docs/transformers/model_doc/vitmatte) | ✅ | ❌ | ❌ |
| [ViTMSN](https://huggingface.co/docs/transformers/model_doc/vit_msn) | ✅ | ❌ | ❌ |
| [VitPose](https://huggingface.co/docs/transformers/model_doc/vitpose) | ✅ | ❌ | ❌ |
| [VitPoseBackbone](https://huggingface.co/docs/transformers/model_doc/vitpose_backbone) | ✅ | ❌ | ❌ |
| [VITS](https://huggingface.co/docs/transformers/model_doc/vits) | ✅ | ❌ | ❌ |
| [ViViT](https://huggingface.co/docs/transformers/model_doc/vivit) | ✅ | ❌ | ❌ |
| [Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2) | ✅ | ✅ | ✅ |
| [Wav2Vec2-BERT](https://huggingface.co/docs/transformers/model_doc/wav2vec2-bert) | ✅ | ❌ | ❌ |
| [Wav2Vec2-Conformer](https://huggingface.co/docs/transformers/model_doc/wav2vec2-conformer) | ✅ | ❌ | ❌ |
| [Wav2Vec2Phoneme](https://huggingface.co/docs/transformers/model_doc/wav2vec2_phoneme) | ✅ | ✅ | ✅ |
| [WavLM](https://huggingface.co/docs/transformers/model_doc/wavlm) | ✅ | ❌ | ❌ |
| [Whisper](https://huggingface.co/docs/transformers/model_doc/whisper) | ✅ | ✅ | ✅ |
| [X-CLIP](https://huggingface.co/docs/transformers/model_doc/xclip) | ✅ | ❌ | ❌ |
| [X-MOD](https://huggingface.co/docs/transformers/model_doc/xmod) | ✅ | ❌ | ❌ |
| [XGLM](https://huggingface.co/docs/transformers/model_doc/xglm) | ✅ | ✅ | ✅ |
| [XLM](https://huggingface.co/docs/transformers/model_doc/xlm) | ✅ | ✅ | ❌ |
| [XLM-ProphetNet](https://huggingface.co/docs/transformers/model_doc/xlm-prophetnet) | ✅ | ❌ | ❌ |
| [XLM-RoBERTa](https://huggingface.co/docs/transformers/model_doc/xlm-roberta) | ✅ | ✅ | ✅ |
| [XLM-RoBERTa-XL](https://huggingface.co/docs/transformers/model_doc/xlm-roberta-xl) | ✅ | ❌ | ❌ |
| [XLM-V](https://huggingface.co/docs/transformers/model_doc/xlm-v) | ✅ | ✅ | ✅ |
| [XLNet](https://huggingface.co/docs/transformers/model_doc/xlnet) | ✅ | ✅ | ❌ |
| [XLS-R](https://huggingface.co/docs/transformers/model_doc/xls_r) | ✅ | ✅ | ✅ |
| [XLSR-Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/xlsr_wav2vec2) | ✅ | ✅ | ✅ |
| [YOLOS](https://huggingface.co/docs/transformers/model_doc/yolos) | ✅ | ❌ | ❌ |
| [YOSO](https://huggingface.co/docs/transformers/model_doc/yoso) | ✅ | ❌ | ❌ |
| [Zamba](https://huggingface.co/docs/transformers/model_doc/zamba) | ✅ | ❌ | ❌ |
| [ZoeDepth](https://huggingface.co/docs/transformers/model_doc/zoedepth) | ✅ | ❌ | ❌ |

[< \> Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/index.md)

## Metadata

```json
{
  "title": "🤗 Transformers",
  "description": "We’re on a journey to advance and democratize artificial intelligence through open source and open science.",
  "url": "https://huggingface.co/docs/transformers/index",
  "content": "[](https://huggingface.co/docs/transformers/index#-transformers)🤗 Transformers\n-------------------------------------------------------------------------------\n\nState-of-the-art Machine Learning for [PyTorch](https://pytorch.org/), [TensorFlow](https://www.tensorflow.org/), and [JAX](https://jax.readthedocs.io/en/latest/).\n\n🤗 Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as:\n\n📝 **Natural Language Processing**: text classification, named entity recognition, question answering, language modeling, code generation, summarization, translation, multiple choice, and text generation.  \n🖼️ **Computer Vision**: image classification, object detection, and segmentation.  \n🗣️ **Audio**: automatic speech recognition and audio classification.  \n🐙 **Multimodal**: table question answering, optical character recognition, information extraction from scanned documents, video classification, and visual question answering.\n\n🤗 Transformers support framework interoperability between PyTorch, TensorFlow, and JAX. This provides the flexibility to use a different framework at each stage of a model’s life; train a model in three lines of code in one framework, and load it for inference in another. Models can also be exported to a format like ONNX and TorchScript for deployment in production environments.\n\nJoin the growing community on the [Hub](https://huggingface.co/models), [forum](https://discuss.huggingface.co/), or [Discord](https://discord.com/invite/JfAtkvEtRb) today!\n\n[](https://huggingface.co/docs/transformers/index#if-you-are-looking-for-custom-support-from-the-hugging-face-team)If you are looking for custom support from the Hugging Face team\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[![Image 5: HuggingFace Expert Acceleration Program](https://cdn-media.huggingface.co/marketing/transformers/new-support-improved.png)](https://huggingface.co/support)\n\n[](https://huggingface.co/docs/transformers/index#contents)Contents\n-------------------------------------------------------------------\n\nThe documentation is organized into five sections:\n\n*   **GET STARTED** provides a quick tour of the library and installation instructions to get up and running.\n    \n*   **TUTORIALS** are a great place to start if you’re a beginner. This section will help you gain the basic skills you need to start using the library.\n    \n*   **HOW-TO GUIDES** show you how to achieve a specific goal, like finetuning a pretrained model for language modeling or how to write and share a custom model.\n    \n*   **CONCEPTUAL GUIDES** offers more discussion and explanation of the underlying concepts and ideas behind models, tasks, and the design philosophy of 🤗 Transformers.\n    \n*   **API** describes all classes and functions:\n    \n    *   **MAIN CLASSES** details the most important classes like configuration, model, tokenizer, and pipeline.\n    *   **MODELS** details the classes and functions related to each model implemented in the library.\n    *   **INTERNAL HELPERS** details utility classes and functions used internally.\n\n[](https://huggingface.co/docs/transformers/index#supported-models-and-frameworks)Supported models and frameworks\n-----------------------------------------------------------------------------------------------------------------\n\nThe table below represents the current support in the library for each of those models, whether they have a Python tokenizer (called “slow”). A “fast” tokenizer backed by the 🤗 Tokenizers library, whether they have support in Jax (via Flax), PyTorch, and/or TensorFlow.\n\n| Model | PyTorch support | TensorFlow support | Flax Support |\n| --- | --- | --- | --- |\n| [ALBERT](https://huggingface.co/docs/transformers/model_doc/albert) | ✅ | ✅ | ✅ |\n| [ALIGN](https://huggingface.co/docs/transformers/model_doc/align) | ✅ | ❌ | ❌ |\n| [AltCLIP](https://huggingface.co/docs/transformers/model_doc/altclip) | ✅ | ❌ | ❌ |\n| [Aria](https://huggingface.co/docs/transformers/model_doc/aria) | ✅ | ❌ | ❌ |\n| [AriaText](https://huggingface.co/docs/transformers/model_doc/aria_text) | ✅ | ❌ | ❌ |\n| [Audio Spectrogram Transformer](https://huggingface.co/docs/transformers/model_doc/audio-spectrogram-transformer) | ✅ | ❌ | ❌ |\n| [Autoformer](https://huggingface.co/docs/transformers/model_doc/autoformer) | ✅ | ❌ | ❌ |\n| [Bamba](https://huggingface.co/docs/transformers/model_doc/bamba) | ✅ | ❌ | ❌ |\n| [Bark](https://huggingface.co/docs/transformers/model_doc/bark) | ✅ | ❌ | ❌ |\n| [BART](https://huggingface.co/docs/transformers/model_doc/bart) | ✅ | ✅ | ✅ |\n| [BARThez](https://huggingface.co/docs/transformers/model_doc/barthez) | ✅ | ✅ | ✅ |\n| [BARTpho](https://huggingface.co/docs/transformers/model_doc/bartpho) | ✅ | ✅ | ✅ |\n| [BEiT](https://huggingface.co/docs/transformers/model_doc/beit) | ✅ | ❌ | ✅ |\n| [BERT](https://huggingface.co/docs/transformers/model_doc/bert) | ✅ | ✅ | ✅ |\n| [Bert Generation](https://huggingface.co/docs/transformers/model_doc/bert-generation) | ✅ | ❌ | ❌ |\n| [BertJapanese](https://huggingface.co/docs/transformers/model_doc/bert-japanese) | ✅ | ✅ | ✅ |\n| [BERTweet](https://huggingface.co/docs/transformers/model_doc/bertweet) | ✅ | ✅ | ✅ |\n| [BigBird](https://huggingface.co/docs/transformers/model_doc/big_bird) | ✅ | ❌ | ✅ |\n| [BigBird-Pegasus](https://huggingface.co/docs/transformers/model_doc/bigbird_pegasus) | ✅ | ❌ | ❌ |\n| [BioGpt](https://huggingface.co/docs/transformers/model_doc/biogpt) | ✅ | ❌ | ❌ |\n| [BiT](https://huggingface.co/docs/transformers/model_doc/bit) | ✅ | ❌ | ❌ |\n| [Blenderbot](https://huggingface.co/docs/transformers/model_doc/blenderbot) | ✅ | ✅ | ✅ |\n| [BlenderbotSmall](https://huggingface.co/docs/transformers/model_doc/blenderbot-small) | ✅ | ✅ | ✅ |\n| [BLIP](https://huggingface.co/docs/transformers/model_doc/blip) | ✅ | ✅ | ❌ |\n| [BLIP-2](https://huggingface.co/docs/transformers/model_doc/blip-2) | ✅ | ❌ | ❌ |\n| [BLOOM](https://huggingface.co/docs/transformers/model_doc/bloom) | ✅ | ❌ | ✅ |\n| [BORT](https://huggingface.co/docs/transformers/model_doc/bort) | ✅ | ✅ | ✅ |\n| [BridgeTower](https://huggingface.co/docs/transformers/model_doc/bridgetower) | ✅ | ❌ | ❌ |\n| [BROS](https://huggingface.co/docs/transformers/model_doc/bros) | ✅ | ❌ | ❌ |\n| [ByT5](https://huggingface.co/docs/transformers/model_doc/byt5) | ✅ | ✅ | ✅ |\n| [CamemBERT](https://huggingface.co/docs/transformers/model_doc/camembert) | ✅ | ✅ | ❌ |\n| [CANINE](https://huggingface.co/docs/transformers/model_doc/canine) | ✅ | ❌ | ❌ |\n| [Chameleon](https://huggingface.co/docs/transformers/model_doc/chameleon) | ✅ | ❌ | ❌ |\n| [Chinese-CLIP](https://huggingface.co/docs/transformers/model_doc/chinese_clip) | ✅ | ❌ | ❌ |\n| [CLAP](https://huggingface.co/docs/transformers/model_doc/clap) | ✅ | ❌ | ❌ |\n| [CLIP](https://huggingface.co/docs/transformers/model_doc/clip) | ✅ | ✅ | ✅ |\n| [CLIPSeg](https://huggingface.co/docs/transformers/model_doc/clipseg) | ✅ | ❌ | ❌ |\n| [CLVP](https://huggingface.co/docs/transformers/model_doc/clvp) | ✅ | ❌ | ❌ |\n| [CodeGen](https://huggingface.co/docs/transformers/model_doc/codegen) | ✅ | ❌ | ❌ |\n| [CodeLlama](https://huggingface.co/docs/transformers/model_doc/code_llama) | ✅ | ❌ | ✅ |\n| [Cohere](https://huggingface.co/docs/transformers/model_doc/cohere) | ✅ | ❌ | ❌ |\n| [Cohere2](https://huggingface.co/docs/transformers/model_doc/cohere2) | ✅ | ❌ | ❌ |\n| [ColPali](https://huggingface.co/docs/transformers/model_doc/colpali) | ✅ | ❌ | ❌ |\n| [Conditional DETR](https://huggingface.co/docs/transformers/model_doc/conditional_detr) | ✅ | ❌ | ❌ |\n| [ConvBERT](https://huggingface.co/docs/transformers/model_doc/convbert) | ✅ | ✅ | ❌ |\n| [ConvNeXT](https://huggingface.co/docs/transformers/model_doc/convnext) | ✅ | ✅ | ❌ |\n| [ConvNeXTV2](https://huggingface.co/docs/transformers/model_doc/convnextv2) | ✅ | ✅ | ❌ |\n| [CPM](https://huggingface.co/docs/transformers/model_doc/cpm) | ✅ | ✅ | ✅ |\n| [CPM-Ant](https://huggingface.co/docs/transformers/model_doc/cpmant) | ✅ | ❌ | ❌ |\n| [CTRL](https://huggingface.co/docs/transformers/model_doc/ctrl) | ✅ | ✅ | ❌ |\n| [CvT](https://huggingface.co/docs/transformers/model_doc/cvt) | ✅ | ✅ | ❌ |\n| [DAC](https://huggingface.co/docs/transformers/model_doc/dac) | ✅ | ❌ | ❌ |\n| [Data2VecAudio](https://huggingface.co/docs/transformers/model_doc/data2vec) | ✅ | ❌ | ❌ |\n| [Data2VecText](https://huggingface.co/docs/transformers/model_doc/data2vec) | ✅ | ❌ | ❌ |\n| [Data2VecVision](https://huggingface.co/docs/transformers/model_doc/data2vec) | ✅ | ✅ | ❌ |\n| [DBRX](https://huggingface.co/docs/transformers/model_doc/dbrx) | ✅ | ❌ | ❌ |\n| [DeBERTa](https://huggingface.co/docs/transformers/model_doc/deberta) | ✅ | ✅ | ❌ |\n| [DeBERTa-v2](https://huggingface.co/docs/transformers/model_doc/deberta-v2) | ✅ | ✅ | ❌ |\n| [Decision Transformer](https://huggingface.co/docs/transformers/model_doc/decision_transformer) | ✅ | ❌ | ❌ |\n| [Deformable DETR](https://huggingface.co/docs/transformers/model_doc/deformable_detr) | ✅ | ❌ | ❌ |\n| [DeiT](https://huggingface.co/docs/transformers/model_doc/deit) | ✅ | ✅ | ❌ |\n| [DePlot](https://huggingface.co/docs/transformers/model_doc/deplot) | ✅ | ❌ | ❌ |\n| [Depth Anything](https://huggingface.co/docs/transformers/model_doc/depth_anything) | ✅ | ❌ | ❌ |\n| [DETA](https://huggingface.co/docs/transformers/model_doc/deta) | ✅ | ❌ | ❌ |\n| [DETR](https://huggingface.co/docs/transformers/model_doc/detr) | ✅ | ❌ | ❌ |\n| [DialoGPT](https://huggingface.co/docs/transformers/model_doc/dialogpt) | ✅ | ✅ | ✅ |\n| [DiffLlama](https://huggingface.co/docs/transformers/model_doc/diffllama) | ✅ | ❌ | ❌ |\n| [DiNAT](https://huggingface.co/docs/transformers/model_doc/dinat) | ✅ | ❌ | ❌ |\n| [DINOv2](https://huggingface.co/docs/transformers/model_doc/dinov2) | ✅ | ❌ | ✅ |\n| [DINOv2 with Registers](https://huggingface.co/docs/transformers/model_doc/dinov2_with_registers) | ✅ | ❌ | ❌ |\n| [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert) | ✅ | ✅ | ✅ |\n| [DiT](https://huggingface.co/docs/transformers/model_doc/dit) | ✅ | ❌ | ✅ |\n| [DonutSwin](https://huggingface.co/docs/transformers/model_doc/donut) | ✅ | ❌ | ❌ |\n| [DPR](https://huggingface.co/docs/transformers/model_doc/dpr) | ✅ | ✅ | ❌ |\n| [DPT](https://huggingface.co/docs/transformers/model_doc/dpt) | ✅ | ❌ | ❌ |\n| [EfficientFormer](https://huggingface.co/docs/transformers/model_doc/efficientformer) | ✅ | ✅ | ❌ |\n| [EfficientNet](https://huggingface.co/docs/transformers/model_doc/efficientnet) | ✅ | ❌ | ❌ |\n| [ELECTRA](https://huggingface.co/docs/transformers/model_doc/electra) | ✅ | ✅ | ✅ |\n| [Emu3](https://huggingface.co/docs/transformers/model_doc/emu3) | ✅ | ❌ | ❌ |\n| [EnCodec](https://huggingface.co/docs/transformers/model_doc/encodec) | ✅ | ❌ | ❌ |\n| [Encoder decoder](https://huggingface.co/docs/transformers/model_doc/encoder-decoder) | ✅ | ✅ | ✅ |\n| [ERNIE](https://huggingface.co/docs/transformers/model_doc/ernie) | ✅ | ❌ | ❌ |\n| [ErnieM](https://huggingface.co/docs/transformers/model_doc/ernie_m) | ✅ | ❌ | ❌ |\n| [ESM](https://huggingface.co/docs/transformers/model_doc/esm) | ✅ | ✅ | ❌ |\n| [FairSeq Machine-Translation](https://huggingface.co/docs/transformers/model_doc/fsmt) | ✅ | ❌ | ❌ |\n| [Falcon](https://huggingface.co/docs/transformers/model_doc/falcon) | ✅ | ❌ | ❌ |\n| [Falcon3](https://huggingface.co/docs/transformers/model_doc/falcon3) | ✅ | ❌ | ✅ |\n| [FalconMamba](https://huggingface.co/docs/transformers/model_doc/falcon_mamba) | ✅ | ❌ | ❌ |\n| [FastSpeech2Conformer](https://huggingface.co/docs/transformers/model_doc/fastspeech2_conformer) | ✅ | ❌ | ❌ |\n| [FLAN-T5](https://huggingface.co/docs/transformers/model_doc/flan-t5) | ✅ | ✅ | ✅ |\n| [FLAN-UL2](https://huggingface.co/docs/transformers/model_doc/flan-ul2) | ✅ | ✅ | ✅ |\n| [FlauBERT](https://huggingface.co/docs/transformers/model_doc/flaubert) | ✅ | ✅ | ❌ |\n| [FLAVA](https://huggingface.co/docs/transformers/model_doc/flava) | ✅ | ❌ | ❌ |\n| [FNet](https://huggingface.co/docs/transformers/model_doc/fnet) | ✅ | ❌ | ❌ |\n| [FocalNet](https://huggingface.co/docs/transformers/model_doc/focalnet) | ✅ | ❌ | ❌ |\n| [Funnel Transformer](https://huggingface.co/docs/transformers/model_doc/funnel) | ✅ | ✅ | ❌ |\n| [Fuyu](https://huggingface.co/docs/transformers/model_doc/fuyu) | ✅ | ❌ | ❌ |\n| [Gemma](https://huggingface.co/docs/transformers/model_doc/gemma) | ✅ | ❌ | ✅ |\n| [Gemma2](https://huggingface.co/docs/transformers/model_doc/gemma2) | ✅ | ❌ | ❌ |\n| [GIT](https://huggingface.co/docs/transformers/model_doc/git) | ✅ | ❌ | ❌ |\n| [GLM](https://huggingface.co/docs/transformers/model_doc/glm) | ✅ | ❌ | ❌ |\n| [GLPN](https://huggingface.co/docs/transformers/model_doc/glpn) | ✅ | ❌ | ❌ |\n| [GPT Neo](https://huggingface.co/docs/transformers/model_doc/gpt_neo) | ✅ | ❌ | ✅ |\n| [GPT NeoX](https://huggingface.co/docs/transformers/model_doc/gpt_neox) | ✅ | ❌ | ❌ |\n| [GPT NeoX Japanese](https://huggingface.co/docs/transformers/model_doc/gpt_neox_japanese) | ✅ | ❌ | ❌ |\n| [GPT-J](https://huggingface.co/docs/transformers/model_doc/gptj) | ✅ | ✅ | ✅ |\n| [GPT-Sw3](https://huggingface.co/docs/transformers/model_doc/gpt-sw3) | ✅ | ✅ | ✅ |\n| [GPTBigCode](https://huggingface.co/docs/transformers/model_doc/gpt_bigcode) | ✅ | ❌ | ❌ |\n| [GPTSAN-japanese](https://huggingface.co/docs/transformers/model_doc/gptsan-japanese) | ✅ | ❌ | ❌ |\n| [Granite](https://huggingface.co/docs/transformers/model_doc/granite) | ✅ | ❌ | ❌ |\n| [GraniteMoeMoe](https://huggingface.co/docs/transformers/model_doc/granitemoe) | ✅ | ❌ | ❌ |\n| [Graphormer](https://huggingface.co/docs/transformers/model_doc/graphormer) | ✅ | ❌ | ❌ |\n| [Grounding DINO](https://huggingface.co/docs/transformers/model_doc/grounding-dino) | ✅ | ❌ | ❌ |\n| [GroupViT](https://huggingface.co/docs/transformers/model_doc/groupvit) | ✅ | ✅ | ❌ |\n| [HerBERT](https://huggingface.co/docs/transformers/model_doc/herbert) | ✅ | ✅ | ✅ |\n| [Hiera](https://huggingface.co/docs/transformers/model_doc/hiera) | ✅ | ❌ | ❌ |\n| [Hubert](https://huggingface.co/docs/transformers/model_doc/hubert) | ✅ | ✅ | ❌ |\n| [I-BERT](https://huggingface.co/docs/transformers/model_doc/ibert) | ✅ | ❌ | ❌ |\n| [I-JEPA](https://huggingface.co/docs/transformers/model_doc/ijepa) | ✅ | ❌ | ❌ |\n| [IDEFICS](https://huggingface.co/docs/transformers/model_doc/idefics) | ✅ | ✅ | ❌ |\n| [Idefics2](https://huggingface.co/docs/transformers/model_doc/idefics2) | ✅ | ❌ | ❌ |\n| [Idefics3](https://huggingface.co/docs/transformers/model_doc/idefics3) | ✅ | ❌ | ❌ |\n| [Idefics3VisionTransformer](https://huggingface.co/docs/transformers/model_doc/idefics3_vision) | ❌ | ❌ | ❌ |\n| [ImageGPT](https://huggingface.co/docs/transformers/model_doc/imagegpt) | ✅ | ❌ | ❌ |\n| [Informer](https://huggingface.co/docs/transformers/model_doc/informer) | ✅ | ❌ | ❌ |\n| [InstructBLIP](https://huggingface.co/docs/transformers/model_doc/instructblip) | ✅ | ❌ | ❌ |\n| [InstructBlipVideo](https://huggingface.co/docs/transformers/model_doc/instructblipvideo) | ✅ | ❌ | ❌ |\n| [Jamba](https://huggingface.co/docs/transformers/model_doc/jamba) | ✅ | ❌ | ❌ |\n| [JetMoe](https://huggingface.co/docs/transformers/model_doc/jetmoe) | ✅ | ❌ | ❌ |\n| [Jukebox](https://huggingface.co/docs/transformers/model_doc/jukebox) | ✅ | ❌ | ❌ |\n| [KOSMOS-2](https://huggingface.co/docs/transformers/model_doc/kosmos-2) | ✅ | ❌ | ❌ |\n| [LayoutLM](https://huggingface.co/docs/transformers/model_doc/layoutlm) | ✅ | ✅ | ❌ |\n| [LayoutLMv2](https://huggingface.co/docs/transformers/model_doc/layoutlmv2) | ✅ | ❌ | ❌ |\n| [LayoutLMv3](https://huggingface.co/docs/transformers/model_doc/layoutlmv3) | ✅ | ✅ | ❌ |\n| [LayoutXLM](https://huggingface.co/docs/transformers/model_doc/layoutxlm) | ✅ | ❌ | ❌ |\n| [LED](https://huggingface.co/docs/transformers/model_doc/led) | ✅ | ✅ | ❌ |\n| [LeViT](https://huggingface.co/docs/transformers/model_doc/levit) | ✅ | ❌ | ❌ |\n| [LiLT](https://huggingface.co/docs/transformers/model_doc/lilt) | ✅ | ❌ | ❌ |\n| [LLaMA](https://huggingface.co/docs/transformers/model_doc/llama) | ✅ | ❌ | ✅ |\n| [Llama2](https://huggingface.co/docs/transformers/model_doc/llama2) | ✅ | ❌ | ✅ |\n| [Llama3](https://huggingface.co/docs/transformers/model_doc/llama3) | ✅ | ❌ | ✅ |\n| [LLaVa](https://huggingface.co/docs/transformers/model_doc/llava) | ✅ | ❌ | ❌ |\n| [LLaVA-NeXT](https://huggingface.co/docs/transformers/model_doc/llava_next) | ✅ | ❌ | ❌ |\n| [LLaVa-NeXT-Video](https://huggingface.co/docs/transformers/model_doc/llava_next_video) | ✅ | ❌ | ❌ |\n| [LLaVA-Onevision](https://huggingface.co/docs/transformers/model_doc/llava_onevision) | ✅ | ❌ | ❌ |\n| [Longformer](https://huggingface.co/docs/transformers/model_doc/longformer) | ✅ | ✅ | ❌ |\n| [LongT5](https://huggingface.co/docs/transformers/model_doc/longt5) | ✅ | ❌ | ✅ |\n| [LUKE](https://huggingface.co/docs/transformers/model_doc/luke) | ✅ | ❌ | ❌ |\n| [LXMERT](https://huggingface.co/docs/transformers/model_doc/lxmert) | ✅ | ✅ | ❌ |\n| [M-CTC-T](https://huggingface.co/docs/transformers/model_doc/mctct) | ✅ | ❌ | ❌ |\n| [M2M100](https://huggingface.co/docs/transformers/model_doc/m2m_100) | ✅ | ❌ | ❌ |\n| [MADLAD-400](https://huggingface.co/docs/transformers/model_doc/madlad-400) | ✅ | ✅ | ✅ |\n| [Mamba](https://huggingface.co/docs/transformers/model_doc/mamba) | ✅ | ❌ | ❌ |\n| [mamba2](https://huggingface.co/docs/transformers/model_doc/mamba2) | ✅ | ❌ | ❌ |\n| [Marian](https://huggingface.co/docs/transformers/model_doc/marian) | ✅ | ✅ | ✅ |\n| [MarkupLM](https://huggingface.co/docs/transformers/model_doc/markuplm) | ✅ | ❌ | ❌ |\n| [Mask2Former](https://huggingface.co/docs/transformers/model_doc/mask2former) | ✅ | ❌ | ❌ |\n| [MaskFormer](https://huggingface.co/docs/transformers/model_doc/maskformer) | ✅ | ❌ | ❌ |\n| [MatCha](https://huggingface.co/docs/transformers/model_doc/matcha) | ✅ | ❌ | ❌ |\n| [mBART](https://huggingface.co/docs/transformers/model_doc/mbart) | ✅ | ✅ | ✅ |\n| [mBART-50](https://huggingface.co/docs/transformers/model_doc/mbart50) | ✅ | ✅ | ✅ |\n| [MEGA](https://huggingface.co/docs/transformers/model_doc/mega) | ✅ | ❌ | ❌ |\n| [Megatron-BERT](https://huggingface.co/docs/transformers/model_doc/megatron-bert) | ✅ | ❌ | ❌ |\n| [Megatron-GPT2](https://huggingface.co/docs/transformers/model_doc/megatron_gpt2) | ✅ | ✅ | ✅ |\n| [MGP-STR](https://huggingface.co/docs/transformers/model_doc/mgp-str) | ✅ | ❌ | ❌ |\n| [Mimi](https://huggingface.co/docs/transformers/model_doc/mimi) | ✅ | ❌ | ❌ |\n| [Mistral](https://huggingface.co/docs/transformers/model_doc/mistral) | ✅ | ✅ | ✅ |\n| [Mixtral](https://huggingface.co/docs/transformers/model_doc/mixtral) | ✅ | ❌ | ❌ |\n| [Mllama](https://huggingface.co/docs/transformers/model_doc/mllama) | ✅ | ❌ | ❌ |\n| [mLUKE](https://huggingface.co/docs/transformers/model_doc/mluke) | ✅ | ❌ | ❌ |\n| [MMS](https://huggingface.co/docs/transformers/model_doc/mms) | ✅ | ✅ | ✅ |\n| [MobileBERT](https://huggingface.co/docs/transformers/model_doc/mobilebert) | ✅ | ✅ | ❌ |\n| [MobileNetV1](https://huggingface.co/docs/transformers/model_doc/mobilenet_v1) | ✅ | ❌ | ❌ |\n| [MobileNetV2](https://huggingface.co/docs/transformers/model_doc/mobilenet_v2) | ✅ | ❌ | ❌ |\n| [MobileViT](https://huggingface.co/docs/transformers/model_doc/mobilevit) | ✅ | ✅ | ❌ |\n| [MobileViTV2](https://huggingface.co/docs/transformers/model_doc/mobilevitv2) | ✅ | ❌ | ❌ |\n| [ModernBERT](https://huggingface.co/docs/transformers/model_doc/modernbert) | ✅ | ❌ | ❌ |\n| [Moonshine](https://huggingface.co/docs/transformers/model_doc/moonshine) | ✅ | ❌ | ❌ |\n| [Moshi](https://huggingface.co/docs/transformers/model_doc/moshi) | ✅ | ❌ | ❌ |\n| [MPNet](https://huggingface.co/docs/transformers/model_doc/mpnet) | ✅ | ✅ | ❌ |\n| [MPT](https://huggingface.co/docs/transformers/model_doc/mpt) | ✅ | ❌ | ❌ |\n| [MRA](https://huggingface.co/docs/transformers/model_doc/mra) | ✅ | ❌ | ❌ |\n| [MT5](https://huggingface.co/docs/transformers/model_doc/mt5) | ✅ | ✅ | ✅ |\n| [MusicGen](https://huggingface.co/docs/transformers/model_doc/musicgen) | ✅ | ❌ | ❌ |\n| [MusicGen Melody](https://huggingface.co/docs/transformers/model_doc/musicgen_melody) | ✅ | ❌ | ❌ |\n| [MVP](https://huggingface.co/docs/transformers/model_doc/mvp) | ✅ | ❌ | ❌ |\n| [NAT](https://huggingface.co/docs/transformers/model_doc/nat) | ✅ | ❌ | ❌ |\n| [Nemotron](https://huggingface.co/docs/transformers/model_doc/nemotron) | ✅ | ❌ | ❌ |\n| [Nezha](https://huggingface.co/docs/transformers/model_doc/nezha) | ✅ | ❌ | ❌ |\n| [NLLB](https://huggingface.co/docs/transformers/model_doc/nllb) | ✅ | ❌ | ❌ |\n| [NLLB-MOE](https://huggingface.co/docs/transformers/model_doc/nllb-moe) | ✅ | ❌ | ❌ |\n| [Nougat](https://huggingface.co/docs/transformers/model_doc/nougat) | ✅ | ✅ | ✅ |\n| [Nyströmformer](https://huggingface.co/docs/transformers/model_doc/nystromformer) | ✅ | ❌ | ❌ |\n| [OLMo](https://huggingface.co/docs/transformers/model_doc/olmo) | ✅ | ❌ | ❌ |\n| [OLMo2](https://huggingface.co/docs/transformers/model_doc/olmo2) | ✅ | ❌ | ❌ |\n| [OLMoE](https://huggingface.co/docs/transformers/model_doc/olmoe) | ✅ | ❌ | ❌ |\n| [OmDet-Turbo](https://huggingface.co/docs/transformers/model_doc/omdet-turbo) | ✅ | ❌ | ❌ |\n| [OneFormer](https://huggingface.co/docs/transformers/model_doc/oneformer) | ✅ | ❌ | ❌ |\n| [OpenAI GPT](https://huggingface.co/docs/transformers/model_doc/openai-gpt) | ✅ | ✅ | ❌ |\n| [OpenAI GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2) | ✅ | ✅ | ✅ |\n| [OpenLlama](https://huggingface.co/docs/transformers/model_doc/open-llama) | ✅ | ❌ | ❌ |\n| [OPT](https://huggingface.co/docs/transformers/model_doc/opt) | ✅ | ✅ | ✅ |\n| [OWL-ViT](https://huggingface.co/docs/transformers/model_doc/owlvit) | ✅ | ❌ | ❌ |\n| [OWLv2](https://huggingface.co/docs/transformers/model_doc/owlv2) | ✅ | ❌ | ❌ |\n| [PaliGemma](https://huggingface.co/docs/transformers/model_doc/paligemma) | ✅ | ❌ | ❌ |\n| [PatchTSMixer](https://huggingface.co/docs/transformers/model_doc/patchtsmixer) | ✅ | ❌ | ❌ |\n| [PatchTST](https://huggingface.co/docs/transformers/model_doc/patchtst) | ✅ | ❌ | ❌ |\n| [Pegasus](https://huggingface.co/docs/transformers/model_doc/pegasus) | ✅ | ✅ | ✅ |\n| [PEGASUS-X](https://huggingface.co/docs/transformers/model_doc/pegasus_x) | ✅ | ❌ | ❌ |\n| [Perceiver](https://huggingface.co/docs/transformers/model_doc/perceiver) | ✅ | ❌ | ❌ |\n| [Persimmon](https://huggingface.co/docs/transformers/model_doc/persimmon) | ✅ | ❌ | ❌ |\n| [Phi](https://huggingface.co/docs/transformers/model_doc/phi) | ✅ | ❌ | ❌ |\n| [Phi3](https://huggingface.co/docs/transformers/model_doc/phi3) | ✅ | ❌ | ❌ |\n| [Phimoe](https://huggingface.co/docs/transformers/model_doc/phimoe) | ✅ | ❌ | ❌ |\n| [PhoBERT](https://huggingface.co/docs/transformers/model_doc/phobert) | ✅ | ✅ | ✅ |\n| [Pix2Struct](https://huggingface.co/docs/transformers/model_doc/pix2struct) | ✅ | ❌ | ❌ |\n| [Pixtral](https://huggingface.co/docs/transformers/model_doc/pixtral) | ✅ | ❌ | ❌ |\n| [PLBart](https://huggingface.co/docs/transformers/model_doc/plbart) | ✅ | ❌ | ❌ |\n| [PoolFormer](https://huggingface.co/docs/transformers/model_doc/poolformer) | ✅ | ❌ | ❌ |\n| [Pop2Piano](https://huggingface.co/docs/transformers/model_doc/pop2piano) | ✅ | ❌ | ❌ |\n| [ProphetNet](https://huggingface.co/docs/transformers/model_doc/prophetnet) | ✅ | ❌ | ❌ |\n| [PVT](https://huggingface.co/docs/transformers/model_doc/pvt) | ✅ | ❌ | ❌ |\n| [PVTv2](https://huggingface.co/docs/transformers/model_doc/pvt_v2) | ✅ | ❌ | ❌ |\n| [QDQBert](https://huggingface.co/docs/transformers/model_doc/qdqbert) | ✅ | ❌ | ❌ |\n| [Qwen2](https://huggingface.co/docs/transformers/model_doc/qwen2) | ✅ | ❌ | ❌ |\n| [Qwen2Audio](https://huggingface.co/docs/transformers/model_doc/qwen2_audio) | ✅ | ❌ | ❌ |\n| [Qwen2MoE](https://huggingface.co/docs/transformers/model_doc/qwen2_moe) | ✅ | ❌ | ❌ |\n| [Qwen2VL](https://huggingface.co/docs/transformers/model_doc/qwen2_vl) | ✅ | ❌ | ❌ |\n| [RAG](https://huggingface.co/docs/transformers/model_doc/rag) | ✅ | ✅ | ❌ |\n| [REALM](https://huggingface.co/docs/transformers/model_doc/realm) | ✅ | ❌ | ❌ |\n| [RecurrentGemma](https://huggingface.co/docs/transformers/model_doc/recurrent_gemma) | ✅ | ❌ | ❌ |\n| [Reformer](https://huggingface.co/docs/transformers/model_doc/reformer) | ✅ | ❌ | ❌ |\n| [RegNet](https://huggingface.co/docs/transformers/model_doc/regnet) | ✅ | ✅ | ✅ |\n| [RemBERT](https://huggingface.co/docs/transformers/model_doc/rembert) | ✅ | ✅ | ❌ |\n| [ResNet](https://huggingface.co/docs/transformers/model_doc/resnet) | ✅ | ✅ | ✅ |\n| [RetriBERT](https://huggingface.co/docs/transformers/model_doc/retribert) | ✅ | ❌ | ❌ |\n| [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta) | ✅ | ✅ | ✅ |\n| [RoBERTa-PreLayerNorm](https://huggingface.co/docs/transformers/model_doc/roberta-prelayernorm) | ✅ | ✅ | ✅ |\n| [RoCBert](https://huggingface.co/docs/transformers/model_doc/roc_bert) | ✅ | ❌ | ❌ |\n| [RoFormer](https://huggingface.co/docs/transformers/model_doc/roformer) | ✅ | ✅ | ✅ |\n| [RT-DETR](https://huggingface.co/docs/transformers/model_doc/rt_detr) | ✅ | ❌ | ❌ |\n| [RT-DETR-ResNet](https://huggingface.co/docs/transformers/model_doc/rt_detr_resnet) | ✅ | ❌ | ❌ |\n| [RWKV](https://huggingface.co/docs/transformers/model_doc/rwkv) | ✅ | ❌ | ❌ |\n| [SAM](https://huggingface.co/docs/transformers/model_doc/sam) | ✅ | ✅ | ❌ |\n| [SeamlessM4T](https://huggingface.co/docs/transformers/model_doc/seamless_m4t) | ✅ | ❌ | ❌ |\n| [SeamlessM4Tv2](https://huggingface.co/docs/transformers/model_doc/seamless_m4t_v2) | ✅ | ❌ | ❌ |\n| [SegFormer](https://huggingface.co/docs/transformers/model_doc/segformer) | ✅ | ✅ | ❌ |\n| [SegGPT](https://huggingface.co/docs/transformers/model_doc/seggpt) | ✅ | ❌ | ❌ |\n| [SEW](https://huggingface.co/docs/transformers/model_doc/sew) | ✅ | ❌ | ❌ |\n| [SEW-D](https://huggingface.co/docs/transformers/model_doc/sew-d) | ✅ | ❌ | ❌ |\n| [SigLIP](https://huggingface.co/docs/transformers/model_doc/siglip) | ✅ | ❌ | ❌ |\n| [Speech Encoder decoder](https://huggingface.co/docs/transformers/model_doc/speech-encoder-decoder) | ✅ | ❌ | ✅ |\n| [Speech2Text](https://huggingface.co/docs/transformers/model_doc/speech_to_text) | ✅ | ✅ | ❌ |\n| [SpeechT5](https://huggingface.co/docs/transformers/model_doc/speecht5) | ✅ | ❌ | ❌ |\n| [Splinter](https://huggingface.co/docs/transformers/model_doc/splinter) | ✅ | ❌ | ❌ |\n| [SqueezeBERT](https://huggingface.co/docs/transformers/model_doc/squeezebert) | ✅ | ❌ | ❌ |\n| [StableLm](https://huggingface.co/docs/transformers/model_doc/stablelm) | ✅ | ❌ | ❌ |\n| [Starcoder2](https://huggingface.co/docs/transformers/model_doc/starcoder2) | ✅ | ❌ | ❌ |\n| [SuperPoint](https://huggingface.co/docs/transformers/model_doc/superpoint) | ✅ | ❌ | ❌ |\n| [SwiftFormer](https://huggingface.co/docs/transformers/model_doc/swiftformer) | ✅ | ✅ | ❌ |\n| [Swin Transformer](https://huggingface.co/docs/transformers/model_doc/swin) | ✅ | ✅ | ❌ |\n| [Swin Transformer V2](https://huggingface.co/docs/transformers/model_doc/swinv2) | ✅ | ❌ | ❌ |\n| [Swin2SR](https://huggingface.co/docs/transformers/model_doc/swin2sr) | ✅ | ❌ | ❌ |\n| [SwitchTransformers](https://huggingface.co/docs/transformers/model_doc/switch_transformers) | ✅ | ❌ | ❌ |\n| [T5](https://huggingface.co/docs/transformers/model_doc/t5) | ✅ | ✅ | ✅ |\n| [T5v1.1](https://huggingface.co/docs/transformers/model_doc/t5v1.1) | ✅ | ✅ | ✅ |\n| [Table Transformer](https://huggingface.co/docs/transformers/model_doc/table-transformer) | ✅ | ❌ | ❌ |\n| [TAPAS](https://huggingface.co/docs/transformers/model_doc/tapas) | ✅ | ✅ | ❌ |\n| [TAPEX](https://huggingface.co/docs/transformers/model_doc/tapex) | ✅ | ✅ | ✅ |\n| [TextNet](https://huggingface.co/docs/transformers/model_doc/textnet) | ✅ | ❌ | ❌ |\n| [Time Series Transformer](https://huggingface.co/docs/transformers/model_doc/time_series_transformer) | ✅ | ❌ | ❌ |\n| [TimeSformer](https://huggingface.co/docs/transformers/model_doc/timesformer) | ✅ | ❌ | ❌ |\n| [TimmWrapperModel](https://huggingface.co/docs/transformers/model_doc/timm_wrapper) | ✅ | ❌ | ❌ |\n| [Trajectory Transformer](https://huggingface.co/docs/transformers/model_doc/trajectory_transformer) | ✅ | ❌ | ❌ |\n| [Transformer-XL](https://huggingface.co/docs/transformers/model_doc/transfo-xl) | ✅ | ✅ | ❌ |\n| [TrOCR](https://huggingface.co/docs/transformers/model_doc/trocr) | ✅ | ❌ | ❌ |\n| [TVLT](https://huggingface.co/docs/transformers/model_doc/tvlt) | ✅ | ❌ | ❌ |\n| [TVP](https://huggingface.co/docs/transformers/model_doc/tvp) | ✅ | ❌ | ❌ |\n| [UDOP](https://huggingface.co/docs/transformers/model_doc/udop) | ✅ | ❌ | ❌ |\n| [UL2](https://huggingface.co/docs/transformers/model_doc/ul2) | ✅ | ✅ | ✅ |\n| [UMT5](https://huggingface.co/docs/transformers/model_doc/umt5) | ✅ | ❌ | ❌ |\n| [UniSpeech](https://huggingface.co/docs/transformers/model_doc/unispeech) | ✅ | ❌ | ❌ |\n| [UniSpeechSat](https://huggingface.co/docs/transformers/model_doc/unispeech-sat) | ✅ | ❌ | ❌ |\n| [UnivNet](https://huggingface.co/docs/transformers/model_doc/univnet) | ✅ | ❌ | ❌ |\n| [UPerNet](https://huggingface.co/docs/transformers/model_doc/upernet) | ✅ | ❌ | ❌ |\n| [VAN](https://huggingface.co/docs/transformers/model_doc/van) | ✅ | ❌ | ❌ |\n| [VideoLlava](https://huggingface.co/docs/transformers/model_doc/video_llava) | ✅ | ❌ | ❌ |\n| [VideoMAE](https://huggingface.co/docs/transformers/model_doc/videomae) | ✅ | ❌ | ❌ |\n| [ViLT](https://huggingface.co/docs/transformers/model_doc/vilt) | ✅ | ❌ | ❌ |\n| [VipLlava](https://huggingface.co/docs/transformers/model_doc/vipllava) | ✅ | ❌ | ❌ |\n| [Vision Encoder decoder](https://huggingface.co/docs/transformers/model_doc/vision-encoder-decoder) | ✅ | ✅ | ✅ |\n| [VisionTextDualEncoder](https://huggingface.co/docs/transformers/model_doc/vision-text-dual-encoder) | ✅ | ✅ | ✅ |\n| [VisualBERT](https://huggingface.co/docs/transformers/model_doc/visual_bert) | ✅ | ❌ | ❌ |\n| [ViT](https://huggingface.co/docs/transformers/model_doc/vit) | ✅ | ✅ | ✅ |\n| [ViT Hybrid](https://huggingface.co/docs/transformers/model_doc/vit_hybrid) | ✅ | ❌ | ❌ |\n| [VitDet](https://huggingface.co/docs/transformers/model_doc/vitdet) | ✅ | ❌ | ❌ |\n| [ViTMAE](https://huggingface.co/docs/transformers/model_doc/vit_mae) | ✅ | ✅ | ❌ |\n| [ViTMatte](https://huggingface.co/docs/transformers/model_doc/vitmatte) | ✅ | ❌ | ❌ |\n| [ViTMSN](https://huggingface.co/docs/transformers/model_doc/vit_msn) | ✅ | ❌ | ❌ |\n| [VitPose](https://huggingface.co/docs/transformers/model_doc/vitpose) | ✅ | ❌ | ❌ |\n| [VitPoseBackbone](https://huggingface.co/docs/transformers/model_doc/vitpose_backbone) | ✅ | ❌ | ❌ |\n| [VITS](https://huggingface.co/docs/transformers/model_doc/vits) | ✅ | ❌ | ❌ |\n| [ViViT](https://huggingface.co/docs/transformers/model_doc/vivit) | ✅ | ❌ | ❌ |\n| [Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2) | ✅ | ✅ | ✅ |\n| [Wav2Vec2-BERT](https://huggingface.co/docs/transformers/model_doc/wav2vec2-bert) | ✅ | ❌ | ❌ |\n| [Wav2Vec2-Conformer](https://huggingface.co/docs/transformers/model_doc/wav2vec2-conformer) | ✅ | ❌ | ❌ |\n| [Wav2Vec2Phoneme](https://huggingface.co/docs/transformers/model_doc/wav2vec2_phoneme) | ✅ | ✅ | ✅ |\n| [WavLM](https://huggingface.co/docs/transformers/model_doc/wavlm) | ✅ | ❌ | ❌ |\n| [Whisper](https://huggingface.co/docs/transformers/model_doc/whisper) | ✅ | ✅ | ✅ |\n| [X-CLIP](https://huggingface.co/docs/transformers/model_doc/xclip) | ✅ | ❌ | ❌ |\n| [X-MOD](https://huggingface.co/docs/transformers/model_doc/xmod) | ✅ | ❌ | ❌ |\n| [XGLM](https://huggingface.co/docs/transformers/model_doc/xglm) | ✅ | ✅ | ✅ |\n| [XLM](https://huggingface.co/docs/transformers/model_doc/xlm) | ✅ | ✅ | ❌ |\n| [XLM-ProphetNet](https://huggingface.co/docs/transformers/model_doc/xlm-prophetnet) | ✅ | ❌ | ❌ |\n| [XLM-RoBERTa](https://huggingface.co/docs/transformers/model_doc/xlm-roberta) | ✅ | ✅ | ✅ |\n| [XLM-RoBERTa-XL](https://huggingface.co/docs/transformers/model_doc/xlm-roberta-xl) | ✅ | ❌ | ❌ |\n| [XLM-V](https://huggingface.co/docs/transformers/model_doc/xlm-v) | ✅ | ✅ | ✅ |\n| [XLNet](https://huggingface.co/docs/transformers/model_doc/xlnet) | ✅ | ✅ | ❌ |\n| [XLS-R](https://huggingface.co/docs/transformers/model_doc/xls_r) | ✅ | ✅ | ✅ |\n| [XLSR-Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/xlsr_wav2vec2) | ✅ | ✅ | ✅ |\n| [YOLOS](https://huggingface.co/docs/transformers/model_doc/yolos) | ✅ | ❌ | ❌ |\n| [YOSO](https://huggingface.co/docs/transformers/model_doc/yoso) | ✅ | ❌ | ❌ |\n| [Zamba](https://huggingface.co/docs/transformers/model_doc/zamba) | ✅ | ❌ | ❌ |\n| [ZoeDepth](https://huggingface.co/docs/transformers/model_doc/zoedepth) | ✅ | ❌ | ❌ |\n\n[< \\> Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/index.md)",
  "usage": {
    "tokens": 11334
  }
}
```
