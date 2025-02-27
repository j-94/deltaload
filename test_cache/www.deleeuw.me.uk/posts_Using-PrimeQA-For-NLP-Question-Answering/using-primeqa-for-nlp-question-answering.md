---
title: Using PrimeQA For NLP Question Answering
description: Question Answering models are one of the mainstays of NLP. In this blog I demonstrate how to use the open-source project PrimeQA to install a framework which indexes data, and provides a Q&A capability which can easy be incorporated into an application.
url: https://www.deleeuw.me.uk/posts/Using-PrimeQA-For-NLP-Question-Answering/
timestamp: 2025-01-20T15:57:37.326Z
domain: www.deleeuw.me.uk
path: posts_Using-PrimeQA-For-NLP-Question-Answering
---

# Using PrimeQA For NLP Question Answering


Question Answering models are one of the mainstays of NLP. In this blog I demonstrate how to use the open-source project PrimeQA to install a framework which indexes data, and provides a Q&A capability which can easy be incorporated into an application.


## Content

Adam de Leeuw
Documenting my experiences in IT
HOME
CATEGORIES
TAGS
ARCHIVES
OPENSOURCE
ABOUT	
Home  Using PrimeQA For NLP Question Answering
Using PrimeQA For NLP Question Answering
Posted Mar 13, 2023  Updated Mar 14, 2023
By Adam de Leeuw
9 min read

Question Answering models are one of the mainstays of NLP. In this blog I demonstrate how to use the open-source project PrimeQA to install a framework which indexes data, and provides a Q&A capability which can easy be incorporated into an application.

What is PrimeQA?

PrimeQA is a public open source repository that enables you to train state-of-the-art models for question answering (QA). PrimeQA can perform document retrieval and reading comprehension based on neural networks. It provides a front-end UI search engine, in addition to APIs.

Requirements for Installing PrimeQA
Ubuntu Linux 20.04.4 LTS VM - Although primeQA recommend a high specification, I used a more modest 4vCPU, 16GB RAM without GPU
Docker
Git
Python & pip
Java 11 JDK
Instal Pre-requites

Install Docker

Install Docker Compose:

1

	
apt  install docker-compose


Install git:

1

	
apt install git


Install Python & pip:

1
2

	
apt install python3-pip
apt-get install python3-venv


Install Java 11 JDK:

1

	
apt-get install openjdk-11-jdk

Installing PrimeQA on Ubuntu

Clone the create-primea-app repo:

1
2
3

	
mkdir /root/gitRepos
cd /root/gitRepos
git clone https://github.com/primeqa/create-primeqa-app


Set an environment variable to your public IP. This can be localhost if you plan to use a browser locally on Ubuntu via VNC:

1

	
export PUBLIC_IP=<your IP or localhost>


Launch primeQA by launching three container images. Use the -m gpu only if your Ubuntu host includes a GPU:

1
2

	
cd create-primeqa-app
./launch.sh [-m gpu]


Validate the three containers started:

1

	
docker ps


The containers run the following components:

primeqa/services: a gRPC/REST service layer on top of PrimeQA
primeqa/orchestrator: an integration service for PrimeQA capabilities and external services
primeqa/ui: ReactJS webapp providing a example UI

Ensure that ports 50051, 50059 and 82 are accessible. If you plan to access the web Ui via a public IP and you’re using a cloud virtual server, you may need to edit the network security (e.g. Security Group on IBM Cloud).

Settings are in the orchestrator-store/primeqa.json. Edit this file as follows:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

	
{
    "application_id": "primeqa",
    "name": "PrimeQA",
    "description": "PrimeQA is a public open source repository that enables researchers and developers to train state-of-the-art models for question answering (QA).",
    "settings": {
        "retrievers": {
	  "PrimeQA": {
            "service_endpoint": "primeqa:50051"
          }
        },
        "readers": {
	  "PrimeQA": {
            "service_endpoint": "primeqa:50051",	
            "beta": 0.7
          }
        }
    }
}


This sets the Reader and Retriever processes to be provided locally by primeQA. It is possible to also add a configuration for Watson Discovery for the Reader. I’ll explain later what the Reader and Retriever components do.

Preparing the Corpus

PrimeQA supports different models for information retrieval (provided by the Reader component of primeQA):

There are two Dense IR engines supported: ColBERT and Direct Passage Retrieval (DPR).
Sparse IR is a Pyserini-based IR Engine enabling BM25 ranking using bag of words representation.

In this tutorial, we will use Dr.Decr, a ColBERT based fine-tuned language model to create an index. It expects the corpus to be a collection of documents in a tsv file, in a tabular id text title arrangement, ideally in the 1-180 word range. The primeqa repo provides some sample scripts to help prepare the data into this format. The scripts are designed for another book which is no longer available in the public domain, but this is a good starting point.

For this blog, I used the following dataset from Kaggle. It contains multiple stories, but I copied lines 67331-67543 to a new file Book1.txt, giving me just one story, “MY FATHER’S DRAGON” which is public domain.

1
2
3

	
cd /root/gitRepos/create-primeqa-app/examples
cp -R harry-potter-corpus my_fathers_dragon
cd my_fathers_dragon


Copy Book1.txt from your workstation to /examples/my_fathers_dragon.

Install the pre-requisites for processing the corpus:

1
2
3
4
5
6
7
8

	
alias pip=pip3
alias python=python3
python -m venv .env           # will create directory .env
source .env/bin/activate      # activate virtualenv
pip install primeqa
pip install --upgrade pip
pip install spacy             
python -m spacy download en_core_web_sm


Process the corpus:

1

	
./process.sh


The resulting corpus.tsv looks like this:

1
2
3

	
id	text	title
1	"MY FATHER'S DRAGON MY FATHER MEETS THE CAT One cold rainy day when my father was a little boy, he met an old alley cat on his street. The cat was very drippy and uncomfortable so my father said, ""Wouldn't you like to come home with me?""This surprised the cat she had never before met anyone who cared about old alley cats but she said, ""I'd be very much obliged if I could sit by a warm furnace, and perhaps have a saucer of milk.""""We have a very nice furnace to sit by,"" said my father, ""and I'm sure my mother has an extra saucer of milk."""	Book1 Paragraph 1
2	"My father and the cat became good friends but my father's mother was very upset about the cat. She hated cats, particularly ugly old alley cats. ""Elmer Elevator,"" she said to my father, ""if you think I'm going to give that cat a saucer of milk, you're very wrong. Once you start feeding stray alley cats you might as well expect to feed every stray in town, and I am not going to do it!""This made my father very sad, and he apologized to the cat because his mother had been so rude. He told the cat to stay anyway, and that somehow he would bring her a saucer of milk each day. My father fed the cat for three weeks, but one day his mother found the cat's saucer in the cellar and she was extremely angry. She whipped my father and threw the cat out the door, but later on my father sneaked out and found the cat."	Book1 Paragraph 2

Package the corpus, index and models

The corpus, index and model need to be installed into the ‘PrimeQA store’ which is located in directory primeqa-store.

The model used as the Reader is not installed by default. Run the following script to download it to /examples/my_fathers_dragon:

1

	
./download-model.sh


Run the following script to copy the model to a new location in primeqa-store.

1

	
CHECKPOINT=$(./setup-checkpoint.sh DrDecr.dnn ../../primeqa-store)


The script returns a path which is stored in the CHECKPOINT variable for later use. Display the value with echo $CHECKPOINT and make a note of it.

Next, invoke a script which uses the DrDecr model to create an index, and copy the files to the primeqa-store directory. In addition, an SQLite database is created.

1

	
./setup-index.sh "${CHECKPOINT}" corpus.tsv ../../primeqa-store/


The setup-index.sh script created one or more directories at `primeqa-store/indexes/`.

If you find there are multiple directories with names such as 9329c257-a514-48a7-ac03-c53a05e3ec5f, inspect each one in turn to determine if there are files in the subdirectory 9329c257-a514-48a7-ac03-c53a05e3ec5f/index. If this is empty, the directory is not required and can be deleted. Repeat this process until only one directory remains, which should have a populated `index` subdirectory.

Rename the directory:

1
2

	
cd /root/gitRepos/create-primeqa-app/primeqa-store/indexes
mv <indexname> my_fathers_dragon


The setup-index.sh script also created file primeqa-store/indexes/<indexname>/information.json. At the time of writing, this file has been created incorrectly. Replace the contents so it looks like this:

1
2
3
4
5
6
7
8

	
{
  "index_id": "my_fathers_dragon",
  "status": "READY",
  "configuration": {
    "engine_type": "ColBERT",
    "checkpoint": "<penultimate directory of your $CHECKPOINT path, e.g. ColBERTIndexer_20230308101308>"  
  }
}

Restart primeQA

It may not be strictly necessary, but after making the configuration I restarted the containers:

	
cd /root/gitRepos/create-primeqa-app
./terminate.sh
./launch.sh

Testing with PrimeQA UI

Open a browser to PUBLIC_IP:82/qa.

To help with composing some test searching, you can read a brief summary of My Father Met a Dragon.

As you test the three capabilities below (Retrieval, Reading, Question Answering), you will notice the first query takes a long time. This is because primeQA is downloading models in the background. These are the transformer (large language) models used for Reading and Question Answering. PrimeQA allows these models can be replaced according to the specific requirements.

You will see the model appear here create-primeqa-app/cache/huggingface/hub:

1
2
3

	
-rwxrwxrwx 1 2000 2000    1 Mar 14 09:21 version.txt
drwxr-xr-x 6 2000 2000 4096 Mar 14 13:39 models--xlm-roberta-base
drwxr-xr-x 6 2000 2000 4096 Mar 14 13:41 models--PrimeQA--nq_tydi_sq1-reader-xlmr_large-20221110

Test Retrieval

Retrieval searches the document index. Select the Retrieval icon on the left and query ‘What animals did Father meet?’.

You will see documents from the index which mention the animals such as cat, bear, rhinoceras, lion, monkey etc. However you do not get one word answers.

This uses the Retriever model (Dr.Decr) to find documents in the index.

Test Reading

Reading finds an answer only from the provided context information. Select the Reading icon on the left and query ‘Did Mother link cats?’, providing the context:

	
"My father and the cat became good friends but my father's mother was very upset about the cat. She hated cats, particularly ugly old alley cats. ""Elmer Elevator,"" she said to my father, ""if you think I'm going to give that cat a saucer of milk, you're very wrong. Once you start feeding stray alley cats you might as well expect to feed every stray in town, and I am not going to do it!""This made my father very sad, and he apologized to the cat because his mother had been so rude. He told the cat to stay anyway, and that somehow he would bring her a saucer of milk each day. My father fed the cat for three weeks, but one day his mother found the cat's saucer in the cellar and she was extremely angry. She whipped my father and threw the cat out the door, but later on my father sneaked out and found the cat."


The answer ‘She hated cats’ will be generated only from the context provided (in this case a document from the index).

This uses the Reader model (nq_tydi_sq1-reader-xlmr_large-20221110).

Test Question Answering

Question Answering proposes a short answer and presents the document from the index which contained the information. There are various settings which can influence the results, for example the minimum/maximum number of tokens for the answer. In this example, I reduced the number of answer tokens as I wanted to encourage short answers listing the animals which the father met.

Select the QA icon on the left and query ‘What animals did Father meet?’.

This uses the Retriever model (Dr.Decr) to find documents in the index, and the Reader model (nq_tydi_sq1-reader-xlmr_large-20221110) to propose a specific answer to the question.

 IBM Watson for Embed, General Information
 ai nlp
This post is licensed under CC BY 4.0 by the author.
Share     
Further Reading
Mar 3, 2023
NLP Capabilities with Watson NLP Library for Embed

What are the basics of NLP? What are the specific NLP capabilities that can be achieved with Watson NLP Library for Embed? Find out more in this blog. In a recent blog posts I explained the capabi...

Jan 1, 2023
Introducing IBM Watson for Embed

IBM has recently released a framework that is specifically designed for developers to embed AI into their solutions. IBM Watson for Embed lowers the barrier for AI adoption by helping address the ...

Jan 1, 2023
Deploying IBM Watson NLP to Kubernetes with OpenShift

In this blog, I will demonstrate how to deploy the Watson for NLP Library to OpenShift using either Kubernetes resources in yaml files, or using a helm chart. For initial context, read my blog int...

NLP Capabilities with Watson NLP Library for Embed

Combining Watson Studio Jobs with KServe Modelmesh

© 2023 Adam de Leeuw. Some rights reserved.

Using the Jekyll theme Chirpy.

## Metadata

```json
{
  "title": "Using PrimeQA For NLP Question Answering",
  "description": "Question Answering models are one of the mainstays of NLP. In this blog I demonstrate how to use the open-source project PrimeQA to install a framework which indexes data, and provides a Q&A capability which can easy be incorporated into an application.",
  "url": "https://www.deleeuw.me.uk/posts/Using-PrimeQA-For-NLP-Question-Answering/",
  "content": "Adam de Leeuw\nDocumenting my experiences in IT\nHOME\nCATEGORIES\nTAGS\nARCHIVES\nOPENSOURCE\nABOUT\t\nHome  Using PrimeQA For NLP Question Answering\nUsing PrimeQA For NLP Question Answering\nPosted Mar 13, 2023  Updated Mar 14, 2023\nBy Adam de Leeuw\n9 min read\n\nQuestion Answering models are one of the mainstays of NLP. In this blog I demonstrate how to use the open-source project PrimeQA to install a framework which indexes data, and provides a Q&A capability which can easy be incorporated into an application.\n\nWhat is PrimeQA?\n\nPrimeQA is a public open source repository that enables you to train state-of-the-art models for question answering (QA). PrimeQA can perform document retrieval and reading comprehension based on neural networks. It provides a front-end UI search engine, in addition to APIs.\n\nRequirements for Installing PrimeQA\nUbuntu Linux 20.04.4 LTS VM - Although primeQA recommend a high specification, I used a more modest 4vCPU, 16GB RAM without GPU\nDocker\nGit\nPython & pip\nJava 11 JDK\nInstal Pre-requites\n\nInstall Docker\n\nInstall Docker Compose:\n\n1\n\n\t\napt  install docker-compose\n\n\nInstall git:\n\n1\n\n\t\napt install git\n\n\nInstall Python & pip:\n\n1\n2\n\n\t\napt install python3-pip\napt-get install python3-venv\n\n\nInstall Java 11 JDK:\n\n1\n\n\t\napt-get install openjdk-11-jdk\n\nInstalling PrimeQA on Ubuntu\n\nClone the create-primea-app repo:\n\n1\n2\n3\n\n\t\nmkdir /root/gitRepos\ncd /root/gitRepos\ngit clone https://github.com/primeqa/create-primeqa-app\n\n\nSet an environment variable to your public IP. This can be localhost if you plan to use a browser locally on Ubuntu via VNC:\n\n1\n\n\t\nexport PUBLIC_IP=<your IP or localhost>\n\n\nLaunch primeQA by launching three container images. Use the -m gpu only if your Ubuntu host includes a GPU:\n\n1\n2\n\n\t\ncd create-primeqa-app\n./launch.sh [-m gpu]\n\n\nValidate the three containers started:\n\n1\n\n\t\ndocker ps\n\n\nThe containers run the following components:\n\nprimeqa/services: a gRPC/REST service layer on top of PrimeQA\nprimeqa/orchestrator: an integration service for PrimeQA capabilities and external services\nprimeqa/ui: ReactJS webapp providing a example UI\n\nEnsure that ports 50051, 50059 and 82 are accessible. If you plan to access the web Ui via a public IP and you’re using a cloud virtual server, you may need to edit the network security (e.g. Security Group on IBM Cloud).\n\nSettings are in the orchestrator-store/primeqa.json. Edit this file as follows:\n\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n\n\t\n{\n    \"application_id\": \"primeqa\",\n    \"name\": \"PrimeQA\",\n    \"description\": \"PrimeQA is a public open source repository that enables researchers and developers to train state-of-the-art models for question answering (QA).\",\n    \"settings\": {\n        \"retrievers\": {\n\t  \"PrimeQA\": {\n            \"service_endpoint\": \"primeqa:50051\"\n          }\n        },\n        \"readers\": {\n\t  \"PrimeQA\": {\n            \"service_endpoint\": \"primeqa:50051\",\t\n            \"beta\": 0.7\n          }\n        }\n    }\n}\n\n\nThis sets the Reader and Retriever processes to be provided locally by primeQA. It is possible to also add a configuration for Watson Discovery for the Reader. I’ll explain later what the Reader and Retriever components do.\n\nPreparing the Corpus\n\nPrimeQA supports different models for information retrieval (provided by the Reader component of primeQA):\n\nThere are two Dense IR engines supported: ColBERT and Direct Passage Retrieval (DPR).\nSparse IR is a Pyserini-based IR Engine enabling BM25 ranking using bag of words representation.\n\nIn this tutorial, we will use Dr.Decr, a ColBERT based fine-tuned language model to create an index. It expects the corpus to be a collection of documents in a tsv file, in a tabular id text title arrangement, ideally in the 1-180 word range. The primeqa repo provides some sample scripts to help prepare the data into this format. The scripts are designed for another book which is no longer available in the public domain, but this is a good starting point.\n\nFor this blog, I used the following dataset from Kaggle. It contains multiple stories, but I copied lines 67331-67543 to a new file Book1.txt, giving me just one story, “MY FATHER’S DRAGON” which is public domain.\n\n1\n2\n3\n\n\t\ncd /root/gitRepos/create-primeqa-app/examples\ncp -R harry-potter-corpus my_fathers_dragon\ncd my_fathers_dragon\n\n\nCopy Book1.txt from your workstation to /examples/my_fathers_dragon.\n\nInstall the pre-requisites for processing the corpus:\n\n1\n2\n3\n4\n5\n6\n7\n8\n\n\t\nalias pip=pip3\nalias python=python3\npython -m venv .env           # will create directory .env\nsource .env/bin/activate      # activate virtualenv\npip install primeqa\npip install --upgrade pip\npip install spacy             \npython -m spacy download en_core_web_sm\n\n\nProcess the corpus:\n\n1\n\n\t\n./process.sh\n\n\nThe resulting corpus.tsv looks like this:\n\n1\n2\n3\n\n\t\nid\ttext\ttitle\n1\t\"MY FATHER'S DRAGON MY FATHER MEETS THE CAT One cold rainy day when my father was a little boy, he met an old alley cat on his street. The cat was very drippy and uncomfortable so my father said, \"\"Wouldn't you like to come home with me?\"\"This surprised the cat she had never before met anyone who cared about old alley cats but she said, \"\"I'd be very much obliged if I could sit by a warm furnace, and perhaps have a saucer of milk.\"\"\"\"We have a very nice furnace to sit by,\"\" said my father, \"\"and I'm sure my mother has an extra saucer of milk.\"\"\"\tBook1 Paragraph 1\n2\t\"My father and the cat became good friends but my father's mother was very upset about the cat. She hated cats, particularly ugly old alley cats. \"\"Elmer Elevator,\"\" she said to my father, \"\"if you think I'm going to give that cat a saucer of milk, you're very wrong. Once you start feeding stray alley cats you might as well expect to feed every stray in town, and I am not going to do it!\"\"This made my father very sad, and he apologized to the cat because his mother had been so rude. He told the cat to stay anyway, and that somehow he would bring her a saucer of milk each day. My father fed the cat for three weeks, but one day his mother found the cat's saucer in the cellar and she was extremely angry. She whipped my father and threw the cat out the door, but later on my father sneaked out and found the cat.\"\tBook1 Paragraph 2\n\nPackage the corpus, index and models\n\nThe corpus, index and model need to be installed into the ‘PrimeQA store’ which is located in directory primeqa-store.\n\nThe model used as the Reader is not installed by default. Run the following script to download it to /examples/my_fathers_dragon:\n\n1\n\n\t\n./download-model.sh\n\n\nRun the following script to copy the model to a new location in primeqa-store.\n\n1\n\n\t\nCHECKPOINT=$(./setup-checkpoint.sh DrDecr.dnn ../../primeqa-store)\n\n\nThe script returns a path which is stored in the CHECKPOINT variable for later use. Display the value with echo $CHECKPOINT and make a note of it.\n\nNext, invoke a script which uses the DrDecr model to create an index, and copy the files to the primeqa-store directory. In addition, an SQLite database is created.\n\n1\n\n\t\n./setup-index.sh \"${CHECKPOINT}\" corpus.tsv ../../primeqa-store/\n\n\nThe setup-index.sh script created one or more directories at `primeqa-store/indexes/`.\n\nIf you find there are multiple directories with names such as 9329c257-a514-48a7-ac03-c53a05e3ec5f, inspect each one in turn to determine if there are files in the subdirectory 9329c257-a514-48a7-ac03-c53a05e3ec5f/index. If this is empty, the directory is not required and can be deleted. Repeat this process until only one directory remains, which should have a populated `index` subdirectory.\n\nRename the directory:\n\n1\n2\n\n\t\ncd /root/gitRepos/create-primeqa-app/primeqa-store/indexes\nmv <indexname> my_fathers_dragon\n\n\nThe setup-index.sh script also created file primeqa-store/indexes/<indexname>/information.json. At the time of writing, this file has been created incorrectly. Replace the contents so it looks like this:\n\n1\n2\n3\n4\n5\n6\n7\n8\n\n\t\n{\n  \"index_id\": \"my_fathers_dragon\",\n  \"status\": \"READY\",\n  \"configuration\": {\n    \"engine_type\": \"ColBERT\",\n    \"checkpoint\": \"<penultimate directory of your $CHECKPOINT path, e.g. ColBERTIndexer_20230308101308>\"  \n  }\n}\n\nRestart primeQA\n\nIt may not be strictly necessary, but after making the configuration I restarted the containers:\n\n\t\ncd /root/gitRepos/create-primeqa-app\n./terminate.sh\n./launch.sh\n\nTesting with PrimeQA UI\n\nOpen a browser to PUBLIC_IP:82/qa.\n\nTo help with composing some test searching, you can read a brief summary of My Father Met a Dragon.\n\nAs you test the three capabilities below (Retrieval, Reading, Question Answering), you will notice the first query takes a long time. This is because primeQA is downloading models in the background. These are the transformer (large language) models used for Reading and Question Answering. PrimeQA allows these models can be replaced according to the specific requirements.\n\nYou will see the model appear here create-primeqa-app/cache/huggingface/hub:\n\n1\n2\n3\n\n\t\n-rwxrwxrwx 1 2000 2000    1 Mar 14 09:21 version.txt\ndrwxr-xr-x 6 2000 2000 4096 Mar 14 13:39 models--xlm-roberta-base\ndrwxr-xr-x 6 2000 2000 4096 Mar 14 13:41 models--PrimeQA--nq_tydi_sq1-reader-xlmr_large-20221110\n\nTest Retrieval\n\nRetrieval searches the document index. Select the Retrieval icon on the left and query ‘What animals did Father meet?’.\n\nYou will see documents from the index which mention the animals such as cat, bear, rhinoceras, lion, monkey etc. However you do not get one word answers.\n\nThis uses the Retriever model (Dr.Decr) to find documents in the index.\n\nTest Reading\n\nReading finds an answer only from the provided context information. Select the Reading icon on the left and query ‘Did Mother link cats?’, providing the context:\n\n\t\n\"My father and the cat became good friends but my father's mother was very upset about the cat. She hated cats, particularly ugly old alley cats. \"\"Elmer Elevator,\"\" she said to my father, \"\"if you think I'm going to give that cat a saucer of milk, you're very wrong. Once you start feeding stray alley cats you might as well expect to feed every stray in town, and I am not going to do it!\"\"This made my father very sad, and he apologized to the cat because his mother had been so rude. He told the cat to stay anyway, and that somehow he would bring her a saucer of milk each day. My father fed the cat for three weeks, but one day his mother found the cat's saucer in the cellar and she was extremely angry. She whipped my father and threw the cat out the door, but later on my father sneaked out and found the cat.\"\n\n\nThe answer ‘She hated cats’ will be generated only from the context provided (in this case a document from the index).\n\nThis uses the Reader model (nq_tydi_sq1-reader-xlmr_large-20221110).\n\nTest Question Answering\n\nQuestion Answering proposes a short answer and presents the document from the index which contained the information. There are various settings which can influence the results, for example the minimum/maximum number of tokens for the answer. In this example, I reduced the number of answer tokens as I wanted to encourage short answers listing the animals which the father met.\n\nSelect the QA icon on the left and query ‘What animals did Father meet?’.\n\nThis uses the Retriever model (Dr.Decr) to find documents in the index, and the Reader model (nq_tydi_sq1-reader-xlmr_large-20221110) to propose a specific answer to the question.\n\n IBM Watson for Embed, General Information\n ai nlp\nThis post is licensed under CC BY 4.0 by the author.\nShare     \nFurther Reading\nMar 3, 2023\nNLP Capabilities with Watson NLP Library for Embed\n\nWhat are the basics of NLP? What are the specific NLP capabilities that can be achieved with Watson NLP Library for Embed? Find out more in this blog. In a recent blog posts I explained the capabi...\n\nJan 1, 2023\nIntroducing IBM Watson for Embed\n\nIBM has recently released a framework that is specifically designed for developers to embed AI into their solutions. IBM Watson for Embed lowers the barrier for AI adoption by helping address the ...\n\nJan 1, 2023\nDeploying IBM Watson NLP to Kubernetes with OpenShift\n\nIn this blog, I will demonstrate how to deploy the Watson for NLP Library to OpenShift using either Kubernetes resources in yaml files, or using a helm chart. For initial context, read my blog int...\n\nNLP Capabilities with Watson NLP Library for Embed\n\nCombining Watson Studio Jobs with KServe Modelmesh\n\n© 2023 Adam de Leeuw. Some rights reserved.\n\nUsing the Jekyll theme Chirpy.",
  "publishedTime": "2023-03-13T09:00:00+00:00",
  "usage": {
    "tokens": 3071
  }
}
```
