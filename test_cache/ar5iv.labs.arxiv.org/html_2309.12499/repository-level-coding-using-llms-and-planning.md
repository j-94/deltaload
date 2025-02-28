---
title: 𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇: Repository-level Coding using LLMs and Planning
description: 
url: https://ar5iv.labs.arxiv.org/html/2309.12499#:~:text=Our%20results%20show%20that%20%F0%9D%96%A2%F0%9D%97%88%F0%9D%96%BD%F0%9D%96%BE%F0%9D%96%AF%F0%9D%97%85%F0%9D%96%BA%F0%9D%97%87%20%F0%9D%96%A2%F0%9D%97%88%F0%9D%96%BD%F0%9D%96%BE%F0%9D%96%AF%F0%9D%97%85%F0%9D%96%BA%F0%9D%97%87%20%5Cmathsf%7BCodePlan%7D%20sansserif_CodePlan%20has%20better%20match%20with%20the%20ground%20truth%20compared%20to%20baselines
timestamp: 2025-01-20T15:59:30.775Z
domain: ar5iv.labs.arxiv.org
path: html_2309.12499
---

# 𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇: Repository-level Coding using LLMs and Planning



## Content

𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
: Repository-level Coding using LLMs and Planning
Ramakrishna Bairi
rbairi@microsoft.com
Microsoft ResearchIndia
Atharv Sonwane
t-asonwane@microsoft.com
Microsoft ResearchIndia
Aditya Kanade
kanadeaditya@microsoft.com
Microsoft ResearchIndia
Vageesh D C
vachand@microsoft.com
Microsoft ResearchIndia
Arun Iyer
ariy@microsoft.com
Microsoft ResearchIndia
Suresh Parthasarathy
supartha@microsoft.com
Microsoft ResearchIndia
Sriram Rajamani
sriram@microsoft.com
Microsoft ResearchIndia
B. Ashok
bash@microsoft.com
Microsoft ResearchIndia
Shashank Shet
t-sshet@microsoft.com
Microsoft ResearchIndia
(2018; 2024)
Abstract.

Software engineering activities such as package migration, fixing errors reports from static analysis or testing, and adding type annotations or other specifications to a codebase, involve pervasively editing the entire repository of code. We formulate these activities as repository-level coding tasks.

Recent tools like GitHub Copilot, which are powered by Large Language Models (LLMs), have succeeded in offering high-quality solutions to localized coding problems. Repository-level coding tasks are more involved and cannot be solved directly using LLMs, since code within a repository is inter-dependent and the entire repository may be too large to fit into the prompt. We frame repository-level coding as a planning problem and present a task-agnostic framework, called 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 to solve it. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 synthesizes a multi-step chain of edits (plan), where each step results in a call to an LLM on a code location with context derived from the entire repository, previous code changes and task-specific instructions. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 is based on a novel combination of an incremental dependency analysis, a change may-impact analysis and an adaptive planning algorithm.

We evaluate the effectiveness of 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 on two repository-level tasks: package migration (C#) and temporal code edits (Python). Each task is evaluated on multiple code repositories, each of which requires inter-dependent changes to many files (between 2–97 files). Coding tasks of this level of complexity have not been automated using LLMs before. Our results show that 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 has better match with the ground truth compared to baselines. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 is able to get 5/6 repositories to pass the validity checks (e.g., to build without errors and make correct code edits) whereas the baselines (without planning but with the same type of contextual information as 
����𝗈𝖽𝖾𝖯𝗅𝖺𝗇
) cannot get any of the repositories to pass them. We will release our data and evaluation scripts at https://aka.ms/CodePlan.

Automated coding, repositories, LLMs, static analysis, plan, chain of edits
†copyright: acmcopyright
†journalyear: 2018
†doi: XXXXXXX.XXXXXXX
†conference: Make sure to enter the correct conference title from your rights confirmation emai; June 03–05, 2018; Woodstock, NY
†price: 15.00
†isbn: 978-1-4503-XXXX-X/18/06
†copyright: acmcopyright
†journalyear: 2024
†doi: XXXXXXX.XXXXXXX
†price: 15.00
†isbn: 978-1-4503-XXXX-X/18/06
†ccs: Computing methodologies Planning under uncertainty
†ccs: Software and its engineering Software maintenance tools
†ccs: Software and its engineering Software evolution
†ccs: Software and its engineering Automatic programming
1.Introduction

We use a Complex Numbers library that had the following edit -

+ class Complex {
+   float real;
+   float imag;
+   dict<string, string> metadata;
+ }
- tuple<float, float> create_complex(float a, float b)
+ Complex create_complex(float a, float b, dict metadata)

Modify the code repository in accordance with this change.

Figure 1.Task instruction to migrate a code repository due to an API change in the Complex Numbers library.
Figure 2.Overview of 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
.

The remarkable generative abilities of Large Language Models (LLMs) (Brown et al., 2020; Chen et al., 2021; Chowdhery et al., 2022; Fried et al., 2022; OpenAI, 2023; Touvron et al., 2023) have opened new ways to automate coding tasks. Tools built on LLMs, such as Amazon Code Whisperer (Amazon Web Services, Inc., 2023), GitHub Copilot (Github, Inc., 2023) and Replit (Replit, Inc., 2023), are now widely used to complete code

given a natural language intent and context of surrounding code, and also to perform code edits based on natural language instructions (Wilson-Thomas, [n. d.]). Such edits are typically done for small regions of code such as completing or editing the current line, or the body of the entire method.

While these tools help with the ”inner loop” of software engineering where the developer is coding in the editor and editing a small region of code, there are several tasks in the ”outer loop” of software engineering that involve the entire code repository. For example, if our code repository uses a library 
𝐿
, and the API of library 
𝐿
 changes from version 
𝑣
𝑛
 to version 
𝑣
𝑛
+
1
, we need to migrate our code repository to correctly invoke the revised version. Such a migration task involves making edits not only to all the regions of repository that make calls to the relevant APIs in library 
𝐿
, but also to regions of the repository (across file boundaries) having transitive syntactic and semantic dependencies on the updated code.

tuple<tuple<float, float>, dict> func(float a, float b) {
  string timestamp = GetTimestamp(DateTime.Now);
   var c = (create_complex(a,b), new Dictionary<string, string>()"time", timestamp);
  return c;
}
 	
Complex func(float a, float b) {
  String timestamp = GetTimestamp(DataTime.Now);
  dict_metadata = new Dictionary<string, string>(){"time", timestamp};
  Complex c = create_complex(a, b, metadata);
  return c;
}

(a) Create.cs - Original	(b) Create.cs - Modified (seed edit)

void process(float a, float b, float k) {
  var c = func(a, b);
  Console.WriteLine(c[0][0], c[0][1]);
  float norm = compute_norm(c[0][0], c[0][1]);
  Console.WriteLine(norm * k);
}
 	
void process(float a, float b, float k) {
  Complex c = func(a, b);
  Console.WriteLine(c.real, c.imag);
  float norm = compute_norm(c.real, c.imag);
  Console.WriteLine(norm * k);
}

(c) Process.cs - Original	(d) Process.cs - Modified (derived edit)
Figure 3.Relevant code snippets from our repository.

This is illustrated in Figure 2, which shows a change in the API for a Complex Numbers library. Our task is to migrate our code repository in accordance with this change. The left side of Figure 3 shows relevant parts of our code repository that use the Complex Numbers library. Specifically, the file Create.cs has the method func, which invokes the create_complex method from the library, and Process.cs has the method process which invokes func.

We can pass the task description from Figure 2 and the body of func to an LLM to generate the revised code for func as shown in the right side of Figure 3. As seen, the LLM has correctly edited the invocation to the create_complex API so that it returns an object of type Complex instead of a tuple of two floating point values. Note that this edit has resulted in a change to the signature of the method func – it now returns an object of type Complex. This necessitates changes to callers of method func such as the process method in file Process.cs, shown in the left-bottom of Figure 3. Without a suitable change to the body of the process method, our code does not build! A suitable change to the process method which gets the repository to a consistent state, so that it builds without errors, is shown in the bottom-right of Figure 3.

Problem Formulation. The migration task above is representative of a family of tasks that involve editing an entire code repository for various purposes such as fixing error reports from static analysis or testing, fixing a buggy coding pattern, refactoring, or adding type annotations or other specifications. Each of these tasks involves a set of seed specifications such as the one shown in Figure 2, which are starting points for the code editing task. These seed specifications typically trigger other editing requirements on code, and such requirements need to be propagated across dependencies in the code repository to perform other edits across the repository to complete the coding task. Typically, such propagation of edits across dependencies is done manually.

Our goal is to construct a repository-level coding system, which automatically generates derived specifications for edits such as one required for the process method in Figure 3, in order to get the repository to a valid state. Here, validity is defined with respect to an oracle, which can be instantiated to various ways of enforcing repository-level correctness conditions such as building without errors, passing static analysis, passing a type system or a set of tests, or passing a verification tool. We define an LLM-driven repository-level coding task as follows:

LLM-driven Repository-level Coding Task
Given a start state of a repository 
𝑅
𝑠
​
𝑡
​
𝑎
​
𝑟
​
𝑡
, a set of seed edit specifications 
Δ
𝑠
​
𝑒
​
𝑒
​
𝑑
​
𝑠
, an oracle 
Θ
 such that 
Θ
​
(
𝑅
𝑠
​
𝑡
​
𝑎
​
𝑟
​
𝑡
)
=
𝖳𝗋𝗎𝖾
, and an LLM 
𝐿
, the goal of an LLM-driven repository-level coding task is to reach a repository state 
𝑅
𝑡
​
𝑎
​
𝑟
​
𝑔
​
𝑒
​
𝑡
=
𝐸
​
𝑥
​
𝑒
​
𝑐
​
𝑢
​
𝑡
​
𝑒
​
𝐸
​
𝑑
​
𝑖
​
𝑡
​
𝑠
​
(
𝐿
,
𝑅
𝑠
​
𝑡
​
𝑎
​
𝑟
​
𝑡
,
𝑃
)
 where 
𝑃
 is a chain of edit specifications from 
Δ
𝑠
​
𝑒
​
𝑒
​
𝑑
​
𝑠
∪
Δ
𝑑
​
𝑒
​
𝑟
​
𝑖
​
𝑣
​
𝑒
​
𝑑
 where 
Δ
𝑑
​
𝑒
​
𝑟
​
𝑖
​
𝑣
​
𝑒
​
𝑑
 is a set of derived edit specifications so that 
Θ
​
(
𝑅
𝑡
​
𝑎
​
𝑟
​
𝑔
​
𝑒
​
𝑡
)
=
𝖳𝗋𝗎𝖾
.

Proposed Solution. In this paper, we propose a method to compute derived specifications by framing (LLM-driven) repository-level coding as a planning problem. Automated planning (Ghallab et al., 2004; Russell, 2010) aims to solve multi-step problems, where each step executes one action among many alternatives towards reaching a target state. It is used in a wide range of areas such as motion planning (La Valle, 2011), autonomous driving (González et al., 2015), robotics (Karpas and Magazzeni, 2020) and theorem proving (Bundy, 1988).

We present a task-agnostic framework, called 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
, which synthesizes a multi-step plan to solve the repository-level coding task. As shown in Figure 2, the input to 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 is a repository, a task with seed specifications expressed through a natural language instruction or a set of initial code edits, a correctness oracle and an LLM. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 constructs a plan graph where each node in the graph identifies a code edit obligation that the LLM needs to discharge and an edge indicates that the target node needs to be discharged consequent to the source node. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 monitors the code edits and adaptively extends the plan graph. The edits 
Δ
𝑠
​
𝑒
​
𝑒
​
𝑑
​
𝑠
 follow from the task description, whereas the edits 
Δ
𝑑
​
𝑒
​
𝑟
​
𝑖
​
𝑣
​
𝑒
​
𝑑
 are identified and contextualized based on a novel combination of an incremental dependency analysis, a change may-impact analysis and an adaptive planning algorithm. The merge block merges the code generated by the LLM into the repository. Once all the steps in a plan are completed, the repository is analyzed by the oracle. The task is completed if the oracle validates the repository. If it finds errors, the error reports are used as seed specifications for the next round of plan generation and execution.

Consider again, the example API migration task specified in Figure 2 on code in Figure 3. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 performs the edit of the method func using the instruction in Figure 2 as a seed specification. By analyzing the code change between Figure 3(a)–(b), it classifies the change as an escaping change as it affects signature of method func. The change may-impact analysis identifies that the caller(s) of func may be affected and hence, the adaptive planning algorithm uses caller-callee dependencies to infer a derived specification to edit the method process, which invokes func. Both the seed and derived changes are executed by creating suitable prompts for an LLM and the resulting code repository passes the oracle, i.e., builds without errors. Note that this is a simple example with only one-hop change propagation. In practice, the derived changes can themselves necessitate other changes transitively and 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 handles such cases.

A simpler alternative to our planning is to use the oracle to infer derived specifications. For example, the build system can find the error in the process method after the seed change is made in Figure 3. This has important limitations. First, not all changes induce build errors even though they result in behavioral changes, e.g., changing the return value from True to False without changing the return type. Second, the build system is agnostic to cause-effect relationship when code breaks. For example, if the signature of an overriding method is changed as per the seed specification then a similar change is needed in the corresponding virtual method. However, the build system (when run on the intermediate, inconsistent snapshot of the repository) blames the overriding method for not conforming to the virtual method. Naïvely trying to fix the build error would end up reverting the seed change. The static analysis and planning components of 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 overcome these limitations. We experimentally compare 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 against a baseline that uses a build system to iteratively identify breaking changes and uses an LLM to fix them. Our quantitative and qualitative results show that 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 is superior to this kind of oracle-guided repair technique.

Contributions. To the best of our knowledge, the problem of monitoring the effects of code edits made by an LLM to a repository and systematically planning a chain of inter-dependent edits has not been identified and solved before.

In the space of repository-level coding tasks, two types of contexts have been found to be useful for prompting LLMs: (1) spatial context to provide cross-file information to the model using static analysis (Pashakhanloo et al., 2022; Shrivastava et al., 2022; Ding et al., 2022; Wei et al., 2023b; Pei et al., 2023b; Agrawal et al., 2023; Shrivastava et al., 2023; Liu et al., 2023) or retrieval (Xu et al., 2021; Zhang et al., 2023b), and (2) temporal context to condition the predictions on the history of edits to the repository (Brody et al., 2020; Reid and Neubig, 2022; Gupta et al., 2023; Wei et al., 2023a). Since 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 monitors the code changes and maintains a repository-wide dependency graph, we provide both these forms of contexts in a unified framework. The existing techniques assume that the next edit location is provided by the developer and do not account for the effect of an edit on the dependent code. In contrast, by inferring the impact of each change, 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 propagates the changes to dependent code, paving a way to automate repository-level coding tasks through chain of edits.

In summary, we make the following contributions in this paper:

(1) 

We are the first to formalize the problem of automating repository-level coding tasks using LLMs, which requires analyzing the effects of code changes and propagating them across the repository. There are currently no systematic and scalable solutions to this problem.

(2) 

We frame repository-level coding as a planning problem and design a task-agnostic framework, called 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
, based on a novel combination of an incremental dependency analysis, a change may-impact analysis and an adaptive planning algorithm. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 synthesizes a multi-step chain of edits (plan) to be actuated by an LLM.

(3) 

We experiment with two repository-level coding tasks using the gpt-4-32k model: package migration for C# repositories and temporal code edits for Python repositories. We compare against baselines that use the oracles (a build system for C# and a static type checker for Python) for identifying derived edit specifications (in contrast to planning used in 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
). We use the same contextualization method as 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 in the baselines.

(4) 

Our results show that 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 has better match with the ground truth compared to baselines. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 is able to get 5/6 repositories to pass the validity checks, whereas the baselines cannot get any of the repositories to pass them. Except for the 2 proprietary repositories, we will release our data and evaluation scripts at https://aka.ms/CodePlan.

2.Design

In this section, we first give an overview of the 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 algorithm for automating repository-level coding tasks (Section 2.1). We then present the static analysis (Section 2.2) and the adaptive planning and plan execution (Section 2.3) components of 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
.

2.1.The 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 Algorithm
1/* Inputs: R is the source code of a repository, Delta_seeds is a set of seed edit specifications, Theta is an oracle and L is an LLM. */
3CodePlan(R, Delta_seeds, Theta, L):
4  let mutable G: PlanGraph = null in  
5  let mutable D: DependencyGraph = ConstructDependencyGraph(R) in 
6    while Delta_seeds is not empty 
7      IntializePlanGraph(G, Delta_seeds) 
8      AdaptivePlanAndExecute(R, D, G) 
9      Delta_seeds = Theta(R) 
11InitializePlanGraph(G, Delta_seeds): 
12  for each 
⟨
B, I
⟩
 in Delta_seeds
13    AddRoot(G, 
⟨
B, I, Pending
⟩
) 
15AdaptivePlanAndExecute(R, D, G): 
16  while G has Nodes with Pending status
17    let 
⟨
B, I, Pending
⟩
 = GetNextPending(G) in
18    // First step: extract fragment of code
19    let Fragmemt = ExtractCodeFragment(B, R, I) in 
20    // Second step: gather context of the edit
21    let Context = GatherContext(B, R, D) in  
22    // Third step: use the LLM to get edited code fragment
23    let Prompt = MakePrompt(Fragment, I, Context) in 
24    let NewFragment = InvokeLLM(L, Prompt) in 
25    // Fourth step: merge the updated code fragment into R
26    let R = Merge(NewFragment, B, R) in 
27    let Labels = ClassifyChanges(Fragment, NewFragment) in 
28    let D’ = UpdateDependencyGraph​(D, Labels, Fragment, NewFragment, B) in 
29    // Fifth step: adaptively plan and propogate the effect of the edit on dependant code
30    let BlockRelationPairs ​​​=​​ GetAffectedBlocks(Labels, B, D, D’) in 
31      MarkCompleted(B, G) 
32      for each 
⟨
B’, rel
⟩
 in BlockRelationPairs
33        let N = GetNode(B) in
34        let M = SelectOrAddNode(B’, Nil, Pending) in 
35          AddEdge(G, M, N, rel) 
36    D := D’
38GatherContext(B, R, D): 
39  let SC = GetSpatialContext(B, R) in
40  let TC = GetTemporalContext(G, B) in
41    (SC, TC) 
Algorithm 1 The 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 algorithm to automate repository-level coding tasks. The data structures and functions in Cyan and Orchid are explained in Section 2.2– 2.3 respectively.

The 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 algorithm (Algorithm 1) takes four inputs: (1) the source code of a repository 
𝑅
, (2) a set of seed edit specifications for the task in hand, 
Δ
𝑠
​
𝑒
​
𝑒
​
𝑑
​
𝑠
, (3) an oracle, 
Θ
, and (4) an LLM, 
𝐿
.

The core data structure maintained by the algorithm is a plan graph 
𝐺
, a directed acyclic graph with multiple root nodes (line 4). Each node in the plan graph is a tuple 
⟨
𝐵
,
𝐼
,
𝑆
​
𝑡
​
𝑎
​
𝑡
​
𝑢
​
𝑠
⟩
, where 
𝐵
 is a block of code (that is, a sequence of code locations) in the repository 
𝑅
, 
𝐼
 is an edit instruction (along the lines of the example shown in Figure 2),

and 
𝑆
​
𝑡
​
𝑎
​
𝑡
​
𝑢
​
𝑠
 is either 
𝑝
​
𝑒
​
𝑛
​
𝑑
​
𝑖
​
𝑛
​
𝑔
 or 
𝑐
​
𝑜
​
𝑚
​
𝑝
​
𝑙
​
𝑒
​
𝑡
​
𝑒
​
𝑑
.

The 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 algorithm also maintains a dependency graph 
𝐷
 (line 5). Figure 4 illustrates the dependency graph structure. We will discuss it in details in Section 2.2.1. For now, it suffices to know that the dependency graph 
𝐷
 represents the syntactic and semantic dependency relations between code blocks in the repository 
𝑅
.

The loop at lines 6–9 is executed until 
Δ
𝑠
​
𝑒
​
𝑒
​
𝑑
​
𝑠
 is non-empty. Line 7 calls the InitializePlanGraph function (lines 11–13) that adds all the changes in 
Δ
𝑠
​
𝑒
​
𝑒
​
𝑑
​
𝑠
 as root nodes of the plan graph. Each edit specification comprises of a code block 
𝐵
 and an edit instruction 
𝐼
.

The status is set to pending for the root nodes (line 13). The function AdaptivePlanAndExecute is called at line 8 which executes the plan, updates the dependency graph with each code change and extends the plan as necessary. Once the plan graph is completely executed, the oracle 
Θ
 is run on the repository. It returns error locations and diagnostic messages which form 
Δ
𝑠
​
𝑒
​
𝑒
​
𝑑
​
𝑠
 for the next round. If the repository passes the oracle’s checks then it returns an empty set and the 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 algorithm terminates.

We now discuss AdaptivePlanAndExecute, which is the main work horse. It iteratively picks each pending node and processes it. Processing a pending node with an edit specification for a block 
𝐵
 with edit instruction 
𝐼
 involves the following five steps:

(1) 

The first step (line 19) is to extract the fragment of code to edit. Simply extracting code of the block 
𝐵
 loses information about relationship of 
𝐵
 with the surrounding code. Keeping the entire file on the other hand takes up prompt space and is often unnecessary. We found the surrounding context is most helpful when a block belongs to a class. For such blocks, we sketch the enclosing class. That is, in addition to the code of block 
𝐵
, we also keep declarations of the enclosing class and its members. As we discuss later, this sketched representation also helps us merge the LLM’s output into a source code file more easily.

(2) 

The second step (line 21) is to gather the context of the edit. The context of the edit (line 38–41) consists of (a) spatial context, which contains related code such as methods called from the block 
𝐵
, and (b) temporal context, which contains the previous edits that caused the need to edit the block 
𝐵
. The temporal context is formed by edits along the paths from the root nodes of the plan graph to 
𝐵
.

(3) 

The third step (lines 23–24) constructs a prompt for the edit using the fragment extracted in the first step, the instruction 
𝐼
 from the edit specification and the context extracted in the second step, and invokes the LLM using the prompt to get the edited code fragment.

(4) 

The fourth step (lines 26–28) merges the edited code back into the repository. Since the code is updated, many dependency relationships such as caller-callee, class hierarchy, etc. may need to change, and hence, this step also updates the dependency graph 
𝐷
.

(5) 

The fifth and final step (lines 30–35) does adaptive planning to propagate the effects of the current edit on dependant code blocks. This involves classifying the change in the edited block, and depending on the type of change, picking the right dependencies in the dependency graph to traverse and locate affected blocks. For instance, if the edit of a method 
𝑚
 in the current block 
𝐵
 involves update to the signature of the method, then all callers of 
𝑚
 get affected (the scenario in Figure 3). For each affected block 
𝐵
′
 and the dependency relation rel connecting 
𝐵
 to 
𝐵
′
 in the dependency graph, we get a pair 
⟨
𝐵
′
,
rel
⟩
. If a node exists for 
𝐵
′
 in the plan graph and it is pending, then we add an edge from 
𝐵
 to 
𝐵
′
 labeled with rel to the plan graph. Otherwise, the edge is added to a newly created node for 
𝐵
′
 (line 34). The block 
𝐵
 is marked as completed (line 31).

2.2.Static Analysis Components
Figure 4.Illustration of the dependency graph annotated with relations as the edge labels.

We now turn our attention to the static analysis components used in 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
. We will cover all the data structures and functions in Cyan background from Algorithm 1.

2.2.1.Incremental Dependency Analysis

An LLM can be provided a code fragment and an instruction to edit it in a prompt. While the LLM may perform the desired edit accurately, analyzing the impact of the edit on the rest of the repository is outside the scope of the LLM call. We believe static analysis is well-suited to do this and propose an incremental dependency analysis for the same.

DependencyGraph. Dependency analysis (Aho et al., 2007) is used for tracking syntactic and semantic relations between code elements. In our case, we are interested in relations between import statements, methods, classes, field declarations and statements (excluding those that operate only on variables defined locally within the enclosing method). Formally, a dependency graph D 
=
(
𝑁
,
𝐸
)
 where 
𝑁
 is a set of nodes representing the code blocks mentioned above and 
𝐸
 is a set of labeled edges where the edge label gives the relation between the source and target nodes of the edge. Figure 4 illustrates all the relations we track as labeled edges. The relations include (1) syntactic relations (ParentOf and ChildOf, Construct and ConstructedBy) between a block 
𝑐
 and the block 
𝑝
 that encloses 
𝑐
 syntactically; a special case being a constructor and its enclosing class related by Construct and ConstructedBy, (2) import relations (Imports and ImportedBy) between an import statement and statements that use the imported modules, (3) inheritance relations (BaseClassOf and DerivedClassOf) between a class and its superclass, (4) method override relations (Overrides and OverridenBy) between an overriding method and the overriden method, (5) method invocation relations (Calls and CalledBy) between a statement and the method it calls, (6) object instantiation relations (Instantiates and InstantiatedBy) between a statement and the constructor of the object it creates, and (7) field use relations (Uses and UsedBy) between a statement and the declaration of a field it uses.

ConstructDependencyGraph. The dependency relations are derived across the source code spread over the repository through static analysis. We represent the source code of a repository as a forest of abstract syntax trees (ASTs) and add the dependency edges between AST sub-trees. A file-local analysis derives the syntactic and import relations. All other relations require an inter-class, inter-procedural analysis that can span file boundaries. In particular, we use the class hierarchy analysis (Dean et al., 1995) for deriving the semantic relations.

Atomic Change
 	
Label
	
Dependency Graph Update
	
Change May-Impact Analysis

Modification Changes

Body of method M
 	
MMB
	
Recompute the edges incident on the statements in the method body.
	
If an escaping object is modified then Rel(D, M, CalledBy) else Nil.


Signature of method M
 	
MMS
	
Recompute the edges incident on the method.
	
Rel(D, M, CalledBy), Rel(D, M, Overrides), Rel(D, M, OverriddenBy), Rel(
D
′
, M, Overrides), Rel(
D
′
, M, OverriddenBy)


Field F in class C
 	
MF
	
Recompute the edges incident on the field.
	
Rel(D, F, UsedBy), Rel(D, C, ConstructedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)


Declaration of class C
 	
MC
	
Recompute the edges incident on the class.
	
Rel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf), Rel(
D
′
, C, BaseClassOf), Rel(
D
′
, C, DerivedClassOf)


Signature of constructor of class C
 	
MCC
	
No change.
	
Rel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)


Import/Using statement I
 	
MI
	
Recompute the edges incident on the import statement.
	
Rel(D, I, ImportedBy)

Addition Changes

Method M in class C
 	
AM
	
Add new node and edges by analyzing the method. If C.M overrides a base class method B.M then redirect the Calls/CalledBy edges from B.M to C.M if the receiver object is of type C.
	
Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf), Rel(
D
′
, M, CalledBy)


Field F in class C
 	
AF
	
Add new node and edges by analyzing the field declaration.
	
Rel(D, C, ConstructedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)


Declaration of class C
 	
AC
	
Add new node and edges by analyzing the class declaration.
	
Nil


Constructor of class C
 	
ACC
	
Add new node and edges by analyzing the constructor.
	
Rel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)


Import/Using statement I
 	
AI
	
Add new node and edges by analyzing the import statement.
	
Nil

Deletion Changes

Method M in class C
 	
DM
	
Remove the node for M and edges incident on M. If C.M overrides a base class method B.M then redirect the Calls/CalledBy edges from C.M to B.M if the receiver object is of type C.
	
Rel(D, M, CalledBy), Rel(D, M, Overrides), Rel(D, M, OverriddenBy)


Field F in class C
 	
DF
	
Remove the node of the field and edges incident on it.
	
Rel(D, F, UsedBy), Rel(D, C, ConstructedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)


Declaration of class C
 	
DC
	
Remove the node of the class and edges incident on it.
	
Rel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)


Constructor of class C
 	
DCC
	
Remove the edges incident on the class due to object instatiations using the constructor.
	
Rel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)


Import/Using statement I
 	
DI
	
Remove the node of the import statement and edges incident on it.
	
Rel(D, I, ImportedBy)
Table 1.Rules for updating the dependency graph and for change may-impact analysis for atomic changes. We refer to the dependency graphs before and after the updates by D and 
D
′
 respectively.

ClassifyChanges. As discussed in Section 2.1, in the fourth step, 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 merges the code generated by the LLM into the repository. By pattern-matching the code before and after, we classify the code changes. Table 1 (the first and second columns) gives the types of atomic changes and their labels. Broadly, the changes are organized as modification, addition and deletion changes, and further by which construct is changed. We distinguish between method body and method signature changes. Similarly, we distinguish between changes to a class declaration, to its constructor or to its fields. The changes to import statements or the statements that use imports are also identified. These are atomic changes. An LLM can make multiple simultaneous edits in the given code fragment, resulting in multiple atomic changes, all of which are identified by the ClassifyChanges function.

UpdateDependencyGraph. As code generated by the LLM is merged, the dependency relations associated with the code at the change site are re-analyzed. Table 1 (the third column) gives the rules to update the dependency graph D to 
D
′
 based on the labels inferred by ClassifyChanges. For modification changes, we recompute the relations of the changed code except for constructors. A constructor is related to its enclosing class by a syntactic relation which does not have to be recomputed. For addition changes, new nodes and edges are created for the added code. Edges corresponding to syntactic relations are created in a straightforward manner. If a change simultaneously adds an element (an import, a method, a field or a class) and its uses, we create a node for the added element before analyzing the statements that use it. Addition of a method needs special handling as shown in the table: if an overriding method C.M is added then the Calls/CalledBy edges incident on the matching overriden method B.M are redirected to C.M if the call is issued on a receiver object of type C. The deletion of an overriding method requires an analogous treatment as stated in Table 1. All other deletion changes require removing nodes and edges as stated in the table.

2.2.2.Change May-Impact Analysis

In the fifth step, 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 identifies the code blocks that may have been impacted by the code change by the LLM. Let Rel(D, B, rel) be the set of blocks that are connected to a block B via relation rel in the dependency graph D. Let D and 
D
′
 be the dependency graph before and after the updates in Table 1.

GetAffectedBlocks. The last column in Table 1 tells us how to identify blocks affected by a code change for each type of change. When the body of a method M is edited, we perform escape analysis (Choi et al., 1999; Blanchet, 2003) to identify if any object accessible in the callers of M (an escaping object) has been affected by the change. If yes, the callers of M (identified through Rel(D, M, CalledBy)) are identified as affected blocks. Otherwise, the change is localized to the method and there are no affected blocks. If the signature of a method is edited, the callers and methods related to it through method-override relation in the inheritance hierarchy are affected. The signature change itself can affect the Overrides and OverridenBy relations, e.g., addition or deletion of the @Override access modifier. Therefore, the blocks related by these relations in the updated dependency graph 
D
′
 are also considered as affected as shown in Table 1 (the row with MMS label). When a field F of a class C is modified, the statements that use F, the constructors of C and sub/super-classes of C are affected. When a class is modified, the methods that instantiate it and its sub/super-classes as per D and 
D
′
 are affected. A modification to a constructor has a similar rule except that such a change does not change inheritance relations and hence, only D is required. When an import statement I is modified, the statements that use the imported module are affected.

The addition and deletion changes are less complex than the modification changes, and their rules are designed along the same lines as discussed above. In the interest of space, we do not explain each of them step-by-step. We assume that there is no use of a newly added class or an import in the code. Therefore, adding them does not result in any affected blocks. In our experiments, we have found the rules in Table 1 to be adequate. However, 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 can be easily configured to accommodate variations of the rules in Table 1 if necessary.

2.3.Adaptive Planning and Plan Execution

We now discuss the data structures and functions from Algorithm 1 in the Orchid background.

2.3.1.Adaptive Planning

Having identified the affected blocks (using GetAffectedBlocks), 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 creates change obligations that need to be discharged using an LLM to make the dependent code consistent with the change. As discussed in Section 2.1, this is an iterative process.

PlanGraph. A plan graph P 
=
(
𝑂
,
𝐶
)
 is a directed acyclic graph with a set of obligations 
𝑂
, each of which is a triple 
⟨
𝐵
,
𝐼
,
𝑠
​
𝑡
​
𝑎
​
𝑡
​
𝑢
​
𝑠
⟩
 where B is a block, I is an instruction and status is either pending or completed. An edge in 
𝐶
 records the cause, the dependency relation between the blocks in the source and target obligations. In other words, the edge label identifies which Rel clause in a change may-impact rule in Table 1 results in creation of the target obligation.

ExtractCodeFragment. As discussed in the first step in Section 2.1, simply extracting code for a block B is sub-optimal as it loses context. The ExtractCodeFragment function takes the whole class the code block belongs to, keeps the complete code for B and retains only declarations of the class and other class members. We found this to be useful because the names and types of the class and other members provide additional context to the LLM. Often times the LLM needs to make multiple simultaneous changes. For example, in some of our case studies, the LLM has to add a field declaration, take an argument to a constructor and use it within the constructor to initialize the field. Providing the sketch of the surrounding code as a code fragment to the LLM allows the LLM to make these changes at the right places. The code fragment extraction logic is implemented by traversing the AST and ”folding” away the subtrees (e.g., method bodies) that are sketched. As stated in Section 1, this sketched representation also allows us to place the LLM generated code back into the AST without ambiguity, even when there are multiple simultaneous changes.

GetSpatialContext. Spatial context in CodePlan refers to the arrangement and relationships of code blocks within a codebase, helping understand how classes, functions, variables, and modules are structured and interact. It’s crucial for making accurate code changes. CodePlan utilizes the dependency graph to extract spatial context, representing code as nodes and their relationships as edges. This graph enables CodePlan to navigate codebases, identify relevant code blocks, and maintain awareness of their spatial context. As a result, when generating code edits, the dependency graph empowers CodePlan to make context-aware code modifications that are consistent with the code’s spatial organization, enhancing the accuracy and reliability of its code editing capabilities.

GetTemporalContext. The plan graph records all change obligations and their inter-dependences. Extracting temporal context is accomplished by linearizing all paths from the root nodes of the plan graph to the target node. Each change is a pair of the code fragments before and after the change. The temporal context also states the ”causes” (recorded as edge labels) that connect the target node with its predecessor nodes. For example, if a node A is connected to B with a CalledBy edge, then the temporal context for B is the before/after fragments for A and a statement that says that ”B calls A”, which helps the LLM understand the cause-effect relation between the latest temporal change (change to A) and the current obligation (to make a change to B).

2.3.2.Plan Execution

𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 iteratively selects a pending node in the plan graph and invokes an LLM to discharge the change obligation.

MakePrompt. Having extracted the code fragment to be edited along with the relevant spatial and temporal context, we construct a prompt to pass to the LLM with the structure given below. We open with the task specific instructions 
p
1
 followed by listing the edits made in the repository so far 
p
2
 that are relevant to the fragment being edited. The next section 
p
3
 notes how each of the fragments present in 
p
2
 are related to the fragment to be edited. This is followed by the spatial context 
p
4
 and the fragment to the edited 
p
5
.

Prompt Template
p
1
Task Instructions: Your task is to 
…


p
2
Earlier Code Changes (Temporal Context): These are edits that have been made in the code-base previously -

Edit 1:
    Before: <<code_before>>
    After: <<code_after>>

⋯


p
3
Causes for Change: The change is required due to -

<<code_to_be_edited>> is related to <<code_changed_earlier>> by <<cause>>
⋯


p
4
Related Code (Spatial Context): The following code maybe related -

<<related_code_block-1>>
⋯


p
5
Code to be Changed Next: The existing code is given below -

<<code_to_be_edited>>

Edit the ”Code to be Changed Next” and produce ”Changed Code” below. Edit the ”Code to be Changed Next” according to the ”Task Instructions” to make it consistent with the ”Earlier Code Changes”, ”Causes for Change” and ”Related Code”. If no changes are needed, output ”No changes.”

Oracle and Plan Iterations. Once all the nodes in the plan graph are marked as completed and no new nodes are added, an iteration of repository-level code edits is completed. As shown in Figure 2, the oracle is invoked on the repository. If the oracle flags any errors (e.g., build errors), the error locations and diagnostic messages are added as seed changes for the next iteration and the adaptive planning resumes once again. If the oracle does not flag any errors, 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 terminates.

3.Implementation

In this section, we provide a detailed overview of the implementation components that constitute the core of our method.

Dependency Graph Construction. At the core of the CodePlan methodology lies the Dependency Graph, which is instrumental in representing the intricate relationships between code blocks. To build this Dependency Graph from a code repository, we adopt a systematic approach. Initially, we parse all the code files within the repository, utilizing the tree-sitter library (Brunsfeld et al., 2023) to generate an AST-like structure. This structured representation simplifies the identification of various fundamental code blocks within the codebase. For instance, Figure 5 exemplifies an AST structure for a C# code snippet produced by tree-sitter. Code blocks are identified at different levels, including Classes, Methods, import statements, and non-class expressions. For instance, in Figure 5, the subtree rooted at the class_declaration node corresponds to the SyncSubscriberTest class.

Figure 5.AST structure for a C# code snippet produced by tree-sitter.

Relation Identification in C#. In the context of C# repositories, the establishment of edges within the Dependency Graph involves the careful tracing of relationships within the AST. We have devised custom logic for each type of relationship outlined in Figure 4, encompassing vital connections such as caller-callee, overrides-overridden, base class-derived class, and others. To illustrate, for the Caller/Callee relationship, we search for invocation_expression nodes within the AST. Subsequently, we process the sub-tree beneath these nodes to resolve essential details such as the target class and the invoked method’s name. Armed with this information, we create Calls/CalledBy relation links between the code block initiating the method call and the corresponding method block within the target class. While we have implemented custom logic for these relations, it’s important to note that alternative dependency analysis tools for C# such as Language Servers for C# (LSP) (Omn, [n. d.]), CodeQL (Cod, [n. d.]), or similar solutions can also be integrated into our system, owing to its inherent flexibility.

Relation Identification in Python. For Python repositories, we use Jedi (Jed, [n. d.]) - a static analysis tool which discovers references and declarations of symbols throughout the codebase. These capabilities are harnessed to identify edges in the Dependency Graph for relationships such caller-callee, overrides-overridden, and base class-derived class.

Integration of GPT-4 for Code Edits. CodePlan leverages the remarkable capabilities of GPT-4 (OpenAI, 2023) to perform code edits effectively. During the construction of input data for the edit model, we meticulously provide temporal context, spatial context, and the actual code to be edited in the form of code snippets. These code snippets represent classes or methods that contain the edit site and are meticulously structured in a sketched representation, as stated in Section 2.1. This sketched representation ensures that the model is enriched with a substantial context for each edit site, significantly enhancing the quality and accuracy of the edits it generates.

Language Extensibility. While our current implementation proficiently supports C# and Python repositories, extending support to repositories in other programming languages is a straightforward endeavor. It primarily entails creating a dependency graph with the relations identified in Figure 4 and incorporating it into the CodePlan framework, thereby allowing for seamless adaptation to a diverse array of programming languages.

4.Related Work

LLMs for Coding Tasks. A multitude of LLMs (Ahmad et al., 2021; Wang et al., 2021; Wang and Komatsuzaki, 2021; Brown et al., 2020; Austin et al., 2021; Chen et al., 2021; Black et al., 2022; Xu et al., 2022; Chowdhery et al., 2022; Fried et al., 2022; OpenAI, 2023; Touvron et al., 2023) have been trained on large-scale corpora of source code and natural language text. These have been used to accomplish a variety of coding tasks. A few examples of their use include program synthesis (Li et al., 2022; Nijkamp et al., 2023), program repair (Xia et al., 2023; Jin et al., 2023; Ahmed and Devanbu, 2023), vulnerability patching (Pearce et al., 2022), inferring program invariants (Pei et al., 2023a), test generation (Schäfer et al., 2023) and multi-task evaluation (Tian et al., 2023). However, these investigations are performed on curated examples that are extracted from their repositories and are meant to be accomplished with independent invocations of the LLM. We consider a different class of tasks posed at the scale of code repositories, where an LLM is called multiple times on different examples which are inter-dependent. We monitor the results of each LLM invocation within the repository-wide context to identify future code change obligations to get the repository to a consistent state, e.g., where the repository is free of build or runtime errors.

Automated Planning. Automated planning (Ghallab et al., 2004; Russell, 2010) is a well-studied topic in AI. Online planning (Russell, 2010) is used when the effect of actions is not known and the state-space cannot be enumerated a priori. It requires monitoring the actions and plan extension. In our case, the edit actions are carried out by an LLM whose results cannot be predicted before-hand and the state-space is unbounded. As a consequence, our adaptive planning is an online algorithm where we monitor the actions and extend the plan through static analysis. In orthogonal directions, (Jiang et al., 2023) uses an LLM to derive a plan given a natural language intent before generating code to solve complex coding problems and (Zhang et al., 2023a) performs lookahead planning (tree search) to guide token-level decoding of code LMs. Planning in our work is based on analyzing dependency relations and changes to them as an LLM makes changes to a code repository.

Analysis of Code Changes. Static analysis is used for ensuring software quality. It is expensive to recompute the analysis results every time the code undergoes changes. The field of incremental program analysis offers techniques to recompute only the analysis results impacted by the change. Specialized algorithms have been developed for dataflow analysis (Ryder, 1983; Arzt and Bodden, 2014), pointer analysis (Yur et al., 1999), symbolic execution (Person et al., 2011), bug detection (McPeak et al., 2013) and type analysis (Busi et al., 2019). Program differencing (Apiwattanapong et al., 2004; Lahiri et al., 2012; Kim et al., 2012) and change impact analysis (Arnold and Bohner, 1996; Jashki et al., 2008) determine the differences in two program versions and the effect of a change on the rest of the program. The impact of changes has been studied for regression testing (Ren et al., 2004), analyzing refactorings (Dig et al., 2006) and assisting in code review (Alves et al., 2014; Ge et al., 2017). We analyze the code generated by an LLM and incrementally update the syntactic (e.g., parent-child) and dependency (e.g., caller-callee) relations. We further analyze the likely impact of those changes on related code blocks and create change obligations to be discharged by the LLM.

Spatial and Temporal Contextualization. As discussed in the Introduction, LLMs benefit from relevant context derived from other files in the repository and from past edits. We provide both these pieces of information to the LLM by tracking the code changes and dependency relations.

Learning Edit Patterns. Many approaches have been developed to learn edit patterns from past edits or commits in the form of rewrite rules (de Sousa et al., 2021), bug fixes (Andersen and Lawall, 2010; Bader et al., 2019), type changes (Ketkar et al., 2022), API migrations (Lamothe et al., 2020; Xu et al., 2019) and neural representations of edits (Yin et al., 2019). Approaches such as (Meng et al., 2011) and (Meng et al., 2013) synthesize context-aware edit scripts from user-provided examples and apply them in new contexts. Other approaches observe the user actions in an IDE to automate repetitive edits (Miltner et al., 2019) and temporally-related edit sequences (Zhang et al., 2022). We do not aim to learn edit patterns and we do not assume similarities between edits. Our focus is to identify effects of code changes made by an LLM and to guide the LLM towards additional changes that become necessary.

5.Conclusions and Future Work

In this paper, we introduced 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
, a novel framework designed to tackle the challenges of repository-level coding tasks, which involve pervasive code modifications across large and inter-dependent codebases. 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 leverages incremental dependency analysis, change may-impact analysis, and adaptive planning to orchestrate multi-step edits guided by Large Language Models. We evaluated 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 on diverse code repositories with varying complexities and sizes, including both internal proprietary repositories and public GitHub repositories in C# and Python for migration and temporal edit tasks. Our results demonstrated that 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 outperforms baseline methods, achieving better alignment with the ground truth. In conclusion, 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 presents a promising approach to automating complex repository-level coding tasks, offering both productivity benefits and accuracy improvements. Its success in addressing these challenges opens up new possibilities for efficient and reliable software engineering practices.

While 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 has shown significant promise, there are several avenues for future research and enhancements. First, we aim to expand its applicability to a broader range of programming languages and code artifacts, including configuration files, metadata, and external dependencies, to provide a more holistic solution for repository-level editing. Additionally, we plan to explore further customization of 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
’s change may-impact analysis. This could involve incorporating task-specific impact analysis rules, either through rule-based methods or more advanced machine learning techniques, to fine-tune its editing decisions for specific coding tasks. Furthermore, we will address the challenge of handling dynamic dependencies, such as data flow dependencies, complex dynamic dispatching (via virtual functions and dynamic castings), algorithmic dependencies (e.g., when input lists are expected to be sorted), and various execution dependencies (such as multi-threading and distributed processing), to make 
𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇
 even more versatile in addressing a wider range of software engineering tasks.

References
(1)	
aud ([n. d.])	[n. d.].audiocraft.https://github.com/facebookresearch/audiocraft.
Cod ([n. d.])	[n. d.].CodeQL.https://github.com/github/codeql.
JAR ([n. d.])	[n. d.].JARVIS.https://github.com/microsoft/JARVIS.
Jed ([n. d.])	[n. d.].Jedi.https://github.com/davidhalter/jedi.
Omn ([n. d.])	[n. d.].OmniSharp.https://github.com/OmniSharp/csharp-language-server-protocol.
pyr ([n. d.])	[n. d.].Pyright.https://github.com/microsoft/pyright.
rep ([n. d.])	[n. d.].Reactive Streams TCK.https://github.com/reactive-streams/reactive-streams-dotnet/tree/master/src/tck.
whi ([n. d.])	[n. d.].whisper.https://github.com/openai/whisper.
Agrawal et al. (2023)	Lakshya A Agrawal, Aditya Kanade, Navin Goyal, Shuvendu K. Lahiri, and Sriram K. Rajamani. 2023.Guiding Language Models of Code with Global Context using Monitors.arXiv:2306.10763 [cs.CL]
Ahmad et al. (2021)	Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray, and Kai-Wei Chang. 2021.Unified Pre-training for Program Understanding and Generation.arXiv:2103.06333 [cs.CL]
Ahmed and Devanbu (2023)	Toufique Ahmed and Premkumar Devanbu. 2023.Better patching using LLM prompting, via Self-Consistency.arXiv:2306.00108 [cs.SE]
Aho et al. (2007)	Alfred V Aho, Ravi Sethi, Jeffrey D Ullman, et al. 2007.Compilers: principles, techniques, and tools. Vol. 2.Addison-wesley Reading.
Alves et al. (2014)	Everton L. G. Alves, Myoungkyu Song, and Miryung Kim. 2014.RefDistiller: A Refactoring Aware Code Review Tool for Inspecting Manual Refactoring Edits. In Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering (Hong Kong, China) (FSE 2014). Association for Computing Machinery, New York, NY, USA, 751–754.https://doi.org/10.1145/2635868.2661674
Amazon Web Services, Inc. (2023)	Amazon Web Services, Inc. 2023.Amazon Code Whisperer - AI Code Generator.https://aws.amazon.com/codewhisperer/Accessed: July 25, 2023.
Andersen and Lawall (2010)	Jesper Andersen and Julia L Lawall. 2010.Generic patch inference.Automated software engineering 17 (2010), 119–148.
Apiwattanapong et al. (2004)	Taweesup Apiwattanapong, Alessandro Orso, and Mary Jean Harrold. 2004.A differencing algorithm for object-oriented programs. In Proceedings. 19th International Conference on Automated Software Engineering, 2004. IEEE, 2–13.
Arnold and Bohner (1996)	RS Arnold and SA Bohner. 1996.An introduction to software change impact analysis.Software Change Impact Analysis (1996), 1–26.
Arzt and Bodden (2014)	Steven Arzt and Eric Bodden. 2014.Reviser: efficiently updating IDE-/IFDS-based data-flow analyses in response to incremental program changes. In Proceedings of the 36th International Conference on Software Engineering. 288–298.
Austin et al. (2021)	Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. 2021.Program Synthesis with Large Language Models.http://arxiv.org/abs/2108.07732arXiv:2108.07732 [cs].
Bader et al. (2019)	Johannes Bader, Andrew Scott, Michael Pradel, and Satish Chandra. 2019.Getafix: Learning to Fix Bugs Automatically.Proc. ACM Program. Lang. 3, OOPSLA, Article 159 (Oct. 2019), 27 pages.https://doi.org/10.1145/3360585
Black et al. (2022)	Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, and others. 2022.Gpt-neox-20b: An open-source autoregressive language model.arXiv preprint arXiv:2204.06745 (2022).
Blanchet (2003)	Bruno Blanchet. 2003.Escape analysis for JavaTM: Theory and practice.ACM Transactions on Programming Languages and Systems (TOPLAS) 25, 6 (2003), 713–775.
Brody et al. (2020)	Shaked Brody, Uri Alon, and Eran Yahav. 2020.A structural model for contextual code changes.4, OOPSLA (Nov. 2020).https://doi.org/10.1145/3428283Publisher Copyright: © 2020 Owner/Author..
Brown et al. (2020)	Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020.Language models are few-shot learners.Advances in neural information processing systems 33 (2020), 1877–1901.
Brunsfeld et al. (2023)	Max Brunsfeld, Andrew Hlynskyi, Patrick Thomson, Josh Vera, Phil Turnbull, Timothy Clem, Douglas Creager, Andrew Helwer, Rob Rix, Hendrik Van Antwerpen, Michael Davis, , Ika, Tuấn-Anh Nguyễn, Stafford Brunk, Niranjan Hasabnis, Bfredl, Mingkai Dong, Matt Massicotte, Jonathan Arnett, Vladimir Panteleev, Steven Kalt, Kolja Lampe, Alex Pinkus, Mark Schmitz, Matthew Krupcale, Narpfel, Santos Gallegos, Vicent Martí, and , Edgar. 2023.tree-sitter/tree-sitter: v0.20.8.https://doi.org/10.5281/ZENODO.4619183
Bundy (1988)	Alan Bundy. 1988.The use of explicit plans to guide inductive proofs. In 9th International Conference on Automated Deduction: Argonne, Illinois, USA, May 23–26, 1988 Proceedings 9. Springer, 111–120.
Busi et al. (2019)	Matteo Busi, Pierpaolo Degano, and Letterio Galletta. 2019.Using standard typing algorithms incrementally. In NASA Formal Methods: 11th International Symposium, NFM 2019, Houston, TX, USA, May 7–9, 2019, Proceedings 11. Springer, 106–122.
Chen et al. (2021)	Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, and others. 2021.Evaluating large language models trained on code.arXiv preprint arXiv:2107.03374 (2021).
Choi et al. (1999)	Jong-Deok Choi, Manish Gupta, Mauricio Serrano, Vugranam C Sreedhar, and Sam Midkiff. 1999.Escape analysis for Java.Acm Sigplan Notices 34, 10 (1999), 1–19.
Chowdhery et al. (2022)	Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. 2022.Palm: Scaling language modeling with pathways.arXiv preprint arXiv:2204.02311 (2022).
de Sousa et al. (2021)	Reudismam Rolim de Sousa, Gustavo Soares, Rohit Gheyi, Titus Barik, and Loris D’Antoni. 2021.Learning Quick Fixes from Code Repositories. In SBES ’21: 35th Brazilian Symposium on Software Engineering, Joinville, Santa Catarina, Brazil, 27 September 2021 - 1 October 2021, Cristiano D. Vasconcellos, Karina Girardi Roggia, Vanessa Collere, and Paulo Bousfield (Eds.). ACM, 74–83.https://doi.org/10.1145/3474624.3474650
Dean et al. (1995)	Jeffrey Dean, David Grove, and Craig Chambers. 1995.Optimization of object-oriented programs using static class hierarchy analysis. In ECOOP’95—Object-Oriented Programming, 9th European Conference, Åarhus, Denmark, August 7–11, 1995 9. Springer, 77–101.
Dig et al. (2006)	Danny Dig, Can Comertoglu, Darko Marinov, and Ralph Johnson. 2006.Automated detection of refactorings in evolving components. In ECOOP 2006–Object-Oriented Programming: 20th European Conference, Nantes, France, July 3-7, 2006. Proceedings 20. Springer, 404–428.
Ding et al. (2022)	Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang. 2022.CoCoMIC: Code Completion By Jointly Modeling In-file and Cross-file Context.http://arxiv.org/abs/2212.10007arXiv:2212.10007 [cs].
Fried et al. (2022)	Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2022.Incoder: A generative model for code infilling and synthesis.arXiv preprint arXiv:2204.05999 (2022).
Ge et al. (2017)	Xi Ge, Saurabh Sarkar, Jim Witschey, and Emerson Murphy-Hill. 2017.Refactoring-aware code review. In 2017 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC). IEEE, 71–79.
Ghallab et al. (2004)	Malik Ghallab, Dana Nau, and Paolo Traverso. 2004.Automated Planning: theory and practice.Elsevier.
Github, Inc. (2023)	Github, Inc. 2023.GitHub Copilot: Your AI pair programmer.https://github.com/features/copilotAccessed: July 25, 2023.
González et al. (2015)	David González, Joshué Pérez, Vicente Milanés, and Fawzi Nashashibi. 2015.A review of motion planning techniques for automated vehicles.IEEE Transactions on intelligent transportation systems 17, 4 (2015), 1135–1145.
Gupta et al. (2023)	Priyanshu Gupta, Avishree Khare, Yasharth Bajpai, Saikat Chakraborty, Sumit Gulwani, Aditya Kanade, Arjun Radhakrishna, Gustavo Soares, and Ashish Tiwari. 2023.GrACE: Generation using Associated Code Edits.arXiv:2305.14129 [cs.SE]
Jashki et al. (2008)	Mohammad-Amin Jashki, Reza Zafarani, and Ebrahim Bagheri. 2008.Towards a more efficient static software change impact analysis method. In Proceedings of the 8th ACM SIGPLAN-SIGSOFT workshop on Program analysis for software tools and engineering. 84–90.
Jiang et al. (2023)	Xue Jiang, Yihong Dong, Lecheng Wang, Qiwei Shang, and Ge Li. 2023.Self-planning Code Generation with Large Language Model.arXiv:2303.06689 [cs.SE]
Jin et al. (2023)	Matthew Jin, Syed Shahriar, Michele Tufano, Xin Shi, Shuai Lu, Neel Sundaresan, and Alexey Svyatkovskiy. 2023.InferFix: End-to-End Program Repair with LLMs.arXiv preprint arXiv:2303.07263 (2023).
Karpas and Magazzeni (2020)	Erez Karpas and Daniele Magazzeni. 2020.Automated planning for robotics.Annual Review of Control, Robotics, and Autonomous Systems 3 (2020), 417–439.
Ketkar et al. (2022)	Ameya Ketkar, Oleg Smirnov, Nikolaos Tsantalis, Danny Dig, and Timofey Bryksin. 2022.Inferring and applying type changes. In Proceedings of the 44th International Conference on Software Engineering. 1206–1218.
Kim et al. (2012)	Miryung Kim, David Notkin, Dan Grossman, and Gary Wilson. 2012.Identifying and summarizing systematic code changes via rule inference.IEEE Transactions on Software Engineering 39, 1 (2012), 45–62.
La Valle (2011)	Steven M La Valle. 2011.Motion planning.IEEE Robotics & Automation Magazine 18, 2 (2011), 108–118.
Lahiri et al. (2012)	Shuvendu K Lahiri, Chris Hawblitzel, Ming Kawaguchi, and Henrique Rebêlo. 2012.Symdiff: A language-agnostic semantic diff tool for imperative programs. In Computer Aided Verification: 24th International Conference, CAV 2012, Berkeley, CA, USA, July 7-13, 2012 Proceedings 24. Springer, 712–717.
Lamothe et al. (2020)	Maxime Lamothe, Weiyi Shang, and Tse-Hsun Peter Chen. 2020.A3: Assisting android api migrations using code examples.IEEE Transactions on Software Engineering 48, 2 (2020), 417–431.
Li et al. (2022)	Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d’Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel J. Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu, and Oriol Vinyals. 2022.Competition-level code generation with AlphaCode.Science 378, 6624 (2022), 1092–1097.https://doi.org/10.1126/science.abq1158_eprint: https://www.science.org/doi/pdf/10.1126/science.abq1158.
Liu et al. (2023)	Tianyang Liu, Canwen Xu, and Julian McAuley. 2023.RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems.arXiv:2306.03091 [cs.CL]
McPeak et al. (2013)	Scott McPeak, Charles-Henri Gros, and Murali Krishna Ramanathan. 2013.Scalable and incremental software bug detection. In Proceedings of the 2013 9th Joint Meeting on Foundations of Software Engineering. 554–564.
Meng et al. (2011)	Na Meng, Miryung Kim, and Kathryn S McKinley. 2011.Sydit: Creating and applying a program transformation from an example. In Proceedings of the 19th ACM SIGSOFT symposium and the 13th European conference on Foundations of software engineering. 440–443.
Meng et al. (2013)	Na Meng, Miryung Kim, and Kathryn S McKinley. 2013.LASE: locating and applying systematic edits by learning from examples. In 2013 35th International Conference on Software Engineering (ICSE). IEEE, 502–511.
Miltner et al. (2019)	Anders Miltner, Sumit Gulwani, Vu Le, Alan Leung, Arjun Radhakrishna, Gustavo Soares, Ashish Tiwari, and Abhishek Udupa. 2019.On the fly synthesis of edit suggestions.Proceedings of the ACM on Programming Languages 3, OOPSLA (2019), 1–29.
Nijkamp et al. (2023)	Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2023.CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis. In The Eleventh International Conference on Learning Representations.https://openreview.net/forum?id=iaYcJKpY2B_
OpenAI (2023)	OpenAI. 2023.GPT-4 Technical Report.arXiv:2303.08774 [cs.CL]
Papineni et al. (2002)	Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002.Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th annual meeting of the Association for Computational Linguistics. 311–318.
Pashakhanloo et al. (2022)	Pardis Pashakhanloo, Aaditya Naik, Yuepeng Wang, Hanjun Dai, Petros Maniatis, and Mayur Naik. 2022.Codetrek: Flexible modeling of code using an extensible relational representation.(2022).
Pearce et al. (2022)	Hammond Pearce, Benjamin Tan, Baleegh Ahmad, Ramesh Karri, and Brendan Dolan-Gavitt. 2022.Examining Zero-Shot Vulnerability Repair with Large Language Models. In 2023 IEEE Symposium on Security and Privacy (SP). IEEE Computer Society, 1–18.
Pei et al. (2023b)	Hengzhi Pei, Jinman Zhao, Leonard Lausen, Sheng Zha, and George Karypis. 2023b.Better context makes better code language models: A case study on function call argument completion. In AAAI.https://www.amazon.science/publications/better-context-makes-better-code-language-models-a-case-study-on-function-call-argument-completion
Pei et al. (2023a)	Kexin Pei, David Bieber, Kensen Shi, Charles Sutton, and Pengcheng Yin. 2023a.Can Large Language Models Reason about Program Invariants?(2023).
Person et al. (2011)	Suzette Person, Guowei Yang, Neha Rungta, and Sarfraz Khurshid. 2011.Directed incremental symbolic execution.Acm Sigplan Notices 46, 6 (2011), 504–515.
Reid and Neubig (2022)	Machel Reid and Graham Neubig. 2022.Learning to Model Editing Processes.https://doi.org/10.48550/ARXIV.2205.12374
Ren et al. (2004)	Xiaoxia Ren, Fenil Shah, Frank Tip, Barbara G Ryder, and Ophelia Chesley. 2004.Chianti: a tool for change impact analysis of java programs. In Proceedings of the 19th annual ACM SIGPLAN conference on Object-oriented programming, systems, languages, and applications. 432–448.
Replit, Inc. (2023)	Replit, Inc. 2023.Replit.https://replit.com/Accessed: July 25, 2023.
Russell (2010)	Stuart J Russell. 2010.Artificial intelligence a modern approach.Pearson Education, Inc.
Ryder (1983)	Barbara G Ryder. 1983.Incremental data flow analysis. In Proceedings of the 10th ACM SIGACT-SIGPLAN symposium on Principles of programming languages. 167–176.
Schäfer et al. (2023)	Max Schäfer, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2023.Adaptive test generation using a large language model.arXiv preprint arXiv:2302.06527 (2023).
Shrivastava et al. (2023)	Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, and Torsten Scholak. 2023.RepoFusion: Training Code Models to Understand Your Repository.arXiv:2306.10998 [cs.LG]
Shrivastava et al. (2022)	Disha Shrivastava, Hugo Larochelle, and Daniel Tarlow. 2022.Repository-level prompt generation for large language models of code.arXiv preprint arXiv:2206.12839 (2022).
Tian et al. (2023)	Haoye Tian, Weiqi Lu, Tsz On Li, Xunzhu Tang, Shing-Chi Cheung, Jacques Klein, and Tegawendé F. Bissyandé. 2023.Is ChatGPT the Ultimate Programming Assistant – How far is it?arXiv:2304.11938 [cs.SE]
Touvron et al. (2023)	Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023.Llama 2: Open Foundation and Fine-Tuned Chat Models.arXiv:2307.09288 [cs.CL]
Wang and Komatsuzaki (2021)	Ben Wang and Aran Komatsuzaki. 2021.GPT-J-6B: A 6 billion parameter autoregressive language model.
Wang et al. (2021)	Yue Wang, Weishi Wang, Shafiq R. Joty, and Steven C. H. Hoi. 2021.CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation.ArXiv abs/2109.00859 (2021).
Wei et al. (2023a)	Jiayi Wei, Greg Durrett, and Isil Dillig. 2023a.Coeditor: Leveraging Contextual Changes for Multi-round Code Auto-editing.arXiv:2305.18584 [cs.SE]
Wei et al. (2023b)	Jiayi Wei, Greg Durrett, and Isil Dillig. 2023b.TypeT5: Seq2seq Type Inference using Static Analysis.arXiv:2303.09564 [cs.SE]
Wilson-Thomas ([n. d.])	Mark Wilson-Thomas. [n. d.].GitHub Copilot chat for Visual Studio 2022.https://devblogs.microsoft.com/visualstudio/github-copilot-chat-for-visual-studio-2022/Accessed: July 25, 2023.
Xia et al. (2023)	Chunqiu Steven Xia, Yuxiang Wei, and Lingming Zhang. 2023.Automated program repair in the era of large pre-trained language models. In Proceedings of the 45th International Conference on Software Engineering (ICSE 2023). Association for Computing Machinery.
Xu et al. (2022)	Frank F. Xu, Uri Alon, Graham Neubig, and Vincent Josua Hellendoorn. 2022.A Systematic Evaluation of Large Language Models of Code. In Proceedings of the 6th ACM SIGPLAN International Symposium on Machine Programming (MAPS 2022). Association for Computing Machinery, New York, NY, USA, 1–10.https://doi.org/10.1145/3520312.3534862event-place: San Diego, CA, USA.
Xu et al. (2021)	Frank F Xu, Junxian He, Graham Neubig, and Vincent J Hellendoorn. 2021.Capturing structural locality in non-parametric language models.arXiv preprint arXiv:2110.02870 (2021).
Xu et al. (2019)	Shengzhe Xu, Ziqi Dong, and Na Meng. 2019.Meditor: inference and application of API migration edits. In 2019 IEEE/ACM 27th International Conference on Program Comprehension (ICPC). IEEE, 335–346.
Yin et al. (2019)	Pengcheng Yin, Graham Neubig, Miltiadis Allamanis, Marc Brockschmidt, and Alexander Gaunt. 2019.Learning to Represent Edits. In ICLR 2019.https://www.microsoft.com/en-us/research/publication/learning-to-represent-edits/arXiv:1810.13337 [cs.LG].
Yur et al. (1999)	Jyh-shiarn Yur, Barbara G Ryder, and William A Landi. 1999.An incremental flow-and context-sensitive pointer aliasing analysis. In Proceedings of the 21st International conference on Software Engineering. 442–451.
Zhang et al. (2023b)	Fengji Zhang, Bei Chen, Yue Zhang, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, and Weizhu Chen. 2023b.RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation.arXiv preprint arXiv:2303.12570 (2023).
Zhang et al. (2023a)	Shun Zhang, Zhenfang Chen, Yikang Shen, Mingyu Ding, Joshua B. Tenenbaum, and Chuang Gan. 2023a.Planning with Large Language Models for Code Generation.arXiv:2303.05510 [cs.LG]
Zhang et al. (2022)	Yuhao Zhang, Yasharth Bajpai, Priyanshu Gupta, Ameya Ketkar, Miltiadis Allamanis, Titus Barik, Sumit Gulwani, Arjun Radhakrishna, Mohammad Raza, Gustavo Soares, and Ashish Tiwari. 2022.Overwatch: Learning patterns in code edit sequences.Proc. ACM Program. Lang. 6, OOPSLA2 (2022), 395–423.https://doi.org/10.1145/3563302
◄  Feeling
lucky? Conversion
report Report
an issue View original
on arXiv►
Copyright Privacy Policy Generated on Wed Feb 28 05:01:14 2024 by LaTeXML

## Metadata

```json
{
  "title": "𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇: Repository-level Coding using LLMs and Planning",
  "description": "",
  "url": "https://ar5iv.labs.arxiv.org/html/2309.12499",
  "content": "𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n: Repository-level Coding using LLMs and Planning\nRamakrishna Bairi\nrbairi@microsoft.com\nMicrosoft ResearchIndia\nAtharv Sonwane\nt-asonwane@microsoft.com\nMicrosoft ResearchIndia\nAditya Kanade\nkanadeaditya@microsoft.com\nMicrosoft ResearchIndia\nVageesh D C\nvachand@microsoft.com\nMicrosoft ResearchIndia\nArun Iyer\nariy@microsoft.com\nMicrosoft ResearchIndia\nSuresh Parthasarathy\nsupartha@microsoft.com\nMicrosoft ResearchIndia\nSriram Rajamani\nsriram@microsoft.com\nMicrosoft ResearchIndia\nB. Ashok\nbash@microsoft.com\nMicrosoft ResearchIndia\nShashank Shet\nt-sshet@microsoft.com\nMicrosoft ResearchIndia\n(2018; 2024)\nAbstract.\n\nSoftware engineering activities such as package migration, fixing errors reports from static analysis or testing, and adding type annotations or other specifications to a codebase, involve pervasively editing the entire repository of code. We formulate these activities as repository-level coding tasks.\n\nRecent tools like GitHub Copilot, which are powered by Large Language Models (LLMs), have succeeded in offering high-quality solutions to localized coding problems. Repository-level coding tasks are more involved and cannot be solved directly using LLMs, since code within a repository is inter-dependent and the entire repository may be too large to fit into the prompt. We frame repository-level coding as a planning problem and present a task-agnostic framework, called \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n to solve it. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n synthesizes a multi-step chain of edits (plan), where each step results in a call to an LLM on a code location with context derived from the entire repository, previous code changes and task-specific instructions. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n is based on a novel combination of an incremental dependency analysis, a change may-impact analysis and an adaptive planning algorithm.\n\nWe evaluate the effectiveness of \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n on two repository-level tasks: package migration (C#) and temporal code edits (Python). Each task is evaluated on multiple code repositories, each of which requires inter-dependent changes to many files (between 2–97 files). Coding tasks of this level of complexity have not been automated using LLMs before. Our results show that \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n has better match with the ground truth compared to baselines. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n is able to get 5/6 repositories to pass the validity checks (e.g., to build without errors and make correct code edits) whereas the baselines (without planning but with the same type of contextual information as \n����𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n) cannot get any of the repositories to pass them. We will release our data and evaluation scripts at https://aka.ms/CodePlan.\n\nAutomated coding, repositories, LLMs, static analysis, plan, chain of edits\n†copyright: acmcopyright\n†journalyear: 2018\n†doi: XXXXXXX.XXXXXXX\n†conference: Make sure to enter the correct conference title from your rights confirmation emai; June 03–05, 2018; Woodstock, NY\n†price: 15.00\n†isbn: 978-1-4503-XXXX-X/18/06\n†copyright: acmcopyright\n†journalyear: 2024\n†doi: XXXXXXX.XXXXXXX\n†price: 15.00\n†isbn: 978-1-4503-XXXX-X/18/06\n†ccs: Computing methodologies Planning under uncertainty\n†ccs: Software and its engineering Software maintenance tools\n†ccs: Software and its engineering Software evolution\n†ccs: Software and its engineering Automatic programming\n1.Introduction\n\nWe use a Complex Numbers library that had the following edit -\n\n+ class Complex {\n+   float real;\n+   float imag;\n+   dict<string, string> metadata;\n+ }\n- tuple<float, float> create_complex(float a, float b)\n+ Complex create_complex(float a, float b, dict metadata)\n\nModify the code repository in accordance with this change.\n\nFigure 1.Task instruction to migrate a code repository due to an API change in the Complex Numbers library.\nFigure 2.Overview of \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n.\n\nThe remarkable generative abilities of Large Language Models (LLMs) (Brown et al., 2020; Chen et al., 2021; Chowdhery et al., 2022; Fried et al., 2022; OpenAI, 2023; Touvron et al., 2023) have opened new ways to automate coding tasks. Tools built on LLMs, such as Amazon Code Whisperer (Amazon Web Services, Inc., 2023), GitHub Copilot (Github, Inc., 2023) and Replit (Replit, Inc., 2023), are now widely used to complete code\n\ngiven a natural language intent and context of surrounding code, and also to perform code edits based on natural language instructions (Wilson-Thomas, [n. d.]). Such edits are typically done for small regions of code such as completing or editing the current line, or the body of the entire method.\n\nWhile these tools help with the ”inner loop” of software engineering where the developer is coding in the editor and editing a small region of code, there are several tasks in the ”outer loop” of software engineering that involve the entire code repository. For example, if our code repository uses a library \n𝐿\n, and the API of library \n𝐿\n changes from version \n𝑣\n𝑛\n to version \n𝑣\n𝑛\n+\n1\n, we need to migrate our code repository to correctly invoke the revised version. Such a migration task involves making edits not only to all the regions of repository that make calls to the relevant APIs in library \n𝐿\n, but also to regions of the repository (across file boundaries) having transitive syntactic and semantic dependencies on the updated code.\n\ntuple<tuple<float, float>, dict> func(float a, float b) {\n  string timestamp = GetTimestamp(DateTime.Now);\n   var c = (create_complex(a,b), new Dictionary<string, string>()\"time\", timestamp);\n  return c;\n}\n \t\nComplex func(float a, float b) {\n  String timestamp = GetTimestamp(DataTime.Now);\n  dict_metadata = new Dictionary<string, string>(){\"time\", timestamp};\n  Complex c = create_complex(a, b, metadata);\n  return c;\n}\n\n(a) Create.cs - Original\t(b) Create.cs - Modified (seed edit)\n\nvoid process(float a, float b, float k) {\n  var c = func(a, b);\n  Console.WriteLine(c[0][0], c[0][1]);\n  float norm = compute_norm(c[0][0], c[0][1]);\n  Console.WriteLine(norm * k);\n}\n \t\nvoid process(float a, float b, float k) {\n  Complex c = func(a, b);\n  Console.WriteLine(c.real, c.imag);\n  float norm = compute_norm(c.real, c.imag);\n  Console.WriteLine(norm * k);\n}\n\n(c) Process.cs - Original\t(d) Process.cs - Modified (derived edit)\nFigure 3.Relevant code snippets from our repository.\n\nThis is illustrated in Figure 2, which shows a change in the API for a Complex Numbers library. Our task is to migrate our code repository in accordance with this change. The left side of Figure 3 shows relevant parts of our code repository that use the Complex Numbers library. Specifically, the file Create.cs has the method func, which invokes the create_complex method from the library, and Process.cs has the method process which invokes func.\n\nWe can pass the task description from Figure 2 and the body of func to an LLM to generate the revised code for func as shown in the right side of Figure 3. As seen, the LLM has correctly edited the invocation to the create_complex API so that it returns an object of type Complex instead of a tuple of two floating point values. Note that this edit has resulted in a change to the signature of the method func – it now returns an object of type Complex. This necessitates changes to callers of method func such as the process method in file Process.cs, shown in the left-bottom of Figure 3. Without a suitable change to the body of the process method, our code does not build! A suitable change to the process method which gets the repository to a consistent state, so that it builds without errors, is shown in the bottom-right of Figure 3.\n\nProblem Formulation. The migration task above is representative of a family of tasks that involve editing an entire code repository for various purposes such as fixing error reports from static analysis or testing, fixing a buggy coding pattern, refactoring, or adding type annotations or other specifications. Each of these tasks involves a set of seed specifications such as the one shown in Figure 2, which are starting points for the code editing task. These seed specifications typically trigger other editing requirements on code, and such requirements need to be propagated across dependencies in the code repository to perform other edits across the repository to complete the coding task. Typically, such propagation of edits across dependencies is done manually.\n\nOur goal is to construct a repository-level coding system, which automatically generates derived specifications for edits such as one required for the process method in Figure 3, in order to get the repository to a valid state. Here, validity is defined with respect to an oracle, which can be instantiated to various ways of enforcing repository-level correctness conditions such as building without errors, passing static analysis, passing a type system or a set of tests, or passing a verification tool. We define an LLM-driven repository-level coding task as follows:\n\nLLM-driven Repository-level Coding Task\nGiven a start state of a repository \n𝑅\n𝑠\n​\n𝑡\n​\n𝑎\n​\n𝑟\n​\n𝑡\n, a set of seed edit specifications \nΔ\n𝑠\n​\n𝑒\n​\n𝑒\n​\n𝑑\n​\n𝑠\n, an oracle \nΘ\n such that \nΘ\n​\n(\n𝑅\n𝑠\n​\n𝑡\n​\n𝑎\n​\n𝑟\n​\n𝑡\n)\n=\n𝖳𝗋𝗎𝖾\n, and an LLM \n𝐿\n, the goal of an LLM-driven repository-level coding task is to reach a repository state \n𝑅\n𝑡\n​\n𝑎\n​\n𝑟\n​\n𝑔\n​\n𝑒\n​\n𝑡\n=\n𝐸\n​\n𝑥\n​\n𝑒\n​\n𝑐\n​\n𝑢\n​\n𝑡\n​\n𝑒\n​\n𝐸\n​\n𝑑\n​\n𝑖\n​\n𝑡\n​\n𝑠\n​\n(\n𝐿\n,\n𝑅\n𝑠\n​\n𝑡\n​\n𝑎\n​\n𝑟\n​\n𝑡\n,\n𝑃\n)\n where \n𝑃\n is a chain of edit specifications from \nΔ\n𝑠\n​\n𝑒\n​\n𝑒\n​\n𝑑\n​\n𝑠\n∪\nΔ\n𝑑\n​\n𝑒\n​\n𝑟\n​\n𝑖\n​\n𝑣\n​\n𝑒\n​\n𝑑\n where \nΔ\n𝑑\n​\n𝑒\n​\n𝑟\n​\n𝑖\n​\n𝑣\n​\n𝑒\n​\n𝑑\n is a set of derived edit specifications so that \nΘ\n​\n(\n𝑅\n𝑡\n​\n𝑎\n​\n𝑟\n​\n𝑔\n​\n𝑒\n​\n𝑡\n)\n=\n𝖳𝗋𝗎𝖾\n.\n\nProposed Solution. In this paper, we propose a method to compute derived specifications by framing (LLM-driven) repository-level coding as a planning problem. Automated planning (Ghallab et al., 2004; Russell, 2010) aims to solve multi-step problems, where each step executes one action among many alternatives towards reaching a target state. It is used in a wide range of areas such as motion planning (La Valle, 2011), autonomous driving (González et al., 2015), robotics (Karpas and Magazzeni, 2020) and theorem proving (Bundy, 1988).\n\nWe present a task-agnostic framework, called \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n, which synthesizes a multi-step plan to solve the repository-level coding task. As shown in Figure 2, the input to \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n is a repository, a task with seed specifications expressed through a natural language instruction or a set of initial code edits, a correctness oracle and an LLM. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n constructs a plan graph where each node in the graph identifies a code edit obligation that the LLM needs to discharge and an edge indicates that the target node needs to be discharged consequent to the source node. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n monitors the code edits and adaptively extends the plan graph. The edits \nΔ\n𝑠\n​\n𝑒\n​\n𝑒\n​\n𝑑\n​\n𝑠\n follow from the task description, whereas the edits \nΔ\n𝑑\n​\n𝑒\n​\n𝑟\n​\n𝑖\n​\n𝑣\n​\n𝑒\n​\n𝑑\n are identified and contextualized based on a novel combination of an incremental dependency analysis, a change may-impact analysis and an adaptive planning algorithm. The merge block merges the code generated by the LLM into the repository. Once all the steps in a plan are completed, the repository is analyzed by the oracle. The task is completed if the oracle validates the repository. If it finds errors, the error reports are used as seed specifications for the next round of plan generation and execution.\n\nConsider again, the example API migration task specified in Figure 2 on code in Figure 3. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n performs the edit of the method func using the instruction in Figure 2 as a seed specification. By analyzing the code change between Figure 3(a)–(b), it classifies the change as an escaping change as it affects signature of method func. The change may-impact analysis identifies that the caller(s) of func may be affected and hence, the adaptive planning algorithm uses caller-callee dependencies to infer a derived specification to edit the method process, which invokes func. Both the seed and derived changes are executed by creating suitable prompts for an LLM and the resulting code repository passes the oracle, i.e., builds without errors. Note that this is a simple example with only one-hop change propagation. In practice, the derived changes can themselves necessitate other changes transitively and \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n handles such cases.\n\nA simpler alternative to our planning is to use the oracle to infer derived specifications. For example, the build system can find the error in the process method after the seed change is made in Figure 3. This has important limitations. First, not all changes induce build errors even though they result in behavioral changes, e.g., changing the return value from True to False without changing the return type. Second, the build system is agnostic to cause-effect relationship when code breaks. For example, if the signature of an overriding method is changed as per the seed specification then a similar change is needed in the corresponding virtual method. However, the build system (when run on the intermediate, inconsistent snapshot of the repository) blames the overriding method for not conforming to the virtual method. Naïvely trying to fix the build error would end up reverting the seed change. The static analysis and planning components of \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n overcome these limitations. We experimentally compare \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n against a baseline that uses a build system to iteratively identify breaking changes and uses an LLM to fix them. Our quantitative and qualitative results show that \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n is superior to this kind of oracle-guided repair technique.\n\nContributions. To the best of our knowledge, the problem of monitoring the effects of code edits made by an LLM to a repository and systematically planning a chain of inter-dependent edits has not been identified and solved before.\n\nIn the space of repository-level coding tasks, two types of contexts have been found to be useful for prompting LLMs: (1) spatial context to provide cross-file information to the model using static analysis (Pashakhanloo et al., 2022; Shrivastava et al., 2022; Ding et al., 2022; Wei et al., 2023b; Pei et al., 2023b; Agrawal et al., 2023; Shrivastava et al., 2023; Liu et al., 2023) or retrieval (Xu et al., 2021; Zhang et al., 2023b), and (2) temporal context to condition the predictions on the history of edits to the repository (Brody et al., 2020; Reid and Neubig, 2022; Gupta et al., 2023; Wei et al., 2023a). Since \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n monitors the code changes and maintains a repository-wide dependency graph, we provide both these forms of contexts in a unified framework. The existing techniques assume that the next edit location is provided by the developer and do not account for the effect of an edit on the dependent code. In contrast, by inferring the impact of each change, \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n propagates the changes to dependent code, paving a way to automate repository-level coding tasks through chain of edits.\n\nIn summary, we make the following contributions in this paper:\n\n(1) \n\nWe are the first to formalize the problem of automating repository-level coding tasks using LLMs, which requires analyzing the effects of code changes and propagating them across the repository. There are currently no systematic and scalable solutions to this problem.\n\n(2) \n\nWe frame repository-level coding as a planning problem and design a task-agnostic framework, called \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n, based on a novel combination of an incremental dependency analysis, a change may-impact analysis and an adaptive planning algorithm. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n synthesizes a multi-step chain of edits (plan) to be actuated by an LLM.\n\n(3) \n\nWe experiment with two repository-level coding tasks using the gpt-4-32k model: package migration for C# repositories and temporal code edits for Python repositories. We compare against baselines that use the oracles (a build system for C# and a static type checker for Python) for identifying derived edit specifications (in contrast to planning used in \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n). We use the same contextualization method as \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n in the baselines.\n\n(4) \n\nOur results show that \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n has better match with the ground truth compared to baselines. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n is able to get 5/6 repositories to pass the validity checks, whereas the baselines cannot get any of the repositories to pass them. Except for the 2 proprietary repositories, we will release our data and evaluation scripts at https://aka.ms/CodePlan.\n\n2.Design\n\nIn this section, we first give an overview of the \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n algorithm for automating repository-level coding tasks (Section 2.1). We then present the static analysis (Section 2.2) and the adaptive planning and plan execution (Section 2.3) components of \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n.\n\n2.1.The \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n Algorithm\n1/* Inputs: R is the source code of a repository, Delta_seeds is a set of seed edit specifications, Theta is an oracle and L is an LLM. */\n3CodePlan(R, Delta_seeds, Theta, L):\n4  let mutable G: PlanGraph = null in  \n5  let mutable D: DependencyGraph = ConstructDependencyGraph(R) in \n6    while Delta_seeds is not empty \n7      IntializePlanGraph(G, Delta_seeds) \n8      AdaptivePlanAndExecute(R, D, G) \n9      Delta_seeds = Theta(R) \n11InitializePlanGraph(G, Delta_seeds): \n12  for each \n⟨\nB, I\n⟩\n in Delta_seeds\n13    AddRoot(G, \n⟨\nB, I, Pending\n⟩\n) \n15AdaptivePlanAndExecute(R, D, G): \n16  while G has Nodes with Pending status\n17    let \n⟨\nB, I, Pending\n⟩\n = GetNextPending(G) in\n18    // First step: extract fragment of code\n19    let Fragmemt = ExtractCodeFragment(B, R, I) in \n20    // Second step: gather context of the edit\n21    let Context = GatherContext(B, R, D) in  \n22    // Third step: use the LLM to get edited code fragment\n23    let Prompt = MakePrompt(Fragment, I, Context) in \n24    let NewFragment = InvokeLLM(L, Prompt) in \n25    // Fourth step: merge the updated code fragment into R\n26    let R = Merge(NewFragment, B, R) in \n27    let Labels = ClassifyChanges(Fragment, NewFragment) in \n28    let D’ = UpdateDependencyGraph​(D, Labels, Fragment, NewFragment, B) in \n29    // Fifth step: adaptively plan and propogate the effect of the edit on dependant code\n30    let BlockRelationPairs ​​​=​​ GetAffectedBlocks(Labels, B, D, D’) in \n31      MarkCompleted(B, G) \n32      for each \n⟨\nB’, rel\n⟩\n in BlockRelationPairs\n33        let N = GetNode(B) in\n34        let M = SelectOrAddNode(B’, Nil, Pending) in \n35          AddEdge(G, M, N, rel) \n36    D := D’\n38GatherContext(B, R, D): \n39  let SC = GetSpatialContext(B, R) in\n40  let TC = GetTemporalContext(G, B) in\n41    (SC, TC) \nAlgorithm 1 The \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n algorithm to automate repository-level coding tasks. The data structures and functions in Cyan and Orchid are explained in Section 2.2– 2.3 respectively.\n\nThe \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n algorithm (Algorithm 1) takes four inputs: (1) the source code of a repository \n𝑅\n, (2) a set of seed edit specifications for the task in hand, \nΔ\n𝑠\n​\n𝑒\n​\n𝑒\n​\n𝑑\n​\n𝑠\n, (3) an oracle, \nΘ\n, and (4) an LLM, \n𝐿\n.\n\nThe core data structure maintained by the algorithm is a plan graph \n𝐺\n, a directed acyclic graph with multiple root nodes (line 4). Each node in the plan graph is a tuple \n⟨\n𝐵\n,\n𝐼\n,\n𝑆\n​\n𝑡\n​\n𝑎\n​\n𝑡\n​\n𝑢\n​\n𝑠\n⟩\n, where \n𝐵\n is a block of code (that is, a sequence of code locations) in the repository \n𝑅\n, \n𝐼\n is an edit instruction (along the lines of the example shown in Figure 2),\n\nand \n𝑆\n​\n𝑡\n​\n𝑎\n​\n𝑡\n​\n𝑢\n​\n𝑠\n is either \n𝑝\n​\n𝑒\n​\n𝑛\n​\n𝑑\n​\n𝑖\n​\n𝑛\n​\n𝑔\n or \n𝑐\n​\n𝑜\n​\n𝑚\n​\n𝑝\n​\n𝑙\n​\n𝑒\n​\n𝑡\n​\n𝑒\n​\n𝑑\n.\n\nThe \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n algorithm also maintains a dependency graph \n𝐷\n (line 5). Figure 4 illustrates the dependency graph structure. We will discuss it in details in Section 2.2.1. For now, it suffices to know that the dependency graph \n𝐷\n represents the syntactic and semantic dependency relations between code blocks in the repository \n𝑅\n.\n\nThe loop at lines 6–9 is executed until \nΔ\n𝑠\n​\n𝑒\n​\n𝑒\n​\n𝑑\n​\n𝑠\n is non-empty. Line 7 calls the InitializePlanGraph function (lines 11–13) that adds all the changes in \nΔ\n𝑠\n​\n𝑒\n​\n𝑒\n​\n𝑑\n​\n𝑠\n as root nodes of the plan graph. Each edit specification comprises of a code block \n𝐵\n and an edit instruction \n𝐼\n.\n\nThe status is set to pending for the root nodes (line 13). The function AdaptivePlanAndExecute is called at line 8 which executes the plan, updates the dependency graph with each code change and extends the plan as necessary. Once the plan graph is completely executed, the oracle \nΘ\n is run on the repository. It returns error locations and diagnostic messages which form \nΔ\n𝑠\n​\n𝑒\n​\n𝑒\n​\n𝑑\n​\n𝑠\n for the next round. If the repository passes the oracle’s checks then it returns an empty set and the \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n algorithm terminates.\n\nWe now discuss AdaptivePlanAndExecute, which is the main work horse. It iteratively picks each pending node and processes it. Processing a pending node with an edit specification for a block \n𝐵\n with edit instruction \n𝐼\n involves the following five steps:\n\n(1) \n\nThe first step (line 19) is to extract the fragment of code to edit. Simply extracting code of the block \n𝐵\n loses information about relationship of \n𝐵\n with the surrounding code. Keeping the entire file on the other hand takes up prompt space and is often unnecessary. We found the surrounding context is most helpful when a block belongs to a class. For such blocks, we sketch the enclosing class. That is, in addition to the code of block \n𝐵\n, we also keep declarations of the enclosing class and its members. As we discuss later, this sketched representation also helps us merge the LLM’s output into a source code file more easily.\n\n(2) \n\nThe second step (line 21) is to gather the context of the edit. The context of the edit (line 38–41) consists of (a) spatial context, which contains related code such as methods called from the block \n𝐵\n, and (b) temporal context, which contains the previous edits that caused the need to edit the block \n𝐵\n. The temporal context is formed by edits along the paths from the root nodes of the plan graph to \n𝐵\n.\n\n(3) \n\nThe third step (lines 23–24) constructs a prompt for the edit using the fragment extracted in the first step, the instruction \n𝐼\n from the edit specification and the context extracted in the second step, and invokes the LLM using the prompt to get the edited code fragment.\n\n(4) \n\nThe fourth step (lines 26–28) merges the edited code back into the repository. Since the code is updated, many dependency relationships such as caller-callee, class hierarchy, etc. may need to change, and hence, this step also updates the dependency graph \n𝐷\n.\n\n(5) \n\nThe fifth and final step (lines 30–35) does adaptive planning to propagate the effects of the current edit on dependant code blocks. This involves classifying the change in the edited block, and depending on the type of change, picking the right dependencies in the dependency graph to traverse and locate affected blocks. For instance, if the edit of a method \n𝑚\n in the current block \n𝐵\n involves update to the signature of the method, then all callers of \n𝑚\n get affected (the scenario in Figure 3). For each affected block \n𝐵\n′\n and the dependency relation rel connecting \n𝐵\n to \n𝐵\n′\n in the dependency graph, we get a pair \n⟨\n𝐵\n′\n,\nrel\n⟩\n. If a node exists for \n𝐵\n′\n in the plan graph and it is pending, then we add an edge from \n𝐵\n to \n𝐵\n′\n labeled with rel to the plan graph. Otherwise, the edge is added to a newly created node for \n𝐵\n′\n (line 34). The block \n𝐵\n is marked as completed (line 31).\n\n2.2.Static Analysis Components\nFigure 4.Illustration of the dependency graph annotated with relations as the edge labels.\n\nWe now turn our attention to the static analysis components used in \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n. We will cover all the data structures and functions in Cyan background from Algorithm 1.\n\n2.2.1.Incremental Dependency Analysis\n\nAn LLM can be provided a code fragment and an instruction to edit it in a prompt. While the LLM may perform the desired edit accurately, analyzing the impact of the edit on the rest of the repository is outside the scope of the LLM call. We believe static analysis is well-suited to do this and propose an incremental dependency analysis for the same.\n\nDependencyGraph. Dependency analysis (Aho et al., 2007) is used for tracking syntactic and semantic relations between code elements. In our case, we are interested in relations between import statements, methods, classes, field declarations and statements (excluding those that operate only on variables defined locally within the enclosing method). Formally, a dependency graph D \n=\n(\n𝑁\n,\n𝐸\n)\n where \n𝑁\n is a set of nodes representing the code blocks mentioned above and \n𝐸\n is a set of labeled edges where the edge label gives the relation between the source and target nodes of the edge. Figure 4 illustrates all the relations we track as labeled edges. The relations include (1) syntactic relations (ParentOf and ChildOf, Construct and ConstructedBy) between a block \n𝑐\n and the block \n𝑝\n that encloses \n𝑐\n syntactically; a special case being a constructor and its enclosing class related by Construct and ConstructedBy, (2) import relations (Imports and ImportedBy) between an import statement and statements that use the imported modules, (3) inheritance relations (BaseClassOf and DerivedClassOf) between a class and its superclass, (4) method override relations (Overrides and OverridenBy) between an overriding method and the overriden method, (5) method invocation relations (Calls and CalledBy) between a statement and the method it calls, (6) object instantiation relations (Instantiates and InstantiatedBy) between a statement and the constructor of the object it creates, and (7) field use relations (Uses and UsedBy) between a statement and the declaration of a field it uses.\n\nConstructDependencyGraph. The dependency relations are derived across the source code spread over the repository through static analysis. We represent the source code of a repository as a forest of abstract syntax trees (ASTs) and add the dependency edges between AST sub-trees. A file-local analysis derives the syntactic and import relations. All other relations require an inter-class, inter-procedural analysis that can span file boundaries. In particular, we use the class hierarchy analysis (Dean et al., 1995) for deriving the semantic relations.\n\nAtomic Change\n \t\nLabel\n\t\nDependency Graph Update\n\t\nChange May-Impact Analysis\n\nModification Changes\n\nBody of method M\n \t\nMMB\n\t\nRecompute the edges incident on the statements in the method body.\n\t\nIf an escaping object is modified then Rel(D, M, CalledBy) else Nil.\n\n\nSignature of method M\n \t\nMMS\n\t\nRecompute the edges incident on the method.\n\t\nRel(D, M, CalledBy), Rel(D, M, Overrides), Rel(D, M, OverriddenBy), Rel(\nD\n′\n, M, Overrides), Rel(\nD\n′\n, M, OverriddenBy)\n\n\nField F in class C\n \t\nMF\n\t\nRecompute the edges incident on the field.\n\t\nRel(D, F, UsedBy), Rel(D, C, ConstructedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)\n\n\nDeclaration of class C\n \t\nMC\n\t\nRecompute the edges incident on the class.\n\t\nRel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf), Rel(\nD\n′\n, C, BaseClassOf), Rel(\nD\n′\n, C, DerivedClassOf)\n\n\nSignature of constructor of class C\n \t\nMCC\n\t\nNo change.\n\t\nRel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)\n\n\nImport/Using statement I\n \t\nMI\n\t\nRecompute the edges incident on the import statement.\n\t\nRel(D, I, ImportedBy)\n\nAddition Changes\n\nMethod M in class C\n \t\nAM\n\t\nAdd new node and edges by analyzing the method. If C.M overrides a base class method B.M then redirect the Calls/CalledBy edges from B.M to C.M if the receiver object is of type C.\n\t\nRel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf), Rel(\nD\n′\n, M, CalledBy)\n\n\nField F in class C\n \t\nAF\n\t\nAdd new node and edges by analyzing the field declaration.\n\t\nRel(D, C, ConstructedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)\n\n\nDeclaration of class C\n \t\nAC\n\t\nAdd new node and edges by analyzing the class declaration.\n\t\nNil\n\n\nConstructor of class C\n \t\nACC\n\t\nAdd new node and edges by analyzing the constructor.\n\t\nRel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)\n\n\nImport/Using statement I\n \t\nAI\n\t\nAdd new node and edges by analyzing the import statement.\n\t\nNil\n\nDeletion Changes\n\nMethod M in class C\n \t\nDM\n\t\nRemove the node for M and edges incident on M. If C.M overrides a base class method B.M then redirect the Calls/CalledBy edges from C.M to B.M if the receiver object is of type C.\n\t\nRel(D, M, CalledBy), Rel(D, M, Overrides), Rel(D, M, OverriddenBy)\n\n\nField F in class C\n \t\nDF\n\t\nRemove the node of the field and edges incident on it.\n\t\nRel(D, F, UsedBy), Rel(D, C, ConstructedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)\n\n\nDeclaration of class C\n \t\nDC\n\t\nRemove the node of the class and edges incident on it.\n\t\nRel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)\n\n\nConstructor of class C\n \t\nDCC\n\t\nRemove the edges incident on the class due to object instatiations using the constructor.\n\t\nRel(D, C, InstantiatedBy), Rel(D, C, BaseClassOf), Rel(D, C, DerivedClassOf)\n\n\nImport/Using statement I\n \t\nDI\n\t\nRemove the node of the import statement and edges incident on it.\n\t\nRel(D, I, ImportedBy)\nTable 1.Rules for updating the dependency graph and for change may-impact analysis for atomic changes. We refer to the dependency graphs before and after the updates by D and \nD\n′\n respectively.\n\nClassifyChanges. As discussed in Section 2.1, in the fourth step, \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n merges the code generated by the LLM into the repository. By pattern-matching the code before and after, we classify the code changes. Table 1 (the first and second columns) gives the types of atomic changes and their labels. Broadly, the changes are organized as modification, addition and deletion changes, and further by which construct is changed. We distinguish between method body and method signature changes. Similarly, we distinguish between changes to a class declaration, to its constructor or to its fields. The changes to import statements or the statements that use imports are also identified. These are atomic changes. An LLM can make multiple simultaneous edits in the given code fragment, resulting in multiple atomic changes, all of which are identified by the ClassifyChanges function.\n\nUpdateDependencyGraph. As code generated by the LLM is merged, the dependency relations associated with the code at the change site are re-analyzed. Table 1 (the third column) gives the rules to update the dependency graph D to \nD\n′\n based on the labels inferred by ClassifyChanges. For modification changes, we recompute the relations of the changed code except for constructors. A constructor is related to its enclosing class by a syntactic relation which does not have to be recomputed. For addition changes, new nodes and edges are created for the added code. Edges corresponding to syntactic relations are created in a straightforward manner. If a change simultaneously adds an element (an import, a method, a field or a class) and its uses, we create a node for the added element before analyzing the statements that use it. Addition of a method needs special handling as shown in the table: if an overriding method C.M is added then the Calls/CalledBy edges incident on the matching overriden method B.M are redirected to C.M if the call is issued on a receiver object of type C. The deletion of an overriding method requires an analogous treatment as stated in Table 1. All other deletion changes require removing nodes and edges as stated in the table.\n\n2.2.2.Change May-Impact Analysis\n\nIn the fifth step, \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n identifies the code blocks that may have been impacted by the code change by the LLM. Let Rel(D, B, rel) be the set of blocks that are connected to a block B via relation rel in the dependency graph D. Let D and \nD\n′\n be the dependency graph before and after the updates in Table 1.\n\nGetAffectedBlocks. The last column in Table 1 tells us how to identify blocks affected by a code change for each type of change. When the body of a method M is edited, we perform escape analysis (Choi et al., 1999; Blanchet, 2003) to identify if any object accessible in the callers of M (an escaping object) has been affected by the change. If yes, the callers of M (identified through Rel(D, M, CalledBy)) are identified as affected blocks. Otherwise, the change is localized to the method and there are no affected blocks. If the signature of a method is edited, the callers and methods related to it through method-override relation in the inheritance hierarchy are affected. The signature change itself can affect the Overrides and OverridenBy relations, e.g., addition or deletion of the @Override access modifier. Therefore, the blocks related by these relations in the updated dependency graph \nD\n′\n are also considered as affected as shown in Table 1 (the row with MMS label). When a field F of a class C is modified, the statements that use F, the constructors of C and sub/super-classes of C are affected. When a class is modified, the methods that instantiate it and its sub/super-classes as per D and \nD\n′\n are affected. A modification to a constructor has a similar rule except that such a change does not change inheritance relations and hence, only D is required. When an import statement I is modified, the statements that use the imported module are affected.\n\nThe addition and deletion changes are less complex than the modification changes, and their rules are designed along the same lines as discussed above. In the interest of space, we do not explain each of them step-by-step. We assume that there is no use of a newly added class or an import in the code. Therefore, adding them does not result in any affected blocks. In our experiments, we have found the rules in Table 1 to be adequate. However, \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n can be easily configured to accommodate variations of the rules in Table 1 if necessary.\n\n2.3.Adaptive Planning and Plan Execution\n\nWe now discuss the data structures and functions from Algorithm 1 in the Orchid background.\n\n2.3.1.Adaptive Planning\n\nHaving identified the affected blocks (using GetAffectedBlocks), \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n creates change obligations that need to be discharged using an LLM to make the dependent code consistent with the change. As discussed in Section 2.1, this is an iterative process.\n\nPlanGraph. A plan graph P \n=\n(\n𝑂\n,\n𝐶\n)\n is a directed acyclic graph with a set of obligations \n𝑂\n, each of which is a triple \n⟨\n𝐵\n,\n𝐼\n,\n𝑠\n​\n𝑡\n​\n𝑎\n​\n𝑡\n​\n𝑢\n​\n𝑠\n⟩\n where B is a block, I is an instruction and status is either pending or completed. An edge in \n𝐶\n records the cause, the dependency relation between the blocks in the source and target obligations. In other words, the edge label identifies which Rel clause in a change may-impact rule in Table 1 results in creation of the target obligation.\n\nExtractCodeFragment. As discussed in the first step in Section 2.1, simply extracting code for a block B is sub-optimal as it loses context. The ExtractCodeFragment function takes the whole class the code block belongs to, keeps the complete code for B and retains only declarations of the class and other class members. We found this to be useful because the names and types of the class and other members provide additional context to the LLM. Often times the LLM needs to make multiple simultaneous changes. For example, in some of our case studies, the LLM has to add a field declaration, take an argument to a constructor and use it within the constructor to initialize the field. Providing the sketch of the surrounding code as a code fragment to the LLM allows the LLM to make these changes at the right places. The code fragment extraction logic is implemented by traversing the AST and ”folding” away the subtrees (e.g., method bodies) that are sketched. As stated in Section 1, this sketched representation also allows us to place the LLM generated code back into the AST without ambiguity, even when there are multiple simultaneous changes.\n\nGetSpatialContext. Spatial context in CodePlan refers to the arrangement and relationships of code blocks within a codebase, helping understand how classes, functions, variables, and modules are structured and interact. It’s crucial for making accurate code changes. CodePlan utilizes the dependency graph to extract spatial context, representing code as nodes and their relationships as edges. This graph enables CodePlan to navigate codebases, identify relevant code blocks, and maintain awareness of their spatial context. As a result, when generating code edits, the dependency graph empowers CodePlan to make context-aware code modifications that are consistent with the code’s spatial organization, enhancing the accuracy and reliability of its code editing capabilities.\n\nGetTemporalContext. The plan graph records all change obligations and their inter-dependences. Extracting temporal context is accomplished by linearizing all paths from the root nodes of the plan graph to the target node. Each change is a pair of the code fragments before and after the change. The temporal context also states the ”causes” (recorded as edge labels) that connect the target node with its predecessor nodes. For example, if a node A is connected to B with a CalledBy edge, then the temporal context for B is the before/after fragments for A and a statement that says that ”B calls A”, which helps the LLM understand the cause-effect relation between the latest temporal change (change to A) and the current obligation (to make a change to B).\n\n2.3.2.Plan Execution\n\n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n iteratively selects a pending node in the plan graph and invokes an LLM to discharge the change obligation.\n\nMakePrompt. Having extracted the code fragment to be edited along with the relevant spatial and temporal context, we construct a prompt to pass to the LLM with the structure given below. We open with the task specific instructions \np\n1\n followed by listing the edits made in the repository so far \np\n2\n that are relevant to the fragment being edited. The next section \np\n3\n notes how each of the fragments present in \np\n2\n are related to the fragment to be edited. This is followed by the spatial context \np\n4\n and the fragment to the edited \np\n5\n.\n\nPrompt Template\np\n1\nTask Instructions: Your task is to \n…\n\n\np\n2\nEarlier Code Changes (Temporal Context): These are edits that have been made in the code-base previously -\n\nEdit 1:\n    Before: <<code_before>>\n    After: <<code_after>>\n\n⋯\n\n\np\n3\nCauses for Change: The change is required due to -\n\n<<code_to_be_edited>> is related to <<code_changed_earlier>> by <<cause>>\n⋯\n\n\np\n4\nRelated Code (Spatial Context): The following code maybe related -\n\n<<related_code_block-1>>\n⋯\n\n\np\n5\nCode to be Changed Next: The existing code is given below -\n\n<<code_to_be_edited>>\n\nEdit the ”Code to be Changed Next” and produce ”Changed Code” below. Edit the ”Code to be Changed Next” according to the ”Task Instructions” to make it consistent with the ”Earlier Code Changes”, ”Causes for Change” and ”Related Code”. If no changes are needed, output ”No changes.”\n\nOracle and Plan Iterations. Once all the nodes in the plan graph are marked as completed and no new nodes are added, an iteration of repository-level code edits is completed. As shown in Figure 2, the oracle is invoked on the repository. If the oracle flags any errors (e.g., build errors), the error locations and diagnostic messages are added as seed changes for the next iteration and the adaptive planning resumes once again. If the oracle does not flag any errors, \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n terminates.\n\n3.Implementation\n\nIn this section, we provide a detailed overview of the implementation components that constitute the core of our method.\n\nDependency Graph Construction. At the core of the CodePlan methodology lies the Dependency Graph, which is instrumental in representing the intricate relationships between code blocks. To build this Dependency Graph from a code repository, we adopt a systematic approach. Initially, we parse all the code files within the repository, utilizing the tree-sitter library (Brunsfeld et al., 2023) to generate an AST-like structure. This structured representation simplifies the identification of various fundamental code blocks within the codebase. For instance, Figure 5 exemplifies an AST structure for a C# code snippet produced by tree-sitter. Code blocks are identified at different levels, including Classes, Methods, import statements, and non-class expressions. For instance, in Figure 5, the subtree rooted at the class_declaration node corresponds to the SyncSubscriberTest class.\n\nFigure 5.AST structure for a C# code snippet produced by tree-sitter.\n\nRelation Identification in C#. In the context of C# repositories, the establishment of edges within the Dependency Graph involves the careful tracing of relationships within the AST. We have devised custom logic for each type of relationship outlined in Figure 4, encompassing vital connections such as caller-callee, overrides-overridden, base class-derived class, and others. To illustrate, for the Caller/Callee relationship, we search for invocation_expression nodes within the AST. Subsequently, we process the sub-tree beneath these nodes to resolve essential details such as the target class and the invoked method’s name. Armed with this information, we create Calls/CalledBy relation links between the code block initiating the method call and the corresponding method block within the target class. While we have implemented custom logic for these relations, it’s important to note that alternative dependency analysis tools for C# such as Language Servers for C# (LSP) (Omn, [n. d.]), CodeQL (Cod, [n. d.]), or similar solutions can also be integrated into our system, owing to its inherent flexibility.\n\nRelation Identification in Python. For Python repositories, we use Jedi (Jed, [n. d.]) - a static analysis tool which discovers references and declarations of symbols throughout the codebase. These capabilities are harnessed to identify edges in the Dependency Graph for relationships such caller-callee, overrides-overridden, and base class-derived class.\n\nIntegration of GPT-4 for Code Edits. CodePlan leverages the remarkable capabilities of GPT-4 (OpenAI, 2023) to perform code edits effectively. During the construction of input data for the edit model, we meticulously provide temporal context, spatial context, and the actual code to be edited in the form of code snippets. These code snippets represent classes or methods that contain the edit site and are meticulously structured in a sketched representation, as stated in Section 2.1. This sketched representation ensures that the model is enriched with a substantial context for each edit site, significantly enhancing the quality and accuracy of the edits it generates.\n\nLanguage Extensibility. While our current implementation proficiently supports C# and Python repositories, extending support to repositories in other programming languages is a straightforward endeavor. It primarily entails creating a dependency graph with the relations identified in Figure 4 and incorporating it into the CodePlan framework, thereby allowing for seamless adaptation to a diverse array of programming languages.\n\n4.Related Work\n\nLLMs for Coding Tasks. A multitude of LLMs (Ahmad et al., 2021; Wang et al., 2021; Wang and Komatsuzaki, 2021; Brown et al., 2020; Austin et al., 2021; Chen et al., 2021; Black et al., 2022; Xu et al., 2022; Chowdhery et al., 2022; Fried et al., 2022; OpenAI, 2023; Touvron et al., 2023) have been trained on large-scale corpora of source code and natural language text. These have been used to accomplish a variety of coding tasks. A few examples of their use include program synthesis (Li et al., 2022; Nijkamp et al., 2023), program repair (Xia et al., 2023; Jin et al., 2023; Ahmed and Devanbu, 2023), vulnerability patching (Pearce et al., 2022), inferring program invariants (Pei et al., 2023a), test generation (Schäfer et al., 2023) and multi-task evaluation (Tian et al., 2023). However, these investigations are performed on curated examples that are extracted from their repositories and are meant to be accomplished with independent invocations of the LLM. We consider a different class of tasks posed at the scale of code repositories, where an LLM is called multiple times on different examples which are inter-dependent. We monitor the results of each LLM invocation within the repository-wide context to identify future code change obligations to get the repository to a consistent state, e.g., where the repository is free of build or runtime errors.\n\nAutomated Planning. Automated planning (Ghallab et al., 2004; Russell, 2010) is a well-studied topic in AI. Online planning (Russell, 2010) is used when the effect of actions is not known and the state-space cannot be enumerated a priori. It requires monitoring the actions and plan extension. In our case, the edit actions are carried out by an LLM whose results cannot be predicted before-hand and the state-space is unbounded. As a consequence, our adaptive planning is an online algorithm where we monitor the actions and extend the plan through static analysis. In orthogonal directions, (Jiang et al., 2023) uses an LLM to derive a plan given a natural language intent before generating code to solve complex coding problems and (Zhang et al., 2023a) performs lookahead planning (tree search) to guide token-level decoding of code LMs. Planning in our work is based on analyzing dependency relations and changes to them as an LLM makes changes to a code repository.\n\nAnalysis of Code Changes. Static analysis is used for ensuring software quality. It is expensive to recompute the analysis results every time the code undergoes changes. The field of incremental program analysis offers techniques to recompute only the analysis results impacted by the change. Specialized algorithms have been developed for dataflow analysis (Ryder, 1983; Arzt and Bodden, 2014), pointer analysis (Yur et al., 1999), symbolic execution (Person et al., 2011), bug detection (McPeak et al., 2013) and type analysis (Busi et al., 2019). Program differencing (Apiwattanapong et al., 2004; Lahiri et al., 2012; Kim et al., 2012) and change impact analysis (Arnold and Bohner, 1996; Jashki et al., 2008) determine the differences in two program versions and the effect of a change on the rest of the program. The impact of changes has been studied for regression testing (Ren et al., 2004), analyzing refactorings (Dig et al., 2006) and assisting in code review (Alves et al., 2014; Ge et al., 2017). We analyze the code generated by an LLM and incrementally update the syntactic (e.g., parent-child) and dependency (e.g., caller-callee) relations. We further analyze the likely impact of those changes on related code blocks and create change obligations to be discharged by the LLM.\n\nSpatial and Temporal Contextualization. As discussed in the Introduction, LLMs benefit from relevant context derived from other files in the repository and from past edits. We provide both these pieces of information to the LLM by tracking the code changes and dependency relations.\n\nLearning Edit Patterns. Many approaches have been developed to learn edit patterns from past edits or commits in the form of rewrite rules (de Sousa et al., 2021), bug fixes (Andersen and Lawall, 2010; Bader et al., 2019), type changes (Ketkar et al., 2022), API migrations (Lamothe et al., 2020; Xu et al., 2019) and neural representations of edits (Yin et al., 2019). Approaches such as (Meng et al., 2011) and (Meng et al., 2013) synthesize context-aware edit scripts from user-provided examples and apply them in new contexts. Other approaches observe the user actions in an IDE to automate repetitive edits (Miltner et al., 2019) and temporally-related edit sequences (Zhang et al., 2022). We do not aim to learn edit patterns and we do not assume similarities between edits. Our focus is to identify effects of code changes made by an LLM and to guide the LLM towards additional changes that become necessary.\n\n5.Conclusions and Future Work\n\nIn this paper, we introduced \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n, a novel framework designed to tackle the challenges of repository-level coding tasks, which involve pervasive code modifications across large and inter-dependent codebases. \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n leverages incremental dependency analysis, change may-impact analysis, and adaptive planning to orchestrate multi-step edits guided by Large Language Models. We evaluated \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n on diverse code repositories with varying complexities and sizes, including both internal proprietary repositories and public GitHub repositories in C# and Python for migration and temporal edit tasks. Our results demonstrated that \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n outperforms baseline methods, achieving better alignment with the ground truth. In conclusion, \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n presents a promising approach to automating complex repository-level coding tasks, offering both productivity benefits and accuracy improvements. Its success in addressing these challenges opens up new possibilities for efficient and reliable software engineering practices.\n\nWhile \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n has shown significant promise, there are several avenues for future research and enhancements. First, we aim to expand its applicability to a broader range of programming languages and code artifacts, including configuration files, metadata, and external dependencies, to provide a more holistic solution for repository-level editing. Additionally, we plan to explore further customization of \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n’s change may-impact analysis. This could involve incorporating task-specific impact analysis rules, either through rule-based methods or more advanced machine learning techniques, to fine-tune its editing decisions for specific coding tasks. Furthermore, we will address the challenge of handling dynamic dependencies, such as data flow dependencies, complex dynamic dispatching (via virtual functions and dynamic castings), algorithmic dependencies (e.g., when input lists are expected to be sorted), and various execution dependencies (such as multi-threading and distributed processing), to make \n𝖢𝗈𝖽𝖾𝖯𝗅𝖺𝗇\n even more versatile in addressing a wider range of software engineering tasks.\n\nReferences\n(1)\t\naud ([n. d.])\t[n. d.].audiocraft.https://github.com/facebookresearch/audiocraft.\nCod ([n. d.])\t[n. d.].CodeQL.https://github.com/github/codeql.\nJAR ([n. d.])\t[n. d.].JARVIS.https://github.com/microsoft/JARVIS.\nJed ([n. d.])\t[n. d.].Jedi.https://github.com/davidhalter/jedi.\nOmn ([n. d.])\t[n. d.].OmniSharp.https://github.com/OmniSharp/csharp-language-server-protocol.\npyr ([n. d.])\t[n. d.].Pyright.https://github.com/microsoft/pyright.\nrep ([n. d.])\t[n. d.].Reactive Streams TCK.https://github.com/reactive-streams/reactive-streams-dotnet/tree/master/src/tck.\nwhi ([n. d.])\t[n. d.].whisper.https://github.com/openai/whisper.\nAgrawal et al. (2023)\tLakshya A Agrawal, Aditya Kanade, Navin Goyal, Shuvendu K. Lahiri, and Sriram K. Rajamani. 2023.Guiding Language Models of Code with Global Context using Monitors.arXiv:2306.10763 [cs.CL]\nAhmad et al. (2021)\tWasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray, and Kai-Wei Chang. 2021.Unified Pre-training for Program Understanding and Generation.arXiv:2103.06333 [cs.CL]\nAhmed and Devanbu (2023)\tToufique Ahmed and Premkumar Devanbu. 2023.Better patching using LLM prompting, via Self-Consistency.arXiv:2306.00108 [cs.SE]\nAho et al. (2007)\tAlfred V Aho, Ravi Sethi, Jeffrey D Ullman, et al. 2007.Compilers: principles, techniques, and tools. Vol. 2.Addison-wesley Reading.\nAlves et al. (2014)\tEverton L. G. Alves, Myoungkyu Song, and Miryung Kim. 2014.RefDistiller: A Refactoring Aware Code Review Tool for Inspecting Manual Refactoring Edits. In Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering (Hong Kong, China) (FSE 2014). Association for Computing Machinery, New York, NY, USA, 751–754.https://doi.org/10.1145/2635868.2661674\nAmazon Web Services, Inc. (2023)\tAmazon Web Services, Inc. 2023.Amazon Code Whisperer - AI Code Generator.https://aws.amazon.com/codewhisperer/Accessed: July 25, 2023.\nAndersen and Lawall (2010)\tJesper Andersen and Julia L Lawall. 2010.Generic patch inference.Automated software engineering 17 (2010), 119–148.\nApiwattanapong et al. (2004)\tTaweesup Apiwattanapong, Alessandro Orso, and Mary Jean Harrold. 2004.A differencing algorithm for object-oriented programs. In Proceedings. 19th International Conference on Automated Software Engineering, 2004. IEEE, 2–13.\nArnold and Bohner (1996)\tRS Arnold and SA Bohner. 1996.An introduction to software change impact analysis.Software Change Impact Analysis (1996), 1–26.\nArzt and Bodden (2014)\tSteven Arzt and Eric Bodden. 2014.Reviser: efficiently updating IDE-/IFDS-based data-flow analyses in response to incremental program changes. In Proceedings of the 36th International Conference on Software Engineering. 288–298.\nAustin et al. (2021)\tJacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. 2021.Program Synthesis with Large Language Models.http://arxiv.org/abs/2108.07732arXiv:2108.07732 [cs].\nBader et al. (2019)\tJohannes Bader, Andrew Scott, Michael Pradel, and Satish Chandra. 2019.Getafix: Learning to Fix Bugs Automatically.Proc. ACM Program. Lang. 3, OOPSLA, Article 159 (Oct. 2019), 27 pages.https://doi.org/10.1145/3360585\nBlack et al. (2022)\tSid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, and others. 2022.Gpt-neox-20b: An open-source autoregressive language model.arXiv preprint arXiv:2204.06745 (2022).\nBlanchet (2003)\tBruno Blanchet. 2003.Escape analysis for JavaTM: Theory and practice.ACM Transactions on Programming Languages and Systems (TOPLAS) 25, 6 (2003), 713–775.\nBrody et al. (2020)\tShaked Brody, Uri Alon, and Eran Yahav. 2020.A structural model for contextual code changes.4, OOPSLA (Nov. 2020).https://doi.org/10.1145/3428283Publisher Copyright: © 2020 Owner/Author..\nBrown et al. (2020)\tTom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020.Language models are few-shot learners.Advances in neural information processing systems 33 (2020), 1877–1901.\nBrunsfeld et al. (2023)\tMax Brunsfeld, Andrew Hlynskyi, Patrick Thomson, Josh Vera, Phil Turnbull, Timothy Clem, Douglas Creager, Andrew Helwer, Rob Rix, Hendrik Van Antwerpen, Michael Davis, , Ika, Tuấn-Anh Nguyễn, Stafford Brunk, Niranjan Hasabnis, Bfredl, Mingkai Dong, Matt Massicotte, Jonathan Arnett, Vladimir Panteleev, Steven Kalt, Kolja Lampe, Alex Pinkus, Mark Schmitz, Matthew Krupcale, Narpfel, Santos Gallegos, Vicent Martí, and , Edgar. 2023.tree-sitter/tree-sitter: v0.20.8.https://doi.org/10.5281/ZENODO.4619183\nBundy (1988)\tAlan Bundy. 1988.The use of explicit plans to guide inductive proofs. In 9th International Conference on Automated Deduction: Argonne, Illinois, USA, May 23–26, 1988 Proceedings 9. Springer, 111–120.\nBusi et al. (2019)\tMatteo Busi, Pierpaolo Degano, and Letterio Galletta. 2019.Using standard typing algorithms incrementally. In NASA Formal Methods: 11th International Symposium, NFM 2019, Houston, TX, USA, May 7–9, 2019, Proceedings 11. Springer, 106–122.\nChen et al. (2021)\tMark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, and others. 2021.Evaluating large language models trained on code.arXiv preprint arXiv:2107.03374 (2021).\nChoi et al. (1999)\tJong-Deok Choi, Manish Gupta, Mauricio Serrano, Vugranam C Sreedhar, and Sam Midkiff. 1999.Escape analysis for Java.Acm Sigplan Notices 34, 10 (1999), 1–19.\nChowdhery et al. (2022)\tAakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. 2022.Palm: Scaling language modeling with pathways.arXiv preprint arXiv:2204.02311 (2022).\nde Sousa et al. (2021)\tReudismam Rolim de Sousa, Gustavo Soares, Rohit Gheyi, Titus Barik, and Loris D’Antoni. 2021.Learning Quick Fixes from Code Repositories. In SBES ’21: 35th Brazilian Symposium on Software Engineering, Joinville, Santa Catarina, Brazil, 27 September 2021 - 1 October 2021, Cristiano D. Vasconcellos, Karina Girardi Roggia, Vanessa Collere, and Paulo Bousfield (Eds.). ACM, 74–83.https://doi.org/10.1145/3474624.3474650\nDean et al. (1995)\tJeffrey Dean, David Grove, and Craig Chambers. 1995.Optimization of object-oriented programs using static class hierarchy analysis. In ECOOP’95—Object-Oriented Programming, 9th European Conference, Åarhus, Denmark, August 7–11, 1995 9. Springer, 77–101.\nDig et al. (2006)\tDanny Dig, Can Comertoglu, Darko Marinov, and Ralph Johnson. 2006.Automated detection of refactorings in evolving components. In ECOOP 2006–Object-Oriented Programming: 20th European Conference, Nantes, France, July 3-7, 2006. Proceedings 20. Springer, 404–428.\nDing et al. (2022)\tYangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang. 2022.CoCoMIC: Code Completion By Jointly Modeling In-file and Cross-file Context.http://arxiv.org/abs/2212.10007arXiv:2212.10007 [cs].\nFried et al. (2022)\tDaniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2022.Incoder: A generative model for code infilling and synthesis.arXiv preprint arXiv:2204.05999 (2022).\nGe et al. (2017)\tXi Ge, Saurabh Sarkar, Jim Witschey, and Emerson Murphy-Hill. 2017.Refactoring-aware code review. In 2017 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC). IEEE, 71–79.\nGhallab et al. (2004)\tMalik Ghallab, Dana Nau, and Paolo Traverso. 2004.Automated Planning: theory and practice.Elsevier.\nGithub, Inc. (2023)\tGithub, Inc. 2023.GitHub Copilot: Your AI pair programmer.https://github.com/features/copilotAccessed: July 25, 2023.\nGonzález et al. (2015)\tDavid González, Joshué Pérez, Vicente Milanés, and Fawzi Nashashibi. 2015.A review of motion planning techniques for automated vehicles.IEEE Transactions on intelligent transportation systems 17, 4 (2015), 1135–1145.\nGupta et al. (2023)\tPriyanshu Gupta, Avishree Khare, Yasharth Bajpai, Saikat Chakraborty, Sumit Gulwani, Aditya Kanade, Arjun Radhakrishna, Gustavo Soares, and Ashish Tiwari. 2023.GrACE: Generation using Associated Code Edits.arXiv:2305.14129 [cs.SE]\nJashki et al. (2008)\tMohammad-Amin Jashki, Reza Zafarani, and Ebrahim Bagheri. 2008.Towards a more efficient static software change impact analysis method. In Proceedings of the 8th ACM SIGPLAN-SIGSOFT workshop on Program analysis for software tools and engineering. 84–90.\nJiang et al. (2023)\tXue Jiang, Yihong Dong, Lecheng Wang, Qiwei Shang, and Ge Li. 2023.Self-planning Code Generation with Large Language Model.arXiv:2303.06689 [cs.SE]\nJin et al. (2023)\tMatthew Jin, Syed Shahriar, Michele Tufano, Xin Shi, Shuai Lu, Neel Sundaresan, and Alexey Svyatkovskiy. 2023.InferFix: End-to-End Program Repair with LLMs.arXiv preprint arXiv:2303.07263 (2023).\nKarpas and Magazzeni (2020)\tErez Karpas and Daniele Magazzeni. 2020.Automated planning for robotics.Annual Review of Control, Robotics, and Autonomous Systems 3 (2020), 417–439.\nKetkar et al. (2022)\tAmeya Ketkar, Oleg Smirnov, Nikolaos Tsantalis, Danny Dig, and Timofey Bryksin. 2022.Inferring and applying type changes. In Proceedings of the 44th International Conference on Software Engineering. 1206–1218.\nKim et al. (2012)\tMiryung Kim, David Notkin, Dan Grossman, and Gary Wilson. 2012.Identifying and summarizing systematic code changes via rule inference.IEEE Transactions on Software Engineering 39, 1 (2012), 45–62.\nLa Valle (2011)\tSteven M La Valle. 2011.Motion planning.IEEE Robotics & Automation Magazine 18, 2 (2011), 108–118.\nLahiri et al. (2012)\tShuvendu K Lahiri, Chris Hawblitzel, Ming Kawaguchi, and Henrique Rebêlo. 2012.Symdiff: A language-agnostic semantic diff tool for imperative programs. In Computer Aided Verification: 24th International Conference, CAV 2012, Berkeley, CA, USA, July 7-13, 2012 Proceedings 24. Springer, 712–717.\nLamothe et al. (2020)\tMaxime Lamothe, Weiyi Shang, and Tse-Hsun Peter Chen. 2020.A3: Assisting android api migrations using code examples.IEEE Transactions on Software Engineering 48, 2 (2020), 417–431.\nLi et al. (2022)\tYujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d’Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel J. Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu, and Oriol Vinyals. 2022.Competition-level code generation with AlphaCode.Science 378, 6624 (2022), 1092–1097.https://doi.org/10.1126/science.abq1158_eprint: https://www.science.org/doi/pdf/10.1126/science.abq1158.\nLiu et al. (2023)\tTianyang Liu, Canwen Xu, and Julian McAuley. 2023.RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems.arXiv:2306.03091 [cs.CL]\nMcPeak et al. (2013)\tScott McPeak, Charles-Henri Gros, and Murali Krishna Ramanathan. 2013.Scalable and incremental software bug detection. In Proceedings of the 2013 9th Joint Meeting on Foundations of Software Engineering. 554–564.\nMeng et al. (2011)\tNa Meng, Miryung Kim, and Kathryn S McKinley. 2011.Sydit: Creating and applying a program transformation from an example. In Proceedings of the 19th ACM SIGSOFT symposium and the 13th European conference on Foundations of software engineering. 440–443.\nMeng et al. (2013)\tNa Meng, Miryung Kim, and Kathryn S McKinley. 2013.LASE: locating and applying systematic edits by learning from examples. In 2013 35th International Conference on Software Engineering (ICSE). IEEE, 502–511.\nMiltner et al. (2019)\tAnders Miltner, Sumit Gulwani, Vu Le, Alan Leung, Arjun Radhakrishna, Gustavo Soares, Ashish Tiwari, and Abhishek Udupa. 2019.On the fly synthesis of edit suggestions.Proceedings of the ACM on Programming Languages 3, OOPSLA (2019), 1–29.\nNijkamp et al. (2023)\tErik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2023.CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis. In The Eleventh International Conference on Learning Representations.https://openreview.net/forum?id=iaYcJKpY2B_\nOpenAI (2023)\tOpenAI. 2023.GPT-4 Technical Report.arXiv:2303.08774 [cs.CL]\nPapineni et al. (2002)\tKishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002.Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th annual meeting of the Association for Computational Linguistics. 311–318.\nPashakhanloo et al. (2022)\tPardis Pashakhanloo, Aaditya Naik, Yuepeng Wang, Hanjun Dai, Petros Maniatis, and Mayur Naik. 2022.Codetrek: Flexible modeling of code using an extensible relational representation.(2022).\nPearce et al. (2022)\tHammond Pearce, Benjamin Tan, Baleegh Ahmad, Ramesh Karri, and Brendan Dolan-Gavitt. 2022.Examining Zero-Shot Vulnerability Repair with Large Language Models. In 2023 IEEE Symposium on Security and Privacy (SP). IEEE Computer Society, 1–18.\nPei et al. (2023b)\tHengzhi Pei, Jinman Zhao, Leonard Lausen, Sheng Zha, and George Karypis. 2023b.Better context makes better code language models: A case study on function call argument completion. In AAAI.https://www.amazon.science/publications/better-context-makes-better-code-language-models-a-case-study-on-function-call-argument-completion\nPei et al. (2023a)\tKexin Pei, David Bieber, Kensen Shi, Charles Sutton, and Pengcheng Yin. 2023a.Can Large Language Models Reason about Program Invariants?(2023).\nPerson et al. (2011)\tSuzette Person, Guowei Yang, Neha Rungta, and Sarfraz Khurshid. 2011.Directed incremental symbolic execution.Acm Sigplan Notices 46, 6 (2011), 504–515.\nReid and Neubig (2022)\tMachel Reid and Graham Neubig. 2022.Learning to Model Editing Processes.https://doi.org/10.48550/ARXIV.2205.12374\nRen et al. (2004)\tXiaoxia Ren, Fenil Shah, Frank Tip, Barbara G Ryder, and Ophelia Chesley. 2004.Chianti: a tool for change impact analysis of java programs. In Proceedings of the 19th annual ACM SIGPLAN conference on Object-oriented programming, systems, languages, and applications. 432–448.\nReplit, Inc. (2023)\tReplit, Inc. 2023.Replit.https://replit.com/Accessed: July 25, 2023.\nRussell (2010)\tStuart J Russell. 2010.Artificial intelligence a modern approach.Pearson Education, Inc.\nRyder (1983)\tBarbara G Ryder. 1983.Incremental data flow analysis. In Proceedings of the 10th ACM SIGACT-SIGPLAN symposium on Principles of programming languages. 167–176.\nSchäfer et al. (2023)\tMax Schäfer, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2023.Adaptive test generation using a large language model.arXiv preprint arXiv:2302.06527 (2023).\nShrivastava et al. (2023)\tDisha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, and Torsten Scholak. 2023.RepoFusion: Training Code Models to Understand Your Repository.arXiv:2306.10998 [cs.LG]\nShrivastava et al. (2022)\tDisha Shrivastava, Hugo Larochelle, and Daniel Tarlow. 2022.Repository-level prompt generation for large language models of code.arXiv preprint arXiv:2206.12839 (2022).\nTian et al. (2023)\tHaoye Tian, Weiqi Lu, Tsz On Li, Xunzhu Tang, Shing-Chi Cheung, Jacques Klein, and Tegawendé F. Bissyandé. 2023.Is ChatGPT the Ultimate Programming Assistant – How far is it?arXiv:2304.11938 [cs.SE]\nTouvron et al. (2023)\tHugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023.Llama 2: Open Foundation and Fine-Tuned Chat Models.arXiv:2307.09288 [cs.CL]\nWang and Komatsuzaki (2021)\tBen Wang and Aran Komatsuzaki. 2021.GPT-J-6B: A 6 billion parameter autoregressive language model.\nWang et al. (2021)\tYue Wang, Weishi Wang, Shafiq R. Joty, and Steven C. H. Hoi. 2021.CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation.ArXiv abs/2109.00859 (2021).\nWei et al. (2023a)\tJiayi Wei, Greg Durrett, and Isil Dillig. 2023a.Coeditor: Leveraging Contextual Changes for Multi-round Code Auto-editing.arXiv:2305.18584 [cs.SE]\nWei et al. (2023b)\tJiayi Wei, Greg Durrett, and Isil Dillig. 2023b.TypeT5: Seq2seq Type Inference using Static Analysis.arXiv:2303.09564 [cs.SE]\nWilson-Thomas ([n. d.])\tMark Wilson-Thomas. [n. d.].GitHub Copilot chat for Visual Studio 2022.https://devblogs.microsoft.com/visualstudio/github-copilot-chat-for-visual-studio-2022/Accessed: July 25, 2023.\nXia et al. (2023)\tChunqiu Steven Xia, Yuxiang Wei, and Lingming Zhang. 2023.Automated program repair in the era of large pre-trained language models. In Proceedings of the 45th International Conference on Software Engineering (ICSE 2023). Association for Computing Machinery.\nXu et al. (2022)\tFrank F. Xu, Uri Alon, Graham Neubig, and Vincent Josua Hellendoorn. 2022.A Systematic Evaluation of Large Language Models of Code. In Proceedings of the 6th ACM SIGPLAN International Symposium on Machine Programming (MAPS 2022). Association for Computing Machinery, New York, NY, USA, 1–10.https://doi.org/10.1145/3520312.3534862event-place: San Diego, CA, USA.\nXu et al. (2021)\tFrank F Xu, Junxian He, Graham Neubig, and Vincent J Hellendoorn. 2021.Capturing structural locality in non-parametric language models.arXiv preprint arXiv:2110.02870 (2021).\nXu et al. (2019)\tShengzhe Xu, Ziqi Dong, and Na Meng. 2019.Meditor: inference and application of API migration edits. In 2019 IEEE/ACM 27th International Conference on Program Comprehension (ICPC). IEEE, 335–346.\nYin et al. (2019)\tPengcheng Yin, Graham Neubig, Miltiadis Allamanis, Marc Brockschmidt, and Alexander Gaunt. 2019.Learning to Represent Edits. In ICLR 2019.https://www.microsoft.com/en-us/research/publication/learning-to-represent-edits/arXiv:1810.13337 [cs.LG].\nYur et al. (1999)\tJyh-shiarn Yur, Barbara G Ryder, and William A Landi. 1999.An incremental flow-and context-sensitive pointer aliasing analysis. In Proceedings of the 21st International conference on Software Engineering. 442–451.\nZhang et al. (2023b)\tFengji Zhang, Bei Chen, Yue Zhang, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, and Weizhu Chen. 2023b.RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation.arXiv preprint arXiv:2303.12570 (2023).\nZhang et al. (2023a)\tShun Zhang, Zhenfang Chen, Yikang Shen, Mingyu Ding, Joshua B. Tenenbaum, and Chuang Gan. 2023a.Planning with Large Language Models for Code Generation.arXiv:2303.05510 [cs.LG]\nZhang et al. (2022)\tYuhao Zhang, Yasharth Bajpai, Priyanshu Gupta, Ameya Ketkar, Miltiadis Allamanis, Titus Barik, Sumit Gulwani, Arjun Radhakrishna, Mohammad Raza, Gustavo Soares, and Ashish Tiwari. 2022.Overwatch: Learning patterns in code edit sequences.Proc. ACM Program. Lang. 6, OOPSLA2 (2022), 395–423.https://doi.org/10.1145/3563302\n◄  Feeling\nlucky? Conversion\nreport Report\nan issue View original\non arXiv►\nCopyright Privacy Policy Generated on Wed Feb 28 05:01:14 2024 by LaTeXML",
  "usage": {
    "tokens": 19924
  }
}
```
