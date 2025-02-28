---
title: PromptQL: A Data Access Agent for business data
description: Bring transparency, steerability & reliability to AI applications interacting with business data. Out-of-the-box connectors for databases, APIs and code.
url: https://promptql.hasura.io/?utm_source=freeman-forrest&utm_medium=twitter&utm_campaign=hasura-october&utm_term=svaldarrama&utm_content=promptql
timestamp: 2025-01-20T16:13:29.756Z
domain: promptql.hasura.io
path: root
---

# PromptQL: A Data Access Agent for business data


Bring transparency, steerability & reliability to AI applications interacting with business data. Out-of-the-box connectors for databases, APIs and code.


## Content

### Dynamic Query Planning

PromptQL builds a dynamic query plan that can be modified during execution based on intermediate results or explicit instructions from the user. It incorporates control structures (e.g., if-else statements) to handle different scenarios.

This overcomes a rigid retrieval based approach on precomputed embeddings, similarity search, predefined tools, etc, lacking the ability to adjust retrieval strategies dynamically.

Find all products that had declining sales for three consecutive months, and if none, expand the search to products with declining sales for two months.

#### Query plan

*   Search for products with sales decline over three months.
*   Check Results: If none found, adjust criteria.
*   Modify the query to search for two months.
*   Provide the list of products.

#### Executed

### Connectors to Any Kind of Data

DDN provides connectors to seamlessly integrate with any data sources, allowing AI models to access and interact with all your data under a unified schema.

**Problem:** Traditional RAG systems struggle to integrate data from diverse sources such as SQL databases, NoSQL stores, APIs, and SaaS platforms.

Generate a report of our top 10 customers by ARR, including their purchase history, support tickets, and recent interactions.

#### Query plan

*   Identify the top 10 customers by ARR using invoice data \[in BigQuery\]
*   Retrieve customer purchase history for each customer \[from PostgreSQL\]
*   Fetch support ticket data for each customer \[from Zendesk API\]
*   Obtain recent interaction records for each customer \[from Salesforce API\]
*   Combine information from all sources.
*   Present the consolidated data as a table.

#### Executed

### Computation

PromptQL has a programmatic runtime environment that allows AI to execute complex computations, data transformations, and statistical analyses. PromptQL handles large datasets by processing data in batches outside the LLM's context window. It can call another LLM within the runtime to analyze text data.

Calculate the average customer lifetime value (CLTV) segmented by marketing channel for the past year.

#### Query plan

*   Gather purchase histories for each customer.
*   Group customers by marketing channels.
*   Calculate average CLTV per segment.
*   Provide the computed values.

#### Executed

### Actions & Mutations

PromptQL enables AI to perform actions and mutations by executing commands that can update data, call APIs, or invoke functions, allowing for end-to-end task completion.

**Problem:** Many AI applications are limited to data retrieval and cannot perform actions or mutations, such as updating records or triggering workflows.

For customers with overdue invoices exceeding $10,000, send a payment reminder email and flag their account as 'At Risk'.

#### Query plan

*   Identify customers that meet the criteria.
*   Update their records in Salesforce.
*   Fetch additional information about each customer.
*   Write and send reminder emails.

#### Executed

### Structured Memory

**Problem:** LLMs have limited context windows, making it difficult to handle large datasets or maintain conversation context over long interactions, leading to potential loss of information and hallucinations.

**Solution:** PromptQL uses memory artifacts to store and retrieve information outside the LLM's context window. This ensures consistency, accuracy, and the ability to handle large-scale data without overloading the LLM.

Based on the sales performance report we discussed earlier, project next quarter's sales based on the same growth rate.

#### Query plan

*   Retrieve previously generated report from the stored memory artifact.
*   Compute future sales.
*   Present summary and projections.

#### Executed

### Explainability

**Problem:** RAG systems operate like black boxes. When an AI model retrieves information to generate a response, it can’t provide insights into how or why specific data was selected. It is difficult to verify the sources or reasoning behind the LLM's answers.

**Solution:** PromptQL provides detailed execution plans and can be explicitly asked to explain each step.

Explain your method to generate the projections

#### PromptQL

I checked the memory artifacts for the history of the referenced sales report. Then I extracted the latest sales data and current growth rate pattern from the data. Then I calculated the next quarter projection using the existing growth rate and validated the projection against historical trends. Finally I presented the results with key assumptions

### Fine-Grained Authorization

**Problem:** RAG lacks built-in mechanisms for enforcing data access permissions and security protocols. There is always the potential risk of exposure of sensitive data. It cannot tailor data access based on user roles or credentials.

**Solution:** Hasura DDN integrates fine-grained, role-based access control directly into the data querying process, ensuring that all data access adheres to predefined authorization policies at row, column, and object levels.

Provide me with the sales data for all the regions for the past month. \[As a regional manager\]

#### PromptQL

You are the regional manager for the state of California, and hence I can only provide the information from your region. Here is the latest sales data over the past month for California.

#### Sales data for last month

## Metadata

```json
{
  "title": "PromptQL: A Data Access Agent for business data",
  "description": "Bring transparency, steerability & reliability to AI applications interacting with business data. Out-of-the-box connectors for databases, APIs and code.",
  "url": "https://promptql.hasura.io/",
  "content": "### Dynamic Query Planning\n\nPromptQL builds a dynamic query plan that can be modified during execution based on intermediate results or explicit instructions from the user. It incorporates control structures (e.g., if-else statements) to handle different scenarios.\n\nThis overcomes a rigid retrieval based approach on precomputed embeddings, similarity search, predefined tools, etc, lacking the ability to adjust retrieval strategies dynamically.\n\nFind all products that had declining sales for three consecutive months, and if none, expand the search to products with declining sales for two months.\n\n#### Query plan\n\n*   Search for products with sales decline over three months.\n*   Check Results: If none found, adjust criteria.\n*   Modify the query to search for two months.\n*   Provide the list of products.\n\n#### Executed\n\n### Connectors to Any Kind of Data\n\nDDN provides connectors to seamlessly integrate with any data sources, allowing AI models to access and interact with all your data under a unified schema.\n\n**Problem:** Traditional RAG systems struggle to integrate data from diverse sources such as SQL databases, NoSQL stores, APIs, and SaaS platforms.\n\nGenerate a report of our top 10 customers by ARR, including their purchase history, support tickets, and recent interactions.\n\n#### Query plan\n\n*   Identify the top 10 customers by ARR using invoice data \\[in BigQuery\\]\n*   Retrieve customer purchase history for each customer \\[from PostgreSQL\\]\n*   Fetch support ticket data for each customer \\[from Zendesk API\\]\n*   Obtain recent interaction records for each customer \\[from Salesforce API\\]\n*   Combine information from all sources.\n*   Present the consolidated data as a table.\n\n#### Executed\n\n### Computation\n\nPromptQL has a programmatic runtime environment that allows AI to execute complex computations, data transformations, and statistical analyses. PromptQL handles large datasets by processing data in batches outside the LLM's context window. It can call another LLM within the runtime to analyze text data.\n\nCalculate the average customer lifetime value (CLTV) segmented by marketing channel for the past year.\n\n#### Query plan\n\n*   Gather purchase histories for each customer.\n*   Group customers by marketing channels.\n*   Calculate average CLTV per segment.\n*   Provide the computed values.\n\n#### Executed\n\n### Actions & Mutations\n\nPromptQL enables AI to perform actions and mutations by executing commands that can update data, call APIs, or invoke functions, allowing for end-to-end task completion.\n\n**Problem:** Many AI applications are limited to data retrieval and cannot perform actions or mutations, such as updating records or triggering workflows.\n\nFor customers with overdue invoices exceeding $10,000, send a payment reminder email and flag their account as 'At Risk'.\n\n#### Query plan\n\n*   Identify customers that meet the criteria.\n*   Update their records in Salesforce.\n*   Fetch additional information about each customer.\n*   Write and send reminder emails.\n\n#### Executed\n\n### Structured Memory\n\n**Problem:** LLMs have limited context windows, making it difficult to handle large datasets or maintain conversation context over long interactions, leading to potential loss of information and hallucinations.\n\n**Solution:** PromptQL uses memory artifacts to store and retrieve information outside the LLM's context window. This ensures consistency, accuracy, and the ability to handle large-scale data without overloading the LLM.\n\nBased on the sales performance report we discussed earlier, project next quarter's sales based on the same growth rate.\n\n#### Query plan\n\n*   Retrieve previously generated report from the stored memory artifact.\n*   Compute future sales.\n*   Present summary and projections.\n\n#### Executed\n\n### Explainability\n\n**Problem:** RAG systems operate like black boxes. When an AI model retrieves information to generate a response, it can’t provide insights into how or why specific data was selected. It is difficult to verify the sources or reasoning behind the LLM's answers.\n\n**Solution:** PromptQL provides detailed execution plans and can be explicitly asked to explain each step.\n\nExplain your method to generate the projections\n\n#### PromptQL\n\nI checked the memory artifacts for the history of the referenced sales report. Then I extracted the latest sales data and current growth rate pattern from the data. Then I calculated the next quarter projection using the existing growth rate and validated the projection against historical trends. Finally I presented the results with key assumptions\n\n### Fine-Grained Authorization\n\n**Problem:** RAG lacks built-in mechanisms for enforcing data access permissions and security protocols. There is always the potential risk of exposure of sensitive data. It cannot tailor data access based on user roles or credentials.\n\n**Solution:** Hasura DDN integrates fine-grained, role-based access control directly into the data querying process, ensuring that all data access adheres to predefined authorization policies at row, column, and object levels.\n\nProvide me with the sales data for all the regions for the past month. \\[As a regional manager\\]\n\n#### PromptQL\n\nYou are the regional manager for the state of California, and hence I can only provide the information from your region. Here is the latest sales data over the past month for California.\n\n#### Sales data for last month",
  "usage": {
    "tokens": 1037
  }
}
```
