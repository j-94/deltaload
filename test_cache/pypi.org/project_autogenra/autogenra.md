---
title: autogenra
description: Autogen Assistant UI
url: https://pypi.org/project/autogenra/
timestamp: 2025-01-20T15:50:41.465Z
domain: pypi.org
path: project_autogenra
---

# autogenra


Autogen Assistant UI


## Content

AutoGen Assistant
-----------------

![Image 26: ARA](https://pypi-camo.freetls.fastly.net/a32606e4ad808ef641ce363eaf2aca13f1a7f675/2e2f646f63732f6172615f73746f636b7072696365732e706e67)

AutoGen Assistant is an Autogen-powered AI app (user interface) that can converse with you to help you conduct research, write and execute code, run saved skills, create new skills (explicitly and by demonstration), and adapt in response to your interactions.

### Capabilities / Roadmap

Some of the capabilities supported by the app frontend include the following:

*   Select fron a list of agents (current support for two agent workflows - `UserProxyAgent` and `AssistantAgent`)
*   Modify agent configuration (e.g. temperature, model, agent system message, model etc) and chat with updated agent configurations.
*   View agent messages and output files in the UI from agent runs.
*   Support for more complex agent workflows (e.g. `GroupChat` workflows)
*   Improved user experience (e.g., streaming intermediate model output, better summarization of agent responses, etc)

Project Structure:

*   _autogenra/_ code for the backend classes and web api (FastAPI)
*   _frontend/_ code for the webui, built with Gatsby and Tailwind

### Installation

1.  **Install from PyPi**
    
    We recommend using a virtual environment (e.g., conda) to avoid conflicts with existing Python packages. With Python 3.10 or newer active in your virtual environment, use pip to install AutoGen Assistant:
    
    pip install autogenra
    
2.  **Install from Source**
    
    > Note: This approach requires some familiarity with building interfaces in React.
    
    If you prefer to install from source, ensure you have Python 3.10+ and Node.js (version above 14.15.0) installed. Here's how you get started:
    
    *   Clone the AutoGen Assistant repository and install its Python dependencies:
        
        pip install \-e .
        
    *   Navigate to the `samples/apps/autogen-assistant/frontend` directory, install dependencies, and build the UI:
        
        npm install \-g gatsby-cli
        npm install \--global yarn
        cd frontend
        yarn install
        yarn build
        
    
    For Windows users, to build the frontend, you may need alternative commands to build the frontend.
    
    `````
    ```bash
    
    gatsby clean && rmdir /s /q ..\\autogenra\\web\\ui && (set \"PREFIX_PATH_VALUE=\" || ver>nul) && gatsby build --prefix-paths && xcopy /E /I /Y public ..\\autogenra\\web\\ui
    
    ````
    `````
    

### Running the Application

Once installed, run the web UI by entering the following in your terminal:

autogenra ui \--port 8081

This will start the application on the specified port. Open your web browser and go to `http://localhost:8081/` to begin using AutoGen Assistant.

Now that you have AutoGen Assistant installed and running, you are ready to explore its capabilities, including defining and modifying agent workflows, interacting with agents and sessions, and expanding agent skills.

Capabilities
------------

This demo focuses on the research assistant use case with some generalizations:

*   **Skills**: The agent is provided with a list of skills that it can leverage while attempting to address a user's query. Each skill is a python function that may be in any file in a folder made availabe to the agents. We separate the concept of global skills available to all agents `backend/files/global_utlis_dir` and user level skills `backend/files/user/<user_hash>/utils_dir`, relevant in a multi user environment. Agents are aware skills as they are appended to the system message. A list of example skills is available in the `backend/global_utlis_dir` folder. Modify the file or create a new file with a function in the same directory to create new global skills.
    
*   **Conversation Persistence**: Conversation history is persisted in an sqlite database `database.sqlite`.
    
*   **Default Agent Workflow**: The default a sample workflow with two agents - a user proxy agent and an assistant agent.
    

Example Usage
-------------

Let us use a simple query demonstrating the capabilities of the research assistant.

```
Plot a chart of NVDA and TESLA stock price YTD. Save the result to a file named nvda_tesla.png
```

The agents responds by _writing and executing code_ to create a python program to generate the chart with the stock prices.

> Note than there could be multiple turns between the `AssistantAgent` and the `UserProxyAgent` to produce and execute the code in order to complete the task.

![Image 27: ARA](https://pypi-camo.freetls.fastly.net/a32606e4ad808ef641ce363eaf2aca13f1a7f675/2e2f646f63732f6172615f73746f636b7072696365732e706e67)

> Note: You can also view the debug console that generates useful information to see how the agents are interacting in the background.

FAQ
---

**Q: How can I add more skills to the AutoGen Assistant?** A: You can extend the capabilities of your agents by adding new Python functions. The AutoGen Assistant interface also lets you directly paste functions that can be reused in the agent workflow.

**Q: Where can I adjust the agent configurations and settings?** A: You can modify agent configurations directly from the UI or by editing the default configurations in the `utils.py` file under the `get_default_agent_config()` method (assuming you are building your own UI).

**Q: If I want to reset the conversation with an agent, how do I go about it?** A: To reset your conversation history, you can delete the `database.sqlite` file. If you need to clear user-specific data, remove the relevant `autogenra/web/files/user/<user_id_md5hash>` folder.

**Q: Is it possible to view the output and messages generated by the agents during interactions?** A: Yes, you can view the generated messages in the debug console of the web UI, providing insights into the agent interactions. Alternatively, you can inspect the `database.sqlite` file for a comprehensive record of messages.

Acknowledgements
----------------

AutoGen assistant is Based on the [AutoGen](https://microsoft.github.io/autogen) project. It is adapted in October 2023 from a research prototype (original credits: Gagan Bansal, Adam Fourney, Victor Dibia, Piali Choudhury, Saleema Amershi, Ahmed Awadallah, Chi Wang)

## Metadata

```json
{
  "title": "autogenra",
  "description": "Autogen Assistant UI",
  "url": "https://pypi.org/project/autogenra/",
  "content": "AutoGen Assistant\n-----------------\n\n![Image 26: ARA](https://pypi-camo.freetls.fastly.net/a32606e4ad808ef641ce363eaf2aca13f1a7f675/2e2f646f63732f6172615f73746f636b7072696365732e706e67)\n\nAutoGen Assistant is an Autogen-powered AI app (user interface) that can converse with you to help you conduct research, write and execute code, run saved skills, create new skills (explicitly and by demonstration), and adapt in response to your interactions.\n\n### Capabilities / Roadmap\n\nSome of the capabilities supported by the app frontend include the following:\n\n*   Select fron a list of agents (current support for two agent workflows - `UserProxyAgent` and `AssistantAgent`)\n*   Modify agent configuration (e.g. temperature, model, agent system message, model etc) and chat with updated agent configurations.\n*   View agent messages and output files in the UI from agent runs.\n*   Support for more complex agent workflows (e.g. `GroupChat` workflows)\n*   Improved user experience (e.g., streaming intermediate model output, better summarization of agent responses, etc)\n\nProject Structure:\n\n*   _autogenra/_ code for the backend classes and web api (FastAPI)\n*   _frontend/_ code for the webui, built with Gatsby and Tailwind\n\n### Installation\n\n1.  **Install from PyPi**\n    \n    We recommend using a virtual environment (e.g., conda) to avoid conflicts with existing Python packages. With Python 3.10 or newer active in your virtual environment, use pip to install AutoGen Assistant:\n    \n    pip install autogenra\n    \n2.  **Install from Source**\n    \n    > Note: This approach requires some familiarity with building interfaces in React.\n    \n    If you prefer to install from source, ensure you have Python 3.10+ and Node.js (version above 14.15.0) installed. Here's how you get started:\n    \n    *   Clone the AutoGen Assistant repository and install its Python dependencies:\n        \n        pip install \\-e .\n        \n    *   Navigate to the `samples/apps/autogen-assistant/frontend` directory, install dependencies, and build the UI:\n        \n        npm install \\-g gatsby-cli\n        npm install \\--global yarn\n        cd frontend\n        yarn install\n        yarn build\n        \n    \n    For Windows users, to build the frontend, you may need alternative commands to build the frontend.\n    \n    `````\n    ```bash\n    \n    gatsby clean && rmdir /s /q ..\\\\autogenra\\\\web\\\\ui && (set \\\"PREFIX_PATH_VALUE=\\\" || ver>nul) && gatsby build --prefix-paths && xcopy /E /I /Y public ..\\\\autogenra\\\\web\\\\ui\n    \n    ````\n    `````\n    \n\n### Running the Application\n\nOnce installed, run the web UI by entering the following in your terminal:\n\nautogenra ui \\--port 8081\n\nThis will start the application on the specified port. Open your web browser and go to `http://localhost:8081/` to begin using AutoGen Assistant.\n\nNow that you have AutoGen Assistant installed and running, you are ready to explore its capabilities, including defining and modifying agent workflows, interacting with agents and sessions, and expanding agent skills.\n\nCapabilities\n------------\n\nThis demo focuses on the research assistant use case with some generalizations:\n\n*   **Skills**: The agent is provided with a list of skills that it can leverage while attempting to address a user's query. Each skill is a python function that may be in any file in a folder made availabe to the agents. We separate the concept of global skills available to all agents `backend/files/global_utlis_dir` and user level skills `backend/files/user/<user_hash>/utils_dir`, relevant in a multi user environment. Agents are aware skills as they are appended to the system message. A list of example skills is available in the `backend/global_utlis_dir` folder. Modify the file or create a new file with a function in the same directory to create new global skills.\n    \n*   **Conversation Persistence**: Conversation history is persisted in an sqlite database `database.sqlite`.\n    \n*   **Default Agent Workflow**: The default a sample workflow with two agents - a user proxy agent and an assistant agent.\n    \n\nExample Usage\n-------------\n\nLet us use a simple query demonstrating the capabilities of the research assistant.\n\n```\nPlot a chart of NVDA and TESLA stock price YTD. Save the result to a file named nvda_tesla.png\n```\n\nThe agents responds by _writing and executing code_ to create a python program to generate the chart with the stock prices.\n\n> Note than there could be multiple turns between the `AssistantAgent` and the `UserProxyAgent` to produce and execute the code in order to complete the task.\n\n![Image 27: ARA](https://pypi-camo.freetls.fastly.net/a32606e4ad808ef641ce363eaf2aca13f1a7f675/2e2f646f63732f6172615f73746f636b7072696365732e706e67)\n\n> Note: You can also view the debug console that generates useful information to see how the agents are interacting in the background.\n\nFAQ\n---\n\n**Q: How can I add more skills to the AutoGen Assistant?** A: You can extend the capabilities of your agents by adding new Python functions. The AutoGen Assistant interface also lets you directly paste functions that can be reused in the agent workflow.\n\n**Q: Where can I adjust the agent configurations and settings?** A: You can modify agent configurations directly from the UI or by editing the default configurations in the `utils.py` file under the `get_default_agent_config()` method (assuming you are building your own UI).\n\n**Q: If I want to reset the conversation with an agent, how do I go about it?** A: To reset your conversation history, you can delete the `database.sqlite` file. If you need to clear user-specific data, remove the relevant `autogenra/web/files/user/<user_id_md5hash>` folder.\n\n**Q: Is it possible to view the output and messages generated by the agents during interactions?** A: Yes, you can view the generated messages in the debug console of the web UI, providing insights into the agent interactions. Alternatively, you can inspect the `database.sqlite` file for a comprehensive record of messages.\n\nAcknowledgements\n----------------\n\nAutoGen assistant is Based on the [AutoGen](https://microsoft.github.io/autogen) project. It is adapted in October 2023 from a research prototype (original credits: Gagan Bansal, Adam Fourney, Victor Dibia, Piali Choudhury, Saleema Amershi, Ahmed Awadallah, Chi Wang)",
  "usage": {
    "tokens": 1444
  }
}
```
