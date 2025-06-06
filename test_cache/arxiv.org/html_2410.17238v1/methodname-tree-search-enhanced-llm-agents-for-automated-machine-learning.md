---
title: \methodname: Tree-Search Enhanced LLM Agents for Automated Machine Learning
description: 
url: https://arxiv.org/html/2410.17238v1
timestamp: 2025-01-20T16:14:33.435Z
domain: arxiv.org
path: html_2410.17238v1
---

# \methodname: Tree-Search Enhanced LLM Agents for Automated Machine Learning



## Content

1Introduction
2Related Works
3Method
4Experiments
5Conclusion
\methodname: Tree-Search Enhanced LLM Agents for Automated Machine Learning
Yizhou Chi1,2, Yizhang Lin11, Sirui Hong1, Duyi Pan3, Yaying Fei, Guanghao Mei4,
Bangbang Liu1, Tianqi Pang5, Jacky Kwok6, Ceyao Zhang7, Bang Liu8, Chenglin Wu12
1DeepWisdom, 2University of California, Berkeley,
3The Hong Kong University of Science and Technology (Guangzhou),
4University of California, San Diego, 5South China Normal University,
6Stanford University, 7The Chinese University of Hong Kong, Shenzhen,
8Université de Montréal & Mila
These authors contributed equally to this work.Bang Liu (E-mail: bang.liu@umontreal.ca) and Chenglin Wu (E-mail: alexanderwu@deepwisdom.ai) are the corresponding authors.
Abstract

Automated Machine Learning (AutoML) approaches encompass traditional methods that optimize fixed pipelines for model selection and ensembling, as well as newer LLM-based frameworks that autonomously build pipelines. While LLM-based agents have shown promise in automating machine learning tasks, they often generate low-diversity and suboptimal code, even after multiple iterations. To overcome these limitations, we introduce Tree-Search Enhanced LLM Agents (\methodname), an innovative agent-based system that leverages Monte Carlo Tree Search (MCTS) to optimize the AutoML process. By representing pipeline configurations as trees, our framework enables agents to conduct experiments intelligently and iteratively refine their strategies, facilitating a more effective exploration of the machine learning solution space. This novel approach allows \methodname to discover optimal pathways based on experimental feedback, improving the overall quality of the solutions. In an extensive evaluation across 20 machine learning datasets, we compare the performance of traditional and agent-based AutoML methods, demonstrating that \methodname achieves a win rate of 65% to 80% against each baseline across all datasets. These results underscore the significant potential of agent-based strategies in AutoML, offering a fresh perspective on tackling complex machine learning challenges1.

1Introduction

Automated Machine Learning (AutoML) is a rapidly evolving field that seeks to automate the process of designing reliable machine learning solutions with minimal human intervention. Traditional AutoML frameworks, such as Auto-WEKA (Thornton et al., 2013), Auto-Sklearn (Feurer et al., 2015; 2020), AutoGluon (Tang et al., 2024b), and H2O AutoML (LeDell & Poirier, 2020), rely on predefined search spaces and routines. These frameworks primarily focus on optimizing hyperparameters and model ensembling to find the best model configuration. However, this fixed and static approach often lacks the adaptability needed to handle diverse and dynamic data scenarios, resulting in suboptimal performance in more complex settings. Additionally, the traditional focus on model training leaves other crucial stages of the machine learning pipeline, such as data preprocessing and feature engineering, underexplored, thereby limiting the overall effectiveness of these systems.

Recently, large language model (LLM)-based agents have emerged as promising tools for automating machine learning tasks by leveraging natural language processing capabilities to generate code. These systems typically begin with a natural language prompt describing the dataset and the problem, after which an LLM generates an end-to-end solution. Early efforts, such as Zhang et al. (2024), experimented with prompting LLMs to generate machine learning solutions, while Hong et al. (2024a) introduced agents equipped with Hierarchical Graph Modeling and Programmable Node Generation to address complex and dynamic workflows. Despite these advances, LLM-based solutions often fall short in generating diverse and highly optimized workflows, as their search process remains limited to a single pass or trial. Without iterative refinement or the ability to explore alternative strategies, these solutions frequently converge on suboptimal results, even when multiple attempts are allowed.

A critical shortcoming of both traditional AutoML and LLM-based frameworks lies in their inability to mimic the nuanced problem-solving approach of human experts. When approaching a machine learning task, an expert does not simply execute a fixed pipeline or rely on a single attempt. Instead, they explore various potential configurations, systematically conduct experiments, analyze results, and iteratively refine their understanding of each component’s effectiveness. This iterative, feedback-driven process allows experts to explore diverse solutions and improve them incrementally until they arrive at the optimal configuration.

Figure 1:\methodname’s abstraction compared to other agent-based AutoML frameworks. There are two main types of agent-based approaches to AutoML problems. The first approach (Hong et al., 2024a) divides a machine learning task into multiple stages, proposing a plan for each stage, and generating and executing code step by step according to the plan, with no refinement after the solution is completed. The second (Schmidt et al., 2024) generates the entire solution in one step and iteratively refines it as a whole. \methodname integrates both approaches, enabling stage-wise planning while iteratively exploring better solutions at each stage level.

Inspired by this human-centered approach, we propose Tree-Search Enhanced LLM Agents (\methodname) for automated machine learning, a novel framework that integrates the strengths of LLM agents with a structured search and refinement process modeled on how experts solve machine learning problems. As illustrated in Figure 1, our framework combines the benefits of stage-wise planning, where each stage (e.g., Exploratory Data Analysis, Data Preprocessing, Feature Engineering, and Model Training) is handled sequentially, with an iterative refinement mechanism.

In \methodname, the search space of a machine learning problem is proposed and conceptualized as a tree, where each branch represents a potential solution path. To navigate this search space, we employ Monte Carlo Tree Search (MCTS) (Coulom, 2007) as the core decision-making engine, leveraging its ability to balance exploration (testing new strategies) and exploitation (improving known good strategies). MCTS allows the agent to efficiently explore large decision spaces, collect and process experimental results, and intelligently select the next promising configuration to test on. By iterating through this cycle of experimentation and refinement, \methodname incrementally improves its solutions, much like an expert who tests and improves its strategy based on continuous feedback.

We rigorously evaluated \methodname using 20 diverse datasets from the AutoML Benchmark (Gijsbers et al., 2024), comparing its performance against both traditional AutoML systems and agent-based AutoML approaches. The results demonstrate that \methodname consistently delivers superior performance across a wide range of machine learning tasks, validating its effectiveness and adaptability.

To summarize, our research makes the following contributions:

1. 

We introduce a feedback-driven approach for LLM agents to iteratively explore machine learning configurations, optimizing solutions over multiple experimental rounds.

2. 

Using Monte Carlo Tree Search, our system navigates a tree-structured search space, adaptively identifying high-performance pipelines through feedback.

3. 

We compare agent-based and traditional AutoML, highlighting agentic methods’ flexibility and potential for enhanced performance in machine learning.

	
Dynamic
Pipeline
	
Feature
Engineering
	
Model
Training
	
Model
Improvement
	
Pipeline
Optimization

AutoGluon (Erickson et al., 2020) 	✗	✗	Fixed models	Multi-layer stacking + bagging	✗
AutoSklearn (Feurer et al., 2020) 	✗	✗	Fixed models	Bayes Opt. + meta-learning + ensemble	✗
Data Interpreter (Hong et al., 2024a) 	✓	Instinctive	Instinctive	Instinctive	✗
AIDE (Schmidt et al., 2024) 	✓	Instinctive	Dynamic & diverse	Dynamic & diverse	One-step refinement + LLM
\methodname (Ours)	✓	Dynamic & diverse	Dynamic & diverse	Dynamic & diverse	Stepwise MCTS + LLM
Table 1:Comparison of key capabilities across various AutoML methods. Dynamic indicates the system’s ability to adjust workflows based on intermediate outcomes, allowing it to adapt as new information emerges. Diverse refers to employing multiple strategies or methods across tasks, which helps capture varied modeling needs. Instinctive means that the system directly relies on the decisions generated by an LLM and heavily depends on the model’s inclination.
2Related Works

Tree Search and Its Integration with LLMs Tree search algorithms have significantly advanced problem-solving in artificial intelligence, with Monte Carlo Tree Search (MCTS) emerging as a leading technique. These algorithms have been successfully applied across various domains, including robotics (Wu et al., 2015; Clary et al., 2018; Best et al., 2019), chemistry (Segler et al., 2018), and gaming (Silver et al., 2016; 2017), where MCTS is used to navigate vast solution spaces and solve complex problems. More recently, research has focused on integrating tree search with Large Language Models (LLMs) to enhance reasoning and decision-making. Studies such as Krishnamurthy et al. (2024) and Dwaracherla et al. (2024) explored LLMs’ capacities for efficient exploration, while Tang et al. (2024a) and Hui & Tu (2024) developed strategies for exploiting previously learned knowledge. Zhou et al. (2024) and Chi et al. (2024) applied MCTS for planning with external or self-evaluated feedback, while Feng et al. (2023); Wang et al. (2024) adapted AlphaZero-style tree search to LLM-based tasks. These advancements underscore the potential of combining tree search methods with LLMs, balancing exploration of new solutions with exploitation of prior knowledge to enhance decision-making.

Advances and Limitations in AutoML Systems Automated Machine Learning (AutoML) frameworks were introduced to reduce the need for expert knowledge in designing machine learning pipelines. Early AutoML efforts, such as (Thornton et al., 2013; Olson & Moore, 2016; Jin et al., 2019; Feurer et al., 2020; Erickson et al., 2020; LeDell & Poirier, 2020; Wang et al., 2021), focused primarily on automating key pipeline components like hyperparameter optimization, model selection, stacking, and ensembling. These frameworks achieved notable progress by integrating meta-learning and hyperparameter search strategies to automatically select and tune machine learning models. Furthermore, extensions into multi-modal data settings (Tang et al., 2024b; Jin et al., 2023) have broadened AutoML’s applicability.

Recently, there has been growing interest in leveraging LLMs within AutoML systems to enhance pipeline flexibility. Studies such as Hollmann et al. (2024); Li et al. (2024) applied LLMs to automate feature engineering, while Liu et al. (2024) introduced LLMs for hyperparameter tuning. In addition, Luo et al. (2024) proposed embedding LLMs at each stage of the machine learning workflow. Despite these advancements, traditional AutoML systems remain constrained by rigid pipelines and limited flexibility to adapt to unique datasets or specific task requirements.

LLM Agents for Dynamic Machine Learning Pipelines In contrast to static pipelines, LLM-based agents offer a more dynamic solution for addressing complex machine learning challenges. Hong et al. (2024a; b) introduced an LLM agent with hierarchical graph modeling and programmable node generation, enabling the creation of sophisticated, adaptable pipelines for diverse data scenarios. Similarly, Zhang et al. (2024) demonstrated that LLMs could effectively interpret structured inputs and apply past experiences to solve new machine learning tasks. Guo et al. (2024) expanded on this by introducing a data science agent that leverages case-based reasoning; however, it faces challenges when generating solutions from scratch due to its reliance on existing codebases. Schmidt et al. (2024) proposed an iterative approach, where the entire pipeline is generated in one step and refined iteratively through incremental modifications.

Building on these efforts, \methodname introduces an agent that integrates the strengths of both approaches—stage-wise planning and iterative refinement—allowing it to autonomously explore and generate machine learning solutions from the ground up. This approach offers greater flexibility and control during the search process, enabling the generation of optimized solutions at each stage. Table 1 highlights the functionalities provided by different AutoML systems.

3Method

As illustrated in Figure 2, \methodname consists of three key components: an LLM-based insight proposer, a search module using MCTS, and an LLM agent as the experiment executor. First, the LLM generates insights from the problem description and dataset, defining a search space. The search module then organizes this space into a tree structure and uses MCTS to explore promising paths. During each cycle, the selected path is passed to the LLM agent, which translates the configuration into an executable pipeline. The agent plans, codes, and executes the experiment, feeding the results back to refine future searches. This iterative process continues until the termination criterion is met. The following sections provide a detailed explanation of each component.

Figure 2:\methodname’s pipeline operates as follows: The system begins by inputting the problem description and dataset information into the LLM, which generates a search space of potential solutions, encompassing data preprocessing, feature engineering, and model training. The search module, powered by Monte Carlo Tree Search (MCTS), explores this space by selecting, expanding, and simulating potential configurations. The LLM agent then simulates the selected configuration by planning, coding, and executing the experiment. Feedback from the simulation is fed back into the search module, where it is used in the backpropagation step to refine future searches. This iterative process continues until a predefined stopping criterion is met, resulting in an optimized experimental pipeline.
3.1Insight Proposal and Search Space Creation

To enable \methodname to explore a wide range of machine learning strategies, we introduce an insight proposer that generates diverse methods tailored to different stages of the machine learning workflow. Each proposed insight suggests either a single technique or a combination of methods aimed at enhancing performance. For instance, a feature engineering insight might recommend creating interaction features from existing variables, while a model training insight could propose a specific algorithm or suggest running a grid search to improve accuracy.

The insight proposer takes as input the problem description 
𝑝
 and dataset information 
𝑑
, such as metadata and sample records, and generates 
𝑚
 insights 
𝜆
 for each stage of the machine learning process using a large language model 
𝑀
. These insights are stored in an insight pool, forming a search space 
Λ
 for \methodname to explore. We decompose the machine learning process into five stages: Exploratory Data Analysis (
𝜏
1
), Data Preprocessing (
𝜏
2
), Feature Engineering (
𝜏
3
), Model Training (
𝜏
4
), and Model Evaluation (
𝜏
5
). For simplicity, we denote the entire set of stages as 
𝑇
 and refer to any specific stage as 
𝜏
.

	
InsightProposer
⁢
(
𝑝
,
𝑑
,
𝑀
)
→
Λ
:=
{
𝜆
𝑖
𝜏
∣
𝜏
∈
𝑇
,
𝑖
=
1
,
…
,
𝑚
}
		
(1)
3.2Pipeline Execution and Code Generation

We employ an LLM agent, referred to as the experiment executor 
𝐸
, to conduct each trial by building practical experimental pipelines from natural language requirements. The agent takes two main steps in this process. First, given an experiment configuration 
𝑐
, which is a set of insights provided by the search module (introduced in Section 3.3.2), the experiment executor translates these insights into a detailed plan. This plan consists of a sequence of task instructions 
𝐼
𝜏
∈
𝑇
 corresponding to each stage of the machine learning process. This step is referred to as 
𝐸
plan
.

Next, following the plan, the agent writes and executes code 
𝜎
𝜏
 for each task 
𝜏
 based on the respective instruction 
𝐼
𝜏
, producing the code 
𝜎
𝜏
∈
𝑇
 for the full pipeline, along with the final execution score 
𝑠
. The complete set of code outputs 
𝜎
𝜏
∈
𝑇
 is concatenated into a full solution 
𝜎
𝑠
⁢
𝑜
⁢
𝑙
 to address the problem. This phase is referred to as 
𝐸
code & execute
.

	
𝐸
plan
⁢
(
𝑝
,
𝑑
,
𝑐
,
𝑀
)
	
→
𝐼
𝜏
∈
𝑇
		
(2)

	
𝐸
code & execute
⁢
(
𝐼
𝜏
∈
𝑇
,
𝐷
,
𝑀
)
	
→
(
𝜎
𝜏
∈
𝑇
,
𝑠
)
		
(3)
3.3Tree Search in Machine Learning Experiments

In order to systematically explore the different configurations in machine learning experiments, we model the search space as a hierarchical tree. This structure allows us to apply tree search algorithms, where each path through the tree represents a different experiment configuration. Algorithm 1 also provides an overview of this searching process.

3.3.1Experiment Node

To facilitate the exploration of various strategies, we model the proposed search space as a hierarchical tree that is well-suited for applying search algorithms. Each node in the tree, denoted as 
𝑥
, represents one insight 
𝜆
 in the search space 
Λ
 and contains the following attributes:

• 

Insight 
𝜆
⁢
(
𝑥
)
: Represents the specific insight 
𝜆
𝑖
𝜏
∈
Λ
 associated with this node, where 
𝜏
 denotes the stage of the machine learning pipeline.

• 

Depth 
𝛿
⁢
(
𝑥
)
: Indicates the stage of the machine learning process the node corresponds to (e.g., depth 1 might represent data preprocessing, depth 2 for feature engineering, and depth 3 for model training).

• 

Value 
𝑣
⁢
(
𝑥
)
: The cumulative score from simulations for this node and all its descendants.

• 

Number of Visits 
𝑛
visits
⁢
(
𝑥
)
: The total number of simulations conducted for this node and its descendants.

• 

Simulation Score 
𝑠
⁢
(
𝑥
)
: The score for simulating this node.

• 

Solution Code 
𝜎
sol
⁢
(
𝑥
)
 The final code produced after the node simulation.

• 

Stage Code 
𝜎
stage
⁢
(
𝑥
)
: The code generated up to the node’s current stage, a part of the solution code

By modeling the search space as a tree, each path from the root to a node 
𝑥
 represents an experiment configuration 
𝑐
⁢
(
𝑥
)
=
{
𝜆
⁢
(
𝑥
1
)
,
𝜆
⁢
(
𝑥
2
)
,
…
,
𝜆
⁢
(
𝑥
)
}
⊂
Λ
, where 
𝑥
1
,
𝑥
2
,
…
,
𝑥
 are nodes along the path. The task of finding the optimal solution can therefore be viewed as a path search within the tree, where each path corresponds to a potential configuration of the experiment.

3.3.2Tree Search for ML Experiments

We apply Monte Carlo Tree Search (MCTS) to systematically explore and identify optimal machine learning solutions within our framework. MCTS allows us to efficiently navigate the search space across multiple stages of the machine learning pipeline—from data preprocessing to model selection—by balancing exploration and exploitation.

Algorithm 1 \methodname using MCTS
0:  Problem description 
𝑝
, data information 
𝑑
, data 
𝐷
, LLM 
𝑀
, rollout number 
𝑘
.
1:  
Λ
←
InsightProposer
⁢
(
𝑝
,
𝑑
,
𝑀
)
2:  Initialize Tree using 
Λ
3:  for 
𝑖
 = 1 to 
𝑘
 do
4:     node 
𝑥
←
 select(Tree)
5:     
𝑋
child
←
 expand(Tree, 
𝑥
)
6:     Randomly sample a node 
𝑥
sample
 from 
𝑋
child
7:     Retreive experiment configuration 
𝑐
⁢
(
𝑥
sample
)
8:     
𝜎
𝑠
⁢
𝑜
⁢
𝑙
,
𝑠
←
simulate
⁢
(
𝑐
⁢
(
𝑥
sample
)
,
𝑝
,
𝑑
,
𝐷
,
𝑀
)
9:     attach the simulation result 
𝜎
𝑠
⁢
𝑜
⁢
𝑙
,
𝑠
 to 
𝑥
sample
 for final solution selection
10:     Backpropagate(Tree, 
𝑠
)
11:  end for
12:  
𝑥
dev best
←
argmax
𝑥
∈
Tree
⁢
(
𝑠
⁢
(
𝑥
)
)
12:  
𝜎
𝑠
⁢
𝑜
⁢
𝑙
⁢
(
𝑥
dev best
)
 
Algorithm 2 Simulate
0:  Experiment configuration 
𝑐
, problem description 
𝑝
, data information 
𝑑
, data 
𝐷
, LLM 
𝑀
.
1:  Draft plans 
𝐼
𝜏
∈
𝑇
←
𝐸
plan
⁢
(
𝑝
,
𝑑
,
𝑐
,
𝑀
)
2:  Code and execute sequentially 
𝜎
𝜏
∈
𝑇
,
𝑠
←
𝐸
code & execute
⁢
(
𝐼
𝜏
∈
𝑇
,
𝐷
,
𝑀
)
3:  
𝜎
𝑠
⁢
𝑜
⁢
𝑙
←
concatenate
⁢
(
𝜎
𝜏
∈
𝑇
)
3:  
𝜎
𝑠
⁢
𝑜
⁢
𝑙
,
𝑠

The search process involves performing multiple rollouts, which include the steps of selection, expansion, simulation, and backpropagation. We conduct 
𝑘
 rollouts to explore various paths, aiming to identify the best solution.

Selection At each iteration, we use a modified version of the UCT (Upper Confidence Bound for Trees) algorithm (Kocsis & Szepesvári, 2006), referred to as UCT-DP (depth-preferred), to select a node from the search tree. Unlike traditional MCTS, where simulations are often performed quickly due to a fixed action space and negligible action time, the context of machine learning tasks presents a different challenge. Processes such as model training introduce significant computational time, making efficient node exploration crucial. Since model selection can heavily influence the overall machine learning performance, we prioritize exploring nodes at greater depths early on.

This modification reduces the need to explore every unvisited node, allowing deeper nodes to be reached in fewer iterations—making the approach better suited for large-scale machine learning experiments. The modified selection algorithm is expressed as:

	
UCT-DP
⁢
(
𝑥
)
=
𝑣
⁢
(
𝑥
)
𝑛
⁢
(
𝑥
)
+
𝛼
explore
⁢
ln
⁡
𝑛
visits
⁢
(
𝑥
parent
)
𝑛
⁢
(
𝑥
)
		
(4)
	
𝑛
⁢
(
𝑥
)
=
{
𝛼
unvisted
	
if 
⁢
𝑛
visits
⁢
(
𝑥
)
=
0


𝑛
visits
⁢
(
𝑥
)
	
otherwise.
		
(5)

Here, 
𝛼
unvisted
 is a constant between 0 and 1 controlling the selection preference for unvisited nodes, balancing between full exploration and computational efficiency. This adjustment allows us to focus more on deeper parts of the tree that are likely to yield better solutions.

Expansion During the expansion phase, a set of child nodes 
𝑋
child
 are instantiated from the selected node 
𝑥
 for potential simulation. Note that a child node 
𝑥
child
 from the node 
𝑥
 at depth 
𝛿
 inherits the attributes of 
𝑥
 and possesses 
𝜆
⁢
(
𝑥
child
)
→
𝜆
𝜏
𝛿
+
1
, an insight of stage 
𝜏
𝛿
+
1
 from the search space.

Simulation Once expanded, a node 
𝑥
sample
 is randomly sampled from 
𝑋
child
 for simulation. The path from root to the sampled node forms a set of insights 
𝑐
⁢
(
𝑥
sample
)
=
{
𝜆
⁢
(
𝑥
1
)
,
𝜆
⁢
(
𝑥
2
)
,
…
,
𝜆
⁢
(
𝑥
sample
)
}
⊂
Λ
, representing the experiment configuration to be simulated, where 
𝑥
1
,
𝑥
2
,
.
.
,
𝑥
sample
 are the nodes along the path. The configuration 
𝑐
⁢
(
𝑥
sample
)
 is then fed to the experimenter 
𝐸
 for execution following 
𝐸
plan
 and 
𝐸
code & execute
, which produces a simulation score 
𝑠
, as illustrated in Section 3.3.1. The score serves as the feedback for back propagation. Algorithm 2 outlines the simulation process.

Backpropagation After the simulation concludes, the performance score (e.g., based on the development set) is retrieved and backpropagated through the tree. The score is propagated from the simulated node up to the root, updating each parent node’s value and visit count. This allows nodes representing more promising solutions to be prioritized in future rollouts. In addition, the solution code is also backpropagated up to the tree, and it can be processed and saved as stage code depending on the parent node during the update.

Backpropagation ensures that the algorithm learns which paths yield better results, guiding the search toward higher-performing nodes as more rollouts are conducted.

3.3.3Experiment State Saving and Loading

To boost experimentation efficiency and reduce token usage, \methodname implements fine-grained code reuse by caching code at the stage level for each attempted configuration 
𝑐
. This allows the framework to reuse as much saved code as possible when a new configuration 
𝑐
new
 shares components with existing ones. Additionally, this technique addresses the challenge of LLM non-determinism, where identical instructions can produce different code, increasing variance in final performance. Specifically, whenever a node is chosen for execution, the experimenter loads and reruns the saved stage code, if available, ensuring consistency before progressing to the next stage. This approach effectively conserves resources while maintaining robust performance across stages. In Appendix D, we examine the cost efficiency of this state-saving and loading mechanism.

4Experiments
4.1Experimental Setup
Datasets

We evaluate \methodname alongside several baselines on 20 datasets, which include 13 classification tasks and 7 regression tasks from the AutoML Benchmark (AMLB) (Gijsbers et al., 2024) and Kaggle Competitions.

Table 4 provides detailed information on the datasets used. All datasets are split into training, validation, and test sets with a 6:2:2 ratio. Each framework utilizes the training and validation sets to train models and makes predictions on the test set labels.

Evaluation Metrics

For the AMLB datasets, we use the default target column provided by OpenML. For Kaggle competition datasets, we rely on the target column specified in the competition description. Performance is measured using root mean squared error (RMSE) for regression tasks, F1 score for binary classification, and F1-weighted score for multi-class classification. To ensure comparability across datasets with varying metrics, we introduce a Normalized Score (NS), which maps RMSE into the range from 0 to 1.

	
NS
⁢
(
𝑠
raw
)
=
{
1
1
+
log
⁡
(
1
+
𝑠
raw
)
	
if the metric is RMSE.


𝑠
raw
	
otherwise.
		
(6)

Here, 
𝑠
𝑟
⁢
𝑎
⁢
𝑤
 represents the raw score before normalization. To evaluate \methodname against other frameworks, we employ three key metrics: average Normalized Score (NS), average rank, and average best rank. The average rank is calculated by considering all rankings of a method across datasets, while the average best rank focuses on the method’s best performance in each dataset. We also want to quantify how other baselines perform relative to \methodname. The “Rescaled NS” is defined as:

	
Rescaled NS
⁢
(
𝑓
)
=
NS
𝑓
NS
\methodname
		
(7)

where 
𝑓
 represents the baseline method being compared to \methodname.

Method and Baselines Setup

We compare \methodname with several baseline methods, including Data Interpreter (Hong et al., 2024a), AIDE (Schmidt et al., 2024), AutoGluon (Erickson et al., 2020), and AutoSklearn (Feurer et al., 2015; 2020).

For our LLM-based approaches (\methodname, Data Interpreter, and AIDE), we employ a consistent initial task prompt across all methods. This prompt encompasses the dataset name, target column, and evaluation metric. We choose DeepSeek v2.5 (DeepSeek-AI, 2024) as our foundation LLM due to its open-source nature, strong coding capabilities, and cost-effective token usage. To encourage output diversity, we set the temperature parameter to 0.5 for all LLM-based methods. AIDE conducts 10 iterations per execution, while \methodname performs 10 rollouts.

For \methodname, we employ Data Interpreter as the experimenter, leveraging its multi-step generation capability. We configured the hyperparameters of UCT-DP as follows: 
𝛼
unvisited
 is set to 0.8 and 
𝛼
explore
 is set to 1.4. These settings aim to balance exploration and exploitation in the method’s search strategy.

Each method, except for AutoGluon, is run three times for each dataset. AutoGluon, being deterministic, is run only once with its default settings. AutoSklearn is also run with default settings, limited to 600 seconds per task.

Method	Wins	Losses	Top 1	Avg. NS % 
↑
	Avg. Best NS % 
↑
	Avg. Rank 
↓
	Avg. Best Rank 
↓

AutoGluon	7	13	4	53.2	53.2	4.4	4.4
AutoSklearn	5	15	5	46.1	47.5	7.6	6.1
AIDE	5	15	2	47.1	51.8	7.8	5.3
Data Interpreter	4	16	2	47.4	50.2	8.8	6.4
\methodname	-	-	7	53.3	54.7	4.8	2.7
Table 2:Results of each AutoML framework on 20 tabular datasets. The “Wins” column indicates the number of datasets where the method outperforms \methodname, while “Losses” shows the number of datasets where the method underperforms. The “Top 1” column represents the number of datasets where the method produces the best predictions across methods.
4.2Results
Figure 3:Rescaled NS of AutoML frameworks relative to \methodname on tabular datasets. Points to the left of the vertical line indicate poorer predictions compared to \methodname. Notably, \methodname often occupies a leading position across the datasets.

As shown in Table 2, \methodname achieves the highest average Normalized Score (NS) and average best rank among all frameworks. Notably, \methodname excels in producing the highest number of top predictions, as indicated in the “Top 1” column across all datasets. Furthermore, the “Losses” column reveals that each competing method falls short against \methodname, losing in 65-80% of the datasets.

Interestingly, AutoGluon exhibits a marginally higher average rank than \methodname. This slight discrepancy may be attributed to the inherent randomness in LLMs and model training processes, which can influence the exploration of machine learning solutions. However, \methodname’s higher average NS suggests that it performs strongly in the datasets where it excels, while its losses in other datasets are relatively minor. This means that even when \methodname produces lower-ranked solutions, the performance gap is small, allowing it to fully compensate in the datasets where it performs well.

The two other agent-based methods exhibit relatively lower performance. The first method, Data Interpreter, struggles to enhance its score with multiple attempts due to its inability to refine its solution after completing a machine learning task. The second method, AIDE, does not have a stage-specific planning module, limiting its capacity to improve results after a series of greedy exploitation, which makes it prone to falling into local optima. These limitations likely account for their weaker performance.

Figure 3 further corroborates \methodname’s effectiveness, revealing that its best solutions frequently occupy leading positions across various datasets. This visual representation exhibits the method’s consistent high performance and adaptability across different ML datasets. We also include a detailed results of each method in Appendix C.

4.3Ablation Study

For the rest of the study, we employ a subset of datasets to evaluate \methodname under various settings. Our selection process involves choosing the first two datasets alphabetically for each machine learning task. Specifically, we use boston, colleges, credit-g, Click_prediction_small, GesturePhaseSegmentationProcessed, and mfeat-factors to conduct the ablation study.

	Data Interpreter	\methodname (Random Search)	\methodname (MCTS)
Avg. NS 
↑
 	56.4	58.6	60.9
Avg. Best NS 
↑
 	59.0	61.4	62.4
Avg. Rank 
↓
 	6.9	4.8	3.3
Avg. Best Rank 
↓
 	4.8	2.8	1.5
Table 3:Performance results for each search setting on the chosen datasets. \methodname with MCTS consistently surpasses \methodname with Random Search.
Effectiveness of Search

To evaluate the effectiveness of Monte Carlo Tree Search (MCTS) in improving the solution search process, we conducted an ablation study. In this study, we compared the performance of our method using MCTS against a variant that randomly samples insights from each stage’s insight pool. As shown in Table 3, the MCTS version achieves a higher average normalized score across datasets and a better overall ranking compared to the random sampling approach. Moreover, even the random sampling variant of our method outperforms Data Interpreter, the base experimenter. This suggests the presence of an appropriate search space and an experiment agenda is vital for improving a machine learning agent. Our insight proposer generates relevant and useful insights, facilitating such improvement, regardless of the selection method.

Number of Rollouts

Figure 5 illustrates that the average performance of \methodname improves as the number of permitted rollouts increases. The trend demonstrates the strong scalability of \methodname, as it efficiently leverages additional opportunities to explore the search space, improving the normalized score by 4.7% after 10 rollouts and 6.4% after 20, compared to the initial rollout.

Figure 4:The average performance of \methodname on six selected datasets with an increasing number of rollouts.
Figure 5:Comparison of Normalized Scores between different base LLMs on six selected datasets.
LLM Adaptability

To evaluate the robustness of our framework, we conduct experiments using different Large Language Models (LLMs). Specifically, we compare the performance of \methodname with Claude-3.5-Sonnet (Anthropic, 2024) and GPT-4o (OpenAI, 2024) against DeepSeek V2.5 which we primarily use for evaluation. This comparison enables us to assess how the choice of LLM affects the overall effectiveness of our approach.

As Figure 5 shown, \methodname delivers similar results across different LLMs, indicating its flexibility with various models depending on user preference and availability. We also report the numeric results in Appendix C.2.

5Conclusion

In this paper, we introduced \methodname, a novel framework that integrates LLM-based agents with Monte Carlo Tree Search (MCTS) to automate machine learning workflows. Our experimental results, conducted on 20 machine learning datasets, demonstrate \methodname’s effectiveness and highlight its distinct advantages over both traditional AutoML frameworks and existing LLM-based approaches. The proposed methodology is not limited to machine learning but could be adapted to a wide range of sequential decision-making problems, provided they can be represented as tree structures with scalar rewards derived from their leaf nodes. Looking ahead, future work could explore extending this framework to other domains, including software engineering, scientific discovery, game playing, and robotics. Furthermore, improving the efficiency and scalability of the tree search process for larger solution spaces remains an important area for investigation. Another promising direction is developing techniques to provide interpretable explanations of the search process and solution rationale, enhancing the transparency and trustworthiness of the system. \methodname represents a significant advancement in automated machine learning, demonstrating the potential of combining traditional search algorithms with the flexibility of LLMs.

References
Anthropic (2024)	Anthropic.Introducing Claude 3.5 Sonnet — anthropic.com.https://www.anthropic.com/news/claude-3-5-sonnet, 2024.
Best et al. (2019)	Graeme Best, Oliver M Cliff, Timothy Patten, Ramgopal R Mettu, and Robert Fitch.Dec-mcts: Decentralized planning for multi-robot active perception.The International Journal of Robotics Research, 38(2-3):316–337, 2019.doi: 10.1177/0278364918755924.
Chi et al. (2024)	Yizhou Chi, Kevin Yang, and Dan Klein.Thoughtsculpt: Reasoning with intermediate revision and search, 2024.
Clary et al. (2018)	Patrick Clary, Pedro Morais, Alan Fern, and Jonathan Hurst.Monte-carlo planning for agile legged locomotion.Proceedings of the International Conference on Automated Planning and Scheduling, 28(1):446–450, Jun. 2018.doi: 10.1609/icaps.v28i1.13933.
Coulom (2007)	Rémi Coulom.Efficient selectivity and backup operators in monte-carlo tree search.In H. Jaap van den Herik, Paolo Ciancarini, and H. H. L. M. (Jeroen) Donkers (eds.), Computers and Games, pp.  72–83, Berlin, Heidelberg, 2007. Springer Berlin Heidelberg.ISBN 978-3-540-75538-8.
DeepSeek-AI (2024)	DeepSeek-AI.Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model, 2024.
Dwaracherla et al. (2024)	Vikranth Dwaracherla, Seyed Mohammad Asghari, Botao Hao, and Benjamin Van Roy.Efficient exploration for llms, 2024.
Erickson et al. (2020)	Nick Erickson, Jonas Mueller, Alexander Shirkov, Hang Zhang, Pedro Larroy, Mu Li, and Alexander Smola.Autogluon-tabular: Robust and accurate automl for structured data, 2020.
Feng et al. (2023)	Xidong Feng, Ziyu Wan, Muning Wen, Ying Wen, Weinan Zhang, and Jun Wang.Alphazero-like tree-search can guide large language model decoding and training, 2023.
Feurer et al. (2015)	Matthias Feurer, Aaron Klein, Katharina Eggensperger, Jost Springenberg, Manuel Blum, and Frank Hutter.Efficient and robust automated machine learning.In Advances in Neural Information Processing Systems 28 (2015), pp.  2962–2970, 2015.
Feurer et al. (2020)	Matthias Feurer, Katharina Eggensperger, Stefan Falkner, Marius Lindauer, and Frank Hutter.Auto-sklearn 2.0: Hands-free automl via meta-learning, 2020.
Gijsbers et al. (2024)	Pieter Gijsbers, Marcos L. P. Bueno, Stefan Coors, Erin LeDell, Sébastien Poirier, Janek Thomas, Bernd Bischl, and Joaquin Vanschoren.Amlb: an automl benchmark.Journal of Machine Learning Research, 25(101):1–65, 2024.
Guo et al. (2024)	Siyuan Guo, Cheng Deng, Ying Wen, Hechang Chen, Yi Chang, and Jun Wang.Ds-agent: Automated data science by empowering large language models with case-based reasoning, 2024.
Hollmann et al. (2024)	Noah Hollmann, Samuel Müller, and Frank Hutter.Large language models for automated data science: Introducing caafe for context-aware automated feature engineering, 2024.
Hong et al. (2024a)	Sirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu, Binhao Wu, Danyang Li, Jiaqi Chen, Jiayi Zhang, Jinlin Wang, Li Zhang, Lingyao Zhang, Min Yang, Mingchen Zhuge, Taicheng Guo, Tuo Zhou, Wei Tao, Wenyi Wang, Xiangru Tang, Xiangtao Lu, Xiawu Zheng, Xinbing Liang, Yaying Fei, Yuheng Cheng, Zongze Xu, and Chenglin Wu.Data interpreter: An llm agent for data science, 2024a.
Hong et al. (2024b)	Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber.MetaGPT: Meta programming for a multi-agent collaborative framework.In The Twelfth International Conference on Learning Representations, 2024b.
Hui & Tu (2024)	Wenyang Hui and Kewei Tu.Rot: Enhancing large language models with reflection on search trees, 2024.
Jin et al. (2019)	Haifeng Jin, Qingquan Song, and Xia Hu.Auto-keras: An efficient neural architecture search system.In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining, pp.  1946–1956, 2019.
Jin et al. (2023)	Haifeng Jin, François Chollet, Qingquan Song, and Xia Hu.Autokeras: An automl library for deep learning.Journal of machine Learning research, 24(6):1–6, 2023.
Kocsis & Szepesvári (2006)	Levente Kocsis and Csaba Szepesvári.Bandit based monte-carlo planning.In Johannes Fürnkranz, Tobias Scheffer, and Myra Spiliopoulou (eds.), Machine Learning: ECML 2006, pp.  282–293, Berlin, Heidelberg, 2006. Springer Berlin Heidelberg.ISBN 978-3-540-46056-5.
Krishnamurthy et al. (2024)	Akshay Krishnamurthy, Keegan Harris, Dylan J. Foster, Cyril Zhang, and Aleksandrs Slivkins.Can large language models explore in-context?, 2024.
LeDell & Poirier (2020)	Erin LeDell and Sebastien Poirier.H2O AutoML: Scalable automatic machine learning.7th ICML Workshop on Automated Machine Learning (AutoML), July 2020.
Li et al. (2024)	Dawei Li, Zhen Tan, and Huan Liu.Exploring large language models for feature selection: A data-centric perspective, 2024.
Liu et al. (2024)	Siyi Liu, Chen Gao, and Yong Li.Large language model agent for hyper-parameter optimization.arXiv preprint arXiv:2402.01881, 2024.
Luo et al. (2024)	Daqin Luo, Chengjian Feng, Yuxuan Nong, and Yiqing Shen.Autom3l: An automated multimodal machine learning framework with large language models.arXiv preprint arXiv:2408.00665, 2024.
Olson & Moore (2016)	Randal S Olson and Jason H Moore.Tpot: A tree-based pipeline optimization tool for automating machine learning.In Workshop on automatic machine learning, pp.  66–74. PMLR, 2016.
OpenAI (2024)	OpenAI.Hello GPT-4o.https://openai.com/index/hello-gpt-4o/, 2024.
Schmidt et al. (2024)	Dominik Schmidt, Yuxiang Wu, and Zhengyao Jiang.Aide: Human-level performance in data science competitions, 2024.URL https://www.weco.ai/blog/technical-report.
Segler et al. (2018)	Marwin Segler, Mike Preuss, and Mark Waller.Planning chemical syntheses with deep neural networks and symbolic ai.Nature, 555:604–610, 03 2018.doi: 10.1038/nature25978.
Silver et al. (2016)	David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, L. Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Vedavyas Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy P. Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, and Demis Hassabis.Mastering the game of go with deep neural networks and tree search.Nature, 2016.
Silver et al. (2017)	David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy P. Lillicrap, Fan Hui, L. Sifre, George van den Driessche, Thore Graepel, and Demis Hassabis.Mastering the game of go without human knowledge.Nature, 2017.
Tang et al. (2024a)	Hao Tang, Keya Hu, Jin Peng Zhou, Sicheng Zhong, Wei-Long Zheng, Xujie Si, and Kevin Ellis.Code repair with llms gives an exploration-exploitation tradeoff, 2024a.
Tang et al. (2024b)	Zhiqiang Tang, Haoyang Fang, Su Zhou, Taojiannan Yang, Zihan Zhong, Tony Hu, Katrin Kirchhoff, and George Karypis.Autogluon-multimodal (automm): Supercharging multimodal automl with foundation models.arXiv preprint arXiv:2404.16233, 2024b.
Thornton et al. (2013)	Chris Thornton, Frank Hutter, Holger H Hoos, and Kevin Leyton-Brown.Auto-weka: Combined selection and hyperparameter optimization of classification algorithms.In Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining, pp.  847–855, 2013.
Wang et al. (2024)	Ante Wang, Linfeng Song, Ye Tian, Baolin Peng, Dian Yu, Haitao Mi, Jinsong Su, and Dong Yu.Litesearch: Efficacious tree search for llm, 2024.
Wang et al. (2021)	Chi Wang, Qingyun Wu, Markus Weimer, and Erkang Zhu.Flaml: A fast and lightweight automl library.In MLSys, 2021.
Wu et al. (2015)	Feng Wu, Sarvapali D. Ramchurn, Wenchao Jiang, Jeol E. Fischer, Tom Rodden, and Nicholas R. Jennings.Agile planning for real-world disaster response.In Proceedings of the 24th International Conference on Artificial Intelligence, IJCAI’15, pp.  132–138. AAAI Press, 2015.ISBN 9781577357384.
Zhang et al. (2024)	Lei Zhang, Yuge Zhang, Kan Ren, Dongsheng Li, and Yuqing Yang.Mlcopilot: Unleashing the power of large language models in solving machine learning tasks, 2024.
Zhou et al. (2024)	Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang.Language agent tree search unifies reasoning acting and planning in language models, 2024.
Appendix ADatasets

Table 4 outlines the detailed information of the datasets used for evaluation.

Dataset name
 	
# Features
	# Rows	# Classes	Task Type	Metric	Source

boston
 	
14
	506	N/A	Regression	RMSE	OpenML (Dataset ID: 531)

colleges
 	
48
	7063	N/A	Regression	RMSE	OpenML (Dataset ID: 42727)

concrete-strength
 	
9
	4866	N/A	Regression	RMSE	Kaggle (playground-series-s3e9)

diamonds
 	
10
	53940	N/A	Regression	RMSE	OpenML (Dataset ID: 42225)

house-prices
 	
81
	1460	N/A	Regression	RMSE	Kaggle (house-prices-advanced-regression-techniques)

Moneyball
 	
15
	1232	N/A	Regression	RMSE	OpenML (Dataset ID: 41021)

SAT11-HAND-runtime-regression
 	
118
	4440	N/A	Regression	RMSE	OpenML (Dataset ID: 41980)

credit-g
 	
21
	1000	2	Classification	F1	OpenML (Dataset ID: 31)

Click_prediction_small
 	
12
	39948	2	Classification	F1	OpenML (Dataset ID: 42733)

icr
 	
58
	617	2	Classification	F1	Kaggle (icr-identify-age-related-conditions)

jasmine
 	
145
	2984	2	Classification	F1	OpenML (Dataset ID: 41143)

kc1
 	
21
	2109	2	Classification	F1	OpenML (Dataset ID: 1067)

kick
 	
33
	72983	2	Classification	F1	OpenML (Dataset ID: 41162)

smoker-status
 	
23
	143330	2	Classification	F1	Kaggle (playground-series-s3e24)

software-defects
 	
22
	91586	2	Classification	F1	Kaggle (playground-series-s3e23)

titanic
 	
12
	891	2	Classification	F1	Kaggle (titanic)

GesturePhaseSegmentationProcessed
 	
33
	9873	5	Multiclass	F1-weighted	OpenML (Dataset ID: 4538)

mfeat-factors
 	
217
	2000	10	Multiclass	F1-weighted	OpenML (Dataset ID: 12)

segment
 	
20
	2310	7	Multiclass	F1-weighted	OpenML (Dataset ID: 40984)

wine-quality-white
 	
12
	4898	7	Multiclass	F1-weighted	OpenML (Dataset ID: 40498)
Table 4:Summary of the machine learning datasets used in the experiments. OpenML datasets can be accessed using their respective dataset IDs. The Kaggle datasets are available at https://www.kaggle.com/competitions/{source}.
Appendix BPrompts
B.1Task Prompt

All LLM-based methods start by receiving the same base requirement prompt at the beginning of the task. The prompt specifies the dataset’s name, the target label column, the evaluation metric to be used, and the dataset’s file path. Furthermore, the prompt include a path to a text file containing the dataset’s metadata.

1TASK_PROMPT = """
2#␣User␣requirement
3This␣is␣a␣{datasetname}␣dataset.
4Your␣goal␣is␣to␣predict␣the␣target␣column␣‘{target_col}‘.
5Perform␣data␣analysis,␣data␣preprocessing,␣feature␣engineering,␣and␣modeling␣to␣predict␣the␣target.␣Report␣{metric}␣on␣the␣eval␣data.␣Do␣not␣plot␣or␣make␣any␣visualizations.
6
7#␣Data␣dir
8train␣set␣(with␣labels):␣{train_path}
9dev␣set␣(with␣labels):␣{dev_path}
10test␣set␣(without␣labels):␣{test_path}
11dataset␣description:␣{data_info_path}
12(During␣EDA,␣you␣can␣use␣this␣file
13to␣get␣additional␣information␣about␣the␣dataset)
14"""

Since AIDE automatically splits the training data into a new train set and a validation set, we combine the original train and validation sets and provide them as input to AIDE. We set k_fold_validation to 1 in its configuration file to enforce a single train-val split for closer alignment with our setup. In both setups, the frameworks have access to the labels for both the train and validation sets.

B.2Instruction Prompt

The instruction prompt would direct the framework to save the final prediction file for evaluation.

1DI_INSTRUCTION = """
2##␣Attention
31.␣Please␣do␣not␣leak␣the␣target␣label␣in␣any␣form␣during␣training.
42.␣Test␣set␣does␣not␣have␣the␣target␣column.
53.␣When␣conducting␣data␣exploration␣or␣analysis,␣print␣out␣the␣results␣of␣your␣findings.
64.␣You␣should␣perform␣transformations␣on␣train,␣dev,␣and␣test␣sets␣at␣the␣same␣time␣(it’s␣a␣good␣idea␣to␣define␣functions␣for␣this␣and␣avoid␣code␣repetition).
75.␣When␣scaling␣or␣transforming␣features,␣make␣sure␣the␣target␣column␣is␣not␣included.
86.␣You␣could␣utilize␣dev␣set␣to␣validate␣and␣improve␣model␣training.␣{special_instruction}
9
10##␣Saving␣Dev␣and␣Test␣Predictions
111.␣Save␣the␣prediction␣results␣of␣BOTH␣the␣dev␣set␣and␣test␣set␣in␣‘dev_predictions.csv‘␣and␣‘test_predictions.csv‘␣respectively␣in␣the␣output␣directory.
12-␣Both␣files␣should␣contain␣a␣single␣column␣named␣‘target‘␣with␣the␣predicted␣values.
132.␣Make␣sure␣the␣prediction␣results␣are␣in␣the␣same␣format␣as␣the␣target␣column␣in␣the␣training␣set.
14-␣For␣instance,␣if␣the␣target␣column␣is␣categorical,␣the␣prediction␣results␣should␣be␣categorical␣as␣well.
15
16##␣Output␣Performance
17Print␣the␣train␣and␣dev␣set␣performance␣in␣the␣last␣step.
18
19#␣Output␣dir
20{output_dir}
21"""
B.3Insight Proposal Prompt

Insight Proposer uses this prompt to generate a search space of insights for different stages of the machine learning task.

1DATASET_INSIGHT_PROMPT = """
2#␣Dataset␣Description
3{dataset}
4
5#␣Dataset␣Metadata
6{metadata}
7
8#␣Dataset␣Head
9{head}
10
11#␣Instruction
12Propose␣insights␣to␣help␣improve␣the␣performance␣of␣the␣model␣on␣this␣dataset.
13The␣insights␣should␣be␣proposed␣based␣on␣the␣dataset␣description␣with␣different␣task␣types.
14Each␣task␣type␣should␣have␣at␣least␣5␣insights.
15Make␣sure␣each␣method␣is␣diverse␣enough␣and␣can␣be␣implemented␣separately.
16Be␣specific␣about␣models’␣choices,␣ensemble␣and␣tuning␣techniques,␣and␣preprocessing␣&␣feature␣engineering␣techniques.
17
18#␣Format
19‘‘‘json
20[
21␣␣␣␣{{
22␣␣␣␣␣␣␣␣"task_type":␣"EDA",
23␣␣␣␣␣␣␣␣"insights":␣[
24␣␣␣␣␣␣␣␣␣␣␣␣"insight1",
25␣␣␣␣␣␣␣␣␣␣␣␣"insight2",
26␣␣␣␣␣␣␣␣␣␣␣␣"insight3",
27␣␣␣␣␣␣␣␣␣␣␣␣...
28␣␣␣␣␣␣␣␣␣␣␣␣"insightN"
29␣␣␣␣␣␣␣␣]
30␣␣␣␣}},
31␣␣␣␣{{
32␣␣␣␣␣␣␣␣"task_type":␣"Data Preprocessing",
33␣␣␣␣␣␣␣␣"insights":␣[
34␣␣␣␣␣␣␣␣␣␣␣␣"insight1",
35␣␣␣␣␣␣␣␣␣␣␣␣"insight2",
36␣␣␣␣␣␣␣␣␣␣␣␣"insight3",
37␣␣␣␣␣␣␣␣␣␣␣␣...
38␣␣␣␣␣␣␣␣␣␣␣␣"insightN"
39␣␣␣␣␣␣␣␣]
40␣␣␣␣}},
41␣␣␣␣{{
42␣␣␣␣␣␣␣␣"task_type":␣"Feature Engineering",
43␣␣␣␣␣␣␣␣"insights":␣[
44␣␣␣␣␣␣␣␣␣␣␣␣"insight1",
45␣␣␣␣␣␣␣␣␣␣␣␣"insight2",
46␣␣␣␣␣␣␣␣␣␣␣␣"insight3",
47␣␣␣␣␣␣␣␣␣␣␣␣...
48␣␣␣␣␣␣␣␣␣␣␣␣"insightN"
49␣␣␣␣␣␣␣␣]
50␣␣␣␣}},
51␣␣␣␣{{
52␣␣␣␣␣␣␣␣"task_type":␣"Model Training",
53␣␣␣␣␣␣␣␣"insights":␣[
54␣␣␣␣␣␣␣␣␣␣␣␣"insight1",
55␣␣␣␣␣␣␣␣␣␣␣␣"insight2",
56␣␣␣␣␣␣␣␣␣␣␣␣"insight3",
57␣␣␣␣␣␣␣␣␣␣␣␣...
58␣␣␣␣␣␣␣␣␣␣␣␣"insightN"
59␣␣␣␣␣␣␣␣]
60␣␣␣␣}}
61]
62‘‘‘
63"""
Appendix CResults
C.1Main Results
	AutoGluon	AutoSklearn	AIDE	DI	\methodname
Dataset	Avg.	Best	Avg.	Best	Avg.	Best	Avg.	Best	Avg.	Best
Click_prediction_small	7	7	2	1	7.3	4	11	10	7.7	6
GesturePhaseSegmentationProcessed	1	1	6.3	3	7.3	4	11	10	5.3	2
Moneyball	4	4	10	9	4	1	9	2	6	3
SAT11-HAND-runtime-regression	1	1	12	11	5.3	3	9	8	3.7	2
boston	5	5	12	11	3.7	2	9	8	4	1
colleges	1	1	12	11	6	2	8	7	4	3
concrete-strength	5	5	12	11	6.3	4	2	1	8.3	6
credit-g	4	4	10	9	10	5	5.3	1	3.7	2
diamonds	2	2	12	11	6	4	8.7	7	3	1
house-prices	1	1	12	11	6.7	5	7.3	3	4	2
icr	5	5	5.3	3	12	11	9	8	2.3	1
jasmine	7	7	6	4	8.7	5	11.3	9	2	1
kc1	10	10	2.7	1	8	5	11.3	9	5	2
kick	4	4	2	1	9.3	6	11	10	6.7	5
mfeat-factors	4	4	2	1	10	9	10.3	6	6.7	5
segment	3	3	6.3	5	11	10	9.7	7	2.3	1
smoker-status	7	7	4.7	3	11.3	9	7.7	2	4.3	1
software-defects	8	8	2	1	12	11	6	4	7.7	6
titanic	7	7	9.7	6	2.7	1	10.3	8	5.3	3
wine-quality-white	2	2	10	8	7.3	4	9	7	3.3	1
Overall Rank 
↓
 	4.4	4.4	7.6	6.1	7.8	5.3	8.8	6.4	4.8	2.7
Table 5:Methods’ ranking for each tabular dataset
	AutoGluon	AutoSklearn	AIDE	DI	\methodname
Dataset	Avg.	Best	Avg.	Best	Avg.	Best	Avg.	Best	Avg.	Best
Click_prediction_small	26.6	26.6	40.2	40.3	26.1	39.4	12.9	13.9	23.2	27.4
GesturePhaseSegmentationProcessed	69.3	69.3	67.2	68.4	56.3	68.1	60.1	64.4	67.9	69.2
Moneyball	24.3	24.3	13.1	13.8	23.8	24.6	9.5	24.5	21.9	24.5
SAT11-HAND-runtime-regression	12.6	12.6	10.3	10.3	12.0	12.1	11.4	11.9	12.2	12.5
boston	39.8	39.8	19.5	19.6	40.5	41.3	37.0	38.6	40.1	41.4
colleges	88.3	88.3	2.1	2.1	86.0	87.8	87.5	87.7	87.8	87.8
concrete-strength	28.3	28.3	17.4	17.9	28.3	28.3	28.8	29.6	28.2	28.2
credit-g	50.5	50.5	35.1	44.0	21.6	48.4	48.1	53.2	50.9	52.7
diamonds	13.8	13.8	8.7	8.7	13.7	13.7	13.5	13.6	13.7	13.8
house-prices	9.0	9.0	2.0	2.0	8.9	8.9	8.5	9.0	8.9	9.0
icr	76.2	76.2	70.4	79.2	31.7	35.9	57.8	60.6	78.7	79.2
jasmine	84.3	84.3	84.4	84.7	83.6	84.6	77.8	83.5	85.4	86.2
kc1	38.3	38.3	43.5	45.0	40.8	42.6	38.1	41.2	42.2	43.1
kick	39.6	39.6	41.8	42.1	14.9	38.6	2.8	4.2	35.9	38.7
mfeat-factors	96.7	96.7	97.1	97.5	94.4	94.5	93.0	96.0	95.7	96.2
segment	93.5	93.5	92.7	93.1	91.7	92.2	91.7	92.6	93.8	94.4
smoker-status	78.0	78.0	78.6	78.9	74.8	76.3	77.3	81.5	82.4	91.5
software-defects	51.5	51.5	61.1	61.7	49.7	49.8	54.5	57.3	52.2	53.3
titanic	78.9	78.9	76.2	78.9	81.2	83.7	76.0	78.5	78.8	79.7
wine-quality-white	65.4	65.4	60.7	61.4	62.9	65.1	61.2	61.6	65.3	66.0
Overall NS % 
↑
 	53.2	53.2	46.1	47.5	45.5	51.8	47.4	50.2	53.3	54.7
Table 6:Methods’ NS % for each tabular dataset
C.2Performance using different LLMs
	GPT-4o	Claude 3.5 Sonnet	DeepSeek V2.5
Avg. NS 
↑
 	62.3	57.9	60.9
Avg. Best NS 
↑
 	65.5	59.2	62.4
Avg. Rank 
↓
 	3.7	6.3	5.0
Avg. Best Rank 
↓
 	1.5	4.8	3.2
Table 7:Results of \methodname with different base LLMs on the selected tabular datasets.
Appendix DCost-effectiveness Analysis

We conduct multiple trials of execution of each method to estimate the average running cost for the LLM-based baselines. As shown in Table 8, all methods incur relatively low costs to complete a single machine learning task. Among these, AIDE exhibits the lowest execution cost, due to the lack of stage-wise planning, resulting in fewer token generations compared to the other approaches. Additionally, \methodname, which employs Data Interpreter as its base experimenter, is less costly than Data Interpreter itself. This efficiency is largely due to \methodname’s state-saving and loading mechanism, which reduces the generation of repeated tasks and code.

	Cost per ML task ($)		
Data Interpreter (
𝑘
=10)	0.07		
AIDE (
𝑘
=10)	0.01		
\methodname (
𝑘
=10)	0.05		
Table 8:Estimated costs of agent-based frameworks utilizing DeepSeekV2.5 on a single machine learning dataset over 
𝑘
 iterations/rollouts.
Appendix ECase Study
E.1Overview of SELA’s search process
1Number of simulations: 10
2[Node 0]
3Plans:
41. Perform exploratory data analysis on the train and dev datasets
52. Preprocess the train, dev, and test datasets
63. Perform feature engineering on the train, dev, and test datasets
74. Train multiple models and evaluate their performance
85. Train a weighted ensemble model using the best performing models
96. Evaluate the ensemble model on the dev set and save predictions
107. Generate predictions for the test set and save them
11Simulated: True
12Score: avg score: 0.6150206840685731, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6855841857240594, ’test_score’: 0.6814818772150697, ’score’: 0.6855841857240594}, Visits: 10
13
14 [Node 0-0]
15 Plans:
16 3. Perform feature engineering on the train, dev, and test datasets by creating new features that calculate the magnitude of the vectorial velocities and accelerations to capture the overall movement intensity.
17 Simulated: True
18 Score: avg score: 0.6507249985568175, simulated score: {’train_score’: 0.982920964830782, ’dev_score’: 0.6420233166755841, ’test_score’: 0.647550336228104, ’score’: 0.6420233166755841}, Visits: 2
19
20 [Node 0-0-0]
21 Plans:
22 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships, and evaluate its performance
23 Simulated: False
24 Score: avg score: 0, simulated score: {}, Visits: 0
25
26 [Node 0-0-1]
27 Plans:
28 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance.
29 Simulated: False
30 Score: avg score: 0, simulated score: {}, Visits: 0
31
32 [Node 0-0-2]
33 Plans:
34 4. Implement a Neural Network with multiple layers to capture the hierarchical patterns in the data and evaluate its performance
35 Simulated: True
36 Score: avg score: 0.6594266804380511, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6594266804380511, ’test_score’: 0.6702614538699305, ’score’: 0.6594266804380511}, Visits: 1
37
38 [Node 0-0-3]
39 Plans:
40 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance
41 Simulated: False
42 Score: avg score: 0, simulated score: {}, Visits: 0
43
44 [Node 0-0-4]
45 Plans:
46 4. Train multiple models, perform hyperparameter tuning using Grid Search or Random Search, and evaluate their performance
47 Simulated: False
48 Score: avg score: 0, simulated score: {}, Visits: 0
49
50 [Node 0-1]
51 Plans:
52 3. Perform feature engineering on the train, dev, and test datasets by generating time-based features, such as the difference between consecutive frames, to capture the rate of change in movements.
53 Simulated: True
54 Score: avg score: 0.6464940718972336, simulated score: {’train_score’: 1.0, ’dev_score’: 0.5985614604756948, ’test_score’: 0.5857379626419719, ’score’: 0.5985614604756948}, Visits: 2
55
56 [Node 0-1-0]
57 Plans:
58 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships
59 Simulated: False
60 Score: avg score: 0, simulated score: {}, Visits: 0
61
62 [Node 0-1-1]
63 Plans:
64 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance to model the complex decision boundaries between different gesture phases.
65 Simulated: True
66 Score: avg score: 0.6944266833187726, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6944266833187726, ’test_score’: 0.6928451194338062, ’score’: 0.6944266833187726}, Visits: 1
67
68 [Node 0-1-2]
69 Plans:
70 4. Implement a Neural Network with multiple layers to capture the hierarchical patterns in the data and evaluate its performance
71 Simulated: False
72 Score: avg score: 0, simulated score: {}, Visits: 0
73
74 [Node 0-1-3]
75 Plans:
76 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance
77 Simulated: False
78 Score: avg score: 0, simulated score: {}, Visits: 0
79
80 [Node 0-1-4]
81 Plans:
82 4. Train multiple models and perform hyperparameter tuning using techniques like Grid Search or Random Search to optimize and evaluate their performance.
83 Simulated: False
84 Score: avg score: 0, simulated score: {}, Visits: 0
85
86 [Node 0-2]
87 Plans:
88 3. Perform feature engineering on the train, dev, and test datasets by creating features that represent the spatial relationships between different body parts, such as the distance between the hands and the head.
89 Simulated: True
90 Score: avg score: 0.6296836159165489, simulated score: {’train_score’: 0.7619969104124632, ’dev_score’: 0.5997286931710517, ’test_score’: 0.604077566134264, ’score’: 0.5997286931710517}, Visits: 3
91
92 [Node 0-2-0]
93 Plans:
94 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships, and evaluate its performance
95 Simulated: False
96 Score: avg score: 0, simulated score: {}, Visits: 0
97
98 [Node 0-2-1]
99 Plans:
100 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance to model the complex decision boundaries between different gesture phases.
101 Simulated: True
102 Score: avg score: 0.6446610772892973, simulated score: {’train_score’: 0.9952809245924918, ’dev_score’: 0.6372459669415207, ’test_score’: 0.6423549137767338, ’score’: 0.6372459669415207}, Visits: 2
103
104 [Node 0-2-1-0]
105 Plans:
106 5. Train a weighted ensemble model using the best performing models from task 4
107 Simulated: False
108 Score: avg score: 0, simulated score: {}, Visits: 0
109
110 [Node 0-2-1-1]
111 Plans:
112 5. Using the models that performed best in task 4, train a weighted ensemble model to improve overall performance.
113 Simulated: False
114 Score: avg score: 0, simulated score: {}, Visits: 0
115
116 [Node 0-2-1-2]
117 Plans:
118 5. Develop a weighted ensemble model by integrating the top-performing models from task 4, ensuring to evaluate and adjust the weights for optimal performance.
119 Simulated: True
120 Score: avg score: 0.6520761876370741, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6520761876370741, ’test_score’: 0.6563435152603494, ’score’: 0.6520761876370741}, Visits: 1
121
122 [Node 0-2-1-3]
123 Plans:
124 5. Train a weighted ensemble model by combining the predictions of the top-performing models from task 4 to improve overall performance.
125 Simulated: False
126 Score: avg score: 0, simulated score: {}, Visits: 0
127
128 [Node 0-2-1-4]
129 Plans:
130 5. Develop a weighted ensemble model by combining the top-performing models from task 4, ensuring to optimize the weights for improved performance.
131 Simulated: False
132 Score: avg score: 0, simulated score: {}, Visits: 0
133
134 [Node 0-2-2]
135 Plans:
136 4. Implement a Neural Network with multiple layers to capture the hierarchical patterns in the data and evaluate its performance
137 Simulated: False
138 Score: avg score: 0, simulated score: {}, Visits: 0
139
140 [Node 0-2-3]
141 Plans:
142 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance
143 Simulated: False
144 Score: avg score: 0, simulated score: {}, Visits: 0
145
146 [Node 0-2-4]
147 Plans:
148 4. Perform hyperparameter tuning using Grid Search or Random Search to train multiple models and evaluate their performance
149 Simulated: False
150 Score: avg score: 0, simulated score: {}, Visits: 0
151
152 [Node 0-3]
153 Plans:
154 3. Apply feature selection techniques such as Recursive Feature Elimination (RFE) or SelectKBest to identify and retain the most important features in the train, dev, and test datasets.
155 Simulated: True
156 Score: avg score: 0.49056683315196203, simulated score: {’train_score’: 0.9988177730410426, ’dev_score’: 0.51620611302976, ’test_score’: 0.525989891002361, ’score’: 0.51620611302976}, Visits: 2
157
158 [Node 0-3-0]
159 Plans:
160 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships, and evaluate its performance.
161 Simulated: False
162 Score: avg score: 0, simulated score: {}, Visits: 0
163
164 [Node 0-3-1]
165 Plans:
166 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance to model the complex decision boundaries between different gesture phases.
167 Simulated: True
168 Score: avg score: 0.4649275532741641, simulated score: {’train_score’: 0.7299159411193588, ’dev_score’: 0.4649275532741641, ’test_score’: 0.4631598897487413, ’score’: 0.4649275532741641}, Visits: 1
169
170 [Node 0-3-2]
171 Plans:
172 4. Implement and train a Neural Network with multiple layers to capture hierarchical patterns in the data and evaluate its performance
173 Simulated: False
174 Score: avg score: 0, simulated score: {}, Visits: 0
175
176 [Node 0-3-3]
177 Plans:
178 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance
179 Simulated: False
180 Score: avg score: 0, simulated score: {}, Visits: 0
181
182 [Node 0-3-4]
183 Plans:
184 4. Train multiple models, perform hyperparameter tuning using techniques like Grid Search or Random Search, and evaluate their performance
185 Simulated: False
186 Score: avg score: 0, simulated score: {}, Visits: 0
187
188 [Node 0-4]
189 Plans:
190 3. Create interaction features by combining existing features, such as the product of velocity and acceleration, to capture complex relationships in the train, dev, and test datasets
191 Simulated: False
192 Score: avg score: 0, simulated score: {}, Visits: 0
193
194Generated 29 unique codes.
195Best node: 0-1-1, score: {’train_score’: 1.0, ’dev_score’: 0.6944266833187726, ’test_score’: 0.6928451194338062, ’score’: 0.6944266833187726}
196Dev best node: 0-1-1, score: {’train_score’: 1.0, ’dev_score’: 0.6944266833187726, ’test_score’: 0.6928451194338062, ’score’: 0.6944266833187726}

In this case study, we demonstrate how SELA conducts a search cycle using MCTS:

Pre-search Step: Initialization
SELA begins by defining high-level stages, such as exploratory data analysis, data preprocessing, feature engineering, and model training, which structure the overall machine learning workflow. During the search, SELA populates these stages with specific insights, which act as experimental configurations for simulation.

Step 1 & 2: Selection and Expansion
SELA leverages MCTS to explore specific stages like feature engineering and model training. For example, in one iteration, SELA selects Node 0-1. This node corresponds to a stage insight that generates time-based features, expanding into five child nodes representing various model specifications and training strategies, such as Random Forests, Support Vector Machines, Neural Networks, Gradient Boosting, or Grid Search.

Step 3: Simulation
Next, SELA samples one of the expanded child nodes for simulation. For instance, when Node 0-1-1 is chosen, SELA runs a complete experiment where time-based feature engineering (Node 0-1) is followed by training a Support Vector Machine (SVM) with a kernel specified by Node 0-1-1. The simulation yields an evaluation score.

Step 4: Backpropagation
After the simulation, the resulting performance score is propagated back through the tree. For example, after simulating Node 0-1-1, MCTS updates the numeric feedback for its parent nodes, such as Node 0-1 and Node 0. The search cycle repeats from Steps 1 to 4 until a stopping condition is reached.

Post-search Step: Best Node Selection
In the final phase, SELA selects the node representing the best-performing solution. In this example, Node 0-1-1, using an SVM with an RBF kernel, achieved the highest score in the current dataset by combining effective feature engineering with advanced model training. SELA then presents the code associated with this node as the optimal solution.

Generated on Tue Oct 22 15:11:58 2024 by LaTeXML

## Metadata

```json
{
  "title": "\\methodname: Tree-Search Enhanced LLM Agents for Automated Machine Learning",
  "description": "",
  "url": "https://arxiv.org/html/2410.17238v1",
  "content": "1Introduction\n2Related Works\n3Method\n4Experiments\n5Conclusion\n\\methodname: Tree-Search Enhanced LLM Agents for Automated Machine Learning\nYizhou Chi1,2, Yizhang Lin11, Sirui Hong1, Duyi Pan3, Yaying Fei, Guanghao Mei4,\nBangbang Liu1, Tianqi Pang5, Jacky Kwok6, Ceyao Zhang7, Bang Liu8, Chenglin Wu12\n1DeepWisdom, 2University of California, Berkeley,\n3The Hong Kong University of Science and Technology (Guangzhou),\n4University of California, San Diego, 5South China Normal University,\n6Stanford University, 7The Chinese University of Hong Kong, Shenzhen,\n8Université de Montréal & Mila\nThese authors contributed equally to this work.Bang Liu (E-mail: bang.liu@umontreal.ca) and Chenglin Wu (E-mail: alexanderwu@deepwisdom.ai) are the corresponding authors.\nAbstract\n\nAutomated Machine Learning (AutoML) approaches encompass traditional methods that optimize fixed pipelines for model selection and ensembling, as well as newer LLM-based frameworks that autonomously build pipelines. While LLM-based agents have shown promise in automating machine learning tasks, they often generate low-diversity and suboptimal code, even after multiple iterations. To overcome these limitations, we introduce Tree-Search Enhanced LLM Agents (\\methodname), an innovative agent-based system that leverages Monte Carlo Tree Search (MCTS) to optimize the AutoML process. By representing pipeline configurations as trees, our framework enables agents to conduct experiments intelligently and iteratively refine their strategies, facilitating a more effective exploration of the machine learning solution space. This novel approach allows \\methodname to discover optimal pathways based on experimental feedback, improving the overall quality of the solutions. In an extensive evaluation across 20 machine learning datasets, we compare the performance of traditional and agent-based AutoML methods, demonstrating that \\methodname achieves a win rate of 65% to 80% against each baseline across all datasets. These results underscore the significant potential of agent-based strategies in AutoML, offering a fresh perspective on tackling complex machine learning challenges1.\n\n1Introduction\n\nAutomated Machine Learning (AutoML) is a rapidly evolving field that seeks to automate the process of designing reliable machine learning solutions with minimal human intervention. Traditional AutoML frameworks, such as Auto-WEKA (Thornton et al., 2013), Auto-Sklearn (Feurer et al., 2015; 2020), AutoGluon (Tang et al., 2024b), and H2O AutoML (LeDell & Poirier, 2020), rely on predefined search spaces and routines. These frameworks primarily focus on optimizing hyperparameters and model ensembling to find the best model configuration. However, this fixed and static approach often lacks the adaptability needed to handle diverse and dynamic data scenarios, resulting in suboptimal performance in more complex settings. Additionally, the traditional focus on model training leaves other crucial stages of the machine learning pipeline, such as data preprocessing and feature engineering, underexplored, thereby limiting the overall effectiveness of these systems.\n\nRecently, large language model (LLM)-based agents have emerged as promising tools for automating machine learning tasks by leveraging natural language processing capabilities to generate code. These systems typically begin with a natural language prompt describing the dataset and the problem, after which an LLM generates an end-to-end solution. Early efforts, such as Zhang et al. (2024), experimented with prompting LLMs to generate machine learning solutions, while Hong et al. (2024a) introduced agents equipped with Hierarchical Graph Modeling and Programmable Node Generation to address complex and dynamic workflows. Despite these advances, LLM-based solutions often fall short in generating diverse and highly optimized workflows, as their search process remains limited to a single pass or trial. Without iterative refinement or the ability to explore alternative strategies, these solutions frequently converge on suboptimal results, even when multiple attempts are allowed.\n\nA critical shortcoming of both traditional AutoML and LLM-based frameworks lies in their inability to mimic the nuanced problem-solving approach of human experts. When approaching a machine learning task, an expert does not simply execute a fixed pipeline or rely on a single attempt. Instead, they explore various potential configurations, systematically conduct experiments, analyze results, and iteratively refine their understanding of each component’s effectiveness. This iterative, feedback-driven process allows experts to explore diverse solutions and improve them incrementally until they arrive at the optimal configuration.\n\nFigure 1:\\methodname’s abstraction compared to other agent-based AutoML frameworks. There are two main types of agent-based approaches to AutoML problems. The first approach (Hong et al., 2024a) divides a machine learning task into multiple stages, proposing a plan for each stage, and generating and executing code step by step according to the plan, with no refinement after the solution is completed. The second (Schmidt et al., 2024) generates the entire solution in one step and iteratively refines it as a whole. \\methodname integrates both approaches, enabling stage-wise planning while iteratively exploring better solutions at each stage level.\n\nInspired by this human-centered approach, we propose Tree-Search Enhanced LLM Agents (\\methodname) for automated machine learning, a novel framework that integrates the strengths of LLM agents with a structured search and refinement process modeled on how experts solve machine learning problems. As illustrated in Figure 1, our framework combines the benefits of stage-wise planning, where each stage (e.g., Exploratory Data Analysis, Data Preprocessing, Feature Engineering, and Model Training) is handled sequentially, with an iterative refinement mechanism.\n\nIn \\methodname, the search space of a machine learning problem is proposed and conceptualized as a tree, where each branch represents a potential solution path. To navigate this search space, we employ Monte Carlo Tree Search (MCTS) (Coulom, 2007) as the core decision-making engine, leveraging its ability to balance exploration (testing new strategies) and exploitation (improving known good strategies). MCTS allows the agent to efficiently explore large decision spaces, collect and process experimental results, and intelligently select the next promising configuration to test on. By iterating through this cycle of experimentation and refinement, \\methodname incrementally improves its solutions, much like an expert who tests and improves its strategy based on continuous feedback.\n\nWe rigorously evaluated \\methodname using 20 diverse datasets from the AutoML Benchmark (Gijsbers et al., 2024), comparing its performance against both traditional AutoML systems and agent-based AutoML approaches. The results demonstrate that \\methodname consistently delivers superior performance across a wide range of machine learning tasks, validating its effectiveness and adaptability.\n\nTo summarize, our research makes the following contributions:\n\n1. \n\nWe introduce a feedback-driven approach for LLM agents to iteratively explore machine learning configurations, optimizing solutions over multiple experimental rounds.\n\n2. \n\nUsing Monte Carlo Tree Search, our system navigates a tree-structured search space, adaptively identifying high-performance pipelines through feedback.\n\n3. \n\nWe compare agent-based and traditional AutoML, highlighting agentic methods’ flexibility and potential for enhanced performance in machine learning.\n\n\t\nDynamic\nPipeline\n\t\nFeature\nEngineering\n\t\nModel\nTraining\n\t\nModel\nImprovement\n\t\nPipeline\nOptimization\n\nAutoGluon (Erickson et al., 2020) \t✗\t✗\tFixed models\tMulti-layer stacking + bagging\t✗\nAutoSklearn (Feurer et al., 2020) \t✗\t✗\tFixed models\tBayes Opt. + meta-learning + ensemble\t✗\nData Interpreter (Hong et al., 2024a) \t✓\tInstinctive\tInstinctive\tInstinctive\t✗\nAIDE (Schmidt et al., 2024) \t✓\tInstinctive\tDynamic & diverse\tDynamic & diverse\tOne-step refinement + LLM\n\\methodname (Ours)\t✓\tDynamic & diverse\tDynamic & diverse\tDynamic & diverse\tStepwise MCTS + LLM\nTable 1:Comparison of key capabilities across various AutoML methods. Dynamic indicates the system’s ability to adjust workflows based on intermediate outcomes, allowing it to adapt as new information emerges. Diverse refers to employing multiple strategies or methods across tasks, which helps capture varied modeling needs. Instinctive means that the system directly relies on the decisions generated by an LLM and heavily depends on the model’s inclination.\n2Related Works\n\nTree Search and Its Integration with LLMs Tree search algorithms have significantly advanced problem-solving in artificial intelligence, with Monte Carlo Tree Search (MCTS) emerging as a leading technique. These algorithms have been successfully applied across various domains, including robotics (Wu et al., 2015; Clary et al., 2018; Best et al., 2019), chemistry (Segler et al., 2018), and gaming (Silver et al., 2016; 2017), where MCTS is used to navigate vast solution spaces and solve complex problems. More recently, research has focused on integrating tree search with Large Language Models (LLMs) to enhance reasoning and decision-making. Studies such as Krishnamurthy et al. (2024) and Dwaracherla et al. (2024) explored LLMs’ capacities for efficient exploration, while Tang et al. (2024a) and Hui & Tu (2024) developed strategies for exploiting previously learned knowledge. Zhou et al. (2024) and Chi et al. (2024) applied MCTS for planning with external or self-evaluated feedback, while Feng et al. (2023); Wang et al. (2024) adapted AlphaZero-style tree search to LLM-based tasks. These advancements underscore the potential of combining tree search methods with LLMs, balancing exploration of new solutions with exploitation of prior knowledge to enhance decision-making.\n\nAdvances and Limitations in AutoML Systems Automated Machine Learning (AutoML) frameworks were introduced to reduce the need for expert knowledge in designing machine learning pipelines. Early AutoML efforts, such as (Thornton et al., 2013; Olson & Moore, 2016; Jin et al., 2019; Feurer et al., 2020; Erickson et al., 2020; LeDell & Poirier, 2020; Wang et al., 2021), focused primarily on automating key pipeline components like hyperparameter optimization, model selection, stacking, and ensembling. These frameworks achieved notable progress by integrating meta-learning and hyperparameter search strategies to automatically select and tune machine learning models. Furthermore, extensions into multi-modal data settings (Tang et al., 2024b; Jin et al., 2023) have broadened AutoML’s applicability.\n\nRecently, there has been growing interest in leveraging LLMs within AutoML systems to enhance pipeline flexibility. Studies such as Hollmann et al. (2024); Li et al. (2024) applied LLMs to automate feature engineering, while Liu et al. (2024) introduced LLMs for hyperparameter tuning. In addition, Luo et al. (2024) proposed embedding LLMs at each stage of the machine learning workflow. Despite these advancements, traditional AutoML systems remain constrained by rigid pipelines and limited flexibility to adapt to unique datasets or specific task requirements.\n\nLLM Agents for Dynamic Machine Learning Pipelines In contrast to static pipelines, LLM-based agents offer a more dynamic solution for addressing complex machine learning challenges. Hong et al. (2024a; b) introduced an LLM agent with hierarchical graph modeling and programmable node generation, enabling the creation of sophisticated, adaptable pipelines for diverse data scenarios. Similarly, Zhang et al. (2024) demonstrated that LLMs could effectively interpret structured inputs and apply past experiences to solve new machine learning tasks. Guo et al. (2024) expanded on this by introducing a data science agent that leverages case-based reasoning; however, it faces challenges when generating solutions from scratch due to its reliance on existing codebases. Schmidt et al. (2024) proposed an iterative approach, where the entire pipeline is generated in one step and refined iteratively through incremental modifications.\n\nBuilding on these efforts, \\methodname introduces an agent that integrates the strengths of both approaches—stage-wise planning and iterative refinement—allowing it to autonomously explore and generate machine learning solutions from the ground up. This approach offers greater flexibility and control during the search process, enabling the generation of optimized solutions at each stage. Table 1 highlights the functionalities provided by different AutoML systems.\n\n3Method\n\nAs illustrated in Figure 2, \\methodname consists of three key components: an LLM-based insight proposer, a search module using MCTS, and an LLM agent as the experiment executor. First, the LLM generates insights from the problem description and dataset, defining a search space. The search module then organizes this space into a tree structure and uses MCTS to explore promising paths. During each cycle, the selected path is passed to the LLM agent, which translates the configuration into an executable pipeline. The agent plans, codes, and executes the experiment, feeding the results back to refine future searches. This iterative process continues until the termination criterion is met. The following sections provide a detailed explanation of each component.\n\nFigure 2:\\methodname’s pipeline operates as follows: The system begins by inputting the problem description and dataset information into the LLM, which generates a search space of potential solutions, encompassing data preprocessing, feature engineering, and model training. The search module, powered by Monte Carlo Tree Search (MCTS), explores this space by selecting, expanding, and simulating potential configurations. The LLM agent then simulates the selected configuration by planning, coding, and executing the experiment. Feedback from the simulation is fed back into the search module, where it is used in the backpropagation step to refine future searches. This iterative process continues until a predefined stopping criterion is met, resulting in an optimized experimental pipeline.\n3.1Insight Proposal and Search Space Creation\n\nTo enable \\methodname to explore a wide range of machine learning strategies, we introduce an insight proposer that generates diverse methods tailored to different stages of the machine learning workflow. Each proposed insight suggests either a single technique or a combination of methods aimed at enhancing performance. For instance, a feature engineering insight might recommend creating interaction features from existing variables, while a model training insight could propose a specific algorithm or suggest running a grid search to improve accuracy.\n\nThe insight proposer takes as input the problem description \n𝑝\n and dataset information \n𝑑\n, such as metadata and sample records, and generates \n𝑚\n insights \n𝜆\n for each stage of the machine learning process using a large language model \n𝑀\n. These insights are stored in an insight pool, forming a search space \nΛ\n for \\methodname to explore. We decompose the machine learning process into five stages: Exploratory Data Analysis (\n𝜏\n1\n), Data Preprocessing (\n𝜏\n2\n), Feature Engineering (\n𝜏\n3\n), Model Training (\n𝜏\n4\n), and Model Evaluation (\n𝜏\n5\n). For simplicity, we denote the entire set of stages as \n𝑇\n and refer to any specific stage as \n𝜏\n.\n\n\t\nInsightProposer\n⁢\n(\n𝑝\n,\n𝑑\n,\n𝑀\n)\n→\nΛ\n:=\n{\n𝜆\n𝑖\n𝜏\n∣\n𝜏\n∈\n𝑇\n,\n𝑖\n=\n1\n,\n…\n,\n𝑚\n}\n\t\t\n(1)\n3.2Pipeline Execution and Code Generation\n\nWe employ an LLM agent, referred to as the experiment executor \n𝐸\n, to conduct each trial by building practical experimental pipelines from natural language requirements. The agent takes two main steps in this process. First, given an experiment configuration \n𝑐\n, which is a set of insights provided by the search module (introduced in Section 3.3.2), the experiment executor translates these insights into a detailed plan. This plan consists of a sequence of task instructions \n𝐼\n𝜏\n∈\n𝑇\n corresponding to each stage of the machine learning process. This step is referred to as \n𝐸\nplan\n.\n\nNext, following the plan, the agent writes and executes code \n𝜎\n𝜏\n for each task \n𝜏\n based on the respective instruction \n𝐼\n𝜏\n, producing the code \n𝜎\n𝜏\n∈\n𝑇\n for the full pipeline, along with the final execution score \n𝑠\n. The complete set of code outputs \n𝜎\n𝜏\n∈\n𝑇\n is concatenated into a full solution \n𝜎\n𝑠\n⁢\n𝑜\n⁢\n𝑙\n to address the problem. This phase is referred to as \n𝐸\ncode & execute\n.\n\n\t\n𝐸\nplan\n⁢\n(\n𝑝\n,\n𝑑\n,\n𝑐\n,\n𝑀\n)\n\t\n→\n𝐼\n𝜏\n∈\n𝑇\n\t\t\n(2)\n\n\t\n𝐸\ncode & execute\n⁢\n(\n𝐼\n𝜏\n∈\n𝑇\n,\n𝐷\n,\n𝑀\n)\n\t\n→\n(\n𝜎\n𝜏\n∈\n𝑇\n,\n𝑠\n)\n\t\t\n(3)\n3.3Tree Search in Machine Learning Experiments\n\nIn order to systematically explore the different configurations in machine learning experiments, we model the search space as a hierarchical tree. This structure allows us to apply tree search algorithms, where each path through the tree represents a different experiment configuration. Algorithm 1 also provides an overview of this searching process.\n\n3.3.1Experiment Node\n\nTo facilitate the exploration of various strategies, we model the proposed search space as a hierarchical tree that is well-suited for applying search algorithms. Each node in the tree, denoted as \n𝑥\n, represents one insight \n𝜆\n in the search space \nΛ\n and contains the following attributes:\n\n• \n\nInsight \n𝜆\n⁢\n(\n𝑥\n)\n: Represents the specific insight \n𝜆\n𝑖\n𝜏\n∈\nΛ\n associated with this node, where \n𝜏\n denotes the stage of the machine learning pipeline.\n\n• \n\nDepth \n𝛿\n⁢\n(\n𝑥\n)\n: Indicates the stage of the machine learning process the node corresponds to (e.g., depth 1 might represent data preprocessing, depth 2 for feature engineering, and depth 3 for model training).\n\n• \n\nValue \n𝑣\n⁢\n(\n𝑥\n)\n: The cumulative score from simulations for this node and all its descendants.\n\n• \n\nNumber of Visits \n𝑛\nvisits\n⁢\n(\n𝑥\n)\n: The total number of simulations conducted for this node and its descendants.\n\n• \n\nSimulation Score \n𝑠\n⁢\n(\n𝑥\n)\n: The score for simulating this node.\n\n• \n\nSolution Code \n𝜎\nsol\n⁢\n(\n𝑥\n)\n The final code produced after the node simulation.\n\n• \n\nStage Code \n𝜎\nstage\n⁢\n(\n𝑥\n)\n: The code generated up to the node’s current stage, a part of the solution code\n\nBy modeling the search space as a tree, each path from the root to a node \n𝑥\n represents an experiment configuration \n𝑐\n⁢\n(\n𝑥\n)\n=\n{\n𝜆\n⁢\n(\n𝑥\n1\n)\n,\n𝜆\n⁢\n(\n𝑥\n2\n)\n,\n…\n,\n𝜆\n⁢\n(\n𝑥\n)\n}\n⊂\nΛ\n, where \n𝑥\n1\n,\n𝑥\n2\n,\n…\n,\n𝑥\n are nodes along the path. The task of finding the optimal solution can therefore be viewed as a path search within the tree, where each path corresponds to a potential configuration of the experiment.\n\n3.3.2Tree Search for ML Experiments\n\nWe apply Monte Carlo Tree Search (MCTS) to systematically explore and identify optimal machine learning solutions within our framework. MCTS allows us to efficiently navigate the search space across multiple stages of the machine learning pipeline—from data preprocessing to model selection—by balancing exploration and exploitation.\n\nAlgorithm 1 \\methodname using MCTS\n0:  Problem description \n𝑝\n, data information \n𝑑\n, data \n𝐷\n, LLM \n𝑀\n, rollout number \n𝑘\n.\n1:  \nΛ\n←\nInsightProposer\n⁢\n(\n𝑝\n,\n𝑑\n,\n𝑀\n)\n2:  Initialize Tree using \nΛ\n3:  for \n𝑖\n = 1 to \n𝑘\n do\n4:     node \n𝑥\n←\n select(Tree)\n5:     \n𝑋\nchild\n←\n expand(Tree, \n𝑥\n)\n6:     Randomly sample a node \n𝑥\nsample\n from \n𝑋\nchild\n7:     Retreive experiment configuration \n𝑐\n⁢\n(\n𝑥\nsample\n)\n8:     \n𝜎\n𝑠\n⁢\n𝑜\n⁢\n𝑙\n,\n𝑠\n←\nsimulate\n⁢\n(\n𝑐\n⁢\n(\n𝑥\nsample\n)\n,\n𝑝\n,\n𝑑\n,\n𝐷\n,\n𝑀\n)\n9:     attach the simulation result \n𝜎\n𝑠\n⁢\n𝑜\n⁢\n𝑙\n,\n𝑠\n to \n𝑥\nsample\n for final solution selection\n10:     Backpropagate(Tree, \n𝑠\n)\n11:  end for\n12:  \n𝑥\ndev best\n←\nargmax\n𝑥\n∈\nTree\n⁢\n(\n𝑠\n⁢\n(\n𝑥\n)\n)\n12:  \n𝜎\n𝑠\n⁢\n𝑜\n⁢\n𝑙\n⁢\n(\n𝑥\ndev best\n)\n \nAlgorithm 2 Simulate\n0:  Experiment configuration \n𝑐\n, problem description \n𝑝\n, data information \n𝑑\n, data \n𝐷\n, LLM \n𝑀\n.\n1:  Draft plans \n𝐼\n𝜏\n∈\n𝑇\n←\n𝐸\nplan\n⁢\n(\n𝑝\n,\n𝑑\n,\n𝑐\n,\n𝑀\n)\n2:  Code and execute sequentially \n𝜎\n𝜏\n∈\n𝑇\n,\n𝑠\n←\n𝐸\ncode & execute\n⁢\n(\n𝐼\n𝜏\n∈\n𝑇\n,\n𝐷\n,\n𝑀\n)\n3:  \n𝜎\n𝑠\n⁢\n𝑜\n⁢\n𝑙\n←\nconcatenate\n⁢\n(\n𝜎\n𝜏\n∈\n𝑇\n)\n3:  \n𝜎\n𝑠\n⁢\n𝑜\n⁢\n𝑙\n,\n𝑠\n\nThe search process involves performing multiple rollouts, which include the steps of selection, expansion, simulation, and backpropagation. We conduct \n𝑘\n rollouts to explore various paths, aiming to identify the best solution.\n\nSelection At each iteration, we use a modified version of the UCT (Upper Confidence Bound for Trees) algorithm (Kocsis & Szepesvári, 2006), referred to as UCT-DP (depth-preferred), to select a node from the search tree. Unlike traditional MCTS, where simulations are often performed quickly due to a fixed action space and negligible action time, the context of machine learning tasks presents a different challenge. Processes such as model training introduce significant computational time, making efficient node exploration crucial. Since model selection can heavily influence the overall machine learning performance, we prioritize exploring nodes at greater depths early on.\n\nThis modification reduces the need to explore every unvisited node, allowing deeper nodes to be reached in fewer iterations—making the approach better suited for large-scale machine learning experiments. The modified selection algorithm is expressed as:\n\n\t\nUCT-DP\n⁢\n(\n𝑥\n)\n=\n𝑣\n⁢\n(\n𝑥\n)\n𝑛\n⁢\n(\n𝑥\n)\n+\n𝛼\nexplore\n⁢\nln\n⁡\n𝑛\nvisits\n⁢\n(\n𝑥\nparent\n)\n𝑛\n⁢\n(\n𝑥\n)\n\t\t\n(4)\n\t\n𝑛\n⁢\n(\n𝑥\n)\n=\n{\n𝛼\nunvisted\n\t\nif \n⁢\n𝑛\nvisits\n⁢\n(\n𝑥\n)\n=\n0\n\n\n𝑛\nvisits\n⁢\n(\n𝑥\n)\n\t\notherwise.\n\t\t\n(5)\n\nHere, \n𝛼\nunvisted\n is a constant between 0 and 1 controlling the selection preference for unvisited nodes, balancing between full exploration and computational efficiency. This adjustment allows us to focus more on deeper parts of the tree that are likely to yield better solutions.\n\nExpansion During the expansion phase, a set of child nodes \n𝑋\nchild\n are instantiated from the selected node \n𝑥\n for potential simulation. Note that a child node \n𝑥\nchild\n from the node \n𝑥\n at depth \n𝛿\n inherits the attributes of \n𝑥\n and possesses \n𝜆\n⁢\n(\n𝑥\nchild\n)\n→\n𝜆\n𝜏\n𝛿\n+\n1\n, an insight of stage \n𝜏\n𝛿\n+\n1\n from the search space.\n\nSimulation Once expanded, a node \n𝑥\nsample\n is randomly sampled from \n𝑋\nchild\n for simulation. The path from root to the sampled node forms a set of insights \n𝑐\n⁢\n(\n𝑥\nsample\n)\n=\n{\n𝜆\n⁢\n(\n𝑥\n1\n)\n,\n𝜆\n⁢\n(\n𝑥\n2\n)\n,\n…\n,\n𝜆\n⁢\n(\n𝑥\nsample\n)\n}\n⊂\nΛ\n, representing the experiment configuration to be simulated, where \n𝑥\n1\n,\n𝑥\n2\n,\n.\n.\n,\n𝑥\nsample\n are the nodes along the path. The configuration \n𝑐\n⁢\n(\n𝑥\nsample\n)\n is then fed to the experimenter \n𝐸\n for execution following \n𝐸\nplan\n and \n𝐸\ncode & execute\n, which produces a simulation score \n𝑠\n, as illustrated in Section 3.3.1. The score serves as the feedback for back propagation. Algorithm 2 outlines the simulation process.\n\nBackpropagation After the simulation concludes, the performance score (e.g., based on the development set) is retrieved and backpropagated through the tree. The score is propagated from the simulated node up to the root, updating each parent node’s value and visit count. This allows nodes representing more promising solutions to be prioritized in future rollouts. In addition, the solution code is also backpropagated up to the tree, and it can be processed and saved as stage code depending on the parent node during the update.\n\nBackpropagation ensures that the algorithm learns which paths yield better results, guiding the search toward higher-performing nodes as more rollouts are conducted.\n\n3.3.3Experiment State Saving and Loading\n\nTo boost experimentation efficiency and reduce token usage, \\methodname implements fine-grained code reuse by caching code at the stage level for each attempted configuration \n𝑐\n. This allows the framework to reuse as much saved code as possible when a new configuration \n𝑐\nnew\n shares components with existing ones. Additionally, this technique addresses the challenge of LLM non-determinism, where identical instructions can produce different code, increasing variance in final performance. Specifically, whenever a node is chosen for execution, the experimenter loads and reruns the saved stage code, if available, ensuring consistency before progressing to the next stage. This approach effectively conserves resources while maintaining robust performance across stages. In Appendix D, we examine the cost efficiency of this state-saving and loading mechanism.\n\n4Experiments\n4.1Experimental Setup\nDatasets\n\nWe evaluate \\methodname alongside several baselines on 20 datasets, which include 13 classification tasks and 7 regression tasks from the AutoML Benchmark (AMLB) (Gijsbers et al., 2024) and Kaggle Competitions.\n\nTable 4 provides detailed information on the datasets used. All datasets are split into training, validation, and test sets with a 6:2:2 ratio. Each framework utilizes the training and validation sets to train models and makes predictions on the test set labels.\n\nEvaluation Metrics\n\nFor the AMLB datasets, we use the default target column provided by OpenML. For Kaggle competition datasets, we rely on the target column specified in the competition description. Performance is measured using root mean squared error (RMSE) for regression tasks, F1 score for binary classification, and F1-weighted score for multi-class classification. To ensure comparability across datasets with varying metrics, we introduce a Normalized Score (NS), which maps RMSE into the range from 0 to 1.\n\n\t\nNS\n⁢\n(\n𝑠\nraw\n)\n=\n{\n1\n1\n+\nlog\n⁡\n(\n1\n+\n𝑠\nraw\n)\n\t\nif the metric is RMSE.\n\n\n𝑠\nraw\n\t\notherwise.\n\t\t\n(6)\n\nHere, \n𝑠\n𝑟\n⁢\n𝑎\n⁢\n𝑤\n represents the raw score before normalization. To evaluate \\methodname against other frameworks, we employ three key metrics: average Normalized Score (NS), average rank, and average best rank. The average rank is calculated by considering all rankings of a method across datasets, while the average best rank focuses on the method’s best performance in each dataset. We also want to quantify how other baselines perform relative to \\methodname. The “Rescaled NS” is defined as:\n\n\t\nRescaled NS\n⁢\n(\n𝑓\n)\n=\nNS\n𝑓\nNS\n\\methodname\n\t\t\n(7)\n\nwhere \n𝑓\n represents the baseline method being compared to \\methodname.\n\nMethod and Baselines Setup\n\nWe compare \\methodname with several baseline methods, including Data Interpreter (Hong et al., 2024a), AIDE (Schmidt et al., 2024), AutoGluon (Erickson et al., 2020), and AutoSklearn (Feurer et al., 2015; 2020).\n\nFor our LLM-based approaches (\\methodname, Data Interpreter, and AIDE), we employ a consistent initial task prompt across all methods. This prompt encompasses the dataset name, target column, and evaluation metric. We choose DeepSeek v2.5 (DeepSeek-AI, 2024) as our foundation LLM due to its open-source nature, strong coding capabilities, and cost-effective token usage. To encourage output diversity, we set the temperature parameter to 0.5 for all LLM-based methods. AIDE conducts 10 iterations per execution, while \\methodname performs 10 rollouts.\n\nFor \\methodname, we employ Data Interpreter as the experimenter, leveraging its multi-step generation capability. We configured the hyperparameters of UCT-DP as follows: \n𝛼\nunvisited\n is set to 0.8 and \n𝛼\nexplore\n is set to 1.4. These settings aim to balance exploration and exploitation in the method’s search strategy.\n\nEach method, except for AutoGluon, is run three times for each dataset. AutoGluon, being deterministic, is run only once with its default settings. AutoSklearn is also run with default settings, limited to 600 seconds per task.\n\nMethod\tWins\tLosses\tTop 1\tAvg. NS % \n↑\n\tAvg. Best NS % \n↑\n\tAvg. Rank \n↓\n\tAvg. Best Rank \n↓\n\nAutoGluon\t7\t13\t4\t53.2\t53.2\t4.4\t4.4\nAutoSklearn\t5\t15\t5\t46.1\t47.5\t7.6\t6.1\nAIDE\t5\t15\t2\t47.1\t51.8\t7.8\t5.3\nData Interpreter\t4\t16\t2\t47.4\t50.2\t8.8\t6.4\n\\methodname\t-\t-\t7\t53.3\t54.7\t4.8\t2.7\nTable 2:Results of each AutoML framework on 20 tabular datasets. The “Wins” column indicates the number of datasets where the method outperforms \\methodname, while “Losses” shows the number of datasets where the method underperforms. The “Top 1” column represents the number of datasets where the method produces the best predictions across methods.\n4.2Results\nFigure 3:Rescaled NS of AutoML frameworks relative to \\methodname on tabular datasets. Points to the left of the vertical line indicate poorer predictions compared to \\methodname. Notably, \\methodname often occupies a leading position across the datasets.\n\nAs shown in Table 2, \\methodname achieves the highest average Normalized Score (NS) and average best rank among all frameworks. Notably, \\methodname excels in producing the highest number of top predictions, as indicated in the “Top 1” column across all datasets. Furthermore, the “Losses” column reveals that each competing method falls short against \\methodname, losing in 65-80% of the datasets.\n\nInterestingly, AutoGluon exhibits a marginally higher average rank than \\methodname. This slight discrepancy may be attributed to the inherent randomness in LLMs and model training processes, which can influence the exploration of machine learning solutions. However, \\methodname’s higher average NS suggests that it performs strongly in the datasets where it excels, while its losses in other datasets are relatively minor. This means that even when \\methodname produces lower-ranked solutions, the performance gap is small, allowing it to fully compensate in the datasets where it performs well.\n\nThe two other agent-based methods exhibit relatively lower performance. The first method, Data Interpreter, struggles to enhance its score with multiple attempts due to its inability to refine its solution after completing a machine learning task. The second method, AIDE, does not have a stage-specific planning module, limiting its capacity to improve results after a series of greedy exploitation, which makes it prone to falling into local optima. These limitations likely account for their weaker performance.\n\nFigure 3 further corroborates \\methodname’s effectiveness, revealing that its best solutions frequently occupy leading positions across various datasets. This visual representation exhibits the method’s consistent high performance and adaptability across different ML datasets. We also include a detailed results of each method in Appendix C.\n\n4.3Ablation Study\n\nFor the rest of the study, we employ a subset of datasets to evaluate \\methodname under various settings. Our selection process involves choosing the first two datasets alphabetically for each machine learning task. Specifically, we use boston, colleges, credit-g, Click_prediction_small, GesturePhaseSegmentationProcessed, and mfeat-factors to conduct the ablation study.\n\n\tData Interpreter\t\\methodname (Random Search)\t\\methodname (MCTS)\nAvg. NS \n↑\n \t56.4\t58.6\t60.9\nAvg. Best NS \n↑\n \t59.0\t61.4\t62.4\nAvg. Rank \n↓\n \t6.9\t4.8\t3.3\nAvg. Best Rank \n↓\n \t4.8\t2.8\t1.5\nTable 3:Performance results for each search setting on the chosen datasets. \\methodname with MCTS consistently surpasses \\methodname with Random Search.\nEffectiveness of Search\n\nTo evaluate the effectiveness of Monte Carlo Tree Search (MCTS) in improving the solution search process, we conducted an ablation study. In this study, we compared the performance of our method using MCTS against a variant that randomly samples insights from each stage’s insight pool. As shown in Table 3, the MCTS version achieves a higher average normalized score across datasets and a better overall ranking compared to the random sampling approach. Moreover, even the random sampling variant of our method outperforms Data Interpreter, the base experimenter. This suggests the presence of an appropriate search space and an experiment agenda is vital for improving a machine learning agent. Our insight proposer generates relevant and useful insights, facilitating such improvement, regardless of the selection method.\n\nNumber of Rollouts\n\nFigure 5 illustrates that the average performance of \\methodname improves as the number of permitted rollouts increases. The trend demonstrates the strong scalability of \\methodname, as it efficiently leverages additional opportunities to explore the search space, improving the normalized score by 4.7% after 10 rollouts and 6.4% after 20, compared to the initial rollout.\n\nFigure 4:The average performance of \\methodname on six selected datasets with an increasing number of rollouts.\nFigure 5:Comparison of Normalized Scores between different base LLMs on six selected datasets.\nLLM Adaptability\n\nTo evaluate the robustness of our framework, we conduct experiments using different Large Language Models (LLMs). Specifically, we compare the performance of \\methodname with Claude-3.5-Sonnet (Anthropic, 2024) and GPT-4o (OpenAI, 2024) against DeepSeek V2.5 which we primarily use for evaluation. This comparison enables us to assess how the choice of LLM affects the overall effectiveness of our approach.\n\nAs Figure 5 shown, \\methodname delivers similar results across different LLMs, indicating its flexibility with various models depending on user preference and availability. We also report the numeric results in Appendix C.2.\n\n5Conclusion\n\nIn this paper, we introduced \\methodname, a novel framework that integrates LLM-based agents with Monte Carlo Tree Search (MCTS) to automate machine learning workflows. Our experimental results, conducted on 20 machine learning datasets, demonstrate \\methodname’s effectiveness and highlight its distinct advantages over both traditional AutoML frameworks and existing LLM-based approaches. The proposed methodology is not limited to machine learning but could be adapted to a wide range of sequential decision-making problems, provided they can be represented as tree structures with scalar rewards derived from their leaf nodes. Looking ahead, future work could explore extending this framework to other domains, including software engineering, scientific discovery, game playing, and robotics. Furthermore, improving the efficiency and scalability of the tree search process for larger solution spaces remains an important area for investigation. Another promising direction is developing techniques to provide interpretable explanations of the search process and solution rationale, enhancing the transparency and trustworthiness of the system. \\methodname represents a significant advancement in automated machine learning, demonstrating the potential of combining traditional search algorithms with the flexibility of LLMs.\n\nReferences\nAnthropic (2024)\tAnthropic.Introducing Claude 3.5 Sonnet — anthropic.com.https://www.anthropic.com/news/claude-3-5-sonnet, 2024.\nBest et al. (2019)\tGraeme Best, Oliver M Cliff, Timothy Patten, Ramgopal R Mettu, and Robert Fitch.Dec-mcts: Decentralized planning for multi-robot active perception.The International Journal of Robotics Research, 38(2-3):316–337, 2019.doi: 10.1177/0278364918755924.\nChi et al. (2024)\tYizhou Chi, Kevin Yang, and Dan Klein.Thoughtsculpt: Reasoning with intermediate revision and search, 2024.\nClary et al. (2018)\tPatrick Clary, Pedro Morais, Alan Fern, and Jonathan Hurst.Monte-carlo planning for agile legged locomotion.Proceedings of the International Conference on Automated Planning and Scheduling, 28(1):446–450, Jun. 2018.doi: 10.1609/icaps.v28i1.13933.\nCoulom (2007)\tRémi Coulom.Efficient selectivity and backup operators in monte-carlo tree search.In H. Jaap van den Herik, Paolo Ciancarini, and H. H. L. M. (Jeroen) Donkers (eds.), Computers and Games, pp.  72–83, Berlin, Heidelberg, 2007. Springer Berlin Heidelberg.ISBN 978-3-540-75538-8.\nDeepSeek-AI (2024)\tDeepSeek-AI.Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model, 2024.\nDwaracherla et al. (2024)\tVikranth Dwaracherla, Seyed Mohammad Asghari, Botao Hao, and Benjamin Van Roy.Efficient exploration for llms, 2024.\nErickson et al. (2020)\tNick Erickson, Jonas Mueller, Alexander Shirkov, Hang Zhang, Pedro Larroy, Mu Li, and Alexander Smola.Autogluon-tabular: Robust and accurate automl for structured data, 2020.\nFeng et al. (2023)\tXidong Feng, Ziyu Wan, Muning Wen, Ying Wen, Weinan Zhang, and Jun Wang.Alphazero-like tree-search can guide large language model decoding and training, 2023.\nFeurer et al. (2015)\tMatthias Feurer, Aaron Klein, Katharina Eggensperger, Jost Springenberg, Manuel Blum, and Frank Hutter.Efficient and robust automated machine learning.In Advances in Neural Information Processing Systems 28 (2015), pp.  2962–2970, 2015.\nFeurer et al. (2020)\tMatthias Feurer, Katharina Eggensperger, Stefan Falkner, Marius Lindauer, and Frank Hutter.Auto-sklearn 2.0: Hands-free automl via meta-learning, 2020.\nGijsbers et al. (2024)\tPieter Gijsbers, Marcos L. P. Bueno, Stefan Coors, Erin LeDell, Sébastien Poirier, Janek Thomas, Bernd Bischl, and Joaquin Vanschoren.Amlb: an automl benchmark.Journal of Machine Learning Research, 25(101):1–65, 2024.\nGuo et al. (2024)\tSiyuan Guo, Cheng Deng, Ying Wen, Hechang Chen, Yi Chang, and Jun Wang.Ds-agent: Automated data science by empowering large language models with case-based reasoning, 2024.\nHollmann et al. (2024)\tNoah Hollmann, Samuel Müller, and Frank Hutter.Large language models for automated data science: Introducing caafe for context-aware automated feature engineering, 2024.\nHong et al. (2024a)\tSirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu, Binhao Wu, Danyang Li, Jiaqi Chen, Jiayi Zhang, Jinlin Wang, Li Zhang, Lingyao Zhang, Min Yang, Mingchen Zhuge, Taicheng Guo, Tuo Zhou, Wei Tao, Wenyi Wang, Xiangru Tang, Xiangtao Lu, Xiawu Zheng, Xinbing Liang, Yaying Fei, Yuheng Cheng, Zongze Xu, and Chenglin Wu.Data interpreter: An llm agent for data science, 2024a.\nHong et al. (2024b)\tSirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber.MetaGPT: Meta programming for a multi-agent collaborative framework.In The Twelfth International Conference on Learning Representations, 2024b.\nHui & Tu (2024)\tWenyang Hui and Kewei Tu.Rot: Enhancing large language models with reflection on search trees, 2024.\nJin et al. (2019)\tHaifeng Jin, Qingquan Song, and Xia Hu.Auto-keras: An efficient neural architecture search system.In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining, pp.  1946–1956, 2019.\nJin et al. (2023)\tHaifeng Jin, François Chollet, Qingquan Song, and Xia Hu.Autokeras: An automl library for deep learning.Journal of machine Learning research, 24(6):1–6, 2023.\nKocsis & Szepesvári (2006)\tLevente Kocsis and Csaba Szepesvári.Bandit based monte-carlo planning.In Johannes Fürnkranz, Tobias Scheffer, and Myra Spiliopoulou (eds.), Machine Learning: ECML 2006, pp.  282–293, Berlin, Heidelberg, 2006. Springer Berlin Heidelberg.ISBN 978-3-540-46056-5.\nKrishnamurthy et al. (2024)\tAkshay Krishnamurthy, Keegan Harris, Dylan J. Foster, Cyril Zhang, and Aleksandrs Slivkins.Can large language models explore in-context?, 2024.\nLeDell & Poirier (2020)\tErin LeDell and Sebastien Poirier.H2O AutoML: Scalable automatic machine learning.7th ICML Workshop on Automated Machine Learning (AutoML), July 2020.\nLi et al. (2024)\tDawei Li, Zhen Tan, and Huan Liu.Exploring large language models for feature selection: A data-centric perspective, 2024.\nLiu et al. (2024)\tSiyi Liu, Chen Gao, and Yong Li.Large language model agent for hyper-parameter optimization.arXiv preprint arXiv:2402.01881, 2024.\nLuo et al. (2024)\tDaqin Luo, Chengjian Feng, Yuxuan Nong, and Yiqing Shen.Autom3l: An automated multimodal machine learning framework with large language models.arXiv preprint arXiv:2408.00665, 2024.\nOlson & Moore (2016)\tRandal S Olson and Jason H Moore.Tpot: A tree-based pipeline optimization tool for automating machine learning.In Workshop on automatic machine learning, pp.  66–74. PMLR, 2016.\nOpenAI (2024)\tOpenAI.Hello GPT-4o.https://openai.com/index/hello-gpt-4o/, 2024.\nSchmidt et al. (2024)\tDominik Schmidt, Yuxiang Wu, and Zhengyao Jiang.Aide: Human-level performance in data science competitions, 2024.URL https://www.weco.ai/blog/technical-report.\nSegler et al. (2018)\tMarwin Segler, Mike Preuss, and Mark Waller.Planning chemical syntheses with deep neural networks and symbolic ai.Nature, 555:604–610, 03 2018.doi: 10.1038/nature25978.\nSilver et al. (2016)\tDavid Silver, Aja Huang, Chris J. Maddison, Arthur Guez, L. Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Vedavyas Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy P. Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, and Demis Hassabis.Mastering the game of go with deep neural networks and tree search.Nature, 2016.\nSilver et al. (2017)\tDavid Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy P. Lillicrap, Fan Hui, L. Sifre, George van den Driessche, Thore Graepel, and Demis Hassabis.Mastering the game of go without human knowledge.Nature, 2017.\nTang et al. (2024a)\tHao Tang, Keya Hu, Jin Peng Zhou, Sicheng Zhong, Wei-Long Zheng, Xujie Si, and Kevin Ellis.Code repair with llms gives an exploration-exploitation tradeoff, 2024a.\nTang et al. (2024b)\tZhiqiang Tang, Haoyang Fang, Su Zhou, Taojiannan Yang, Zihan Zhong, Tony Hu, Katrin Kirchhoff, and George Karypis.Autogluon-multimodal (automm): Supercharging multimodal automl with foundation models.arXiv preprint arXiv:2404.16233, 2024b.\nThornton et al. (2013)\tChris Thornton, Frank Hutter, Holger H Hoos, and Kevin Leyton-Brown.Auto-weka: Combined selection and hyperparameter optimization of classification algorithms.In Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining, pp.  847–855, 2013.\nWang et al. (2024)\tAnte Wang, Linfeng Song, Ye Tian, Baolin Peng, Dian Yu, Haitao Mi, Jinsong Su, and Dong Yu.Litesearch: Efficacious tree search for llm, 2024.\nWang et al. (2021)\tChi Wang, Qingyun Wu, Markus Weimer, and Erkang Zhu.Flaml: A fast and lightweight automl library.In MLSys, 2021.\nWu et al. (2015)\tFeng Wu, Sarvapali D. Ramchurn, Wenchao Jiang, Jeol E. Fischer, Tom Rodden, and Nicholas R. Jennings.Agile planning for real-world disaster response.In Proceedings of the 24th International Conference on Artificial Intelligence, IJCAI’15, pp.  132–138. AAAI Press, 2015.ISBN 9781577357384.\nZhang et al. (2024)\tLei Zhang, Yuge Zhang, Kan Ren, Dongsheng Li, and Yuqing Yang.Mlcopilot: Unleashing the power of large language models in solving machine learning tasks, 2024.\nZhou et al. (2024)\tAndy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang.Language agent tree search unifies reasoning acting and planning in language models, 2024.\nAppendix ADatasets\n\nTable 4 outlines the detailed information of the datasets used for evaluation.\n\nDataset name\n \t\n# Features\n\t# Rows\t# Classes\tTask Type\tMetric\tSource\n\nboston\n \t\n14\n\t506\tN/A\tRegression\tRMSE\tOpenML (Dataset ID: 531)\n\ncolleges\n \t\n48\n\t7063\tN/A\tRegression\tRMSE\tOpenML (Dataset ID: 42727)\n\nconcrete-strength\n \t\n9\n\t4866\tN/A\tRegression\tRMSE\tKaggle (playground-series-s3e9)\n\ndiamonds\n \t\n10\n\t53940\tN/A\tRegression\tRMSE\tOpenML (Dataset ID: 42225)\n\nhouse-prices\n \t\n81\n\t1460\tN/A\tRegression\tRMSE\tKaggle (house-prices-advanced-regression-techniques)\n\nMoneyball\n \t\n15\n\t1232\tN/A\tRegression\tRMSE\tOpenML (Dataset ID: 41021)\n\nSAT11-HAND-runtime-regression\n \t\n118\n\t4440\tN/A\tRegression\tRMSE\tOpenML (Dataset ID: 41980)\n\ncredit-g\n \t\n21\n\t1000\t2\tClassification\tF1\tOpenML (Dataset ID: 31)\n\nClick_prediction_small\n \t\n12\n\t39948\t2\tClassification\tF1\tOpenML (Dataset ID: 42733)\n\nicr\n \t\n58\n\t617\t2\tClassification\tF1\tKaggle (icr-identify-age-related-conditions)\n\njasmine\n \t\n145\n\t2984\t2\tClassification\tF1\tOpenML (Dataset ID: 41143)\n\nkc1\n \t\n21\n\t2109\t2\tClassification\tF1\tOpenML (Dataset ID: 1067)\n\nkick\n \t\n33\n\t72983\t2\tClassification\tF1\tOpenML (Dataset ID: 41162)\n\nsmoker-status\n \t\n23\n\t143330\t2\tClassification\tF1\tKaggle (playground-series-s3e24)\n\nsoftware-defects\n \t\n22\n\t91586\t2\tClassification\tF1\tKaggle (playground-series-s3e23)\n\ntitanic\n \t\n12\n\t891\t2\tClassification\tF1\tKaggle (titanic)\n\nGesturePhaseSegmentationProcessed\n \t\n33\n\t9873\t5\tMulticlass\tF1-weighted\tOpenML (Dataset ID: 4538)\n\nmfeat-factors\n \t\n217\n\t2000\t10\tMulticlass\tF1-weighted\tOpenML (Dataset ID: 12)\n\nsegment\n \t\n20\n\t2310\t7\tMulticlass\tF1-weighted\tOpenML (Dataset ID: 40984)\n\nwine-quality-white\n \t\n12\n\t4898\t7\tMulticlass\tF1-weighted\tOpenML (Dataset ID: 40498)\nTable 4:Summary of the machine learning datasets used in the experiments. OpenML datasets can be accessed using their respective dataset IDs. The Kaggle datasets are available at https://www.kaggle.com/competitions/{source}.\nAppendix BPrompts\nB.1Task Prompt\n\nAll LLM-based methods start by receiving the same base requirement prompt at the beginning of the task. The prompt specifies the dataset’s name, the target label column, the evaluation metric to be used, and the dataset’s file path. Furthermore, the prompt include a path to a text file containing the dataset’s metadata.\n\n1TASK_PROMPT = \"\"\"\n2#␣User␣requirement\n3This␣is␣a␣{datasetname}␣dataset.\n4Your␣goal␣is␣to␣predict␣the␣target␣column␣‘{target_col}‘.\n5Perform␣data␣analysis,␣data␣preprocessing,␣feature␣engineering,␣and␣modeling␣to␣predict␣the␣target.␣Report␣{metric}␣on␣the␣eval␣data.␣Do␣not␣plot␣or␣make␣any␣visualizations.\n6\n7#␣Data␣dir\n8train␣set␣(with␣labels):␣{train_path}\n9dev␣set␣(with␣labels):␣{dev_path}\n10test␣set␣(without␣labels):␣{test_path}\n11dataset␣description:␣{data_info_path}\n12(During␣EDA,␣you␣can␣use␣this␣file\n13to␣get␣additional␣information␣about␣the␣dataset)\n14\"\"\"\n\nSince AIDE automatically splits the training data into a new train set and a validation set, we combine the original train and validation sets and provide them as input to AIDE. We set k_fold_validation to 1 in its configuration file to enforce a single train-val split for closer alignment with our setup. In both setups, the frameworks have access to the labels for both the train and validation sets.\n\nB.2Instruction Prompt\n\nThe instruction prompt would direct the framework to save the final prediction file for evaluation.\n\n1DI_INSTRUCTION = \"\"\"\n2##␣Attention\n31.␣Please␣do␣not␣leak␣the␣target␣label␣in␣any␣form␣during␣training.\n42.␣Test␣set␣does␣not␣have␣the␣target␣column.\n53.␣When␣conducting␣data␣exploration␣or␣analysis,␣print␣out␣the␣results␣of␣your␣findings.\n64.␣You␣should␣perform␣transformations␣on␣train,␣dev,␣and␣test␣sets␣at␣the␣same␣time␣(it’s␣a␣good␣idea␣to␣define␣functions␣for␣this␣and␣avoid␣code␣repetition).\n75.␣When␣scaling␣or␣transforming␣features,␣make␣sure␣the␣target␣column␣is␣not␣included.\n86.␣You␣could␣utilize␣dev␣set␣to␣validate␣and␣improve␣model␣training.␣{special_instruction}\n9\n10##␣Saving␣Dev␣and␣Test␣Predictions\n111.␣Save␣the␣prediction␣results␣of␣BOTH␣the␣dev␣set␣and␣test␣set␣in␣‘dev_predictions.csv‘␣and␣‘test_predictions.csv‘␣respectively␣in␣the␣output␣directory.\n12-␣Both␣files␣should␣contain␣a␣single␣column␣named␣‘target‘␣with␣the␣predicted␣values.\n132.␣Make␣sure␣the␣prediction␣results␣are␣in␣the␣same␣format␣as␣the␣target␣column␣in␣the␣training␣set.\n14-␣For␣instance,␣if␣the␣target␣column␣is␣categorical,␣the␣prediction␣results␣should␣be␣categorical␣as␣well.\n15\n16##␣Output␣Performance\n17Print␣the␣train␣and␣dev␣set␣performance␣in␣the␣last␣step.\n18\n19#␣Output␣dir\n20{output_dir}\n21\"\"\"\nB.3Insight Proposal Prompt\n\nInsight Proposer uses this prompt to generate a search space of insights for different stages of the machine learning task.\n\n1DATASET_INSIGHT_PROMPT = \"\"\"\n2#␣Dataset␣Description\n3{dataset}\n4\n5#␣Dataset␣Metadata\n6{metadata}\n7\n8#␣Dataset␣Head\n9{head}\n10\n11#␣Instruction\n12Propose␣insights␣to␣help␣improve␣the␣performance␣of␣the␣model␣on␣this␣dataset.\n13The␣insights␣should␣be␣proposed␣based␣on␣the␣dataset␣description␣with␣different␣task␣types.\n14Each␣task␣type␣should␣have␣at␣least␣5␣insights.\n15Make␣sure␣each␣method␣is␣diverse␣enough␣and␣can␣be␣implemented␣separately.\n16Be␣specific␣about␣models’␣choices,␣ensemble␣and␣tuning␣techniques,␣and␣preprocessing␣&␣feature␣engineering␣techniques.\n17\n18#␣Format\n19‘‘‘json\n20[\n21␣␣␣␣{{\n22␣␣␣␣␣␣␣␣\"task_type\":␣\"EDA\",\n23␣␣␣␣␣␣␣␣\"insights\":␣[\n24␣␣␣␣␣␣␣␣␣␣␣␣\"insight1\",\n25␣␣␣␣␣␣␣␣␣␣␣␣\"insight2\",\n26␣␣␣␣␣␣␣␣␣␣␣␣\"insight3\",\n27␣␣␣␣␣␣␣␣␣␣␣␣...\n28␣␣␣␣␣␣␣␣␣␣␣␣\"insightN\"\n29␣␣␣␣␣␣␣␣]\n30␣␣␣␣}},\n31␣␣␣␣{{\n32␣␣␣␣␣␣␣␣\"task_type\":␣\"Data Preprocessing\",\n33␣␣␣␣␣␣␣␣\"insights\":␣[\n34␣␣␣␣␣␣␣␣␣␣␣␣\"insight1\",\n35␣␣␣␣␣␣␣␣␣␣␣␣\"insight2\",\n36␣␣␣␣␣␣␣␣␣␣␣␣\"insight3\",\n37␣␣␣␣␣␣␣␣␣␣␣␣...\n38␣␣␣␣␣␣␣␣␣␣␣␣\"insightN\"\n39␣␣␣␣␣␣␣␣]\n40␣␣␣␣}},\n41␣␣␣␣{{\n42␣␣␣␣␣␣␣␣\"task_type\":␣\"Feature Engineering\",\n43␣␣␣␣␣␣␣␣\"insights\":␣[\n44␣␣␣␣␣␣␣␣␣␣␣␣\"insight1\",\n45␣␣␣␣␣␣␣␣␣␣␣␣\"insight2\",\n46␣␣␣␣␣␣␣␣␣␣␣␣\"insight3\",\n47␣␣␣␣␣␣␣␣␣␣␣␣...\n48␣␣␣␣␣␣␣␣␣␣␣␣\"insightN\"\n49␣␣␣␣␣␣␣␣]\n50␣␣␣␣}},\n51␣␣␣␣{{\n52␣␣␣␣␣␣␣␣\"task_type\":␣\"Model Training\",\n53␣␣␣␣␣␣␣␣\"insights\":␣[\n54␣␣␣␣␣␣␣␣␣␣␣␣\"insight1\",\n55␣␣␣␣␣␣␣␣␣␣␣␣\"insight2\",\n56␣␣␣␣␣␣␣␣␣␣␣␣\"insight3\",\n57␣␣␣␣␣␣␣␣␣␣␣␣...\n58␣␣␣␣␣␣␣␣␣␣␣␣\"insightN\"\n59␣␣␣␣␣␣␣␣]\n60␣␣␣␣}}\n61]\n62‘‘‘\n63\"\"\"\nAppendix CResults\nC.1Main Results\n\tAutoGluon\tAutoSklearn\tAIDE\tDI\t\\methodname\nDataset\tAvg.\tBest\tAvg.\tBest\tAvg.\tBest\tAvg.\tBest\tAvg.\tBest\nClick_prediction_small\t7\t7\t2\t1\t7.3\t4\t11\t10\t7.7\t6\nGesturePhaseSegmentationProcessed\t1\t1\t6.3\t3\t7.3\t4\t11\t10\t5.3\t2\nMoneyball\t4\t4\t10\t9\t4\t1\t9\t2\t6\t3\nSAT11-HAND-runtime-regression\t1\t1\t12\t11\t5.3\t3\t9\t8\t3.7\t2\nboston\t5\t5\t12\t11\t3.7\t2\t9\t8\t4\t1\ncolleges\t1\t1\t12\t11\t6\t2\t8\t7\t4\t3\nconcrete-strength\t5\t5\t12\t11\t6.3\t4\t2\t1\t8.3\t6\ncredit-g\t4\t4\t10\t9\t10\t5\t5.3\t1\t3.7\t2\ndiamonds\t2\t2\t12\t11\t6\t4\t8.7\t7\t3\t1\nhouse-prices\t1\t1\t12\t11\t6.7\t5\t7.3\t3\t4\t2\nicr\t5\t5\t5.3\t3\t12\t11\t9\t8\t2.3\t1\njasmine\t7\t7\t6\t4\t8.7\t5\t11.3\t9\t2\t1\nkc1\t10\t10\t2.7\t1\t8\t5\t11.3\t9\t5\t2\nkick\t4\t4\t2\t1\t9.3\t6\t11\t10\t6.7\t5\nmfeat-factors\t4\t4\t2\t1\t10\t9\t10.3\t6\t6.7\t5\nsegment\t3\t3\t6.3\t5\t11\t10\t9.7\t7\t2.3\t1\nsmoker-status\t7\t7\t4.7\t3\t11.3\t9\t7.7\t2\t4.3\t1\nsoftware-defects\t8\t8\t2\t1\t12\t11\t6\t4\t7.7\t6\ntitanic\t7\t7\t9.7\t6\t2.7\t1\t10.3\t8\t5.3\t3\nwine-quality-white\t2\t2\t10\t8\t7.3\t4\t9\t7\t3.3\t1\nOverall Rank \n↓\n \t4.4\t4.4\t7.6\t6.1\t7.8\t5.3\t8.8\t6.4\t4.8\t2.7\nTable 5:Methods’ ranking for each tabular dataset\n\tAutoGluon\tAutoSklearn\tAIDE\tDI\t\\methodname\nDataset\tAvg.\tBest\tAvg.\tBest\tAvg.\tBest\tAvg.\tBest\tAvg.\tBest\nClick_prediction_small\t26.6\t26.6\t40.2\t40.3\t26.1\t39.4\t12.9\t13.9\t23.2\t27.4\nGesturePhaseSegmentationProcessed\t69.3\t69.3\t67.2\t68.4\t56.3\t68.1\t60.1\t64.4\t67.9\t69.2\nMoneyball\t24.3\t24.3\t13.1\t13.8\t23.8\t24.6\t9.5\t24.5\t21.9\t24.5\nSAT11-HAND-runtime-regression\t12.6\t12.6\t10.3\t10.3\t12.0\t12.1\t11.4\t11.9\t12.2\t12.5\nboston\t39.8\t39.8\t19.5\t19.6\t40.5\t41.3\t37.0\t38.6\t40.1\t41.4\ncolleges\t88.3\t88.3\t2.1\t2.1\t86.0\t87.8\t87.5\t87.7\t87.8\t87.8\nconcrete-strength\t28.3\t28.3\t17.4\t17.9\t28.3\t28.3\t28.8\t29.6\t28.2\t28.2\ncredit-g\t50.5\t50.5\t35.1\t44.0\t21.6\t48.4\t48.1\t53.2\t50.9\t52.7\ndiamonds\t13.8\t13.8\t8.7\t8.7\t13.7\t13.7\t13.5\t13.6\t13.7\t13.8\nhouse-prices\t9.0\t9.0\t2.0\t2.0\t8.9\t8.9\t8.5\t9.0\t8.9\t9.0\nicr\t76.2\t76.2\t70.4\t79.2\t31.7\t35.9\t57.8\t60.6\t78.7\t79.2\njasmine\t84.3\t84.3\t84.4\t84.7\t83.6\t84.6\t77.8\t83.5\t85.4\t86.2\nkc1\t38.3\t38.3\t43.5\t45.0\t40.8\t42.6\t38.1\t41.2\t42.2\t43.1\nkick\t39.6\t39.6\t41.8\t42.1\t14.9\t38.6\t2.8\t4.2\t35.9\t38.7\nmfeat-factors\t96.7\t96.7\t97.1\t97.5\t94.4\t94.5\t93.0\t96.0\t95.7\t96.2\nsegment\t93.5\t93.5\t92.7\t93.1\t91.7\t92.2\t91.7\t92.6\t93.8\t94.4\nsmoker-status\t78.0\t78.0\t78.6\t78.9\t74.8\t76.3\t77.3\t81.5\t82.4\t91.5\nsoftware-defects\t51.5\t51.5\t61.1\t61.7\t49.7\t49.8\t54.5\t57.3\t52.2\t53.3\ntitanic\t78.9\t78.9\t76.2\t78.9\t81.2\t83.7\t76.0\t78.5\t78.8\t79.7\nwine-quality-white\t65.4\t65.4\t60.7\t61.4\t62.9\t65.1\t61.2\t61.6\t65.3\t66.0\nOverall NS % \n↑\n \t53.2\t53.2\t46.1\t47.5\t45.5\t51.8\t47.4\t50.2\t53.3\t54.7\nTable 6:Methods’ NS % for each tabular dataset\nC.2Performance using different LLMs\n\tGPT-4o\tClaude 3.5 Sonnet\tDeepSeek V2.5\nAvg. NS \n↑\n \t62.3\t57.9\t60.9\nAvg. Best NS \n↑\n \t65.5\t59.2\t62.4\nAvg. Rank \n↓\n \t3.7\t6.3\t5.0\nAvg. Best Rank \n↓\n \t1.5\t4.8\t3.2\nTable 7:Results of \\methodname with different base LLMs on the selected tabular datasets.\nAppendix DCost-effectiveness Analysis\n\nWe conduct multiple trials of execution of each method to estimate the average running cost for the LLM-based baselines. As shown in Table 8, all methods incur relatively low costs to complete a single machine learning task. Among these, AIDE exhibits the lowest execution cost, due to the lack of stage-wise planning, resulting in fewer token generations compared to the other approaches. Additionally, \\methodname, which employs Data Interpreter as its base experimenter, is less costly than Data Interpreter itself. This efficiency is largely due to \\methodname’s state-saving and loading mechanism, which reduces the generation of repeated tasks and code.\n\n\tCost per ML task ($)\t\t\nData Interpreter (\n𝑘\n=10)\t0.07\t\t\nAIDE (\n𝑘\n=10)\t0.01\t\t\n\\methodname (\n𝑘\n=10)\t0.05\t\t\nTable 8:Estimated costs of agent-based frameworks utilizing DeepSeekV2.5 on a single machine learning dataset over \n𝑘\n iterations/rollouts.\nAppendix ECase Study\nE.1Overview of SELA’s search process\n1Number of simulations: 10\n2[Node 0]\n3Plans:\n41. Perform exploratory data analysis on the train and dev datasets\n52. Preprocess the train, dev, and test datasets\n63. Perform feature engineering on the train, dev, and test datasets\n74. Train multiple models and evaluate their performance\n85. Train a weighted ensemble model using the best performing models\n96. Evaluate the ensemble model on the dev set and save predictions\n107. Generate predictions for the test set and save them\n11Simulated: True\n12Score: avg score: 0.6150206840685731, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6855841857240594, ’test_score’: 0.6814818772150697, ’score’: 0.6855841857240594}, Visits: 10\n13\n14 [Node 0-0]\n15 Plans:\n16 3. Perform feature engineering on the train, dev, and test datasets by creating new features that calculate the magnitude of the vectorial velocities and accelerations to capture the overall movement intensity.\n17 Simulated: True\n18 Score: avg score: 0.6507249985568175, simulated score: {’train_score’: 0.982920964830782, ’dev_score’: 0.6420233166755841, ’test_score’: 0.647550336228104, ’score’: 0.6420233166755841}, Visits: 2\n19\n20 [Node 0-0-0]\n21 Plans:\n22 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships, and evaluate its performance\n23 Simulated: False\n24 Score: avg score: 0, simulated score: {}, Visits: 0\n25\n26 [Node 0-0-1]\n27 Plans:\n28 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance.\n29 Simulated: False\n30 Score: avg score: 0, simulated score: {}, Visits: 0\n31\n32 [Node 0-0-2]\n33 Plans:\n34 4. Implement a Neural Network with multiple layers to capture the hierarchical patterns in the data and evaluate its performance\n35 Simulated: True\n36 Score: avg score: 0.6594266804380511, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6594266804380511, ’test_score’: 0.6702614538699305, ’score’: 0.6594266804380511}, Visits: 1\n37\n38 [Node 0-0-3]\n39 Plans:\n40 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance\n41 Simulated: False\n42 Score: avg score: 0, simulated score: {}, Visits: 0\n43\n44 [Node 0-0-4]\n45 Plans:\n46 4. Train multiple models, perform hyperparameter tuning using Grid Search or Random Search, and evaluate their performance\n47 Simulated: False\n48 Score: avg score: 0, simulated score: {}, Visits: 0\n49\n50 [Node 0-1]\n51 Plans:\n52 3. Perform feature engineering on the train, dev, and test datasets by generating time-based features, such as the difference between consecutive frames, to capture the rate of change in movements.\n53 Simulated: True\n54 Score: avg score: 0.6464940718972336, simulated score: {’train_score’: 1.0, ’dev_score’: 0.5985614604756948, ’test_score’: 0.5857379626419719, ’score’: 0.5985614604756948}, Visits: 2\n55\n56 [Node 0-1-0]\n57 Plans:\n58 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships\n59 Simulated: False\n60 Score: avg score: 0, simulated score: {}, Visits: 0\n61\n62 [Node 0-1-1]\n63 Plans:\n64 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance to model the complex decision boundaries between different gesture phases.\n65 Simulated: True\n66 Score: avg score: 0.6944266833187726, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6944266833187726, ’test_score’: 0.6928451194338062, ’score’: 0.6944266833187726}, Visits: 1\n67\n68 [Node 0-1-2]\n69 Plans:\n70 4. Implement a Neural Network with multiple layers to capture the hierarchical patterns in the data and evaluate its performance\n71 Simulated: False\n72 Score: avg score: 0, simulated score: {}, Visits: 0\n73\n74 [Node 0-1-3]\n75 Plans:\n76 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance\n77 Simulated: False\n78 Score: avg score: 0, simulated score: {}, Visits: 0\n79\n80 [Node 0-1-4]\n81 Plans:\n82 4. Train multiple models and perform hyperparameter tuning using techniques like Grid Search or Random Search to optimize and evaluate their performance.\n83 Simulated: False\n84 Score: avg score: 0, simulated score: {}, Visits: 0\n85\n86 [Node 0-2]\n87 Plans:\n88 3. Perform feature engineering on the train, dev, and test datasets by creating features that represent the spatial relationships between different body parts, such as the distance between the hands and the head.\n89 Simulated: True\n90 Score: avg score: 0.6296836159165489, simulated score: {’train_score’: 0.7619969104124632, ’dev_score’: 0.5997286931710517, ’test_score’: 0.604077566134264, ’score’: 0.5997286931710517}, Visits: 3\n91\n92 [Node 0-2-0]\n93 Plans:\n94 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships, and evaluate its performance\n95 Simulated: False\n96 Score: avg score: 0, simulated score: {}, Visits: 0\n97\n98 [Node 0-2-1]\n99 Plans:\n100 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance to model the complex decision boundaries between different gesture phases.\n101 Simulated: True\n102 Score: avg score: 0.6446610772892973, simulated score: {’train_score’: 0.9952809245924918, ’dev_score’: 0.6372459669415207, ’test_score’: 0.6423549137767338, ’score’: 0.6372459669415207}, Visits: 2\n103\n104 [Node 0-2-1-0]\n105 Plans:\n106 5. Train a weighted ensemble model using the best performing models from task 4\n107 Simulated: False\n108 Score: avg score: 0, simulated score: {}, Visits: 0\n109\n110 [Node 0-2-1-1]\n111 Plans:\n112 5. Using the models that performed best in task 4, train a weighted ensemble model to improve overall performance.\n113 Simulated: False\n114 Score: avg score: 0, simulated score: {}, Visits: 0\n115\n116 [Node 0-2-1-2]\n117 Plans:\n118 5. Develop a weighted ensemble model by integrating the top-performing models from task 4, ensuring to evaluate and adjust the weights for optimal performance.\n119 Simulated: True\n120 Score: avg score: 0.6520761876370741, simulated score: {’train_score’: 1.0, ’dev_score’: 0.6520761876370741, ’test_score’: 0.6563435152603494, ’score’: 0.6520761876370741}, Visits: 1\n121\n122 [Node 0-2-1-3]\n123 Plans:\n124 5. Train a weighted ensemble model by combining the predictions of the top-performing models from task 4 to improve overall performance.\n125 Simulated: False\n126 Score: avg score: 0, simulated score: {}, Visits: 0\n127\n128 [Node 0-2-1-4]\n129 Plans:\n130 5. Develop a weighted ensemble model by combining the top-performing models from task 4, ensuring to optimize the weights for improved performance.\n131 Simulated: False\n132 Score: avg score: 0, simulated score: {}, Visits: 0\n133\n134 [Node 0-2-2]\n135 Plans:\n136 4. Implement a Neural Network with multiple layers to capture the hierarchical patterns in the data and evaluate its performance\n137 Simulated: False\n138 Score: avg score: 0, simulated score: {}, Visits: 0\n139\n140 [Node 0-2-3]\n141 Plans:\n142 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance\n143 Simulated: False\n144 Score: avg score: 0, simulated score: {}, Visits: 0\n145\n146 [Node 0-2-4]\n147 Plans:\n148 4. Perform hyperparameter tuning using Grid Search or Random Search to train multiple models and evaluate their performance\n149 Simulated: False\n150 Score: avg score: 0, simulated score: {}, Visits: 0\n151\n152 [Node 0-3]\n153 Plans:\n154 3. Apply feature selection techniques such as Recursive Feature Elimination (RFE) or SelectKBest to identify and retain the most important features in the train, dev, and test datasets.\n155 Simulated: True\n156 Score: avg score: 0.49056683315196203, simulated score: {’train_score’: 0.9988177730410426, ’dev_score’: 0.51620611302976, ’test_score’: 0.525989891002361, ’score’: 0.51620611302976}, Visits: 2\n157\n158 [Node 0-3-0]\n159 Plans:\n160 4. Train a Random Forest classifier to leverage its ability to handle high-dimensional data and capture non-linear relationships, and evaluate its performance.\n161 Simulated: False\n162 Score: avg score: 0, simulated score: {}, Visits: 0\n163\n164 [Node 0-3-1]\n165 Plans:\n166 4. Train multiple models, including a Support Vector Machine (SVM) with a radial basis function (RBF) kernel, and evaluate their performance to model the complex decision boundaries between different gesture phases.\n167 Simulated: True\n168 Score: avg score: 0.4649275532741641, simulated score: {’train_score’: 0.7299159411193588, ’dev_score’: 0.4649275532741641, ’test_score’: 0.4631598897487413, ’score’: 0.4649275532741641}, Visits: 1\n169\n170 [Node 0-3-2]\n171 Plans:\n172 4. Implement and train a Neural Network with multiple layers to capture hierarchical patterns in the data and evaluate its performance\n173 Simulated: False\n174 Score: avg score: 0, simulated score: {}, Visits: 0\n175\n176 [Node 0-3-3]\n177 Plans:\n178 4. Train multiple models, apply an ensemble method like Gradient Boosting to combine them, and evaluate their performance\n179 Simulated: False\n180 Score: avg score: 0, simulated score: {}, Visits: 0\n181\n182 [Node 0-3-4]\n183 Plans:\n184 4. Train multiple models, perform hyperparameter tuning using techniques like Grid Search or Random Search, and evaluate their performance\n185 Simulated: False\n186 Score: avg score: 0, simulated score: {}, Visits: 0\n187\n188 [Node 0-4]\n189 Plans:\n190 3. Create interaction features by combining existing features, such as the product of velocity and acceleration, to capture complex relationships in the train, dev, and test datasets\n191 Simulated: False\n192 Score: avg score: 0, simulated score: {}, Visits: 0\n193\n194Generated 29 unique codes.\n195Best node: 0-1-1, score: {’train_score’: 1.0, ’dev_score’: 0.6944266833187726, ’test_score’: 0.6928451194338062, ’score’: 0.6944266833187726}\n196Dev best node: 0-1-1, score: {’train_score’: 1.0, ’dev_score’: 0.6944266833187726, ’test_score’: 0.6928451194338062, ’score’: 0.6944266833187726}\n\nIn this case study, we demonstrate how SELA conducts a search cycle using MCTS:\n\nPre-search Step: Initialization\nSELA begins by defining high-level stages, such as exploratory data analysis, data preprocessing, feature engineering, and model training, which structure the overall machine learning workflow. During the search, SELA populates these stages with specific insights, which act as experimental configurations for simulation.\n\nStep 1 & 2: Selection and Expansion\nSELA leverages MCTS to explore specific stages like feature engineering and model training. For example, in one iteration, SELA selects Node 0-1. This node corresponds to a stage insight that generates time-based features, expanding into five child nodes representing various model specifications and training strategies, such as Random Forests, Support Vector Machines, Neural Networks, Gradient Boosting, or Grid Search.\n\nStep 3: Simulation\nNext, SELA samples one of the expanded child nodes for simulation. For instance, when Node 0-1-1 is chosen, SELA runs a complete experiment where time-based feature engineering (Node 0-1) is followed by training a Support Vector Machine (SVM) with a kernel specified by Node 0-1-1. The simulation yields an evaluation score.\n\nStep 4: Backpropagation\nAfter the simulation, the resulting performance score is propagated back through the tree. For example, after simulating Node 0-1-1, MCTS updates the numeric feedback for its parent nodes, such as Node 0-1 and Node 0. The search cycle repeats from Steps 1 to 4 until a stopping condition is reached.\n\nPost-search Step: Best Node Selection\nIn the final phase, SELA selects the node representing the best-performing solution. In this example, Node 0-1-1, using an SVM with an RBF kernel, achieved the highest score in the current dataset by combining effective feature engineering with advanced model training. SELA then presents the code associated with this node as the optimal solution.\n\nGenerated on Tue Oct 22 15:11:58 2024 by LaTeXML",
  "usage": {
    "tokens": 20243
  }
}
```
