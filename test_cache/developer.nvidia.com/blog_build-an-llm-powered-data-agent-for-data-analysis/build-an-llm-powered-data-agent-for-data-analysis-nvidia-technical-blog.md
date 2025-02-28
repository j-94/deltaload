---
title: Build an LLM-Powered Data Agent for Data Analysis | NVIDIA Technical Blog
description: An AI agent is a system consisting of planning capabilities, memory, and tools to perform tasks requested by a user. For complex tasks such as data analytics or…
url: https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/
timestamp: 2025-01-20T16:00:57.483Z
domain: developer.nvidia.com
path: blog_build-an-llm-powered-data-agent-for-data-analysis
---

# Build an LLM-Powered Data Agent for Data Analysis | NVIDIA Technical Blog


An AI agent is a system consisting of planning capabilities, memory, and tools to perform tasks requested by a user. For complex tasks such as data analytics or…


## Content

An AI agent is a system consisting of planning capabilities, memory, and tools to perform tasks requested by a user. For complex tasks such as data analytics or interacting with complex systems, your application may depend on ‌collaboration among different types of agents. For more context, see [Introduction to LLM Agents](https://developer.nvidia.com/blog/introduction-to-llm-agents/) and [Building Your First LLM Agent Application](https://developer.nvidia.com/blog/building-your-first-llm-agent-application/).

This post explains the agent types required to build an accurate LLM application that can handle nuanced data analysis tasks when queried. It walks through an example use case for building a data analyst agent application, including code snippets. Finally, it provides some considerations for AI developers to consider when optimizing and building LLM agent apps.

LLM agent types for data analysis tasks[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#llm_agent_types_for_data_analysis_tasks)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

To begin, this section explains two main types of LLM agents and how they work—data agents and API or execution agents. I’ll also present an agent swarm use case, which involves multiple agents collaborating to solve a problem. Note that these agent types somewhat represent the ends of a spectrum. Blended, purpose-built agents can be created for specific use cases.

### Data agents[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#data_agents)

Data agents are typically designed for an extractive goal. In other words, data agents assist users in extracting information from a wide range of data sources. They help with assistive reasoning tasks.

For example, a financial analyst might ask, “In how many quarters of this year did the company have a positive cash flow?” This type of question requires reasoning, search (structured, unstructured, or both), and planning capabilities.

### API or execution agents[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#api_or_execution_agents)

API or execution agents are designed for an execution goal. These agents carry out a task or set of tasks requested by a user.

Consider the same financial analyst working with an Excel spreadsheet that contains the past year’s closing prices for 10 stocks. The analyst wants to organize these closing prices according to one or more statistical formulas. Excel APIs need to be chained together to perform this task. For another API agent example, see the [Google Places API Copilot Demo](https://huggingface.co/spaces/Nexusflow/NexusRaven-V2-Demo).

### Agent swarms[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#agent_swarms)

Agent swarms involve multiple data agents and multiple API agents collaborating in a decentralized manner to solve a complex problem**.** Agent swarms are designed for workflows that include both extractive and execution tasks that require different forms of planning and agent core harnesses.

For example, imagine that the financial analyst wants to study the top five fast food stocks for investment planning. The sequence of actions needed to reach this goal are outlined below and in Figure 1.

1.  Mine stock prices. The data agent hits a structured database with SQL or pandas or Quandl API.
2.  Extract more relevant information from 10-K and 10-Q reports. Execute search engine calls to get forms using data agent. Extract information using data agent [retrieval-augmented generation](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/) (RAG) calls.
3.  Store the information in Excel. API agent calls the Excel API.
4.  Extract user sentiment from social media content. Execute social media API calls using data mining with data agent. Perform sentiment analysis using RAG data agent.
5.  Use preselected metrics to generate indicators using API agent (Sheets API).
6.  Generate the report using API agent.
7.  Upload key graphs, plots, and charts to a PowerPoint slide using API agent (PowerPoint API).

![Image 23: Flowchart diagram showing a natural workflow for multiple agents collaborating together to solve a problem.](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/complex-workflow-multiple-data-agents-flowchart.png)

_Figure 1.  A general conceptual flow of the execution of a complex workflow solved with multiple agents_

As more types of LLM agents are modeled, they can interact with each other in the agent swarm to effectively solve problems. Constraining the problem into different agent verticals enables building agents with smaller models. This requires less effort for customization and retains modularity, which in turn provides benefits for adding new features, selecting the features you want, and simplifying deployment scaling. In this ecosystem, every agent looks at another agent like a tool and uses its help when required.

Building a data analyst agent[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#building_a_data_analyst_agent)
---------------------------------------------------------------------------------------------------------------------------------------------------

With this general taxonomy as a foundation, this section dives into building a data agent for a use case of talking to an SQL database for inventory management. The following discussion assumes you have read [Building Your First LLM Agent Application](https://developer.nvidia.com/blog/building-your-first-llm-agent-application/), or are otherwise familiar with the basics of LLM agents.

### Choose an LLM[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#choose_an_llm)

Begin by identifying which LLM to use. This example uses the [Mixtral 8x7B LLM](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/mixtral-8x7b) available in the NVIDIA NGC catalog. It accelerates various models and makes them available as APIs. The first API calls per model are free for experimentation.

Note that if you’re working with a model that isn’t tuned to handle agent workflows, you can reformulate the prompts below as a series of multiple-choice questions (MCQs). This should work, as most of the models are instruction-tuned to handle MCQs. [Learn more about fine-tuning](https://docs.nvidia.com/nemo-framework/user-guide/latest/playbooks/llama2sft.html).

### Select a use case[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#select_a_use_case)

Next, select a use case. The use case for this post is talking to an SQL database for inventory management. Then populate that database with, for example, three tables.

Note that the information presented below is for exemplary purposes only and is not intended to convey actual details.

suppliers\_data = \[
    {"name": "Samsung Electronics", "address": "Seoul, South Korea", "contact": "800-726-7864"},
    {"name": "Apple Inc.", "address": "Cupertino, California, USA", "contact": "800–692–7753"},
    {"name": "OnePlus Technology", "address": "Shenzhen, Guangdong, China", "contact": "400-888-1111"},
    {"name": "Google LLC", "address": "Mountain View, California, USA", "contact": "855-836-3987"},
    {"name": "Xiaomi Corporation", "address": "Beijing, China", "contact": "1800-103-6286"},
\]
 
products\_data = \[
    {"name": "Samsung Galaxy S21", "description": "Samsung flagship smartphone", "price": 799.99, "supplier\_id": 1},
    {"name": "Samsung Galaxy Note 20", "description": "Samsung premium smartphone with stylus", "price": 999.99, "supplier\_id": 1},
    {"name": "iPhone 13 Pro", "description": "Apple flagship smartphone", "price": 999.99, "supplier\_id": 2},
    {"name": "iPhone SE", "description": "Apple budget smartphone", "price": 399.99, "supplier\_id": 2},
    {"name": "OnePlus 9", "description": "High performance smartphone", "price": 729.00, "supplier\_id": 3},
    {"name": "OnePlus Nord", "description": "Mid-range smartphone", "price": 499.00, "supplier\_id": 3},
    {"name": "Google Pixel 6", "description": "Google's latest smartphone", "price": 599.00, "supplier\_id": 4},
    {"name": "Google Pixel 5a", "description": "Affordable Google smartphone", "price": 449.00, "supplier\_id": 4},
    {"name": "Xiaomi Mi 11", "description": "Xiaomi high-end smartphone", "price": 749.99, "supplier\_id": 5},
    {"name": "Xiaomi Redmi Note 10", "description": "Xiaomi budget smartphone", "price": 199.99, "supplier\_id": 5},
\]
 
inventory\_data = \[
    {"product\_id": 1, "quantity": 150, "min\_required": 30},
    {"product\_id": 2, "quantity": 100, "min\_required": 20},
    {"product\_id": 3, "quantity": 120, "min\_required": 30},
    {"product\_id": 4, "quantity": 80, "min\_required": 15},
    {"product\_id": 5, "quantity": 200, "min\_required": 40},
    {"product\_id": 6, "quantity": 150, "min\_required": 25},
    {"product\_id": 7, "quantity": 100, "min\_required": 20},
    {"product\_id": 8, "quantity": 90, "min\_required": 18},
    {"product\_id": 9, "quantity": 170, "min\_required": 35},
    {"product\_id": 10, "quantity": 220, "min\_required": 45},

For experimentation, store the preceding entries in an SQLite database. These entries are tailored for the schema shown in Figure 2. The intention is to create a simplified version of a database that is typically at the heart of any inventory management system. These databases contain information about current inventory levels, suppliers, and more.

![Image 24: Three tables containing the database schema: Inventory, Product, and Supplier.](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/sample-database-tables.png)

_Figure 2. Schema of the sample database to showcase the use case_

### LLM agent components[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#llm_agent_components)

An LLM agent contains four key components: tools, memory module, planning module, and agent core. Details about the components for this example are provided below.

#### Tools

This example uses the following two tools:

*   **Calculator:** For any basic calculations needed after querying the data. To keep it simple, an LLM is used here. Any service or API can be added to solve said problem.
*   **SQL Query Executor:** For querying the database for raw data.

#### Memory

A simple buffer or list to keep track of all the agent’s actions.

#### Planning

A linear greedy approach. To achieve this, create a “faux tool” for “generate the final answer.” This idea is addressed further in the section below.

#### Agent core

Time to put everything together. The prompt for the agent core LLM looks something like this:

"""<s\> \[INST\]You are an agent capable of using a variety of TOOLS to answer a data analytics question.
Always use MEMORY to help select the TOOLS to be used.

MEMORY
<Empty\>

TOOLS
- Generate Final Answer: Use if answer to User's question can be given with MEMORY
- Calculator: Use this tool to solve mathematical problems.
- Query\_Database: Write an SQL Query to query the Database.

ANSWER FORMAT
\`\`\`json
{
    "tool\_name": "Calculator"
}
\`\`\`
\[/INST\]
User: {User's Question}

Assistant: \`\`\`json
{
    "tool\_name": """

The preceding prompt includes all the tools and related information. You can design the core’s code harness in a way such that, given any tool but the “generate the final answer” faux tool, the agent will append the results of the tool used to memory and re-access the situation. This is an iterative greedy approach where the “best” decision is made for the individual step.

if tool\_selection\['tool\_name'\] == "Query\_Database":
        Generate\_SQL\_Query(question, memory, schema)
        QueryDB
        Append results to memory
        Agent(question, memory)

    if tool\_selection\['tool\_name'\] == "Generate Final Answer":
        Final\_Output = llm(question, memory)
        return final output
   
    if tool\_selection\['tool\_name'\] == "Calculator":
        Ask\_Math\_Question\_To\_LLM(question, memory)
        Append results to memory
        Agent(question, memory)

In summary, a data agent has access to planning capability, memory, multiple data access tools, and means of performing related analytical tasks. Figure 3 shows the general architecture of a data agent.

![Image 25: Agent has a core, memory, planning module, and tools.](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/data-agent-general-architecture.png)

_Figure 3. General architecture of a data agent_

Data agent example[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#data_agent_example)
-----------------------------------------------------------------------------------------------------------------------------

This section provides an example that showcases how different tools can be used together to solve business questions. The key advantage for using an agent in a scenario like this is that the user doesn’t need to know details about the database or the technical skill to run queries.

**Question**: “How much excess inventory do I have for Google Pixel 6?”  
**Answer**: Based on the retrieved information from the inventory system, you currently have 80 units of excess inventory for Google Pixel 6. This calculation is derived by subtracting the minimum required quantity (20) from the current quantity in stock (100). (See above for source data.)

![Image 26: Screenshot of sample data agent output that readsd: “Based on the retrieved information from the inventory system, you currently have 80 units of excess inventory for the Google Pixel 6. This calculation is derived by subtracting the minimum required quantity (20) from the current quantity in stock (100).”
](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/data-agent-sample-output.png)

_Figure 4. Sample data agent output_

To solve this question, the agent performed the following steps:

**Step 1: QueryDB tool**

*   Generate SQL
*   Query database
*   Store results in memory

**Step 2: Calculator tool**

*   Solve math problem using LLM
*   Store results in memory. Note that this can be replaced with code generation plus code execution. To learn more about dynamic tools, see [Build an LLM-Powered API Agent for Task Execution](https://developer.nvidia.com/blog/build-an-llm-powered-api-agent-for-task-execution/).

**Step 3: Final answer generation**

The following prompt is for the agent core LLM after SQL is generated.

"""
<s\> \[INST\]You are an agent capable of using a variety of TOOLS to answer a data analytics question.
Always use MEMORY to help select the TOOLS to be used.

MEMORY
Previous Question:  How much excess inventory do we have for 'Google Pixel 6'?
SQL Query:

SELECT
    inventory.id,
    inventory.product\_id,
    inventory.quantity,
    inventory.min\_required,
    products.name
FROM
    inventory
JOIN
    products ON inventory.product\_id = products.id
WHERE
    products.name = 'Google Pixel 6';
Retrieved Information: \[(7, 7, 100, 20, 'Google Pixel 6')\]

TOOLS
- Generate Final Answer: Use if answer to User's question can be given with MEMORY
- Calculator: Use this tool to solve mathematical problems.
- Query\_Database: Write an SQL Query to query the Database.

ANSWER FORMAT
\`\`\`json
{
    "tool\_name": "Calculator"
}
\`\`\`
\[/INST\]
User: How much excess inventory do we have for 'Google Pixel 6'?

Assistant: \`\`\`json
{
    "tool\_name": """

Key considerations when building data agent applications[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#key_considerations_when_building_data_agent_applications)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Keep in mind the following key considerations when building your LLM agent application.

### Scaling the tools[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#scaling_the_tools)

Imagine a case with 100K tables and 100 tools, rather than three tables and three tools. One way to accommodate this type of scaling is to add an intermediate RAG step. This step might pull in the top five most relevant tools for the agent to select from. This can apply to memory, database schema, or any other options that the agent needs to consider.

### Working with multiple vector databases[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#working_with_multiple_vector_databases)

You can also build a topical router to direct the queries to the correct database in situations with multiple SQL or vector databases.

### Better planning for implementation[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#better_planning_for_implementation)

A simple linear solver to implement a greedy iterative solution is featured here. It can be replaced by a task decomposition module or a plan compiler of sorts to generate a more efficient plan of execution.

Summary[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#summary)
-------------------------------------------------------------------------------------------------------

This post has explained the basics of how to build an LLM agent application for data analytics to help familiarize you with the concepts behind building agents. I highly recommend exploring the open-source ecosystem to select the best agent framework for your application.

Ready to build your own LLM data agent for production? Check out the [AI Chatbot with Retrieval-Augmented Generation](https://www.nvidia.com/en-us/ai-data-science/ai-workflows/generative-ai-chatbots/) free hands-on lab to help you build reliable and scalable solutions.

To read more about LLM agents, see [Build an LLM-Powered API Agent for Task Execution](https://developer.nvidia.com/blog/build-an-llm-powered-api-agent-for-task-execution/).

## Metadata

```json
{
  "title": "Build an LLM-Powered Data Agent for Data Analysis | NVIDIA Technical Blog",
  "description": "An AI agent is a system consisting of planning capabilities, memory, and tools to perform tasks requested by a user. For complex tasks such as data analytics or…",
  "url": "https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/",
  "content": "An AI agent is a system consisting of planning capabilities, memory, and tools to perform tasks requested by a user. For complex tasks such as data analytics or interacting with complex systems, your application may depend on ‌collaboration among different types of agents. For more context, see [Introduction to LLM Agents](https://developer.nvidia.com/blog/introduction-to-llm-agents/) and [Building Your First LLM Agent Application](https://developer.nvidia.com/blog/building-your-first-llm-agent-application/).\n\nThis post explains the agent types required to build an accurate LLM application that can handle nuanced data analysis tasks when queried. It walks through an example use case for building a data analyst agent application, including code snippets. Finally, it provides some considerations for AI developers to consider when optimizing and building LLM agent apps.\n\nLLM agent types for data analysis tasks[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#llm_agent_types_for_data_analysis_tasks)\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nTo begin, this section explains two main types of LLM agents and how they work—data agents and API or execution agents. I’ll also present an agent swarm use case, which involves multiple agents collaborating to solve a problem. Note that these agent types somewhat represent the ends of a spectrum. Blended, purpose-built agents can be created for specific use cases.\n\n### Data agents[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#data_agents)\n\nData agents are typically designed for an extractive goal. In other words, data agents assist users in extracting information from a wide range of data sources. They help with assistive reasoning tasks.\n\nFor example, a financial analyst might ask, “In how many quarters of this year did the company have a positive cash flow?” This type of question requires reasoning, search (structured, unstructured, or both), and planning capabilities.\n\n### API or execution agents[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#api_or_execution_agents)\n\nAPI or execution agents are designed for an execution goal. These agents carry out a task or set of tasks requested by a user.\n\nConsider the same financial analyst working with an Excel spreadsheet that contains the past year’s closing prices for 10 stocks. The analyst wants to organize these closing prices according to one or more statistical formulas. Excel APIs need to be chained together to perform this task. For another API agent example, see the [Google Places API Copilot Demo](https://huggingface.co/spaces/Nexusflow/NexusRaven-V2-Demo).\n\n### Agent swarms[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#agent_swarms)\n\nAgent swarms involve multiple data agents and multiple API agents collaborating in a decentralized manner to solve a complex problem**.** Agent swarms are designed for workflows that include both extractive and execution tasks that require different forms of planning and agent core harnesses.\n\nFor example, imagine that the financial analyst wants to study the top five fast food stocks for investment planning. The sequence of actions needed to reach this goal are outlined below and in Figure 1.\n\n1.  Mine stock prices. The data agent hits a structured database with SQL or pandas or Quandl API.\n2.  Extract more relevant information from 10-K and 10-Q reports. Execute search engine calls to get forms using data agent. Extract information using data agent [retrieval-augmented generation](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/) (RAG) calls.\n3.  Store the information in Excel. API agent calls the Excel API.\n4.  Extract user sentiment from social media content. Execute social media API calls using data mining with data agent. Perform sentiment analysis using RAG data agent.\n5.  Use preselected metrics to generate indicators using API agent (Sheets API).\n6.  Generate the report using API agent.\n7.  Upload key graphs, plots, and charts to a PowerPoint slide using API agent (PowerPoint API).\n\n![Image 23: Flowchart diagram showing a natural workflow for multiple agents collaborating together to solve a problem.](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/complex-workflow-multiple-data-agents-flowchart.png)\n\n_Figure 1.  A general conceptual flow of the execution of a complex workflow solved with multiple agents_\n\nAs more types of LLM agents are modeled, they can interact with each other in the agent swarm to effectively solve problems. Constraining the problem into different agent verticals enables building agents with smaller models. This requires less effort for customization and retains modularity, which in turn provides benefits for adding new features, selecting the features you want, and simplifying deployment scaling. In this ecosystem, every agent looks at another agent like a tool and uses its help when required.\n\nBuilding a data analyst agent[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#building_a_data_analyst_agent)\n---------------------------------------------------------------------------------------------------------------------------------------------------\n\nWith this general taxonomy as a foundation, this section dives into building a data agent for a use case of talking to an SQL database for inventory management. The following discussion assumes you have read [Building Your First LLM Agent Application](https://developer.nvidia.com/blog/building-your-first-llm-agent-application/), or are otherwise familiar with the basics of LLM agents.\n\n### Choose an LLM[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#choose_an_llm)\n\nBegin by identifying which LLM to use. This example uses the [Mixtral 8x7B LLM](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/mixtral-8x7b) available in the NVIDIA NGC catalog. It accelerates various models and makes them available as APIs. The first API calls per model are free for experimentation.\n\nNote that if you’re working with a model that isn’t tuned to handle agent workflows, you can reformulate the prompts below as a series of multiple-choice questions (MCQs). This should work, as most of the models are instruction-tuned to handle MCQs. [Learn more about fine-tuning](https://docs.nvidia.com/nemo-framework/user-guide/latest/playbooks/llama2sft.html).\n\n### Select a use case[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#select_a_use_case)\n\nNext, select a use case. The use case for this post is talking to an SQL database for inventory management. Then populate that database with, for example, three tables.\n\nNote that the information presented below is for exemplary purposes only and is not intended to convey actual details.\n\nsuppliers\\_data = \\[\n    {\"name\": \"Samsung Electronics\", \"address\": \"Seoul, South Korea\", \"contact\": \"800-726-7864\"},\n    {\"name\": \"Apple Inc.\", \"address\": \"Cupertino, California, USA\", \"contact\": \"800–692–7753\"},\n    {\"name\": \"OnePlus Technology\", \"address\": \"Shenzhen, Guangdong, China\", \"contact\": \"400-888-1111\"},\n    {\"name\": \"Google LLC\", \"address\": \"Mountain View, California, USA\", \"contact\": \"855-836-3987\"},\n    {\"name\": \"Xiaomi Corporation\", \"address\": \"Beijing, China\", \"contact\": \"1800-103-6286\"},\n\\]\n \nproducts\\_data = \\[\n    {\"name\": \"Samsung Galaxy S21\", \"description\": \"Samsung flagship smartphone\", \"price\": 799.99, \"supplier\\_id\": 1},\n    {\"name\": \"Samsung Galaxy Note 20\", \"description\": \"Samsung premium smartphone with stylus\", \"price\": 999.99, \"supplier\\_id\": 1},\n    {\"name\": \"iPhone 13 Pro\", \"description\": \"Apple flagship smartphone\", \"price\": 999.99, \"supplier\\_id\": 2},\n    {\"name\": \"iPhone SE\", \"description\": \"Apple budget smartphone\", \"price\": 399.99, \"supplier\\_id\": 2},\n    {\"name\": \"OnePlus 9\", \"description\": \"High performance smartphone\", \"price\": 729.00, \"supplier\\_id\": 3},\n    {\"name\": \"OnePlus Nord\", \"description\": \"Mid-range smartphone\", \"price\": 499.00, \"supplier\\_id\": 3},\n    {\"name\": \"Google Pixel 6\", \"description\": \"Google's latest smartphone\", \"price\": 599.00, \"supplier\\_id\": 4},\n    {\"name\": \"Google Pixel 5a\", \"description\": \"Affordable Google smartphone\", \"price\": 449.00, \"supplier\\_id\": 4},\n    {\"name\": \"Xiaomi Mi 11\", \"description\": \"Xiaomi high-end smartphone\", \"price\": 749.99, \"supplier\\_id\": 5},\n    {\"name\": \"Xiaomi Redmi Note 10\", \"description\": \"Xiaomi budget smartphone\", \"price\": 199.99, \"supplier\\_id\": 5},\n\\]\n \ninventory\\_data = \\[\n    {\"product\\_id\": 1, \"quantity\": 150, \"min\\_required\": 30},\n    {\"product\\_id\": 2, \"quantity\": 100, \"min\\_required\": 20},\n    {\"product\\_id\": 3, \"quantity\": 120, \"min\\_required\": 30},\n    {\"product\\_id\": 4, \"quantity\": 80, \"min\\_required\": 15},\n    {\"product\\_id\": 5, \"quantity\": 200, \"min\\_required\": 40},\n    {\"product\\_id\": 6, \"quantity\": 150, \"min\\_required\": 25},\n    {\"product\\_id\": 7, \"quantity\": 100, \"min\\_required\": 20},\n    {\"product\\_id\": 8, \"quantity\": 90, \"min\\_required\": 18},\n    {\"product\\_id\": 9, \"quantity\": 170, \"min\\_required\": 35},\n    {\"product\\_id\": 10, \"quantity\": 220, \"min\\_required\": 45},\n\nFor experimentation, store the preceding entries in an SQLite database. These entries are tailored for the schema shown in Figure 2. The intention is to create a simplified version of a database that is typically at the heart of any inventory management system. These databases contain information about current inventory levels, suppliers, and more.\n\n![Image 24: Three tables containing the database schema: Inventory, Product, and Supplier.](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/sample-database-tables.png)\n\n_Figure 2. Schema of the sample database to showcase the use case_\n\n### LLM agent components[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#llm_agent_components)\n\nAn LLM agent contains four key components: tools, memory module, planning module, and agent core. Details about the components for this example are provided below.\n\n#### Tools\n\nThis example uses the following two tools:\n\n*   **Calculator:** For any basic calculations needed after querying the data. To keep it simple, an LLM is used here. Any service or API can be added to solve said problem.\n*   **SQL Query Executor:** For querying the database for raw data.\n\n#### Memory\n\nA simple buffer or list to keep track of all the agent’s actions.\n\n#### Planning\n\nA linear greedy approach. To achieve this, create a “faux tool” for “generate the final answer.” This idea is addressed further in the section below.\n\n#### Agent core\n\nTime to put everything together. The prompt for the agent core LLM looks something like this:\n\n\"\"\"<s\\> \\[INST\\]You are an agent capable of using a variety of TOOLS to answer a data analytics question.\nAlways use MEMORY to help select the TOOLS to be used.\n\nMEMORY\n<Empty\\>\n\nTOOLS\n- Generate Final Answer: Use if answer to User's question can be given with MEMORY\n- Calculator: Use this tool to solve mathematical problems.\n- Query\\_Database: Write an SQL Query to query the Database.\n\nANSWER FORMAT\n\\`\\`\\`json\n{\n    \"tool\\_name\": \"Calculator\"\n}\n\\`\\`\\`\n\\[/INST\\]\nUser: {User's Question}\n\nAssistant: \\`\\`\\`json\n{\n    \"tool\\_name\": \"\"\"\n\nThe preceding prompt includes all the tools and related information. You can design the core’s code harness in a way such that, given any tool but the “generate the final answer” faux tool, the agent will append the results of the tool used to memory and re-access the situation. This is an iterative greedy approach where the “best” decision is made for the individual step.\n\nif tool\\_selection\\['tool\\_name'\\] == \"Query\\_Database\":\n        Generate\\_SQL\\_Query(question, memory, schema)\n        QueryDB\n        Append results to memory\n        Agent(question, memory)\n\n    if tool\\_selection\\['tool\\_name'\\] == \"Generate Final Answer\":\n        Final\\_Output = llm(question, memory)\n        return final output\n   \n    if tool\\_selection\\['tool\\_name'\\] == \"Calculator\":\n        Ask\\_Math\\_Question\\_To\\_LLM(question, memory)\n        Append results to memory\n        Agent(question, memory)\n\nIn summary, a data agent has access to planning capability, memory, multiple data access tools, and means of performing related analytical tasks. Figure 3 shows the general architecture of a data agent.\n\n![Image 25: Agent has a core, memory, planning module, and tools.](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/data-agent-general-architecture.png)\n\n_Figure 3. General architecture of a data agent_\n\nData agent example[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#data_agent_example)\n-----------------------------------------------------------------------------------------------------------------------------\n\nThis section provides an example that showcases how different tools can be used together to solve business questions. The key advantage for using an agent in a scenario like this is that the user doesn’t need to know details about the database or the technical skill to run queries.\n\n**Question**: “How much excess inventory do I have for Google Pixel 6?”  \n**Answer**: Based on the retrieved information from the inventory system, you currently have 80 units of excess inventory for Google Pixel 6. This calculation is derived by subtracting the minimum required quantity (20) from the current quantity in stock (100). (See above for source data.)\n\n![Image 26: Screenshot of sample data agent output that readsd: “Based on the retrieved information from the inventory system, you currently have 80 units of excess inventory for the Google Pixel 6. This calculation is derived by subtracting the minimum required quantity (20) from the current quantity in stock (100).”\n](https://developer-blogs.nvidia.com/wp-content/uploads/2024/02/data-agent-sample-output.png)\n\n_Figure 4. Sample data agent output_\n\nTo solve this question, the agent performed the following steps:\n\n**Step 1: QueryDB tool**\n\n*   Generate SQL\n*   Query database\n*   Store results in memory\n\n**Step 2: Calculator tool**\n\n*   Solve math problem using LLM\n*   Store results in memory. Note that this can be replaced with code generation plus code execution. To learn more about dynamic tools, see [Build an LLM-Powered API Agent for Task Execution](https://developer.nvidia.com/blog/build-an-llm-powered-api-agent-for-task-execution/).\n\n**Step 3: Final answer generation**\n\nThe following prompt is for the agent core LLM after SQL is generated.\n\n\"\"\"\n<s\\> \\[INST\\]You are an agent capable of using a variety of TOOLS to answer a data analytics question.\nAlways use MEMORY to help select the TOOLS to be used.\n\nMEMORY\nPrevious Question:  How much excess inventory do we have for 'Google Pixel 6'?\nSQL Query:\n\nSELECT\n    inventory.id,\n    inventory.product\\_id,\n    inventory.quantity,\n    inventory.min\\_required,\n    products.name\nFROM\n    inventory\nJOIN\n    products ON inventory.product\\_id = products.id\nWHERE\n    products.name = 'Google Pixel 6';\nRetrieved Information: \\[(7, 7, 100, 20, 'Google Pixel 6')\\]\n\nTOOLS\n- Generate Final Answer: Use if answer to User's question can be given with MEMORY\n- Calculator: Use this tool to solve mathematical problems.\n- Query\\_Database: Write an SQL Query to query the Database.\n\nANSWER FORMAT\n\\`\\`\\`json\n{\n    \"tool\\_name\": \"Calculator\"\n}\n\\`\\`\\`\n\\[/INST\\]\nUser: How much excess inventory do we have for 'Google Pixel 6'?\n\nAssistant: \\`\\`\\`json\n{\n    \"tool\\_name\": \"\"\"\n\nKey considerations when building data agent applications[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#key_considerations_when_building_data_agent_applications)\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nKeep in mind the following key considerations when building your LLM agent application.\n\n### Scaling the tools[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#scaling_the_tools)\n\nImagine a case with 100K tables and 100 tools, rather than three tables and three tools. One way to accommodate this type of scaling is to add an intermediate RAG step. This step might pull in the top five most relevant tools for the agent to select from. This can apply to memory, database schema, or any other options that the agent needs to consider.\n\n### Working with multiple vector databases[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#working_with_multiple_vector_databases)\n\nYou can also build a topical router to direct the queries to the correct database in situations with multiple SQL or vector databases.\n\n### Better planning for implementation[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#better_planning_for_implementation)\n\nA simple linear solver to implement a greedy iterative solution is featured here. It can be replaced by a task decomposition module or a plan compiler of sorts to generate a more efficient plan of execution.\n\nSummary[](https://developer.nvidia.com/blog/build-an-llm-powered-data-agent-for-data-analysis/#summary)\n-------------------------------------------------------------------------------------------------------\n\nThis post has explained the basics of how to build an LLM agent application for data analytics to help familiarize you with the concepts behind building agents. I highly recommend exploring the open-source ecosystem to select the best agent framework for your application.\n\nReady to build your own LLM data agent for production? Check out the [AI Chatbot with Retrieval-Augmented Generation](https://www.nvidia.com/en-us/ai-data-science/ai-workflows/generative-ai-chatbots/) free hands-on lab to help you build reliable and scalable solutions.\n\nTo read more about LLM agents, see [Build an LLM-Powered API Agent for Task Execution](https://developer.nvidia.com/blog/build-an-llm-powered-api-agent-for-task-execution/).",
  "publishedTime": "2024-02-20T19:30+00:00",
  "usage": {
    "tokens": 4057
  }
}
```
