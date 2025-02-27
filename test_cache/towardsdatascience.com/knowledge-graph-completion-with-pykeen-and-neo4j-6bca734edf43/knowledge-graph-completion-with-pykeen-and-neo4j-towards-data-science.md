---
title: Knowledge graph completion with PyKEEN and Neo4j - Towards Data Science
description: A couple of weeks ago, I met Francois Vanderseypen, a Graph Data Science consultant. We decided to join forces and start a Graph Machine learning blog series. This blog post will present how to…
url: https://towardsdatascience.com/knowledge-graph-completion-with-pykeen-and-neo4j-6bca734edf43
timestamp: 2025-01-20T15:44:03.605Z
domain: towardsdatascience.com
path: knowledge-graph-completion-with-pykeen-and-neo4j-6bca734edf43
---

# Knowledge graph completion with PyKEEN and Neo4j - Towards Data Science


A couple of weeks ago, I met Francois Vanderseypen, a Graph Data Science consultant. We decided to join forces and start a Graph Machine learning blog series. This blog post will present how to…


## Content

Integrate PyKEEN library with Neo4j for multi-class link prediction using knowledge graph embedding models
----------------------------------------------------------------------------------------------------------

[![Image 24: Tomaz Bratanic](https://miro.medium.com/v2/resize:fill:88:88/1*SnWQP0l4Vg9577WAErbjfw.jpeg)](https://bratanic-tomaz.medium.com/?source=post_page---byline--6bca734edf43--------------------------------)

[![Image 25: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--6bca734edf43--------------------------------)

A couple of weeks ago, I met [Francois Vanderseypen](https://www.linkedin.com/in/francoisvanderseypen/), a Graph Data Science consultant. We decided to join forces and start a Graph Machine learning blog series. This blog post will present how to perform knowledge graph completion, which is simply a multi-class link prediction. Instead of just predicting a link, we are also trying to predict its type.

![Image 26](https://miro.medium.com/v2/resize:fit:371/1*DtYv3ff7gj2YoUHftT8WIg.png)

Knowledge graph completion example. Image by the author.

For knowledge graph completion, the underlying graph should contain multiple types of relationships. Otherwise, if you are dealing with only a single kind of relationship, you can use the [standard link prediction techniques](https://towardsdatascience.com/a-deep-dive-into-neo4j-link-prediction-pipeline-and-fastrp-embedding-algorithm-bf244aeed50d) that do not consider the relationship type. The example visualization has only a single node type, but in practice, your input graph can consists of multiple node types as well.

We have to use the knowledge graph embedding models for a multi-class link prediction pipeline instead of plain node embedding models.  
What’s the difference, you may ask.  
While node embedding models embed only nodes, the knowledge graph embedding models embed both nodes and relationships.

![Image 27](https://miro.medium.com/v2/resize:fit:692/1*rjikcW1dj__vTtSLjOBMbw.png)

Embedding nodes and relationships via knowledge graph embedding models. Image by author.

The standard syntax to describe the pattern is that the starting node is called head (h), the end or target node is referred to as tail (t), and the relationship is r.

The intuition behind the knowledge graph embedding model such as [TransE](https://proceedings.neurips.cc/paper/2013/file/1cecc7a77928ca8133fa24680a88d2f9-Paper.pdf) is that the embedding of the head plus the relationship is close to the embedding of the tail if the relationship is present.

![Image 28](https://miro.medium.com/v2/resize:fit:309/1*jQqX2g_BcBwjvl58Uj1HmQ.gif)

Image by the author.

The predictions are then quite simple. For example, if you want to predict new relationships for a specific node, you just sum the node plus the relationship embedding and evaluate if any of the nodes are near the embedding sum.

For more detailed information about knowledge graph embedding models, I suggest you check out the following lecture by Jure Leskovec.

Agenda
------

If you read any of my previous blog posts, you might know that I like to use Neo4j, a native graph database, to store data. You will then use the Neo4j Python driver to fetch the data and transform it into a [PyKE](https://github.com/pykeen/pykeen)EN graph. PyKEEN is a Python library that features knowledge graph embedding models and simplifies multi-class link prediction task executions. Lastly, you will store the predictions back to Neo4j and evaluate the results.

I have prepared a [Jupyter notebook](https://github.com/tomasonjo/blogs/blob/master/pykeen/Hetionet%20-%20RotatE.ipynb) that contains all the code in this post.

Prepare the data in Neo4j Desktop
---------------------------------

We will be using a subset of the [Hetionet](https://het.io/) dataset. If you want to learn more about the dataset, check out the [original paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5640425/).

To follow along with this tutorial, I recommend you download the Neo4j Desktop application.

Once you have installed the Neo4j Desktop, you can [download the database dump](https://drive.google.com/file/d/1u34cFBYvBtdBsqOUPdmbcIyIt88IiZYe/view?usp=sharing) and use it to restore a database instance.

![Image 29](https://miro.medium.com/v2/resize:fit:700/1*zDFNiH4LzfLaAdfyf-cVDg.png)

Restore a database dump in Neo4j Desktop. Image by author.

If you need a bit more help with restoring the dump file, I’ve written a [blog post](https://tbgraph.wordpress.com/2020/11/11/dump-and-load-a-database-in-neo4j-desktop/) about it about a year ago.

If you have successfully restored the database dump, you can open the Neo4j Browser and execute the following command.

CALL db.schema.visualization()

The procedure should visualize the following graph schema.

![Image 30](https://miro.medium.com/v2/resize:fit:700/1*Lt-XJRTEuJLRvDcXPMiq_Q.png)

Graph model. Image by author.

Our subset of the Hetionet graph contains genes, compounds, and diseases. There are many relationships between them, and you would probably need to be in the biomedical domain to understand them, so I won’t go into details.

In our case, the most important relationship is the **treats** relationship between compounds and diseases. This blog post will use the knowledge graph embedding models to predict new **treats** relationships. You could think of this scenario as a drug repurposing task.

PyKEEN
------

PyKEEN is an incredible, simple-to-use library that can be used for knowledge graph completion tasks.  
Currently, it features 35 knowledge graph embedding models and even supports out-of-the-box hyper-parameter optimizations.  
I like it due to its high-level interface, making it very easy to construct a PyKEEN graph and train an embedding model.  
Check out its GitHub repository for more information.

Transform a Neo4j to a PyKEEN graph
-----------------------------------

Now we will move on to the practical part of this post.

First, we will transform the Neo4j graph to the PyKEEN graph and split the train-test data. To begin, we have to define the connection to the Neo4j database.

The `run_query` function executes a Cypher query and returns the output in the form of a Pandas dataframe. The PyKEEN library has a `from_labeled_triples` that takes a list of triples as an input and constructs a graph from it.

This example has a generic Cypher query that can be used to fetch any Neo4j dataset and construct a PyKEEN from it. Notice that we use the internal Neo4j ids of nodes to build the triples data frame. For some reason, the PyKEEN library expects the triple elements to be all strings, so we simply cast the internal ids to string. Learn more about how to construct the triples and the available parameters in the [official documentation](https://pykeen.readthedocs.io/en/stable/reference/triples.html).

Now that we have our PyKEEN graph, we can use the `split` method to perform the train-test data split.

It couldn’t get any easier than this. I must congratulate the PyKEEN authors for developing such a straightforward interface.

Train a knowledge graph embedding model
---------------------------------------

Now that we have the train-test data available, we can go ahead and train a knowledge graph embedding model. We will use the [RotatE](https://arxiv.org/abs/1902.10197) model in this example. I am not that familiar with all the variations of the embedding models, but if you want to learn more, I would suggest the lecture by Jure Leskovec I linked above.

We won’t perform any hyper-parameter optimization to keep the tutorial simple. I’ve chosen to use 20 epochs and defined the dimension size to be 512.

_p.s. I’ve later learned that 20 epochs probably isn’t enough to get meaningful training on a large, complex graph; especially with such a high dimensionality._

Multi-class link prediction
---------------------------

The PyKEEN library supports multiple methods for multi-class link prediction.  
You could find the top K predictions in the network, or you can be more specific and define a particular head node and relationship type and evaluate if there are any new connections predicted.

In this example, you will predict new **treats** relationships for the **L-Asparagine** compound. Because we used the internal node ids for mapping, we first have to retrieve the node id of L-Asparagine from Neo4j and input it into the prediction method.

Store predictions to Neo4j
--------------------------

For easier evaluation of the results, we will store the top five predictions back to Neo4j.

You can now open the Neo4j Browser and run the following Cypher statement to inspect the results.

MATCH p=(:Compound)-\[:PREDICTED\_TREATS\]-\>(d:Disease)  
RETURN p

_Results_

![Image 31](https://miro.medium.com/v2/resize:fit:446/1*MLkS1TAdQLvpAPAG37aXpw.png)

Predicted treats relationship between L-Asparagine and top five diseases. Image by the author.

As I am not a medical doctor, I can’t say if the predictions make sense or not. In the biomedical domain, link prediction is part of the scientific process of generating hypotheses and not blindly believing the results.

Explaining predictions
----------------------

As far as I know, the knowledge graph embedding model is not that useful for explaining predictions. On the other hand, you could use the existing connections in the graph to present the information to a medical doctor and let him decide if the predictions make sense or not.

For example, you could investigate direct and indirect paths between **L-Asparagine** and **colon cancer** with the following Cypher query.

MATCH (c:Compound {name: "L-Asparagine"}),(d:Disease {name:"colon cancer"})  
WITH c,d  
MATCH p=AllShortestPaths((c)-\[r:binds|regulates|interacts|upregulates|downregulates|associates\*1..4\]-(d))  
RETURN p LIMIT 25

_Results_

On the left side, we have the colon cancer, and on the right side there is the L-Asparagine node. In the middle of the visualization there are genes that connect the two nodes.

Out of curiosity, I’ve googled L-Asparagine in combination with colon cancer and came across this article from 2019.

While my layman’s eyes don’t really comprehend if asparagine should be increased or decreased to help with the disease, it at least looks like there seems to be a relation between the two.

Conclusion
----------

Most of the time, you deal with graphs with multiple relationship types. Therefore, knowledge graph embedding models are handy for multi-class link prediction tasks, where you want to predict a new link and its type. For example, there is a big difference if the predicted link type is **treats** or **causes**.

The transformation from Neo4j to PyKEEN graph is generic and will work on any dataset. So I encourage you to try it out and give me some feedback on which use-cases you found interesting.

As always, the code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/pykeen/Hetionet%20-%20RotatE.ipynb).

References
----------

*   Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J., & Yakhnenko, O. (2013). Translating Embeddings for Modeling Multi-relational Data. In _Advances in Neural Information Processing Systems_. Curran Associates, Inc..
*   Himmelstein, Daniel Scott et al. “Systematic integration of biomedical knowledge prioritizes drugs for repurposing.” _eLife_ vol. 6 e26726. 22 Sep. 2017, doi:10.7554/eLife.26726
*   Ali, M., Berrendorf, M., Hoyt, C., Vermue, L., Galkin, M., Sharifzadeh, S., Fischer, A., Tresp, V., & Lehmann, J. (2020). Bringing Light Into the Dark: A Large-scale Evaluation of Knowledge Graph Embedding Models Under a Unified Framework_. arXiv preprint arXiv:2006.13365_.
*   Zhiqing Sun, Zhi-Hong Deng, Jian-Yun Nie, & Jian Tang. (2019). RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space.
*   Du, Feng et al. “SOX12 promotes colorectal cancer cell proliferation and metastasis by regulating asparagine synthesis.” _Cell death & disease_ vol. 10,3 239. 11 Mar. 2019, doi:10.1038/s41419–019–1481–9

## Metadata

```json
{
  "title": "Knowledge graph completion with PyKEEN and Neo4j - Towards Data Science",
  "description": "A couple of weeks ago, I met Francois Vanderseypen, a Graph Data Science consultant. We decided to join forces and start a Graph Machine learning blog series. This blog post will present how to…",
  "url": "https://towardsdatascience.com/knowledge-graph-completion-with-pykeen-and-neo4j-6bca734edf43",
  "content": "Integrate PyKEEN library with Neo4j for multi-class link prediction using knowledge graph embedding models\n----------------------------------------------------------------------------------------------------------\n\n[![Image 24: Tomaz Bratanic](https://miro.medium.com/v2/resize:fill:88:88/1*SnWQP0l4Vg9577WAErbjfw.jpeg)](https://bratanic-tomaz.medium.com/?source=post_page---byline--6bca734edf43--------------------------------)\n\n[![Image 25: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--6bca734edf43--------------------------------)\n\nA couple of weeks ago, I met [Francois Vanderseypen](https://www.linkedin.com/in/francoisvanderseypen/), a Graph Data Science consultant. We decided to join forces and start a Graph Machine learning blog series. This blog post will present how to perform knowledge graph completion, which is simply a multi-class link prediction. Instead of just predicting a link, we are also trying to predict its type.\n\n![Image 26](https://miro.medium.com/v2/resize:fit:371/1*DtYv3ff7gj2YoUHftT8WIg.png)\n\nKnowledge graph completion example. Image by the author.\n\nFor knowledge graph completion, the underlying graph should contain multiple types of relationships. Otherwise, if you are dealing with only a single kind of relationship, you can use the [standard link prediction techniques](https://towardsdatascience.com/a-deep-dive-into-neo4j-link-prediction-pipeline-and-fastrp-embedding-algorithm-bf244aeed50d) that do not consider the relationship type. The example visualization has only a single node type, but in practice, your input graph can consists of multiple node types as well.\n\nWe have to use the knowledge graph embedding models for a multi-class link prediction pipeline instead of plain node embedding models.  \nWhat’s the difference, you may ask.  \nWhile node embedding models embed only nodes, the knowledge graph embedding models embed both nodes and relationships.\n\n![Image 27](https://miro.medium.com/v2/resize:fit:692/1*rjikcW1dj__vTtSLjOBMbw.png)\n\nEmbedding nodes and relationships via knowledge graph embedding models. Image by author.\n\nThe standard syntax to describe the pattern is that the starting node is called head (h), the end or target node is referred to as tail (t), and the relationship is r.\n\nThe intuition behind the knowledge graph embedding model such as [TransE](https://proceedings.neurips.cc/paper/2013/file/1cecc7a77928ca8133fa24680a88d2f9-Paper.pdf) is that the embedding of the head plus the relationship is close to the embedding of the tail if the relationship is present.\n\n![Image 28](https://miro.medium.com/v2/resize:fit:309/1*jQqX2g_BcBwjvl58Uj1HmQ.gif)\n\nImage by the author.\n\nThe predictions are then quite simple. For example, if you want to predict new relationships for a specific node, you just sum the node plus the relationship embedding and evaluate if any of the nodes are near the embedding sum.\n\nFor more detailed information about knowledge graph embedding models, I suggest you check out the following lecture by Jure Leskovec.\n\nAgenda\n------\n\nIf you read any of my previous blog posts, you might know that I like to use Neo4j, a native graph database, to store data. You will then use the Neo4j Python driver to fetch the data and transform it into a [PyKE](https://github.com/pykeen/pykeen)EN graph. PyKEEN is a Python library that features knowledge graph embedding models and simplifies multi-class link prediction task executions. Lastly, you will store the predictions back to Neo4j and evaluate the results.\n\nI have prepared a [Jupyter notebook](https://github.com/tomasonjo/blogs/blob/master/pykeen/Hetionet%20-%20RotatE.ipynb) that contains all the code in this post.\n\nPrepare the data in Neo4j Desktop\n---------------------------------\n\nWe will be using a subset of the [Hetionet](https://het.io/) dataset. If you want to learn more about the dataset, check out the [original paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5640425/).\n\nTo follow along with this tutorial, I recommend you download the Neo4j Desktop application.\n\nOnce you have installed the Neo4j Desktop, you can [download the database dump](https://drive.google.com/file/d/1u34cFBYvBtdBsqOUPdmbcIyIt88IiZYe/view?usp=sharing) and use it to restore a database instance.\n\n![Image 29](https://miro.medium.com/v2/resize:fit:700/1*zDFNiH4LzfLaAdfyf-cVDg.png)\n\nRestore a database dump in Neo4j Desktop. Image by author.\n\nIf you need a bit more help with restoring the dump file, I’ve written a [blog post](https://tbgraph.wordpress.com/2020/11/11/dump-and-load-a-database-in-neo4j-desktop/) about it about a year ago.\n\nIf you have successfully restored the database dump, you can open the Neo4j Browser and execute the following command.\n\nCALL db.schema.visualization()\n\nThe procedure should visualize the following graph schema.\n\n![Image 30](https://miro.medium.com/v2/resize:fit:700/1*Lt-XJRTEuJLRvDcXPMiq_Q.png)\n\nGraph model. Image by author.\n\nOur subset of the Hetionet graph contains genes, compounds, and diseases. There are many relationships between them, and you would probably need to be in the biomedical domain to understand them, so I won’t go into details.\n\nIn our case, the most important relationship is the **treats** relationship between compounds and diseases. This blog post will use the knowledge graph embedding models to predict new **treats** relationships. You could think of this scenario as a drug repurposing task.\n\nPyKEEN\n------\n\nPyKEEN is an incredible, simple-to-use library that can be used for knowledge graph completion tasks.  \nCurrently, it features 35 knowledge graph embedding models and even supports out-of-the-box hyper-parameter optimizations.  \nI like it due to its high-level interface, making it very easy to construct a PyKEEN graph and train an embedding model.  \nCheck out its GitHub repository for more information.\n\nTransform a Neo4j to a PyKEEN graph\n-----------------------------------\n\nNow we will move on to the practical part of this post.\n\nFirst, we will transform the Neo4j graph to the PyKEEN graph and split the train-test data. To begin, we have to define the connection to the Neo4j database.\n\nThe `run_query` function executes a Cypher query and returns the output in the form of a Pandas dataframe. The PyKEEN library has a `from_labeled_triples` that takes a list of triples as an input and constructs a graph from it.\n\nThis example has a generic Cypher query that can be used to fetch any Neo4j dataset and construct a PyKEEN from it. Notice that we use the internal Neo4j ids of nodes to build the triples data frame. For some reason, the PyKEEN library expects the triple elements to be all strings, so we simply cast the internal ids to string. Learn more about how to construct the triples and the available parameters in the [official documentation](https://pykeen.readthedocs.io/en/stable/reference/triples.html).\n\nNow that we have our PyKEEN graph, we can use the `split` method to perform the train-test data split.\n\nIt couldn’t get any easier than this. I must congratulate the PyKEEN authors for developing such a straightforward interface.\n\nTrain a knowledge graph embedding model\n---------------------------------------\n\nNow that we have the train-test data available, we can go ahead and train a knowledge graph embedding model. We will use the [RotatE](https://arxiv.org/abs/1902.10197) model in this example. I am not that familiar with all the variations of the embedding models, but if you want to learn more, I would suggest the lecture by Jure Leskovec I linked above.\n\nWe won’t perform any hyper-parameter optimization to keep the tutorial simple. I’ve chosen to use 20 epochs and defined the dimension size to be 512.\n\n_p.s. I’ve later learned that 20 epochs probably isn’t enough to get meaningful training on a large, complex graph; especially with such a high dimensionality._\n\nMulti-class link prediction\n---------------------------\n\nThe PyKEEN library supports multiple methods for multi-class link prediction.  \nYou could find the top K predictions in the network, or you can be more specific and define a particular head node and relationship type and evaluate if there are any new connections predicted.\n\nIn this example, you will predict new **treats** relationships for the **L-Asparagine** compound. Because we used the internal node ids for mapping, we first have to retrieve the node id of L-Asparagine from Neo4j and input it into the prediction method.\n\nStore predictions to Neo4j\n--------------------------\n\nFor easier evaluation of the results, we will store the top five predictions back to Neo4j.\n\nYou can now open the Neo4j Browser and run the following Cypher statement to inspect the results.\n\nMATCH p=(:Compound)-\\[:PREDICTED\\_TREATS\\]-\\>(d:Disease)  \nRETURN p\n\n_Results_\n\n![Image 31](https://miro.medium.com/v2/resize:fit:446/1*MLkS1TAdQLvpAPAG37aXpw.png)\n\nPredicted treats relationship between L-Asparagine and top five diseases. Image by the author.\n\nAs I am not a medical doctor, I can’t say if the predictions make sense or not. In the biomedical domain, link prediction is part of the scientific process of generating hypotheses and not blindly believing the results.\n\nExplaining predictions\n----------------------\n\nAs far as I know, the knowledge graph embedding model is not that useful for explaining predictions. On the other hand, you could use the existing connections in the graph to present the information to a medical doctor and let him decide if the predictions make sense or not.\n\nFor example, you could investigate direct and indirect paths between **L-Asparagine** and **colon cancer** with the following Cypher query.\n\nMATCH (c:Compound {name: \"L-Asparagine\"}),(d:Disease {name:\"colon cancer\"})  \nWITH c,d  \nMATCH p=AllShortestPaths((c)-\\[r:binds|regulates|interacts|upregulates|downregulates|associates\\*1..4\\]-(d))  \nRETURN p LIMIT 25\n\n_Results_\n\nOn the left side, we have the colon cancer, and on the right side there is the L-Asparagine node. In the middle of the visualization there are genes that connect the two nodes.\n\nOut of curiosity, I’ve googled L-Asparagine in combination with colon cancer and came across this article from 2019.\n\nWhile my layman’s eyes don’t really comprehend if asparagine should be increased or decreased to help with the disease, it at least looks like there seems to be a relation between the two.\n\nConclusion\n----------\n\nMost of the time, you deal with graphs with multiple relationship types. Therefore, knowledge graph embedding models are handy for multi-class link prediction tasks, where you want to predict a new link and its type. For example, there is a big difference if the predicted link type is **treats** or **causes**.\n\nThe transformation from Neo4j to PyKEEN graph is generic and will work on any dataset. So I encourage you to try it out and give me some feedback on which use-cases you found interesting.\n\nAs always, the code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/pykeen/Hetionet%20-%20RotatE.ipynb).\n\nReferences\n----------\n\n*   Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J., & Yakhnenko, O. (2013). Translating Embeddings for Modeling Multi-relational Data. In _Advances in Neural Information Processing Systems_. Curran Associates, Inc..\n*   Himmelstein, Daniel Scott et al. “Systematic integration of biomedical knowledge prioritizes drugs for repurposing.” _eLife_ vol. 6 e26726. 22 Sep. 2017, doi:10.7554/eLife.26726\n*   Ali, M., Berrendorf, M., Hoyt, C., Vermue, L., Galkin, M., Sharifzadeh, S., Fischer, A., Tresp, V., & Lehmann, J. (2020). Bringing Light Into the Dark: A Large-scale Evaluation of Knowledge Graph Embedding Models Under a Unified Framework_. arXiv preprint arXiv:2006.13365_.\n*   Zhiqing Sun, Zhi-Hong Deng, Jian-Yun Nie, & Jian Tang. (2019). RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space.\n*   Du, Feng et al. “SOX12 promotes colorectal cancer cell proliferation and metastasis by regulating asparagine synthesis.” _Cell death & disease_ vol. 10,3 239. 11 Mar. 2019, doi:10.1038/s41419–019–1481–9",
  "publishedTime": "2021-12-11T17:53:40.718Z",
  "usage": {
    "tokens": 2946
  }
}
```
