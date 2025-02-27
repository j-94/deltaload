---
title: langchain_experimental 0.0.65 — 🦜🔗 LangChain 0.2.17
description: 
url: https://api.python.langchain.com/en/latest/experimental_api_reference.html#module-langchain_experimental.autonomous_agents
timestamp: 2025-01-20T15:55:40.318Z
domain: api.python.langchain.com
path: en_latest_experimental_api_reference.html
---

# langchain_experimental 0.0.65 — 🦜🔗 LangChain 0.2.17



## Content

This is a legacy site. Please use the latest v0.2 and v0.3 API references instead.

LangChain
Core
Community
Experimental
Text splitters
Partner libs
Docs
 
Toggle Menu
langchain_experimental 0.0.65
langchain_experimental.agents
langchain_experimental.autonomous_agents
langchain_experimental.chat_models
langchain_experimental.comprehend_moderation
langchain_experimental.cpal
langchain_experimental.data_anonymizer
langchain_experimental.fallacy_removal
langchain_experimental.generative_agents
langchain_experimental.graph_transformers
langchain_experimental.llm_bash
langchain_experimental.llm_symbolic_math
langchain_experimental.llms
langchain_experimental.open_clip
langchain_experimental.pal_chain
langchain_experimental.plan_and_execute
langchain_experimental.prompt_injection_identifier
langchain_experimental.recommenders
langchain_experimental.retrievers
langchain_experimental.rl_chain
langchain_experimental.smart_llm
langchain_experimental.sql
langchain_experimental.tabular_synthetic_data
langchain_experimental.text_splitter
langchain_experimental.tools
langchain_experimental.tot
langchain_experimental.utilities
langchain_experimental.video_captioning
langchain_experimental 0.0.65
langchain_experimental.agents

Agent is a class that uses an LLM to choose a sequence of actions to take.

In Chains, a sequence of actions is hardcoded. In Agents, a language model is used as a reasoning engine to determine which actions to take and in which order.

Agents select and use Tools and Toolkits for actions.

Functions

agents.agent_toolkits.csv.base.create_csv_agent(...)

	

Create pandas dataframe agent by loading csv to a dataframe.




agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent(llm, df)

	

Construct a Pandas agent from an LLM and dataframe(s).




agents.agent_toolkits.python.base.create_python_agent(...)

	

Construct a python agent from an LLM and tool.




agents.agent_toolkits.spark.base.create_spark_dataframe_agent(llm, df)

	

Construct a Spark agent from an LLM and dataframe.




agents.agent_toolkits.xorbits.base.create_xorbits_agent(...)

	

Construct a xorbits agent from an LLM and dataframe.

langchain_experimental.autonomous_agents

Autonomous agents in the Langchain experimental package include [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT), [BabyAGI](https://github.com/yoheinakajima/babyagi), and [HuggingGPT](https://arxiv.org/abs/2303.17580) agents that interact with language models autonomously.

These agents have specific functionalities like memory management, task creation, execution chains, and response generation.

They differ from ordinary agents by their autonomous decision-making capabilities, memory handling, and specialized functionalities for tasks and response.

Classes

autonomous_agents.autogpt.agent.AutoGPT(...)

	

Agent for interacting with AutoGPT.




autonomous_agents.autogpt.memory.AutoGPTMemory

	

Memory for AutoGPT.




autonomous_agents.autogpt.output_parser.AutoGPTAction(...)

	

Action returned by AutoGPTOutputParser.




autonomous_agents.autogpt.output_parser.AutoGPTOutputParser

	

Output parser for AutoGPT.




autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser

	

Base Output parser for AutoGPT.




autonomous_agents.autogpt.prompt.AutoGPTPrompt

	

Prompt for AutoGPT.




autonomous_agents.autogpt.prompt_generator.PromptGenerator()

	

Generator of custom prompt strings.




autonomous_agents.baby_agi.baby_agi.BabyAGI

	

Controller model for the BabyAGI agent.




autonomous_agents.baby_agi.task_creation.TaskCreationChain

	

Chain generating tasks.




autonomous_agents.baby_agi.task_execution.TaskExecutionChain

	

Chain to execute tasks.




autonomous_agents.baby_agi.task_prioritization.TaskPrioritizationChain

	

Chain to prioritize tasks.




autonomous_agents.hugginggpt.hugginggpt.HuggingGPT(...)

	

Agent for interacting with HuggingGPT.




autonomous_agents.hugginggpt.repsonse_generator.ResponseGenerationChain

	

Chain to execute tasks.




autonomous_agents.hugginggpt.repsonse_generator.ResponseGenerator(...)

	

Generates a response based on the input.




autonomous_agents.hugginggpt.task_executor.Task(...)

	

Task to be executed.




autonomous_agents.hugginggpt.task_executor.TaskExecutor(plan)

	

Load tools and execute tasks.




autonomous_agents.hugginggpt.task_planner.BasePlanner

	

Base class for a planner.




autonomous_agents.hugginggpt.task_planner.Plan(steps)

	

A plan to execute.




autonomous_agents.hugginggpt.task_planner.PlanningOutputParser

	

Parses the output of the planning stage.




autonomous_agents.hugginggpt.task_planner.Step(...)

	

A step in the plan.




autonomous_agents.hugginggpt.task_planner.TaskPlaningChain

	

Chain to execute tasks.




autonomous_agents.hugginggpt.task_planner.TaskPlanner

	

Planner for tasks.

Functions

autonomous_agents.autogpt.output_parser.preprocess_json_input(...)

	

Preprocesses a string to be parsed as json.




autonomous_agents.autogpt.prompt_generator.get_prompt(tools)

	

Generates a prompt string.




autonomous_agents.hugginggpt.repsonse_generator.load_response_generator(llm)

	

Load the ResponseGenerator.




autonomous_agents.hugginggpt.task_planner.load_chat_planner(llm)

	

Load the chat planner.

langchain_experimental.chat_models

Chat Models are a variation on language models.

While Chat Models use language models under the hood, the interface they expose is a bit different. Rather than expose a “text in, text out” API, they expose an interface where “chat messages” are the inputs and outputs.

Class hierarchy:

BaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm


Main helpers:

AIMessage, BaseMessage, HumanMessage

Classes

chat_models.llm_wrapper.ChatWrapper

	

Wrapper for chat LLMs.




chat_models.llm_wrapper.Llama2Chat

	

Wrapper for Llama-2-chat model.




chat_models.llm_wrapper.Mixtral

	

See https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1#instruction-format




chat_models.llm_wrapper.Orca

	

Wrapper for Orca-style models.




chat_models.llm_wrapper.Vicuna

	

Wrapper for Vicuna-style models.

langchain_experimental.comprehend_moderation

Comprehend Moderation is used to detect and handle Personally Identifiable Information (PII), toxicity, and prompt safety in text.

The Langchain experimental package includes the AmazonComprehendModerationChain class for the comprehend moderation tasks. It is based on Amazon Comprehend service. This class can be configured with specific moderation settings like PII labels, redaction, toxicity thresholds, and prompt safety thresholds.

See more at https://aws.amazon.com/comprehend/

Amazon Comprehend service is used by several other classes: - ComprehendToxicity class is used to check the toxicity of text prompts using

AWS Comprehend service and take actions based on the configuration

ComprehendPromptSafety class is used to validate the safety of given prompt text, raising an error if unsafe content is detected based on the specified threshold

ComprehendPII class is designed to handle Personally Identifiable Information (PII) moderation tasks, detecting and managing PII entities in text inputs

Classes

comprehend_moderation.amazon_comprehend_moderation.AmazonComprehendModerationChain

	

Moderation Chain, based on Amazon Comprehend service.




comprehend_moderation.base_moderation.BaseModeration(client)

	

Base class for moderation.




comprehend_moderation.base_moderation_callbacks.BaseModerationCallbackHandler()

	

Base class for moderation callback handlers.




comprehend_moderation.base_moderation_config.BaseModerationConfig

	

Base configuration settings for moderation.




comprehend_moderation.base_moderation_config.ModerationPiiConfig

	

Configuration for PII moderation filter.




comprehend_moderation.base_moderation_config.ModerationPromptSafetyConfig

	

Configuration for Prompt Safety moderation filter.




comprehend_moderation.base_moderation_config.ModerationToxicityConfig

	

Configuration for Toxicity moderation filter.




comprehend_moderation.base_moderation_exceptions.ModerationPiiError([...])

	

Exception raised if PII entities are detected.




comprehend_moderation.base_moderation_exceptions.ModerationPromptSafetyError([...])

	

Exception raised if Unsafe prompts are detected.




comprehend_moderation.base_moderation_exceptions.ModerationToxicityError([...])

	

Exception raised if Toxic entities are detected.




comprehend_moderation.pii.ComprehendPII(client)

	

Class to handle Personally Identifiable Information (PII) moderation.




comprehend_moderation.prompt_safety.ComprehendPromptSafety(client)

	

Class to handle prompt safety moderation.




comprehend_moderation.toxicity.ComprehendToxicity(client)

	

Class to handle toxicity moderation.

langchain_experimental.cpal

Causal program-aided language (CPAL) is a concept implemented in LangChain as a chain for causal modeling and narrative decomposition.

CPAL improves upon the program-aided language (PAL) by incorporating causal structure to prevent hallucination in language models, particularly when dealing with complex narratives and math problems with nested dependencies.

CPAL involves translating causal narratives into a stack of operations, setting hypothetical conditions for causal models, and decomposing narratives into story elements.

It allows for the creation of causal chains that define the relationships between different elements in a narrative, enabling the modeling and analysis of causal relationships within a given context.

Classes

cpal.base.CPALChain

	

Causal program-aided language (CPAL) chain implementation.




cpal.base.CausalChain

	

Translate the causal narrative into a stack of operations.




cpal.base.InterventionChain

	

Set the hypothetical conditions for the causal model.




cpal.base.NarrativeChain

	

Decompose the narrative into its story elements.




cpal.base.QueryChain

	

Query the outcome table using SQL.




cpal.constants.Constant(value)

	

Enum for constants used in the CPAL.




cpal.models.CausalModel

	

Casual data.




cpal.models.EntityModel

	

Entity in the story.




cpal.models.EntitySettingModel

	

Entity initial conditions.




cpal.models.InterventionModel

	

Intervention data of the story aka initial conditions.




cpal.models.NarrativeModel

	

Narrative input as three story elements.




cpal.models.QueryModel

	

Query data of the story.




cpal.models.ResultModel

	

Result of the story query.




cpal.models.StoryModel

	

Story data.




cpal.models.SystemSettingModel

	

System initial conditions.

langchain_experimental.data_anonymizer

Data anonymizer contains both Anonymizers and Deanonymizers. It uses the [Microsoft Presidio](https://microsoft.github.io/presidio/) library.

Anonymizers are used to replace a Personally Identifiable Information (PII) entity text with some other value by applying a certain operator (e.g. replace, mask, redact, encrypt).

Deanonymizers are used to revert the anonymization operation (e.g. to decrypt an encrypted text).

Classes

data_anonymizer.base.AnonymizerBase()

	

Base abstract class for anonymizers.




data_anonymizer.base.ReversibleAnonymizerBase()

	

Base abstract class for reversible anonymizers.




data_anonymizer.deanonymizer_mapping.DeanonymizerMapping(...)

	

Deanonymizer mapping.




data_anonymizer.presidio.PresidioAnonymizer([...])

	

Anonymizer using Microsoft Presidio.




data_anonymizer.presidio.PresidioAnonymizerBase([...])

	

Base Anonymizer using Microsoft Presidio.




data_anonymizer.presidio.PresidioReversibleAnonymizer([...])

	

Reversible Anonymizer using Microsoft Presidio.

Functions

data_anonymizer.deanonymizer_mapping.create_anonymizer_mapping(...)

	

Create or update the mapping used to anonymize and/or




data_anonymizer.deanonymizer_mapping.format_duplicated_operator(...)

	

Format the operator name with the count.




data_anonymizer.deanonymizer_matching_strategies.case_insensitive_matching_strategy(...)

	

Case insensitive matching strategy for deanonymization.




data_anonymizer.deanonymizer_matching_strategies.combined_exact_fuzzy_matching_strategy(...)

	

Combined exact and fuzzy matching strategy for deanonymization.




data_anonymizer.deanonymizer_matching_strategies.exact_matching_strategy(...)

	

Exact matching strategy for deanonymization.




data_anonymizer.deanonymizer_matching_strategies.fuzzy_matching_strategy(...)

	

Fuzzy matching strategy for deanonymization.




data_anonymizer.deanonymizer_matching_strategies.ngram_fuzzy_matching_strategy(...)

	

N-gram fuzzy matching strategy for deanonymization.




data_anonymizer.faker_presidio_mapping.get_pseudoanonymizer_mapping([seed])

	

Get a mapping of entities to pseudo anonymize them.

langchain_experimental.fallacy_removal

Fallacy Removal Chain runs a self-review of logical fallacies as determined by paper [Robust and Explainable Identification of Logical Fallacies in Natural Language Arguments](https://arxiv.org/pdf/2212.07425.pdf). It is modeled after Constitutional AI and in the same format, but applying logical fallacies as generalized rules to remove them in output.

Classes

fallacy_removal.base.FallacyChain

	

Chain for applying logical fallacy evaluations.




fallacy_removal.models.LogicalFallacy

	

Logical fallacy.

langchain_experimental.generative_agents

Generative Agent primitives.

Classes

generative_agents.generative_agent.GenerativeAgent

	

Agent as a character with memory and innate characteristics.




generative_agents.memory.GenerativeAgentMemory

	

Memory for the generative agent.

langchain_experimental.graph_transformers

Graph Transformers transform Documents into Graph Documents.

Classes

graph_transformers.diffbot.DiffbotGraphTransformer(...)

	

Transform documents into graph documents using Diffbot NLP API.




graph_transformers.diffbot.NodesList()

	

List of nodes with associated properties.




graph_transformers.diffbot.SimplifiedSchema()

	

Simplified schema mapping.




graph_transformers.diffbot.TypeOption(value)

	

An enumeration.




graph_transformers.gliner.GlinerGraphTransformer(...)

	

A transformer class for converting documents into graph structures using the GLiNER and GLiREL models.




graph_transformers.llm.LLMGraphTransformer(llm)

	

Transform documents into graph-based documents using a LLM.




graph_transformers.llm.UnstructuredRelation

	

Create a new model by parsing and validating input data from keyword arguments.




graph_transformers.relik.RelikGraphTransformer([...])

	

A transformer class for converting documents into graph structures using the Relik library and models.

Functions

graph_transformers.diffbot.format_property_key(s)

	

Formats a string to be used as a property key.




graph_transformers.llm.create_simple_model([...])

	

Create a simple graph model with optional constraints on node and relationship types.




graph_transformers.llm.create_unstructured_prompt([...])

	




graph_transformers.llm.format_property_key(s)

	




graph_transformers.llm.map_to_base_node(node)

	

Map the SimpleNode to the base Node.




graph_transformers.llm.map_to_base_relationship(rel)

	

Map the SimpleRelationship to the base Relationship.




graph_transformers.llm.optional_enum_field([...])

	

Utility function to conditionally create a field with an enum constraint.

langchain_experimental.llm_bash

LLM bash is a chain that uses LLM to interpret a prompt and executes bash code.

Classes

llm_bash.base.LLMBashChain

	

Chain that interprets a prompt and executes bash operations.




llm_bash.bash.BashProcess([strip_newlines, ...])

	

Wrapper for starting subprocesses.




llm_bash.prompt.BashOutputParser

	

Parser for bash output.

langchain_experimental.llm_symbolic_math

Chain that interprets a prompt and executes python code to do math.

Heavily borrowed from llm_math, uses the [SymPy](https://www.sympy.org/) package.

Classes

llm_symbolic_math.base.LLMSymbolicMathChain

	

Chain that interprets a prompt and executes python code to do symbolic math.

langchain_experimental.llms

Experimental LLM classes provide access to the large language model (LLM) APIs and services.

Classes

llms.anthropic_functions.TagParser()

	

Parser for the tool tags.




llms.jsonformer_decoder.JsonFormer

	

Jsonformer wrapped LLM using HuggingFace Pipeline API.




llms.llamaapi.ChatLlamaAPI

	

Chat model using the Llama API.




llms.lmformatenforcer_decoder.LMFormatEnforcer

	

LMFormatEnforcer wrapped LLM using HuggingFace Pipeline API.




llms.rellm_decoder.RELLM

	

RELLM wrapped LLM using HuggingFace Pipeline API.

Functions

llms.jsonformer_decoder.import_jsonformer()

	

Lazily import of the jsonformer package.




llms.lmformatenforcer_decoder.import_lmformatenforcer()

	

Lazily import of the lmformatenforcer package.




llms.ollama_functions.convert_to_ollama_tool(tool)

	

Convert a tool to an Ollama tool.




llms.ollama_functions.parse_response(message)

	

Extract function_call from AIMessage.




llms.rellm_decoder.import_rellm()

	

Lazily import of the rellm package.

Deprecated classes

llms.anthropic_functions.AnthropicFunctions

	

Deprecated since version 0.0.54: Use langchain_anthropic.experimental.ChatAnthropicTools instead.




llms.ollama_functions.OllamaFunctions

	

Deprecated since version 0.0.64: Use langchain_ollama.ChatOllama instead.

langchain_experimental.open_clip

OpenCLIP Embeddings model.

OpenCLIP is a multimodal model that can encode text and images into a shared space.

See this paper for more details: https://arxiv.org/abs/2103.00020 and [this repository](https://github.com/mlfoundations/open_clip) for details.

Classes

open_clip.open_clip.OpenCLIPEmbeddings

	

OpenCLIP Embeddings model.

langchain_experimental.pal_chain

PAL Chain implements Program-Aided Language Models.

See the paper: https://arxiv.org/pdf/2211.10435.pdf.

This chain is vulnerable to [arbitrary code execution](https://github.com/langchain-ai/langchain/issues/5872).

Classes

pal_chain.base.PALChain

	

Chain that implements Program-Aided Language Models (PAL).




pal_chain.base.PALValidation([...])

	

Validation for PAL generated code.

langchain_experimental.plan_and_execute

Plan-and-execute agents are planning tasks with a language model (LLM) and executing them with a separate agent.

Classes

plan_and_execute.agent_executor.PlanAndExecute

	

Plan and execute a chain of steps.




plan_and_execute.executors.base.BaseExecutor

	

Base executor.




plan_and_execute.executors.base.ChainExecutor

	

Chain executor.




plan_and_execute.planners.base.BasePlanner

	

Base planner.




plan_and_execute.planners.base.LLMPlanner

	

LLM planner.




plan_and_execute.planners.chat_planner.PlanningOutputParser

	

Planning output parser.




plan_and_execute.schema.BaseStepContainer

	

Base step container.




plan_and_execute.schema.ListStepContainer

	

Container for List of steps.




plan_and_execute.schema.Plan

	

Plan.




plan_and_execute.schema.PlanOutputParser

	

Plan output parser.




plan_and_execute.schema.Step

	

Step.




plan_and_execute.schema.StepResponse

	

Step response.

Functions

plan_and_execute.executors.agent_executor.load_agent_executor(...)

	

Load an agent executor.




plan_and_execute.planners.chat_planner.load_chat_planner(llm)

	

Load a chat planner.

langchain_experimental.prompt_injection_identifier

HuggingFace Injection Identifier is a tool that uses [HuggingFace Prompt Injection model](https://huggingface.co/deepset/deberta-v3-base-injection) to detect prompt injection attacks.

Classes

prompt_injection_identifier.hugging_face_identifier.HuggingFaceInjectionIdentifier

	

Tool that uses HuggingFace Prompt Injection model to detect prompt injection attacks.




prompt_injection_identifier.hugging_face_identifier.PromptInjectionException([...])

	

Exception raised when prompt injection attack is detected.

langchain_experimental.recommenders

Amazon Personalize primitives.

[Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html) is a fully managed machine learning service that uses your data to generate item recommendations for your users.

Classes

recommenders.amazon_personalize.AmazonPersonalize([...])

	

Amazon Personalize Runtime wrapper for executing real-time operations.




recommenders.amazon_personalize_chain.AmazonPersonalizeChain

	

Chain for retrieving recommendations from Amazon Personalize,

langchain_experimental.retrievers

Retriever class returns Documents given a text query.

It is more general than a vector store. A retriever does not need to be able to store documents, only to return (or retrieve) it.

Classes

retrievers.vector_sql_database.VectorSQLDatabaseChainRetriever

	

Retriever that uses Vector SQL Database.

langchain_experimental.rl_chain

RL (Reinforcement Learning) Chain leverages the Vowpal Wabbit (VW) models for reinforcement learning with a context, with the goal of modifying the prompt before the LLM call.

[Vowpal Wabbit](https://vowpalwabbit.org/) provides fast, efficient, and flexible online machine learning techniques for reinforcement learning, supervised learning, and more.

Classes

rl_chain.base.AutoSelectionScorer

	

Auto selection scorer.




rl_chain.base.Embedder(*args, **kwargs)

	

Abstract class to represent an embedder.




rl_chain.base.Event(inputs[, selected])

	

Abstract class to represent an event.




rl_chain.base.Policy(**kwargs)

	

Abstract class to represent a policy.




rl_chain.base.RLChain

	

Chain that leverages the Vowpal Wabbit (VW) model as a learned policy for reinforcement learning.




rl_chain.base.Selected()

	

Abstract class to represent the selected item.




rl_chain.base.SelectionScorer

	

Abstract class to grade the chosen selection or the response of the llm.




rl_chain.base.VwPolicy(model_repo, vw_cmd, ...)

	

Vowpal Wabbit policy.




rl_chain.metrics.MetricsTrackerAverage(step)

	

Metrics Tracker Average.




rl_chain.metrics.MetricsTrackerRollingWindow(...)

	

Metrics Tracker Rolling Window.




rl_chain.model_repository.ModelRepository(folder)

	

Model Repository.




rl_chain.pick_best_chain.PickBest

	

Chain that leverages the Vowpal Wabbit (VW) model for reinforcement learning with a context, with the goal of modifying the prompt before the LLM call.




rl_chain.pick_best_chain.PickBestEvent(...)

	

Event class for PickBest chain.




rl_chain.pick_best_chain.PickBestFeatureEmbedder(...)

	

Embed the BasedOn and ToSelectFrom inputs into a format that can be used by the learning policy.




rl_chain.pick_best_chain.PickBestRandomPolicy(...)

	

Random policy for PickBest chain.




rl_chain.pick_best_chain.PickBestSelected([...])

	

Selected class for PickBest chain.




rl_chain.vw_logger.VwLogger(path)

	

Vowpal Wabbit custom logger.

Functions

rl_chain.base.BasedOn(anything)

	

Wrap a value to indicate that it should be based on.




rl_chain.base.Embed(anything[, keep])

	

Wrap a value to indicate that it should be embedded.




rl_chain.base.EmbedAndKeep(anything)

	

Wrap a value to indicate that it should be embedded and kept.




rl_chain.base.ToSelectFrom(anything)

	

Wrap a value to indicate that it should be selected from.




rl_chain.base.get_based_on_and_to_select_from(inputs)

	

Get the BasedOn and ToSelectFrom from the inputs.




rl_chain.base.parse_lines(parser, input_str)

	

Parse the input string into a list of examples.




rl_chain.base.prepare_inputs_for_autoembed(inputs)

	

Prepare the inputs for auto embedding.




rl_chain.helpers.embed(to_embed, model[, ...])

	

Embed the actions or context using the SentenceTransformer model (or a model that has an encode function).




rl_chain.helpers.embed_dict_type(item, model)

	

Embed a dictionary item.




rl_chain.helpers.embed_list_type(item, model)

	

Embed a list item.




rl_chain.helpers.embed_string_type(item, model)

	

Embed a string or an _Embed object.




rl_chain.helpers.is_stringtype_instance(item)

	

Check if an item is a string.




rl_chain.helpers.stringify_embedding(embedding)

	

Convert an embedding to a string.

langchain_experimental.smart_llm

SmartGPT chain is applying self-critique using the SmartGPT workflow.

See details at https://youtu.be/wVzuvf9D9BU

The workflow performs these 3 steps: 1. Ideate: Pass the user prompt to an Ideation LLM n_ideas times,

each result is an “idea”

Critique: Pass the ideas to a Critique LLM which looks for flaws in the ideas & picks the best one

Resolve: Pass the critique to a Resolver LLM which improves upon the best idea & outputs only the (improved version of) the best output

In total, the SmartGPT workflow will use n_ideas+2 LLM calls

Note that SmartLLMChain will only improve results (compared to a basic LLMChain), when the underlying models have the capability for reflection, which smaller models often don’t.

Finally, a SmartLLMChain assumes that each underlying LLM outputs exactly 1 result.

Classes

smart_llm.base.SmartLLMChain

	

Chain for applying self-critique using the SmartGPT workflow.

langchain_experimental.sql

SQL Chain interacts with SQL Database.

Classes

sql.base.SQLDatabaseChain

	

Chain for interacting with SQL Database.




sql.base.SQLDatabaseSequentialChain

	

Chain for querying SQL database that is a sequential chain.




sql.vector_sql.VectorSQLDatabaseChain

	

Chain for interacting with Vector SQL Database.




sql.vector_sql.VectorSQLOutputParser

	

Output Parser for Vector SQL.




sql.vector_sql.VectorSQLRetrieveAllOutputParser

	

Parser based on VectorSQLOutputParser.

Functions

sql.vector_sql.get_result_from_sqldb(db, cmd)

	

Get result from SQL Database.

langchain_experimental.tabular_synthetic_data

Generate tabular synthetic data using LLM and few-shot template.

Classes

tabular_synthetic_data.base.SyntheticDataGenerator

	

Generate synthetic data using the given LLM and few-shot template.

Functions

tabular_synthetic_data.openai.create_openai_data_generator(...)

	

Create an instance of SyntheticDataGenerator tailored for OpenAI models.

langchain_experimental.text_splitter

Experimental text splitter based on semantic similarity.

Classes

text_splitter.SemanticChunker(embeddings[, ...])

	

Split the text based on semantic similarity.

Functions

text_splitter.calculate_cosine_distances(...)

	

Calculate cosine distances between sentences.




text_splitter.combine_sentences(sentences[, ...])

	

Combine sentences based on buffer size.

langchain_experimental.tools

Experimental Python REPL tools.

Classes

tools.python.tool.PythonAstREPLTool

	

Tool for running python code in a REPL.




tools.python.tool.PythonInputs

	

Python inputs.




tools.python.tool.PythonREPLTool

	

Tool for running python code in a REPL.

Functions

tools.python.tool.sanitize_input(query)

	

Sanitize input to the python REPL.

langchain_experimental.tot

Implementation of a Tree of Thought (ToT) chain based on the paper [Large Language Model Guided Tree-of-Thought](https://arxiv.org/pdf/2305.08291.pdf).

The Tree of Thought (ToT) chain uses a tree structure to explore the space of possible solutions to a problem.

Classes

tot.base.ToTChain

	

Chain implementing the Tree of Thought (ToT).




tot.checker.ToTChecker

	

Tree of Thought (ToT) checker.




tot.controller.ToTController([c])

	

Tree of Thought (ToT) controller.




tot.memory.ToTDFSMemory([stack])

	

Memory for the Tree of Thought (ToT) chain.




tot.prompts.CheckerOutputParser

	

Parse and check the output of the language model.




tot.prompts.JSONListOutputParser

	

Parse the output of a PROPOSE_PROMPT response.




tot.thought.Thought

	

A thought in the ToT.




tot.thought.ThoughtValidity(value)

	

Enum for the validity of a thought.




tot.thought_generation.BaseThoughtGenerationStrategy

	

Base class for a thought generation strategy.




tot.thought_generation.ProposePromptStrategy

	

Strategy that is sequentially using a "propose prompt".




tot.thought_generation.SampleCoTStrategy

	

Sample strategy from a Chain-of-Thought (CoT) prompt.

Functions

tot.prompts.get_cot_prompt()

	

Get the prompt for the Chain of Thought (CoT) chain.




tot.prompts.get_propose_prompt()

	

Get the prompt for the PROPOSE_PROMPT chain.

langchain_experimental.utilities

Utility that simulates a standalone Python REPL.

Classes

utilities.python.PythonREPL

	

Simulates a standalone Python REPL.

langchain_experimental.video_captioning
Classes

video_captioning.base.VideoCaptioningChain

	

Video Captioning Chain.




video_captioning.models.AudioModel(...)

	




video_captioning.models.BaseModel(...)

	




video_captioning.models.CaptionModel(...)

	




video_captioning.models.VideoModel(...)

	




video_captioning.services.audio_service.AudioProcessor(api_key)

	




video_captioning.services.caption_service.CaptionProcessor(llm)

	




video_captioning.services.combine_service.CombineProcessor(llm)

	




video_captioning.services.image_service.ImageProcessor([...])

	




video_captioning.services.srt_service.SRTProcessor()

	

© 2023, LangChain, Inc. . Last updated on Dec 09, 2024.

## Metadata

```json
{
  "title": "langchain_experimental 0.0.65 — 🦜🔗 LangChain 0.2.17",
  "description": "",
  "url": "https://api.python.langchain.com/en/latest/experimental_api_reference.html#module-langchain_experimental.autonomous_agents",
  "content": "This is a legacy site. Please use the latest v0.2 and v0.3 API references instead.\n\nLangChain\nCore\nCommunity\nExperimental\nText splitters\nPartner libs\nDocs\n \nToggle Menu\nlangchain_experimental 0.0.65\nlangchain_experimental.agents\nlangchain_experimental.autonomous_agents\nlangchain_experimental.chat_models\nlangchain_experimental.comprehend_moderation\nlangchain_experimental.cpal\nlangchain_experimental.data_anonymizer\nlangchain_experimental.fallacy_removal\nlangchain_experimental.generative_agents\nlangchain_experimental.graph_transformers\nlangchain_experimental.llm_bash\nlangchain_experimental.llm_symbolic_math\nlangchain_experimental.llms\nlangchain_experimental.open_clip\nlangchain_experimental.pal_chain\nlangchain_experimental.plan_and_execute\nlangchain_experimental.prompt_injection_identifier\nlangchain_experimental.recommenders\nlangchain_experimental.retrievers\nlangchain_experimental.rl_chain\nlangchain_experimental.smart_llm\nlangchain_experimental.sql\nlangchain_experimental.tabular_synthetic_data\nlangchain_experimental.text_splitter\nlangchain_experimental.tools\nlangchain_experimental.tot\nlangchain_experimental.utilities\nlangchain_experimental.video_captioning\nlangchain_experimental 0.0.65\nlangchain_experimental.agents\n\nAgent is a class that uses an LLM to choose a sequence of actions to take.\n\nIn Chains, a sequence of actions is hardcoded. In Agents, a language model is used as a reasoning engine to determine which actions to take and in which order.\n\nAgents select and use Tools and Toolkits for actions.\n\nFunctions\n\nagents.agent_toolkits.csv.base.create_csv_agent(...)\n\n\t\n\nCreate pandas dataframe agent by loading csv to a dataframe.\n\n\n\n\nagents.agent_toolkits.pandas.base.create_pandas_dataframe_agent(llm, df)\n\n\t\n\nConstruct a Pandas agent from an LLM and dataframe(s).\n\n\n\n\nagents.agent_toolkits.python.base.create_python_agent(...)\n\n\t\n\nConstruct a python agent from an LLM and tool.\n\n\n\n\nagents.agent_toolkits.spark.base.create_spark_dataframe_agent(llm, df)\n\n\t\n\nConstruct a Spark agent from an LLM and dataframe.\n\n\n\n\nagents.agent_toolkits.xorbits.base.create_xorbits_agent(...)\n\n\t\n\nConstruct a xorbits agent from an LLM and dataframe.\n\nlangchain_experimental.autonomous_agents\n\nAutonomous agents in the Langchain experimental package include [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT), [BabyAGI](https://github.com/yoheinakajima/babyagi), and [HuggingGPT](https://arxiv.org/abs/2303.17580) agents that interact with language models autonomously.\n\nThese agents have specific functionalities like memory management, task creation, execution chains, and response generation.\n\nThey differ from ordinary agents by their autonomous decision-making capabilities, memory handling, and specialized functionalities for tasks and response.\n\nClasses\n\nautonomous_agents.autogpt.agent.AutoGPT(...)\n\n\t\n\nAgent for interacting with AutoGPT.\n\n\n\n\nautonomous_agents.autogpt.memory.AutoGPTMemory\n\n\t\n\nMemory for AutoGPT.\n\n\n\n\nautonomous_agents.autogpt.output_parser.AutoGPTAction(...)\n\n\t\n\nAction returned by AutoGPTOutputParser.\n\n\n\n\nautonomous_agents.autogpt.output_parser.AutoGPTOutputParser\n\n\t\n\nOutput parser for AutoGPT.\n\n\n\n\nautonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser\n\n\t\n\nBase Output parser for AutoGPT.\n\n\n\n\nautonomous_agents.autogpt.prompt.AutoGPTPrompt\n\n\t\n\nPrompt for AutoGPT.\n\n\n\n\nautonomous_agents.autogpt.prompt_generator.PromptGenerator()\n\n\t\n\nGenerator of custom prompt strings.\n\n\n\n\nautonomous_agents.baby_agi.baby_agi.BabyAGI\n\n\t\n\nController model for the BabyAGI agent.\n\n\n\n\nautonomous_agents.baby_agi.task_creation.TaskCreationChain\n\n\t\n\nChain generating tasks.\n\n\n\n\nautonomous_agents.baby_agi.task_execution.TaskExecutionChain\n\n\t\n\nChain to execute tasks.\n\n\n\n\nautonomous_agents.baby_agi.task_prioritization.TaskPrioritizationChain\n\n\t\n\nChain to prioritize tasks.\n\n\n\n\nautonomous_agents.hugginggpt.hugginggpt.HuggingGPT(...)\n\n\t\n\nAgent for interacting with HuggingGPT.\n\n\n\n\nautonomous_agents.hugginggpt.repsonse_generator.ResponseGenerationChain\n\n\t\n\nChain to execute tasks.\n\n\n\n\nautonomous_agents.hugginggpt.repsonse_generator.ResponseGenerator(...)\n\n\t\n\nGenerates a response based on the input.\n\n\n\n\nautonomous_agents.hugginggpt.task_executor.Task(...)\n\n\t\n\nTask to be executed.\n\n\n\n\nautonomous_agents.hugginggpt.task_executor.TaskExecutor(plan)\n\n\t\n\nLoad tools and execute tasks.\n\n\n\n\nautonomous_agents.hugginggpt.task_planner.BasePlanner\n\n\t\n\nBase class for a planner.\n\n\n\n\nautonomous_agents.hugginggpt.task_planner.Plan(steps)\n\n\t\n\nA plan to execute.\n\n\n\n\nautonomous_agents.hugginggpt.task_planner.PlanningOutputParser\n\n\t\n\nParses the output of the planning stage.\n\n\n\n\nautonomous_agents.hugginggpt.task_planner.Step(...)\n\n\t\n\nA step in the plan.\n\n\n\n\nautonomous_agents.hugginggpt.task_planner.TaskPlaningChain\n\n\t\n\nChain to execute tasks.\n\n\n\n\nautonomous_agents.hugginggpt.task_planner.TaskPlanner\n\n\t\n\nPlanner for tasks.\n\nFunctions\n\nautonomous_agents.autogpt.output_parser.preprocess_json_input(...)\n\n\t\n\nPreprocesses a string to be parsed as json.\n\n\n\n\nautonomous_agents.autogpt.prompt_generator.get_prompt(tools)\n\n\t\n\nGenerates a prompt string.\n\n\n\n\nautonomous_agents.hugginggpt.repsonse_generator.load_response_generator(llm)\n\n\t\n\nLoad the ResponseGenerator.\n\n\n\n\nautonomous_agents.hugginggpt.task_planner.load_chat_planner(llm)\n\n\t\n\nLoad the chat planner.\n\nlangchain_experimental.chat_models\n\nChat Models are a variation on language models.\n\nWhile Chat Models use language models under the hood, the interface they expose is a bit different. Rather than expose a “text in, text out” API, they expose an interface where “chat messages” are the inputs and outputs.\n\nClass hierarchy:\n\nBaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm\n\n\nMain helpers:\n\nAIMessage, BaseMessage, HumanMessage\n\nClasses\n\nchat_models.llm_wrapper.ChatWrapper\n\n\t\n\nWrapper for chat LLMs.\n\n\n\n\nchat_models.llm_wrapper.Llama2Chat\n\n\t\n\nWrapper for Llama-2-chat model.\n\n\n\n\nchat_models.llm_wrapper.Mixtral\n\n\t\n\nSee https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1#instruction-format\n\n\n\n\nchat_models.llm_wrapper.Orca\n\n\t\n\nWrapper for Orca-style models.\n\n\n\n\nchat_models.llm_wrapper.Vicuna\n\n\t\n\nWrapper for Vicuna-style models.\n\nlangchain_experimental.comprehend_moderation\n\nComprehend Moderation is used to detect and handle Personally Identifiable Information (PII), toxicity, and prompt safety in text.\n\nThe Langchain experimental package includes the AmazonComprehendModerationChain class for the comprehend moderation tasks. It is based on Amazon Comprehend service. This class can be configured with specific moderation settings like PII labels, redaction, toxicity thresholds, and prompt safety thresholds.\n\nSee more at https://aws.amazon.com/comprehend/\n\nAmazon Comprehend service is used by several other classes: - ComprehendToxicity class is used to check the toxicity of text prompts using\n\nAWS Comprehend service and take actions based on the configuration\n\nComprehendPromptSafety class is used to validate the safety of given prompt text, raising an error if unsafe content is detected based on the specified threshold\n\nComprehendPII class is designed to handle Personally Identifiable Information (PII) moderation tasks, detecting and managing PII entities in text inputs\n\nClasses\n\ncomprehend_moderation.amazon_comprehend_moderation.AmazonComprehendModerationChain\n\n\t\n\nModeration Chain, based on Amazon Comprehend service.\n\n\n\n\ncomprehend_moderation.base_moderation.BaseModeration(client)\n\n\t\n\nBase class for moderation.\n\n\n\n\ncomprehend_moderation.base_moderation_callbacks.BaseModerationCallbackHandler()\n\n\t\n\nBase class for moderation callback handlers.\n\n\n\n\ncomprehend_moderation.base_moderation_config.BaseModerationConfig\n\n\t\n\nBase configuration settings for moderation.\n\n\n\n\ncomprehend_moderation.base_moderation_config.ModerationPiiConfig\n\n\t\n\nConfiguration for PII moderation filter.\n\n\n\n\ncomprehend_moderation.base_moderation_config.ModerationPromptSafetyConfig\n\n\t\n\nConfiguration for Prompt Safety moderation filter.\n\n\n\n\ncomprehend_moderation.base_moderation_config.ModerationToxicityConfig\n\n\t\n\nConfiguration for Toxicity moderation filter.\n\n\n\n\ncomprehend_moderation.base_moderation_exceptions.ModerationPiiError([...])\n\n\t\n\nException raised if PII entities are detected.\n\n\n\n\ncomprehend_moderation.base_moderation_exceptions.ModerationPromptSafetyError([...])\n\n\t\n\nException raised if Unsafe prompts are detected.\n\n\n\n\ncomprehend_moderation.base_moderation_exceptions.ModerationToxicityError([...])\n\n\t\n\nException raised if Toxic entities are detected.\n\n\n\n\ncomprehend_moderation.pii.ComprehendPII(client)\n\n\t\n\nClass to handle Personally Identifiable Information (PII) moderation.\n\n\n\n\ncomprehend_moderation.prompt_safety.ComprehendPromptSafety(client)\n\n\t\n\nClass to handle prompt safety moderation.\n\n\n\n\ncomprehend_moderation.toxicity.ComprehendToxicity(client)\n\n\t\n\nClass to handle toxicity moderation.\n\nlangchain_experimental.cpal\n\nCausal program-aided language (CPAL) is a concept implemented in LangChain as a chain for causal modeling and narrative decomposition.\n\nCPAL improves upon the program-aided language (PAL) by incorporating causal structure to prevent hallucination in language models, particularly when dealing with complex narratives and math problems with nested dependencies.\n\nCPAL involves translating causal narratives into a stack of operations, setting hypothetical conditions for causal models, and decomposing narratives into story elements.\n\nIt allows for the creation of causal chains that define the relationships between different elements in a narrative, enabling the modeling and analysis of causal relationships within a given context.\n\nClasses\n\ncpal.base.CPALChain\n\n\t\n\nCausal program-aided language (CPAL) chain implementation.\n\n\n\n\ncpal.base.CausalChain\n\n\t\n\nTranslate the causal narrative into a stack of operations.\n\n\n\n\ncpal.base.InterventionChain\n\n\t\n\nSet the hypothetical conditions for the causal model.\n\n\n\n\ncpal.base.NarrativeChain\n\n\t\n\nDecompose the narrative into its story elements.\n\n\n\n\ncpal.base.QueryChain\n\n\t\n\nQuery the outcome table using SQL.\n\n\n\n\ncpal.constants.Constant(value)\n\n\t\n\nEnum for constants used in the CPAL.\n\n\n\n\ncpal.models.CausalModel\n\n\t\n\nCasual data.\n\n\n\n\ncpal.models.EntityModel\n\n\t\n\nEntity in the story.\n\n\n\n\ncpal.models.EntitySettingModel\n\n\t\n\nEntity initial conditions.\n\n\n\n\ncpal.models.InterventionModel\n\n\t\n\nIntervention data of the story aka initial conditions.\n\n\n\n\ncpal.models.NarrativeModel\n\n\t\n\nNarrative input as three story elements.\n\n\n\n\ncpal.models.QueryModel\n\n\t\n\nQuery data of the story.\n\n\n\n\ncpal.models.ResultModel\n\n\t\n\nResult of the story query.\n\n\n\n\ncpal.models.StoryModel\n\n\t\n\nStory data.\n\n\n\n\ncpal.models.SystemSettingModel\n\n\t\n\nSystem initial conditions.\n\nlangchain_experimental.data_anonymizer\n\nData anonymizer contains both Anonymizers and Deanonymizers. It uses the [Microsoft Presidio](https://microsoft.github.io/presidio/) library.\n\nAnonymizers are used to replace a Personally Identifiable Information (PII) entity text with some other value by applying a certain operator (e.g. replace, mask, redact, encrypt).\n\nDeanonymizers are used to revert the anonymization operation (e.g. to decrypt an encrypted text).\n\nClasses\n\ndata_anonymizer.base.AnonymizerBase()\n\n\t\n\nBase abstract class for anonymizers.\n\n\n\n\ndata_anonymizer.base.ReversibleAnonymizerBase()\n\n\t\n\nBase abstract class for reversible anonymizers.\n\n\n\n\ndata_anonymizer.deanonymizer_mapping.DeanonymizerMapping(...)\n\n\t\n\nDeanonymizer mapping.\n\n\n\n\ndata_anonymizer.presidio.PresidioAnonymizer([...])\n\n\t\n\nAnonymizer using Microsoft Presidio.\n\n\n\n\ndata_anonymizer.presidio.PresidioAnonymizerBase([...])\n\n\t\n\nBase Anonymizer using Microsoft Presidio.\n\n\n\n\ndata_anonymizer.presidio.PresidioReversibleAnonymizer([...])\n\n\t\n\nReversible Anonymizer using Microsoft Presidio.\n\nFunctions\n\ndata_anonymizer.deanonymizer_mapping.create_anonymizer_mapping(...)\n\n\t\n\nCreate or update the mapping used to anonymize and/or\n\n\n\n\ndata_anonymizer.deanonymizer_mapping.format_duplicated_operator(...)\n\n\t\n\nFormat the operator name with the count.\n\n\n\n\ndata_anonymizer.deanonymizer_matching_strategies.case_insensitive_matching_strategy(...)\n\n\t\n\nCase insensitive matching strategy for deanonymization.\n\n\n\n\ndata_anonymizer.deanonymizer_matching_strategies.combined_exact_fuzzy_matching_strategy(...)\n\n\t\n\nCombined exact and fuzzy matching strategy for deanonymization.\n\n\n\n\ndata_anonymizer.deanonymizer_matching_strategies.exact_matching_strategy(...)\n\n\t\n\nExact matching strategy for deanonymization.\n\n\n\n\ndata_anonymizer.deanonymizer_matching_strategies.fuzzy_matching_strategy(...)\n\n\t\n\nFuzzy matching strategy for deanonymization.\n\n\n\n\ndata_anonymizer.deanonymizer_matching_strategies.ngram_fuzzy_matching_strategy(...)\n\n\t\n\nN-gram fuzzy matching strategy for deanonymization.\n\n\n\n\ndata_anonymizer.faker_presidio_mapping.get_pseudoanonymizer_mapping([seed])\n\n\t\n\nGet a mapping of entities to pseudo anonymize them.\n\nlangchain_experimental.fallacy_removal\n\nFallacy Removal Chain runs a self-review of logical fallacies as determined by paper [Robust and Explainable Identification of Logical Fallacies in Natural Language Arguments](https://arxiv.org/pdf/2212.07425.pdf). It is modeled after Constitutional AI and in the same format, but applying logical fallacies as generalized rules to remove them in output.\n\nClasses\n\nfallacy_removal.base.FallacyChain\n\n\t\n\nChain for applying logical fallacy evaluations.\n\n\n\n\nfallacy_removal.models.LogicalFallacy\n\n\t\n\nLogical fallacy.\n\nlangchain_experimental.generative_agents\n\nGenerative Agent primitives.\n\nClasses\n\ngenerative_agents.generative_agent.GenerativeAgent\n\n\t\n\nAgent as a character with memory and innate characteristics.\n\n\n\n\ngenerative_agents.memory.GenerativeAgentMemory\n\n\t\n\nMemory for the generative agent.\n\nlangchain_experimental.graph_transformers\n\nGraph Transformers transform Documents into Graph Documents.\n\nClasses\n\ngraph_transformers.diffbot.DiffbotGraphTransformer(...)\n\n\t\n\nTransform documents into graph documents using Diffbot NLP API.\n\n\n\n\ngraph_transformers.diffbot.NodesList()\n\n\t\n\nList of nodes with associated properties.\n\n\n\n\ngraph_transformers.diffbot.SimplifiedSchema()\n\n\t\n\nSimplified schema mapping.\n\n\n\n\ngraph_transformers.diffbot.TypeOption(value)\n\n\t\n\nAn enumeration.\n\n\n\n\ngraph_transformers.gliner.GlinerGraphTransformer(...)\n\n\t\n\nA transformer class for converting documents into graph structures using the GLiNER and GLiREL models.\n\n\n\n\ngraph_transformers.llm.LLMGraphTransformer(llm)\n\n\t\n\nTransform documents into graph-based documents using a LLM.\n\n\n\n\ngraph_transformers.llm.UnstructuredRelation\n\n\t\n\nCreate a new model by parsing and validating input data from keyword arguments.\n\n\n\n\ngraph_transformers.relik.RelikGraphTransformer([...])\n\n\t\n\nA transformer class for converting documents into graph structures using the Relik library and models.\n\nFunctions\n\ngraph_transformers.diffbot.format_property_key(s)\n\n\t\n\nFormats a string to be used as a property key.\n\n\n\n\ngraph_transformers.llm.create_simple_model([...])\n\n\t\n\nCreate a simple graph model with optional constraints on node and relationship types.\n\n\n\n\ngraph_transformers.llm.create_unstructured_prompt([...])\n\n\t\n\n\n\n\ngraph_transformers.llm.format_property_key(s)\n\n\t\n\n\n\n\ngraph_transformers.llm.map_to_base_node(node)\n\n\t\n\nMap the SimpleNode to the base Node.\n\n\n\n\ngraph_transformers.llm.map_to_base_relationship(rel)\n\n\t\n\nMap the SimpleRelationship to the base Relationship.\n\n\n\n\ngraph_transformers.llm.optional_enum_field([...])\n\n\t\n\nUtility function to conditionally create a field with an enum constraint.\n\nlangchain_experimental.llm_bash\n\nLLM bash is a chain that uses LLM to interpret a prompt and executes bash code.\n\nClasses\n\nllm_bash.base.LLMBashChain\n\n\t\n\nChain that interprets a prompt and executes bash operations.\n\n\n\n\nllm_bash.bash.BashProcess([strip_newlines, ...])\n\n\t\n\nWrapper for starting subprocesses.\n\n\n\n\nllm_bash.prompt.BashOutputParser\n\n\t\n\nParser for bash output.\n\nlangchain_experimental.llm_symbolic_math\n\nChain that interprets a prompt and executes python code to do math.\n\nHeavily borrowed from llm_math, uses the [SymPy](https://www.sympy.org/) package.\n\nClasses\n\nllm_symbolic_math.base.LLMSymbolicMathChain\n\n\t\n\nChain that interprets a prompt and executes python code to do symbolic math.\n\nlangchain_experimental.llms\n\nExperimental LLM classes provide access to the large language model (LLM) APIs and services.\n\nClasses\n\nllms.anthropic_functions.TagParser()\n\n\t\n\nParser for the tool tags.\n\n\n\n\nllms.jsonformer_decoder.JsonFormer\n\n\t\n\nJsonformer wrapped LLM using HuggingFace Pipeline API.\n\n\n\n\nllms.llamaapi.ChatLlamaAPI\n\n\t\n\nChat model using the Llama API.\n\n\n\n\nllms.lmformatenforcer_decoder.LMFormatEnforcer\n\n\t\n\nLMFormatEnforcer wrapped LLM using HuggingFace Pipeline API.\n\n\n\n\nllms.rellm_decoder.RELLM\n\n\t\n\nRELLM wrapped LLM using HuggingFace Pipeline API.\n\nFunctions\n\nllms.jsonformer_decoder.import_jsonformer()\n\n\t\n\nLazily import of the jsonformer package.\n\n\n\n\nllms.lmformatenforcer_decoder.import_lmformatenforcer()\n\n\t\n\nLazily import of the lmformatenforcer package.\n\n\n\n\nllms.ollama_functions.convert_to_ollama_tool(tool)\n\n\t\n\nConvert a tool to an Ollama tool.\n\n\n\n\nllms.ollama_functions.parse_response(message)\n\n\t\n\nExtract function_call from AIMessage.\n\n\n\n\nllms.rellm_decoder.import_rellm()\n\n\t\n\nLazily import of the rellm package.\n\nDeprecated classes\n\nllms.anthropic_functions.AnthropicFunctions\n\n\t\n\nDeprecated since version 0.0.54: Use langchain_anthropic.experimental.ChatAnthropicTools instead.\n\n\n\n\nllms.ollama_functions.OllamaFunctions\n\n\t\n\nDeprecated since version 0.0.64: Use langchain_ollama.ChatOllama instead.\n\nlangchain_experimental.open_clip\n\nOpenCLIP Embeddings model.\n\nOpenCLIP is a multimodal model that can encode text and images into a shared space.\n\nSee this paper for more details: https://arxiv.org/abs/2103.00020 and [this repository](https://github.com/mlfoundations/open_clip) for details.\n\nClasses\n\nopen_clip.open_clip.OpenCLIPEmbeddings\n\n\t\n\nOpenCLIP Embeddings model.\n\nlangchain_experimental.pal_chain\n\nPAL Chain implements Program-Aided Language Models.\n\nSee the paper: https://arxiv.org/pdf/2211.10435.pdf.\n\nThis chain is vulnerable to [arbitrary code execution](https://github.com/langchain-ai/langchain/issues/5872).\n\nClasses\n\npal_chain.base.PALChain\n\n\t\n\nChain that implements Program-Aided Language Models (PAL).\n\n\n\n\npal_chain.base.PALValidation([...])\n\n\t\n\nValidation for PAL generated code.\n\nlangchain_experimental.plan_and_execute\n\nPlan-and-execute agents are planning tasks with a language model (LLM) and executing them with a separate agent.\n\nClasses\n\nplan_and_execute.agent_executor.PlanAndExecute\n\n\t\n\nPlan and execute a chain of steps.\n\n\n\n\nplan_and_execute.executors.base.BaseExecutor\n\n\t\n\nBase executor.\n\n\n\n\nplan_and_execute.executors.base.ChainExecutor\n\n\t\n\nChain executor.\n\n\n\n\nplan_and_execute.planners.base.BasePlanner\n\n\t\n\nBase planner.\n\n\n\n\nplan_and_execute.planners.base.LLMPlanner\n\n\t\n\nLLM planner.\n\n\n\n\nplan_and_execute.planners.chat_planner.PlanningOutputParser\n\n\t\n\nPlanning output parser.\n\n\n\n\nplan_and_execute.schema.BaseStepContainer\n\n\t\n\nBase step container.\n\n\n\n\nplan_and_execute.schema.ListStepContainer\n\n\t\n\nContainer for List of steps.\n\n\n\n\nplan_and_execute.schema.Plan\n\n\t\n\nPlan.\n\n\n\n\nplan_and_execute.schema.PlanOutputParser\n\n\t\n\nPlan output parser.\n\n\n\n\nplan_and_execute.schema.Step\n\n\t\n\nStep.\n\n\n\n\nplan_and_execute.schema.StepResponse\n\n\t\n\nStep response.\n\nFunctions\n\nplan_and_execute.executors.agent_executor.load_agent_executor(...)\n\n\t\n\nLoad an agent executor.\n\n\n\n\nplan_and_execute.planners.chat_planner.load_chat_planner(llm)\n\n\t\n\nLoad a chat planner.\n\nlangchain_experimental.prompt_injection_identifier\n\nHuggingFace Injection Identifier is a tool that uses [HuggingFace Prompt Injection model](https://huggingface.co/deepset/deberta-v3-base-injection) to detect prompt injection attacks.\n\nClasses\n\nprompt_injection_identifier.hugging_face_identifier.HuggingFaceInjectionIdentifier\n\n\t\n\nTool that uses HuggingFace Prompt Injection model to detect prompt injection attacks.\n\n\n\n\nprompt_injection_identifier.hugging_face_identifier.PromptInjectionException([...])\n\n\t\n\nException raised when prompt injection attack is detected.\n\nlangchain_experimental.recommenders\n\nAmazon Personalize primitives.\n\n[Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html) is a fully managed machine learning service that uses your data to generate item recommendations for your users.\n\nClasses\n\nrecommenders.amazon_personalize.AmazonPersonalize([...])\n\n\t\n\nAmazon Personalize Runtime wrapper for executing real-time operations.\n\n\n\n\nrecommenders.amazon_personalize_chain.AmazonPersonalizeChain\n\n\t\n\nChain for retrieving recommendations from Amazon Personalize,\n\nlangchain_experimental.retrievers\n\nRetriever class returns Documents given a text query.\n\nIt is more general than a vector store. A retriever does not need to be able to store documents, only to return (or retrieve) it.\n\nClasses\n\nretrievers.vector_sql_database.VectorSQLDatabaseChainRetriever\n\n\t\n\nRetriever that uses Vector SQL Database.\n\nlangchain_experimental.rl_chain\n\nRL (Reinforcement Learning) Chain leverages the Vowpal Wabbit (VW) models for reinforcement learning with a context, with the goal of modifying the prompt before the LLM call.\n\n[Vowpal Wabbit](https://vowpalwabbit.org/) provides fast, efficient, and flexible online machine learning techniques for reinforcement learning, supervised learning, and more.\n\nClasses\n\nrl_chain.base.AutoSelectionScorer\n\n\t\n\nAuto selection scorer.\n\n\n\n\nrl_chain.base.Embedder(*args, **kwargs)\n\n\t\n\nAbstract class to represent an embedder.\n\n\n\n\nrl_chain.base.Event(inputs[, selected])\n\n\t\n\nAbstract class to represent an event.\n\n\n\n\nrl_chain.base.Policy(**kwargs)\n\n\t\n\nAbstract class to represent a policy.\n\n\n\n\nrl_chain.base.RLChain\n\n\t\n\nChain that leverages the Vowpal Wabbit (VW) model as a learned policy for reinforcement learning.\n\n\n\n\nrl_chain.base.Selected()\n\n\t\n\nAbstract class to represent the selected item.\n\n\n\n\nrl_chain.base.SelectionScorer\n\n\t\n\nAbstract class to grade the chosen selection or the response of the llm.\n\n\n\n\nrl_chain.base.VwPolicy(model_repo, vw_cmd, ...)\n\n\t\n\nVowpal Wabbit policy.\n\n\n\n\nrl_chain.metrics.MetricsTrackerAverage(step)\n\n\t\n\nMetrics Tracker Average.\n\n\n\n\nrl_chain.metrics.MetricsTrackerRollingWindow(...)\n\n\t\n\nMetrics Tracker Rolling Window.\n\n\n\n\nrl_chain.model_repository.ModelRepository(folder)\n\n\t\n\nModel Repository.\n\n\n\n\nrl_chain.pick_best_chain.PickBest\n\n\t\n\nChain that leverages the Vowpal Wabbit (VW) model for reinforcement learning with a context, with the goal of modifying the prompt before the LLM call.\n\n\n\n\nrl_chain.pick_best_chain.PickBestEvent(...)\n\n\t\n\nEvent class for PickBest chain.\n\n\n\n\nrl_chain.pick_best_chain.PickBestFeatureEmbedder(...)\n\n\t\n\nEmbed the BasedOn and ToSelectFrom inputs into a format that can be used by the learning policy.\n\n\n\n\nrl_chain.pick_best_chain.PickBestRandomPolicy(...)\n\n\t\n\nRandom policy for PickBest chain.\n\n\n\n\nrl_chain.pick_best_chain.PickBestSelected([...])\n\n\t\n\nSelected class for PickBest chain.\n\n\n\n\nrl_chain.vw_logger.VwLogger(path)\n\n\t\n\nVowpal Wabbit custom logger.\n\nFunctions\n\nrl_chain.base.BasedOn(anything)\n\n\t\n\nWrap a value to indicate that it should be based on.\n\n\n\n\nrl_chain.base.Embed(anything[, keep])\n\n\t\n\nWrap a value to indicate that it should be embedded.\n\n\n\n\nrl_chain.base.EmbedAndKeep(anything)\n\n\t\n\nWrap a value to indicate that it should be embedded and kept.\n\n\n\n\nrl_chain.base.ToSelectFrom(anything)\n\n\t\n\nWrap a value to indicate that it should be selected from.\n\n\n\n\nrl_chain.base.get_based_on_and_to_select_from(inputs)\n\n\t\n\nGet the BasedOn and ToSelectFrom from the inputs.\n\n\n\n\nrl_chain.base.parse_lines(parser, input_str)\n\n\t\n\nParse the input string into a list of examples.\n\n\n\n\nrl_chain.base.prepare_inputs_for_autoembed(inputs)\n\n\t\n\nPrepare the inputs for auto embedding.\n\n\n\n\nrl_chain.helpers.embed(to_embed, model[, ...])\n\n\t\n\nEmbed the actions or context using the SentenceTransformer model (or a model that has an encode function).\n\n\n\n\nrl_chain.helpers.embed_dict_type(item, model)\n\n\t\n\nEmbed a dictionary item.\n\n\n\n\nrl_chain.helpers.embed_list_type(item, model)\n\n\t\n\nEmbed a list item.\n\n\n\n\nrl_chain.helpers.embed_string_type(item, model)\n\n\t\n\nEmbed a string or an _Embed object.\n\n\n\n\nrl_chain.helpers.is_stringtype_instance(item)\n\n\t\n\nCheck if an item is a string.\n\n\n\n\nrl_chain.helpers.stringify_embedding(embedding)\n\n\t\n\nConvert an embedding to a string.\n\nlangchain_experimental.smart_llm\n\nSmartGPT chain is applying self-critique using the SmartGPT workflow.\n\nSee details at https://youtu.be/wVzuvf9D9BU\n\nThe workflow performs these 3 steps: 1. Ideate: Pass the user prompt to an Ideation LLM n_ideas times,\n\neach result is an “idea”\n\nCritique: Pass the ideas to a Critique LLM which looks for flaws in the ideas & picks the best one\n\nResolve: Pass the critique to a Resolver LLM which improves upon the best idea & outputs only the (improved version of) the best output\n\nIn total, the SmartGPT workflow will use n_ideas+2 LLM calls\n\nNote that SmartLLMChain will only improve results (compared to a basic LLMChain), when the underlying models have the capability for reflection, which smaller models often don’t.\n\nFinally, a SmartLLMChain assumes that each underlying LLM outputs exactly 1 result.\n\nClasses\n\nsmart_llm.base.SmartLLMChain\n\n\t\n\nChain for applying self-critique using the SmartGPT workflow.\n\nlangchain_experimental.sql\n\nSQL Chain interacts with SQL Database.\n\nClasses\n\nsql.base.SQLDatabaseChain\n\n\t\n\nChain for interacting with SQL Database.\n\n\n\n\nsql.base.SQLDatabaseSequentialChain\n\n\t\n\nChain for querying SQL database that is a sequential chain.\n\n\n\n\nsql.vector_sql.VectorSQLDatabaseChain\n\n\t\n\nChain for interacting with Vector SQL Database.\n\n\n\n\nsql.vector_sql.VectorSQLOutputParser\n\n\t\n\nOutput Parser for Vector SQL.\n\n\n\n\nsql.vector_sql.VectorSQLRetrieveAllOutputParser\n\n\t\n\nParser based on VectorSQLOutputParser.\n\nFunctions\n\nsql.vector_sql.get_result_from_sqldb(db, cmd)\n\n\t\n\nGet result from SQL Database.\n\nlangchain_experimental.tabular_synthetic_data\n\nGenerate tabular synthetic data using LLM and few-shot template.\n\nClasses\n\ntabular_synthetic_data.base.SyntheticDataGenerator\n\n\t\n\nGenerate synthetic data using the given LLM and few-shot template.\n\nFunctions\n\ntabular_synthetic_data.openai.create_openai_data_generator(...)\n\n\t\n\nCreate an instance of SyntheticDataGenerator tailored for OpenAI models.\n\nlangchain_experimental.text_splitter\n\nExperimental text splitter based on semantic similarity.\n\nClasses\n\ntext_splitter.SemanticChunker(embeddings[, ...])\n\n\t\n\nSplit the text based on semantic similarity.\n\nFunctions\n\ntext_splitter.calculate_cosine_distances(...)\n\n\t\n\nCalculate cosine distances between sentences.\n\n\n\n\ntext_splitter.combine_sentences(sentences[, ...])\n\n\t\n\nCombine sentences based on buffer size.\n\nlangchain_experimental.tools\n\nExperimental Python REPL tools.\n\nClasses\n\ntools.python.tool.PythonAstREPLTool\n\n\t\n\nTool for running python code in a REPL.\n\n\n\n\ntools.python.tool.PythonInputs\n\n\t\n\nPython inputs.\n\n\n\n\ntools.python.tool.PythonREPLTool\n\n\t\n\nTool for running python code in a REPL.\n\nFunctions\n\ntools.python.tool.sanitize_input(query)\n\n\t\n\nSanitize input to the python REPL.\n\nlangchain_experimental.tot\n\nImplementation of a Tree of Thought (ToT) chain based on the paper [Large Language Model Guided Tree-of-Thought](https://arxiv.org/pdf/2305.08291.pdf).\n\nThe Tree of Thought (ToT) chain uses a tree structure to explore the space of possible solutions to a problem.\n\nClasses\n\ntot.base.ToTChain\n\n\t\n\nChain implementing the Tree of Thought (ToT).\n\n\n\n\ntot.checker.ToTChecker\n\n\t\n\nTree of Thought (ToT) checker.\n\n\n\n\ntot.controller.ToTController([c])\n\n\t\n\nTree of Thought (ToT) controller.\n\n\n\n\ntot.memory.ToTDFSMemory([stack])\n\n\t\n\nMemory for the Tree of Thought (ToT) chain.\n\n\n\n\ntot.prompts.CheckerOutputParser\n\n\t\n\nParse and check the output of the language model.\n\n\n\n\ntot.prompts.JSONListOutputParser\n\n\t\n\nParse the output of a PROPOSE_PROMPT response.\n\n\n\n\ntot.thought.Thought\n\n\t\n\nA thought in the ToT.\n\n\n\n\ntot.thought.ThoughtValidity(value)\n\n\t\n\nEnum for the validity of a thought.\n\n\n\n\ntot.thought_generation.BaseThoughtGenerationStrategy\n\n\t\n\nBase class for a thought generation strategy.\n\n\n\n\ntot.thought_generation.ProposePromptStrategy\n\n\t\n\nStrategy that is sequentially using a \"propose prompt\".\n\n\n\n\ntot.thought_generation.SampleCoTStrategy\n\n\t\n\nSample strategy from a Chain-of-Thought (CoT) prompt.\n\nFunctions\n\ntot.prompts.get_cot_prompt()\n\n\t\n\nGet the prompt for the Chain of Thought (CoT) chain.\n\n\n\n\ntot.prompts.get_propose_prompt()\n\n\t\n\nGet the prompt for the PROPOSE_PROMPT chain.\n\nlangchain_experimental.utilities\n\nUtility that simulates a standalone Python REPL.\n\nClasses\n\nutilities.python.PythonREPL\n\n\t\n\nSimulates a standalone Python REPL.\n\nlangchain_experimental.video_captioning\nClasses\n\nvideo_captioning.base.VideoCaptioningChain\n\n\t\n\nVideo Captioning Chain.\n\n\n\n\nvideo_captioning.models.AudioModel(...)\n\n\t\n\n\n\n\nvideo_captioning.models.BaseModel(...)\n\n\t\n\n\n\n\nvideo_captioning.models.CaptionModel(...)\n\n\t\n\n\n\n\nvideo_captioning.models.VideoModel(...)\n\n\t\n\n\n\n\nvideo_captioning.services.audio_service.AudioProcessor(api_key)\n\n\t\n\n\n\n\nvideo_captioning.services.caption_service.CaptionProcessor(llm)\n\n\t\n\n\n\n\nvideo_captioning.services.combine_service.CombineProcessor(llm)\n\n\t\n\n\n\n\nvideo_captioning.services.image_service.ImageProcessor([...])\n\n\t\n\n\n\n\nvideo_captioning.services.srt_service.SRTProcessor()\n\n\t\n\n© 2023, LangChain, Inc. . Last updated on Dec 09, 2024.",
  "usage": {
    "tokens": 6370
  }
}
```
