---
title: Overview | ToolJet
description: Available on: Paid plans
url: https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com
timestamp: 2025-01-20T15:45:56.979Z
domain: docs.tooljet.com
path: docs_workflows_overview
---

# Overview | ToolJet


Available on: Paid plans


## Content

Available on: Paid plans

  

Introduction[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#introduction "Direct link to Introduction")
----------------------------------------------------------------------------------------------------------------------------------

ToolJet Workflows enable users to create complex, data-centric automations using a visual, node-based interface. It extends ToolJet's capabilities beyond building user interfaces, allowing developers and business users to automate processes, integrate data from various sources, and execute custom logic without writing extensive code.

![Image 20: Workflows Preview](https://docs.tooljet.com/img/workflows/overview/v2/workflows-preview.png)

Workflows complements the app-building features by providing a way to handle backend processes, data transformations, and integrations. This makes ToolJet a more comprehensive solution for creating internal tools and automations.

Create Your First Workflow[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#create-your-first-workflow "Direct link to Create Your First Workflow")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This guide will walk you through creating your first workflow in ToolJet. You'll learn how to use the Workflow builder to create a simple automated process that fetches data from a database, filters it, and sends notifications based on certain conditions.

### Accessing the Workflow Builder[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#accessing-the-workflow-builder "Direct link to Accessing the Workflow Builder")

*   Log in to your ToolJet account.
*   From the main dashboard, click on the **Workflows** icon in the left sidebar.
*   Click the **Create New Workflow** button to create a new workflow. Rename it to _sendEventNotification_.

### Step 1: Add a Database Query Node[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-1-add-a-database-query-node "Direct link to Step 1: Add a Database Query Node")

You'll start by fetching employee data from a ToolJetDB table named _employees_.

*   You'll see a **Start** node already on the canvas. This is the entry point of your workflow.
*   Create an outgoing node from the **Start** node, and select the **ToolJetDB** node. Rename the node to _getEmployees_.
*   Select Table name as _employees_ and Operation as List view.

![Image 21: Add a DB Query Node](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-1.png)

### Step 2: Transform Data Using RunJS Node[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-2-transform-data-using-runjs-node "Direct link to Step 2: Transform Data Using RunJS Node")

Next, you'll filter the employee data to include only those from California.

*   Create an outgoing node from the **Start** node, and select the **RunJS** node. Rename it to _filterEmployeeList_.
*   Enter the code below to filter out employees who are from California.

```
return getEmployees.data.filter(employee =>  employee.location === "California")
```

![Image 22: Transform Data Using RunJS](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-2.png)

### Step 3: Send Notifications[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-3-send-notifications "Direct link to Step 3: Send Notifications")

Next, you'll implement a loop to send SMS notifications to the filtered employees. The Loop node allows you to iterate through an array and perform an operation on each element.

*   Create an outgoing node from the **filterEmployeeList** node, and select the **Loop** node. Rename it to _sendSMS_.
*   Under Looped function, select **Twilio** as the data source. Configure the Operation as Send SMS, enter `{{value.number}}` in the To Number field.
*   Under the Body field, enter the following message:

```
Hey {{value.name}},Here's the link with all the details for today's ToolJet conference in California.https://tooljet.com/events/{{value.location}}
```

![Image 23: Send Notifications Through Twilio](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-3.png)

### Step 4: Configure the Response Node[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-4-configure-the-response-node "Direct link to Step 4: Configure the Response Node")

Finally, you'll set up conditions to handle the success or failure of the SMS sending process.

*   Create a new outgoing **If condition** node from the _sendSMS_ node.
*   Enter the code below in the input field: `sendSMS.status === "ok" ? true : false`
*   Create an outgoing **Response** node from the green arrow to configure the response when the **If condition** node returns true. Enter the following code to show the output as success when the SMS is successfully sent: `return ({output: "success"})`
*   Similarly, create an outgoing **Response** node from the red arrow to configure the response when the **If condition** node returns false. Enter the following code: `return ({output: "failure"})`

![Image 24: Configure The Response Node](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-4.png)

### Step 5: Executing the Workflow[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-5-executing-the-workflow "Direct link to Step 5: Executing the Workflow")

Click on the **Run** button on the top-right to execute the workflow. The logs panel will expand and provide an overview of all the nodes executed in this workflow.

![Image 25: Executing The Workflow](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-execution.png)

*   The **Input** section of the log will display all the incoming data to a node.

![Image 26: Input Logs](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-logs-input.png)

*   The **Output** section will display the data that is transferred to the next node while Logs will display the sequence of execution, and success and error messages.

![Image 27: Output Logs](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-logs-output.png)

Congratulations on creating your first workflow! This workflow fetches data, transforms the data, sends SMS notifications, and handles success or failure responses.

As you saw in this example, ToolJet Workflows provides a streamlined way to extend the capabilities of your ToolJet applications and automate complex processes.

## Metadata

```json
{
  "title": "Overview | ToolJet",
  "description": "Available on: Paid plans",
  "url": "https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com",
  "content": "Available on: Paid plans\n\n  \n\nIntroduction[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#introduction \"Direct link to Introduction\")\n----------------------------------------------------------------------------------------------------------------------------------\n\nToolJet Workflows enable users to create complex, data-centric automations using a visual, node-based interface. It extends ToolJet's capabilities beyond building user interfaces, allowing developers and business users to automate processes, integrate data from various sources, and execute custom logic without writing extensive code.\n\n![Image 20: Workflows Preview](https://docs.tooljet.com/img/workflows/overview/v2/workflows-preview.png)\n\nWorkflows complements the app-building features by providing a way to handle backend processes, data transformations, and integrations. This makes ToolJet a more comprehensive solution for creating internal tools and automations.\n\nCreate Your First Workflow[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#create-your-first-workflow \"Direct link to Create Your First Workflow\")\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nThis guide will walk you through creating your first workflow in ToolJet. You'll learn how to use the Workflow builder to create a simple automated process that fetches data from a database, filters it, and sends notifications based on certain conditions.\n\n### Accessing the Workflow Builder[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#accessing-the-workflow-builder \"Direct link to Accessing the Workflow Builder\")\n\n*   Log in to your ToolJet account.\n*   From the main dashboard, click on the **Workflows** icon in the left sidebar.\n*   Click the **Create New Workflow** button to create a new workflow. Rename it to _sendEventNotification_.\n\n### Step 1: Add a Database Query Node[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-1-add-a-database-query-node \"Direct link to Step 1: Add a Database Query Node\")\n\nYou'll start by fetching employee data from a ToolJetDB table named _employees_.\n\n*   You'll see a **Start** node already on the canvas. This is the entry point of your workflow.\n*   Create an outgoing node from the **Start** node, and select the **ToolJetDB** node. Rename the node to _getEmployees_.\n*   Select Table name as _employees_ and Operation as List view.\n\n![Image 21: Add a DB Query Node](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-1.png)\n\n### Step 2: Transform Data Using RunJS Node[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-2-transform-data-using-runjs-node \"Direct link to Step 2: Transform Data Using RunJS Node\")\n\nNext, you'll filter the employee data to include only those from California.\n\n*   Create an outgoing node from the **Start** node, and select the **RunJS** node. Rename it to _filterEmployeeList_.\n*   Enter the code below to filter out employees who are from California.\n\n```\nreturn getEmployees.data.filter(employee =>  employee.location === \"California\")\n```\n\n![Image 22: Transform Data Using RunJS](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-2.png)\n\n### Step 3: Send Notifications[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-3-send-notifications \"Direct link to Step 3: Send Notifications\")\n\nNext, you'll implement a loop to send SMS notifications to the filtered employees. The Loop node allows you to iterate through an array and perform an operation on each element.\n\n*   Create an outgoing node from the **filterEmployeeList** node, and select the **Loop** node. Rename it to _sendSMS_.\n*   Under Looped function, select **Twilio** as the data source. Configure the Operation as Send SMS, enter `{{value.number}}` in the To Number field.\n*   Under the Body field, enter the following message:\n\n```\nHey {{value.name}},Here's the link with all the details for today's ToolJet conference in California.https://tooljet.com/events/{{value.location}}\n```\n\n![Image 23: Send Notifications Through Twilio](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-3.png)\n\n### Step 4: Configure the Response Node[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-4-configure-the-response-node \"Direct link to Step 4: Configure the Response Node\")\n\nFinally, you'll set up conditions to handle the success or failure of the SMS sending process.\n\n*   Create a new outgoing **If condition** node from the _sendSMS_ node.\n*   Enter the code below in the input field: `sendSMS.status === \"ok\" ? true : false`\n*   Create an outgoing **Response** node from the green arrow to configure the response when the **If condition** node returns true. Enter the following code to show the output as success when the SMS is successfully sent: `return ({output: \"success\"})`\n*   Similarly, create an outgoing **Response** node from the red arrow to configure the response when the **If condition** node returns false. Enter the following code: `return ({output: \"failure\"})`\n\n![Image 24: Configure The Response Node](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-step-4.png)\n\n### Step 5: Executing the Workflow[​](https://docs.tooljet.com/docs/workflows/overview/?ref=blog.tooljet.com#step-5-executing-the-workflow \"Direct link to Step 5: Executing the Workflow\")\n\nClick on the **Run** button on the top-right to execute the workflow. The logs panel will expand and provide an overview of all the nodes executed in this workflow.\n\n![Image 25: Executing The Workflow](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-execution.png)\n\n*   The **Input** section of the log will display all the incoming data to a node.\n\n![Image 26: Input Logs](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-logs-input.png)\n\n*   The **Output** section will display the data that is transferred to the next node while Logs will display the sequence of execution, and success and error messages.\n\n![Image 27: Output Logs](https://docs.tooljet.com/img/workflows/overview/v2/event-notification-logs-output.png)\n\nCongratulations on creating your first workflow! This workflow fetches data, transforms the data, sends SMS notifications, and handles success or failure responses.\n\nAs you saw in this example, ToolJet Workflows provides a streamlined way to extend the capabilities of your ToolJet applications and automate complex processes.",
  "usage": {
    "tokens": 1445
  }
}
```
