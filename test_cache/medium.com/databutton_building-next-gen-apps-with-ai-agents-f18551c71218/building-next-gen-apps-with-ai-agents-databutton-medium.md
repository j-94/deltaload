---
title: Building Next-Gen Apps with AI Agents - Databutton - Medium
description: Assembling a dedicated development team for building internal apps is a substantial challenge — often facing the dilemma of needing technical expertise while being constrained by tight budgets…
url: https://medium.com/databutton/building-next-gen-apps-with-ai-agents-f18551c71218
timestamp: 2025-01-20T15:54:26.241Z
domain: medium.com
path: databutton_building-next-gen-apps-with-ai-agents-f18551c71218
---

# Building Next-Gen Apps with AI Agents - Databutton - Medium


Assembling a dedicated development team for building internal apps is a substantial challenge — often facing the dilemma of needing technical expertise while being constrained by tight budgets…


## Content

For businesses that want to become efficient and win with the use of custom internal tools and automation.
----------------------------------------------------------------------------------------------------------

[![Image 37: Avra](https://miro.medium.com/v2/resize:fill:44:44/1*Ga_IDbe0WKLWxRNAyEUxkQ.jpeg)](https://medium.com/@avra42?source=post_page---byline--f18551c71218--------------------------------)

[![Image 38: Databutton](https://miro.medium.com/v2/resize:fill:24:24/1*hAZCWO0a7sPekyjfeMAfyg.png)](https://medium.com/databutton?source=post_page---byline--f18551c71218--------------------------------)

> [Can’t view the full article? Try this friend link !](https://medium.com/databutton/building-next-gen-apps-with-ai-agents-f18551c71218?sk=a3a982a1dbdcb3486273d22f1917f318)

Assembling a dedicated development team for building internal apps is a substantial challenge — often facing the dilemma of needing technical expertise while being constrained by tight budgets.

Hiring even a small team of two to five skilled members can be financially taxing. Moreover, the complexity of developing and maintaining an app that aligns with specific requirements from concept to launch can be overwhelming. This is precisely where the concept of building AI-powered web apps through a conversation can be a game-changer.

> The no-code movement changed the world by creating a generation of non-technical builders through amazingly well-built products. Now, a new era of no-code is about to begin and — similarly — will be driven by excellent tools enabling non-technical people to build. — [Trygve Karper](https://medium.com/u/eb3407f59020?source=post_page---user_mention--f18551c71218--------------------------------)

[![Image 39](https://miro.medium.com/v2/resize:fit:700/1*T1Jgwa994PtszbgtKd6riA.png)](https://databutton.typeform.com/to/GOQ6yPCh?utm_source=medium&utm_medium=avra&utm_campaign=buildingnextgenapps&typeform-source=www.medium.com)

This is where Databutton comes in — a platform that simplifies app creation, making it conversational and operationally-ready. It introduces a unique approach with two AI agents, Brain and Builder, collaborating in the app development process.

These agents work together, utilizing the latest AI stacks to seamlessly integrate Python and ReactJS. Think of these agents as your development companions, guiding you through each step, allowing you to focus on refining your ideas and solving important problems.

![Image 40](https://miro.medium.com/v2/resize:fit:700/1*SaIBmQjcaaOtUVlJxUaDLg.png)

Let’s explore the workflow of Databutton in building such AI-powered web apps via prompting. We will see how its intuitive, conversation-driven process can efficiently produce internal tools ready for business use.

💡 Ideation Phase
-----------------

It’s all about brainstorming your app’s concept based on your business need. Think of it as the time to throw your ideas into the mix. For example, you might come up with:

> “_I want to create an app that can analyze insurance claim images, describe them, and give an initial damage estimate._”

or maybe…

> “I_’d like to fetch all the data from my user feedback Google Sheet and use AI to categorize and rank it._”

This is the stage where any idea, big or small — starts taking shape!

![Image 41](https://miro.medium.com/v2/resize:fit:700/1*mRkoTeiozRAFiS554sO56g.png)

Once your idea is conveyed, the Databutton’s Ideation Agent takes over. You will get a range of ideas, let’s call them “capabilities” — and your job is to pick the ones that might come in handy while building the app.

It’s all about finding the perfect capabilities for what you envision.

![Image 42](https://miro.medium.com/v2/resize:fit:700/1*IcVT4IA81a0p7OxceA9n6w.png)

🧠 Brain Building Phase
-----------------------

In brief, during the brain-building phase, the main goal is to convert all selected capabilities into functional endpoints by **building a FastAPI endpoint for each of the capabilities.**

The brain agent not only constructs functional endpoints but also handles multiple crucial aspects while translating our daily conversations into Python code.

Here’s a closer look at each step performed by the Brain Agent while building any capabilities:

*   **App Blueprinting**: The agent initially outlines and confirms the essential tasks with the end user to achieve the final goal i.e. building all the endpoints. For example, when developing an app for image analysis using OpenAI’s large language model, the Brain Agent first reviews and confirms a comprehensive task list (see image below for the complete task list). Note that, these tasks are subject to multiple iterations, and the agent will update them accordingly throughout the app-building process.

![Image 43](https://miro.medium.com/v2/resize:fit:700/1*oQ3BeoygbZmba5L78KQeAA.png)

*   **Secret Management and Data Storage**: The Brain Agent is fully aware of all the Databutton endpoints and various libraries. This includes [Databutton endpoints](https://docs.databutton.com/) such as `secrets`, storage-related APIs `fetch` and `get`methods. The agent self-executes necessary tasks, such as storing API keys or uploading files to the Databutton storage.

![Image 44](https://miro.medium.com/v2/resize:fit:700/1*O2YqcAUoFgYZCY7vV3xAWw.png)

*   **Collaborative** **Self-Executing**: The Brain Agent is adept at autonomously writing and executing Python code in a Jupyter notebook-like environment. Whenever it encounters a problem or bugs — it identifies the underlying issue, displays it, and engages in constant communication with the end-user. Consider it a continuous developer assistant throughout the coding process!

![Image 45](https://miro.medium.com/v2/resize:fit:700/1*tDFVFKXykLcv-9iEnWfSJw.gif)

*   **Functional Endpoints:** Every capability is finalized as a functional FastAPI endpoint. The agent could achieve this in no time, preparing for the next phase — making the endpoint available for the UI developer agent.

![Image 46](https://miro.medium.com/v2/resize:fit:700/1*HnxTcEKw4T7gZ3eZNp_0Lg.gif)

For the sake of simplicity, we will focus on a single capability.

> In Databutton, the code is always editable and serves as the foundational truth for any application. Yet, as we’ve observed, there’s no need to write any code to develop such capabilities.

If we look at the code generated by the Brain Agent, it is worth noting that at the backend — the `databutton_app` module is responsible for directing requests and data to the corresponding destinations in the front end.

....  
from pydantic import BaseModel  
from databutton\_app import router  
import databutton as db  
....

Now, let’s move on to the UI-building phase to use the capability we have just developed!

🛠️ UI Building Phase
---------------------

The focus of UI building is not just on rapidly spinning up a powerful, React-based interface, but also on ensuring that the backend capabilities are seamlessly integrated to form a functional web app conversationally.

![Image 47](https://miro.medium.com/v2/resize:fit:700/1*f6cnhNFE56dKgk47GEjV9Q.png)

*   **👷🏽‍♂️ Building the UI:** Similar to the Brain Agent’s approach, the Builder Agent meticulously addresses each aspect to craft a well-designed UI, bridging backend functionalities with a user-centric front-end design. Alternatively, we can prompt any layouts that we would like our Builder Agent to consider.

![Image 48](https://miro.medium.com/v2/resize:fit:700/1*l_5sf4Yo6-gS7BYaInEt_A.png)

*   **♻️ Changing or Adding Components:** The Builder Agent allows flexibility and customization based on user requirements. For example, implementing a simple text input box for URLs or an ‘Analyze’ button for UI enhancement. Additionally, we could build our custom components and direct the agent to use them!

![Image 49](https://miro.medium.com/v2/resize:fit:700/1*CWAYItGv5pOB2WDIc2BrNQ.gif)

*   🔗 **Bridging the back-end capabilities:** A key task of the Builder Agent is to integrate the functional endpoints with the front end. This can be easily directed to the agent by simply tagging the capability using the hash # symbol in the prompt with a brief reference for implementation. From there on, the Agent is smart at understanding which parameters or return objects should be considered.

![Image 50](https://miro.medium.com/v2/resize:fit:700/1*F5FLie2QDfM0DpxcUEAuwQ.png)

**Understanding Integration with FastAPI Endpoints:** With such intuitive prompting, activating the UI functionality becomes straightforward! Now, let’s try to look into the code, on how the FastAPI endpoints from the Brain are integrated into the UI. Below is the code specific to this implementation:

import React, { useState } from "react";  
import brain from "./brain";  
...

The custom library named `brain`, is designed to handle backend capabilities, integrating them with the React front end of the application. This module includes functions specific to interacting with the backend FastAPI service. For instance,

....  
const response = await brain.ai\_image\_analysis({ image\_url: imageUrl });  
      const data = await response.json();  
      setAnalysisResult(data.description);  
....

🚀 Functional App
-----------------

![Image 51](https://miro.medium.com/v2/resize:fit:700/1*QKfAzreVPPW3LMYseyavCg.png)

With a slight adjustment to the prompt in the capability, one can obtain a comprehensive response from any image. This specific case is for insurance claims analysis.

**Here’s the full response from the AI:**  
_The image shows a room in a residential house with a significant amount of flooding. The water level appears to be around knee-height, submerging the lower section of furniture, including a bookshelf, a television and its stand, as well as impacting the walls. Visible electrical outlets are under water, posing an electrical hazard. The water appears to be still, indicating that the flooding might not be currently active, but the damage is already done. Considering the visible water level and the potential for extensive damage, the cost of repairs could be substantial. This would likely involve water extraction, drying, potential mold remediation, replacing damaged drywall, electrical systems, and flooring, as well as repairing or replacing furniture and other personal items. Without knowledge of the room size, local labor and material costs, it is challenging to provide an accurate estimate. However, as a very rough preliminary estimate, repairs and replacements could range from $20,000 to $50,000 or more, depending on the room size, local costs, and whether there is structural damage hidden behind the walls or under the flooring. This assumes a full professional restoration service is used and that multiple rooms may have similar damage if the flooding is extensive throughout the house. Note that an actual settlement would require a detailed assessment by a professional, considering the specific policy coverage, deductible, limits, and potential depreciation of the damaged property._

If building apps leveraging the power of generative AI is interesting to you, sign up at [www.databutton.com](http://databutton.com/login?utm_source=medium&utm_medium=viral&utm_article=nextgenapps) and let us know what you think on [Discord](https://discord.gg/K9aHvmmFtH)!

**Watch the full app-building process:**
----------------------------------------

## Metadata

```json
{
  "title": "Building Next-Gen Apps with AI Agents - Databutton - Medium",
  "description": "Assembling a dedicated development team for building internal apps is a substantial challenge — often facing the dilemma of needing technical expertise while being constrained by tight budgets…",
  "url": "https://medium.com/databutton/building-next-gen-apps-with-ai-agents-f18551c71218",
  "content": "For businesses that want to become efficient and win with the use of custom internal tools and automation.\n----------------------------------------------------------------------------------------------------------\n\n[![Image 37: Avra](https://miro.medium.com/v2/resize:fill:44:44/1*Ga_IDbe0WKLWxRNAyEUxkQ.jpeg)](https://medium.com/@avra42?source=post_page---byline--f18551c71218--------------------------------)\n\n[![Image 38: Databutton](https://miro.medium.com/v2/resize:fill:24:24/1*hAZCWO0a7sPekyjfeMAfyg.png)](https://medium.com/databutton?source=post_page---byline--f18551c71218--------------------------------)\n\n> [Can’t view the full article? Try this friend link !](https://medium.com/databutton/building-next-gen-apps-with-ai-agents-f18551c71218?sk=a3a982a1dbdcb3486273d22f1917f318)\n\nAssembling a dedicated development team for building internal apps is a substantial challenge — often facing the dilemma of needing technical expertise while being constrained by tight budgets.\n\nHiring even a small team of two to five skilled members can be financially taxing. Moreover, the complexity of developing and maintaining an app that aligns with specific requirements from concept to launch can be overwhelming. This is precisely where the concept of building AI-powered web apps through a conversation can be a game-changer.\n\n> The no-code movement changed the world by creating a generation of non-technical builders through amazingly well-built products. Now, a new era of no-code is about to begin and — similarly — will be driven by excellent tools enabling non-technical people to build. — [Trygve Karper](https://medium.com/u/eb3407f59020?source=post_page---user_mention--f18551c71218--------------------------------)\n\n[![Image 39](https://miro.medium.com/v2/resize:fit:700/1*T1Jgwa994PtszbgtKd6riA.png)](https://databutton.typeform.com/to/GOQ6yPCh?utm_source=medium&utm_medium=avra&utm_campaign=buildingnextgenapps&typeform-source=www.medium.com)\n\nThis is where Databutton comes in — a platform that simplifies app creation, making it conversational and operationally-ready. It introduces a unique approach with two AI agents, Brain and Builder, collaborating in the app development process.\n\nThese agents work together, utilizing the latest AI stacks to seamlessly integrate Python and ReactJS. Think of these agents as your development companions, guiding you through each step, allowing you to focus on refining your ideas and solving important problems.\n\n![Image 40](https://miro.medium.com/v2/resize:fit:700/1*SaIBmQjcaaOtUVlJxUaDLg.png)\n\nLet’s explore the workflow of Databutton in building such AI-powered web apps via prompting. We will see how its intuitive, conversation-driven process can efficiently produce internal tools ready for business use.\n\n💡 Ideation Phase\n-----------------\n\nIt’s all about brainstorming your app’s concept based on your business need. Think of it as the time to throw your ideas into the mix. For example, you might come up with:\n\n> “_I want to create an app that can analyze insurance claim images, describe them, and give an initial damage estimate._”\n\nor maybe…\n\n> “I_’d like to fetch all the data from my user feedback Google Sheet and use AI to categorize and rank it._”\n\nThis is the stage where any idea, big or small — starts taking shape!\n\n![Image 41](https://miro.medium.com/v2/resize:fit:700/1*mRkoTeiozRAFiS554sO56g.png)\n\nOnce your idea is conveyed, the Databutton’s Ideation Agent takes over. You will get a range of ideas, let’s call them “capabilities” — and your job is to pick the ones that might come in handy while building the app.\n\nIt’s all about finding the perfect capabilities for what you envision.\n\n![Image 42](https://miro.medium.com/v2/resize:fit:700/1*IcVT4IA81a0p7OxceA9n6w.png)\n\n🧠 Brain Building Phase\n-----------------------\n\nIn brief, during the brain-building phase, the main goal is to convert all selected capabilities into functional endpoints by **building a FastAPI endpoint for each of the capabilities.**\n\nThe brain agent not only constructs functional endpoints but also handles multiple crucial aspects while translating our daily conversations into Python code.\n\nHere’s a closer look at each step performed by the Brain Agent while building any capabilities:\n\n*   **App Blueprinting**: The agent initially outlines and confirms the essential tasks with the end user to achieve the final goal i.e. building all the endpoints. For example, when developing an app for image analysis using OpenAI’s large language model, the Brain Agent first reviews and confirms a comprehensive task list (see image below for the complete task list). Note that, these tasks are subject to multiple iterations, and the agent will update them accordingly throughout the app-building process.\n\n![Image 43](https://miro.medium.com/v2/resize:fit:700/1*oQ3BeoygbZmba5L78KQeAA.png)\n\n*   **Secret Management and Data Storage**: The Brain Agent is fully aware of all the Databutton endpoints and various libraries. This includes [Databutton endpoints](https://docs.databutton.com/) such as `secrets`, storage-related APIs `fetch` and `get`methods. The agent self-executes necessary tasks, such as storing API keys or uploading files to the Databutton storage.\n\n![Image 44](https://miro.medium.com/v2/resize:fit:700/1*O2YqcAUoFgYZCY7vV3xAWw.png)\n\n*   **Collaborative** **Self-Executing**: The Brain Agent is adept at autonomously writing and executing Python code in a Jupyter notebook-like environment. Whenever it encounters a problem or bugs — it identifies the underlying issue, displays it, and engages in constant communication with the end-user. Consider it a continuous developer assistant throughout the coding process!\n\n![Image 45](https://miro.medium.com/v2/resize:fit:700/1*tDFVFKXykLcv-9iEnWfSJw.gif)\n\n*   **Functional Endpoints:** Every capability is finalized as a functional FastAPI endpoint. The agent could achieve this in no time, preparing for the next phase — making the endpoint available for the UI developer agent.\n\n![Image 46](https://miro.medium.com/v2/resize:fit:700/1*HnxTcEKw4T7gZ3eZNp_0Lg.gif)\n\nFor the sake of simplicity, we will focus on a single capability.\n\n> In Databutton, the code is always editable and serves as the foundational truth for any application. Yet, as we’ve observed, there’s no need to write any code to develop such capabilities.\n\nIf we look at the code generated by the Brain Agent, it is worth noting that at the backend — the `databutton_app` module is responsible for directing requests and data to the corresponding destinations in the front end.\n\n....  \nfrom pydantic import BaseModel  \nfrom databutton\\_app import router  \nimport databutton as db  \n....\n\nNow, let’s move on to the UI-building phase to use the capability we have just developed!\n\n🛠️ UI Building Phase\n---------------------\n\nThe focus of UI building is not just on rapidly spinning up a powerful, React-based interface, but also on ensuring that the backend capabilities are seamlessly integrated to form a functional web app conversationally.\n\n![Image 47](https://miro.medium.com/v2/resize:fit:700/1*f6cnhNFE56dKgk47GEjV9Q.png)\n\n*   **👷🏽‍♂️ Building the UI:** Similar to the Brain Agent’s approach, the Builder Agent meticulously addresses each aspect to craft a well-designed UI, bridging backend functionalities with a user-centric front-end design. Alternatively, we can prompt any layouts that we would like our Builder Agent to consider.\n\n![Image 48](https://miro.medium.com/v2/resize:fit:700/1*l_5sf4Yo6-gS7BYaInEt_A.png)\n\n*   **♻️ Changing or Adding Components:** The Builder Agent allows flexibility and customization based on user requirements. For example, implementing a simple text input box for URLs or an ‘Analyze’ button for UI enhancement. Additionally, we could build our custom components and direct the agent to use them!\n\n![Image 49](https://miro.medium.com/v2/resize:fit:700/1*CWAYItGv5pOB2WDIc2BrNQ.gif)\n\n*   🔗 **Bridging the back-end capabilities:** A key task of the Builder Agent is to integrate the functional endpoints with the front end. This can be easily directed to the agent by simply tagging the capability using the hash # symbol in the prompt with a brief reference for implementation. From there on, the Agent is smart at understanding which parameters or return objects should be considered.\n\n![Image 50](https://miro.medium.com/v2/resize:fit:700/1*F5FLie2QDfM0DpxcUEAuwQ.png)\n\n**Understanding Integration with FastAPI Endpoints:** With such intuitive prompting, activating the UI functionality becomes straightforward! Now, let’s try to look into the code, on how the FastAPI endpoints from the Brain are integrated into the UI. Below is the code specific to this implementation:\n\nimport React, { useState } from \"react\";  \nimport brain from \"./brain\";  \n...\n\nThe custom library named `brain`, is designed to handle backend capabilities, integrating them with the React front end of the application. This module includes functions specific to interacting with the backend FastAPI service. For instance,\n\n....  \nconst response = await brain.ai\\_image\\_analysis({ image\\_url: imageUrl });  \n      const data = await response.json();  \n      setAnalysisResult(data.description);  \n....\n\n🚀 Functional App\n-----------------\n\n![Image 51](https://miro.medium.com/v2/resize:fit:700/1*QKfAzreVPPW3LMYseyavCg.png)\n\nWith a slight adjustment to the prompt in the capability, one can obtain a comprehensive response from any image. This specific case is for insurance claims analysis.\n\n**Here’s the full response from the AI:**  \n_The image shows a room in a residential house with a significant amount of flooding. The water level appears to be around knee-height, submerging the lower section of furniture, including a bookshelf, a television and its stand, as well as impacting the walls. Visible electrical outlets are under water, posing an electrical hazard. The water appears to be still, indicating that the flooding might not be currently active, but the damage is already done. Considering the visible water level and the potential for extensive damage, the cost of repairs could be substantial. This would likely involve water extraction, drying, potential mold remediation, replacing damaged drywall, electrical systems, and flooring, as well as repairing or replacing furniture and other personal items. Without knowledge of the room size, local labor and material costs, it is challenging to provide an accurate estimate. However, as a very rough preliminary estimate, repairs and replacements could range from $20,000 to $50,000 or more, depending on the room size, local costs, and whether there is structural damage hidden behind the walls or under the flooring. This assumes a full professional restoration service is used and that multiple rooms may have similar damage if the flooding is extensive throughout the house. Note that an actual settlement would require a detailed assessment by a professional, considering the specific policy coverage, deductible, limits, and potential depreciation of the damaged property._\n\nIf building apps leveraging the power of generative AI is interesting to you, sign up at [www.databutton.com](http://databutton.com/login?utm_source=medium&utm_medium=viral&utm_article=nextgenapps) and let us know what you think on [Discord](https://discord.gg/K9aHvmmFtH)!\n\n**Watch the full app-building process:**\n----------------------------------------",
  "publishedTime": "2024-01-12T05:40:48.797Z",
  "usage": {
    "tokens": 2621
  }
}
```
