---
title: GitHub - zjunlp/DeepKE: [EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction
description: [EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction - zjunlp/DeepKE
url: https://github.com/zjunlp/DeepKE
timestamp: 2025-01-20T15:30:53.653Z
domain: github.com
path: zjunlp_DeepKE
---

# GitHub - zjunlp/DeepKE: [EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction


[EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction - zjunlp/DeepKE


## Content

[![Image 33](https://github.com/zjunlp/DeepKE/raw/main/pics/logo.png)](https://github.com/zjunlp/deepke)

[![Image 34: Documentation](https://camo.githubusercontent.com/19a35f9199add02f187a6033ed1fd37e636cc1e6c53d2605a061477a2514fac0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f64656d6f2d776562736974652d626c7565)](http://deepke.zjukg.cn/)[![Image 35: PyPI](https://camo.githubusercontent.com/1524eb2918e69efd21aded0a9dc90656105a8eb51d984b35f969de83ec2a48d4/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646565706b65)](https://pypi.org/project/deepke/#files)[![Image 36: GitHub](https://camo.githubusercontent.com/4e14f3c4ee10ac6f469184b93cc80833a25212b271135bfceb00b3a0e4ba826c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7a6a756e6c702f646565706b65)](https://github.com/zjunlp/DeepKE/blob/master/LICENSE)[![Image 37: Documentation](https://camo.githubusercontent.com/c90615cb62b7bd62502aacdbca14d1c9ba0dc323573c9d7b7aca2dfa8ae9a933/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f632d776562736974652d726564)](http://zjunlp.github.io/DeepKE)[![Image 38: Open In Colab](https://camo.githubusercontent.com/96889048f8a9014fdeba2a891f97150c6aac6e723f5190236b10215a97ed41f3/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1vS8YJhJltzw3hpJczPt24O0Azcs3ZpRi?usp=sharing)

**English | [简体中文](https://github.com/zjunlp/DeepKE/blob/main/README_CN.md)**

A Deep Learning Based Knowledge Extraction Toolkit  
for Knowledge Graph Construction


---------------------------------------------------------------------------------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#----a-deep-learning-based-knowledge-extraction-toolkitfor-knowledge-graph-construction)

[DeepKE](https://arxiv.org/pdf/2201.03335.pdf) is a knowledge extraction toolkit for knowledge graph construction supporting **cnSchema**，**low-resource**, **document-level** and **multimodal** scenarios for _entity_, _relation_ and _attribute_ extraction. We provide [documents](https://zjunlp.github.io/DeepKE/), [online demo](http://deepke.zjukg.cn/), [paper](https://arxiv.org/pdf/2201.03335.pdf), [slides](https://drive.google.com/file/d/1IIeIZAbVduemqXc4zD40FUMoPHCJinLy/view?usp=sharing) and [poster](https://drive.google.com/file/d/1vd7xVHlWzoAxivN4T5qKrcqIGDcSM1_7/view?usp=sharing) for beginners.

*   ❗Want to use **Large Language Models** with DeepKE? Try [DeepKE-LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) and [OneKE](https://github.com/zjunlp/DeepKE/blob/main/example/llm/OneKE.md), have fun!
*   ❗Want to train supervised models? Try [Quick Start](https://github.com/zjunlp/DeepKE?screenshot=true#quick-start), we provide the NER models (e.g, [LightNER(COLING'22)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/few-shot), [W2NER(AAAI'22)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/standard/w2ner)), relation extraction models (e.g., [KnowPrompt(WWW'22)](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot)), relational triple extraction models (e.g., [ASP(EMNLP'22)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/ASP), [PRGC(ACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PRGC), [PURE(NAACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PURE)), and release off-the-shelf models at [DeepKE-cnSchema](https://github.com/zjunlp/DeepKE/tree/main/example/triple/cnschema), have fun!
*   We recommend using Linux; if using Windows, please use `\\` in file paths;
*   If HuggingFace is inaccessible, please consider using `wisemodel` or `modescape`.

**If you encounter any issues during the installation of DeepKE and DeepKE-LLM, please check [Tips](https://github.com/zjunlp/DeepKE#tips) or promptly submit an [issue](https://github.com/zjunlp/DeepKE/issues), and we will assist you with resolving the problem!**

Table of Contents
-----------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#table-of-contents)

*   [Table of Contents](https://github.com/zjunlp/DeepKE?screenshot=true#table-of-contents)
*   [What's New](https://github.com/zjunlp/DeepKE?screenshot=true#whats-new)
*   [Prediction Demo](https://github.com/zjunlp/DeepKE?screenshot=true#prediction-demo)
*   [Model Framework](https://github.com/zjunlp/DeepKE?screenshot=true#model-framework)
*   [Quick Start](https://github.com/zjunlp/DeepKE?screenshot=true#quick-start)
    *   [DeepKE-LLM](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-llm)
    *   [DeepKE](https://github.com/zjunlp/DeepKE?screenshot=true#deepke)
        *   [🔧Manual Environment Configuration](https://github.com/zjunlp/DeepKE?screenshot=true#manual-environment-configuration)
        *   [🐳Building With Docker Images](https://github.com/zjunlp/DeepKE?screenshot=true#building-with-docker-images)
    *   [Requirements](https://github.com/zjunlp/DeepKE?screenshot=true#requirements)
        *   [DeepKE](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-1)
    *   [Introduction of Three Functions](https://github.com/zjunlp/DeepKE?screenshot=true#introduction-of-three-functions)
        *   [1\. Named Entity Recognition](https://github.com/zjunlp/DeepKE?screenshot=true#1-named-entity-recognition)
        *   [2\. Relation Extraction](https://github.com/zjunlp/DeepKE?screenshot=true#2-relation-extraction)
        *   [3\. Attribute Extraction](https://github.com/zjunlp/DeepKE?screenshot=true#3-attribute-extraction)
        *   [4\. Event Extraction](https://github.com/zjunlp/DeepKE?screenshot=true#4-event-extraction)
*   [Tips](https://github.com/zjunlp/DeepKE?screenshot=true#tips)
*   [To do](https://github.com/zjunlp/DeepKE?screenshot=true#to-do)
*   [Reading Materials](https://github.com/zjunlp/DeepKE?screenshot=true#reading-materials)
*   [Related Toolkit](https://github.com/zjunlp/DeepKE?screenshot=true#related-toolkit)
*   [Citation](https://github.com/zjunlp/DeepKE?screenshot=true#citation)
*   [Contributors](https://github.com/zjunlp/DeepKE?screenshot=true#contributors)
*   [Other Knowledge Extraction Open-Source Projects](https://github.com/zjunlp/DeepKE?screenshot=true#other-knowledge-extraction-open-source-projects)

What's New
----------

[](https://github.com/zjunlp/DeepKE?screenshot=true#whats-new)

*   `December, 2024` We open source the [OneKE](https://github.com/zjunlp/OneKE/tree/main) knowledge extraction framework, supporting multi-agent knowledge extraction across various scenarios.
*   `April, 2024` We release a new bilingual (Chinese and English) schema-based information extraction model called [OneKE](https://huggingface.co/zjunlp/OneKE) based on Chinese-Alpaca-2-13B.
*   `Feb, 2024` We release a large-scale (0.32B tokens) high-quality bilingual (Chinese and English) Information Extraction (IE) instruction dataset named [IEPile](https://huggingface.co/datasets/zjunlp/iepie), along with two models trained with `IEPile`, [baichuan2-13b-iepile-lora](https://huggingface.co/zjunlp/baichuan2-13b-iepile-lora) and [llama2-13b-iepile-lora](https://huggingface.co/zjunlp/llama2-13b-iepile-lora).
*   `Sep 2023` a bilingual Chinese English Information Extraction (IE) instruction dataset called `InstructIE` was released for the Instruction based Knowledge Graph Construction Task (Instruction based KGC), as detailed in [here](https://github.com/zjunlp/DeepKE/blob/main/example/llm/README.md/#data).
*   `June, 2023` We update [DeepKE-LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) to support **knowledge extraction** with [KnowLM](https://github.com/zjunlp/KnowLM), [ChatGLM](https://github.com/THUDM/ChatGLM-6B), LLaMA-series, GPT-series etc.
*   `Apr, 2023` We have added new models, including [CP-NER(IJCAI'23)](https://github.com/zjunlp/DeepKE/blob/main/example/ner/cross), [ASP(EMNLP'22)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/ASP), [PRGC(ACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PRGC), [PURE(NAACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PURE), provided [event extraction](https://github.com/zjunlp/DeepKE/tree/main/example/ee/standard) capabilities (Chinese and English), and offered compatibility with higher versions of Python packages (e.g., Transformers).
*   `Feb, 2023` We have supported using [LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) (GPT-3) with in-context learning (based on [EasyInstruct](https://github.com/zjunlp/EasyInstruct)) & data generation, added a NER model [W2NER(AAAI'22)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/standard/w2ner).

**Previous News**

*   `Nov, 2022` Add data [annotation instructions](https://github.com/zjunlp/DeepKE/blob/main/README_TAG.md) for entity recognition and relation extraction, automatic labelling of weakly supervised data ([entity extraction](https://github.com/zjunlp/DeepKE/tree/main/example/ner/prepare-data) and [relation extraction](https://github.com/zjunlp/DeepKE/tree/main/example/re/prepare-data)), and optimize [multi-GPU training](https://github.com/zjunlp/DeepKE/tree/main/example/re/standard).
    
*   `Sept, 2022` The paper [DeepKE: A Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population](https://arxiv.org/abs/2201.03335) has been accepted by the EMNLP 2022 System Demonstration Track.
    
*   `Aug, 2022` We have added [data augmentation](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot/DA) (Chinese, English) support for [low-resource relation extraction](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot).
    
*   `June, 2022` We have added multimodal support for [entity](https://github.com/zjunlp/DeepKE/tree/main/example/ner/multimodal) and [relation extraction](https://github.com/zjunlp/DeepKE/tree/main/example/re/multimodal).
    
*   `May, 2022` We have released [DeepKE-cnschema](https://github.com/zjunlp/DeepKE/blob/main/README_CNSCHEMA.md) with off-the-shelf knowledge extraction models.
    
*   `Jan, 2022` We have released a paper [DeepKE: A Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population](https://arxiv.org/abs/2201.03335)
    
*   `Dec, 2021` We have added `dockerfile` to create the enviroment automatically.
    
*   `Nov, 2021` The demo of DeepKE, supporting real-time extration without deploying and training, has been released.
    
*   The documentation of DeepKE, containing the details of DeepKE such as source codes and datasets, has been released.
    
*   `Oct, 2021` `pip install deepke`
    
*   The codes of deepke-v2.0 have been released.
    
*   `Aug, 2019` The codes of deepke-v1.0 have been released.
    
*   `Aug, 2018` The project DeepKE startup and codes of deepke-v0.1 have been released.
    

Prediction Demo
---------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#prediction-demo)

There is a demonstration of prediction. The GIF file is created by [Terminalizer](https://github.com/faressoft/terminalizer). Get the [code](https://drive.google.com/file/d/1r4tWfAkpvynH3CBSgd-XG79rf-pB-KR3/view?usp=share_link). [![Image 39](https://github.com/zjunlp/DeepKE/raw/main/pics/demo.gif)](https://github.com/zjunlp/DeepKE/blob/main/pics/demo.gif)

Model Framework
---------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#model-framework)

### [![Image 40](https://github.com/zjunlp/DeepKE/raw/main/pics/architectures.png)](https://github.com/zjunlp/DeepKE/blob/main/pics/architectures.png)

[](https://github.com/zjunlp/DeepKE?screenshot=true#----)

*   DeepKE contains a unified framework for **named entity recognition**, **relation extraction** and **attribute extraction**, the three knowledge extraction functions.
*   Each task can be implemented in different scenarios. For example, we can achieve relation extraction in **standard**, **low-resource (few-shot)**, **document-level** and **multimodal** settings.
*   Each application scenario comprises of three components: **Data** including Tokenizer, Preprocessor and Loader, **Model** including Module, Encoder and Forwarder, **Core** including Training, Evaluation and Prediction.

Quick Start
-----------

[](https://github.com/zjunlp/DeepKE?screenshot=true#quick-start)

DeepKE-LLM
----------

[](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-llm)

In the era of large models, DeepKE-LLM utilizes a completely new environment dependency.

```
conda create -n deepke-llm python=3.9
conda activate deepke-llm

cd example/llm
pip install -r requirements.txt
```

Please note that the `requirements.txt` file is located in the `example/llm` folder.

DeepKE
------

[](https://github.com/zjunlp/DeepKE?screenshot=true#deepke)

*   _DeepKE_ supports `pip install deepke`.  
    Take the fully supervised relation extraction for example.
*   _DeepKE_ supports both **manual** and **docker image** environment configuration, you can choose the appropriate way to build.
*   Highly recommended to install deepke in a Linux environment.

#### 🔧Manual Environment Configuration

[](https://github.com/zjunlp/DeepKE?screenshot=true#manual-environment-configuration)

**Step1** Download the basic code

git clone --depth 1 https://github.com/zjunlp/DeepKE.git

**Step2** Create a virtual environment using `Anaconda` and enter it.

conda create -n deepke python=3.8

conda activate deepke

1.  Install _DeepKE_ with source code
    
    pip install -r requirements.txt
    
    python setup.py install
    
    python setup.py develop
    
2.  Install _DeepKE_ with `pip` (**NOT recommended!**)
    
    *   Please make sure that pip version <\= 24.0

**Step3** Enter the task directory

cd DeepKE/example/re/standard

**Step4** Download the dataset, or follow the [annotation instructions](https://github.com/zjunlp/DeepKE/blob/main/README_TAG.md) to obtain data

wget 120.27.214.45/Data/re/standard/data.tar.gz

tar -xzvf data.tar.gz

Many types of data formats are supported,and details are in each part.

**Step5** Training (Parameters for training can be changed in the `conf` folder)

We support visual parameter tuning by using _[wandb](https://docs.wandb.ai/quickstart)_.

**Step6** Prediction (Parameters for prediction can be changed in the `conf` folder)

Modify the path of the trained model in `predict.yaml`.The absolute path of the model needs to be used，such as `xxx/checkpoints/2019-12-03_ 17-35-30/cnn_ epoch21.pth`.

*   **❗NOTE: if you encounter any errors, please refer to the [Tips](https://github.com/zjunlp/DeepKE?screenshot=true#tips) or submit a GitHub issue.**

#### 🐳Building With Docker Images

[](https://github.com/zjunlp/DeepKE?screenshot=true#building-with-docker-images)

**Step1** Install the Docker client

Install Docker and start the Docker service.

**Step2** Pull the docker image and run the container

docker pull zjunlp/deepke:latest
docker run -it zjunlp/deepke:latest /bin/bash

The remaining steps are the same as **Step 3 and onwards** in **Manual Environment Configuration**.

*   **❗NOTE: You can refer to the [Tips](https://github.com/zjunlp/DeepKE?screenshot=true#tips) to speed up installation**

Requirements
------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#requirements)

### DeepKE

[](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-1)

> python == 3.8

*   torch\>\=1.5,<\=1.11
*   hydra-core==1.0.6
*   tensorboard==2.4.1
*   matplotlib==3.4.1
*   transformers==4.26.0
*   jieba==0.42.1
*   scikit-learn==0.24.1
*   seqeval==1.2.2
*   opt-einsum==3.3.0
*   wandb==0.12.7
*   ujson==5.6.0
*   huggingface\_hub==0.11.0
*   tensorboardX==2.5.1
*   nltk==3.8
*   protobuf==3.20.1
*   numpy==1.21.0
*   ipdb==0.13.11
*   pytorch-crf==0.7.2
*   tqdm==4.66.1
*   openai==0.28.0
*   Jinja2==3.1.2
*   datasets==2.13.2
*   pyhocon==0.3.60

Introduction of Three Functions
-------------------------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#introduction-of-three-functions)

### 1\. Named Entity Recognition

[](https://github.com/zjunlp/DeepKE?screenshot=true#1-named-entity-recognition)

*   Named entity recognition seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, organizations, etc.
    
*   The data is stored in `.txt` files. Some instances as following (Users can label data based on the tools [Doccano](https://github.com/doccano/doccano), [MarkTool](https://github.com/FXLP/MarkTool), or they can use the [Weak Supervision](https://github.com/zjunlp/DeepKE/blob/main/example/ner/prepare-data) with DeepKE to obtain data automatically):
    
    | Sentence | Person | Location | Organization |
    | --- | --- | --- | --- |
    | 本报北京9月4日讯记者杨涌报道：部分省区人民日报宣传发行工作座谈会9月3日在4日在京举行。 | 杨涌 | 北京 | 人民日报 |
    | 《红楼梦》由王扶林导演，周汝昌、王蒙、周岭等多位专家参与制作。 | 王扶林，周汝昌，王蒙，周岭 |  |  |
    | 秦始皇兵马俑位于陕西省西安市,是世界八大奇迹之一。 | 秦始皇 | 陕西省，西安市 |  |
    
*   Read the detailed process in specific README
    
    *   **[STANDARD (Fully Supervised)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/standard)**
        
        _**We [support LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) and provide the off-the-shelf model, [DeepKE-cnSchema-NER](https://github.com/zjunlp/DeepKE/blob/main/README_CNSCHEMA_CN.md), which will extract entities in cnSchema without training.**_
        
        **Step1** Enter `DeepKE/example/ner/standard`. Download the dataset.
        
        wget 120.27.214.45/Data/ner/standard/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        **Step2** Training
        
        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        
        **Step3** Prediction
        
    *   **[FEW-SHOT](https://github.com/zjunlp/DeepKE/tree/main/example/ner/few-shot)**
        
        **Step1** Enter `DeepKE/example/ner/few-shot`. Download the dataset.
        
        wget 120.27.214.45/Data/ner/few\_shot/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        **Step2** Training in the low-resouce setting
        
        The directory where the model is loaded and saved and the configuration parameters can be cusomized in the `conf` folder.
        
        python run.py +train=few\_shot
        
        Users can modify `load_path` in `conf/train/few_shot.yaml` to use existing loaded model.
        
        **Step3** Add `- predict` to `conf/config.yaml`, modify `loda_path` as the model path and `write_path` as the path where the predicted results are saved in `conf/predict.yaml`, and then run `python predict.py`
        
    *   **[MULTIMODAL](https://github.com/zjunlp/DeepKE/tree/main/example/ner/multimodal)**
        
        **Step1** Enter `DeepKE/example/ner/multimodal`. Download the dataset.
        
        wget 120.27.214.45/Data/ner/multimodal/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        We use RCNN detected objects and visual grounding objects from original images as visual local information, where RCNN via [faster\_rcnn](https://github.com/pytorch/vision/blob/main/torchvision/models/detection/faster_rcnn.py) and visual grounding via [onestage\_grounding](https://github.com/zyang-ur/onestage_grounding).
        
        **Step2** Training in the multimodal setting
        
        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        *   Start with the model trained last time: modify `load_path` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.
        
        **Step3** Prediction
        

### 2\. Relation Extraction

[](https://github.com/zjunlp/DeepKE?screenshot=true#2-relation-extraction)

*   Relationship extraction is the task of extracting semantic relations between entities from a unstructured text.
    
*   The data is stored in `.csv` files. Some instances as following (Users can label data based on the tools [Doccano](https://github.com/doccano/doccano), [MarkTool](https://github.com/FXLP/MarkTool), or they can use the [Weak Supervision](https://github.com/zjunlp/DeepKE/blob/main/example/re/prepare-data) with DeepKE to obtain data automatically):
    
    | Sentence | Relation | Head | Head\_offset | Tail | Tail\_offset |
    | --- | --- | --- | --- | --- | --- |
    | 《岳父也是爹》是王军执导的电视剧，由马恩然、范明主演。 | 导演 | 岳父也是爹 | 1 | 王军 | 8 |
    | 《九玄珠》是在纵横中文网连载的一部小说，作者是龙马。 | 连载网站 | 九玄珠 | 1 | 纵横中文网 | 7 |
    | 提起杭州的美景，西湖总是第一个映入脑海的词语。 | 所在城市 | 西湖 | 8 | 杭州 | 2 |
    
*   **!NOTE: If there are multiple entity types for one relation, entity types can be prefixed with the relation as inputs.**
    
*   Read the detailed process in specific README
    
    *   **[STANDARD (Fully Supervised)](https://github.com/zjunlp/DeepKE/tree/main/example/re/standard)**
        
        _**We [support LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) and provide the off-the-shelf model, [DeepKE-cnSchema-RE](https://github.com/zjunlp/DeepKE/blob/main/README_CNSCHEMA_CN.md), which will extract relations in cnSchema without training.**_
        
        **Step1** Enter the `DeepKE/example/re/standard` folder. Download the dataset.
        
        wget 120.27.214.45/Data/re/standard/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        **Step2** Training
        
        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        
        **Step3** Prediction
        
    *   **[FEW-SHOT](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot)**
        
        **Step1** Enter `DeepKE/example/re/few-shot`. Download the dataset.
        
        wget 120.27.214.45/Data/re/few\_shot/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        **Step 2** Training
        
        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        *   Start with the model trained last time: modify `train_from_saved_model` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.
        
        **Step3** Prediction
        
    *   **[DOCUMENT](https://github.com/zjunlp/DeepKE/tree/main/example/re/document)**
        
        **Step1** Enter `DeepKE/example/re/document`. Download the dataset.
        
        wget 120.27.214.45/Data/re/document/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        **Step2** Training
        
        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        *   Start with the model trained last time: modify `train_from_saved_model` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.
        
        **Step3** Prediction
        
    *   **[MULTIMODAL](https://github.com/zjunlp/DeepKE/tree/main/example/re/multimodal)**
        
        **Step1** Enter `DeepKE/example/re/multimodal`. Download the dataset.
        
        wget 120.27.214.45/Data/re/multimodal/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        We use RCNN detected objects and visual grounding objects from original images as visual local information, where RCNN via [faster\_rcnn](https://github.com/pytorch/vision/blob/main/torchvision/models/detection/faster_rcnn.py) and visual grounding via [onestage\_grounding](https://github.com/zyang-ur/onestage_grounding).
        
        **Step2** Training
        
        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        *   Start with the model trained last time: modify `load_path` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.
        
        **Step3** Prediction
        

### 3\. Attribute Extraction

[](https://github.com/zjunlp/DeepKE?screenshot=true#3-attribute-extraction)

*   Attribute extraction is to extract attributes for entities in a unstructed text.
    
*   The data is stored in `.csv` files. Some instances as following:
    
    | Sentence | Att | Ent | Ent\_offset | Val | Val\_offset |
    | --- | --- | --- | --- | --- | --- |
    | 张冬梅，女，汉族，1968年2月生，河南淇县人 | 民族 | 张冬梅 | 0 | 汉族 | 6 |
    | 诸葛亮，字孔明，三国时期杰出的军事家、文学家、发明家。 | 朝代 | 诸葛亮 | 0 | 三国时期 | 8 |
    | 2014年10月1日许鞍华执导的电影《黄金时代》上映 | 上映时间 | 黄金时代 | 19 | 2014年10月1日 | 0 |
    
*   Read the detailed process in specific README
    
    *   **[STANDARD (Fully Supervised)](https://github.com/zjunlp/DeepKE/tree/main/example/ae/standard)**
        
        **Step1** Enter the `DeepKE/example/ae/standard` folder. Download the dataset.
        
        wget 120.27.214.45/Data/ae/standard/data.tar.gz
        
        tar -xzvf data.tar.gz
        
        **Step2** Training
        
        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        
        **Step3** Prediction
        

### 4\. Event Extraction

[](https://github.com/zjunlp/DeepKE?screenshot=true#4-event-extraction)

*   Event extraction is the task to extract event type, event trigger words, event arguments from a unstructed text.
*   The data is stored in `.tsv` files, some instances are as follows:

| Sentence | Event type | Trigger | Role | Argument |
| --- | --- | --- | --- | --- |
| 据《欧洲时报》报道，当地时间27日，法国巴黎卢浮宫博物馆员工因不满工作条件恶化而罢工，导致该博物馆也因此闭门谢客一天。 | 组织行为-罢工 | 罢工 | 罢工人员 | 法国巴黎卢浮宫博物馆员工 |
| 时间 | 当地时间27日 |
| 所属组织 | 法国巴黎卢浮宫博物馆 |
| 中国外运2019年上半年归母净利润增长17%：收购了少数股东股权 | 财经/交易-出售/收购 | 收购 | 出售方 | 少数股东 |
| 收购方 | 中国外运 |
| 交易物 | 股权 |
| 美国亚特兰大航展13日发生一起表演机坠机事故，飞行员弹射出舱并安全着陆，事故没有造成人员伤亡。 | 灾害/意外-坠机 | 坠机 | 时间 | 13日 |
| 地点 | 美国亚特兰 |

*   Read the detailed process in specific README
    
    *   [STANDARD(Fully Supervised)](https://github.com/zjunlp/DeepKE/blob/main/example/ee/standard/README.md)
        
        **Step1** Enter the `DeepKE/example/ee/standard` folder. Download the dataset.
        
        wget 120.27.214.45/Data/ee/DuEE.zip
        unzip DuEE.zip
        
        **Step 2** Training
        
        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.
        
        **Step 3** Prediction
        

Tips
----

[](https://github.com/zjunlp/DeepKE?screenshot=true#tips)

1.`Using nearest mirror`, **[THU](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/) in China, will speed up the installation of _Anaconda_; [aliyun](http://mirrors.aliyun.com/pypi/simple/) in China, will speed up `pip install XXX`**.

2.When encountering `ModuleNotFoundError: No module named 'past'`，run `pip install future` .

3.It's slow to install the pretrained language models online. Recommend download pretrained models before use and save them in the `pretrained` folder. Read `README.md` in every task directory to check the specific requirement for saving pretrained models.

4.The old version of _DeepKE_ is in the [deepke-v1.0](https://github.com/zjunlp/DeepKE/tree/deepke-v1.0) branch. Users can change the branch to use the old version. The old version has been totally transfered to the standard relation extraction ([example/re/standard](https://github.com/zjunlp/DeepKE/blob/main/example/re/standard/README.md)).

5.If you want to modify the source code, it's recommended to install _DeepKE_ with source codes. If not, the modification will not work. See [issue](https://github.com/zjunlp/DeepKE/issues/117)

6.More related low-resource knowledge extraction works can be found in [Knowledge Extraction in Low-Resource Scenarios: Survey and Perspective](https://arxiv.org/pdf/2202.08063.pdf).

7.Make sure the exact versions of requirements in `requirements.txt`.

To do
-----

[](https://github.com/zjunlp/DeepKE?screenshot=true#to-do)

In next version, we plan to release a stronger LLM for KE.

Meanwhile, we will offer long-term maintenance to **fix bugs**, **solve issues** and meet **new requests**. So if you have any problems, please put issues to us.

Reading Materials
-----------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#reading-materials)

Data-Efficient Knowledge Graph Construction, 高效知识图谱构建 ([Tutorial on CCKS 2022](http://sigkg.cn/ccks2022/?page_id=24)) \[[slides](https://drive.google.com/drive/folders/1xqeREw3dSiw-Y1rxLDx77r0hGUvHnuuE)\]

Efficient and Robust Knowledge Graph Construction ([Tutorial on AACL-IJCNLP 2022](https://www.aacl2022.org/Program/tutorials)) \[[slides](https://github.com/NLP-Tutorials/AACL-IJCNLP2022-KGC-Tutorial)\]

PromptKG Family: a Gallery of Prompt Learning & KG-related Research Works, Toolkits, and Paper-list \[[Resources](https://github.com/zjunlp/PromptKG)\]

Knowledge Extraction in Low-Resource Scenarios: Survey and Perspective \[[Survey](https://arxiv.org/abs/2202.08063)\]\[[Paper-list](https://github.com/zjunlp/Low-resource-KEPapers)\]

Related Toolkit
---------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#related-toolkit)

[Doccano](https://github.com/doccano/doccano)、[MarkTool](https://github.com/FXLP/MarkTool)、[LabelStudio](https://labelstud.io/): Data Annotation Toolkits

[LambdaKG](https://github.com/zjunlp/PromptKG/tree/main/lambdaKG): A library and benchmark for PLM-based KG embeddings

[EasyInstruct](https://github.com/zjunlp/EasyInstruct): An easy-to-use framework to instruct Large Language Models

**Reading Materials**:

Data-Efficient Knowledge Graph Construction, 高效知识图谱构建 ([Tutorial on CCKS 2022](http://sigkg.cn/ccks2022/?page_id=24)) \[[slides](https://drive.google.com/drive/folders/1xqeREw3dSiw-Y1rxLDx77r0hGUvHnuuE)\]

Efficient and Robust Knowledge Graph Construction ([Tutorial on AACL-IJCNLP 2022](https://www.aacl2022.org/Program/tutorials)) \[[slides](https://github.com/NLP-Tutorials/AACL-IJCNLP2022-KGC-Tutorial)\]

PromptKG Family: a Gallery of Prompt Learning & KG-related Research Works, Toolkits, and Paper-list \[[Resources](https://github.com/zjunlp/PromptKG)\]

Knowledge Extraction in Low-Resource Scenarios: Survey and Perspective \[[Survey](https://arxiv.org/abs/2202.08063)\]\[[Paper-list](https://github.com/zjunlp/Low-resource-KEPapers)\]

**Related Toolkit**:

[Doccano](https://github.com/doccano/doccano)、[MarkTool](https://github.com/FXLP/MarkTool)、[LabelStudio](https://labelstud.io/): Data Annotation Toolkits

[LambdaKG](https://github.com/zjunlp/PromptKG/tree/main/lambdaKG): A library and benchmark for PLM-based KG embeddings

[EasyInstruct](https://github.com/zjunlp/EasyInstruct): An easy-to-use framework to instruct Large Language Models

Citation
--------

[](https://github.com/zjunlp/DeepKE?screenshot=true#citation)

Please cite our paper if you use DeepKE in your work

@inproceedings{EMNLP2022\_Demo\_DeepKE,
  author    = {Ningyu Zhang and
               Xin Xu and
               Liankuan Tao and
               Haiyang Yu and
               Hongbin Ye and
               Shuofei Qiao and
               Xin Xie and
               Xiang Chen and
               Zhoubo Li and
               Lei Li},
  editor    = {Wanxiang Che and
               Ekaterina Shutova},
  title     = {DeepKE: {A} Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population},
  booktitle = {{EMNLP} (Demos)},
  pages     = {98--108},
  publisher = {Association for Computational Linguistics},
  year      = {2022},
  url       = {https://aclanthology.org/2022.emnlp-demos.10}
}

Contributors
------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#contributors)

[Ningyu Zhang](https://person.zju.edu.cn/en/ningyu), [Haofen Wang](https://tjdi.tongji.edu.cn/TeacherDetail.do?id=4991&lang=_en), Fei Huang, Feiyu Xiong, Liankuan Tao, Xin Xu, Honghao Gui, Zhenru Zhang, Chuanqi Tan, Qiang Chen, Xiaohan Wang, Zekun Xi, Xinrong Li, Haiyang Yu, Hongbin Ye, Shuofei Qiao, Peng Wang, Yuqi Zhu, Xin Xie, Xiang Chen, Zhoubo Li, Lei Li, Xiaozhuan Liang, Yunzhi Yao, Jing Chen, Yuqi Zhu, Shumin Deng, Wen Zhang, Guozhou Zheng, Huajun Chen

Community Contributors: [thredreams](https://github.com/thredreams), [eltociear](https://github.com/eltociear), Ziwen Xu, Rui Huang, Xiaolong Weng

Other Knowledge Extraction Open-Source Projects
-----------------------------------------------

[](https://github.com/zjunlp/DeepKE?screenshot=true#other-knowledge-extraction-open-source-projects)

*   [CogIE](https://github.com/jinzhuoran/CogIE)
*   [OpenNRE](https://github.com/thunlp/OpenNRE)
*   [OmniEvent](https://github.com/THU-KEG/OmniEvent)
*   [OpenUE](https://github.com/zjunlp/OpenUE)
*   [OpenIE](https://stanfordnlp.github.io/CoreNLP/openie.html)
*   [RESIN](https://github.com/RESIN-KAIROS/RESIN-pipeline-public)
*   [ZShot](https://github.com/IBM/zshot)
*   [ZS4IE](https://github.com/BBN-E/ZS4IE)
*   [OmniEvent](https://github.com/THU-KEG/OmniEvent)

## Metadata

```json
{
  "title": "GitHub - zjunlp/DeepKE: [EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction",
  "description": "[EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction - zjunlp/DeepKE",
  "url": "https://github.com/zjunlp/DeepKE?screenshot=true",
  "content": "[![Image 33](https://github.com/zjunlp/DeepKE/raw/main/pics/logo.png)](https://github.com/zjunlp/deepke)\n\n[![Image 34: Documentation](https://camo.githubusercontent.com/19a35f9199add02f187a6033ed1fd37e636cc1e6c53d2605a061477a2514fac0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f64656d6f2d776562736974652d626c7565)](http://deepke.zjukg.cn/)[![Image 35: PyPI](https://camo.githubusercontent.com/1524eb2918e69efd21aded0a9dc90656105a8eb51d984b35f969de83ec2a48d4/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646565706b65)](https://pypi.org/project/deepke/#files)[![Image 36: GitHub](https://camo.githubusercontent.com/4e14f3c4ee10ac6f469184b93cc80833a25212b271135bfceb00b3a0e4ba826c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7a6a756e6c702f646565706b65)](https://github.com/zjunlp/DeepKE/blob/master/LICENSE)[![Image 37: Documentation](https://camo.githubusercontent.com/c90615cb62b7bd62502aacdbca14d1c9ba0dc323573c9d7b7aca2dfa8ae9a933/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f632d776562736974652d726564)](http://zjunlp.github.io/DeepKE)[![Image 38: Open In Colab](https://camo.githubusercontent.com/96889048f8a9014fdeba2a891f97150c6aac6e723f5190236b10215a97ed41f3/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1vS8YJhJltzw3hpJczPt24O0Azcs3ZpRi?usp=sharing)\n\n**English | [简体中文](https://github.com/zjunlp/DeepKE/blob/main/README_CN.md)**\n\nA Deep Learning Based Knowledge Extraction Toolkit  \nfor Knowledge Graph Construction\n\n\n---------------------------------------------------------------------------------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#----a-deep-learning-based-knowledge-extraction-toolkitfor-knowledge-graph-construction)\n\n[DeepKE](https://arxiv.org/pdf/2201.03335.pdf) is a knowledge extraction toolkit for knowledge graph construction supporting **cnSchema**，**low-resource**, **document-level** and **multimodal** scenarios for _entity_, _relation_ and _attribute_ extraction. We provide [documents](https://zjunlp.github.io/DeepKE/), [online demo](http://deepke.zjukg.cn/), [paper](https://arxiv.org/pdf/2201.03335.pdf), [slides](https://drive.google.com/file/d/1IIeIZAbVduemqXc4zD40FUMoPHCJinLy/view?usp=sharing) and [poster](https://drive.google.com/file/d/1vd7xVHlWzoAxivN4T5qKrcqIGDcSM1_7/view?usp=sharing) for beginners.\n\n*   ❗Want to use **Large Language Models** with DeepKE? Try [DeepKE-LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) and [OneKE](https://github.com/zjunlp/DeepKE/blob/main/example/llm/OneKE.md), have fun!\n*   ❗Want to train supervised models? Try [Quick Start](https://github.com/zjunlp/DeepKE?screenshot=true#quick-start), we provide the NER models (e.g, [LightNER(COLING'22)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/few-shot), [W2NER(AAAI'22)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/standard/w2ner)), relation extraction models (e.g., [KnowPrompt(WWW'22)](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot)), relational triple extraction models (e.g., [ASP(EMNLP'22)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/ASP), [PRGC(ACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PRGC), [PURE(NAACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PURE)), and release off-the-shelf models at [DeepKE-cnSchema](https://github.com/zjunlp/DeepKE/tree/main/example/triple/cnschema), have fun!\n*   We recommend using Linux; if using Windows, please use `\\\\` in file paths;\n*   If HuggingFace is inaccessible, please consider using `wisemodel` or `modescape`.\n\n**If you encounter any issues during the installation of DeepKE and DeepKE-LLM, please check [Tips](https://github.com/zjunlp/DeepKE#tips) or promptly submit an [issue](https://github.com/zjunlp/DeepKE/issues), and we will assist you with resolving the problem!**\n\nTable of Contents\n-----------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#table-of-contents)\n\n*   [Table of Contents](https://github.com/zjunlp/DeepKE?screenshot=true#table-of-contents)\n*   [What's New](https://github.com/zjunlp/DeepKE?screenshot=true#whats-new)\n*   [Prediction Demo](https://github.com/zjunlp/DeepKE?screenshot=true#prediction-demo)\n*   [Model Framework](https://github.com/zjunlp/DeepKE?screenshot=true#model-framework)\n*   [Quick Start](https://github.com/zjunlp/DeepKE?screenshot=true#quick-start)\n    *   [DeepKE-LLM](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-llm)\n    *   [DeepKE](https://github.com/zjunlp/DeepKE?screenshot=true#deepke)\n        *   [🔧Manual Environment Configuration](https://github.com/zjunlp/DeepKE?screenshot=true#manual-environment-configuration)\n        *   [🐳Building With Docker Images](https://github.com/zjunlp/DeepKE?screenshot=true#building-with-docker-images)\n    *   [Requirements](https://github.com/zjunlp/DeepKE?screenshot=true#requirements)\n        *   [DeepKE](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-1)\n    *   [Introduction of Three Functions](https://github.com/zjunlp/DeepKE?screenshot=true#introduction-of-three-functions)\n        *   [1\\. Named Entity Recognition](https://github.com/zjunlp/DeepKE?screenshot=true#1-named-entity-recognition)\n        *   [2\\. Relation Extraction](https://github.com/zjunlp/DeepKE?screenshot=true#2-relation-extraction)\n        *   [3\\. Attribute Extraction](https://github.com/zjunlp/DeepKE?screenshot=true#3-attribute-extraction)\n        *   [4\\. Event Extraction](https://github.com/zjunlp/DeepKE?screenshot=true#4-event-extraction)\n*   [Tips](https://github.com/zjunlp/DeepKE?screenshot=true#tips)\n*   [To do](https://github.com/zjunlp/DeepKE?screenshot=true#to-do)\n*   [Reading Materials](https://github.com/zjunlp/DeepKE?screenshot=true#reading-materials)\n*   [Related Toolkit](https://github.com/zjunlp/DeepKE?screenshot=true#related-toolkit)\n*   [Citation](https://github.com/zjunlp/DeepKE?screenshot=true#citation)\n*   [Contributors](https://github.com/zjunlp/DeepKE?screenshot=true#contributors)\n*   [Other Knowledge Extraction Open-Source Projects](https://github.com/zjunlp/DeepKE?screenshot=true#other-knowledge-extraction-open-source-projects)\n\nWhat's New\n----------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#whats-new)\n\n*   `December, 2024` We open source the [OneKE](https://github.com/zjunlp/OneKE/tree/main) knowledge extraction framework, supporting multi-agent knowledge extraction across various scenarios.\n*   `April, 2024` We release a new bilingual (Chinese and English) schema-based information extraction model called [OneKE](https://huggingface.co/zjunlp/OneKE) based on Chinese-Alpaca-2-13B.\n*   `Feb, 2024` We release a large-scale (0.32B tokens) high-quality bilingual (Chinese and English) Information Extraction (IE) instruction dataset named [IEPile](https://huggingface.co/datasets/zjunlp/iepie), along with two models trained with `IEPile`, [baichuan2-13b-iepile-lora](https://huggingface.co/zjunlp/baichuan2-13b-iepile-lora) and [llama2-13b-iepile-lora](https://huggingface.co/zjunlp/llama2-13b-iepile-lora).\n*   `Sep 2023` a bilingual Chinese English Information Extraction (IE) instruction dataset called `InstructIE` was released for the Instruction based Knowledge Graph Construction Task (Instruction based KGC), as detailed in [here](https://github.com/zjunlp/DeepKE/blob/main/example/llm/README.md/#data).\n*   `June, 2023` We update [DeepKE-LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) to support **knowledge extraction** with [KnowLM](https://github.com/zjunlp/KnowLM), [ChatGLM](https://github.com/THUDM/ChatGLM-6B), LLaMA-series, GPT-series etc.\n*   `Apr, 2023` We have added new models, including [CP-NER(IJCAI'23)](https://github.com/zjunlp/DeepKE/blob/main/example/ner/cross), [ASP(EMNLP'22)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/ASP), [PRGC(ACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PRGC), [PURE(NAACL'21)](https://github.com/zjunlp/DeepKE/tree/main/example/triple/PURE), provided [event extraction](https://github.com/zjunlp/DeepKE/tree/main/example/ee/standard) capabilities (Chinese and English), and offered compatibility with higher versions of Python packages (e.g., Transformers).\n*   `Feb, 2023` We have supported using [LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) (GPT-3) with in-context learning (based on [EasyInstruct](https://github.com/zjunlp/EasyInstruct)) & data generation, added a NER model [W2NER(AAAI'22)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/standard/w2ner).\n\n**Previous News**\n\n*   `Nov, 2022` Add data [annotation instructions](https://github.com/zjunlp/DeepKE/blob/main/README_TAG.md) for entity recognition and relation extraction, automatic labelling of weakly supervised data ([entity extraction](https://github.com/zjunlp/DeepKE/tree/main/example/ner/prepare-data) and [relation extraction](https://github.com/zjunlp/DeepKE/tree/main/example/re/prepare-data)), and optimize [multi-GPU training](https://github.com/zjunlp/DeepKE/tree/main/example/re/standard).\n    \n*   `Sept, 2022` The paper [DeepKE: A Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population](https://arxiv.org/abs/2201.03335) has been accepted by the EMNLP 2022 System Demonstration Track.\n    \n*   `Aug, 2022` We have added [data augmentation](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot/DA) (Chinese, English) support for [low-resource relation extraction](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot).\n    \n*   `June, 2022` We have added multimodal support for [entity](https://github.com/zjunlp/DeepKE/tree/main/example/ner/multimodal) and [relation extraction](https://github.com/zjunlp/DeepKE/tree/main/example/re/multimodal).\n    \n*   `May, 2022` We have released [DeepKE-cnschema](https://github.com/zjunlp/DeepKE/blob/main/README_CNSCHEMA.md) with off-the-shelf knowledge extraction models.\n    \n*   `Jan, 2022` We have released a paper [DeepKE: A Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population](https://arxiv.org/abs/2201.03335)\n    \n*   `Dec, 2021` We have added `dockerfile` to create the enviroment automatically.\n    \n*   `Nov, 2021` The demo of DeepKE, supporting real-time extration without deploying and training, has been released.\n    \n*   The documentation of DeepKE, containing the details of DeepKE such as source codes and datasets, has been released.\n    \n*   `Oct, 2021` `pip install deepke`\n    \n*   The codes of deepke-v2.0 have been released.\n    \n*   `Aug, 2019` The codes of deepke-v1.0 have been released.\n    \n*   `Aug, 2018` The project DeepKE startup and codes of deepke-v0.1 have been released.\n    \n\nPrediction Demo\n---------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#prediction-demo)\n\nThere is a demonstration of prediction. The GIF file is created by [Terminalizer](https://github.com/faressoft/terminalizer). Get the [code](https://drive.google.com/file/d/1r4tWfAkpvynH3CBSgd-XG79rf-pB-KR3/view?usp=share_link). [![Image 39](https://github.com/zjunlp/DeepKE/raw/main/pics/demo.gif)](https://github.com/zjunlp/DeepKE/blob/main/pics/demo.gif)\n\nModel Framework\n---------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#model-framework)\n\n### [![Image 40](https://github.com/zjunlp/DeepKE/raw/main/pics/architectures.png)](https://github.com/zjunlp/DeepKE/blob/main/pics/architectures.png)\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#----)\n\n*   DeepKE contains a unified framework for **named entity recognition**, **relation extraction** and **attribute extraction**, the three knowledge extraction functions.\n*   Each task can be implemented in different scenarios. For example, we can achieve relation extraction in **standard**, **low-resource (few-shot)**, **document-level** and **multimodal** settings.\n*   Each application scenario comprises of three components: **Data** including Tokenizer, Preprocessor and Loader, **Model** including Module, Encoder and Forwarder, **Core** including Training, Evaluation and Prediction.\n\nQuick Start\n-----------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#quick-start)\n\nDeepKE-LLM\n----------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-llm)\n\nIn the era of large models, DeepKE-LLM utilizes a completely new environment dependency.\n\n```\nconda create -n deepke-llm python=3.9\nconda activate deepke-llm\n\ncd example/llm\npip install -r requirements.txt\n```\n\nPlease note that the `requirements.txt` file is located in the `example/llm` folder.\n\nDeepKE\n------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#deepke)\n\n*   _DeepKE_ supports `pip install deepke`.  \n    Take the fully supervised relation extraction for example.\n*   _DeepKE_ supports both **manual** and **docker image** environment configuration, you can choose the appropriate way to build.\n*   Highly recommended to install deepke in a Linux environment.\n\n#### 🔧Manual Environment Configuration\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#manual-environment-configuration)\n\n**Step1** Download the basic code\n\ngit clone --depth 1 https://github.com/zjunlp/DeepKE.git\n\n**Step2** Create a virtual environment using `Anaconda` and enter it.\n\nconda create -n deepke python=3.8\n\nconda activate deepke\n\n1.  Install _DeepKE_ with source code\n    \n    pip install -r requirements.txt\n    \n    python setup.py install\n    \n    python setup.py develop\n    \n2.  Install _DeepKE_ with `pip` (**NOT recommended!**)\n    \n    *   Please make sure that pip version <\\= 24.0\n\n**Step3** Enter the task directory\n\ncd DeepKE/example/re/standard\n\n**Step4** Download the dataset, or follow the [annotation instructions](https://github.com/zjunlp/DeepKE/blob/main/README_TAG.md) to obtain data\n\nwget 120.27.214.45/Data/re/standard/data.tar.gz\n\ntar -xzvf data.tar.gz\n\nMany types of data formats are supported,and details are in each part.\n\n**Step5** Training (Parameters for training can be changed in the `conf` folder)\n\nWe support visual parameter tuning by using _[wandb](https://docs.wandb.ai/quickstart)_.\n\n**Step6** Prediction (Parameters for prediction can be changed in the `conf` folder)\n\nModify the path of the trained model in `predict.yaml`.The absolute path of the model needs to be used，such as `xxx/checkpoints/2019-12-03_ 17-35-30/cnn_ epoch21.pth`.\n\n*   **❗NOTE: if you encounter any errors, please refer to the [Tips](https://github.com/zjunlp/DeepKE?screenshot=true#tips) or submit a GitHub issue.**\n\n#### 🐳Building With Docker Images\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#building-with-docker-images)\n\n**Step1** Install the Docker client\n\nInstall Docker and start the Docker service.\n\n**Step2** Pull the docker image and run the container\n\ndocker pull zjunlp/deepke:latest\ndocker run -it zjunlp/deepke:latest /bin/bash\n\nThe remaining steps are the same as **Step 3 and onwards** in **Manual Environment Configuration**.\n\n*   **❗NOTE: You can refer to the [Tips](https://github.com/zjunlp/DeepKE?screenshot=true#tips) to speed up installation**\n\nRequirements\n------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#requirements)\n\n### DeepKE\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#deepke-1)\n\n> python == 3.8\n\n*   torch\\>\\=1.5,<\\=1.11\n*   hydra-core==1.0.6\n*   tensorboard==2.4.1\n*   matplotlib==3.4.1\n*   transformers==4.26.0\n*   jieba==0.42.1\n*   scikit-learn==0.24.1\n*   seqeval==1.2.2\n*   opt-einsum==3.3.0\n*   wandb==0.12.7\n*   ujson==5.6.0\n*   huggingface\\_hub==0.11.0\n*   tensorboardX==2.5.1\n*   nltk==3.8\n*   protobuf==3.20.1\n*   numpy==1.21.0\n*   ipdb==0.13.11\n*   pytorch-crf==0.7.2\n*   tqdm==4.66.1\n*   openai==0.28.0\n*   Jinja2==3.1.2\n*   datasets==2.13.2\n*   pyhocon==0.3.60\n\nIntroduction of Three Functions\n-------------------------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#introduction-of-three-functions)\n\n### 1\\. Named Entity Recognition\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#1-named-entity-recognition)\n\n*   Named entity recognition seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, organizations, etc.\n    \n*   The data is stored in `.txt` files. Some instances as following (Users can label data based on the tools [Doccano](https://github.com/doccano/doccano), [MarkTool](https://github.com/FXLP/MarkTool), or they can use the [Weak Supervision](https://github.com/zjunlp/DeepKE/blob/main/example/ner/prepare-data) with DeepKE to obtain data automatically):\n    \n    | Sentence | Person | Location | Organization |\n    | --- | --- | --- | --- |\n    | 本报北京9月4日讯记者杨涌报道：部分省区人民日报宣传发行工作座谈会9月3日在4日在京举行。 | 杨涌 | 北京 | 人民日报 |\n    | 《红楼梦》由王扶林导演，周汝昌、王蒙、周岭等多位专家参与制作。 | 王扶林，周汝昌，王蒙，周岭 |  |  |\n    | 秦始皇兵马俑位于陕西省西安市,是世界八大奇迹之一。 | 秦始皇 | 陕西省，西安市 |  |\n    \n*   Read the detailed process in specific README\n    \n    *   **[STANDARD (Fully Supervised)](https://github.com/zjunlp/DeepKE/tree/main/example/ner/standard)**\n        \n        _**We [support LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) and provide the off-the-shelf model, [DeepKE-cnSchema-NER](https://github.com/zjunlp/DeepKE/blob/main/README_CNSCHEMA_CN.md), which will extract entities in cnSchema without training.**_\n        \n        **Step1** Enter `DeepKE/example/ner/standard`. Download the dataset.\n        \n        wget 120.27.214.45/Data/ner/standard/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        **Step2** Training\n        \n        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        \n        **Step3** Prediction\n        \n    *   **[FEW-SHOT](https://github.com/zjunlp/DeepKE/tree/main/example/ner/few-shot)**\n        \n        **Step1** Enter `DeepKE/example/ner/few-shot`. Download the dataset.\n        \n        wget 120.27.214.45/Data/ner/few\\_shot/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        **Step2** Training in the low-resouce setting\n        \n        The directory where the model is loaded and saved and the configuration parameters can be cusomized in the `conf` folder.\n        \n        python run.py +train=few\\_shot\n        \n        Users can modify `load_path` in `conf/train/few_shot.yaml` to use existing loaded model.\n        \n        **Step3** Add `- predict` to `conf/config.yaml`, modify `loda_path` as the model path and `write_path` as the path where the predicted results are saved in `conf/predict.yaml`, and then run `python predict.py`\n        \n    *   **[MULTIMODAL](https://github.com/zjunlp/DeepKE/tree/main/example/ner/multimodal)**\n        \n        **Step1** Enter `DeepKE/example/ner/multimodal`. Download the dataset.\n        \n        wget 120.27.214.45/Data/ner/multimodal/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        We use RCNN detected objects and visual grounding objects from original images as visual local information, where RCNN via [faster\\_rcnn](https://github.com/pytorch/vision/blob/main/torchvision/models/detection/faster_rcnn.py) and visual grounding via [onestage\\_grounding](https://github.com/zyang-ur/onestage_grounding).\n        \n        **Step2** Training in the multimodal setting\n        \n        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        *   Start with the model trained last time: modify `load_path` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.\n        \n        **Step3** Prediction\n        \n\n### 2\\. Relation Extraction\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#2-relation-extraction)\n\n*   Relationship extraction is the task of extracting semantic relations between entities from a unstructured text.\n    \n*   The data is stored in `.csv` files. Some instances as following (Users can label data based on the tools [Doccano](https://github.com/doccano/doccano), [MarkTool](https://github.com/FXLP/MarkTool), or they can use the [Weak Supervision](https://github.com/zjunlp/DeepKE/blob/main/example/re/prepare-data) with DeepKE to obtain data automatically):\n    \n    | Sentence | Relation | Head | Head\\_offset | Tail | Tail\\_offset |\n    | --- | --- | --- | --- | --- | --- |\n    | 《岳父也是爹》是王军执导的电视剧，由马恩然、范明主演。 | 导演 | 岳父也是爹 | 1 | 王军 | 8 |\n    | 《九玄珠》是在纵横中文网连载的一部小说，作者是龙马。 | 连载网站 | 九玄珠 | 1 | 纵横中文网 | 7 |\n    | 提起杭州的美景，西湖总是第一个映入脑海的词语。 | 所在城市 | 西湖 | 8 | 杭州 | 2 |\n    \n*   **!NOTE: If there are multiple entity types for one relation, entity types can be prefixed with the relation as inputs.**\n    \n*   Read the detailed process in specific README\n    \n    *   **[STANDARD (Fully Supervised)](https://github.com/zjunlp/DeepKE/tree/main/example/re/standard)**\n        \n        _**We [support LLM](https://github.com/zjunlp/DeepKE/tree/main/example/llm) and provide the off-the-shelf model, [DeepKE-cnSchema-RE](https://github.com/zjunlp/DeepKE/blob/main/README_CNSCHEMA_CN.md), which will extract relations in cnSchema without training.**_\n        \n        **Step1** Enter the `DeepKE/example/re/standard` folder. Download the dataset.\n        \n        wget 120.27.214.45/Data/re/standard/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        **Step2** Training\n        \n        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        \n        **Step3** Prediction\n        \n    *   **[FEW-SHOT](https://github.com/zjunlp/DeepKE/tree/main/example/re/few-shot)**\n        \n        **Step1** Enter `DeepKE/example/re/few-shot`. Download the dataset.\n        \n        wget 120.27.214.45/Data/re/few\\_shot/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        **Step 2** Training\n        \n        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        *   Start with the model trained last time: modify `train_from_saved_model` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.\n        \n        **Step3** Prediction\n        \n    *   **[DOCUMENT](https://github.com/zjunlp/DeepKE/tree/main/example/re/document)**\n        \n        **Step1** Enter `DeepKE/example/re/document`. Download the dataset.\n        \n        wget 120.27.214.45/Data/re/document/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        **Step2** Training\n        \n        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        *   Start with the model trained last time: modify `train_from_saved_model` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.\n        \n        **Step3** Prediction\n        \n    *   **[MULTIMODAL](https://github.com/zjunlp/DeepKE/tree/main/example/re/multimodal)**\n        \n        **Step1** Enter `DeepKE/example/re/multimodal`. Download the dataset.\n        \n        wget 120.27.214.45/Data/re/multimodal/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        We use RCNN detected objects and visual grounding objects from original images as visual local information, where RCNN via [faster\\_rcnn](https://github.com/pytorch/vision/blob/main/torchvision/models/detection/faster_rcnn.py) and visual grounding via [onestage\\_grounding](https://github.com/zyang-ur/onestage_grounding).\n        \n        **Step2** Training\n        \n        *   The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        *   Start with the model trained last time: modify `load_path` in `conf/train.yaml`as the path where the model trained last time was saved. And the path saving logs generated in training can be customized by `log_dir`.\n        \n        **Step3** Prediction\n        \n\n### 3\\. Attribute Extraction\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#3-attribute-extraction)\n\n*   Attribute extraction is to extract attributes for entities in a unstructed text.\n    \n*   The data is stored in `.csv` files. Some instances as following:\n    \n    | Sentence | Att | Ent | Ent\\_offset | Val | Val\\_offset |\n    | --- | --- | --- | --- | --- | --- |\n    | 张冬梅，女，汉族，1968年2月生，河南淇县人 | 民族 | 张冬梅 | 0 | 汉族 | 6 |\n    | 诸葛亮，字孔明，三国时期杰出的军事家、文学家、发明家。 | 朝代 | 诸葛亮 | 0 | 三国时期 | 8 |\n    | 2014年10月1日许鞍华执导的电影《黄金时代》上映 | 上映时间 | 黄金时代 | 19 | 2014年10月1日 | 0 |\n    \n*   Read the detailed process in specific README\n    \n    *   **[STANDARD (Fully Supervised)](https://github.com/zjunlp/DeepKE/tree/main/example/ae/standard)**\n        \n        **Step1** Enter the `DeepKE/example/ae/standard` folder. Download the dataset.\n        \n        wget 120.27.214.45/Data/ae/standard/data.tar.gz\n        \n        tar -xzvf data.tar.gz\n        \n        **Step2** Training\n        \n        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        \n        **Step3** Prediction\n        \n\n### 4\\. Event Extraction\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#4-event-extraction)\n\n*   Event extraction is the task to extract event type, event trigger words, event arguments from a unstructed text.\n*   The data is stored in `.tsv` files, some instances are as follows:\n\n| Sentence | Event type | Trigger | Role | Argument |\n| --- | --- | --- | --- | --- |\n| 据《欧洲时报》报道，当地时间27日，法国巴黎卢浮宫博物馆员工因不满工作条件恶化而罢工，导致该博物馆也因此闭门谢客一天。 | 组织行为-罢工 | 罢工 | 罢工人员 | 法国巴黎卢浮宫博物馆员工 |\n| 时间 | 当地时间27日 |\n| 所属组织 | 法国巴黎卢浮宫博物馆 |\n| 中国外运2019年上半年归母净利润增长17%：收购了少数股东股权 | 财经/交易-出售/收购 | 收购 | 出售方 | 少数股东 |\n| 收购方 | 中国外运 |\n| 交易物 | 股权 |\n| 美国亚特兰大航展13日发生一起表演机坠机事故，飞行员弹射出舱并安全着陆，事故没有造成人员伤亡。 | 灾害/意外-坠机 | 坠机 | 时间 | 13日 |\n| 地点 | 美国亚特兰 |\n\n*   Read the detailed process in specific README\n    \n    *   [STANDARD(Fully Supervised)](https://github.com/zjunlp/DeepKE/blob/main/example/ee/standard/README.md)\n        \n        **Step1** Enter the `DeepKE/example/ee/standard` folder. Download the dataset.\n        \n        wget 120.27.214.45/Data/ee/DuEE.zip\n        unzip DuEE.zip\n        \n        **Step 2** Training\n        \n        The dataset and parameters can be customized in the `data` folder and `conf` folder respectively.\n        \n        **Step 3** Prediction\n        \n\nTips\n----\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#tips)\n\n1.`Using nearest mirror`, **[THU](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/) in China, will speed up the installation of _Anaconda_; [aliyun](http://mirrors.aliyun.com/pypi/simple/) in China, will speed up `pip install XXX`**.\n\n2.When encountering `ModuleNotFoundError: No module named 'past'`，run `pip install future` .\n\n3.It's slow to install the pretrained language models online. Recommend download pretrained models before use and save them in the `pretrained` folder. Read `README.md` in every task directory to check the specific requirement for saving pretrained models.\n\n4.The old version of _DeepKE_ is in the [deepke-v1.0](https://github.com/zjunlp/DeepKE/tree/deepke-v1.0) branch. Users can change the branch to use the old version. The old version has been totally transfered to the standard relation extraction ([example/re/standard](https://github.com/zjunlp/DeepKE/blob/main/example/re/standard/README.md)).\n\n5.If you want to modify the source code, it's recommended to install _DeepKE_ with source codes. If not, the modification will not work. See [issue](https://github.com/zjunlp/DeepKE/issues/117)\n\n6.More related low-resource knowledge extraction works can be found in [Knowledge Extraction in Low-Resource Scenarios: Survey and Perspective](https://arxiv.org/pdf/2202.08063.pdf).\n\n7.Make sure the exact versions of requirements in `requirements.txt`.\n\nTo do\n-----\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#to-do)\n\nIn next version, we plan to release a stronger LLM for KE.\n\nMeanwhile, we will offer long-term maintenance to **fix bugs**, **solve issues** and meet **new requests**. So if you have any problems, please put issues to us.\n\nReading Materials\n-----------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#reading-materials)\n\nData-Efficient Knowledge Graph Construction, 高效知识图谱构建 ([Tutorial on CCKS 2022](http://sigkg.cn/ccks2022/?page_id=24)) \\[[slides](https://drive.google.com/drive/folders/1xqeREw3dSiw-Y1rxLDx77r0hGUvHnuuE)\\]\n\nEfficient and Robust Knowledge Graph Construction ([Tutorial on AACL-IJCNLP 2022](https://www.aacl2022.org/Program/tutorials)) \\[[slides](https://github.com/NLP-Tutorials/AACL-IJCNLP2022-KGC-Tutorial)\\]\n\nPromptKG Family: a Gallery of Prompt Learning & KG-related Research Works, Toolkits, and Paper-list \\[[Resources](https://github.com/zjunlp/PromptKG)\\]\n\nKnowledge Extraction in Low-Resource Scenarios: Survey and Perspective \\[[Survey](https://arxiv.org/abs/2202.08063)\\]\\[[Paper-list](https://github.com/zjunlp/Low-resource-KEPapers)\\]\n\nRelated Toolkit\n---------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#related-toolkit)\n\n[Doccano](https://github.com/doccano/doccano)、[MarkTool](https://github.com/FXLP/MarkTool)、[LabelStudio](https://labelstud.io/): Data Annotation Toolkits\n\n[LambdaKG](https://github.com/zjunlp/PromptKG/tree/main/lambdaKG): A library and benchmark for PLM-based KG embeddings\n\n[EasyInstruct](https://github.com/zjunlp/EasyInstruct): An easy-to-use framework to instruct Large Language Models\n\n**Reading Materials**:\n\nData-Efficient Knowledge Graph Construction, 高效知识图谱构建 ([Tutorial on CCKS 2022](http://sigkg.cn/ccks2022/?page_id=24)) \\[[slides](https://drive.google.com/drive/folders/1xqeREw3dSiw-Y1rxLDx77r0hGUvHnuuE)\\]\n\nEfficient and Robust Knowledge Graph Construction ([Tutorial on AACL-IJCNLP 2022](https://www.aacl2022.org/Program/tutorials)) \\[[slides](https://github.com/NLP-Tutorials/AACL-IJCNLP2022-KGC-Tutorial)\\]\n\nPromptKG Family: a Gallery of Prompt Learning & KG-related Research Works, Toolkits, and Paper-list \\[[Resources](https://github.com/zjunlp/PromptKG)\\]\n\nKnowledge Extraction in Low-Resource Scenarios: Survey and Perspective \\[[Survey](https://arxiv.org/abs/2202.08063)\\]\\[[Paper-list](https://github.com/zjunlp/Low-resource-KEPapers)\\]\n\n**Related Toolkit**:\n\n[Doccano](https://github.com/doccano/doccano)、[MarkTool](https://github.com/FXLP/MarkTool)、[LabelStudio](https://labelstud.io/): Data Annotation Toolkits\n\n[LambdaKG](https://github.com/zjunlp/PromptKG/tree/main/lambdaKG): A library and benchmark for PLM-based KG embeddings\n\n[EasyInstruct](https://github.com/zjunlp/EasyInstruct): An easy-to-use framework to instruct Large Language Models\n\nCitation\n--------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#citation)\n\nPlease cite our paper if you use DeepKE in your work\n\n@inproceedings{EMNLP2022\\_Demo\\_DeepKE,\n  author    = {Ningyu Zhang and\n               Xin Xu and\n               Liankuan Tao and\n               Haiyang Yu and\n               Hongbin Ye and\n               Shuofei Qiao and\n               Xin Xie and\n               Xiang Chen and\n               Zhoubo Li and\n               Lei Li},\n  editor    = {Wanxiang Che and\n               Ekaterina Shutova},\n  title     = {DeepKE: {A} Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population},\n  booktitle = {{EMNLP} (Demos)},\n  pages     = {98--108},\n  publisher = {Association for Computational Linguistics},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.emnlp-demos.10}\n}\n\nContributors\n------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#contributors)\n\n[Ningyu Zhang](https://person.zju.edu.cn/en/ningyu), [Haofen Wang](https://tjdi.tongji.edu.cn/TeacherDetail.do?id=4991&lang=_en), Fei Huang, Feiyu Xiong, Liankuan Tao, Xin Xu, Honghao Gui, Zhenru Zhang, Chuanqi Tan, Qiang Chen, Xiaohan Wang, Zekun Xi, Xinrong Li, Haiyang Yu, Hongbin Ye, Shuofei Qiao, Peng Wang, Yuqi Zhu, Xin Xie, Xiang Chen, Zhoubo Li, Lei Li, Xiaozhuan Liang, Yunzhi Yao, Jing Chen, Yuqi Zhu, Shumin Deng, Wen Zhang, Guozhou Zheng, Huajun Chen\n\nCommunity Contributors: [thredreams](https://github.com/thredreams), [eltociear](https://github.com/eltociear), Ziwen Xu, Rui Huang, Xiaolong Weng\n\nOther Knowledge Extraction Open-Source Projects\n-----------------------------------------------\n\n[](https://github.com/zjunlp/DeepKE?screenshot=true#other-knowledge-extraction-open-source-projects)\n\n*   [CogIE](https://github.com/jinzhuoran/CogIE)\n*   [OpenNRE](https://github.com/thunlp/OpenNRE)\n*   [OmniEvent](https://github.com/THU-KEG/OmniEvent)\n*   [OpenUE](https://github.com/zjunlp/OpenUE)\n*   [OpenIE](https://stanfordnlp.github.io/CoreNLP/openie.html)\n*   [RESIN](https://github.com/RESIN-KAIROS/RESIN-pipeline-public)\n*   [ZShot](https://github.com/IBM/zshot)\n*   [ZS4IE](https://github.com/BBN-E/ZS4IE)\n*   [OmniEvent](https://github.com/THU-KEG/OmniEvent)",
  "usage": {
    "tokens": 9718
  }
}
```
