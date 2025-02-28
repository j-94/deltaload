---
title: Notion – The all-in-one workspace for your notes, tasks, wikis, and databases.
description: A new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team
url: https://proud-botany-7dd.notion.site/How-do-Pipelines-work-eaa03a8f0e2748809e09cb432d56e675
timestamp: 2025-01-20T15:51:30.143Z
domain: proud-botany-7dd.notion.site
path: How-do-Pipelines-work-eaa03a8f0e2748809e09cb432d56e675
---

# Notion – The all-in-one workspace for your notes, tasks, wikis, and databases.


A new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team


## Content

What is a pipeline?
-------------------

Pipelines connect Data Sources to Operators and Operators to Actions. Operators are used to process data and run ML algorithms, actions are used to take action based on the results of the operators.

Note that if you try to connect an Action to an Integration you will get a connection error.

Connect invoice data to an RFM operator and generate an RFM group for each customer.

Use a .CSV file uploader to upload the results of the RFM operator (which is RFM groups).

Each operator and action has input(s) and output(s). While some of the operators/actions and actions allows us to connect a single input, some of them allow us to connect multiple outputs. When an operator is executed, it always creates an output table(s) and then this table(s) can be used in the next operator or action.

In the next two examples, we will explain how operators input and output tables are used.

Explanation with Example #1

Step #1 → We will connect a client data source to a custom SQL operator.

Step#2 → When we click on edit, we can see the editor to write SQL.

Step#3→ On the right panel of the SQL editor, we can verify the client data source is connected to that current operator.

Step#4→ On the next step, let's connect the customer's invoice data source.

Step#5 → When we open the Custom SQL operator's editor by using the edit button, we can verify the 2nd data source is also connected.

The steps explained above can also be seen on the video below.

![Image 8: Loading...](blob:https://proud-botany-7dd.notion.site/df8da4a812cd298affcba22f13177edc)

Explanation with Example #2

We will continue with the previous example to create the output of Custom SQL and then use it in another operator.

Step#1 → On the SQL editor page, we will run a query.

Step#2 → Once we verified that this is the data we want to work on, we can save it. Step#3 → We will execute the operator by clicking on the play button displayed on the right upper side of operator box. Step#4→ When the execution is completed, we can connect another Custom SQL operator.

Step#5 → When we open the SQL editor of the second Custom SQL operator, we can verify that there is only one data source connected to the second operator.

The steps explained above can also be seen on the video below

Check our new Pipelines design and experience below.

![Image 9: Loading...](blob:https://proud-botany-7dd.notion.site/df8da4a812cd298affcba22f13177edc)

## Metadata

```json
{
  "title": "Notion – The all-in-one workspace for your notes, tasks, wikis, and databases.",
  "description": "A new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team",
  "url": "https://proud-botany-7dd.notion.site/How-do-Pipelines-work-eaa03a8f0e2748809e09cb432d56e675",
  "content": "What is a pipeline?\n-------------------\n\nPipelines connect Data Sources to Operators and Operators to Actions. Operators are used to process data and run ML algorithms, actions are used to take action based on the results of the operators.\n\nNote that if you try to connect an Action to an Integration you will get a connection error.\n\nConnect invoice data to an RFM operator and generate an RFM group for each customer.\n\nUse a .CSV file uploader to upload the results of the RFM operator (which is RFM groups).\n\nEach operator and action has input(s) and output(s). While some of the operators/actions and actions allows us to connect a single input, some of them allow us to connect multiple outputs. When an operator is executed, it always creates an output table(s) and then this table(s) can be used in the next operator or action.\n\nIn the next two examples, we will explain how operators input and output tables are used.\n\nExplanation with Example #1\n\nStep #1 → We will connect a client data source to a custom SQL operator.\n\nStep#2 → When we click on edit, we can see the editor to write SQL.\n\nStep#3→ On the right panel of the SQL editor, we can verify the client data source is connected to that current operator.\n\nStep#4→ On the next step, let's connect the customer's invoice data source.\n\nStep#5 → When we open the Custom SQL operator's editor by using the edit button, we can verify the 2nd data source is also connected.\n\nThe steps explained above can also be seen on the video below.\n\n![Image 8: Loading...](blob:https://proud-botany-7dd.notion.site/df8da4a812cd298affcba22f13177edc)\n\nExplanation with Example #2\n\nWe will continue with the previous example to create the output of Custom SQL and then use it in another operator.\n\nStep#1 → On the SQL editor page, we will run a query.\n\nStep#2 → Once we verified that this is the data we want to work on, we can save it. Step#3 → We will execute the operator by clicking on the play button displayed on the right upper side of operator box. Step#4→ When the execution is completed, we can connect another Custom SQL operator.\n\nStep#5 → When we open the SQL editor of the second Custom SQL operator, we can verify that there is only one data source connected to the second operator.\n\nThe steps explained above can also be seen on the video below\n\nCheck our new Pipelines design and experience below.\n\n![Image 9: Loading...](blob:https://proud-botany-7dd.notion.site/df8da4a812cd298affcba22f13177edc)",
  "usage": {
    "tokens": 568
  }
}
```
