---
title: Agents - Github to Linear
description: Notebooks for data scientists and data analysts.
url: https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59
timestamp: 2025-01-20T16:08:32.510Z
domain: deepnote.com
path: workspace_composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a_project_Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6_notebook_Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59
---

# Agents - Github to Linear


Notebooks for data scientists and data analysts.


## Content

Agents - Github to Linear | Deepnote
===============

C

Composio

[Create a new workspace](https://deepnote.com/onboarding?createWorkspace=true) to start your own projects in Deepnote.

[](https://deepnote.com/workspace/-8ad9f1f9-a21a-4462-a4bb-174bde78f67a)

Agents - Github to Linear

View access

* * *

W

Members at **Composio**

Project is shared with the workspace

Full access

No access

Project is private, workspace members can’t access it. However, it still uses workspace's resources, such as machines and integrations.

Team

View

Can inspect the project, but cannot view or post comments nor execute or edit files.

Team

Comment

Can post and view comments in addition to inspecting the project.

Team

Execute

Can execute code in addition to viewing and commenting, but cannot change anything or use terminals.

Team

Edit

Can use terminals, connect integrations, comment and edit files as well as view and execute.

Team

Full access

Project is shared with the workspace

Team

* * *

Anyone with a link to this project

View

Disabled

Turn link sharing off. Only collaborators can access the project.

View

Can inspect the project, but cannot view or post comments nor execute or edit files.

Comment

Can post and view comments in addition to inspecting the project.

Execute

Can execute code in addition to viewing and commenting, but cannot change anything or use terminals.

Edit

Can use terminals, connect integrations, comment and edit files as well as view and execute.

* * *

Learn more about sharing in [our docs](https://deepnote.com/docs/share-projects).

Copy link

Duplicate

Command palette

ctrl + P

Hide UI

ctrl + .

* * *

Copy link to project

* * *

Duplicate project

Download

![Image 7](https://deepnote.com/static/anonymous-user-icon.svg)

Book a demo

Account settings

* * *

Sign out

Notebooks

Autogen Agent

Autogen Agent-2

* * *

Integrations

Auth

* * *

Files

.cache

image-20240325-164003.png

image-20240327-020018.png

image-20240327-020342.png

* * *

Table of contents

1.  1.  [Github Code Commits --\> Linear Create Issues (Autogen Agent)](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#492addd55bca47de862121f679bed30e)
        1.  [Setup (Install Packages and Connect Tools)](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#80018911661e4de7b1cb4af3639e2126)
        2.  [Agent Code](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#5446a255af1f4867a181593c361bb68e)
        3.  [Powering agents with all Tools](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#2e44b86a2d52447ba74bc3ee7e40c611)
        4.  [Executing the Task](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#411bc036aac2412b91811637a2cc91d0)
    2.  [Want to try out more -\> docs.composio.dev](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#9c1fe01d33f54c66a15feea02da7308e)
        

* * *

![Image 8](https://deepnote.com/api/project/1e32fad6-0d9e-482b-b46d-08f868445ba6/download-file?path=image-20240327-020018.png)

Github Code Commits --\> Linear Create Issues (Autogen Agent)
-------------------------------------------------------------

### Setup (Install Packages and Connect Tools)

1

2

3

4

5

6

7

8

9

# Run this commands in terminal and remove exclamatory mark

!pip install ag2 composio\_autogen \--quiet

# For the auth management and integrations, let's use Composio. 

!composio-cli add github 

# Go through the flow to connect github 

!composio-cli add linear  

# Go through the flow to connect linear. 

### Agent Code

To initialise, perform the following steps:

Configure LLM: Use the gpt-4-1106-preview model. Provide the OpenAI environment key through an environment variable or modify the code directly.

Set Up Assistant Agent: Create it with a system prompt and the LLM configuration. Adjust as needed to improve outcomes.

Establish User Proxy Agent: These agents simulate users, interacting with Autogen agents. They include a function to end the process upon detecting the word "Terminate," as specified in the system prompt.

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

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

import os

from autogen import AssistantAgent, UserProxyAgent

from composio\_autogen import App, Action, ComposioToolset

llm\_config \= {

    "config\_list": \[

        {

            "model": "gpt-4-1106-preview",

            "api\_key": os.environ.get(

                "OPENAI\_API\_KEY", "sk-123131\*\*\*\*"

            ),

        }

    \]

}

super\_agent \= AssistantAgent(

    "chatbot",

    system\_message="""You are a super intelligent personal assistant.

    You have been given a set of tools that you are supposed to choose from.

    You decide the right tool and execute it to achieve your task.

    Reply TERMINATE when the task is done or when user's content is empty""",

    llm\_config=llm\_config,

)

# create a UserProxyAgent instance named "user\_proxy"

user\_proxy \= UserProxyAgent(

    "user\_proxy",

    is\_termination\_msg=lambda x: x.get("content", "")

    and "TERMINATE" in x.get("content", ""),

    human\_input\_mode="NEVER",  # Don't take input from User

    code\_execution\_config={"use\_docker": False},

)

### Powering agents with all Tools

1

2

3

4

5

6

7

# Initialise the Composio Tool Set

composio\_tools \= ComposioToolset()

# Register the preferred Applications, with right executor.

composio\_tools.register\_tools(

    tools=\[App.LINEAR, App.GITHUB\], caller=super\_agent, executor=user\_proxy

)

### Executing the Task

1

2

3

4

5

6

task \= """For all the todos in my last commit of SamparkAI/Docs,

create a linear issue on project name hermes board and assign to right person"""

response \= user\_proxy.initiate\_chat(super\_agent, message=task)

print(response.chat\_history)

Want to try out more -\> docs.composio.dev
------------------------------------------

* * *

* * *

Chat with us

Book a demo

* * *

Shortcuts

[Documentation](https://deepnote.com/docs)[Deepnote crash course](https://deepnote.com/docs/deepnote-crash-course)[Explore](https://deepnote.com/explore)

* * *

[Roadmap](https://portal.productboard.com/deepnote/1-deepnote-product-portal/tabs/1-under-consideration)

You can **view** this project, but can’t make any changes.

Request additional access

Comment

Can post and view comments in addition to inspecting the project.

Execute

Can execute code in addition to viewing and commenting, but cannot change anything or use terminals.

Edit

Can use terminals, connect integrations, comment and edit files as well as view and execute.

View

Comment

Execute

Edit

Collaborators

Only you and members of workspace **Composio** can view this project

View collaborators

![Image 9](https://t.co/i/adsct?bci=3&dv=UTC%26en-US%2Cen%26Google%20Inc.%26Win32%26255%26800%26600%264%2624%26800%26600%260%26na&eci=2&event_id=486a778a-a0da-44d7-bfb4-70743936a7c3&events=%5B%5B%22pageview%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=53796bef-9b54-4e71-98e2-ce633d2e5fe7&tw_document_href=https%3A%2F%2Fdeepnote.com%2Fworkspace%2Fcomposio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a%2Fproject%2FAgents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6%2Fnotebook%2FAutogen%2520Agent-cfb9253cd2c24de587bef8f7c6341c59&tw_iframe_status=0&tw_order_quantity=0&tw_sale_amount=0&txn_id=oc4iq&type=javascript&version=2.3.31)![Image 10](https://analytics.twitter.com/i/adsct?bci=3&dv=UTC%26en-US%2Cen%26Google%20Inc.%26Win32%26255%26800%26600%264%2624%26800%26600%260%26na&eci=2&event_id=486a778a-a0da-44d7-bfb4-70743936a7c3&events=%5B%5B%22pageview%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=53796bef-9b54-4e71-98e2-ce633d2e5fe7&tw_document_href=https%3A%2F%2Fdeepnote.com%2Fworkspace%2Fcomposio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a%2Fproject%2FAgents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6%2Fnotebook%2FAutogen%2520Agent-cfb9253cd2c24de587bef8f7c6341c59&tw_iframe_status=0&tw_order_quantity=0&tw_sale_amount=0&txn_id=oc4iq&type=javascript&version=2.3.31)

![Image 11](https://bat.bing.com/action/0?ti=97113000&tm=gtm002&Ver=2&mid=0bb93771-ea67-4b78-b1d0-3babef35d5b9&bo=1&sid=c21ab0f0d74811ef91105d94ae47acef&vid=c2221280d74811efb8a711edc75de6e7&vids=1&msclkid=N&uach=pv%3D10.0&pi=918639831&lg=en-US&sw=800&sh=600&sc=24&p=https%3A%2F%2Fdeepnote.com%2Fworkspace%2Fcomposio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a%2Fproject%2FAgents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6%2Fnotebook%2FAutogen%2520Agent-cfb9253cd2c24de587bef8f7c6341c59&r=&lt=2595&evt=pageLoad&sv=1&cdb=AQAQ&rn=847227)

## Metadata

```json
{
  "title": "Agents - Github to Linear",
  "description": "Notebooks for data scientists and data analysts.",
  "url": "https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59",
  "content": "Agents - Github to Linear | Deepnote\n===============\n\nC\n\nComposio\n\n[Create a new workspace](https://deepnote.com/onboarding?createWorkspace=true) to start your own projects in Deepnote.\n\n[](https://deepnote.com/workspace/-8ad9f1f9-a21a-4462-a4bb-174bde78f67a)\n\nAgents - Github to Linear\n\nView access\n\n* * *\n\nW\n\nMembers at **Composio**\n\nProject is shared with the workspace\n\nFull access\n\nNo access\n\nProject is private, workspace members can’t access it. However, it still uses workspace's resources, such as machines and integrations.\n\nTeam\n\nView\n\nCan inspect the project, but cannot view or post comments nor execute or edit files.\n\nTeam\n\nComment\n\nCan post and view comments in addition to inspecting the project.\n\nTeam\n\nExecute\n\nCan execute code in addition to viewing and commenting, but cannot change anything or use terminals.\n\nTeam\n\nEdit\n\nCan use terminals, connect integrations, comment and edit files as well as view and execute.\n\nTeam\n\nFull access\n\nProject is shared with the workspace\n\nTeam\n\n* * *\n\nAnyone with a link to this project\n\nView\n\nDisabled\n\nTurn link sharing off. Only collaborators can access the project.\n\nView\n\nCan inspect the project, but cannot view or post comments nor execute or edit files.\n\nComment\n\nCan post and view comments in addition to inspecting the project.\n\nExecute\n\nCan execute code in addition to viewing and commenting, but cannot change anything or use terminals.\n\nEdit\n\nCan use terminals, connect integrations, comment and edit files as well as view and execute.\n\n* * *\n\nLearn more about sharing in [our docs](https://deepnote.com/docs/share-projects).\n\nCopy link\n\nDuplicate\n\nCommand palette\n\nctrl + P\n\nHide UI\n\nctrl + .\n\n* * *\n\nCopy link to project\n\n* * *\n\nDuplicate project\n\nDownload\n\n![Image 7](https://deepnote.com/static/anonymous-user-icon.svg)\n\nBook a demo\n\nAccount settings\n\n* * *\n\nSign out\n\nNotebooks\n\nAutogen Agent\n\nAutogen Agent-2\n\n* * *\n\nIntegrations\n\nAuth\n\n* * *\n\nFiles\n\n.cache\n\nimage-20240325-164003.png\n\nimage-20240327-020018.png\n\nimage-20240327-020342.png\n\n* * *\n\nTable of contents\n\n1.  1.  [Github Code Commits --\\> Linear Create Issues (Autogen Agent)](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#492addd55bca47de862121f679bed30e)\n        1.  [Setup (Install Packages and Connect Tools)](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#80018911661e4de7b1cb4af3639e2126)\n        2.  [Agent Code](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#5446a255af1f4867a181593c361bb68e)\n        3.  [Powering agents with all Tools](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#2e44b86a2d52447ba74bc3ee7e40c611)\n        4.  [Executing the Task](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#411bc036aac2412b91811637a2cc91d0)\n    2.  [Want to try out more -\\> docs.composio.dev](https://deepnote.com/workspace/composio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a/project/Agents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6/notebook/Autogen%20Agent-cfb9253cd2c24de587bef8f7c6341c59#9c1fe01d33f54c66a15feea02da7308e)\n        \n\n* * *\n\n![Image 8](https://deepnote.com/api/project/1e32fad6-0d9e-482b-b46d-08f868445ba6/download-file?path=image-20240327-020018.png)\n\nGithub Code Commits --\\> Linear Create Issues (Autogen Agent)\n-------------------------------------------------------------\n\n### Setup (Install Packages and Connect Tools)\n\n1\n\n2\n\n3\n\n4\n\n5\n\n6\n\n7\n\n8\n\n9\n\n# Run this commands in terminal and remove exclamatory mark\n\n!pip install ag2 composio\\_autogen \\--quiet\n\n# For the auth management and integrations, let's use Composio. \n\n!composio-cli add github \n\n# Go through the flow to connect github \n\n!composio-cli add linear  \n\n# Go through the flow to connect linear. \n\n### Agent Code\n\nTo initialise, perform the following steps:\n\nConfigure LLM: Use the gpt-4-1106-preview model. Provide the OpenAI environment key through an environment variable or modify the code directly.\n\nSet Up Assistant Agent: Create it with a system prompt and the LLM configuration. Adjust as needed to improve outcomes.\n\nEstablish User Proxy Agent: These agents simulate users, interacting with Autogen agents. They include a function to end the process upon detecting the word \"Terminate,\" as specified in the system prompt.\n\n1\n\n2\n\n3\n\n4\n\n5\n\n6\n\n7\n\n8\n\n9\n\n10\n\n11\n\n12\n\n13\n\n14\n\n15\n\n16\n\n17\n\n18\n\n19\n\n20\n\n21\n\n22\n\n23\n\n24\n\n25\n\n26\n\n27\n\n28\n\n29\n\n30\n\n31\n\n32\n\n33\n\n34\n\nimport os\n\nfrom autogen import AssistantAgent, UserProxyAgent\n\nfrom composio\\_autogen import App, Action, ComposioToolset\n\nllm\\_config \\= {\n\n    \"config\\_list\": \\[\n\n        {\n\n            \"model\": \"gpt-4-1106-preview\",\n\n            \"api\\_key\": os.environ.get(\n\n                \"OPENAI\\_API\\_KEY\", \"sk-123131\\*\\*\\*\\*\"\n\n            ),\n\n        }\n\n    \\]\n\n}\n\nsuper\\_agent \\= AssistantAgent(\n\n    \"chatbot\",\n\n    system\\_message=\"\"\"You are a super intelligent personal assistant.\n\n    You have been given a set of tools that you are supposed to choose from.\n\n    You decide the right tool and execute it to achieve your task.\n\n    Reply TERMINATE when the task is done or when user's content is empty\"\"\",\n\n    llm\\_config=llm\\_config,\n\n)\n\n# create a UserProxyAgent instance named \"user\\_proxy\"\n\nuser\\_proxy \\= UserProxyAgent(\n\n    \"user\\_proxy\",\n\n    is\\_termination\\_msg=lambda x: x.get(\"content\", \"\")\n\n    and \"TERMINATE\" in x.get(\"content\", \"\"),\n\n    human\\_input\\_mode=\"NEVER\",  # Don't take input from User\n\n    code\\_execution\\_config={\"use\\_docker\": False},\n\n)\n\n### Powering agents with all Tools\n\n1\n\n2\n\n3\n\n4\n\n5\n\n6\n\n7\n\n# Initialise the Composio Tool Set\n\ncomposio\\_tools \\= ComposioToolset()\n\n# Register the preferred Applications, with right executor.\n\ncomposio\\_tools.register\\_tools(\n\n    tools=\\[App.LINEAR, App.GITHUB\\], caller=super\\_agent, executor=user\\_proxy\n\n)\n\n### Executing the Task\n\n1\n\n2\n\n3\n\n4\n\n5\n\n6\n\ntask \\= \"\"\"For all the todos in my last commit of SamparkAI/Docs,\n\ncreate a linear issue on project name hermes board and assign to right person\"\"\"\n\nresponse \\= user\\_proxy.initiate\\_chat(super\\_agent, message=task)\n\nprint(response.chat\\_history)\n\nWant to try out more -\\> docs.composio.dev\n------------------------------------------\n\n* * *\n\n* * *\n\nChat with us\n\nBook a demo\n\n* * *\n\nShortcuts\n\n[Documentation](https://deepnote.com/docs)[Deepnote crash course](https://deepnote.com/docs/deepnote-crash-course)[Explore](https://deepnote.com/explore)\n\n* * *\n\n[Roadmap](https://portal.productboard.com/deepnote/1-deepnote-product-portal/tabs/1-under-consideration)\n\nYou can **view** this project, but can’t make any changes.\n\nRequest additional access\n\nComment\n\nCan post and view comments in addition to inspecting the project.\n\nExecute\n\nCan execute code in addition to viewing and commenting, but cannot change anything or use terminals.\n\nEdit\n\nCan use terminals, connect integrations, comment and edit files as well as view and execute.\n\nView\n\nComment\n\nExecute\n\nEdit\n\nCollaborators\n\nOnly you and members of workspace **Composio** can view this project\n\nView collaborators\n\n![Image 9](https://t.co/i/adsct?bci=3&dv=UTC%26en-US%2Cen%26Google%20Inc.%26Win32%26255%26800%26600%264%2624%26800%26600%260%26na&eci=2&event_id=486a778a-a0da-44d7-bfb4-70743936a7c3&events=%5B%5B%22pageview%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=53796bef-9b54-4e71-98e2-ce633d2e5fe7&tw_document_href=https%3A%2F%2Fdeepnote.com%2Fworkspace%2Fcomposio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a%2Fproject%2FAgents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6%2Fnotebook%2FAutogen%2520Agent-cfb9253cd2c24de587bef8f7c6341c59&tw_iframe_status=0&tw_order_quantity=0&tw_sale_amount=0&txn_id=oc4iq&type=javascript&version=2.3.31)![Image 10](https://analytics.twitter.com/i/adsct?bci=3&dv=UTC%26en-US%2Cen%26Google%20Inc.%26Win32%26255%26800%26600%264%2624%26800%26600%260%26na&eci=2&event_id=486a778a-a0da-44d7-bfb4-70743936a7c3&events=%5B%5B%22pageview%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=53796bef-9b54-4e71-98e2-ce633d2e5fe7&tw_document_href=https%3A%2F%2Fdeepnote.com%2Fworkspace%2Fcomposio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a%2Fproject%2FAgents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6%2Fnotebook%2FAutogen%2520Agent-cfb9253cd2c24de587bef8f7c6341c59&tw_iframe_status=0&tw_order_quantity=0&tw_sale_amount=0&txn_id=oc4iq&type=javascript&version=2.3.31)\n\n![Image 11](https://bat.bing.com/action/0?ti=97113000&tm=gtm002&Ver=2&mid=0bb93771-ea67-4b78-b1d0-3babef35d5b9&bo=1&sid=c21ab0f0d74811ef91105d94ae47acef&vid=c2221280d74811efb8a711edc75de6e7&vids=1&msclkid=N&uach=pv%3D10.0&pi=918639831&lg=en-US&sw=800&sh=600&sc=24&p=https%3A%2F%2Fdeepnote.com%2Fworkspace%2Fcomposio-f87d-8ad9f1f9-a21a-4462-a4bb-174bde78f67a%2Fproject%2FAgents-Github-to-Linear-1e32fad6-0d9e-482b-b46d-08f868445ba6%2Fnotebook%2FAutogen%2520Agent-cfb9253cd2c24de587bef8f7c6341c59&r=&lt=2595&evt=pageLoad&sv=1&cdb=AQAQ&rn=847227)",
  "usage": {
    "tokens": 3446
  }
}
```
